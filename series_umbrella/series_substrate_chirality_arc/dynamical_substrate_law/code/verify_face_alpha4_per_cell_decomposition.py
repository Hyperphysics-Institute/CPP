#!/usr/bin/env python3
"""
PER-CELL DECOMPOSITION extension of `verify_face_alpha4_closure.py`.

Generates the per-cell breakdown for the ChatGPT re-review packet
(Patch 0626 follow-up; targets §3.1/§3.2/§3.3 PARTIAL → CONFIRMED upgrade).

Partitions the 20,736 face-aligned k=4 paths from `v_host` by the shell-tuple
(s_v'', s_v''', s_v'''') -- shells of the 2nd, 3rd, and 4th path vertices --
and reports the per-cell:
  - path count
  - per-cell numerical sum at mpmath dps=60
  - PSLQ identification in basis {1, phi, sqrt(3), sqrt(3)*phi}

Cell sums for both `alpha_4^(rho)` and `alpha_4^(ax)` should add to:
    alpha_4^(rho) = 641/2 - 180 phi      ~ +29.254
    alpha_4^(ax)  = (401 - 167 phi)/3    ~ +43.596
with the sqrt(3) and sqrt(3)*phi coefficients summing to exactly zero across
cells (THEO-DSL-11 Theorem 1 cancellation mechanism at even k=4).

Individual cells may carry non-zero sqrt(3) components; the cancellation
across cells demonstrates the parity mechanism doing real work.
"""
import itertools, time, json
from collections import defaultdict
import mpmath as mp

mp.mp.dps = 60

phi = (1 + mp.sqrt(5)) / 2
SQRT3 = mp.sqrt(3)

# ---------------------------------------------------------- 600-cell build
def build_600cell_mp():
    V = []
    for i in range(4):
        for s in (mp.mpf(1), mp.mpf(-1)):
            v = [mp.mpf(0)] * 4; v[i] = s; V.append(v)
    for sg in itertools.product((mp.mpf("0.5"), mp.mpf("-0.5")), repeat=4):
        V.append(list(sg))
    base = [phi / 2, mp.mpf("0.5"), 1 / (2 * phi), mp.mpf(0)]
    def even(p):
        c = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]: c += 1
        return c % 2 == 0
    for perm in itertools.permutations(range(4)):
        if not even(perm): continue
        for sg in itertools.product((mp.mpf(1), mp.mpf(-1)), repeat=4):
            V.append([base[perm[k]] * sg[k] for k in range(4)])
    U = []
    for v in V:
        if not any(max(abs(v[k] - u[k]) for k in range(4)) < mp.mpf("1e-40") for u in U):
            U.append(v)
    return U

print(f"Building 600-cell at mpmath dps={mp.mp.dps}...")
UU = build_600cell_mp()
assert len(UU) == 120, f"expected 120 vertices, got {len(UU)}"

def dot(a, b): return sum(a[k] * b[k] for k in range(4))
def vsub(a, b): return [a[k] - b[k] for k in range(4)]
def vnorm(a): return mp.sqrt(dot(a, a))
def edge_dir(a_idx, b_idx):
    e = vsub(UU[b_idx], UU[a_idx])
    s = vnorm(e)
    return [x / s for x in e]

# Verify norms
for k in range(120):
    assert abs(vnorm(UU[k]) - 1) < mp.mpf("1e-40")
print(f"  All 120 vertices verified unit norm at dps={mp.mp.dps}.")

# Neighbours
target_dot = phi / 2
nbr = {i: [j for j in range(120) if j != i and abs(dot(UU[i], UU[j]) - target_dot) < mp.mpf("1e-40")] for i in range(120)}
for i in range(120):
    assert len(nbr[i]) == 12
print(f"  All 120 vertices have exactly 12 neighbours at <u,v>=phi/2.")

# Host + face setup (canonical: v_host = vertex 0, first neighbour-pair forming a face)
HOST = 0
vh = UU[HOST]
S1 = nbr[HOST]
assert len(S1) == 12

# Pick canonical face (first triangular face at S1)
ui_idx = S1[0]
uj_idx = None
for c in S1[1:]:
    if abs(dot(UU[ui_idx], UU[c]) - target_dot) < mp.mpf("1e-40"):
        uj_idx = c
        break
assert uj_idx is not None
ui = UU[ui_idx]; uj = UU[uj_idx]

