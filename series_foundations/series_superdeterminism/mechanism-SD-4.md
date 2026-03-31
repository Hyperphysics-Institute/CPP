# Mechanism — SD-4: The Nexus Correlation Function — Two Exact Limits

**Paper:** SD-4 (cpp_sd4_nexus_correlation_function_v1.tex)
**Last updated:** 31 March 2026

---

## Part 1: The Nexus as a Lattice Path Integral

**Step 1 — The Nexus correlation function K is defined as a lattice path integral.**
The Nexus constraint at every Absolute Moment can be expressed as a path integral over all DI-bit configurations consistent with global conservation. The Nexus correlation function K(λ, θ_A, θ_B) is the expectation value, in this path integral, of the correlator between the particle hidden variable λ and the apparatus orientations θ_A, θ_B. SD-4 derives K exactly in two limiting cases and conjectures its form for general N_app, N_part.

---

## Part 2: Macroscopic Limit — QM Recovered Exactly (Theorem 1)

**Step 2 — As N_app → ∞, K → 0 uniformly.**
THEO-SD-8 (macroscopic limit): As N_app → ∞ with N_part fixed:

    K → 0  at rate  K ~ N_part / N_app

Standard quantum mechanics is the N_app → ∞ limit of CPP. The proof uses the lattice central limit theorem applied to the Nexus constraint: as the apparatus becomes macroscopic, the N_app DP Sea pairs it comprises average out the Nexus correlation, producing K → 0 and hence E_CPP → −cos θ = E_QM. This is a proved theorem, not a conjecture.

---

## Part 3: Single-CP Limit — Maximum Nexus Coupling (Theorem 2)

**Step 3 — For N_app = N_part = 1, K factorises exactly.**
THEO-SD-9 (single-CP limit): When the apparatus has only one CP and the particle has only one CP:

    K(λ, θ) = K₀(λ) × f_{H₄}(θ − θ_λ)

where f_{H₄} is the angular function from SD-2 and θ_λ is the preferred axis of the particle hidden variable. The Nexus coupling is maximally strong when apparatus and particle are at the same scale. This exact result confirms the product structure conjectured in SD-3: the correlation separates into an angular factor (determined by SD-2) and an amplitude factor K₀(λ) (still open in SD-5).

---

## Part 4: Planck-Energy Limit — QM Fails Completely (Theorem 3)

**Step 4 — At Planck energies, K ~ O(1).**
THEO-SD-10 (Planck-energy limit): As the particle de Broglie wavelength λ_dB → l_P:

    K → O(1)

Standard QM fails completely at Planck energies. The Nexus correction is no longer small — it becomes the dominant term in the Bell correlation function. CPP predicts significant deviations from the QM prediction at Planck-scale energies, though no current experiment approaches this regime.

---

## Part 5: The Interpolation Conjecture

**Step 5 — The general case is conjectured by saddle-point approximation.**
For general N_app and N_part, the saddle-point evaluation of the Nexus path integral gives:

    K(λ, θ_A, θ_B) ≈ ε_Nexus × K₀(λ) × f_{H₄}(θ_A − θ_B − θ_λ) + O(ε²)

where ε_Nexus = N_part / N_app. This interpolation conjecture is consistent with both exact limits (K → 0 as ε → 0; K → K₀ f_{H₄} at ε = 1) and is supported by the saddle-point evaluation. Proving it non-perturbatively — to all orders in ε — is the primary remaining open problem in CPP quantum foundations (SD-5).

---

## Part 6: The Complete CPP Bell Test Prediction

**Step 6 — Five distinguishing properties of the CPP correction.**
SD-4 assembles the complete experimental prediction:
1. Angular signature: extrema at golden-ratio angles {36°, 72°, 108°, ...}
2. Ratio test: δE(36°)/δE(120°) ≈ −1.065 (independent of amplitude)
3. N_q scaling: δE ∝ N_q for parallel Bell pairs (SNR ∝ √N_q)
4. Temperature dependence: ε ∝ 1/(N_q T) → larger at lower T
5. No free parameters: all predictions follow from sea_strength, φ, and l_P

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Step 1: Nexus as path integral | §2 (Nexus as a Lattice Path Integral) |
| Step 2: macroscopic limit | §3, THEO-SD-8 |
| Step 3: single-CP limit | §4, THEO-SD-9 |
| Step 4: Planck-energy limit | §5, THEO-SD-10 |
| Step 5: interpolation conjecture | §6 (Interpolation Conjecture) |
| Step 6: complete prediction | §7 (Complete CPP Prediction for Bell Tests) |
