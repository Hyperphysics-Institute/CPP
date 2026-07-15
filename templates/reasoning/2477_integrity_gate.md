# Reasoning fragment — Patch 2477 — the publication integrity gate

**Session:** AUDIT-WARM-2476 continuation, 15 July 2026.
**Scope:** infrastructure (OPEN-WORKFLOW-PREDICTION-AUDIT, queue item 2 of the
2026-07-15 handover).
**Deliverable:** `scripts/integrity_audit.py` + BLOCKING hook in
`scripts/publication_audit.sh`.

## Why a new engine rather than extending the shell script

`publication_audit.sh` answers "did each mandated artifact get TOUCHED" — a
presence check, grep-shaped, honest at what it does. The handover's gate asks a
different question: "is what got touched REAL." That requires parsing Python
ASTs (stub detection), classifying imports against the stdlib, resolving
citations through LaTeX escaping and basename ambiguity, and applying
context-sensitive prose checks (a withdrawn claim QUOTED inside a correction
note must not re-fire the alarm). None of that is grep-shaped. The engine is
stdlib-only Python — the same standard the 2471 replacement scripts adopted —
invoked by the shell gate so a paper cannot PASS publication audit while citing
a stub.

## The FAIL/WARN split, and why it is where it is

FAIL is reserved for what a hostile reviewer would call fabrication-adjacent:
a cited script that does not exist (F1), does not parse (F2), is a stub in the
SR-1 pattern (F4), carries an elision marker in code (F5), live
dimensional-necessity billing (F6), or zero-parameter billing that the frontier
has already withdrawn (F7). Undeclared non-stdlib imports (F3) also FAIL per
the handover's explicit spec, but the report bands them separately as
reproducibility-class — numpy is endemic in pre-2471 scripts and mass-flagging
it as fabrication would bury the signal the gate exists to find.

WARN is reserved for what only a human can adjudicate: hard-coded
high-precision literals inside print statements (the fabricated-MC output
signature — but legitimately-printed reference values look identical to a
parser), target-variable circularity candidates, identity-language cohabiting
with prediction billing (the gamma-bridge pattern — SR-1's own §A.8.1 defect,
which no regex can distinguish from an honest equivalence proof), and
absorption language sharing a file with zero-parameter claims.

## Calibration record (the tool was verified, not read)

Run 1, SR-1 (known casualty): caught all three fabricated MC files, caught the
withdrawn dimensional-necessity claim still LIVE in three doc-suite files
(mechanism/development/glossary-SR-1.md — the ninth instance of the
eight-passes lesson), and false-positived on LaTeX-escaped paths, glob
fragments, and the .tex's own correction note. Each false positive got a
targeted fix: un-escape `\_`, skip `*`-prefixed tokens, 400-char withdrawal
context guard on F6.

Run 2, SS-2 (presumed healthy): exposed the per-paper scope bleeding into
sibling papers sharing a directory (SS-7/SS-9 findings attributed to SS-2) and
warn-noise on transcripts, which legitimately contain "in this response"
because they ARE AI transcripts. Fixes: foreign-paper path guard keyed on the
discovered ID set; W2/W3/W5 narrowed to .tex.

Run 3, programme-wide: exposed four more false-positive classes, each fixed —
(i) the stub detector missed re-assignment as a fill (SS-9's `irreps_dim = {}`
in a DEGEN branch, rebound in the else branch, is correct code); (ii) F7
matched withdrawal tokens anywhere on 6,000-char campaign mega-lines
(DM-1/2/3 false hits) — now a ±150-char proximity window; (iii) the window
then dropped SR-1's GENUINE hit because SR.md:27 uses bold lowercase
`**withdrawn**` and the matcher knew only ALL-CAPS — both forms now match;
(iv) ambiguous basenames (two copies of `parameters_600cell.py`) reported as
missing — now resolved by longest shared path prefix with the paper. A final
class: citations explicitly marked "(planned)" (SS-1a's mc_hadron_mass.py)
are forward references, not fabricated billing — downgraded to
W-PLANNED-SCRIPT, but only when EVERY citing site carries the marker.

Every one of these calibration defects was found by running the tool against
the corpus and checking each hit at the source — the handover's closing
instruction applied to the auditor itself.
