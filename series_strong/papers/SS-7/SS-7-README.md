# SS-7 — Per-Paper Subfolder

SS-7 (Alpha-Cluster Regime and the 3N−6 Edge Formula for Medium-Mass Nuclei) was migrated to the per-paper subfolder convention on 25 April 2026 (patch 0020, OPEN-ORG-004 final completion). Original locations: split between `series_strong/` (v1.2 root copies, drag-drop misfiled) and `series_strong/papers/` (flat layout including stale v1.1 copies).

## Layout

```
SS-7/
├── SS-7-README.md                                          ← this file
├── SS-7_alpha_cluster_edge_formula.tex                     ← canonical .tex (v1.2; from series_strong/ root)
├── SS-7_alpha_cluster_edge_formula.pdf                     ← compiled PDF (v1.2)
├── reviews/                                                ← verbatim reviewer correspondence (empty; reviews live in reviews-SS-7.md)
├── letters/                                                ← Claude Opus correspondence (8 files)
│   ├── SS-7_chatgpt_rereview_request_letter.md
│   ├── SS-7_chatgpt_round2_closing_letter.md
│   ├── SS-7_copilot_round2_closing_letter.md
│   ├── SS-7_v0.1_chatgpt_review_response.md
│   ├── SS-7_v0.1_copilot_review_response.md
│   ├── SS-7_v1.0_chatgpt_round2_response.md
│   ├── SS-7_v1.0_copilot_round2_response.md
│   └── SS-7_v1.2_reviewer_verification_letter.md
├── sketches/                                               ← derivation notes, exploratory analyses (2 files)
│   ├── SS-7_v1.1_G3_discrepancy_note.md                   ← technical note registering the G3 RMS discrepancy that drove the v1.2 cycle
│   └── SS-7_v1.2_revision_plan.md                         ← v1.2 revision plan (pre-execution)
├── scripts/                                                ← Python verification scripts (1 file)
│   └── SS-7_alpha_cluster_edge_formula.py                 ← v1.2 numerical verification (8 zero-parameter predictions, R_alpha-alpha derivation, extended N=Z chain)
├── founders_voice/                                         ← Thomas's recorded intuitions (empty)
└── documentation_suite/                                    ← 12 files (8 doc-suite + handover + 2 transcripts + OSF status)
    ├── development-SS-7.md
    ├── glossary-SS-7.md
    ├── handover-SS-7.md                                    ← renamed from SS-7_v1.2_handover.md (matches SS-8 lab-notebook-trio convention)
    ├── keywords-SS-7.md
    ├── lay-summary-SS-7.md
    ├── mechanism-SS-7.md
    ├── phenomena-SS-7.md
    ├── philosophy-SS-7.md
    ├── reviews-SS-7.md
    ├── transcript-SS-7.md                                  ← renamed from SS-7_development_transcript.md (covers v0.1 → v1.1 development arc)
    ├── SS-7_v1.2_transcript.md                             ← kept name; v1.2 cycle-specific addendum (symmetric-honesty retirement)
    └── SS-7_OSF_registration_status.md                     ← v1.1 OSF registration status (preserved for audit; v1.2 status pending separate update)
```

Two of six standard subfolders are empty (`founders_voice/`, `reviews/`) and carry `.gitkeep` placeholders.

## Status

**Paper version:** v1.2 (21 April 2026 header). Symmetric-honesty corrections cycle complete; OPEN-SS-22 retired as the first retired open problem in the programme record. 12 concurrent zero-parameter N=Z alpha-chain predictions at N_α ∈ [3,14], RMS 0.80%; registers OPEN-SS-25.

**OSF status:** Existing DOI 10.17605/OSF.IO/JXE8D from v0.1 registration. v1.2 PDF update pending Thomas-side action per `documentation_suite/SS-7_OSF_registration_status.md` (status doc references v1.1; v1.2 update is implicit but undocumented separately).

**Doc-suite completeness:** 8 of 8 doc-suite files at v1.2 header currency (mechanism, glossary, phenomena, philosophy, keywords, development, reviews, lay-summary). Plus the lab-notebook trio (handover, transcript, v1.2 transcript addendum) and OSF status doc.

