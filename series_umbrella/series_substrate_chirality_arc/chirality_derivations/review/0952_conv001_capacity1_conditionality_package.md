# CONV-047 — CONV-001 dispatch package: restating THEO-CHIR-CAPACITY-1's Mechanism-A conditionality

**Patch:** 0952, 13 Sep 2026. **Lane:** chirality (09xx). **Type:** CONV-001 five-slot panel dispatch. **Bar:** majority per question; on PASS the chirality lane enacts the restatement in a separate patch.

**Economy classification (WORKFLOW-REVIEW-ECONOMY, binding founder ruling 15 Jul 2026, Patch 2495; reaffirmed 7 Aug 2026, Patch 3025).** This is a **win** under clause 1(a) — a positive claim entering a registry: it strengthens a registered theorem by narrowing its stated conditionality. It is **not** clause 1(b); the lane is not stuck. The founder also issued clause 1(c) explicitly on 13 Sep 2026. **Full five-slot panel is therefore required, not optional** — clause 5's counterpart obligation applies: the scrutiny saved on the negatives and closures of Patches 0940–0951 must actually be spent here.

For the record, the supporting patches were correctly *not* panelled: 0940, 0941, 0949, 0950 and 0951 each moved no verdict and registered no claim, and took one dated line apiece under clause 2. This dispatch is the first item in the sequence that meets the win bar.

**No verdict moves by this patch.** V3/W3 stand; CAPACITY-1's registered wording is untouched until adjudication.

---

## What is being asked

THEO-CHIR-CAPACITY-1 is currently registered as conditional on **Mechanism A** (OPEN-FP-F1-2), specifically on per-edge independence of its measure and on pointwise non-degeneracy of the dynamical η. The proposal is to narrow the first of those.

**Proposed restatement:**

> THEO-CHIR-CAPACITY-1 is conditional on **MA.1's reversal-odd first harmonic** — `r(ê; v) = r₀(1 + δ ê·n̂)` with `δ ≡ B` — together with per-edge independence of the measure and pointwise non-degeneracy of the dynamical η. It is **not** conditional on `A = 0` (absence of a reversal-even midpoint term) nor on first-harmonic truncation. The reversal-odd first harmonic is **derived**, not assumed (Patch 0949).

**Why it matters.** If sustained, CAPACITY-1's Mechanism-A dependence rests on derived content only, and the V3 verdict's remaining conditionality is piece 1 alone — pointwise non-degeneracy — which is a separate and older question.

## The supporting chain (all inlined in the dispatch block)

- **Patch 0949 (L4-A).** Representation theory on the 1,440 directed edges under H₄-covariance, harmonics in n̂, Frobenius reciprocity. H₄ is arc-transitive ⇒ `r₀` is one constant, no tangent term. The directed-edge stabiliser is C₅v (order 10) with fixed subspace `span{v, w}` ⇒ the first-harmonic family is **two**-parameter, `A(m·n̂) + B(ê·n̂)`. The **reversal-odd part is one-dimensional**, `B ê·n̂` — MA.1's form exactly, unique up to scale. The reversal-even `A`-term **cancels identically** in MA.2's antisymmetric current at all 120 vertices for arbitrary `A` (α₁ = 6/φ² reproduced with A = 0.5). Verify 8/8. **Not forced:** `A = 0`, and linear-exactness (Sym² invariants dim 4).
- **Patch 0950 (C1, C2).** C1: both residual terms are **per-edge functions**, so per-edge independence survives; and the 0828 refined-chord bound `ρ(M) ≤ κ(z*) < 1` **never references the rate law**, being built from the observable's weights under the pointwise floor — re-verified, 0 violations / 120 adversarial non-homogeneous weightings, max ρ = 0.491. 0828 was specifically hardened for n̂-dependent non-uniform rules, which is what `A ≠ 0` produces. C2: a **constant** `A` promotes the small-δ steady-current scaling from δ³ to ~A²δ — a real two-order effect — **but** C2 is stated at the physical bias, and at δ = φ⁻³ the current runs 1.7–3.4×10⁻⁵ across A ∈ [0,1] with O(J²) ≤ 1.1×10⁻⁹; divergence-free and T-odd throughout. Verify 7/7.
- **Patch 0951 (C3).** K_lift recomputed **in 0821's own machinery**: 0.0532 at A = 0 (baseline reproduced), 0.0526–0.0532 across A ∈ [0,1] with the rate-to-d.o.f. coupling κ scanned over {±0.5, ±1, ±2}. Worst case /K_c = 0.64 uniform (36% margin), 0.20 staggered (80% margin); correlator short-range throughout (≤0.008). Verify 5/5.

