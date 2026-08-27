# **COMOVING BUILD — THE ERROR BUDGET IS FROZEN, BEFORE ANY SIZING.** The instrument reads the equation of state DIRECTLY off staged expansion (`1 + w = −∂ln ρ_Sea/∂ln V`) instead of inferring it from a fixed-box temperature scan, and its total error target is **σ_w ≤ 0.005** — four times tighter than the standing 3419 bound, which makes DESI-preferred w₀ a 20σ signal and F-W-1's −1.023 a 4.6σ one, so the instrument can adjudicate every live hypothesis in the lane. Budget allocated in quadrature (0.0048 total), reading rules and three guards frozen here, and **the one input the corpus cannot supply — the within-trajectory scatter s_within — is assigned to a pilot, not guessed**

**Patch 3435 (26 Aug 2026). DE lane, session 160. Executes item 1(a)
of the 3434 handover. Verify: `code/3435_comoving_error_budget.py`.
Next patch (DE): 3436.**

---

## §1 — What the instrument measures, and why it is not the fixed-box quantity

The fixed-box proxy infers w from a temperature scan:
**p ≡ d ln n_eq/d ln T**, with T ∝ 1/a and ρ_Λ ∝ n giving
**w = −1 + p/3** (3413). Every DE reading in the 3400–3419 arc runs
through that chain, and the chain's weak link was flagged at four
separate points: the box does not expand. Temperature is standing in
for expansion, and the substitution is an assumption, not a
measurement.

The comoving build removes the substitution. Under true staged
expansion, with ρ ∝ a^(−3(1+w)) and V ∝ a³:

> **1 + w = − ∂ ln ρ_Sea / ∂ ln V**

This is a direct read. No temperature proxy, no n_eq identification,
no threshold choice — and therefore none of the threshold-artefact
exposure that cost D-ENTITY-1 its verdict at 3419.

**Design (frozen): paired trajectories.** Each seed is carried
*through* the expansion rather than re-initialised at each volume, and
ln ρ_Sea is recorded at M stage points spaced uniformly in ln V across
a lever arm L = ln(V_final/V_initial). The per-seed OLS slope is fitted
first; the S seed-level slopes are then pooled. Pairing cancels the
seed-to-seed offset in ρ_Sea, which is the dominant nuisance in an
unpaired design and is exactly the variance the fixed-box campaigns
had to fight (the 4× seed spread re-attributed at 3172).

For uniformly spaced design points, sd(ln V) → L/√12, so

> **σ_w,stat = √12 · s_within / (L · √(M·S))**

where **s_within** is the residual scatter of ln ρ_Sea about the
trajectory fit.

---

## §2 — The target: why σ_total = 0.005, and not tighter

| hypothesis | \|w + 1\| | significance at σ = 0.005 |
|---|---|---|
| DESI-preferred w₀ = −0.90 | 0.100 | **20.0σ** |
| F-W-1 w = −1.023 (demoted 3422) | 0.023 | **4.6σ** |
| standing 3419 bound | 0.0198 | **4.0×** tightening |

Three things fix the number. It is **4× tighter than the standing
bound**, so a confirmation is new information rather than a
restatement. It puts **every live hypothesis above 4σ**, so the
instrument adjudicates rather than merely fails to exclude. And it
sits at the **knee of the cost curve**: statistical error falls as
1/√(M·S), so σ = 0.002 would cost 6.25× the runs for a discrimination
gain that no hypothesis on the table needs.

**Frozen quadrature allocation:**

| term | allocation |
|---|---|
| statistical (seeds × stages) | 0.0030 |
| finite-size extrapolation | 0.0030 |
| expansion-rate / adiabaticity | 0.0020 |
| estimator definition | 0.0010 |
| **quadrature total** | **0.0048** |

Finite-size is allocated equal weight to statistics deliberately. The
fixed-box campaign's own verdict at 3171/3172 was FINITE-SIZE-EFFECT;
a comoving build that budgets for statistics and hopes on size would
be repeating the lane's most recent structural lesson rather than
learning it.

---

## §3 — The design surface

Largest tolerable **s_within** at σ_stat = 0.003 (from
`code/3435_comoving_error_budget.py` §3):

| lever arm | M=6,S=8 | M=8,S=16 | M=12,S=24 | M=12,S=48 |
|---|---|---|---|---|
| V×4 (a×1.59) | 0.0083 | 0.0136 | 0.0204 | 0.0288 |
| **V×8 (a×2)** | 0.0125 | **0.0204** | 0.0306 | 0.0432 |
| V×27 (a×3) | 0.0198 | 0.0323 | 0.0484 | 0.0685 |
| V×64 (a×4) | 0.0250 | 0.0407 | 0.0611 | 0.0864 |

**Baseline design: L = ln 8, M = 8, S = 16, 128 total runs**, which
tolerates a 2.0% per-point scatter in ρ_Sea. The lever arm is the
cheapest axis in the budget — it enters linearly while runs enter as a
square root — so if the pilot returns a large s_within, **extend L
before adding seeds**. The ceiling on L is physical, not statistical:
the box must still contain the correlation length at V_final, which is
the pilot's second deliverable.

