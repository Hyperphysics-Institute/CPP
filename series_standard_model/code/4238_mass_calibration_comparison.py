#!/usr/bin/env python3
"""4238 -- the corpus's mass calibration against the numbers this session used (founder's request at close).
Corpus: c04 - rest mass = energy of one Compton ZBW cycle of the polarization cloud, m c^2 = h nu_C; calibration m_e.
        SS-2 - m_const = 312.7 MeV DERIVED (free-cage constituent scale); r_ZBW = hbar c / m_const = 0.631 fm; 4188: never
               run this backwards (r_ZBW -> m_const is circular).  SF-3 - heavy quark masses from m_e + 600-cell + SU(3), RMS 2.1%.
This session (4229, 4231, 4233): m_const = 313 MeV as INPUT; r_ZBW = hbar c / m_const; ZBW cycle frequency m_const c^2/(2 pi hbar)."""
hbarc = 197.327; h_MeVs = 4.135667e-21; hbar_MeVs = h_MeVs/(2*3.141592653589793)
m_ss2 = 312.7; m_used = 313.0
print(f"r_ZBW from SS-2's m_const = {hbarc/m_ss2:.4f} fm  (glossary 0.631);  from this session's 313 MeV = {hbarc/m_used:.4f} fm  -> difference {100*(1-m_ss2/m_used):.2f}%")
nuC = m_used/h_MeVs; f_used = m_used/(2*3.141592653589793*hbar_MeVs)
print(f"c04 Compton frequency nu_C = m c^2 / h = {nuC:.3e} /s;  4231/4233 cycle frequency m c^2/(2 pi hbar) = {f_used:.3e} /s  -> identical")
print("energy locus: c04 puts the rest mass in the cloud's oscillation, not in any DP -> reading (alpha) of 4232, as used.")
print("direction of inference: SS-2 derives m_const; this session took it as input and never re-derived it from r_ZBW (4188 rule kept).")
print("electron: c04 calibrates to m_e = 0.511 MeV; 4204/4228 have the electron's rest mass established at the event as its Compton cloud forms about the captured -eCP; consistent.")
