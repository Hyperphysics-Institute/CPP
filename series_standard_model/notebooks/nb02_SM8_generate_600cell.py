import itertools
import numpy as np

phi = (1 + 5**0.5) / 2
invphi = 1 / phi

vertices = []

# Group A: (±1, 0, 0, 0)
for i in range(4):
    for s in [+1, -1]:
        v = [0, 0, 0, 0]
        v[i] = s
        vertices.append(v)

# Group B: (±1/2, ±1/2, ±1/2, ±1/2) with even number of minus signs
for signs in itertools.product([+0.5, -0.5], repeat=4):
    if sum(s < 0 for s in signs) % 2 == 0:
        vertices.append(list(signs))

# Group C: even permutations of (0, ±invphi, ±phi, ±1)
base = [0, invphi, phi, 1]
for signs in itertools.product([+1, -1], repeat=3):
    signed = [0, signs[0]*invphi, signs[1]*phi, signs[2]*1]
    for perm in set(itertools.permutations(signed)):
        vertices.append(list(perm))

vertices = np.array(vertices)
print("Total vertices:", len(vertices))

np.savetxt("nb02_SM8_600cell_vertices.txt", vertices)
