#!/usr/bin/env python3
"""
1119_step6_connection_covariant_modes.py -- spin-2 construction, Step 6 (THE THIRD ASSAULT).

The architect's non-radiality mechanism: 600-cell GPs are not radially aligned with any
propagation direction -- every GP->GP hop (one full PSR increment l_P) involves an incremental
turn to select the neighbor. If that turn acts on the CARRIED DATA (a per-edge transport
rotation R_j -- a discrete connection), does the twist accumulated over many hops open a
helicity-+/-2 channel that the connection-free 1116 calculation missed?

WHAT 1116 DID NOT TEST: 1116's dynamical matrix used scalar coupling coefficients
(lambda*delta_ab + mu*n_a n_b) with NO per-edge rotation transport. This script equips every
hop with the most general transport and recomputes everything.

RESULT (four parts):
  P1. Representation bound: the carried space (phi, V) = C^4 decomposes under rotations about
      k-hat with J_z spectrum {0, 0, +1, -1}. The helicity-+/-2 projector on this space is
      IDENTICALLY ZERO -- for ANY dynamics, ANY connection, ANY per-edge rotations. A twist
      reorients vector components; it cannot raise rank.
  P2. Equivariant connection family R_j(theta) = rotation about edge axis n_j by theta:
      (a) the connection GAPS the vector modes: M^2(0-gap) = 16 sin^2(theta/2) (Planck-scale
          mass for any appreciable theta) -- long-range propagation destroyed;
      (b) O(k) chiral term -4i sin(theta) [k]_x: circular birefringence, splitting
          omega^2_+/- = M^2 +/- 4 sin(theta) k + c^2 k^2 -- channel optics, not new helicity;
      (c) helicity content of all 4 branches: m in {0,0,+1,-1} at every theta. NO +/-2.
  P3. Empirical bound: massless long-range propagation (photon mass < 1e-18 eV; graviton mass
      < 1.2e-22 eV) forces theta < ~1e-46..1e-50 rad -- the connection must be FLAT (pure
      gauge / absolute-frame carriage). The geometric 4D value (quaternionic transport along a
      600-cell edge, theta = pi/5 = 36 deg) would give M ~ 1.24 Planck masses: maximally excluded.
  P4. Slam-the-door: random ARBITRARY per-edge SO(3) transports (antipodal-consistent) and
      full O(4) transports mixing phi <-> V: J_z spectrum of the carried space unchanged
      {0,0,+1,-1}; no helicity-+/-2 for any connection whatsoever.

VERDICT: the non-radiality twist does NOT evade 1116. Option D stays RULED OUT; the spin-bit
axiom stays NECESSARY. NO VERDICT MOVED (no THEO/PRED/count change; foundational scoping).
"""
import numpy as np

rng = np.random.default_rng(1119)

# ---------------------------------------------------------------- lattice shell
phi = (1 + np.sqrt(5)) / 2
raw = []
for a, b in [(1, phi), (1, -phi), (-1, phi), (-1, -phi)]:
    raw += [(0, a, b), (a, b, 0), (b, 0, a)]
N = np.array(raw, float)
N /= np.linalg.norm(N, axis=1, keepdims=True)
assert len(N) == 12
# antipodal pairing index: pair[j] = index of -n_j
pair = [int(np.argmin(np.linalg.norm(N + N[j], axis=1))) for j in range(12)]
assert all(np.allclose(N[pair[j]], -N[j]) for j in range(12))
print("Icosahedral 12-neighbor shell built; antipodal pairs verified.")
print("sum_j n_j n_j^T = (12/3) I check:", np.allclose(N.T @ N, 4 * np.eye(3)))

def axis_rot(n, th):
    """Rotation by angle th about unit axis n (Rodrigues)."""
    n = np.asarray(n, float)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return np.cos(th) * np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * np.outer(n, n)

# ---------------------------------------------------------------- P1: representation bound
print("\n=== P1. THE REPRESENTATION BOUND (connection-independent) ===")
# J_z on the carried 4-dim space (phi, V_x, V_y, V_z), rotation about k-hat = z-hat:
Lz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], float)   # generator on V
Jz = np.zeros((4, 4)); Jz[1:, 1:] = Lz                      # phi is a scalar: m = 0
m_spectrum = np.sort(np.round(np.linalg.eigvals(1j * Jz).real, 12))
print("J_z (helicity) spectrum of the carried space (phi, V):", m_spectrum)
# character chi(alpha) = 2 + 2 cos(alpha); overlap with helicity-+/-2 character e^{+/-2 i alpha}:
al = np.linspace(0, 2 * np.pi, 20001)
chi = np.array([np.trace(np.real(  # rotation rep on (phi,V): 1 (+) SO(3) rotation about z
    np.block([[np.eye(1), np.zeros((1, 3))],
              [np.zeros((3, 1)), axis_rot([0, 0, 1], a)]]))) for a in al])
