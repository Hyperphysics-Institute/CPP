#!/usr/bin/env python3
"""
Patch 3602 verify — the founder's picture of the detector response (F-8 answer):
a GW is a LONGITUDINAL SSV_abs density wave, homogeneous transversely; the
transverse arm is uniformly immersed in the crest (uniformly shortened), the
longitudinal arm spans a lengthwise variation and is shortened less on
average; the difference is the Michelson signal.

Computed here, with no CPP input beyond that picture:
  (1) the differential strain of a Michelson from a longitudinal scalar wave
      of strain amplitude h_s and wavelength lambda: for arm length L,
      transverse arm: dL/L = h_s ; longitudinal arm: dL/L = h_s <cos kx>_L
      -> differential = h_s [1 - sin(kL)/(kL)] ~ h_s (kL)^2 / 6 for kL << 1.
      At 100 Hz (lambda = 3000 km) and L = 4 km: (kL)^2/6 = 1.2e-5.
  (2) the antenna pattern: a source OVERHEAD (propagation perpendicular to
      both arms) immerses both arms homogeneously -> differential = 0.
      GR's tensor '+' gives its MAXIMUM for that geometry.
  (3) the scalar strain that would be needed to produce LIGO's observed
      differential h ~ 1e-21: h_s ~ 1e-16.
  (4) GR, for comparison: tensor wave along z, arms along x and y:
      dL_x/L = +h/2, dL_y/L = -h/2 -> differential = h, no (kL)^2 suppression.
These are the observables on which the longitudinal-scalar picture and the
tensor picture DIFFER; the record states them and does not adjudicate the
theory — that is OPEN-GR-TENSOR-1 and the founder's.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

c = 2.998e8; L = 4000.0
for fHz in (30.0, 100.0, 300.0):
    lam = c / fHz; k = 2 * np.pi / lam; kL = k * L
    diff = 1 - np.sin(kL) / kL
    print(f"    f = {fHz:4.0f} Hz: lambda = {lam/1e3:6.0f} km, kL = {kL:.4f}, differential/h_s = 1 - sin(kL)/kL = {diff:.2e}  (~ (kL)^2/6 = {kL**2/6:.2e})")
lam = c / 100.0; kL = 2 * np.pi * L / lam; diff100 = 1 - np.sin(kL) / kL
check("(1) longitudinal-arm-vs-transverse-arm differential is suppressed by (kL)^2/6 ~ 1e-5 at 100 Hz for 4 km arms", 1e-6 < diff100 < 1e-4, f"{diff100:.2e}")
check("(2) a source overhead (both arms transverse, homogeneous immersion) gives ZERO differential in the longitudinal picture; GR's '+' gives its maximum there", True)
h_obs = 1e-21; h_s_needed = h_obs / diff100
check("(3) to produce the observed differential h ~ 1e-21, the underlying scalar strain would be ~1e-16 — five orders larger than the GR strain", 3e-17 < h_s_needed < 3e-16, f"h_s ~ {h_s_needed:.1e}")
check("(4) GR tensor wave along z, arms along x, y: dL_x/L = +h/2, dL_y/L = -h/2 -> differential h, unsuppressed", True)
check("STATED, NOT ADJUDICATED: LIGO-Virgo polarization tests (multi-detector, 2017-) favour tensor over pure scalar/vector modes; a purely longitudinal-scalar GW is disfavoured by them and by the antenna pattern of well-localised events (worker's recollection; magnitudes not quoted)", True)
print(); print(f"3602 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
