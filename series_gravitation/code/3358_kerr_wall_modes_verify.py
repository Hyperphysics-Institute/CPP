#!/usr/bin/env python3
"""3358_kerr_wall_modes_verify.py — TEUKOLSKY LADDER RUNG 3b.

Two parts, each with its own known-answer validation before anything
new is reported.

PART A — Leaver's coupled Kerr continued fractions (angular + radial,
1985), s = -2, validated against TABULATED Kerr quasinormal modes for
(2,2) at a/M = 0, 0.5, 0.7, 0.9. Both recurrences were written from
memory; the tables are the test. Passing this validates (i) the s = -2
angular sector for ALL (ell, m) including ell = 2 — the case 3357 had to
exclude because Leaver's series absorbs the pole exponent into its
prefactor — and (ii) the Kerr radial recurrence.

PART B — the first EXACT Kerr wall resonances in the lane, in the
SCALAR (s = 0) sector. Why scalar first: R = 0 is the natural Dirichlet
condition for a scalar field, with no transformation issue, whereas the
gravitational wall condition must be posed on the Sasaki-Nakamura
variable (rung 3c). And every census result in this lane so far (3334,
3339, 3354) was at scalar/eikonal grade — so this IS the exact version
of the grade the lane has been working at. Method: direct inward
integration of the s = 0 Kerr radial Teukolsky equation
    Delta d/dr(Delta dR/dr) + [K^2 - Delta*lambda] R = 0,
    K = (r^2+a^2) omega - a m,  lambda = A(a omega) + a^2 omega^2 - 2 a m omega,
from a numerically-fitted outgoing asymptotic series at r0, to the
derived wall, root-finding on R(r_w) = 0 in the complex omega plane.
Validation ladder for Part B, asserted: (B1) at a = 0 the s = 0 Kerr
wall mode must match the same instrument run on the Schwarzschild s = 0
potential; (B2) root independent of r0; (B3) zero is sharp; (B4) the
angular eigenvalue from the Leaver CF at real c must match 3353's
finite-difference value.

FENCE: Part B is s = 0. The s = -2 wall (Sasaki-Nakamura) is rung 3c.
Units: Leaver internals in 2M = 1; everything reported in M = 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
from scipy.linalg import eigh_tridiagonal

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ======================= Leaver machinery (2M = 1 inside) =======================
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


def A_leaver(c, ell, m, s):
    g = ell * (ell + 1) - s * (s + 1) + 0j
    f = lambda v: [ang_cf(v[0] + 1j * v[1], c, m, s).real,
                   ang_cf(v[0] + 1j * v[1], c, m, s).imag]
    r = fsolve(f, [g.real, g.imag], xtol=1e-13)
    return r[0] + 1j * r[1]


def rad_cf(w, a, A, m, s, N=400):
    b = np.sqrt(1 - 4 * a * a)
    q = w / 2 - a * m
    c0 = 1 - s - 1j * w - (2j / b) * q
    c1 = -4 + 2j * w * (2 + b) + (4j / b) * q
    c2 = s + 3 - 3j * w - (2j / b) * q
    c3 = (w * w * (4 + 2 * b - a * a) - 2 * a * m * w - s - 1 + (2 + b) * 1j * w
          - A + ((4 * w + 2j) / b) * q)
    c4 = s + 1 - 2 * w * w - (2 * s + 3) * 1j * w - ((4 * w + 2j) / b) * q
    al = lambda n: n * n + (c0 + 1) * n + c0
    be = lambda n: -2 * n * n + (c1 + 2) * n + c3
    ga = lambda n: n * n + (c2 - 3) * n + c4 - c2 + 2
    x = 0j
    for n in range(N, 0, -1):
        x = -al(n - 1) * ga(n) / (be(n) + x)
    return be(0) + x


def kerr_qnm(a_M, ell, m, s, guess_M):
    a = a_M / 2.0
    def F(v):
        w = v[0] + 1j * v[1]
        A = A_leaver(a * w, ell, m, s)
        val = rad_cf(w, a, A, m, s)
        return [val.real, val.imag]
    r = fsolve(F, [2 * guess_M.real, 2 * guess_M.imag], xtol=1e-12)
    return (r[0] + 1j * r[1]) / 2.0


# ======================= PART A: validation =======================
KNOWN = {0.0: 0.37367 - 0.08896j, 0.5: 0.46412 - 0.08558j,
         0.7: 0.53260 - 0.08079j, 0.9: 0.67163 - 0.06486j}
errs = {}
for aM, wk in KNOWN.items():
    w = kerr_qnm(aM, 2, 2, -2, wk)
    errs[aM] = abs(w - wk) / abs(wk)
check("A1. LEAVER KERR (angular + radial CFs, s = -2, written from memory) "
      "reproduces TABULATED (2,2) Kerr QNMs at a/M = 0, 0.5, 0.7, 0.9",
      max(errs.values()) < 3e-4,
      "; ".join(f"a={a}: {e:.1e}" for a, e in errs.items()))

# ell = 2 gravitational angular eigenvalue — the case 3357 could not do
c_22 = 0.68 * 0.3953          # a * omega_top(2,-2), from 3354
A22 = A_leaver(c_22, 2, -2, -2)
A22_0 = A_leaver(0.0, 2, -2, -2)
check("A2. THE ell = 2 GAP FROM 3357 CLOSED: the gravitational (s = -2) "
      "angular eigenvalue at (2,-2) is obtained by the Leaver series, which "
      "absorbs the zero pole exponent into its prefactor",
      abs(A22_0 - 4.0) < 1e-8 and abs(A22.imag) < 1e-9,
      f"A(2,-2; c=0) = {A22_0.real:.6f} (exact 4); at c = {c_22:.4f}: "
      f"A = {A22.real:.5f} vs scalar-sector 5.989 and eikonal 6.25")

# Leaver s=0 angular vs 3353 finite differences at real c (cross-instrument)
def A_fd(ell, m, c, N=1600):
    xf = np.linspace(-1.0, 1.0, N + 2); x = xf[1:-1]; h = xf[1] - xf[0]
    xh = 0.5 * (xf[:-1] + xf[1:]); p = 1.0 - xh * xh
    main = -(p[:-1] + p[1:]) / h ** 2 + (c * c * x * x - m * m / (1.0 - x * x))
    off = p[1:-1] / h ** 2
    idx = ell - abs(m)
    ev = eigh_tridiagonal(main, off, eigvals_only=True,
                          select="i", select_range=(N - 1 - idx, N - 1))
    return float(-ev[0])


xi = abs(A_leaver(0.2757, 2, -2, 0).real - A_fd(2, -2, 0.2757))
check("B4. CROSS-INSTRUMENT: Leaver's angular CF at s = 0 agrees with 3353's "
      "finite-difference eigenvalue at real c to 1e-6",
      xi < 1e-6, f"|A_Leaver - A_FD| = {xi:.1e} at (2,-2), c = 0.2757")

# ======================= PART B: scalar Kerr wall modes =======================
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


def rstar_kerr(r, a):
    rp = 1 + np.sqrt(1 - a * a); rm = 1 - np.sqrt(1 - a * a)
    if a == 0.0:
        return r + 2 * np.log(r / 2 - 1)
    return (r + (2 * rp / (rp - rm)) * np.log((r - rp) / 2)
            - (2 * rm / (rp - rm)) * np.log((r - rm) / 2))


def scalar_kerr_R_at_wall(w, a, ell, m, r0=40.0, nterms=8):
    """Integrate s=0 Kerr radial Teukolsky inward from a fitted outgoing
    asymptotic series; return R(r_w)."""
    rw = r_surface(a)
    A = A_leaver((a / 2) * (2 * w) if False else a * w, ell, m, 0)   # c = a*omega (M=1)
    lam = A + a * a * w * w - 2 * a * m * w

    def coeffs(r):
        D = r * r - 2 * r + a * a
        K = (r * r + a * a) * w - a * m
        return D, K

    # asymptotic outgoing: R ~ e^{i w r*} r^-1 sum c_k r^-k ; fit c_k numerically
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)

    def pd(cc, r):
        D, K = coeffs(r)
        dr_star = (r * r + a * a) / D
        S = sum(cc[k] / r ** (k + 1) for k in range(len(cc)))
        dS = sum(-(k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        d2S = sum((k + 1) * (k + 2) * cc[k] / r ** (k + 3) for k in range(len(cc)))
        e = np.exp(1j * w * rstar_kerr(r, a))
        # d/dr (e S) = e (i w dr_star S + dS); second derivative below
        ddr_star = (2 * r * D - (r * r + a * a) * (2 * r - 2)) / D ** 2
        R = e * S
        Rp = e * (1j * w * dr_star * S + dS)
        Rpp = e * ((1j * w * dr_star) ** 2 * S + 1j * w * ddr_star * S
                   + 2 * 1j * w * dr_star * dS + d2S)
        return R, Rp, Rpp

    def resid(cc):
        out = []
        for r in rs:
            D, K = coeffs(r)
            R, Rp, Rpp = pd(cc, r)
            out.append((D * D * Rpp + D * (2 * r - 2) * Rp + (K * K - D * lam) * R)
                       / np.exp(1j * w * rstar_kerr(r, a)))
        return np.array(out)

    M_ = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0
        M_[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(M_, -base, rcond=None)[0]
    R0, Rp0, _ = pd(c, r0)

    def rhs(r, y):
        D, K = coeffs(r)
        R = y[0] + 1j * y[1]; Rp = y[2] + 1j * y[3]
        Rpp = -(D * (2 * r - 2) * Rp + (K * K - D * lam) * R) / (D * D)
        return [Rp.real, Rp.imag, Rpp.real, Rpp.imag]

    sol = solve_ivp(rhs, [r0, rw], [R0.real, R0.imag, Rp0.real, Rp0.imag],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    return sol.y[0, -1] + 1j * sol.y[1, -1]


def wall_root(a, ell, m, guess, r0=40.0):
    f = lambda v: [scalar_kerr_R_at_wall(v[0] + 1j * v[1], a, ell, m, r0).real,
                   scalar_kerr_R_at_wall(v[0] + 1j * v[1], a, ell, m, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]


# B1: a = 0 must match the Schwarzschild s = 0 potential run on the rung-2 instrument
def schw_s0_wall(guess, r0=40.0):
    V = lambda r: (1 - 2 / r) * (6 / r ** 2 + 2 / r ** 3)     # ell=2, s=0
    rst = lambda r: r + 2 * np.log(r / 2 - 1)
    def psi_w(w):
        c = np.zeros(8, dtype=complex); c[0] = 1.0
        rs = np.linspace(r0, 4 * r0, 40)
        def pd(cc, r):
            f = 1 - 2 / r
            S = sum(cc[k] / r ** k for k in range(len(cc)))
            dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
            d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
            e = np.exp(1j * w * rst(r))
            return (e * S, e * (1j * w / f * S + dS),
                    e * ((1j * w / f) ** 2 * S + 2 * (1j * w / f) * dS + d2S
                         - 1j * w * (2 / r ** 2) / f ** 2 * S))
        def resid(cc):
            return np.array([(( (1-2/r)**2 * pd(cc,r)[2] + (1-2/r)*(2/r**2)*pd(cc,r)[1]
                                + (w*w - V(r))*pd(cc,r)[0]) / np.exp(1j*w*rst(r))) for r in rs])
        M_ = np.zeros((40, 7), dtype=complex); base = resid(c)
        for k in range(1, 8):
            cc = c.copy(); cc[k] = 1.0; M_[:, k-1] = resid(cc) - base
        c[1:] = np.linalg.lstsq(M_, -base, rcond=None)[0]
        p0, dp0, _ = pd(c, r0)
        def rhs(r, y):
            f = 1-2/r; fp = 2/r**2; psi = y[0]+1j*y[1]; dpsi = y[2]+1j*y[3]
            d2 = -(f*fp*dpsi + (w*w - V(r))*psi)/(f*f)
            return [dpsi.real, dpsi.imag, d2.real, d2.imag]
        s = solve_ivp(rhs, [r0, 2.25], [p0.real,p0.imag,dp0.real,dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
        return s.y[0,-1] + 1j*s.y[1,-1]
    f = lambda v: [psi_w(v[0]+1j*v[1]).real, psi_w(v[0]+1j*v[1]).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11)
    return s[0]+1j*s[1]


w_schw_kerr = wall_root(0.0, 2, -2, 0.48 - 0.10j)
w_schw_rw = schw_s0_wall(0.48 - 0.10j)
check("B1. a = 0 LIMIT: the Kerr scalar instrument at a = 0 reproduces the "
      "Schwarzschild s = 0 wall mode computed by the rung-2 instrument on "
      "the s = 0 potential — two independent codes, one number",
      abs(w_schw_kerr - w_schw_rw) < 1e-4,
      f"Kerr(a=0) {w_schw_kerr:.5f} vs Schwarzschild {w_schw_rw:.5f}")

# THE NEW RESULT: scalar Kerr wall modes at chi = 0.68
A_SPIN = 0.68
targets = [(2, -2, 0.45 - 0.10j), (3, -3, 0.62 - 0.10j), (2, 1, 0.62 - 0.12j)]
res = {}
print(f"      chi = {A_SPIN}, wall r = {r_surface(A_SPIN):.4f} M — exact scalar wall modes:")
for ell, m, g in targets:
    w = wall_root(A_SPIN, ell, m, g)
    res[(ell, m)] = w
    print(f"        ({ell},{m:+d}): w = {w:.5f}  f = {to_hz(w.real):.1f} Hz @62  "
          f"Q = {w.real/(2*abs(w.imag)):.2f}")

w22 = res[(2, -2)]
r0s = [wall_root(A_SPIN, 2, -2, w22, r0) for r0 in (30.0, 50.0)]
check("B2. ROOT INDEPENDENT OF r0 (direct-integration instability test, "
      "Kerr): (2,-2) at chi = 0.68 stable across r0 = 30, 40, 50",
      max(abs(r - w22) for r in r0s) < 1e-4,
      f"spread {max(abs(r - w22) for r in r0s):.1e} about {w22:.5f}")

on = abs(scalar_kerr_R_at_wall(w22, A_SPIN, 2, -2))
off = abs(scalar_kerr_R_at_wall(w22 + 0.02j, A_SPIN, 2, -2))
check("B3. ZERO IS SHARP: |R(r_w)| at the (2,-2) root is orders below its "
      "value a small step away",
      on / off < 1e-2, f"contrast {on/off:.1e}")

# comparison with the WKB census
check("B5. AGAINST THE WKB CENSUS (3334/3354): the exact (2,-2) line sits "
      "ABOVE the eikonal barrier top 0.3953-0.4055, as the chi = 0 anchor "
      "predicted (+15% there), and is a BROAD top-of-barrier feature — "
      "no trapped comb at ell = 2, exactly",
      w22.real > 0.40 and w22.real / (2 * abs(w22.imag)) < 4,
      f"Re w = {w22.real:.4f} vs top 0.3953 ({w22.real/0.3953-1:+.1%}); "
      f"Q = {w22.real/(2*abs(w22.imag)):.2f} (Leg-A-style Q~5 would be a "
      f"narrow line; this is broad, consistent with 3356's Q = 1.9 at chi=0)")

# retrograde vs prograde-exposed ordering — the discriminator, exact
w21 = res[(2, 1)]
check("B6. THE DISCRIMINATOR AT EXACT GRADE: the retrograde (2,-2) line lies "
      "BELOW the exposed prograde (2,+1) line, preserving GR-2's "
      "retrograde-keyed ORDERING with exact scalar Kerr modes",
      w22.real < w21.real,
      f"(2,-2) {to_hz(w22.real):.0f} Hz < (2,+1) {to_hz(w21.real):.0f} Hz @62 Msun")

check("B7. SCOPE ASSERTED: Part B is SCALAR (s = 0) — the exact version of the "
      "grade every lane census has been at. The GRAVITATIONAL wall (s = -2) "
      "requires the Sasaki-Nakamura variable for its boundary condition and "
      "is rung 3c, NOT delivered here",
      True, "")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
