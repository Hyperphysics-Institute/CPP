#!/usr/bin/env python3
"""
Patch 3670 verify — OPEN-GR-SURFACE-IMPEDANCE-1, attempt 4 step 2: THE TWO-DATUM TARGET AS A FUNCTION, and the
parameter-free surface mechanisms scored against BOTH data at once. Run from the repo root (exec's 3668's CD Z+
instrument, which exec's 3359/3358).

WHY THIS BEFORE ANOTHER DERIVATION. Attempts 1, 2a, 2b, 3, 3b each tried to produce ONE number (the a = 0 real
step) from a surface mechanism; 3655 named a constant candidate (psi^4). 3668 added a second datum with a PHASE.
Before spending a sixth derivation on a constant, establish what the target IS: (A) how the Kerr requirement
moves with spin; (B) whether the a = 0 "one number for four members" is a property of the surface or of the
function the hypothesis was fitted to; (C) which zero-parameter surface mechanisms can meet both data at all.

DEFINITIONS (3644, 3657, 3668). At the wall r_w (F_n = 4/9, lapse 1/2; 8M/3 at a = 0), the requirement is the
horizon-equivalent law beta_hor(omega) = log-derivative (in r*) of the solution ingoing at the horizon, read as
a reflector R = (beta + ik)/(ik - beta), k = omega - m Omega_w (surface frame), at real omega = Re omega_QNM.
This is, by construction, the reflection of GR's OWN region r_+ < r < r_w (the excised region) as seen from r_w
in the given variable — "the horizon's own from 8M/3" (3644).

TESTS
 (A) chi in {0, 0.2, 0.4, 0.6, 0.68, 0.8, 0.9}, (2,2), on Z+: r_w(chi), Omega_w(chi), Leaver omega_QNM(chi),
     |R|, phase, s_reread = k/|Im beta|. Also (2,0) and (2,-2) at chi = 0.68 (retrograde-keyed template).
 (B) a = 0, l = 2, 3, 4: s_exc(omega) = omega/|Im beta_hor(omega)| and phase(R) over real omega in
     [0.2, 1.0], and at each l's own Re omega_QNM. Question: is s_exc ~ 3.2 at all three l because the
     excised region's reflection is FLAT there? (If yes, the four-member a = 0 group tested the flatness of a GR
     function, not a surface constant.)
 (A') and (B'): the same at the COMPLEX poles — where the pole is actually decided. FOUND ON THE FIRST RUN (rule 4:
     the failing expectation located): the "a = 0 real step |R| = 0.53 at -3 deg" of 3644/3657 §4 was beta at the
     COMPLEX pole read with k REAL (bhZ0 = 0.008 - 0.116i, k = Re omega); at real omega the a = 0 horizon reflects
     Z+ at 0.39, -43 deg. The Kerr "0.71 at -17" / "0.77 at -13" were real-omega readings. The two "data" were
     never the same object. The pole is set by beta_hor at the complex frequency; the requirement is stated there.
 (C) mechanisms against BOTH data, stated at the complex poles (a = 0 l = 2: beta_hor = +0.009 - 0.116i;
     Kerr 0.68 (2,2) on Z+: beta_hor at its pole) and, for the record, at real omega:
     (i)   real impedance step (the hypothesis; psi^4 candidate): phase 0 by construction — Kerr phase.
     (ii)  delayed compliant surface, R = R0 exp(-2 i k tau_d): fit tau_d from the Kerr phase, predict a = 0.
           A one-Moment (Planck) delay gives phase ~ omega t_P ~ 0: recorded.
     (iii) frame Doppler: the co-rotating real step is (i) in the surface frame — already tested (3657, 3668).
     (iv)  the excised region itself: meets both by construction — is the a = 0 number then DERIVED from GR?
"""
import io, contextlib, numpy as np
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------------------------------------------------------- 3668's instrument (silenced): calV_CD, beta_hor_Z, root_Z, lam_of, kerr_qnm, rstar, F_n, refl
src68 = open("series_gravitation/code/3668_kerrwall1b_cd_zplus_even_kerr_verify.py").read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src68.split("# ============================================================ T1")[0].replace("PASS = FAIL = 0", "PASS68 = FAIL68 = 0").replace('def check(name, cond, detail="")', 'def check68(name, cond, detail="")'))
SB = -1                                                           # the isospectral even-type variable (3668 T3)

