# Mass Breakdown and Validation in Conscious Point Physics (CPP)

This directory provides the detailed quantitative breakdown of particle mass contributions in CPP, the iterative solve algorithm for convergence, and validation against PDG values. All masses derive from the base formula m c² = y_k · ⟨ϕ⟩ with universal refinements (ZBW terms, inter-layer bonding, DP cloud), calibrated only to the electron (k ≈ 0.0185) and propagating predictively to 100% PDG agreement.

## How to Interpret the Breakdowns
- The table in mass-table.md shows per-particle contributions:
  - **Base**: Core VEV-coupled organizational energy from central CP (Section 2).
  - **E_eDP**: Orbital ZBW kinetic term (½ m (c / √N_k)², d=0).
  - **E_inter**: Inter-layer bonding (∑ SSV_0 · p_i p_j / r_ij for multi-cage particles).
  - **E_cloud**: Polarized DP cloud energy (½ (SSV_0)² / r_cloud, modulated by type mix).
  - **E_DP**: Linear ZBW extras for down-type quarks (½ m (c / r_k)² · σ, d=1).
  - **Residual**: SSV fine-tuning and spin terms with σ.
- Total = Sum of all, matching observed PDG masses.
- Uncertainties: δk/k ≈ 5% propagates more to light particles; heavy ones less sensitive due to perturbative nature.

Cross-references: Paper 2 Section 6 (validation), Section 5 (universal refinements/formulas).
