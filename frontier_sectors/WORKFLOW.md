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


---

### OPEN-WORKFLOW-1 — Session 1152 findings (bibliography consolidation, attempt 2)

**Context.** Re-attempt of the per-paper-bib → master consolidation after the
Session-1151 live run (commit `3911b39`) was reverted (`0c497b4`). The first run
failed every paper (3×SKIP, 3×REVERT) and zeroed two committed PDFs; revert
restored all. Root-causing the failures surfaced several findings independent of
the bib task itself.

**Script bugs fixed (consolidate_bibliography.sh v2, commit `9a53a62`):**
- *Backslash repoint path* — `os.path.relpath` on Windows emitted
  `..\..\bibliography\cpp_references`; LaTeX read `\b`,`\c` as escapes → bibtex
  never found master → recompile failed → false REVERT (SM-7/8/9). Fixed:
  force forward slashes.
- *Brittle baseline compile* — `-halt-on-error` on a cold first pass (no
  `.aux`/`.bbl`) returned non-zero on healthy papers → false SKIP. Fixed: no
  halt-on-error, two pdflatex passes, judge on `.bbl` production not exit code.
- *CRLF in `.bbl` diff* — MiKTeX CRLF output would read as a change vs an LF
  baseline → latent false REVIEW. Fixed: normalize line endings before compare.

**Repo-health findings (not bib-related; surfaced by the failures):**
- **`.gitignore *.pdf` blocks figure PDFs repo-wide.** Papers whose `.tex` does
  `\includegraphics{...pdf}` cannot compile from a clean clone — the figure PDFs
  are build artifacts, never committed (only SVG+PNG are). SM-6 was the tripwire;
  this is a *systemic* reproducibility gap affecting any PDF-figure paper.
  Fix pattern established (Option A, commit `19b4ac1`): commit a `build_figures.sh`
  in the figure dir that regenerates PDFs from committed SVGs via cairosvg;
  figure PDFs stay ignored. Reusable for other papers as the same issue is found.
- **SR-1 latent cold-compile bug** (commit `037e1e3`): line 1512 had escaped
  underscores in two `\ref` keys → `Missing \endcsname` fatal. Shipped PDF had
  been built from a state that no longer compiled cold (source/artifact drift).
- **SM-10 original SKIP was a false negative** — compiles clean cold, no repair
  needed; only the script bugs blocked it.

**OSF re-deposit pending** (rendered artifact changed vs deposit):
- SR-1 — 47→50 pp after the `\ref` fix (broken refs now resolve).
- SM-6 — rebuilt 16 pp with real (previously-missing) figures.
- (Bib repoint, when run, requires NO re-deposit — `.bbl`-identity by design.)

**State at note time:** three `1152` commits staged locally on `0c497b4`; bib
consolidation itself NOT yet re-run (pending `--only SM-10` validation of v2).

---

### OPEN-WORKFLOW-1 — Session 1152 addendum: SM-7/8/9 PARKED (master-bib content reconciliation needed)

**Where consolidation stopped and why.** SM-10 consolidated cleanly (commit
`c97b76d`). Extending to SM-7/8/9 surfaced that the master bib diverges from the
per-paper bibs in **three independent content classes**, varying entry-by-entry —
so a mechanical repoint would silently degrade shipped bibliographies. This is no
longer a consolidation task; it is a **reference-data reconciliation audit**, and
is parked for a dedicated session with the source-paper `.tex` titles/CHANGELOGs
open for adjudication.

**The three divergence classes found:**
1. **Version drift** (self-citation `note` versions). FIXED in master this session
   (commit `2d220f1`): SM-6 v2.1→v3, SM-10 v0.1→v2.0. Authority = each paper's own
   CHANGELOG. Other master SM entries already correct (SM-3 v6, SM-8 v4.1, SM-9 v2.2).
2. **URL/DOI completeness.** Master entries are MISSING `\url{...}` DOI links that
   the per-paper bibs carry (seen in SM-7's `[REVIEW]`: master drops the OSF DOI on
   abshier2026sm6/sm2 and a PhysRevLett.32.438 URL). Repoint-to-master would lose links.
3. **Title divergence (same key, different title).** `abshier2026sm2` (SM-2):
   - SM-7 local bib: "Mass Generation from Geometric Hierarchies"
   - master:         "Quark Mass Formula and Hybrid Spectral Structure"
   Substantive, not formatting. Authority = SM-2's own `.tex` title (UNRESOLVED —
   needs a look at SM-2_*.tex).

**Known-stale per-paper bib entries (will be corrected BY repointing to a
reconciled master, once master is made a correct superset):**
- SR-1 / SM-6 / SM-8 local bibs say SM-3 v5 (true: v6).
- SM-8 / SM-9 local bibs say SM-10 v1.0 (true: v2.0).
- SM-9 local bib says SM-9 v1.0 (true: v2.2) — stale about its own paper.

**Method limitation recorded.** The `.bbl`-byte-identity check proves "rendering
unchanged after repoint," NOT "rendering is correct." SM-10 passed only because its
local bib and master happened to agree on what SM-10 cites; it does not certify
those shared values are right. Reconciliation must validate against source `.tex`,
not against `.bbl` identity.

**Next-session task list (OPEN-WORKFLOW-1):**
1. Make master bib a correct superset: resolve SM-2 title vs SM-2.tex; restore the
   missing `\url{}` DOI fields; re-verify all self-citation versions vs CHANGELOGs.
2. Re-run consolidation SM-7 → SM-8 → SM-9 against the reconciled master; expect
   `[REVIEW]` to clear to loss-free `[OK]` (or accept changes that are pure
   corrections, manually repoint+archive).
3. Consolidate SR-1 and SM-6 (bibs still local; both now compile cold).
4. OSF re-deposit: SR-1 (47→50 pp), SM-6 (figures restored). 
5. Confirm SM-8 current version (header says v4.0; decided v4.1 — verify in CHANGELOG).

**Banked & committed this session (commits `9a53a62`→`2d220f1`):** script v3
(2 bug fixes, validated); SM-10 consolidated; SR-1 typo repair; SM-6 figure
build-script (Option A); master version-drift correction; this documentation.
1151 failed run honestly reverted (`0c497b4`). Tree clean at park.
