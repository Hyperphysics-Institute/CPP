# Mechanism — SD-4: The Nexus Correlation Function — Two Exact Limits and the Interpolation Conjecture

**Paper:** SD-4 (cpp_sd4_nexus_correlation_function_v1.tex)
**Series:** Foundations (series_foundations/)
**Last updated:** 31 March 2026

*SD-4 is the capstone of the SD series. It proves three exact results: (1) QM is recovered as N_app → ∞; (2) the Nexus produces genuine correlations at N_app = N_part = 1; (3) QM fails at Planck energies. It conjectures the interpolation formula connecting these limits and assembles the five-property experimental signature. The paper opens with "Honest accounting is essential for a capstone paper" — every result is labelled as theorem, conjecture, or open problem.*

---

## Part 1: The Nexus as a Lattice Path Integral

**Step 1 — The standard CPP partition function (without Nexus) gives QM.**
In CPP, observable probabilities are computed from the DI-bit path integral over the 600-cell lattice:

    Z_QM[φ] = ∫ D[φ] exp(iS[φ]/ℏ)

where φ = {ρᵢ, φᵢ} is the DI-bit field (density and phase) at each Grid Point, and S is the CPP action from the QM series. Standard quantum mechanics emerges from Z_QM after averaging over hidden variables.

**Step 2 — The Nexus constraint modifies the partition function.**
The Nexus enforces global DI-bit conservation: Σᵢ δbᵢ = 0, where δbᵢ is the DI-bit change at Grid Point i during the experiment. The constrained partition function is:

    Z_CPP[φ] = ∫ D[φ] exp(iS[φ]/ℏ) × δ(Σᵢ δbᵢ[φ])

The delta functional is the mathematical implementation of the Nexus. Without it, Z_CPP = Z_QM and standard QM is recovered.

**Step 3 — The Nexus field μ couples all Grid Points globally.**
Writing the delta functional as a Fourier integral introduces the Nexus field μ — a Lagrange multiplier:

    δ(Σᵢ δbᵢ) = ∫ (dμ/2π) exp(iμ Σᵢ δbᵢ[φ])

The constrained partition function becomes:

    Z_CPP[φ] = ∫ (dμ/2π) ∫ D[φ] exp(i(S[φ] + μ Σᵢ δbᵢ[φ])/ℏ)

The Nexus field μ couples all Grid Points through the global sum Σᵢ δbᵢ. This is mathematically equivalent to adding a global coupling term to the action. μ is not a physical field — it is a mathematical device for implementing the constraint. Integrating over μ enforces DI-bit conservation exactly.

**Step 4 — The Grid Points partition into three subsets.**
For a Bell experiment, the Grid Points divide into:

    P:  N_part Grid Points associated with the particle pair (hidden variables λ)
    A:  N_app Grid Points associated with the apparatus (orientation θ_A, θ_B)
    R:  N_rest remaining Grid Points (cosmic environment, N_rest ≈ N_total)

The Nexus correlation function K is the ratio of constrained to unconstrained partition functions, integrated over apparatus and environment degrees of freedom at fixed λ:

    K(λ, θ_A, θ_B) = Z_CPP(λ, θ_A, θ_B)/Z_QM(λ) × (normalisation) − 1

K = 0 recovers standard QM. K ≠ 0 is the superdeterministic correction.

---

## Part 2: Macroscopic Limit — QM Recovered Exactly (THEO-SD-8)

**Step 5 — The saddle-point of the μ-integral determines the leading behaviour.**
The saddle-point condition ∂_μ(S_eff) = 0 gives:

    μ* = −⟨Σ_{i∈P} δbᵢ⟩_λ / (N_app + N_rest)

The Nexus field μ* is the ratio of the particle's net DI-bit change to the total number of compensating Grid Points. This ratio controls the coupling between particle and apparatus in the path integral.

**Step 6 — As N_app → ∞, μ* → 0 and K → 0.**
With N_part fixed and N_app → ∞, the denominator grows without bound while the numerator stays bounded:

    μ* ~ N_part / (N_app + N_rest) → 0

The correlation function at leading order is:

    K ≈ iμ* × ⟨Δb_A(θ)⟩ = O(N_part / N_app) → 0

The lattice central limit theorem controls the fluctuations around the saddle point: with N_app independent degrees of freedom, fluctuations are O(1/√N_app) relative to the mean, subdominant to the O(N_part/N_app) leading term. Standard quantum mechanics is the N_app → ∞ limit of CPP. This is a proved theorem.

**Step 7 — This explains 100 years of experimental consistency.**
For any macroscopic detector (N_app ~ 10²⁶) measuring any laboratory-scale quantum system (N_part ~ 2), the CPP correction is suppressed by ε ~ 10⁻²⁶. Twenty-two orders below current precision. CPP is fully consistent with all existing quantum experiments — not by fiat but by theorem.

---

## Part 3: Single-CP Limit — Maximum Nexus Coupling (THEO-SD-9)

