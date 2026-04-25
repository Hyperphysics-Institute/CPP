# SS-7 Versioned Drafts and Transient Artifacts Archive

Historical SS-7 paper trio (v1.1 stale copies superseded by v1.2 canonical) plus transient v1.2 cycle artifacts preserved here per `templates/operating_system.md` §11. Created 25 April 2026 (patch 0020) when SS-7 was migrated to its per-paper subfolder.

## Contents

### v1.1 stale paper trio (3 files)

The v1.2 cycle (symmetric-honesty corrections, OPEN-SS-22 retirement) was completed on 21 April 2026 with the canonical .tex/.pdf/.py landing at `series_strong/` root. The earlier v1.1 copies remained at `series_strong/papers/` (flat, pre-migration). These were superseded by v1.2 but kept on disk as side-by-side drafts. During patch 0020 migration, the v1.1 copies were moved here with explicit `_v1.1` filename suffix per Thomas's instruction in the migration scoping conversation.

| File | Header version | Notes |
|---|---|---|
| `SS-7_alpha_cluster_edge_formula_v1.1.tex` | "Version 1.1 — 20 April 2026 (post round-2 external review)" | 89,647 bytes |
| `SS-7_alpha_cluster_edge_formula_v1.1.pdf` | (paired with v1.1 .tex) | 440,232 bytes |
| `SS-7_alpha_cluster_edge_formula_v1.1.py` | "Paper: SS-7 v1.1" | 9,467 bytes; older numerical-verification script |

### Transient v1.2 cycle artifacts (2 files)

One-time artifacts produced during the v1.2 cycle that have served their purpose. Preserved for historical audit; not active programme content.

| File | Purpose |
|---|---|
| `SS-7_v1.2_apply_instructions.md` | Drag-drop apply instructions used by Thomas during the v1.2 patch cycle (5,362 bytes; supersedes itself once applied) |
| `0003-SS-7-v1.2-partial-paper-body-notebook-PH.patch` | Leftover patch file from the v1.2 work; the patch was applied as part of SS-7 v1.2 production and has no further active use |

## Reference

- `series_strong/papers/SS-7/SS-7-README.md` — current SS-7 paper folder
- `templates/operating_system.md` §11 — single-file-per-paper convention; patch-file lifecycle
- `series_strong/papers/SS-7/documentation_suite/transcript-SS-7.md` — narrative of v0.1 → v1.1 development
- `series_strong/papers/SS-7/documentation_suite/SS-7_v1.2_transcript.md` — narrative of v1.2 cycle including OPEN-SS-22 retirement
- `series_strong/papers/SS-7/sketches/SS-7_v1.1_G3_discrepancy_note.md` — the technical finding that triggered the v1.2 cycle
