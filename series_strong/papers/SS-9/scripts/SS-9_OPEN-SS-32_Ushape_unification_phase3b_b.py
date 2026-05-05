"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase B sub-phase B (Phase 3B-B).

Phase 3B-B: full character-theory IRREP decomposition with belt-IRREP
dimension scaling.

Phase 3B-A (RULED OUT, Session 14) used a fixed-dimension belt subspace
(monopole + 2D E_2 quadrupole, dim(B) ≤ 3) and produced anti-correlated
pattern within axial polytopes — belt fraction monotonically decreases
N_α=5 (0.39) → N_α=10 (0.10) while empirical magnitude monotonically
increases.  Phase 3B-A §6 identified the structural problem: fixed-
dimension belt subspaces cover a shrinking fraction of belt-radial
space as polytopes grow, so dimension must scale with N.

Phase 3B-B operationalizes "belt-IRREP" via the C_n proper-rotation
subgroup of each axial polytope's full point group.  The C_n IRREPs
are labeled by angular momentum m = 0, 1, ..., n-1.  Three natural
"belt-IRREP" definitions are tested independently:

  B-B1  "all m ≠ 0"  -- every axially-anisotropic mode (broadest).
                        At C_n, fraction of mode space with m ≠ 0 is
                        roughly (n-1)/n of total.
  B-B2  "m = 2 only" -- specifically the oblate-quadrupole IRREP, the
                        SS-7 OPEN-SS-32 hypothesis target.  Exists only
                        when n ≥ 3 (else m=2 wraps to m=0 or m=1).
  B-B3  "m ≠ 0 and in-plane radial only" -- the dimension-scaling
                        generalization of Phase 3B-A's fixed 3-dim
                        belt-radial subspace.

DEGENERATE-inertia polytopes (T_d, O_h, I_h) have no preferred axis;
declared dim(belt) = 0 by symmetry, identical to Phase 3B-A.

This is the simplest "full character-theory" implementation that
respects belt-IRREP dimension scaling.  Strictly the full point group
decomposition (D_nh, D_nd including reflections and improper rotations)
would be a further refinement; the C_n proper-rotation subgroup is a
coarser decomposition that gives an UPPER BOUND on the variance content
of any belt-IRREP definition within the full point group (further
restriction can only reduce variance).  So: if Phase 3B-B's C_n
construction overshoots empirical structurally, the full-point-group
refinement cannot rescue it.  Conversely, if C_n undershoots, the
full-point-group refinement undershoots more.

OPERATIONAL DEFINITIONS

