#!/usr/bin/env python3
"""X3 FROZEN ANALYSIS (Patch 2789) under the 2786 prereg §1.
Committed observable per chain: F1 near-window slope kappa_fit/kappa_D
via the COMMITTED extraction (2761 analyze() Yukawa curve_fit on the
frozen window lo=2*a_s, hi=3.0/KAPPA=0.546 fm) wrapped in the FROZEN
covariance model: 24 equal contiguous sample blocks, 2000 block-
bootstrap resamples, extraction re-run per resample, quoted error =
bootstrap std. Applied identically to the two NEW chains and the four
RV chains entering the pooling rule.
Replication classes (frozen 2786 §1): REPLICATED / NOT-REPLICATED /
INCONCLUSIVE via inverse-variance pooling within a_s + Stouffer across."""
import math, json, gzip
import numpy as np
from scipy.optimize import curve_fit

PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NBLK=24; NBOOT=2000; RNGSEED=2789  # analysis rng, not a chain seed

def load(path):
    op=gzip.open if path.endswith('.gz') else open
    return json.load(op(path))

def f1_boot(d):
    profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]; a_s=d["a_s"]
    rcen=(np.arange(nb)+0.5)*rmax/nb
    lo,hi=2*a_s,3.0/KAPPA
    bl=len(profs)//NBLK
    blocks=np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(NBLK)])
    fmono=lambda r_,Aa,k_: Aa*np.exp(-k_*r_)/r_
    def extract(bset):
        mean=bset.mean(0); sem=bset.std(0,ddof=1)/math.sqrt(len(bset))
        m=(rcen>lo)&(rcen<hi)&(sem>0)
        x,y,e=rcen[m],mean[m],np.maximum(sem[m],1e-7)
        pm,_=curve_fit(fmono,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=20000)
        return pm[1]
    k0=extract(blocks)
    rng=np.random.default_rng(RNGSEED)
    ks=[]
    for _ in range(NBOOT):
        idx=rng.integers(0,NBLK,NBLK)
        try: ks.append(extract(blocks[idx]))
        except Exception: pass
    ks=np.array(ks)
    return k0/KAPPA, float(ks.std(ddof=1))/KAPPA, len(ks)

chains={  # label: (path, a_s group)
 "X3-R04":("/tmp/x3x4/rv_X3-R04.json",0.04),
 "X3-R02":("/tmp/x3x4/rv_X3-R02.json",0.02),
 "RV-MAIN-A":("data/rv2714/rv_RV-MAIN-A.json.gz",0.04),
 "RV-MAIN-B":("data/rv2714/rv_RV-MAIN-B.json.gz",0.04),
 "RV-CORE":("data/rv2714/rv_RV-CORE.json.gz",0.02)}

res={}
print("== F1 window slope kappa_fit/kappa_D (frozen extraction; 24x2000 block bootstrap) ==")
for lab,(p,g) in chains.items():
    r,err,nok=f1_boot(load(p))
    res[lab]=(r,err,g)
    dev=(r-1.0)/err
    print(f"  {lab:10s}: {r:.4f} +/- {err:.4f}  ({dev:+.2f} sigma vs DH)  [boot ok {nok}/2000]")

print("\n== Frozen replication evaluation ==")
new_below = all(res[l][0]<1.0 for l in ("X3-R04","X3-R02"))
print(f"  (a) both new chains kappa/kappa_D < 1: {new_below}")
cons={}
for new,ref in (("X3-R04",("RV-MAIN-A","RV-MAIN-B")),("X3-R02",("RV-CORE",))):
    rn,en,_=res[new]
    w=[1/res[l][1]**2 for l in ref]; rv=sum(res[l][0]*wi for l,wi in zip(ref,w))/sum(w)
    ev=(1/sum(w))**0.5
    z=abs(rn-rv)/math.sqrt(en**2+ev**2)
    cons[new]=z
    print(f"  (b) {new} vs RV counterpart: {rn:.4f} vs {rv:.4f} -> {z:.2f} sigma combined "
          f"({'consistent' if z<=2 else 'INCONSISTENT'})")
zs=[]
for g in (0.04,0.02):
    grp=[l for l in res if res[l][2]==g]
    w=[1/res[l][1]**2 for l in grp]
    rp=sum(res[l][0]*wi for l,wi in zip(grp,w))/sum(w); ep=(1/sum(w))**0.5
    z=(1.0-rp)/ep
    zs.append(z)
    print(f"  pooled a_s={g}: {rp:.4f} +/- {ep:.4f}  ({z:+.2f} sigma below DH)")
stouffer=sum(zs)/math.sqrt(len(zs))
print(f"  (c) Stouffer combined below-DH significance: {stouffer:.2f} sigma")

if new_below and all(z<=2 for z in cons.values()) and stouffer>=3:
    verdict="REPLICATED"
elif (not new_below) or stouffer<2:
    verdict="NOT-REPLICATED"
else:
    verdict="INCONCLUSIVE"
print(f"\nX3 FROZEN VERDICT: {verdict}")
print("(No PR1 enactment here in any branch; feeds the consolidated S4-X report.)")
