# Research Frontier Architecture — Decision Document

**Location:** `/CPP/templates/Research_Frontier_Architecture.md`
**Created:** 12 April 2026
**Status:** DECIDED — ready for implementation
**Decision by:** Thomas Lee Abshier ND, with Claude Opus
**Referenced by:** `bootup.md` (session startup), `operating_system.md` (Phase 9 checklist)

---

## The Decision

CPP adopts a **three-layer problem tracking architecture**:

1. **Research_Frontier.md** — the dashboard (one flat file, fast retrieval)
2. **Problem histories** — the travelogue (one file per problem, full narrative)
3. **Papers** — the formal synthesis (theorems and proofs)

Each layer serves a different reader and a different purpose. Together they tell the complete story of CPP's evolution from open questions to proved results.

### Companion decision: Registry separation

The current `postulates_and_theorems.md` duplicates content from `axiom-registry.md` and mixes the two foundational pillars. It is replaced by:

- **`axiom-registry.md`** — what we assume. Axiom tiers, growth tracking, reduction conjectures. *(Already exists, already works well.)*
- **`theorem-registry.md`** — what we've proved. All theorems and corollaries, organised by series, with proof references and axiom dependencies. *(To be extracted from `postulates_and_theorems.md`.)*

These two files highlight the mutual dependence of CPP's foundational pillars: the axioms generate the theorems, and the growing theorem count relative to a stable axiom count is the theory's primary measure of progress.

### What gets archived after implementation

| File | Reason |
|---|---|
| `open_problems/*.md` (50+ individual files) | Absorbed into `Research_Frontier.md` + `problem_histories/` |
| `propositions.md` | Absorbed into `Research_Frontier.md` (status: PROP) |
| `solution_candidates.md` | Absorbed into frontier entries' "Current best lead" field |
| `postulates_and_theorems.md` | Split into `axiom-registry.md` (axioms) + `theorem-registry.md` (theorems) |

---

## Layer 1: Research_Frontier.md (The Dashboard)

**Location:** `/CPP/Research_Frontier.md` (root level, peer of `predictions.md`)
**Audience:** A physicist scanning CPP for the first time; a collaborator triaging what to work on next; an AI starting a new session.
**Purpose:** One flat file showing the complete landscape of every identified problem, conjecture, proposition, and frontier item — with status, sector, dependencies, and enough context to assess interconnections.
**Answers the question:** *What is solved, what is open, and what connects to what?*

### Format

Each entry gets a compact block:

```markdown
### [ID]: [Short title]
**Status:** OPEN | CONJ | PROP | THEO | FALS
**Sector(s):** SM, SS, EW, QM, SR, SD, GLOBAL
**Priority:** #1-10 or LOW/MED/HIGH
**One-line statement:** [What the problem asks]
**What a solution looks like:** [What would count as resolving this]
**Dependencies:** [Which other problems or papers block or feed this one]
**Cross-sector connections:** [How this problem touches other sectors]
**Current best lead:** [Most promising approach, if any]
**History file:** `problem_histories/PH-[ID].md`
**Paper(s):** [Which papers confront this problem]
**Last updated:** [Date]
```

### Sections (organised by status)

1. **Active Open Problems** (OPEN) — unsolved, no promising lead yet
2. **Conjectures Under Investigation** (CONJ) — proposed answer, not yet proved
3. **Propositions In Progress** (PROP) — physically motivated, partially demonstrated
4. **Recently Resolved** (THEO) — proved in a paper; kept here for one cycle then moved to section 5
5. **Resolved Archive** (THEO) — complete list of all problems that became theorems, with date and paper
6. **Falsified** (FALS) — tested and found wrong; never deleted

### Update trigger

**After every paper.** The paper production pipeline (Phase 9 in `operating_system.md`) includes updating `Research_Frontier.md`. Every paper should explicitly confront one or more open problems. When a problem changes status, update its entry and move it to the appropriate section.

---

## Layer 2: Problem Histories (The Travelogue)

**Location:** `/CPP/problem_histories/PH-[ID].md`
**Audience:** A researcher who wants to understand how a specific result was actually discovered; a future book author; anyone who wants to relive the journey.
**Purpose:** The full narrative of each problem's life — from identification through wrong turns, negative results, physical intuitions, breakthroughs, and eventual resolution (or falsification). This is the *drama* of discovery.
**Answers the question:** *How did you actually get from the open problem to the theorem?*

### Format

Each problem history is a living document that grows as the problem evolves:

