# CPP Programme To-Do List

**Location**: `/CPP/todolist.md` (repo root, parallel to `Research_Frontier.md`, `future_projects.md`, `paper_catalog.md`).

**Purpose**: Track small carried-over items, deferred protocol steps, and hygiene gaps that don't warrant full `future_projects.md` entries but must be cleared before the next paper begins. The "easy to lose" things — things that compound if not externalized.

**Discipline (introduced 7 May 2026 Session 33 close)**: A new paper does not start until this file's **P1 — Must clear before next paper** section is empty. Items move to **Cleared items (history)** at the bottom when completed (with date and patch number for audit). Items can also be reclassified to `future_projects.md` if they grow into multi-session projects, or deleted as no-longer-applicable with a note.

## How this file relates to other tracking files

- **`future_projects.md`** — registered active projects with full mechanism / falsifier / companion fields. Multi-session work with a clear deliverable. SS-9 anthology chapter (A.3) and TATWD integration (A.4) live there, not here.
- **`Research_Frontier.md`** — last-updated session-by-session log of the programme's frontier state. Programme-level open problems and their status.
- **`session_logs/`** — per-session entries capturing what happened.
- **`todolist.md`** (this file) — *small carried-over items, deferred protocol steps, hygiene gaps*. Kept short on purpose. If an entry here grows beyond a few patches of work, promote it to `future_projects.md`.

A new item belongs here (rather than in `future_projects.md`) if it's: small enough to clear in one or a few patches; not its own multi-session project; or explicitly deferred from a session whose main work was different.

---

## P1 — Must clear before next paper (SS-10)

### TODO-001 — SS-9 Phase 7 Section A 7-companion documentation suite

**Status**: DEFERRED pending trigger
**Trigger**: After (a) public posting (OSF + arXiv) lands AND (b) external-feedback window settles — either no v1.x revision arrives within Thomas's chosen window, or v1.x ships and stabilizes.
**Deliverable**: 7 companion files per `templates/paper_completion_checklist.md` Section A and `templates/documentation-suite.md`:
- `mechanism-SS-9.md` (A1) — step-by-step mechanism narrative with mathematical-correspondence table
- `glossary-SS-9.md` (A2) — paper-specific terms organized by category
- `phenomena-SS-9.md` (A3) — what the paper explains (PHEN-E empirical, PHEN-P predictions, PHEN-V consilience)
- `philosophy-SS-9.md` (A4) — epistemological framing
- `development-SS-9.md` (A5) — already exists as session-continuity file; may need final consolidation pass at v1.0+ trigger
- `reviews-SS-9.md` (A6) — all reviews + FAQ
- `keywords-SS-9.md` (A7) — keywords and registry cross-refs
**Estimated effort**: 1 dedicated session (~3-5 hours per checklist).
**Why deferred**: Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35-48): default to deferring Trigger 2 until paper is unambiguously done. SS-9's sub-task (e) was rescoped to "open invitation post-v1.0 ship via public posting," creating a built-in feedback pipeline that may produce v1.x. Producing 7 companion files now risks needing to redo them. The OPEN-SS-22 retirement experience (SS-7 v1.1 → v1.2) is the precedent.
**Registered**: 7 May 2026 Session 33 close.

### TODO-002 — SS-8 and SS-9 PDF compile (posting prerequisite)

**Status**: HYGIENE GAP — also a TODO-007 (public posting) prerequisite
**Issue**: Two papers are missing their `.pdf` artifacts in the repo despite having been compiled locally during their respective ship sessions. (a) `series_strong/papers/SS-8/` has `SS-8_interstitial_neutron_2EV_scaling.tex` but no `.pdf`; SS-8 has v1.0 OSF pending per `paper_catalog.md` but the PDF was never committed. (b) `series_strong/papers/SS-9/` has `SS-9_simplicial_alpha_polytope_connectivity.tex` but no `.pdf`; `paper_catalog.md` describes SS-9 as "32 pages compiled, three pdflatex passes zero errors after pass 3" referring to the local Session 32 v1.0 ship compile, but `git log --all` shows the PDF was never committed. (Compare SS-7 which has both `SS-7_alpha_cluster_edge_formula.tex` AND `SS-7_alpha_cluster_edge_formula.pdf` in the repo.) **The original TODO-002 entry in this file at Session 33 close incorrectly stated "SS-9 has both .tex and .pdf" — that was an error caught Session 36.** Both PDFs are posting prerequisites since OSF and arXiv submissions both require PDF.
**Deliverable**: Three-pass `pdflatex` + `bibtex` build of SS-8 v1.0 AND SS-9 v1.0; commit both `.pdf` files to the repo at `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.pdf` and `series_strong/papers/SS-9/SS-9_simplicial_alpha_polytope_connectivity.pdf`. Verify against `paper_catalog.md` rows (currently both show v1.0 OSF pending).
**Estimated effort**: 1 small patch from Thomas's local environment (~15 minutes for both PDFs combined; pdflatex not available in Claude's sandbox so this is a Thomas action).
**Apply chain when ready**: `git add series_strong/papers/SS-8/*.pdf series_strong/papers/SS-9/*.pdf && git commit -m "TODO-002 cleared: SS-8 + SS-9 PDF compile and commit" && git push origin main`. No format-patch chain needed — single direct commit + push from Thomas's local repo.
**Registered**: 7 May 2026 Session 33 close; **scope corrected** 7 May 2026 Session 36 patch 0285 to include SS-9.

