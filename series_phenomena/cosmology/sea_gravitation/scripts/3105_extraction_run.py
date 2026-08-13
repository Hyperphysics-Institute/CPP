#!/usr/bin/env python
"""Patch 3105 -- THE CONSOLIDATED EXTRACTION RUN (prereg: Patch 3104,
extraction_run_prereg.md; committed BEFORE this file was written).

Instrument: the 3088 arc-force lattice array core, verbatim except the
preregistered extensions:
  (i)  mixed species -- per-pair bond stiffness Gp (e-class 1.0,
       q-class 52.94), applied to the RETARDED PARTNER attraction only
       (strong bond partner-internal; inter-pair forces electric);
  (ii) |V| <= 1 GP/Moment saturation (DECLARED INSTRUMENT
       REGULARIZATION per prereg S1; FQ-9.1 rides);
  (iii) per-Moment pair-separation retention for the six frozen
       read-outs (prereg S3).
Gates (3088 verbatim): one-step sign/magnitude exact + resolved orbit.
A failed gate voids everything below it. No band quantity anywhere.
"""
import numpy as np

GQ = 52.94   # q-class bond stiffness (k^2, Patch 3103)


def clip_rows(V):
    n = np.sqrt(np.einsum('ij,ij->i', V, V))
    return V / np.maximum(n, 1.0)[:, None]


# ---------------- gates: 3088 verbatim ------------------------------
def _pair_eb(X, V, q):
    d = X[0] - X[1]; s = np.linalg.norm(d)
    se = max(s, 1.0); rhat = d/s
    E = np.zeros((2, 3))
    E[0] = q[0]*q[1]*d/(se**2*s)
    E[1] = -E[0]
    Vc = clip_rows(V)
    B = np.zeros((2, 3))
    B[0] = q[1]*np.cross(Vc[1],  rhat)/se**2
    B[1] = q[0]*np.cross(Vc[0], -rhat)/se**2
    return E, B


def check_signs():
    X = np.array([[2., 0., 0.], [-2., 0., 0.]])
    V = np.array([[0., 0.2, 0.], [0., -0.2, 0.]])
    q = np.array([1.0, -1.0])
    E, B = _pair_eb(X, V, q)
    Fm = q[0]*np.cross(V[0], B[0])
    want = np.array([-0.04/16.0, 0.0, 0.0])
    return bool(np.allclose(Fm, want))


def check_orbit(a=6.0, T=60000):
    v = np.sqrt(1.0/(4*a - 1.0))
    X = np.array([[a, 0., 0.], [-a, 0., 0.]])
    V = np.array([[0., v, 0.], [0., -v, 0.]])
    q = np.array([1.0, -1.0])
    encs, rads = [], []
    for t in range(T):
        E, B = _pair_eb(X, V, q)
        vm = V + 0.5*E
        tvec = 0.5*q[:, None]*B
        t2 = np.einsum('ij,ij->i', tvec, tvec)[:, None]
        vp = vm + np.cross(vm + np.cross(vm, tvec), 2*tvec/(1.0+t2))
        V = vp + 0.5*E
        X = X + V
        sep = np.linalg.norm(X[0] - X[1])
        rads.append(sep/2)
        encs.append(0.5*np.einsum('ij,ij->', V, V) - 1.0/max(sep, 1.0))
    r = np.array(rads); e = np.array(encs)
    return abs(e[-100:].mean() - e[:100].mean()) < 1e-4 and abs(r[-100:].mean() - r[:100].mean()) < 0.5