```markdown
# Problem History: [ID] — [Title]

**Created:** [Date problem was first identified]
**Status:** [Current status]
**Resolved:** [Date, if applicable]
**Resolution paper:** [Paper ID, if applicable]

---

## The Problem

[Clear statement of what we're trying to solve and why it matters.
What would physics look like if we solved this? What's at stake?]

## The Journey

### [Date] — Problem Identified ([context])

[How the problem was first recognised. What prompted it.
Thomas's words if available.]

### [Date] — First Attempt: [approach] — [RESULT]

[What was tried. What happened. If negative result: what
was learned, what was ruled out. If promising: what the
lead was.

Thomas's physical intuitions preserved verbatim.
AI contributions attributed.
Dead ends documented honestly.]

### [Date] — Breakthrough / Key Insight

[The moment something clicked. What triggered it.
Who contributed what. The emotional and intellectual
arc of the discovery.]

### [Date] — Formalisation

[How the insight became a conjecture, then a proposition,
then a theorem. Which paper contains the proof.
What the reviews said.]

---

## Status Progression

| Date | Status | Event | Paper |
|------|--------|-------|-------|
| [date] | OPEN | Problem identified | — |
| [date] | CONJ | [Name] proposed [idea] | — |
| [date] | CONJ | Negative result: [what failed] | — |
| [date] | PROP | Physical mechanism identified | — |
| [date] | THEO | Proved in [Paper] Theorem N | [Paper] |

---

## Cross-References

- **Research_Frontier.md entry:** [ID]
- **Related problems:** [list]
- **Key founders_vision.md entries:** [dates]
- **Development transcripts:** [files]
- **Verification notebooks:** [files]
```

### Naming convention

- `PH-OPEN-SM-cage-1.md` — history of the scaling exponent problem
- `PH-CONJ-EW-1.md` — history of the Weinberg angle conjecture
- `PH-FALS-C-SM-2.md` — history of the falsified φ^(3(l-1)) scaling

### When to create a problem history

