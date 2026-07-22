# RV-2714 RE-VERIFICATION PREREG (FROZEN) — deliverable 2 of the REACH-AUDIT-2714 charter, executing the RA-2 consequence: the five S4-E chains re-run with the FIXED code under gate v2 (CONV-005, blocking), fresh frozen seeds 20260798–20260802, and every CONTAMINATED-RERUN quantity (RV-1 spectrum, RV-2 PR1 κ-tension, RV-3 X6 dual extraction, RV-4 Ewald-grade character) re-read under its ORIGINAL frozen criteria — no new thresholds, no new functionals, no fork: whatever the clean chains read REPLACES the contaminated predecessor same-font, and the S4-X bundle dispatch unblocks when the last RV row lands

**Patch 2760, 22 July 2026. Frozen BEFORE any run; no RV chain has
been started at this patch. Blocking precondition per CONV-005: gate
v2 (five seed-1 trial moves, B totals vs fixed-A increments, 10⁻⁸)
PASSES before each production run or that run reports the defect
instead. Rider v2.5 governs; 79.5% not in scope. Reasoning:
`reasoning/2760.md`.**

## §1 — Runs (mirror the 2714 charter exactly; only the code and seeds change)

Sampler: the FIXED A path (`mn[i]=False`, the 2755 lineage), verified
against the independent B implementation by gate v2 at each N.
Protocol constants identical to the frozen campaign stack (A = 0.589/φ,
Θ ≈ 35.149 MeV, ε_soft, full-PREF k-space, step, sampling cadence —
all verbatim from `code/2714_alpha1_s4e_ewald.py` RUNS/constants).

| Run | N | a_s | seed (fresh) | eq + prod sweeps (as 2714) |
|---|---|---|---|---|
| RV-MAIN-A | 686 | 0.04 | 20260798 | 600 + 2400 |
| RV-MAIN-B | 686 | 0.04 | 20260799 | 600 + 2400 |
| RV-SIZE-S | 432 | 0.04 | 20260800 | 400 + 1600 |
| RV-SIZE-L | 1024 | 0.04 | 20260801 | 400 + 1600 |
| RV-CORE | 432 | 0.02 | 20260802 | 400 + 1600 |

Seed pool: …798–802 are hereby RESERVED; consumed only when the
corresponding production run starts (post-gate). Execution:
checkpointed foreground chunks per the standing container-execution
lesson (2756 disclosure; REACH-AUDIT-2 §1(a)). Cost estimate,
disclosed: the 2714 act completed these five chains chunked across
one session; the fixed increment adds no per-move cost. Data archive:
`data/rv2714/` (gzipped per-sample profiles, per the X1 archival
precedent, for seat re-analysis).

## §2 — Readouts (original frozen criteria re-applied; nothing new)

- **RV-1 — the undriven fluctuation spectrum** at the §1 state
  points, by the arc's standing estimator with the X3-LONG fresh-full-
  summation cross-check embedded. Its clean values REPLACE the
  septuple; "consistency" language is retired until clean cross-
  checks exist.
- **RV-2 — the PR1 κ-tension:** the frozen 2713 criteria (C1–C5)
  re-evaluated verbatim on the clean chains, including the C3 AIC
  criterion with its documented defect diagnosis carried alongside
  (the criterion re-applies AS FROZEN; its 2714-era diagnosis travels
  with the readout, not as an amendment).
- **RV-3 — the X6 matched-functional dual extraction:** the frozen
  2735 functionals (F1 near-window, F2 far-window, F3 k-space pole)
  re-run against the clean chains and the unchanged 2721 HNC solver,
  with the same self-validation gate (solver copy reproduces the
  committed 2721 ratios to 4 decimals before any new number).
- **RV-4 — Ewald-grade character:** the 2713 alternation counter
  (2σ sign-alternation census) on the clean chains; its reading
  restores or revises the Ewald-grade leg of FG-STAGGER-PROXY-
  ARTIFACT (table row 13) — the analytic and S4-N legs stand
  regardless.

## §3 — Disposition rules (frozen)

1. No fork and no verdict classes: each RV row is a REPLACEMENT
   measurement. Whatever it reads is the number of record, same-font,
   favorable or not — including the possibility that the 20–26%
   below-HNC suppression was entirely the defect (spectrum agrees
   with HNC) or partially real (a smaller clean suppression). Neither
   outcome is privileged anywhere in this prereg.
2. PR1/PR2/PR5 evaluation resumes ONLY on clean numbers; every
   S4-X-stage inference previously drawn from rows the table marked
   CONTAMINATED is re-derived from the RV values or dropped.
3. The S4-X bundle dispatch (one packet: full arc + DRIVE-AUDIT-1 +
   corrections ledger + audit outcome + RV results) assembles when
   RV-1..RV-4 have all landed. The FA-SG-R1 paste is independent and
   already unblocked (table §3(h)).
4. Any gate v2 FAIL, any mid-run anomaly, or any deviation from §1
   parameters blocks production and reports same-font, per CONV-005
   and the standing prereg discipline.
