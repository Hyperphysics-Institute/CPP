#!/usr/bin/env python3
"""4325 -- founder ruling (founders_voice/4325): at the Planck level the CP obeys the same axiom as everywhere -- it moves
the distance of its SSV_net (V_i) each Moment, not light speed; DI-bits travel at light speed and build the PSR shell
each Moment; DP-arcs build up during acceleration and are exhausted during deceleration.

4324's general relation (half-cycle action additive over Moments, hbar/2 = f1 * L * t_M with L the apogee-to-apogee
path; Coulomb at occupancy c): alpha = c * PSR / (2 L).  It contains no speed and no Moment count: any V_i profile with
the same swing L gives the same alpha.  Demonstrated below with several profiles; then what full covering fixes."""
import numpy as np
alpha = 1/137.035999084
PSR = 1.0

def half_cycle(profile, K):
    """per-Moment steps (in PSR, each <= 1 = light speed) for a half-cycle of K Moments"""
    t = (np.arange(K)+0.5)/K
    v = {"constant": np.ones(K), "sine": np.sin(np.pi*t), "slow-ends": np.sin(np.pi*t)**2}[profile]
    return v

print("alpha = c PSR/(2L) for different V_i profiles with the SAME swing L (full covering, c = 1)")
L_target = PSR/(2*alpha)
print(f"   full covering fixes L = PSR/(2 alpha) = {L_target:.3f} PSR apogee to apogee (amplitude {L_target/2:.3f} PSR)")
print(f"   {'profile':>10s} {'peak V_i (c)':>12s} {'Moments/half':>13s} {'Moments/cycle':>14s} {'L (PSR)':>9s} {'alpha':>10s}")
for prof in ["constant", "sine", "slow-ends"]:
    for vmax in [1.0, 0.5, 0.1]:
        # choose K so that the path equals L_target at this peak speed
        K = 2
        while True:
            v = half_cycle(prof, K); v = v/v.max()*vmax
            if v.sum() >= L_target: break
            K += 1
        steps = v*(L_target/v.sum())                   # rescale so L is exact
        a = 1.0*PSR/(2*steps.sum())
        print(f"   {prof:>10s} {steps.max():12.3f} {K:13d} {2*K:14d} {steps.sum():9.3f} {a:10.6f}")
print(f"   measured alpha = {alpha:.6f}: every row, whatever the speed or the number of Moments.")

print("\nwhat is and is not fixed")
print(f"   fixed by alpha at full covering: the swing, {L_target:.2f} PSR = the DP's largest separation at apogee (~{L_target:.0f} l_P)")
print("   NOT fixed by alpha: the number of Moments per cycle (>= 137 at light speed; set by the V_i history,")
print("   i.e. by how fast DP-arcs build up and release) -- the founder's ruling leaves exactly that free.")
print("   At partial occupancy c < 1 the swing shrinks in proportion: L = c PSR/(2 alpha).")
