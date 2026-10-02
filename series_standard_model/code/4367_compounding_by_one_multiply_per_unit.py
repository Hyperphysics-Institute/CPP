#!/usr/bin/env python3
"""Patch 4367 - how a GP could execute the compounding conversion (founder, 2 Oct 2026).

The founder's picture is kept: every DI-bit adds the same amount (the census Delta is plain addition,
GR-1j's census linearity).  The only non-additive step is the CONVERSION of that sum into a PSR,
which the corpus has never specified (founder 4365).  Three ways a GP could do it:

  (i)   step by step:   start from the deep-space count n_inf and, for each unit of arrived stress,
                        keep the fraction (1 - f):  n = n_inf * (1 - f)^Delta      (one multiply per unit)
  (ii)  table:          n = T[Delta], one table shared by every GP (a design constant)
  (iii) formula:        n = n_inf * exp(-3 k Delta)

Check: for integer Delta, (i) IS an exact exponential, with 3k = -ln(1 - f).  So the "compound
interest" needs no logarithm and no table: one multiplication per arriving unit, done identically by
every GP.  Contrast: dividing by the sum (n ~ 1/(S0 + Delta), the inverse proportion) is also a
single operation, but it is the wrong curve (4365-4366).
"""
import sympy as sp
print(__doc__)

f, D = sp.symbols('f Delta', positive=True)
n_step = (1 - f)**D
k3 = -sp.log(1 - f)
print("(i) ln[(1-f)^Delta] - (-3k Delta) with 3k = -ln(1-f):",
      sp.simplify(sp.expand_log(sp.log(n_step), force=True) + k3 * D), " -> exact exponential")
print("    3k = -ln(1-f) = f + f^2/2 + ... ; for small f, 3k ~ f")

# numeric illustration on an integer census, with an illustrative f (not a calibrated value)
fv = 1e-3
n_inf = 1.0
for Dv in (0, 1, 10, 100, 1000):
    step = n_inf
    for _ in range(Dv):
        step *= (1 - fv)
    expo = n_inf * float(sp.exp(sp.log(1 - fv) * Dv))
    inv = 1.0 / (1 + fv * Dv)                     # inverse proportion with the same first-order slope
    print(f"   Delta={Dv:5d}: step-by-step {step:.10f}   exponential {expo:.10f}   inverse proportion {inv:.10f}")
print("   step-by-step = exponential to machine precision; the inverse proportion departs at second order.")

# PSR and lapse from the count
q = (n_step)**sp.Rational(1, 3)
print("\nPSR ratio q = n^(1/3) = (1-f)^(Delta/3): the PSR also shrinks by a fixed fraction per unit of stress;")
print("second-order coefficient in eps = k Delta:", sp.series(sp.exp(-sp.Symbol('eps')), sp.Symbol('eps'), 0, 3).removeO())
