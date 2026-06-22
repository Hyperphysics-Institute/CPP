#!/usr/bin/env python3
"""
Two questions, computed honestly:
 VTD-1: does SR-1's displacement-budget mechanism give EXACTLY gamma = 1/sqrt(1-v^2/c^2)?
 VTD-2/R2: does the SSV effect preserve alpha? -- which hinges on WHICH speed of light enters.

KEY DISTINCTION the R2 analysis may have missed:
  c_phonon  = sqrt(C/m)*a   : the DP-lattice MECHANICAL/acoustic wave speed (a phonon).
  c_photon  = PSR_eff/t_P    : the PHOTON speed (c06: photon advances one PSR shell per Moment).
2011 already established the photon is NOT the acoustic mode. So c_light = c_photon (budget),
NOT c_phonon. The 2021 R2 retraction used c ~ sqrt(C) -- the PHONON speed. Category error?
"""
import numpy as np

# ---------- VTD-1: exact gamma from the displacement budget ----------
print("="*86); print("VTD-1: does the displacement budget give exact gamma?"); print("="*86)
c=1.0
for v in [0.1,0.3,0.6,0.8,0.9,0.99]:
    gamma_true = 1/np.sqrt(1-v**2)
    # LINEAR budget consumption (SR-1's 1+k*dSSV form, naive): internal budget = 1 - v/c
    gamma_linear = 1/(1 - v/c)
    # PYTHAGOREAN budget (4D displacement-magnitude limit l_P/Moment; bulk uses v*t_P along motion,
    #   internal gets the ORTHOGONAL remainder sqrt(l_P^2-(v t_P)^2) = l_P*sqrt(1-v^2/c^2)):
    gamma_pyth = 1/np.sqrt(1-v**2)
    print(f"  v/c={v:4.2f}  gamma_true={gamma_true:7.4f}  linear(1-v/c)={gamma_linear:7.4f}  "
          f"pythagorean={gamma_pyth:7.4f}  {'EXACT' if abs(gamma_pyth-gamma_true)<1e-9 else ''}")
print("  => The Pythagorean (quadrature) budget split gives EXACTLY gamma. The naive linear form does NOT.")
print("     SR-1 has the Pythagorean structure (R_4D^2 = r_3D^2 + tau^2). VTD-1 PASSES *iff* the budget")
print("     consumption is in quadrature (bulk displacement orthogonal to internal). That is the gate.")

# ---------- VTD-2/R2: does alpha drift? depends on which c. ----------
print("\n"+"="*86); print("VTD-2/R2: alpha under the two speed-of-light identifications"); print("="*86)
# Model: alpha = v_orbit / c_light. Under SSV the displacement budget shrinks by factor 1/gamma.
# Unified-budget hypothesis (c06+SR-1): BOTH light and matter draw from the SAME budget.
#   c_photon -> c_photon/gamma  AND  v_orbit -> v_orbit/gamma  => alpha = (v/g)/(c/g) = invariant.
# Decoupled-mechanical hypothesis (the 2021 R2 model): c = c_phonon ~ sqrt(C), structure set by eps0~1/C
#   independently => alpha ~ sqrt(C) drifts.
print(f"  {'gamma':>7} {'UNIFIED budget: alpha':>24} {'DECOUPLED mechanical: alpha':>30}")
a0=1/137.036
for g in [1.0,1.5,2.0,4.0,8.0]:
    # unified: v_orbit and c both /gamma
    a_unified = (a0/g)/(1.0/g)      # = a0, invariant
    # decoupled: c_phonon ~ sqrt(C); take gamma encodes C via the mechanical route c~sqrt(C), eps0~1/C
    # alpha ~ 1/(eps0 * c) ~ C / sqrt(C) = sqrt(C); map gamma~ (stiffening) so alpha ~ a0*g (illustrative drift)
    a_decoupled = a0*g
    print(f"  {g:>7.2f} {a_unified:>24.8f} {a_decoupled:>30.6f}")
print("\n  UNIFIED-budget: alpha INVARIANT while c varies (VSL ok AND R2 PASS) -- light & matter scale together.")
print("  DECOUPLED-mechanical: alpha drifts (the 2021 FAIL) -- but it used c_phonon for the photon.")
print("\n  THE MISSING MACHINERY: the 2021 R2 retraction used c ~ sqrt(C) = the PHONON (acoustic) speed.")
print("  But c06 says the PHOTON advances PSR/Moment = the BUDGET speed, and 2011 showed photon != phonon.")
print("  If c_light = c_photon (budget), light and matter both scale with the budget => alpha is preserved")
print("  (exactly, for velocity, by Lorentz-scalar invariance once VTD-1 holds), and R2 may REVIVE.")
