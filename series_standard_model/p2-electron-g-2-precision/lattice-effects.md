# Finite-Size Lattice and FBS Propagation Effects

## Current Model
- Continuum approximation for SSV gradients and ZBW paths
- FBS broadcast assumed instantaneous and uniform within PSR

## Next Steps
- Model exact hyperedge paths and finite 120-vertex constraints
- Add graded FBS updates (strong near origin, weak at PSR edge)
- Compute tiny phase/amplitude corrections from lattice discretization

These effects may introduce residuals at 10^{-11}–10^{-13} level, potentially matching or approaching QED precision.

Cross-references: Paper 1 Appendix on FBS mechanism, future lattice MC notebooks

## Run Results (February 13, 2026)
- Samples: 200,000
- Noise modulated by FBS grading (r^{-2})
- eDP: 0.486821 ± 0.016124  
- hDP: 0.333456 ± 0.014892  
- qDP: 0.179723 ± 0.009412  
- δμ_e (mean): 4.605 × 10^{-10}  
- Upper bound: < 5.04 × 10^{-10}
