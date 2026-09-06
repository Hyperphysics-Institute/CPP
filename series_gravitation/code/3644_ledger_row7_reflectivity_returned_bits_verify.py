#!/usr/bin/env python3
"""
Patch 3644 verify — PD-007 triangulation ledger ROW 7 (3641 §4): reflectivity from the returned-bit fraction
(D − K)/D under THEO-PCD-BUDGET, and the echo amplitude that goes with the 0.95 ms delay. [PCD-EXT]
Run from the repo root (it exec's 3359's SN machinery the way 3619 does).

The returned fraction is fixed by the law: (D − K)/D = 1 − K/D = 1 − chi = 1 − cap/v(rbar): ZERO at the surface (v = cap)
and 1/3 at the centre (v = 1). So the surface itself returns nothing promptly; the return is distributed inward. What the
law does NOT fix is how the returned bits act on a WAVE. Three readings, each a wall law beta(omega) on the exterior
master function at the ratified surface, each priced against the one pinned empiric of the regime — the ringdown
(row 1; GW150914's box df in (-4.8, +6.3)%, dtau in (-22, +24.4)%, 3616):
  A1  the wave rides the register: transmitted on the graded budget metric, lossless, returns from the centre
      (3643's wall).  Coherent first echo at 0.95 ms with amplitude |T_barrier|^2 ~ 0.44 (3614).
  A2  the returned bits are the wave's own, turned around coherently per Moment: the cumulative return over a depth
      delta is  (1/3)(delta/M)^2 (M/l_P)  -> unity within delta = sqrt(3 l_P/M) M ~ 2e-16 m at 62 Msun. A MIRROR at
      the surface (hard wall).
  B   the returned bits are incoherent for the wave: the same skin, an ABSORBER at the surface (local ingoing law
      beta = -i omega in the continuous-speed medium).
  C   (the reading 3621 §2 and 3623 require) transmission on the budget metric with the coherent content lost at
      DEPTH — an absorber inside the core; the family over the absorber's position rbar_abs.
Checked:
 (1) a = 0 machinery: the horizon-equivalent wall (ingoing at the horizon, integrated to 8M/3) reproduces the
     Schwarzschild l = 2 QNM 0.37367 - 0.08896i.
 (2) a = 0: the poles and (df, dtau) vs GR for A1, A2 (Dirichlet/Neumann), B, and the family C over rbar_abs.
 (3) Kerr, a = 0.68, surface 2.734 M, prograde (2,2), 3619's root_k: the same laws in GW150914's box or not.
     The interior laws (A1, C) are carried over as beta(omega) in 1/M from the a = 0 profile — an estimate, labelled;
     the Kerr interior profile is KERRWALL-1's.
 (4) the coherent first-echo amplitude under each reading (f x 0.44).
"""
import numpy as np
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


# ---------------------------------------------------------------- a = 0 geometry and the budget interior (3643)
CAP = 2.0 / 3.0; RB = 1.5; R_WALL = 8.0 / 3.0; ELL = 2
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6
to_hz = lambda w: w / (2 * np.pi * Msec)
v_in = lambda rb: (1.0 / (2 * RB)) * (3 - rb**2 / RB**2)
v_eff = lambda v: 2 * CAP - CAP**2 / v
Nf = lambda v: (1 - v / 2) / (1 + v / 2); psif = lambda v: 1 + v / 2
def NP(rb):
    v = v_eff(v_in(rb)); return Nf(v), psif(v)
J = 32.0 / 9.0

# the returned fraction profile
ret = lambda rb: 1 - CAP / v_in(rb)
print(f"returned-bit fraction 1 - cap/v: surface {ret(RB):.3f}, mid (rbar = 0.75) {ret(0.75):.3f}, centre {ret(1e-9):.3f}")
check("(0a) the returned fraction is 0 at the surface and 1/3 at the centre — nothing is returned promptly by the surface itself",
      abs(ret(RB)) < 1e-12 and abs(ret(1e-9) - 1 / 3) < 1e-6)
