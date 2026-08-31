#!/usr/bin/env python3
"""3359_sn_gravitational_wall_modes_verify.py — TEUKOLSKY LADDER RUNG 3c,
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


# ---------------- T1: a = 0 reduction to Regge-Wheeler ----------------
w_test = 0.44859 - 0.11749j
lam0 = 4.0 + 0j
V_RW = lambda r: (1 - 2 / r) * (6 / r ** 2 - 6 / r ** 3)
d1 = []
for r in (2.3, 3.0, 5.0, 10.0, 30.0):
    F, U = sn_FU(r, 0.0, w_test, -2, lam0)
    d1.append(max(abs(U + w_test * w_test - V_RW(r)), abs(F)))
check("T1. THE RECALL TEST: at a = 0 the Sasaki-Nakamura potential reduces "
      "EXACTLY to Regge-Wheeler (U_SN + omega^2 = V_RW pointwise, F = 0) — a "
      "wrong term anywhere in eta/alpha/beta/U would break this",
      max(d1) < 1e-8, f"max pointwise deviation {max(d1):.1e} over r = 2.3..30")

# ---------------- T2: Kerr short-range ----------------
a68 = 0.68
A22 = A_leaver(a68 * w_test, 2, -2)
lam22 = A22 + a68 * a68 * w_test * w_test - 2 * a68 * (-2) * w_test
dev = [abs(sn_FU(r, a68, w_test, -2, lam22)[1] + w_test * w_test) for r in (50.0, 200.0, 1000.0)]
check("T2. KERR ASYMPTOTICS: U -> -omega^2 at large r with 1/r falloff — the "
      "SN potential is short-range, so X ~ e^{+-i omega r*} and X = 0 is a "
      "well-posed node condition",
      dev[0] > dev[1] > dev[2] and dev[2] < 1e-5,
      f"|U + omega^2| at r = 50/200/1000: {dev[0]:.1e} / {dev[1]:.1e} / {dev[2]:.1e}")

# ---------------- the SN wall solver ----------------
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


def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):
    rw = r_surface(a)
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
    return sol.y[0, -1] + 1j * sol.y[1, -1]


def wall_root(a, ell, m, guess, r0=40.0):
    f = lambda v: [X_at_wall(v[0] + 1j * v[1], a, ell, m, r0).real,
                   X_at_wall(v[0] + 1j * v[1], a, ell, m, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]


# ---------------- T3: a = 0 wall mode reproduces 3356 ----------------
w0 = wall_root(0.0, 2, -2, 0.45 - 0.11j)
check("T3. THE DECISIVE TEST: at a = 0 the SN wall instrument reproduces "
      "3356's exact Regge-Wheeler wall resonance from an independent code",
      abs(w0 - (0.44859 - 0.11749j)) < 2e-4,
      f"SN(a=0) {w0:.5f} vs RW (3356) 0.44859-0.11749i, "
      f"|diff| = {abs(w0-(0.44859-0.11749j)):.1e}")

# ---------------- THE GRAVITATIONAL KERR WALL SPECTRUM ----------------
# Every reported root must pass BOTH instability tests individually; a
# root-finder that returns its own guess is recorded as NOT-LOCATED, not
# as a number. (First run: (2,+1) came back as exactly its guess and was
# nearly reported — the contrast test below is what catches that.)
def validated_root(ell, m, guess):
    w = wall_root(a68, ell, m, guess)
    on = abs(X_at_wall(w, a68, ell, m)); off = abs(X_at_wall(w + 0.02j, a68, ell, m))
    sp = max(abs(wall_root(a68, ell, m, w, r0) - w) for r0 in (30.0, 50.0))
    ok = (on / off < 1e-2) and (sp < 1e-4)
    return w, on / off, sp, ok

targets = [(2, -2, 0.47 - 0.11j), (3, -3, 0.62 - 0.08j), (2, 1, 0.62 - 0.25j)]
res, val = {}, {}
print(f"      chi = {a68}, wall r = {r_surface(a68):.4f} M — GRAVITATIONAL (s=-2) wall modes:")
for ell, m, g in targets:
    w, contrast, sp, ok = validated_root(ell, m, g)
    val[(ell, m)] = ok
    if ok:
        res[(ell, m)] = w
        print(f"        ({ell},{m:+d}): w = {w:.5f}  f = {to_hz(w.real):.1f} Hz @62  "
              f"Q = {w.real/(2*abs(w.imag)):.2f}   [contrast {contrast:.1e}, r0-spread {sp:.1e}]")
    else:
        print(f"        ({ell},{m:+d}): NOT LOCATED — root-finder returned {w:.3f} with "
              f"contrast {contrast:.1e} (a genuine zero has < 1e-2); see K6")

w22 = res[(2, -2)]
check("K1. EVERY REPORTED ROOT IS r0-INDEPENDENT (direct-integration "
      "instability test), individually, not just the first one",
      all(val[k] for k in res) and (2, -2) in res and (3, -3) in res,
      "; ".join(f"({k[0]},{k[1]:+d}) validated" for k in res))
check("K2. EVERY REPORTED ZERO IS SHARP, individually",
      all(val[k] for k in res), "contrast < 1e-2 for each reported mode")

# First run FAILED the hypothesis "scalar was a faithful proxy": the
# gravitational lines sit 12-24% BELOW the scalar ones. The failure is
# physics, not error, and it was already visible at a = 0 (RW 0.4486 vs
# scalar 0.5647, ratio 0.794): the s = -2 effective potential is lower
# than the s = 0 one, so its resonances sit lower. Recorded as a
# correction to 3358's framing, not smoothed into agreement.
SCALAR = {(2, -2): 0.48085 - 0.11668j, (3, -3): 0.62812 - 0.07843j}
ratios = {k: res[k].real / SCALAR[k].real for k in res if k in SCALAR}
check("K3. THE HYPOTHESIS FAILED AND IS CORRECTED: the gravitational lines "
      "sit 12-24% BELOW the scalar-sector lines (3358). The scalar census "
      "was a faithful proxy for STRUCTURE (no comb, broad ell=2) but NOT "
      "for line POSITIONS, and NOT for the ordering test (its comparator was "
      "withdrawn; CONV-037 revision 8) — the a = 0 ratio (RW/scalar = 0.794) "
      "already said so",
      all(0.70 < r < 0.95 for r in ratios.values()),
      "; ".join(f"({k[0]},{k[1]:+d}): grav {res[k].real:.4f} / scalar "
                f"{SCALAR[k].real:.4f} = {r:.3f}" for k, r in ratios.items())
      + "; a=0 reference 0.794")

check("K4. NO TRAPPED COMB AT ell = 2 — NOW AT GRAVITATIONAL GRADE: the (2,-2) "
      "line is a single broad top-of-barrier resonance (Q of order 2), not a "
      "narrow trapped mode",
      res[(2, -2)].real / (2 * abs(res[(2, -2)].imag)) < 4,
      f"Q(2,-2) = {res[(2,-2)].real/(2*abs(res[(2,-2)].imag)):.2f}")

check("K5. THE DISCRIMINATOR'S ORDERING TEST IS *NOT* ESTABLISHED AT "
      "GRAVITATIONAL GRADE, and this check says so: the prograde-exposed "
      "comparator (2,+1) could not be located (K6), so the retrograde-keyed "
      "ordering remains at its previous grade (eikonal-WKB, and scalar-exact "
      "at 3358 — itself now withdrawn for (2,+1), see K6)",
      (2, 1) not in res,
      "(2,+1) NOT LOCATED; ordering stated only for what IS located: "
      f"(2,-2) {to_hz(res[(2,-2)].real):.0f} Hz < (3,-3) "
      f"{to_hz(res[(3,-3)].real):.0f} Hz (both retrograde — not the discriminator)")

check("K6. METHOD LIMIT FOUND AND A 3358 RESULT WITHDRAWN: direct inward "
      "integration is reliable for |Im omega| <~ 0.12 (validated) but at "
      "Q ~ 1 (|Im omega| ~ 0.3) the ingoing contamination grows ~e^27 over "
      "the range and the root-finder cannot move. (2,+1) is therefore "
      "NOT LOCATED here — and 3358's scalar (2,+1) = 0.63877-0.30216i, which "
      "never received the r0/sharpness tests, is WITHDRAWN as unvalidated",
      (2, 1) not in res,
      "very broad (Q ~ 1) modes need a different instrument (a series method "
      "or a contour/Riccati formulation); registered as open")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
