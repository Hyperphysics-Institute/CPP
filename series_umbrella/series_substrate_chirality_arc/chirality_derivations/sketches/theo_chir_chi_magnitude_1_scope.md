# THEO-CHIR-CHI-1: Scope and Precondition Sketch

## Deriving the Substrate Chirality Magnitude χ = φ⁻³ from 600-Cell Geometry

**Patch 0637, Session 148** (29 May 2026)
**Sector:** CHIR (Substrate Chirality Arc) — second downstream derivation target of the audit-spawned OPEN-CHIR-* programme.
**Resolves (in part):** audit entry **E21** (the substrate chirality magnitude χ = φ⁻³) / **OPEN-CHIR-1d**.
**Status of this document:** scope-and-precondition sketch. Unlike the E20 sketch (which scoped a near-complete viability closure), this sketch's primary job is to **map the gap honestly**: χ = φ⁻³ is currently a foundational input (FI-C-9), its *value* has a partial geometric derivation (Capotauro Finding C-3), and the residual gap splits into a near-term-reachable piece and a deep deferred piece. The sketch reserves **THEO-CHIR-CHI-1** for the near-term piece and registers the deep piece honestly as deferred.

---

## §0 Working-session firewall

This sketch plans; it does not prove. It inventories the existing χ = φ⁻³ groundwork, answers the reviewer's standing "why exponent −3?" question at the level the existing work supports, decomposes OPEN-CHIR-1d into two sub-gaps of very different difficulty, and sets a realistic layer expectation. It does **not** upgrade E21's classification (it stays emergent (provisional)); it does **not** eliminate FI-C-9; and it explicitly refuses to treat the supporting numerical signposts (δ_CP, Δp_LR proximities) as derivations.

A correction this sketch makes to the audit record: THEO-CHIR-AUDIT-1 noted E21 as "partially addressed by THEO-CHIR-CONT-1.3's topological-projection argument." That is imprecise. CONT-1.3 establishes magnitude **inheritance** — that the substrate magnitude χ/6 projects through the continuum-limit map Φ preserving magnitude at leading order. It consumes χ; it does not derive χ. The actual partial derivation of the *value* χ = φ⁻³ is Capotauro **Finding C-3** (the distance-ratio calculation, §2.1 below). The audit's note is corrected here, not by re-editing the v1.1-frozen audit, but in this sketch and in CHIR.md.

---

## §1 The question

### §1.1 What E21 is

Audit entry E21 is the substrate chirality magnitude **χ = φ⁻³ ≈ 0.236**, the scalar controlling the substrate's edge-length perturbation (edges aligned with n̂ have effective length 1 + ε·ê·n̂ with |ε| = |χ| = φ⁻³). The audit classified E21 **emergent (provisional)** at v1.1, with proposed handling "derive from n̂ + A2 (OPEN-CHIR-1d)." E21 is the magnitude that the E20 theorem (THEO-CHIR-PCD-ORIENTATION-1) deliberately set aside: it is the F.1 Phase-3 content, not the E20 primitive count.

### §1.2 What OPEN-CHIR-1d asks

> **Derive the value χ = φ⁻³ from n̂ + the 600-cell geometry alone, with no chirality input — eliminating FI-C-9 (the substrate-vacuum broken-symmetry order parameter) as a foundational input.**

This is the target the F.1 sketch itself flagged (§14.17) as a deep long-term ambition: "deriving the chirality scale |χ| = φ⁻³ itself from pure 600-cell polytope geometry and locality constraints, with no chirality input… substantially deeper than the F.1 closure (which still inserts n̂ and |χ| axiomatically)." It is therefore expected to be harder than E20, and this sketch treats it as a **staged** target rather than a single viability closure.

---

## §2 Existing groundwork

### §2.1 The value χ = φ⁻³ has a partial geometric derivation (Finding C-3)

