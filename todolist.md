# CPP Programme To-Do List

**Location**: `/CPP/todolist.md` (repo root, parallel to `research_frontier.md`, `future_projects.md`, `paper_catalog.md`).

**Purpose**: Track small carried-over items, deferred protocol steps, and hygiene gaps that don't warrant full `future_projects.md` entries but must be cleared before the next paper begins. The "easy to lose" things — things that compound if not externalized.

**Discipline (introduced 7 May 2026 Session 33 close)**: A new paper does not start until this file's **P1 — Must clear before next paper** section is empty. Items move to **Cleared items (history)** at the bottom when completed (with date and patch number for audit). Items can also be reclassified to `future_projects.md` if they grow into multi-session projects, or deleted as no-longer-applicable with a note.

## How this file relates to other tracking files

- **`future_projects.md`** — registered active projects with full mechanism / falsifier / companion fields. Multi-session work with a clear deliverable. SS-9 anthology chapter (A.3) and TATWD integration (A.4) live there, not here.
- **`research_frontier.md`** — last-updated session-by-session log of the programme's frontier state. Programme-level open problems and their status.
- **`session_logs/`** — per-session entries capturing what happened.
- **`todolist.md`** (this file) — *small carried-over items, deferred protocol steps, hygiene gaps*. Kept short on purpose. If an entry here grows beyond a few patches of work, promote it to `future_projects.md`.

A new item belongs here (rather than in `future_projects.md`) if it's: small enough to clear in one or a few patches; not its own multi-session project; or explicitly deferred from a session whose main work was different.

---

## P1 — Must clear before next paper (SS-10)

*(Empty — gate cleared 7 May 2026 Session 36 close patch 0288. SS-10 may begin.)*

The Session 36 P1 audit found that all originally-P1 items except TODO-002 were either deferred on external triggers (TODO-001) or were historical/programme hygiene that does not actually forward-block SS-10 (TODO-003, 004, 005, 006). Per this file's own escape-valve discipline (*"If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why"*), they were demoted to P2 and TODO-002 was cleared after its actual completion via patches 0286 + 0287 + commit `55c5986`. Result: P1 genuinely empty; SS-10 begins on a clean slate at the next session.

---

## P2 — At Thomas's discretion (not blocking next paper)

### TODO-001 — SS-9 Phase 7 Section A 7-companion documentation suite

**Status**: DEFERRED pending external-feedback trigger; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: The Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35-48) defers this until SS-9 is unambiguously done — meaning until either (a) v1.x revision ships and stabilizes after external feedback or (b) a reasonable post-posting window passes with no feedback. The trigger is gated on TODO-007 (public posting) and is *external* in nature, so the item cannot fire on its own and producing the 7 companion files prematurely risks rework. Demotion to P2 acknowledges that the file's own discipline is being honored: this is a deferred item awaiting an external trigger, not an item the next session must clear before starting SS-10.
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
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-003 — Tier 4 reasoning recovery for chat window `a49b320e` (March 19 – April 6, 2026)

**Status**: PROGRAMME-LEVEL DEFERRED multi-session backlog; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Recovery of substantive Opus reasoning into per-paper `reasoning-[ID].md` files for already-shipped historical papers (16 papers: SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5) is hygiene work on the historical record, not a precondition for new paper work. SS-10's framing and execution do not depend on having recovered reasoning artifacts for unrelated earlier papers. This item should be revisited as a long-term backlog candidate; if it grows into a dedicated multi-session project, it should be promoted to `future_projects.md` rather than carried as a single TODO.
**Issue**: Foundational development of SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5 happened in chat window `a49b320e`; substantive Opus reasoning has not been recovered into per-paper `reasoning-[ID].md` files.
**Deliverable**: Per-paper `reasoning-SR-1.md`, `reasoning-EW-1.md` through `reasoning-EW-5.md`, `reasoning-SS-1.md`, `reasoning-QM-1.md` through `reasoning-QM-6.md`, `reasoning-SM-1.md` through `reasoning-SM-5.md` (16 files). Source: chat window `a49b320e` transcript at `/mnt/transcripts/` if accessible, or `conversation_search` recovery per the `templates/operating_system.md` §6 protocol.
**Estimated effort**: Multi-session — could be ~16 separate small patches (one per paper) or a single large multi-patch chain.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-004 — `reasoning-SM-9.md` (patch 0027, pine-tree model)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003 — historical hygiene for an already-shipped paper, does not gate SS-10.
**Deliverable**: `reasoning-SM-9.md` per the four-tier discipline format used for SS-9.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-005 — `reasoning-SM-10.md` (patch 0028, FEM journey)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003.
**Deliverable**: `reasoning-SM-10.md` per the four-tier discipline format.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-006 — OPEN-WORKFLOW-1 legacy `.bib` file cleanup (programme-wide bibliography migration)

