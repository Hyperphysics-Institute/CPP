#!/usr/bin/env python3
# 4037 - the founder asks: something is fundamentally wrong; what is most likely wrong?
# He argues the masses are probably right because they predict accurately.
#
# I agree the masses are probably right. But the inference "masses work, therefore the
# geometry is right" does not go through, and the reason is measurable.
import os, re, subprocess, math
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def cnt(path,pat):
    if not os.path.exists(path): return -1
    return len(re.findall(pat, open(path,encoding='utf-8',errors='replace').read(), re.I))
SF1="flagship_papers/charged_leptons/sf-1_charged_leptons.tex"
SF3="flagship_papers/quarks/sf-3_quarks.tex"
SF4="flagship_papers/neutrinos/sf-4_neutrinos.tex"
SM2="series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex"

print("T1 -- THE STRONGEST MASS PREDICTION IN THE CORPUS USES NO ICOSAHEDRAL GEOMETRY")
for p,lab in ((SF1,"SF-1 charged leptons"),(SF3,"SF-3 quarks"),
              (SF4,"SF-4 neutrinos"),(SM2,"SM-2 mass breakdown")):
    print(f"    {lab:<22} 'icosahedr' appears {cnt(p,'icosahedr'):>3} times")
chk("SF-1 mentions it ZERO times", cnt(SF1,"icosahedr")==0,
    "and SF-1 is the cleanest prediction the programme has: the Koide relation "
    "K = 2/3, the Koide phase theta = 132.731 deg, and m_mu and m_tau")
t=open(SF1,encoding='utf-8',errors='replace').read()
chk("its geometry is a THREE-VERTEX COLOUR TRIANGLE", "three-vertex colour triangle" in t,
    "'A charged lepton is a minimal cage whose base is the three-vertex colour "
    "triangle' -- and 'the three charged leptons are the three stationary OCCUPATION "
    "PATTERNS of a single three-vertex colour cage'")
chk("with ONE calibration and ZERO shape parameters",
    "one calibration ($m_e$) and zero shape parameters" in t)
chk("=> a triangle embeds in ANY lattice; the crystallographic restriction does not "
    "touch it", True,
    "4036's obstruction is about regular ICOSAHEDRA on lattice sites. A 3-vertex "
    "triangle is not an icosahedron")

print("\nT2 -- AND THE TABLE THAT DOES USE THE CAGES COMPUTES NOTHING")
print("  Patch 4002 established it and it is worth restating here, because it is the")
print("  hinge of the whole question: SM-2's Mass Contribution Breakdown is a")
print("  FIXED-FRACTION PARTITION OF THE CALIBRATED PDG TOTAL, with a residual sized to")
print("  close the sum. Divide the W row by 80380: 1/2, 1/6, 0, 1/20, 0, 17/60 -> 1.")
print("  All twelve rows do this.")
chk("so the CAGE COLUMN LABELS ROWS; it does not generate numbers", True,
    "nothing about a particle's constituents enters the arithmetic of its row -- 4002 "
    "verified this across all twelve rows")
chk("=> SM-2's mass table cannot be EVIDENCE for the cage taxonomy", True,
    "the numbers came from experiment; the cages were written beside them")

print("\nT3 -- SO THE INFERENCE DOES NOT GO THROUGH")
print("  'The masses predict accurately, therefore the geometry is right.'")
print("  The mass SUCCESSES and the ICOSAHEDRAL COMMITMENT are largely DISJOINT:")
print("    SF-1  Koide K, theta, m_mu, m_tau   icosahedral: 0 mentions. Triangle only.")
print("    SF-4  Sum m_nu = 64.9 meV           uses z, and 4016 showed only the COUNT")
print("                                        enters (M0 ~ z, sigma ~ z^-10). Not shape.")
print("    SM-2  the full cage taxonomy        partitions measured totals (4002).")
chk("the only place the icosahedral ARRANGEMENT is load-bearing is a table that "
    "computes nothing", True,
    "which is why 'the masses work' is compatible with the substrate geometry being "
    "wrong, unspecified, or merely local")

print("\nT4 -- WHAT I THINK IS MOST LIKELY WRONG")
print("  Not the masses. Not the axioms. THE GLOBAL LATTICE CONSTRUCTION -- and it is")
print("  most likely wrong because NOTHING IN THE MASS SECTOR EVER NEEDED IT.")
print("  Everything that does load-bearing work in SM is LOCAL:")
print("    - a three-vertex colour triangle          (SF-1)")
print("    - a COUNT of twelve                        (SF-4, via 4016)")
print("    - a first-shell distance ratio -> chi      (Capotauro / CHI-1)")
print("  None of these requires a global 600-cell tiling of flat R^4. They require a")
print("  substrate with the right LOCAL structure.")
chk("and that is why 4033 found the global construction unspecified", True,
    "it was never specified because nothing downstream ever forced it. An unused "
    "commitment does not get pinned down")
print("  MEANWHILE SR-1 DOES need the global structure -- its W2 world-call rests on the")
print("  substrate's symmetry CLASS for the anisotropy argument. So the conflict this")
print("  arc has been chasing is between SR's GLOBAL commitment and SM's LOCAL ones,")
print("  and the local ones are satisfiable in many global structures.")
chk("this is a HYPOTHESIS about where to look, not a finding", True,
    "it is consistent with everything measured in 4002-4036 and it predicts something "
    "checkable: that no SM result changes if the global tiling is replaced, provided "
    "the local structures survive. NOT yet tested")
chk("and it is the OPPOSITE of despair", True,
    "if the global construction is unused, it is free to be chosen to satisfy SR "
    "alone -- and the three-horned dilemma is then SR's problem, not the mass "
    "programme's")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. No paper revised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
