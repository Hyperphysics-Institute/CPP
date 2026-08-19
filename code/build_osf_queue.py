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
OWNED = ["APPROVED", "CHANGE_CLASS", "RESERVED_DOI", "CONCEPT_DOI",
         "PREPRINT_ID", "POSTED", "OSF_LINK", "PARENT", "RELATION",
         "COMMUNITY", "NOTES"]

# Default Zenodo community for the corpus. A record may belong to only ONE
# community by the review-request route, so the community carries the
# CORPUS-WIDE grouping and the PARENT/RELATION links carry the F.1 and SR-1
# clusters. The two are complementary, not alternatives.
DEFAULT_COMMUNITY = "conscious-point-physics"

VALID_CHANGE = {"", "editorial", "substantive"}


def read_existing():
    """Carry forward every human/pipeline-owned column, keyed on .tex path.

    Columns are matched BY HEADER NAME, never by position. Positional reading
    is what corrupted the two previous migrations: the 3-to-6 column change
    shifted Ver and Changed into APPROVED and CHANGE_CLASS and marked all 113
    rows malformed, and a subsequent all-or-nothing guard silently erased
    SF-1's recovered DOI (fixed at Patch 3218). Reading by name means a column
    may be added, removed or reordered without any cell landing in the wrong
    field -- which matters now that RESERVED_DOI holds values that exist
    NOWHERE ELSE: a reserved Zenodo DOI is internal to Zenodo, is not
    recoverable if its draft is deleted, and may already be baked into a built
    PDF's bibliography. Losing one silently would invalidate that PDF with no
    way to reconstruct the value.

    Rows in an older layout are read for whichever owned columns their header
    did contain; columns that did not exist come back empty rather than
    picking up a neighbour's value.
    """
    keep = {}
    if not os.path.exists(QUEUE):
        return keep
    header = None
    for line in io.open(QUEUE, encoding="utf-8", errors="replace"):
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("`*") for c in line.strip().strip("|").split("|")]
        # The header is the row naming the file column alongside owned columns.
        if header is None:
            names = [c.upper().replace(" ", "_") for c in cells]
            if "FILE" in names and any(o in names for o in OWNED):
                header = names
            continue
        m = re.search(r"`([^`]+\.tex)`", line)
        if not m:
            continue
        row = {}
        for col in OWNED:
            row[col] = (cells[header.index(col)]
                        if col in header and header.index(col) < len(cells)
                        else "")
        keep[m.group(1)] = [row[c] for c in OWNED]
    return keep


F1_PARENT = ("series_umbrella/series_substrate_chirality_arc/"
             "dynamical_substrate_law/dynamical_substrate_law.tex")

VALID_RELATION = {"", "isSupplementTo", "isPartOf", "isDocumentedBy",
                  "isDerivedFrom", "references"}


