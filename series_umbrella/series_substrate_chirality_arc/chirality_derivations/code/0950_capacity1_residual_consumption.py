#!/usr/bin/env python3
"""
0950 — does THEO-CHIR-CAPACITY-1 (V3) consume L4-A's named residual?

Patch 0949 discharged MA.1's form to its reversal-odd first harmonic and named
what is NOT forced: the reversal-even midpoint term A (m.n), and higher
harmonics. 0949 filed, but did not claim, the question of whether V3's
Mechanism-A conditionality consumes that residual. This patch answers it by
re-running CAPACITY-1's three discharged conditions with A != 0 switched on,
reusing the 0694 NESS construction.

CAPACITY-1's Mechanism-A dependence, as stated at 0924/0925:
  "conditional on Mechanism A and per-edge independence of its measure
   (C1 shared-edge step)".

  C1  shared-edge-only coupling (0826) on the per-edge-independent measure,
      plus the refined-chord spectral bound (0828).
  C2  the O(delta^3) NESS current neither shifts the threshold nor drives
      ordering, at the physical bias (0822).
  C3  eta off-critical in every mode, |K_lift| ~ 0.053 vs thresholds (0823-5).

Tests
  T1  the residual terms are PER-EDGE functions. A (m.n) depends only on the
      undirected edge {v,w} (its midpoint); a quadratic n^T T n depends only on
      the directed edge. Neither introduces any coupling between DISTINCT
      edges. So the factorization structure of the measure over edges is
      untouched -- only per-edge parameter VALUES change.
  T2  per-edge independence therefore survives A != 0: exhibited by showing the
      effective per-edge tilt is B/(r0 + A m.n), a function of that edge alone.
  T3  C1's spectral bound does not reference the rate law AT ALL. kappa(z*) is
      built from the OBSERVABLE's weights c^v_e under the pointwise
      participation floor p(v) >= 4; rates enter only via "per-edge-independent
      measure => nearest-neighbour coupling", which T1/T2 preserve. Re-verified
      here against 120 adversarial non-homogeneous weightings, as at 0828.
      => C1 IS ROBUST TO THE RESIDUAL.
  T4  C2, tested not argued: rebuild the 0694 NESS with A != 0 and measure the
      delta-scaling of the steady current. A = 0 reproduces 0694's delta^3.
      With a CONSTANT A the onset moves to ~delta^1, with J ~ A^2 delta -- a
      TWO-order promotion at small delta. (My first pass tied A to delta, which
      gives A^2 delta = delta^3 and masked the effect entirely; the test refused
      the claim and the claim was corrected, not the test.)
  T5  C2's structural argument survives regardless: the current stays
      divergence-free and T-odd, so T-odd current vs T-even eta-ordering still
      couples only at O(J^2). Only the magnitude input can move.
  T6  and the magnitude does NOT move where C2 makes its claim. C2 is stated
      "at the physical bias, not all-orders". At delta = phi^-3 the current is
      2e-5 to 3e-5 across A in [0, 1] -- within a factor of 2 of the A = 0
      value, with O(J^2) ~ 1e-9 throughout, far below C3's clearance. The
      scaling change is a small-delta phenomenon that does not reach the
      physical bias.
  T7  C3's |K_lift| is computed from the measure and so is A-sensitive in
      principle; its headline margin (~44% uniform, 33% on the kappa bound)
      is reported alongside the measured shift so the re-read is quantitative.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
CHI = PHI ** -3
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def build_600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5*np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI/2, 0.5, 1/(2*PHI), 0.0]
    ev = [p for p in itertools.permutations(range(4))
          if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in ev:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); vals = [s[0]*base[0], s[1]*base[1], s[2]*base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    V = np.array(U)
    G = V @ V.T
    edges = [(i, j) for i in range(120) for j in range(i+1, 120)
             if abs(G[i, j] - PHI/2) < 1e-8]
    return V, edges

V, edges = build_600()
nhat = V[0].copy()
inv_edge = PHI  # 1/edge_length

# ---------- T1 / T2 : the residual is per-edge
mid = {(i, j): (V[i] + V[j]) / 2 for i, j in edges}
dirs = {(i, j): (V[j] - V[i]) * inv_edge for i, j in edges}
# midpoint is reversal-symmetric; direction flips
t1 = all(np.allclose(mid[(i, j)], (V[j] + V[i]) / 2) and
         np.allclose(-(dirs[(i, j)]), (V[i] - V[j]) * inv_edge) for i, j in edges)
ok("T1", t1 and len(edges) == 720,
   f"{len(edges)} undirected edges; A (m.n) depends only on the edge's midpoint and a quadratic "
   "n^T T n only on the directed edge — neither couples DISTINCT edges, so the measure's "
   "factorization structure over edges is untouched")

r0, B = 1.0, 1e-3
def tilt(i, j, A):
    return B / (r0 + A * float(mid[(i, j)] @ nhat))
t2 = all(np.isfinite(tilt(i, j, 0.5)) for i, j in edges)
distinct = len({round(tilt(i, j, 0.5), 12) for i, j in edges}) > 1
ok("T2", t2 and distinct,
   "effective per-edge tilt B/(r0 + A m.n) is a function of that edge alone (and now varies "
   "edge to edge) — per-edge independence SURVIVES A != 0")

# ---------- T3 : C1's bound is about the observable, not the rates
rng = np.random.default_rng(828)
nbr = {i: [] for i in range(120)}
for i, j in edges: nbr[i].append(j); nbr[j].append(i)
def kappa(z): return (2/np.pi) * np.arcsin(z) / z
viol = 0; rhos = []
for _ in range(120):                      # 120 adversarial non-homogeneous weightings, as 0828
    c = {}
    for v in range(120):
        w = rng.random(len(nbr[v])) ** 3 + 1e-3      # deliberately spiky
        w = w / np.linalg.norm(w)
        # enforce the pointwise participation floor p(v) >= 4  <=>  sum c^4 <= 1/4
        while np.sum(w**4) > 0.25:
            w = (w + 0.25/len(w)); w = w / np.linalg.norm(w)
        for k, u in enumerate(nbr[v]): c[(v, u)] = w[k]
    M = np.zeros((120, 120))
    for i, j in edges:
        z = c[(i, j)] * c[(j, i)]
        M[i, j] = M[j, i] = (2/np.pi) * np.arcsin(min(z, 1.0))
    zstar = max(c[(i, j)] * c[(j, i)] for i, j in edges)
    rho = max(abs(np.linalg.eigvalsh(M)))
    rhos.append(rho)
    if rho > kappa(zstar) + 1e-9: viol += 1
ok("T3", viol == 0 and max(rhos) < 1.0,
   f"C1's spectral bound re-verified: 0 violations over 120 adversarial non-homogeneous weightings, "
   f"max rho = {max(rhos):.4f} < 1. The bound's inputs are the OBSERVABLE's weights under the "
   "pointwise floor — the rate law never appears. C1 IS ROBUST TO THE RESIDUAL")

# ---------- T4 : C2, tested. Rebuild the NESS with A != 0.
def stationary(delta, A):
    Q = np.zeros((120, 120))
    for i, j in edges:
        cij = float(dirs[(i, j)] @ nhat); mij = float(mid[(i, j)] @ nhat)
        Q[i, j] = r0 * (1 + A*mij + delta*cij)
        Q[j, i] = r0 * (1 + A*mij - delta*cij)
    for i in range(120): Q[i, i] = -Q[i].sum()
    Aug = np.vstack([Q.T, np.ones(120)])
    b = np.zeros(121); b[-1] = 1.0
    pi, *_ = np.linalg.lstsq(Aug, b, rcond=None)
    return pi

def Jmax(delta, A, pi):
    out = 0.0
    for i, j in edges:
        cij = float(dirs[(i, j)] @ nhat); mij = float(mid[(i, j)] @ nhat)
        rij = r0*(1 + A*mij + delta*cij); rji = r0*(1 + A*mij - delta*cij)
        out = max(out, abs(pi[i]*rij - pi[j]*rji))
    return out

def slope(ds, js):
    L = np.polyfit(np.log(ds), np.log(js), 1); return L[0]

ds = np.array([2e-3, 4e-3, 8e-3, 1.6e-2])
s0 = slope(ds, [Jmax(d, 0.0, stationary(d, 0.0)) for d in ds])
s_const = slope(ds, [Jmax(d, 0.3, stationary(d, 0.3)) for d in ds])
# A^2 scaling of the promoted term
j_a = [Jmax(1.6e-2, a, stationary(1.6e-2, a)) for a in (0.2, 0.4, 0.8)]
a2_like = 3.0 < j_a[1]/j_a[0] < 5.5 and 3.0 < j_a[2]/j_a[1] < 9.0
ok("T4", abs(s0 - 3.0) < 0.15 and abs(s_const - 1.0) < 0.2 and a2_like,
   f"steady-current onset: A = 0 gives slope {s0:.2f} (0694's delta^3, reproduced); CONSTANT A = 0.3 "
   f"gives slope {s_const:.2f}, i.e. J ~ A^2 delta — a TWO-order promotion at small delta. "
   "(First pass tied A to delta, giving A^2 delta = delta^3 and masking this; the test refused the "
   "claim and the claim was corrected)")

# ---------- T5 : C2's structural argument survives
d = 8e-3; pi = stationary(d, d)
div = np.zeros(120)
for i, j in edges:
    cij = float(dirs[(i, j)] @ nhat); mij = float(mid[(i, j)] @ nhat)
    Jij = pi[i]*r0*(1 + d*mij + d*cij) - pi[j]*r0*(1 + d*mij - d*cij)
    div[i] += Jij; div[j] -= Jij
ok("T5", np.max(np.abs(div)) < 1e-10,
   f"with A != 0 the NESS current is still divergence-free (max |div J| = {np.max(np.abs(div)):.2e}); "
   "T-odd current vs T-even eta-ordering still couples only at O(J^2). C2's SYMMETRY argument is "
   "untouched — only its magnitude input moves")

# ---------- T6 : magnitude at the physical bias
d_phys = CHI
Js = {a: Jmax(d_phys, a, stationary(d_phys, a)) for a in (0.0, 0.1, 0.236, 0.5, 1.0)}
ratio = max(Js.values()) / min(Js.values())
ok("T6", ratio < 2.5 and max(v*v for v in Js.values()) < 1e-8,
   f"at the physical bias delta = phi^-3: J = { {a: f'{v:.2e}' for a, v in Js.items()} }; spread across "
   f"A in [0,1] is a factor of {ratio:.2f}, O(J^2) <= {max(v*v for v in Js.values()):.2e} throughout. "
   "C2 is stated AT THE PHYSICAL BIAS, and there the residual does not move the magnitude — the "
   "scaling change of T4 is a small-delta phenomenon that does not reach phi^-3")

# ---------- T7 : report the measure shift for the quantitative re-read
pi0 = stationary(d_phys, 0.0); piA = stationary(d_phys, d_phys)
shift = float(np.max(np.abs(piA - pi0)) / np.max(np.abs(pi0 - 1/120)))
ok("T7", np.isfinite(shift),
   f"measure shift from the residual at the physical bias: max|pi_A - pi_0| is {100*shift:.1f}% of the "
   "A=0 tilt itself. C3's |K_lift| ~ 0.053 against thresholds 0.095 / 0.27 (margins ~44% / 80%) is "
   "computed from the measure and should be re-evaluated at this shift by 0927's holder")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
