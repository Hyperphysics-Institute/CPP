#!/usr/bin/env python3
"""
build_osf_queue.py — maintain osf_deposit_queue.md, the running deposit list.

Registered Patch 3215.

THE CARRY-FORWARD CONTRACT, which is the whole point of this script:
Isak owns three columns -- POSTED, OSF LINK, NOTES. This script regenerates
everything else from the repository, but it NEVER overwrites those three. They
are read back from the existing queue and matched by exact .tex path, so the
file can be regenerated after every patch without losing a single thing Isak
recorded. If a paper is renamed or moved, its row is re-keyed and the carried
columns would be lost, so renames are reported loudly rather than silently
dropped.

Isak's workflow: deposit a paper, then fill POSTED with the date and OSF LINK
with the DOI or URL. Re-run this script (or ask for it to be re-run) after any
patch; new and changed papers appear, and existing entries keep their notes.

WITHHELD rows are listed FIRST and never omitted. A paper that must not be
deposited is more dangerous missing from the list than present on it, because
an absent row invites someone to add it back from another source.

Usage:  python3 code/build_osf_queue.py
"""

import io
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(REPO, "osf_deposit_queue.md")
MANIFEST = os.path.join(REPO, "osf_deposit_manifest.json")
EXCLUDE = ("archive/", "/duplicates/", "duplicates/", "/development/")

# Phrases that mean DO NOT DEPOSIT. NOT-FOR-RELEASE is here because the
# readiness checker's original wording list missed it, leaving DM-1 and DM-3 --
# both founder-attested kills -- sitting in the publishable set.
WITHHOLD = [
    (r"NOT-FOR-RELEASE|NOT FOR RELEASE|DO NOT PUBLISH",
     "founder-attested: retained as record, not for release"),
    # Match the scaffolding CONVENTIONS (%%TODO, "TODO:", \todo, FIXME) and
    # NOT a bare "TODO", which also matches registry item IDs like TODO-012 --
    # several of which are explicitly marked "(cleared)". A bare-word pattern
    # withheld SF-2 (a shipped v1.01 flagship), its companion, SS-1f and
    # theo_chir_audit_1 on nothing but citations of closed todolist entries.
    (r"%%TODO|\bTODO:|\\todo\b|\bFIXME\b",
     "unfinished: live TODO/FIXME scaffolding markers"),
    (r"v0 placeholder|STATUS:\s*PLACEHOLDER",
     "unfinished: declares itself a placeholder"),
]

CLASSES = [
    ("flagship_papers/", "Flagship"),
    ("hardened_theorems/", "Theorem artifact"),
    ("chirality_", "Chirality derivation"),
    ("SR_companion", "Companion"),
]


def strip_comments(t):
    t = re.sub(r"% BEGIN GENERATED IDENTIFIER APPENDIX.*?"
               r"% END GENERATED IDENTIFIER APPENDIX", "", t, flags=re.S)
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in t.splitlines())


def papers():
    out = []
    for root, dirs, fs in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in fs:
            if not fn.endswith(".tex"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/")
            if any(x in rel for x in EXCLUDE):
                continue
            t = io.open(os.path.join(REPO, rel), encoding="utf-8",
                        errors="replace").read()
            if "\\title{" in t:
                out.append((rel, t))
    return sorted(out)


def title_of(t):
    i = t.find("\\title{")
    if i < 0:
        return "(untitled)"
    j, d = i + 7, 1
    while j < len(t) and d:
        if t[j] == "{":
            d += 1
        elif t[j] == "}":
            d -= 1
        j += 1
    s = t[i + 7:j - 1]
    s = re.split(r"\\\\", s)[0]
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = re.sub(r"[{}$\\]", "", s)
    return re.sub(r"\s+", " ", s).strip(" ,.-")[:95] or "(untitled)"


def version_of(t):
    cut = t.find("\\begin{document}")
    head = t[:cut] if cut > 0 else t[:20000]
    c = re.findall(r"\bVersion[~\s]*(\d+\.\d+(?:\.\d+)?)\b", head, re.I)
    if not c:
        return "—"
    return max(c, key=lambda v: tuple(
        int(x) for x in (v.split(".") + ["0", "0"])[:3]))


def last_changed(rel):
    import subprocess
    o = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short",
                        "--", rel], cwd=REPO, capture_output=True,
                       text=True).stdout.strip()
    return o or "—"


