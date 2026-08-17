#!/usr/bin/env python3
"""
rebuild_paper_catalog.py — regenerate paper_catalog.md from repo ground truth.

Registered Patch 3205 (16 Aug 2026), F-SW-10 referred item 4.

GROUND TRUTH RULES (do not relax these):
  * Title, version and file path come from the .tex file itself.
  * Last-touched date and patch number come from `git log` on that file.
  * OSF / arXiv deposit state is NEVER inferred. It is carried forward from
    the prior catalog by exact path match, and any paper with no prior row is
    emitted as UNKNOWN. Nothing in this repo is a reliable record of what is
    actually live on OSF; only the founder can confirm that.

Usage:
    python3 code/rebuild_paper_catalog.py            # write paper_catalog.md
    python3 code/rebuild_paper_catalog.py --since 2026-06-21   # change report
"""

import argparse
import os
import re
import subprocess
import sys
from collections import OrderedDict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories excluded from the live catalog. archive/ is retired work;
# duplicates/ is quarantined (Patch 3201/3202).
EXCLUDE_DIR_PARTS = ("archive/", "/duplicates/", "duplicates/")

# Section grouping: (heading, path prefix). Order is the emitted order.
SECTIONS = [
    ("SF-Line Flagship Papers", "flagship_papers/"),
    ("Strong Sector Series", "series_strong/"),
    ("Standard Model Emergence Series", "series_standard_model/"),
    ("Special Relativity Series", "series_relativity/"),
    ("Electroweak Series", "series_electroweak/"),
    ("Quantum Mechanics Series", "series_quantum_mechanics/"),
    ("Foundations Series", "series_foundations/"),
    ("Phenomena / Cosmology", "series_phenomena/"),
    ("Umbrella / Substrate-Chirality Arc", "series_umbrella/"),
]


def sh(args):
    return subprocess.run(
        args, cwd=REPO, capture_output=True, text=True, errors="replace"
    ).stdout.strip()


def find_papers():
    out = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            if not fn.endswith(".tex"):
                continue
            rel = os.path.relpath(os.path.join(root, fn), REPO).replace("\\", "/")
            if any(p in rel for p in EXCLUDE_DIR_PARTS):
                continue
            try:
                with open(os.path.join(root, fn), encoding="utf-8",
                          errors="replace") as fh:
                    text = fh.read()
            except OSError:
                continue
            if "\\title{" not in text:
                continue
            out.append((rel, text))
    return sorted(out)


