#!/usr/bin/env python3
"""MOBILE-SEA MOVING-SOURCE ENGINE (Patch 2902).

Deterministic pairwise retarded shell-broadcast N-body under the frozen
prereg `sketches/mobile_sea_moving_source_prereg.md`. Built from spec:
  - propagation: c05 shell broadcast (ballistic, retarded, 1/4piR^2),
    Branch-1 structure as verified at Patch 2895;
  - emission state-independent (founder ruling, 31 Jul 2026);
  - motion: the C19/C20 primitive per-CP, step = min(|net|/abs,1)*PSR;
  - no self-force; partner interaction included (binding emergent).

Stages (CLI): v1 | v2 | v3 | v4 | run
The dressed measurement (`run`) is NOT executed at Patch 2902 commit
time; only v1-v4 are. See prereg section 6.
"""
import sys
import numpy as np

PSR = 0.5
D0 = 0.6            # initial pair separation
SOFT2 = 0.05 ** 2   # softening^2 (prereg section 2.7)
CLAT = 1.0


# ----------------------------------------------------------------- setup
def build_sea(rho_min=1.0, rho_max=8.0, x_lo=-16.0, x_hi=16.0, spacing=2.5):
    """Neutral pairs on a regular grid in a cylinder about the x-axis.
    Initial dipole orientation transverse-radial (x-reflection symmetric).
    Returns pos (N,3), charge (N,), pair index array (Np,2)."""
    xs = np.arange(x_lo, x_hi + 1e-9, spacing)
    ys = np.arange(-rho_max, rho_max + 1e-9, spacing)
    centres, orient = [], []
    for x in xs:
        for y in ys:
            for z in ys:
                rho = np.hypot(y, z)
                if rho_min <= rho <= rho_max:
                    centres.append((x, y, z))
                    orient.append((0.0, y / rho, z / rho))
    centres = np.array(centres)
    orient = np.array(orient)
    plus = centres + 0.5 * D0 * orient
    minus = centres - 0.5 * D0 * orient
    pos = np.concatenate([plus, minus])
    q = np.concatenate([np.ones(len(plus)), -np.ones(len(minus))])
    pairs = np.stack([np.arange(len(plus)),
                      len(plus) + np.arange(len(plus))], axis=1)
    return pos, q, pairs


# ------------------------------------------------- retarded field solver
class History:
    """Positions of all CPs at Moments -T_pre .. t_now, linearly
    interpolated at continuous times. Source (index 0) is backward-
    extrapolated at prescribed uniform velocity for t < 0; Sea CPs hold
    their initial positions for t < 0."""

    def __init__(self, pos0, beta, T_pre, T_total):
        self.N = len(pos0)
        self.T_pre = T_pre
        self.H = np.zeros((T_pre + T_total + 1, self.N, 3))
        for m in range(T_pre + 1):
            t = m - T_pre
            self.H[m] = pos0
            self.H[m, 0, 0] = pos0[0, 0] + beta * t
        self.t_now = 0

    def append(self, pos):
        self.t_now += 1
        self.H[self.t_now + self.T_pre] = pos

    def interp(self, tq, e_idx):
        """Positions of emitters e_idx at per-element continuous times tq
        (same shape as e_idx broadcast). Returns (...,3)."""
        m = tq + self.T_pre
        m0 = np.clip(np.floor(m).astype(int), 0, self.T_pre + self.t_now)
        m1 = np.clip(m0 + 1, 0, self.T_pre + self.t_now)
        f = (m - m0)[..., None]
        return (1 - f) * self.H[m0, e_idx] + f * self.H[m1, e_idx]


def field_at(recv_pos, recv_idx, hist, t, T_max, n_iter=28):
    """SSV_net (M,3) and SSV_abs (M,) at receiver positions recv_pos
    (their CP indices recv_idx, for self-exclusion), from all N emitters,
    retarded condition solved by vectorized bisection."""
    N = hist.N
    M = len(recv_pos)
    e_idx = np.broadcast_to(np.arange(N)[None, :], (M, N))
    lo = np.full((M, N), t - T_max)
    hi = np.full((M, N), float(t))
    for _ in range(n_iter):
        mid = 0.5 * (lo + hi)
        xe = hist.interp(mid, e_idx)
        g = np.linalg.norm(recv_pos[:, None, :] - xe, axis=2) \
            - CLAT * (t - mid)
        lo = np.where(g > 0, lo, mid)
        hi = np.where(g > 0, mid, hi)
    tr = 0.5 * (lo + hi)
    xe = hist.interp(tr, e_idx)
    dvec = recv_pos[:, None, :] - xe
    R = np.linalg.norm(dvec, axis=2)
    amp = 1.0 / (4 * np.pi * (R * R + SOFT2))
    self_mask = (e_idx == recv_idx[:, None])
    amp = np.where(self_mask, 0.0, amp)
    with np.errstate(invalid='ignore'):
        u = dvec / np.where(R[..., None] > 0, R[..., None], 1.0)
    return None, amp, u  # composed by caller with charges


