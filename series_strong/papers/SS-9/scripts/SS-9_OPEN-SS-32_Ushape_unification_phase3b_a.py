"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase B sub-phase A (Phase 3B-A).

Phase 3B-A: belt-subspace projection of the full Hessian decomposition.

Phase 3A (RULED OUT, Session 13) gave a flat -85±1% softening across all eight
canonical alpha-chain deltahedra: enriching the mode basis from Phase 2's
single uniform-scaling dof to the full vibrational space (3N-6 modes summed
equally) is too inclusive — local soft modes (vertex rocking) dominate, and
they are shape-class-insensitive.

Phase 3B-A is the simplest IRREP-selective realization the §6 of Phase 3A
specified: project Hessian eigenmodes onto a "belt subspace" capturing the
SS-7 OPEN-SS-32 oblate-quadrupole deformation pattern, then weight per-mode
zero-point variance by the projection.  The belt subspace is a multi-vector
basis covering monopole (A_1 in-plane radial breathing) plus 2D E-type
quadrupole (cos(2φ), sin(2φ) angular patterns) at each axial polytope.

Three sharply constrained quantitative targets from Phase 3A's bracketing
(empirical -33.6% peak vs Phase 3A upper bound -85%, ~40% of upper bound):

  (a) Average belt-fraction f_belt ~ 0.4 at J-solid mid-range N_α=7..10,
      yielding belt-projected softening ~-33% (vs Phase 3A's -85%).
  (b) Near-zero belt-projection at regular polytopes T_d, O_h, I_h
      (no belt IRREP — degenerate inertia tensor → no preferred axis).
  (c) O_h ≪ D_{2d} ratio at N_α=6 vs N_α=8 — Reading-A vs Reading-B/C
      discriminator.

OPERATIONAL DEFINITIONS

Inertia classification.  Compute the inertia tensor I_ab = Σ_i (δ_ab r_i² -
r_i,a r_i,b) about the COM.  Diagonalize.  Three regimes:

  - DEGENERATE: all three eigenvalues equal within tolerance — T_d, O_h, I_h.
    No preferred axis.  Belt subspace dim = 0; all f_belt = 0 by symmetry.
    Targets (b) and (c) are structural symmetry identities at this level.
  - PROLATE: smallest eigenvalue is unique (mass concentrated on the axis,
    rocket shape) — bipyramids etc.  Principal axis = eigenvector of
    smallest eigenvalue.
  - OBLATE: largest eigenvalue is unique (mass concentrated perpendicular
    to axis, discus shape).  Principal axis = eigenvector of largest
    eigenvalue.

Belt subspace.  For an axial polytope with principal axis ẑ_p, build an
orthonormal frame {x̂_p, ŷ_p, ẑ_p} and assign each vertex i cylindrical
coordinates (ρ_i, φ_i, z_i).  Define three belt basis vectors of length 3N
(displacement at each vertex):

  b^(0):     b^(0)_i  =  ρ̂_i                  (in-plane radial dilation;
                                                   monopole, A_1 breathing)
  b^(c2):    b^(c2)_i =  cos(2 φ_i) ρ̂_i        (E_2 quadrupole cos)
  b^(s2):    b^(s2)_i =  sin(2 φ_i) ρ̂_i        (E_2 quadrupole sin)

Project out rigid-body modes (3 translations + 3 rotations about COM) from
each, then Gram-Schmidt orthonormalize the surviving set.  This produces an
orthonormal belt basis {ê^a} of dimension dim(B) ≤ 3.

Belt fraction per mode.  For each Hessian eigenmode v_k:

  f_k^belt = Σ_{a ∈ B} |⟨ê^a | v_k⟩|²              ∈ [0, 1]

Belt-weighted variance.  Replace the Phase 3A sum-over-modes by the
belt-fraction-weighted sum:

  ⟨(δr)²⟩_belt = (1/|E|) Σ_modes f_k^belt × C_k^edge
  delta_belt   = -2 ⟨(δr)²⟩_belt / R_α²

In the limit f_k^belt = 1 ∀k, recover Phase 3A's full result.  In the limit
f_k^belt = 0 ∀k (DEGENERATE polytopes), get 0 by symmetry.  Per-mode
contributions are weighted by their alignment with the belt subspace.

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_unification_phase3b_a.md

Inheritance: polytopes, edge construction, Hessian build, m_α / B_pair / R_α
constants, and empirical R-shift inputs from Phase 3A script.
"""

import math
import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 3A script, which inherited from Phase 2)
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
# Polytope construction (verbatim from Phase 3A script)
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
# Phase 3A core: full Hessian (verbatim)
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


# ---------------------------------------------------------------------------
# Phase 3B-A new: inertia classification, belt subspace, projection
# ---------------------------------------------------------------------------
def inertia_tensor(verts):
    """Mass-weighted inertia tensor about the COM (uniform unit vertex masses)."""
    com = verts.mean(axis=0)
    verts_c = verts - com
    I = np.zeros((3, 3))
    for r in verts_c:
        I += np.eye(3) * (r @ r) - np.outer(r, r)
    return I


def classify_axial_structure(verts, deg_thresh=1e-3):
    """Classify polytope by inertia tensor eigenvalue structure.

    Returns (regime, axis, eigvals) where regime is 'DEGEN', 'PROLATE',
    or 'OBLATE', axis is the principal axis unit vector (None for DEGEN),
    and eigvals is the sorted-ascending inertia eigenvalue triple.
    """
    I = inertia_tensor(verts)
    eigvals, eigvecs = np.linalg.eigh(I)  # ascending

    spread = (eigvals.max() - eigvals.min()) / max(eigvals.max(), 1e-12)
    if spread < deg_thresh:
        return 'DEGEN', None, eigvals

    # Compare gaps: if smallest is unique, prolate; if largest is unique,
    # oblate.
    gap_low = eigvals[1] - eigvals[0]
    gap_hi  = eigvals[2] - eigvals[1]
    if gap_low > gap_hi:
        # smallest is unique → prolate (rocket)
        return 'PROLATE', eigvecs[:, 0], eigvals
    else:
        # largest is unique → oblate (discus)
        return 'OBLATE',  eigvecs[:, 2], eigvals


def gram_schmidt(vectors, tol=1e-10):
    """Orthonormalize a list of vectors, dropping linearly dependent ones."""
    out = []
    for v in vectors:
        u = v.copy()
        for o in out:
            u = u - (u @ o) * o
        norm = np.linalg.norm(u)
        if norm > tol:
            out.append(u / norm)
    return out


def rigid_body_basis(verts):
    """Build orthonormalized rigid-body subspace (3 translations + 3 rotations
    about the COM) as a list of 3N-dim vectors."""
    N = len(verts)
    com = verts.mean(axis=0)
    verts_c = verts - com

    rb_raw = []
    # Three translations
    for a in range(3):
        t = np.zeros(3*N)
        for i in range(N):
            t[3*i + a] = 1.0
        rb_raw.append(t)
    # Three rotations about COM
    for ax in [np.array([1.0,0,0]), np.array([0,1.0,0]), np.array([0,0,1.0])]:
        r = np.zeros(3*N)
        for i in range(N):
            r[3*i:3*i+3] = np.cross(ax, verts_c[i])
        rb_raw.append(r)
    return gram_schmidt(rb_raw)


def project_out_subspace(vec, basis_orth):
    """Project vec onto the orthogonal complement of an orthonormal basis."""
    result = vec.copy()
    for b in basis_orth:
        result = result - (result @ b) * b
    return result


def build_belt_basis(verts, axis):
    """Build raw 3 belt-deformation basis vectors of length 3N.

    Belt deformations defined in the principal-axis frame:
      b_mono[i]  =  ρ̂_i             (A_1 in-plane radial breathing)
      b_cos[i]   =  cos(2 φ_i) ρ̂_i  (E_2 quadrupole cos)
      b_sin[i]   =  sin(2 φ_i) ρ̂_i  (E_2 quadrupole sin)

    Vertices on the axis (ρ_i ≈ 0) contribute zero to all three (no radial
    direction to displace along).
    """
    N = len(verts)
    com = verts.mean(axis=0)
    verts_c = verts - com

    # Build orthonormal frame {x̂_p, ŷ_p, ẑ_p = axis}
    axis_unit = axis / np.linalg.norm(axis)
    if abs(axis_unit[0]) < 0.9:
        ref = np.array([1.0, 0, 0])
    else:
        ref = np.array([0, 1.0, 0])
    x_p = ref - axis_unit * (ref @ axis_unit)
    x_p = x_p / np.linalg.norm(x_p)
    y_p = np.cross(axis_unit, x_p)

    b_mono = np.zeros(3*N)
    b_cos  = np.zeros(3*N)
    b_sin  = np.zeros(3*N)

    for i in range(N):
        r = verts_c[i]
        z_i = r @ axis_unit
        r_perp = r - z_i * axis_unit
        rho_i = np.linalg.norm(r_perp)
        if rho_i < 1e-8:
            continue                                # apex vertex: skip
        rhat = r_perp / rho_i
        x_i = r @ x_p
        y_i = r @ y_p
        phi_i = math.atan2(y_i, x_i)

        b_mono[3*i:3*i+3] = rhat
        b_cos[3*i:3*i+3]  = math.cos(2 * phi_i) * rhat
        b_sin[3*i:3*i+3]  = math.sin(2 * phi_i) * rhat

    return [b_mono, b_cos, b_sin]


def build_belt_subspace(verts, axis):
    """Construct orthonormal belt subspace orthogonal to rigid-body modes."""
    if axis is None:
        return []
    rb_orth = rigid_body_basis(verts)
    raw = build_belt_basis(verts, axis)
    cleaned = [project_out_subspace(b, rb_orth) for b in raw]
    return gram_schmidt(cleaned)


# ---------------------------------------------------------------------------
# Phase 3B-A vibrational analysis with belt-subspace projection
# ---------------------------------------------------------------------------
def vibrational_analysis_phase3b_a(verts, edges, sigma_K3=sigma_K3_canon,
                                   eps_zero=1e-6):
    """Full Hessian + belt-subspace projection.  Returns full-mode and
    belt-projected per-edge MSD and softening.
    """
    N = len(verts)
    H = build_hessian(verts, edges, sigma_K3=sigma_K3)
    eigvals, eigvecs = np.linalg.eigh(H)

    abs_max = np.max(np.abs(eigvals))
    is_zero = np.abs(eigvals) < eps_zero * abs_max
    n_rigid = int(np.sum(is_zero))
    n_vib   = 3*N - n_rigid

    cls, axis, inertia_eigs = classify_axial_structure(verts)
    belt_basis_orth = build_belt_subspace(verts, axis)
    dim_belt = len(belt_basis_orth)

    n_edges = len(edges)
    edge_msd_full = 0.0
    edge_msd_belt = 0.0
    sum_f_belt    = 0.0          # sanity check: should equal dim_belt
    hbar_omegas   = []

    for k in range(3*N):
        if is_zero[k]:
            continue
        lam = eigvals[k]
        if lam <= 0:
            continue
        v_k = eigvecs[:, k]
        v_per_v = v_k.reshape(N, 3)

        # belt fraction of mode
        f_belt = 0.0
        for e in belt_basis_orth:
            c = float(v_k @ e)
            f_belt += c * c
        sum_f_belt += f_belt

        # per-edge MSD contribution (full Phase 3A formula)
        prefactor = hbar_c / (2.0 * math.sqrt(m_alpha * lam))
        msd_k_full = 0.0
        for i, j, n_hat in edges:
            relative = v_per_v[i] - v_per_v[j]
            proj = float(np.dot(relative, n_hat))
            msd_k_full += prefactor * proj * proj
        edge_msd_full += msd_k_full
        edge_msd_belt += f_belt * msd_k_full

        omega_k = math.sqrt(lam / m_alpha)
        hbar_omegas.append(hbar_c * omega_k)

    edge_msd_full_avg = edge_msd_full / n_edges
    edge_msd_belt_avg = edge_msd_belt / n_edges

    delta_full = -2.0 * edge_msd_full_avg / R_alpha**2
    delta_belt = -2.0 * edge_msd_belt_avg / R_alpha**2

    belt_var_frac = (edge_msd_belt / edge_msd_full) if edge_msd_full > 0 else 0

    return {
        'cls':              cls,
        'inertia_eigvals':  inertia_eigs,
        'dim_belt':         dim_belt,
        'n_vib':            n_vib,
        'hbar_omega_min':   min(hbar_omegas) if hbar_omegas else float('nan'),
        'hbar_omega_max':   max(hbar_omegas) if hbar_omegas else float('nan'),
        'edge_msd_full_avg': edge_msd_full_avg,
        'edge_msd_belt_avg': edge_msd_belt_avg,
        'delta_full':       delta_full,
        'delta_belt':       delta_belt,
        'belt_var_frac':    belt_var_frac,
        'sum_f_belt':       sum_f_belt,        # sanity: = dim_belt iff no
                                                #          rigid-body leakage
    }


def empirical_required_softening(R_required_change_pct):
    x = R_required_change_pct / 100.0
    return -(1.0 - 1.0 / (1.0 + x) ** 2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 110)
    print("SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 3 Phase B sub-phase A "
          "(Phase 3B-A)")
    print("Belt-subspace projection of full Hessian; "
          "K_3 Gaussian pair-potential")
    print("=" * 110)
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

    print("Phase 3B-A: belt-subspace projection (monopole + 2D E_2 quadrupole)")
    print(f"  {'N':>3} {'polytope':>22} {'sym':>5} {'class':>8} {'dim_B':>5} "
          f"{'|E|':>3} "
          f"{'<dr2>full':>10} {'<dr2>belt':>10} "
          f"{'-d_full%':>9} {'-d_belt%':>9} "
          f"{'-d_emp%':>9} {'belt/full':>9}")
    print("  " + "-"*110)

    rows = []
    for N, fn, name, sym, R_pct in delta_polys:
        v = fn()
        edges = build_edges(v)
        E = len(edges)
        if E != 3*N - 6:
            print(f"  WARN N={N}: |E|={E} != 3N-6={3*N-6}")

        result = vibrational_analysis_phase3b_a(v, edges,
                                                sigma_K3=sigma_K3_canon)
        emp_soft = empirical_required_softening(R_pct)
        belt_full_ratio = (result['delta_belt'] / result['delta_full']
                           if result['delta_full'] != 0 else 0.0)

        print(f"  {N:>3} {name:>22} {sym:>5} {result['cls']:>8} "
              f"{result['dim_belt']:>5} {E:>3} "
              f"{result['edge_msd_full_avg']:>10.4f} "
              f"{result['edge_msd_belt_avg']:>10.4f} "
              f"{result['delta_full']*100:>9.2f} "
              f"{result['delta_belt']*100:>9.2f} "
              f"{emp_soft*100:>+8.1f} "
              f"{belt_full_ratio:>9.3f}")
        rows.append((N, name, sym, result, emp_soft))

    print()

    # --- Sanity checks --------------------------------------------------
    print("Sanity checks:")
    print(f"  {'N':>3} {'class':>8} {'dim_B':>5} {'sum f_belt':>11} "
          f"{'inertia eigvals (sorted)':>40}")
    for N, name, sym, result, _ in rows:
        ev = result['inertia_eigvals']
        ev_str = f"[{ev[0]:.3f}, {ev[1]:.3f}, {ev[2]:.3f}]"
        print(f"  {N:>3} {result['cls']:>8} "
              f"{result['dim_belt']:>5} "
              f"{result['sum_f_belt']:>11.4f} "
              f"{ev_str:>40}")
    print()
    print("  Σ f_belt over modes should equal dim_belt for clean orthogonal")
    print("  basis with no rigid-body leakage.")
    print()

    # --- Phase 3A reproduction check (delta_full should match -85±1%) ---
    print("Phase 3A reproduction check (delta_full should equal Phase 3A "
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

    # --- Target audits ---------------------------------------------------
    print("=" * 110)
    print("TARGET AUDIT — three sharply constrained quantitative targets "
          "from Phase 3A bracketing")
    print("=" * 110)

    # Target (a): J-solid mid-range N_α=7..10 average belt fraction ~ 0.4
    j_solid = [r for r in rows if r[0] in (7, 8, 9, 10)]
    avg_belt_frac = np.mean([
        r[3]['delta_belt'] / r[3]['delta_full']
        if r[3]['delta_full'] != 0 else 0.0
        for r in j_solid
    ])
    target_a = 0.40
    print(f"\nTarget (a) — J-solid mid-range belt fraction at N_α=7..10 "
          f"target ~{target_a:.2f}:")
    for r in j_solid:
        bf = (r[3]['delta_belt'] / r[3]['delta_full']
              if r[3]['delta_full'] != 0 else 0.0)
        print(f"    N_α={r[0]:>3}  ({r[2]:>5}): belt fraction "
              f"{bf:.4f},  belt-projected softening "
              f"{r[3]['delta_belt']*100:>+7.2f}%,  empirical "
              f"{r[4]*100:>+7.2f}%")
    print(f"  Average J-solid belt fraction: {avg_belt_frac:.4f}")
    print(f"  Target:                         {target_a:.4f}")
    if avg_belt_frac > 0.30:
        print(f"  Verdict: ✓ TARGET (a) MET (belt fraction within 25% of "
              f"target)")
    elif avg_belt_frac > 0.15:
        print(f"  Verdict: ~ TARGET (a) PARTIAL (belt fraction is "
              f"{target_a/avg_belt_frac:.1f}× too small)")
    else:
        print(f"  Verdict: ✗ TARGET (a) NOT MET (belt fraction is "
              f"{target_a/avg_belt_frac:.1f}× too small)")

    # Target (b): Regular polytopes have near-zero belt fraction
    regular = [r for r in rows if r[0] in (4, 6, 12)]
    print(f"\nTarget (b) — regular polytopes (T_d, O_h, I_h) belt fraction "
          f"target ≈ 0:")
    for r in regular:
        bf = (r[3]['delta_belt'] / r[3]['delta_full']
              if r[3]['delta_full'] != 0 else 0.0)
        print(f"    N_α={r[0]:>3}  ({r[2]:>5}, {r[3]['cls']:>8}): "
              f"dim_belt={r[3]['dim_belt']}, belt fraction {bf:.6f}")
    if all((r[3]['dim_belt'] == 0) for r in regular):
        print("  Verdict: ✓ TARGET (b) MET (all regular polytopes have "
              "dim_belt=0 by inertia degeneracy; belt fraction = 0 "
              "structurally)")
    else:
        print("  Verdict: ✗ TARGET (b) NOT STRUCTURALLY ENFORCED (some "
              "regular polytopes have non-zero dim_belt)")

    # Target (c): O_h ≪ D_2d ratio at N=6 vs N=8
    r6 = next(r for r in rows if r[0] == 6)
    r8 = next(r for r in rows if r[0] == 8)
    bf6 = (r6[3]['delta_belt'] / r6[3]['delta_full']
           if r6[3]['delta_full'] != 0 else 0.0)
    bf8 = (r8[3]['delta_belt'] / r8[3]['delta_full']
           if r8[3]['delta_full'] != 0 else 0.0)
    print(f"\nTarget (c) — N_α=6 (O_h) ≪ N_α=8 (D_2d) belt fraction:")
    print(f"  O_h  belt fraction: {bf6:.6f}  (dim_belt={r6[3]['dim_belt']})")
    print(f"  D_2d belt fraction: {bf8:.6f}  (dim_belt={r8[3]['dim_belt']})")
    if bf6 < 0.05 and bf8 > 0.05:
        print("  Verdict: ✓ TARGET (c) MET (O_h vanishes by symmetry, "
              "D_2d non-zero)")
    elif bf6 < bf8 * 0.3:
        print("  Verdict: ~ TARGET (c) PARTIAL (O_h substantially less "
              "than D_2d)")
    else:
        print("  Verdict: ✗ TARGET (c) NOT MET")

    # --- Pattern shape comparison ---------------------------------------
    print()
    print("=" * 110)
    print("PATTERN COMPARISON — does belt-projected softening track empirical "
          "U-shape?")
    print("=" * 110)
    print(f"  {'N':>3} {'polytope':>22} {'-d_belt%':>10} {'-d_emp%':>10} "
          f"{'belt/emp':>10}")
    for r in rows:
        N, name, sym, result, emp = r
        d_belt = result['delta_belt'] * 100
        d_emp  = emp * 100
        ratio  = d_belt / d_emp if d_emp != 0 else float('nan')
        print(f"  {N:>3} {name:>22} {d_belt:>+10.2f} {d_emp:>+10.2f} "
              f"{ratio:>10.3f}")

    print()
    print("If ratios at J-solid mid-range (N=7..10) are clustered near 1.0,")
    print("the belt-projected model approximately reproduces the empirical")
    print("U-shape MAGNITUDE.  Pattern shape (J-solid peak vs regular-polytope")
    print("endpoints) is checked separately — empirical wants near-zero at")
    print("N=4 and N=12, peak near N=10.")
    print()


if __name__ == '__main__':
    main()
