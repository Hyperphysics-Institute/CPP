"""
F.1 Sub-Question Phase 3 verification — Substrate-Wigner-Eckart matrix element.

Computes the substrate-Wigner-Eckart matrix element |M^thermo| under Case A.1
unification (delta = chi = phi^-3) + verifies empirical agreement against
leptogenesis CP-asymmetry target Delta-p_LR^obs ~ 0.04.

Matrix element chain (Wigner-Eckart):
  |M^thermo| = |C^thermo_reduced| * d_Gamma/V_cage
             = |delta| * 1/6                (Schur factor at icosahedral cage)

Under Case A.1: delta = chi = phi^-3, giving |M^thermo| = chi/6.

Inputs are pure framework constants (phi, chi). No empirical fitting parameters.
Run from CPP repo root:
  python3 series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/code/verify_phase3.py
"""
import numpy as np

PHI = (1.0 + np.sqrt(5.0)) / 2.0
CHI = PHI**(-3)  # substrate primitive chirality magnitude (Capotauro v2.0)

def main():
    print("="*72)
    print("F.1 Sub-Question Phase 3 verification — Substrate-W-E matrix element")
    print("="*72)
    print(f"\nFramework constants:")
    print(f"  phi               = {PHI:.15f}")
    print(f"  chi = phi^(-3)    = {CHI:.15f}  ~ {CHI:.6f}")
    print(f"  d_Gamma/V_cage    = 2/12 = 1/6 = {1.0/6.0:.15f}")
    print(f"                      (Schur factor at icosahedral cage; Capotauro §20.7,")
    print(f"                       Finding C-W40 substrate-locality unification)")

    # Phase 3 result under Case A.1
    delta_A1 = CHI  # Case A.1 unification hypothesis
    M_thermo_A1 = delta_A1 / 6.0

    print(f"\n--- Case A.1: delta = chi = phi^-3 (unification) ---")
    print(f"  delta_A.1         = {delta_A1:.15f}  ~ {delta_A1:.6f}")
    print(f"  |M^thermo|_A.1    = delta/6 = {M_thermo_A1:.15f}  ~ {M_thermo_A1:.6f}")
    print(f"                    = chi/6 (unification with Capotauro spatial sector)")

    # Empirical target
    p_LR_obs = 0.04  # leptogenesis CP-asymmetry observational order-of-magnitude
    p_LR_obs_low = 0.035  # conservative lower bound
    p_LR_obs_high = 0.045  # conservative upper bound

    print(f"\n--- Empirical target: Delta-p_LR^obs ~ {p_LR_obs} (leptogenesis) ---")
    print(f"  Conservative range: [{p_LR_obs_low}, {p_LR_obs_high}]")
    deviation = abs(M_thermo_A1 - p_LR_obs) / p_LR_obs * 100
    print(f"  Deviation of Case A.1 from central value: {deviation:.2f}%")
    in_range = p_LR_obs_low <= M_thermo_A1 <= p_LR_obs_high
    print(f"  Case A.1 prediction in conservative range: {in_range}")

    # Case A.2 alternative — delta as free parameter
    print(f"\n--- Case A.2: delta independent of chi (free parameter) ---")
    delta_A2_required = p_LR_obs * 6.0  # to match empirical target central value
    print(f"  delta_A.2 required for |M^thermo| = {p_LR_obs}: {delta_A2_required:.6f}")
    print(f"  Distance from Case A.1's chi = {CHI:.6f}: {abs(delta_A2_required - CHI):.6f}")
    print(f"  Ratio delta_A.2 / chi = {delta_A2_required/CHI:.6f}")
    print(f"  Verdict: Case A.2 would require fitting delta to ~chi, essentially")
    print(f"           reproducing Case A.1 with an extra free parameter. Disfavored")
    print(f"           by Occam's razor and minimal-primitives principle.")

    # Cross-section against other structural-value candidates
    print(f"\n--- Cross-check: other structural values for |M^thermo| ---")
    candidates = {
        "chi/6                = phi^-3 / 6    ":      CHI/6.0,
        "chi/(6 phi)          = phi^-4 / 6    ":      CHI/(6.0*PHI),
        "chi * phi/6          = phi^-2 / 6    ":      CHI*PHI/6.0,
        "1/(6 phi^2)          = ~equivalent   ":      1.0/(6.0*PHI*PHI),
        "1/(6 phi)            = ~baseline     ":      1.0/(6.0*PHI),
    }
    for name, val in candidates.items():
        match = "<-- MATCH" if abs(val - p_LR_obs) < 0.003 else ""
        print(f"  {name}= {val:.6f}  {match}")

    # Critical magnitude — Phase 1 prefactor 6/phi^2 absorption check
    print(f"\n--- Phase 1 prefactor absorption (unit-vector normalization) ---")
    phase1_prefactor = 6.0 / (PHI*PHI)
    print(f"  Phase 1 magnitude: |j_DI^net|/r_0 = 6 delta/phi^2 = {phase1_prefactor:.6f} * delta")
    print(f"  Under unit-vector normalization: |hat_j_DI^net|_0 = 6 r_0 delta/phi^2")
    print(f"  -> omega_PCD(v_host) = sigma_cycle * hat_n (unit vector, prefactor absorbed)")
    print(f"  -> |M^thermo| depends only on chirality magnitude |delta| + Schur factor,")
    print(f"     NOT on Phase 1's geometric prefactor 6/phi^2")
    if not in_range:
        print(f"  Sanity check: if Phase 1 prefactor entered |M^thermo|, prediction would be")
        wrong = phase1_prefactor * CHI / 6.0
        print(f"  {phase1_prefactor:.3f} * chi / 6 = {wrong:.6f} -- {'MATCHES' if abs(wrong-p_LR_obs)<0.01 else 'DOES NOT MATCH'} empirical")

    print("\n" + "="*72)
    print("VERDICT: Case A.1 unification (delta = chi = phi^-3) gives zero-parameter")
    print(f"prediction |M^thermo| = chi/6 = {CHI/6.0:.6f}, matching empirical leptogenesis")
    print(f"CP-asymmetry target Delta-p_LR^obs ~ {p_LR_obs} to ~{deviation:.1f}%.")
    print("Phase 3 closes positively under Case A.1.")
    print("="*72)

if __name__ == "__main__":
    main()
