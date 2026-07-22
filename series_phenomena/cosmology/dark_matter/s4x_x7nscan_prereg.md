# S4-X X7-NSCAN PREREGISTRATION (DRIVE-AUDIT-1, second act) — FROZEN BEFORE ANY RUN

**Patch 2749, 21 July 2026. Charter authority: X5-FE record §3 ("N-SCAN")
and the 2746–2748 handover's SINGLE NEXT ACT. Executed under Rider v2.5;
promotion barred; 79.5% not in scope.**

## Purpose

X5-FE (F3) exonerated the campaign's driven code path at N = 64 and
established that the B2 anomaly is SCALE-DEPENDENT: driven/tilt
enhancement ratio r(64) = 1.13 ± 0.12 versus r(432) = 1.70. X7-NSCAN
runs the SAME campaign path A at three intermediate sizes to locate the
onset and read its SHAPE, discriminating candidate (a) (N-dependent
numerical pathology, smooth drift expected) from candidate (b)
(finite-size-onset ergodicity failure under the symmetry-breaking
drive, sharp threshold expected). Candidates stay unranked until the
curve is read.

## Design (frozen)

- Sizes: N ∈ {128, 216, 320}, each 50/50 charge split.
- Protocol identical to X5-FE path A at each N: same density
  (L = (N/N_CP)^{1/3}), a_s = 0.04, ε = 2.4 MeV, one driven mode
  k1x = (2π/L)(1,0,0), identical k-set (n²max = 27), α = 5.6/L,
  r_c = L/2, step 0.20·A, Metropolis single-particle moves.
- Per size, an A-path PAIR: DRV (driven) and UND (undriven → exact
  Gibbs tilt prediction via reweighting, jackknife error, 10 blocks),
  1k equilibration + 16k sampling sweeps, sample every 10
  (1600 samples/ensemble).
- Code: `code/2749_s4x_x7nscan.py` — the run_A machinery of
  `2746_s4x_x5fe.py` verbatim (this is the code path under audit;
  no reimplementation), parameterized by N only.
- Seeds (frozen, continuing the campaign sequence):
  N128-DRV 20260783, N128-UND 20260784, N216-DRV 20260785,
  N216-UND 20260786, N320-DRV 20260787, N320-UND 20260788.
- Readout per size: r(N) = ⟨A⟩_DRV / tilt_A(N), error by quadrature
  of the DRV block-SEM and the tilt jackknife error propagated
  through the ratio.
- Anchors (not re-run): r(64) = 1.13 ± 0.12 (X5-FE), r(432) = 1.70
  (X3-LONG, three chains).

## Frozen classification

Define per size: ENHANCED if (r − 1) exceeds 2σ_r AND r ≥ 1.40;
UNENHANCED if r is within 2σ_r of the N = 64 baseline band AND
r < 1.30; else INTERMEDIATE.

- **G1 — SHARP THRESHOLD:** at least one scanned size UNENHANCED and a
  larger scanned size ENHANCED, with no ENHANCED size below an
  UNENHANCED one → onset bracketed inside the scan; (b)-like shape
  reading recorded (not enacted); **B-CHECK charters at the smallest
  ENHANCED N.**
- **G2 — SMOOTH DRIFT:** r monotonically increasing across
  64 → 128 → 216 → 320 with every size INTERMEDIATE or ENHANCED but
  no UNENHANCED→ENHANCED bracket → (a)-like shape reading recorded
  (not enacted); AUTOMATON-1 remains arbiter-of-record; B-CHECK at
  the smallest size with r ≥ 1.40, if any, else at 432.
- **G3 — FLAT THROUGH 320:** all three UNENHANCED → onset in
  (320, 432]; B-CHECK at 432 becomes the instrument (cost
  permitting); AUTOMATON-1 elevated further.
- **G4 — OTHER:** non-monotonic or unclassifiable → PARTIAL; extend
  with intermediate sizes before any reading.

## Power (pre-run estimate)

At 1600 samples with the observed autocorrelation at N = 64,
σ_r ≈ 0.10–0.18 per point (growing with N as Var(A) grows). The gap
between the anchors (1.13 vs 1.70) is ≈ 3–5σ_r, so an onset inside
the scan is resolvable; a hypothetical shallow drift of ≤ +0.1/step
may land INTERMEDIATE — recorded honestly if so (feeds G2/G4, not
forced into G1).

## Disclosure (pre-run)

A 20-sweep timing benchmark (seed 1, discarded, no observable read)
was run before this freeze solely to size the compute chunking:
~18/33/55 ms per sweep at 128/216/320, ≈ 61 min total. No production
seed was touched.

## Escalation

Whatever fires, the record patches with the curve, the shape reading,
and the archived series (`data/x7nscan/`); the eventual panel dispatch
bundles the full S4-X + DRIVE-AUDIT-1 campaign per the economy rule.
