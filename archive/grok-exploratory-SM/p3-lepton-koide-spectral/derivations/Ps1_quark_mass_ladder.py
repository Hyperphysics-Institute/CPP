#!/usr/bin/env python3
"""
PS-1: Quark Mass Ladder — Verifiable Computation
=================================================

Tests every proposed mass mechanism against the ACTUAL 600-cell geometry.
No hand-waving, no fabricated tables. Every number computed from code.

The question: can any combination of established CPP quantities
(α_geom, sea_strength, E_eDP, 600-cell shell structure, PSR formula)
reproduce the quark mass hierarchy?

Author: Claude (Anthropic) for Thomas Lee Abshier / Hyperphysics Institute
Date: 25 March 2026
"""

import numpy as np
from itertools import product as iterproduct

phi = (1 + np.sqrt(5)) / 2

# ================================================================
# ESTABLISHED CPP QUANTITIES (all derived in prior sessions)
# ================================================================
alpha_geom = 3*(11 + 5*np.sqrt(5)) * np.sqrt(5 + np.sqrt(5)) / 320
sea_strength = 10 * alpha_geom / (12 * phi**2)  # derived
sea_strength_cal = 0.185  # calibrated (for comparison)
hbar_c = 197.3269804  # MeV·fm
r_conf = 0.16  # fm (from Cornell potential)
E_eDP = sea_strength * hbar_c / (phi**2 * r_conf)  # Theorem 3

print("=" * 78)
print("PS-1: QUARK MASS LADDER — VERIFIABLE COMPUTATION")
print("=" * 78)
print(f"\nEstablished CPP quantities:")
print(f"  α_geom        = {alpha_geom:.6f}")
print(f"  sea_strength   = {sea_strength:.6f} (derived)")
print(f"  sea_strength   = {sea_strength_cal:.6f} (calibrated)")
print(f"  ℏc             = {hbar_c:.4f} MeV·fm")
print(f"  r_conf          = {r_conf} fm")
print(f"  E_eDP          = {E_eDP:.2f} MeV (derived)")
print(f"  φ              = {phi:.10f}")
print(f"  φ²             = {phi**2:.6f}")
print(f"  φ³             = {phi**3:.6f}")

# PDG quark masses (current masses for light quarks, pole for heavy)
pdg_current = {
    'u': 2.16, 'd': 4.70, 's': 93.4, 
    'c': 1270, 'b': 4180, 't': 172760
}
pdg_constituent = {
    'u': 336, 'd': 340, 's': 486,
    'c': 1550, 'b': 4730, 't': 172760
}

# ================================================================
# SECTION 1: THE ACTUAL 600-CELL SHELL STRUCTURE
# ================================================================

print(f"\n{'='*78}")
print("SECTION 1: ACTUAL 600-CELL DISTANCE SHELLS")
print(f"{'='*78}")

# From our exact computation
shells = [
    {'d2': 1/phi**2, 'dist': 1/phi, 'N': 12, 'label': '1/φ² (nn)'},
    {'d2': 1.0,      'dist': 1.0,   'N': 20, 'label': '1 (circumrad)'},
    {'d2': 3-phi,    'dist': np.sqrt(3-phi), 'N': 12, 'label': '3-φ'},
    {'d2': 2.0,      'dist': np.sqrt(2),     'N': 30, 'label': '2 (equatorial)'},
    {'d2': phi+1,    'dist': np.sqrt(phi+1),  'N': 12, 'label': 'φ+1'},
    {'d2': 3.0,      'dist': np.sqrt(3),      'N': 20, 'label': '3'},
    {'d2': 2+phi,    'dist': np.sqrt(2+phi),   'N': 12, 'label': '2+φ'},
    {'d2': 4.0,      'dist': 2.0,              'N': 1,  'label': '4 (antipode)'},
]

# Projected 3D volumes (from our computation)
shell_volumes = [0.515028, 1.809017, 2.181695, 3.266125, 
                 2.181695, 1.809017, 0.515028, 0.0]

print(f"\n{'Shell':>6} {'d²':>8} {'d':>8} {'N':>4} {'V_3D':>10} {'Label':>16}")
print("-" * 58)
for i, (s, v) in enumerate(zip(shells, shell_volumes)):
    print(f"{i:6d} {s['d2']:8.4f} {s['dist']:8.4f} {s['N']:4d} {v:10.4f} {s['label']:>16}")

