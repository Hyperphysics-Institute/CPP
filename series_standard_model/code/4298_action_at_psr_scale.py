#!/usr/bin/env python3
"""4298 -- founders_voice/4298: does the weakest centripetal acceleration at a PSR radius set the smallest unit of action?
Corpus units (master_glossary): Moment = Planck time t_P; PSR = displacement per Absolute Moment (base: Planck length),
shrinking with SSV_abs; a CP displaces at most one PSR per Moment (speed c).  GP lattice: nested 600-cells
(founders_vision sec 2)."""
import numpy as np
hbar=1.054571817e-34; c=299792458.0; G=6.67430e-11; me=9.1093837015e-31; eV=1.602176634e-19
lP=np.sqrt(hbar*G/c**3); tP=lP/c; mP=np.sqrt(hbar*c/G); pP=mP*c; EP=mP*c*c; rC=hbar/(me*c)
print(f"(1) lattice units: PSR = l_P = {lP:.4e} m, Moment = t_P = {tP:.4e} s, one PSR per Moment = c")
print(f"    centripetal acceleration on a circle of radius one PSR at one PSR per Moment: a = c^2/l_P = {c*c/lP:.3e} m/s^2")
print("    -> this is the LARGEST (a CP cannot step faster). A weaker one means a slower CP, v^2/l_P. Landing is GP-quantised")
print("       and GPs sit at a finer, sub-Planck spacing (xi2_relay_computation l.172; SR-1 Patch 0736), so the smallest")
print("       nonzero step is one GP spacing: a minimum speed and a minimum centripetal acceleration do exist.")
print("       Their values depend on that spacing (not evaluated here). Either way, the next rows show they fix no action.")
print("\n(2) acceleration is not action. Angular momentum = momentum x radius; the lattice gives the radius, not the momentum:")
for lab,p in (("electron-scale CP, m_e c/3",me*c/3),("whole electron, m_e c",me*c),("half the Planck momentum",pP/2),("Planck momentum",pP)):
    print(f"  {lab:28s}: L at one PSR = {p*lP/hbar:.3e} hbar")
print(f"  -> hbar/2 at one PSR needs p = hbar/(2 l_P) = m_P c/2, energy {EP/2/eV/1e9:.2e} GeV = {EP/2/(me*c*c):.2e} m_e c^2")
print(f"  -> at electron-scale momentum hbar/2 needs radius hbar/(2p): p = m_e c/3 -> {1.5:.2f} r_C = {1.5*rC/lP:.2e} PSR")
print("\n(3) what the lattice DOES supply: a natural unit of action, hbar = p_P l_P = E_P t_P (one Planck energy for one Moment).")
print("    The half: smallest closed loops of one-PSR steps, momentum along each step, L = p x apothem:")
for name,N in (("triangle (600-cell face)",3),("square (cubic lattice -- NOT the corpus lattice)",4),("pentagonal ring (icosahedral vertex figure)",5)):
    ap=0.5/np.tan(np.pi/N)
    print(f"  {name:48s}: apothem {ap:.4f} PSR  ->  L = {ap:.4f} p l_P" + ("   (= hbar/2 with p = p_P)" if abs(ap-0.5)<1e-12 else ""))
ap=(np.sqrt(3)/2)/2   # rhombus of two unit equilateral triangles: inradius = area/(2 a) = (sqrt3/2)/2
print(f"  {'rhombus of two triangles (600-cell 4-step loop)':48s}: inradius {ap:.4f} PSR  ->  L = {ap:.4f} p l_P")
print("  -> only a regular square gives exactly 1/2; the 600-cell's faces are triangles and its loops give 0.289, 0.433, 0.688.")
print("\n(4) the size-independence test: measured angular momentum comes in hbar/2 steps for an electron and for a bowling ball")
print("    alike. A minimum set at one radius by one acceleration gives L proportional to the momentum there, not a fixed lump.")
