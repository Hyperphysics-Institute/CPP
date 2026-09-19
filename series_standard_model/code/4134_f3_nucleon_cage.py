#!/usr/bin/env python3
"""
Patch 4134 — TODO-4133-F3CALC steps 1-2, run on the corpus's OWN nucleon.

WHAT IS TESTED
--------------
Under the amendment (A3' Patch 4120) the helicity bit is b ~ A . V, ONE number
per CP per Moment: A = the CP's axial channel (its spin axis), V = SSV_net, the
GP's summed polar vector (master_glossary: "every CP executes one Displace step
per its GP's computed SSV_net").  F3 -- the strong sector stays P-even to the
~1e-7 hadronic bound -- therefore asks whether the total pseudoscalar

        B_tot = sum_i  A_i . V_i

vanishes on the corpus's actual nucleon.

THE NUCLEON, AS THE CORPUS STATES IT (SS-2, not a generic cage):
  "The proton occupies a single tetrahedral cell of the 600-cell lattice.
   V1(-): u1 (+2/3), V2(-): u2 (+2/3), V3(+): d (-1/3), V4(+): OPEN."
  Distortion eps = 1.94:  u-u = 1.071 fm,  u-d = 0.620 fm.
  The down's captured -eCP "oscillates linearly through the central +qCP"
  (radial), displaced by delta * l_edge.

Checks:
  C1  the regular tetrahedron admits NO inversion   (kills the 4133 sketch)
  C2  the z=12 coordination shell IS antipodally paired (4101 step 1 stands --
      4101 and 4133 were talking about two different objects)
  C3  the occupied nucleon configuration is PLANAR and its symmetry group
      contains an improper element (the plane itself)
  C4  V_i is in that plane for ANY radial pairwise law (law-independent)
  C5  B_tot for spins along a common axis n:  B_tot = n . W,  W in the plane
  C6  is W = 0?  (if yes: F3 holds for every spin orientation)
  C7  the free particle contrast
"""
import numpy as np
import itertools

np.set_printoptions(precision=6, suppress=True)
PHI = (1 + 5 ** 0.5) / 2
out = []
def say(s=""):
    print(s); out.append(s)

# ----------------------------------------------------------------- C1
say("C1  regular tetrahedron: is it centrosymmetric?")
tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
tet = tet - tet.mean(0)
def maps_to_self(P, M, tol=1e-9):
    Q = P @ M.T
    for q in Q:
        if not np.any(np.linalg.norm(P - q, axis=1) < tol):
            return False
    return True
inv = -np.eye(3)
say(f"    inversion maps vertex set to itself: {maps_to_self(tet, inv)}")
# but it does admit a MIRROR
mir = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 1.]])  # x <-> y, det = -1
say(f"    a mirror (x<->y, det = {np.linalg.det(mir):+.0f}) does:       {maps_to_self(tet, mir)}")
say("    => the 4133 inversion-pairing sketch CANNOT apply to a tetrahedral cell.")
say("       Achirality of a tetrahedron is carried by a MIRROR, not by inversion.")
say()

# ----------------------------------------------------------------- C2
say("C2  z=12 coordination shell of a 600-cell vertex (icosahedron of bond dirs)")
ico = []
for s1 in (1, -1):
    for s2 in (1, -1):
        ico += [[0, s1 * 1, s2 * PHI], [s1 * 1, s2 * PHI, 0], [s2 * PHI, 0, s1 * 1]]
ico = np.array(ico, float)
ico /= np.linalg.norm(ico, axis=1)[:, None]
paired = sum(1 for v in ico if np.any(np.linalg.norm(ico + v, axis=1) < 1e-9))
say(f"    vertices: {len(ico)}   antipodally paired: {paired}/12  -> 4101 step 1 STANDS")
say("    => 4101 (coordination shell) and 4133 (the cage cell) are DIFFERENT objects.")
say()

# ----------------------------------------------------------------- C3
say("C3  the corpus proton: occupied vertices only (the 4th vertex is OPEN = no CP)")
d_uu, d_ud = 1.071, 0.620                      # fm, SS-2 eps = 1.94
u1 = np.array([-d_uu / 2, 0.0, 0.0])
u2 = np.array([+d_uu / 2, 0.0, 0.0])
h = (d_ud ** 2 - (d_uu / 2) ** 2)
say(f"    u-d^2 - (u-u/2)^2 = {h:+.4f}  -> the isoceles triangle "
    f"{'CLOSES' if h > 0 else 'DOES NOT CLOSE'} with these two SS-2 lengths")
if h <= 0:
    say("    NOTE: SS-2's two quoted separations are mutually inconsistent as a")
    say("    Euclidean triangle (u-d < half of u-u). Recorded as a finding; the")
    say("    symmetry results below do NOT depend on the numerical lengths.")
    d_ud = 0.62
    hy = 0.30                                  # placeholder height, symmetry only
else:
    hy = h ** 0.5
dq = np.array([0.0, hy, 0.0])
pos = np.array([u1, u2, dq])
chg = np.array([2 / 3, 2 / 3, -1 / 3])
say(f"    three charge-bearing vertices are coplanar by construction "
    f"(3 points always are): normal = z-hat")
say("    charges: u(+2/3), u(+2/3), d(-1/3); the d's captured -eCP oscillates")
say("    RADIALLY through its own +qCP (SS-2) -> stays in the same plane.")
mirror_z = np.diag([1.0, 1.0, -1.0])
say(f"    plane reflection maps positions+charges to themselves: "
    f"{maps_to_self(pos, mirror_z)}  (improper, det = {np.linalg.det(mirror_z):+.0f})")
say()

