# 70/30 L/R Pilot Study - Chiral Asymmetry Meta-Analysis

## Project Overview

This repository contains the pilot phase of an amended meta-analysis investigating primordial chiral bias across physical phenomena. The study tests a refined hypothesis based on initial findings from 48 high-quality studies that revealed a robust 70% left-handed preference rather than the originally hypothesized uniform 4% bias.

## Study Information

**Title**: Meta-Analysis of Chiral Asymmetries as Evidence for Primordial 600-Cell Lattice Bias (Amendment - Pilot Phase)

**Principal Investigator**: Thomas Abshier  
**AI Collaborator**: Claude (Anthropic Sonnet-4)  
**Amendment Date**: January 26, 2026  
**OSF Registration**: (https://osf.io/qjf6w)  
**DOI**: 10.17605/OSF.IO/V7W43

## Hypothesis

**Original Hypothesis (Disproved)**: Uniform ~4% left-handed chiral preference (ΔpLR ≈ 0.04) across all physical scales

**Refined Hypothesis (Under Test)**: A primordial left-chiral bias exists, manifesting as a ~70/30 L/R statistical preference across randomly sampled high-quality studies, with scale-dependent modulation by competing physical processes.

## Theoretical Framework

The study tests predictions from Conscious Point Physics (CPP) theory, specifically that Capotauro nucleation (~130 million years post-Big Bang) in a 600-cell lattice framework creates a detectable primordial left-chiral bias. The amended hypothesis proposes this manifests as a statistical imprint rather than uniform effects.

## Study Design

### Pilot Phase (Current)
- **Sample Size**: Exactly 52 additional phenomena
- **Timeline**: 2-week selection + 2-3 week analysis
- **Design**: Independent selector methodology with blinding protocol

### Selection Protocol
- **Selector**: Claude AI (phenomena identification)
- **Analyst**: Thomas Abshier (directional classification & statistics)
- **Blinding**: Claude isolated from directional analysis; Thomas blind to selection until completion

### Inclusion Criteria
- Peer-reviewed publications (2015-2026)
- Statistical significance >2σ (p < 0.05)
- Clear directional handedness/chirality measurement
- Independence from original 48-study dataset
- Diverse physical scale representation

### Exclusion Criteria
- Overlap with original dataset
- Purely theoretical studies
- Ambiguous directional outcomes
- Insufficient statistical rigor

## Methodology

### Statistical Analysis
- **Primary Test**: One-sample binomial test for 70% left-handed preference
- **Significance Level**: α = 0.01
- **Independence Weighting**: Fractional weights for shared datasets/instruments
- **Expected Effective n**: 35-40 (from 52 raw phenomena)

### Scale Categories
1. **Quantum/Sub-atomic**: Expected ≥80% left-handed
2. **Intermediate** (planetary/stellar/biological): Expected ~70% left-handed  
3. **Cosmic/Large-scale**: Expected variable but overall left-biased

### Success Criteria
- **Strong Support**: ≥70% left-handed at p ≤ 0.01 + scale-dependent pattern
- **Falsification**: <60% left-handed at p < 0.05

## Repository Structure

├── README.md
├── data/
│ ├── pilot_phenomena_raw.csv # Raw selected phenomena data
│ ├── pilot_phenomena_classified.csv # With directional classifications
│ └── independence_weights.csv # Calculated independence weights
├── analysis/
│ ├── pilot_analysis.R # Primary statistical analysis
│ ├── scale_subgroup_analysis.R # Scale-dependent analysis
│ └── exploratory_analysis.R # Optional exploratory tests
├── selection_log/
│ ├── tranche_01_phenomena.md # First 10 phenomena (Studies 1-10)
│ ├── tranche_02_phenomena.md # Second tranche
│ ├── ...
│ └── selection_criteria_log.md # Real-time selection decisions
├── documentation/
│ ├── osf_amendment.pdf # Original OSF amendment document
│ ├── selection_protocol.md # Detailed selection methodology
│ └── blinding_verification.md # Blinding protocol documentation
└── results/
├── pilot_results.md # Primary findings summary
├── figures/ # Statistical plots and visualizations
└── supplementary_analysis.md # Exploratory results

markdown


## Current Status

### Completed
- ✅ OSF amendment submitted and approved
- ✅ All 52 phenomena selected (Studies 1-52/52) **COMPLETE**
- ⏳ **Current Phase**: Independence verification and weighting

### Next Steps
1. Independence verification and weighting
2. Directional classification by Thomas Abshier
3. Statistical analysis per preregistered protocol
4. Results interpretation and formal study design

## Data Transparency

### Selection Transparency
- All phenomena selection decisions documented in real-time
- Selection reasoning recorded before directional analysis
- Complete audit trail of inclusion/exclusion decisions

### Analysis Transparency  
- All analysis code publicly available
- Pre-registered statistical plan followed exactly
- No post-hoc modifications to success criteria

## Key Features

### Methodological Innovation
- **Independent Selector Protocol**: AI performs selection isolated from analysis
- **Scale-Dependent Testing**: Different expectations across physical scales
- **Adaptive Preregistration**: Transparent hypothesis refinement based on data

### Bias Controls
- Claude AI selector blind to specific original dataset composition
- Thomas Abshier analyst blind to selection until completion
- Independence verification prevents dataset overlap
- Public documentation prevents post-hoc rationalization

## Timeline

- **Week 1-2**: Phenomena selection (Claude AI) ✅ **COMPLETE**
- **Week 3**: Independence verification and weighting
- **Week 4-5**: Directional classification and analysis (Thomas Abshier)  
- **Week 6**: Results interpretation and formal study design

## Expected Outcomes

### If 70/30 Pattern Replicates
- Strong evidence for primordial chiral bias
- Scale-dependent modulation confirmed
- Proceed to formal preregistered meta-analysis (100+ studies)

### If Pattern Fails to Replicate  
- Falsification of refined hypothesis
- Investigation of potential confounding factors
- Theory refinement or abandonment

## Citation

If using this work, please cite:
Abshier, T. & Claude AI (2026). Meta-Analysis of Chiral Asymmetries as Evidence for
Primordial 600-Cell Lattice Bias: 70/30 Pilot Study Amendment.
OSF Preregistration. [DOI]

pgsql


## Contact

**Thomas Lee Abshier, ND**  
drthomas007@protonmail.com
503-255-9500 (landline) 

**Questions about AI collaboration methodology:**  
Reference: Anthropic Claude Sonnet-4 selection protocol documentation

---

## Acknowledgments

This study demonstrates transparent hypothesis refinement in response to empirical evidence and exemplifies adaptive preregistration methodology. The collaboration between human researcher and AI system provides a novel approach to bias-reduced scientific investigation.

**Conflict of Interest**: No financial conflicts. Thomas Abshier developed both original and refined hypotheses; Claude AI maintains analytical independence without outcome preference.
