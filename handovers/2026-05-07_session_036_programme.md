# Session 36 close — handover for next Opus context window

**Date authored**: 7 May 2026 (Session 36 close, programme date)
**Real date authored**: 8 May 2026 (Friday)
**Author**: Claude Opus 4.7 (current context window)
**For**: Claude Opus 4.7 (next context window)
**Programme**: Conscious Point Physics (CPP)
**Repo**: `github.com/Hyperphysics-Institute/CPP` (origin/main HEAD will be `2004327` after Thomas pushes patch 0288)

---

## What this document is

This is a context-window-transition handover. The current Session 36 conversation is long enough that Thomas needs a fresh context window to start Session 37. This document gives the next Opus context everything it needs to pick up cleanly without rereading the entire Session 36 conversation.

**Read order recommended for the next context**:

1. This document (orientation) — note the **"Strategic decision at Session 36 close"** section below SUPERSEDES the previous SS-10-focused forward queue
2. **`/CPP/research_priorities.md`** (NEW patch 0290 — strategic prioritization framework; **read this before any session work** to understand the active priority order)
3. **`/CPP/flagship_papers/unification/hierarchy_paper_outline.md`** (original Track-1 active paper outline with four open questions for Thomas — relocated from `papers_in_progress/` per patch 0293; folder renamed `hierarchy_problem/` → `unification/` per patch 0295 when Option-3 four-family + unification SF-line architecture was adopted; this outline now serves as source material for SF-5 the unification synthesis paper; Q1 dissolved into SF-4 neutrinos — see [`/CPP/flagship_papers/README.md`](flagship_papers/README.md))
4. `series_strong/papers/SS-9/documentation_suite/handover-SS-9.md` (SS-9-specific permanent handover; covers SS-9 history through Session 35 close + Session 36 patch 0285 errata)
5. The Session 36 entry + Session 36 close strategic appendix in `session_logs/2026-05-02_session_log.md` (technical details + durable strategic-conversation record)
6. `todolist.md` (P1-empty; new work picks up from research_priorities.md, NOT from todolist)
7. `research_frontier.md` last-updated header (latest programme-state summary; remember: this catalogs ALL 82+ open problems — most are now LOW priority per Session 36 strategic decision; only Track 1-4 problems are actively pursued)
8. `paper_catalog.md` SS-9 row (now at v1.0 SHIPPED with .pdf in repo)

---

## Where the programme is right now

**SS-9 is structurally complete.** The four-track paper completion sequence shipped:

| Track | Description | Status |
|---|---|---|
| Paper text | `SS-9_simplicial_alpha_polytope_connectivity.tex` v1.0 | ✓ Shipped Session 32, frozen per anti-priority |
| Track 1 | Anthology chapter `book_project/chapters/SS-9_the_polyhedrons_conditions.md` (~5389 words, Rovelli/SciAm register) | ✓ Done Session 34 |
| Track 2 | TATWD integration into `CPP_the_theory.md` (NEW Chapter 22c + Chapters 32-35) and `book_project/TATWD_outline_revised.md` | ✓ Done Session 35 |
| Track 3 | Registers freeze (`paper_catalog.md`, `theorem-registry.md` THEO-SS-16, `master_glossary.md`) | ✓ Done Session 33 |
| Track 4 | OSF/arXiv submission guide at `series_strong/papers/SS-9/letters/` | ✓ Done Session 33 |
| **PDF compile** | **SS-8 + SS-9 PDFs in repo (TODO-002)** | **✓ Done Session 36 — see below** |

**Programme state UNCHANGED** in technical sense across Sessions 33–36:
- 12 negative results
- 19 SS sector problems
- 4 OPEN-SS-37 closure routes
- SS-9 SHIPPED at v1.0

**`todolist.md` P1 is EMPTY at Session 36 close.** SS-10 may begin at the next session. The Session 36 P1 audit found that all originally-P1 items except TODO-002 (which was completed) were either deferred on external triggers or were historical/programme hygiene that does not actually forward-block SS-10. They were demoted to P2 per the file's own escape-valve discipline.

---

## What Session 36 actually did

Session 36 was mostly bookkeeping plus one substantive technical chain (TODO-002 PDF compile clearance). Here's the chronology:

### Phase 1 — Pre-OSF-posting verification caught two errata (patch 0285)

Just after the Session 35 close push, Claude pre-flighted OSF posting prep and caught two errata in the just-pushed Session 35 documentation:
1. **handover-SS-9.md filename wrong in 3 places** — had `SS-9_alpha_cluster_simplicial_polytope_derivation.tex` but actual filename is `SS-9_simplicial_alpha_polytope_connectivity.tex`. Same wrong filename had been in the handover since Session 34 (patch 0279) and went into Session 35 (patch 0284).
2. **`todolist.md` TODO-002 had wrong scope** — original entry said "SS-9 has both .tex and .pdf" but `git log --all` showed SS-9 PDF was never committed despite `paper_catalog.md` describing SS-9 as "32 pages compiled." The Session 32 v1.0 ship compile was local-only; PDF was never in repo.

