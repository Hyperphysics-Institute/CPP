#!/usr/bin/env python3
"""4232 -- the energy roadblock test. Two readings of the orbital's 313 MeV:
(alpha) it is the energy of the bound fall-reset-return oscillation in the core's field (configuration energy);
        a DP reset out of the core carries only what the reset kick gives it, and the core's configuration awaits the refill.
(beta)  it is carried by the DP as circulation; a released DP must shed it on the way out.
Test (beta) against the neutron-decay spectrum; state the (alpha) ledger."""
m_n, m_p, m_e = 939.565, 938.272, 0.511
Q = m_n - m_p - m_e
print(f"Q = m_n - m_p - m_e = {Q:.3f} MeV; the antineutrino's energy is bounded by Q (endpoint), mean 0.480 MeV (4204).")
print(f"(beta) predicts a released orbital carrying ~313 MeV: exceeds the endpoint by a factor {313/Q:.0f}. REFUTED by the spectrum.")
print(f"(alpha) ledger: core configuration energy ~313 MeV stays at the core (rebuilt by the refill half; m_u ~ m_d at constituent level),")
print(f"        the linear -eCP's release supplies m_n - m_p = {m_n-m_p:.3f} MeV, of which {m_e} goes to the electron's rest mass and {Q:.3f} MeV")
print(f"        is shared continuously by electron and antineutrino KE. Antineutrino rest energy (SF-4, cage eigenmodes) ~5e-8 MeV,")
print(f"        i.e. {5e-8/313:.0e} of the orbital's bound energy: the neutrino's mass is not a residue of the quark's.")
