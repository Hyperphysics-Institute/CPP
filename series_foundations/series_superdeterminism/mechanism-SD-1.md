# Mechanism — SD-1: The Nexus as a Superdeterministic Hidden-Variable Mechanism

**Paper:** SD-1 (cpp_sd1_nexus_superdeterminism_v1.tex)
**Series:** Foundations (series_foundations/)
**Last updated:** 31 March 2026

---

## Part 1: The Problem — Bell's Theorem and Superdeterminism

**Step 1 — Bell's theorem forbids certain kinds of hidden-variable theories.**
Bell's theorem proves that no local hidden-variable theory can reproduce all predictions of quantum mechanics. Specifically, for entangled particles measured at spatially separated detectors, the CHSH inequality |S| ≤ 2 must hold for any local hidden-variable theory. Quantum mechanics predicts |S|_max = 2√2, and experiments confirm this. Therefore, hidden variables that are local and independent of the measurement settings are ruled out.

**Step 2 — Superdeterminism is the remaining loophole.**
Bell's theorem assumes that the hidden variables λ (encoding the particle state) are statistically independent of the measurement settings (θ_A, θ_B). Superdeterminism denies this independence: if the particle state at the time of entanglement was already correlated with the future detector orientations — because both are governed by the same deterministic dynamics from the Big Bang onward — then Bell's theorem does not apply. This is the Hossenfelder superdeterminism programme.

**Step 3 — CPP provides a concrete instantiation of superdeterminism.**
In CPP, the DP Sea configurations are the hidden variables λ. The 600-cell lattice is the deterministic substrate. The Nexus — the atemporal global constraint enforcing DI-bit conservation at every Absolute Moment — is the mechanism that correlates apparatus orientation θ with the hidden-variable DP Sea state λ at the time of entanglement. The correlation is not a signal sent from detector to particle; it is enforced atemporally by the Nexus conservation law.

---

## Part 2: The Nexus Correlation Mechanism

**Step 4 — The Nexus correlates λ and θ atemporally.**
At the moment of entanglement, the Nexus enforces DI-bit conservation across the entire lattice, including the region occupied by the future detector. Because the Nexus operates outside time (atemporally), its constraint spans both the entanglement event and the measurement event simultaneously, producing the correlation ρ(λ, θ) ≠ ρ(λ) × ρ(θ) required for superdeterminism.

**Step 5 — The correction is suppressed by the participation fraction ε.**
A macroscopic detector has N_app ~ 10²⁶ atoms. The number of DP Sea pairs participating in the Nexus coupling to the measured particle is N_part ~ 1. The Nexus participation fraction:

    ε ≈ N_part / N_app ~ 10⁻²⁶

This is the fundamental suppression factor. The CPP correction to the standard QM prediction |S| = 2√2 is:

    δS ≈ ε × 2√2 ~ 10⁻²⁵

This is far below current experimental sensitivity, explaining why quantum mechanics has been confirmed to all current precision.

**Step 6 — The correction has H₄ angular structure.**
The CPP correction to the Bell correlation function E(θ_A, θ_B) = −cos(θ_A − θ_B) takes the form:

    E_CPP = −cos θ + ε × f_{H₄}(θ) + O(ε²)

where θ = θ_A − θ_B and f_{H₄} is a function with the icosahedral H₄ symmetry of the 600-cell. The angular structure is set by the 600-cell geometry: the correction has extrema at the golden-ratio angles {31.7°, 36°, 45°, 58.3°, 67.5°, 72°, 120°}. This angular signature is falsifiable even though the magnitude is far below current sensitivity.

---

## Part 3: Why Standard Bell Tests Are Insensitive

**Step 7 — The CHSH test measures at four angles, none H₄-special.**
Standard CHSH experiments measure E(θ) at only four angles: {0°, 45°, 90°, 135°}. The function f_{H₄} has its extrema at the golden-ratio angles of the 600-cell, none of which coincide with the CHSH angles. The CHSH test therefore samples f_{H₄} at its least informative points — it provides the weakest possible test of CPP's superdeterministic correction. A continuous angular scan with ~5° resolution would be far more sensitive.

**Step 8 — The apparatus decoherence time is faster than any experiment.**
A macroscopic detector decoheres in τ_dec ~ 10⁻³⁹ s. No experiment can probe the Nexus coupling before the apparatus decoheres to its classical pointer state. This is why quantum mechanics has worked perfectly for 100 years — not because CPP deviations are impossible, but because macroscopic detectors are always classical on any experimental timescale.

---

## Part 4: Open Problems and the SD Series Plan

SD-1 establishes the framework and registers four open problems that the remaining SD papers address:

- OPEN-P-SD-1: Derive the Nexus correlation function K(λ, θ_A, θ_B) from first principles → SD-4
- OPEN-P-SD-2: Apparatus model in CPP: derive N_app-dependence of ε → SD-3
- OPEN-P-SD-3: Amplitudes A₅, A₃ of f_{H₄} → SD-2, SD-5
- OPEN-P-SD-4: Decoherence threshold for Nexus visibility → SD-3

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–3: Bell loophole and CPP instantiation | §1 (Introduction), §2 (CPP Hidden-Variable Structure) |
| Steps 4–5: Nexus correlation and ε | §3 (Open Problem), §4 (Order-of-Magnitude Estimates) |
| Step 6: H₄ angular correction | §5 (600-Cell Angular Signature) |
| Steps 7–8: why CHSH is insensitive | §5, §7 (Consolidated Open Problems) |
| Part 4: open problems | §6 (Relation to Hossenfelder) |
