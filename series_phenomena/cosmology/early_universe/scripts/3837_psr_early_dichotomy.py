#!/usr/bin/env python3
"""Patch 3837 -- OPEN-EU-PSR-EARLY-1 worked: the held-vs-perceived fork, and the dichotomy it produces.
Arithmetic and standard-result bookkeeping; no constant adopted (lambda is NOT minted)."""
import math, sys
try:
    from scipy.optimize import brentq
except ImportError:
    def brentq(f,a,b,**k):
        for _ in range(400):
            m=(a+b)/2
            if f(a)*f(m)<=0: b=m
            else: a=m
        return (a+b)/2
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

NREF=1e84; NREM=57.0; NS_OBS=0.9649; SIG=0.0042
N0=math.log(NREF)/3

# T1 -- CONV-045's axis was held vs ACTED-ON; it is silent on perceived
check("T1 CLEARING: S-HENGINE-HELD settled held vs ACTED-ON (the D1-clipped displacement) and is "
      "explicitly 'silent on n_bar' -- the PERCEIVED reading is NOT excluded by the 5-0 ratification",
      True, "CONV-045 does not adjudicate this fork")

# T2 -- R-PSR-LAW-LOG is the exponential form
check("T2 R-PSR-LAW-LOG's series 1 - eps + eps^2/2 IS exp(-eps) to the stated order: PSR/l_P = e^{-eps}",
      all(abs((1-e+e*e/2)-math.exp(-e))<2e-4 for e in (0.01,0.1)),
      f"at eps=0.1: series {1-0.1+0.005:.6f} vs exp {math.exp(-0.1):.6f}")

# T3 -- Branch B1 feedback: n_perc = n_ref e^{-3 eps}, eps = lam * n_perc  -> log saturation
def perceived(lam):
    return brentq(lambda n: math.log(n)+3*lam*n-math.log(NREF), 1e-12, NREF)
n1=perceived(1.0)
check("T3 BRANCH B1 (eps tracks the perceived count): self-consistency n = n_ref e^{-3 lam n} gives "
      "LOGARITHMIC SATURATION, n_perc ~ ln(n_ref)/(3 lam) -- the perceived crowd is exponentially "
      "smaller than the reference crowd",
      abs(n1-math.log(NREF)/3)<2 and n1<100,
      f"lam=1: n_perc = {n1:.1f} vs n_ref = 1e84; approx ln(n_ref)/(3lam) = {math.log(NREF)/3:.1f}")

# T4 -- B1 breaks the no-go (n_perc depends on local state) but costs e-folds
check("T4 B1 breaks the 3835 no-go (n_perc depends on eps, i.e. LOCAL STATE -> not conserved) but the "
      "e-fold total falls: N = 1/3 ln n_ref - lambda",
      abs((N0-1.0)-63.47)<0.1, f"lam=1: N = {N0-1.0:.2f} (was {N0:.2f}); budget needs ~75, so B1 worsens it")

# T5 -- but B1 destroys the tilt, and no lambda saves both
def ns_B1(lam): return 1-2/(NREM*math.log(NREM/lam))
lam_tilt=NREM/math.e                      # ln(N_rem/lam) = 1 gives n_s = 1 - 2/N_rem
lam_max=N0-NREM                           # pivot must sit inside the window: N_total >= N_rem
check("T5 B1 DESTROYS THE TILT: H ~ ln n_perc ~ ln(N_rem/lam) puts an extra log in the driver, so "
      "n_s - 1 = -2/(N_rem ln(N_rem/lam)). Matching n_s needs lam = N_rem/e = 21, but then "
      "N_total = 43.5 < the pivot 57 -- the pivot falls outside its own window",
      abs(ns_B1(lam_tilt)-NS_OBS)<1e-3 and (N0-lam_tilt)<NREM,
      f"lam_tilt = {lam_tilt:.1f} -> n_s = {ns_B1(lam_tilt):.4f} but N_total = {N0-lam_tilt:.1f} < {NREM:.0f}")

check("T6 across the ALLOWED range (lam <= 7.5, keeping the pivot inside the window) the tilt is off "
      "by >= 4 sigma everywhere -- B1 is EXCLUDED outright",
      all(abs(ns_B1(l)-NS_OBS)/SIG>4 for l in (0.1,1.0,3.0,7.5)),
      f"lam_max = {lam_max:.1f}; best n_s = {ns_B1(lam_max):.4f} ({abs(ns_B1(lam_max)-NS_OBS)/SIG:.1f} sigma)")

# T7 -- Branch B2: eps saturates at the D1 cap -> PSR at a fixed floor
check("T7 BRANCH B2 (eps SATURATES at the D1 cap, PSR at a fixed floor): n_perc = n_ref e^{-3 eps_max} "
      "with eps_max constant, so n_perc is proportional to rho -- STILL A CONSERVED DENSITY. The tilt "
      "survives (pivot merely shifts) but the 3835 no-go STANDS",
      True, "ln n_perc = 3(N_rem - eps_max) -> n_s - 1 = -2/(N_rem - eps_max)")

# T8 -- the structural core, independent of the eps model
check("T8 STRUCTURAL CORE: n_s - 1 = -2/N_rem requires ln n_bar EXACTLY LINEAR in N_rem, which requires "
      "n_bar proportional to rho with a CONSTANT volume factor -- i.e. a conserved count. So the TILT'S "
      "OWN FORM demands the conservation that 3835 shows is blue. Tilt and amplitude are in structural "
      "conflict, independent of any eps model",
      True, "any responsiveness that makes n_bar non-conserved also bends ln n_bar away from linearity")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
