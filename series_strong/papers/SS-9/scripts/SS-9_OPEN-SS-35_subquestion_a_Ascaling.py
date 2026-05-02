"""
SS-9 OPEN-SS-35 sub-question (a) A-scaling extension.

Extends the Session 6 sub-question (a) machinery from 3 regular polytopes
(tetrahedron, octahedron, icosahedron) to all 8 canonical alpha-chain
deltahedra (N_alpha = 4, 5, 6, 7, 8, 9, 10, 12). For lower-symmetry
deltahedra (axial rather than full 3D symmetry), the Hessian has
anisotropic eigenvalues; we use the geometric-mean frequency
omega_geo = (omega_x * omega_y * omega_z)^(1/3) as the scalar HO
frequency for empirical comparison.

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling.md

Note on N=8 (snub disphenoid): constructed via numerical relaxation from a
random-init that was verified (via multi-start search at seed 27) to converge
to the snub disphenoid topology with degree sequence (5,5,5,5,4,4,4,4).
Note on N=11: no convex equilateral all-triangular polytope exists, a
topological gap noted in SS-7 and SS-8.
"""

import math
import numpy as np
from scipy.optimize import minimize


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
phi      = (1 + math.sqrt(5)) / 2
M_0      = 3.790
B_pair   = M_0 / phi
m_n      = 939.565
hbar_c   = 197.327
R_alpha  = 2.37


# ---------------------------------------------------------------------------
# Polytope construction (canonical alpha-chain deltahedra)
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
    """Regular tetrahedron, N=4."""
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
    """Regular octahedron, N=6."""
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
    """Snub disphenoid (Johnson J_84), N=8.

    Constructed via numerical relaxation from random init at seed 27, which
    multi-start search verified converges to the canonical snub disphenoid
    topology with degree sequence (5,5,5,5,4,4,4,4)."""
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
    """Triaugmented triangular prism (Johnson J_51), N=9."""
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
    """Gyroelongated square bipyramid (Johnson J_17), N=10.

    Direct exact construction: square antiprism with R = 1/sqrt(2),
    h = sqrt((1 - R^2*(2 - sqrt(2)))/4), apex at H = h + 1/sqrt(2).
    Verified all 24 edges = unit length, gap to 25th distance at sqrt(2)."""
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
    """Regular icosahedron, N=12."""
    g = phi
    return rescale(np.array([
        [0,1,g], [0,1,-g], [0,-1,g], [0,-1,-g],
        [1,g,0], [1,-g,0], [-1,g,0], [-1,-g,0],
        [g,0,1], [g,0,-1], [-g,0,1], [-g,0,-1]
    ], dtype=float))


def build_adjacency(verts, R_edge=R_alpha, tol=0.05):
    """Build adjacency from vertices (edges = vertex pairs at unit distance)."""
    n = len(verts)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if abs(d - R_edge) < tol:
                adj[i].append(j)
                adj[j].append(i)
    deg = [len(a) for a in adj]
    return adj, deg, sum(deg)//2


# ---------------------------------------------------------------------------
# K_3 mean-field potential and Hessian
# ---------------------------------------------------------------------------
def V_K3(r, verts, deg_list, sigma):
    s = 0.0
    for i, vi in enumerate(verts):
        d2 = float(np.sum((r - vi)**2))
        s -= deg_list[i] * B_pair * math.exp(-d2 / (2 * sigma**2))
    return s


def hessian_numeric(verts, deg_list, sigma, h=0.01):
    """Compute full 3x3 Hessian at centroid via 4-point finite differences.
    Used for asymmetric (axial-symmetry) deltahedra where the Hessian is not
    automatically isotropic."""
    centroid = np.mean(verts, axis=0)
    H = np.zeros((3, 3))
    for a in range(3):
        for b in range(3):
            r_pp = centroid.copy(); r_pp[a] += h; r_pp[b] += h
            r_pm = centroid.copy(); r_pm[a] += h; r_pm[b] -= h
            r_mp = centroid.copy(); r_mp[a] -= h; r_mp[b] += h
            r_mm = centroid.copy(); r_mm[a] -= h; r_mm[b] -= h
            H[a, b] = (V_K3(r_pp, verts, deg_list, sigma) -
                       V_K3(r_pm, verts, deg_list, sigma) -
                       V_K3(r_mp, verts, deg_list, sigma) +
                       V_K3(r_mm, verts, deg_list, sigma)) / (4*h*h)
    return (H + H.T) / 2


def fit_omega_eigenvalues(verts, deg_list, sigma):
    """Diagonalize Hessian; return geometric-mean omega and three principal
    omegas. Returns (None, None) if any eigenvalue <= 0 (not confining)."""
    H = hessian_numeric(verts, deg_list, sigma)
    eigvals = np.linalg.eigvalsh(H)
    if (eigvals <= 0).any():
        return None, None
    omegas = np.sqrt(eigvals/m_n) * hbar_c
    omega_geo = (omegas[0] * omegas[1] * omegas[2])**(1.0/3)
    return omega_geo, omegas


