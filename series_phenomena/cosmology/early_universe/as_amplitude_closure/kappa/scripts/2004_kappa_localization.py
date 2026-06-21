#!/usr/bin/env python3
"""
R3 / derive-kappa: can the boost coupling kappa (-> A_s) be derived, or is it a
posited axiom constant? Falsification-first: locate where the smallness MUST live
and check whether CPP determines it.

Structure (corpus): H_eff = kappa*kT*ln nbar (0751 Step 4); the boost law's SHAPE
(H_eff ~ ln nbar) was derived in the n_s arc (-> tilt p=2), but its MAGNITUDE kappa
is the refined form of the brick4 H-axiom constant -- "constant by axiom, NOT
derived" (brick4_branch_v_adoption_and_toy_spec.md, item 2).
"""
import numpy as np
A_s_obs, Nstar = 2.1e-9, 57.0
# E_Pl in GeV, t_P; natural units kT_bath ~ E_Pl (LEMMA-NS-BATH, 0767)
Mpl_GeV = 2.435e18

ln_nbar_pivot = 3*Nstar                 # = 171
f_sup_pivot   = 1.0                     # superposed fraction ~1 at nbar~1e74 (almost all GPs stacked)

print("="*68); print("R3 / derive-kappa : where does the A_s smallness live?"); print("="*68)

# --- target kappa from the single-field calibration (2003) ---
eps = 1/(2*Nstar)
H_star_Mpl = np.sqrt(8*np.pi**2*eps*A_s_obs)           # H_*/Mpl
# H_eff = kappa*kT*ln nbar ; kT~E_Pl~Mpl ; so kappa ~ (H_*/Mpl)/ln nbar :
kappa_target = H_star_Mpl/ln_nbar_pivot
print(f"\nTarget: H_* = {H_star_Mpl:.2e} Mpl ; ln nbar_pivot = {ln_nbar_pivot:.0f}")
print(f"   -> kappa_target ~ {kappa_target:.2e}  (single-field calibration; order 1e-7..1e-6)")
print(f"   <-> per-Moment boost H_eff*t_P = kappa*ln nbar ~ {kappa_target*ln_nbar_pivot:.1e} at pivot")

# --- localization: the smallness is in kappa, NOT in f_sup or kT ---
print("\n[localization] A_s ~ (kappa*kT)^2 ; rule out the other factors:")
print(f"  kT  : pinned ~ E_Pl by LEMMA-NS-BATH (0767)         -> NOT the small factor")
print(f"  f_sup: at nbar~1e74 almost all GPs superposed, f_sup~{f_sup_pivot:.0f} -> NOT the small factor")
print(f"        (a small f_sup would also kill the tilt: const boost -> n_s=1 cliff, 0741)")
print(f"  => the smallness MUST sit in kappa itself (the boost COUPLING).")

# --- falsification fences: kappa is not FORCED to an excluded value ---
kappa_O1   = 1.0
As_if_O1   = A_s_obs*(kappa_O1/kappa_target)**2
kappa_pois = np.exp(-ln_nbar_pivot)     # the excluded shot-noise scale e^-171
print("\n[fences] is kappa forced to an EXCLUDED value by known structure?")
print(f"  kappa~O(1) (naive H-axiom)   -> A_s ~ {As_if_O1:.1e}  (>> obs; EXCLUDED)")
print(f"  kappa~e^-171 (Poisson)       -> A_s ~ 10^-150         (<< obs; EXCLUDED, =2003)")
print(f"  kappa~{kappa_target:.0e} (target)        -> A_s = {A_s_obs:.1e}  (obs; ALLOWED, not forced)")
print(f"  => known structure neither derives nor excludes kappa~1e-7; it is OPEN/posited.")

# --- the shape-vs-magnitude split (the clean structural statement) ---
print("\n[shape vs magnitude] what the n_s arc did and did not fix:")
print("  DERIVED  : H_eff ~ ln nbar (the boost-law SHAPE) -> tilt p=2, n_s=0.9649.")
print("  NOT FIXED: the boost-law MAGNITUDE kappa -> A_s. (kappa-orthogonality, 2003.)")
print("  The magnitude is the H-axiom constant: 'constant by axiom, NOT derived' (brick4).")

# --- honest NON-evidence note on a numeric coincidence ---
alpha = 1/137.036
print("\n[NON-evidence note, flagged not claimed]")
print(f"  kappa_target ~ {kappa_target:.1e}; alpha^3 = {alpha**3:.1e} (ratio {kappa_target/alpha**3:.2f}).")
print(f"  The order is suggestively near alpha^3 IF the per-superposition boost is")
print(f"  EM/SSV-mediated -- BUT the single-field calibration uncertainty (factor few-10)")
print(f"  EXCEEDS the alpha^3 discrepancy, so this is at most a where-to-look hint, NOT")
print(f"  evidence and NOT a derivation. Recorded so it is neither lost nor overclaimed.")

print("\n"+"="*68); print("VERDICT (derive-kappa):")
print(" kappa does NOT derive from the current corpus. It is the MAGNITUDE of the")
print(" H-engine boost law (refined H-axiom constant), carried as POSITED ('constant")
print(" by axiom, NOT derived', brick4). The n_s arc fixed the boost-law SHAPE (tilt);")
print(" the MAGNITUDE kappa (= A_s) is the orthogonal piece it could not reach.")
print(" Smallness localized to kappa (kT pinned ~E_Pl; f_sup~1). Target kappa~2e-7,")
print(" allowed but not forced. => A_s STAYS ADOPTED; parity with inflation (which")
print(" likewise posits the inflaton scale). R3 residual sharpened to ONE axiom-level")
print(" constant: derive the H-engine boost coupling kappa from A1-A11. alpha^3 flagged")
print(" as a where-to-look hint only (NOT evidence).")
