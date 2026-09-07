#!/usr/bin/env python3
"""
Patch 3657 verify — KERRWALL-1: the Sasaki-Nakamura <-> local-wave dictionary at the Kerr wall, and the Kerr test
of H-SURFACE-IMPEDANCE with s UNCHANGED (rule 6, member 5). Run from the repo root (exec's 3359's SN machinery
and 3644's a = 0 Zerilli machinery the way 3619/3644/3646 do).

THE DICTIONARY (derived, not fitted). The SN equation is  X'' - F X' - U X = 0  (' = d/dr*). The first-derivative
term is why X is not locally plane-wave at the wall and why a pure-imaginary law on X is not a local absorber
(3644 §3). Because  F dr* = (eta'/eta) dr  EXACTLY (F = eta' Delta / (eta (r^2+a^2)), dr*/dr = (r^2+a^2)/Delta), the
substitution  Y = X / sqrt(eta)  removes it:  Y'' = W Y,  W = U + F^2/4 + F'/2.  Y is the local wave; the wall law
transports as  beta_X = beta_Y + F(r_w)/2.  At a = 0, eta = c0 = const, F = 0, Y = X = Regge-Wheeler: the dictionary
is the identity. eta, F are 3359's own (validated: T1 a = 0 reduction, T3 wall mode, 3619 Kerr QNM to 0.7%/1.3%).

TESTS
 (1) a = 0 on the SN/RW function: the horizon-equivalent law at 8M/3 at omega_QNM (l = 2) — is it nearly pure
     imaginary as on Zerilli (+0.008 - 0.116i, 3644)? The hypothesis was pinned on Zerilli; the odd master function
     is the a = 0 member of the SN family, so the hypothesis must be checked there before any Kerr number.
 (2) a = 0: H-SURFACE-IMPEDANCE on RW, s = 3.218 unchanged: the l = 2 line vs the box.
 (3) Kerr a = 0.68, wall 2.734 M, (2,2): the dictionary term F(r_w)/2 at real omega ~ omega_QNM; the horizon law on X
     (3619/3644: Re +0.063) and on Y (= beta_X - F/2). Does the dictionary remove the real part?
 (4) The Kerr test: beta_X = F/2 - i (omega - m Omega)/s, s = 3.218 UNCHANGED, Omega in {Omega_w (the surface's own
     frame-dragging rate — the surface's frame, the a = 0 reading carried unchanged), Omega_H, 0}. Score against the
     machinery's own horizon-equivalent pole (same code, same wall) and against the literature Kerr line; GW150914 box.
 (5) The pin re-read at Kerr: s_Kerr = (omega - m Omega)/|Im beta_Y,hor| — is s universal, or does the horizon's
     admittance in the local-wave variable move with spin?
"""
import io, contextlib, numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
BOX = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4
S_PIN = 3.218                                                      # 3644, a = 0 l = 2 Zerilli horizon point; UNCHANGED

# ---------------------------------------------------------------- 3359's SN machinery (silenced), 3619's wall solver
src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src.split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = src.split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)

def lam_of(w, a, ell, m):
    A = A_leaver(a * w, ell, m) if a != 0.0 else (ell * (ell + 1) - 2 + 0j)
    return A + a * a * w * w - 2 * a * m * w

def eta_of(r, a, w, m, lam, M=1.0):
    c0 = -12j * w * M + lam * (lam + 2) - 12 * a * w * (a * w - m)
    c1 = 8j * a * (3 * a * w - lam * (a * w - m))
    c2 = -24j * a * M * (a * w - m) + 12 * a * a * (1 - 2 * (a * w - m) ** 2)
    c3 = 24j * a ** 3 * (a * w - m) - 24 * M * a * a
    c4 = 12 * a ** 4
    return c0 + c1 / r + c2 / r ** 2 + c3 / r ** 3 + c4 / r ** 4

def F_wall(w, a, ell, m, rw):
    lam = lam_of(w, a, ell, m); return sn_FU(rw, a, w, m, lam)[0]

