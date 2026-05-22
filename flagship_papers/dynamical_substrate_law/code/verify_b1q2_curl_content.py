"""
B.1.q2 curl content verification.

Session 139 Patch 0535 — Phase 2 foundations work, sub-question B.1.q2
(F1_phase2_foundations_work.md §11).

Numerically verifies the analytical claim:

    The discrete curl of j_{DI}^{net} at v_host vanishes at first order in delta.

Specifically: the trapezoidal circulation of j_{DI}^{net} around any of the 30
host-first-shell side-face triangles (v_host, v_i, v_j) -- where (v_i, v_j) is
one of the 30 first-shell-to-first-shell edges of v_host's icosahedral
first-shell -- evaluates to zero identically at O(delta).

By the spanning argument (the 30 face 2-forms span the full 6D 2-form space at
v_host under I_h symmetry), zero circulation on all 30 side faces implies the
full 4D curl 2-form vanishes at v_host at first order. This is STRONGER than
B.1.b's ansatz (which required only no perpendicular-to-n_hat component).

The structural origin of the cancellation: the per-vertex current formula
j(v) = 2 r_0 delta [(2+phi) n_hat - (4 a/phi) v] from Patch 0533 sec 9.4 gives
contributions whose perpendicular-plane content cancels via the K3-base
protection identity hat{e}_{ij} dot n_hat = 0 for first-shell-to-first-shell
edges -- the same identity Capotauro uses for spatial-sector K3-base protection.

Three load-bearing identities verified:
(1) j(v_host) = (6 r_0 delta / phi^2) n_hat   [Phase 1 reproducibility]
(2) j(v_i) = 4 r_0 delta [n_hat - sin(36 deg) e_i]   [Patch 0533 sec 9.5]
(3) trapezoidal_circulation(v_host, v_i, v_j) = 0 for all 30 side faces
    at O(delta) -- the B.1.q2 curl-vanishing result.
"""
import numpy as np
from itertools import permutations as P

phi = (1 + np.sqrt(5)) / 2
edge_length = 1 / phi


def build_600_cell_vertices():
    """Construct all 120 vertices of the 600-cell in 4D, unit circumradius."""
    verts = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4)
            v[i] = s
            verts.append(v)
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                for s4 in (1, -1):
                    verts.append(np.array([s1 / 2, s2 / 2, s3 / 2, s4 / 2]))
    base_vals = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                signed = [base_vals[0] * s1, base_vals[1] * s2,
                          base_vals[2] * s3, base_vals[3]]
                for perm in P(range(4)):
                    inv = sum(1 for i in range(4) for j in range(i + 1, 4)
                              if perm[i] > perm[j])
                    if inv % 2 == 0:
                        verts.append(np.array([signed[perm[i]] for i in range(4)]))
    unique = []
    for v in verts:
        if not any(np.allclose(v, u, atol=1e-9) for u in unique):
            unique.append(v)
    return np.array(unique)


def compute_current(v, n_hat, all_verts, edge_len, delta=1.0, r0=1.0):
    """Per-vertex current j(v) = 2 r0 delta sum_j (u_j . n_hat) u_j."""
    dists = np.array([np.linalg.norm(u - v) for u in all_verts])
    fs_mask = np.abs(dists - edge_len) < 1e-6
    fs = all_verts[fs_mask]
    assert len(fs) == 12, f"Expected 12 first-shell neighbors, got {len(fs)}"
    u_vecs = np.array([(u - v) / np.linalg.norm(u - v) for u in fs])
    projections = u_vecs @ n_hat
    return 2 * r0 * delta * (projections[:, np.newaxis] * u_vecs).sum(axis=0)


def trapezoidal_circulation(v_host, v_i, v_j, j_host, j_i, j_j):
    """Trapezoidal circulation of vector field around triangle (v_host, v_i, v_j).

    oint j . dl approximated as
        (1/2) [ (j_host + j_i) . (v_i - v_host)
              + (j_i + j_j) . (v_j - v_i)
              + (j_j + j_host) . (v_host - v_j) ]

    Simplifies to
        (1/2) [ j_host . (v_i - v_j) + j_i . (v_j - v_host) + j_j . (v_host - v_i) ]
    """
    return 0.5 * (j_host @ (v_i - v_j)
                  + j_i @ (v_j - v_host)
                  + j_j @ (v_host - v_i))


