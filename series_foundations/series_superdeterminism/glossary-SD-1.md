# Glossary — SD Series: Foundations / Superdeterminism

**Papers:** SD-1 through SD-5
**Series:** series_foundations/
**Last updated:** 31 March 2026

*This glossary covers terms specific to the SD series. General CPP terms are in the master glossary.*

---

## A₅ (Leading Angular Amplitude)

The amplitude of the dominant Fourier component of f_{H₄}:

    f_{H₄}(θ) = A₅ cos(5θ) + A₃ cos(3θ) + ...

Conjectured to equal φ⁻³/(2π) ≈ 0.0375 — the same geometric dilution factor φ⁻³ that governs the electroweak boson mass scale in the EW series. If confirmed, A₅ is determined by 600-cell geometry with no free parameters. Proving this requires completing the K₀ derivation (SD-5).

---

## CHSH Blind Spot

The observation (THEO-SD-4, SD-2) that the four standard CHSH measurement angles {0°, 45°, 90°, 135°} are not H₄-special angles — they are not extrema of f_{H₄}(θ). The CPP correction to the Bell correlation function has its largest and most structured signal at the golden-ratio angles of the 600-cell, none of which coincide with the CHSH angles. A standard CHSH experiment therefore provides the weakest possible test of the CPP superdeterministic correction.

---

## D₅ Projected Symmetry

The residual symmetry group on the measurement-angle circle S¹ obtained by projecting the 600-cell's H₄ Coxeter group (order 14,400) onto the one-dimensional space of relative measurement angles θ = θ_A − θ_B. D₅ is the dihedral group of order 10 — the symmetry group of the regular pentagon. The D₅ symmetry forces the leading Fourier component of f_{H₄} to be cos(5θ). Proved in THEO-SD-1 (SD-2).

---

## DP Sea Anisotropy (δ)

The fractional anisotropy imprinted on the DP Sea by an oriented measurement apparatus of linear size L:

    δ = sea_strength × (l_P / L) ~ 3 × 10⁻³⁴  (for L ~ 1 cm)

This is the CPP microscopic definition of "apparatus orientation" — the DP Sea around the detector is slightly asymmetric in the direction θ set by the apparatus geometry. The Nexus reads this anisotropy when establishing the λ–θ correlation. Proved in THEO-SD-5 (SD-3).

---

## ε (Nexus Participation Fraction)

The fundamental suppression factor in the CPP correction to Bell correlations:

    ε ≈ N_part / N_app

where N_part is the number of DP Sea pairs participating in the Nexus coupling to the measured particle (~1) and N_app is the number of atoms in the macroscopic detector (~10²⁶). For a standard macroscopic Bell test, ε ~ 10⁻²⁶. This suppression explains why standard quantum mechanics has been confirmed to all current experimental precision: the CPP correction δS ≈ ε × 2√2 ~ 10⁻²⁵ is far below any current sensitivity.

---

## f_{H₄}(θ)

The angular correction function in the CPP Bell correlation formula:

    E_CPP(θ) = −cos θ + ε × f_{H₄}(θ) + O(ε²)

f_{H₄} has the icosahedral H₄ symmetry of the 600-cell. Its Fourier decomposition (THEO-SD-2, SD-2) is:

    f_{H₄}(θ) = A₅ cos(5θ) + A₃ cos(3θ) + A₁₀ cos(10θ) + ...

The angular form is fully derived from group theory; the amplitudes A₅ and A₃ are partially conjectured (SD-5 open problem).

---

## H₄-Special Angles

The angles at which f_{H₄}(θ) has local extrema, set by the golden-ratio geometry of the 600-cell:

    θ ∈ {36°, 60°, 72°, 90°, 108°, 120°, 144°, 180°, ...}

These are the angles where the icosahedral 5-fold structure and the tetrahedral 3-fold structure of the 600-cell both have simultaneous extrema. The CPP correction to Bell correlations is largest and most structured at these angles. None of the standard CHSH angles {0°, 45°, 90°, 135°} are H₄-special, making continuous angular scans far more sensitive than CHSH tests (THEO-SD-3, SD-2).

---

## Hossenfelder Programme

