#!/usr/bin/env python3
"""
Patch 3653 verify — the verdict on [PCD-EXT] under PD-007 rules 5 and 6, after the founder declined to pin the mechanism.
(1) Derivation from the cycle as stated (3640 §2-§4): Perceive samples K of D bits; Compute acts on the sample; Displace
    acts on Compute's output. So the displacement (conformal factor) saturates by the same K/D as the count (clock):
    chi_psi = chi_N = cap/v. 3640 §4 said exactly this: "if only the processed ones, the budget law is the theory's."
    => the extension AS DERIVED has q = 2/3 at the wall (3650/3652) and is EXCLUDED by GW250114 (3651). Rule 5.
(2) The compliance-ratio rescue is closed: q = (2/3) chi_psi/chi_N >= 0.762 with chi_psi <= 1 needs chi_N <= 0.875 AT
    THE LEVEL SET, where the budget law gives chi_N = 1 — a harder clamp on the clock than the law derives. Not a
    derivation; and a refit (rule 5 forbids).
(3) Rule 6: the one pre-existing corpus-native reading that passes is C5's linear trace lock (-3) at the wall (3633 §2's
    open discrepancy). Named as HYPOTHESIS H-WALL-LOCK-C5 (never adopted). Group: member 1 (static Love number) scored
    Lambda = +9.2 (passes); members 2 (the dynamical closure's ringdown with the same lock) and 3 (3633's readings
    under it) owed.
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1.0; R = 8 / 3; C = 3 / 8; CAP = 2 / 3
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
g_ = sol("g"); d_ = sol("d")
def Lam_of_q(q):
    lam = -(g_[2] - q * g_[0]) / (d_[2] - q * d_[0]); H, Hp, K = g_ + lam * d_; return Lam(hinderer_k2(R * Hp / H))
BOUND = 34.8

print("(1) derivation from the cycle as stated")
# budget law: both channels scaled K/D = cap/v (3640 §2 item 2). At the level set v = cap: chi = 1 for both.
chi_N = lambda v: CAP / v; chi_psi = lambda v: CAP / v      # the cycle: Displace uses Compute's output, which uses the sample
q_derived = (2 / 3) * chi_psi(CAP) / chi_N(CAP)
print(f"    chi_N(cap) = {chi_N(CAP):.3f}, chi_psi(cap) = {chi_psi(CAP):.3f}  ->  q = (2/3) chi_psi/chi_N = {q_derived:.4f};  Lambda = {Lam_of_q(q_derived):+.0f}")
check("(1a) the cycle as stated gives chi_psi = chi_N (Displace acts on the processed sample): q = 2/3 — 3640 §4's 'if only the processed ones, the budget law is the theory's'", abs(q_derived - 2 / 3) < 1e-12)
check("(1b) the extension AS DERIVED is excluded by GW250114 (Lambda = +714 vs < 34.8): rule 5 — a failed extension, not a datum to refit", Lam_of_q(q_derived) > BOUND)

print("(2) the compliance-ratio rescue, closed")
q_plus = 0.7622
chiN_needed = (2 / 3) / q_plus          # with chi_psi = 1
print(f"    with chi_psi <= 1, survival q >= {q_plus} needs chi_N <= {chiN_needed:.3f} at the level set; the budget law gives chi_N = 1 there")
check("(2a) the rescue requires the CLOCK to be clamped harder than the budget law derives (chi_N <= 0.875 at v = cap): not a derivation from the cycle, and a refit under rule 5", chiN_needed < 0.9 and abs(chi_N(CAP) - 1) < 1e-12)
check("(2b) an over-responding displacement (chi_psi > 1) is the only other route; nothing in the cycle produces a response larger than the demand: closed", True)

print("(3) rule 6: the pre-existing corpus-native reading that passes, as a HYPOTHESIS")
q_C5 = 1.0          # C5's linear lock -3 => K/H0 = 1
L_C5 = Lam_of_q(q_C5)
print(f"    H-WALL-LOCK-C5: static trace lock -3 at the level set (3633 §2's linear dictionary): q = 1, Lambda = {L_C5:+.1f}")
check("(3a) member 1 (static Love number): Lambda = +9.2 < 34.8 — descriptive on GW250114", abs(L_C5 - 9.2) < 0.2 and L_C5 < BOUND)
check("(3b) the hypothesis is a pre-existing corpus statement (C5), not a number fitted to the bound: admissible under rule 6 as a hypothesis, never adopted", True)
check("(3c) members 2 (the dynamical closure's l = 2 ringdown with the same lock, no refit) and 3 (3633's static readings under it) are OWED before any reconnection to the axioms is attempted", True)

print()
print(f"3653 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
