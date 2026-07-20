# N2B-DISC-1-2 execution record — VERDICT RD2 (PARTITION-SUSPECT, ADVERSE): THE BLOCK STANDS AND HARDENS; FUNNEL VERDICT RF1 AT w=4: THE ≈7D REACH IS SINK-MEDIATED

**Patch 2624, 20 July 2026.** Execution under `n2b_disc1_2_prereg.md` (2623) only,
which carries the 2620 spec verbatim plus the two 2622-designed corrections. Verify:
`code/2624_n2b_disc1_2.py`, all stages (controls | m1 | m23 | m4 | m5), foreground-
chunked. **Disclosed erratum (cosmetic):** the script's runtime banner carries the
stale line "PATCH 2621 … prereg 2620" from its verbatim-copy construction; the
docstring, filename, and this record identify the governing documents correctly;
the script is committed exactly as run.

## 1. Controls — ALL PASS (gating satisfied; the cell reads)

```
[C1] registered: CAP Sea=304.706982 gmax=2.097582 / n1_disc identical, deltas 0.0
[C2a] Sea(eta=0) = -1.421e-13  (machine-zero PASS)
[C2b] Edrift(eta=0) 48.715, 25.446, 11.002 ; ratios 1.91, 2.31  (both >= 1.5 PASS)
[C3] isolated square: max ktA=0.0079, max ktB=0.0000 MeV  (PASS)
```

## 2. M2/M3 — the discriminator gates (raw, then reading)

```
v=0.10: S1p(1/50 —, 1/100 251.32, 1/200 235.33, 1/400 212.60)
        increments |400-200|=22.73 > |200-100|=15.97  NOT shrinking; final-inc 0.107
        method agreement 0.000 (1/200), 0.001 (1/400)   [PASS <= 0.10]
v=0.95: S1p(1/50 408.72, 1/100 436.32, 1/200 285.03, 1/400 402.18)  non-monotone
        final-inc 0.291; method agreement 0.300 (1/200), 0.222 (1/400)  [FAIL]
M3: physical spread 106.24 (v-grid, 1/200; note non-monotone: 235.3, 178.8, 285.0)
    impl spread: v=0.10 anchor 38.84 (ratio 0.366)  v=0.95 anchor 236.66 (ratio 2.228)
    [both FAIL <= 0.20]
Baseline guard: every gated deposit [clear] (all S1p >> 3x own-cell Edrift).
```

**READING — RD2, PARTITION-SUSPECT (adverse), as frozen.** Scope named by the
failing gates: **(i)** S_1pass is NOT dt-convergent at EITHER anchor (final
increments 10.7% and 29.1% against the 5% gate); **(ii)** the independent
decompositions agree to four decimals at low γ and DISAGREE at 22–30% at transit-γ
— the high-γ single-pass deposit is decomposition-definition-dependent; **(iii)**
implementation spread rivals (0.37) or exceeds (2.23) physical spread. **The DISC-1
BLOCK STANDS AND HARDENS:** high-γ (v > 0.3c) consumers, Sea-deposit-growth
discussion, and H-a/H-b preference remain blocked, now with the additional
registered fact that the single-pass quantity as frozen (global-argmin t_ca window)
is implementation-sensitive. Model/instrument repair is a NEW candidate entering at
the top (declared below, not run). Recorded in the same font as a win.

**Disclosed-unread (banked for the successor cell):** S_cum — the end-of-window
cumulative deposit — is dt-stable to ~4% at BOTH anchors across all tested dt
(292.5–296.8 at v=0.10; 572.5–596.7 at v=0.95). The wandering lives in the
single-pass window's t_ca definition (chaos-exposed global argmin during the bound
phase), not visibly in the cumulative ledger. The successor cell's prime design
input.

## 3. M1 — component tracking (registers as DATA; no mechanism promotion)

All 12 cells CAP. f_1pass ∈ [0.46, 0.85] — the majority of the encounter deposit
lands within the single pass in every cell (burst-leaning profile; H-a/H-b remain
unpromoted and blocked per RD2). D^B tracks S_1pass to < 0.1% at v ≤ 0.4 across the
full grid; the divergence is confined to transit-γ. End-of-window |Δcen| (1.5–136
fm) is post-capture recoil carried by the registered momentum ledger, not aim drift
— the settled square is static pre-contact (2622 D3), so aim-relevant approach
drift ≈ 0 in every cell; disclosed as the operative reading of the drift clause.

