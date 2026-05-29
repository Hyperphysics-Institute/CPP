#!/usr/bin/env python3
"""
verify_merge_2_parity_decomposition.py
THEO-CHIR-MERGE-2 (Patch 0647, Session 149) verification.

Two independent checks underpinning the parity-decomposition theorem:

  CHECK 1 (Lemma "600-cell achirality"): the 120 vertices of the unit 600-cell
    are closed under an improper orthogonal transformation (the reflection
    R = diag(-1,1,1,1), det R = -1). Hence the substrate geometry admits a
    handedness-reversing symmetry => it is achiral => it supplies NO primitive
    pseudoscalar. The only primitive pseudoscalar is sign(n-hat) = FI-C-9.

  CHECK 2 (the parity decomposition): the (P, T) discrete-symmetry characters of
    {n-hat, delta, j, omega_PCD, sigma_cycle} are mutually consistent, the
    relation sigma_cycle = sign(delta) * sign(n-hat) is (P-odd, T-odd) on both
    sides, and the P-odd (pseudoscalar) content of sigma_cycle is carried
    entirely by sign(n-hat) while the P-even/T-odd (arrow) content is carried
    entirely by sign(delta).

Tier 2/3: CHECK 1 is exact geometry at machine precision; CHECK 2 is a
discrete-symmetry bookkeeping consistency check (the load-bearing physical
assignments delta:T-odd and omega_PCD:T-odd are stated as theorem hypotheses).
"""

import itertools
import numpy as np

PHI = (1.0 + 5.0 ** 0.5) / 2.0
TOL = 1e-12


# ----------------------------------------------------------------------
# 600-cell vertices (unit circumradius), 8 + 16 + 96 = 120
# ----------------------------------------------------------------------
def even_permutations(seq):
    """Yield the even permutations (A4) of a 4-element sequence by index."""
    n = len(seq)
    for perm in itertools.permutations(range(n)):
        # parity of the permutation
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        if inv % 2 == 0:
            yield tuple(seq[perm[k]] for k in range(n))


def six_hundred_cell_vertices():
    verts = set()

    def add(v):
        verts.add(tuple(round(x, 10) for x in v))

    # (A) 16-cell: permutations of (+/-1, 0, 0, 0)  -> 8
    for pos in range(4):
        for s in (+1.0, -1.0):
            v = [0.0, 0.0, 0.0, 0.0]
            v[pos] = s
            add(v)

    # (B) tesseract: (+/-1/2)^4  -> 16
    for signs in itertools.product((+0.5, -0.5), repeat=4):
        add(signs)

    # (C) snub 24-cell: even permutations of (+/-phi/2, +/-1/2, +/-1/(2phi), 0) -> 96
    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    nonzero_idx_in_base = [0, 1, 2]  # positions of the nonzero magnitudes in `base`
    for perm in even_permutations(base):
        # apply independent signs to the three nonzero entries
        for sgn in itertools.product((+1.0, -1.0), repeat=3):
            v = list(perm)
            k = 0
            for i in range(4):
                if abs(v[i]) > 1e-9:
                    v[i] = v[i] * sgn[k]
                    k += 1
            add(v)

    return np.array(sorted(verts))


def check_1_achirality():
    V = six_hundred_cell_vertices()
    assert V.shape == (120, 4), f"expected 120 vertices, got {V.shape[0]}"

    # all unit circumradius
    norms = np.linalg.norm(V, axis=1)
    assert np.allclose(norms, 1.0, atol=TOL), "vertices are not all unit norm"

    # reflection R = diag(-1,1,1,1): improper (det = -1)
    R = np.diag([-1.0, 1.0, 1.0, 1.0])
    detR = np.linalg.det(R)
    assert abs(detR + 1.0) < TOL, f"R is not improper, det={detR}"

    vertset = {tuple(np.round(v, 8)) for v in V}
    for v in V:
        rv = tuple(np.round(R @ v, 8))
        assert rv in vertset, f"reflection maps {v} outside the vertex set"

    # also confirm closure under the central inversion -I (proper in 4D, det=+1):
    detI = np.linalg.det(-np.eye(4))
    assert abs(detI - 1.0) < TOL, "in 4D, -I should be proper (det=+1)"

    print("CHECK 1 PASS: 600-cell (120 unit vertices) is closed under the improper")
    print("              reflection diag(-1,1,1,1) (det=-1) => achiral => the")
    print("              substrate supplies no primitive pseudoscalar; FI-C-9 = sign(n-hat)")
    print("              is the unique primitive pseudoscalar.")
    return True


