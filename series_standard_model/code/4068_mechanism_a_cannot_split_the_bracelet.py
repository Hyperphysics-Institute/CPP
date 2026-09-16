"""4068 (EW lane) -- 4050's uncomputed step, executed: Mechanism A CANNOT split the W-bracelet's
two helicity states. Not "does not at this delta" -- CANNOT, by an exact symmetry, at every delta.

THE RESULT. Theta = diag(1,1,1,-1) is an IMPROPER symmetry of the entire Mechanism-A dynamics:
    * Theta preserves the 600-cell and fixes n_hat exactly (4046).
    * Mechanism A's rates r(v->w) = r0 (1 + delta * e_vw . n_hat) depend on the geometry only through
      e_vw . n_hat, and Theta preserves both e_vw and n_hat  =>  Q is Theta-EQUIVARIANT at every delta.
    * Hence pi is Theta-invariant, and EVERY functional of (Q, pi) is Theta-even.
  The helicity h is Theta-ODD (4050: flips on all 63 rings, unchanged on none). A Theta-even dynamics
  cannot assign different values to two states exchanged by Theta. The splitting is IDENTICALLY ZERO.

  Delta != 0 breaks TIME-reversal (detailed balance fails at O(delta^3), 0689/TARROW-2) -- confirmed here.
  It does NOT break SPATIAL parity. The T-arrow and the P-asymmetry are independent, and Mechanism A
  supplies only the first.

CHECKS (exact linear algebra, full 120-vertex chain, no sampling)
  A1  rings + helicity reproduce 4050 -- WITH AN ERRATUM (see A1 output).
  A2  Theta maps rings to rings and flips h on all 63 rings through the host vertex.
  A3  delta = 0: pi uniform, all circulations zero (the degenerate starting point).
  A4  THE SYMMETRY: Q[Theta v, Theta w] = Q[v, w] and pi[Theta v] = pi[v] to machine precision, at
      every delta tested. This is the theorem, numerically.
  A5  THE CONSEQUENCE: on SF-2's W-bracelet orbit (the 1200 rings, identified by centroid norm
      |c| = 1/(2phi) + 1/2 = 0.809017 = phi/2), Delta = circ(R) - circ(Theta R) is ZERO to machine
      precision at every delta, while individual circulations are nonzero (~5e-5). The instrument sees;
      there is nothing to see.
  A6  CONTROL (the instrument is not blind): the NESS current itself is nonzero and its detailed-balance
      defect scales as delta^3, reproducing 0689/TARROW-2 independently.
  A7  OBSERVABLE-CHOICE NOTE: circulation is P-EVEN (4049/4050's own lesson). A6 shows the negative does
      not depend on that choice -- A4 forbids ANY observable, P-odd or P-even, from splitting.
"""
import numpy as np, itertools as it, collections
from itertools import permutations as P

phi = (1 + np.sqrt(5)) / 2; edge = 1 / phi