**Inverse view** (baseline L = ln 8): s_within = 0.02 needs 123 runs;
0.035 needs 378; 0.05 needs 771; 0.10 needs 3,084. At 24 logical cores
these are 5, 16, 32 and 129 runs per core — the last is the only one
that threatens the days-scale envelope.

---

## §4 — The one number this budget does not supply

**s_within is not in the corpus.** The fixed-box campaigns measured
var(f_b) (2.33e−4 → 5.2e−5 across sizes, 3172) — a partition variance,
not a density scatter, and measured without expansion. Transferring it
would be precisely the CONV-003 failure: same formula, stale
parameters, wrong observable.

So it is assigned, not assumed. **The pilot's whole job is to return
three numbers**, before any production run is sized:

1. **s_within(N)** at ≥ 2 values of N — the scatter of ln ρ_Sea about
   a short trajectory fit.
2. **The Sea relaxation time under staged expansion**, which fixes the
   minimum dwell per stage point. The fixed-box figure is ~15 Moments
   (3401); whether it holds while the box is growing is the question.
3. **The correlation length at V_final**, which caps L and fixes the
   minimum box.

Memory and wall-clock sizing follow from those. Nothing about N, box,
step count or ensemble is decided in this patch, because deciding it
now would be sizing to a guessed budget — the inversion the handover's
ordering exists to prevent.

---

## §5 — Guards, frozen with the budget

- **F-C1 — rate independence.** Two expansion rates separated by ≥ 4×
  in dlnV/dt must agree: **|w(fast) − w(slow)| ≤ 0.015** (3σ_total).
  The physical expansion is adiabatic to ~10⁻⁶⁰ in H·τ; every
  simulation is unimaginably faster, so rate-independence is not a
  nicety, it is the entire warrant for reading the result as an
  equilibrium equation of state.
- **F-C2 — finite-size extrapolability.** ≥ 3 values of N, with the
  extrapolated intercept's uncertainty folded into the 0.003
  allocation. A non-monotone or non-extrapolable N-trend voids the
  reading.
- **F-C3 — null-mode calibration.** With expansion frozen (L = 0) the
  engine must reproduce the fixed-box 3419 result inside its own
  error. This is the instrument validating against the thing it is
  built to test; if it cannot recover the known answer in the known
  regime, its answer in the new regime means nothing.

---

## §6 — Reading rules, frozen before the first run

| verdict | condition |
|---|---|
| **CONFIRM** | \|ŵ + 1\| ≤ 3σ_total **and** σ_total ≤ 0.005 |
| **REFUTE-PROXY** | \|ŵ + 1\| > 3σ_total **and** σ_total ≤ 0.005 |
| **INDECISIVE** | σ_total > 0.005 — report achieved σ and the binding resource; no reading |
| **INVALID** | any of F-C1, F-C2, F-C3 fails — no reading |

**REFUTE-PROXY yields a direction, not a value.** If the fixed-box
proxy is refuted, the measured magnitude is *not* thereby a reading on
dark energy; it requires its own preregistration to interpret. This
clause is written now because the temptation to promote a surprising
magnitude into a result arrives only after the surprise, and 3419's
guard is the lane's evidence that a rule written beforehand will
actually refuse.

**No pre-declaration is recorded**, per the 3434 §5 calibration note.
The lane's pre-declaration record stands at two correct of ten, and
both of last session's route authors were overturned by their own
executions. This is a confirm-or-refute instrument for a standing
conclusion; what the worker expects it to say is not information.

---

## §7 — Environment pinned (founder-reported, 26 Aug)

**VideoCPU** — Python 3.12.10 (64-bit), interpreter at
`C:\Users\DrThomas\AppData\Local\Programs\Python\Python312\python.exe`,
**numpy 2.5.2**, **scipy 1.18.1** (installed this session; absent
before), 24 logical cores / 16 physical, 32 GB RAM. Multiprocessing
start method is **spawn** (Windows default), so the engine keeps all
top-level work behind `if __name__ == "__main__":` and passes or
rebuilds per-worker state explicitly — the convention
`scripts/3140_n7_videocpu_runner.py` already follows.

**Machine ruling (PD-006, 3434) unchanged:** comoving build =
VideoCPU; Kila6 remains DM-lane; staged escalation only on a pilot
anomaly near resolution, via DM-lane queue coordination.

---

## §8 — Owed

- **Folder-convention divergence.** The registered convention places
  `.py` under `code/`; this lane has ~40 `.py` under `scripts/`. This
  patch follows the registered convention and creates `code/`. The
  resulting split is real and should be resolved by a mechanical
  consolidation pass, registered here as owed rather than settled
  silently in either direction.

---

# AMENDMENT — Patch 3436 (26 Aug 2026): the founder's Picture-B ruling promotes F-C1 from guard to estimator

**Verify: `code/3436_rate_extrapolation.py`. Next patch (DE): 3437.**

## §10 — The ruling

Asked whether the Sea settles as quickly while the box grows, the
founder ruled **Picture B**, with the mechanism stated directly:

