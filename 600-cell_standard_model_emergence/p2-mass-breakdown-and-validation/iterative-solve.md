# Iterative Solve Algorithm for Mass Convergence

CPP masses are computed iteratively from the base formula m c² = y_k · ⟨ϕ⟩ + refinements(m), as refinements depend on m.

## Algorithm (Section 5)
1. Initialize: m_0 = y_k · ⟨ϕ⟩ (base from VEV and Yukawa).
2. Compute refinements: E_eDP, E_inter, E_cloud, E_DP, residual (using m_n, σ, N_k, DP mix).
3. Update: m_{n+1} = m_n + sum(refinements(m_n)).
4. Converge: Repeat until |m_{n+1} - m_n| < 10^{-6} MeV (rapid, <10 iterations due to perturbative nature).

## Justification
Refinements are small (~10-40% of base for most), ensuring convergence. Mass-dependent terms (e.g., E_ZBW = ½ m (c / r_eff)²) reflect self-consistent organization.

Cross-references: Section 5 (universal refinements), Section 6 (validation).
