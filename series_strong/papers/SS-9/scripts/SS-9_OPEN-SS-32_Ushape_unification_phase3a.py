"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase A reproducible computation.

Phase 3 Phase A: full 3N-6 vibrational-mode Hessian decomposition of the
K_3 Gaussian pair-potential at each canonical alpha-chain deltahedron's
equilibrium configuration.  Phase 2 (uniform-scaling model (a)) was
RULED OUT on three independent grounds.  Phase 3 Phase A executes the
full-Hessian generalization — model (b) at zeroth order, summed over
ALL vibrational modes (not just the totally-symmetric A_1 uniform-scaling
mode).

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3a.md

MODEL.  Each polytope edge (i,j) at equilibrium |R_i - R_j| = R_alpha
contributes a Gaussian pair potential:
  V_pair(r) = -B_pair * exp(-(r - R_alpha)^2 / (2 sigma_K3^2))
At equilibrium: V_pair(R_alpha) = -B_pair (recovers SS-7 LO).
            V_pair'(R_alpha) = 0  (no tension term)
            V_pair''(R_alpha) = B_pair / sigma_K3^2  (spring per edge)

Hessian H is 3N x 3N matrix.  For each edge (i,j) with unit vector
n_hat = (R_i - R_j)/R_alpha, the Hessian contribution is the standard
"spring connecting i and j along n_hat":
  H_{(i,a),(i,b)} += k_edge * n_hat_a * n_hat_b
  H_{(j,a),(j,b)} += k_edge * n_hat_a * n_hat_b
  H_{(i,a),(j,b)} -= k_edge * n_hat_a * n_hat_b
  H_{(j,a),(i,b)} -= k_edge * n_hat_a * n_hat_b
where k_edge = V_pair''(R_alpha) = B_pair / sigma_K3^2.

Diagonalize H to get 3N eigenvalues lambda_k and orthonormal eigenvectors
v_k.  Six lambda_k are (numerically) ~0 from rigid-body modes (3
translations + 3 rotations); these are excluded.  Remaining 3N-6 are
genuine vibrational modes.

For each non-rigid-body mode k (eigenvalue lambda_k > 0):
  omega_k^2 = lambda_k / m_alpha    (units 1/fm^2 in c=1)
  hbar*omega_k = hbar_c * sqrt(lambda_k / (m_alpha))   [MeV]
  Mode-k variance of edge (i,j):
    <(delta r_ij)^2>_k = hbar_c / (2 sqrt(m_alpha * lambda_k))
                        * [(v_k(i) - v_k(j)) . n_hat_ij]^2
                        [units fm^2]

Average over all edges and sum over all modes:
  <(delta r)^2>_avg = (1/|E|) sum_{edges} sum_modes <(delta r_ij)^2>_k

Fractional softening of nucleon-orbital hbar*omega^*:
  Delta(hbar*omega^*) / hbar*omega^* ~ -2 <(delta r)^2>_avg / R_alpha^2

DIAGNOSTICS.  Three:
  1. Magnitude — does full Hessian close the factor 7 magnitude gap of Phase 2?
  2. Pattern — does the model produce U-shape (J-solid mid-range overshoot)
     where Phase 2 model (a) produced monotonic decrease?
  3. N=6 selection rule — under model (b), does O_h symmetry produce
     less softening than D_2d (snub disphenoid, J-solid analog)?

