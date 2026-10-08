#!/usr/bin/env python3
"""Patch 4391 -- founder: the photon crosses a sea of DPs that ZBW-oscillate; near the Sun SSV_abs slows
that oscillation; could that change the bending?  (Crystal "positions" are really forces in the DP sea.)

Part 1: an oscillator's static response goes as 1/omega0^2, so a ZBW slowed by U raises the DP sea's
        response by 2U: the square turns one U into two.
Part 2: the polarizable-vacuum (PV) bookkeeping (Dicke 1957; Puthoff, arXiv gr-qc/9909037): with the
        vacuum's dielectric factor K, light ~ 1/K, rulers ~ K^-1/2, clocks ~ K^-1/2.  Check against the
        solar-system targets (ruler 1-U, light 1-2U, clock 1-U) and against 4389's picture (b).
Part 3: K = exp(2U) gives the exponential metric = CPP's one-PSR (kappa = 0) exterior (4375).
"""
import sympy as sp
U, w0, q, m = sp.symbols('U omega0 q m', positive=True)
lin = lambda e: sp.expand(sp.series(e, U, 0, 2).removeO())
print("Part 1: oscillator response chi = q^2/(m omega0^2); slow omega0 by (1 - U):")
chi = q**2/(m*w0**2)
ratio = sp.simplify(chi.subs(w0, w0*(1-U))/chi)
print("  chi ratio =", ratio, "~", lin(ratio), " (a U slowing becomes a 2U rise in response)")
print("  Holds with the DP's charge and mass FIXED.  If DP mass scaled like PV masses (K^3/2) the response would")
print("  fall (chi ~ K^-1/2): the mass behaviour of a DP decides it.")
print("  eps alone x(1+2U): light 1/sqrt(eps*mu) slows by U only (half the bending).  Both eps and mu x(1+2U)")
print("  are needed for 2U; the magnetic part is NOT shown by this oscillator argument (assumption).")
print("  Also needs eps0 to be essentially all DP response (4384), else eps = 1 + chi rises by less than 2U.")

print("\nPart 2: PV bookkeeping with K = 1 + 2U")
K = sp.exp(2*U)
light, ruler, clock = 1/K, K**sp.Rational(-1, 2), K**sp.Rational(-1, 2)
print(f"  light {lin(light)}, ruler {lin(ruler)}, clock {lin(clock)}; local light speed "
      f"v/(ruler*clock) = {sp.simplify(light/(ruler*clock))}")
print("  targets: ruler 1 - U, light 1 - 2U, clock 1 - U  -> all met; local c constant.")
print("  This is 4389's picture (b): light (one PSR per Moment) slows twice as much as clocks, and crystals")
print("  shrink by half the PSR's fraction -- here because the forces holding them act through the same medium.")
print("  Bending 4GM/(c^2 b) and Shapiro follow from light ~ 1/K (index K = 1 + 2U).")

print("\nPart 3: metric for K = exp(2U)")
r, M = sp.symbols('r M', positive=True)
Kr = sp.exp(2*M/r)
print("  g00 = -1/K =", -1/Kr, ";  g_ij = K =", Kr)
print("  = the exponential (one-PSR, kappa = 0) exterior of 4375: beta = gamma = 1 (post-Newtonian order; g_ij")
print("  differs from isotropic Schwarzschild at U^2: 1+2U+2U^2 vs 1+2U+1.5U^2); strong field differs from")
print("  Einstein (shadow +4.6%, ringdown about -4%, 4374): the weak-field question is solved, the strong-field")
print("  one is not.")
