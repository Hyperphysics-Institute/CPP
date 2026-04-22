#!/usr/bin/env python3
# ============================================================
# SS-8 OPEN-SS-26: SSV-minimization sketch for D1
# Purpose: evaluate interstitial-neutron binding energy at 4
#          candidate site classes on two test alpha-polytopes
#          (octahedron N_α=6, GESBP N_α=10) under two models.
# Author:  Claude Opus, 21 April 2026
# ============================================================

import numpy as np
from itertools import combinations


# ---------- polytope 1: octahedron (N_α = 6) ----------

def octahedron():
    """Regular octahedron with unit circumradius.
    Vertices on coordinate axes; edge length = sqrt(2)."""
    V = np.array([
        [ 1,  0,  0], [-1,  0,  0],
        [ 0,  1,  0], [ 0, -1,  0],
        [ 0,  0,  1], [ 0,  0, -1],
    ], dtype=float)
    # edges: non-antipodal vertex pairs (antipodal pairs: (0,1),(2,3),(4,5))
    edges = []
    for i, j in combinations(range(6), 2):
        if i // 2 != j // 2:
            edges.append((i, j))
    # faces: triangles picking one vertex from each antipodal pair
    faces = [(a, b, c) for a in (0, 1) for b in (2, 3) for c in (4, 5)]
    return V, edges, faces


# ---------- polytope 2: gyroelongated square bipyramid (N_α = 10) ----------

def gesbp():
    """Regular gyroelongated square bipyramid (Johnson solid J17).
    All edges unit length. Returns (V, edges, faces)."""
    # geometry for unit edges
    r = 1 / np.sqrt(2)          # square circumradius
    h_mid = np.sqrt(0.5 - (r - 0.5) ** 2 - 0.25) / 2
    # solve: (r - 1/2)^2 + (1/2)^2 + (2 h_mid)^2 = 1
    #   → 4 h_mid^2 = 1 - 1/4 - (r - 1/2)^2
    val = 1.0 - 0.25 - (r - 0.5) ** 2
    h_mid = 0.5 * np.sqrt(val)
    h_top = h_mid + 1 / np.sqrt(2)
    # vertices
    top_apex = np.array([0, 0,  h_top])
    bot_apex = np.array([0, 0, -h_top])
    top_sq = np.array([[r * np.cos(k * np.pi / 2),
                        r * np.sin(k * np.pi / 2),
                         h_mid] for k in range(4)])
    bot_sq = np.array([[r * np.cos(k * np.pi / 2 + np.pi / 4),
                        r * np.sin(k * np.pi / 2 + np.pi / 4),
                        -h_mid] for k in range(4)])
    V = np.vstack([top_apex[None, :], top_sq, bot_sq, bot_apex[None, :]])
    # indexing: 0=top_apex, 1..4=top_sq, 5..8=bot_sq, 9=bot_apex

    # edges: find all vertex pairs within edge-length tolerance
    edges = []
    for i, j in combinations(range(10), 2):
        if abs(np.linalg.norm(V[i] - V[j]) - 1.0) < 1e-6:
            edges.append((i, j))

    # faces: triangulate by looking for triangles whose edges are all in `edges`
    E = set(tuple(sorted(e)) for e in edges)
    faces = []
    for i, j, k in combinations(range(10), 3):
        if (all(tuple(sorted(p)) in E for p in [(i, j), (j, k), (i, k)])):
            faces.append((i, j, k))
    return V, edges, faces


# ---------- site enumeration ----------

