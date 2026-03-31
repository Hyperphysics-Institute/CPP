# Mechanism — SD-3: The CPP Apparatus Model — Macroscopic Detectors, Decoherence, and the Quantum Processor Trade-Off Law

**Paper:** SD-3 (cpp_sd3_apparatus_model_v1.tex)
**Series:** Foundations (series_foundations/)
**Last updated:** 31 March 2026

*This file provides a sequential cause-and-effect account of the physical mechanisms in SD-3. SD-1 established the framework (Nexus as superdeterministic mechanism), SD-2 derived the angular form (f_{H₄} from H₄ symmetry). SD-3 addresses the scale: how large is the deviation, why is it currently undetectable, and what experimental architecture gives the best chance of detection? The answers require modelling the measurement apparatus as a CPP structure — not an external classical device but a collection of ~10²⁶ eCPs participating in the same Nexus constraint as the measured particles.*

---

## Part 1: The Apparatus as a CPP Structure

**Step 1 — A measurement apparatus is a macroscopic DP Sea configuration.**
In CPP, a polarisation analyser or spin detector is not an external classical boundary condition imposed on the quantum system — it is a macroscopic collection of N_app ~ 10²⁶ eCPs arranged in a crystal, magnetic, or optical medium, embedded in the same 600-cell lattice and participating in the same Nexus constraint as the particles being measured. Its orientation θ is a collective degree of freedom of those eCPs, defined as the macroscopic average of the individual eCP SSV vectors:

    θ = (1/N_app) Σᵢ θᵢ

where θᵢ is the orientation of the i-th eCP relative to a reference direction. Individual eCPs fluctuate thermally; the collective average is sharp to O(1/√N_app) — which for N_app ~ 10²⁶ means the apparatus orientation is defined to ~10⁻¹³ radians. This is the CPP account of why macroscopic detectors have definite orientations.

**Step 2 — The apparatus imprints a fractional anisotropy on the surrounding DP Sea.**
An oriented collection of coherently aligned eCPs creates an anisotropic SSV field in the surrounding Dipole Sea. At position r from the apparatus centre, the fractional anisotropy of the DP Sea density is:

    δ(r, θ) = sea_strength × (l_P / |r|) × cos(θ − φ_r)

where φ_r is the angular direction of r and sea_strength ≈ 0.178 (derived in SS-1). This is THEO-SD-5 (DP Sea anisotropy scale). At the apparatus surface (characteristic size L ~ 1 cm):

    δ₀ = sea_strength × (l_P / L) ≈ 0.185 × (1.62 × 10⁻³⁵ m / 10⁻² m) ≈ 3 × 10⁻³⁴

This is vanishingly small — but it is the microscopic CPP meaning of "the apparatus has orientation θ." The surrounding DP Sea is anisotropic by the fraction δ₀ in the direction θ. The Nexus reads this anisotropy when establishing the λ–θ correlation.

---

## Part 2: Thermal Decoherence — Why Macroscopic Detectors Are Always Classical

**Step 3 — A macroscopic apparatus decoheres to a classical pointer state almost instantaneously.**
THEO-SD-6 (apparatus is always classical): A macroscopic measurement apparatus with N_app atoms at temperature T decoheres to a classical (definite-orientation) state in time:

    τ_dec = ℏ / (N_app × k_B × T)

This follows from the standard Joos-Zeh-Zurek decoherence theory applied to the collective orientation degree of freedom, confirmed by the CPP Lindblad master equation (QM-4). Numerically:

    Room temperature (300 K):        τ_dec ≈ 2.5 × 10⁻⁴⁰ s
    Liquid helium (4.2 K):           τ_dec ≈ 1.8 × 10⁻³⁸ s
    Dilution refrigerator (10 mK):   τ_dec ≈ 7.6 × 10⁻³⁶ s

Even at 10 mK, decoherence occurs in 10⁻³⁶ seconds — 24 orders of magnitude faster than the Planck time (5.4 × 10⁻⁴⁴ s is the Planck time, so τ_dec is actually 8 orders faster than tP, but 27 orders faster than any measurement timescale τ_meas ≳ 10⁻⁹ s). The apparatus is always in a classical state during any Bell measurement.

