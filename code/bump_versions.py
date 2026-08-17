#!/usr/bin/env python3
"""
bump_versions.py — advance the version of every paper changed by a patch, and
assign a first version to any paper that has none.

Registered Patch 3212, implementing the founder ruling of 16 Aug 2026:
"Please update the paper version if you make any changes, and assign a version
number if it doesn't already have one."

WHAT "VERSION 1.0" MEANS HERE. For a paper that has never carried a stamp,
this tool assigns 1.0 and says so explicitly in the changelog entry: 1.0 is the
FIRST VERSION STAMP, not a claim that the paper has reached v1.0 shipped grade.
Conflating the two would silently promote unshipped work, so the distinction is
written into every stamp this tool creates.

STAMPS ARE WRITTEN IN TWO PLACES, matching the c04/c06 house style:
  1. a leading "% Version X" CHANGELOG comment  (the authority)
  2. the \\date{} title-page line               (what the reader sees)
Writing only one is the c06 defect found at Patch 3205: the changelog said 2.3
while the title page still said 2.2, so a recompiled PDF would have carried the
wrong number to OSF.

Usage:
    python3 code/bump_versions.py --files-from LIST --patch 3212 --reason "..."
    python3 code/bump_versions.py ... --apply      # omit for a dry run
"""

import argparse
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER_RE = re.compile(r"\bVersion[~\s]*(\d+\.\d+(?:\.\d+)?)\b", re.I)
CHANGELOG_RE = re.compile(r"^\s*%.*?\bVersion[~\s]*(\d+(?:\.\d+){0,2})\b",
                          re.I | re.M)


def vtuple(s):
    parts = (s.split(".") + ["0", "0"])[:3]
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (0, 0, 0)


def brace_block(text, macro):
    i = text.find("\\" + macro + "{")
    if i < 0:
        return None, None
    j, depth = i + len(macro) + 2, 1
    while j < len(text) and depth:
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
        j += 1
    return i, j                      # [i, j) spans \macro{...}


def current_version(text):
    """Highest version anywhere in the header. Requires a decimal point, so
    cross-references like c06's '(Version 16)' to a predecessor document are
    not mistaken for this paper's version."""
    cut = text.find("\\begin{document}")
    cands = VER_RE.findall(text[:cut] if cut > 0 else text[:20000])
    return max(cands, key=vtuple) if cands else None


def next_version(v):
    """Bump the last component: 2.3 -> 2.4, 1.01 -> 1.02, 3.3.1 -> 3.3.2."""
    parts = v.split(".")
    width = len(parts[-1])
    parts[-1] = str(int(parts[-1]) + 1).zfill(width)
    return ".".join(parts)


def wrap(text, width=72, prefix="%   "):
    out, line = [], prefix
    for w in text.split():
        if len(line) + len(w) + 1 > width and line.strip() != prefix.strip():
            out.append(line)
            line = prefix + w
        else:
            line = (line + " " + w) if line.strip() != prefix.strip() else prefix + w
    if line.strip() != prefix.strip():
        out.append(line)
    return "\n".join(out)


def insert_changelog(text, entry):
    """Before the first existing '% Version' comment; else at the top of the
    leading comment block; else immediately before \\documentclass."""
    m = CHANGELOG_RE.search(text)
    if m:
        at = text.rfind("\n", 0, m.start()) + 1
        return text[:at] + entry + "\n" + text[at:]
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines) and lines[i].lstrip().startswith("%"):
        i += 1
    if i > 0:
        at = sum(len(l) for l in lines[:i])
        return text[:at] + entry + "\n" + text[at:]
    d = text.find("\\documentclass")
    if d < 0:
        return None
    return text[:d] + entry + "\n" + text[d:]


def stamp_date(text, newv, patch, reason):
    i, j = brace_block(text, "date")
    if i is None:
        return None
    inner = text[i + 6:j - 1]
    add = ("\\\\[2pt]\n{\\small Version~%s --- 17 August 2026 "
           "(Patch %s: %s)}" % (newv, patch, reason))
    return text[:j - 1] + add + text[j - 1:]


def process(rel, patch, reason, first_note, apply_):
    path = os.path.join(REPO, rel)
    text = io.open(path, encoding="utf-8", errors="replace").read()
    cur = current_version(text)
    if cur:
        newv, kind = next_version(cur), "bump"
        body = ("%% Version %s --- 17 August 2026 (Patch %s):\n%s"
                % (newv, patch, wrap(reason)))
    else:
        newv, kind = "1.0", "first"
        body = ("%% Version %s --- 17 August 2026 (Patch %s):\n%s\n%s"
                % (newv, patch, wrap(reason), wrap(first_note)))
    t2 = insert_changelog(text, body)
    if t2 is None:
        return (rel, cur, None, "no changelog anchor")
    t3 = stamp_date(t2, newv, patch, reason)
    if t3 is None:
        return (rel, cur, None, "no \\date{} to stamp")
    if apply_:
        io.open(path, "w", encoding="utf-8").write(t3)
    return (rel, cur, newv, kind)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--files-from", required=True)
    ap.add_argument("--patch", required=True)
    ap.add_argument("--reason", required=True)
    ap.add_argument("--first-note", default=(
        "This is the FIRST version stamp assigned to this paper; 1.0 denotes "
        "the first stamped revision, NOT a claim of v1.0 shipped grade."))
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    files = [l.strip() for l in io.open(a.files_from, encoding="utf-8")
             if l.strip() and not l.startswith("#")]
    bumps = firsts = fails = 0
    for rel in files:
        rel_, cur, newv, kind = process(
            rel, a.patch, a.reason, a.first_note, a.apply)
        if newv is None:
            fails += 1
            print(f"  FAIL  {kind:22}  {rel_}")
        elif kind == "first":
            firsts += 1
            print(f"  FIRST  (none) -> {newv:6}  {rel_}")
        else:
            bumps += 1
            print(f"  BUMP   {cur:6} -> {newv:6}  {rel_}")
    print(f"\n{bumps} bumped, {firsts} first-stamped, {fails} failed"
          f"{'' if a.apply else '  (DRY RUN — nothing written)'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
