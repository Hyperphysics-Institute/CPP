# ROUND-2 AMENDMENT — GEOMETRIC DEFECT IN THE ×4-WINDOW SPEC; ENSEMBLE RESPECIFICATION

**Patch 2905. Committed BEFORE any round-2 leg is executed or read; the
2906 execution record follows in a separate commit so the ordering is
provable in `git log`.**

---

## §1 — DEFECT IN THE FROZEN ROUND-2 SPEC (worker error, recorded)

The §4 round-2 spec of `mobile_sea_differential_record.md` (Patch 2904)
froze windows ×4 without checking transit length. At those windows the
source's transit β·(T_eq + T_meas) is 22 (β = 0.05), 34 (β = 0.10), and
58 (β = 0.20) length units, against a Sea cylinder of length 30: **for
β ≥ 0.10 the source exits the Sea mid-measurement.** The spec as frozen
is infeasible. The worker failed to check this before freezing — same
lapse class as the 2886 configuration failures, caught this time before
execution rather than after.

## §2 — AMENDED ROUND 2 (equal statistical power, fixed geometry)

**Observable and bands UNCHANGED** from
`mobile_sea_differential_amendment.md`. Replaced: the single ×4 window
becomes an **ensemble of 4 phase-staggered transits** per β, each at the
round-1 grid-matched window (which fits the geometry: transits 7, 11.5,
20.6 units, all inside the cylinder with buffer):

- Phases: the source's start x is offset by **{0, 0.625, 1.25, 1.875}**
  = k·(spacing/4), k = 0..3. The four quarter-phases cancel the
  washboard's fundamental harmonic exactly, in addition to the
  common-mode subtraction.
- Per β: 4 mobile legs + 4 frozen legs, pairwise differenced at equal
  phase; **ΔD(β) = the ensemble mean of the four differences**;
  ensemble scatter reported.
- Floor: the same 4-phase procedure at β = 0; ΔF₀ = |ensemble-mean
  ΔD(0)|; **Q_Δ = 5·ΔF₀ as before. Bands, β grid {0.05, 0.10, 0.20},
  fit, provisional status, and the frozen null-interpretation note all
  carry over verbatim.**
- Total Moments equal the ×4 spec (same raw power), with better
  systematics.

## §3 — EXECUTION INFRASTRUCTURE CHANGE, DECLARED

To fit the ensemble in the per-call compute cap, the retardation solve
gains a compiled (numba) kernel with **identical float64 numerics and
identical bisection logic** to the committed numpy path. Gate, frozen in
advance: on identical state, kernel and reference must agree on the
source's SSV_net to **≤ 1×10⁻¹⁰ absolute** over a 10-Moment comparison,
and V1/V2 must PASS on the kernel path; the validation output is
committed with the execution record. If the gate fails, round 2 runs on
the reference path at whatever pace that imposes.

**Worker expectation: CANCELLATION, unchanged, declared a fourth time.**
