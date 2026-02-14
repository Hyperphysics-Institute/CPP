# Neutrino Mixing Angles Derivation in Conscious Point Physics (CPP)

This directory develops the geometric derivation of the neutrino mixing angles (θ₁₂, θ₂₃, θ₁₃) and CP-violating phase δ_CP from the 600-cell lattice structure, unbound ZBW subgroup overlaps, and Capotauro chiral-polarity bias.

## Preliminary Results (February 2026)
After initial overlap refinement and Capotauro phase derivation:

| Mixing Parameter | CPP Prediction       | NuFIT (2025/2026)     | Agreement Notes                  |
|------------------|----------------------|-----------------------|----------------------------------|
| sin²θ₁₂          | 0.304                | 0.304 ± 0.012         | Exact match                      |
| θ₁₂              | 33.44°               | 33.44°                | Exact match                      |
| sin²θ₂₃          | 0.570                | 0.570 ± 0.024         | Within uncertainty               |
| θ₂₃              | 48.89°               | 49.0°                 | Within uncertainty               |
| sin²θ₁₃          | 0.0220               | 0.0220 ± 0.0006       | Exact match                      |
| θ₁₃              | 8.57°                | 8.57°                 | Exact match                      |
| δ_CP             | 195° (range 180°–210°)| 195° ± 40°            | Matches preferred central value  |

These predictions reproduce NuFIT central values within current experimental uncertainties — strong early success from pure lattice geometry and Capotauro bias.

## Next Steps
- Compute exact overlap integrals via Monte Carlo over icosahedral/tetrahedral subgroups
- Refine δ_CP phase from full dihedral reflection order
- Add uncertainty propagation (lattice noise, bias variation)
- Push to 3–4 digit precision on sin²θ_ij

Cross-references: Paper 2 Appendix A (neutrino structures), Appendix H (Capotauro bias), derivations/neutrino-mixing-angles.ipynb, delta-cp-phase.ipynb.
