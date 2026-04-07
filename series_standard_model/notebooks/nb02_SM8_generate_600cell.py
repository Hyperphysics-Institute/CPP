import itertools
import numpy as np

phi = (1 + 5**0.5) / 2
invphi = 1 / phi

vertices = []

# Group A: 8 vertices (±1, 0, 0, 0)
for i in range(4):
    for s in [+1, -1]:
        v = [0, 0, 0, 0]
        v[i] = s
        vertices.append(v)

# Group B: 16 vertices (±1/2, ±1/2, ±1/2, ±1/2) with even number of minus signs
for signs in itertools.product([+0.5, -0.5], repeat=4):
    if sum(s < 0 for s in signs) % 2 == 0:
        vertices.append(list(signs))

# Group C: 96 vertices
base = [0, invphi, phi, 1]

# Even permutations only
def even_permutations(lst):
    perms = set(itertools.permutations(lst))
    even = []
    for p in perms:
        # Compute permutation parity
        inv = 0
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] > p[j]:
                    inv += 1
        if inv % 2 == 0:
            even.append(p)
    return even

for signs in itertools.product([+1, -1], repeat=3):
    signed = [0, signs[0]*invphi, signs[1]*phi, signs[2]*1]
    for perm in even_permutations(signed):
        vertices.append(list(perm))

vertices = np.array(vertices)
print("Total vertices:", len(vertices))

np.savetxt("600cell_vertices.txt", vertices)