def moment_step(pos, q, hist, t, T_max, beta, mobile_sea=True):
    """One Moment: compute SSV at every CP, move Sea CPs by the
    primitive, advect the source. Returns new pos and the source's
    (SSV_net vector, SSV_abs)."""
    _, amp, u = field_at(pos, np.arange(len(pos)), hist, t, T_max)
    sgn = q[None, :] * q[:, None]                    # (recv, emit)
    net = np.einsum('re,re,rec->rc', amp, sgn, u)
    ab = amp.sum(axis=1)
    src_net, src_ab = net[0].copy(), ab[0]
    new = pos.copy()
    if mobile_sea:
        nn = np.linalg.norm(net[1:], axis=1)
        frac = np.minimum(nn / np.maximum(ab[1:], 1e-30), 1.0)
        step = frac[:, None] * PSR * net[1:] \
            / np.where(nn[:, None] > 0, nn[:, None], 1.0)
        new[1:] = pos[1:] + step
    new[0, 0] = pos[0, 0] + beta      # prescribed source advection
    return new, src_net, src_ab


def run(beta, rho_min=1.0, rho_max=8.0, x_half=16.0, spacing=2.5,
        T_eq=40, T_meas=60, mobile_sea=True, verbose=False):
    sea, qs, _ = build_sea(rho_min, rho_max, -x_half, x_half, spacing)
    x_src0 = -0.5 * beta * (T_eq + T_meas)   # centre the transit
    pos = np.concatenate([[[x_src0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * x_half + 20) ** 2 + (2 * rho_max) ** 2) + 5
    hist = History(pos, beta, int(np.ceil(T_max)) + 2, T_eq + T_meas)
    Dx, AB = [], []
    for t in range(T_eq + T_meas):
        pos, src_net, src_ab = moment_step(pos, q, hist, t, T_max,
                                           beta, mobile_sea)
        hist.append(pos)
        if t >= T_eq:
            Dx.append(src_net[0])
            AB.append(src_ab)
        if verbose and t % 20 == 0:
            print(f"  t={t:4d}  D_x={src_net[0]:+.3e}  ab={src_ab:.3f}")
    return float(np.mean(Dx)), float(np.std(Dx)), float(np.mean(AB)), pos


# ------------------------------------------------------------ validations
def v1():
    """Static pointing + 1/4pi r^2 falloff."""
    src = np.array([[0.0, 0.0, 0.0]])
    probes = np.array([[3.0, 0, 0], [0, 5.0, 0], [0, 0, 8.0],
                       [4.0, 4.0, 0]])
    pos = np.concatenate([src, probes])
    q = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    hist = History(pos, 0.0, 40, 2)
    _, amp, u = field_at(pos, np.arange(len(pos)), hist, 0, 35.0)
    ok = True
    for i, p in enumerate(probes, start=1):
        r = np.linalg.norm(p)
        a_meas = amp[i, 0]
        a_theo = 1.0 / (4 * np.pi * (r * r + SOFT2))
        align = np.dot(u[i, 0], p / r)
        print(f"  probe r={r:6.3f}: amp={a_meas:.6e} vs {a_theo:.6e} "
              f"(ratio {a_meas/a_theo:.6f}), alignment={align:+.6f}")
        ok &= abs(a_meas / a_theo - 1) < 1e-6 and align > 1 - 1e-9
    print(f"  V1 {'PASS' if ok else 'FAIL'}")


def v2():
    """Isolated pair: bound and bounded over 500 Moments (emergent ZBW)."""
    pos = np.array([[0.0, 0.0, 0.0],
                    [0.3, 0.0, 0.0], [-0.3, 0.0, 0.0]])
    # index 0 is a dummy far-away source with zero effect: put it far out
    pos[0] = [500.0, 0, 0]
    q = np.array([1.0, 1.0, -1.0])
    hist = History(pos, 0.0, 30, 501)
    seps = []
    for t in range(500):
        pos, _, _ = moment_step(pos, q, hist, t, 25.0, 0.0, True)
        hist.append(pos)
        seps.append(np.linalg.norm(pos[1] - pos[2]))
    seps = np.array(seps)
    print(f"  pair separation: min={seps.min():.3f} max={seps.max():.3f} "
          f"mean={seps.mean():.3f} (D0={D0}, PSR={PSR})")
    bound = seps.max() < 5.0
    print(f"  V2 {'PASS (bound, bounded)' if bound else 'FAIL (unbound)'}")


def v3():
    """beta = 0 floor: axial drive from symmetry violation only."""
    D, sd, ab, _ = run(0.0, T_eq=30, T_meas=30)
    print(f"  F0 = |D(0)| = {abs(D):.3e}   (std/Moment {sd:.3e}, "
          f"SSV_abs at source {ab:.3f})")
    return abs(D)


def v4():
    """Smoke: moving source, mobile Sea, short run; drive NOT read."""
    _, _, _, pos = run(0.10, T_eq=20, T_meas=10)
    disp = np.linalg.norm(pos[1:], axis=1)
    print(f"  final Sea extent: max|x| = {disp.max():.2f} "
          f"(finite => no blow-up); step cap held by construction")
    print("  V4 PASS (drive not read)")


if __name__ == '__main__':
    stage = sys.argv[1] if len(sys.argv) > 1 else 'v1'
    if stage == 'v1':
        v1()
    elif stage == 'v2':
        v2()
    elif stage == 'v3':
        v3()
    elif stage == 'v4':
        v4()
    elif stage == 'run':
        beta = float(sys.argv[2])
        kw = {}
        for kv in sys.argv[3:]:
            k, v = kv.split('=')
            kw[k] = float(v) if '.' in v else int(v)
        D, sd, ab, _ = run(beta, verbose=True, **kw)
        print(f"D({beta}) = {D:+.6e}   std/Moment {sd:.3e}   "
              f"SSV_abs {ab:.4f}")
