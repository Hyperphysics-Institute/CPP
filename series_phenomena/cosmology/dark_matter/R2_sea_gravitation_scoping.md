# DM Arc — R2: The Sea-Gravitation Question (scoping)

**Patch:** 0705 (Session 149, 31 May 2026) · **Work item:** OPEN-COSMO-DM-1 R2 · **Gated on:** OPEN-SR-5
**Status:** scoping deliverable (not a calculation). Outcome: the question is **more favorable** than Step 2 implied — there is a candidate resolution *and* a dark-energy↔dark-matter unification angle — but the resolution is **not yet derived**, and one specific thing must be shown.
**Verify:** `scripts/0705_lambda_sea_estimate.py`

> **⟨UPDATE — Patch 0846 (DM 08xx lane), applying CC-umbrella handoff Patch 1105 (CC-U/5).⟩**
> **The §3 "not derived / coincidence-restatement" framing and the §5 "do not write up yet" posture below are superseded** by SR-5 Steps A–D (Patches 0720–0723) and the cosmological-constant umbrella (Patches 1101–1104):
> - **Suppression derived (Step C).** ρ_Λ = c²H²/8πG = (1/8π)ρ_P(l_P/R_H)² — both the (l_P/R_H)² scaling *and* the 1/8π coefficient are now derived from the substrate rather than inserted. §3.1's "coincidence-restatement" verdict no longer holds.
> - **Horizon ambiguity resolved (Step D3).** The future event horizon is selected (Li 2004), giving w_Λ(now) ≈ −1.02. The ~10× horizon-choice swing flagged in §3.1 is closed.
> - **Friedmann recovered (Step D1).** The expansion history follows, with q crossing zero (acceleration onset) at z ≈ 0.63. The make-or-break test posed in §3 / §4(iii) is met.
> - **"Why-now" reframed.** The dynamical ρ_Λ ∝ H² is now the *resolution* of the coincidence problem (Λ larger in the past), per the umbrella's static-vs-dynamical verdict (dynamical). The static N⁴ reading of §2(b) is demoted to a present-epoch coincidence (1/N⁴ ≈ (l_P/R_H)² because R_H ≈ N²l_P today).
>
> **Net for R2:** the **uniform-Sea-inert / dark-energy leg is in hand**, conditional on the **c08 closed field equation (op:einstein)** — the single standing cap, shared with the dark-matter split (see `series_umbrella/series_cosmological_constant_arc/`, Patches 1101–1104, and CC-U/4 scoping `1105_ccu4_c08_scoping.md`). The §4(ii) gravitating-swirls-at-DM-amplitude leg and the full DM identification remain this lane's open work (DM-1 draft `DM-1_draft_manuscript.md`). This does **not** revive structure formation — CONJ-COSMO-1's structure-formation role stays a separate standing conditional-false verdict (Patch 0729). **Treat §3–§5 below as the frozen 0705 snapshot.**

> **⟨UPDATE — Patch 0855 (DM 08xx lane): the c08 cap is DISCHARGED.⟩**
> The Patch 0846 note above left the uniform-Sea-inert / dark-energy leg "conditional on the c08 closed field equation (op:einstein) — the single standing cap." **That cap is now discharged (Patch 1161).** The op:einstein closure derives G_μν = 8πG/c⁴·T_μν[LSP] at λ = 16πG/c⁴ with **zero new parameters** (DG-3 3/3), and the absolute-|SSV| monopole is annihilated by 600-cell icosahedral symmetry (spherical 5-design, Σv̂ = 0; Patches 1107–1108) → **D2 (ground-state exclusion) CLOSED, falsifier D2-1 refuted** (formerly the single most load-bearing risk). The R2 uniform-Sea-inert leg therefore now stands on a **derived** field equation, no longer conditional on c08.
> **Remaining open condition:** the **event-horizon IR-scale selection** (falsifier D3-1) — the one cap shared with the CC / Project-C l_P excavation. Net: R2's dark-energy leg is in hand on a derived field equation; a single cosmological IR-scale condition remains. **Still conditionally supported, not promoted to a derived result.** (Cross-ref DM-1 §9, Patch 0855; `series_phenomena/cosmology/sea_gravitation/stepD_friedmann_and_checks.md`, D2 CLOSED.)

---

## 1. The question (restated precisely)

Step 2 surfaced the requirement R2: for free qDP/hTetra concentrations to be dark matter, the *uniform* ambient Sea must not produce a catastrophic cosmological gravitation (Ω_Sea ~ 10⁴⁵–10¹²⁰ if it gravitated at full density), while the Sea's *inhomogeneities* must gravitate as DM. Step 2 phrased this as "the uniform Sea must not gravitate" — which, it turns out, is too strong. The accurate requirement is more interesting.

## 2. What the gravity foundation already says (the favorable part)

**(a) CPP gravity is gradient-sourced (c05).** The force is F = m'c²·k·∇(ΔSSV) — the gradient of net SSV, not its absolute value. So a *uniform* Sea exerts no local force **by construction**. The "only inhomogeneities gravitate locally" property the DM picture needs is not an added assumption; it is how c05 already works. This removes the appearance of special pleading.

