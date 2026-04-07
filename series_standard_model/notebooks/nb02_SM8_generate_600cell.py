import numpy as np
import itertools

phi = (1 + np.sqrt(5)) / 2

vertices = []

# ===================================================================
# Type 1: 8 axis-aligned points (±1, 0, 0, 0) and permutations
# ===================================================================
for i in range(4):
    for s in [-1, 1]:
        v = np.zeros(4)
        v[i] = s
        vertices.append(v)

# ===================================================================
# Type 2: ALL 16 points (±1/2, ±1/2, ±1/2, ±1/2)
# ===================================================================
for signs in itertools.product([-1, 1], repeat=4):
    v = np.array(signs, dtype=float) * 0.5
    vertices.append(v)

# ===================================================================
# Type 3: 96 golden-ratio points — EVEN permutations only
# ===================================================================
vals_base = [0.0, 0.5, phi/2, 1/(2*phi)]
sign_combos = list(itertools.product([-1., 1.], repeat=3))

# Pre-compute the 12 even permutations of indices (0,1,2,3)
even_perms = []
for p in itertools.permutations(range(4)):
    inv_count = sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j])
    if inv_count % 2 == 0:
        even_perms.append(p)

for signs in sign_combos:
    a = signs[0] * vals_base[1]
    b = signs[1] * vals_base[2]
    c = signs[2] * vals_base[3]
    items = [vals_base[0], a, b, c]
    for p in even_perms:
        v = np.zeros(4)
        for idx_pos, item_idx in enumerate(p):
            v[item_idx] = items[idx_pos]
        vertices.append(v)

# Convert, remove any floating-point duplicates, and verify
vertices = np.array(vertices)
vertices = np.unique(np.round(vertices, decimals=12), axis=0)

print("Total unique vertices:", len(vertices))
print("All norms ≈ 1?", np.allclose(np.linalg.norm(vertices, axis=1), 1.0, atol=1e-8))

# Optional: save to file
np.savetxt("nb2_SM8_600cell_vertices.txt", vertices, fmt="%.12f")
