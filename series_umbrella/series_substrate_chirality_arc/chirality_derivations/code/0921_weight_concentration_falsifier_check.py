import numpy as np, itertools
phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
def build_600cell():
    V=set()
    for i in range(4):
        for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
    for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
    for sg in itertools.product([1,-1],repeat=3):
        for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
    V=np.array(sorted(V)); N=len(V)
    D=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=D[D>1e-6].min(); A=np.abs(D-ed)<1e-6
    nbr=[list(map(int,np.where(A[v])[0])) for v in range(N)]
    return V,N,nbr

# 0921 — verification of ChatGPT's weight-concentration falsifier against the equal-weight R(m) bound.
# Reproduces: equal-weight R(m)<1 is defeated by concentration; super-criticality persists to
# participation p ~ 2.2 (m=4) .. 3.8 (m=12) in the one-big-weight family; the loose all-neighbours-
# concentrate worst case stays ~1.7 even at p=4-5 (so a bare MEAN m_eff>=4 floor does not rescue rho<1).
import numpy as np
from scipy.optimize import minimize
arc=lambda z:(2/np.pi)*np.arcsin(np.clip(z,0,1))

def rowsum_and_p(w):
    w=np.abs(w); w=w/np.linalg.norm(w); wmax=w.max()
    S=arc(w*wmax).sum(); p=1.0/np.sum(w**4); return S,p

print("FACT: one-big-weight family (W,e,...,e): super-criticality (rowsum>=1) persists above p=1")
for m in [4,6,12]:
    print(f" m={m}:")
    for W in [0.99,0.9,0.8,0.75,1/np.sqrt(m)]:
        if W<1/np.sqrt(m): continue
        rest=np.sqrt(max(0,(1-W**2)/(m-1))); w=np.array([W]+[rest]*(m-1))
        S,p=rowsum_and_p(w)
        print(f"   W={W:5.3f}  p={p:5.2f}  rowsum={S:6.4f}  {'SUPER-CRIT' if S>=1 else 'sub-crit'}")

print("\nLOOSE worst-case (maximise rowsum at fixed participation, a_i<=w_max), m=20:")
m=20
def part(w): w=np.abs(w); w=w/np.linalg.norm(w); return 1.0/np.sum(w**4)
def negS(w):
    w=np.abs(w); w=w/np.linalg.norm(w); return -arc(w*w.max()).sum()
for ptar in [2,3,4,5]:
    best=0
    for _ in range(40):
        x0=np.abs(np.random.default_rng().normal(size=m))+0.01
        r=minimize(negS,x0,constraints=[{'type':'eq','fun':lambda w,pt=ptar:part(w)-pt}],
                   method='SLSQP',options={'maxiter':300,'ftol':1e-9})
        if r.success: best=max(best,-r.fun)
    print(f"   p={ptar}: max rowsum ~ {best:.3f}  {'(margin gone)' if best>=1 else ''}")
print("\n=> equal-weight R(m) assumed equal weights; concentration defeats it; a MEAN floor is insufficient.")
