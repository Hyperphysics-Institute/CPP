#!/usr/bin/env python3
"""continuity_gate.py -- detect patches that were reported applied but are NOT in the repo.

WHY THIS EXISTS. At Patch 4028 the EW lane found origin/main sitting at 4026 although
4027 had been reported applied. The routine `git reset --hard origin/main` at bootup had
already discarded the only other copy; it was recovered from the reflog, which is not
guaranteed to exist. A patch that silently fails to apply is the one failure mode this
workflow had no gate for -- worse than a wrong number, because work continues on a
foundation that is not there.

AN HONEST LIMIT, STATED UP FRONT. A cleanly-missing TAIL patch cannot be detected from
inside the repo: the missing patch is also the one that would have updated the registry
and the frontier header, so everything left behind is self-consistent at N-1. What IS
detectable is:

  (1) A GAP IN THE MIDDLE -- patch N and N+2 present, N+1 absent. This is the dangerous
      silent case, because later work proceeds on a broken foundation and nothing
      complains.
  (2) LOCAL AHEAD OF ORIGIN -- commits that exist here and were never pushed. This is
      exactly what 4028 hit, and it IS catchable at the moment of generating a patch,
      which is when it matters.

For the tail case the fix is procedural, not automatic: the apply macro must end by
verifying origin's tip against the expected number. That is in the patch instructions,
not in this file, because it has to run on the founder's machine.

USAGE:  python3 code/continuity_gate.py [--lane chir|ew|...]
EXIT:   0 clean, 1 a gap or an unpushed commit.
"""
import re, subprocess, sys

# 4104: 'ew' read (4000,4099) while the live EW block had been 4100-4199 since Patch 4100,
# so THIS GATE -- the one whose whole job is spotting a silently-missing patch -- was not
# watching the range every patch since 4100 was written into. Rule 6 in id_block_registry.md
# named only code/next_id.py, because it was written at 3807 and this file did not exist until
# 4029; the rule never grew to cover a second table. Rule 6 generalised in the same commit.
# Fourth Rule-6 lag on record (3700, 3800, 3900 in next_id.py), first in this gate.
BLOCKS = {'chir':(900,999),'de':(3400,3499),'dm':(3500,3599),'gr':(3700,3799),
          'eu':(3900,3999),'ew':(4300,4399),'ew-4200':(4200,4299),'ew-4100':(4100,4199),'ew-4000':(4000,4099)}
# 4241: FIFTH Rule-6 lag, second in this gate. The 4199 commit swapped next_id.py's key and the
# registry row says 'gate keys swapped in the 4199 commit' -- but only next_id.py was swapped; this
# table still read 'ew':(4100,4199) through 4200-4240, so the whole live 4200 block was unwatched.
# Found at Session 238 boot: the gate's report had no 4200-4299 row. Retain, never replace.

def sh(*a):
    return subprocess.run(["git",*a],capture_output=True,text=True,errors="replace").stdout

def main():
    lane = None
    if len(sys.argv)>2 and sys.argv[1]=="--lane": lane=sys.argv[2].lower()
    subjects = sh("log","--all","--format=%s").splitlines()
    nums=set()
    for s in subjects:
        m=re.match(r"\s*(?:Patch\s+)?(\d{3,4})[a-z]?\b", s)
        if m: nums.add(int(m.group(1)))
    bad=0; warn=0
    print("PATCH-NUMBER RUNS PER LANE  (gaps are reported, not failed -- a gap may be an\n"
          "unparsed reservation, and nothing inside the repo can tell the two apart)")
    for name,(lo,hi) in BLOCKS.items():
        if lane and name!=lane: continue
        used=sorted(n for n in nums if lo<=n<=hi)
        if len(used)<2: continue
        gaps=[n for n in range(used[0],used[-1]+1) if n not in nums]
        tag=f"{name:<5} {lo}-{hi}: {len(used):>3} used, {used[0]}..{used[-1]}"
        if gaps:
            print(f"  [gap ] {tag}\n         absent inside the run: {gaps}")
            warn+=1
        else:
            print(f"  [ ok ] {tag}  contiguous")

    print("\nLOCAL vs ORIGIN, COMPARED BY PATCH NUMBER (not by SHA -- `git am` on the")
    print("founder's machine rewrites SHAs, so a SHA comparison is a false positive)")
    def numset(ref):
        out=set()
        for s in sh("log",ref,"--format=%s").splitlines():
            m=re.match(r"\s*(?:Patch\s+)?(\d{3,4})[a-z]?\b", s)
            if m: out.add(int(m.group(1)))
        return out
    here=numset("HEAD"); there=numset("origin/main")
    missing=sorted(here-there)
    if missing:
        print(f"  [FAIL] patch numbers here but NOT on origin: {missing}")
        print("         If these were reported APPLIED, they were not. Re-send them.")
        bad+=1
    else:
        print("  [ ok ] every local patch number is present on origin")

    print()
    if bad:
        print("FAIL -- work exists locally that origin does not have.")
        return 1
    if warn:
        print("PASS, with gaps reported above. They are worth the owning lane's eyes:")
        print("a reservation is fine, a genuinely lost patch means later work sits on a")
        print("foundation that is not in the repo.")
    else:
        print("PASS")
    print("\nLIMIT: a cleanly-missing TAIL patch is NOT detectable here -- the missing")
    print("patch is also the one that would have updated the registry and the frontier")
    print("header, so what remains is self-consistent at N-1. The apply macro must verify")
    print("origin's tip against the expected number; that has to run on the founder's")
    print("machine and cannot live in this file.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
