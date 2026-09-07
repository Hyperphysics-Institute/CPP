#!/usr/bin/env python3
"""
Patch 3672 verify — THE COMPLEX RAY AT KERR (METH-L1-015 carried onto the CD Z+ instrument of 3668): the prograde
(2,+1) comparator, NOT LOCATED since 3359 §4 (direct integration cannot reach Q ~ 1), located. Run from the repo
root (exec's 3668's instrument, which exec's 3359/3358).

THE INSTRUMENT (3659, now at Kerr). Along the ray r* = r*_w + t e^{iθ} the outgoing solution grows toward the wall
for θ > arctan|ω_I/ω_R|, so inward integration is stable at any Im ω; the horizon side is the reflected ray
r* = r*_w − t e^{iθ}, on which the ingoing solution e^{−ikr*} grows toward the wall. r is carried as a complex
state, dr/dr* = Δ/(r²+a²); the CD potential is closed-form and analytic in r (3668), which is why Z+ rather than
SN (whose U needs a numerical derivative) carries the ray. λ = A_{-2,lm}(aω) + a²ω² − 2amω at complex ω (Leaver's
angular CF handles complex c). Far end: the outgoing series e^{iωr*} Σ c_k r^{-k} fitted on the ray.

VALIDATION BEFORE ANY WALL NUMBER (3359 §1 discipline):
 (V0) the ray closes on the real wall (|r(t=0) − r_w| < 1e-8) on both sides.
 (V1) (2,2) fundamental at χ = 0.68 via the horizon-equivalent law = Leaver's radial CF (3358) to < 1e-4.
 (V2) THE DECISIVE TEST: (2,2) FIRST OVERTONE at χ = 0.68 via the horizon law = Leaver's n = 1 root to < 1e-3
      — Im ω ≈ −0.25, where direct integration stalls.
 (V3) (2,+1) and (2,−2) fundamentals = Leaver.  (V4) θ / far-end independence at the overtone.
THEN
 (1) The wall family on Z+ at r_w(0.68) = 2.7344 M for (2,m), m = +2, +1, 0, −2: Dirichlet (Z+ = 0, the
     even-variable node) and Neumann (dZ+/dr* = 0); each root passed θ/T-independence. Q = Re ω/(2|Im ω|).
     These are MODEL walls (the two ends of the compliance family, 3390/3391), not derived laws; the point is the
     INSTRUMENT and the ORDERING.
 (2) THE ORDERING TEST (PRED-O-39 (e), at eikonal grade since 3359): under the same wall, is the prograde (2,+1)
     line broader (lower Q) than the retrograde (2,−2)? Recorded as computed, both walls.
"""
import io, contextlib, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src68 = open("series_gravitation/code/3668_kerrwall1b_cd_zplus_even_kerr_verify.py").read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src68.split("# ============================================================ T1")[0].replace("PASS = FAIL = 0", "PASS68 = FAIL68 = 0").replace('def check(name, cond, detail="")', 'def check68(name, cond, detail="")'))
SB = -1; A68 = 0.68; RW = 2.7344; RP = 1 + np.sqrt(1 - A68 * A68); RM = 1 - np.sqrt(1 - A68 * A68); OMH = A68 / (2 * RP)
RSW = rstar(RW, A68)
Msec = 62.7 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec); Q_of = lambda w: w.real / (2 * abs(w.imag))

def r_of_rstar(rs, guess):
    r = complex(guess)
    for _ in range(100):
        f = rstar(r, A68) - rs; df = (r * r + A68 * A68) / (r * r - 2 * r + A68 * A68)
        r = r - f / df
    return r

