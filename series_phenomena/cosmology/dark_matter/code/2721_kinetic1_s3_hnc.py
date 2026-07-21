#!/usr/bin/env python3
"""KINETIC-1 K1-S3 (Patch 2721) under the FROZEN 2718 charter SS3.

METHOD DECLARATION (frozen HERE, before any coefficient is extracted):
Hypernetted-chain (HNC) closure of the two-component Ornstein-Zernike
equations for the EXACT simulated system -- symmetric +/- soft-Coulomb
fluid, v_ab(r) = z_a z_b q^2 / sqrt(r^2 + a_s^2), at the closed
parameters (theta = 35.1495 MeV, q^2 = alpha_EM hbar c, per-species
density n = n_CP/2 = 29.318 /fm^3). Long range handled by the erf
split (v_long = z z q^2 erf(r/sigma)/r, sigma = 4 a_s, analytic FT);
radial grid N = 4096, dr = 0.002 fm; sine-transform OZ; Picard with
mixing; convergence max|dgamma| < 1e-9. The chain function's own
Coulomb tail is renormalized ANALYTICALLY (gamma_d = gamma_d^short +
G_lr with G_lr = 2 beta Q2 [1/r - e^{-kappa_D r}/r], transformed in
closed form) -- the finite-box Dirichlet truncation bug this repairs
was caught by the validation gate on the first run and is disclosed
in the record.
VALIDATION GATE (must pass before any prediction is read): at
theta x 100 (Gamma/100) the extracted kappa_eff must equal kappa_D
within 0.5%.
EXTRACTION (frozen): kappa_eff = -slope of ln|r h_d(r)| over
r in [0.40, 1.00] fm. PREDICTION TARGETS (compared only after the
predictions print): S4-E kappa_fit/kappa_D = 1.106 +/- 0.023
(a_s = 0.04) and 1.036 +/- 0.040 (a_s = 0.02). Expected HNC closure
accuracy at Gamma ~ 0.2: few percent (stated in advance).
GP-limit statement: the a_s ladder {0.04, 0.02, 0.01, 0.005} at the
reconciled Gamma gives the method's a_s -> 0 prediction for the
physical kappa_eff/kappa_D. Gamma ladder {0.5, 1, 2} x Gamma_rec at
a_s = 0.04 characterizes the correction's Gamma-scaling (fitted
exponent reported as characterization, not theorem)."""
import math, numpy as np
from scipy.fft import dst, idst

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; NSP=NCP/2.0; Q2=ALPHA_EM*HBARC
THETA0=2*math.sqrt(2)*math.pi*Q2/A

N=4096; dr=0.002; R=N*dr
r=(np.arange(N)+1)*dr
k=(np.arange(N)+1)*math.pi/R

def ft(f):   # 3D radial FT: f(k) = 4pi/k * int r f sin(kr) dr  via DST-I
    return 4*math.pi/k * dst(r*f,type=1)*dr/2.0
def ift(F):
    return 1.0/(2*math.pi**2*r) * dst(k*F,type=1)*(math.pi/R)/2.0/ (math.pi/R) * (math.pi/R)
def ift2(F):
    return (1.0/(2*math.pi**2)) / r * dst(k*F,type=1) * (math.pi/R) / 2.0

