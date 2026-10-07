#!/usr/bin/env python3
"""Patch 4386 -- founder (correcting 4385): CP spacings in crystals and particle cages are fixed in
ABSOLUTE distance (the 1/r^2 law is in absolute distance); light advances one PSR per Moment, so
in absolute distance it is slower where the PSR is smaller; clocks take more Moments per
oscillation; absolute time (the Moment) never slows.

Part 1: the weak-field metric this implies, and its PPN gamma.
Part 2: light bending at the solar limb and the Shapiro coefficient vs measurement.
Part 3: the readings that pass (rulers in PSR units, 4385; 3386's proper-step reading).
Part 4: once-counting and the static census (shell theorem): the thicker shell cannot change it.
"""
import sympy as sp
U, a, b = sp.symbols('U a b', positive=True)

print("Part 1: rulers absolute (g_ij = 1), light speed = PSR per Moment = q in absolute units,")
print("        clock period = PSR-hops across a cage of fixed absolute size -> clock rate = q.")
print("  q = PSR/l_P = 1 - a*U (a sets the PSR law's strength; U = GM/(r c^2)).")
q = 1 - a*U
g00 = -q**2
print("  g00 = -(1 - a U)^2 ~ -(1 - 2aU)  -> Newtonian potential and redshift: a*U")
print("  g_ij = delta (no U term) -> PPN gamma = 0")
print("  Light: coordinate speed q, refractive index n = 1/q ~ 1 + aU.")

print("\nPart 2: analytic comparison with the measured values (redshift fixes a = 1: Gravity Probe A, GPS)")
GR = sp.Rational(4)          # GR deflection 4GM/(c^2 b) = 4U(b); index n = 1 + 2U
for lab, aval in (("a = 1 (redshift right)", 1), ("a = 2 (bending right)", 2)):
    defl = 2*aval              # deflection of a ray in index 1 + aU: 2a GM/(c^2 b)
    print(f"  {lab}: redshift {aval}xGR, deflection {defl}/4 of GR "
          f"({defl/4*1.7505:.3f} arcsec at the solar limb vs 1.7505 measured), Shapiro {aval}/2 of GR")
print("  Measured: VLBI deflection gives gamma to ~1e-4; Cassini Shapiro gamma = 1 + (2.1 +/- 2.3)e-5.")
print("  -> with rulers absolute, clock rate and light speed are locked together (both = PSR per Moment),")
print("     so redshift and light bending cannot both be right: one is off by a factor 2.")

print("\nPart 2b: the general statement.  With rulers fixed in absolute distance, the two measured facts")
print("  (clock rate 1 - U, coordinate light speed 1 - 2U) give a LOCALLY measured light speed")
print("  c_loc = (1 - 2U)/(1 - U) ~ 1 - U: lower near a mass.  Only gamma = 0 (light = clock rate) keeps")
print("  c_loc fixed, and gamma = 0 fails the light tests.  So absolute rulers force one of:")
print("   gamma = 0 (excluded), or a potential-dependent local light speed (LPI for light).")
dU = 2*0.0167*9.87e-9
print(f"  Earth's orbit: U_sun swings by ~{dU:.1e} a year, so an optical cavity (length set by a crystal)")
print("  against an atomic clock would swing by that much; cavity-vs-clock LPI tests bound such swings")
print("  to a small fraction of it (published bounds to be checked).")
print("  Clock branch: clocks slowing as sqrt(q) with a = 2 gives redshift U and light delay 2U")
print("  (precedent for a clock law apart from the PSR: 4373, 4379-4380); it is this LPI branch.")

print("\nPart 3: readings that pass the weak field")
print("  (i) rulers in PSR units (4385): g_ij = q^-2 delta -> gamma = 1, redshift a = 1. Passes.")
print("  (ii) 3386 (reading, unratified): one PSR per Moment with the lattice step's proper length")
print("       psi^2 l_P -> hop per Moment 1/((1+u) psi^2) ~ 1 - 2u while clocks run 1 - u. Passes.")
print("  Both need the light path, measured by the physics, to be longer near the mass than in")
print("  absolute grid distance (GR-1i L575-577: 'half of n - 1 from the compressed spatial lattice').")

print("\nPart 4: once-counting and the static census")
print("  Every GP writes fresh DI-bits each Moment from its local CP and the arrivals; nothing is")
print("  re-sent, only the summed effect propagates (founder 4386).  For a STATIC source the census")
print("  at each GP is the linear relay of the source.  A harmonic u = C/r equals its own average over ANY")
print("  centred, isotropic kernel of any thickness (mean-value property; GR-1j T-2; 4371 part 1), and")
print("  the PSR-gradient skew of the kernel is O(l_P/r).  Counting once makes the relay linear;")
print("  the mean-value property is why thickness does not matter.")
print("  So earlier delivery through a thicker shell changes transients, not the static census.")
print("  The thick shell can change the PSR only through the conversion SSV_abs -> PSR itself.")