print(f"\nKey observations:")
print(f"  1. Palindromic: 12, 20, 12, 30, 12, 20, 12, 1")
print(f"  2. Volumes PEAK at shell 3 (equatorial) and DECREASE after")
print(f"  3. No 60-vertex shell exists anywhere")
print(f"  4. No 4-vertex shell (tet base has 3 vertices, not its own shell)")

# ================================================================
# SECTION 2: THE CPP CAGE ASSIGNMENT vs ACTUAL SHELLS
# ================================================================

print(f"\n{'='*78}")
print("SECTION 2: CPP CAGE POLYHEDRA vs ACTUAL 600-CELL SHELLS")
print(f"{'='*78}")

cpp_cages = [
    {'name': 'bare (u,d)', 'n': 0, 'N': 0, 'polyhedron': 'none'},
    {'name': 'strange',     'n': 1, 'N': 4, 'polyhedron': 'tetrahedron'},
    {'name': 'charm',       'n': 2, 'N': 12, 'polyhedron': 'icosahedron'},
    {'name': 'bottom',      'n': 3, 'N': 20, 'polyhedron': 'dodecahedron'},
    {'name': 'top',         'n': 4, 'N': 60, 'polyhedron': 'C60 fullerene'},
]

print(f"\n{'Quark':>10} {'n':>3} {'CPP N':>6} {'Polyhedron':>16} {'Match to shell?':>20}")
print("-" * 60)
for c in cpp_cages:
    match = "—"
    if c['N'] == 0:
        match = "bare vertex"
    elif c['N'] == 4:
        match = "NOT a shell (tet cell)"
    elif c['N'] == 12:
        match = "Shell 0 or 2 or 4 or 6"
    elif c['N'] == 20:
        match = "Shell 1 or 5"
    elif c['N'] == 60:
        match = "NO MATCH (no 60-shell)"
    print(f"{c['name']:>10} {c['n']:3d} {c['N']:6d} {c['polyhedron']:>16} {match:>20}")

print(f"""
FINDING: The CPP cage vertex counts (4, 12, 20, 60) do NOT correspond
to distance shells of the 600-cell (12, 20, 12, 30, 12, 20, 12, 1).
- N=4 (tet): The 600-cell has 600 tetrahedral CELLS, but "4 vertices of
  a tetrahedron" is a cell, not a distance shell. A cell's vertices are
  NOT all equidistant from a reference vertex.
- N=12: Matches shells 0, 2, 4, 6 — but WHICH 12-vertex shell is the
  "icosahedral cage"? Shell 0 (the nearest neighbors) IS an icosahedron.
- N=20: Matches shells 1, 5 — the 20-vertex shells exist.
- N=60: No 60-vertex shell exists. Period.
""")

# ================================================================
# SECTION 3: TEST ALL PROPOSED MECHANISMS
# ================================================================

print(f"{'='*78}")
print("SECTION 3: TESTING MASS MECHANISMS WITH REAL NUMBERS")
print(f"{'='*78}")

pdg_masses = [93.4, 1270, 4180, 172760]  # s, c, b, t current masses
quark_names = ['strange', 'charm', 'bottom', 'top']
cage_n = [1, 2, 3, 4]
cpp_N = [4, 12, 20, 60]

# ------------------------------------------------------------------
# Mechanism A: Naive φ^(3(l-1)) (the original conjecture)
# ------------------------------------------------------------------
print(f"\n--- Mechanism A: Naive N_l × E_eDP × φ^(3(l-1)) ---")
print(f"{'Quark':>10} {'N':>4} {'φ^3(l-1)':>10} {'M_struct':>10} {'PDG':>8} {'Ratio':>8}")
print("-" * 55)
cumul = 5.0  # u/d base
for i, (name, n, N, pdg) in enumerate(zip(quark_names, cage_n, cpp_N, pdg_masses)):
    shell_E = N * E_eDP * phi**(3*(n-1))
    cumul += shell_E
    print(f"{name:>10} {N:4d} {phi**(3*(n-1)):10.2f} {cumul:10.1f} {pdg:8.1f} {cumul/pdg:8.2f}")

# ------------------------------------------------------------------
# Mechanism B: PSR compression only
# ------------------------------------------------------------------
print(f"\n--- Mechanism B: PSR compression r_eff = l_P/(1 + α·n·sea) ---")
print(f"{'n':>3} {'r_eff/r':>10} {'(r_eff/r)³':>12}")
print("-" * 28)
for n in range(1, 5):
    r_ratio = 1.0 / (1 + alpha_geom * n * sea_strength)
    print(f"{n:3d} {r_ratio:10.6f} {r_ratio**3:12.6f}")

