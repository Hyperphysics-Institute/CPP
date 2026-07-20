# FORM-1 Agenda B holdout execution record — VERDICT FB-MECH-B-SUPPORTED: the phase-robustness boundary is a CHAOS boundary of the target's coupled mode sector (Branch-U class); the steep-width schedule does NOT re-converge through dt = 1/800; the soft width and the endpoint both converge; onset localized ω ∈ (2.18, 2.61) c/fm

**Patch 2658, 20 July 2026. Execution under `form1_b_holdout_prereg.md` (2657);
predictions read verbatim from 2656 §4 (frozen before any instrument cell).
Verify: `code/2658_form1_b_holdout.py`, stages pin | h. One disclosed
pre-commit mechanics correction: the exec-load namespace `__file__` binding
(the 2635 precedent, verbatim class); no number had printed.**

## 1. Raw outputs (verbatim)

```
[PIN] nine cells vs the 2629 P1 printed row: ALL-MATCH True (to the digit)
[H2] w=4: S_WA(1/400)=182.72  S_WA(1/800)=220.13   final-inc = 0.1699
     (S_cum 292.5 -> 292.9, 0.14%; Edrift 8.4 -> 4.5; CAP/CAP)
[H3] w=2: S_WA(1/400)=151.72  S_WA(1/800)=152.03   final-inc = 0.0020
[H1] w=2.5 [QUARANTINED]: S_WA = 69.11, 72.27, 74.07   final-inc(200->400) = 0.0242
```

## 2. Readings (frozen classes applied verbatim)

- **P-H2 → FB-MECH-B-SUPPORTED.** final-inc = 17.0% ≥ 5%: the steep width
  does not leave the saturated class as dt falls — it moves AWAY from
  convergence (11.6% → 17.0%) while the endpoint S_cum tightens to 0.14%.
  The FB-MECH-A re-convergence prediction FAILED; the FB-MECH-B persistence
  prediction FIRED. The schedule's non-convergence is trajectory-level and
  survives a further halving: **Branch-U class** (2513/2514 chaotic-floor
  lineage), not sampled-phase error.
- **P-H3 → MET, both clauses.** 0.20% ≤ 2.5%, and at/below the registered
  0.41% class (falling ≈ ∝ dt): the soft width's multi-mode dynamics is
  regular at this excitation; its schedule is a covered observable.
- **P-H1 (diagnostic, quarantined):** 2.42% — convergent-to-marginal. The
  onset therefore sits between w = 2.5 and w = 3: **ω ∈ (2.18, 2.61) c/fm at
  the tested dt** — the boundary's first drawn localization, diagnostic-grade.

## 3. What attaches to the FD-BOUNDARY registration (observation-grade, the C7 attachment pattern; no claim promoted, no consumer moves)

The phase-robustness boundary the charter asked Agenda B to predict is, on
tonight's discriminator, a **chaos boundary**: below it (soft), the target's
coupled anharmonic modes are regular and the shed schedule is a genuine
observable; above it (steep), the modes are chaotic, dt-differences amplify
at trajectory level, and the schedule is non-convergent at EVERY affordable
dt — while the endpoint ledger, an integral of the motion's bookkeeping,
converges at drift order throughout (0.14% here; T1's structure restated
from a third independent direction, after 2626 and 2629). Two consequences
recorded for the composite patch, neither registered here: (i) the DISC
amendment's "schedule blocked pending FORM-1" clause has its FORM-1 answer —
the blocked quantities are not recoverable by refinement in the chaotic
regime, so the endpoint-only scope is the law's own scope there, not a
temporary caution; (ii) the future Agenda-B derivation target is
reclassified: not a phase-error estimate but a statistical/transport account
of a chaotic mode sector (the Branch-U and C7-D1 offset-floor results are
its adjacent data).

## 4. Standing

PIN exact (nine for nine); zero new instrument defects (the J4 apparatus'
second clean arc); w ∈ {2.5, 3} quarantined; no DM consumer sentence rides on
any number above; DISC amendment scope untouched at this patch; 2513/2635/
2626/2629/C7 unedited; **79.5% untouched.** Composite adjudication for
Agenda B waits for the session-close patch per charter §5. Reasoning:
`reasoning/2658.md`.
