#!/usr/bin/env python3
"""4304 -- founders_voice/4304: N = 4 pi (PSR_min/s)^2 (one DI-bit per GP on a one-GP-deep surface at the smallest PSR).
With 4301's conversion-free relation alpha = N s/(4 pi PSR):  alpha = PSR_min^2 / (s PSR)."""
import numpy as np
alpha=1/137.035999; lP=1.616255e-35
print("alpha = N s/(4 pi PSR) with N = 4 pi (PSR_min/s)^2  ->  alpha = PSR_min^2/(s PSR)  ->  PSR_min = sqrt(alpha s PSR)")
for lab,R in (("GR-FE-1: PSR/s = 1e30",1e30),("EU: PSR/s = 1/9.9e-33",1/9.9e-33)):
    s=1.0/R   # in PSR units
    for name,pm in (("register floor l_P/2 (3367)",0.5),("packing floor PSR_min = s",s)):
        N=4*np.pi*(pm/s)**2; a=N*s/(4*np.pi)
        print(f"  {lab:24s} {name:30s}: N = {N:.1e}  alpha = {a:.1e}")
    pm=np.sqrt(alpha*s); print(f"  {lab:24s} alpha = 1/137 needs PSR_min = {pm:.2e} PSR = {pm*R:.1e} GP spacings = {pm*lP:.1e} m;  N = {4*np.pi*(pm/s)**2:.1e}")
print("  -> alpha = 1/137 puts the black-hole PSR at ~1e-16 of the ordinary PSR: sqrt(alpha) x the geometric mean of s and PSR.")
print("     Neither floor on file (l_P/2; one GP) gives it: they miss by ~1e29 and ~1e-30.")
print("Spread through the 10% shell: a fraction N/(4 pi x 0.1 R^3) of the band's GPs receives a DI-bit per Moment:")
for R in (1e30,1/9.9e-33):
    N=4*np.pi*alpha*R; print(f"  R = {R:.1e}: occupancy = {N/(4*np.pi*0.1*R**3):.1e} per Moment (alpha-consistent N)")

print("\nThe band is DERIVED on file (pass 3, Patch 3135, founder's fanout rule): sigma_r/<r> = 0.093-0.076 for N = 6-22 hops,")
print("~0.096 at moderate hop counts. Under 4302's per-layer reading alpha = f/(4 pi):")
for f_ in (0.096,0.093,0.0917,0.076):
    print(f"  f = {f_:.4f}: alpha = 1/{4*np.pi/f_:.1f}")
print(f"  alpha = 1/137.036 needs f = 4 pi alpha = {4*np.pi*alpha:.5f}: inside the derived range, 1.4% from 0.093, 4.7% from 0.096.")
print("  (caveats: 'one DI-bit per layer' is a construction; sigma_r vs full width differ by ~2.4x; the physical hop count is open)")
print("Founder's PSR_min calibration and the per-layer rule agree iff 4 pi (PSR_min/s)^2 = f PSR/s, i.e. PSR_min = sqrt(f s PSR/4 pi).")
