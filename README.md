# Conscious Point Physics (CPP)

**A geometric, discrete framework deriving the Standard Model from the 600-cell polytope**

**Authors:** Thomas Lee Abshier, ND — Claude Sonnet & Opus (Anthropic) — Grok (xAI)  
**Institution:** Hyperphysics Institute — [hyperphysics.com](https://hyperphysics.com)  
**Last updated:** 27 March 2026

---

## What This Is

This repository contains the complete theoretical programme of Conscious Point Physics (CPP): a speculative framework in which the Standard Model gauge structure, charge quantisation, lepton mass ratios, and neutrino mixing emerge from the geometry of the 600-cell polytope (120 vertices, golden-ratio edge lengths, H₄ symmetry group).

The framework rests on seven core postulates (see [`postulates_and_theorems.md`](postulates_and_theorems.md)) and derives its results from 600-cell lattice geometry plus a single calibration constant. Everything claimed as "derived" is backed by runnable code. Everything open is registered in [`open_problems/`](open_problems/).

**If you want to know what CPP claims and what is proved, read the two registry files first:**
- [`paper_catalog.md`](paper_catalog.md) — every paper, its ID, status, and location
- [`postulates_and_theorems.md`](postulates_and_theorems.md) — every postulate, theorem, corollary, conjecture, and falsified claim

---

## The Theory in One Paragraph

Conscious Points (CPs) occupy vertices of a 600-cell lattice. They interact via Space Stress Vector (SSV) gradients and oscillate as Dipole Pairs (DPs) at Zitterbewegung frequencies. The tetrahedral cells of the 600-cell host quark colour (SU(3)_c); the icosahedral vertex coordination hosts the electroweak sector (SU(2)_L × U(1)_Y). The equilateral triangle K₃ formed by the three base vertices of each tetrahedral cage encodes both charge quantisation (δ = 1/3, combinatorial) and the Koide lepton mass relation (K = 2/3, spectral). A single geometric invariant α_geom ≈ 0.5594, computed from the 600-cell Voronoi stiffness integral, threads through the relativistic, electromagnetic, and strong sectors.

---

## The Four K₃ Results

The same equilateral triangle — the base of the 600-cell tetrahedral cage — gives four distinct Standard Model quantities:

| Result | Value | K₃ structure | Paper |
|--------|-------|--------------|-------|
| Charge quantisation | δ = 1/3 (exact) | Combinatorial: 3 equal vertices, completeness | SM-1 |
| Koide lepton mass ratio | K = 2/3 (exact) | Spectral: eigenvalue ratio λ₊/\|λ₋\| = 2:1 | SM-3 |
| Lepton mass constraint | m_τ from m_e + m_μ | Vertex occupation ∝ \|ψᵢ\|² | SM-4 |
| Tribimaximal PMNS mixing | U_TBM (exact, zeroth order) | Eigenvector–vertex change of basis | SM-5 |

---

## Key Derived Constants

| Constant | Value | Source |
|----------|-------|--------|
| φ (golden ratio) | (1+√5)/2 ≈ 1.6180 | 600-cell vertex coordinates |
| α_geom | 3(11+5√5)√(5+√5)/320 ≈ 0.5594 | Voronoi stiffness integral (SS-T4) |
| k_SM | α_geom/(12φ²) ≈ 0.01781 | SS-T5 |
| sea_strength | 10 × k_SM ≈ 0.1780 | SS-T6 |
| δ (charge fraction) | 1/3 (exact) | SM-T1 |
| K (Koide ratio) | 2/3 (exact) | SM-T2 |

---

## What Is Proved, What Is Open, What Is Falsified

### Proved (14 theorems)

**Strong sector (SS-1):** SU(3) algebra from tetrahedral hopping (exact) · Gluon masslessness · β₀ = 7 · α_geom exact closed form · k_SM and sea_strength derived · GMO relations · Hadron decuplet · Quark mass ordering

**Standard Model (SM-1 through SM-5):** δ = 1/3 charge quantisation · K = 2/3 Koide ratio · K3 postulates derived from CPP axioms · TBM neutrino mixing (zeroth order) · θ_Koide undetermined in K3+SSV (structural theorem SM-T6)

### Open (registered in [`open_problems/`](open_problems/))

| Count | Series | Key problems |
|-------|--------|-------------|
| 10 | OP-SS | Quark mass formula, string tension, chiral condensate, 2-loop β, glueball, Λ_QCD |
| 10 | OP-SM | Koide phase θ, three generations, Capotauro, TBM corrections, cosmological constant |
| 8 | OP-SR | PSR formula, full Einstein equations, Big Bang, equivalence principle |
| 6 | OP-EW | η derivation, unified mass formula, chirality |
| 7 | OP-QM | Born rule, Schrödinger derivation, spin, entanglement |
| 2 | OP-GLOBAL | Three generations (global), SM unification |

### Falsified (recorded to prevent rework)

| Conjecture | Why it fails | Reference |
|------------|-------------|-----------|
| C₆₀ (60 vertices) as top quark cage | No 60-vertex distance shell exists in the 600-cell | PS-1, March 2026 |
| φ^(3(l-1)) quark mass scaling | Actual shell volumes deviate by 3–8× | PS-1, March 2026 |
| Aharonov-Bohm loop for θ_Koide | C3 symmetry prevents degeneracy breaking | Session F |
| 4D embedding perturbation for θ | C3 preserved exactly under all tested perturbations | Session G |
| Self-consistent ZBW feedback for θ | Converges to trivial fixed point θ = 180° | Session L |
| Löwdin downfolding (K4→K3) for θ | Apex is dark to antibonding modes | Session E |

> **Note on the last four entries:** Sessions E, F, G, and L are not independent failures — they are the four mechanisms tested under the **structural theorem SM-T6** (proved), which establishes that no mechanism within the K3+SSV framework can select the Koide phase θ, because C3 symmetry leaves the antibonding subspace degenerate for any such perturbation. The theorem is the umbrella; the four falsified mechanisms are what was tested to establish it. The correct next step is the electroweak sector (EW series), not further K3+SSV mechanisms.

---

## Repository Structure

```
CPP/
├── README.md                          ← you are here
├── INDEX.md                           ← directory-level navigation
├── paper_catalog.md                   ← master list of all papers with IDs and status
├── postulates_and_theorems.md         ← registry of all postulates, theorems, falsified claims
├── LICENSE / LICENSE-CC-BY-4.0.md
│
├── series_strong/                     ← Strong sector (SS series)
│   ├── cpp_ss_unified_v2.tex          ← SS-1: submission-ready unified paper
│   ├── cpp_ss1–5_*.tex                ← Individual companion papers v1
│   ├── mc_su3_algebra.py/.ipynb       ← Monte Carlo verification (33/33 checks pass)
│   ├── notebooks/                     ← 14 derivation/verification notebooks
│   └── figures/
│
├── series_standard_model/             ← Standard Model emergence (SM series)
│   ├── papers/                        ← SM-1 through SM-5 + tech notes + dev logs
│   ├── notebooks/                     ← PS-1 quark mass ladder analysis
│   ├── p1-*/                          ← Paper 1 topic directories
│   ├── p2-*/                          ← Paper 2 topic directories (27 subdirectories)
│   ├── cpp-zbw-mixing-fractions/      ← ZBW mixing notebooks and calculator
│   ├── suppression/                   ← Five suppression mechanisms with notebooks
│   ├── INDEX.md / README.md           ← Series-level navigation
│   └── potential_solutions.md
│
├── series_relativity/                 ← Special Relativity (SR series)
│   ├── main_special_relativity_emergence/  ← SR-1 paper + figures + notebooks
│   ├── companion_papers/              ← 22 companion papers (c01–c22)
│   ├── 600cell_k_alpha_geom_consistency_fix.py  ← α_geom verification code
│   ├── k_prefactor_resolution.md      ← α_geom correction documentation
│   └── lattice-derived_coupling_constant_k.md
│
├── series_electroweak/                ← Electroweak sector (EW series)
│   ├── cpp_ew1–5_*.tex                ← EW papers (need consolidation)
│   ├── mc_weinberg_unification.*      ← Monte Carlo verification
│   └── figures/
│
├── series_quantum_mechanics/          ← QM foundations (QM series)
│   ├── cpp2040a–f_*/                  ← Six QM topic papers
│   └── development/
│
├── series_foundations/                ← Foundational papers
│   ├── cpp_sd1–5_*.tex                ← Superdeterminism papers (SD-1 through SD-5)
│   ├── TN-SR-1_vacuum_energy_*.tex    ← Technical note on vacuum energy
│   ├── dp-sea-polarization/           ← DP Sea physics
│   └── dp_sea_composition/
│
├── series_nuclear/                    ← Nuclear physics (planned)
│
├── series_experimental_phenomena/     ← Experimental connections
│   ├── 600-cell_electron_g-2/         ← Electron g-2 analysis
│   └── swarm-analysis-chiral_evidence/← Multi-scale swarm analysis (58 entries)
│
├── series_synthesis/                  ← Cross-series synthesis
│   └── cpp_qm_synthesis_submission.tex ← QM synthesis paper
│
├── open_problems/                     ← All registered open problems
│   ├── OP-SS/  (10 problems)
│   ├── OP-SM/  (10 problems)
│   ├── OP-SR/  (8 problems)
│   ├── OP-EW/  (6 problems)
│   ├── OP-QM/  (7 problems)
│   ├── OP-GLOBAL/ (2 problems)
│   └── OP-SS-1_quark_mass_ladder_ps1_analysis.md
│
└── archive/                           ← Superseded material
    └── legacy_structure/
```

---

## Submission Status

| Paper ID | Title | Status |
|----------|-------|--------|
| **SS-1** | The Strong Sector from the 600-Cell Lattice | **Submission-ready** |
| **SM-1** | Binding Mechanisms and Cage Stability (v6) | **Submission-ready** |
| **SM-2** | Mass Generation from Geometric Hierarchies (v30) | **Submission-ready** |
| **SM-3** | K3 Spectral Theorem and the Koide Formula (v5) | **Submission-ready** |
| **SM-4** | Charged Lepton Masses from K3 | **Submission-ready** |
| **SM-5** | Tribimaximal Neutrino Mixing from K3 | **Submission-ready** |
| **SR-1** | Special Relativity from 600-Cell Geometry (v17) | **Submission-ready** |
| SM-TN-1 | Reconstruction of Original CPP Mass Calculations | Ready |
| SM-TN-2 | Bridge from Original to 600-Cell | Needs minor corrections |
| EW-1–5 | Electroweak series (v2 in repo) | Needs consolidation |
| QM-1 | QM Synthesis | Needs review |
| SD-1–5 | Superdeterminism series | Needs review |
| CC-1 | CPP Analysis of Ξcc⁺ (LHCb Moriond 2026) | Planned — requires SS-1 on OSF first |

---

## Verification Standards

Every numerical claim in a submission-ready paper is backed by runnable code. The standard: if a result cannot be reproduced by executing a notebook or script, it does not appear in a paper.

Key verification code:
- `series_strong/mc_su3_algebra.py` — 33/33 algebraic checks for SU(3) derivation
- `series_relativity/600cell_k_alpha_geom_consistency_fix.py` — α_geom numerical verification
- `series_standard_model/notebooks/ps1_quark_mass_ladder_verifiable.py` — PS-1 mass analysis

---

## How to Navigate

1. **Start with** [`paper_catalog.md`](paper_catalog.md) — find the paper you want by its ID
2. **Check status in** [`postulates_and_theorems.md`](postulates_and_theorems.md) — see what's proved vs open
3. **Read the paper** in the appropriate `series_*/` directory
4. **Check open problems** in [`open_problems/`](open_problems/) for what remains
5. **See [`INDEX.md`](INDEX.md)** for a directory-by-directory map

---

## Authorship

- **Thomas Lee Abshier, ND** — Physical framework, theoretical direction, core insights
- **Claude Sonnet & Opus (Anthropic)** — Derivations, code, paper writing, numerical verification, pre-submission review
- **Grok (xAI)** — Conceptual contributions (PSR saturation, layer-depth counting, proton mass quantification)

Contributions are credited per-session in development logs within each series directory.

---

*License: Content CC-BY-4.0; Code MIT (see individual files).*  
*Feedback, rigorous critiques, and falsification attempts are welcome.*  
*Contact: drthomas007@protonmail.com*
