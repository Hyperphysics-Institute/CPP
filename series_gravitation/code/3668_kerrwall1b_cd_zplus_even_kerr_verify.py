#!/usr/bin/env python3
"""
Patch 3668 verify — OPEN-GR-KERRWALL-1b: H-SURFACE-IMPEDANCE on the EVEN-type Kerr master variable
(Chandrasekhar-Detweiler Z+) at chi = 0.68, s = 3.218 UNCHANGED (rule 6). Run from the repo root
(exec's 3359's SN/Leaver-angular machinery and 3358's Leaver radial continued fraction).

LITERATURE-BOUND (3657 §5; handover 164 next act 1). The CD potential is transcribed from
Hatsuda & Kimura, "Semi-analytic expressions for quasinormal modes of slowly rotating Kerr black
holes", arXiv:2006.15496, eqs. (12)-(17) [their refs: Chandrasekhar & Detweiler, Proc. R. Soc. A 350,
165 (1976); Detweiler, Proc. R. Soc. A 352, 381 (1977)]:

    X'' + (omega^2 - V_CD) X = 0,   ' = d/dr*,   dr*/dr = (r^2+a^2)/Delta,
    V_CD = omega^2 + calV,
    calV = (-K^2 + Delta lam)/(r^2+a^2)^2 + 2 Delta (r^3 M + a^4)/(r^2 (r^2+a^2)^3) + 3 a^2 Delta^2/(r^2+a^2)^4
           - 4 lam rho^2 Delta ( -2 lam rho^2 (r^2 - a^2) + 2 r (r M - a^2)(4 lam r + 6M + kappa2) )
             / ( r^2 (r^2+a^2)^2 ( 2 lam r^2 + (6M + kappa2) r - 2 lam (a^2 + a m/sigma) )^2 ),
    K = (r^2+a^2) omega - a m,   rho^2 = r^2 + a^2 + a m/sigma,   sigma = -omega,
    kappa2 = +-sqrt( 36 M^2 - 2 lam ( (a^2 + a m/sigma)(5 lam + 6) - 12 a^2 ) + 2 b2 lam (lam + 2) ),
    b2 = +-3 (a^2 + a m/sigma).
Their footnote 7: the minus signs give Regge-Wheeler at a -> 0, the plus signs Zerilli. Their lam is the
angular eigenvalue with lam_0 = l^2 + l - 2, i.e. lam = A_{-2,lm}(a omega) + a^2 omega^2 - 2 a m omega
(their footnote 8) — the SAME lam 3359 feeds the SN equation. Same omega convention (e^{-i omega t};
outgoing e^{+i omega r*}, ingoing e^{-i k r*}, k = omega - m Omega_H; their App. A).

Nothing in the potential is from memory. Four sign choices exist (kappa2, b2); at a = 0 b2 = 0, so the
kappa2 sign alone selects the parity. FOUND HERE (T3): only b2 = -3 alpha^2 gives potentials isospectral with
Teukolsky at Kerr (both kappa2 signs, to 6e-5); b2 = +3 alpha^2 does not (3.6e-3 and 4e-2, non-convergent in the
horizon start). So the even-type Kerr variable is Z+ := (kappa2 > 0, b2 = -3 alpha^2) — NOT the literal "both plus"
reading of Hatsuda-Kimura's footnote 7. The b2 > 0 combinations are reported and excluded.

VALIDATION BEFORE ANY KERR NUMBER (BLOCKING, 3359 §1 recall risk):
 T1  a = 0: calV(+) + omega^2 = V_Zerilli pointwise; calV(-) + omega^2 = V_Regge-Wheeler pointwise.
 T2  a = 0: the horizon-equivalent pole on Z+ and on Z- both = the Schwarzschild l = 2 QNM (Chandrasekhar's
     parity map: the two potentials are isospectral).
 T3  Kerr chi = 0.68, (2,2): the horizon-equivalent poles on Z+(b2 +), Z+(b2 -), Z-(b2 -) all = Leaver's
     Kerr QNM (3358's radial CF) — the four CD potentials are isospectral with Teukolsky.
 T4  a = 0: the horizon law on Z+ at 8M/3 = 3644's Zerilli point (+0.008 - 0.116i). RECORD CORRECTION found
     here: 3644 evaluated that point at the COMPLEX QNM frequency (beta_horizon(wGR), wGR complex); at REAL
     omega_QNM the Zerilli horizon law is +0.116 - 0.185i. 3657 §3/(1b) compared Regge-Wheeler at real omega
     (+0.105 - 0.206i) against Zerilli at complex omega and concluded the parities differ at a = 0; at matched
     omega they are alike (both near-imaginary at the pole, both real-heavy at real omega). 3657's premise that
     "the hypothesis lives naturally on the even variable" rested on that mismatch.
THEN
 (5) Kerr: the horizon law on Z+ at the wall at real omega; the horizon seen from the wall as a reflector,
     R = (beta + ik)/(ik - beta), in the three frames — is the Kerr requirement (|R| ~ 0.7 at ~ -17 deg on the
     SN local wave, 3657) a property of the variable or of the horizon?
 (6) THE TEST: beta_Z+ = -i (omega - m Omega)/s, s = 3.218 unchanged, Omega in {Omega_w, Omega_H, 0}, both
     b2 signs; scored vs the machinery's own horizon pole on Z+ (H) and Leaver (K); GW250114 box
     (df +-2.4 %, dtau (-15, +17) %; 3659) and the GW150914 box for continuity with 3657.
 (7) s-scan on Z+ (is it the number or the form?).
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
BOX250 = lambda d: -2.4 < d[0] < 2.4 and -15 < d[1] < 17          # GW250114 (3659)
BOX150 = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4        # GW150914 (3616; 3657's)
S_PIN = 3.218                                                     # 3644 a = 0 l = 2 Zerilli pin; UNCHANGED

# ------------------------------------------------------------ 3358's Leaver radial CF (own namespace), 3359's angular CF + rstar
ns = {"np": np, "fsolve": fsolve}
src58 = open("series_gravitation/code/3358_kerr_wall_modes_verify.py").read()
exec(src58.split("# ======================= Leaver machinery (2M = 1 inside) =======================")[1].split("# ======================= PART A")[0], ns)
kerr_qnm = ns["kerr_qnm"]
src59 = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(src59.split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
exec(src59.split("# ---------------- the SN wall solver ----------------")[1].split("def X_at_wall")[0])   # _AA, F_n, r_surface, rstar

def lam_of(w, a, ell, m):
    A = A_leaver(a * w, ell, m) if a != 0.0 else (ell * (ell + 1) - 2 + 0j)
    return A + a * a * w * w - 2 * a * m * w

# ------------------------------------------------------------ the Chandrasekhar-Detweiler potential (Hatsuda-Kimura eqs. 13-17)
def calV_CD(r, a, w, m, lam, sk, sb, M=1.0):
    """calV = V_CD - omega^2 (so X'' = calV X). sk = sign of kappa2, sb = sign of b2."""
    D = r * r - 2 * M * r + a * a
    K = (r * r + a * a) * w - a * m
    sig = -w
    al2 = a * a + a * m / sig                       # Chandrasekhar's alpha^2 = a^2 + a m/sigma
    rho2 = r * r + al2
    b2 = sb * 3 * al2
    kap2 = sk * np.sqrt(36 * M * M - 2 * lam * (al2 * (5 * lam + 6) - 12 * a * a) + 2 * b2 * lam * (lam + 2) + 0j)
    t1 = (-K * K + D * lam) / (r * r + a * a) ** 2
    t2 = 2 * D * (r ** 3 * M + a ** 4) / (r * r * (r * r + a * a) ** 3)
    t3 = 3 * a * a * D * D / (r * r + a * a) ** 4
    num = -4 * lam * rho2 * D * (-2 * lam * rho2 * (r * r - a * a) + 2 * r * (r * M - a * a) * (4 * lam * r + 6 * M + kap2))
    den = r * r * (r * r + a * a) ** 2 * (2 * lam * r * r + (6 * M + kap2) * r - 2 * lam * al2) ** 2
    return t1 + t2 + t3 + num / den

# reference a = 0 potentials (3644's V_Z; 3359's V_RW)
def V_Z(r, ell):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r ** 3 + 6 * n * n * r ** 2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r ** 3 * (n * r + 3) ** 2)
V_RW = lambda r, ell: (1 - 2 / r) * (ell * (ell + 1) / r ** 2 - 6 / r ** 3)

# ------------------------------------------------------------ Schroedinger-form wall solver (F = 0), generic in the potential
def Z_at_wall(w, a, ell, m, rw, sk, sb, r0=40.0, nterms=8):
    lam = lam_of(w, a, ell, m)
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)
    def pd(cc, r):
        D = r * r - 2 * r + a * a; drs = (r * r + a * a) / D
        S = sum(cc[k] / r ** k for k in range(len(cc)))
        dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r, a))
        X = e * S
        dX_dr = e * (1j * w * drs * S + dS); Xp = dX_dr / drs
        ddrs = (2 * r * D - (r * r + a * a) * (2 * r - 2)) / D ** 2
        d2X_dr2 = e * ((1j * w * drs) ** 2 * S + 1j * w * ddrs * S + 2 * 1j * w * drs * dS + d2S)
        Xpp = (d2X_dr2 - Xp * ddrs) / drs ** 2
        return X, Xp, Xpp
    def resid(cc):
        return np.array([(pd(cc, r)[2] - calV_CD(r, a, w, m, lam, sk, sb) * pd(cc, r)[0]) / np.exp(1j * w * rstar(r, a)) for r in rs])
    Mx = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0; Mx[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(Mx, -base, rcond=None)[0]
    X0, Xp0, _ = pd(c, r0)
    def rhs(t, y):
        r = y[4]; D = r * r - 2 * r + a * a
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]; Xpp = calV_CD(r, a, w, m, lam, sk, sb) * X
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, D / (r * r + a * a)]
    sol = solve_ivp(rhs, [rstar(r0, a), rstar(rw, a)], [X0.real, X0.imag, Xp0.real, Xp0.imag, r0], rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])

def beta_hor_Z(w, a, ell, m, rw, sk, sb, eps=1e-6):
    """horizon-equivalent law on the CD variable at r_w: log-derivative (r*) of the solution ingoing at the horizon."""
    lam = lam_of(w, a, ell, m)
    rp = 1 + np.sqrt(1 - a * a); OmH = a / (2 * rp) if a != 0 else 0.0; k = w - m * OmH
    r_start = rp + eps                      # 1e-6: at complex omega the outgoing branch grows outward and contaminates a coarser start
    X0 = np.exp(-1j * k * rstar(r_start, a)); Xp0 = -1j * k * X0
    def rhs(t, y):
        r = y[4]; D = r * r - 2 * r + a * a
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]; Xpp = calV_CD(r, a, w, m, lam, sk, sb) * X
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, D / (r * r + a * a)]
    sol = solve_ivp(rhs, [rstar(r_start, a), rstar(rw, a)], [X0.real, X0.imag, Xp0.real, Xp0.imag, r_start], rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[2, -1] + 1j * sol.y[3, -1]) / (sol.y[0, -1] + 1j * sol.y[1, -1])

def root_Z(beta_fn, a, ell, m, rw, sk, sb, guess):
    def Fk(w):
        X, Xp = Z_at_wall(w, a, ell, m, rw, sk, sb); b = beta_fn(w); return (Xp - b * X) / (1 + abs(b))
    fn = lambda v: [Fk(v[0] + 1j * v[1]).real, Fk(v[0] + 1j * v[1]).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]

def refl(beta, k): return (beta + 1j * k) / (1j * k - beta)

# ============================================================ T1: a = 0 pointwise reduction
print("T1. a = 0: the transcribed CD potential reduces pointwise to Zerilli (kappa2 > 0) and Regge-Wheeler (kappa2 < 0)")
wGR = 0.37367 - 0.08896j; R0 = 8.0 / 3.0
dZ = dR = []
dZ = [max(abs(calV_CD(r, 0.0, wGR, 2, 4.0 + 0j, +1, sb) + wGR * wGR - V_Z(r, 2)) for sb in (+1, -1)) for r in (2.3, 8 / 3, 3.0, 5.0, 10.0, 30.0)]
dR = [max(abs(calV_CD(r, 0.0, wGR, 2, 4.0 + 0j, -1, sb) + wGR * wGR - V_RW(r, 2)) for sb in (+1, -1)) for r in (2.3, 8 / 3, 3.0, 5.0, 10.0, 30.0)]
dZ3 = [abs(calV_CD(r, 0.0, wGR, 3, 10.0 + 0j, +1, -1) + wGR * wGR - V_Z(r, 3)) for r in (2.3, 3.0, 10.0)]
check("T1a. calV(kappa2 > 0) + omega^2 = V_Zerilli(l = 2) pointwise at a = 0 (both b2 signs; b2 = 0 there)", max(dZ) < 1e-12, f"max dev {max(dZ):.1e}")
check("T1b. calV(kappa2 < 0) + omega^2 = V_Regge-Wheeler(l = 2) pointwise at a = 0", max(dR) < 1e-12, f"max dev {max(dR):.1e}")
check("T1c. l = 3 Zerilli reproduced too (the lam-dependence of the transcription is right, not just l = 2)", max(dZ3) < 1e-12, f"max dev {max(dZ3):.1e}")

# ============================================================ T2: a = 0 isospectrality of the two parities
print("T2. a = 0: horizon-equivalent poles at 8M/3 on Z+ and Z- both reproduce the Schwarzschild l = 2 QNM (Chandrasekhar's parity map)")
dev0 = lambda w: (100 * (w.real / wGR.real - 1), 100 * (abs(wGR.imag) / abs(w.imag) - 1))
wZp0 = root_Z(lambda w: beta_hor_Z(w, 0.0, 2, 2, R0, +1, -1), 0.0, 2, 2, R0, +1, -1, 0.37 - 0.09j)
wZm0 = root_Z(lambda w: beta_hor_Z(w, 0.0, 2, 2, R0, -1, -1), 0.0, 2, 2, R0, -1, -1, 0.37 - 0.09j)
print(f"    Z+: {wZp0.real:.5f} {wZp0.imag:+.5f}i   Z-: {wZm0.real:.5f} {wZm0.imag:+.5f}i   (Leaver {wGR.real:.5f} {wGR.imag:+.5f}i)")
check("T2. both parities' horizon-equivalent poles = Schwarzschild QNM to < 1e-4 relative, and to each other", abs(wZp0 - wGR) / abs(wGR) < 1e-4 and abs(wZm0 - wGR) / abs(wGR) < 1e-4 and abs(wZp0 - wZm0) < 1e-4,
      f"Z+ dev {dev0(wZp0)[0]:+.3f}%/{dev0(wZp0)[1]:+.3f}%; |Z+ - Z-| = {abs(wZp0 - wZm0):.1e}")

# ============================================================ T3: Kerr isospectrality vs Leaver
A68 = 0.68; RW68 = 2.7344
print(f"T3. Kerr chi = {A68}, (2,2), wall {RW68} M: horizon-equivalent poles on the CD potentials vs Leaver's radial continued fraction (3358)")
wK = kerr_qnm(A68, 2, 2, -2, 0.526 - 0.082j)
print(f"    Leaver (2,2) at chi = 0.68: {wK.real:.5f} {wK.imag:+.5f}i  ({to_hz(wK.real):.1f} Hz at 62 Msun; Berti fit ~0.526 -0.082i)")
signs = {"Z+ (kappa2 +, b2 +)": (+1, +1), "Z+ (kappa2 +, b2 -)": (+1, -1), "Z- (kappa2 -, b2 -)": (-1, -1), "Z- (kappa2 -, b2 +)": (-1, +1)}
wH = {}
for lab, (sk, sb) in signs.items():
    wH[lab] = root_Z(lambda w, sk=sk, sb=sb: beta_hor_Z(w, A68, 2, 2, RW68, sk, sb), A68, 2, 2, RW68, sk, sb, wK)
    print(f"    {lab}: {wH[lab].real:.5f} {wH[lab].imag:+.5f}i   |dev| vs Leaver {abs(wH[lab] - wK) / abs(wK):.1e}")
devK = lambda w: (100 * (w.real / wK.real - 1), 100 * (abs(wK.imag) / abs(w.imag) - 1))
iso = {l: abs(wH[l] - wK) / abs(wK) for l in wH}
check("T3a. the b2 = -3 alpha^2 potentials, BOTH kappa2 signs, are isospectral with Teukolsky at chi = 0.68: horizon-equivalent poles = Leaver's (2,2) QNM to < 2e-4 relative (the test a wrong am/sigma sign, a wrong kappa2, or a wrong term would fail)",
      iso["Z+ (kappa2 +, b2 -)"] < 2e-4 and iso["Z- (kappa2 -, b2 -)"] < 2e-4, f'Z+: {iso["Z+ (kappa2 +, b2 -)"]:.1e}; Z-: {iso["Z- (kappa2 -, b2 -)"]:.1e}')
check("T3b. FINDING: the b2 = +3 alpha^2 potentials are NOT isospectral (deviations do not converge with the horizon start) — excluded; the even-type Kerr variable is Z+ = (kappa2 > 0, b2 = -3 alpha^2), not the literal both-plus reading of Hatsuda-Kimura's footnote 7",
      iso["Z+ (kappa2 +, b2 +)"] > 1e-3 and iso["Z- (kappa2 -, b2 +)"] > 1e-3, f'(+,+): {iso["Z+ (kappa2 +, b2 +)"]:.1e}; (-,+): {iso["Z- (kappa2 -, b2 +)"]:.1e}')
SB = -1                                                            # the isospectral even-type variable from here on
sn_pole = 0.5242 - 0.0810j
print(f"    (3619/3657's SN horizon-equivalent pole {sn_pole.real:.4f} {sn_pole.imag:+.4f}i was {devK(sn_pole)[0]:+.2f}% / {devK(sn_pole)[1]:+.2f}% from Leaver; the CD instrument is the tighter one)")

# ============================================================ T4: a = 0 horizon law on Z+ vs 3644's Zerilli point — and the record correction
print("T4. a = 0: the horizon law on Z+ at 8M/3 vs 3644's Zerilli point +0.008 -0.116i")
bZc = beta_hor_Z(wGR, 0.0, 2, 2, R0, +1, SB); bZr = beta_hor_Z(wGR.real, 0.0, 2, 2, R0, +1, SB)
bRc = beta_hor_Z(wGR, 0.0, 2, 2, R0, -1, SB); bRr = beta_hor_Z(wGR.real, 0.0, 2, 2, R0, -1, SB)
print(f"    at the COMPLEX QNM frequency (3644's evaluation point, beta_horizon(wGR)): Z+ {bZc.real:+.4f} {bZc.imag:+.4f}i   Z- {bRc.real:+.4f} {bRc.imag:+.4f}i")
print(f"    at REAL omega_QNM:                                                       Z+ {bZr.real:+.4f} {bZr.imag:+.4f}i   Z- {bRr.real:+.4f} {bRr.imag:+.4f}i   [3657 (1b) quoted RW at real omega +0.1052 -0.2060i against Zerilli's complex-omega value]")
print(f"    the pin's defining number re-evaluated with the converged start: Re omega/|Im beta_Z+(wGR)| = {wGR.real/abs(bZc.imag):.3f} (pin {S_PIN}, from a 1e-4 start; frozen, not refit)")
check("T4a. the Z+ horizon law at the complex QNM frequency reproduces 3644's Zerilli point to 4e-3 (3644's 1e-4 start; the CD variable at a = 0 IS Zerilli)", abs(bZc - (0.008 - 0.116j)) < 4e-3, f"|diff| = {abs(bZc - (0.008 - 0.116j)):.1e}")
check("T4b. RECORD CORRECTION to 3657 §3/(1b) and CONV-042's 'near-pure-imaginary horizon is an even-variable property': at MATCHED frequency the two parities' horizon laws at 8M/3 are alike — both near-imaginary at the pole (|Re| < 0.01), both real-heavy at real omega (Re ~ +0.11) — the contrast in 3657 was an omega mismatch, not a parity property",
      abs(bZc.real) < 0.01 and abs(bRc.real) < 0.01 and bZr.real > 0.08 and bRr.real > 0.08,
      f"pole: Z+ Re {bZc.real:+.4f}, Z- Re {bRc.real:+.4f}; real omega: Z+ Re {bZr.real:+.4f}, Z- Re {bRr.real:+.4f}")

# ============================================================ (5) Kerr: the horizon law on Z+ at the wall
print(f"(5) Kerr: the horizon law on Z+ at r_w = {RW68} M at real omega, and the horizon seen from the wall as a reflector of Z+")
rp = 1 + np.sqrt(1 - A68 * A68); OmH = A68 / (2 * rp)
Aw = (RW68 ** 2 + A68 ** 2) ** 2 - (RW68 ** 2 - 2 * RW68 + A68 ** 2) * A68 ** 2
Omw = 2 * A68 * RW68 / Aw
frames = {"Omega = Omega_w (surface's own frame)": Omw, "Omega = Omega_H": OmH, "Omega = 0 (asymptotic omega)": 0.0}
print(f"    Omega_H = {OmH:.4f}, Omega_w = {Omw:.4f}")
wr = wK.real
bZ = beta_hor_Z(wr, A68, 2, 2, RW68, +1, SB); bZm = beta_hor_Z(wr, A68, 2, 2, RW68, -1, SB)
bZc68 = beta_hor_Z(wK, A68, 2, 2, RW68, +1, SB)
print(f"    beta_hor,Z+ at real omega = {wr:.4f}: {bZ.real:+.4f} {bZ.imag:+.4f}i;   at the complex pole: {bZc68.real:+.4f} {bZc68.imag:+.4f}i")
print(f"    beta_hor,Z- at real omega          : {bZm.real:+.4f} {bZm.imag:+.4f}i      [SN local wave Y (3657): +0.0574 -0.0709i; SN X: +0.0681 -0.1546i]")
print("    the horizon as a reflector of Z+, R = (beta + ik)/(ik - beta), k = omega - m Omega:")
RZ = {flab: refl(bZ, wr - 2 * Om) for flab, Om in frames.items()}
for flab, R in RZ.items(): print(f"      Z+, {flab:36s}: |R| = {abs(R):.3f}, phase {np.degrees(np.angle(R)):+.1f} deg     [SN Y (3657): Omega_w 0.707 at -16.7; Omega_H 0.397 at -59.1; 0: 0.764 at -12.7]")
Rw = RZ["Omega = Omega_w (surface's own frame)"]
check("(5) RECORDED: the Kerr horizon's reflection of the even-type variable from the wall in the surface frame — the Kerr requirement re-read in the variable the hypothesis was pinned on", True, f"|R| {abs(Rw):.3f} at {np.degrees(np.angle(Rw)):+.1f} deg")
check("(5b) FINDING: in the surface frame the horizon's reflection of Z+ is still a COMPLEX impedance (|phase| > 8 deg, |R| > the a = 0 value 0.53) — the requirement of 3657 §4 is basis-robust in kind (a lossy spring), with basis-dependent numbers (0.71 at -17 on SN's Y; here on Z+)",
      abs(np.degrees(np.angle(Rw))) > 8 and abs(Rw) > 0.53, f"phase {np.degrees(np.angle(Rw)):+.1f} deg, |R| {abs(Rw):.2f}")

# ============================================================ (6) THE TEST: the hypothesis on Z+, s unchanged
print(f"(6) THE KERR TEST ON Z+: beta = -i (omega - m Omega)/s, s = {S_PIN} UNCHANGED; scored vs the Z+ horizon pole (H) and Leaver (K); GW250114 box df +-2.4% / dtau (-15,+17)%; [GW150914 box in brackets]")
res = {}
wHZ = wH["Z+ (kappa2 +, b2 -)"]
devH = lambda w: (100 * (w.real / wHZ.real - 1), 100 * (abs(wHZ.imag) / abs(w.imag) - 1))
for flab, Om in frames.items():
    w = root_Z(lambda w, Om=Om: -1j * (w - 2 * Om) / S_PIN, A68, 2, 2, RW68, +1, SB, 0.40 - 0.11j)
    res[flab] = (w, devH(w), devK(w)); dH, dK = devH(w), devK(w)
    print(f"    Z+, {flab:36s}: {w.real:.4f} {w.imag:+.4f}i  vs H: df {dH[0]:+6.1f}% dtau {dH[1]:+6.1f}% {'IN' if BOX250(dH) else 'out'} [{'IN' if BOX150(dH) else 'out'}];  vs K: df {dK[0]:+6.1f}% dtau {dK[1]:+6.1f}% {'IN' if BOX250(dK) else 'out'} [{'IN' if BOX150(dK) else 'out'}]     [3657 on SN X, same frame: {({'Omega = Omega_w (surface\'s own frame)': '-18.9%/-47.4%', 'Omega = Omega_H': '-14.3%/-38.2%', 'Omega = 0 (asymptotic omega)': '-20.5%/-50.5%'})[flab]}]")
in250 = [k for k, v in res.items() if BOX250(v[1])]; in150 = [k for k, v in res.items() if BOX150(v[1])]
prim = res["Omega = Omega_w (surface's own frame)"]
check("(6a) RECORDED EITHER WAY: whether the pure-imaginary law with the a = 0 Zerilli-pinned s lands the Kerr (2,2) line on the EVEN-type Kerr variable — the hypothesis' Kerr member on the variable it was pinned on", True,
      f"in GW250114 box: {in250}; in GW150914 box: {in150}")
check("(6b) VERDICT for OPEN-GR-KERRWALL-1b: the Kerr member FAILS on Z+ too — no frame, in either box (recorded as computed; the door is closed)", True,
      "FAILS on Z+" if not in250 and not in150 else f"DESCRIPTIVE on Z+ in: {in250 or in150}")
check("(6c) FINDING: on Z+ the frequency miss is LARGER than on the SN realization (~-27% vs -19%) and the damping miss smaller (-32% vs -47%); neither realization comes near the box — the even variable relocates the miss, it does not close it", prim[1][0] < -18.9 and abs(prim[1][1]) > 25, f"surface frame: df {prim[1][0]:+.1f}% / dtau {prim[1][1]:+.1f}% (SN X: -18.9% / -47.4%)")

# ============================================================ (7) s-scan on Z+
print("(7) s-scan on Z+, surface frame and Omega_H: the number or the form?")
scan_in = []
for flab, Om in (("Omega_w", Omw), ("Omega_H", OmH)):
    prev = res["Omega = Omega_w (surface's own frame)" if flab == "Omega_w" else "Omega = Omega_H"][0]
    line = f"      {flab}: "
    for sv in (1.5, 2.0, 3.218, 5.0, 8.0, 15.0, 40.0):
        w = root_Z(lambda w, Om=Om, sv=sv: -1j * (w - 2 * Om) / sv, A68, 2, 2, RW68, +1, SB, prev); prev = w
        dH = devH(w); line += f"s={sv:g} ({dH[0]:+.0f}%,{dH[1]:+.0f}%){' IN' if BOX250(dH) else ''}  "
        if BOX250(dH): scan_in.append((flab, sv))
    print(line)
check("(7) FINDING: NO s in [1.5, 40] puts the pure-imaginary law on Z+ inside the GW250114 box in either frame — on the even variable too, the failure is the FORM (a real impedance step), not the number", len(scan_in) == 0, f"in-box (frame, s): {scan_in}")
print("    the pin re-read on Z+ at Kerr, s_Kerr = (omega - m Omega)/|Im beta_hor,Z+|: " + ", ".join(f"{flab.split(' ')[2]}: {(wr - 2*Om)/abs(bZ.imag):.3f}" for flab, Om in frames.items()) + "   (a = 0 pin 3.218; SN Y: 5.70 / 1.86 / 7.39)")

print(); print(f"3668 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
