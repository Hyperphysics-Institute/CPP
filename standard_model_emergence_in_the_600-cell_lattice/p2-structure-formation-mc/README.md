# Full Monte Carlo for Structure Formation from Lattice Defects

This directory performs large-scale Monte Carlo simulations of structure formation seeded by lattice defects from incomplete Capotauro breaking.

## Preliminary Results (February 14, 2026)
- Small-scale (100k defects): P(k) ≈ k^{-3} at low k, oscillations at high k
- Medium-scale (1M defects): slope ≈ -2.95 to -3.05, pronounced lattice oscillations
- Qualitative: Filamentary clustering + voids emerging

These runs show the expected behavior: scale-invariant power with lattice imprint.

## Scaling Notes
- 100k–1M: runnable on laptop/Colab
- 5M–10M: Colab Pro or local GPU
- 10^7+: Cloud GPU (Vast.ai, AWS) recommended

Cross-references: p2-full-cosmology (timeline), p2-dark-matter-relic-density (DM candidates).