**Notable v1.1 vs v1.2 duplicate cleanup (resolved during this migration):** When the migration audit began, two copies of the .tex/.pdf/.py existed: v1.2 at `series_strong/` root (Thomas's drag-drop misfile) and v1.1 at `series_strong/papers/` (flat). The v1.2 copies were promoted to canonical via `git mv` into this folder; the v1.1 copies were archived to `archive/SS-7_versioned_drafts/` with explicit `_v1.1` filename suffix per Thomas's instruction during the migration scoping conversation.

## Migration cross-reference

This subfolder migration involved 30 file operations: 25 git mvs + 5 archive moves. The following table shows the major categories:

### Files migrated to `series_strong/papers/SS-7/` (canonical layer):

| Original location | New location |
|---|---|
| `series_strong/SS-7_alpha_cluster_edge_formula.tex` (v1.2 root) | `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` |
| `series_strong/SS-7_alpha_cluster_edge_formula.pdf` (v1.2 root) | `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.pdf` |
| `series_strong/SS-7_alpha_cluster_edge_formula.py` (v1.2 root) | `series_strong/papers/SS-7/scripts/SS-7_alpha_cluster_edge_formula.py` |
| `series_strong/SS-7_v1.2_handover.md` (root) | `series_strong/papers/SS-7/documentation_suite/handover-SS-7.md` (RENAMED) |

### Files migrated to documentation_suite/ (12):

| Original location (flat at series_strong/papers/) | New location |
|---|---|
| `development-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/development-SS-7.md` |
| `glossary-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/glossary-SS-7.md` |
| `keywords-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/keywords-SS-7.md` |
| `lay-summary-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/lay-summary-SS-7.md` |
| `mechanism-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/mechanism-SS-7.md` |
| `phenomena-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/phenomena-SS-7.md` |
| `philosophy-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/philosophy-SS-7.md` |
| `reviews-SS-7.md` | `series_strong/papers/SS-7/documentation_suite/reviews-SS-7.md` |
| `SS-7_development_transcript.md` | `series_strong/papers/SS-7/documentation_suite/transcript-SS-7.md` (RENAMED) |
| `SS-7_v1.2_transcript.md` | `series_strong/papers/SS-7/documentation_suite/SS-7_v1.2_transcript.md` (kept name) |
| `SS-7_OSF_registration_status.md` | `series_strong/papers/SS-7/documentation_suite/SS-7_OSF_registration_status.md` |

### Files migrated to letters/ (8):

All eight `SS-7_*_letter.md`, `SS-7_*_response.md`, and `SS-7_v1.2_reviewer_verification_letter.md` files moved to `series_strong/papers/SS-7/letters/`.

### Files migrated to sketches/ (2):

`SS-7_v1.1_G3_discrepancy_note.md` and `SS-7_v1.2_revision_plan.md` moved to `series_strong/papers/SS-7/sketches/`.

### Files archived (5):

| Original location | Archive location |
|---|---|
| `series_strong/papers/SS-7_alpha_cluster_edge_formula.tex` (v1.1 stale) | `archive/SS-7_versioned_drafts/SS-7_alpha_cluster_edge_formula_v1.1.tex` |
| `series_strong/papers/SS-7_alpha_cluster_edge_formula.pdf` (v1.1 stale) | `archive/SS-7_versioned_drafts/SS-7_alpha_cluster_edge_formula_v1.1.pdf` |
| `series_strong/papers/SS-7_alpha_cluster_edge_formula.py` (v1.1 stale) | `archive/SS-7_versioned_drafts/SS-7_alpha_cluster_edge_formula_v1.1.py` |
| `series_strong/SS-7_v1.2_apply_instructions.md` (transient) | `archive/SS-7_versioned_drafts/SS-7_v1.2_apply_instructions.md` |
| `series_strong/0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch` (transient) | `archive/SS-7_versioned_drafts/0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch` |

The canonical .tex uses an embedded `\begin{thebibliography}` block (no external `.bib` reference), so moving it required no path-update inside the .tex file. Compilation behavior unchanged.

## Convention reference

This subfolder structure follows `templates/operating_system.md` §11 "Per-paper subfolder convention" and the `{scope}-README.md` convention codified in the same §11 location (patch 0017). The `documentation_suite/` folder uses the unified convention codified in `templates/documentation-suite.md` §"Folder Location" (patch 0015).
