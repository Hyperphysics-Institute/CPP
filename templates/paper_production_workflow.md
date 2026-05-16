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
   - Minimal source-file header block pointing to `documentation_suite/changelog-<paper>.md` (no inline CHANGELOG comment block; see `paper-formatting.md` §3.1)
   - letterpaper, natbib authoryear, booktabs
   - Abstract, Keywords, Plain Language Summary
   - raggedright, Table of Contents
   - Sections with `% ===` markers
   - **CPP Physical Mechanism section** (see below)
   - **CPP-to-Conventional-Physics Mapping section** (see below)
   - Appendices (numerical verification, sensitivity analysis)
   - Acknowledgements with OSF DOI
2. Create `documentation_suite/changelog-<paper>.md` with v0.1 entry (see `templates/documentation-suite.md` §9).
   - `.bib` bibliography: use the master file `bibliography/cpp_references.bib` via `\bibliography{../../bibliography/cpp_references}`. Alternatively, use an inline `thebibliography` block with `\bibitem{}` entries (no external .bib needed). **Do NOT create a new per-paper `[ID]_references.bib` file — those are deprecated.**
2. Compile to PDF (pdflatex + bibtex, 3 passes).
3. Run formatting audit (all template checks must pass).

### Required: CPP Physical Mechanism Bridge

Every CPP paper must include a section (typically after the mathematical derivation and before the conclusion) that answers two questions:

**Question 1 — "What is physically happening?"**
Explain the CPP mechanism in terms of CPs, DPs, chains, cages, SSV fields, and DI-bit propagation. What physical objects are involved? What are they doing? Where is the energy? This section should be intelligible to a physicist who accepts the CPP ontology but hasn't read the mathematical proof.

**Question 2 — "How does this map to conventional physics?"**
Provide a table or structured comparison showing how each element of the CPP mechanistic account corresponds to the conventional physics description. The mapping is *structural*, not literal — CPP operates at a finer granularity than perturbative QFT, so there is generally no one-to-one correspondence between individual CPP elements and individual Feynman diagrams. The correspondence is at the level of the symmetry, the degrees of freedom, and the observable predictions.

**Why this matters:** Without the physical mechanism section, a CPP paper looks like a mathematical reproduction of known results. With it, the paper demonstrates that CPP provides a *deeper* account — it explains *why* the mathematics takes the form it does. This is the difference between "CPP accommodates SU(3)" and "CPP explains why the strong force has 8 degrees of freedom."

**Example (from SS-3 v1.1):**
- Physical mechanism: 4 linear DP-chain bond oscillations + 4 coupled harmonic junction oscillations = 8 modes
- Mapping: 8 CPP oscillation modes ↔ 8 QCD gluon fields; colour states ↔ cage base vertices; gluon exchange ↔ DI-bit propagation along DP chains; confinement ↔ cage energetic stability

**Output:** `[PAPER-ID]_[title].tex`, `.pdf` (bibliography via master `bibliography/cpp_references.bib` or inline `\bibitem`)

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

The atomic task list for Phase 9 (content registry updates, navigation updates, final verification, and git commit/push) is consolidated into `templates/paper_completion_checklist.md` Sections C, D, G, and H. Execute those sections against this paper; skip items whose trigger condition is not met. Reference-level update procedures for each individual file live in `operating_system.md` §10.

Do NOT re-enumerate the per-file tasks here. The 20 April 2026 consolidation moved atomic tasks to a single authoritative file to prevent drift between parallel enumerations.

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
[ ] Phase 7–9: Execute templates/paper_completion_checklist.md in full
               (documentation suite, notebooks, registry updates, navigation
               updates, transcripts, OSF finalisation, git commit/push,
               final verification)
```

*Phase 7–9 was previously enumerated as ~13 separate checkbox items here;
consolidated 20 April 2026 into `templates/paper_completion_checklist.md`.
Run that checklist end-to-end; its completion criterion covers Phase 7–9
in full.*

---

## Version History of This Document

| Date | Change |
|------|--------|
| 3 April 2026 | Initial version, codifying SM-6/SM-7 workflow |
| 20 April 2026 | Phase 9 tables and Phase 0-9 copy-template reduced to pointers at `templates/paper_completion_checklist.md`. Atomic task enumeration consolidated into a single authoritative file to prevent drift. Reference procedures remain in `operating_system.md` §10. |

---

*Document created by Claude Opus, 3 April 2026, at Thomas's request.*
*"We should have an operating system document that formalizes the addition of each piece." — Thomas Lee Abshier, 3 April 2026*