Patch 0285 fixed both: 3 filename corrections in handover-SS-9.md + TODO-002 scope expanded to cover both SS-8 AND SS-9 PDFs.

### Phase 2 — TODO-002 PDF compile (the technical chain)

This took several iterations because Thomas's local LaTeX environment surfaced bugs in SS-8.tex that hadn't been compiled since Session 32 (or possibly never compiled cleanly).

**First Thomas attempt** (without patches 0286 + 0287, before MiKTeX auto-install enabled):
- SS-8 compile failed at line 278 abstract: `! Missing $ inserted` on `the programme-level \Kthree-mode quantum first identi...`. The `\Kthree` macro was defined as bare `\newcommand{\Kthree}{K_3}` (math-mode subscript syntax) but invoked in text mode in the abstract paragraph and keywords line.
- pdflatex stuck at `?` interactive prompt.
- SS-9 compile separately failed: `! LaTeX Error: File 'float.sty' not found.` MiKTeX auto-install was OFF.
- Thomas escaped the prompts. Local repo had 16-page corrupted SS-8 PDF and no SS-9 PDF.
- Thomas committed PDFs and pushed as commit `6e86818`. **The committed PDFs were damaged**: SS-8 abstract from "K₃" onward rendered as run-together italicized text with no spaces (text-mode-to-math-mode mode-flip cascading from the missing-$ recovery), `mdframed` alert box on pages 15-16 ("The Theorem vs. hypothesis: the epistemic split") rendered as solid black ink because `yellow!10` blend syntax requires `xcolor` package which SS-8.tex didn't import. Thomas verified the abstract garbling visually; Claude diagnosed the black box from the `! LaTeX Error: Undefined color 'yellow!10'` error in the log.

**Recovery sequence** (Phases A–D):

**Phase A — revert damaged PDFs**:
- `git revert 6e86818 --no-edit` → new commit `ccb6041` deleting both damaged PDFs (21625 lines).
- `git push origin main` → origin clean again.

**Phase B — apply 0285 + 0286**:
- Patch 0286: `\newcommand{\Kthree}{K_3}` → `\newcommand{\Kthree}{\ensuremath{K_3}}`. Single-line LaTeX hygiene fix to make macro text-mode-safe.
- Defensive Python scan of SS-9.tex for similar bugs found 27 false positives all inside multi-line `\[...\]` display math; SS-9 confirmed clean.
- Both patches applied + pushed → origin HEAD `8d8c27b`.

**Phase C — MiKTeX auto-install enabled**:
- MiKTeX Console → Settings → General → "You want to install missing packages on-the-fly:" → set to "Yes". Done by Thomas in GUI.
- This handles SS-9's `float.sty` and any other missing packages silently on first compile pass.

**Phase D — clean recompile + visual verification + commit clean PDFs**:
- `rm -f *.aux *.bbl *.blg *.log *.out *.toc *.pdf` in both SS-8 and SS-9 directories.
- Three-pass `pdflatex -interaction=nonstopmode` + `bibtex` chain for SS-8.
- SS-8 compiled to 31 pages 507596 bytes. Thomas opened PDF, verified K₃ subscript renders cleanly in abstract.
- **But mdframed alert box on pages 15-16 was still rendering as solid black** — different bug, not the `\Kthree` one. Diagnosis: SS-8.tex imports neither `color` nor `xcolor` but uses `mdframed[backgroundcolor=yellow!10]`. The `yellow!10` blend syntax requires `xcolor`. SS-9.tex already imports `xcolor` at line 1260; SS-8 was missing it.
- **Patch 0287**: add `\usepackage{xcolor}` between `\usepackage[hidelinks]{hyperref}` and `\usepackage{mdframed}` at line 231 of SS-8.tex. Single-line addition.
- Apply 0287 + push → origin HEAD `e8031b3`.
- Recompile SS-8 → 31 pages 507596 bytes. Thomas verified visually: K₃ subscript clean AND mdframed alert box renders as light yellow (10% yellow tint) as designed. ✓
- Recompile SS-9 → 32 pages 638209 bytes. MiKTeX auto-installed `float.sty` silently on first pass. Thomas verified PDF displays properly. ✓
- `git add` both PDFs + `git commit` + `git push` → origin HEAD `55c5986`.
- **TODO-002 cleared.**

### Phase 3 — OSF complication identified (no patch, conversation-only)