INHERITANCE.  Polytope geometries and constants from Phase 2 script
(SS-9_OPEN-SS-32_Ushape_unification_phase2.py).
"""

import math
import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Constants (inherited from Phase 2 script)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790
B_pair       = M_0 / phi
m_n          = 939.565
m_alpha      = 3727.4
hbar_c       = 197.327
R_alpha      = 2.37
sigma_K3_canon = 1.68


# ---------------------------------------------------------------------------
# Polytope construction (inherited verbatim from Phase 2 script)
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
    return rescale(np.array([[1,1,1], [1,-1,-1], [-1,1,-1], [-1,-1,1]],
                            dtype=float))


def poly_5():
    return rescale(np.array([
        [1, 0, 0],
        [-0.5, math.sqrt(3)/2, 0],
        [-0.5, -math.sqrt(3)/2, 0],
        [0, 0, math.sqrt(2)],
        [0, 0, -math.sqrt(2)]
    ]))


def poly_6():
    return rescale(np.array([[1,0,0], [-1,0,0], [0,1,0], [0,-1,0],
                             [0,0,1], [0,0,-1]], dtype=float))


def poly_7():
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
    g = phi
    return rescale(np.array([
        [0,1,g], [0,1,-g], [0,-1,g], [0,-1,-g],
        [1,g,0], [1,-g,0], [-1,g,0], [-1,-g,0],
        [g,0,1], [g,0,-1], [-g,0,1], [-g,0,-1]
    ], dtype=float))


def build_edges(verts, R_edge=R_alpha, tol=0.05):
    """Return list of (i,j,unit_vec) for each edge."""
    n = len(verts)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dvec = verts[i] - verts[j]
            d = np.linalg.norm(dvec)
            if abs(d - R_edge) < tol:
                edges.append((i, j, dvec / d))
    return edges


# ---------------------------------------------------------------------------
# Phase 3 Phase A core: full Hessian decomposition
# ---------------------------------------------------------------------------
def build_hessian(verts, edges, sigma_K3=sigma_K3_canon):
    """Build full 3N x 3N Hessian matrix from K_3 Gaussian pair potentials."""
    N = len(verts)
    H = np.zeros((3*N, 3*N))
    k_edge = B_pair / sigma_K3**2  # spring constant per edge in MeV/fm^2

    for i, j, n_hat in edges:
        # outer product n_hat n_hat^T
        nnT = np.outer(n_hat, n_hat)
        # Diagonal blocks +k * n n^T
        H[3*i:3*i+3, 3*i:3*i+3] += k_edge * nnT
        H[3*j:3*j+3, 3*j:3*j+3] += k_edge * nnT
        # Off-diagonal blocks -k * n n^T (symmetric)
        H[3*i:3*i+3, 3*j:3*j+3] -= k_edge * nnT
        H[3*j:3*j+3, 3*i:3*i+3] -= k_edge * nnT

    # Symmetrize (numerical safety)
    H = (H + H.T) / 2
    return H


def vibrational_analysis(verts, edges, sigma_K3=sigma_K3_canon, eps_zero=1e-6):
    """Full Hessian diagonalization and zero-point edge-length fluctuation.

    Returns dict with:
      eigenvalues (sorted ascending), eigenvectors (each column is a mode),
      n_rigid (count of near-zero modes ~6), n_vib (3N - n_rigid),
      hbar_omega_modes (MeV, sorted), <(delta r)^2>_avg (fm^2),
      fractional softening (dimensionless).
    """
    N = len(verts)
    H = build_hessian(verts, edges, sigma_K3=sigma_K3)
    eigvals, eigvecs = np.linalg.eigh(H)  # ascending order
    # Identify rigid-body (zero) modes
    abs_max = np.max(np.abs(eigvals))
    is_zero = np.abs(eigvals) < eps_zero * abs_max
    n_rigid = int(np.sum(is_zero))
    n_vib   = 3*N - n_rigid

    # For each vibrational mode (lambda_k > 0), compute hbar*omega_k
    # and contribution to <(delta r)^2>_edge_averaged.
    hbar_omegas = []
    edge_msd_sum = 0.0
    n_edges = len(edges)

    for k in range(3*N):
        if is_zero[k]:
            continue
        lam = eigvals[k]
        if lam <= 0:
            continue
        v_k = eigvecs[:, k]               # length 3N
        v_k_per_vertex = v_k.reshape(N, 3)

        omega_k = math.sqrt(lam / m_alpha)              # 1/fm
        hbar_om = hbar_c * omega_k                       # MeV
        hbar_omegas.append(hbar_om)

        # Mode-k zero-point edge-length variance, summed over edges
        prefactor = hbar_c / (2.0 * math.sqrt(m_alpha * lam))  # fm^2
        for i, j, n_hat in edges:
            relative = v_k_per_vertex[i] - v_k_per_vertex[j]
            proj = float(np.dot(relative, n_hat))
            edge_msd_sum += prefactor * proj * proj

    edge_msd_avg = edge_msd_sum / n_edges
    delta_frac   = -2.0 * edge_msd_avg / R_alpha**2

    return {
        'N':              N,
        'eigvals':        eigvals,
        'n_rigid':        n_rigid,
        'n_vib':          n_vib,
        'hbar_omegas':    sorted(hbar_omegas),
        'edge_msd_avg':   edge_msd_avg,
        'delta_frac':     delta_frac,
    }


def empirical_required_softening(R_required_change_pct):
    x = R_required_change_pct / 100.0
    return -(1.0 - 1.0 / (1.0 + x) ** 2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 100)
    print("SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase A")
    print("Full 3N-6 vibrational-mode Hessian decomposition; K_3 Gaussian pair-potential")
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
          f"R_alpha = {R_alpha} fm, m_alpha = {m_alpha} MeV/c^2")
    print(f"K_3 spring per edge: k_edge = B_pair/sigma_K3^2 = "
          f"{B_pair/sigma_K3_canon**2:.3f} MeV/fm^2 at sigma_K3={sigma_K3_canon} fm")
    print()

    print("Per-polytope Hessian decomposition:")
    print(f"  {'N':>3} {'polytope':>22} {'sym':>5} {'|E|':>3} "
          f"{'n_vib':>5} {'omega_min':>9} {'omega_max':>9} "
          f"{'<dr^2>':>9} {'pred soft':>10} {'emp req':>9} {'pred/emp':>9}")
    print("  " + "-"*100)

    rows = []
    for N, fn, name, sym, R_pct in delta_polys:
        v = fn()
        edges = build_edges(v)
        E = len(edges)
        if E != 3*N - 6:
            print(f"  WARN N={N}: |E|={E} != 3N-6={3*N-6}")
        result = vibrational_analysis(v, edges, sigma_K3=sigma_K3_canon)

        omega_min = result['hbar_omegas'][0]
        omega_max = result['hbar_omegas'][-1]
        delta_frac = result['delta_frac']
        emp_soft = empirical_required_softening(R_pct)
        ratio = delta_frac / emp_soft if emp_soft != 0 else float('nan')

        print(f"  {N:>3} {name:>22} {sym:>5} {E:>3} "
              f"{result['n_vib']:>5} "
              f"{omega_min:>9.3f} {omega_max:>9.3f} "
              f"{result['edge_msd_avg']:>9.4f} "
              f"{delta_frac*100:>9.2f}% {emp_soft*100:>+8.1f}% {ratio:>9.3f}")
        rows.append((N, name, sym, E, result, emp_soft, ratio))

    print()
    print("Reading the table:")
    print("  n_vib       = 3N - 6 vibrational modes (rigid-body excluded)")
    print("  omega_min   = lowest non-zero hbar*omega_k (MeV)")
    print("  omega_max   = highest hbar*omega_k (MeV)")
    print("  <dr^2>      = edge-averaged sum of zero-point edge-length variances (fm^2)")
    print("  pred soft   = -2 * <dr^2> / R_alpha^2 (fractional softening)")
    print("  emp req     = 1 - 1/(1+x)^2 from Session 12 inversion")
    print()

    # ---- Pattern check ----
    print("Predicted softening pattern across deltahedra:")
    softenings = [r[4]['delta_frac'] for r in rows]
    for r in rows:
        N = r[0]
        s = r[4]['delta_frac']
        emp_pct = empirical_required_softening({4:-5.3, 5:6.7, 6:12.7, 7:19.1,
                                                 8:21.1, 9:22.3, 10:22.7,
                                                 12:-0.7}[N])
        print(f"  N={N:>2}: pred {s*100:+7.2f}%   emp {emp_pct*100:+7.1f}%")

    print()
    Ns         = [r[0] for r in rows]
    pred_pcts  = [r[4]['delta_frac']*100 for r in rows]
    emp_pcts   = [empirical_required_softening(R_pct)*100
                  for _,_,_,_, R_pct in [(N, fn, name, sym, R_pct)
                                         for N, fn, name, sym, R_pct in delta_polys]]

    # Detect peak position
    peak_idx_pred = int(np.argmin(pred_pcts))
    peak_idx_emp  = int(np.argmin(emp_pcts))
    print(f"Predicted softening peak (most negative): N={Ns[peak_idx_pred]} "
          f"({pred_pcts[peak_idx_pred]:+.2f}%)")
    print(f"Empirical softening peak (most negative): N={Ns[peak_idx_emp]} "
          f"({emp_pcts[peak_idx_emp]:+.2f}%)")

    # U-shape diagnostic
    print()
    print("U-shape diagnostic test:")
    print(f"  N=4 endpoint (tetrahedron, regular T_d):  pred {pred_pcts[0]:+.2f}%, "
          f"emp {emp_pcts[0]:+.1f}%")
    print(f"  N=8 J-solid (snub disphenoid):            pred {pred_pcts[4]:+.2f}%, "
          f"emp {emp_pcts[4]:+.1f}%")
    print(f"  N=12 endpoint (icosahedron, regular I_h): pred {pred_pcts[7]:+.2f}%, "
          f"emp {emp_pcts[7]:+.1f}%")

    # If all three constraints (low N=4, low N=12, peak in mid-range) hold:
    is_n4_small  = abs(pred_pcts[0]) < 8.0
    is_n12_small = abs(pred_pcts[7]) < 8.0
    is_mid_peak  = peak_idx_pred >= 3 and peak_idx_pred <= 6  # N in [7,10]
    print()
    print(f"  N=4 endpoint < 8% softening: {is_n4_small}")
    print(f"  N=12 endpoint < 8% softening: {is_n12_small}")
    print(f"  Peak in J-solid mid-range (N=7..10): {is_mid_peak}")
    print(f"  -> Full U-shape pattern reproduction: {is_n4_small and is_n12_small and is_mid_peak}")

    # ---- N=6 selection-rule test ----
    n6_pred = pred_pcts[2]
    n8_pred = pred_pcts[4]
    print()
    print(f"Reading A/B/C discriminator: N=6 octahedron (O_h) vs N=8 snub disphenoid (D_2d):")
    print(f"  N=6 (O_h, no belt):       {n6_pred:+.2f}%")
    print(f"  N=8 (D_2d, belt-active):  {n8_pred:+.2f}%")
    print(f"  Ratio N=6/N=8: {n6_pred/n8_pred:.3f}")
    if abs(n6_pred) < 0.5 * abs(n8_pred):
        print("  -> N=6 substantially less than N=8.  Reading A or C consistent.")
    else:
        print("  -> N=6 comparable to N=8.  Uniform-scaling-like behavior persists at full Hessian.")

    # ---- Magnitude assessment ----
    print()
    peak_pred = min(pred_pcts)
    peak_emp  = min(emp_pcts)
    print(f"Magnitude assessment at empirical peak:")
    print(f"  N={Ns[peak_idx_emp]}, empirical: {peak_emp:+.1f}%")
    print(f"  N={Ns[peak_idx_emp]}, model:     {pred_pcts[peak_idx_emp]:+.2f}%")
    print(f"  Model/empirical at empirical peak: {pred_pcts[peak_idx_emp]/peak_emp:.3f}")
    print(f"  Phase 2 Model (a) gave: 0.136 at same point")
    improvement = (pred_pcts[peak_idx_emp]/peak_emp) / 0.136
    print(f"  Phase 3 / Phase 2 improvement factor: {improvement:.2f}x")

    # ---- Comparison with Phase 2 model (a) ----
    print()
    print("Comparison with Phase 2 model (a) at same sigma_K3=1.68 fm:")
    phase2_predicts = {4:-21.05, 5:-13.78, 6:-10.53, 7:-7.99, 8:-6.47,
                       9:-5.42, 10:-4.57, 12:-3.50}
    print(f"  {'N':>3} {'Phase 2 (a)':>12} {'Phase 3 (b)':>12} {'ratio (b)/(a)':>14}")
    for r in rows:
        N = r[0]
        s2 = phase2_predicts[N]
        s3 = r[4]['delta_frac'] * 100
        print(f"  {N:>3} {s2:>12.2f}% {s3:>12.2f}% {s3/s2:>14.3f}")

    print()
    print("=" * 100)
    print("Phase 3 Phase A summary:")
    print("=" * 100)


if __name__ == "__main__":
    main()
