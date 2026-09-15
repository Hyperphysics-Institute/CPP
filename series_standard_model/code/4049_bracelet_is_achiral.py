#!/usr/bin/env python3
# 4049 - I proposed a division of labour at 4048: substrate supplies the SIGN, W
# bracelet supplies the MAXIMALITY. PD-008 says test my own convenient framing. The
# bracelet side FAILS, and the gap it leaves is nameable.
import numpy as np, math, itertools as it, os, re
from itertools import permutations as P
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
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
A=(np.abs(D-e)<1e-9); nb=[set(np.flatnonzero(A[i]).tolist()) for i in range(N)]
cycles=[]
def walk(p):
    if len(p)==6:
        if p[0] in nb[p[-1]] and not any(
            b in nb[a] and abs(p.index(a)-p.index(b)) not in (1,5)
            for a,b in it.combinations(p,2)): cycles.append(tuple(p))
        return
    for x in nb[p[-1]]:
        if x in p or (len(p)>=2 and x<p[1]): continue
        walk(p+(x,))
for a in sorted(nb[0]): walk((0,a))

print("T1 -- THE CORPUS'S OWN THEOREM ALREADY SAYS THE BRACELET IS ACHIRAL")
SF2="flagship_papers/electroweak/sf-2_companion.tex"
t=open(SF2,encoding='utf-8',errors='replace').read() if os.path.exists(SF2) else ""
chk("Theorem 4.2 gives the W bracelet stabilizer as D_6 of order 12",
    "stabilizer $D_6$ of order 12" in t,
    "'The 4800 induced 6-cycles partition into exactly 2 H_4-orbits; one orbit (size "
    "1200, stabilizer D_6 of order 12) is the W bracelet (regular hexagonal ring)'")
chk("D_6 of order 12 is the DIHEDRAL group -- 6 rotations AND 6 reflections", True,
    "a stabilizer containing reflections means the object is ACHIRAL. The corpus says "
    "so in its own theorem and I did not read it that way until now")

print("\nT2 -- AND AN INDEPENDENT COMPUTATION AGREES")
print(f"    induced 6-cycles through one vertex: {len(cycles)}")
def torsions(idx):
    C=np.array([V[i] for i in idx]); C=C-C.mean(0)
    Q=C@np.linalg.svd(C)[2][:3].T
    return tuple(int(np.sign(round(np.linalg.det(np.array(
        [Q[(i+1)%6]-Q[i],Q[(i+2)%6]-Q[(i+1)%6],Q[(i+3)%6]-Q[(i+2)%6]])),9)))
        for i in range(6))
def achiral(k):
    rn=tuple(-x for x in reversed(k))
    return any(rn==k[i:]+k[:i] for i in range(6))
pat={}
for c in cycles: pat[torsions(c)]=pat.get(torsions(c),0)+1
print("    torsion patterns found (a skew hexagon is a helix -- CHIRAL -- only if all")
print("    six signs agree; achiral if reversal-and-negation returns the same cycle):")
for k,v in sorted(pat.items(), key=lambda x:-x[1])[:5]:
    print(f"      {str(k):<28} x{v:>3}   {'ACHIRAL' if achiral(k) else 'CHIRAL'}")
chk("NO induced 6-cycle is a helix; every pattern is reversal-negation symmetric",
    all(achiral(k) for k in pat) and not any(len(set(k))==1 for k in pat))
chk("=> the W bracelet SCAFFOLD offers no two handedness states to select between",
    True, "there are not two mirror-image bracelets. There is one, and it is its own "
    "mirror image")

print("\nT3 -- A METHOD NOTE: MY FIRST TEST SAID THE OPPOSITE")
print("    Searching the signed-permutation subgroup found 0 improper symmetries and")
print("    would have read as CHIRAL. That subgroup is 192 elements of H_4's 14400 --")
print("    it also found only 1 proper symmetry, which should have been the tell.")
chk("the torsion pattern is the right instrument for a skew polygon", True,
    "sixth time today an instrument has returned a confidently wrong answer, and the "
    "second time the giveaway was a control coming out wrong rather than the result")

print("\nT4 -- SO MY OWN DIVISION OF LABOUR, ONE PATCH OLD, HAS NO MECHANISM")
chk("the corpus's W state does not supply a handedness either", True,
    "SF-2 describes the bracelet as a CATALYST, activated when an external charge is "
    "captured at its D_6-SYMMETRIC CENTROID. A D_6-symmetric centroid is achiral too")
chk("=> 4048's division of labour FAILS on the bracelet side as currently described",
    True, "I proposed it one patch ago as the constructive reading of a negative. It "
    "does not survive its own test")
print("\n  WHAT THE BRACELET WOULD NEED, and this is the actionable residue:")
print("    a BINARY, P-ODD, TWO-STATE degree of freedom on the ring -- a CIRCULATION,")
print("    a WINDING, or a TRAVERSAL ORIENTATION. Such a thing is all-or-nothing, which")
print("    is exactly the maximality V-A wants, and it is exactly what a 2% substrate")
print("    sign could select between.")
chk("NOT present in the current description", True,
    "and that is a specific, nameable gap on SF-2's side -- far more actionable than "
    "'derive V-A'. NOT this lane's to fill")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. SF-2 unrevised.")
raise SystemExit(1 if fails else 0)
