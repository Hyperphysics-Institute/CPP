#!/usr/bin/env python3
"""X3/X4 requirement-7 leg (Patch 2787) under the FROZEN 2786 prereg.
High-resolution S_zz(k) vs HNC on the ARCHIVED clean rv2714 chains.
Zero new simulation. HNC = the committed 2721/2761 solver VERBATIM
(self-validation gate re-fired before any comparison is read).

DEVIATION DEV-1 (disclosed same-font, panel ratification requested):
the frozen prereg operationalized req-7 errors as per-sample bootstrap;
the archived szz are time-averaged accumulations with no per-sample
record, so bootstrap is unimplementable on the archive. Implemented
error model (maximal honest): between-chain half-spread where two
independent chains share a geometry (MAIN-A/B), quadrature with the
committed +/-1.5% HNC closure floor; single-chain geometries report the
ratio with the HNC floor only, marked ADVISORY, no sigma quoted."""
import math, json, gzip
import numpy as np
from scipy.fft import dst

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; NSP=NCP/2.0; Q2=ALPHA_EM*HBARC
THETA0=2*math.sqrt(2)*math.pi*Q2/A
N=4096; dr=0.002; R=N*dr
r=(np.arange(N)+1)*dr; k=(np.arange(N)+1)*math.pi/R

def ft(f):  return 4*math.pi/k*dst(r*f,type=1)*dr/2.0
def ift(F): return (1.0/(2*math.pi**2*r))*dst(k*F,type=1)*(math.pi/R)/2.0

def solve_hnc_szz(a_s,mix=0.25,itmax=8000,tol=1e-9):
    """Verbatim 2721/2761 solver, Szz(k) exposed truncation-free."""
    beta=1.0/THETA0; sig=4*a_s
    v0=Q2/np.sqrt(r*r+a_s*a_s)
    vl=Q2*np.vectorize(math.erf)(r/sig)/r
    vl_k=4*math.pi*Q2/(k*k)*np.exp(-k*k*sig*sig/4.0)
    kD=math.sqrt(4*math.pi*NCP*Q2*beta)
    G_lr=2*beta*Q2*(1.0-np.exp(-kD*r))/r
    G_lr_k=8*math.pi*beta*Q2*kD*kD/(k*k*(k*k+kD*kD))
    g_pp=0.5*G_lr.copy(); g_pm=-0.5*G_lr.copy()
    for it in range(itmax):
        c_pp=np.exp(-beta*v0+g_pp)-1.0-g_pp
        c_pm=np.exp(+beta*v0+g_pm)-1.0-g_pm
        cs_pp=ft(c_pp+beta*vl)-beta*vl_k
        cs_pm=ft(c_pm-beta*vl)+beta*vl_k
        cd=cs_pp-cs_pm; cs=cs_pp+cs_pm
        gd_k=NSP*cd*cd/(1.0-NSP*cd)
        gs_k=NSP*cs*cs/(1.0-NSP*cs)
        gd=ift(gd_k-G_lr_k)+G_lr
        gs=ift(gs_k)
        g_pp_n=0.5*(gs+gd); g_pm_n=0.5*(gs-gd)
        d=max(np.max(np.abs(g_pp_n-g_pp)),np.max(np.abs(g_pm_n-g_pm)))
        g_pp=(1-mix)*g_pp+mix*g_pp_n
        g_pm=(1-mix)*g_pm+mix*g_pm_n
        if d<tol: break
    c_pp=np.exp(-beta*v0+g_pp)-1.0-g_pp
    c_pm=np.exp(+beta*v0+g_pm)-1.0-g_pm
    hd=(c_pp-c_pm)+(g_pp-g_pm)
    cd_f=ft(c_pp-c_pm)  # note: without lr split ONLY for gate slope; use split form:
    cs_pp=ft(c_pp+np.float64(1.0)*0)  # placeholder no-op
    # recompute split-form cd for Szz (as in loop)
    vl_=Q2*np.vectorize(math.erf)(r/sig)/r
    cs_ppf=ft(c_pp+beta*vl_)-beta*vl_k
    cs_pmf=ft(c_pm-beta*vl_)+beta*vl_k
    cdf=cs_ppf-cs_pmf
    gd_k=NSP*cdf*cdf/(1.0-NSP*cdf)
    hd_k=cdf+gd_k
    Szz=1.0+NSP*hd_k
    m=(r>=0.40)&(r<=1.00)&(np.abs(hd)>0)
    co=np.polyfit(r[m],np.log(np.abs(hd[m])*r[m]),1)
    return -co[0], d, it, Szz

