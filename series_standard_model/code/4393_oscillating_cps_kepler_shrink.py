#!/usr/bin/env python3
"""Patch 4393 -- founder: crystal "distances" are not fixed; CPs oscillate (ZBW, cage motion) about a
centre; near the Sun the oscillation is slower, and the passing photon drives the DPs more slowly; "perhaps
the two together may exert the cumulative effect".

Question: does slower oscillation make a bound inverse-square pair sit closer?  Bound motion under an
inverse-square pull obeys Kepler's rule  omega^2 * a^3 = k Q^2 / m  (a = size, omega = rate, k = the
medium's force constant, Q = charge, m = inertia).  First-order shifts near the Sun (in units of U):
  da = (dk - dm - 2 domega) / 3.
Part 1: each ingredient alone and together.
Part 2: the self-consistent PV-form family (hbar, Q fixed; m c^2 tied to the oscillation frequency, as in
        the ZBW) and what the two measurements (bending -> K = 1 + 2U; redshift -> omega 1 - U) select.
"""
import sympy as sp
U = sp.symbols('U')
def da(dk, dm, dw): return sp.Rational(1, 3)*(dk - dm - 2*dw)
print("Part 1: Kepler's rule, first-order shifts (x U)")
cases = [("oscillation slower by U only (k, m unchanged -- unphysical: omega cannot change then; shown for contrast)", 0, 0, -1),
         ("+ DP sea softer: force at a given distance weaker by 2U (the same softening that slows light 2U)", -2, 0, -1),
         ("+ inertia up by 3U (mass = energy / c_grid^2: energy down U, c_grid^2 down 4U)", -2, 3, -1)]
for lab, dk, dm, dw in cases:
    print(f"  {lab}:\n     size shift {da(dk, dm, dw)} U")
print("  -> slower alone: the pair spreads (+2/3 U, like a slower, wider orbit).  Slower + softer sea: size")
print("     unchanged (his 'A and B fixed').  Slower + softer + heavier: shrinks by U, exactly what the data need.")

print("\nPart 2: Bohr form with hbar and Q fixed, medium k ~ 1/K, mass m ~ K^mu")
K, mu = sp.symbols('K mu', positive=True)
a = 1/(K**mu * K**-1)                 # a = hbar^2/(m k Q^2)
v = K**-1                             # v = k Q^2 / hbar
w = sp.simplify(v/a)                  # orbital rate
c_grid = K**-1
print("  size a ~", sp.simplify(a), "; rate omega ~", w, "; local light speed c_grid/(a*omega) ~",
      sp.simplify(c_grid/(a*w)), "; alpha = kQ^2/(hbar c_grid) ~", sp.simplify(K**-1/c_grid))
print("  -> local light speed and alpha are constant for ANY mu; the size and rate are not.")
sol = sp.solve(sp.Eq((mu - 2)*2, -1), mu)[0]     # redshift: omega ~ K^(mu-2), K = 1+2U, omega = 1 - U
print(f"  INPUT from redshift (omega = 1 - U with K = 1 + 2U): mu = {sol}: m ~ K^{sol}, a ~ K^{1-sol}, omega ~ K^{sol-2}")
print("  -> crystals shrink by U; clocks slow by U; inertia up by 3U; energy (m c_grid^2) down by U.")
print("  The same as the polarizable-vacuum rules (Puthoff: m ~ K^3/2, lengths ~ K^-1/2, frequencies ~ K^-1/2).")

print("\nPart 3: what this really is")
m_id = sp.simplify((K**(mu-2))/(c_grid**2))      # hbar*omega/(alpha^2 c^2) with alpha const
print("  hbar*omega/c_grid^2 ~", m_id, "= m for every mu: 'mass = energy/c^2' adds no constraint.")
print("  size a ~ c_grid/omega (local light speed constant): c_grid down 2U (bending), omega down U (redshift)")
print("  -> a down U.  The shrink = redshift + bending + local light-speed invariance; Kepler adds no new input.")
print("  Masses here are far-away (grid) bookkeeping; a locally measured mass is unchanged.")
