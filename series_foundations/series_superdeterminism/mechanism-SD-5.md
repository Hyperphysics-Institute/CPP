# Mechanism — SD-5: K₀ Derivation — The Hidden-Variable Amplitude

**Paper:** SD-5 (cpp_sd5_K0_derivation_v0.tex)
**Series position:** Research agenda paper — v0, target to become v1 when derivation is complete
**Last updated:** 31 March 2026

---

## Part 1: What SD-5 Is

SD-5 is unusual in the CPP series: it is a research agenda document rather than a completed derivation. Where SD-1 through SD-4 each proved theorems, SD-5 identifies the two remaining mathematical problems and the specific techniques needed to solve them. Upon completion of the derivation, this document becomes Version 1 with the full results. It is included in the series as an honest record of where the frontier currently stands.

---

## Part 2: The Two Open Questions

**Open Question 1 — The hidden-variable factor K₀(λ).**
SD-4 Theorem 2 showed that in the single-CP limit, K = K₀(λ) × f_{H₄}(θ − θ_λ). The angular factor f_{H₄} is fully derived (SD-2). The hidden-variable factor K₀(λ) — the projection of the particle hidden variable λ onto the DI-bit exchange degree of freedom — is not yet derived. K₀(λ) determines the amplitude of the CPP correction. Until it is derived, the magnitude of δE is unknown (only its angular dependence and N_q scaling are known).

**Open Question 2 — Non-perturbative interpolation.**
SD-4 conjectured K ≈ ε × K₀ × f_{H₄} based on a saddle-point approximation. This is the leading-order result in ε = N_part/N_app. The full non-perturbative result — proving this conjecture to all orders in ε — requires solving the Nexus path integral exactly, which is an open mathematical problem.

---

## Part 3: Why the Amplitude Matters

**Step 1 — The ratio test is amplitude-independent; the magnitude is not.**
SD-2 established the ratio test δE(36°)/δE(120°) ≈ −1.065, which is independent of the amplitude A₅ = K₀ × φ⁻³/(2π) (conjectured). This ratio can be tested with any precision Bell test that scans angles. However, the question "how precise must the experiment be to see the CPP signal?" requires knowing the amplitude. Without K₀, only lower bounds on the required experimental precision can be set.

**Step 2 — The A₅ = φ⁻³/(2π) conjecture connects to the EW series.**
The conjectured amplitude A₅ = φ⁻³/(2π) involves φ⁻³ — the same geometric dilution factor that governs the electroweak boson masses (EW-1 through EW-4). If proved, this would establish a direct quantitative connection between the CPP superdeterministic correction to Bell correlations and the CPP electroweak mass scale. Both would follow from the same 600-cell volume ratio φ⁻³, derived without free parameters in the EW series.

---

## Part 4: The Research Programme

**Step 3 — The available mathematical tools.**
SD-5 identifies four techniques from existing CPP results that can be brought to bear on the K₀ derivation:
1. The Nexus path integral formulation from SD-4 — provides the framework
2. The 600-cell adjacency matrix eigenmodes from QM-5 — provides the lattice basis for expanding λ
3. The sea_strength parameter from SS-1 THEO-SS-6 — provides the DP Sea coupling constant
4. The ZBW partner-switching dynamics from propositions.md — provides the particle hidden-variable model

**Step 4 — The target result.**
When complete, the K₀ derivation will give:

    A₅ = K₀(λ̄) × φ⁻³/(2π)

where λ̄ is the DP Sea configuration averaged over the ZBW cycle, expressed in terms of sea_strength and the 600-cell vertex coordinates. If A₅ = φ⁻³/(2π) is confirmed, the complete CPP Bell prediction will be parameter-free: the angular form from SD-2, the suppression from ε = N_part/N_app, and the amplitude from A₅ will all be fixed by known CPP geometry.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Parts 1–2: what is open and why | §1 (Abstract), §2 (Mathematical Problem) |
| Part 3: amplitude and A₅ conjecture | §5 (A₅ conjecture), §4 (Non-perturbative problem) |
| Part 4: research programme | §3 (Research Programme), §4 |