> Space expands, and the DP-entities evaporate CPs and bind with other
> CPs, which then form DPs; those DPs bond and form new DP entities.

This is a **cycle with throughput** — entity → evaporated CP → DP →
new entity. At zero drive the cycle runs with zero net (detailed
balance). Under expansion it carries a net, and **that net is the
lag**. The Sea under expansion therefore occupies a *driven steady
state*, not equilibrium, and ρ_Sea carries a rate-dependent offset at
every finite expansion rate.

**This is internally consistent with the corpus**, which matters: it
is 3401's Le Chatelier resolution applied to the instrument. The net
formation rate was already established there as a restoring *response*
tracking expansion rather than an independent constant. Picture B is
that same statement seen from the measurement side, and 3419's
structural finding fits it too — entity COUNT nearly invariant while
binding WITHIN entities moves is what a throughput cycle with a
robust population looks like.

## §11 — Consequence: F-C1 is retired as a guard

§5's F-C1 required |w(fast) − w(slow)| ≤ 0.015. Under Picture B that
requirement is **wrong**, and would fail a correctly functioning
instrument. Rate dependence is now expected physics, not
contamination.

**F-C1 is therefore promoted from a guard into an estimator.** Measure
w at a ladder of expansion rates and fit

> **w(ṙ) = b₀ + b₁ṙ + b₂ṙ²**, reading **b₀** as the answer.

The physical universe expands at H·τ ~ 10⁻⁶⁰. **The intercept is the
physical answer** — not an idealisation of it. b₁ is reported as a
measured property of the driven Sea, explicitly *not* as a reading on
dark energy.

**Direction of extrapolation is the favourable one.** We are not
interpolating toward the physical rate, which sits ~59 orders below
anything simulable. We are extrapolating to zero, and linear response
holds *better* as drive weakens. The hazard is the reverse case: the
entire accessible ladder sitting in the nonlinear regime with the
linear regime beneath it. That is what the new guard tests.

## §12 — Amended design and budget

**Quadrature allocation — magnitudes unchanged, one term's meaning
changed:**

| term | allocation | change |
|---|---|---|
| intercept (rate-extrapolated statistical) | 0.0030 | was single-rate statistical |
| finite-size extrapolation | 0.0030 | unchanged |
| **residual nonlinearity in ṙ** | 0.0020 | **was adiabaticity guard slack** |
| estimator definition | 0.0010 | unchanged |
| **quadrature total** | **0.0048** | **σ_total ≤ 0.005 preserved** |

**Rate ladder selected: K = 4, span 8× (ṙ ∈ {1, 2, 4, 8} × ṙ_slow).**

| ladder | intercept inflation | total runs | wall-clock |
|---|---|---|---|
| K=3, span 4× | 1.225× | 576 (4.5×) | 10.5× |
| **K=4, span 8×** | **0.860×** | **378 (3.0×)** | **11.1×** |
| K=4, span 27× | 0.699× | 250 (2.0×) | 19.5× |
| K=5, span 16× | 0.677× | 293 (2.3×) | 14.2× |

Four points beat one even after extrapolating — the inflation factor
is **below unity**, so the ladder costs 3× the runs but returns a
*better* intercept than a single rate would have returned a slope.
The 27× span is rejected not on run count but on wall-clock: its slow
rung runs 27× long, and wall-clock is dominated by the slowest rung in
every ladder.

**Per-rate design at σ_per_point = 0.0035:** M=8, S=16 (128 runs)
tolerates s_within = 0.0237; M=8, S=24 or M=12, S=16 (192 runs)
tolerates 0.0290.

## §13 — Amended guards

- **F-C1 — RETIRED** as a guard (superseded by the estimator above).
- **F-C1′ — LINEARITY (new).** Require **|b₂| · ṙ_max² ≤ 0.0020**. If
  curvature exceeds the nonlinearity allocation, the ladder sits in
  the nonlinear regime → **INDECISIVE**, and the report must state
  whether a slower rung is reachable inside the envelope.
- **F-C2 — unchanged.**
- **F-C3 — AMENDED.** At ṙ = 0 there is no trajectory and no slope, so
  the old formulation (reproduce the fixed-box result at L = 0) no
  longer describes a null mode. It now checks that **the cycle runs
  with zero net at zero drive** — the founder's mechanism at its own
  fixed point. An engine that shows a net at zero drive is broken in a
  way that would masquerade as dark energy.

**Reading rules (§6) unchanged in form**, applied to **b₀** rather
than to a single-rate slope.

## §14 — Pilot, amended

A fourth deliverable is added ahead of the production ladder:
**measure the lag response at two rates** and confirm the rate
dependence is visible and orderly at accessible rates. If it is not
visible, the ladder's lever arm is wasted and the design needs
rethinking before 378 runs are committed rather than after.

## §15 — Fence

Nothing here alters Λ, d_s^emp = 4.636, w = −1.00 ± 0.02, the
3400–3419 frozen conclusions, 3422, 3423, 3429, 3430, 3431, 3433, or
any ruling. §§1–4 and §6–§9 of 3435 stand as written; §5's F-C1 and
F-C3 are superseded above. The DM lane is untouched. Next patch (DE):
3437.
