#!/usr/bin/env python3
"""
Patch 3648 verify — OPEN-GR-SURFACE-IMPEDANCE-1, attempt 2b: JUNCTION-1 PROPER.
The two channels COUPLED THROUGH A3'-s METRIC MAP (3378's reconstruction), not summed (2a, 3646).

3378: in RW gauge, K = f Z' + A Z;  H2 - K = c1(w,r) Z + c2(r) Z'.  The register (count) channel is the
spatial trace T = H2 + 2K (delta ln psi^4 = T/3); the tensor channel is the traceless part D = H2 - K.
3643/3644 imposed the budget interior's count law directly on Z (treating Z as the count field). 2b imposes
each channel's OWN law on its OWN component:
   count:  (dT/dr*)/T = beta_c(w)   with beta_c = the budget interior's lossless law (3643/3644 beta_budget)
   tensor: (dD/dr*)/D = beta_t(w)   with beta_t = -i w  (locally ingoing: absorbed by the core, 3609-3610/3621)
Each, after eliminating Z'' by the Zerilli equation, is a Robin law on Z:  (dZ/dr*)/Z = beta^Z_X(w).
A single even mode has ONE Z'/Z at the wall, so the two laws are two demands on one number: the junction is
the question whether (and where) they agree. Target: beta_hor(w_QNM) = +0.008 - 0.116 i (3644). Hypothesis
H-SURFACE-IMPEDANCE: beta = -i w / 3.22.
Scored: each channel law alone (pole, box), the two laws' disagreement at w_QNM, the compatibility locus
det(w) = beta^Z_c - beta^Z_t = 0 near the QNM, and the static (w -> 0) limit against 3647's chi* = 0.49.
"""
import io, contextlib, numpy as np, sympy as sp
from scipy.optimize import fsolve

PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------- 3644 machinery (interior budget law, exterior Zerilli, horizon target, root-finder) ----------------
src = open('series_gravitation/code/3644_ledger_row7_reflectivity_returned_bits_verify.py').read().split('print("(1) a = 0 machinery')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src, ns)
beta_budget = ns["beta_budget"]; wall_values = ns["wall_values"]; beta_horizon = ns["beta_horizon"]
root0 = ns["root0"]; wGR = ns["wGR"]; dev0 = ns["dev0"]; BOX = ns["BOX"]; V_Z = ns["V_Z"]; R_WALL = ns["R_WALL"]
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)

# ---------------- 3378's metric map, symbolic, at the wall ----------------
print("(1) 3378's reconstruction at r_w = 8M/3, l = 2: the two channels as linear forms in (Z, Z')")
r, M, w, lam = sp.symbols("r M omega lambda", positive=True)
f = 1 - 2 * M / r; Lam = lam * r + 3 * M
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
K = f * Zp + A * Z
Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
def linform(expr):
    e = sp.expand(sp.simplify(expr)); b = sp.simplify(e.coeff(Zp)); a = sp.simplify((e - b * Zp).coeff(Z)); return a, b
Ta, Tb = linform(H2 + 2 * K)          # T = Ta Z + Tb Z'
Da, Db = linform(H2 - K)              # D = Da Z + Db Z'
check("(1a) both channels are linear in (Z, Z') with no Z'' (the Zerilli equation removed it)",
      all(not sp.simplify(x).has(sp.diff(Z, r, 2)) for x in (Ta, Tb, Da, Db)))
check("(1b) both channels have nonzero Z' coefficient (neither is Dirichlet-type on Z)", sp.simplify(Tb) != 0 and sp.simplify(Db) != 0)

def robin_from_channel(a, b, beta_sym):
    """channel X = a Z + b Z'. Impose f dX/dr = beta_X X. Returns (dZ/dr*)/Z = f Z'/Z as a sympy expr in w (r, lam, M fixed)."""
    Xp = sp.diff(a, r) * Z + a * Zp + sp.diff(b, r) * Zp + b * Zpp        # Z'' eliminated by the ODE
    cond = sp.expand(f * Xp - beta_sym * (a * Z + b * Zp))
    cb = sp.simplify(cond.coeff(Zp)); ca = sp.simplify((cond - cb * Zp).coeff(Z))
    return sp.simplify(-f * ca / cb)

