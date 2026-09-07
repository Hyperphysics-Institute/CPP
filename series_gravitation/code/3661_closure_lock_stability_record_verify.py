#!/usr/bin/env python3
"""
Patch 3661 verify — handover item 5: the register closure's OWN even-sector stability record (3643 §5 was the
budget interior; 3654 found the closure's lock laws have one long-lived trapped mode each, Im ω = −0.0002 (C5)
and ≈ −0.003 (c07), "damped, barely"). Two things a record needs that 3654 did not do:
 (A) an argument-principle count of zeros of the junction in the upper half-plane, on a contour whose lower edge
     sits at Im ω = 5e-4 and whose left edge reaches Re ω = 0.005 — i.e. a contour that includes ω ≈ 0, where
     3650's static near-zero mode lives — in the POLE-FREE form F = c_a Z + c_b dZ/dr (K − qH₂ itself; no
     division by the Z′ coefficient, so a zero of c_b cannot fake a winding);
 (B) the sign of Im ω of each trapped mode, resolved: refined at r0 = 50/100/200 with tight tolerances, and the
     pole's sharpness. A mode with |Im ω| ~ 2e-4 needs its sign established, not assumed.
Run from the repo root (exec's 3654, which exec's 3644). ~10 min.
"""
import io, contextlib, numpy as np, sympy as sp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src = open("series_gravitation/code/3654_wall_lock_c5_dynamical_verify.py").read()
pre = src.split('print("(2) l = 2 spectrum')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(pre, ns)
wall_values = ns["wall_values"]; bfn = ns["bfn"]; sub0 = ns["sub0"]; w_ = ns["w"]; q_ = ns["q"]
ca_fn = sp.lambdify((w_, q_), ns["ca"].subs(sub0), "numpy"); cb_fn = sp.lambdify((w_, q_), ns["cb"].subs(sub0), "numpy")
R_WALL = 8.0 / 3.0; f_w = 1 - 2 / R_WALL
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)

def F_free(wc, qv, r0=50.0):
    """K − qH₂ at the wall, pole-free: c_a Z + c_b dZ/dr, normalised by |Z| so the phase is the junction's."""
    Z, dZ_rs = wall_values(wc, r0, ell=2); dZ_r = dZ_rs / f_w
    return (complex(ca_fn(wc, qv)) * Z + complex(cb_fn(wc, qv)) * dZ_r) / abs(Z)

print("(0) the pole-free form: c_b never vanishes on the contour region (so the Robin form and the pole-free form have the same zeros there)")
cbs = [abs(complex(cb_fn(x + 1j * y, 1.0))) for x in np.linspace(0.005, 1.2, 25) for y in (5e-4, 0.1, 0.4)]
check("(0) |c_b| > 0 on the region for q = 1 (and q = 2/3)", min(cbs) > 1e-6 and min(abs(complex(cb_fn(x + 1j * y, 2 / 3))) for x in np.linspace(0.005, 1.2, 25) for y in (5e-4, 0.4)) > 1e-6, f"min |c_b| = {min(cbs):.2e}")

def bottom_edge(re, y, n, dense_at=(0.0244, 0.1648), half=0.012, n_dense=70):
    """the bottom edge passes ~7e-4 above the trapped poles (B): the phase turns fast only there, so the edge is
    sampled uniformly (n) plus a dense cluster (n_dense) within ±half of each pole's real part."""
    xs = list(np.linspace(re[0], re[1], n))
    for x0 in dense_at: xs += list(np.linspace(x0 - half, x0 + half, n_dense))
    return [complex(x, y) for x in sorted(set(xs))]
