"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 9 R3-Coulomb Refinement C
(non-NN K_3 contributions, on top of Phase 8 Refinement A extended-charge Coulomb).

Session 20 Phase 8 (sketch §6.1 / 0204 handover) registered Session 21 Priority 1
as: "Refinement C — non-NN K_3 contributions. At r = sqrt(2) R_alpha = 3.35 fm,
K_3 Gaussian = 0.918 (NOT exponentially small). Per-pair K_3 binding 0.918 *
B_pair = 2.150 MeV (vs 2.342 canonical NN). Polytope distribution: octa 3
antipodal at sqrt(2) R, tetra 0, icosa 30 second-shell at phi*R = 3.83 fm where
K_3 = 0.684 (corrected — handover quoted 0.766; actual at phi*R is 0.684).
Predicted F1: extra binding pulls delta R INWARD; Phase 5 sign theorem still
gives Delta E > 0 for any delta R != 0; F1 PASSES analytically by composition."

Phase 8 (Session 20) established Refinement A as the first multi-session
refinement of R3-Coulomb, achieving factor 3.6 polytope-residual magnitude
improvement over Phase 6 (max residual 0.0495 MeV/alpha vs Phase 6 0.0137 vs
empirical 0.1042) and near-exact zero-parameter match at ^40Ca and ^36Ar (within
0.001 MeV/alpha each). The mechanism (NN-fraction-weighted differential
softening) was identified, quantified, and confirmed as polytope-residual-
generating. Refinement A captures ~half (48%) of empirical polytope-residual
scale; the other half pending Refinements C, D, R3-Pauli, and shell-physics
decomposition for sub-shell-closure nuclei (^28Si, ^32S — outside R3 scope).

PHASE 4-8 LESSON CARRIED FORWARD: F1 sign analytical check FIRST.

Pre-empted F1 sign argument (sign-theorem composition workflow extended to
non-NN K_3, Phase 6 §5.2 → Phase 8 §2 → Phase 9):
  Level 1 (within-mechanism):
    (i)   K_3 binding V_K3(r) = -B_pair exp(-(r-R_alpha)^2 / (2 sigma_K3^2))
          has minimum at r = R_alpha; for any pair past peak (r > R_alpha)
          like non-NN diagonals, dV/dr > 0, force is INWARD toward peak.
    (ii)  Adding non-NN K_3 contributions → ADDITIONAL inward force on delta R
          coordinate.  Equilibrium delta R reduces: delta R_{C+A} < delta R_A.
    (iii) Phase 5 sign theorem extended: for delta R > 0, ALL pairs (NN at
          r_0 = R_alpha and non-NN at r_0 > R_alpha) move further from K_3
          peak, so Delta V_K3 > 0 per pair (binding loss).
    (iv)  At equilibrium delta R_eq^{C+A} > 0, Coulomb savings still exceed
          total K_3 loss (NN + non-NN) by force balance → net binding
          gain > 0 = empirical-required.
    F1 PASSES at within-mechanism level by composition.

  Level 2 (empirical comparison):
    Refinement C+A predicts net binding gain > 0 vs canonical-no-expansion
    (same direction as Phase 8).  Empirical alpha-conjugate excess vs smooth
    baseline is positive.  F1 SIGN COMPATIBLE at smooth-A level.
    Polytope-residual sign agreement requires computation.

Computational comparison tests F2 magnitude and F3 pattern.

KEY QUESTION: does adding non-NN K_3 binding generate further polytope-specific
structure that Phase 8's NN-fraction-weighted differential Coulomb softening
missed?  In particular:

  - Tetrahedron (N=4): all 6 pairs are NN, no non-NN contribution → delta R
    unchanged from Phase 8.
  - Octahedron (N=6): 12 NN + 3 antipodal at sqrt(2) R_alpha (K_3 = 0.918).
    Modest additional binding (3 * 0.918 * B_pair = 6.45 MeV at canonical).
  - Icosahedron (N=12): 30 NN + 30 second-shell at phi*R_alpha (K_3 = 0.684)
    + 6 antipodal at sqrt(1+phi^2)*R_alpha (K_3 = 0.445).  LARGE additional
    binding (30*0.684 + 6*0.445)*B_pair = 54.3 MeV at canonical (vs NN 70.3
    MeV).  77% additional K_3 binding from non-NN pairs.

