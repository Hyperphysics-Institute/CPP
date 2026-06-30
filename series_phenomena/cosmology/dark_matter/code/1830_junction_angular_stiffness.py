#!/usr/bin/env python3
"""
Patch 1830 -- the coupled-trio calculation (junction angular stiffness leg, decisive).
======================================================================================
The cluster floor and the self-limiting both hinge on whether the glueball junction is angularly
FLEXIBLE. Round 1 ASSUMED flexible (drop ~1/8 -> floor ~0.8). This computes the criterion.

A junction acts as a HINGE (flexible) iff pivoting it is cheaper than bending the arm it joins:
    kappa_theta < 3 B / L_arm
where B is the arm's flexural rigidity (E_ee shell, the bending layer) and L_arm = (N/2) d.

RESULT (unfavorable-leaning): the threshold 3B/L_arm ~ 0.15-0.53 MeV for the relevant arms (N=28..8)
is BELOW E_ee. The natural junction scale (>= E_ee ~ 0.9 MeV; up to E_qq ~ 66 MeV if color-continuous)
EXCEEDS it. So the junction leans RIGID-to-MARGINAL, not clean-flexible -> per-fusion drop ~1/3-1/2
-> cluster floor ~1.0-1.6 cm^2/g (mild-to-moderate tension), NOT the assumed 0.8.
"""
import numpy as np
E_ee, E_qq, d, w = 0.9, 66.0, 1.0, 2.0   # MeV, MeV, fm, fm

I_area = (np.pi/4)*(w/2)**4              # fm^4, area moment for width w
B = (E_ee/d**3)*I_area                   # MeV*fm, arm flexural rigidity (shell)
print(f"arm flexural rigidity  B = {B:.2f} MeV*fm  (E_ee shell, I={I_area:.2f} fm^4)")
print(f"{'N':>4}{'L_arm(fm)':>10}{'3B/L (MeV)':>12}{'flexible iff kappa< ':>22}")
for N in (8,14,28,45):
    L=(N/2)*d; print(f"{N:>4}{L:>10.1f}{3*B/L:>12.2f}{'(sub-E_ee)':>22}")
print(f"\nnatural junction scales: E_ee={E_ee} MeV (knot/shell), E_qq={E_qq:.0f} MeV (color-continuous)")
print("=> natural kappa_theta EXCEEDS threshold by ~2x (E_ee) to ~100x (E_qq): leans RIGID/MARGINAL.\n")

sm0=3.1
print("per-fusion drop -> cluster floor (sigma/m_0 ~ 3.1):")
for lab,drop in (("clean-flexible (assumed)",1/8),("marginal kappa~E_ee",1/3),("rigid",1/2)):
    tag = "OK" if sm0*drop<1.0 else "TENSION"
    print(f"  {lab:24s} drop={drop:.3f} -> floor~{sm0*drop:.2f}  [{tag}]")

print("\nmitigations (partial): (i) crossing geometry forbids a continuous perpendicular spine,")
print("  capping kappa_theta well below E_qq; (ii) 3B/L ~ 1/N so SHORT arms are more flexible, and")
print("  self-limiting stops fusion at short arms (N~7-14) -> the late, floor-setting junctions are")
print("  the most flexible. Still needs kappa_theta <~ 0.3-0.5 MeV (sub-E_ee) -- not guaranteed.")
print("\nDECISIVE next: SF-5 angular energy of a 4-arm color knot vs inter-arm angle.")
print("  < ~0.4 MeV -> viable (floor ~0.8);  >= E_ee -> cluster tension stands.")

# --- coupled legs 2 & 3 (sensitivities), same unfavorable direction when pushed ---
print("\n--- leg 2 (R_color): v_thr ~ 1/sqrt(R_color); R_color=0.7d -> v_thr x%.2f -> %.0f km/s"
      % (1/np.sqrt(0.7), 1770/np.sqrt(0.7)))
print("    smaller R_color -> higher v_thr -> less of cluster pop fuses -> HIGHER sigma/m (worse).")
print("--- leg 3 (tail-rate): lower penetrating-tail fraction -> less fusion -> HIGHER sigma/m (worse).")
print("    All three legs, when pushed, move the cluster floor the SAME way: UP, into tension.")
