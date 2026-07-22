# S4-X X5 RECORD — the external-field arbiter, executed under the frozen 2737 prereg, WITH the forensic chain it triggered: **V1 (PR3) FAILS — the driven first-moment response sits ABOVE the fluctuation spectrum at all three shells** (S_drv/S_zz ≈ 1.4–1.7; jointly significant even under conservatively doubled per-mode errors) — the frozen rule fires: **SIMULATION-ESTIMATOR-SYSTEMATIC; the X6 pole numbers are QUARANTINED**; the forensic ladder then eliminated implementation drift (|S_maint − S_fresh| ~ 1e-12; suppression REPRODUCES with fresh sums in a new box/seed) and validated the harness normalization on the exact ideal-gas FDT case (all modes consistent with 1.000) — leaving ONE leading hypothesis, stated with its competitors and its designed discriminator: **a slow relaxation component in the interacting Sea's small-k charge dynamics that short chains under-sample in the VARIANCE (biasing S_zz low) — X3-LONG decides**

**Patch 2738, 21 July 2026. Prereg frozen at 2737 before any run;
verdicts enacted as committed; the two forensic runs (X5b drift/fresh
audit; ideal-gas calibration) are recorded in §3 with their inline
scripts preserved in this record's commit. Driven-run data archived
(data/x5_runs/). Reasoning: `reasoning/2738.md`. 79.5% not in scope.**

## §1 — The frozen battery

Linearity (V-LIN): PASS all four modes (full vs half amplitude,
0.40–0.62σ). Direction (V-DIR): k1x vs k1y 2.23σ — FLAGGED by the
frozen rule; resolved in §3 as noise-scale, not anisotropy (the
ideal-gas calibration shows per-mode driven errors of this scale;
R8 not substantively triggered). **V1 (PR3): FAIL at every shell** —
n²=1: S_drv 0.2307 ± 0.0205 vs S_zz 0.1374 ± 0.0029 (4.5σ);
n²=2: 0.3543 ± 0.0356 vs 0.2473 ± 0.0079 (2.9σ);
n²=3: 0.5474 ± 0.0287 vs 0.3259 ± 0.0178 (6.6σ). References at the
same k: HNC-like 0.196 / 0.328 / 0.422. The driven probe scatters
around-to-above HNC; the fluctuation numbers sit 25–30% below it.
Per-mode IACT measured directly on the driven series: τ = 1.0–2.3
samples (ESS 66–151) — BOTH estimators sampling-verified at the
windowed level. **Frozen V2 enacted: classification updates to
SIMULATION-ESTIMATOR-SYSTEMATIC; the X6 pole functional and its
6.6σ statement are QUARANTINED.**

## §2 — Why this is the strangest and most productive result of the campaign

Within an exactly-sampled Gibbs measure, driven mean and fluctuation
variance MUST agree (FDT is a theorem there). A sampling-verified
disagreement therefore indicts either an implementation or the
"exactly-sampled" premise. §3 executed the audit ladder the same
night.

## §3 — The forensic ladder (each step eliminating a named candidate)

1. **Implementation drift — ELIMINATED.** Fresh-summation audit run
   (N = 432, new seed): max |S_maintained − S_fresh| = 1.05e−12 over
   the run; maintained and fresh S_zz identical to 4 decimals; AND
   the small-k suppression REPRODUCES (0.177/0.334/0.434 vs HNC-ref
   0.249/0.399/0.499) — a sixth independent chain, second box
   geometry, estimator-independent. The suppression is a property of
   the sampled chains, not of the accumulator.
2. **Harness normalization — VALIDATED.** Ideal-gas driven run
   (interactions off; FDT exact and analytic): S_drv per mode =
   0.73 ± 0.26 / 1.21 ± 0.19 / 0.78 ± 0.26 / 0.88 ± 0.08 — all
   consistent with the exact 1.0000; no factor-level bug; and the
   calibration exposes the honest per-mode noise scale of driven
   measurements (±0.1–0.25 at this depth), motivating the
   conservative doubling under which the §1 discrepancies remain
   jointly ~4σ.
3. **Triad mixing (k1x + k1y = k2) — INSUFFICIENT** (O(βε) ~ 7%
   relative, one mode only; the pattern spans all shells including
   the triad-free k3).
4. **Surviving leading hypothesis (stated, not enacted):** the
   interacting Sea at a_s = 0.04 carries a SLOW relaxation component
   in its small-k charge dynamics (plausibly association/pair
   dynamics), with τ_slow beyond the windowed-IACT horizon of every
   chain run to date. Consequence: short chains under-accumulate the
   slow component's VARIANCE — S_zz biased LOW — while HNC and
   (partially) the driven mean sit higher; the same bias would
   contaminate the far-field profile curvature behind the original
   κ_fit excess, and its a_s-dependence could dissolve the
   contact-ordering paradox. Competitors kept alive: a residual
   harness effect below the calibration's ±20% power; heavy-tailed
   relaxation biasing the driven mean instead. 
5. **The discriminator, specified for X3-LONG (prereg to freeze at
   execution):** ONE chain, a_s = 0.04, ≥ 20,000 sweeps (≥ 10× any
   chain to date), sampling every 25 sweeps, per-mode IACT with
   explicit tail diagnostics (multi-window τ; blocked variance vs
   block length), BOTH estimators in the same chain (fresh S_zz +
   an embedded weak drive). Signature: if S_zz(chain length) GROWS
   toward S_drv/HNC as the window opens, the slow-component
   hypothesis closes the entire complex — X5, X6, X1's paradox, and
   the original tension — in one mechanism; if S_zz is flat at the
   suppressed value, the disagreement is physical and the automaton
   inherits it.

## §4 — Status

**PR3: FAILED at these chain lengths** — recorded plainly; GPT's
criterion did exactly its designed job, catching the fluctuation
estimator asserting what the driven probe denies. **PR1:**
classification now SIMULATION-ESTIMATOR-SYSTEMATIC (slow-component
candidate), confirmation delegated to X3-LONG; promotion remains
barred. **Unthreatened throughout:** the monotonic character (every
alternation test still 0), the a_s = 0.02 concordance, the HNC
GP-limit statement, rider v2.5, and the 79.5%. The campaign's
adverse-capable ledger now reads: three consecutive worker-side
hypotheses (error inflation; window mismatch; estimator validity)
each executed by its own frozen test, each execution narrowing the
mechanism space — the record is converging the hard way, which is
the only way that counts.
