# D-DS-INDEP CAMPAIGN — PART 1 (n_side 3 complete, both seeds; n_side 4 seed 5 complete): the finite-size trend is VISIBLE (the f_b transition moves 3.42 → 3.20 across the first size step); two order parameters UNBRACKETED at the low grid edge per the declared escape; NO cosmological quantity computed anywhere

**Patch 3120 (13 Aug 2026). Executes `ds_indep_prereg.md` (3119)
part-wise as declared. Verify: `scripts/3120_ds_indep_campaign.py`
(+ raw state `scripts/3120_state_part1.json`). Seed agreement at
n = 3: ≤ 0.004 on every parameter at every spacing.**

## §1 — Curves (seed-averaged)

n_side = 3 (27 pairs), d_s = 2.0 → 5.0:
f_b 0.262 → 0.456 (monotone rise) · ρ_swap 0.497 → 0.522 (weak dome
peaking near 3.5–4.0) · f_dwell 0.262 → 0.071 (steep fall at small
spacing) · ξ_state 1.3 → 3.7 (rising, noisy, occasional UNDEF).

n_side = 4 (64 pairs), d_s = 2.5 → 4.5: same shapes; values within
0.01 of n = 3 at matched spacings (the curves themselves are nearly
size-converged; the SLOPES — which locate the transitions — are
what shift).

## §2 — Susceptibility peaks (the frozen §4 rule)

| parameter | d*(n=3) | d*(n=4) |
|---|---|---|
| f_b | 3.417 | 3.196 |
| ρ_swap | 3.076 | UNBRACKETED (edge) |
| f_dwell | UNBRACKETED (edge) | UNBRACKETED (edge) |
| ξ_state | 4.046 | UNDEFINED (missing values at large d_s) |

Dispositions, per the declared escapes: f_dwell's steepest change
sits below the grid at both sizes — it tracks a DIFFERENT, lower
transition (the dwell-occupancy collapse) and will report
UNBRACKETED unless the n ≥ 5 grids extend to 2.0; ρ_swap's n = 4
peak fell at the grid edge (its n = 4 grid starts at 2.5); ξ_state
is statistics-limited at n = 4 (the state field is near-uniform at
large spacing — more snapshots at n ≥ 5 may resolve it). **f_b is
the cleanly bracketed parameter at both sizes, and its transition
moves DOWN with system size: 3.42 → 3.20 — the finite-size shift
the Gemini catch predicted, now measured.** No extrapolation yet
(the frozen rule requires ≥ 3 sizes).

## §3 — Remaining

Part 2: n = 4 seed 11 (5 cells) + n = 5 seed 5 (4 cells, grid
extended to {2.0, 2.5, 3.0, 3.5, 4.0, 4.5} — a declared grid
extension for the edge-bracketed parameters, extending DOWNWARD
only, before any extrapolation exists to be influenced). Part 3:
extrapolation at three sizes. n = 6 remains queued for Kila6
post-Route-C. No fold, no corridor, no c_Li — here or anywhere in
this campaign, per the governing constraint.
