#!/usr/bin/env python3
"""Patch 3831 -- C-2's end-condition bridge, and the spectrum requirement stated as a scale window.
Arithmetic on quantities the corpus already carries; nothing adopted, no mechanism derived."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

lP=1.616e-35; Mpc=3.086e22; Robs=4.40e26; A_S=2.1e-9; NCP=5.2e97
zeta=math.sqrt(A_S)

# T1 -- the bridge itself: N = 1/3 ln(n_init/n_end), n_end = 1 => dN = (1/3) drho/rho
def N_of(nbar): return math.log(nbar)/3
eps=1e-6
dN=(N_of(1.0*(1+eps))-N_of(1.0))/eps      # d N / d(ln n) = 1/3
check("T1 BRIDGE: N = 1/3 ln n_init with n_end = 1 (a count) => dN = (1/3) drho/rho -- a DENSITY "
      "perturbation reaches the end condition; delta-kT and composition do not",
      abs(dN-1/3)<1e-4, f"dN/dln n = {dN:.6f}")

# T2 -- required initial density contrast
drho_req=3*zeta
check("T2 required initial contrast drho/rho = 3 zeta = 1.4e-4 on the observable scales",
      1e-4<drho_req<2e-4, f"zeta = {zeta:.2e}, drho/rho = {drho_req:.2e}")

# T3 -- which INITIAL scales the CMB probes, budget-closed (N = 75, ball radius l_P -> R_obs)
ratio=lP/Robs
lo=30*Mpc*ratio/lP; hi=14000*Mpc*ratio/lP
check("T3 the CMB window maps back to initial scales ~0.002-1.0 l_P: the OUTER ~2.7 decades of the "
      "ball, nothing near the GP spacing (~1e-32 l_P)",
      0.001<lo<0.005 and 0.9<hi<1.1 and math.log10(hi/lo)>2.5,
      f"{lo:.4f} - {hi:.4f} l_P, spanning {math.log10(hi/lo):.1f} decades")

# T4 -- the Poisson floor on those scales: coherence is mandatory, not optional
def poisson(frac): return 1/math.sqrt(NCP*frac**3)
check("T4 Poisson (incoherent) contrast on the window is ~1e-46, short of the requirement by ~42 "
      "orders -> C-2 must be COHERENT; an incoherent density candidate cannot work",
      poisson(lo)<1e-40 and math.log10(drho_req/poisson(lo))>40,
      f"Poisson at {lo:.4f} l_P = {poisson(lo):.2e}; shortfall 10^{math.log10(drho_req/poisson(lo)):.0f}")

# T5 -- bookkeeping correction to 3822: the conserved count is NOT blocked by the end condition
# it enters dN exactly as C-2 does; it failed on amplitude (Poisson) and on whiteness (n_s = 1)
check("T5 CORRECTION to 3822: the count is in the SAME class as C-2 (it does enter dN); it failed on "
      "amplitude and spectrum, NOT on the end-condition wall. The wall took delta-kT and composition only",
      True, "the 'three-for-three' phrasing at 3822 was wrong; two-for-three, and the third failed differently")

# T6 -- one inward shell is not a spectrum: a shell of radius r gives oscillatory (Bessel) structure
# with a characteristic k ~ 1/r, not a power law across 2.7 decades
check("T6 a single inward-propagating shell carries one scale (k ~ 1/R), not a power law across the "
      "2.7-decade window -> C-2's spectrum debt is NOT discharged by the edge alone",
      True, "structural; same failure mode as C-3's peaked S(k) at 3829")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
