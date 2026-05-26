"""
F.1 Sub-Question Phase 1 verification — Net DI-bit current at host vertex.

Constructs the 600-cell vertex coordinates explicitly, picks a host vertex,
identifies its 12 first-shell neighbors, and verifies the substrate-locality
geometric facts + the Phase 1 Mechanism A current computation:

  (1) hat_u_i . hat_n = -1/(2*phi) for all 12 first-shell unit vectors
  (2) sum_i hat_u_i = -(6/phi) * hat_n  [orthogonal components cancel by I_h]
  (3) sum_i (hat_u_i . hat_n) * hat_u_i = (3/phi^2) * hat_n
  (4) Net DI-bit current: j_DI^net = (6 r_0 delta / phi^2) * hat_n at first order

These are cross-checks against analytic results derived under the substrate-
locality framework. Run from CPP repo root:
  python3 series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/code/verify_phase1.py

No external dependencies beyond NumPy. Runtime < 5 seconds.
"""
import numpy as np
from itertools import permutations, product

PHI = (1.0 + np.sqrt(5.0)) / 2.0

def gen_600cell_vertices():
    """Generate the 120 vertices of the regular 600-cell on S^3.

    Standard construction (Coxeter): 8 + 16 + 96 = 120 vertices, all at unit
    distance from origin, edge length 1/phi.
      - 8 vertices: (+/-1, 0, 0, 0) and permutations
      - 16 vertices: (+/-1/2, +/-1/2, +/-1/2, +/-1/2)
      - 96 vertices: even permutations of (+/-phi/2, +/-1/2, +/-1/(2*phi), 0)
    """
    verts = set()

    # 8 vertices: (+/-1, 0, 0, 0) and permutations
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4
            v[i] = s
            verts.add(tuple(v))

    # 16 vertices: (+/-1/2)^4
    for signs in product((0.5, -0.5), repeat=4):
        verts.add(signs)

    # 96 vertices: even permutations of (+/-phi/2, +/-1/2, +/-1/(2*phi), 0)
    base = (PHI/2.0, 0.5, 1.0/(2.0*PHI), 0.0)
    for perm in permutations(range(4)):
        # parity of permutation
        inv = sum(1 for i in range(4) for j in range(i+1,4) if perm[i] > perm[j])
        if inv % 2 != 0:
            continue
        # all sign choices on the 3 nonzero entries
        for s1, s2, s3 in product((1.0,-1.0), repeat=3):
            entry = [0.0]*4
            entry[perm[0]] = s1 * base[0]
            entry[perm[1]] = s2 * base[1]
            entry[perm[2]] = s3 * base[2]
            entry[perm[3]] = 0.0 * base[3]
            verts.add(tuple(entry))

    arr = np.array(sorted(verts))
    assert arr.shape == (120, 4), f"Expected 120 vertices, got {arr.shape[0]}"
    # All on unit sphere?
    norms = np.linalg.norm(arr, axis=1)
    assert np.allclose(norms, 1.0), f"Vertex norms not unit: range [{norms.min()}, {norms.max()}]"
    return arr

def find_first_shell(verts, host_idx, target_edge_length):
    """Return indices of first-shell (nearest) neighbors of the host vertex."""
    v0 = verts[host_idx]
    diffs = verts - v0
    dists = np.linalg.norm(diffs, axis=1)
    # First-shell neighbors are at distance == 1/phi (the 600-cell edge length)
    tol = 1e-9
    neighbors = np.where(np.abs(dists - target_edge_length) < tol)[0]
    return neighbors

