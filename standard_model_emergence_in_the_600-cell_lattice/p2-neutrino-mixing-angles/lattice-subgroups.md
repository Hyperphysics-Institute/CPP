# Neutrino Mixing from 600-Cell Lattice Subgroups

The PMNS mixing matrix elements emerge from overlaps between unbound ZBW flavor subgroups in the 600-cell lattice.

## Flavor Subgroups
- ν_e: single eDP orbital (minimal, isotropic)
- ν_μ: single qDP orbital (moderate resonance)
- ν_τ: hDP-tetra cluster (4 interconnected hDPs, highest organization)

## Mixing Mechanism
- The 600-cell has icosahedral subgroups (order 60) and tetrahedral subgroups (order 12).
- Mixing angles from projection overlaps:
  - θ₁₂ ≈ arcsin(√(overlap eDP–qDP / total))
  - θ₂₃ ≈ arcsin(√(overlap qDP–hDP-tetra / total))
  - θ₁₃ ≈ arcsin(√(overlap eDP–hDP-tetra / total)) × χ (chiral bias)
- δ_CP from phase difference in Capotauro bias between subgroups.

## Preliminary Estimate
- sin²θ₁₂ ≈ 0.30–0.32 (from eDP–qDP overlap)
- sin²θ₂₃ ≈ 0.55–0.58 (from qDP–hDP-tetra)
- sin²θ₁₃ ≈ 0.02–0.023 (small due to eDP–hDP-tetra mismatch)

Next: exact overlap integrals via MC over icosahedral/tetrahedral subgroups.

Cross-references: derivations/neutrino-mixing-angles.ipynb
