# N2B-ROB-2 pre-registration: the economy-matched re-run of ROB-1's two undrawn cells (φ = 45°, +y face) — committed before any run

**Patch 2637, 20 July 2026. Status: N2B-ROB-2 OPENED at pre-registration; NO run
performed.** This is the declared successor from the ROB-1 record (2631 §4:
"finer-dt and/or economy-leg-matched re-runs of the two cells; a φ ∈ (30°, 45°)
refinement if a wall is wanted rather than bracketed") and the 2636 handover §3
successor list. Founder-free per the standing queue discipline. Governed by this
document, the ROB-1 prereg (2630) whose conventions carry VERBATIM except where
amended below, and the chain lineage (2598 → 2604 → 2610–2614 → 2615/2616 →
2630/2631). Verify: none at prereg; execution next patch under this document only.

## 0. Target and framing

ROB-1 (2631) registered two cells UNDRAWN-AT-THIS-INSTRUMENT: **φ = 45°** (axis
+z, b = 0.5D, w = 4) and **+y face** (b = 0.5D, φ = 0, w = 4). Both halted at
stage 7 dt-UNSTABLY with one disclosed signature: at dt = 1/100 the incident
MISSES cleanly (Sea = 2–3 MeV, γmax = 1.01) while at dt = 1/200 it captures. The
convicted mechanism is the instrument, not the physics: the registered 2611
launcher's declared 1/200 economy leg (`if dtf < 1/150: brief TC = 20 re-settle
of the 1/100-propagated object before launch`) means **the two dt legs launch at
marginally different object states** — invisible everywhere else, visible exactly
at marginal aim against the grown asymmetric 6-object. An instrument that
disagrees with itself at marginal cells does not draw walls there (2631
discipline, restated in the 2636 handover §5).

ROB-2 removes the mismatch and asks the question the cells were built to answer:
**do the two cells complete, halt, or remain marginal when both dt legs launch
at the identical object state?**

## 1. The matched instrument (the single amendment; everything else verbatim)

**`scan_cell_matched`** = the registered 2611 `scan_cell` with the economy
re-settle leg REMOVED: for every dt, the launch state is the propagated chain
state `(Hc, Vc)` as-is — no per-leg re-settle at any dt. Both dt legs of every
stage therefore launch at bitwise-identical initial data and differ ONLY in the
encounter integration step. This is the honest dt-union: identical initial
conditions, varying discretization. The amendment is one branch deletion; the
transverse-direction rule, launch distance (ext + 4D), classifier (registered B1
final-state form), and every constant carry verbatim by exec-load of the 2611
artifact. The chain builder carries verbatim from 2630 §1 (4-square settle
TC = 60 at 1/100; four sequential launches; stage BOUND iff CAP ∧ dmax < 3D both
dt; propagate on the 1/100 path; completion settle at 1/200, TC = 60, dmax < 3D).

**Disclosed consequence accepted in advance:** the finer-dt leg now starts from a
state carrying the coarse integrator's settle noise. That is the point — the
shared initial condition is what makes the dt-union read the ENCOUNTER's
discretization sensitivity rather than the settle's. If the matched convention
itself is the fragile element, C-M2 below is built to catch it.

## 2. Controls (gating; run FIRST; failure stops the cell unread — RC4)

- **C-M1 — matched registered-channel control:** the matched chain builder at
  the unperturbed channel (axis +z, b = 0.5D, φ = 0, w = 4) must COMPLETE
  dt-stably with the settled 8-object inside dmax < 3D. (The matched instrument
  must do what the registered instrument did at the registered channel.)
- **C-M2 — drawn-cell conservatism control:** the matched chain builder at
  **φ = 30°** (the drawn cell nearest the undrawn φ = 45°) must COMPLETE
  dt-stably. If removing the economy leg FLIPS a drawn cell, the instrument
  change is not conservative and NOTHING reads at the undrawn cells (RC4; the
  flip itself is disclosed raw and the envelope's φ = 30 entry acquires an
  instrument-dependence flag for adjudication — a control failure that is
  itself information, reported in the same font).

## 3. The two cells and the frozen escalation ladder

Full-chain runs under the matched instrument, w = 4 (steep), dt-union
{1/100, 1/200} unconditional:

- **Cell A:** axis +z, b = 0.5D, **φ = 45°**.
- **Cell B:** axis **+y**, b = 0.5D, φ = 0.

**Escalation (frozen now, executed without re-registration):** if a cell's
stage-7 (or any stage's) verdict pair STILL disagrees across {1/100, 1/200}
under the matched instrument, that cell re-runs once at dt-union
**{1/200, 1/400}**, propagating on the 1/200 path, completion settle at 1/400.
No further escalation; a cell that disagrees at both unions reads RM2.

**Conditional refinement (frozen now):** if and only if Cell A reads RM1-WALL
(halts dt-stably), one refinement chain runs at **φ = 37.5°** under the matched
instrument at {1/100, 1/200} to halve the (30°, 45°] bracket. No refinement runs
against an RM2 cell (refining an undrawn boundary is meaningless) and none runs
for Cell B (faces are discrete; there is nothing between +y and the drawn faces).

Per chain, report verbatim per 2630 §3: per-stage verdict pairs (both dt), Sea
(endpoint-ledger values per SINK-OBS-1, no schedule claims), γmax, |Δcen| at
capture, stage-of-first-failure if any, settle numbers on completion; any FRG on
its own line.

## 4. Frozen readings

- **RM1-COMPLETE (per cell):** the cell COMPLETES dt-stably under the matched
  instrument → the cell is DRAWN as a completion; the envelope extends (Cell A:
  orientation tolerance ≥ 45° at the tested grid; Cell B: 4 of 4 tested faces).
  The ROB-1 consumer sentence is superseded by the wider one, FW-1 riding.
- **RM1-WALL (per cell):** the cell HALTS dt-stably (both legs non-BOUND at the
  same stage) → the cell is DRAWN as a boundary; the envelope registers its wall
  (Cell A: φ-wall inside (30°, 45°], refined to (30°, 37.5°] or (37.5°, 45°] by
  the conditional chain; Cell B: +y is a face wall — a face-dependent
  completion map, registered as structure, FORM-relevant beside the 2631
  +x-geometry observation). A wall is the convention's honest shape (2630 RR2
  language); NOT adverse.
- **RM2-UNDRAWN-CONFIRMED (per cell):** dt-instability persists at BOTH unions
  under the matched instrument → the marginality is not the economy leg's
  artifact; the cell registers UNDRAWN-CONFIRMED with both unions' raw pairs
  disclosed, and the declared successor class becomes derivational
  (FORM-1-lineage: the marginal-aim boundary at the grown 6-object is a
  geometry question, not an integration question). No wall, no completion, no
  further re-runs at this instrument class.
- **RM3-RC4:** C-M1 or C-M2 fails → nothing reads; raw disclosed; corrected
  re-entry only.
- **Mixed outcomes compose per cell** (e.g., Cell A RM1-COMPLETE with Cell B
  RM2 is a legal composite; each cell reads independently).

## 5. Fences (verbatim 2630 §4 + this cell's own)

Existence only — no rates, no σ, no flux statements; FW-1 rides every consumer
sentence (all results are aimed-convention results); deposits quoted are
endpoint-ledger values (SINK-OBS-1) with no schedule claims; the DISC block is
untouched (v = 0.10c throughout; no high-γ consumer moves); no promotion; the
ROB-1 record is NOT edited — this record supersedes its two undrawn entries by
citation if RM1 fires, and confirms them if RM2 fires; **79.5% untouched under
every reading.**

## 6. Bookkeeping

Prereg: this document (Patch 2637). Execution: `code/2638_n2b_rob2.py`, stages
`controls | cells | escalate | refine` foreground-chunked; record:
`n2b_rob2_record.md` (Patch 2638). Reasoning fragments at both patches.
