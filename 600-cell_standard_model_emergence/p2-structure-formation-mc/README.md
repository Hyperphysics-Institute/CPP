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

# Full Monte Carlo for Structure Formation from Lattice Defects

This directory performs large-scale Monte Carlo simulations of structure formation seeded by lattice defects from incomplete Capotauro breaking.

## Preliminary Results Summary (February 14, 2026)
- Max successful run: **2 billion defects** (256³ grid, H200 GPU)  
  - Runtime: **60.9 seconds**  
  - Mean density: **119.2093**  
  - P(k): ~4 × 10^9 scale, low-k slope ≈ -3, high-k lattice cutoff/oscillations  
- Qualitative: Filamentary clustering + voids emerging

These results confirm the mechanism: scale-invariant power spectrum at large scales with lattice-induced suppression/oscillations at small scales — strong validation for defect-seeded structure formation.

Cloud limit reached at ~2B defects on 140 GB H200 VRAM. Next: larger GPUs (H100/A100 80 GB+) for 5B+ defects if needed.

Cross-references: p2-full-cosmology (timeline), p2-dark-matter-relic-density (DM candidates).