def main():
    print("="*72)
    print("F.1 Sub-Question Phase 1 verification — DI-bit current at host")
    print("="*72)
    print(f"\nphi = {PHI:.15f}")
    print(f"600-cell edge length = 1/phi = {1.0/PHI:.15f}")
    print(f"Expected hat_u . hat_n = -1/(2 phi) = {-1.0/(2.0*PHI):.15f}")
    print(f"Expected sum hat_u = -(6/phi) hat_n; magnitude = {6.0/PHI:.15f}")
    print(f"Expected sum (hat_u.hat_n) hat_u = (3/phi^2) hat_n; magnitude = {3.0/(PHI*PHI):.15f}")

    # Generate 600-cell
    print("\n--- Step 1: Construct 600-cell ---")
    verts = gen_600cell_vertices()
    print(f"Generated {verts.shape[0]} vertices, all at unit distance from origin")

    # Pick host vertex — use vertex (1, 0, 0, 0)
    host_idx = None
    for i, v in enumerate(verts):
        if np.allclose(v, [1.0, 0.0, 0.0, 0.0]):
            host_idx = i
            break
    assert host_idx is not None
    v_host = verts[host_idx]
    n_hat = v_host / np.linalg.norm(v_host)  # = v_host since |v_host| = 1
    print(f"\nHost vertex: index {host_idx}, position {v_host}")
    print(f"n_hat = {n_hat}")

    # Find first-shell
    print("\n--- Step 2: Find first-shell neighbors ---")
    neighbors = find_first_shell(verts, host_idx, target_edge_length=1.0/PHI)
    print(f"First-shell count: {len(neighbors)} (expected: 12)")
    assert len(neighbors) == 12, f"Expected 12 first-shell neighbors, got {len(neighbors)}"

    # Compute unit edge vectors hat_u_i from host to neighbor i
    print("\n--- Step 3: Compute unit edge vectors hat_u_i ---")
    edge_vecs = verts[neighbors] - v_host
    edge_norms = np.linalg.norm(edge_vecs, axis=1)
    print(f"Edge length range: [{edge_norms.min():.15f}, {edge_norms.max():.15f}]")
    assert np.allclose(edge_norms, 1.0/PHI), "Edge lengths not all = 1/phi"
    u_hats = edge_vecs / edge_norms[:, None]

    # Verification 1: hat_u_i . hat_n = -1/(2 phi) for all 12
    print("\n--- Verification 1: hat_u_i . hat_n uniform = -1/(2 phi) ---")
    proj = u_hats @ n_hat
    expected = -1.0/(2.0*PHI)
    print(f"  Projections range: [{proj.min():.15f}, {proj.max():.15f}]")
    print(f"  Expected:                {expected:.15f}")
    print(f"  Max deviation from expected: {np.max(np.abs(proj - expected)):.2e}")
    assert np.allclose(proj, expected, atol=1e-12), "Projection not uniform = -1/(2 phi)"
    print("  PASS")

    # Verification 2: sum hat_u_i = -(6/phi) hat_n
    print("\n--- Verification 2: sum_i hat_u_i = -(6/phi) hat_n ---")
    sum_u = u_hats.sum(axis=0)
    expected_sum = -(6.0/PHI) * n_hat
    print(f"  Computed sum: {sum_u}")
    print(f"  Expected:     {expected_sum}")
    print(f"  Difference magnitude: {np.linalg.norm(sum_u - expected_sum):.2e}")
    assert np.allclose(sum_u, expected_sum, atol=1e-12), "Sum hat_u != -(6/phi) hat_n"
    # Also check orthogonal component is zero
    sum_u_perp = sum_u - (sum_u @ n_hat) * n_hat
    print(f"  Orthogonal component magnitude: {np.linalg.norm(sum_u_perp):.2e}")
    print("  PASS")

    # Verification 3: sum (hat_u_i . hat_n) hat_u_i = (3/phi^2) hat_n
    print("\n--- Verification 3: sum_i (hat_u_i.hat_n) hat_u_i = (3/phi^2) hat_n ---")
    weighted = (proj[:, None] * u_hats).sum(axis=0)
    expected_weighted = (3.0/(PHI*PHI)) * n_hat
    print(f"  Computed: {weighted}")
    print(f"  Expected: {expected_weighted}")
    print(f"  Difference magnitude: {np.linalg.norm(weighted - expected_weighted):.2e}")
    assert np.allclose(weighted, expected_weighted, atol=1e-12), "Weighted sum mismatch"
    print("  PASS")

    # Verification 4: Net DI-bit current at first order in delta
    print("\n--- Verification 4: j_DI_net = (6 r_0 delta / phi^2) hat_n ---")
    r_0 = 1.0  # arbitrary
    test_deltas = [0.0, 0.1, PHI**(-3), 0.5, -0.2]  # include Case A.1 unification value
    print(f"  r_0 = {r_0} (arbitrary normalization)")
    for delta in test_deltas:
        r_plus = r_0 * (1.0 + delta * proj)            # outgoing rates
        r_minus = r_0 * (1.0 - delta * proj)            # incoming rates (uses -hat_u . n)
        j_DI = ((r_plus - r_minus)[:, None] * u_hats).sum(axis=0)
        j_DI_analytic = (6.0 * r_0 * delta / (PHI*PHI)) * n_hat
        diff = np.linalg.norm(j_DI - j_DI_analytic)
        # Check magnitude and direction
        if delta != 0:
            j_norm = np.linalg.norm(j_DI)
            j_direction = j_DI / j_norm if j_norm > 0 else np.zeros(4)
            sign_along_n = np.sign(j_DI @ n_hat)
            print(f"  delta = {delta:+.6f}: j_DI_numerical = {j_DI}")
            print(f"                  j_DI_analytic  = {j_DI_analytic}")
            print(f"                  diff magnitude = {diff:.2e}")
            print(f"                  sign along hat_n = {sign_along_n:+.0f}, magnitude = {j_norm:.6f}")
        else:
            print(f"  delta = {delta:+.6f}: j_DI = {j_DI} (must be exactly 0)")
        assert np.allclose(j_DI, j_DI_analytic, atol=1e-12), f"Current mismatch at delta={delta}"
    print("  PASS at all test delta values")

    # Numerical value at Case A.1 unification delta = chi = phi^(-3)
    print("\n--- Phase 1 result at Case A.1 (delta = chi = phi^-3) ---")
    delta_A1 = PHI**(-3)
    j_A1 = (6.0 * r_0 * delta_A1 / (PHI*PHI))
    print(f"  delta_A.1 = phi^-3 = {delta_A1:.15f} ~ {delta_A1:.6f}")
    print(f"  |j_DI_net| / r_0 = 6 * phi^-5 = {6.0 * PHI**(-5):.6f}")
    print(f"  Direction: +hat_n (substrate primitive direction)")

    print("\n" + "="*72)
    print("ALL VERIFICATIONS PASSED.")
    print("Phase 1 falsifier check: local-I_h-preservation does NOT force j_DI = 0.")
    print("Mechanism A's sub-step (i) closes positively.")
    print("="*72)

if __name__ == "__main__":
    main()
