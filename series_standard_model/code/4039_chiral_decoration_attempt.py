#!/usr/bin/env python3
# 4039 - fourth attempt at building 4038's target, and it fails for a reason that
# sharpens the target.
#
# TARGET (4038): a flat-space point set with icosahedral ROTATION symmetry I (532),
# NO improper operations, nearest shell of exactly twelve.
# ATTEMPT: decorate the 600-cell chirally -- keep the rotations, break the mirrors.
import numpy as np, math, itertools as it
from itertools import permutations as P
from scipy.spatial import cKDTree
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
A=(np.abs(D-e)<1e-9)
cells=[(i,a,b,c) for i in range(N)
       for a,b,c in it.combinations([x for x in np.flatnonzero(A[i]) if x>i],3)
       if A[a,b] and A[a,c] and A[b,c]]
def syms(X):
    key={tuple(np.round(v,9)) for v in X}; pr=im=0
    for pm in it.permutations(range(4)):
        for sg in it.product((1,-1),repeat=4):
            M=np.zeros((4,4))
            for i in range(4): M[i,pm[i]]=sg[i]
            if all(tuple(np.round(M@v,9)) in key for v in X):
                if round(np.linalg.det(M))==-1: im+=1
                else: pr+=1
    return pr,im
def decorate(eps):
    dec=[]
    for (i,a,b,c) in cells:
        cen=(V[i]+V[a]+V[b]+V[c])/4
        s=np.sign(round(np.linalg.det(np.array([V[i],V[a],V[b],V[c]])),12))
        if s: dec.append(cen*(1+eps*s))
    return np.vstack([V,np.array(dec)])
def chir(X,nhat):
    T=cKDTree(X); d,_=T.query(X,k=2); nn=float(np.median(d[:,1]))
    nb=[np.array([j for j in T.query_ball_point(x,nn*1.02) if not np.allclose(X[j],x)]) for x in X]
    tot=0.0; cnt=0
    for v0 in range(0,len(X),7):
        for a in nb[v0]:
            for b in nb[a]:
                if b==v0: continue
                for c in nb[b]:
                    if c==a: continue
                    tot+=np.sign(round(np.linalg.det(
                        np.array([X[a]-X[v0],X[b]-X[a],X[c]-X[b],nhat])),12)); cnt+=1
    return tot,cnt
print("T1 -- THE ATTEMPT: decorate each of the 600 tetrahedral cells with a signed")
print("      radial offset, the sign taken from the cell's vertex determinant.")
chk(f"the 600-cell has {len(cells)} tetrahedral cells", len(cells)==600)
pr0,im0=syms(V)
print(f"    bare 600-cell: proper {pr0}, improper {im0} (signed-permutation subgroup)")
nhat=V[0]/np.linalg.norm(V[0])
res={}
for eps in (-0.10,-0.05,0.05,0.10):
    X=decorate(eps); pr,im=syms(X); t,c=chir(X,nhat); res[eps]=(pr,im,t,c)
    print(f"    eps={eps:+.2f}: {len(X)} pts, proper {pr}, improper {im}, "
          f"chirality sum {t:+.1f} over {c} paths")

print("\nT2 -- IT KILLS THE MIRRORS ... AND THE ROTATIONS WITH THEM")
chk("improper symmetries go to ZERO", all(v[1]==0 for v in res.values()),
    f"from {im0} on the bare polytope -- the mirror-breaking half worked")
chk("but the PROPER symmetries collapse too", all(v[0]<=1 for v in res.values()),
    f"from {pr0} to 1. The decoration is not rotation-equivariant, so it does not "
    "realise point group I -- it realises nothing")

print("\nT3 -- AND THE CHIRALITY IS NOT SYSTEMATIC, WHICH CONFIRMS THE DIAGNOSIS")
sums=[res[k][2] for k in (-0.10,-0.05,0.05,0.10)]
print(f"    chirality sums at eps = -0.10, -0.05, +0.05, +0.10: {sums}")
chk("the sign does NOT flip with eps", not (sums[0]*sums[3]<0),
    "a genuine chiral decoration is the mirror image of itself under eps -> -eps, so "
    "the sum MUST flip. It does not -- so what is being measured is the arbitrariness "
    "of the decoration, not a handedness")

print("\nT4 -- THE DIAGNOSIS, AND IT SHARPENS THE TARGET")
print("  The per-cell sign was sign det[V_i, V_a, V_b, V_c] with the vertices taken in")
print("  INDEX order. Index order is not a geometric property of the cell: a rotation")
print("  permutes cells but does not carry my labelling with it, so the sign is assigned")
print("  inconsistently and the decoration is effectively arbitrary.")
print("  And there is no fixing it by choosing a better order, because:")
tet=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
key={tuple(np.round(v,9)) for v in tet}
imp=0
for pm in it.permutations(range(3)):
    for sg in it.product((1,-1),repeat=3):
        M=np.zeros((3,3))
        for i in range(3): M[i,pm[i]]=sg[i]
        if all(tuple(np.round(M@v,9)) in key for v in tet) and round(np.linalg.det(M))==-1:
            imp+=1
chk(f"A REGULAR TETRAHEDRON IS ACHIRAL -- it has {imp} improper symmetries of its own",
    imp>0,
    "so there IS no per-cell handedness to decorate with. The object being decorated "
    "has to be handed already, and a tetrahedron is not")

print("\nT5 -- SO THE TARGET IS SHARPER THAN 4038 LEFT IT")
print("  A chiral decoration must be built on a motif that is ITSELF handed. In the")
print("  600-cell the natural candidate is the RING OF FIVE TETRAHEDRA around an edge:")
print("  five is odd, a cyclic ring of five admits two traversal senses, and it is the")
print("  same five whose 352.644 deg leaves the 7.356-deg deficit (4019).")
chk("NOT tested here", True,
    "named as the next candidate with the reason it is the candidate. Fourth failed "
    "attempt at 4038's target, and the first with a diagnosis rather than a shrug")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. No chirality generated.")
raise SystemExit(1 if fails else 0)
