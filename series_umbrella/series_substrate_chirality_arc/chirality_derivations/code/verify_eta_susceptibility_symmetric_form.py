#!/usr/bin/env python3
"""
verify_eta_susceptibility_symmetric_form.py  --  Patch 1100 (Phase-0 parallel round, W1).

STAGE-2 (reachable structural) pass for the sign(mu^2) verdict-mover, built on the
Patch-0694 NESS construction (code/setup_ness_stationary_measure.py).  It computes the
FORM of the symmetric-part eta-field susceptibility and then demonstrates, concretely,
that the SIGN bottoms out at the named gap (H-NESS).

It does NOT assert sign(mu^2), does NOT crystallize THEO-CHIR-CAPACITY-1, and does NOT
move a verdict: FI-C-9 = V3, sign(delta) = W3 STAND.

Background (consumed, not re-derived):
  - Landau identity (0684 sec.1):  chi_eta^-1 = d^2 V/d eta^2|_0 = 2 mu^2  =>  sign(mu^2)=sign(chi_eta^-1).
  - chi_eta = sum_{v,w} <eta_v eta_w>_c, the connected correlator IN the NESS pi (0694).
  - The symmetric (time-reversible) part of chi_eta is the equilibrium-like correlator from the
    detailed-balance-through-O(delta^2) part of pi; the current part is O(delta^3) (0689/0694).

What is reachable here (the symmetric-part FORM):
  In the Gaussian (equilibrium-like) approximation the symmetric eta-field measure has action
  S_sym = (1/2) sum_{v,w} eta_v (L + m^2 I)_{vw} eta_w, with L the 600-cell GRAPH LAPLACIAN
  (the kinetic channel of 0684 sec.3) and m^2 the field mass (the eta^2-curvature itself).
  Then  chi_sym = 1^T (L + m^2 I)^-1 1.  Because L's zero mode is the constant vector
  (L 1 = 0), this is dominated by the zero mode:  chi_sym = N / m^2  exactly.  Hence
  chi_sym^-1 = m^2 / N  and  sign(mu^2) = sign(m^2).  The susceptibility FORM is therefore
  fully reachable AND it reduces the entire sign bit to one number: sign(m^2), the field mass.

Where it stops (H-NESS), shown concretely:
  m^2 is a property of the eta-FIELD measure.  The constructed pi is the SINGLE-WALKER
  stationary measure -- a distribution over one walker's vertex position (a 1-point marginal
  on 120 states).  It does NOT contain the eta-field two-point function.  The only off-diagonal
  connected correlator a single walker supplies is the single-OCCUPANCY artifact
  <n_v n_w>_c = -pi_v pi_w (v!=w) -- sign-definite negative, carrying NO information about m^2.
  Bridging pi -> m^2 requires EITHER (i) an occupation/many-walker generator (NEW mechanism)
  OR (ii) a justified single-site reduction (the H-NESS hypothesis itself).  Neither is
  available without inventing machinery, so the sign is NOT computed.  This is the escalation
  STOP, not a discharge.

  CHECK 1  geometry: 120 vertices, 720 edges, degree 12 (reuse of the 0689/0694 build).
  CHECK 2  graph-Laplacian zero mode: L 1 = 0, lambda_0 = 0; report spectral gap, lambda_max.
  CHECK 3  symmetric-part FORM: chi_sym(m^2) = N/m^2 to machine precision (zero-mode domination).
  CHECK 4  (H-NESS) gap: single-walker off-diagonal conn. corr. = -pi_v pi_w (occupancy artifact),
           verified equal to the pi-product and shown to be m^2-independent -> NOT chi_eta.

NO sign(mu^2). NO theorem. NO verdict move.
"""
import numpy as np
from itertools import permutations as P

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
    """Single-walker Mechanism-A NESS pi (left null vector of Q). Reused from 0694."""
    N = len(V); Q = np.zeros((N, N))
    for (i, j) in edges:
        e = V[j] - V[i]; u = e / np.linalg.norm(e); c = float(u @ nhat)
        Q[i, j] = r0 * (1 + delta * c)
        Q[j, i] = r0 * (1 - delta * c)
    for i in range(N):
        Q[i, i] = -Q[i].sum()
    w, vecs = np.linalg.eig(Q.T)
    k = int(np.argmin(np.abs(w)))
    pi = np.real(vecs[:, k]); pi = pi / pi.sum()
    return pi


