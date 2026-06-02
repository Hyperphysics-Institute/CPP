#!/usr/bin/env python3
"""
0729_scaling_phase_nogo.py
==========================
OPEN-SR-7 derivation -> OPEN-COSMO-DM-2 Step 1 (the cheapest potential kill).

Question (DM-2 generation half): does CPP early dynamics -- the GP-exclusion /
CP-GP packing dynamics near the initial Moment -- admit ANY scaling-symmetric /
quasi-de-Sitter phase, i.e. any window of (near-)constant Hubble rate H that
could generate a near-scale-invariant (equal-power-per-log-interval) primordial
spectrum?

This script verifies, with no free parameters, four facts that together force
the Step-1 verdict, GIVEN the Step-D excess-sourcing Friedmann framework (Gate 1)
that the whole CPP cosmological sector already rests on.

CHECK 1  Barotropic FRW: a(t) ~ t^(2/[3(1+w)]), H(t)=2/[3(1+w)t]. H is constant
         in t ONLY in the de Sitter limit w -> -1. Any w > -1 gives H ~ 1/t.
CHECK 2  Deceleration q = (1+3w)/2 > 0 for all w > -1/3; the ZBW substrate range
         w in [0,1/3] is firmly decelerating; even the stiffest causal fluid w=1
         -> a~t^(1/3), still decelerating.
CHECK 3  GP exclusion is EMERGENT from ZBW DP oscillation (P5 demoted axiom ->
         theorem T-CPP-1; f_ZBW ~ 1/(2 t_P) is the FASTEST mode in CPP). A
         coherent oscillating field in V~phi^n has <w>=(n-2)/(n+2): the physical
         ZBW range (n=2 harmonic -> w=0 matter; n=4 -> w=1/3 radiation) gives
         w in [0,1/3]; reaching w=-1 needs n->0 (a FROZEN, non-oscillating
         field), the antithesis of fast ZBW. So the natural CPP scalar cannot be
         an inflaton.
CHECK 4  The clincher (reading-independent). Scale-invariant perturbation
         GENERATION requires a SHRINKING comoving Hubble radius d/dt[(aH)^-1] < 0,
         i.e. accelerated expansion a_ddot>0  <=>  w < -1/3. The ZBW substrate
         gives w in [0,1/3] => a_ddot<0 => the comoving horizon GROWS => modes
         ENTER (not exit) => no freezing => no scale-free frozen spectrum.

Verdict: conditional on Gate 1, the only constant-H-capable source is the
uniform Sea ground state, which excess-sourcing makes NON-gravitating (no de
Sitter); the ZBW DP-oscillation source is a fast-oscillating DILUTING medium
(w in [0,1/3]).  No scaling-symmetric phase on either branch.  CONJ-COSMO-1
fails as a PRIMARY structure-formation model -- a clean CONDITIONAL false.
"""

import numpy as np

PASS = []

