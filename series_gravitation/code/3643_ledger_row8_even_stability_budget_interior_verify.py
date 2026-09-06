#!/usr/bin/env python3
"""
Patch 3643 verify — PD-007 triangulation ledger ROW 8 (3641 §4): 3390's even-sector wall instability (b2 < 0,
growing modes at r_w = 8M/3) re-run with the THEO-PCD-BUDGET interior (3640) in place of the trace-pinned wall.
A fail here fails the extension (3641 §2 rule 5). [PCD-EXT]

What changes. 3378/3383/3390 modelled the even (polar) sector's surface as the zero-compliance limit of the
count channel: the trace pinned at the level set, H2 + 2K = 0, which is the Robin law beta_l(omega) = b0 - b2 w^2
on the exterior Zerilli function. Beyond ~2.4M both b0 and b2 flip sign; at the ratified surface 8M/3 the
boundary 'mass' b2 is NEGATIVE and the poles have Im w > 0 (3390: 0.5199 + 0.034i, l = 2; 0.7665 + 0.036i, l = 3).
Under the budget law the register is NOT pinned: the count keeps recording above the cap at the scaled rate
(v_eff = 2 cap - cap^2/v), the metric is C^1 through the surface (sigma = P = 0, 3640 §3), and the wave
transmits inward with the coordinate speed N/psi^2 of the budget metric (3389's lattice hop per Moment; 3639 §4
'collision ringing transmits internally'). So the even sector becomes the same kind of problem 3384 solved for the
odd sector — transmit to a regular centre — with a GRADED interior instead of a flat one, and with the interface
rule 3384 used (master function and its rbar-derivative continuous; dr*/drbar = J at the surface).

Interior model (least assumption, same as 3384/3621): the master function u = rbar * Phi with Phi a minimally
coupled scalar on the budget metric  g = -N^2 dt^2 + psi^4 (drbar^2 + rbar^2 dOmega^2),  N = N(v_eff), psi = psi(v_eff):
    d/drbar (N psi^2 rbar^2 Phi') + [ w^2 psi^6 rbar^2 / N - N psi^2 l(l+1)] Phi = 0,  Phi ~ rbar^l at the centre.
With N, psi frozen at their surface values this is exactly 3384's Riccati-Bessel interior with k = J w (checked).
The wall law on the exterior Zerilli function: beta(w) = (1/J) (u'/u)|_R,  J = dr*/drbar|_R = psi^2/N|_surface.

Checked here:
 (1) J at 8M/3 is 32/9 = 3.556 from the exterior dictionary AND equals psi^2/N of the budget interior at the
     surface: the wave speed is continuous through the C^1 surface (no impedance step). Note: 3390 carried
     J = 6.75 (the 9M/4 value) into its odd-sector line at 8M/3 — flagged, not fixed here (odd sector is not row 8).
 (2) flat-core limit reproduces the Riccati-Bessel wall (1/J) k g(k mu) to 1e-8.
 (3) beta(w) is REAL on the real axis (lossless interior, |R| = 1) and its low-frequency law beta = b0 - b2 w^2 has
     b2 > 0: the boundary mass is the core's INERTIA, positive. The negative b2 was the clamp's, not the theory's.
 (4) the poles for l = 2, 3 at 8M/3 under the budget wall: Im w < 0 (damped); r0-independent; sharp.
 (5) ARGUMENT PRINCIPLE: the winding number of F(w) around a rectangle in the UPPER half-plane
     (Re w in [0.05, 1.2], Im w in [0.005, 0.4]) is >= 1 for 3390's trace wall (the growing pole is inside) and
     0 for the budget wall — no growing mode anywhere in the band, not just none near the guess.
 (6) the interior-cavity family (first standing wave) sits ABOVE the l = 2 line; the flat-core reference and the
     3390 numbers for comparison.
Runtime: the contour counts take a few minutes; run under nohup.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
from scipy.special import spherical_jn

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ---------------------------------------------------------------- geometry (M = 1)
CAP = 2.0 / 3.0
RB = 1.5                                   # isotropic surface radius, v = 2/3 -> areal 8M/3
R_WALL = 8.0 / 3.0
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)

v_in = lambda rb: (1.0 / (2 * RB)) * (3 - rb**2 / RB**2)          # uniform count in lattice coordinates (3639 §3)
v_eff = lambda v: 2 * CAP - CAP**2 / v                             # THEO-PCD-BUDGET (3640)
Nf = lambda v: (1 - v / 2) / (1 + v / 2)
psif = lambda v: 1 + v / 2


def NP(rb, flat=False):
    v = CAP if flat else v_eff(v_in(rb))
    return Nf(v), psif(v)


# (1) J: exterior dictionary vs interior speed at the surface
J_ext = (1 / (1 - 2 / R_WALL)) * psif(CAP) * (1 - CAP / 2)        # dr*/dr * dr/drbar
N_s, psi_s = NP(RB)
J_int = psi_s**2 / N_s
print(f"J = dr*/drbar at 8M/3: exterior dictionary {J_ext:.6f} (= 32/9 = {32/9:.6f}); interior psi^2/N at the surface {J_int:.6f}")
check("(1) J = 32/9 at 8M/3 from the exterior map, and the budget interior's psi^2/N at the surface is the same number: the wave speed is continuous through the C^1 surface",
      abs(J_ext - 32 / 9) < 1e-12 and abs(J_int - J_ext) < 1e-12, f"J = {J_ext:.4f}")
check("(1b) 3390's odd-sector line used J = 6.75 (the 9M/4 value) at 8M/3; the dictionary value there is 32/9 — flagged for the odd sector (not row 8)", abs(6.75 - J_ext) > 1)
J = J_ext
print(f"    interior speed N/psi^2: surface {N_s/psi_s**2:.4f}, centre {NP(1e-9)[0]/NP(1e-9)[1]**2:.4f}  (graded: slower inward)")


# ---------------------------------------------------------------- interior: regular scalar on the budget metric
def interior_logderiv(wc, ell, flat=False, r_in=1e-3):
    """returns (u'/u) at rbar = RB for u = rbar*Phi, Phi the regular solution; complex omega."""
    def rhs(rb, y):
        N, psi = NP(rb, flat)
        # d/drb (P Phi') + Q Phi = 0, P = N psi^2 rb^2, Q = w^2 psi^6 rb^2/N - N psi^2 l(l+1)
        # numerical P' by finite difference (P is smooth)
        h = 1e-6
        Np, pp = NP(rb + h, flat); Nm, pm = NP(rb - h, flat)
        P = N * psi**2 * rb**2
        dP = (Np * pp**2 * (rb + h)**2 - Nm * pm**2 * (rb - h)**2) / (2 * h)
        Q = wc * wc * psi**6 * rb**2 / N - N * psi**2 * ell * (ell + 1)
        Phi = y[0] + 1j * y[1]; dPhi = y[2] + 1j * y[3]
        d2 = -(dP * dPhi + Q * Phi) / P
        return [dPhi.real, dPhi.imag, d2.real, d2.imag]
    y0 = [r_in**ell, 0.0, ell * r_in**(ell - 1), 0.0]
    s = solve_ivp(rhs, [r_in, RB], y0, rtol=1e-11, atol=1e-14, method="DOP853")
    Phi = s.y[0, -1] + 1j * s.y[1, -1]; dPhi = s.y[2, -1] + 1j * s.y[3, -1]
    u = RB * Phi; du = Phi + RB * dPhi
    return du / u


def interior_u(wc, ell, r_in=1e-3):
    """(u, du/drbar) at the surface, unnormalised — for the pole-free wall function."""
    def rhs(rb, y):
        N, psi = NP(rb)
        h = 1e-6
        Np, pp = NP(rb + h); Nm, pm = NP(rb - h)
        P = N * psi**2 * rb**2
        dP = (Np * pp**2 * (rb + h)**2 - Nm * pm**2 * (rb - h)**2) / (2 * h)
        Q = wc * wc * psi**6 * rb**2 / N - N * psi**2 * ell * (ell + 1)
        Phi = y[0] + 1j * y[1]; dPhi = y[2] + 1j * y[3]
        d2 = -(dP * dPhi + Q * Phi) / P
        return [dPhi.real, dPhi.imag, d2.real, d2.imag]
    y0 = [r_in**ell, 0.0, ell * r_in**(ell - 1), 0.0]
    s = solve_ivp(rhs, [r_in, RB], y0, rtol=1e-11, atol=1e-14, method="DOP853")
    Phi = s.y[0, -1] + 1j * s.y[1, -1]; dPhi = s.y[2, -1] + 1j * s.y[3, -1]
    return RB * Phi, Phi + RB * dPhi


def beta_budget(wc, ell, flat=False):
    return interior_logderiv(wc, ell, flat) / J


def g_of(x, ell):
    j = spherical_jn(ell, x); jp = spherical_jn(ell, x, derivative=True)
    return (j + x * jp) / (x * j)


def beta_rb(wc, ell):                       # 3384's flat-core Riccati-Bessel law, k = J w
    k = J * wc
    return (1.0 / J) * k * g_of(k * RB, ell)


# (2) flat-core limit
for ell in (2, 3):
    errs = [abs(beta_budget(w, ell, flat=True) - beta_rb(w, ell)) for w in (0.1, 0.3 - 0.05j, 0.6 + 0.02j)]
    check(f"(2) l = {ell}: with N, psi frozen at the surface the interior reduces to 3384's Riccati-Bessel wall (1/J) k g(k mu) — agreement 1e-8",
          max(errs) < 1e-8, f"max |diff| = {max(errs):.1e}")

# (3) real on the real axis; low-frequency boundary mass
ws = np.array([0.02, 0.04, 0.06, 0.08, 0.10])
for ell in (2, 3):
    bs = np.array([beta_budget(w, ell) for w in ws])
    check(f"(3a) l = {ell}: beta(omega) is real on the real axis (lossless, |R| = 1)", np.max(np.abs(bs.imag)) < 1e-9)
    # fit b0 - b2 w^2 (+ b4 w^4)
    A = np.vstack([np.ones_like(ws), -ws**2, ws**4]).T
    b0, b2, _ = np.linalg.lstsq(A, bs.real, rcond=None)[0]
    b2_flat = J * RB / (2 * ell + 3)      # Riccati-Bessel: beta = (l+1)/(J mu) - J mu w^2/(2l+3) + ...
    print(f"    l = {ell}: budget wall  beta = {b0:+.4f} - ({b2:+.4f}) w^2 ;  flat-core reference b0 = {(ell+1)/(J*RB):+.4f}, b2 = {b2_flat:+.4f}")
    check(f"(3b) l = {ell}: the boundary 'mass' b2 is POSITIVE — the core's inertia (3390's trace wall had b2 < 0: l=2 -0.85, l=3 -0.99 in the 3383 convention)", b2 > 0, f"b2 = {b2:+.4f}")
    check(f"(3c) l = {ell}: b0 > 0 (a restoring boundary, no Neumann crossing from below)", b0 > 0, f"b0 = {b0:+.4f}")


# ---------------------------------------------------------------- exterior (3356/3390 machinery, verbatim)
def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)


