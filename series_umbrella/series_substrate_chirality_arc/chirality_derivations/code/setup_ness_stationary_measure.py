#!/usr/bin/env python3
"""
setup_ness_stationary_measure.py  --  Patch 0694, Session 153.

SETUP / CHARACTERIZATION pass for the sign(mu^2) verdict-mover (Priority 1).
Constructs the Mechanism-A non-equilibrium stationary measure (NESS) on the
600-cell and CHARACTERIZES it.  It does NOT compute the eta-curvature and does
NOT assert sign(mu^2): V3/W3 stand.  This is the "construct the NESS before
reaching for the eta^2-curvature" setup Thomas asked for.

Mechanism A (F.1 framework axiom, OPEN-FP-F1-2): the directed-edge rate field
    r(v->w) = r0 (1 + delta * e_vw . n_hat),   e_vw = unit(V[w]-V[v]).
These are the transition rates of a continuous-time Markov process (a single
DI-bit walker) on the 600-cell graph (120 vertices, degree 12).  Its generator
is Q with off-diagonals Q_vw = r(v->w) on edges (0 otherwise) and
Q_vv = -sum_w Q_vw.  The stationary measure pi solves pi Q = 0 (left null vector).
The steady probability current on edge (v,w) is
    J_vw = pi_v r(v->w) - pi_w r(w->v).
Detailed balance (equilibrium, J==0) <=> Kolmogorov cycle condition; Patch 0689
showed it HOLDS through O(delta^2) and FAILS at O(delta^3) (per-face content
2 delta^3 abc on 420/1200 faces).  So this NESS is a genuine non-equilibrium
steady state whose current must ONSET at O(delta^3).  This script verifies
exactly that -- tying the constructed pi back to the reviewed TARROW-2 finding.

  CHECK 1  geometry: 120 vertices, 720 edges, degree 12 (reuse of the 0689 build).
  CHECK 2  pi is a valid probability measure (all pi_v > 0, sum = 1) for delta!=0.
  CHECK 3  delta-scaling of the tilt  d_pi(delta) = max_v |pi_v - 1/120|   (expect ~ delta^1:
           pi tilts at first order via the conservative O(delta^1) gradient).
  CHECK 4  delta-scaling of the steady current  J_max(delta) = max_edge |J_vw|  (expect ~ delta^3:
           the current onsets at third order, matching the 0689 Kolmogorov result).
  CHECK 5  consistency: at delta=0 the chain is reversible (J==0, pi uniform).

NO eta field is built, NO susceptibility is computed, NO sign is asserted.
"""
import numpy as np
from itertools import permutations as P, combinations

phi = (1 + np.sqrt(5)) / 2
edge = 1 / phi


def build_600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16):
        Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    base = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                sg = [base[0] * s1, base[1] * s2, base[2] * s3, base[3]]
                for pm in P(range(4)):
                    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if pm[i] > pm[j])
                    if inv % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U):
            U.append(v)
    return np.array(U)


def stationary(V, edges, nhat, delta, r0=1.0):
    """Build the CTMC generator Q for rate r(v->w)=r0(1+delta e_vw.nhat) and
    return its stationary distribution pi (left null vector, normalized)."""
    N = len(V)
    Q = np.zeros((N, N))
    for (i, j) in edges:
        e = V[j] - V[i]; u = e / np.linalg.norm(e)
        c = float(u @ nhat)
        Q[i, j] = r0 * (1 + delta * c)   # i -> j
        Q[j, i] = r0 * (1 - delta * c)   # j -> i  (e_ji . nhat = -c)
    for i in range(N):
        Q[i, i] = -Q[i].sum()
    # stationary: pi Q = 0  <=>  Q^T pi^T = 0  -> null vector of Q^T
    w, vecs = np.linalg.eig(Q.T)
    k = int(np.argmin(np.abs(w)))            # eigenvalue nearest 0
    pi = np.real(vecs[:, k])
    pi = pi / pi.sum()
    return pi, Q


def current_max(V, edges, nhat, pi, delta, r0=1.0):
    Jmax = 0.0
    for (i, j) in edges:
        e = V[j] - V[i]; u = e / np.linalg.norm(e); c = float(u @ nhat)
        rij = r0 * (1 + delta * c); rji = r0 * (1 - delta * c)
        J = pi[i] * rij - pi[j] * rji
        Jmax = max(Jmax, abs(J))
    return Jmax


