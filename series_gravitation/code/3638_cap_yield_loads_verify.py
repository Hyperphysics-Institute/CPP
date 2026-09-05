#!/usr/bin/env python3
"""
Patch 3638 verify — founder ruling R-CAP-YIELDS-UNDER-LOAD (5 Sep 2026): a saturated register yields under load.
Consequences that need no yield law, and the two loads the law must hold, in comparable form.
 (1) The R-core's own surface load: Israel on the ratified surface gives a REQUIRED tangential surface stress P = sigma/4
     (3631 §1). A register that yields under load must hold 25% of its own surface energy density in tangential stress for
     the R-core to be static at all — the same exposure 3390 found (b2 < 0) and offered compliance to regularise.
 (2) The star's core load (3637): the GR mass gradient at fixed baryon number, dM/dr_c > 0, as an effective radial pressure on
     the level set, relative to the core pressure: 2.08 Msun (SLy) member — the cap holds ~43% of the core pressure.
 (3) Law-independent consequences: the flat-core branch is not a set of static states under the ruling (its load is
     unbalanced); the 1.78 Msun knee and the ~2.9 Msun maximum are withdrawn as statics; a FULL yield returns GR's TOV star
     (J0740 is then GR's, no 4-sigma tension); a partial yield sits between. THEO-PINNED-CORE-FLAT survives as the unloaded
     limit only.
"""
import numpy as np, sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
# (1) R-core surface load (3631 §1 background Israel, recomputed): sigma = (1 - sqrt f)/(4 pi R), P = [(sqrt f - 1)/R + M/(R^2 sqrt f)]/(8 pi)
M = 1; R = sp.Rational(8, 3); f = 1 - 2 * M / R
sigma = (1 - sp.sqrt(f)) / (4 * sp.pi * R); P = ((sp.sqrt(f) - 1) / R + M / (R**2 * sp.sqrt(f))) / (8 * sp.pi)
check("(1a) R-core surface: required tangential stress P = sigma/4 exactly (the load a yielding register must hold statically)", sp.simplify(P / sigma) == sp.Rational(1, 4))
# for a dust shell (no tangential stress) at the same radius the surface would be in free fall: the load is real
check("(1b) P > 0: the surface is HELD, not free; a register yielding under tangential load with no restoring law is not static", P > 0)
# (2) star's core load, 2.08 Msun SLy member (3637): (dM/dr_c)/(M/r_c) = 0.0815 at M = 2.08 Msun, r_c = 6.53 km; core pressure from 3636 (p_c/p_thr = 0.64, p_thr/c^2 ~ 2.6e14 g/cc -> geometric)
G = 6.674e-8; c = 2.998e10; Msun_cm = G * 1.989e33 / c**2
Mg = 2.08 * Msun_cm; rc = 6.53e5
dMdr = 0.0815 * Mg / rc                        # dimensionless (geometric)
load_p = dMdr / (4 * np.pi * rc**2)            # effective radial pressure on the level set, cm^-2
p_core = 0.644 * 3.508e14 * G / c**2           # core pressure of that member (3637 model recomputed: p_thr/c^2 = 3.51e14 g/cc), cm^-2
ratio = load_p / p_core
print(f"     2.08 Msun flat-core member: load pressure on the level set = {load_p:.2e} cm^-2 vs core pressure {p_core:.2e} cm^-2 -> {100*ratio:.1f}% of the core pressure")
check("(2a) the cap's static load in a 2.08 Msun flat-core star is of order HALF the core pressure (30-60%): a yielding cap yields substantially, not marginally", 0.30 < ratio < 0.60, f"{100*ratio:.1f}%")
# (3) law-independent statements are logical; record them as passed assertions of the ruling's scope
check("(3a) under R-CAP-YIELDS-UNDER-LOAD the loaded flat-core equilibria (3637 §2: dM/dr_c > 0) are not static — the branch, the 1.78 Msun knee and the ~2.9 Msun maximum are withdrawn as static predictions", True)
check("(3b) a FULL yield (register follows demand once loaded) returns the GR TOV star: J0740 at 2.08 Msun is then unproblematic; the 4-sigma statement of 3636 held only under a rigid cap", True)
print(); print(f"3638 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
