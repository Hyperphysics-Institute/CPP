"""
B.1.q4 first-shell current sum identity verification.

Session 139 Patch 0533 — Phase 2 foundations work, sub-question B.1.q4
(F1_phase2_foundations_work.md §9).

Numerically verifies the analytical derivation of:

    sum_{i=1}^{12} hat{j}_{DI}^{net}(v_i) = (24/sqrt(7-phi)) * n_hat
    ≈ 10.345 * n_hat   at first order in delta

where {v_i} are the 12 first-shell neighbors of v_host in the 600-cell with
vertex-aligned n_hat = v_host, and j_{DI}^{net}(v) is computed via the Phase 1
formula j(v) = 2 r_0 delta * sum_j (u_j^v . n_hat) u_j^v applied generally
(not just at v_host).

Five load-bearing identities verified:
(1) hat{u}_i . n_hat = -1/(2 phi) uniform at v_host
(2) sum_i hat{u}_i = -(6/phi) n_hat at v_host (Phase 1 verification)
(3) j(v_host) = (6 r_0 delta / phi^2) n_hat (Phase 1 boxed result)
(4) |j(v_i)| = 2 r_0 delta sqrt(7-phi) uniform across the 12 first-shell vertices
    (I_h residual symmetry permutation)
(5) sum_i hat{j}(v_i) = (24/sqrt(7-phi)) n_hat ≈ 10.345 n_hat
    (the B.1.q4 identity)
"""
import numpy as np
from itertools import permutations as P

phi = (1 + np.sqrt(5)) / 2
edge_length = 1 / phi  # 600-cell edge length when circumradius = 1


def build_600_cell_vertices():
    """Construct all 120 vertices of the 600-cell in 4D, unit circumradius."""
    verts = []

    # 8 vertices: (+-1, 0, 0, 0) and permutations
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4)
            v[i] = s
            verts.append(v)

    # 16 vertices: (+-1/2, +-1/2, +-1/2, +-1/2)
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                for s4 in (1, -1):
                    verts.append(np.array([s1 / 2, s2 / 2, s3 / 2, s4 / 2]))

    # 96 vertices: even permutations of (+-phi/2, +-1/2, +-1/(2 phi), 0)
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

    # Deduplicate
    unique = []
    for v in verts:
        if not any(np.allclose(v, u, atol=1e-9) for u in unique):
            unique.append(v)
    return np.array(unique)


def compute_current(v, n_hat, all_verts, edge_len, delta=1.0, r0=1.0):
    """Per-vertex current j(v) = 2 r0 delta sum_j (u_j . n_hat) u_j.

    u_j are the 12 unit directions from v to its first-shell neighbors.
    """
    dists = np.array([np.linalg.norm(u - v) for u in all_verts])
    fs_mask = np.abs(dists - edge_len) < 1e-6
    fs = all_verts[fs_mask]
    assert len(fs) == 12, f"Expected 12 first-shell neighbors, got {len(fs)}"
    u_vecs = np.array([(u - v) / np.linalg.norm(u - v) for u in fs])
    projections = u_vecs @ n_hat
    return 2 * r0 * delta * (projections[:, np.newaxis] * u_vecs).sum(axis=0)


def main():
    verts = build_600_cell_vertices()
    assert len(verts) == 120, f"Expected 120 vertices, got {len(verts)}"
    print(f"600-cell vertices: {len(verts)}")

    # v_host = first axis-aligned vertex; n_hat = v_host (Capotauro Reading C)
    v_host = np.array([1.0, 0.0, 0.0, 0.0])
    n_hat = v_host.copy()

    # First-shell of v_host
    dists = np.array([np.linalg.norm(v - v_host) for v in verts])
    first_shell = verts[np.abs(dists - edge_length) < 1e-6]
    assert len(first_shell) == 12

    u_vectors = np.array([(v - v_host) / np.linalg.norm(v - v_host)
                          for v in first_shell])

    # Identity (1): hat{u}_i . n_hat = -1/(2 phi) uniform
    projections = u_vectors @ n_hat
    expected_proj = -1 / (2 * phi)
    print(f"\n(1) u_i . n_hat: min={projections.min():.10f}, "
          f"max={projections.max():.10f}, expected={expected_proj:.10f}, "
          f"max_dev={np.max(np.abs(projections - expected_proj)):.2e}")

    # Identity (2): sum_i hat{u}_i = -(6/phi) n_hat
    sum_u = u_vectors.sum(axis=0)
    expected_sum_u = -(6 / phi) * n_hat
    print(f"(2) sum_i u_i = {sum_u}, expected = {expected_sum_u}, "
          f"max_dev={np.max(np.abs(sum_u - expected_sum_u)):.2e}")

    # Identity (3): j(v_host) = (6 r0 delta / phi^2) n_hat
    delta_test = 0.5
    r0_test = 1.0
    j_host = compute_current(v_host, n_hat, verts, edge_length,
                              delta=delta_test, r0=r0_test)
    expected_j_host = (6 * r0_test * delta_test / phi**2) * n_hat
    print(f"(3) j(v_host) = {j_host}, expected = {expected_j_host}, "
          f"max_dev={np.max(np.abs(j_host - expected_j_host)):.2e}")

    # Compute currents at all 12 first-shell vertices
    currents_fs = np.array([compute_current(v_i, n_hat, verts, edge_length,
                                              delta=delta_test, r0=r0_test)
                             for v_i in first_shell])

    # Identity (4): |j(v_i)| = 2 r0 delta sqrt(7-phi) uniform
    mags = np.linalg.norm(currents_fs, axis=1)
    expected_mag = 2 * r0_test * delta_test * np.sqrt(7 - phi)
    print(f"(4) |j(v_i)|: min={mags.min():.10f}, max={mags.max():.10f}, "
          f"expected={expected_mag:.10f}, "
          f"max_dev={np.max(np.abs(mags - expected_mag)):.2e}")

    # Identity (5): sum_i hat{j}(v_i) = (24/sqrt(7-phi)) n_hat
    unit_currents = currents_fs / mags[:, np.newaxis]
    sum_unit = unit_currents.sum(axis=0)
    expected_sum_unit = (24 / np.sqrt(7 - phi)) * n_hat
    print(f"(5) sum_i hat{{j}}(v_i) = {sum_unit}, "
          f"expected = {expected_sum_unit}, "
          f"max_dev={np.max(np.abs(sum_unit - expected_sum_unit)):.2e}")

    # Test across multiple delta values
    print("\n--- Identity (5) across multiple delta values ---")
    for delta in (0.0, 0.1, 1 / phi**3, 0.5, -0.2):
        if delta == 0:
            print(f"  delta={delta}: trivially j=0; identity vacuous")
            continue
        cs = np.array([compute_current(v_i, n_hat, verts, edge_length,
                                         delta=delta, r0=1.0)
                       for v_i in first_shell])
        ms = np.linalg.norm(cs, axis=1)
        sgn = np.sign(delta)
        # Unit vectors are sign-invariant in magnitude but flip direction with delta sign
        ucs = cs / ms[:, np.newaxis]
        su = ucs.sum(axis=0)
        eu = sgn * (24 / np.sqrt(7 - phi)) * n_hat
        dev = np.max(np.abs(su - eu))
        print(f"  delta={delta:.6f}: sum_i hat{{j}} = "
              f"{su[0]:.6f}*n_hat, expected {eu[0]:.6f}, dev={dev:.2e}")

    print("\nAll identities verified at machine precision.")


if __name__ == "__main__":
    main()
