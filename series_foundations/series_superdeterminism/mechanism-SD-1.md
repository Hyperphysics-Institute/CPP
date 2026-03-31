# Mechanism — SD-1: The Nexus as a Superdeterministic Hidden-Variable Mechanism

**Paper:** SD-1 (cpp_sd1_nexus_superdeterminism_v1.tex)
**Series:** Foundations (series_foundations/)
**Last updated:** 31 March 2026

*This file provides a sequential cause-and-effect account of the physical mechanisms in SD-1. SD-1 is a position paper and open-problem statement: it identifies the CPP structure that instantiates superdeterminism (the Nexus), establishes the magnitude and angular form of the predicted correction to quantum mechanics, connects to the Hossenfelder programme, and registers the four open problems that the remaining SD papers address. For term definitions see glossary-SD-1.md; for the formal propositions see the paper itself.*

---

## Part 1: The Problem — Bell's Theorem and Its Assumptions

**Step 1 — Bell's theorem rests on two assumptions, not one.**
Bell's 1964 theorem proves that no hidden-variable theory can reproduce all predictions of quantum mechanics *if* the theory satisfies two conditions simultaneously: (a) locality — the outcome at Alice's detector depends only on the local hidden variable λ and Alice's setting θ_A, not on Bob's distant setting θ_B; and (b) statistical independence — the hidden variable λ is uncorrelated with the measurement settings:

    ρ(λ | θ_A, θ_B) = ρ(λ)

Under these two conditions, the CHSH inequality |S| ≤ 2 must hold. Quantum mechanics predicts |S|_max = 2√2, and experiments confirm this to precision ~10⁻³. Most physicists interpret this as ruling out hidden-variable theories. But it rules out only theories satisfying *both* conditions.

**Step 2 — Superdeterminism denies statistical independence.**
Bohmian mechanics escapes Bell's theorem by violating locality (the guiding equation is non-local). Superdeterminism escapes by violating statistical independence: if the particle state λ at the time of entanglement is correlated with the future detector orientations θ_A, θ_B — because both are determined by the same deterministic dynamics — then Bell's theorem does not apply. The distribution becomes:

    ρ(λ | θ_A, θ_B) = ρ(λ) × [1 + K(λ, θ_A, θ_B)]

where K is the Nexus correlation function. K = 0 recovers standard QM.

**Step 3 — Superdeterminism without a mechanism is empty.**
Bell himself dismissed superdeterminism as a "conspiracy theory" because it requires a cosmic coincidence: the particle state must be correlated with the experimenter's choice made potentially billions of years later. Without a mechanism explaining this correlation, the proposal is unfalsifiable metaphysics. The CPP contribution is to provide the mechanism.

---

## Part 2: The CPP Hidden-Variable Structure

**Step 4 — The hidden variables in CPP are the DP Sea configurations.**
In CPP, every measurement outcome is determined by the configuration of the Dipole Sea at the time of the interaction. The hidden variable λ for an entangled pair is the joint DP Sea state of the two particles and all the hDP structures mediating their interaction:

    λ = {ρᵢ, φᵢ, sᵢ}_{i ∈ N_pair}

where ρᵢ is the DI-bit density, φᵢ is the phase, and sᵢ is the spin orientation at each Grid Point i in the causal neighbourhood N_pair. Standard quantum mechanics averages over this distribution — quantum probabilities arise from ignorance of λ, not from fundamental randomness.

**Step 5 — CPP is local at the interaction level.**
The SSV mechanism is local: the SSV at each Grid Point depends only on the DP Sea density and gradient at that point and its 12 nearest neighbours (the 600-cell vertex coordination number z = 12). No instantaneous action at a distance is required for any individual interaction. The apparent non-locality of entanglement arises from the fact that the hidden variables λ were set at the time of entanglement to be correlated across both particles — because the two particles shared a common causal past in which their DP Sea states were jointly constrained by the Nexus.

**Step 6 — The Nexus violates statistical independence.**
The Nexus enforces global DI-bit conservation: Σᵢ δbᵢ = 0 across the entire lattice at every Absolute Moment. The apparatus is a macroscopic collection of ~10²⁶ eCPs embedded in the same lattice. Its orientation θ is a collective degree of freedom of those eCPs. The Nexus constrains both the particle's DP Sea state λ and the apparatus's DP Sea state simultaneously — they are not independent because they are both constrained by the same global conservation law. This is the precise statement of why CPP is superdeterministic:

    ρ(λ | θ_A, θ_B) ≠ ρ(λ)

The correlation is not a signal; it is a constraint — of the same logical type as conservation of energy. Conservation laws correlate apparently distant events atemporally without being conspiratorial.

---

## Part 3: Three Constraints on the Nexus Correlation Function

**Step 7 — K has zero mean over hidden variables.**
The Nexus correlation function K(λ, θ_A, θ_B) satisfies:

    ∫ K(λ, θ_A, θ_B) ρ(λ) dλ = 0

This is required by normalisation: averaging over hidden variables must recover the standard QM distribution. The Nexus shifts the hidden-variable distribution but does not change the total probability.

**Step 8 — K is bounded by the participation fraction.**
The magnitude of K satisfies:

    |K(λ, θ_A, θ_B)| ≲ N_part / N_app

The Nexus distributes the DI-bit conservation constraint over all Grid Points. The pair contributes N_part ~ 1 and the apparatus contributes N_app ~ 10²⁶. The fractional influence of the pair on the apparatus state scales as N_part/N_app ~ 10⁻²⁶ — the participation fraction ε.

**Step 9 — K factorises into hidden-variable and angular parts.**
The 600-cell's H₄ symmetry (order 14,400) forces K to factorise:

    K(λ, θ_A, θ_B) = K₀(λ) × f_{H₄}(θ_A − θ_B)

