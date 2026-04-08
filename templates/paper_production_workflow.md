# CPP Paper Production Operating System

**Location:** `/CPP/paper_production_workflow.md`
**Purpose:** Formalise the complete workflow for producing a new CPP paper, from initial physical intuition through OSF registration and documentation.
**Last updated:** 3 April 2026

---

## Overview

Each CPP paper follows a production pipeline that has evolved through the SM-6 and SM-7 campaigns. This document codifies that pipeline so every future paper achieves the same standard of documentation, review, and archival.

---

## Phase 0: Founder's Vision Capture

**Before any mathematics begins.**

1. Thomas describes the physical mechanism in his own words (in conversation, via Otter transcript, or stream-of-consciousness text).
2. AI assistant captures the description verbatim and places it in `founders_vision.md` under the appropriate entity/interaction section.
3. Tag the entry with the date and session identifier.

**Output:** Updated `founders_vision.md` with new physical intuition entry.

---

## Phase 1: Exploration and Discovery

**The working session where the physics happens.**

1. State the goal: what phenomenon are we trying to derive?
2. Check which axioms from `axiom-registry.md` are available.
3. Explore systematically — compute, test models, follow leads.
4. When a result emerges, verify numerically.
5. Check mutual reinforcement with existing results.

**During the session:**
- The AI assistant saves key physical insights from Thomas to `founders_vision.md`.
- All computation happens in the conversation and is captured in the raw transcript.

**Output:** A derivation result with numerical verification.

---

## Phase 2: Paper Drafting (v1)

**Immediately after discovery, while context is fresh.**

1. Draft the `.tex` file following `templates/paper-formatting.md`:
   - CHANGELOG comment block
   - letterpaper, natbib authoryear, booktabs
   - Abstract, Keywords, Plain Language Summary
   - raggedright, Table of Contents
   - Sections with `% ===` markers
   - Appendices (numerical verification, sensitivity analysis)
   - Acknowledgements with OSF DOI
   - `.bib` bibliography (local, next to `.tex`)
2. Compile to PDF (pdflatex + bibtex, 3 passes).
3. Run formatting audit (all template checks must pass).

**Output:** `[PAPER-ID]_[title].tex`, `.pdf`, `[PAPER-ID]_references.bib`

---

## Phase 3: Development Log

**Record the intellectual history.**

Write `development-[PAPER-ID].md` covering:
- Starting point and motivation
- Key decisions and dead ends
- Discovery moments with timestamps (Mountain Time)
- What was tried and failed
- What worked and why
- Open problems identified during the session

**Output:** `development-[PAPER-ID].md`

---

## Phase 4: Team Review

**Send to Grok, Copilot, and Sonnet for independent review.**

### 4a. Friendly reviews (Grok + Copilot)

Prepare tailored prompts that:
- Summarise the core result
- State the key assumptions
- Ask 5-6 specific questions targeting each reviewer's expertise
- Request: "Is this internally consistent, non-tuned, and worthy of being called a theorem?"

### 4b. Incorporate friendly feedback → v2

Apply all valid suggestions. Typical changes:
- Tighten theorem statements
- Add explicit assumption dependencies
- Correct framing (e.g., "mode complementarity" not "unification")
- Flag open problems with OPEN-P numbers

### 4c. Hostile review (Sonnet 4.0)

Prepare adversarial prompt:
- "Act as a skeptical referee. Be adversarial."
- State claims clearly so they can be attacked
- Ask Sonnet to address specific attack vectors
- Request verdict: Accept / Major Revision / Minor Revision / Reject

### 4d. Respond to hostile review

Sort criticisms into:
- ✅ Valid — must address
- ⚠️ Partially valid — acknowledge but defend
- ❌ Wrong — rebut with evidence

Write `response-to-sonnet-[PAPER-ID].md` with point-by-point responses.

### 4e. Final revision → v2.x

Incorporate all valid criticisms. The paper should now be the strongest version that can be produced with current knowledge.

**Output:** `reviews-[PAPER-ID].md`, `response-to-sonnet-[PAPER-ID].md`, review prompts file, updated `.tex` and `.pdf`

---

## Phase 5: Axiom Registry Update

1. Open `axiom-registry.md`.
2. Check which existing axioms were used.
3. If new axioms were needed, add them to the appropriate tier.
4. Add new predictions to the ledger with axiom dependencies.
5. Update the growth table (cumulative axioms vs predictions).
6. Check whether any axiom reductions were achieved.

**Output:** Updated `axiom-registry.md`

---

## Phase 6: OSF Registration

1. Upload the PDF to the OSF project (osf.io/9dfya).
2. Update the OSF wiki:
   - Add row to Submission-Ready Papers table
   - Update paper count in header
   - Update "Last updated" date
3. Confirm the upload notification email.

**Output:** Timestamped PDF on OSF, updated wiki.

---

## Phase 7: Documentation Suite

Generate the 8-file documentation suite per `templates/documentation-suite.md`:

