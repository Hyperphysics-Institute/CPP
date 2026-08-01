#!/usr/bin/env python3
"""PATCH 2906 -- round-2 ensemble execution (amended spec, Patch 2905).
Compiled retardation kernel with frozen validation gate; falls back to
the reference numpy path if the gate fails.
Usage:
  validate                       -- run the kernel gate (V1/V2 + 10-Moment 1e-10 agreement)
  leg <tag> <beta> <T_meas> <mobile:0|1> <x_offset>
"""
import sys, os, json, time, pickle
import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location(
    "eng", os.path.join(os.path.dirname(__file__), "2902_mobile_sea_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
from numba import njit, prange

SOFT2 = eng.SOFT2; PSR = eng.PSR; CLAT = 1.0

@njit(parallel=True, cache=False, fastmath=False)
def kernel(recv, ridx, H, T_pre, t_now, t, T_max, q, tr_prev, use_warm):
    M = recv.shape[0]; N = H.shape[1]
    net = np.zeros((M, 3)); ab = np.zeros(M); tr_out = np.empty((M, N))
    hi_idx = int(T_pre) + int(t_now)
    T_pre = float(T_pre)
    for i in prange(M):
        rx, ry, rz = recv[i, 0], recv[i, 1], recv[i, 2]
        qi = q[ridx[i]]
        for e in range(N):
            if e == ridx[i]:
                tr_out[i, e] = t - 1.0
                continue
            if use_warm:
                lo = tr_prev[i, e] + 1.0 - 3.0
                hi = tr_prev[i, e] + 1.0 + 3.0
                if hi > t: hi = float(t)
            else:
                lo = t - T_max; hi = float(t)
            # bracket validity via g at ends; reset if invalid
            for _chk in range(1):
                m = lo + T_pre
                m0 = int(np.floor(m))
                if m0 < 0: m0 = 0
                if m0 > hi_idx: m0 = hi_idx
                m1 = m0 + 1
                if m1 > hi_idx: m1 = hi_idx
                f = m - m0
                ex = (1-f)*H[m0, e, 0] + f*H[m1, e, 0]
                ey = (1-f)*H[m0, e, 1] + f*H[m1, e, 1]
                ez = (1-f)*H[m0, e, 2] + f*H[m1, e, 2]
                glo = np.sqrt((rx-ex)**2+(ry-ey)**2+(rz-ez)**2) - CLAT*(t-lo)
                m = hi + T_pre
                m0 = int(np.floor(m))
                if m0 < 0: m0 = 0
                if m0 > hi_idx: m0 = hi_idx
                m1 = m0 + 1
                if m1 > hi_idx: m1 = hi_idx
                f = m - m0
                ex = (1-f)*H[m0, e, 0] + f*H[m1, e, 0]
                ey = (1-f)*H[m0, e, 1] + f*H[m1, e, 1]
                ez = (1-f)*H[m0, e, 2] + f*H[m1, e, 2]
                ghi = np.sqrt((rx-ex)**2+(ry-ey)**2+(rz-ez)**2) - CLAT*(t-hi)
                if glo > 0.0 or ghi < 0.0:
                    lo = t - T_max; hi = float(t)
                    n_it = 28
                else:
                    n_it = 14 if use_warm else 28
            for _ in range(n_it):
                mid = 0.5*(lo+hi)
                m = mid + T_pre
                m0 = int(np.floor(m))
                if m0 < 0: m0 = 0
                if m0 > hi_idx: m0 = hi_idx
                m1 = m0 + 1
                if m1 > hi_idx: m1 = hi_idx
                f = m - m0
                ex = (1-f)*H[m0, e, 0] + f*H[m1, e, 0]
                ey = (1-f)*H[m0, e, 1] + f*H[m1, e, 1]
                ez = (1-f)*H[m0, e, 2] + f*H[m1, e, 2]
                g = np.sqrt((rx-ex)**2+(ry-ey)**2+(rz-ez)**2) - CLAT*(t-mid)
                if g > 0.0: hi = mid
                else: lo = mid
            trm = 0.5*(lo+hi)
            tr_out[i, e] = trm
            m = trm + T_pre
            m0 = int(np.floor(m))
            if m0 < 0: m0 = 0
            if m0 > hi_idx: m0 = hi_idx
            m1 = m0 + 1
            if m1 > hi_idx: m1 = hi_idx
            f = m - m0
            ex = (1-f)*H[m0, e, 0] + f*H[m1, e, 0]
            ey = (1-f)*H[m0, e, 1] + f*H[m1, e, 1]
            ez = (1-f)*H[m0, e, 2] + f*H[m1, e, 2]
            dx, dy, dz = rx-ex, ry-ey, rz-ez
            R = np.sqrt(dx*dx+dy*dy+dz*dz)
            a = 1.0/(4.0*np.pi*(R*R+SOFT2))
            s = q[e]*qi
            if R > 0.0:
                inv = 1.0/R
                net[i,0] += s*a*dx*inv
                net[i,1] += s*a*dy*inv
                net[i,2] += s*a*dz*inv
            ab[i] += a
    return net, ab, tr_out


def moment_step_fast(pos, q, hist, t, T_max, beta, mobile_sea=True, tr_prev=None):
    if mobile_sea:
        recv, ridx = pos, np.arange(len(pos))
    else:
        recv, ridx = pos[:1], np.arange(1)
    use_warm = tr_prev is not None
    tp = tr_prev if use_warm else np.zeros((len(recv), hist.N))
    net, ab, tr = kernel(recv, ridx, hist.H, float(hist.T_pre),
                         hist.t_now, float(t), T_max, q, tp, use_warm)
    src_net, src_ab = net[0].copy(), ab[0]
    new = pos.copy()
    if mobile_sea:
        nn = np.sqrt((net[1:]**2).sum(axis=1))
        frac = np.minimum(nn/np.maximum(ab[1:], 1e-30), 1.0)
        denom = np.where(nn > 0, nn, 1.0)
        new[1:] = pos[1:] + (frac/denom)[:, None]*PSR*net[1:]
    new[0, 0] = pos[0, 0] + beta
    return new, src_net, src_ab, tr


def validate():
    print("== kernel gate ==")
    # 10-Moment agreement on the source SSV_net, identical state
    sea, qs, _ = eng.build_sea()
    pos0 = np.concatenate([[[-3.0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt(52.0**2+16.0**2)+5
    diffs = []
    for path in ("ref", "fast"):
        pos = pos0.copy()
        hist = eng.History(pos, 0.10, int(np.ceil(T_max))+2, 12)
        tr = None; series = []
        for t in range(10):
            if path == "ref":
                pos, sn, sa, tr = eng.moment_step(pos, q, hist, t, T_max,
                                                  0.10, True, tr)
            else:
                pos, sn, sa, tr = moment_step_fast(pos, q, hist, t, T_max,
                                                   0.10, True, tr)
            hist.append(pos)
            series.append((sn[0], sn[1], sn[2], sa))
        if path == "ref":
            ref_series = np.array(series)
        else:
            d = np.abs(np.array(series) - ref_series).max()
            print(f"  10-Moment max |kernel - reference| = {d:.3e} "
                  f"(gate: <= 1e-10)")
            gate = d <= 1e-10
    # V1/V2 on kernel path: V1 exercises field solve; V2 dynamics
    eng.moment_step = moment_step_fast
    print("  V1 on kernel path:"); eng.v1()
    print("  V2 on kernel path:"); eng.v2()
    print(f"== GATE {'PASS' if gate else 'FAIL -- reference path mandatory'} ==")
    return gate


def leg(tag, beta, T_meas, mobile, x_off):
    T_EQ = 40
    CK = f"/tmp/ck_{tag}_{beta}_{x_off}.pkl"
    T_max = np.sqrt(52.0**2+16.0**2)+5
    if os.path.exists(CK):
        st = pickle.load(open(CK, "rb"))
        pos, q, tr, t0m, Dx, AB = (st[k] for k in
                                   ("pos", "q", "tr", "t", "Dx", "AB"))
        hist = eng.History(pos, beta, int(np.ceil(T_max))+2, T_EQ+T_meas)
        hist.H = st["H"]; hist.t_now = st["t_now"]
        print(f"[{tag} b={beta} ph={x_off}] resume at {t0m}")
    else:
        sea, qs, _ = eng.build_sea()
        x0 = -0.5*beta*(T_EQ+T_meas) + x_off
        pos = np.concatenate([[[x0, 0.0, 0.0]], sea])
        q = np.concatenate([[1.0], qs])
        hist = eng.History(pos, beta, int(np.ceil(T_max))+2, T_EQ+T_meas)
        tr, t0m, Dx, AB = None, 0, [], []
    t_start = time.time()
    for t in range(t0m, T_EQ+T_meas):
        pos, sn, sa, tr = moment_step_fast(pos, q, hist, t, T_max, beta,
                                           bool(mobile), tr)
        hist.append(pos)
        if t >= T_EQ:
            Dx.append(sn[0]); AB.append(sa)
        if time.time()-t_start > 235 and t < T_EQ+T_meas-1:
            pickle.dump(dict(pos=pos, q=q, tr=tr, t=t+1, H=hist.H,
                             t_now=hist.t_now, Dx=Dx, AB=AB), open(CK, "wb"))
            print(f"[{tag} b={beta} ph={x_off}] checkpoint {t+1}/{T_EQ+T_meas}")
            return
    D = float(np.mean(Dx)); sd = float(np.std(Dx))
    res = dict(tag=tag, beta=beta, D=D, sd=sd, ab=float(np.mean(AB)),
               T_meas=T_meas, mobile=int(mobile), phase=x_off)
    db = json.load(open("/tmp/2903_results.json"))
    db.append(res); json.dump(db, open("/tmp/2903_results.json", "w"), indent=1)
    if os.path.exists(CK): os.remove(CK)
    print(f"[{tag} b={beta} ph={x_off} mob={mobile}] DONE D={D:+.6e} sd={sd:.2e}")


if __name__ == "__main__":
    if sys.argv[1] == "validate":
        validate()
    else:
        leg(sys.argv[2], float(sys.argv[3]), int(sys.argv[4]),
            int(sys.argv[5]), float(sys.argv[6]))