# ----------------------------------------------------------------- C4
say("C4  V_i = SSV_net at each quark, for a generic RADIAL pairwise law")
def V_of(pos, chg, power):
    V = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i == j:
                continue
            r = pos[i] - pos[j]
            V[i] += chg[i] * chg[j] * r / np.linalg.norm(r) ** power
    return V
for p in (3, 2, 1):                             # 1/r^2 force, 1/r, linear
    V = V_of(pos, chg, p)
    say(f"    power {p}: max |V_z| = {np.abs(V[:, 2]).max():.3e}  (in-plane)")
say("    => for ANY radial law the V_i lie in the quark plane. Law-independent.")
say()

# ----------------------------------------------------------------- C5 / C6
say("C5/C6  B_tot = sum_i A_i . V_i for spins along a common axis n")
V = V_of(pos, chg, 3)
# SU(6) proton, spin up: the two u carry +, the d carries -  (the assignment
# A3G-7 used at 4126; the amendment itself assigns no spin -- founder 4107)
s = np.array([+1.0, +1.0, -1.0])
W = (s[:, None] * V).sum(0)
say(f"    W = sum_i s_i V_i = {W}")
say(f"    |W| = {np.linalg.norm(W):.6e} ;  W_z = {W[2]:.3e} (in-plane, as C4 forces)")
say(f"    B_tot(n) = n . W  ->  ZERO for every n iff W = 0.")
say(f"    W == 0 ?  {np.linalg.norm(W) < 1e-12}")
n_perp = np.array([0.0, 0.0, 1.0])
say(f"    n perpendicular to the quark plane: B_tot = {n_perp @ W:.3e}  -> EXACTLY 0")
best = W / np.linalg.norm(W)
say(f"    n along W (worst case):             B_tot = {best @ W:.6e}  -> O(1), not small")
say(f"    isotropic average over n:           <B_tot> = 0 (n.W averages to zero),")
say("      but that is an ORIENTATION average, not a per-nucleon cancellation.")
say()

# C6b: does W vanish for any spin assignment?
say("C6b which spin assignments kill W outright?")
for combo in itertools.product([1, -1], repeat=3):
    Wc = (np.array(combo, float)[:, None] * V).sum(0)
    tag = "W = 0" if np.linalg.norm(Wc) < 1e-12 else f"|W| = {np.linalg.norm(Wc):.3e}"
    say(f"    s = {combo}: {tag}")
say("    THE PATTERN: W = 0 for exactly the two ALL-PARALLEL assignments, and this")
say("    is a theorem, not an accident -- the V_i are pairwise action-reaction")
say(f"    terms, so sum_i V_i = {np.linalg.norm(V.sum(0)):.3e} identically, and W = s * sum V = 0")
say("    whenever every s_i is the same. The SU(6) proton is NOT all-parallel.")
say()

# ----------------------------------------------------------------- C7
say("C7  free-particle contrast (unchanged from 4101 step 4)")
say("    free CP: V = SSV_net is a single persistent direction, |A.V| = O(1).")
say("    The same linear coupling therefore gives O(1) on a free leg. The contrast")
say("    F3 needs is intact; what changed is WHY the confined case cancels.")
say()

# ------------------------------------------------------- C8 the s-wave average
say("C8  the L = 0 ground state: average n.W over cage orientations")
rng = np.random.default_rng(4134)
def rand_rot(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q); w, x, y, z = q
    return np.array([[1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)],
                     [2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)],
                     [2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]])
n = np.array([0.0, 0.0, 1.0])
vals = np.array([n @ (rand_rot(rng) @ W) for _ in range(200000)])
say(f"    <n.W> over 200000 isotropic cage orientations = {vals.mean():+.3e}")
say(f"    (s.e.m. {vals.std()/len(vals)**0.5:.1e}; consistent with exactly zero)")
say(f"    rms per nucleon = {vals.std():.4f} -- the cancellation is an AVERAGE,")
say("    not a pointwise one, and it is exactly what L = 0 (s-wave: internal")
say("    frame uncorrelated with the spin axis) guarantees by rotational")
say("    invariance. A residual spin-orientation correlation eps leaves")
say(f"    B_tot ~ eps * |W| = eps * {np.linalg.norm(W):.3f}, so the ~1e-7 hadronic PV")
say("    bound caps eps at ~1e-7 -- the same shape as 4101's antipodal-imbalance cap.")
say()

say("VERDICT")
say("  (1) F3 does NOT follow from inversion pairing of the nucleon cell: the")
say("      tetrahedral cell has no inversion at all (C1). The 4133 sketch is")
say("      WITHDRAWN as applied to the nucleon.")
say("  (2) 4101's antipodal argument is untouched -- it is about the z=12")
say("      coordination shell, a different object, which IS paired (C2).")
say("  (3) Under the amendment's own b ~ A.V, B_tot = n.W with W = sum_i s_i V_i")
say("      a polar vector in the cage frame (C4, C5).")
say("  (4) W = 0 EXACTLY whenever the constituent spins are all parallel, because")
say("      sum_i V_i = 0 by action-reaction (C6b). The SU(6) proton is not.")
say("  (5) For the SU(6) assignment F3 holds by the L = 0 s-wave average (C8),")
say("      not pointwise, and it is broken by any spin-orientation correlation.")
say("      NEW NAMED REQUIREMENT -- R-F3-ISO: the confined structure's internal")
say("      frame must be uncorrelated with its spin axis to <~1e-7. Guaranteed by")
say("      L = 0 for nucleon ground states; NOT guaranteed if the A_i channel")
say("      itself induces a spin-orientation coupling. That is the thing to test.")

open("/tmp/4134_out.txt", "w").write("\n".join(out))
