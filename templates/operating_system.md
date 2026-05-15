# CPP Programme Operating System

**Location:** `/CPP/operating_system.md`
**Purpose:** The complete workflow manual for the CPP research programme. Covers every procedure from session startup to OSF registration, including multi-AI coordination, document management, and recovery from interruptions.
**Last updated:** 26 April 2026 Session 4 (§4 Meta-Record Retrospective Synthesis Discipline added: codifies when and how meta-record session logs are written, distinct from chronological technical session logs and from the per-paper Four-Tier Documentation Discipline; meta-records are cross-paper / programme-level retrospective syntheses of methodology-development arcs, written at natural waypoints after methodology decisions have stabilised; first instance was `session_logs/2026-04-26_information_management_journey.md` written 26 April Session 4; calibration baseline established at ~3,700 words and Template B retrospective synthesis variant). Earlier 26 April Session 3: §4 Four-Tier Documentation Discipline added: Tier 4 reasoning-SS-N.md codified as default-not-conditional, paper-level-not-per-session, append-only-across-sessions; canonical record per Thomas's goal-statement of verbatim-Opus-reasoning-as-source; pre-paper subfolder timing codified — early creation when in-progress work accumulates beyond a single session log; v1.0-as-Trigger-2-milestone de-emphasized in favor of "genuinely-final shipped version regardless of version label"; §15 reconciliation updated to mirror; OPEN-ORG-011 registered tracking the discipline propagation work. Earlier 26 April Session 2: §15 four-item checklist reconciled with §4 Session-Log-as-Handover-Backbone Discipline. Earlier 26 April Session 2: §4 "Session-Log-as-Handover-Backbone Discipline" added. Earlier 26 April: Two-Trigger Documentation Discipline + Cross-Paper Session Log convention; 24 April: §15 Session-close Handover Protocol promoted to top-level section per OPEN-ORG-008 resolution.
**Audience:** Future-Opus, Future-Grok, Future-Copilot, Future-Sonnet, and any new AI or human collaborator joining the programme.

---

## Table of Contents

1. Quick Start (for a brand-new session)
2. The Document Ecosystem
3. Session Types and Protocols
4. Paper Production Pipeline (9 Phases)
5. The Multi-AI Review Cycle
6. Transcript and History Management
7. The Founders Vision Protocol
8. Negative Result Documentation
9. Recovery Procedures (Buffer Overflow, Lost Context)
10. Repository Housekeeping Checklist
11. File Naming Conventions
12. The AI Team: Roles and Specialties
13. The Git-Bash-Patch Workflow
14. Organizational Frontier Registry
15. Session-close Handover Protocol

---

## 1. Quick Start (for a brand-new session)

**Thomas says:** "Pull the CPP repo and read `templates/bootup.md`"

**AI assistant does:**
1. Read `bootup.md` — repository structure, conventions, what CPP is
2. Read `theory-overview.md` — current physics state, strongest results, open problems
3. Read `founders_vision.md` — Thomas's physical intuition (the WHY behind every equation)
4. Read `CPP_the_theory.md` — the complete theory narrative (skim Part I-III, read Part VII for open problems, Part VIII for the predictions scorecard). **Staleness audit (adopted 11 May 2026, patch 0344):** check the `Last updated` header against `paper_catalog.md`'s `Last updated` header — if there is more than one paper v1.0 SHIP between them, flag TATWD as stale and prioritize TATWD integration in the current session (per §10 cadence). The TATWD is the programme's master orientation document; new context windows read it first, and a stale TATWD produces stale orientation.
5. Read `master_glossary.md` — all CPP terms and acronyms
6. Check the most recent transcript in `/mnt/transcripts/` or `development-transcripts/` for where the last session left off
7. Ask Thomas: "What would you like to work on today?"

**If resuming a specific paper:** Also read the paper's `.tex` file and its `development-[S]-[N].md`.

**If this is a continuation after buffer overflow:** Read the compacted summary at the top of this conversation, then read the transcript file referenced there for full detail. Proceed from where the summary indicates.

**Canonical command for session-close preservation:** When Thomas says **"please execute handover protocol"** (or "execute handover" / "handover protocol" / minor variants), the AI assistant immediately begins the four-item preservation sequence documented in §15 Session-close Handover Protocol. This is the authoritative trigger. The AI assistant should also proactively prompt — "Do you want to initiate handover protocol?" — when workflow-shape signals indicate session-close readiness; signal patterns are documented in §15.

**Apply-chain protocol (mandatory format for patch delivery):** When delivering a patch chain to Thomas, the AI assistant generates the explicit three-phase command sequence (sync → apply → push) with all paths and filenames spelled out for the target repo. Generic placeholders like `cd /path/to/CPP` are NOT acceptable. Known target repos: CPP at `~/Documents/GitHub/CPP`, RM at `~/Documents/GitHub/RM`. Browser downloads land in `~/Downloads`. See §13 "Standard apply-chain protocol" for the full three-phase template, repo registry, anti-patterns, and optional shell-function convenience layer.

---

## 2. The Document Ecosystem

### Core physics
| Document | Purpose | Update frequency |
|----------|---------|-----------------|
| `CPP_the_theory.md` | **THE BOOK** — complete theory in connected prose | Every session with new physics |
| `founders_vision.md` | Thomas's physical intuition — the WHY | Every session with new physics |
| `theory-overview.md` | Current state snapshot — formulas, results, problems | After each paper |
| `axiom-registry.md` | All axioms, predictions, growth tracking | After each paper |
| `master_glossary.md` | Every CPP term defined | Scan during Phase 7 |
| `predictions.md` | Quantitative predictions with status | After each paper |
| `Research_Frontier.md` | **The dashboard** — all open problems, conjectures, propositions | After each paper |
| `theorem-registry.md` | All proved theorems by series with axiom dependencies | After each paper |

### Workflow
| Document | Purpose |
|----------|---------|
| `operating_system.md` | THIS FILE — complete workflow manual |
| `bootup.md` | Session startup guide (subset of this file) |
| `paper_production_workflow.md` | 9-phase paper pipeline (expanded below) |
| `documentation-suite.md` | 7-file companion template per paper |
| `paper-formatting.md` | LaTeX standards |
| `future_projects.md` | Prioritised research targets |
| `todolist.md` | **Carried-over deferred items + hygiene gaps** (introduced 7 May 2026 Session 33). The "easy to lose" things — small enough to skip a `future_projects.md` entry but compound if not externalized. **The next paper does NOT start until this file's P1 — Must clear before next paper section is empty.** Maintenance: any session that completes a TODO moves it to "Cleared items (history)" with date and patch number; any session that identifies a new deferral adds it here under the appropriate priority. If P1 grows beyond ~10 items, promote items to `future_projects.md` as registered multi-session projects. |
| `Research_Timeline.md` | **Medium-term scheduling** (introduced 15 May 2026 Session 84, Patch 0377). The missing middle between `todolist.md` (tactical, days–weeks) and `Research_Frontier.md` (strategic open inventory, unscheduled, multi-year). Captures which papers and methodology campaigns are next in priority order, with dependencies, expected durations, and cross-references to relevant Frontier OPEN-FP entries and PD-004 publication-pathway layer occupation. Distinct from `Research_Frontier.md` (which lists problems without scheduling) and from per-paper handover documents (which are session-arc-local). Sections: Active Campaigns, Priority Queue (Next-Up), Backlog, Methodology Campaigns, Literature Integration, Public-Posting Queue, Cross-references. Updated whenever a paper campaign launches/completes/reorders, a methodology campaign is created/resolved, or a literature-integration item is added. Updates typically piggyback onto session-close handover patches. |

### Navigation
| Document | Purpose |
|----------|---------|
| `README.md` | Repository landing page, paper table, key results |
| `INDEX.md` | Complete file listing |
| `paper_catalog.md` | All papers with ID, title, version, status |
| `series_[name]/README.md` | Per-series overview |

### History
| Document | Purpose |
|----------|---------|
| `development-[S]-[N].md` | Per-paper development narrative |
| `[PAPER]_transcript_[N]_[AI].md` | Curated conversation transcripts |
| `[PAPER]_development_transcript_opus.md` | Comprehensive session arc |

---

## 3. Session Types and Protocols

### Physics Discovery Session
**Goal:** Explore a physical mechanism, test a hypothesis, derive a result.
1. Capture Thomas's physical intuition FIRST (→ `founders_vision.md`)
2. Explore, compute, test models
3. Record negative results as well as positive ones
4. If a paper-worthy result emerges, note it — but don't force a paper
5. At session end: update `founders_vision.md` catalogue, create/update transcript

