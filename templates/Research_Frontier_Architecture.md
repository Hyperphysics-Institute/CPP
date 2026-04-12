# Research Frontier Architecture — Decision Document

**Location:** `/CPP/open_problems/Research_Frontier_Architecture.md`
**Created:** 12 April 2026
**Status:** DECIDED — ready for implementation
**Decision by:** Thomas Lee Abshier ND, with Claude Opus

---

## The Decision

CPP adopts a **three-layer problem tracking architecture**:

1. **Research_Frontier.md** — the dashboard (one flat file, fast retrieval)
2. **Problem histories** — the travelogue (one file per problem, full narrative)
3. **Papers** — the formal synthesis (theorems and proofs)

Each layer serves a different reader and a different purpose. Together they tell the complete story of CPP's evolution from open questions to proved results.

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

- `PH-OPEN-P-SM-cage-1.md` — history of the scaling exponent problem
- `PH-CONJ-EW-1.md` — history of the Weinberg angle conjecture
- `PH-FALS-C-SM-2.md` — history of the falsified φ^(3(l-1)) scaling

### When to create a problem history

- When significant work begins on a problem (not at registration — that's just the frontier entry)
- When a problem produces a negative result worth documenting
- When a problem is resolved (write the complete history as part of Phase 7 documentation)

### When to update

- After every session that touches the problem
- After every review that provides insight on the problem
- After resolution — write the complete "looking back" narrative

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
This paper addresses OPEN-P-SM-cage-1 (derive the scaling exponent)
and advances CONJ-SM-9-1 (pair counting decomposition) to a
partially proved status.
```

And in its conclusion, update the status:

```latex
\subsection{Problem Status After This Paper}
\begin{itemize}
\item OPEN-P-SM-cage-1: PARTIALLY RESOLVED (7/3 decomposed; rigorous proof pending)
\item CONJ-SM-9-1: CONJECTURED → PARTIALLY SUPPORTED
\item NEW: OPEN-P-SM-10-FEM (FEM simulation for first-principles derivation)
\end{itemize}
```

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

**Key rule:** Items can skip stages (OPEN → THEO happens when a breakthrough solves it outright) and can regress (CONJ → FALS, PROP → FALS). The history file documents every transition.

---

## Implementation Plan

### Phase 1: Build Research_Frontier.md (1 session)
1. Read all 50+ files in `open_problems/`
2. Read conjectures from `postulates_and_theorems.md`
3. Read `propositions.md`
4. Read `solution_candidates.md`
5. Consolidate into one flat file with the format above
6. Verify nothing is lost

### Phase 2: Retrofit Problem Histories (2-3 sessions)
1. Start with the 5-10 most important problems (the ones with the richest stories)
2. Draw from: development transcripts, `founders_vision.md` catalogue entries, paper development logs, session histories
3. Build the narrative for each

**Priority problems for first batch:**
- PH-OPEN-P-SM-cage-1 (scaling exponent — the central open problem)
- PH-CONJ-EW-1 (Weinberg angle — the most celebrated result)
- PH-THEO-SM8-3 (three generations — the biggest structural discovery)
- PH-FALS-C-SM-2 (φ^(3(l-1)) falsification — the most important negative result)
- PH-OPEN-P-SM-10-FEM (FEM simulation — the #1 priority forward project)

### Phase 3: Update Pipeline (quick)
1. Add `Research_Frontier.md` update to `operating_system.md` Section 10 checklist
2. Add problem history update to Phase 7 documentation suite
3. Add "Open Problems Addressed" and "Problem Status After This Paper" to `paper-formatting.md` template
4. Update `bootup.md` to reference `Research_Frontier.md` in the session startup sequence

### Phase 4: Consolidation (1 session)
1. Once `Research_Frontier.md` is verified complete, the 50+ individual files in `open_problems/` become redundant
2. Options: archive them, or keep them as stubs pointing to the frontier file
3. `propositions.md` and `solution_candidates.md` content is absorbed into the frontier
4. `postulates_and_theorems.md` keeps axioms and theorems only (the settled results)

---

## What This Replaces

| Old location | Content | New home |
|---|---|---|
| `open_problems/*.md` (50+ files) | Individual problem statements | `Research_Frontier.md` (dashboard) + `problem_histories/` (narratives) |
| `propositions.md` | Physically motivated claims | `Research_Frontier.md` (status: PROP) |
| `solution_candidates.md` | Candidate solutions | `Research_Frontier.md` (entries' "Current best lead" field) |
| Conjectures in `postulates_and_theorems.md` | Proposed theorems | `Research_Frontier.md` (status: CONJ) |
| `postulates_and_theorems.md` axioms + theorems | Settled results | **Stays** — this file keeps the proved results |
| `predictions.md` | Quantitative predictions | **Stays** — this file is already the right format |
| `axiom-registry.md` | Axiom tracking | **Stays** — this file is already the right format |

---

## Why This Works for CPP

CPP is unusual in that it has a 39-year development history, multiple AI collaborators generating results at high speed, and a founder whose physical intuitions drive every breakthrough. The standard academic approach — bury the journey in supplementary material — loses the most valuable part of the story. The problem history layer preserves it.

Thomas's vision: *"People will enjoy the drama of following the twists and turns of discovery. It will make it a lot easier to write the book."*

The three layers serve three timescales:
- **Research_Frontier.md** — what matters *right now* (session planning, triage)
- **Problem histories** — what happened *over weeks and months* (the research arc)
- **Papers** — what stands *permanently* (the formal record)

---

*Decision document prepared 12 April 2026.*
*Implementation begins when Thomas schedules a dedicated session for Phase 1.*
