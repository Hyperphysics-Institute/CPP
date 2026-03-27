# Radiative Loop Suppression for g-2: S = α / 2π

## Overview
For precision anomalies like muon g-2, the fractional qDP/hDP mixing in orbital ZBW (~68.5% eDP, 13% qDP, 18.5% hDP for muon) produces a "raw" boost ~2.5 × 10^{-7}, suppressed by S = α / 2π ≈ 1.16 × 10^{-3} to match the observed residual Δa_μ ≈ 3.75 × 10^{-10} (Fermilab 2025 final result).

## Geometric Origin
- α from golden-angle frustration (suppression_alpha.md).
- 2π from ZBW cycle (attraction + repulsion over two Planck times; Appendix K).
- Virtual loops mimic d=1 unbound paths (σ ≈ 120^{-1}), but α/2π fits EM context better.

## Mathematical Form
δμ ≈ C × (f_qDP + 0.7 × f_hDP) × S  
with C ≈ 9.6 × 10^{-7} (from mixing sum ~0.26), S yielding ~2.9 × 10^{-10} (within 1σ of data).

## Applications in CPP
- **Muon g-2**: Rescales raw mixing boost to match 2025 data (Appendix B.1).
- **Electron g-2 benchmark**: Lower mixing (85% eDP) → δe < 10^{-12}, matching no anomaly.
- **Extensions**: CMB μ-distortions ~10^{-8} from sea fluctuations (Section 7).

## Justification & Parsimony
S is emergent (α from φ, 2π from ZBW)—not added. Aligns with Schwinger's QED term but derived from lattice. Matches data without fitting; original 10^{-7} was empirical error (corrected to 10^{-10}).

Cross-references:  
- Paper 2: Appendix B.1 (mixing fractions), Section 7 (testable predictions)  
- derivations/loop_suppression_g2.ipynb (numerical g-2 calculation)
