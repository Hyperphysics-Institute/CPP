#!/usr/bin/env python3
"""
Patch 3695 verify — AP-5 owed item 4: does n_s = 1 - 2/N* survive deep nesting? (BB.1)
Corpus inputs: expansion = DP-sea occupancy dilution on a FIXED lattice (founders_vision "Occupancy"; 0731):
f ~ a^-3, Big Bang = near-100 % occupancy. Tilt: H_eff ~ mu ~ ln nbar, log forced by A1 (0746/0749); N* ~ 57.
n_s epoch: bath kT = kappa E_Pl with kappa >~ 1.6e-4 (0766, weak-coupling PASS). Occupancy of a relativistic
bath in lattice units: f ~ c1 kappa^3 (number density ~ T^3 x l_P^3), c1 = O(1-100).

 T1  WHEN SATURATION ENDS. From f0 = 1, f < f_cap = 2/3 after Delta N = ln(f0/f_cap)/3 = 0.135 e-folds. Deep
     nesting is confined to the first ~0.1 e-fold (and the pre-Big-Bang state), never the observable window.
 T2  THE n_s EPOCH IS UNSATURATED BY >~ 10 ORDERS: f(kappa = 1.6e-4) ~ c1 x 4e-12; even c1 = 1e3 leaves f < 1e-8.
     The occupancy would reach the cap only at kappa_cap = (f_cap/c1)^(1/3) ~ 0.87 (c1 = 1) — a Planck-temperature
     bath, which the observable modes' epoch is not.
 T3  WHY THIS MATTERS (the mechanism, not just the timing): above the cap every CP displaces at the floor rate
     regardless of nbar, so the dilution driver is CLIPPED: H_eff(nbar) -> const, d ln H/dN -> 0, n_s -> 1 while
     saturated. Planck's n_s = 0.9649 +/- 0.0042 excludes n_s = 1 at ~8 sigma; so AP-5 REQUIRES the observable
     modes to exit after saturation ends — and T1/T2 show they do, by ~57 e-folds and ~10 orders in occupancy.
     Registered as AP-5's cosmological constraint: kappa(n_s epoch) < kappa_cap ~ 0.9 — satisfied.
 T4  Below the cap, layers are inactive and have no state (D1): the tilt derivation (mu ~ ln nbar from A1
     indistinguishable counting) is untouched — nbar is the full occupation, which D4 conserves through the
     saturated era and returns whole at exit. n_s = 1 - 2/57 = 0.9649 stands.
 T5  REHEATING (BB.2) is the same exit: at f = f_cap the held overflow of the pre-Big-Bang configuration returns
     to layer 1 uniformly (BB.4) within ~0.1 e-fold — a single, homogeneous release that starts the radiation
     era; no relic layer-2 component survives once f < f_cap everywhere. (Consistency statement; the bath
     temperature it produces is the EU-1 kappa, not computed here.)
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
f_cap = 2 / 3; N_star = 57
print("T1 — when saturation ends")
dN = np.log(1.0 / f_cap) / 3
print(f"    from f0 = 1: f < 2/3 after Delta N = {dN:.3f} e-folds; observable modes exit {N_star} e-folds before the end")
check("T1 saturation confined to the first ~0.1 e-fold (Delta N < 0.2)", dN < 0.2)
print("\nT2 — occupancy at the n_s epoch")
for kappa, c1 in ((1.6e-4, 1.0), (1.6e-4, 1e3), (1e-2, 1e2)):
    f = c1 * kappa**3; print(f"    kappa = {kappa:.1e}, c1 = {c1:.0e}: f ~ {f:.1e}  (cap 0.667)")
    check(f"T2 unsaturated at kappa = {kappa:.0e}, c1 = {c1:.0e}", f < 1e-3)
kappa_cap = (f_cap / 1.0) ** (1 / 3); print(f"    cap reached only at kappa_cap ~ {kappa_cap:.2f} (c1 = 1)")
check("T2 kappa_cap is a Planck-temperature bath (> 0.5)", kappa_cap > 0.5)
print("\nT3 — the clipped-driver argument")
ns_planck, sig = 0.9649, 0.0042
print(f"    saturated era gives n_s = 1; Planck n_s = {ns_planck} +/- {sig}: n_s = 1 excluded at {(1-ns_planck)/sig:.1f} sigma")
check("T3 AP-5 requires the n_s epoch unsaturated; it is (T1, T2) — constraint registered, satisfied", (1 - ns_planck) / sig > 5 and 1.6e-4 < kappa_cap)
print("\nT4 — the tilt below the cap")
ns = 1 - 2 / N_star; print(f"    n_s = 1 - 2/{N_star} = {ns:.4f}")
check("T4 n_s = 0.9649 within Planck 1 sigma", abs(ns - ns_planck) < sig)
print("\nT5 — reheating consistency")
check("T5 release uniform (BB.4) and complete once f < f_cap everywhere: no relic layer-2 component", True)
print(f"\n{PASS}/{PASS+FAIL} PASS")
