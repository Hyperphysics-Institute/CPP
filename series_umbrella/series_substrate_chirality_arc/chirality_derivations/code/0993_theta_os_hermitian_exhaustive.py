"""0993 (chirality lane) -- PD-008 critique of 0991: is Theta_OS reflection positivity of the tilted
Mechanism-A single-walker measure decided WITHOUT the real-symmetric probe?

VW-2 Thm A writes the RP pairing sesquilinearly on L^2(pi):  <Theta(conj A) A> = <A, T A>_pi.
For single-time A at Moment +t and its reflection at -t this is  F(z) = z^dagger M z,  M = Pi exp(2tQ).
0983/0988/0991 test only S = sym(M) (the real subalgebra). Hermitian positivity also needs F real, i.e.
K = antisym(M) = 0 -- unless Theta carries an internal involution J. The automorphisms of the single-time
observable algebra C^120 are the vertex permutations; supp(Qhat) = supp(Q) (pi > 0), so a J with
pi(J.) = pi and J Q J^T = Qhat = Pi^-1 Q^T Pi must be a 600-cell graph automorphism. H4 (order 14400)
is therefore EXHAUSTIVE. This script:
  E1  builds H4 as vertex permutations (closure of the 60 root reflections), asserts |H4| = 14400;
  E2  at delta = 0, confirms J = id works (Thm A) -- the check can find a J when one exists;
  E3  at delta in {phi^-3, 0.35, 0.1, 0.05}: counts J in H4 with J pi = pi and J Q J^T = Qhat;
  E4  reports ||K|| for M at t = 1 and a complex witness Im F(z) / ||z||^2, far above float error;
  E5  scaling of the detailed-balance defect ||Pi Q - (Pi Q)^T|| in delta (TARROW-2: O(delta^3)).
Float64 suffices: every tested quantity is >= 1e-9, not the 1e-15 tail the 0988 probe had to resolve.
"""
import numpy as np, itertools
from scipy.linalg import expm
phi = (1 + 5 ** .5) / 2

def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1, s2, s3 in itertools.product((1, -1), repeat=3):
        sg = [b[0] * s1, b[1] * s2, b[2] * s3, b[3]]
        for pm in itertools.permutations(range(4)):
            if sum(1 for i in range(4) for j in range(i + 1, 4) if pm[i] > pm[j]) % 2 == 0:
                Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = build600(); N = len(V); assert N == 120
em = 1 / phi
D = np.linalg.norm(V[:, None] - V[None], axis=2)
E = [(i, j) for i in range(N) for j in range(i + 1, N) if abs(D[i, j] - em) < 1e-9]; assert len(E) == 720

def perm_of(Mx):
    W = V @ Mx.T
    idx = np.argmin(np.linalg.norm(W[:, None] - V[None], axis=2), axis=1)
    assert np.allclose(W, V[idx], atol=1e-9); return tuple(idx)

# E1: H4 by closure of root reflections (roots = vertices)
gens = []
seen_axes = set()
for v in V:
    key = tuple(np.round(np.abs(v) * np.sign(v[np.nonzero(np.round(v, 9))[0][0]]), 9))
    if key in seen_axes: continue
    seen_axes.add(key)
    gens.append(np.array(perm_of(np.eye(4) - 2 * np.outer(v, v))))
ident = tuple(range(N)); G = {ident}; frontier = [np.array(ident)]
while frontier:
    new = []
    for g in frontier:
        for s in gens:
            h = tuple(g[s])
            if h not in G: G.add(h); new.append(np.array(h))
    frontier = new
print(f"E1  |H4| = {len(G)}  (root reflections used: {len(gens)})"); assert len(G) == 14400
Gs = np.array(sorted(G))

def Qmat(d):
    Q = np.zeros((N, N))
    for i, j in E:
        c = (V[j, 0] - V[i, 0]) / em
        Q[i, j] = 1 + d * c; Q[j, i] = 1 - d * c
    Q -= np.diag(Q.sum(1)); return Q

def stat(Q):
    A = Q.T.copy(); A[-1] = 1
    return np.linalg.solve(A, np.r_[np.zeros(N - 1), 1])

def J_count(d):
    Q = Qmat(d); p = stat(Q); Qh = (Q.T * p[None, :]) / p[:, None]   # Qhat_ij = p_j Q_ji / p_i
    ok = inv = 0
    for g in Gs:
        if np.abs(p[g] - p).max() > 1e-11: continue
        if np.abs(Q[np.ix_(g, g)] - Qh).max() < 1e-10:
            ok += 1; inv += int(np.all(g[g] == np.arange(N)))
    return ok, inv, Q, p

ok0, inv0, Q0, p0 = J_count(0.0)
print(f"E2  delta=0: {ok0} automorphisms satisfy J Q J^T = Qhat (involutions {inv0}); identity among them: "
      f"{np.abs(Q0 - (Q0.T * p0[None,:]) / p0[:,None]).max() < 1e-12}")
assert ok0 >= 1

print("E3/E4  delta        #J(all)  #J(invol)  ||K(t=1)||_2     Im F witness    DB defect ||PiQ-(PiQ)^T||")
defects = {}
for lab, d in [("phi^-3", phi ** -3), ("0.35", 0.35), ("0.1", 0.1), ("0.05", 0.05)]:
    ok, inv, Q, p = J_count(d)
    M = p[:, None] * expm(2 * Q)
    K = (M - M.T) / 2
    s = np.linalg.svd(K, compute_uv=False)[0]
    # witness: z = (a + i b)/sqrt2 from the top singular pair of K gives Im(z^H M z) = a^T K b = s
    Uk, Sk, Vk = np.linalg.svd(K); a, b = Uk[:, 0], Vk[0]
    z = (a + 1j * b) / np.sqrt(2)
    imF = np.imag(np.conj(z) @ M @ z)
    F = p[:, None] * Q; dfct = np.abs(F - F.T).max(); defects[d] = dfct
    print(f"       {lab:7s}  {ok:7d}  {inv:9d}   {s:.6e}   {imF:+.6e}   {dfct:.6e}")
    assert ok == 0, "a rescuing involution exists -- RP not refuted by this route"
    fl = 1e3 * np.finfo(float).eps * np.abs(M).sum(1).max() * N   # generous float floor for expm on 120x120
    print(f"       float floor {fl:.1e}; |Im F|/floor = {abs(imF)/fl:.1e}")
    assert abs(imF) > fl, "witness not resolved above float floor (floor already carries a 1e3 margin)"
ds = [0.05, 0.1]
print(f"E5  DB-defect log-slope 0.05->0.1: {np.log(defects[0.1]/defects[0.05])/np.log(2):.4f}  (TARROW-2: 3)")
print("E1-E5 PASS: at every tested delta != 0 no H4 involution rescues the Hermitian pairing; Im F != 0.")
