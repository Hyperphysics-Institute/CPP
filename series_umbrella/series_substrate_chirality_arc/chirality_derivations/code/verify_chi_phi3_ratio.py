#!/usr/bin/env python3
"""
verify_chi_phi3_ratio.py  --  Verification for THEO-CHIR-CHI-1 (OPEN-CHIR-1d / E21).

Tier 2/3 verification (per PD-002): constructs the 600-cell at unit circumradius,
computes the distance spectrum (shells) from a host vertex, enumerates the
symmetric-bias ratios (d_j - d_i)/(d_j + d_i) of all distinct distance pairs, and
checks the THEO-CHIR-CHI-1 selection claims:

  (C1) the two nearest shells are at d = 1/phi (12 vertices, icosahedral vertex
       figure) and d = 1 (20 vertices, dodecahedral next shell);
  (C2) their symmetric bias equals phi^-3 exactly: (1-1/phi)/(1+1/phi) = phi^-2/phi
       = phi^-3 ~ 0.236068;
  (C3) (1/phi, 1) is the UNIQUE adjacent (consecutive-shell) pair that is also the
       two-shortest-distance pair, and is the maximal-bias adjacent pair;
  (C4) the literature alternatives 1/sqrt5 and 5-2sqrt5 are produced ONLY by
       NON-adjacent edge-to-distant-shell pairs (edge<->phi-shell; edge<->antipode),
       hence excluded by the locality criterion.

Run: python3 verify_chi_phi3_ratio.py    (requires numpy)
"""
import numpy as np
from itertools import permutations, product
from collections import Counter
from math import isclose

phi = (1 + 5**0.5) / 2

def even_perms(t):
    out = []
    for p in permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j])
        if inv % 2 == 0:
            out.append(tuple(t[p[k]] for k in range(4)))
    return out

def build_600cell():
    V = set()
    for pos in range(4):
        for sgn in (1, -1):
            v = [0,0,0,0]; v[pos] = sgn; V.add(tuple(v))           # 8: perms of (+-1,0,0,0)
    for s in product([0.5,-0.5], repeat=4):
        V.add(tuple(s))                                            # 16: (+-1/2)^4
    vals = (phi/2, 0.5, 1/(2*phi), 0.0)
    for ep in set(even_perms(vals)):                              # 96: even perms, signs on nonzero
        nz = [i for i in range(4) if abs(ep[i]) > 1e-12]
        for sc in product([1,-1], repeat=len(nz)):
            w = list(ep)
            for k,i in enumerate(nz): w[i] = ep[i]*sc[k]
            V.add(tuple(round(x,12) for x in w))
    return [np.array(v) for v in V]

def main():
    V = build_600cell()
    assert len(V) == 120, f"expected 120 vertices, got {len(V)}"
    assert all(abs(np.linalg.norm(v)-1) < 1e-9 for v in V), "vertices not unit-circumradius"

    host = np.array([1.0,0,0,0])
    mult = Counter(round(float(np.linalg.norm(host-v)),9) for v in V if np.linalg.norm(host-v) > 1e-9)
    shells = sorted(mult)                                          # distinct distances, ascending
    assert len(shells) == 8, f"expected 8 distinct distances, got {len(shells)}"

    # (C1) two nearest shells
    d1, d2 = shells[0], shells[1]
    assert isclose(d1, 1/phi, abs_tol=1e-9) and mult[d1] == 12, "nearest shell != 1/phi x12 (icosahedron)"
    assert isclose(d2, 1.0,   abs_tol=1e-9) and mult[d2] == 20, "second shell != 1 x20 (dodecahedron)"

    # (C2) symmetric bias of the two nearest = phi^-3
    bias12 = (d2 - d1)/(d2 + d1)
    assert isclose(bias12, phi**-3, abs_tol=1e-12), f"bias(1/phi,1)={bias12} != phi^-3"

    # all pairwise biases
    pairs = []
    for i in range(len(shells)):
        for j in range(i+1, len(shells)):
            pairs.append((shells[i], shells[j], (shells[j]-shells[i])/(shells[j]+shells[i]), j==i+1))

    # (C3) (1/phi,1) is the unique adjacent pair giving phi^-3, and the max adjacent bias
    adj = [(a,b,c) for (a,b,c,is_adj) in pairs if is_adj]
    adj_phi3 = [(a,b) for (a,b,c) in adj if isclose(c, phi**-3, abs_tol=1e-9)]
    assert adj_phi3 == [(d1, d2)], f"phi^-3 not the unique adjacent pair: {adj_phi3}"
    assert max(adj, key=lambda t: t[2])[:2] == (d1, d2), "two-nearest pair is not the maximal-bias adjacent pair"

    # (C4) alternatives produced only by non-adjacent edge-to-distant pairs
    def producers(val):
        return [(a,b,'adj' if is_adj else 'non-adj') for (a,b,c,is_adj) in pairs if isclose(c, val, abs_tol=1e-6)]
    inv_sqrt5 = producers(1/5**0.5)
    fivem2sqrt5 = producers(5 - 2*5**0.5)
    assert all(tag == 'non-adj' for *_,tag in inv_sqrt5), "1/sqrt5 has an adjacent producer"
    assert all(tag == 'non-adj' for *_,tag in fivem2sqrt5), "5-2sqrt5 has an adjacent producer"
    # both pair the EDGE with a distant shell
    assert all(isclose(a, d1, abs_tol=1e-9) for a,b,_ in inv_sqrt5), "1/sqrt5 not an edge-pairing"
    assert all(isclose(a, d1, abs_tol=1e-9) for a,b,_ in fivem2sqrt5), "5-2sqrt5 not an edge-pairing"

    print("ALL CHECKS PASS")
    print(f"  shells (R=1): {[round(s,6) for s in shells]}")
    print(f"  multiplicities: {[mult[s] for s in shells]}  (sum={sum(mult.values())})")
    print(f"  two nearest: d1=1/phi x{mult[d1]} (icosahedron), d2=1 x{mult[d2]} (dodecahedron)")
    print(f"  symmetric bias (d1,d2) = (1-1/phi)/(1+1/phi) = phi^-2/phi = phi^-3 = {bias12:.9f}")
    print(f"  phi^-3 adjacent producers: {adj_phi3}  (unique)")
    print(f"  1/sqrt5 producers: {inv_sqrt5}  (edge<->phi-shell, non-adjacent)")
    print(f"  5-2sqrt5 producers: {fivem2sqrt5}  (edge<->antipode, non-adjacent)")

if __name__ == "__main__":
    main()
