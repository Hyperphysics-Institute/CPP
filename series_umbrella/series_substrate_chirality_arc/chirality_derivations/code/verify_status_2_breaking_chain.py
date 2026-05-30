#!/usr/bin/env python3
"""
verify_status_2_breaking_chain.py
THEO-CHIR-STATUS-2 (Patch 0654, Session 149) verification.

1d-β-i (breaking chain) + partial 1d-β-iii (no axiom-level pseudoscalar fixes the sign).

CHECK 1 (breaking chain H_4 -> H_4^+):
  - the 600-cell (120 unit vertices) is closed under the improper reflection
    R = diag(-1,1,1,1), det R = -1  => its isometry group H_4 contains improper
    elements (achiral; re-confirms MERGE-2);
  - the orientation (det) map g |-> det(g) in {+1,-1} is a homomorphism whose kernel
    is the rotation subgroup H_4^+ (index 2); demonstrated on {I, R, R^2, a product
    of two reflections} -- the Z_2 grading that is the enantiomorph order parameter;
  - the two degenerate chiral vacua are the two det-cosets (related by any reflection).
  (Group orders |H_4| = 14400, |H_4^+| = 7200 are cited standard facts.)

CHECK 2 (no P-even quantity fixes the enantiomorph => V2 excluded at axiom level):
  - a 4-vertex ordered frame has a SIGNED 4-volume D = det[v1;v2;v3;v4] (a pseudoscalar);
    under R it flips sign, D -> det(R) D = -D  (P-odd)  => it tracks the enantiomorph;
  - P-even data -- the Gram matrix G_ij = v_i . v_j, hence det G, and the full
    pairwise-distance multiset -- are R-invariant (R orthogonal): they CANNOT
    distinguish the two enantiomorphs;
  - therefore fixing sign(n-hat) requires a P-odd (pseudoscalar) quantity; by MERGE-2
    the unique primitive pseudoscalar is FI-C-9 itself (circular), so no axiom-level
    pseudoscalar fixes the sign => value-axis != 'derived' at axiom level => V2 excluded;
    the chiral-vacuum (capacity=Yes) outcome is pinned to V1 (Theorem STATUS-1).
"""

import itertools
import numpy as np

PHI = (1.0 + 5.0 ** 0.5) / 2.0
TOL = 1e-9


def _parity(perm):
    """Parity of a permutation given as a tuple of indices: +1 even, -1 odd."""
    perm = list(perm)
    seen = [False] * len(perm)
    sign = 1
    for i in range(len(perm)):
        if seen[i]:
            continue
        j, length = i, 0
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            length += 1
        if length % 2 == 0:
            sign = -sign
    return sign


def even_permutations(base):
    """Yield the rearrangements of `base` under even index-permutations (12 of them)."""
    n = len(base)
    for perm in itertools.permutations(range(n)):
        if _parity(perm) == 1:
            yield tuple(base[perm[i]] for i in range(n))


def six_hundred_cell_vertices():
    verts = set()

    def add(v):
        verts.add(tuple(round(x, 10) for x in v))

    # (A) 16-cell: permutations of (+/-1,0,0,0) -> 8
    for pos in range(4):
        for s in (+1.0, -1.0):
            v = [0.0, 0.0, 0.0, 0.0]
            v[pos] = s
            add(v)
    # (B) tesseract: (+/-1/2)^4 -> 16
    for signs in itertools.product((+0.5, -0.5), repeat=4):
        add(signs)
    # (C) snub 24-cell: even perms of (+/-phi/2,+/-1/2,+/-1/(2phi),0) -> 96
    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    for perm in even_permutations(base):
        for sgn in itertools.product((+1.0, -1.0), repeat=3):
            v = list(perm)
            k = 0
            for i in range(4):
                if abs(v[i]) > 1e-9:
                    v[i] = v[i] * sgn[k]
                    k += 1
            add(v)
    return np.array(sorted(verts))


R = np.diag([-1.0, 1.0, 1.0, 1.0])  # the enantiomorph-flipping reflection