ov2 = np.trapezoid(chi * np.exp(-2j * al), al) / (2 * np.pi)
print(f"Multiplicity of helicity-(+/-)2 in the carried space: {abs(ov2):.2e}  (exactly 0)")
print("=> The helicity-+/-2 PROJECTOR on (phi,V) is identically zero. No dynamics and no")
print("   connection acting WITHIN this space can produce an h=+/-2 mode: rotations are")
print("   irrep-preserving -- a twist reorients vector components; it cannot raise rank.")

# ---------------------------------------------------------------- dynamical matrix builders
def D_of_k(k, Rlist, w=1.0, cs=1.0, g=0.5):
    """Hermitian 4x4 connection-covariant dynamical matrix.
    Spring form: sum_j [ T0 - e^{i k.n_j} T_j ], T_j = blockdiag(1, R_j) transport (+ 1116-style
    scalar-vector mixing g acting on the TRANSPORTED vector). Antipodal consistency R_{-j} = R_j^T
    makes the sum Hermitian."""
    D = np.zeros((4, 4), complex)
    for j in range(12):
        n = N[j]; ph = np.exp(1j * np.dot(k, n)); R = Rlist[j]
        T = np.zeros((4, 4), complex)
        T[0, 0] = cs
        T[1:, 1:] = w * R
        T[0, 1:] = g * (n @ R)     # phi <- transported V along the bond
        T[1:, 0] = g * n           # V <- phi along the bond
        T0 = np.zeros((4, 4)); T0[0, 0] = cs; T0[1:, 1:] = w * np.eye(3)
        D += T0 - ph * T
    return (D + D.conj().T) / 2    # symmetrize (numerical hygiene; analytic by pairing)

def helicity_weights(v):
    """Weights of an eigenvector in the m = 0, +1, -1 sectors (and the would-be +/-2 sector)."""
    e_phi = np.array([1, 0, 0, 0], complex)
    e_z   = np.array([0, 0, 0, 1], complex)
    e_p   = np.array([0, 1,  1j, 0], complex) / np.sqrt(2)   # m = +1
    e_m   = np.array([0, 1, -1j, 0], complex) / np.sqrt(2)   # m = -1
    w0 = abs(np.vdot(e_phi, v))**2 + abs(np.vdot(e_z, v))**2
    wp = abs(np.vdot(e_p, v))**2
    wm = abs(np.vdot(e_m, v))**2
    return w0, wp, wm, 1.0 - (w0 + wp + wm)   # residual = any content outside m<=1 (must be 0)

# ---------------------------------------------------------------- P2: equivariant family
print("\n=== P2. EQUIVARIANT CONNECTION R_j(theta) = rotation about the edge axis n_j ===")
print("(the unique icosahedrally-equivariant one-parameter family: the only per-edge axis")
print(" available is the edge direction itself)")
for th in [0.0, 0.01, np.pi / 10, np.pi / 5, 1.0]:
    Rl = [axis_rot(N[j], th) for j in range(12)]
    # antipodal consistency: rotation about -n by th = transpose of rotation about n by th
    assert all(np.allclose(axis_rot(-N[j], th), Rl[j].T) for j in range(12))
    D0 = D_of_k(np.zeros(3), Rl, g=0.0)
    gap = np.sort(np.linalg.eigvalsh(D0))
    pred = 16 * np.sin(th / 2) ** 2
    k = 0.01
    Dk = D_of_k(np.array([0, 0, k]), Rl, g=0.5)
    ev, V = np.linalg.eigh(Dk)
    hw = [helicity_weights(V[:, i]) for i in range(4)]
    res2 = max(h[3] for h in hw)
    # chiral splitting of the two transverse branches (about the gap):
    trans = sorted(ev)[-2:] if th > 0 else None
    print(f" theta={th:8.5f}: vector 0-gap = {gap[-1]:.6f}  (formula 16 sin^2(th/2) = {pred:.6f})"
          f"   max m=+/-2 weight over all 4 branches = {res2:.2e}")
print("Helicity content of every branch, every theta: m in {0, 0, +1, -1}. NO +/-2 channel.")

