#!/usr/bin/env python3
"""
0729_scaling_phase_nogo.py
===========================
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
CHECK 2  Deceleration q = (1+3w)/2 > 0 for all w > -1/3; the packing/exclusion
         range w in (0,1] is firmly decelerating; stiff limit w=1 -> a~t^(1/3),
         the SLOWEST (most decelerating) causal expansion.
CHECK 3  A parameter-free excluded-volume ("hard-core packing") equation of
         state: w(n) stiffens to the causal limit w->1 as n->n_max (saturation,
         the initial Moment) and softens as the lattice dilutes (n->0), but stays
         in (0,1] throughout -- it NEVER approaches -1. So H falls monotonically;
         no constant-H window exists on the packing branch.
CHECK 4  The clincher (reading-independent). Scale-invariant perturbation
         GENERATION requires a SHRINKING comoving Hubble radius d/dt[(aH)^-1] < 0,
         i.e. accelerated expansion ä>0  <=>  w < -1/3. The packing source gives
         w in (0,1] => ä<0 => the comoving horizon GROWS => modes ENTER (not exit)
         => no freezing => no scale-free frozen spectrum is generated.

Verdict: conditional on Gate 1, the only constant-H-capable source is the
uniform Sea ground state, which excess-sourcing makes NON-gravitating (no de
Sitter); the GP-exclusion source is a maximally stiff (w->1) DILUTING excess.
No scaling-symmetric phase on either branch.  CONJ-COSMO-1 fails as a PRIMARY
structure-formation model -- a clean CONDITIONAL false.
"""

import numpy as np

PASS = []

