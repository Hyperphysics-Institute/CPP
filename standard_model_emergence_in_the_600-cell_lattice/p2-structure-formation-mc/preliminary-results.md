# Preliminary Results from Structure Formation MC

## Small-Scale Run (N_defects = 100,000, grid_size = 64)
- Mean density: 0.038  
- P(k): scale-invariant at low k (~k^{-3}), oscillations at high k (lattice imprint)  
- Qualitative: Sparse filamentary clustering

## Medium-Scale Run (N_defects = 1,000,000, grid_size = 128)
- Mean density: 0.382  
- P(k): stronger scale-invariance at low k (slope ≈ -2.95 to -3.05)  
- Pronounced oscillations at high k (lattice periodicity)  
- Defect clustering: Clear filamentary + void structure

These preliminary runs confirm the mechanism — scale-invariant power spectrum at large scales with lattice-induced oscillations at small scales — consistent with seeding large-scale structure.

Next: larger runs (5–10M defects) on cloud GPU for production P(k).

Cross-references: derivations/structure-formation-mc.ipynb