### TODO-003 — Tier 4 reasoning recovery for chat window `a49b320e` (March 19 – April 6, 2026)

**Status**: PROGRAMME-LEVEL DEFERRED (largest single backlog item)
**Issue**: Foundational development of SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5 happened in this chat window; substantive Opus reasoning has not been recovered into per-paper `reasoning-[ID].md` files.
**Deliverable**: Per-paper `reasoning-SR-1.md`, `reasoning-EW-1.md` through `reasoning-EW-5.md`, `reasoning-SS-1.md`, `reasoning-QM-1.md` through `reasoning-QM-6.md`, `reasoning-SM-1.md` through `reasoning-SM-5.md` (16 files). Source: chat window `a49b320e` transcript at `/mnt/transcripts/` if accessible, or `conversation_search` recovery per the `templates/operating_system.md` §6 protocol.
**Estimated effort**: Multi-session — could be ~16 separate small patches (one per paper) or a single large multi-patch chain. Pre-session inspection of the source transcript will determine scope.
**Registered**: 7 May 2026 Session 33 close (carried over from earlier programme-level backlog per Claude's memory of prior work).

### TODO-004 — `reasoning-SM-9.md` (patch 0027, pine-tree model)

**Status**: PROGRAMME-LEVEL DEFERRED
**Issue**: SM-9 development arc captured Opus reasoning around the pine-tree model derivation; not yet recovered to `reasoning-SM-9.md`.
**Deliverable**: `reasoning-SM-9.md` per the four-tier discipline format used for SS-9.
**Estimated effort**: 1 patch (per the previously-planned patch 0027 numbering).
**Registered**: 7 May 2026 Session 33 close (carried over).

### TODO-005 — `reasoning-SM-10.md` (patch 0028, FEM journey)

**Status**: PROGRAMME-LEVEL DEFERRED
**Issue**: SM-10 development arc captured Opus reasoning around the FEM (finite element method) journey; not yet recovered to `reasoning-SM-10.md`.
**Deliverable**: `reasoning-SM-10.md` per the four-tier discipline format.
**Estimated effort**: 1 patch (per the previously-planned patch 0028 numbering).
**Registered**: 7 May 2026 Session 33 close (carried over).

### TODO-006 — OPEN-WORKFLOW-1 legacy `.bib` file cleanup

**Status**: PROGRAMME HYGIENE
**Issue**: Bibliography consolidation policy established `bibliography/cpp_references.bib` as single source of truth; legacy per-series and per-paper `.bib` files are deprecated (per `templates/paper_production_workflow.md` Phase 2 note: "Do NOT create a new per-paper `[ID]_references.bib` file — those are deprecated"). Cleanup audit is registered as OPEN-WORKFLOW-1.
**Deliverable**: Audit `series_*/` and `series_*/papers/*/` for stray `.bib` files; delete or migrate entries to `bibliography/cpp_references.bib`; verify all paper `.tex` files cite the central `.bib`.
**Estimated effort**: 1 small audit-and-cleanup patch (depends on how many strays exist).
**Registered**: 7 May 2026 Session 33 close (carried over from earlier OPEN-WORKFLOW-1 registration).

---

## P2 — At Thomas's discretion (not blocking next paper)

### TODO-007 — SS-9 public posting (OSF deposit + arXiv submission)

**Status**: PENDING Thomas's timing decision
**Operational protocol**: `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` (created Session 33 patch 0268).
**Two reasonable options** (both consistent with rescoped sub-task (e)):
- **Option A**: post now to lock priority date and start external-feedback clock.
- **Option B**: wait until anthology chapter (Session 34) and TATWD integration (Session 35) are complete to present a fuller programme picture at posting time.
**Note**: TODO-001 (SS-9 Phase 7 Section A) trigger depends on this resolving — public posting is the precondition for the external-feedback window.
**Registered**: 7 May 2026 Session 33 close.

---

## Cleared items (history)

*Items move here with date and patch number when completed. Cleared items are not deleted — they form an audit trail of what was done and when.*

(none yet — this file introduced 7 May 2026 Session 33 close, patch 0274)

---

## Maintenance

This file is maintained per session: any session that completes a TODO item moves it to "Cleared items (history)" with the completion date and patch number. Any session that identifies a new deferred item adds it here under the appropriate priority. Sessions that touch only this file (no other substantive work) follow the standard programme practice of session log + Research_Frontier.md last-updated entry — the documentation suite for a paper is updated only if the cleared item was paper-specific.

If this file's P1 section grows large (more than ~10 items), reconsider whether some items should be promoted to `future_projects.md` as registered multi-session projects rather than carried as to-dos.

If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why. The discipline is "P1 must be empty before SS-10," not "every deferred item is P1."