Sabine Hossenfelder's proposal (2024) that quantum mechanics is not fundamental but is the statistical average of an underlying deterministic hidden-variables theory (superdeterminism), and that the apparent impossibility of this programme is maintained by circular argument rather than physical necessity. CPP provides a concrete instantiation of the Hossenfelder programme: the DP Sea configurations are the hidden variables, the 600-cell lattice is the deterministic substrate, and the Nexus is the mechanism that produces the measurement-setting correlations required for superdeterminism.

---

## Interpolation Conjecture (SD-4 Conjecture 1)

The conjectured form of the Nexus correlation function for general N_app and N_part:

    K(λ, θ_A, θ_B) ≈ ε_Nexus × K₀(λ) × f_{H₄}(θ_A − θ_B − θ_λ) + O(ε²)

where ε_Nexus = N_part/N_app. This interpolates between the two exact limits proved in SD-4: K → 0 as N_app → ∞ (QM recovered) and K = K₀ f_{H₄} at N_app = N_part = 1 (single-CP limit). Supported by the leading-order saddle-point evaluation of the Nexus path integral; proving it non-perturbatively is the primary open problem of the SD series.

---

## K₀(λ) (Hidden-Variable Amplitude Factor)

The particle-side factor in the Nexus correlation function, representing the projection of the particle hidden variable λ onto the DI-bit exchange degree of freedom. K₀(λ) determines the amplitude of the CPP correction to Bell correlations. It is known to exist and factorise from the angular factor f_{H₄} (from THEO-SD-9, SD-4), but its explicit functional form is not yet derived. Deriving K₀(λ) from sea_strength, the 600-cell vertex coordinates, and the ZBW dynamics is the primary open problem of SD-5.

---

## Nexus Correlation Function (K)

The function K(λ, θ_A, θ_B) that quantifies the Nexus-induced correlation between the particle hidden variable λ and the measurement apparatus orientations θ_A, θ_B:

    E_CPP = ∫ E_QM(θ_A, θ_B | λ) × ρ(λ) × [1 + K(λ, θ_A, θ_B)] dλ

K = 0 recovers standard QM (K → 0 as N_app → ∞, proved). K ~ O(1) occurs in the single-CP limit and at Planck energies. The full derivation of K from the Nexus path integral is the central mathematical problem of the SD series.

---

## Quantum Processor Trade-off Law (THEO-SD-7)

The result (SD-3) that for a quantum processor with N_q qubits:

    ε_QP × τ_q = ħ / (N_sub × k_B × T) = const(T)

The signal per circuit run from the CPP correction is independent of the number of qubits N_q: increasing N_q raises the participation fraction ε_QP but proportionally shortens the coherence time τ_q. The optimal strategy is not maximum qubits but maximum parallel Bell pairs — SNR scales as √N_q.

---

## Ratio Test

The CPP prediction that the ratio of the angular correction at 36° to that at 120° is:

    δE(36°) / δE(120°) ≈ −1.065

This prediction is independent of the unknown amplitude A₅ — it tests the angular structure of f_{H₄} alone. It is falsifiable at precision ~ ε × 10⁻² ~ 10⁻²⁸ with a continuous-angle Bell scan and provides a unique identifying signature of the CPP superdeterministic correction.

---

## Superdeterminism

The hypothesis that the measurement settings θ_A, θ_B in a Bell experiment are not statistically independent of the particle hidden variables λ — because all three were jointly determined by the same deterministic dynamics at the Big Bang or at the time of entanglement. If true, Bell's theorem does not apply, and local hidden-variable theories are not ruled out. CPP makes this concrete: the Nexus is the mechanism that correlates θ and λ atemporally, without any signal passing between particle and detector.

---

## τ_dec (Apparatus Decoherence Time)

The time for a macroscopic detector to decohere to its classical pointer state:

    τ_dec = ħ / (N_app × k_B × T) ≲ 10⁻³⁹ s

For any macroscopic detector (N_app ~ 10²⁶, T ≳ 1 mK), τ_dec is 24 orders of magnitude faster than the Planck time and immeasurably short. This is why macroscopic detectors are always classical and why quantum mechanics has appeared complete for 100 years. Proved in THEO-SD-6 (SD-3).