def beta_hor_X(w, a, ell, m, rw):
    """horizon-equivalent law on the SN function X at r_w: log-derivative (r*) of the solution ingoing at the horizon."""
    lam = lam_of(w, a, ell, m)
    rp = 1 + np.sqrt(1 - a * a); OmH = a / (2 * rp) if a != 0 else 0.0; k = w - m * OmH
    r_start = rp + 1e-3
    X0 = np.exp(-1j * k * rstar(r_start, a)); Xp0 = -1j * k * X0
    def rhs(t, y):
        r = y[4]; D = r * r - 2 * r + a * a
        F, U = sn_FU(r, a, w, m, lam)
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]; Xpp = F * Xp + U * X
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, D / (r * r + a * a)]
    sol = solve_ivp(rhs, [rstar(r_start, a), rstar(rw, a)], [X0.real, X0.imag, Xp0.real, Xp0.imag, r_start], rtol=1e-11, atol=1e-13, method="DOP853")
    X = sol.y[0, -1] + 1j * sol.y[1, -1]; Xp = sol.y[2, -1] + 1j * sol.y[3, -1]
    return Xp / X

def root_X(beta_fn, a, ell, m, rw, guess):
    def Fk(w):
        X, Xp = X_at_wall(w, a, ell, m, 40.0, rw=rw); b = beta_fn(w); return (Xp - b * X) / (1 + abs(b))
    fn = lambda v: [Fk(v[0] + 1j * v[1]).real, Fk(v[0] + 1j * v[1]).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]

# ---------------------------------------------------------------- (0) the dictionary is an identity: F dr* = d ln eta
print("(0) the dictionary: Y = X/sqrt(eta) turns X'' - F X' - U X = 0 into Y'' = W Y, because F dr* = (eta'/eta) dr exactly")
A68 = 0.68; RW68 = 2.7344
wprobe = 0.528 - 0.082j; lam_p = lam_of(wprobe, A68, 2, 2)
devs = []
for r in (2.734, 3.0, 4.0, 8.0):
    F = sn_FU(r, A68, wprobe, 2, lam_p)[0]
    h = 1e-6; D = r * r - 2 * r + A68 * A68
    dlneta_dr = (np.log(eta_of(r + h, A68, wprobe, 2, lam_p)) - np.log(eta_of(r - h, A68, wprobe, 2, lam_p))) / (2 * h)
    devs.append(abs(F - dlneta_dr * D / (r * r + A68 * A68)))
check("(0) F = (d ln eta / dr) (dr/dr*) pointwise at Kerr (2,2): the SN first-derivative term is a pure gauge factor sqrt(eta) on X; the local wave is Y = X/sqrt(eta) and any wall law transports as beta_X = beta_Y + F/2", max(devs) < 1e-7, f"max |F - d ln eta/dr*| = {max(devs):.1e}")

# ---------------------------------------------------------------- (1) a = 0: the horizon law on the SN/RW function
print("(1) a = 0, l = 2, wall 8M/3, on the SN (= Regge-Wheeler) function")
wGR = 0.37367 - 0.08896j; R0 = 8.0 / 3.0
dev0 = lambda w: (100 * (w.real / wGR.real - 1), 100 * (abs(wGR.imag) / abs(w.imag) - 1))
bhRW = beta_hor_X(wGR.real, 0.0, 2, -2, R0)
bhRWc = beta_hor_X(wGR, 0.0, 2, -2, R0)
w_hRW = root_X(lambda w: beta_hor_X(w, 0.0, 2, -2, R0), 0.0, 2, -2, R0, 0.37 - 0.09j)
print(f"    horizon-equivalent wall on RW: pole {w_hRW.real:.5f} {w_hRW.imag:+.5f}i (GR {wGR.real:.5f} {wGR.imag:+.5f}i; dev {dev0(w_hRW)[0]:+.2f}% / {dev0(w_hRW)[1]:+.2f}%)")
print(f"    beta_hor,RW(Re omega_QNM) = {bhRW.real:+.4f} {bhRW.imag:+.4f}i   [Zerilli, 3644: +0.008 -0.116i];  at complex omega_QNM: {bhRWc.real:+.4f} {bhRWc.imag:+.4f}i")
s_RW = wGR.real / abs(bhRW.imag)
print(f"    the a = 0 pin re-read on RW: s_RW = omega/|Im beta_hor,RW| = {s_RW:.3f}  (Zerilli pin 3.218)")
check("(1a) machinery: the horizon-equivalent wall on the SN/RW function at 8M/3 reproduces the Schwarzschild l = 2 QNM to < 0.5% / 2%", abs(dev0(w_hRW)[0]) < 0.5 and abs(dev0(w_hRW)[1]) < 2)
check("(1b) at a = 0 the horizon law on the ODD master function is NOT the near-pure-imaginary law it is on Zerilli: |Re beta_hor,RW| exceeds Zerilli's +0.008 several-fold — the variable matters already at a = 0 (Chandrasekhar's map between the parities is a differential relation, so a local law on one is non-local on the other)",
      abs(bhRW.real) > 0.03, f"Re beta_hor,RW = {bhRW.real:+.4f} vs Zerilli +0.008")