def solve_hnc(theta,a_s,mix=0.25,itmax=8000,tol=1e-9):
    beta=1.0/theta
    sig=4*a_s
    v0=Q2/np.sqrt(r*r+a_s*a_s)          # magnitude; pp=+v0, pm=-v0
    vl=Q2*np.vectorize(math.erf)(r/sig)/r
    vl_k=4*math.pi*Q2/(k*k)*np.exp(-k*k*sig*sig/4.0)
    kD=math.sqrt(4*math.pi*NCP*Q2*beta)
    # analytic long-range part of the d-channel chain function
    G_lr=2*beta*Q2*(1.0-np.exp(-kD*r))/r
    G_lr_k=8*math.pi*beta*Q2*kD*kD/(k*k*(k*k+kD*kD))
    g_pp=0.5*G_lr.copy(); g_pm=-0.5*G_lr.copy()   # DH warm start
    for it in range(itmax):
        c_pp=np.exp(-beta*v0+g_pp)-1.0-g_pp
        c_pm=np.exp(+beta*v0+g_pm)-1.0-g_pm
        cs_pp=ft(c_pp+beta*vl)-beta*vl_k
        cs_pm=ft(c_pm-beta*vl)+beta*vl_k
        cd=cs_pp-cs_pm; cs=cs_pp+cs_pm
        gd_k=NSP*cd*cd/(1.0-NSP*cd)
        gs_k=NSP*cs*cs/(1.0-NSP*cs)
        gd=ift2(gd_k-G_lr_k)+G_lr        # renormalized inverse
        gs=ift2(gs_k)
        g_pp_n=0.5*(gs+gd); g_pm_n=0.5*(gs-gd)
        d=max(np.max(np.abs(g_pp_n-g_pp)),np.max(np.abs(g_pm_n-g_pm)))
        g_pp=(1-mix)*g_pp+mix*g_pp_n
        g_pm=(1-mix)*g_pm+mix*g_pm_n
        if d<tol: break
    c_pp=np.exp(-beta*v0+g_pp)-1.0-g_pp
    c_pm=np.exp(+beta*v0+g_pm)-1.0-g_pm
    hd=(c_pp-c_pm)+(g_pp-g_pm)
    m=(r>=0.40)&(r<=1.00)&(np.abs(hd)>0)
    co=np.polyfit(r[m],np.log(np.abs(hd[m])*r[m]),1)
    keff=-co[0]
    hd_k=cd+gd_k                        # k-space, truncation-free
    Szz=1.0+NSP*hd_k
    return keff,d,it,(k,Szz)

print("== VALIDATION GATE (theta x 100 -> Gamma/100 must reproduce DH) ==")
th=100*THETA0
kD=math.sqrt(4*math.pi*NCP*Q2/th)
keff,dcv,it,_=solve_hnc(th,0.04)
print(f"  Gamma={Q2*kD/th:.5f}: kappa_eff={keff:.4f} vs kappa_D={kD:.4f} "
      f"(ratio {keff/kD:.4f}) conv={dcv:.1e}@{it}  -> "
      f"{'PASS' if abs(keff/kD-1)<0.005 else 'FAIL'}")

print("\n== PREDICTIONS (printed before target comparison) ==")
preds={}
for a_s in (0.04,0.02,0.01,0.005):
    keff,dcv,it,sz=solve_hnc(THETA0,a_s)
    preds[a_s]=keff
    print(f"  a_s={a_s:.3f} fm: kappa_eff = {keff:.4f} /fm  "
          f"kappa_eff/kappa_D = {keff/KAPPA:.4f}  conv={dcv:.1e}@{it}")
kk,Szz=sz
mlow=(kk>0)&(kk<3.0)
print(f"  S_zz small-k (a_s=0.005): "+", ".join(
    f"k={kk[j]:.2f}:{Szz[j]:.4f}" for j in np.where(mlow)[0][::300][:4]))

print("\n== Gamma-scaling characterization (a_s=0.04) ==")
sc=[]
for f in (0.5,1.0,2.0):
    th=THETA0/f   # Gamma scales as theta^-3/2 at fixed q,n... report actual Gamma
    kD=math.sqrt(4*math.pi*NCP*Q2/th)
    keff,_,_,_=solve_hnc(th,0.04)
    G=Q2*kD/th
    sc.append((G,keff/kD))
    print(f"  Gamma={G:.4f}: kappa_eff/kappa_D = {keff/kD:.4f}")
lg=np.log([s[0] for s in sc]); le=np.log([s[1]-1 for s in sc])
p=np.polyfit(lg,le,1)
print(f"  fitted excess-scaling exponent d ln(k/kD - 1)/d ln Gamma = {p[0]:.2f} "
      f"(characterization only)")

print("\n== COMPARISON TO THE FROZEN TARGETS ==")
for a_s,tgt,err in ((0.04,1.106,0.023),(0.02,1.036,0.040)):
    pr=preds[a_s]/KAPPA
    print(f"  a_s={a_s}: HNC {pr:.4f} vs S4-E {tgt:.3f}+/-{err:.3f} -> "
          f"deviation {abs(pr-tgt)/err:.2f} sigma")
print(f"  GP-limit trend: a_s->0 HNC prediction kappa_eff/kappa_D = "
      f"{preds[0.005]/KAPPA:.4f} (ladder {', '.join(f'{preds[a]/KAPPA:.4f}' for a in (0.04,0.02,0.01,0.005))})")
print(f"  implied physical screening at this coupling: l = {1/preds[0.005]:.4f} fm "
      f"vs leading-order d_DP/2 = {A/2:.4f} fm")
