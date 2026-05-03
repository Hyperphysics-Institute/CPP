"""
SS-9 OPEN-SS-35 sub-question (b) B-alpha layer 3:
Cluster-surface Thomas-form spin-orbit (Path (i) Phase 1, Session 11).

Phase 1 of the multi-session arc identified in Session 10 as Priority 1:
test whether the K_3 Gaussian-modulated mean field's spherically-averaged
Thomas-form weight f_SO(r) = (1/r) * dV_avg/dr produces enhanced V_SO_eff
for high-l surface-localized states (in the way Bohr-Mottelson Woods-Saxon
does empirically).

RESULT: Path (i) RULED OUT. The K_3 cluster shell at A=56 (sigma/R = 0.75)
has a FUZZY surface, not a sharp Woods-Saxon-style surface. Consequently
f_SO(r) peaks at the cluster CENTER (not the surface) and decreases
monotonically outward. Matrix elements <f_SO>_{0,l} decrease from
7.41 MeV/fm^2 at l=0 to 2.14 MeV/fm^2 at l=6 (factor 3.5x reduction).

V_SO_eff(l=6) = 0.338 MeV — only 29% of central baseline 1.17 MeV,
13% of empirical strong-magic threshold. Fourth programme-level negative-
result demonstration in OPEN-SS-35 closure programme.

Structural diagnosis: the geometric deficiency is shape-level (Gaussian
fuzzy surface vs Woods-Saxon sharp surface), not perturbation-level.
Cannot be fixed by parameter adjustment within the K_3 Gaussian +
HO + L.S framework. Magic-strength gap closure requires additional
CPP physics beyond the smooth K_3 Gaussian-modulated mean field.

Companion sketch:
  series_strong/papers/SS-9/sketches/
  SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3_cluster_surface_phase1.md
"""

import numpy as np
from scipy import integrate, special


# ---------------------------------------------------------------------------
# Constants and CPP-derived inputs
# ---------------------------------------------------------------------------
hbar_c = 197.327                # MeV*fm
m_n_c2 = 939.565                # MeV
hbar_omega = 13.0               # MeV at A~56 (sub-question (a))
sigma = hbar_c / np.sqrt(m_n_c2 * hbar_omega)  # 1.7855 fm

# Cluster geometry at A~56 (deltahedron-core configuration)
N_alpha = 14
R_cluster = 2.37                # fm — alpha-vertex radius (proxy from A=48 ico)
deg_avg = 5                     # average vertex degree
B_pair = 2.342                  # MeV (M_0/phi)
V0_per_alpha = B_pair * deg_avg # 11.71 MeV

# Calibration anchor: Session 8 layer 1 baseline
V_SO_central = 1.17             # MeV ((v_F/c)^2 * hbar*omega = 0.09 * 13)


# ---------------------------------------------------------------------------
# Spherically-averaged K_3 shell potential
# ---------------------------------------------------------------------------
def V_avg(r):
    """V_avg(r) for shell of N_alpha Gaussians at radius R, each depth V0,
    width sigma. Standard derivation via shell average of exp(-|r-R'|^2/2sigma^2).
    """
    if abs(r) < 1e-8:
        return -N_alpha * V0_per_alpha * np.exp(-R_cluster**2 / (2 * sigma**2))
    factor = -(N_alpha * V0_per_alpha * sigma**2) / (2 * r * R_cluster)
    g_minus = np.exp(-(r - R_cluster)**2 / (2 * sigma**2))
    g_plus  = np.exp(-(r + R_cluster)**2 / (2 * sigma**2))
    return factor * (g_minus - g_plus)


def dV_dr(r, h=1e-4):
    """Numerical derivative of V_avg."""
    return (V_avg(r + h) - V_avg(r - h)) / (2 * h)


