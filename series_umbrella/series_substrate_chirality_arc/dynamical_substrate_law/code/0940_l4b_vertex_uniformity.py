#!/usr/bin/env python3
"""
0940 — L4-B of OPEN-FP-F1-2: the vertex-uniformity of Mechanism A derived from
A11 (600-cell substrate), not assumed.

Claim. In MA.1, r(ê) = r0(1 + δ ê·n̂), the parameters r0 and δ carry no vertex
label: r0(v) ≡ r0 and δ(v) ≡ δ for every substrate vertex v. In MA.2 the
first-shell current construction has the same form at every v. All vertex
dependence of the OUTPUT enters through the explicit argument ê·n̂.

The argument has two halves and the second is the one that does work:

  (a) The bare substrate is vertex-transitive: Aut(600-cell) acts transitively
      on the 120 vertices, so no function of a vertex built from substrate
      structure alone can distinguish one vertex from another. Any v-dependence
      of r0 or δ would be such a function. (T1–T3)

  (b) Fixing n̂ breaks that transitivity — so (a) alone is not enough, and this
      is where a naive argument fails. Under vertex-aligned Reading C the
      residual group is Stab(n̂) ≅ H3 = I_h (order 120), and its orbits on the
      120 vertices are the nine n̂-shells. So the pair (substrate, n̂) DOES
      distinguish vertices — but only through the single invariant v·n̂, which
      is exactly the quantity MA.1 already carries explicitly. A residual
      vertex-dependence of r0 or δ would have to be a Stab(n̂)-invariant
      function of v that is NOT a function of v·n̂ alone; T5 shows no such
      function exists, because Stab(n̂) acts transitively on each shell.
      (T4–T6)

Together: the only vertex-distinguishing datum available to the rate law is
v·n̂, which MA.1 uses explicitly; therefore r0 and δ are constants. That is
vertex-uniformity, derived from A11 + the single primitive n̂, with no appeal
to Mechanism A itself.

Tests
  T1  the 600-cell: 120 vertices, every vertex has exactly 12 nearest
      neighbours at edge length 1/φ (the substrate of A11).
  T2  vertex-transitivity of the bare substrate: the isometry group acts with a
      single orbit on the 120 vertices (checked constructively — an isometry
      carrying v_host to each v is exhibited).
  T3  the stabiliser of a vertex has order 120 (= 14400/120), the local I_h of
      Reading C.
  T4  fixing n̂ = v_host, the 120 vertices fall into exactly 8 shells by the
      invariant v·n̂ ∈ {1, φ/2, 1/2, 1/(2φ), 0, −1/(2φ), −1/2, −φ/2, −1} —
      transitivity is broken.
  T5  Stab(n̂) acts TRANSITIVELY on each shell: so every Stab(n̂)-invariant
      function of a vertex is a function of v·n̂ alone. This is the step that
      forecloses a residual vertex label.
  T6  consequence, exhibited: two vertices in the same shell have first-shell
      environments carried into each other by an element of Stab(n̂), hence
      identical multisets of ê·n̂ over their first shells — the rate law's
      entire input. Two vertices in DIFFERENT shells need not, and do not.
  T7  the same statement for MA.2's construction: the first-shell edge-direction
      multiset {ê·n̂} is constant within a shell and the O(δ¹) current
      Σ ê (ê·n̂) is carried by the group element, so the construction's form is
      vertex-independent while its value tracks the shell.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9
res = []

def ok(name, cond, note=""):
    res.append(cond); print(f"{name} {'PASS' if cond else 'FAIL'}  {note}")

def vertices_600():
    V = []
    for s in itertools.product([1, -1], repeat=4):
        V.append(0.5 * np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI / 2, 0.5, 1 / (2 * PHI), 0.0]
    evens = [p for p in itertools.permutations(range(4))
             if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in evens:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4)
            vals = [s[0] * base[0], s[1] * base[1], s[2] * base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = vertices_600()
N = len(V)
edge = 1 / PHI
G = V @ V.T                      # Gram matrix: all the geometry there is

# ---- T1
nbr = [np.where(np.abs(G[i] - PHI / 2) < 1e-8)[0] for i in range(N)]
ok("T1", N == 120 and all(len(x) == 12 for x in nbr),
   f"{N} vertices, every vertex has {len(nbr[0])} first-shell neighbours at edge {edge:.4f}")

# ---- isometries as 4x4 orthogonal maps permuting V, built from an ordered frame
idx = [0]
for j in nbr[0]:
    A = np.array([V[i] for i in idx] + [V[j]])
    if np.linalg.matrix_rank(A, tol=1e-8) == len(idx) + 1:
        idx.append(int(j))
    if len(idx) == 4: break
assert len(idx) == 4
A = np.array([V[i] for i in idx])
Ainv = np.linalg.inv(A)
gram_ref = A @ A.T

def perm_of(M):
    Y = V @ M.T
    p = np.full(N, -1, dtype=int)
    for a, y in enumerate(Y):
        d = np.abs(V - y).max(axis=1)
        h = np.where(d < 1e-7)[0]
        if len(h) != 1: return None
        p[a] = h[0]
    return tuple(p)

def isometry_to(frame_idx):
    """orthogonal M with M V[idx[k]] = V[frame_idx[k]], or None"""
    B = np.array([V[i] for i in frame_idx])
    if not np.allclose(B @ B.T, gram_ref, atol=1e-7): return None
    M = (Ainv @ B).T
    if not np.allclose(M @ M.T, np.eye(4), atol=1e-7): return None
    return M

# ---- T2: transitivity of the bare substrate — exhibit an isometry v_host -> v
host = 0
n_hat = V[host].copy()
reached, witness = set(), {}
for target in range(N):
    # map the reference frame onto a frame based at `target` with the same Gram
    found = None
    for cand in itertools.permutations(nbr[target], 3):
        fr = [target] + list(cand)
        M = isometry_to(fr)
        if M is not None and perm_of(M) is not None:
            found = M; break
    if found is not None:
        reached.add(target); witness[target] = found
ok("T2", len(reached) == N,
   f"an isometry carrying v_host to v was exhibited for {len(reached)}/{N} vertices — one orbit, vertex-transitive")

# ---- T3: stabiliser order
stab = []
seen = set()
for cand in itertools.permutations(nbr[host], 3):
    M = isometry_to([host] + list(cand))
    if M is None: continue
    p = perm_of(M)
    if p is not None and p[host] == host and p not in seen:
        seen.add(p); stab.append((p, M))
ok("T3", len(stab) == 120, f"|Stab(v_host)| = {len(stab)} = 14400/120 — the local I_h of Reading C")

# ---- T4: n̂ breaks transitivity into shells
proj = V @ n_hat
shell_vals = sorted({round(x, 9) for x in proj}, reverse=True)
shells = {sv: np.where(np.abs(proj - sv) < 1e-8)[0] for sv in shell_vals}
ok("T4", len(shell_vals) == 9 and len(shells[shell_vals[0]]) == 1,
   f"n̂ splits 120 vertices into {len(shell_vals)} shells by v·n̂ = "
   + ", ".join(f"{s:+.4f}({len(shells[s])})" for s in shell_vals))

# ---- T5: Stab(n̂) = Stab(v_host) acts transitively on each shell
trans = {}
for sv, members in shells.items():
    m0 = members[0]
    orb = {p[m0] for p, _ in stab}
    trans[sv] = (orb == set(members.tolist()))
ok("T5", all(trans.values()),
   "Stab(n̂) is transitive on every shell ⇒ every Stab(n̂)-invariant function of a vertex "
   "is a function of v·n̂ alone; no residual vertex label exists")

# ---- T6: same-shell vertices have identical first-shell ê·n̂ multisets; cross-shell differ
def edge_proj_multiset(v_i):
    out = sorted(round(float((V[j] - V[v_i]) @ n_hat / edge), 9) for j in nbr[v_i])
    return tuple(out)

same_ok, diff_seen = True, set()
for sv, members in shells.items():
    sigs = {edge_proj_multiset(m) for m in members}
    if len(sigs) != 1: same_ok = False
    diff_seen.add(next(iter(sigs)))
ok("T6", same_ok and len(diff_seen) == len(shells),
   f"first-shell ê·n̂ multiset is constant within each shell and distinct across all {len(shells)} shells")

# ---- T7: MA.2's O(δ¹) current form is carried by the group element
def J1(v_i):
    return sum(((V[j] - V[v_i]) / edge) * float((V[j] - V[v_i]) @ n_hat / edge) for j in nbr[v_i])

host_J = J1(host)
carried = True
for sv, members in shells.items():
    m0 = members[0]; J0 = J1(m0)
    for m in members:
        g = next((M for p, M in stab if p[m0] == m), None)
        if g is None: carried = False; break
        if not np.allclose(J1(m), g @ J0, atol=1e-7): carried = False; break
ok("T7", carried and np.linalg.norm(host_J) > TOL,
   "MA.2's first-shell sum Σ ê(ê·n̂) at any v equals the group image of its shell representative's — "
   "same construction, value tracking the shell only")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
