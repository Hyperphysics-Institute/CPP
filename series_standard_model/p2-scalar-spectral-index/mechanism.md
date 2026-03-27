# Mechanism: n_s from φ^n Power Spectrum Tilt

The scalar spectral index n_s emerges from fluctuations during golden-ratio shell inflation.

## Mechanism
- Shell radii grow as R_n = R_0 × φ^n
- Fluctuation amplitude δρ/ρ ≈ 1 / (φ^n) (from SSV minimization)
- Power spectrum P(k) ∝ k^{n_s - 1}, with k ~ 1/R_n
- Tilt n_s ≈ 1 - 2 / (N_shells × ln φ)

## Preliminary Estimate
- N_shells ≈ 60 (e-folds ~41.6 from previous run)
- n_s ≈ 1 - 2 / (60 × ln φ) ≈ 1 - 2 / (60 × 0.481) ≈ **0.930** (base)
- With corrections (multi-shell averaging): ~0.96–0.97

Next: full MC over shell fluctuations for 0.965 match.

Cross-references: derivations/scalar-spectral-index.ipynb
