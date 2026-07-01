#!/usr/bin/env python3
"""
OPEN-COSMO-DM-4 route B (patch 2207, substrate-cosmology lane): derive eps_nuc from nucleation vs growth rate.
=============================================================================================================
Executes the DM 2206 handover ask (founder-chosen route B, 1848): derive the CPP nucleation rate vs growth rate
at the aggregation epoch -> seed fraction eps_nuc = n_seed/n_monomer -> N_form = 1/eps_nuc; does eps_nuc ~ 1e-3?

RESULT: in nucleation-and-growth, eps_nuc = R_nuc/R_acc at the nucleation freeze, and the collision prefactors
(n_mono, sigma, v -- ALL the cosmology) CANCEL between the nucleation and accretion channels, leaving
eps_nuc ~ exp(-dG*_nuc/kT_form). So eps_nuc is set by the nucleation BARRIER, not the epoch (valid because
aggregation is collision-fast, Gamma/H~1e7-1e11, 2206). eps_nuc~1e-3 <=> dG*_nuc ~ 6.5 kT_form.

Sensitivity (corrects+affirms 1848): N_form=1/eps_nuc is linear in eps_nuc, but eps_nuc=exp(-dG*/kT) is
exponential in the barrier, so N_form=exp(+dG*/kT) is exponential in dG* -- 1848's 'B linear vs A exponential'
is imprecise (BOTH exp in their knob). The real advantage: B's exponent (dG*/kT~6.6) is ~4x SMALLER than A's
(E/2kT~25), so B needs its knob pinned to ~14% vs A's ~3.7% -- ~4x looser. Plus dG*_nuc~6.5 kT is a natural
few-kT scale for a specific-geometry nucleus, while A's T_DM/T_rad~1e-2 needs a decoupling coincidence. So the
founder's CONCLUSION (B less fine-tuned, better gradient) holds -- for the smaller-exponent + natural-scale
reason, not linearity. VERDICT: the pin is dG*_nuc (ribbon->cross nucleation barrier, a geometry/energetics
calc); substrate-cosmology has reduced eps_nuc to it and shown the epoch drops out. Not killed, not predicted;
cluster sigma/m~1/v^2 branch stands.
"""

