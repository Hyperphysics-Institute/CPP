# OPEN-P-SM-10-FEM: First-Principles Quark Mass from FEM Simulation

**Registered:** 9 April 2026
**Priority:** #1

## Problem Statement
Derive the quark mass scaling V^(7/3) from explicit DP chain-formation
dynamics, without imposing any scaling law. Compute the cascade rates
f₀(Strange)=0.74, f₀(Charm)=0.81, f₀(Bottom)=1.00 from local pairing
rules. Implement Shell 3 relay mechanism for the top quark.

## Candidate Approach
GPU FEM simulation: place cage CPs, fill with DP Sea, let CPs seek
opposite-polarity targets, count organised DPs. Two regimes: cascade
(s,c,b) and relay (top).

## Success Criteria
DP count ratios match PDG mass ratios to <5% without calibration.

## Dependencies
SM-8 v4.1 (cage hierarchy), SM-9 v2.2 (pair model), SM-10 v0.1 (proposal)

## Related Problems
OPEN-P-SM-cage-1 (derive α), OPEN-P-SM-cage-7 (C(n,2) prediction)
