#!/usr/bin/env python3
"""4205 -- the measured neutron-decay correlation coefficients (targets), and the crudest one-axis
prediction of the inheritance model (P2, founder-ratified at 4205) for the electron asymmetry A.
SM:  lam = g_A/g_V = -1.2754;  a = (1-l^2)/(1+3l^2);  A = -2 l(l+1)/(1+3l^2);  B = 2 l(l-1)/(1+3l^2).
P2 one-axis: electron spin = departed d-quark sense, parallel to neutron spin with probability P;
ejection rule sends the electron AGAINST its spin at v/c -> A_P2 = -(2P-1) (at v/c = 1)."""
l = -1.2754; D = 1 + 3 * l * l
print(f"measured/SM targets: a = {(1-l*l)/D:+.3f}   A = {-2*l*(l+1)/D:+.3f}   B = {2*l*(l-1)/D:+.3f}")
for name, dq in (('SU(6) quark model, Delta-d(neutron) = 4/3', 4/3), ('measured spin fractions, Delta-d(neutron) = Delta-u(proton) = 0.84', 0.84)):
    P = (1 + dq / 2) / 2
    print(f"{name:70s} P(d parallel) = {P:.2f}  ->  one-axis A_P2 = {-(2*P-1):+.2f}")
print("\nmeasured A = -0.118: sign agrees; magnitude 3.5-5.5x too large in the one-axis reading.")
print("B: P2 GT channel puts the antineutrino spin along the neutron spin and ejects it along its spin -> B large positive (measured +0.987): sign agrees.")
