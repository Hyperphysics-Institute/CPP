# Capotauro Mechanism — Paper Outline (v0.1 draft target)

**Location:** `flagship_papers/capotauro/capotauro_outline.md`
**Status:** OUTLINE v0.1 — Session 104 (Patch 0398, 16 May 2026)
**Purpose:** Section-by-section structure for the Capotauro flagship paper packaging the Sessions 87-102 sub-claim (c) v1.0 closure trajectory into publication-grade form.
**Companion sketches:** `sketches/Capotauro_chi_phi_closure.md` (parent, 681 lines) and `sketches/Capotauro_subclaim_c_wigner_eckart.md` (sub-claim (c) working sketch, 2146 lines).
**Theorem-registry anchor:** THEO-CAP-1 (Composite Capotauro Wigner-Eckart Theorem; theorem #62 in SF-Line section per Patch 0397).
**Target ship:** v1.0 in approximately 10 sessions of v0.x drafting following SF-4 cadence.

---

## Strategic context

The Capotauro paper presents the v1.0 closure of OPEN-SM-4 sub-claim (c) — the Composite Capotauro Wigner-Eckart Theorem — to external audience. The closure was achieved across 16 sessions (Sessions 87-102, Patches 0381-0396), formally registered Session 103 Patch 0397 as THEO-CAP-1, and delivers one programme-level empirical prediction (Δp_LR = χ/6 ≈ 0.0394) validated within 2% of observed ~0.04.

**Why ship now**: Sub-claim (c) is closed at theorem level with end-to-end numerical verification to machine precision; the empirical prediction is validated; the foundational inputs are fully enumerated (FI-C-1 through FI-C-10); the open questions (sub-claims (a), (b), Q11 sin²θ₁₃, FI-C-10 first-principles) are honestly scoped as post-v1.0 work. Multi-reviewer convergence on SF-4 and SS-9 demonstrated that working sketches surface what external review does not catch and vice versa — paper drafting is the discipline that locks in v1.0 substance and opens the door to external feedback.

**What this paper does NOT close**: Capotauro sub-claim (a) Capotauro nucleation event; sub-claim (b) substrate-vacuum symmetry-breaking dynamics; Q11 sin²θ₁₃ derivation from |M| = χ/6 (re-scoped to SF-2 v2.0+); FI-C-10 first-principles verification (registered for SS-corpus territory). These are explicit in §9 of the paper.

**Position in SF-line**: The Capotauro paper is the third flagship paper to ship at v1.0 after SF-4 (Session 54) and SF-2 (Session 83); the first flagship paper not in the SF-N numbering convention; the first paper to register a programme-level theorem (THEO-CAP-1) ahead of its own publication (registered Session 103 Patch 0397, three patches before its outline).

---

## Headline claim (draft v0.1 — refine before §0 abstract drafting)

**CPP derives the chirality matrix element |M| = χ/6 = φ⁻³/6 ≈ 0.0394 on the K3-doublet at theorem level from substrate-vacuum broken-symmetry physics, with the parity-violation asymmetry prediction Δp_LR ≈ 0.0394 validated within 2% of observed ~0.04 — zero free parameters, conditional theorem closure on FI-C-1 through FI-C-10 + 4 CPP axioms (A1, A3, A4, A7).**

**Refined draft after multi-reviewer convergence**: TBD.

**Plain-language version** (for abstract second paragraph): The Capotauro mechanism is the substrate-physics machinery that produces parity-violation in the electroweak sector of CPP. The theorem derives, from a substrate-vacuum chirality magnitude χ = φ⁻³ ≈ 0.236 set by the broken-symmetry order parameter of the H₄ → I₄ chirality ℤ₂, the chirality matrix element |M| = χ/6 ≈ 0.0394 on the K3-doublet of charged-lepton substrate states. This matrix element directly predicts the parity-violation asymmetry Δp_LR ≈ 0.04 observed empirically. The eight-step proof gathers structural results across sixteen sessions of derivation (Sessions 87-102) and matches to machine precision at every numerical checkpoint.

---

## Falsifiers (cumulative falsifier set for v1.0 paper)

The paper commits to falsifiers spanning direct empirical, structural, and framework-level categories. Five candidates for v1.0 ship:

1. **Δp_LR observed outside ±2% of χ/6 ≈ 0.0394** (direct empirical) — would falsify Theorem 18.1 / THEO-CAP-1 at the level of the matrix-element prediction. Current empirical state: observed ~0.04, agreement within 2%.

2. **K3-doublet basis structure (FI-C-3 extended)** revealed to be incorrect at theorem level after independent re-derivation — would falsify the chirality observable's |χ_±⟩ ζ-parity decomposition that underlies the matrix-element calculation.

3. **Substrate-vacuum chirality magnitude χ ≠ φ⁻³** (framework-level) — would falsify FI-C-9. The empirical anchor for χ = φ⁻³ ≈ 0.236 is the natural distance-ratio bias of the broken H₄ → I₄ phase plus consistency with multiple downstream observables. A χ value inconsistent with this magnitude (say, 0.5 or 0.1) would require either redefining FI-C-9 or falsifying the framework.

4. **Cage-shell extension to chirality observables (FI-C-10) ruled out** by independent derivation — would falsify the m_⊥ = 1/6 cage-shell averaging factor that combines with the K3-amplitude factor to give |M| = χ/6. The FI-C-10 verification work (open, registered) is itself a falsification opportunity.

5. **Cross-sector inconsistency**: any observable predicted in SF-2 or SF-4 that depends on the Capotauro chirality input |M| = χ/6 must remain consistent. A future SF-2 v2.0+ derivation of sin²θ₁₃ that yields a value contradicting observation while using the χ = φ⁻³ + cage-shell-averaging input would falsify the framework end-to-end.

**Notable absences from falsifier set**: sin²θ₁₃ deviation is *not* a Capotauro falsifier (per Session 101 re-scoping; Q11 belongs to SF-2 v2.0+); δ_CP and η_B deviations are not v1.0 falsifiers (those are downstream observables to be derived in future Capotauro sub-claims (a), (b) work).

---

## Section-by-section outline

### §0 Abstract

Three-paragraph structure following SS-9 / SF-4 / SF-2 v1.0 convention:

- Paragraph 1: **Headline claim** (the |M| = χ/6 result and Δp_LR validation).
- Paragraph 2: **Plain-language summary** (substrate-vacuum chirality magnitude χ = φ⁻³; chirality observable on K3-doublet; eight-step proof; cross-sector inheritance).
- Paragraph 3: **Honest scope** (sub-claim (c) only; sub-claims (a), (b), Q11 sin²θ₁₃ explicitly out of scope; conditional theorem closure on FI-C-1 through FI-C-10 + 4 CPP axioms).

Length: ~250 words. SF-4 v1.0 style with strict-C inheritance discipline.

### §1 Introduction and strategic frame

- **§1.1 The Capotauro problem in CPP**: parity violation in the electroweak sector requires a substrate-level chirality mechanism; the historical Abshier/Grok 2025 paper proposed the framework but did not derive |M| at theorem level. This paper closes that gap for sub-claim (c).
- **§1.2 What this paper delivers**: Theorem 18.1 (Composite Capotauro Wigner-Eckart Theorem) at conditional theorem closure level on 10 FIs + 4 CPP axioms; primary empirical prediction Δp_LR = χ/6 validated within 2%; foundational input FI-C-10 (cage-shell extension to chirality observables) registered in trajectory.
- **§1.3 What this paper does NOT deliver**: sub-claim (a) Capotauro nucleation event; sub-claim (b) substrate-vacuum dynamics; Q11 sin²θ₁₃ derivation (re-scoped to SF-2 v2.0+); FI-C-10 first-principles verification.
- **§1.4 Position in the SF-line and broader programme**: third flagship paper to ship at v1.0; first non-SF-N flagship; first theorem-registered ahead of publication.
- **§1.5 Cross-sector entanglement structure**: the closure has compounding value across SM-2, SM-4, SM-5, SF-2, SF-4 simultaneously — this is the strongest argument for prioritization of Capotauro work.
- **§1.6 Strict-C inheritance discipline**: how the paper distinguishes claims at theorem level, claims at FI-inherited level, and claims at structural-argument level.

Length: ~3-4 pages source.

### §2 Substrate-vacuum broken-symmetry physics

The foundational physics underlying the Capotauro mechanism. Inherits from parent sketch §1.2 + §1.3 + §1.7.

- **§2.1 The H₄ → I₄ chirality ℤ₂**: the 600-cell substrate's full symmetry group H₄ has order 14400 with rotational subgroup I₄ of order 7200 (index 2); the racemic geometric structure with chirality ℤ₂ as the broken symmetry.
- **§2.2 FI-C-9 substrate-vacuum order parameter**: |χ| = φ⁻³ ≈ 0.236 as the natural distance-ratio bias of the broken H₄ → I₄ phase; sign of χ as frozen boundary condition; universality of empirical chirality across scales.
- **§2.3 The χ = φ⁻¹ vs χ = φ⁻² vs χ = φ⁻³ inconsistency**: historical resolution at φ⁻³ via the natural distance-ratio bias of the broken phase (Session 87 reframing decision); methodological note on spontaneous-symmetry-breaking framing vs postulated-initial-bias framing.
- **§2.4 The empirical anchor**: parity-violation in the electroweak sector at the Δp_LR ≈ 0.04 scale; cosmological context (CEERS U-100588 / Gandolfi et al. 2025) as supportive but not load-bearing.

Length: ~4-5 pages source.

### §3 The K3-doublet and the chirality observable

The Wigner-Eckart machinery setup. Inherits from sub-sketch §3-§11.

- **§3.1 K3 base structure and four-cage taxonomy (FI-C-2)**: K₃ = {V₁, V₂, V₃} equilateral triangle; SM-1 four-cage taxonomy (V = 4, 12, 20, 30).
- **§3.2 K3-doublet TBM-aligned basis (FI-C-3)**: {|φ₋⁽¹⁾⟩, |φ₋⁽²⁾⟩} from the standard S₃ → S₂ branching rule (inherited from SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem).
- **§3.3 The perpendicular wavefunction structure |χ_±⟩** (Session 91 extension): K3-doublet basis states extended over perpendicular direction with |χ_±⟩ as ζ-parity-decomposed substrate orientation field; ζ-EVEN/ODD components and the σ_1ζ-EVEN pairing convention.
- **§3.4 The chirality observable** Ĉ_χ: substrate-level operator; irrep B₂ of K3 stabilizer D₆ = S₃ × ℤ₂; ζ-ODD by Finding C-W11; identification of |χ_±⟩ as ζ-parity-decomposed substrate orientation field at K3 location.
- **§3.5 Full K3-doublet basis states**: |Φ₋⁽ⁱ⁾⟩ = |φ₋⁽ⁱ⁾⟩ ⊗ |χ_i⟩.

Length: ~4-5 pages source.

### §4 The D₆ stabilizer and Wigner-Eckart framework

The structural framework that makes the matrix-element calculation possible.

- **§4.1 The K3 stabilizer D₆ = S₃ × ℤ₂** (Findings C-W5, C-W6): full D₆ structure on K3-doublet space.
- **§4.2 The chirality-preserving subgroup S₃' identification** (Finding C-W7): correcting the §3.1 informal "D₆ → C₆" framing.
- **§4.3 Irreducible representations of D₆**: B₂ for the chirality observable; E-doublet for the cage-shell wavefunction.
- **§4.4 Wigner-Eckart on D₆**: matrix elements of B₂ operators on E-doublet states; the K3-amplitude × perpendicular-direction product structure.
- **§4.5 The σ_1-ODD operator parameterization correction** (Session 95): the unique A₂-irrep generator T_{A₂}(b) = i·b·S where S is real antisymmetric with cross-product-with-(1,1,1) structure; eigenvalues {0, ±b√3} on K3-amplitudes.

Length: ~4-5 pages source.

### §5 The Composite Capotauro Wigner-Eckart Theorem (Theorem 5.1 of paper = Theorem 18.1 of working sketch)

**The flagship result**. Inherits from sub-sketch §18 Theorem 18.1.

- **§5.1 Theorem statement**: |M| = |⟨Φ₋⁽¹⁾|Ĉ_χ|Φ₋⁽²⁾⟩| = χ/6 = φ⁻³/6 ≈ 0.0394.
- **§5.2 Eight-step proof**: gathered from Sessions 88-97 (Patches 0381-0391).
  - **§5.2.1 Chirality-eigenvalue matching factor |M_{K₃}| = χ** (Session 96): derivation of b = χ/√3 via the chirality-eigenvalue matching principle.
  - **§5.2.2 Cage-shell averaging factor |M_⊥| = 1/6** (Session 97): derivation via d_E/V_cage = 2/12 by Schur orthogonality, requiring FI-C-10.
  - **§5.2.3 Composite product**: |M| = |M_{K₃}| · |M_⊥| = χ · (1/6) = χ/6.
- **§5.3 Numerical verification**: end-to-end match to machine precision 10⁻¹⁷; all intermediate quantities verified.
- **§5.4 Foundational inputs and axiom accounting**: 10 FIs (FI-C-1 through FI-C-10) + 4 CPP axioms (A1, A3, A4, A7); A3 + A7 most load-bearing per Picture B substrate-orientation-field framework.
- **§5.5 Connection to SF-4 v4.0 Composite K3-Cage-Shell Coupling Theorem (THEO-SF-4-5)**: the cross-sector inheritance pattern; FI-C-3 + FI-C-10 as the load-bearing inheritance bridges.

Length: ~6-8 pages source. This is the longest section in the paper.

### §6 Primary empirical prediction: Δp_LR = χ/6

The empirical capstone. Direct consequence of Theorem 5.1.

- **§6.1 The parity-violation asymmetry on K3-doublet measurements**: Δp_LR = |M| from the standard Wigner-Eckart interpretation of chirality-observable expectation values.
- **§6.2 Predicted value**: Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394.
- **§6.3 Observed value**: Δp_LR ≈ 0.04 (empirical anchor from Abshier/Grok 2025 + cosmological constraints).
- **§6.4 Agreement**: within 2%.
- **§6.5 What "within 2%" means**: the empirical anchor 0.04 is itself a back-derivation from η_B ≈ 6×10⁻¹⁰ via leptogenesis (not a direct measurement of parity-violation asymmetry on K3-doublet states); the 2% agreement is therefore a consistency check at the structural-numerical level, not a precision test. Honest framing required.

Length: ~3-4 pages source.

### §7 sin²θ₁₃ posture (re-scoped to SF-2 v2.0+)

The most consequential re-scoping decision in the trajectory. Inherits from sub-sketch §20 + §21.

- **§7.1 The Sessions 99-101 trajectory**: candidate γ numerical observation sin²θ₁₃ = b · m_⊥ = χ/(6√3) ≈ 0.0227 matches observation within 1σ but lacks rigorous derivation.
- **§7.2 The linear-vs-quadratic scaling tension**: standard PMNS perturbation predicts quadratic scaling ∝ |M|² ≈ 0.001 (off by factor 21); wavefunction-level coupling also gives quadratic (off by factor 64); 22 candidate scalings tested, none match.
- **§7.3 Re-scoping decision**: Q11 sin²θ₁₃ derivation moved to SF-2 v2.0+ scope. Capotauro mechanism provides |M| = χ/6 as chirality coupling input; precise relation |M| → sin²θ₁₃ is the SF-2 framework's responsibility.
- **§7.4 The numerical conjecture**: candidate γ registered as structural observation to guide SF-2 v2.0+ work. Whether candidate γ is structurally meaningful or numerical coincidence is the open question for SF-2.
- **§7.5 Why this is honest scope-limitation**: the alternative would be ansatz-fitting a CPP-specific perturbation framework that produces linear scaling without independent structural motivation; that would be derivation in name only.

Length: ~3-4 pages source. Critical section for reviewer-honesty.

### §8 Cumulative falsifier

Full enumeration with experimental references and threshold definitions.

- **§8.1 Direct empirical falsifiers**: (1) Δp_LR outside ±2% of χ/6; (2) FI-C-9 chirality magnitude inconsistency.
- **§8.2 Framework-level falsifiers**: (3) FI-C-3 K3-doublet basis structure error; (4) FI-C-10 cage-shell extension ruled out by independent derivation; (5) cross-sector inconsistency with SF-2/SF-4 predictions.
- **§8.3 Modular falsification scenarios**: how partial failure modes affect the framework's residual claims.
- **§8.4 Notable absences**: sin²θ₁₃ deviation is NOT a Capotauro falsifier; δ_CP and η_B deviations are NOT v1.0 falsifiers (downstream observables in future sub-claims (a), (b) work).

Length: ~2-3 pages source.

### §9 Open theorem-level work

Honest open-problem registry. Inherits from sub-sketch §22.7 + parent sketch §1.8.

- **§9.1 Sub-claim (a) Capotauro nucleation event**: derivation of the specific substrate-dynamical primitive that selects the broken phase from the symmetric phase. Cosmological timing question (legacy "120 Myr post-Big Bang" figure) is downstream.
- **§9.2 Sub-claim (b) substrate-vacuum symmetry-breaking dynamics**: derivation of the H₄ → I₄ chirality ℤ₂ symmetry-breaking dynamics; foundational substrate-physics territory; intersects with OPEN-FP-SS-* work.
- **§9.3 Q11 sin²θ₁₃ derivation (re-scoped to SF-2 v2.0+)**: the highest-consequence post-v1.0 target; candidate γ numerical conjecture as guiding structural observation; CPP-specific perturbation framework development required.
- **§9.4 FI-C-10 first-principles verification**: derivation from primitive CPP axioms (A3 DI-bit propagation + A4 Nexus connectivity); SS-corpus territory.
- **§9.5 Roadmap to v2.0+**: priority order, estimated timeline, decision points.

Length: ~3-4 pages source.

### §10 Discussion

Programme context, cross-sector connections, methodological observations.

- **§10.1 Programme-level pattern**: pattern strength at integer counts and substrate primitives is the load-bearing signal across the CPP corpus (SS-7 twelve nuclei to 1.5%, SM-9 top quark to 0.02%, SF-4 σ_ν to 2%, Capotauro Δp_LR to 2%) — not multi-decimal-place fitting precision.
- **§10.2 Cross-sector implications**: Capotauro's role in providing chirality coupling to SF-2 (CHIR closure), SF-4 (δ_CP forced consequence), SM-2 (qDP/eDP charge asymmetry), SM-4 (this paper), SM-5 (PMNS sector via SF-2 v2.0+ Q11 work).
- **§10.3 Methodological observation — first programme-level theorem registered ahead of paper publication**: THEO-CAP-1 registered Session 103 Patch 0397 before the paper outline (Session 104 Patch 0398, this work); methodological pattern for theorem-registry registration from sub-claim closure trajectories via working sketches.
- **§10.4 Methodological observation — Tier 4 reasoning recovery enabled the closure**: the Sessions 87-102 trajectory was made possible by Tier 4 reasoning capture across patches 0024-0028 (recovery of foundational SR-1 / EW-1 / SS-1 / QM-1 / SM-1 reasoning); without that recovery, the FI-C-9 + FI-C-10 + the eight-step proof would not have converged.
- **§10.5 Outlook**: 2026-2032+ experimental landscape relevant to Capotauro predictions; JUNO precision measurements; LHC precision electroweak; cosmological μ-distortion bounds.

Length: ~4-5 pages source.

### §11 References

Bibliography target: ~25-30 entries. Categories:

- **CPP-internal flagship references**: SM-1, SM-2, SM-3, SM-4, SM-5, SF-2, SF-4, SS-1, SS-9; theorem-registry; axiom-registry; Research_Frontier.
- **Capotauro historical references**: Abshier/Grok 2025 (the originating informal paper); CEERS U-100588 / Gandolfi et al. 2025 (cosmological anchor).
- **Wigner-Eckart machinery and group theory**: Wigner 1931; Tinkham group theory; Hamermesh group theory.
- **PMNS framework**: NuFIT 6.0 + Esteban et al. arXiv:2410.05380; standard PMNS references.
- **Substrate-physics historical**: Coxeter 1973 (polytope theory); Steinitz 1922 (polytope realization); Freudenthal-van der Waerden 1947 (deltahedra).
- **Empirical anchors**: Planck 2018 (cosmological parameters); PDG 2024 (precision electroweak); JUNO 2025 (arXiv:2511.14593 if available).

Length: ~3-4 pages source.

---

## Predictions table (master, for §6 + cross-reference)

| Observable | Predicted | Empirical anchor | Match | Status |
|:---|:---:|:---:|:---:|:---:|
| **|M| chirality matrix element on K3-doublet** | χ/6 = φ⁻³/6 ≈ 0.0394 | n/a (theoretical intermediate) | n/a | THEOREM at v1.0 (Theorem 5.1) |
| **Δp_LR parity-violation asymmetry** | χ/6 ≈ 0.0394 | ~0.04 (Abshier/Grok 2025 back-derivation from η_B) | within 2% | **PRIMARY EMPIRICAL PREDICTION at v1.0** |
| **sin²θ₁₃** | not derived in this paper | 0.02220 ± 0.00069 (NuFIT 6.0) | n/a | RE-SCOPED to SF-2 v2.0+ (Q11) |
| **δ_CP** | not derived in this paper | 195° ± 40° (NuFIT 6.0) | n/a | DOWNSTREAM (sub-claims (a), (b)) |
| **η_B baryon asymmetry** | not derived in this paper | 6.12×10⁻¹⁰ (Planck 2018) | n/a | DOWNSTREAM (sub-claims (a), (b)) |

**Single primary empirical prediction at v1.0**: Δp_LR ≈ 0.0394 within 2% of observed ~0.04. All other Capotauro observables (sin²θ₁₃, δ_CP, η_B) are registered as out-of-scope at v1.0 with explicit cross-references to where they're closed (SF-2 v2.0+ for sin²θ₁₃; future Capotauro sub-claims for δ_CP and η_B).

---

## Source material map

| Section | Primary source(s) | Status |
|:---|:---|:---|
| §0 Abstract | TBD v0.1 drafting | New |
| §1 Introduction | Parent sketch §1.1–§1.6; this outline §strategic context | Synthesis |
| §2 Substrate-vacuum broken-symmetry | Parent sketch §1.2 + §1.3 (FI-C-9) + §1.7 | Synthesis |
| §3 K3-doublet + chirality observable | Sub-sketch §3-§11; parent sketch §1.3 (FI-C-3) | Synthesis |
| §4 D₆ stabilizer + Wigner-Eckart | Sub-sketch §9, §12, §15 | Synthesis |
| §5 Theorem 5.1 | Sub-sketch §18 (Theorem 18.1) + §22 (closure summary) | Direct port + reformatting |
| §6 Δp_LR prediction | Sub-sketch §22.4; parent sketch §1.8 | Synthesis |
| §7 sin²θ₁₃ posture | Sub-sketch §19, §20, §21 | Direct port + reformatting |
| §8 Cumulative falsifier | This outline §falsifiers | Direct |
| §9 Open work | Sub-sketch §22.7 + parent sketch §1.8 | Synthesis |
| §10 Discussion | Parent sketch §1.5 + Research_Frontier §forward queue | New synthesis |
| §11 References | Multiple flagship papers + external | Synthesis |

---

## Inheritance / dependencies

The paper inherits structurally from:

- **SM-1** (four-cage taxonomy; THEO-SM-1 charge quantization; THEO-SM-3 K₃ spectral theorem). All at theorem level.
- **SM-3** (K₃ spectral theorem; THEO-SM-3). At theorem level.
- **SM-4** (e/μ/τ charged-lepton K3-vertex identification). Foundational input for FI-C-3.
- **SM-5** (TBM zeroth order; THEO-SM-5 PMNS structural impossibility theorem; op:nu_id RESOLVED cross-sector via SF-4 v4.0). At theorem level via cross-sector closure.
- **SF-2 v1.0** (W bracelet D₆ stabilizer THEO-SF-2-1; W⁰ catalyst framework PROP-SF-2-1 through PROP-SF-2-6). At theorem level.
- **SF-4 v4.0+** (Composite K3-Cage-Shell Coupling Theorem THEO-SF-4-5; first cross-sector closure in CPP). At conditional theorem closure level. Critical inheritance for FI-C-3 (TBM-aligned basis at theorem level).

The paper does NOT inherit from:
- SS-corpus papers (SS-7, SS-8, SS-9). Capotauro is electroweak-sector work, not strong-sector.
- QM-corpus papers (QM-1 through QM-5). Capotauro is substrate-physics + group-theoretic, not foundational QM.
- SD-corpus papers (SD-1 through SD-5). Capotauro is structural, not superdeterminism work.

---

## Pre-emptive reviewer concerns

Items the v0.x drafting cycle and AI review passes will likely surface. Each registered here for explicit treatment at v0.1+ drafting time.

1. **FI-C-9 derivability**: reviewers will ask "is FI-C-9 a foundational postulate or a derivable structural fact?". Honest answer: postulate at v1.0; derivation in OPEN-SM-4 sub-claims (a), (b) territory. Treatment: explicit §2.2 + §9.1 + §9.2.

2. **FI-C-10 derivability**: reviewers will ask "where does the cage-shell extension to chirality observables come from?". Honest answer: postulate at v1.0; derivation from A3 + A4 in OPEN-SS-* territory. Treatment: explicit §3.5 + §9.4.

3. **|M| = χ/6 vs candidate γ tension**: reviewers will ask "you have χ/6 ≈ 0.0394 matching Δp_LR within 2%, and χ/(6√3) ≈ 0.0227 matching sin²θ₁₃ within 1σ — is the second match accidental or structurally meaningful?". Honest answer: open question for SF-2 v2.0+; current state is candidate γ is registered as structural observation pending derivation. Treatment: explicit §7.4.

4. **Cross-sector inheritance complexity**: reviewers will ask "the inheritance chain SM-1 + SM-4 + SF-2 + SF-4 is dense; can the closure be evaluated without re-deriving all four flagship papers?". Honest answer: yes — the inheritances are clearly demarcated as FIs in §3.2 (FI-C-3) + §3.5 (FI-C-10) + §4.1 (FI-C-4). The closure is structurally local to the K3-doublet + chirality observable framework once the FIs are accepted. Treatment: explicit §5.5.

5. **The "back-derivation" provenance of Δp_LR ≈ 0.04**: reviewers will ask "is 0.04 a measurement or a back-derivation from η_B?". Honest answer: back-derivation. Treatment: explicit §6.5 + §8.

6. **The σ_1-ODD parameterization correction (Session 95)**: reviewers may flag the Session 93 → Session 95 correction as a sign of fragile early work. Honest answer: the correction was caught and fixed in trajectory; the v1.0 result is structurally clean. Treatment: §4.5 + brief mention in §10.4.

7. **Naming convention THEO-CAP-N**: reviewers will ask "why CAP and not SF-N?". Honest answer: Capotauro is flagship-paper-pending and outside the SF numerical sequence; THEO-CAP-N naming reflects this status. Treatment: explicit §10.3.

8. **Sin²θ₁₃ re-scoping in particular** (most likely reviewer concern): reviewers will ask "you originally hoped to derive sin²θ₁₃ and now you're saying it belongs to SF-2 v2.0+ — is this principled or convenient?". Honest answer: principled — the linear-vs-quadratic scaling tension surfaced in Sessions 99-100 cannot be resolved within standard perturbation theory; the Capotauro mechanism's primary empirical content is Δp_LR (validated) and the connection to sin²θ₁₃ requires CPP-specific perturbation framework belonging to SF-2 scope. Treatment: §7 in full.

---

## Drafting plan and timeline

Following the SF-4 (~10 sessions of v0.x drafting) and SS-9 (~14 sessions including polish) cadence patterns:

| Stage | Sessions (estimate) | Deliverable |
|:---|:---:|:---|
| v0.1 .tex foundation | 105-106 | Title block + abstract + §0 + §1 + bibliography stub; ~600-line .tex source |
| v0.2 §2 + §3 development | 107 | Substrate physics + K3-doublet structure full draft |
| v0.3 §4 + §5 development | 108-109 | D₆ Wigner-Eckart + Theorem 5.1 full draft (the longest section) |
| v0.4 §6 + §7 + §8 development | 110 | Predictions + sin²θ₁₃ posture + falsifier full draft |
| v0.5 §9 + §10 + §11 development | 111 | Open work + discussion + references full draft |
| v0.6 integration polish | 112 | Cross-section consistency + version-line cleanup + first PDF compile |
| v0.7 AI review pass 1 incorporation | 113 | ChatGPT v0.6 review on .tex source |
| v0.8 AI review pass 2 incorporation | 114 | CoPilot v0.7 review on .tex source |
| v0.9 AI review pass 3 incorporation | 115 | ChatGPT v0.8 review on .tex source (or Grok) |
| v1.0 SHIP | 116 (estimate) | Multi-reviewer convergence + v1.0 .tex frozen + four-tier documentation suite at v1.0 freeze |

**Total estimated timeline**: ~12-13 sessions from outline lock (Session 104, this work) to v1.0 SHIP. Within the typical SF-line paper drafting envelope.

**Critical dependencies**:
- Outline lock (Session 104, this patch).
- Tier 4 reasoning recovery (carried forward from Sessions 86+).
- Sub-sketch §18 Theorem 18.1 frozen (Session 98 Patch 0392; SOURCE-OF-TRUTH for §5).
- Parent sketch §1.8 closure trajectory summary frozen (Session 103 Patch 0397; SOURCE-OF-TRUTH for §1 + §10).

**Risk factors**:
- Multi-reviewer convergence on §7 sin²θ₁₃ posture might require additional re-framing rounds (the re-scoping decision is reviewer-honesty-sensitive).
- FI-C-9 + FI-C-10 derivability questions might surface during review and require either additional v0.x patches or explicit forward-pointing to sub-claims (a), (b) and SS-corpus work.

---

## What this paper ESTABLISHES vs DOES NOT ESTABLISH

**ESTABLISHES at theorem level**:

- The K3-doublet chirality matrix element |M| = χ/6 = φ⁻³/6 ≈ 0.0394 at conditional theorem closure on 10 FIs + 4 CPP axioms.
- The decomposition |M| = |M_{K₃}| · |M_⊥| where |M_{K₃}| = χ and |M_⊥| = 1/6.
- The chirality-eigenvalue matching principle: b = χ/√3 from spectral radius √3 of the unique A₂-irrep generator's cross-product-with-(1,1,1) structure.
- The cage-shell averaging principle: m_⊥ = 1/6 from d_E/V_cage = 2/12 by Schur orthogonality.
- The empirical prediction Δp_LR = χ/6 ≈ 0.0394 validated within 2% of observed ~0.04.
- FI-C-10 cage-shell extension to chirality observables as a registered foundational input.
- 34 findings (C-W1 through C-W34) documenting the closure trajectory.

**DOES NOT ESTABLISH**:

- The substrate-vacuum broken-symmetry order parameter |χ| = φ⁻³ at theorem level (FI-C-9 postulate; derivation is sub-claim (b) work).
- The substrate-dynamical primitive that selects the broken phase (sub-claim (a) Capotauro nucleation event).
- The PMNS sin²θ₁₃ derivation from |M| = χ/6 (re-scoped to SF-2 v2.0+ Q11).
- The PMNS δ_CP and baryon asymmetry η_B (downstream Capotauro sub-claim work).
- FI-C-10 first-principles closure from primitive CPP axioms (registered for SS-corpus territory).

**HONEST FRAMING**: This is partial closure of OPEN-SM-4. Sub-claim (c) — the chirality matrix element on K3-doublet — is closed at theorem level with empirical validation. Sub-claims (a) and (b) — the nucleation event and substrate-vacuum dynamics — remain open. The OPEN-SM-4 entry in research_frontier.md advances from OPEN to OPEN (PARTIAL CLOSURE) per Session 103 Patch 0397; this paper packages the partial closure for publication.

---

**Outline locked Session 104 Patch 0398.** v0.1 .tex drafting begins Session 105.
