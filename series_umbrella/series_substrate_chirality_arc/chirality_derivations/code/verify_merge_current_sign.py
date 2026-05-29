#!/usr/bin/env python3
"""
verify_merge_current_sign.py  --  Verification for THEO-CHIR-MERGE-1 (OPEN-CHIR-MERGE).

Tier 2/3 verification of the load-bearing sign fact behind the MERGE-beta verdict (M3: the
temporal arrow's sign is NOT pinned to sign(n_hat) at current rigor):

  (C1) the host-to-first-shell unit projection u_i . n_hat = -1/(2*phi) is UNIFORM across all 12
       first-shell neighbours (DSL Identity I1 / Theorem host-first-shell-projection);
  (C2) the net first-shell DI-bit current (Mechanism A, first order) is
         j_net = sum_i 2*delta*(u_i . n_hat) u_i = (6*delta/phi^2) n_hat,
       i.e. it is PARALLEL to n_hat with magnitude 6|delta|/phi^2 and DIRECTION sign(delta)*n_hat;
  (C3) therefore the thermodynamic-arrow direction carries the factor sign(delta) IN ADDITION to
       n_hat. Since delta is an independent Mechanism-A framework input (its tie to the spatial
       chirality parameter eps/chi = phi^-3 is unpinned at Layer 3; OPEN-FP-F1-2 / Layer 4), the
       arrow sign sign(delta)*sign(n_hat) does NOT reduce to sign(n_hat) alone -> the merge sign
       is undetermined (M3), not M1.

This is the numerical anchor for the structural verdict; it does not (and cannot) decide the
sign question, which is gated on the Layer-4 Mechanism-A derivation. It confirms only that the
arrow direction is sign(delta)*n_hat (the fact the M3 reasoning rests on).

Run: python3 verify_merge_current_sign.py   (requires numpy)
"""
import numpy as np
from itertools import permutations, product
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
        for sgn in (1,-1):
            v=[0,0,0,0]; v[pos]=sgn; V.add(tuple(v))
    for s in product([0.5,-0.5],repeat=4):
        V.add(tuple(s))
    vals=(phi/2,0.5,1/(2*phi),0.0)
    for ep in set(even_perms(vals)):
        nz=[i for i in range(4) if abs(ep[i])>1e-12]
        for sc in product([1,-1],repeat=len(nz)):
            w=list(ep)
            for k,i in enumerate(nz): w[i]=ep[i]*sc[k]
            V.add(tuple(round(x,12) for x in w))
    return [np.array(v) for v in V]

def net_current(first_shell, host, n_hat, delta):
    """j_net = sum_i [r(+u_i) - r(-u_i)] u_i with r(e)=r0(1+delta e.n_hat); r0 cancels."""
    j = np.zeros(4)
    for v in first_shell:
        u = v - host; u = u/np.linalg.norm(u)
        j += 2*delta*float(u @ n_hat) * u
    return j

def main():
    V = build_600cell()
    assert len(V)==120
    host = np.array([1.0,0,0,0]); n_hat = host.copy()

    d = [(round(float(np.linalg.norm(host-v)),9), v) for v in V if np.linalg.norm(host-v)>1e-9]
    first_shell = [v for dist,v in d if isclose(dist, 1/phi, abs_tol=1e-9)]
    assert len(first_shell)==12, "first shell != 12"

    # (C1) uniform host-to-first-shell projection = -1/(2 phi)
    projs = [float(((v-host)/np.linalg.norm(v-host)) @ n_hat) for v in first_shell]
    target = -1/(2*phi)
    assert all(isclose(p, target, abs_tol=1e-9) for p in projs), "I1 not uniform"

    # (C2) net current = (6 delta / phi^2) n_hat for delta = +1 and -1
    for delta in (+1.0, -1.0, +0.37, -0.37):
        j = net_current(first_shell, host, n_hat, delta)
        expected = (6*delta/phi**2) * n_hat
        assert np.allclose(j, expected, atol=1e-9), f"current mismatch at delta={delta}"
        # direction parallel to sign(delta)*n_hat
        if abs(delta) > 1e-9:
            jhat = j/np.linalg.norm(j)
            assert np.allclose(jhat, np.sign(delta)*n_hat, atol=1e-9), "direction != sign(delta) n_hat"

    jp = net_current(first_shell, host, n_hat, +1.0)
    jm = net_current(first_shell, host, n_hat, -1.0)

    print("ALL CHECKS PASS")
    print(f"  (C1) u_i . n_hat = -1/(2 phi) = {target:.6f} uniform across all 12 first-shell nbrs")
    print(f"  (C2) j_net(delta=+1) = (6/phi^2) n_hat,  6/phi^2 = {6/phi**2:.6f}  (dir = +n_hat)")
    print(f"       j_net(delta=-1) = -(6/phi^2) n_hat                       (dir = -n_hat)")
    print(f"       => j_net direction = sign(delta) * n_hat  (verified at delta=+-1, +-0.37)")
    print(f"  (C3) the arrow sign carries sign(delta) IN ADDITION to sign(n_hat); delta is an")
    print(f"       independent Layer-3 framework input (tie to eps/chi unpinned, OPEN-FP-F1-2).")
    print(f"       => arrow sign = sign(delta)*sign(n_hat) does NOT reduce to sign(n_hat): MERGE-beta = M3.")

if __name__ == "__main__":
    main()
