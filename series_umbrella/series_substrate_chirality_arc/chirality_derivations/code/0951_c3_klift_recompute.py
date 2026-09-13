#!/usr/bin/env python3
"""
0951 — C3's K_lift recomputed with L4-A's residual switched on.

Patch 0950 left one item between V3 and unconditional-on-the-residual: C3's
|K_lift| ~ 0.053 is computed in the measure, and the measure moves when the
reversal-even term A (m.n) is present. This recomputes K_lift in 0821's OWN
machinery -- same eta-field, same orientation weights, same correlator-vs-graph-
distance estimator -- rather than reconstructing a possibly different object.

How the residual enters the edge d.o.f. In 0821 the per-edge variable is
    x_e = delta * bias_e + N(0, 1),        bias_e = e.n  (reversal-ODD)
i.e. the rate law's tilt appears as a per-edge MEAN SHIFT. The residual
A (m.n) is reversal-EVEN: it multiplies both traversal directions of an edge
equally, so it cannot shift that mean. It enters instead as a per-edge SCALE
on the edge's fluctuation:
    x_e = delta * bias_e + (1 + kappa * A * mid_e.n) * N(0, 1).
The proportionality kappa between the rate modulation and the d.o.f. scale is
NOT on file, so it is scanned rather than assumed, and the sensitivity is
reported. That is the honest form of this recompute.

  T1  reproduce 0821's baseline: m=12 canonical vertex-figure eta at delta =
      0.08, A = 0, giving C_nn ~ -0.053 and K_lift/K_c ~ 0.64, with short-range
      decay (|C_d2/C_d1| << 1).
  T2  K_lift with the residual on, at A = delta (A the same order as the tilt)
      across a kappa scan: report the worst case.
  T3  K_lift with the residual on at A = 0.5 and A = 1.0 (A of order unity,
      the unconstrained case) across the same scan: report the worst case.
  T4  the decisive comparison: worst-case |K_lift| * a_max against BOTH
      thresholds -- uniform K_c = 1/lambda_max = 1/12 and the staggered/AFM
      K_c = 1/|lambda_min| (0824's frustration-corrected proxy). C3 clears iff
      both ratios stay below 1.
  T5  the eta-correlator stays SHORT-RANGE with the residual on (the d>=2
      content does not grow), so the nearest-neighbour-only confinement that
      C1's shared-edge step relies on is not disturbed.
"""
import numpy as np, itertools, collections, sys

