#!/usr/bin/env python3
"""RV-3 X6 battery (Patch 2761, RV-2714 prereg) -- the FROZEN 2735
matched-functional battery re-run VERBATIM against the CLEAN RV
chains. Only the sim input paths/labels differ from the committed
2735 script; functionals, windows, solver, gates identical."""

import math, json, numpy as np
from scipy.fft import dst
from scipy.optimize import curve_fit
from scipy.special import erfc as serfc

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; NSP=NCP/2.0; Q2=ALPHA_EM*HBARC
THETA0=2*math.sqrt(2)*math.pi*Q2/A
N=4096; dr=0.002; R=N*dr
r=(np.arange(N)+1)*dr; k=(np.arange(N)+1)*math.pi/R
def ft(f):  return 4*math.pi/k*dst(r*f,type=1)*dr/2.0
def ift(F): return (1.0/(2*math.pi**2*r))*dst(k*F,type=1)*(math.pi/R)/2.0

def solve_hnc_hd(a_s,mix=0.25,itmax=8000,tol=1e-9):
    """Verbatim copy of the committed 2721 solver with h_d exposed."""
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
        dcv=max(np.max(np.abs(g_pp_n-g_pp)),np.max(np.abs(g_pm_n-g_pm)))
        g_pp=(1-mix)*g_pp+mix*g_pp_n; g_pm=(1-mix)*g_pm+mix*g_pm_n
        if dcv<tol: break
    c_pp=np.exp(-beta*v0+g_pp)-1.0-g_pp
    c_pm=np.exp(+beta*v0+g_pm)-1.0-g_pm
    hd=(c_pp-c_pm)+(g_pp-g_pm)
    hd_k=cd+gd_k
    Szz=1.0+NSP*hd_k
    return hd,Szz

def slope(rr,hh,lo,hi,sig=None):
    m=(rr>=lo)&(rr<=hi)&(np.abs(hh)>0)
    if sig is None:
        co=np.polyfit(rr[m],np.log(np.abs(hh[m])*rr[m]),1)
        return -co[0],0.0
    x,y,e=rr[m],hh[m],np.maximum(sig[m],1e-8)
    fmn=lambda r_,Aa,k_: Aa*np.exp(-k_*r_)/r_
    pm,pc=curve_fit(fmn,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=20000)
    return pm[1],math.sqrt(max(pc[1][1],0))

# --- self-validation gate ---
hd04,Szz04=solve_hnc_hd(0.04); hd02,Szz02=solve_hnc_hd(0.02)
v04,_=slope(r,hd04,0.40,1.00); v02,_=slope(r,hd02,0.40,1.00)
print(f"GATE: local solver on [0.40,1.00]: {v04/KAPPA:.4f} / {v02/KAPPA:.4f} "
      f"(committed 1.0206 / 1.0042) -> "
      f"{'PASS' if abs(v04/KAPPA-1.0206)<0.001 and abs(v02/KAPPA-1.0042)<0.001 else 'FAIL-STOP'}")

# --- sim data ---
def simprof(label):
    d=json.load(open(f"/tmp/rv2714/rv_RV-{label}.json"))
    profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]
    rcen=(np.arange(nb)+0.5)*rmax/nb
    n=len(profs)
    mean=profs.mean(0)
    sem_naive=profs.std(0,ddof=1)/math.sqrt(n)
    nblk=10; bl=n//nblk
    bm=np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(nblk)])
    sem_blk=bm.std(0,ddof=1)/math.sqrt(nblk)
    sig=np.maximum(sem_blk,sem_naive*math.sqrt(2*0.55))
    return rcen,mean,sig,d
rA,mA,sA,dA=simprof("MAIN-A"); rB,mB,sB,dB=simprof("MAIN-B"); rC,mC,sC,dC=simprof("CORE")
mAB=0.5*(mA+mB); sAB=0.5*np.sqrt(sA**2+sB**2)