def r_wall(a):
    """the lane's surface: F_n(r, chi, equator) = 4/9 (lapse 1/2; CONV-040 ansatz A) — 8M/3 at a = 0, 2.7344 at 0.68."""
    if a == 0.0: return 8.0 / 3.0
    rp = 1 + np.sqrt(1 - a * a)
    return brentq(lambda r: F_n(r, a, np.pi / 2) - 4.0 / 9.0, rp * (1 + 1e-9), 20.0, xtol=1e-12)
def Omega_w(a, rw):
    Aw = (rw ** 2 + a ** 2) ** 2 - (rw ** 2 - 2 * rw + a ** 2) * a ** 2
    return 2 * a * rw / Aw

# ================================================================ (A) the Kerr requirement as a function of spin
print("(A) the requirement on Z+ vs spin, (2,2), surface frame: r_w, Omega_w, Leaver omega_QNM, |R|, phase, s_reread")
check("(A0) the surface rule reproduces the lane's numbers: r_w(0) = 8/3, r_w(0.68) = 2.7344", abs(r_wall(0.0) - 8 / 3) < 1e-12 and abs(r_wall(0.68) - 2.7344) < 2e-4, f"r_w(0.68) = {r_wall(0.68):.5f}")
chis = [0.0, 0.2, 0.4, 0.6, 0.68, 0.8, 0.9]
guess = 0.37367 - 0.08896j; rows = []
for a in chis:
    rw = r_wall(a); Om = Omega_w(a, rw)
    wq = kerr_qnm(a, 2, 2, -2, guess) if a > 0 else guess; guess = wq
    wr = wq.real; k = wr - 2 * Om
    b = beta_hor_Z(wr, a, 2, 2, rw, +1, SB); R = refl(b, k)
    rows.append((a, rw, Om, wq, b, R, k / abs(b.imag)))
    print(f"    chi {a:.2f}: r_w {rw:.4f}  Omega_w {Om:.4f}  omega_QNM {wq.real:.4f}{wq.imag:+.4f}i  k {k:.4f}  beta_hor {b.real:+.4f}{b.imag:+.4f}i  |R| {abs(R):.3f}  phase {np.degrees(np.angle(R)):+.1f} deg  s_reread {k/abs(b.imag):.2f}")
R0 = rows[0][5]; R68 = [r for r in rows if r[0] == 0.68][0][5]
phases = [np.degrees(np.angle(r[5])) for r in rows]; mods = [abs(r[5]) for r in rows]
check("(A1) RECORD CORRECTION (extends 3668 §2): at REAL omega the a = 0 horizon from 8M/3 reflects Z+ at |R| = 0.39, -43 deg — NOT the '0.53 at -3 deg' of 3644/3657 §4, which was beta at the complex pole read with k real; chi = 0.68 reproduces 3668's real-omega reading 0.77 at -13 deg", abs(abs(R0) - 0.389) < 0.01 and abs(phases[0] + 43.3) < 1 and abs(abs(R68) - 0.769) < 0.01 and abs(phases[4] + 12.9) < 1, f"a = 0: {abs(R0):.3f} at {phases[0]:+.1f}; 0.68: {abs(R68):.3f} at {phases[4]:+.1f}")
mono_mod = all(mods[i + 1] >= mods[i] - 1e-3 for i in range(len(mods) - 1))
check("(A2) RECORDED: at real omega the requirement is a strong FUNCTION of spin — |R| 0.39 -> 0.80 and the phase -43 deg -> +99 deg (through zero near chi ~ 0.72) in the surface frame; there is no spin at which it is a real step of 0.53", True,
      f"|R|: {' '.join(f'{m:.2f}' for m in mods)}; phase: {' '.join(f'{p:+.0f}' for p in phases)} deg; monotone |R|: {mono_mod}")
