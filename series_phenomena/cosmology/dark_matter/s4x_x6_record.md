# S4-X X6 RECORD — the matched-functional dual extraction, executed under the frozen prereg: **the extraction-window hypothesis is REFUTED — matched functionals SHARPEN the discrepancy** (F1 matched near window: 5.8σ; F3 matched k-space pole at identical k: 6.6σ; F2 far window: 1.4σ advisory/noise-limited) — the instruments disagree about the profile's SHAPE: HNC is near-pure-Yukawa (window map 0.997 → 1.018), the simulation is functional-dependent (1.12 → 1.26, growing toward small k); the frozen rule fires: **CLOSURE-ERROR CANDIDATE / UNRESOLVED STANDS**, PR1 remains unmet, X3 + X4 carry — and the contact-ordering paradox now DEEPENS (association physics should be stronger at the agreeing a_s = 0.02 point), making PR3's independent external-field χ the natural arbiter

**Patch 2735, 21 July 2026. Executed under the prereg frozen in
`code/2735_s4x_x6_dual_extraction.py` (self-validation gate PASSED:
the local hd-exposing solver copy reproduces the committed 2721
ratios to 4 decimals before any new number was read). All inputs =
committed artifacts (data/s4e_chains/; the 2721 solver). Reasoning:
`reasoning/2735.md`. 79.5% not in scope.**

## §1 — The battery (a_s = 0.04 unless noted; sim errors X1-corrected; HNC ±1.5% floor)

| Functional | Simulation | HNC (same functional) | Δ |
|---|---|---|---|
| F1 slope, window (0.08, 0.546) | 1.1158 ± 0.0203 | 0.9688 | **5.82σ** |
| F1 at a_s = 0.02, window (0.04, 0.546) | 1.0265 ± 0.0423 | 0.9898 | 0.82σ |
| F2 slope, window (0.40, 0.88) | 1.2216 ± 0.1449 | 1.0179 | 1.40σ (ADVISORY: sim error > 10%) |
| F3 pole, k²/S_zz intercept, shells n² = 1–3 (k = 2.77/3.91/4.79) | 1.2605 ± 0.0373 (A: 1.242, B: 1.277) | 0.9967 | **6.56σ** |

HNC window-sensitivity map (end 0.88): [0.08→] 0.9969, [0.20→]
1.0096, [0.40→] 1.0179 — a ~2% spread: **HNC's profile is essentially
Yukawa.** The simulation's extraction spans 1.12–1.26 across
functionals, rising as the functional weights larger r / smaller k.

## §2 — What X6 settles and what it deepens

1. **Settled: the discrepancy is NOT extraction geometry.** X1's
   named candidate mechanism is refuted by its own frozen test —
   identical windows and identical pole fits at identical k disagree
   more, not less. Two disciplined instruments are measuring
   genuinely different correlation SHAPES at a_s = 0.04.
2. **The new diagnostic signature:** the discrepancy GROWS toward
   small k (pole functional worst at 6.6σ; chains agree with each
   other, A 1.242 / B 1.277). The simulated Sea's long-wavelength
   charge fluctuations are MORE suppressed (stronger screening) than
   HNC predicts.
3. **Deepened, honestly: the contact-ordering paradox.** Short-range
   association physics (the natural culprit for extra structure) is
   STRONGER at a_s = 0.02 (βv(0) = 2.05) than at 0.04 (1.02), yet
   0.02 agrees at every functional tested. No candidate mechanism on
   the table survives this ordering untested; the record therefore
   CLASSIFIES nothing beyond the frozen class and lists, without
   ranking: HNC closure error with non-monotone a_s dependence;
   a k-space finite-size/Ewald systematic specific to the 0.04
   chains (disfavored by A/B consistency and by SIZE-S/L agreement,
   but not excluded — X4's second sizes at small a_s test it);
   genuine soft-core physics at the 0.04 point. 
4. **The arbiter is already chartered:** PR3/X5 — the weak
   external-field measurement — determines χ(k) INDEPENDENTLY of the
   equilibrium fluctuation relation, on the same footing for both
   instruments' predictions. X6 elevates X5 to co-lead with X4.
   X3 (one longer 0.04 chain) retains its role as fluke-exclusion.

## §3 — Status

PR1: **unmet** (unexplained discrepancy now 5.8–6.6σ under matched
functionals); promotion barred; rider v2.5 governs; monotonic
character unthreatened (all alternation tests remain 0). Execution
order forward: **X4 ladder (with X2's small-k instrumentation
merged and second sizes at a_s ≤ 0.01) and X5 external-field, in
parallel as resources permit; X3 replication; AUTOMATON-1 prereg
independent.** Adverse-capable ledger: two consecutive worker-favored
hypotheses (error inflation; window mismatch) killed by their own
frozen tests in two consecutive patches.