Cyclic-symmetry detection.  For each axial polytope, the principal
axis (from Phase 3B-A's inertia classification) is the candidate C_n
axis.  Try n = 2, 3, 4, 5 in increasing order; n is the LARGEST for
which the rotation by 2π/n about the principal axis maps the polytope
vertex set to itself within numerical tolerance.

Vertex permutation.  Under the C_n rotation, each vertex maps to
another vertex.  Build a permutation π such that vertex i maps to
vertex π(i).

Rotation operator on displacement space.  R_n acts on 3N-dim
displacement space as a tensor product of vertex permutation and
3D rotation:
  R_n[displacement at vertex i, axis a] = R_3D[axis a, axis b] *
                                          displacement at vertex π(i),
                                          axis b
i.e., R_n displaces (rotated copy of) the displacement at the
pre-image vertex.

Angular-m projection operators.  For each m ∈ {0, 1, ..., n-1}:
  P_m = (1/n) Σ_{j=0}^{n-1} cos(2πmj/n) R_n^j

(real-valued projection; equivalent to averaging R_n^j and R_n^{-j}
contributions to capture cos(mθ) symmetric m components.  For m and
n-m, these are degenerate IRREP partners — captured together by the
real cosine projection.)

For odd n: m=0 is 1-dim (A_1); m=1, ..., (n-1)/2 are 2-dim doublets.
For even n: m=0 and m=n/2 are 1-dim; intermediate m are 2-dim.

Belt-IRREP fractions.  For each Hessian eigenmode v_k:
  f_k^{B-B1} = Σ_{m=1}^{n-1} ||P_m v_k||² = ||(I - P_0) v_k||²
  f_k^{B-B2} = ||P_2 v_k||²       (only defined for n ≥ 3)
  f_k^{B-B3} = ||P_radial · (I - P_0) v_k||²  where P_radial restricts
                                              to in-plane radial dir.

Belt-projected variance.  Same per-edge MSD weighting scheme as Phase
3B-A but with f_k^{B-B1}, f_k^{B-B2}, f_k^{B-B3} replacing the fixed-
dim f_k^{belt}.

Sanity checks: Σ_k f_k^{B-B1} should equal the count of m ≠ 0 modes
in the vibrational subspace.  Σ_k all f_k^{(m)} should equal n_vib
exactly (completeness of P_0, ..., P_{n-1}).

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3b_b.md

Inheritance: polytopes, edge construction, Hessian build, m_α / B_pair
/ R_α constants from Phase 3A; inertia classification + Gram-Schmidt +
rigid-body subspace + per-mode variance scheme from Phase 3B-A.
"""

import math
import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 3B-A / Phase 3A)
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
# Polytope construction (verbatim from Phase 3B-A / Phase 3A)
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
# Hessian + inertia (inherited from Phase 3A / 3B-A)
# ---------------------------------------------------------------------------
def build_hessian(verts, edges, sigma_K3=sigma_K3_canon):
    N = len(verts)
    H = np.zeros((3*N, 3*N))
    k_edge = B_pair / sigma_K3**2
    for i, j, n_hat in edges:
        nnT = np.outer(n_hat, n_hat)
        H[3*i:3*i+3, 3*i:3*i+3] += k_edge * nnT
        H[3*j:3*j+3, 3*j:3*j+3] += k_edge * nnT
        H[3*i:3*i+3, 3*j:3*j+3] -= k_edge * nnT
        H[3*j:3*j+3, 3*i:3*i+3] -= k_edge * nnT
    H = (H + H.T) / 2
    return H


def inertia_tensor(verts):
    com = verts.mean(axis=0)
    verts_c = verts - com
    I = np.zeros((3, 3))
    for r in verts_c:
        I += np.eye(3) * (r @ r) - np.outer(r, r)
    return I


def classify_axial_structure(verts, deg_thresh=1e-3):
    I = inertia_tensor(verts)
    eigvals, eigvecs = np.linalg.eigh(I)
    spread = (eigvals.max() - eigvals.min()) / max(eigvals.max(), 1e-12)
    if spread < deg_thresh:
        return 'DEGEN', None, eigvals
    gap_low = eigvals[1] - eigvals[0]
    gap_hi  = eigvals[2] - eigvals[1]
    if gap_low > gap_hi:
        return 'PROLATE', eigvecs[:, 0], eigvals
    else:
        return 'OBLATE',  eigvecs[:, 2], eigvals


# ---------------------------------------------------------------------------
# Phase 3B-B new: cyclic-symmetry detection + IRREP projection
# ---------------------------------------------------------------------------
def rotation_matrix_axis_angle(axis, theta):
    """Rodrigues formula: 3D rotation matrix by angle theta about axis."""
    a = axis / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]],
                  [a[2], 0, -a[0]],
                  [-a[1], a[0], 0]])
    return np.eye(3) + math.sin(theta) * K + (1 - math.cos(theta)) * (K @ K)


def detect_vertex_permutation(verts, axis, n, tol=0.05):
    """For C_n rotation about axis, return permutation pi such that vertex i
    rotates onto vertex pi[i].  Returns None if the rotation does not map
    the vertex set to itself within tolerance."""
    com = verts.mean(axis=0)
    verts_c = verts - com
    R = rotation_matrix_axis_angle(axis, 2 * math.pi / n)
    rotated = (R @ verts_c.T).T

    N = len(verts)
    pi = np.full(N, -1, dtype=int)
    for i in range(N):
        # find the original vertex closest to rotated[i]
        dists = np.linalg.norm(verts_c - rotated[i], axis=1)
        best = int(np.argmin(dists))
        if dists[best] > tol * R_alpha:
            return None
        pi[i] = best

    # Check it's a valid permutation
    if len(set(pi.tolist())) != N:
        return None
    return pi


def detect_largest_Cn(verts, axis):
    """Find the largest n in {2, 3, 4, 5} for which the polytope has C_n
    proper-rotation symmetry about axis.  Returns (n, permutation) or
    (1, identity) if no non-trivial rotation found.
    """
    N = len(verts)
    for n_try in [5, 4, 3, 2]:
        pi = detect_vertex_permutation(verts, axis, n_try)
        if pi is not None:
            return n_try, pi
    return 1, np.arange(N)


def build_Cn_displacement_operator(verts, axis, n, perm):
    """Build the 3N x 3N matrix R_n acting on displacement space.

    Under R_n, the displacement at vertex i maps to the displacement at
    vertex perm[i] rotated by the 3D rotation.  Equivalently:
      (R_n u)[3*perm[i] : 3*perm[i]+3]  =  R_3D @ u[3*i : 3*i+3]

    So as a 3N x 3N matrix, the entries are:
      R_n[3*perm[i]:3*perm[i]+3, 3*i:3*i+3] = R_3D
    and zero elsewhere.
    """
    N = len(verts)
    R_3D = rotation_matrix_axis_angle(axis, 2 * math.pi / n)
    R_op = np.zeros((3*N, 3*N))
    for i in range(N):
        j = perm[i]
        R_op[3*j:3*j+3, 3*i:3*i+3] = R_3D
    return R_op


def build_irrep_projectors(R_op, n):
    """Build real-valued m-IRREP projection operators P_m for m = 0, ..., n-1.

    P_m = (1/n) Σ_{j=0}^{n-1} cos(2π m j / n) R_op^j

    (This captures the cos(mθ) component; for n even the m=n/2 projector
    is real; for general m and n-m these are degenerate IRREP partners
    that we collapse via real-cosine.  Σ_m P_m = I to within numerical
    tolerance.)

    Returns list of 3N x 3N matrices [P_0, P_1, ..., P_{n-1}].
    """
    if n == 1:
        return [np.eye(R_op.shape[0])]
    powers = [np.eye(R_op.shape[0])]
    for j in range(1, n):
        powers.append(powers[-1] @ R_op)
    P = []
    for m in range(n):
        Pm = np.zeros_like(R_op)
        for j in range(n):
            Pm += math.cos(2 * math.pi * m * j / n) * powers[j]
        Pm /= n
        P.append(Pm)
    return P


def build_radial_projector(verts, axis):
    """Build 3N x 3N projector onto in-plane radial-displacement subspace
    (each vertex's ρ̂_i direction in the principal-axis frame).
    Vertices on the axis (ρ_i ≈ 0) contribute zero rows/cols.
    """
    N = len(verts)
    com = verts.mean(axis=0)
    verts_c = verts - com
    axis_unit = axis / np.linalg.norm(axis)

    P_rad = np.zeros((3*N, 3*N))
    for i in range(N):
        r = verts_c[i]
        z_i = r @ axis_unit
        r_perp = r - z_i * axis_unit
        rho_i = np.linalg.norm(r_perp)
        if rho_i < 1e-8:
            continue
        rhat = r_perp / rho_i
        # Projector onto rhat at vertex i: outer product of rhat with itself
        P_rad[3*i:3*i+3, 3*i:3*i+3] = np.outer(rhat, rhat)
    return P_rad


# ---------------------------------------------------------------------------
# Vibrational analysis with three Phase 3B-B variants
# ---------------------------------------------------------------------------
def vibrational_analysis_phase3b_b(verts, edges, sigma_K3=sigma_K3_canon,
                                   eps_zero=1e-6):
    """Full Hessian + three belt-IRREP projection variants:
        B-B1:  all m ≠ 0 (any axial-symmetry-breaking mode)
        B-B2:  m = 2 only (oblate-quadrupole IRREP)
        B-B3:  m ≠ 0 AND in-plane radial only (dim-scaling Phase 3B-A)
    """
    N = len(verts)
    H = build_hessian(verts, edges, sigma_K3=sigma_K3)
    eigvals, eigvecs = np.linalg.eigh(H)

    abs_max = np.max(np.abs(eigvals))
    is_zero = np.abs(eigvals) < eps_zero * abs_max
    n_rigid = int(np.sum(is_zero))
    n_vib   = 3*N - n_rigid

    cls, axis, inertia_eigs = classify_axial_structure(verts)

    if cls == 'DEGEN':
        # Reading-A structural commitment: no axis → no belt-IRREP
        n_cyc = 0
        irreps_dim = {}
        P_proj = None
    else:
        n_cyc, perm = detect_largest_Cn(verts, axis)
        if n_cyc <= 1:
            irreps_dim = {}
            P_proj = None
        else:
            R_op = build_Cn_displacement_operator(verts, axis, n_cyc, perm)
            P_list = build_irrep_projectors(R_op, n_cyc)
            P_rad  = build_radial_projector(verts, axis)
            P_proj = (P_list, P_rad)
            # Diagnostic: trace of each projector = dimension of m-IRREP
            irreps_dim = {m: float(np.trace(P_list[m])) for m in range(n_cyc)}

    n_edges = len(edges)
    edge_msd_full = 0.0
    edge_msd_BB1  = 0.0          # all m ≠ 0
    edge_msd_BB2  = 0.0          # m = 2 only
    edge_msd_BB3  = 0.0          # m ≠ 0 AND in-plane radial

    # Per-mode IRREP-component sums for sanity
    sum_f_BB1 = 0.0
    sum_f_BB2 = 0.0
    sum_f_BB3 = 0.0

    for k in range(3*N):
        if is_zero[k]:
            continue
        lam = eigvals[k]
        if lam <= 0:
            continue
        v_k = eigvecs[:, k]
        v_per_v = v_k.reshape(N, 3)

        # belt-IRREP fractions
        f_BB1 = 0.0
        f_BB2 = 0.0
        f_BB3 = 0.0
        if P_proj is not None:
            P_list, P_rad = P_proj
            n_cyc_local = len(P_list)
            # B-B1: ||(I - P_0) v_k||^2  =  1 - ||P_0 v_k||^2
            P0v = P_list[0] @ v_k
            f_BB1 = 1.0 - float(P0v @ P0v)
            f_BB1 = max(f_BB1, 0.0)
            # B-B2: ||P_2 v_k||^2 (only if m=2 exists, i.e. n_cyc >= 3)
            if n_cyc_local >= 3:
                P2v = P_list[2] @ v_k
                f_BB2 = float(P2v @ P2v)
            # B-B3: ||P_rad · (I - P_0) v_k||^2
            non_sym_v = v_k - P0v
            radial_non_sym = P_rad @ non_sym_v
            f_BB3 = float(radial_non_sym @ radial_non_sym)

        sum_f_BB1 += f_BB1
        sum_f_BB2 += f_BB2
        sum_f_BB3 += f_BB3

        # per-edge MSD
        prefactor = hbar_c / (2.0 * math.sqrt(m_alpha * lam))
        msd_k_full = 0.0
        for i, j, n_hat in edges:
            relative = v_per_v[i] - v_per_v[j]
            proj = float(np.dot(relative, n_hat))
            msd_k_full += prefactor * proj * proj
        edge_msd_full += msd_k_full
        edge_msd_BB1  += f_BB1 * msd_k_full
        edge_msd_BB2  += f_BB2 * msd_k_full
        edge_msd_BB3  += f_BB3 * msd_k_full

    return {
        'cls':              cls,
        'inertia_eigvals':  inertia_eigs,
        'n_cyc':            n_cyc if cls != 'DEGEN' else 0,
        'irreps_dim':       irreps_dim,
        'n_vib':            n_vib,
        'edge_msd_full_avg': edge_msd_full / n_edges,
        'edge_msd_BB1_avg':  edge_msd_BB1 / n_edges,
        'edge_msd_BB2_avg':  edge_msd_BB2 / n_edges,
        'edge_msd_BB3_avg':  edge_msd_BB3 / n_edges,
        'delta_full':       -2.0 * (edge_msd_full / n_edges) / R_alpha**2,
        'delta_BB1':        -2.0 * (edge_msd_BB1  / n_edges) / R_alpha**2,
        'delta_BB2':        -2.0 * (edge_msd_BB2  / n_edges) / R_alpha**2,
        'delta_BB3':        -2.0 * (edge_msd_BB3  / n_edges) / R_alpha**2,
        'sum_f_BB1':        sum_f_BB1,
        'sum_f_BB2':        sum_f_BB2,
        'sum_f_BB3':        sum_f_BB3,
    }


def empirical_required_softening(R_required_change_pct):
    x = R_required_change_pct / 100.0
    return -(1.0 - 1.0 / (1.0 + x) ** 2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 130)
    print("SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase B sub-phase B "
          "(Phase 3B-B)")
    print("Full C_n IRREP decomposition with three belt-IRREP variants; "
          "K_3 Gaussian pair-potential")
    print("=" * 130)
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
          f"{B_pair/sigma_K3_canon**2:.3f} MeV/fm^2 at "
          f"sigma_K3={sigma_K3_canon} fm")
    print()

    print("Phase 3B-B: full C_n IRREP decomposition; "
          "three belt-IRREP variants tested")
    print(f"  {'N':>3} {'sym':>5} {'class':>8} {'C_n':>3} "
          f"{'-d_full%':>9} {'-d_BB1%':>9} {'-d_BB2%':>9} {'-d_BB3%':>9} "
          f"{'-d_emp%':>9} "
          f"{'BB1/full':>9} {'BB2/full':>9} {'BB3/full':>9}")
    print("  " + "-"*128)

    rows = []
    for N, fn, name, sym, R_pct in delta_polys:
        v = fn()
        edges = build_edges(v)
        if len(edges) != 3*N - 6:
            print(f"  WARN N={N}: |E|={len(edges)} != 3N-6={3*N-6}")

        result = vibrational_analysis_phase3b_b(v, edges,
                                                sigma_K3=sigma_K3_canon)
        emp_soft = empirical_required_softening(R_pct)

        if result['delta_full'] != 0:
            BB1f = result['delta_BB1'] / result['delta_full']
            BB2f = result['delta_BB2'] / result['delta_full']
            BB3f = result['delta_BB3'] / result['delta_full']
        else:
            BB1f = BB2f = BB3f = 0.0

        print(f"  {N:>3} {sym:>5} {result['cls']:>8} "
              f"{result['n_cyc']:>3} "
              f"{result['delta_full']*100:>9.2f} "
              f"{result['delta_BB1']*100:>9.2f} "
              f"{result['delta_BB2']*100:>9.2f} "
              f"{result['delta_BB3']*100:>9.2f} "
              f"{emp_soft*100:>+8.1f} "
              f"{BB1f:>9.3f} {BB2f:>9.3f} {BB3f:>9.3f}")
        rows.append((N, name, sym, result, emp_soft))

    print()

    # --- Sanity checks --------------------------------------------------
    print("Sanity checks: per-IRREP dimensions (trace of projectors) and "
          "Σ f over modes")
    print(f"  {'N':>3} {'class':>8} {'C_n':>3} "
          f"{'sum_f_BB1':>10} {'sum_f_BB2':>10} {'sum_f_BB3':>10} "
          f"{'IRREP dimensions (trace P_m)':>40}")
    for N, name, sym, result, _ in rows:
        irreps = result['irreps_dim']
        dim_str = (', '.join(f"P{m}={d:.1f}" for m, d in irreps.items())
                   if irreps else "—")
        print(f"  {N:>3} {result['cls']:>8} {result['n_cyc']:>3} "
              f"{result['sum_f_BB1']:>10.4f} "
              f"{result['sum_f_BB2']:>10.4f} "
              f"{result['sum_f_BB3']:>10.4f} "
              f"{dim_str:>40}")
    print()
    print("  Σ f_BB1 = (n_vib − count of m=0 modes); Σ trace P_m = 3N.")
    print("  Σ f_BB3 ≤ Σ f_BB1 (B-B3 is more restrictive than B-B1).")
    print()

    # --- Phase 3A reproduction check ------------------------------------
    print("Phase 3A reproduction check (delta_full should match Phase 3A "
          "table within rounding):")
    phase3a_expected = {4: -86.77, 5: -85.71, 6: -86.53, 7: -85.22,
                        8: -85.47, 9: -85.35, 10: -85.15, 12: -84.92}
    for N, name, sym, result, _ in rows:
        d_full_pct = result['delta_full'] * 100
        expected = phase3a_expected[N]
        diff = d_full_pct - expected
        ok = "✓" if abs(diff) < 0.05 else "✗"
        print(f"  N={N:>3}: predicted {d_full_pct:>8.3f}%, "
              f"Phase 3A expected {expected:>7.2f}%, "
              f"diff {diff:+.3f}%  {ok}")
    print()

    # --- Pattern comparison ---------------------------------------------
    print("=" * 130)
    print("PATTERN COMPARISON — does ANY belt-IRREP variant track empirical "
          "U-shape?")
    print("=" * 130)
    print(f"  {'N':>3} {'polytope':>22} "
          f"{'-d_BB1%':>10} {'-d_BB2%':>10} {'-d_BB3%':>10} "
          f"{'-d_emp%':>10} "
          f"{'BB1/emp':>9} {'BB2/emp':>9} {'BB3/emp':>9}")
    for r in rows:
        N, name, sym, result, emp = r
        d_BB1 = result['delta_BB1'] * 100
        d_BB2 = result['delta_BB2'] * 100
        d_BB3 = result['delta_BB3'] * 100
        d_emp = emp * 100
        r1 = d_BB1 / d_emp if d_emp != 0 else float('nan')
        r2 = d_BB2 / d_emp if d_emp != 0 else float('nan')
        r3 = d_BB3 / d_emp if d_emp != 0 else float('nan')
        print(f"  {N:>3} {name:>22} "
              f"{d_BB1:>+10.2f} {d_BB2:>+10.2f} {d_BB3:>+10.2f} "
              f"{d_emp:>+10.2f} "
              f"{r1:>9.3f} {r2:>9.3f} {r3:>9.3f}")
    print()

    # --- Target audits --------------------------------------------------
    print("=" * 130)
    print("TARGET AUDIT — three quantitative targets from Phase 3A bracketing")
    print("=" * 130)

    j_solid = [r for r in rows if r[0] in (7, 8, 9, 10)]

    for variant_label, key in [('B-B1 (all m≠0)',  'delta_BB1'),
                                ('B-B2 (m=2 only)', 'delta_BB2'),
                                ('B-B3 (radial m≠0)', 'delta_BB3')]:
        avg_var_frac = np.mean([
            r[3][key] / r[3]['delta_full']
            if r[3]['delta_full'] != 0 else 0.0
            for r in j_solid
        ])
        print(f"\nTarget (a) for {variant_label} — J-solid mid-range "
              f"variance fraction at N=7..10 target ~0.40:")
        for r in j_solid:
            vf = (r[3][key] / r[3]['delta_full']
                  if r[3]['delta_full'] != 0 else 0.0)
            print(f"    N={r[0]:>3} ({r[2]:>5}): variance fraction "
                  f"{vf:.4f}, predicted {r[3][key]*100:>+7.2f}%, "
                  f"empirical {r[4]*100:>+7.2f}%")
        print(f"  Average J-solid variance fraction: {avg_var_frac:.4f}")
        print(f"  Target: 0.40")

    # --- Pattern-shape diagnostic for each variant ----------------------
    print()
    print("=" * 130)
    print("PATTERN-SHAPE DIAGNOSTIC — does any variant produce empirical "
          "monotonic INCREASE N=5→10?")
    print("=" * 130)
    print("  Empirical magnitude:        N=5: 12.16,  N=7: 29.50,  "
          "N=8: 31.81,  N=9: 33.14,  N=10: 33.58  (monotonic INCREASE)")

    axial_rows = [r for r in rows if r[0] in (5, 7, 8, 9, 10)]
    for variant_label, key in [('B-B1 (all m≠0)',  'delta_BB1'),
                                ('B-B2 (m=2 only)', 'delta_BB2'),
                                ('B-B3 (radial m≠0)', 'delta_BB3')]:
        magnitudes = [abs(r[3][key]) * 100 for r in axial_rows]
        Ns = [r[0] for r in axial_rows]
        print(f"\n  {variant_label}:")
        print(f"    " + ", ".join(f"N={N}: {m:.2f}" for N, m in zip(Ns, magnitudes)))
        # Check monotonic increase from N=5 to N=10
        is_monotonic_inc = all(magnitudes[i] <= magnitudes[i+1] + 1e-3
                                for i in range(len(magnitudes)-1))
        is_monotonic_dec = all(magnitudes[i] >= magnitudes[i+1] - 1e-3
                                for i in range(len(magnitudes)-1))
        if is_monotonic_inc:
            print(f"    Monotonic INCREASE — matches empirical.")
        elif is_monotonic_dec:
            print(f"    Monotonic DECREASE — anti-correlated with empirical.")
        else:
            print(f"    Non-monotonic — does not match empirical monotonic "
                  f"increase.")


if __name__ == '__main__':
    main()
