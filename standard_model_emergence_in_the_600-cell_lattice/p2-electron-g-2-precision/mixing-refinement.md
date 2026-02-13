# Refining Mixing Fractions for Electron (N_k=1)

## Current Status
- Muon (N_k=4): ~68.5% eDP, 13% qDP, 18.5% hDP (mean-field + thermal Boltzmann, Appendix B.1)
- Electron (N_k=1): Lower mixing expected (~85–90% eDP dominant) due to minimal cage → negligible g-2 deviation

## Next Steps
- Replace mean-field with full Monte Carlo over 600-cell lattice paths (or icosahedral subgroup embedding)
- Include exact thermal fluctuations, SSV gradient variation, and FBS broadcast grading
- Target: mixing fractions to ~0.1% precision → deviation bound < 10^{-12}

Once computed, we can plug refined f_qDP and f_hDP into the δμ formula:
δμ ≈ C × (f_qDP + 0.7 × f_hDP) × S

Cross-references: derivations/electron-mixing-mc.ipynb (main calculation notebook)