**(b) The uniform Sea has a candidate cosmological role: Λ (c08 dev notes).** The c08 development notes record an estimate that the vacuum SSV of the DP sea *is* the cosmological constant: ρ_Λ ≈ α_geom·(E_P/l_P³)·(l_P/R_H)². So the uniform Sea is not required to be gravitationally inert *cosmologically* — it can source dark energy, suppressed from the Planck density by the horizon-scale factor.

**(c) The unification angle.** Taken together, the **same** Dipole Sea would source **both** dark energy (its uniform mode → suppressed Λ) **and** dark matter (its swirl inhomogeneities → unsuppressed local-gradient gravity). That is a genuine dark-sector unification: two of cosmology's three dark puzzles from one substrate, distinguished only by uniform-mode vs gradient-mode. If it holds up, it is a significant claim — and it is the strongest reason to keep pushing CONJ-COSMO-1.

## 3. What is NOT derived (the honest part)

The c08 Λ estimate is **unregistered development-notes material**, attributed to a Grok session and verified by Claude only as *numerically close*. Two problems:

1. **Horizon sensitivity (= the coincidence in disguise).** `scripts/0705_lambda_sea_estimate.py` reproduces the estimate and varies R_H: the Hubble length gives 6.78× the observed Λ, the particle horizon gives 0.66× — a ~10× swing on a choice CPP does not fix. The factor (l_P/R_H)² ~ 10⁻¹²² is exactly the well-known Λ ~ 1/R_H² near-coincidence; getting "factor 1.5" requires choosing the particle horizon. As it stands this is a **coincidence-restatement, not a derivation**: nothing in CPP yet derives *why* the vacuum SSV is suppressed by (l_P/R_H)², nor which horizon enters.

2. **Time-dependence / "why now."** R_H grows with cosmic time, so a vacuum density tracking 1/R_H² is *dynamical*, not a true constant — inheriting (not solving) the standard coincidence problem unless the suppression mechanism explains the constancy.

And the make-or-break test remains untouched: **does "uniform mode → suppressed, gradients → unsuppressed" reproduce the Friedmann expansion?** Standard cosmology's matter and radiation eras manifestly *do* respond to uniform energy density (the universe decelerates under uniform matter). A CPP cosmology in which the uniform Sea contributes only a tiny suppressed Λ must still recover the observed expansion history sourced by uniform matter/radiation. That dynamics does not yet exist (OPEN-SR-5 is a 23-March stub; c07/c08 list "Friedmann from homogeneous isotropic DP sea" as future work).

## 4. The scoped requirement (what OPEN-SR-5 must now deliver)

A single CPP cosmological sector must yield, from one mechanism rather than three assumptions:
- **(i)** the uniform Sea mode → a vacuum/Λ contribution suppressed to ~observed magnitude, with the suppression factor **derived** (not the inserted (l_P/R_H)²) and the horizon ambiguity resolved;
- **(ii)** Sea inhomogeneities (swirls) → unsuppressed local-gradient gravity of the right amplitude to be DM (this is also where R1, the DM/baryon ratio, must be confronted — the swirl spectrum sets both);
- **(iii)** the standard Friedmann expansion history (matter/radiation/Λ eras) recovered, including that uniform matter/radiation gravitate cosmologically even though the uniform *Sea* mode is suppressed — i.e., a principled distinction between "Sea vacuum mode" and "matter/radiation overdensities on the Sea."

Until (i)–(iii) exist as one derivation, CONJ-COSMO-1's quantitative cosmology (Steps 4–5) rests on an unbuilt foundation.

## 5. Recommendation

R2 does **not** kill the arc — it upgrades its ceiling (the DM↔Λ unification is a real prize) while pinning the single load-bearing gap (a derived Sea-gravitation/expansion sector, not the coincidence-level Λ estimate). Concretely:

- **Elevate OPEN-SR-5** from stub to the scoped problem in §4, carrying the DM dependency; make the OPEN-COSMO-DM-1 ↔ OPEN-SR-5 link bidirectional (done this patch).
- **Treat OPEN-SR-5 as a hard prerequisite** for DM Steps 4–5; do not attempt quantitative power-spectrum or rotation-curve work until at least (iii) exists.
- **Do not write up CONJ-COSMO-1 yet.** Both kill-gates survived, but the honest headline is "no showstopper; a promising dark-sector unification; one unbuilt cosmological sector it all rests on." The paper-worthy result is the unification *once the sector exists*.
- **Cheap parallel work that does not depend on OPEN-SR-5:** Step 3 (coldness — qDP/hTetra velocity dispersion at decoupling) is a self-contained kinematic estimate and can proceed independently. Step 4 (power spectrum) cannot — it needs the expansion dynamics.

The most valuable next physics move is therefore either to begin scoping the OPEN-SR-5 cosmological sector proper (a large undertaking, arguably its own arc), or to knock out Step 3 (coldness) as the last cheap self-contained gate while the cosmological sector is contemplated. That fork is for Thomas.
