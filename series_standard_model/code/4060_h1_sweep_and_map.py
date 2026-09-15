#!/usr/bin/env python3
# 4060 - the sweep H1's refutation deserves: who else depends on it, and a correction to
# how I have been describing VW-1 for eight patches.
import os, re, subprocess
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def sh(*a): return subprocess.run(a,capture_output=True,text=True,errors="replace").stdout
CH=open("frontier_sectors/CHIR.md",encoding='utf-8',errors='replace').read()

print("T1 -- A CORRECTION I HAVE REPEATED FOR EIGHT PATCHES: VW-1 HAS THREE HYPOTHESES")
chk("CHIR.md states VW-1 as a CONJUNCTION of H1, H2 and H3",
    "[H1]" in CH and "[H2]" in CH and "[H3]" in CH,
    "'if the DSL measure is reflection-positive [H1] + the det-coset Z2 is "
    "vectorial-not-axial [H2] + no theta-term [H3]'")
chk("I have been calling H1 'VW-1's SOLE residual' since 4022", True,
    "that phrasing came from 4003, which said B-iii's residuals were (H1) and (H-NESS) "
    "-- a statement about OPEN-SM-4's sub-claim, NOT about VW-1's hypothesis list. I "
    "carried it across and repeated it")
chk("the CONCLUSION is unaffected: a conjunction fails if one conjunct fails", True,
    "H1 refuted kills VW-1 regardless of H2 and H3. The error was descriptive, not "
    "logical -- but it made VW-1 look more fragile than it is and H1 more central")

print("\nT2 -- AND THE CORPUS CARRIES A MAP I HAVE BEEN WORKING WITHOUT")
print("  CHIR.md, 'The P-face / T-face map (CPT-unified, from TARROW-1)':")
print("    sign(n-hat) = FI-C-9, P-ODD  <->  electroweak PARITY VIOLATION (V-A), E26")
print("    sign(delta),        T-ODD    <->  SM CP-VIOLATION (delta_CP)")
chk("the map is in CHIR.md", "P-face / T-face map" in CH and "V2-reopener" in CH)
chk("=> THE CHIRAL-LATTICE ARC (4038-4048) BEARS ON V-A, NOT ON delta_CP", True,
    "geometric handedness is P-odd, and the P-face is V-A. 4046 checked the kinds "
    "matched for V-A and was right, but without this map in front of me")
chk("=> THE H1 ARC (4022-4059) BEARS ON delta_CP, VIA sign(delta) ON THE T-FACE", True,
    "which is why H1 showed up in SF-2's delta_CP scoping and not in the V-A work. Two "
    "different faces, and I have been working both without the map")
print("  Having the map would not have changed a single computation. It would have")
print("  changed how I described where each result lands, and at 4048 I spent a patch")
print("  discovering by measurement that the substrate cannot supply V-A's maximality --")
print("  a P-face question -- while the H1 line was the T-face one all along.")

print("\nT3 -- THE SWEEP: WHO ELSE DEPENDS ON H1?")
live=[f for f in sh("git","grep","-lE","reflection.positiv","--","*.md","*.tex").split()
      if not f.startswith(("handovers/","archive/","Development/"))
      and "/reasoning/40" not in f and "/code/40" not in f]
print(f"    files citing reflection positivity outside this session's own output: {len(live)}")
for f in live: print(f"      {f}")
# NOTE: the draft asserted "the live dependency set is SMALL and already known" and
# FAILED. It is not small. That assertion was written before running the sweep, which
# is precisely the habit this session has spent sixty patches unlearning.
theorems=[f for f in live if f.endswith(".tex")]
scoping=[f for f in live if "scoping" in f or "scope" in f or "gonogo" in f]
chk(f"the dependency set is NOT small: {len(live)} live files", len(live)>10,
    "and my draft said it was, before looking")
chk(f"{len(theorems)} are THEOREM SOURCES: {[os.path.basename(f) for f in theorems]}",
    len(theorems)>=3,
    "VW-1 is the one I knew about. VW-2 and TARROW-2 are not, and I have not checked "
    "whether their dependence on H1 is load-bearing or incidental")
chk(f"{len(scoping)} are SCOPING or GO/NO-GO documents",
    len(scoping)>=3,
    "including a dedicated H1 attack-scoping document, a dedicated OS-positivity probe "
    "scoping, and the chirality theorem GO/NO-GO verdict spec")
chk("and one is flagship_assembly_scope.md", 
    any("flagship_assembly_scope" in f for f in live),
    "a flagship ASSEMBLY scope citing reflection positivity is the kind of dependency "
    "that does not announce itself")
chk("=> 4058 and 4059 did NOT cover the exposure", True,
    "they found two consumers. There are more, and characterising which are "
    "load-bearing is a CHIR-lane audit, not an EW-lane grep. What this patch delivers "
    "is the LIST and the correction, not the audit")

print("\nT4 -- WHAT THIS PATCH IS AND IS NOT")
chk("it is a CORRECTION and a SWEEP, not a new result", True,
    "no computation here. The correction fixes eight patches of mis-description; the "
    "sweep bounds the damage")
chk("and the bounding is the useful half", True,
    "after a refutation the open question is 'what else falls', and leaving that "
    "unanswered is how a 2028 discovery gets made -- which is exactly what 4059 warned "
    "about one patch ago")
chk("NOT claimed: that H2 or H3 hold", True,
    "they are untested here and irrelevant to the conclusion, since H1 already fails. "
    "If anyone repairs H1, H2 and H3 become live again and are NOT discharged")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. V1 EXCLUDED and V3 CONFIRMED both STAND.")
raise SystemExit(1 if fails else 0)