## 4. M4 — split-ON/OFF trajectory table (registers raw)

```
v=0.10 b=0 w=4: ON CAP / OFF CAP@1/100 -> UNR@1/200   (OFF dt-UNSTABLE)
v=0.10 b=1 w=4: ON CAP / OFF CAP@1/100 -> UNR@1/200   (OFF dt-UNSTABLE)
v=0.95 b=0 w=4: ON CAP / OFF SCA  (both dt)
v=0.95 b=1 w=4: ON CAP / OFF SCA  (both dt)
v=0.10 b=0 w=2: ON CAP / OFF CAP  (both dt)
```

Registered raw facts: **at transit-γ the OFF instrument scatters dt-stably where
the ON instrument captures — capture at high γ is sink-dependent.** At v=0.10, w=4
the OFF classification is dt-unstable (drift-fed CAP at coarse dt dissolving at
fine dt); at w=2 the OFF capture is dt-stable. Mechanistic interpretation stays
blocked per RD2.

## 5. M5 — FUNNEL-1 (analytic + numeric; classification quantities, deposit-free)

```
Analytic (well ONLY, registered forms):  KE_inc(0.10c) = 0.6650 MeV
  b_W(w=2) = 4.5D      b_W(w=4) = 2.5D
Numeric (v=0.10c, dt-union on brackets):
  w=4 ON : CAP through 8D; b=8 CAP at 1/200      -> R_f(ON)  >= 8D (dt-stable, grid-exceeded)
  w=4 OFF: bracket last-CAP b=5 (1/200 CAP), first-non-CAP b=6 (1/200 SCA)  -> R_f(OFF) = 5D
  w=2 ON : CAP through 8D; b=8 CAP at 1/200      -> R_f(ON)  >= 8D (dt-stable, grid-exceeded)
  w=2 OFF: patchwork UNR/CAP; bracket b=8 flips SCA at 1/200 -> dt-UNSTABLE, no R_f established
```

**READING — RF1 at w=4: THE FUNNEL IS SINK-MEDIATED.** R_f(ON) − R_f(OFF) ≥ 3D
(≥ 2D gate met, both legs dt-stable) and the potentials-only analytic bound
b_W = 2.5D ≪ R_f(ON) ≥ 8D. The 2612 "~7D reach" observation is consistent with and
now classified by this record; the registered bound is a LOWER bound (reach ≥ 8D,
beyond grid — the upper-bound scan is a declared follow-on, not run). At w=2: the
ON reach ≥ 8D and b_W = 4.5D register; the OFF leg is dt-unstable at the bracket, so
**no class is forced at w=2** (disclosed; RF1-consistent but not read).
**FUNNEL-1's panel condition is DISCHARGED-AT-CLASS for w=4** (classified sink
artifact-class and bounded below); the upper bound and the w=2 OFF stabilization are
declared successor items.

## 6. Declared successors (queued, NOT run)

- **DISC-2 (the repair candidate, enters at the top per RD2):** re-entry with a
  dt-robust single-pass window (candidates: first-entry crossing of a declared
  radius; first local minimum; fixed-time window from launch) and/or gating on the
  dt-stable S_cum; designed from this record's disclosures, its own prereg.
- **FUNNEL upper bound:** offset grid b > 8D, ON, both widths.
- **w=2 OFF bracket stabilization** (finer dt on the w=2 OFF family).

## 7. Standing

DISC-1 executed to verdict: **RD2 adverse — the block stands and hardens** (this IS
the discriminator doing its job: the panel asked whether the high-γ deposit is
trustworthy and the answer tonight is NO-AS-INSTRUMENTED). FUNNEL-1
discharged-at-class (w=4). ETA-1's "instrument-defined at transit-γ" clause is now
QUANTIFIED (22–30% decomposition-dependence). FW-1, CORR-1, REPL-1, ROB-1, FORM-1,
DEP-1, AMB-1 untouched; EDGE-2(i) still queued; no rates, no σ_cap, no relic
contact; **79.5% untouched.** Founder-free queue after this patch: DISC-2 (top),
ROB-1, DEP-1, R-B 1–4.
