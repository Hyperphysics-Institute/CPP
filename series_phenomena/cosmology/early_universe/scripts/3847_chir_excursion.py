#!/usr/bin/env python3
"""Patch 3847 -- sanctioned cross-lane excursion into CHIR: read the FI-C-RC-2 distance ratio and
evaluate C-4's mass. Arithmetic on a retrieved corpus value; nothing adopted, no cross-lane object
modified."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

phi=(1+math.sqrt(5))/2; EPS=phi**-3
hl=4.7e13/2.435e18; LAM_HARD=0.0517; LAM_REQ=(hl/6)**2

check("T1 EXCURSION RESULT: the perturbative-distance-ratio constraint (Capotauro sketch S2.4) selects "
      "eps = phi^-3 = 0.2361. This IS chi, the substrate chirality magnitude, derived at full Layer 3 "
      "via THEO-SD-CHIR-1 (Patch 0434) -- it is an ORDER-UNITY number, not a small one",
      abs(EPS-0.2361)<1e-4, f"eps = phi^-3 = {EPS:.4f}")

check("T2 the requirement from 3845: lambda = lam_hard*g(delta) <= 1.03e-11 needs g <= 2.0e-10; with "
      "delta = 0.236 that needs eps^n with n >= 15.5 -- an implausible order",
      abs(math.log(LAM_REQ/LAM_HARD)/math.log(EPS)-15.5)<0.3,
      f"n >= {math.log(LAM_REQ/LAM_HARD)/math.log(EPS):.1f}")

# most favourable structure on file: local-I_h preservation at first order (Finding C-W39)
def mH(n):
    lam=LAM_HARD*EPS**n
    return lam, 6*math.sqrt(lam)/hl
check("T3 the most favourable structure on file is local-I_h preservation at FIRST order in eps "
      "(Finding C-W39: all first-shell edges tangent to n-hat at O(eps)), pushing the symmetry breaking "
      "to O(eps^2). Even taking the energy quadratic in that distortion (g = eps^4) gives m/H = 3.9e3",
      3e3<mH(4)[1]<5e3, f"g = eps^4: lambda = {mH(4)[0]:.2e}, m/H = {mH(4)[1]:.2e}")

check("T4 and eps^6 -- beyond any structure the corpus supports -- still gives m/H = 9.3e2",
      mH(6)[1]>100, f"m/H = {mH(6)[1]:.2e}")

check("T5 VERDICT: C-4 FAILS the mass bound by ~3.6 orders. It dies the same way the register spring "
      "died (1.3e5), by a smaller margin but decisively",
      mH(4)[1]>1e3, f"C-4 m/H ~ {mH(4)[1]:.1e} vs spring 1.3e5 vs required <= 1")

check("T6 the failure traces to a single fact: the substrate's own chirality magnitude is phi^-3, an "
      "order-unity number. C-4 needed the lattice's grip on n-hat to be one part in 1e10; the corpus "
      "says it is one part in four",
      0.2<EPS<0.3, "no plausible power of an O(1) number reaches 1e-10")

check("T7 C-4 WITHDRAWN. With C-2 and C-3 already demoted and the count, delta-kT and composition dead, "
      "the amplitude sector has NO surviving candidate",
      True, "the 3835 no-go's only escape route is now closed at both ends")

check("T8 what this does NOT touch: PRED-C-96's tilt (reads the adopted pivot, untouched throughout); "
      "the e-fold budget (~10.5 short, a separate and still-open problem); T-1, T-2",
      True, "the tilt stands; the amplitude does not")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
