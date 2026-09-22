#!/usr/bin/env python3
"""4233 -- the neutron lifetime written in the reset mechanism's units, and what each budget factor must supply.
Standard rate: Gamma = G_F^2 |V_ud|^2 (1 + 3 lam^2) m_e^5 f / (2 pi^3), f = 1.6887 (phase-space integral incl. m_e).
With G_F = sqrt2 g^2 / (8 m_W^2) this is  Gamma = [g^4 |V|^2 (1+3 lam^2) f / (64 pi^3)] (m_e/m_W)^4 m_e.
Per ZBW cycle of the orbital (frequency m_const/(2 pi hbar)):  P = 2 pi hbar Gamma / m_const.
Budget from 4231:  P = (pole in pocket: 2 r_pk / (2 pi r_orb)) x (W0 present at the orbit, aligned) x (outward branch)."""
import math
hbar_MeVs = 6.582119569e-22; hbarc = 197.327
m_e, m_W, m_const = 0.510999, 80379.0, 313.0
alpha, s2 = 1/137.036, 0.23122
g2 = 4*math.pi*alpha/s2; g4 = g2*g2
Vud2 = 0.9737**2; lam = -1.2754; D = 1+3*lam*lam; f = 1.6887
G_F = 1.1663788e-11   # MeV^-2, measured (the g-form with tree-level m_W gives G_F 7% low; radiative)
Gamma = G_F**2*Vud2*D*f*m_e**5/(2*math.pi**3)               # MeV
tau = hbar_MeVs/Gamma
print(f"SM rate in this form: Gamma = {Gamma:.3e} MeV  ->  tau = {tau:.0f} s   (measured 878.4 s; the 4% residual is the radiative correction not included here)")
P = 2*math.pi*Gamma/m_const     # dimensionless: (Gamma/hbar) x (2 pi hbar / m_const)
pref = g4*Vud2*D*f/(64*math.pi**3)
print(f"per-cycle probability P = {P:.2e};  in the g-form P = 2pi x [{pref:.2e}] x (m_e/m_W)^4 [{(m_e/m_W)**4:.2e}] x (m_e/m_const) [{m_e/m_const:.2e}] x (G_F_meas/G_F_tree)^2")
r_orb, r_pk = hbarc/m_const, hbarc/m_W
hit = 2*r_pk/(2*math.pi*r_orb)
rest = P/hit
print(f"pole-in-pocket (geometry, 4231) = {hit:.2e};  so (W0 present, aligned) x (outward) = {rest:.2e}")
shape = (m_e/m_W)**4*(m_e/m_const)
print(f"compare (m_e/m_W)^4 (m_e/m_const) = {shape:.2e};  ratio = {rest/shape:.2f}")
print("\nReading: the pocket geometry takes out one factor 1/(2 pi) x (m_const/m_W); what remains for the substrate to supply is")
print("(m_e/m_W)^4 x (m_e/m_const) x O(5): the fourth power is the SM's squared W propagator at the lepton-mass scale --")
print("in the picture, the probability that a bracelet of mass m_W exists at the orbit with only m_e-scale energy available,")
print("as (E/m_W)^2 in amplitude. The extra m_e/m_const is the fraction of a ZBW cycle the outward branch has to succeed in.")
print("NOT derived: the bracelet-formation rule that gives (E/m_W)^2 is the sector's missing input; this fixes its target.")
