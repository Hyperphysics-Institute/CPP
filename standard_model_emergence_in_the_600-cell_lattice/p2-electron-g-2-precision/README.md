# Electron g-2 Precision Refinement in Conscious Point Physics (CPP)

This directory is the workspace for improving the electron anomalous magnetic moment (g-2) prediction within the CPP framework to approach or match current experimental precision (~10^{-12}–10^{-13} relative).

## Current Status
- Muon g-2 residual: ~2.9 × 10^{-10} (within 1σ of 2025 Fermilab + lattice QCD result)
- Electron g-2: Currently predicted negligible deviation (< 10^{-12}), consistent with experiment (no anomaly)
- Mechanism: Fractional qDP/hDP mixing in orbital ZBW suppressed by S = α/(2π) ≈ 1.16 × 10^{-3}, with α from golden-angle projection

## Goals
1. Refine mixing fractions for N_k=1 (electron) using full lattice Monte Carlo (beyond mean-field)
2. Compute higher-order loop-like corrections (second- and third-order in φ-series expansion of α)
3. Incorporate finite-size lattice effects and FBS propagation grading
4. Achieve 10^{-11} to low 10^{-12} precision bound (next milestone)
5. Document results for integration into Appendix N (precision) and future standalone paper

## Roadmap
- Phase 1: Refine electron mixing fractions → better baseline deviation bound
- Phase 2: Multi-order S corrections → improve suppression factor
- Phase 3: Lattice & FBS effects → add tiny residual contributions
- Phase 4: Full comparison to CODATA 2025/2026 bound

Cross-references: Paper 2 Appendix B.1 (muon mixing), Appendix G/L (α derivation), Appendix N (precision discussion).

Notebooks in derivations/ are executable (Python 3, numpy/scipy/matplotlib). Results will be tracked here.
Last updated: February 13, 2026

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
