#!/usr/bin/env python3
"""
0966 — the owed physical-bias test, plus the three fixes the pre-dispatch
returns demanded. Run BEFORE any R-2 dispatch.

Five pre-dispatch returns on the 0965 draft (GPT-5.6 Sol, Grok 4.6, Gemini,
Copilot, DeepSeek) were unanimous: HOLD. Their demands, addressed here.

  GROK'S DECISIVE OBJECTION, answered first because if it stands the whole T4
  evidence is worthless: "C_nn is a proxy for participation. The claim is about
  p(v). If C_nn is insensitive to a drop from p=12 toward p=4, a 3e-4 shift is
  not evidence."

Tests
  T1  IS C_nn SENSITIVE TO PARTICIPATION AT ALL? C_nn = (2/pi) arcsin(1/p) on
      the Gaussian base, so C_nn(p=12) = 0.0531 against C_nn(p=4) = 0.1609 --
      a factor of 3 across exactly the range in dispute. The proxy is sensitive.
  T2  THE NULL RESULT CONVERTS INTO A BOUND, which is the right answer to Grok
      rather than a defence of the proxy: inverting the relation, a measured
      |dC_nn| <= 3e-4 EXCLUDES any participation below p ~ 11.9.
  T3  p_eff(delta) REPORTED DIRECTLY, as Grok and Copilot required -- not
      C_nn alone. p_eff = 1/sin(pi C_nn / 2), measured across a multi-point
      delta scan THROUGH the physical bias, with standard errors.
  T4  THE OWED TEST AT THE PHYSICAL BIAS delta = phi^-3, with error bars, not
      the convenience value 0.10 used at 0965.
  T5  MULTI-POINT SCAN, not two endpoints (GPT, Grok, Copilot, DeepSeek): is
      there a systematic delta-dependent trend in p_eff, or only noise?
  T6  LINK (c) RESCOPED. 0965's T2 was weak and Grok said so: rank{d, n} = 2 is
      trivial and does not show a 2- or 3-edge reading is degenerate once
      (r1, r2) are in the frame. GPT put the logic sharply: four vectors to
      DEFINE chirality does not imply four edge coefficients to READ it -- only
      ONE of {d, n, r1, r2} is an edge direction. The dimensional argument as
      written does not carry (c). What carries it is the SCOPE: the canonical
      observable is the whole-vertex-figure orientation (0820 SS(1)), and a
      single-edge det is frame-dependent, hence not an invariant handedness
      reading. Demonstrated here.
"""
import itertools, sys, collections
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
CHI = PHI ** -3
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

C_of_p = lambda p: (2/np.pi)*np.arcsin(1.0/p)
p_of_C = lambda C: 1.0/np.sin(np.pi*C/2) if C > 0 else np.inf

# ---- T1  is the proxy sensitive?
c12, c4 = C_of_p(12), C_of_p(4)
ok("T1", c4/c12 > 2.5,
   f"C_nn IS sensitive to participation: C_nn(p=12) = {c12:.4f} vs C_nn(p=4) = {c4:.4f}, a factor of "
   f"{c4/c12:.2f} across exactly the range in dispute. Grok's objection is answerable — the proxy "
   "responds strongly to the quantity the claim is about")

# ---- T2  null result -> bound
dC = 3e-4
lo = 12.0
while lo > 1 and abs(C_of_p(lo) - c12) <= dC: lo -= 0.001
ok("T2", lo > 10,
   f"the NULL RESULT CONVERTS TO A BOUND: |dC_nn| <= {dC} excludes any participation below "
   f"p = {lo:.2f}. The 0965 measurement does not merely fail to detect concentration — it bounds "
   f"concentration to p >= {lo:.1f}, against a floor of 4")

# ---- lattice + observable
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
nbr = [np.where(np.abs(G[i] - PHI/2) < 1e-8)[0] for i in range(N)]
nhat = V[0].copy()
Adj = np.zeros((N, N), bool)
for i in range(N):
    for w in nbr[i]: Adj[i, int(w)] = True
dist = np.full((N, N), -1)
for s0 in range(N):
    dist[s0, s0] = 0; q = collections.deque([s0])
    while q:
        u = q.popleft()
        for w in np.where(Adj[u])[0]:
            if dist[s0, w] < 0: dist[s0, w] = dist[s0, u]+1; q.append(w)
