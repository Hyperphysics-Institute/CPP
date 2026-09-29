#!/usr/bin/env python3
"""4323 -- founder (founders_voice/4323): the CP at apogee responds to the landing shell; the concentration of DI-bits
per GP in the shell 'could be related to the 1/137 coupling'; with a one-PSR flip the CP would respond to its own
message from its previous apogee, so the timing must be adjusted to respond to the opposite charge's shell.

(1) alpha in terms of the landing concentration c = DI-bits landing on one GP per Moment at r = PSR.
    Target: one CP taking what lands on its own GP (4301's sigma = s^2), full push per DI-bit (p = 1, 4299).
    Force on the target at r = PSR: F = c f1.  Conservation + spreading (4309 sec 2): c(r) = c (PSR/r)^2, so F r^2 is
    constant: Coulomb, with e^2/(4 pi eps0) = F r^2 = c f1 PSR^2.
    Action (4320/4322): hbar/2 = f1 PSR t_M, and c = PSR/t_M  ->  hbar c = 2 f1 PSR^2.
    alpha = e^2/(4 pi eps0 hbar c) = c/2.   No N, no R, no band thickness appear.
(2) What N then is, for the landing geometries on file.
(3) The flip's timing: whose volley does each CP land on?"""
import numpy as np
alpha = 1/137.035999084

print("(1) alpha = c/2, c = DI-bits landing on one GP per Moment in the landing zone at r = PSR")
c = 2*alpha
print(f"    measured alpha needs c = 2 alpha = {c:.6f}: one DI-bit per {1/c:.2f} GPs of the landing zone per Moment")
print(f"    full covering (c = 1, founder 4303) gives alpha = 1/2 ({0.5/alpha:.1f}x too strong)")
# numeric check of the chain with arbitrary f1, PSR, t_M
f1, PSR, tM = 3.7, 11.0, 0.9
F = c*f1; k = F*PSR**2; hbar = 2*f1*PSR*tM; cc = PSR/tM
print(f"    chain check (arbitrary f1, PSR, t_M): e^2/(4 pi eps0 hbar c) = {k/(hbar*cc):.6f}  vs  c/2 = {c/2:.6f}")

print("\n(2) N = c x (GPs in the landing zone): the landing geometry decides N, not alpha")
for R in [1e30, 1e32]:
    surf = 4*np.pi*R**2
    band = 4*np.pi*R**2*(0.019*R)          # 4309: rms relative width 1.9%, as the band's depth in GPs
    print(f"    R = {R:.0e}: one-GP-deep surface ({surf:.1e} GPs): N = {c*surf:.2e}   (4322's 8 pi alpha R^2)")
    print(f"               2% band volume   ({band:.1e} GPs): N = {c*band:.2e}   (R returns through the band's depth)")

print("\n(3) the symmetric one-PSR flip (4318 table, M = 2: apogee to apogee = one PSR = the landing radius, 4309)")
A = 0.5                                     # amplitude in PSR
pos = lambda sgn, n: sgn*A*(1 if n % 2 == 0 else -1)
print(f"    {'Moment':>6s} {'+CP at':>7s} {'own last emission':>18s} {'dist':>5s} {'-CP last emission':>18s} {'dist':>5s}")
for n in range(1, 5):
    p_now = pos(+1, n); own = pos(+1, n-1); par = pos(-1, n-1)
    print(f"    {n:6d} {p_now:7.2f} {own:18.2f} {abs(p_now-own):5.2f} {par:18.2f} {abs(p_now-par):5.2f}")
print("    Each CP lands exactly one PSR from its OWN last emission point (on its own landing shell, within the 1.9% band)")
print("    and at distance 0 from its partner's (at the centre of the partner's shell, never on it). A symmetric flip")
print("    couples each CP to its own previous message; reaching the partner's shell needs a different timing.")
