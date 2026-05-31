# Reviews — THEO-CHIR-VW-1 (the V2-exclusion ↔ Vafa–Witten no-go unification; the sign(μ²) route to B-iii capacity)

**Artifact:** `chirality_derivations/theo_chir_vw_1.tex` (v1.0 → v1.1, Patch 0680 → 0682).
**Review package (immutable request record):** `review/theo_chir_vw_1_review_package_v1.0.md` (Patch 0681).
**Cycle:** OPENED Patch 0681 → **CLOSED Patch 0682, 3/3, no falsifier**.

---

## Outcome

**3/3 CONFIRM at the Layer-2.5 provisional conditional scope; no falsifier; NO verdict move (V3/W3 stand).**

| Reviewer | Verdict | Tier reached |
|---|---|---|
| **ChatGPT** | CONFIRM-WITH-CALIBRATION | SCRIPT-EXECUTED (CHECK 1/2/3 pass) |
| **Copilot** | CONFIRM / endorse | INDEPENDENTLY RECOMPUTED (det-coset ℤ₂); INSPECTED |
| **Grok** | CONFIRM / endorse | SCRIPT-EXECUTED (CHECK 1/2/3 pass) + INDEPENDENTLY RECOMPUTED (group theory, Tier 2 from first principles) |

(Reviewer attribution per Thomas's identification at integration: the SCRIPT-EXECUTED CONFIRM-WITH-CALIBRATION body was pasted twice during dispatch — that duplicate is ChatGPT; the third slot initially received a misrouted THEO-CHIR-AUDIT-1 review and was re-sent. All three VW-1 reviews below are distinct and on-artifact.)

All three endorse the registered position (§3 of the package): VW-b and VW-c established; the unification (Thm 5.1) sound and non-conflating; the verdict map (Thm 6.1) genuinely conditional on the open H1; **no verdict move**. The two reviewers who could run the embedded script (§7) did so and report CHECK 1/2/3 PASS; all three independently recomputed the det-coset ℤ₂ group theory (|H₄|=14400, |H₄⁺|=7200, index 2, det=−1 generator, vectorial-not-axial).

---

## Triage synthesis (the foregrounded questions, §5)

**Q1 — H1 honesty / no-verdict-move (existential).** Affirmed 3/3. Reflection positivity H1 is held open throughout (Prop 4.2; CHECK 3 hard-codes `H1_proved = False`); the verdict map is a genuine function of H1 (H1 unknown → no conclusion; H1 → dichotomy); V3/W3 explicitly unchanged. No reviewer found any step that smuggles a positivity claim or a verdict move. Grok: VW-a "correctly isolates the single sharp remaining question." ChatGPT: "no reader can infer a proof of reflection positivity or a capacity upgrade." Copilot: the conditional dichotomy "orients the programme cleanly."

**Q2 — Vafa–Witten transposition legitimacy (the deepest risk).** Affirmed 3/3 as a *conditional route*, not an applied no-go. ChatGPT (the most cautious): legitimate **only** as a conditional analogy/route; the artifact "mostly scopes this correctly" but should avoid summary wording that could read as "VW applies to CPP now," and VW-c should be framed as an audit of *known obstruction classes*, not a complete proof that no hypothesis is missing. Grok (pressed hardest): "legitimate transposition, no verdict-flipping defect" — the bare substrate meets VW-b (vectorial reflection) and VW-c (no chiral content / no θ-term / real coefficients) at the bare-lattice level, with any evasion entering only via the external SM channel; "no hidden gauge-theory assumption." Copilot: legitimate as a conditional template onto the Φ-continuum EFT, **provided the gauge/fermion hypotheses remain explicitly assumed, not silently satisfied** — make explicit that VW is applied to the *hypothetical* DSL continuum EFT assuming it is a standard vector-like gauge theory.

**Q3 — unification vs conflation.** Affirmed 3/3. Capacity (sign μ²) and value (sign-selection) stay distinct bits (DG-4); the unification is the *shared root* (one parity-even, reflection-positive measure closes both the explicit and spontaneous routes), not an identification of the two bits. Falsifiable separately (H1 vs axiom-level pseudoscalar existence).

**Q4 — det-coset ℤ₂ group theory.** Confirmed 3/3 (recomputed; script-run by ChatGPT + Grok). |H₄|=14400, |H₄⁺|=7200=ker(det), index 2, quotient ℤ₂, generator a det=−1 reflection; vectorial, not axial.

**Q5–Q8 — evasion audit / spontaneous-vs-explicit / reduction fairness / overclaim.** No falsifier. The reduction claim (Q7) drew the calibration: it reduces to H1 **within the VW route**, with continuum-limit promotion and the measure-class transposition folded into H1's scope (Copilot + ChatGPT). Overclaim sweep (Q8/Q6): clean; Vafa–Witten consumed as a cited result, not re-derived.

---

## Calibrations applied (v1.1; convergent, wording-only, NO verdict or theorem-statement change)

1. **"VW no-go" → "VW-style conditional no-go"** in summary lines (ChatGPT) — make the H1-conditionality unmissable wherever the no-go is referenced in summary.
2. **The reduction (Q7):** "the entire capacity question reduces to one positivity question" → "the **VW-route** capacity question reduces to H1, i.e. reflection positivity of the **Φ-continuum DSL measure** (the continuum-limit promotion + measure-class transposition are part of H1's scope)" (ChatGPT + Copilot).
3. **VW-c framed as a known-obstruction-class audit**, not an exhaustive proof that no VW hypothesis is missing (ChatGPT).
4. **H1 stated as a property of the Φ-continuum EFT measure** obtained via CONT-1, not just the finite substrate (Copilot + Grok).
5. **"V3 by principle" always paired with "conditional on H1 and within the bare substrate axioms"** (ChatGPT).

These are honest-scope tightenings: they narrow nothing in the established content (VW-b, VW-c, the unification) and change no verdict (V3/W3 stand). Installed as a v1.1 calibration Remark + targeted summary rewording; the theorem statements (Lemmas 3.1/4.1, Thm 5.1/6.1, Prop 4.2) are unchanged.

---

## Verbatim reviews

### ChatGPT — CONFIRM-WITH-CALIBRATION (SCRIPT-EXECUTED)

> **One-line verdict on Q1 and Q2.** Q1 (INSPECTED / SCRIPT-EXECUTED): H1 is honestly held open, and "no verdict move" is airtight. Q2 (INSPECTED): the Vafa–Witten transposition is legitimate only as a conditional analogy/route, not as an applied no-go theorem yet; the artifact mostly scopes this correctly, but should avoid wording that sounds like VW already applies to CPP before H1 and the continuum/measure hypotheses are proved.
>
> **Q1 — H1 honesty / no verdict move. CONFIRMED.** The package explicitly says reflection positivity is not proved, no sign(μ²) is computed, H1 is open, and V3/W3 remain unchanged. The conditional map ("if H1, then no spontaneous substrate parity breaking; if not H1, no conclusion") is clean.
>
> **Q2 — Vafa–Witten transposition. CONFIRM-WITH-CALIBRATION.** VW's original theorem is not merely "reflection positivity + parity"; it is tied to vector-like gauge theories with a specific Euclidean functional measure. CPP/DSL is not yet shown to have that same measure class. So the theorem should be read as: *if the CPP continuum DSL measure satisfies the relevant VW/reflection-positivity hypotheses, then the substrate parity ℤ₂ cannot break spontaneously.* That is valid. What would be invalid is saying "VW applies" before H1 plus the measure transposition are proved. The package mostly avoids that, but "VW-c evasion audit" should be framed as an audit of known obstruction classes, not a complete proof that no VW hypothesis is missing.
>
> **Q3 — unification vs conflation. CONFIRMED.** Capacity and value remain distinct. STATUS-2 closes the explicit/value-sign route at axiom level; VW, conditional on H1, closes spontaneous capacity. The unification is not "same bit" but "same reflection-positive, parity-even substrate measure would block both routes." Coherent.
>
> **Q4 — det-coset symmetry class. INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED.** Checks pass: |H₄|=14400, |H₄⁺|=7200, index 2, quotient ℤ₂, det(−1) generator. Vectorial reflection/parity class, not axial.
>
> **Q5 — evasion audit. PARTIAL-CONFIRMED.** "Bare substrate has no chiral content, no θ-term, no manifest complex phase" is plausible at the reachable level. Real ℚ[φ] coefficients are a reasonable first-pass no-manifest-phase check, but not evidence enough for OS/reflection positivity. The package says this; keep that limitation prominent.
>
> **Q6 — spontaneous vs explicit. CONFIRMED.** VW only addresses spontaneous breaking. STATUS-2 addresses explicit axiom-level sign fixing. External explicit bridge remains open. Split is correct.
>
> **Q7 — reduction claim. CONFIRM-WITH-CALIBRATION.** The capacity question reduces to H1 only within the VW route. There are still surrounding dependencies: continuum-limit promotion, full DSL effective action, and whether CPP's measure truly meets VW's theorem class. Phrase as "the VW capacity route reduces to one sharp positivity question," not "the entire capacity question reduces to one positivity question."
>
> **Q8 — overclaim sweep.** No verdict-flipping overclaim found. "V3 by principle" should always be paired with "conditional on H1 and within bare substrate axioms."
>
> **Verdict-flipping objections:** none, provided v1.0 is read as conditional. **Calibrations:** (1) "VW no-go" → "VW-style conditional no-go" in some summary lines; (2) "capacity question reduced to H1" → "VW-route capacity question reduced to H1 plus continuum/measure transposition"; (3) mark VW-c as "known evasion-route audit," not exhaustive. **Final endorsement: CONFIRM-WITH-CALIBRATION at Layer-2.5 conditional scope.**

### Copilot — CONFIRM / endorse (INDEPENDENTLY RECOMPUTED + INSPECTED)

> **One-line verdict.** Q1 (H1 honesty / no-verdict-move): INSPECTED — H1 is genuinely left open and the "no verdict move" boundary is held cleanly. Q2 (VW transposition): INSPECTED — legitimate as a conditional template onto the DSL continuum EFT, provided its gauge/fermion hypotheses remain explicitly assumed, not silently satisfied.
>
> **Q1.** H1 status (VW-a): the text is explicit that reflection positivity H1 is not proved; VW-a is framed as "first-pass criteria + no manifest obstruction," and CHECK 3 hard-codes `H1_proved = False`. No step upgrades this to "H1 holds." The verdict map (VW-d) is explicitly a function of H1 (unknown → no conclusion; true → dichotomy). No smuggled positivity / hidden verdict move. Objection: none.
>
> **Q2.** The artifact uses Vafa–Witten only in the conditional form and treats the CPP substrate as a *hypothetical* such theory; it does not claim the substrate already is one. Hypotheses mapping: VW-b (vectorial parity, det=−1), VW-c (θ-free; chiral/θ/complex enter only via the SM bridge), H1 left open. Calibration: add one sentence making explicit that "Vafa–Witten is applied to the *hypothetical* DSL continuum EFT, assuming it is a standard vector-like gauge theory with reflection positivity and no θ-term." Objection: none.
>
> **Q3.** Two bits remain distinct (CHECK 2: capacity vs value); the shared root (parity-even, reflection-positive measure) is conceptually sound. No conflation; no change needed.
>
> **Q4.** INDEPENDENTLY RECOMPUTED: |H₄|=14400, |H₄⁺|=7200, index 2 ⇒ ℤ₂; generator a det=−1 reflection; vectorial parity, not axial/chiral.
>
> **Q5/Q6.** Evasion classification matches prior CHIR/TARROW/BRIDGE results; "first-pass" language already present and not overclaimed. Spontaneous (VW) vs explicit (STATUS-2) split correct; branch (B) correctly inherits BRIDGE-1's kinematic/P2 cap.
>
> **Q7.** Reduction fair at Layer-2.5; calibration: explicitly state H1 is a statement about the continuum EFT measure obtained via Φ, not just the finite substrate.
>
> **Q8.** "V3 by principle" appears only conditional on H1; "forced"/"settled by principle" describe only the conditional dichotomy; no positivity proof / computed sign(μ²) / verdict change.
>
> **Overall:** endorse at the stated Layer-2.5 conditional scope. VW-b and VW-c sound; the unification (Thm 5.1) structurally correct and non-conflating; VW-d genuinely conditional on H1 with no verdict move; the reduction fair with the continuum-limit inheritance folded into H1. No verdict-flipping objections; only minor calibration.

### Grok — CONFIRM / endorse (SCRIPT-EXECUTED + INDEPENDENTLY RECOMPUTED Tier 2)

> **Q1 verdict (unification soundness):** sound and non-conflating — STATUS-2's axiom-level V2-exclusion (value side) and the conditional Vafa–Witten no-go (capacity side) are cleanly two faces of one reflection-positivity property, with H1 explicitly left open. **Q2 verdict (VW transposition to non-gauge substrate):** Vafa–Witten legitimately transposes to the bare CPP substrate under the stated conditions (no gauge fields, no chiral fermions, real ℚ[φ] coefficients, vectorial ℤ₂); the analogy is honest and scoped as conditional/first-pass.
>
> All numerical/structural claims INSPECTED for consistency with the inline package + consumed priors. Group-theoretic claims INDEPENDENTLY RECOMPUTED (Tier 2 from first principles). The full embedded verification script (§7) SCRIPT-EXECUTED — ALL CHECKS 1/2/3 PASS exactly (group orders, tuple equality, reflection-positivity criteria, conditional verdict map, no verdict move).
>
> **Q1 (theorem & conditional no-go, pressed):** sound and honestly scoped. Thm 5.1 unifies the explicit-breaking route (closed unconditionally by STATUS-2 V2-exclusion) with the spontaneous route (closed conditionally on H1 by VW-b + VW-c). The conditional dichotomy (Thm 6.1) is clean: if H1, μ²>0 within substrate axioms → observed FI-C-9 ≠ 0 is either genuine primitive (stronger V3) or externally sourced via the SM bridge. No verdict move. H1 repeatedly flagged open/first-pass (Prop 4.2) — no overclaim. VW-a correctly isolates the single sharp remaining question.
>
> **Q2 (VW transposition, pressed hardest):** legitimate transposition, no verdict-flipping defect. VW (1984) applies to reflection-positive, vector-like, θ-free theories and forbids spontaneous parity breaking (μ²>0). The bare substrate meets VW-b (det-coset ℤ₂ = proper vectorial reflection, det=−1 isometry of H₄, not axial) and VW-c (no chiral fermion content; no θ-term, sign(δ)=W3 not an action term; real DSL-4..12 coefficients). The transposition is valid at the bare-lattice-measure level (prior to Φ or the SM bridge); any evasion enters only via the external SM channel (BRIDGE-1 kinematic P2). No hidden gauge-theory assumption; scoped conditional on H1.
>
> **Q3 (unification vs conflation):** sound, non-conflating. Value side (axiom-level V2-exclusion, no P-odd pseudoscalar to fix sign(η)) and capacity side (VW no-go on sign(μ²)) explicitly "two faces of one property" (parity-even + reflection-positive measure); not merged; falsifiable separately. No conflation.
>
> **Q4 (det-coset ℤ₂):** confirmed (INDEPENDENTLY RECOMPUTED Tier 2 + SCRIPT-EXECUTED CHECK 1). |H₄|=14400, |H₄⁺|=7200, index 2, quotient ℤ₂; det homomorphism kernel H₄⁺; generator any reflection (e.g. diag(−1,1,1,1)); order parameter sign(n̂)=FI-C-9 the ℤ₂ label, vectorial not axial.
>
> **Q5 (honest caps & downstream safety):** none found. All IS-NOT statements, H1-conditionality, and "no verdict move" language explicit and repeated; downstream (CONJ-CHIR-1, B-iii) cleanly isolated to the external SM-bridge channel.
>
> **Q6 (overclaim / hidden-assumption sweep):** none. H1 not proved (explicitly open); Vafa–Witten consumed as a cited result, not re-derived; scope narrowly the structural/conditional unification at Layer-2.5.
>
> **Overall:** endorse THEO-CHIR-VW-1 at its stated Layer-2.5 provisional scope with no changes required. Sound, honestly scoped, genuinely informative: sharpens the capacity question to a single testable hypothesis (H1 / reflection positivity of the DSL measure) while unifying the value and capacity exclusions without overclaiming. The conditional dichotomy (Thm 6.1) orients the programme cleanly. Ready for integration.

---

## Process note

Two dispatch-side mishaps occurred and were caught at integration, both protecting the swarm-validation count: (1) the ChatGPT review was pasted twice verbatim — recognized as a duplicate (two independent models do not produce byte-identical reviews), not counted as two; (2) the third slot initially received a misrouted THEO-CHIR-AUDIT-1 review (different artifact — F1/F2/F3 falsifiers, the 27-entry map, no mention of Vafa–Witten/μ²/H1) — recognized as off-artifact and re-sent, yielding the genuine Grok pass. The cycle was closed only once three distinct on-artifact reviews were in hand. Per DG-3, no verdict language changed at any point; V3/W3 stand.
