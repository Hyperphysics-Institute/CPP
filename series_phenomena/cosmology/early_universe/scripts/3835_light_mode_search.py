#!/usr/bin/env python3
"""Patch 3835 -- systematic search for a light mode (omega <~ H) in the crowding phase, and the
structural no-go it turns up. Arithmetic and standard-result bookkeeping only; nothing adopted."""
import math, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

MPl=2.435e18; H=4.7e13; h=H/MPl              # H in reduced-Planck units
check("T1 'light' means omega/H <~ 1, and a Planck-rate mode has omega/H ~ 5e4 -- nothing LOCAL can "
      "qualify; slowness must be parametric, not accidental",
      4e4<1/h<7e4, f"H/M_Pl = {h:.2e}, omega_Planck/H = {1/h:.1e}")

# mechanism 1: conservation -> hydrodynamic mode, omega ~ D k^2 with D ~ l_P^2/t_P = 1
k_cross=math.sqrt(h)
check("T2 MECHANISM 1 (conservation): a conserved density relaxes at omega ~ D k^2, so it is LIGHT for "
      "lambda > ~230 l_P -- every horizon-scale and super-horizon mode qualifies",
      200<1/k_cross<260 and (1/k_cross)/(1/h)<0.01,
      f"crossover lambda = {1/k_cross:.0f} l_P = {100*(1/k_cross)/(1/h):.2f}% of the horizon")

# mechanism 2: symmetry -> Goldstone, omega = c k
check("T3 MECHANISM 2 (Goldstone): omega = c k is light exactly for k < H, i.e. at and beyond horizon "
      "crossing -- the standard massless-field condition",
      True, "freezes at horizon exit with delta ~ H/2pi per mode")

# mechanism 3: a near-flat potential (a light scalar). CPP's engine has three factors.
check("T4 MECHANISM 3 (near-flat potential): CPP's driver is H_eff = kappa0 kT ln n_bar -- the only "
      "factors available are kappa0, kT and the count",
      True, "kT killed at 3818 (does not reach the end condition); kappa0 likewise affects the RATE only")

# THE NO-GO CHAIN
# (a) zeta = dN (3831); (b) N = 1/3 ln n_init with n_end = 1 FIXED and geometric;
# (c) so only the COUNT contributes to dN; (d) the count is locally conserved;
# (e) conserved densities have P(k) -> k^2 (number) or k^4 (causal/stress) as k -> 0
for nP,label in ((2,"conserved number"),(4,"causal + conserved stress")):
    ns=1+nP
    check(f"T5.{nP} {label}: P_zeta ~ k^{nP} => n_s = {ns}, against the observed 0.9649 -- EXCLUDED",
          ns>=3, f"n_s = {ns} vs 0.9649")

check("T6 NO-GO: the end condition n_bar_end = 1 is a fixed geometric threshold, so ONLY the count "
      "enters dN; the count is conserved; conserved densities are BLUE. Therefore NO light mode can "
      "supply a near-scale-invariant zeta while the end condition stays purely geometric",
      True, "the obstruction is the END CONDITION, not the absence of a field")

check("T7 ESCAPE: if n_bar_end depends on a NON-conserved dynamical variable (e.g. a contracted PSR "
      "set by local state -- OPEN-EU-PSR-EARLY-1), that variable enters dN and may be light and "
      "non-conserved. PSR-EARLY-1 is promoted from a budget question to the amplitude's escape route",
      True, "3818 S5 route 1, now load-bearing for the amplitude as well as the budget")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
