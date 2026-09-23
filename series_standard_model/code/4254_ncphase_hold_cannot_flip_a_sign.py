#!/usr/bin/env python3
"""4254 -- TODO-4246-NCPHASE: can the founder's 'W0 holds the arc energy for one Moment' (4240 element 3) supply the
bare-core sign as a phase of the direct-transit amplitude (reading R2)? A delay t adds a phase E t/hbar."""
import math
hbar_MeVs=6.582119569e-22; c=2.998e23  # fm/s
t_P=5.391e-44; m_W=80379.0; r_B=0.58779*0.589
for lab,t in [("one Moment (Planck time)",t_P),("the W0's own time hbar/m_W",hbar_MeVs/m_W),("light-crossing of the ring 2 r_B/c",2*r_B/c)]:
    for E in [1.0,10.0,100.0]:   # electron energy scale, MeV
        print(f"  hold = {lab:34s} E = {E:5.1f} MeV: phase E t/hbar = {E*t/hbar_MeVs:.2e} rad")
E_Qweak=1160.0; print(f"  hold = light-crossing, Qweak beam E = {E_Qweak:.0f} MeV: phase = {E_Qweak*2*r_B/c/hbar_MeVs:.2f} rad")
print("  -> a sign needs a constant phase pi. The Planck-Moment and hbar/m_W readings give <= 1e-5 rad; the ring light-crossing gives an")
print("     ENERGY-DEPENDENT phase (3e-3 rad at 1 MeV, 4 rad at the Qweak beam energy) -- but Q_W keeps one sign from Cs (eV) to Qweak")
print("     (1.16 GeV), so an energy-dependent phase is excluded by data. The hold cannot supply the bare-core sign on any reading.")
print("\nwhat is left, both readings:")
print("  R1 (4216, displacement rule): the input is the release primitive (against spin, ONESIGN); at an occupied centroid the NC act IS a")
print("     release -> against; the bare core's direct transit is its exchange partner -> along. CC/NC relative sign DERIVED. Load-bearing:")
print("     exchange antisymmetry applied to a push weight.")
print("  R2 (amplitudes): the input is the sign of the direct amplitude relative to photon exchange (a coupling sign); the d sign follows by")
print("     exchange. CC/NC relative sign is then an input, as it was at 4216 (measured Q_W). No phase mechanism available.")
print("  Either way: ONE sign + Fermi statistics + capacity one give all of Q_W's isospin part. R1 is adopted as working (more economical,")
print("  and it explains 4216's finding that the captured object carries the CC sign); R2 stays on record as the critic's frame.")
