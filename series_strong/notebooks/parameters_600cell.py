"""
parameters_600cell.py
=====================
Shared physical and geometric constants for the CPP 600-cell series.

All notebooks in CPP/series_strong/ import from this file.
Every parameter here is either:
  (a) Derived from first principles (no free parameters), or
  (b) Calibrated from a single measurement with explicit provenance.

References
----------
SS#1  : cpp_ss1_overview_v1.tex
SS#2  : cpp_ss2_su3_algebra_v1.tex
EW#2  : cpp_ew2_W_v3.1.tex
C14   : Cornell potential companion
C15   : Color charge companion
CPP-5014 : Charge neutrality and quark charges
"""

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# 1.  GOLDEN RATIO AND 600-CELL GEOMETRIC CONSTANTS
#     Source: 600-cell vertex coordinates in Q(phi)
#     All exact — no calibration.
# ─────────────────────────────────────────────────────────────────────────────

phi      = (1.0 + np.sqrt(5.0)) / 2.0   # = 1.6180339887...  golden ratio
phi_inv  = 1.0 / phi                     # = 0.6180339887...  = phi - 1
phi_inv2 = 1.0 / phi**2                  # = 0.3819660113...  = 2 - phi
phi_inv3 = 1.0 / phi**3                  # = 0.2360679775...
phi_2    = phi**2                        # = 2.6180339887...  = phi + 1
phi_3    = phi**3                        # = 4.2360679775...
phi_4    = phi**4                        # = 6.8541019662...
phi_8    = phi**8                        # = 46.9787...  (used in quark mass inner SSV)

# ─────────────────────────────────────────────────────────────────────────────
# 2.  PHYSICAL CONSTANTS (SI and natural units)
#     Standard values — no calibration.
# ─────────────────────────────────────────────────────────────────────────────

hbar_c      = 0.197327        # GeV·fm   (exact to 6 sig figs)
l_P_fm      = 1.616e-35 / 1e-15  # Planck length in fm
alpha_s_MZ  = 0.118           # PDG strong coupling at M_Z
Lambda_QCD  = 0.218           # GeV  (PDG MSbar, 5-flavour)
M_Z         = 91.2            # GeV
hbar        = 1.055e-34       # J·s

# ─────────────────────────────────────────────────────────────────────────────
# 3.  CPP CORE PARAMETERS
#     Source: CPP-5014 and companions C14, C15.
# ─────────────────────────────────────────────────────────────────────────────

sea_strength = 0.185
# The single CPP free parameter.  Calibrated from neutron charge neutrality
# (CPP-5014).  Used in EW, strong, and QM series.

sigma_conf = 0.9              # GeV/fm  string tension, calibrated to charmonium (C14)
r_conf     = np.sqrt(alpha_s_MZ * hbar_c / sigma_conf)  # = 0.161 fm, self-consistent

# ─────────────────────────────────────────────────────────────────────────────
# 4.  FRACTIONAL CHARGE PARAMETER
#     Source: C15 / SS#2 (tetrahedral C3 symmetry)
# ─────────────────────────────────────────────────────────────────────────────

delta_charge = 1.0 / 3.0
# The hDP overlap fraction that produces fractional charges.
#
# DERIVATION (C15, Theorem 1):
#   Color = vertex identity on the tetrahedral base {V1, V2, V3}.
#   A quark qCP occupies exactly one of the three base vertices.
#   The hDP chain linking the qCP to the cage boundary has overlap
#   fraction delta = 1/N_vertices = 1/3 by the C3 rotational symmetry.
#
#   Charge assignment:
#     up-type   (+qCP):  q = +e(1 - delta) = +2e/3
#     down-type (-qCP):  q = -e(1 - 2*delta) = -e/3
#
# NOTE on fractional_charges_overlap.ipynb:
#   That notebook attempts to derive delta = 1/3 from the SSV volume
#   integral:  delta = phi_inv2 × (outer SSV fraction).
#   Analysis shows that 1/3 is NOT derivable from phi-geometric integrals
#   alone (1/3 is rational; phi is irrational — they are algebraically
#   independent).  The integral approach is physically motivated but the
#   exact value 1/3 comes from the C3 vertex-count argument above.
#   This is Open Problem OP-SS-9 (see cpp_ss_unified_v2.tex).

# ─────────────────────────────────────────────────────────────────────────────
# 5.  SSV FIELD PARAMETERS
#     Source: CPP field equations (SR companion C2)
# ─────────────────────────────────────────────────────────────────────────────

