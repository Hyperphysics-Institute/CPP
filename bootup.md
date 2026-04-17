# CPP Session Bootup Guide

**Location:** `/CPP/bootup.md`
**Purpose:** Load this file at the start of every new AI session working on CPP. It provides everything needed to continue productive work.
**Last updated:** 16 April 2026

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

- Read the most recent transcript in `series_standard_model/development-transcripts/`
- Check `/mnt/transcripts/` for raw conversation logs
- Check if Thomas has Grok/Copilot exchanges to share

### Step 3: Ask Thomas

"What would you like to work on today?"

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
├── series_standard_model/            ← SM-1 through SM-10
│   ├── papers/                       ← .tex, .pdf, .bib files
│   ├── [type]-SM-N.md                ← 7 documentation suite files per paper
│   ├── figures/figures-SM-N/         ← SVG + PDF figures
│   ├── notebooks/                    ← Verification notebooks
│   └── development-transcripts/      ← Curated conversation logs
│
├── series_electroweak/               ← EW-1 through EW-5
├── series_quantum_mechanics/         ← QM-1 through QM-6
├── series_relativity/                ← SR-1
├── series_strong/                    ← SS-1
├── series_foundations/               ← SD-1 through SD-5
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

## 7. Strongest Current Results (April 2026)

### Zero-Parameter Formula (SM-8 v4.1 + SM-9 v2.2)

```
M_q = m_e (z/φ) V^(7/3)           q = s, c, b
M_t = m_e (z/φ) V_t^(7/3) × 16   q = t
```

RMS = 2.1% across four orders of magnitude, **zero free parameters**.

| Prediction | CPP | Experimental | Error | Params |
|-----------|-----|-------------|-------|--------|
| m_s (zero-param) | 96.3 MeV | 93.4 MeV | +3.1% | 0 |
| m_c (zero-param) | 1,249 MeV | 1,270 MeV | −1.6% | 0 |
| m_b (zero-param) | 4,115 MeV | 4,180 MeV | −1.6% | 0 |
| m_t (zero-param) | 169,571 MeV | 172,760 MeV | −1.8% | 0 |
| m_t (calibrated, v3.x) | 172,800 MeV | 172,760 MeV | 0.02% | 2 |
| sin²θ_W | 3/(8φ) = 0.2312 | 0.23121 | 0.24% | 0 |
| m_μ (Koide) | 105.66 MeV | 105.66 MeV | <0.01% | 1 cal |
| m_τ (Koide) | 1776.9 MeV | 1776.9 MeV | <0.01% | 1 cal |
| # Generations | 3 | 3 | exact | 0 |

Axiom count: 7 (plus A8', A9'). Predictions: 15+. Ratio: 0.47.

---

## 8. Currently Active Open Problems

1. **OPEN-P-SM-cage-1:** Rigorous derivation of α = 7/3 from cage geometry (partially resolved in SM-9; FEM target in SM-10)
2. **OPEN-P-SM-cage-7:** Why does C(n,2) predict m_b/m_s to 0.6%?
3. **OPEN-P-SM-cage-3:** Connect cage 2/3 fraction to Koide K = 2/3
4. **OPEN-P-SM-cage-6:** Apply cage model to leptons
5. **OPEN-P-FV-1:** SSV_abs → Lorentz factor (SR-1 re-derivation)
6. **SM-10 FEM Simulation:** First-principles quark mass from chain network simulation — the #1 priority forward project. Phase 1 (CPU proof-of-concept) can be attempted immediately.
7. **Strange quark residual (+3.1%):** Largest error in zero-parameter formula. Candidate explanations: absent surface blanket, chiral condensate coupling, ZBW instability.
8. **OPEN-SS-16 (Layer B Gap):** Derive operator formalism and system-bath coupling from CPP primitives. Closes the Layer B gap across SM-3, SS-3, and all future papers. **Highest-leverage single piece of work remaining.** Target paper: SS-4.

Full list: `Research_Frontier.md` and `future_projects.md`.

---

## 9. What to Update After Every Paper

**TRIGGER:** Run this checklist after completing the documentation suite (Phase 7), BEFORE pushing to GitHub. Full procedures in `operating_system.md` Section 10.

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

## 12. Papers in the Programme (April 2026)

| Series | Papers | Status |
|--------|--------|--------|
| Standard Model (SM) | SM-1 through SM-10 | SM-1–7 on OSF; SM-8 v4.1 ready; SM-9 v2.2 ready; SM-10 v0.1 proposal |
| Electroweak (EW) | EW-1 through EW-5 | On OSF |
| Quantum Mechanics (QM) | QM-1 through QM-6 | On OSF |
| Relativity (SR) | SR-1 | On OSF |
| Strong Sector (SS) | SS-1, SS-2, SS-3 | SS-1 on OSF; SS-2 v1.0 pending; SS-3 v1.3 submission-ready |
| Foundations (SD) | SD-1 through SD-5 | On OSF |

Total: 28 papers. Full details: `paper_catalog.md`.

---

## 13. OSF Registration

1. Prepare PDF + .tex + .bib + figures
2. Write metadata (title, abstract, keywords, dependencies, version)
3. Upload to OSF component under CPP project
4. OSF auto-assigns DOI
5. Update `paper_catalog.md` and `README.md`

---

*This file is self-sufficient. A new AI reading ONLY this file knows: what CPP is, where everything lives, what to read next, who the team is, what the results are, and what to do. For the full workflow manual, read `operating_system.md`. For the complete theory, read `CPP_the_theory.md`.*
