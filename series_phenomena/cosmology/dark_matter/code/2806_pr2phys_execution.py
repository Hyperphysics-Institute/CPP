#!/usr/bin/env python3
"""PR2-PHYS SUCCESSOR GATE EXECUTION (Patch 2806) under the frozen
2795 prereg. Estimator per SS1: per-chain kappa_phys = inverse-variance
joint of (fixed-physical-window real-space component, form selected at
rung level by dAIC>=10) and (k-side from 4 smallest shells; per-sample
PA-1 where present, MAIN-A/B spread (+) 1.5% floor model for archived
0.04). BLIND STAGE (first execution anywhere, per the SS0 attestation):
the (a_s,1/L) surface, GOF gate chi2/dof<=2.0, band [0.97,1.03] at
<=3% total. Consumes the 15-chain PR2 ladder exactly (SS0: 'existing
committed 15-chain archive'); X3 chains excluded (replication
instruments, not ladder members) -- disclosed.
DRAFTING-AMBIGUITY RESOLUTION (disclosed): SS1 says 'rung-pooled'
real profiles while the surface form kappa_phys(a_s,L) requires
L-resolved inputs; resolved in favor of the surface's explicit form:
form selection at rung level, kappa_phys evaluated PER CHAIN."""
import math, json, gzip
import numpy as np
from scipy.optimize import curve_fit

PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NBLK=24; NBOOT=2000
LADDER={ # label:(path,a_s)
 "RV-MAIN-A":("data/rv2714/rv_RV-MAIN-A.json.gz",0.04),
 "RV-MAIN-B":("data/rv2714/rv_RV-MAIN-B.json.gz",0.04),
 "RV-SIZE-S":("data/rv2714/rv_RV-SIZE-S.json.gz",0.04),
 "RV-SIZE-L":("data/rv2714/rv_RV-SIZE-L.json.gz",0.04),
 "RV-CORE":("data/rv2714/rv_RV-CORE.json.gz",0.02),
 "X4-02-686":("data/x3x4/X4-02-686.json.gz",0.02),
 "X4-02-1024":("data/x3x4/X4-02-1024.json.gz",0.02),
 "X4-01-432A":("data/x3x4/X4-01-432A.json.gz",0.01),
 "X4-01-432B":("data/x3x4/X4-01-432B.json.gz",0.01),
 "X4-01-686":("data/x3x4/X4-01-686.json.gz",0.01),
 "X4-01-1024":("data/x3x4/X4-01-1024.json.gz",0.01),
 "X4-005-432A":("data/x3x4/X4-005-432A.json.gz",0.005),
 "X4-005-432B":("data/x3x4/X4-005-432B.json.gz",0.005),
 "X4-005-686":("data/x3x4/X4-005-686.json.gz",0.005),
 "X4-005-1024":("data/x3x4/X4-005-1024.json.gz",0.005)}
LO,HI=0.08,0.546
F1=lambda r,Aa,k: Aa*np.exp(-k*r)/r
F2=lambda r,A1,k1,A2,k2: A1*np.exp(-k1*r)/r + A2*np.exp(-k2*r)/r

def load(lab): return json.load(gzip.open(LADDER[lab][0]))
def blocks_of(d):
    profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]
    rc=(np.arange(nb)+0.5)*rmax/nb
    bl=len(profs)//NBLK
    return rc,np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(NBLK)])

# rung-level form selection on the fixed window
forms={}
print("== rung-level form selection (fixed window 0.08-0.546, dAIC>=10) ==")
for a_s in (0.04,0.02,0.01,0.005):
    labs=[l for l in LADDER if LADDER[l][1]==a_s]
    allb=[]; rc=None
    for l in labs:
        rc_,b=blocks_of(load(l)); allb.append(b); rc=rc_
    allb=np.vstack(allb)
    mean=allb.mean(0); sem=allb.std(0,ddof=1)/math.sqrt(len(allb))
    m=(rc>LO)&(rc<HI)&(sem>0)
    x,y,e=rc[m],mean[m],np.maximum(sem[m],1e-7)
    pA,_=curve_fit(F1,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=30000)
    c2A=np.sum(((y-F1(x,*pA))/e)**2)
    best=None
    for kg in (3*KAPPA,6*KAPPA,12*KAPPA):
        try:
            pB,_=curve_fit(F2,x,y,p0=[pA[0],pA[1],y[0]*x[0],kg],sigma=e,maxfev=60000)
            c2=np.sum(((y-F2(x,*pB))/e)**2)
            if best is None or c2<best[0]: best=(c2,pB)
        except Exception: pass
    dAIC=(c2A+4)-(best[0]+8)
    forms[a_s]="two" if dAIC>=10 else "one"
    print(f"  a_s={a_s}: dAIC={dAIC:.1f} -> {forms[a_s]}-mode")

