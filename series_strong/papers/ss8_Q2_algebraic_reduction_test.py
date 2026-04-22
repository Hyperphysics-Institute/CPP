#!/usr/bin/env python3
# ============================================================
# SS-8 Model B algebraic reduction test
# Purpose: Check ChatGPT's Q2 concern — does Model B reduce to
#          a monotonic function of vertex degree or adjacency
#          count in the SR limit?
#
# Method:  Evaluate Model B at multiple lambda values spanning
#          strict-SR (0.05 x edge) to long-range (1.5 x edge).
#          Extract leading-order coefficients.  Compare against
#          Model A's (deg(v), 2, 1, 0) counting rule and against
#          nearest-neighbor multiplicity at min-distance.
# ============================================================

import numpy as np
from itertools import combinations


def octahedron():
    V = np.array([
        [ 1,  0,  0], [-1,  0,  0],
        [ 0,  1,  0], [ 0, -1,  0],
        [ 0,  0,  1], [ 0,  0, -1],
    ], dtype=float)
    edges = []
    for i, j in combinations(range(6), 2):
        if i // 2 != j // 2:
            edges.append((i, j))
    faces = [(a, b, c) for a in (0, 1) for b in (2, 3) for c in (4, 5)]
    return V, edges, faces


def gesbp():
    r = 1 / np.sqrt(2)
    val = 1.0 - 0.25 - (r - 0.5) ** 2
    h_mid = 0.5 * np.sqrt(val)
    h_top = h_mid + 1 / np.sqrt(2)
    top_apex = np.array([0, 0,  h_top])
    bot_apex = np.array([0, 0, -h_top])
    top_sq = np.array([[r * np.cos(k * np.pi / 2),
                        r * np.sin(k * np.pi / 2),
                         h_mid] for k in range(4)])
    bot_sq = np.array([[r * np.cos(k * np.pi / 2 + np.pi / 4),
                        r * np.sin(k * np.pi / 2 + np.pi / 4),
                        -h_mid] for k in range(4)])
    V = np.vstack([top_apex[None, :], top_sq, bot_sq, bot_apex[None, :]])
    edges = []
    for i, j in combinations(range(10), 2):
        if abs(np.linalg.norm(V[i] - V[j]) - 1.0) < 1e-6:
            edges.append((i, j))
    E = set(tuple(sorted(e)) for e in edges)
    faces = []
    for i, j, k in combinations(range(10), 3):
        if (all(tuple(sorted(p)) in E for p in [(i, j), (j, k), (i, k)])):
            faces.append((i, j, k))
    return V, edges, faces


def modelB_energy(site, V, lam, V0=1.0):
    dists = np.linalg.norm(V - site, axis=1)
    return -V0 * np.sum(np.exp(-dists / lam))


def leading_coefficient(site, V, lam, V0=1.0):
    """Return (multiplicity at min distance, min distance)."""
    dists = np.linalg.norm(V - site, axis=1)
    d_min = np.min(dists)
    n_min = np.sum(np.abs(dists - d_min) < 1e-6)
    return n_min, d_min


