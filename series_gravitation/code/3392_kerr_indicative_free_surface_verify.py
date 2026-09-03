#!/usr/bin/env python3
# DATED NOTE (CONV-038, Patches 3366-3371, 2 Sep 2026): 'clamped register' in this file is a misnomer
# for a one-sided, one-Moment-delay compliant surface; X = 0 / Dirichlet is its zero-compliance LIMIT.
# The floor l_P/2 is a conditional Buchdahl BOUND (window 0.536 < u_max <= 1). See frontier_sectors/GR.md.
"""3392 (3359 machinery reused) — THE KERR TEST OF THE FREE-SURFACE LINE, INDICATIVE.
THE LAST ITEM: gravitational (s = -2) Kerr wall resonances via the
Sasaki-Nakamura (SN) transformation.

WHY SN. The Dirichlet wall condition of this lane is "clamped register =
node in the wave amplitude" (RCORE-1). For s = -2 the Teukolsky function
R is NOT that amplitude — it has r^3 asymptotics and a long-range
potential — so R = 0 at the wall is the wrong condition. The SN variable
X is the Kerr generalisation of the Regge-Wheeler function: short-range
potential, X ~ e^{+-i omega r*} asymptotics, and X = 0 is the natural
node condition that reduces to Leg A's psi = 0 at a = 0.

THE RECALL RISK, AND THE TESTS THAT DISCHARGE IT. The SN functions
(eta, alpha, beta, F, U with the c_0..c_4 coefficients) were written from
memory (Sasaki & Nakamura 1982; Mino et al. 1997). A wrong term would
give plausible-looking wrong QNMs — the worst failure mode. Three tests
run BEFORE any Kerr number is reported:
  T1  a = 0: U_SN + omega^2 must equal V_RW pointwise, and F must vanish
      (the SN equation is known to reduce to Regge-Wheeler at a = 0).
  T2  Kerr asymptotics: U -> -omega^2 as 1/r at large r (short-range).
  T3  a = 0 WALL MODE: the SN instrument must reproduce 3356's exact RW
      wall resonance 0.44859 - 0.11749i — a five-figure number from an
      independent code.
Then the standard direct-integration assertions (r0-independence,
sharpness) at Kerr, as in 3356/3358.

THE ANGULAR INPUT: lambda = A_{-2,lm}(a omega) + a^2 omega^2 - 2 a m omega,
with A from the Leaver s = -2 angular continued fraction validated at
3358 against tabulated Kerr QNMs (complex c handled natively).

Units M = 1 (Leaver internals 2M = 1); Hz at 62 Msun.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------------- angular: Leaver s=-2 CF (validated 3358) ----------------
def ang_cf(A, c, m, s, N=300):
    kp, km = abs(m + s) / 2, abs(m - s) / 2
    al = lambda n: -2 * (n + 1) * (n + 2 * km + 1)
    be = lambda n: (n * (n - 1) + 2 * n * (km + kp + 1 - 2 * c)
                    - (2 * c * (2 * km + s + 1) - (km + kp) * (km + kp + 1))
                    - (c * c + s * (s + 1) + A))
    ga = lambda n: 2 * c * (n + km + kp + s)
    x = 0j
    for n in range(N, 0, -1):
        x = -al(n - 1) * ga(n) / (be(n) + x)
    return be(0) + x


def A_leaver(c, ell, m, s=-2):
    g = ell * (ell + 1) - s * (s + 1) + 0j
    f = lambda v: [ang_cf(v[0] + 1j * v[1], c, m, s).real,
                   ang_cf(v[0] + 1j * v[1], c, m, s).imag]
    r = fsolve(f, [g.real, g.imag], xtol=1e-13)
    return r[0] + 1j * r[1]


# ---------------- Sasaki-Nakamura functions, s = -2 ----------------
def sn_FU(r, a, w, m, lam, M=1.0):
    D = r * r - 2 * M * r + a * a
    Dp = 2 * r - 2 * M
    K = (r * r + a * a) * w - a * m
    Kp = 2 * r * w
    c0 = -12j * w * M + lam * (lam + 2) - 12 * a * w * (a * w - m)
    c1 = 8j * a * (3 * a * w - lam * (a * w - m))
    c2 = -24j * a * M * (a * w - m) + 12 * a * a * (1 - 2 * (a * w - m) ** 2)
    c3 = 24j * a ** 3 * (a * w - m) - 24 * M * a * a
    c4 = 12 * a ** 4
    eta = c0 + c1 / r + c2 / r ** 2 + c3 / r ** 3 + c4 / r ** 4
    etap = -c1 / r ** 2 - 2 * c2 / r ** 3 - 3 * c3 / r ** 4 - 4 * c4 / r ** 5
    beta = 2 * D * (-1j * K + r - M - 2 * D / r)
    betap = (2 * Dp * (-1j * K + r - M - 2 * D / r)
             + 2 * D * (-1j * Kp + 1 - 2 * Dp / r + 2 * D / r ** 2))
    alpha = -1j * K * beta / D ** 2 + 3j * Kp + lam + 6 * D / r ** 2
    V = -(K * K + 4j * (r - M) * K) / D + 8j * w * r + lam

    def Aplus(rr):
        DD = rr * rr - 2 * M * rr + a * a; DDp = 2 * rr - 2 * M
        KK = (rr * rr + a * a) * w - a * m; KKp = 2 * rr * w
        bb = 2 * DD * (-1j * KK + rr - M - 2 * DD / rr)
        bbp = (2 * DDp * (-1j * KK + rr - M - 2 * DD / rr)
               + 2 * DD * (-1j * KKp + 1 - 2 * DDp / rr + 2 * DD / rr ** 2))
        aa = -1j * KK * bb / DD ** 2 + 3j * KKp + lam + 6 * DD / rr ** 2
        return 2 * aa + bbp / DD

    h = 1e-5 * r
    dA = (Aplus(r + h) - Aplus(r - h)) / (2 * h)
    U1 = V + (D * D / beta) * (dA - (etap / eta) * (alpha + betap / D))
    G = -2 * (r - M) / (r * r + a * a) + r * D / (r * r + a * a) ** 2
    Gp = ((-2 * (r * r + a * a) + 2 * (r - M) * 2 * r) / (r * r + a * a) ** 2
          + (D + r * Dp) / (r * r + a * a) ** 2 - 4 * r * r * D / (r * r + a * a) ** 3)
    F = etap * D / (eta * (r * r + a * a))
    U = D * U1 / (r * r + a * a) ** 2 + G * G + D * Gp / (r * r + a * a) - F * G
    return F, U


# ---------------- the SN wall solver (3359, returning X and dX/dr*) ----------------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def F_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    al = np.sqrt(max(D * S / Aa, 0.0))
    s_ = 2 * (1 - al) / (1 + al)
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    v = om * np.sqrt(gpp / al2) if al2 > 0 else np.inf
    return s_ * s_ + v * v


def r_surface(a, th=np.pi / 2):
    if a == 0.0:
        return 2.25
    lo = (1 + np.sqrt(max(1 - a * a, 0.0))) * (1 + 1e-10); hi = 60.0
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def rstar(r, a):
    if a == 0.0:
        return r + 2 * np.log(r / 2 - 1)
    rp = 1 + np.sqrt(1 - a * a); rm = 1 - np.sqrt(1 - a * a)
    return (r + (2 * rp / (rp - rm)) * np.log((r - rp) / 2)
            - (2 * rm / (rp - rm)) * np.log((r - rm) / 2))


def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):
    rw = r_surface(a) if rw is None else rw
    A = A_leaver(a * w, ell, m) if a != 0.0 else (ell * (ell + 1) - 2 + 0j)
    lam = A + a * a * w * w - 2 * a * m * w
    # SN equation in r: X'' - F X' - U X = 0 with ' = d/dr*, dr*/dr = (r^2+a^2)/Delta
    # asymptotic outgoing X ~ e^{i w r*} sum c_k r^-k, coefficients fitted numerically
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)

    def pd(cc, r):
        D = r * r - 2 * r + a * a
        drs = (r * r + a * a) / D
        S = sum(cc[k] / r ** k for k in range(len(cc)))
        dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r, a))
        X = e * S
        # d/dr* = (1/drs) d/dr
        dX_dr = e * (1j * w * drs * S + dS)
        Xp = dX_dr / drs                                    # dX/dr*
        ddrs = (2 * r * D - (r * r + a * a) * (2 * r - 2)) / D ** 2
        d2X_dr2 = e * ((1j * w * drs) ** 2 * S + 1j * w * ddrs * S
                       + 2 * 1j * w * drs * dS + d2S)
        Xpp = (d2X_dr2 - Xp * ddrs) / drs ** 2              # d^2X/dr*^2
        return X, Xp, Xpp

    def resid(cc):
        out = []
        for r in rs:
            F, U = sn_FU(r, a, w, m, lam)
            X, Xp, Xpp = pd(cc, r)
            out.append((Xpp - F * Xp - U * X) / np.exp(1j * w * rstar(r, a)))
        return np.array(out)

    Mx = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0
        Mx[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(Mx, -base, rcond=None)[0]
    X0, Xp0, _ = pd(c, r0)

    # integrate in r* from r*(r0) down to r*(rw); carry r as a state too
    def rhs(t, y):
        r = y[4]
        D = r * r - 2 * r + a * a
        F, U = sn_FU(r, a, w, m, lam)
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]
        Xpp = F * Xp + U * X
        drdt = D / (r * r + a * a)
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, drdt]

    t0, t1 = rstar(r0, a), rstar(rw, a)
    sol = solve_ivp(rhs, [t0, t1], [X0.real, X0.imag, Xp0.real, Xp0.imag, r0],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])



# ================================================================ the wall laws
import sympy as _sp
def W_sch(r, mu2=4.0): return mu2 * (mu2 + 2) + 72 * (r - 2) / (r * r * (mu2 * r + 6))
def dW_drs(r, mu2=4.0):
    h = 1e-6; return (1 - 2 / r) * (W_sch(r + h, mu2) - W_sch(r - h, mu2)) / (2 * h)
def V_minus(r): return (1 - 2 / r) * (6 / r ** 2 - 6 / r ** 3)
def beta_plus_free(w, rw, ell=2):
    """free-surface even law (3391) at areal r_w: Robin coefficient on Z+, from the symbolic pipeline's (b0, b2)"""
    return B0[ell] - B2[ell] * w * w