**Step 4 — Classical character does not suppress the CPP correction.**
This is a subtle and important point. The apparatus being classical does not mean the CPP correction vanishes — it means the apparatus orientation θ is sharp and well-defined during the measurement. The Nexus correlation (SD-1 Proposition 1) couples θ to the particle hidden variable λ; this coupling is active regardless of whether the apparatus is in a quantum superposition. The CPP correction exists *because* the apparatus has a definite orientation, not despite it. The decoherence theorem explains why quantum mechanics has worked perfectly for 100 years — macroscopic detectors are never quantum — while leaving the superdeterministic correction intact.

---

## Part 3: The Quantum Processor Trade-Off Law

**Step 5 — A quantum processor plays two competing roles in a CPP Bell test.**
A quantum processor with N_q qubits at temperature T (dilution refrigerator, T ~ 10 mK) simultaneously:

(a) Provides quantum coherence: the qubits form a quantum system with collective decoherence time τ_q = ℏ/(N_q k_B T), which *shrinks* as N_q increases.

(b) Raises the participation fraction: with N_q qubits, the particle-side of the Nexus constraint involves N_q Grid Points, raising ε_QP = N_q/N_sub, which *grows* as N_q increases.

These two effects are in direct competition. More qubits give you more Nexus sensitivity but proportionally less time to observe it.

**Step 6 — The ε·τ product is independent of N_q.**
THEO-SD-7 (quantum processor trade-off law): The product of the Nexus participation fraction ε_QP and the quantum coherence time τ_q is:

    ε_QP × τ_q = (N_q / N_sub) × (ℏ / (N_q × k_B × T)) = ℏ / (N_sub × k_B × T) = const(T)

The N_q cancels exactly. The product depends only on temperature and substrate size — not on the number of qubits. This has the structure of an uncertainty principle for CPP detectability: you can have high Nexus sensitivity (large ε) or long quantum coherence (large τ), but not both.

**Step 7 — The signal per circuit run is independent of N_q.**
The CPP signal accumulated in a single circuit run of N_gates gates is:

    S_run = ε_QP × |f_{H₄}(θ)| × N_gates = ε_QP × |f_{H₄}| × τ_q / τ_gate

Substituting the trade-off law:

    S_run = ℏ / (N_sub × k_B × T × τ_gate) × |f_{H₄}(θ)|

This is COROLLARY-SD-1: the signal per run is independent of N_q. At T = 10 mK and τ_gate = 50 ns:

    S_run ≈ 1.5 × 10⁻²⁸

This is the fundamental per-run sensitivity floor set by the substrate thermal bath.

---

## Part 4: What N_q Actually Buys — Parallel Bell Pairs

**Step 8 — N_q parallel Bell pairs accumulate signal linearly.**
Although N_q does not affect the signal per run (Step 7), it helps in a different way. With N_q qubits, one can measure N_q parallel Bell pairs simultaneously in a single run. Each parallel pair contributes an independent CPP correction. The total signal from N_q parallel pairs scales as N_q, while shot noise scales as √N_q:

    Total signal ~ N_q × M × S_run        (linear in N_q and runs M)
    Total noise  ~ √(N_q × M)             (shot noise)
    SNR_CPP      ~ √(N_q × M) × S_run     (square root scaling)

This is PREDICTION-SD-1 (N_q scaling law): a CPP signal, if present, grows linearly with N_q at fixed M. This linear growth distinguishes it from systematic errors (independent of N_q), shot noise (scales as √N_q), and other quantum effects. Larger processors are better, but by a square root, not linearly.

---

## Part 5: Temperature Dependence

**Step 9 — The CPP signal scales as 1/T.**
From the trade-off law, S_run ∝ 1/T. Colder systems accumulate CPP signal faster:

    T = 100 mK:    S_run ≈ 1.5 × 10⁻²⁹
    T = 10 mK:     S_run ≈ 1.5 × 10⁻²⁸  (current dilution refrigerators)
    T = 1 mK:      S_run ≈ 1.5 × 10⁻²⁷
    T = 0.1 mK:    S_run ≈ 1.5 × 10⁻²⁶  (achievable but uncommon)