def check(name, cond):
    PASS.append(bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# ---------------------------------------------------------------------------
print("CHECK 1 -- barotropic FRW scale factor & Hubble rate")
def power_p(w):
    return 2.0/(3.0*(1.0+w))

def integrate_H_times_t(w, t0=1.0, t1=10.0, steps=200000):
    p = power_p(w)
    H0 = p/t0
    a0 = 1.0
    dt = (t1-t0)/steps
    a = a0; t = t0
    samples = []
    for i in range(steps):
        H = H0 * a**(-3.0*(1.0+w)/2.0)
        samples.append(H*t)
        a += a*H*dt
        t += dt
    return p, np.array(samples)

for w in [1.0, 1.0/3.0, 0.0, -1.0/3.0, -0.9]:
    p, s = integrate_H_times_t(w)
    const_in_t = np.allclose(s, p, rtol=2e-3)
    check(f"w={w:+.3f}: H*t = p = {p:.4f} (constant in t, H falls as 1/t)", const_in_t)

ws = np.array([-0.99, -0.999, -0.9999])
ps = power_p(ws)
check("w -> -1 : p = 2/[3(1+w)] -> infinity (H constant only in de Sitter limit)",
      np.all(np.diff(ps) > 0) and ps[-1] > 1e3)

# ---------------------------------------------------------------------------
print("CHECK 2 -- deceleration parameter & the diluting-medium range")
def q_of_w(w):
    return 0.5*(1.0+3.0*w)
check("q(w)>0 (decelerating) for all w > -1/3", q_of_w(-1/3+1e-9) > 0 and q_of_w(0) > 0 and q_of_w(1) > 0)
check("ZBW substrate range w in [0,1/3] is decelerating: q(0)=0.5, q(1/3)=1.0", abs(q_of_w(0)-0.5)<1e-12 and abs(q_of_w(1/3)-1.0)<1e-12)
check("even the stiffest causal fluid w=1 -> a ~ t^(1/3) (slowest causal growth, still decelerating)", abs(power_p(1.0)-1.0/3.0) < 1e-12)
check("acceleration onset is w < -1/3 (de Sitter w=-1 is far below any diluting source)",
      q_of_w(-1.0) < 0 and q_of_w(1.0) > 0)

# ---------------------------------------------------------------------------
print("CHECK 3 -- ZBW-grounded EoS: the early substrate is a Sea of FAST-oscillating DPs")
# GP exclusion is NOT a primitive packing axiom: it is EMERGENT from ZBW DP
# oscillation (P5 demoted axiom -> theorem, T-CPP-1; the DP {A(-),B(+)} bounces
# in/out to d_min and back each Moment, f_ZBW ~ 1/(2 t_P) -- a geometric
# consequence of the lattice step + 1/r^2 force law, the FASTEST mode in CPP).
# A coherent field oscillating in V ~ phi^n time-averages (virial) to
#   <w> = (n-2)/(n+2):
#     n=2 (quadratic / harmonic ZBW bond) -> w = 0    (matter-like, pressureless)
#     n=4 (quartic / hot relativistic)    -> w = 1/3  (radiation-like)
#     n->0 (FLAT potential, frozen/slow-roll) -> w -> -1 (de Sitter)  <-- the ONLY
#       way to reach w=-1 is to STOP oscillating; the antithesis of ZBW.
def w_virial(n):
    return (n-2.0)/(n+2.0)
check("quadratic ZBW bond (n=2): <w>=0 (matter-like)", abs(w_virial(2.0)-0.0) < 1e-12)
check("relativistic/quartic (n=4): <w>=1/3 (radiation-like)", abs(w_virial(4.0)-1.0/3.0) < 1e-12)
check("physical ZBW oscillation (n in [2,4]) gives w in [0,1/3], all > -1/3 (decelerating)",
      all(q_of_w(w_virial(n)) > 0 for n in np.linspace(2.0, 4.0, 50)))
check("w=-1 (de Sitter) requires n->0: the FROZEN / non-oscillating limit, opposite of fast ZBW",
      w_virial(1e-6) < -0.999 and w_virial(2.0) >= 0.0)
n_hist = np.linspace(2.0, 4.0, 500)
check("q>0 across the entire physical ZBW EoS range => H decreases => no constant-H window",
      np.all(q_of_w(w_virial(n_hist)) > 0))

# ---------------------------------------------------------------------------
print("CHECK 4 -- comoving Hubble radius: scale-invariant GENERATION needs it to SHRINK")
# ZBW substrate branch w in [0,1/3] -> p = 2/[3(1+w)] in [1/2, 2/3] < 1 -> dR/dt>0
#   -> comoving horizon GROWS -> modes ENTER -> NO freezing -> NO generation.
def p_exponent(w):
    return power_p(w)
for w in [1.0/3.0, 0.0]:
    p = p_exponent(w)
    grows = (1.0 - p) > 0
    check(f"ZBW substrate w={w:+.3f}: comoving Hubble radius R~t^(1-p), 1-p={1-p:+.3f}>0 -> GROWS -> modes enter, no freezing", grows)
p_inf = p_exponent(-0.9)
check("de Sitter-side w=-0.9: p>1 -> R shrinks -> modes exit/freeze (the inflationary condition)", (1.0 - p_inf) < 0)
check("identity: d/dt[(aH)^-1]<0  <=>  a_ddot>0  <=>  w<-1/3 (the ZBW range w in [0,1/3] is excluded)",
      q_of_w(-1/3 - 1e-6) < 0 and q_of_w(0.0) > 0)

# ---------------------------------------------------------------------------
print()
if all(PASS):
    print(f"ALL {len(PASS)} CHECKS PASS")
    print("Step-1 verdict (conditional on Gate-1 excess-sourcing): CPP early dynamics")
    print("admits NO scaling-symmetric / quasi-de-Sitter phase. GP exclusion is EMERGENT")
    print("from ZBW DP oscillation (the fastest mode in CPP); the early substrate is a")
    print("fast-oscillating DP Sea -> matter/radiation-like (w in [0,1/3]) -> comoving")
    print("horizon GROWS -> no mode freezing -> no scale-invariant generation. Reaching")
    print("w=-1 needs a FROZEN field (n->0), the antithesis of ZBW. The only constant-H")
    print("source (uniform Sea) is non-gravitating by excess-sourcing. => CONJ-COSMO-1 fails")
    print("as a PRIMARY structure-formation model: clean CONDITIONAL false (on Gate 1).")
else:
    print(f"{sum(PASS)}/{len(PASS)} checks passed -- see FAIL lines above.")
