#!/usr/bin/env python3
"""4216 -- TODO-4214-ONESIGN item 3: is the neutral-current drift the SAME sign as the charged-current throw?
Charged current (4201): a lepton of label q leaves along  q * (own spin).   Electron q = -1: against spin.
Neutral current (4196, standard form H = G_F Q_W/(2 sqrt2 m c) {sigma.p, rho}/2):
    v_extra = [G_F Q_W(partner) rho /(2 sqrt2 m c)] sigma   for an ELECTRON probe; a positron probe flips.
    => v_extra along  -q_probe * Q_W(partner) * sigma.
One primitive requires the neutral-current weight to be POSITIVE, i.e. the contact weight is  -Q_W(partner).
"""
phi = (1+5**0.5)/2; s2 = 3/(8*phi)
QW = lambda T3, Q: 2*T3 - 4*Q*s2
core = QW(.5, 2/3); osc = QW(-.5, -1/3) - core
print("charged current:  electron thrown AGAINST its spin (q = -1).")
print(f"neutral current:  drift along -q*Q_W*sigma;  Q_W(neutron) = {3*core+2*osc:+.3f}  ->  electron drifts AGAINST its spin.  SAME sign.")
print(f"                  Q_W(proton)  = {3*core+osc:+.4f}  ->  along its spin, weakly (the cores win by 0.07).")
print(f"\nso the contact weight in the displacement rule is -Q_W(partner):")
print(f"   per linear oscillator (captured -eCP): {-osc:+.3f}    per +qCP core: {-core:+.3f}")
print("The linear oscillator -- the object the W captures -- carries the POSITIVE weight in both currents.")
print("Caesium: Q_W measured -72.6 (negative), sign of E_PNC as predicted by the standard form: the input sign is measured, not assumed.")