def analyze_polytope(name, V, edges, faces, edge_length):
    print(f"\n{'=' * 72}")
    print(f"POLYTOPE: {name}")
    print(f"  V = {len(V)}, E = {len(edges)}, F = {len(faces)}")
    print(f"  edge length = {edge_length:.4f}")
    print(f"{'=' * 72}")

    # vertex degrees
    vdeg = [0] * len(V)
    for i, j in edges:
        vdeg[i] += 1
        vdeg[j] += 1
    print(f"  vertex degrees: {sorted(set(vdeg))}")

    # canonical sites (one representative per class)
    sites = {}

    # pick a vertex of each distinct degree
    for d in sorted(set(vdeg)):
        for i, deg_i in enumerate(vdeg):
            if deg_i == d:
                sites[f'vertex(deg={d})'] = V[i]
                break

    # an edge midpoint
    i, j = edges[0]
    sites['edge_mid'] = (V[i] + V[j]) / 2

    # a face center
    i, j, k = faces[0]
    sites['face_center'] = (V[i] + V[j] + V[k]) / 3

    # centroid
    sites['centroid'] = np.mean(V, axis=0)

    # Part 1: leading coefficient (n_min, d_min) at each site
    print(f"\nPart 1 — Leading-order structure (Model B in SR limit):")
    print(f"  At each site, E_B ~ -V_0 * n_min * exp(-d_min/lambda) + subleading")
    print(f"  where n_min = multiplicity at min-distance to alpha-vertex,")
    print(f"        d_min = min-distance to alpha-vertex.")
    print()
    print(f"{'site':<20} {'n_min':>8} {'d_min':>8} "
          f"{'(compare Model A count)':>25}")
    print("-" * 72)

    model_A_counts = {}
    for site_name, pos in sites.items():
        n_min, d_min = leading_coefficient(pos, V, lam=1.0)
        # Model A count
        if 'vertex' in site_name:
            deg = int(site_name.split('=')[1].rstrip(')'))
            ma = f"deg(v)={deg}"
        elif site_name == 'edge_mid':
            ma = "2 (faces on edge)"
        elif site_name == 'face_center':
            ma = "1 (the face)"
        elif site_name == 'centroid':
            ma = "0"
        else:
            ma = "?"
        model_A_counts[site_name] = ma
        print(f"{site_name:<20} {n_min:>8d} {d_min:>8.4f} {ma:>25}")

    # Part 2: evaluate E at multiple lambda values (strict SR to long range)
    print(f"\nPart 2 — Numerical E_B / V_0 at multiple lambda values")
    print(f"  (lambda expressed as fraction of edge length)")
    print()
    lam_fracs = [0.05, 0.10, 0.20, 0.35, 0.50, 0.70, 1.00, 1.50]
    headers = ["site"] + [f"lam={f:.2f}" for f in lam_fracs]
    print("  " + " | ".join(f"{h:>14}" for h in headers))
    print("  " + "-" * (17 * len(headers)))

    results = {}
    for site_name, pos in sites.items():
        row = [site_name]
        results[site_name] = {}
        for f in lam_fracs:
            lam = f * edge_length
            E = modelB_energy(pos, V, lam)
            row.append(f"{E:.6f}")
            results[site_name][f] = E
        print("  " + " | ".join(f"{v:>14}" for v in row))

    # Part 3: extract deg(v)-dependence at vertex sites
    vertex_sites = [s for s in sites if 'vertex' in s]
    if len(vertex_sites) >= 2:
        print(f"\nPart 3 — Testing ChatGPT's Q2: does E_vertex scale with deg(v)?")
        print(f"  If Model B reduces to a function of deg(v), then")
        print(f"  E_vertex(deg=d1) / E_vertex(deg=d2) should equal d1/d2")
        print(f"  (or monotonically track d1/d2).")
        print()
        print(f"  Actual ratios across lambda values:")
        print()
        v1, v2 = vertex_sites[0], vertex_sites[1]
        d1 = int(v1.split('=')[1].rstrip(')'))
        d2 = int(v2.split('=')[1].rstrip(')'))
        print(f"  (v1 = {v1}, v2 = {v2})")
        print(f"  deg ratio d1/d2 = {d1 / d2:.4f}")
        print()
        print(f"  {'lambda':>8} {'E(v1)':>12} {'E(v2)':>12} "
              f"{'E(v1)/E(v2)':>14} {'matches d1/d2?':>18}")
        for f in lam_fracs:
            e1, e2 = results[v1][f], results[v2][f]
            ratio = e1 / e2
            match = "~yes" if abs(ratio - d1/d2) < 0.05 else (
                "~no" if abs(ratio - 1.0) < 0.05 else "partial")
            print(f"  {f:>8.2f} {e1:>12.6f} {e2:>12.6f} "
                  f"{ratio:>14.4f} {match:>18}")

    return results


