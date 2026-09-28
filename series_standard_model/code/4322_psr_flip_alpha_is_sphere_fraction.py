#!/usr/bin/env python3
"""4322 -- founder ruling (founders_voice/4322): the Planck flip moves ONE PSR per Moment (light speed); the action
increments are in V_i; the oscillating ZBW tracks and affects the line of its transit ('no time for radiation in one
Moment, only time for transit').

4301's counting, re-run with the ruling's action quantum:
    Coulomb from counting (4301):   e^2/(4 pi eps0) = N sigma f1 / (4 pi)
    action (4320 + 4322):           hbar/2 = f1 * PSR * t_M     (least force, one PSR of displacement, one Moment)
    light speed (c04, 4288):        c = PSR / t_M
    ->  alpha = e^2/(4 pi eps0 hbar c) = N sigma f1/(4 pi) / (2 f1 PSR t_M * PSR/t_M) = N sigma / (8 pi PSR^2)
    with sigma = s^2 (4301):        alpha = N / (8 pi R^2),   R = PSR/s.
The previous forms: 4301 (hbar = f1 s t_M): alpha = N/(4 pi R); 4320 (hbar/2 = f1 s t_M): alpha = N/(8 pi R)."""
import numpy as np
alpha = 1/137.035999084

print("alpha under the three action quanta (sigma = s^2):")
print("   4301  hbar   = one GP push over one Moment  : alpha = N/(4 pi R)")
print("   4320  hbar/2 = one GP push over one Moment  : alpha = N/(8 pi R)")
print("   4322  hbar/2 = one PSR flip over one Moment : alpha = N/(8 pi R^2)")

f = 2*alpha   # N / (4 pi R^2)
print(f"\n4322: N/(4 pi R^2) = 2 alpha = {f:.6f} = 1/{1/f:.3f}")
print("   i.e. each Moment a GP's volley reaches one GP in", f"{1/f:.2f}", "of the GPs on its PSR sphere")
for R in [1e30, 1e32]:
    N = 8*np.pi*alpha*R**2
    print(f"   R = {R:.0e}: N = 8 pi alpha R^2 = {N:.3e} DI-bits per GP per Moment")
print("   The relation no longer contains R: alpha is a geometric fraction, the same for every GP spacing on file.")

print("\nThe founder's covering condition (4303: one DI-bit per GP of the PSR sphere, N = 4 pi R^2):")
print(f"   4301 form : alpha = R      -> {1e30:.0e}..{1e32:.0e}  (x{1e30/alpha:.0e}..x{1e32/alpha:.0e} too strong)")
print(f"   4322 form : alpha = 1/2    -> x{0.5/alpha:.1f} too strong  (the 10^32 tension of 4301/4303 becomes 1/(2 alpha) = {1/(2*alpha):.1f})")

print("\nEquivalently, a volley that covers, one GP deep, the sphere of radius r_cov (4304's surface reading):")
rc = np.sqrt(2*alpha)
print(f"   N = 4 pi r_cov^2/s^2 -> alpha = r_cov^2/(2 PSR^2) -> r_cov = sqrt(2 alpha) PSR = {rc:.4f} PSR (scale-free)")
print(f"   (4304/4310 under the GP quantum: PSR_min = sqrt(alpha s PSR) = {np.sqrt(alpha/1e30):.1e} PSR at R = 1e30 -- the 1e16 tension)")

print("\nThe Planck ZBW's own track in one Moment (founder: 'tracks and affects the line'):")
for R in [1e30, 1e32]:
    print(f"   R = {R:.0e}: the flip transits {R:.0e} GPs (one PSR); a static charge sits on 1 GP")
print("   The track is the ZBW's footprint; the volley N is every GP's emission (AP-4). They are different objects.")
