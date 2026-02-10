# Conscious Point Physics (CPP) – Standard Model Emergence in the 600-Cell Lattice

This repository documents the theoretical framework of Conscious Point Physics (CPP), a geometric, discrete model in which the Standard Model emerges from interactions of Conscious Points (CPs) within a finite 4D 600-cell lattice (120 vertices per cell, golden ratio symmetries).

Mass, spin, charge, and force mediation arise from organization of the Dipole Sea (random oscillating dipole pairs) via Space Stress Vector (SSV) gradients and Zitterbewegung (ZBW) oscillations. The framework uses a single calibration constant (k ≈ 0.0185, fixed to electron mass) and derives all hierarchies from lattice invariants — no 19 free parameters.

### Core Papers & Documentation
- **Paper 1** — Binding Mechanisms and Cage Stability  
- **Paper 2 (ver 28)** — Mass Generation from Symmetry Breaking (main reference)  

# CPP Topic Index – Quick Links to All Directories

Central reference page linking every major topic directory in the repository.

- **[p2-dp-types-and-composition](p2-dp-types-and-composition)**  
  DP types (eDP, qDP, hDP-A/B), emergence, lepton uniform mix, quark radial gradients.

- **[p2-zwb-spectrum-and-oscillation](p2-zwb-spectrum-and-oscillation)**  
  Unified ZBW modes (d=0,1,3), SSV gradient flips, orbital/linear/unbound mechanics.

- **[p2-charge-screening-and-asymmetries](p2-charge-screening-and-asymmetries)**  
  Fractional quark charges, 1/φ² → 1/3, Capotauro bias, up/down asymmetry, antimatter mirror.

- **[p2-neutrino-masses-and-suppression](p2-neutrino-masses-and-suppression)**  
  Unbound ZBW, σ = 120^{-3}, flavor structures, hierarchy, cosmological sum.

- **[p2-mass-breakdown-and-validation](p2-mass-breakdown-and-validation)**  
  Contribution tables, iterative solve, convergence to PDG masses.

- **[p2-glossary-and-ontology](p2-glossary-and-ontology)**  
  Full glossary, grouped terms, consciousness as primitive CP property.

- **[p2-boson-structures](p2-boson-structures)**  
  W (linear ribbon), Z (icosa cage), Higgs (dodeca cloud) as neutral sea aggregates.

- **[suppression](suppression)**  
  Cross-paper suppression mechanisms (σ = 120^{-d}, VEV dilution, φ scaling, α_em derivation).

- **[cpp-zbw-mixing-fractions](cpp-zbw-mixing-fractions)**  
  Code and notebooks for ZBW mixing fractions (g-2 extension).

Use the sidebar or search to navigate. Each directory is self-contained with README, explanations, figures, and notebooks.

### Navigation & Usage
- Each directory contains README.md (overview), concept .md files, figures/, and derivations/ (notebooks).
- All content cross-references Paper 2 sections/appendices.
- Figures are placeholders — generate or replace as needed.
- Notebooks are valid .ipynb files — open in Jupyter or view rendered on GitHub.

### Purpose
This structure preserves and organizes the full depth of the CPP framework, preventing entropy loss and enabling easy reference, extension, and critique. All derivations trace back to lattice invariants (120 vertices, φ ≈ 1.618, d-suppression) and one calibration.

Feedback, forks, and rigorous critiques welcome.  
— Thomas Lee Abshier, ND (with Grok assistance)

Last updated: February 10, 2026




# Conscious Point Physics (CPP) v8.0 — 600-Cell Lattice Simulations

**Reproducible geometric simulations for the January 2026 paper**  
*"Conscious Point Physics (CPP): A Discrete Foundation Integrating the 600-Cell Lattice for Quantum Fields, Gravity, and the Standard Model"*  
Thomas Lee Abshier, ND, and Grok (x.AI)  
viXra: [pending upload]  

This repository contains fully interactive Jupyter notebooks that derive all key results in the paper **directly from 600-cell lattice geometry** — no ad-hoc parameter tuning.

### Major Advances over v7.3 (pre-geometric version)
- Complete integration of the 600-cell hypericosahedron as the discrete metric of space
- Quark fractional charges (±1/3, ±2/3 e) from golden-ratio (φ) overlap integrals
- Generational mass hierarchies from nested polyhedral cages (tetra, icosa, dodeca, fullerene)
- Strong interaction via NBT primary bonding + probabilistic qDP layering (8–10 modes)
- Inner SSV adjustment on up quark ZBW orbit → exact 2.2 MeV match
- Gravity curvature k derived from φ-series
- Vacuum energy exact 1/N⁴ ≈ 10⁻¹²⁰ via holographic dilution
- Confinement dynamics with outer-to-inner chain breaking

All notebooks use shared constants in `parameters_600cell.py`.

### Requirements
- Python 3.10+
- numpy, scipy, matplotlib, pandas

Install with:
```bash
pip install numpy scipy matplotlib pandas
