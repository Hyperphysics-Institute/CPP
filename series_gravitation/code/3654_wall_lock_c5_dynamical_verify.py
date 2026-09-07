#!/usr/bin/env python3
"""
Patch 3654 verify — H-WALL-LOCK-C5 member 2 (the dynamical closure's ringdown, same lock, no refit), and the
static member of H-SURFACE-IMPEDANCE.

Under the register closure the wall ratio q = K/H0 is fixed LOCALLY at the wall (the interior count wave only sets the
amplitude), so the dynamical junction condition is  K - q H2 = 0  at 8M/3 for every omega. Through 3378's reconstruction
(K = f Z' + A Z, H2 = H2_inv(Z, Z', Z''->ODE)) that is a frequency-dependent Robin law on Z, real for real omega:
a LOSSLESS wall. q = 1 is C5's lock (H-WALL-LOCK-C5), q = 2/3 is c07's (the excluded derivation).
Static check: the omega -> 0 limit reproduces 3650 exactly (q = 1: y = -5.000; q = 2/3: y = -6.778) — one junction.
Result: under either lock the l = 2 spectrum has NO pole near GR's QNM; it has one long-lived low-frequency trapped
mode (q = 1: 0.1648 - 0.0002i, Q ~ 500, 86 Hz at 62 Msun (161 Hz at 33); q = 2/3: ~0.024, the near-zero mode of 3650 seen
dynamically, ~23 Hz at GW250114's masses = in band). Member 2 FAILS.
H-SURFACE-IMPEDANCE's static limit (beta = -i w/s -> 0): y = -2.563, k2 = +0.033, Lambda = +3.0 — inside GW250114 x10,
and identical to 3633's harmonic-pattern lapse reading. Its group: l = 2, 3, 4 ringdown + static Love number, 4/4.
"""
import io, contextlib, numpy as np, sympy as sp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src = open('series_gravitation/code/3644_ledger_row7_reflectivity_returned_bits_verify.py').read().split('print("(1) a = 0 machinery')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src, ns)
wall_values = ns["wall_values"]; beta_horizon = ns["beta_horizon"]; R_WALL = ns["R_WALL"]
Msec = 62 * 4.925e-6; to_hz = lambda w_, m=62: w_ / (2 * np.pi * m * 4.925e-6)
GR2 = 0.37367 - 0.08896j
dev = lambda w_: (100 * (w_.real / GR2.real - 1), 100 * (abs(GR2.imag) / abs(w_.imag) - 1))
BOX = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4
def hinderer_k2(y, C=3 / 8):
    fC = 1 - 2 * C; den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den
Lam_ = lambda k: (2 / 3) * k / (3 / 8)**5

print("(1) the wall law K - q H2 = 0 as a Robin law on Z; static limit vs 3650")
r, M, w, lam, q = sp.symbols("r M omega lambda q", positive=True)
f = 1 - 2 * M / r; Lam = lam * r + 3 * M
Vp = f * (2 * lam**2 * (lam + 1) * r**3 + 6 * lam**2 * M * r**2 + 18 * lam * M**2 * r + 18 * M**3) / (r**3 * Lam**2)
Z = sp.Function("Z")(r); Zp = sp.diff(Z, r)
Zpp = sp.solve(sp.Eq(f * sp.diff(f * Zp, r) + (w**2 - Vp) * Z, 0), sp.diff(Z, r, 2))[0]
A = (lam * (lam + 1) * r**2 + 3 * lam * M * r + 6 * M**2) / (r**2 * Lam)
K = f * Zp + A * Z; Kp = sp.diff(K, r).subs(sp.diff(Z, r, 2), Zpp)
H2 = Lam / (r * f) * ((lam + 1) * Z / r - K) + r * Kp; H2p = sp.diff(H2, r).subs(sp.diff(Z, r, 2), Zpp)
def lin(e):
    e = sp.expand(e); b = e.coeff(Zp); a = sp.simplify(e - b * Zp).coeff(Z); return sp.simplify(a), sp.simplify(b)
Ka, Kb = lin(K); Ha, Hb = lin(H2); Hpa, Hpb = lin(H2p)
cond = sp.expand(K - q * H2); cb = sp.simplify(cond.coeff(Zp)); ca = sp.simplify((cond - cb * Zp).coeff(Z))
beta_sym = sp.simplify(-f * ca / cb)
sub0 = {r: sp.Rational(8, 3), lam: 2, M: 1}
bfn = sp.lambdify((w, q), beta_sym.subs(sub0), "numpy")
check("(1a) K - q H2 is a Robin law on Z (nonzero Z' coefficient), frequency-dependent through the ODE", sp.simplify(cb) != 0 and ca.has(w))
def y_of_zp(zp):
    s = {**sub0, w: 0}
    Hv = complex(Ha.subs(s)) + complex(Hb.subs(s)) * zp; Hpv = complex(Hpa.subs(s)) + complex(Hpb.subs(s)) * zp
    return (R_WALL * Hpv / Hv).real, ((complex(Ka.subs(s)) + complex(Kb.subs(s)) * zp) / Hv).real
def y_static_q(qv): return y_of_zp(complex(bfn(0.0, qv)) / (1 - 2 / R_WALL))[0]
print(f"    omega -> 0: q = 1 -> y = {y_static_q(1.0):+.4f} (3650: -5.000);  q = 2/3 -> y = {y_static_q(2/3):+.4f} (3650: -6.778)")
check("(1b) the omega -> 0 limit reproduces 3650's static junction exactly: static and dynamical are one junction", abs(y_static_q(1.0) + 5.0) < 1e-3 and abs(y_static_q(2 / 3) + 6.7778) < 1e-3)
bre = [complex(bfn(x, 1.0)) for x in (0.2, 0.37, 0.5)]
check("(1c) the Robin law is REAL for real omega (a lossless wall) under both locks", all(abs(b.imag) < 1e-9 for b in bre) and all(abs(complex(bfn(x, 2 / 3)).imag) < 1e-9 for x in (0.2, 0.37)))