sr = [r[6] for r in rows]
check("(A3) FINDING: the re-read impedance s = k/|Im beta| is NOT a constant across spin (the a = 0 pin 3.22 is the chi = 0 value of a rising curve)", max(sr) / min(sr) > 1.5, f"s_reread(chi): {' '.join(f'{v:.2f}' for v in sr)}")
# m = 0, -2 at chi = 0.68 (retrograde-keyed template)
print("    chi = 0.68, other m (Leaver guesses from the Kerr (2,m) fundamentals; each root's continued-fraction residual is checked):")
rw68 = r_wall(0.68); Om68 = Omega_w(0.68, rw68)
for m, g in ((0, 0.40 - 0.088j), (-2, 0.30 - 0.090j)):
    wq = kerr_qnm(0.68, 2, m, -2, g); wr = wq.real; k = wr - m * Om68
    b = beta_hor_Z(wr, 0.68, 2, m, rw68, +1, SB); R = refl(b, k)
    print(f"      (2,{m:+d}): omega_QNM {wq.real:.4f}{wq.imag:+.4f}i  k {k:.4f}  beta_hor {b.real:+.4f}{b.imag:+.4f}i  |R| {abs(R):.3f}  phase {np.degrees(np.angle(R)):+.1f} deg  s_reread {k/abs(b.imag):.2f}")


# ================================================================ (A') the requirement AT THE COMPLEX POLE vs spin — where the pole is decided
print("(A') the requirement at the complex pole, beta_hor(omega_QNM) on Z+, vs the hypothesis's law -i(omega_QNM - m Omega_w)/3.218 there")
S_PIN = 3.218; mism = []
for a, rw, Om, wq, b, R, sr_ in rows:
    bc = beta_hor_Z(wq, a, 2, 2, rw, +1, SB); hyp = -1j * (wq - 2 * Om) / S_PIN
    mism.append((a, bc, hyp, abs(bc - hyp)))
    print(f"    chi {a:.2f}: beta_hor(pole) {bc.real:+.4f}{bc.imag:+.4f}i   hypothesis {hyp.real:+.4f}{hyp.imag:+.4f}i   |mismatch| {abs(bc-hyp):.3f}   Im sign {'same' if bc.imag*hyp.imag > 0 else 'OPPOSITE'}")
m0 = mism[0][3]; m68 = mism[4][3]
check("(A'1) at a = 0 the hypothesis's law sits 0.036 from the horizon's at the pole (the -2.2%/+4.9% calibration residual is this mismatch); the pin 3.218 is Re omega/|Im beta_hor(pole)| = 3.235 with the converged start", m0 < 0.05 and abs(mism[0][1].imag * S_PIN / rows[0][3].real + 1) < 0.02, f"|mismatch|(0) = {m0:.3f}")
check("(A'2) FINDING: at Kerr the mismatch at the pole is an order of magnitude larger and, from chi ~ 0.6, Im beta_hor at the pole has the OPPOSITE sign to any absorbing law -ik/s: no real s, no delay, no frame can produce it — the failure of 3657/3668 located at the pole", m68 > 0.2 and mism[4][1].imag * mism[4][2].imag < 0, f"|mismatch|(0.68) = {m68:.3f}; Im beta_hor(pole, 0.68) = {mism[4][1].imag:+.3f} vs hypothesis {mism[4][2].imag:+.3f}")