# ---------------------------------------------------------------- (2) a = 0: the hypothesis on RW, s unchanged
wD_RW = root_X(lambda w: -1j * w / S_PIN, 0.0, 2, -2, R0, 0.37 - 0.09j); d = dev0(wD_RW)
print(f"(2) H-SURFACE-IMPEDANCE on RW at a = 0, s = {S_PIN} unchanged: {wD_RW.real:.4f} {wD_RW.imag:+.4f}i  df {d[0]:+.1f}%  dtau {d[1]:+.1f}%  {'IN box' if BOX(d) else 'out'}")
wD_RW2 = root_X(lambda w: -1j * w / s_RW, 0.0, 2, -2, R0, 0.37 - 0.09j); d2 = dev0(wD_RW2)
print(f"    (for reference, the law with RW's own admittance s_RW = {s_RW:.2f}: {wD_RW2.real:.4f} {wD_RW2.imag:+.4f}i  df {d2[0]:+.1f}%  dtau {d2[1]:+.1f}%  {'IN box' if BOX(d2) else 'out'})")
hyp_on_RW_in_box = BOX(d)
check("(2) recorded either way: whether the pure-imaginary law with the Zerilli-pinned s is descriptive on the odd master function at a = 0 (if it is, the hypothesis is parity-robust; if not, the hypothesis is a statement on the EVEN variable and the Kerr test must be read with that in mind)", True, f"in box: {hyp_on_RW_in_box}")

# ---------------------------------------------------------------- (3) Kerr: the dictionary term and the horizon law on Y
print(f"(3) Kerr a = {A68}, wall {RW68} M, prograde (2,2)")
rp = 1 + np.sqrt(1 - A68 * A68); OmH = A68 / (2 * rp)
Aw = (RW68 ** 2 + A68 ** 2) ** 2 - (RW68 ** 2 - 2 * RW68 + A68 ** 2) * A68 ** 2   # equatorial A
Omw = 2 * A68 * RW68 / Aw
print(f"    Omega_H = {OmH:.4f},  Omega_w (frame dragging at the wall, equator) = {Omw:.4f}")
w_hX = root_X(lambda w: beta_hor_X(w, A68, 2, 2, RW68), A68, 2, 2, RW68, 0.52 - 0.08j)
wK = 0.528 - 0.082j
devH = lambda w: (100 * (w.real / w_hX.real - 1), 100 * (abs(w_hX.imag) / abs(w.imag) - 1))
devK = lambda w: (100 * (w.real / wK.real - 1), 100 * (abs(wK.imag) / abs(w.imag) - 1))
print(f"    horizon-equivalent pole on X: {w_hX.real:.4f} {w_hX.imag:+.4f}i  (3619: 0.5242 -0.0810i; literature ~0.528 -0.082i; dev vs lit {devK(w_hX)[0]:+.1f}% / {devK(w_hX)[1]:+.1f}%)")
wr = w_hX.real
bX = beta_hor_X(wr, A68, 2, 2, RW68); Fw = F_wall(wr, A68, 2, 2, RW68); bY = bX - Fw / 2
print(f"    at real omega = {wr:.4f}:  beta_hor,X = {bX.real:+.4f} {bX.imag:+.4f}i;   F(r_w)/2 = {Fw.real/2:+.4f} {Fw.imag/2:+.4f}i;   beta_hor,Y = beta_X - F/2 = {bY.real:+.4f} {bY.imag:+.4f}i")
check("(3a) machinery: the horizon-equivalent wall on X reproduces the Kerr (2,2) line (3619) to < 1.5% / 4%", abs(devK(w_hX)[0]) < 1.5 and abs(devK(w_hX)[1]) < 4)
check("(3b) FINDING, against the expectation the patch was built on: the dictionary term F/2 is IMAGINARY-dominated at the wall and its real part is a small fraction of the horizon law's — the SN first-derivative term is NOT where 3644's '+0.063' comes from; the real part is in the local wave itself", abs(Fw.real / 2) < abs(bX.real) / 3 and abs(Fw.imag) > abs(Fw.real), f"F/2 = {Fw.real/2:+.4f} {Fw.imag/2:+.4f}i vs Re beta_hor,X = {bX.real:+.4f}")
check("(3c) on the local wave Y the horizon law's real part is REDUCED relative to X (the dictionary moves the Kerr horizon point toward the imaginary axis, as the a = 0 Zerilli point sits)", abs(bY.real) < abs(bX.real), f"|Re| {abs(bX.real):.4f} -> {abs(bY.real):.4f}")

