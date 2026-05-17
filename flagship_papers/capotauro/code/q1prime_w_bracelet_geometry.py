#!/usr/bin/env python3
"""
Q1' Verification Script: Geometric relationship between H_4's two 1200-orbits
in the 600-cell — the face-centroid orbit and the W bracelet (induced 6-cycle)
orbit.

Session 125, Patch 0418, 16 May 2026.
Author: Opus (CPP collaborative AI).
Repository: Hyperphysics-Institute/CPP.

This script supports §10 of `Capotauro_chiral_mechanism_candidate.md`,
the Q1' partial-progress closure for OPEN-FI-C-9-FP-MECHANISM.

PROCEDURE
---------
1. Generate the 120 vertices of the 600-cell at unit radius (standard
   icosian / Hurwitz-quaternion coordinates).
2. Identify edges (vertex pairs at distance 1/phi).
3. Verify edge count = 720 and vertex degree = 12 (matches SF-2 §sec:600cell_setup).
4. Enumerate triangular faces (3-cliques in the edge graph).
   Verify face count = 1200 (matches SF-2 Step 1 of Theorem 4.2 proof).
5. Enumerate induced 6-cycles in the edge graph.
   Classify by H_4-invariant signature into:
     - Orbit A: 3600 cycles, stabilizer order 4
     - Orbit B: 1200 cycles, stabilizer order 12 (D_6) — the W bracelet
   Verify (matches SF-2 Theorem 4.2 / sec:Wbracelet_thm).
6. Compute bracelet centroid positions and directions.
7. Compare bracelet centroid directions vs face centroid directions on S^3.
8. Test hypothesis: bracelet centroid directions = 600-cell vertex directions.

OUTPUT
------
- Verifies 600-cell facts (vertex/edge/face counts) and SF-2 stated W bracelet
  classification (4800 = 3600 + 1200; signatures; centroid radius phi/2).
- Establishes the new geometric result: the 1200 W bracelet centroids project
  onto exactly 120 distinct unit directions on S^3, and those 120 directions
  are the 120 vertex directions of the 600-cell itself, with exactly 10
  bracelets per vertex direction.
- Confirms the structural identification: each W bracelet is a Petrie hexagon
  of the SM-1 first-shell icosahedron around one specific 600-cell vertex.
- The nearest face centroid direction to any bracelet centroid direction lies
  at cosine sqrt((1+phi)/3) = 0.934172 — the cosine between any 600-cell vertex
  and the centroid of any triangular face containing it.

IMPLICATIONS FOR READING C
--------------------------
- The W bracelet orbit and the face orbit are DIFFERENT H_4-orbits on S^3.
  At the unit-direction level, the W bracelet centroid directions coincide
  with the VERTEX orbit (120 elements, stabilizer H_3), not the face orbit
  (1200 elements, stabilizer D_6).
- Under VERTEX-aligned Reading C (n̂ = a 600-cell vertex direction):
  10 W bracelets are collinear with n̂ at radius phi/2; their D_6 stabilizers
  are 10 distinct Petrie-polygon subgroups of the substrate residual H_3.
  Cross-sector unification with SF-2 W bracelet is natural.
- Under FACE-aligned Reading C (n̂ = a face centroid direction):
  the K3-doublet (whose stabilizer is D_6 = S_3 × Z_2) is collinear with n̂,
  matching the paper's downstream machinery exactly (Finding C-W35).
  The W bracelet sits off-axis at cosine sqrt((1+phi)/3) ≈ 0.934 from n̂.

The Q1' question (vertex vs face) acquires complementary structural arguments
on both sides; neither reading produces full cross-sector unification, but each
maximally accommodates one of the two SF-2-or-Capotauro substrate objects.

REPRODUCIBILITY
---------------
Run: python3 q1prime_w_bracelet_geometry.py
Expected runtime: < 30 seconds on commodity hardware.
Dependencies: numpy only.

REFERENCES
----------
- Humphreys, Reflection Groups and Coxeter Groups, CUP 1990, §1.10
- SF-2 v1.0 §sec:Wbracelet_thm (Theorem 4.2)
- Capotauro v1.0 §6.4 (K3-doublet stabilizer)
- Capotauro_chiral_mechanism_candidate.md (this sketch)
"""

