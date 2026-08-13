# PREREGISTRATION — D-DS-INDEP: THE INDEPENDENT BOUNDARY CAMPAIGN (CONV-019 consensus mandate; committed BEFORE execution)

**Patch 3119 (13 Aug 2026). Executes the panel's Q1/Q6 mandate as
upgraded in the 3118 adjudication. GOVERNING CONSTRAINT, stated
first: NO COSMOLOGICAL QUANTITY appears anywhere in the campaign's
scripts or analysis — no c_Li, no corridor, no band, no fold. The
campaign outputs ONE number, the extrapolated transition spacing
d_s*, which is FROZEN in its results patch before any fold ever
sees it. The fold itself remains gated behind D-CHAN-ADD and
OBL-ARC-FIELD per Q6 (CLOSED-PENDING).**

## §1 — Instrument

The 3111 memoryless array core, verbatim dynamics (mixed species —
the physical weave; σ_n = 0.30; T = 3000), instrumented with
per-pair swap-event recording and periodic state snapshots. No
dynamical change of any kind.

## §2 — Sizes and cells (finite-size scaling per the Gemini catch)

| n_side | N (pairs) | d_s grid | seeds | venue |
|---|---|---|---|---|
| 3 | 27 | 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0 | 5, 11 | container |
| 4 | 64 | 2.5, 3.0, 3.5, 4.0, 4.5 | 5, 11 | container |
| 5 | 125 | 3.0, 3.5, 4.0, 4.5 | 5 | container |
| 6 | 216 | 2.5–4.5 (0.5 steps) | 5, 11 | **Kila6, queued post-Route-C** |

Container execution proceeds size-by-size across sessions as compute
allows; partial completion is committed per-part with the state
recorded; the extrapolation runs only when ≥ 3 sizes are complete.

## §3 — The four predeclared microscopic order parameters
(stationary window = final third; all computed per cell)

1. **f_b(d_s):** bound-state occupancy — fraction of (pair, Moment)
   with d_p ≤ d_s/2.
2. **ρ_swap(d_s):** partner-change rate — swap events per pair per
   Moment (pair lifetime τ = 1/ρ_swap is its declared reciprocal
   check, not an independent parameter).
3. **f_dwell(d_s):** superposition-dwell occupancy — fraction of
   (pair, Moment) with d_p < 1 GP.
4. **ξ_state(d_s):** state-correlation length — assign each pair
   centre b_i = 1[bound]; C(r) = ⟨δb_i δb_j⟩ binned over centre
   separations (periodic min-image); ξ = the separation at which
   C(r) first falls below C(first bin)/e (linear interpolation
   between bins; if C is non-positive at the first bin, ξ is
   UNDEFINED for that cell and reported as such).

## §4 — Transition location rule (frozen; convention-minimal)

For each order parameter P and size N: the transition
**d*(P, N) = argmax |dP/d(d_s)|** — the susceptibility peak —
computed by central differences on the grid with quadratic
three-point peak interpolation; grid-edge maxima are reported as
UNBRACKETED (no location claimed from an edge). **Extrapolation:**
d*(P, N) fitted linearly in 1/n_side (inverse linear size) over the
completed sizes; the intercept is d*(P, ∞). **The campaign's
output: d_s* = the mean of the defined d*(P, ∞) over the four
parameters, with spread reported; if the four disagree by > 0.75
l_P (peak-to-peak), the campaign reports SPLIT and the panel
adjudicates before any freeze.**

## §5 — Coincidence test (reporting only; no location authority)

The prior locators — the r = 0.5 crossing and the FAITHFUL-
attainability edge — are tracked per size and compared AFTER d_s* is
computed, answering the panel's question of which (if either) the
real transition coincides with. Neither has any role in §4.

## §6 — Use commitments

The extrapolated d_s* (or SPLIT) is committed in the campaign's
final results patch and FROZEN. No fold, no corridor comparison, no
c_Li computation occurs in this campaign or its patches. Escape
clauses: a cell failing the frozen stationarity criterion is
excluded by the classifier and reported; if fewer than three sizes
complete in-container, the extrapolation waits for Kila6. Kila6
Route C and the DM ledger untouched; Route C arrival still trumps
all.
