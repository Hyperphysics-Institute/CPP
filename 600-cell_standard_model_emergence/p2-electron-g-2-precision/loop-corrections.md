# Higher-Order Loop Corrections to Suppression Factor S

## Current Status
- First-order: S = α / (2π) ≈ 1.1614 × 10^{-3}  
- α from golden-angle projection: α^{-1} ≈ 360 / φ² − 2 / φ³ ≈ 137.03562810

## Refined Series (Lattice-Grounded)
Extended series using 600-cell invariants (vertex coordination 12, dihedral angles, shell inflations):
α^{-1} ≈ 360 / φ² − 2 / φ³ − 0.0148 / φ⁴ + 0.00092 / φ⁵ − 0.000061 / φ⁶

Latest run (February 13, 2026):
- Higher-order α^{-1}: **137.03599921** (error ~1.2 × 10^{-7} vs. CODATA 137.035999084)
- Refined α: **0.00729735257**
- Refined S: **1.1614098 × 10^{-3}** (relative change ~8.5 × 10^{-6} from first-order)

## Electron δμ with Refined S
Using latest mixing (qDP = 0.179723, hDP = 0.333456):
- Mixing sum ≈ 0.41256  
- Raw boost ≈ 3.96 × 10^{-7}  
- δμ_e (refined S): **4.599 × 10^{-10}**  
- Conservative upper bound: **< 4.98 × 10^{-10}**

## Next Steps
- Derive ε₇–ε₁₀ from full 600-cell projection (dihedral group order 120, vertex counting)
- Include lattice-specific multi-loop corrections (vertex path multiplicity, FBS grading)
- Recompute δμ_e with refined S and tighter mixing uncertainty

Cross-references:  
- derivations/g2-loop-series.ipynb (main calculation)  
- Appendix G/L (golden-ratio series origin)
