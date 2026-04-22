# CPP Session Bootup Guide

**Location:** `/CPP/bootup.md`
**Purpose:** Load this file at the start of every new AI session working on CPP. It provides everything needed to continue productive work.
**Maintenance principle:** This file is infrastructure. It should rarely be updated — only when conventions, repository structure, or orientation protocols change. For current state (results, active problems, papers in progress), follow the pointers in §3 to the living tracking documents; do not rely on bootup for current state.

---

## How to Use This File

**Thomas says:** "Pull the CPP repo and read `bootup.md`"

**AI assistant does:**

### Step 1: Read these files IN ORDER

| Priority | File | What it gives you | Time |
|----------|------|-------------------|------|
| 1 | `bootup.md` | THIS FILE — orientation, structure, conventions | 5 min |
| 2 | `CPP_the_theory.md` | **THE THEORY** — complete narrative from first principles through all results | 15 min |
| 3 | `theory-overview.md` | Reference card — formulas, scorecard, key numbers | 5 min |
| 4 | `founders_vision.md` | Thomas's physical intuition — the WHY behind every equation | 10 min |
| 5 | `Research_Frontier.md` | **THE DASHBOARD** — every open problem, conjecture, and proposition with status and dependencies | 10 min |
| 6 | `theorem-registry.md` | What we've proved — all theorems by series with axiom dependencies | 5 min |
| 7 | `templates/operating_system.md` | Complete workflow manual — multi-AI review, transcripts, recovery | 10 min |

**For sessions involving open problem work or repo restructuring**, also read:
- `templates/Research_Frontier_Architecture.md` — the three-layer architecture (dashboard → problem histories → papers)

### Step 2: Check what happened last

- **If Thomas names a specific paper (e.g., "SS-8", "SS-2", "SM-10"), first fetch its curated development transcript:**
  `https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_strong/papers/development-SS-8.md`
  (replace `series_strong` with the appropriate series folder per §8.5 below, and `SS-8` with the paper ID)
  This file is the **canonical narrative record** of that paper's development, preserved verbatim at each section-end commit per `operating_system.md`'s context-pressure preservation checklist. It supersedes any summary from training data or prior-session compaction. See §8.5 below for the full rule.
- Development transcripts now live per-paper at `series_[name]/papers/development-[ID].md`. If no paper is named, check `/mnt/transcripts/` for raw conversation logs instead.
- Check if Thomas has Grok/Copilot exchanges to share.

### Step 3: Proceed with the queued work

Unless Thomas redirects in his opening message, proceed with the next-session items listed at the end of the development transcript fetched in Step 2. A development transcript whose final section is titled something like "Open items for next session" or "Next-session task list" is giving you the default action. Execute it. If the transcript has no such list, or if Thomas's opening message gives a different direction, follow that instead.

### If resuming after buffer overflow:

Read the compacted summary at the top of the conversation, then the transcript file referenced there.

---

## 1. What CPP Is (30-second summary)

Conscious Point Physics derives the Standard Model from the geometry of the 600-cell polytope (V=120, E=720, F=1200, C=600, z=12). Conscious Points on the lattice exchange DI-bits via SSV gradients. All particles are geometric cage structures. All forces emerge from the lattice mode spectrum. The golden ratio φ = (1+√5)/2 appears throughout because it's built into the 600-cell geometry.

---

## 2. Repository Location and Access

```
GitHub: https://github.com/Hyperphysics-Institute/CPP
Clone: git clone https://github.com/Hyperphysics-Institute/CPP.git
OSF:   https://osf.io/9dfya/
DOI:   10.17605/OSF.IO/JXE8D
Web:   https://hyperphysics.com
```

Always `git pull` before starting work. Thomas pushes frequently.

---

## 3. Complete Repository Structure