def series_far(w, m, r_pts, lam, nterms=10):
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    def pd(cc, r):
        D = r * r - 2 * r + A68 * A68; drs = (r * r + A68 * A68) / D
        S = sum(cc[k] / r ** k for k in range(len(cc))); dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r, A68))
        X = e * S; dX_dr = e * (1j * w * drs * S + dS); Xp = dX_dr / drs
        ddrs = (2 * r * D - (r * r + A68 * A68) * (2 * r - 2)) / D ** 2
        d2X_dr2 = e * ((1j * w * drs) ** 2 * S + 1j * w * ddrs * S + 2 * 1j * w * drs * dS + d2S)
        Xpp = (d2X_dr2 - Xp * ddrs) / drs ** 2
        return X, Xp, Xpp
    def resid(cc):
        return np.array([(pd(cc, r)[2] - calV_CD(r, A68, w, m, lam, +1, SB) * pd(cc, r)[0]) / np.exp(1j * w * rstar(r, A68)) for r in r_pts])
    Mx = np.zeros((len(r_pts), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; Mx[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(Mx, -base, rcond=None)[0]
    return lambda r: pd(c, r)

def ray_rhs(w, m, lam, e):
    def rhs(t, y):
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]; r = y[4] + 1j * y[5]
        Xpp = calV_CD(r, A68, w, m, lam, +1, SB) * X; dr = (r * r - 2 * r + A68 * A68) / (r * r + A68 * A68)
        return [(Xp * e).real, (Xp * e).imag, (Xpp * e).real, (Xpp * e).imag, (dr * e).real, (dr * e).imag]
    return rhs

def wall_out(w, m, theta=np.pi / 3, T=60.0):
    """outgoing-at-infinity Z+ and its r*-derivative at the wall via the ray; also |r(0) − r_w|."""
    lam = lam_of(w, A68, 2, m); e = np.exp(1j * theta)
    rs_end = RSW + T * e; r_end = r_of_rstar(rs_end, rs_end)
    pts = [r_of_rstar(RSW + tt * e, RSW + tt * e) for tt in np.linspace(T, 4 * T, 30)]
    X0, Xp0, _ = series_far(w, m, pts, lam)(r_end)
    sol = solve_ivp(ray_rhs(w, m, lam, e), [T, 0.0], [X0.real, X0.imag, Xp0.real, Xp0.imag, r_end.real, r_end.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1]), abs(sol.y[4, -1] + 1j * sol.y[5, -1] - RW)

def beta_hor_ray(w, m, theta=np.pi / 3, T=40.0):
    """horizon-equivalent law at the wall via the reflected ray (ingoing e^{-ikr*} at Re r* → −∞)."""
    lam = lam_of(w, A68, 2, m); e = -np.exp(1j * theta); k = w - m * OMH
    rs_end = RSW + T * e
    r_end = RP + 2 * np.exp((rs_end - RP) * (RP - RM) / (2 * RP))
    for _ in range(80):
        r_end = RP + 2 * np.exp((rs_end - r_end + (2 * RM / (RP - RM)) * np.log((r_end - RM) / 2)) * (RP - RM) / (2 * RP))
    X0 = np.exp(-1j * k * rs_end); Xp0 = -1j * k * X0
    sol = solve_ivp(ray_rhs(w, m, lam, e), [T, 0.0], [X0.real, X0.imag, Xp0.real, Xp0.imag, r_end.real, r_end.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[2, -1] + 1j * sol.y[3, -1]) / (sol.y[0, -1] + 1j * sol.y[1, -1]), abs(sol.y[4, -1] + 1j * sol.y[5, -1] - RW)

def root_ray(law, m, guess, **kw):
    """law: 'D' (Z+ = 0), 'N' (dZ+/dr* = 0), or callable beta(w)."""
    def F(w):
        X, Xp, _ = wall_out(w, m, **kw)
        if law == "D": return X
        if law == "N": return Xp
        b = law(w); return (Xp - b * X) / (1 + abs(b))
    fn = lambda v: [F(v[0] + 1j * v[1]).real, F(v[0] + 1j * v[1]).imag]
    s, info, ier, msg = fsolve(fn, [guess.real, guess.imag], xtol=1e-10, full_output=True)
    w = s[0] + 1j * s[1]; res = abs(F(w))
    return w, res

# ================================================================ validation
print("(V) validation of the ray instrument on the CD Z+ potential at chi = 0.68")
wK22 = kerr_qnm(A68, 2, 2, -2, 0.524 - 0.082j)
wK22n1 = kerr_qnm(A68, 2, 2, -2, 0.51 - 0.25j)
wK21 = kerr_qnm(A68, 2, 1, -2, 0.45 - 0.087j)
wK2m2 = kerr_qnm(A68, 2, -2, -2, 0.311 - 0.089j)
print(f"    Leaver: (2,+2) n=0 {wK22:.5f}; (2,+2) n=1 {wK22n1:.5f}; (2,+1) n=0 {wK21:.5f}; (2,-2) n=0 {wK2m2:.5f}")
check("(V-L) Leaver's n = 1 root is the first overtone (Im ≈ 3x the fundamental's, Re within 5%)", 2.5 < wK22n1.imag / wK22.imag < 3.6 and abs(wK22n1.real / wK22.real - 1) < 0.05)
_, _, e_out = wall_out(wK22, 2); _, e_hor = beta_hor_ray(wK22, 2)
check("(V0) the ray closes on the real wall on both sides (|r(0) − r_w| < 1e-8)", e_out < 1e-8 and e_hor < 1e-8, f"out {e_out:.1e}, hor {e_hor:.1e}")
w_h22, r22 = root_ray(lambda w: beta_hor_ray(w, 2)[0], 2, wK22)
check("(V1) (2,2) fundamental via the horizon-equivalent law on the ray = Leaver to < 1e-4 relative", abs(w_h22 - wK22) / abs(wK22) < 1e-4, f"{w_h22:.6f} vs {wK22:.6f}; dev {abs(w_h22-wK22)/abs(wK22):.1e}")
w_h22n1, _ = root_ray(lambda w: beta_hor_ray(w, 2)[0], 2, wK22n1)
check("(V2) THE DECISIVE TEST: the (2,2) FIRST OVERTONE at chi = 0.68 via the horizon law on the ray = Leaver's n = 1 root to < 1e-3 — the instrument reaches Im ω ≈ −0.25 at Kerr", abs(w_h22n1 - wK22n1) / abs(wK22n1) < 1e-3, f"{w_h22n1:.5f} vs {wK22n1:.5f}; dev {abs(w_h22n1-wK22n1)/abs(wK22n1):.1e}")
w_h21, _ = root_ray(lambda w: beta_hor_ray(w, 1)[0], 1, wK21); w_h2m2, _ = root_ray(lambda w: beta_hor_ray(w, -2)[0], -2, wK2m2)
check("(V3) (2,+1) and (2,−2) fundamentals via the horizon law = Leaver to < 1e-3", abs(w_h21 - wK21) / abs(wK21) < 1e-3 and abs(w_h2m2 - wK2m2) / abs(wK2m2) < 1e-3, f"(2,+1) dev {abs(w_h21-wK21)/abs(wK21):.1e}; (2,−2) dev {abs(w_h2m2-wK2m2)/abs(wK2m2):.1e}")
w_b, _ = root_ray(lambda w: beta_hor_ray(w, 2, theta=np.radians(50), T=45.0)[0], 2, w_h22n1, theta=np.radians(50), T=70.0)
w_c, _ = root_ray(lambda w: beta_hor_ray(w, 2, theta=np.radians(70), T=40.0)[0], 2, w_h22n1, theta=np.radians(70), T=50.0)
check("(V4) θ / far-end independence at the overtone (50°/70°, T = 50/70): spread < 1e-4", max(abs(w_b - w_h22n1), abs(w_c - w_h22n1)) < 1e-4, f"spread {max(abs(w_b - w_h22n1), abs(w_c - w_h22n1)):.1e}")

# ================================================================ (1) the wall family: Dirichlet and Neumann on Z+, (2,m)
print(f"(1) model walls on Z+ at r_w = {RW} M, chi = 0.68: Dirichlet (Z+ = 0) and Neumann (dZ+/dr* = 0); each root: θ/T-independence and residual")
modes = {+2: wK22, +1: wK21, 0: kerr_qnm(A68, 2, 0, -2, 0.393 - 0.085j), -2: wK2m2}
results = {}
for law in ("D", "N"):
    for m, wk in modes.items():
        best = None
        for g in (wk, wk.real + 0.02 - 0.20j, wk.real - 0.05 - 0.30j, wk.real + 0.10 - 0.12j):
            w, res = root_ray(law, m, g)
            if res < 1e-7 and w.imag < 0 and w.real > 0.05:
                w2, _ = root_ray(law, m, w, theta=np.radians(50), T=75.0)
                if abs(w2 - w) < 1e-5:
                    if best is None or abs(w.imag) < abs(best.imag): best = w
        results[(law, m)] = best
        if best is None: print(f"    {law} (2,{m:+d}): no converged root from the guess set")
        else: print(f"    {law} (2,{m:+d}): {best.real:.5f} {best.imag:+.5f}i   f = {to_hz(best.real):6.1f} Hz   Q = {Q_of(best):.2f}   (Kerr QNM: {wk.real:.4f}{wk.imag:+.4f}i, Q {Q_of(wk):.2f})")
located = results[("D", 1)] is not None and results[("N", 1)] is not None
check("(1) THE (2,+1) COMPARATOR IS LOCATED on both model walls (converged, θ/T-independent to 1e-5, residual < 1e-7) — the 3359 §4 method limit is discharged at Kerr", located,
      "; ".join(f"{law}: {results[(law,1)]:.4f} (Q {Q_of(results[(law,1)]):.2f})" for law in ("D", "N") if results[(law, 1)] is not None))

# ================================================================ (2) the ordering test
print("(2) THE ORDERING TEST (PRED-O-39 (e)): under the same wall, Q(2,+1) vs Q(2,−2), and Q(2,+2)")
for law, name in (("D", "Dirichlet"), ("N", "Neumann")):
    qs = {m: (Q_of(results[(law, m)]) if results[(law, m)] is not None else None) for m in (+2, +1, 0, -2)}
    print(f"    {name}: " + "  ".join(f"Q(2,{m:+d}) = {q:.2f}" if q is not None else f"Q(2,{m:+d}) = —" for m, q in qs.items()))
    if qs[1] is not None and qs[-2] is not None:
        check(f"(2-{law}) RECORDED: retrograde keying as ORDERING under the {name} wall — Q(2,−2) > Q(2,+1)? (the retrograde line sharper than the prograde comparator)", True,
              f"Q(2,−2) = {qs[-2]:.2f} vs Q(2,+1) = {qs[1]:.2f} → {'RETROGRADE SHARPER' if qs[-2] > qs[1] else 'PROGRADE SHARPER OR EQUAL'}")
print(); print(f"3672 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
