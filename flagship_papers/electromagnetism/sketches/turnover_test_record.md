# EXECUTION RECORD — TURNOVER TEST: **REFUTED, DECISIVELY** — THE DRIVE SUSTAINS AND GROWS THROUGH β = 0.30; THE HYBRID'S TURNOVER WAS ITS OWN ARTIFACT (MECHANISM OPEN); THE DIRECT FIVE-β DATASET BOUNDS THE TRUE CURVATURE AT O(1)

**Patch 2924. Executed against the FROZEN prereg of Patch 2923.
Driver `code/2924_turnover_driver.py` (24 paired 2907-class engine
runs at the frozen literals: β = 0.25, T = 50; β = 0.30, T = 33).
Archive: `data/2924_turnover_results.json`.**

## §1 — FROZEN VERDICT

| β | Δ values (10⁻³) | M | SE | M/SE | positive |
|---|---|---|---|---|---|
| 0.25 | +1.08, +0.63, +1.31, +2.78, +2.59, +4.72 | **+2.19e-3** | 0.62e-3 | **+3.55** | 6/6 |
| 0.30 | +3.70, +3.76, +2.75, +3.25, +5.20, +5.52 | **+4.03e-3** | 0.45e-3 | **+9.00** | 6/6 |

Both β satisfy the REFUTED band (M ≥ +2.0e-3 with M/SE ≥ +2.0);
monotone increasing between the test points; 12/12 legs positive; no
leg failed its symmetry gate; no seed substitutions.

**VERDICT: TURNOVER REFUTED — sustained forward drive.** The hybrid's
point predictions scored: D(0.25) ≈ +0.4e-3 (measured +2.19e-3,
~3σ off) and D(0.30) ≈ −1.6e-3 (measured +4.03e-3, **12σ off,
wrong sign**). The direct-trend prediction (both ≥ +3e-3) scored
half: 0.30 yes, 0.25 no.

## §2 — THE HYBRID'S ARTIFACT: PRIME SUSPECT TESTED AND KILLED

Suspected mechanism (window-support truncation: ξ_ret exits the
measured pattern window increasingly with β): **FALSE** — the outside
fraction is 23–31%, oscillating with the discrete cell columns, flat
in β. The hybrid's high-β shape failure is real but its mechanism is
**unidentified**; registered as OPEN-HYB-SHAPE-1 (candidates: window
non-convergence of the co-moving pattern at short T; β³ basis
leakage; kernel-weighted rather than counted truncation). It is
deprioritized: the direct instrument answers the arc's question, and
the hybrid's low-β linear output (k_h, thrice validated) is not in
doubt.

## §3 — THE DIRECT FIVE-β DATASET (unbanded fit, disclosed)

D/β = {12.0, 15.2, 13.8, 8.7, 13.4}e-3 across β = {0.05, 0.10, 0.20,
0.25, 0.30}. Weighted (β, β³) fit: k = +1.366e-2,
**c_direct = +0.91 ± 2.40** (16–84%: −1.5 .. +2.8), χ²/dof = 1.23.

- **No drag onset anywhere in the measured range.** cβ² ≤ ~0.08 at
  β = 0.3 even at the central c.
- The catastrophic curvature readings of the hybrid rounds (c ~ 16–20)
  are dead: they were basis and instrument artifacts in sequence.
- The static-Sea analytic target c = 1/5 sits comfortably inside the
  direct band. So does 0. **The direct instrument bounds c at O(1)
  and cannot decide the 1/5 question:** reaching σ_c ≈ 0.05 by brute
  ensemble scaling needs ~2000× the legs — the 2908 power wall,
  re-derived for the direct method.

## §4 — DISPOSITION

The precision route to c is NOT more legs. Two routes remain, in
priority order per the standing queue: (1) **the analytic derivation
of c = 1/5 from the round-trip angular moments** — queued since 2900,
cheap, and now the highest-leverage item in the arc: an analytic
1/5 confronted with the direct bound c = +0.9 ± 2.4 would close the
static-channel question without another engine Moment; (2) a repaired
hybrid (contingent on OPEN-HYB-SHAPE-1). For B1 and Newton I, the
present state is materially IMPROVED: the drive is measured
near-linear with no reversal to β = 0.3, and the exact-linearity
question is now a bounded, sign-stable target rather than an
apparent catastrophe.

## §5 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand. CONJ-FP-1: A HOLDS, B CLOSED; curvature: bounded O(1)
(direct), precision OPEN. Anti-screening OPEN (2918).
OPEN-HYB-SHAPE-1 registered (this patch).
