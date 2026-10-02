#!/usr/bin/env python3
"""Patch 4366 - what would make the founder's inverse proportion (GP count of the Planck sphere
proportional to 1/SSV_abs) work?  (Founder, 2 Oct 2026, answering 4365 section 2.)

n = GPs in the PSR ball, q = PSR/PSR_inf = (n/n_inf)^(1/3); Delta = the linear, harmonic census
(GR-1j L193-221); eps = k*Delta.  GR-1j writes SSV_abs = SSV_abs,0 + Delta (additive).

  1. Inverse proportion to an ADDITIVE SSV_abs, any power m:  n ~ (S0 + Delta)^(-m).
     Second order and background dependence as functions of c = m/3; bounds from Mercury and clocks.
  2. Inverse proportion to a COMPOUNDING SSV_abs:  SSV_abs = S0 * exp(3 k Delta)  (each arrival of
     stress raises the register by a fixed fraction of what is already there).  n ~ 1/SSV_abs is then
     exactly the 4365 compounding law, for ANY S0: 4360's condition k*SSV_abs,0 = 1/3 disappears.
"""
import sympy as sp
print(__doc__)

D, k, S0, e, e0, c = sp.symbols('Delta k S0 epsilon epsilon0 c', positive=True)

# 1. additive SSV_abs, power law: q = (1 + Delta/S0)^(-c); first order fixes c/S0 = k
x = sp.Symbol('x', positive=True)
q1 = (1 + e / c)**(-c)                     # eps = c*x = k*Delta  (first order matched)
ser = sp.series(q1, e, 0, 3).removeO()
coef2 = sp.simplify(ser.coeff(e, 2))
print("1. q = (1 + eps/c)^(-c) =", sp.expand(ser), " -> second-order coefficient", coef2, "(Mercury needs 1/2)")
bg = sp.simplify(sp.diff(sp.log(q1), e).subs(e, e0) / (-1))
print("   local field factor in a background eps0:", bg, " -> first-order dependence eps0/c")
beta_tol = 1e-4                            # |beta - 1| (planetary ephemerides / perihelia), order of magnitude
dU = 2 * 0.0167 * 9.87e-9                  # annual peak-to-peak potential change at Earth
bound = 1.2e-17                            # clock bound used in this arc (Lange 2021, 4352)
print(f"   Mercury: coefficient - 1/2 = 1/(2c) <= ~{beta_tol:g}  ->  c >= {1/(2*beta_tol):.0f}")
print(f"   clocks:  annual swing dU/c <= {bound:g}             ->  c >= {dU/bound:.1e}")
print("   c = 1/3 (m = 1, the plain inverse proportion) gives coefficient 2 (beta = 5/2) and swing 3 dU.")
print("   As c -> infinity, (1 + eps/c)^(-c) -> exp(-eps): the power law only works in the limit where it IS compounding.")
print("   limit check:", sp.limit(q1, c, sp.oo))

# 2. compounding SSV_abs
SSV = S0 * sp.exp(3 * k * D)
q2 = (S0 / SSV)**sp.Rational(1, 3)
print("\n2. SSV_abs = S0 exp(3 k Delta), n ~ 1/SSV_abs  ->  q =", sp.simplify(q2), "  (no S0: any background value works)")
print("   count x SSV_abs = constant holds EXACTLY (4360's 'PSR^3 x SSV_abs constant'), and the second order is 1/2.")
print("   What changes: SSV_abs is no longer the additive census; the additive, harmonic quantity is")
print("   Delta = ln(SSV_abs/S0)/(3k).  Predictions are identical to 4365's compounding count (same q(Delta)).")
print("   Unchanged: the 4364 source rule (injection ~ n_s) is still needed; the third order (-1/6) and the")
print("   4.6% larger shadow (4365) come with it.")