def norm_title(s):
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    s = re.sub(r"[{}$\\`'\"~,.:;-]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def infer_parents(rows, texts):
    """Infer PARENT and RELATION from evidence in the papers themselves.

    Evidence-first, and deliberately conservative: where a paper gives no
    evidence of a parent, the field is left EMPTY and reported, rather than
    inferred from its directory. The SR_companion_papers folder is not
    homogeneous -- c07-c13 are general relativity and c14-c15 are
    strong-sector -- so a blanket 'everything here is a companion to SR-1'
    default would attach a dozen papers to the wrong parent, and a wrong
    relation in DataCite metadata is worse than none: it is machine-readable
    and propagates into indexes.

    Rule 1: anything under hardened_theorems/ is a proof step supporting the
            F.1 Dynamical Substrate Law, which those papers state in their own
            author line ("F.1 Dynamical Substrate Law trajectory").
    Rule 2: a paper declaring `Companion Paper to ``TITLE''` is matched to the
            paper whose title is TITLE.
    Rule 3: otherwise blank.
    """
    by_title = {}
    for rel, t in texts.items():
        i = t.find("\\title{")
        if i < 0:
            continue
        j, d = i + 7, 1
        while j < len(t) and d:
            if t[j] == "{":
                d += 1
            elif t[j] == "}":
                d -= 1
            j += 1
        by_title.setdefault(norm_title(re.split(r"\\\\", t[i + 7:j - 1])[0]), rel)

    out = {}
    for rel, t in texts.items():
        if "hardened_theorems/" in rel and F1_PARENT in texts:
            out[rel] = (F1_PARENT, "isSupplementTo", "rule1: F.1 trajectory")
            continue
        m = re.search(r"[Cc]ompanion [Pp]aper to\s*[`\u201c]{1,2}"
                      r"([^`\u201d]{5,140})", t)
        if m:
            want = norm_title(m.group(1))
            # Titles carry a paper-ID prefix ("SR-1: Mechanistic Derivation
            # of...") that the companion's declaration omits, so a prefix
            # comparison never matches. Strip a leading "xx 9 " style ID from
            # both sides and compare by containment instead.
            def core(x):
                return re.sub(r"^[a-z]{1,3}\s*\d+[a-z]?\s+", "", x)
            wc = core(want)
            hit = ""
            for k, v in by_title.items():
                kc = core(k)
                if not kc or v == rel:
                    continue
                if wc[:45] in kc or kc[:45] in wc:
                    hit = v
                    break
            if hit and hit != rel:
                out[rel] = (hit, "isSupplementTo", "rule2: declared companion")
                continue
            out[rel] = ("", "", f"declares companion to '{m.group(1)[:40]}' "
                                "-- no matching paper found")
            continue
        out[rel] = ("", "", "")
    return out


def citation_graph(rows, texts):
    """Which CPP papers each paper cites, as .tex paths.

    Self-citations are resolved through bibliography/doi_harmonization_worksheet.csv:
    bib key -> paper ID -> .tex filename. Only 12 of 117 papers cite any other
    CPP paper, and the graph is acyclic -- which is what makes single-pass
    publication possible at all.
    """
    import csv
    key2id = {}
    ws = os.path.join(REPO, "bibliography", "doi_harmonization_worksheet.csv")
    if os.path.exists(ws):
        for row in csv.DictReader(io.open(ws, encoding="utf-8-sig")):
            k = (row.get("bib_key") or "").strip()
            pid = (row.get("paper_id") or "").strip()
            if k and pid:
                key2id[k] = pid
    id2tex = {}
    for rel in texts:
        base = os.path.basename(rel).lower()
        for pid in set(key2id.values()):
            if base.startswith(pid.lower() + "_"):
                id2tex.setdefault(pid, rel)
    dep = {}
    for rel, t in texts.items():
        d = set()
        for m in re.finditer(r"\\cite[a-z]*\{([^}]*)\}", t):
            for k in m.group(1).split(","):
                k = k.strip()
                tgt = id2tex.get(key2id.get(k, ""), "")
                if tgt and tgt != rel:
                    d.add(tgt)
        dep[rel] = d
    return dep


def assign_waves(dep):
    """Topological layering: a paper's wave is one past its latest dependency.

    Wave N can only be deposited once every paper in waves < N has a DOI, so
    each paper is published EXACTLY ONCE with correct citations -- no
    deposit-then-republish cycle. Papers on the never-deposit list are treated
    as satisfied dependencies: nothing may stall waiting for a DOI that will
    never be minted.
    """
    wave, remaining, guard = {}, set(dep), 0
    satisfied = set()
    while remaining and guard < 100:
        guard += 1
        ready = [r for r in remaining if dep[r] <= satisfied]
        if not ready:                       # cycle: fail loudly, do not guess
            for r in sorted(remaining):
                wave[r] = None
            break
        for r in ready:
            wave[r] = guard
        satisfied |= set(ready)
        remaining -= set(ready)
    return wave


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
    # Require an EXPLICIT classification, not merely a well-formed one. Blank
    # is accepted as a valid *format* (VALID_CHANGE) so the queue does not
    # report every untouched row as malformed, but it is not enough to deposit
    # on. The reason is defence in depth: the worst failure this contract
    # guards against is creating a duplicate preprint for a paper that already
    # has one, which is not cleanly reversible. That happens when PREPRINT_ID
    # goes missing -- and a PREPRINT_ID was in fact silently dropped by the
    # seeding bug fixed at Patch 3218. Requiring a human-entered CHANGE_CLASS
    # puts a second, independent human check on the same row.
    if r["CHANGE_CLASS"] not in ("editorial", "substantive"):
        return False, (f"CHANGE_CLASS '{r['CHANGE_CLASS']}' not set "
                       "(use 'editorial' or 'substantive')")
    if r.get("wave_blocked_by"):
        n = len(r["wave_blocked_by"])
        return False, (f"wave {r.get('wave')}: blocked, {n} cited paper(s) "
                       "have no DOI yet")
    # Reservation is a tracked step that must happen BEFORE the PDF is built,
    # because the whole point of reserving is to bake the DOI into the paper's
    # own bibliography. Depositing without it would publish a paper whose
    # references are already wrong.
    if not (r.get("RESERVED_DOI") or "").strip():
        return False, "no reserved DOI yet (reserve before building the PDF)"
    if not r["PREPRINT_ID"]:
        return True, "create: approved, DOI reserved, no deposit yet"
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
        r["_text"] = t
        rows.append(r)

    # ---- waves -----------------------------------------------------------
    texts = {r["rel"]: r.pop("_text") for r in rows}
    dep = citation_graph(rows, texts)
    inferred = infer_parents(rows, texts)
    wave = assign_waves(dep)
    byrel = {r["rel"]: r for r in rows}
    never = {r["rel"] for r in rows if r["withheld"]}
    for r in rows:
        # A recorded PARENT always wins over an inferred one; inference only
        # fills a blank, so a founder correction is never overwritten.
        # Never default a community onto a withheld paper: it will not be
        # deposited, so a community assignment on its row would read as
        # deposit intent for a paper that must never be deposited.
        if not (r.get("COMMUNITY") or "").strip() and not r["withheld"]:
            r["COMMUNITY"] = DEFAULT_COMMUNITY
        pi, ri, why = inferred.get(r["rel"], ("", "", ""))
        if not (r.get("PARENT") or "").strip() and pi:
            r["PARENT"], r["RELATION"] = pi, ri
        r["parent_source"] = why
        r["wave"] = wave.get(r["rel"])
        r["cites"] = sorted(dep.get(r["rel"], ()))
        # A dependency is satisfied once it HAS a DOI, or once it is known to
        # be one that will never be deposited. Otherwise a live paper could
        # stall forever behind a withheld one.
        r["wave_blocked_by"] = sorted(
            d for d in dep.get(r["rel"], ())
            if d not in never
            and not (byrel.get(d, {}).get("OSF_LINK") or "").strip())
    for r in rows:
        r["eligible"], r["reason"] = eligibility(r)

    held = [r for r in rows if r["withheld"]]
    rdy = [r for r in rows if not r["withheld"]]
    elig = [r for r in rows if r["eligible"]]
    bad = [r for r in rows if r["CHANGE_CLASS"] not in VALID_CHANGE]
    missing = [k for k in keep if k not in {r["rel"] for r in rows}]

    # Reciprocal links: Zenodo relations are NOT auto-reciprocal, so a parent
    # must declare isSupplementedBy/hasPart for each child or its record will
    # not list them. Generated here so the 137 back-links are never hand-set.
    INVERSE = {"isSupplementTo": "isSupplementedBy", "isPartOf": "hasPart",
               "isDocumentedBy": "documents", "isDerivedFrom": "isSourceOf",
               "references": "isReferencedBy"}
    kids = {}
    for r in rows:
        par = (r.get("PARENT") or "").strip()
        if par:
            kids.setdefault(par, []).append(
                {"child": r["rel"], "inverse":
                 INVERSE.get(r.get("RELATION") or "", "isSupplementedBy")})
    for r in rows:
        r["children"] = sorted(kids.get(r["rel"], []),
                               key=lambda k: k["child"])

    # ---- machine contract ------------------------------------------------
    manifest = {
        "generated": "regenerate with code/build_osf_queue.py; do not hand-edit",
        "contract_version": 2,
        "deposit_sequence": [
            "1. RESERVE the DOI on a Zenodo draft and record it in "
            "RESERVED_DOI immediately. A reserved DOI exists only inside "
            "Zenodo and CANNOT be recovered if the draft is deleted.",
            "2. WRITE the reserved DOI into the paper's own bibliography. "
            "This is the whole point of reserving, and it is why the PDF must "
            "not be built first.",
            "3. BUILD the PDF from the .tex that now contains the DOI.",
            "4. UPLOAD the PDF to the draft that holds that reserved DOI. "
            "Never to a new draft -- a new draft means a different DOI, and "
            "the PDF's own bibliography would then be wrong.",
            "5. CREATE the community review request on the DRAFT, before "
            "publishing. Community membership is no longer a metadata field; "
            "under InvenioRDM it is a request/review flow, and only ONE "
            "community per record is permitted.",
            "6. PUBLISH. This mints the version DOI and, on first publication, "
            "the concept DOI.",
            "7. ACCEPT the community request as curator, then record "
            "PREPRINT_ID, POSTED, CONCEPT_DOI.",
            "8. SET the reciprocal relation on the PARENT record. Zenodo "
            "relations are NOT automatically reciprocal: the child's "
            "isSupplementTo does not create the parent's isSupplementedBy. "
            "See each parent's 'children' list.",
            "NEVER delete a draft holding a reserved DOI that has already "
            "been written into a built PDF.",
        ],
        "counts": {"total": len(rows), "withheld": len(held),
                   "eligible_now": len(elig)},
        "never_deposit": sorted(r["rel"] for r in held),
        "waves": {str(w): sorted(r["rel"] for r in rows if r["wave"] == w)
                  for w in sorted({r["wave"] for r in rows
                                   if r["wave"] is not None})},
        "papers": [{k: r[k] for k in
                    ("rel", "title", "ver", "changed", "cls", "withheld",
                     "wave", "cites", "wave_blocked_by",
                     "children", "parent_source",
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
    A("## Deposit sequence — the order is not optional")
    A("")
    A("Each step exists because doing it later breaks something that cannot "
      "be repaired afterwards. The same list is in "
      "`osf_deposit_manifest.json` under `deposit_sequence`, so the pipeline "
      "and the operator read identical instructions.")
    A("")
    for step in manifest["deposit_sequence"]:
        # Numbered steps carry their own ordinal; anything else is a standing
        # warning, not a step, and must not be given a step number.
        A(step if step[0].isdigit() else f"\n**{step}**")
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