def outgoing_start(wc, r0, Vf, nterms=8):
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)
    def pd(cc, rr):
        f = 1 - 2 / rr
        S = sum(cc[k] / rr**k for k in range(len(cc))); dS = sum(-k * cc[k] / rr**(k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / rr**(k + 2) for k in range(len(cc)))
        e = np.exp(1j * wc * rstar(rr))
        return (e * S, e * (1j * wc / f * S + dS), e * ((1j * wc / f) ** 2 * S + 2 * (1j * wc / f) * dS + d2S - 1j * wc * (2 / rr**2) / f**2 * S))
    def resid(cc):
        out = []
        for rr in rs:
            f = 1 - 2 / rr; fp = 2 / rr**2; p, dp, d2p = pd(cc, rr)
            out.append((f * f * d2p + f * fp * dp + (wc * wc - Vf(rr)) * p) / np.exp(1j * wc * rstar(rr)))
        return np.array(out)
    A = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]
    p, dp, _ = pd(c, r0); return p, dp


def wall_values(wc, Vf, r0):
    p0, dp0 = outgoing_start(wc, r0, Vf)
    def rhs(rr, y):
        f = 1 - 2 / rr; fp = 2 / rr**2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - Vf(rr)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    s = solve_ivp(rhs, [r0, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    psi = s.y[0, -1] + 1j * s.y[1, -1]; dpsi = s.y[2, -1] + 1j * s.y[3, -1]
    return psi, (1 - 2 / R_WALL) * dpsi


# 3390's trace-wall coefficients at 8M/3 (recomputed symbolically, 3378 pipeline) — the CONTROL
r_, M_, w_ = sp.symbols("r M omega", positive=True)
def beta_sym(ell, rw):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M_ / r_; Lam = lam * r_ + 3 * M_
    Z = sp.Function("Z")(r_); Zp = sp.diff(Z, r_)
    Vp = f * (2 * lam**2 * (lam + 1) * r_**3 + 6 * lam**2 * M_ * r_**2 + 18 * lam * M_**2 * r_ + 18 * M_**3) / (r_**3 * Lam**2)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r_) + (w_**2 - Vp) * Z, 0), sp.diff(Z, r_, 2))[0]
    A = (lam * (lam + 1) * r_**2 + 3 * lam * M_ * r_ + 6 * M_**2) / (r_**2 * Lam)
    K = f * Zp + A * Z; Kp = sp.diff(K, r_).subs(sp.diff(Z, r_, 2), Zpp)
    H2 = Lam / (r_ * f) * ((lam + 1) * Z / r_ - K) + r_ * Kp
    tr = sp.expand(sp.simplify(H2 + 2 * K)); tc2 = sp.simplify(tr.coeff(Zp)); tc1 = sp.simplify((tr - tc2 * Zp).coeff(Z))
    b = sp.simplify((f * (-tc1 / tc2)).subs({r_: rw * M_}).subs(M_, 1))
    return float(b.subs(w_, 0)), -float(sp.diff(b, w_, 2) / 2)
