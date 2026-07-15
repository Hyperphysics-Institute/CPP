# Reasoning fragment — Patch 2478 — the programme-wide mechanical pass

**Session:** AUDIT-WARM-2476 continuation, 15 July 2026.
**Scope:** `OPEN-WORKFLOW-PREDICTION-AUDIT` queue item 1 (mechanical layer).
**Deliverables:** `Development/integrity_audit/2026-07-15_mechanical_pass_raw.md`
(generated artifact, reproducible from the gate) +
`Development/integrity_audit/2026-07-15_adjudication_memo.md` (the analysis) +
this fragment + the WORKFLOW.md status update.

## What the sweep can and cannot say — stated before the result

The gate mechanizes spec items (a), (b)-static, (d), (f). It surfaces (c) and (e)
as WARN bands because circularity and input-as-output are judgment calls: a script
that assigns `expected = 0.5594` and compares against it is honest verification if
the input data came from geometry, and fabrication if the input data came from
`expected`. A regex cannot tell them apart; a reader can, in about five minutes per
script. The sweep therefore CANNOT certify the ~108 correspondences as genuinely
zero-parameter. What it can do is find every place where the ARTIFACT-level part of
the k-pattern recurs: cited scripts that do not exist, stubs, elisions, live
withdrawn billing, and frontier contradictions.

## The result, and the read I put on it

19 unique fabrication-class findings, 7 clusters, epicenter SR-1/SR-2 exactly as
the handover hypothesized. The tail outside SR is real but characteristically
different: SF-2's two panel review packages cite verify scripts that were never
committed (the most serious non-SR item — the panel adjudicated packages whose
verification does not exist); SF-1's reasoning fragments 1402/1403 lost the script
leg of their patch bundles (protocol violation, likely recoverable from
transcripts); SS-9 has a wrong-name citation propagated into its OSF/arXiv
submission guide plus one genuinely missing sketch script; SD-2 points readers at
supplementary code that is not there.

The negative result matters as much: no SM-series, QM-series, EU-1, SF-4, SF-6,
SF-7, SS-5, or SS-6 fabrication-class findings, and NO further instance anywhere of
the full five-step k-pattern (compute → absorb → bill → cite-unrun-verification).
The k defect and its immediate family appear to be localized, not endemic. That is
a mechanical-level statement only, and I have written it with the qualifier every
time because the last instance to nominate a result as "most secure" was nominating
H.1.

## Decisions deliberately NOT taken this session

1. The F3 numpy question (116 findings) is a convention decision — mass-rewriting
   pre-2471 scripts to stdlib would be make-work; a repo-level dependency
   declaration honored by the gate is the cheap fix. Founder call, memo
   §Reproducibility.
2. The two fabricated-MC notebooks and their siblings are NOT deleted — their
   names embed the retracted claim (handover STILL-UNAUDITED list) and disposition
   (delete vs quarantine-with-tombstone) is a founder call with provenance
   implications.
3. The theorem track is registered as explicitly open, not silently absorbed:
   the gate covers theorems only where they cite scripts, and H.1 is the proof
   that read-time review of proofs is worth nothing. The ordering heuristic
   (load-bearing, class-coverage, script-less first) is in the memo.

## G7 note

Nothing in this pass moves any physics verdict. The sweep found artifact debt, not
new physics; no status of any prediction or theorem was changed by this patch
except the audit item's own.