def check_1_breaking_chain():
    V = six_hundred_cell_vertices()
    assert V.shape == (120, 4), f"expected 120 vertices, got {V.shape}"
    assert np.allclose(np.linalg.norm(V, axis=1), 1.0, atol=TOL), "non-unit vertices"

    # R is improper; 600-cell closed under R (achiral) => H_4 has improper elements
    assert abs(np.linalg.det(R) + 1.0) < TOL, "R should be improper (det -1)"
    vset = {tuple(np.round(v, 8)) for v in V}
    for v in V:
        assert tuple(np.round(R @ v, 8)) in vset, "R maps a vertex off the polytope"

    # the det map is a Z_2 homomorphism; kernel = rotation subgroup H_4^+ (index 2).
    # demonstrate on a few isometries of the polytope:
    I4 = np.eye(4)
    R2 = R @ R                       # = I (proper)
    R_b = np.diag([1.0, -1.0, 1.0, 1.0])  # another reflection (improper)
    rot = R @ R_b                    # product of two reflections -> proper rotation
    # all of these map the polytope to itself:
    for M in (I4, R, R_b, rot):
        for v in V:
            assert tuple(np.round(M @ v, 8)) in vset, "isometry maps off polytope"
    # det grading:
    assert abs(np.linalg.det(I4) - 1.0) < TOL          # identity: proper
    assert abs(np.linalg.det(R) + 1.0) < TOL           # reflection: improper
    assert abs(np.linalg.det(R2) - 1.0) < TOL          # R^2: proper
    assert abs(np.linalg.det(rot) - 1.0) < TOL         # two reflections: proper
    # multiplicativity (homomorphism): det(R*R_b) = det(R)*det(R_b)
    assert abs(np.linalg.det(R @ R_b) - np.linalg.det(R) * np.linalg.det(R_b)) < TOL

    print("CHECK 1 PASS: 600-cell closed under improper R (det -1) => H_4 achiral;")
    print("              det: H_4 -> {+1,-1} is a homomorphism, kernel = rotation")
    print("              subgroup H_4^+ (index 2; |H_4|=14400, |H_4^+|=7200). The chiral")
    print("              vacuum breaks H_4 -> H_4^+; order parameter = the det-pseudoscalar")
    print("              (the enantiomorph FI-C-9); the two vacua are the two det-cosets.")
    return True


def check_2_pseudoscalar_excludes_v2():
    V = six_hundred_cell_vertices()
    # pick 4 vertices forming a non-degenerate frame
    idx = [0, 1, 2, 3]
    frame = V[idx]
    while abs(np.linalg.det(frame)) < 1e-6:
        idx[-1] += 1
        frame = V[idx]

    D = np.linalg.det(frame)                 # signed 4-volume: a pseudoscalar
    frame_mirror = (R @ frame.T).T           # apply the enantiomorph flip
    D_mirror = np.linalg.det(frame_mirror)

    # P-odd: signed volume flips sign (D_mirror = det(R) * D = -D)
    assert abs(D_mirror + D) < 1e-6, "signed volume should flip under R (P-odd)"

    # P-even invariants are unchanged under R (R orthogonal):
    G = frame @ frame.T                      # Gram matrix (inner products)
    G_mirror = frame_mirror @ frame_mirror.T
    assert np.allclose(G, G_mirror, atol=TOL), "Gram (P-even) must be R-invariant"
    assert abs(abs(D_mirror) - abs(D)) < 1e-6, "|signed volume| (P-even) must be R-invariant"

    # full pairwise-distance multiset (P-even) is identical for V and R.V
    def dist_multiset(P):
        d = []
        for i in range(len(P)):
            for j in range(i + 1, len(P)):
                d.append(round(float(np.linalg.norm(P[i] - P[j])), 6))
        return sorted(d)
    VR = (R @ V.T).T
    assert dist_multiset(V) == dist_multiset(VR), "distance multiset (P-even) must match"

    print("CHECK 2 PASS: the signed 4-volume (a pseudoscalar) flips under R (P-odd) and")
    print("              tracks the enantiomorph; every P-even invariant (Gram, |volume|,")
    print("              distance multiset) is R-invariant. => fixing sign(n-hat) requires")
    print("              a P-odd pseudoscalar; the unique primitive pseudoscalar is FI-C-9")
    print("              itself (MERGE-2), so NO axiom-level pseudoscalar fixes the sign")
    print("              => value-axis != 'derived' at axiom level => V2 excluded; the")
    print("              capacity=Yes outcome is pinned to V1.")
    return True


if __name__ == "__main__":
    ok1 = check_1_breaking_chain()
    print()
    ok2 = check_2_pseudoscalar_excludes_v2()
    print()
    if ok1 and ok2:
        print("ALL CHECKS PASS.")
        print("THEO-CHIR-STATUS-2: the FI-C-9 emergence, if/when it occurs (capacity=Yes via")
        print("1d-beta-ii), is the SSB H_4 -> H_4^+ with a Z_2 pseudoscalar order parameter,")
        print("and is pinned to verdict V1 (emergent mechanism, contingent sign) -- NOT V2 --")
        print("at the axiom level, reopenable to V2 only by a cross-sector pseudoscalar (1d-beta-v).")
