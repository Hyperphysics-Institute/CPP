#!/usr/bin/env python3
# 4008 - what A2's lattice actually IS. Run BEFORE building the scaling study 4007
# specified, because the corpus reads A2 two ways and 4007 picked one without checking.
#
#   programme_orientation s177: "In the tessellated lattice, every Grid Point is the
#     centre of its own 600-cell. Shell 7 of vertex A is Shell 1 of neighbouring vertex B."
#     -> reads as an EXTENDED lattice of many 600-cells. 4007 built on this.
#   EU lane, Patch 1300: "600-cell {3,3,5} *is* the regular tessellation of S^3";
#     "A2 -> substrate = S^3 tessellation, compact, boundary = empty."
#     -> reads as ONE closed 600-cell, 120 vertices.
#
# These are not the same substrate and they give opposite answers about whether a
# correlation length is even a well-posed question. Tested here rather than assumed.
import numpy as np
from itertools import permutations as P
phi=(1+np.sqrt(5))/2; edge=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

def build_600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    base=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[base[0]*s1,base[1]*s2,base[2]*s3,base[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V=build_600(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
radii=sorted({round(x,6) for x in D[0]})

print("T1 -- the shell structure of ONE 600-cell about a vertex")
counts=[int((np.abs(D[0]-x)<1e-6).sum()) for x in radii]
for k,(x,c) in enumerate(zip(radii,counts)): print(f"    shell {k}: r={x:.5f}  n={c:>3}")
chk("nine shells, counts 1,12,20,12,30,12,20,12,1", counts==[1,12,20,12,30,12,20,12,1])
chk(f"they exhaust the polytope: sum = {sum(counts)} = 120", sum(counts)==N,
    "so 'shell 7' is INTERNAL to one 600-cell -- it needs no second cell to exist")

print("\nT2 -- s177's WORKED EXAMPLE, TESTED")
s7=set(np.flatnonzero(np.abs(D[0]-radii[7])<1e-6))
nb0=set(np.flatnonzero(np.abs(D[0]-edge)<1e-6))
match=[b for b in range(N) if set(np.flatnonzero(np.abs(D[b]-edge)<1e-6))==s7]
anti=int(np.argmax(D[0]))
chk("shell 7 of A IS exactly shell 1 of another vertex -- the set identity HOLDS",
    len(match)==1, f"the unique such vertex is {match[0]}")
chk("but that vertex is A's ANTIPODE, not a neighbour",
    match==[anti] and anti not in nb0,
    f"vertex {anti} sits at r={D[0,anti]:.3f} (shell 8, the unique antipode); "
    f"no neighbour of A has this property")
chk("V[antipode] = -V[A]", np.allclose(V[anti], -V[0]))
print("  => s177's geometric content is RIGHT and its relation is MISSTATED: shell 7 of A")
print("     is shell 1 of A's ANTIPODE. And that is a fact ABOUT ONE CLOSED 600-CELL --")
print("     it is evidence FOR the closed reading, not for an extended lattice.")

print("\nT3 -- the closed reading, checked independently")
chk("f-vector: V - E + F - C = 120 - 720 + 1200 - 600 = 0 = chi(S^3)",
    120-720+1200-600 == 0, "the 600-cell {3,3,5} IS the regular tessellation of S^3 "
    "(EU lane Patch 1300; standard mathematics)")
chk("every vertex sees the identical shell profile (vertex-transitive)",
    all([int((np.abs(D[v]-x)<1e-6).sum()) for x in sorted({round(y,6) for y in D[v]})]==counts
        for v in range(0,N,17)),
    "which is what s177's 'every Grid Point is the centre of its own 600-cell' states -- "
    "vertex-transitivity, NOT a lattice of many cells")

print("\nT4 -- 4007's 'SCOPE ERROR' FINDING IS WITHDRAWN")
print("  4007 asserted that a single 600-cell is 'the first shell around one host vertex,")
print("  not the substrate', and that 0694/0813/1100/4005/4006 therefore ran on the wrong")
print("  object. THAT RESTED ENTIRELY ON s177's 'neighbouring vertex B' -- the one clause")
print("  in it that this script shows is misstated -- and I did not check A2's reading")
print("  anywhere else in the corpus before asserting it. The EU lane had read A2 the")
print("  opposite way since Patch 1300 and I did not look.")
chk("the assertion 'the route ran on the wrong object' is WITHDRAWN", True,
    "not established; the evidence now points the other way")
chk("what SURVIVES from 4007", True,
    "the founder ruling and its A3' resolution -- FIELD-RANGE AT ONE SHELL -- are "
    "untouched by this and stand")

print("\nT5 -- WHAT THE CLOSED READING WOULD MEAN, IF IT IS THE RIGHT ONE")
print("  The substrate would be a CLOSED 3-manifold with 120 vertices and diameter 5.")
print("  Then there is NO THERMODYNAMIC LIMIT, a correlation length in the")
print("  critical-phenomena sense is NOT A WELL-POSED QUESTION on it, and 4007's")
print("  finite-size-scaling study has nothing to scale TO.")
print("  AND 4006's MEASUREMENT WOULD BE THE COMPLETE ANSWER RATHER THAN A TRUNCATED")
print("  ONE: d = 1 correlation real, d >= 2 at noise, measured on the whole substrate.")
print("  The route would close.")
chk("NOT ASSERTED HERE (D-4)", True,
    "whether A2's substrate is literally 120 vertices, or whether 'host vertex' "
    "language elsewhere (FI-C-RC-2, the 1200 W-bracelets = 10 x 120 host vertices) "
    "implies an extended structure, is a PHYSICAL-PICTURE question -- the founder's "
    "under PD-006(a). Asked, not decided")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
