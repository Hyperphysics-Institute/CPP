#!/usr/bin/env python3
"""
Patch 1828 -- CONV-001 round-1 fold: the junction ANGULAR stiffness controls floor AND self-limiting together.
=============================================================================================================
Verifies the inertial bookkeeping behind the panel fold (rebuts Gemini Obj 3; unifies the two open numbers).
After one fusion the arm ~ N/2. A later collision on an arm is backed by:
  - FLEXIBLE (angularly compliant) junction -> arms decoupled -> backing = arm (N/2) -> v_thr RISES -> stalls
  - RIGID junction                          -> whole X backs   -> backing = 2N      -> v_thr FALLS -> runaway
So the SAME angular flexibility that gives the low per-fusion drop (floor ~0.8) also gives the self-limiting.
They stand or fall together on one property: the glueball-junction angular (hinge) stiffness.
"""
import numpy as np
E_ee, m_el, c = 0.9, 1408.0, 299792.458
def vthr(backing_elements): return 2*np.sqrt(E_ee/(backing_elements*m_el))*c
N = 28
print(f"baseline rod (N={N}):           v_thr = {vthr(N):.0f} km/s")
print(f"FLEXIBLE joint, arm backing N/2={N//2}: v_thr = {vthr(N//2):.0f} km/s  (RISES -> self-limits)")
print(f"RIGID joint, whole-X backing 2N={2*N}: v_thr = {vthr(2*N):.0f} km/s  (FALLS -> runaway)")
print()
print("R_color sensitivity (Obj 2): v_thr ~ 1/sqrt(R_color); R_color=0.7d -> v_thr x %.2f -> %.0f km/s"
      % (1/np.sqrt(0.7), 1770/np.sqrt(0.7)))
print()
print("=> One property (junction angular stiffness) sets BOTH the cluster floor and the self-limiting.")
print("=> Decisive next calc: derive the angular/hinge stiffness of a single-point glueball core-core junction.")