def main():
    print("=" * 72)
    print("SS-8 Q2 TEST — Does Model B reduce to Model A?")
    print("=" * 72)
    print()
    print("Test logic: If Model B's ranking at the 4 site classes reduces")
    print("to a monotonic function of vertex degree (or adjacency count),")
    print("then Model B is 'Model A in disguise' (ChatGPT's Q2 concern).")
    print()
    print("Check 1: leading-order structure at each site (Part 1 table).")
    print("         Does (n_min, d_min) match Model A's counting rule?")
    print("Check 2: numerical evaluation at multiple lambda (Part 2).")
    print("         Does ranking at non-vertex sites match Model A's ordering?")
    print("Check 3: deg(v) scaling of E_vertex across polytopes (Part 3).")
    print("         Does E_vertex scale linearly with deg(v) as Model A says?")
    print()

    # run for both test polytopes
    V1, E1, F1 = octahedron()
    edge1 = np.linalg.norm(V1[E1[0][0]] - V1[E1[0][1]])
    res1 = analyze_polytope("Octahedron (N_alpha = 6)",
                             V1, E1, F1, edge1)

    V2, E2, F2 = gesbp()
    edge2 = 1.0
    res2 = analyze_polytope("Gyroelongated square bipyramid (N_alpha = 10)",
                             V2, E2, F2, edge2)

    # cross-polytope deg(v) test
    print("\n" + "=" * 72)
    print("CROSS-POLYTOPE TEST: does E_vertex scale with deg(v)?")
    print("=" * 72)
    print()
    print("Compare:")
    print("  octahedron vertex (deg=4) vs GESBP apex-vertex (deg=4)")
    print("  octahedron vertex (deg=4) vs GESBP belt-vertex (deg=5)")
    print()
    print(f"{'lambda':>8} {'oct(4)':>12} {'gesbp(4)':>12} "
          f"{'gesbp(5)':>12} {'A pred (4:5)':>14} {'B obs ratio':>14}")
    for f in [0.05, 0.10, 0.20, 0.35, 0.50, 0.70, 1.00]:
        oct4 = res1['vertex(deg=4)'][f]
        gesbp4 = res2['vertex(deg=4)'][f]
        gesbp5 = res2['vertex(deg=5)'][f]
        ratio_A_pred = 4 / 5  # Model A predicts deg(v) ratio
        ratio_B_obs = gesbp4 / gesbp5
        print(f"{f:>8.2f} {oct4:>12.6f} {gesbp4:>12.6f} "
              f"{gesbp5:>12.6f} {ratio_A_pred:>14.4f} {ratio_B_obs:>14.4f}")

    print("\n" + "=" * 72)
    print("HEADLINE FINDINGS (answering ChatGPT's Q2)")
    print("=" * 72)

    print("""
1. Model A's site counting is (deg(v), 2, 1, 0) for
   (vertex, edge, face, centroid).

2. Model B's leading-order 'counting' in the SR limit is
   (n_min, d_min) = (1, 0) at vertex, (2, L/2) at edge-mid,
                    (3, d_face) at face, (V, R) at centroid.

3. These are STRUCTURALLY DIFFERENT.  At the vertex site:
     Model A says: E_vertex ~ -deg(v) * B_pair  (linear in deg(v))
     Model B says: E_vertex ~ -V_0 * 1         (constant in deg(v),
                                                 PLUS subleading
                                                 deg(v)-linear
                                                 correction at finite
                                                 lambda with prefactor
                                                 exp(-edge/lambda))

4. At strict SR (lambda / edge << 1), Model B's E_vertex becomes
   independent of deg(v).  This is qualitatively different from
   Model A, which remains linear in deg(v) at all scales.

5. At finite lambda (e.g. the sketch-tested 0.35 * edge), Model B
   picks up a weak deg(v)-linear correction with small coefficient
   exp(-edge/lambda) ~ 0.06.  This is NOT Model A's coupling;
   it is a DISTINCT functional form.

6. Therefore Model B does NOT reduce to Model A.  They agree on
   the qualitative conclusion (vertex wins) but predict different
   quantitative structures at vertex sites.  They are genuinely
   independent derivations of D1.

7. A testable discriminator: Model A predicts E_vertex scales as
   deg(v); Model B predicts it is approximately constant across
   vertices of different degrees.  Phase 1b data is averaged over
   all vertices per polytope, so doesn't discriminate.  A
   site-resolved future measurement would.
""")


if __name__ == "__main__":
    main()
