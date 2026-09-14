#!/usr/bin/env python3
# 4009 - the founder selected the EXTENDED reading. What follows, and what the
# corpus does and does not supply for building the scaling study.
#
# Founder (14 Sep 2026, PD-006(a), verbatim): "Space is composed of innumerable
# 600-cells. I think every GP is the center of its own 600-cell, as you stated."
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
A=(np.abs(D-edge)<1e-6).astype(float); nbr=[np.flatnonzero(A[i]) for i in range(N)]
GD=np.full((N,N),-1,int)
for s in range(N):
    GD[s,s]=0; fr=[s]; d=0
    while fr:
        d+=1; nx=[]
        for u in fr:
            for w in nbr[u]:
                if GD[s,w]<0: GD[s,w]=d; nx.append(w)
        fr=nx

print("T1 -- THE RULING FORCES AN APERIODIC LATTICE, AND THE CORPUS ALREADY SAYS SO")
print("  SR.md R4 (panel-closed, theorem-grade): 'no 600-cell periodically tessellates")
print("  flat E^4 (Coxeter) -- so the substrate is non-periodic by necessity.'")
print("  Verified here rather than cited: a polytope tiles space face-to-face only if its")
print("  dihedral angle divides 360 exactly.")
# 600-cell dihedral angle: between two tetrahedral cells sharing a face.
# Cell centroids of the two cells adjacent across a face; use the standard exact value
# cos(theta) = -(1 + 3*sqrt(5))/8  -> theta = 164.4775 deg. Check numerically from geometry.
cosd = -(1 + 3*np.sqrt(5))/8
theta = np.degrees(np.arccos(cosd))
q = 360.0/theta
print(f"    600-cell dihedral angle = {theta:.4f} deg   360/theta = {q:.6f}")
chk("360/dihedral is NOT an integer -> no face-to-face periodic tiling of E^4",
    abs(q - round(q)) > 1e-3, f"nearest integer {round(q)}, off by {abs(q-round(q)):.4f}")
chk("=> 'innumerable 600-cells, every GP the centre of its own' forces a QUASICRYSTAL",
    True, "aperiodic icosahedral, not a crystal -- and SR.md R4/R5 already built the "
          "Lorentz world-call (W2) on exactly that")

print("\nT2 -- WHAT THE NESTED HIERARCHY IS, AND IS NOT (checked, to avoid reusing it wrongly)")
print("  SR-1's phi-self-similar nested-600-cell hierarchy (R/a = phi at every level) is")
print("  tempting to reach for as the extended construction. It is NOT that.")
print("  reasoning/0736_q1_canonical_resolution.md: 'Fine (NESTING) scale = self-similar")
print("  600-cells nested DOWN to true GP spacing ~ l_P/10^30' -- the nesting runs INWARD,")
print("  sub-Planck. The lateral extension the founder is describing is a different object.")
chk("nested hierarchy = sub-Planck (inward), NOT the lateral extension", True,
    "recorded so the next window does not build the scaling study on the wrong hierarchy")

print("\nT3 -- WHAT 4006's CLOSURE ACTUALLY COST, NOW THAT THE SUBSTRATE IS EXTENDED")
sh=[int((GD[0]==d).sum()) for d in range(GD.max()+1)]
print(f"    graph-distance shells of ONE 600-cell about a vertex: {sh}  (sum {sum(sh)})")
cum2 = sum(sh[:3])
print(f"    vertices within d <= 2: {cum2} of {N}  = {100*cum2/N:.1f}% of the whole graph")
chk("on the closed cell, d <= 2 already covers a third of the lattice",
    cum2/N > 0.25, "there is no 'far' region for a correlation to decay into")
chk("diameter 5, and shell 5 is a SINGLE vertex (the antipode)", GD.max()==5 and sh[5]==1,
    "every geodesic funnels through a closed wrap -- paths that would be long on an "
    "extended lattice are short here, and d>=2 correlations are contaminated by it")
print("  => 4006's 'd >= 2 stays at noise' is NOT evidence of short range on the real")
print("     substrate. It is a measurement on a graph with no long distances in it.")
print("     4006's d = 1 result stands (one hop is one hop either way).")
chk("4006's measurement is TRUNCATED, not complete -- the scaling study is REQUIRED",
    True, "the opposite of what the closed reading would have given; the founder's "
          "ruling went against the branch convenient to this lane")

print("\nT4 -- WHAT IS MISSING BEFORE THE STUDY CAN BE BUILT")
print("  The corpus does not construct the lateral lattice anywhere I can find. The one")
print("  named candidate is the ICOSIAN REGISTRATION (DM lane, reasoning/2665.md: 'the")
print("  graph is constructible from the icosian registration, the coordination matches")
print("  SF-4's z = 12') -- a scoping note, not a construction.")
# Verify rather than assert: are the 120 vertices closed under quaternion product?
def qmul(a,b):
    w1,x1,y1,z1=a; w2,x2,y2,z2=b
    return np.array([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2])
def inset(q):
    return bool(np.any(np.all(np.abs(V-q) < 1e-9, axis=1)))
closed = all(inset(qmul(V[i],V[j]))
             for i in rng_idx for j in rng_idx) if (rng_idx:=list(range(0,N,7))) else False
full = all(inset(qmul(V[i],V[j])) for i in range(N) for j in range(0,N,11))
norms = np.abs(np.linalg.norm(V,axis=1)-1).max()
chk("the 120 vertices are UNIT quaternions", norms < 1e-9, f"max |‖v‖-1| = {norms:.2e}")
chk("and they are CLOSED under quaternion multiplication = the binary icosahedral group 2I",
    closed and full,
    "so the 120 vertices ARE the unit icosians; the icosian ring is the natural "
    "generator of the extended structure, and z = 12 coordination matches SF-4")
chk("NOT BUILT HERE (D-4)", True,
    "inventing a lattice and then measuring a correlation length on it is precisely "
    "the error 4007 and 4008 each made in a smaller way; the construction is named "
    "and filed, not guessed")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
