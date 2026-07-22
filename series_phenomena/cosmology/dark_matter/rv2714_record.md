# RV-2714 RECORD — executed under the frozen 2760 prereg: **gate v2 PASS on all five geometries (≤4×10⁻¹³) before any production sweep; all five chains completed at full frozen length from the reserved seeds; and the clean numbers rewrite the tension** — RV-1: the "20–26% below-HNC" fluctuation suppression is DEAD (κ_S/κ_D = 0.982–1.015 across all five chains, was 1.18–1.25 legacy; the k-space pole agrees with HNC at 0.49σ, was 6.6σ) — the defect manufactured the entire S_zz suppression; RV-4: MONOTONIC character CONFIRMED at Ewald grade on clean chains (zero 2σ alternations in all five; the FG-STAGGER-PROXY-ARTIFACT Ewald leg is RESTORED); RV-2: the frozen C1–C5 read FAIL but the failure INVERTED — clean κ_fit = 0.9032 × κ_D (legacy was 1.106×), C2 and C4 flip to PASS, and the sole substantive residual is the real-space near-window slope sitting ~10% BELOW DH while k-space and the far window agree; RV-3: the frozen 2735 rule fires CLOSURE-ERROR CANDIDATE / UNRESOLVED as committed (F1 = 2.56σ > 2), with the discrepancy collapsed from 5.8–6.6σ to F1 2.56σ / F2 0.53σ / F3 0.49σ — X3/X4 carry, now against a marginal not a monstrous tension

**Patch 2761, 22 July 2026. Seeds consumed: 20260798–20260802 (pool
now spent through …802). Verify: `code/2761_rv2714_execution.py`
(gate / chunked execution / verbatim-2714 analyzer) and
`code/2761_rv2714_x6_battery.py` (verbatim-2735 battery, generated
by mechanical path-substitution from the committed 2735 script; its
self-validation gate reproduced the committed 2721 solver ratios
1.0206/1.0042 exactly before any new number). Data archived at
`data/rv2714/` (five gzipped per-sample chains for seat re-analysis).
S-drift cross-check ≤ 2.3×10⁻¹² at every chunk boundary. Reasoning:
`reasoning/2761.md`. 79.5% not in scope.**

## §1 — Execution (exactly as chartered; no deviations)

Gate v2 (CONV-005, blocking, five seed-1 trial moves per geometry,
fixed-A increments vs independent brute-force totals, threshold
10⁻⁸): **PASS at all five geometries, worst relative discrepancy
3.7×10⁻¹³** — production licensed. All five chains then completed at
the frozen 2714 lengths:

| Run | N | a_s | seed | sweeps | acc | samples |
|---|---|---|---|---|---|---|
| RV-MAIN-A | 686 | 0.04 | 20260798 | 600+2400 | 0.93 | 480 |
| RV-MAIN-B | 686 | 0.04 | 20260799 | 600+2400 | 0.93 | 480 |
| RV-SIZE-S | 432 | 0.04 | 20260800 | 400+1600 | 0.93 | 320 |
| RV-SIZE-L | 1024 | 0.04 | 20260801 | 400+1600 | 0.93 | 320 |
| RV-CORE | 432 | 0.02 | 20260802 | 400+1600 | 0.91 | 320 |

(Legacy acceptance under the defect ran lower — the spurious 2–28 MeV
penalty rejected moves the Hamiltonian accepts; the clean chains'
0.91–0.93 is itself a visible signature of the fix.)

## §2 — RV-1: the fluctuation spectrum (REPLACEMENT; the suppression finding is VOID)

Clean κ_S/κ_D by chain: **0.986 / 0.990 / 0.982 / 1.015 / 0.987**
(legacy: 1.18–1.25). Matched-k pole (F3 functional): sim
1.0161 ± 0.0369 vs HNC-at-same-k 0.9967 — **0.49σ** (legacy 6.6σ).
The standing claim "the a_s = 0.04 Sea suppresses small-k charge
fluctuations 20–26% below HNC" (X3-LONG §, X6) is hereby REPLACED:
**the clean S_zz is consistent with DH/HNC at the few-percent level;
the entire suppression was the 2714 self-pair defect** (mechanism per
2756 §3: the g-penalty stiffened the chains and under-sampled the
fluctuations). "Septuple consistency" language is retired; the clean
cross-checks now on record are: five-chain κ_S concordance, F3 pole
agreement, and the F2 far-window agreement below.

## §3 — RV-2: the frozen 2713 criteria on clean chains

