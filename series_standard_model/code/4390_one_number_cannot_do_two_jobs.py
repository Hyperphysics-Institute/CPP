#!/usr/bin/env python3
"""Patch 4390 -- founder: picture (b) (one PSR per Moment), with A and B FIXED on the GP lattice (crystal
spacing set by the inverse-square fall-off of a CP's DI-bit concentration in absolute distance); the
absolute clock never slows; clocks appear slow because crossing A-B takes more Moments.

Part 1: with A, B fixed and light one PSR per Moment, ONE number (the PSR ratio p) sets both the clock rate
        (crossings per Moment ~ p) and light's speed on the grid (p).  The data need light to slow twice
        as much as clocks.  Show what each tuning gives.
Part 2: what (b) needs instead: the crystal spacing d ~ p^(1/2).
Part 3: Claude's suggestion (not on file): an inverse-square balance gives d ~ p^(1/2) if the
        quantity held fixed at the balance point is counted per Planck-sphere LENGTH; per grid point gives
        d fixed; per Planck-sphere cross-section gives d ~ p.
"""
import numpy as np
GM_c2, Rsun, AU = 1476.6, 6.957e8, 1.496e11
rad2as = 206264.806
U_surf = GM_c2/Rsun
GM_earth_c2 = 4.435e-3; R_earth = 6.371e6; r_gps = 2.6561e7
GPS_grav = GM_earth_c2*(1/R_earth - 1/r_gps)*86400*1e6   # microseconds/day, GR gravitational part
print("Part 1: A, B fixed; light one PSR per Moment; PSR ratio p = 1 - kU")
for k, lab in ((1, "tuned to clocks (k = 1)"), (2, "tuned to light bending (k = 2)")):
    bend = 2*k*GM_c2/Rsun*rad2as
    print(f"  {lab}: clock slowing at the Sun's surface {k*U_surf:.2e} (GR value {U_surf:.2e}; solar observations agree to a few %);"
          f" bending {bend:.3f}\" (measured 1.751\"); GPS gravitational offset {k*GPS_grav:.1f} us/day"
          f" (needed {GPS_grav:.1f})")
print("  -> one number cannot fit both: clocks and light both go as p, the data need light at p^2.")
print(f"     (Gravity Probe A: clock effect confirmed to ~7e-5; GPS drift with k = 2: {GPS_grav*1e-6*2.998e8/1e3:.1f} km/day)")
print("  Redshift cannot escape: in a static field a photon's frequency in Moments is conserved, so the received")
print("  ratio is the emitter's rate in Moments.  The one escape is a clock that is not a light-speed crossing")
print("  (4388 row 5: CP motion ~ sqrt(p)); but a light clock (cavity between fixed A and B) still runs as p, so")
print("  cavity-vs-atomic comparisons over the annual solar-potential swing (~3.3e-10) would see it.")

print("\nPart 2: picture (b) as stated in 4389: PSR p = 1 - 2U, light p per Moment, crystal d, clock p/d.")
print("  clock = 1 - U needs d = p^(1/2) ~ 1 - U: A and B must move closer on the grid by U.")

print("\nPart 3 (Claude's suggestion): where does an inverse-square balance put CP_B?")
print("  CP_A's DI-bit concentration falls as 1/d^2 in absolute distance.  If CP_B settles where the amount")
print("  it senses reaches a fixed level, the answer depends on what it senses:")
import sympy as sp
pp, d, n = sp.symbols('p d n', positive=True)
for lab, nval in (("per grid point", 0), ("per Planck-sphere length", 1), ("per Planck-sphere cross-section", 2),
                  ("per Planck-sphere volume", 3)):
    sol = sp.solve(sp.Eq(pp**nval/d**2, 1), d)[0]          # sensed amount p^n/d^2 held fixed
    expo = sp.simplify(sp.expand_log(sp.log(sol), force=True)/sp.log(pp)) if nval else 0
    clock = 1 - sp.Rational(expo)
    tag = "   (b) WORKS (chosen to fit)" if nval == 1 else ("   clocks SPEED UP" if clock < 0 else "")
    print(f"   {lab:34s} d ~ p^{expo}  -> clock ~ p^{clock}{tag}")
print("  The family p^n/d^2 gives d ~ p^(n/2): any exponent is available; 'per length' is the one that fits.")
print("  d ~ sqrt(p) ~ 1 - U is GR's isotropic spatial factor.")
print("  'Per grid point' is his current thesis (A, B fixed) and gives clock = light: the failing case.")
