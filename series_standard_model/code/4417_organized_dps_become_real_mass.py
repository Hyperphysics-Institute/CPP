"""Patch 4417 -- founder: organized DPs (separated or arced by velocity, a current's B field, or stored charge's E field)
become 'real' (as per the amount of their separation), an extended part of the system's mass, resisting acceleration.

Part 1. Any sign-blind measure of a DP's 'realness' as a function of its separation d is even in d (4416's symmetry), so it
        starts at d^2. For a DP sea that polarizes linearly (separation proportional to the local field), d^2 goes as E^2,
        the field's energy density. Compare: realness linear in |d| (mass ~ |E|) against quadratic (mass ~ E^2), for a
        capacitor whose voltage doubles.
Part 2. A linear dielectric made of springs: the spring energy is (1/2) E.P exactly (an identity, eps_pol = n q^2/k by
        definition). In a linear dielectric u = (1/2) eps_bare E^2 + (1/2) E.P, so the spring energy is the WHOLE field
        energy only if eps_bare = 0 (D = P), a strong commitment: Gauss's law then forces complete screening.
Part 3. Sizes: the mass of the field region for a 1 uF capacitor at 1 kV, a 1 T magnet volume, and an electron's
        classical electromagnetic mass with the 4/3 factor of field-momentum inertia (Abraham-Lorentz).
"""
import numpy as np
c = 2.998e8; eps0 = 8.854e-12; mu0 = 4e-7*np.pi; e = 1.602e-19; me = 9.109e-31

print("Part 1 (capacitor voltage doubled):")
print("  realness linear in separation:    mass of field region x2  (not energy-like; the sign-blind symmetry also forbids it")
print("                                     unless realness has a kink at zero separation)")
print("  realness quadratic in separation: mass of field region x4  = stored energy C V^2 / 2 scales x4  (relativity)")

print("Part 2 (toy: DPs of charge q on springs k, density n; separation d = qE/k):")
q, k, n = 1.0, 3.0, 2.0
for E in (0.1, 0.2, 0.4):
    d = q*E/k
    spring_energy = n*0.5*k*d**2             # energy stored in separated DPs per volume
    eps_pol = n*q**2/k                       # polarizability per volume of the DP springs
    print(f"  E {E:.1f}: spring energy {spring_energy:.5f}   (1/2) eps_pol E^2 {0.5*eps_pol*E**2:.5f}")
print("  identity: spring energy = (1/2) E.P; equals the whole field energy only if eps_bare = 0 (D = P).")

print("Part 3 (sizes):")
C, V = 1e-6, 1e3
U = 0.5*C*V**2
print(f"  1 uF at 1 kV: stored energy {U:.2f} J -> extra mass {U/c**2:.1e} kg (field energy between the plates; the field's")
print("    stresses source ~2u/c^2 there and the plates' stresses cancel the surplus -- only the closed total is E/c^2)")
u = 1.0**2/(2*mu0)
print(f"  1 T over 1 litre: energy {u*1e-3:.0f} J -> extra mass {u*1e-3/c**2:.1e} kg")
a = 2.818e-15                                  # classical electron radius
Ufield = e**2/(8*np.pi*eps0*a)                 # field energy outside a charged shell of radius a
print(f"  charged shell (electron, radius {a:.3e} m): field energy/c^2 = {Ufield/c**2/me:.3f} m_e;"
      f" field-momentum inertia = (4/3) x that = {4/3*Ufield/c**2/me:.3f} m_e")
print("  4/3 from the non-covariant field momentum (Abraham, Lorentz); cures: covariant definition (Fermi 1922, Rohrlich 1960)")
print("  and, for stability, Poincare stresses (1906); Laue (1911): a closed static system has inertia exactly E/c^2.")
print("  CPP's own scalar toy (2496, demoted at 2880) gave the sea's back-reaction inertia (2/3) U_pol/c^2 for an open cloud;")
print("  CPP's realized DPs must give exactly energy/c^2 for inertia AND gravity, in every direction of acceleration.")