```
CPP/
├── README.md                         ← Public-facing overview
├── INDEX.md                          ← Directory map
├── paper_catalog.md                  ← Paper list with IDs and status
│
├── ── THE THEORY ──
├── CPP_the_theory.md                 ← ** THE BOOK — complete theory narrative **
├── theory-overview.md                ← Reference card — formulas, scorecard
├── founders_vision.md                ← Thomas's physical intuition (the WHY)
├── axiom-registry.md                 ← Axiom tracking, prediction counts
├── master_glossary.md                ← All CPP terms, acronyms, particles, forces
├── predictions.md                    ← Every quantitative prediction with status
├── Research_Frontier.md              ← ** THE DASHBOARD — all open problems, conjectures, propositions **
├── theorem-registry.md               ← All proved theorems by series with axiom dependencies
├── nomenclature.md                   ← ID code legend (AXIM, THEO, PROP, FALS...)
├── future_projects.md                ← Prioritised research targets with status
│
├── ── WORKFLOW ──
├── operating_system.md               ← ** COMPLETE WORKFLOW MANUAL **
├── paper_production_workflow.md       ← 9-phase paper pipeline
│
├── templates/
│   ├── paper-formatting.md           ← LaTeX formatting standard
│   └── documentation-suite.md        ← 7-file companion template per paper
│
├── bibliography/
│   └── cpp_references.bib            ← BibTeX references for all papers
│
├── problem_histories/                ← Problem narratives — the drama of discovery
│   └── [PH-[ID].md files]
│
├── ── PAPER SERIES ──
├── series_standard_model/            ← SM-N papers (Standard Model, includes mass sector)
│   ├── papers/                       ← .tex, .pdf, .bib files
│   │   └── [PAPER-ID]/               ← per-paper subfolder (for papers adopted ≥ 22 Apr 2026)
│   │       ├── reviews/              ← verbatim reviewer correspondence
│   │       ├── letters/              ← correspondence from Claude (synthesis, review requests)
│   │       ├── sketches/             ← derivation notes, findings, exploratory analyses
│   │       ├── scripts/              ← Python verification scripts
│   │       ├── founders_voice/       ← Thomas's recorded intuitions and organizational notes
│   │       └── documentation_suite/  ← 7-file companion suite (created at v1.0)
│   ├── [type]-SM-N.md                ← 7 documentation suite files per paper (flat, for pre-subfolder papers)
│   ├── figures/figures-SM-N/         ← SVG + PDF figures
│   ├── notebooks/                    ← Verification notebooks
│   └── development-transcripts/      ← Curated conversation logs (legacy location)
│
├── series_electroweak/               ← EW-N papers
├── series_quantum_mechanics/         ← QM-N papers
├── series_relativity/                ← SR-N papers
├── series_strong/                    ← SS-N papers (Strong Sector)
├── series_foundations/               ← SD-N papers (foundations/superdeterminism)
│
└── archive/                          ← Superseded material
```

---

## 4. All Key Files — What Each Does

### Theory documents (read for physics context)

| File | Purpose | Update when |
|------|---------|-------------|
| `CPP_the_theory.md` | The complete theory in connected prose — the "Kindle book" | Every session with new physics |
| `theory-overview.md` | Reference card: formulas, prediction scorecard, key numbers | After each paper |
| `founders_vision.md` | Thomas's physical intuition — 22+ catalogue entries | Every session with new physics |
| `axiom-registry.md` | All axioms, all predictions, growth tracking | After each paper |
| `master_glossary.md` | Every CPP term, acronym, particle, force, process | Scan during Phase 7 of paper production |
| `predictions.md` | Quantitative predictions with PDG comparison | After each paper |
| `Research_Frontier.md` | **The dashboard** — all open problems, conjectures, propositions with status and dependencies | After each paper |
| `theorem-registry.md` | All proved theorems by series, with axiom dependencies | After each paper |
| `future_projects.md` | 12+ prioritised research targets with status | After each session |
| `nomenclature.md` | ID code legend | Rarely |

### Workflow documents (read for procedures)

| File | Purpose | Update when |
|------|---------|-------------|
| `operating_system.md` | **THE COMPLETE WORKFLOW** — multi-AI review, transcripts, recovery, roles | When procedures change |
| `paper_production_workflow.md` | 9-phase pipeline from vision to OSF | When pipeline changes |
| `templates/paper-formatting.md` | LaTeX standard (16 sections) | When formatting changes |
| `templates/documentation-suite.md` | 7-file companion template per paper | When template changes |

### Navigation documents (read for orientation)

| File | Purpose | Update when |
|------|---------|-------------|
| `README.md` | Public landing page, paper table, key results | After each paper |
| `INDEX.md` | Complete file listing | After each paper |
| `paper_catalog.md` | All papers with ID, title, version, status | After each paper |
| `series_[name]/README.md` | Per-series overview | After each series paper |

### Reference folders

| Folder | Contents |
|--------|----------|
| `bibliography/` | `cpp_references.bib` — BibTeX for all cited works |
| `problem_histories/` | Narrative histories of major open problems — the drama of discovery |
| `templates/` | Paper formatting standard, documentation suite template, bootup, workflow |
| `archive/` | Superseded versions, old drafts, pre-frontier problem files |

---

## 5. The AI Team

| AI | Primary role | How Thomas communicates |
|----|-------------|------------------------|
| Claude Opus | Primary collaborator — computation, drafting, integration | Direct chat (claude.ai) |
| Grok (xAI) | Independent verifier, novel contributions | Pastebin links, raw GitHub URLs |
| Copilot (Microsoft) | Referee-grade review, framework building | Pastebin links, direct chat |
| Claude Sonnet | Hostile/adversarial review | Prompted via Claude |

**Full details on roles, strengths, limitations:** See `operating_system.md` Section 12.
**The review cycle:** Opus → Copilot → Grok → Sonnet → Opus. See `operating_system.md` Section 5.