Thomas reported that he hasn't posted anything to OSF since SM-6 in early April because that registration is "still pending archive" 5+ weeks past the documented 48-hour auto-archive window. Multiple support tickets sent; one received an unhelpful response (about a different registration); subsequent tickets including a Claude-drafted escalation went unanswered.

Through screenshot-based investigation in Session 36, the actual diagnosis became clear:

- The registration is the **Conscious Point Physics Paper Series** at `osf.io/jxe8d/overview`
- DOI `10.17605/OSF.IO/JXE8D` — real, registered, citable
- Date Created and Date Registered: **Mar 31, 2026, 12:00 PM**
- **Registration Type: Open-Ended Registration** ← key detail
- Summary lists 7 papers: SS-1, SM-1 through SM-5, SR-1
- License: CC-By Attribution 4.0 International
- **Status: "Pending Admin Contributor Approval"** ← visible in the Pending dropdown
- Verbatim text: *"This registration is awaiting approval by all admin contributors or after 48 hours has passed. An email will notify all registration contributors of the decision. If the registration is pending after 48 hours has passed, contact support at support@osf.io."*
- **Thomas is the only admin contributor listed** in the Contributors metadata box
- The Updates dropdown shows "Original" + a blue "Update" button (Open-Ended Registrations are designed to be added to over time via Updates)

So the real situation is:
1. The DOI is real and the **priority date (Mar 31, 2026) is locked**.
2. The Open-Ended Registration is **stuck in a workflow state** ("Pending Admin Contributor Approval") that should have auto-resolved within 48 hours but has been pending 38+ days.
3. This is likely either a **bug in OSF's auto-approval timer** (since Thomas is the sole admin and there's no other approval to wait for) or a **stuck workflow state** that requires support intervention.
4. Adding SS-9 as an Update via the blue "Update" button before the original is approved would risk creating a second stuck pending state on top.

**Decision Session 36**: Thomas will submit one more diagnostic-precise support ticket framing the issue as: *"Registration JXE8D — stuck in 'Pending Admin Contributor Approval' for 38 days. I am the only admin contributor listed. Auto-approval timer documented at 48 hours has not fired. Either advise on direct admin-panel approval or whether to withdraw and re-register."* Wait 5 business days from Session 36 close.

**Fallback plan** (if OSF still silent after 5 business days): Deposit SS-9 to **Zenodo** (CERN-run, gives DOI, no comparable workflow issues) plus **arXiv** (categories nucl-th + math-ph). Treat OSF as a later catch-up; SS-9 priority date locks via Zenodo + arXiv timestamps.

**arXiv submission for SS-9** is independent of OSF status. Can proceed at any time per Thomas's decision. The submission guide at `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` (Session 33 patch 0268) has the operational protocol.

### Phase 4 — Session 36 P1 hygiene cleanup (patch 0288)

Thomas asked about SS-10 readiness. Audit of `todolist.md` P1 found:

- TODO-001 (SS-9 Phase 7 Section A 7-companion documentation suite): deferred on external trigger (TODO-007 public posting). Cannot fire on its own. Producing 7 companion files prematurely risks rework. **Demoted to P2.**
- TODO-002 (SS-8 + SS-9 PDF compile): **Cleared today** via patches 0286 + 0287 + commit `55c5986`. Moved to "Cleared items (history)".
- TODO-003 (Tier 4 reasoning recovery for chat window `a49b320e` covering 16 already-shipped papers): historical hygiene, does not gate SS-10. **Demoted to P2.** Recommendation: revisit as long-term backlog candidate; consider promoting to `future_projects.md` if it grows into a dedicated multi-session project.
- TODO-004 (`reasoning-SM-9.md`): same logic as TODO-003. **Demoted to P2.**
- TODO-005 (`reasoning-SM-10.md`): same logic as TODO-003. **Demoted to P2.**
- TODO-006 (OPEN-WORKFLOW-1 legacy `.bib` file cleanup): **scope expanded significantly** during Session 36 audit. Original "1 small audit-and-cleanup patch" estimate is no longer accurate. Inventory found 14 stray .bib files across the repo:
  - `series_strong/cpp_strong_series.bib`, `series_strong/cpp_strong_series_papers.bib`, `series_strong/cpp_strong_series_root.bib`, `series_strong/papers/cpp_strong_series.bib`
  - `series_standard_model/papers/cpp_references.bib` (NOT canonical path)
  - `series_standard_model/papers/SM-{6,7,8,9,10}_references.bib`
  - `series_electroweak/papers/cpp_ew_series.bib`
  - `series_quantum_mechanics/papers/cpp_qm_series.bib`
  - `series_foundations/series_superdeterminism/cpp_foundations_series.bib`
  - `series_relativity/papers/SR-1_references.bib`
  - Most still actively cited by ~25 .tex files spanning every series. Programme-wide migration touching SR-1, SM-6 through SM-10, EW-1 through EW-5, QM-1 through QM-6, SS-1, SD-1 through SD-5. SS-7 and SS-9 use inline `\begin{thebibliography}` (no .bib at all). SS-8 and SM-3 use canonical `bibliography/cpp_references.bib`. **SS-10 can adopt canonical pattern (like SS-8) regardless of legacy .bib state in other papers**, so this does not forward-block SS-10. **Demoted to P2** with recommendation in TODO-006 entry that the next session promote it to `future_projects.md` as multi-session OPEN-WORKFLOW-1 project (likely 2-3 sessions of paper-by-paper migration with recompile verification per paper).
