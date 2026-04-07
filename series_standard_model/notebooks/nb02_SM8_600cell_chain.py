import numpy as np

# Parameters
M = 50  # number of 600-cell copies in the chain; you can adjust

# Load base 600-cell edge list
base_edges = np.loadtxt("nb2_SM8_600cell_edgelist.txt", dtype=int)
num_vertices_base = 120

print("Loaded base 600-cell with", num_vertices_base, "vertices and", len(base_edges), "edges.")

all_edges = []

# 1. Internal edges for each copy
for k in range(M):
    offset = k * num_vertices_base
    for u, v in base_edges:
        all_edges.append((u + offset, v + offset))

# 2. Bridge edges between consecutive copies
# Simple scheme: connect vertex i in copy k to vertex i in copy k+1
for k in range(M - 1):
    offset_k = k * num_vertices_base
    offset_next = (k + 1) * num_vertices_base
    for i in range(num_vertices_base):
        all_edges.append((offset_k + i, offset_next + i))

all_edges = np.array(all_edges, dtype=int)

num_vertices_total = M * num_vertices_base
print("Total vertices:", num_vertices_total)
print("Total edges:", len(all_edges))

# Degree sanity check
deg = np.zeros(num_vertices_total, dtype=int)
for u, v in all_edges:
    deg[u] += 1
    deg[v] += 1

print("Degree stats: min", deg.min(), "max", deg.max(), "mean", deg.mean())

# Save edge list
np.savetxt("nb02_SM8_600cell_chain_edgelist.txt", all_edges, fmt="%d")
print("Wrote nb02_SM8_600cell_chain_edgelist.txt")