def f_SO(r):
    """Thomas-form weight (1/r) * dV_avg/dr.
    
    Limit at r=0: (1/r)*dV/dr -> V''(0) (finite by L'Hopital, since V'(0)=0
    by symmetry).
    """
    if r < 1e-4:
        h = 1e-3
        return (V_avg(h) + V_avg(-h) - 2*V_avg(0)) / h**2
    return dV_dr(r) / r


# ---------------------------------------------------------------------------
# HO ground-state-of-l radial wavefunction
# ---------------------------------------------------------------------------
def R_0l(r, l, a=sigma):
    """Normalized HO radial wavefunction R_{n=0, l}(r) with width a.
    Normalization: integral |R|^2 r^2 dr = 1.
    """
    norm_sq = 2 / (a**3 * special.gamma(l + 1.5))
    return np.sqrt(norm_sq) * (r / a)**l * np.exp(-r**2 / (2 * a**2))


# ---------------------------------------------------------------------------
# Matrix element computation
# ---------------------------------------------------------------------------
def matrix_element_fSO_0l(l, a=sigma, r_max=25):
    """<0, l | f_SO(r) | 0, l> = integral |R_{0,l}|^2 * f_SO(r) * r^2 dr."""
    integrand = lambda r: R_0l(r, l, a)**2 * f_SO(r) * r**2
    result, _ = integrate.quad(integrand, 0.001, r_max, limit=200)
    return result


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------
def main():
    print("=" * 76)
    print("Session 11 Phase 1: Cluster-surface form factor in K_3 mean field")
    print("=" * 76)
    print()
    print(f"CPP-derived inputs:")
    print(f"  hbar*omega = {hbar_omega} MeV")
    print(f"  sigma = {sigma:.4f} fm (nucleon localization length)")
    print(f"  N_alpha = {N_alpha}, R_cluster = {R_cluster} fm")
    print(f"  V0_per_alpha = {V0_per_alpha:.3f} MeV")
    print(f"  Sharpness ratio sigma/R_cluster = {sigma/R_cluster:.3f}")
    print(f"    (compare Woods-Saxon a/R ~ 0.1 — order of magnitude sharper)")
    print()
    
    # V_avg profile
    print(f"V_avg(r) profile at A=56:")
    print(f"  V_avg(0)        = {V_avg(0):8.3f} MeV  (well bottom)")
    print(f"  V_avg(R_cluster) = {V_avg(R_cluster):8.3f} MeV  (alpha-vertex shell)")
    print(f"  V_avg(5 fm)     = {V_avg(5.0):8.3f} MeV  (well outside cluster)")
    print()
    
    # f_SO profile — peaks at center, NOT at surface
    print(f"f_SO(r) = (1/r)*dV_avg/dr profile (MeV/fm^2):")
    for r in [0.01, 1.0, 2.37, 4.0, 5.0]:
        print(f"  r={r:.2f} fm: {f_SO(r):.4f}")
    print(f"  Peak: at the CENTER (r->0), value {f_SO(0.001):.3f} MeV/fm^2")
    print(f"  This is OPPOSITE of Bohr-Mottelson WS where df/dr peaks at surface.")
    print()
    
    # HO state spatial extent — high-l states live OUTSIDE cluster
    print(f"HO state |0,l> spatial extent:")
    print(f"  {'l':>3} {'orbital':>9} {'<r> (fm)':>11}")
    for l in range(7):
        spd = 'spdfghi'
        mean_r, _ = integrate.quad(lambda r: R_0l(r, l)**2 * r**3, 0, 25)
        print(f"  {l:>3} 1{spd[l]:>8} {mean_r:>11.3f}")
    print(f"  (R_cluster = {R_cluster} fm; high-l states extend BEYOND cluster surface)")
    print()
    
    # Matrix elements — decrease monotonically with l
    print(f"Matrix elements <f_SO>_{{0,l}} (MeV/fm^2):")
    me_vals = {}
    for l in range(7):
        me = matrix_element_fSO_0l(l)
        me_vals[l] = me
    for l in range(7):
        ratio = me_vals[l] / me_vals[0]
        print(f"  l={l}: <f_SO> = {me_vals[l]:.4f}   (ratio to l=0: {ratio:.4f})")
    print()
    
    # Calibration
    K_calib = V_SO_central / me_vals[0]
    K_bare_thomas = hbar_c**2 / (2 * m_n_c2**2)
    print(f"Calibration:")
    print(f"  K = V_SO_central / <f_SO>_{{0,0}} = {K_calib:.4f} fm^2")
    print(f"  K_bare_Thomas = (hbar*c)^2 / (2*m_n c^2)^2 = {K_bare_thomas:.4f} fm^2")
    print(f"  Ratio: K_CPP / K_bare = {K_calib/K_bare_thomas:.2f}")
    print()
    
    # V_SO_eff(l) — DECREASES with l (wrong direction!)
    print(f"V_SO_eff(l) = K * <f_SO>_{{0,l}}:")
    print(f"  {'l':>3} {'orbital':>9} {'magic':>7} {'V_SO (MeV)':>13} "
          f"{'V_SO/hw':>10} {'% of 0.20 thresh':>18}")
    print("  " + "-" * 70)
    spd = 'spdfghi'
    magics = {0: '-', 1: '8', 2: '20', 3: '28', 4: '50', 5: '82', 6: '126'}
    for l in range(7):
        V_SO_l = K_calib * me_vals[l]
        ratio_hw = V_SO_l / hbar_omega
        threshold_pct = ratio_hw / 0.20 * 100
        print(f"  {l:>3} 1{spd[l]:>8} {magics[l]:>7} {V_SO_l:>13.4f} "
              f"{ratio_hw:>10.4f} {threshold_pct:>15.1f}%")
    print()
    
    # Comparison: Session 9 uniform vs Phase 1 l-dependent
    print(f"Comparison: Session 9 uniform V_SO vs Phase 1 l-dependent")
    print(f"  Session 9: V_SO = 1.17 MeV uniform across all l")
    print(f"             -> V_SO/hbar*omega = 0.090 uniform (45% of strong-magic threshold)")
    print(f"  Phase 1:   V_SO_eff(l) DECREASES from 1.17 (l=0) to 0.338 (l=6)")
    print(f"             -> V_SO/hbar*omega from 0.090 (l=0) to 0.026 (l=6)")
    print(f"             -> WORSE than Session 9 uniform for high-l!")
    print()
    
    # Verdict
    print("=" * 76)
    print("PHASE 1 VERDICT: Path (i) cluster-surface Thomas-form RULED OUT")
    print("=" * 76)
    print()
    print("Three grounds:")
    print("  1. Wrong sign: V_SO_eff(l) DECREASES with l, opposite of empirical")
    print("     centrifugal-style enhancement (Bohr-Mottelson Woods-Saxon ENHANCES")
    print("     high-l via sharp surface form factor).")
    print("  2. Magnitude: V_SO_eff(l=6) = 0.338 MeV is 13% of empirical strong-")
    print("     magic threshold, WORSE than Session 9's uniform 1.17 MeV (45%).")
    print("  3. Structural origin: K_3 Gaussian-modulated mean field has FUZZY")
    print("     surface (sigma/R = 0.75 at A=56), opposite of Woods-Saxon SHARP")
    print("     surface (a/R ~ 0.1). Geometric deficiency is shape-level.")
    print()
    print("Fourth programme-level negative-result demonstration in OPEN-SS-35")
    print("closure programme (after Route D in S5P2, Route B-gamma in S7P2,")
    print("Route 1b in S10).")
    print()
    print("Programme implication: gap-strength closure of OPEN-SS-35 sub-question")
    print("(b) Route B-alpha layer 3 cannot be achieved within K_3 Gaussian-")
    print("modulated mean field + HO + L.S + V_SO refinement framework. Magic-")
    print("strength gap closure requires additional CPP physics BEYOND the")
    print("smooth K_3 Gaussian-modulated mean field.")


if __name__ == "__main__":
    main()