# Centroid normal
sum3 = [vh[k] + ui[k] + uj[k] for k in range(4)]
sum3_norm = vnorm(sum3)
expected_centroid_norm = phi * SQRT3
assert abs(sum3_norm - expected_centroid_norm) < mp.mpf("1e-40")
print(f"  |v_h + u_i + u_j| = phi*sqrt(3) verified at dps={mp.mp.dps} (residual < 1e-40).")
nFperp = [sum3[k] / sum3_norm for k in range(4)]

# n_rho = v_h (unit norm)
nrho = vh
# n_ax = u_i + u_j - phi*v_h
nax = [ui[k] + uj[k] - phi * vh[k] for k in range(4)]
# |n_ax|^2 = 2 + phi - phi^2 = 2 + phi - (phi + 1) = 1
nax_norm = vnorm(nax)
assert abs(nax_norm - 1) < mp.mpf("1e-40")
print(f"  |n_ax| = 1 verified at dps={mp.mp.dps}.")

# ---------------------------------------------------------- Shell classification
# 9 shells: <u, v_host> values
shell_values = [mp.mpf(1), phi / 2, mp.mpf("0.5"), 1 / (2 * phi), mp.mpf(0),
                -1 / (2 * phi), mp.mpf("-0.5"), -phi / 2, mp.mpf(-1)]
shell_labels = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']

def shell_of(v_idx):
    d = dot(UU[v_idx], vh)
    for k, sv in enumerate(shell_values):
        if abs(d - sv) < mp.mpf("1e-40"):
            return shell_labels[k]
    raise ValueError(f"unknown shell for vertex {v_idx}: <v,vh> = {mp.nstr(d, 40)}")

# Verify shell occupancy: B0=1, B1=12, ..., B8=1 (icosahedral shells of 600-cell)
shell_occ = defaultdict(int)
for i in range(120):
    shell_occ[shell_of(i)] += 1
print(f"  Shell occupancies: {dict(shell_occ)}")
assert shell_occ == {'B0': 1, 'B1': 12, 'B2': 20, 'B3': 12, 'B4': 30, 'B5': 12, 'B6': 20, 'B7': 12, 'B8': 1}

# ---------------------------------------------------------- Per-cell k=4 assembly
print(f"\nRunning k=4 face-aligned assembly with per-cell decomposition at dps={mp.mp.dps}...")
print(f"  Partition: (s_v'', s_v''', s_v'''')   (s_v' = B1 forced)")

cell_paths = defaultdict(int)
cell_sum_rho = defaultdict(lambda: mp.mpf(0))
cell_sum_ax = defaultdict(lambda: mp.mpf(0))

total_paths = 0
t0 = time.time()

for u1 in S1:
    e1 = edge_dir(HOST, u1)
    w1 = dot(e1, nFperp)
    e1_rho = dot(e1, nrho)
    e1_ax = dot(e1, nax)
    for u2 in nbr[u1]:
        e2 = edge_dir(u1, u2)
        w2 = dot(e2, nFperp)
        s2 = shell_of(u2)
        for u3 in nbr[u2]:
            e3 = edge_dir(u2, u3)
            w3 = dot(e3, nFperp)
            s3 = shell_of(u3)
            for u4 in nbr[u3]:
                e4 = edge_dir(u3, u4)
                w4 = dot(e4, nFperp)
                s4 = shell_of(u4)

                P = w1 * w2 * w3 * w4
                contrib_rho = P * e1_rho
                contrib_ax = P * e1_ax

                cell = (s2, s3, s4)
                cell_paths[cell] += 1
                cell_sum_rho[cell] += contrib_rho
                cell_sum_ax[cell] += contrib_ax
                total_paths += 1

elapsed = time.time() - t0
print(f"  Assembly complete in {elapsed:.1f}s")
print(f"  Total paths enumerated: {total_paths}")
assert total_paths == 20736, f"expected 20736 paths, got {total_paths}"
print(f"  Non-empty cells: {len(cell_paths)}")

# ---------------------------------------------------------- PSLQ per cell
print(f"\nRunning PSLQ identification per cell in basis {{1, phi, sqrt(3), sqrt(3)*phi}}...")
basis = [mp.mpf(1), phi, SQRT3, SQRT3 * phi]