Capotauro Finding C-3 (`capotauro/sketches/Capotauro_chi_phi_closure.md`) derives the value as the **symmetric-bias parameter of the 600-cell's edge-to-first-non-edge distance ratio**. In unit-circumradius normalization the 600-cell edge length is φ⁻¹ (the A5 metric η = ℓ_edge/R_circ = 1/φ). The dimensionless symmetric bias of the φ⁻¹ : 1 length pair is
$$
\chi \;=\; \frac{1 - \varphi^{-1}}{1 + \varphi^{-1}}
\;=\; \frac{\varphi^{-2}}{\varphi}
\;=\; \varphi^{-3} \approx 0.236,
$$
using $1 - \varphi^{-1} = \varphi^{-2}$ (since $\varphi^{-1} = \varphi - 1$, so $1-\varphi^{-1} = 2-\varphi = \varphi^{-2}$) and $1 + \varphi^{-1} = \varphi$. **This is the answer to the reviewer's standing "why exponent −3?" question:** the exponent is $-2 - (-1) \cdot (\text{?})$… concretely, numerator $\varphi^{-2}$ over denominator $\varphi^{+1}$ gives $\varphi^{-3}$. The exponent is not free; it is fixed once the edge-to-first-non-edge symmetric-bias ratio is the chosen generator.

Finding C-3 also **corrects a prior arithmetic error**: the OP-SM-4 archive had derived χ = φ⁻² by dropping one factor of 1/φ in the simplification; the corrected value is φ⁻³. (This is itself a useful provenance datum: the value was error-corrected, not pattern-matched to fit.)

### §2.2 But it is registered as a foundational input (FI-C-9)