TRACE = {ell: beta_sym(ell, sp.Rational(8, 3)) for ell in (2, 3)}
check("(control) 3390's trace wall at 8M/3 reproduced: b0 < 0 and b2 < 0 for l = 2, 3", all(TRACE[l][0] < 0 and TRACE[l][1] < 0 for l in (2, 3)),
      "; ".join(f"l={l}: {b0:+.3f} - ({b2:+.3f}) w^2" for l, (b0, b2) in TRACE.items()))


def F(wc, ell, wall, r0=50.0):
    Vf = lambda rr: V_Z(rr, ell)
    psi, dpsi_rs = wall_values(wc, Vf, r0)
    if wall == "D": return psi
    if wall == "trace":
        b0, b2 = TRACE[ell]; return dpsi_rs - (b0 - b2 * wc * wc) * psi
    if wall == "budget":
        ld = interior_logderiv(wc, ell)              # u'/u at the surface
        return dpsi_rs - (ld / J) * psi
    if wall == "budget_entire":                      # pole-free form u*dpsi - (u'/J)*psi (same zeros, no interior-resonance poles)
        u, du = interior_u(wc, ell)
        return u * dpsi_rs - (du / J) * psi
    if wall == "flat": return dpsi_rs - beta_rb(wc, ell) * psi