**Status**: PROGRAMME-WIDE MIGRATION — scope much larger than originally registered; not a forward blocker for SS-10
**Why P2 (Session 36 demotion + scope expansion)**: The Session 36 audit found **14 stray `.bib` files** across the repo, with most still **actively cited** by ~25 `.tex` files spanning every series. This is not a quick "audit and delete" patch — it's a programme-wide migration touching SR-1, SM-6 through SM-10, EW-1 through EW-5, QM-1 through QM-6, SS-1, SD-1 through SD-5, plus the orphan-or-active `series_strong/papers/cpp_strong_series.bib` and three `series_strong/cpp_strong_series*.bib` files at the series root. SS-7 and SS-9 use inline `\begin{thebibliography}` blocks (no .bib file at all). SS-8 and SM-3 use the canonical `bibliography/cpp_references.bib`. SS-10 can adopt the canonical pattern (like SS-8 did) regardless of what other papers use, so this migration does not forward-block SS-10. **Recommendation for next session**: consider promoting this to `future_projects.md` as a multi-session OPEN-WORKFLOW-1 project, since it's no longer "1 small patch" scope.
**Issue**: Bibliography consolidation policy established `bibliography/cpp_references.bib` as single source of truth; legacy per-series and per-paper `.bib` files are deprecated (per `templates/paper_production_workflow.md` Phase 2 note: "Do NOT create a new per-paper `[ID]_references.bib` file — those are deprecated"). Cleanup audit is registered as OPEN-WORKFLOW-1.
**Stray .bib inventory (Session 36 audit)**: `series_strong/cpp_strong_series.bib`, `series_strong/cpp_strong_series_papers.bib`, `series_strong/cpp_strong_series_root.bib`, `series_strong/papers/cpp_strong_series.bib`, `series_standard_model/papers/cpp_references.bib` (note: NOT canonical path), `series_standard_model/papers/SM-{6,7,8,9,10}_references.bib`, `series_electroweak/papers/cpp_ew_series.bib`, `series_quantum_mechanics/papers/cpp_qm_series.bib`, `series_foundations/series_superdeterminism/cpp_foundations_series.bib`, `series_relativity/papers/SR-1_references.bib`. Active `.tex` consumers identified per audit.
**Deliverable**: Programme-wide migration: (1) merge unique entries from each stray `.bib` into `bibliography/cpp_references.bib`; (2) update `\bibliography{...}` line in each consuming `.tex` to point to `../../../bibliography/cpp_references` (path depth varies by series structure); (3) delete strays; (4) recompile each affected paper to verify no broken citations.
**Estimated effort**: Multi-session if done thoroughly (likely 2-3 sessions); paper-by-paper migration with recompile verification per paper.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2 with scope expansion** 7 May 2026 Session 36 close patch 0288.

### TODO-007 — SS-9 public posting (OSF deposit + arXiv submission)

**Status**: PENDING Thomas's timing decision; OSF complication identified Session 36 (see below)
**Operational protocol**: `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` (created Session 33 patch 0268).
**Session 36 update — OSF complication identified**: Thomas's existing Open-Ended Registration `10.17605/OSF.IO/JXE8D` (the "Conscious Point Physics Paper Series" master registration created Mar 31, 2026, listing SS-1, SM-1 through SM-5, SR-1) has been stuck in **"Pending Admin Contributor Approval"** state for 5+ weeks despite the documented 48-hour auto-approval window. Thomas is the only admin contributor listed. Multiple support tickets sent; one received an unhelpful response (about a different registration); subsequent tickets unanswered including a Claude-drafted escalation. The DOI is real and the priority date (Mar 31, 2026) is locked, but the registration is technically not finalized. **Decision Session 36**: Thomas will submit one more diagnostic-specific support ticket framing the issue precisely as "Pending Admin Contributor Approval state stuck >38 days, only one admin contributor, auto-approval timer never fired." Wait 5 business days for OSF response. **If OSF resolves** → add SS-9 as an Update to the existing JXE8D registration (the registration is Open-Ended, designed to be added to over time), and post to arXiv in parallel (categories nucl-th + math-ph). **If OSF still silent after 5 business days** → fallback to depositing SS-9 on **Zenodo** (CERN-run, gives DOI, no comparable workflow issues) plus arXiv, treating OSF as a later catch-up.
**Two original options remain open** (both consistent with rescoped sub-task (e)):
- **Option A**: post now to lock priority date and start external-feedback clock.
- **Option B**: wait until anthology chapter (Session 34) and TATWD integration (Session 35) are complete to present a fuller programme picture at posting time.
Both are now fully available since Sessions 34 and 35 are complete; only the OSF technical issue remains as a delay factor.
**Note**: TODO-001 (SS-9 Phase 7 Section A) trigger depends on this resolving — public posting is the precondition for the external-feedback window.
**Registered**: 7 May 2026 Session 33 close; **OSF complication and fallback plan added** 7 May 2026 Session 36 close patch 0288.

