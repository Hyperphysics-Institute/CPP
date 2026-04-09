# CPP Programme Operating System

**Location:** `/CPP/operating_system.md`
**Purpose:** The complete workflow manual for the CPP research programme. Covers every procedure from session startup to OSF registration, including multi-AI coordination, document management, and recovery from interruptions.
**Last updated:** 8 April 2026
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
| `master_glossary.md` | Every CPP term defined | When new terms appear |
| `predictions.md` | Quantitative predictions with status | After each paper |
| `postulates_and_theorems.md` | Formal mathematical results | After each paper |

### Workflow
| Document | Purpose |
|----------|---------|
| `operating_system.md` | THIS FILE — complete workflow manual |
| `bootup.md` | Session startup guide (subset of this file) |
| `paper_production_workflow.md` | 9-phase paper pipeline (expanded below) |
| `documentation-suite.md` | 8-file companion template per paper |
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

### Phase 5: Axiom Registry Update
- Check if new axioms were introduced
- Check if existing axioms were consolidated (e.g., A6' replacing A6-A9)
- Update axiom count and prediction count
- Compute axiom-to-prediction ratio

### Phase 6: OSF Registration
- Prepare PDF and .tex
- Write OSF metadata (title, abstract, keywords, dependencies)
- Register with DOI

### Phase 7: Documentation Suite
- Create all 8 companion files per `documentation-suite.md`
- Files: development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, keywords

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

### Key lessons from SM-8:
- Grok contributed the most important single result (z=12 theorem). Don't just ask for review — ask for CONTRIBUTION.
- Copilot excels at referee-proofing — framing, axioms, anticipated criticisms.
- Sonnet's hostile review is valuable for identifying real weaknesses but tends toward philosophical objection ("this isn't QCD") rather than technical critique.
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

**Example from SM-8/SM-9:**
- Sea composition doesn't affect mass ratios (cancels when uniform)
- Additive chain-energy models fail by 65-92%
- Spectral dimension d_s ≈ 3.55 ≠ α ≈ 2.38
- φ^(3(l-1)) scaling falsified for light quark masses (PS-1)

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
- [ ] `master_glossary.md` (see procedure below)
- [ ] `founders_vision.md` (see procedure in Section 7)
- [ ] `predictions.md` (see procedure below)
- [ ] `postulates_and_theorems.md` (see procedure below)
- [ ] `future_projects.md` (see procedure below)
- [ ] `CPP_the_theory.md` (see procedure below)
- [ ] `bibliography/cpp_references.bib` (see procedure below)
- [ ] `open_problems/` (see procedure below)

#### theory-overview.md update procedure
1. Add any new quantitative results to the "Strongest Quantitative Results" table
2. Update the "Key Formulas" reference card if new formulas were derived
3. Update "Open Problems" — move solved problems out, add new ones
4. Update "Series Status" table with new paper version and status
5. If axiom count changed, update the axiom summary

#### axiom-registry.md update procedure
1. Check: did the paper use any axiom not already in the registry? If so, add it.
2. Check: did the paper consolidate axioms (as SM-8 did with A6')? If so, update tiers.
3. Add every new quantitative prediction to the Prediction Ledger:
   ```
   | 13 | m_t (cage × z=12) | 172,800 MeV | 172,760 | 0.02% | A2,A6' + m_s,m_c | SM-8 |
   ```
4. Update the axiom count summary and axiom-to-prediction ratio
5. Add a row to the Growth Table showing this paper's contribution
6. Check if any conjectured reductions were achieved

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
   | SM-8-1 | m_b (cage V^2.38) | 4,304 MeV | 4,180 MeV | 3.0% | A2 + m_s,m_c | CONFIRMED |
   ```
2. Update status of existing predictions if new data or analysis changes them
3. Update the total prediction count and zero-parameter prediction count

#### postulates_and_theorems.md update procedure
1. Add each new theorem with its ID, statement, and proof reference:
   ```
   **THEO-SM-8-1** (Bonded Shells): The 600-cell has exactly four bonded
   polyhedral distance shells. [SM-8, Theorem 3.1]
   ```
2. Add any new conjectures (CONJ) with status
3. Add any new corollaries (CORO)
4. If a conjecture was proved or falsified, update its status (CONJ → THEO or CONJ → FALS)

#### future_projects.md update procedure
1. Mark any completed projects as DONE with date
2. Update status of in-progress projects (e.g., "SM-9 v2.0 drafted")
3. Add any new research targets that emerged during the session
4. Re-prioritise if the session changed what's most promising

#### CPP_the_theory.md update procedure
1. Identify which chapter(s) the new results belong to
2. Add the results in connected prose (not bullet points — this is the "Kindle book")
3. Update the Prediction Scorecard in Part VI
4. If a new chapter is needed (new topic area), add it in the appropriate Part
5. Move any resolved open problems from Part V to the relevant chapter
6. Add any new open problems to Part V

#### bibliography/cpp_references.bib update procedure
**TRIGGER:** After any new paper is completed, or when a new external reference is cited.
1. Add a BibTeX entry for the new CPP paper:
   ```bibtex
   @article{abshier2026sm8,
     author  = {Abshier, Thomas Lee and {Claude Opus} and {Grok} and {Copilot}},
     title   = {Quark Generation Structure from 600-Cell Distance Shells},
     journal = {Hyperphysics Institute},
     year    = {2026},
     note    = {SM-8 v3.0}
   }
   ```
2. Add BibTeX entries for any external works cited in the paper
3. Verify all cite keys match what's used in the paper's .tex file

#### open_problems/ update procedure
**TRIGGER:** After any session that registers new open problems or resolves existing ones.
1. For each new OPEN-P problem, create a file:
   ```
   Filename: OPEN-P-SM-cage-7.md
   Content: Problem statement, context, why it matters,
            candidate approaches, related problems
   ```
2. For resolved problems: add a "RESOLVED" header with date, resolution, and
   which paper resolved it. Do NOT delete the file — it's part of the history.
3. For falsified conjectures: rename with FALS prefix or add FALSIFIED header

### Navigation documents (update structure)
- [ ] `README.md` — add paper to table, update counts (see procedure below)
- [ ] `INDEX.md` — add new files (see procedure below)
- [ ] `paper_catalog.md` — add paper entry
- [ ] `series_[name]/README.md` — add paper to series

#### README.md update procedure
1. Add the new paper to the "Registered Papers" table:
   ```
   | SM-8 | Quark Generation Structure from 600-Cell Distance Shells | v3.0 | OSF registered |
   ```
2. Update the paper count ("24 papers" → "25 papers" etc.)
3. If the paper produced a headline result, add it to "Strongest Results":
   ```
   | m_t = 172,800 MeV | 172,760 MeV | 0.02% | SM-8 |
   ```
4. If axiom count changed, update the axiom summary line
5. Add any new series-level achievements to the series table

#### INDEX.md update procedure
1. Add every new file created during this paper's production:
   - The paper itself (.tex, .pdf)
   - All 8 documentation suite files
   - Any development transcripts
   - Any new figures
2. Add files to the correct folder section in INDEX.md
3. Format: `- [filename](path) — one-line description`
4. If a new folder was created, add the folder heading

#### paper_catalog.md update procedure
1. Add one row per new paper:
   ```
   | SM-8 | Quark Generation Structure from 600-Cell Distance Shells | v3.0 | 14 pages | April 2026 | OSF pending |
   ```
2. Update the total paper count at the top

### History documents (create/update)
- [ ] `development-[S]-[N].md` — paper development narrative (see procedure below)
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
- Same name for `.tex`, `.pdf`, and all companion `.md` files
- Examples:
  - `SM-6_lepton_mass_spectrum.tex`
  - `SM-7_heavy_quark_mass_spectrum.tex`
  - `SM-8_quark_generation_600cell_shells.tex`
  - `SM-9_scaling_exponent.tex`

### Version management
- **ONE file per paper, overwritten with each revision.** Git history preserves all versions.
- The `.tex` header contains a CHANGELOG block documenting each version.
- The development transcript documents WHY each version changed.
- Do NOT create `SM-8_v1.tex`, `SM-8_v2.tex`, etc. — this creates clutter and confusion.
- **Exception:** If a revision fundamentally changes scope, archive the old version in `archive/` with a note.
- To recover an old version: `git log [filename]` then `git checkout <hash> -- [filename]`

### Staging/scratch files
- Files like `SM-8_integration_items.md` (work-orders collecting items to integrate elsewhere) should be moved to `archive/` once all items are integrated.
- Do not leave completed staging files in `papers/`.

### Documentation suite
- `[type]-[S]-[N].md`
- Example: `development-SM-8.md`, `FAQ-SM-8.md`, `reviews-SM-8.md`

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
- **Notable contribution:** Scheme-dependence criticism led to important SM-8 remark

---

## Appendix: Lessons Learned from SM-8 (April 2026)

1. **Papers emerge from exploration.** SM-8 was not planned. Allow discovery sessions to produce unexpected papers.

2. **Negative results are publications.** SM-9 is entirely about what didn't work. Document failures with the same care as successes.

3. **The multi-AI team is more than the sum of its parts.** Grok's z=12 multiplier came from asking for review, not for a specific calculation. Give the team room to contribute.

4. **Honest self-assessment strengthens papers.** The "epistemological status" remark in SM-8 — acknowledging that the case is inductive, not deductive — was praised by all reviewers.

5. **Buffer overflows will happen.** Plan for them: keep `founders_vision.md` and transcripts current so nothing is lost.

6. **The founder's voice is irreplaceable.** Thomas's stream-of-consciousness descriptions (the near-field/far-field mechanism, the fractal branching picture, the cooperative coupling insight) generate every breakthrough. Capture them immediately.

---

*This document supersedes `bootup.md` as the complete reference.*
*`bootup.md` remains the quick-start guide for sessions.*
*Created 8 April 2026 by Claude Opus at Thomas's request.*