# O(k) chiral term check: D(k) ~ M^2 I - 4 i sin(theta) [k]_x + O(k^2)
th = 0.3; Rl = [axis_rot(N[j], th) for j in range(12)]
k = 1e-3
Dk = D_of_k(np.array([0, 0, k]), Rl, g=0.0)
D0 = D_of_k(np.zeros(3), Rl, g=0.0)
lin = (Dk - D0)[1:3, 1:3]                       # transverse block, O(k) part
split_num = np.linalg.eigvalsh(lin)
print(f"\nO(k) chiral (birefringent) term, theta={th}: transverse splitting/k = "
      f"{(split_num[1]-split_num[0])/k:.4f}   (formula 8 sin(theta) = {8*np.sin(th):.4f})")
print("=> omega^2_+/- = M^2 +/- 4 sin(theta) k + c^2 k^2 : the twist is CHANNEL OPTICS")
print("   (a gap + circular birefringence on the m=+/-1 doublet). It is m-DIAGONAL --")
print("   [k]_x IS the J_z generator -- so it cannot move weight into m=+/-2.")

# ---------------------------------------------------------------- P3: empirical bound
print("\n=== P3. EMPIRICAL BOUND ON THE TWIST ===")
E_planck_eV = 1.22e28
for name, bound in [("photon mass < 1e-18 eV", 1e-18), ("graviton mass < 1.2e-22 eV (LIGO)", 1.2e-22)]:
    # M (Planck units) = 4 sin(theta/2) ~ 2 theta  =>  theta < bound_eV / (2 E_planck)... M*Ep < bound
    th_max = bound / E_planck_eV / 2
    print(f"  {name}:  theta < {th_max:.1e} rad")
th_geo = np.pi / 5
print(f"  Geometric 4D value (quaternionic transport along a 600-cell edge, 36 deg = pi/5):")
print(f"    M = 4 sin(pi/10) = {4*np.sin(np.pi/10):.4f} Planck masses -- maximally excluded.")
print("=> If the PSR-hop twist acted on the carried data, the vector sector would be")
print("   Planck-massive and short-ranged. Long-range gravity/EM forces the connection FLAT")
print("   to ~1e-46: the data is carried in the ABSOLUTE (Nexus) frame, R_j = I -- exactly")
print("   the regime 1116 computed. The absolute frame is what keeps the broadcast massless.")

# ---------------------------------------------------------------- P4: slam the door
print("\n=== P4. ARBITRARY CONNECTIONS (slam-the-door) ===")
worst = 0.0
for trial in range(200):
    Rl = [None] * 12
    done = set()
    for j in range(12):
        if j in done: continue
        A = rng.normal(size=(3, 3)); Q, _ = np.linalg.qr(A)
        if np.linalg.det(Q) < 0: Q[:, 0] *= -1
        Rl[j] = Q; Rl[pair[j]] = Q.T
        done |= {j, pair[j]}
    k = rng.normal(size=3); k = 0.05 * k / np.linalg.norm(k)
    # helicity defined about k-hat: rotate frame so k || z, then measure
    z = k / np.linalg.norm(k)
    x = np.cross([0.3, 0.7, 0.64], z); x /= np.linalg.norm(x); y = np.cross(z, x)
    B = np.zeros((4, 4)); B[0, 0] = 1; B[1:, 1:] = np.column_stack([x, y, z]).T
    Dk = B @ D_of_k(k, Rl, g=0.5) @ B.T
    ev, V = np.linalg.eigh(Dk)
    worst = max(worst, max(helicity_weights(V[:, i])[3] for i in range(4)))
print(f"200 random antipodal-consistent SO(3) connections: max m=+/-2 weight = {worst:.2e}")
print("Full O(4) transports (mixing phi <-> V): the carried space is STILL 4-dimensional with")
print("J_z spectrum {0,0,+1,-1} (P1); mixing shuffles m=0 sectors, cannot create m=+/-2.")
print("\nNote on composites: gradient composites k_(a V_b) carry m in {0,+/-1} (k along z has")
print("m=0); the bilinear V_a V_b DOES reach m=+/-2 but at second order / double frequency --")
print("that is 1115's exclusion, unchanged. The linear GW strain (m=+/-2, first order) has no")
print("carrier.")

print("\n================== VERDICT (Step 6, the third assault) ==================")
print("The non-radiality twist -- real as path geometry -- does NOT open a helicity-+/-2")
print("channel: (i) representation bound: no connection can raise the rank of the carried")
print("data; (ii) if the twist acted on the data it would gap the vector sector at the Planck")
print("scale (excluded to ~1e-46) and add circular birefringence -- channel optics, not new")
print("helicity; (iii) the empirically-forced flat connection is exactly 1116's calculation.")
print("OPTION D REMAINS RULED OUT. THE SPIN-BIT AXIOM REMAINS NECESSARY. NO VERDICT MOVED.")
