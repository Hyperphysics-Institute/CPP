#!/usr/bin/env python3
"""Patch 4365 - the founder's proposal (1 Oct 2026): compute the PSR from SSV_abs through the
number of GPs enclosed in the Planck sphere (radius = the local PSR) for that SSV_abs.

n(Delta) = GPs inside the PSR ball; q = PSR/PSR_inf = (n/n_inf)^(1/3); eps = k*Delta (GR-1 L284).
Two natural readings of "correlate":
  (A) proportional:  n ~ 1/SSV_abs = 1/(S0 + Delta)           (the count falls as stress rises)
  (B) compounding:   n = n_inf * exp(-3 k Delta)              (each equal step of added stress
                                                               removes the same FRACTION of GPs;
                                                               Claude's reading, not the founder's)
Checks: the PSR law each gives, against the ratified R-PSR-LAW-LOG (1 - eps + eps^2/2, Mercury);
the background dependence of the local field (d ln q / dDelta); the uniqueness of (B) under
local invariance; the black-hole floor; numbers.
"""
import sympy as sp

D, k, S0, e, e0, de = sp.symbols('Delta k S0 epsilon epsilon0 deps', positive=True)
print(__doc__)

ratified = 1 - e + e**2 / 2
print("Ratified (3390):            q = 1 - eps + eps^2/2 + O(eps^3);  GR isotropic third order: -1/4 (3390 note)")

# (A) proportional: q^3 = S0/(S0+Delta); first order matches only if k*S0 = 1/3 (4360's condition)
qA = (S0 / (S0 + D))**sp.Rational(1, 3)
qA_e = sp.series(qA.subs(D, 3 * S0 * e), e, 0, 4).removeO()      # k*S0 = 1/3  => Delta = 3*S0*eps
print("(A) n ~ 1/SSV_abs, k*S0=1/3: q =", sp.expand(qA_e), "  -> second order 2 (beta = 5/2): Mercury fails (= 4360/4361)")

# (B) compounding
qB = sp.exp(-k * D)
qB_e = sp.series(sp.exp(-e), e, 0, 4).removeO()
print("(B) n = n_inf exp(-3 k Delta): q =", sp.expand(qB_e), "  -> second order 1/2 = Mercury's, now a consequence")
print("    third order -1/6 (GR isotropic -1/4): a strong-field difference, open in the corpus since 3390")

# background dependence of the local field: d ln q / d Delta at background Delta0
print("\nLocal field strength per unit census, relative to deep space (G_loc and, by one rule, alpha):")
for name, q in (("truncated polynomial", ratified.subs(e, k * D)), ("(A) proportional", qA.subs(S0, 1 / (3 * k))),
                ("(B) compounding", qB)):
    s = sp.simplify(sp.diff(sp.log(q), D) / (-k))
    ser = sp.series(s.subs(D, e0 / k), e0, 0, 3).removeO()
    print(f"   {name:22s}: {sp.expand(ser)}")
print("   (A) depends on the background at FIRST order under the 4364 source rule, even with k*S0 = 1/3.")
print("   -> (B) is the only one with NO dependence on the background: the absolute stress (Sun, Galaxy,")
print("      cosmology) scales out exactly (for G; for alpha if its reading is metric-coupled, 4364 sec 2).")

# uniqueness: local invariance demands the fractional response of the count to added stress be
# the same in every background:  d ln n / d Delta = constant
n = sp.Function('n')
c = sp.Symbol('c', positive=True)
sol = sp.dsolve(sp.Eq(sp.diff(n(D), D) / n(D), -3 * c), n(D))
print("\nUniqueness: d ln n/dDelta = -3c (same fraction per unit stress in every background) =>", sol)
print("   GIVEN the pure-count source rule (injection ~ n_s), within CPP's linear census and the gather")
print("   kernel, local invariance forces (B), and (B)'s second order is Mercury's 1/2: two open choices")
print("   (source rule, PSR law) become one. Not unique in general: a source rule ~ R_s^3/|dlnq/dDelta|_s")
print("   would make any law invariant; and GR keeps local invariance with a non-exponential lapse (4365 critic).")

# the source rule in the same terms
print("\nThe 4364 source rule in these terms: injection per Moment ~ R_s^3 ~ n_s, the SAME number the GP")
print("uses to set its PSR. One computed quantity, the GP count of the Planck sphere, sets rulers, clocks")
print("and how strongly a resident CP stamps its DI-bits.")

# the ratified law's open third order: the residual is set by it, not by the truncation
g3 = sp.Symbol('gamma3')
qg = 1 - e + e**2 / 2 + g3 * e**3
resg = sp.series(sp.diff(sp.log(qg), e).subs(e, e0) / (-1), e0, 0, 3).removeO()
print("\nRatified law with its open third order gamma3 (3390 left it open):")
print("   background factor =", sp.expand(resg), " -> zero only for gamma3 = -1/6 (B);")
print("   GR-1c's Pade/Schwarzschild lapse (gamma3 = -1/4) gives", sp.expand(resg.subs(g3, sp.Rational(-1, 4))),
      "; the truncated polynomial (gamma3 = 0) gives", sp.expand(resg.subs(g3, 0)), "(4364 section 2 assumed this)")

# strong field: (B) with rulers = clocks (g_ij = q^-2 delta) is the exponential metric
m, r = sp.symbols('m r', positive=True)
lapse = sp.exp(-m / r)
areal = r * sp.exp(m / r)
b_crit = areal / lapse                                  # impact parameter b = areal radius / lapse
r_ph = sp.solve(sp.diff(b_crit, r), r)[0]
print("\nStrong field under (B) with one PSR for rulers and clocks (exponential metric):")
print(f"   photon sphere: isotropic r = {r_ph}, areal radius = {sp.N(areal.subs(r, r_ph)/m, 5)} m  (GR: 3 m)")
bB, bGR = sp.N(b_crit.subs(r, r_ph) / m, 6), sp.N(3 * sp.sqrt(3), 6)
print(f"   shadow (critical impact parameter) = {bB} m  vs GR 3*sqrt(3) = {bGR} m  ->  {sp.N(100*(bB/bGR-1), 3)}% larger")
print("   no horizon (lapse > 0 for all r); 4365 critic: EHT's Sgr A*/M87* shadow sizes agree with GR at the ~10% level,")
print("   so this is not excluded today, but it is testable.")

# numbers
Usun, Ugal = 9.87e-9, 1.0e-6
dU = 2 * 0.0167 * Usun
bound = 1.2e-17
print("\nAnnual swing of the local coupling at Earth (bound 1.2e-17):")
for name, e0v in (("eps0 = U_sun", Usun), ("eps0 = U_gal", Ugal)):
    print(f"   {name}: truncated poly eps0*deps = {e0v*dU:.1e} ({e0v*dU/bound:.2f}x); Pade eps0*deps/2 = {e0v*dU/2:.1e}; (B) 0;"
          f"  (A) 3*deps = {3*dU:.1e} ({3*dU/bound:.0e}x, first order)")