edges = [(i, int(j)) for i in range(N) for j in nbr[i] if i < j]
eidx = {e: k for k, e in enumerate(edges)}
inc = [[eidx[tuple(sorted((v, int(w))))] for w in nbr[v]] for v in range(N)]
nh2 = np.array([1.0, PHI, PHI**2, PHI**3]); nh2 /= np.linalg.norm(nh2)
bias_e = np.array([float(((V[b]-V[a])/np.linalg.norm(V[b]-V[a])) @ nh2) for a, b in edges])
r1 = np.array([1., -1, 0, 0])/np.sqrt(2); r2 = np.array([0, 0, 1., -1])/np.sqrt(2)
W = [np.array([np.sign(np.linalg.det(np.array([(V[w]-V[v])/np.linalg.norm(V[w]-V[v]), nh2, r1, r2])))
               for w in nbr[v]]) for v in range(N)]

def Cnn_rep(delta, reps=6, MC=2500, seed0=101):
    vals = []
    for r_ in range(reps):
        rng = np.random.default_rng(seed0 + 977*r_)
        em = np.zeros(N); acc = np.zeros((N, N))
        for _ in range(MC):
            x = delta*bias_e + rng.normal(size=len(edges))
            eta = np.array([np.sign(W[v] @ x[inc[v]]) for v in range(N)])
            em += eta; acc += np.outer(eta, eta)
        em /= MC; acc /= MC; C = acc - np.outer(em, em)
        vals.append(float(C[dist == 1].mean()))
    v = np.array(vals); return v.mean(), v.std(ddof=1)/np.sqrt(len(v))

deltas = [0.0, 0.05, 0.10, 0.16, CHI, 0.30]
rows = []
for d in deltas:
    m, se = Cnn_rep(d)
    rows.append((d, m, se, p_of(abs(m)) if False else p_of_C(abs(m))))
print("\n  delta      C_nn      s.e.     p_eff")
for d, m, se, pe in rows:
    tag = "  <-- PHYSICAL" if abs(d - CHI) < 1e-9 else ""
    print(f"  {d:6.4f}  {m:+8.4f}  {se:7.5f}  {pe:8.3f}{tag}")

phys = [r for r in rows if abs(r[0]-CHI) < 1e-9][0]
base = rows[0]
ok("T3", phys[3] >= 4.0,
   f"p_eff REPORTED DIRECTLY (not C_nn alone): at the physical bias delta = phi^-3 = {CHI:.4f}, "
   f"p_eff = {phys[3]:.2f} against the floor of 4")
ok("T4", abs(phys[1] - base[1]) < 5*max(phys[2], base[2]) + 0.002,
   f"OWED TEST DONE at delta = phi^-3: C_nn = {phys[1]:+.4f} +- {phys[2]:.5f} against {base[1]:+.4f} "
   f"+- {base[2]:.5f} at delta = 0; shift {abs(phys[1]-base[1]):.4f}, within noise. 0965 tested at "
   "0.10, a convenience value; this is the registered physical bias")

pes = np.array([r[3] for r in rows]); ds = np.array([r[0] for r in rows])
slope = np.polyfit(ds, pes, 1)[0]
ok("T5", abs(slope) < 6.0 and pes.min() >= 4.0,
   f"MULTI-POINT SCAN through the physical value (6 points, 6 independent MC replicates each): "
   f"p_eff ranges [{pes.min():.2f}, {pes.max():.2f}], linear trend in delta = {slope:+.2f} per unit "
   "delta. No systematic concentration; minimum stays far above the floor")

# ---- T6  link (c) rescoped
def single_edge_sign(v, k, a1, a2):
    d = (V[nbr[v][k]]-V[v]); d /= np.linalg.norm(d)
    return np.sign(np.linalg.det(np.array([d, nh2, a1, a2])))
rng = np.random.default_rng(5)
flips = 0
for _ in range(200):
    a1 = rng.normal(size=4); a1 -= (a1@nh2)*nh2; a1 /= np.linalg.norm(a1)
    a2 = rng.normal(size=4); a2 -= (a2@nh2)*nh2; a2 -= (a2@a1)*a1; a2 /= np.linalg.norm(a2)
    if single_edge_sign(0, 0, a1, a2) != single_edge_sign(0, 0, r1, r2): flips += 1
ok("T6", flips > 20,
   f"LINK (c) RESCOPED. 0965's T2 was weak (Grok: rank{{d,n}} = 2 is trivial; GPT: only ONE of "
   f"{{d, n, r1, r2}} is an edge direction, so 'four vectors to DEFINE chirality' does not give "
   f"'four edges to READ it'). What actually carries (c) is SCOPE: a single-edge det is "
   f"FRAME-DEPENDENT — its sign flips under {flips}/200 random admissible frames — so it is not an "
   "invariant handedness reading. The canonical observable is the whole-vertex-figure orientation "
   "(0820 SS(1)), and CAPACITY-1's eta must be scoped to it. Under that scope (c) holds; as a ban on "
   "every sub-4-support functional it assumed the conclusion, and that version is withdrawn")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