def site_classes(V, edges, faces):
    """Return dict mapping site-class name → list of (position, meta).
    meta includes e.g. degree for vertex sites, participation counts."""
    out = {}

    # vertex sites: the vertex positions themselves, displaced infinitesimally
    # outward (handled symbolically — site is "at" v for counting purposes)
    vertex_deg = [0] * len(V)
    for i, j in edges:
        vertex_deg[i] += 1
        vertex_deg[j] += 1
    out['vertex'] = [(V[i], {'index': i, 'degree': vertex_deg[i]})
                      for i in range(len(V))]

    # edge-midpoint sites
    out['edge_mid'] = [((V[i] + V[j]) / 2, {'edge': (i, j)})
                        for i, j in edges]

    # face-center sites
    out['face_center'] = [((V[i] + V[j] + V[k]) / 3, {'face': (i, j, k)})
                           for i, j, k in faces]

    # centroid (single site)
    out['centroid'] = [(np.mean(V, axis=0), {})]

    return out


# ---------- counting-rule energy (model A: pure K_3 face participation) ----------

def face_participation_count(site_pos, site_meta, site_class, faces):
    """Count K_3 faces 'participating' with a neutron at the given site.

    Counting rule (derived from D2 as stated in the note):
      - vertex v:   count faces incident at v (= degree of v)
      - edge e:     count faces containing edge e (= 2 for simplicial polytope)
      - face f:     count = 1 (the face itself)
      - centroid:   count = 0 (not inside or adjacent to any face)
    """
    if site_class == 'vertex':
        v = site_meta['index']
        return sum(1 for (a, b, c) in faces if v in (a, b, c))
    if site_class == 'edge_mid':
        i, j = site_meta['edge']
        return sum(1 for (a, b, c) in faces
                   if i in (a, b, c) and j in (a, b, c))
    if site_class == 'face_center':
        return 1
    if site_class == 'centroid':
        return 0
    raise ValueError(f"unknown site class: {site_class}")


# ---------- SR-nn-pair SSV energy (model B: Yukawa-like pair potential) ----------

def ssv_energy_nnpair(site_pos, V, lam, V0=1.0):
    """Neutron SSV energy = sum over alpha-outer-nucleons of -V0 * exp(-d/lam).

    Treats each alpha-vertex as the location of its outer nucleon.
    Units: V0 sets the per-contact reference scale; lam is the SR range
    in units of the polytope circumradius.

    SR regime: lam << typical edge length. For octahedron edge = sqrt(2).
    """
    dists = np.linalg.norm(V - site_pos, axis=1)
    return -V0 * np.sum(np.exp(-dists / lam))


# ---------- the main computation ----------

def evaluate_polytope(name, V, edges, faces, lam_frac=0.35):
    """Evaluate both models at all site classes, report class-best site."""
    print(f"\n{'=' * 70}")
    print(f"POLYTOPE: {name}")
    print(f"  V = {len(V)}, E = {len(edges)}, F = {len(faces)}")
    print(f"  2E/V (average degree) = {2 * len(edges) / len(V):.3f}")
    print(f"  6 - 12/V              = {6 - 12 / len(V):.3f}")
    edge_len = np.linalg.norm(V[edges[0][0]] - V[edges[0][1]])
    lam = lam_frac * edge_len
    print(f"  reference edge length = {edge_len:.4f}")
    print(f"  SR-nn-pair range lam  = {lam:.4f} "
          f"(= {lam_frac} × edge length)")
    print()

    sites = site_classes(V, edges, faces)

    # Model A: face-participation count
    print(f"MODEL A — K_3 face-participation count (D2-derived counting rule)")
    print(f"{'class':<14} {'best site':<20} "
          f"{'participation':>13} {'E / B_pair':>12}")
    print("-" * 63)
    resA = {}
    for cls, sites_of_cls in sites.items():
        counts = [face_participation_count(p, m, cls, faces)
                  for (p, m) in sites_of_cls]
        best = max(counts) if counts else 0
        best_idx = counts.index(best) if counts else -1
        best_site = sites_of_cls[best_idx] if best_idx >= 0 else None
        label = (f"deg={best_site[1].get('degree', '?')}"
                 if cls == 'vertex' else str(best_site[1]))
        resA[cls] = {'count': best, 'label': label}
        print(f"{cls:<14} {label:<20} "
              f"{best:>13d} {-float(best):>12.3f}")

    # Model B: SR-nn-pair Yukawa
    print(f"\nMODEL B — SR-nn-pair SSV (Yukawa-like), lam = {lam:.3f}")
    print(f"{'class':<14} {'best site':<20} "
          f"{'E / V_0':>13} {'rel. to vertex':>16}")
    print("-" * 67)
    E_vertex = None
    resB = {}
    for cls, sites_of_cls in sites.items():
        energies = [ssv_energy_nnpair(p, V, lam) for (p, m) in sites_of_cls]
        best_E = min(energies)
        best_idx = energies.index(best_E)
        best_site = sites_of_cls[best_idx]
        label = (f"deg={best_site[1].get('degree', '?')}"
                 if cls == 'vertex' else str(best_site[1])[:18])
        if cls == 'vertex':
            E_vertex = best_E
        rel = best_E / E_vertex if E_vertex else float('nan')
        resB[cls] = {'E': best_E, 'label': label, 'rel': rel}
        print(f"{cls:<14} {label:<20} "
              f"{best_E:>13.5f} {rel:>15.3f}×")

    return resA, resB


