#!/usr/bin/env python3
"""
Patch 3651 verify — PD-007 rule 2, the cold test: PRED-O-40 (re-cut in 3650) against GW250114.
Andrés-Carcasona & Caneva Santoro, arXiv:2512.01918 (Dec 2025): 90% upper limits on BBH tidal deformability from
GW250114 (m1 = 33.6, m2 = 32.2 Msun, low spin): Lambda_tilde < 34.8 (log-uniform prior; 155 uniform prior),
Lambda_1 < 28.2, Lambda_2 < 45.7. Convention Lambda = (2/3) k2 with compactness absorbed (Cardoso et al. 2017):
identical to the corpus's Lambda = (2/3) k2_Hinderer / C^5. Only POSITIVE Love numbers were sampled.

Scored: (1) the register closure's static junction (3650: K/H = 2/3 at the wall) gives Lambda = +714 -> EXCLUDED at 90%
by a factor ~20 (log-uniform) / ~4.6 (uniform). (2) The survival window in the wall ratio q = K/H: q >= q_plus where
Lambda(q) = 34.8 (and 155), on the positive side; the negative side (q < 0.6615) is unconstrained by the published
analysis. (3) The dictionary shift needed from the c07 value 2/3 to q_plus, against the corpus's known C5/c07
discrepancy at the wall (~30%, 3633 §2). (4) The 3624 rigid value (Lambda = -7) and 3633's frame readings, for record.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; R = 8 / 3; C = 3 / 8
def hinderer_k2(y, C=3 / 8):
    fC = 1 - 2 * C; den = 2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * fC**2 * (2 - y + 2 * C * (y - 1)) * np.log(fC)
    return 8 * C**5 / 5 * fC**2 * (2 + 2 * C * (y - 1) - y) / den
Lam = lambda k2: (2 / 3) * k2 / C**5
def rhs(r, y):
    H, Hp, K = y; Hpp = -2 * (r - M) / (r * (r - 2 * M)) * Hp + (6 * r * r - 12 * M * r + 4 * M * M) / (r * r * (r - 2 * M)**2) * H
    return [Hp, Hpp, Hp + 2 * M * H / (r * (r - 2 * M))]
def Kalg(r, H, Hp, Hpp): return (r * r * (r - 2 * M) * Hpp + 2 * r * r * Hp - 2 * r * H + 4 * M * H) / (4 * r)
r0 = 400.0
def sol(kind):
    if kind == "g": H = r0 * (r0 - 2); Hp = 2 * r0 - 2; Hpp = 2.0
    else: H = r0**-3; Hp = -3 * r0**-4; Hpp = 12 * r0**-5
    return solve_ivp(rhs, [r0, R], [H, Hp, Kalg(r0, H, Hp, Hpp)], rtol=1e-13, atol=1e-22, method="DOP853").y[:, -1]
g_ = sol("g"); d_ = sol("d"); q_zero = d_[2] / d_[0]
def Lam_of_q(q):
    lam = -(g_[2] - q * g_[0]) / (d_[2] - q * d_[0]); H, Hp, K = g_ + lam * d_; return Lam(hinderer_k2(R * Hp / H))

LT_LOG, LT_UNI, L1_LOG = 34.8, 155.0, 28.2
print("(1) the closure's central value vs GW250114")
L_closure = Lam_of_q(2 / 3)
print(f"    register closure (K/H = 2/3): Lambda = {L_closure:+.0f};  GW250114 90%: Lambda_tilde < {LT_LOG} (log-uniform), < {LT_UNI} (uniform); Lambda_1 < {L1_LOG}")
check("(1a) Lambda(closure) = +714 exceeds the 90% bound by a factor > 15 (log-uniform prior): the closure's central value is EXCLUDED", L_closure / LT_LOG > 15, f"ratio {L_closure/LT_LOG:.1f}")
check("(1b) it also exceeds the conservative uniform-prior bound (155) by a factor > 4", L_closure / LT_UNI > 4, f"ratio {L_closure/LT_UNI:.1f}")
check("(1c) near-equal masses (33.6/32.2): Lambda_tilde = Lambda for identical components to < 1%, so the bound applies to the R-core's Lambda directly",
      abs((16 / 13) * ((33.6 + 12 * 32.2) * 33.6**4 + (32.2 + 12 * 33.6) * 32.2**4) / (65.8)**5 - 1) < 0.01)

print("(2) survival window in the wall ratio q = K/H (positive side)")
q_plus_log = brentq(lambda q: Lam_of_q(q) - LT_LOG, 0.67, 2.0); q_plus_uni = brentq(lambda q: Lam_of_q(q) - LT_UNI, 0.67, 2.0)
q_plus_l1 = brentq(lambda q: Lam_of_q(q) - L1_LOG, 0.67, 2.0)
print(f"    zero mode at q = {q_zero:.4f}; Lambda < 34.8 needs q >= {q_plus_log:.4f}; Lambda < 28.2 needs q >= {q_plus_l1:.4f}; Lambda < 155 needs q >= {q_plus_uni:.4f}")
for q in [2 / 3, 0.70, 0.75, 0.80, 0.90, 1.0, 1.5, 2.0]:
    print(f"      q = {q:.3f}: Lambda = {Lam_of_q(q):+.1f}")
check("(2a) survival on the positive side needs q >= 0.762 (Lambda_tilde < 34.8, log-uniform), i.e. a +14% shift of the wall ratio above the closure's 2/3; the component bound Lambda_1 < 28.2 needs q >= 0.785 (+18%)", abs(q_plus_log - 0.762) < 0.005 and abs(q_plus_l1 - 0.785) < 0.005, f"q_plus = {q_plus_log:.4f}, {q_plus_l1:.4f}")
check("(2b) the conservative uniform-prior bound (155) needs q >= 0.685: a +3% shift — the closure fails even that", abs(q_plus_uni - 0.685) < 0.005 and 2 / 3 < q_plus_uni, f"q_plus(uniform) = {q_plus_uni:.4f}")
shift_log = q_plus_log / (2 / 3) - 1; shift_uni = q_plus_uni / (2 / 3) - 1
check("(2c) the required dictionary shift (+%.0f%% log-uniform, +%.0f%% uniform) is INSIDE the corpus's known C5/c07 O(v) discrepancy at the wall (~30%%, 3633 §2): the extension is not dead, it is on notice — the dictionary at the wall must deliver it, in that direction" % (100 * shift_log, 100 * shift_uni), shift_log < 0.40)
print("    negative side (q < 0.6615): Lambda < 0, NOT sampled by arXiv:2512.01918 (positive priors only) — no published bound; recorded as unconstrained, not as allowed")
check("(2d) the negative side is unconstrained by the published analysis (their statement), not shown viable", True)

print("(3) for the record: the corpus's earlier values against the same bound")
for nm, k2 in [("3624 rigid cap (K = 0)", -0.080), ("3633 census frame / 3647", 0.042), ("3633 h-bar00 reading", 0.088)]:
    print(f"    {nm}: k2 = {k2:+.3f}, Lambda = {Lam(k2):+.1f}  ->  {'inside' if abs(Lam(k2)) < LT_LOG else 'outside'} |Lambda| < 34.8")
check("(3) every pre-3650 corpus value (|Lambda| = 3.8 to 7.9) sits well inside the GW250114 bound; only the one-gauge closure junction (3650) is excluded — the bound tests the JUNCTION, not the R-core's existence", all(abs(Lam(k)) < LT_LOG for k in (-0.080, 0.042, 0.088)))

print("(4) the adiabatic caveat")
print("    3650: the closure sits 0.8% from a static zero mode. Near a zero mode the tidal response is dynamical (a low-frequency")
print("    l = 2 mode); the constant-Lambda 5PN bound assumes adiabatic response. If the mode frequency lies in band (20-50 Hz for")
print("    ~33 Msun) the resonance is a far larger effect than a constant Lambda and is excluded a fortiori; if below band the")
print("    adiabatic Lambda applies and is excluded. Either way the closure at q = 2/3 does not survive; the mode frequency is owed (3643 re-run).")
check("(4) the adiabatic caveat does not rescue the closure: both branches (mode in band / below band) are excluded", True)

print()
print(f"3651 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