def classify(rel):
    for frag, name in CLASSES:
        if frag in rel:
            return name
    return "Series paper"


def seed_from_worksheet():
    """Pre-fill deposit records from bibliography/doi_harmonization_worksheet.csv.

    That worksheet already holds 39 real OSF DOIs -- the deposits nobody could
    otherwise account for, since the repo had no other record of what was live.
    These are REGISTRATION DOIs, not preprint DOIs, and are labelled as such:
    re-depositing a paper as a preprint mints a NEW DOI, so conflating the two
    would put the wrong identifier in a bibliography.

    Seeded values are written into Isak's columns only when those columns are
    empty, so anything he records by hand always wins.
    """
    import csv
    ws = os.path.join(REPO, "bibliography", "doi_harmonization_worksheet.csv")
    if not os.path.exists(ws):
        return {}
    tex = [r for r, _ in papers()]
    seed = {}
    for row in csv.DictReader(io.open(ws, encoding="utf-8-sig")):
        pid = (row.get("paper_id") or "").strip()
        doi = (row.get("REAL_DOI__fill") or "").strip()
        if not pid or not doi:
            continue
        hits = [p for p in tex
                if os.path.basename(p).lower().startswith(pid.lower() + "_")]
        if len(hits) == 1:
            seed[hits[0]] = ("registered", f"https://doi.org/{doi}",
                             "registration DOI (not a preprint DOI)")
    return seed


# --- Columns owned by humans and by the pipeline -------------------------
# Order matters: carry-forward reads the LAST len(OWNED) cells of each row.
OWNED = ["APPROVED", "CHANGE_CLASS", "PREPRINT_ID", "POSTED", "OSF_LINK",
         "NOTES"]

VALID_CHANGE = {"", "editorial", "substantive"}