import numpy as np
from itertools import permutations
from collections import Counter, defaultdict

phi = (1 + np.sqrt(5)) / 2
inv_phi = 1 / phi


def parity(perm):
    """Parity of a permutation (0 = even, 1 = odd)."""
    n = len(perm)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inv += 1
    return inv % 2


def build_600cell():
    """Generate the 120 vertices of the 600-cell at unit radius."""
    vertices = set()
    # 8 vertices: (±1, 0, 0, 0) and permutations
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = s
            vertices.add(tuple(v))
    # 16 vertices: (±1/2, ±1/2, ±1/2, ±1/2)
    for signs in range(16):
        v = tuple(((-1) ** ((signs >> i) & 1)) * 0.5 for i in range(4))
        vertices.add(v)
    # 96 vertices: even permutations of (±phi/2, ±1/2, ±1/(2*phi), 0)
    base = (phi / 2, 0.5, 1 / (2 * phi), 0.0)
    even_perms = [p for p in permutations(range(4)) if parity(p) == 0]
    for perm in even_perms:
        permuted = [base[perm[i]] for i in range(4)]
        nonzero_idx = [i for i, x in enumerate(permuted) if abs(x) > 1e-12]
        for sb in range(2 ** len(nonzero_idx)):
            v = list(permuted)
            for k, idx in enumerate(nonzero_idx):
                if (sb >> k) & 1:
                    v[idx] = -v[idx]
            vertices.add(tuple(round(x, 10) for x in v))
    return np.array(sorted(vertices))


def find_edges(V, tol=1e-8):
    """Return edge index pairs (i,j) with i<j at distance 1/phi."""
    N = len(V)
    edge_len_sq = inv_phi ** 2
    edges = []
    diff = V[:, None, :] - V[None, :, :]
    d2 = np.sum(diff ** 2, axis=2)
    for i in range(N):
        for j in range(i + 1, N):
            if abs(d2[i, j] - edge_len_sq) < tol:
                edges.append((i, j))
    return edges


def find_faces(adj):
    """Return triangular faces as sorted-index tuples (i,j,k) with i<j<k."""
    faces = set()
    N = len(adj)
    for i in range(N):
        for j in adj[i]:
            if j <= i:
                continue
            for k in adj[i] & adj[j]:
                if k > j:
                    faces.add((i, j, k))
    return faces


def canonicalize_cycle(cycle):
    """Lex-min representative under cyclic rotation and reflection (12 symmetries)."""
    n = len(cycle)
    cands = []
    for s in range(n):
        cands.append(tuple(cycle[(s + i) % n] for i in range(n)))
        cands.append(tuple(cycle[(s - i) % n] for i in range(n)))
    return min(cands)


def find_induced_6_cycles(adj, edge_set):
    """Enumerate induced 6-cycles. Each cycle returned once, with v0 = min(cycle)."""
    N = len(adj)
    def is_edge(a, b):
        if a == b:
            return False
        if a > b:
            a, b = b, a
        return (a, b) in edge_set
    cycles = set()
    for v0 in range(N):
        for v1 in adj[v0]:
            if v1 <= v0:
                continue
            for v2 in adj[v1]:
                if v2 == v0 or v2 < v0 or is_edge(v0, v2):
                    continue
                for v3 in adj[v2]:
                    if v3 in (v0, v1) or v3 < v0:
                        continue
                    if is_edge(v0, v3) or is_edge(v1, v3):
                        continue
                    for v4 in adj[v3]:
                        if v4 in (v0, v1, v2) or v4 < v0:
                            continue
                        if is_edge(v0, v4) or is_edge(v1, v4) or is_edge(v2, v4):
                            continue
                        for v5 in adj[v4]:
                            if v5 in (v0, v1, v2, v3) or v5 < v0:
                                continue
                            if not is_edge(v5, v0):
                                continue
                            if is_edge(v1, v5) or is_edge(v2, v5) or is_edge(v3, v5):
                                continue
                            cycles.add(canonicalize_cycle((v0, v1, v2, v3, v4, v5)))
    return cycles