Despite the Finding C-3 calculation, χ = φ⁻³ is **registered as FI-C-9** ("substrate-vacuum broken-symmetry order parameter," Session 87, Patch 0381) and consumed as input by THEO-CAP-1, THEO-SD-CHIR-1/2, and the F.1 arc. The reason FI-C-9 retains input status (Capotauro's own statement): the v1.0 closure "*uses* this FI as input rather than deriving it" because **deriving the symmetry-breaking dynamics** — the substrate-dynamical primitive that selects the broken (chiral) phase of $H_4 \to I_4$ from the symmetric phase — is deferred (registered as OPEN-SM-4 ↔ SS-corpus future work). So the value is computed (Finding C-3) but the input status persists because the *selection of the broken phase* is not dynamically derived.

### §2.3 What is established vs. what is open

- **Established (Layer 3):** the identification χ ≡ ε (Capotauro Finding C-W39, the local-$I_h$-preservation theorem) — the chirality magnitude *equals* the substrate edge-perturbation magnitude. The cage-shell factor 1/6 (THEO-CAP-1 / SD-CHIR). The continuum **inheritance** of χ/6 (CONT-1.3).
- **Partially derived (the value):** χ = φ⁻³ from the Finding C-3 distance-ratio (the exponent is fixed *given* the ratio).
- **Open:** (a) **why that ratio** — the candidate-magnitude space is not a singleton; the three "cleanly-derived" candidates are φ⁻³ (edge-to-first-non-edge symmetric bias), 1/√5 ≈ 0.447, and 5 − 2√5 ≈ 0.528 (Capotauro §6 Q3). (b) **the symmetry-breaking dynamics** (FI-C-9's input status). (c) numerical signposts (δ_CP = 180° + arctan(φ⁻³) ≈ 193.3° vs NuFIT 195° ± 40°; Δp_LR = φ⁻³/6 ≈ 0.0394 vs ~0.04) **support** φ⁻³ but are explicitly **signposts, not derivations**.

---

## §3 Gap decomposition and the honest target

OPEN-CHIR-1d splits into two sub-gaps of very different difficulty. Treating them as one ("derive φ⁻³") obscures that one is near-term reachable and the other is a deep programme target.

### §3.1 Sub-gap 1d-α — ratio selection (near-term; THEO-CHIR-CHI-1)

**Claim to target:** the edge-to-first-non-edge symmetric-bias ratio (1−φ⁻¹)/(1+φ⁻¹) is the canonical chirality-magnitude generator from the 600-cell's distance structure, uniquely selected (or selected up to a stated structural criterion) over the alternatives 1/√5 and 5−2√5. Given this selection, χ = φ⁻³ follows by the §2.1 arithmetic.

This is the reachable piece. It is a **600-cell combinatorial-geometry** question: enumerate the natural symmetric-bias ratios on the polytope's distance spectrum (Finding C-4 lists 8 distinct distances), state the structural criterion that singles out the edge-to-first-non-edge pair (e.g. it is the unique pair bridging the two shortest substrate distances at the host vertex's first shell, the locus where n̂ breaks $H_4 \to H_3$), and show the alternatives fail that criterion. Plausible layer: **Layer 2/2.5** (a structural-selection argument, not a dynamical derivation). Reserved theorem ID: **THEO-CHIR-CHI-1**.

The honest caveat for 1d-α: even a clean selection criterion gives χ = φ⁻³ *conditional on the symmetric-bias-of-a-distance-pair* being the right *form* of the magnitude generator. Why a symmetric bias (1−r)/(1+r) of a distance pair — rather than some other geometric functional of the 600-cell — is itself a structural choice 1d-α must state, not assume.

### §3.2 Sub-gap 1d-β — symmetry-breaking dynamics (deep; deferred)

**Target:** derive the $H_4 \to I_4$ symmetry-breaking dynamics that select the broken chiral phase, eliminating FI-C-9 as an input entirely. This is the deep piece the F.1 §14.17 long-term target names and that Capotauro defers to OPEN-SM-4 ↔ SS-corpus. It is **not** scoped for near-term closure; this sketch registers it as a deferred deep target and does not reserve a theorem ID for it.

### §3.3 The honest layer and E21's classification

E21 stays **emergent (provisional)**. Closing 1d-α alone would *not* upgrade E21 to emergent (established), because (i) 1d-β (the dynamics / FI-C-9 elimination) remains open, and (ii) the F.1 magnitude content that consumes χ (Case A.1 δ=χ) is itself provisional. So E21's provisional status is robust regardless of 1d-α's outcome. What 1d-α *does* buy: it converts the exponent −3 from "computed but ratio-unjustified" to "computed from a stated structural selection criterion," materially strengthening the provisional classification and directly answering the reviewer's exponent question at structural-argument rigor.

This staging is the honest analog of the E20 economy: there, the primitive count was firm while the magnitude was provisional; here, the exponent is derivable-given-the-ratio while the ratio-selection (1d-α) and the dynamics (1d-β) are the owed pieces, of which only 1d-α is near-term.

---

## §4 Section structure of the eventual THEO-CHIR-CHI-1 artifact (1d-α)

~6 sections, Layer 2/2.5 structural-selection theorem:

1. **Setup** (~35 lines): E21, the FI-C-9 status, the goal (justify the ratio, hence the exponent), the explicit non-goal (1d-β dynamics).
2. **The 600-cell distance spectrum at the host vertex** (~70 lines): Finding C-4's 8 distinct distances; the first-shell structure under vertex-aligned n̂ ($H_4 \to H_3 = I_h$); enumeration of candidate symmetric-bias ratios and their values (φ⁻³, 1/√5, 5−2√5, …).
3. **The selection criterion** (~70 lines): the structural criterion singling out the edge-to-first-non-edge pair (candidate: the unique pair bridging the two shortest distances at the chirality-breaking locus); demonstration that the alternatives fail it.
4. **The exponent** (~30 lines): given the ratio, (1−φ⁻¹)/(1+φ⁻¹) = φ⁻²/φ = φ⁻³, the §2.1 arithmetic, with a verify script.
5. **Layer, signposts, and what is not claimed** (~45 lines): Layer 2/2.5; δ_CP and Δp_LR as signposts not derivations; 1d-β explicitly deferred; FI-C-9 not yet eliminated.
6. **Conclusion + falsifiers** (~25 lines). Falsifiers: (F1) an alternative 600-cell ratio satisfying the selection criterion with a different value; (F2) a demonstration that the symmetric-bias-of-a-distance-pair is the wrong *form* of generator; (F3) a 1d-β dynamics derivation yielding χ ≠ φ⁻³ (which would refute, not just defer).

A `verify_chi_phi3_ratio.py` confirming the distance spectrum + the ratio arithmetic at machine precision is a Tier-2/3 deliverable bundled with the artifact.

---

## §5 Precondition and honesty notes

- **Audit CONT-1.3 imprecision corrected** (§0): CONT-1.3 is inheritance, not derivation; the magnitude derivation is Finding C-3. Tracked here + CHIR.md; audit .tex stays v1.1-frozen.
- **FI-C-9 not eliminated by 1d-α.** Even with 1d-α closed, χ = φ⁻³ remains a foundational input until 1d-β derives the symmetry-breaking dynamics. The artifact must say so.
- **Signposts are signposts.** δ_CP ≈ 193.3° and Δp_LR ≈ 0.0394 support φ⁻³ but are numerical proximities; per Finding C-5 they are "registered as numerical signposts that support the corrected χ = φ⁻³ value but do not validate it." The artifact inherits that discipline (and the `AI_team_expectations.md` §1.3 verbatim-verification rule).
- **Cross-link to E20.** χ does not enter the E20 primitive count (THEO-CHIR-PCD-ORIENTATION-1 excluded the magnitude by design); 1d-α/1d-β do not change E20's resolution.

---

## §6 Patch sequence

- **Patch 0637 (this patch):** this scope-and-precondition sketch; reasoning fragment; CHIR.md OPEN-CHIR-1d update (scope sketch in progress; the 1d-α/1d-β decomposition; the CONT-1.3→Finding-C-3 correction); registry changelog. No theorem-registry proved-row; THEO-CHIR-CHI-1 reserved for 1d-α.
- **Patch 0638+ (target):** the THEO-CHIR-CHI-1 artifact (1d-α ratio-selection theorem) at `chirality_derivations/theo_chir_chi_1.tex` + reasoning + verify script, once the selection criterion of §3.1 is in hand. Plausibly preceded by a short combinatorial-geometry exploration of the distance-spectrum candidate ratios.
- **Deferred (no patch scheduled):** 1d-β (symmetry-breaking dynamics / FI-C-9 elimination), a deep OPEN-SM-4 ↔ SS-corpus target per F.1 §14.17 and the Capotauro deferral.

---

## §7 What the eventual artifact contributes

It answers the most-cited reviewer question about the CHIR programme ("why φ⁻³ and not φ⁻¹/φ⁻²/1/√5?") at structural-argument rigor, by justifying the ratio that fixes the exponent. It converts E21 from "value computed, ratio unjustified" to "value computed from a stated selection criterion," strengthening the provisional classification without overclaiming a full FI-C-9 elimination. And it cleanly separates the reachable piece (1d-α, geometry) from the deep piece (1d-β, dynamics), so the programme does not mistake the former's closure for the latter's.

---

## §8 References

- `chirality_audit/theo_chir_audit_1.tex` (v1.1) — E21 (emergent (P)); the CONT-1.3 note this sketch corrects.
- `capotauro/sketches/Capotauro_chi_phi_closure.md` — **Finding C-3** (χ = φ⁻³ from the edge-to-first-non-edge symmetric-bias ratio; the φ⁻² archive error correction); **Finding C-4** (8 distinct 600-cell distances); **Finding C-5/C-7** (δ_CP and Δp_LR signposts; T = V/2 = 6); §6 Q3 (the candidate-magnitude list φ⁻³ / 1/√5 / 5−2√5); FI-C-9 registration.
- `theorem-registry.md` — FI-C-9 (substrate-vacuum broken-symmetry order parameter |χ| = φ⁻³); THEO-CAP-1, THEO-SD-CHIR-1/2 (consume χ); the χ ≡ ε identification (Finding C-W39).
- `chirality_continuum/` — THEO-CHIR-CONT-1.3 (magnitude *inheritance* via topological projection — consumes χ, does not derive it).
- `dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` §13 (|M| = |δ|/6, Case A.1 δ=χ), §14.17 (the χ-from-pure-geometry long-term target = 1d-β), §11.10 (the geometric-imbalance-counting hint, an alternative 1d-α/1d-β attack route).
- `axiom-registry.md` — A5 metric (η = 1/φ, the edge length entering the ratio); A2 (600-cell distance structure).
- `frontier_sectors/CHIR.md` — OPEN-CHIR-1d; E21; the THEO-CHIR-PCD-ORIENTATION-1 record (E20, the sibling target).

---

**Scope document complete.** Patch 0637 commits this sketch + reasoning + the CHIR.md update. The near-term artifact (THEO-CHIR-CHI-1, sub-gap 1d-α) ships at Patch 0638+ once the ratio-selection criterion is in hand. The honest finding: χ = φ⁻³'s exponent is derivable *given* the edge-to-first-non-edge symmetric-bias ratio (answering "why −3"); justifying that ratio is the near-term reachable piece (1d-α); deriving the symmetry-breaking dynamics that eliminates FI-C-9 is the deep deferred piece (1d-β). E21 stays emergent (provisional) throughout.
