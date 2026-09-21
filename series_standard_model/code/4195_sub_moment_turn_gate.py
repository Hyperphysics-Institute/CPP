#!/usr/bin/env python3
"""4195 — exploration of the founder's sub-Moment transit picture (founders_voice/4195_*).

Picture: within ONE Moment the CP walks edge-by-edge through many GPs from its origin GP to the END GP
THAT V_i HAS ALREADY FIXED; at each GP on the way the next GP is chosen by a binary gate that consults
the register's axial vector A. Because the endpoint is fixed by V, the net displacement per Moment is
untouched whatever the gate does -- 4194's self-propulsion argument does not reach this configuration.

Candidates at each GP: the K neighbours best aligned with the REMAINING displacement (so the walk always
closes on the endpoint). Gates compared:
  none   : uniform random choice among the candidates (control)
  toward : take the candidate most aligned with A            score = e . A            (4193's term)
  turn   : take the candidate that turns counter-clockwise   score = (e_prev x e) . A
           about A relative to the hop just made
Measured: endpoint miss; h = mean (e_k x e_k+1).D_hat  (the walk's screw sense about its own travel);
bow = mean lateral offset of the track, resolved along A_perp and along D_hat x A.
Mirror test: reflect D (polar) and A (axial) in a lattice mirror plane, rerun, and compare with the
reflected original track. 'same' means the rule is parity-symmetric; 'DIFFERENT' means it violates P.
"""
import numpy as np
phi = (1 + 5 ** 0.5) / 2
E = np.array([(0, a, b * phi) for a in (1, -1) for b in (1, -1)]
             + [(a, b * phi, 0) for a in (1, -1) for b in (1, -1)]
             + [(b * phi, 0, a) for a in (1, -1) for b in (1, -1)], float)
E /= np.linalg.norm(E, axis=1)[:, None]
unit = lambda v: v / np.linalg.norm(v)

def walk(D, A, gate, K, seed=0, first=None):
    rng = np.random.default_rng(seed)
    x, prev, track = np.zeros(3), first, [np.zeros(3)]
    for _ in range(int(4 * np.linalg.norm(D)) + 50):
        R = D - x
        if np.linalg.norm(R) < 0.75: break
        cand = np.argsort(E @ unit(R))[-K:]
        if gate == 'none' or (gate == 'turn' and prev is None): k = rng.choice(cand)
        elif gate == 'toward': k = cand[np.argmax(E[cand] @ A)]
        else:                  k = cand[np.argmax(np.cross(prev, E[cand]) @ A)]
        prev = E[k]; x = x + prev; track.append(x.copy())
    return np.array(track)

def measures(tr, D, A):
    e = np.diff(tr, axis=0); Dh = unit(D)
    h = np.mean(np.cross(e[:-1], e[1:]) @ Dh)
    lat = tr - np.outer(tr @ Dh, Dh)
    Ap = A - (A @ Dh) * Dh
    bA = lat.mean(0) @ unit(Ap) if np.linalg.norm(Ap) > 1e-9 else 0.0
    DxA = np.cross(Dh, A)
    bX = lat.mean(0) @ unit(DxA) if np.linalg.norm(DxA) > 1e-9 else 0.0
    return np.linalg.norm(tr[-1] - D), h, bA, bX

rng = np.random.default_rng(4195)
M = np.diag([-1.0, 1.0, 1.0])                                     # x -> -x, a mirror plane of the 12-shell
NDIR, L = 60, 300                                                 # 60 random travel directions, 300 hops each
dirs = [unit(v) for v in rng.normal(size=(NDIR, 3))]
perps = [unit(np.cross(d, rng.normal(size=3))) for d in dirs]
spin = {'A parallel to travel': lambda d, p: d, 'A anti-parallel': lambda d, p: -d, 'A perpendicular': lambda d, p: p}

print(f"averages over {NDIR} random travel directions, {L} hops each; +/- is the standard error")
print(f"{'gate':7s} {'K':>2s} {'spin':22s} {'miss':>5s} {'screw h':>16s} {'bow along A_perp':>18s} {'bow along DxA':>16s}  mirror image obeys the rule")
for gate in ('none', 'toward', 'turn'):
    for K in (2, 3):
        for name, f in spin.items():
            rows, same = [], 0
            for d, p in zip(dirs, perps):
                D, A = L * d, f(d, p)
                rows.append(measures(walk(D, A, gate, K, 1), D, A))
                if gate != 'none':
                    tr = walk(D, A, gate, K, 0, first=E[0])
                    trm = walk(M @ D, -(M @ A), gate, K, 0, first=M @ E[0])   # axial: A -> det(M) M A
                    same += tr.shape == trm.shape and np.allclose(tr @ M.T, trm, atol=1e-9)
            r = np.array(rows); m, se = r.mean(0), r.std(0) / np.sqrt(NDIR)
            v = '(control)' if gate == 'none' else f"{same}/{NDIR}"
            print(f"{gate:7s} {K:2d} {name:22s} {m[0]:5.2f} {m[1]:8.4f}+/-{se[1]:.4f} {m[2]:10.2f}+/-{se[2]:5.2f} {m[3]:9.2f}+/-{se[3]:5.2f}  {v}")