def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [b[0]*s1, b[1]*s2, b[2]*s3, b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = build600(); N = len(V); assert N == 120
D = np.linalg.norm(V[:, None] - V[None], axis=2)
A = np.abs(D - edge) < 1e-9
nb = [set(np.flatnonzero(A[i]).tolist()) for i in range(N)]
assert all(len(x) == 12 for x in nb)

cyc = []
def walk(p):
    if len(p) == 6:
        if p[0] in nb[p[-1]] and not any(b in nb[a] and abs(p.index(a)-p.index(b)) not in (1,5)
                                         for a, b in it.combinations(p, 2)): cyc.append(tuple(p))
        return
    for x in nb[p[-1]]:
        if x in p or (len(p) >= 2 and x < p[1]): continue
        walk(p + (x,))
for a in sorted(nb[0]): walk((0, a))

canon = lambda R: min(min((R[i:]+R[:i]) for i in range(6)), min((R[::-1][i:]+R[::-1][:i]) for i in range(6)))
allcyc = {}
def walk_all(p, start):
    if len(p) == 6:
        if p[0] in nb[p[-1]] and not any(b in nb[a] and abs(p.index(a)-p.index(b)) not in (1,5)
                                         for a, b in it.combinations(p, 2)): allcyc[canon(tuple(p))] = tuple(p)
        return
    for x in nb[p[-1]]:
        if x in p or x < start: continue
        walk_all(p + (x,), start)
for s in range(N):
    for a in nb[s]:
        if a > s: walk_all((s, a), s)

nhat = V[0] / np.linalg.norm(V[0]); Th = np.diag([1., 1, 1, -1])
EPS = np.zeros((4,4,4,4))
for q in it.permutations(range(4)): EPS[q] = np.sign(np.linalg.det(np.eye(4)[list(q)]))

def bivec(idx):
    C = np.array([V[i] for i in idx]); C = C - C.mean(0)
    L = np.zeros((4,4))
    for i in range(6):
        a, b = C[i], C[(i+1) % 6]; L += np.outer(a, b) - np.outer(b, a)
    return L

def hel(idx):
    return float(np.einsum('ijkl,ij,k,l->', EPS, bivec(idx), np.array([V[i] for i in idx]).mean(0), nhat))

h = np.array([hel(c) for c in cyc])
cnt = collections.Counter(np.round(np.abs(h), 6))
print(f"A1  rings through host vertex: {len(cyc)}; all carry nonzero helicity: {all(abs(x)>1e-9 for x in h)}")
print(f"A1  *** ERRATUM TO 4050 *** |h| takes TWO values, not one: {dict(cnt)}")
print(f"    1/(2phi) = {1/(2*phi):.6f} holds for {cnt[round(1/(2*phi),6)]} of 63 rings, NOT all 63.")
print(f"    4050 read the magnitude off nz[0] and generalised. P-oddness and the flip are unaffected.")
assert len(cyc) == 63 and all(abs(x) > 1e-9 for x in h) and len(cnt) == 2

key = {tuple(np.round(v, 9)): i for i, v in enumerate(V)}
pmv = np.array([key[tuple(np.round(Th @ V[i], 9))] for i in range(N)])
def th(R): return tuple(int(pmv[i]) for i in R)
flip = sum(1 for R in cyc if abs(hel(th(R)) + hel(R)) < 1e-9)
print(f"A2  induced 6-cycles: {len(allcyc)}; Theta flips h on {flip}/63, unchanged on {63-flip}")
assert flip == 63

def ness(d):
    Q = np.zeros((N, N))
    for v in range(N):
        for w in nb[v]:
            Q[v, w] = 1 + d * float(((V[w]-V[v])/edge) @ nhat)
    np.fill_diagonal(Q, -Q.sum(1))
    M = Q.T.copy(); M[-1] = 1
    return Q, np.linalg.solve(M, np.r_[np.zeros(N-1), 1])

def circ(R, Q, pi):
    return sum(pi[R[i]]*Q[R[i],R[(i+1)%6]] - pi[R[(i+1)%6]]*Q[R[(i+1)%6],R[i]] for i in range(6))

Q0, pi0 = ness(0.0)
print(f"A3  delta=0: pi uniform {np.allclose(pi0,1/N)}; max|circ| = {max(abs(circ(R,Q0,pi0)) for R in cyc):.1e}")

cn = lambda R: round(float(np.linalg.norm(np.array([V[i] for i in R]).mean(0))), 6)
W = [R for R in allcyc.values() if cn(R) == 0.809017]
print(f"A5  W-bracelet orbit (SF-2 Thm 4.2, |c| = phi/2 = 0.809017): {len(W)} rings; Theta closes on it: "
      f"{all(canon(th(R)) in allcyc for R in W)}")
assert len(W) == 1200

print("A4/A5/A6  delta      |Q[Tv,Tw]-Q|   |pi[Tv]-pi|    max|circ| on W   max|SPLITTING|   DB defect")
dd = {}
for lab, d in [("phi^-3", phi**-3), ("0.35", 0.35), ("0.2", 0.2), ("0.1", 0.1), ("0.05", 0.05)]:
    Q, pi = ness(d)
    eq = max(abs(Q[pmv[v], pmv[w]] - Q[v, w]) for v in range(N) for w in range(N))
    pe = np.abs(pi[pmv] - pi).max()
    c = np.array([circ(R, Q, pi) for R in W])
    De = np.array([circ(R, Q, pi) - circ(th(R), Q, pi) for R in W])
    F = pi[:, None] * Q; dfct = np.abs(F - F.T).max(); dd[d] = dfct
    print(f"          {lab:7s}  {eq:.2e}      {pe:.2e}     {np.abs(c).max():.4e}      {np.abs(De).max():.2e}      {dfct:.3e}")
    assert eq < 1e-12 and pe < 1e-12, "Theta-equivariance failed -- the theorem would be false"
    assert np.abs(De).max() < 1e-12, "a splitting appeared -- would contradict A4"
    assert np.abs(c).max() > 1e-8, "circulations vanished -- instrument blind, result unreadable"

print(f"A6  DB-defect log-slope 0.1->0.2: {np.log(dd[0.2]/dd[0.1])/np.log(2):.4f}; "
      f"0.05->0.1: {np.log(dd[0.1]/dd[0.05])/np.log(2):.4f}   (0689/TARROW-2: delta^3)")
print("\nVERDICT: Theta is an exact improper symmetry of Mechanism A at every delta. The helicity is")
print("Theta-odd. Therefore NO functional of the Mechanism-A NESS can split the two states -- the")
print("splitting is identically zero, not small. Mechanism A breaks T, not P. It is NOT the chirality")
print("source. 4066's 'cheaper candidate route' is REFUTED.")
