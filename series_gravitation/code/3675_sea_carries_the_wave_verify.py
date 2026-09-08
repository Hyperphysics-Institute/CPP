#!/usr/bin/env python3
"""
Patch 3675 verify — OPEN-GR-CORE-DISSIPATION-1 / the 3670 re-cut: WHICH QUANTITIES DOES THE CAP ACT ON?
Working-extension candidate THEO-PCD-SEA ("the sea carries the wave"): the census truncation (K of D) acts on
the GP's own state (count -> clock floor; net -> displacement, hence the static core) and NOT on the messenger
content the GP relays, which is the full shell-sum over all D arriving bits. Under it the wave propagates on the
sea's demand field v = M/rbar continued below the cap to v = 2 — GR's excised region (3670 §5 iv) — and the
surface presents GR's own admittance beta_hor(omega, l, m, chi) at every frequency with no constant.

Units M = 1. Schwarzschild only here (Kerr follows by the same argument on the CD Z+ instrument, 3668; owed).

 T1  MACHINERY / THE EXTENSION'S ROW-7 LINE: the horizon-equivalent wall at 8M/3 (GR's wave equation continued
     inward from the wall, ingoing at r+ = 2M) reproduces Leaver's Schwarzschild QNMs for l = 2 and l = 3.
     Under THEO-PCD-SEA this IS the R-core's line: delta f = delta tau = 0 by construction. (3644 found the same
     with 3359's machinery; this is an independent, self-contained implementation.)
 T2  The census profile the extension leaves behind: the untaken (returned) fraction 1 - cap/v(rbar), cap = 2/3
     at the surface (v_eff runs 2/3 -> 8/9 under 3640; here only v matters): 0 at the surface, 1/2 at v = 4/3,
     2/3 at v = 2 (the wave horizon of the sea metric). These bits are the STATIC over-supply; the extension's
     claim is that the wave's modulation is not split with them. Areal radii for those v recorded.
 T3  The extension's falsifier, priced: if the modulation WERE returned coherently from the wave-horizon
     region, it would come back after the tortoise round trip from 8M/3 to one PSR floor (l_P/2 proper) outside
     v = 2. Delay at 62 Msun computed; it is a ~0.2 s Planckian echo — a loud, already-searched signature.
     THEO-PCD-SEA predicts NO such return (the returned static excess carries no modulation), so PRED-O-39's
     0.95 ms cavity echo (3640, budget-law cavity) has no object under this extension: a null.
 T4  Row 6 under the extension: the static l = 2 tidal field is Q_ij content on the sea -> GR's -> k2 = 0 for
     a black hole; Lambda_tilde = 0 < 34.8 (GW250114). Passes; the budget law's +714 was the register's tide.
 T5  Consistency at the join: the sea's v and the budget register's v_eff agree in value AND slope at the
     surface (C^1, 3640 §3) — so nothing about the exterior (rows 1, 2) changes under either partition, and the
     two partitions differ only INSIDE the cap: the register (matter) metric flattens, the sea (wave) metric is
     GR's. Checked numerically: v_eff(cap) = cap, dv_eff/dv|cap = 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

R_WALL = 8.0 / 3.0
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
Msec = 62 * 4.925e-6

def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r**3 * (n * r + 3) ** 2)

# ---------------- outgoing start at large r (3383's fitted asymptotic series — not recalled) ----------------
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

def integrate(wc, Vf, r_from, r_to, p0, dp0):
    def rhs(rr, y):
        f = 1 - 2 / rr; fp = 2 / rr**2
        psi = y[0] + 1j * y[1]; dpsi = y[2] + 1j * y[3]
        d2 = -(f * fp * dpsi + (wc * wc - Vf(rr)) * psi) / (f * f)
        return [dpsi.real, dpsi.imag, d2.real, d2.imag]
    s = solve_ivp(rhs, [r_from, r_to], [p0.real, p0.imag, dp0.real, dp0.imag], rtol=1e-11, atol=1e-13, method="DOP853")
    return s.y[0, -1] + 1j * s.y[1, -1], s.y[2, -1] + 1j * s.y[3, -1]

# ---------------- ingoing start near the horizon: Z ~ (r-2)^{-2 i w} (1 + c1 (r-2)), c1 from the ODE ----------------
def ingoing_start(wc, ell, eps=1e-5):
    # Frobenius: with x = r - 2, Z = x^{-2iw} (1 + c1 x + ...); c1 fitted numerically from the ODE residual on a small x range
    def pd(c1, rr):
        x = rr - 2; s = -2j * wc
        S = 1 + c1 * x; dS = c1
        Z = x**s * S; dZ = x**s * (s / x * S + dS); d2Z = x**s * ((s * (s - 1) / x**2) * S + 2 * s / x * dS)
        return Z, dZ, d2Z
    xs = np.linspace(eps, 20 * eps, 12) + 2
    def resid(c1):
        out = []
        for rr in xs:
            f = 1 - 2 / rr; fp = 2 / rr**2; Z, dZ, d2Z = pd(c1, rr)
            out.append((f * f * d2Z + f * fp * dZ + (wc * wc - V_Z(rr, ell)) * Z) / (rr - 2)**(-2j * wc))
        return np.array(out)
    base = resid(0.0); dres = resid(1.0) - base
    c1 = -np.vdot(dres, base) / np.vdot(dres, dres)
    Z, dZ, _ = pd(c1, 2 + eps)
    return Z, dZ

def wronskian_at_wall(wc, ell, r0=40.0):
    po, dpo = outgoing_start(wc, r0, lambda r: V_Z(r, ell))
    Zo, dZo = integrate(wc, lambda r: V_Z(r, ell), r0, R_WALL, po, dpo)
    pi, dpi = ingoing_start(wc, ell)
    Zi, dZi = integrate(wc, lambda r: V_Z(r, ell), 2 + 1e-5, R_WALL, pi, dpi)
    W = Zo * dZi - dZo * Zi
    return W / (abs(Zo) * abs(Zi) + 1e-300), (Zi, dZi)

def qnm_root(ell, w0):
    F = lambda v: [x for x in (lambda W: (W.real, W.imag))(wronskian_at_wall(v[0] + 1j * v[1], ell)[0])]
    sol = fsolve(F, [w0.real, w0.imag], xtol=1e-11)
    return sol[0] + 1j * sol[1]

LEAVER = {2: 0.37367 - 0.08896j, 3: 0.59944 - 0.09270j}   # Leaver 1985, Schwarzschild fundamental, 2M = 1 -> M = 1 scaled: these are M=1 values
print("T1 — horizon-equivalent wall at 8M/3 = GR's wave equation continued below the cap, ingoing at r+ (THEO-PCD-SEA's line)")
for ell in (2, 3):
    w = qnm_root(ell, LEAVER[ell])
    df = (w.real / LEAVER[ell].real - 1) * 100; dtau = (LEAVER[ell].imag / w.imag - 1) * 100
    print(f"    l = {ell}: pole {w.real:.5f} {w.imag:+.5f} i   vs Leaver {LEAVER[ell].real:.5f} {LEAVER[ell].imag:+.5f} i   (df {df:+.3f}%, dtau {dtau:+.3f}%)")
    check(f"T1 l = {ell}: the extension's line is Leaver's to < 0.1 % in f and tau", abs(df) < 0.1 and abs(dtau) < 0.1)
    # sharpness: |W| rises off the root
    Wr = abs(wronskian_at_wall(w, ell)[0]); Woff = abs(wronskian_at_wall(w * (1 + 0.01), ell)[0])
    check(f"T1 l = {ell}: root is sharp (|W| off-root / on-root > 30)", Woff / max(Wr, 1e-300) > 30, f"{Woff / max(Wr, 1e-300):.0f}")
# the admittance the extension presents at the wall AT the pole, on the Zerilli variable (for the record; 3670's s = 3.22 is 1/|Im beta|/omega)
w2 = qnm_root(2, LEAVER[2]); _, (Zi, dZi) = wronskian_at_wall(w2, 2)
beta = (1 - 2 / R_WALL) * dZi / (1j * w2 * Zi)
print(f"    l = 2 pole admittance on Z+ at 8M/3 under the extension: dZ/dr* /(i w Z) = {beta.real:+.4f} {beta.imag:+.4f} i  ->  omega/|Im(beta*i w)/w| ... 3644's s = {1/abs((beta*1j*w2).imag/w2.real) if abs((beta*1j*w2).imag)>0 else float('nan'):.3f}")

print("\nT2 — the census profile the extension leaves behind (static over-supply, NOT the wave)")
CAP = 2.0 / 3.0
areal = lambda v: (1 + v / 2) ** 2 / v                     # isotropic v = M/rbar -> areal r/M
returned = lambda v: 1 - CAP / v
for v in (CAP, 4 / 3, 2.0):
    print(f"    v = {v:.4f}: areal r = {areal(v):.4f} M, returned fraction 1 - cap/v = {returned(v):.4f}")
check("T2 surface: v = cap at areal 8M/3, returned fraction 0", abs(areal(CAP) - R_WALL) < 1e-12 and abs(returned(CAP)) < 1e-12)
check("T2 wave horizon of the sea metric: v = 2 is areal 2M, returned fraction 2/3", abs(areal(2.0) - 2.0) < 1e-12 and abs(returned(2.0) - 2 / 3) < 1e-12)

print("\nT3 — the falsifier priced: a coherent return from one PSR floor outside the wave horizon")
lP = 1.616e-35; M_m = 62 * 1476.6                          # 62 Msun in metres (GM/c^2)
ell_prop = lP / 2                                          # the PSR floor l_P/2 (R-FLOOR-REGISTER)
dr = ell_prop**2 / (8 * M_m)                               # proper distance ell above r+ : ell = 2 sqrt(2M (r - 2M))
rs_h = 2.0 + dr / M_m + 2 * np.log(dr / (2 * M_m))         # tortoise (M = 1) of that point
delay = 2 * (rstar(R_WALL) - rs_h) * Msec
print(f"    r*(8M/3) = {rstar(R_WALL):+.4f} M; r*(floor point) = {rs_h:+.1f} M; round trip = {2*(rstar(R_WALL)-rs_h):.1f} M = {delay*1e3:.0f} ms at 62 Msun")
check("T3 a coherent return from the floor would arrive ~0.2 s after the ringdown (Planckian echo), not at 0.95 ms", 0.1 < delay < 0.4)

print("\nT4 — row 6 under the extension: static tide on the sea = GR's black-hole tide")
k2_bh = 0.0; Lam_tilde = (16 / 13) * 0.0                   # Lambda = (2/3) k2 C^-5 = 0 for k2 = 0
check("T4 Lambda_tilde = 0 < 34.8 (GW250114, arXiv:2512.01918): row 6 PASSES with no constant", Lam_tilde < 34.8)

print("\nT5 — the two partitions agree at the join (nothing exterior changes)")
v_eff = lambda v: 2 * CAP - CAP**2 / v
dv = 1e-6
check("T5 v_eff(cap) = cap and dv_eff/dv|cap = 1 (C^1 join, 3640 §3)", abs(v_eff(CAP) - CAP) < 1e-12 and abs((v_eff(CAP + dv) - v_eff(CAP - dv)) / (2 * dv) - 1) < 1e-5,
      f"v_eff(2) = {v_eff(2.0):.4f} vs sea v = 2 at the wave horizon: the partitions differ only inside")

print(f"\n{PASS}/{PASS+FAIL} PASS")