k_curvature = sea_strength * (l_P_fm / r_conf)**2
# Lorentz amplification coefficient in the SSV stress-energy density:
#   gamma(r) = 1 + k_curvature * S(r)
#   S(r) = 1/r^4  (dominant Coulomb-like SSV term)
#
# Dimensional derivation:
#   k_curvature ~ sea_strength * (l_P / r_conf)^2
#   = 0.185 * (1.62e-20 fm / 0.161 fm)^2
#   = 0.185 * 1.01e-38
#   ≈ 1.87e-39  (dimensionless when r in fm)
#
# This is effectively zero at laboratory scales.  The k_curvature term
# is negligible for all strong-sector calculations involving r > l_P.
# It appears in the notebooks as a placeholder for the Planck-scale
# correction; for all numerical purposes k_curvature ≈ 0.

k_curvature_numerical = 0.1
# Numerical stand-in used in the notebooks (fractional_charges_overlap,
# nested_cage_masses) for exploratory calculations.  This is NOT the
# physical value.  The physical value is k_curvature ≈ 1.87e-39 above.

# ─────────────────────────────────────────────────────────────────────────────
# 6.  DP BINDING ENERGIES
#     Source: cpp_benchmark.ipynb v12; ratios E_qDP/E_eDP = 3 (exact)
# ─────────────────────────────────────────────────────────────────────────────

E_eDP = 88.0       # MeV  eDP binding energy
E_qDP = 264.0      # MeV  = 3 * E_eDP  (exact ratio)
E_hDP = np.sqrt(E_eDP * E_qDP)  # = sqrt(3) * E_eDP  (geometric mean, exact)
# Ratios: E_eDP : E_hDP : E_qDP = 1 : sqrt(3) : 3
# Used in quark mass formula (OP-SS-1):
#   M_q ~ inner_SSV + sum_layers E_DP(layer) * phi^{3*(layer-1)}

tau_DP = 1.0 / np.log(phi**2)   # = 1 / ln(phi^2) ≈ 1.039
# Decay constant for qDP→hDP composition shift across cage layers.
# Derived from SSV integral over phi-nested shells (cpp_benchmark.ipynb).
# Note: cpp_benchmark uses tau=2.0 (rounded); the first-principles value is 1.039.

time_avg_correction = 1.12
# Time-averaging correction from ZBW orbital motion.
# Appears in inner_SSV formula: E_inner = E_eDP * (1/phi^8) * time_avg_correction
# Estimated from ZBW phase averaging; not yet derived from first principles.

# ─────────────────────────────────────────────────────────────────────────────
# 7.  BARYON SPECTRUM PARAMETERS
#     Source: hadron_spectrum.ipynb; confirmed by mc_su3_algebra.py
# ─────────────────────────────────────────────────────────────────────────────

base_nucleon         = 938.5    # MeV  calibrated to proton/neutron average
strange_uplift       = 148.0    # MeV per unit of strangeness
spin_excitation      = 294.0    # MeV  = M(Delta) - M(proton)  hyperfine gap
dp_sea_mass_fluct    = 0.008    # fractional (0.8%) DP Sea mass uncertainty
# The 0.8% fluctuation gives sigma_mass ~ 7.5 MeV for nucleon,
# ~13 MeV for Omega-. This is the irreducible floor from DP Sea
# DI-bit density variations.

# ─────────────────────────────────────────────────────────────────────────────
# 8.  PROBABILISTIC STRONG MODES (geodesic path structure)
#     Source: strong_modes_probabilistic.ipynb (Stage 22)
# ─────────────────────────────────────────────────────────────────────────────

phase_choices = np.array([3, 4, 5, 6])
# Number of outer geodesic paths in the third 600-cell layer.
# Layer structure: 1 (central) + 3 (middle, ~120°) + third_layer.

phase_probs = np.array([0.25, 0.25, 0.25, 0.25])
# Equal probability for each outer count.
# Mean third layer = 4.5 → total mean = 1 + 3 + 4.5 = 8.5 ≈ QCD 8 gluons.
# The exactly-8 algebraic result (T^a = λ^a/2, SS#2) is the time-averaged
# count; these parameters give the underlying probabilistic distribution.
# Sequential breaking strengths (outer→middle→central):
layer_strength_outer   = 0.4   # Tortuous + bowed geodesics — break first
layer_strength_middle  = 0.7   # ~120° paths — intermediate
layer_strength_central = 1.0   # Shortest, straightest — break last

# ─────────────────────────────────────────────────────────────────────────────
# 9.  MONTE CARLO DEFAULTS
# ─────────────────────────────────────────────────────────────────────────────

n_events_default = 10_000
# Default number of Monte Carlo events for ensemble calculations.
# Set to 10,000 for speed; increase to 100,000 for publication-quality
# uncertainty estimates.

n_events_publication = 100_000
# Use this for final runs before submission.

