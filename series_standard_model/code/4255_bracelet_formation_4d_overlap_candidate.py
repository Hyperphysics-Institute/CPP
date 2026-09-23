#!/usr/bin/env python3
"""4255 -- the (E/m_W)^2 bracelet-formation amplitude (4233's target; TODO-4251-LIFETIME): a CANDIDATE rule, not a derivation.
Candidate: on the 4D substrate, the probability that the decay's released wave (4-extent lambda = hbar c / E) coheres with
the bracelet's zero-gradient pocket (4-extent r_pk = hbar c / m_W) is a 4-volume ratio, (r_pk/lambda)^4 = (E/m_W)^4 --
the squared W propagator read as a 4D overlap. The ring's GEOMETRIC size (0.346 fm, 4251) is the trap; the Compton pocket
is the coherent core where the reset acts (4229's number, reinstated in that role only).
What E is: in the SM form Gamma ~ g^4 m_e^5 f / m_W^4 the m_W^-4 is the propagator and the m_e^5 is phase space at the
Q-value scale, so E is the released energy scale, Q ~ 0.78 MeV, not the W's."""
import math
hbar_MeVs=6.582119569e-22; m_e,m_W,m_const,Q=0.510999,80379.0,313.0,0.782
G_F=1.1663788e-11; Vud2=0.9737**2; lam=-1.2754; D=1+3*lam*lam; f=1.6887
Gamma=G_F**2*Vud2*D*f*m_e**5/(2*math.pi**3); P=2*math.pi*Gamma/m_const   # per ZBW cycle (4233)
print(f"per-cycle decay probability (4233): P = {P:.3e}")
for lab,E in [("E = m_e",m_e),("E = Q (n-p-m_e)",Q)]:
    ov=(E/m_W)**4
    print(f"  4D overlap with {lab:16s}: (E/m_W)^4 = {ov:.3e};  P / overlap = {P/ov:.3e};  x (m_const/E) = {P/ov*m_const/E:.3e}")
print("  -> with E = m_e, P/(E/m_W)^4 = 8.8e-6 = (m_e/m_const) x 5.4e-3; with E = Q, 1.6e-6. Neither leaves O(1): the candidate has the")
print("     SHAPE of the target (a lepton-scale energy to the fourth over m_W) and the coefficient 5e-3 is not supplied.")
alpha=1/137.036; s2=0.23122; g2=4*math.pi*alpha/s2
print(f"  the SM's own coefficient in this form: g^4 |V|^2 (1+3 lam^2) f / (64 pi^3) = {g2*g2*Vud2*D*f/(64*math.pi**3):.3e}  (g^2 = {g2:.3f}) -- the weak")
print("     coupling squared, times the f/(64 pi^3) phase-space normalisation: in CPP these would be the bracelet's own coupling to the")
print("     released pair and the 4D phase-space measure. Not on file.")
print("\nstatus: candidate registered (CAND-EW-4DOVERLAP-4255); not adopted. Needs: (i) a substrate statement that coherence over a 4-volume")
print("gives an overlap probability; (ii) what supplies the g^4-scale coefficient; (iii) a picture ruling on whether the bracelet forms by")
print("Sea chance (E-independent) or is pulled together by the process (E-dependent).")
