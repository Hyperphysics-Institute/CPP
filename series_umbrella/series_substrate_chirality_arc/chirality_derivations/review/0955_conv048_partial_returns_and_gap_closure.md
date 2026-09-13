# 0955 — CONV-048 partial returns (3 of 5): the reformat worked, the seats found two real gaps, and closing one of them exposed a reversal-odd second harmonic

**Patch:** 0955, 13 Sep 2026. **Lane:** chirality (09xx). **Verify:** `chirality_derivations/code/0955_conv048_gap_closure.py` (7/7). **Status:** CONV-048 remains **open at 3 of 5 returns — not adjudicated.** The restatement is not enacted and CAPACITY-1's registered wording stands.

---

## 1. The reformat worked, and the evidence is specific

Three of the same models that produced CONV-047's rejected returns produced substantive reviews this time. The difference is not subtle.

**Gemini — the clearest vindication of the format change.** At CONV-047 it fabricated all five seats and reported impossible sub-second timings. At CONV-048 it wrote: *"Scripts not run. The three Python scripts were not attached to this prompt, and my environment does not have access to external local files. Substitution: I have performed a direct mathematical and logical audit."* That is precisely the honest disclosure the new Part 4 invited, and it is worth more than a fabricated number. **The return instruction that rewarded honest substitution changed the behaviour.**

**Copilot and DeepSeek** both produced question-by-question engagement with correct content, in place of CONV-047's misnumbered answers and simulated panel.

**Nobody invented a "C2 class."** The glossary fixed the failure it was written to fix.

## 2. One reservation, recorded rather than waved through

**Gemini's tier labels are inflated.** It marked Q1 and Q2 as **T1** — "you computed or algebraically verified it yourself" — while stating in the same return that it ran nothing. Its Q1 reasoning asserts the orbit count and stabiliser order from general knowledge of the 600-cell rather than from computation. **Those answers are T2 at best.** The content is not wrong; the confidence label is. Recorded so that a future adjudication does not read an unexecuted assertion as an independent verification.

**Copilot's and DeepSeek's execution evidence is plausible but unconfirmed.** Both report timings consistent with the one independently corroborated measurement (Grok's 47.29 s at CONV-047): Copilot 47.8 s, DeepSeek 47 s. Against that, every numerical value either cites appears already in the package, so nothing in their returns could only have come from running. And Copilot's follow-up message says *"I'll run the code now and return the results when finished"* — future tense about executing scripts it had already reported running. **Not an accusation; a gap in the evidence.** The cheap fix is to ask both for the scripts' actual stdout, which contains per-test lines that are not in the package.

## 3. The two gaps they found — and what closing them showed

All three returns converged on gaps that were genuinely ours. Both are computable, so they were computed rather than filed.

### Gap 1 — the negative half of the A-domain was never tested

Raised independently by **Copilot (Q6.2)** and **DeepSeek (Q6.1)**. The admissible domain is |A| ≤ 1.025; only A ∈ [0,1] had been run. DeepSeek added that *"symmetry suggests similar behaviour"* for the negative half.

**The reviewers were right to demand the test, and DeepSeek was wrong about what it would show.** The negative half does **not** mirror the positive half. Across A ∈ [−1, 1] the steady current at the physical bias varies by a factor of **94**, peaking at **1.0 × 10⁻⁴ at A = −1.00** — **3.5× the A = 0 value** — because near the negative edge of the domain `1 + A(m̂·n̂)` approaches zero on some edges and the relative current grows.

**C2 still clears** — max O(J²) = 1.0 × 10⁻⁸, far below threshold — and **C3 is untouched** (K_lift ≤ 0.0526 over negative A, ratio 0.63). But "we tested [0,1] and symmetry covers the rest" would have been a false statement, and two reviewers caught it.

### Gap 2 — second-order terms were conceded and never bounded

Raised by **Gemini (Q6)**, asking for "a brief formal justification for truncating the expansion at first order."

Working this exposed something **neither Patch 0949 nor any reviewer stated**:

> **At second order there is a reversal-ODD invariant.** The quadratic forms available are `(ê·n̂)²`, `(m̂·n̂)²` and `(ê·n̂)(m̂·n̂)`. The first two are reversal-even; **the third is reversal-odd.**

This matters because the entire first-order safety argument ran on parity: the unforced term `A(m̂·n̂)` was harmless *precisely because it is reversal-even*, so it cancels in the antisymmetric current and cannot shift a reversal-odd mean. **That protection does not extend to second order.** The odd quadratic shifts the tilt itself.

Tested:

- **C1 — untouched.** A second-order term is still a function of a single directed edge, so the locality step holds regardless of parity (T4).
- **C2 — a real effect.** At coefficient ±φ⁻³ the odd quadratic **raises the current 3.3×** over its absence, a larger effect than the even first-order term produced. Still clears: max O(J²) = 9.3 × 10⁻⁹ (T5).
- **C3 — clears.** K_lift 0.0528 vs baseline 0.0526 (T6).
- **The honest limit (T7).** K_lift at odd-quadratic coefficients 1, 3, 10 gives 0.0513, 0.0405, 0.0111 — it does not cross the threshold at any tested value, and in fact *decreases*. But the term is not inert by parity the way `A` was, and **a coefficient of order 1 or more would need its own argument rather than inheriting the first-order one.**

**This is a named residual, not a closed one.** At the framework's own scale it is harmless; the general case is not established, and the proposal should say so rather than claim second order has been dispatched.

## 4. Consequence for the proposal

The substantive verdicts across the three returns are uniform — **Q1 sound, Q2 sound, Q5 piece-1 correctly untouched, C2 amendment endorsed, κ conceded as scanned not derived, all three recommending ENACT WITH AMENDMENTS.** Combined with CONV-047's two valid seats, five independent reviews now agree on Q1 and Q5, and none has found a falsifier for the uniqueness claim.

**But CONV-048 is at 3 of 5 and cannot be adjudicated.** Two seats are outstanding. And the proposal's wording now needs one change earned from Gap 2: its clause "nor on the rate law terminating at first order" is **stronger than what has been shown.** What has been shown is that second-order terms are harmless *at the framework's scale*, with the odd channel newly identified and not bounded in general. The clause should be narrowed accordingly before any enactment.

## 5. Disposition

- **CONV-048 open at 3/5.** Not adjudicated, not enacted. CAPACITY-1's registered conditionality stands.
- **Gap 1 CLOSED** — negative A tested; C2 and C3 clear; the asymmetry recorded.
- **Gap 2 PARTIALLY CLOSED** — the reversal-odd second harmonic is now identified and tested at the framework's scale; **general second-order behaviour remains open and is a named residual.** Filed.
- **Proposal wording amendment owed** before enactment: narrow the first-order-truncation clause to what §3 actually supports.
- **Execution evidence** for Copilot and DeepSeek: request stdout. **Gemini's Q1/Q2 tiers to be read as T2**, not T1, at adjudication.
- **No verdict moves. No THEO registered. No count change.**
