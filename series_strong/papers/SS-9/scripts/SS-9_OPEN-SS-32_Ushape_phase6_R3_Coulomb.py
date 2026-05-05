"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 6 R3-Coulomb scoping.

Session 17 Phase 5 (Sessions 17 close, patches 0185-0189) established that R3
(uniform R_α(N) shift) and R4 (cluster shape distortion) PASS SCOPING under
all three falsifier criteria — F1 sign by Gaussian symmetry, F2 magnitude
capacity well above empirical scale, F3 pattern monotonic for any monotonic
δR(N).  R3 and R4 advanced to multi-session derivation status.  The Phase 5
forward pointer (sketch §6.1) registered four candidate physics for R3 δR(N)
specification:
  (R3-Coulomb)  cluster Coulomb repulsion driving R_α outward
  (R3-Pauli)    Pauli blocking at internal alpha-alpha contacts
  (R3-surface)  alternative surface-density forms (NOT R1 surface-tension)
  (R4-shape)    spin-orbit cluster contributions with shape dependence

Phase 5 sketch §6.1 designated R3-Coulomb as the natural Session 18 first move:
"compute Coulomb-driven equilibrium δR(N) using simplified CPP charge model,
compare to Phase 5 R3-lin calibration (δR(10) ≈ 1 fm), assess whether Coulomb
alone, Pauli alone, or both together come close."  This script executes that
investigation.

PHASE 5 LESSON CARRIED FORWARD: F1 sign analytical check FIRST, before
computation.  For R3-Coulomb the sign argument is one paragraph composed of
two analytical results:
  (i)  Coulomb between same-sign charges (alpha = +2e) is repulsive → drives
       cluster expansion → δR_Coulomb > 0
  (ii) Phase 5 sign theorem: any δR ≠ 0 gives ΔE_R3 = B_pair · [1 -
       exp(-δR²/(2σ²))] > 0 per edge (Gaussian symmetry).
  Composition: δR_Coulomb > 0 → ΔE_R3 > 0 = empirical-required sign.
  F1 PASSES analytically for R3-Coulomb.

Computation tests F2 magnitude (does Coulomb-driven δR(10) match Phase 5
R3-lin target ≈ 1.05 fm?) and F3 pattern (monotonic in N across J-solid?).

OPERATIONAL DEFINITIONS

Simplified CPP charge model.  Each alpha cluster is a point charge q_α = +2e
at its J-solid vertex.  Inter-cluster Coulomb energy:

    V_C(R_α) = (2e)² · Σ_{pairs i<j} 1/r_ij(R_α)

where r_ij(R_α) is the alpha-alpha pair separation in the J-solid at edge
length R_α.  Convention: e²·k_C = 1.44 MeV·fm (Coulomb constant in nuclear
units), so (2e)²·k_C = 5.76 MeV·fm.

For uniform expansion δR (all distances scale by (R_α + δR)/R_α from canonical
R_α):
    V_C(δR) = V_C(0) · R_α / (R_α + δR)
where V_C(0) ≡ V_C(R_α = canonical = 2.37 fm).

K_3 binding for nearest-neighbor (edge) pairs at non-canonical separation:
    V_K3(δR) = -|E| · B_pair · exp(-δR²/(2σ²))

Total potential energy as function of δR:
    V_total(δR) = V_C(0) · R_α/(R_α + δR) - |E| · B_pair · exp(-δR²/(2σ²))

Force balance ∂V/∂(δR) = 0 at equilibrium:

    |E| · B_pair · (δR/σ²) · exp(-δR²/(2σ²))   =   V_C(0) · R_α/(R_α + δR)²
    [K_3 restoring force pulling δR back to 0]      [Coulomb push for expansion]

Solve numerically for δR_eq per polytope.

EMPIRICAL TARGETS

Phase 5 R3-lin calibration (sketch §3.3):
    δR(N=10) = 1.052 fm = 44.4% of R_canon
    α = 0.1753 fm/(N-4 unit) for δR(N) = α(N-4)
    Target: ΔE/α = 1 MeV at N=10

Phase 5 R3-emp (using empirical R_pct from Session 12 R1 inversion):
    δR(N=5..10) = 0.346, 0.453, 0.500, 0.529, 0.538 fm

We compare δR_Coulomb(N) to both targets.