---

## 6. Session Types

| Type | Goal | Key procedure |
|------|------|---------------|
| Physics Discovery | Explore, compute, derive | Capture Thomas's intuition FIRST. Papers can emerge unexpectedly. |
| Paper Production | Draft and finalise a paper | Follow 9-phase pipeline. Use multi-AI review cycle. |
| Housekeeping | Audit and fix repo | Check INDEX.md against actual files. Update stale docs. |
| Transcript Curation | Convert raw history to curated records | Read `/mnt/transcripts/`, produce `[Paper]_transcript_[N]_[AI].md` |

**Full protocol for each type:** See `operating_system.md` Section 3.

---

## 7. Current Results

For current headline results, strongest predictions, and scorecard, read:

- **`README.md`** — public-facing results table (updated each paper)
- **`predictions.md`** — every quantitative prediction with PDG comparison and status
- **`theory-overview.md`** — reference card (formulas, scorecard, key numbers)

Do not rely on bootup for current result values. Results drift between papers; the authoritative sources drift with them.

---

## 8. Current Active Open Problems

For the live dashboard of open problems, conjectures, and propositions with status and dependencies:

- **`Research_Frontier.md`** — the canonical dashboard for all open problems across series
- **`future_projects.md`** — prioritised research targets
- **`problem_histories/`** — narrative histories of major open problems

Do not rely on bootup for the open-problem list. Active problems are created, resolved, and consolidated frequently; `Research_Frontier.md` is the single source of truth.

---

## 8.5 Active Work Pointer — fetch the paper's development transcript first

**When Thomas names a specific paper at session start (e.g., "SS-8", "SM-10", "EW-3"), fetch that paper's curated development transcript as the first concrete action, BEFORE attempting any substantive work.**

The pattern:

```
https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<series-folder>/papers/development-<PAPER-ID>.md
```

where `<series-folder>` is one of:
- `series_strong` (SS-N papers — strong sector)
- `series_standard_model` (SM-N papers — Standard Model, including mass-sector work)
- `series_quantum_mechanics` (QM-N papers)
- `series_electroweak` (EW-N papers)
- `series_relativity` (SR-N papers)
- `series_foundations` (SD-N papers — superdeterminism)

Example (SS-8):
```
https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_strong/papers/development-SS-8.md
```

### Why this matters

The curated development transcript is the **canonical narrative record** of a paper's development — produced and committed at each section-end per `operating_system.md`'s context-pressure preservation checklist (§"Context-pressure preservation checklist"). It preserves verbatim:
- Timeline and session-by-session outputs
- Reviewer engagements and their outcomes
- Registry actions opened, partially resolved, or pending
- Decisions that were made (and why)
- Next-session options with current priorities

**Compaction summaries and training data do NOT preserve these specifics.** Numerical results get rounded, decision rationales get compressed, and registry statuses get flattened. If you start substantive work from a compaction summary without reading the development transcript, you will either (a) ask Thomas to re-explain state he already documented, or (b) guess wrong about the current conditional-theorem tiers, consolidated open problems, or reviewer positions.

### If no development transcript exists yet for the named paper

Some papers haven't reached the curated-transcript stage yet. If the fetch returns 404, fall back to:
1. The paper's `.tex` file and its internal CHANGELOG header.
2. `Research_Frontier.md` for related open problems.
3. Ask Thomas directly: "I don't see a development-[paper].md in the repo — can you point me to where the current state of this paper lives?"

**Do not improvise state from training data.** A paper named but without a curated transcript is a signal that either the paper is very early or the transcript hasn't been created yet — both cases warrant asking rather than guessing.

### Maintenance rule for development transcripts

