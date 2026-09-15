#!/usr/bin/env python3
"""0988 (chirality lane) -- EXACT-RATE Theta_OS PROBE on 4022's toy measure. TODO-0988-CHIR.

Question. 0983 computed the OS time-reflection pairing  S(t) = sym( Pi * exp(2 t Q) )  for the
single-walker [PCD-EXT] generator on the 600-cell and found min eig S = -3.5e-15 at delta = 0.35,
t = 1, stable from 30 to 50 digits -- but from FLOAT-precision rates. Is that a signal or float input?
This script builds the rates EXACTLY in Q[phi] (mpmath at DPS digits, coordinates snapped to
{0, 1/2, 1, phi/2, 1/(2 phi)}) and repeats the computation. It needs ~10-20 min per case on one core
(mp.expm and mp.eigsy at 120x120, DPS 30); claude.ai containers kill it at 5 min. RUN ON Kila6.

Run:   python 0988_theta_os_exact_probe.py            # all cases below, results to 0988_results.txt
       python 0988_theta_os_exact_probe.py 0.35 1 30  # one case: delta t dps
Deps:  numpy, mpmath (pure wheels; fine on Kila6's no-MSVC Python 3.12).

Decision rule (pre-committed, 0988):
  * |min eig| < 1e-(DPS-6) at DPS 30 AND at DPS 45  -> ZERO: the -3.5e-15 was float input; the
    single-time necessary condition for VW-a-4 HOLDS on the toy at every tested (delta, t).
  * min eig < -1e-12 and stable across DPS               -> NEGATIVE: a necessary condition for
    Theta_OS positivity fails on the SINGLE-WALKER toy at that (delta, t). A toy result, [PCD-EXT];
    it says nothing about H1 on the DSL measure and moves no verdict. File as a finding, then scope.
  Anything else -> report the numbers, claim nothing.
"""
import sys, time, math, numpy as np
from itertools import permutations as P
import mpmath as mp

def build600():
    phi = (1 + 5 ** .5) / 2
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi / 2, 1 / 2, 1 / (2 * phi), 0]
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                sg = [b[0] * s1, b[1] * s2, b[2] * s3, b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i + 1, 4) if pm[i] > pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

def run(delta, t, dps):
    mp.mp.dps = dps
    V = build600(); N = len(V)
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    ph = (1 + mp.sqrt(5)) / 2; em = 1 / ph
    E = [(i, j) for i in range(N) for j in range(i + 1, N) if abs(D[i, j] - float(em)) < 1e-9]
    assert N == 120 and len(E) == 720
    cands = [mp.mpf(0), mp.mpf(1) / 2, mp.mpf(1), ph / 2, 1 / (2 * ph)]
    def snap(x):
        s = -1 if x < 0 else 1; a = abs(x)
        c = min(cands, key=lambda z: abs(float(z) - a)); assert abs(float(c) - a) < 1e-9; return s * c
    Vm = [[snap(x) for x in v] for v in V]
    d = mp.mpf(delta); tt = mp.mpf(t)
    Q = mp.zeros(N, N)
    for i, j in E:                       # n-hat = (1,0,0,0): the n-hat-FIXING sector of Theta = diag(1,1,1,-1)
        c = (Vm[j][0] - Vm[i][0]) / em
        Q[i, j] = 1 + d * c; Q[j, i] = 1 - d * c
    for i in range(N): Q[i, i] = -sum(Q[i, k] for k in range(N) if k != i)
    t0 = time.time()
    A = Q.T.copy()
    for j in range(N): A[N - 1, j] = 1
    p = mp.lu_solve(A, mp.matrix([0] * (N - 1) + [1]))          # exact stationary law
    M = mp.expm(Q * (2 * tt))
    for i in range(N):
        for j in range(N): M[i, j] *= p[i]
    S = (M + M.T) / 2
    ev = sorted(mp.eigsy(S)[0][i] for i in range(N))
    line = (f"delta={delta} t={t} dps={dps}  min eig={mp.nstr(ev[0], 8)}  2nd={mp.nstr(ev[1], 8)}  "
            f"max={mp.nstr(ev[-1], 8)}  min p={mp.nstr(min(p), 6)}  secs={time.time() - t0:.0f}")
    print(line, flush=True)
    return line

if __name__ == "__main__":
    if len(sys.argv) == 4:
        run(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
    else:
        cases = [(0.35, 1.0, 30), (0.35, 1.0, 45), (0.0, 1.0, 30), (0.10, 1.0, 30),
                 (0.35, 2.0, 30), (0.35, 0.5, 30), (0.20, 1.0, 30)]
        with open("0988_results.txt", "a") as f:
            for c in cases:
                f.write(run(*c) + "\n"); f.flush()