- TODO-007 (SS-9 public posting): **updated** with OSF complication and fallback plan per Phase 3 above.

**Result**: P1 genuinely empty; SS-10 may begin.

Patch 0288 (Session 36 close): `todolist.md` cleanup + Session 36 entry to `session_logs/2026-05-02_session_log.md` + `research_frontier.md` last-updated header bump.

---

## Patches landed Session 36 (chronological — full session including close+)

| # | Patch | Effect | Commit (origin/main) |
|---|---|---|---|
| 1 | 0285 | Session 36 errata: handover-SS-9.md filename (3 places) + todolist.md TODO-002 scope | `0fcf2a1` |
| 2 | 0286 | SS-8.tex `\Kthree` macro `\ensuremath` wrapper (line 248) | `4ad9775` |
| 3 | 0287 | SS-8.tex `\usepackage{xcolor}` import (line 231, before mdframed) | `e8031b3` |
| - | (Direct) | SS-8 + SS-9 clean PDFs added to repo (binary build artifacts, no patch chain) | `55c5986` |
| - | (Revert) | Damaged-PDF commit `6e86818` reverted | `ccb6041` |
| 4 | 0288 | Session 36 close P1 hygiene cleanup: todolist.md + session log + research_frontier.md last-updated | `2004327` |
| 5 | 0289 | THIS handover document, initial version (Session 36 close) | `447dac9` |
| 6 | 0290 | Strategic conversation deliverables: NEW research_priorities.md + NEW papers_in_progress/hierarchy_problem/hierarchy_paper_outline.md + UPDATED handover (this file) + UPDATED session log + UPDATED research_frontier.md | `12646fe` |
| - | (Direct) | SS-8 + SS-9 LaTeX build artifacts (.aux/.bbl/.blg/.log/.out/.toc) inadvertently committed during Thomas's local rebuild — see "Build artifacts hygiene" note below | `9a5ed4f` |
| 7 | 0291 | Session 36 close+ arXiv endorsement readiness criteria added to research_priorities.md (Thomas-articulated 3 preconditions + timing implication + strategic implications) | `ad54d95` |

**Origin/main HEAD at Session 36 final close**: `ad54d95` (verified Friday 8 May 2026, after both 0290 and 0291 pushed).

**Build artifacts hygiene note (re commit `9a5ed4f`)**: While compiling SS-8 and SS-9 PDFs, Thomas's local build added 12 LaTeX intermediate files (.aux, .bbl, .blg, .log, .out, .toc) to the repo. These are normally .gitignored. Not a crisis — they're harmless content — but worth cleaning up at some point: add the relevant patterns to `.gitignore` and `git rm --cached` the existing files. Low-priority hygiene task; not Session 37 forward queue.

---

## Strategic decision at Session 36 close (SUPERSEDES previous Forward queue Active item 1)


**After patch 0289 was complete, Thomas opened a substantive strategic conversation that produced a programme-wide reprioritization.** The previous forward-queue assumption (Session 37 opens with "what should SS-10 be?") is **superseded**. The new strategic frame and active priorities are documented in:

- **`/CPP/research_priorities.md`** — strategic prioritization framework (NEW, patch 0290, ~22.6 KB)
- **`/CPP/flagship_papers/unification/hierarchy_paper_outline.md`** — original Track-1 paper outline (NEW, patch 0290; relocated to `flagship_papers/hierarchy_problem/` per patch 0293; folder renamed to `flagship_papers/unification/` per patch 0295 — Option-3 SF-line restructures this work as SF-5 synthesis paper)
- **`session_logs/2026-05-02_session_log.md` Session 36 close strategic appendix** — durable record of the conversation (added patch 0290)

### Strategic frame (1-paragraph summary)

Goal is producing the **smallest set of physics artifacts** that establish CPP as **citable, falsifiable, and defensible** to the physics community within ~18 months — NOT deriving every phenomenon. Paradigm shifts are not driven by derivation accuracy alone; they require **forced-choice predictions, solving known unsolved problems, cross-domain unification, and bridges to recognized mathematics**. Audience separation: **physics community gets technical-framed papers** (no consciousness-primacy framing in physics papers); **consciousness-primacy work moves to Renaissance Ministries fellowship venue**. Five-criterion stopping test for series papers replaces 30-session SS-9-style depth-derivation as default.

