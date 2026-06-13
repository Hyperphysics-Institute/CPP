<!--
  Extracted from Research_Frontier.md lines 1370-1384
  Source range: Workflow / Infrastructure
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Workflow / Infrastructure (WORKFLOW) — 1 problem

### OPEN-WORKFLOW-1: Consolidate All Bibliography Files
**Status:** OPEN
**Sector(s):** Infrastructure
**Priority:** MEDIUM
**One-line statement:** Merge all 12 per-paper and per-series `.bib` files into `bibliography/cpp_references.bib` as the single master bibliography; update old paper `.tex` files to reference it.
**What a solution looks like:** (1) Audit all 245 existing entries across 12 files; (2) resolve 22 known citation-key collisions (different content with same key); (3) merge 113 unique entries into master; (4) update `\bibliography{}` commands in all existing paper `.tex` files to reference master only; (5) move legacy `.bib` files to `archive/pre_consolidation_2026-04-15/`; (6) verify all papers still compile with same citation output.
**Tractability:** 1 dedicated session (2–3 hours of focused collision resolution and compile verification)
**Tooling (13 June 2026):** `scripts/consolidate_bibliography.sh` automates the per-paper consolidation **for local use** (needs working pdflatex+bibtex; not the container). It merges each per-paper bib's unique entries into the master (collisions keep the master entry), repoints the `.tex`, and converts a paper **only if** its BibTeX-generated `.bbl` is byte-identical before/after the repoint — proving the rendered bibliography (hence the OSF artifact) is unchanged. Papers whose `.bbl` changes (e.g. a self-citation where the master entry renders a trailing URL differently) are auto-reverted and flagged `[REVIEW]` for a manual accept-or-canonicalize decision. Per-series bibs (`cpp_*_series`, `gr_companion`, `references`) are deliberately excluded pending content-classification. Run `--dry-run` first; does not commit.
**What was done (15 April 2026):** Policy declared — master file is single source of truth; new papers cite master only; legacy files frozen with deprecation headers. SS-3 bibliography entries (cpp_ss3, humphreys1972) added to master. Stale `cpp_ss3` key in strong-series bibs renamed to `cpp_ss3_old_gluons` to free the namespace.
**What was done (13 June 2026 — SR-2 SHIP audit + gate hardening):** The SR-2 SHIP surfaced a *fresh* regression — a local `SR-2_references.bib` authored at draft time (Patch 1136) in violation of the 15-Apr policy — which the per-step checklist did not catch. Fixed: migrated to master + removed (Patch 1147); SR-2 is now the **first paper fully central-bib compliant at SHIP**. Hardened against recurrence (Patch 1149): OS §10 now states an explicit **BLOCKING SHIP GATE** precluding *creation* of any new per-paper/per-series `.bib`; paper-completion-checklist item **H7** added; `scripts/publication_audit.sh` now emits a `[FAIL]` (not advisory) for a paper's own local `.bib` or a `\bibliography{[ID]_references}` in its `.tex`.
**Current non-compliant inventory (13 June 2026 audit; remediation = this consolidation task):**
- Per-paper local bibs: `SR-1_references.bib`; `SM-6/7/8/9/10_references.bib` (6 papers).
- Stray master copy: `series_standard_model/papers/cpp_references.bib` (duplicate outside `bibliography/`).
- Per-series bibs cited in `.tex`: `cpp_ew_series` (EW-1..5), `cpp_strong_series` (SS-line), `cpp_qm_series` (QM-1..6), `cpp_foundations_series` (SD-1..5), `gr_companion` (c07 + GR companions), `references` (DP-Sea model).
- Compliant: SR-2 (and any future paper, enforced by the H7 gate).
**Collision classification (13 June 2026 audit — de-risks the consolidation):** The per-paper-bib key collisions with the master were sampled and are **benign / cosmetic, not "different content"** as the earlier "(2) resolve 22 known collisions" line feared. Every external-reference collision checked (`coxeter1973`, `pdg2024`, `koide1983`, `georgi1974`, `foot1994`, `rivero2005`, `humphreys1972`) is the **same reference** in legacy and master (identical titles); the diffs are whitespace / field-order / a trailing `\url{}`. Self-entry collisions (`abshier2026*`) are version/URL drift (e.g. master `abshier2026sr1` lacks the `\url{}` the SM-6 copy carries). **Implication:** repointing a paper to the master keeps the master entry (canonical) and renders the *same* bibliography. Unique-entry merge load (legacy keys absent from master): **SR-1 = 18**, SM-6 = 1, SM-8 = 1, SM-9 = 2, SM-7 = 0, SM-10 = 0; the stray `series_standard_model/papers/cpp_references.bib` = 31 entries, all already in master (unreferenced by any `.tex`), so removable. **Not yet classified:** the per-series bibs (`cpp_*_series`, `gr_companion`, `references`) — the documented "22 collisions" figure may live there; classify in the dedicated session.
**OSF re-deposit determination (13 June 2026):** A central-bib repoint that preserves rendered output does **not** require an OSF update. OSF versions track the scholarly artifact (the paper as read); the CPP convention ties re-deposit to mechanism/main-claim changes (paper-completion-checklist Completion Criterion), not internal build wiring. Because the sampled collisions are same-reference, the rendered bibliography is preserved (modulo trivial formatting like a stray URL — not a content revision). The only papers that would need an OSF touch are any where a *per-series* collision turns out to resolve a citation to a genuinely different work — which is exactly what the per-series classification (above) must confirm before that paper is repointed. Net: for SR-1 + SM-6..10, expected **no OSF re-deposit**; confirm per-paper at remediation by diffing the rendered reference list pre/post.
**Verification constraint:** step (6) "verify same citation output" requires a clean per-paper recompile; the container cannot reliably compile the legacy papers (SR-1's in-place compile truncated its PDF during the 1149 audit run), so the remediation must run on a machine where each paper compiles — i.e. the dedicated local session, not an in-container sweep.
**Paper(s):** None (infrastructure)
**Last updated:** 13 June 2026

---

