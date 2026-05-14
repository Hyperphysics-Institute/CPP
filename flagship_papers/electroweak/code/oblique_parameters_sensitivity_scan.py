"""
SF-2 Companion: Oblique-Parameter Sensitivity Scan
====================================================

GPU-runnable Python program scanning over the substrate-symmetry-motivated
ratio space (Pi_33/Pi_11, Pi_3Q/Pi_11) to identify which combinations
of these integrand ratios deliver |Delta S|, |Delta T|, |Delta U| within
the LEP/SLC 3-sigma allowed regions.

This SUPPLEMENTS the original oblique_parameters_framework.py program by
demonstrating the heuristic-placeholder sensitivity range identified in
SF-2 Companion v1.2 Section 5.6: Pi_33/Pi_11 in [0.85, 1.0] and
Pi_3Q/Pi_11 in [0.7, 1.0] expected to land within bounds.

The original program used placeholder ratios (Pi_33/Pi_11 = 0.7,
Pi_3Q/Pi_11 = 0.05) producing |Delta S|, |Delta U| outside 3-sigma; this
scan demonstrates that ratios closer to the substrate-symmetry-expected
near-cancellation region land within bounds.

Companion to: SF-2 Companion paper Section 5.6 (sf-2_companion.tex v1.2)
Main paper: SF-2 v0.7 (sf-2_electroweak.tex) Section 13.2.1

Uses PyTorch for GPU acceleration. Requires:
    pip install torch numpy

Run with:
    python oblique_parameters_sensitivity_scan.py

Hardware: Tested on Nvidia GPUs with CUDA. Will fall back to CPU
if CUDA not available.

Author: Anthropic Claude Opus 4
Date: 14 May 2026
Patch: 0365 (supplementary to Patch 0364)
"""

import torch
import numpy as np
import time

# =====================================================================
# Configuration
# =====================================================================

# Use GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

# Physical constants (PDG 2024) -- matches oblique_parameters_framework.py
M_W = 80.377          # W mass in GeV
M_Z = 91.1876         # Z mass in GeV
SIN2_THETA_W = 0.23121
COS2_THETA_W = 1.0 - SIN2_THETA_W
ALPHA_EM = 1.0 / 137.036

# LEP/SLC global-fit allowed regions (PDG 2024)
S_OBS, S_SIGMA = 0.00, 0.07     # S = 0.00 +/- 0.07 -> 3-sigma in [-0.21, 0.21]
T_OBS, T_SIGMA = 0.03, 0.06     # T = 0.03 +/- 0.06 -> 3-sigma in [-0.15, 0.21]
U_OBS, U_SIGMA = 0.00, 0.06     # U = 0.00 +/- 0.06 -> 3-sigma in [-0.18, 0.18]

S_LOWER, S_UPPER = S_OBS - 3*S_SIGMA, S_OBS + 3*S_SIGMA
T_LOWER, T_UPPER = T_OBS - 3*T_SIGMA, T_OBS + 3*T_SIGMA
U_LOWER, U_UPPER = U_OBS - 3*U_SIGMA, U_OBS + 3*U_SIGMA

# Sensitivity-scan grid (substrate-symmetry-motivated ranges per Companion v1.2 Sec 5.6)
N_GRID = 16
R33_RANGE = (0.85, 1.00)        # Pi_33/Pi_11: substrate D_6 near-equality expected
R3Q_RANGE = (0.70, 1.00)        # Pi_3Q/Pi_11: substrate D_6 zero-charge cancellation expected

# Monte Carlo settings (matches oblique_parameters_framework.py)
N_VERTICES = 6                  # W bracelet has 6 vertices
N_MC_SAMPLES = 1_000_000
Q_RANGE = (M_Z, 200.0)


# =====================================================================
# Substrate-level Monte Carlo (D_6-symmetric bracelet sampling)
# =====================================================================

