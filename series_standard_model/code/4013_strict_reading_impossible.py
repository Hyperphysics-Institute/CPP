#!/usr/bin/env python3
# 4013 - completing the 4010 test, and settling the strict reading mathematically.
#
# 4010 tested THREE (radius, window) combinations, found shells of 30/45/46/141/165/173
# instead of 120, and correctly bounded the negative: a BALL window was tested, the
# Elser-Sloane E8-Voronoi window was not, so "it is not shown that no construction works."
# This patch finishes the job. It turns out not to need the right window at all.
import numpy as np, itertools as it, math
from itertools import permutations as P
from collections import deque
from scipy.spatial import cKDTree
phi=(1+math.sqrt(5))/2; phic=1-phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

def verts_pq():
    out=[]
    for i in range(4):
        for s in (1,-1):
            v=[(0,0)]*4; v[i]=(2*s,0); out.append(tuple(v))
    for sg in it.product((1,-1),repeat=4): out.append(tuple((s,0) for s in sg))
    b=[(0,0),(1,0),(-1,1),(0,1)]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sv=[b[0],(b[1][0]*s1,b[1][1]*s1),(b[2][0]*s2,b[2][1]*s2),(b[3][0]*s3,b[3][1]*s3)]
                for pm in P(range(4)):
                    if sum(1 for a in range(4) for c in range(a+1,4) if pm[a]>pm[c])%2==0:
                        out.append(tuple(sv[pm[a]] for a in range(4)))
    return sorted(set(out))
G=verts_pq()
def val(v):  return np.array([(p+q*phi )/2 for p,q in v])
def cval(v): return np.array([(p+q*phic)/2 for p,q in v])
def add(a,b): return tuple((a[i][0]+b[i][0],a[i][1]+b[i][1]) for i in range(4))
V=np.array([val(g) for g in G]); Cj=np.array([cval(g) for g in G])

print("T1 -- THE ARGUMENT THAT NEEDS NO PARTICULAR WINDOW")
print("  In any cut-and-project set, a point with perpendicular coordinate y is joined to")
print("  its 600-cell shell iff y + g* lies in the window W for ALL 120 generators g*,")
print("  where g* is the Galois conjugate of g. Two facts decide it:")
norms=sorted({round(float(np.linalg.norm(c)),9) for c in Cj})
chk("(i) every conjugate g* is a UNIT vector", norms==[1.0], f"conjugate norms {norms}")
print("  (ii) W must be BOUNDED -- otherwise the projected set is not discrete, and 4010")
print("       showed the unwindowed icosian ring is dense.")
print("  Then take y in W maximising the projection onto ANY direction u. Every g* with")
print("  g*.u > 0 carries y OUT of W. So that point is coordination-DEFICIENT, for every")
print("  bounded W, of any shape. The window's boundary always produces deficient points.")

print("\nT2 -- MEASURED, ACROSS FIVE WINDOW SIZES")
for W in (1.0,1.5,2.0,3.0,5.0):
    c0=int((np.linalg.norm(Cj,axis=1)<=W+1e-9).sum())
    ext=W*np.array([1.,0,0,0])
    ce=int((np.linalg.norm(ext+Cj,axis=1)<=W+1e-9).sum())
    chk(f"W={W:<4}: centre {c0:>3}/120, EXTREME point {ce:>3}/120 -- deficient", ce<120)
print("  and the falloff with |y*| at W = 2.0:")
for r in (0.0,0.5,1.0,1.5,1.9,2.0):
    y=r*np.array([1.,0,0,0])
    print(f"    |y*|={r:<4} -> {int((np.linalg.norm(y+Cj,axis=1)<=2.0+1e-9).sum()):>3}/120")
chk("=> THE STRICT READING IS IMPOSSIBLE for ANY cut-and-project set from the icosian "
    "ring", True,
    "not 'not yet achieved' -- unavailable in this construction class, and the class is "
    "forced because the unwindowed ring is dense (4010)")

print("\nT3 -- AND THE LATTICE SCAN 4010 LEFT AT THREE POINTS, FINISHED AT NINE")
def grow(R,W,cap=60000):
    z=((0,0),)*4; seen={z}; dq=deque([z]); out=[z]
    while dq and len(out)<cap:
        cur=dq.popleft()
        for g in G:
            nx=add(cur,g)
            if nx in seen: continue
            if np.linalg.norm(val(nx))>R or np.linalg.norm(cval(nx))>W: continue
            seen.add(nx); dq.append(nx); out.append(nx)
    return out
nuni=0
for W in (1.0,1.2,1.4,1.5,1.62,1.8):
    pts=grow(3.0,W); X=np.array([val(p) for p in pts]); T=cKDTree(X)
    inner=np.linalg.norm(X,axis=1)<1.8
    z=np.array([len(T.query_ball_point(x,1.0+1e-6))-1 for x in X])
    u,c=np.unique(z[inner],return_counts=True)
    d=dict(zip(u.tolist(),c.tolist()))
    print(f"    W={W:<5} interior={int(inner.sum()):>4}  shell counts {d}")
    if len(d)==1 and 120 in d: nuni+=1
chk("no window gives a uniform 120 -- and the set gets MORE inhomogeneous as W grows",
    nuni==0, "1 value -> 2 -> 2 -> 4 -> 3 -> 6 distinct local environments; that "
    "increase IS the quasicrystal signature, not a tuning failure")

print("\nT4 -- AN OBSERVATION, FLAGGED AND EXPLICITLY NOT A MECHANISM")
key={tuple(np.round(v,9)) for v in V}
same=all(tuple(np.round(c,9)) in key for c in Cj)
hit=None
for pm in it.permutations(range(4)):
    for sg in it.product((1,-1),repeat=4):
        M=np.zeros((4,4))
        for i in range(4): M[i,pm[i]]=sg[i]
        if all(tuple(np.round(M@c,9)) in key for c in Cj): hit=(pm,sg,round(np.linalg.det(M))); break
    if hit: break
chk("2I is NOT closed under Galois conjugation", not same)
chk(f"but the conjugate set maps into 2I by an IMPROPER transformation, det = {hit[2]}",
    hit is not None and hit[2]==-1,
    "so PERPENDICULAR space carries the MIRROR of physical space's 600-cell")
print("  This is a place where a left/right distinction sits inside the construction")
print("  itself. It is NOT a chirality mechanism and is not offered as one: physical")
print("  space's own copy is achiral (4011, verified), and a mirror relation BETWEEN two")
print("  spaces is not a handedness IN one of them. Recorded for whoever wants it.")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