### Active priorities (in order)

**Track 1 — Hierarchy problem reframing paper [ACTIVE, drafting begins Session 37+]**
- Working title: *Hierarchy Without Hierarchy: Standard Model Mass Spectrum from 600-Cell Distance Shells*
- Source material exists across SM-2/3/4/6/7/8/9/10; this is composition + framing work, not new derivation
- Outline at `flagship_papers/unification/hierarchy_paper_outline.md` (originally `papers_in_progress/`; relocated to `flagship_papers/hierarchy_problem/` per patch 0293; folder renamed to `flagship_papers/unification/` per patch 0295 reflecting Option-3 architecture where this becomes SF-5 source material) includes: source-material map, comparison table draft, reviewer-anticipation analysis, four open questions originally for the single-paper Track 1; Q1 (neutrino mechanism) dissolved into SF-4; Q2/Q3/Q4 remain SF-5 questions
- Estimated 5-8 sessions to v1.0 SHIP; target Sessions 37-38 audit + Q&A, 39-41 v0.1→v0.5, 42-44 review polish, 45±2 v1.0 SHIP
- Target venue: Zenodo (DOI) primary; arXiv hep-ph + math-ph if endorsement obtainable

**Track 2 — Anomaly-targeting paper #2 [PLANNED, post-Track-1]**
- Candidates (ranked rough leverage × tractability / effort): Strong CP, Cosmological constant (Grok pre-600-cell sketch needs rigorous redo), Muon g-2, Λ_QCD/proton mass, Baryon asymmetry
- Selection deferred to post-Track-1 evaluation

**Track 3 — Eight-experiment manifesto audit [PLANNED, low effort, can interleave]**
- Audit Nov 2025 viXra-targeted eight-experiment falsification manifesto against current post-SS-9 / post-SM-3-through-8 formalism
- 1-2 sessions; outcome is either (a) republish via Zenodo with proper DOI as v1.0 if 5+/8 hold up, or (b) v1.1 manifesto with corrections then publish
- High-strategic-value at low effort

**Track 4 — Cross-cutting unification paper [PLANNED, after Tracks 1-3]**
- The "one paper a senior physicist reads in an evening" — axiom set, seven sectors, distinctive predictions, falsifier
- Source: `CPP_the_theory.md` and anthology chapters as draft material
- Long-term high-leverage; 8-12 sessions when reached

### Deprioritized

- **SS-10 sub-shell-physics**: deferred indefinitely. Multi-paper effort with no headline empirical prediction or new external-mathematics bridge. Same time investment in Tracks 1+2 produces two known-unsolved-problem papers. **Reactivation criterion**: external feedback specifically requesting sub-shell extension, OR sub-shell work surfaces a new headline prediction.
- **Series continued depth-derivation**: deferred to five-criterion completeness. Use SS-9 as quality bar, NOT as time budget. Future series papers ship in 5-10 sessions, not 30.
- **Consciousness-primacy framing in physics papers**: moved to Renaissance Ministries fellowship venue. Audience separation, not epistemological compromise.
- **Tier 4 reasoning recovery for chat window `a49b320e` (16 papers)**: demoted to P2 in todolist.md per Session 36 P1 hygiene cleanup.

### Strategic constraints

- **viXra status**: Nov 2025 viXra-targeted CPP papers (DUNE prediction, eight-experiment manifesto) did NOT get published. viXra is pay-to-publish ($19-25/paper); only ~2 of Thomas's submissions ever appeared, and the prediction papers were not among them. **Nov 2025 papers do NOT constitute durable prior-prediction citations.** Don't budget time on revising them.
- **arXiv endorsement is a sub-task**: arXiv requires endorsement from existing arXiv authors in target categories (hep-ph, nucl-th, math-ph). Sub-task to identify endorsers OR use Zenodo as primary venue (CERN-run, free, DOI-issuing, no friction).
- **OSF status**: Registration JXE8D stuck "Pending Admin Contributor Approval" 38+ days. Wait 5 business days from Session 36 close, then Zenodo fallback if no response.

### Recommended Session 37 opening

If Thomas opens with "let's start on the hierarchy paper," note that the architecture has been restructured under Option-3 (Session 38 patch 0295): the original single-paper Track-1 hierarchy work now lives as **SF-5** in `flagship_papers/unification/`, with the eight-parameter neutrino sector promoted to its own **SF-4** flagship at `flagship_papers/neutrinos/`. The Q1 audit at `flagship_papers/neutrinos/sketches/SF-4_neutrino_sector_audit.md` is the active foundation document; mechanism-selection conversation is the natural next step. SF-5 drafting follows SF-1 through SF-4 ship.