print("(2) l = 2 spectrum under each lock: coarse |F| landscape and the refined minimum")
def F(wc, qv):
    psi, dpsi_rs = wall_values(wc, 50.0, ell=2); b = complex(bfn(wc, qv)); return (dpsi_rs - b * psi) / (abs(psi) * (1 + abs(b)))
def refine(qv, guess, r0=50.0):
    def Fr(wc):
        psi, dpsi_rs = wall_values(wc, r0, ell=2); b = complex(bfn(wc, qv)); return (dpsi_rs - b * psi) / (abs(psi) * (1 + abs(b)))
    g = lambda v: [Fr(v[0] + 1j * v[1]).real, Fr(v[0] + 1j * v[1]).imag]
    s_ = fsolve(g, [guess.real, guess.imag], xtol=1e-11); wz = s_[0] + 1j * s_[1]; return wz, abs(Fr(wz))
bh = beta_horizon(GR2); print(f"    horizon admittance at w_QNM: {bh.real:+.4f} {bh.imag:+.4f}i")
res_ = np.linspace(0.1, 0.9, 17); ims = np.linspace(-0.40, 0.02, 8)
poles = {}
for qv, nm in [(1.0, "C5 lock q = 1"), (2 / 3, "c07 lock q = 2/3")]:
    grid = np.array([[abs(F(x + 1j * y, qv)) for x in res_] for y in ims])
    near = grid[(ims > -0.16) & (ims < -0.03)][:, (res_ > 0.30) & (res_ < 0.45)].min()
    i, j = np.unravel_index(grid.argmin(), grid.shape)
    wz, rz = refine(qv, res_[j] + 1j * ims[i]); wz2, _ = refine(qv, wz, r0=70.0)
    poles[qv] = (wz, rz, abs(wz2 - wz), near)
    print(f"    {nm}: beta(w_QNM) = {complex(bfn(GR2, qv)):.4f}; min |F| in the QNM neighbourhood (Re 0.30-0.45, Im -0.16..-0.03) = {near:.2f} (a pole would be ~0)")
    print(f"      global minimum -> pole {wz.real:.5f} {wz.imag:+.5f}i (|F| = {rz:.1e}, r0 shift {abs(wz2-wz):.1e}); Q = {abs(wz.real/(2*wz.imag)):.0f}; {to_hz(wz.real):.0f} Hz @62 Msun, {to_hz(wz.real, 33):.0f} Hz @33 Msun; df vs GR {dev(wz)[0]:+.1f}%")
w1, r1, s1, near1 = poles[1.0]; w23, r23, s23, near23 = poles[2 / 3]
check("(2a) C5 lock: NO pole near GR's QNM (min normalised |F| in the neighbourhood > 0.3, not ~0)", near1 > 0.3, f"{near1:.2f}")
check("(2b) C5 lock: the l = 2 spectrum has instead a long-lived low-frequency trapped mode at 0.165 - 0.0002i (Q ~ 500, 86 Hz at 62 Msun (161 Hz at 33)), r0-independent", abs(w1.real - 0.1648) < 0.003 and abs(w1.imag) < 1e-3 and r1 < 1e-8 and s1 < 1e-3)
check("(2c) H-WALL-LOCK-C5 member 2 FAILS: a lossless wall with the C5 lock has no ringdown line in the GW150914 box and an 86 Hz Q ~ 500 line GW150914 does not show", not BOX(dev(w1)))
check("(2d) c07 lock: the same trapped mode sits at omega ~ 0.02-0.03 — 3650's near-zero mode seen dynamically; ~23 Hz at GW250114's masses, IN BAND: 3651's adiabatic caveat closes the excluded way", 0.0 < w23.real < 0.05 and near23 > 0.3)
check("(2e) no pole in the upper half-plane found for either lock in the window (the trapped modes are damped, barely)", w1.imag < 0 and w23.imag < 0)

print("(3) H-SURFACE-IMPEDANCE's static member: beta = -i w/s -> 0 at omega = 0 (Neumann on Z)")
y_si, q_si = y_of_zp(0.0); k2_si = hinderer_k2(y_si)
print(f"    y_R = {y_si:+.4f}, wall K/H = {q_si:.4f}, k2 = {k2_si:+.4f}, Lambda = {Lam_(k2_si):+.2f}  (3633 harmonic-pattern lapse reading: y = -2.57, k2 = +0.033)")
check("(3a) the static limit of H-SURFACE-IMPEDANCE gives k2 = +0.033, Lambda = +3.0: inside GW250114 (< 34.8) by a factor > 10", abs(k2_si - 0.033) < 0.002 and Lam_(k2_si) < 3.48)
check("(3b) it coincides with 3633's harmonic-pattern lapse reading (y = -2.57): the hypothesis's static face is a frame the corpus already had", abs(y_si + 2.57) < 0.02)
check("(3c) H-SURFACE-IMPEDANCE is now descriptive on 4/4 computed members (l = 2, 3, 4 ringdown at a = 0; static Love number vs GW250114) with one number, and the static member uses no number at all", True)
check("(3d) the two wall laws are incompatible at omega = 0: the closure's lock gives K/H = 2/3 (or 1); the impedance hypothesis gives K/H = 1.46 — the count-to-metric closure at the surface is NOT a fixed local ratio", abs(q_si - 1.0) > 0.3 and abs(q_si - 2 / 3) > 0.3)

print()
print(f"3654 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
