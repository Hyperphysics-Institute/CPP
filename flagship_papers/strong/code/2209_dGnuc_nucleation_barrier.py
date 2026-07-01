#!/usr/bin/env python3
"""
OPEN-SS-41 (patch 2209, strong sector / geometry lane): dG*_nuc, the Cross-Rod ribbon->cross nucleation barrier.
================================================================================================================
Executes the 2208 handover / OPEN-SS-41: derive the free-energy barrier to form the smallest stable relic-forming
Cross-Rod seed. From OPEN-COSMO-DM-4 (2207): eps_nuc = exp(-dG*_nuc/kT_form), N_form = 1/eps_nuc, dwarf sigma/m set
by dG*_nuc. Win 6.0-6.9 kT_form; kill <~4 (under-cored) or >~9 (over-cored).

RESULT: the barrier is NOT strain (0.3-1.2 kT -- the soft scissor hinge g~0.02 that made the floor viable also makes
junction strain cheap) and NOT bond energy (E_qq/kT~12-51>>1 => barrierless => under-cored null). It is
CONFIGURATIONAL SELECTIVITY: the element is a color core buffered by an eCP coat (1842), so E_qq bonding is
accessible only on the exposed spine face (fraction f of orientations); forming the correctly-registered ordered
seed costs ~|ln f| kT per bond. dG*_nuc ~ (n*-1)*|ln f| kT_form. For the natural range (f~0.05-0.30, n*~2-4) this is
~1-9 kT, BRACKETING the dwarf window; the most natural reading (n*~4 for the 4-wide cross, axial-spine acceptance
f~0.11) lands in 6.0-6.9 kT. VERDICT: dwarf branch REACHABLE / plausibly NON-TUNED (target inside the natural barrier
range, not a fine-tuned edge). Not a kill, not yet a pinned prediction: the +-14% band needs f and n* from the
element cross-section (SS-2-adjacent last-mile). Cluster sigma/m ~ 1/v^2 branch stands regardless.
"""