def kreal_chain(lab,seed):
    d=load(lab); rc,blocks=blocks_of(d); a_s=LADDER[lab][1]
    def ex(bs):
        mean=bs.mean(0); sem=bs.std(0,ddof=1)/math.sqrt(len(bs))
        m=(rc>LO)&(rc<HI)&(sem>0)
        x,y,e=rc[m],mean[m],np.maximum(sem[m],1e-7)
        if forms[a_s]=="one":
            p,_=curve_fit(F1,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=30000); return p[1]
        best=None
        for kg in (3*KAPPA,6*KAPPA,12*KAPPA):
            try:
                p,_=curve_fit(F2,x,y,p0=[0.05,KAPPA,y[0]*x[0],kg],sigma=e,maxfev=60000)
                c2=np.sum(((y-F2(x,*p))/e)**2)
                if best is None or c2<best[0]: best=(c2,min(p[1],p[3]))
            except Exception: pass
        return best[1]
    k0=ex(blocks); rng=np.random.default_rng(seed); ks=[]
    for _ in range(NBOOT):
        try: ks.append(ex(blocks[rng.integers(0,NBLK,NBLK)]))
        except Exception: pass
    return k0,float(np.std(ks,ddof=1))

def kside_chain(lab):
    d=load(lab); k2=np.array(d["k2"]); L=d["L"]
    n2=np.round(k2/(2*math.pi/L)**2).astype(int)
    shells=sorted(set(n2))[:4]
    if "szz_samples" in d:
        ss=np.array(d["szz_samples"]); k2v=[]; k2e=[]
        for v in shells:
            j=np.where(n2==v)[0]
            per=ss[:,j].mean(1); bl=len(per)//NBLK
            bm=np.array([per[q*bl:(q+1)*bl].mean() for q in range(NBLK)])
            S=bm.mean(); Se=bm.std(ddof=1)/math.sqrt(NBLK); kv=math.sqrt(k2[j][0])
            k2v.append(kv*kv*(1/S-1)); k2e.append(kv*kv*Se/S**2)
    else:
        szz=np.array(d["szz"]); k2v=[]; k2e=[]
        for v in shells:
            j=np.where(n2==v)[0]; S=szz[j].mean(); kv=math.sqrt(k2[j][0])
            k2v.append(kv*kv*(1/S-1)); k2e.append(abs(k2v[-1])*math.sqrt(0.015**2+0.02**2))
    w=1/np.array(k2e)**2
    kj2=float(np.sum(np.array(k2v)*w)/w.sum()); kj2e=math.sqrt(1/w.sum())
    kk=math.sqrt(max(kj2,1e-9))
    return kk,kj2e/(2*kk)

print("\n== per-chain kappa_phys (joint real (+) k-side; verdict inputs) ==")
pts=[]
for lab in LADDER:
    a_s=LADDER[lab][1]; L=load(lab)["L"]
    kr,kre=kreal_chain(lab,2806)
    kk,kke=kside_chain(lab)
    w=np.array([1/kre**2,1/kke**2])
    kj=(kr*w[0]+kk*w[1])/w.sum(); kje=math.sqrt(1/w.sum())
    pts.append((a_s,L,kj/KAPPA,kje/KAPPA))
    print(f"  {lab:12s}: real {kr/KAPPA:.4f}+/-{kre/KAPPA:.4f}  k {kk/KAPPA:.4f}+/-{kke/KAPPA:.4f}  -> kappa_phys/kappa_D = {kj/KAPPA:.4f}+/-{kje/KAPPA:.4f}")

print("\n== BLIND STAGE (first execution): (a_s,1/L) surface + GOF + verdict ==")
pts=np.array(pts); X,Li,Y,E=pts[:,0],1/pts[:,1],pts[:,2],pts[:,3]
res={}
for p in (1,2):
    Mx=np.vstack([np.ones_like(X),X**p,Li]).T
    W=np.diag(1/E**2)
    C=np.linalg.inv(Mx.T@W@Mx); b=C@Mx.T@W@Y
    chi2=float(np.sum(((Y-Mx@b)/E)**2))
    res[p]=(b,C,chi2)
    print(f"  p={p}: kappa_eff/kappa_D = {b[0]:.4f} +/- {math.sqrt(C[0,0]):.4f}  chi2/dof = {chi2/(len(Y)-3):.2f}")
pbest=min(res,key=lambda p:res[p][2])
b,C,chi2=res[pbest]; dof=len(Y)-3
keff=b[0]; kerr=math.sqrt(C[0,0]); msp=abs(res[1][0][0]-res[2][0][0])/2
tot=math.sqrt(kerr**2+msp**2)
gof=chi2/dof<=2.0
print(f"  AIC-selected p={pbest}; GOF chi2/dof={chi2/dof:.2f} ({'MET' if gof else 'NOT MET'} <=2.0)")
print(f"  kappa_eff/kappa_D = {keff:.4f}; total = {tot:.4f} (boot {kerr:.4f} (+) model {msp:.4f})")
print(f"  staggering census: zero (of record, leg 5)")
if not gof: v="UNRESOLVED (GOF gate)"
elif 0.97<=keff<=1.03 and tot<=0.03: v="PASS"
elif (keff<0.97-tot) or (keff>1.03+tot): v="FAIL"
else: v="UNRESOLVED"
print(f"  PR2-PHYS FROZEN VERDICT: {v}")