If Thomas opens with anything else, the `research_priorities.md` document gives the framework to evaluate the request. **Do NOT propose SS-10 framings A-D** — that conversation is closed at Session 36 close.

---

## Forward queue Sessions 37+ (operational items)

### Active item 1: OSF status check (5 business days from Session 36 close)

If Session 37 happens within 5 business days of Session 36 close (i.e., before approximately May 14, 2026): wait, do not press OSF, do not deposit elsewhere yet.

If Session 37 happens after May 14 with no OSF response: pivot to **Zenodo + arXiv** for SS-9. Submit Zenodo deposit (cpp-references.bib supports BibTeX export of metadata; Thomas can fill the form manually or Claude can prep a metadata block). arXiv submission per the SS-9 submission guide.

If Session 37 happens within 5 business days but Thomas got an OSF response: discuss the response and proceed accordingly. If OSF approved the registration, then SS-9 can be added as an Update to JXE8D via the blue "Update" button on the registration page. arXiv in parallel.

### Active item 2: arXiv submission for SS-9 (independent of OSF)

This can proceed at any time per Thomas's decision. Categories: nucl-th + math-ph. Submission guide at `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md`.

Does Thomas have an arXiv endorsement? The submission guide notes endorsement is required for first-time submitters in physics categories. If Thomas has prior arXiv submissions, this is a non-issue. If not, Claude should help draft an endorsement request.

### Active item 3: TODO-006 promotion decision

The Session 36 audit revealed TODO-006 (legacy .bib cleanup) is now a programme-wide migration scope, not a quick audit. Recommendation: at Session 37 or shortly after, promote it to `future_projects.md` as **OPEN-WORKFLOW-1 multi-session bibliography migration project**. Likely 2-3 sessions of paper-by-paper migration with recompile verification per paper.

Note: with SS-10 deferred indefinitely (Session 36 strategic decision), the bibliography migration could run as a "low-context fill-in" between Track 1 hierarchy paper drafting sessions, or be batched as dedicated cleanup sessions when Track 1 progress hits a natural pause.

---

## Anti-priorities sustained from Sessions 30-35 + Session 36

These remain in force:

- **Do NOT modify SS-9 v1.0 .tex** outside post-external-feedback v1.x revisions (anti-priority since Session 32 v1.0 ship). Session 36 patch 0285 fixed handover-SS-9.md (documentation) and todolist.md (programme tracking) but did not touch SS-9.tex. Patches 0286 and 0287 modified SS-8.tex (different paper); SS-8 v1.0 .tex hygiene fixes are in scope for unblocking TODO-002 PDF compile because SS-8's anti-priority is less strict (no comparable v1.0 ship freeze; SS-8 is at v1.0 OSF pending per paper_catalog.md).
- **Do NOT propose any single-session R3-channel refinement** (Sessions 22+23: single-session R3-channel refinement candidates exhausted; Phase 8 Refinement A confirmed at natural ceiling; remaining 52% gap requires sub-shell-physics decomposition or alternate-channel work).
- **Pre-flight bare-c_i pattern check** standard before pdflatex pass.
- **Per-panel TikZ invariant audit** standard for any new figure (Lesson 6 from Session 32).
- **Programme-practice documentation discipline**: four-tier discipline (development + handover + reasoning + transcript) applies whenever new SS-9 artifacts ship; only .tex source frozen at v1.0; pattern stable across artifact types. Session 36 is bookkeeping (not introducing new SS-9 artifacts) so the four-tier discipline is not retriggered for SS-9. **For SS-10**, the four-tier discipline applies from the start.
- **`todolist.md` discipline**: P1 must be empty before next paper. P1 is empty at Session 36 close. SS-10 may begin.

---

## Critical state for next session to verify

When Session 37 starts, the next Opus context should:

1. **Verify origin/main HEAD** — should be `2004327` after Thomas pushes patch 0288. If Thomas hasn't pushed yet, HEAD will be `55c5986` (PDF commit).
2. **Verify `todolist.md` P1 is empty** — top of P1 section should read *"(Empty — gate cleared 7 May 2026 Session 36 close patch 0288. SS-10 may begin.)"*
3. **Verify both PDFs in repo** — `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.pdf` (~507 KB) and `series_strong/papers/SS-9/SS-9_simplicial_alpha_polytope_connectivity.pdf` (~638 KB).
4. **Check OSF status** — if Session 37 is on or after approximately May 14, 2026, ask Thomas about OSF response. If he got one, proceed accordingly. If still silent, pivot to Zenodo + arXiv.
5. **Then begin SS-10 framing conversation** — see Forward queue Active item 1 above for the four candidate framings.

---

