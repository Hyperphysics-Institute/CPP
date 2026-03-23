"""
mc_weinberg_unification.py
==========================
Monte Carlo verification of the CPP electroweak sector.
GitHub: CPP/series_electroweak/mc_weinberg_unification.py

Computes and verifies:
  1. Weinberg angle  sin²θ_W  from four-layer eigenvalue-weighted
     phase interference (EW Series #1/#5, Theorem 4).
  2. W boson mass m_W  — bracelet topology, n_v=12 (EW #2).
  3. Z boson mass m_Z  — icosahedral loop, n_v=12 (EW #3).
  4. Higgs-like mass m_H — dodecahedral shell, n_v=20 (EW #4).
  5. Self-consistency cross-check: m_Z/m_W vs. 1/cos(θ_W) (EW #3 §4).

CORRECTIONS vs. published v3 papers
-------------------------------------
The v3 papers contain two numerical errors in intermediate steps that
do NOT affect the final results (which are calibrated) but ARE wrong
in the derivation chain. This code uses the correct values and documents
the discrepancies:

  (A) φ^{-20/3}: paper states 0.01814, correct value is 0.04043.
      Consequence: f_geom^H (paper) = 0.0635; f_geom^H (correct) = 0.1415.
      The published masses are still reproduced because η_H absorbs
      the factor-of-2.23 difference (Open Problem EW-1).

  (B) Sensitivity analysis: paper quotes δm_W ≈ ±0.010 GeV for ±5%
      sea_strength variation. The formula gives δm_W ≈ ±4.0 GeV.
      The paper's values match the PDG uncertainty by construction,
      not by derivation.

References
----------
EW #1 v3 : cpp_ew1_intro_v3.tex   — Weinberg angle, overview
EW #2 v3 : cpp_ew2_W_v3.tex       — W mass, eqs. 4–6
EW #3 v3 : cpp_ew3_Z_v3.tex       — Z mass, eqs. 7–9
EW #4 v3 : cpp_ew4_Higgs_v3.tex   — H mass, eqs. 10–12
EW #5 v3 : cpp_ew5_unification_v3.tex — four theorems, Table 2
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional

# ─────────────────────────────────────────────────────────────────────────────
# 1.  FUNDAMENTAL CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

PHI = (1.0 + np.sqrt(5.0)) / 2.0    # golden ratio φ ≈ 1.6180
HBAR_C_OVER_LP = 1.2209e19           # ℏc/l_P = E_Planck  [GeV]

# ─────────────────────────────────────────────────────────────────────────────
# 2.  SHARED PARAMETERS  (fixed from independent sectors)
# ─────────────────────────────────────────────────────────────────────────────

SEA_STRENGTH       = 0.185   # neutron charge neutrality (CPP-5014)
HYBRID_WEAK_FACTOR = 1.5     # 3 weak layers / 2 EM polarities

# Topology-dependent density enhancement factors
LOOP_DENSITY_FACTOR  = 1.2   # closed icosahedral loop  — Z  (EW #3 §2.2)
SHELL_DENSITY_FACTOR = 1.4   # dodecahedral shell       — H  (EW #4 §2.2)

# Integration ranges  r_max - r_min  [units of l_P]
R_EFF_WZ = 3.5   # W and Z   (EW #2 eq. 6, EW #3 §3.2)
R_EFF_H  = 4.5   # Higgs     (EW #4 §3.2)

# Derived geometric dilution: V_subgraph / V_600-cell = φ^{-3}  (EW #1 §4)
GEOM_DILUTION = PHI ** (-3)   # ≈ 0.2361  — DERIVED, no free parameter

# ─────────────────────────────────────────────────────────────────────────────
# 3.  CALIBRATED η VALUES  (Open Problem EW-1)
# ─────────────────────────────────────────────────────────────────────────────
#
# After applying the geometric dilution φ^{-3}, the formula still produces
# energies ~10^18 GeV. The remaining reduction η ~ 10^{-17} bridges to the
# weak scale. η is calibrated here to reproduce PDG central values.
# A first-principles derivation of η is Open Problem EW-1.
#
# Note: η_W ≠ η_Z ≠ η_H (three distinct values), confirming Open Problem EW-2
# (no unified mass formula with a single integration range and single η).

def _compute_base_energy(n_v: int, r_eff: float, extra: float) -> float:
    """Base confinement energy (before η) in GeV."""
    fg = HYBRID_WEAK_FACTOR * (n_v / 12.0) * PHI ** (-n_v / 3.0) * extra
    return fg * SEA_STRENGTH * HBAR_C_OVER_LP * 4.0 * np.pi * r_eff * GEOM_DILUTION

_BASE_W = _compute_base_energy(12, R_EFF_WZ, 1.0)
_BASE_Z = _compute_base_energy(12, R_EFF_WZ, LOOP_DENSITY_FACTOR)
_BASE_H = _compute_base_energy(20, R_EFF_H,  SHELL_DENSITY_FACTOR)

ETA_W = 80.377  / _BASE_W    # ≈ 1.566e-17
ETA_Z = 91.1876 / _BASE_Z    # ≈ 1.481e-17
ETA_H = 125.10  / _BASE_H    # ≈ 2.932e-17

# ─────────────────────────────────────────────────────────────────────────────
# 4.  COUPLING CONSTANTS  (Open Problem EW-3)
# ─────────────────────────────────────────────────────────────────────────────
#
# g and g' are reproduced from 600-cell shell vertex ratios but require
# a calibration factor vertex_count_correction = 1.18.
# The paper quotes g ≈ 0.652, g' ≈ 0.357.
# With those values: sin²θ_W = 0.357²/(0.652²+0.357²) = 0.2307 (not 0.2312).
# A corrected g' = 0.35756 gives sin²θ_W = 0.23121 exactly.
# We use the corrected value for the Monte Carlo.

G_WEAK  = 0.652      # SU(2)_L coupling (reproduced from vertex ratios)
# g' calibrated to exactly reproduce PDG sin²θ_W = 0.23121:
_sin2_target = 0.23121
G_PRIME = np.sqrt(_sin2_target * G_WEAK**2 / (1.0 - _sin2_target))  # ≈ 0.35756

# Shell vertex counts (for coupling ratio reference)
SHELL_VERTICES = {"inner": 16, "middle": 64, "outer": 40, "total": 120}

# ─────────────────────────────────────────────────────────────────────────────
# 5.  600-CELL EIGENVALUE SPECTRUM
# ─────────────────────────────────────────────────────────────────────────────

EIGENVALUES = np.array([
    12.0,           # Z⁰  — ground state, λ=12
    1.0 + PHI,      # W   — intermediate positive pair
    PHI - 1.0,      # W   — intermediate positive pair
    0.0,            # γ   — massless DP-Sea mode
    1.0 - PHI,      # dodecahedral modes (no distinct subgraph)
    -PHI,           # dodecahedral modes (no distinct subgraph)
    -(1.0 + PHI),   # H   — most frustrated, λ=-(1+φ)
])

EIGENVALUE_ASSIGNMENT = {
    12.0:           ("Z⁰",  "ground state, most symmetric, λ=12"),
    1.0 + PHI:      ("W",   f"intermediate positive, λ=1+φ≈{1+PHI:.3f}"),
    PHI - 1.0:      ("W",   f"intermediate positive, λ=φ-1≈{PHI-1:.3f}"),
    0.0:            ("γ",   "massless DP-Sea mode, λ=0"),
    1.0 - PHI:      ("—",   f"dodecahedral mode, λ=1-φ≈{1-PHI:.3f}"),
    -PHI:           ("—",   f"dodecahedral mode, λ=-φ≈{-PHI:.3f}"),
    -(1.0 + PHI):   ("H",   f"most frustrated, λ=-(1+φ)≈{-(1+PHI):.3f}"),
}

# PDG 2026 reference
PDG = {
    "m_W":         80.377,
    "m_Z":         91.1876,
    "m_H":         125.10,
    "sin2_thetaW": 0.23121,
    "Gamma_W":     2.085,
    "Gamma_Z":     2.4952,
    "Gamma_H":     0.00407,
    "sigma_m_W":   0.012,
    "sigma_m_Z":   0.0021,
    "sigma_m_H":   0.14,
    "sigma_sin2":  0.00004,
}

# ─────────────────────────────────────────────────────────────────────────────
# 6.  CORE FORMULAS
# ─────────────────────────────────────────────────────────────────────────────

def f_geom(n_v: int, extra_factor: float = 1.0) -> float:
    """
    Dimensionless geometric confinement factor  (EW #2 eq. 5):

        f_geom = HWF × (n_v/12) × φ^{-n_v/3} × extra_factor

    NOTE: for n_v=20 this gives 0.1415, NOT 0.0635 as stated in the
    published v3 paper. The paper has an error: it uses
    φ^{-20/3} ≈ 0.01814, but the correct value is 0.04043.
    The masses are still reproduced because η_H absorbs the difference.
    """
    return HYBRID_WEAK_FACTOR * (n_v / 12.0) * PHI**(-n_v / 3.0) * extra_factor


def confinement_energy(n_v: int, r_eff: float,
                       extra_factor: float, eta: float) -> float:
    """
    SS-Vector compression energy in GeV (EW #2 eq. 4,6):

        E_conf = f_geom × sea_strength × (ℏc/l_P³) × 4π × r_eff
                 × φ^{-3} × η

    The integral ∫ (1/r²)·4πr² dr = 4π·r_eff (l_P units).
    φ^{-3} is the derived geometric dilution component.
    η is the calibrated Planck-to-weak reduction (Open Problem EW-1).
    """
    fg = f_geom(n_v, extra_factor)
    return fg * SEA_STRENGTH * HBAR_C_OVER_LP * 4*np.pi * r_eff * GEOM_DILUTION * eta


def sin2_weinberg(g: float = G_WEAK, g_prime: float = G_PRIME) -> float:
    """
    Weinberg angle from coupling ratio (EW #5 Theorem 4):

        sin²θ_W = g'^2 / (g² + g'^2)

    The four-layer phase interference weights p_k = (1 - k/5)² cancel
    when g_k = g and g'_k = g' are constant across layers, reducing to
    the standard coupling-ratio formula.
    """
    return g_prime**2 / (g**2 + g_prime**2)


def phase_weights(n_layers: int = 4) -> np.ndarray:
    """p_k = (1 - k/5)² for k=1..4  (EW #1 eq. 2)."""
    k = np.arange(1, n_layers + 1, dtype=float)
    return (1.0 - k / 5.0) ** 2

# ─────────────────────────────────────────────────────────────────────────────
# 7.  MONTE CARLO SIMULATIONS
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class MCResult:
    name:    str
    mean:    float
    std:     float
    n:       int
    pdg:     float
    pdg_sig: float
    unit:    str = ""

    @property
    def agree_pct(self) -> float:
        return 100.0 * abs(self.mean - self.pdg) / self.pdg

    @property
    def n_sigma_from_pdg_central(self) -> float:
        """Deviation of CPP mean from PDG mean, in CPP σ units."""
        return abs(self.mean - self.pdg) / self.std if self.std > 0 else 0.0

    def __str__(self) -> str:
        return (
            f"{self.name:20s}: {self.mean:.5f} ± {self.std:.5f} {self.unit}"
            f"   PDG = {self.pdg:.5f}"
            f"   Δ = {self.agree_pct:.4f}%"
        )


def mc_weinberg(n: int = 1_000_000, seed: int = 42) -> MCResult:
    """
    Monte Carlo for sin²θ_W.

    g and g' are drawn from Gaussians with ±1% lattice fluctuations.
    The formula sin²θ_W = g'^2 / (g² + g'^2) is applied per event.
    """
    rng = np.random.default_rng(seed)
    g_s  = rng.normal(G_WEAK,  G_WEAK  * 0.01, n)
    gp_s = rng.normal(G_PRIME, G_PRIME * 0.01, n)
    sin2 = gp_s**2 / (g_s**2 + gp_s**2)
    return MCResult("sin²θ_W", float(np.mean(sin2)), float(np.std(sin2)),
                    n, PDG["sin2_thetaW"], PDG["sigma_sin2"])


def mc_mass(name: str, n_v: int, r_eff: float, extra: float, eta: float,
            pdg_mass: float, pdg_sig: float,
            n: int = 1_000_000, seed: int = 42) -> MCResult:
    """
    Monte Carlo for a boson mass.

    Uncertainty sources:
      • sea_strength  ±5%   (dominant physical uncertainty)
      • n_v           ±0.5  (ensemble variance around central value)
      • r_eff         ±2%   (lattice discreteness)
    """
    rng = np.random.default_rng(seed)
    ss_s = rng.normal(SEA_STRENGTH, SEA_STRENGTH * 0.05, n)
    nv_s = np.clip(rng.normal(n_v, 0.5, n), n_v - 1.5, n_v + 1.5)
    r_s  = rng.normal(r_eff, r_eff * 0.02, n)

    fg   = HYBRID_WEAK_FACTOR * (nv_s / 12.0) * PHI**(-nv_s / 3.0) * extra
    mass = fg * ss_s * HBAR_C_OVER_LP * 4*np.pi * r_s * GEOM_DILUTION * eta
    return MCResult(name, float(np.mean(mass)), float(np.std(mass)),
                    n, pdg_mass, pdg_sig, "GeV")


def run_all(n: int = 1_000_000) -> Dict[str, MCResult]:
    """Run all four Monte Carlo simulations."""
    print(f"Running Monte Carlo  (n = {n:,} events each) ...")
    results = {}
    for label, func, kw in [
        ("sin2_thetaW", mc_weinberg,
         {"n": n, "seed": 42}),
        ("m_W", mc_mass,
         {"name":"m_W","n_v":12,"r_eff":R_EFF_WZ,"extra":1.0,"eta":ETA_W,
          "pdg_mass":PDG["m_W"],"pdg_sig":PDG["sigma_m_W"],"n":n,"seed":43}),
        ("m_Z", mc_mass,
         {"name":"m_Z","n_v":12,"r_eff":R_EFF_WZ,"extra":LOOP_DENSITY_FACTOR,
          "eta":ETA_Z,"pdg_mass":PDG["m_Z"],"pdg_sig":PDG["sigma_m_Z"],"n":n,"seed":44}),
        ("m_H", mc_mass,
         {"name":"m_H","n_v":20,"r_eff":R_EFF_H,"extra":SHELL_DENSITY_FACTOR,
          "eta":ETA_H,"pdg_mass":PDG["m_H"],"pdg_sig":PDG["sigma_m_H"],"n":n,"seed":45}),
    ]:
        print(f"  {label:15s} ...", end="", flush=True)
        results[label] = func(**kw)
        print(" done")
    return results

# ─────────────────────────────────────────────────────────────────────────────
# 8.  ANALYSIS FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def print_eigenvalue_table() -> None:
    print("\n── 600-cell eigenvalue → boson assignment (EW #1 Table 1) ──")
    print(f"  {'λ':>8}  {'Boson':6}  Description")
    print(f"  {'─'*8}  {'─'*6}  {'─'*45}")
    for lam, (boson, desc) in sorted(
            EIGENVALUE_ASSIGNMENT.items(), key=lambda x: -x[0]):
        print(f"  {lam:+8.3f}  {boson:6}  {desc}")


def print_geometric_factors() -> None:
    print("\n── Geometric factors f_geom ──")
    rows = [
        ("W  bracelet  n_v=12", 12, 1.0,                 "0.2188"),
        ("Z  ico-loop  n_v=12", 12, LOOP_DENSITY_FACTOR,  "0.2626"),
        ("H  dodecahed n_v=20", 20, SHELL_DENSITY_FACTOR, "0.0635 ← PAPER ERROR"),
    ]
    for label, nv, ex, paper_val in rows:
        fg = f_geom(nv, ex)
        flag = " ✓" if abs(fg - float(paper_val.split()[0])) < 0.001 else \
               f" ← code={fg:.4f}, paper={paper_val}"
        print(f"  f_geom({label}) = {fg:.4f}   paper: {paper_val}{flag}")
    print()
    print("  NOTE: For n_v=20, φ^{-20/3} = 0.04043 (not 0.01814 as stated in EW #4).")
    print("  This factor-of-2.23 error in the intermediate step is absorbed into η_H.")
    print("  The published masses are still correct; the derivation chain is not.")


def print_calibration() -> None:
    print("\n── Calibrated η values (Open Problem EW-1) ──")
    print(f"  η_W = {ETA_W:.4e}   (base_W = {_BASE_W:.4e} GeV)")
    print(f"  η_Z = {ETA_Z:.4e}   (base_Z = {_BASE_Z:.4e} GeV)")
    print(f"  η_H = {ETA_H:.4e}   (base_H = {_BASE_H:.4e} GeV)")
    print()
    print("  η_W ≠ η_Z ≠ η_H → confirms Open Problem EW-2 (no unified mass formula).")
    print(f"  Geometric component φ^{{-3}} = {GEOM_DILUTION:.6f}  (derived ✓)")
    print(f"  Remaining Planck-to-weak factor: ~{ETA_W:.1e}  (open ✗)")


def print_sensitivity() -> None:
    print("\n── True parameter sensitivity of m_W ──")
    m0 = _BASE_W * ETA_W
    rows = [
        ("sea_strength ±5%",  0.05 * m0),
        ("n_v ±1",            abs(m0 * (1/12.0 - np.log(PHI)/3.0))),
        ("r_eff ±2%",         0.02 * m0),
    ]
    for label, delta in rows:
        print(f"  {label:20s}: δm_W = ±{delta:.4f} GeV")
    print()
    print("  Published v3 paper values (±0.010, ±0.008, ±0.004 GeV) are")
    print("  chosen to sum in quadrature to the PDG uncertainty (±0.012 GeV),")
    print("  not computed from the formula. This is part of the calibration issue.")


def crosscheck(results: Dict[str, MCResult]) -> None:
    sin2 = results["sin2_thetaW"].mean
    cos_w = np.sqrt(1.0 - sin2)
    ratio_w = 1.0 / cos_w
    mZ  = results["m_Z"].mean
    mW  = results["m_W"].mean
    ratio_d = mZ / mW
    disc = 100.0 * abs(ratio_w - ratio_d) / ratio_d

    print("\n── Self-consistency: Weinberg angle ↔ m_Z/m_W  (EW #3 §4) ──")
    print(f"  sin²θ_W (MC)          = {sin2:.6f}")
    print(f"  cos θ_W               = {cos_w:.6f}")
    print(f"  m_Z/m_W from Weinberg = 1/cos θ_W = {ratio_w:.6f}")
    print(f"  m_Z/m_W from masses   = {mZ:.4f}/{mW:.4f} = {ratio_d:.6f}")
    print(f"  Discrepancy           = {disc:.3f}%")
    status = "✓  PASS (< 1%)" if disc < 1.0 else "✗  FAIL"
    print(f"  Status                = {status}")
    print(f"  (Paper reports 0.5%; this code gets {disc:.1f}%")
    print(f"   because the g'/g ratio is calibrated to the Weinberg angle,")
    print(f"   while η_Z and η_W are calibrated to the masses separately.)")


def print_summary(results: Dict[str, MCResult]) -> None:
    print("\n" + "═"*68)
    print("  CPP Electroweak Monte Carlo — Results")
    print("═"*68)
    print(f"\n  φ       = {PHI:.8f}")
    print(f"  φ^{{-3}} = {GEOM_DILUTION:.8f}  (derived)")
    print(f"  η_W     = {ETA_W:.4e}  (calibrated)")
    print()
    print(f"  {'Observable':20s}  {'CPP mean':>12}  {'CPP σ':>10}  "
          f"{'PDG':>10}  {'Δ (%)':>8}")
    print(f"  {'─'*20}  {'─'*12}  {'─'*10}  {'─'*10}  {'─'*8}")
    for r in results.values():
        print(f"  {r.name:20s}  {r.mean:12.5f}  "
              f"{r.std:10.5f}  {r.pdg:10.5f}  {r.agree_pct:8.4f}%")
    crosscheck(results)


def print_open_problems() -> None:
    print("\n── Open Problems (from EW Series v3) ──")
    problems = [
        ("OP-EW-1", "Derive η (Planck-to-weak reduction ~10^{-17}) from\n"
                    "           first principles (cosmic-horizon GP lattice)."),
        ("OP-EW-2", "Single unified mass formula: one r_eff, one η reproducing\n"
                    "           m_W, m_Z, m_H simultaneously."),
        ("OP-EW-3", "Derive g and g' purely from vertex counts {16,64,40}\n"
                    "           and golden-ratio factors (eliminate vertex_count_correction=1.18)."),
        ("OP-EW-4", "Express m_Z/m_W=1.134 and m_H/m_Z=1.372 as closed\n"
                    "           functions of the six 600-cell eigenvalues."),
        ("OP-EW-5", "Derive loop density factor ℓ_Z: reduction 1.437→1.2\n"
                    "           from 4D stereographic projection analytically."),
        ("OP-EW-6", "Derive shell density factor s_H: same for dodecahedral case."),
    ]
    for pid, desc in problems:
        print(f"  {pid}: {desc}")

# ─────────────────────────────────────────────────────────────────────────────
# 9.  MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("CPP Electroweak Monte Carlo Verification")
    print("=========================================")
    print("github.com/CPP/series_electroweak\n")

    print_eigenvalue_table()
    print_geometric_factors()
    print_calibration()
    print_sensitivity()

    results = run_all(n_events := 1_000_000)

    print_summary(results)
    print_open_problems()
    print()
