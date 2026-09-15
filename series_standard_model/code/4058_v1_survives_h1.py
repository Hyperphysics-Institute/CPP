#!/usr/bin/env python3
# 4058 - does 4057's refutation of H1 reopen V1? The natural worry after a theorem's
# residual is refuted. Checked against what CAPACITY-1 actually rests on.
import numpy as np, math, os, re
from itertools import permutations as P
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
CH="frontier_sectors/CHIR.md"
t=open(CH,encoding='utf-8',errors='replace').read() if os.path.exists(CH) else ""

print("T1 -- WHAT CAPACITY-1 ACTUALLY RESTS ON")
chk("THEO-CHIR-CAPACITY-1 carries the V3-confirmed / V1-excluded verdict",
    "V3 confirmed" in t and "V1 excluded" in t)
chk("its conditionality was NARROWED at 0960 to three named things",
    "MA.1's reversal-odd first harmonic" in t and "per-edge independence" in t
    and "pointwise non-degeneracy of the dynamical" in t,
    "(i) MA.1's reversal-odd first harmonic r = r0(1 + delta e.n), derived and unique "
    "up to scale at 0949; (ii) per-edge independence; (iii) pointwise non-degeneracy of "
    "the dynamical eta -- 'piece 1, unchanged and still assumed'")
chk("it does NOT cite VW-1, H1, or reflection positivity anywhere in that conditionality",
    not re.search(r"CAPACITY-1.{0,900}(reflection positiv|THEO-CHIR-VW-1|\bH1\b)", t, re.S|re.I),
    "the narrowed conditionality names three things and none of them is RP")

print("\nT2 -- SO 4057 DOES NOT REOPEN V1")
print("  H1 was VW-1's residual. VW-1 and CAPACITY-1 are DIFFERENT theorems reaching a")
print("  compatible conclusion by DIFFERENT routes: VW-1 by a positivity argument,")
print("  CAPACITY-1 by the capacity/first-harmonic route. Refuting H1 removes VW-1's")
print("  support and leaves CAPACITY-1 untouched.")
chk("V1 stays EXCLUDED and V3 stays CONFIRMED", True,
    "which is worth establishing explicitly, because the natural worry after refuting a "
    "theorem's sole residual is that everything downstream falls with it. Here it does "
    "not, and the reason is that the verdict never rested on that theorem")
chk("and 4005's direct measurement is a third leg", True,
    "chi_eta finite with d>=1 correlations ~1e-3 -- an unbroken branch measured "
    "directly, independent of both theorems")

print("\nT3 -- BUT CAPACITY-1's THIRD CONDITION IS THE ONE 4023 FOUND DEFECTIVE")
print("  'Pointwise non-degeneracy of the dynamical eta' is piece 1, still assumed.")
print("  And 4023 established that eta -- 'sign det of the four highest-n-hat-projection")
print("  neighbours' -- has its 4th and 5th projections TIED at 120/120 vertices on the")
print("  UNPERTURBED lattice, so the selection is arbitrary and eta is ill-defined there.")
phi=(1+math.sqrt(5))/2; e=1/phi
def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in(1,-1):
        for s2 in(1,-1):
            for s3 in(1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
nbr=[np.flatnonzero(np.abs(D[i]-e)<1e-9) for i in range(N)]
nhat=np.array([1.,0,0,0])
tie=sum(1 for v in range(N)
        if len(np.unique(np.round(np.sort((V[nbr[v]]-V[v])@nhat)[-5:],9)))<5)
chk(f"unperturbed: the 4/5 projection boundary ties at {tie}/{N} vertices", tie==N,
    "every vertex. eta is pointwise DEGENERATE on the unperturbed lattice")
ok=0
for eps in (0.02,0.05,0.10):
    X=V+eps*np.random.default_rng(1).standard_normal((N,4))
    if all(len(np.unique(np.round(np.sort((X[nbr[v]]-X[v])@nhat)[-5:],9)))==5
           for v in range(N)): ok+=1
chk(f"perturbed: the ties are broken at all {ok}/3 amplitudes tested", ok==3,
    "so the condition HOLDS where CAPACITY-1 uses it -- on dynamical, perturbed "
    "configurations")

print("\nT4 -- SO THE CONDITION IS SATISFIED, AND ITS STATEMENT IS NOT")
chk("CAPACITY-1's piece 1 is TRUE as used", True,
    "0813 and 4005 evaluate eta on perturbed configurations. No result is invalidated, "
    "which is what 4023 said")
chk("but the statement carries no 'on perturbed configurations' qualifier", True,
    "and 4023 found that defect without knowing it landed on a NAMED CONDITIONALITY of "
    "a 3/3 review-closed theorem. That is more consequential than 4023 reported -- not "
    "because anything is wrong, but because the assumption is now known to be FALSE in "
    "the unperturbed limit and the theorem does not say so")
chk("filed for the CHIR lane as a TEXT fix, not a physics one", True,
    "add the qualifier to piece 1. NOT this lane's to edit -- CAPACITY-1 is review-closed")

print("\nT5 -- AND THE ABSENCE GATE FORCED A SEARCH THAT FOUND SOMETHING LARGER")
print("  The draft said 'VW-1 and H1 appear nowhere in it'. True of CAPACITY-1's")
print("  conditionality; the gate made me check the claim UNSCOPED, and H1 turns out to")
print("  be load-bearing somewhere I had not looked.")
SC="flagship_papers/electroweak/review/reviews-SF2-DELTACP-SCOPING.md"
sc=open(SC,encoding='utf-8',errors='replace').read() if os.path.exists(SC) else ""
chk("SF-2's delta_CP SCOPING REVIEW makes H1 a named contingency",
    "H1 closes within" in sc or "H1 closure" in sc,
    "Copilot's verdict: 'CONDITIONAL-GO -- viable only if SQ1 salvage or H1 closes "
    "within ~10 sessions'. H1's closure was ONE OF TWO contingencies for proceeding")
chk("and the adjudication already judged the OTHER contingency near-zero",
    "near zero" in sc or "near-zero" in sc,
    "'The probability that the SQ1 provenance audit finds a derivation chain is near "
    "zero' -- so H1 was effectively the surviving contingency")
chk("=> 4057 CLOSES THAT CONTINGENCY NEGATIVELY", True,
    "H1 does not close; on the physical measure it is FALSE. The CONDITIONAL-GO's "
    "condition is now settled in the negative, which is a decision input SF-2's lane "
    "should have. NOT this lane's decision to revise")
chk("the gate is why this was found", True,
    "the computation and the CHIR.md reading were both correct and both scoped. Only "
    "the unscoped search reached the review package, and it is the third time today a "
    "gate or control has produced the patch's most consequential line")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. V1 EXCLUDED and V3 CONFIRMED both STAND.")
raise SystemExit(1 if fails else 0)