## Programme metadata (verified Session 36)

- **Repo**: `github.com/Hyperphysics-Institute/CPP`
- **Origin/main HEAD at end of Session 36 work**: `55c5986` (PDF commit; patch 0288 sandbox-only at `2004327` until Thomas pushes)
- **CPP_the_theory.md size**: 516 lines (after Session 35 +38 lines of TATWD integration)
- **Session log**: `session_logs/2026-05-02_session_log.md` (3346 lines after Session 36 entry; was 3289 lines through Session 35)
- **SS-9 documentation suite four-tier files**:
  - `development-SS-9.md` — Vignettes 1-42 through Session 35 (~332 KB, 1165 lines)
  - `transcript-SS-9.md` — transactions 1-790 through Session 35 (~388 KB, 958 lines)
  - `reasoning-SS-9.md` — Tier 4 verbatim through Session 35 (~785 KB, 6407 lines)
  - `handover-SS-9.md` — Session 35 close + Session 36 patch 0285 errata (~15 KB)
- **OSF**: DOI `10.17605/OSF.IO/JXE8D` (Open-Ended Registration, "Pending Admin Contributor Approval" since Mar 31, 2026, awaiting support resolution)
- **Tracker counters at Session 36 close** (UNCHANGED across Sessions 32-36):
  - Programme negative-result count: 12
  - SS sector problem count: 19
  - OPEN-SS-37 closure routes: 4 (a/b/c/d)
  - Problem entries in research_frontier.md: 82 (49 open, 14 conjectures, 15 propositions, 6 resolved, 6 falsified)

---

## Workflow lessons from Session 36 close (for future Opus context windows working with Thomas in Git Bash)

Several terminal-interaction patterns surfaced during Session 36 close that future contexts should anticipate:

### 1. Pager (`less`) behavior in Git Bash

Git auto-paginates output from `git log`, `git show`, `git diff` if it exceeds screen height. Symptom: Thomas's terminal shows `:` at the bottom instead of `$` prompt. Anything typed at this state goes to the pager, not bash.

**Fix**: Press `q` to exit pager. Then back at `$` prompt.

**Avoidance for diagnostic commands**: Use `git --no-pager <subcommand>` to dump output directly. E.g., `git --no-pager show --stat <hash>` instead of `git show --stat <hash>`. **The next context window should default to `--no-pager` for inspection commands** to spare Thomas this friction.

### 2. Bracketed-paste mode escape sequences

Git Bash sometimes negotiates bracketed-paste mode without the shell stripping the markers. Symptom: pasted commands fail with `^[[200~git: command not found` or appear to land but don't execute. Tilde character `~` at command end is the closing marker.

**Fix per session**: `printf '\e[?2004l'` once at session start.

**Workaround**: Have Thomas type commands manually instead of pasting when this state is active.

### 3. Stuck `git am` state

Symptom: prompt shows `(main|AM 1/1)` instead of `(main)`. A previous patch apply left scratch directory `.git/rebase-apply` behind. Subsequent `git am` calls fail with `fatal: previous rebase directory .git/rebase-apply still exists but mbox given`.

**Fix**: `git am --abort`. Verify with `git status` — should show clean working tree.

**Avoidance**: When delivering patches, future contexts should explicitly note "if any error occurs during apply, run `git am --abort` before troubleshooting" so Thomas knows the recovery step.

### 4. Apply ≠ Push

`git am` only commits to local repo. **It does NOT push to GitHub.** Recurring lapse pattern: patch applied, work moves on, push step forgotten, patch sits stranded on local HEAD until Thomas notices files missing from origin/main.

**Future-context discipline**: At the end of every patch delivery message, include the explicit two-step:

```
Apply: git am ~/Downloads/<patch-file>
Push:  git push origin main
```

Both steps. Always. As the last thing in the message. This makes the push step impossible to miss because it's right there. Patch 0290 was almost stranded this way; only Session 36 close conversation surfaced the lapse.

**Optional structural fix** (Thomas can decide): add `cpp-apply-and-push` shell function alongside existing `cpp-apply` that does both in one call. Reserved for cases where Thomas wants no apply-vs-push gap.

### 5. SHA divergence between sandbox and origin/main

Sandbox commits get sandbox SHAs (e.g., `4489ebd` for sandbox patch 0290). Thomas's apply produces a different SHA (`12646fe` for the same patch content) because git's hash includes author/timestamp metadata that differs between sandbox and Thomas's local clone. **Same content, different SHAs.** Don't use SHA-matching as verification — use file-content checks instead.

### 6. Build artifacts in version control