# ---------------------------------------------------------------- (4) the Kerr test, s unchanged
print(f"(4) THE KERR TEST — beta_X = F(r_w)/2 - i (omega - m Omega)/s, s = {S_PIN} UNCHANGED; scored vs the machinery's horizon-equivalent pole (H) and the literature line (K); GW150914 box")
laws = {
    "Omega = Omega_w (surface's own frame)": Omw,
    "Omega = Omega_H":                       OmH,
    "Omega = 0 (asymptotic omega)":         0.0,
}
res = {}
for lab, Om in laws.items():
    w = root_X(lambda w, Om=Om: F_wall(w, A68, 2, 2, RW68) / 2 - 1j * (w - 2 * Om) / S_PIN, A68, 2, 2, RW68, 0.51 - 0.09j)
    res[lab] = w; dH = devH(w); dK = devK(w)
    print(f"    {lab:36s}: {w.real:.4f} {w.imag:+.4f}i  vs H: df {dH[0]:+6.1f}% dtau {dH[1]:+6.1f}% {'IN' if BOX(dH) else 'out'};  vs K: df {dK[0]:+6.1f}% dtau {dK[1]:+6.1f}% {'IN' if BOX(dK) else 'out'}")
# the same laws WITHOUT the dictionary term (3644's form), for the record
print("    (without the dictionary term, 3644's form beta = -i(omega - m Omega)/s:)")
res0 = {}
for lab, Om in laws.items():
    w = root_X(lambda w, Om=Om: -1j * (w - 2 * Om) / S_PIN, A68, 2, 2, RW68, 0.50 - 0.10j)
    res0[lab] = w; dH = devH(w)
    print(f"      {lab:34s}: {w.real:.4f} {w.imag:+.4f}i  vs H: df {dH[0]:+6.1f}% dtau {dH[1]:+6.1f}% {'IN' if BOX(dH) else 'out'}")
primary = "Omega = Omega_w (surface's own frame)"
in_any = [lab for lab, w in res.items() if BOX(devH(w))]
check("(4a) with the dictionary term the surface-frame law (Omega_w) lands the Kerr (2,2) line inside the box with s unchanged — the hypothesis' 5th member — OR it does not and the member fails; recorded as computed", True,
      f"primary (Omega_w): df {devH(res[primary])[0]:+.1f}% / dtau {devH(res[primary])[1]:+.1f}% -> {'DESCRIPTIVE' if BOX(devH(res[primary])) else 'FAILS'}; in-box frames: {in_any}")
check("(4b) FINDING: the dictionary does NOT rescue the Kerr member — no frame is in the box, and the damping residual of the surface-frame law grows with the dictionary term (the -i F/2 part adds absorption)", len(in_any) == 0 and abs(devH(res[primary])[1]) > abs(devH(res0[primary])[1]),
      f"primary dtau: {devH(res0[primary])[1]:+.1f}% (3644 form) -> {devH(res[primary])[1]:+.1f}% (dictionaried)")
# is it the number or the form? scan s with the dictionary term, both frames
print("    s-scan with the dictionary term (is it s, or the pure-imaginary form?):")
scan_in = []
for lab, Om in (("Omega_w", Omw), ("Omega_H", OmH)):
    prev = res[primary] if lab == "Omega_w" else res["Omega = Omega_H"]
    line = f"      {lab}: "
    for sv in (1.5, 2.0, 3.218, 5.0, 8.0, 15.0, 40.0):
        w = root_X(lambda w, Om=Om, sv=sv: F_wall(w, A68, 2, 2, RW68) / 2 - 1j * (w - 2 * Om) / sv, A68, 2, 2, RW68, prev); prev = w
        dH = devH(w); line += f"s={sv:g} ({dH[0]:+.0f}%,{dH[1]:+.0f}%){' IN' if BOX(dH) else ''}  "
        if BOX(dH): scan_in.append((lab, sv))
    print(line)
