#!/usr/bin/env python3
"""
Patch 2491 -- SR-MECH-2485 Step 3 -- M1: canonical uniqueness of the
distinguished 2-plane for a uniformly moving aggregate.

Verifies the invariant-theory claims of the M1 derivation
(SR-MECH-2485_mechanism_session.md, step 3). stdlib only (F3/numpy
convention ruling still owed; per 2488/2489 practice). Fixed seed.

Setup: absolute-frame orthonormal basis (e0, e1, e2, e3) with
  e0 = tau_hat        (Absolute Moment axis, c01: universal, fixed)
  e1 = e_motion       (aggregate's absolute velocity direction)
  e2, e3 span P_perp  (the spatial plane orthogonal to e_motion)
Pi      = span(tau_hat, e_motion)   -- the candidate-(a) plane
P_perp  = span(e2, e3)

Arena symmetry (A3' C2 flat isotropic transport + M4 ball verdict):
spatial SO(3) fixing tau_hat. Stabilizer of the data {tau_hat, e_motion}:
SO(2) rotations about e_motion, acting as identity on span(tau_hat,
e_motion) and as R(theta) on P_perp.

Checks:
  V1  Pi and P_perp are SO(2)-invariant for generic theta; random
      2-planes are not (any random plane passing invariance is, in fact,
      Pi or P_perp to tolerance).
  V2  Exactly-two: the structured mixed family plane(alpha, beta) =
      span(line-in-Pi(alpha), line-in-P_perp(beta)) fails invariance for
      ALL (alpha, beta) under generic theta -- no third invariant plane
      hides in the mixed family (rep theory: trivial^2 (+) rot(theta)
      admits no other invariant 2-dim subspace at generic theta).
  V3  k = 1 and k = 3 have CONTINUA of invariant subspaces (every line
      in Pi is invariant; so is each line's orthocomplement) -- no
      unique distinguished line or 3-space exists. k = 2 is the unique
      dimension with a finite invariant set.
  V4  v -> 0 limit: stabilizer grows to full SO(3); NO 2-plane survives
      (Pi, P_perp, mixed planes, and span(tau_hat, u) all fail under a
      generic spatial rotation); only span(tau_hat) (k=1) and the
      spatial 3-space (k=3) remain invariant. Consistent with d = v*t_P
      = 0: the plane ceases to exist exactly where nothing needs it.
  V5  BROKEN BRANCH (kill-liveness, kept per 2488/2489 practice): if the
      residual symmetry about e_motion were the discrete C2 = {1, R(pi)}
      instead of continuous SO(2), the ENTIRE mixed family plane(alpha,
      beta) becomes invariant (R(pi) = -1 on P_perp fixes every line) --
      a two-parameter continuum; uniqueness DIES. The continuous
      isotropy delivered by A3' C2 + M4 is load-bearing; the kill was
      live.
  V6  The per-Moment displacement 4-vector Delta(v) = c*t_P*tau_hat +
      v*t_P*e_motion lies in Pi exactly and has identically zero
      P_perp-projection, for all sampled v in (0, c) -- Pi is the unique
      invariant 2-plane CONTAINING the data; P_perp contains none of it.
"""

import math
import random

random.seed(2491)

TOL_ZERO = 1e-12   # "invariant" threshold
TOL_FAIL = 1e-3    # "definitely not invariant" threshold


# ----------------------------------------------------------------------
# minimal 4D linear algebra (stdlib)
# ----------------------------------------------------------------------

def mat_mul(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)]
            for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def mat_sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def fro_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def gram_schmidt(cols):
    """Orthonormalize a list of 4-vectors (columns); returns list or None."""
    out = []
    for v in cols:
        w = list(v)
        for u in out:
            d = sum(a * b for a, b in zip(w, u))
            w = [a - d * b for a, b in zip(w, u)]
        n = math.sqrt(sum(a * a for a in w))
        if n < 1e-10:
            return None
        out.append([a / n for a in w])
    return out


