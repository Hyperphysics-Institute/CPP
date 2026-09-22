#!/usr/bin/env python3
"""4202 -- (a) neutral-lepton count per beta decay under each capture picture; (b) how often a down
quark's spin is parallel to the neutron's spin in the SU(6) quark model (the standard Delta-q values:
proton Delta-u = 4/3, Delta-d = -1/3; neutron by isospin swap)."""
pics = {'P1 (4199): electron captures a Sea DP; core keeps its DP':                    1,
        'P2 (4201): electron takes the quark DP; core refills from the Sea':          1,
        'P3 (founder 4202 as asked): electron captures a Sea DP AND core refills':    2}
print("neutral spinning Sea DPs created per decay (measured: one antineutrino)")
for k, v in pics.items(): print(f"  {v}   {k}")
dq = 4/3                      # neutron: Delta-d = +4/3 over two d quarks
per = dq / 2                  # n_up - n_down per d quark
print(f"\nSU(6): per down quark in a neutron, n_up - n_down = {per:.3f}  ->  P(d spin parallel to neutron spin) = {(1+per)/2:.3f}")
print("P2 predicts the beta electron's spin is that d-quark orbital sense: parallel to the neutron spin 5/6 of the time before ejection.")