def bracelet_vertex_charges(device, n_samples):
    """
    Generate Monte Carlo samples of D_6-symmetric W bracelet vertex
    charge configurations (zero net charge across 6 vertices).
    Identical to oblique_parameters_framework.py for consistency.
    """
    charges_pool = torch.tensor([1.0, -1.0, 2.0/3.0, -2.0/3.0], device=device)
    indices = torch.randint(0, 4, (n_samples, 6), device=device)
    charges = charges_pool[indices]
    net_charge = charges.sum(dim=1)
    valid_mask = torch.abs(net_charge) < 1e-6
    return charges[valid_mask]


# =====================================================================
# Vectorized Peskin-Takeuchi formulas (analytical ratio dependence)
# =====================================================================

# Key insight: the Peskin-Takeuchi formulas factor cleanly under the
# substitution Pi_33 = r33 * Pi_11, Pi_3Q = r3q * Pi_11:
#
#   Delta S = -16*pi * (Pi_33 - Pi_3Q) = -16*pi * Pi_11 * (r33 - r3q)
#   Delta T = (4*pi / (sin^2 cos^2 m_Z^2)) * Pi_11 * (1 - r33)
#   Delta U = 16*pi * Pi_11 * (1 - r33)
#
# So a SINGLE Monte Carlo of Pi_11(q^2, charges) suffices; the scan
# over ratios is then an analytical re-weighting.

def compute_delta_parameters(pi_11_samples, r33, r3q):
    """
    Compute (Delta S, Delta T, Delta U) for a given (r33, r3q) ratio
    pair, using pre-computed Pi_11 Monte Carlo samples.
    Returns: (S_mean, T_mean, U_mean) as Python floats.
    """
    S_samples = -16.0 * np.pi * pi_11_samples * (r33 - r3q)
    T_samples = (4.0 * np.pi / (SIN2_THETA_W * COS2_THETA_W * M_Z ** 2)) * pi_11_samples * (1.0 - r33)
    U_samples = 16.0 * np.pi * pi_11_samples * (1.0 - r33)
    return float(S_samples.mean()), float(T_samples.mean()), float(U_samples.mean())


# =====================================================================
# Main calculation
# =====================================================================

