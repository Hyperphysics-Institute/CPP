#!/usr/bin/env python3
"""
600cell_spectrum.py
Project C / Route B (Patch 1003).

Constructs the 600-cell (120 unit-quaternion vertices = binary icosahedral
group 2I), builds its nearest-neighbour graph (12-regular, edge = 1/phi), and
computes the exact adjacency / graph-Laplacian spectrum. This is the "mode
structure" Route B must draw on. Pure geometry; no physics input, no fitting.

Result (exact, golden-ratio closed forms):

  Adjacency eigenvalues:
     12, 6 + 6/phi, 4 phi, 3, 0, -2, -4/phi, -3, -6/phi
  Laplacian L = 12 I - A eigenvalues:
     0, 6 - 6/phi (= 6 phi^-2), 12 - 4 phi, 9, 12, 14, 12 + 4/phi, 15, 12 + 6/phi
  Spectral gap  lambda_1 = 6 phi^-2 = 2.29180
  Largest       lambda_max = 12 + 6/phi = 15.70820
"""

import numpy as np
from itertools import permutations, product

PHI = (1 + 5 ** 0.5) / 2


def parity(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def even_perms(t):
    return {tuple(t[p[i]] for i in range(4))
            for p in permutations(range(4)) if parity(p) == 1}


def vertices_600cell():
    V = set()
    for i in range(4):                       # 8:  (+-1,0,0,0) and perms
        for s in (1.0, -1.0):
            v = [0.0, 0.0, 0.0, 0.0]; v[i] = s; V.add(tuple(v))
    for signs in product((0.5, -0.5), repeat=4):   # 16: (+-1/2)^4
        V.add(tuple(signs))
    a, b, c = PHI / 2, 0.5, 1 / (2 * PHI)    # 96: even perms of (+-phi/2,+-1/2,+-1/2phi,0)
    for sa in (a, -a):
        for sb in (b, -b):
            for sc in (c, -c):
                V |= even_perms((sa, sb, sc, 0.0))
    return np.array(sorted(V))


def spectrum():
    V = vertices_600cell()
    D = np.sqrt(((V[:, None, :] - V[None, :, :]) ** 2).sum(-1))
    edge = D[D > 1e-9].min()                 # smallest nonzero distance (unrounded)
    A = (np.abs(D - edge) < 1e-6).astype(float)
    eigA = np.linalg.eigvalsh(A)
    eigL = 12 - eigA
    return V, A, eigA, eigL, edge


if __name__ == "__main__":
    V, A, eigA, eigL, edge = spectrum()
    assert V.shape == (120, 4), "must be 120 vertices"
    assert np.allclose(np.linalg.norm(V, axis=1), 1.0), "all on unit S^3"
    assert (A.sum(1) == 12).all(), "12-regular"
    assert abs(edge - 1 / PHI) < 1e-6, "edge = 1/phi"
    print(f"vertices: {len(V)}   degree: 12   edge: {edge:.6f} = 1/phi")
    print("adjacency distinct eigenvalues:", np.unique(np.round(eigA, 5)))
    print("Laplacian distinct eigenvalues:", np.sort(np.unique(np.round(eigL, 5))))
    print(f"spectral gap = 6 phi^-2 = {6/PHI**2:.5f}")
    print(f"lambda_max   = 12 + 6/phi = {12+6/PHI:.5f}")
