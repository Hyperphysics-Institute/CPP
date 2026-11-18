#!/usr/bin/env python3
"""Patch 4488 verify script: can a record carried by each CP give a pair's Bell correlations?

The founder's Group Entity accounting (4485) and Copilot's bond records (4485, 4486) both ask
what each CP or GP must carry. This script tests one premise only: whether a record that
travels WITH each member, read locally at measurement, can reach the measured CHSH value.

Four cases, each printed as one row of the classification table:
  L1  every deterministic local record (each CP carries an answer for each setting): 16 strategies
  L2  a shared random tag drawn at the source plus local records (convex mixtures of L1): bound by L1's max
      (value column: |S|; for the no-signalling row: the marginal probability)
  J1  the joint singlet state, E(a,b) = -cos(a-b) (QM-3, THEO-QM-3/4): the measured value
  P1  the same membership with a product state |up>|down> (a group label with no joint amplitudes)
Also checked: J1's local marginals, on both sides, do not depend on the far setting (THEO-QM-5, no-signalling).
Prior art in the corpus: series_quantum_mechanics/code/3315_qm3_bell_verify.py (checks 5, 2, 4, 0) and QM-3's
retraction of the fixed-DI-bit-pool model (QM-3_bell_entanglement.tex). This script restates them for the per-CP case.

Pure Python; no dependencies. Exit 0 if every check holds.
"""
import itertools
import math

A_SET = (0.0, math.pi / 2)            # Alice: 0, 90 degrees
B_SET = (math.pi / 4, 3 * math.pi / 4)  # Bob: 45, 135 degrees


def chsh(E):
    a0, a1 = A_SET
    b0, b1 = B_SET
    return E(a0, b0) - E(a0, b1) + E(a1, b0) + E(a1, b1)


checks = []

# L1: deterministic local records. Each side carries a pair of answers (one per setting).
best_local = 0.0
n_strat = 0
for ra in itertools.product((-1, 1), repeat=2):
    for rb in itertools.product((-1, 1), repeat=2):
        n_strat += 1
        s = (ra[0] * rb[0] - ra[0] * rb[1] + ra[1] * rb[0] + ra[1] * rb[1])
        best_local = max(best_local, abs(s))
checks.append(("L1 local record, deterministic", f"{n_strat} strategies", best_local, best_local <= 2))

# L2: shared tag + local records = convex mixture of L1, so |S| <= max over L1 (the vertices).
# The bound is analytic (convexity); the sample uses sparse (near-vertex) mixtures so it approaches the bound.
import random
random.seed(4488)
strategies = []
for ra in itertools.product((-1, 1), repeat=2):
    for rb in itertools.product((-1, 1), repeat=2):
        strategies.append(ra[0] * rb[0] - ra[0] * rb[1] + ra[1] * rb[0] + ra[1] * rb[1])
vertex_max = max(abs(x) for x in strategies)
best_mix = 0.0
for _ in range(20000):
    w = [random.random() ** 12 for _ in strategies]   # sparse weights: mass near a few vertices
    t = sum(w)
    best_mix = max(best_mix, abs(sum(wi * si for wi, si in zip(w, strategies)) / t))
checks.append(("L2 shared tag + local records", "convexity; vertices", vertex_max,
               vertex_max <= 2 and best_mix <= vertex_max + 1e-12))
print(f"(L2 sampled sparse mixtures: max |S| = {best_mix:.6f}, never above the vertex bound {vertex_max:.1f})")

# J1: joint singlet state.
E_singlet = lambda a, b: -math.cos(a - b)
S_j = chsh(E_singlet)
checks.append(("J1 joint state (singlet)", "E=-cos(a-b)", abs(S_j), abs(abs(S_j) - 2 * math.sqrt(2)) < 1e-12))

# P1: same two members, product state |up_z>|down_z>, spin measured in the x-z plane.
# For a spin-1/2 state along +z, <sigma_theta> = cos(theta); along -z, -cos(theta). Product => E = -cos(a)cos(b).
E_prod = lambda a, b: -math.cos(a) * math.cos(b)
best_prod = 0.0
grid = [k * math.pi / 90 for k in range(-90, 91)]
for a0 in grid[::6]:
    for a1 in grid[::6]:
        for b0 in grid[::6]:
            for b1 in grid[::6]:
                s = E_prod(a0, b0) - E_prod(a0, b1) + E_prod(a1, b0) + E_prod(a1, b1)
                best_prod = max(best_prod, abs(s))
checks.append(("P1 membership label, product state", "grid max", best_prod, best_prod <= 2 + 1e-12))

# No-signalling for J1: P(A=+1 | a, b) = 1/2 for every b.
def p_joint(x, y, a, b):
    # singlet: P(x,y) = (1 - x*y*cos(a-b)) / 4
    return (1 - x * y * math.cos(a - b)) / 4

ns_ok = True
for a in A_SET:
    margs = [p_joint(1, 1, a, b) + p_joint(1, -1, a, b) for b in B_SET]
    ns_ok &= all(abs(m - 0.5) < 1e-12 for m in margs)
for b in B_SET:
    margs = [p_joint(1, 1, a, b) + p_joint(-1, 1, a, b) for a in A_SET]
    ns_ok &= all(abs(m - 0.5) < 1e-12 for m in margs)
checks.append(("J1 no-signalling, both marginals", "P(+1) each side, any far setting", 0.5, ns_ok))

print("CLASSIFICATION TABLE (Patch 4488)")
print(f"{'case':38s} {'scope':32s} {'value':>10s}  verdict")
for name, scope, val, ok in checks:
    verdict = "PASS" if ok else "FAIL"
    if name.startswith(("L", "P")):
        verdict += "  (<= 2: cannot reach the measured 2.83)"
    elif "singlet" in name:
        verdict += "  (= 2*sqrt(2): reaches it)"
    print(f"{name:38s} {scope:32s} {val:10.6f}  {verdict}")
n_pass = sum(ok for *_, ok in checks)
print(f"{n_pass}/{len(checks)} PASS")
raise SystemExit(0 if n_pass == len(checks) else 1)