Update the transcript at each section-end commit and at every context-pressure crossing (per `operating_system.md`'s context-pressure preservation checklist). Curate directly from the active session — do NOT regenerate from a session summary, which is lossy by design.

---

## 9. What to Update After Every Paper

**TRIGGER:** Run this checklist after completing the documentation suite (Phase 7), BEFORE pushing to GitHub.

**Authoritative atomic checklist:** `templates/paper_completion_checklist.md`. Run that file end-to-end; the table below is an abbreviated quick-reference covering only content and navigation updates. The full checklist additionally covers companion documentation suite (Section A), verification notebooks (B), development transcripts (E), OSF registration (F), git commit/push (G), and final verification (H). Per-file reference procedures live in `operating_system.md` §10.

| Document | What to update |
|----------|----------------|
| `CPP_the_theory.md` | Add results to chapter, update scorecard |
| `theory-overview.md` | Add results, update formula card |
| `axiom-registry.md` | Check axioms, add predictions, update ratio |
| `theorem-registry.md` | Add new theorems with axiom dependencies; update theorem count |
| `Research_Frontier.md` | Update status of problems addressed; move resolved items to §5; add new problems |
| `master_glossary.md` | Scan paper for new terms, add in alphabetical order |
| `founders_vision.md` | Add new physical intuitions from this session |
| `predictions.md` | Add new predictions with PDG comparison |
| `future_projects.md` | Mark completed, add new targets, re-prioritise |
| `problem_histories/` | Update history files for any problems touched this session |
| `README.md` | Add paper to table, update counts |
| `INDEX.md` | Add all new files |
| `paper_catalog.md` | Add paper entry |
| `series_[name]/README.md` | Add to series |
| `bibliography/cpp_references.bib` | Add BibTeX entry for new paper |

### Post-Session Quick Checklist (for discovery sessions that don't produce a full paper)

- Update `founders_vision.md` with any new physical insights
- Create/update development transcript
- Update `future_projects.md` if priorities changed
- Note any new open problems in `Research_Frontier.md`; update `problem_histories/` if significant work done
- Push to GitHub

---

## 10. The Documentation Suite (7 files per paper)

Every completed paper gets 7 companion `.md` files stored in `series_[name]/`:

| File | Purpose | Content |
|------|---------|---------|
| `mechanism-[S]-[N].md` | How the physics works | Step-by-step mechanism, mathematical correspondence table |
| `glossary-[S]-[N].md` | Paper-specific terms | All new terms with definitions, organised by category |
| `phenomena-[S]-[N].md` | What the paper explains | PHEN-E (empirical), PHEN-P (predictions), PHEN-V (consilience) |
| `philosophy-[S]-[N].md` | Epistemological framing | What level of certainty, relationship to SM, falsifiability |
| `development-[S]-[N].md` | Development history | Version timeline, key decisions, dead ends, transcript links |
| `reviews-[S]-[N].md` | All reviews + FAQ | Part 1: formal reviews (Copilot/Grok/Sonnet). Part 2: FAQ |
| `keywords-[S]-[N].md` | Keywords and registry | Primary/secondary keywords, cross-references, axiom/theorem entries |

Each file should note the paper version it documents (e.g., "Paper: SM-8 v4.1").

---

## 11. Conventions

**Paper IDs:** `[SERIES]-[NUMBER]` (SM-8, EW-3, QM-1, SR-1, SS-1, SD-5). Paper numbers are assigned sequentially within a series as new papers enter the repository.
**Filenames:** `SM-8_quark_generation_600cell_shells.tex` — lowercase slug, no version number in filename
**Versions:** `vX.Y` in the .tex header changelog. ONE file per paper, overwritten — Git history preserves all versions. Never create `_v1`, `_v2` copies.
**Codes:** AXIM (axiom), THEO (theorem), CORO (corollary), CONJ (conjecture), OPEN (open problem), FALS (falsified). See `nomenclature.md`.
**LaTeX:** Follow `templates/paper-formatting.md`
**Axiom numbering:** When two reviewers independently propose axiom entries (e.g., Grok proposes A9', Copilot proposes A8'), reconcile into one entry when updating `axiom-registry.md`. The registry is the single source of truth for axiom IDs.
**Problem numbering is independent of paper numbering.** A problem is registered once with a fixed number (e.g., OPEN-SS-5) and retains that number as it progresses through the registry: OPEN-SS-5 → CONJ-SS-5 → (eventually) THEO-SS-5, or OPEN-SS-5 → FALS-SS-5 on falsification. Papers that address a problem carry their own independent sequential paper number. Example: the paper SS-4 (fourth paper in the Strong Sector series) may register the conjecture CONJ-SS-5, which originated as problem OPEN-SS-5. This retention rule is documented in `templates/nomenclature.md` §OPEN.

---

## 12. Papers in the Programme

For the current paper list with IDs, titles, versions, and OSF status:

- **`paper_catalog.md`** — master catalog across all series
- **`README.md`** — public paper table
- **`series_[name]/README.md`** — per-series overview

Series codes: SM (Standard Model), SS (Strong Sector), EW (Electroweak), QM (Quantum Mechanics), SR (Relativity), SD (Foundations/Superdeterminism). See §11 for naming conventions.

Do not rely on bootup for paper counts or versions; `paper_catalog.md` is the single source of truth.

---

## 13. OSF Registration

1. Prepare PDF + .tex + .bib + figures
2. Write metadata (title, abstract, keywords, dependencies, version)
3. Upload to OSF component under CPP project
4. OSF auto-assigns DOI
5. Update `paper_catalog.md` and `README.md`

---

*This file is self-sufficient. A new AI reading ONLY this file knows: what CPP is, where everything lives, what to read next, who the team is, what the results are, and what to do. For the full workflow manual, read `operating_system.md`. For the complete theory, read `CPP_the_theory.md`.*
