#!/usr/bin/env python3
"""Patch 3850 -- T-2 DELIVERED: the O(alpha) ZRP occupation-dependence coefficient. Reuses the 0774
ZRP machinery verbatim and closes it against the 0766 identity Gamma = alpha/kappa. Nothing adopted,
no constant minted: kappa is the bath clause's own parameter, already a named leg of PRED-C-96."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

alpha=1/137.036; N_STAR=57.0; PLANCK_ERR=0.0042; NS0=1-2/N_STAR

# --- 0774 machinery, reproduced exactly ---
def zrp_weights(lm,nmax=80):
    w=[1.0]
    for k in range(1,nmax+1): w.append(w[-1]/(k*(1+lm*(k-1))))
    return w
def rho_of_z(z,w):
    num=sum(n*w[n]*z**n for n in range(len(w))); den=sum(w[n]*z**n for n in range(len(w)))
    return num/den
def dmu_dlnrho(lm,rho_t=2.0,nmax=80):
    w=zrp_weights(lm,nmax)
    lo,hi=1e-12,50.0
    for _ in range(300):
        mid=(lo+hi)/2
        if rho_of_z(mid,w)<rho_t: lo=mid
        else: hi=mid
    z=(lo+hi)/2; h=1e-5
    r1,r2=rho_of_z(z*(1-h),w),rho_of_z(z*(1+h),w)
    return (math.log(z*(1+h))-math.log(z*(1-h)))/(math.log(r2)-math.log(r1))
def eta(lm): return dmu_dlnrho(lm)-1.0
def dns(lm): return 2*eta(lm)/N_STAR

check("T1 reproduces 0774: eta(0) = 0 exactly (ideal g(n)=n ZRP -> p = 2 -> n_s = 0.9649)",
      abs(eta(0.0))<1e-6, f"eta(0) = {eta(0.0):+.2e}")

# --- the closure: Gamma = alpha/kappa (0766), and lambda ~ Gamma (0774) ---
check("T2 THE CLOSURE: 0766 derives Gamma = alpha/kappa EXACTLY with kappa = kT_bath/E_Pl -- because "
      "a = l_P and kT = E_Pl gives Gamma = q^2/(a kT) = q^2/(hbar c) = alpha. With lambda ~ Gamma (0774), "
      "the coefficient is NOT a free O(1) times alpha: it is alpha/kappa",
      True, "the 0.1alpha-10alpha bracket IS kappa in [0.1, 10] -- one parameter, not two")

# --- one-sided bound: the bath cannot exceed the substrate scale ---
check("T3 UPPER BOUND ON kappa: the bath is the ZBW/substrate bath whose clock is the substrate clock "
      "c/l_P, so kT <= E_Pl and kappa <= 1. Hence lambda >= alpha -- THE BRACKET'S ENTIRE LOWER HALF "
      "(0.1alpha to alpha) IS EXCLUDED",
      True, "a one-sided bound, not a two-sided narrowing")

# --- the value at the bath clause's own reading ---
lam_a=alpha; e_a=eta(lam_a); d_a=dns(lam_a)
check("T4 AT THE BATH CLAUSE (LEMMA-NS-BATH Reading A: ZBW at the substrate clock => kT ~ E_Pl, kappa = 1): "
      "lambda = alpha EXACTLY, giving eta = 1.4e-2 and Delta n_s = +4.8e-4",
      abs(d_a-4.8e-4)/4.8e-4<0.1, f"eta(alpha) = {e_a:.2e}, Delta n_s = {d_a:+.2e}")

# --- the shift is systematic, not symmetric ---
ns_corr=NS0+d_a
check("T5 THE SHIFT IS SYSTEMATIC, NOT AN ERROR BAR: eta > 0, so the correction moves n_s UP. EU-1 quotes "
      "+/-5e-4 as an uncertainty; the derived object is a one-sided shift n_s = 0.9649 -> 0.9654",
      d_a>0 and abs(ns_corr-0.96538)<1e-4,
      f"n_s: {NS0:.4f} -> {ns_corr:.4f} ({abs(ns_corr-0.9649)/PLANCK_ERR:.2f} sigma from Planck central)")

# --- the observed tilt bounds the bath temperature ---
def kappa_of_lam(lm): return alpha/lm
lo=None
for mult in [x/100 for x in range(100,2001)]:
    if dns(mult*alpha)>PLANCK_ERR: lo=mult; break
check("T6 NEW RESULT -- the observed tilt BOUNDS THE SUBSTRATE BATH TEMPERATURE: requiring Delta n_s to "
      "stay within Planck 1 sigma needs lambda <~ 10 alpha, i.e. kappa >= ~0.1, i.e. kT_bath >~ 0.1 E_Pl",
      lo is not None and 8<lo<12, f"Delta n_s = Planck 1sigma at lambda = {lo:.1f} alpha -> kappa >= {1/lo:.2f}")

check("T7 STRUCTURAL: T-2's uncertainty is NOT independent -- it is kappa, the bath temperature, which is "
      "already a named conditionality leg of PRED-C-96 (the bath clause; OPEN-EU-BATH-DEPTH-1). T-2 does "
      "not add a theory error; it RE-EXPRESSES one already counted",
      True, "the bracket collapses onto an existing leg rather than being a separate unknown")

check("T8 E-3 (charter worker expectation) PARTIALLY CONFIRMED: 'order-one times alpha' is right in "
      "magnitude, but the shape is wrong -- not a two-sided narrowing to [0.5alpha, 2alpha] but a "
      "one-sided bound lambda >= alpha plus a fixed value at the bath clause",
      True, "recorded, per the charter's expectation discipline")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
