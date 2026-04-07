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
# Type 2: 16 points (±1/2, ±1/2, ±1/2, ±1/2) with even number of minus signs
# ===================================================================
for signs in itertools.product([-1, 1], repeat=4):
    v = np.array(signs, dtype=float) * 0.5
    if sum(s < 0 for s in signs) % 2 == 0:
        vertices.append(v)

# ===================================================================
# Type 3: 96 golden-ratio points — EVEN permutations only
# ===================================================================
for signs in itertools.product([-1., 1.], repeat=3):
    a = signs[0] * 0.5
    b = signs[1] * (phi / 2)
    c = signs[2] * (1 / (2 * phi))
    items = [0., a, b, c]                     # the four values (0 and the three signed ones)

    for p in itertools.permutations(range(4)):   # p = permutation of indices 0,1,2,3
        # Compute inversion count to test parity of the permutation
        inv_count = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]:
                    inv_count += 1
        if inv_count % 2 == 0:                    # even permutation only
            v = np.zeros(4)
            v[p[0]] = items[0]
            v[p[1]] = items[1]
            v[p[2]] = items[2]
            v[p[3]] = items[3]
            vertices.append(v)

# Convert to array and remove any floating-point duplicates
vertices = np.array(vertices)
vertices = np.unique(np.round(vertices, decimals=10), axis=0)

print("Total unique vertices:", len(vertices))
print("All norms ≈ 1?", np.allclose(np.linalg.norm(vertices, axis=1), 1.0, atol=1e-8))

# Save
np.savetxt("600cell_vertices.txt", vertices, fmt="%.10f")
