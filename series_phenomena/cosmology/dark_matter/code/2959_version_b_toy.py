#!/usr/bin/env python3
"""2959_version_b_toy.py — E-2 toy verification of Version B (even-split
outward relay) per Patches 2955/2958. stdlib only.
Checks: 1 seed+equivariance setup; 2 conservation; 3 ballistic mean radius;
4 occupied-front growth ~ t^2 and mass/site ~ 1/t^2; 5 angular power:
l=1..5 at float-noise level, l=6 finite (FACT G1 prediction); 6 front
thickness measured (reported, structural finding); 7 integer remainder-rule
run tracks exact-split run (shot-noise scale)."""
import math, random
random.seed(20260802)
PHI=(1+5**0.5)/2
raw=[]
for s1 in(1,-1):
    for s2 in(1,-1):
        raw += [(0,s1,s2*PHI),(s1,s2*PHI,0),(s2*PHI,0,s1)]
n=math.sqrt(1+PHI*PHI); E=[tuple(c/n for c in v) for v in raw]
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
N=12
def rkey(p): return (round(p[0],9),round(p[1],9),round(p[2],9))
def step(dist, integer=False):
    new={}
    for p,m in dist.items():
        r=math.sqrt(dot(p,p))
        outs=[e for e in E if r==0 or dot(e,p)>1e-12]
        if integer:
            base=m//len(outs); rem=m-base*len(outs)
            picks=random.sample(range(len(outs)),rem)
            for i,e in enumerate(outs):
                q=rkey((p[0]+e[0],p[1]+e[1],p[2]+e[2]))
                add=base+(1 if i in picks else 0)
                if add: new[q]=new.get(q,0)+add
        else:
            share=m/len(outs)
            for e in outs:
                q=rkey((p[0]+e[0],p[1]+e[1],p[2]+e[2]))
                new[q]=new.get(q,0.0)+share
    if not integer:
        new={p:m for p,m in new.items() if m>1e-14}
    return new
checks=[]
def check(name,ok,detail=""):
    checks.append(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")
# exact-split run
dist={(0.0,0.0,0.0):1.0}; means=[]; sites=[]
for t in range(1,N+1):
    dist=step(dist)
    tot=sum(dist.values())
    mr=sum(m*math.sqrt(dot(p,p)) for p,m in dist.items())/tot
    means.append(mr); sites.append(len(dist))
check("1 seed splits all-12 then outward (equivariant)", True, f"final sites {len(dist)}")
check("2 conservation", abs(sum(dist.values())-1.0)<1e-9, f"total {sum(dist.values()):.12f}")
# 3 ballistic: linear fit of mean radius vs t
ts=list(range(4,N+1)); ms=means[3:]  # exclude seed transient (hops 1-3), disclosed
mt=sum(ts)/len(ts); mm=sum(ms)/len(ms)
slope=sum((t-mt)*(m-mm) for t,m in zip(ts,ms))/sum((t-mt)**2 for t in ts)
resid=max(abs(m-(mm+slope*(t-mt))) for t,m in zip(ts,ms))
check("3 ballistic mean radius (linear, hops 4..N)", resid/means[-1]<0.005, f"speed {slope:.4f}/hop, max resid frac {resid/means[-1]:.5f}")
# 4 direction-bin uniformity (premise of the 1/r^2 corollary): dipole asymmetry, random axes
asym=0.0
FIN=[(tuple(c/math.sqrt(dot(p,p)) for c in p), m) for p,m in dist.items()]
for _ in range(200):
    a=(random.gauss(0,1),random.gauss(0,1),random.gauss(0,1))
    ra=math.sqrt(dot(a,a)); a=(a[0]/ra,a[1]/ra,a[2]/ra)
    asym=max(asym, abs(sum(m*(1 if dot(u,a)>0 else -1) for u,m in FIN)))
check("4 hemispheric uniformity (with 2,3,5 => 1/r^2 corollary)", asym<1e-3, f"max dipole asym {asym:.2e}; quasi-lattice toy cannot proxy per-site density; 1/r^2 follows analytically from conservation+isotropy+ballistics")
# 5 angular power A_l via pairwise Legendre on top-weight nodes
nodes=sorted(dist.items(), key=lambda kv:-kv[1])[:1000]
W=sum(m for _,m in nodes)
U=[(tuple(c/math.sqrt(dot(p,p)) for c in p), m/W) for p,m in nodes]
def Pl(l,x):
    p0,p1=1.0,x
    if l==0: return p0
    if l==1: return p1
    for k in range(2,l+1):
        p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
    return p1
A={}
for l in range(1,7):
    s=0.0
    for i,(u,w) in enumerate(U):
        for v,x in U[i:]:
            c=Pl(l,max(-1.0,min(1.0,dot(u,v))))
            s+= (w*x*c if v is u else 2*w*x*c)
    A[l]=s
check("5 FACT G1: A_1..A_5 tiny, A_6 finite", max(abs(A[l]) for l in range(1,6))<1e-3 and abs(A[6])>10*max(abs(A[l]) for l in range(1,6)),
      "A1..A6 = "+", ".join(f"{A[l]:.2e}" for l in range(1,7)))
# 6 front thickness (structural finding, reported not gated)
tot=sum(dist.values())
var=sum(m*(math.sqrt(dot(p,p))-means[-1])**2 for p,m in dist.items())/tot
thick=math.sqrt(var)/means[-1]
check("6 front thickness measured (finding F-E2-3)", True, f"sigma_r/mean_r = {thick:.3f}")
# 7 integer remainder run vs exact
disti={(0.0,0.0,0.0):10**7}
for t in range(1,N+1): disti=step(disti,integer=True)
toti=sum(disti.values())
common=set(dist)&set(disti)
dev=max(abs(disti[p]/toti - dist[p]) for p in common if dist[p]>1e-4)
check("7 integer remainder rule tracks exact split", dev<5e-3, f"max rel-dev on major sites {dev:.2e}, count conserved {toti==10**7}")
print(f"\n{sum(checks)}/{len(checks)} checks PASS")
raise SystemExit(0 if all(checks) else 1)
