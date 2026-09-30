# Conscious Point Physics (CPP)

**A discrete first-principles Theory of Everything deriving the Standard Model from 600-cell lattice geometry**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet and Opus (Anthropic), Copilot (Microsoft)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**Repository:** [github.com/Hyperphysics-Institute/CPP](https://github.com/Hyperphysics-Institute/CPP)
**Earlier OSF project registration:** [doi.org/10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D) · **Paper deposits:** the CERN repository (Zenodo), not yet made — see [`pre_deposit_roadmap.md`](pre_deposit_roadmap.md)
**License:** CC BY 4.0
**Last updated:** 29 September 2026 (Patch 4337 — headline sections refreshed to the live registries: status, basis of each headline, deposit state. The earlier May–June status notes are in the git history and in [`research_frontier.md`](research_frontier.md).)

---

## Programme Status (29 September 2026)

**Where things stand, with the basis of each claim.** The authoritative sources are [`predictions.md`](predictions.md) (every quantitative claim with status), [`theory-overview.md`](theory-overview.md) (the scorecard, audited row by row), [`paper_catalog.md`](paper_catalog.md) (papers and versions) and [`pre_deposit_roadmap.md`](pre_deposit_roadmap.md) (what must be settled before the corpus is deposited).

- **Derived at zero parameters (as claimed by the papers):** sin²θ_W = 3/(8φ), α_s = 5/(8φ), their exact sum 1/φ; the lepton and quark Koide phases; m_Z/m_W = 1.141; SU(3) as the unique algebra of the three-vertex cage.
- **One calibration (the electron mass):** the muon and tau masses; the heavy-quark masses (RMS 2.1%); the neutrino sector.
- **Conditional:** Koide K = 2/3 (on Layer B, OPEN-SS-16); the nuclear bindings (on stated hypothesis stacks); n_s ≈ 0.9654 (framework-conditional, at an adopted pivot).
- **Calibrated:** the absolute W, Z and Higgs masses; the fine-structure constant (α = PSR/(2L) with one calibrated swing); the cosmological constant.
- **Held pending critique:** SS-2 (proton radius and moment), SS-5, SS-6, SS-9.
- **Derived conditionally:** the general static field equation of gravity with a Birkhoff-type uniqueness (GR-1j), on a constitutive form graded at W2 strength; the full nonlinear Einstein equations remain open.
- **Not yet derived:** ħ (identified); spin ħ/2 (input; the spin papers now say so); the electromagnetic constants (tuned toy model).
- **Conjecture or primitive:** dark matter (a conjecture, far short of the needed clumping); the handedness of the weak interaction (a primitive).

**Counts:** 9 axioms; 108 counted correspondences in the tally (60 of them conditional); 82 theorems + 9 corollaries; 128 papers in the tree, 122 deposit candidates; a trial deposit has been made, the main deposit not yet.

---

## What CPP Is

Conscious Point Physics proposes that physical reality consists of Conscious Points (CPs) — fundamental entities with polarity, position on a 600-cell lattice, and the capacity to perceive and respond to their local environment. All Standard Model particles emerge as stable geometric configurations of CPs within the lattice, and all fundamental forces arise from a single interaction: the Space Stress Vector (SSV) between CPs.

The theory is built on nine axioms (see [`axiom-registry.md`](axiom-registry.md)) and derives its results from the geometry of the 600-cell — a regular 4-dimensional polytope with 120 vertices, 720 edges, and icosahedral H₄ symmetry. The 600-cell is the sole geometric input. The coupling constants and mixing angles listed above are derived from it; the masses need one calibration (the electron mass), and other constants enter as calibrations or identifications — the status list above says which. For proved results, see [`theorem-registry.md`](theorem-registry.md). For open problems and conjectures, see [`research_frontier.md`](research_frontier.md).

---

## Headline Result: The Charged Lepton Mass Spectrum (SM-6, April 2026)

The masses of the electron, muon, and tau are derived from the 600-cell geometry with **one calibration constant** (the electron mass) and **zero free shape parameters**, conditional on the Koide ratio K = 2/3, which rests on the Layer B assumption (OPEN-SS-16):

- **Weinberg angle:** sin²θ_W = 3/(8φ) ≈ 0.23176 (PDG MS-bar: 0.23122, agreement 0.24%)
- **Koide phase:** cos(θ) = −(2/3)(1 + 3/(104φ)), θ = 132.731° (PDG: 132.732°, agreement 0.003%)
- **Muon mass:** 105.47 MeV (PDG: 105.66, 0.18%)
- **Tau mass:** 1774.1 MeV (PDG: 1776.9, 0.15%)

The Standard Model requires 3 free parameters for the charged lepton masses. The Koide formula (1981) reduced this to 2. CPP reduces it to 1.

---

## Flagship Papers

[`flagship_papers/`](flagship_papers/) houses the programme's cross-cutting apex artifacts: papers that solve named unsolved problems in mainstream physics, make forced-choice prospective predictions, or provide cross-domain unification. They build on the series papers below — they do not replace them — and are written for an audience reading across sectors.

The Standard-Model fermion-mass programme is structured as **four family-paper flagships plus a unification synthesis**, the SF-line:

- **SF-1** — Charged Lepton Mass Spectrum from K3 + 600-Cell Geometry. [`flagship_papers/charged_leptons/`](flagship_papers/charged_leptons/)
- **SF-2** — Electroweak Sector Unification from 600-Cell Geometry. [`flagship_papers/electroweak/`](flagship_papers/electroweak/)
- **SF-3** — Quark Sector Unification from 600-Cell Distance Shells. [`flagship_papers/quarks/`](flagship_papers/quarks/)
- **SF-4 [v3.4]** — Neutrino Sector Unification from 600-Cell Geometry; eight parameters from one calibration. [`flagship_papers/neutrinos/`](flagship_papers/neutrinos/)
- **SF-5 [v1.04]** — Strong-Sector Unification from 600-Cell Geometry. [`flagship_papers/strong/`](flagship_papers/strong/)
- **SF-6 [v1.6]** — Electromagnetism Unified (μ₀, ε₀, c from a tuned toy model; OPEN-FP-6-CONSTANTS).
- **SF-8 [v0.5]** — Emergent Electrostatics: Coulomb's law measured out of the lattice (scalar sector).
- **SF-7 [v0.11, not for deposit]** — Standard Model Unification, *Hierarchy Without Hierarchy* (placeholder). [`flagship_papers/unification/`](flagship_papers/unification/)
- **Capotauro [v2.3]**, **Chirality Continuum [v1.0]**, **F.1 Dynamical Substrate Law [v1.0]** — the substrate-chirality arc (`series_umbrella/`).

The strategic frame governing flagship-paper selection and the SF-line architecture is in [`research_priorities.md`](research_priorities.md) and [`flagship_papers/README.md`](flagship_papers/README.md).

---

## Series Papers (see [`paper_catalog.md`](paper_catalog.md) for the full, current list)

No paper is yet deposited in the CERN repository (Zenodo); deposits are made by Isak, who builds the PDFs, once the founder approves each paper in [`osf_deposit_queue.md`](osf_deposit_queue.md). Source files and documentation are in this repository. The table below is the April 2026 core set, with each row's current status noted; the Gravitation series (GR-1, GR-1a–1j, GR-2), SF-6, SF-8, EU-1, TP-1 and the DM papers came later.

| ID | Title | Key Result |
|----|-------|------------|
| **SS-1** | The Strong Sector from the 600-Cell Lattice | SU(3) colour algebra derived exactly; β₀ = 7; 9 theorems |
| **SS-2** | Lattice-Scale Grounding and Nucleon Structure | l_unit = 0.589 fm; r_proton = 0.883 fm (+5%) — **held pending critique** |
| **SS-3** | Uniqueness of SU(3) from the Tetrahedral Cage | SU(3) is the unique algebra of 3 colour vertices; 4+4 physical mode basis |
| **SS-4** | String Tension from the 600-Cell Face-Mode Multiplicity | σ = M₀z²/(φ l_edge) = 926.5 MeV/fm (+1.8% vs Cornell) — conditional |
| **SS-5** | Light-Nuclei Binding Energies from Open-Vertex Cascade | d, ³H, ³He, ⁴He all ≤5.3% error; ⁵He/⁵Li/⁸Be unbound — conditional; **held pending critique** |
| **SS-6** | Deuteron Observables Beyond Binding: Scope and Limits of the Base-to-Base Picture | Scoping paper: rigid-bipyramid intrinsic Q_d oblate (reveals Q_d orbital-dominated); zero-range a_np = 1/κ = 4.32 fm from B_d alone |
| **SS-7** | Alpha-Cluster Regime and the 3N−6 Edge Formula for Medium-Mass Nuclei | 12 strict-N=Z alpha-chain bindings ¹²C through ⁵⁶Ni, RMS 0.80% — conditional; uses the measured ⁴He binding as input |
| **SS-8** | Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope | 42 conditional zero-parameter predictions; sub-1% agreements at ²⁶Mg octahedron and ⁴²Ca gyroelongated square bipyramid |
| **SM-1** | Binding Mechanisms and Cage Stability | Tetrahedral cage as electron ground state; δ = 1/3; SSV₀ = 0.2555 MeV |
| **SM-2** | Mass Generation from Geometric Hierarchies | Semi-empirical mass framework; one calibration constant k ≈ 0.0185 |
| **SM-3** | K3 Spectral Theorem and the Koide Formula | K = 2/3 from K₃ eigenvalue ratio, conditional on Layer B (OPEN-SS-16) |
| **SM-4** | Charged Lepton Masses from K3 | 11 ppm consistency; structural impossibility of θ from K3+SSV |
| **SM-5** | Tribimaximal Neutrino Mixing from K3 | U_PMNS = U_TBM from K₃ eigenvectors, zero free parameters — a zeroth-order form (θ₁₂, θ₂₃ differ from data by 8%, 13%) |
| **SR-1** | Mechanistic Derivation of Relativistic Effects | Lorentz invariance from 600-cell lattice wave propagation |
| **SR-2** | The Spin-Bit Axiom / Derived Einstein Quadrupole Formula | A3′ adds the rank-2 GW channel; λ = 16πG/c⁴ at zero new parameters; closes op:einstein (a) (v1.0 SHIPPED) |
| **SM-6** | The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry | sin²θ_W = 3/(8φ); Koide phase derived; 1 calibration, 0 shape parameters |
| **SM-7** | Heavy Quark Mass Spectrum and Strong Coupling | α_s = 5/(8φ); quark Koide phase; m_b 1.4%, m_t 1.7% (two-calibration route, superseded by SF-3) |
| **SM-8** | Quark Generation Structure from 600-Cell Distance Shells | Zero-param quark masses RMS 2.1%; four-bonded-cage-types theorem (per Theorem 4.1) |
| **SM-9** | The Quark Mass Scaling Exponent | V^(7/3) derivation; Symmetry Degeneracy Theorem |
| **SM-10** | First-Principles Quark Mass from FEM Chain Network Simulation | Cascade mechanism; two-regime physics; organised DP density |

---

## Strongest Results (basis stated; full audited table in [`theory-overview.md`](theory-overview.md))

| Result | Precision | Source | Basis |
|--------|-----------|--------|-------|
| Weinberg angle sin²θ_W = 3/(8φ) | 0.24% | SM-6 | zero-param |
| Coupling sum sin²θ_W + α_s = 1/φ; ratio 5/3 | exact | SM-7 | zero-param |
| Koide phase θ = 132.731° | 0.003% | SM-6 | zero-param given K = 2/3 |
| Koide ratio K = 2/3 | 11 ppm | SM-3 | conditional on Layer B |
| Muon, tau masses | 0.18%, 0.15% | SM-6 | 1 calibration (m_e) |
| Heavy-quark masses (s, c, b, t) | RMS 2.1% | SM-8/9, SF-3 | 1 calibration (m_e) |
| m_Z/m_W = 1.141 | 0.57% | SF-2 | zero-param ratio |
| Neutrino m₂, Σm_ν, σ_ν | 1.7%, in bound, 2.0% | SF-4 | 1 calibration (m_e) |
| SU(3) colour algebra; uniqueness; β₀ = 7 | exact / structural | SS-1, SS-3 | zero-param |
| Charge quantisation δ = 1/3 | exact | SM-1 | zero-param |
| Three-generation theorem | structural | SM-8 | within the SM-8 model |
| String tension σ = 926.5 MeV/fm | +1.8% | SS-4 | conditional |
| Light-nuclei bindings (d, ³H, ³He, ⁴He) | +5.3% … −1.4% | SS-5 | conditional; held |
| Alpha-chain nuclei ¹²C→⁵⁶Ni | RMS 0.80% (1.77% fully CPP) | SS-7 | conditional; measured ⁴He input |
| ⁸⁴Mo, ⁸⁸Ru, ⁹²Pd | 0.05–0.13% | SS-9 | calibrated (⁵⁶Ni); held |
| Spectral index n_s = 0.9654 | 0.12σ | EU-1 | framework-conditional; pivot adopted |
| Proton radius, magnetic moment | +5.0%, −0.1% | SS-2 | held pending critique |
| α_s(m_H) = 0.1132 | +0.2% | SS-2 | calibrated in effect (A11 matching) |

---

## Repository Structure

```
CPP/
├── README.md                    ← This file
├── INDEX.md                     ← Directory-by-directory map
├── paper_catalog.md             ← Master list of all papers with IDs and status
├── research_frontier.md          ← ** THE DASHBOARD — all open problems, conjectures, propositions **
├── theorem-registry.md           ← All proved theorems by series with axiom dependencies
├── axiom-registry.md             ← Axiom tracking, prediction counts
├── predictions.md               ← Every quantitative prediction with status
├── nomenclature.md              ← ID code legend (AXIM, THEO, PROP, etc.)
│
├── problem_histories/           ← Problem narratives — the drama of discovery
├── templates/                   ← Formatting standards and documentation templates
│   ├── paper-formatting.md      ← Master formatting standard for all papers
│   └── documentation-suite.md   ← Template for the 8 documentation files per paper
│
├── bibliography/                ← Site-wide bibliography
│   └── cpp_references.bib       ← Aggregated from all local .bib files
│
├── series_strong/               ← SS-1 through SS-5 + companions + notebooks
├── series_standard_model/       ← SM-1 through SM-10 + documentation
├── series_relativity/           ← SR-1, SR-2 + 22 companion papers
├── series_electroweak/          ← EW-1 through EW-5
├── series_quantum_mechanics/    ← QM-1 through QM-6
├── series_foundations/          ← SD-1 through SD-5 (superdeterminism)
├── series_gravitation/          ← GR-1, GR-1a–1j, GR-2
├── series_phenomena/            ← EU-1, TP-1, DM-1–3
├── series_umbrella/             ← Capotauro, chirality continuum, F.1, hardened theorems
├── flagship_papers/             ← SF-1 through SF-8
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
- **Want to contribute?** See [`research_frontier.md`](research_frontier.md) — the complete problem dashboard with recommended attack order.
- **Writing a new paper?** See [`templates/paper-formatting.md`](templates/paper-formatting.md).

---

*Repository maintained by Thomas Lee Abshier ND, Hyperphysics Institute. AI co-authors: Grok (xAI), Claude Sonnet and Opus (Anthropic), Copilot (Microsoft). All papers under CC BY 4.0.*
