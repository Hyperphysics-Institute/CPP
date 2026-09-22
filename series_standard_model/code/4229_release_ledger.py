#!/usr/bin/env python3
"""4229 -- the release ledger: what the quark's orbital eDP must do to become the antineutrino.
Before: bound orbital ZBW at the down quark, smearing radius r_ZBW = hbar c / m_const (4178), m_const ~ 313 MeV.
After:  unanchored orbital ZBW = the antineutrino (SF-4), rest energy m_nu < 0.8 eV (KATRIN), plausibly ~0.05 eV.
Conserved across the release: the orbital angular momentum, hbar/2.  Not conserved: the circulation energy,
which the refill half of the created counter-pair must re-establish at the up quark."""
hbarc = 197.327  # MeV fm
m_const = 313.0
r_q = hbarc/m_const
print(f"bound orbital at the quark:   m = {m_const:.0f} MeV   r_ZBW = {r_q:.3f} fm")
for m_nu_eV in (0.8, 0.05, 0.01):
    m = m_nu_eV*1e-6; r = hbarc/m
    print(f"unanchored orbital (nubar):   m = {m_nu_eV:5.2f} eV   r_ZBW = {r:.3e} fm = {r*1e-15*1e6:.2f} um   energy ratio before/after = {m_const/m:.1e}   radius ratio = {r/r_q:.1e}")
print("\nangular momentum: L = hbar/2 before and after (the orbital's, carried out unchanged; B = +1 at the vertex)")
print("energy: the ~313 MeV of circulation does NOT leave with the antineutrino; the up quark has the same constituent")
print("        mass, so the refill half of the created pair re-establishes it. The lepton pair shares only Q = 0.782 MeV,")
print("        continuously (4204 s3). The release is therefore an EXPANSION of the orbital by ~1e9-1e10 in radius at")
print("        fixed L, with its circulation energy handed to the refill -- not a detachment of an intact 313-MeV rotor.")
# size of the W0 null pocket vs the orbital
m_W = 80379.0
r_W = hbarc/m_W
print(f"\nW0 scale: hbar c / m_W = {r_W:.4f} fm;  orbital radius / W0 scale = {r_q/r_W:.0f}")
print("   The centroid's zero-SSV_net pocket (founder step 1) is ~250x smaller than the orbital it must release:")
print("   the orbital DP passes THROUGH the pocket, once per circulation if the geometry aligns; it does not sit in it.")
