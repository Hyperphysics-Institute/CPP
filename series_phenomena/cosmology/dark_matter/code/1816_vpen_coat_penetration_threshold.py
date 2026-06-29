#!/usr/bin/env python3
"""
Patch 1816 -- v_pen: the eCP-coat penetration threshold (calc #1 of the collisional program, 1815 sec5).
=====================================================================================================
QUESTION (the phase-space gate). In a transverse Cross-Rod collision, do the qCP cores get driven
THROUGH their mutual eCP coats into contact? If yes, the qq-contact channels open (chain-switching /
glueball / X-bond, mechanisms 3/4/5). If no, the coat holds and the physics is the BENDING fork
(bend-fracture vs crack-arrest, mechanisms 1/2). v_pen is the relative velocity that just reaches qq
contact -- comparing it to dwarf (~30-100 km/s) and cluster (~1000-3000 km/s) velocities PARTITIONS
the whole program, and COMPUTES the open "does the coat hold?" fork rather than guessing it.

ENERGY BALANCE (local per-contact; NO new knobs -- every input is pinned corpus):
  (1/2) mu v_pen^2 = E_barrier     ->   v_pen = sqrt(2 E_barrier / mu)
  - E_barrier = kappa_b * E_ee : the coat barrier traces to the pinned eCP-shell bond E_ee ~ 0.9 MeV
    (the energy scale holding the coat in place; kappa_b ~ O(1), band [0.5,4] for 1..few coat bonds).
  - mu = effective LOCAL colliding mass / 2. The penetration is a fast LOCAL event; only the locally
    impacted material participates (the rest of the rod is causally disconnected on the contact
    timescale). Central: one element pair, mu = m_element/2. Band: qCP-core-only (lighter, higher
    v_pen) .. a few elements (heavier, lower v_pen).
  All masses pinned: m_element = 4 qDP + 4 eDP = 4*264 + 4*88 = 1408 MeV (0886); E_ee from 1813.
"""
import numpy as np
c_kms   = 299792.458
E_qDP, E_eDP = 264.0, 88.0
m_element = 4*E_qDP + 4*E_eDP          # 1408 MeV  (8 qCP + 8 eCP = 4 m_hTetra; 0886)
m_qcore   = 4*E_qDP                    # 1056 MeV  (qCP core only)
E_ee      = 0.9                        # MeV  eCP-shell bond (1813 central)

def v_pen(E_barrier, mu):              # MeV, MeV -> km/s   (v/c = sqrt(2E/mu), non-rel)
    return np.sqrt(2*E_barrier/mu) * c_kms

print("="*72)
print("v_pen -- eCP-coat penetration threshold (does the coat hold at DM velocities?)")
print("="*72)
print(f"  pinned: m_element={m_element:.0f} MeV  m_qcore={m_qcore:.0f} MeV  E_ee={E_ee} MeV")
print(f"  v_pen = sqrt(2*kappa_b*E_ee / mu)\n")
print(f"  {'mu model':<26} {'mu[MeV]':>8} | " + " | ".join(f"kb={kb}" for kb in (0.5,1,2,4)))
rows = [("1 element pair (central)", m_element/2),
        ("qCP-core pair (light)",    m_qcore/2),
        ("4-element (heavy)",        2*m_element)]
allv=[]
for name,mu in rows:
    vs=[v_pen(kb*E_ee, mu) for kb in (0.5,1,2,4)]
    allv+=vs
    print(f"  {name:<26} {mu:>8.0f} | " + " | ".join(f"{v:7.0f}" for v in vs))
vlo,vhi=min(allv),max(allv)
vcen=v_pen(E_ee, m_element/2)
print(f"\n  CENTRAL (1 element pair, kappa_b=1): v_pen = {vcen:.0f} km/s = {vcen/c_kms:.4f} c")
print(f"  full O(1) band: v_pen ~ {vlo:.0f} - {vhi:.0f} km/s")

print("\n  Compare to dark-matter relative velocities:")
for env,v in (("dwarf",60),("galaxy",250),("cluster (typ)",2000),("cluster (Bullet-like)",4000)):
    print(f"    {env:<22} v_rel ~ {v:>5} km/s   ->  v_pen/v_rel = {vcen/v:6.0f}x  (coat {'HOLDS' if vcen>v else 'PENETRATED'})")

print("\n" + "="*72)
print("VERDICT: v_pen ~ 15,000 km/s central (full O(1) band 5,400-35,000 km/s). Central is ~8x")
print("above typical cluster (~2000) and ~4x above Bullet-like (~4000); only the doubly-pessimistic")
print("corner (heaviest local mass AND weakest barrier) drops to ~5,400 km/s, still >Bullet but by")
print("only ~1.3x. => THE eCP COAT HOLDS dwarf->typical-cluster; qq-contact channels (chain-")
print("   switching/glueball/X-bond, mech 3/4/5) are velocity-SUPPRESSED dwarf->typical-cluster")
print("   (marginal only in the most extreme Bullet-like collisions at pessimistic O(1)).")
print("=> The operative collisional regime is the BENDING fork (mech 1/2): bend-fracture vs")
print("   crack-arrest. That is calc #2 -- the v_pen gate has selected the branch to compute next.")
print("Consistency w/ 0860: whole-rod bending energy (collective, lever-arm amplified) CAN reach")
print("the bond scale at cluster v, while LOCAL per-contact penetration cannot -- so fragmentation,")
print("if it happens, is by BENDING at the outer-fiber E_ee, not by local qq penetration. Coherent.")
print("="*72)
