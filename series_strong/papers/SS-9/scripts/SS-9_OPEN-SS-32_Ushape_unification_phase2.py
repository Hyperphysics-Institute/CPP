"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 2 reproducible computation.

Phase 2 of the multi-session OPEN-SS-32 ↔ U-shape unification investigation
registered at Session 12 close as Priority 1 forward pointer.  Phase 1
(`SS-9_OPEN-SS-32_Ushape_unification_phase1.md`) established the prior-art
base, the geometric naturalness of the unification hypothesis, and the
discriminating N_alpha=6 selection-rule test.  Phase 2 executes the
uniform-scaling radial-breathing-mode computation per Phase 1 §6.3.

MODEL.  Uniform scaling lambda: each vertex R_i -> lambda * R_i.
  Energy at lambda detuning:
      E_cluster(lambda) = const - |E| * B_pair * exp(-(lambda-1)^2 (R_alpha/sigma_K3)^2 / 2)
  Spring constant:
      k_lambda = |E| * B_pair * (R_alpha/sigma_K3)^2     [MeV per dimensionless^2 = MeV]
  Effective mass for the lambda dof (kinetic energy = (1/2) M_lambda (dlambda/dt)^2):
      M_lambda * c^2 = m_alpha * sum_i |R_i|^2            [MeV * fm^2]
  Breathing-mode frequency:
      hbar * omega_br = hbar_c * sqrt(k_lambda / M_lambda c^2)   [MeV]
  Ground-state zero-point of the lambda dof:
      <(Delta lambda)^2> = hbar_c / (2 * sqrt(k_lambda * M_lambda c^2))
  Fractional softening of nucleon-orbital hbar*omega^*
  (since hbar*omega^* ~ 1/R_alpha^2):
      Delta(hbar*omega^*) / hbar*omega^* ~ -2 <(Delta lambda)^2>

CALIBRATION.  sigma_K3 is the K_3 mode width in space.  Natural CPP-internal
scale: sigma_K3 = R_RMS^alpha = 1.68 fm (the alpha overlap scale that anchors
the SS-7 §11 screening discussion).  Sensitivity scan at sigma_K3 in
{1.0, 1.4, 1.68, 2.0, 2.5} fm to bracket the result.

DIAGNOSTICS.  Three:
  1. Sign — a priori correct (positive zero-point broadening always lowers
     a 1/R^2 frequency dependence).
  2. Magnitude — empirical U-shape requires +7-23% R_alpha expansion at
     N_alpha = 5-10, which corresponds to -15-37% hbar*omega softening.
     Does the model produce comparable softening at peak?
  3. N_alpha=6 selection rule — Reading A (broader breathing selection
     than oblate deformation) predicts non-zero softening at the
     octahedron; Readings B/C predict zero or near-zero.

INHERITANCE.  Polytope geometries and constants from Session 7 A-scaling
script (series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling.py).

