#!/usr/bin/env python3
"""4253 -- (A) TODO-4251-LKICK: 4231's 'B = +1 by geometry' re-derived with the pivot named. (B) the founder's 4253 answer
on the occupied centroid (switch / pass-through indistinguishable -> mixing) against 4246's premise."""
import numpy as np
hbarc=197.327; r_orb=hbarc/313.0; r_pk_c=hbarc/80379.0; r_B=0.58779*0.589
print("(A) which angular momentum does a kick at the pole change?")
print("  L about the CORE = r_pole x p, |r_pole| ~ r_orb: a kick dp ~ p at the pole changes it by up to |dL|/L ~ 1 -- for ANY pocket size.")
print("  Only a CENTRAL kick (directed at the core) leaves it unchanged; a kick radial about a pocket centred at r_c from the core has")
print("  torque r_c x F: it is small only if |r_c| << r_orb, i.e. the pocket sits AT the core -- the core-in-centroid reading (4247: not the picture).")
print("  L about the POLE's own position: lever arm <= pocket radius -> 4231's ratio. That quantity is not the released L.")
print("  The released object's L is the eDP's mutual spin about the PAIR's centre (4219 clarification, 4229 ledger): lever arm = the eDP's")
print("  half-length, set by the eDP, not by the pocket.")
for lab,r in [("Compton pocket",r_pk_c),("600-cell ring",r_B)]:
    print(f"  4231's ratio at {lab:14s}: r/r_orb = {r/r_orb:.3f} -- irrelevant to L about the core either way.")
print("  -> B = +1 rests on G-EW-SWAP-4228 ('leaves ... carrying the quark's orbital angular momentum unchanged', founder-ratified) and")
print("     4223's h_nubar = 1; 4231's geometric guarantee is withdrawn independent of the bracelet size. TODO-4251-LKICK closed.")
print("\n(B) the occupied centroid: founder -- switch and pass-through are indistinguishable; there would be a mixing.")
print("  Indistinguishable final states add at the amplitude level; for two identical -eCPs the exchange term enters with the Fermi sign.")
print("  That is 4246's premise verbatim: A_d = T_dir - T_ex with T_dir blocked by occupancy (capacity one) -> -1. Founder's reading SUPPORTS it.")
print("  'Releases both' is a different, inelastic event (the down quark would lose its linear -eCP): not the elastic NC process Q_W measures.")
