#!/usr/bin/env python3
"""
deferral_gate.py — run BEFORE `git format-patch`, on every patch. Not advisory.

    python3 code/deferral_gate.py            # checks HEAD
    python3 code/deferral_gate.py <commit>   # checks that commit

Rule (bootup §0.5 D-9, §3 DEFERRAL RIDER): a patch that puts anything aside —
"owed", "deferred", "flagged, not fixed", "at the next recompile", "left to the
X lane", "carried", "reconcile when …" — must write that item into todolist.md
in the SAME commit, under the lane that will act. A deferral that is not in
todolist.md is not a deferral; it is a drop. Three arcs lost their owed items
this way (TODO-3930-EU, TODO-3938-DM, TODO-0937-CHIR), each recovered only
because the founder asked.

The gate scans the commit message and the ADDED lines of the diff for the
deferral vocabulary. If it finds any and todolist.md is not among the files
changed, it fails and prints every hit so you can file them. To assert that a
hit is a false positive (e.g. "the three flags are closed"), put the literal
token NOTHING-DEFERRED in the commit message, at the start of a clause and
followed by a dash or colon and your reason:

    <token> — every hit is the gate's own name in a citation of 0939.

(written out in full, at the start of a clause, in place of <token>)

That assertion is auditable in git log, which is the point. Two rules keep the
token honest (both Patch 0975): a bare MENTION of the token is not an assertion,
and when the token IS asserted the hits are printed anyway — an override the
author never reads is not an audit.

Exit 0 = pass. Exit 1 = file the items (or assert NOTHING-DEFERRED) and amend.
"""
import re, subprocess, sys

commit = sys.argv[1] if len(sys.argv) > 1 else "HEAD"

def git(*a):
    # errors="replace": a single undecodable byte anywhere in the diff used to raise
    # UnicodeDecodeError here and take the whole gate down. A gate that CRASHES on bad
    # input is a gate that is not run. Corruption is now REPORTED by encoding_gate.py
    # instead (added Patch 4014, after this crash surfaced two corrupt files).
    return subprocess.run(["git", *a], capture_output=True, text=True,
                          errors="replace", check=True).stdout

msg = git("log", "-1", "--format=%B", commit)
files = git("show", "--name-only", "--format=", commit).split()
diff = git("show", "--format=", "--unified=0", commit)
added = [l[1:] for l in diff.splitlines()
         if l.startswith("+") and not l.startswith("+++")]

# Vocabulary of putting-aside. Word-boundaried; case-insensitive.
PATTERNS = [
    r"\bowed\b", r"\bowe[sd]? to\b", r"\bdefer(?:red|s|ral)?\b",
    r"\bflagged?\b(?! F\d)",          # "flagged" but not "flag F1"
    r"\bnot (?:fixed|supplied|pinned|done|settled) (?:here|in this patch|by this patch)\b",
    r"\bat the next (?:recompile|SHIP|session|window)\b",
    r"\bleft to (?:the )?\w+(?: lane)?\b", r"\bleaves? (?:it|this|that) to\b",
    r"\bcarried (?:forward|over)?\b", r"\breconcile[sd]? when\b",
    r"\bto be (?:amended|reconciled|written|done|fixed)\b",
    r"\bfollow-?up\b", r"\bfor (?:a )?later\b", r"\bpending\b",
    r"\bstill (?:owed|open|blocked)\b", r"\bnext action\b",
]
rx = re.compile("|".join(PATTERNS), re.I)

hits = []
for src, lines in (("commit message", msg.splitlines()), ("added lines", added)):
    for l in lines:
        # skip lines that are themselves todolist.md content or the gate's own text
        if "todolist.md" in l and src == "added lines":
            continue
        m = rx.search(l)
        if m:
            hits.append((src, m.group(0), l.strip()[:140]))

touched = any(f.endswith("todolist.md") for f in files)
# The token counts only as an ASSERTION, never as a MENTION. It must open a clause
# (line start, or after . : ;) and introduce a reason with a dash or colon.
# Patch 0974 was not asserting anything: its message said "all PASS or
# NOTHING-DEFERRED asserted in the log" — a narrative sentence ABOUT the gate,
# in the same breath as "STEPS C/D … are OWED, deferred". A bare substring test
# read that mention as an override and waved through the drop that started this.
# Predicted at 0962: "the gate fires on its own name, which will recur in any
# patch that cites 0939." It recurred. (Added Patch 0975.)
ASSERT_RX = re.compile(r"(?:^|(?<=[.:;])\s*)NOTHING-DEFERRED\s*[-–—:]", re.M)
asserted = bool(ASSERT_RX.search(msg))

print(f"deferral_gate: {commit} — {len(hits)} deferral-vocabulary hit(s); "
      f"todolist.md {'TOUCHED' if touched else 'not touched'}; "
      f"NOTHING-DEFERRED {'asserted' if asserted else 'not asserted'}")
if hits and not touched and not asserted:
    print("\nFAIL — this patch puts things aside and does not file them. Hits:")
    for src, word, line in hits[:40]:
        print(f"  [{src}] «{word}»  {line}")
    if len(hits) > 40:
        print(f"  … {len(hits) - 40} more")
    print("\nFile each item in todolist.md under the lane that acts (same commit, "
          "`git commit --amend`), or add the token NOTHING-DEFERRED to the message "
          "if every hit is a false positive — clause-initial, with a dash and your reason.")
    sys.exit(1)
if hits and asserted:
    # Show what is being overridden. The assertion is auditable in git log, but an
    # author who never SEES the hits cannot audit his own override at the moment he
    # makes it. Patch 0974 asserted NOTHING-DEFERRED on a commit whose own body read
    # "Steps C/D … OWED"; the gate found that line and printed only "PASS by
    # assertion", so nothing contradicted the author. (Added Patch 0975.)
    print("\nOVERRIDDEN by NOTHING-DEFERRED — recorded in git log. "
          "Read these before you accept the override:")
    for src, word, line in hits[:40]:
        print(f"  [{src}] «{word}»  {line}")
    if len(hits) > 40:
        print(f"  … {len(hits) - 40} more")
    print("\nIf any of these is a real item, it belongs in todolist.md, not behind "
          "the token. A false override is indistinguishable from a drop.")
else:
    print("PASS")
