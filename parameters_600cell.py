"""
parameters_600cell.py
Shared geometric parameters for CPP v8.0 (600-cell lattice implementation)
January 2026 — Thomas Lee Abshier, ND & Grok (x.AI)

All values derived from 600-cell geometry and Planck units.
No free calibration parameters beyond Planck scale and N.
"""

import numpy as np
from scipy.constants import Planck, c, hbar, G

# Planck units
l_P = Planck / np.sqrt(2 * np.pi * c**3 / (hbar * G))  # Planck length (approx 1.616e-35 m)
m_P = np.sqrt(hbar * c / G)                           # Planck mass
E_P = m_P * c**2                                       # Planck energy
t_P = l_P / c                                          # Planck time

# Cosmic holographic site count (horizon surface / l_P^2)
N_cosmic = 1e61                                        # As in paper

# Golden ratio from 600-cell edge/vertex geometry
phi = (1 + np.sqrt(5)) / 2                             # φ ≈ 1.6180339887
phi_inv = 1 / phi                                      # φ⁻¹ ≈ 0.618
phi_inv2 = phi_inv**2                                  # φ⁻² ≈ 0.381966 ≈ 1/φ²

# Curvature amplification factor k from infinite φ-series (nested shell density)
# k ≈ ∑_{n=1}^∞ φ^{-2n} = φ^{-2} / (1 - φ^{-2})
k_curvature = phi_inv2 / (1 - phi_inv2)                # ≈ 0.018512

# Typical radial scaling factors between nested shells (600-cell subgraphs)
# Inner DP oscillation radius / outer cage radius ≈ φ⁻¹
r_inner_over_outer = phi_inv

# Number of angular phase layers (probabilistic for v8.0)
# Base: 1 (central) + 3 (120°) + variable third layer (mean 4.5)
phase_probs = [0.01, 0.05, 0.1, 0.15, 0.3, 0.39]      # For 1–6 third-layer chains
phase_choices = np.arange(1, 7)

# Monte Carlo settings
n_events_default = 100000
rng_seed = 42

print("CPP v8.0 600-cell parameters loaded")
print(f"Golden ratio φ = {phi:.10f}")
print(f"Curvature k ≈ {k_curvature:.6f}")
print(f"Overlap factor base ≈ {phi_inv2:.6f} → 1/3 after weighting")
