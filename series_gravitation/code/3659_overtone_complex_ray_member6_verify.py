#!/usr/bin/env python3
"""
Patch 3659 verify — the ℓ = 2 first overtone as H-SURFACE-IMPEDANCE member 6 (a = 0, Zerilli, 8M/3), with a
COMPLEX-RAY solver that replaces the stalled direct integration (3646: stalls at Im ω ≈ −0.27; handover item 3
asked for a Leaver-type instrument — the ray is the cheaper one and is validated below on the known overtone).
Run from the repo root. Also re-cuts the ringdown box to GW250114 (handover item 2, searched first per BLOCKING 3).

THE INSTRUMENT. Along real r*, integrating inward from r0 the outgoing solution e^{iωr*} shrinks and the ingoing
contaminant grows, by e^{2|Im ω| Δr*} ≈ e^{24} for the overtone. Along the ray r* = r*_w + t e^{iθ} the outgoing
solution's modulus is e^{-t(ω_R sinθ + ω_I cosθ)}: for θ > arctan(|ω_I|/ω_R) (≈ 38° at the overtone) it GROWS
toward the wall and the contaminant decays, so inward integration is stable. The horizon side is the same ray
reflected: r* = r*_w − t e^{iθ}, Re r* → −∞ so ψ → e^{-iωr*} is the horizon condition; the ingoing solution grows
toward the wall for the same θ. The ODE is integrated in t with complex r carried as a state (dr/dr* = 1 − 2/r);
the Zerilli potential is analytic and the path avoids r = 0, 2. θ = 60° here. r is recovered at the ray's far end
by complex Newton on r + 2 ln(r/2 − 1) = r*.

VALIDATION (before any hypothesis number): (V1) the fundamental via the horizon-equivalent law and via the
hypothesis reproduce 3644's real-axis poles (0.3737 − 0.0890 i; 0.3656 − 0.0848 i); (V2) the overtone via the
horizon-equivalent law reproduces Leaver's 0.34671 − 0.27391 i; (V3) θ-independence (50° vs 70°) and far-end
independence at the overtone.

THEN: the hypothesis β = −iω/s, s = 3.218 UNCHANGED, at the overtone; scored against GR (Leaver) and the
GW250114 overtone box (δf ∈ [e^{-0.2} − 1, e^{0.4} − 1] = [−18%, +49%] at 90% around Kerr; damping
unconstrained — PRL 135, 111403 (2025): δf₂₂₁ = 0.1 ± 0.3, δγ₂₂₁ uninformative). The fundamental box re-cut:
f₂₂₀ = 247 ± 6 Hz (±2.4%), γ₂₂₀ = 221 +39/−32 Hz → δτ ∈ (−15%, +17%), at χ_f = 0.68 ± 0.01, M_f = 62.7 M☉.
The a = 0 members are re-scored against the re-cut box for the record (the box is Kerr's; the members are a = 0).
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

R_WALL = 8.0 / 3.0; S_PIN = 3.218
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
RSW = rstar(R_WALL)
def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)

def r_of_rstar(rs, guess):
    r = complex(guess)
    for _ in range(80):
        f = r + 2 * np.log(r / 2 - 1) - rs; df = 1 + 2 / (r - 2)
        r = r - f / df
    return r

def outgoing_series(wc, ell, r_pts, nterms=10):
    """ψ = e^{iωr*} Σ c_k r^-k fitted by least squares on the Zerilli equation at the (complex) points r_pts."""
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    def pd(cc, rr):
        f = 1 - 2 / rr
        S = sum(cc[k] / rr**k for k in range(len(cc))); dS = sum(-k * cc[k] / rr**(k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / rr**(k + 2) for k in range(len(cc)))
        e = np.exp(1j * wc * rstar(rr))
        return (e * S, e * (1j * wc / f * S + dS), e * ((1j * wc / f) ** 2 * S + 2 * (1j * wc / f) * dS + d2S - 1j * wc * (2 / rr**2) / f**2 * S))
    def resid(cc):
        out = []
        for rr in r_pts:
            f = 1 - 2 / rr; fp = 2 / rr**2; p, dp, d2p = pd(cc, rr)
            out.append((f * f * d2p + f * fp * dp + (wc * wc - V_Z(rr, ell)) * p) / np.exp(1j * wc * rstar(rr)))
        return np.array(out)
    A = np.zeros((len(r_pts), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; A[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(A, -base, rcond=None)[0]
    return lambda rr: pd(c, rr)

def ray_rhs(wc, ell, e):
    """state y = [Re ψ, Im ψ, Re ψ', Im ψ', Re r, Im r]; ' = d/dr*; dr*/dt = e."""
    def rhs(t, y):
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]; r = y[4] + 1j * y[5]
        d2 = (V_Z(r, ell) - wc * wc) * psi
        dr = (1 - 2 / r)
        return [(dpsi * e).real, (dpsi * e).imag, (d2 * e).real, (d2 * e).imag, (dr * e).real, (dr * e).imag]
    return rhs