# ---------------- the extended array (3088 core + extensions) --------
def run(ds, gamma, T=3000, kick=0.05, seed=5, sig_n=0.30, mixed=True,
        n_side=3):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np
    L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0)
    q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    # species: alternate pairs q-class/e-class for spatial mixing
    pair_species_q = (np.arange(Np) % 2 == 1) if mixed else np.zeros(Np, bool)
    Gp_pair = np.where(pair_species_q, GQ, 1.0)
    Gcp = np.repeat(Gp_pair, 2)               # per-CP bond stiffness
    V = rng.normal(0, kick, (Nc, 3)); V[1::2] = -V[0::2]
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    VHist = np.zeros((T, Nc, 3))
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
        E = np.einsum('ij,ijk->ik', kern, D)
        Vc = clip_rows(V)
        rhat = D / rs[:, :, None]
        Bk = np.where(co, 0.0, 1.0/re**2)[:, :, None] * \
             np.cross(Vc[None, :, :] * q[None, :, None], rhat)
        np.einsum('iik->ik', Bk)[:] = 0.0
        B = Bk.sum(axis=1)
        for i in range(Nc):
            p = partner[i]
            dv = D[i, p]; rr = r[i, p]
            if not co[i, p]:
                E[i] -= qq[i, p]/(max(rr, 1.0)**2 * rr) * dv
                B[i] -= q[p]*np.cross(clip_rows(V[p][None])[0],
                                      dv/rr)/max(rr, 1.0)**2
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
                    # EXTENSION (i): strong bond partner-internal x Gcp
                    E[i] += Gcp[i]*qq[i, p]/(max(s, 1.0)**2 * s) * w
                    vp_ret = clip_rows(VHist[tr, p][None])[0]
                    B[i] += q[p]*np.cross(vp_ret, w/s)/max(s, 1.0)**2
        if sig_n > 0:
            fld = rng.normal(0, sig_n, (Nc, 3))
            near = r[idx, partner] < 1.0
            for i in np.where(near)[0]:
                if i < partner[i]:
                    fld[partner[i]] = fld[i]
            E = E + q[:, None]*fld
        vm = V + 0.5*E
        tvec = 0.5*q[:, None]*B
        t2 = np.einsum('ij,ij->i', tvec, tvec)[:, None]
        vp = vm + np.cross(vm + np.cross(vm, tvec), 2*tvec/(1.0+t2))
        V = gamma*(vp + 0.5*E)
        V = clip_rows(V)                      # EXTENSION (ii): |V| <= 1
        if not np.all(np.isfinite(V)):
            return None
        VHist[t-1] = V
        X = (X + np.round(V)) % L
        Hist[t] = X
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
    # ---------- frozen read-outs (prereg S3), stationary window ------
    th = (T-1)//3
    W = dp_hist[2*th:]
    eq = ~pair_species_q if mixed else np.ones(Np, bool)
    qm = pair_species_q
    We, Wq = W[:, eq], W[:, qm]
    gas_e = We > ds/2.0
    r_gas = float(gas_e.mean())
    gas_q = Wq > ds/2.0 if mixed and qm.any() else np.zeros((1, 1), bool)
    tot_gas = gas_e.sum() + (gas_q.sum() if mixed else 0)
    x_q = float(gas_q.sum()/tot_gas) if tot_gas > 0 else float('nan')
    eta_gas = float((We**2)[gas_e].mean()/ds**2) if gas_e.any() else float('nan')
    bnd_e = We[We <= ds/2.0]; bnd_q = Wq[Wq <= ds/2.0] if mixed else np.array([1.0])
    s_meas = float((bnd_q**2).mean()/(bnd_e**2).mean()) if mixed and bnd_q.size and bnd_e.size else float('nan')
    # arrangement: e-class centres, periodic S4 vs FCC at matched density
    aC4 = float('nan')
    if cent_snaps:
        vals = []
        for C in cent_snaps:
            Ce = C[eq]
            n = len(Ce)
            Dm = Ce[:, None, :] - Ce[None, :, :]; Dm -= L*np.round(Dm/L)
            r2m = np.einsum('ijk,ijk->ij', Dm, Dm)
            np.fill_diagonal(r2m, np.inf)
            S4m = float(np.mean(np.sum(r2m**-2, axis=1)))
            dens = n/L**3
            S4f = 25.3382*(dens/np.sqrt(2.0))**(4.0/3.0)
            vals.append(S4m/S4f)
        aC4 = float(np.mean(vals))
    eta_e_bound = float((bnd_e**2).mean()/ds**2) if bnd_e.size else float('nan')
    # phase classification (3088, on e-class)
    eta_all = float((We**2).mean()/ds**2)
    phase = ("FAITHFUL" if (eta_all < 1.2 and regen >= 5) else
             "FROZEN-SUP" if (eta_all < 1e-3 and regen == 0) else
             "GLASS" if regen < 5 else "OTHER")
    return dict(r=r_gas, xq=x_q, eta_gas=eta_gas, s=s_meas, aC4=aC4,
                eta_e=eta_e_bound, eta_all=eta_all, regen=regen,
                sws=sws, phase=phase,
                se_r=float(gas_e.mean(axis=0).std()/np.sqrt(max(eq.sum(),1))))


if __name__ == "__main__":
    print("GATE 1 (one-step sign/magnitude):", "PASS" if check_signs() else "FAIL")
    ok2 = check_orbit()
    print("GATE 2 (resolved orbit a=6):    ", "PASS" if ok2 else "FAIL")
    assert check_signs() and ok2, "GATE FAILED — run void"

    print("\n=== EXTRACTION CELLS (prereg S2) ===")
    print(f"{'cell':>4} {'ds':>4} {'g':>5} {'seed':>5} {'phase':>10} {'r':>7} {'x_q':>6} "
          f"{'eta_gas':>8} {'s_meas':>9} {'a_C4':>6} {'eta_e':>7} {'regen':>6}")
    cells = [("E1", 8, 0.80, 5, True), ("E2", 8, 0.90, 11, True),
             ("E3", 12, 0.85, 5, True),
             ("B1", 5, 0.85, 5, False), ("B2", 6, 0.85, 5, False),
             ("B3", 7, 0.85, 5, False)]
    res = {}
    for nm, ds, g, sd, mx in cells:
        z = run(ds, g, seed=sd, mixed=mx)
        res[nm] = z
        if z is None:
            print(f"{nm:>4} OVERFLOW"); continue
        print(f"{nm:>4} {ds:4d} {g:5.2f} {sd:5d} {z['phase']:>10} {z['r']:7.4f} "
              f"{z['xq']:6.3f} {z['eta_gas']:8.3f} {z['s']:9.5f} {z['aC4']:6.3f} "
              f"{z['eta_e']:7.4f} {z['regen']:6d}")
    print("\nBoundary verdict (B-cells, e-class 3D): FAITHFUL attainability by d_s above.")
    print("Read-outs feed the single assembly per the prereg use commitments;")
    print("s_meas carries the |V|<=1 regularization flag (FQ-9.1). No band quantity.")
