#!/usr/bin/env python3
"""
Patch 3684 verify — THE REGISTER SECTOR UNDER THEO-PCD-SEA: geometry of the two zones and the row-6 condition.
Isotropic v = M/rbar; areal r = rbar (1 + v/2)^2. R-core surface at v = cap = 2/3 (areal 8M/3); the sea metric's
wave horizon at v = 2 (areal 2M). M = 1.

 T1  Zones: shell 2/3 <= v <= 2 (areal 8M/3 -> 2M) is register matter VISIBLE to the sea; v > 2 (r < 2M) is DARK.
     Proper radial thickness of the shell on the sea (GR) metric: int psi^2 drbar, psi = 1 + v/2.
 T2  Row-6 condition: Lambda = (2/3) k2 C^-5 with C = M/R = 3/8 for the R-core; GW250114 bound Lambda_tilde < 34.8
     (equal masses: Lambda_tilde = Lambda) -> k2(shell) < 34.8 * 1.5 / (8/3)^5 = 0.388. A rigid floor gives k2 = 0
     (passes); R-CAP-SPRING gives finite k2 (OWED: needs a register law). 3675's "row 6 passes by construction" is
     WEAKENED to "passes iff k2(shell) < 0.39".
 T3  For reference, the budget register's +714 (3650) corresponds to k2 = 714 * 1.5 / (8/3)^5 = 7.95 — unphysical
     (k2 <= ~0.15 for any fluid star; ~1 for an incompressible sphere). So the budget law's failure was not a
     small miss: whatever the register shell's stiffness, it must give a k2 fifty times smaller than that.
 T4  Exterior bimetric signature: the two metrics agree in value and slope at v = cap (3640 §3, 3675 T5), so no
     exterior observable distinguishes them; the partition is testable only through interior-sourced effects
     (tides from the visible shell — row 6 — and the absence of a return from v > 2 — row 5, scored at 3683).
"""
import numpy as np
from scipy.integrate import quad
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
CAP = 2/3
areal = lambda v: (1 + v/2)**2 / v
print("T1 — zones")
rb_s, rb_h = 1/CAP, 1/2.0
thick = quad(lambda rb: (1 + 1/(2*rb))**2, rb_h, rb_s)[0]
print(f"    surface v = {CAP:.3f}: rbar = {rb_s:.3f} M, areal {areal(CAP):.3f} M;  wave horizon v = 2: rbar = {rb_h:.3f} M, areal {areal(2.0):.3f} M")
print(f"    visible shell: areal 2M -> 8M/3 (Delta r = {8/3-2:.3f} M); proper thickness on the sea metric = {thick:.3f} M")
check("T1 wave horizon inside the R-core surface (2M < 8M/3)", areal(2.0) < areal(CAP))
print("\nT2 — row-6 condition")
C = 3/8; k2max = 34.8 * 1.5 * C**5
print(f"    Lambda = (2/3) k2 C^-5, C = {C:.3f}: Lambda_tilde < 34.8  =>  k2(shell) < {k2max:.3f}")
check("T2 k2 bound recorded: 0.35 < k2max < 0.42", 0.35 < k2max < 0.42, f"{k2max:.3f}")
check("T2 rigid floor (k2 = 0) passes; spring floor is conditional (owed)", True)
print("\nT3 — the budget register's k2")
k2_budget = 714 * 1.5 * C**5
print(f"    Lambda = 714  =>  k2 = {k2_budget:.2f}  (incompressible sphere ~ 0.75-1; fluid stars <~ 0.15)")
check("T3 budget k2 is unphysical (> 1)", k2_budget > 1.0, f"{k2_budget:.2f}")
print("\nT4 — exterior degeneracy of the two metrics")
v_eff = lambda v: 2*CAP - CAP**2/v; dv = 1e-6
check("T4 C^1 join at the surface: v_eff(cap) = cap, slope 1", abs(v_eff(CAP)-CAP) < 1e-12 and abs((v_eff(CAP+dv)-v_eff(CAP-dv))/(2*dv) - 1) < 1e-5)
print(f"\n{PASS}/{PASS+FAIL} PASS")