def wall_values_ray(wc, ell, theta=np.pi / 3, T=60.0):
    """outgoing-at-infinity solution and its r*-derivative at the wall, via the complex ray r* = r*_w + t e^{iθ}."""
    e = np.exp(1j * theta)
    rs_end = RSW + T * e; r_end = r_of_rstar(rs_end, rs_end)
    pts = [r_of_rstar(RSW + tt * e, RSW + tt * e) for tt in np.linspace(T, 4 * T, 30)]
    ser = outgoing_series(wc, ell, pts)
    p0, dp0_dr, _ = ser(r_end); dp0 = dp0_dr * (1 - 2 / r_end)          # d/dr* = f d/dr
    sol = solve_ivp(ray_rhs(wc, ell, e), [T, 0.0], [p0.real, p0.imag, dp0.real, dp0.imag, r_end.real, r_end.imag],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    psi = sol.y[0, -1] + 1j * sol.y[1, -1]; dpsi = sol.y[2, -1] + 1j * sol.y[3, -1]
    r_back = sol.y[4, -1] + 1j * sol.y[5, -1]
    return psi, dpsi, abs(r_back - R_WALL)

def beta_horizon_ray(wc, ell, theta=np.pi / 3, T=40.0):
    """horizon-equivalent law at the wall: log-derivative (r*) of the solution ingoing at the horizon, via the reflected ray."""
    e = -np.exp(1j * theta)
    rs_end = RSW + T * e
    # r near 2: r - 2 = 2 exp((r* - r)/2); iterate
    r_end = 2 + 2 * np.exp((rs_end - 2) / 2)
    for _ in range(60): r_end = 2 + 2 * np.exp((rs_end - r_end) / 2)
    p0 = np.exp(-1j * wc * rs_end); dp0 = -1j * wc * p0
    sol = solve_ivp(ray_rhs(wc, ell, e), [T, 0.0], [p0.real, p0.imag, dp0.real, dp0.imag, r_end.real, r_end.imag],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    psi = sol.y[0, -1] + 1j * sol.y[1, -1]; dpsi = sol.y[2, -1] + 1j * sol.y[3, -1]
    return dpsi / psi

def root_ray(beta_fn, ell, guess, **kw):
    def F(wc):
        psi, dpsi, _ = wall_values_ray(wc, ell, **kw); b = beta_fn(wc); return (dpsi - b * psi) / (1 + abs(b))
    fn = lambda v: [F(v[0] + 1j * v[1]).real, F(v[0] + 1j * v[1]).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]

Msec = 62.7 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
wGR0 = 0.37367 - 0.08896j; wGR1 = 0.34671 - 0.27391j
dev = lambda w, ref: (100 * (w.real / ref.real - 1), 100 * (abs(ref.imag) / abs(w.imag) - 1))
BOX150914 = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4
BOX250114_F = lambda d: -2.4 < d[0] < 2.4 and -15 < d[1] < 17                  # fundamental, re-cut
BOX250114_OT = lambda d: (np.exp(-0.2) - 1) * 100 < d[0] < (np.exp(0.4) - 1) * 100   # overtone: frequency only

print("(V) validation of the complex-ray instrument")
_, _, rerr = wall_values_ray(wGR0, 2)
check("(V0) the ray returns to the wall: |r(t=0) − 8M/3| < 1e-8 (the complex r state closes on the real wall)", rerr < 1e-8, f"{rerr:.1e}")
w_h0 = root_ray(lambda w: beta_horizon_ray(w, 2), 2, 0.37 - 0.09j)
w_D0 = root_ray(lambda w: -1j * w / S_PIN, 2, 0.37 - 0.09j)
print(f"    fundamental: horizon-equivalent {w_h0.real:.5f} {w_h0.imag:+.5f}i (Leaver {wGR0.real:.5f} {wGR0.imag:+.5f}i); hypothesis {w_D0.real:.4f} {w_D0.imag:+.4f}i (3644 real-axis: 0.3656 −0.0848i)")
check("(V1) on the fundamental the ray instrument reproduces both the real-axis machinery (3644) and Leaver: horizon law to < 0.3%/1%, hypothesis pole to < 0.1%", abs(dev(w_h0, wGR0)[0]) < 0.3 and abs(dev(w_h0, wGR0)[1]) < 1 and abs(w_D0 - (0.3656 - 0.0848j)) < 5e-4, f"|Δ hyp| = {abs(w_D0 - (0.3656 - 0.0848j)):.1e}")
w_h1 = root_ray(lambda w: beta_horizon_ray(w, 2), 2, 0.35 - 0.27j)
print(f"    overtone: horizon-equivalent {w_h1.real:.5f} {w_h1.imag:+.5f}i vs Leaver {wGR1.real:.5f} {wGR1.imag:+.5f}i; dev {dev(w_h1, wGR1)[0]:+.2f}% / {dev(w_h1, wGR1)[1]:+.2f}%")
check("(V2) THE DECISIVE TEST: the overtone via the horizon-equivalent wall reproduces Leaver's Schwarzschild n = 1 mode to < 0.5% / 2% — the instrument reaches Im ω ≈ −0.27 where direct integration stalled (3646)", abs(dev(w_h1, wGR1)[0]) < 0.5 and abs(dev(w_h1, wGR1)[1]) < 2)
w_h1b = root_ray(lambda w: beta_horizon_ray(w, 2, theta=np.radians(50), T=45.0), 2, w_h1, theta=np.radians(50), T=70.0)
w_h1c = root_ray(lambda w: beta_horizon_ray(w, 2, theta=np.radians(70), T=40.0), 2, w_h1, theta=np.radians(70), T=50.0)
check("(V3) θ- and far-end-independence at the overtone (50°/70°, T = 50/70): spread < 1e-4", max(abs(w_h1b - w_h1), abs(w_h1c - w_h1)) < 1e-4, f"spread {max(abs(w_h1b - w_h1), abs(w_h1c - w_h1)):.1e}")

print("(1) the horizon seen from 8M/3 at the overtone")
bh1 = beta_horizon_ray(wGR1, 2); bh0 = beta_horizon_ray(wGR0, 2)
print(f"    β_hor(ω_221) = {bh1.real:+.4f} {bh1.imag:+.4f}i  (fundamental: {bh0.real:+.4f} {bh0.imag:+.4f}i);  re-read pin s = |ω|/|Im β| → {abs(wGR1)/abs(bh1.imag):.2f} at the overtone vs {abs(wGR0)/abs(bh0.imag):.2f} at the fundamental")

print(f"(2) MEMBER 6 — the ℓ = 2 first overtone, β = −iω/s, s = {S_PIN} unchanged")
w_D1 = root_ray(lambda w: -1j * w / S_PIN, 2, 0.35 - 0.27j)
d1 = dev(w_D1, wGR1)
print(f"    hypothesis {w_D1.real:.4f} {w_D1.imag:+.4f}i vs GR {wGR1.real:.4f} {wGR1.imag:+.4f}i: δf {d1[0]:+.1f}%  δτ {d1[1]:+.1f}%  ({to_hz(w_D1.real):.0f} Hz, γ = {abs(w_D1.imag)/Msec:.0f} Hz @62.7 M☉)")
print(f"    GW250114 overtone box (frequency only, 90%): δf ∈ ({(np.exp(-0.2)-1)*100:+.0f}%, {(np.exp(0.4)-1)*100:+.0f}%) → {'IN' if BOX250114_OT(d1) else 'out'};  GW150914 fundamental-shaped box → {'IN' if BOX150914(d1) else 'out'}")
check("(2) recorded as computed: the overtone member with s unchanged — descriptive (inside the GW250114 overtone frequency box) or not", True, f"δf {d1[0]:+.1f}%, δτ {d1[1]:+.1f}% → {'DESCRIPTIVE (frequency box; damping unconstrained by data)' if BOX250114_OT(d1) else 'FAILS'}")
check("(2b) the overtone's damping residual, for the record against GR (no data box exists for it yet): reported", True, f"δτ {d1[1]:+.1f}% vs GR")
# sensitivity: which s keep the overtone in the frequency box
sens = {}
for sv in (2.0, 2.5, 3.218, 5.0, 8.0):
    w = root_ray(lambda w, sv=sv: -1j * w / sv, 2, w_D1); sens[sv] = dev(w, wGR1)
print("    s-sensitivity at the overtone: " + "  ".join(f"s={sv:g} ({d[0]:+.0f}%,{d[1]:+.0f}%)" for sv, d in sens.items()))

print("(3) the ringdown box re-cut to GW250114 (PRL 135, 111403: f₂₂₀ = 247 ± 6 Hz, γ₂₂₀ = 221 +39/−32 Hz at 10.5 t_M; χ_f = 0.68 ± 0.01)")
print(f"    fundamental box: δf ∈ (−2.4, +2.4)%, δτ ∈ (−15, +17)%  [GW150914 was (−4.8, +6.3)% / (−22, +24.4)%]")
members = {"ℓ=2 (pin, 3644)": (-2.2, 4.9), "ℓ=3 (3644)": (-1.4, -1.3), "ℓ=4 (3646)": (-1.0, -5.1), "ℓ=2 odd RW (3657)": (-0.8, 12.0), "ℓ=3 odd RW (3657)": (-1.2, 0.5)}
for lab, d in members.items():
    print(f"      a = 0 member {lab:22s}: δf {d[0]:+.1f}% δτ {d[1]:+.1f}% → GW150914 {'IN' if BOX150914(d) else 'out'}; GW250114-shaped {'IN' if BOX250114_F(d) else 'out'}")
check("(3) the a = 0 fundamentals all sit inside a GW250114-shaped box too (the box is Kerr's; recorded for scale, not as a Kerr test — the Kerr member itself fails, 3657)", all(BOX250114_F(d) for d in members.values()))

print(); print(f"3659 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
