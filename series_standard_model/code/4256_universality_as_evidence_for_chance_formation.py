#!/usr/bin/env python3
"""4256 -- the founder's bet (W0 forms by chance, host-independent) has a measurement behind it: lepton universality.
If the bracelet's presence rate depended on the host's gradient, G_F extracted from muon decay (a lepton host) and from
neutron/nuclear beta decay (a quark host, CKM-corrected) would differ. They agree at the 1e-3 level (CKM unitarity tests).
Consequence for CAND-EW-4DOVERLAP-4255: E cannot enter at formation; it enters at the capture/release (the released
wave's coherence with the pocket), which is where the candidate already places it. The coefficient = the Sea's
host-independent presence rate x CPP's phase-space measure -- the SM's own coefficient ratio is pure phase space:"""
import math
G_F=1.1663788e-11; m_e,m_mu,m_W,m_const=0.510999,105.658,80379.0,313.0
Vud2=0.9737**2; lam=-1.2754; D=1+3*lam*lam; f=1.6887
cn=Vud2*D*f/(2*math.pi**3); cmu=1/(192*math.pi**3)
print(f"Gamma_n  = G_F^2 m_e^5  x {cn:.3e}   (|V_ud|^2 (1+3 lam^2) f / 2 pi^3)")
print(f"Gamma_mu = G_F^2 m_mu^5 x {cmu:.3e}   (1 / 192 pi^3)")
print(f"ratio of coefficients = {cn/cmu:.0f} -- entirely phase space (two-body n vs three-body mu); the (E/m_W)^4 x E and G_F are common.")
print("-> host-independence of G_F to ~1e-3 (CKM unitarity) bounds any environmental BIAS of bracelet formation below ~0.1%:")
print("   the founder's 'bias but not direction' is allowed only at that level. His 'by chance' is the reading the data pick.")
print("-> tension to record, not resolve: 'stabilised on capture' vs SF-2 Prop. lifetime, where the captured charge BREAKS D6 and")
print("   is the decay channel (Gamma_W = 2 GeV is the ACTIVATED W). The bare W0's width is unmeasured; both can be true only if the")
print("   virtual bare bracelet is shorter-lived than hbar/Gamma_W = 3e-25 s, i.e. dies within ~a Compton time.")