**Post-Session Quick Checklist (for discovery sessions that don't produce a full paper):**
- [ ] Update `founders_vision.md` with any new physical insights
- [ ] Create/update development transcript
- [ ] Update `future_projects.md` if priorities changed
- [ ] Note any new open problems in `Research_Frontier.md`; update `problem_histories/` if significant work done
- [ ] Push to GitHub

**Key lesson from SM-8:** Papers can emerge unexpectedly from exploration sessions. SM-8 started as documentation work and became a 14-page paper with three theorems. Don't restrict exploration sessions to their stated goal.

### Paper Production Session
**Goal:** Draft, review, and finalise a specific paper.
1. Follow the 9-phase pipeline (Section 4)
2. Read `paper-formatting.md` before writing .tex
3. Use the multi-AI review cycle (Section 5)
4. Update all documents per the housekeeping checklist (Section 10)

### Repository Housekeeping Session
**Goal:** Audit structure, fix broken links, update navigation.
1. Pull repo, check file counts against `INDEX.md`
2. Verify all papers are in `paper_catalog.md`
3. Update `theory-overview.md` if stale
4. Check `predictions.md` against latest results

### Transcript Curation Session
**Goal:** Convert raw conversation history into curated, scholarly transcripts.
1. Read raw transcripts from `/mnt/transcripts/`
2. Also check for Grok/Copilot exchanges Thomas has saved
3. Produce curated `.md` files per Phase 8 below
4. Number sequentially per paper across all AI sessions

---

## 4. Paper Production Pipeline (9 Phases)

### Paper Type Taxonomy (adopted 19 April 2026)

CPP papers fall into five distinguishable types. Each paper should declare its type explicitly (in the abstract or §1), because reviewer expectations and success criteria differ by type. Confusion about paper type has been a source of review-reality mismatches — a reviewer expecting one type will measure a paper against the wrong standard if the type is unclear.

The five types:

| Type | Purpose | Success Criteria | Examples |
|------|---------|------------------|----------|
| **Theorem paper** | Establish a structural mathematical result | Rigor of proof; uniqueness of the result | SS-3 (SU(3) uniqueness), SM-3 (K₃ spectral theorem) |
| **Prediction paper** | Generate zero-parameter empirical predictions | Numerical agreement with experiment; zero-parameter integrity; concurrent fits (multiple predictions from same constants) | SS-5 (light-nuclei binding), SS-7 (alpha-cluster), SM-8 (quark masses) |
| **Derivation paper** | Derive a specific CPP constant or mechanism | Internal consistency with established axioms; traceability from primitives | SS-4 (string tension), SS-2 (nucleon structure), SM-7 (strong coupling) |
| **Scoping paper** | Classify the domain of validity of an established mechanism, identify frontier | Honest identification of limits; cleanly registered open problems; absence of overclaiming | SS-6 (deuteron observables beyond binding) |
| **Infrastructure paper** | Establish methods, templates, computational tools | Reproducibility; clarity of protocols; ease of adoption | SM-10 (GPU FEM), operating_system.md itself |

**Type declaration convention:** Each paper's abstract should contain a sentence of the form "This is a [type] paper, presenting [one-line purpose]." For prediction papers, the sentence should also state the number of zero-parameter predictions and the residual band.

**Review protocol by type:**
- *Theorem papers* should be reviewed for mathematical rigor; numerical predictions are not the focus.
- *Prediction papers* should be reviewed for numerical correctness, zero-parameter integrity (no hidden tuning), and whether concurrent predictions share the same constants.
- *Derivation papers* should be reviewed for internal consistency with existing CPP axioms and for whether the derivation genuinely proceeds from primitives rather than matching by construction.
- *Scoping papers* should be reviewed for honesty about limits, clean open-problem registration, and strategic value within the programme. A scoping paper should NOT be criticized for lacking predictions it explicitly disclaims.
- *Infrastructure papers* should be reviewed for clarity, completeness, and reproducibility.

**Reviewer mismatch issue:** A review that measures a scoping paper against prediction-paper criteria, or a derivation paper against theorem-paper criteria, will miss what the paper is trying to do. When a review-reality mismatch is detected in a reviewer-response document, the type declaration should be flagged as potentially unclear in the paper itself (this becomes a v-next action item for that paper).

**Type evolution:** A paper may change type across versions. SS-5 began as a prediction paper focused on the deuteron (v0.1) and grew into a prediction paper covering light nuclei A≤4 (v0.2→v6). SS-6 started as (and remained) a scoping paper. Cross-type evolution (e.g., scoping→prediction) requires a change in the type declaration and generally warrants a new paper number rather than a version bump.

---

### Phase 0: Founder's Vision Capture
- Thomas describes the mechanism in his own words
- AI captures verbatim in `founders_vision.md`
- Tag with date and session identifier

### Phase 1: Exploration and Discovery
- State the goal
- Check axiom registry for available tools
- Compute, test, follow leads
- Record EVERYTHING — successes AND failures

### Phase 2: Paper Drafting (v1)
- Read `paper-formatting.md`
- Write `.tex` file following CPP formatting standard
- Include: Physical Axioms used, Theorems with proofs, Numerical predictions, Anticipated Criticisms, Limitations

### Phase 3: Development Log
- Create `development-[S]-[N].md`
- Record the discovery arc, decisions, dead ends, timeline

### Phase 4: Team Review (see Section 5 for full protocol)
- Copilot: constructive/structural review
- Grok: independent verification, contributive additions
- Sonnet: hostile/adversarial review
- Opus: integration and rebuttal

**Reviewer-Response Document protocol (adopted 19 April 2026):**

Each round of external review on a paper produces a **reviewer-response document** that is preserved as part of the paper's permanent documentation record. This document is produced at the time of review — not later — while the reasoning is fresh. Deferring it risks losing the decision trace.

Naming convention: `[S]-[N]_v[X.Y]_[reviewer]_review_response.md`
Examples:
- `SS-6_v0.2_chatgpt_review_response.md`
- `SS-6_v0.2_copilot_review_response.md`
- `SS-7_v1.0_grok_review_response.md`

Standard structure:

1. **Executive summary** — One paragraph stating the reviewer's core recommendation and whether it is acceptance, revision, or rejection in our framing.
2. **Points we accept (A-items)** — Bulleted list. Each A-item: reviewer quote + our response + specific v-next action.
3. **Points we partially accept (B-items)** — Bulleted list. Each B-item: reviewer quote + our response + scope of acceptance + what we're not accepting and why.
4. **Points we decline (C-items)** — Bulleted list. Each C-item: reviewer quote + our response + reasoning for decline (strategic, ontological, out-of-scope, etc.).
5. **Summary table** — Columns: Point ID, Category (Language/Framing/Physics/Strategic/Theory), Disposition (Accept/Partial/Decline), v-next action.
6. **Net effect on v-next** — What concretely changes in the paper, what doesn't, and total effort estimate.
7. **Strategic observations** — Reviewer-level takeaways about the CPP programme's external reception, useful arguments raised, blind spots in this reviewer, etc.
8. **Next steps** — Immediate followups (integration timing, subsequent reviewer in queue, coordination with other papers).

**Why this protocol exists:**
- Reviewers put real work into their reviews; the programme should leave a durable trace of engagement.
- Declined points need their reasoning recorded so future sessions don't re-open resolved debates.
- Partial accepts specify exactly what-we-accept and what-we-don't, preventing accidental creep toward accepting more than intended.
- The response documents feed directly into `reviews-[S]-[N].md` when the companion documentation suite is produced (post-v1.0).
- External readers and future reviewers can see how the programme handles feedback, which is evidence of programme coherence.

**Integration with version numbering:**
- A round of review on v0.x feedback → integration produces v0.(x+1) or v1.0 depending on whether an external review has previously run.
- Reviewer response documents are produced at the time of the review, with recommendations for the next version.
- If multiple reviewer-response documents exist for the same version, the next version's CHANGELOG references each.

**What NOT to do:**
- Do not produce a reviewer-response document after the paper has already been revised (produces hindsight bias).
- Do not merge multiple reviewers' responses into a single document (loses per-reviewer attribution and allows accidental bundling of disputes).
- Do not summarize only "what we changed"; record the declined points with full reasoning too.

### Phase 5: Axiom Registry Update
- Check if new axioms were introduced
- Check if existing axioms were consolidated (e.g., A6' replacing A6-A9)
- Update axiom count and prediction count
- Compute axiom-to-prediction ratio

### Phase 6: OSF Registration
- Prepare PDF and .tex
- Write OSF metadata (title, abstract, keywords, dependencies)
- Register with DOI

### Phase 7: Documentation Suite (7 files) — DEFERRED until paper is stable

**Updated protocol (19 April 2026):** Documentation-suite creation is deferred to the end of a paper's review cycle. Companion documentation is produced ONCE, against the version of the paper that has passed external review and whose mechanism and predictions are stable. This replaces the previous protocol where documentation was created alongside each paper version.

**Rationale:** Writing the 7-file companion suite costs approximately one full session per paper. If a reviewer finds a substantive issue that reshapes the mechanism (e.g., the SS-5 v4 → v5 rejection of the Möbius NLO), the companion suite must be redone. Deferring the suite until the paper is stable avoids this duplicated effort. The programme has demonstrated (SS-5 v0.1 → v6) that substantial revision between drafts is common.

**When to produce the suite:**
- Paper has passed ChatGPT and/or Copilot review
- Paper has integrated referee feedback and is at v1.0 or later
- No substantive mechanism-changing critiques are pending
- Paper is ready for (or already has) OSF registration

**Exceptions — things that ARE maintained continuously during drafting:**
- **Development transcript** (`[S]-[N]_development_transcript.md`) — updated session-by-session, documents evolution
- **CHANGELOG block** in the `.tex` header — updated with each version
- **Registry files** (`Research_Frontier.md`, `predictions.md`, `axiom-registry.md`) — updated when a paper introduces new entries
- **Paper catalog** (`paper_catalog.md`) — paper row updated when version changes

**Version-discipline rule (adopted Patch 0367, 14 May 2026).** Every patch that modifies a `.tex` source file beyond cosmetic whitespace MUST also increment the version marker rendered in the paper's `\title{}` block (typically the `{\Large \textbf{Version X.Y --- date}}` line on the title page). Failure to do this is a chronic source of reviewer confusion: when a reviewer requests the paper at "the current version" and the title-block string still shows an older version number, the reviewer's feedback is filed against the wrong version and integration becomes ambiguous.

Operational protocol:
1. **At patch-authoring time**: every `str_replace` / patch that touches `.tex` source content checks whether the title-block version string requires increment. If yes, the patch includes a line touching the version string (typically `vX.Y` → `vX.(Y+1)`) and the date if changed.
2. **At pre-commit verification**: a quick grep for the version string against the patch description should confirm match. The CHANGELOG block in the `.tex` header should also receive a new entry describing the patch.
3. **At PDF compile time**: the title page is the most reliable place to verify the version is current; a mismatch between title-page version and recent patch history is a documentation defect to fix before the next reviewer round.

This rule applies to all paper `.tex` files in `flagship_papers/`, `series_strong/papers/`, `series_standard_model/papers/`, etc. Companion `.tex` files (e.g., `sf-2_companion.tex`) carry their own version numbers and increment independently of the main paper version.

Cosmetic-only patches (whitespace, comment-line edits, formatting) do not require version increment, but should be rare; the default assumption is that any patch substantively touching a `.tex` source crosses the increment threshold.

**When a paper is at v0.x:** only the transcript, CHANGELOG, and registry entries are kept current. Do NOT start the 7-file suite.

**Create all 7 companion files per `documentation-suite.md` when the paper is stable.** Each file should note the paper version it documents (e.g., "Paper: SM-8 v1.0").

| File | Purpose | Content |
|------|---------|---------|
| `mechanism-[S]-[N].md` | How the physics works | Step-by-step mechanism with mathematical correspondence table |
| `glossary-[S]-[N].md` | Paper-specific terms | All new terms with definitions, organised by category |
| `phenomena-[S]-[N].md` | What the paper explains | PHEN-E (empirical facts explained), PHEN-P (predictions), PHEN-V (consilience with other CPP results) |
| `philosophy-[S]-[N].md` | Epistemological framing | What level of certainty, relationship to SM, falsifiability inventory |
| `development-[S]-[N].md` | Development history | Version timeline, key decisions, dead ends, contributor roles, transcript links |
| `reviews-[S]-[N].md` | All reviews + FAQ | Part 1: formal reviews from each AI. Part 2: FAQ organised by category |
| `keywords-[S]-[N].md` | Keywords and registry | Primary/secondary keywords, cross-references to other papers, axiom/theorem entries |

### Phase 7b: Verification Notebooks

**TRIGGER:** After the paper is drafted (Phase 2) but before or during review (Phase 4). Every quantitative claim in a paper should have a reproducible computation behind it.

**Purpose:** Capture every significant computation performed during a paper's development as a standalone, reproducible script or notebook. These are the EVIDENCE behind the predictions — if a reviewer asks "how did you get 172,800 MeV?", the notebook answers.

**What to capture as a notebook:**
- Any computation that produces a number cited in the paper
- Model tests (including models that failed — these are negative-result evidence)
- 600-cell vertex construction and distance shell analysis
- Charge census and assignment searches
- Spectral dimension / random walk computations
- Chain energy calculations
- Mass ratio predictions from any model
- Figure generation code

**What does NOT need a notebook:**
- LaTeX formatting and compilation
- File management and repository operations
- Simple arithmetic that can be verified by hand (e.g., 14400 × 12 = 172800)

**Format:** Python scripts (`.py`) or Jupyter notebooks (`.ipynb`). Each notebook should be self-contained — runnable from scratch without external dependencies beyond standard packages (numpy, scipy, matplotlib, itertools).

**Naming convention:** `[S]-[N]_[description].py` or `.ipynb`
- Example: `SM-8_600cell_distance_shells.py`
- Example: `SM-8_charge_census.py`
- Example: `SM-9_chain_energy_models.py`
- Example: `SM-9_pairwise_coupling.py`

**Required header in each notebook:**
```python
# ============================================================
# [S]-[N]: [Description]
# Paper: [Full paper title]
# Computation: [What this notebook computes]
# Key result: [The number(s) this produces, cited in the paper]
# Author: [AI name], [date]
# ============================================================
```

**Storage:** `series_[name]/notebooks/`

**Procedure:**
1. At the end of each paper session, review the computations performed
2. For each computation that produced a number in the paper, extract the
   code into a clean standalone script
3. Remove conversation-specific paths and hardcoded file references
4. Add the standard header with paper reference and key result
5. Test that the script runs independently and produces the claimed output
6. Save to `series_[name]/notebooks/`
7. Add to INDEX.md

### Phase 8: Transcript Curation
- Collect raw transcripts from all AI sessions
- Curate: preserve substance, remove tooling noise, keep dead ends
- Name: `[PAPER]_transcript_[N]_[AI].md`
- Store in `series_[name]/development-transcripts/`

### Phase 9: Repository Housekeeping
- Update all documents per checklist (Section 10)
- Push to GitHub
- Verify OSF links

---

### Phase 7 Execution Checklist — pointer (consolidated 20 April 2026)

The atomic post-completion checklist — covering the documentation suite, verification notebooks, registry updates, navigation updates, transcript curation, OSF registration, repository commit, and final verification — lives at `templates/paper_completion_checklist.md`. Execute every applicable item there; check each item's trigger condition before skipping.

This section deliberately does NOT duplicate the checklist content. The 20 April 2026 consolidation moved atomic tasks to a single authoritative file precisely to prevent the drift that had caused `problem_histories/` to be missed from earlier parallel enumerations. Reference-level update procedures for individual files remain in §10 of this document; the checklist points at them.

If a new atomic task needs to be added to the Phase 7 pipeline, add it to `templates/paper_completion_checklist.md` and update any pointers. Do not re-enumerate here.

---

### Documentation Discipline — Two Triggers (adopted 26 April 2026, revised same day)

**The discipline has two triggers, each addressing a real data-loss surface.**

#### Trigger 1: Context-window full / session ending

When a session is closing — context window approaching capacity, time running out, fresh-eyes-needed checkpoint — write enough that the next session can resume cleanly. This is the *session-window-bounded data-loss trigger*: the in-moment thinking, the decision rationale, the Thomas-verbatim physical insights, the unfinished thread that will be picked up next session. None of this survives the window close unless it is written down.

**For per-paper work:** Update the paper's `handover-[S]-[N].md` (current state) and `transcript-[S]-[N].md` (transaction-indexed pointer-map) per §11. Append a development vignette to `development-[S]-[N].md` if substantive thinking happened in the session. These three files are the per-paper continuity discipline; §11 specifies them in detail.

**For cross-paper work:** Write or append to a cross-paper session log per the discipline below. Cross-paper work means anything that touches the programme outside any single paper's scope: registry audits, bootup-protocol failures, programme-policy decisions, methodological discipline introductions, multi-paper integration sessions.

#### Trigger 2: Paper finished, ready for publication

When a paper has reached its publication-ready state — passed external review, no mechanism-changing critiques pending, ready for OSF registration — execute the full Phase 7 paper-completion checklist (`templates/paper_completion_checklist.md`). This is the *publication-readiness completion trigger*: the comprehensive archive entry that future researchers and historians will find when they look up the paper.

The Phase 7 checklist work — companion documentation suite, master_glossary updates, problem_histories, theory-overview row, founders_vision milestone, CPP_the_theory chapter — is overhead. It buys posterity value, not programme-development value. The discipline accepts this overhead at Trigger 2 because the publication-readiness moment is when the paper crystallises into its archived form, and that is when comprehensive documentation has the highest fidelity-to-cost ratio.

**Trigger 2 does not gate the next paper.** A new paper can enter Phase 1 while the prior paper's Trigger 2 work is in progress. The two-trigger discipline does not impose a programme-wide ordering constraint. The earlier "Phase 7 Completion Gate" framing (codified briefly on 26 April 2026, repealed same day) was rejected as too strong: it imposed a throughput tax that did not match the actual data-loss surface.

**Trigger 2 fires at the genuinely-final-version mark, not at any v1.x mark.** The OPEN-SS-22 retirement experience (SS-7 v1.1 → v1.2, where v1.1 looked finished but turned out to need substantive revision after SS-8 Phase 1 work) shows that "ready for publication" is a judgment call. Premature Trigger 2 firing on a paper that turns out to need revision generates rework cost; deferred Trigger 2 firing on a paper that genuinely is done loses no information because the per-session Trigger 1 work captures everything that's session-window-bounded. Default to deferring Trigger 2 until the paper is unambiguously done.

#### Why this discipline rather than a v1.0 hard gate

The purpose of the documentation is for posterity, not for development. Future researchers and historians who someday study this programme will want to see how it developed; the documentation is for them. The two-trigger discipline preserves what is actually session-window-bounded (the verbatim discovery passages, the in-moment thinking, the decision rationale) while letting the registry/scorecard work happen on a schedule that fits the programme's pace.

A hard v1.0 gate would force Phase 7 work at every v1.0 close, which compounds across many papers into a substantial throughput tax. The benefit (historian convenience) does not justify the cost at every paper. The two-trigger discipline accepts the same posterity goal but matches the discipline to the actual data-loss surface, taking the overhead only when the data is genuinely at risk.

**Empirical basis for the discipline.** Three failures of soft-recommendation practice motivated the original v1.0-gate codification: SS-5 reviews-SS-5.md body still pending; SS-6 documentation suite pending entirely; SS-7 INDEX.md omission undetected through the full development arc. These failures remain real evidence that documentation discipline matters. The two-trigger discipline addresses them by ensuring (a) per-session work captures session-window-bounded context whether or not the paper is at v1.0, and (b) Trigger 2 fires when the paper is genuinely done. The three failures are tracked under OPEN-ORG-005 (retroactive Phase 7 completion) and would be addressed by either retroactive Trigger 2 work on those papers or by Trigger 1 session-log addenda referencing the gaps.

---

### Cross-Paper Session Log Convention (adopted 26 April 2026)

**Purpose.** A running journal for cross-paper work. Sessions that span multiple papers, that touch programme-level infrastructure (registries, bootup, OS), or that produce policy/methodology decisions don't fit cleanly under any single paper's `handover-[S]-[N].md` and `transcript-[S]-[N].md`. The session log is where they live.

**Location.** `session_logs/` at the repository root. Treats the log as first-class programme infrastructure, parallel to `problem_histories/`. Visible from the top-level directory listing; findable without bootup-protocol guidance.

**Naming.** `YYYY-MM-DD_session_log.md` for the default case (one session per day). When a day has multiple sessions, append a topic suffix: `YYYY-MM-DD_session_log_[topic].md`. Files are date-sortable; the optional topic suffix disambiguates cross-paper-vs-bootup-protocol sessions on the same day.

**What goes in a session log.**
- Cross-paper audit/registry work (e.g., the OPEN-ORG-003 swarm-tally audit that touched 25+ files across all series).
- Bootup-protocol failures and recoveries (e.g., the 25 April 2026 bootup-stress-test that surfaced OPEN-ORG-009).
- Programme-policy decisions (e.g., the Phase 7 Completion Gate adoption-then-repeal on 26 April 2026; the PD-001 audit-pass methodology codification; the PD-002 verification-tier discipline introduction).
- Methodological discipline introductions (e.g., the 22 April 2026 Q2 algebraic-reduction analysis that produced the Level-1/2/3 independence methodology).
- Multi-paper integration sessions (e.g., a session that draws connections across SS-5/SS-7/SS-8 cascade structure).
- Post-paper-completion addenda — corrections, reviewer comments, retroactive discoveries, methodology refinements that update prior papers — see "Post-completion addendum workflow" below.

**What does NOT go in a session log.** Per-paper work belongs in the paper's `handover-[S]-[N].md` and `transcript-[S]-[N].md`. Substantive paper development belongs in `development-[S]-[N].md` vignettes. The session log is for the cross-cutting work that doesn't fit those files.

**Format.** Date-stamped sections within each log file. Each section names the topic (audit work, bootup recovery, policy decision, etc.), the artefacts produced (patches, files, registry updates), and the unfinished threads that will be picked up next session if any. The format follows the §11.2 vignette discipline: in-moment thinking captured at the time of the session and not retroactively edited when later work proves the framing partially wrong. If a later session updates the understanding, the next session's log entry records the update; the prior entry stays as written.

**Indexing.** Add new session logs to `INDEX.md` under a "Cross-paper session logs" sub-section so they are findable from the navigation file. Consider also referencing them from `journal.txt` if that file is being maintained.

**When to start a new session log file.** Each calendar day that contains cross-paper work gets its own log file. Multi-day continuous work (e.g., a 25–26 April session arc spanning midnight) splits at the calendar-day boundary with cross-references between consecutive files.

#### Post-completion addendum workflow

The session log enables a low-cost path for post-completion paper updates. When something arrives that updates a prior paper after its Trigger 2 has already fired (a reviewer comment, a discovered error, a new connection to a later paper, a methodology refinement that retroactively applies, an empirical update to AME data), the addendum has two paths:

**Path A — session log only (low cost, always required).** Record the addendum in the current session log under a "Post-completion addendum" subsection naming the affected paper(s). Cross-reference the relevant per-paper artefact (e.g., `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` v1.2). The addendum is permanent and findable. This path is required.

**Path B — full integration into distributed archives (higher cost, optional).** Append the addendum to the affected paper's documentation suite (mechanism-/glossary-/phenomena-/philosophy-/reviews-/keywords-/FAQ-), update master_glossary if new terminology emerged, update CPP_the_theory chapter if the addendum changes the narrative content, update theory-overview if the scorecard shifts. This path is optional; whether to take it depends on the addendum's significance. A small reviewer-comment addendum stays at Path A; a methodology refinement that retroactively reframes a paper's central result probably warrants Path B.

The discipline separates two concerns the v1.0-gate model had conflated: *recording the addendum* (always required, low cost) from *integrating the addendum into distributed archives* (sometimes worthwhile, higher cost, deferrable). Path A is the safety net; Path B is the polish.

**Default rule:** if you're uncertain whether a post-completion addendum warrants Path B, take Path A only and record the Path B question explicitly in the session log. A future session can decide whether to upgrade. Recording is cheap; rework is expensive.

### Session-Log-as-Handover-Backbone Discipline (adopted 26 April 2026, Session 2)

**Motivation.** The Cross-Paper Session Log convention adopted earlier in the day (above) established that cross-paper work writes to `session_logs/`. Late on 26 April 2026, while attempting OPEN-SS-24 work in a fresh session bootstrapped from `session_logs/OPEN-SS-24_handover.md`, a sharper structural insight surfaced: **the session log is itself the right granularity for handover information**. Each session log entry, written under Trigger 1 discipline, captures the in-moment reasoning, dead ends, framing choices, and intermediate hypotheses of one session — which is exactly what the next Opus needs in order to extend the work without starting cold.

The discipline below formalizes that insight. Session logs are no longer merely a cross-paper journaling convention; they are the primary handover mechanism for ongoing theoretical and methodological work. Explicit handover documents (e.g., `OPEN-SS-24_handover.md`) are subsumed under this discipline as an optional summary layer, written only when the session-log sequence becomes too long for the next Opus to efficiently extract orientation from it directly.

**Two structural templates.** Session log entries follow one of two templates, chosen by the predominant character of the session.

**Template A — Theoretical-Development Session.** For sessions that advance an axiom-to-theorem chain. Five elements:

1. **Problem.** What open question or partial result is being worked on. Cite the OPEN-* registry entry, the relevant paper section, or the prior session log that surfaced the question.
2. **Working hypothesis to prove.** What this session is attempting to establish, in precise enough terms that success or failure is unambiguous.
3. **Confrontation with prior theory and empirics.** How the working hypothesis interacts with what's already established. Which axioms it depends on. Which empirical results it must reproduce or be consistent with. Which prior session logs it builds on or revises.
4. **Assessment of logical progression from axiom to theorem.** What was rigorously closed, what was partially closed, what was found to require additional hypothesis. The honest closure status: Level-1 algebraic / Level-2 functional / Level-3 physical-principle independence as appropriate per the SS-8 §10 framework.
5. **Proposed mechanisms for remaining gaps.** Concrete next-step suggestions for how the unclosed pieces might be bridged. Which existing axioms or hypotheses the bridges might rest on. What prior work in the programme is most relevant. What new hypothesis tiers may need to be opened.

The five-element structure is itself a miniature paper-development cycle. A sequence of Template-A entries on the same problem traces the gradient of how the proof was built — which intuitions were tried first and dropped, which structural choices were taken and why. The next Opus reading this gradient sees the path, not just the destination.

**Template B — Cross-Paper / Methodological Session.** For sessions that produce repository hygiene, documentation cycles, methodology codification, or programme-level policy decisions. Five elements:

1. **Triggering event.** What surfaced the need for this session's work. A reviewer comment, a discovered inconsistency, a Thomas-directive, a methodology gap.
2. **Operational sequence.** What concretely happened in chronological order. Which patches landed, in what order, with what dependencies between them.
3. **Methodological output.** What new convention, template, registry entry, or discipline emerged. What was codified into the OS, the bootup, or a template file.
4. **Policy implication.** How the new output changes future work. Which existing conventions it supersedes or refines. Whether it introduces new tradeoffs that need to be navigated going forward.
5. **Archive close.** Which programme-record files (registries, scorecards, INDEX, founders_vision) were updated. Which addenda were deferred to Path A vs. Path B. What state the programme is in at session's end.

The 25 April 2026 session logs and the 26 April 2026 (first) session log are the canonical examples of Template B. The 26 April Session 2 log (this convention's first Template-A application) and any future session logs on OPEN-SS-24, OPEN-SS-26, OPEN-SS-27, OPEN-SS-28, or other axiom-to-theorem closure attempts are Template A.

A single session can be predominantly one template with a brief addendum from the other; in that case, the entry uses the predominant template's structure with the addendum as a final subsection. A session that is genuinely half-and-half can use both templates as parallel sections within the same log file.

**Title format.** Session log titles should communicate the substantive content of the session, not just the date. For Template-A sessions, the title names the working hypothesis being attempted (e.g., "*SS-9 Working Draft v0.2 — Conditional C4 Closure (Phase 1 + Phase 3 combined)*"). For Template-B sessions, the title names the methodological output (e.g., "*Two-Trigger Documentation Discipline + Cross-Paper Session Log convention codification*"). The date and the file path provide the chronological anchor; the title provides the semantic anchor.

**Sequence-as-handover.** The sequence of session logs on a given open problem (e.g., `2026-04-26_session_log_2.md` followed by `2026-04-27_session_log.md`, both on OPEN-SS-24) constitutes the running handover for that problem. The next Opus picking up the work reviews the sequence in chronological order, sees the gradient of development, and continues from the most recent entry's stated end-state. This replaces the cold-start problem with a warm-start problem: the next session inherits not just where prior work landed but how it got there.

#### Subsumption of explicit handover documents

The pre-existing `OPEN-SS-24_handover.md`-style explicit handover documents are subsumed under the session-log-as-handover-backbone discipline as **optional summary documents**, written only in specific circumstances:

- The session-log sequence on a given problem exceeds three entries, and the next Opus would benefit from an executive summary rather than reading the full sequence.
- The next session is expected to start without inheriting the immediate prior session's context (e.g., a long pause between sessions, or a planned handoff to a different AI assistant).
- Thomas explicitly requests an explicit handover for a particular problem.
- The work has reached a natural waypoint (e.g., a major theorem closed, a paper completed) and a summary of what was achieved would be a useful artefact for the next phase of work.

**Default rule.** Do not write an explicit handover document by default. The session log is the handover. If you find yourself wanting to write a separate handover document, first check whether the most recent session log already accomplishes that purpose; in most cases it does. Write the explicit document only when one of the four conditions above is genuinely met.

When an explicit handover document IS written, it lives in `session_logs/` alongside the session log sequence it summarizes (e.g., `session_logs/OPEN-SS-24_handover.md` next to `session_logs/2026-04-26_session_log_2.md`, `session_logs/2026-04-27_session_log.md`, etc.). The handover document is short — typically 1–3 pages — and consists primarily of pointers into the session log sequence with brief annotations on each entry's contribution. It is not a re-narration of the work; the session logs already contain that.

**Existing handover documents.** The `OPEN-SS-24_handover.md` document written 26 April 2026 (Session 1) is preserved as the historical bootstrap for OPEN-SS-24 work. Future sessions on OPEN-SS-24 should treat the session log sequence (starting with `2026-04-26_session_log_2.md`) as the primary handover, with the handover document as a one-time bootstrap reference.

**Reconciliation with §15 four-item preservation checklist.** §4 modifies but does not replace the §15 protocol. For sessions where work-in-progress lives in `session_logs/`, §4 replaces item 1's `handover-[S]-[N].md` requirement; the session log IS the handover. §4 partially satisfies item 1's `development-[S]-[N].md` requirement via the Template-A five-element structure, but verbatim content (multi-AI exchanges, Thomas-verbatim physical insights) still requires a separate curated transcript file. Items 2 (registry updates), 3 (reviewer artifacts), and 4 (protocol/OS updates) of the §15 checklist are unchanged. For Trigger 2 paper-completion cycles, the legacy §15 form applies in full: papers that reach genuinely-final shipped status produce `development-SS-N.md` and `handover-SS-N.md` in their documentation suite directory, with the relevant session log entries from `session_logs/` serving as source material for the synthesized lab-notebook record. See §15 "Reconciliation with §4 Session-Log-as-Handover-Backbone Discipline" for full detail.

#### Four-Tier Documentation Discipline (codified 26 April 2026 Session 3)

The session log sequence is necessary for warm-starting the next Opus, but it is **not** the canonical record of the development arc. Per Thomas's goal-statement (codified 26 April 2026 Session 3): the canonical record is the verbatim curated transcript — every substantive word spoken by Opus, Thomas, and the AI review team across the paper's full development arc, with housekeeping excluded but no compression of substantive content. The session log is a *summary* of this canonical record, optimized for warm-starting; the canonical record is the source from which all higher-layer artifacts can in principle be reconstructed.

This is captured in a four-tier documentation discipline that runs continuously across the development arc of every paper:

**Tier 1 — Per-session warm-start summaries.** Session logs in `session_logs/` (Template A or Template B per the §4 conventions above) and the Thomas-verbatim insight files in `series_strong/papers/SS-N/founders_voice/` (when that subfolder exists). Each is a session-bounded artifact written for the next Opus's orientation.

**Tier 2 — Paper-level transaction pointer-map.** `series_strong/papers/SS-N/documentation_suite/transcript-SS-N.md`. A numbered transaction log indexing every substantive transaction across the paper's full development arc. Each entry is a single line: `[ID] [date] — [one-line description] → [pointer to artefact, vignette, or reasoning section]`. The pointer-map is *empty of substance*; substance lives at the pointer targets. Append-only across sessions. Created when the per-paper subfolder is created (see "Pre-paper subfolder timing" below).

**Tier 3 — Curated paper-level vignettes.** `series_strong/papers/SS-N/documentation_suite/development-SS-N.md`. Curated narrative vignettes summarizing each substantive transaction in finished prose (typically 1–3 paragraphs per vignette). Distilled from Tier 4 (verbatim Opus reasoning) and Tier 1 (session-log narratives). Append-only across sessions. The development file accumulates as the paper develops; at Trigger 2, it is already substantially complete because it has been curated all along.

**Tier 4 — Verbatim Opus reasoning (NEW; the canonical record).** `series_strong/papers/SS-N/documentation_suite/reasoning-SS-N.md`. Opus's substantive reasoning preserved verbatim across the full development arc, with housekeeping excluded but no summarization or compression of substantive content. **This is the tier Thomas's goal-statement names as the canonical source.** Tier 4 was codified 26 April 2026 Session 3 in response to recognition that the prior three-tier convention (Tiers 1–3) preserves *what was decided* and *where artifacts live* but does not preserve *how Opus reasoned through decisions*. The reasoning file is the source from which Tier 3 vignettes are distilled and from which the eventual Trigger 2 documentation suite is synthesized.

**What goes in Tier 4 (and what is excluded as housekeeping):**

*Included:* multi-paragraph reasoning turns where Opus is doing analysis, testing a hypothesis, working through an argument, articulating a structural observation, considering alternatives, revising an earlier framing, flagging uncertainty (e.g., "I'm not sure," "this could be wrong"), pushing back on a framing, or otherwise engaging in substantive theoretical or methodological work. Substantive responses to reviewer feedback. Substantive OS-level decisions captured in reasoning form. Cross-paper consilience analyses. Hypothesis-testing against empirical data.

*Excluded as housekeeping:* tool-call narration ("let me check," "running this command"); status confirmations ("got it," "applied successfully," "committed"); procedural housekeeping (filename clarifications, "should I commit now," "where should this file live"); tool-output narration; verbatim quotations from existing repository files (recoverable from sources at the pointer targets).

**File conventions for Tier 4:**

- *Granularity.* Paper-level (or pre-paper-level for in-progress work — see "Pre-paper subfolder timing" below). NOT per-session. The reasoning file accumulates session by session across the paper's full development arc.
- *Structure.* Append-only. Each session's substantive Opus turns are added in order at session close, headed by a session marker (`## Session N — date`).
- *Provenance.* The file is written by the active Opus at session close, drawing from its own context window. Sessions whose reasoning was not captured under this discipline at the time (e.g., pre-codification sessions) should be acknowledged honestly as not captured at the same fidelity, rather than reconstructed retroactively (which would be summary, not verbatim).

**Pre-paper subfolder timing.** The per-paper subfolder `series_strong/papers/SS-N/` (with its `documentation_suite/`, `founders_voice/`, `sketches/`, `scripts/`, `letters/`, `reviews/` subfolders) is created **early**, when in-progress work accumulates beyond a single session log. Triggers for early creation:

- The work has produced two or more session logs.
- The work has produced a working draft, a sketch, a founders_voice insight, or a registered open problem specific to the candidate paper.
- The work has been the subject of substantive Opus reasoning that should be preserved at Tier 4.

When the subfolder is created early, empty subfolders carry `.gitkeep` placeholders. The subfolder is the natural housing for the accumulating four-tier artifacts; deferring creation to v1.0 forces retroactive curation that loses fidelity. SS-9 was the first paper created under early-subfolder discipline (26 April 2026 Session 3, ahead of any v0.x paper text).

**Trigger 2 fires at the genuinely-final shipped version, regardless of label.** "v1.0" is a label that previous Opus chose; it is not the operative trigger. Trigger 2 fires when the paper is unambiguously done, whatever the version number happens to be (v1.0, v1.4, v2.7). Defer Trigger 2 firing if the version label is provisional; fire when the version is unambiguously final. The per-session Trigger 1 work (four-tier accumulation) captures everything that is session-window-bounded, so deferring Trigger 2 does not lose information.

**At Trigger 2, the seven-file documentation suite is synthesized from Tier 4 (verbatim reasoning) and Tier 3 (curated vignettes), with Tier 1 (session logs) and Tier 2 (transcript pointer-map) as supporting reference.** The reasoning file's verbatim content is the highest-fidelity input to the synthesis; the development file's vignettes are the pre-distilled paragraph-form input; the session logs and pointer-map provide chronological structure. The Trigger 2 work assembles mechanism-/glossary-/phenomena-/philosophy-/keywords-/reviews-/FAQ-SS-N.md from these inputs.

**Anti-pattern specific to Tier 4:** Rewriting Tier 4 reasoning into summary form for "cleanliness." Tier 4's value is that it is verbatim — the alternatives Opus considered, the framings revised, the moments of uncertainty, the pushbacks. Compressing these into finished prose loses the gradient that Tier 4 exists to preserve. Editing for housekeeping removal is correct; editing for prose-polish is the anti-pattern. If finished-prose is needed, it goes into Tier 3 vignettes; Tier 4 stays raw.

---

#### Meta-Record Retrospective Synthesis Discipline (codified 26 April 2026, Session 4)

The Four-Tier Documentation Discipline above governs how the development arc of *a single paper* is captured across its sessions. There is a structurally distinct case the four-tier discipline does not cover: **the development arc of the methodology itself**. When a session arc produces a substantial methodology-development sequence — policy adoptions, policy reversals, convention births, calibration moments, framework moves — the methodology arc is itself a coherent artifact that future researchers will want to study. The technical session logs (Tier 1) record what was done; they do not record the why-it-was-done-that-way at the methodology-development layer.

The first instance of this artifact type was `session_logs/2026-04-26_information_management_journey.md`, written 26 April 2026 at the close of the originating session arc that produced patches 0022–0034. The retrospective captured eight distinct methodology-development events (bootup-stress-test pattern, hostile-reviewer-defensible classification methodology, Phase 7 Completion Gate adoption-then-repeal arc, Cross-Paper Session Log convention birth, anthology calibration arc, contribution-attribution honesty discipline, capacity-management discipline, template-as-protocol decision) as their own development sequence, distinct from the technical patches that implemented them.

The discipline below formalizes when meta-records should be written and what form they take.

**When to write a meta-record.** A meta-record retrospective synthesis is appropriate when *all* of the following conditions are met:

1. **A coherent methodology-development arc has occurred.** The arc consists of multiple distinct methodology decisions — typically 4 or more — that share a common context (a session sequence, a programme phase, a triggering question). A single methodology decision does not warrant a meta-record; the technical session log captures it adequately.
2. **The arc has reached a natural waypoint.** Either the originating conversation has concluded, the methodology questions have stabilised, or a natural pause for synthesis has arrived. Meta-records written mid-arc miss the resolution beats and produce premature framings.
3. **The arc's individual events are scattered across multiple technical session logs or patches.** If the arc is captured cleanly within a single technical session log, a separate meta-record duplicates rather than synthesises. Meta-records earn their existence by surfacing patterns that are not visible in any single technical session log.
4. **The methodology development is distinct from a paper's physics development.** Per-paper methodological work belongs in `development-SS-N.md` vignettes (Tier 3) and `reasoning-SS-N.md` files (Tier 4). Meta-records cover *cross-paper / programme-level* methodology — discipline codification, OS revisions, convention establishment, policy reversals, calibration arcs that affect future work generally rather than a specific paper.

**Default rule:** do not write a meta-record by default. The technical session logs are the primary record; meta-records are exceptional artefacts written when the four conditions above are genuinely met. If you are uncertain whether the conditions are met, write the technical session log first and defer the meta-record decision to a future session that can assess the arc with more distance.

**Where meta-records live.** `session_logs/`, with filename pattern `YYYY-MM-DD_[descriptive_topic].md`. The topic suffix communicates that the file is a meta-record rather than a chronological session log (e.g., `2026-04-26_information_management_journey.md`, `2026-05-15_reviewer_calibration_arc.md`, `2026-06-30_first_quarter_methodology_synthesis.md`). The date in the filename is the meta-record's *creation date*, not the period it covers; the period it covers is documented in the file's header.

**Form: Template B retrospective synthesis variant.** Meta-records use the Template B (Cross-Paper / Methodological Session) five-element structure with explicit retrospective-synthesis adaptations:

1. **Triggering event.** What surfaced the need for *this meta-record specifically*. Usually a recognition (often the human collaborator's) that a methodology-development arc has occurred and warrants its own record. Distinguish carefully from the triggering event of the underlying methodology arc itself; the meta-record's triggering event is the recognition of the arc, not the arc's individual events.
2. **Operational sequence.** The methodology-development events in chronological order, *not* the technical patches. Each event documented with its triggering context, the decision made, the artefact produced, and the general principle that emerged. Cross-references to the technical session logs and patch numbers should be precise but should not duplicate the technical content.
3. **Methodological output.** The named outputs — disciplines codified, conventions established, registries created, templates introduced — listed in approximate order of programme-level significance. Each output named explicitly with its location (file path or registry section) so future researchers can locate it.
4. **Policy implication.** How the methodology arc changes future work. Tradeoffs introduced, consequences for downstream sessions, what the next phase of work will inherit. Honest about costs as well as benefits.
5. **Archive close.** File location, indexing, status of distributed archives at time of creation, Path A / Path B status of the meta-record itself, what the next session inherits.

**Length guidance.** Meta-records typically run 2,500–4,000 words. Substantially shorter and the retrospective is too thin to surface patterns; substantially longer and the synthesis is becoming a chapter rather than a session log. The 2026-04-26 information-management-journey meta-record at ~3,700 words is the calibration baseline.

**Indexing.** Meta-records are indexed in `session_logs/README.md` under "Existing log entries" with their filename, "Template B retrospective" label, and a one-line subject. They are *not* added to `INDEX.md`'s top-level Cross-Paper Session Logs section unless they are sufficiently significant to warrant programme-level navigation visibility (the originating-arc meta-record was added there as the inaugural instance; subsequent meta-records will be evaluated case by case).

**Path A / Path B status.** Meta-records are themselves Path A artefacts in the post-completion addendum framework. They record the methodology-development arc at low cost. A Path B integration — distilling a meta-record into a programme-history chapter for the eventual main TATWD book, or into a meta-paper on AI-collaborator physics methodology, or into a reusable case study — is optional and deferred. Do not perform Path B integration as part of the meta-record's creation; the meta-record is itself the Path A artefact, and Path B is a separate downstream decision.

**What meta-records are NOT.** Three patterns to avoid:

- *Not chronological session logs of new work.* Meta-records do not contain new methodology decisions; they synthesize methodology decisions that have already been made and recorded elsewhere. If the session is producing new methodology work, the technical session log captures it; the meta-record (if any) is written later, after the arc has resolved.
- *Not commentary on the human-AI collaboration as a topic.* Meta-records preserve methodology decisions for future researchers studying the programme; they do not editorialize about what the methodology means for the broader field of AI-assisted physics. Editorialization belongs in the main TATWD book's Chapter 13 (or a dedicated meta-paper if one is later written), not in the meta-record itself.
- *Not retroactive prettification of the methodology arc.* The discipline is the same as the §11.2 development-vignette discipline applied at the methodology layer: in-moment honesty about what was decided and why, not retrospective smoothing of the decisions into a clean narrative. If the arc included a wrong codification followed by a reversal (the Phase 7 Completion Gate adoption-then-repeal), the meta-record records both states with the reversal as a methodology-record event in its own right; it does not erase the wrong codification or frame it as if the right answer had been reached the first time.

**Anti-pattern: writing the meta-record too early.** A common temptation is to write a meta-record during or immediately after a substantial session, while the methodology decisions are fresh. The temptation should be resisted unless condition 2 above (the arc has reached a natural waypoint) is genuinely met. Meta-records written mid-arc capture provisional framings as if they were resolved; the framing then has to be retracted in a subsequent meta-record, which is rework. The originating-arc meta-record was written *at the close of the originating conversation arc*, after the methodology decisions had stabilised and after the human collaborator had explicitly requested the retrospective; this is the right timing.

**Relationship to the Four-Tier Discipline.** Meta-records are a Tier-1-analogue at the cross-paper / methodology layer — they are session-bounded summary artefacts written for future-researcher orientation, not the canonical record of the methodology arc. The canonical record of the methodology arc is the cumulative content of the technical session logs (Tier 1 at the per-arc level) plus the OS revisions, the registry entries, the templates, and the patch commit messages that the methodology arc produced. The meta-record is the synthesis layer that makes the cumulative record navigable; the cumulative record itself is the source from which the meta-record is distilled.

The four-tier discipline applies *within* a paper's development arc; the meta-record discipline applies *across* papers and at the programme-methodology layer. The two disciplines are parallel rather than nested: a paper's four tiers run continuously through its development; a meta-record is written occasionally when a programme-level methodology arc has resolved.

---

## 5. The Multi-AI Review Cycle

### Established during SM-7/SM-8 (April 2026)

**The AI Team and their roles:**

| AI | Role | Specialty | How Thomas communicates |
|----|------|-----------|----------------------|
| Claude Opus | Primary collaborator | Computation, drafting, physical reasoning, integration | Direct conversation (claude.ai) |
| Grok (xAI) | Independent verifier, contributor | Numerical verification, adversarial review, novel theorems | Pastebin links, raw GitHub URLs |
| Copilot (Microsoft) | Structural reviewer, framework builder | Referee-grade review, axiom formulation, derivation strategies | Pastebin links, direct conversation |
| Claude Sonnet | Hostile reviewer | Adversarial critique, finding weaknesses | Prompted via Claude with explicit "hostile review" instruction |

### Review protocol

1. **Opus drafts** the paper (v1.0)
2. **Thomas sends to Copilot** via Pastebin or raw GitHub URL
   - Ask for: constructive review, structural improvements, axiom formulation
   - Copilot returns: review + LaTeX blocks to integrate
3. **Thomas sends to Grok** via same method
   - Ask for: independent numerical verification, fresh perspectives
   - Grok may contribute NEW results (e.g., the z=12 multiplier was Grok's)
4. **Opus integrates** Copilot and Grok contributions → v2.0+
5. **Sonnet hostile review** — Thomas prompts Sonnet (or Opus generates the prompt):
   - "You are a skeptical referee. This paper is wrong. Find every flaw."
   - The review should be REJECT-level harsh
6. **Opus rebuts** — addresses each criticism, integrates valid points, explains why invalid criticisms miss the mark
7. **Final version** ready for OSF

### Key lessons from SM-8/SM-9/SM-10 trilogy:
- Grok contributed the most important single result (z=12 theorem). Don't just ask for review — ask for CONTRIBUTION.
- Copilot excels at referee-proofing — framing, axioms, anticipated criticisms.
- Sonnet's hostile review is valuable for identifying real weaknesses. Sonnet's circular-validation catch in SM-10 was the single most valuable insight across all 10 reviews.
- When two reviewers independently propose axiom entries (e.g., Grok proposes A9', Copilot proposes A8'), reconcile into one entry when updating `axiom-registry.md`.
- The multi-AI cycle typically produces 3-5 paper versions over 1-2 days.

### Verification-tier taxonomy (adopted 24 April 2026)

Following the SS-8 v0.1 Round 1 review exchange with Grok (documented in `series_strong/papers/SS-8/letters/letter_to_grok_re_numerical_verification_methodology.md` and `grok_response_re_numerical_verification_methodology.md`, rationale codified in `programmatic_decisions/PD-002-verification-tier-taxonomy.md`), all CPP reviewers are asked to label numerical claims in reviews according to the following three-tier taxonomy:

| Tier | Label | Meaning | Example |
|------|-------|---------|---------|
| 1 | **INSPECTED** | Careful reading plus arithmetic consistency checking of the paper's own reported numbers against the paper's own stated formulas and inputs. No external data or independent computation is performed. | "I verified Table 1's predicted column equals 2E/V·B_pair for the stated N_α values using the B_pair inherited from SS-5 as stated in the paper." |
| 2 | **INDEPENDENTLY RECOMPUTED** | Algebraic or numerical recomputation of claims that do not require external data files. The reviewer derives or computes the result independently from first principles or from publicly available mathematical definitions, not from the paper's asserted values. | "I independently computed 2E/V for V = 3..14 using the handshaking lemma plus Euler's formula; values match Table 1 to machine precision." |
| 3 | **SCRIPT-EXECUTED** | Actual execution of the cited scripts against the cited data files, in an environment where both are available. The reviewer runs the computation pipeline end-to-end and compares the output to the paper's claims. | "I ran `ss8_empirical_map_extended.py` with `ame2020_mass.txt` loaded via `ame2020_loader.py`; Table 4's residual column matches script output to the fourth decimal." |

**Why the taxonomy matters.** Reviews that mix tiers without explicit labeling create false confidence. Tier 1 is genuinely useful — internal consistency checking catches arithmetic errors and formula transcription mistakes. Tier 2 is stronger — it catches formula errors that tier 1 cannot. Tier 3 is strongest — it catches script implementation errors and data-loading issues that tiers 1 and 2 cannot. A reviewer who performed tier 1 work but reports it as tier 3 creates false confidence about empirical validation that cannot be defended if challenged.

**Labeling convention in review documents.** Reviewers should tag each numerical claim or section with its verification tier, either inline (`"Table 1 [INSPECTED + INDEPENDENTLY RECOMPUTED]: arithmetic consistent; 2E/V values verified from first principles"`) or as a summary block at the top or bottom of the review:

```
VERIFICATION TIERS APPLIED IN THIS REVIEW:
- §2 derivation: INDEPENDENTLY RECOMPUTED (algebraic checks of Theorems 1, 2, 3)
- §3 Tables 1-3: INSPECTED + INDEPENDENTLY RECOMPUTED (combinatorial columns
  recomputed; empirical columns inspected against stated inputs)
- §4 Table 4: INSPECTED only (script infrastructure not available in my environment)
- §5-10 prose: not a verification target; structural review only
```

**Tier mismatches are non-punitive failures.** A reviewer who labels tier 1 work correctly is contributing exactly the value tier 1 provides. A reviewer who labels tier 1 work as tier 3 is creating a failure mode — not because tier 1 is bad, but because the mismatch misleads downstream integrators about what has been empirically tested. When a tier mismatch is detected, the appropriate response is a private letter asking for clarification (not public confrontation), which produces either a clarification of what actually happened (possibly revealing the work was better than initially claimed, as in the Grok exchange which revealed genuine tier-2 combinatorial recomputation), or an acknowledged shorthand that can be corrected in future reviews. Either outcome is healthy.

**Applies to all reviewers.** The taxonomy applies uniformly to Opus, Grok, Copilot, Sonnet, ChatGPT, and any additional AI reviewers added to the cycle. Human reviewers (Thomas, future collaborators) follow the same convention when providing written reviews.

---

## 6. Transcript and History Management

### What gets captured

| Type | Where | When |
|------|-------|------|
| Raw conversation | `/mnt/transcripts/` (auto) | Every Claude session |
| Compacted summary | Top of conversation (auto) | When context compacts |
| Curated transcript | `development-transcripts/` folder | End of session or next session |
| Development narrative | `development-[S]-[N].md` | During/after paper production |
| Founders vision entries | `founders_vision.md` catalogue | During physics sessions |
| Grok/Copilot exchanges | Thomas saves manually | After each external AI session |

### Curated transcript format

```markdown
# [Paper] Transcript [N] — [Title]

**Session:** [AI name], [date]
**Participants:** Thomas Lee Abshier ND, [AI names]
**Context:** [What was being worked on]

---

## [Section heading — the topic being discussed]

[Curated dialogue and computation results]
[Thomas's words preserved verbatim where significant]
[AI reasoning preserved, tooling noise removed]

---

*Transcript curated by [AI], [date]*
```

### Numbering convention
- Transcripts are numbered sequentially PER PAPER across all AI sessions
- Example: SM-7_transcript_01 through SM-7_transcript_11 span multiple sessions
- If a paper emerges unexpectedly (as SM-8 did), renumber from the discovery point

### What to INCLUDE in curated transcripts

**Always include — these are the scholarly record:**
- Thomas's physical descriptions and intuitions (verbatim when possible)
- Thomas's questions that redirected the investigation
- AI reasoning chains that led to discoveries or key decisions
- Computational results (numerical values, table outputs, key formulas)
- Negative results — models that failed, with the quantitative evidence of failure
- Disagreements between Thomas and AI, or between different AIs
- "Wait, what if..." moments that changed direction
- Corrections to earlier errors (what was wrong, how it was caught)
- Decisions about paper structure, axiom formulation, or physical interpretation
- Key quotes from Grok/Copilot/Sonnet reviews and the responses to them
- The discovery arc — how one finding led to the next

**Always EXCLUDE — these are noise:**
- File system commands (`ls`, `cp`, `mkdir`, `cd`, `cat`)
- Path references and directory navigation
- LaTeX compilation output and error messages
- Python/code execution boilerplate (import statements, variable setup)
- "Please wait while I compute..." messages
- Tool invocation details (bash_tool, web_fetch, create_file mechanics)
- Formatting instructions ("make this a table", "use bold for...")
- Git commands and push/pull operations
- Session reconnection noise ("Your buffers overflowed...")
- Repeated content (if the same computation is run multiple times, keep only the final version with a note)
- Claude's internal system messages and context-management notes

**Judgment calls — include if substantive, exclude if routine:**
- Code that implements a physical model (INCLUDE the logic, EXCLUDE the boilerplate)
- Numerical output tables (INCLUDE the final results table, EXCLUDE intermediate debugging prints)
- Requests for documents (EXCLUDE "please generate the FAQ", INCLUDE "we need a document that captures X because Y")
- Thomas's instructions about workflow (EXCLUDE "save this to outputs", INCLUDE "I think we should document this because scholars will study it")

---

## 7. The Founders Vision Protocol

### When to update
- Every time Thomas describes a physical mechanism, interaction, or entity
- Every time a new structural insight emerges from computation
- Every time a negative result eliminates a physical picture
- At the END of every session that touches physics

### Format for narrative sections (Part I-V)

```markdown
### [Section number]. [Entity/Interaction name]

*Source: Thomas's description, [date] ([AI] session):*

[Thomas's physical description — paraphrased or verbatim]

[Formalisation reference: which axiom, theorem, or paper]

*[Seed questions for future sessions]*
```

### Format for chronological catalogue entries

```markdown
### [Date] — [Short title] ([AI] session)

**Context:** [What prompted this]
**Thomas's words:** "[Verbatim quote if available]"
**Key finding:** [One-line summary]
**Formalised as:** [Paper/section reference]
```

### What to capture vs. what to skip
- **CAPTURE:** Physical mechanisms, structural insights, negative results, novel physical pictures, corrections to earlier understanding
- **SKIP:** Formatting instructions, file management, compilation details, requests for documents

---

## 8. Negative Result Documentation

### Learned from SM-8/SM-9: negative results are as valuable as positive ones.

**Negative results to document:**
1. Models tested that FAILED (with quantitative results showing the failure)
2. Derivation routes attempted that didn't work
3. Conjectures tested and falsified
4. Physical pictures that seemed promising but didn't produce correct predictions

**Where to document:**
- In the relevant paper (SM-9 is entirely about negative results and open problems)
- In `founders_vision.md` catalogue with "NEGATIVE RESULT" tag
- In the development transcript with full computation details

**Example from SM-8/SM-9/SM-10:**
- Sea composition doesn't affect mass ratios (cancels when uniform)
- Additive chain-energy models fail by 65-92%
- Spectral dimension d_s ≈ 3.55 ≠ α ≈ 2.38
- φ^(3(l-1)) scaling falsified for light quark masses (PS-1)
- Pine tree fractal cascade undercounts DPs by 4-10× (SM-9 session)
- V_opp-based power laws give 23% RMS vs V's 2.1% (SM-9 session)

### Format

```markdown
### [Date] — [What was tested] — NEGATIVE RESULT

**Hypothesis:** [What we expected]
**Test:** [What we computed]
**Result:** [What we found]
**Why it matters:** [What this rules out or constrains]
```

---

## 9. Recovery Procedures

### Buffer overflow / context limit reached
1. The conversation auto-compacts — a summary appears at the top
2. A transcript file is saved in `/mnt/transcripts/`
3. In the NEW conversation:
   - Read the compacted summary
   - Read the transcript file (incrementally — it may be massive)
   - Check `founders_vision.md` and latest transcripts in outputs for what was captured
   - Ask Thomas: "What from the last session still needs to be documented?"
   - Create a continuation transcript (Part 2, Part 3, etc.)

### Lost Grok/Copilot context
- Thomas saves Grok/Copilot exchanges as Pastebin links or text files
- At next session: Thomas pastes the exchange, Opus integrates
- Key: Opus should not assume it knows what Grok/Copilot said — always read the actual text

### Session interrupted without documentation
- At the start of next session, check `/mnt/transcripts/` for the raw conversation
- Read it incrementally and produce the curated transcript
- Update `founders_vision.md` with any insights not yet captured

---

## 10. Repository Housekeeping — Reference Procedures

**Role:** This section holds the **reference-level update procedures** for each repository-level content and navigation document. It is NOT an atomic task list. The atomic post-completion task list lives at `templates/paper_completion_checklist.md`; checklist items there cite procedures here by name.

**Consolidated 20 April 2026.** Prior to consolidation, §10 carried atomic task checkbox lists that duplicated content in `operating_system.md` §4.10 and `paper_production_workflow.md` §9. Those parallel enumerations drifted — `problem_histories/` was missed from §4.10 Section C despite being present here. All atomic task content has been moved to the checklist; §10 now holds only the per-file procedures.

**When to consult this section:** while executing a specific atomic item in `paper_completion_checklist.md` that cites a procedure here. Example: checklist C2 (`axiom-registry.md`) points at the "axiom-registry.md update procedure" below.

**When to update this section:** when the procedure for updating a specific file changes (e.g., new columns in the Prediction Ledger, new format for glossary entries). When a NEW file is added to the repository's ongoing maintenance surface, both (1) add its reference procedure here and (2) add an atomic item to `paper_completion_checklist.md` Section C or D pointing at it.

**Do NOT re-introduce atomic task checkboxes here.** The consolidation exists to prevent drift.

### Content documents (update substance)

#### theory-overview.md update procedure
1. Add any new quantitative results to the "Strongest Quantitative Results" table
2. Update the "Key Formulas" reference card if new formulas were derived
3. Update "Open Problems" — move solved problems out, add new ones
4. Update "Series Status" table with new paper version and status
5. If axiom count changed, update the axiom summary

#### axiom-registry.md update procedure
1. Check: did the paper use any axiom not already in the registry? If so, add it.
2. Check: did the paper consolidate axioms (as SM-8 did with A6')? If so, update tiers.
3. **Reconcile numbering:** If multiple reviewers proposed axiom entries independently (e.g., Grok proposes A9', Copilot proposes A8' for the same principle), reconcile into a single entry. The axiom registry is the single source of truth for axiom IDs.
4. Add every new quantitative prediction to the Prediction Ledger:
   ```
   | 13 | m_t (zero-param) | 169,571 MeV | 172,760 | −1.8% | A2,A8' | SM-8 v4.1 |
   ```
5. Update the axiom count summary and axiom-to-prediction ratio
6. Add a row to the Growth Table showing this paper's contribution
7. Check if any conjectured reductions were achieved

#### master_glossary.md update procedure
1. Scan the new paper for any term not already in the glossary
2. Add each new term in alphabetical position with format:
   ```
   **Term** — Definition. [First appeared: SM-8]
   ```
3. Common sources of new terms: new physical mechanisms, new cage structures,
   new mathematical objects, new particle descriptions
4. Also check `founders_vision.md` for terms Thomas used that aren't yet defined

#### predictions.md update procedure
1. Add each new quantitative prediction:
   ```
   | SM-8-1 | m_b (zero-param) | 4,115 MeV | 4,180 MeV | −1.6% | A2,A8' | CONFIRMED |
   ```
2. Update status of existing predictions if new data or analysis changes them
3. Update the total prediction count and zero-parameter prediction count

#### postulates_and_theorems.md update procedure
**[ARCHIVED — 12 April 2026]** This file has been split into `axiom-registry.md` (axioms), `theorem-registry.md` (theorems/corollaries), and `Research_Frontier.md` (conjectures, propositions, open problems, falsified items). Update those files directly. The archived copy is at `archive/pre_frontier_2026-04-12/postulates_and_theorems.md`.

#### theorem-registry.md update procedure
1. Add each new theorem with ID, name, result, axiom dependencies, and paper reference
2. Add any new corollaries
3. Update the theorem count and theorems-per-axiom ratio
4. Update the "Open Problems Remaining" table if a theorem resolves one

#### Research_Frontier.md update procedure
1. For each problem the paper addresses: update status, "Current best lead," and "Last updated"
2. If a problem is resolved: move entry from §1 (OPEN) to §4 (Recently Resolved)
3. If a conjecture is proved: move from §2 (CONJ) to §4 (Recently Resolved)
4. If a conjecture is falsified: move from §2 (CONJ) to §6 (FALS)
5. Add any NEW problems or conjectures that emerged during the session
6. Update the dependency graph if connections changed
7. Update the problem count summary table

#### problem_histories/ update procedure
**TRIGGER:** After any session that touches an open problem — not just after papers.
1. If a history file exists for the problem: add a dated journal entry recording what was tried, what was learned, and who contributed what
2. If no history file exists and significant work was done: create one using the template in `templates/Research_Frontier_Architecture.md`
3. Capture Thomas's physical intuitions verbatim — these are the most valuable content
4. Document negative results honestly — they narrow the solution space

#### future_projects.md update procedure
1. Mark any completed projects as DONE with date
2. Update status of in-progress projects (e.g., "SM-9 v2.2 completed")
3. Add any new research targets that emerged during the session
4. Re-prioritise if the session changed what's most promising
5. **Current #1 priority (April 2026):** SM-10 FEM chain network simulation — Phase 1 (CPU proof-of-concept) can be attempted immediately

#### CPP_the_theory.md update procedure

**Cadence (adopted 11 May 2026, patch 0344):**
- **Mandatory** at v1.0 SHIP of any new paper; at any paper version that adds new theorems / chapters / open problems to the programme; at any programme-architecture event (cross-sector closure, new methodology framework, sector synthesis).
- **Optional** for intra-paper revisions (v_n.x review-cycle calibration, archival polish, wording-precision updates) when no programme-state changes occur. Batch deferred updates into the dossier-completeness closeout sequence (§15 below).
- **Backstop**: the dossier-completeness closeout sequence explicitly verifies TATWD integration before the campaign closes; deferred updates get caught there.

**Procedure (6 steps):**
1. Identify which chapter(s) the new results belong to.
2. Add the results in connected prose (not bullet points — this is the "Kindle book").
3. Update the Predictions Scorecard in Part VIII with new zero-parameter correspondences. Update the axiom-to-prediction ratio if it shifts.
4. If a new chapter is needed (new topic area, new sector synthesis, new methodology pattern), add it in the appropriate Part. Recent precedents: Chapter 22c for SS-9 conditional theorem closure (Session 35); Chapter 22d for SF-4 neutrino sector + first cross-sector closure (Session 81); Chapter 35.5 for the conditional-closure framework + cross-sector closure programme methodology (Session 81).
5. Move any resolved open problems from Part VII to the relevant chapter (preserve narrative continuity in Part VII via "RESOLVED via ... (see Chapter X)").
6. Add any new open problems to Part VII with cross-reference to the paper that registered them.

**Failure mode this procedure prevents:** forward-queueing TATWD integration at each SHIP and never executing it. SF-4 had TATWD integration listed in the post-SHIP forward queue at v1.0 / v2.0 / v3.0 / v4.0 and was not executed until Session 81's dossier-completeness closeout (patch 0343) batched all four into a single integration. The cadence-calibration above makes v1.0 SHIP integration mandatory rather than aspirational; intra-paper revisions are explicitly exempted to avoid churn.

#### bibliography/cpp_references.bib update procedure
**TRIGGER:** After any new paper is completed, or when a new external reference is cited.

**Policy (15 April 2026):** `bibliography/cpp_references.bib` is the **single master bibliography** for the entire CPP programme. All new entries — CPP papers and external works — go here and nowhere else. Per-paper and per-series .bib files are **deprecated and frozen** (legacy compatibility only). Full consolidation of the 12 legacy .bib files into the master is tracked as OPEN-WORKFLOW-1 in Research_Frontier.md.

**For new papers:**
1. Cite using `\bibliography{../../bibliography/cpp_references}` (path relative to paper's .tex location). Alternatively, embed citations inline via `\bibitem{}` inside a `thebibliography` environment — this avoids any .bib dependency.
2. Add a BibTeX entry for the new CPP paper to `bibliography/cpp_references.bib`:
   ```bibtex
   @article{abshier2026ss3,
     author  = {Abshier, Thomas Lee and {Claude Opus (Anthropic)}},
     title   = {{Uniqueness of SU(3) from the Tetrahedral Cage}},
     journal = {Hyperphysics Institute},
     year    = {2026},
     note    = {SS-3 v1.3}
   }
   ```
3. Add BibTeX entries for any external works cited in the paper to the master file.
4. Verify all cite keys match what's used in the paper's .tex file.
5. **Do NOT add entries to** `series_[name]/cpp_[series]_series.bib` or per-paper `[ID]_references.bib` files. These are frozen.

**For existing papers:** No action required. Registered papers continue to use whatever .bib they were registered with. Conversion to the master bib will be done as part of the OPEN-WORKFLOW-1 consolidation session.

#### open_problems/ update procedure
**[ARCHIVED — 12 April 2026]** The `open_problems/` directory has been replaced by `Research_Frontier.md` (dashboard) and `problem_histories/` (narratives). New problems go in `Research_Frontier.md` §1. Narrative updates go in `problem_histories/PH-[ID].md`. The archived copies are at `archive/pre_frontier_2026-04-12/open_problems/`.

### Navigation documents (update structure)

#### README.md update procedure
1. Add the new paper to the "Registered Papers" table:
   ```
   | SM-8 | Quark Generation Structure from 600-Cell Distance Shells | v4.1 | OSF pending |
   ```
2. Update the paper count ("24 papers" → "26 papers" etc.)
3. If the paper produced a headline result, add it to "Strongest Results":
   ```
   | Zero-param quark masses (RMS) | 2.1% | 4 quarks | SM-8 v4.1 |
   ```
4. If axiom count changed, update the axiom summary line
5. Add any new series-level achievements to the series table

#### INDEX.md update procedure
1. Add every new file created during this paper's production:
   - The paper itself (.tex, .pdf, .bib)
   - All 7 documentation suite files
   - Any development transcripts
   - Any new figures
2. Add files to the correct folder section in INDEX.md
3. Format: `- [filename](path) — one-line description`
4. If a new folder was created, add the folder heading

#### paper_catalog.md update procedure
1. Add one row per new paper:
   ```
   | SM-8 | Quark Generation Structure from 600-Cell Distance Shells | v4.1 | 15 pages | April 2026 | OSF pending |
   ```
2. Update the total paper count at the top

### History documents (create/update)

#### development-[S]-[N].md procedure
**TRIGGER:** Create during Phase 3 of paper production. Update throughout.
1. Follow the template in `templates/documentation-suite.md`
2. Required sections: Discovery timeline, Key decisions, Dead ends,
   Contributors and roles, Dependencies on other papers
3. This is the "lab notebook" — keep it honest about wrong turns

#### Development transcript procedure
**TRIGGER:** At the end of each session that contributes to a paper, OR at the
start of the next session (to capture what was missed).
1. Read the raw transcript from `/mnt/transcripts/`
2. Curate: preserve all substantive dialogue, remove tooling noise
3. Preserve Thomas's words verbatim where they contain physical insight
4. Keep dead ends and negative results — they're part of the scholarly record
5. Number sequentially: `SM-8_transcript_01_opus.md`, `_02_copilot.md`, etc.
6. For comprehensive multi-session arcs: `SM-8_development_transcript_opus.md`

#### series_[name]/README.md procedure
**TRIGGER:** After any paper in that series is completed.
1. Add the paper to the series paper table
2. Update the series description if the new paper changes the series scope
3. Add any new cross-references between papers in the series

---

## 11. File Naming Conventions

### Papers
- Format: `[S]-[N]_[short_descriptive_slug].tex`
- Slug: lowercase, 3-5 words, underscores, no version number
- Same name for `.tex`, `.pdf`, and `.bib` files
- Examples:
  - `SM-6_lepton_mass_spectrum.tex`
  - `SM-8_quark_generation_600cell_shells.tex`
  - `SM-9_scaling_exponent.tex`
  - `SM-10_chain_network_FEM.tex`
  - `SS-5_light_nuclei_open_vertex_cascade.tex`
  - `SS-7_alpha_cluster_edge_formula.tex`
  - `SS-8_interstitial_neutron_2EV_scaling.tex`

**Enforcement reminder.** This rule is checked at first file-creation, not after. Writing `SS-N_paper.tex` as a placeholder "to be renamed later" creates a rename commit that pollutes history; write the canonical descriptive filename the first time. If the final descriptive title isn't yet settled at first-draft time, pause and decide it before creating the file. (This rule was violated during SS-8 v0.1 initial drafting on 23 April 2026; the rename commit that added these SS-family examples was the correction.)

### README files — `{scope}-README.md` convention (adopted 24 April 2026)

**Format:** `{scope}-README.md` where `{scope}` is a short identifier naming the directory's purpose (e.g., `data`, `SS-8`, `series_strong`, `scripts`).

**Rationale.** Plain `README.md` is a GitHub-standard convention and has the virtue of being universally recognized. However, it has two failure modes in the CPP programme's actual workflow:

1. **Download ambiguity.** A file downloaded from a browser (common for patch review and artifact-sharing workflows) loses its folder context and arrives in `Downloads/` with a generic name; if multiple READMEs are in flight simultaneously, the OS de-duplicates them with `README (1).md`, `README (2).md` suffixes and the information trail is lost.
2. **Drag-drop misfiling.** A generic name provides no intrinsic signal about where the file belongs; drag-drop to the wrong directory is easy and has happened during actual CPP work.

The `{scope}-README.md` prefix preserves the README convention's semantic (any tool searching for `*README*` still finds it, and GitHub's web interface still auto-renders files with `README` in the name) while adding context that travels with the file when it leaves its directory. This matches the paper-filename pattern (`SS-8_interstitial_neutron_2EV_scaling.tex` rather than `paper.tex`) — filenames should carry their own context.

**Cost acknowledged.** GitHub's web interface treats plain `README.md` slightly specially: when browsing a directory on github.com, the unprefixed `README.md` is auto-displayed beneath the file listing. A `{scope}-README.md` still renders, but requires a click. This cost is small because CPP readers primarily navigate via local file explorer and text editor, not casual GitHub browsing.

**Examples:**
- `series_strong/data/data-README.md` — documents external data dependencies for the Strong Sector series (the first file created under this convention, 24 April 2026).
- `series_strong/series_strong-README.md` (candidate rename) — currently named `series_strong_README.md`; underscore-vs-hyphen normalization deferred to the README-cleanup patch (see "Retroactive normalization" below).
- `series_strong/papers/SS-8/SS-8-README.md` (candidate rename) — currently `README.md`; to be normalized.

**Format details:**
- Hyphen between scope and "README" (not underscore).
- `README` is uppercase (matching GitHub ecosystem convention).
- `.md` extension.
- Scope identifier uses the same conventions as the directory name itself (snake_case or SS-N style, as appropriate to the directory).

**Retroactive normalization.** The CPP repository contains existing README files using three inconsistent conventions: plain `README.md`, `{scope}_README.md` with underscore, and `README-{scope}.md` with leading-README format. A programmatic decision and cleanup patch will normalize all existing READMEs to the `{scope}-README.md` convention at a future session; this is not a forcing priority since content is unaffected, only filenames.

**New READMEs** created from 24 April 2026 onward use the `{scope}-README.md` convention from creation. Writing a plain `README.md` as a placeholder "to be renamed later" creates exactly the rename-commit-pollution failure mode this convention is designed to avoid.

### Version management
- **ONE file per paper, overwritten with each revision.** Git history preserves all versions.
- The `.tex` header contains a CHANGELOG block documenting each version.
- The development transcript documents WHY each version changed.
- Do NOT create `SM-8_v1.tex`, `SM-8_v2.tex`, etc. — this creates clutter and confusion.
- **Exception:** If a revision fundamentally changes scope, archive the old version in `archive/` with a note.
- To recover an old version: `git log [filename]` then `git checkout <hash> -- [filename]`

### Version number nomenclature (adopted 19 April 2026)

CPP papers use standard semantic-version-style labels to communicate maturity:

| Label | Meaning | When applied |
|-------|---------|--------------|
| **v0.1** | Initial preliminary draft, exploratory, may change substantially | First compile of a new paper |
| **v0.2, v0.3, …** | Pre-review minor revisions (correctness fixes, clarifications) | Author-side polish before any external review |
| **v1.0** | First "release" version | After at least one round of external review (ChatGPT, Copilot, Grok, or Sonnet) has been integrated |
| **v1.1, v1.2, …** | Post-release minor revisions (bug fixes, small corrections, clarifications) | Small changes that don't reshape the paper's claims |
| **v2.0** | Major revision | Substantive new content, reframing, or mechanism change |

**Rule:** A paper that has passed external review and integrated referee feedback is at least v1.0. A paper that has not yet been reviewed is at most v0.x. Staying at v0.x indefinitely obscures paper maturity from future readers; promote to v1.0 once the first review cycle closes.

**Grandfather clause:** Papers already labeled with non-standard version numbers (SS-5 v6, SM-8 v4.1, SS-3 v1.3, etc.) will be relabeled during the comprehensive programme-wide polish pass. The convention above applies to all papers started from 19 April 2026 onward.

### Commit cadence (adopted 22 April 2026)

Commit triggers are decoupled from version milestones. The principle is **production first, batch housekeeping at natural seams**.

Two valid commit triggers:

1. **Section-end batch.** When a discrete target within a paper is complete (e.g., "D1 SSV-minimization attack," "SM-11 lattice-scale grounding," "nuclear-scale companion suite"), batch-commit all artifacts produced in that attack as a single coherent commit. The commit message names the section and what was delivered.
2. **Context-pressure preservation.** When a context window is approaching its boundary and substantive work on disk has not yet been committed, commit before compaction. This is not optional: transcript summaries are lossy (specific numbers, exact wording, and registry statuses get abbreviated or extrapolated), whereas committed files are verbatim. Anything that would hurt to reconstruct from a summary must be committed before the summary happens.

What is explicitly **not** a commit trigger:
- Reviewer-cycle settlement on a sub-deliverable. A single reviewer round closing does not by itself justify a commit; if the work is mid-attack it stays on disk until the attack completes or context pressure forces the commit.
- Version milestones (v0.1 → v1.0) in isolation. The paper-completion checklist still runs at v1.0 (see `paper_completion_checklist.md`), but commits have already happened at section-ends; v1.0 is a Tier M milestone with its own documentation expectations layered on top of the existing commit record.

Commit message convention for section-end batches:
- Title: `[series/paper] [section name] — [one-line deliverable summary]`
- Body: bullet list of files added/modified, with one-line purpose each; cross-reference to any opened or resolved OPEN-SS problems; note any registry implications pending ratification.

This rule supersedes the prior implicit convention that archival happened only at v1.0. The v1.0 documentation suite remains the canonical Tier M milestone for paper-level external use; the section-end commit cadence runs beneath it to preserve work continuously.

### Context-pressure preservation checklist

**Promoted to §15 Session-close Handover Protocol (24 April 2026, per OPEN-ORG-008 resolution).** The four-item checklist that previously lived in this subsection — covering curated development transcript, registry updates pending ratification, reviewer response artifacts, and protocol/operating-system updates — has been relocated to top-level §15 to make it visible from the table of contents and from the §1 Quick Start command vocabulary. The trigger is unchanged: at context-pressure threshold (≥70% context consumed) or before any planned session end, the four-item sequence runs.

**The commit-cadence linkage holds.** The "context-pressure preservation" trigger in the commit cadence rule above (item 2) fires the §15 protocol. The two are interlocked: commit cadence says "commit before compaction"; §15 specifies what must be committed and in what form. See §15 for the canonical procedure and the user-/Claude-initiated dual-trigger mechanism.

### Intermediate registry-suite triggers (adopted 22 April 2026)

The v1.0 paper-completion checklist triggers the full 7-file documentation suite. Two *intermediate* registry-suite triggers exist beneath v1.0:

1. **Substantial section-end with registry implications.** When a section-end commit (per commit-cadence rule) opens or partially resolves OPEN-SS problems, the following registry files must be checked for updates before the next session: `Research_Frontier.md` (new problems), `problem_histories/PH-*.md` (partial resolutions), paper's own `[paper].tex` CHANGELOG header (if the paper exists yet). If any are not updated, flag as "pending" in the section-end commit message.
2. **Context-pressure crossing.** The §15 Session-close Handover Protocol four-item checklist (formerly in this section, see back-pointer above) includes registry updates as one of its four required items. This is an intermediate trigger independent of v1.0 milestone.

These intermediate triggers prevent registry drift between the full v1.0 documentation-suite events, which can be weeks or months apart during exploratory development.

### Staging/scratch files
- Files like `SM-8_integration_items.md` (work-orders collecting items to integrate elsewhere) should be moved to `archive/` once all items are integrated.
- Do not leave completed staging files in `papers/`.

### Documentation suite
- `[type]-[S]-[N].md`
- Example: `mechanism-SM-8.md`, `reviews-SM-8.md`, `keywords-SM-9.md`

### Transcripts
- `[PAPER]_transcript_[NN]_[ai_name].md`
- Example: `SM-7_transcript_09_opus.md`
- Comprehensive: `SM-8_development_transcript_opus.md`

### Infrastructure
- Descriptive lowercase with underscores: `founders_vision.md`, `theory_overview.md`

### Per-paper subfolder convention (adopted 22 April 2026)

Papers whose development begins on or after 22 April 2026 use a per-paper subfolder under `series_[name]/papers/`, rather than the flat-file convention used by earlier papers. The structure is:

```
series_[name]/papers/[PAPER-ID]/
├── README.md                            ← folder overview + transition notes
├── [PAPER-ID]_paper.tex                 ← the paper (canonical filename, no version suffix)
├── [PAPER-ID]_paper.pdf                 ← current build
├── reviews/                             ← verbatim reviewer correspondence
│   ├── round1_[reviewer].md             ← one file per reviewer per round per target
│   ├── round2_[reviewer]_on_[target].md
│   └── README.md                        ← catalog of reviews by round/reviewer/target
├── letters/                             ← Claude Opus correspondence
│   ├── [PAPER-ID]_[round]_review_request.md
│   ├── [PAPER-ID]_[round]_synthesis_letter.md
│   └── [PAPER-ID]_correction_letter_to_[reviewer].md
├── sketches/                            ← derivation notes, findings, exploratory analyses
├── scripts/                             ← Python verification scripts
├── founders_voice/                      ← Thomas's recorded intuitions and organizational notes
└── documentation_suite/                 ← the paper's companion documentation (three-file handover + the 7-file suite)
    ├── handover-[PAPER-ID].md           ← session-continuity state (bounded snapshot)
    ├── development-[PAPER-ID].md        ← session-by-session vignettes (append-only, never retroactively edited)
    ├── transcript-[PAPER-ID].md         ← transaction-indexed pointer-map (optional)
    ├── mechanism-[PAPER-ID].md          ← 7-file suite files — added progressively from first to v1.0+
    ├── glossary-[PAPER-ID].md
    ├── phenomena-[PAPER-ID].md
    ├── philosophy-[PAPER-ID].md
    ├── reviews-[PAPER-ID].md
    ├── keywords-[PAPER-ID].md
    └── FAQ-[PAPER-ID].md
```

**Lazy folder creation.** Do not create subfolders that have no content yet. A brand-new paper with only a sketch has `sketches/` and nothing else. `documentation_suite/` is created as soon as the first suite file is written — typically `handover-[PAPER-ID].md` at the first session close.

**What goes in `founders_voice/`.** Thomas's organizational vision for the paper, gedanken experiments, pattern-recognition intuitions, decisions about structure and presentation, recorded verbatim or as he provides them. This is analogous to `letters/` for Claude and `reviews/` for external reviewers: it captures the founder's voice as a first-class artefact class of the paper's development record. Contributions may be occasional — Thomas does not need to produce a founder's-voice entry for every session.

**Transition rule for existing papers.** Papers that existed before 22 April 2026 remain in the flat `series_[name]/papers/` layout. Do not migrate them unless a specific reason arises (e.g., the flat layout becomes unmanageable, or the paper is reopened for substantive revision). When migrating, use `git mv` to preserve history; update every cross-reference.

**First paper using this convention.** SS-8 — see `series_strong/papers/SS-8/` for the reference layout.

**Why the change.** The flat convention was shaped by the prior workflow in which Thomas alone moved files from Downloads into the repo; ergonomic considerations favoured a single destination directory. Under the Git-Bash-Patch workflow (see §13), Claude generates files directly in the sandbox and patches them into the repo, so folder depth imposes no ergonomic cost. Subfolders then become a clean win: they separate artefact classes with different maintenance rhythms (reviews are append-only, sketches iterate, the paper .tex overwrites in place), they make review archives discoverable without markdown-noise flooding, and they let the per-paper workspace scale as more reviewer rounds accumulate.

### The three-file documentation-suite convention (adopted 22 April 2026)

Within `documentation_suite/`, three files serve distinct session-continuity purposes and must not be merged. Their behaviors differ by design:

**`transcript-[PAPER-ID].md` — transaction-indexed pointer-map.** An ordinal-numbered index of every substantive transaction in the paper's development history. Each entry: three-digit transaction ID (e.g., `001`, `002`), date, one-line description, pointer to the artefact that holds the verbatim content (a file in `reviews/`, `letters/`, `sketches/`, `founders_voice/`, or `scripts/`). The transcript is a roadmap, not an archive — the substantive content lives at the pointer targets. Append-only as new transactions occur.

**`development-[PAPER-ID].md` — session-by-session vignettes.** A chronological sequence of session summaries, each written at the session's end, preserving the texture of what that session believed at that moment. Append-only. **Never retrospectively edited.** If a later session proves an earlier session's framing wrong, the later session's vignette records the correction; the earlier vignette stays as written. This preserves in-moment honesty — a decision that looked weird at the time and turned out to be right should be recorded as it was thought, not prettified in hindsight. A compact leading table tracks vignettes by date and one-liner.

**`handover-[PAPER-ID].md` — bounded current-state snapshot.** The prospective operational document for the next Claude context window. Names the active paper, current state, queued open items with priority ordering, pending registry ratifications, and pointers to substantive artefacts. Ruthlessly short: a few hundred lines max. Replaced (not appended to) at each session close; old handover content moves into `development-[PAPER-ID].md` as a vignette.

**Division of labor.** The test that tells the three files apart:
- If the content is **verbatim and substantive**, it goes in a standalone artefact (`reviews/`, `letters/`, `sketches/`, `founders_voice/`, `scripts/`), and the three documentation-suite files point at it.
- If the content is **retrospective narrative about the paper's lineage written in-moment**, it goes in `development-[PAPER-ID].md`.
- If the content is **forward-looking state for the next session**, it goes in `handover-[PAPER-ID].md`.
- If the content is **a transaction identifier to be referenced later**, it goes in `transcript-[PAPER-ID].md`.

**No crystallization point.** The documentation-suite files have no "completion" state. v1.0 is a milestone of external-readiness, not finality; post-v1.0 revisions (reviewer feedback, OSF reader feedback, public feedback, programme-level discoveries that affect the paper's framing) are expected and their treatment is identical to pre-v1.0 revisions. The documentation suite tracks these continuously. The seven narrative companion files (`mechanism-`, `glossary-`, `phenomena-`, `philosophy-`, `reviews-`, `keywords-`, `FAQ-`) are built progressively from the first section-end forward, not heroically at v1.0; incremental authorship keeps rationales fresher than retrospective writing does.

**Post-publication feedback.** External feedback that arrives after OSF registration (reader emails, social-media engagement, experimental results bearing on predictions, citations-by-criticism) is filed in `reviews/` alongside pre-publication reviewer correspondence. The content type is the same; only the source and timing differ. Keeping it in one folder ensures a future researcher finds all external voices on the paper in one place.

### Documentation continuity — the three hierarchies (adopted 22 April 2026)

CPP maintains three separate documentation hierarchies that drift if not updated continuously. Every session that produces substantive content must ask: "Does any file in any of these three hierarchies need an update?" If yes, the update rides in the same patch as the substantive work.

**Hierarchy 1 — Per-paper documentation suite.** Files in `series_[name]/papers/[PAPER-ID]/documentation_suite/` for papers using the per-paper subfolder convention, or files at `series_[name]/papers/` for legacy-flat papers. These are updated at each session close (handover and development files specifically) and at section-ends (other suite files as relevant).

**Hierarchy 2 — Programme-level registry.** Files at `/CPP` root: `axiom-registry.md`, `theorem-registry.md`, `Research_Frontier.md`, `predictions.md`, `master_glossary.md`, `founders_vision.md`, `theory-overview.md`, `paper_catalog.md`, `future_projects.md`, `CPP_the_theory.md`, `postulates_and_theorems.md`, `propositions.md`, `solution_candidates.md`, `README.md`, `INDEX.md`. Updates are triggered by: new theorems or corollaries (theorem-registry), new axioms (axiom-registry), new or resolved open problems (Research_Frontier), new predictions (predictions), new terminology (master_glossary), new Thomas-voice intuitions (founders_vision), etc. A subtantive section-end commit should sweep these files — even if no update is needed, the check itself prevents drift.

**Hierarchy 3 — Templates and conventions.** Files in `templates/`: `operating_system.md`, `relationship_protocol.md`, `AI_team_expectations.md`, `paper-formatting.md`, `documentation-suite.md`, `paper_production_workflow.md`, `paper_completion_checklist.md`, `nomenclature.md`, `Research_Frontier_Architecture.md`. Updates are triggered when the session identifies a new workflow pattern, failure mode, or team convention. New rules that won't reach the next session unless committed belong here.

**Update discipline.** The bootup, section-end, and handover moments all trigger the three-hierarchies sweep. If a session identified a registry-relevant result and failed to update Hierarchy 2, or identified a protocol pattern and failed to update Hierarchy 3, that's a failure mode for `AI_team_expectations.md` §2 (Claude Opus), not a neutral state. Per Thomas (22 April 2026): "There are no sacred cows; everyone depends on everyone, and we can't get better without knowing the results of our actions."

---

## 12. The AI Team: Roles and Specialties

### Claude Opus (primary)
- **Strengths:** Deep computation, physical reasoning, paper drafting, integration of multi-source input, long-context work, honest negative-result reporting
- **Limitations:** Can lose track in very long sessions (buffer overflow), may over-optimise for elegance at expense of honesty
- **Best used for:** Discovery sessions, paper drafting, computation, transcript curation

### Grok (xAI)
- **Strengths:** Independent numerical verification, fresh theoretical perspectives, willingness to contribute novel results (not just review)
- **Limitations:** Needs full context via Pastebin/URL (no persistent memory of CPP)
- **Best used for:** Verification of numerical results, independent derivation attempts, novel contributions
- **Notable contribution:** z=12 post-gap coordination multiplier (SM-8)

### Copilot (Microsoft)
- **Strengths:** Referee-grade structural review, axiom formulation, framework building, LaTeX block generation
- **Limitations:** Tends toward generality over CPP-specific physics
- **Best used for:** Paper review, axiom structure, scaling-law frameworks, anticipated criticisms
- **Notable contribution:** Physical axioms A/B, scaling law derivation framework, spectral dimension proposal (SM-8/SM-9)

### Claude Sonnet (hostile reviewer)
- **Strengths:** Finding genuine weaknesses, adversarial perspective, identifying unstated assumptions
- **Limitations:** Tends toward philosophical rejection ("this isn't real physics") rather than constructive critique; may miss the forest for the trees
- **Best used for:** Final review before OSF registration; identifying what a hostile referee would say
- **Notable contributions:** Scheme-dependence criticism (SM-8); circular-validation catch (SM-10) — the single most valuable insight across 10 reviews

---

## 13. The Git-Bash-Patch Workflow (adopted 22 April 2026)

Claude's sandbox has no push credentials to origin (by design — Anthropic's infrastructure does not hold GitHub tokens for Thomas's account). Commits authored by Claude therefore reach origin via a patch handoff rather than a direct push. The workflow is deterministic, recoverable, and preserves Claude's authorship in git history.

### The nine-step flow

1. **Discussion and analysis in chat.** Thomas and Claude work through the substantive problem. No file writes yet.
2. **Claude clones or pulls the repo into its sandbox** at `/home/claude/CPP` if not already present. Branch from `main` if the work is non-trivial.
3. **Claude drafts artefacts.** Files are created, edited, and verified in the sandbox. Claude sets the committer identity once per sandbox session: `git config user.email "noreply@anthropic.com"` and `git config user.name "Claude Opus"`.
4. **Section-end batch commit in sandbox.** When the discrete target is complete, Claude stages the artefacts and commits with a section-and-deliverable-style message (see §11 "Commit cadence" and "Commit message convention").
5. **Patch generation.** `git format-patch -1 HEAD --output=/mnt/user-data/outputs/NNNN-description.patch` (or `-N HEAD~N..HEAD` for multi-commit batches).
6. **Claude presents the patch via `present_files`.** The patch appears in Thomas's artefact panel as a download.
7. **Thomas downloads the patch** to local Downloads folder.
8. **Thomas applies the patch locally:**
   ```
   cd ~/Documents/GitHub/CPP
   git am ~/Downloads/NNNN-description.patch
   ```
9. **Thomas pushes to origin:** `git push origin main`. The commits now exist on GitHub with Claude's authorship intact.

Optional tenth step: Thomas deletes the local patch file. Not required — the commit is already on origin.

### What makes it work

- **Authorship preservation.** `git am` preserves the commit author and message exactly as Claude wrote them; Thomas appears in git history as the committer who applied the patch, not as the author.
- **Human-in-the-loop control.** Thomas can review the patch before applying, reject it, or amend it. The handoff is explicit.
- **Git-native.** No ad-hoc file copying, no manual reconstruction. Patches are the standard interchange format for disconnected git workflows.
- **Recoverable failure modes.** Every failure has a documented recovery path (below).

### Failure modes and recovery

**Baseline drift.** Patch was generated against Claude's sandbox tip X, but Thomas's origin has moved past X (perhaps Thomas made commits directly, or another session pushed first). Symptom: `error: patch does not apply`. Recovery: Claude re-pulls origin into the sandbox, rebases or regenerates the patch against the actual current tip.

**Duplicate apply.** Patch was already applied (e.g., Thomas downloaded and applied it earlier, now trying again). Symptom: `already exists in index` or similar. Recovery: `git am --skip` if the patch is definitely already in history; `git am --abort` and verify state otherwise.

**Claude's sandbox out of sync.** Claude modifies files in the sandbox against an outdated clone, not noticing that origin has advanced. Symptom: generated patch does not apply cleanly. Prevention: Claude always runs `git pull origin main` (or equivalent re-clone) at session start before any edits.

**Identity not set.** Commit is authored with the default sandbox identity, not `Claude Opus <noreply@anthropic.com>`. Symptom: git history attributes the commit to `root` or similar. Recovery: amend the commit with `git commit --amend --author="Claude Opus <noreply@anthropic.com>"` before generating the patch. Prevention: set identity as the first action in a new sandbox session.

### Standard apply-chain protocol — adopted 7 May 2026

This subsection defines the canonical procedure by which Claude-authored patches reach origin/main on Thomas's local machine. The protocol is **repo-agnostic**: it works identically for CPP, RM, and any future Claude-collaborative repo Thomas adopts. The shell function variants documented at the end of this subsection are optional convenience layers, not the primary mechanism — adoption is encouraged but not required, and Claude does not depend on them when generating apply-chain instructions.

**Environment.** Thomas runs Git Bash on Windows (MINGW64). Browser downloads land in `~/Downloads`. The home directory is `/c/Users/DrThomas` in MINGW64-speak; in normal use, `~` is the only path prefix needed.

**Repo registry.** Known Claude-collaborative repos:

| Repo  | Local path                       | Origin                                       | Used for                                |
|-------|----------------------------------|----------------------------------------------|-----------------------------------------|
| CPP   | `~/Documents/GitHub/CPP`         | github.com/Hyperphysics-Institute/CPP        | Conscious Point Physics programme       |
| RM    | `~/Documents/GitHub/RM`          | github.com/Renaissance-Ministries/RM         | Renaissance Ministries content + CVN    |
| (new) | `~/Documents/GitHub/<REPO>`      | (varies)                                     | (per-repo)                              |

When Claude works in either repo, it follows the same three-phase apply-chain protocol below; only the repo path changes. New repos added to this registry should follow the `~/Documents/GitHub/<REPO>` pattern unless Thomas specifies otherwise.

### The three-phase protocol

**Phase 1 — Sync.** Reset to origin/main and confirm baseline.

```
cd ~/Documents/GitHub/<REPO>
git checkout main
git pull origin main
```

After `git pull`, note the short SHA of HEAD — this is the baseline against which patches will apply. If `git pull` reports "Already up to date" the local main matches origin/main and apply can proceed; if it reports new commits being merged, Claude's patches were generated against a different baseline and may fail to apply (see Failure modes).

**Phase 2 — Apply.** Apply each patch in order, one `git am` per line for visibility.

```
git am ~/Downloads/<patch-1>.patch
git am ~/Downloads/<patch-2>.patch
git am ~/Downloads/<patch-3>.patch
...
```

Each line is a distinct command. The terminal echoes the commit subject after each successful application so Thomas can visually verify each patch landed. **If any `git am` fails, run `git am --abort` immediately and stop — do not proceed to Phase 3 with an incomplete apply.** A partially-applied chain leaves the working tree in a recoverable state, but pushing it would commit incomplete history to origin.

**Phase 3 — Push.**

```
git push origin main
```

After successful push, GitHub origin/main contains the new commits with Claude's authorship preserved. The apply chain is complete.

### Claude's delivery obligation

When Claude delivers a patch chain to Thomas, Claude generates the full command sequence with all paths and filenames explicit:

- `~/Documents/GitHub/<REPO>` filled in with the actual repo from the registry above (no `/path/to/REPO` or `cd /path/to/CPP` placeholders)
- `~/Downloads/<filename>.patch` for each patch, with the actual filename Claude generated
- One command per line, sequential, copy-pasteable
- Brace-expansion globs (`02{56,57,58,59,60,61}-*.patch`) acceptable for contiguous, dense ranges if Thomas prefers compactness; explicit one-per-line is the default

Claude must also state which repo the chain targets and the baseline commit it applies against, so Thomas can verify before running.

### Failure modes and recovery

**Baseline drift.** Patch was generated against a baseline that no longer matches Thomas's local origin/main. Symptom: `error: patch does not apply`. Recovery: Thomas runs `git am --abort`, reports the actual `git rev-parse HEAD` after `git pull`, and Claude regenerates the chain against that baseline.

**Duplicate apply.** A patch in the chain is already in history. Symptom: `Patch already applied` or `nothing to commit`. Recovery: `git am --skip` to advance past the redundant patch, then continue. If unclear whether a patch is already applied, abort and verify via `git log --oneline | head -10`.

**Patch file missing in Downloads.** Symptom: `git am` reports "could not open ... No such file or directory". Recovery: confirm the file is in `~/Downloads/` (not in `Downloads/Patches/` or some sub-folder; not still in browser-download "Downloads" overlay); re-run.

**Chain abort mid-stream.** If `git am` fails on patch N and Thomas runs `git am --abort`, patches 1 through N-1 are still applied locally but not pushed. Recovery: either `git push origin main` to push what landed (incomplete chain) and ask Claude to regenerate from N onward, OR `git reset --hard origin/main` to discard the partial apply and restart the full chain from a clean baseline. The latter is usually cleaner.

### Anti-patterns (Claude must not produce these)

- Generic `cd /path/to/CPP` or `cd /path/to/REPO` placeholders. These fail on copy-paste and require Thomas to mentally substitute paths every time.
- `git am NNNN-*.patch` without the `~/Downloads/` path prefix. This assumes the patches are in the working directory, which is rarely true after a fresh download.
- Ambiguous `git am *.patch` globbing. May apply unintended files; never use.
- Mixing repos in a single chain. Each chain targets exactly one repo; cross-repo work requires separate chains.
- Assuming `cpp-apply` / `rm-apply` shell functions are installed without first confirming. The protocol above does not depend on them.

### Optional convenience: shell-function wrappers

For Thomas's day-to-day use, the three-phase protocol can be compressed into a single command by installing thin shell-function wrappers in `~/.bashrc`. Adoption is optional — the manual protocol above works regardless, and Claude continues to generate the explicit three-phase form for delivery.

The recommended function set is a generic `repo-apply` plus one thin wrapper per known repo:

```bash
# Generic apply function — takes repo path as first argument
repo-apply() {
  local repo="$1"; shift
  local downloads=~/Downloads

  if [ -z "$repo" ] || [ $# -eq 0 ]; then
    echo "Usage: repo-apply <repo-path> <patch-prefix> [<patch-prefix> ...]"
    return 1
  fi

  cd "$repo" || { echo "ERROR: cannot cd to $repo"; return 1; }

  echo "=== Sync $repo with origin/main ==="
  git checkout main || return 1
  git pull origin main || return 1
  echo "Baseline HEAD: $(git rev-parse --short HEAD)"

  echo "=== Verify patches present in $downloads ==="
  local missing=0
  for n in "$@"; do
    local found=("$downloads"/"$n"-*.patch)
    if [ -e "${found[0]}" ]; then
      echo "  found:   ${found[0]##*/}"
    else
      echo "  MISSING: $n-*.patch"; missing=1
    fi
  done
  [ $missing -eq 1 ] && { echo "Aborting."; return 1; }

  echo "=== Apply patches in order ==="
  for n in "$@"; do
    echo "--- $n ---"
    git am "$downloads"/"$n"-*.patch || {
      echo "FAILED applying $n. Run 'git am --abort' to back out."
      return 1
    }
  done

  echo "=== Push to origin ==="
  git push origin main || return 1
  echo "=== Done. New HEAD: $(git rev-parse --short HEAD) ==="
}

# Thin wrappers for known repos
cpp-apply() { repo-apply ~/Documents/GitHub/CPP "$@"; }
rm-apply()  { repo-apply ~/Documents/GitHub/RM  "$@"; }
```

After installation, every CPP apply chain reduces to `cpp-apply 0256 0257 0258 0259 0260 0261` and every RM apply chain to `rm-apply <prefixes>`. New repos can be added by writing a new wrapper line.

**Recommended installation method.** The most reliable way to append a multi-line block to `~/.bashrc` is via a single-quoted heredoc, which prevents bash from expanding `$repo`, `$downloads`, etc. while writing:

```
cat >> ~/.bashrc << 'BASHRC_EOF'
[paste the function block here, including the 'BASHRC_EOF' delimiter at the end on its own line]
BASHRC_EOF
```

After saving, run `source ~/.bashrc` (on a separate prompt line, not glued to the closing brace) to activate in the current shell. The functions persist across all future Git Bash sessions thereafter.

If heredoc paste fails (Windows line-ending interaction with Git Bash is occasionally finicky), the alternative is to open `~/.bashrc` in an editor (`nano ~/.bashrc` or `notepad ~/.bashrc`), scroll to the end, paste the function block, save, and run `source ~/.bashrc`. The editor path is more robust against paste-buffer artifacts.

### Origin and rationale

Adopted 7 May 2026 after two failure modes in close succession:

1. **The placeholder failure.** SS-9 v0.8 patch chain (0256-0260) failed on first apply because Claude handed Thomas a generic `cd /path/to/CPP` template. Bash error: `cd: /path/to/CPP: No such file or directory`. The friction was recurring across sessions.

2. **The shell-function setup failure.** Initial fix proposed a `cpp-apply` shell function added via heredoc to `~/.bashrc`. The heredoc paste in Git Bash glued the closing `}` to the next command (`}source ~/.bashrc`), leaving the shell waiting for a function-body terminator that never came. The function was never defined; the apply chain didn't run.

The lesson: the protocol must work *without* depending on optional setup. The three-phase manual protocol above is the canonical procedure; shell functions are layered on top as a convenience for users who have installed them. Claude generates explicit three-phase commands as the primary delivery, and the protocol is independent of any local shell state.

The protocol is also explicitly multi-repo from the start: CPP and RM are first-class entries in the repo registry, and the same procedure applies to both.

### When to use each flow

- **Git-Bash-Patch** — structural edits, multi-file changes, new files where commit-message structure and Claude's authorship should be recorded in git history, and any case where the patch needs to encode folder structure or file-move semantics. This is the default for substantive session work and for any commit touching 3+ files.
- **Drag-drop + GitHub Desktop (for single-file drops)** — single new .tex paper files or single-file edits. Thomas downloads the file from Claude's outputs, renames to drop the `_v0.x` suffix (canonical filenames carry no version suffix; version history lives in the internal CHANGELOG), drops into the target folder via file explorer, and commits via GitHub Desktop with a sensible message. This is more ergonomic than Git-Bash-Patch for single-file cases and was adopted as the standard workflow for such cases on 24 April 2026 during the SS-8 v0.1 session. Claude still produces a format-patch as a fallback option in the same session in case Thomas prefers it, but the expectation for single-file drops is the drag-drop path.
- **Direct-file-copy (legacy)** — single-file one-off edits Thomas makes himself, when Claude's authorship is not relevant. Thomas may still use this for his own edits.
- **Claude Code (not yet in use for CPP)** — agentic-coding sessions where Claude has direct push access. Not currently configured for CPP; mentioned here for completeness.

### Commit message conventions apply

Patches inherit the commit message Claude wrote in the sandbox. Follow §11 "Commit message convention for section-end batches": title is `[series/paper] [section name] — [one-line deliverable summary]`; body is a bullet list of files changed with one-line purpose each, plus cross-references to any opened or resolved OPEN-SS problems and any pending registry ratifications.

### Relation to the per-paper subfolder convention

The Git-Bash-Patch workflow is what made the per-paper subfolder convention (§11) ergonomic. Under the prior flat-files workflow, Thomas moved files one at a time from Downloads into `series_[name]/papers/`; subdirectories multiplied the manual steps. Under Git-Bash-Patch, the patch encodes the entire folder structure and `git am` creates any missing directories automatically. Deeper hierarchy is now free.

---

### Binary artifact workflow — adopted 11 May 2026

The Git-Bash-Patch workflow handles `.tex` source files cleanly across machines, but compiled `.pdf` outputs are a separate matter. `pdflatex` produces byte-non-deterministic output (timestamps in PDF metadata, font rasterization differences across builds), so the same `.tex` source compiled on different machines produces `.pdf` files with different git blob hashes even when the content is identical. This breaks `git am` when a patch attempts to update a `.pdf` against a starting state that doesn't match the local machine's `.pdf` bytes.

The failure mode was observed at patch 0336 on 11 May 2026: SF-4 v4.1 was compiled in Claude's sandbox and committed; the resulting patch failed to apply on ClearPC because the local `.pdf` (compiled at an earlier date on ClearPC) had different bytes than the sandbox `.pdf`, even though both came from identical `.tex` source.

**Adopted convention.** ClearPC is the designated canonical compile machine for flagship paper PDFs (`flagship_papers/*/`, also `series_*/papers/`). The workflow is:

1. **Claude commits `.tex` only.** All patches generated by Claude touch source files (`.tex`, `.md`, `.bib`, etc.) but never compiled binaries (`.pdf`). Claude's sandbox may compile `.pdf` for verification (to confirm `\ref` resolution, no LaTeX errors, page count, etc.), but the resulting `.pdf` is not staged or committed.

2. **Thomas applies `.tex` patches on ClearPC** via the standard three-phase protocol (§13).

3. **Thomas recompiles `.pdf` locally on ClearPC** via the convenience script `scripts/cpp-recompile-pdf.sh`, which runs `pdflatex` twice, stages the resulting `.pdf`, commits it with an auto-generated message referencing the source HEAD, and pushes to origin.

4. **Travel machines (Surface) apply `.tex` patches and may locally verify with `cpp-recompile-pdf.sh --no-push`.** The `--no-push` flag compiles the PDF for local viewing but does not commit. Surface should never push a recompiled PDF to origin.

This separates source-of-truth (the `.tex` on origin) from the derived artifact (the `.pdf`), avoiding cross-machine binary friction while keeping the `.pdf` available in the repository for GitHub-web viewing, reviewer access, and quick visual reference.

**The recompile script.** `scripts/cpp-recompile-pdf.sh` takes a paper directory as argument:

```bash
# On ClearPC, after applying a .tex patch chain:
cd ~/Documents/GitHub/CPP
bash scripts/cpp-recompile-pdf.sh flagship_papers/neutrinos

# On Surface, for local verification only:
bash scripts/cpp-recompile-pdf.sh flagship_papers/neutrinos --no-push
```

The script runs `pdflatex` twice (for cross-reference resolution), cleans auxiliary files, stages the new `.pdf`, commits with a message of the form `"Recompile <basename>.pdf locally to match source at <short-sha> — N pages, M bytes"`, and pushes (unless `--no-push`). Exit code 2 means no commit was needed (PDF bytes match what's already tracked).

**Anti-patterns Claude must not produce.**

- Never include `.pdf` (or any compiled binary) in a Claude-generated patch. Sandbox-compiled PDFs are for verification only.
- Never instruct Thomas to apply a patch that touches both `.tex` and `.pdf`. Source patches and binary commits are separate concerns under this workflow.

**Anti-patterns Thomas should avoid.**

- Never `git commit` a recompiled `.pdf` from a travel machine. Use `cpp-recompile-pdf.sh --no-push` for local verification, or simply view the local file without committing.
- Never bypass the script and manually `git add *.pdf && git commit` after recompiling unless the script's auto-message is genuinely inappropriate (e.g., the recompile is part of a larger commit). In that case, the rationale should be in the manual commit message.

**Origin and rationale.** Adopted 11 May 2026 after patch 0336 application failure (SF-4 v4.1 `.pdf` blob mismatch between sandbox and ClearPC). Three alternatives were considered: (A) designate ClearPC as canonical compile machine (chosen); (B) use Git LFS for `.pdf` (rejected — requires LFS setup on every machine); (C) stop tracking `.pdf` entirely (rejected — preserves GitHub-web-viewable PDF for reviewer convenience). Option A is the lowest-friction solution that preserves both the source-of-truth discipline (Claude never touches binaries) and the in-repo PDF availability.

**Relation to public posting.** The in-repo `.pdf` is a working artifact for development and reviewer access. The canonical public-posting PDF lives at Zenodo + arXiv after the paper reaches v1.0-SHIP-ready state. The Zenodo/arXiv submission is generated locally on ClearPC (same as the in-repo PDF) and uploaded directly, not pulled from the repo. The two PDFs (in-repo and public) may have different bytes due to compile-time differences but will be content-identical from identical `.tex` source.

---

### Programme-level methodology references — adopted 11 May 2026

Two programme-level methodology documents capture conventions that flagship papers depend on:

- **`templates/conditional_closure_framework.md`** — programme-wide convention on conditional theorem closure, foundational input (FI) accounting, and the "RESOLVED" terminology convention. First instantiated in SF-4 v4.2 via Remark `rem:conditional_closure`; generalized to programme convention here. Every future flagship paper should produce an equivalent paper-level Remark setting the conditional-closure framing globally for its own scope.
- **`theorem-dependency-graph.md`** — programme-level theorem dependency map. Sector-organized inventory of all formal mathematical objects (theorems, propositions, lemmas, corollaries) with their inheritance and load-bearing relationships. Companion to `theorem-registry.md` (which holds the mathematical statements); this document maps the relationships between statements.

Both documents are updated at each flagship-paper SHIP or version increment that adds new formal objects or changes closure level. The update should be part of the SHIP-mechanics checklist in `templates/paper_completion_checklist.md` going forward.

---

## Appendix: Lessons Learned (April 2026)

### From SM-8
1. **Papers emerge from exploration.** SM-8 was not planned. Allow discovery sessions to produce unexpected papers.
2. **Negative results are publications.** SM-9 is entirely about what didn't work. Document failures with the same care as successes.
3. **The multi-AI team is more than the sum of its parts.** Grok's z=12 multiplier came from asking for review, not for a specific calculation. Give the team room to contribute.

### From SM-9
4. **Honest self-assessment strengthens papers.** Acknowledging that 7/3 is "partially derived" (not proven) was praised by all reviewers.
5. **The founder's voice is irreplaceable.** Thomas's stream-of-consciousness descriptions (the pine tree model, the three bonding regions, the cooperative coupling) generate every breakthrough. Capture them immediately.

### From SM-10
6. **Watch for circular validation.** Sonnet caught that comparing simulation output to formula-derived targets is circular. Always test against independent empirical data (PDG mass ratios), not model predictions.

### From the full trilogy
7. **Buffer overflows will happen.** Plan for them: keep `founders_vision.md` and transcripts current so nothing is lost.
8. **The documentation suite is scholarship.** The 7 companion files per paper, the curated transcripts, and the review records ARE the scholarly record that future researchers will study.
9. **37 files in one session is possible.** The SM-8/9/10 trilogy session produced 3 papers, 10 reviews, 21 documentation suite files, and 3 transcripts in a single sitting. The pipeline works.

---

## 14. Organizational Frontier Registry (adopted 24 April 2026)

**Registry file:** `/CPP/Organizational_Frontier.md`
**Rationale file:** `/CPP/programmatic_decisions/PD-003-organizational-frontier-registry.md`
**Parallel to:** `Research_Frontier.md` (theoretical/physics problems)

### Purpose

Captures organizational, infrastructural, and governance-level improvement items that have been identified during programme work but have not yet been acted on. Solves the chronic failure mode where "good ideas for later" degrade across session compaction, drift through repeated handover paraphrasing, or become irretrievable when the underlying failure mode recurs in future sessions.

### The reflexive-drop protocol

When an organizational improvement idea surfaces during active work (paper drafting, infrastructure building, review cycles), do **not** act on it immediately (scope disruption) and do **not** carry it in session memory (compaction loss). Instead:

1. **Stop for 60–90 seconds.**
2. **Open `Organizational_Frontier.md`.**
3. **Add an `OPEN-ORG-NNN` entry** using the template in §2 of that file. Full fidelity: originating context, problem description, proposed fix, trigger condition, blocking dependencies, history.
4. **Commit** (immediately, or stage for the next batched commit).
5. **Return to current work.**

The attention loop closes at step 5; the preservation loop was closed at step 3–4. The idea survives compaction because it's in a committed file, not in active session memory.

### Trigger-condition types

Each entry specifies when it becomes workable. Five trigger types are recognized:

1. **Between-paper execution.** Workable in any session where no paper-drafting is actively in flight and no higher-priority OPEN-ORG item is queued ahead.
2. **Threshold-triggered.** Fires when programme state crosses a specified threshold (e.g., `operating_system.md` exceeds ~1500 lines).
3. **Opportunistic / combine-with.** Executes combined with some other work that's going to happen anyway (e.g., SS-7 script refactor combined with SS-7 subfolder migration).
4. **Milestone-triggered.** Fires when the programme reaches a specified milestone (e.g., swarm-tally header required before SS-9 drafting).
5. **Next-session.** Execute at the next available opportunity. Used sparingly, only when recurring friction makes deferral costly.

### Session-close handover protocol

The "Pending for next session" list at each session close **no longer carries content** for organizational items. Instead, it points at the registry:

> OPEN-ORG registry current as of this session. Newly registered this session: OPEN-ORG-{X}, OPEN-ORG-{Y}. Became workable this session but deferred to time constraints: OPEN-ORG-{Z}. Next session should scan registry against current state to identify workable items.

The content lives in `Organizational_Frontier.md` (durable, version-controlled, searchable). The handover is a short pointer. This eliminates the paraphrase-drift failure mode where pending items get restated slightly differently each session until they detach from original intent.

### Signals that reflexive-drop is warranted

The following phrases, when they arise during session work, are signals that an organizational item is about to be carried in session memory instead of durable infrastructure. The correct response is always: register, return.

- "We should eventually X"
- "This is a good idea but out of scope now"
- "Noting this for later"
- "Future Opus should Y"
- "At some point we need to Z"
- "Flag for the next session"
- "I'll mention this in the handover"

Each of these uttered in a session is a reflexive-drop cue. Cost: 60–90 seconds. Benefit: elimination of degradation risk.

### Maintenance cadence

- **Scanned at each session start** against current programme state. Items whose triggers have fired are candidates for the session slot (if any slot is available).
- **Scanned at each paper's v1.0 completion milestone** alongside `Research_Frontier.md`. Workable items get queued; completed items get moved to §3 (Resolved) of the registry file with resolution-date and commit reference.
- **Scanned when a new entry is added** to check for duplication or relationship with existing entries.

### Meta-discipline: this file is itself registry content

If, during future sessions, this §14 needs updating (new trigger types, refined protocols, clarifications), the update itself may be registered as an OPEN-ORG item rather than implemented inline. The registry holds itself to the same discipline it asks of other programme work.

---

## 15. Session-close Handover Protocol (promoted to top level 24 April 2026)

**Purpose.** Specifies the procedure that runs when a session is approaching its end — whether due to context-pressure crossing, planned session close, or substantive milestone completion — to ensure that no narrative, registry, reviewer, or protocol artifact is lost to compaction. This section was promoted from a buried subsection of §10 to top-level visibility per OPEN-ORG-008 resolution, after a 23–24 April 2026 SS-8 v0.2 session demonstrated the failure mode where the protocol existed on paper but did not fire because Claude could not reliably self-monitor and the procedure was not in Claude's active working set during substantive work.

### Dual-trigger mechanism

The protocol fires on either of two triggers, by design redundant. Self-monitoring of context consumption by Claude has proven unreliable; the dual-trigger discipline moves the fire-decision to observable signals.

**Trigger 1: User-initiated (canonical).** When Thomas says any of the following, Claude immediately begins the four-item preservation sequence below regardless of what else is in flight:

- "please execute handover protocol"
- "execute handover protocol"
- "execute handover"
- "handover protocol"
- "run the handover"
- Any minor variant carrying the same intent

This is the authoritative trigger. Thomas can reliably detect when he is approaching session-close readiness; this moves the fire-decision to the reliable sensor. The phrase functions as a hotkey — unambiguous, short, memorable.

**Trigger 2: Claude-initiated prompt on workflow-shape signals.** When Claude notices any of the following workflow-shape patterns during a session, Claude immediately asks Thomas: **"Do you want to initiate handover protocol?"** This is a prompting discipline, not an auto-fire — the decision still belongs to Thomas, but the opportunity to fire does not get missed because Claude was absorbed in the work itself.

Workflow-shape signals that warrant the prompt:

- Substantive milestone just completed (v1.0 paper shipped, major registry update committed, multi-step infrastructure landed)
- Long session duration (multiple hours of dense work, multiple commits to origin)
- "We've done a lot today" / "good stopping point" / "ready to close" / "this is a good place to stop" — uttered by Thomas
- Claude itself observing that "the session has reached a natural seam" or similar
- Any topic-shift cue suggesting the substantive work is winding down

Note: these overlap with but are distinct from the §14 reflexive-drop signals. The §14 list catches *individual organizational ideas* that should be registered immediately; this §15 list catches *whole-session shape changes* that warrant the four-item preservation sequence. When a workflow-shape signal fires, Claude prompts; if Thomas confirms, the four-item sequence below runs.

### The 8-step handover sequence

When the protocol fires (by either trigger), execute these eight steps **in order**. Each step has explicit completion criteria. Steps that are N/A this session are explicitly marked "N/A" in the Step H paste-ready handover document for audit-trail completeness — never silently skipped.

The sequence is mandatory because the failure mode this protocol addresses is *partial firing*: completing some items but not others, leaving the next session with a fragmented handover that has to be reconstructed from distributed sources. Sequencing converts the discipline from "verify these four artifacts exist" into "execute these eight operations." The failure rate of the latter is materially lower because each operation has a definite trigger and a definite completion check.

#### Step A — Tier 1: Session Log Entry / Addendum

Append a Template-A or Template-B entry to the active session log file (typically `session_logs/[YYYY-MM-DD]_session_log.md`) covering the substantive work of the current session. If the session produced multiple substantive phases (each with its own deliverable), each phase gets its own entry. If the session reached a clean close that re-evaluated earlier phase decisions (e.g., a register-and-defer reversal, a same-session resolution), append a session-close addendum entry.

Completion criterion: every substantive phase in the session has a corresponding session-log entry; the file is committed.

#### Step B — Tier 2: Transcript Pointer-Map Additions

Append numbered transaction entries to `series_<name>/papers/<ID>/documentation_suite/transcript-<ID>.md` (or to a cross-paper transcript at `session_logs/transcript-cross-paper.md` for non-paper-scoped work) covering each substantive transaction in the session. Each entry is a single line in the format:

```
- `NNN` <date> Session N <phase descriptor> — <brief substantive description> → `<file path or §-pointer to artifact>`
```

Continue numbering from the previous highest transaction number. The transcript file is *empty of substance*; substance lives at the pointer targets. The pointer-map gives the chronological index.

Completion criterion: every substantive deliverable in the session (sketch §, computation result, registry update, decision arc, verdict) has a numbered pointer entry; the file is committed.

#### Step C — Tier 3: Development Vignettes

For paper-scoped work, append a curated paragraph-form vignette to `series_<name>/papers/<ID>/documentation_suite/development-<ID>.md` summarizing the session's work in finished prose (1–3 paragraphs per vignette, occasionally up to 5 for complex multi-phase sessions). For sessions producing multiple substantive phases, each phase typically gets its own vignette. Vignettes are append-only across sessions; they accumulate as the paper develops.

Completion criterion: vignette(s) covering the session's substantive work are appended; the file is committed. **N/A for sessions that produced no substantive paper-scoped reasoning** (e.g., pure infrastructure or organizational sessions) — explicitly mark N/A in Step H.

#### Step D — Tier 4: Verbatim Opus Reasoning Narrative

Append session reasoning entries to `series_<name>/papers/<ID>/documentation_suite/reasoning-<ID>.md` in the format established by prior session entries (Title with one-paragraph summary; Tier 4 inclusion scope; Strategy; technical sections; Findings; Verdict; State at session close; Forward-looking pointers). For multi-phase sessions, each phase is its own entry. **Tier 4 is the canonical record.** Tiers 1, 2, and 3 are derived from it.

What goes in Tier 4 (and what is excluded as housekeeping) is specified in §4 Four-Tier Documentation Discipline. Briefly: included are multi-paragraph reasoning turns where Opus is doing analysis, testing a hypothesis, working through an argument, articulating a structural observation, considering alternatives, revising an earlier framing, flagging uncertainty, pushing back on a framing, or otherwise engaging in substantive theoretical or methodological work. Excluded are tool-call narration, status confirmations, procedural housekeeping, tool-output narration, and verbatim quotations from existing repository files.

Completion criterion: Tier 4 entries covering the session's substantive reasoning are appended; the file is committed. **N/A for sessions that produced no substantive paper-scoped reasoning** — explicitly mark N/A in Step H.

#### Step E — Registry Updates (each registry independently audited)

**TATWD integration audit** (adopted 11 May 2026, patch 0344): As a final step of registry-update audit, verify that `CPP_the_theory.md` (TATWD) has been integrated for any v1.0 SHIPs or programme-architecture events that landed during this session's work or in unresolved forward-queue items. The cadence specified in §10 makes TATWD integration mandatory at v1.0 SHIP and at programme-architecture events; if the integration was deferred (e.g., for intra-paper revision sequences), the dossier-completeness closeout sequence is where the catch-up happens. Check the `Last updated` header of `CPP_the_theory.md` against `paper_catalog.md`'s `Last updated` header — if the TATWD header is older than the most recent v1.0 SHIP or architecture event in paper_catalog, TATWD update is required before declaring the session-close handover complete.

The Session 81 patch 0343 closeout that batched SF-4 v1.0 → v4.4 TATWD integration in a single update is the precedent for "delayed batch" cases. With the §10 cadence calibration in force, future delayed batches should not accumulate past one or two paper revisions before integration.



Walk each of the following registries; for each, either update with the session's findings or explicitly mark N/A:

- **`Research_Frontier.md`** — update the relevant OPEN-SS-NN / CONJ-SS-NN entry with the session's paragraph; if the session resolved or falsified a problem, change status accordingly and move to the resolved/falsified section.
- **`Organizational_Frontier.md`** — register any new OPEN-ORG-NNN items surfaced this session (using the §1 register-and-defer pattern); update status of any existing items moved this session; move resolved items to §3 per registry convention.
- **`axiom-registry.md`** — register any new axioms; update prediction counts if predictions were closed.
- **`theorem-registry.md`** — register any new theorems with axiom dependencies; update theorem count.
- **`predictions.md`** — register any new quantitative predictions with PDG comparison; update status of existing predictions if confirmed/falsified this session.
- **`future_projects.md`** — update prioritised research targets with status; this is the **after-each-session** cadence file (per `bootup.md` §5), so this almost always has a non-N/A update for any session producing forward-looking pointers.
- **`problem_histories/PH-*.md`** — update narrative history for any major open problem (OPEN-SS-NN with status arc) substantively touched this session.
- **`master_glossary.md`** — add new terms if any were coined this session.
- **`paper_catalog.md`** — refresh active-paper rows whose status text is now stale (typically every 3–5 sessions of active development).

Completion criterion: each registry has either been updated or explicitly marked N/A in Step H. **Each registry must be audited independently** — bundling them as "registry updates done" without per-registry verification is the failure mode that registry drift accumulates from.

#### Step F — Reviewer Response Artifacts

If the session generated review content (reviewer letters received, correction letters issued, synthesis letters to reviewers, multi-AI exchange transcripts), commit these in full verbatim form to the paper's `letters/` and/or `reviews/` folders. Summaries of reviewer content are particularly lossy because specific language and line-citations are the review's substance, not decoration.

Completion criterion: all reviewer artifacts committed verbatim, or explicitly marked N/A in Step H.

#### Step G — Protocol / Operating-System Updates

If the session identified a new protocol case (e.g., updates to `relationship_protocol.md`), a new operating-system rule, a new programmatic-decision warranting codification (PD-NNN), or any procedural refinement (including refinements to this §15 itself), write the update into the appropriate file before compaction. Do not leave codification for "next session" — next session starts from a lossy summary and will not remember the specific reasoning that produced the rule.

Completion criterion: protocol/OS updates committed, or explicitly marked N/A in Step H.

#### Step H — Paste-Ready Handover Document (the canonical session-close artifact)

Create or overwrite `series_<name>/papers/<ID>/documentation_suite/handover-<ID>.md` (for paper-scoped work) or `session_logs/handover-current.md` (for cross-paper / methodological work) with a concentrated 80–120 line forward-looking orientation document. The paste-ready handover is **the single artifact the next session reads first**; it is designed to be pasted directly into the new context window's opening message after Thomas's bootup command, giving the next Opus instance a complete one-page state-of-the-programme without requiring synthesis from distributed sources.

The handover document follows this structure:

```markdown
# [Paper-ID] Handover — Session [N] Close ([Date])

**Repository state:** origin/main at commit `[hash]`, patch [highest-NNNN] highest.
**Active paper(s):** [Paper-ID] ([title or working title]). [Pre-paper / In-development / v0.x active / Trigger 2 pending / etc.]

## One-paragraph state

[Concise prose paragraph: what the paper is about, what state it's in, what the most recent session(s) produced, what the active investigation is. ~6-10 sentences.]

## Forward queue

**Priority 1:** [highest-priority next-session work, with sharpness markers if applicable]
**Priority 2:** [second]
**Priority 3:** [third or "deferred"]
**Priority 4:** [parallel or low-priority items]
**Anti-priorities:** [explicit "do not do X until Y"]

## Where to find detail

- **Last session log entry:** `session_logs/[file].md` §"[entry title]" lines [start–end]
- **Latest Tier 4 reasoning:** `series_<name>/papers/<ID>/documentation_suite/reasoning-<ID>.md` §"[latest entry title]"
- **Active sketches:** [paths]
- **Active scripts:** [paths]
- **Live registry entries:** `Research_Frontier.md` §[OPEN-SS-NN], `Organizational_Frontier.md` §[OPEN-ORG-NNN] [if any active]

## Step-by-step audit of this session's handover

- Step A (Tier 1 session log): ✓ / N/A — [brief note]
- Step B (Tier 2 transcript): ✓ / N/A — [transactions NNN–NNN appended]
- Step C (Tier 3 vignette): ✓ / N/A — [vignette N appended]
- Step D (Tier 4 reasoning): ✓ / N/A — [entries for phases X, Y, Z appended]
- Step E (registries): [per-registry ✓ / N/A list]
- Step F (reviewer artifacts): ✓ / N/A — [brief note]
- Step G (protocol/OS updates): ✓ / N/A — [brief note]
- Step H (this document): ✓ — file at [path]

## Recent session count

[1–2 lines: cumulative patches landed, programme-level milestones since paper creation]

## Quick-start for next session

1. Paste this handover into the opening message of the new context window (or attach as the opening human message).
2. Bootup as usual: `git clone https://github.com/Hyperphysics-Institute/CPP.git && cd CPP` + read `bootup.md`.
3. Default action: execute Priority 1 above, unless Thomas redirects.
```

Completion criterion: handover-[ID].md (or handover-current.md) is created/overwritten and committed; ALL Step A–G items are explicitly accounted for in the audit table (✓ or N/A with brief note); the file is paste-ready (no in-text references to "see chat above" or similar context-window-bound language).

The handover document is **always produced**, even when the bulk of preceding steps are N/A. A pure-infrastructure session still produces a handover document with most steps marked N/A and the paste-ready summary covering what the next session needs.

### Reconciliation with §4 Four-Tier Documentation Discipline

The 8-step sequence above incorporates the §4 Four-Tier Documentation Discipline directly into Steps A–D. The previous §15-vs-§4 reconciliation paragraph is superseded: there is no longer a separate "session log replaces handover" rule for in-progress work. Both are produced — Step A produces the session log entry, Step H produces the paste-ready handover document. Step H is the new canonical "first artifact next session reads," replacing both the legacy `handover-[S]-[N].md` artifact (for in-progress papers) and the legacy "session log IS the handover" rule (for cross-paper work). For Trigger 2 paper-completion cycles, the documentation suite (mechanism/glossary/phenomena/philosophy/keywords/reviews/FAQ + lay-summary) is produced *in addition to* Steps A–H, not as a replacement for them.

### Reconciliation with §14 Pointer Format

The §14 "Session-close handover protocol" subsection (a narrower-scope subsection within the Organizational Frontier Registry section) specifies the *output format* for the OPEN-ORG queue: a short pointer to the registry rather than restated content. That format applies inside Step H's "Live registry entries" subsection — the OPEN-ORG queue gets a pointer, not restated content. §15 specifies the broader 8-step procedure; §14 specifies one output format inside Step H.

### Commit message convention

Commit messages for handover-protocol patches follow the convention: `[paper/series] Session [N] handover protocol — [brief summary of preserved items]`. This is distinct from the section-end-batch commit cadence in §10; section-end batches are task-driven, handover-protocol commits are session-continuity-driven. Both may occur in the same session.

### Anti-patterns to recognize

The following are signs that the protocol is being mistakenly skipped or that its execution is degrading:

- **Half-firing the protocol.** Completing some steps but not others without explicitly marking the unexecuted steps N/A. The 8-step sequence is mandatory; "I did the obvious ones" is the failure mode the sequencing is designed to prevent. If a step is genuinely N/A, it gets a "N/A" mark in the Step H audit table with brief rationale — not silent omission.
- **Producing the paste-ready handover (Step H) as inline chat text instead of a committed file.** The handover document only serves its function if it lives on disk where the next session can read it; an inline chat summary at session close dies at compaction. If the user asks for a session-close summary, that summary goes into Step H's file, not into the chat reply.
- **Treating the auto-generated session summary or compaction as a substitute for Steps A–H.** The summary is lossy by design — specific numbers, exact phrasing, and registry statuses get abbreviated or extrapolated. The 8-step sequence is verbatim by construction; the summary is not.
- **Bundling registries as "registry updates done" without per-registry audit.** Step E walks 9 registries individually because registry drift is the #1 source of next-session disorientation, and registry drift accumulates from registries that were "implicitly covered" but not actually checked. Each registry gets its own ✓ or N/A in the Step H audit.
- **Conflating "governance files committed" with "protocol fired completely."** The 8 steps are independent; satisfying any subset does not satisfy the whole. In particular, registry updates (Step E) often fire during the session as a side effect of work; this does not by itself satisfy Steps A, B, C, D, F, G, or H.
- **Deferring protocol/OS updates (Step G) to "next session."** Next session starts from a lossy summary or a paste-ready handover that doesn't reflect the as-yet-uncodified rule. The reasoning that produced a new rule will not survive compaction unless it is committed in this session. (This is the failure mode that produced OPEN-ORG-013's same-session register-then-resolve pattern.)
- **Skipping Step H because Steps A–G "have it covered."** They don't. Step H is the only artifact designed for direct paste into a new context window; the others are reference material. The 80–120-line concentrated form is structurally distinct from any of the inputs to it. Treating "we wrote the session log" as adequate handover is the failure mode the §4 reconciliation tried to address but didn't fully solve, which is why Step H now exists as a first-class step rather than an inferred consequence of the others.

### Maintenance cadence

- This §15 is itself §14-registered content per the meta-discipline rule above; if the protocol needs refinement, the refinement may be registered as an OPEN-ORG item rather than edited inline. Major refinements that fundamentally restructure the protocol (e.g., the 8-step sequencing replacement of the four-item checklist, adopted 5 May 2026 Session 13 close per OPEN-ORG-014 register-and-resolve) warrant inline edits with cross-reference to the originating OPEN-ORG entry.
- The 8-step sequence may be extended (e.g., a ninth step may be added) when a session-close failure mode demonstrates an artifact class not currently covered. As of 5 May 2026, eight steps cover the observed failure space, with Step H (paste-ready handover) added in this revision specifically to address the §4-vs-§15 reconciliation tension that produced fragmented handovers across distributed sources.
- The canonical command vocabulary may be extended with additional accepted variants over time; the existing list is illustrative rather than exhaustive.
- The Step H handover document template may be refined (additional sections added, audit table extended) as new failure modes surface; refinements should preserve the 80–120-line target length, since the artifact's value depends on its concentratedness.

---

*This document supersedes `bootup.md` as the complete reference.*
*`bootup.md` remains the quick-start guide for sessions.*
*Created 8 April 2026 by Claude Opus at Thomas's request.*
*Updated 9 April 2026 — SM-8/9/10 trilogy lessons, 7-file suite, SM-10 FEM references, Post-Session Quick Checklist, axiom reconciliation note.*
*Reconciled 11 April 2026 — merged operating_system.md and operating_system2.md; restored Phase 7b (Verification Notebooks) and transcript include/exclude guidance from v1.*
*Updated 24 April 2026 — added §14 Organizational Frontier Registry (adopted per PD-003).*
*Updated 24 April 2026 — added §15 Session-close Handover Protocol promoted from §10 buried subsection per OPEN-ORG-008 resolution; canonical command vocabulary "execute handover protocol" codified; dual-trigger mechanism (user-initiated + Claude-initiated workflow-shape prompt) documented; four-item checklist extended to name handover-[S]-[N].md alongside development-[S]-[N].md.*
