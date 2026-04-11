import numpy as np

# Load the 120 vertices (4D coordinates)
vertices = np.loadtxt("nb02_SM8_600cell_vertices.txt")
N = vertices.shape[0]
print("Loaded vertices:", N)

# Compute all pairwise distances and detect edges
# The 600-cell is a regular polytope: all edges have the same length.
# We estimate the edge length from the first nonzero distance and use a tolerance.

edges = []
tol = 1e-6

# Find a reference edge length
ref_len = None
for i in range(N):
    for j in range(i+1, N):
        d = np.linalg.norm(vertices[i] - vertices[j])
        if d > tol:
            ref_len = d
            break
    if ref_len is not None:
        break

if ref_len is None:
    raise RuntimeError("Could not find a reference edge length.")

print("Reference edge length ~", ref_len)

# Collect all pairs whose distance matches the edge length within tolerance
for i in range(N):
    for j in range(i+1, N):
        d = np.linalg.norm(vertices[i] - vertices[j])
        if abs(d - ref_len) < tol:
            edges.append((i, j))

edges = np.array(edges, dtype=int)
print("Number of edges:", len(edges))

# Optional sanity check: degree distribution
deg = np.zeros(N, dtype=int)
for u, v in edges:
    deg[u] += 1
    deg[v] += 1

print("Degree stats: min", deg.min(), "max", deg.max(), "mean", deg.mean())

# Save edge list
np.savetxt("nb02_SM8_600cell_edgelist.txt", edges, fmt="%d")
print("Wrote nb02_SM8_600cell_edgelist.txt")
