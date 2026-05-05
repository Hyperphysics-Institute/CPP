"""
SS-9 OPEN-SS-32 ↔ U-shape unification — Phase 8 R3-Coulomb Refinement A
(extended Gaussian alpha charge distribution).

Session 19 Phase 7 (sketch §6 / 0199 handover) registered Session 20 Priority 1
as: "R3-Coulomb refinements that target polytope-specific signal — Refinement A
extended Gaussian charge distribution at radius ~1.6 fm, softens NN Coulomb by
~10-20%, preserves smooth-A".  The Phase 7 reframing established that Phase 6's
5% bullseye captured the SMOOTH-A cluster Coulomb stabilization scale (correct,
absorbed into SEMF), but did NOT generate empirical polytope-specific structure
(¹⁶O excess, ²⁸Si peak, ⁴⁸Cr below-SEMF; empirical residual scale ±0.10 MeV/α
vs Phase 6 residual scale ±0.014 MeV/α — factor ~7 mismatch).

PHASE 4/5/6/7 LESSON CARRIED FORWARD: F1 sign analytical check FIRST.

Pre-empted F1 sign argument (sign-theorem composition workflow):
  Level 1 (within-mechanism):
    (i)  Extended Gaussian charge alpha pairs interact via
         V_C^(A)(r) = k_C·q²/r · erf(r/(2σ_q)) with σ_q tied to alpha rms
         charge radius.  erf > 0 for r > 0 → V_C^(A)(r) > 0 → still purely
         repulsive at all separations.
    (ii) Repulsive Coulomb drives cluster expansion → δR_A > 0.
    (iii) Phase 5 sign theorem: any δR ≠ 0 gives ΔV_edge > 0 per edge.
    Composition: δR_A > 0 → ΔE_R3 > 0 = empirical-required.
    F1 PASSES at within-mechanism level.

  Level 2 (empirical comparison):
    Refinement A predicts net binding gain > 0 vs canonical-no-expansion
    (same direction as Phase 6).  Empirical: alpha-conjugate nuclei show
    binding excess vs smooth (non-clustering) baseline.  F1 SIGN COMPATIBLE
    at smooth-A level.  Polytope-residual level requires computation.

Computational comparison tests F2 magnitude and F3 pattern.

KEY QUESTION: does extended-charge softening of NN Coulomb (~8% at canonical
R_α) vs non-NN Coulomb (~1% at √2·R_α) generate polytope-specific structure
that Phase 6 missed?

Polytopes have widely varying NN fractions:
  N=4  tetrahedron:        6 NN /  6 total = 100% NN
  N=12 icosahedron:       30 NN / 66 total = 45% NN
Differential softening between high-NN and low-NN polytopes could shift the
polytope-residual structure by O(few %) of total V_C — potentially comparable
to empirical residual scale ±0.10 MeV/α.

OPERATIONAL DEFINITIONS

Extended-charge Coulomb (alpha as 3D Gaussian charge):
  ρ_α(r) = (1/(2π σ_q²)^(3/2)) · exp(-r²/(2σ_q²)),  q_total = 2e
  rms charge radius: <r²>^(1/2) = σ_q · √3
  Convention: alpha rms charge radius r_α^charge ≈ 1.68 fm (PDG-style value)
              σ_q = r_α^charge / √3 = 0.970 fm

Inter-cluster Coulomb between two identical Gaussian charges at separation r:
  V_C^(A)(r) = k_C · q1·q2 / r · erf(r / (2σ_q))
where k_C·e² = 1.44 MeV·fm and q = 2e for alphas, so prefactor (2e)²·k_C
= 5.76 MeV·fm.

Compared to point-charge V_C^(0)(r) = k_C·q²/r:
  Softening factor = erf(r/(2σ_q))
  At r = R_α canonical = 2.37 fm, σ_q = 0.970:
     erf(2.37/1.94) = erf(1.221) = 0.9173 → 8.27% NN softening
  At r = √2·R_α = 3.35 fm:
     erf(3.35/1.94) = erf(1.727) = 0.9854 → 1.46% softening
  At r = 4 fm:
     erf(4/1.94) = erf(2.062) = 0.9963 → 0.37% softening
  → essentially point-charge for r > 4 fm.

Force balance for uniform δR expansion under extended-charge Coulomb:
Each pair separation r_ij^canon scales to r_ij^canon · (1 + δR/R_α) ≡ r_ij(δR).

V_C^(A,total)(δR) = Σ_pairs k_C·q² · erf(r_ij(δR)/(2σ_q)) / r_ij(δR)

Force on δR coordinate (positive = wants to expand):
F_C^A(δR) = -∂V_C^(A,total)/∂(δR)
        = +Σ_pairs k_C·q² · (r_ij/R_α) · {
              erf(r_ij(δR)/(2σ_q)) / r_ij(δR)²
            - exp(-(r_ij(δR)/(2σ_q))²) / (σ_q · √π · r_ij(δR))
          }

[Each pair contributes a positive force pushing δR → +∞ since V_C decreases
with r at all r > 0.]

Equilibrium condition: F_C^A(δR_eq) = K_3 restoring force at δR_eq:
  Σ_pairs k_C·q² · (r_ij/R_α) · {erf(r/(2σ_q))/r² - exp(-(r/(2σ_q))²)/(σ_q√π·r)}
  = |E| · B_pair · (δR/σ_K3²) · exp(-δR²/(2σ_K3²))

Solved numerically per polytope.

PHASE 8 EXPECTATIONS

If Refinement A is the right physics for polytope-residual generation:
  - Smooth-A part should remain close to Phase 6 (since Coulomb scale
    ~preserved at order ~5-8% level)
  - Polytope-residuals should grow beyond Phase 6's ±0.014 MeV/α scale
    toward empirical ±0.10 MeV/α scale
  - Specific polytope ordering (¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca, ⁴⁸Cr)
    may shift: tetrahedron gets MORE softening (all NN) → smaller δR → smaller
    binding gain; icosahedron gets LESS softening (low NN fraction) → larger
    relative δR
  - Some sign agreements may flip relative to Phase 6

If Refinement A is NOT the dominant mechanism:
  - Polytope-residuals barely shift (factor ~1-2 from Phase 6)
  - Need Refinement C (non-NN K₃) and/or R3-Pauli for polytope-specific signal
  - Then Refinement A is small correction, not the structure-generator

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-32_Ushape_phase8_R3_Coulomb_RefA.md

Inheritance: polytopes / edge construction / m_α / B_pair / R_α / σ_K3 from
Phase 5; sign-theorem composition workflow from Phase 6 §5.2; smooth-A vs
polytope-residual methodology from Phase 7; AME 2020 binding data from Phase 7.
"""

