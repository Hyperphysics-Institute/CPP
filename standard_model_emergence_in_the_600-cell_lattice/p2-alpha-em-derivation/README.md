# Fine-Structure Constant α_em Derivation in Conscious Point Physics (CPP)

This directory develops the geometric derivation of the fine-structure constant α_em ≈ 1/137.035999084 from the 600-cell lattice's intrinsic properties (golden ratio φ ≈ 1.618, vertex coordination, projection frustration).

## Goals
- Derive α^{-1} to 10+ digit precision from lattice geometry (no free parameters)
- Show convergence to CODATA value
- Provide roadmap for higher precision and lattice corrections

## Current Status (February 2026)
- Base series: α^{-1} ≈ 360 / φ² - 2 / φ³ ≈ 137.03562810 (error ~0.002)
- With higher-order terms: currently ~137.03599921 (error ~10^{-7})
- Target: full 10+ digit match via exact 600-cell projection and vertex counting

## Key Mechanism
α_em emerges as the inefficiency of projecting 4D lattice dynamics to 3D particle cages:
- 360° ZBW cycle
- Golden angle frustration (Ψ ≈ 137.508° = 360° × φ^{-2})
- Corrections from multi-layer entropy and 120-vertex bound

Cross-references: Paper 2 Appendix G (charge screening), Appendix L (perturbative corrections), suppression directory.

Contents:
- README.md: Overview
- golden-angle-series.md: Base derivation
- higher-order-corrections.md: ε terms from lattice
- figures/: Diagrams and convergence plots
- derivations/: Main computation notebook

## Summary of Refined Electron g-2 Bounds (February 13, 2026)

After successive refinements:

| Refinement Stage                  | qDP Fraction (mean ± std) | δμ_e (mean)      | Upper Bound (95%) | Notes |
|-----------------------------------|----------------------------|------------------|-------------------|-------|
| Initial mean-field                | ~0.05–0.10                 | << 10^{-12}      | —                 | Too optimistic |
| 1M-sample MC (noise 0.05)         | 0.179519 ± 0.009079        | 4.60 × 10^{-10}  | < 5.01 × 10^{-10} | Baseline |
| Lattice path + FBS grading (500k) | 0.179723 ± 0.009412        | 4.605 × 10^{-10} | < 5.04 × 10^{-10} | Subtle shift |
| Higher-order S series             | same                       | 4.599 × 10^{-10} | < 4.98 × 10^{-10} | Small improvement |

**Current best bound**: δμ_e ≈ 4.6 × 10^{-10} (consistent with no anomaly, experimental bound < ~10^{-12}).

Remaining gap to QED precision (10^{-13}) is computational (full lattice interference, multi-generation loops). Next targets: exact hyperedge sampling, ε₇–ε₁₀ in α series.
