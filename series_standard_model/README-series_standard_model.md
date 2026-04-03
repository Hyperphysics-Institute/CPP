# Standard Model Emergence — SM Series

**Deriving particle masses, mixing angles, and the Koide formula from 600-cell geometry**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet and Opus (Anthropic), Copilot (Microsoft)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**OSF Registration:** [doi.org/10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D)
**Last updated:** 2 April 2026

---

## Overview

The SM series derives the Standard Model particle spectrum from the 600-cell lattice. The headline result is SM-6: the complete charged lepton mass spectrum (electron, muon, tau) from one calibration constant and zero free shape parameters, with the Weinberg angle and Koide phase both derived from lattice geometry.

---

## Papers

| ID | Title | Version | Key Result |
|----|-------|---------|------------|
| **SM-1** | Binding Mechanisms and Cage Stability | v6 | Tetrahedral cage ground state; δ = 1/3 charge quantisation; SSV₀ = 0.2555 MeV |
| **SM-2** | Mass Generation from Geometric Hierarchies | v30 | Semi-empirical mass framework; one calibration constant k ≈ 0.0185 |
| **SM-3** | K3 Spectral Theorem and the Koide Formula | v5 | K = 2/3 derived exactly from K₃ eigenvalue ratio — zero free parameters |
| **SM-4** | Charged Lepton Masses from K3 | v5 | 11 ppm consistency; structural impossibility of θ from K3+SSV alone |
| **SM-5** | Tribimaximal Neutrino Mixing from K3 | v1 | U_PMNS = U_TBM exactly from K₃ eigenvectors — zero free parameters |
| **SM-6** | The Charged Lepton Mass Spectrum | v3 | sin²θ_W = 3/(8φ); cos(θ_Koide) = −(2/3)(1+3/(104φ)); muon 0.18%, tau 0.15% |

---

## Headline Result: SM-6 (April 2026)

The masses of the three charged leptons are derived with **one calibration constant** (the electron mass) and **zero free shape parameters**:
- **Weinberg angle:** sin²θ_W = 3/(8φ) ≈ 0.2318 (PDG: 0.2312, 0.24%)
- **Koide phase:** θ = 132.731° (PDG: 132.732°, 0.003%)
- **Muon mass:** 105.47 MeV (0.18%)
- **Tau mass:** 1774.1 MeV (0.15%)

The Standard Model requires 3 free parameters. Koide reduced to 2. CPP reduces to 1.

---

## Directory Structure

```
series_standard_model/
├── papers/                     ← .tex, .pdf, .bib, and all documentation .md files
├── figures/
│   └── figures-SM-6/           ← 4 SVG + PDF figures for SM-6
├── notebooks/                  ← Verification notebooks
├── cpp-zbw-mixing-fractions/   ← ZBW mixing fraction computations
└── README.md                   ← This file
```

---

## Documentation

Each paper has 8 companion files: development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, and keywords. SM-6 documentation includes the full derivation history with timeline, 5 documented dead ends, and the coupling-ratio dead end that led to the operational Weinberg angle definition.

---

*See the [main README](../README.md) for the full repository overview.*