import math
import numpy as np
from scipy.optimize import minimize, brentq
from scipy.special import erf


# ---------------------------------------------------------------------------
# Constants (verbatim from Phase 5/6/7)
# ---------------------------------------------------------------------------
phi          = (1 + math.sqrt(5)) / 2
M_0          = 3.790
B_pair       = M_0 / phi
R_alpha      = 2.37
sigma_K3_canon = 1.68
COULOMB_AA   = 4 * 1.44   # = 5.76 MeV·fm

# Refinement A: alpha extended Gaussian charge distribution
R_ALPHA_CHARGE   = 1.68     # alpha rms charge radius [fm], conventional value
SIGMA_Q          = R_ALPHA_CHARGE / math.sqrt(3)   # Gaussian width = 0.970 fm
# Convolution width for two identical Gaussians: σ_eff² = 2σ_q² → σ_eff = σ_q·√2
# In V_C = k_C q²/r · erf(r/(σ_eff·√2)) = k_C q²/r · erf(r/(2σ_q))
TWO_SIGMA_Q  = 2 * SIGMA_Q   # = 1.940 fm

# AME 2020 binding energies (MeV) for alpha-conjugate nuclei (verbatim Phase 7)
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

# SEMF parameters for alpha-conjugate baseline (Phase 7 verbatim)
SEMF_aV = 15.8
SEMF_aS = 17.8
SEMF_aC = 0.711
SEMF_aP = 11.18


def semf_baseline(A, Z):
    """SEMF binding energy for alpha-conjugate nucleus (N=Z, even-even)."""
    return SEMF_aV*A - SEMF_aS*A**(2/3) - SEMF_aC*Z**2/A**(1/3) + SEMF_aP/math.sqrt(A)


