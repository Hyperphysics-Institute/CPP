# Updated mixing_calculator.py with lepton gradients fixed and delta_mu function

import numpy as np
from scipy.optimize import minimize

def calculate_mixing_fractions(N_k, particle_type='lepton'):
    """
    Calculate orbital ZBW DP mixing fractions for leptons or quarks.

    Parameters:
    - N_k: int, cage occupancy (e.g., 4 for muon, 1 for up quark)
    - particle_type: str, 'lepton' or 'quark' (default: 'lepton')

    Returns:
    - dict with 'eDP', 'qDP', 'hDP' fractions
    """
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio ≈1.618
    base_gradient = 1.0

    if particle_type == 'lepton':
        gradients = {
            'eDP': (phi - 1) * base_gradient,  # Favorable (lowest) for leptons
            'hDP': base_gradient,              # Intermediate
            'qDP': phi * base_gradient         # Least favorable
        }
        labels = ['eDP', 'hDP', 'qDP']
    elif particle_type == 'quark':
        gradients = {
            'qDP': (phi - 1) * base_gradient,  # Favorable for quarks
            'hDP': base_gradient,              # Intermediate
            'eDP': phi * base_gradient         # Least favorable
        }
        labels = ['qDP', 'hDP', 'eDP']
    else:
        raise ValueError("particle_type must be 'lepton' or 'quark'")

    T = N_k  # Thermal scale proportional to N_k

    # Energy function to minimize
    def energy(f):
        return np.dot(f, [gradients[label] for label in labels])

    # Constraints: sum to 1
    cons = ({'type': 'eq', 'fun': lambda f: np.sum(f) - 1})
    bounds = [(0, 1)] * 3

    # Minimize energy
    res = minimize(energy, [1/3, 1/3, 1/3], method='SLSQP', bounds=bounds, constraints=cons)
    min_fractions = res.x

    # Thermal probabilities (Boltzmann-like)
    energies = np.array([gradients[label] for label in labels])
    probs = np.exp(-energies / T)
    probs /= np.sum(probs)

    # Equilibrium: average of min and thermal
    equil = 0.5 * min_fractions + 0.5 * probs
    equil /= np.sum(equil)  # Normalize

    return {labels[i]: equil[i] for i in range(3)}

def compute_delta_mu(fracs, C_orig=9.6e-7, alpha_em=1/137.036):
    S = alpha_em / (2 * np.pi)  # Suppression factor
    mixing_sum = fracs['qDP'] + 0.7 * fracs['hDP']
    return C_orig * S * mixing_sum

def sensitivity_sweep(particle_type='quark', N_k_values=[1, 4, 12, 20, 60, 30000]):
    """
    Compute sensitivity of dominant fraction to N_k.

    Returns:
    - list of dominant fractions (eDP for lepton, qDP for quark)
    """
    dominant_fracs = []
    for N_k in N_k_values:
        fracs = calculate_mixing_fractions(N_k, particle_type)
        dominant = fracs['eDP'] if particle_type == 'lepton' else fracs['qDP']
        dominant_fracs.append(dominant)
    return dominant_fracs

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate ZBW mixing fractions")
    parser.add_argument('--N_k', type=int, default=4, help='Cage occupancy')
    parser.add_argument('--type', type=str, default='lepton', choices=['lepton', 'quark'], help='Particle type')
    parser.add_argument('--sweep', action='store_true', help='Run N_k sensitivity sweep')
    
    args = parser.parse_args()
    
    if args.sweep:
        N_k_vals = [1, 4, 12, 20, 60, 30000]
        fracs = sensitivity_sweep(args.type, N_k_vals)
        print(f"{args.type.capitalize()} dominant fractions over N_k {N_k_vals}: {fracs}")
    else:
        fracs = calculate_mixing_fractions(args.N_k, args.type)
        print(f"{args.type.capitalize()} fractions for N_k={args.N_k}: {fracs}")
        if args.type == 'lepton':
            delta_mu = compute_delta_mu(fracs)
            print(f"Predicted δμ: {delta_mu:.2e}")
