#!/usr/bin/env python
"""Patch 3111 -- THE MEMORYLESS CAMPAIGN (prereg: 3110, committed before
this file existed). Instrument per R-CP-MEMORYLESS: first-order,
X += SSV_net fresh each Moment, nothing carried; no velocity variable;
no brake; continuous positions. Read-outs: the 3104 S3 definitions
verbatim. No band quantity anywhere."""
import numpy as np

GQ = 52.94


def run(ds, seed=5, mixed=True, T=3000, sig_n=0.30, n_side=3):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np
    L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0)
    X = X + rng.normal(0, 0.3, X.shape)          # symmetry-breaking seed offsets
    q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    pair_q = (np.arange(Np) % 2 == 1) if mixed else np.zeros(Np, bool)
    Gcp = np.repeat(np.where(pair_q, GQ, 1.0), 2)
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    Disp = np.zeros((Nc, 3))                     # previous displacement (FIELD content)
    ptr = np.zeros(Nc, dtype=int)
    qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool); opp = (qq < 0)
    sws = 0; regen = 0
    prev_sup = np.ones(Np, bool)
    idx = np.arange(Nc)
    dp_hist = np.zeros((T-1, Np))
    cent_snaps = []
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6
        rs = np.where(co, 1.0, r); re = np.maximum(rs, 1.0)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        F = np.einsum('ij,ijk->ik', kern, D)
        # arc term: sources carry previous displacement, clipped at c (field)
        nv = np.sqrt(np.einsum('ij,ij->i', Disp, Disp))
        Vc = Disp / np.maximum(nv, 1.0)[:, None]
        rhat = D / rs[:, :, None]
        Bk = np.where(co, 0.0, 1.0/re**2)[:, :, None] * \
             np.cross(Vc[None, :, :] * q[None, :, None], rhat)
        np.einsum('iik->ik', Bk)[:] = 0.0
        B = Bk.sum(axis=1)
        Fmag = q[:, None]*np.cross(Vc, B)        # first-order arc contribution
        F = F + Fmag
        for i in range(Nc):
            p = partner[i]
            dv = D[i, p]; rr = r[i, p]
            if not co[i, p]:
                F[i] -= qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
            tr = min(ptr[i], t-1)
            def gap(tt):
                w = X[i] - Hist[tt, p]; w -= L*np.round(w/L)
                return np.sqrt(w@w)
            while tr+1 <= t-1 and (t-(tr+1)) >= gap(tr+1):
                tr += 1
            while tr >= 0 and (t-tr) < gap(tr):
                tr -= 1
            ptr[i] = max(tr, 0)
            if tr >= 0:
                w = X[i] - Hist[tr, p]; w -= L*np.round(w/L)
                s = np.sqrt(w@w)
                if s > 1e-9:
                    F[i] += Gcp[i]*qq[i, p]/(max(s, 1.0)**2 * s) * w
        # jitter field, charge-coupled (R-DWELL-1 semantics)
        fld = rng.normal(0, sig_n, (Nc, 3))
        near = r[idx, partner] < 1.0
        for i in np.where(near)[0]:
            if i < partner[i]:
                fld[partner[i]] = fld[i]
        F = F + q[:, None]*fld
        # MEMORYLESS STEP: displacement = SSV_net, nothing carried
        Disp = F.copy()
        X = (X + F) % L
        Hist[t] = X
        # swaps: founder perigee rule
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc):
            ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[idx, j_star]; d_par = r[idx, partner]
        want = (d_new < d_par) & (d_new < ds/2.0)
        done = np.zeros(Nc, bool)
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]:
                continue
            m, kk = partner[i], partner[j]
            if done[m] or done[kk] or len({i, j, m, kk}) < 4:
                continue
            partner[i], partner[j] = j, i
            partner[m], partner[kk] = kk, m
            done[[i, j, m, kk]] = True; sws += 1
        pi = np.arange(0, Nc, 2); dp = r[pi, partner[pi]]
        dp_hist[t-1] = dp
        sup = dp < 1.0
        regen += int(np.sum(sup & ~prev_sup))
        prev_sup = sup
        if t >= 2*T//3 and (t % (T//10) == 0):
            cent = X[pi] + 0.5*(X[partner[pi]] - X[pi]
                                - L*np.round((X[partner[pi]] - X[pi])/L))
            cent_snaps.append((cent % L).copy())
    th = (T-1)//3
    W = dp_hist[2*th:]
    Wmid = dp_hist[th:2*th]
    eq = ~pair_q if mixed else np.ones(Np, bool)
    qm = pair_q
    We, Wq = W[:, eq], W[:, qm]
    gas_e = We > ds/2.0
    r_gas = float(gas_e.mean())
    gas_q = Wq > ds/2.0 if mixed and qm.any() else np.zeros((1, 1), bool)
    tot_gas = gas_e.sum() + (gas_q.sum() if mixed else 0)
    x_q = float(gas_q.sum()/tot_gas) if tot_gas > 0 else float('nan')
    eta_gas = float((We**2)[gas_e].mean()/ds**2) if gas_e.any() else float('nan')
    bnd_e = We[We <= ds/2.0]
    bnd_q = Wq[Wq <= ds/2.0] if (mixed and qm.any()) else np.array([])
    s_meas = float((bnd_q**2).mean()/(bnd_e**2).mean()) if bnd_q.size and bnd_e.size else float('nan')
    aC4 = float('nan')
    if cent_snaps:
        vals = []
        for C in cent_snaps:
            Ce = C[eq]; n = len(Ce)
            Dm = Ce[:, None, :] - Ce[None, :, :]; Dm -= L*np.round(Dm/L)
            r2m = np.einsum('ijk,ijk->ij', Dm, Dm)
            np.fill_diagonal(r2m, np.inf)
            S4m = float(np.mean(np.sum(r2m**-2, axis=1)))
            S4f = 25.3382*((n/L**3)/np.sqrt(2.0))**(4.0/3.0)
            vals.append(S4m/S4f)
        aC4 = float(np.mean(vals))
    eta_all = float((We**2).mean()/ds**2)
    stat = (We**2).mean()/max((Wmid**2).mean(), 1e-12)
    phase = ("FAITHFUL" if (eta_all < 1.2 and regen >= 5 and 0.5 < stat < 2.0)
             else "FROZEN-SUP" if (eta_all < 1e-3 and regen == 0)
             else "GLASS" if regen < 5 else "OTHER")
    return dict(r=r_gas, xq=x_q, eta_gas=eta_gas, s=s_meas, aC4=aC4,
                eta_e=float((bnd_e**2).mean()/ds**2) if bnd_e.size else float('nan'),
                eta_all=eta_all, regen=regen, sws=sws, phase=phase, stat=float(stat))


if __name__ == "__main__":
    print("=== MEMORYLESS CAMPAIGN (prereg 3110) ===")
    print(f"{'cell':>4} {'ds':>4} {'seed':>5} {'phase':>10} {'r':>7} {'x_q':>6} "
          f"{'eta_gas':>8} {'s_meas':>9} {'a_C4':>7} {'eta_e':>7} {'stat':>5} {'regen':>6}")
    cells = [("M1", 8, 5, True), ("M2", 8, 11, True), ("M3", 12, 5, True),
             ("MB1", 3, 5, False), ("MB2", 5, 5, False), ("MB3", 7, 5, False)]
    for nm, ds, sd, mx in cells:
        z = run(ds, seed=sd, mixed=mx)
        print(f"{nm:>4} {ds:4d} {sd:5d} {z['phase']:>10} {z['r']:7.4f} "
              f"{z['xq']:6.3f} {z['eta_gas']:8.3f} {z['s']:9.5f} {z['aC4']:7.3f} "
              f"{z['eta_e']:7.4f} {z['stat']:5.2f} {z['regen']:6d}")
    print("\nRead-outs feed the F-CLI-2 successor assembly per prereg 3110 S4.")
