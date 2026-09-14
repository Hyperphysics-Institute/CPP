#!/usr/bin/env python3
"""
0971 — TARROW-2 re-read against Patch 0960.

OPEN-CHIR-1d-beta's problem history states that discharging Mechanism A
"would unconditionalize BOTH CAPACITY-1 (spatial) and TARROW-2 (temporal)",
and THEO-CHIR-TARROW-2's own header says "once OPEN-FP-F1-2 discharges
Mechanism A the W-move becomes unconditional." Patch 0960 narrowed Mechanism A
to its DERIVED reversal-odd first harmonic, leaving A (the reversal-even
midpoint term) and higher harmonics as named residuals. Nobody had re-read
TARROW-2 against that. This does.

TARROW-2's argument is a Kolmogorov cycle computation on the 1200 triangular
faces of the 600-cell:
  (i)   the cycle log-ratio is ODD in delta -- no O(delta^2) term, so the first
        possible violation is O(delta^3);
  (ii)  per face a+b+c = 0 (closed loop, uniform edge length), so the
        O(delta^1) sum vanishes for EVERY face, and the O(delta^3) content is
        2 delta^3 abc via a^3+b^3+c^3 = 3abc;
  (iii) 420 of the 1200 faces carry nonzero abc => detailed balance VIOLATED
        => the process is non-reversible => C_T = Yes.

Tests
  T1   the face count and the a+b+c = 0 identity, reproduced.
  T2   TARROW-2's headline numbers at A = 0: exactly 420 of 1200 faces carry
       nonzero cycle affinity, and the abc values are 1/8 and 1/4.
  T3   the order counting at A = 0: max cycle affinity scales as delta^3,
       confirming claim (i)/(ii).
  T4   THE RESIDUAL BREAKS THE ORDER COUNTING. With a constant reversal-even A,
       the per-face O(delta^1) cancellation FAILS: the effective tilt becomes
       B/(1 + A m_e), which is position-dependent, so sum over the face is no
       longer proportional to a+b+c = 0. Measured slope drops from 3 to ~1.
       TARROW-2's claim (i) -- "no O(delta^2) term, first violation at
       O(delta^3)" -- therefore CONSUMES A = 0, exactly as Patch 0949 predicted
       for the NESS-based results.
  T5   BUT THE CONCLUSION IS ROBUST, AND STRENGTHENED. The SAME 420 faces carry
       nonzero affinity at every A tested: the residual changes the ORDER at
       which detailed balance fails, not WHETHER it fails -- and it fails
       EARLIER. Non-reversibility, hence C_T = Yes, hence the W3 -> W1
       candidate, survives the residual.
  T6   at the physical bias delta = phi^-3 the violation is large in both
       cases, so nothing here is a small-delta artefact.
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
adj = np.abs(G - PHI/2) < 1e-8
nbr = [np.where(adj[i])[0] for i in range(N)]
nhat = V[0].copy()
faces = []
for i in range(N):
    nb = [int(x) for x in nbr[i] if x > i]
    for a, b_ in itertools.combinations(nb, 2):
        if adj[a, b_]: faces.append((i, a, b_))

def proj(u, w):
    d = V[w] - V[u]; return float((d/np.linalg.norm(d)) @ nhat)
def mid(u, w):
    return float(((V[u] + V[w])/2) @ nhat)

abcs = []
sums = []
for f in faces:
    a = proj(f[0], f[1]); b = proj(f[1], f[2]); c = proj(f[2], f[0])
    sums.append(a + b + c); abcs.append(a*b*c)
sums = np.array(sums); abcs = np.array(abcs)

ok("T1", len(faces) == 1200 and np.abs(sums).max() < 1e-12,
   f"{len(faces)} triangular faces (TARROW-2 states 1200); the per-face identity a+b+c = 0 holds "
   f"exactly, max |a+b+c| = {np.abs(sums).max():.1e}")

nz = int((np.abs(abcs) > 1e-12).sum())
vals = sorted({round(abs(x), 6) for x in abcs if abs(x) > 1e-12})
ok("T2", nz == 420 and vals == [0.125, 0.25],
   f"TARROW-2's headline numbers reproduced at A = 0: exactly {nz} of {len(faces)} faces carry "
   f"nonzero abc, with |abc| values {vals} = 1/8 and 1/4")

def cyc(face, A, B, C=0.0):
    tot = 0.0
    for k in range(3):
        u, w = face[k], face[(k+1) % 3]
        cc = proj(u, w); mm = mid(u, w)
        tot += np.log((1 + A*mm + B*cc + C*cc*mm)/(1 + A*mm - B*cc - C*cc*mm))
    return tot

ds = np.array([2e-3, 4e-3, 8e-3, 1.6e-2])
def slope(A):
    mx = [max(abs(cyc(f, A, d)) for f in faces) for d in ds]
    return float(np.polyfit(np.log(ds), np.log(mx), 1)[0])

s0 = slope(0.0)
ok("T3", abs(s0 - 3.0) < 0.15,
   f"order counting at A = 0: max cycle affinity scales as delta^{s0:.2f} — TARROW-2's claims (i) and "
   "(ii) reproduced, the O(delta^1) sum vanishing per face and the first violation at O(delta^3)")

sA = slope(0.3)
ok("T4", abs(sA - 1.0) < 0.2,
   f"THE RESIDUAL BREAKS THE ORDER COUNTING: with constant A = 0.3 the slope is {sA:.2f}, not 3. The "
   "per-face O(delta^1) cancellation fails because the effective tilt becomes B/(1 + A m_e), which is "
   "position-dependent, so the face sum is no longer proportional to a+b+c = 0. TARROW-2's claim (i) "
   "CONSUMES A = 0, exactly as Patch 0949 predicted for the NESS-based results")

viol = {}
for A in (0.0, 0.3, -0.3, 1.0):
    s = np.array([cyc(f, A, 1e-2) for f in faces])
    viol[A] = int((np.abs(s) > 1e-12).sum())
ok("T5", len(set(viol.values())) == 1 and set(viol.values()) == {420},
   f"BUT THE CONCLUSION IS ROBUST AND STRENGTHENED: the same {viol[0.0]} faces carry nonzero affinity "
   f"at every A tested {sorted(viol)} — the residual changes the ORDER at which detailed balance "
   "fails, not WHETHER it fails, and it fails EARLIER. Non-reversibility, C_T = Yes, and the "
   "W3 -> W1 candidate all survive")

phys = {A: max(abs(cyc(f, A, CHI)) for f in faces) for A in (0.0, 0.3)}
ok("T6", min(phys.values()) > 1e-4,
   f"at the physical bias delta = phi^-3 the maximum cycle affinity is {phys[0.0]:.3e} at A = 0 and "
   f"{phys[0.3]:.3e} at A = 0.3 — large in both cases, so none of this is a small-delta artefact")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
