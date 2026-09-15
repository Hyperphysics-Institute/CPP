#!/usr/bin/env python3
"""absence_gate.py -- catch UNVERIFIED ABSENCE CLAIMS in a patch.

WHY THIS EXISTS. Three times in nine patches the EW lane asserted that something was
not in the corpus, on the strength of a grep scoped to two or three paths:

  4003  "(H1) and (H-NESS) are idle since 8 June"        -> retracted at 4004
  4007  "the route ran on the wrong object"               -> withdrawn at 4008
  4011  "'10% of the radius of the PSR' appears nowhere"  -> retracted at 4012

At 4008, having made the error twice, the lane wrote its own remedy into the reasoning
fragment: "the remedy is not more care; it is a SECOND GREP before any claim of the form
'the corpus says X'." Three patches later it made the error again. A rule written as
advice to oneself is not a rule -- which is the same lesson todolist.md's D-9 and
code/deferral_gate.py already record for deferrals. So: mechanize it.

An absence claim is cheap to make, expensive to retract, and uniquely damaging: it tells
the next worker not to look. Unlike a wrong number, nothing downstream contradicts it.

USAGE:  python3 code/absence_gate.py [<commit-ish>]     (default HEAD)
EXIT:   0 pass, 1 an absence claim with no evidence of an unscoped search.
OVERRIDE: put SEARCHED-UNSCOPED in the commit message, naming the pattern searched.
"""
import re, subprocess, sys

ABSENCE = [
    r"appears?\s+nowhere", r"occurs?\s+in\s+exactly\s+one",
    r"\bnowhere\s+in\s+the\s+corpus\b", r"\bnot\s+in\s+the\s+corpus\b",
    r"\bis\s+not\s+constructed\s+anywhere\b", r"\bdoes\s+not\s+(?:exist|appear)\s+anywhere\b",
    r"\bno\s+\w+\s+(?:is|are)\s+registered\b", r"\bidle\s+since\b",
    r"\buntouched\s+since\b", r"\bnobody\s+has\b", r"\bnever\s+(?:been\s+)?(?:run|computed|checked)\b",
    r"\bthe\s+corpus\s+does\s+not\b", r"\bfound\s+nothing\b", r"\bzero\s+hits\b",
    r"\bI\s+(?:can|could)\s+not\s+find\b", r"\banywhere\s+I\s+can\s+find\b",
]
# Evidence that the search was actually unscoped.
# Searched paths that are easy to miss. If a patch makes an absence claim and has NOT
# named one of these, the evidence is probably still scoped. Added at 4031, after the
# EW lane spent 4008-4030 re-deriving results that sat in Development/transcripts/ --
# a directory none of its greps had ever touched.
EASY_TO_MISS = ["Development/transcripts", "archive/", "founders_voice", "Development/"]
EVIDENCE = [
    r"SEARCHED-UNSCOPED", r"grep\s+-r\w*\s+[^\n]*\s\.\s*$", r"grep\s+-r\w*\b[^\n]*--include",
    r"git\s+grep", r"unscoped", r"across the (?:full |whole )?(?:tree|repo|corpus)",
    r"repo-wide", r"whole tree",
]

def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    msg = subprocess.run(["git","log","-1","--format=%B",ref],
                         capture_output=True,text=True,errors="replace").stdout
    diff = subprocess.run(["git","show","--format=","--unified=0",ref],
                          capture_output=True,text=True,errors="replace").stdout
    # research_frontier.md's prepend convention re-adds the PREVIOUS header line as an
    # "Earlier **Last updated:**" line on every patch, so historical claims quoted there
    # fire as if they were new. Skip those: they are records, not claims being made now.
    # (Added at 4017, after this gate produced exactly that false positive on itself. A
    # gate with systematic false positives gets ignored, which is the failure mode it
    # was built against.)
    # research_frontier.md and the sector files prepend a new header and push the old
    # one onto the SAME line after "Earlier **Last updated:", so a single added line
    # carries the entire history of that file -- every retracted claim ever quoted
    # there fires as if it were new. Truncate each added line at the first such marker
    # and keep only the part being written NOW.
    # (4017 skipped lines STARTING with the marker, which missed the sector files,
    # where it appears mid-line. A gate with systematic false positives gets ignored,
    # which is the failure mode it was built against; fixed properly here at 4018.)
    def _now(l):
        i = l.find("Earlier **Last updated:")
        return l if i < 0 else l[:i]
    added = "\n".join(_now(l[1:]) for l in diff.splitlines()
                      if l.startswith("+") and not l.startswith("+++"))
    body = msg + "\n" + added

    hits = []
    for pat in ABSENCE:
        for m in re.finditer(pat, body, re.I):
            s = body[max(0,m.start()-70):m.end()+70].replace("\n"," ")
            hits.append((m.group(0), s.strip()))
    if not hits:
        print(f"absence_gate: {ref} — no absence claims. PASS"); return 0

    ev = [p for p in EVIDENCE if re.search(p, body, re.I|re.M)]
    print(f"absence_gate: {ref} — {len(hits)} absence claim(s); "
          f"evidence of unscoped search: {ev if ev else 'NONE'}")
    for w,s in hits[:8]:
        print(f"  «{w}»  {s[:150]}")
    missed=[d for d in EASY_TO_MISS if d not in body]
    if ev and missed:
        print(f"\nEvidence present, but these easy-to-miss paths are unnamed: {missed}")
        print("Not a failure -- but 4008-4030 re-derived three months of work that sat in")
        print("Development/transcripts/, and no grep in that arc ever touched it.")
    if ev:
        print("\nEvidence present. PASS — but the claim is only as good as the pattern searched:")
        print("an unscoped grep for the WRONG STRING is still a scoped grep. 4011 searched")
        print("'10% of' and missed 'F-E2-3', 'D-ARC-GAMMA', 'shell thickness' and the")
        print("founders_voice/ files that carried the quantity under other names.")
        return 0
    print("\nFAIL — an absence claim with no evidence of an unscoped search.")
    print("Run it unscoped, over the WHOLE tree, and try more than one phrasing of the")
    print("thing you say is missing. Then either drop the claim or add SEARCHED-UNSCOPED")
    print("to the commit message naming the patterns you searched.")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
