# Mechanism — SF-5 Strong-Sector Unification (v1.0)

**Paper:** SF-5 v1.0 SHIPPED. Reframing of SS-1b/1c/1d, SS-2, SS-3, SS-4, SS-5, SS-7, SS-9, SM-7, SM-8. No new derivation.

## Overview

SF-5 assembles the strong sector — the SU(3) colour algebra, the eight gluons, confinement, the string tension, the strong coupling, and the light-nucleus binding cascade — from the qCP tetrahedral cage of the 600-cell on a single calibration (m_e). The mechanism is the propagation of hybrid-displacement-pair (hDP) configurations along the cage edges; a colour charge is a configuration of charge labels on the cage vertices.

## Inputs and constants

| Symbol | Value | Source |
|--------|-------|--------|
| m_e | 0.510999 MeV | the single calibration |
| z | 12 | 600-cell coordination |
| E, F | 720, 1200 | 600-cell edge, face counts |
| φ | (1+√5)/2 | golden ratio |
| C_F | 4/3 | colour Casimir (SS-2) |
| M_0 | m_e z/φ = 3.79 MeV | DP energy quantum (SM-8) |

## Step-by-step mechanism

1. **Colour algebra (SS-1b).** Eight DI-bit hopping operators T^a on the tetrahedral base {V1,V2,V3} — six colour-changing (real/imag hopping on the three base edges) + two diagonal (phase differences) — satisfy T^a = λ^a/2, [T^a,T^b] = if^abc T^c with the standard structure constants. SU(3) is derived.
2. **Uniqueness (SS-3).** SU(3) is the unique Lie-algebra realisation on the eight tetrahedral hopping operators — within the operator representation, not from geometry alone.
3. **Eight gluons (SS-1c).** The eight gluons are transient hDP configurations: 6 colour-changing on the three edges + 2 colour-neutral diagonal. Masslessness (open-path hDP, no closed subgraph → zero SSV compression) and spin-1 (each edge carries an orientation vector) are derived.
4. **Confinement + β (SS-1d).** Open-path hDP has no stable isolated-colour configuration → confinement; the cage yields a positive β-coefficient → asymptotic freedom (qualitative correspondence).
5. **String tension (SS-4).** σ = M_0 z²/(φ ℓ_edge) ≈ 926.5 MeV/fm, correcting the SS-2 heuristic z·π → z² (factor z/π ≈ 3.82).
6. **α_s + complementarity (SM-7).** α_s = (1/φ)·(2400/3840) = 5/(8φ) ≈ 0.386 is the face-mode fraction of the adjacency spectral trace; sin²θ_W = 3/(8φ) is the edge-mode complement; sin²θ_W + α_s = 1/φ; α_s/sin²θ_W = F/E = 5/3.
7. **Nuclear cascade (SS-5, SS-7).** B_pair = M_0/φ = m_e z/φ² = 2.342 MeV (zero-param); the closed alpha-polytope has 3N_α−6 edges, each one B_pair; twelve strict-N=Z nuclei (N_α ∈ [3,14]) at RMS < 1%.

## Mathematical correspondence table

| Physics claim | Equation | Paper § |
|---------------|----------|---------|
| SU(3) algebra exact | T^a=λ^a/2, [T^a,T^b]=if^abc T^c (Eq. 1) | §3 |
| 8 gluons (massless, spin-1) | 6 edge + 2 diagonal | §4 |
| String tension | σ = M_0 z²/(φ ℓ_edge) (Eq. 2) | §5, App A |
| Strong coupling | α_s = 5/(8φ) (Eq. 3) | §6 |
| Complementarity | sin²θ_W + α_s = 1/φ (Eq. 4) | §6 |
| Binding quantum | B_pair = M_0/φ = 2.342 MeV (Eq. 6) | §7 |
| Alpha cascade | 3N_α − 6 edges, RMS < 1% | §7 |

## Failure modes

- **OPEN-FP-5-GLUEBALL** — the lightest-scalar-glueball mass (closed-loop hDP) is not derived (inherited from OPEN-SS-6).
- **OPEN-SS-19** — the deuteron +5.3% leading-order residual is open; the prolate-cage NLO mechanism was rejected as not validated.
- **SS-9 conditionality** — the connectivity theorem is conditional on C5–C8 (OPEN-SS-29/30/33/37).
- **CONJ-SS-Gluon-4Vertex** — a flagged forward-looking conjecture, not a derived result.