- When significant work begins on a problem (not at registration — that's just the frontier entry)
- When a problem produces a negative result worth documenting
- When a problem is resolved (write the complete history as part of Phase 7 documentation)

### When to update — CRITICAL

**At every advancement in or elaboration of the problem, whether vertical or lateral.**

- **Vertical advancement:** Status change (OPEN → CONJ → PROP → THEO or → FALS). These are the chapter breaks.
- **Lateral enrichment:** A new candidate approach, a negative result that narrows the solution space, Thomas describing a physical picture that reframes the problem, a cross-sector connection discovered, an AI contributing a novel perspective. These are the *substance* of the story.

Every contribution to the problem's evolution is documented. This IS the journey, the story, and should capture the contemporaneous evolutionary steps in detail. Reconstructing the story later from the paper alone would lose the drama. Each problem history is a chapter draft for the CPP book.

**Practical trigger:** After every session that touches the problem, update its history file before pushing to GitHub.

---

## Layer 3: Papers (The Formal Synthesis)

**Location:** `series_[name]/papers/[S]-[N]_[slug].tex`
**Audience:** A referee; the scientific record.
**Purpose:** Axioms, theorems, proofs, predictions. The formal result.
**Answers the question:** *Prove it.*

### Connection to the other layers

Every paper should explicitly state in its introduction which open problems it confronts:

```latex
\subsection{Open Problems Addressed}
This paper addresses OPEN-SM-cage-1 (derive the scaling exponent)
and advances CONJ-SM-9-1 (pair counting decomposition) to a
partially proved status.
```

And in its conclusion, update the status:

```latex
\subsection{Problem Status After This Paper}
\begin{itemize}
\item OPEN-SM-cage-1: PARTIALLY RESOLVED (7/3 decomposed; rigorous proof pending)
\item CONJ-SM-9-1: CONJECTURED → PARTIALLY SUPPORTED
\item NEW: OPEN-SM-10-FEM (FEM simulation for first-principles derivation)
\end{itemize}
```

---

## Nomenclature

### Simplified prefix convention

Since all items in the frontier are problems at various stages, the OPEN-P prefix is redundant. The simplified convention:

| Prefix | Meaning | Example |
|--------|---------|---------|
| OPEN-[sector]-[name] | Open problem | OPEN-SM-cage-1 |
| CONJ-[sector]-[name] | Conjecture | CONJ-EW-1 |
| PROP-[sector]-[name] | Proposition | PROP-SM-cage-bound |
| THEO-[sector]-[name] | Theorem (resolved) | THEO-SM8-3 |
| FALS-[sector]-[name] | Falsified | FALS-C-SM-2 |

Problem history files use the `PH-` prefix: `PH-OPEN-SM-cage-1.md`, `PH-CONJ-EW-1.md`.

### Sector codes

SM (Standard Model), SS (Strong Sector), EW (Electroweak), QM (Quantum Mechanics), SR (Relativity), SD (Superdeterminism/Foundations), GLOBAL (cross-cutting).

---

## The Lifecycle

```
IDENTIFIED → OPEN → CONJ → PROP → THEO
                 ↘              ↗
                  → FALS ←——————
```

| Stage | Meaning | What triggers advancement |
|-------|---------|--------------------------|
| **OPEN** | Problem identified, no candidate solution | Registration in Research_Frontier.md |
| **CONJ** | A proposed answer exists but is not proved | Someone proposes a specific mechanism or formula |
| **PROP** | Physically motivated, partially demonstrated | Computation or argument supports it but gaps remain |
| **THEO** | Proved from axioms in a paper | Formal proof accepted through multi-AI review |
| **FALS** | Tested and found wrong | Explicit computation or argument shows failure |

**Key rules:**
- Items can skip stages (OPEN → THEO happens when a breakthrough solves it outright)
- Items can regress (CONJ → FALS, PROP → FALS)
- The history file documents every transition AND every lateral enrichment
- The frontier file gets one entry updated per transition
- The paper contains the formal result

---

## The Registries (Settled Results)

### axiom-registry.md — What We Assume *(already exists)*

The axiom registry tracks every postulated rule of CP behaviour: axiom tiers, where each axiom is used, what it predicts, growth tracking, and reduction conjectures. The axiom-to-prediction ratio is the primary health metric of the theory.

### theorem-registry.md — What We've Proved *(to be created)*

Extracted from `postulates_and_theorems.md`. Contains all theorems and corollaries organised by series, with proof references and explicit axiom dependencies. Includes:

- Theorems by series (SS, SM, QM, EW, SD)
- Corollaries
- Cross-reference to axiom dependencies
- Count tracking: total theorems, theorems per axiom

The two registries together tell the story of CPP's deductive structure: a small set of axioms generating a growing body of proved results.

---

## Implementation Plan

### Phase 1: Build Research_Frontier.md (1 session)
1. Read all 50+ files in `open_problems/`
2. Read conjectures from `postulates_and_theorems.md`
3. Read `propositions.md`
4. Read `solution_candidates.md`
5. Consolidate into one flat file with the format above
6. Verify nothing is lost

### Phase 2: Extract theorem-registry.md (same session or next)
1. Extract all theorems and corollaries from `postulates_and_theorems.md`
2. Organise by series
3. Add axiom dependency cross-references
4. Verify `axiom-registry.md` has no theorem content that should move

### Phase 3: Build first batch of problem histories (2-3 sessions)

Start with the problems that have the richest stories:

| Priority | ID | Why |
|---|---|---|
| 1 | OPEN-SM-cage-1 | Scaling exponent — the central open problem |
| 2 | CONJ-EW-1 | Weinberg angle — the most celebrated result |
| 3 | THEO-SM8-3 | Three generations — the biggest structural discovery |
| 4 | FALS-C-SM-2 | φ^(3(l-1)) falsification — the most important negative result |
| 5 | OPEN-SM-10-FEM | FEM simulation — the #1 priority forward project |
| 6 | PROP-SM-cage-bound | SM particles as cage-bound structures — foundational proposition underlying the entire cage programme. Central to nearly every SM paper. Evolution from Thomas's physical intuition through cage hierarchy discovery is one of the great CPP stories. |

Draw from: development transcripts, `founders_vision.md` catalogue entries, paper development logs, session histories.

### Phase 4: Update pipeline (quick)
1. Add `Research_Frontier.md` update to `operating_system.md` Section 10 checklist
2. Add problem history update to Phase 7 documentation suite
3. Add "Open Problems Addressed" and "Problem Status After This Paper" to `paper-formatting.md` template
4. Update `bootup.md`:
   - Add `Research_Frontier.md` to the session startup reading sequence
   - Reference this architecture document as a module of `operating_system.md` to be reviewed in the bootup sequence for new Opus sessions

### Phase 5: Consolidation (1 session)
1. Once `Research_Frontier.md` and `theorem-registry.md` are verified complete:
   - Archive `open_problems/` individual files
   - Archive `propositions.md`
   - Archive `solution_candidates.md`
   - Archive `postulates_and_theorems.md`
2. Verify all content is captured in the new structure
3. Update all cross-references in other documents

---

## Why This Works for CPP

CPP is unusual in that it has a 39-year development history, multiple AI collaborators generating results at high speed, and a founder whose physical intuitions drive every breakthrough. The standard academic approach — bury the journey in supplementary material — loses the most valuable part of the story. The problem history layer preserves it.

Thomas's vision: *"Every one of these problem-resolution passages will be its own chapter, its own saga. People will enjoy the drama of following the twists and turns of discovery. It will make it a lot easier to write the book. It will allow researchers to relive the excitement and journey we experienced as we saw it evolve from a problem to a theorem."*

The three layers serve three timescales:
- **Research_Frontier.md** — what matters *right now* (session planning, triage)
- **Problem histories** — what happened *over weeks and months* (the research arc)
- **Papers** — what stands *permanently* (the formal record)

And the two registries anchor the deductive structure:
- **axiom-registry.md** — the foundations (what we assume)
- **theorem-registry.md** — the edifice (what we've built)

---

*Decision document prepared 12 April 2026.*
*Implementation begins when Thomas schedules a dedicated session for Phase 1.*
*This document is referenced by `bootup.md` and `operating_system.md`.*
