# CPP Session Bootup Guide

**Location:** `/CPP/templates/bootup.md`
**Purpose:** Load this file at the start of every new AI session working on CPP. It provides the essential context, locations, conventions, and current state needed to continue productive work without repeating setup.
**Last updated:** 8 April 2026

---

## How to Use This File

**Thomas:** At the start of a new chat, say:
> "Pull the CPP repo and read `templates/bootup.md`"

**AI assistant:** After reading this file, you know:
1. What CPP is and where everything lives
2. What the current state of the theory is
3. What templates and workflows to follow
4. What the active open problems are

Then read `theory-overview.md` for the current physics state.

For the COMPLETE workflow manual (multi-AI review, transcript management,
negative result documentation, recovery procedures), read `operating_system.md`.
This bootup file is the quick-start; the operating system is the full reference.

---

## 1. Repository Location and Access

```
GitHub: https://github.com/Hyperphysics-Institute/CPP
Clone: git clone https://github.com/Hyperphysics-Institute/CPP.git
OSF:   https://osf.io/9dfya/
DOI:   10.17605/OSF.IO/JXE8D
```

Always `git pull` before starting work. Thomas pushes frequently.

---

## 2. What CPP Is (30-second summary)

Conscious Point Physics derives the Standard Model from the geometry of the 600-cell polytope (V=120, E=720, F=1200, C=600, z=12). Conscious Points on the lattice exchange DI-bits via SSV gradients. All particles are geometric cage structures. All forces emerge from the lattice mode spectrum. The golden ratio φ = (1+√5)/2 appears throughout because it's built into the 600-cell geometry.

**Key constants:** SSV₀ = 0.2555 MeV, φ = 1.6180, sin²θ_W = 3/(8φ), α_s = 5/(8φ), K = 2/3

---

## 3. Key Files to Read for Context

**Read these BEFORE doing physics:**

| File | What it tells you |
|------|-------------------|
| `theory-overview.md` | Current state of all results, what's proved, what's open |
| `axiom-registry.md` | The 10 axioms, 17 predictions, and growth trajectory |
| `founders_vision.md` | Thomas's physical intuition — the mental model behind the math |
| `master_glossary.md` | All CPP terms, acronyms, particles, forces, and processes |

**Read these BEFORE doing paper production:**

| File | What it tells you |
|------|-------------------|
| `templates/paper-formatting.md` | LaTeX formatting standard (16 sections) |
| `templates/documentation-suite.md` | Template for the 8 documentation files per paper |
| `paper_production_workflow.md` | The 9-phase pipeline from vision to OSF |

**Reference files (consult as needed):**

| File | Content |
|------|---------|
| `master_glossary.md` | All CPP terms, acronyms, forces, particles, processes |
| `postulates_and_theorems.md` | Formal axioms (AXIM), theorems (THEO), corollaries |
| `predictions.md` | Every quantitative prediction with status |
| `open_problems/` | 50+ registered problems with OPEN-P numbers |
| `nomenclature.md` | ID code legend (AXIM, THEO, PROP, FALS, etc.) |
| `propositions.md` | Physically motivated claims not yet proved |
| `solution_candidates.md` | Candidate solutions for open problems |
| `paper_catalog.md` | Master list of all papers with IDs and status |
| `INDEX.md` | Directory-by-directory map of the repo |

---

## 4. Repository Structure

```
CPP/
├── README.md                     ← Public-facing overview (update after each paper)
├── INDEX.md                      ← Directory map (update after each paper)
├── paper_catalog.md              ← Paper list (update after each paper)
├── theory-overview.md            ← Current physics state (update after each paper)
├── axiom-registry.md             ← Axiom tracking (update after each paper)
├── founders_vision.md            ← Thomas's physical intuition (update each session)
├── paper_production_workflow.md  ← 9-phase workflow
├── postulates_and_theorems.md
├── predictions.md
├── nomenclature.md
├── propositions.md
├── solution_candidates.md
│
├── templates/
│   ├── bootup.md                 ← THIS FILE
│   ├── paper-formatting.md       ← LaTeX standard
│   └── documentation-suite.md    ← 8-file template
│
├── series_standard_model/        ← SM-1 through SM-7
│   ├── papers/                   ← .tex, .pdf, .bib, all .md docs
│   ├── figures/figures-SM-N/     ← SVG + PDF figures
│   ├── notebooks/                ← Verification notebooks
│   └── development-transcripts/  ← Curated conversation logs
│
├── series_electroweak/           ← EW-1 through EW-5
├── series_quantum_mechanics/     ← QM-1 through QM-6
│   ├── papers/
│   ├── figures/figures-QM-N/
│   └── notebooks/
├── series_relativity/            ← SR-1
│   ├── papers/
│   ├── figures/figures-SR-1/
│   └── development/
├── series_strong/                ← SS-1
│   └── papers/
├── series_foundations/            ← SD-1 through SD-5
│   └── series_superdeterminism/
│
├── open_problems/
├── bibliography/
│   └── cpp_references.bib
└── archive/                      ← Superseded material
```