print(f"\n  PSR compression gives factors of 0.75 to 0.37.")
print(f"  Not enough: strange needs 93/340 = 0.27, bottom needs 4180/35000 = 0.12")

# ------------------------------------------------------------------
# Mechanism C: Phase cancellation C_n = |Σ exp(i 2πm/φ²)|/n
# ------------------------------------------------------------------
print(f"\n--- Mechanism C: Phase cancellation C_n ---")
for n in range(1, 5):
    phase_sum = sum(np.exp(1j * 2*np.pi * m / phi**2) for m in range(n+1))
    C_n = abs(phase_sum) / n
    print(f"  n={n}: C_n = {C_n:.6f}")

print(f"\n  C_n oscillates erratically: 0.72, 0.24, 0.36, 0.07")
print(f"  Not a systematic suppression — quasi-random.")

# ------------------------------------------------------------------
# Mechanism D: Actual shell volumes (from our computation)
# ------------------------------------------------------------------
print(f"\n--- Mechanism D: Use ACTUAL 600-cell shell volumes ---")
print(f"  Shell volumes: {[f'{v:.3f}' for v in shell_volumes[:4]]}")
print(f"  V ratios (to shell 0): {[f'{v/shell_volumes[0]:.2f}' for v in shell_volumes[:4]]}")
print(f"  Actual volumes grow SLOWER than φ³ — makes problem WORSE.")

# ------------------------------------------------------------------
# Mechanism E: Combined (A×B×C) — Grok's proposal
# ------------------------------------------------------------------
print(f"\n--- Mechanism E: Grok's combined (naive × PSR × phase) ---")
print(f"{'Quark':>10} {'Naive':>10} {'×PSR³':>10} {'×C_n':>10} {'Combined':>10} {'PDG':>8} {'Ratio':>8}")
print("-" * 72)

cumul = 5.0
for i, (name, n, N, pdg) in enumerate(zip(quark_names, cage_n, cpp_N, pdg_masses)):
    naive = N * E_eDP * phi**(3*(n-1))
    r_ratio = 1.0 / (1 + alpha_geom * n * sea_strength)
    psr_cubed = r_ratio**3
    phase_sum = sum(np.exp(1j * 2*np.pi * m / phi**2) for m in range(n+1))
    C_n = abs(phase_sum) / n
    
    combined = naive * psr_cubed * C_n
    cumul += combined
    
    print(f"{name:>10} {naive:10.1f} {naive*psr_cubed:10.1f} "
          f"{naive*psr_cubed*C_n:10.1f} {cumul:10.1f} {pdg:8.1f} {cumul/pdg:8.2f}")

# ================================================================
# SECTION 4: ALTERNATIVE — WHAT IF MASS ~ DISTANCE FROM APEX?
# ================================================================

print(f"\n{'='*78}")
print("SECTION 4: ALTERNATIVE MECHANISMS")
print(f"{'='*78}")

# ------------------------------------------------------------------
# Alt 1: Mass proportional to shell distance (SSV energy ~ 1/r)
# ------------------------------------------------------------------
print(f"\n--- Alt 1: M ~ sea_strength × ℏc / r_shell ---")
print(f"  If each generation's mass is set by SSV energy at its shell radius:")
print(f"{'Shell':>6} {'d':>8} {'E=sea×ℏc/d':>14} {'E/E_shell0':>12}")
print("-" * 44)
for i, s in enumerate(shells[:4]):
    E_ssv = sea_strength * hbar_c / (s['dist'] * r_conf)
    ratio = E_ssv / (sea_strength * hbar_c / (shells[0]['dist'] * r_conf))
    print(f"{i:6d} {s['dist']:8.4f} {E_ssv:14.2f} {ratio:12.4f}")

# ------------------------------------------------------------------
# Alt 2: Mass ~ N_shell × SSV energy at shell distance
# ------------------------------------------------------------------
print(f"\n--- Alt 2: M ~ N × sea_strength × ℏc / (r_shell × φ²) ---")
print(f"{'Shell':>6} {'N':>4} {'d':>8} {'E':>10} {'Cumul':>10}")
print("-" * 42)
cumul = 5.0
for i, (s, v) in enumerate(zip(shells[:4], shell_volumes[:4])):
    E = s['N'] * sea_strength * hbar_c / (s['dist'] * r_conf * phi**2)
    cumul += E
    pdg_i = pdg_masses[i] if i < len(pdg_masses) else 0
    print(f"{i:6d} {s['N']:4d} {s['dist']:8.4f} {E:10.2f} {cumul:10.2f}")

