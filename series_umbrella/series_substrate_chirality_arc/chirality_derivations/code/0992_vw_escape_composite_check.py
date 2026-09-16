"""0992 -- PD-008 attack on 0985: does a P-odd AND Moment-odd composite rescue the VW route?

Three structural checks on a generic finite Markov chain (exact linear algebra, no sampling).
They hold for ANY chain; the toy is generic on purpose (the claims are not 600-cell specific).

  C1  |E[exp(i lam X)]| <= 1 for ANY real path observable X of ANY chain, reversible or not.
      => the positivity half of Vafa-Witten costs nothing on a classical substrate and uses no RP;
         the whole content sits in 'the physical source is a phase' (H1', VW-1 Rmk 6.3).
  C2  A real source on the same X obeys Jensen: E[exp(lam X)] >= exp(lam <X>)  (opposite sign to VW).
  C3  The Moment-odd composite  K = g_sym(x_t, x_{t+1}) * j(x_t, x_{t+1})   (g_sym symmetric,
      j antisymmetric) has <K> = 0 EXACTLY on a reversible (detailed-balance) chain, for every g, j,
      and <K> != 0 once an antisymmetric cycle perturbation delta breaks detailed balance.
      => where VW-2 Thm A supplies Theta_OS positivity (detailed balance) the composite is
         identically unsourced; where it is nonzero, detailed balance -- and Thm A -- is gone.
"""
import numpy as np

rng = np.random.default_rng(992)
N = 7

def chain(delta):
    # reversible part: symmetric conductances on the complete graph, pi uniform
    C = rng_C.copy()
    # antisymmetric cycle perturbation on the ring 0->1->...->N-1->0 (keeps uniform pi stationary:
    # it is a divergence-free circulation, so column sums are unchanged)
    A = np.zeros((N, N))
    for k in range(N):
        A[k, (k + 1) % N] += delta
        A[(k + 1) % N, k] -= delta
    W = C + A                     # rates, W[x,y] = rate x->y
    assert (W[~np.eye(N, dtype=bool)] > 0).all()
    np.fill_diagonal(W, 0.0)
    P = W / W.sum(1).max()        # uniformized one-Moment kernel
    P += np.diag(1.0 - P.sum(1))
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(abs(w - 1))]); pi /= pi.sum()
    return P, pi

rng_C = rng.uniform(0.5, 1.5, (N, N)); rng_C = 0.5 * (rng_C + rng_C.T)
g = rng.normal(size=(N, N)); g = 0.5 * (g + g.T)           # symmetric (Moment-even) factor
j = rng.normal(size=(N, N)); j = 0.5 * (j - j.T)           # antisymmetric (Moment-odd) current
h = g * j                                                   # the composite, per transition

def db_violation(P, pi):
    F = pi[:, None] * P
    return np.abs(F - F.T).max()

def mean_K(P, pi):
    return float((pi[:, None] * P * h).sum())

def char_fn(P, pi, lam, T, X, phase=True):
    M = P * (np.exp(1j * lam * X) if phase else np.exp(lam * X))
    v = pi.astype(complex)
    for _ in range(T):
        v = v @ M
    return v.sum()

print("delta   DB-violation     <K>            |E e^{i lam X}|  E e^{lam X}  e^{lam T<K>}")
for delta in ["0", "0.05", "0.1", "0.2"]:
    d = float(delta); assert str(d) == str(float(delta))
    P, pi = chain(d)
    K = mean_K(P, pi)
    T, lam = 6, 0.8
    cf = abs(char_fn(P, pi, lam, T, h, phase=True))
    re = char_fn(P, pi, lam, T, h, phase=False).real
    jb = np.exp(lam * T * K)
    print(f"{delta:5s}  {db_violation(P, pi):.3e}   {K:+.6e}   {cf:.6f}       {re:.6f}     {jb:.6f}")
    assert cf <= 1 + 1e-12, "C1 failed"                 # holds reversible or not
    assert re >= jb - 1e-12, "C2 failed"                # Jensen, real source
    if d == 0.0:
        assert db_violation(P, pi) < 1e-12 and abs(K) < 1e-14, "C3 failed at delta=0"
    else:
        assert db_violation(P, pi) > 1e-6 and abs(K) > 1e-8, "C3: composite did not switch on"

# odd in delta: the composite is sourced by the T-arrow itself
Kp = mean_K(*chain(0.1)); Km = mean_K(*chain(-0.1))
print(f"<K>(+0.1) = {Kp:+.6e}, <K>(-0.1) = {Km:+.6e}, sum = {Kp+Km:+.1e}")
assert abs(Kp + Km) < 1e-12, "composite not odd in delta"
print("C1, C2, C3 PASS")
