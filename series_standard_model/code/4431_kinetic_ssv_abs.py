"""Patch 4431 -- founder: near light speed, ever more DPs near the electron and its cloud gain arc-separation and become real;
the effective SSV_abs rises without limit as v -> c. Proposed as the equivalence of kinetic and gravitational SSV_abs.

Part 1. What the mass shell (4425) requires of the realized charge: total S = gamma M, net V = gamma M v, so the realized
        increase over rest is (gamma - 1) M -- unbounded as v -> c, as he says, and EXACTLY that amount.
Part 2. Dilution (4425 condition 1, 4430): f = V / (S_own + S_other). Realized-only removes the resting sea's paired DPs
        (S_sea = 0 by construction, so f = v is not a result), but NOT the realized CPs of nearby matter, which must count
        (they source gravity): S_other = S_matter brings the dilution back. The step needs S to be the CP's own share.
Part 3. Why the equivalence with a static mass must be partial: if a fast electron's realized SSV_abs acted like a static mass
        gamma m_e (all-round PSR shrinking, spherical pull), it would reach the Planck energy, gamma m_e c^2 = E_P, at
        gamma ~ 2.4e22; nothing about the electron changes in its own frame (relativity principle), and its gravity is the
        flattened, boosted field, not a static sphere of mass gamma m_e.
"""
import numpy as np
M = 1.0
print("Part 1 (realized charge required, in units of the rest value M):")
for v in (0.1, 0.6, 0.9, 0.99, 0.9999):
    g = 1/np.sqrt(1 - v**2)
    print(f"  v {v}: total S = {g*M:9.3f}  realized increase (gamma - 1) M = {(g-1)*M:9.3f}  net V = {g*M*v:9.3f}")
print("Part 2 (step f = V / (S_own + S_other), v = 0.6, S_own = gamma M):")
v = 0.6; g = 1/np.sqrt(1 - v**2)
for label, so in (("resting sea, paired DPs counted fully, 1 M", 1.0), ("realized-only: sea share 0 (by construction)", 0.0),
                  ("realized-only, nearby matter's realized CPs 1 M", 1.0), ("realized-only, nearby matter 10 M", 10.0)):
    print(f"  {label:50s}: f = {g*M*v/(g*M + so):.4f}   (should be {v})")
print("Part 3:")
me_c2_GeV = 0.000511; EP_GeV = 1.22e19
print(f"  gamma at which gamma m_e c^2 reaches the Planck energy: {EP_GeV/me_c2_GeV:.1e}")
print("  (highest-energy cosmic-ray protons reach gamma ~ 3e11; electrons in accelerators ~ 2e5)")