---

## 5. The AI Team

| AI | Role | Strengths |
|----|------|-----------|
| **Claude Opus** | Primary collaborator | Paper drafting, derivation, numerical verification, documentation |
| **Grok (xAI)** | SSV/PSR mechanism, independent verification | Physical mechanism, efficiency framework, honest review |
| **Copilot (Microsoft)** | Perturbation theory, projector algebra | Formal theorem tightening, bond-counting framework, referee-grade proofs |
| **Claude Sonnet** | Hostile reviewer | Adversarial critique (role: find every weakness) |

**Workflow:** Opus drafts → Grok + Copilot review → incorporate feedback → Sonnet hostile review → respond and finalise.

---

## 6. Session Types and What to Do

### Physics Discovery Session
1. Read `theory-overview.md` and `axiom-registry.md`
2. Thomas describes the target phenomenon
3. Capture Thomas's physical intuition in `founders_vision.md`
4. Explore, compute, derive
5. If result found → proceed to paper drafting

### Paper Production Session
1. Follow `paper_production_workflow.md` (9 phases)
2. Read `templates/paper-formatting.md` before writing .tex
3. After paper is complete, update:
   - `theory-overview.md`
   - `axiom-registry.md`
   - `README.md` (Registered Papers table)
   - `INDEX.md`
   - `paper_catalog.md`
   - `predictions.md` (if new predictions)
   - `postulates_and_theorems.md` (if new theorems)
   - `series_[name]/README.md`

### Repository Housekeeping Session
1. Pull repo, audit structure
2. Fix formatting, paths, missing files
3. Update documentation

### Transcript Curation Session
1. Read raw transcripts from `/mnt/transcripts/`
2. Produce curated `.md` files per `paper_production_workflow.md` Phase 8

---

## 7. OSF Registration Procedure

1. Upload PDF to OSF project: https://osf.io/9dfya/
2. Update OSF wiki:
   - Add row to Submission-Ready Papers table
   - Update paper count in header
   - Update "Last updated" date
3. DOI for all papers: `10.17605/OSF.IO/JXE8D`

---

## 8. Conventions

- **Timestamps:** Mountain Time (MDT/MST) for development docs, date-only for papers, UTC for git
- **File naming:** `[PAPER-ID]_[snake_case_title].tex` (e.g., `SM-7_heavy_quark_mass_spectrum.tex`)
- **Documentation:** 8 files per paper: development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, keywords
- **Bibliography:** Local `[PAPER-ID]_references.bib` next to .tex; site-wide `cpp_references.bib` aggregated
- **Figure paths:** `\graphicspath{{../figures/figures-[PAPER-ID]/}}`
- **Golden ratio:** Use `\varphi` (not `\phi`), macro `\phig`
- **600-cell:** Always hyphenated
- **Open problems:** Numbered as OPEN-P-[PAPER]-[N]

---

## 9. What to Update After Each Paper

| Document | What to update |
|----------|----------------|
| `theory-overview.md` | Add new results, update scorecard |
| `axiom-registry.md` | Check axiom usage, add predictions, update growth table |
| `master_glossary.md` | Add new terms, acronyms, particles, processes |
| `README.md` | Add paper to Registered Papers table, update count |
| `INDEX.md` | Add new files/folders |
| `paper_catalog.md` | Add paper entry |
| `predictions.md` | Add new quantitative predictions |
| `postulates_and_theorems.md` | Add new theorems |
| `founders_vision.md` | Add any new physical intuitions from Thomas |
| `series_[name]/README.md` | Add paper to series table |

---

*This is a living document. Update it whenever new conventions are established or the workflow changes.*
