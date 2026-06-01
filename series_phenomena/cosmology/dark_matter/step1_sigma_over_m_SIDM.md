# DM Arc — Step 1: Self-interaction σ/m vs the SIDM bound

**Patch:** 0703 (Session 149, 31 May 2026) · **Work item:** OPEN-COSMO-DM-1 Step 1 · **Gate:** Gate 1 (collisionless), quantitative
**Status of result:** order-of-magnitude estimate — **NO KILL**; provisional survival with a named closure requirement.
**Verify:** `scripts/0703_sigma_over_m.py`

---

## 1. What Step 1 tests

The "cheapest potential kill." If net-neutral qDP / hTetra structures are the dark-matter constituents, their *self-interaction* cross-section per unit mass must satisfy the self-interacting-dark-matter (SIDM) bound, σ/m ≲ ~1 cm²/g at cluster scales (dwarf scales tolerate somewhat more; Bullet Cluster is the canonical constraint). Above it, the cold-collisionless identification fails and the arc would pivot to an SIDM framing or be abandoned.

**The relevant cross-section is the *residual* one** — the interaction between two *separate* color-neutral structures — not the confinement binding that holds a single structure together. This is the exact analog of the nuclear force being the short-range residual of the color force between color-neutral nucleons. (Confusing the two would wrongly import the GeV/fm string tension into a scattering cross-section.)

## 2. Inputs and provenance

| Quantity | Value | Source |
|---|---|---|
| Strong coupling α_s (at ~r₀) | 0.3 | c14 [paper] |
| Cornell crossover r₀ | 0.26 fm | c14 [paper] |
| Residual interaction range R_int | ~r₀ = 0.26 fm | **conservative estimate** — the structure's own size; "subquantum" ⇒ likely smaller, *increasing* the margin |
| qDP mass | ~0.3 GeV | **estimate** — c04 gives mass = Compton standing-wave energy but no absolute qDP value; QCD/constituent scale used as the *light* (worst-case) bracket |
| hTetra mass | ~1.5 GeV | **estimate** — charm/baryon-frame scale |
| Halo ρ_DM, v | 0.3 GeV/cm³, ~200 km/s | standard |

The two load-bearing *estimates* are the constituent mass (factor ~few) and the absence of resonant enhancement (factor up to ~10²–10³). The geometric size is deliberately conservative.

## 3. Computation

Residual cross-section, geometric: σ ≈ π r₀² = 0.212 fm² = 2.12×10⁻²⁷ cm².

σ/m = σ / (m · 1.783×10⁻²⁴ g/GeV):

| Species | m | σ/m (geometric) | margin vs 1 cm²/g |
|---|---|---|---|
| qDP (light — the binding case) | 0.30 GeV | 4.0×10⁻³ cm²/g | **252× below** |
| hTetra (charm/baryon frame) | 1.5 GeV | 7.9×10⁻⁴ cm²/g | **1259× below** |

Collision-rate cross-check (Γ = ρ(σ/m)v, over a Hubble time): the light qDP channel gives **~0.02 collisions per particle per Hubble time** at halo density — effectively collisionless, consistent with the σ/m margin and with Bullet-Cluster behavior.

Enhancement stress test (multiply σ by a near-threshold resonance factor):

| Enhancement | qDP σ/m | hTetra σ/m |
|---|---|---|
| ×1 (geometric) | 4.0×10⁻³ — PASS | 7.9×10⁻⁴ — PASS |
| ×100 (nucleon-like) | 4.0×10⁻¹ — PASS | 7.9×10⁻² — PASS |
| ×1000 (strong resonance) | 4.0 — **FAIL** | 7.9×10⁻¹ — PASS |

## 4. Verdict

**No kill at Step 1.** The geometric estimate clears the SIDM bound by ~2–3 orders of magnitude for both species, and the collision rate is ~0.02 per Hubble time — robustly collisionless. The survival is not fragile: even nucleon-like resonant enhancement (×100) passes. The light qDP channel fails *only* under an extreme ×1000 near-threshold resonance.

This is the most important green light the arc could get from its cheapest test: the cold-collisionless identification is quantitatively viable, not merely "no obvious showstopper."

## 5. What this sharpens (Gate-1 closure requirement)

Step 1 converts the vague "Gate 1 survivable" into one concrete requirement: **bound the residual qDP/qDP and qDP/hTetra scattering length** to rule out the pathological ×~10³ near-threshold resonance in the light channel. Two honest gaps feed this:

1. **Constituent mass.** An absolute qDP/hTetra mass (vs the present QCD-scale estimate) would firm up the margin. Natural next computation from c04's ZBW machinery + the qCP cage. A *lighter* qDP would erode the margin (σ/m ∝ 1/m), so this is the variable to pin down.
2. **Residual potential shape.** Whether the color-neutral qDP/hTetra residual interaction supports a near-threshold bound state (large scattering length) — the only thing that could lift σ/m by the required ~10³. Requires the residual (van-der-Waals-like) color potential between neutral structures, not yet computed in the companion set.

Neither gap threatens the headline (survival is robust to ×100); both define the Gate-1 closure deliverable. **Recommended:** proceed to Step 2 (bookkeeping — the second-cheapest kill) before investing in the residual-potential computation, since a Step-2 failure would moot it.
