# The 5:1 ratio (Ω_DM/Ω_b ≈ 5.36): scoping the routes — not derivable as a first-pass; route B (asymmetric DM) is the promising direction

**Patch:** 0843 (Session 156, 10 June 2026) · **Type:** scoping/assessment (NOT a derivation). · **Lane:** DM-2 / `dark_matter/` (no shared-file touch; collision-safe vs Project C window).
**Sharpens:** Step 2 (Patch 0704) requirement **R1**. **Verify:** `code/0843_relic_abundance_scoping.py`.

---

## Where the 5:1 stands

Step 2 (0704) already settled the status honestly: the dark-to-baryon ratio Ω_DM/Ω_b ≈ 5.36 is **not derived** — it is relocated to the free primordial swirl-overdensity amplitude (δ ≈ 10⁻⁴⁷), "exactly as unexplained as ΛCDM's Ω_DM/Ω_b." Nothing in the eDP:qDP lock or the hTetra freeze-out pins the overall ratio to ~5. This patch does not change that; it surveys what a CPP-native derivation would require and judges which route, if any, is realistic. This is the *other* calibrated input (alongside the absolute mass scale = Project C) and the remaining piece of a fully standalone DM-1.

## Three candidate routes

**(A) Shared-origin freeze-out.** DM (qDP/hTetra swirls) and baryons (quark cages) both condense from the same Dipole Sea; the ratio is the relative survival of frozen-out swirls vs the baryon relic. But the baryon relic is set by the asymmetry η ≈ 6×10⁻¹⁰ (itself a CPP baryogenesis problem, undeveloped) and the swirl amplitude is the unexplained δ. A ratio of two undetermined quantities is not a derivation.

**(B) Asymmetric dark matter via a shared Sea asymmetry — the structurally promising route.** If the qDP/hTetra number density is tied to the *same* asymmetry that produces baryons, then Ω_DM/Ω_b = (m_DM/m_p)(n_DM/n_b), which naturally yields an O(1)–O(10) ratio rather than two independent fine-tunings. The bookkeeping:

| DM unit | m_DM [GeV] | required n_DM/n_b for 5.36 |
|---|---|---|
| single qDP | 0.264 | 19.0 |
| single hTetra (~3× qDP) | 0.79 | 6.4 |
| ~5 m_p aggregate | 4.7 | 1.07 |

The canonical ADM result (n_DM ~ n_b from one shared asymmetry) requires the DM **unit** to be a heavy aggregate (~4.7 GeV ≈ ~18 qDPs or a few hTetras), not a single qDP. Two things make this route attractive in CPP specifically: it converts the coincidence into a *structural* ratio, and CPP has a **native asymmetry candidate** — the DP-Sea polarity/chirality asymmetry developed in the substrate chirality arc — which could be the common source feeding both the baryon and DM asymmetries. But it is not closeable now: it needs the DM-unit mass/composition (Project-C-adjacent) and the shared-asymmetry mechanism (connects to CPP baryogenesis + the chirality arc), neither derived.

**(C) Symmetric thermal relic.** qDP/hTetra as a WIMP-like thermal relic, abundance set by the annihilation/recombination cross-section at freeze-out (⟨σv⟩ ~ 3×10⁻²⁶ cm³/s for Ω_DM ~ 0.26). Note this is the *annihilation/aggregation* cross-section — **not** the elastic σ_V ≈ 0.20 cm²/g derived this session (0841), which governs halo self-interaction, a different quantity. Needs the qDP annihilation channel and freeze-out temperature — open.

## Verdict and recommendation

The 5:1 is **not derivable as a first-pass.** Each route bottoms out in an undeveloped CPP sub-sector — baryogenesis (the asymmetry η), the qDP/hTetra production/aggregation history, or the DM-unit mass. The **most promising direction is route B** (asymmetric DM via a shared Sea asymmetry), because it is the only one that turns the coincidence into a structural O(1) ratio and because CPP already has a candidate asymmetry (the substrate chirality/polarity arc) to feed it. Recommend registering R1 as a **scoped open problem** pointing at route B, explicitly paired with: (i) the DM-unit mass/composition (Project-C-adjacent), and (ii) a CPP baryogenesis/asymmetry sub-arc.

## What this means for the publication-track paper

The σ_V/m discriminant paper (0840–0842) **does not depend on the 5:1.** It stands on the derived, falsifiable self-interaction signature; the abundance ratio is an *inherited/calibrated* input there, on par with ΛCDM — and should be stated as such, not hidden. The 5:1, like the Sea-gravitation gate (DM-2) and the absolute mass scale (Project C), is part of the *full identification* program, not the microphysics-plus-discriminant result that is publishable now. No verdict/THEO/ID; conditional on the qDP/hTetra-DM conjecture.
