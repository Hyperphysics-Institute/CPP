#!/usr/bin/env python3
"""0988/0989 (chirality lane) -- EXACT-RATE Theta_OS PROBE on 4022's toy measure. TODO-0988-CHIR.

0989 REVISION (after run 1 on Kila6, results in 0988_results_kila6_run1.txt):
  * delta and t are now parsed from STRINGS (mp.mpf("0.35") = 7/20 exactly). Run 1 passed Python
    floats, so delta carried the binary value 0.35 - 2.2e-17. Hygiene, NOT the cause of run 1's
    -3.5e-15: |d lambda_min / d delta| <= ||Pi|| 2t ||dQ/d delta|| ~ 0.25, so that input error moves
    lambda_min by < 1e-17. The dps-30/45 invariance means the value was EXACTLY RESOLVED.
  * Run 1 showed the 0988 thresholds were mis-sized: the spectrum's genuine tail is
    ~ p_min * exp(-2 t lambda_max(Q)) ~ 1e-16 at t=1 (delta=0 returns exactly that), so a ZERO
    criterion of 1e-24 and a NEGATIVE criterion of 1e-12 were both unreachable. Run 1 therefore
    adjudicates as "report, claim nothing" under the 0988 rule, and that verdict STANDS for run 1.
  * The script now prints the ARITHMETIC FLOOR per case: floor = max_eig * 10^(2 - dps).
  * NEW PRE-COMMITTED RULE (0989, fixed before run 2):
      NEGATIVE : lambda_min < -1e6 * floor at dps 30, AND lambda_min agrees to 6 significant digits
                 across dps 30 / 45 / 60.
      ZERO     : |lambda_min| < 1e3 * floor at every dps run.
      else     : report, claim nothing.
    Run 2 cases: (0.35, 1), (0.35, 2), (0.35, 0.75) at dps 30, 45, 60. Nine runs, ~20-40 min each.
  * RUN 2 RESULT (0991): NEGATIVE at (0.35,1) and (0.35,2), 8-digit stable across 30/45/60 digits,
    |min/floor| ~ 1e15; resolved POSITIVE at (0.35, 0.75). See 0989_results_kila6_run2.txt. (Filed at 0991, the slot reserved for it.)
  * RUN 3 WITHDRAWN AT 0993 -- DO NOT RUN. VW-a-4 at the physical bias is decided without it: the Hermitian
    OS pairing fails at every tested delta != 0 and no H4 involution rescues it (code/0993_theta_os_hermitian_exhaustive.py).
    The real-symmetric sign this script computes is consumed by no theorem. Original run-3 text follows.
  * RUN 3 (0991, rule unchanged): delta = phi^-3 (the physical bias, 0966) at t = 1, 2, 4; plus 0.25
    and 0.30 at t = 1 to bracket the sign change. Token "phi-3" is exact in Q[phi]. Eight runs.
    A NEGATIVE verdict is a TOY result: the single-time OS pairing of the single-walker [PCD-EXT]
    measure goes negative at large tilt and longer separation. It says nothing about H1 on the DSL
    measure (VW-2 Thm A already needs detailed balance at delta=0) and moves no verdict.


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
    # 0991: delta may be the token 'phi-3' = phi^-3 (the registered physical bias, 0966) -- exact in Q[phi]
    d = (1 / ph) ** 3 if str(delta) == 'phi-3' else mp.mpf(str(delta)); tt = mp.mpf(str(t))
    if str(delta) == "0.35": assert d == mp.mpf(7) / 20
    if str(delta) == "0.75": assert d == mp.mpf(3) / 4
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
    floor = ev[-1] * mp.mpf(10) ** (2 - dps)
    line = (f"delta={delta} t={t} dps={dps}  min eig={mp.nstr(ev[0], 8)}  2nd={mp.nstr(ev[1], 8)}  "
            f"max={mp.nstr(ev[-1], 8)}  floor={mp.nstr(floor, 3)}  min/floor={mp.nstr(ev[0] / floor, 4)}  "
            f"min p={mp.nstr(min(p), 6)}  secs={time.time() - t0:.0f}")
    print(line, flush=True)
    return line

if __name__ == "__main__":
    if len(sys.argv) == 4:
        run(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        # 0991 RUN 3 (rule unchanged from 0989): the PHYSICAL bias delta = phi^-3 ~ 0.236, which sits between
        # run 1's positive delta=0.2 and negative delta=0.35 at t=1. Results to 0991_results.txt.
        cases = [("phi-3", "1", 30), ("phi-3", "1", 45), ("phi-3", "2", 30), ("phi-3", "2", 45),
                 ("phi-3", "4", 30), ("phi-3", "4", 45), ("0.25", "1", 30), ("0.30", "1", 30)]
        with open("0991_results.txt", "a") as f:
            for c in cases:
                f.write(run(*c) + "\n"); f.flush()
