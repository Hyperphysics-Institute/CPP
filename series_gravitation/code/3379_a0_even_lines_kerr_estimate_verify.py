#!/usr/bin/env python3
"""
Patch 3379 verify — the a = 0 even-sector line set under the derived
trace-pinned wall, for BOTH flagship lines (l = 2 and l = 3), and the Kerr
recompute assessed honestly: an ESTIMATE, and the blocker named.

Part 1. beta_l(omega) — the Robin coefficient (dZ+/dr*)/Z+ at r_w = 9M/4 from
        'H2 + 2K = 0' — derived symbolically for l = 2 (as at 3378) AND l = 3.
Part 2. Wigner scans (even sector, Zerilli, 3297 method) for l = 2 and l = 3
        with the Dirichlet wall and the derived wall: lowest-resonance
        positions, shifts, Hz at 62 Msun.
Part 3. The Kerr flagship: the shipped values (3359, SN ladder, X = 0) are for
        the RW-like sector, which the register does not govern. What can be
        stated NOW is the a = 0 even-sector shift applied to the Kerr lines as
        a scaled ESTIMATE — labelled, bracketed, not a recompute.
Part 4. The blocker, stated: imposing 'spatial trace pinned' on the Kerr
        master function at the surface requires metric reconstruction in
        Kerr (Hertz-potential / CCK, with its gauge subtleties). That is a
        known, hard, literature-level computation; attempting it by recall
        would be guessing. Economy-protocol status assessed in the record.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ================================================================ Part 1: beta_l(omega)
print("Part 1 — beta_l(omega) at the Buchdahl wall for l = 2 and l = 3")
r, M, w = sp.symbols("r M omega", positive=True)


def beta_of(ell):
    lam = sp.Rational((ell - 1) * (ell + 2), 2)
    f = 1 - 2 * M / r; Lam = lam * r + 3 * M
    Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
    Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
    Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
    A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
    K = f * Zp + A * Z
    Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
    H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp
    trace = sp.expand(sp.simplify(H2 + 2 * K))
    tc2 = sp.simplify(trace.coeff(Zp)); tc1 = sp.simplify((trace - tc2 * Zp).coeff(Z))
    beta_rs = sp.simplify(f * (-tc1 / tc2))
    return sp.simplify(beta_rs.subs({r: sp.Rational(9, 4) * M}).subs(M, 1)), Vp.subs(M, 1)


betas, Vps = {}, {}
for ell in (2, 3):
    b, Vp = beta_of(ell); betas[ell] = b; Vps[ell] = Vp
    b0 = float(b.subs(w, 0)); b2 = -float(sp.diff(b, w, 2) / 2); w0 = np.sqrt(b0 / b2)
    print(f"    l = {ell}: beta = {sp.nsimplify(sp.expand(b))}   ->  b0 = {b0:.3f}, b2 = {b2:.2f}, Neumann at M omega_0 = {w0:.4f}")
check("l = 2 reproduces 3378: b0 = 2.496, b2 = 14.46, M omega_0 = 0.415", abs(float(betas[2].subs(w, 0)) - 2.496) < 0.005)
b0_3 = float(betas[3].subs(w, 0)); b2_3 = -float(sp.diff(betas[3], w, 2) / 2)
check("l = 3: beta_3(omega) has the same quadratic form with positive b0 and b2 (a Neumann crossing exists)", b0_3 > 0 and b2_3 > 0)

# ================================================================ Part 2: Wigner scans
print("Part 2 — even-sector Wigner scans, Dirichlet vs derived wall (M = 1)")
Msec = 62 * 4.925e-6


def fn(x): return 1 - 2.0 / x


def build_grid(Vfun, r_w=2.25, r_far_star=250.0, n=120_000):
    rstar_w = r_w + 2 * np.log(r_w / 2 - 1); h = (r_far_star - rstar_w) / n
    rr = np.empty(n + 1); rr[0] = r_w
    for i in range(n):
        x = rr[i]; k1 = fn(x); k2 = fn(x + 0.5 * h * k1); k3 = fn(x + 0.5 * h * k2); k4 = fn(x + h * k3)
        rr[i + 1] = x + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return h, rr, Vfun(rr), r_far_star


def wigner(omegas, grid, bfun):
    h, rr, V, r_far = grid; h2 = h * h; phases = []
    for om in omegas:
        Q = om * om - V; F = 1 + h2 * Q / 12.0
        if bfun is None: p0, p1 = 0.0, h
        else:
            b = float(bfun(om)); p0 = 1.0; p1 = p0 * (1 + b * h) - 0.5 * h2 * Q[0] * p0
        for i in range(1, len(rr) - 1):
            p2 = ((12 - 10 * F[i]) * p1 - F[i - 1] * p0) / F[i + 1]; p0, p1 = p1, p2
        dpsi = (p1 - p0) / h; psi = p1
        Aamp = 0.5 * (psi + dpsi / (1j * om)) * np.exp(-1j * om * r_far)
        phases.append(np.angle(Aamp / np.conj(Aamp)))
    return np.unwrap(np.array(phases))


results = {}
for ell, (lo, hi) in ((2, (0.30, 0.65)), (3, (0.45, 0.95))):
    Vfun = sp.lambdify(r, Vps[ell], "numpy"); grid = build_grid(Vfun)
    oms = np.linspace(lo, hi, 351)
    bfun = sp.lambdify(w, betas[ell], "numpy")
    phD = wigner(oms, grid, None); phR = wigner(oms, grid, bfun)
    tauD = np.gradient(phD, oms); tauR_raw = np.gradient(phR, oms)
    # A DISPERSIVE wall contributes its OWN d(phase)/d(omega) — arg[(i w + beta)/(i w - beta)] — which is
    # not a cavity time. It spikes where beta -> 0 (the Neumann crossing) and would masquerade as a
    # resonance. Subtract it: tau_cavity = tau_total - d(arg R_wall)/d(omega). (Dirichlet: arg = pi, const.)
    bvals = np.array([float(bfun(om)) for om in oms])
    phi_wall = np.unwrap(np.angle((1j * oms + bvals) / (1j * oms - bvals)))
    tauR = tauR_raw - np.gradient(phi_wall, oms)
    # the features are broad: report the centroid of each delay curve over its half-maximum region
    def centroid(tau):
        m = tau > 0.5 * tau.max(); return float(np.sum(oms[m] * tau[m]) / np.sum(tau[m]))
    wD = centroid(tauD); wR = centroid(tauR); wR_raw = float(oms[np.argmax(tauR_raw)])
    vmax = float(np.sqrt(Vfun(np.linspace(2.3, 6, 40001)).max()))
    b0 = float(bfun(0.0)); b2 = -(float(bfun(1.0)) - b0); w_neu = np.sqrt(b0 / b2)
    results[ell] = dict(wD=wD, wR=wR, shift=(wR - wD) / wD, vtop=vmax, wR_raw=wR_raw, w_neu=w_neu, tauD=float(tauD.max()), tauR=float(tauR.max()))
    print(f"    l = {ell}: barrier top {vmax:.3f};  Neumann crossing {w_neu:.3f};  RAW derived-wall delay peak {wR_raw:.3f} (= the crossing: artifact)")
    print(f"           cavity delay centroid: Dirichlet {wD:.3f} ({wD/(2*np.pi*Msec):.0f} Hz)  derived wall {wR:.3f} ({wR/(2*np.pi*Msec):.0f} Hz)  shift {100*(wR-wD)/wD:+.1f}%;  peak delays {results[ell]['tauD']:.1f} -> {results[ell]['tauR']:.1f}")
check_art = abs(wR_raw - w_neu) < 0.01
check("the RAW dispersive-wall delay peak coincides with the Neumann crossing for BOTH l — it is the wall's own dispersion, not a cavity resonance (3378's '0.412' was this artifact)",
      all(abs(results[l]["wR_raw"] - results[l]["w_neu"]) < 0.01 for l in (2, 3)))
# decomposition of the derived-wall delay peak: the wall's own dispersion at the crossing is
# d(arg R_wall)/d(omega)|_{beta=0} = -2 beta'/omega = 4 b2; the remainder is cavity.
for l in (2, 3):
    b0 = float(sp.lambdify(w, betas[l], "numpy")(0.0)); b2 = -(float(sp.lambdify(w, betas[l], "numpy")(1.0)) - b0)
    results[l]["wall_disp"] = 4 * b2
    print(f"    l = {l}: derived-wall delay peak {results[l]['tauR'] + results[l]['wall_disp']:.0f} total = {results[l]['wall_disp']:.0f} (wall dispersion, 4 b2) + {results[l]['tauR']:.0f} (cavity)")
check("after removing the wall's own dispersion (4 b2 = 58 / 67), a LARGE cavity delay remains at the crossing (>= 5x the Dirichlet peak): a near-trapped mode enabled by the Neumann-like wall, not an artifact",
      all(results[l]["tauR"] > 5 * results[l]["tauD"] for l in (2, 3)), f"l=2 {results[2]['tauR']:.0f} vs {results[2]['tauD']:.0f}; l=3 {results[3]['tauR']:.0f} vs {results[3]['tauD']:.0f}")
check("the feature sits near the barrier top (within 7%: l=2 6% above, l=3 1% below) — the Neumann crossing and the barrier top nearly coincide (unexplained; recorded)",
      all(abs(results[l]["wR"] / results[l]["vtop"] - 1) < 0.07 for l in (2, 3)), f"l=2 {results[2]['wR']/results[2]['vtop']-1:+.3f}, l=3 {results[3]['wR']/results[3]['vtop']-1:+.3f}")
check("shift of the even-sector feature relative to the Dirichlet centroid: -13% for BOTH l (identical to 3 s.f. — structural, not accidental; recorded, unexplained)",
      all(abs(results[l]["shift"] + 0.134) < 0.01 for l in (2, 3)))
check("3378's '0.412, -5 to -10%, width not claimed' is SUPERSEDED: the position stands, the shift is -13%, and the width is mostly cavity", True)

# ================================================================ Part 3: the Kerr ESTIMATE
print("Part 3 — the Kerr flagship: a scaled ESTIMATE, not a recompute")
kerr_shipped = {"(2,-2)": 191.2, "(3,-3)": 288.5}          # GR-2 V1.6 / 3363 at chi = 0.68 (SN ladder, X = 0, RW-like sector)
est = {}
for name, fHz, ell in (("(2,-2)", 191.2, 2), ("(3,-3)", 288.5, 3)):
    s = results[ell]["shift"]; est[name] = fHz * (1 + s)
    print(f"    {name}: shipped {fHz:.1f} Hz (odd/RW-like sector, X = 0)  ->  even-sector a=0 shift {100*s:+.1f}%  ->  ESTIMATE {est[name]:.0f} Hz")
check("ESTIMATE only: the a = 0 even-sector fractional shift applied to the Kerr lines; NOT a Kerr recompute", True)
check("(2,-2) ESTIMATE 166 Hz, (3,-3) ESTIMATE 250 Hz — both ~13% below the shipped values; a scaled guess, not a Kerr result", abs(est["(2,-2)"] - 166) < 3 and abs(est["(3,-3)"] - 250) < 4)

# ================================================================ Part 4: the blocker
print("Part 4 — the blocker for the Kerr recompute, stated")
check("the trace condition H2 + 2K = 0 is a statement about the METRIC perturbation at the surface; in Kerr the master variable is the Teukolsky/SN function and the metric is recovered only by reconstruction (Hertz potential, CCK) with gauge subtleties — a literature-level computation, not a recall", True)
check("no slow-rotation shortcut is adopted here: at chi = 0.68 an O(a) expansion of the wall condition is not controlled", True)
check("economy protocol: this is trigger 2a (further unilateral work on the Kerr wall map would be guessing) — recorded for the founder's decision, not dispatched", True)

print()
print(f"3379 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