# ---------------------------------------------------------------------------
# Polytope construction (verbatim from Phase 5/6/7)
# ---------------------------------------------------------------------------
def rescale(verts, R_target=R_alpha):
    n = len(verts)
    md = math.inf
    for i in range(n):
        for j in range(i+1, n):
            d = np.linalg.norm(verts[i] - verts[j])
            if d < md: md = d
    return verts * (R_target / md)


def poly_4():
    return rescale(np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],
                            dtype=float))


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


# ---------------------------------------------------------------------------
# Refinement A: extended Gaussian charge Coulomb energy
# ---------------------------------------------------------------------------
def coulomb_pair_extended(r, sigma_q=SIGMA_Q):
    """V_C^(A)(r) for two identical Gaussian charges at separation r.

    V_C^(A)(r) = k_C·q²/r · erf(r/(2σ_q))
    with prefactor k_C·(2e)² = 5.76 MeV·fm absorbed into COULOMB_AA.
    """
    return COULOMB_AA / r * erf(r / (2*sigma_q))


def coulomb_pair_pointcharge(r):
    """Phase 6 point-charge V_C^(0)(r) = k_C·q²/r."""
    return COULOMB_AA / r


def coulomb_total_extended(verts, sigma_q=SIGMA_Q):
    """V_C^A(0) = Σ pairs of V_C^(A)(r_ij) at canonical geometry."""
    n = len(verts); V = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r_ij = np.linalg.norm(verts[i]-verts[j])
            V += coulomb_pair_extended(r_ij, sigma_q)
    return V


def coulomb_total_pointcharge(verts):
    """V_C^(0)(0) Phase 6 reference."""
    n = len(verts); V = 0.0
    for i in range(n):
        for j in range(i+1, n):
            r_ij = np.linalg.norm(verts[i]-verts[j])
            V += coulomb_pair_pointcharge(r_ij)
    return V


def precompute_pair_distances(verts):
    """Return list of pair distances at canonical geometry."""
    n = len(verts); pairs = []
    for i in range(n):
        for j in range(i+1, n):
            pairs.append(np.linalg.norm(verts[i]-verts[j]))
    return pairs


# ---------------------------------------------------------------------------
# Force balance for extended-charge Coulomb
# ---------------------------------------------------------------------------
def coulomb_force_extended(delta_R, pair_distances_canon, sigma_q=SIGMA_Q,
                            R_canon=R_alpha):
    """Coulomb force pushing for expansion under uniform δR scaling.

    F_C^A(δR) = -∂V_C^(A,total)/∂(δR)
    Each pair: r_ij(δR) = r_ij^canon · (1 + δR/R_canon)
    Force per pair = -dV_C^(A)(r)/dr · dr/dδR = -dV_C/dr · r_ij^canon/R_canon
                   = (r_ij^canon/R_canon) · {erf/r² - exp/(σ_q √π r)} · k_C·q²
    Summing over pairs.
    """
    s = 1.0 + delta_R / R_canon
    F = 0.0
    inv_sqrt_pi = 1.0 / math.sqrt(math.pi)
    for r0 in pair_distances_canon:
        r = r0 * s
        x = r / (2*sigma_q)
        # dV_C/dr = k_C·q² · [-erf(x)/r² + (1/(r·σ_q √π)) exp(-x²)]
        # Force on δR = -dV_C/dr · (r0/R_canon)
        dVdr = COULOMB_AA * (-erf(x)/r**2 + inv_sqrt_pi/(r*sigma_q) * math.exp(-x*x))
        F += -dVdr * (r0 / R_canon)
    return F


def k3_force(delta_R, n_edges, sigma_K3=sigma_K3_canon):
    """K_3 restoring force magnitude: |E|·B_pair·(δR/σ²)·exp(-δR²/(2σ²)).

    Equilibrium condition F_C^A(δR) = |F_K3(δR)|.
    """
    return n_edges * B_pair * (delta_R/sigma_K3**2) * math.exp(-delta_R**2/(2*sigma_K3**2))


