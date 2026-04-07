import numpy as np

# ============================================================
# Load the base 600-cell adjacency
# ============================================================
base_edges = np.loadtxt("nb02_SM8_600cell_edgelist.txt", dtype=int)
num_vertices_base = 120

print("Loaded base 600-cell with", num_vertices_base, "vertices and", len(base_edges), "edges.")

# ============================================================
# Tiny 1-ring surrogate parameters
# ============================================================
# 1 central cell + 6 neighbors
NUM_NEIGHBORS = 6
TOTAL_CELLS = 1 + NUM_NEIGHBORS

# ============================================================
# Build the graph
# ============================================================
all_edges = []

# 1. Internal edges for each cell
for k in range(TOTAL_CELLS):
    offset = k * num_vertices_base
    for u, v in base_edges:
        all_edges.append((u + offset, v + offset))

# 2. Connect each neighbor cell to the central cell
# Simple deterministic mapping: vertex i in neighbor k connects to vertex i in central cell
for k in range(1, TOTAL_CELLS):
    offset_center = 0
    offset_neighbor = k * num_vertices_base
    for i in range(num_vertices_base):
        all_edges.append((offset_center + i, offset_neighbor + i))

# Convert to array
all_edges = np.array(all_edges, dtype=int)

# ============================================================
# Stats
# ============================================================
num_vertices_total = TOTAL_CELLS * num_vertices_base
print("Total vertices:", num_vertices_total)
print("Total edges:", len(all_edges))

deg = np.zeros(num_vertices_total, dtype=int)
for u, v in all_edges:
    deg[u] += 1
    deg[v] += 1

print("Degree stats: min", deg.min(), "max", deg.max(), "mean", deg.mean())

# ============================================================
# Save edge list
# ============================================================
np.savetxt("nb02_SM8_tiny1ring_edgelist.txt", all_edges, fmt="%d")
print("Wrote nb02_SM8_tiny1ring_edgelist.txt")