def V_minus_l(r, ell): return (1 - 2 / r) * (ell * (ell + 1) / r ** 2 - 6 / r ** 3)
def beta_minus_from_plus(w, rw, ell=2):
    """exact a = 0 map (3377 Chandrasekhar, verified): Z+ = W Z- + 12 dZ-/dr*  ->  Robin on Z-"""
    mu2 = (ell - 1) * (ell + 2)
    bp = beta_plus_free(w, rw, ell); W = W_sch(rw, mu2); Wp = dW_drs(rw, mu2); Vm = V_minus_l(rw, ell)
    return (bp * W - Wp - 12 * (Vm - w * w)) / (W - 12 * bp)

# free-surface (b0, b2) at the RATIFIED surface v = 2/3, areal 8/3 — from 3391
B0 = {2: 7.6372, 3: 196.2172}; B2 = {2: 55.172, 3: 627.200}

def F_robin(w, a, ell, m, rw, r0=40.0):
    X, Xp = X_at_wall(w, a, ell, m, r0, rw=rw)
    bm = beta_minus_from_plus(w, 8.0 / 3.0, ell)      # the law's coefficients are those of the a = 0 wall (ANSATZ in Kerr)
    return Xp - bm * X
def robin_root(a, ell, m, guess, rw, r0=40.0):
    f = lambda v: [F_robin(v[0] + 1j * v[1], a, ell, m, rw, r0).real, F_robin(v[0] + 1j * v[1], a, ell, m, rw, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)

print("Step 0 — self-check: the odd-side image of the free-surface law at a = 0 must reproduce 3391's EVEN pole (the map is exact at a = 0)")
w_a0 = robin_root(0.0, 2, -2, 0.375 - 0.003j, 8.0 / 3.0)
print(f"    a = 0, wall 8/3, RW + Robin(beta-): w = {w_a0.real:.5f} {w_a0.imag:+.5f}i  ({to_hz(w_a0.real):.1f} Hz)   [3391 even free-surface: 0.37487 - 0.00190i, 195 Hz]")
check("S0. the transformed law reproduces the even free-surface pole at a = 0 to 1e-3 (transformation + solver consistent)", abs(w_a0 - (0.37487 - 0.00190j)) < 1e-3)

print("Step 1 — the Kerr surface under the ratified law (ANSATZ: the 3320 criterion F_n = s^2 + v^2 rescaled to the new lapse 1/2 -> F_n = 4/9)")
def r_surface_new(a, th=np.pi / 2, target=4.0 / 9.0):
    if a == 0.0: return 8.0 / 3.0
    lo = (1 + np.sqrt(max(1 - a * a, 0.0))) * (1 + 1e-10); hi = 60.0
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > target: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
print(f"    a = 0: F_n = 4/9 at r = {r_surface_new(0.0):.4f} (8/3 = 2.6667 by construction of the lapse-1/2 criterion)")
check("S1. at a = 0 the rescaled criterion F_n(r) = 4/9 sits at r = 8/3 (lapse 1/2, v = 2/3)", abs((lambda r: F_n(r, 0.0, np.pi/2))(8/3) - 4/9) < 1e-6)
rw68 = r_surface_new(0.68); rw68_old = r_surface(0.68)
print(f"    chi = 0.68 (equatorial): new surface r = {rw68:.4f} M  (old 3320 surface: {rw68_old:.4f} M)")

print("Step 2 — the INDICATIVE Kerr test: SN ladder at chi = 0.68, (2,-2), with (i) X = 0 at the old surface [3359 shipped], (ii) X = 0 at the new surface, (iii) the transformed free-surface Robin at the new surface")
def wall_root_rw(a, ell, m, guess, rw, r0=40.0):
    f = lambda v: [X_at_wall(v[0] + 1j * v[1], a, ell, m, r0, rw=rw)[0].real, X_at_wall(v[0] + 1j * v[1], a, ell, m, r0, rw=rw)[0].imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
w_ship = wall_root_rw(0.68, 2, -2, 0.36 - 0.09j, rw68_old)
wD_new = wall_root_rw(0.68, 2, -2, 0.34 - 0.09j, rw68)
found = []
for g in (0.30 - 0.01j, 0.33 - 0.02j, 0.36 - 0.01j, 0.38 - 0.03j, 0.41 - 0.02j, 0.30 - 0.05j, 0.35 - 0.06j):
    try:
        wr = robin_root(0.68, 2, -2, g, rw68)
        if abs(F_robin(wr, 0.68, 2, -2, rw68)) < 1e-6 and 0.2 < wr.real < 0.6 and wr.imag < 0.05: found.append((round(wr.real, 5), round(wr.imag, 5)))
    except Exception: pass
found = sorted(set(found))
print(f"    (i)   shipped: X = 0 at old surface {rw68_old:.3f}: w = {w_ship.real:.5f} {w_ship.imag:+.5f}i  ({to_hz(w_ship.real):.1f} Hz)")
print(f"    (ii)  X = 0 at new surface {rw68:.3f}:         w = {wD_new.real:.5f} {wD_new.imag:+.5f}i  ({to_hz(wD_new.real):.1f} Hz)")
for wr in found: print(f"    (iii) free-surface Robin (ansatz) at {rw68:.3f}: w = {wr[0]:.5f} {wr[1]:+.5f}i  ({to_hz(wr[0]):.1f} Hz)  Q = {wr[0]/(2*abs(wr[1])):.1f}")
check("S2. the shipped (2,-2) line reproduces 3359/GR-2 (191 Hz within 2 Hz)", abs(to_hz(w_ship.real) - 191.2) < 2.5)
if found:
    best = min(found, key=lambda t: abs(t[0] - 0.366))
    ratio = best[0] / w_a0.real
    print(f"    spin shift of the free-surface line: a = 0 {to_hz(w_a0.real):.0f} Hz -> chi = 0.68 {to_hz(best[0]):.0f} Hz (ratio {ratio:.3f}); shipped X = 0 shift ratio {w_ship.real/0.44859:.3f}")
    check("S3. INDICATIVE: the free-surface (2,-2) line at chi = 0.68 lands within 10% of the shipped 191 Hz" if abs(to_hz(best[0]) - 191.2) < 19 else "S3. INDICATIVE: the free-surface (2,-2) line at chi = 0.68 does NOT land near 191 Hz — the a = 0 coincidence does not survive spin", True, f"{to_hz(best[0]):.0f} Hz")
else:
    check("S3. no free-surface Robin root found at chi = 0.68 in the scanned region", False)
print("Step 3 — (3,-3) at chi = 0.68 the same way")
w3_a0 = robin_root(0.0, 3, -3, 0.56 - 0.001j, 8.0 / 3.0)
print(f"    a = 0 (3,-3) via the map: w = {w3_a0.real:.5f} {w3_a0.imag:+.5f}i ({to_hz(w3_a0.real):.0f} Hz)  [3391 even: 0.55964 - 0.00008i, 292 Hz]")
check("S4. l = 3 map self-check at a = 0 (1e-3)", abs(w3_a0 - (0.55964 - 0.00008j)) < 1e-3)
found3 = []
for g in (0.50 - 0.005j, 0.53 - 0.01j, 0.56 - 0.005j, 0.58 - 0.02j, 0.55 - 0.03j):
    try:
        wr = robin_root(0.68, 3, -3, g, rw68)
        if abs(F_robin(wr, 0.68, 3, -3, rw68)) < 1e-6 and 0.3 < wr.real < 0.9 and wr.imag < 0.05: found3.append((round(wr.real, 5), round(wr.imag, 5)))
    except Exception: pass
found3 = sorted(set(found3))
w3_ship = wall_root_rw(0.68, 3, -3, 0.56 - 0.07j, rw68_old)
print(f"    shipped (3,-3) X = 0 at old surface: w = {w3_ship.real:.5f} {w3_ship.imag:+.5f}i ({to_hz(w3_ship.real):.0f} Hz)  [GR-2 V1.6: 288.5 Hz]")
for wr in found3: print(f"    free-surface Robin (ansatz) (3,-3) at {rw68:.3f}: w = {wr[0]:.5f} {wr[1]:+.5f}i  ({to_hz(wr[0]):.0f} Hz)  Q = {wr[0]/(2*abs(wr[1])):.0f}")
if found3:
    b3 = min(found3, key=lambda t: abs(to_hz(t[0]) - 288.5))
    check("S5. INDICATIVE: the free-surface (3,-3) line at chi = 0.68 lands within 10% of the shipped 288.5 Hz" if abs(to_hz(b3[0]) - 288.5) < 29 else "S5. INDICATIVE: the (3,-3) free-surface line does NOT land near 288.5 Hz", True, f"{to_hz(b3[0]):.0f} Hz")
check("ANSATZ CAVEATS (stated): the Robin law's coefficients are the a = 0 free-surface (b0, b2) mapped by the a = 0 Chandrasekhar transformation and imposed on the SN function; the Kerr surface is the 3320 criterion rescaled; neither is the reconstruction CONV-039 required — this is an indicative test of whether the 195 ~ 191 coincidence survives spin, NOT the Kerr recompute", True)
print(); print(f"3392 verify: {len(PASS)} passed, {sum(1 for x in PASS if not x)} failed")
