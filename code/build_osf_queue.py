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
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(REPO, "osf_deposit_queue.md")
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


def read_existing():
    """Carry forward Isak's three columns, keyed on the .tex path."""
    keep = {}
    if not os.path.exists(QUEUE):
        return keep
    for line in io.open(QUEUE, encoding="utf-8", errors="replace"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            continue
        m = re.search(r"`([^`]+\.tex)`", " ".join(cells))
        if m:
            keep[m.group(1)] = (cells[-3], cells[-2], cells[-1])
    return keep


def main():
    keep = read_existing()
    rows = []
    for rel, t in papers():
        # WITHHOLD detection scans the RAW text, comments included, unlike
        # every other check in this repo. The usual rule -- comments never
        # reach the PDF, so they are not public-facing -- is right for jargon
        # and wrong here. SF-7 marks its unwritten sections with %%TODO
        # comments; they render nothing, but they are exactly the evidence
        # that the paper is scaffolded and unfinished. Withholding asks
        # whether the PAPER is finished, not what the READER sees.
        body = t
        why = ""
        for pat, reason in WITHHOLD:
            if re.search(pat, body, re.I):
                why = reason
                break
        posted, link, notes = keep.get(rel, ("", "", ""))
        rows.append({
            "rel": rel, "title": title_of(t), "ver": version_of(t),
            "changed": last_changed(rel), "cls": classify(rel),
            "withheld": why, "posted": posted, "link": link, "notes": notes,
        })

    held = [r for r in rows if r["withheld"]]
    rdy = [r for r in rows if not r["withheld"]]
    carried = sum(1 for r in rows if r["posted"] or r["link"] or r["notes"])
    missing = [k for k in keep if k not in {r["rel"] for r in rows}]

    L = []
    A = L.append
    A("# OSF deposit queue")
    A("")
    A("**Generated by `code/build_osf_queue.py`. Re-run it after any patch.**")
    A("")
    A("## For Isak — how to use this file")
    A("")
    A("Fill in the last three columns — **POSTED**, **OSF LINK**, **NOTES** — "
      "as you deposit. **This script never overwrites those three.** It reads "
      "them back and re-attaches them by file path, so the rest of the table "
      "can be regenerated after every change without losing your entries. "
      "Everything else in the table is derived from the repository and will be "
      "overwritten, so put your working notes only in the NOTES column.")
    A("")
    A("Deposit by **version change**, not on a schedule: OSF entries are "
      "versioned and DOI'd, so a daily run churns new versions of papers that "
      "did not change. The VER and CHANGED columns tell you what actually "
      "moved since you last deposited.")
    A("")
    A("If a paper is renamed or moved, its row is re-keyed and your columns "
      "for it are lost. Renames are reported at the bottom of this file rather "
      "than dropped silently — check that section after a big patch.")
    A("")
    A(f"**Counts:** {len(rdy)} clear to deposit · **{len(held)} WITHHELD** · "
      f"{len(rows)} total · {carried} rows carrying deposit records.")
    A("")
    A("---")
    A("")
    A("## DO NOT DEPOSIT — withheld")
    A("")
    A("These are listed rather than omitted on purpose: a paper that must not "
      "be deposited is more dangerous missing from this list than present on "
      "it, because an absent row invites someone to add it back from another "
      "source. **Do not post these, and do not remove these rows.**")
    A("")
    A("| # | Paper | File | Why withheld |")
    A("|---|---|---|---|")
    for i, r in enumerate(held, 1):
        A(f"| {i} | {r['title']} | `{r['rel']}` | **{r['withheld']}** |")
    A("")
    A("---")
    A("")
    A("## Clear to deposit")
    A("")
    A("Every paper below compiles to a PDF and carries no unfinished or "
      "not-for-release marker. **CLASS is a judgement call, not a rule** — "
      "\"Theorem artifact\" marks short proof documents supporting a larger "
      "paper, which may belong as supplementary files rather than standalone "
      "deposits. Confirm with Thomas before treating those as separate "
      "publications.")
    A("")
    A("| # | Class | Paper | File | Ver | Changed | POSTED | OSF LINK | NOTES |")
    A("|---|---|---|---|---|---|---|---|---|")
    order = {"Flagship": 0, "Series paper": 1, "Companion": 2,
             "Chirality derivation": 3, "Theorem artifact": 4}
    rdy.sort(key=lambda r: (order.get(r["cls"], 9), r["rel"]))
    for i, r in enumerate(rdy, 1):
        A(f"| {i} | {r['cls']} | {r['title']} | `{r['rel']}` | {r['ver']} | "
          f"{r['changed']} | {r['posted']} | {r['link']} | {r['notes']} |")
    A("")
    if missing:
        A("---")
        A("")
        A("## Rows carried from a previous run whose file no longer exists")
        A("")
        A("These were renamed, moved or deleted. Any deposit record attached "
          "to them could not be re-keyed — re-attach it to the new path by "
          "hand.")
        A("")
        for k in sorted(missing):
            A(f"- `{k}` — was: {keep[k]}")
        A("")

    io.open(QUEUE, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"osf_deposit_queue.md written: {len(rdy)} clear, {len(held)} "
          f"withheld, {len(rows)} total.")
    if carried:
        print(f"  carried {carried} existing deposit record(s) forward.")
    if missing:
        print(f"  WARNING: {len(missing)} carried row(s) no longer resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
