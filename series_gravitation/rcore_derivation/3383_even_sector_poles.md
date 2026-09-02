# The complex poles decide it: the even-sector displacement is −7.5% (ℓ = 2) and −10.7% (ℓ = 3), not −13.4%; the modes ARE near-trapped (Q = 25, 92); the Neumann-crossing/barrier-top coincidence is a property of the Buchdahl wall

**Patch 3383, Session 161, 2 Sep 2026.** Verify `code/3383_even_sector_poles_verify.py` (14/14). Reasoning `reasoning/3383.md`. Discharges CONV-039 Q2's UNDETERMINED (GPT, Grok) and Q6(α).

**Standing:** the poles are COMPUTED (direct integration, 3356 rung-2 machinery; r0-independent to 1e-14; sharp; the Dirichlet ℓ = 2 pole reproduces 3356's Zerilli root 0.44506 − 0.13442i exactly). The a = 0 even-sector numbers below supersede 3378 §3 and 3379 §2. Still at a = 0; still conditional on the trace model (zero-compliance limit).

## §1 The poles (M = 1, r_w = 9M/4, 62 M_⊙ in Hz)

| ℓ | wall | Mω | Hz | Q |
|---|---|---|---|---|
| 2 | Dirichlet (shipped assumption) | 0.44506 − 0.13442 i | 232 | 1.66 |
| 2 | Neumann (diagnostic) | 0.38153 − 0.02492 i | 199 | 7.65 |
| 2 | **Robin β₂(ω), derived** | **0.41159 − 0.00815 i** | **215** | **25.3** |
| 3 | Dirichlet | 0.67582 − 0.10476 i | 352 | 3.23 |
| 3 | Neumann | 0.58280 − 0.01368 i | 304 | 21.3 |
| 3 | **Robin β₃(ω), derived** | **0.60367 − 0.00329 i** | **315** | **91.7** |

## §2 What the poles say about the panel's two objections

- **The −13.4% was a locator artifact** (Grok's objection sustained). The true displacements of the pole real parts are **−7.5% (ℓ = 2)** and **−10.7% (ℓ = 3)** — negative for both, not identical. The 3379 *centroids* (0.412, 0.604) were in fact the pole real parts to three figures; it was the *Dirichlet reference* that the half-max centroid mis-located (0.475 vs the pole's 0.445 — a broad, low-Q feature is exactly where a centroid drifts).
- **"Near-trapped" is earned** (GPT's objection answered). Q rises from 1.7 → 25 (ℓ = 2) and 3.2 → 92 (ℓ = 3). The derived wall turns a broad top-of-barrier hump into a narrow line. This is the physical content of the Neumann crossing sitting at the barrier top.

## §3 Q6(α): the crossing is a property of the Buchdahl wall

`β_ℓ(ω) = b₀ − b₂ω²`; the Neumann crossing `ω₀ = √(b₀/b₂)` vs the barrier top `√(max V_ℓ)`:

| r_w | ℓ = 2 | ℓ = 3 | ℓ = 4 |
|---|---|---|---|
| **9M/4 (Buchdahl)** | **1.068** | **0.995** | **0.972** |
| 2.5M | 1.287 | 1.203 | 1.175 |
| 3M | 1.383 | 1.298 | 1.267 |

At Buchdahl the crossing sits at the barrier top to 7% for ℓ = 2, 3, 4 (and tightening with ℓ); off Buchdahl it drifts to +20–40%. **Structural, and specific to the Buchdahl wall** — the same radius at which the surface lapse is 1/3, the Schwarzschild interior's central pressure diverges, and (CONV-038) the register saturation is extremal. Not explained here; now a sharper fact.

Two more facts from varying `r_w`: (i) `b₀` and `b₂` flip sign *together* beyond ~2.4M, so the crossing persists everywhere but β's sign inverts (the wall is softer-than-Dirichlet below the crossing at Buchdahl, stiffer above it for larger walls); (ii) **`β_ℓ` diverges at `r_w = 2.38M` (ℓ = 2) / `2.36M` (ℓ = 3)** — there, and only there, the trace condition *is* exact Dirichlet on `Z⁺`. That radius is not Buchdahl. The old `X = 0` would have been the derived even-sector wall for a surface 6% further out.

## §4 What this changes

- GR-2 V1.8's "displacement −13.4%, provisional" → **"−7.5% (ℓ = 2), −10.7% (ℓ = 3), from complex poles; Q 25 and 92"** at the next version. Not enacted here (ledger unchanged); one line in the paper.
- 3379's Kerr *estimate* (166 / 250 Hz) rescaled to the pole shifts would read ~177 / ~258 Hz — still a scaled guess, still not a prediction, still outside prediction language.
- The a = 0 even sector is now as settled as it can be without the c_* map and the Kerr reconstruction: **positions and widths from poles, wall law derived, slicing robust.**

## §5 Owed
- The odd sector under both c_* brackets (OPEN-GR-ODDWALL-1).
- The O(kd) skin term.
- Q6(β) for the mechanism of "crossing = barrier top at Buchdahl" — an analytic question, open.