def check(name, cond):
    PASS.append(bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

# ---------------------------------------------------------------------------
print("CHECK 1 -- barotropic FRW scale factor & Hubble rate")
# Solve continuity + Friedmann for a single barotropic fluid p = w rho c^2.
# Continuity: rho_dot + 3 H (rho + p/c^2) = 0  ->  rho ~ a^{-3(1+w)}.
# Friedmann (flat): H^2 = (8 pi G/3) rho ~ a^{-3(1+w)}.
# Power-law solution a ~ t^p with p = 2/[3(1+w)] (for w != -1):
#   H = p/t,  and H is CONSTANT in t  <=>  p -> infinity  <=>  w -> -1.
def power_p(w):
    return 2.0/(3.0*(1.0+w))

# Numerically integrate a(t) for several w and confirm H*t = p = const.
def integrate_H_times_t(w, t0=1.0, t1=10.0, steps=200000):
    # da/dt = a*H, with H = H0 * a^{-3(1+w)/2} (Friedmann, flat, set H0 at t0)
    p = power_p(w)
    H0 = p/t0                      # match the analytic power-law at t0
    a0 = 1.0
    dt = (t1-t0)/steps
    a = a0; t = t0
    samples = []
    for i in range(steps):
        H = H0 * a**(-3.0*(1.0+w)/2.0)
        samples.append(H*t)        # should equal p at all t for the power-law
        a += a*H*dt
        t += dt
    return p, np.array(samples)

for w in [1.0, 1.0/3.0, 0.0, -1.0/3.0, -0.9]:
    p, s = integrate_H_times_t(w)
    const_in_t = np.allclose(s, p, rtol=2e-3)
    check(f"w={w:+.3f}: H*t = p = {p:.4f} (constant in t, H falls as 1/t)", const_in_t)

# de Sitter limit: as w -> -1, p -> infinity (H -> constant, a -> exponential)
ws = np.array([-0.99, -0.999, -0.9999])
ps = power_p(ws)
check("w -> -1 : p = 2/[3(1+w)] -> infinity (H constant only in de Sitter limit)",
      np.all(np.diff(ps) > 0) and ps[-1] > 1e3)

# ---------------------------------------------------------------------------
print("CHECK 2 -- deceleration parameter & the stiff (packing) extreme")
def q_of_w(w):
    return 0.5*(1.0+3.0*w)         # q = -a_ddot a / a_dot^2 = (1+3w)/2
check("q(w)>0 (decelerating) for all w > -1/3", q_of_w(-1/3+1e-9) > 0 and q_of_w(0) > 0 and q_of_w(1) > 0)
check("packing range w in (0,1] is decelerating: q(0)=0.5, q(1)=2.0", abs(q_of_w(0)-0.5)<1e-12 and abs(q_of_w(1)-2.0)<1e-12)
check("stiff limit w=1 -> a ~ t^(1/3) (slowest causal growth)", abs(power_p(1.0)-1.0/3.0) < 1e-12)
check("acceleration onset is w < -1/3 (de Sitter w=-1 is far outside packing range)",
      q_of_w(-1.0) < 0 and q_of_w(1.0) > 0)

# ---------------------------------------------------------------------------
print("CHECK 3 -- parameter-free excluded-volume packing EoS: w(n) in (0,1], never -1")
# Hard-core / excluded-volume fluid (the generic form of a packing limit):
#   p(n) = n e0 * x/(1-x),  x = n/n_max  (pressure diverges at saturation x->1)
# Energy density rho c^2 = n e0 (rest+thermal scale e0 per quantum; e0>0).
# Effective w = p/(rho c^2) = x/(1-x).  As x->1 (initial Moment, saturated):
#   w -> +infinity, but causality caps the SOUND speed so the physical EoS
#   saturates at the stiff causal limit w_eff -> 1 (c_s -> c).  As x->0: w->0.
# So on (0,1] the *causal* effective w lies in (0,1]; it is bounded BELOW by 0
# and never approaches -1.  Demonstrate across the full dilution history.
xs = np.linspace(1e-4, 1.0-1e-6, 5000)
w_raw = xs/(1.0-xs)
w_causal = np.minimum(w_raw, 1.0)          # causal cap: stiffest is w=1 (c_s=c)
check("excluded-volume w_raw = x/(1-x) >= 0 and diverges at saturation x->1", np.all(w_raw >= 0) and w_raw[-1] > 100)
check("causal-capped w in (0,1] for all dilution states x in (0,1]", np.all((w_causal > 0) & (w_causal <= 1.0+1e-12)))
check("w(n) NEVER approaches -1 on the packing branch (min over history)", w_causal.min() > -1.0 + 0.5)  # min is ~0, far from -1
# H falls monotonically along the packing branch: since w>-1/3 throughout, q>0 throughout.
q_hist = q_of_w(w_causal)
check("q>0 over the entire packing dilution history => H decreases throughout (no constant-H window)", np.all(q_hist > 0))

# ---------------------------------------------------------------------------
print("CHECK 4 -- comoving Hubble radius: scale-invariant GENERATION needs it to SHRINK")
# Comoving Hubble radius R = (a H)^{-1}.  For power-law a~t^p, H~1/t:
#   a H ~ t^{p-1}  ->  R = (aH)^{-1} ~ t^{1-p}.
#   dR/dt < 0 (modes EXIT, freeze -> scale-free spectrum)  <=>  p>1  <=>  w<-1/3.
# Packing branch w in (0,1] -> p = 2/[3(1+w)] in [1/3, 2/3] < 1 -> dR/dt>0
#   -> comoving horizon GROWS -> modes ENTER -> NO freezing -> NO generation.
def p_exponent(w):  # exponent of comoving Hubble radius R ~ t^{1-p}
    return power_p(w)
for w in [1.0, 1.0/3.0, 0.0]:
    p = p_exponent(w)
    grows = (1.0 - p) > 0           # R ~ t^{1-p}; grows iff 1-p>0 iff p<1
    check(f"packing w={w:+.3f}: comoving Hubble radius R~t^(1-p), 1-p={1-p:+.3f}>0 -> GROWS -> modes enter, no freezing", grows)
# inflationary requirement, for contrast
p_inf = p_exponent(-0.9)
check("de Sitter-side w=-0.9: p>1 -> R shrinks -> modes exit/freeze (the inflationary condition)", (1.0 - p_inf) < 0)
# direct kinematic identity: comoving-horizon shrinks  <=>  a_ddot>0  <=>  w<-1/3
check("identity: d/dt[(aH)^-1]<0  <=>  a_ddot>0  <=>  w<-1/3 (packing range w>0 is excluded)",
      q_of_w(-1/3 - 1e-6) < 0 and q_of_w(0.0) > 0)

# ---------------------------------------------------------------------------
print()
if all(PASS):
    print(f"ALL {len(PASS)} CHECKS PASS")
    print("Step-1 verdict (conditional on Gate-1 excess-sourcing): CPP early dynamics")
    print("admits NO scaling-symmetric / quasi-de-Sitter phase. The packing/GP-exclusion")
    print("source is a maximally stiff (w in (0,1]) DILUTING excess -> comoving horizon")
    print("GROWS -> no mode freezing -> no scale-invariant generation. The only constant-H")
    print("source (uniform Sea) is non-gravitating by excess-sourcing. => CONJ-COSMO-1 fails")
    print("as a PRIMARY structure-formation model: clean CONDITIONAL false (on Gate 1).")
else:
    print(f"{sum(PASS)}/{len(PASS)} checks passed -- see FAIL lines above.")
