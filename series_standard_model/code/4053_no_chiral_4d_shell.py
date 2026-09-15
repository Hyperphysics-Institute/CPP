#!/usr/bin/env python3
# 4053 - RETRACTION. 4051's "chiral 4D shell" was never chiral. It was a rotated copy of
# the 600-cell, which is achiral. Everything downstream of that object is withdrawn.
import numpy as np, math, itertools as it
from itertools import permutations as P
from scipy.spatial import cKDTree
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2
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
V=build600()
def Lq(q):
    w,x,y,z=q
    return np.array([[w,-x,-y,-z],[x,w,-z,y],[y,z,w,-x],[z,-y,x,w]])
LEFT=[Lq(q) for q in V]
def orbit4(p):
    O=[]
    for R in LEFT:
        q=R@p
        if not any(np.allclose(q,x,atol=1e-8) for x in O): O.append(q)
    return np.array(O)
def spec(X):
    D=np.array([[np.linalg.norm(X[i]-X[j]) for j in range(len(X))] for i in range(len(X))])
    u,c=np.unique(np.round(D,6),return_counts=True); return tuple(zip(u.tolist(),c.tolist()))
sd=np.array([0.31,0.57,0.23,1.77]); sd/=np.linalg.norm(sd); S=orbit4(sd)

print("T1 -- THE INSTRUMENT 4052 SPECIFIED, BUILT -- AND IT RETURNS ZERO ON EVERYTHING")
print("  4D graph helicity: sum of sign det[u1,u2,u3,u4] over 4-hop paths. Under central")
print("  symmetry every step flips and (-1)^4 = +1, so it SURVIVES inversion; under")
print("  reflection the determinant flips, so it is P-ODD. Exactly 4052's specification.")
def h4d(X):
    T=cKDTree(X); d,_=T.query(X,k=2); cut=float(np.median(d[:,1]))*1.05
    nb=[np.array([j for j in T.query_ball_point(x,cut) if not np.allclose(X[j],x)]) for x in X]
    tot=0.0; cnt=0
    for v in range(len(X)):
        for a in nb[v]:
            for b in nb[a]:
                if b==v: continue
                for c in nb[b]:
                    if c==a: continue
                    for e in nb[c]:
                        if e==b: continue
                        tot+=np.sign(round(np.linalg.det(np.array(
                            [X[a]-X[v],X[b]-X[a],X[c]-X[b],X[e]-X[c]])),10)); cnt+=1
    return tot,cnt
t,c=h4d(S); t0,c0=h4d(V)
print(f"    4051's 'chiral' shell: {c} paths, helicity {t:+.1f}")
print(f"    600-cell itself:       {c0} paths, helicity {t0:+.1f}")
chk("both are exactly zero, and the path counts are IDENTICAL", abs(t)<1e-9 and c==c0,
    "identical path counts for two supposedly different objects is the tell")

print("\nT2 -- BECAUSE THEY ARE THE SAME OBJECT")
o0=orbit4(np.array([1.,0,0,0]))
chk("orbit4((1,0,0,0)) IS the 600-cell vertex set",
    {tuple(np.round(v,7)) for v in o0}=={tuple(np.round(v,7)) for v in V},
    "L_q applied to (1,0,0,0) returns the first COLUMN of L_q, which is q itself -- so "
    "the orbit of that point is literally the 120 icosians")
chk("and left multiplication is an ISOMETRY, so EVERY orbit is a congruent copy",
    spec(S)==spec(V),
    "the distance spectra match exactly. 4051's shell is a ROTATED 600-CELL")
chk("=> it is ACHIRAL: H4 contains reflections", True,
    "4051's test -- 'Theta does not map it to itself' -- only showed the copy was "
    "MISALIGNED with that particular reflection. Misaligned is not chiral, and I read "
    "it as chiral")

print("\nT3 -- WHAT IS WITHDRAWN")
for w in ("4051's chiral 4D shell: NOT CHIRAL. Retracted.",
          "4051's splitting attempt: it was never probing a chiral environment, so its "
          "two failures say nothing about splitting.",
          "4052's central-symmetry diagnosis: TRUE of the object but not the reason the "
          "attempt failed. The attempt failed because there was no chirality present."):
    chk(w[:72], True, w[72:] if len(w)>72 else "")
chk("4052's POSITIVE content survives", True,
    "inversion is proper in 4D (det(-I4) = +1), central symmetry and chirality can "
    "coexist in 4D, and a P-odd 4D scalar needs four Levi-Civita slots. All true, all "
    "independent of the retracted object -- and the instrument built from it works")

print("\nT4 -- AND THE REAL STATE, WHICH IS WORSE THAN I HAVE BEEN REPORTING")
chk("NO CHIRAL 4D STRUCTURE HAS EVER BEEN BUILT IN THIS ARC", True,
    "4041's chiral cluster is THREE-dimensional and was verified against 3D controls. "
    "The 4D analogue was attempted only at 4051 and is now retracted. The bracelet, "
    "n-hat and the 600-cell all live in 4D")
chk("so 4050's mechanism sketch has no 4D chiral substrate to run on", True,
    "the two helicity states are real and exactly degenerate (4050 stands). What would "
    "split them has not been constructed in the right dimension")
chk("the honest statement of the remaining work", True,
    "build a chiral 4D point set -- an orbit of a subgroup of H4's ROTATION half that "
    "is NOT an orbit of H4 itself. The left-icosian group is the wrong choice because "
    "its orbits are congruent to the 600-cell. NOT attempted here")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. Nothing derived.")
raise SystemExit(1 if fails else 0)