rng = np.random.default_rng(31)
phi = (1 + np.sqrt(5)) / 2
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def even_perms(t):
    P = [p for p in itertools.permutations(range(4))
         if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V = set()
for i in range(4):
    for s in (1, -1): v = [0, 0, 0, 0]; v[i] = s; V.add(tuple(v))
for s in itertools.product([0.5, -0.5], repeat=4): V.add(s)
for sg in itertools.product([1, -1], repeat=3):
    for w in even_perms([0, sg[0]*0.5, sg[1]*1/(2*phi), sg[2]*phi/2]): V.add(w)
V = np.array(sorted(V)); N = len(V)
Dm = np.sqrt(((V[:, None] - V[None])**2).sum(-1))
ed = np.min(Dm[Dm > 1e-6]); Adj = (np.abs(Dm - ed) < 1e-6)
nbr = [np.where(Adj[v])[0] for v in range(N)]

dist = np.full((N, N), -1)
for s in range(N):
    dist[s, s] = 0; q = collections.deque([s])
    while q:
        u = q.popleft()
        for w in np.where(Adj[u])[0]:
            if dist[s, w] < 0: dist[s, w] = dist[s, u] + 1; q.append(w)

nhat = np.array([1.0, phi, phi**2, phi**3]); nhat /= np.linalg.norm(nhat)
E = {}
for v in range(N):
    for w in nbr[v]: E[tuple(sorted((v, int(w))))] = True
edges = list(E.keys()); eidx = {e: i for i, e in enumerate(edges)}; nE = len(edges)
inc = [[eidx[tuple(sorted((v, int(w))))] for w in nbr[v]] for v in range(N)]
bias = np.array([(lambda d: d/np.linalg.norm(d))(V[max(e)] - V[min(e)]) @ nhat for e in edges])
midn = np.array([((V[e[0]] + V[e[1]])/2) @ nhat for e in edges])      # reversal-EVEN

lam = np.linalg.eigvalsh(Adj.astype(float))
lam_max, lam_min = lam.max(), lam.min()
Kc_unif, Kc_afm = 1/lam_max, 1/abs(lam_min)

def orient_weights(frame):
    r1, r2 = frame; W = []
    for v in range(N):
        ws = []
        for w in nbr[v]:
            d = V[w] - V[v]; d /= np.linalg.norm(d)
            ws.append(np.sign(np.linalg.det(np.array([d, nhat, r1, r2]))))
        W.append(np.array(ws))
    return W

def corr(W, m_read, delta, A=0.0, kappa=0.0, MC=8000, seed=31):
    r = np.random.default_rng(seed)
    readidx, readw = [], []
    for v in range(N):
        order = sorted(range(len(nbr[v])), key=lambda k: -abs((V[nbr[v][k]] - V[v]) @ nhat))[:m_read]
        readidx.append([inc[v][k] for k in order]); readw.append(W[v][order])
    scale = 1.0 + kappa * A * midn                      # reversal-even per-edge scale
    scale = np.maximum(scale, 1e-3)
    em = np.zeros(N); acc = np.zeros((N, N))
    for _ in range(MC):
        x = delta * bias + scale * r.normal(size=nE)
        eta = np.array([np.sign(readw[v] @ x[readidx[v]]) for v in range(N)])
        em += eta; acc += np.outer(eta, eta)
    em /= MC; acc /= MC; C = acc - np.outer(em, em)
    cd = {d: C[dist == d].mean() for d in range(0, 4)}
    return cd, float(np.arctanh(np.clip(abs(cd[1]), 0, 0.999)))

f0 = (np.array([1., -1, 0, 0])/np.sqrt(2), np.array([0, 0, 1., -1])/np.sqrt(2))
W = orient_weights(f0)
delta0 = 0.08

# ---- T1 baseline
cd0, K0 = corr(W, 12, delta0, 0.0, 0.0)
ok("T1", abs(abs(cd0[1]) - 0.053) < 0.012 and abs(cd0[2]/cd0[1]) < 0.15,
   f"0821 baseline reproduced: C_nn = {cd0[1]:+.4f}, K_lift = {K0:.4f}, K_lift/K_c(unif) = {K0/Kc_unif:.2f}, "
   f"decay |C_d2/C_d1| = {abs(cd0[2]/cd0[1]):.3f}")

# ---- T2 / T3  residual on
kappas = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
def worst(Aval):
    out = []
    for kp in kappas:
        cd, K = corr(W, 12, delta0, Aval, kp)
        out.append((K, kp, cd))
    return max(out, key=lambda t: t[0])

K_Adelta, kp_a, cd_a = worst(delta0)
ok("T2", K_Adelta / Kc_unif < 1.0,
   f"A = delta: worst-case over kappa scan is K_lift = {K_Adelta:.4f} (kappa = {kp_a:+.1f}), "
   f"K_lift/K_c(unif) = {K_Adelta/Kc_unif:.2f}")

K_A05, kp_b, cd_b = worst(0.5)
K_A10, kp_c, cd_c = worst(1.0)
ok("T3", K_A05 / Kc_unif < 1.0 and K_A10 / Kc_unif < 1.0,
   f"A = 0.5: K_lift = {K_A05:.4f} (/K_c = {K_A05/Kc_unif:.2f}); "
   f"A = 1.0: K_lift = {K_A10:.4f} (/K_c = {K_A10/Kc_unif:.2f})")

# ---- T4 both thresholds
Kw = max(K0, K_Adelta, K_A05, K_A10)
r_unif, r_afm = Kw / Kc_unif, Kw / Kc_afm
ok("T4", r_unif < 1.0 and r_afm < 1.0,
   f"WORST CASE over all A and kappa tested: K_lift = {Kw:.4f}. Against uniform K_c = 1/{lam_max:.3f} "
   f"=> ratio {r_unif:.2f} (margin {100*(1-r_unif):.0f}%); against staggered/AFM K_c = 1/{abs(lam_min):.3f} "
   f"=> ratio {r_afm:.2f} (margin {100*(1-r_afm):.0f}%). C3 CLEARS ON BOTH CHANNELS")

# ---- T5 short-range preserved
decays = [abs(cd[2]/cd[1]) for cd in (cd0, cd_a, cd_b, cd_c)]
ok("T5", max(decays) < 0.2,
   f"eta-correlator stays short-range with the residual on: max |C_d2/C_d1| = {max(decays):.3f} — "
   "the nearest-neighbour confinement C1's shared-edge step relies on is not disturbed")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
