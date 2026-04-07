import numpy as np
import itertools

phi = (1 + np.sqrt(5)) / 2

vertices = []

# H4 root system: 120 roots
# Type 1: 8 roots of the form (±1, 0, 0, 0)
for i in range(4):
    for s in [+1, -1]:
        v = [0, 0, 0, 0]
        v[i] = s
        vertices.append(v)

# Type 2: 16 roots of the form (±1/2, ±1/2, ±1/2, ±1/2)
# with an even number of minus signs
for signs in itertools.product([+0.5, -0.5], repeat=4):
    if sum(s < 0 for s in signs) % 2 == 0:
        vertices.append(list(signs))

# Type 3: 96 roots of the form (0, ±1/2, ±phi/2, ±1/(2phi))
# with all permutations
vals = [0, 0.5, phi/2, 1/(2*phi)]

for signs in itertools.product([+1, -1], repeat=3):
    signed = [0, signs[0]*0.5, signs[1]*(phi/2), signs[2]*(1/(2*phi))]
    for perm in set(itertools.permutations(signed)):
        vertices.append(list(perm))

# Convert to array and remove duplicates
vertices = np.array(vertices)
vertices = np.unique(vertices, axis=0)

print("Total vertices:", len(vertices))
np.savetxt("600cell_vertices.txt", vertices)