| File | Content |
|------|---------|
| `development-[ID].md` | Session history and timeline (from Phase 3) |
| `reviews-[ID].md` | All team reviews compiled (from Phase 4) |
| `FAQ-[ID].md` | 8-12 Q&A pairs covering major objections |
| `glossary-[ID].md` | Key terms with CPP-specific definitions |
| `mechanism-[ID].md` | How the derivation works physically |
| `phenomena-[ID].md` | What's explained, predicted, and not explained |
| `philosophy-[ID].md` | Philosophical implications and context |
| `keywords-[ID].md` | Primary/secondary keywords, PACS/MSC codes, elevator pitch, SEO |

All files go to `series_[name]/papers/`.

**Output:** 8 documentation files.

---

## Phase 8: Transcript Curation

**Preserve the intellectual drama for scholarship.**

### 8a. Raw transcript collection

At the end of each session, the raw conversation transcript is saved. Sources:
- Claude sessions: auto-saved in `/mnt/transcripts/` as `.txt` files
- Grok sessions: copy-paste from Thomas's chat window
- Copilot sessions: copy-paste from Thomas's chat window
- Otter transcripts: export from Otter.ai

### 8b. Curated transcript production

From each raw session, produce a curated transcript:

**Filename:** `[PAPER-ID]_transcript_[N]_[AI-name].md`
**Example:** `SM-7_transcript_01_opus.md`, `SM-7_transcript_02_copilot.md`

**Curation rules:**
- Preserve all substantive dialogue verbatim (Thomas's words, AI reasoning, discoveries)
- Remove: file system commands, formatting instructions, path references, compilation output, "please wait" messages, tool invocation details
- Smooth: obvious typos, broken sentences from copy-paste artifacts, session disconnection noise
- Keep: wrong turns, dead ends, "wait, what if..." moments, disagreements, corrections
- Add: section headers with timestamps, brief context notes in [brackets]
- Number sequentially per paper across all AI sessions

### 8c. Storage

```
series_[name]/development-transcripts/
├── [PAPER-ID]_transcript_01_opus.md
├── [PAPER-ID]_transcript_02_copilot.md
├── [PAPER-ID]_transcript_03_grok.md
├── [PAPER-ID]_transcript_04_opus.md
└── ...
```

**Output:** Numbered, curated transcript files in `development-transcripts/`.

---

## Phase 9: Repository Housekeeping

**Update every affected document after each paper.**

### 9a. Theory-state documents (update content)

| Document | What to update |
|----------|----------------|
| `theory-overview.md` | Add new results to scorecard, update formula card, open problems |
| `axiom-registry.md` | Check axiom usage, add predictions, update growth table |
| `master_glossary.md` | Add any new terms, acronyms, particles, or processes introduced |
| `founders_vision.md` | Add any new physical intuitions captured during the session |
| `predictions.md` | Add new quantitative predictions with status |
| `postulates_and_theorems.md` | Add new theorems (THEO), corollaries (CORO), conjectures (CONJ) |
| `propositions.md` | Add new physically motivated claims |
| `solution_candidates.md` | Update if open problems were addressed |
| `open_problems/` | Register new OPEN-P entries; close solved ones |

### 9b. Navigation documents (update structure)

| Document | What to update |
|----------|----------------|
| `README.md` | Add paper to Registered Papers table, update count, strongest results |
| `INDEX.md` | Add new files and folders |
| `paper_catalog.md` | Add paper entry with ID, title, version, status |
| `series_[name]/README.md` | Add paper to series table |

### 9c. Final steps

1. Push all new files to GitHub.
2. Verify all links in OSF wiki still work.
3. Confirm no stale references in README or INDEX.

**Output:** Clean, up-to-date repository.

---

## Checklist (copy for each new paper)

```
Paper: [PAPER-ID]
Date started: 
Date registered on OSF: 

[ ] Phase 0: Founder's vision captured
[ ] Phase 1: Discovery session complete
[ ] Phase 2: Paper v1 drafted and compiled
[ ] Phase 3: Development log written
[ ] Phase 4a: Grok review received
[ ] Phase 4a: Copilot review received
[ ] Phase 4b: v2 incorporating friendly reviews
[ ] Phase 4c: Sonnet hostile review received
[ ] Phase 4d: Response to Sonnet written
[ ] Phase 4e: Final version (v2.x)
[ ] Phase 5: Axiom registry updated
[ ] Phase 6: PDF uploaded to OSF, wiki updated
[ ] Phase 7: Documentation suite (8 files)
[ ] Phase 8: Transcripts curated and filed
[ ] Phase 9a: theory-overview.md updated
[ ] Phase 9a: master_glossary.md updated
[ ] Phase 9a: founders_vision.md updated (if new intuitions)
[ ] Phase 9a: predictions.md updated (if new predictions)
[ ] Phase 9a: postulates_and_theorems.md updated (if new theorems)
[ ] Phase 9b: README.md updated
[ ] Phase 9b: INDEX.md updated
[ ] Phase 9b: paper_catalog.md updated
[ ] Phase 9b: series README updated
[ ] Phase 9c: GitHub pushed, links verified
```

---

## Version History of This Document

| Date | Change |
|------|--------|
| 3 April 2026 | Initial version, codifying SM-6/SM-7 workflow |

---

*Document created by Claude Opus, 3 April 2026, at Thomas's request.*
*"We should have an operating system document that formalizes the addition of each piece." — Thomas Lee Abshier, 3 April 2026*
