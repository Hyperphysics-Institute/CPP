import numpy as np
import itertools

phi = (1 + np.sqrt(5)) / 2
invphi = 1 / phi

vertices = []

# Group 1: 16 vertices of the form (±1, 0, 0, 0) and permutations
for i in range(4):
    for s in [+1, -1]:
        v = [0, 0, 0, 0]
        v[i] = s
        vertices.append(v)

# Group 2: 8 vertices of the form (±1/2, ±1/2, ±1/2, ±1/2) with even number of minus signs
for signs in itertools.product([+0.5, -0.5], repeat=4):
    if sum(s < 0 for s in signs) % 2 == 0:
        vertices.append(list(signs))

# Group 3: 96 vertices from permutations of (0, ±invphi, ±phi, ±1)
base = [0, invphi, phi, 1]

for signs in itertools.product([+1, -1], repeat=3):
    signed = [0, signs[0]*invphi, signs[1]*phi, signs[2]*1]
    for perm in set(itertools.permutations(signed)):
        vertices.append(list(perm))

# Convert to array and remove duplicates
vertices = np.array(vertices)
vertices = np.unique(vertices, axis=0)

print("Total vertices:", len(vertices))
np.savetxt("600cell_vertices.txt", vertices)
