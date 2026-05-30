# Review package — THEO-CHIR-STATUS-1 + THEO-CHIR-STATUS-2 (the chirality primitive/emergent-status capstone)

**For:** the CPP review panel (ChatGPT, Grok, Copilot — independent reviews).
**Target:** the **pair** THEO-CHIR-STATUS-1 (v1.0, Patch 0653) + THEO-CHIR-STATUS-2 (v1.0, Patch 0654), which together constitute the programme's registered answer to its headline chirality question. Review them as a unit.
**What we want:** an adversarial check of whether this capstone is *sound and honestly scoped* — and, most importantly, whether it is **genuinely informative** rather than a relabeling of ignorance. Verdict-flipping objections need a worked argument, not a sketch.

**Disambiguation (read first).** This is the CPP **chirality** programme's *status* capstone — a pair of Layer-2.5 **classification/structural** theorems about whether chirality in CPP is primitive or emergent. It is **NOT** a nuclear-physics OPEN-SS audit, **NOT** the THEO-CHIR-AUDIT-1 enumeration, **NOT** a DSL/F.1 derivation, and (critically) **NOT a claim to have *derived* chirality**. Everything needed is inline; engage the inline content, do not reconstruct from memory.

---

## 0. Context (what is already settled, and what these two theorems do)

The prior result **THEO-CHIR-MERGE-2** (review cycle closed 3/3, conditional on MERGE-α) reduced *all currently-identified* chirality (pseudoscalar, P-odd) content in CPP to **one** primitive: `FI-C-9 = sign(n̂)`, the frozen substrate-vacuum enantiomorph. (The spatial capture handedness is `ζ × FI-C-9`; the temporal cycle handedness is `sign(δ) × FI-C-9`; the modulating `sign(δ)` is the T-arrow, not a chirality — that is the separate question OPEN-CHIR-2a.) Also established there: the 600-cell is **achiral** (closed under the reflection `diag(−1,1,1,1)`), so the geometry supplies no handedness, and FI-C-9 is the **unique** primitive pseudoscalar.

So "is chirality primitive or emergent?" reduces to one object: **is FI-C-9 primitive or emergent?** (= OPEN-CHIR-1d-β). The two theorems under review answer this *at current rigor* and *characterize the upgrade*. Neither derives FI-C-9; both are explicit about that.

---

## 1. THEO-CHIR-STATUS-1 — the verdict structure and current-rigor placement (V3)

**Two emergence axes.** *Capacity* `C ∈ {No, Yes}`: is there a *derivable substrate mechanism* that drives the vacuum to break the achiral symmetry to a chiral phase (produces a handedness-bearing vacuum at all)? *Value* `V ∈ {derived, spontaneous, free}`: *given* a chiral vacuum, is the specific enantiomorph sign fixed by a derivable asymmetry (derived), selected contingently (spontaneous), or unconstrained (free)?

**Three verdicts.**
- **V3 (irreducible primitive):** C = No. No mechanism → FI-C-9 is a frozen boundary condition.
- **V1 (emergent mechanism, contingent sign):** C = Yes, V ∈ {spontaneous, free}. The mechanism is derived; the sign is contingent (standard spontaneous symmetry breaking).
- **V2 (fully emergent):** C = Yes, V = derived. Mechanism *and* sign derived.

**Theorem (exhaustive partition).** {V1,V2,V3} partition the outcome space C×V exhaustively and mutually exclusively: C=No → V3 (value moot, the three C=No cells collapse); C=Yes∧derived → V2; C=Yes∧{spontaneous,free} → V1. (Machine-checked, `verify_status_1_verdict_partition.py` CHECK 1.)

**Theorem (current-rigor status is V3).** Under the present registered framework, capacity is C=No (not established), so the verdict is **V3**. Evidence: (P1) MERGE-2 reduces all currently-identified chirality to FI-C-9; (P2) the 600-cell is achiral → any handedness needs a symmetry-breaking event, not mere geometry; (P3) CHI-1/CAP-1/MERGE-2 all *consume* FI-C-9 (none derives it); (P4) no registered substrate mechanism produces a chiral vacuum (1d-β-ii open). (Machine-checked CHECK 2.)

