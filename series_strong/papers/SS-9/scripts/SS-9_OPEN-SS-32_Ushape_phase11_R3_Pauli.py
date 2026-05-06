"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 11 R3-Pauli scoping.

Session 22 Phase 10 (sketch §7.1 / 0214 handover) registered Session 23 Priority 1
as R3-Pauli scoping — sole remaining single-session-tractable refinement
candidate after Phases 9 + 10 ruled out the entire sigma-parameterized K_3
refinement class. Pauli is naturally NN-localized via wave-function overlap
(alpha-alpha Pauli core acts at short range; exponentially suppressed at non-NN
distances) — has the right structural symmetry that K_3-sigma-tuning variants
lack.

Phase 8 (Session 20) Refinement A (extended Gaussian alpha charge distribution)
delivered factor 3.6 polytope-residual magnitude improvement and near-exact
zero-parameter match at ^40Ca (within 0.0001 MeV/alpha) and ^36Ar (within 0.001
MeV/alpha). Status: standing best refinement, structurally STRENGTHENED by
Phases 9 + 10.

PHASE 4-10 LESSON CARRIED FORWARD: F1 sign analytical check FIRST.

Pauli model specification (Gaussian repulsive core):

  V_P(r) = V_P^0 * exp(-r^2 / (2 sigma_P^2))

with V_P^0 > 0 (repulsive amplitude) and sigma_P set by alpha matter rms
radius scale.  Alpha rms matter radius is approximately 1.5 fm (cf. Egelhof et
al. 2002, electron scattering value 1.676 fm; matter radius slightly smaller
due to neutron skin).  We fix sigma_P = 1.5 fm at scoping (one-parameter
model).  V_P^0 calibrated to preserve Phase 6 5% smooth-A bullseye and Phase 8
1% bullseye at N = 10 — i.e., delta R(N=10) ~ 1.05 fm.

Wave-function-overlap structure verification:
  At R_alpha = 2.37 fm (NN):              V_P/V_P^0 = exp(-1.248) = 0.287
  At sqrt(2)*R_alpha = 3.35 fm (1st non-NN): V_P/V_P^0 = exp(-2.493) = 0.083 (factor 3.5 suppression vs NN)
  At phi*R_alpha = 3.835 fm (icosa 2nd):  V_P/V_P^0 = exp(-3.273) = 0.038 (factor 7.6 suppression)
  At sqrt(1+phi^2)*R_alpha = 4.508 fm:    V_P/V_P^0 = exp(-4.516) = 0.0109 (factor 26 suppression)

Pauli is exponentially suppressed at non-NN distances — exactly the structural
symmetry that K_3-sigma-tuning variants lacked.

Pre-empted F1 sign argument (sign-theorem composition workflow extended to
Pauli):
  Level 1 (within-mechanism):
    (i)   V_P(r) > 0 (repulsive) for all r; gradient dV_P/dr < 0 for r > 0
          (force outward, away from peak at r = 0).
    (ii)  Adding Pauli to Phase 8 system → additional outward force on
          delta R coordinate.  Equilibrium delta R_{P+A} > delta R_A.
    (iii) Phase 5 sign theorem unchanged: delta R > 0 → Delta V_edge > 0.
    (iv)  At delta R_eq^{P+A} > 0, Coulomb-plus-Pauli savings exceed K_3 loss →
          net binding gain > 0 = empirical-required.
    F1 PASSES at within-mechanism level by composition.

  Level 2 (empirical-comparison):
    Predicted net binding gain > 0 vs canonical-no-expansion (same direction
    as Phase 6/8).  F1 SIGN COMPATIBLE at smooth-A level.

Computational strategy:
  1. Fix sigma_P = 1.5 fm (alpha matter rms radius, no fit parameter).
  2. Scan V_P^0 in {0.5, 1.0, 1.5, 2.0, 3.0, 5.0} MeV; calibrate to
     Phase 8 smooth-A bullseye (delta R(N=10) ~ 1.05 fm).
  3. For best-fit V_P^0, compute polytope-residuals with smooth-A detrending
     (Phase 7 methodology).
  4. Test against Phase 8 anchor matches (registered Phase 9 + Phase 10
     constraint): ^40Ca within 0.005 MeV/alpha; ^36Ar within 0.005 MeV/alpha.
  5. Test against Phase 8 sign agreement: Phase 11 should match or improve
     6/8 polytopes.
  6. Test ^48Cr trajectory: Phase 8 overshoots empirical (+0.041 vs +0.021).
     Pauli adds outward force — does it push ^48Cr further out (worse) or
     differently per polytope?

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase11_R3_Pauli.md

