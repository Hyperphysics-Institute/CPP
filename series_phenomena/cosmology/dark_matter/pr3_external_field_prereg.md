# PR3 EXTERNAL-FIELD SUSCEPTIBILITY — PREREGISTRATION (FROZEN)

**Patch 2819. Frozen 2026-07-26 BEFORE any measurement. Authority:
PR3 frozen text (kinetic1_returns_adjudication §5): "Weak external
charge potential at ≥3 small wave numbers; the directly measured
χ(k,0) agrees with the unperturbed-S_zz-inferred susceptibility within
combined uncertainty — TESTING, not assuming, the fluctuation-response
bridge (and probing directional components, discharging part of R8)."
Executed on the committed 2761-lineage soft-core Ewald Metropolis
machinery (the model all screening results rest on), NOT on the
automaton.**

## §1 — The identity under test (stated before measurement)

With charge structure factor ρ_k = Σ_i σ_i e^{−i k·x_i} and
S_zz(k) = ⟨|ρ_k|²⟩₀ / N measured in the UNPERTURBED ensemble, classical
linear response predicts, for a weak external potential coupling
H_ext = A·Re[ρ_{−k}]:

  **⟨Re ρ_k⟩_A / A = − β · ⟨|ρ_k|²⟩₀ / 2 = − β N S_zz(k) / 2**

(the factor ½ from the real-part projection of a complex mode).
**Committed test statistic: the RATIO**
 **Λ(k) ≡ [measured ⟨Re ρ_k⟩_A / A] / [− β N S_zz(k) / 2]**,
which equals 1 if the fluctuation-response bridge holds.

## §2 — Frozen protocol

- **Model/machinery:** committed 2761 lineage verbatim (L_UNIT = 0.589
  fm, a = L_UNIT/φ, soft-core Ewald, θ per the committed convention),
  N = 432, a_s = 0.02, geometry from the committed ladder.
- **Wave numbers [W]:** the **four** smallest committed k-shells
  (n² = 1, 2, 3, 4) — exceeds PR3's ≥3 minimum; k along all available
  shell directions, giving the directional probe PR3 requires.
- **Amplitudes [W]:** A ∈ {A₀, 2A₀} with A₀ chosen so the induced
  |⟨Re ρ_k⟩| stays ≤ 5% of √⟨|ρ_k|²⟩₀ (linear-regime guard);
  **linearity is CHECKED, not assumed** — the two amplitudes must give
  consistent Λ within combined error, else the leg reports
  NONLINEAR-REGIME and no verdict.
- **Sampling:** eq 400 sweeps, production 3000, sample every 10;
  unperturbed reference chain run at the SAME length and seed family.
- **Errors:** 24-block × 2000-resample block bootstrap on every
  verdict quantity (campaign standard).
- **Seeds:** 20260820 (unperturbed), 20260821–20260828 (perturbed:
  4 shells × 2 amplitudes).

## §3 — Frozen verdict classes

- **PR3-PASS:** Λ(k) consistent with 1 within combined bootstrap
  uncertainty at **≥ 3 of the 4** shells, AND the two amplitudes agree
  (linearity guard), AND no shell shows Λ deviating from 1 by more
  than 3σ.
- **PR3-FAIL:** ≥ 2 shells deviate from 1 by more than 3σ, or the
  linearity guard fails.
- **PR3-UNRESOLVED:** otherwise (including error bars too wide to
  discriminate — reported as such, not as a pass).

Directional component: Λ reported per shell direction; anisotropy
beyond combined error is reported as an R8-relevant finding
(report-only, no verdict weight — R8's discharge is a separate act).

**Freeze declaration:** every wave number, amplitude rule, statistic,
error model, seed, and class boundary above was fixed before any
number was computed. Enactment of PR3's status is panel business.

---

## EXECUTION RECORD (Patch 2820) — **PR3: UNRESOLVED (underpowered by design)**

**Executed 2026-07-26 under the frozen protocol above. Script:
`code/2819_pr3_external_field.py` (committed 2790 Ewald/Metropolis
machinery, unmodified, plus H_ext = A·Re[ρ_{−k}]).**

**Unperturbed reference (seed 20260820, n² = 1):**
⟨|ρ_k|²⟩₀ = 112.5083 ± 9.6789 (S_zz = 0.2604), acceptance 0.94.
Predicted response slope −βN S_zz/2 = −1.6004 per unit A.
Frozen 5% linearity guard ⇒ **A₀ = 0.331**.

**Perturbed legs (n² = 1):**
| A | ⟨Re ρ_k⟩_A | Λ(k) | σ from 1 |
|---|---|---|---|
| A₀ = 0.33 | +0.4067 ± 0.7915 | −0.770 ± 1.499 | 1.18 |
| 2A₀ = 0.66 | −1.3864 ± 0.9594 | +1.313 ± 0.908 | 0.34 |

**VERDICT: PR3-UNRESOLVED**, per the frozen class "error bars too
wide to discriminate — reported as such, not as a pass." Both legs
are formally consistent with Λ = 1 (1.18σ and 0.34σ), and the 2A₀ leg
recovers the predicted sign and magnitude — but the uncertainties
(±1.50 and ±0.91 on a quantity whose test value is 1) cannot
discriminate the bridge holding from it failing by a factor of two.
**Consistency at this precision is not evidence.**

**DESIGN DEFECT DISCLOSED (D-PR3-1, same-font, against the leg's
interest):** the frozen 5% linearity guard and the frozen chain length
(3000 sweeps, 300 samples) are jointly incompatible. The guard caps
the signal at 5% of the RMS fluctuation, while the sampling error on
⟨Re ρ_k⟩ is ~10% of that same RMS — i.e. **the design guarantees a
sub-unity signal-to-noise ratio before any data is taken.** Power
analysis: reaching 3σ discrimination of Λ = 1 at 2A₀ requires ≈ 8×
more samples; 5σ requires ≈ 21×. The remaining shells (n² = 2, 3, 4)
were NOT run: at identical design power they cannot change the
verdict, and running them would spend compute to decorate an
UNRESOLVED. Reported unrun with reason, per campaign standard.

**Successor requirement (for a fresh prereg, not enacted here):**
either (a) production ≥ 25,000 sweeps per leg at the frozen guard, or
(b) a relaxed guard with linearity verified across ≥ 3 amplitudes
rather than assumed from 2, or (c) a variance-reduction estimator
(e.g. measuring the response via the perturbation's conjugate
correlation rather than the raw mean). **The worker declines to choose
after seeing data**; PR3 remains PARTIAL and PR6's external-field leg
remains open.