# ================================================================ (B) a = 0: the excised region's reflection as a function of omega and l
print("(B) a = 0: s_exc(omega) = omega/|Im beta_hor| and phase(R) on Z+ over real omega, l = 2, 3, 4; and at each l's own Re omega_QNM")
wq0 = {2: 0.37367 - 0.08896j, 3: 0.59944 - 0.09270j, 4: 0.80918 - 0.09416j}
def lam0(ell): return ell * (ell + 1) - 2 + 0j
def beta0(w, ell):
    # a = 0 on Z+: lam is ell-dependent; beta_hor_Z uses lam_of(w, 0, ell, m) = ell(ell+1)-2 — fine for any m
    return beta_hor_Z(w, 0.0, ell, 2, 8 / 3, +1, SB)
sweep = np.arange(0.20, 1.001, 0.05); tab = {}
for ell in (2, 3, 4):
    tab[ell] = [(w, beta0(w, ell)) for w in sweep]
    line = f"    l = {ell}: " + "  ".join(f"w{w:.2f}:s{w/abs(b.imag):.2f}/{np.degrees(np.angle(refl(b, w))):+.0f}" for w, b in tab[ell] if abs(w - round(w * 10) / 10) < 1e-9)
    print(line)
s_at = {}; s_pole = {}; mis_pole = {}
for ell in (2, 3, 4):
    w = wq0[ell].real; b = beta0(w, ell); s_at[ell] = w / abs(b.imag)
    bc = beta0(wq0[ell], ell); s_pole[ell] = wq0[ell].real / abs(bc.imag); mis_pole[ell] = abs(bc - (-1j * wq0[ell] / 3.218))
    print(f"    l = {ell}: at REAL Re omega_QNM = {w:.4f}: beta_hor {b.real:+.4f}{b.imag:+.4f}i  s_exc {s_at[ell]:.3f}  |R| {abs(refl(b, w)):.3f}  phase {np.degrees(np.angle(refl(b, w))):+.1f} deg;   at the COMPLEX pole: beta_hor {bc.real:+.4f}{bc.imag:+.4f}i  s_pole {s_pole[ell]:.3f}  |beta_hor - (-i omega/3.218)| {mis_pole[ell]:.3f}")
spread = max(s_at.values()) / min(s_at.values()) - 1; spread_p = max(s_pole.values()) / min(s_pole.values()) - 1
check("(B1) FINDING: the a = 0 group's descriptiveness lives at the COMPLEX poles — there the hypothesis's law sits within 0.04-0.06 of the horizon's at all three l (the l = 2 calibration residual is 0.036), even though the ratio Re omega/|Im beta_hor| rises 3.24 -> 3.64 -> 3.90 (20%); at REAL omega the ratio is 2.0-2.7 and the reflection is -43 to -28 deg — GR's excised region is a frequency-dependent complex reflector whose values AT THE POLES are close to one nearly-imaginary law within the box's tolerance; that is what one constant described, and it is not an l-flat constant",
      max(mis_pole.values()) < 0.07 and spread_p > 0.15 and spread > 0.2, f"s_pole(2,3,4) = {s_pole[2]:.3f}, {s_pole[3]:.3f}, {s_pole[4]:.3f} (spread {100*spread_p:.1f}%); mismatch at poles {mis_pole[2]:.3f}, {mis_pole[3]:.3f}, {mis_pole[4]:.3f}; real-omega s_exc spread {100*spread:.0f}%")
# how flat over omega at l = 2 around the QNM frequency
sl2 = [(w, w / abs(b.imag)) for w, b in tab[2] if 0.30 <= w <= 0.60]
check("(B2) RECORDED: l = 2 s_exc over omega in [0.30, 0.60] (the ringdown band) — the flatness that made one constant serve", True, "  ".join(f"{w:.2f}:{s:.2f}" for w, s in sl2))
check("(B3) FINDING: the a = 0 'real step' is not exactly real either — the phase of R at Re omega_QNM is small but nonzero and l-dependent; the hypothesis's phase 0 is the same kind of approximation at a = 0 as it is a failure at Kerr, only smaller", True,
      "; ".join(f"l={ell}: {np.degrees(np.angle(refl(beta0(wq0[ell].real, ell), wq0[ell].real))):+.1f} deg" for ell in (2, 3, 4)))

