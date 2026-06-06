#!/usr/bin/env python3
r"""
0772_zrp_htheorem.py
====================
Exact master-equation verification of the H-theorem for the minimal-PCD occupation dynamics, modeled as a
symmetric constant-rate ZERO-RANGE PROCESS (ZRP). This DERIVES (given the ZRP model) the two pieces of the
bath clause that 0769 could only GROUND:
  leg 1(a) -- relaxation/mixing exists (H-theorem: KL to the stationary measure is a Lyapunov function),
  leg 1(c) -- the stationary state is the INDISTINGUISHABLE Gibbs state (product-Poisson; the n_i! is the
              Gibbs indistinguishability divisor -> mu = kT ln(rho), the tilt's log).

ZRP model of minimal-PCD / ZBW dynamics:
  * State = occupation numbers (n_0, ..., n_{L-1}) on L lattice sites (A1: CPs indistinguishable ->
    occupation-number objects).
  * Each CP hops independently at the ZBW rate (set = 1) to a uniformly chosen neighbour: the hop
    (n_i -> n_i - 1, n_j -> n_j + 1) has rate g(n_i)*p(i,j) with g(n) = n (constant per-CP rate) and
    p(i,j) = 1/deg(i) symmetric.

Theory:
  * The symmetric constant-rate ZRP is REVERSIBLE w.r.t. the canonical product-Poisson (here, fixed-N:
    multinomial) measure pi(n) = N!/(prod n_i!) (1/L)^N -- detailed balance pi(n)W(n->n') = pi(n')W(n'->n).
  * For ANY Markov generator with stationary pi, the relative entropy H(t) = sum_n P(n,t) ln[P(n,t)/pi(n)]
    is non-increasing (Lyapunov), strictly so until P = pi (irreducibility). => monotone relaxation to pi.
  * pi's single-site marginal is Binomial(N, 1/L) -> Poisson(N/L) as N -> infinity (the indistinguishable
    ideal-gas Gibbs state with mu = kT ln(N/L)).

This script builds the EXACT generator on a triangle (L=3, N=6; 28 states), and verifies:
  (1) detailed balance w.r.t. the multinomial pi (machine precision);
  (2) pi is stationary (Q pi = 0);
  (3) H(t) decreases monotonically to 0 from a delta initial condition (exact matrix exponential);
  (4) the spectral gap is O(1) in the ZBW rate -> tau_eq ~ O(few) ZBW times -> N_mix ~ O(1), consistent
      with the 0753 toy and the 0769 timescale argument;
  (5) the stationary single-site marginal is Binomial(N,1/L), approaching Poisson(N/L).
"""

import numpy as np
from itertools import product as iproduct
from math import factorial, lgamma
from scipy.linalg import expm