# ---------- cross-polytope summary ----------

def main():
    print("=" * 70)
    print("SS-8 OPEN-SS-26 — SSV minimization sketch for D1")
    print("Evaluating vertex vs edge-mid vs face-center vs centroid")
    print("=" * 70)

    # octahedron
    V1, E1, F1 = octahedron()
    resA_oct, resB_oct = evaluate_polytope("Octahedron (N_α = 6)",
                                            V1, E1, F1)

    # GESBP
    V2, E2, F2 = gesbp()
    resA_gesbp, resB_gesbp = evaluate_polytope(
        "Gyroelongated square bipyramid (N_α = 10)",
        V2, E2, F2)

    # headline
    print("\n" + "=" * 70)
    print("HEADLINE RESULT")
    print("=" * 70)
    print()
    print("MODEL A (face-participation counting, derived from D2):")
    print(f"  Octahedron:  vertex wins with deg=4 K_3 faces × B_pair;")
    print(f"               runner-up edge-mid at 2; gap factor 2.00.")
    print(f"  GESBP:       best vertex (belt) wins with deg=5 × B_pair;")
    print(f"               runner-up edge-mid at 2; gap factor 2.50.")
    print(f"  → vertex always wins because every simplicial polytope has")
    print(f"    min vertex degree ≥ 3 (triangulated sphere), and an edge")
    print(f"    is in exactly 2 faces while a face-center is in 1.")
    print()
    print("MODEL B (SR-nn-pair Yukawa SSV, lam = 0.35 × edge):")
    print(f"  Octahedron:  vertex wins — E_vertex / E_edge-mid < 1 (deeper)")
    print(f"  GESBP:       vertex wins — same pattern")
    print(f"  → vertex wins because at lam << edge, only sites adjacent to")
    print(f"    an alpha-vertex receive non-suppressed pair-contact energy.")
    print()
    print("CONCLUSION")
    print("-" * 70)
    print("Model A makes vertex-preference a trivial consequence of D2's")
    print("counting rule (degree ≥ 3 > 2 > 1 > 0 for the four site classes).")
    print("Model B gives the same vertex-preference from SR-nn-pair physics,")
    print("independent of D2.  The two arguments converge on D1 via")
    print("independent premises:")
    print("  - Model A needs D2 (counting rule) to be stated.")
    print("  - Model B needs SR-nn-pair range lam << L_αα (inherited from")
    print("    SS-5 pair physics and SS-7 alpha-alpha contact distance).")
    print()
    print("Under either premise, D1 follows.  Neither is a pure-primitive")
    print("derivation, so D1 promotes to 'conditional theorem' status only.")
    print("The primary remaining open problem is OPEN-SS-27 (deriving D2")
    print("from A6' at the interstitial-nucleon scale).")
    print("=" * 70)


if __name__ == "__main__":
    main()
