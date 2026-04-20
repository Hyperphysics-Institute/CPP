# CPP Programme Operating System

**Location:** `/CPP/operating_system.md`
**Purpose:** The complete workflow manual for the CPP research programme. Covers every procedure from session startup to OSF registration, including multi-AI coordination, document management, and recovery from interruptions.
**Last updated:** 11 April 2026
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

---

## 1. Quick Start (for a brand-new session)

**Thomas says:** "Pull the CPP repo and read `templates/bootup.md`"

**AI assistant does:**
1. Read `bootup.md` — repository structure, conventions, what CPP is
2. Read `theory-overview.md` — current physics state, strongest results, open problems
3. Read `founders_vision.md` — Thomas's physical intuition (the WHY behind every equation)
4. Read `CPP_the_theory.md` — the complete theory narrative (skim Part I-III, read Part V for open problems)
5. Read `master_glossary.md` — all CPP terms and acronyms
6. Check the most recent transcript in `/mnt/transcripts/` or `development-transcripts/` for where the last session left off
7. Ask Thomas: "What would you like to work on today?"

**If resuming a specific paper:** Also read the paper's `.tex` file and its `development-[S]-[N].md`.

**If this is a continuation after buffer overflow:** Read the compacted summary at the top of this conversation, then read the transcript file referenced there for full detail. Proceed from where the summary indicates.

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

## 10. Repository Housekeeping Checklist

**TRIGGER:** Run this checklist immediately after completing Phase 7 (Documentation Suite) of the paper production pipeline — BEFORE pushing to GitHub. Do not push until all items are checked.

**Estimated time:** 15-20 minutes for a single paper.

**Run after every paper is completed:**

### Content documents (update substance)
- [ ] `theory-overview.md` (see procedure below)
- [ ] `axiom-registry.md` (see procedure below)
- [ ] `theorem-registry.md` (see procedure below)
- [ ] `Research_Frontier.md` (see procedure below)
- [ ] `master_glossary.md` (see procedure below)
- [ ] `founders_vision.md` (see procedure in Section 7)
- [ ] `predictions.md` (see procedure below)
- [ ] `future_projects.md` (see procedure below)
- [ ] `CPP_the_theory.md` (see procedure below)
- [ ] `bibliography/cpp_references.bib` (see procedure below)
- [ ] `problem_histories/` (see procedure below)

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
1. Identify which chapter(s) the new results belong to
2. Add the results in connected prose (not bullet points — this is the "Kindle book")
3. Update the Prediction Scorecard in Part VI
4. If a new chapter is needed (new topic area), add it in the appropriate Part
5. Move any resolved open problems from Part V to the relevant chapter
6. Add any new open problems to Part V

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
- [ ] `README.md` — add paper to table, update counts (see procedure below)
- [ ] `INDEX.md` — add new files (see procedure below)
- [ ] `paper_catalog.md` — add paper entry
- [ ] `series_[name]/README.md` — add paper to series

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
- [ ] `development-[S]-[N].md` — paper development narrative (see procedure below)
- [ ] Verification notebooks in `series_[name]/notebooks/` (see Phase 7b)
- [ ] Curated transcripts — all sessions contributing to the paper
- [ ] Comprehensive development transcript (see procedure below)

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

### Final steps
- [ ] Push all files to GitHub
- [ ] Register on OSF (if applicable)
- [ ] Verify OSF wiki links

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

*This document supersedes `bootup.md` as the complete reference.*
*`bootup.md` remains the quick-start guide for sessions.*
*Created 8 April 2026 by Claude Opus at Thomas's request.*
*Updated 9 April 2026 — SM-8/9/10 trilogy lessons, 7-file suite, SM-10 FEM references, Post-Session Quick Checklist, axiom reconciliation note.*
*Reconciled 11 April 2026 — merged operating_system.md and operating_system2.md; restored Phase 7b (Verification Notebooks) and transcript include/exclude guidance from v1.*
