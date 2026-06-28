# Capture audit — DM Cross-Rod campaign (patches 0860–0889)

**Run:** 2026-06-28 (manual nightly-equivalent; the §3.1 automatic-capture macro is not yet built, so this
audit was run by hand against the **Option-B canonical verbatim source** — the Claude account data export
`conversations.json`, conversation `260625 0865 DM characteristics SF-2/SF-5`, 93 messages, updated
2026-06-28T07:06). **Auditor:** Opus. **Scope:** founder-contribution capture only (the §4.1 path).

## Finding

The Cross-Rod campaign's **load-bearing founder contributions were captured as trigger-references and
paraphrase in the per-patch reasoning fragments, but NOT preserved verbatim**, and they are **absent from
the canonical `founders_vision.md`** (whose DM section ends at the pre-Cross-Rod June-1 tetra-gravity
conjecture). This is the same capture-gap class the reasoning-capture protocol §10 exists to close: at the
time, the founder's words were available and were summarized rather than preserved. Because the verbatim
source survived in the account export, the loss is **recoverable** (the capture-and-audit protocol's central
claim — irreversible loss → recoverable processing loss — holds here in practice).

## Per-contribution audit

| Turn | Contribution | Patch anchor | Capture status |
|---|---|---|---|
| H5 | Planar-vs-helical hTetra excursions; chain grows until coplanar, ends edge-bond to loop | 0866–0867 (strand/loop morphology) | **PARAPHRASE** |
| H6 | ee-hinge bond probabilities (½ on ee, ¼ qq); the fluffy hTetra ball; weak +/+ −/− vertex bonding | 0868 (ball / branching d_f) | **PARTIAL** |
| H11 | hTetras are not long strands → side chains + amorphous mass; the 4-wide cross is a stiffer, different entity; glueball not viable | 0869–0870 (morphology pivot: strand killed, cross selected) | **PARAPHRASE** |
| H13 | 3D fluff on the cross spine is limited by eDP cocooning of the DP Sea — density reduced from the first layer; no preferred bonding reaction on the neutralized spine | 0880 (d_f=1 width mechanism) + 0872 (corona seed) | **PARAPHRASE** |
| H14 | The eDP coat cannot bond deep: the DP Sea's kT energetics are the same around the coat as in unnucleated space; transient eDP interbonding is the Sea's native state; the buffy coat is thin and transient | 0872–0877 (corona retirement) — the load-bearing physical insight | **GAP** |
| H25 | Naming the element the 'Cross-Rod'; the structural edit: the 8qCP cubic core + 4 hTetra element is the viable entity | 0879–0880 (Cross-Rod name + cube-core footnote) | **PARAPHRASE** |
| H26 | The cube-core structure derivation: 8qCP+8eCP = a cross of four e:q:q:e elements; the W-boson two-ring mental start; floppy open-qDP-edge ribbon folds into the glueball; the open attractive central qDP core accommodates a chain on either side → the cross | 0880 (genesis / cube structure) | **GAP** |
| H27 | The genesis story: qCP/eCP → qDP/eDP/hDP → hTetra; Method 1 (hTetras → Cross-Rod element → stack 4qCP-to-4qCP); Method 2 (qDP chains → eDP-qDP chains → four-fold bundle) | 0880 (genesis Methods 1 & 2) | **GAP** |
| H28 | The W-boson framing is mental inspiration only, not part of the assembly; the eqqe 4-wide ribbon lineage; the fifth-chain question | 0880 (genesis cleanup — W-omission) | **PARTIAL** |
| H41 | Versioning decision: the submission draft is DM-1 v0.2 (review candidate), not v1.0 until agreement across all reviews | 0888 (DM-1 → v0.2) | **CAPTURED** |

**Severity tally:** 3 GAP (verbatim insight not preserved), 4 PARAPHRASE, 2 PARTIAL, 1 CAPTURED.

The three **GAP** items (H14 corona insight, H26 cube-structure derivation, H27 genesis Methods) are the
most significant: they are the founder contributions that most directly shaped load-bearing results (the
corona retirement and the entire Cross-Rod structure/genesis), and they were the least faithfully preserved.

## Disposition (staged — NOT promoted)

Per capture-and-audit §4.1 (staged-default; *the machine never decides it has earned the right to write his
voice*), the verbatim backfill is **staged for TLA review**, not written to canonical `founders_vision.md`:
`Development/staging/2026-06-28/founders/dm_cross_rod_founders_backfill.md`. Every entry is labelled
**[REVIEW]** (multi-sentence physics with a context anchor — never an AUTO-promote class). TLA reviews,
edits/approves, and applies + pushes the approved entries to `founders_vision.md`. The canonical write stays
yours. Nothing in this patch touches `founders_vision.md`.

## Process note (for the documentation suite)

This gap is structural, not careless: it confirms the protocol's own diagnosis — *selective extraction done
in real time, in the hot path, under load, drops the founder's voice first*. The standing per-patch
founder-contribution block (reasoning-capture §10) caught the **fact** of a contribution (every gapped patch
correctly names Thomas as the trigger) but not the **words**. Two cheap hardening options for the suite work:
(a) when a patch's trigger is a founder turn, paste the verbatim turn into the fragment's founder block at
patch-time (not a summary of it); (b) until the automatic-capture macro exists, run this export-based audit
at each campaign close, while the export still contains the window.
