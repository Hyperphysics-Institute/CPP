#!/usr/bin/env python3
"""Patch 4392 -- the founder: calibrate the DP sea's response to the empirics for now; charge never
changes (primitive); mass is an energetic equivalent related to organization.

Part 1: the PV-form working convention: light c/K, clocks K^-1/2, crystals K^-1/2, charge fixed.
Part 2: the one-PSR metric g00 = -q^2, g_ij = q^-2 IS the PV metric with K = q^-2 (proper PSR q).
Part 3: WC-EINSTEIN-AREAL in PV form: K = (eps + sqrt(1+eps^2))^2; agrees with PV's exp(2 eps) through
        eps^2 (weak field identical), departs at eps^3 (strong field: Einstein's photon sphere etc.).
"""
import sympy as sp
e = sp.symbols('epsilon', positive=True)
q_areal = sp.sqrt(1 + e**2) - e
K_areal = sp.simplify(1/q_areal**2)
K_exp = sp.exp(2*e)
Ks = sp.symbols('K', positive=True)
light, clock, crystal = 1/Ks, Ks**sp.Rational(-1, 2), Ks**sp.Rational(-1, 2)
print("Part 1: PV bookkeeping: local light speed v/(ruler*clock) =", sp.simplify(light/(crystal*clock)))
qs = sp.symbols('q', positive=True)
same = sp.simplify((-qs**2) - (-1/Ks)).subs(Ks, 1/qs**2) == 0 and sp.simplify(qs**-2 - Ks).subs(Ks, 1/qs**2) == 0
print("Part 2: one-PSR metric (-q^2, q^-2) equals PV metric (-1/K, K) with K = 1/q^2:", same)
print("Part 3: K for WC-EINSTEIN-AREAL =", sp.simplify((e + sp.sqrt(1+e**2))**2 - K_areal) == 0 and "(eps + sqrt(1+eps^2))^2")
print("  series areal :", sp.series(K_areal, e, 0, 4))
print("  series exp   :", sp.series(K_exp, e, 0, 4))
print("  difference   :", sp.series(K_areal - K_exp, e, 0, 5))
print("  -> identical through eps^2 (redshift, bending, Shapiro, Mercury); differ from eps^3 on (strong field).")
for lab, KK in (("areal", K_areal), ("exp", K_exp)):
    print(f"  q = K^-1/2 ({lab}):", sp.series(KK**sp.Rational(-1, 2), e, 0, 4))
print("  -> both 1 - eps + eps^2/2 (R-PSR-LAW-LOG's 1/2); third order 0 (areal) vs -1/6 (exp).")