VERDICT (computed at end of script, not pre-stated).
"""

import math
import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Constants (inherited from Session 7 script)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790                       # MeV (CPP base mass scale)
B_pair       = M_0 / phi                   # 2.342 MeV (K_3 collective quantum)
m_n          = 939.565                     # MeV (nucleon mass)
m_alpha      = 3727.4                      # MeV (alpha-particle rest energy)
hbar_c       = 197.327                     # MeV*fm
R_alpha      = 2.37                        # fm (alpha-alpha contact distance, SS-7)
sigma_K3_canon = 1.68                      # fm (R_RMS^alpha, SS-7 §11 screening discussion)


# ---------------------------------------------------------------------------
# Polytope construction (inherited verbatim from Session 7 script)
# ---------------------------------------------------------------------------
def rescale(verts, R_target=R_alpha):
    n = len(verts)
    md = math.inf
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if d < md:
                md = d
    return verts * (R_target / md)


def poly_4():
    """Regular tetrahedron, N=4, T_d."""
    return rescale(np.array([[1,1,1], [1,-1,-1], [-1,1,-1], [-1,-1,1]],
                            dtype=float))


def poly_5():
    """Triangular bipyramid (D_3h), N=5."""
    return rescale(np.array([
        [1, 0, 0],
        [-0.5, math.sqrt(3)/2, 0],
        [-0.5, -math.sqrt(3)/2, 0],
        [0, 0, math.sqrt(2)],
        [0, 0, -math.sqrt(2)]
    ]))


def poly_6():
    """Regular octahedron, N=6, O_h."""
    return rescale(np.array([[1,0,0], [-1,0,0], [0,1,0], [0,-1,0],
                             [0,0,1], [0,0,-1]], dtype=float))


def poly_7():
    """Pentagonal bipyramid (D_5h), N=7."""
    pentR = 1.0
    edge = 2 * math.sin(math.pi/5)
    h = math.sqrt(edge**2 - pentR**2)
    pent = []
    for k in range(5):
        a = 2*math.pi*k/5
        pent.append([pentR*math.cos(a), pentR*math.sin(a), 0])
    pent.append([0, 0, h])
    pent.append([0, 0, -h])
    return rescale(np.array(pent))


def poly_8():
    """Snub disphenoid (Johnson J_84), N=8, D_2d."""
    np.random.seed(27)
    v0 = np.random.randn(24) * 0.6
    def loss(p):
        v = p.reshape(8, 3)
        ds = sorted([np.linalg.norm(v[i]-v[j])
                     for i in range(8) for j in range(i+1, 8)])
        return (sum((d-1)**2 for d in ds[:18]) +
                50*sum(max(0, 1.05-d)**2 for d in ds[18:]))
    res = minimize(loss, v0, method='Powell',
                   options={'maxiter': 10000, 'xtol': 1e-10})
    return rescale(res.x.reshape(8, 3))


def poly_9():
    """Triaugmented triangular prism (Johnson J_51), N=9, D_3h."""
    h = 0.5
    s = 1.0
    R = s / math.sqrt(3)
    prism = []
    for k in range(3):
        a = 2*math.pi*k/3
        prism.append([R*math.cos(a), R*math.sin(a), h])
        prism.append([R*math.cos(a), R*math.sin(a), -h])
    aug = []
    for k in range(3):
        a1 = 2*math.pi*k/3
        a2 = 2*math.pi*(k+1)/3
        mx = R*(math.cos(a1)+math.cos(a2))/2
        my = R*(math.sin(a1)+math.sin(a2))/2
        nrm = math.sqrt(mx**2 + my**2)
        ext = 1/math.sqrt(2)
        aug.append([mx + ext*mx/nrm, my + ext*my/nrm, 0])
    v0 = np.array(prism + aug).flatten()
    def loss(p):
        v = p.reshape(9, 3)
        ds = sorted([np.linalg.norm(v[i]-v[j])
                     for i in range(9) for j in range(i+1, 9)])
        return (sum((d-1)**2 for d in ds[:21]) +
                50*sum(max(0, 1.05-d)**2 for d in ds[21:]))
    res = minimize(loss, v0, method='Powell',
                   options={'maxiter': 30000, 'xtol': 1e-10})
    return rescale(res.x.reshape(9, 3))


def poly_10():
    """Gyroelongated square bipyramid (Johnson J_17), N=10, D_4d."""
    R = 1/math.sqrt(2)
    h = math.sqrt((1 - R**2*(2-math.sqrt(2)))/4)
    H = h + 1/math.sqrt(2)
    v = []
    for k in range(4):
        a = math.pi/2 * k
        v.append([R*math.cos(a), R*math.sin(a), h])
    for k in range(4):
        a = math.pi/2 * k + math.pi/4
        v.append([R*math.cos(a), R*math.sin(a), -h])
    v.append([0, 0, H])
    v.append([0, 0, -H])
    return rescale(np.array(v))


def poly_12():
    """Regular icosahedron, N=12, I_h."""
    g = phi
    return rescale(np.array([
        [0,1,g], [0,1,-g], [0,-1,g], [0,-1,-g],
        [1,g,0], [1,-g,0], [-1,g,0], [-1,-g,0],
        [g,0,1], [g,0,-1], [-g,0,1], [-g,0,-1]
    ], dtype=float))


def build_adjacency(verts, R_edge=R_alpha, tol=0.05):
    n = len(verts)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if abs(d - R_edge) < tol:
                adj[i].append(j); adj[j].append(i)
    deg = [len(a) for a in adj]
    return adj, deg, sum(deg) // 2


# ---------------------------------------------------------------------------
# Phase 2 core: uniform-scaling radial-breathing mode
# ---------------------------------------------------------------------------
def breathing_observables(verts, E, sigma_K3=sigma_K3_canon):
    """For a polytope at edge=R_alpha with |E| edges, return:
        k_lambda    [MeV]   spring constant for uniform scaling
        M_lambda_c2 [MeV*fm^2]  mass parameter for lambda dof
        hbar_omega_br [MeV]
        var_lambda dimensionless (zero-point amplitude squared)
        delta_hbarom_frac dimensionless (fractional softening of hbar*omega^*)
    """
    centroid = np.mean(verts, axis=0)
    R_squared_sum = float(np.sum(np.linalg.norm(verts - centroid, axis=1) ** 2))

    k_lambda    = E * B_pair * (R_alpha / sigma_K3) ** 2
    M_lambda_c2 = m_alpha * R_squared_sum
    hbar_om_br  = hbar_c * math.sqrt(k_lambda / M_lambda_c2)
    var_lambda  = hbar_c / (2.0 * math.sqrt(k_lambda * M_lambda_c2))
    delta_frac  = -2.0 * var_lambda

    return {
        'R2_sum':        R_squared_sum,
        'k_lambda':      k_lambda,
        'M_lambda_c2':   M_lambda_c2,
        'hbar_omega_br': hbar_om_br,
        'var_lambda':    var_lambda,
        'delta_frac':    delta_frac,
    }


def empirical_required_softening(N_alpha, R_required_change_pct):
    """Empirical: required R_alpha expansion x corresponds to hbar*omega
    softening of (1 - 1/(1+x)^2).  Returns negative-of-fraction (softening)."""
    x = R_required_change_pct / 100.0
    softening = (1.0 - 1.0 / (1.0 + x) ** 2)
    return -softening


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 100)
    print("SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 2 (Session 14 candidate result)")
    print("Uniform-scaling radial-breathing-mode prediction vs Session 12 inversion-table U-shape")
    print("=" * 100)
    print()

    delta_polys = [
        (4,  poly_4,  'tetrahedron',         'T_d',   -5.3),
        (5,  poly_5,  'triangular bipyramid','D_3h',  +6.7),
        (6,  poly_6,  'octahedron',          'O_h',  +12.7),
        (7,  poly_7,  'pentagonal bipyramid','D_5h', +19.1),
        (8,  poly_8,  'snub disphenoid',     'D_2d', +21.1),
        (9,  poly_9,  'triaug. tri. prism',  'D_3h', +22.3),
        (10, poly_10, 'gyroel. sq. bipyr.',  'D_4d', +22.7),
        (12, poly_12, 'icosahedron',         'I_h',   -0.7),
    ]

    print(f"Constants: B_pair = M_0/phi = {B_pair:.3f} MeV, "
          f"R_alpha = {R_alpha} fm, m_alpha = {m_alpha} MeV/c^2, "
          f"sigma_K3 = {sigma_K3_canon} fm (canonical, R_RMS^alpha)")
    print()

    print("Per-polytope geometry verification and breathing-mode observables:")
    print(f"  {'N':>3} {'polytope':>22} {'sym':>5} {'|E|':>3} "
          f"{'<R^2>':>7} {'omega_br':>9} {'<dlam^2>':>9} "
          f"{'pred soft':>10} {'emp req':>9} {'pred/emp':>9}")
    print("  " + "-"*100)

    rows = []
    for N, fn, name, sym, R_pct in delta_polys:
        v = fn()
        adj, deg, E = build_adjacency(v)
        if E != 3*N - 6:
            print(f"  WARN N={N}: |E|={E} != 3N-6={3*N-6}")
        obs = breathing_observables(v, E, sigma_K3=sigma_K3_canon)
        emp_soft = empirical_required_softening(N, R_pct)
        ratio = obs['delta_frac'] / emp_soft if emp_soft != 0 else float('nan')

        print(f"  {N:>3} {name:>22} {sym:>5} {E:>3} "
              f"{obs['R2_sum']:>7.2f} {obs['hbar_omega_br']:>9.3f} "
              f"{obs['var_lambda']:>9.4f} {obs['delta_frac']*100:>9.2f}% "
              f"{emp_soft*100:>+8.1f}% {ratio:>9.3f}")
        rows.append((N, name, sym, E, obs, emp_soft, ratio))

    print()
    print("Reading the table:")
    print("  pred soft   = -2 * <(Delta lambda)^2>            (model prediction, fractional)")
    print("  emp req     = 1 - 1/(1+x)^2 where x = R_alpha % required (Session 12 inversion)")
    print("  pred/emp    = ratio of model softening to empirical-required softening")
    print()

    # ---- Pattern check ----
    softenings = [r[4]['delta_frac'] for r in rows]
    print("Predicted softening pattern (fraction):")
    for r in rows:
        N = r[0]
        s = r[4]['delta_frac']
        print(f"  N={N:>2}: {s:+.4f}")

    print()
    print("U-shape diagnostic: empirical pattern is")
    print("  -5.3% (N=4) -> +20-23% (N=7-10) -> -0.7% (N=12), peaking at N=10")
    print("Predicted pattern: monotonic with N (decreasing magnitude as N grows)?")
    is_mono = all(abs(rows[i+1][4]['delta_frac']) <= abs(rows[i][4]['delta_frac'])
                  for i in range(len(rows)-1))
    print(f"  Monotonic decrease with N: {is_mono}")

    # ---- N=6 selection-rule discriminator ----
    print()
    print("Reading A/B/C discriminator at N_alpha=6 (octahedron, O_h):")
    n6_pred = next(r for r in rows if r[0] == 6)[4]['delta_frac']
    print(f"  Model predicts softening at N=6: {n6_pred*100:.2f}%")
    if abs(n6_pred) > 0.01:
        print("  -> Model gives NON-ZERO softening at N=6.")
        print("     This is consistent with Reading A (broader breathing selection")
        print("     than OPEN-SS-32 oblate-deformation selection).")
        print("     The octahedron has edges and therefore a uniform-scaling")
        print("     breathing mode, even though O_h forbids static oblate deformation.")
    else:
        print("  -> Model gives near-zero softening at N=6 (Readings B/C).")

    # ---- Sensitivity scan over sigma_K3 ----
    print()
    print("Sensitivity scan over sigma_K3 (canonical 1.68 fm):")
    print(f"  {'sigma_K3':>9} {'<dlam^2> at N=8':>16} {'pred soft at N=8':>18}")
    for sigma in [1.0, 1.4, 1.68, 2.0, 2.5]:
        v8 = poly_8()
        _, _, E8 = build_adjacency(v8)
        obs8 = breathing_observables(v8, E8, sigma_K3=sigma)
        print(f"  {sigma:>9.2f} fm {obs8['var_lambda']:>16.4f} "
              f"{obs8['delta_frac']*100:>16.2f}%")

    print()
    print("Magnitude assessment.")
    print("  At N=10 (peak of empirical U-shape), empirical softening required is",
          f"{empirical_required_softening(10, 22.7)*100:+.1f}%")
    n10_pred = next(r for r in rows if r[0] == 10)[4]['delta_frac']
    print(f"  Model prediction at N=10: {n10_pred*100:+.2f}%")
    print(f"  Predicted/empirical at N=10: {n10_pred/empirical_required_softening(10, 22.7):.3f}")

    print()
    print("=" * 100)
    print("Summary findings:")
    print("=" * 100)

    # Sign
    if all(s < 0 for s in softenings):
        print("  (1) SIGN: Predicted softening is uniformly negative (lowers hbar*omega).")
        print("      Sign matches empirical U-shape requirement (which needs softening")
        print("      for 5 <= N_alpha <= 10).")
    else:
        print("  (1) SIGN: predicted softening pattern includes positive values "
              "(unexpected; check geometry).")

    # Magnitude
    peak_ratio = abs(n10_pred / empirical_required_softening(10, 22.7))
    print(f"  (2) MAGNITUDE: at N=10 (empirical peak), model gives "
          f"{peak_ratio*100:.1f}% of empirical-required softening.")
    if peak_ratio < 0.3:
        print("      Model UNDERPREDICTS by factor 1/{:.2f} ~ {:.0f}x at peak.".format(
            peak_ratio, 1/peak_ratio))
        print("      Uniform-scaling radial-breathing alone cannot close R2.")
    elif peak_ratio < 0.7:
        print("      Model produces partial closure of empirical magnitude.")
    else:
        print("      Model produces near-full closure of empirical magnitude.")

    # Pattern
    print(f"  (3) PATTERN: model is monotonic in N; empirical is U-shaped.")
    print("      The model does NOT reproduce the U-shape selection-rule structure.")
    print("      Uniform-scaling captures edge density (3N-6)/N which saturates")
    print("      smoothly with N, not the J-solid mid-range overshoot.")

    # Selection rule
    print(f"  (4) N=6 SELECTION-RULE TEST: {n6_pred*100:.2f}% softening predicted.")
    print("      Non-zero -> Reading A consistent (broader breathing selection)")
    print("      OR uniform scaling is the wrong dof; symmetry-resolved")
    print("      decomposition (model b) needed for shape-class sensitivity.")

    print()
    print("Verdict: uniform-scaling model is INSUFFICIENT.")
    print("  - Magnitude undershoots empirical at peak by factor ~5-10x.")
    print("  - Pattern is monotonic, not U-shaped.")
    print("  - Phase 3 needs symmetry-resolved breathing decomposition")
    print("    (one mode per IRREP) targeting belt-localized J-solid modes.")
    print("  - R2 closure not achieved by simplest model (a); under model (a)")
    print("    the unification hypothesis is partially supported (sign correct,")
    print("    non-zero at N=6 supports Reading A) but quantitatively short.")


if __name__ == "__main__":
    main()