FALSIFIERS

  F1 (sign): δR_Coulomb > 0 universally.  PASSES analytically (above).
  F2 (magnitude): δR_Coulomb(10) compared to R3-lin target 1.05 fm.
                  If within factor of 2-3, magnitude-compatible.
                  If much smaller, Coulomb alone insufficient (Pauli/etc
                  needed).  If much larger, Coulomb overshoots (other
                  attractive physics needed to compensate).
  F3 (pattern):  δR_Coulomb(N) monotonic in N within J-solid range?
                  How does the functional shape compare?

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase6_R3_Coulomb.md

Inheritance: polytopes, edge construction, m_α / B_pair / R_α / σ_K3 constants
from Phase 5; analytical sign-check methodology lesson from Phase 4 / Phase 5
handover.
"""

import math
import numpy as np
from scipy.optimize import minimize, brentq


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 5)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790
B_pair       = M_0 / phi
m_n          = 939.565
m_alpha      = 3727.4
hbar_c       = 197.327
R_alpha      = 2.37
sigma_K3_canon = 1.68

# Coulomb in nuclear units: k_C · e² = 1.44 MeV·fm; alpha charge q = 2e
# So Coulomb prefactor for alpha-alpha pair = (2e)² · k_C = 5.76 MeV·fm
COULOMB_AA = 4 * 1.44   # = 5.76 MeV·fm


# ---------------------------------------------------------------------------
# Polytope construction (verbatim from Phase 5)
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
# Coulomb energy: simplified CPP charge model (alpha = point charge +2e)
# ---------------------------------------------------------------------------
def compute_coulomb_energy(verts, coulomb_pre=COULOMB_AA):
    """V_C(0) = (2e)² · Σ_{pairs} 1/r_ij at canonical geometry.

    Sums over ALL alpha-alpha pairs (not just nearest-neighbor edges) because
    Coulomb is long-range and all pairs feel the repulsion.  In contrast,
    K_3 binding is only at edge (nearest-neighbor) pairs — captured by |E|
    in the K_3 term elsewhere.

    Returns: V_C(0) in MeV at canonical R_α = 2.37 fm geometry.
    """
    n = len(verts)
    V_C = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r_ij = np.linalg.norm(verts[i] - verts[j])
            V_C += coulomb_pre / r_ij
    return V_C


def pair_distances_summary(verts):
    """Return list of (count, distance) pairs for unique pair distances."""
    n = len(verts)
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            r_ij = np.linalg.norm(verts[i] - verts[j])
            distances.append(r_ij)
    distances.sort()
    # bin to nearest 1%
    binned = {}
    for d in distances:
        key = round(d, 2)
        binned[key] = binned.get(key, 0) + 1
    return [(c, d) for d, c in sorted(binned.items())]


# ---------------------------------------------------------------------------
# Equilibrium δR_Coulomb solver
# ---------------------------------------------------------------------------
def force_balance(delta_R, V_C0, n_edges, sigma_K3=sigma_K3_canon,
                  R_canon=R_alpha):
    """Net force on δR coordinate (positive = wants to increase δR).

    F(δR) = K_3 restoring + Coulomb push
          = -|E|·B_pair·(δR/σ²)·exp(-δR²/(2σ²)) + V_C(0)·R_canon/(R+δR)²

    At δR=0: F(0) = +V_C(0)/R_canon > 0 (cluster wants to expand).
    At δR=δR_eq: F = 0 (force balance).
    For δR > δR_eq: F < 0 (K_3 force restores).

    Convention: F > 0 means net force pushes δR larger.
    """
    K3_restoring = -n_edges * B_pair * (delta_R / sigma_K3**2) * \
                   math.exp(-delta_R**2 / (2 * sigma_K3**2))
    coulomb_push = V_C0 * R_canon / (R_canon + delta_R)**2
    return K3_restoring + coulomb_push


def solve_equilibrium(V_C0, n_edges, sigma_K3=sigma_K3_canon,
                      R_canon=R_alpha, search_max=10.0):
    """Solve force_balance(δR) = 0 for the equilibrium δR_eq.

    F(0) = V_C(0)/R_canon > 0  (always, for V_C > 0)
    For large δR, K_3 restoring grows then decays via exp(-δR²/(2σ²)),
    while Coulomb decays as 1/(R+δR)².  We need to find the FIRST
    crossing where F changes from + to -.

    Strategy: F(δR) starts positive at δR=0; bracket the first negative
    value by stepping out, then bisect.
    """
    # Step out to find first sign change
    n_steps = 1000
    delta_step = search_max / n_steps
    prev_F = force_balance(0.0, V_C0, n_edges, sigma_K3, R_canon)
    if prev_F <= 0:
        return 0.0  # already at or past equilibrium
    for k in range(1, n_steps + 1):
        delta_R = k * delta_step
        F = force_balance(delta_R, V_C0, n_edges, sigma_K3, R_canon)
        if F < 0:
            # Bracket [delta_R - delta_step, delta_R]
            try:
                root = brentq(force_balance,
                              delta_R - delta_step, delta_R,
                              args=(V_C0, n_edges, sigma_K3, R_canon),
                              xtol=1e-6)
                return root
            except ValueError:
                return delta_R
    return None  # no crossing found


def potential_energy(delta_R, V_C0, n_edges, sigma_K3=sigma_K3_canon,
                     R_canon=R_alpha):
    """V_total(δR) = V_C(δR) + V_K3(δR), measured from equilibrium-at-canonical.

    V_C(δR)  = V_C(0) · R_canon/(R_canon + δR)   [decreases with expansion]
    V_K3(δR) = -|E|·B_pair·exp(-δR²/(2σ²))        [becomes less negative]
    """
    V_C = V_C0 * R_canon / (R_canon + delta_R)
    V_K3 = -n_edges * B_pair * math.exp(-delta_R**2 / (2 * sigma_K3**2))
    return V_C + V_K3


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 130)
    print("SS-9 OPEN-SS-32 ↔ U-shape — Phase 6 R3-Coulomb scoping")
    print("=" * 130)
    print()

    print("Q: Does Coulomb-driven equilibrium δR(N) come close to Phase 5")
    print("   R3-lin calibration target (δR(10) ≈ 1 fm) in magnitude and")
    print("   pattern across J-solid range?")
    print()
    print("Phase 5 lesson applied (per 0189 handover): F1 sign analytical check")
    print("FIRST, before computation.")
    print()
    print("Pre-empted F1 sign argument (composition of two analytical results):")
    print("  (i)  Coulomb between alpha clusters (each charge +2e) is")
    print("       repulsive → drives cluster expansion → δR_Coulomb > 0.")
    print("  (ii) Phase 5 sign theorem: any δR ≠ 0 gives ΔE_R3 = B_pair ·")
    print("       [1 - exp(-δR²/(2σ²))] > 0 per edge (Gaussian symmetry).")
    print("  Composition: δR_Coulomb > 0 → ΔE_R3 > 0 = empirical-required.")
    print("  F1 PASSES analytically for R3-Coulomb.")
    print()
    print("Computation tests F2 magnitude and F3 pattern only.")
    print()

    polys = [
        (4,  poly_4,  'tetrahedron',         'T_d'),
        (5,  poly_5,  'trig. bipyramid',     'D_3h'),
        (6,  poly_6,  'octahedron',          'O_h'),
        (7,  poly_7,  'pentagonal bipyramid','D_5h'),
        (8,  poly_8,  'snub disphenoid',     'D_2d'),
        (9,  poly_9,  'triaug. tri. prism',  'D_3h'),
        (10, poly_10, 'gyroel. sq. bipyr.',  'D_4d'),
        (12, poly_12, 'icosahedron',         'I_h'),
    ]

    print(f"Constants: B_pair = {B_pair:.3f} MeV, R_canon = {R_alpha} fm, "
          f"σ_K3 = {sigma_K3_canon} fm, (2e)²·k_C = {COULOMB_AA} MeV·fm")
    print()

    # ---- Pair distance summary ---------------------------------------
    print("Pair-distance structure per polytope (canonical R_α = 2.37 fm):")
    print(f"  {'N':>3} {'sym':>5} {'|E|':>3} {'#pairs':>6} "
          f"{'unique pair distances [fm], (count×distance)':<60}")
    print("  " + "-"*120)
    cluster_data = []
    for N, fn, name, sym in polys:
        v = fn()
        edges = build_edges(v)
        if len(edges) != 3*N - 6:
            print(f"  WARN N={N}: |E|={len(edges)} != 3N-6={3*N-6}")
        n_pairs = N*(N-1)//2
        pair_summary = pair_distances_summary(v)
        # format: "6×2.37" etc.
        pair_str = ", ".join(f"{c}×{d:.2f}" for c, d in pair_summary)
        print(f"  {N:>3} {sym:>5} {len(edges):>3} {n_pairs:>6}  {pair_str}")
        cluster_data.append((N, name, sym, v, edges))
    print()

    # ---- V_C(0) per polytope -----------------------------------------
    print("Coulomb energy V_C(0) at canonical geometry (point-charge alphas):")
    print(f"  {'N':>3} {'sym':>5} {'V_C [MeV]':>11} "
          f"{'V_C/pair [MeV]':>16} {'V_C(SEMF) [MeV]':>17} {'ratio':>8}")
    print("  " + "-"*90)
    for N, name, sym, v, edges in cluster_data:
        V_C0 = compute_coulomb_energy(v)
        Z = 2 * N  # 2 protons per alpha
        A = 4 * N
        V_C_SEMF = 0.711 * Z**2 / A**(1.0/3.0) if A > 0 else 0
        n_pairs = N*(N-1)//2
        V_C_per_pair = V_C0 / n_pairs if n_pairs > 0 else 0
        ratio = V_C0 / V_C_SEMF if V_C_SEMF > 1e-6 else 0
        print(f"  {N:>3} {sym:>5} {V_C0:>11.3f} {V_C_per_pair:>16.4f} "
              f"{V_C_SEMF:>17.3f} {ratio:>8.3f}")
    print()
    print("  V_C(SEMF) = 0.711·Z²/A^(1/3) is the bulk-Coulomb estimate from")
    print("  uniform-charge SEMF.  Our point-charge V_C(0) treats each alpha")
    print("  as +2e at its J-solid vertex; ratio V_C(point) / V_C(SEMF)")
    print("  reflects the difference between vertex-localized and uniform-")
    print("  distributed charge models — both are simplifications.")
    print()

    # ---- Equilibrium δR_Coulomb --------------------------------------
    print("Equilibrium δR_Coulomb solving K_3 + Coulomb force balance:")
    print(f"  {'N':>3} {'sym':>5} {'V_C [MeV]':>11} "
          f"{'|E|·B_pair':>11} {'δR_C [fm]':>10} {'δR_C/R_α':>10} "
          f"{'ΔE_K3 [MeV]':>13} {'ΔE/α [MeV]':>12} {'R3-lin tgt':>12}")
    print("  " + "-"*120)

    # R3-lin target from Phase 5: δR(N) = 0.1753·(N-4) fm
    alpha_lin = 0.1753

    r3c_results = []
    for N, name, sym, v, edges in cluster_data:
        n_edges = len(edges)
        V_C0 = compute_coulomb_energy(v)
        delta_R = solve_equilibrium(V_C0, n_edges)
        if delta_R is None:
            print(f"  {N:>3} {sym:>5} (no equilibrium)")
            continue

        # K_3 binding loss at this δR
        delta_E_K3 = n_edges * B_pair * (1 - math.exp(
            -delta_R**2 / (2 * sigma_K3_canon**2)))
        delta_E_per_alpha = delta_E_K3 / N

        # R3-lin target
        delta_R_target = alpha_lin * max(0, N - 4)

        EE_B = n_edges * B_pair
        print(f"  {N:>3} {sym:>5} {V_C0:>11.3f} {EE_B:>11.3f} "
              f"{delta_R:>10.4f} {delta_R/R_alpha:>10.4f} "
              f"{delta_E_K3:>13.4f} {delta_E_per_alpha:>12.4f} "
              f"{delta_R_target:>12.4f}")
        r3c_results.append((N, sym, V_C0, delta_R, delta_E_K3,
                            delta_E_per_alpha, delta_R_target))
    print()

    # ---- F2 magnitude analysis ---------------------------------------
    print("F2 magnitude analysis: δR_Coulomb vs Phase 5 R3-lin target")
    print(f"  {'N':>3} {'sym':>5} {'δR_C [fm]':>10} {'R3-lin [fm]':>12} "
          f"{'ratio':>8} {'δR_C - tgt [fm]':>16}")
    for (N, sym, V_C0, delta_R, _, _, delta_R_target) in r3c_results:
        ratio = delta_R / delta_R_target if delta_R_target > 1e-3 else 0
        diff = delta_R - delta_R_target
        print(f"  {N:>3} {sym:>5} {delta_R:>10.4f} {delta_R_target:>12.4f} "
              f"{ratio:>8.3f} {diff:>+16.4f}")
    print()

    # ---- F3 pattern analysis -----------------------------------------
    print("F3 pattern analysis: monotonicity of δR_Coulomb in N "
          "(J-solid range only)")
    j_solid = [(N, dr) for (N, _, _, dr, _, _, _) in r3c_results
               if N in (5, 7, 8, 9, 10)]
    print(f"  N    δR_Coulomb [fm]")
    for N, dr in j_solid:
        print(f"  {N:<3}  {dr:.4f}")
    monotonic = all(j_solid[i+1][1] > j_solid[i][1]
                    for i in range(len(j_solid) - 1))
    print(f"  Monotonically increasing in N? "
          f"{'YES' if monotonic else 'NO'}")
    print()

    # ---- Compare functional shape to R3-lin ----------------------
    print("Functional shape comparison: δR_Coulomb(N) vs R3-lin α(N-4):")
    print("  R3-lin uses constant α = 0.1753 fm/(N-4 unit) by construction.")
    print("  Best-fit α_C from Coulomb result (least-squares over J-solids):")
    if len(j_solid) >= 2:
        # Fit δR_C = α_C · (N - 4)
        Ns = np.array([N for N, _ in j_solid], dtype=float)
        drs = np.array([dr for _, dr in j_solid])
        Nmin = 4.0
        # Solve α_C minimizing Σ (α_C·(N-Nmin) - dr)²
        x = Ns - Nmin
        alpha_C = float(np.sum(x * drs) / np.sum(x * x))
        # Residuals
        residuals = drs - alpha_C * x
        print(f"  α_C = {alpha_C:.4f} fm/(N-4 unit)  vs  α_target = "
              f"{alpha_lin:.4f}  (ratio {alpha_C/alpha_lin:.3f})")
        print(f"  Residuals at N=5,7,8,9,10: "
              f"{', '.join(f'{r:+.4f}' for r in residuals)} fm")
    print()

    # ---- Verdict ----------------------------------------------------
    print("=" * 130)
    print("VERDICT")
    print("=" * 130)
    print()
    print("F1 (sign): R3-Coulomb PASSES analytically by composition.")
    print("           Coulomb repulsion → δR > 0 → Phase 5 sign theorem →")
    print("           ΔE_R3 > 0 = empirical-required.  No computation needed.")
    print()
    if r3c_results:
        # extract δR(N=10) for verdict
        n10_res = [r for r in r3c_results if r[0] == 10]
        if n10_res:
            dR10 = n10_res[0][3]
            ratio10 = dR10 / 1.052
            print(f"F2 (magnitude): δR_Coulomb(N=10) = {dR10:.3f} fm vs Phase")
            print(f"                5 R3-lin target 1.052 fm; ratio "
                  f"{ratio10:.2f}.")
            if 0.5 <= ratio10 <= 2.0:
                print("                MAGNITUDE-COMPATIBLE — within factor 2 "
                      "of target.")
            elif ratio10 < 0.5:
                print("                MAGNITUDE-INSUFFICIENT — Coulomb alone")
                print("                undershoots target; needs additional ")
                print("                physics (Pauli, surface-density, etc).")
            else:
                print("                MAGNITUDE-OVERSHOOTS — Coulomb gives")
                print("                more than target; would need other")
                print("                attractive physics to compensate.")
        print()
    if monotonic:
        print("F3 (pattern): δR_Coulomb(N) MONOTONIC in N across J-solid range.")
        print("              Pattern-compatible with empirical monotonic-in-N ")
        print("              U-shape signature.")
    else:
        print("F3 (pattern): δR_Coulomb(N) NOT MONOTONIC across J-solid range.")
        print("              Pattern-incompatible — F3 fails.")
    print()
    print("Phase 6 outcome depends on F2/F3 results above.  See companion")
    print("sketch §4 for full verdict and forward pointers.")
    print()


if __name__ == '__main__':
    main()
