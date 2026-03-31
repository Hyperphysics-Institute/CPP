# Conscious Point Physics (CPP)

**A discrete first-principles Theory of Everything deriving the Standard Model from 600-cell lattice geometry**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet and Opus (Anthropic)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**Repository:** [github.com/Hyperphysics-Institute/CPP](https://github.com/Hyperphysics-Institute/CPP)
**License:** CC BY 4.0
**Last updated:** 31 March 2026

---

## What CPP Is

Conscious Point Physics proposes that physical reality consists of Conscious Points (CPs) — fundamental entities with polarity, position on a 600-cell lattice, and the capacity to perceive and respond to their local environment. All Standard Model particles emerge as stable geometric configurations of CPs within the lattice, and all fundamental forces arise from a single interaction: the Space Stress Vector (SSV) between CPs.

The theory is built on six axioms (see [`postulates_and_theorems.md`](postulates_and_theorems.md)) and derives its results from the geometry of the 600-cell — a regular 4-dimensional polytope with 120 vertices, 720 edges, and icosahedral H₄ symmetry. The 600-cell is the sole geometric input; all particle masses, coupling constants, and mixing angles are consequences of its structure.

---

## Submission-Ready Papers (7)

These papers are ready for OSF preregistration and viXra timestamping.

| ID | Title | Key Result | File |
|----|-------|------------|------|
| **SS-1** | The Strong Sector from the 600-Cell Lattice | SU(3) colour algebra derived exactly; β₀ = 7; 9 theorems | [`series_strong/SS-1_strong_sector_from_600cell_lattice.tex`](series_strong/SS-1_strong_sector_from_600cell_lattice.tex) |
| **SM-1** | Binding Mechanisms and Cage Stability | Tetrahedral cage as electron ground state; δ = 1/3 charge quantisation; SSV₀ = 0.2555 MeV | [`series_standard_model/papers/SM-1_binding_mechanisms_and_cage_stability.tex`](series_standard_model/papers/SM-1_binding_mechanisms_and_cage_stability.tex) |
| **SM-2** | Mass Generation from Geometric Hierarchies | Semi-empirical mass framework; one calibration constant k ≈ 0.0185 | [`series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex`](series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex) |
| **SM-3** | K3 Spectral Theorem and the Koide Formula | K = 2/3 derived exactly from K₃ eigenvalue ratio — zero free parameters | [`series_standard_model/papers/SM-3_k3_spectral_theorem_koide_formula.tex`](series_standard_model/papers/SM-3_k3_spectral_theorem_koide_formula.tex) |
| **SM-4** | Charged Lepton Masses from K3 | 11 ppm consistency; structural impossibility of θ from K3+SSV | [`series_standard_model/papers/SM-4_charged_lepton_masses_from_k3.tex`](series_standard_model/papers/SM-4_charged_lepton_masses_from_k3.tex) |
| **SM-5** | Tribimaximal Neutrino Mixing from K3 | U_PMNS⁽⁰⁾ = U_TBM exactly from K₃ eigenvectors — zero free parameters | [`series_standard_model/papers/SM-5_tribimaximal_neutrino_mixing_from_k3.tex`](series_standard_model/papers/SM-5_tribimaximal_neutrino_mixing_from_k3.tex) |
| **SR-1** | Mechanistic Derivation of Relativistic Effects | Lorentz invariance from 600-cell lattice wave propagation | [`series_relativity/main_special_relativity_emergence/SR-1_special_relativity_emergence.tex`](series_relativity/main_special_relativity_emergence/SR-1_special_relativity_emergence.tex) |

---

## Strongest Results

| Result | Precision | Source |
|--------|-----------|--------|
| Koide ratio K = 2/3 | 0.001% (11 ppm) | SM-3 (zero parameters) |
| SU(3) colour algebra | Machine precision (33/33 checks) | SS-1 Theorem 1 |
| Charge quantisation δ = 1/3 | Exact | SM-1 Theorem 1 |
| One-loop β₀ = 7 | Exact | SS-1 Theorem 3 |
| sin²θ_W = 0.2312 | 0.004% vs PDG | EW-1 (Monte Carlo, zero parameters) |
| K(c,b,t) ≈ 2/3 | 0.42% | PS-1 (signal identified, not yet a theorem) |
| TBM neutrino mixing | Zeroth-order, 10–14% corrections needed | SM-5 (zero parameters given ansatz) |

---

## Repository Structure

```
CPP/
├── README.md                    ← This file
├── INDEX.md                     ← Directory-by-directory map
├── paper_catalog.md             ← Master list of all papers with IDs and status
├── postulates_and_theorems.md   ← 6 axioms, theorems, corollaries, falsified claims
├── predictions.md               ← Every quantitative prediction with status
├── propositions.md              ← Physically motivated claims not yet proved
├── nomenclature.md              ← ID code legend (AXIM, THEO, PROP, etc.)
├── solution_candidates.md       ← Candidate solutions for open problems
│
├── series_strong/               ← SS-1 + 5 companions + notebooks
├── series_standard_model/       ← SM-1 through SM-5 + documentation
├── series_relativity/           ← SR-1 + 22 companion papers
├── series_electroweak/          ← EW-1 through EW-5 (needs consolidation)
├── series_quantum_mechanics/    ← QM-1 through QM-6
├── series_foundations/          ← SD-1 through SD-5 (superdeterminism)
├── series_nuclear/              ← Planned
├── series_experimental_phenomena/ ← g-2, swarm analysis
├── series_synthesis/            ← QM synthesis paper
├── open_problems/               ← 40+ registered problems with status tracking
└── archive/                     ← Superseded files
```

---

## Documentation System

Each paper in the series has six companion documentation files:

| File type | Purpose |
|-----------|---------|
| `mechanism-XX-N.md` | Step-by-step cause-and-effect narrative of the physics |
| `glossary-XX-N.md` | Precise definitions of all terms specific to that paper |
| `phenomena-XX-N.md` | Mapping of theorems to observable reality (Explained / Predicted / Consilience) |
| `reviews-XX-N.md` | Formal review objections and FAQ for conventional physicists |
| `philosophy-XX-N.md` | Epistemological and philosophical foundations |
| `development-XX-N.md` | Intellectual history — the laboratory notebook record |

Documentation is complete for: SS-1, SM-1 through SM-5, EW-1 through EW-5, QM-1 through QM-6, SD-1 through SD-5.

---

## Scientific Honesty Standards

CPP maintains explicit distinction between:
- **Derived** results (proved from axioms, zero free parameters)
- **Calibrated** results (one or more parameters fitted to data)
- **Semi-empirical** results (mechanism identified, quantitative fit requires calibration)
- **Open** problems (mechanism not yet identified)
- **Falsified** claims (tested and found wrong — never deleted, always documented)

The falsified claims register includes 7 entries (FALS-C-1 through FALS-C-7). The open problems register contains 40+ active problems across all series.

---

## How to Navigate

- **New to CPP?** Start with [`mechanism-SM-1.md`](series_standard_model/papers/mechanism-SM-1.md) — it walks through the physics from first principles.
- **Want to evaluate the theory?** Read [`predictions.md`](predictions.md) — every quantitative claim with status.
- **Looking for a specific paper?** See [`paper_catalog.md`](paper_catalog.md).
- **Want to contribute?** See [`open_problems/`](open_problems/) — registered problems with suggested approaches.

---

*Repository maintained by Thomas Lee Abshier ND, Hyperphysics Institute. AI co-authors: Grok (xAI), Claude Sonnet and Opus (Anthropic). All papers under CC BY 4.0.*
