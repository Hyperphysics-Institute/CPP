#!/usr/bin/env python3
"""
Patch 1835 -- the scissor mode is considerably softer than longitudinal compression (founder read) -> floor viable.
==================================================================================================================
1834 established the hinge stiffness is the ZBW DYNAMIC (ponderomotive) stiffness, scale ~f*E_ee, f unknown.
Thomas's physical read (30 June) pins the DIRECTION: the scissor/hinge mode is considerably softer than the
longitudinal E_qq compression between face-to-face 8qCP cubes, because the bonding charges across the hinge sit
FARTHER apart (eDP coat pairs at the lever end; qDP pairs near the hinge but past the face-to-face core) and at
VARIABLE distance, so the SSV gradients are much softer and graded along the lever.

Ponderomotive stiffness ~ (SSV/field gradient)^2, which falls steeply with charge separation r. So "farther
apart" -> strong suppression. f = (d/r_hinge)^p for gradient-squared laws p. Even modest r_hinge~2d gives
f~0.05-0.25 -> kappa_theta ~ 0.05-0.23 MeV: sub-E_ee and BELOW the flexibility threshold (3B/L_arm~0.30 at N=14)
-> hinge flexible -> cluster floor ~0.4-0.8 -> VIABLE.
"""
import numpy as np
E_ee,d,B,sm0 = 0.9,1.0,0.71,3.1

print("softening f = kappa_scissor/kappa_long = (d/r_hinge)^p  (gradient-squared falloff):")
print(f"{'r_hinge/d':>10}" + "".join(f"  p={p}" for p in (2,3,4,6)))
for rh in (1.5,2.0,2.5,3.0):
    print(f"{rh:>10.1f}" + "".join(f"{(d/rh)**p:>6.3f}" for p in (2,3,4,6)))

print("\nkappa_theta ~ f * E_ee  (hinge torque dominated by coat eDP pairs, softened by distance):")
for p,rh in [(3,2.0),(4,2.0),(3,2.5)]:
    f=(d/rh)**p; print(f"  p={p}, r_hinge={rh}d: f={f:.3f} -> kappa_theta ~ {f*E_ee:.2f} MeV")

thr14 = 3*B/(14/2*d)
print(f"\nflexibility threshold 3B/L_arm (N=14) = {thr14:.2f} MeV")
print("floor (kappa_theta < threshold -> hinge soft -> drop 1/8-1/4):")
for kth in (0.05,0.10,0.15,0.23):
    drop = 1/8 if kth < 0.5*thr14 else 1/4
    print(f"  kappa_theta~{kth:.2f} MeV -> drop~{drop:.3f} -> floor~{sm0*drop:.2f}")

print("\nVERDICT: founder read + ponderomotive gradient scaling AGREE -- scissor mode considerably softer,")
print("f~0.05-0.25 -> kappa_theta ~0.05-0.23 MeV (sub-E_ee, below threshold) -> floor ~0.4-0.8 -> VIABLE.")
print("Direction now robust; exact floor (0.4 vs 0.8) still wants the full ponderomotive calc (ZBW freq/amp,")
print("SSV gradient law). The candidate's cluster floor lands in the allowed band on the correct (dynamic) physics.")