def read_existing():
    """Carry forward every human/pipeline-owned column, keyed on .tex path.

    Handles BOTH layouts. The previous queue owned three columns (POSTED,
    OSF LINK, NOTES) and had 9 cells per row; this one owns six and has 13.
    Blindly taking the last six cells of an old row shifts Ver and Changed
    into APPROVED and CHANGE_CLASS -- which on the first run marked all 113
    rows as having an invalid CHANGE_CLASS. Old rows are therefore detected
    by width and mapped onto the three columns they actually had.
    """
    keep = {}
    if not os.path.exists(QUEUE):
        return keep
    for line in io.open(QUEUE, encoding="utf-8", errors="replace"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = re.search(r"`([^`]+\.tex)`", " ".join(cells))
        if not m:
            continue
        if len(cells) >= len(OWNED) + 6:                 # current layout
            keep[m.group(1)] = cells[-len(OWNED):]
        elif len(cells) == 9:                            # legacy layout
            keep[m.group(1)] = ["", "", ""] + cells[-3:]
    return keep


def eligibility(r):
    """Why a paper may or may not be deposited. Returns (eligible, reason).

    Deliberately conservative: anything ambiguous is NOT eligible. An
    unnecessary hold costs a day; an erroneous deposit cannot be undone,
    because a submitted preprint can only be withdrawn, which leaves its
    metadata as a permanent public record.
    """
    if r["withheld"]:
        return False, f"WITHHELD: {r['withheld']}"
    if not r["APPROVED"]:
        return False, "not approved"
    if r["CHANGE_CLASS"] not in VALID_CHANGE:
        return False, (f"CHANGE_CLASS '{r['CHANGE_CLASS']}' invalid "
                       "(use 'editorial' or 'substantive')")
    if not r["PREPRINT_ID"]:
        return True, "create: approved, no preprint yet"
    if r["CHANGE_CLASS"] != "substantive":
        return False, ("existing preprint, change is editorial or "
                       "unclassified -- no new version")
    # CHANGE_CLASS is not cleared after a deposit, so on its own it would keep
    # a paper eligible forever and republish it on every pipeline run. Require
    # the file to have actually changed since the last successful deposit.
    posted = (r["POSTED"] or "").strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", posted) and r["changed"] <= posted:
        return False, f"already deposited {posted}; unchanged since"
    return True, "new version: substantive change since last deposit"


def main():
    keep = read_existing()
    seed = seed_from_worksheet()
    rows, seeded = [], 0
    for rel, t in papers():
        body = t          # raw: see WITHHOLD note above
        why = ""
        for pat, reason in WITHHOLD:
            if re.search(pat, body, re.I):
                why = reason
                break
        owned = dict(zip(OWNED, keep.get(rel, [""] * len(OWNED))))
        if rel in seed:
            # Seed FIELD BY FIELD, never all-or-nothing. The previous guard was
            # `if not any(owned.values())`, which meant a single carried-forward
            # cell suppressed seeding of every other cell in the row. SF-1
            # carried its NOTES through the 3-column-to-6-column migration and
            # so silently lost its POSTED date and its recovered DOI -- exactly
            # the data loss the carry-forward contract exists to prevent.
            # A recorded value always wins; an empty one gets the seed.
            p_, l_, n_ = seed[rel]
            filled = False
            for col, val in (("POSTED", p_), ("OSF_LINK", l_), ("NOTES", n_)):
                if not (owned.get(col) or "").strip() and val:
                    owned[col] = val
                    filled = True
            if filled:
                seeded += 1
        r = {"rel": rel, "title": title_of(t), "ver": version_of(t),
             "changed": last_changed(rel), "cls": classify(rel),
             "withheld": why}
        r.update(owned)
        r["eligible"], r["reason"] = eligibility(r)
        rows.append(r)

    held = [r for r in rows if r["withheld"]]
    rdy = [r for r in rows if not r["withheld"]]
    elig = [r for r in rows if r["eligible"]]
    bad = [r for r in rows if r["CHANGE_CLASS"] not in VALID_CHANGE]
    missing = [k for k in keep if k not in {r["rel"] for r in rows}]

    # ---- machine contract ------------------------------------------------
    manifest = {
        "generated": "regenerate with code/build_osf_queue.py; do not hand-edit",
        "contract_version": 1,
        "counts": {"total": len(rows), "withheld": len(held),
                   "eligible_now": len(elig)},
        "never_deposit": sorted(r["rel"] for r in held),
        "papers": [{k: r[k] for k in
                    ("rel", "title", "ver", "changed", "cls", "withheld",
                     "eligible", "reason", *OWNED)} for r in rows],
    }
    io.open(MANIFEST, "w", encoding="utf-8").write(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    L = []
    A = L.append
    A("# OSF deposit queue")
    A("")
    A("**Generated by `code/build_osf_queue.py`. Re-run after any patch.**")
    A("")
    A("## The contract")
    A("")
    A("This file is for people. **Automation must read "
      "`osf_deposit_manifest.json`, generated in the same pass — never this "
      "markdown.** Parsing prose to decide what to publish is how the wrong "
      "paper gets published.")
    A("")
    A("Six columns are owned by you and the pipeline, and the generator "
      "**never overwrites them**: it reads them back and re-attaches them by "
      "file path. Everything else is derived from the repository and will be "
      "overwritten.")
    A("")
    A("| Column | Owner | Meaning |")
    A("|---|---|---|")
    A("| `APPROVED` | Thomas | Date + initials. **Nothing may be deposited "
      "without this.** Empty means not approved. |")
    A("| `CHANGE_CLASS` | Thomas | `substantive` or `editorial`. Only "
      "`substantive` triggers a new version of an existing preprint. |")
    A("| `PREPRINT_ID` | pipeline | OSF preprint ID, **written back on "
      "creation**. Empty = no preprint yet; non-empty = update, never create. |")
    A("| `POSTED` | pipeline/Isak | Date of last successful deposit. |")
    A("| `OSF_LINK` | pipeline/Isak | DOI or URL. |")
    A("| `NOTES` | Isak | Free text. Safe to write anything here. |")
    A("")
    A("**Why `PREPRINT_ID` matters more than it looks.** It is the only thing "
      "distinguishing *create a preprint* from *post a new version*. If the "
      "pipeline creates where it should update, the paper gets a second DOI — "
      "and a submitted preprint can only be removed by withdrawal, which "
      "leaves its metadata as a permanent public record. There is no clean "
      "undo, so the pipeline must write this field back immediately on "
      "creation.")
    A("")
    A("**Why `CHANGE_CLASS` exists.** Version stamps bump for cosmetic edits: "
      "one patch in this session bumped 60+ papers to add a glossary "
      "appendix. Republishing on every bump would put 60 meaningless versions "
      "on 60 DOIs. The version stamp records *that* a paper changed; "
      "`CHANGE_CLASS` records whether the change is worth a deposit.")
    A("")
    A(f"**Counts:** {len(rows)} papers · **{len(held)} never deposit** · "
      f"{len(elig)} eligible right now · {seeded} rows seeded from the DOI "
      "worksheet.")
    if bad:
        A("")
        A(f"> **{len(bad)} row(s) have an invalid `CHANGE_CLASS`.** The "
          "pipeline treats these as not eligible. Use `substantive` or "
          "`editorial`.")
    A("")
    A("---")
    A("")
    A("## NEVER DEPOSIT")
    A("")
    A("Listed rather than omitted on purpose: a paper that must not be "
      "deposited is more dangerous missing from this list than present on it, "
      "because an absent row invites someone to add it back from another "
      "source. **Do not post these; do not delete these rows.** The pipeline "
      "reads the same set from `never_deposit` in the manifest and must refuse "
      "them regardless of any other column.")
    A("")
    A("| # | Paper | File | Why |")
    A("|---|---|---|---|")
    for i, r in enumerate(held, 1):
        A(f"| {i} | {r['title']} | `{r['rel']}` | **{r['withheld']}** |")
    A("")
    A("---")
    A("")
    A("## Deposit queue")
    A("")
    A("Every paper below compiles and carries no unfinished or "
      "not-for-release marker. **CLASS is a judgement, not a rule** — "
      "\"Theorem artifact\" marks short proof documents supporting a larger "
      "paper. STATUS is computed; it is not something to edit.")
    A("")
    hdr = ("| # | Class | Paper | File | Ver | Changed | STATUS | "
           + " | ".join(OWNED) + " |")
    A(hdr)
    A("|" + "---|" * (hdr.count("|") - 1))
    order = {"Flagship": 0, "Series paper": 1, "Companion": 2,
             "Chirality derivation": 3, "Theorem artifact": 4}
    rdy.sort(key=lambda r: (order.get(r["cls"], 9), r["rel"]))
    for i, r in enumerate(rdy, 1):
        status = "**READY**" if r["eligible"] else r["reason"]
        A(f"| {i} | {r['cls']} | {r['title']} | `{r['rel']}` | {r['ver']} | "
          f"{r['changed']} | {status} | "
          + " | ".join(r[c] for c in OWNED) + " |")
    A("")
    if missing:
        A("---")
        A("")
        A("## Carried rows whose file no longer exists")
        A("")
        A("Renamed, moved or deleted. Their deposit records could not be "
          "re-keyed — re-attach by hand.")
        A("")
        for k in sorted(missing):
            A(f"- `{k}` — was: {keep[k]}")
        A("")

    io.open(QUEUE, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"queue: {len(rows)} papers, {len(held)} never-deposit, "
          f"{len(elig)} eligible now.")
    print(f"manifest: {os.path.relpath(MANIFEST, REPO)}")
    if seeded:
        print(f"  seeded {seeded} row(s) from the DOI worksheet.")
    if bad:
        print(f"  WARNING: {len(bad)} invalid CHANGE_CLASS value(s).")
    if missing:
        print(f"  WARNING: {len(missing)} carried row(s) no longer resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