## Questions for the panel

**Q1 — the uniqueness claim (0949).** Is the representation-theoretic argument sound and exhaustive: arc-transitivity ⇒ constant `r₀`; directed-edge stabiliser C₅v with 2-dimensional fixed subspace ⇒ two-parameter first harmonic; reversal-odd part one-dimensional ⇒ MA.1's form unique up to scale? Any hidden orbit, any missed invariant, any error in the Frobenius step?

**Q2 — the C1 robustness claim (0950).** Does per-edge independence genuinely survive `A ≠ 0`? The argument is that `A(m·n̂)` and any quadratic `n̂ᵀT(v,ê)n̂` are functions of a single edge, so no coupling between *distinct* edges is introduced and the measure's factorization structure is untouched. Is that sufficient, or does per-edge independence require something stronger that the residual breaks?

**Q3 — the C2 scope judgment (0950).** C2 is stated "at the physical bias, not all-orders." Given that a constant `A` changes the small-δ scaling exponent from 3 to ~1, is it legitimate to rest C2 on the magnitude at δ = φ⁻³, or does the exponent change constitute a falsifier for C2 as written? **This is the question the lane considers most likely to draw an objection.**

**Q4 — the C3 modelling choice (0951).** The residual enters 0821's edge d.o.f. as a per-edge *scale* (`x_e = δ·bias_e + (1 + κ A m_e·n̂)·N(0,1)`) rather than a mean shift, because it is reversal-even. The coupling κ is not on file and was scanned. Is the scale-not-mean mapping correct, and is scanning κ an adequate substitute for deriving it?

**Q5 — the restatement itself.** Is the proposed wording above the right narrowing — neither over-claiming (it does not assert Mechanism A is discharged, nor that V3 is unconditional) nor under-claiming? In particular: is it correct that **piece 1, pointwise non-degeneracy of the dynamical η, is entirely untouched** by Patches 0949–0951 and remains CAPACITY-1's live conditionality?

**Q6 — anything the lane has missed.** Adopted regardless of the verdict on Q1–Q5.

## Seat mandates

**IDENTITY** (self-label model and version). **OWN-RUN** — each seat runs `0949_l4a_rate_law_form.py`, `0950_capacity1_residual_consumption.py` and `0951_c3_klift_recompute.py` independently and reports **COUNT-LINE** (`8/8`, `7/7`, `5/5`) plus wall-clock seconds. **Inline returns.** Tier legend: T1 = independently computed or algebraically verified; T2 = premise-chain and internal-consistency audit; T3 = substrate-level physical interpretation requiring a founder call.

**Steers:** Q1 (the representation theory) and Q3 (the C2 scope judgment) are the load-bearing ones; every seat should address both. Q4 is a modelling judgment where a dissent is especially wanted.

## Binding rules for adjudication

- Majority per question.
- **Majority UNSOUND on Q1** voids the restatement entirely and returns L4-A to OPEN — the derived-uniqueness claim is the whole basis.
- **Majority falsifier on Q3** leaves C2 conditional on `A = 0` and the restatement must carry that exception explicitly, or be withdrawn.
- **Majority UNSOUND on Q2** is the most serious outcome: it would reopen CAPACITY-1's *existing* registered conditionality, not merely block the narrowing. Escalates to the founder.
- **Any seat contradicting Q5's piece-1 statement** escalates to the founder before enactment.
- Q6 items adopted regardless.

## Scope held

Banks the dispatch package only. **No verdict moved, no THEO registered, no ID consumed beyond 0952, no CHIR.md verdict edit, no count change.** CAPACITY-1's registered wording stands until adjudication. Returns to be recorded in `review/reviews-CONV-047.md` and adjudicated in a separate patch.
