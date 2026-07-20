# C7-D2 execution record — VERDICT D2-NO-ENTRY (dt-stable, both phases) WITH THE NONMONOTONE CLAUSE FIRING AT THE TOP ADJACENCY — and a dt-STABLE SIGN FLIP at phase 0, a = 0.32, disclosed as data per the prereg's sign clause

**Patch 2650, 20 July 2026.** Execution under `c7_discriminant_campaign_prereg.md`
(2649) §2 ONLY — first arc of the frozen order D2→D1→D3. Verify:
`code/2650_c7_d2.py`, stages guardtest | pin | ladder, all run. Per the
campaign's composite-only rule: **this reading REGISTERS AND WAITS. No
adjudication sentence, no C7 sentence, no Branch-N re-reading occurs at this
patch.**

## 1. Controls — ALL PASS

- **Guard-trigger test (J4-2):** zero-denominator ratio path fires the guard
  (`inf`, no exception) — PASS.
- **C-D2 pin (the arc-abort gate):** the verbatim 2635 diagnostic reproduces
  EXACTLY under this loader — ratios **+0.94 / +1.10** at phases 0 / π/2
  (registered 0.94/1.10 class), reach-S base ring Etot **+2130.9** matching the
  2635 registered value to the printed digit. The instrument is the registered
  instrument.

## 2. The ladder (a ∈ {0.04, 0.08, 0.16, 0.32}, m2, phases {0, π/2}, dt-union {τ_C/50, τ_C/25})

```
dt=1/50  ph=0.00: dT = -80.02 / -72.88 / -90.27 / +158.95   ratios +0.91, +1.24, -1.76
dt=1/50  ph=1.57: dT = -71.10 / -72.06 / -84.38 /  -34.21   ratios +1.01, +1.17, +0.41
dt=1/25  ph=0.00: dT = -93.19 / -81.99 / -87.48 / +143.88   ratios +0.88, +1.07, -1.64
dt=1/25  ph=1.57: dT = -114.87 / -92.25 / -85.44 / -27.05   ratios +0.80, +0.93, +0.32
```

**No cell in any phase at any dt reaches the [3, 5] window** — the quadratic
regime is not reachable on this ladder. The top adjacency moves decisively AWAY
from 4 in every leg (−1.76/−1.64 at phase 0; +0.41/+0.32 at phase π/2): the
prereg's nonmonotone clause fires there. **Frozen reading: D2-NO-ENTRY**, with
the D2-NONMONOTONE clause registered at the top adjacency, dt-stable
throughout.

**Sign clause (data, not failure, per prereg §2):** at phase 0 the a = 0.32
rung flips POSITIVE at BOTH dt (+158.95 / +143.88) — the perturbation-energy
curve dT(a) crosses zero between a = 0.16 and a = 0.32 at this phase. The
surface is not single-signed in amplitude.

## 3. Observation registered without claim (composite adjudication owns any sentence)

Across a factor of 4 in amplitude (0.04 → 0.16), dT is nearly
amplitude-INDEPENDENT (−71 to −93 MeV band, all legs). An amplitude-independent
offset fed to the curvature estimator c = 2ΔT/x² produces c ∝ 1/x² — at
x = 0.04, 2·(−80)/0.04² ≈ −10⁵, precisely the order of the registered
2513/2635 SIG-NEG magnitudes (m2 −51430/−73304 as ensemble means over
mixed-phase members). The Branch-N numbers are therefore CONSISTENT with an
amplitude-independent energy offset wearing a curvature estimator's units —
the "coherent-sign invalid-regime" reading (2648) gains its first quantitative
mechanism candidate. **No adjudication rides on this observation; D1's floor
characterization and D3's direct construction are the arcs that would test
it.** (If the offset story is right, D1 should see the floor behave as an
offset statistic and D3 should find no plateau at these amplitudes — noted as
a pre-D1/D3 expectation IN WRITING so a later match cannot be retro-fitted.)

## 4. Standing

D2 DISCHARGED at reading D2-NO-ENTRY (+ nonmonotone top adjacency + dt-stable
phase-0 sign flip, all disclosed). Per the 2649 order, **C7-D1 is next**
(TC ∈ {60, 120, 240}, a = 0.04, both dt, pin at TC = 60), then D3. Composite
adjudication only after all three. Fences held: no DM-consumer sentence rides
on this reading; DISC amendment scope untouched; 2513/2635 unedited; C7 text
untouched; FORM-1 charter untouched; **79.5% untouched.** Reasoning:
`reasoning/2650.md`.
