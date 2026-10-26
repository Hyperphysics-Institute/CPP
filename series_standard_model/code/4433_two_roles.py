"""Patch 4433 -- founder: each GP emits the integrated sum of the DI-bits received from the GPs at PSR distance (AP-4); gravity is
another SSV_abs signal superimposed on the near cloud's, its GRADIENT bending the electron by the limb difference; each CP's SSV_abs
contribution is weighted by its realness; a neutral DP (both CPs on one GP) contributes zero SSV_net and zero SSV_abs.

Part 1. Gravity through the gradient, not the amplitude: a symmetric near cloud (realness falling with distance from the CP) adds a
        huge SSV_abs at the CP but no gradient there; a distant body adds a tiny SSV_abs and a tiny gradient, which survives.
        Limb difference across one PSR: (S(+PSR) - S(-PSR)) for cloud alone, body alone, and both.
Part 2. A realness-weighted scalar sum relayed by AP-4's summation (4355: lossless, Laplace -> 1/r statics): if only real charge
        counts, the universe's real charges set a baseline, and a body's fractional addition at distance r is
        (N_body / r) / (N_universe / R_universe). Compare with the measured gravitational potential GM/(r c^2) for the Earth (surface)
        and the Sun (at 1 AU): a Sciama/Mach-type coincidence, one universal factor, not a derivation.
"""
import numpy as np
print("Part 1 (SSV_abs and its limb difference at the CP, arbitrary units, PSR = 1):")
def cloud(x):   # symmetric near cloud centred on the CP at x = 0, falling off with distance
    return 1e6/(1 + x**2)
def body(x, D=1e4, N=1e3):   # distant body at x = D, 1/r scalar
    return N/abs(D - x)
for name, f in (("near cloud alone", cloud), ("distant body alone", body), ("both superimposed", lambda x: cloud(x) + body(x))):
    print(f"  {name:20s}: S at CP {f(0.0):.6e}   limb difference S(+1) - S(-1) = {f(1.0) - f(-1.0):+.3e}")
print("  the cloud's huge, symmetric SSV_abs adds nothing to the limb difference; the body's gradient survives the superposition")

print("Part 2 (realness-weighted 1/r sum, universe as baseline; nucleons as the unit of real charge):")
Nu, Ru = 1e80, 4.4e26
G, c = 6.674e-11, 2.998e8
for name, M, r in (("Earth at its surface", 5.97e24, 6.371e6), ("Sun at 1 AU", 1.989e30, 1.496e11)):
    N = M/1.6726e-27
    frac = (N/r)/(Nu/Ru); U = G*M/(r*c**2)
    print(f"  {name:22s}: fractional addition {frac:.2e}   GM/(r c^2) = {U:.2e}   ratio {frac/U:.2f}")
print(f"  the same ratio for both: it is (N_u / R_u)^-1 (m_p / (G/c^2)) = c^2 R_u / (G M_u) ~ {c**2*Ru/(G*Nu*1.6726e-27):.2f} --")
print("  Sciama's 1953 relation G M_u / (R_u c^2) ~ 1, a known order-one coincidence (any M/r sum gives one ratio for all bodies;")
print("  uniform sphere from centre: factor ~2.4). Assumes N proportional to M -- the realness weighting must sum to mass-energy.")
print(f"  In count units the baseline N_u/R_u = {Nu/Ru:.1e} per metre vs one fully real charge at l_P: {1/1.616e-35:.1e} --")
print("  the background outweighs the near cloud ~1e18: the step must use the CP's own share (two roles, required).")
