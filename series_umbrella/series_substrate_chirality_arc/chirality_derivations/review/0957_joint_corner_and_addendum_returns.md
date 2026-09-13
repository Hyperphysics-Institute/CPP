# 0957 — CONV-048 addendum returns (5/5) and the joint corner: two reviewers were right to refuse "each still clears," and the corner is superadditive

**Patch:** 0957, 13 Sep 2026. **Lane:** chirality (09xx). **Verify:** `chirality_derivations/code/0957_joint_corner_combined_bound.py` (6/6). **Status:** all five addendum returns in; **still not adjudicated and not enacted**, because this patch found a further error in the proposal that must be fixed first.

---

## 1. The addendum returns — 5 of 5, and the panel converged

| seat | Q1 | Q2 | Q3 | Q5 | verdict |
|---|---|---|---|---|---|
| GPT-5.6 Sol | SOUND | SOUND | **FALSIFIER → SOUND** | piece 1 live | proceed, if C2 is no longer cited as O(δ³) and the odd channel is carried as a named residual |
| Grok 4.6 | SOUND | SOUND | not a falsifier; old numbers withdrawn | piece 1 live | admissible with amendments |
| Gemini | unchanged SOUND | unchanged SOUND | adequate with amendment | unchanged | enact with amendments |
| Copilot | unchanged | unchanged | adequate; combined bound required | unchanged | enact with amendments |
| DeepSeek | unchanged | unchanged | adequate with strengthened note | unchanged | enact with amendments |

**GPT withdrew its falsifier.** Its stated reason is worth recording because it is the strongest endorsement in the round: *"the new odd quadratic is a much better hostile test than the original A-scan. It removes the accidental first-order parity shield and still fails to endanger CAPACITY-1 at the registered scale."* Five independent reviews now agree on **Q1**, **Q2** and **Q5**, and no seat has ever found a falsifier for the uniqueness claim.

**All five endorse the Q6 disposition** — "harmless at the framework's scale, named open beyond it." GPT: declining to mention second order *"would make the theorem look cleaner by hiding the first symmetry-allowed channel that defeats the first-order parity protection."* Grok: closing it *"would invent a bound you do not have (pushing the odd coefficient to 1, 3, 10 makes K_lift fall, which is not a theorem)."*

## 2. The one thing they would not accept — and they were right

Two seats independently refused the accumulation argument, and both converted it into the same concrete test.

> **Grok:** *"What concerns me is not the separate clearances. It is stacking them. Negative A and the odd quadratic were run as two experiments, not at the joint corner… Additive-in-amplitude they would still be O(10⁻⁴) in J. Multiplicative-on-the-slow-edges they are unshown."*
>
> **Copilot (required edits 1, 4):** *"their combined worst-case (if they were to align) must be bounded explicitly."*

The corner was untested. It is tested here, and it produced two results.

### 2a. The admissible domain is not a rectangle — the proposal is wrong as written

Patches 0955/0956 published the admissible range as **|A| ≤ 1.025**, computed at **C = 0**. With the odd quadratic switched on, rate positivity fails earlier: at `A = −1.00, C = +φ⁻³` the minimum rate is **−0.0434** — negative, hence inadmissible (T1).

**So the A-domain sentence now in the reviewer package is false.** It states a bound that only holds on one slice of a two-parameter region. This is the second time in three patches that a published scope claim has been narrower in reality than written, and it was found by taking the reviewers' demand seriously rather than by re-reading.

### 2b. Stacking is superadditive — Grok was right to ask and wrong about the answer

At the worst admissible joint point the current is **9.6 × 10⁻⁴**, against 2.6 × 10⁻⁴ for negative A alone and 4.0 × 10⁻⁴ for the odd quadratic alone. In squared terms the joint value is **4.0× the sum** of the two separate squared values (T4) — the amplitudes roughly *double* rather than adding in quadrature.

**This refutes both Grok's expectation and this patch's own first assertion**, which was written as "additive, not multiplicative" and which the test refused. It is the same pattern as the negative-A prediction at 0955: the reviewer was right that the test was needed and wrong about what it would show. That is twice now, and it is a good argument for running the test rather than reasoning about it.

### 2c. The combined bound, reported by scale

Copilot asked for a single number. Reporting one number would hide the scale dependence the whole disposition rests on, so it is reported as two (T5):

- **At the framework coefficient scale** (|C| ≤ φ⁻³), over the entire joint admissible region: **max J² = 1.3 × 10⁻⁸**.
- **Over the extended scan** (|C| ≤ 0.6): **max J² = 9.3 × 10⁻⁷** — three orders higher.

**C3 is untouched throughout:** worst K_lift over the joint region including the κ scan is 0.0526, ratio 0.63 against the uniform threshold (T6).

**Both figures still clear.** But "five or more orders below," which the addendum and several returns used, is accurate only at the framework scale. At the extended scan the margin is roughly two orders against the coupling threshold, not five. **That is a real erosion and the proposal must not keep quoting the larger margin.**

## 3. Consequence: the proposal needs a third correction before adjudication

Two corrections have already been made (C2's characterisation at 0956; the truncation clause at 0956). This patch forces a third:

1. **The A-domain sentence must become joint.** "|A| ≤ 1.025" is a C = 0 statement. The admissible set is a region in (A, C), and the proposal must say so.
2. **The margin claim must be scale-split.** "Five or more orders" holds at framework scale; at extended coefficients it is ~two. The proposal should quote the framework-scale number and state the extended one separately.
3. **Superadditivity must be stated**, not left implicit — because the natural reading of "each effect still clears" is exactly the independence assumption GPT warned against: *"What would concern me is silently assuming additivity or independence of all possible residuals."* We now know they are not independent.

**None of this defeats the narrowing.** Every condition still clears at the framework scale, which is what the amended proposal claims. But the proposal's *numbers* are wrong in two places and its *silence* on stacking is exactly the thing one reviewer named as the thing that would concern him.

## 4. Disposition

- **CONV-048: 5/5 addendum returns, quorum met on the addendum questions**, but **not adjudicated** — the proposal changed materially again in this patch, and adjudicating against a document with two known-wrong numbers would be adjudicating the wrong thing.
- **Owed, and blocking:** the three corrections in §3, then a final short confirmation round (the corrections narrow and clarify; they do not introduce new claims).
- **No verdict moves. CAPACITY-1's registered conditionality stands. No THEO registered.**
- **Standing credit:** the joint corner, the negative-A gap and the second-order question all came from reviewers. Three of the four substantive findings in this arc since 0954 originated in the panel, not in the lane.
