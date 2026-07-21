"""Patch 2665 — FA-SEA-GREEN scoping: instrument demonstration ONLY.
Builds the 600-cell vertex set (icosian construction, session-127 lineage),
verifies |V|=120, |E|=720, degree z=12 (SS-2/SF-4 registered coordination),
and confirms the graph Laplacian spectrum is computable (smallest nonzero
eigenvalue reported dimensionless). DELIBERATELY OMITTED: any Green-function
decay length, any gap parameter, any kernel comparison — fork-neutrality
guard: the machinery is demonstrated without pre-seeing either FA-C3
candidate. All outputs dimensionless, instrument-level, quarantined."""
import numpy as np, itertools
phi = (1 + 5**0.5) / 2
V = []
# 8 unit-quaternion axis vertices + 16 half-integer vertices (24 Hurwitz units)
for i in range(4):
    for s in (1, -1):
        v = [0.0]*4; v[i] = s; V.append(v)
V += [[a/2, b/2, c/2, d/2] for a in (1,-1) for b in (1,-1) for c in (1,-1) for d in (1,-1)]
# 96 even permutations of (±phi, ±1, ±1/phi, 0)/2
base = [phi/2, 0.5, 1/(2*phi), 0.0]
def even_perms():
    seen = set()
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i+1,4) if p[i] > p[j])
        if inv % 2 == 0 and p not in seen:
            seen.add(p); yield p
for p in even_perms():
    for s0 in (1,-1):
        for s1 in (1,-1):
            for s2 in (1,-1):
                v = [0.0]*4
                v[p[0]] = s0*base[0]; v[p[1]] = s1*base[1]; v[p[2]] = s2*base[2]; v[p[3]] = 0.0
                V.append(tuple(round(x,10) for x in v))
V = np.array(sorted(set(tuple(round(x,10) for x in v) for v in V)))
assert V.shape[0] == 120, f"vertex count {V.shape[0]} != 120"
r = np.linalg.norm(V, axis=1)
assert np.allclose(r, 1.0), "not unit circumradius"
D = np.linalg.norm(V[:,None,:] - V[None,:,:], axis=2)
edge_len = 1/phi  # registered: edge = circumradius/phi (SS-2)
A = (np.abs(D - edge_len) < 1e-6).astype(int)
deg = A.sum(1)
n_edges = A.sum()//2
assert np.all(deg == 12), f"degree set {sorted(set(deg))} != {{12}}"
assert n_edges == 720, f"edge count {n_edges} != 720"
L = np.diag(deg) - A
ev = np.linalg.eigvalsh(L)
assert abs(ev[0]) < 1e-9 and ev[1] > 1e-9, "Laplacian spectrum malformed"
print(f"PASS: |V|=120, |E|={n_edges}, degree z=12 uniform (matches SS-2/SF-4)")
print(f"PASS: edge length = circumradius/phi = {edge_len:.6f} (dimensionless)")
print(f"PASS: graph Laplacian computable; lambda_1 = {ev[1]:.6f} (dimensionless, instrument-level)")
print("GUARD: no gap parameter, no Green function, no kernel comparison computed — fork blind intact")