print("\n== F1: matched SIM window (2a_s, 3/kD) ==")
kS1,eS1=slope(rA,mAB,0.08,3.0/KAPPA,sAB)
kH1,_=slope(r,hd04,0.08,3.0/KAPPA)
D1=abs(kS1-kH1)/math.sqrt(eS1**2+(0.015*KAPPA)**2)
print(f"  a_s=0.04: sim {kS1/KAPPA:.4f}+/-{eS1/KAPPA:.4f} vs HNC {kH1/KAPPA:.4f} -> {D1:.2f} sigma")
kS1c,eS1c=slope(rC,mC,0.04,3.0/KAPPA,sC)
kH1c,_=slope(r,hd02,0.04,3.0/KAPPA)
print(f"  a_s=0.02: sim {kS1c/KAPPA:.4f}+/-{eS1c/KAPPA:.4f} vs HNC {kH1c/KAPPA:.4f} -> "
      f"{abs(kS1c-kH1c)/math.sqrt(eS1c**2+(0.015*KAPPA)**2):.2f} sigma")

print("\n== F2: matched FAR window [0.40, 0.88] ==")
kS2,eS2=slope(rA,mAB,0.40,0.88,sAB)
kH2,_=slope(r,hd04,0.40,0.88)
adv=" (ADVISORY: sim error >10%)" if eS2/kS2>0.10 else ""
print(f"  a_s=0.04: sim {kS2/KAPPA:.4f}+/-{eS2/KAPPA:.4f} vs HNC {kH2/KAPPA:.4f} -> "
      f"{abs(kS2-kH2)/math.sqrt(eS2**2+(0.015*KAPPA)**2):.2f} sigma{adv}")

print("\n== F3: matched k-space pole (shells n^2=1,2,3 of the MAIN box) ==")
def pole_from_szz(kk,ss):
    x=kk*kk; y=kk*kk/ss
    co=np.polyfit(x,y,1)
    return math.sqrt(max(co[1],0))
k2A=np.array(dA["k2"]); szzA=np.array(dA["szz"]); k2B=np.array(dB["k2"]); szzB=np.array(dB["szz"])
LA=dA["L"]; n2=np.round(k2A/(2*math.pi/LA)**2).astype(int)
kk=[];ssA=[];ssB=[]
for v in (1,2,3):
    j=np.where(n2==v)[0]
    kk.append(math.sqrt(k2A[j].mean())); ssA.append(szzA[j].mean()); ssB.append(szzB[j].mean())
kk=np.array(kk); ssSim=0.5*(np.array(ssA)+np.array(ssB))
kpS=pole_from_szz(kk,ssSim)
SzzH=np.interp(kk,k,Szz04)
kpH=pole_from_szz(kk,SzzH)
# sim pole error: from A-B spread
kpA=pole_from_szz(kk,np.array(ssA)); kpB=pole_from_szz(kk,np.array(ssB))
epS=abs(kpA-kpB)/2+0.02*KAPPA
D3=abs(kpS-kpH)/math.sqrt(epS**2+(0.015*KAPPA)**2)
print(f"  a_s=0.04: sim pole {kpS/KAPPA:.4f}+/-{epS/KAPPA:.4f} (A:{kpA/KAPPA:.4f} B:{kpB/KAPPA:.4f}) "
      f"vs HNC-at-same-k {kpH/KAPPA:.4f} -> {D3:.2f} sigma")

print("\n== DIAGNOSTIC: HNC window-sensitivity (a_s=0.04, end 0.88) ==")
for r0 in (0.08,0.20,0.40):
    kv,_=slope(r,hd04,r0,0.88)
    print(f"  window [{r0:.2f},0.88]: kappa/kD = {kv/KAPPA:.4f}")

upd = (D1<=2) and (D3<=2)
print(f"\nCLASSIFICATION UPDATE (frozen rule): F1={'PASS' if D1<=2 else 'FAIL'} "
      f"F3={'PASS' if D3<=2 else 'FAIL'} -> "
      f"{'EXTRACTION-SYSTEMATIC (X1 classification updates)' if upd else 'CLOSURE-ERROR CANDIDATE / UNRESOLVED stands; X3+X4 carry'}")
