# PD-007 rule 2, the cold test: PRED-O-40 as re-cut in 3650 against GW250114. The register closure's static junction (K/H = 2/3 at the wall, c07 dictionary) gives Λ = +714; GW250114 bounds Λ̃ < 34.8 at 90% (log-uniform prior; 155 uniform). **The closure's central value is excluded, by 20× (4.6× at the conservative bound).** Survival window: the wall ratio must be q ≥ 0.762 (+14% over 2/3; +18% for the component bound), or lie on the negative side (q < 0.6615), which the published analysis did not sample. The required shift is inside the corpus's known O(v) dictionary discrepancy at the wall (~30%, 3633 §2) — so the extension is not dead; it is on notice, with the direction and size of what the dictionary must deliver now fixed. Every pre-3650 corpus value (|Λ| ≤ 8) is inside the bound: **GW250114 tests the junction, not the R-core**

**Patch 3651, Session 163, 6 Sep 2026.** Verify `code/3651_pred_o40_cold_test_gw250114_verify.py` (9/9). Reasoning `reasoning/3651.md`. Source: Andrés-Carcasona & Caneva Santoro, "No Love for black holes: tightest constraints on tidal Love numbers of black holes from GW250114," arXiv:2512.01918 (Dec 2025). No paper touched.

## §1 The bound, and that it applies
GW250114 (O4b; m₁ = 33.6, m₂ = 32.2 M☉ source frame; low spin; SNR ≈ 80). Electric ℓ = 2 tidal deformabilities added at 5PN/6PN to IMRPhenomPv2; log-uniform priors on Λ_i ∈ [10⁻³, 5000]. Result: Λ̃ < 34.8, Λ₁ < 28.2, Λ₂ < 45.7 at 90%; ln B ≈ 0 (no preference for tides). With uniform priors: Λ̃ < 155, Λ₁ < 165. Their convention Λ = (2/3)k₂ with the compactness absorbed into k₂ (Cardoso et al. 2017) is the corpus's Λ = (2/3)k₂/C⁵. For identical components Λ̃ = Λ to < 1% at this mass ratio. Only positive Love numbers were sampled; the authors state that negative-TLN objects are not constrained by their analysis.

## §2 The score
| corpus value | k₂ | Λ | vs Λ̃ < 34.8 |
|---|---|---|---|
| 3624 rigid cap, K(R) = 0 | −0.080 | −7.2 | inside (and negative: unsampled) |
| 3633 census frame = 3647 | +0.042 | +3.8 | inside |
| 3633 h̄₀₀ reading | +0.088 | +7.9 | inside |
| **3650 register closure, K/H = 2/3** | **+7.9** | **+714** | **excluded, 20× (4.6× at 155)** |

## §3 The survival window
Λ(q) along the wall ratio q = K/H: +714 (2/3), +94 (0.70), +40 (0.75), +25 (0.80), +9 (1.0), +1 (2.0).
- Λ̃ < 34.8 ⇒ **q ≥ 0.762** (+14% over the closure's 2/3); Λ₁ < 28.2 ⇒ q ≥ 0.785 (+18%); even Λ̃ < 155 ⇒ q ≥ 0.685 (+3%) — the closure fails the conservative bound too.
- Negative side (q < 0.6615): Λ < 0, unconstrained by this analysis. Recorded as unconstrained, not as viable: a |Λ| of hundreds enters the phase with the opposite sign and would be visible to the same data; no published bound exists.
- The +14% shift is inside the ~30% by which the corpus's linear (C5) and nonlinear (c07) static dictionaries differ at the wall (3633 §2). **What 3650 left as "the dictionary decides the sign" is now "the dictionary must move the wall ratio up by ≥ 14% (or cross to the negative side) for the extension to survive GW250114."** A direction and a size, not a free choice.

## §4 The adiabatic caveat, and why it does not rescue the closure
3650 put the closure 0.8% from a static zero mode. Near one, the tidal response is dynamical (a low-frequency ℓ = 2 mode of the object), and a constant 5PN Λ is not the right description. Two cases: the mode in band (20–50 Hz for 33 M☉) — a resonance far larger than a constant Λ, excluded a fortiori; below band — the adiabatic Λ applies and is excluded. The closure at q = 2/3 does not survive on either branch. The mode frequency itself is the owed 3643 re-run.

## §5 Standing
- PRED-O-40: **TESTED COLD.** The register closure's static junction at the c07 dictionary value is excluded; the R-core with any pre-3650 surface reading is not. Row 6 stays OPEN with the survival window attached: q ≥ 0.762 or negative side.
- OPEN-GR-LATTICE-FRAME-1 (static face): promoted from "decides the sign" to **"decides survival"** — the count↔lapse dictionary at v = 2/3, to better than the 14% margin, in the direction K/H > 2/3.
- Alternatively, the induced ℓ = 2 surface layer of 3650 §5 (1% residual) is the other place a shift could come from; it is a 1% effect, an order of magnitude too small unless the perturbed layer's own law is stiff. Recorded; not pursued here.
- V2.3 must carry this section. CONV-042 (the extension round) now has a live empirical stake.
