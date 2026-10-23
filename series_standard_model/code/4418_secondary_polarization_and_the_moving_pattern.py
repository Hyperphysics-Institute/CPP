"""Patch 4418 -- founder: realized DPs count as extra charges in creating mass; a secondary effect follows (the realized
sea polarizes and arcs the surrounding sea in turn); more separation, more realness, more secondary polarization; DPs
partner-switch, so the same DPs do not travel, but the polarized cohort stays tied to the plates and must be accelerated.

Part 1. The standard analogue of his secondary effect, for a polarizable medium sitting in a BARE vacuum (a heuristic for
        the DP sea, which under 4417's eps_bare = 0 has no bare background): each generation of polarization adds the
        Lorentz local field P/3 for the next; summed, it is the Clausius-Mossotti response to the macroscopic field.
        Doubling the macroscopic field doubles every generation, so the stored energy still grows fourfold: the cascade
        changes the coefficient, not the power.
Part 2. Convergence in that analogue: x = n alpha / 3 < 1, else the polarization catastrophe.
Part 3. The interrupted remark (DPs pulled in from the surroundings as they align): a field gradient pulls a polarizable
        medium toward stronger field with force ~ grad E^2 (dielectrophoresis / electrostriction), so the density rise is
        second order. DP number is conserved, so a redistribution adds no net mass unless DPs are created. PVLAS bounds
        only the anisotropic (birefringent) part of a field-induced index change, not an isotropic, mass-like shift.
"""
import numpy as np

print("Part 1 (local-field series in a bare background, eps_bare = 1; macroscopic field E0):")
x = 0.3                                    # n*alpha/3: each generation's polarization makes x times the field for the next
for E0 in (1.0, 2.0):
    P, gens, field = 0.0, [], E0
    for k in range(60):
        dP = 3*x*field                     # n*alpha*(field seen by this generation)
        gens.append(dP); P += dP
        field = dP/3                       # the local field this generation adds for the next (P/3)
    P_cm = 3*x*E0/(1 - x)                  # Clausius-Mossotti closed form
    print(f"  E0 {E0:.0f}: generations {gens[0]:.3f}, {gens[1]:.3f}, {gens[2]:.4f} ...  sum {P:.6f}  (closed form {P_cm:.6f})"
          f"  stored energy (1/2)E0.P {0.5*E0*P:.5f}")
print("  doubling E0 doubles every generation and quadruples the energy: the square law survives; the coefficient is")
print(f"  enhanced by 1/(1-x) = {1/(1-x):.2f}.")

print("Part 2 (convergence):")
for xx in (0.1, 0.5, 0.9, 0.99):
    print(f"  x {xx:.2f}: enhancement 1/(1-x) = {1/(1-xx):.1f}")
print("  x >= 1: no finite response (the sea would polarize spontaneously); the secondary effect must stay smaller.")

print("Part 3 (pull-in of DPs; quoted bounds and computed conversions):")
A_e = 1.32e-24; c = 2.998e8; G = 6.674e-11; mu0 = 4e-7*np.pi
print(f"  QED (quoted coefficient): n_par - 1 = 7 A_e B^2 = {7*A_e:.1e} at 1 T; PVLAS (quoted, Ejlli 2020) bounds only the")
print("  ANISOTROPIC part, delta n / B^2 = (1.9 +/- 2.7)e-23 per T^2; an isotropic index shift, as a mass-like count rise")
print("  would give, is not seen by PVLAS, and no laboratory limit near that level is quoted here.")
print(f"  1 T corresponds to E = cB = {c*1:.1e} V/m, so a capacitor at 1 MV/m is like {1e6/c:.1e} T: B^2 factor {(1e6/c)**2:.1e}")
rho = 1.0/(2*mu0)/c**2
print(f"  the field energy's own E/c^2 potential at 1 T over 1 m (as 4416 part 3; not a pull-in effect): U ~ G rho (1 m)^2 / c^2 = {G*rho/c**2:.0e} (computed)")
print("  DP-number conservation: DPs pulled in from the surroundings thin the surroundings; the integrated count change is")
print("  zero, so a redistribution adds no net gravitating mass unless DPs are created.")
