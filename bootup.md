# CPP Session Bootup Guide

**Location:** `/CPP/templates/bootup.md`
**Purpose:** Load this file at the start of every new AI session working on CPP. It provides everything needed to continue productive work.
**Last updated:** 8 April 2026

---

## How to Use This File

**Thomas says:** "Pull the CPP repo and read `templates/bootup.md`"

**AI assistant does:**

### Step 1: Read these files IN ORDER
| Priority | File | What it gives you | Time |
|----------|------|-------------------|------|
| 1 | `templates/bootup.md` | THIS FILE — orientation, structure, conventions | 5 min |
| 2 | `CPP_the_theory.md` | **THE THEORY** — complete narrative from first principles through all results | 15 min |
| 3 | `theory-overview.md` | Reference card — formulas, scorecard, key numbers | 5 min |
| 4 | `founders_vision.md` | Thomas's physical intuition — the WHY behind every equation | 10 min |
| 5 | `operating_system.md` | Complete workflow manual — multi-AI review, transcripts, recovery | 10 min |

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
├── postulates_and_theorems.md        ← Formal AXIM, THEO, CORO, CONJ entries
├── propositions.md                   ← Physically motivated claims
├── nomenclature.md                   ← ID code legend (AXIM, THEO, PROP, FALS...)
├── solution_candidates.md            ← Candidate solutions for open problems
├── future_projects.md                ← Prioritised research targets with status
│
├── ── WORKFLOW ──
├── operating_system.md               ← ** COMPLETE WORKFLOW MANUAL **
├── paper_production_workflow.md       ← 9-phase paper pipeline
│
├── templates/
│   ├── bootup.md                     ← ** THIS FILE **
│   ├── paper-formatting.md           ← LaTeX formatting standard
│   └── documentation-suite.md        ← 8-file companion template per paper
│
├── bibliography/
│   └── cpp_references.bib            ← BibTeX references for all papers
│
├── open_problems/                    ← 50+ registered OPEN-P entries
│   └── [OPEN-P-XX-N.md files]
│
├── ── PAPER SERIES ──
├── series_standard_model/            ← SM-1 through SM-9
│   ├── papers/                       ← .tex, .pdf, all .md companion docs
│   ├── figures/figures-SM-N/         ← SVG + PDF figures
│   ├── notebooks/                    ← Verification notebooks
│   └── development-transcripts/      ← Curated conversation logs
│       ├── SM-7_transcript_01-11_opus.md
│       ├── SM-8_development_transcript_opus.md
│       └── SM-8_development_transcript_opus_part2.md
│
├── series_electroweak/               ← EW-1 through EW-5
│   ├── papers/
│   └── figures/
├── series_quantum_mechanics/         ← QM-1 through QM-6
│   ├── papers/
│   ├── figures/
│   └── notebooks/
├── series_relativity/                ← SR-1
│   ├── papers/
│   ├── figures/
│   └── development/
├── series_strong/                    ← SS-1
│   └── papers/
├── series_foundations/               ← SD-1 through SD-5
│   └── series_superdeterminism/
│
└── archive/                          ← Superseded material
```

---

## 4. All Key Files — What Each Does

### Theory documents (read for physics context)
| File | Purpose | Update when |
|------|---------|------------|
| `CPP_the_theory.md` | The complete theory in connected prose — the "Kindle book" | Every session with new physics |
| `theory-overview.md` | Reference card: formulas, prediction scorecard, key numbers | After each paper |
| `founders_vision.md` | Thomas's physical intuition — 22+ catalogue entries | Every session with new physics |
| `axiom-registry.md` | All axioms, all predictions, growth tracking | After each paper |
| `master_glossary.md` | Every CPP term, acronym, particle, force, process | When new terms appear |
| `predictions.md` | Quantitative predictions with PDG comparison | After each paper |
| `postulates_and_theorems.md` | Formal AXIM, THEO, CORO, CONJ entries | After each paper |
| `propositions.md` | Physically motivated claims not yet proved | As needed |
| `solution_candidates.md` | Candidate solutions for open problems | As needed |
| `future_projects.md` | 12+ prioritised research targets with status | After each session |
| `nomenclature.md` | ID code legend | Rarely |

### Workflow documents (read for procedures)
| File | Purpose | Update when |
|------|---------|------------|
| `operating_system.md` | **THE COMPLETE WORKFLOW** — multi-AI review, transcripts, recovery, roles | When procedures change |
| `paper_production_workflow.md` | 9-phase pipeline from vision to OSF | When pipeline changes |
| `templates/paper-formatting.md` | LaTeX standard (16 sections) | When formatting changes |
| `templates/documentation-suite.md` | 8-file companion template per paper | When template changes |

### Navigation documents (read for orientation)
| File | Purpose | Update when |
|------|---------|------------|
| `README.md` | Public landing page, paper table, strongest results | After each paper |
| `INDEX.md` | Complete file listing | After each paper |
| `paper_catalog.md` | All papers with ID, title, version, status | After each paper |
| `series_[name]/README.md` | Per-series overview | After each series paper |

### Reference folders
| Folder | Contents |
|--------|----------|
| `bibliography/` | `cpp_references.bib` — BibTeX for all cited works |
| `open_problems/` | Individual `.md` files for each OPEN-P registered problem |
| `templates/` | This bootup file, paper formatting standard, documentation suite template |
| `archive/` | Superseded versions, old drafts |

---

## 5. The AI Team

| AI | Primary role | How Thomas communicates |
|----|-------------|----------------------|
| Claude Opus | Primary collaborator — computation, drafting, integration | Direct chat (claude.ai) |
| Grok (xAI) | Independent verifier, novel contributions | Pastebin links, raw GitHub URLs |
| Copilot (Microsoft) | Referee-grade review, framework building | Pastebin links, direct chat |
| Claude Sonnet | Hostile/adversarial review | Prompted via Claude |

**Full details on roles, strengths, limitations:** See `operating_system.md` Section 12.
**The review cycle:** Opus → Copilot → Grok → Sonnet → Opus. See `operating_system.md` Section 5.

---

## 6. Session Types

| Type | Goal | Key procedure |
|------|------|--------------|
| Physics Discovery | Explore, compute, derive | Capture Thomas's intuition FIRST. Papers can emerge unexpectedly. |
| Paper Production | Draft and finalise a paper | Follow 9-phase pipeline. Use multi-AI review cycle. |
| Housekeeping | Audit and fix repo | Check INDEX.md against actual files. Update stale docs. |
| Transcript Curation | Convert raw history to curated records | Read `/mnt/transcripts/`, produce `[Paper]_transcript_[N]_[AI].md` |

**Full protocol for each type:** See `operating_system.md` Section 3.

---

## 7. Strongest Current Results (April 2026)

| Prediction | CPP | Experimental | Error | Params |
|-----------|-----|-------------|-------|--------|
| sin²θ_W | 3/(8φ) = 0.2312 | 0.23121 | 0.24% | 0 |
| m_b (cage V^2.38) | 4,304 MeV | 4,180 MeV | 3.0% | 0 |
| m_t (cage × z=12) | 172,800 MeV | 172,760 MeV | 0.02% | 0 |
| C(n,2) → m_b/m_s | 45.0 | 44.75 | 0.6% | 0 |
| m_μ (Koide) | 105.66 MeV | 105.66 MeV | <0.01% | 1 cal |
| m_τ (Koide) | 1776.9 MeV | 1776.9 MeV | <0.01% | 1 cal |
| # Generations | 3 | 3 | exact | 0 |

Axiom count: 7. Predictions: 11+. Ratio: 0.64.

---

## 8. Currently Active Open Problems

1. **OPEN-P-SM-cage-1:** Derive α = 2.38 from 600-cell geometry
2. **OPEN-P-SM-cage-7:** Why does C(n,2) predict m_b/m_s to 0.6%?
3. **OPEN-P-SM-cage-3:** Connect cage 2/3 fraction to Koide K = 2/3
4. **OPEN-P-SM-cage-6:** Apply cage model to leptons
5. **OPEN-P-FV-1:** SSV_abs → Lorentz factor (SR-1 re-derivation)

Full list: `open_problems/` folder and `future_projects.md`.

---

## 9. What to Update After Every Paper

**WHEN:** Immediately after completing the documentation suite (Phase 7), before pushing to GitHub. See `templates/operating_system.md` Section 10 for detailed procedures for each file.

| Document | What to update |
|----------|----------------|
| `CPP_the_theory.md` | Add results to chapter, update scorecard |
| `theory-overview.md` | Add results, update formula card |
| `axiom-registry.md` | Check axioms, add predictions |
| `master_glossary.md` | Add new terms |
| `founders_vision.md` | Add new physical intuitions |
| `predictions.md` | Add new predictions |
| `postulates_and_theorems.md` | Add new theorems |
| `future_projects.md` | Update project status |
| `README.md` | Add paper to table |
| `INDEX.md` | Add new files |
| `paper_catalog.md` | Add paper entry |
| `series_[name]/README.md` | Add to series |
| `series_[name]/notebooks/` | Extract computation code into standalone .py/.ipynb (see operating_system.md Phase 7b) |

---

## 10. Conventions

**Paper IDs:** `[SERIES]-[NUMBER]` (SM-8, EW-3, QM-1, SR-1, SS-1, SD-5)
**Filenames:** `SM-8_quark_generation_600cell_shells.tex` — lowercase slug, no version number in filename
**Versions:** `vX.Y` in the .tex header changelog. ONE file per paper, overwritten — Git history preserves all versions. Never create `_v1`, `_v2` copies.
**Codes:** AXIM (axiom), THEO (theorem), CORO (corollary), CONJ (conjecture), OPEN-P (open problem), FALS (falsified). See `templates/nomenclature.md`.
**LaTeX:** Follow `templates/paper-formatting.md`

---

## 11. Papers in the Programme (April 2026)

| Series | Papers | Status |
|--------|--------|--------|
| Standard Model (SM) | SM-1 through SM-9 | SM-1–7 on OSF; SM-8 ready; SM-9 v1.0 |
| Electroweak (EW) | EW-1 through EW-5 | On OSF |
| Quantum Mechanics (QM) | QM-1 through QM-6 | On OSF |
| Relativity (SR) | SR-1 | On OSF |
| Strong Sector (SS) | SS-1 | On OSF |
| Foundations (SD) | SD-1 through SD-5 | On OSF |

Total: 24+ papers. Full details: `paper_catalog.md`.

---

## 12. OSF Registration

1. Prepare PDF + .tex + figures
2. Write metadata (title, abstract, keywords, dependencies, version)
3. Upload to OSF component under CPP project
4. OSF auto-assigns DOI
5. Update `paper_catalog.md` and `README.md`

---

*This file is self-sufficient. A new AI reading ONLY this file knows: what CPP is, where everything lives, what to read next, who the team is, what the results are, and what to do. For the full workflow manual, read `operating_system.md`. For the complete theory, read `CPP_the_theory.md`.*
