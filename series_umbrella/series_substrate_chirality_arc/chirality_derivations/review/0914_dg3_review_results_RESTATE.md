# DG-3 review results — THEO-CHIR-CAPACITY-1: **RESTATE** (not a pass); verdict NOT enacted

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0914_dg3_review_results_RESTATE.md`
**Patch:** 0914 · **Reviews adjudicated:** ChatGPT (complete), Copilot (complete), Grok (PENDING — not received; only a placeholder came through).
**Disposition:** Pass criterion (3/3 CONFIRM, no unresolved falsifier) **NOT met** — two complete reviews both returned **RESTATE**. **THEO-CHIR-CAPACITY-1 is NOT enacted.** V3/W3 stand; CAPACITY-1 reserved; OPEN-CHIR-1d-β stays OPEN; prediction count unchanged; conditional on Mechanism A.

---

## Tally

| | Q1 η-identity | Q2 current | Q3 comparison | Q4 logic/framing | Q5 scope | Overall |
|---|---|---|---|---|---|---|
| ChatGPT | FALSIFY | FALSIFY | FALSIFY | FALSIFY | CONFIRM | **RESTATE** |
| Copilot | FALSIFY | CONFIRM | CONFIRM | CONFIRM | CONFIRM | **RESTATE** |
| Grok | — | — | — | — | — | PENDING |

Both completed reviewers land their *overall* on the **same** issue: **Q1 — the universality of C1.** That convergence is the signal.

## 1. The central, convergent falsifier (Q1) — genuine, and it is the η-identity spot

C1 shows that no **tested** candidate mode (support m∈{4,6,8,12} × 3 frames, equilibrium measure) condenses — a **sample**, which the doc itself flagged as "not a proof." The package then phrased the conclusion universally ("η disordered in **every** mode"). Both reviewers correctly flag the gap: a more-local or non-local admissible η **outside the tested family** is not strictly excluded. This is exactly the η-identity question (C1) flagged all season as the one place the argument might be incomplete — adversarial review put its finger on it.

**This is not merely a wording issue; it needs one of two real moves:**

- **Path A — restore the universal claim via an eigenmode-completeness closure (recommended; likely largely in hand).** The η-model is an Ising-type model on the 120 vertices of the 600-cell, coupling confined by review-closed **CHI-1 locality** to the nearest shells (12-regular). The eigenmodes of any such local coupling operator form a **complete** basis, and a mode with eigenvalue λ has mean-field threshold 1/|λ|. The **largest** |λ| has the **smallest** threshold — so it binds first. For a 12-regular local operator, **λ_max ≤ 12** (Perron bound; the uniform mode saturates it), and |λ_min|=3.708 < 12. Hence the single condition **|K_lift|·λ_max < 1** clears **every** eigenmode at once. With |K_lift|≈0.053 and λ_max=12: 0.053·12 ≈ 0.64 < 1 (mean-field), i.e. the **conservative ≈44% margin already computed is the exhaustive, worst-case-sign, all-eigenmodes bound** — not a sample. The "scan over m" was a confusing presentation of "λ_max is bounded across η-definitions"; reframed as eigenmode completeness + a locality-bounded λ_max, it answers Q1 directly. **F.1 window (residual-1 owner) to formalize and confirm the one residual:** does CHI-1 locality guarantee λ_max ≤ 12 for the *actual* dynamical η-coupling operator (no enhanced/long-range component that lifts λ_max above the coordination number)? If yes, the universal claim holds and re-review should clear Q1.
- **Path B — honest scope-narrowing (Copilot's calibration; airtight now, weaker headline).** Restate to: *"V1 (net-handedness / det-coset condensation) is excluded within the local-η regime compatible with Mechanism A, at the physical bias, with ≈44% conservative margin,"* flagging exotic non-local constructions as outside the theorem's scope. This is already essentially review-endorsed (both reviewers accept the uniform exclusion + margin); it just isn't the strictly-universal "chirality is a primitive, full stop."

**Verdict-owner lean:** pursue **Path A** — the closure looks mostly derivable from work already done (CHI-1 + the λ_max/λ_min spectrum), and it would restore the strong claim rather than retreat to the regime-bounded one. Path B is the fallback if λ_max ≤ 12 cannot be guaranteed for the dynamical operator.

## 2. Documentation gap (Q3, ChatGPT) — real, fixable

The package's both-channels C3 asserts the staggered threshold (λ_min=−3.708, K_c^AFM≈0.27) and the both-channels reconciliation, but those live in `residual3_afm_correction.md` (0824) and `threshold_reconciliation.md` (0825), **which were not linked.** The linked residual-3 (`residual3_true_Kc.md`, 0823) still carries the **superseded** framing — "a staggered mode … is not a net global handedness (not V1)" — which directly contradicts the package's C3. A reviewer reading the linked sources therefore sees an unsubstantiated 0.27 and an internal contradiction. **Fixes:** (a) add 0824 + 0825 to the source links; (b) annotate 0823 (forward-only) that its "staggered not V1" framing was corrected by 0825 (staggered *does* break the det-coset ℤ₂).

## 3. Wording inconsistency (Q4, ChatGPT) — fixable

The Q4 chain as written ("uniform mode off-critical ⇒ no det-coset breaking") is inconsistent with the both-channels scope. **Fix:** reword to "**both** uniform and staggered modes off-critical ⇒ no det-coset breaking ⇒ μ²>0 ⇒ V3 confirmed / V1 excluded." (Under Path A, "all eigenmodes off-critical via |K_lift|·λ_max<1.")

## 4. Standard-of-proof (Q2: ChatGPT FALSIFY / Copilot CONFIRM) — carry as an explicit scope limit

C2 is a physical-bias parametric/symmetry argument, not an all-orders NESS proof (a stated caveat). Copilot judged it overwhelming at the physical bias; ChatGPT held the all-orders line. **Resolution:** carry "at the physical bias δ=φ⁻³" as an explicit scope limit in the restated claim (optionally, the F.1 window later pursues the all-orders statement). Not a blocker for a Mechanism-A-conditional status theorem, but the limit must be stated, not buried.

## 5. What the reviews DID confirm (so the result is not a teardown)

Both reviewers CONFIRM **Q5** (scope/honesty: Mechanism-A conditionality, no-derivation, temporal axis + OPEN-SM-4 correctly untouched). The framing guard (μ²>0 ⇒ primitive, not emergent) drew **no inversion flag** from either. Copilot additionally CONFIRMS Q2/Q3/Q4. The result both reviewers explicitly endorse: **"uniform net-handedness condensation is excluded at the Mechanism-A physical bias, ≈42–47% conservative margin."** The entire disagreement is whether that extends to a **strictly universal** "all modes / V1 excluded" claim — which is precisely what Path A would close.

## 6. Disposition + next steps

- **No verdict moved.** CAPACITY-1 NOT enacted. V3/W3 stand; OPEN-CHIR-1d-β OPEN; count unchanged.
- **Collect Grok's review** (the body did not come through). It cannot turn RESTATE→PASS (two reviewers already RESTATE), but may surface a distinct falsifier to fold in.
- **Thomas's call: Path A vs Path B.** Path A → hand the eigenmode-completeness / λ_max-bound closure to the F.1 window to formalize; if it holds, reframe C1 and re-review. Path B → restate to the local-η regime now.
- **Then:** rebuild the package with the §2/§3/§4 fixes + the chosen Path, re-fire to the swarm (3/3 CONFIRM remains the bar). The §2–§4 fixes apply on **either** path.

## Scope held

Review-results record + restatement plan. **No verdict moved, no THEO registered, no CHIR.md edit, no count change.** CAPACITY-1 reserved. Conditional on Mechanism A (OPEN-FP-F1-2).