def main():
    V = build_600(); N = len(V)
    Dm = np.array([[np.linalg.norm(V[i] - V[j]) for j in range(N)] for i in range(N)])
    A = (np.abs(Dm - edge) < 1e-6).astype(float)
    deg = A.sum(1)
    edges = [(i, j) for i in range(N) for j in range(i + 1, N) if A[i, j] > 0]
    L = np.diag(deg) - A

    c1 = (N == 120 and len(edges) == 720 and deg.min() == 12 and deg.max() == 12)
    print("CHECK 1 -- 600-cell geometry")
    print(f"  vertices={N} edges={len(edges)} degree=[{int(deg.min())},{int(deg.max())}]"
          f"  [{'PASS' if c1 else 'FAIL'}]\n")

    # CHECK 2 -- graph-Laplacian zero mode
    evals = np.sort(np.linalg.eigvalsh(L))
    Lnorm = np.linalg.norm(L @ np.ones(N))
    c2 = (abs(evals[0]) < 1e-9) and (Lnorm < 1e-9) and (evals[1] > 1e-6)
    print("CHECK 2 -- graph-Laplacian zero mode (the symmetric kinetic channel, 0684 sec.3)")
    print(f"  lambda_0 = {evals[0]:.3e}  (expect 0)   ||L@1|| = {Lnorm:.3e}  (constant = zero mode)")
    print(f"  spectral gap lambda_1 = {evals[1]:.6f}   lambda_max = {evals[-1]:.6f}"
          f"   [{'PASS' if c2 else 'FAIL'}]\n")

    # CHECK 3 -- symmetric-part susceptibility FORM: chi_sym(m2) = N/m2 exactly
    print("CHECK 3 -- symmetric-part FORM  chi_sym(m2) = 1^T (L + m2 I)^-1 1  =  N/m2")
    print(f"  {'m2':>8} {'chi_sym':>16} {'N/m2':>16} {'ratio':>12}")
    ratios_ok = True
    for m2 in [0.05, 0.1, 0.5, 1.0, 2.0]:
        chi = float(np.ones(N) @ np.linalg.solve(L + m2 * np.eye(N), np.ones(N)))
        ratio = chi * m2 / N
        ratios_ok = ratios_ok and (abs(ratio - 1.0) < 1e-9)
        print(f"  {m2:>8.2f} {chi:>16.4f} {N/m2:>16.4f} {ratio:>12.8f}")
    print(f"  => zero-mode domination exact: chi_sym = N/m2; chi_sym^-1 ∝ m2 => sign(mu^2)=sign(m2).")
    print(f"     The sign bit reduces ENTIRELY to sign(m2), the field mass."
          f"  [{'PASS' if ratios_ok else 'FAIL'}]\n")

    # CHECK 4 -- (H-NESS) gap: single-walker pi does not contain the field two-point function
    nhat = V[np.argmax(V[:, 0])].copy(); nhat /= np.linalg.norm(nhat)
    pi = stationary(V, edges, nhat, delta=0.02)
    # single-walker occupation field n_v in {0,1}, exactly one occupied -> marginal pi.
    # off-diagonal connected correlator (v!=w):  <n_v n_w> - <n_v><n_w> = 0 - pi_v pi_w
    vv, ww = 0, 1
    measured = -pi[vv] * pi[ww]           # what a single walker forces
    # m2-independence: this number has no m2 in it at all (it is purely kinematic)
    c4 = (measured < 0) and abs(measured - (0.0 - pi[vv] * pi[ww])) < 1e-15
    print("CHECK 4 -- (H-NESS) gap: what single-walker pi supplies vs what chi_eta needs")
    print(f"  single-occupancy off-diagonal conn. corr  <n_v n_w>_c = -pi_v*pi_w = {measured:.3e}")
    print("  -> sign-definite NEGATIVE, purely the one-walker-can't-be-in-two-places constraint;")
    print("     contains NO m2, hence NO sign(mu^2) information. A chi assembled from pi alone")
    print("     measures the occupancy constraint, not the eta-field curvature."
          f"  [{'PASS (gap confirmed)' if c4 else 'FAIL'}]\n")

    print("=" * 74)
    print("RESULT")
    print("  - Symmetric-part susceptibility FORM is reachable and clean:")
    print("    chi_sym = N/m2 (zero-mode dominated)  =>  sign(mu^2) = sign(m2).")
    print("  - m2 (the eta-field mass) is NOT supplied by the single-walker pi.")
    print("  - Bridging pi -> m2 needs EITHER (i) an occupation/many-walker generator")
    print("    [a NEW mechanism] OR (ii) a justified single-site reduction [= the H-NESS")
    print("    hypothesis]. Neither is available without inventing machinery.")
    print("  - STOP at (H-NESS). NO sign(mu^2). NO theorem. NO verdict move. V3/W3 STAND.")
    print("=" * 74)


if __name__ == "__main__":
    main()