Inheritance: polytopes / edge construction / m_alpha / B_pair / R_alpha /
sigma_K3 from Phase 5; sign-theorem composition workflow from Phase 6 §5.2;
smooth-A vs polytope-residual methodology from Phase 7; AME 2020 binding data
from Phase 7; extended Gaussian alpha charge (Refinement A) from Phase 8.
"""

import math
import numpy as np
from scipy.optimize import minimize, brentq, brent
from scipy.special import erf


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 5/6/7/8/9/10)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790
B_pair       = M_0 / phi
R_alpha      = 2.37
sigma_K3_canon = 1.68
COULOMB_AA   = 4 * 1.44

# Refinement A (Phase 8): alpha extended Gaussian charge
R_ALPHA_CHARGE   = 1.68
SIGMA_Q          = R_ALPHA_CHARGE / math.sqrt(3)

# Phase 11: Pauli model defaults
SIGMA_P_DEFAULT  = 1.5  # fm, alpha matter rms radius scale

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

SEMF_aV = 15.8
SEMF_aS = 17.8
SEMF_aC = 0.711
SEMF_aP = 11.18


def semf_baseline(A, Z):
    return SEMF_aV*A - SEMF_aS*A**(2/3) - SEMF_aC*Z**2/A**(1/3) + SEMF_aP/math.sqrt(A)


# ---------------------------------------------------------------------------
# Polytope construction (verbatim from Phase 5-10)
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
# Refinement A (Phase 8): extended Gaussian charge Coulomb
# ---------------------------------------------------------------------------
def coulomb_pair_extended(r, sigma_q=SIGMA_Q):
    return COULOMB_AA / r * erf(r / (2*sigma_q))


def coulomb_force_extended(delta_R, pair_distances_canon, sigma_q=SIGMA_Q,
                            R_canon=R_alpha):
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
# Phase 6/8: NN-only K_3 force
# ---------------------------------------------------------------------------
def k3_force_NN_only(delta_R, n_edges, sigma_K3=sigma_K3_canon):
    return n_edges * B_pair * (delta_R/sigma_K3**2) * math.exp(-delta_R**2/(2*sigma_K3**2))


# ---------------------------------------------------------------------------
# Phase 11: Pauli Gaussian repulsive core
# ---------------------------------------------------------------------------
def pauli_pair(r, V_P0, sigma_P):
    """V_P(r) = V_P0 * exp(-r^2 / (2 sigma_P^2)) — repulsive Gaussian."""
    return V_P0 * math.exp(-r**2 / (2*sigma_P**2))


def pauli_total(pair_distances, V_P0, sigma_P):
    return sum(pauli_pair(r, V_P0, sigma_P) for r in pair_distances)


def pauli_force(delta_R, pair_distances_canon, V_P0, sigma_P, R_canon=R_alpha):
    """Outward force MAGNITUDE on delta R from Pauli (matches Phase 8 convention).

    For each pair at canonical r_0:
      r(delta R) = r_0 * (1 + delta R / R_canon)
      dV_P/dr = -V_P0 * (r / sigma_P^2) * exp(-r^2 / (2 sigma_P^2))
      Force_outward = -dV_P/dr * (r_0 / R_canon) = V_P0 * (r/sigma_P^2) * exp(-r^2/(2sigma_P^2)) * (r_0/R_canon)
    """
    s = 1.0 + delta_R / R_canon
    F_outward = 0.0
    for r0 in pair_distances_canon:
        r = r0 * s
        F_outward += V_P0 * (r / sigma_P**2) * math.exp(-r**2 / (2*sigma_P**2)) * (r0/R_canon)
    return F_outward


# ---------------------------------------------------------------------------
# Equilibrium solvers
# ---------------------------------------------------------------------------
def solve_equilibrium_phase8(pair_distances_canon, n_edges,
                               sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                               R_canon=R_alpha, search_max=10.0):
    """Phase 8 reference: Coulomb_extended (outward) - K_3_NN (inward)."""
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


def solve_equilibrium_phase11(pair_distances_canon, n_edges,
                                V_P0, sigma_P=SIGMA_P_DEFAULT,
                                sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                                R_canon=R_alpha, search_max=10.0):
    """Phase 11: Coulomb_extended (out) + Pauli (out) - K_3_NN (in)."""
    def net(dr):
        return coulomb_force_extended(dr, pair_distances_canon, sigma_q, R_canon) \
             + pauli_force(dr, pair_distances_canon, V_P0, sigma_P, R_canon) \
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
# Net binding gain calculation (Phase 8 form + Pauli term)
# ---------------------------------------------------------------------------
def net_gain_per_alpha_phase11(N, dR, pair_distances_canon, n_edges,
                                  V_P0, sigma_P=SIGMA_P_DEFAULT,
                                  sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                                  R_canon=R_alpha):
    """Net binding gain per alpha: Coulomb savings + Pauli savings - K_3 loss."""
    if dR is None or dR == 0:
        return 0.0
    s = 1 + dR/R_canon
    # Coulomb savings (Phase 8 form, extended-charge)
    VC_canon = sum(coulomb_pair_extended(r0, sigma_q) for r0 in pair_distances_canon)
    VC_eq = sum(coulomb_pair_extended(r0*s, sigma_q) for r0 in pair_distances_canon)
    coul_savings = (VC_canon - VC_eq) / N
    # Pauli savings (V_P decreases as cluster expands — analogous savings)
    VP_canon = pauli_total(pair_distances_canon, V_P0, sigma_P)
    VP_eq = pauli_total([r0*s for r0 in pair_distances_canon], V_P0, sigma_P)
    pauli_savings = (VP_canon - VP_eq) / N  # positive (V_P decreases as r increases)
    # K_3 loss (NN-only, Phase 8 convention)
    K3_loss = n_edges * B_pair * (1 - math.exp(-dR**2 / (2*sigma_K3**2))) / N
    return coul_savings + pauli_savings - K3_loss


def net_gain_per_alpha_phase8(N, dR, pair_distances_canon, n_edges,
                                sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                                R_canon=R_alpha):
    """Phase 8 reference net gain."""
    if dR is None or dR == 0:
        return 0.0
    s = 1 + dR/R_canon
    VC_canon = sum(coulomb_pair_extended(r0, sigma_q) for r0 in pair_distances_canon)
    VC_eq = sum(coulomb_pair_extended(r0*s, sigma_q) for r0 in pair_distances_canon)
    coul_savings = (VC_canon - VC_eq) / N
    K3_loss = n_edges * B_pair * (1 - math.exp(-dR**2 / (2*sigma_K3**2))) / N
    return coul_savings - K3_loss


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
# Pauli amplitude verification (wave-function-overlap structure)
# ---------------------------------------------------------------------------
def verify_wavefunction_overlap_structure(sigma_P=SIGMA_P_DEFAULT):
    print(f"  Pauli amplitude V_P(r)/V_P^0 at characteristic distances (sigma_P = {sigma_P} fm):")
    distances = [
        (R_alpha, "NN (R_alpha = 2.37 fm)"),
        (math.sqrt(2)*R_alpha, "1st non-NN (sqrt(2)*R_alpha = 3.35 fm, octa antipodal)"),
        (phi*R_alpha, "icosa 2nd-shell (phi*R_alpha = 3.84 fm)"),
        (math.sqrt(1+phi**2)*R_alpha, "icosa antipodal (sqrt(1+phi^2)*R_alpha = 4.51 fm)"),
    ]
    for r, desc in distances:
        amp = math.exp(-r**2 / (2*sigma_P**2))
        print(f"    {desc:<55} V_P/V_P^0 = {amp:.4f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("="*132)
    print("SS-9 OPEN-SS-32 ↔ U-shape — Phase 11 R3-Pauli scoping (Gaussian repulsive core)")
    print("="*132)
    print()
    print("Phase 4-10 lesson applied: F1 sign analytical check FIRST.")
    print()
    print("Pre-empted F1 sign argument (sign-theorem composition workflow extended to Pauli):")
    print("  Level 1 (within-mechanism): V_P(r) > 0 (repulsive); dV_P/dr < 0 for r > 0 → force outward;")
    print("                              adding Pauli to Phase 8 → additional outward force on δR;")
    print("                              equilibrium δR_{P+A} > δR_A; Phase 5 sign theorem unchanged;")
    print("                              at δR_eq^{P+A} > 0, Coulomb-plus-Pauli savings exceed K_3 loss")
    print("                              → net binding gain > 0.  F1 PASSES analytically.")
    print("  Level 2 (empirical-comparison): F1 SIGN COMPATIBLE at smooth-A level.")
    print()
    print("Pauli model: V_P(r) = V_P^0 * exp(-r^2 / (2 sigma_P^2)), with sigma_P = 1.5 fm fixed")
    print("(alpha matter rms radius scale; no fit parameter).")
    print()

    print("Wave-function-overlap structure check:")
    verify_wavefunction_overlap_structure(SIGMA_P_DEFAULT)
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

    # Empirical reference
    Ns_ref = [N for N, *_ in cluster_data]
    dBA_emp = []
    for N in Ns_ref:
        nuc, A, Z, B_emp = AME_DATA[N]
        dBA_emp.append(B_emp/A - semf_baseline(A, Z)/A)
    a_emp, b_emp, resid_emp = detrend_linear(Ns_ref, dBA_emp)
    print(f"Empirical reference: Δ(B/A) ≈ {a_emp:.5f}·N + {b_emp:+.5f} MeV/α; "
          f"max residual {max(abs(r) for r in resid_emp):.4f} MeV/α")
    print()

    # Phase 8 baseline
    p8_gains = []
    p8_dR = {}
    for (N, name, sym, v, edges, pds) in cluster_data:
        dR = solve_equilibrium_phase8(pds, len(edges))
        p8_dR[N] = dR
        p8_gains.append(net_gain_per_alpha_phase8(N, dR, pds, len(edges)))
    a_p8, b_p8, resid_p8 = detrend_linear(Ns_ref, p8_gains)
    sign_p8 = sum(1 for i in range(len(Ns_ref))
                   if np.sign(resid_p8[i]) == np.sign(resid_emp[i])
                   and abs(resid_emp[i]) > 0.001 and abs(resid_p8[i]) > 1e-6)
    print(f"Phase 8 reference: net gain ≈ {a_p8:+.4f}·N + {b_p8:+.4f} MeV/α; "
          f"max residual {max(abs(r) for r in resid_p8):.4f} MeV/α; sign agreement {sign_p8}/8")
    print(f"  Phase 8 anchor matches: ⁴⁰Ca {resid_p8[Ns_ref.index(10)]:+.5f} (emp {resid_emp[Ns_ref.index(10)]:+.5f}); "
          f"³⁶Ar {resid_p8[Ns_ref.index(9)]:+.5f} (emp {resid_emp[Ns_ref.index(9)]:+.5f})")
    print()

    # ========================================================================
    # V_P^0 scan — calibrate Pauli amplitude
    # ========================================================================
    print("="*132)
    print("V_P^0 scan — calibrate Pauli amplitude (sigma_P = 1.5 fm fixed)")
    print("="*132)
    print()

    V_P0_grid = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
    scan_summary = []

    print(f"  {'V_P^0 [MeV]':>12} {'slope':>9} {'maxResid':>9} {'sign':>5} "
          f"{'36Ar resid':>11} {'40Ca resid':>11} {'36Ar err':>10} {'40Ca err':>10} "
          f"{'δR(N=4)':>9} {'δR(N=10)':>10} {'δR(N=12)':>10}")
    print("  " + "-"*135)

    for V_P0 in V_P0_grid:
        gains = []
        dR_per_N = {}
        for (N, name, sym, v, edges, pds) in cluster_data:
            dR = solve_equilibrium_phase11(pds, len(edges), V_P0)
            dR_per_N[N] = dR if dR is not None else 0.0
            gains.append(net_gain_per_alpha_phase11(N, dR, pds, len(edges), V_P0))

        a, b, resid = detrend_linear(Ns_ref, gains)
        sign_match = sum(1 for i in range(len(Ns_ref))
                          if np.sign(resid[i]) == np.sign(resid_emp[i])
                          and abs(resid_emp[i]) > 0.001 and abs(resid[i]) > 1e-6)
        idx9 = Ns_ref.index(9)
        idx10 = Ns_ref.index(10)
        anchor_36Ar_err = abs(resid[idx9] - resid_emp[idx9])
        anchor_40Ca_err = abs(resid[idx10] - resid_emp[idx10])

        scan_summary.append({
            'V_P0': V_P0,
            'slope': a,
            'intercept': b,
            'max_resid': max(abs(r) for r in resid),
            'sign_match': sign_match,
            '36Ar_err': anchor_36Ar_err,
            '40Ca_err': anchor_40Ca_err,
            '36Ar_resid': resid[idx9],
            '40Ca_resid': resid[idx10],
            'dR_per_N': dR_per_N,
            'resid_full': resid,
            'gains': gains,
        })

        print(f"  {V_P0:>12.2f} {a:>+9.4f} {max(abs(r) for r in resid):>9.4f} "
              f"{sign_match:>5d} {resid[idx9]:>+11.5f} {resid[idx10]:>+11.5f} "
              f"{anchor_36Ar_err:>10.5f} {anchor_40Ca_err:>10.5f} "
              f"{dR_per_N[4]:>9.4f} {dR_per_N[10]:>10.4f} {dR_per_N[12]:>10.4f}")

    print()
    print("Phase 5 R3-lin smooth-A target: δR(N=10) = 1.052 fm (Phase 8 = 1.042; Phase 6 = 1.104)")
    print("Phase 8 anchor preservation: 36Ar err < 0.005 MeV/α AND 40Ca err < 0.005 MeV/α")
    print()

    # ========================================================================
    # Find V_P^0 that preserves Phase 8 smooth-A bullseye
    # ========================================================================
    print("="*132)
    print("Smooth-A calibration: find V_P^0 keeping δR(N=10) closest to 1.052 fm target")
    print("="*132)
    print()

    # Bracket V_P^0: at V=0 (Phase 8), δR(10)=1.042; at higher V, δR(10) increases
    # Find V where δR(10) ≈ 1.052 (Phase 5 target)
    pds_10 = None
    n_edges_10 = None
    for (N, name, sym, v, edges, pds) in cluster_data:
        if N == 10:
            pds_10 = pds; n_edges_10 = len(edges)
            break

    def dR10_minus_target(V_P0):
        dR = solve_equilibrium_phase11(pds_10, n_edges_10, V_P0)
        return (dR if dR is not None else 0.0) - 1.052

    # Phase 8 already 1.042 (1% off); test V_P^0 ∈ [0, 1.0] to bracket
    V_P0_min = 0.0
    V_P0_max = 5.0
    if dR10_minus_target(V_P0_min) > 0:
        # Phase 8 already overshoots; go negative? No, V_P0 must be ≥ 0
        print(f"  At V_P^0 = 0 (Phase 8): δR(10) - 1.052 = {dR10_minus_target(V_P0_min):+.4f} fm")
        print(f"  → Phase 8 already at or beyond target — V_P^0 = 0 is calibration optimum.")
        V_P0_calibrated = 0.0
    elif dR10_minus_target(V_P0_max) < 0:
        print(f"  At V_P^0 = {V_P0_max}: δR(10) - 1.052 = {dR10_minus_target(V_P0_max):+.4f} fm — Pauli not strong enough to reach target.")
        V_P0_calibrated = V_P0_max
    else:
        try:
            V_P0_calibrated = brentq(dR10_minus_target, V_P0_min, V_P0_max, xtol=1e-4)
            print(f"  Calibrated V_P^0 = {V_P0_calibrated:.4f} MeV")
            print(f"    sigma_P = 1.5 fm fixed; V_P^0 calibrated to Phase 5 R3-lin smooth-A target δR(N=10) = 1.052 fm")
        except ValueError as e:
            print(f"  Calibration error: {e}")
            V_P0_calibrated = 0.0
    print()

    # Compute polytope-residuals at calibrated V_P^0
    print(f"Polytope-residuals at calibrated V_P^0 = {V_P0_calibrated:.4f} MeV:")
    gains_cal = []
    dR_cal = {}
    for (N, name, sym, v, edges, pds) in cluster_data:
        dR = solve_equilibrium_phase11(pds, len(edges), V_P0_calibrated)
        dR_cal[N] = dR if dR is not None else 0.0
        gains_cal.append(net_gain_per_alpha_phase11(N, dR, pds, len(edges), V_P0_calibrated))
    a_cal, b_cal, resid_cal = detrend_linear(Ns_ref, gains_cal)
    sign_cal = sum(1 for i in range(len(Ns_ref))
                    if np.sign(resid_cal[i]) == np.sign(resid_emp[i])
                    and abs(resid_emp[i]) > 0.001 and abs(resid_cal[i]) > 1e-6)
    print(f"  smooth-A: {a_cal:+.4f}·N + {b_cal:+.4f} MeV/α (Phase 8 = {a_p8:+.4f}·N + {b_p8:+.4f}; emp = {a_emp:+.5f}·N + {b_emp:+.5f})")
    print(f"  max polytope residual: {max(abs(r) for r in resid_cal):.4f} MeV/α "
          f"(Phase 8 = {max(abs(r) for r in resid_p8):.4f}; emp = {max(abs(r) for r in resid_emp):.4f})")
    print(f"  sign agreement: {sign_cal}/8 (Phase 8 = {sign_p8}/8)")
    print()

    # ========================================================================
    # Polytope-by-polytope comparison
    # ========================================================================
    print("F2/F3 — polytope-by-polytope: Phase 8 vs Phase 11 (calibrated) vs empirical")
    print(f"  {'N':>3} {'nuc':>5} {'emp':>10} {'P8':>10} {'P11':>10} {'P11-P8':>9} "
          f"{'P11 sign?':>10} {'δR_P11':>9}")
    print("  " + "-"*100)
    for i, N in enumerate(Ns_ref):
        emp = resid_emp[i]
        p8 = resid_p8[i]
        p11 = resid_cal[i]
        match = (np.sign(emp) == np.sign(p11) and abs(emp) > 0.001 and abs(p11) > 1e-6)
        print(f"  {N:>3} {AME_DATA[N][0]:>5} {emp:>+10.5f} {p8:>+10.5f} {p11:>+10.5f} "
              f"{p11-p8:>+9.5f} {'YES' if match else 'no':>10} {dR_cal[N]:>9.4f}")
    print()

    # Anchor preservation
    idx9 = Ns_ref.index(9)
    idx10 = Ns_ref.index(10)
    anchor_36Ar_err = abs(resid_cal[idx9] - resid_emp[idx9])
    anchor_40Ca_err = abs(resid_cal[idx10] - resid_emp[idx10])
    print(f"Anchor check (registered Phase 9 + Phase 10 constraint):")
    print(f"  36Ar: P11 = {resid_cal[idx9]:+.5f}, emp = {resid_emp[idx9]:+.5f}, "
          f"err = {anchor_36Ar_err:.5f} ({'PRESERVED' if anchor_36Ar_err < 0.005 else 'LOST'})")
    print(f"  40Ca: P11 = {resid_cal[idx10]:+.5f}, emp = {resid_emp[idx10]:+.5f}, "
          f"err = {anchor_40Ca_err:.5f} ({'PRESERVED' if anchor_40Ca_err < 0.005 else 'LOST'})")
    print()

    # ========================================================================
    # Verdict
    # ========================================================================
    print("="*132)
    print("VERDICT")
    print("="*132)
    print()
    print("F1 (sign): F1 PASSES analytically (Pauli outward + Coulomb outward + K_3 inward → δR > 0; "
          "Phase 5 sign theorem → ΔE > 0).")
    print()
    print(f"F2 (magnitude): Phase 11 max polytope residual = {max(abs(r) for r in resid_cal):.4f} MeV/α "
          f"(Phase 8 = {max(abs(r) for r in resid_p8):.4f}; emp = {max(abs(r) for r in resid_emp):.4f}).")
    if max(abs(r) for r in resid_cal) > max(abs(r) for r in resid_p8) * 1.05:
        print("  Phase 11 INCREASES polytope-residual magnitude vs Phase 8.")
    elif max(abs(r) for r in resid_cal) < max(abs(r) for r in resid_p8) * 0.95:
        print("  Phase 11 DECREASES polytope-residual magnitude vs Phase 8.")
    else:
        print("  Phase 11 leaves polytope-residual magnitude approximately unchanged from Phase 8.")
    print()
    print(f"F3 (pattern): Phase 11 sign agreement {sign_cal}/8 vs Phase 8 {sign_p8}/8.")
    if anchor_36Ar_err < 0.005 and anchor_40Ca_err < 0.005:
        print("  Phase 8 anchor matches PRESERVED at calibrated V_P^0.")
    else:
        print("  Phase 8 anchor matches LOST at calibrated V_P^0.")
    print()


if __name__ == '__main__':
    main()