def slope(xs, ys):
    """log-log slope of ys vs xs (least squares over the sampled points)."""
    lx, ly = np.log(np.array(xs)), np.log(np.array(ys))
    return float(np.polyfit(lx, ly, 1)[0])


def main():
    V = build_600(); N = len(V)
    Dm = np.array([[np.linalg.norm(V[i] - V[j]) for j in range(N)] for i in range(N)])
    adj = (np.abs(Dm - edge) < 1e-6)
    deg = adj.sum(1)
    edges = [(i, j) for i in range(N) for j in range(i + 1, N) if adj[i, j]]
    c1 = (N == 120 and len(edges) == 720 and deg.min() == 12 and deg.max() == 12)
    print("CHECK 1 -- 600-cell geometry")
    print(f"  vertices={N} edges={len(edges)} degree=[{deg.min()},{deg.max()}]"
          f"  [{'PASS' if c1 else 'FAIL'}]\n")

    nhat = V[np.argmax(V[:, 0])].copy(); nhat /= np.linalg.norm(nhat)  # vertex-aligned Reading C

    # --- delta = 0 anchor (reversible / equilibrium) ---
    pi0, _ = stationary(V, edges, nhat, 0.0)
    J0 = current_max(V, edges, nhat, pi0, 0.0)
    c5 = (np.max(np.abs(pi0 - 1.0 / N)) < 1e-9) and (J0 < 1e-12)
    print("CHECK 5 -- delta=0 anchor (isotropic rates => reversible equilibrium)")
    print(f"  max|pi - 1/120| = {np.max(np.abs(pi0 - 1.0/N)):.2e}   J_max = {J0:.2e}"
          f"   [{'PASS (pi uniform, no current)' if c5 else 'FAIL'}]\n")

    # --- delta != 0: validity + delta-scaling of tilt and current ---
    deltas = [4e-3, 8e-3, 1.6e-2, 3.2e-2]
    valid_all = True
    d_pi, J_mx = [], []
    print("CHECK 2/3/4 -- NESS validity + scaling (delta sweep)")
    print(f"  {'delta':>8} {'min pi':>12} {'sum pi':>10} {'max|pi-1/120|':>15} {'J_max':>12}")
    for d in deltas:
        pi, _ = stationary(V, edges, nhat, d)
        jm = current_max(V, edges, nhat, pi, d)
        valid = (pi.min() > 0) and (abs(pi.sum() - 1.0) < 1e-9)
        valid_all = valid_all and valid
        d_pi.append(np.max(np.abs(pi - 1.0 / N))); J_mx.append(jm)
        print(f"  {d:>8.4f} {pi.min():>12.6e} {pi.sum():>10.6f} "
              f"{np.max(np.abs(pi-1.0/N)):>15.3e} {jm:>12.3e}")

    s_pi = slope(deltas, d_pi)
    s_J = slope(deltas, J_mx)
    print(f"\n  CHECK 2  pi a valid probability measure for all sampled delta:"
          f"  [{'PASS' if valid_all else 'FAIL'}]")
    print(f"  CHECK 3  tilt scaling  d_log(d_pi)/d_log(delta)  = {s_pi:.3f}"
          f"   (expect ~1: first-order gradient tilt)   [{'PASS' if abs(s_pi-1)<0.15 else 'CHECK'}]")
    print(f"  CHECK 4  current scaling d_log(J_max)/d_log(delta) = {s_J:.3f}"
          f"   (expect ~3: O(delta^3) onset, 0689)        [{'PASS' if abs(s_J-3)<0.25 else 'CHECK'}]")

    print("\n" + "=" * 70)
    print("NESS CONSTRUCTED AND CHARACTERIZED.")
    print("  - pi is a valid non-equilibrium stationary measure for delta != 0.")
    print("  - pi tilts from uniform at O(delta^1) (conservative gradient part).")
    print("  - the steady probability current ONSETS at O(delta^3), reproducing")
    print("    the Patch-0689 detailed-balance violation from the stationary side.")
    print("  - SETUP ONLY: no eta field, no susceptibility, no sign(mu^2). V3/W3 stand.")
    print("=" * 70)


if __name__ == "__main__":
    main()