### TODO-008 — OPEN-WORKFLOW-DOCS-CATCHUP (programme-wide documentation-suite discipline-tightening per discipline-tightening-after-precedent principle)

**Status**: REGISTERED — two-part item: (A) flagship documentation-suite backlog catch-up for SF-4 v1.0 and SF-2 v1.0; (B) programme-wide gate-language codification of synchronous-documentation-suite requirement for v1.0 SHIP going forward
**Why P2 (not P1)**: This is hygiene/discipline-tightening work — it does not gate any specific next paper. The flagship papers themselves are already shipped; their documentation-suite backlog is a programme-record-completeness item. The gate-language codification is forward-looking discipline that will apply to future flagships from the next v1.0 SHIP onward. Neither sub-item blocks SS-10 or any other in-flight work.

**Precedent (Capotauro v1.0 SHIP arc)**: Capotauro v1.0 SHIPPED at Patch 0415 Session 122 with **the first complete documentation suite shipped synchronously with a CPP flagship v1.0 SHIP**. The Session 123 doc-suite catch-up arc (Patches 0416–0416L) produced ten documentation files: Section E four-tier discipline (handover ✓ 0416 + development ✓ 0416B + transcript ✓ 0416C + reasoning ✓ 0416D) + Section A six standalone companions (mechanism ✓ 0416E + glossary ✓ 0416F + phenomena ✓ 0416G + philosophy ✓ 0416H + reviews ✓ 0416I + keywords ✓ 0416J) + anthology chapter (✓ 0416K) + TATWD integration (✓ 0416L). This is the reference implementation for the synchronous-documentation-suite discipline. Per the **discipline-tightening-after-precedent principle** (recognized at Session 123 Patch 0416D as a programme-level convention; same pattern as Sessions 115–116 per-paper changelog file convention codification at Patch 0408 reference implementation → Patch 0409 programme-wide codification), the precedent makes credible the codification of synchronous-doc-suite requirement as a programme-wide v1.0 SHIP gate.

**Sub-item (A): Flagship documentation-suite backlog catch-up**

The two flagships that shipped v1.0 before Capotauro (SF-4 v1.0 at 14 May 2026; SF-2 v1.0 at 14 May 2026 jointly with its Companion paper) shipped without Section A standalone companions. Backlog inventory:

- **SF-4 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/neutrinos/documentation_suite/` has development-SF-4.md + handover-SF-4.md + reasoning-SF-4.md + transcript-SF-4.md (Section E four-tier discipline only)
  - Missing: mechanism-SF-4.md (A1) + glossary-SF-4.md (A2) + phenomena-SF-4.md (A3) + philosophy-SF-4.md (A4) + development-SF-4.md final consolidation pass (A5; current file is session-continuity, not the consolidated paper-development file) + reviews-SF-4.md (A6) + keywords-SF-4.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template
  - **Trigger**: After SF-4 v4.4 public posting (currently pending Thomas's timing decision per TODO-007-analog for SF-4) AND external-feedback window settles, per Two-Triggers discipline. Same trigger logic as TODO-001 for SS-9.

- **SF-2 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/electroweak/documentation_suite/` has development-SF-2.md + handover-SF-2.md + reasoning-SF-2.md + transcript-SF-2.md (Section E four-tier discipline only); Companion paper documentation status to be audited
  - Missing: mechanism-SF-2.md (A1) + glossary-SF-2.md (A2) + phenomena-SF-2.md (A3) + philosophy-SF-2.md (A4) + development-SF-2.md final consolidation pass (A5) + reviews-SF-2.md (A6) + keywords-SF-2.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template; possibly 2 sessions if Companion paper warrants parallel suite
  - **Trigger**: Same Two-Triggers logic as SF-4 — after SF-2 v1.0 public posting + external-feedback window settles.

