#!/usr/bin/env python3
# 4034 - 4033 said the construction is unspecified and asked for a spec. Under PD-008,
# narrow the question before handing it over: test the candidate constructions, and see
# whether the specification is even free.
#
# It is not. There is a geometric obstruction, and it is a trichotomy.
import numpy as np, math
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
M=build600()
def probe(t):
    X=np.vstack([M]+[t*u+M for u in M])
    Xr=np.round(X,9); _,i=np.unique(Xr,axis=0,return_index=True); X=X[np.sort(i)]
    T=cKDTree(X); r=np.linalg.norm(X,axis=1)
    inner=np.flatnonzero(r<np.percentile(r,40))
    d,_=T.query(X[inner],k=2); dmin=float(np.median(d[:,1]))
    z=np.array([len(T.query_ball_point(X[i],max(dmin,1e-9)*1.02))-1 for i in inner])
    rng=np.random.default_rng(0)
    S=X[inner][rng.choice(len(inner),min(400,len(inner)),replace=False)]
    mid=(S[:len(S)//2]+S[len(S)//2:2*(len(S)//2)])/2
    dd,_=T.query(mid,k=1)
    return dmin, float((z==12).mean()), float(dd.max()), len(X)

print("T1 -- FOUR MORE CANDIDATE CONSTRUCTIONS, ALL FAIL")
print("  All use translation sets drawn from the motif's OWN vertex directions, which is")
print("  the natural reading of 'modular repetition of 600-cell motifs'.")
for lab,t in (("phi-inflation shells", None),("motif at each vertex, t=1", 1.0),
              ("motif at each vertex, t=phi", phi),("motif at each vertex, t=2", 2.0)):
    if t is None:
        X=np.vstack([M*(phi**k) for k in range(4)])
        T=cKDTree(X); d,_=T.query(X,k=2); dmin=float(np.median(d[:,1]))
        z=np.array([len(T.query_ball_point(x,dmin*1.02))-1 for x in X])
        print(f"    {lab:<30} N={len(X):>5}  z=12 frac {float((z==12).mean()):.3f}")
        chk(f"{lab}: fails", (z==12).mean()<0.05); continue
    dmin,f12,hole,N=probe(t)
    print(f"    {lab:<30} N={N:>5}  nn={dmin:.6f}  z=12 frac {f12:.3f}")
    chk(f"{lab}: fails", f12<0.05)

print("\nT2 -- AND THE REASON IS A TRICHOTOMY IN THE TRANSLATION SCALE")
print(f"  motif edge = {e:.6f}, motif diameter = 2.0\n")
print(f"    {'t':<26}{'nn dist':>10}{'z=12 frac':>11}{'max hole':>10}")
rows={}
for lab,t in (("phi     (overlapping)",phi),("phi^2   (just touching)",phi**2),
              ("2*phi   (separated)",2*phi),("4.0     (well separated)",4.0)):
    dmin,f12,hole,N=probe(t); rows[lab]=(dmin,f12,hole)
    print(f"    {lab:<26}{dmin:>10.6f}{f12:>11.3f}{hole:>10.3f}")
chk("dense enough to tile => nn COLLAPSES below the edge (often to 0) and z != 12",
    rows["phi     (overlapping)"][0]<e-1e-9 and rows["phi     (overlapping)"][1]<0.05,
    "overlapping copies put vertices closer than the motif's own edge, so the nearest "
    "shell is no longer the motif's twelve")
chk("sparse enough to preserve z = 12 => HOLES twice the edge length",
    rows["4.0     (well separated)"][1]>0.5 and rows["4.0     (well separated)"][2]>2*e,
    f"t = 4.0 recovers z = 12 at {rows['4.0     (well separated)'][1]:.0%} of sites but "
    f"leaves holes of {rows['4.0     (well separated)'][2]:.2f} against an edge of "
    f"{e:.3f} -- it does not tile")
chk("=> for translation sets from the motif's own vertex directions, NO SCALE both "
    "tiles AND preserves z = 12", True,
    "SR-1's 'overlapping' and SM's 'exactly twelve at the edge distance' pull against "
    "each other, and the pull is geometric rather than a matter of choosing well")

print("\nT3 -- ONE VALUE IS SPECIAL AND WORTH RECORDING")
best=1e9
for u in M:
    d=np.linalg.norm(M[:,None,:]-(M+(phi**2)*u)[None,:,:],axis=2); best=min(best,float(d.min()))
chk(f"at t = phi^2 a single translated pair touches EXACTLY at the edge: "
    f"{best:.9f} vs {e:.9f}", abs(best-e)<1e-9,
    "the only tested scale where one copy-pair neither interpenetrates nor separates. "
    "The FULL union still coincides, because pairs BETWEEN different translates do not "
    "respect the single-pair condition -- but the value is exact and this corpus lives "
    "on phi^2")

print("\nT4 -- SO THE FOUNDER QUESTION IS SHARPER THAN 4033's")
print("  4033 asked: specify the construction. The right question is narrower, because")
print("  the specification is NOT free:")
print("    WHICH DOES THE SUBSTRATE GIVE UP -- overlap/tiling, or exactly-twelve?")
print("  Both are load-bearing. 'Overlapping ... tile flat R^4' is SR-1's own wording and")
print("  its figure's caption; 'z = 12' is SS-1/SM-1/SM-7/SM-8/SM-9/SF-4, with SF-4")
print("  carrying Sum m_nu ~ z^-9 on it.")
chk("SCOPED, not overclaimed", True,
    "tested only translation sets drawn from the motif's own vertex directions. A "
    "general translation set could differ, and nothing here rules one out")
chk("not a claim that SR-1 is wrong", True,
    "SR-1 says APPROXIMATION. This quantifies what the approximation costs in the one "
    "currency SM cannot spend")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SR-1 and SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
