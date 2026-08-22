#!/usr/bin/env python
"""Patch 3120+ -- D-DS-INDEP CAMPAIGN (prereg: 3119, committed before
this file existed). NO COSMOLOGICAL QUANTITY appears anywhere in this
file: the outputs are order-parameter curves, susceptibility peaks,
and (at >= 3 sizes) an extrapolated transition spacing. Nothing else.

Instrument: the 3111 memoryless core VERBATIM dynamics, instrumented
with (a) executed-swap counting in the stationary window (rho_swap =
2*ops/(Np*T_w): each executed swap re-partners exactly two pairs) and
(b) state snapshots (pair centres + bound indicator) for xi_state.

Usage:
  python 3120_ds_indep_campaign.py run <n_side> <seed> <ds1> [ds2 ...]
  python 3120_ds_indep_campaign.py analyze
State accumulates in /tmp/3120_state.json across invocations.
"""
import sys, os, json
import numpy as np

SIG_N = 0.30
T = 3000
STATE = "/tmp/3121_state.json"  # v2 state; v1 retained at /tmp/3120_state.json


def run(ds, n_side, seed, r_soft=1.0, drive=None, probe=False):
    rng = np.random.default_rng(seed)
    Np = n_side**3; Nc = 2*Np
    L = n_side*ds
    grid = np.array([[i, j, k] for i in range(n_side) for j in range(n_side)
                     for k in range(n_side)], float)*ds + ds/2
    X = np.repeat(grid, 2, axis=0) + rng.normal(0, 0.3, (Nc, 3))
    q = np.tile([1.0, -1.0], Np)
    partner = np.arange(Nc); partner[0::2] += 1; partner[1::2] -= 1
    pair_q = (np.arange(Np) % 2 == 1)
    Gcp = np.repeat(np.where(pair_q, 52.94, 1.0), 2)
    Hist = np.zeros((T, Nc, 3)); Hist[0] = X
    Disp = np.zeros((Nc, 3))
    ptr = np.zeros(Nc, dtype=int)
    qq = np.outer(q, q)
    eye = np.eye(Nc, dtype=bool); opp = (qq < 0)
    idx = np.arange(Nc)
    dp_hist = np.zeros((T-1, Np))
    swap_ops = np.zeros(T-1, dtype=int)
    snaps = []
    th = (T-1)//3
    _amb = []
    for t in range(1, T):
        D = X[:, None, :] - X[None, :, :]; D -= L*np.round(D/L)
        r = np.sqrt(np.einsum('ijk,ijk->ij', D, D)); np.fill_diagonal(r, 1.0)
        co = r < 1e-6
        # r_soft: the Coulomb softening radius (Patch 3152 -- parameterized
        # for the commensuration test; DEFAULT 1.0 is the historical value,
        # so every prior result is bit-identical).
        rs = np.where(co, 1.0, r); re = np.maximum(rs, r_soft)
        kern = np.where(co, 0.0, qq/(re**2 * rs))
        F = np.einsum('ij,ijk->ik', kern, D)
        nv = np.sqrt(np.einsum('ij,ij->i', Disp, Disp))
        Vc = Disp / np.maximum(nv, 1.0)[:, None]
        rhat = D / rs[:, :, None]
        Bk = np.where(co, 0.0, 1.0/re**2)[:, :, None] * \
             np.cross(Vc[None, :, :] * q[None, :, None], rhat)
        np.einsum('iik->ik', Bk)[:] = 0.0
        B = Bk.sum(axis=1)
        F = F + q[:, None]*np.cross(Vc, B)
        # --- retarded partner term, VECTORIZED (declared instrument
        # optimization, Patch 3121: identical arithmetic per element;
        # bit-identity regression vs the part-1 state REQUIRED) -------
        P = partner
        qp = qq[idx, P]
        dvp = D[idx, P]; rrp = r[idx, P]; cop = co[idx, P]
        F -= np.where(cop, 0.0, qp/(np.maximum(rrp, 1.0)**2 * rrp))[:, None] * dvp
        tr = np.minimum(ptr, t-1)
        # advance to fixpoint
        for _ in range(64):
            cand = tr + 1
            ok = cand <= t-1
            cc = np.where(ok, cand, 0)
            w = X - Hist[cc, P]; w -= L*np.round(w/L)
            g = np.sqrt(np.einsum('ij,ij->i', w, w))
            adv = ok & ((t - cand) >= g)
            if not adv.any():
                break
            tr = np.where(adv, cand, tr)
        # retreat to fixpoint
        for _ in range(64):
            ok = tr >= 0
            cc = np.where(ok, tr, 0)
            w = X - Hist[cc, P]; w -= L*np.round(w/L)
            g = np.sqrt(np.einsum('ij,ij->i', w, w))
            ret = ok & ((t - tr) < g)
            if not ret.any():
                break
            tr = np.where(ret, tr - 1, tr)
        ptr[:] = np.maximum(tr, 0)
        use = tr >= 0
        cc = np.where(use, tr, 0)
        w = X - Hist[cc, P]; w -= L*np.round(w/L)
        s = np.sqrt(np.einsum('ij,ij->i', w, w))
        good = use & (s > 1e-9)
        coef = np.where(good, Gcp*qp/(np.maximum(s, 1.0)**2 * np.where(s > 1e-9, s, 1.0)), 0.0)
        F += coef[:, None] * w
        # Patch 3179 (Phase B): 'drive' replaces the Gaussian surrogate with
        # the computed arrival samples when provided; DEFAULT None leaves this
        # line byte-identical (same RNG draw) -- B-1 gate verifies.
        if drive is None:
            fld = rng.normal(0, SIG_N, (Nc, 3))
        else:
            fld = drive[t % len(drive)]
        near = r[idx, partner] < 1.0
        for i in np.where(near)[0]:
            if i < partner[i]:
                fld[partner[i]] = fld[i]
        F = F + q[:, None]*fld
        Disp = F.copy()
        X = (X + F) % L
        Hist[t] = X
        # Patch 3179: diagnostic probe -- the ambient NON-PARTNER Coulomb
        # field (the 3138 sigma_ambient statistic), sampled sparsely in the
        # final third; no RNG, no dynamics touched.
        if probe and t >= 2*th and (t % 10) == 0:
            wp = X[:,None,:]-X[None,:,:]; wp -= L*np.round(wp/L)
            sp = np.sqrt(np.einsum('ijk,ijk->ij', wp, wp)); np.fill_diagonal(sp, np.inf)
            for _i in range(Nc): sp[_i, partner[_i]] = np.inf
            cf = qq/(np.maximum(sp,1.0)**2*np.where(sp>1e-9,sp,1.0))
            _amb.append((cf[:,:,None]*wp).sum(1))
        ro = np.where(opp & ~eye, r, np.inf)
        for i in range(Nc):
            ro[i, partner[i]] = np.inf
        j_star = np.argmin(ro, axis=1)
        d_new = ro[idx, j_star]; d_par = r[idx, partner]
        want = (d_new < d_par) & (d_new < ds/2.0)
        done = np.zeros(Nc, bool)
        ops = 0
        for i in np.where(want)[0]:
            j = j_star[i]
            if done[i] or done[j]:
                continue
            m, kk = partner[i], partner[j]
            if done[m] or done[kk] or len({i, j, m, kk}) < 4:
                continue
            partner[i], partner[j] = j, i
            partner[m], partner[kk] = kk, m
            done[[i, j, m, kk]] = True; ops += 1
        swap_ops[t-1] = ops
        pi = np.arange(0, Nc, 2)
        dp_hist[t-1] = r[pi, partner[pi]]
        if t >= 2*th and (t % (T//10) == 0):
            dvec = X[partner[pi]] - X[pi]; dvec -= L*np.round(dvec/L)
            cent = (X[pi] + 0.5*dvec) % L
            snaps.append((cent.copy(), (dp_hist[t-1] <= ds/2.0).copy()))
    # ---- order parameters (stationary window = final third) ---------
    W = dp_hist[2*th:]
    Wmid = dp_hist[th:2*th]
    if probe and _amb:
        _A = np.concatenate(_amb, 0)
        sig_amb = float(_A.std(axis=0).mean())
    else:
        sig_amb = None
    f_b = float((W <= ds/2.0).mean())
    rho_swap = float(2.0*swap_ops[2*th:].sum()/(Np*(T-1-2*th)))
    f_dwell = float((W < 1.0).mean())
    # xi_state from snapshots
    xis = []
    for cent, b in snaps:
        db = b.astype(float) - b.mean()
        Dm = cent[:, None, :] - cent[None, :, :]; Dm -= L*np.round(Dm/L)
        rm = np.sqrt(np.einsum('ijk,ijk->ij', Dm, Dm))
        iu = np.triu_indices(Np, 1)
        rr_, cc_ = rm[iu], (db[:, None]*db[None, :])[iu]
        bins = np.arange(0.0, L/2 + 1.0, 1.0)
        prof = []
        for a, bb in zip(bins[:-1], bins[1:]):
            m = (rr_ >= a) & (rr_ < bb)
            if m.sum() >= 3:
                prof.append(((a+bb)/2, float(cc_[m].mean())))
        if not prof:
            continue
        C0 = prof[0][1]
        if C0 <= 0:
            xis.append(None); continue
        target = C0/np.e
        xi = None
        for (r1, c1), (r2, c2) in zip(prof, prof[1:]):
            if c1 >= target > c2:
                xi = r1 + (c1-target)*(r2-r1)/max(c1-c2, 1e-12)
                break
        xis.append(xi)
    xis_def = [x for x in xis if x is not None]
    xi_state = float(np.mean(xis_def)) if xis_def else None
    stat = float((W**2).mean()/max((Wmid**2).mean(), 1e-12))
    eta_all = float((W**2).mean()/ds**2)
    regen = int(((dp_hist[2*th:] < 1.0) & ~np.vstack([np.ones((1, Np), bool),
                 dp_hist[2*th:-1] < 1.0])).sum())
    phase = ("FAITHFUL" if (eta_all < 1.2 and regen >= 5 and 0.5 < stat < 2.0)
             else "OTHER")
    # --- ADDITIVE instrumentation (Patch 3147, CONV-021-mandated): the
    # per-Moment bound-fraction series over the same final-third window,
    # giving the Binder moments. NO dynamics, RNG draws, or existing
    # outputs are touched -- every prior key is bit-identical. -----------
    fb_t = (W <= ds/2.0).mean(axis=1)          # per-Moment bound fraction
    m1 = float(fb_t.mean()); dm = fb_t - m1
    m2 = float((dm**2).mean()); m4 = float((dm**4).mean())
    binder = float(1.0 - m4/(3.0*m2**2)) if m2 > 1e-15 else None
    return dict(f_b=f_b, rho_swap=rho_swap, f_dwell=f_dwell,
                xi_state=xi_state, r=1.0-f_b, phase=phase, stat=stat,
                m2=m2, m4=m4, binder=binder, sig_amb=sig_amb)


def peak(dss, vals):
    """Susceptibility peak: argmax |dP/d(ds)|, central differences +
    quadratic 3-pt interpolation; edge -> UNBRACKETED (None)."""
    dss = np.array(dss); vals = np.array(vals, float)
    d = np.gradient(vals, dss)
    a = np.abs(d)
    i = int(np.argmax(a))
    if i == 0 or i == len(dss)-1:
        return None
    x0, x1, x2 = dss[i-1], dss[i], dss[i+1]
    y0, y1, y2 = a[i-1], a[i], a[i+1]
    den = (y0 - 2*y1 + y2)
    if abs(den) < 1e-12:
        return float(x1)
    return float(x1 + 0.5*(y0 - y2)/den * (x1 - x0))


if __name__ == "__main__":
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    if sys.argv[1] == "run":
        n_side, seed = int(sys.argv[2]), int(sys.argv[3])
        for ds in [float(x) for x in sys.argv[4:]]:
            key = f"{n_side}:{ds}:{seed}"
            if key in st:
                continue
            z = run(ds, n_side, seed)
            st[key] = z
            json.dump(st, open(STATE, "w"))
            xi = f"{z['xi_state']:.2f}" if z['xi_state'] else "UNDEF"
            print(f"  n={n_side} ds={ds} seed={seed}: f_b={z['f_b']:.4f} "
                  f"rho_swap={z['rho_swap']:.4f} f_dwell={z['f_dwell']:.4f} "
                  f"xi={xi} phase={z['phase']} stat={z['stat']:.2f}")
    else:
        print("=== D-DS-INDEP ANALYSIS (prereg 3119 rules; no cosmology) ===")
        sizes = sorted({int(k.split(":")[0]) for k in st})
        results = {}
        for n in sizes:
            dss = sorted({float(k.split(":")[1]) for k in st
                          if k.startswith(f"{n}:")})
            print(f"\n-- n_side = {n} (N = {n**3} pairs) --")
            print(f"{'ds':>5} {'f_b':>8} {'rho_swap':>9} {'f_dwell':>8} {'xi':>6} {'r':>7} {'phase':>9}")
            curves = {p: [] for p in ("f_b", "rho_swap", "f_dwell", "xi_state")}
            for ds in dss:
                cells = [st[k] for k in st if k.startswith(f"{n}:{ds}:")]
                m = {p: np.mean([c[p] for c in cells if c[p] is not None])
                     if any(c[p] is not None for c in cells) else None
                     for p in curves}
                for p in curves:
                    curves[p].append(m[p])
                xi = f"{m['xi_state']:.2f}" if m['xi_state'] else "UNDEF"
                rmean = np.mean([c["r"] for c in cells])
                ph = "/".join(sorted({c["phase"][:5] for c in cells}))
                print(f"{ds:5.1f} {m['f_b']:8.4f} {m['rho_swap']:9.4f} "
                      f"{m['f_dwell']:8.4f} {xi:>6} {rmean:7.4f} {ph:>9}")
            results[n] = {}
            for p in ("f_b", "rho_swap", "f_dwell", "xi_state"):
                vals = curves[p]
                if any(v is None for v in vals):
                    results[n][p] = None
                    print(f"   d*({p}) = UNDEFINED (missing values)")
                    continue
                pk = peak(dss, vals)
                results[n][p] = pk
                print(f"   d*({p}, n={n}) = "
                      f"{'UNBRACKETED (edge)' if pk is None else f'{pk:.3f}'}")
        if len(sizes) >= 3:
            print("\n-- EXTRAPOLATION (linear in 1/n_side) --")
            outs = []
            for p in ("f_b", "rho_swap", "f_dwell", "xi_state"):
                pts = [(1.0/n, results[n][p]) for n in sizes
                       if results[n].get(p) is not None]
                if len(pts) >= 3:
                    x, y = zip(*pts)
                    b, a = np.polyfit(x, y, 1)
                    outs.append((p, float(a)))
                    print(f"   d*({p}, inf) = {a:.3f}")
                else:
                    print(f"   d*({p}, inf): insufficient defined sizes")
            if outs:
                vals = [v for _, v in outs]
                spread = max(vals) - min(vals)
                verdict = "SPLIT (panel adjudicates)" if spread > 0.75 else \
                          f"d_s* = {np.mean(vals):.3f} +/- {spread/2:.3f}"
                print(f"\n   CAMPAIGN OUTPUT: {verdict}  (spread {spread:.3f})")
        else:
            print("\n[extrapolation waits: fewer than 3 sizes complete]")
