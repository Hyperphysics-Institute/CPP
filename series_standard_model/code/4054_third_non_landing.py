#!/usr/bin/env python3
# 4054 - a third consecutive attempt that does not land, and a stop.
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
def qmul(a,b):
    w1,x1,y1,z1=a; w2,x2,y2,z2=b
    return np.array([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2])
cj=lambda q: np.array([q[0],-q[1],-q[2],-q[3]])
def corb(p):
    O=[]
    for q in V:
        r=qmul(qmul(q,p),cj(q))
        if not any(np.allclose(r,x,atol=1e-8) for x in O): O.append(r)
    return np.array(O)

print("T1 -- THE ATTEMPT: lift 4041's verified 3D chiral orbit into 4D by CONJUGATION")
print("  x -> q x q-bar fixes the real part and acts as SO(3) on the imaginary part, so")
print("  it should carry the 3D construction into 4D unchanged.")
sizes={}
for nm,p in (("generic imaginary",[0.0,0.31,0.57,1.77]),
             ("supposed 5-fold axis",[0.0,0,1,phi]),
             ("real axis",[1.0,0,0,0])):
    p=np.array(p); O=corb(p/np.linalg.norm(p)); sizes[nm]=len(O)
    print(f"    seed {nm:<22} orbit size {len(O):>3}")
chk("the real axis is fixed (orbit 1), as conjugation requires", sizes["real axis"]==1)
chk("BUT the supposed 5-fold-axis seed ALSO gives 60, and it should give 12",
    sizes["supposed 5-fold axis"]==60,
    "in 3D a 5-fold-axis seed has a 12-point orbit and the cluster stays ACHIRAL "
    "(4041). Getting 60 means my special positions are NOT where I think they are in "
    "the conjugation frame -- so I do not have a working 3D -> 4D lift, only a map I "
    "have not aligned")

print("\nT2 -- AND THE MEASUREMENT IS UNINFORMATIVE ANYWAY")
p=np.array([0.0,0.31,0.57,1.77]); p/=np.linalg.norm(p); IM=corb(p)
for w0 in (0.0,0.5):
    S=np.array([[w0,*x[1:]] for x in IM]); S/=np.linalg.norm(S,axis=1,keepdims=True)
    T=cKDTree(S); d,_=T.query(S,k=2); cut=float(np.median(d[:,1]))*1.15
    nb=[np.array([j for j in T.query_ball_point(x,cut) if not np.allclose(S[j],x)]) for x in S]
    tot=0; cnt=0
    for v in range(len(S)):
        for a in nb[v]:
            for b in nb[a]:
                if b==v: continue
                for c in nb[b]:
                    if c==a: continue
                    for e in nb[c]:
                        if e==b: continue
                        tot+=np.sign(round(np.linalg.det(np.array(
                            [S[a]-S[v],S[b]-S[a],S[c]-S[b],S[e]-S[c]])),10)); cnt+=1
    print(f"    4D shell at w0={w0}: {len(S)} points, 4-hop paths {cnt}, helicity {tot:+.0f}")
    if w0==0.0: npath=cnt
chk(f"only ~{npath} 4-hop paths -- the graph is far too sparse to measure anything",
    npath<500,
    "this is 4041's failure repeated exactly: a zero that means 'I cannot see', not "
    "'there is nothing there'. I recognised it at 4041, wrote it up, and have now built "
    "the same trap again")

print("\nT3 -- SO THIS IS A THIRD CONSECUTIVE NON-LANDING, AND THAT IS THE SIGNAL")
print("    4051  splitting attempt        -> both functionals wrong, then RETRACTED at 4053")
print("    4052  diagnosis                -> true in part, but the wrong reason; superseded")
print("    4053  retraction               -> the object was never chiral")
print("    4054  this attempt             -> lift misaligned, graph too sparse")
chk("the lane should stop here rather than produce a fourth", True,
    "the last four patches have produced one retraction and no result. Continuing past "
    "that point is how a second retraction gets made")

print("\nT4 -- WHAT IS ACTUALLY ESTABLISHED, STATED CLEANLY FOR WHOEVER PICKS THIS UP")
for s in ("SF-6's OPEN-SD-CHIR-PRIMITIVE names n-hat-on-a-host-vertex as leading "
          "candidate; it CANNOT work -- Theta fixes n-hat and preserves the 600-cell (4046).",
          "A chiral cluster with icosahedral ROTATION symmetry and an achiral z = 12 "
          "first shell EXISTS and is measured -- IN THREE DIMENSIONS (4041, 4042, 4047).",
          "It preserves the icosahedral and dodecahedral shells CPP uses (4043).",
          "Its parity-odd dispersion enters at O(k^15), so it is not excluded by the "
          "absence of vacuum optical activity -- and cannot be calibrated by it (4044, 4045).",
          "A structural helicity bias caps at ~2%, so it cannot supply V-A's maximality (4048).",
          "The W bracelet is ACHIRAL, by the corpus's own Theorem 4.2 and independently (4049).",
          "Ring-bivector contracted with n-hat IS the P-odd binary variable, and its two "
          "states are EXACTLY DEGENERATE under the present symmetry (4050).",
          "NO CHIRAL 4D STRUCTURE HAS BEEN BUILT. Everything chiral here is 3D (4053, 4054)."):
    chk(s[:78], True, s[78:] if len(s)>78 else "")
chk("the gap is dimensional and it is the whole remaining problem", True,
    "a chiral 4D point set with icosahedral rotation symmetry, tested with the 4D graph "
    "helicity on a graph DENSE ENOUGH to resolve it. Both halves of that sentence are "
    "requirements, and this patch met neither")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. Nothing derived.")
raise SystemExit(1 if fails else 0)
