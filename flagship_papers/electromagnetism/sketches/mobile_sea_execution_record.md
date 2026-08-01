# EXECUTION RECORD — MOBILE-SEA DRESSED DRIVE, BASE GRID

**Patch 2903. Executed against the frozen bands of
`mobile_sea_moving_source_prereg.md` (Patch 2902), which was committed
BEFORE this run; the ordering is verifiable in `git log`.**

# VERDICT: **INCONCLUSIVE** — on two independent frozen grounds.

**The worker's declared expectation was CANCELLATION. This run supports
no outcome, including that one.**

---

## §0 — TWO PRE-EXECUTION ENGINE CORRECTIONS (committed this patch)

1. **Grid-asymmetry defect, caught by inspection before any dressed
   number was read:** `arange`-built grids were reflection-asymmetric
   (xs = −16…+14, ys = −8…+7), seeding a spurious fore/aft bias into the
   axial observable — the estimator-defect shape this arc has caught four
   times, this time caught *before* the measurement. Fixed to symmetric
   construction; the β = 0 floor improved 1.68×10⁻³ → 1.10×10⁻³ (30-Moment
   window) and per-Moment chatter halved.
2. **Warm-started retardation bisection** (previous Moment's retarded
   times + 1 as bracket centre, fallback to full bracket on failure):
   ~1.75× speedup at identical declared precision; V1/V2 re-validated
   bit-identical PASS.

## §1 — RESULT (base configuration, 60-Moment window)

F₀ = |D(0)| = **9.17×10⁻⁵**; Q threshold 5·F₀ = **4.58×10⁻⁴**.
Data: `data/2903_base_grid_results.json`; driver:
`code/2903_dressed_execution.py`.

| β | D(β) | vs Q | sign |
|---|---|---|---|
| 0.05 | **+1.996×10⁻³** | passes | forward |
| 0.10 | **−2.973×10⁻³** | passes | **backward** |
| 0.15 | **−0.906×10⁻³** | passes | backward |
| 0.20 | **+0.0028×10⁻³** | **FAILS** | ~zero |

## §2 — WHY INCONCLUSIVE, AGAINST THE FROZEN BANDS

**FAILURE 1 — SIGN NOT UNIFORM IN β** (frozen §4: "sign flips with β" ⟹
INCONCLUSIVE). Forward at 0.05, backward at 0.10–0.15, zero at 0.20.

**FAILURE 2 — Q FAILS AT β = 0.20** (|D| = 2.8×10⁻⁶ < 4.6×10⁻⁴).

**Statistical reality check:** per-Moment chatter is 7–9×10⁻³; a
60-Moment window gives a naive standard error ~1×10⁻³, so every entry in
§1 is a ≲3σ number. **No entry is individually trustworthy, and the
frozen guards are doing at 2903 exactly what they did at 2886: preventing
a pattern of underpowered numbers from becoming a verdict.**

## §3 — OBSTACLE DIAGNOSED

The β = 0 floor measures *static* noise, but a moving source samples the
Sea's grid periodicity (spacing 2.5): a **transit-lock oscillation** at
frequency β/2.5 per Moment that a fixed 60-Moment window averages poorly.
At β = 0.05 the measurement covers only 1.2 grid cells — essentially no
phase averaging — while at β = 0.20 it covers 4.8 cells. The ±2–3×10⁻³
scatter with alternating signs matches this artifact in size and
structure.

**Recorded without weight, because the guards exist precisely to stop
this kind of reading:** the point with the best phase averaging (β = 0.20)
reads zero — which is what full cancellation would look like, and also
what noise would look like.

## §4 — WHAT RESOLVES IT (registered; the sharp one is pre-registered
separately BEFORE being run)

1. **Windows matched to the grid-crossing period** — T_meas an integer
   multiple of 2.5/β, so transit phase averages exactly.
2. **Phase-averaging** over runs with the source's start offset by
   fractions of the grid spacing.
3. **A DIFFERENTIAL observable** — identical geometry, identical
   trajectory, identical window, run twice: Sea MOBILE vs Sea FROZEN;
   drive ΔD = D_mobile − D_frozen. The transit-lock systematic is
   common-mode and subtracts; the frozen leg carries no ZBW chatter. This
   is a **new observable and therefore gets its own pre-registration with
   its own bands**, committed in this same patch BEFORE any differential
   number exists: `mobile_sea_differential_amendment.md`. **The §4 bands
   of the original prereg remain frozen and untouched for the original
   observable.**

## §5 — STANDING

CONJ-FP-1: Condition A remains OPEN (this run yields no sign verdict);
Condition B stands CLOSED per 2895; LINK 2 and LINK 3 (substrate form)
remain OPEN. Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7
holds DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, and
the 7 July no-carried-velocity ruling all stand.
