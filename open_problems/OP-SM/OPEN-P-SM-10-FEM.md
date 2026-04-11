# OPEN-P-SM-10-FEM: First-Principles Quark Mass from FEM Simulation

**Registered:** 9 April 2026
**Priority:** #1
**Status:** OPEN (Phase 1-2 complete, Phase 3 pending)

---

## Problem Statement

Derive the quark mass scaling V^(7/3) from explicit DP chain-formation dynamics, without imposing any scaling law. Compare organised DP count ratios directly to PDG mass ratios (not to V^(7/3)-derived targets — this avoids circular validation, per Sonnet's review).

## Calibration Targets (from CPU Phase 1-2)

| Quark | f₀ (cascade rate) | N_DPs | Mass (MeV) | PDG (MeV) |
|-------|-------------------|-------|-----------|-----------|
| Strange | 0.738 | 24.6 | 93.4 | 93.4 |
| Charm | 0.805 | 335.1 | 1,270.0 | 1,270.0 |
| Bottom | 0.9997 | 1,103.0 | 4,180.0 | 4,180.0 |
| Top (relay) | 0.998 | 45,585.7 | 172,760.0 | 172,760.0 |

The GPU FEM must produce these f₀ values from local DP pairing rules alone.

## Two-Regime Physics

**Pre-gap (s, c, b):** Intra-cage cascade. Chain cross-linking with radially-varying f(r). Mass dominated by near-center region (51-88%).

**Post-gap (top):** Shell 3 relay mechanism. 12 Shell 3 vertices act as secondary central CPs, creating criss-cross web to Shell 4. Relay contributes 99% of top mass. Enhancement: z × C_F = 16.

## Candidate Approach

GPU FEM simulation (CUDA or JAX):
1. Place cage CPs at lattice positions
2. Fill interior with DP Sea at natural density
3. Each DP has two CPs; each CP seeks nearest opposite-polarity target
4. Let chains form, cross-link, and cascade
5. For top: implement Shell 3 relay (DP dissociation to occupy edgeless vertices)
6. Count organised DPs; compare ratios to PDG

## Success Criteria

- **Level A:** DP count ratios match PDG mass ratios to <5%. V^(7/3) emerges without being imposed.
- **Level B:** Correct ordering and approximate magnitude. Three-region structure emerges.
- **Level C:** Informative failure — reveals which physical assumptions are incorrect.

## Dependencies

- SM-8 v4.1 (cage hierarchy, shell structure)
- SM-9 v2.2 (pair model, chain-type interpretation)
- SM-10 v0.1 (simulation design)
- GPU infrastructure (Isak)

## Related Problems

- OPEN-P-SM-cage-1: Derive α = 7/3 (this problem is the computational approach)
- OPEN-P-SM-cage-7: Why does C(n,2) predict m_b/m_s to 0.6%?
- OPEN-P-SM-cage-3: Connect cage 2/3 fraction to Koide K = 2/3

---

*Registered by Thomas Lee Abshier ND and Claude Opus (Anthropic), 9 April 2026.*
