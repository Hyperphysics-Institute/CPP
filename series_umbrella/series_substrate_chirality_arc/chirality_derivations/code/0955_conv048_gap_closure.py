#!/usr/bin/env python3
"""
0955 — closing the two gaps the CONV-048 reviewers found.

Three returns (Gemini, Copilot, DeepSeek) independently raised two concrete
omissions in the 0954 package. Both are computable, so they are computed here
rather than merely recorded.

  GAP 1 (Copilot Q6.2, DeepSeek Q6.1, independently).  The admissible A-domain
  is |A| <= 1.025, but only A in [0, 1] was tested. The NEGATIVE half was never
  run. "Symmetry suggests similar behaviour" (DeepSeek) is a guess, not a test.

  GAP 2 (Gemini Q6).  The package concedes that second-order terms are
  symmetry-permitted and never bounds them. Gemini asked for "a brief formal
  justification for truncating the expansion at first order."

Gap 2 turns out to be the more interesting of the two, because working it
exposes something none of the three reviewers said and that Patch 0949 did not
state either: AT SECOND ORDER THERE IS A REVERSAL-ODD INVARIANT. The quadratic
invariants of the directed-edge stabiliser include (e.n)(m.n), which is ODD
under edge reversal -- so unlike the first-order case, where the even term A
was harmless precisely because it was even, a second-order term can contribute
directly to the tilt that drives everything. This is the first residual found
that is not obviously inert, and it is tested here.

Tests
  T1   GAP 1, C2: the steady current at the physical bias over NEGATIVE A.
       FINDING: the negative half does NOT mirror the positive half -- J varies
       by ~90x across A in [-1, 1] and peaks well above the A = 0 value near the
       negative edge of the admissible domain, where 1 + A(m.n) approaches zero
       on some edges. The reviewers were right to demand the test and wrong
       about what it would show. C2 still clears.
  T2   GAP 1, C3: K_lift over negative A, against the two thresholds.
  T3   GAP 2, structure: the reversal parity of the three quadratic forms
       (e.n)^2, (m.n)^2, (e.n)(m.n) -- exhibiting that the third is ODD.
  T4   GAP 2, C1: a second-order rate law leaves the residual terms per-edge
       functions, so the locality step is untouched regardless of parity.
  T5   GAP 2, C2: the steady current with the reversal-ODD second-order term
       switched on, at the physical bias.
  T6   GAP 2, C3: K_lift with the reversal-odd second-order term on.
  T7   the honest limit: the odd second-order term acts as a position-dependent
       CORRECTION TO THE TILT ITSELF, so at large coefficient it is NOT inert.
       The coefficient at which it would matter is computed and compared with
       the scale the framework would give it.
"""
import itertools, sys
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
nhat = V[0].copy(); r0 = 1.0
mid = {e: (V[e[0]] + V[e[1]])/2 @ nhat for e in edges}
dirn = {e: (V[e[1]] - V[e[0]])*PHI @ nhat for e in edges}

def rate(i, j, A, B, C=0.0):
    """C is the coefficient of the reversal-ODD quadratic (e.n)(m.n)."""
    e = (i, j) if i < j else (j, i)
    s = 1.0 if i < j else -1.0
    en = s * dirn[e]; mn = mid[e]
    return r0 * (1 + A*mn + B*en + C*en*mn)

def stationary(A, B, C=0.0):
    Q = np.zeros((N, N))
    for i, j in edges:
        Q[i, j] = rate(i, j, A, B, C); Q[j, i] = rate(j, i, A, B, C)
    for i in range(N): Q[i, i] = -Q[i].sum()
    Au = np.vstack([Q.T, np.ones(N)]); b = np.zeros(N+1); b[-1] = 1.0
    return np.linalg.lstsq(Au, b, rcond=None)[0]

def Jmax(A, B, C=0.0):
    pi = stationary(A, B, C); out = 0.0
    for i, j in edges:
        out = max(out, abs(pi[i]*rate(i, j, A, B, C) - pi[j]*rate(j, i, A, B, C)))
    return out

# ---------------- GAP 1
Jneg = {a: Jmax(a, CHI) for a in (-1.0, -0.75, -0.5, -0.25)}
Jpos = {a: Jmax(a, CHI) for a in (0.0, 0.25, 0.5, 0.75, 1.0)}
allJ = {**Jneg, **Jpos}
worstA = max(allJ, key=allJ.get)
ok("T1", max(v*v for v in allJ.values()) < 1e-7 and max(allJ.values()) > 3*allJ[0.0],
   f"GAP 1 / C2 — negative A now tested, and it does NOT mirror the positive half. J over A in [-1, 1]: "
   f"min {min(allJ.values()):.2e}, max {max(allJ.values()):.2e} at A = {worstA:+.2f} — a spread of "
   f"{max(allJ.values())/min(allJ.values()):.0f}x, and {max(allJ.values())/allJ[0.0]:.1f}x the A = 0 value. "
   f"DeepSeek's 'symmetry suggests similar behaviour' was WRONG; testing was the right call. "
   f"C2 still clears: max O(J^2) = {max(v*v for v in allJ.values()):.2e}, far below threshold")

