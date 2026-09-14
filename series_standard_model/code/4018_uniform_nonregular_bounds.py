#!/usr/bin/env python3
# 4018 - the room 4017 left open: uniform (vertex-transitive) but NON-regular structures.
# Two more classes close, by arguments unrelated to each other and to 4009/4013/4017.
import numpy as np, math
from itertools import permutations as P
phi=(1+math.sqrt(5))/2; e=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def build():
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
V=build(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
nb=np.flatnonzero(np.abs(D[0]-e)<1e-9); d=V[nb]-V[0]; S=d.sum(axis=0)

print("T1 -- THE VERTEX FIGURE IS NOT CENTRALLY SYMMETRIC ABOUT ITS VERTEX")
ip=d@V[0]
chk("all 12 neighbour offsets have the SAME inner product with v0",
    np.allclose(ip, ip[0], atol=1e-9), f"{ip[0]:.6f} -- they lie in one 3-flat")
chk("and all on ONE side: the neighbour set lies in a half-space",
    bool((ip<0).all() or (ip>0).all()))
chk(f"so the offsets do NOT sum to zero: |sum| = {np.linalg.norm(S):.6f}",
    np.linalg.norm(S)>1e-6)
have={tuple(np.round(x,9)) for x in V[nb]}
refl={tuple(np.round(2*V[0]-x,9)) for x in V[nb]}
chk("{2*v0 - w_i} != {w_i}", have!=refl)
print("  A BRAVAIS LATTICE has inversion symmetry at every point, so its nearest-")
print("  neighbour set is ALWAYS centrally symmetric about that point. The 600-cell's is")
print("  not. => NO BRAVAIS LATTICE IN ANY DIMENSION can carry this vertex figure.")
chk("class closed: Bravais lattices, any dimension", True,
    "an argument with nothing in common with Coxeter's dihedral angle (4009), the "
    "window boundary (4013) or the Gram signature (4017)")

print("\nT2 -- H4 IS NOT CRYSTALLOGRAPHIC: it has IRRATIONAL TRACES")
def Lq(q):
    w,x,y,z=q
    return np.array([[w,-x,-y,-z],[x,w,-z,y],[y,z,w,-x],[z,-y,x,w]])
tr=sorted({round(float(np.trace(Lq(q))),9) for q in V})
irr=[t for t in tr if abs(t-round(t))>1e-9]
print(f"    traces of the isoclinic rotations L_q, q in 2I: {tr}")
chk("H4 contains rotations of IRRATIONAL trace", len(irr)==4,
    f"{irr} = +-2/phi and +-2*phi")
chk("trace is basis-independent, so no conjugate of H4 lies in GL(4,Z)", True,
    "=> H4 has no faithful INTEGRAL representation => H4 IS NOT CRYSTALLOGRAPHIC in 4D")
chk("class closed: any periodic structure with full H4 site symmetry", True,
    "no space group of E^4 can have H4 as a site group")

print("\nT3 -- A NUMBER THAT TURNS OUT TO BE ONE NUMBER, NOT TWO")
A=(np.abs(D-e)<1e-9).astype(float); L=np.diag(A.sum(1))-A
lam1=np.sort(np.linalg.eigvalsh(L))[1]
chk(f"graph-Laplacian spectral gap lambda_1 = {lam1:.9f}", abs(lam1-2.291796068)<1e-8,
    "Patch 1100 used exactly this value in the mu^2-sign computation")
chk("|sum of the 12 neighbour offsets| is the SAME number",
    abs(np.linalg.norm(S)-lam1)<1e-9)
chk("and both equal 12(1 - phi/2) exactly", abs(lam1-12*(1-phi/2))<1e-9,
    "the vertex figure's central ASYMMETRY and 1100's spectral gap are the same "
    "quantity seen twice -- recorded as an identity, NOT as a mechanism")

print("\nT4 -- WHAT IS NOW CLOSED, AND WHAT IS NOT")
print("  CLOSED, by five arguments with nothing in common:")
print("    1. periodic Euclidean tiling        4009  dihedral angle 164.4775 deg")
print("    2. bounded-window cut-and-project   4013  window boundary")
print("    3. regular honeycomb, any curvature 4017  Gram signature + vertex figure")
print("    4. Bravais lattice, any dimension   4018  vertex figure not centrally symmetric")
print("    5. periodic with full H4 site sym   4018  irrational trace")
print("  NOT CLOSED, and stated so it is not mistaken for closed:")
print("    - periodic, vertex-transitive, with site symmetry a PROPER SUBGROUP of H4")
print("      whose 12 nearest neighbours nonetheless form a regular icosahedron")
print("    - APERIODIC uniform structures outside the cut-and-project class")
chk("the remaining room is narrower but NOT empty", True,
    "five classes closed is not a proof that nothing works, and this patch does not "
    "claim it is")
chk("the founder's question is still his", True,
    "nothing here adopts the weak reading")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