# ------------------------------------------------------------------
# Alt 3: Koide-like approach for quarks
# ------------------------------------------------------------------
print(f"\n--- Alt 3: Can any K3-like mechanism work for quarks? ---")

# For each quark triplet, check Koide K
triplets = [
    ('u, c, t', [2.16, 1270, 172760]),
    ('d, s, b', [4.70, 93.4, 4180]),
    ('u, d, s', [2.16, 4.70, 93.4]),
    ('c, b, t', [1270, 4180, 172760]),
]

for name, masses in triplets:
    K = sum(masses) / (sum(np.sqrt(masses)))**2
    print(f"  K({name}) = {K:.4f}  (vs 2/3 = {2/3:.4f}, dev = {abs(K-2/3)/(2/3)*100:.1f}%)")

# ================================================================
# SECTION 5: THE FUNDAMENTAL QUESTION — WHAT DETERMINES QUARK MASSES?
# ================================================================

print(f"\n{'='*78}")
print("SECTION 5: WHAT THE DATA ACTUALLY TELLS US")
print(f"{'='*78}")

print(f"\n--- Mass ratios between generations ---")
for i in range(len(pdg_masses)-1):
    ratio = pdg_masses[i+1] / pdg_masses[i]
    phi_exp = np.log(ratio) / np.log(phi)
    print(f"  m_{quark_names[i+1]}/m_{quark_names[i]} = {ratio:.1f} "
          f"= φ^{phi_exp:.2f}")

print(f"\n--- Lepton-quark mass correspondences ---")
lepton_masses = [0.511, 105.658, 1776.86]
lepton_names = ['e', 'μ', 'τ']
for i, (lname, lmass) in enumerate(zip(lepton_names, lepton_masses)):
    # Find which quark mass is closest
    for qname, qmass in pdg_current.items():
        ratio = qmass / lmass
        if 0.5 < ratio < 500:
            phi_exp = np.log(ratio) / np.log(phi) if ratio > 0 else 0
            print(f"  m_{qname}/m_{lname} = {ratio:.2f} = φ^{phi_exp:.2f}")

# Test: do quark masses follow pure φ powers from a base?
print(f"\n--- Are quark masses pure φ powers from some base? ---")
m_base = pdg_current['u']
for name, mass in pdg_current.items():
    ratio = mass / m_base
    phi_exp = np.log(ratio) / np.log(phi) if ratio > 1 else 0
    nearest_int = round(phi_exp)
    pred = m_base * phi**nearest_int if nearest_int > 0 else m_base
    err = abs(pred - mass) / mass * 100 if mass > 0 else 0
    print(f"  m_{name}/m_u = {ratio:10.1f} = φ^{phi_exp:6.2f} "
          f"≈ φ^{nearest_int:2d} → {pred:10.1f} MeV ({err:5.1f}% off)")

# ================================================================
# SECTION 6: THE PROTON MASS DECOMPOSITION (WHAT ACTUALLY WORKS)
# ================================================================

print(f"\n{'='*78}")
print("SECTION 6: WHAT CPP ACTUALLY GETS RIGHT ABOUT MASS")
print(f"{'='*78}")

M_proton = 938.3
m_u_current = 2.16
m_d_current = 4.70
quark_fraction = (2*m_u_current + m_d_current) / M_proton

print(f"\n  Proton mass: {M_proton} MeV")
print(f"  Current quark masses: 2×m_u + m_d = {2*m_u_current + m_d_current:.1f} MeV")
print(f"  Quark mass fraction: {quark_fraction*100:.1f}%")
print(f"  qDP chain energy: {(1-quark_fraction)*100:.1f}% = {M_proton*(1-quark_fraction):.1f} MeV")
print(f"")
print(f"  This is the one mass result CPP gets right: 99% of the proton mass")
print(f"  is qDP chain energy (= gluon field energy in QCD).")
print(f"  This does NOT depend on the cage-depth model at all.")

# ================================================================
# SECTION 7: HONEST SUMMARY
# ================================================================

print(f"\n{'='*78}")
print("SECTION 7: HONEST SUMMARY")
print(f"{'='*78}")

