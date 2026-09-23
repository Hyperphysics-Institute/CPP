#!/usr/bin/env python3
"""4248 -- the founder's trap (the linear -eCP ZBW-oscillates among the bracelet's +CPs inside the centroid, founders_voice/4248)
against the quark core's pull, at the two physical sizes the corpus carries for the W0 bracelet:
  (i)  4229's reading: W0 scale = hbar c/m_W = 0.0025 fm (fed 4231's 0.4% kick bound and 4233's rate factor);
  (ii) the 600-cell reading: bracelet vertex radius r_B = 0.58779 lattice units (SF-2 Thm W bracelet) x l_unit = 0.589 fm (SS-2).
Energies as Coulomb-like SSV wells, alpha hbar c / r per unit charge; geometric factors of O(1) not resolved."""
a_hc=1.43996  # MeV fm
for lab,rB in [("(i)  Compton reading, 4229", 197.327/80377.), ("(ii) 600-cell reading, SF-2 x SS-2", 0.58779*0.589)]:
    well=a_hc/rB
    print(f"{lab:38s} r_B = {rB:.4f} fm   ring well scale per unit charge = {well:8.1f} MeV")
print()
for d in [0.1,0.35,0.62]:
    print(f"core pull on the linear -eCP at d = {d:.2f} fm:  (2/3) alpha hbar c / d = {(2/3)*a_hc/d:5.1f} MeV")
print(f"SF-2 Prop. activated: |Delta E_centroid| = O(m_e) ~ a few MeV        SS-2: m_d - m_u = 340 - 336 = 4 MeV (the -eCP's binding scale at the core)")
print(f"linear -eCP oscillation scale 0.105 fm (SS-2) vs r_B: (i) {0.105/(197.327/80377.):.0f} x larger than the ring;  (ii) {0.105/(0.58779*0.589):.2f} x the ring -> inside it")
print("""
-> (i)  the ring well (~600 MeV) beats the core (~10 MeV) by ~60x: the trap holds trivially, but a 1-MeV Delta E_centroid (SF-2) is then unexplained.
-> (ii) the ring well (~4 MeV) is the SAME scale as SF-2's Delta E_centroid and as the -eCP's binding to the core: the trap is real
        and marginal, decided by the geometry of the 12 CPs -- and the linear -eCP's whole oscillation fits inside the bracelet,
        which is the founder's 'oscillates inside the centroid' literally. Under (ii) 4231's pocket-kick bound and 4233's rate
        factor, both computed with 0.0025 fm, must be redone (TODO-4248-BRACELET-SCALE).""")
