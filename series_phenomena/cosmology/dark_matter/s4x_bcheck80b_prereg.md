# S4-X B-CHECK-80B PREREGISTRATION (DRIVE-AUDIT-1, fourth act, part 2) — AMENDED CHARTER, FROZEN BEFORE ANY PRODUCTION RUN

**Patch 2755, 22 July 2026. Supersedes the 2753 charter's blocked
production (gate FAIL, record 2754). One act now answers the sharper
question the gate created: is the 2714 self-pair defect the MECHANISM
of the B2 enhancement at the onset, or does the enhancement survive
the fix? 79.5% not in scope. AUTOMATON-1 remains arbiter-of-record
per the standing elevation.**

## §1 — Design (frozen)

Same system as 2753 §2 (N = 80, 40/40, a_s = 0.04, L = (N/N_CP)^{1/3},
k_d = (2π/L)(1,0,0), ε = 2.4 MeV). Three production ensembles:

1. **A-FIX-UND** — run_A verbatim PLUS the one-line fix `mn[i] = False`
   (excluding the moved particle's old position from its new-position
   pair sum; nothing else changed). Undriven. Frozen seed **20260796**
   (next in pool sequence). 1k eq + 16k sampling, sample every 10
   → 1600 samples. Yields the UNCONTAMINATED tilt:
   tilt_fix = ⟨A e^{−βεA}⟩/⟨e^{−βεA}⟩, jackknife error, estimator
   identical to 2749 `analyze`.
2. **A-FIX-DRV** — same fixed path, driven. Frozen seed **20260797**.
   1k + 16k, sample every 10.
3. **B-DRV** — the independent brute-force sampler (2746 design, full
   k-space prefactor per 2754 §4.4). Frozen seed **20260795**
   (unconsumed, consumed here). 1k + 12k, sample every 10 → 1200
   samples.

**Gate v2 (pre-run, blocking):** five seed-1 trial moves; B's
from-scratch total-energy differences vs A-FIX's incremental dE;
|ΔE_B − dE_AFIX| ≤ 10⁻⁸·max(1, |dE_AFIX|) on all five. Expected
~10⁻¹⁴ (the 2754 identity minus the defect). PASS is a precondition
to all three runs; gate reads no observable, consumes no pool seed.

**Legacy comparators (context only, NOT fork inputs):** the defective-
path N = 80 values tilt_legacy = −1.185 ± 0.144, A-DRV_legacy =
−1.922 ± 0.157, r_legacy = 1.622 ± 0.237. The fork below runs
entirely on clean quantities; legacy deltas are reported
descriptively to quantify the defect's bite.

## §2 — Frozen fork J (2σ combined bands)

Let m_F ± e_F = A-FIX-DRV 10-block mean; tilt_fix ± t_F from
A-FIX-UND; m_B ± e_B = B-DRV 10-block mean.
r_fix = m_F/tilt_fix ± σ_r (propagated); σ_FB = √(e_F² + e_B²).

- **J1 — DEFECT IS THE MECHANISM:** |r_fix − 1| ≤ 2σ_r AND
  |m_B − m_F| ≤ 2σ_FB → the clean samplers agree with each other and
  with the exact Gibbs tilt; the enhancement at the onset was an
  artifact of the 2714 self-pair defect; candidate **(a) CONFIRMED
  with named mechanism**. Remedy: repo-wide reach audit charter
  (every ensemble descending from 2714; exposure of X3-LONG, X5-LIN,
  X5-EXT-FIELD, X5-FE anchors, X7 twelve series; assessment of any
  standing-ledger observable consuming them), then the re-verification
  campaign, then the bundled panel dispatch per the economy rule.
- **J2 — ENHANCEMENT SURVIVES THE FIX:** (r_fix − 1) > 2σ_r AND
  |m_B − m_F| ≤ 2σ_FB → two clean, mutually-agreeing implementations
  both exceed the exact tilt: a correct-code equilibration failure —
  candidate **(b)-like**; no mechanism reading enacted; AUTOMATON-1
  adjudicates as arbiter-of-record.
- **J3 — CLEAN SAMPLERS DISAGREE:** |m_B − m_F| > 2σ_FB → a residual
  implementation defect exists; localize by mechanical diff; no
  physics reading.
- **J4 — OTHER** (any other pattern, incl. r_fix intermediate) →
  PARTIAL; extend under a fresh prereg or hand to AUTOMATON-1.

**Power:** Var(A) ≈ 19 at N = 80 → e_F ≈ 0.14, e_B ≈ 0.16, t_F ≈
0.14; σ_r ≈ 0.17–0.20. The legacy enhancement (0.737 in mean units,
3.46σ) is comfortably detectable if it survives; unity is
comfortably confirmable if it does not.

## §3 — Disclosures (frozen)

1. Benchmarks: B at 0.215 s/sweep (this container; seed 1, 3 sweeps,
   discarded) → ≈ 0.78 h; A-FIX to be benchmarked identically
   (timing only, seed 1, discarded, disclosed in the record) before
   the production chunk plan is set.
2. Chunked execution with checkpoints; E_cur (B) recomputed from
   scratch at every resume; A-FIX chain state carried exactly
   (rng, pos, S, done, ser) as in 2749.
3. Seeds 20260796/97 are new pool assignments (sequence continuation);
   20260795 consumed as assigned; any unconsumed contingency seed
   returns to the pool at record time.
4. No standing claim is reclassified by this act regardless of fork
   outcome; all reclassification proposals route to the corrections
   ledger and the bundled panel dispatch.

## §4 — Out of scope

Everything in 2753 §6, unchanged.
