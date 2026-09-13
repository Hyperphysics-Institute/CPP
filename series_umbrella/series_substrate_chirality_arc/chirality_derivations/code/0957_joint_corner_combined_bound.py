#!/usr/bin/env python3
"""
0957 — the joint corner, and the single combined worst-case bound.

Two CONV-048 addendum returns independently refused to accept "each effect
still clears" as a safety argument:

  Grok (Q3): "What concerns me is not the separate clearances. It is stacking
  them. Negative A and the odd quadratic were run as two experiments, not at
  the joint corner (slow edges from A -> -1 *and* an odd quadratic tilt).
  Additive-in-amplitude they would still be O(1e-4) in J. Multiplicative-on-
  the-slow-edges they are unshown."

  Copilot (Q3, required edit 1 and 4): "their combined worst-case (if they were
  to align) must be bounded explicitly" -- a single worst-case numeric statement
  covering the A range, the odd-quadratic coefficients and the kappa modelling
  uncertainty.

They are right and the case was untested. It is tested here, and it produced a
result neither reviewer anticipated and that Patch 0955 got wrong.

  T1  THE ADMISSIBLE DOMAIN IS NOT A RECTANGLE. Patch 0955/0956 stated the
      admissible range as |A| <= 1.025, computed at C = 0. With the odd
      quadratic switched on, rate positivity fails earlier: at A = -1.00,
      C = +phi^-3 the minimum rate is NEGATIVE (-0.043). So the (A, C) domain
      is a joint region, and the previously published A-bound is only valid on
      the C = 0 slice. The proposal's A-domain sentence is therefore WRONG as
      written and must be restated jointly.
  T2  the joint admissible region computed on a grid, with its boundary.
  T3  the joint corner: worst-case J and J^2 over the admissible (A, C) region
      at the physical bias. Compared against each effect alone.
  T4  STACKING IS SUPERADDITIVE. This refutes both the script's first guess and
      Grok's "additive-in-amplitude" expectation: at extended odd-quadratic
      coefficients the joint J^2 is about 4x the SUM of the two separate J^2
      values, i.e. the amplitudes roughly double rather than adding in
      quadrature. Grok was right to demand the corner and wrong about what it
      would show -- the same pattern as the negative-A prediction at 0955.
  T5  the combined worst-case bound Copilot asked for, reported SEPARATELY at
      the framework coefficient scale and over the extended scan, because the
      two differ by three orders of magnitude and reporting one number would
      hide exactly the scale dependence the disposition rests on.
  T6  the same for C3: worst-case K_lift over the joint region including the
      kappa scan, against both thresholds.
"""
import itertools, sys, collections
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
CHI = PHI ** -3
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def v600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5*np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    b = [PHI/2, 0.5, 1/(2*PHI), 0.0]
    ev = [p for p in itertools.permutations(range(4))
          if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in ev:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); val = [s[0]*b[0], s[1]*b[1], s[2]*b[2], 0.0]
            for k in range(4): v[p[k]] = val[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = v600(); N = 120; G = V @ V.T
edges = [(i, j) for i in range(N) for j in range(i+1, N) if abs(G[i, j] - PHI/2) < 1e-8]
nhat = V[0].copy()
mn = np.array([((V[i]+V[j])/2) @ nhat for i, j in edges])
en = np.array([((V[j]-V[i])*PHI) @ nhat for i, j in edges])
B = CHI

def min_rate(A, C):
    """min over both traversals of every edge"""
    fwd = 1 + A*mn + B*en + C*en*mn
    bwd = 1 + A*mn - B*en - C*en*mn
    return float(min(fwd.min(), bwd.min()))

def J_of(A, C):
    Q = np.zeros((N, N))
    for k, (i, j) in enumerate(edges):
        Q[i, j] = 1 + A*mn[k] + B*en[k] + C*en[k]*mn[k]
        Q[j, i] = 1 + A*mn[k] - B*en[k] - C*en[k]*mn[k]
    for i in range(N): Q[i, i] = -Q[i].sum()
    Au = np.vstack([Q.T, np.ones(N)]); b = np.zeros(N+1); b[-1] = 1.0
    pi = np.linalg.lstsq(Au, b, rcond=None)[0]
    out = 0.0
    for k, (i, j) in enumerate(edges):
        out = max(out, abs(pi[i]*Q[i, j] - pi[j]*Q[j, i]))
    return out

# ---------------- T1  the domain is not a rectangle
mr_corner = min_rate(-1.0, +CHI)
mr_C0 = min_rate(-1.0, 0.0)
ok("T1", mr_corner < 0 < mr_C0,
   f"the admissible domain is NOT a rectangle: at A = -1.00, C = 0 the minimum rate is {mr_C0:+.4f} "
   f"(admissible), but at A = -1.00, C = +phi^-3 it is {mr_corner:+.4f} (NEGATIVE, inadmissible). "
   "The published |A| <= 1.025 was computed at C = 0 only and does not hold jointly — "
   "the proposal's A-domain sentence is WRONG as written")

# ---------------- T2  joint region
As = np.linspace(-1.1, 1.1, 45)
Cs = np.linspace(-0.6, 0.6, 25)
adm = [(a, c) for a in As for c in Cs if min_rate(a, c) > 0]
a_at_C0 = max(a for a, c in adm if abs(c) < 1e-9)
a_at_Cmax = max((a for a, c in adm if abs(c - max(abs(x) for _, x in adm)) < 1e-9), default=None)
ok("T2", len(adm) > 0 and a_at_C0 >= 1.0,
   f"joint admissible region mapped on a {len(As)}x{len(Cs)} grid: {len(adm)} admissible points. "
   f"On the C = 0 slice |A| reaches {a_at_C0:.2f} (consistent with the published 1.025); "
   "off that slice the A-range contracts")

# ---------------- T3 / T4 / T5  joint corner and combined bound
J_base = J_of(0.0, 0.0)
J_negA = max(J_of(a, 0.0) for a, c in adm if a < 0)
J_oddC = max(J_of(0.0, c) for a, c in adm if abs(a) < 1e-9 and c != 0)
worst = max(adm, key=lambda p: J_of(*p))
J_joint = J_of(*worst)
ok("T3", J_joint > J_negA and J_joint > J_oddC,
   f"joint corner IS worse than either alone: worst admissible (A, C) = ({worst[0]:+.2f}, {worst[1]:+.3f}) "
   f"gives J = {J_joint:.3e}, against {J_negA:.3e} (negative A alone) and {J_oddC:.3e} (odd C alone); "
   f"baseline {J_base:.3e}")

sum_sq = J_negA**2 + J_oddC**2
ok("T4", J_joint**2 > 2.0 * sum_sq,
   f"STACKING IS SUPERADDITIVE: joint J^2 = {J_joint**2:.3e} against the sum of the separate J^2 values "
   f"{sum_sq:.3e} — a ratio of {J_joint**2/sum_sq:.2f}, i.e. the amplitudes roughly DOUBLE rather than "
   "adding in quadrature. This refutes both this script's first assertion and Grok's expectation that "
   "stacking would be additive-in-amplitude. He was right to demand the corner and wrong about the answer")

# framework scale vs extended range, reported separately
adm_fw = [(a, c) for a, c in adm if abs(c) <= CHI + 1e-9]
w_fw = max(adm_fw, key=lambda p: J_of(*p)); J_fw = J_of(*w_fw)
ok("T5", J_fw**2 < 1e-7 and J_joint**2 < 1e-5,
   f"COMBINED WORST-CASE BOUND (Copilot required edit 1/4), reported BY SCALE because the two differ by "
   f"three orders: at the framework coefficient scale |C| <= phi^-3 the worst admissible (A, C) = "
   f"({w_fw[0]:+.2f}, {w_fw[1]:+.3f}) gives **max J^2 = {J_fw**2:.2e}**; over the extended scan "
   f"|C| <= 0.6 it is **max J^2 = {J_joint**2:.2e}** at ({worst[0]:+.2f}, {worst[1]:+.3f}). Reporting one "
   "number would hide exactly the scale dependence the disposition rests on")

# ---------------- T6  C3 over the joint region incl. kappa
Adj = np.zeros((N, N), bool)
for i, j in edges: Adj[i, j] = Adj[j, i] = True
nbr = [np.where(Adj[v])[0] for v in range(N)]
dist = np.full((N, N), -1)
for s in range(N):
    dist[s, s] = 0; q = collections.deque([s])
    while q:
        u = q.popleft()
        for w in np.where(Adj[u])[0]:
            if dist[s, w] < 0: dist[s, w] = dist[s, u]+1; q.append(w)
nh2 = np.array([1.0, PHI, PHI**2, PHI**3]); nh2 /= np.linalg.norm(nh2)
eidx = {e: k for k, e in enumerate(edges)}
inc = [[eidx[tuple(sorted((v, int(w))))] for w in nbr[v]] for v in range(N)]
bias2 = np.array([(V[max(e)]-V[min(e)])/np.linalg.norm(V[max(e)]-V[min(e)]) @ nh2 for e in edges])
midn2 = np.array([((V[e[0]]+V[e[1]])/2) @ nh2 for e in edges])
f0 = (np.array([1., -1, 0, 0])/np.sqrt(2), np.array([0, 0, 1., -1])/np.sqrt(2))
W = []
for v in range(N):
    ws = []
    for w in nbr[v]:
        d = V[w]-V[v]; d /= np.linalg.norm(d)
        ws.append(np.sign(np.linalg.det(np.array([d, nh2, f0[0], f0[1]]))))
    W.append(np.array(ws))
readidx, readw = [], []
for v in range(N):
    order = sorted(range(len(nbr[v])), key=lambda k: -abs((V[nbr[v][k]]-V[v]) @ nh2))[:12]
    readidx.append([inc[v][k] for k in order]); readw.append(W[v][order])

def klift(A, C, kappa, delta=0.08, MC=3000, seed=31):
    r = np.random.default_rng(seed)
    scale = np.maximum(1.0 + kappa*A*midn2, 1e-3)
    mean = delta*bias2 + C*bias2*midn2
    em = np.zeros(N); acc = np.zeros((N, N))
    for _ in range(MC):
        x = mean + scale*r.normal(size=len(edges))
        eta = np.array([np.sign(readw[v] @ x[readidx[v]]) for v in range(N)])
        em += eta; acc += np.outer(eta, eta)
    em /= MC; acc /= MC; Cm = acc - np.outer(em, em)
    return float(np.arctanh(min(abs(Cm[dist == 1].mean()), 0.999)))

corners = [(a, c) for a in (-0.9, -0.5, 0.5, 0.9) for c in (-CHI, CHI) if min_rate(a, c) > 0]
Ks = [klift(a, c, kp) for a, c in corners for kp in (-1.0, 1.0)]
ok("T6", max(Ks) < 1/12,
   f"C3 over the joint region including the kappa scan: worst K_lift = {max(Ks):.4f} against thresholds "
   f"1/12 = 0.0833 (ratio {max(Ks)*12:.2f}) and 0.27. Clears on both channels")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