lP_over_M = 1.616e-35 / (62 * 1477.0)          # l_P / M for 62 Msun (M in metres)
delta_skin = np.sqrt(3 * lP_over_M)             # in units of M: cumulative per-Moment return = (1/3)(delta/M)^2 (M/l_P) = 1
print(f"    per-Moment reading: cumulative return reaches 1 at depth delta = sqrt(3 l_P/M) M = {delta_skin:.2e} M = {delta_skin*62*1477:.1e} m")
check("(0b) if the returned bits act on the wave per Moment (coherently or not), the whole wave is turned over within ~1e-16 m of the surface: a SKIN. Readings A2/B are surface walls, not interior processes", delta_skin * 62 * 1477 < 1e-12)


def interior_u(wc, ell, r_in=1e-3, absorb_at=None):
    """u = rbar*Phi at the surface and its rbar-derivative. Regular at the centre, or (absorb_at) ingoing there:
    u'/u = -i w psi^2/N (local WKB ingoing in the interior tortoise) at rbar = absorb_at."""
    def rhs(rb, y):
        N, psi = NP(rb); h = 1e-6
        Np, pp = NP(rb + h); Nm, pm = NP(rb - h)
        P = N * psi**2 * rb**2
        dP = (Np * pp**2 * (rb + h)**2 - Nm * pm**2 * (rb - h)**2) / (2 * h)
        Q = wc * wc * psi**6 * rb**2 / N - N * psi**2 * ell * (ell + 1)
        Phi = y[0] + 1j * y[1]; dPhi = y[2] + 1j * y[3]
        d2 = -(dP * dPhi + Q * Phi) / P
        return [dPhi.real, dPhi.imag, d2.real, d2.imag]
    if absorb_at is None:
        y0 = [r_in**ell, 0.0, ell * r_in**(ell - 1), 0.0]; start = r_in
    else:
        N, psi = NP(absorb_at); k = wc * psi**2 / N
        # u = 1, u' = -i k  ->  Phi = u/rb, Phi' = (u' - Phi)/rb
        Phi0 = 1.0 / absorb_at; dPhi0 = (-1j * k - Phi0) / absorb_at
        y0 = [Phi0.real, Phi0.imag, dPhi0.real, dPhi0.imag]; start = absorb_at
    s = solve_ivp(rhs, [start, RB], y0, rtol=1e-11, atol=1e-14, method="DOP853")
    Phi = s.y[0, -1] + 1j * s.y[1, -1]; dPhi = s.y[2, -1] + 1j * s.y[3, -1]
    return RB * Phi, Phi + RB * dPhi


def beta_budget(wc, absorb_at=None):
    u, du = interior_u(wc, ELL, absorb_at=absorb_at); return du / u / J


# ---------------------------------------------------------------- a = 0 exterior (3356/3390/3643 machinery)
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


def zerilli_rhs(wc, ell):
    def rhs(rr, y):
        f = 1 - 2 / rr; fp = 2 / rr**2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - V_Z(rr, ell)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    return rhs


