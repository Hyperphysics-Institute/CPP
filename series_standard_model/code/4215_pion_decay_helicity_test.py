#!/usr/bin/env python3
"""4215 -- TODO-4214-ONESIGN item 2: pi+ -> l+ nu_l under the ejection rule.
Spin-0 parent, two-body: leptons back to back, spins must cancel. Ejection rule (4201): a lepton of
label q leaves along q x own spin with bias W ~ 1 + h cos, h = beta (its measured helicity |v/c|).
The nu_l (q=-1) is LEFT-handed; spin cancellation then FORCES the l+ to be LEFT-handed too -- the
'wrong' helicity for an antiparticle -- which the rule allows only with probability (1-beta)/2.
Prediction: Gamma ~ p * (1-beta)/2 per channel.  SM: Gamma ~ p * m_l^2 (helicity suppression)."""
mpi, mmu, me = 139.570, 105.658, 0.511
def kin(m):
    p = (mpi**2 - m**2) / (2*mpi); E = (mpi**2 + m**2) / (2*mpi); return p, E, p/E
pm, Em, bm = kin(mmu); pe, Ee, be = kin(me)
print(f"mu+: p = {pm:.2f} MeV, beta = {bm:.3f}, P(wrong helicity) = (1-beta)/2 = {(1-bm)/2:.3f}")
print(f"e+ : p = {pe:.2f} MeV, beta = {be:.6f}, P(wrong helicity) = {(1-be)/2:.2e}")
model = (pe*(1-be)/2) / (pm*(1-bm)/2)
sm = (me**2/mmu**2) * ((mpi**2-me**2)/(mpi**2-mmu**2))**2
print(f"\nGamma(pi->e nu)/Gamma(pi->mu nu):  model {model:.2e}   SM tree {sm:.2e}   measured 1.230e-4")
print(f"model/measured = {model/1.230e-4:.2f}")
print("\nSIGN: mu+ left-handed (wrong for an antiparticle), forced by the left-handed neutrino: model agrees.")
print("MAGNITUDE: the rule's (1-beta) versus the SM's m^2 -- same order, off by ~1.4 in the e/mu ratio.")
