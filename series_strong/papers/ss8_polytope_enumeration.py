#!/usr/bin/env python3
# =========================================================================
# SS-8 Phase 1b: Polytope Interstitial-Site Enumeration
#
# For each alpha-chain polytope (convex deltahedron at N_alpha), count the
# available interstitial sites by coordination number k, and test whether
# the naive "binding = k * B_pair per neutron" model reproduces the
# observed Delta / N_ex values from the extended empirical map.
#
# Scope: Phase 1b only. We count TOPOLOGICALLY (vertex/edge/face inventory).
# Coordinate-level detailed neighbor analysis and Pauli decrements are
# deferred to v0.1 full draft.
#
# Author: Claude Opus, 21 April 2026
# =========================================================================

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ame2020_loader import load_ame2020  # noqa: E402

B_alpha = 28.296
B_pair  = 2.342  # M_0 / phi (SS-5, via A11)
def ss7_pred(Na): return Na * B_alpha + (3 * Na - 6) * B_pair

AME = load_ame2020()

# -------- The 8 convex deltahedra (Freudenthal 1947) ---------------------
# (V, E, F) determined by convex deltahedron identity and Euler's formula:
#   simplicial: 3F = 2E,  V - E + F = 2  =>  E = 3V - 6,  F = 2V - 4
# Interior-centroid sites: empirically, octahedron and icosahedron
# have a single high-symmetry interior point equidistant from all vertices.
# Tetrahedron has an interior centroid but it sits INSIDE the space of
# the alpha K3 faces (non-distinguished).
#
# Entries: (name, V, E, F, interior_centroid_k, has_interior_bulk_site)
DELTAHEDRA = [
    # N_a=3 is NOT a convex deltahedron (it's the degenerate triangle),
    # but SS-7 treats it as a planar 3-alpha configuration with 2 "faces"
    # (front/back of the triangle). Include for continuity.
    (3,  "triangle (planar)",                 3,  3,  2,   None, False),
    (4,  "tetrahedron",                       4,  6,  4,   4,    False),
    (5,  "triangular bipyramid",              5,  9,  6,   None, False),
    (6,  "octahedron",                        6, 12,  8,   6,    True),
    (7,  "pentagonal bipyramid",              7, 15, 10,   None, False),
    (8,  "snub disphenoid",                   8, 18, 12,   None, False),
    (9,  "triaugmented triangular prism",     9, 21, 14,   None, False),
    (10, "gyroelongated square bipyramid",   10, 24, 16,   None, False),
    # N_a = 11: no convex deltahedron exists (Freudenthal 1947). The
    # simplicial graph still satisfies 3N-6=27 edges, but not realized
    # as a strictly deltahedral convex polyhedron. SS-7 empirically
    # fits 44Ti at -0.2%, so the graph-level simplicial count suffices.
    (11, "(no convex deltahedron)",          11, 27, 18,   None, False),
    (12, "icosahedron",                      12, 30, 20,   12,   True),
    (13, "(interior / mass hypothesis)",     13, 33, 22,   None, False),
    (14, "(interior / mass hypothesis)",     14, 36, 24,   None, False),
]

ELEM = {6: "C", 8: "O", 10: "Ne", 12: "Mg", 14: "Si", 16: "S",
        18: "Ar", 20: "Ca", 22: "Ti", 24: "Cr", 26: "Fe", 28: "Ni"}

def Bx(Z, A):
    e = AME.get((Z, A))
    return (e["BE_total"], e["estimated"]) if e else (None, None)

# -------- Observed Delta/N_ex at N_ex=2 for comparison --------------------
observed_per_n_nex2 = {}  # Na -> (Delta/N_ex, AME estimated?)
for Na in range(3, 15):
    Z = 2 * Na
    Bexp, est = Bx(Z, 4*Na + 2)
    if Bexp is None:
        continue
    delta = Bexp - ss7_pred(Na)
    observed_per_n_nex2[Na] = (delta / 2.0, est)

# -------- Section A: Topological enumeration -----------------------------
print("=" * 100)
print("SECTION A: Convex deltahedra for the SS-8 alpha-chain polytopes")
print("  V = alpha vertices; E = 3V-6 alpha-alpha K3 edges; F = 2V-4 K3 faces")
print("=" * 100)
print(f"{'N_a':>4} {'Polytope':<38} {'V':>3} {'E':>4} {'F':>4} "
      f"{'face-sites(k=3)':>16} {'edge-sites(k=2)':>16} {'interior k':>10}")
print("-" * 100)
for Na, name, V, E, F, interior_k, has_bulk in DELTAHEDRA:
    ik = str(interior_k) if interior_k is not None else "-"
    print(f"{Na:>4} {name:<38} {V:>3} {E:>4} {F:>4} "
          f"{F:>16} {E:>16} {ik:>10}")
print()

# -------- Section B: Naive face-center k=3 model --------------------------
print("=" * 100)
print("SECTION B: Naive face-center k=3 model")
print("  Hypothesis: each extra neutron occupies a k=3 face-center interstitial site.")
print("  Predicted Delta/N_ex = 3 * B_pair = {:.3f} MeV.".format(3 * B_pair))
print("  Compare to observed Delta/N_ex at N_ex=2 (from extended map).")
print("=" * 100)
pred_k3 = 3 * B_pair
print(f"{'N_a':>4} {'polytope':<38} {'sites(F)':>9} "
      f"{'predicted':>10} {'observed':>10} {'ratio obs/pred':>16}")
