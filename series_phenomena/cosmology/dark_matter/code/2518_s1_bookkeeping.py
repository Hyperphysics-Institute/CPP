#!/usr/bin/env python3
"""Patch 2518 verify: S1 baryon net-CP bookkeeping identity checks.

All inputs are registered structure (relic1_s1_baryon_cp_bookkeeping.md section 1).
Convention: net = (n_qCP, n_eCP), SIGNED unpaired counts per species
(+1 per +CP excess, -1 per -CP excess); all DP-paired content nets to zero
by the registered DP definition (opposite-polarity bound pairs).
Charges: +qCP = +2/3, -qCP = -2/3, +eCP = +1, -eCP = -1, so
charge(net) = (2/3)*n_qCP + 1*n_eCP.
"""

def add(*nets):
    return (sum(n[0] for n in nets), sum(n[1] for n in nets))

def charge(net):
    return net[0] * (2.0 / 3.0) + net[1] * 1.0

# Registered constituents
u = (1, 0)          # cageless; one central +qCP                       [SS-1f, SS-2]
d = (1, -1)         # u + captured -eCP (the linear oscillator)        [SS-2, founders_vision]
htetra = (0, 0)     # 2 hDPs, each an opposite-polarity pair -> net 0  [master_glossary]
electron = (0, -1)

# Nucleons
proton = add(u, u, d, htetra)
neutron = add(u, d, d, htetra)
assert proton == (3, -1) and abs(charge(proton) - 1.0) < 1e-12
assert neutron == (3, -2) and abs(charge(neutron)) < 1e-12
print(f"proton  net = {proton},  charge = {charge(proton):+.3f} (expect +1)")
print(f"neutron net = {neutron}, charge = {charge(neutron):+.3f} (expect  0)")

# Neutral-bulk invariant: (+3, -2) unpaired CPs per baryon
h_atom = add(proton, electron)
he4_atom = add(proton, proton, neutron, neutron, electron, electron)
assert h_atom == (3, -2) and abs(charge(h_atom)) < 1e-12
assert he4_atom == (12, -8) and abs(charge(he4_atom)) < 1e-12
assert (he4_atom[0] / 4, he4_atom[1] / 4) == (3.0, -2.0)
print(f"H atom net = {h_atom}; 4He atom net = {he4_atom} -> per baryon (3, -2): INVARIANT OK")

# DM side, registered at 2435: 8-qCP cube is 4+/4-, 8-eCP shell is 4+/4-
element = (4 - 4, 4 - 4)
ring = (8 * element[0], 8 * element[1])
assert element == (0, 0) and ring == (0, 0)
print(f"DM element net = {element}; N=8 ring net = {ring} -> asymmetry charge ZERO")

# Consequence: a conserved net-CP-sign charge the ring carries none of cannot set n_ring by sharing.
print("S2 candidate (a) net-CP-sign charge sharing: CLOSED-NEGATIVE")
print("ALL CHECKS PASS")
