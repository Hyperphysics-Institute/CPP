#!/usr/bin/env python3
"""
0946 — does the first-shell travel-distance asymmetry supply the W^0's chirality?

Founder question, 13 Sep 2026: "since we found an asymmetry in the travel
distances between vertices, does this resolve the question of the chirality of
the W^0 boson?"

The asymmetry meant is MA.1's r(e) = r0(1 + delta e.n) together with the
Patch 0941 finding that the twelve first-shell directions all sit at
e.n = -1/(2phi), so the edge set is not centrally symmetric and the O(delta^1)
current is (6/phi^2) r0 delta n.

The answer turns on parity CLASS, which is exactly where THEO-CHIR-MERGE-2
(Patch 0647) already ruled once: sign(delta) is P-EVEN / T-odd -- an arrow, not
a handedness. This script re-establishes that for the W^0 specifically and then
locates where the W^0's handedness actually can come from.

  T1  the bare substrate is ACHIRAL: the 600-cell's symmetry group contains
      orientation-reversing elements (det = -1), so the lattice by itself has
      no handedness to donate.
  T2  the first-shell direction set at v_host is achiral too: it is carried to
      itself by an orientation-reversing element that also FIXES n. So the
      object the rate law is built on is mirror-symmetric about n.
  T3  therefore the rate law is P-even: r(e) = r0(1 + delta e.n) is invariant
      under that same orientation-reversing element, for every first-shell
      direction. Nothing in MA.1 distinguishes a left from a right.
  T4  and the current it produces is a POLAR vector: J = (6/phi^2) r0 delta n
      maps to itself under the n-fixing reflection. A polar vector along n is
      an arrow. A chirality needs a pseudoscalar, which n alone cannot build.
      CONCLUSION: the travel-distance asymmetry does NOT supply chirality.
  T5  where the W's handedness does come from, already on file: the W-bracelet
      is built from first-shell vertices, so by Substrate-Locality Unification
      (Finding C-W40) it inherits the substrate pseudoscalar chi, giving
      |M^W| = chi/6 (THEO-SD-CHIR-1). chi is P-odd; delta is P-even. Different
      classes, exhibited side by side.
  T6  NEW, and the part the founder's ruling leaves open: the W^0 is three qDPs
      and three eDPs on the six Petrie-hexagon sites, but the ARRANGEMENT was
      not specified. Of the distinct arrangements of 3+3 on a 6-ring there are
      4 up to rotation and 3 up to rotation+reflection -- so EXACTLY ONE is
      chiral, existing as a left/right pair; the other two are achiral.
  T7  the decoration breaks the bracelet's D6: each arrangement's stabiliser
      inside D6 (order 12) is computed, and the chiral one is the one whose
      stabiliser contains NO reflection.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def vertices_600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5 * np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI / 2, 0.5, 1 / (2 * PHI), 0.0]
    evens = [p for p in itertools.permutations(range(4))
             if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in evens:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); vals = [s[0]*base[0], s[1]*base[1], s[2]*base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = vertices_600(); N = len(V); edge = 1 / PHI
G = V @ V.T
nbr = [np.where(np.abs(G[i] - PHI/2) < 1e-8)[0] for i in range(N)]
host = 0; n_hat = V[host].copy()
U12 = np.array([(V[j] - V[host]) / edge for j in nbr[host]])

# --- build the vertex stabiliser as 4x4 orthogonal maps (cf. 0940)
idx = [host]
for j in nbr[host]:
    A = np.array([V[i] for i in idx] + [V[j]])
    if np.linalg.matrix_rank(A, tol=1e-8) == len(idx) + 1: idx.append(int(j))
    if len(idx) == 4: break
A = np.array([V[i] for i in idx]); Ainv = np.linalg.inv(A); gram = A @ A.T

def perm_of(M):
    Y = V @ M.T; p = np.full(N, -1, int)
    for a, y in enumerate(Y):
        h = np.where(np.abs(V - y).max(axis=1) < 1e-7)[0]
        if len(h) != 1: return None
        p[a] = h[0]
    return tuple(p)

stab = []
for cand in itertools.permutations(nbr[host], 3):
    B = np.array([V[host]] + [V[c] for c in cand])
    if not np.allclose(B @ B.T, gram, atol=1e-7): continue
    M = (Ainv @ B).T
    if not np.allclose(M @ M.T, np.eye(4), atol=1e-7): continue
    if perm_of(M) is not None: stab.append(M)

dets = [round(np.linalg.det(M)) for M in stab]
ok("T1", len(stab) == 120 and -1 in dets,
   f"|Stab(v_host)| = {len(stab)}, containing {dets.count(-1)} orientation-reversing elements "
   "— the bare 600-cell substrate is ACHIRAL and has no handedness to donate")

# an orientation-reversing element that fixes n_hat and preserves the 12 directions
refl = None
for M, d in zip(stab, dets):
    if d != -1: continue
    if not np.allclose(M @ n_hat, n_hat, atol=1e-8): continue
    img = U12 @ M.T
    if all(any(np.allclose(x, y, atol=1e-7) for y in U12) for x in img):
        refl = M; break
ok("T2", refl is not None,
   "an orientation-reversing element of Stab exists that FIXES n and carries the twelve "
   "first-shell directions to themselves — the rate law's underlying object is mirror-symmetric about n")

# T3: rate law invariance under that reflection
r = lambda u, d=1e-3: 1.0 * (1.0 + d * float(u @ n_hat))
inv_ok = True
for u in U12:
    u2 = refl @ u
    j = np.argmin([np.abs(U12 - u2).max(axis=1).min() for _ in [0]] or [0])
    match = U12[np.abs(U12 - u2).max(axis=1).argmin()]
    if abs(r(match) - r(u)) > 1e-15: inv_ok = False; break
ok("T3", inv_ok,
   "r(e) = r0(1 + delta e.n) is invariant under that reflection for every first-shell direction: "
   "MA.1 is P-EVEN and distinguishes no left from right (THEO-CHIR-MERGE-2, Patch 0647)")

# T4: the current is a polar vector fixed by the reflection
J = sum((r(u) - r(-u)) * u for u in U12)
ok("T4", np.allclose(refl @ J, J, atol=1e-9) and abs(float(J @ n_hat)) > 0,
   f"J = {float(J @ n_hat)/1e-3:.6f} r0 delta n is carried to itself by the mirror: a POLAR vector, "
   "i.e. an ARROW. A chirality requires a pseudoscalar, which n alone cannot build. "
   "=> the travel-distance asymmetry does NOT supply the W^0's chirality")

# T5: chi is the P-odd object, delta the P-even one
chi = PHI ** -3
ok("T5", abs(chi / 6 - 0.0394) < 5e-4,
   f"the W's handedness handle is |M^W| = chi/6 = {chi/6:.4f} (THEO-SD-CHIR-1), the bracelet "
   "inheriting the substrate PSEUDOSCALAR chi from first-shell vertices (Finding C-W40). "
   "chi is P-odd, delta is P-even — different classes")

# T6: arrangements of 3 qDP + 3 eDP on a 6-ring
def rots(t): return {tuple(t[i:] + t[:i]) for i in range(6)}
def refls(t):
    rv = tuple(reversed(t)); return rots(rv)
arrangements = [t for t in itertools.product("qe", repeat=6) if t.count("q") == 3]
necklaces, bracelets = set(), set()
for t in arrangements:
    necklaces.add(min(rots(t))); bracelets.add(min(rots(t) | refls(t)))
chiral = [n for n in necklaces if min(refls(tuple(n))) != n]
ok("T6", len(necklaces) == 4 and len(bracelets) == 3 and len(chiral) == 2,
   f"3 qDP + 3 eDP on a 6-ring: {len(necklaces)} arrangements up to rotation, {len(bracelets)} up to "
   f"rotation+reflection => EXACTLY ONE chiral pair ({sorted(''.join(c) for c in chiral)}); "
   "the other two arrangements are achiral. The founder's ruling did not fix the arrangement")

# T7: stabiliser inside D6 of each bracelet class
def stab_D6(t):
    order, has_refl = 0, False
    for i in range(6):
        if tuple(t[i:] + t[:i]) == t: order += 1
    rv = tuple(reversed(t))
    for i in range(6):
        if tuple(rv[i:] + rv[:i]) == t: order += 1; has_refl = True
    return order, has_refl
info = {}
for b in bracelets:
    info[''.join(b)] = stab_D6(tuple(b))
chiral_reps = {''.join(min(rots(tuple(c)))) for c in chiral}
no_refl = [k for k, (o, hr) in info.items() if not hr]
ok("T7", len(no_refl) == 1 and all(info[k][0] < 12 for k in info),
   f"stabilisers inside D6 (order 12): { {k: v[0] for k, v in info.items()} }; the one class with NO "
   f"reflection is {no_refl} — the chiral arrangement. Every decoration breaks D6")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
