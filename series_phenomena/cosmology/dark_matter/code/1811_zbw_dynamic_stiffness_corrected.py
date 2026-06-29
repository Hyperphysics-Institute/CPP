#!/usr/bin/env python3
"""
Patch 1811 -- ZBW dynamic stiffness: corrected coordination + the dynamic-stabilization framing.
================================================================================================
Founder corrections (TLA, recorded to founders_vision.md this patch, authorized):
 (1) The 4 eCP ZBW partners of each perimeter eCP are 2 IN-PLANE + 2 AXIAL (one above, one below),
     NOT 4 axial (corrects 0899). So the LONGITUDINAL (scission) coordination is n_axial,e = 2.
 (2) The statistics is NOT a biasing weight: uniform coordination (every eCP=5, every qCP=8) +
     cycle-symmetric oscillation (equal attraction/contraction vs repulsion/expansion at 90/180/270 deg)
     => it averages to a well-defined DYNAMIC STIFFNESS. This is deterministic cycle-averaging
     (ponderomotive / Kapitza / Paul-trap dynamic stabilization), NOT a thermal ensemble -> the
     OPEN-FP-SF-2-eta ensemble framework is confirmed OFF the critical path.
"""
import numpy as np
hbarc=197.3269804; alpha=1/137.035999; coul=alpha*hbarc; WIN=(0.8e-3,2.0)
n_axial=2  # CORRECTED (was 4 in 0899): 2 in-plane + 2 axial(1 up,1 down) + 1 core qCP = 5 partners
print("="*70); print("Corrected coordination -> M and the f_ZBW it implies for in-window"); print("="*70)
print(f"\n  eCP partners (5): 2 in-plane eCP + 2 AXIAL eCP (1 up,1 down) + 1 core qCP")
print(f"  longitudinal (scission) coordination n_axial,e = {n_axial}")
print(f"  M = n_axial * f_ZBW = {n_axial}*f_ZBW ; E_ee = M*(alpha*hbar*c/d)\n")
print(f"  'moderate dynamic stiffness' <=> M ~ O(1).  With n_axial={n_axial}:")
for M in (1.0,1.5,2.0):
    print(f"    M={M:.1f} -> f_ZBW = {M/n_axial:.2f}  (per-bond ZBW binds {M/n_axial*100:.0f}% of static Coulomb depth)")
print(f"  => in-window M~1-2 needs f_ZBW ~ 0.5-1.0 -- natural for a tightly-bound ZBW oscillation,")
print(f"     though it cannot be tiny. (n_axial=2 tightens this vs 0899's n_axial=4 which allowed 0.25.)\n")
print(f"  Window check (M=1, i.e. f_ZBW=0.5): E_ee = alpha*hbar*c/d :")
for d in (1.0,1.5,2.0,3.0):
    e=coul/d; print(f"    d={d:.1f} fm -> E_ee={e*1e3:6.0f} keV  in-window={WIN[0]<=e<=WIN[1]}")
print(f"\n  f_ZBW is now the PONDEROMOTIVE/effective-stiffness fraction of a single ZBW-stabilized")
print(f"  opposite-charge bond -- a deterministic TWO-body cycle-average, computable without the")
print(f"  ensemble framework. Remaining pins: d (geometric) + f_ZBW (two-body ZBW). Both tractable.")
print("="*70)