**Critical framing (Remark).** **V3 means "not yet derived," NOT "underivable."** It is the current-rigor floor, explicitly upgradeable; not an ontological claim.

**Theorem (V1 upgrade condition).** V3→V1 iff 1d-β-ii derives a chiral-vacuum mechanism (C→Yes) with V ∈ {spontaneous, free}; V1→V2 additionally needs a derivable sign-fixing asymmetry (V=derived).

**Honest caps (STATUS-1):** classification result, not a derivation (FI-C-9 not derived); V3 is current-rigor not ontological; inherits MERGE-2's MERGE-α conditionality + the "currently-identified" hedge (G6: an independent (P-odd,T-odd) primitive would add to the count); **spatial chirality only** (the T-arrow status is the parallel OPEN-CHIR-2a; full status = STATUS-1 ∧ 2a).

---

## 2. THEO-CHIR-STATUS-2 — the breaking chain and the V2-exclusion (pins the upgrade to V1)

This extends STATUS-1; it does **not** move the placement (verdict stays V3), it sharpens the *upgrade target*.

**(1d-β-i) The breaking chain.** *Lemma:* the 600-cell isometry group is the Coxeter group H₄ (order 14400, reflection-generated, hence containing improper isometries); the orientation map `det: H₄ → {±1}` is a homomorphism with kernel the rotation subgroup H₄⁺ (order 7200, index 2); quotient H₄/H₄⁺ ≅ ℤ₂. *Theorem:* a chiral substrate vacuum is the spontaneous breaking **H₄ → H₄⁺**; the order parameter labelling the two degenerate broken vacua is the ℤ₂-valued det-pseudoscalar `sign(n̂) = FI-C-9`; the two vacua are exchanged by any reflection in the nontrivial coset. (CHECK 1: closure under `R=diag(−1,1,1,1)`, det grading on {I, R, R², a 2-reflection rotation}, homomorphism multiplicativity.)

**(partial 1d-β-iii) No axiom-level pseudoscalar fixes the sign.** *Lemma:* a quantity can differ on the two vacua only if it is P-odd (a pseudoscalar); every P-even invariant takes the same value on both (they are reflection-images). Concretely (CHECK 2): the signed 4-volume `det[v₁;v₂;v₃;v₄]` of an ordered vertex frame flips sign under R (P-odd), while the Gram matrix, the unsigned volume, and the full pairwise-distance multiset are R-invariant (P-even). *Theorem (axiom-level V2-exclusion):* fixing `sign(n̂)` requires a P-odd pseudoscalar; by MERGE-2 the unique primitive pseudoscalar is FI-C-9 itself (circular); no other axiom-level pseudoscalar exists; so the sign cannot be explicitly derived at the axiom level → V ≠ derived at axiom level → **V2 excluded at axiom level**.

**Corollary (the upgrade is pinned to V1).** Combining with STATUS-1: should capacity upgrade to Yes (1d-β-ii), the verdict is **V1** (emergent mechanism, contingent/free sign), not V2 — at the axiom level. The FI-C-9 emergence target is exactly standard SSB.

**Reopening (Remark, honest cap).** The exclusion is *axiom-level*, not absolute: a **cross-sector** pseudoscalar — the natural candidate being a Standard-Model CP-violating phase (1d-β-v, the FI-C-9 ↔ electroweak-parity-violation link, OPEN-SM-4) — could couple to and fix the sign, reopening V2. Precise claim: *V2 excluded at axiom level; the upgrade is V1 unless a cross-sector pseudoscalar supplies an explicit sign-fixing* (falsifier H3′).

**Honest caps (STATUS-2):** placement unchanged (still V3 — no mechanism derived, 1d-β-ii open); V2-exclusion axiom-level not absolute; inherits MERGE-2 conditionality + "currently-identified"; spatial chirality only; group orders (14400/7200) cited standard facts, structural claims machine-checked.

---

## 3. The registered goal-answer the pair produces