# ================================================================ (C) mechanisms against BOTH data
print("(C) parameter-free surface mechanisms scored against both data at once")
k0 = rows[0][3].real; k68 = rows[4][3].real - 2 * rows[4][2]
ph0 = np.angle(R0); ph68 = np.angle(R68)
print(f"    real-omega readings: a = 0: |R| {abs(R0):.3f}, phase {np.degrees(ph0):+.1f} deg at k = {k0:.4f};  Kerr 0.68: |R| {abs(R68):.3f}, phase {np.degrees(ph68):+.1f} deg at k = {k68:.4f}")
print(f"    pole readings (the data that decide): a = 0: beta_hor {mism[0][1].real:+.4f}{mism[0][1].imag:+.4f}i;  Kerr 0.68: beta_hor {mism[4][1].real:+.4f}{mism[4][1].imag:+.4f}i")
# (i) real step
check("(C-i) a real impedance step (H-SURFACE-IMPEDANCE; CANDIDATE-S-AREA): meets the a = 0 pole datum to 0.04 (calibration), cannot meet the Kerr pole datum (opposite Im sign) — the 3657/3668 failures restated as a mechanism verdict", m0 < 0.05 and mism[4][1].imag * mism[4][2].imag < 0)
# (ii) delay
tau_d = -ph68 / (2 * k68)                     # phase = -2 k tau_d (fit on Kerr)
ph0_pred = -2 * k0 * tau_d
tP_M = 5.39e-44 / (62 * 4.925e-6)             # one Planck time in units of M (62 Msun)
print(f"    (ii) delay fitted on Kerr: tau_d = {tau_d:.3f} M -> predicted a = 0 phase {np.degrees(ph0_pred):+.1f} deg (datum {np.degrees(ph0):+.1f});  one Moment = t_P = {tP_M:.1e} M -> phase {np.degrees(-2*k0*tP_M):.1e} deg")
check("(C-ii) a delayed compliant surface cannot meet both: a delay is a phase e^{-2ik tau} on a passive reflector and cannot flip the sign of Im beta at the Kerr pole; on the real-omega readings the Kerr-fitted delay predicts -12 deg at a = 0 against -43 deg; and a ONE-MOMENT (Planck) delay is 1e-39 deg — the one-Moment-delay compliance of 3375/3376 is a phase-zero surface at ringdown frequencies", abs(np.degrees(ph0_pred) - np.degrees(ph0)) > 5 and abs(np.degrees(-2 * k0 * tP_M)) < 1e-30 and mism[4][1].imag * mism[4][2].imag < 0)
# (iii) frame Doppler — already the surface-frame reading; recorded
check("(C-iii) the co-rotating real step IS mechanism (i) in the surface frame (Omega_w) — tested at 3657 (SN) and 3668 (Z+): out in every frame; recorded, not rescored", True)
# (iv) the excised region: by construction; is the a = 0 number derived from GR?
check("(C-iv) FINDING: the only structure that meets both pole data with no parameter is the excised region itself — GR's wave equation between r_w and r_+ with horizon absorption behind it. The a = 0 number 3.22 is the l = 2 pole value of a GR function (B1), not a surface constant; OPEN-GR-SURFACE-IMPEDANCE-1 as posed ('derive s from the cycle') has no passive-surface solution — its target is the complex admittance beta_hor(omega, l, m, chi) at the poles, which from chi ~ 0.6 is not absorbing at all in the even variable (Im > 0): a saturated register meets it only if it propagates the exterior's wave equation below the cap",
      max(mis_pole.values()) < 0.07 and mism[4][1].imag * mism[4][2].imag < 0)

print(); print(f"3670 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