Naive prediction: Refinement C will reduce delta R most dramatically at
icosahedron (N=12); little or no effect at tetrahedron (N=4); intermediate at
J-solid mid-range polytopes (N=5-10).

POLYTOPE-RESIDUAL EXPECTATION:
  Phase 8 currently OVERSHOOTS empirical at ^48Cr (+0.041 vs empirical +0.021)
  → Refinement C reducing delta R^48Cr should reduce predicted residual
  toward empirical (factor 2 improvement potential at N=12).

  Phase 8 UNDERSHOOTS empirical at ^16O (+0.05 vs empirical +0.104)
  → Refinement C does nothing to ^16O (no non-NN pairs in tetrahedron).
  ^16O remains a magnitude shortfall, plausibly shell-physics-enhanced.

  ^40Ca and ^36Ar are near-exact in Phase 8.  Refinement C must NOT degrade
  these matches (otherwise refinement is counter-productive).  Predicted
  shift at N=9, 10 from non-NN K_3: small relative to icosahedron because
  fewer non-NN pairs and more diluted spread.

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase9_R3_Coulomb_RefC.md

Inheritance: polytopes / edge construction / m_alpha / B_pair / R_alpha / sigma_K3
from Phase 5; sign-theorem composition workflow from Phase 6 §5.2; smooth-A vs
polytope-residual methodology from Phase 7; AME 2020 binding data from Phase 7;
extended Gaussian alpha charge (Refinement A) from Phase 8.
"""

import math
import numpy as np
from scipy.optimize import minimize, brentq
from scipy.special import erf


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 5/6/7/8)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790
B_pair       = M_0 / phi
R_alpha      = 2.37
sigma_K3_canon = 1.68
COULOMB_AA   = 4 * 1.44   # = 5.76 MeV·fm

# Refinement A (Phase 8): alpha extended Gaussian charge distribution
R_ALPHA_CHARGE   = 1.68     # alpha rms charge radius [fm]
SIGMA_Q          = R_ALPHA_CHARGE / math.sqrt(3)   # 0.970 fm
TWO_SIGMA_Q      = 2 * SIGMA_Q

# AME 2020 binding energies (verbatim Phase 7)
AME_DATA = {
    4:  ('16O',  16,  8, 127.619),
    5:  ('20Ne', 20, 10, 160.645),
    6:  ('24Mg', 24, 12, 198.257),
    7:  ('28Si', 28, 14, 236.537),
    8:  ('32S',  32, 16, 271.781),
    9:  ('36Ar', 36, 18, 306.715),
    10: ('40Ca', 40, 20, 342.052),
    12: ('48Cr', 48, 24, 411.462),
}

# SEMF parameters (Phase 7 verbatim)
SEMF_aV = 15.8
SEMF_aS = 17.8
SEMF_aC = 0.711
SEMF_aP = 11.18


def semf_baseline(A, Z):
    return SEMF_aV*A - SEMF_aS*A**(2/3) - SEMF_aC*Z**2/A**(1/3) + SEMF_aP/math.sqrt(A)


# ---------------------------------------------------------------------------
# Polytope construction (verbatim from Phase 5/6/7/8)
# ---------------------------------------------------------------------------
def rescale(verts, R_target=R_alpha):
    n = len(verts); md = math.inf
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if d < md: md = d
    return verts * (R_target / md)


def poly_4():
    return rescale(np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float))


def poly_5():
    return rescale(np.array([
        [1,0,0],[-0.5,math.sqrt(3)/2,0],[-0.5,-math.sqrt(3)/2,0],
        [0,0,math.sqrt(2)],[0,0,-math.sqrt(2)]]))


def poly_6():
    return rescale(np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],
                             [0,0,1],[0,0,-1]],dtype=float))


def poly_7():
    pentR = 1.0; edge = 2*math.sin(math.pi/5); h = math.sqrt(edge**2-pentR**2)
    pent = []
    for k in range(5):
        a = 2*math.pi*k/5
        pent.append([pentR*math.cos(a), pentR*math.sin(a), 0])
    pent.append([0,0,h]); pent.append([0,0,-h])
    return rescale(np.array(pent))


def poly_8():
    np.random.seed(27)
    v0 = np.random.randn(24)*0.6
    def loss(p):
        v = p.reshape(8,3)
        ds = sorted([np.linalg.norm(v[i]-v[j]) for i in range(8) for j in range(i+1,8)])
        return sum((d-1)**2 for d in ds[:18]) + 50*sum(max(0,1.05-d)**2 for d in ds[18:])
    res = minimize(loss, v0, method='Powell', options={'maxiter':10000,'xtol':1e-10})
    return rescale(res.x.reshape(8,3))


def poly_9():
    h = 0.5; s = 1.0; R = s/math.sqrt(3)
    prism = []
    for k in range(3):
        a = 2*math.pi*k/3
        prism.append([R*math.cos(a),R*math.sin(a),h])
        prism.append([R*math.cos(a),R*math.sin(a),-h])
    aug = []
    for k in range(3):
        a1 = 2*math.pi*k/3; a2 = 2*math.pi*(k+1)/3
        mx = R*(math.cos(a1)+math.cos(a2))/2; my = R*(math.sin(a1)+math.sin(a2))/2
        nrm = math.sqrt(mx**2+my**2); ext = 1/math.sqrt(2)
        aug.append([mx+ext*mx/nrm, my+ext*my/nrm, 0])
    v0 = np.array(prism+aug).flatten()
    def loss(p):
        v = p.reshape(9,3)
        ds = sorted([np.linalg.norm(v[i]-v[j]) for i in range(9) for j in range(i+1,9)])
        return sum((d-1)**2 for d in ds[:21]) + 50*sum(max(0,1.05-d)**2 for d in ds[21:])
    res = minimize(loss, v0, method='Powell', options={'maxiter':30000,'xtol':1e-10})
    return rescale(res.x.reshape(9,3))


def poly_10():
    R = 1/math.sqrt(2)
    h = math.sqrt((1-R**2*(2-math.sqrt(2)))/4)
    H = h+1/math.sqrt(2)
    v = []
    for k in range(4):
        a = math.pi/2*k
        v.append([R*math.cos(a),R*math.sin(a),h])
    for k in range(4):
        a = math.pi/2*k+math.pi/4
        v.append([R*math.cos(a),R*math.sin(a),-h])
    v.append([0,0,H]); v.append([0,0,-H])
    return rescale(np.array(v))


def poly_12():
    g = phi
    return rescale(np.array([
        [0,1,g],[0,1,-g],[0,-1,g],[0,-1,-g],
        [1,g,0],[1,-g,0],[-1,g,0],[-1,-g,0],
        [g,0,1],[g,0,-1],[-g,0,1],[-g,0,-1]],dtype=float))


def build_edges(verts, R_edge=R_alpha, tol=0.05):
    n = len(verts); edges = []
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i]-verts[j])
            if abs(d-R_edge) < tol:
                edges.append((i,j))
    return edges


def precompute_pair_distances(verts):
    n = len(verts); pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append(np.linalg.norm(verts[i]-verts[j]))
    return pairs


# ---------------------------------------------------------------------------
# Refinement A: extended Gaussian charge Coulomb (verbatim from Phase 8)
# ---------------------------------------------------------------------------
def coulomb_pair_extended(r, sigma_q=SIGMA_Q):
    return COULOMB_AA / r * erf(r / (2*sigma_q))


def coulomb_pair_pointcharge(r):
    return COULOMB_AA / r


def coulomb_total_extended(verts, sigma_q=SIGMA_Q):
    n = len(verts); V = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r_ij = np.linalg.norm(verts[i]-verts[j])
            V += coulomb_pair_extended(r_ij, sigma_q)
    return V


def coulomb_force_extended(delta_R, pair_distances_canon, sigma_q=SIGMA_Q,
                            R_canon=R_alpha):
    """Force on delta R from extended-charge Coulomb (Phase 8)."""
    s = 1.0 + delta_R / R_canon
    F = 0.0
    inv_sqrt_pi = 1.0 / math.sqrt(math.pi)
    for r0 in pair_distances_canon:
        r = r0 * s
        x = r / (2*sigma_q)
        dVdr = COULOMB_AA * (-erf(x)/r**2 + inv_sqrt_pi/(r*sigma_q) * math.exp(-x*x))
        F += -dVdr * (r0 / R_canon)
    return F


# ---------------------------------------------------------------------------
# Refinement C: K_3 contribution from ALL pairs (NN + non-NN)
# ---------------------------------------------------------------------------
def k3_pair(r, sigma_K3=sigma_K3_canon, R_canon=R_alpha):
    """K_3 binding per pair at separation r:
       V_K3(r) = -B_pair * exp(-(r-R_canon)^2 / (2 sigma^2))
    """
    return -B_pair * math.exp(-(r-R_canon)**2 / (2*sigma_K3**2))


def k3_total_all_pairs(pair_distances, sigma_K3=sigma_K3_canon, R_canon=R_alpha):
    """V_K3^{total}(0) = sum over all pairs (NN + non-NN) at canonical."""
    return sum(k3_pair(r, sigma_K3, R_canon) for r in pair_distances)


def k3_force_all_pairs(delta_R, pair_distances_canon, sigma_K3=sigma_K3_canon,
                        R_canon=R_alpha):
    """Inward K_3 force MAGNITUDE on delta R, summed over ALL pairs (Refinement C).

    Returns |F_K3_all_pairs| = sum over pairs of (dV_K3/d(delta R) > 0 for any
    pair past peak under expansion).  Convention matches Phase 8
    k3_force_NN_only: positive value = magnitude of inward force.

    For each pair at canonical r_0, displacement under uniform delta R scaling:
      r(delta R) = r_0 * (1 + delta R / R_canon)
      u(delta R) = r(delta R) - R_canon = (r_0 - R_canon) + r_0 * delta R / R_canon

    dV_K3/dr at r = +B_pair * u/sigma^2 * exp(-u^2/(2 sigma^2))
    dV_K3/d(delta R) = dV/dr * dr/d(delta R) = dV/dr * r_0/R_canon

    For NN pair (r_0 = R_canon) at delta R > 0: u = delta R > 0 → dV/d(deltaR) > 0
      → energy increases with delta R → inward force magnitude = +dV/d(deltaR).
    For non-NN pair (r_0 > R_canon) at any delta R >= 0: u > 0 → dV/d(deltaR) > 0
      → inward force magnitude = +dV/d(deltaR).  (Already inward at canonical.)

    Sum gives total inward force MAGNITUDE; equilibrium with Coulomb outward:
      coulomb_force_extended(dr) = k3_force_all_pairs(dr).
    """
    s = 1.0 + delta_R / R_canon
    F_inward = 0.0
    for r0 in pair_distances_canon:
        r = r0 * s
        u = r - R_canon
        # dV_K3/d(delta R) per pair = B_pair * u/sigma^2 * exp(-u^2/(2sigma^2)) * (r_0/R_canon)
        F_inward += B_pair * (u/sigma_K3**2) * math.exp(-(u**2)/(2*sigma_K3**2)) * (r0/R_canon)
    return F_inward


def k3_force_NN_only(delta_R, n_edges, sigma_K3=sigma_K3_canon):
    """Phase 8 NN-only K_3 force: |E| * B_pair * (delta R / sigma^2) *
    exp(-delta R^2 / (2 sigma^2)).  Reference for comparison."""
    return n_edges * B_pair * (delta_R/sigma_K3**2) * math.exp(-delta_R**2/(2*sigma_K3**2))


# ---------------------------------------------------------------------------
# Equilibrium solvers: Phase 9 (Refinement A + C) and Phase 8 (Refinement A only)
# ---------------------------------------------------------------------------
def solve_equilibrium_refCA(pair_distances_canon, sigma_q=SIGMA_Q,
                              sigma_K3=sigma_K3_canon, R_canon=R_alpha,
                              search_max=10.0):
    """Phase 9 equilibrium: F_C^A(delta R) = F_K3^all(delta R).

    Net force = Coulomb (outward) - K_3 all-pairs (inward).
    Solve for delta R where net = 0.
    Note: at delta R = 0, Coulomb is outward and non-NN K_3 is already inward
    (since non-NN pairs are past K_3 peak), but typically Coulomb dominates.
    """
    def net(dr):
        return coulomb_force_extended(dr, pair_distances_canon, sigma_q, R_canon) \
             - k3_force_all_pairs(dr, pair_distances_canon, sigma_K3, R_canon)
    if net(0.0) <= 0:
        return 0.0
    n_steps = 1000
    delta_step = search_max/n_steps
    for k in range(1, n_steps+1):
        dR = k*delta_step
        if net(dR) < 0:
            try:
                return brentq(net, dR-delta_step, dR, xtol=1e-7)
            except ValueError:
                return dR
    return None


def solve_equilibrium_refA(pair_distances_canon, n_edges,
                            sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                            R_canon=R_alpha, search_max=10.0):
    """Phase 8 equilibrium reference: Refinement A Coulomb + NN-only K_3."""
    def net(dr):
        return coulomb_force_extended(dr, pair_distances_canon, sigma_q, R_canon) \
             - k3_force_NN_only(dr, n_edges, sigma_K3)
    if net(0.0) <= 0:
        return 0.0
    n_steps = 1000
    delta_step = search_max/n_steps
    for k in range(1, n_steps+1):
        dR = k*delta_step
        if net(dR) < 0:
            try:
                return brentq(net, dR-delta_step, dR, xtol=1e-7)
            except ValueError:
                return dR
    return None


# ---------------------------------------------------------------------------
# Smooth-A vs polytope-residual decomposition (Phase 7 methodology)
# ---------------------------------------------------------------------------
def detrend_linear(N_arr, y_arr):
    Ns = np.asarray(N_arr, dtype=float)
    ys = np.asarray(y_arr, dtype=float)
    A = np.column_stack([Ns, np.ones_like(Ns)])
    coeffs, *_ = np.linalg.lstsq(A, ys, rcond=None)
    a, b = coeffs
    residuals = ys - (a*Ns + b)
    return a, b, residuals


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("="*132)
    print("SS-9 OPEN-SS-32 ↔ U-shape — Phase 9 Refinement C "
          "(non-NN K_3 contributions)")
    print("="*132)
    print()
    print("Q: Does adding non-NN K_3 binding (alongside Phase 8 Refinement A "
          "extended Gaussian charge)")
    print("   generate further polytope-specific structure beyond Phase 8?  "
          "Particularly: does icosahedron's")
    print("   30 second-shell + 6 antipodal K_3 contributions push ⁴⁸Cr "
          "polytope-residual toward empirical?")
    print()
    print("Phase 4-8 lesson applied: F1 sign analytical check FIRST.")
    print()
    print("Pre-empted F1 sign argument (sign-theorem composition workflow "
          "extended to non-NN K_3):")
    print("  Level 1 (within-mechanism): adding non-NN K_3 → ADDITIONAL "
          "inward force on δR coordinate;")
    print("                              equilibrium δR_{C+A} < δR_A "
          "(less expansion).  Phase 5 sign theorem")
    print("                              extended: for δR > 0, all pairs "
          "(NN + non-NN) move further from K_3 peak,")
    print("                              so ΔV_K3 > 0 per pair.  At δR_eq, "
          "Coulomb savings still exceed total")
    print("                              K_3 loss → net binding gain > 0.  "
          "F1 PASSES analytically.")
    print("  Level 2 (empirical-comparison): smooth-A binding gain still "
          "positive — same direction as empirical")
    print("                              α-cluster binding excess.  F1 SIGN "
          "COMPATIBLE at smooth-A level;")
    print("                              polytope-residual level needs computation.")
    print()

    polys = [
        (4,  poly_4,  'tetra',     'T_d'),
        (5,  poly_5,  'tri-bipyr', 'D_3h'),
        (6,  poly_6,  'octa',      'O_h'),
        (7,  poly_7,  'pent-bipyr','D_5h'),
        (8,  poly_8,  'snub-disph','D_2d'),
        (9,  poly_9,  'tri-aug',   'D_3h'),
        (10, poly_10, 'gyro-sq',   'D_4d'),
        (12, poly_12, 'icosa',     'I_h'),
    ]

    cluster_data = []
    for N, fn, name, sym in polys:
        v = fn()
        edges = build_edges(v)
        pds = precompute_pair_distances(v)
        cluster_data.append((N, name, sym, v, edges, pds))

    # ---- Pair distance distributions per polytope ----
    print("Pair distance distributions per polytope (canonical):")
    print(f"  {'N':>3} {'sym':>5} {'#pairs':>7} {'#NN(R_α)':>10} {'#non-NN':>9} "
          f"{'unique non-NN distances [fm]':>40}")
    print("  " + "-"*100)
    for N, name, sym, v, edges, pds in cluster_data:
        n_pairs = len(pds)
        n_NN = len(edges)
        n_nonNN = n_pairs - n_NN
        nonNN_distances = [r for r in pds if abs(r - R_alpha) > 0.05]
        # Bucket distances
        unique = []
        for r in nonNN_distances:
            found = False
            for u in unique:
                if abs(u[0] - r) < 0.05:
                    u[1] += 1
                    found = True
                    break
            if not found:
                unique.append([r, 1])
        unique_str = ', '.join(f"{u[0]:.3f}({u[1]})" for u in sorted(unique))
        print(f"  {N:>3} {sym:>5} {n_pairs:>7} {n_NN:>10} {n_nonNN:>9} "
              f"{unique_str:>40}")
    print()

    # ---- K_3 contribution at canonical (NN + non-NN totals) ----
    print("K_3 binding at canonical δR=0 — NN vs non-NN contributions:")
    print(f"  {'N':>3} {'sym':>5} {'V_K3^NN(0)':>12} {'V_K3^nonNN(0)':>15} "
          f"{'V_K3^total(0)':>15} {'non-NN frac':>12}")
    print("  " + "-"*100)
    for N, name, sym, v, edges, pds in cluster_data:
        n_NN = len(edges)
        V_NN = sum(k3_pair(R_alpha) for _ in range(n_NN))  # all NN at R_alpha
        V_nonNN = sum(k3_pair(r) for r in pds if abs(r - R_alpha) > 0.05)
        V_total = V_NN + V_nonNN
        frac = V_nonNN / V_NN * 100 if V_NN < 0 else 0
        print(f"  {N:>3} {sym:>5} {V_NN:>12.3f} {V_nonNN:>15.3f} "
              f"{V_total:>15.3f} {frac:>11.1f}%")
    print()

    # ---- Equilibrium δR comparison: Phase 9 (RefC+A) vs Phase 8 (RefA) ----
    print("Equilibrium δR: Phase 9 (Refinement A + C) vs Phase 8 (Refinement A only):")
    print(f"  {'N':>3} {'sym':>5} {'V_C^A(0)':>10} "
          f"{'δR_{C+A}':>10} {'δR_A':>10} {'shift %':>9} "
          f"{'ΔE_K3^total/α':>15} {'ΔE_K3^A/α':>12}")
    print("  " + "-"*120)
    p9_results = []
    p8_results = []
    for N, name, sym, v, edges, pds in cluster_data:
        n_edges = len(edges)
        VC_p8 = coulomb_total_extended(v)
        # Phase 9: Refinement C+A
        dR_CA = solve_equilibrium_refCA(pds)
        # Phase 8: Refinement A only
        dR_A = solve_equilibrium_refA(pds, n_edges)

        # Phase 9 K_3 binding loss per alpha at equilibrium
        s_CA = 1 + dR_CA/R_alpha
        VK3_total_CA_eq = sum(k3_pair(r0*s_CA) for r0 in pds)
        VK3_total_CA_canon = sum(k3_pair(r0) for r0 in pds)
        ΔEK3_CA = VK3_total_CA_eq - VK3_total_CA_canon  # positive (binding loss)
        ΔEK3_CA_per_alpha = ΔEK3_CA / N

        # Phase 8 K_3 binding loss per alpha at equilibrium (NN only)
        ΔEK3_A = n_edges * B_pair * (1 - math.exp(-dR_A**2/(2*sigma_K3_canon**2)))
        ΔEK3_A_per_alpha = ΔEK3_A / N

        shift_pct = (dR_CA/dR_A - 1) * 100 if dR_A > 0 else 0
        print(f"  {N:>3} {sym:>5} {VC_p8:>10.3f} "
              f"{dR_CA:>10.4f} {dR_A:>10.4f} {shift_pct:>+9.3f} "
              f"{ΔEK3_CA_per_alpha:>15.4f} {ΔEK3_A_per_alpha:>12.4f}")
        p9_results.append((N, name, dR_CA, ΔEK3_CA, VC_p8, pds, n_edges))
        p8_results.append((N, name, dR_A, ΔEK3_A))
    print()

    # ---- Net binding gain per alpha: Phase 9 vs Phase 8 ----
    print("Net binding gain per α (Coulomb savings minus K_3 loss):")
    print(f"  {'N':>3} {'sym':>5} {'P9 Coul/α':>11} "
          f"{'P9 K_3/α':>10} {'P9 net gain':>13} "
          f"{'P8 net gain':>13} {'Δ(P9-P8)':>11}")
    print("  " + "-"*110)
    p9_net_gain = []
    p8_net_gain = []
    for i, ((N, name, dR_CA, ΔEK3_CA, VC0, pds, n_edges),
            (N2, name2, dR_A, ΔEK3_A)) in enumerate(zip(p9_results, p8_results)):
        # Phase 9 Coulomb savings (using extended-charge V_C^A)
        s_CA = 1 + dR_CA/R_alpha
        VC_eq = sum(coulomb_pair_extended(r0*s_CA) for r0 in pds)
        VC_savings_CA = (VC0 - VC_eq) / N
        K3_loss_CA = ΔEK3_CA / N
        net_gain_CA = VC_savings_CA - K3_loss_CA
        # Phase 8 reference
        s_A = 1 + dR_A/R_alpha
        VC_eq_A = sum(coulomb_pair_extended(r0*s_A) for r0 in pds)
        VC_savings_A = (VC0 - VC_eq_A) / N
        K3_loss_A = ΔEK3_A / N
        net_gain_A = VC_savings_A - K3_loss_A
        diff = net_gain_CA - net_gain_A
        print(f"  {N:>3} {polys[i][3]:>5} "
              f"{VC_savings_CA:>11.4f} {K3_loss_CA:>10.4f} "
              f"{net_gain_CA:>+13.4f} {net_gain_A:>+13.4f} {diff:>+11.4f}")
        p9_net_gain.append((N, net_gain_CA))
        p8_net_gain.append((N, net_gain_A))
    print()

    # ---- Smooth-A vs polytope-residual decomposition ----
    print("Smooth-A vs polytope-residual decomposition (Phase 7 methodology):")
    Ns_p9 = [item[0] for item in p9_net_gain]
    gains_p9 = [item[1] for item in p9_net_gain]
    a_p9, b_p9, resid_p9 = detrend_linear(Ns_p9, gains_p9)
    print(f"  Phase 9 net gain ≈ {a_p9:.4f}·N + {b_p9:+.4f} MeV/α (linear-in-N fit)")
    print(f"  Phase 9 polytope residuals (after detrending):")
    for i, (N, gn) in enumerate(p9_net_gain):
        print(f"    N={N:>2} ({AME_DATA[N][0]:>5}): residual = {resid_p9[i]:+.5f} MeV/α")
    print(f"  Phase 9 max |residual| = {max(abs(r) for r in resid_p9):.5f} MeV/α")
    print()

    # Phase 8 reference
    Ns_p8 = [item[0] for item in p8_net_gain]
    gains_p8 = [item[1] for item in p8_net_gain]
    a_p8, b_p8, resid_p8 = detrend_linear(Ns_p8, gains_p8)
    print(f"  Phase 8 reference: net gain ≈ {a_p8:.4f}·N + {b_p8:+.4f} MeV/α")
    print(f"  Phase 8 max |residual| = {max(abs(r) for r in resid_p8):.5f} MeV/α")
    print()

    # Empirical
    emp_dBA = []
    for N in Ns_p9:
        nuc, A, Z, B_emp = AME_DATA[N]
        BA_emp = B_emp/A
        BA_semf = semf_baseline(A, Z)/A
        emp_dBA.append((N, BA_emp - BA_semf))
    Ns_emp = [item[0] for item in emp_dBA]
    dBA_emp = [item[1] for item in emp_dBA]
    a_emp, b_emp, resid_emp = detrend_linear(Ns_emp, dBA_emp)
    print(f"  Empirical Δ(B/A) ≈ {a_emp:.5f}·N + {b_emp:+.5f} MeV/α")
    print(f"  Empirical max |residual| = {max(abs(r) for r in resid_emp):.5f} MeV/α")
    print()

    # ---- F2/F3 polytope-by-polytope comparison ----
    print("F2/F3 — polytope-residual comparison: Phase 9 vs Phase 8 vs empirical")
    print(f"  {'N':>3} {'nuc':>5} {'P8 resid':>10} {'P9 resid':>10} "
          f"{'emp resid':>10} {'P9 sign?':>10} {'P8 sign?':>10}")
    print("  " + "-"*80)
    sign_match_p9 = 0
    sign_match_p8 = 0
    for i, N in enumerate(Ns_p9):
        emp = resid_emp[i]
        p8 = resid_p8[i]
        p9 = resid_p9[i]
        match_p9 = (np.sign(emp) == np.sign(p9) and abs(emp) > 0.001 and abs(p9) > 1e-6)
        match_p8 = (np.sign(emp) == np.sign(p8) and abs(emp) > 0.001 and abs(p8) > 1e-6)
        if match_p9: sign_match_p9 += 1
        if match_p8: sign_match_p8 += 1
        print(f"  {N:>3} {AME_DATA[N][0]:>5} {p8:>+10.5f} {p9:>+10.5f} "
              f"{emp:>+10.5f} {'YES' if match_p9 else 'no':>10} "
              f"{'YES' if match_p8 else 'no':>10}")
    print()
    print(f"  Phase 9 sign agreement: {sign_match_p9}/{len(Ns_p9)} polytopes")
    print(f"  Phase 8 sign agreement: {sign_match_p8}/{len(Ns_p9)} polytopes")
    print(f"  Phase 9 max residual = {max(abs(r) for r in resid_p9):.4f} MeV/α")
    print(f"  Phase 8 max residual = {max(abs(r) for r in resid_p8):.4f} MeV/α")
    print(f"  Empirical max residual = {max(abs(r) for r in resid_emp):.4f} MeV/α")
    p9_emp_ratio = max(abs(r) for r in resid_p9) / max(abs(r) for r in resid_emp)
    p8_emp_ratio = max(abs(r) for r in resid_p8) / max(abs(r) for r in resid_emp)
    print(f"  Phase 9/empirical magnitude ratio: {p9_emp_ratio:.3f}")
    print(f"  Phase 8/empirical magnitude ratio: {p8_emp_ratio:.3f}")
    print()

    # ---- Specific anchor checks: 40Ca and 36Ar (Phase 8 near-exact) ----
    print("Anchor check: Phase 8 near-exact matches at ⁴⁰Ca and ³⁶Ar — "
          "are they preserved in Phase 9?")
    for i, N in enumerate(Ns_p9):
        if N in [9, 10]:
            print(f"  N={N} ({AME_DATA[N][0]}): "
                  f"empirical {resid_emp[i]:+.5f}, "
                  f"Phase 8 {resid_p8[i]:+.5f}, "
                  f"Phase 9 {resid_p9[i]:+.5f}")
    print()

    # ---- ¹⁶O and ⁴⁸Cr behavior ----
    print("Targeted polytopes: ¹⁶O (Phase 8 undershoots empirical) and "
          "⁴⁸Cr (Phase 8 overshoots empirical):")
    for i, N in enumerate(Ns_p9):
        if N in [4, 12]:
            print(f"  N={N} ({AME_DATA[N][0]}): "
                  f"empirical {resid_emp[i]:+.5f}, "
                  f"Phase 8 {resid_p8[i]:+.5f}, "
                  f"Phase 9 {resid_p9[i]:+.5f}, "
                  f"Δ(P9-P8) = {resid_p9[i] - resid_p8[i]:+.5f}")
    print()

    # ---- Verdict ----
    print("="*132)
    print("VERDICT")
    print("="*132)
    print()
    print("F1 (sign): F1 PASSES at within-mechanism level (Refinement C+A → "
          "δR_{C+A} > 0 → ΔE > 0).")
    print(f"           Polytope-residual sign agreement: {sign_match_p9}/"
          f"{len(Ns_p9)} (vs Phase 8 {sign_match_p8}/{len(Ns_p9)}).")
    print()
    print("F2 (magnitude):")
    print(f"  Phase 9 max polytope residual = "
          f"{max(abs(r) for r in resid_p9):.4f} MeV/α")
    print(f"  Phase 8 max polytope residual = "
          f"{max(abs(r) for r in resid_p8):.4f} MeV/α")
    print(f"  Empirical max polytope residual = "
          f"{max(abs(r) for r in resid_emp):.4f} MeV/α")
    if p9_emp_ratio > p8_emp_ratio * 1.2:
        print("  Refinement C INCREASES polytope-residual magnitude further "
              "toward empirical scale.")
    elif p9_emp_ratio < p8_emp_ratio * 0.8:
        print("  Refinement C DECREASES polytope-residual magnitude (counter-"
              "productive).")
    else:
        print("  Refinement C leaves polytope-residual magnitude approximately "
              "unchanged from Phase 8.")
    print()
    print("F3 (pattern): see polytope-by-polytope sign and magnitude tables above.")
    print()


if __name__ == '__main__':
    main()