print("-" * 100)
for Na, name, V, E, F, _, _ in DELTAHEDRA:
    if Na not in observed_per_n_nex2:
        continue
    obs, est = observed_per_n_nex2[Na]
    mark = "*" if est else " "
    ratio = obs / pred_k3
    print(f"{Na:>4} {name:<38} {F:>9} "
          f"{pred_k3:>10.3f} {obs:>+9.3f}{mark} {ratio:>16.3f}")
print()

# -------- Section C: Effective k_eff required to match observation --------
print("=" * 100)
print("SECTION C: Effective coordination number k_eff = Delta(N_ex=2) / (2 * B_pair)")
print("  What coordination number would the naive 'binding = k * B_pair' model need?")
print("=" * 100)
print(f"{'N_a':>4} {'polytope':<38} {'Delta(N_ex=2)':>14} {'k_eff':>8} "
      f"{'k_eff/V':>10} {'k_eff/F':>10}")
print("-" * 100)
k_eff_table = {}
for Na, name, V, E, F, _, _ in DELTAHEDRA:
    if Na not in observed_per_n_nex2:
        continue
    obs, est = observed_per_n_nex2[Na]  # = Delta/N_ex = Delta/2 already
    Delta_Nex2 = 2 * obs
    k_eff = Delta_Nex2 / B_pair / 2.0  # = observed per-neutron / B_pair
    k_eff_table[Na] = k_eff
    print(f"{Na:>4} {name:<38} {Delta_Nex2:>+13.3f}  {k_eff:>7.2f} "
          f"{k_eff/V:>10.3f} {k_eff/F:>10.3f}")
print()

# -------- Section D: Interior site hypothesis for N_a = 6, 12 -------------
print("=" * 100)
print("SECTION D: Interior-centroid site test")
print("  Octahedron (N_a=6) and icosahedron (N_a=12) have unique interior centroids")
print("  equidistant from ALL V vertices (k = V = 6 or 12).")
print("  Hypothesis H2-strong: first 2 neutrons (spin-paired) occupy the centroid,")
print("  binding at k = V per neutron.")
print("=" * 100)
for Na, name, V, E, F, interior_k, has_bulk in DELTAHEDRA:
    if not has_bulk:
        continue
    if Na not in observed_per_n_nex2:
        continue
    obs, _ = observed_per_n_nex2[Na]
    pred_strong = V * B_pair
    print(f"  N_a = {Na} ({name}):")
    print(f"    Interior centroid prediction:  k = V = {V}  ->  "
          f"{V} * B_pair = {pred_strong:.3f} MeV per neutron")
    print(f"    Observed Delta/N_ex at N_ex=2: {obs:+.3f} MeV per neutron")
    print(f"    Ratio observed/prediction: {obs/pred_strong:.3f}")
print()

# -------- Section E: k_eff trend vs N_a analysis --------------------------
print("=" * 100)
print("SECTION E: k_eff trend analysis")
print("=" * 100)
measured = [(Na, k) for Na, k in k_eff_table.items() if Na in observed_per_n_nex2]
if measured:
    vals = [k for _, k in measured]
    print(f"  N samples: {len(measured)}  "
          f"mean k_eff: {sum(vals)/len(vals):.2f}  "
          f"range: [{min(vals):.2f}, {max(vals):.2f}]")
    print(f"  k_eff at light side (N_a = 3..5):  "
          f"{[round(k_eff_table[n], 2) for n in [3,4,5] if n in k_eff_table]}")
    print(f"  k_eff in bulk (N_a = 8..14):       "
          f"{[round(k_eff_table[n], 2) for n in range(8,15) if n in k_eff_table]}")

print()
print("=" * 100)
print("KEY FINDINGS")
print("=" * 100)
print("""
1. Naive face-center k=3 model predicts Delta/N_ex = 7.03 MeV per neutron.
   Observed: ~11-13 MeV at N_a >= 8; ~6-7 MeV at N_a = 3,4. Ratio obs/pred
   ranges 0.89 (N_a=4) to 1.89 (N_a=14). Naive model UNDERPREDICTS the bulk
   and roughly matches the light side.

2. Effective k_eff required: ~2.7 (light side) to ~5.6 (heavy side). Scales
   with polytope size but does NOT simply equal V or F.

3. Interior-centroid-only hypothesis (k = V for 1st pair of neutrons)
   OVERPREDICTS: octahedron (N_a=6) pred 14.05, obs 9.40 (0.67x);
   icosahedron (N_a=12) pred 28.10, obs 12.62 (0.45x). Strongly ruled out
   as the dominant site for light neutrons.

4. N_a = 11 gap: no convex deltahedron exists. SS-7 empirical fit at
   44Ti (-0.20% residual) depends on the graph being simplicial (27 edges),
   NOT on the polytope being deltahedral. This is a subtle consistency
   point for SS-8 at N_a = 11, N_ex > 0 (should use graph-simplicial
   counting, not deltahedral face counting).

5. k_eff scales RATIONALLY with E/V (edges per vertex) in the heavy regime:
   at N_a = 10, E/V = 2.4; k_eff = 4.87. At N_a = 12, E/V = 2.5; k_eff = 5.39.
   Scaling suggests k_eff ~ (local edge-density) * const. Not simply f(F).
""")
