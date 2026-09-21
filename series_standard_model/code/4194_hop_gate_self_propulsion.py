#!/usr/bin/env python3
"""4194 — first falsifier for the hop gate q(e.A): does a free, spin-polarised CP drift along its spin?

Corpus inputs (c03): the CP executes a deterministic 12-edge step EVERY tick, choosing the edge that
maximises e_k . V; and V at the CP's GP always carries the DP Sea's ZBW fluctuation, a continuous
rapidly varying vector of amplitude sigma. So (i) exact ties in e_k . V have measure zero, and (ii) a
free particle at rest is V_org = 0 plus isotropic noise.

Always-on gate: choose k maximising  e_k . (V + kappa q A).  Because the score is LINEAR in V, this is
IDENTICAL to the ungated rule in an extra uniform field  kappa q A  -- an electric-like field pointing
along the particle's own spin. The Monte Carlo below only puts a number on the resulting drift.
"""
import numpy as np
rng = np.random.default_rng(4194)
phi = (1 + 5 ** 0.5) / 2
E = np.array([(0, s1, s2 * phi) for s1 in (1, -1) for s2 in (1, -1)]
             + [(s1, s2 * phi, 0) for s1 in (1, -1) for s2 in (1, -1)]
             + [(s2 * phi, 0, s1) for s1 in (1, -1) for s2 in (1, -1)], float)
E /= np.linalg.norm(E, axis=1)[:, None]                     # the 12 icosahedral neighbour directions

N = 400_000
noise = rng.normal(size=(N, 3))                             # isotropic ZBW noise, sigma = 1 per component
ties = np.mean(np.sort(noise @ E.T, axis=1)[:, -1] == np.sort(noise @ E.T, axis=1)[:, -2])
print(f"fraction of ticks with an exact tie in e.V (tie-only gate fires): {ties:.1e}\n")

print("always-on gate, free CP at rest (V_org = 0), spin along three inequivalent lattice directions")
print(f"{'kappa/sigma':>12s} {'drift/c along A: 5-fold':>24s} {'3-fold':>10s} {'2-fold':>10s} {'drift/(kappa/sigma)':>20s}")
axes = {'5': E[0], '3': (E[0] + E[4] + E[8]), '2': (E[0] + E[1])}
for k in (1e-3, 1e-2, 1e-1, 1.0):
    out = []
    for a in axes.values():
        a = a / np.linalg.norm(a)
        hop = E[np.argmax((noise + k * a) @ E.T, axis=1)]   # q = +1; q = -1 mirrors the sign
        anti = E[np.argmax((-noise + k * a) @ E.T, axis=1)] # antithetic pair: cancels the noise's own mean
        out.append(0.5 * (hop @ a).mean() + 0.5 * (anti @ a).mean())
    print(f"{k:12.0e} {out[0]:24.5f} {out[1]:10.5f} {out[2]:10.5f} {np.mean(out)/k:20.3f}")
