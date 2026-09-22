#!/usr/bin/env python3
"""4217 -- TODO-4214-ONESIGN item 5: 'neutrinos are only left-handed'. Under the ejection rule with bias
h = beta, the wrong-helicity fraction at creation is (1-beta)/2 = m^2/(2 E (E+p)) ~ m^2/(4E^2)."""
def wrong(m_eV, E_MeV):
    E = E_MeV*1e6; p = (E*E - m_eV*m_eV)**0.5; return (E-p)/(2*E)
for m in (0.05, 0.5):
    for name, E in (('reactor nubar, 3 MeV', 3.0), ('beta-decay nubar, 0.5 MeV', 0.5), ('solar pp nu, 0.3 MeV', 0.3)):
        print(f"m_nu = {m:4.2f} eV  {name:28s}  wrong-helicity fraction {wrong(m,E):.1e}")
print("\nSM (Dirac): wrong-helicity amplitude^2 ~ m^2/(4E^2) at these energies -- the same number.")