```
RV-MAIN-A: kappa_fit=5.034±0.145 (0.9163×)  alt=0  ΔAIC=−1.3  κ_S=0.986×
RV-MAIN-B: kappa_fit=4.890±0.133 (0.8901×)  alt=0  ΔAIC=−1.3  κ_S=0.990×
RV-SIZE-S: kappa_fit=4.971±0.190 (0.9048×)  alt=0  ΔAIC=+6.4  κ_S=0.982×
RV-SIZE-L: kappa_fit=5.098±0.162 (0.9278×)  alt=0  ΔAIC=−1.4  κ_S=1.015×
RV-CORE:   kappa_fit=4.734±0.179 (0.8616×)  alt=0  ΔAIC=+12.7 κ_S=0.987×
MAIN combined kappa_fit = 4.962 (0.9032 × κ_D); |A−B| = 0.144 ≤ 0.393
C1 FAIL   C2 PASS   C3 FAIL   C4 PASS   C5 PASS   →  RV S4-E FAIL
```

The composite verdict re-reads FAIL as frozen — but the failure
inverted and narrowed. Legacy-vs-clean, criterion by criterion:
**C2** (κ_S within 10% of κ_D): FAIL → **PASS** (the S_zz side is
resolved). **C4** (size drift ≤ 5%): FAIL → **PASS** (0.9048 → 0.9278
across 432→1024, spread 2.3%). **C5** PASS → PASS. **C3** (AIC): FAIL
→ FAIL on 2 of 5 runs — with zero significant alternations anywhere,
i.e. the documented 2714-era criterion defect reproduces on clean
data (the oscillatory model absorbs smooth curvature against
block-SEMs; the diagnosis travels with the readout as chartered, not
as an amendment). **C1** (2% gate + monotonicity): monotonicity HOLDS
(alt = 0 everywhere); the 2% gate fails with the tension INVERTED:
clean κ_fit sits **~10% BELOW κ_D** (legacy: 9–17% above). The
legacy "moderate-coupling enhancement" interpretation (2714 §2.2) is
VOID with the number it interpreted; the clean residual is a
real-space near-window slope BELOW DH, size ~5σ statistical, at an
extraction window where HNC itself reads 0.97 — i.e. O(Γ)-shape
territory, now to be interrogated by the standing instruments.

## §4 — RV-3: the frozen 2735 matched-functional battery (clean)

```
GATE: solver reproduces committed 2721 ratios exactly → PASS
F1 (near window, a_s=0.04): sim 0.9054±0.0197 vs HNC 0.9688 → 2.56σ
F1 (near window, a_s=0.02): sim 0.8864±0.0334 vs HNC 0.9898 → 2.82σ
F2 (far window  [0.40,0.88]): sim 0.9730±0.0837 vs HNC 1.0179 → 0.53σ
F3 (k-space pole, same k):    sim 1.0161±0.0369 vs HNC 0.9967 → 0.49σ
Frozen rule (F1 AND F3 ≤ 2σ): F1 FAIL, F3 PASS →
  CLOSURE-ERROR CANDIDATE / UNRESOLVED stands; X3+X4 carry
```

The frozen classification stands as committed — and the landscape
under it is transformed: the legacy battery read 5.8σ/6.6σ with the
instruments disagreeing about the profile's SHAPE; the clean battery
reads agreement in k-space and the far window, with a single marginal
2.5–2.8σ near-window tension, consistent in direction (below-DH) with
the C1 residual and present at both a_s values. What X3/X4 now carry
is a marginal, sign-definite, window-localized residual — not a
monster.

## §5 — RV-4: Ewald-grade character (RESTORED)

Zero 2σ sign alternations in all five clean chains. The Ewald-grade
MONOTONIC corroboration of FG-STAGGER-PROXY-ARTIFACT (exposure table
row 13's contaminated leg) is **RESTORED on clean data**: all three
legs — 2706 analytic, 2709 S4-N, and now RV-2714 Ewald — read
monotonic. The provisional classification's evidential basis is whole
again; its status (PROVISIONAL, panel property) is unchanged, as it
must be from inside.

## §6 — Disposition (per prereg §3; nothing re-decided)

1. Replacement complete: every RV row landed; the exposure table's
   CONTAMINATED-RERUN entries now point here for their numbers of
   record.
2. PR evaluation resumes on clean numbers only, at the consolidated
   S4-X report (panel property): PR1's ≤2σ bar remains unmet (F1
   2.56σ) but by a margin, not by 6σ; PR2's a_s-ladder (X4) and X3
   replication carry exactly as the frozen 2735 rule directs.
3. **The S4-X bundle dispatch is UNBLOCKED** (RV-1..RV-4 all landed):
   one packet = full S4-X arc + DRIVE-AUDIT-1 + corrections ledger +
   REACH-AUDIT-2714 outcome + this record.
4. Same-font disclosure: the RV-3 driver was produced by mechanical
   path-substitution from the committed 2735 script (transformation
   preserved in this record's commit); the substitution touched ONLY
   the sim input path — functionals, windows, solver, and gates are
   byte-identical.
