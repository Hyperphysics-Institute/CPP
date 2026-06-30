#!/usr/bin/env python3
"""
Patch 1831 -- the founder's edge-hinge junction mechanism: corrects the 1830 category error.
============================================================================================
Thomas's junction-formation sequence: two velocity-qualified rods strip a single eDP each, the 8qDP
cores appose at 90deg, the cores do NOT fracture (energy wall), no glueball reorganization (sub-fracture
energy), and a SINGLE strong qq bond forms between the two EDGES -- a literal hinge, like two hTetras
bonded on apposed qq edges. The rods are too rigid to bend into a full-face 8qCP bond, so they remain
edge-bonded and FREE TO HINGE.

This fixes 1830's category error: 1830 tied the junction ANGULAR stiffness to the BOND DEPTH (modelled it
as a knot, kappa_theta >= E_ee). For an edge-hinge, rotating about the edge does NOT stretch the bond, so
the bond depth (E_qq) sets only the STRETCH stiffness (junction holds, no fragmentation); the HINGE
(dihedral) stiffness is decoupled, set by secondary coat/steric effects (<~ E_ee). The 1830 'tense' lean
rested on the wrong model.
"""
import numpy as np
E_ee, E_qq, m_el, d, w, c = 0.9, 66.0, 1408.0, 1.0, 2.0, 299792.458

print("1) STABILITY: is the rigid face-bond reachable from the hinge?")
print("   Single-edge hinge folds by ROTATING about the edge -> rods go coplanar/side-by-side, not")
print("   stacked face-to-face. Full 8qCP face bond needs TRANSLATION to stack lengths -- unavailable")
print("   from a one-point hinge with rigid rods. Face-bond GEOMETRICALLY INACCESSIBLE -> hinge STABLE.\n")

print("2) SELF-LIMITING: hinge guarantees inertial decoupling (runaway branch closed)")
vthr = lambda b: 2*np.sqrt(E_ee/(b*m_el))*c
N=28
print(f"   collision on an arm backed by arm inertia (N/2={N//2}) -> v_thr={vthr(N//2):.0f} km/s RISES -> stalls")
print(f"   (rigid whole-X backing 2N={2*N} -> v_thr={vthr(2*N):.0f} FALLS = runaway). Hinge => no runaway.\n")

print("3) CLUSTER FLOOR: wide kinematic hinge range; floor set by residual dihedral stiffness")
sm0=3.1
for lab,drop,kap in (("soft hinge (kappa<<E_ee)",1/8,"<0.3"),
                     ("mild bias (kappa~0.4 MeV)",1/4,"~0.4"),
                     ("strong bias (kappa~E_ee)",1/2,"~0.9")):
    tag="OK" if sm0*drop<1.0 else "TENSION"
    print(f"   {lab:26s} drop~{drop:.3f} -> floor~{sm0*drop:.2f} [{tag}] (kappa {kap} MeV)")
print("\n   Floor <~0.8 as long as kappa_theta <~ 0.4-0.5 MeV (sub-E_ee) -- plausible for a geometric")
print("   hinge whose restoring torque is secondary coat/steric, with 1 of 4 eDPs stripped at contact.")

print("\nNET vs 1830: self-limiting SECURED (runaway closed by the hinge), floor moves from '1.0-1.5")
print("tense' back to ~0.8-1.0 (favorable-to-marginal). Make-or-break re-sharpened: the dihedral")
print("restoring torque of a single locally-stripped qq edge-hinge -- a specific, tractable number,")
print("more so than the 4-arm-knot energy 1830 named.")
