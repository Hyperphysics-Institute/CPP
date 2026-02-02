# Pre-Registration: Independent Test of Uniform Handedness Preference Across Physical Phenomena

**Version**: 1.0  
**Date**: January 22, 2026  
**Authors**: Claude (Sonnet-4), Thomas Lee Abshier, ND (with Grok assistance)  
**Status**: Draft – open for joint revision before finalizing  

## 1. Background & Rationale

Thomas Abshier and Grok have reported strong statistical evidence for a uniform handedness preference (Δp_LR ≈ 0.04) across 73 primary physical observations spanning quantum to cosmological scales. After granular independence weighting for shared datasets/instruments, the effective sample size is ≈49, yielding a binomial probability under the 50/50 null of ≈1.78 × 10⁻¹⁵.

This pre-registration defines the protocol for an independent test of the same phenomenon using a new set of phenomena selected by Claude without prior knowledge of the original swarm entries. The goal is to determine whether the directional handedness preference replicates in a blind, independently curated sample.

## 2. Selection Criteria

Claude will independently select 75–100 peer-reviewed studies (published 2015–2026) meeting these objective criteria:

- Observational or experimental data (not pure theory or simulation-only)
- Quantifiable handedness/chiral/asymmetry metric (e.g., spin direction, polarization degree, rotation sense, helicity, clustering preference, outflow direction, line shift asymmetry, etc.)
- Reported statistical significance >2σ from null (or clear directional preference)
- Diverse physical scales: quantum, mesoscopic, galactic, high-z, cosmological
- Published in peer-reviewed journals or reputable archives (arXiv with follow-up publication preferred)

Exclusion criteria:
- Any overlap with Thomas Abshier’s original 78 swarm entries (to avoid selection bias)
- Purely theoretical predictions without empirical data
- Studies where handedness is not a primary or clearly reported outcome

## 3. Analysis Protocol

Thomas Abshier (with Grok) will analyze the provided list using **exactly** the pre-registered methodology:

- **Handedness quantification**: Consistent with original paper (fractional excess of one direction: Δp_LR = (left − right)/(left + right) or equivalent)
- **Independence weighting**: Fractional (1/n for n entries sharing the same dataset/instrument/survey/physical mechanism; full 1.0 for independent replications)
- **Statistical test**: Binomial probability of perfect directional concordance under null p=0.5
- **Effect size**: Report average Δp_LR and consistency of direction
- **Documentation**: All steps publicly documented in a new GitHub repo/branch (code, calculations, decisions)

## 4. Success/Failure Criteria

- **Confirmatory**: Consistent directional bias (same sign as original Δp_LR > 0) across the set, with overall binomial p < 0.01 after independence weighting.
- **Falsification**: ≥3 independent probes showing clear reversal (opposite sign, p < 0.05 each) OR overall p > 0.01 after correction.
- **Inconclusive**: Results between these thresholds — further investigation required.

## 5. Timeline & Logistics

- **Week 1–2**: Finalize protocol, pre-register on OSF/GitHub
- **Week 3–4**: Claude provides independent list (75–100 phenomena)
- **Week 5–7**: Thomas performs analysis (public notebook)
- **Week 8–9**: Joint review of results
- **Week 10+**: Co-authored report/paper summarizing methods and outcomes

## Signatures / Agreement

[To be signed digitally or via email confirmation once final protocol is agreed]

Claude (Sonnet-4): ___________________________ Date: __________
Thomas Lee Abshier, ND: _____________________ Date: __________

This protocol is public and immutable once registered. Any deviations will be documented and justified.
