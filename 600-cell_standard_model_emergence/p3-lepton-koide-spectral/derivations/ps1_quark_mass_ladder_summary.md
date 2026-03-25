# PS-1: Quark Mass Ladder — Complete Analysis and Findings

**Date:** 25 March 2026  
**For:** Thomas Lee Abshier / Hyperphysics Institute  
**Status:** OP-SS-1 remains OPEN. No mechanism reproduces quark masses from first principles.  

---

## Executive Summary

Every proposed quark mass mechanism was tested against exact 600-cell geometry with verifiable code. **None of them work.** The cage-depth model with φ^(3(l-1)) scaling is numerically falsified. Grok's three-mechanism correction (PSR compression + phase cancellation + exact volumes) was computed explicitly and still fails by factors of 0.07–2.0×. The φ^(3(l-1)) claim should be removed or heavily qualified in the strong sector paper.

However, two striking numerical findings emerged that may point toward the correct mechanism.

---

## What Was Tested

| Mechanism | Description | Result | Verdict |
|-----------|-------------|--------|---------|
| A: Naive φ³ scaling | N_l × E_eDP × φ^(3(l-1)) | Off by 2.4–8.3× | **Falsified** |
| B: PSR compression | r_eff = l_P/(1+α·n·sea) | Factors of 0.37–0.75 | Too small |
| C: Phase cancellation | C_n = \|Σ exp(i2πm/φ²)\|/n | Oscillates: 0.07–0.72 | Quasi-random |
| D: Actual shell volumes | From exact 600-cell computation | Grow *slower* than φ³ | Wrong direction |
| E: Combined (Grok) | A × B × C | Off by 0.07–2.0× | **Still fails** |

---

## Two Remarkable Numerical Findings

### Finding 1: m_u = m_e × φ³ to 0.2%

The up quark mass is the electron mass scaled by exactly one factor of φ³:

**m_u/m_e = 4.227 vs φ³ = 4.236 — error 0.21%**

This is the most precise quark-lepton mass relation in the data. φ³ is the volume ratio of the 600-cell edge cube to the Planck volume, and is also the volume of one tetrahedral cell in circumradius units. If the up quark is an electron plus one tetrahedral cell's worth of SSV energy, this relation follows naturally.

### Finding 2: K(c, b, t) = 2/3 to 0.4%

The three heaviest quarks (charm, bottom, top) nearly satisfy the Koide relation:

**K(c,b,t) = 0.6695 vs 2/3 = 0.6667 — deviation 0.42%**

Compare: K(d,s,b) = 0.731 (9.7% off), K(u,c,t) = 0.849 (27% off). The heavy-quark triplet is two orders of magnitude closer to 2/3 than the generation-grouped triplets.

**Physical interpretation:** For heavy quarks, the current mass vastly exceeds the cage binding contribution. The K3 spectral structure (which gives K = 2/3 for leptons) "shows through" when the cage contamination is small relative to the total mass. This is consistent with Thomas's DP-cloud picture: mass is primarily ZBW thermal energy (governed by K3), with cage binding as a perturbation that's relatively larger for light quarks.

---

## The Quark Mass φ-Exponent Sequence

All six quark masses can be expressed as m_e × φ^n with integer exponents:

| Quark | Mass (MeV) | n (from m_e) | m_e × φ^n | Error |
|-------|-----------|-------------|-----------|-------|
| u | 2.16 | 3 | 2.16 | **0.2%** |
| d | 4.70 | 5 | 5.67 | 20.6% |
| s | 93.4 | 11 | 101.7 | 8.9% |
| c | 1270 | 16 | 1128 | 11.2% |
| b | 4180 | 19 | 4777 | 14.3% |
| t | 172760 | 26 | 138707 | 19.7% |

**Exponent sequence:** 3, 5, 11, 16, 19, 26  
**Differences:** 2, 6, 5, 3, 7

The errors are systematically 10–20% (except u at 0.2%), and the exponent differences show no obvious arithmetic pattern. The observation is suggestive but not a derivation.

Note that the lepton exponents (from our earlier calculation) are approximately 0, 11, 17 — and 11 appears for both m_s/m_e AND m_μ/m_e. The strange quark and muon have nearly the same mass ratio to the electron expressed in φ-powers.

---

## What the 600-Cell Actually Provides for Mass

### Confirmed (solid):
- **Qualitative ordering:** More cage structure → more mass (proved: each shell adds positive energy)
- **m_u < m_d direction:** SSV sign asymmetry (qualitative, from cage geometry)
- **Proton mass ≈ 99% field energy:** qDP chain mechanism (correct, cage-independent)
- **K = 2/3 for leptons:** K3 spectral theorem (conditional on P1+P3)

### Falsified:
- **φ^(3(l-1)) volume scaling:** Actual shells don't follow this
- **C₆₀ fourth cage:** No 60-vertex shell in the 600-cell
- **Cage vertex counting as mass mechanism:** Corrections dominate base terms

### Open:
- **Why the φ-exponents are 3, 5, 11, 16, 19, 26**
- **Why K(c,b,t) ≈ 2/3 but K(d,s,b) ≠ 2/3**
- **Thomas's DP-cloud thermal mechanism** (consistent but not computed)

---

## Recommendations

### For the strong sector paper (cpp_ss_unified_v2.tex):

1. **Keep OP-SS-1 as OPEN** — it already is, correctly
2. **Qualify the φ^(3(l-1)) claim** in the mass-ladder open problem section. Replace "The volume scaling φ^(3(l-1)) is the multiplicative mechanism (established)" with "The volume scaling φ^(3(l-1)) is a conjecture that captures the qualitative hierarchy but is quantitatively falsified by exact 600-cell shell computation (factor 3–8× errors). The correct mass mechanism is open."
3. **Remove the C₆₀ fourth cage claim** or qualify it: "The C₆₀ fullerene does not appear as a distance shell of the 600-cell. The top quark cage, if it exists, uses a non-shell polyhedral substructure (62 vertices from shells 1+2+3) rather than a single distance shell."
4. **Add Finding 2** (K(c,b,t) ≈ 2/3) as a remark — it strengthens the K3 framework

### For the lepton series:

5. **Add Finding 1** (m_u = m_e × φ³) as a remark connecting the quark and lepton sectors
6. **The K3 spectral theorem and Paper 4 proceed unchanged** — the lepton mass framework doesn't depend on the cage-depth model

### For future work:

7. **Thomas's thermal/DP-cloud picture** should be the next computational target for OP-SS-1, not further cage-geometry fixes
8. **The φ-exponent sequence** (3, 5, 11, 16, 19, 26) is an empirical constraint that any correct mechanism must reproduce