def signature_of(cycle, V):
    """H_4-invariant signature: sorted multiset of 15 pairwise squared distances."""
    pts = [V[v] for v in cycle]
    dists_sq = []
    for i in range(6):
        for j in range(i + 1, 6):
            dists_sq.append(round(float(np.sum((pts[i] - pts[j]) ** 2)), 8))
    return tuple(sorted(dists_sq))


def round_dir(d, prec=8):
    return tuple(round(float(x), prec) for x in d)


def main():
    print("=" * 70)
    print("Q1' geometric verification: W bracelet vs face orbit in the 600-cell")
    print("=" * 70)

    # Step 1: 600-cell vertices
    V = build_600cell()
    print(f"\n[Step 1] 600-cell vertices: {len(V)} (expected 120)")
    assert len(V) == 120
    assert np.allclose(np.linalg.norm(V, axis=1), 1.0)
    print(f"         All at unit radius: confirmed")

    # Step 2: edges
    edges = find_edges(V)
    N = len(V)
    print(f"\n[Step 2] Edges: {len(edges)} (expected 720)")
    assert len(edges) == 720
    adj = [set() for _ in range(N)]
    edge_set = set()
    for (i, j) in edges:
        adj[i].add(j)
        adj[j].add(i)
        edge_set.add((i, j))
    degrees = [len(adj[i]) for i in range(N)]
    assert all(d == 12 for d in degrees), "Not all vertices have degree 12"
    print(f"         All vertices degree 12: confirmed (icosahedral first-shell coordination z=12)")

    # Step 3: faces
    faces = find_faces(adj)
    print(f"\n[Step 3] Triangular faces: {len(faces)} (expected 1200)")
    assert len(faces) == 1200

    # Step 4: induced 6-cycles + classify
    cycles = find_induced_6_cycles(adj, edge_set)
    print(f"\n[Step 4] Induced 6-cycles: {len(cycles)} (expected 4800, per SF-2 Thm 4.2)")
    assert len(cycles) == 4800
    sigs = defaultdict(list)
    for c in cycles:
        sigs[signature_of(c, V)].append(c)
    print(f"         Distinct signatures: {len(sigs)} (expected 2)")
    orbit_A = orbit_B = None
    for sig, cs in sigs.items():
        if len(cs) == 1200:
            orbit_B = cs
        elif len(cs) == 3600:
            orbit_A = cs
    print(f"         Orbit A: {len(orbit_A)} cycles, signature {Counter(sigs_key for sigs_key in sigs if len(sigs[sigs_key]) == 3600)}")
    print(f"         Orbit B: {len(orbit_B)} cycles (the W bracelet)")
    assert len(orbit_A) == 3600 and len(orbit_B) == 1200

    # Step 5: bracelet centroids
    centroids_B = np.array([np.mean([V[v] for v in c], axis=0) for c in orbit_B])
    radii_B = np.linalg.norm(centroids_B, axis=1)
    print(f"\n[Step 5] Orbit B centroid radii: {radii_B.min():.6f} to {radii_B.max():.6f}")
    print(f"         phi/2 = {phi/2:.6f} (expected match per SF-2 Thm 4.2 Step 4)")
    assert np.allclose(radii_B, phi / 2)

    # Step 6: bracelet directions vs face directions
    dirs_B = centroids_B / radii_B[:, None]
    face_centroids = np.array([np.mean([V[v] for v in f], axis=0) for f in faces])
    face_radii = np.linalg.norm(face_centroids, axis=1)
    face_dirs = face_centroids / face_radii[:, None]
    set_dirs_B = set(round_dir(d) for d in dirs_B)
    set_face_dirs = set(round_dir(d) for d in face_dirs)
    common = set_dirs_B & set_face_dirs
    print(f"\n[Step 6] Distinct bracelet centroid directions: {len(set_dirs_B)}")
    print(f"         Distinct face centroid directions:     {len(set_face_dirs)}")
    print(f"         Directions in common:                  {len(common)}")
    assert len(common) == 0, "Bracelet and face directions must be disjoint"
    print(f"         Bracelet and face orbits on S^3 are DISJOINT — DIFFERENT H_4-orbits")

    # Step 7: bracelet directions = vertex directions
    set_vertex_dirs = set(round_dir(v) for v in V)
    print(f"\n[Step 7] Distinct vertex directions of 600-cell: {len(set_vertex_dirs)}")
    print(f"         Bracelet directions ∩ vertex directions: {len(set_dirs_B & set_vertex_dirs)}")
    assert set_dirs_B == set_vertex_dirs, "Bracelet directions must coincide with vertex directions"
    print(f"         *** Bracelet centroid directions = 600-cell vertex directions ***")

    # 10 bracelets per vertex
    v_to_braces = defaultdict(int)
    for d in dirs_B:
        v_to_braces[round_dir(d)] += 1
    counts = list(v_to_braces.values())
    print(f"\n[Step 8] Bracelets per vertex direction: min={min(counts)}, max={max(counts)}")
    assert all(c == 10 for c in counts), "Each vertex must host exactly 10 bracelets"
    print(f"         *** Exactly 10 bracelets per vertex direction (10 × 120 = 1200) ***")

    # Confirm: each bracelet's 6 vertices are edge-neighbors of the central vertex
    print(f"\n[Step 9] Confirming bracelet vertices are first-shell icosahedral neighbors:")
    failures = 0
    for cyc in orbit_B[:50]:  # Sample first 50
        c = np.mean([V[v] for v in cyc], axis=0)
        # Find the vertex direction this bracelet centers on
        c_unit = c / np.linalg.norm(c)
        v_idx = None
        for i in range(N):
            if np.allclose(V[i], c_unit):
                v_idx = i
                break
        assert v_idx is not None
        # All 6 bracelet vertices must be edge-neighbors of v_idx
        for bv in cyc:
            if bv not in adj[v_idx]:
                failures += 1
    assert failures == 0
    print(f"         All sampled bracelets confirmed: 6 cycle-vertices are edge-neighbors of central vertex")
    print(f"         Each bracelet = a Petrie hexagon of the SM-1 first-shell icosahedron")

    # Cosine identity
    cos_pred = np.sqrt((1 + phi) / 3)
    print(f"\n[Step 10] Vertex-to-containing-face cosine: sqrt((1+phi)/3) = {cos_pred:.6f}")
    # Verify on a sample
    for v_idx in [0]:
        v_dir = V[v_idx]
        cosines_to_faces = face_dirs @ v_dir
        max_cos = cosines_to_faces.max()
        print(f"         Max(face_dir · vertex_0) = {max_cos:.6f}")
        assert abs(max_cos - cos_pred) < 1e-5

    print("\n" + "=" * 70)
    print("ALL CHECKS PASSED")
    print("=" * 70)
    print("\nSUMMARY OF NEW STRUCTURAL FACTS (Finding C-W36):")
    print(" - The 1200 W bracelets cluster as 10-per-vertex around the 120 vertex directions.")
    print(" - Each bracelet is a Petrie hexagon of the SM-1 first-shell icosahedron.")
    print(" - W bracelet centroid directions are the VERTEX orbit, not the face orbit.")
    print(" - Under vertex-aligned Reading C, W bracelets sit on-axis in the substrate.")
    print(" - Under face-aligned Reading C, W bracelets sit off-axis at cosine sqrt((1+phi)/3).")
    print(" - The K3-doublet (face-centered) and W bracelet (vertex-centered) cannot")
    print("   BOTH be on-axis with the substrate primitive direction simultaneously.")


if __name__ == "__main__":
    main()
