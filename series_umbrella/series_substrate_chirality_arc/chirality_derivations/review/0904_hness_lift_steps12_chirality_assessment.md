# Chirality-lane review — H-NESS lift Steps 1–2 (assessment of Patch 0813)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0904_hness_lift_steps12_chirality_assessment.md`
**Patch:** 0904 · **Reviews:** Patch 0813 (DM/F.1 window — 600-cell build + local η + symmetric χ_η in product base)
**Disposition:** Favorable-branch **conditional infrastructure input**. **No verdict move. 0903 stands unchanged.** Header count unchanged; OPEN-CHIR-1d-β and OPEN-SM-4 remain OPEN.

---

## 1. What 0813 established (accepted)

- **600-cell built correctly:** 120 unit-quaternion vertices, degree-12 adjacency at edge 1/φ — the genuine {3,3,5}. ✔
- **η proxy:** a local signed-determinant pseudoscalar over the canonical-frame top-projection neighbours; flips under global reflection; homogeneous mean ≈ 0 (correct — the bare 600-cell is achiral, H₄ has reflections). A defensible *local ℤ₂ enantiomorph indicator*. ✔ (proxy, not yet the confirmed H₄/H₄⁺ field — see §3.)
- **Computation:** in the product (ZRP-template) base the connected correlator is on-site ≈1 and at noise level for all d ≥ 1 ⇒ **χ_η ≈ 0.87–1.01, finite, positive, on-site-variance dominated, robust over perturbation strength.** ✔
- **Landau chain:** χ finite-positive ⟺ χ⁻¹ = 2μ² > 0 ⟺ η = 0 is the stable vacuum. ✔

## 2. Framing correction (load-bearing — the result is the opposite of "emergent")

μ² > 0 / η = 0-stable is the **UNBROKEN (symmetric) branch**: the dynamics provably do **not** condense a chiral order parameter. In verdict language this is **V3 *confirmed*** — FI-C-9 remains a primitive/inherited input because the engine does not generate it — and it **forecloses** the condensation route to V1 (which is the μ² < 0, broken branch).

The 0813 gloss "V3 stands by principle (emergent)" and "chirality emergent at the engine level" is **inverted**. The correct statement: *on this branch the engine is handedness-neutral, so chirality is not dynamically generated and stays primitive (V3); V1-by-condensation is the branch this result excludes, not supports.* Read literally, the computation shows the **absence** of dynamically-generated handedness — not an active handed bias of the substrate.

## 3. The gate is not lifted (why this does not touch 0903)

The finiteness of χ_η follows **almost tautologically from the product base**: in a zero-correlation-length measure, χ = Σ_r⟨η₀η_r⟩_c collapses to the on-site variance, so "finite" is *inherited*, not independently derived. The computation confirms off-criticality **given** an off-critical field measure; it does not establish that the actual η-*field* measure is off-critical. That step is exactly the F.1 §14.17 content the 0903 closure named as the open gate. The decisive thing was assumed, not shown.

**Conditions that must close before any verdict move (the chirality-lane gate):**
1. Confirm the precise **H₄/H₄⁺ order-parameter field is local** (finiteness is robust to the exact local form, but "local" must hold for the true field, not just the proxy).
2. Confirm the η-**field correlator** (not merely the ZRP occupation template) inherits the product/off-critical structure.
3. Mechanism A (OPEN-FP-F1-2) remains a framework axiom underneath the whole route.

Conditions (1)–(2) are §14.17-level work and sit in this lane; until both close, this is a favorable-branch conditional input, not a confirmation that moves V3.

## 4. Guard against over-reading

This result does **not** show the substrate "choosing" a handedness at a primitive level. It shows handedness-*neutral* dynamics that leave the observed chirality encoded in the already-named primitive **FI-C-9 = sign(n̂)** (the orientation pseudoscalar) as an input — i.e. a conditional confirmation of the existing V3 picture (MERGE-2 already reduced all chirality to FI-C-9), not a newly-discovered axiom. It is also premature to elevate to "chirality is a settled axiom": V3 is "not-yet-derived," and V3 deliberately keeps the V1 (derivable) route open; a single conditional, assumption-laden, single-branch computation does not foreclose it in either direction. The worthwhile follow-on is *descriptive* — state cleanly what sign(n̂) is and where it enters the axioms — not a new ontological claim.

## 5. Step 3 (O(δ³) current)

Agreed it is a **refinement, not a sign-gate**: with χ ≈ 0.87–1.01, μ² ≈ 1/(2χ) sits well away from zero, so a perturbative O(δ³) current shifts μ² but cannot flip its sign — **provided** the O(δ³) term is genuinely perturbative relative to μ². Worth running for DM-2's quantitative residual skew; it cannot change the chirality read either way.

## 6. Disposition

Recorded as a chirality-lane assessment answering the DM window's hand-off. **0903 (determination-arc closure) is unchanged.** The deep V3→V1 engine stays OPEN and gated on §14.17; the next real chirality work is closing conditions (1)–(2) above. No THEO, no ID, no count change.

---

## Addendum — Patch 0905 (cross-lane resolution + gate sharpening)

**Cross-lane resolution.** The DM/F.1 lane accepted the framing correction and retracted the inverted "emergent" label in its own records (Patch 0815): μ² > 0 / V3 = chirality **primitive/inherited** (engine handedness-neutral, unbroken branch); the *emergent* outcome would be the μ² < 0 condensation branch, which this is not. Chirality lane confirms the resolution. No verdict change.

**Gate sharpening — condition (2) now has indication *against*, not merely "unconfirmed."** The DM lane reports (0815, citing its own 0814) that the real Mechanism-A NESS **departs from the clean product (ZRP-template) base** on which 0813's finite-χ was computed. Consequence for this review: the finite-positive χ_η of 0813 sits on an idealized base the dynamics do not satisfy, so **finite χ is not established for the real η-field measure** — it must be recomputed on the actual measure.

Precise logic (to prevent a second inversion): "departs from product" (current structure / non-Gaussian features) is **not** the same as "critical." Off-criticality (finite correlation length) is a separate property from being exactly product, so this **reopens the χ computation on the real measure rather than flipping the sign** — the recomputed χ could still be finite (off-critical but non-product) or could reveal correlations; unknown until computed, and that computation *is* the §14.17 content. (The DM lane's 0810 separately argues a NESS *current* can coexist with a *symmetric* equal-time distribution — current ≠ skew — so the real measure's internal structure is itself unsettled; the chirality lane does not adjudicate that here, only notes that the product-base assumption underpinning 0813's finite χ is not safe.)

**Disposition unchanged.** 0903 and the §14.17 gate stand; this only moves condition (2) from "assumed/unconfirmed" to "the base used is known to differ from the real measure → recompute required, §14.17-gated." No verdict, no THEO, no count change. In-bounds next chirality move: the **descriptive sign(n̂) task**. Parked (§14.17-gated): recompute χ_η on the real Mechanism-A measure.