**Step 8 — For N_app = N_part = 1, the Nexus constraint is exact.**
When both apparatus and particle consist of a single CP, the global conservation constraint Σᵢ δbᵢ = 0 reduces to two terms:

    δb_apparatus = −δb_particle

The apparatus DI-bit change is completely determined by the particle. No averaging, no approximation — the constraint is exact.

**Step 9 — K factorises into amplitude and angular parts.**
The partition function in this limit constrains the apparatus field to be the negative of the particle field. The action separates into particle, apparatus, and coupling terms. The coupling term S_PA is the DI-bit exchange interaction between the two CPs, whose angular dependence is set by the relative orientation of the two Grid Points in the 600-cell. Since the 600-cell adjacency matrix has H₄ symmetry:

    K(λ, θ) = K₀(λ) × f_{H₄}(θ − θ_λ)

where K₀(λ) is the projection of λ onto the DI-bit exchange degree of freedom and f_{H₄} is the angular function from SD-2. The angular form is confirmed from the path integral structure — it enters through the 600-cell eigenvalues, not as an additional postulate.

**Step 10 — This proves the Nexus produces genuine correlations.**
The single-CP limit is not physically realisable (real experiments have macroscopic detectors), but it proves a crucial point: the Nexus does produce non-zero K. The superdeterministic structure is real — it exists at the lattice level. The macroscopic limit (Step 6) shows it is suppressed; the single-CP limit shows it is not zero.

---

## Part 4: Planck-Energy Limit — QM Fails Completely (THEO-SD-10)

**Step 11 — At Planck energies, the lattice granularity matters.**
As the particle de Broglie wavelength λ_dB approaches the Planck length l_P, the particle's DP Sea configuration spans O(1) Grid Points. The effective particle count is:

    N_part^eff ~ (λ_dB / l_P)³

For λ_dB ≫ l_P (all current experiments): N_part^eff ≫ 1 and K ≪ 1 (QM works).
For λ_dB → l_P: N_part^eff → 1 and the distinction between "particle Grid Points" and "apparatus Grid Points" dissolves. The Nexus constraint strongly couples the two subsystems and K → O(1).

**Step 12 — QM fails qualitatively at the Planck scale.**
Standard QM predicts smooth behaviour at all energies. CPP predicts a qualitative departure at E ~ E_Planck ~ 10¹⁹ GeV: the Bell correlation function acquires O(1) corrections with the specific H₄ angular structure. Current experiments (LHC: λ_dB ~ 10⁻¹⁹ m) are 16 orders above l_P. The deviation at LHC energies is O((l_P/λ_dB)²) ~ 10⁻³² — completely unobservable.

---

## Part 5: The Interpolation Conjecture

**Step 13 — The saddle-point evaluation gives the conjecture for general N_app.**
Expanding the Nexus path integral around the saddle point μ* for finite N_app and N_part at leading order in ε = N_part/N_app:

    K(λ, θ_A, θ_B) ≈ ε_Nexus × K₀(λ) × f_{H₄}(θ_A − θ_B − θ_λ) + O(ε²)

This interpolation conjecture is consistent with both exact limits: as ε → 0, K → 0 (macroscopic limit); at ε = 1, K = K₀ f_{H₄} (single-CP limit). It is supported by the saddle-point calculation but not proved to all orders in ε. The non-perturbative proof is the primary remaining open problem (SD-5).

**Step 14 — The conjecture is strongly constrained by the boundary conditions.**
Any function K(ε) that reduces to zero at ε = 0, to K₀ f_{H₄} at ε = 1, and is analytic in ε must have the form ε × K₀ × f_{H₄} + O(ε²) at leading order. The conjecture is therefore the simplest function consistent with both exact limits. Proving that higher-order corrections are O(ε²) and not O(ε) requires the non-perturbative analysis.

---

## Part 6: The Complete Five-Property CPP Signature

**Step 15 — Assembling the prediction from SD-1 through SD-4.**
The complete falsifiable prediction for a quantum processor Bell test:

(1) A residual δE(θ) after subtracting −cos θ with extrema at golden-ratio angles {36°, 72°, 108°, ...} — from SD-2
(2) The residual grows linearly with N_q at fixed M — from SD-3
(3) The residual grows as 1/T at fixed N_q — from SD-3
(4) The ratio δE(36°)/δE(120°) ≈ −1.065 is amplitude-independent — from SD-2
(5) The residual vanishes at θ = 90° to leading order — from SD-2

All five together uniquely identify CPP. Properties 2–4 can distinguish CPP from any systematic error with standard angular dependence. No other superdeterministic model predicts this specific combination.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–4: Nexus path integral formulation | §2 (Nexus as Lattice Path Integral), Eq. 1–5 |
| Steps 5–7: macroscopic limit proof | §3, THEO-SD-8, Eq. 6–9 |
| Steps 8–10: single-CP limit proof | §4, THEO-SD-9, Eq. 10–12 |
| Steps 11–12: Planck-energy limit | §5, THEO-SD-10, Eq. 13–14 |
| Steps 13–14: interpolation conjecture | §6, Conjecture 1, Eq. 15 |
| Step 15: five-property signature | §7 (Complete CPP Prediction) |
