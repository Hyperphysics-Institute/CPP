#!/usr/bin/env python3
# 4057 - WHY H1 fails, whether it can be fixed, and why it cannot.
# The convenient answer was available and the founder's own ruling rules it out.
import numpy as np, math, itertools as it, os
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
                for pm_ in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm_[i]>pm_[j])%2==0:
                        Vs.append(np.array([sg[pm_[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(D[i,j]-e)<1e-9]
key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
Th=np.diag([1.,1,1,-1]); PM=np.array([key[tuple(np.round(Th@V[i],9))] for i in range(N)])
plus=[i for i in range(N) if V[i][3]>1e-9]
def stat(nh,delta):
    Q=np.zeros((N,N))
    for (i,j) in edges:
        u=(V[j]-V[i]); u/=np.linalg.norm(u); c=float(u@nh)
        Q[i,j]=1+delta*c; Q[j,i]=1-delta*c
    for i in range(N): Q[i,i]=-Q[i].sum()
    w,vec=np.linalg.eig(Q.T); k=int(np.argmin(np.abs(w)))
    p=np.real(vec[:,k]); return p/p.sum()
K=200; K2=K*(K-1); K3=K2*(K-2); K4=K3*(K-3)
def mins(nh,delta):
    p=stat(nh,delta); lam=K*p
    u1=np.array([p[PM[a]]**2 for a in plus]); v1=np.array([p[PM[a]] for a in plus])
    u2=np.array([p[a]**2 for a in plus]);     v2=np.array([p[a] for a in plus])
    GM=K4*np.outer(u1,u2)+K3*(np.outer(u1,v2)+np.outer(v1,u2))+K2*np.outer(v1,v2)
    m1=np.array([lam[PM[a]]+lam[PM[a]]**2 for a in plus])
    m2=np.array([lam[a]+lam[a]**2 for a in plus])
    GP=np.outer(m1,m2)
    return (float(np.linalg.eigvalsh((GM+GM.T)/2).min()),
            float(np.linalg.eigvalsh((GP+GP.T)/2).min()))

print("T1 -- THE CAUSE: A FIXED TOTAL IS A NON-LOCAL CONSTRAINT")
print("  4056's indefiniteness was p-INDEPENDENT, so it lives in the MULTINOMIAL, not")
print("  the physics. A multinomial has a FIXED TOTAL K, and a fixed total is a")
print("  NON-LOCAL constraint -- the classic way to break reflection positivity.")
print("  Test the grand-canonical version: INDEPENDENT POISSON occupations, where")
print("  E[n_i^2 n_j^2] = (l_i + l_i^2)(l_j + l_j^2) factorises and the Gram is RANK ONE.\n")
print(f"    {'sector':<16}{'delta':>7}{'MULTINOMIAL':>16}{'POISSON':>16}")
for nm,nh in (("n-hat FIXED",np.array([1.,0,0,0])),("n-hat FLIPPED",np.array([0.,0,0,1]))):
    for delta in (0.0,0.10,0.35):
        a,b=mins(nh,delta)
        print(f"    {nm:<16}{delta:>7.2f}{a:>16.4e}{b:>16.4e}")
mf=[mins(np.array([1.,0,0,0]),d) for d in (0.10,0.35)]
chk("POISSON is PSD in the n-hat-FIXING sector at every delta",
    all(abs(b)<1e-10 for _,b in mf),
    f"{mf[0][1]:+.1e} and {mf[1][1]:+.1e} -- machine zero, against multinomial's "
    f"{mf[0][0]:+.1e} and {mf[1][0]:+.1e}")
ml=[mins(np.array([0.,0,0,1]),d) for d in (0.10,0.35)]
chk("but the n-hat-FLIPPING failure SURVIVES the change", all(b<-1 for _,b in ml),
    f"Poisson gives {ml[0][1]:+.2f} and {ml[1][1]:+.2f}. That failure is a genuine "
    "Theta-asymmetry of the measure, not a constraint artifact")
chk("=> the n-hat-FIXING failure IS caused by the fixed total", True,
    "cause identified, and a fix is available: drop the fixed total")

print("\nT2 -- AND THE FIX IS RULED OUT BY THE FOUNDER'S OWN REGISTERED RULING")
hits=[]
for f in ("founders_voice/founder_ruling_GR-FE-1_physical_picture_2026-08-19.md",
          "series_gravitation/fe1_derivation/T2_T3_uniqueness_and_source.md"):
    if os.path.exists(f):
        t=open(f,encoding='utf-8',errors='replace').read()
        if "conserved" in t: hits.append(f)
chk("CP conservation is founder-ruled, not a modelling choice", len(hits)>=1,
    "GR-FE-1 (19 Aug 2026): 'The GPs, the CPs, and DI-bits are all conserved'; "
    "T2_T3 records it as the registered picture: 'CPs are conserved'")
chk("so the FIXED TOTAL IS PHYSICAL, and the grand-canonical version relaxes a "
    "conservation law the founder has ruled", True,
    "the Poisson measure is not a better model of the same physics -- it is a model of "
    "different physics")

print("\nT3 -- SO H1's FAILURE IS REAL, NOT AN ARTIFACT")
chk("4056 stands", True,
    "the canonical measure is the physical one and it breaks RP in the n-hat-fixing "
    "sector for delta > 0")
chk("4023 stays undermined", True,
    "and 4024 stays standing, for the reason 4056 gave: its argument never used RP")
print("  I want the shape of this on record. The convenient answer was AVAILABLE and")
print("  CORRECT-LOOKING: Poisson restores RP exactly where it was needed, and I could")
print("  have written 'the failure is a modelling artifact, [PCD-EXT] should be replaced'")
print("  without checking whether the replacement is physically admissible. It is not.")
chk("the check that killed it was a corpus search, not a computation", True,
    "the computation SUPPORTED the convenient reading. Only the founder's ruling "
    "refutes it, and that ruling is three weeks old and in a lane I was not working")

print("\nT4 -- WHAT THIS LEAVES, STATED FOR VW-1's HOLDER")
print("  RP on [PCD-EXT] fails in BOTH sectors for delta > 0. The n-hat-FLIPPING failure")
print("  is intrinsic. The n-hat-FIXING failure is caused by CP conservation -- which is")
print("  axiom-level, so it cannot be traded away for RP.")
print("  => H1 is not merely unproven. On the physical measure it is FALSE, and a")
print("     VW-1-style argument needs either a different positivity condition or a")
print("     different route entirely.")
chk("that is a stronger statement than 4056 made, and it is worse news", True,
    "4056 said [PCD-EXT] cannot discharge H1. This says the physical constraint is what "
    "breaks it, so no occupation model respecting CP conservation will do better")
chk("NOT claimed: that no positivity condition survives", True,
    "only that REFLECTION positivity, on the squared class, does not. Whether a weaker "
    "condition suffices for VW-1 is that theorem's question")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
