# PREREGISTRATION — THE L-6b SYSTEMATIC-CHANNEL MARGIN κ_sys FROM THE FROZEN ROUTE A ENSEMBLE (ALGORITHM FROZEN BEFORE COMPUTATION; CONV-017 CONDITION C-i)

**Patch 3051 (10 Aug 2026). Frozen BEFORE any estimand computation
(only file structure/metadata was inspected: keys, series length,
pair count, domains). Implements the CONV-017 adjudication §2
conditions C-i..C-iii. Verify script `code/3052_kappa_sys_margin.py`
must implement THIS text verbatim; the computation patch reports
whatever it prints. Gate consequences per adjudication §3 (G1).**

## §1 — Data and estimand

Data: `data/kmem2/` — 320 pairs × {step, ctrl} × {std (x_half=16),
dom (x_half=32)}; F(t), t = 0..239 Moments; β-step at t_step = 24.
PRIMARY (gating): the std domain, all 320 pairs. DISCLOSED
(non-gating): the dom domain, identical pipeline, one number.

Estimand: the SYSTEMATIC CHANNEL is the ensemble-mean paired response
Δ̄(t) = mean over pairs of [F_step(t) − F_ctrl(t)]. Stationary
response Δ_∞ = mean of Δ̄(t) over t ∈ [200, 240). Deviation
D(t) = Δ̄(t) − Δ_∞. **κ_sys** = the per-Moment decay factor of |D(t)|
in the post-transient region. Micro-chaos propagation (the D-KAPPA
amplification): enters as pair-to-pair scatter and is propagated
EMPIRICALLY by the pair bootstrap below — no analytic correction is
applied or needed at this grade.

## §2 — Frozen algorithm

1. σ(t): pair-bootstrap SD of Δ̄(t) (NBOOT = 10000, resample the 320
   pairs with replacement; master seed 30510810).
2. Post-transient boundary: t_post = 48 (= t_step + 1.5·x_half — the
   same T_BALL scaling that gives 36 at x=24; the ballistic transient
   is EXCLUDED from the κ_sys fit so transient decay cannot be
   laundered as systematic contraction).
3. Fit window W: the contiguous run t ∈ [t_post, 200) from t_post to
   the first t with |D(t)| ≤ 3σ(t).
4. **BRANCH-FIT** (if |W| ≥ 8): weighted least squares of ln|D(t)| on
   t over W, weights 1/σ_ln² with σ_ln = σ(t)/|D(t)|; slope s;
   κ_sys = e^s.
5. **BRANCH-BOUND** (if |W| < 8 AND ∃ t_c ∈ [t_step+1, t_post) with
   |D(t_c)| > 3σ(t_c), t_c = the LAST such t): the response reached
   the floor within the transient window; the frozen conservative
   bound κ_sys ≤ κ_bound = (3σ(t_post)/|D(t_c)|)^{1/(t_post − t_c)}
   is reported as the estimate (decay from the last resolved point to
   the floor, spread over the maximal interval — the SLOWEST decay
   consistent with the data).
6. **INDETERMINATE** (neither branch): G1 FAILS by construction.
7. CI: full-pipeline pair bootstrap (window/branch re-selected per
   replicate), 99% percentile interval on κ_sys (or κ_bound).
8. **GATE G1 (frozen): PASS iff the branch resolved AND the 99% upper
   bound κ_sys^{U99} < 1.** Margin δ = 1 − κ_sys^{U99}. Marginal
   (CI touching 1) or INDETERMINATE → G1 FAIL → the frozen Route C
   design class executes (adjudication §1) and item 1B returns to
   OPEN.

## §3 — Reporting (all of it, whatever it says)

κ_sys (or κ_bound) with the 99% CI and branch taken; δ; |W| and the
window; D(t) trace summary (peak, floor-crossing time); the dom-domain
disclosed number; the Route B x=28 tertiary consistency note (computed
post hoc, labeled as such, non-gating). No threshold moves after the
run; the verdict line prints PASS or FAIL in the G1 language only.