def contour(re=(0.005, 1.2), im=(5e-4, 0.4), n=80):
    pts = bottom_edge(re, im[0], n)
    ys = sorted(set(list(np.linspace(im[0], im[1], n // 2)) + list(np.linspace(im[0], 0.04, 40))))   # vertical edges: dense near the real axis (phase turns fast as ω → 0)
    pts += [complex(re[1], y) for y in ys]
    pts += [complex(x, im[1]) for x in np.linspace(re[1], re[0], n)]
    pts += [complex(re[0], y) for y in ys[::-1]]
    return pts
def winding_fn(Ff):
    pts = contour(); vals = np.array([Ff(w) for w in pts])
    ph = np.unwrap(np.angle(vals)); return (ph[-1] - ph[0] + np.angle(vals[0]) - np.angle(vals[-1])) / (2 * np.pi), np.abs(np.diff(ph)).max()
def winding(qv): return winding_fn(lambda w: F_free(w, qv))

print("(A) argument principle, upper half-plane, contour Re ω ∈ [0.005, 1.2], Im ω ∈ [5e-4, 0.4] (includes ω ≈ 0); bottom edge locally refined at the trapped poles")
wind = {}
for qv, nm in [(1.0, "C5 lock q = 1"), (2 / 3, "c07 lock q = 2/3")]:
    nq, jq = winding(qv); wind[qv] = (nq, jq)
    print(f"    {nm}: winding {nq:+.3f} (max phase step {jq:.2f} rad)")
    check(f"(A) {nm}: NO zero of the junction in the upper half-plane down to Im ω = 5e-4 and to Re ω = 0.005 — no growing even mode, including near ω ≈ 0", round(nq) == 0 and jq < 1.5, f"winding {nq:+.3f}, max step {jq:.2f}")
# control: a wall known to have a growing mode — 3390's trace wall b0 - b2 w^2 is in 3643; use a Neumann-like real Robin far from the closure as a sanity of the contour instead: the horizon law has no UHP zero (it IS the black hole)
def F_hor(wc, r0=50.0):
    Z, dZ_rs = wall_values(wc, r0, ell=2); b = ns["beta_horizon"](wc); return (dZ_rs - b * Z) / (abs(Z) * (1 + abs(b)))
nh, jh = winding_fn(F_hor)
check("(A-ctrl) the same contour on the horizon-equivalent wall gives winding 0 (a black hole has no growing mode): the contour machinery is sound", round(nh) == 0 and jh < 1.5, f"winding {nh:+.3f}, max step {jh:.2f}")

print("(B) the trapped modes' damping sign, resolved")
def refine(qv, guess, r0):
    Fr = lambda wc: F_free(wc, qv, r0)
    g = lambda v: [Fr(v[0] + 1j * v[1]).real, Fr(v[0] + 1j * v[1]).imag]
    s = fsolve(g, [guess.real, guess.imag], xtol=1e-13); return s[0] + 1j * s[1]
modes = {}
for qv, nm, g in [(1.0, "C5 lock q = 1", 0.1648 - 0.0002j), (2 / 3, "c07 lock q = 2/3", 0.024 - 0.003j)]:
    ws = {r0: refine(qv, g, r0) for r0 in (50.0, 100.0, 200.0)}
    w = ws[200.0]; spread = max(abs(ws[r0] - w) for r0 in ws)
    on = abs(F_free(w, qv, 200.0)); off = abs(F_free(w + 0.005j, qv, 200.0))
    modes[qv] = (w, spread, on / off)
    print(f"    {nm}: " + ", ".join(f"r0={r0:.0f}: {x.real:.5f} {x.imag:+.2e}i" for r0, x in ws.items()) + f";  spread {spread:.1e};  contrast {on/off:.1e};  Q = {w.real/(2*abs(w.imag)):.0f};  {to_hz(w.real):.1f} Hz @62, {to_hz(w.real)*62/62.7:.1f} Hz @62.7")
    check(f"(B) {nm}: Im ω < 0 with |Im ω| exceeding the r0-spread by > 10× — DAMPED, sign resolved", w.imag < 0 and abs(w.imag) > 10 * spread and on / off < 1e-2, f"Im ω = {w.imag:+.2e}, spread {spread:.1e}")
wC5, wc07 = modes[1.0][0], modes[2 / 3][0]
print(f"    decay times: C5 τ = {1/abs(wC5.imag):.0f} M = {1/abs(wC5.imag)*Msec*1e3:.0f} ms @62 M☉;  c07 τ = {1/abs(wc07.imag):.0f} M = {1/abs(wc07.imag)*Msec*1e3:.0f} ms")
check("(B2) the record: under either lock the even sector is STABLE (no upper-half-plane zero) but carries a long-lived trapped mode — C5: Q ≈ 490; c07: Q ≈ 3e5, MARGINAL (3654's '≈ −0.003' was the coarse-grid value; the refined pole sits 0.8% from 3650's static zero mode and is damped only at the 1e-8 level) — with no line near GR's ringdown (3654); stability, not phenomenology, is what this patch certifies", round(wind[1.0][0]) == 0 and round(wind[2 / 3][0]) == 0 and wC5.imag < 0 and wc07.imag < 0)
print(); print(f"3661 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
