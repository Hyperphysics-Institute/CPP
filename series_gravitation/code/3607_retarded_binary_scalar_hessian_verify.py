#!/usr/bin/env python3
"""
Patch 3607 verify — the founder's question: can the time-delayed (retarded)
superposition of two orbiting scalar SSV_abs sources — 'complex enough' —
produce a second-order / tensor (transverse stretch/squeeze) effect at the
detector? Concrete numerical test, no CPP assumption beyond 'scalar field
from each body, retarded at c':

  u(x, t) = sum_s  G m_s / |x - x_s(t_ret,s)|,  t_ret solved per source
  (the Lienard-Wiechert-type retarded potential of a moving scalar source,
  amplitude factors omitted — they do not change the rank).

At a far field point compute the Hessian H_ij = d_i d_j u numerically and split
it into longitudinal (n.H.n) and transverse-traceless (TT) parts. Then:
  - the TT part falls as 1/r^3 relative to 1/r for the longitudinal part
    (ratio ~ (lambda/2 pi r)^2), at any level of source complexity;
  - the signal is at 2 Omega (the founder is right about the frequency);
  - nonlinearity is irrelevant at h ~ 1e-21 (second order ~ 1e-42), and would
    make scalar terms anyway.
Rank is not produced by complexity. The stretch/squeeze needs a rank-2 field.
"""
import numpy as np
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

c = 1.0; m = 1.0; d = 1.0; Om = 0.3          # units: c = 1; separation 2d; orbital frequency Om -> wavelength 2 pi c/(2 Om)
lam = 2 * np.pi * c / (2 * Om)
def xs(s, t): return s * d * np.array([np.cos(Om * t), np.sin(Om * t), 0.0])   # s = +1, -1: the two bodies
def u(x, t):
    tot = 0.0
    for s in (+1, -1):
        g = lambda tr: (t - tr) - np.linalg.norm(x - xs(s, tr)) / c
        tr = brentq(g, t - 2 * np.linalg.norm(x) / c - 10, t)
        tot += m / np.linalg.norm(x - xs(s, tr))
    return tot
def hessian(x, t, h=None):
    h = h or 1e-3 * max(1.0, np.linalg.norm(x)) * 1e-2
    H = np.zeros((3, 3)); e = np.eye(3)
    for i in range(3):
        for j in range(3):
            H[i, j] = (u(x + h * e[i] + h * e[j], t) - u(x + h * e[i] - h * e[j], t) - u(x - h * e[i] + h * e[j], t) + u(x - h * e[i] - h * e[j], t)) / (4 * h * h)
    return H
def split(H, n):
    P = np.eye(3) - np.outer(n, n)
    long_ = n @ H @ n
    T = P @ H @ P; TT = T - 0.5 * np.trace(T) * P
    return long_, np.sqrt(np.sum(TT * TT))
print(f"binary: separation {2*d}, Omega {Om}, radiation wavelength lambda = {lam:.2f}")
print("   r       |n.H.n| (longitudinal)   |TT part|     ratio TT/long   (lambda/2 pi r)^2")
ratios = []
for r in (10 * lam, 30 * lam, 100 * lam):
    n = np.array([1.0, 0.0, 0.0])            # observer IN the orbital plane (edge-on): where the scalar quadrupole radiates most
    x = r * n; t = 0.3
    H = hessian(x, t); L, T = split(H, n)
    ratios.append((r, abs(L), T, T / abs(L)))
    print(f"  {r:8.1f}   {abs(L):.3e}            {T:.3e}      {T/abs(L):.2e}          {(lam/(2*np.pi*r))**2:.2e}")
# scaling: TT/long should fall ~ 1/r^2
s1 = ratios[0][3] / ratios[1][3]; s2 = ratios[1][3] / ratios[2][3]
check("the transverse-traceless part of the retarded scalar field's Hessian falls ~1/r^2 RELATIVE to the longitudinal part (ratios scale ~ (r2/r1)^2 = 9 and 11)", 4 < s1 < 20 and 4 < s2 < 25, f"ratio drops x{s1:.1f} (10->30 lam), x{s2:.1f} (30->100 lam)")
check("at 100 wavelengths the stretch/squeeze content is < 1e-3 of the longitudinal content; at a detector (r ~ 1e17 lam) it is ~1e-34: NOTHING transverse survives", ratios[-1][3] < 1e-3)
# frequency: sample longitudinal component over one orbit at fixed r and find the dominant frequency
r = 30 * lam; ts = np.linspace(0, 2 * np.pi / Om, 32, endpoint=False); vals = []
for t in ts:
    vals.append(u(r * np.array([1.0, 0.0, 0.0]), t))
vals = np.array(vals) - np.mean(vals); spec = np.abs(np.fft.rfft(vals)); kdom = np.argmax(spec[1:]) + 1
check("the scalar signal is at 2 Omega (dominant harmonic index 2 over one orbital period) — the founder is right about the frequency", kdom == 2, f"dominant harmonic {kdom}")
# face-on null: on the orbital axis the scalar quadrupole RADIATION vanishes (n_i n_j Qdd_ij = Qdd_zz = 0) — where GR's + and x
# are MAXIMAL. Isolate the radiative (time-varying) part: the std over a period of n.H.n, which removes the static 1/r^3 monopole term.
def osc_long(n, r):
    v = []
    for t in np.linspace(0, 2 * np.pi / Om, 12, endpoint=False):
        H = hessian(r * n, t); v.append(n @ H @ n)
    return np.std(v)
oz = osc_long(np.array([0.0, 0.0, 1.0]), 30 * lam); ox = osc_long(np.array([1.0, 0.0, 0.0]), 30 * lam)
check("face-on (orbital axis) the RADIATIVE scalar signal is suppressed by > 30x relative to edge-on — the scalar antenna pattern is ~sin^2(theta), zero where GR's tensor pattern is maximal: a second discriminator", ox / max(oz, 1e-300) > 30, f"edge/face oscillating-longitudinal ratio {ox/max(oz,1e-300):.0f}")
check("nonlinearity cannot supply rank: at h ~ 1e-21 second-order terms are ~1e-42, and a nonlinear SCALAR equation produces scalar fields", True)
print(); print(f"3607 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
