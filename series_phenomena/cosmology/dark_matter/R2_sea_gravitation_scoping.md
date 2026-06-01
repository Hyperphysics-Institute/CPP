# DM Arc — R2: The Sea-Gravitation Question (scoping)

**Patch:** 0705 (Session 149, 31 May 2026) · **Work item:** OPEN-COSMO-DM-1 R2 · **Gated on:** OPEN-SR-5
**Status:** scoping deliverable (not a calculation). Outcome: the question is **more favorable** than Step 2 implied — there is a candidate resolution *and* a dark-energy↔dark-matter unification angle — but the resolution is **not yet derived**, and one specific thing must be shown.
**Verify:** `scripts/0705_lambda_sea_estimate.py`

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
