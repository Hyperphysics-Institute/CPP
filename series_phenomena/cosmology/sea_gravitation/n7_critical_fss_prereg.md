# PREREGISTRATION — THE n = 7 CRITICAL-FSS CAMPAIGN (the N216 CHALLENGE's resolution instrument), FROZEN BEFORE THE RUN; venue: VideoCPU (16-core, NEW MACHINE — GPU offered and DECLINED for determinism); runs IN PARALLEL with Kila6's Route C

**Patch 3140 (15 Aug 2026). Freezes the analysis form per the 3130
declaration ("the FSS form and its fit window frozen BEFORE the
run"). The founder made VideoCPU available this session; the
campaign therefore no longer waits for Route C.**

## §1 — Instrument and cells

The v2 campaign instrument UNCHANGED
(`scripts/3120_ds_indep_campaign.py`); n_side = 7 (343 pairs,
Nc = 686); grid d_s ∈ {1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0};
seeds {5, 11}; T = 3000; NO cosmological quantity anywhere.
Runner: `scripts/3140_n7_videocpu_runner.py` — one cell per
process, 14 parallel workers, JSON checkpointing per cell
(crash-safe resume). GPU DECLINED: challenge-resolution data must
be bit-reproducible under seeds; CPU numpy guarantees it.

## §2 — The frozen analysis (the critical form)

Per-parameter peaks by the 3119 §4 susceptibility rule, unchanged.
**Scaling ansatz: d*(n) = d*∞ + a·n^(−1/ν)**, fit over ALL sizes
with a defined interior peak (f_b: n = 3..7 expected; f_dwell:
its defined sizes), by exhaustive ν grid search
(ν ∈ [0.40, 4.00], step 0.02; linear least squares in n^(−1/ν) at
each ν; minimum SSE selects). Combination: the 3119 frozen rule —
mean over defined parameters, spread reported.

## §3 — The frozen resolution rule (the challenge's verdict words)

Let D = |d*∞(critical, combined) − 2.450|.
- D ≤ 0.182 ⇒ **CHALLENGE RESOLVES-CONFIRMING** (the 3130
  discrepancy attributed to the linear model's inadequacy; the
  frozen 2.450 stands).
- D > 0.182 ⇒ **CHALLENGE STANDS-QUANTIFIED** (the critical value
  becomes the challenger's number).
EITHER WAY: the frozen 2.450 remains unrevised pending panel; the
full package (linear fits, critical fits, all five sizes, this
prereg) goes to CONV-021 alongside the Route C round. The d_s = 2.0
anomaly's n = 7 behavior is reported descriptively (bound to no
verdict).

## §4 — VideoCPU operating protocol

Machine registered: **VideoCPU** — 16-core compute machine, GPU
present (declined), repo at `~/Documents/GitHub/CPP`, standard
four-machine path pattern. Setup: clone, `pip install numpy
--break-system-packages` if needed, then
`python scripts/3140_n7_videocpu_runner.py run` (≈ 1–2 h wall at
14 workers), then `python scripts/3140_n7_videocpu_runner.py
analyze` and paste the printed summary block back to the worker.
State persists in `scripts/3140_n7_state.json` (machine-local
backup; the pasted summary is the reporting channel).