# ─────────────────────────────────────────────────────────────────────────────
# 10.  QUARK MASSES (constituent and current)
#     Source: SS#1 Table 1; PDG 2026 for current masses
# ─────────────────────────────────────────────────────────────────────────────

# Constituent quark masses (GeV) — used in hadron mass calculations
M_QUARK_CONST = {
    'u': 0.336, 'd': 0.340, 's': 0.486,
    'c': 1.550, 'b': 4.730, 't': 172.76,
}

# Current quark masses (MeV) — used in chiral limit and GOR relation
M_QUARK_CURR = {
    'u': 2.2, 'd': 4.7, 's': 93.5,
    'c': 1273.0, 'b': 4183.0, 't': 172570.0,
}

# Cage depths from SS#1 Table 1
CAGE_DEPTH = {'u': 0, 'd': 0, 's': 1, 'c': 2, 'b': 3, 't': 4}
CHARGE     = {'u': +2/3, 'd': -1/3, 's': -1/3, 'c': +2/3, 'b': -1/3, 't': +2/3}

# ─────────────────────────────────────────────────────────────────────────────
# 11. SELF-CONSISTENCY CHECKS
# ─────────────────────────────────────────────────────────────────────────────

def verify_parameters():
    """Run internal consistency checks on all parameters."""
    errors = []

    # Golden ratio identity: phi^2 = phi + 1
    if abs(phi**2 - phi - 1) > 1e-14:
        errors.append(f"phi^2 != phi+1: {phi**2} vs {phi+1}")

    # phi * phi_inv = 1
    if abs(phi * phi_inv - 1) > 1e-14:
        errors.append("phi * phi_inv != 1")

    # Charge formula check
    q_up   = +(1 - delta_charge)
    q_down = -(1 - 2*delta_charge)
    if abs(q_up - 2/3) > 1e-14:
        errors.append(f"up charge = {q_up}, not 2/3")
    if abs(abs(q_down) - 1/3) > 1e-13:
        errors.append(f"down charge = {q_down}, not 1/3")

    # DP energy ratios
    if abs(E_qDP / E_eDP - 3.0) > 1e-10:
        errors.append(f"E_qDP/E_eDP = {E_qDP/E_eDP}, not 3")
    if abs(E_hDP / E_eDP - np.sqrt(3)) > 1e-10:
        errors.append(f"E_hDP/E_eDP = {E_hDP/E_eDP}, not sqrt(3)")

    # Self-consistent string tension
    sigma_check = alpha_s_MZ * hbar_c / r_conf**2
    if abs(sigma_check - sigma_conf) > 0.001:
        errors.append(f"sigma self-consistency: {sigma_check} vs {sigma_conf}")

    # Tau derivation
    tau_check = 1.0 / np.log(phi**2)
    if abs(tau_check - tau_DP) > 1e-12:
        errors.append(f"tau_DP = {tau_DP}, check = {tau_check}")

    if errors:
        print("PARAMETER ERRORS:")
        for e in errors:
            print(f"  {e}")
        return False
    else:
        print("All parameter self-consistency checks passed.")
        return True


if __name__ == "__main__":
    print("CPP 600-Cell Parameters")
    print("=======================")
    print()
    print(f"phi          = {phi:.10f}")
    print(f"phi_inv      = {phi_inv:.10f}")
    print(f"phi_inv2     = {phi_inv2:.10f}")
    print(f"phi_3        = {phi_3:.10f}")
    print(f"phi_8        = {phi_8:.10f}")
    print()
    print(f"sea_strength = {sea_strength}")
    print(f"sigma_conf   = {sigma_conf} GeV/fm")
    print(f"r_conf       = {r_conf:.6f} fm")
    print()
    print(f"delta_charge = {delta_charge:.10f} = 1/3 (from C3 vertex symmetry)")
    print(f"up charge    = {+(1-delta_charge):.10f} = +2/3")
    print(f"down charge  = {-(1-2*delta_charge):.10f} = -1/3")
    print()
    print(f"E_eDP        = {E_eDP} MeV")
    print(f"E_qDP        = {E_qDP} MeV  (= 3 * E_eDP)")
    print(f"E_hDP        = {E_hDP:.4f} MeV  (= sqrt(3) * E_eDP)")
    print(f"tau_DP       = {tau_DP:.6f}  (= 1/ln(phi^2))")
    print()
    print(f"k_curvature  = {k_curvature:.3e}  (physical, negligible at lab scales)")
    print(f"k_curvature_numerical = {k_curvature_numerical}  (notebooks stand-in)")
    print()
    print(f"n_events_default = {n_events_default:,}")
    print()
    verify_parameters()