def projector(basis_vectors):
    """P = B B^T for orthonormal basis vectors (list of 4-vectors)."""
    B = gram_schmidt(basis_vectors)
    assert B is not None, "degenerate basis"
    P = [[0.0] * 4 for _ in range(4)]
    for u in B:
        for i in range(4):
            for j in range(4):
                P[i][j] += u[i] * u[j]
    return P


def deviation(R, P):
    """|| R P R^T - P ||_F  -- zero iff the subspace is R-invariant."""
    return fro_norm(mat_sub(mat_mul(mat_mul(R, P), transpose(R)), P))


def rot_about_e1(theta):
    """Stabilizer element: identity on span(e0, e1), R(theta) on P_perp."""
    c, s = math.cos(theta), math.sin(theta)
    return [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, c, -s],
            [0, 0, s, c]]


def givens(i, j, theta):
    R = [[1.0 if a == b else 0.0 for b in range(4)] for a in range(4)]
    c, s = math.cos(theta), math.sin(theta)
    R[i][i] = c
    R[j][j] = c
    R[i][j] = -s
    R[j][i] = s
    return R


def random_spatial_rotation():
    """Random SO(3) on coords (1,2,3), fixing e0 = tau_hat (c01/SR-1)."""
    R = givens(1, 2, random.uniform(0.3, 2.8))
    R = mat_mul(R, givens(1, 3, random.uniform(0.3, 2.8)))
    R = mat_mul(R, givens(2, 3, random.uniform(0.3, 2.8)))
    return R


def random_plane():
    while True:
        cols = [[random.gauss(0, 1) for _ in range(4)] for _ in range(2)]
        B = gram_schmidt(cols)
        if B is not None:
            return projector(B)


E0 = [1, 0, 0, 0]
E1 = [0, 1, 0, 0]
E2 = [0, 0, 1, 0]
E3 = [0, 0, 0, 1]

P_PI = projector([E0, E1])
P_PERP = projector([E2, E3])


def line_in_pi(alpha):
    return [math.cos(alpha), math.sin(alpha), 0, 0]


def line_in_perp(beta):
    return [0, 0, math.cos(beta), math.sin(beta)]


def mixed_plane(alpha, beta):
    return projector([line_in_pi(alpha), line_in_perp(beta)])


results = {}

# ----------------------------------------------------------------------
# V1 -- Pi, P_perp invariant; random planes not (unless they ARE Pi/P_perp)
# ----------------------------------------------------------------------
thetas = [random.uniform(0.2, math.pi - 0.2) for _ in range(20)]
v1_pi = max(deviation(rot_about_e1(t), P_PI) for t in thetas)
v1_pp = max(deviation(rot_about_e1(t), P_PERP) for t in thetas)
v1_ok = v1_pi < TOL_ZERO and v1_pp < TOL_ZERO
n_false_pos = 0
for _ in range(200):
    P = random_plane()
    dev = max(deviation(rot_about_e1(t), P) for t in thetas)
    if dev < 1e-8:
        near = min(fro_norm(mat_sub(P, P_PI)), fro_norm(mat_sub(P, P_PERP)))
        if near > 1e-4:
            n_false_pos += 1
v1_ok = v1_ok and n_false_pos == 0
results["V1 Pi & P_perp invariant; no stray invariant among 200 random"] = v1_ok

# ----------------------------------------------------------------------
# V2 -- no third invariant plane in the mixed family at generic theta
# ----------------------------------------------------------------------
theta_g = 1.234567
min_dev = min(deviation(rot_about_e1(theta_g), mixed_plane(a * math.pi / 24,
                                                           b * math.pi / 24))
              for a in range(24) for b in range(24))
results["V2 mixed family ALL fail at generic theta (exactly-two)"] = \
    min_dev > TOL_FAIL

