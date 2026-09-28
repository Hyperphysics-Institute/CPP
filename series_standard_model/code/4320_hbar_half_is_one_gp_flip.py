#!/usr/bin/env python3
"""4320 -- founder ruling: the Planck-level ZBW is the apogee-to-apogee flip (c04's two Moments per cycle), and one
flip is the action hbar/2, 'an elemental motion of a single GP over a single Moment'.

(1) Action per half-cycle: c04 Def. Level 1 states hbar = E_P t_P per half-cycle; the ruling says hbar/2.
(2) The flip's length on the lattice: reading (i) one GP step (the founder's 4299/4301/4320 wording), reading (ii) one
    PSR at c (4318 sec 2, from 4288's 'light speed at the smallest level').
(3) 4301 re-run with the founder's action quantum as hbar/2 = f1 s t_M (4301 used hbar = f1 s t_M):
    e^2/(4 pi eps0) = N sigma f1 / (4 pi)  and  hbar c = 2 f1 s t_M c = 2 f1 s PSR   ->   alpha = N sigma / (8 pi s PSR),
    and with sigma = s^2 (4301):  alpha = N / (8 pi R),  R = PSR/s.
(4) What N/R means: a volley that covers the PSR sphere one DI-bit per GP (4303) against one that covers a single
    radial line of GPs."""
import numpy as np
alpha = 1/137.035999084

print("(1) action per half-cycle (one flip)")
print("    c04 v2.2 Def. Level 1:  hbar = E_P t_P       -> per full cycle 2 hbar, energy scale E_P")
print("    founder 4320:           hbar/2 per flip      -> per full cycle hbar,   energy scale E_P/2 = hbar/(2 t_P)")
print("    ratio c04/founder = 2: c04's Level-1 action (or its energy per cycle) is restated by a factor 2")

print("\n(2) the flip's length (half-cycle = one Moment)")
for R, lab in [(1e30, "GR-FE-1"), (1e32, "EU")]:
    print(f"    {lab:8s} R = {R:.0e}:  (i) one GP step -> amplitude s/2, CP speed s/t_P = c/R = {1/R:.0e} c;"
          f"   (ii) one PSR -> amplitude {R/2:.0e} GPs, speed c")

print("\n(3) 4301 with hbar/2 = one GP push over one Moment:  alpha = N sigma/(8 pi s PSR) = N/(8 pi R)  (sigma = s^2)")
for R, lab in [(1e30, "GR-FE-1"), (1e32, "EU")]:
    N_new = 8*np.pi*alpha*R; N_old = 4*np.pi*alpha*R
    print(f"    {lab:8s} R = {R:.0e}:  N = 8 pi alpha R = {N_new:.3e} DI-bits per GP per Moment  (4310 had {N_old:.3e}; x2)")

print("\n(4) the size of a GP's volley, in GPs of one PSR")
print(f"    alpha = N/(8 pi R)  ->  N/R = 8 pi alpha = {8*np.pi*alpha:.5f} = 1/{1/(8*np.pi*alpha):.3f}")
for R in [1e30, 1e32]:
    print(f"    R = {R:.0e}:  sphere cover (one DI-bit per GP of the PSR sphere, 4303) N = 4 pi R^2 = {4*np.pi*R*R:.1e}"
          f" -> alpha = R/2 = {R/2:.0e} (x{R/2/alpha:.0e} too strong);   line cover N = R -> alpha = 1/8pi = 1/{8*np.pi:.2f}")
print(f"    measured alpha needs N = R/{1/(8*np.pi*alpha):.3f}: about one DI-bit per {1/(8*np.pi*alpha):.2f} GPs along ONE radius --")
print("    the volley scales with the PSR's LENGTH in GPs, not its area; within a factor 5.45 of a single radial line.")