results = []
for cell in sorted(cell_paths.keys()):
    n = cell_paths[cell]
    s_rho = cell_sum_rho[cell]
    s_ax = cell_sum_ax[cell]

    # PSLQ for rho component
    try:
        if abs(s_rho) < mp.mpf("1e-50"):
            rel_rho = "≈0"
        else:
            rel_rho = mp.pslq([s_rho] + basis, tol=mp.mpf("1e-40"), maxcoeff=10**10)
    except Exception as e:
        rel_rho = f"PSLQ_FAIL ({e})"

    # PSLQ for ax component
    try:
        if abs(s_ax) < mp.mpf("1e-50"):
            rel_ax = "≈0"
        else:
            rel_ax = mp.pslq([s_ax] + basis, tol=mp.mpf("1e-40"), maxcoeff=10**10)
    except Exception as e:
        rel_ax = f"PSLQ_FAIL ({e})"

    results.append({
        'cell': cell,
        'n_paths': n,
        'sum_rho': mp.nstr(s_rho, 40),
        'sum_ax': mp.nstr(s_ax, 40),
        'rel_rho': str(rel_rho),
        'rel_ax': str(rel_ax),
    })

# ---------------------------------------------------------- Output
print("\n" + "=" * 76)
print("PER-CELL DECOMPOSITION TABLE")
print("=" * 76)
print(f"{'cell':<22} {'n_paths':<10} {'PSLQ on sum_rho':<35} {'PSLQ on sum_ax'}")
print("-" * 105)

total_n = 0
for r in results:
    cell_str = f"({r['cell'][0]},{r['cell'][1]},{r['cell'][2]})"
    print(f"{cell_str:<22} {r['n_paths']:<10} {r['rel_rho']:<35} {r['rel_ax']}")
    total_n += r['n_paths']

print("-" * 105)
print(f"{'TOTAL':<22} {total_n:<10}")

# Sum-of-cells check
total_rho = sum(cell_sum_rho.values())
total_ax = sum(cell_sum_ax.values())
target_rho = mp.mpf(641) / 2 - 180 * phi
target_ax = (401 - 167 * phi) / 3

print(f"\n{'CLOSED FORM VERIFICATION'}")
print(f"{'='*76}")
print(f"  Sum over cells -- alpha_4^(rho) = {mp.nstr(total_rho, 40)}")
print(f"  Target       -- 641/2 - 180*phi = {mp.nstr(target_rho, 40)}")
print(f"  Residual                        = {mp.nstr(total_rho - target_rho, 20)}")
print()
print(f"  Sum over cells -- alpha_4^(ax)  = {mp.nstr(total_ax, 40)}")
print(f"  Target       -- (401-167*phi)/3 = {mp.nstr(target_ax, 40)}")
print(f"  Residual                        = {mp.nstr(total_ax - target_ax, 20)}")

# PSLQ on full sum (sanity check)
full_rel_rho = mp.pslq([total_rho] + basis, tol=mp.mpf("1e-40"), maxcoeff=10**6)
full_rel_ax = mp.pslq([total_ax] + basis, tol=mp.mpf("1e-40"), maxcoeff=10**6)
print(f"\n  PSLQ on full alpha_4^(rho): {full_rel_rho}")
print(f"  PSLQ on full alpha_4^(ax) : {full_rel_ax}")
print(f"  Expected for rho: [-2, 641, -360, 0, 0]")
print(f"  Expected for ax : [-3, 401, -167, 0, 0]")

# Save structured output to JSON for the markdown packet
output_data = {
    'dps': mp.mp.dps,
    'total_paths': total_paths,
    'non_empty_cells': len(results),
    'cells': results,
    'total_sum_rho': mp.nstr(total_rho, 40),
    'total_sum_ax': mp.nstr(total_ax, 40),
    'target_rho': mp.nstr(target_rho, 40),
    'target_ax': mp.nstr(target_ax, 40),
    'residual_rho': mp.nstr(total_rho - target_rho, 20),
    'residual_ax': mp.nstr(total_ax - target_ax, 20),
    'full_rel_rho': str(full_rel_rho),
    'full_rel_ax': str(full_rel_ax),
}
with open('/tmp/per_cell_decomposition.json', 'w') as f:
    json.dump(output_data, f, indent=2, default=str)
print(f"\nResults saved to /tmp/per_cell_decomposition.json")