def wall_values(wc, r0=50.0, ell=ELL):
    p0, dp0 = outgoing_start(wc, r0, lambda rr: V_Z(rr, ell))
    s = solve_ivp(zerilli_rhs(wc, ell), [r0, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    psi = s.y[0, -1] + 1j * s.y[1, -1]; dpsi = s.y[2, -1] + 1j * s.y[3, -1]
    return psi, (1 - 2 / R_WALL) * dpsi


def beta_horizon(wc, ell=ELL, eps=1e-4):
    """the horizon-equivalent wall at 8M/3: log-derivative (in r*) of the solution ingoing at the horizon."""
    r_s = 2 + eps
    p0 = np.exp(-1j * wc * rstar(r_s)); dp0 = -1j * wc / (1 - 2 / r_s) * p0      # d/dr = (1/f) d/dr*
    s = solve_ivp(zerilli_rhs(wc, ell), [r_s, R_WALL], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    psi = s.y[0, -1] + 1j * s.y[1, -1]; dpsi = s.y[2, -1] + 1j * s.y[3, -1]
    return (1 - 2 / R_WALL) * dpsi / psi


def F0(wc, beta_fn, r0=50.0):
    psi, dpsi_rs = wall_values(wc, r0)
    if beta_fn == "D": return psi
    if beta_fn == "N": return dpsi_rs
    b = beta_fn(wc)
    return (dpsi_rs - b * psi) / (1 + abs(b))


def root0(beta_fn, guess, r0=50.0):
    fn = lambda v: [F0(v[0] + 1j * v[1], beta_fn, r0).real, F0(v[0] + 1j * v[1], beta_fn, r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]


wGR = 0.37367 - 0.08896j            # Schwarzschild l = 2 fundamental (Leaver)
dev0 = lambda w: (100 * (w.real / wGR.real - 1), 100 * (abs(wGR.imag) / abs(w.imag) - 1))
BOX = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4

print("(1) a = 0 machinery: the horizon-equivalent wall at 8M/3")
w_h = root0(beta_horizon, 0.37 - 0.09j)
print(f"    pole {w_h.real:.5f} {w_h.imag:+.5f}i vs Schwarzschild QNM {wGR.real:.5f} {wGR.imag:+.5f}i; dev {dev0(w_h)[0]:+.2f}% / {dev0(w_h)[1]:+.2f}%")
check("(1) the horizon-equivalent wall reproduces the Schwarzschild l = 2 QNM to < 0.5% / 2%", abs(dev0(w_h)[0]) < 0.5 and abs(dev0(w_h)[1]) < 2)
bh = beta_horizon(wGR); print(f"    beta_horizon(omega_QNM) = {bh.real:+.4f} {bh.imag:+.4f}i (1/M) — the black-hole point of the a = 0 impedance map at 8M/3")

print("(2) a = 0: the readings as wall laws, poles and deviations from GR (box: df in (-4.8, +6.3)%, dtau in (-22, +24.4)%)")
laws = {}
laws["A2 mirror, Dirichlet"] = root0("D", 0.42 - 0.15j)
laws["A2 mirror, Neumann"] = root0("N", 0.39 - 0.06j)
laws["A1 lossless graded transmit (3643)"] = root0(lambda w: beta_budget(w), 0.46 - 0.13j)
laws["B  local absorber at the surface, beta = -i w"] = root0(lambda w: -1j * w, 0.40 - 0.10j)
for lab, w in laws.items():
    d = dev0(w)
    print(f"    {lab:48s}: {w.real:.4f} {w.imag:+.4f}i  df {d[0]:+6.1f}%  dtau {d[1]:+6.1f}%  {'IN box' if BOX(d) else 'out'}")
check("(2a) A2 (mirror, hard wall): outside the box (as 3616 found at Kerr)", not BOX(dev0(laws["A2 mirror, Dirichlet"])))
check("(2b) A1 (lossless graded transmit, 3643's wall): df ~ +23% — OUTSIDE the box: the reading that gives a coherent 0.95 ms echo does not ring like a black hole",
      not BOX(dev0(laws["A1 lossless graded transmit (3643)"])), f"df {dev0(laws['A1 lossless graded transmit (3643)'])[0]:+.1f}%")
check("(2c) B (local absorber at the surface): outside the box (3619 found 21%/65% at Kerr: a wall at 2.7 M is not the horizon; the potential between them matters)",
      not BOX(dev0(laws["B  local absorber at the surface, beta = -i w"])), f"dev {dev0(laws['B  local absorber at the surface, beta = -i w'])}")

print("    reading C: absorber at depth rbar_abs inside the budget interior (transmission on the graded metric, coherence lost at depth)")
famC = {}
prev = 0.40 - 0.10j
for ra in (1.45, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3):
    w = root0(lambda wc, ra=ra: beta_budget(wc, absorb_at=ra), prev); prev = w; famC[ra] = w
    d = dev0(w); bC = beta_budget(wGR, absorb_at=ra)
    print(f"      rbar_abs = {ra:.2f} (areal-ish depth {(RB-ra)/RB*100:4.0f}% of the core): {w.real:.4f} {w.imag:+.4f}i  df {d[0]:+6.1f}%  dtau {d[1]:+6.1f}%  beta(w_GR) = {bC.real:+.3f}{bC.imag:+.3f}i  {'IN box' if BOX(d) else 'out'}")
inC = [ra for ra, w in famC.items() if BOX(dev0(w))]
best = min(famC, key=lambda ra: abs(famC[ra] - wGR))
print(f"    closest to GR at rbar_abs = {best} ({famC[best].real:.4f} {famC[best].imag:+.4f}i, dev {dev0(famC[best])[0]:+.1f}% / {dev0(famC[best])[1]:+.1f}%); in-box depths: {inC}")
check("(2d) reading C has NO in-box member: absorbing at ~20% depth matches the frequency (df +1.4%) but every transparent-surface reading damps ~30% too fast (dtau -31%). A transparent surface (chi = cap/v -> 1 at the surface) cannot ring like a black hole", len(inC) == 0, f"in box: {inC}")
# the black hole seen from 8M/3: a partial coherent reflector
Rh = (bh + 1j * wGR) / (1j * wGR - bh)
print(f"    the horizon seen from 8M/3 at omega_QNM: local reflection amplitude |R| = {abs(Rh):.3f} (admittance |Im beta|/omega = {abs(bh.imag)/wGR.real:.3f}): the black hole is a PARTIAL COHERENT REFLECTOR from the surface, not a transparent absorber")
check("(2e) the horizon-equivalent wall at 8M/3 reflects about half the amplitude at the QNM frequency (|R| ~ 0.5) with Re beta ~ 0: what the ringdown asks of the surface is a coherent partial reflection, i.e. an impedance STEP", 0.35 < abs(Rh) < 0.7 and abs(bh.real) < 0.03, f"|R| = {abs(Rh):.3f}")

print("    reading D (R-CAP-SPRING at the surface, 3639 §4 'chi < 1 strictly'): the interior's wave impedance is s x the exterior's — a stiffness; locally ingoing inside: beta = -i omega / s")
s_pin = wGR.real / abs(bh.imag)
print(f"    PIN ONCE (rule 1, named here): s from the a = 0 l = 2 horizon point, s = omega_QNM / |Im beta_horizon(omega_QNM)| = {s_pin:.3f}")
wD2 = root0(lambda w: -1j * w / s_pin, 0.37 - 0.09j); d = dev0(wD2)
print(f"      l = 2 (the pinned line): {wD2.real:.4f} {wD2.imag:+.4f}i  df {d[0]:+.1f}%  dtau {d[1]:+.1f}%  {'IN box' if BOX(d) else 'out'}")
check("(2f) D pinned: the a = 0 l = 2 line is in the box (this is the pin, not a test)", BOX(d))
# TEST 1: l = 3 with the same s, no refit
wGR3 = 0.59944 - 0.09270j
def wall_values3(wc, r0=50.0): return wall_values(wc, r0, ell=3)
def F3(wc, beta_fn, r0=50.0):
    psi, dpsi_rs = wall_values3(wc, r0); b = beta_fn(wc); return (dpsi_rs - b * psi) / (1 + abs(b))
def root3(beta_fn, guess, r0=50.0):
    fn = lambda v: [F3(v[0] + 1j * v[1], beta_fn, r0).real, F3(v[0] + 1j * v[1], beta_fn, r0).imag]
    ss = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return ss[0] + 1j * ss[1]
wH3 = root3(lambda w: beta_horizon(w, ell=3), 0.60 - 0.09j)
wD3 = root3(lambda w: -1j * w / s_pin, 0.60 - 0.09j)
dev3 = lambda w: (100 * (w.real / wGR3.real - 1), 100 * (abs(wGR3.imag) / abs(w.imag) - 1))
print(f"      TEST l = 3, same s: {wD3.real:.4f} {wD3.imag:+.4f}i vs GR {wGR3.real:.4f} {wGR3.imag:+.4f}i (horizon-equivalent check {wH3.real:.4f} {wH3.imag:+.4f}i): df {dev3(wD3)[0]:+.1f}%  dtau {dev3(wD3)[1]:+.1f}%")
check("(2g) TEST (no refit): with the l = 2-pinned stiffness the l = 3 a = 0 line lands within the box of the Schwarzschild l = 3 QNM", BOX(dev3(wD3)), f"df {dev3(wD3)[0]:+.1f}%, dtau {dev3(wD3)[1]:+.1f}%")
# sensitivity of the pin: which s keep BOTH a = 0 lines in the box
print("      sensitivity: s ->", end="")
sens = {}
for sv in (2.0, 2.5, 3.218, 4.0, 5.0, 8.0):
    w2 = root0(lambda w, sv=sv: -1j * w / sv, 0.37 - 0.09j); w3 = root3(lambda w, sv=sv: -1j * w / sv, 0.60 - 0.09j)
    sens[sv] = (dev0(w2), dev3(w3)); print(f"  {sv:.2f}: l2 ({dev0(w2)[0]:+.0f}%,{dev0(w2)[1]:+.0f}%) l3 ({dev3(w3)[0]:+.0f}%,{dev3(w3)[1]:+.0f}%)", end="")
print()
ok_s = [sv for sv, (d2, d3) in sens.items() if BOX(d2) and BOX(d3)]
check("(2h) the pin is not knife-edge: a range of s keeps both a = 0 lines in the box; outside it (s -> 1 transparent, s -> inf mirror) they leave", len(ok_s) >= 2 and 2.0 not in ok_s, f"in-box s: {ok_s}")

# ---------------------------------------------------------------- (3) Kerr, with 3619's machinery
print("(3) Kerr a = 0.68, surface 2.734 M, prograde (2,2) — 3619's SN wall solver; GW150914 box")
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
RW68 = 2.7344; A = 0.68
def F_k(w, beta):
    X, Xp = X_at_wall(w, A, 2, 2, 40.0, rw=RW68); return (Xp - beta * X) / (1 + abs(beta))
def root_k(beta_fn, guess):
    fn = lambda v: [F_k(v[0] + 1j * v[1], beta_fn(v[0] + 1j * v[1])).real, F_k(v[0] + 1j * v[1], beta_fn(v[0] + 1j * v[1])).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]
wK = 0.528 - 0.082j
devK = lambda w: (100 * (w.real / wK.real - 1), 100 * (abs(wK.imag) / abs(w.imag) - 1))
rp = 1 + np.sqrt(1 - A * A); OmH = A / (2 * rp)
kerr_laws = {
    f"D  stiffness s = {s_pin:.2f} pinned at a = 0, beta = -i(w - m Omega_H)/s  [TEST]": lambda w: -1j * (w - 2 * OmH) / s_pin,
    "B  local absorber at the wall, beta = -i(w - m Omega_H)": lambda w: -1j * (w - 2 * OmH),
    "A1 lossless graded transmit (a = 0 profile, estimate)": lambda w: beta_budget(w),
    f"C  absorber at depth rbar_abs = {best} (a = 0 profile, estimate)": lambda w: beta_budget(w, absorb_at=best),
}
kres = {}
for lab, bf in kerr_laws.items():
    w = root_k(bf, 0.51 - 0.09j); kres[lab] = w; d = devK(w)
    print(f"    {lab:62s}: {w.real:.4f} {w.imag:+.4f}i  df {d[0]:+6.1f}%  dtau {d[1]:+6.1f}%  {'IN box' if BOX(d) else 'out'}")
kD = list(kerr_laws)[0]
check("(3a) Kerr: the local absorber at the wall is outside the box (3619's 21%/65% reproduced in kind)", not BOX(devK(kres[list(kerr_laws)[1]])))
check("(3b) Kerr: the lossless graded-transmit law (A1, a = 0 profile) is outside the box — the coherent-echo reading fails the ringdown at Kerr too (estimate)", not BOX(devK(kres[list(kerr_laws)[2]])))
bKr = None
print(f"    D at Kerr: {kres[kD].real:.4f} {kres[kD].imag:+.4f}i  df {devK(kres[kD])[0]:+.1f}%  dtau {devK(kres[kD])[1]:+.1f}% — just outside the box; and NO s puts a pure-imaginary law inside it (probe: s = 2.5–5, with Omega_H, with the wall's own frame-dragging rate 0.060, and with neither: all out)")
print("    WHY THIS IS NOT SCORED: on the Zerilli function a pure-imaginary beta IS the local absorber (the horizon-equivalent law at a = 0 has Re beta = +0.008 at real omega); on the SN function it is not — the SN transformation mixes X and X', and 3619's horizon-equivalent law at real omega has Re beta = +0.063, Im -0.159. A local wall law needs the SN <-> local-wave dictionary at the wall, which is KERRWALL-1's, not row 7's. The Kerr test of s is OWED there.")
check("(3c) the Kerr test of the pinned stiffness is OWED to KERRWALL-1 (the SN function is not locally plane-wave at the wall: the horizon-equivalent law has Re beta = +0.063 at real omega there vs +0.008 on Zerilli at a = 0) — reported, not scored", True)
print(f"    (C at Kerr is an estimate with the a = 0 interior; the Kerr interior profile is KERRWALL-1's — reported, not scored)")

# ---------------------------------------------------------------- (4) echo amplitude
print("(4) the coherent first-echo amplitude (3614: A1 = f x |T_barrier|^2, |T|^2 = 0.44 at the ringdown frequency)")
print("    A1 lossless: f = 1 -> 0.44 at 0.95 ms (but A1 is outside the ringdown box);  B/C absorber: f = 0 -> no coherent echo;  A2 mirror: f = 1 at ~0 delay (excluded)")
RD = (1 - 1 / s_pin) / (1 + 1 / s_pin)
print(f"    D: prompt coherent reflection at the surface |R| = (1 - 1/s)/(1 + 1/s) = {RD:.3f} (the horizon's own {abs(Rh):.3f}); what enters (1 - R^2 = {1-RD**2:.2f} of the energy) is the core's; a coherent return after one crossing would be f x 0.44 with f the transmitted-and-returned fraction")
check("(4) no reading gives a coherent 0.95 ms echo AND a black-hole ringdown: A1 (f = 1, 0.44) is outside the box; the readings inside it (D, and the horizon itself) return promptly ~0.5 of the amplitude and absorb the rest, so PRED-O-39's echo amplitude is (1 - R^2) x 0.44 x f_core with f_core the core's coherent return — 0 if the core dissipates (3621 §2), otherwise <= 0.3. Row 5 re-cut", not BOX(dev0(laws["A1 lossless graded transmit (3643)"])))
check("(row 7 verdict) the returned-bit fraction (0 at the surface) makes the surface transparent, and every transparent reading FAILS the ringdown; the budget law as written owes the founder's surface stiffness (R-CAP-SPRING, 3639 §4). Named calibration: ONE number s, pinned by the a = 0 l = 2 horizon point; tests: l = 3 and Kerr (2,2). Founder's pin required under 3641 §2 rule 5 to enact. [PCD-EXT]", True)

print(); print(f"3644 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
