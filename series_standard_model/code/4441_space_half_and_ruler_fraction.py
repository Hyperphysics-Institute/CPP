"""Patch 4441 -- founder: near light speed the sea's DP arc-separation mixes with the electron's polarized cloud, keeping the
connected-force integrity; gravity bends the whole energy-cohort mass.  This is 4440's Path 1.

Part 1. ARITHMETIC combining the assumed pieces (a consistency check, not a derivation). Path 1 in full (4440): force E g every Moment, 4424 inertia (gamma m across, gamma^3 m along), speed following c/K,
        turning by the space half.  Totals equal GR.
Part 2. The space half depends on how much rulers (the PSR) shrink near a mass compared with how much clocks slow.
        Write the ruler factor as B = 1 + 2 gamma_ppn U (gamma_ppn = 1 in GR and in WC-DP-SEA-PV's K = 1 + 2U, 4392).
        Then across (1 + gamma_ppn v^2) g, along [1 - (2 + gamma_ppn) v^2] g, light's bending (1 + gamma_ppn)/2 of GR's.
        Bounds: Cassini Shapiro delay |gamma_ppn - 1| ~ 2e-5; VLBI deflection ~ 1e-4.
"""
import numpy as np
print("Part 1 (Path 1, toward the mass, / g):")
for v in (0.0, 0.5, 0.9, 0.99):
    g = 1/np.sqrt(1 - v**2)
    across = (g)/(g) + v**2                 # E g over gamma m, plus space-half turning
    along = (g)/(g**3) - 2*v**2             # E g over gamma^3 m, plus speed following c/K
    print(f"  v {v}: across {across:.3f} (GR {1+v**2:.3f})   along {along:+.3f} (GR {1-3*v**2:+.3f})")
print("  light (v = 1, across): push 1 + space half 1 = 2 (its full bending)")
print("Part 2 (ruler shrink as a fraction gamma_ppn of the clock slowing):")
for gp in (0.0, 0.5, 1.0, 1.5):
    print(f"  gamma_ppn {gp}: fast electron at 0.9c across {1 + gp*0.81:.3f} (GR 1.810), along {1 - (2+gp)*0.81:+.3f} (GR -1.430);"
          f" light's bending {(1+gp)/2:.3f} x GR" + ("   <- GR" if gp == 1.0 else ""))
