#!/usr/bin/env python3
"""
Patch 0897 -- Q_stiff SCOPING diagnostic: the contact overlap regime (eDP vs qDP).
==================================================================================
Scoping support for series_phenomena/cosmology/dark_matter/qstiff_contact_polarizability_scoping.md.
Q_stiff = alpha_pol(contact)/alpha_pol(free-cloud) for the eDP composite is the single number the
make-or-break reduced to (0896): in-window <=> Q_stiff <~ 0.1. This script computes the one PINNABLE
first-cut diagnostic -- the overlap ratio a/size at the coat hard-core contact -- which grounds the
DIRECTION of the quench (Q_stiff<1 structurally forced for the eDP) without fabricating its MAGNITUDE
(which needs the substrate-thermodynamic / inter-CP-potential framework = OPEN-FP-SF-2-eta).
Run: python3 0897_qstiff_overlap_diagnostic.py
"""
import numpy as np
hbarc = 197.3269804
E_eDP, E_qDP = 88.0, 264.0
a_contact = 1.0   # fm, eDP-coat hard core (corpus); inter-element contact separation

print("=" * 72)
print("Q_stiff SCOPING -- first-cut diagnostic: the overlap regime at contact")
print("=" * 72)
size_eDP = hbarc / E_eDP
size_qDP = hbarc / E_qDP
print(f"\n  eDP Compton size  hbar c/E_eDP = {size_eDP:.2f} fm")
print(f"  qDP Compton size  hbar c/E_qDP = {size_qDP:.2f} fm")
print(f"  contact separation a (coat hard core) = {a_contact:.2f} fm\n")
print(f"  overlap ratio a/size :  eDP = {a_contact/size_eDP:.2f}   qDP = {a_contact/size_qDP:.2f}")
print("  -> qDP: a/size ~ 1.3  (marginal-multipole; London 'marginal at f=0.2', 0835 -- estimate STANDS)")
print("  -> eDP: a/size ~ 0.45 (DEEP OVERLAP; the two eDPs interpenetrate to ~half their own size)")
print("     In deep overlap the free-cloud London/induced-dipole picture is INVALID and the")
print("     polarizability is necessarily QUENCHED (charges cannot freely displace; Pauli/exchange).")
print(f"\n  KEY ASYMMETRY: construction 2's (E_qDP/E_eDP)^6={(E_qDP/E_eDP)**6:.0f}x enhancement assumes the")
print("  SOFT eDP responds as a free cloud -- but the eDP is exactly the one that DEEPLY OVERLAPS at")
print("  contact, so its free-cloud polarizability is the LEAST valid. The enhancement over-counts")
print("  polarizability for the wrong particle. => Q_stiff<1 is STRUCTURALLY FORCED for the eDP,")
print("  grounding Review II's quench in a regime diagnostic rather than an assertion.")
print(f"\n  Threshold to settle (from 0896): in-window <=> Q_stiff <~ 0.1 ; construction 1 <=> ~0.008.")
print("  DIRECTION now grounded (quench real); MAGNITUDE (does it reach <~0.1?) = the framework calc.")
print("=" * 72)
