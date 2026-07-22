# S4-X B-CHECK-80 PREREGISTRATION (DRIVE-AUDIT-1, fourth act) — FROZEN BEFORE ANY RUN

**Patch 2753, 22 July 2026. Registered under the standing DRIVE-AUDIT-1
escalation (X5-FE F3 → X7-NSCAN G4 → X7-NSCAN-EXT H4) and the 2751
record's §3 queue: one run of the independent brute-force B sampler at
N = 80 — the smallest size inside the onset window (64, 80] — as the
sharp discriminant between candidate (a) (incremental-path numerical
pathology) and candidate (b) (finite-size-onset ergodicity failure).
79.5% not in scope. AUTOMATON-1 remains arbiter-of-record per the
frozen H4 clause regardless of this act's outcome.**

## §1 — Purpose

At N = 80 the campaign's A-path driven mean (−1.922 ± 0.157) exceeds
the exact Gibbs tilt response (−1.185 ± 0.144) by 3.46σ (r = 1.622 ±
0.237, ENHANCED). The B sampler shares no state machinery with path A:
per move, the TOTAL energy of the proposed configuration is rebuilt
from nothing (full pair sum with the identical masked erfc + softcore
formula; full k-space structure factor rebuilt from all particles),
with only the current total energy carried. If B reproduces the
enhancement at the onset itself, no incremental-machinery defect can
explain the anomaly; if B sits at tilt level, the incremental path is
impeached specifically inside the onset window.

## §2 — Design (frozen)

- **System:** N = 80 (40/40), a_s = 0.04, same density (L = (N/N_CP)^{1/3}),
  one driven mode k_d = (2π/L)(1,0,0), ε = 2.4 MeV — the exact box and
  protocol of the X7-NSCAN-EXT N = 80 point.
- **Sampler:** the 2746 B design, parameterized at N = 80. Per move:
  E_new = E_real(full pair sum, min-image, masked erfc + softcore)
  + E_k(structure factor rebuilt from scratch) + ε·Σ Z cos(k_d·x);
  Metropolis on E_new − E_cur; E_cur carried, recomputed from scratch
  at every checkpoint resume.
- **k-space convention (frozen):** E_k = PREF · Σ_half W_K |S(k)|²
  with PREF = 2(2π/L³)Q² — the FULL prefactor matching path A's
  incremental convention dE_k = PREF · Δ(Σ W_K |S|²). See §5
  disclosure on the committed 2746 file.
- **Run:** frozen seed **20260795** (returned unconsumed to the pool at
  2751 close; consumed here as assigned). 1k equilibration + 12k
  sampling sweeps, sample A = Σ Z cos(k_d·x) every 10 sweeps → 1200
  samples; 10-block SEM. Checkpointed; chunked execution permitted;
  chain state (rng, x, done, ser) carried exactly across chunks.
- **Comparators (frozen, from the archived EXT series, estimator
  identical to 2749 `analyze`):** tilt_A(80) = −1.185 ± 0.144
  (recomputed at analysis time from `data/x7nscan/x7nscan_N80-UND.json.gz`
  for exactness); A-DRV(80) = −1.922 ± 0.157 (from
  `data/x7nscan/x7nscan_N80-DRV.json.gz`).

## §3 — Hamiltonian-identity gate (pre-run, blocking)

Before any production sweep: with rng seed 1, draw one random N = 80
configuration and five random trial moves. For each move compute
(i) ΔE_B = E_B(new) − E_B(old) by two from-scratch total-energy
evaluations, and (ii) dE_A by path A's incremental machinery (masked
real-space sums, structure-factor update dS, dE_k, drive delta) on the
same move. **Gate: |ΔE_B − dE_A| ≤ 10⁻⁸ · max(1, |dE_A|) on all five
moves.** PASS is a precondition to production; FAIL blocks the run and
the session reports the defect instead. The gate reads no observable
and consumes no pool seed. This formalizes the 2747 lesson
("inspection before results is cheap; its absence is not") into a
mechanical precondition: B's Hamiltonian is certified identical to
A's while sharing none of A's state machinery.

## §4 — Frozen fork (2σ combined bands)

Let m_B ± e_B be B's 10-block driven mean; σ_AB = √(e_B² + 0.157²);
σ_Bt = √(e_B² + te²) with te the jackknife tilt error.

- **I1 — REPRODUCED:** |m_B − (−1.922)| ≤ 2σ_AB AND
  |m_B − tilt| > 2σ_Bt → candidate (a) **dies at the onset**; the
  finding becomes (b): finite-size-onset ergodicity failure of
  local-move Metropolis under a symmetry-breaking field — reportable
  sampler physics. AUTOMATON-1 adjudicates the mechanism as
  arbiter-of-record.
- **I2 — TILT-LEVEL:** |m_B − tilt| ≤ 2σ_Bt AND
  |m_B − (−1.922)| > 2σ_AB → the incremental path is impeached
  specifically at the onset window; next act = mechanical diff of the
  A-path increments at N = 80 vs 64, fix, and a re-verification
  campaign over all driven artifacts.
- **I3 — OTHER** (both windows, neither, or any other pattern) →
  PARTIAL; extend (B to 24k sweeps under a fresh frozen prereg, or
  hand directly to AUTOMATON-1 per the standing elevation). No shape
  or mechanism reading enacted under I3.

**Power:** Var(A) ≈ 18.6 at N = 80, IAT 1.4–1.8 samples at 10-sweep
spacing → expected e_B ≈ 0.15–0.17; σ_AB ≈ 0.22, σ_Bt ≈ 0.21;
hypothesis separation 0.737 ≈ 3.4σ — the exclusive windows are
disjoint except for a narrow central strip that routes to I3.

## §5 — Disclosures (frozen with the prereg)

1. **Committed-2746 code/record discrepancy.** The 2747 record
   disclosed a spurious 0.5 in B's k-space prefactor, caught by
   inspection and fixed before any comparative result was read. The
   committed `code/2746_s4x_x5fe.py`, however, still evaluates a net
   0.5·PREF·Σ (the line `...*2.0/2.0` is arithmetically the identity),
   with an adjacent comment claiming "prefactor already full" — the
   committed file does not reflect the documented runtime fix. Archived
   B-DRV variance (18.86 vs A-DRV 16.13 at N = 64) is inconclusive on
   which convention actually ran. This is recorded as a capture defect
   for the corrections ledger; it does not reopen F3 here (the fork's
   physics conclusion was triple-anchored by A-DRV/tilt agreement),
   but the identity gate in §3 makes THIS act self-certifying
   regardless of the 2746 file's state.
2. **Cost benchmark:** timing-only, seed 1, ≤ 5 sweeps, no observable
   read, discarded, disclosed in the record. Prior measurement:
   ≈ 0.25 s/sweep ≈ 0.9 h for 1k + 12k.
3. Checkpoint-resume recomputes E_cur from scratch (drift-proof by
   construction); chunk boundaries are disclosed in the record if any
   operational anomaly occurs.

## §6 — What this act cannot touch

The septuply-consistent fluctuation spectrum, the X6 shape finding,
un-quarantined pole, monotonic character, K1-FORM-ONLY + R1–R8, both
ℓ caps, GP-limit statement, FA-C3 CLOSED, Candidate (B) 79.5%, LANE B
HELD, RELIC-1, qCP fence, DeepSeek advisory — all out of scope. The
anomaly under audit remains confined to the driven-MEAN instrument at
N ≥ onset; no standing claim consumes it.