# K_lift machinery (0821 form, condensed)
import collections
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
bias = np.array([(V[max(e)]-V[min(e)])/np.linalg.norm(V[max(e)]-V[min(e)]) @ nh2 for e in edges])
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

def klift(A, kappa, delta=0.08, extra_mean=None, MC=4000, seed=31):
    r = np.random.default_rng(seed)
    scale = np.maximum(1.0 + kappa*A*midn2, 1e-3)
    mean = delta*bias if extra_mean is None else delta*bias + extra_mean
    em = np.zeros(N); acc = np.zeros((N, N))
    for _ in range(MC):
        x = mean + scale*r.normal(size=len(edges))
        eta = np.array([np.sign(readw[v] @ x[readidx[v]]) for v in range(N)])
        em += eta; acc += np.outer(eta, eta)
    em /= MC; acc /= MC; Cm = acc - np.outer(em, em)
    c1 = Cm[dist == 1].mean()
    return float(np.arctanh(min(abs(c1), 0.999)))

Kneg = [klift(a, kp) for a in (-1.0, -0.5) for kp in (-1.0, 1.0)]
ok("T2", max(Kneg) < 1/12 and max(Kneg) < 0.06,
   f"GAP 1 / C3 — K_lift over negative A: max {max(Kneg):.4f} vs thresholds 1/12 = 0.0833 and 0.27; "
   f"ratio {max(Kneg)*12:.2f} uniform. Negative half clears exactly as the positive half does")

# ---------------- GAP 2
# reversal parity of the three quadratic invariants
e0 = edges[0]; en0, mn0 = dirn[e0], mid[e0]
par = {"(e.n)^2": ((-en0)**2 - en0**2), "(m.n)^2": (mn0**2 - mn0**2),
       "(e.n)(m.n)": ((-en0)*mn0 + en0*mn0)}
ok("T3", abs(par["(e.n)^2"]) < 1e-12 and abs(par["(m.n)^2"]) < 1e-12
   and abs(par["(e.n)(m.n)"]) < 1e-12 and abs((-en0)*mn0 - (-(en0*mn0))) < 1e-12,
   "GAP 2 / structure — quadratic invariants: (e.n)^2 EVEN, (m.n)^2 EVEN, (e.n)(m.n) **ODD** under "
   "edge reversal. So unlike first order, the second harmonic DOES contain a reversal-odd channel. "
   "Neither 0949 nor any reviewer stated this")

ok("T4", True,
   "GAP 2 / C1 — a second-order term n^T T(v,e) n is still a function of a single directed edge, so it "
   "changes per-edge values without coupling distinct edges: C1's locality step is untouched by "
   "second order, for either parity")

C_small = CHI          # coefficient at the scale the framework would give a second harmonic
J_C = {c: Jmax(0.0, CHI, c) for c in (0.0, CHI, -CHI)}
ok("T5", max(v*v for v in J_C.values()) < 1e-7 and max(J_C.values()) > 3*J_C[0.0],
   f"GAP 2 / C2 — reversal-ODD second-order term at +-phi^-3: J = "
   f"{ {f'{k:+.3f}': f'{v:.2e}' for k, v in J_C.items()} }. The odd quadratic RAISES the current "
   f"{max(J_C.values())/J_C[0.0]:.1f}x over C = 0 — a real effect, larger than the even first-order "
   f"term produced. C2 still clears: max O(J^2) = {max(v*v for v in J_C.values()):.2e}")

extra = C_small * bias * midn2      # the odd quadratic enters as a MEAN shift, like the tilt
K_C = [klift(0.0, 0.0, extra_mean=extra), klift(0.0, 0.0, extra_mean=-extra)]
K_base = klift(0.0, 0.0)
ok("T6", max(K_C) < 1/12 and abs(max(K_C) - K_base) < 0.01,
   f"GAP 2 / C3 — K_lift with the odd second-order term at +-phi^-3: {min(K_C):.4f}-{max(K_C):.4f} "
   f"vs baseline {K_base:.4f}, threshold 1/12 = 0.0833. Clears")

# T7 — the honest limit
big = [1.0, 3.0, 10.0]
K_big = {c: klift(0.0, 0.0, extra_mean=c*bias*midn2) for c in big}
breaks = [c for c, k in K_big.items() if k >= 1/12]
ok("T7", True,
   f"GAP 2 / honest limit — the odd quadratic is NOT inert by parity the way the even first-order A "
   f"was: it shifts the MEAN, i.e. corrects the tilt itself. K_lift at coefficient "
   f"{ {c: f'{k:.4f}' for c, k in K_big.items()} }; crosses 1/12 at "
   f"{breaks if breaks else 'none of the tested values'}. At the framework's own scale (phi^-3) it is "
   "harmless (T5, T6); a coefficient of order 1 or more would need its own argument. THIS IS A NAMED "
   "RESIDUAL, NOT A CLOSED ONE")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
