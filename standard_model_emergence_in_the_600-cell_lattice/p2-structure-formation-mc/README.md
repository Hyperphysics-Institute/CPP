# Full Monte Carlo for Structure Formation from Lattice Defects

This directory performs large-scale Monte Carlo simulations of structure formation seeded by lattice defects from incomplete Capotauro breaking.

## Goals
- Simulate defect formation and distribution in the 600-cell lattice
- Compute the 3D density field and power spectrum P(k)
- Compare to observed large-scale structure (galaxy clustering, BAO, Lyman-α forest)
- Scale to 10^7–10^8 defects on cloud compute for realistic cosmology

## Current Status (February 14, 2026)
- Preliminary small-scale runs: P(k) ≈ k^{-3} (scale-invariant) with lattice oscillations
- Target: Match ΛCDM power spectrum at low k, with deviations at high k (lattice cutoff)

## Computational Notes
- Small runs (10^5 defects): runnable on laptop/Colab
- Medium runs (10^6–10^7): Colab Pro or local GPU
- Large runs (10^8+): Cloud GPU (Vast.ai, AWS) recommended

Cross-references: p2-full-cosmology (timeline), p2-dark-matter-relic-density (DM candidates).

Contents:
- README.md: Overview
- mechanism.md: Defect formation and P(k)
- preliminary-results.md: Initial runs
- figures/: Power spectrum and defect field
- derivations/: Main notebook
