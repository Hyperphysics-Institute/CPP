# Phenomena — SD-3: The Measurement Apparatus as a CPP Structure

**Paper:** SD-3 (cpp_sd3_apparatus_model_v1.tex)
**Version:** v1
**Last updated:** 31 March 2026

---

## Section 1: Explained Phenomena (PHEN-E)

### PHEN-SD3-E1. Classical Detectors Always Produce Definite Outcomes

**Observation:** In 100 years of quantum mechanics experiments, no macroscopic detector has ever been observed in a superposition state. Detectors always click or don't click — they never click-and-don't-click simultaneously.

**CPP account (THEO-SD-6):** τ_dec = ħ/(N_app × k_B × T) ~ 10⁻³⁹ s. Decoherence to a definite pointer state is instantaneous on any experimental timescale. This is a quantitative proved theorem, not an interpretational claim.

### PHEN-SD3-E2. Quantum Processors Are More Coherent Than Classical Detectors

**Observation:** Superconducting quantum processors operate at T ~ 10 mK and have coherence times τ_q ~ 10⁻⁴ to 10⁻¹ s. Classical detectors operating at room temperature decohere in ~10⁻³⁹ s.

**CPP account:** The trade-off law (THEO-SD-7) shows that quantum processors have ε_QP × τ_q = const(T). Lower temperature and fewer atoms both increase sensitivity. The quantum processor regime is physically distinct from the macroscopic detector regime — it is the only accessible experimental regime where ε is not completely negligible.

## Section 2: Novel Predictions (PHEN-P)

### PHEN-SD3-P1. CPP Signal Scales Linearly with N_q, Noise as √N_q

**Prediction:** For N_q parallel Bell pairs on a quantum processor, the total CPP signal δE ∝ N_q while statistical noise ∝ √N_q. SNR ∝ √N_q makes large-qubit processors optimal. **Status:** PRED-O — requires ~10⁶ qubits at 10 mK for sensitivity approaching detectability.

### PHEN-SD3-P2. DP Sea Anisotropy ~ 3 × 10⁻³⁴ for Centimetre-Scale Apparatus

**Prediction (THEO-SD-5):** A detector of linear size L = 1 cm imprints fractional DP Sea anisotropy δ = sea_strength × l_P/L ≈ 3 × 10⁻³⁴. **Status:** PRED-O — not directly measurable; sets the scale for Nexus coupling.

## Section 3: Validated Phenomena — Consilience (PHEN-V)

### PHEN-SD3-V1. Decoherence Rate Uses sea_strength from SS-1

The apparatus decoherence rate (THEO-SD-6) and the DP Sea anisotropy (THEO-SD-5) both use sea_strength = 0.178 from SS-1 THEO-SS-6. The same lattice constant derived from the 600-cell Voronoi geometry that governs QCD coupling also determines quantum decoherence rates and CPP apparatus coupling.


*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 31 March 2026.*