> Chirality in CPP is **emergent down to one currently-identified irreducible primitive (FI-C-9 — verdict V3 at current rigor, conditional on MERGE-α)** plus the separately-tracked T-arrow (2a). When/if FI-C-9 becomes emergent (via the deep mechanism 1d-β-ii) it will be **exactly V1 — emergent mechanism, contingent sign — not V2** (axiom-level), with a cross-sector pseudoscalar (1d-β-v) the only V2-reopener.

---

## 4. What we want you to scrutinize (the load-bearing claims)

Please press hardest on **(Q1)** — it is the one most likely to deflate the whole exercise.

- **(Q1) Is this classification *informative*, or is it relabeling ignorance?** "We have not derived FI-C-9, therefore V3" could be read as dressing up "we don't know" in a verdict label. Argue whether the V3 placement (and the V1-pinning) carries genuine content — e.g., does the capacity/value factorization, the exhaustiveness, and the V2-exclusion actually constrain the *future* derivation in a falsifiable way, or not? If you think it is empty, say so and why.
- **(Q2) Is the capacity/value factorization complete?** Are there emergence modes outside C×V — e.g. *partial* capacity (a mechanism that produces handedness only under extra conditions), or "emergence as an inherited cosmological boundary condition" (neither a derived mechanism nor a free axiom-choice)? If so, the exhaustiveness theorem (and verdict V3 vs V1) needs restating.
- **(Q3) Is the V3 placement honest and correct?** Is "no registered mechanism ⇒ C=No ⇒ V3" the right inference, and is the "not yet derived ≠ underivable" framing sound (not a hedge that makes V3 unfalsifiable)?
- **(Q4) Is the H₄ → H₄⁺ breaking chain correct group theory?** Orders 14400 / 7200, index 2, the det-homomorphism with kernel H₄⁺, the ℤ₂ order parameter = the det-pseudoscalar = FI-C-9, the two-fold degeneracy. (Grok: please run/confirm CHECK 1.)
- **(Q5) Is the V2-exclusion sound?** Does distinguishing the two enantiomorphs genuinely require a P-odd pseudoscalar (Lemma)? Is the appeal to MERGE-2's *uniqueness* of FI-C-9 legitimate here (note it is conditional on MERGE-α)? Is the "axiom-level, reopenable cross-sector (1d-β-v)" scoping correctly drawn — i.e. not overclaimed as absolute, not underclaimed so as to be vacuous? (Grok: CHECK 2.)
- **(Q6) Is the V1-pinning corollary valid**, given Q2/Q5? Does anything let C=Yes land on V2 *at axiom level*?
- **(Q7) Any overclaim or hidden assumption** across the pair — especially anything that would let a reader infer chirality has been *derived* (it has not), or that V3 is a *result* rather than a *floor*.

---

## 5. Triage priority

Q1 (informativeness — the existential check) > Q2 (factorization completeness) > Q5 (V2-exclusion soundness) > Q4 (group theory) > Q3 (V3 honesty) > Q6 (V1-pinning) > Q7 (overclaim sweep). A clean confirmation still sharpens the capstone; a verdict-flipping objection on Q1 or Q2 is the highest-value outcome.

---

## 6. Response format

- Label each claim **INSPECTED** (internal-consistency reading) / **INDEPENDENTLY RECOMPUTED** (you re-derive — e.g. the group orders/det-homomorphism, the partition exhaustiveness, the P-even-invariance) / **SCRIPT-EXECUTED** (you run CHECK 1 / CHECK 2 — Grok especially).
- **Lead with a one-line verdict on Q1** (is the capstone genuinely informative or a relabeling?), then the per-question findings.
- Distinguish *verdict-flipping* objections (with a worked argument) from *calibration* suggestions (wording/scope).
- State explicitly whether you would endorse the registered goal-answer (§3) at its stated Layer-2.5 provisional scope, or what must change first.

*Verification status: both `verify_status_1_verdict_partition.py` (CHECK 1 partition + CHECK 2 placement) and `verify_status_2_breaking_chain.py` (CHECK 1 breaking chain + ℤ₂ grading; CHECK 2 pseudoscalar/V2-exclusion) pass. Theorems compile clean (5 pp each, zero undefined refs).*