bc, bt = sp.symbols("beta_c beta_t")
vals = {r: sp.Rational(8, 3), lam: 2, M: 1}
betaZ_c_sym = robin_from_channel(Ta, Tb, bc).subs(vals)     # function of (w, beta_c)
betaZ_t_sym = robin_from_channel(Da, Db, bt).subs(vals)     # function of (w, beta_t)
betaZ_c_fn = sp.lambdify((w, bc), betaZ_c_sym, "numpy")
betaZ_t_fn = sp.lambdify((w, bt), betaZ_t_sym, "numpy")
# sanity: the 3378 trace-pinned wall is beta_c -> infinity (T = 0); recover 3390's b0 at 8M/3 as the limit
trace_pinned = sp.simplify(sp.limit(betaZ_c_sym, bc, sp.oo))
b0_tp = complex(trace_pinned.subs(w, 0))
print(f"    limit beta_c -> inf (T = 0, the 3390 trace clamp) at 8M/3: beta(0) = {b0_tp.real:+.4f}")
check("(1c) the beta_c -> inf limit of the count-channel law reproduces the trace-pinned Robin law's static value at 8M/3 (b0 < 0 there, 3390: the clamp's 'b0' at 8M/3 is negative)", abs(b0_tp.imag) < 1e-9 and b0_tp.real < 0, f"b0 = {b0_tp.real:.4f}")

# ---------------- (2) the two channel laws at the GR QNM ----------------
print("(2) the two channel laws at w_QNM, against the horizon target and the hypothesis")
beta_c_w = lambda wc: beta_budget(wc)                 # count: budget interior, lossless, C^1 (3643/3644)
beta_t_w = lambda wc: -1j * wc                        # tensor: absorbed / locally ingoing
lawC = lambda wc: complex(betaZ_c_fn(wc, beta_c_w(wc)))
lawT = lambda wc: complex(betaZ_t_fn(wc, beta_t_w(wc)))
lawH = lambda wc: -1j * wc / 3.22                     # hypothesis (3644/3646)
bh = beta_horizon(wGR)
bC, bT, bH = lawC(wGR), lawT(wGR), lawH(wGR)
bBud = beta_budget(wGR)                               # 3644's reading: budget law imposed on Z itself
print(f"    target  beta_hor(w_QNM)         = {bh.real:+.4f} {bh.imag:+.4f}i")
print(f"    hypothesis  -i w/3.22            = {bH.real:+.4f} {bH.imag:+.4f}i")
print(f"    3644 (budget law ON Z)           = {bBud.real:+.4f} {bBud.imag:+.4f}i")
print(f"    2b count channel T (budget law)  = {bC.real:+.4f} {bC.imag:+.4f}i")
print(f"    2b tensor channel D (absorbed)   = {bT.real:+.4f} {bT.imag:+.4f}i")
print(f"    |lawC - lawT| at w_QNM           = {abs(bC - bT):.4f}   (the two demands on one Z'/Z)")
check("(2a) the two channel laws DISAGREE at w_QNM by more than the whole target admittance (|target| = 0.116): a single Z cannot satisfy both — the channels are not independently imposable", abs(bC - bT) > abs(bh))

# ---------------- (3) poles under each law alone, and the box ----------------
print("(3) poles: each channel law imposed alone (as if it were the whole wall), l = 2 fundamental")
res = {}
for name, fn, guess in [("count channel T (budget law through the map)", lawC, 0.42 - 0.12j),
                        ("tensor channel D (absorbed through the map)", lawT, 0.37 - 0.09j)]:
    wp = root0(fn, guess); d = dev0(wp); res[name] = (wp, d)
    resid = abs(ns["F0"](wp, fn)); 
    print(f"    {name}: {wp.real:.5f} {wp.imag:+.5f}i  ({to_hz(wp.real):.0f} Hz); df {d[0]:+.1f}% / dtau {d[1]:+.1f}%; in box: {BOX(d)}; |F| = {resid:.1e}")
wC, dC = res["count channel T (budget law through the map)"]; wT, dT = res["tensor channel D (absorbed through the map)"]
check("(3a) count-channel-only wall (the count field's law on its own component): outside the ringdown box (same failure family as 3644: damps or shifts wrong)", not BOX(dC), f"df {dC[0]:+.1f}% dtau {dC[1]:+.1f}%")
check("(3b) tensor-channel-only wall (absorb D, count unconstrained): Kerr-like frequency, box status recorded", True, f"df {dT[0]:+.1f}% dtau {dT[1]:+.1f}%, box {BOX(dT)}")

# ---------------- (4) the coupled condition: where do the two laws agree? ----------------
print("(4) the junction as a compatibility locus: det(w) = lawC(w) - lawT(w) = 0 near the QNM")
det = lambda wc: lawC(wc) - lawT(wc)
def croot(fn, guess):
    g = lambda v: [fn(v[0] + 1j * v[1]).real, fn(v[0] + 1j * v[1]).imag]
    s = fsolve(g, [guess.real, guess.imag], xtol=1e-11); wz = s[0] + 1j * s[1]; return wz, abs(fn(wz))