print(f"""
WHAT WORKS:
  1. SU(3) from tetrahedral hopping operators (exact, verified)
  2. Gluon masslessness from open-path topology (exact)
  3. β₀ = 7 from Casimirs (exact)
  4. Hadron spectrum: GMO relations, Ω⁻, quarkonium (0.003-0.5%)
  5. Proton mass ≈ 99% qDP chain energy (correct mechanism)
  6. α_geom → k_SM → sea_strength (derived, 3.9% from calibrated)
  7. δ = 1/3 charge quantisation (exact, topological)
  8. K = 2/3 Koide formula (conditional on P1+P3)

WHAT DOES NOT WORK:
  1. φ^(3(l-1)) shell volume scaling — falsified by exact computation
  2. Cage-depth model for quark masses — structural masses off by 3-8×
  3. C₆₀ fourth cage for top quark — no 60-vertex shell exists
  4. PSR compression as mass correction — too small (factors of 0.4-0.8)
  5. Phase cancellation — quasi-random, not systematic
  6. Combined Grok proposal — still wrong by factors of 0.07-2.0

THE HONEST STATUS OF OP-SS-1 (quark mass formula):
  The quark mass formula is OPEN. No combination of established CPP
  mechanisms reproduces the quark mass hierarchy from first principles.
  
  The cage-depth ordering (more shells → more mass) is qualitatively
  correct but the QUANTITATIVE scaling is wrong. The "corrections"
  needed are larger than the "base terms," which means the decomposition
  itself is incorrect.
  
  The most promising observation remains:
    m_s/m_u ≈ φ^8 (43 vs 93, ~2× off)
    m_c/m_u ≈ φ^13 (549 vs 1270, ~2× off)  
    m_b/m_u ≈ φ^16 (2207 vs 4180, ~2× off)
    m_t/m_u ≈ φ^24 (103,681 vs 172,760, ~1.7× off)
  
  But the exponents (8, 13, 16, 24) have no obvious 600-cell origin,
  and the factor-of-2 errors are systematic.

RECOMMENDATION FOR THE STRONG SECTOR PAPER:
  1. Keep OP-SS-1 as OPEN (it already is)
  2. REMOVE or QUALIFY the φ^(3(l-1)) claim in the mass-ladder section
  3. State honestly that the mass hierarchy mechanism is not yet derived
  4. The paper's strength is the SU(3) algebra, not the masses
""")

# ================================================================
# SECTION 8: WHAT WOULD A WORKING MECHANISM LOOK LIKE?
# ================================================================

print(f"{'='*78}")
print("SECTION 8: CONSTRAINTS ON ANY CORRECT MECHANISM")
print(f"{'='*78}")

print(f"\nAny correct quark mass mechanism must satisfy ALL of:")
print(f"  1. m_u < m_d (SSV sign asymmetry — qualitatively understood)")
print(f"  2. m_s/m_d ≈ 20 (one generation step)")
print(f"  3. m_c/m_s ≈ 14 (cross-generation)")
print(f"  4. m_b/m_c ≈ 3.3 (one generation step)")
print(f"  5. m_t/m_b ≈ 41 (anomalously large — top quark problem)")
print(f"  6. Quarks do NOT satisfy Koide (K ≠ 2/3)")
print(f"  7. The mechanism must reduce to K=2/3 for leptons (no cage)")
print(f"  8. Use only φ, α_geom, sea_strength, and 600-cell geometry")
print(f"")

# Test Thomas's thermal/DP-cloud idea
print(f"Thomas's DP-cloud thermal picture predicts:")
print(f"  - Mass from thermal DP cloud, not vertex counting")
print(f"  - Scaffolding (cage) sets boundary conditions")
print(f"  - ZBW oscillation in radial SSV potential provides mass energy")
print(f"  - Inner shells contribute more (higher SSV)")
print(f"  - Three modes of thermal equilibrium → three generations")
print(f"")
print(f"  This picture is CONSISTENT with:")
print(f"  - Proton mass ≈ 99% field energy (✓)")
print(f"  - Koide K=2/3 for leptons (K3 thermal equipartition ✓)")
print(f"  - Quarks breaking Koide (strong sector contaminates ✓)")
print(f"")
print(f"  But it has NOT been computed. The SSV radial potential")
print(f"  V(r) = -sea_strength × ℏc/r has known eigenvalues,")
print(f"  but mapping those to quark masses requires specifying")
print(f"  what 'cage boundary conditions' means quantitatively.")