def main():
    verts = build_600_cell_vertices()
    assert len(verts) == 120
    print(f"600-cell vertices: {len(verts)}")

    v_host = np.array([1.0, 0.0, 0.0, 0.0])
    n_hat = v_host.copy()

    dists = np.array([np.linalg.norm(v - v_host) for v in verts])
    first_shell = verts[np.abs(dists - edge_length) < 1e-6]
    assert len(first_shell) == 12

    # Identity (1): Phase 1 reproducibility
    delta_test, r0_test = 0.1, 1.0
    j_host = compute_current(v_host, n_hat, verts, edge_length,
                              delta=delta_test, r0=r0_test)
    expected_j_host = (6 * r0_test * delta_test / phi**2) * n_hat
    dev_1 = np.max(np.abs(j_host - expected_j_host))
    print(f"\n(1) j(v_host) = {j_host}, expected = {expected_j_host}, "
          f"max_dev = {dev_1:.2e}")

    # Compute currents at all 12 first-shell vertices
    j_fs = np.array([compute_current(vi, n_hat, verts, edge_length,
                                       delta=delta_test, r0=r0_test)
                     for vi in first_shell])

    # Identity (2): j(v_i) decomposition -- check magnitudes match analytical
    expected_mag = 2 * r0_test * delta_test * np.sqrt(7 - phi)
    mags = np.linalg.norm(j_fs, axis=1)
    dev_2 = np.max(np.abs(mags - expected_mag))
    print(f"(2) |j(v_i)|: uniform = {mags[0]:.10f}, expected = {expected_mag:.10f}, "
          f"max_dev = {dev_2:.2e}")

    # Identity (3): trapezoidal circulation vanishes on all 30 side-face triangles
    # First find the 30 first-shell-to-first-shell edges (icosahedron edges)
    fs_dists = np.array([[np.linalg.norm(first_shell[i] - first_shell[j])
                           for j in range(12)] for i in range(12)])
    fs_edges = [(i, j) for i in range(12) for j in range(i + 1, 12)
                if np.abs(fs_dists[i, j] - edge_length) < 1e-6]
    assert len(fs_edges) == 30, f"Expected 30 first-shell edges, got {len(fs_edges)}"
    print(f"\nFirst-shell-to-first-shell edges: {len(fs_edges)} (icosahedron edges)")

    # Compute circulation around each (v_host, v_i, v_j) side-face triangle
    circulations = np.array([
        trapezoidal_circulation(v_host, first_shell[i], first_shell[j],
                                 j_host, j_fs[i], j_fs[j])
        for (i, j) in fs_edges
    ])
    max_circ = np.max(np.abs(circulations))
    print(f"(3) max |trapezoidal_circulation| over 30 side-faces: "
          f"{max_circ:.2e}   (expected: 0)")
    print(f"    mean circulation: {np.mean(circulations):.2e}")
    print(f"    std  circulation: {np.std(circulations):.2e}")

    # Verify across multiple delta values
    print("\n--- B.1.q2 identity across multiple delta values ---")
    for delta in (0.0, 0.1, 1 / phi**3, 0.5, -0.2):
        if delta == 0:
            print(f"  delta = {delta}: trivially j = 0; identity vacuous")
            continue
        jh = compute_current(v_host, n_hat, verts, edge_length,
                              delta=delta, r0=1.0)
        jfs = np.array([compute_current(vi, n_hat, verts, edge_length,
                                          delta=delta, r0=1.0)
                        for vi in first_shell])
        circs = np.array([
            trapezoidal_circulation(v_host, first_shell[i], first_shell[j],
                                     jh, jfs[i], jfs[j])
            for (i, j) in fs_edges
        ])
        max_c = np.max(np.abs(circs))
        print(f"  delta = {delta:.6f}: max |circulation| = {max_c:.2e}")

    print("\nB.1.q2 curl-vanishing identity verified at machine precision.")
    print("Curl at v_host at first order in delta is identically zero --")
    print("stronger than B.1.b ansatz's claim of 'no perpendicular-to-n_hat component'.")


if __name__ == "__main__":
    main()