# --- self-validation gate (frozen: reproduce committed slope ratios) ---
k04,d04,i04,S04=solve_hnc_szz(0.04)
k02,d02,i02,S02=solve_hnc_szz(0.02)
g_ok = abs(k04/KAPPA-1.0206)<0.001 and abs(k02/KAPPA-1.0042)<0.001
print(f"GATE: HNC slopes {k04/KAPPA:.4f}/{k02/KAPPA:.4f} vs committed 1.0206/1.0042 "
      f"conv {d04:.1e}@{i04},{d02:.1e}@{i02} -> {'PASS' if g_ok else 'FAIL-STOP'}")
assert g_ok

HNC={0.04:S04,0.02:S02}
def shells(label):
    d=json.load(gzip.open(f"data/rv2714/rv_RV-{label}.json.gz"))
    k2=np.array(d["k2"]); szz=np.array(d["szz"]); L=d["L"]; a_s=d["a_s"]
    n2=np.round(k2/(2*math.pi/L)**2).astype(int)
    out={}
    for v in sorted(set(n2)):
        j=np.where(n2==v)[0]
        kk=math.sqrt(k2[j][0])
        out[v]=(kk,float(szz[j].mean()))
    return a_s,L,out

print("\n== per-shell Delta(k) = S_zz^sim / S_zz^HNC  (k-cut 2*pi/0.08 = 78.5/fm: all shells qualify) ==")
labels=["MAIN-A","MAIN-B","SIZE-S","SIZE-L","CORE"]
data={lab:shells(lab) for lab in labels}
FLOOR=0.015

# MAIN pair: combined with between-chain half-spread (+) HNC floor
aA,LA,shA=data["MAIN-A"]; aB,LB,shB=data["MAIN-B"]
assert abs(LA-LB)<1e-9
common=sorted(set(shA)&set(shB))
print(f"\n-- MAIN-A/B combined (N=686, a_s=0.04, L={LA:.4f}) : sigma quotable --")
persist=[]
for v in common:
    kk,sA_=shA[v]; _,sB_=shB[v]
    sH=float(np.interp(kk,k,HNC[0.04]))
    dA_=sA_/sH; dB_=sB_/sH; dm=0.5*(dA_+dB_)
    half=abs(dA_-dB_)/2.0
    err=math.sqrt(half**2+(FLOOR*dm)**2)
    sig=abs(dm-1.0)/err if err>0 else float('inf')
    tag=" **" if sig>2 else ""
    if sig>2: persist.append((kk,dm,sig))
    print(f"   n2={v:2d} k={kk:6.3f}: A={dA_:.4f} B={dB_:.4f} mean={dm:.4f}+/-{err:.4f} ({sig:.2f} sigma){tag}")
if persist:
    ks=[p[0] for p in persist]
    print(f"   PERSISTENT >2sigma k-range: [{min(ks):.3f}, {max(ks):.3f}] /fm ({len(persist)} shells)")
else:
    print("   PERSISTENT >2sigma k-range: NONE")

for lab in ("SIZE-S","SIZE-L","CORE"):
    a_s,L,sh=data[lab]
    print(f"\n-- {lab} (a_s={a_s}, L={L:.4f}) : ADVISORY (single chain; HNC floor only, no sigma) --")
    worst=(0,1.0)
    for v in sorted(sh):
        kk,ss=sh[v]
        sH=float(np.interp(kk,k,HNC[a_s]))
        dd=ss/sH
        if abs(dd-1)>abs(worst[1]-1): worst=(kk,dd)
        print(f"   n2={v:2d} k={kk:6.3f}: Delta={dd:.4f}")
    print(f"   worst |Delta-1|: {abs(worst[1]-1)*100:.2f}% at k={worst[0]:.3f}")
print("\nREQ-7 LEG COMPLETE (archived data only; zero new sweeps).")
