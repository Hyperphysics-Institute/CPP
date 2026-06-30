#!/usr/bin/env python3
"""
Patch 1836 -- the floor verdict reduces to a SCALE-FREE ratio g, unified with the corpus edge-bond SSV potential.
================================================================================================================
Running the "full kappa_theta" converges on the corpus's OWN edge-bond SSV near-cancellation -- the G1 make-or-
break flagged in the 25 June handover (handovers/2026-06-25_..._edge_bond_ssv_deciding_calc.md), which decides
"whether the entire DM candidate lives." The X-junction dihedral stiffness kappa_theta IS that same qq-edge-bond
angular stiffness -- the residual of (closer like-charge repulsion) - (farther opposite-charge screening) -- the
same potential that sets the ribbon persistence length ell_p (~100-700 fm) and the per-rung E_ee.

KEY MOVE: the floor flexibility test (1830) is kappa_theta < 3B/L_arm. Since kappa_theta (scissor) and B (arm
bend) are the SAME edge-bond potential in two geometries, write g = kappa_scissor/kappa_bend; with B = kappa_bend
* l_rung (worm-like chain) and L_arm = (N/2) l_rung, the test becomes:

    g  <  6/N

SCALE-FREE: the absolute stiffness, kT_form, ZBW frequency/amplitude, AND the static-vs-dynamic (Earnshaw)
sign question ALL CANCEL in g -- whatever stabilizes the bend stabilizes the scissor the same way (same bond).
Only the GEOMETRY ratio survives. Thomas's read (perpendicular crossing -> off-hinge charges farther apart than
the in-line ribbon bend; stiffness ~ gradient^2 -> farther = softer) gives g ~ 0.06-0.30, below g_crit=0.43 at
the floor-setting N~14 arms -> hinge flexible -> floor ~0.4-0.8 -> VIABLE.
"""
import numpy as np
sm0=3.1
print("floor verdict: g = kappa_scissor/kappa_bend  <  g_crit = 6/N")
for N in (8,14,28):
    print(f"  N={N:3d}: g_crit = {6/N:.2f}")
print("\nThomas perpendicular-crossing read -> g (scissor softer than in-line bend, gradient^2 falloff):")
for rr,p in [(1.5,3),(2.0,3),(2.0,4),(2.5,3)]:
    g=(1/rr)**p; print(f"  sep-ratio {rr}, grad-power {p}: g~{g:.2f}  {'FLEXIBLE' if g<0.43 else 'marginal'}")
print(f"\n=> g ~ 0.06-0.30 < g_crit(N=14)=0.43 -> flexible -> drop 1/8-1/4 -> floor ~{sm0/8:.2f}-{sm0/4:.2f} VIABLE")
print()
print("Why this is robust where 1833/1834 were not:")
print("  - 1833 static absolute kappa: bounced (near-cancellation, geometry-sensitive).")
print("  - 1834 Earnshaw: static FULL config unstable -- but the edge-bond BEND coordinate is RESTORING")
print("    (corpus G1: screened near-cancellation), and that sign question CANCELS in the ratio g anyway.")
print("  - 1836 ratio g: independent of absolute scale, kT, ZBW params, and the stabilization mechanism.")
print()
print("UNIFICATION: DM cluster floor, ribbon ell_p, per-rung E_ee = ONE edge-bond SSV potential (G1, still")
print("open, SF-2/SF-5 lane). Definitive g = that potential in scissor-vs-bend geometry. Anchored estimate: VIABLE.")
