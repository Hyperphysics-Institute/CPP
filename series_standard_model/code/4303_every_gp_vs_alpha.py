#!/usr/bin/env python3
"""4303 -- founders_voice/4303: one DI-bit for every GP on the PSR sphere (spread over the 10% band).  Against 4301's
alpha = N s/(4 pi PSR) (N = DI-bits per GP per Moment; the force/mass conversions cancel, also when a CP's displacement is
the net fraction of its arrivals).  R = PSR/s = GP layers per PSR."""
import numpy as np
alpha=1/137.035999; f=0.1
for lab,R in (("GR-FE-1: R = 1e30",1e30),("EU: R = 1/9.9e-33",1/9.9e-33)):
    Na=4*np.pi*alpha*R; Nsurf=4*np.pi*R*R; Nband=4*np.pi*f*R**3
    print(f"{lab:20s}: alpha needs N = {Na:.2e} = one DI-bit per GP LAYER of a 9.2%-deep band")
    print(f"{'':20s}  one DI-bit per GP on the sphere's surface: N = {Nsurf:.1e}  ({Nsurf/Na:.0e} x alpha's N)")
    print(f"{'':20s}  one DI-bit per GP in the 10% band:          N = {Nband:.1e}  ({Nband/Na:.0e} x alpha's N)")
    print(f"{'':20s}  alpha that 'every GP in the band' would give: {Nband*1/(4*np.pi*R):.1e}")
print("Every GP in the band over-emits by R^2 ~ 1e60-1e64 relative to alpha under the founder's action quantum (least work")
print("over one Moment); equivalently, if every GP in the band is covered, the action quantum must be ~R^2 least-works.")
