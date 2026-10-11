#!/usr/bin/env python3
"""Patch 4397 -- founder: the PSR is smallest toward the Sun and grows with the angle to a maximum 180 degrees away.

Part 1: why the first-order fore-aft term is an end-point term, and why that stops at first order:
        1/PSR = 1 + a c + (b + a^2) c^2 + ... (c = cos theta): a^2 acts as an extra b.
Part 2: the decisive case -- a ROUND sphere, unchanged in shape, shifted away from the Sun by beta:
        reach d(theta) = -beta cos(theta) + sqrt(1 - beta^2 sin^2(theta))  (toward 1-beta, away 1+beta, across sqrt(1-beta^2)).
        Compare with the light cone of Schwarzschild in Painleve-Gullstrand ('river') form with river speed beta.
Part 3: with beta^2 = 2u (u = m/r on the flat grid): clocks, rulers, round-trip light, floor, horizon.
"""
import numpy as np, sympy as sp
th, beta, v, u = sp.symbols('theta beta v u', positive=True)
a, b, c = sp.symbols('a b c')
print("Part 1:", "1/(1 - a c - b c^2) =", sp.series(1/(1 - a*c - b*c**2), c, 0, 3).removeO())
print("  the a*c term integrates to an end-point term; the (b + a^2) c^2 term bends light: b_eff = b + a^2.")
print("  So a large shift (a ~ sqrt(U)) is NOT invisible: its square acts at first order in U.\n")

print("Part 2: round sphere shifted by beta away from the Sun")
d = -beta*sp.cos(th) + sp.sqrt(1 - beta**2*sp.sin(th)**2)
print("  toward:", sp.simplify(d.subs(th, 0)), " away:", sp.simplify(d.subs(th, sp.pi)), " across:", sp.simplify(d.subs(th, sp.pi/2)))
# PG (outflow river, speed v): ds^2 = -dT^2 + (dr - v dT)^2 + r^2 dOmega^2.  Null speed s along direction with radial
# component cos(alpha) (alpha from outward):  (s cos a - v)^2 + s^2 sin^2 a = 1.
al = sp.symbols('alpha')
s = sp.symbols('s', positive=True)
s_pg = sp.solve(sp.Eq((s*sp.cos(al) - v)**2 + (s*sp.sin(al))**2, 1), s)
s_pg = [x for x in s_pg if x.subs({v: 0.3, al: 0.4}).is_positive][0]
# toward-Sun angle theta = pi - alpha
ok = all(abs(float((s_pg.subs(al, sp.pi - tv) - d.subs(th, tv)).subs({v: bv, beta: bv}))) < 1e-12
         for bv in (0.1, 0.5, 0.86) for tv in (0.0, 0.7, 1.6, 2.5, 3.1))
print("  shifted-sphere reach = Painleve-Gullstrand null speed with river speed beta, at every angle tested:", ok)
print("  (the light cone in the river form is a unit sphere centred on the river velocity -- Hamilton & Lisle 2008)\n")

print("Part 3: beta^2 = 2u, the squared speed of a body falling from far away, in units of c")
bsq = 2*u
clock = sp.sqrt(1 - bsq)
print("  static clock (Lorentz factor of the fall speed): sqrt(1 - 2u) =", sp.series(clock, u, 0, 2).removeO())
print("  radial ruler: Lorentz-contracted by sqrt(1 - 2u); sideways ruler unchanged")
rt = sp.simplify(2/(1/(1 - sp.sqrt(bsq)) + 1/(1 + sp.sqrt(bsq))))
print("  round-trip radial light speed (harmonic mean of 1-beta, 1+beta):", rt, " = 1 - 2u: Schwarzschild's radial value")
print("  across:", sp.simplify(d.subs(th, sp.pi/2)).subs(beta, sp.sqrt(bsq)), " = Schwarzschild's tangential value")
floor = sp.solve(sp.Eq(sp.sqrt(1 - bsq), sp.Rational(1, 2)), u)
print("  floor (across reach = 1/2): u =", floor, "-> r = 8m/3; beta there =", sp.sqrt(bsq).subs(u, floor[0]))
print("  horizon (beta = 1): u = 1/2, r = 2m -- inside the floor.")
print("  sign: shortest TOWARD the mass (his) = outflowing river; shortest AWAY = inflowing river (the usual black-hole")
print("  river).  Identical for every static measurement outside the horizon; they differ only at a horizon.")
