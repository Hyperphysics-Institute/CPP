# Pre-Registration: Independent Test of Uniform Handedness Preference  
Across Physical Phenomena

**Version**: 2.0 (incorporating Claude's refinements)  
**Date**: January 22, 2026  
**Authors**: Claude (Sonnet-4), Thomas Lee Abshier, ND (with Grok assistance)  
**Status**: Draft – awaiting final joint approval before public registration

## 1. Background & Rationale

Thomas Abshier and Grok reported strong statistical evidence for a uniform handedness preference (Δp_LR ≈ 0.04) across 73 primary physical observations spanning quantum to cosmological scales. After granular independence weighting for shared datasets/instruments/surveys/mechanisms, the effective sample size is ≈49, yielding a binomial probability under the 50/50 null of ≈1.78 × 10⁻¹⁵.

This pre-registration defines the protocol for an independent test using a new set of phenomena selected by Claude without prior knowledge of the original swarm entries. The goal is to determine whether the directional handedness preference replicates in a blind, independently curated sample.

## 2. Selection Criteria

Claude will independently select 75–100 peer-reviewed studies (published 2015–2026) meeting these objective criteria:

- Observational or experimental data (not pure theory or simulation-only)
- Quantifiable handedness/chiral/asymmetry metric (e.g., spin direction, polarization degree, rotation sense, helicity, clustering preference, outflow direction, line shift asymmetry, etc.)
- Reported statistical significance >2σ from null (or clear directional preference)
- Diverse physical scales: quantum, mesoscopic, galactic, high-z, cosmological
- Published in peer-reviewed journals or reputable archives (arXiv with follow-up publication preferred)

**Additional independence requirement**: Studies must be substantively independent from the original 78 swarm entries (different datasets, instruments, physical systems, or research teams). Where uncertainty exists about overlap, the phenomenon will be excluded to maintain conservative independence.

## 3. Analysis Protocol

Thomas Abshier (with Grok) will analyze the provided list using **exactly** the pre-registered methodology:

- **Handedness quantification**: Consistent with original paper (fractional excess of one direction: Δp_LR = (left − right)/(left + right) or equivalent)
- **Independence weighting**: Fractional (1/n for n entries sharing the same dataset/instrument/survey/physical mechanism; full 1.0 for independent replications by different teams/instruments)
- **All handedness determinations and independence weightings will be documented with explicit reasoning before statistical analysis begins**
- **Any ambiguous cases in direction assignment will be discussed jointly and resolved by pre-established criteria**
- **Statistical test**: Binomial probability of perfect directional concordance under null p=0.5
- **Effect size**: Report average Δp_LR and consistency of direction (expected ≈0.04 based on original findings, though consistent directionality is the primary test)
- **Minimum sample requirement**: Effective n ≥ 30 after independence weighting for meaningful statistical power
- **Documentation**: All steps publicly documented in a dedicated GitHub repository (code, calculations, decisions, reasoning logs)

## 4. Success/Failure Criteria

- **Confirmatory**: Consistent directional bias (same sign as original Δp_LR > 0) across the set, with overall binomial p < 0.01 after independence weighting.
- **Falsification**: ≥3 independent probes showing clear reversal (opposite sign, p < 0.05 each) OR overall p > 0.01 after correction.
- **Inconclusive**: Results between these thresholds — further investigation required.

## 5. Timeline & Logistics

- **Week 1–2**: Finalize protocol, pre-register publicly on OSF (with DOI) + mirror on GitHub
- **Week 3–4**: Claude compiles independent phenomena list (75–100)
- **Week 5–7**: Thomas conducts analysis (public notebook)
- **Week 8–9**: Joint review & interpretation
- **Week 10+**: Co-authored report/paper summarizing methods and outcomes

**Data & documentation commitment**: All working documents, selection reasoning, analysis code, raw data (where shareable), and results (confirmatory or falsifying) will be maintained in a public GitHub repository. Any protocol deviations will be documented in real-time with justification.

## Signatures / Agreement

[To be signed digitally or via email confirmation once final protocol is agreed]

Claude (Sonnet-4): ___________________________ Date: __________  
Thomas Lee Abshier, ND: _____________________ Date: __________

This protocol is public and immutable once registered. Any deviations will be documented and justified.
