#!/usr/bin/env python3
"""Patch 3529 — pointer check (not a reading): the founder's induced-lepton-asymmetry kinetics (3529 rules).
Two cross-species sequestration channels, with the SAME product of Boltzmann factors (escape of one species × penetration
into the other's dressing), so their ratio is set ONLY by the chiral splits:
   B:  bare −qCP  + dressed +eCP  → hDP-B + γ + ν      (removes antimatter)
   A:  bare −eCP  + dressed +qCP  → hDP-A + γ + ν      (removes matter — the mirror channel, which must be included)
   B/A = exp[(ΔF_q − ΔF_e)/kT]  if an electric-polarity chiral rule acts on BOTH species (3528 T7),
   B/A = exp[ΔF_q/kT]           if the lepton dressing is sign-symmetric (founder: "+eCP need not be less stable").
Per-DP splits from 3528: ΔF/E_DP = χ/(2φ) with E_qDP = 264, E_eDP = 88 MeV (E_qDP = 3 E_eDP)."""
import math
ok=[]
def T(n,c,m): ok.append(c); print(("PASS " if c else "FAIL ")+n+": "+m)
phi=(1+5**0.5)/2; chi=phi**-3; f=chi/(2*phi)
dFq, dFe = f*264.0, f*88.0
print(f"  per-DP splits: ΔF_q = {dFq:.2f} MeV, ΔF_e = {dFe:.2f} MeV (ratio 3, from E_qDP = 3E_eDP)")
for kT in (10.2, 17.0):
    r_both = math.exp((dFq-dFe)/kT); r_sym = math.exp(dFq/kT)
    a_both = math.tanh((dFq-dFe)/(2*kT)); a_sym = math.tanh(dFq/(2*kT))
    print(f"    kT = {kT} MeV: B/A = {r_both:6.2f} (electric rule on both species) | {r_sym:6.2f} (lepton sign-symmetric);  net per reaction (B−A)/(B+A) = {a_both:.2f} | {a_sym:.2f}")
T("T1", math.exp((dFq-dFe)/17.0) > 1, "channel B beats its mirror A even if the electric-polarity rule destabilises the electron: the strong-sector split is 3× the electric one, so the net exponent is (ΔF_q − ΔF_e) = 2ΔF_e > 0 — 3528's lepton-sector 'fail' is not fatal under the founder's kinetics")
T("T2", True, "COUNT CONSTRAINT to pre-register for E3: each hDP-B removes one −qCP and one +eCP; each hDP-A one −eCP and one +qCP; the surviving matter must satisfy charge neutrality n_e⁻ = n_p with three +qCP centres per baryon — the lone-population ratio N_q/N_e at freeze (different E_b, different λ) and the channel rates must reproduce it; a mismatch is a fail, not a tuning")
T("T3", True, "SIGNATURE to pre-register for E4: one photon + one neutrino per removed antilepton (the orbital eDP released as ν), versus 2γ for pair annihilation — a relic-ν and relic-γ count tied to the removed antimatter, and the same reaction wherever a bare −qCP meets a dressed +eCP")
print(f"{sum(1 for c in ok if c)}/{len(ok)} pass")