This is PREDICTION-SD-2 (temperature enhancement): at fixed N_q and M, the CPP signal scales as 1/T. Cooling from 10 mK to 0.1 mK gives a factor of 100 enhancement. The 1/T dependence is a falsifiable prediction — running the same circuit at multiple temperatures should show this scaling if CPP is correct.

---

## Part 6: The Two Coupling Channels — Nexus vs. Direct SSV

**Step 10 — The Nexus term dominates the direct SSV term by eight orders of magnitude.**
The total coupling of the apparatus orientation θ to the particle hidden variable λ has two independent channels:

    Γ(θ, λ) = ε_Nexus × f_{H₄}(θ − θ_λ)  +  δ₀ × cos(θ − θ_λ)
               \_____________________/          \___________________/
                Nexus (atemporal)                direct SSV (causal)

The direct SSV contribution (δ₀ ~ 10⁻³⁴) propagates at the speed of light and has a simple cosine angular dependence. The Nexus contribution (ε_Nexus ~ 10⁻²⁶) operates atemporally and has the H₄ angular structure f_{H₄}. The Nexus dominates by eight orders of magnitude. This hierarchy has a critical physical consequence: if the CPP correction arose from the direct SSV field (causal), the angular dependence would be cos θ — indistinguishable from a systematic error. Because the Nexus term dominates, the angular dependence is f_{H₄}(θ) with its 5-fold and 3-fold structure (SD-2). The icosahedral angular signature is the distinctive fingerprint that separates CPP from any causal correction.

---

## Part 7: The Complete Experimental Prescription

**Step 11 — The five-property CPP signature in a quantum processor Bell test.**
Combining SD-1 through SD-3, the complete falsifiable prediction is:

(1) A residual δE(θ) after subtracting −cos θ, with 72° and 120° periodicity (from SD-2)
(2) The residual grows linearly with N_q (from Step 8)
(3) The residual grows as 1/T (from Step 9)
(4) The ratio δE(36°)/δE(120°) ≈ −1.065 is φ-valued and independent of amplitude (from SD-2)
(5) The residual vanishes at θ = 90° to leading order (from SD-2)

All five properties together would uniquely identify a CPP signal. Properties 2–4 can distinguish CPP from any systematic error with a standard angular dependence.

---

## Part 8: Why Current Experiments Are Blind

**Step 12 — The sensitivity gap is 22 orders of magnitude.**
Standard optical Bell tests achieve sensitivity ~10⁻³. The CPP signal is ~10⁻²⁶. Even near-future experiments with 10⁸ runs reach only ~10⁻⁶. The gap is currently unbridgeable by direct measurement.

The CPP position is not that the deviation is undetectable forever, but that macroscopic detectors are maximally unfavourable. The prediction is that quantum computer engineering will eventually produce unexpected anomalies — not from directly targeting CPP, but from building ever-larger and more precise quantum systems. When those anomalies come, they will have the specific five-property signature of Step 11. Until then, the angular structure (ratio test) and N_q scaling provide the most accessible indirect tests.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–2: apparatus as CPP structure | §2 (Apparatus as CPP Structure), THEO-SD-5 (Eq. 2–3) |
| Steps 3–4: decoherence and classical apparatus | §3, THEO-SD-6 (Eq. 4), Table 1, Remark |
| Steps 5–7: trade-off law and signal per run | §4, THEO-SD-7 (Eq. 5–7), COROLLARY-SD-1 (Eq. 8–9) |
| Step 8: N_q parallel Bell pairs | §4.3, PREDICTION-SD-1 (Eq. 10–12) |
| Step 9: temperature dependence | §5, PREDICTION-SD-2 (Eq. 13), Table 2 |
| Step 10: Nexus vs. direct SSV | §6, (Eq. 14), Remark |
| Steps 11–12: experimental programme and sensitivity gap | §7–8, Table 3 |