check("(4c) FINDING: NO s in [1.5, 40] puts the pure-imaginary local-wave law inside the Kerr box in either frame — the failure is the FORM (a real impedance step), not the number s", len(scan_in) == 0, f"in-box (frame, s): {scan_in}")
# what the Kerr ringdown asks of the wall: the horizon's reflection seen from r_w in the local-wave variable
def refl(beta, k): return (beta + 1j * k) / (1j * k - beta)
bhZ0 = 0.008 - 0.116j; RZ0 = refl(bhZ0, wGR.real)
RY = {lab: refl(bY, wr - 2 * Om) for lab, Om in laws.items()}
print(f"    the horizon seen from the wall as a reflector of the local wave, R = (beta + ik)/(ik - beta):")
print(f"      a = 0, Zerilli (3644's point): |R| = {abs(RZ0):.3f}, phase {np.degrees(np.angle(RZ0)):+.1f} deg  (the hypothesis: |R| = {(1-1/S_PIN)/(1+1/S_PIN):.3f}, phase 0)")
for lab, R in RY.items(): print(f"      Kerr, Y, {lab:36s}: |R| = {abs(R):.3f}, phase {np.degrees(np.angle(R)):+.1f} deg")
RYw = RY[primary]
check("(4d) THE KERR REQUIREMENT (recorded like row 7's): in the surface's frame the Kerr horizon reflects the local wave with |R| > the a = 0 value AND a phase of order -15 deg — a COMPLEX impedance (a lossy spring), where the hypothesis has a real one (phase 0). This is what a Kerr member of any surface law must reproduce", abs(RYw) > abs(RZ0) and abs(np.degrees(np.angle(RYw))) > 8, f"|R| {abs(RZ0):.2f} -> {abs(RYw):.2f}, phase {np.degrees(np.angle(RZ0)):+.0f} -> {np.degrees(np.angle(RYw)):+.0f} deg")

# ---------------------------------------------------------------- (2b) parity robustness of the group at a = 0: l = 3 on RW
wGR3 = 0.59944 - 0.09270j
dev3 = lambda w: (100 * (w.real / wGR3.real - 1), 100 * (abs(wGR3.imag) / abs(w.imag) - 1))
wD3 = root_X(lambda w: -1j * w / S_PIN, 0.0, 3, -3, R0, 0.60 - 0.09j); d3 = dev3(wD3)
print(f"(2b) H-SURFACE-IMPEDANCE on RW at a = 0, l = 3, s unchanged: {wD3.real:.4f} {wD3.imag:+.4f}i  df {d3[0]:+.1f}%  dtau {d3[1]:+.1f}%  {'IN box' if BOX(d3) else 'out'}  (Zerilli, 3644: -1.4% / -1.3%)")
check("(2b) the a = 0 group is parity-robust in the box: l = 2 and l = 3 on the odd master function, s unchanged, both inside (with larger damping residuals than on Zerilli)", BOX(d) and BOX(d3), f"l=2 {d[1]:+.1f}%, l=3 {d3[1]:+.1f}% in dtau")

# ---------------------------------------------------------------- (5) the pin re-read at Kerr
print("(5) the pin re-read at Kerr in the local-wave variable: s_Kerr = (omega - m Omega)/|Im beta_hor,Y|")
for lab, Om in laws.items():
    print(f"    {lab:36s}: s_Kerr = {(wr - 2*Om)/abs(bY.imag):.3f}")
sK = (wr - 2 * Omw) / abs(bY.imag)
check("(5) recorded: the horizon's admittance in the local-wave variable at the surface's frame gives s_Kerr; its distance from the a = 0 pin 3.218 is the spin-dependence of the impedance reading (a universal s would give ~3.2)", True, f"s_Kerr(Omega_w) = {sK:.3f} vs 3.218 ({100*(sK/3.218-1):+.0f}%)")

print(); print(f"3657 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