def solve_equilibrium_pointcharge(verts, n_edges, sigma_K3=sigma_K3_canon,
                                    R_canon=R_alpha, search_max=10.0):
    """Phase 6 point-charge reference equilibrium: solves
       V_C(0)·R/(R+dr)² = |E|·B_pair·(dr/σ²)·exp(-dr²/(2σ²))
    using stepping search for first sign change (like original Phase 6 script).
    """
    VC0 = coulomb_total_pointcharge(verts)
    def F(dr):
        return VC0 * R_canon/(R_canon+dr)**2 - n_edges*B_pair*(dr/sigma_K3**2)*math.exp(-dr**2/(2*sigma_K3**2))
    if F(0.0) <= 0:
        return 0.0
    n_steps = 1000
    delta_step = search_max/n_steps
    for k in range(1, n_steps+1):
        dr = k*delta_step
        if F(dr) < 0:
            try:
                return brentq(F, dr-delta_step, dr, xtol=1e-7)
            except ValueError:
                return dr
    return None
    """K_3 restoring force: F_K3(δR) = -|E|·B_pair·(δR/σ²)·exp(-δR²/(2σ²))

    Negative for δR > 0 (restoring back to canonical).  We use the magnitude
    |F_K3| = |E|·B_pair·(δR/σ²)·exp(-δR²/(2σ²)) for the equilibrium condition
    F_C^A = |F_K3|.
    """
    return n_edges * B_pair * (delta_R/sigma_K3**2) * math.exp(-delta_R**2/(2*sigma_K3**2))


def solve_equilibrium_refA(pair_distances_canon, n_edges,
                            sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon,
                            R_canon=R_alpha, search_max=10.0):
    """Solve F_C^A(δR) = |F_K3(δR)|  ↔  net force = 0 for equilibrium δR_eq."""
    def net(dr):
        return coulomb_force_extended(dr, pair_distances_canon, sigma_q, R_canon) \
             - k3_force(dr, n_edges, sigma_K3)
    # net(0) = F_C^A(0) > 0 (cluster wants to expand)
    if net(0.0) <= 0:
        return 0.0
    # Step out to find first sign change
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


def total_potential(delta_R, pair_distances_canon, n_edges,
                     sigma_q=SIGMA_Q, sigma_K3=sigma_K3_canon, R_canon=R_alpha):
    """V_total^(A)(δR) = V_C^(A,total)(δR) + V_K3(δR), all relative to δR=0."""
    s = 1.0 + delta_R/R_canon
    V_C = sum(coulomb_pair_extended(r0*s, sigma_q) for r0 in pair_distances_canon)
    V_K3 = -n_edges * B_pair * math.exp(-delta_R**2/(2*sigma_K3**2))
    return V_C + V_K3