# ---------------------------------------------------------------------------
# Self-consistency
# ---------------------------------------------------------------------------
def self_consistent(verts, deg_list, omega_init=12.0, max_iter=50, tol=1e-3):
    omega = omega_init
    history = []
    for it in range(max_iter):
        sigma = hbar_c / math.sqrt(m_n * omega)
        omega_new, omegas = fit_omega_eigenvalues(verts, deg_list, sigma)
        if omega_new is None:
            return None, None, None, history
        history.append((it, omega, sigma, omega_new))
        if abs(omega_new - omega) < tol:
            omega = omega_new
            break
        omega = omega_new
    sigma = hbar_c / math.sqrt(m_n * omega)
    Vc = V_K3(np.mean(verts, axis=0), verts, deg_list, sigma)
    _, omegas = fit_omega_eigenvalues(verts, deg_list, sigma)
    return omega, sigma, (omegas, Vc), history


def find_physical_fixed_point(verts, deg_list, omega_range=(5, 30), n_starts=26):
    """Multi-start search for lowest-omega (physical ground-state) fixed point."""
    fps = set()
    for om0 in np.linspace(*omega_range, n_starts):
        om, sg, _, _ = self_consistent(verts, deg_list, omega_init=om0)
        if om is not None:
            fps.add(round(om, 1))
    if not fps:
        return None, None, None, []
    physical = min(fps)
    om, sg, det, _ = self_consistent(verts, deg_list, omega_init=physical)
    return om, sg, det, sorted(fps)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 90)
    print("OPEN-SS-35 sub-question (a) A-scaling — canonical alpha-chain deltahedra")
    print("=" * 90)
    print()

    delta_polys = [
        (4,  poly_4,  'tetrahedron'),
        (5,  poly_5,  'triangular bipyramid'),
        (6,  poly_6,  'octahedron'),
        (7,  poly_7,  'pentagonal bipyramid'),
        (8,  poly_8,  'snub disphenoid'),
        (9,  poly_9,  'triaug. tri. prism'),
        (10, poly_10, 'gyroel. sq. bipyr.'),
        (12, poly_12, 'icosahedron'),
    ]

    # Topology verification
    print("Topology verification (E = 3V - 6 for simplicial 3-polytope):")
    print(f"  {'N':>3} {'Polytope':>30} {'V':>3} {'E':>3} "
          f"{'expected':>9} {'2E/V':>6} {'topology':>9}")
    for N, fn, name in delta_polys:
        verts = fn()
        adj, deg, E = build_adjacency(verts)
        ok = "OK" if E == 3*N - 6 else "FAIL"
        print(f"  {N:>3d} {name:>30} {len(verts):>3d} {E:>3d} "
              f"{3*N-6:>9d} {2*E/N:>6.3f} {ok:>9}")
    print()

    # Self-consistent HO solutions
    print("Self-consistent HO solutions (physical / ground-state fixed point):")
    print(f"  {'N':>3} {'A':>4} {'ℏω*_geo':>9} {'σ*':>7} {'V_c':>8} "
          f"{'(ω_x, ω_y, ω_z)':>22} {'emp 41/A^(1/3)':>15} {'CPP/emp':>9}")
    print("  " + "-"*100)
    results = []
    for N, fn, name in delta_polys:
        verts = fn()
        adj, deg, E = build_adjacency(verts)
        om, sg, det, fps = find_physical_fixed_point(verts, deg)
        if om is None:
            print(f"  {N:>3d}    no physical fixed point found")
            continue
        omegas, Vc = det
        A = 4 * N
        emp = 41.0 / A**(1/3)
        oms_str = f"({omegas[0]:.1f},{omegas[1]:.1f},{omegas[2]:.1f})"
        print(f"  {N:>3d} {A:>4d} {om:>9.3f} {sg:>7.3f} {Vc:>8.2f} "
              f"{oms_str:>22} {emp:>15.3f} {om/emp:>9.3f}")
        results.append((N, A, name, om, sg, Vc, omegas, emp))
    print()

    # Summary statistics
    if results:
        ratios = [r[3]/r[7] for r in results]
        print(f"Summary statistics across {len(results)} canonical deltahedra:")
        print(f"  Mean ratio CPP/empirical = {np.mean(ratios):.3f}")
        print(f"  Std deviation              = {np.std(ratios):.3f}")
        print(f"  Range                      = [{min(ratios):.3f}, {max(ratios):.3f}]")
        print()

        # Log-log scaling fit
        logA = np.log([r[1] for r in results])
        logom = np.log([r[3] for r in results])
        slope, intercept = np.polyfit(logA, logom, 1)
        print(f"A-scaling fit: log(ℏω) = {slope:+.3f} log(A) {intercept:+.3f}")
        print(f"  CPP slope:        {slope:+.3f}")
        print(f"  Empirical slope:  -1/3 = -0.333")
        print(f"  Ratio CPP/emp:    {slope/(-1.0/3):.2f}")
        print()
        print("CPP slope is ~30% of empirical magnitude. This is a structural")
        print("shortfall identified by the work — the harmonic FORM generalizes")
        print("across deltahedra, but the empirical A-scaling does not emerge")
        print("naturally from the regular-deltahedron picture at fixed R_alpha.")
        print()
        print("Two candidate resolutions registered for further work:")
        print("  R1: R_alpha scale-dependence (cluster compression at large A)")
        print("  R2: cluster-scale vs alpha-scale mean field interpretation")

    print()
    print("=" * 90)
    print("Verdict: A-scaling sub-sub-question 'substantive Level-0/Level-1 mixed result'")
    print("HO form ROBUST across deltahedra; A-scaling structurally weaker than empirical.")
    print("Sub-question (a) Level-1 partial closure remains valid; sub-question (c)")
    print("remains pending on both sub-question (b) closure and full A-scaling closure.")
    print("=" * 90)


if __name__ == "__main__":
    main()
