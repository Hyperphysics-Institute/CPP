# The proper SIDM cross-section: identical-boson viscosity σ_V/m ≈ 0.20 cm²/g (velocity-independent)

**Patch:** 0841 (Session 156, 10 June 2026) · **Type:** first-pass — tightens 0840's O(1) factors into a definite number. · **Lane:** DM-2 / `dark_matter/` (no shared-file touch; collision-safe vs Project C window).
**Builds on:** 0840 (σ/m flat), 0833 (qDP identical bosons). **Verify:** `code/0841_viscosity_cross_section.py`.

---

0840 quoted the distinguishable s-wave total σ₀/m ≈ 0.15 cm²/g and flagged two O(1) corrections (identical-boson ×2, viscosity ×⅔). The SIDM-relevant quantity is the **viscosity cross-section** σ_V (weighted by 1−cos²θ — symmetric under θ→π−θ, the correct choice for identical particles, and the one that matches the cross-section used in SIDM N-body calibrations). This patch evaluates it properly.

**For pure s-wave identical bosons, σ_V = (4/3)·σ₀** — the ×2 from identical-boson symmetrization [amplitude f(θ)+f(π−θ), half-range integration] times the ×⅔ from the (1−cos²θ) weighting on isotropic s-wave scattering. So the two O(1) factors do not cancel; they combine to ×4/3.

| f | σ₀/m (distinguishable total) | **σ_V/m (identical-boson viscosity)** |
|---|---|---|
| 0.10 | 0.205 | 0.274 |
| **0.20** | 0.148 | **0.197** |
| 0.35 | 0.072 | 0.097 |
| 0.50 | 0.019 | 0.025 |
| 1.00 | 0.248 | 0.331 |

**Central: σ_V/m ≈ 0.20 cm²/g** (f-band ≈ 0.03–0.27, Ramsauer dip near f≈0.5). It is **velocity-independent** to four digits across 30–3000 km/s (same kλ≪1 argument as 0840; higher partial waves negligible, δ₂/δ₀ ~ (kλ)⁴ ~ 10⁻¹⁰–10⁻²⁴).

So the 0840 result firms: the proper SIDM viscosity cross-section is **σ_V/m ≈ 0.20 cm²/g, velocity-independent**, with the factor-3 magnitude uncertainty still inherited from f (0835). This is the number to compare against system-by-system SIDM constraints and to feed into the core-radius estimate (0842). Scope: first-pass, pure s-wave (justified), no verdict/THEO; conditional on the qDP/hTetra-DM conjecture, the Mechanism-A measure, and f≈0.2.
