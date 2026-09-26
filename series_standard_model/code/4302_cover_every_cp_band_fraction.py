#!/usr/bin/env python3
"""4302 -- founders_voice/4302: the covering condition counts CPs in the landing shell (radius PSR, thickness f PSR, f ~ 0.1).
CP densities on file: today's calibrated Sea n_DP = 1.004e-2 per l_P^3 (DE lane, Session 187) -> n_CP = 2 n_DP;
end of inflation n = 1 CP per rest-frame Planck sphere (EU lane, Session 198); black-hole packing ~ 1 CP per PSR^3 (order).
alpha relation (4301): alpha = N s/(4 pi PSR), N = DI-bits per GP per Moment, s = GP spacing."""
import numpy as np
alpha=1/137.035999; f=0.1
print("(1) CPs in the landing shell 4 pi PSR^2 x f PSR (f = 0.1), i.e. the DI-bits needed to give each one a DI-bit:")
for lab,n in (("today's Sea (2 x 1.004e-2 per l_P^3)",2*1.004e-2),("end of inflation (1 per Planck sphere)",1/(4/3*np.pi)),("black-hole packing (~1 per PSR^3)",1.0)):
    print(f"  {lab:40s}: {4*np.pi*f*n:.3f} CPs in the shell")
print("  -> at every density on file the shell holds of order one CP or fewer; covering every CP needs N of order 1.")
print("     The conception is consistent (no over-emission), but it does not set N ~ 1e29-1e31 (4301).")
print("\n(2) what alpha's N is, in GP layers: N = 4 pi alpha (PSR/s) =", f"{4*np.pi*alpha:.4f} x (PSR/s)")
print("    the 10% band spans 0.1 PSR/s GP layers. If a GP emits ONE DI-bit per GP layer across a band of fraction f:")
print("      N = f PSR/s  ->  alpha = f/(4 pi)")
for f_ in (0.10,4*np.pi*alpha):
    print(f"    f = {f_:.4f}: alpha = {f_/(4*np.pi):.5f} = 1/{4*np.pi/f_:.1f}")
print("    -> the founder's 'about 10%' band gives 1/125.7, within 8% of 1/137.0; alpha = 1/137.036 needs f = 0.0917.")
print("    (recorded with caution: one number against one number; the 'one DI-bit per layer' rule is not on file)")
