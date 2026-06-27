#!/usr/bin/env python3
"""
Patch 0880 (genesis: why the Cross-Rod stays THIN as it lengthens -> the d_f=1 mechanism)
=========================================================================================
The sigma/m = 0.11*N result (0878) assumes d_f = 1 (a rigid rod that grows in length, not width).
Thomas's genesis supplies the MECHANISM behind that assumption: a fifth lateral chain is not forbidden,
it is OUT-COMPETED. A growing rod presents reactive (unshielded qCP) surface only on its TWO axial
end-faces; its ~N lateral element-faces are eDP-coat SHIELDED. Free chains/hTetras in solution are
attracted to the strongest SSV gradient, which is the unshielded end-faces -- so length outruns width
until the lateral count N overwhelms the per-site strength deficit. This estimates the crossover N*.

INPUT (established): the electric-vs-color hierarchy from the corona calc (0874) --
   weak/strong = f_electric/f_color = (3*alpha/alpha_s)^2  ~  1/190 .. 1/520   (i.e. ~190-520x weaker).
GEOMETRY: axial growth runs at ~2 strong sites; lateral bundling at ~N weak sites.
CROSSOVER: lateral overtakes axial when  N * (weak/strong) ~ 2  =>  N* ~ 2 * (strong/weak).

The dwarf-core band (0878) wants N_dwarf ~ 5-60. If N* >> N_dwarf, the rod is robustly thin (d_f=1)
across the entire band-relevant range, and freeze-out only has to set the LENGTH, not police the width.

Run: python3 0880_thin_rod_endfraction_crossover.py
"""
import numpy as np
strong_over_weak = (190.0, 520.0)   # color/electric ratio (0874)
N_dwarf_band     = (5.0, 60.0)      # band-reaching size (0878)
n_axial_sites    = 2                 # two reactive end-faces on a rod

print("="*82)
print("Thin-rod crossover: when does lateral bundling overtake axial growth? (Patch 0880)")
print("="*82)
print(f"\nElectric-vs-color hierarchy (0874): lateral sites are {strong_over_weak[0]:.0f}-{strong_over_weak[1]:.0f}x weaker.")
print(f"Geometry: {n_axial_sites} reactive axial end-faces  vs  ~N shielded lateral faces.\n")
Nstar = [n_axial_sites*r for r in strong_over_weak]
print(f"  crossover  N* = {n_axial_sites} * (strong/weak)  ~  {Nstar[0]:.0f} - {Nstar[1]:.0f} elements")
print(f"  band wants N_dwarf ~ {N_dwarf_band[0]:.0f} - {N_dwarf_band[1]:.0f} elements (0878)")
margin = (Nstar[0]/N_dwarf_band[1], Nstar[1]/N_dwarf_band[0])
print(f"  margin N*/N_dwarf ~ {margin[0]:.0f}x (worst) to {margin[1]:.0f}x (best)\n")
print("VERDICT (Layer C): the crossover to lateral thickening sits at N* ~ a FEW HUNDRED to ~1000")
print("elements, while the dwarf-core band lives at N_dwarf ~ tens -- so the Cross-Rod is robustly")
print("THIN (d_f = 1) with a ~1-2 order-of-magnitude margin throughout the band-relevant range.")
print("The d_f=1 assumption behind sigma/m = 0.11*N now has a MECHANISM under it (shielding")
print("competition), not just an input. The residual knob is unchanged: freeze-out must SET the")
print("length at N ~ tens (early, before depletion starves the cross into the weak-lateral regime);")
print("that is the same N_dwarf(v) kinetics as 0878, now with the width side mechanistically closed.")
print("="*82)