def root(ell, wall, guess, r0=50.0):
    fn = lambda v: [F(v[0] + 1j * v[1], ell, wall, r0).real, F(v[0] + 1j * v[1], ell, wall, r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]


# (4) the poles
print("Poles at r_w = 8M/3 (M = 1; Hz at 62 Msun)")
poles = {}
for ell, gD, gB in ((2, 0.42 - 0.15j, 0.42 - 0.08j), (3, 0.63 - 0.18j, 0.65 - 0.08j)):
    wD = root(ell, "D", gD)                      # Dirichlet reference: direct integration is mildly unstable at Im w ~ -0.2 (3390 note); the root is the 3390 value to 1e-3
    wT = root(ell, "trace", {2: 0.52 + 0.034j, 3: 0.766 + 0.036j}[ell])
    wF = root(ell, "flat", gB)
    wB = root(ell, "budget", gB)
    poles[ell] = dict(D=wD, T=wT, F=wF, B=wB)
    for lab, ww in (("Dirichlet (reference)", wD), ("trace-pinned Robin (3390, the clamp)", wT),
                    ("flat core, J = 32/9 (chi = 0 interior, transmit)", wF), ("BUDGET interior, N/psi^2 graded [PCD-EXT]", wB)):
        print(f"    l = {ell} {lab:48s}: w = {ww.real:.5f} {ww.imag:+.5f} i   ({to_hz(ww.real):.0f} Hz)   Q = {ww.real/(2*abs(ww.imag)):.2f}")
check("(4a) control: 3390's growing even poles reproduced (Im > 0, l = 2 and 3)", poles[2]["T"].imag > 0 and poles[3]["T"].imag > 0,
      f"l=2 {poles[2]['T']:.4f}, l=3 {poles[3]['T']:.4f}")
check("(4b) ROW 8: under the budget interior the even-sector poles are DAMPED (Im < 0) for l = 2 and l = 3",
      poles[2]["B"].imag < 0 and poles[3]["B"].imag < 0, f"l=2 {poles[2]['B']:.5f}, l=3 {poles[3]['B']:.5f}")
for ell in (2, 3):
    rr0 = [root(ell, "budget", poles[ell]["B"], r0) for r0 in (40.0, 60.0, 80.0)]
    spread = max(abs(x - poles[ell]["B"]) for x in rr0)
    check(f"(4c) l = {ell} budget pole r0-independent (1e-4)", spread < 1e-4, f"spread {spread:.1e}")
    wB = poles[ell]["B"]; f0 = abs(F(wB, ell, "budget")); f1 = abs(F(wB + 0.01, ell, "budget"))
    check(f"(4d) l = {ell} budget pole is sharp (|F| rises > 1e3x at +0.01 off the root)", f1 / max(f0, 1e-300) > 1e3, f"ratio {f1/max(f0,1e-300):.1e}")


# (5) argument principle in the upper half-plane
def winding(ell, wall, re=(0.05, 1.2), im=(0.005, 0.4), n=60):
    pts = []
    pts += [complex(x, im[0]) for x in np.linspace(re[0], re[1], n)]
    pts += [complex(re[1], y) for y in np.linspace(im[0], im[1], n // 2)]
    pts += [complex(x, im[1]) for x in np.linspace(re[1], re[0], n)]
    pts += [complex(re[0], y) for y in np.linspace(im[1], im[0], n // 2)]
    vals = np.array([F(w, ell, wall) for w in pts])
    ph = np.unwrap(np.angle(vals)); return (ph[-1] - ph[0] + np.angle(vals[0]) - np.angle(vals[-1])) / (2 * np.pi), np.abs(np.diff(ph)).max()
for ell in (2, 3):
    nT, jT = winding(ell, "trace")
    nB, jB = winding(ell, "budget_entire", n=80)
    print(f"    l = {ell}: winding number in the upper half-plane  trace wall {nT:+.3f} (max phase step {jT:.2f}),  budget wall {nB:+.3f} (max phase step {jB:.2f})")
    check(f"(5a) l = {ell} control: the trace wall has >= 1 zero of F in the upper half-plane (the growing mode)", round(nT) >= 1 and jT < 2.5)
    check(f"(5b) l = {ell} ROW 8: the budget wall (pole-free form u psi' - u' psi/J) has NO zero in the upper half-plane (Re w 0.05-1.2, Im w 0.005-0.4): no growing even mode in the band",
          round(nB) == 0 and jB < 1.5, f"winding {nB:+.3f}, max phase step {jB:.2f}")

# (6) interior cavity family and the line's position
opt = 0.0
rbs = np.linspace(1e-6, RB, 20001); Ns, ps = zip(*[NP(rb) for rb in rbs]); opt = np.trapezoid(np.array(ps)**2 / np.array(Ns), rbs)
w_cav = 5.7635 / opt                    # first zero of x j_2(x) over the interior optical depth, WKB-flat estimate
print(f"    interior optical depth (centre -> surface) {opt:.3f} (flat-core value J mu = {J*RB:.3f}, ratio {opt/(J*RB):.3f} = 3640's 1.363)")
print(f"    first interior standing wave (l = 2), estimate Mw ~ {w_cav:.3f} ({to_hz(w_cav):.0f} Hz); the l = 2 line sits at {poles[2]['B'].real:.3f}")
check("(6a) the interior optical depth is 1.363x the flat-core value — the same number as 3640's echo-cavity ratio (one geometry, two readings)", abs(opt / (J * RB) - 1.3628) < 2e-3)
check("(6b) the first interior standing wave sits ABOVE the l = 2 line (it does not split the mode, cf. 3621's Kerr-surface lossless-core problem)", w_cav > poles[2]["B"].real + 0.1)
check("(6c) row 8 verdict: PASSES — the instability was the clamp's (a negative boundary mass); the budget interior's boundary mass is positive, its poles are damped, and the upper half-plane is empty. [PCD-EXT] until the ledger closes", poles[2]["B"].imag < 0 and poles[3]["B"].imag < 0)

print()
print(f"3643 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
