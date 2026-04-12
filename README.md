# Conscious Point Physics (CPP)

**A discrete first-principles Theory of Everything deriving the Standard Model from 600-cell lattice geometry**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet and Opus (Anthropic), Copilot (Microsoft)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**Repository:** [github.com/Hyperphysics-Institute/CPP](https://github.com/Hyperphysics-Institute/CPP)
**OSF Registration:** [doi.org/10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D)
**License:** CC BY 4.0
**Last updated:** 11 April 2026

---

## What CPP Is

Conscious Point Physics proposes that physical reality consists of Conscious Points (CPs) — fundamental entities with polarity, position on a 600-cell lattice, and the capacity to perceive and respond to their local environment. All Standard Model particles emerge as stable geometric configurations of CPs within the lattice, and all fundamental forces arise from a single interaction: the Space Stress Vector (SSV) between CPs.

The theory is built on nine axioms (see [`postulates_and_theorems.md`](postulates_and_theorems.md)) and derives its results from the geometry of the 600-cell — a regular 4-dimensional polytope with 120 vertices, 720 edges, and icosahedral H₄ symmetry. The 600-cell is the sole geometric input; all particle masses, coupling constants, and mixing angles are consequences of its structure.

---

## Headline Result: The Charged Lepton Mass Spectrum (SM-6, April 2026)

The masses of the electron, muon, and tau are derived from the 600-cell geometry with **one calibration constant** (the electron mass) and **zero free shape parameters**:

- **Weinberg angle:** sin²θ_W = 3/(8φ) ≈ 0.2318 (PDG: 0.2312, agreement 0.24%)
- **Koide phase:** cos(θ) = −(2/3)(1 + 3/(104φ)), θ = 132.731° (PDG: 132.732°, agreement 0.003%)
- **Muon mass:** 105.47 MeV (PDG: 105.66, 0.18%)
- **Tau mass:** 1774.1 MeV (PDG: 1776.9, 0.15%)

The Standard Model requires 3 free parameters for the charged lepton masses. The Koide formula (1981) reduced this to 2. CPP reduces it to 1.

---

## Registered Papers (13)

All papers are registered on OSF with DOI [10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D). PDFs are available on the [OSF project page](https://osf.io/9dfya/). Source files and documentation are in this repository.

| ID | Title | Key Result |
|----|-------|------------|
| **SS-1** | The Strong Sector from the 600-Cell Lattice | SU(3) colour algebra derived exactly; β₀ = 7; 9 theorems |
| **SS-2** | Lattice-Scale Grounding and Nucleon Structure | l_unit = 0.589 fm; r_proton = 0.883 fm (+5%, 0 params) |
| **SM-1** | Binding Mechanisms and Cage Stability | Tetrahedral cage as electron ground state; δ = 1/3; SSV₀ = 0.2555 MeV |
| **SM-2** | Mass Generation from Geometric Hierarchies | Semi-empirical mass framework; one calibration constant k ≈ 0.0185 |
| **SM-3** | K3 Spectral Theorem and the Koide Formula | K = 2/3 derived exactly from K₃ eigenvalue ratio — zero free parameters |
| **SM-4** | Charged Lepton Masses from K3 | 11 ppm consistency; structural impossibility of θ from K3+SSV |
| **SM-5** | Tribimaximal Neutrino Mixing from K3 | U_PMNS = U_TBM exactly from K₃ eigenvectors — zero free parameters |
| **SR-1** | Mechanistic Derivation of Relativistic Effects | Lorentz invariance from 600-cell lattice wave propagation |
| **SM-6** | The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry | sin²θ_W = 3/(8φ); Koide phase derived; 1 calibration, 0 shape parameters |
| **SM-7** | Heavy Quark Mass Spectrum and Strong Coupling | α_s = 5/(8φ); quark Koide phase; m_b 1.4%, m_t 1.7% |
| **SM-8** | Quark Generation Structure from 600-Cell Distance Shells | Zero-param quark masses RMS 2.1%; 3-generation theorem |
| **SM-9** | The Quark Mass Scaling Exponent | V^(7/3) derivation; Symmetry Degeneracy Theorem |
| **SM-10** | First-Principles Quark Mass from FEM Chain Network Simulation | Cascade mechanism; two-regime physics; organised DP density |

---

## Strongest Results

| Result | Precision | Source | Parameters |
|--------|-----------|--------|------------|
| Koide ratio K = 2/3 | 11 ppm | SM-3 | 0 |
| Koide phase θ = 132.731° | 0.003% | SM-6 | 0 |
| Weinberg angle sin²θ_W = 3/(8φ) | 0.24% | SM-6 | 0 |
| Muon mass 105.47 MeV | 0.18% | SM-6 | 0 (shape) |
| Tau mass 1774.1 MeV | 0.15% | SM-6 | 0 (shape) |
| SU(3) colour algebra | Machine precision (33/33) | SS-1 | 0 |
| Charge quantisation δ = 1/3 | Exact | SM-1 | 0 |
| One-loop β₀ = 7 | Exact | SS-1 | 0 |
| TBM neutrino mixing | Zeroth-order | SM-5 | 0 (given ansatz) |
| Zero-param quark masses (RMS) | 2.1% | SM-8/9 | 0 |
| Three-generation theorem | Exact (structural) | SM-8 | 0 |
| Symmetry Degeneracy Theorem | Exact (mathematical) | SM-9 | 0 |
| Proton charge radius 0.883 fm | +5.0% | SS-2 | 0 |
| Proton magnetic moment 2.789 μ_N | −0.1% | SS-2 | 0 |
| α_s(m_H) = 0.1132 | +0.2% | SS-2 | 0 |

---

## Repository Structure

```
CPP/
├── README.md                    ← This file
├── INDEX.md                     ← Directory-by-directory map
├── paper_catalog.md             ← Master list of all papers with IDs and status
├── postulates_and_theorems.md   ← 6 axioms, theorems, corollaries, conjectures
├── predictions.md               ← Every quantitative prediction with status
├── propositions.md              ← Physically motivated claims not yet proved
├── nomenclature.md              ← ID code legend (AXIM, THEO, PROP, etc.)
├── solution_candidates.md       ← Candidate solutions for open problems
│
├── templates/                   ← Formatting standards and documentation templates
│   ├── paper-formatting.md      ← Master formatting standard for all papers
│   └── documentation-suite.md   ← Template for the 8 documentation files per paper
│
├── bibliography/                ← Site-wide bibliography
│   └── cpp_references.bib       ← Aggregated from all local .bib files
│
├── series_strong/               ← SS-1, SS-2 + companions + notebooks
├── series_standard_model/       ← SM-1 through SM-10 + documentation
├── series_relativity/           ← SR-1 + 22 companion papers
├── series_electroweak/          ← EW-1 through EW-5
├── series_quantum_mechanics/    ← QM-1 through QM-6
├── series_foundations/          ← SD-1 through SD-5 (superdeterminism)
├── open_problems/               ← 50+ registered problems with status tracking
└── archive/                     ← Superseded and exploratory material
```

---

## Documentation System

Each paper has seven companion documentation files:

| File type | Purpose |
|-----------|---------|
| `development-XX-N.md` | Intellectual history — decisions, dead ends, timeline |
| `glossary-XX-N.md` | Precise definitions of all terms |
| `mechanism-XX-N.md` | Step-by-step physical mechanisms |
| `phenomena-XX-N.md` | Mapping of theorems to observable reality |
| `philosophy-XX-N.md` | Epistemological foundations and honest assessment |
| `reviews-XX-N.md` | External reviews, responses to critiques, and FAQ |
| `keywords-XX-N.md` | Keywords, PACS/MSC codes, SEO data |

Documentation is complete for all registered papers plus the EW, QM, and SD series. Templates for generating new documentation are in [`templates/`](templates/).

---

## Scientific Honesty Standards

CPP maintains explicit distinction between:
- **Derived** results (proved from axioms, zero free parameters)
- **Calibrated** results (one or more parameters fitted to data)
- **Semi-empirical** results (mechanism identified, quantitative fit requires calibration)
- **Open** problems (mechanism not yet identified)
- **Falsified** claims (tested and found wrong — never deleted, always documented)

The falsified claims register includes 7 entries. The open problems register contains 50+ active problems across all series.

---

## How to Navigate

- **New to CPP?** Start with [`mechanism-SM-1.md`](series_standard_model/papers/mechanism-SM-1.md) — it walks through the physics from first principles.
- **Want the headline result?** Read SM-6 ([PDF on OSF](https://osf.io/9dfya/)) — the lepton mass spectrum from one equation.
- **Want to evaluate the theory?** Read [`predictions.md`](predictions.md) — every quantitative claim with status.
- **Looking for a specific paper?** See [`paper_catalog.md`](paper_catalog.md).
- **Want to contribute?** See [`open_problems/`](open_problems/).
- **Writing a new paper?** See [`templates/paper-formatting.md`](templates/paper-formatting.md).

---

*Repository maintained by Thomas Lee Abshier ND, Hyperphysics Institute. AI co-authors: Grok (xAI), Claude Sonnet and Opus (Anthropic), Copilot (Microsoft). All papers under CC BY 4.0.*
