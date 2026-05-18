# CPP Documentation Suite Template

**Location:** `/CPP/templates/documentation-suite.md`
**Purpose:** Defines the structure and content expectations for each documentation file that accompanies every CPP paper.
**Last updated:** 24 April 2026 (folder-location section added; lab-notebook trio aligned with doc-suite folder per Thomas's decision during SS-5/6/7 migration scoping)

---

## Overview

Every CPP paper has up to 8 companion `.md` files in the canonical doc-suite, plus the `changelog-[S]-[N].md` version-archaeology file (which is maintained continuously from v0.1), plus optionally 2 lab-notebook-trio files (handover, transcript) that serve session-continuity purposes. The 8 doc-suite files serve different audiences and purposes:

| File | Audience | Purpose |
|------|----------|---------|
| `development-[S]-[N].md` | Future collaborators (human + AI) | How the paper came to be — decisions, dead ends, timeline. Also serves as the lab-notebook vignette file (see "Relationship to lab-notebook trio" below). |
| `glossary-[S]-[N].md` | All readers | Define every technical term; status labels |
| `mechanism-[S]-[N].md` | Physicists | Physical mechanisms with intuitive explanations |
| `phenomena-[S]-[N].md` | Physicists + general | What the paper explains and predicts |
| `philosophy-[S]-[N].md` | Theorists + philosophers | Conceptual content, type classification, honest assessment |
| `reviews-[S]-[N].md` | Authors + referees | External reviews received, critiques addressed |
| `FAQ-[S]-[N].md` | General readers + web | Anticipated questions and clear answers (legacy-allowed; not required for papers adopted ≥ 22 April 2026) |
| `keywords-[S]-[N].md` | SEO / web tooling / search | Keywords, PACS/MSC codes, elevator pitch |

In addition, **every paper carries a `changelog-[S]-[N].md` file from v0.1 onward** (adopted Patch 0408 Session 115; codified Patch 0409 Session 116). This is the canonical version archaeology — replacing the historical pattern of putting CHANGELOG comment blocks in `.tex` headers and visible version-history paragraphs in `.tex` title blocks. The changelog file is maintained continuously during drafting (unlike the 7-file canonical doc-suite which is produced post-v1.0). See `operating_system.md` ``Version-archaeology architecture rule'' for the convention and `flagship_papers/capotauro/documentation_suite/changelog-capotauro.md` for the reference implementation.

Some papers also carry a `lay-summary-[S]-[N].md` file (e.g., SS-7) for non-physicist accessibility; this is allowed but not required.

Naming convention: `[S]` = series abbreviation (SM, EW, SR, SS, QM, SD, SF), `[N]` = paper number; for papers without an `[S]-[N]` identifier (e.g. the Capotauro flagship which is `capotauro`), the bare paper name substitutes (e.g. `changelog-capotauro.md`). Canonical filenames carry no version suffix; version history lives in the changelog file, not in the filename.

---

## Folder Location (decision adopted 24 April 2026)

**All documentation suite files for a given paper live in `series_[name]/papers/[PAPER-ID]/documentation_suite/`** under the per-paper-subfolder convention adopted 22 April 2026 (`templates/operating_system.md` §11). This applies uniformly to:

- The 8 canonical doc-suite files listed above (development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, keywords)
- The 2 lab-notebook-trio session-continuity files (`handover-[S]-[N].md`, `transcript-[S]-[N].md`) introduced for SS-8 and codified in `operating_system.md` §15
- Any optional supplementary files such as `lay-summary-[S]-[N].md`

For papers adopted before 22 April 2026 (SS-1 through SS-7, SM-N legacy papers), doc-suite files currently live flat in `series_[name]/papers/` and migrate to per-paper subfolders under OPEN-ORG-004's opportunistic trigger.

### Relationship to lab-notebook trio

`operating_system.md` §15 specifies a session-continuity *lab-notebook trio*: `development-[S]-[N].md` (vignette-style narrative, append-only), `handover-[S]-[N].md` (current-state orientation document, replaced at each session close), and `transcript-[S]-[N].md` (transaction-indexed pointer-map). The `development-[S]-[N].md` member of the trio is the **same file** as the canonical doc-suite's `development-[S]-[N].md` listed above — a single file serving both purposes (intellectual laboratory record AND session-by-session vignette history). The `handover` and `transcript` files are additions specific to the per-paper-subfolder convention and do not exist in the older flat-files layout.

A paper at v1.0+ under the per-paper-subfolder convention may therefore have up to 10 file types in `documentation_suite/`: the 8 canonical doc-suite files plus `handover-[S]-[N].md` plus `transcript-[S]-[N].md`. A paper still under the legacy-flat layout has only the doc-suite files at `series_[name]/papers/` level.

### Decision rationale

Thomas's decision (24 April 2026, during SS-5/6/7 migration scoping): *"All 7 .md files you noted go in the documentation suite (mechanism, glossary, phenomena, philosophy, reviews, keywords, development). The definitions of what each of these files is [are] defined, probably in Templates, but these files are called the 'documentation suite.'"* Codification here resolves the prior ambiguity about whether the older 8-file doc-suite and the SS-8 3-file lab-notebook trio occupied separate folders or shared one. They share `documentation_suite/`. Naming overlap on `development-[S]-[N].md` is not a collision because it is the same file under both conventions.

---

## 1. development-[S]-[N].md

### Purpose
The intellectual laboratory notebook. Records HOW the paper came to be — not what it says (that's the paper), but what decisions were made, what failed, what was surprising, and what the timeline was. This is the file a future AI or collaborator reads to understand the context.

### Required Sections

```markdown
# Development History: [S]-[N] — [Full Title]

**Series:** [Series name]
**Authors:** [All contributors]
**Document type:** Development narrative — laboratory notebook record
**Last updated:** [Date]

---

## Purpose of This File
[1-2 paragraphs: what this document records and why]

---

## The Starting Point
[What question or task initiated this paper? What was known before?]

---

## Key Discoveries (chronological)
### Discovery 1: [Name]
[What was found, how, what it means]

### Discovery 2: [Name]
...

---

## Failed Approaches
### Failed Approach 1: [Name]
[What was tried, why it failed, what it ruled out]
...

---

## Key Decisions and Why
### Decision 1: [Name]
[What was decided, what alternatives existed, why this choice]
...

---

## The Paper
[How the paper was structured, review cycle, version history]

---

## Open Problems
[What remains to be solved, natural next targets]

---

## File Manifest
[Table of all files produced]

---

## Timeline
[Chronological event list with timestamps in Mountain Time (MDT/MST)]
```

### Style Notes
- Write in past tense (this is a record of what happened)
- Include dead ends — they are as valuable as successes
- Be specific about WHO contributed WHAT
- Timestamps in Mountain Time (Thomas's local time; MDT = UTC-6 in summer, MST = UTC-7 in winter)

### Problem History Updates (Phase 7 addition)
After completing the development file, also update any relevant **problem history files** in `problem_histories/`. If the paper advances, resolves, or falsifies an open problem listed in `research_frontier.md`, add a dated journal entry to the corresponding `PH-[ID].md` file recording what was tried, what was learned, and the status change. See `templates/research_frontier_architecture.md` for the problem history format. If no history file exists yet and the paper produced significant progress on a problem, create one.

---

## 2. glossary-[S]-[N].md

### Purpose
Define every technical term used in the paper. A reader should be able to look up any unfamiliar term here without leaving the document.

### Required Sections

```markdown
# Glossary — [S]-[N]: [Full Title]

## Core Mathematical Objects
[Matrices, graphs, operators, spaces — with eigenvalues, dimensions, properties]

## Physical Concepts
[CPP-specific physics terms — SSV, DI-bit, edge mode, face mode, etc.]

## Standard Physics Terms (used non-standardly)
[Any term where CPP's usage differs from the SM — flag explicitly]

## Status Labels
[Define: PROVED, DERIVED, CONJECTURED, AXIOM, etc.]
```

### Style Notes
- Each entry: **Bold term:** definition (1-3 sentences)
- Include numerical values where relevant (e.g., "z = 12, the 600-cell coordination number")
- Cross-reference the paper's equations/theorems where appropriate
- If a term has a different meaning in the SM, note the difference explicitly

---

## 3. mechanism-[S]-[N].md

### Purpose
Explain the physical mechanisms in the paper at an intuitive level. A physicist unfamiliar with CPP should understand WHAT is happening physically (not just mathematically) after reading this file.

### Required Sections

```markdown
# Mechanism — [S]-[N]: [Full Title]

## Mechanism 1: [Name]
**What it does:** [One sentence]
**How it works:** [2-5 sentences: the physical picture]
**Key insight:** [The non-obvious part]

## Mechanism 2: [Name]
...
```

### Style Notes
- Each mechanism gets its own section
- Start with "what it does" (the output/result) before "how it works" (the process)
- Use analogies where they clarify — but flag them as analogies, not identities
- If the mechanism differs from the SM explanation of the same phenomenon, explain both and why they differ

---

## 4. phenomena-[S]-[N].md

### Purpose
List what the paper explains (matches existing data) and what it predicts (testable claims not yet verified). This is the scorecard.

### Required Sections

```markdown
# Phenomena — [S]-[N]: [Full Title]

## Phenomena Explained
### 1. [Phenomenon name]
- **SM status:** [Free parameter / unexplained / partially explained]
- **CPP derivation:** [One sentence: how CPP gets this]
- **Accuracy:** [Numerical comparison with data]

### 2. [Phenomenon name]
...

## Phenomena Predicted
### N. [Prediction name]
- **Prediction:** [What CPP predicts]
- **Testable:** [How it could be verified or falsified]
```

### Style Notes
- Number phenomena consecutively across both sections
- Always include the SM status for context (what does the SM say about this?)
- Predictions must be FALSIFIABLE — state what would disprove them
- Include accuracy numbers (percentages, σ, ppm) for all comparisons

---

## 5. philosophy-[S]-[N].md

### Purpose
The conceptual and philosophical content of the paper. Type classification (how much is proved vs assumed), honest assessment of strengths and weaknesses, and deeper interpretive points.

### Required Sections

```markdown
# Philosophy — [S]-[N]: [Full Title]

## Type Classification
[Type 1: purely derived / Type 1.5: framework derived, value calibrated /
 Type 2: zero-parameter derivation / Type 3: requires new axiom]

## Key Philosophical Points
### 1. [Point name]
[2-5 sentences]

### 2. [Point name]
...

## Honest Assessment
### What CPP IS doing
[Bullet points]

### What CPP is NOT doing
[Bullet points — preempt mischaracterisations]

### Weakest link
[Identify the single weakest assumption explicitly]
```

### Style Notes
- Be HONEST. The philosophy file is where we acknowledge limitations, not where we hide them.
- The "What CPP is NOT doing" section preempts strawman critiques
- The "Weakest link" section tells a reader exactly where to push if they want to challenge the paper
- Type classification follows the scale established in philosophy-EW-1.md

---

## 6. reviews-[S]-[N].md

### Purpose
Record all external reviews and critical assessments received, and document the responses. This is the paper's dialogue with its critics — the adversarial record. This file is largely FIXED once the review cycle is complete.

### Required Sections

```markdown
# Reviews — [S]-[N]: [Full Title]

## Review 1: [Reviewer name/system] — [Positive/Negative/Mixed]
**Verdict:** [One-sentence summary]
**Key points:** [Bullet list]

## Review 2: [Reviewer name/system] — [Positive/Negative/Mixed]
...

## Critical Review: [Reviewer] — Detailed Response
### Objection 1: "[Quoted objection]"
**Response:** [Our response, 2-5 sentences]

### Objection 2: "[Quoted objection]"
**Response:** ...

## Summary
[Overall assessment of the review landscape]
```

### Style Notes
- Include ALL reviews, positive and negative
- Quote objections fairly (don't strawman the critic)
- Responses should be substantive, not defensive
- If an objection is valid, ACKNOWLEDGE it and explain what we're doing about it
- The strongest objection should get the longest, most careful response
- This file is a HISTORICAL RECORD — add new reviews as they come in, but don't delete old ones

---

## 7. FAQ-[S]-[N].md

### Purpose
Anticipated and received questions from readers, seminar audiences, forum discussions, and future AI sessions. This is the LIVING companion to the paper — it grows as new questions come in. Each Q&A pair is a potential web page for hyperphysics.com.

### Required Sections

```markdown
# FAQ — [S]-[N]: [Full Title]

## Conceptual Questions

### Q: [Question in plain language]
**A:** [Clear, direct answer — 2-5 sentences. No jargon without definition.]

### Q: [Question]
**A:** [Answer]
...

## Technical Questions

### Q: [Question requiring mathematical detail]
**A:** [Answer with equations if needed, but explain the physics too.]
...

## Comparison with Standard Model

### Q: How does this differ from the SM explanation of [phenomenon]?
**A:** [Honest comparison — what CPP does differently and why.]
...

## Challenges and Limitations

### Q: What if [objection or concern]?
**A:** [Honest response — acknowledge limitations where they exist.]
...
```

### Style Notes
- Write questions as a curious, intelligent non-specialist would ask them
- Answers should be self-contained — a reader should understand the answer without reading the paper
- Start with the most common/obvious questions, end with the most technical
- The "Challenges and Limitations" section is where honest self-criticism lives — don't hide weaknesses
- This file GROWS over time: add new Q&A pairs as questions come in from any source
- Each Q&A pair should work as a standalone web page snippet (for hyperphysics.com SEO)
- Unlike reviews.md (historical record), FAQ.md is a living document that should be updated and improved

---

## 8. keywords-[S]-[N].md

### Purpose
Structured keyword data for search, SEO, and web tooling. Designed to be machine-readable by Isak's Claude Code agent for hyperphysics.com integration.

### Required Sections

```markdown
# [S]-[N] Keywords

## Primary Keywords
- [5-8 terms that MUST appear in search results for this paper]

## Secondary Keywords
- [5-10 supporting/related terms]

## PACS Codes
- [Physics and Astronomy Classification Scheme codes]

## MSC Codes
- [Mathematics Subject Classification codes]

## Elevator Pitch
[One sentence: what this paper does and why it matters.
 This can be used as a meta description for the web page.]

## SEO Notes
[Alternative phrasings, related search terms that users might type,
 suggested meta descriptions, long-tail keywords.
 This section is specifically for the Claude Code agent
 managing hyperphysics.com.]
```

### Style Notes
- Primary keywords should be specific enough to find THIS paper, not just the CPP programme
- Include both CPP jargon ("600-cell lattice") and standard physics terms ("lepton mass hierarchy")
- The Elevator Pitch should be usable as-is for a tweet, a conference abstract subtitle, or an HTML meta description
- SEO Notes should include misspellings and alternative formulations that real humans search for (e.g., "Koide relation" as well as "Koide formula")

---

## 9. changelog-[S]-[N].md

### Purpose
Canonical version archaeology for the paper. This is the single source of truth for "what changed at each version". Replaces the historical pattern of CHANGELOG comment blocks at the top of `.tex` files and visible version-history paragraphs in `.tex` title blocks (both retired Patch 0408 Session 115; codified Patch 0409 Session 116). See `operating_system.md` ``Version-archaeology architecture rule'' for the architectural justification.

### Audience
- Researchers tracing the closure trajectory
- Future AI collaborators picking up the paper after a context-window switch
- External reviewers wanting to know what changed between review rounds
- The paper's own future authors when authoring later versions

### Maintenance discipline
Unlike the 7-file canonical doc-suite (which is produced post-v1.0), `changelog-[S]-[N].md` is **maintained continuously from v0.1 onward**. Every patch that touches the paper `.tex` source beyond cosmetic whitespace adds an entry to this file in the same patch.

### Required sections

```markdown
# Changelog: [Paper title]

**Paper**: [Full paper title]
**Source**: `[full path to .tex]`
**Programme registration**: [Theorem registry anchor if any]
**OPEN-problem status**: [Open problem this paper closes / partially closes if any]
**Maintainer**: Thomas Lee Abshier ND, Hyperphysics Institute

[One-paragraph purpose statement: this file is canonical version archaeology going forward; the .tex source carries only its current title block.]

---

## Version X.Y — [Date] (Session [N], Patch [PPPP])

[Per-version narrative: what changed, why, what review items it addresses, compile result, working-sketch refs if applicable.]

---

[Earlier versions in descending order.]

---

## Working sketches (source-of-truth Tier 4 reasoning)

[List of working-sketch files this paper derives from, with brief description.]

---

## Patch register

| Patch | Session | Version | Type | Summary |
|:---:|:---:|:---:|:---|:---|
| [PPPP] | [N] | vX.Y | [Paper/Programme/Review] | [One-line summary] |

---

*Last updated: Session [N], Patch [PPPP] ([Date])*
```

### Reference implementation
`flagship_papers/capotauro/documentation_suite/changelog-capotauro.md` is the v1.0 reference implementation (Patch 0408, Session 115).

### Filename rule
Filename matches `changelog-[S]-[N].md` for series papers (e.g., `changelog-SS-9.md`, `changelog-SF-4.md`) and `changelog-<paper>.md` for flagship papers without an `[S]-[N]` identifier (e.g., `changelog-capotauro.md`).

---

## Quick Reference: What Goes Where

| "I want to know..." | Read this file |
|---------------------|---------------|
| What terms mean | glossary |
| How the physics works | mechanism |
| What's explained and predicted | phenomena |
| The honest strengths and weaknesses | philosophy |
| What external reviewers said | reviews |
| Common questions and clear answers | FAQ |
| How the paper was developed | development |
| What changed at each version | changelog |
| What to search for | keywords |

---

*This template should be consulted when generating documentation for any new CPP paper. It is stored alongside the paper formatting standard in `/CPP/templates/`.*
