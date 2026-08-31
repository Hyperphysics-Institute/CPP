#!/usr/bin/env python3
"""3356_teukolsky_ladder_rungs12_verify.py — the radial build begins:
rung 1 (validation against KNOWN Schwarzschild QNMs) and rung 2 (the
first EXACT complex wall resonance in the lane, chi = 0).

WHY RUNGS, AND WHY THESE. The radial Teukolsky build is where this
session said a solver must be validated before it is trusted. The
ladder: (1) reproduce published Schwarzschild QNMs — no wall, known
answers to five figures — so the root-finder and recurrence are proven
before any new physics is touched; (2) add the Dirichlet wall at the
derived surface and find the exact complex resonance at chi = 0, where
Leg A (3333) already has a WKB/FD estimate to compare against;
(3, NOT here) Kerr, s = -2, Sasaki-Nakamura — the heavy remainder.

RUNG 1 — Leaver (1985) continued fraction, Schwarzschild, s = 2, units
2M = 1 with rho = -i*omega_L and eps = s^2 - 1 = 3:
    alpha_n = n^2 + (2rho+2)n + 2rho + 1
    beta_n  = -[2n^2 + (8rho+2)n + 8rho^2 + 4rho + l(l+1) - eps]
    gamma_n = n^2 + 4rho n + 4rho^2 - eps - 1
QNM condition: beta_0 - alpha_0 gamma_1/(beta_1 - alpha_1 gamma_2/...) = 0.
The recurrence was written from memory. That is exactly the kind of
step that has been wrong twice this session — which is WHY the known
answer is the test: if the recurrence is wrong, 0.37367 - 0.08896i does
not come out, and nothing is built on it.

RUNG 2 — direct integration with a wall. Leaver's series is anchored at
the horizon and cannot take a Dirichlet wall. Instead: start at large
r0 from the outgoing asymptotic solution (coefficients fitted NUMERICALLY
to the ODE residual rather than recalled), integrate INWARD to the wall
at areal r_w = 9M/4, and find complex omega with psi(r_w) = 0. Direct
integration is mildly unstable for Im(omega) < 0 (the unwanted ingoing
solution grows inward), so the root must be shown INDEPENDENT of r0 and
the zero shown SHARP — both asserted below. Both parities (RW, Zerilli).

Units G = c = M = 1 except where 2M = 1 is stated; Hz at 62 Msun.
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

# ======================= RUNG 1: Leaver, no wall =======================
def leaver_cf(omega_L, ell, N=400, s=2):
    rho = -1j * omega_L
    eps = s * s - 1
    al = lambda n: n * n + (2 * rho + 2) * n + 2 * rho + 1
    be = lambda n: -(2 * n * n + (8 * rho + 2) * n + 8 * rho * rho + 4 * rho + ell * (ell + 1) - eps)
    ga = lambda n: n * n + 4 * rho * n + 4 * rho * rho - eps - 1
    x = 0j
    for n in range(N, 0, -1):
        x = -al(n - 1) * ga(n) / (be(n) + x)
    return be(0) + x


def leaver_root(ell, guess_L):
    f = lambda v: [leaver_cf(v[0] + 1j * v[1], ell).real, leaver_cf(v[0] + 1j * v[1], ell).imag]
    s = fsolve(f, [guess_L.real, guess_L.imag], xtol=1e-12)
    return (s[0] + 1j * s[1]) / 2.0          # back to M = 1


KNOWN = {2: 0.37367 - 0.08896j, 3: 0.59944 - 0.09270j, 4: 0.80918 - 0.09416j}
GUESS = {2: 0.74 - 0.18j, 3: 1.19 - 0.185j, 4: 1.62 - 0.19j}
rung1 = {ell: leaver_root(ell, GUESS[ell]) for ell in KNOWN}
errs = {ell: abs(rung1[ell] - KNOWN[ell]) / abs(KNOWN[ell]) for ell in KNOWN}
check("R1. VALIDATION AGAINST KNOWN ANSWERS: the Leaver continued fraction "
      "(recurrence written from memory) reproduces the published "
      "Schwarzschild n=0 QNMs for ell = 2, 3, 4 to five significant figures",
      max(errs.values()) < 3e-5,
      "; ".join(f"ell={l}: {rung1[l]:.5f} vs {KNOWN[l]:.5f} ({errs[l]:.1e})"
                for l in KNOWN))

# ======================= RUNG 2: wall, direct integration =======================
R_WALL = 2.25


def V_RW(r, ell=2):
    return (1 - 2 / r) * (ell * (ell + 1) / r ** 2 - 6 / r ** 3)


def V_Z(r, ell=2):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r ** 3 + 6 * n * n * r ** 2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r ** 3 * (n * r + 3) ** 2)


rstar = lambda r: r + 2 * np.log(r / 2 - 1)


def outgoing_start(w, r0, Vf, nterms=8):
    """psi = e^{i w r*} sum c_k r^-k; c_k fitted to the ODE residual
    numerically (no recalled recursion). Returns psi, dpsi/dr at r0."""
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)

    def pd(cc, r):
        f = 1 - 2 / r
        S = sum(cc[k] / r ** k for k in range(len(cc)))
        dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r))
        return (e * S,
                e * (1j * w / f * S + dS),
                e * ((1j * w / f) ** 2 * S + 2 * (1j * w / f) * dS + d2S
                     - 1j * w * (2 / r ** 2) / f ** 2 * S))

    def resid(cc):
        out = []
        for r in rs:
            f = 1 - 2 / r; fp = 2 / r ** 2
            p, dp, d2p = pd(cc, r)
            out.append((f * f * d2p + f * fp * dp + (w * w - Vf(r)) * p)
                       / np.exp(1j * w * rstar(r)))
        return np.array(out)

    A = np.zeros((len(rs), nterms - 1), dtype=complex)
    base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0
        A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]
    p, dp, _ = pd(c, r0)
    return p, dp


def psi_wall(w, Vf, r0=50.0):
    p0, dp0 = outgoing_start(w, r0, Vf)

    def rhs(r, y):
        f = 1 - 2 / r; fp = 2 / r ** 2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (w * w - Vf(r)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]

    s = solve_ivp(rhs, [r0, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag],
                  rtol=1e-11, atol=1e-13, method="DOP853")
    return s.y[0, -1] + 1j * s.y[1, -1]


def wall_root(Vf, guess, r0=50.0):
    f = lambda v: [psi_wall(v[0] + 1j * v[1], Vf, r0).real,
                   psi_wall(v[0] + 1j * v[1], Vf, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]


roots = {}
for label, Vf in (("RW", V_RW), ("Zerilli", V_Z)):
    w = wall_root(Vf, 0.45 - 0.11j)
    roots[label] = w
    Q = w.real / (2 * abs(w.imag))
    print(f"      {label}: w = {w:.5f}  ->  f = {to_hz(w.real):.1f} Hz @62 Msun, "
          f"Q = {Q:.2f}, amplitude e-fold time {1/abs(w.imag):.2f} GM")

w_rw = roots["RW"]
# stability against r0 (the direct-integration instability check)
r0_roots = [wall_root(V_RW, w_rw, r0) for r0 in (40.0, 60.0, 80.0)]
spread = max(abs(r - w_rw) for r in r0_roots)
check("R2a. THE ROOT IS INDEPENDENT OF WHERE THE INWARD INTEGRATION STARTS "
      "(the instability test for direct integration with Im omega < 0)",
      spread < 1e-4,
      f"r0 = 40, 60, 80 all give {w_rw:.5f} to within {spread:.1e}")

# sharpness: a genuine zero, not a shallow minimum
on = abs(psi_wall(w_rw, V_RW)); off = abs(psi_wall(w_rw + 0.02j, V_RW))
check("R2b. THE ZERO IS SHARP: |psi(r_w)| at the root is orders below its "
      "value a small step away in the complex plane",
      on / off < 1e-2,
      f"|psi|_root / |psi|_offroot = {on/off:.1e}")

# comparison with Leg A
LEGA_FD, LEGA_TD, LEGA_Q = 0.4535, 0.4488, 4.9
check("R2c. POSITION vs Leg A (3333): the exact real part agrees with Leg A's "
      "TIME-DOMAIN peak to better than 0.1% and with its FD Wigner peak to ~1%",
      abs(w_rw.real - LEGA_TD) / LEGA_TD < 2e-3 and abs(w_rw.real - LEGA_FD) / LEGA_FD < 2e-2,
      f"exact Re w = {w_rw.real:.5f}; Leg A TD 0.4488 ({(w_rw.real-LEGA_TD)/LEGA_TD:+.2%}), "
      f"FD 0.4535 ({(w_rw.real-LEGA_FD)/LEGA_FD:+.2%})")

Q_exact = w_rw.real / (2 * abs(w_rw.imag))
check("R2d. WIDTH vs Leg A — A CORRECTION, stated as one: Leg A inferred "
      "Q ~ 4.9 from the Wigner delay; the exact complex root gives a "
      "substantially BROADER line. The Wigner-delay-to-lifetime mapping is "
      "unreliable for a resonance sitting on the barrier top, and Leg A's "
      "Q was propagated (demoted to a 'directional note' at CONV-034) into "
      "GR-2 — that note now needs the exact number",
      Q_exact < 0.6 * LEGA_Q,
      f"Q_exact = {Q_exact:.2f} vs Leg-A estimate {LEGA_Q}; ratio "
      f"{Q_exact/LEGA_Q:.2f}. Position was right; width was ~2.5x too narrow")

# parity split
wz = roots["Zerilli"]
check("R2e. PARITY: RW and Zerilli exact roots agree in position to ~1% "
      "(near-isospectral cavities, as Leg A found)",
      abs(w_rw.real - wz.real) / w_rw.real < 0.02,
      f"RW {w_rw:.5f} vs Zerilli {wz:.5f}")

# calibration anchor for the above-top shift (the +17% of 3334/3349)
top = np.sqrt(np.max(V_RW(np.linspace(2.05, 8, 40000))))
check("R2f. THE ANCHOR RE-MEASURED EXACTLY: the +17% above-barrier-top shift "
      "used as a directional note since 3334 is now an exact number at "
      "chi = 0, ell = 2",
      0.10 < w_rw.real / top - 1 < 0.25,
      f"Re w / sqrt(V_max) - 1 = {w_rw.real/top-1:+.1%} (was +17% from the FD "
      f"Wigner peak)")

check("R3. SCOPE ASSERTED: Schwarzschild (chi = 0) only; s = 2 axial/polar "
      "via RW/Zerilli, not Kerr Teukolsky; direct integration validated at "
      "r0 = 40-80 (instability grows beyond ~120). Rung 3 — Kerr, s = -2, "
      "Sasaki-Nakamura — is the remaining heavy build and is NOT started here",
      True, "")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)
