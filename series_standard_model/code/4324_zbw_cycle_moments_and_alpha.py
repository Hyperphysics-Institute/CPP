#!/usr/bin/env python3
"""4324 -- founder (founders_voice/4324): (a) what matters is how many DI-bits land on the GP the CP lands on; 'every
GP had 68 or 69 DI-bits ... over many oscillations ... an average total DI-bit influence of 137 from apogee to apogee';
(b) a two-Moment cycle leaves no time for DP-arcs to store and return energy, so the hbar/2 ZBW cycle is much longer
than two Moments.

General form.  Let the CP's half-cycle (apogee to apogee) take K Moments and travel a path L; the action of the
half-cycle is the sum of its per-Moment actions against the least force: hbar/2 = f1 * L * t_M (4301 extended; 4322
had K = 1, L = PSR).  Coulomb from counting at r = PSR with occupancy c (DI-bits landing on one GP per Moment):
e^2/(4 pi eps0) = c f1 PSR^2 (4323).  c = PSR/t_M.  Then
        alpha = c f1 PSR^2 / (2 f1 L t_M * PSR/t_M) = c * PSR / (2 L).
"""
import numpy as np
alpha = 1/137.035999084

print("(a) the founder's '68 or 69 DI-bits per GP' read PER MOMENT, in 4323's alpha = c/2:")
print(f"    c = 68.5 -> alpha = {68.5/2:.2f}: charge {68.5/2/alpha:.0f}x too strong. 4323 needs c = 2 alpha = 1/68.5,")
print("    i.e. 68.5 is GPs per DI-bit, not DI-bits per GP.  Read PER HALF-CYCLE instead, it is (c) below.")

print("\n(b)/(c) a cycle of M Moments, CP stepping one PSR every Moment (constant speed c, a triangle wave):")
print("    half-cycle K = M/2 Moments, L = (M/2) PSR  ->  alpha = c / M")
for c in [1.0, 0.5]:
    print(f"    occupancy c = {c}: M = c/alpha = {c/alpha:.3f} Moments per full ZBW cycle")
print("    With full covering (c = 1, the founder's 4303 picture): ONE FULL ZBW CYCLE = 1/alpha = 137.04 MOMENTS.")
print("    The CP lands on one GP per Moment holding one DI-bit: 68.5 landings per half-cycle, 137 per cycle --")
print("    the founder's '68 or 69 per ... 137 from apogee to apogee', counted over Moments rather than per GP.")

print("\n    the founder's profile (rest at apogee, fastest at the centre): sampled sine, largest step one PSR")
f = lambda M: np.sin(np.pi/M)/2 - alpha          # c = 1: alpha = PSR/(2L), L = 2A = PSR/sin(pi/M)
lo, hi = 3.0, 1e4
for _ in range(200):
    mid = (lo+hi)/2
    lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
print(f"    c = 1: alpha = sin(pi/M)/2  ->  M = {lo:.2f} Moments per cycle (= 137.04 x pi/2 = {137.036*np.pi/2:.2f} in the limit)")

print("\n(d) the per-Moment action, full covering:")
print("    a = f1 * PSR * t_M;  e^2/(4 pi eps0) = f1 PSR^2  ->  a = e^2/(4 pi eps0 c)  (the charge's own action unit)")
print(f"    hbar = M a  ->  a/hbar = 1/M = alpha = {alpha:.6f}:  hbar is 137 per-Moment actions of one charge (constant speed)")
