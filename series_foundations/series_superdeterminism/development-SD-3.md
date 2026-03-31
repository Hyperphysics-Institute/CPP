# Development History — SD-3: The Measurement Apparatus as a CPP Structure

**Paper:** SD-3
**Series:** Foundations (series_foundations/)
**Last updated:** 31 March 2026

---

**Full title:** SD-3: The Measurement Apparatus as a CPP Structure
**File:** cpp_sd3_apparatus_model_v1.tex | **Version:** v1

## Central Results — Three Theorems

| Theorem | Result |
|---------|--------|
| THEO-SD-5 (DP Sea anisotropy) | δ = sea_strength × l_P/L ~ 3 × 10⁻³⁴ for L ~ 1 cm |
| THEO-SD-6 (apparatus always classical) | τ_dec = ħ/(N_app k_B T) ≲ 10⁻³⁹ s |
| THEO-SD-7 (quantum processor trade-off) | ε_QP × τ_q = ħ/(N_sub k_B T) = const(T) |

**Prediction 1 (N-qubit scaling):** SNR ∝ √N_q for N_q parallel Bell pairs.

## Key Numbers

    τ_dec ~ 10⁻³⁹ s  (macroscopic detector, room temperature)
    δ ~ 3 × 10⁻³⁴    (DP Sea anisotropy for L ~ 1 cm apparatus)
    ε_QP × τ_q = ħ/(N_sub k_B T)  (constant at fixed T)

## Cross-Series Connection

THEO-SD-5 and THEO-SD-6 use sea_strength = 0.178 from SS-1 THEO-SS-6 (strong sector theorem). QM-4 Lindblad dephasing rate also uses sea_strength. Both SD-3 and QM-4 are quantitative applications of the same lattice constant to quantum decoherence.

---

*See also: open_problems/README.md (OPEN-P-SD-1 through OPEN-P-SD-5), postulates_and_theorems.md (THEO-SD-1 through THEO-SD-10).*