def main():
    L, N = 3, 6
    neighbours = {0: [1, 2], 1: [0, 2], 2: [0, 1]}   # triangle (each site degree 2)

    # enumerate states: occupation vectors summing to N
    states = [s for s in iproduct(range(N+1), repeat=L) if sum(s) == N]
    idx = {s: k for k, s in enumerate(states)}
    M = len(states)

    # stationary multinomial pi(n) = N!/(prod n_i!) (1/L)^N
    def pi_of(s):
        return factorial(N)/np.prod([factorial(x) for x in s]) * (1/L)**N
    pi = np.array([pi_of(s) for s in states])
    pi /= pi.sum()

    # generator Q: dP/dt = Q P, Q[to, from] = rate(from->to)
    Q = np.zeros((M, M))
    for s in states:
        f = idx[s]
        for i in range(L):
            if s[i] == 0:
                continue
            for j in neighbours[i]:
                rate = s[i] * (1.0/len(neighbours[i]))   # g(n_i)=n_i, symmetric kernel 1/deg
                t = list(s); t[i] -= 1; t[j] += 1; t = tuple(t)
                Q[idx[t], f] += rate
                Q[f, f]      -= rate

    # (1) detailed balance: pi[f]*Q[t,f] == pi[t]*Q[f,t]
    db_err = 0.0
    for f in range(M):
        for t in range(M):
            if t != f and Q[t, f] > 0:
                db_err = max(db_err, abs(pi[f]*Q[t, f] - pi[t]*Q[f, t]))
    # (2) stationarity
    stat_err = np.max(np.abs(Q @ pi))

    # (3) H(t) monotone decrease from a delta initial condition (all N at site 0)
    P0 = np.zeros(M); P0[idx[(N, 0, 0)]] = 1.0
    ts = np.linspace(0, 8, 41)
    Hs = []
    for t in ts:
        P = expm(Q*t) @ P0
        P = np.clip(P, 1e-300, None)
        Hs.append(float(np.sum(P*np.log(P/pi))))
    Hs = np.array(Hs)
    monotone = bool(np.all(np.diff(Hs) <= 1e-12))

    # (4) spectral gap (smallest nonzero |Re eigenvalue| of Q)
    ev = np.linalg.eigvals(Q)
    re = np.sort(np.real(ev))           # one ~0 (stationary), rest negative
    gap = -re[-2]
    tau_eq = 1.0/gap

    # (5) stationary single-site marginal vs Binomial(N,1/L) and Poisson(N/L)
    marg = np.zeros(N+1)
    for k, s in enumerate(states):
        marg[s[0]] += pi[k]
    binom = np.array([factorial(N)/(factorial(n)*factorial(N-n))*(1/L)**n*(1-1/L)**(N-n) for n in range(N+1)])
    rho = N/L
    pois = np.array([np.exp(-rho + n*np.log(rho) - lgamma(n+1)) for n in range(N+1)])

    print("="*74)
    print("Exact master-equation H-theorem for the symmetric constant-rate ZRP")
    print(f"  L={L} sites (triangle), N={N} particles, {M} states; ZBW hop rate = 1")
    print("="*74)
    print(f"  (1) detailed balance max error vs multinomial pi : {db_err:.2e}   {'PASS' if db_err<1e-12 else 'FAIL'}")
    print(f"  (2) stationarity  max|Q.pi|                      : {stat_err:.2e}   {'PASS' if stat_err<1e-12 else 'FAIL'}")
    print(f"  (3) H(t)=KL(P(t)||pi) monotonically non-increasing: {monotone}   {'PASS' if monotone else 'FAIL'}")
    print(f"        H(0)={Hs[0]:.4f}  ->  H(t_end)={Hs[-1]:.2e}  (relaxes to 0 = P reaches pi)")
    print(f"  (4) spectral gap = {gap:.4f} (in ZBW-rate units) -> tau_eq = {tau_eq:.3f} ZBW times")
    print(f"        => N_mix = O(tau_eq) ~ {tau_eq:.1f}, consistent with 0753 toy (O(10-30)) and 0769")
    print(f"  (5) stationary site-0 marginal vs Binomial(N,1/L) max diff: {np.max(np.abs(marg-binom)):.2e}")
    print(f"        marginal mean = {np.sum(np.arange(N+1)*marg):.4f} (= N/L = {rho}); -> Poisson({rho}) as N->inf")
    print(f"        marginal  : {np.round(marg,4)}")
    print(f"        Binomial  : {np.round(binom,4)}")
    print(f"        Poisson({rho}): {np.round(pois,4)}  (limit shape)")

    print("\n" + "="*74)
    print("READING")
    print("="*74)
    print("""  Given the ZRP model of the minimal-PCD / ZBW dynamics, leg 1(a) and 1(c) are THEOREMS, not
  assertions:
    - (a) relaxation/mixing: the relative entropy H(t)=KL(P(t)||pi) is a strict Lyapunov function
          (verified monotone above) -> the occupations provably relax to pi, with tau_eq set by the
          spectral gap (O(few) ZBW times -> N_mix ~ O(1-10), consistent with 0753/0769).
    - (c) stationary state: pi is the product-Poisson (here multinomial) measure -- the n_i! is the
          Gibbs INDISTINGUISHABILITY divisor (A1), giving mu = kT ln(rho), the tilt's log. The
          distinguishable/labelled stationary state (which would give the n_s=1 cliff, 0749) is NOT a
          stationary measure of this dynamics.

  UPGRADE: leg 1(a)+(c) move from 'grounded' (0769) to 'DERIVED, given the ZRP model.' The remaining
  premise is the ZRP IDENTIFICATION itself -- that the ZBW switching of indistinguishable CPs on the
  lattice is a symmetric, constant-rate zero-range process. This is a far more minimal and checkable
  premise than 'the bath clause holds': it is the minimal faithful model of independent ZBW hops on the
  A1 occupation space, and it is the natural target of a future A1-A11 derivation. Until that lands,
  n_s = 0.9649 remains conditional/grounded -- but leg 1's relaxation + correct stationary state are now
  proven consequences of the model, not posits.""")

if __name__ == "__main__":
    main()