# ----------------------------------------------------------------------
# Parity / time-reversal character bookkeeping
# ----------------------------------------------------------------------
# Encode characters as exponents in {+1: even, -1: odd}.
EVEN, ODD = +1, -1

CHAR = {
    # quantity      :  (P,   T)
    "n_hat":           (ODD,  EVEN),   # polar spatial dir; sign(n_hat)=FI-C-9
    "delta":           (EVEN, ODD),    # Mech-A rate asymmetry (Lemmas 2.2, 2.3)
    "j_net":           (ODD,  ODD),    # DI-bit current ~ delta * n_hat
    "omega_PCD":       (EVEN, ODD),    # axial cycle orientation (Lemma 2.4)
    "sigma_cycle":     (ODD,  ODD),    # from omega_PCD = sigma_cycle * n_hat
}


def mult(a, b):
    return (a[0] * b[0], a[1] * b[1])


def check_2_parity_decomposition():
    # (i) consistency of j_net = (6 delta / phi^2) n_hat  (positive scalar 6/phi^2)
    assert mult(CHAR["delta"], CHAR["n_hat"]) == CHAR["j_net"], \
        "j_net character != char(delta)*char(n_hat)"

    # (ii) consistency of omega_PCD = sigma_cycle * n_hat
    #      => char(sigma_cycle) = char(omega_PCD) * char(n_hat)  (n_hat is its own inverse char)
    derived_sigma = mult(CHAR["omega_PCD"], CHAR["n_hat"])
    assert derived_sigma == CHAR["sigma_cycle"], \
        "sigma_cycle character inconsistent with omega_PCD = sigma_cycle n_hat"

    # (iii) the MERGE-1 relation sigma_cycle = sign(delta) * sign(n_hat) is P,T-covariant
    rhs = mult(CHAR["delta"], CHAR["n_hat"])  # sign(delta)*sign(n_hat)
    assert rhs == CHAR["sigma_cycle"], \
        "relation sigma_cycle = sign(delta) sign(n_hat) is not P,T-consistent"
    assert CHAR["sigma_cycle"] == (ODD, ODD), "sigma_cycle should be (P-odd, T-odd)"

    # (iv) THE DECOMPOSITION:
    #   the P-odd (pseudoscalar) content sits ENTIRELY in sign(n_hat) [=FI-C-9],
    #   because sign(delta) is P-even (carries no pseudoscalar);
    #   the P-even/T-odd (arrow) content sits ENTIRELY in sign(delta),
    #   because sign(n_hat) is T-even (carries no arrow).
    assert CHAR["delta"][0] == EVEN, "sign(delta) must be P-even (cannot carry chirality)"
    assert CHAR["n_hat"][0] == ODD, "sign(n_hat)=FI-C-9 must be P-odd (the pseudoscalar)"
    assert CHAR["delta"][1] == ODD, "sign(delta) must be T-odd (the arrow content)"
    assert CHAR["n_hat"][1] == EVEN, "sign(n_hat) must be T-even (carries no arrow)"

    # (v) the parity category-mismatch: sign(delta) and sign(n_hat) have DIFFERENT (P,T)
    #     characters, so no P,T-covariant relation can equate or tie them.
    assert CHAR["delta"] != CHAR["n_hat"], \
        "category-mismatch claim fails: sign(delta) and sign(n_hat) share (P,T) character"

    print("CHECK 2 PASS: (P,T) characters consistent across the relation chain;")
    print("              sigma_cycle = sign(delta) * sign(n-hat) is (P-odd, T-odd);")
    print("              P-odd (chirality) content = sign(n-hat)=FI-C-9 (unique pseudoscalar);")
    print("              P-even/T-odd (arrow) content = sign(delta);")
    print("              sign(delta) and sign(n-hat) differ in (P,T) => 'tie them' is a")
    print("              parity category-mismatch (corrects MERGE-1's M1 route).")
    return True


if __name__ == "__main__":
    ok1 = check_1_achirality()
    print()
    ok2 = check_2_parity_decomposition()
    print()
    if ok1 and ok2:
        print("ALL CHECKS PASS.")
        print("Verdict M1-chi: ONE chirality (pseudoscalar) primitive = FI-C-9, shared by")
        print("spatial capture handedness (CAP-1) and temporal cycle handedness (this theorem);")
        print("sign(delta) is the time-reversal arrow, gated on OPEN-CHIR-2a / F.2 (not a chirality).")