where K₀(λ) depends only on the hidden variables and f_{H₄} is a function with the icosahedral H₄ symmetry of the 600-cell. The factorisation follows from the covariance of the Nexus constraint under H₄ rotations: the apparatus orientation θ enters only through the relative angle θ_A − θ_B, which the Nexus "sees" through the relative orientation of the two detector subgraphs in the lattice.

---

## Part 4: Order-of-Magnitude Estimates

**Step 10 — The participation fraction gives ε ~ 10⁻²⁶.**
For a standard loophole-free Bell test with two photons measured by macroscopic polarisers:

    N_part = 2        (two photons)
    N_app ~ 10²⁶     (atoms in detector)
    ε = N_part/N_app ≈ 2 × 10⁻²⁶

The correction to the CHSH parameter is:

    |δS|_CPP ≈ ε × S_QM ≈ 2 × 10⁻²⁶ × 2√2 ≈ 5.7 × 10⁻²⁶

This is 22 orders of magnitude below the current best experimental precision of |δS|_exp ~ 10⁻³ (Li et al. 2018).

**Step 11 — A naive Planck-scale estimate gives a much smaller number.**
The alternative estimate using the de Broglie wavelength:

    ε_Planck ~ (l_P / λ_dB)² ~ (1.6 × 10⁻³⁵ / 8 × 10⁻⁷)² ~ 4 × 10⁻⁵⁸

This is 32 orders smaller than the participation fraction estimate. The two estimates bracket the true answer from below (ε_Planck) and above (ε_Nexus). The full derivation (SD-4, SD-5) will determine which is correct.

**Step 12 — Quantum processors offer an enhanced regime.**
A quantum processor with N_q qubits has all N_q qubits forming a single quantum system simultaneously participating in the Nexus constraint:

    ε_QP = N_q / N_substrate

For N_q = 1000: ε_QP ~ 10⁻²³. For N_q = 10⁶: ε_QP ~ 10⁻²⁰. Quantum processors can also scan θ continuously, accessing the H₄ angular structure that the standard CHSH protocol misses.

---

## Part 5: The 600-Cell Angular Signature

**Step 13 — The correction has a specific angular structure at golden-ratio angles.**
The angular function f_{H₄}(θ) has extrema at the special angles of the 600-cell lattice, determined by the H₄ symmetry group:

    θ ∈ {31.7°, 36°, 58.3°, 67.5°, 72°, 120°, ...}

These are the angles where the icosahedral 5-fold structure and tetrahedral 3-fold structure of the 600-cell produce simultaneous extrema. The correction vanishes at generic angles between these special values.

**Step 14 — The CHSH-optimal angle 45° is not H₄-special.**
The CHSH inequality is maximally violated at θ = 45°. This angle is not a special angle of the 600-cell: cos(45°) = 1/√2 ∉ ℚ(φ), where ℚ(φ) is the golden-ratio field in which all 600-cell vertex coordinates lie. The standard CHSH test therefore samples f_{H₄} at its least informative points. This is the CHSH blind spot — formalised as a theorem in SD-2.

**Step 15 — The angular signature is falsifiable even if the magnitude is unknown.**
The prediction is not merely "a small correction exists" — it is "a small correction exists with specific icosahedral angular structure." The ratio δE(36°)/δE(120°) ≈ −1.065 is amplitude-independent: it tests the angular shape alone. If any deviation from −cos θ is ever detected, the ratio distinguishes CPP from all other models.

---

## Part 6: Connection to the Hossenfelder Programme

**Step 16 — CPP provides the geometric structure Hossenfelder identifies as necessary.**
Hossenfelder (2024) argues three things: (a) a preferred time direction eliminates causality paradoxes; (b) quantum mechanics resembles the Liouville equation of statistical mechanics, suggesting it is statistical over hidden variables; (c) quantum computers will produce anomalies consistent with hidden variables. CPP has specific counterparts: (a) the DP Sea rest frame provides the preferred slicing; (b) the DP Sea phase-space distribution plays the role of the Liouville distribution; (c) the five-property CPP signature (SD-4) is the specific anomaly to look for.

This is not analogy — CPP provides the geometric structure that Hossenfelder's programme identifies as necessary but does not specify.

---

## Part 7: The SD Series Plan

**Step 17 — Four open problems define the remaining work.**
SD-1 registers four open problems that structure the rest of the series:

    OPEN-P-SD-1: Derive K(λ, θ_A, θ_B) from first principles → SD-4
    OPEN-P-SD-2: Apparatus model: derive N_app-dependence of ε → SD-3
    OPEN-P-SD-3: Amplitudes A₅, A₃ of f_{H₄} → SD-2, SD-5
    OPEN-P-SD-4: Decoherence threshold for Nexus visibility → SD-3

The papers are logically sequential: SD-2 derives the angular form (pure group theory), SD-3 models the apparatus (thermodynamics), SD-4 derives the correlation function in exact limits (path integral), SD-5 addresses the remaining amplitude derivation (research agenda).

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–3: Bell's theorem and the superdeterminism loophole | §1 (Introduction), §1.1 (Connection to Hossenfelder) |
| Steps 4–6: CPP hidden-variable structure | §2 (CPP Hidden-Variable Structure), Eq. 1–3 |
| Steps 7–9: three constraints on K | §3 (Open Problem), Proposition 1, Eq. 4–6 |
| Steps 10–12: magnitude estimates | §4 (Order-of-Magnitude Estimates), Eq. 7–9 |
| Steps 13–15: angular signature | §5 (600-Cell Angular Signature), Table 1, Prediction 1 |
| Step 16: Hossenfelder connection | §6 (Relation to Hossenfelder) |
| Step 17: open problems | §7 (Consolidated Open Problems) |