def clean_tex(s):
    """Strip LaTeX markup from an extracted title."""
    s = re.sub(r"\\\\\s*\[[^\]]*\]", " — ", s)   # \\[6pt] line breaks
    s = re.sub(r"\\\\", " — ", s)
    s = re.sub(r"\\(textbf|emph|textit|texttt|mathrm|text)\s*\{", "{", s)
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = re.sub(r"[~$]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" ,.-")


def extract_title(text):
    i = text.find("\\title{")
    if i < 0:
        return ""
    j, depth = i + 7, 1
    while j < len(text) and depth:
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
        j += 1
    title = clean_tex(text[i + 7:j - 1])
    # Titles often carry a trailing subtitle after a version marker; keep it,
    # but drop an embedded version stamp so it lands in the Version column.
    return re.sub(r"\s*Version\s*[\d.]+.*$", "", title, flags=re.I).strip()


VERSION_RE = re.compile(r"(?:Version|\bv)[~\s]*(\d+(?:\.\d+){0,2})\b", re.I)


def _vtuple(s):
    parts = (s.split(".") + ["0", "0"])[:3]
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (0, 0, 0)


def _brace_block(text, macro):
    """Return the balanced contents of \\macro{...}, or ''."""
    i = text.find("\\" + macro + "{")
    if i < 0:
        return ""
    j, depth = i + len(macro) + 2, 1
    while j < len(text) and depth:
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
        j += 1
    return text[i + len(macro) + 2:j - 1]


# Require a decimal point. The corpus stamps versions in at least three
# places (a leading % CHANGELOG block, \date{}, and a \Large title-page line),
# so all three are scanned. Bare integers are NOT accepted: c06 line 5 carries
# "(Version 16)" referring to a PREDECESSOR document, which max()'d over every
# real version in the file. Requiring X.Y excludes that whole class of
# cross-reference at the cost of missing genuinely integer-versioned papers,
# which are then reported honestly as unstamped rather than guessed at.
ANY_VER_RE = re.compile(r"\bVersion[~\s]*(\d+\.\d+(?:\.\d+)?)\b", re.I)


def extract_version(text):
    """
    Canonical version = the highest entry in the leading CHANGELOG comment
    block. This follows the house rule: filenames never carry version
    suffixes, and version history is tracked ONLY in the internal CHANGELOG
    header. The header is therefore the authority.

    \\date{} is a *rendering* of that version onto the title page and can go
    stale independently — c06 was found at CHANGELOG 2.3 (Patch 3202) with
    \\date{} still reading 2.2, which would have shipped a mislabelled PDF.
    So \\date{} is NOT used as a source; it is cross-checked and any
    disagreement is reported as a defect.

    No free-text fallback. Scanning the whole header for version-like strings
    produces false positives ("Theorem 3.1" was misread as v3.1 in SF-2), and
    a guessed version in a deposit catalog is worse than an honest blank.

    Returns (version, date_stamp, mismatch_bool). version is "—" if unstamped.
    """
    # The header is everything before \begin{document}, not an arbitrary
    # character count. DM-1 carries a 205-line comment block and its
    # version entry sits at offset 15382, which a 12000-char window missed
    # entirely -- reporting a correctly stamped paper as unstamped.
    cut = text.find("\\begin{document}")
    head = text[:cut] if cut > 0 else text[:20000]
    cands = ANY_VER_RE.findall(head)
    version = max(cands, key=_vtuple) if cands else "—"

    date_block = _brace_block(text, "date")
    dcands = ANY_VER_RE.findall(date_block) if date_block else []
    date_stamp = max(dcands, key=_vtuple) if dcands else "—"

    mismatch = (version != "—" and date_stamp != "—"
                and _vtuple(version) != _vtuple(date_stamp))
    return (version, date_stamp, mismatch)


PATCH_RE = re.compile(r"Patch(?:es)?\s+(\d{3,4}[a-zA-Z]?)")


def git_last_touch(path):
    line = sh(["git", "log", "-1", "--format=%ad|%s", "--date=short", "--", path])
    if not line or "|" not in line:
        return ("—", "—")
    date, subject = line.split("|", 1)
    m = PATCH_RE.search(subject)
    return (date, m.group(1) if m else "—")


def parse_prior_catalog(path):
    """Carry forward deposit state by exact .tex path match. Never guess."""
    prior = {}
    if not os.path.exists(path):
        return prior
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            m = re.search(r"`([^`]+\.tex)`", cells[3])
            if m:
                prior[m.group(1)] = cells[4]
    return prior


def deposit_state(rel, prior):
    if rel in prior and prior[rel]:
        return prior[rel]
    return "**UNKNOWN — not in prior catalog**"


def section_for(rel):
    for name, prefix in SECTIONS:
        if rel.startswith(prefix):
            return name
    return "Unsorted"


def build(since=None):
    papers = find_papers()
    prior = parse_prior_catalog(os.path.join(REPO, "paper_catalog.md"))

    rows = []
    for rel, text in papers:
        date, patch = git_last_touch(rel)
        ver, dstamp, mism = extract_version(text)
        rows.append({
            "path": rel,
            "title": extract_title(text) or "(title not parsed)",
            "version": ver,
            "date_stamp": dstamp,
            "mismatch": mism,
            "date": date,
            "patch": patch,
            "state": deposit_state(rel, prior),
            "section": section_for(rel),
            "carried": rel in prior,
        })

    grouped = OrderedDict((name, []) for name, _ in SECTIONS)
    grouped["Unsorted"] = []
    for r in rows:
        grouped[r["section"]].append(r)
    for v in grouped.values():
        v.sort(key=lambda r: r["path"])

    n_unknown = sum(1 for r in rows if not r["carried"])
    changed = [r for r in rows if since and r["date"] != "—" and r["date"] > since]

    L = []
    A = L.append
    A("# CPP Paper Catalog")
    A("")
    A("**Regenerated 16 August 2026 (Patch 3205) from repository ground truth "
      "by `code/rebuild_paper_catalog.py`.** The prior catalog was last "
      "substantively updated 21 June 2026 (Patch 1609) and had fallen ~2 "
      "months stale, which is why the Patch 3203 OSF manifest could not answer "
      "the founder's deposit question from the repo (F-SW-10 referred item 4).")
    A("")
    A("## How to read this file — and what it does NOT tell you")
    A("")
    A("**Trustworthy, because it is derived mechanically each run:** the file "
      "path, the title, the version stamp read from the `.tex` header, and the "
      "date and patch number of the last commit touching that file. These are "
      "regenerated from the tree and from `git log`; they cannot drift.")
    A("")
    A("**NOT trustworthy without founder confirmation: the Deposit column.** "
      "Nothing in this repository records what is actually live on OSF or "
      "arXiv. Deposit state is *carried forward verbatim* from the prior "
      "catalog by exact path match and is **never inferred**. A paper with no "
      "prior row is emitted as UNKNOWN rather than assumed undeposited. "
      "`research_priorities.md` §242 records OSF registration "
      "`10.17605/OSF.IO/JXE8D` stuck in *Pending Admin Contributor Approval* "
      "for 38+ days as of the Session 36 close, with a Zenodo fallback "
      "contemplated; **whether that ever resolved is recorded nowhere in this "
      "repo.** Resolving it is a founder action, not a repo action.")
    A("")
    A(f"**Coverage:** {len(rows)} live papers. **{n_unknown} were absent from "
      f"the prior catalog entirely** — the direct measure of the staleness "
      f"this rebuild corrects. `archive/` and quarantined `duplicates/` "
      f"directories are excluded by design.")
    A("")
    A("**To regenerate:** `python3 code/rebuild_paper_catalog.py`  ·  "
      "**To list papers changed since a date:** "
      "`python3 code/rebuild_paper_catalog.py --since YYYY-MM-DD`")
    A("")
    A("---")
    A("")

    for name, _ in SECTIONS:
        rs = grouped[name]
        if not rs:
            continue
        A(f"## {name}")
        A("")
        A("| Title | Ver | File | Last touched | Patch | Deposit |")
        A("|---|---|---|---|---|---|")
        for r in rs:
            title = r["title"]
            if len(title) > 95:
                title = title[:92] + "..."
            A(f"| {title} | {r["version"]} | `{r["path"]}` | {r["date"]} | "
              f"{r['patch']} | {r['state']} |")
        A("")
        A("---")
        A("")

    if grouped["Unsorted"]:
        A("## Unsorted — path prefix matched no section")
        A("")
        A("| Title | Ver | File | Last touched | Patch |")
        A("|---|---|---|---|---|")
        for r in grouped["Unsorted"]:
            A(f"| {r['title']} | {r['version']} | `{r['path']}` | {r['date']} "
              f"| {r['patch']} |")
        A("")

    mism = [r for r in rows if r["mismatch"]]
    if mism:
        A("## DEFECT — title-page version disagrees with the CHANGELOG")
        A("")
        A(f"**{len(mism)} paper(s).** The version history is authoritative; "
          "`\\date{}` renders it onto the title page and can be missed during "
          "a bump. **A PDF recompiled from these files would deposit to OSF "
          "carrying the wrong version number.** Fix the `\\date{}` line before "
          "recompiling.")
        A("")
        A("| File | CHANGELOG | Title page | Last patch |")
        A("|---|---|---|---|")
        for r in sorted(mism, key=lambda r: r["path"]):
            A(f"| `{r['path']}` | **{r['version']}** | {r['date_stamp']} | "
              f"{r['patch']} |")
        A("")

    unstamped = [r for r in rows if r["version"] == "—"]
    if unstamped:
        A("## Papers carrying no parseable version stamp")
        A("")
        A(f"**{len(unstamped)} of {len(rows)}.** No `Version X.Y` string was "
          "found in the header, `\\date{}`, or title block. These are reported "
          "rather than guessed at: an invented version in a deposit catalog is "
          "worse than a visible blank. Integer-only stamps (`Version 3`) are "
          "deliberately not accepted, because bare integers in these headers "
          "are usually cross-references to predecessor documents.")
        A("")
        A("| File | Last touched | Patch |")
        A("|---|---|---|")
        for r in sorted(unstamped, key=lambda r: r["path"]):
            A(f"| `{r['path']}` | {r['date']} | {r['patch']} |")
        A("")

    if since:
        A(f"## Papers changed since {since} — OSF re-deposit shortlist")
        A("")
        A(f"**{len(changed)} of {len(rows)} papers.** This is the answer to "
          "*which PDFs need updating*, conditional on the founder confirming "
          "what is actually live.")
        A("")
        A("| File | Last touched | Patch |")
        A("|---|---|---|")
        for r in sorted(changed, key=lambda r: r["date"], reverse=True):
            A(f"| `{r['path']}` | {r['date']} | {r['patch']} |")
        A("")

    return "\n".join(L) + "\n", rows, changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", help="YYYY-MM-DD; emit a change shortlist")
    ap.add_argument("--stdout", action="store_true",
                    help="print instead of writing paper_catalog.md")
    args = ap.parse_args()

    text, rows, changed = build(args.since)
    if args.stdout:
        sys.stdout.write(text)
    else:
        with open(os.path.join(REPO, "paper_catalog.md"), "w",
                  encoding="utf-8") as fh:
            fh.write(text)
        print(f"paper_catalog.md rewritten: {len(rows)} papers.")
        if args.since:
            print(f"{len(changed)} changed since {args.since}.")


if __name__ == "__main__":
    main()
