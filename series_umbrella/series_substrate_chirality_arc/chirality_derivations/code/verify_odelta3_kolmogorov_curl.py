#!/usr/bin/env python3
"""
verify_odelta3_kolmogorov_curl.py  --  Patch 0689, Session 152.

The O(delta^3) Kolmogorov / detailed-balance computation for the Mechanism-A
substrate rate field (the first verdict-relevant computation of the deep engine,
1d-beta-ii / F.1 sec-14.17).

Mechanism A (F.1 framework axiom): r(e) = r0 (1 + delta * e.n_hat) on the 600-cell.
Detailed balance (reversibility) of the induced Markov process holds iff the
Kolmogorov cycle condition holds: for every cycle, prod(forward rates) =
prod(backward rates). The per-directed-edge log-ratio is

    L(a->b) = log[ r(a->b) / r(b->a) ] = log[(1+delta c)/(1-delta c)]
            = 2 ( delta c + delta^3 c^3/3 + delta^5 c^5/5 + ... ),   c = e_ab . n_hat

-- ODD in delta only (forward/backward antisymmetry). Detailed balance <=> the
sum of L around every face vanishes at every order.  KEY CORRECTION to the 0688
sketch's "O(delta^2) gate": there is NO O(delta^2) term; the first possible
violation is O(delta^3).

Per triangular face, the three oriented edge-projections satisfy a+b+c=0 (closed
loop + uniform 600-cell edge length), so the O(delta^1) sum vanishes for EVERY
face, and the O(delta^3) sum is (2/3)(a^3+b^3+c^3) = (2/3)(3abc) = 2abc -- the
triple product of edge-projections.

  CHECK 1  geometry: 120 vertices, 720 edges, 1200 triangular faces, degree 12.
  CHECK 2  O(delta^1): max|a+b+c| over all faces = 0 (DB holds at first order).
  CHECK 3  O(delta^3): compute abc per face. RESULT (reported, not assumed):
           is detailed balance preserved (all abc=0) or violated (some abc!=0)?
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


def main():
    V = build_600(); N = len(V)
    Dm = np.array([[np.linalg.norm(V[i] - V[j]) for j in range(N)] for i in range(N)])
    adj = (np.abs(Dm - edge) < 1e-6)
    deg = adj.sum(1)
    edges = [(i, j) for i in range(N) for j in range(i + 1, N) if adj[i, j]]
    faces = [(i, j, k) for i, j, k in combinations(range(N), 3)
             if adj[i, j] and adj[j, k] and adj[i, k]]
    c1 = (N == 120 and len(edges) == 720 and len(faces) == 1200
          and deg.min() == 12 and deg.max() == 12)
    print("CHECK 1 -- 600-cell geometry")
    print(f"  vertices={N} edges={len(edges)} faces={len(faces)} degree=[{deg.min()},{deg.max()}]"
          f"  [{'PASS' if c1 else 'FAIL'}]\n")

    nhat = V[np.argmax(V[:, 0])].copy(); nhat /= np.linalg.norm(nhat)   # vertex-aligned Reading C

    def proj(a, b):
        e = V[b] - V[a]; return float(e @ nhat) / np.linalg.norm(e)

    sum1, abc = [], []
    for (i, j, k) in faces:
        a, b, cc = proj(i, j), proj(j, k), proj(k, i)
        sum1.append(a + b + cc); abc.append(a * b * cc)
    sum1 = np.array(sum1); abc = np.array(abc)

    c2 = np.max(np.abs(sum1)) < 1e-12
    print("CHECK 2 -- O(delta^1) per-face curl (detailed balance at first order)")
    print(f"  max|a+b+c| over 1200 faces = {np.max(np.abs(sum1)):.2e}  (=0 => DB holds at O(d^1))"
          f"  [{'PASS' if c2 else 'FAIL'}]\n")

    nz = np.abs(abc) > 1e-9
    print("CHECK 3 -- O(delta^3) Kolmogorov content (per-face curl ~ 2 delta^3 abc)")
    print(f"  max|abc| = {np.max(np.abs(abc)):.4f}")
    print(f"  faces with abc != 0: {int(nz.sum())} of {len(faces)}")
    print(f"  distinct nonzero |abc| values: {sorted(set(np.round(np.abs(abc[nz]),6)))}")
    db_holds_o3 = (np.max(np.abs(abc)) < 1e-9)
    # classify nonzero faces by host-shell membership (n_hat vertex = host)
    host = int(np.argmax(V @ nhat))
    dh = np.array([np.linalg.norm(V[m] - V[host]) for m in range(N)])
    shell = np.where(np.arange(N) == host, 0, np.where(np.abs(dh - edge) < 1e-6, 1, 2))
    touches2 = sum(1 for idx, (i, j, k) in enumerate(faces)
                   if nz[idx] and 2 in (shell[i], shell[j], shell[k]))
    print(f"  of the {int(nz.sum())} nonzero faces, {touches2} touch the 2nd shell "
          f"(consistent with the first-shell cancellation)")
    print(f"\n  RESULT: detailed balance at O(delta^3) is "
          f"{'PRESERVED (all abc=0)' if db_holds_o3 else 'VIOLATED (probability current present)'}.")
    print(f"  => the Mechanism-A process is {'reversible' if db_holds_o3 else 'NON-reversible'} at third order;")
    print(f"     the curl-free / equilibrium (V3-by-principle) branch is "
          f"{'confirmed' if db_holds_o3 else 'RULED OUT'} at O(delta^3).")
    print(f"\n[CHECK 3 is a faithful computation, not a pass/fail gate -- it REPORTS the curl content.]")
    print("=" * 68)
    print("ALL STRUCTURAL CHECKS PASS" if (c1 and c2) else "STRUCTURAL CHECK FAILED")
    print("=" * 68)


if __name__ == "__main__":
    main()
