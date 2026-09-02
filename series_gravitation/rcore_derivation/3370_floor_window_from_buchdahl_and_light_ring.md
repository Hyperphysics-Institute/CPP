# OPEN-GR-FLOOR-1 — The cap is boxed: 0.536 < u_max ≤ 1 (Buchdahl above, light ring below) — and the flagship arc is not robust inside the box

**Patch 3370, Session 161, 2 Sep 2026.** Verify `code/3370_floor_sensitivity_conv038_amend_verify.py` (26/26). Founder rulings R-FLOOR-FINITE / R-CELL-SIZE-OPEN (`founders_voice/founder_ruling_floor_finite_cell_size_open_2026-09-02.md`). Reasoning `reasoning/3370.md`.

**Standing:** the *window* is DERIVED (two bounds, each conditional as stated); the *value* is OPEN.

## §1 What closed and what didn't

- **Zero floor: CLOSED** (R-FLOOR-FINITE). SR-1's "collapses (r_eff → 0)" is superseded as physics; SR-1 corrigendum owed in its own lane.
- **Value: OPEN** (R-CELL-SIZE-OPEN). The founder has no picture for why the cell is the size it is. Neither Buchdahl attainment (`u = 1`) nor SR-1's `α_geom` has priority by authority.
- **SR-1 vs GR-1c: NOT a contradiction.** Both SR-1 candidates (0.5594, 0.2444) satisfy Buchdahl `u ≤ 1`. The two papers are consistent as *bound + candidate*. What was in dispute was only attainment, and the panel had already stripped that.

## §2 The lower bound — the founder's "criteria of reality," quantified

A GW150914-class ringdown matches Kerr quasinormal modes. Those are set at the light ring (areal `3μ`). An object whose surface sits *outside* the light ring has no photon sphere and no Kerr-like ringdown (Cardoso & Pani 2019 review; the standard exotic-compact-object result). So reality requires the saturation surface inside `3μ`:

    R(u) = (μ/u)(1 + u/2)² < 3μ   ⟺   u² − 8u + 4 < 0   ⟺   u > 4 − √12 = 0.536

on the exterior branch. Combined with Buchdahl:

    **0.536 < u_max ≤ 1,   i.e.   l_P/2 ≤ PSR_floor < 0.651 l_P.**

- `α_geom` (unit-insphere) = 0.2444: **empirically excluded** as a physical cap.
- `α_geom` (unit-circumradius) = 0.5594: clears the light ring by 4%.
- `u = 1`: mid-window.

This is a bound from observation, not from the substrate. It is the first quantitative statement about the cap that does not rest on either paper's premise.

## §3 Sensitivity — what the flagship inherits from the open value

| u_max | r̄_s/μ | R/r_S | lapse | c_*/c | Level-A cavity Δt (62 M_⊙) |
|---|---|---|---|---|---|
| 1 (GR-1c) | 1.000 | 1.125 | 0.333 | 0.500 | **2.15 ms** (3297) |
| 0.5594 | 1.788 | 1.464 | 0.563 | 0.641 | **0.14 ms** |
| 0.2444 | 4.092 | 2.576 | 0.782 | 0.804 | none — wall outside the light ring |

Every number in the R-core arc downstream of the floor — the 2.15 ms delay, the derived Kerr surface, the wall modes, the 188–194 Hz line — was computed at `u = 1`. Inside the admissible window the cavity length varies by more than an order of magnitude. **The flagship band is not robust to the floor value.** PRED-O-39 must carry that as a second caveat beside the boundary-phase caveat (CONV-038 Q4(iii)).

## §4 What would close the value

- **FLOOR-1(a)** — derive attainment at `u = 1`, or show the register can stop below it. A physical principle, not a story: what does a static cap at `u = 0.9` violate?
- **FLOOR-1(b)** — the interior bridge: what `u` means inside saturation (the panel's constant-u vs Einstein-interior equivocation).
- **FLOOR-1(c)** — the map `SSV_crit → u`: an invariant definition of the cell that holds one Planck energy. The founder has none; this is now a first-principles open problem in the lattice-scale sector (Tier 6, A11), not a normalisation choice.
- **Empirical tightening** — a resolved echo at the predicted delay would fix the wall and hence `u_max` directly; a null with adequate injection recovery would exclude `u = 1` at the echo's amplitude.

## §5 Consistency remark (in the founder's favour)

The founder's two rulings are consistent with each other and with the window: a finite floor (§1) whose magnitude is unexplained (§1) and whose admissible range is set by observation (§2). "Required to meet the criteria of reality" is, on this record, a bound and not yet a number — which is exactly what a founder who says he has no geometric argument should be saying.
