# N2B-ROB-1 pre-registration: the aimed-convention sensitivity envelope on the assembly chain — lateral offset, orientation, and approach-face perturbations at chain level, committed before any run

**Patch 2630, 20 July 2026. Status: N2B-ROB-1 OPENED at pre-registration; NO run
performed.** This is Seat 1's declared founder-free cell (2618 §5 ROB-1: "aimed-
convention sensitivity study (aim offsets, orientation perturbations, impact-
parameter variations)"), executed at the level where the WIN lives: full-chain
4→8 completion. Governed by this document and the chain lineage (2598 → 2604 →
2610–2614 correction → 2615/2616) only. Verify: none at prereg.

## 0. Target and framing

The WIN's existence claim is scoped to the aimed convention (FW-1). ROB-1 asks:
**how large a systematic aim error does the aimed convention tolerate before the
chain stops completing?** A finite envelope is a FEATURE, not a failure — the claim
was convention-scoped from registration; this cell draws the convention's walls.
Perturbations are applied UNIFORMLY to every stage launch (modeling a
systematically mis-aimed protocol, the realistic error class the 2612 artifact
exemplified). **Launch convention (mandatory clause):** all launches use the
registered AIMED launcher `scan_cell` (2611 artifact, exec-loaded verbatim) —
centroid-relative by construction, re-centered at every stage, so drift
compensation is inherent to the instrument; per-stage |Δcen| at capture is
reported. The legacy fixed-column `stage_capture` is NOT used for any launch
(it is the 2612 artifact's source protocol; excluded by citation).

## 1. Registered inputs (verbatim; zero freedom)

Engine + launcher: exec-load of the registered 2611 artifact (→ 2604 engine);
`scan_cell`, `n1_gamma`, constants are the registered objects. η = 0.5. Declared
channel: axis +z, b = 0.5D, φ = 0, v = 0.10c (CH, 2604), charge alternation
5(−1), 6(+1), 7(−1), 8(+1). **Chain builder (this cell's uniform instrument):**
settle the 4-square (TC = 60, the regen base), then four sequential `scan_cell`
launches on the (perturbed) channel; stage BOUND iff CAP ∧ whole-object
dmax < 3D, both dt (dt-union {1/100, 1/200} unconditional, the 2615 economy for
the 1/200 leg per stage); chain propagates on the 1/100 path; COMPLETE requires
all four stages BOUND dt-stably plus the finished 8-object settled at 1/200
(TC = 60, dmax < 3D). Width: **w = 4 (steep) primary**; **w = 2 (soft) confirm**
at the registered channel + the largest steep-surviving perturbation per family.

## 2. Control (gating; run FIRST; failure stops the cell unread)

**C-R′ — uniform-launcher registered-channel control:** the chain builder at the
UNPERTURBED channel (axis +z, b = 0.5D, φ = 0) completes at w = 4, dt-stable, with
the settled 8-object inside dmax < 3D. (The registered chain completions used
mixed launchers across their lineage; this cell's comparisons are valid only if
its own uniform aimed instrument completes at the registered channel. If C-R′
fails, RC4: raw disclosed, nothing read, corrected re-entry only.) The w = 2
member of C-R′ runs with the soft confirm block and gates only the soft rows.

## 3. Perturbation families (frozen grids; applied to every stage)

- **F1 — lateral offset (impact parameter):** b ∈ {0.0, 0.5*, 1.0, 1.5, 2.0}D
  (φ = 0, axis +z). (* = registered value, satisfied by C-R′.)
- **F2 — orientation:** φ ∈ {15°, 30°, 45°} (b = 0.5D, axis +z; φ = 0 is C-R′).
- **F3 — approach face:** axis ∈ {+x, +y, −z} (b = 0.5D, φ = 0; +z is C-R′).

Per chain, report: per-stage verdict pairs (both dt), Sea, gmax, |Δcen| at
capture, stage-of-first-failure if any, settle numbers on completion. Any FRG at
any stage is reported in its own line (N3-relevant, the 2609 precedent).

## 4. Frozen readings

- **RR1 — ROBUST-ACROSS-ENVELOPE:** every tested perturbation in F1–F3 completes
  dt-stably at w = 4 → ROB-1 DISCHARGED: the aimed convention tolerates ≥ 2.0D
  offset, ≥ 45° orientation error, and arbitrary face choice at chain level within
  the tested grid; the envelope registers with its grid bounds stated.
- **RR2 — BOUNDED ENVELOPE (expected class; NOT adverse):** some perturbation
  fails dt-stably → the envelope registers with its boundary per family (largest
  completing / smallest failing) and the stage-of-first-failure map; ROB-1
  DISCHARGED-WITH-BOUNDS. A finite wall is the convention's honest shape.
- **RR3 — UNSTABLE / CONTROL FAILURE:** C-R′ fails or dt-instabilities prevent a
  boundary from being drawn → nothing reads; RC4.
- **Soft rows:** confirmation-grade only; they gate the sentence "the envelope is
  width-shared" and nothing else.
- **Fences:** existence only — no rates, no σ, no flux statements (perturbed-
  channel completions are still aimed-convention results; FW-1 rides every
  consumer sentence); no promotion; DISC block untouched; deposits reported are
  endpoint-ledger S_cum values per SINK-OBS-1 (2629) and carry no schedule
  claims; 79.5% untouched.

## 5. Bookkeeping

Next patch: execution under this document only. Verify script
`code/2631_n2b_rob1.py` (stages control | f1 | f2 | f3 | soft), foreground-chunked.
