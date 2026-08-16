# CONV-021 RETURNS ADJUDICATED — Q3 UNANIMOUS APPARENT-ONLY and Q6 UNANIMOUS (run n = 9, 10 + scale-invariant diagnostics): the challenge REMAINS OPEN and the panel has specified exactly how to close it; Q1 the estimator: NEITHER-SPECIFY 3–1–1 raw, but the three do NOT name one estimator ⇒ NO SINGLE ESTIMATOR IS FIXED; the mandated SUITE is implemented instead (Binder crossings + data collapse + the unchanged peak locator), with the decision rule FROZEN BEFORE the run; **Q4: the economy-rule repair-without-a-round is RATIFIED PROCEDURALLY-SOUND (3–2 raw, 3–1 deduplicated)**; INDEPENDENCE FLAG: Copilot's and DeepSeek's returns are VERBATIM IDENTICAL — recorded, tallied both ways, outcome unchanged in every question

**Patch 3147 (15 Aug 2026). Adjudicates the five returns under the
3146 binding rules.**

## §1 — Tallies (raw, and deduplicated for the identical pair)

| Q | raw (5 seats) | dedup (4) | BINDING OUTCOME |
|---|---|---|---|
| Q1 estimator | NEITHER-SPECIFY ×3 (Gemini: Binder crossings; Copilot & DeepSeek: trimmed-convergence median + Binder + collapse), INSUFFICIENT-DATA ×1 (GPT), DIRECT-CONVERGENCE ×1 (Grok) | NS ×2, ID ×1, DC ×1 | **NO SINGLE ESTIMATOR FIXED** — the NEITHER-SPECIFY seats name DIFFERENT estimators, so the 3146 rule's "majority answer fixes the estimator" does not trigger on a shared answer; the worker selects none (§2) |
| Q2 challenge | REMAINS-OPEN ×2, STANDS-QUANTIFIED ×2 (2.614 ± 0.03), RESOLVES-CONFIRMING ×1 | ROPEN ×2, SQ ×1, RC ×1 | **REMAINS OPEN** (no majority either way; frozen 2.450 unrevised) |
| Q3 convergence | **APPARENT-ONLY ×5** | ×4 | **UNANIMOUS: the tail is APPARENT-ONLY — n = 9 and n = 10 required** |
| Q4 repair w/o round | PROCEDURALLY-SOUND ×3, SHOULD-HAVE-DISPATCHED ×2 | PS ×3, SHD ×1 | **RATIFIED PROCEDURALLY-SOUND** (dissent recorded verbatim: an independent methodological check on estimator family would have been added) |
| Q5 d_s = 2.0 | UNKNOWN-INVESTIGATE ×3, CONFOUNDING ×2 | UI ×3, C ×1 | **UNKNOWN-INVESTIGATE** — but ALL FIVE name the SAME diagnostic (map the full f_b(d_s) curves; test whether the dip biases the peak), so it is mandated regardless |
| Q6 next action | **UNANIMOUS in substance: run n = 9 and n = 10 under the unchanged locator; add Binder cumulants and/or global data collapse; record fine-grid full curves; freeze the criterion first** | same | **ADOPTED IN FULL** |

**INDEPENDENCE FLAG:** Copilot's and DeepSeek's returns are
verbatim identical (every answer, both paragraphs, the concrete-error
text). Recorded per the CONV-019 precedent; tallies given both ways
above; NO outcome changes under deduplication. Recommended (founder
action, optional): re-ask one of the two for an independent return.

## §2 — Why no estimator is selected, and what is done instead

The 3146 rule fixes an estimator only on a majority naming the SAME
one. Gemini names Binder crossings; Copilot/DeepSeek name a
trimmed-convergence median SUPPLEMENTED by Binder crossings and data
collapse; GPT declines pending data; Grok takes direct convergence.
The common content across every seat that named methods is: **(a)
larger sizes, (b) scale-invariant diagnostics.** That union — not a
worker preference — is what the mandated pass implements, with all
three candidate estimators computed and reported side by side and the
decision rule frozen in §3 BEFORE the run (GPT's explicit
requirement, adopted).

## §3 — THE MANDATED PASS, FROZEN NOW (prereg for n = 9, 10)

**Instrument:** unchanged dynamics. Instrumentation ADDED additively
(Patch 3147): the per-Moment bound-fraction series over the same
final-third window yields m₂, m₄ and the Binder cumulant
U = 1 − m₄/(3m₂²). **REGRESSION VERIFIED: every pre-existing output
key is bit-identical after the addition** (no RNG draw, no dynamics,
no aggregation changed).
**Cells:** n = 9 (729 pairs) and n = 10 (1000 pairs), grid
{1.5 … 5.0} × seeds {5, 11}; PLUS the Q5-mandated fine grid
{1.75, 1.90, 2.10, 2.25} at n = 8 and n = 9 for the anomaly map.
Workers auto-sized (16 at n = 9; 8 at n = 10 for memory headroom) —
not a scientific parameter.
**The three estimators, all computed, none privileged:**
E1 peak-locator convergence value (unchanged locator; the sequence's
last value once the convergence test passes); E2 Binder-crossing
d_c (crossings of U_n between adjacent sizes n ≥ 6, the crossing
sequence reported; d_c = mean of the last two crossings); E3 global
data collapse (grid search over (d_c, ν) minimizing the collapse
residual of f_b vs (d_s − d_c)·n^{1/ν} for n ≥ 6).
**FROZEN CONVERGENCE TEST (Q3's requirement):** the tail is
ESTABLISHED-CONVERGED iff |peak(9) − peak(8)| ≤ 0.02 AND
|peak(10) − peak(9)| ≤ 0.02 AND the three last steps show no
coherent renewed drift (their signed sum ≤ 0.03 in magnitude).
**FROZEN VERDICT RULE:** if max|E_i − E_j| ≤ 0.10 across the three
estimators, D_res = their mean, and then |D_res − 2.450| ≤ 0.182 ⇒
**CHALLENGE RESOLVES-CONFIRMING**; else ⇒ **CHALLENGE
STANDS-QUANTIFIED at D_res**. If the estimators disagree by more
than 0.10, or the convergence test fails ⇒ **REMAINS-OPEN**, back to
the panel with all three numbers. The frozen d_s* = 2.450 stands
unrevised in every branch; the calibration is untouched by
construction (OBL-CAL-LABEL).

## §4 — Disposition

Runner: `scripts/3147_n910_runner.py` (run / analyze; per-cell
checkpointing; ≈ 3 h for n = 9, ≈ 6–8 h for n = 10, overnight-safe
and resumable). Founder labor: one command, one paste-back. Q4's
ratification is recorded as PRECEDENT: instrument repairs frozen
before their testing data may proceed without a round; the two-seat
dissent is preserved verbatim in the record. Kila6 Route C untouched
and still trumping all.