- **SS-9 v1.0 documentation-suite backlog**: Already tracked at TODO-001 (registered 7 May 2026 Session 33; demoted to P2 Session 36 Patch 0288). The SS-9 trigger logic is the canonical reference for the Two-Triggers discipline. TODO-008 does NOT re-register the SS-9 item; it cross-references TODO-001 as the SS-9 instance of the broader pattern.

**Sub-item (B): Programme-wide gate-language codification**

The Capotauro precedent makes credible a tightening of the v1.0 SHIP gate-language to require synchronous documentation-suite completion. The codification work is a separate downstream item, not bundled with the backlog catch-up:

- **`templates/operating_system.md` §4 Phase 7 (post-SHIP doc-suite work)** — modify gate-language to specify: "A flagship paper does not reach v1.0 SHIPPED status until its Section A 6 standalone companions + Section E 4 four-tier discipline files are complete in `flagship_papers/<paper>/documentation_suite/`. Synchronous completion is the default; the Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35–48) applies only as an explicit exception for cases where external-feedback gating is more important than synchronous completion (e.g., a paper that may revise substantially after first external review)."
- **`templates/paper_completion_checklist.md` Section A** — modify the Two-Triggers discipline language to clarify that synchronous completion is the new default (per Capotauro precedent), with the Two-Triggers as documented exception path rather than default workflow. The Two-Triggers default should remain available for papers like SS-9 where the v1.0 paper itself is the primary deliverable and the documentation suite can wait for external-feedback shape.
- **Cross-reference**: `book_project/chapters/capotauro_what_was_always_there.md` §"The Method Underneath" + `programme_orientation.md` Chapter 35.5 § Methodological observation as the master-document references for the precedent.
- Estimated effort: 1 patch (~30 minutes) — small editorial codification patches against the two template files. Should be done after Sub-item (A) is at least partially in hand (per discipline-tightening-after-precedent principle: the codification is credible because multiple instances of the discipline now exist).

**Estimated effort total**: 2-3 sessions for Sub-item (A) (SF-4 + SF-2 backlog completion, possibly serialized); 1 small patch for Sub-item (B) (codification).
**Registered**: 16 May 2026 Session 123 close Patch 0416M as the **final patch in the Capotauro doc-suite catch-up arc** (Patches 0416 + 0416A through 0416L preceding this patch). Forward queue: items fire on Two-Triggers external-feedback signal for each affected paper; codification patch can fire any time after Sub-item (A) is partially in hand.

---

## Cleared items (history)

*Items move here with date and patch number when completed. Cleared items are not deleted — they form an audit trail of what was done and when.*

### TODO-002 — SS-8 and SS-9 PDF compile (posting prerequisite) — CLEARED 7 May 2026 Session 36

**Cleared**: 7 May 2026 Session 36 via patches 0286 (SS-8.tex `\Kthree` macro `\ensuremath` fix) + 0287 (SS-8.tex `\usepackage{xcolor}` import for `yellow!10` blend) + direct commit `55c5986` (PDFs added to repo: SS-8 31 pages 507596 bytes, SS-9 32 pages 638209 bytes; both visually verified clean before commit; SS-9 compile triggered MiKTeX auto-install of `float.sty` per Phase C MiKTeX setting change).
**Resolution narrative**: First Thomas attempt (without patches 0285+0286+0287) compiled with errors and produced damaged PDFs (SS-8 abstract garbled with run-together italicized text from `\Kthree`-mode-quantum text, mdframed alert box on pages 15-16 rendering as solid black from undefined `yellow!10`). Damaged PDFs were committed as `6e86818` then reverted as `ccb6041` after diagnosis. Patches 0286 (`\Kthree` `\ensuremath` wrapper) and 0287 (`xcolor` package import) were then applied; MiKTeX auto-install set to "Yes"; aux files cleaned; recompile produced clean PDFs verified visually (K₃ subscript renders cleanly, alert box light-yellow as designed). Commit `55c5986` pushed both PDFs to origin successfully.
**Original registration**: 7 May 2026 Session 33 close patch 0274; scope corrected Session 36 patch 0285 to include SS-9.

---

## Maintenance

This file is maintained per session: any session that completes a TODO item moves it to "Cleared items (history)" with the completion date and patch number. Any session that identifies a new deferred item adds it here under the appropriate priority. Sessions that touch only this file (no other substantive work) follow the standard programme practice of session log + research_frontier.md last-updated entry — the documentation suite for a paper is updated only if the cleared item was paper-specific.

If this file's P1 section grows large (more than ~10 items), reconsider whether some items should be promoted to `future_projects.md` as registered multi-session projects rather than carried as to-dos.

If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why. The discipline is "P1 must be empty before SS-10," not "every deferred item is P1."