# ---------------------------------------------------------------------------
# Smooth-A vs polytope-residual decomposition (Phase 7 methodology)
# ---------------------------------------------------------------------------
def detrend_linear(N_arr, y_arr):
    """Fit y = a·N + b, return (a, b, residuals)."""
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
    print("SS-9 OPEN-SS-32 ↔ U-shape — Phase 8 Refinement A "
          "(extended Gaussian alpha charge)")
    print("="*132)
    print()
    print("Q: Does extended Gaussian alpha charge distribution (radius "
          "1.68 fm, σ_q = 0.970 fm) generate")
    print("   polytope-specific residual structure that simple Phase 6 "
          "point-charge missed?")
    print()
    print("Phase 4-7 lesson applied: F1 sign analytical check FIRST, before "
          "computation.")
    print()
    print("Pre-empted F1 sign argument (sign-theorem composition workflow, "
          "Phase 6 §5.2):")
    print("  Level 1 (within-mechanism): erf(r/(2σ_q)) > 0 for r > 0, so "
          "extended-charge Coulomb")
    print("                              still purely repulsive → δR_A > 0 → "
          "Phase 5 sign theorem")
    print("                              → ΔE_R3 > 0 = empirical-required.  "
          "F1 PASSES analytically.")
    print("  Level 2 (empirical-comparison): smooth-A binding gain still "
          "positive (cluster more bound)")
    print("                              same direction as empirical α-cluster "
          "binding excess.  F1 SIGN")
    print("                              COMPATIBLE at smooth-A level; "
          "polytope-residual level needs computation.")
    print()
    print(f"Constants: B_pair = {B_pair:.3f} MeV, R_canon = {R_alpha} fm, "
          f"σ_K3 = {sigma_K3_canon} fm, (2e)²·k_C = {COULOMB_AA} MeV·fm")
    print(f"Refinement A: alpha rms charge radius = {R_ALPHA_CHARGE} fm, "
          f"σ_q = {SIGMA_Q:.4f} fm")
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

    # ---- V_C comparison: point-charge vs extended ----
    print("Coulomb energy V_C(0): point-charge (Phase 6) vs extended (Phase 8 A)")
    print(f"  {'N':>3} {'sym':>5} {'#NN':>4} {'#nonNN':>7} "
          f"{'NN frac':>8} {'V_C^(0) MeV':>12} "
          f"{'V_C^(A) MeV':>12} {'softening %':>12}")
    print("  " + "-"*90)
    p6_VC, p8_VC, NN_fracs = [], [], []
    for N, name, sym, v, edges, pds in cluster_data:
        n_pairs = len(pds)
        n_NN = len(edges)
        n_nonNN = n_pairs - n_NN
        nn_frac = n_NN / n_pairs if n_pairs else 0
        VC_p6 = coulomb_total_pointcharge(v)
        VC_p8 = coulomb_total_extended(v)
        soft_pct = (1 - VC_p8/VC_p6) * 100
        print(f"  {N:>3} {sym:>5} {n_NN:>4} {n_nonNN:>7} {nn_frac:>8.3f} "
              f"{VC_p6:>12.3f} {VC_p8:>12.3f} {soft_pct:>12.3f}")
        p6_VC.append(VC_p6); p8_VC.append(VC_p8); NN_fracs.append(nn_frac)
    print()
    print(f"  Softening varies from {min((1-p8_VC[i]/p6_VC[i])*100 for i in range(len(p6_VC))):.2f}% (low-NN-fraction)")
    print(f"  to {max((1-p8_VC[i]/p6_VC[i])*100 for i in range(len(p6_VC))):.2f}% "
          "(high-NN-fraction).  Differential softening = polytope-specific signature.")
    print()

    # ---- Equilibrium δR_C^A and ΔE/α ----
    print("Equilibrium δR_C^A and net binding gain per alpha (Phase 8 vs Phase 6):")
    print(f"  {'N':>3} {'sym':>5} {'V_C^A':>9} {'|E|·Bp':>9} "
          f"{'δR^A [fm]':>11} {'δR^(0) P6':>10} {'shift %':>9} "
          f"{'ΔE_K3^A':>9} {'ΔE/α^A':>9} {'ΔE/α^(0) P6':>13}")
    print("  " + "-"*120)
    p8_results = []
    for N, name, sym, v, edges, pds in cluster_data:
        n_edges = len(edges)
        VC_p8 = coulomb_total_extended(v)
        # Equilibrium with Refinement A
        dR_A = solve_equilibrium_refA(pds, n_edges)
        if dR_A is None:
            print(f"  {N:>3} {sym:>5} (no equilibrium for Phase 8)")
            continue
        ΔE_K3_A = n_edges * B_pair * (1 - math.exp(-dR_A**2/(2*sigma_K3_canon**2)))
        ΔE_alpha_A = ΔE_K3_A / N
        # Phase 6 point-charge result for comparison
        dR_p6 = solve_equilibrium_pointcharge(v, n_edges)
        if dR_p6 is None:
            dR_p6 = float('nan')
        ΔE_K3_p6 = n_edges * B_pair * (1 - math.exp(-dR_p6**2/(2*sigma_K3_canon**2)))
        ΔE_alpha_p6 = ΔE_K3_p6 / N
        shift_pct = (dR_A/dR_p6 - 1) * 100 if not math.isnan(dR_p6) else 0
        EE_B = n_edges * B_pair
        print(f"  {N:>3} {sym:>5} {VC_p8:>9.3f} {EE_B:>9.3f} "
              f"{dR_A:>11.4f} {dR_p6:>10.4f} {shift_pct:>+9.3f} "
              f"{ΔE_K3_A:>9.4f} {ΔE_alpha_A:>9.4f} {ΔE_alpha_p6:>13.4f}")
        p8_results.append((N, name, sym, VC_p8, dR_A, ΔE_K3_A, ΔE_alpha_A, ΔE_alpha_p6))
    print()

    # ---- Net binding gain per α (cluster more bound than canonical-no-expansion) ----
    print("Net binding gain per α (positive = cluster more bound than δR=0):")
    print(f"  {'N':>3} {'sym':>5} {'V_C^A_eq':>10} {'V_C^A(0)':>10} "
          f"{'Coul savings/α':>15} {'K3 loss/α':>11} {'net gain/α':>12}")
    print("  " + "-"*100)
    p8_net_gain = []
    for N, name, sym, v, edges, pds in cluster_data:
        n_edges = len(edges)
        VC_p8_canon = coulomb_total_extended(v)
        dR_A = solve_equilibrium_refA(pds, n_edges)
        if dR_A is None:
            continue
        s = 1 + dR_A/R_alpha
        VC_p8_eq = sum(coulomb_pair_extended(r0*s) for r0 in pds)
        coul_saving_per_alpha = (VC_p8_canon - VC_p8_eq) / N
        ΔE_K3_A = n_edges * B_pair * (1 - math.exp(-dR_A**2/(2*sigma_K3_canon**2)))
        K3_loss_per_alpha = ΔE_K3_A / N
        net_gain_per_alpha = coul_saving_per_alpha - K3_loss_per_alpha
        print(f"  {N:>3} {sym:>5} {VC_p8_eq:>10.3f} {VC_p8_canon:>10.3f} "
              f"{coul_saving_per_alpha:>15.4f} {K3_loss_per_alpha:>11.4f} "
              f"{net_gain_per_alpha:>+12.4f}")
        p8_net_gain.append((N, net_gain_per_alpha))
    print()

    # ---- Smooth-A vs polytope-residual decomposition (Phase 7 methodology) ----
    print("Smooth-A vs polytope-residual decomposition (Phase 7 methodology):")
    Ns = [item[0] for item in p8_net_gain]
    gains = [item[1] for item in p8_net_gain]
    a, b, resid_p8 = detrend_linear(Ns, gains)
    print(f"  Phase 8 net gain ≈ {a:.4f}·N + {b:+.4f} MeV/α (linear-in-N fit)")
    print(f"  Phase 8 polytope residuals (after detrending):")
    for i, (N, gn) in enumerate(p8_net_gain):
        print(f"    N={N:>2} ({AME_DATA[N][0]:>5}): residual = {resid_p8[i]:+.5f} MeV/α")
    print(f"  Phase 8 max |residual| = {max(abs(r) for r in resid_p8):.5f} MeV/α")
    print()

    # Phase 6 reference
    p6_net_gain = []
    for N, name, sym, v, edges, pds in cluster_data:
        n_edges = len(edges)
        VC_p6 = coulomb_total_pointcharge(v)
        dR_p6 = solve_equilibrium_pointcharge(v, n_edges)
        if dR_p6 is None or dR_p6 == 0:
            continue
        VC_p6_eq = VC_p6 * R_alpha/(R_alpha+dR_p6)
        coul_p6 = (VC_p6 - VC_p6_eq)/N
        ΔE_p6 = n_edges*B_pair*(1-math.exp(-dR_p6**2/(2*sigma_K3_canon**2)))/N
        p6_net_gain.append((N, coul_p6 - ΔE_p6))
    Ns_p6 = [item[0] for item in p6_net_gain]
    gains_p6 = [item[1] for item in p6_net_gain]
    a_p6, b_p6, resid_p6 = detrend_linear(Ns_p6, gains_p6)
    print(f"  Phase 6 reference: net gain ≈ {a_p6:.4f}·N + {b_p6:+.4f} MeV/α")
    print(f"  Phase 6 max |residual| = {max(abs(r) for r in resid_p6):.5f} MeV/α")
    print()

    # Empirical
    print("  Empirical Δ(B/A) - SEMF residuals after detrending (Phase 7 verbatim):")
    emp_dBA = []
    for N in Ns:
        nuc, A, Z, B_emp = AME_DATA[N]
        BA_emp = B_emp/A
        BA_semf = semf_baseline(A, Z)/A
        emp_dBA.append((N, BA_emp - BA_semf))
    Ns_emp = [item[0] for item in emp_dBA]
    dBA_emp = [item[1] for item in emp_dBA]
    a_emp, b_emp, resid_emp = detrend_linear(Ns_emp, dBA_emp)
    print(f"    Empirical Δ(B/A) ≈ {a_emp:.5f}·N + {b_emp:+.5f} MeV/α")
    print(f"    Empirical max |residual| = {max(abs(r) for r in resid_emp):.5f} MeV/α")
    print()

    # ---- F2 / F3 comparison ----
    print("F2 / F3 — polytope-residual comparison: Phase 8 vs Phase 6 vs empirical")
    print(f"  {'N':>3} {'nuc':>5} {'P6 resid':>10} {'P8 resid':>10} "
          f"{'emp resid':>10} {'P8 sign?':>10} {'P6 sign?':>10}")
    print("  " + "-"*80)
    sign_match_p8 = 0
    sign_match_p6 = 0
    for i, N in enumerate(Ns):
        emp = resid_emp[i]
        p6 = resid_p6[i] if i < len(resid_p6) else 0
        p8 = resid_p8[i]
        match_p8 = (np.sign(emp) == np.sign(p8) and abs(emp) > 0.001 and abs(p8) > 1e-6)
        match_p6 = (np.sign(emp) == np.sign(p6) and abs(emp) > 0.001 and abs(p6) > 1e-6)
        if match_p8: sign_match_p8 += 1
        if match_p6: sign_match_p6 += 1
        print(f"  {N:>3} {AME_DATA[N][0]:>5} {p6:>+10.5f} {p8:>+10.5f} "
              f"{emp:>+10.5f} {'YES' if match_p8 else 'no':>10} "
              f"{'YES' if match_p6 else 'no':>10}")
    print()
    print(f"  Phase 8 sign agreement: {sign_match_p8}/{len(Ns)} polytopes")
    print(f"  Phase 6 sign agreement: {sign_match_p6}/{len(Ns)} polytopes")
    print(f"  Phase 8 max residual = {max(abs(r) for r in resid_p8):.4f} MeV/α")
    print(f"  Phase 6 max residual = {max(abs(r) for r in resid_p6):.4f} MeV/α")
    print(f"  Empirical max residual = {max(abs(r) for r in resid_emp):.4f} MeV/α")
    p8_emp_ratio = max(abs(r) for r in resid_p8) / max(abs(r) for r in resid_emp)
    p6_emp_ratio = max(abs(r) for r in resid_p6) / max(abs(r) for r in resid_emp)
    print(f"  Phase 8/empirical magnitude ratio: {p8_emp_ratio:.3f}")
    print(f"  Phase 6/empirical magnitude ratio: {p6_emp_ratio:.3f}")
    print()

    # ---- Verdict ----
    print("="*132)
    print("VERDICT")
    print("="*132)
    print()
    print("F1 (sign): F1 PASSES at within-mechanism level (Refinement A → δR > 0 → ΔE > 0).")
    print("           F1 SIGN COMPATIBLE at smooth-A level (positive binding gain).")
    print(f"           Polytope-residual sign agreement: {sign_match_p8}/{len(Ns)} (vs Phase 6 {sign_match_p6}/{len(Ns)}).")
    print()
    print("F2 (magnitude):")
    print(f"  Phase 8 max polytope residual = {max(abs(r) for r in resid_p8):.4f} MeV/α")
    print(f"  Phase 6 max polytope residual = {max(abs(r) for r in resid_p6):.4f} MeV/α")
    print(f"  Empirical max polytope residual = {max(abs(r) for r in resid_emp):.4f} MeV/α")
    if p8_emp_ratio > p6_emp_ratio * 1.5:
        print("  Refinement A INCREASES polytope-residual magnitude toward empirical scale.")
    elif p8_emp_ratio < p6_emp_ratio * 0.7:
        print("  Refinement A DECREASES polytope-residual magnitude (counter-productive).")
    else:
        print("  Refinement A leaves polytope-residual magnitude approximately unchanged.")
    print()
    print("F3 (pattern): see polytope-by-polytope sign table above.")
    print()
    print("Phase 8 outcome depends on F2/F3 above; see companion sketch.")
    print()


if __name__ == '__main__':
    main()
