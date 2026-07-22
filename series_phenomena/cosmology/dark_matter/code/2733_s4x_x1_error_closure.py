#!/usr/bin/env python3
"""S4-X X1 (Patch 2733) under the frozen s4x_charter.md, stage X1 -> PR1.

PREREGISTRATION (frozen HERE, before any result is computed):
DATA: the five committed S4-E chains (per-sample signed charge
profiles, every 5 sweeps; data archived at data/s4e_chains/).
OBSERVABLE for autocorrelation: the projection u_t = sum_b w_b
rho_b(t) with w = the chain's own mean profile restricted to the fit
window (2 a_s, 3/kappa_D) -- the scalar that carries the kappa
information.
IACT ESTIMATOR: standard windowed sum tau_int = 1/2 + sum_{t<=W}
rho(t), Sokal window W = smallest t with t >= 5*tau_int(t).
ESS = N_samples / (2 tau_int).
CORRECTED ERRORS: per-bin sigma_corr = naive per-sample SEM *
sqrt(2 tau_int); the FINAL per-bin error = max(block-SEM(10 blocks),
sigma_corr) -- conservative. kappa refit: same all-bin signed
weighted fit as 2714, with corrected weights.
CHAIN VARIATION: MAIN-A vs MAIN-B corrected |diff| vs 2*combined.
CLASSIFICATION RULE (frozen): at a_s = 0.04, D = |kappa_sim_corr -
kappa_HNC| / sigma_comb with kappa_HNC = 1.0206*kappa_D and
sigma_HNC = 1.5% * kappa_D:
  - D <= 2 and chains consistent -> "SIMULATION-ERROR (RESOLVED):
    the tension was underestimated errors" (Gemini 1.5 sigma target
    also reported);
  - D > 2 and chains consistent -> "CLOSURE-ERROR CANDIDATE or
    UNRESOLVED";
  - chains inconsistent -> "SIMULATION-ERROR (UNRESOLVED SAMPLING)".
MONOTONICITY: re-verified with corrected errors (2-sigma alternation
test, all bins, frozen window)."""
import math, json, numpy as np

PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
RUNS=["MAIN-A","MAIN-B","SIZE-S","SIZE-L","CORE"]
K_HNC={0.04:1.0206*KAPPA, 0.02:1.0042*KAPPA}
res={}
for label in RUNS:
    d=json.load(open(f"/tmp/s4e_{label}.json"))
    profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]; a_s=d["a_s"]
    n=len(profs); rcen=(np.arange(nb)+0.5)*rmax/nb
    lo,hi=2*a_s,3.0/KAPPA
    m=(rcen>lo)&(rcen<hi)
    mean=profs.mean(0)
    w=np.where(m,mean,0.0)
    u=profs@w
    uc=u-u.mean()
    ac=np.correlate(uc,uc,'full')[n-1:]/ (uc.var()*np.arange(n,0,-1))
    tau=0.5; W=n-1
    for t in range(1,n):
        tau+=ac[t]
        if t>=5*tau: W=t; break
    ess=n/(2*tau)
    sem_naive=profs.std(0,ddof=1)/math.sqrt(n)
    sig_corr=sem_naive*math.sqrt(2*tau)
    nblk=10; bl=n//nblk
    bm=np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(nblk)])
    sem_blk=bm.std(0,ddof=1)/math.sqrt(nblk)
    sig=np.maximum(sem_blk,sig_corr)
    x,y,e=rcen[m],mean[m],np.maximum(sig[m],1e-7)
    from scipy.optimize import curve_fit
    fm=lambda r_,Aa,k_: Aa*np.exp(-k_*r_)/r_
    pm,pc=curve_fit(fm,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=20000)
    kfit=pm[1]; kerr=math.sqrt(max(pc[1][1],0))
    lead=np.sign(y[np.argmax(np.abs(y))])
    viol=int(np.sum((np.sign(y)!=lead)&(np.abs(y)>2*e)))
    res[label]=(kfit,kerr,tau,ess,viol,a_s)
    print(f"[{label}] a_s={a_s}: tau_int={tau:.2f} samples (window {W}) ESS={ess:.0f} | "
          f"kappa_corr={kfit:.3f}+/-{kerr:.3f} ({kfit/KAPPA:.4f}x, was 2714 naive) | alt={viol}")
kA,eA=res["MAIN-A"][0],res["MAIN-A"][1]; kB,eB=res["MAIN-B"][0],res["MAIN-B"][1]
comb=math.sqrt(eA*eA+eB*eB)
chains_ok=abs(kA-kB)<=2*comb
kmain=0.5*(kA+kB); emain=0.5*comb
sig_hnc=0.015*KAPPA
D=abs(kmain-K_HNC[0.04])/math.sqrt(emain**2+sig_hnc**2)
print(f"\nMAIN combined (corrected): {kmain:.3f}+/-{emain:.3f} ({kmain/KAPPA:.4f}x) ; "
      f"|A-B|={abs(kA-kB):.3f} vs 2*comb={2*comb:.3f} -> chains {'CONSISTENT' if chains_ok else 'INCONSISTENT'}")
print(f"a_s=0.04 tension: D = |{kmain/KAPPA:.4f} - 1.0206| / sigma_comb = {D:.2f} sigma "
      f"(Gemini 1.5-sigma target: {'MET' if D<=1.5 else 'NOT MET'})")
kC,eC=res["CORE"][0],res["CORE"][1]
DC=abs(kC-K_HNC[0.02])/math.sqrt(eC**2+sig_hnc**2)
print(f"a_s=0.02 check: D = {DC:.2f} sigma")
if D<=2 and chains_ok: cls="SIMULATION-ERROR (RESOLVED): underestimated errors"
elif chains_ok: cls="CLOSURE-ERROR CANDIDATE or UNRESOLVED"
else: cls="SIMULATION-ERROR (UNRESOLVED SAMPLING)"
print(f"CLASSIFICATION (frozen rule): {cls}")
print(f"Monotonicity under corrected errors: "
      f"{'PRESERVED (0 alternations everywhere)' if all(r[4]==0 for r in res.values()) else 'CHECK'}")