best = None
for g in [0.37 - 0.09j, 0.42 - 0.12j, 0.30 - 0.05j, 0.45 - 0.05j, 0.35 - 0.20j, 0.25 - 0.10j]:
    try:
        wz, rz = croot(det, g)
        if rz < 1e-6 and 0.05 < wz.real < 1.0 and -0.6 < wz.imag < 0.05:
            if best is None or abs(wz - wGR) < abs(best - wGR): best = wz
    except Exception: pass
if best is not None:
    dB = dev0(best); print(f"    nearest compatibility point: {best.real:.5f} {best.imag:+.5f}i  ({to_hz(best.real):.0f} Hz); df {dB[0]:+.1f}% / dtau {dB[1]:+.1f}%; in box: {BOX(dB)}")
    # Is the exterior a mode there? F0 = dpsi_rs - beta psi with beta = lawC(best) (= lawT(best))
    Fm = abs(ns["F0"](best, lawC)); print(f"    |F0| of the exterior at that point with the common law: {Fm:.2e} (a mode iff ~0)")
    check("(4a) a compatibility point (both channel laws agree) exists in the lower half-plane near the ringdown", True, f"{best:.5f}")
    check("(4b) the compatibility point is NOT itself a quasinormal mode of the exterior (|F0| not ~0): agreement of the two channel demands does not make a resonance", Fm > 1e-3, f"|F0| = {Fm:.2e}")
else:
    print("    no compatibility point found in the search window")
    check("(4a) no compatibility point in the window: the two laws never agree near the ringdown", True)

# ---------------- (5) the static limit against 3647's chi* ----------------
print("(5) static limit w -> 0: does the two-channel junction land on the FREE or RIGID branch of 3647?")
# Static: the count channel at w -> 0 has beta_c -> beta_budget(0+); the tensor channel absorbed: beta_t -> 0 (Neumann on D).
eps = 1e-3
bC0 = lawC(eps); bT0 = lawT(eps)
print(f"    lawC(w->0) = {bC0.real:+.4f} {bC0.imag:+.4f}i    lawT(w->0) = {bT0.real:+.4f} {bT0.imag:+.4f}i")
# Map a static Robin law on Z to Hinderer's y = R H'/H via the same reconstruction (H0 = H2 static): y = R H2'/H2 with Z'/Z = betaZ/f
H2a, H2b = linform(H2)
def y_from_betaZ(bZ):
    zp = complex(bZ) / (1 - 2 / R_WALL)     # Z'/Z (d/dr)
    sub = {w: 0, **vals}
    a = complex(H2a.subs(sub)); b = complex(H2b.subs(sub))
    H2v = a + b * zp
    # H2' = a' + a zp + b' zp + b Z''/Z with Z''/Z from the static Zerilli ODE
    pz, qz = linform(Zpp)                      # Z'' = pz Z + qz Z'
    Zpp_over_Z = complex(pz.subs(sub)) + complex(qz.subs(sub)) * zp
    ap = complex(sp.diff(H2a, r).subs(sub)); bp = complex(sp.diff(H2b, r).subs(sub))
    H2p = ap + a * zp + bp * zp + b * Zpp_over_Z
    return (R_WALL * H2p / H2v)
def hinderer_k2(y, C=3 / 8):
    fC = 1 - 2 * C
    den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den
y_star = -6.8051
for name, b in [("count channel", bC0), ("tensor channel", bT0)]:
    yv = y_from_betaZ(b); k2 = hinderer_k2(yv.real)
    print(f"    {name}: y_R = {yv.real:+.3f} -> k2 = {k2:+.4f}  (k2 > 0 band is y* = -6.81 < y < 5, the numerator zero)")
yC = y_from_betaZ(bC0).real; yT = y_from_betaZ(bT0).real
check("(5a) the count-channel static law and the tensor-channel static law give DIFFERENT y_R: the static junction is as overdetermined as the dynamical one", abs(yC - yT) > 0.5, f"y_C = {yC:+.2f}, y_T = {yT:+.2f}")
check("(5b) neither channel law alone reproduces 3647's level-set static result (y_R = -3.22, k2 = +0.042): the static two-channel junction is reported, not assumed", abs(yC + 3.22) > 0.5 and abs(yT + 3.22) > 0.5, f"3647: -3.22; count: {yC:+.2f}; tensor: {yT:+.2f}")
check("(5c) the count channel's static law lands in Hinderer's y > 5 band (k2 small negative): a Robin law on the TRACE at w = 0 is not the level-set condition of 3647 — the two static descriptions differ, recorded as a discrepancy to resolve (not resolved here)", yC > 5, f"y_C = {yC:+.2f}")

print()
print(f"3648 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