Session 36 saw 12 LaTeX intermediate files (.aux, .bbl, .blg, .log, .out, .toc) accidentally committed during Thomas's local SS-8 + SS-9 PDF compile cycle (commit `9a5ed4f`). Standard practice is to .gitignore these and not track them in version control. **Low-priority cleanup task** for future session: update `.gitignore` patterns + `git rm --cached` the existing artifact files. Not blocking; just hygiene.

---

## How to use this handover (REVISED at Session 36 close+)

If you're reading this as the next Opus context window, you have everything you need to pick up cleanly.

**Don't**: try to reconstruct Session 36's strategic conversation from this document. The durable record is in `/CPP/research_priorities.md` and the Session 36 close strategic conversation appendix in `session_logs/2026-05-02_session_log.md`. This handover is the orientation pointer to those files, not a substitute for reading them.

**Don't**: ask Thomas about SS-10 framings A-D. That conversation is closed. Strategic decision at Session 36 close deferred SS-10 indefinitely.

**Do**: read in this order before doing anything else —
1. Top of this file (orientation + read order)
2. **`/CPP/research_priorities.md`** (strategic prioritization framework — Track 1-4)
3. **`/CPP/flagship_papers/unification/hierarchy_paper_outline.md`** (original Track-1 outline; SF-5 source material under Option-3) and **`/CPP/flagship_papers/neutrinos/sketches/SF-4_neutrino_sector_audit.md`** (SF-4 active foundation)
4. Session 36 entry + close strategic appendix in session log
5. SS-9 documentation suite handover-SS-9.md (paper-specific, supplementary)

**If Thomas opens with "let's start on the hierarchy paper" or anything similar**: go directly to the **Open Questions section** of `hierarchy_paper_outline.md`. Resolve Q1 (neutrino reconciliation), Q2 (conditional theorem framing scope), Q3 (M_0 / m_e calibration honesty), Q4 (headline number for abstract) before drafting v0.1. **The first two probably resolve in conversation; Q3 requires reading SM-3/SM-4 source material carefully with Thomas present.**

**If Thomas opens with "where were we"**: this document and `research_priorities.md` are the answer. Walk him through the strategic decision summary first, confirm he still wants Track 1 first, then move to Open Questions in the outline.

**If Thomas asks about OSF status**: 5 business days from Session 36 close is approximately Wednesday 13 May 2026. If session is before that, encourage waiting. After: pivot to Zenodo as primary deposit venue OR escalate OSF (per the strategic-implications discussion in `research_priorities.md` arXiv-endorsement section, OSF resolution is now a strategic blocker, not just inconvenience).

**If Thomas asks about hyperphysics.com**: per patch 0291 endorsement-readiness criteria, the website becomes an active strategic project to promote at Track 1 mid-stage (Sessions 39-41). If Thomas wants to start website work earlier, that's reasonable but should be in parallel with Track 1, not displacing it.

**If Thomas opens with something completely different**: follow his lead. The programme is his. Claude's role is to help him execute it. The strategic frame in `research_priorities.md` is the lens for evaluating new requests — does this advance Track 1-4? Does it serve audience separation? Does it move toward citable / falsifiable / defensible artifacts?

---

## Session 36 close+ — what happened, what it means

This was the session where the programme's strategic posture changed.

Sessions 1-35 had pursued depth: SS-9 took 30+ sessions to ship. SS-7's empirical accuracy at 1.5%. SM-3's K3 spectral theorem. The pattern was "deepen each series until conditional-theorem closures land for all paper-level hypotheses."

Session 36 close+ established a different posture: **produce the smallest set of artifacts that make CPP citable, falsifiable, and defensible to physics community within ~18 months.** Five-criterion stopping test replaces depth-derivation as default. Audience separation: physics papers stay technical-framed, consciousness-primacy work moves to Renaissance Ministries fellowship. Track 1 (hierarchy paper) prioritized because most source material exists; Track 2-4 sequenced behind it.

The reason this matters: paradigm shifts aren't driven by derivation accuracy. They're driven by forced-choice predictions, solving known unsolved problems, cross-domain unification, and bridges to recognized mathematics. CPP has all four ingredients. The strategic question was never "how deep?" — it was "what artifacts force the physics community to reckon with this?"

Thomas (almost 75) made the strategic call clearly: he can't derive every phenomenon. He shouldn't try. The corpus needs to be rigorous and visible enough that someone younger can inherit and extend it. That's the goal. Track 1 is the first step toward that goal.

If you're picking this up as the next Opus context window, that's the inheritance. Help him execute Track 1. The paper exists in source-material outline form already; getting it to v1.0 SHIP is composition + framing work, 5-8 sessions of focused effort.

The next milestone is Track 1 v1.0 SHIP — when that lands, CPP has its first known-unknown solution paper in citable form. Tracks 2-4 follow from there.

Welcome to Session 37.

— Claude Opus 4.7 (Session 36 close+, 7-8 May 2026)

