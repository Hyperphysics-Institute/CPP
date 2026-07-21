# KINETIC-1 K1-S3 RECORD — the O(Γ) prediction, executed prediction-first by the declared method (two-component HNC on the exact simulated system): **at the GP-scale limit the declared method predicts κ_eff ≈ κ_D — ℓ_phys = d_DP/2 stands within the ~1.5% method floor** (HNC a_s→0 ladder: 1.021 → 1.004 → 0.996 → 0.986; implied ℓ = 0.1845 vs 0.1820 fm); the a_s = 0.02 simulation point AGREES (0.8σ); the a_s = 0.04 point shows a ~3σ TENSION, flagged to S4-X, sitting exactly where the seats suspected the simulation's error bars; the excess scales ∝ Γ^1.0 at fixed core; the validation gate FAILED its strict 0.5% threshold (0.9868 — the 1.3% extraction systematic that defines the method floor), and the first run's solver bug was CAUGHT BY THE GATE (long-range chain truncation; fixed by analytic renormalization; both disclosed)

**Patch 2721, 21 July 2026. Executed under the frozen 2718 charter §3.
The method (HNC, grid, split, fit window, validation gate, targets,
expected accuracy) was declared in the script header BEFORE any
coefficient was extracted; predictions printed before the target
comparison; nothing renamed after results. Verify:
`code/2721_kinetic1_s3_hnc.py`. 79.5% not in scope. Reasoning:
`reasoning/2721.md`.**

## §1 — Discipline events, same-font, first

1. **The validation gate earned its existence twice.** First run: the
   gate FAILED grossly (0.586) — an implementation bug (finite-box
   Dirichlet truncation of the non-decaying Coulomb piece inside the
   chain function γ) was caught BEFORE any prediction was read, and
   repaired by the standard analytic long-range renormalization
   (γ_d = γ_d^short + G_lr, G_lr transformed in closed form). Second
   run: the gate still FAILS its strict 0.5% threshold — 0.9868, a
   1.3% extraction systematic (pre-asymptotic fit window at the
   weak-coupling reference point + residual grid effects). The gate
   verdict stands as committed; its miss is quantified and carried as
   a **±1.5% method floor** on every prediction below.
2. All predictions printed before the comparison section executed;
   the comparison bands are the S4-E block errors combined with the
   method floor.

## §2 — The predictions (declared method, frozen extraction)

| a_s (fm) | HNC κ_eff/κ_D | S4-E target | combined deviation |
|---|---|---|---|
| 0.040 | 1.0206 ± 0.015 | 1.106 ± 0.023 | **~3.1σ — TENSION** |
| 0.020 | 1.0042 ± 0.015 | 1.036 ± 0.040 | 0.7σ — agrees |
| 0.010 | 0.9964 ± 0.015 | — | (ladder) |
| 0.005 | 0.9863 ± 0.015 | — | (GP-limit trend) |

**Γ-scaling (a_s = 0.04, frozen ladder):** excess = κ_eff/κ_D − 1 =
0.0067 / 0.0206 / 0.0541 at Γ = 0.080 / 0.225 / 0.637 — fitted
exponent **1.00**: linear in Γ at fixed core (characterization, not
theorem). S_zz(k→0) → 0 (0.005 at k = 0.38 /fm) — the perfect-
screening (Stillinger–Lovett-type) behaviour is respected.

## §3 — The promotion-relevant statement

**At the GP-scale (a_s → 0) limit — the limit the founder's
commitment 3 designates as physical — the declared method predicts
κ_eff/κ_D = 0.99 ± 0.015, i.e. NO net coupling excess: the physical
screening length is ℓ = 0.1845 ± 0.003 fm ≈ d_DP/2 = 0.1820 fm.** The
finite-core excess that S4-E measured is, per HNC, a property of the
soft-core regularization, vanishing in the physical limit. This is an
independent, declared-method confirmation of the rider-v2.5 continuum
candidate at the ~1.5% level — offered to the panel's promotion
refreeze, not self-promoted.

## §4 — The one tension, honestly framed and routed

At a_s = 0.04 the simulation says 1.106 ± 0.023 and HNC says
1.021 ± 0.015 — ~3σ apart, while the a_s = 0.02 point agrees. Two
candidate resolutions, both testable and NEITHER assumed: (a) the
S4-E error bars at a_s = 0.04 are optimistic (block-SEM without
integrated autocorrelation — precisely GPT's Q3 item 4, already
conceded once at 2714); (b) HNC under-predicts the excess where
βv(contact) ≈ 1 (closure error concentrated at the finite core).
**Routing:** S4-X (already named) now has a sharpened first task —
autocorrelation-aware re-analysis of the existing a_s = 0.04 chains
plus one longer chain — before any new physics is inferred from the
tension. The GP-limit statement of §3 does not depend on which
resolution wins (both leave the a_s → 0 prediction intact).

## §5 — Arc status

K1-S1 done (2719); **K1-S3 done — class: K1-S3-PARTIAL** (GP-limit
prediction clean and concordant; one finite-core tension flagged and
routed); K1-S2 (Gibbs/MaxEnt) remains, the arc's close item. The
consolidated KINETIC-1 report and the panel promotion-refreeze
dispatch follow K1-S2 per the economy rule.