# ----------------------------------------------------------------------
# V3 -- continua at k = 1 and k = 3
# ----------------------------------------------------------------------
k1_max = 0.0
k3_max = 0.0
for a in range(36):
    alpha = a * math.pi / 36
    L = projector([line_in_pi(alpha)])
    k1_max = max(k1_max, max(deviation(rot_about_e1(t), L) for t in thetas))
    # orthocomplement of the line: 3-space
    I4 = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
    L3 = mat_sub(I4, L)
    k3_max = max(k3_max, max(deviation(rot_about_e1(t), L3) for t in thetas))
results["V3 k=1 and k=3 carry invariant CONTINUA (no uniqueness there)"] = \
    k1_max < TOL_ZERO and k3_max < TOL_ZERO

# ----------------------------------------------------------------------
# V4 -- v -> 0: full SO(3); no invariant 2-plane survives
# ----------------------------------------------------------------------
rots = [random_spatial_rotation() for _ in range(15)]
fail_pi = max(deviation(R, P_PI) for R in rots) > TOL_FAIL
fail_pp = max(deviation(R, P_PERP) for R in rots) > TOL_FAIL
fail_mixed = max(deviation(R, mixed_plane(0.7, 1.1)) for R in rots) > TOL_FAIL
fail_tau_u = max(deviation(R, projector([E0, [0, 0.6, 0.8, 0]]))
                 for R in rots) > TOL_FAIL
tau_line_ok = max(deviation(R, projector([E0])) for R in rots) < TOL_ZERO
spatial3_ok = max(deviation(R, projector([E1, E2, E3]))
                  for R in rots) < TOL_ZERO
none_random = True
for _ in range(200):
    P = random_plane()
    if max(deviation(R, P) for R in rots) < 1e-8:
        none_random = False
results["V4 v=0: NO invariant 2-plane (tau-line & spatial 3-space only)"] = \
    (fail_pi and fail_pp and fail_mixed and fail_tau_u and tau_line_ok
     and spatial3_ok and none_random)

# ----------------------------------------------------------------------
# V5 -- BROKEN BRANCH: discrete C2 stabilizer => continuum; uniqueness dies
# ----------------------------------------------------------------------
R_pi = rot_about_e1(math.pi)
c2_max = max(deviation(R_pi, mixed_plane(a * math.pi / 24, b * math.pi / 24))
             for a in range(24) for b in range(24))
results["V5 BROKEN BRANCH: C2 stabilizer -> mixed continuum ALL invariant"] = \
    c2_max < TOL_ZERO

# ----------------------------------------------------------------------
# V6 -- Delta(v) lies in Pi exactly; zero P_perp projection
# ----------------------------------------------------------------------
v6_ok = True
for v_over_c in (0.001, 0.1, 0.5, 0.9, 0.999):
    delta = [1.0, v_over_c, 0.0, 0.0]      # (c t_P, v t_P, 0, 0) / (l_P)
    p_pi = [sum(P_PI[i][j] * delta[j] for j in range(4)) for i in range(4)]
    p_pp = [sum(P_PERP[i][j] * delta[j] for j in range(4)) for i in range(4)]
    in_pi = math.sqrt(sum((a - b) ** 2 for a, b in zip(p_pi, delta)))
    in_pp = math.sqrt(sum(a * a for a in p_pp))
    if in_pi > TOL_ZERO or in_pp > TOL_ZERO:
        v6_ok = False
results["V6 Delta(v) in Pi exactly; P_perp-projection identically zero"] = \
    v6_ok

# ----------------------------------------------------------------------
print("Patch 2491 -- M1 canonical plane uniqueness -- verify")
print("=" * 68)
all_ok = True
for name, ok in results.items():
    print(("PASS  " if ok else "FAIL  ") + name)
    all_ok = all_ok and ok
print("=" * 68)
print("ALL PASS" if all_ok else "FAILURES PRESENT")
raise SystemExit(0 if all_ok else 1)
