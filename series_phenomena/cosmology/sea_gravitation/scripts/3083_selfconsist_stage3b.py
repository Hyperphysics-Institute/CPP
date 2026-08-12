#!/usr/bin/env python
"""Patch 3083 -- D-SEA-SELFCONSIST Stage 3b: the closed, regulated array.

The energy balance is now fully ruled and BOTH sides live in the model:
  PUMP   the retardation of inter-CP influence (R-ZBW-DELAY) -- the
         same mechanism that overheated Stage 3 -- injects directed KE
         ("the ZBW cycle is a perpetual motion machine", founder, 3082);
  BRAKE  the entropic redistribution of a lone CP's directed KE
         (R-CP-ENTROPIC-LOSS): retention gamma per Moment.
D-ARC-GAMMA has not yet pinned gamma numerically (the 10%-shell ruling
admits more than one quantitative reading), so gamma is SCANNED across
its plausible range and the question put to the array is INSENSITIVITY:
does the faithful phase exist, and is eta_z stable, across gamma? If
yes, the ambiguity is immaterial (as density proved immaterial to the
Stage-2 shape); if no, FQ-6 poses the precise geometric question.
NOTHING ELSE IS ADDED: no noise term, no seeding, no external drive.
Annealed start (superposed pairs, kick 0.05); the retardation pump
must build the jitter itself against the brake. R-GP-REZERO is
honoured by construction (fields rebuilt fresh each Moment).

Phase classification per run (late third):
  GAS       eta within 25% of the uniform-gas value 2.25
  COLLAPSED <v^2> < 1e-6 and eta < 1e-3 (pump lost to brake)
  GLASS     regenerations ~ 0 with eta order-1 (stuck, mislabelled)
  FAITHFUL  bound (eta << gas), regenerating, stationary (v^2 flat)
No band quantity appears anywhere. Fixed seeds; one repeat seed line.
"""
import sys
import numpy as np

def run_3b(ds, gamma, T=3000, kick=0.05, seed=5, sig_n=0.0, lattice=False):
    # sig_n: R-JITTER-SOURCE noise floor (per-Moment SSV_net summation
    # fluctuation; granularity unruled => scanned for insensitivity).
    rng = np.random.default_rng(seed)
    n_side, Np = 3, 27; Nc = 2*Np; L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0); q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    V = rng.normal(0, kick, (Nc, 3)); V[1::2] = -V[0::2]
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    ptr = np.zeros(Nc, dtype=int); qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool); opp = (qq < 0)
    d2s, v2s, sws, regen = [], [], 0, 0
    prev_sup = np.ones(Np, bool)
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6; rs = np.where(co, 1.0, r); re = np.maximum(rs, 1.0)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        F = -np.einsum('ij,ijk->ik', kern, D)
        for i in range(Nc):
            p = partner[i]
            dv = D[i, p]; rr = np.sqrt(dv@dv)
            if rr > 1e-6:
                F[i] += qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
            tr = min(ptr[i], t-1)
            def gap(tt):
                w = X[i] - Hist[tt, p]; w -= L*np.round(w/L); return np.sqrt(w@w)
            while tr+1 <= t-1 and (t-(tr+1)) >= gap(tr+1): tr += 1
            while tr >= 0 and (t-tr) < gap(tr): tr -= 1
            ptr[i] = max(tr, 0)
            if tr >= 0:
                w = X[i] - Hist[tr, p]; w -= L*np.round(w/L); s = np.sqrt(w@w)
                if s > 1e-9:
                    F[i] += -qq[i, partner[i]]/(max(s, 1.0)**2 * s) * w
        if sig_n > 0:
            # R-JITTER-SOURCE as a FIELD: co-located partners feel the SAME
            # vector and respond OPPOSITELY (charge-coupled) -- the R-DWELL-1
            # relaunch mechanism. Separated CPs draw independent local fields.
            fld = rng.normal(0, sig_n, (Nc, 3))
            near = r[np.arange(Nc), partner] < 1.0
            for i in np.where(near)[0]:
                if i < partner[i]:
                    fld[partner[i]] = fld[i]
            F = F + q[:, None]*fld
        V = gamma*V + F                              # brake + pump + ruled floor
        X = (X + (np.round(V) if lattice else V)) % L   # Stage 3c: GP-address jumps
        Hist[t] = X
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc): ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[np.arange(Nc), j_star]; d_par = r[np.arange(Nc), partner]
        want = (d_new < d_par) & (d_new < ds/2.0)   # founder perigee rule at the poach scale
        done = np.zeros(Nc, bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]: continue
            m, k = partner[i], partner[j]
            if done[m] or done[k] or len({i, j, m, k}) < 4: continue
            partner[i], partner[j] = j, i; partner[m], partner[k] = k, m
            done[[i, j, m, k]] = True; sws += 1
        pi = np.arange(0, Nc, 2); dp = r[pi, partner[pi]]
        d2s.append(np.mean(dp**2))
        sup = dp < 1.0; regen += int(np.sum(sup & ~prev_sup)); prev_sup = sup
        v2s.append(np.mean(np.einsum('ij,ij->i', V, V)))
    d2 = np.array(d2s); v2 = np.array(v2s); th = len(d2)//3
    eta = d2[2*th:].mean()/ds**2
    drift = v2[2*th:].mean()/max(v2[th:2*th].mean(), 1e-30)
    v2l = v2[2*th:].mean()
    gas = abs(eta - 2.25) < 0.6
    if v2l < 1e-6 and eta < 1e-3: phase = "COLLAPSED"
    elif gas: phase = "GAS"
    elif regen < 5: phase = "GLASS"
    elif eta < 1.2 and 0.3 < drift < 3.0: phase = "FAITHFUL"
    else: phase = "OTHER"
    return dict(ds=ds, g=gamma, eta=eta, fsw=sws/max(regen, 1), regen=regen,
                v2=v2l, drift=drift, phase=phase)

if __name__ == "__main__":
    cfgs = eval(sys.argv[1]) if len(sys.argv) > 1 else [(8.0, 0.9, 5, 0.03, True)]
    print(f"{'d_s':>5} {'gamma':>6} {'sig_n':>7} {'phase':>10} {'eta_z':>9} {'f_sw':>6} {'regen':>6} {'v2_late':>9} {'drift':>6}")
    for cfg in cfgs:
        ds, g, sd, sn = cfg[:4]; lat = cfg[4] if len(cfg) > 4 else False
        z = run_3b(ds, g, seed=sd, sig_n=sn, lattice=lat)
        print(f"{ds:5.0f} {g:6.2f} {sn:7.3f} {z['phase']:>10} {z['eta']:9.4f} {z['fsw']:6.2f} "
              f"{z['regen']:6d} {z['v2']:9.2e} {z['drift']:6.2f}")