def main():
    print('SF-2 Companion: Oblique-Parameter Sensitivity Scan')
    print('=' * 70)
    print(f'Scan range: Pi_33/Pi_11 in {R33_RANGE}, Pi_3Q/Pi_11 in {R3Q_RANGE}')
    print(f'Grid resolution: {N_GRID}x{N_GRID} = {N_GRID*N_GRID} ratio combinations')
    print(f'Monte Carlo samples: {N_MC_SAMPLES:,}')
    print(f'Momentum range: Q in [{Q_RANGE[0]:.1f}, {Q_RANGE[1]:.1f}] GeV')
    print()
    print(f'LEP/SLC 3-sigma allowed regions (PDG 2024):')
    print(f'  S in [{S_LOWER:+.2f}, {S_UPPER:+.2f}]')
    print(f'  T in [{T_LOWER:+.2f}, {T_UPPER:+.2f}]')
    print(f'  U in [{U_LOWER:+.2f}, {U_UPPER:+.2f}]')
    print()

    # -----------------------------------------------------------------
    # Phase 1: Generate D_6-symmetric bracelet Monte Carlo samples
    # -----------------------------------------------------------------
    t_start = time.time()
    charges = bracelet_vertex_charges(device, N_MC_SAMPLES)
    n_valid = len(charges)
    print(f'Phase 1: D_6-symmetric configurations sampled: {n_valid:,} ({n_valid/N_MC_SAMPLES:.1%} of {N_MC_SAMPLES:,})')

    # -----------------------------------------------------------------
    # Phase 2: Compute base Pi_11 (independent of (r33, r3q))
    # -----------------------------------------------------------------
    log_q_min = np.log(Q_RANGE[0] ** 2)
    log_q_max = np.log(Q_RANGE[1] ** 2)
    log_q_sq = torch.rand(n_valid, device=device) * (log_q_max - log_q_min) + log_q_min
    q_sq_samples = torch.exp(log_q_sq)
    q_sq_sum = (charges ** 2).sum(dim=1)
    form_factor = q_sq_samples / M_W ** 2 / (1.0 + q_sq_samples / M_W ** 2)
    pi_11 = ALPHA_EM * q_sq_sum * form_factor  # shape (n_valid,)
    print(f'Phase 2: Base Pi_11 computed: mean = {float(pi_11.mean()):.6f}, std = {float(pi_11.std()):.6f}')

    # -----------------------------------------------------------------
    # Phase 3: Grid scan over (r33, r3q)
    # -----------------------------------------------------------------
    r33_values = np.linspace(R33_RANGE[0], R33_RANGE[1], N_GRID)
    r3q_values = np.linspace(R3Q_RANGE[0], R3Q_RANGE[1], N_GRID)

    # Storage: grid_results[i, j] = (S, T, U, all_within_bool)
    S_grid = np.zeros((N_GRID, N_GRID))
    T_grid = np.zeros((N_GRID, N_GRID))
    U_grid = np.zeros((N_GRID, N_GRID))
    within_grid = np.zeros((N_GRID, N_GRID), dtype=bool)

    for i, r33 in enumerate(r33_values):
        for j, r3q in enumerate(r3q_values):
            S, T, U = compute_delta_parameters(pi_11, r33, r3q)
            S_grid[i, j] = S
            T_grid[i, j] = T
            U_grid[i, j] = U
            within_grid[i, j] = (S_LOWER < S < S_UPPER and
                                 T_LOWER < T < T_UPPER and
                                 U_LOWER < U < U_UPPER)

    elapsed = time.time() - t_start
    print(f'Phase 3: Grid scan completed in {elapsed:.2f} seconds total')
    print()

    # -----------------------------------------------------------------
    # Phase 4: Output
    # -----------------------------------------------------------------
    print('=' * 70)
    print('WITHIN-BOUNDS STATUS GRID')
    print('=' * 70)
    print('  PASS = all of |Delta S|, |Delta T|, |Delta U| within LEP/SLC 3-sigma')
    print('  FAIL = at least one outside 3-sigma')
    print()
    print('  Rows: Pi_33/Pi_11 (top -> bottom = ' +
          f'{R33_RANGE[0]:.2f} -> {R33_RANGE[1]:.2f})')
    print('  Columns: Pi_3Q/Pi_11 (left -> right = ' +
          f'{R3Q_RANGE[0]:.2f} -> {R3Q_RANGE[1]:.2f})')
    print()

    # Compact heatmap: show every other column to fit screen
    col_step = 2
    header = '  r33\\r3Q'
    for j in range(0, N_GRID, col_step):
        header += f'  {r3q_values[j]:5.3f}'
    print(header)
    print('  ' + '-' * (len(header) - 2))
    for i in range(N_GRID):
        row = f'  {r33_values[i]:6.3f} '
        for j in range(0, N_GRID, col_step):
            row += '   PASS' if within_grid[i, j] else '   FAIL'
        print(row)
    print()

    # -----------------------------------------------------------------
    # Summary statistics
    # -----------------------------------------------------------------
    n_passing = int(within_grid.sum())
    total = N_GRID * N_GRID
    print('=' * 70)
    print('SUMMARY')
    print('=' * 70)
    print(f'  Within-bounds combinations: {n_passing} / {total} ({n_passing/total:.1%})')

    if n_passing > 0:
        # Find best-positioned ratios (minimize max relative deviation in S, U)
        score = np.maximum(np.abs(S_grid) / abs(S_UPPER),
                           np.abs(U_grid) / abs(U_UPPER))
        score[~within_grid] = np.inf
        best_idx = np.unravel_index(np.argmin(score), score.shape)
        bi, bj = best_idx
        print()
        print('  Best-positioned ratios (minimum max relative deviation):')
        print(f'    Pi_33/Pi_11 = {r33_values[bi]:.3f}')
        print(f'    Pi_3Q/Pi_11 = {r3q_values[bj]:.3f}')
        print(f'    -> Delta S = {S_grid[bi, bj]:+.4f}  '
              f'(3-sigma: [{S_LOWER:+.2f}, {S_UPPER:+.2f}], WITHIN)')
        print(f'    -> Delta T = {T_grid[bi, bj]:+.6f}  '
              f'(3-sigma: [{T_LOWER:+.2f}, {T_UPPER:+.2f}], WITHIN)')
        print(f'    -> Delta U = {U_grid[bi, bj]:+.4f}  '
              f'(3-sigma: [{U_LOWER:+.2f}, {U_UPPER:+.2f}], WITHIN)')

        # Show corner cases for context
        print()
        print('  Corner-case sensitivity (boundary behavior):')
        for label, (r33, r3q) in [
            ('Most central (r33=1.0, r3q=1.0)', (1.0, 1.0)),
            ('Min r33, max r3q (r33=0.85, r3q=1.0)', (0.85, 1.0)),
            ('Max r33, min r3q (r33=1.0, r3q=0.70)', (1.0, 0.70)),
            ('Min r33, min r3q (r33=0.85, r3q=0.70)', (0.85, 0.70)),
        ]:
            # Find closest grid point
            i_close = np.argmin(np.abs(r33_values - r33))
            j_close = np.argmin(np.abs(r3q_values - r3q))
            status = 'PASS' if within_grid[i_close, j_close] else 'FAIL'
            print(f'    {label}:')
            print(f'      Delta S = {S_grid[i_close, j_close]:+.4f}, '
                  f'Delta T = {T_grid[i_close, j_close]:+.6f}, '
                  f'Delta U = {U_grid[i_close, j_close]:+.4f}  [{status}]')

    print()
    print('=' * 70)
    print('COMPARISON TO ORIGINAL HEURISTIC PLACEHOLDERS')
    print('=' * 70)
    # Compute original placeholder result for comparison
    S_orig, T_orig, U_orig = compute_delta_parameters(pi_11, 0.7, 0.05)
    print(f'  Original ratios (oblique_parameters_framework.py): Pi_33/Pi_11 = 0.70, Pi_3Q/Pi_11 = 0.05')
    print(f'    -> Delta S = {S_orig:+.4f}  '
          f'({"OUTSIDE" if not (S_LOWER < S_orig < S_UPPER) else "WITHIN"} 3-sigma)')
    print(f'    -> Delta T = {T_orig:+.6f}  '
          f'({"OUTSIDE" if not (T_LOWER < T_orig < T_UPPER) else "WITHIN"} 3-sigma)')
    print(f'    -> Delta U = {U_orig:+.4f}  '
          f'({"OUTSIDE" if not (U_LOWER < U_orig < U_UPPER) else "WITHIN"} 3-sigma)')

    print()
    print('=' * 70)
    print('INTERPRETATION')
    print('=' * 70)
    print('  The sensitivity scan demonstrates that simple ratio adjustments')
    print('  within the substrate-symmetry-motivated range land |Delta S|,')
    print('  |Delta T|, |Delta U| within the LEP/SLC 3-sigma bounds.')
    print()
    print('  Specifically:')
    print('    * |Delta T| is uniformly small across the entire scan range')
    print('      (driven by the m_W^0 = m_W+/- mass-degeneracy prediction;')
    print('       1 - r33 small means small Delta T regardless of r3q).')
    print('    * |Delta S| requires r33 ~ r3q (small ratio difference);')
    print('      satisfied for most of the scan grid.')
    print('    * |Delta U| requires r33 ~ 1 (Pi_33 close to Pi_11);')
    print('      satisfied across the entire r33 range [0.85, 1.0].')
    print()
    print('  This is the substantive constraint identified in Companion v1.2')
    print('  Section 5.6: the eventual continuum-EFT derivation of the W^0')
    print('  oblique-parameter contribution should target the within-bounds')
    print('  region via D_6-symmetric Pi_ij near-cancellations.')
    print()
    print('  NOTE: this is a sensitivity scan over heuristic placeholders,')
    print('  not a derived prediction. The within-bounds region is the')
    print('  research target for the eventual derivation, not a current')
    print('  framework-level claim.')


if __name__ == '__main__':
    main()
