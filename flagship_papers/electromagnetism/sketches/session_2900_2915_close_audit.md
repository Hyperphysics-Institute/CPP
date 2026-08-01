# SESSION-CLOSE AUDIT — PATCHES 2900–2915 (+ ROUND-2 WINDOW PINNING)

**Patch 2916. The handover-protocol audit battery, run at founder
request after Patch 2915 was applied.**

## §1 — AUDIT RESULTS

| audit | result |
|---|---|
| A1 tree state | CLEAN — no uncommitted changes; patches 2900–2915 in unbroken sequence atop 2899 |
| A2 reasoning capture | **16/16** fragments present (2900–2915) |
| A3 per-patch bundling | **16/16** — every reasoning fragment lives in its own patch's commit (the 2899-flagged lapse class: zero occurrences this session) |
| A4 founders_voice | Both 31-Jul rulings captured verbatim, same-patch, per CONV-009 |
| A5 data archives | 13 data files present; every banded or recorded number traceable |
| A6 file-placement scope | 58 files, all within the six expected trees (EM code/data/reasoning/sketches, founders_voice, handovers); conventions honored |
| A7 ledger integrity | frontier / frontier_sectors / dark_matter: **zero files touched** — "ledger untouched" claims verified |
| A8 number fidelity | Spot-checks: 2910 M, 2912 M/SE, 2914 c_hyb/σ_c — archived JSON matches record text exactly |
| A9 code validity | 10/10 session code files parse |
| A10 round-2 executability | **DEFECT FOUND — see §2** |

## §2 — FINDING: ROUND-2 WINDOW SPEC AMBIGUOUS AND LATENTLY INFEASIBLE

The 2914 §4 text — "matched windows (125/100/75/63/63… computed as
round multiples of 2.5/β capped to [60,125])" — fails audit twice:
(i) the example list does not consistently equal round multiples of the
grid period (e.g. 100 is not a multiple of 35.71 for β = 0.07), and
(ii) the cap alone permits T_meas = 125 at β = 0.20, whose transit
(0.20 × 165 = 33 units) EXITS the 30-unit Sea — the exact 2905 failure
class, caught again by arithmetic before execution.

**PINNED, pre-execution, disclosed:** round-2 windows are exactly

> **β = 0.04 → 125; β = 0.07 → 107; β = 0.10 → 100; β = 0.14 → 89;
> β = 0.20 → 63** (each the round multiple of 2.5/β nearest the top of
> its feasible range), T_eq = 40.

Verified transits: 6.6 / 10.3 / 14.0 / 18.1 / 20.6 units — all inside
the Sea, edge buffers 11.7 / 9.9 / 8.0 / 6.0 / 4.7 (the smallest equals
the round-1 β = 0.2 precedent). Nothing else in the round-2 spec, gates,
or bands changes; this pin resolves an ambiguity, created before any
round-2 leg exists.

## §3 — RESIDUAL NOTES

/tmp working state (results JSON, checkpoints) is ephemeral by design;
all verdict-relevant material is repo-archived (A5). The next worker
should treat `data/` as authoritative and /tmp as absent.
