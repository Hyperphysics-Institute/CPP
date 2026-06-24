# DM-1 (DRAFT): Dark Matter as a Velocity-Independent Self-Interacting Species of Charge-Neutral qDP/hTetra Aggregates

**Status:** working draft assembled from Patches 0700–0843 (Session 156). **Grade target:** microphysics + positive discriminant (NOT full identification — see §9, §11). **Conditional on:** CONJ-COSMO-1 (the qDP/hTetra-DM conjecture) and the Mechanism-A measure. Filled sections carry content; **[OPEN]** / **[TIGHTEN]** / **[TO FILL]** mark what remains.

---

## Abstract  *(draft)*

We propose and test the hypothesis (CONJ-COSMO-1) that cosmological dark matter is composed of charge-neutral aggregates of quark-sector dipole pairs (qDPs) and hybrid tetrahedra (hTetra), the residual neutral structures of the Conscious-Point Dipole Sea. Working from the substrate, we (i) derive the microphysics of the candidate — constituent mass m_qDP ≈ 264 MeV, identical-boson statistics, and a residual two-gluon color van der Waals interaction (depth V₀ ≈ 53 MeV, range λ ≈ 1.3 fm) — and show it is automatically collisionless at the bare level, diffuse (no bound nuggets), and stable against glueball decay; and (ii) derive, from that interaction, a **velocity-independent** self-interaction cross-section **σ_V/m ≈ 0.20 cm²/g** across the full dwarf-to-cluster velocity range. The velocity-independence is a robust kinematic consequence of the heavy constituent and short range, and is the opposite of the σ/m ∝ v⁻⁴ behavior of light-mediator self-interacting dark matter (SIDM). This yields a positive, falsifiable signature: mild dwarf cores (r_core ≈ 0.1–0.3 kpc, at the small/detectable edge), flat across mass scale, consistent with cluster bounds. The candidate is distinguished from collisionless cold dark matter (σ/m = 0) and from velocity-dependent SIDM. The absolute mass scale and the dark-to-baryon ratio are inherited as calibrated inputs (on par with ΛCDM); the cosmological identification rests on the Sea-gravitation structure (DM-2), which is traversed without kill but conditional.

## 1. Introduction  *(draft)*

[FILLED] The dark-matter problem; the standard CDM placeholder and its small-scale tensions (core-cusp, diversity, missing satellites); SIDM as a response. CPP's claim: dark matter is not a new particle but residual neutral substrate structure. **Scope of this paper:** the *microphysics* of the qDP/hTetra candidate and a *positive, derived, falsifiable discriminant* (the self-interaction signature). **Out of scope (stated, not hidden):** the full cosmological identification (§9), the absolute mass scale (§8), and the dark-to-baryon ratio (§8).
[TO FILL] One-paragraph CPP-substrate primer for a non-CPP reader (DPs, the Sea, color-neutral residuals); ~3 citations to the SM/SS flagships for the constituent physics.

## 2. The candidate: qDP/hTetra aggregates  *(draft)*

[FILLED] **Constituents.** From the DP-Sea composition: binding energies E_eDP = 88, E_hDP = 152, E_qDP = 264 MeV, with E_qDP = 3·E_eDP (color factor 3) and E_hDP = √(E_eDP·E_qDP). **Constituent mass m_qDP ≈ 264 MeV** (ratio-clean; the absolute scale is §8 / Project C). **Statistics:** the qCP carries fermionic ZBW (spin-½), so the qDP pair is a **boson**; the Sea soliton ground state is spin-0. **Conjecture (CONJ-COSMO-1):** dark matter is charge-neutral (color-singlet, electrically neutral) qDP/hTetra aggregates — existing substrate structures, not a new field.
[TIGHTEN] The DM "unit" (single qDP vs hTetra vs heavy aggregate) is not pinned; it matters for the abundance (§8). State the range used.

## 3. Survival of the cheap-kill gates (necessary, not sufficient)  *(draft, condensed)*

[FILLED] The candidate survives the three cosmology-independent falsification gates with wide margins: **Step 1** (self-interaction at the bare geometric level, σ/m ~ 10⁻³ cm²/g — collisionless, ~10²–10³× below the Bullet-Cluster bound); **Step 3** (coldness — decisively cold, far above the warm-DM boundary); **Step 5** (rotation curves — passes, non-discriminating). These establish *compatibility*, not identification: a generic GeV-scale CDM placeholder passes them identically. The discriminating content is §5–§7.
[NOTE] Keep this section short in the final paper — these are the "did not die" gates; the paper's weight is on §4–§7.

## 4. Microphysics: the residual interaction  *(draft)*

[FILLED] **The residual potential.** Between color-singlet qDPs the residual is a *two-gluon color van der Waals* interaction (a color-singlet cannot emit a single gluon; the hDP is identified as the gluon). Hard core r_c ≈ 1.0 fm (eDP coat), attractive Yukawa range λ ≈ 1.3 fm, depth V₀ = f·E_qDP with **f ≈ 0.2** (color-polarizability estimate; factor-3 band 0.07–0.6) ⇒ **V₀ ≈ 53 MeV**.
[FILLED] **Consequences, all derived:** (a) *glueball-avoidance* is robust (any coat r_c > r_qDP puts the saturation density below the confinement density); (b) the candidate is *collisionless* at halo scales; (c) it is *diffuse* — no self-bound nuggets form (self-binding would need f ≳ 0.38; de Boer quantum parameter Λ ~ 0.75–2.4 ≫ He-4's 0.18, i.e. too quantum to self-bind); (d) *no near-threshold resonance* (the residual, being a van der Waals residue of E_qDP, is weaker than its source — the resonance pole sits well above), which structurally excludes the only σ/m-amplifying falsifier.
[FILLED] **Falsifiers closed this arc:** F2 (near-threshold bound state lifting σ/m by ~10³) — structurally excluded; F1 (a much lighter constituent) — m_qDP firmed at 264 MeV.
[FILLED] **Figure 1** (`figures/0849_residual_potential.png`; regenerate/verify via `scripts/0849_residual_potential.py`). *(a)* The residual potential V(r) = V₀[(r_c/r)¹² − 2(r_c/r)⁶]·exp(−(r−r_c)/λ): a hard core at r_c ≈ 1.0 fm and an attractive screened-van-der-Waals well of depth V₀ ≈ 53 MeV, range λ ≈ 1.3 fm (numerical minimum −53 MeV at 0.99 fm — consistent with f·E_qDP). *(b)* The saturation density (cores touch at spacing ≈ r_c) sits a factor (r_qDP/r_c)³ below the confinement density (spacing ≈ r_qDP < r_c): ρ_sat/ρ_conf ≈ 0.12 for a representative r_qDP ≈ 0.5 fm. So the medium saturates into a diffuse phase *before* reaching confinement — glueball-avoidance, and the conclusion follows for any r_qDP < r_c.

## 5. Discriminant I — a velocity-independent self-interaction  *(draft, core result)*

[FILLED] **Derivation.** Finite-energy partial-wave scattering of the §4 potential (m_qDP = 264 MeV). Across v = 30–3000 km/s, kλ ≈ 9×10⁻⁵ → 9×10⁻³ ≪ 1, so scattering stays in the s-wave scattering-length limit; higher partial waves negligible (δ₂/δ₀ ~ (kλ)⁴). The proper SIDM viscosity cross-section for identical bosons is σ_V = (4/3)σ₀ (×2 boson symmetrization × ⅔ viscosity weighting).
[FILLED] **Result: σ_V/m ≈ 0.20 cm²/g, velocity-independent** to four digits over the entire astrophysical range (f-band 0.03–0.27, Ramsauer dip near f ≈ 0.5). The flatness is a robust kinematic consequence of the *heavy* constituent (264 MeV) and *short* range (1.3 fm): the velocity scale for σ to acquire structure is v ~ c. This is the **opposite** of light-mediator SIDM (σ/m ∝ v⁻⁴).
[FILLED] **Overlay** (Fig. 0840): consistent with cluster bounds; at/just above the dwarf coring threshold; below the strong-core preference.
[TIGHTEN] Magnitude carries the factor-3 from f (partly Project-C-feedable). Flatness does not.

## 6. Discriminant II — observable dwarf cores  *(draft)*

[FILLED] **One-scatter density** ρ₁ = 1/[(σ_V/m)·v·t]: cores form where ρ_halo > ρ₁. At σ_V/m = 0.20, t = 10 Gyr: ρ₁ ≈ 0.08 M⊙/pc³ (dwarf), 0.0016 (cluster). **Representative dwarf core: r_core ≈ 0.27 kpc** (vs ≈ 0.81 kpc for strong SIDM σ/m = 1) — a *few-hundred-parsec, mild* core at the small/detectable edge of the observed 0.2–1 kpc range. **Cluster:** a modest core forms; σ_V/m = 0.20 is at the edge of current bounds (fine vs looser ~0.5–1, mild tension vs tightest ~0.1).
[FILLED] **Robust vs uncertain:** robust — mild (~0.1–0.3 kpc), flat across scale, detectable-edge; uncertain — the core *size* is halo-model dependent (factor ~2) on top of f's factor ~3.
[FILLED] **Specific confrontation (Fig. 2, `figures/0850_specific_dwarf_fit.png`; verify via `scripts/0850_specific_dwarf_fit.py`).** We test the velocity-*independent* σ_V/m ≈ 0.20 against two well-measured systems ~5× apart in velocity, writing the cored central density as the one-scatter density ρ₁(σ₁D) = 1/[(σ_V/m)·⟨v_rel⟩·t] with ⟨v_rel⟩ ≈ 2.26 σ₁D and t = 10 Gyr:

| galaxy | σ₁D (km/s) | ρ₁ predicted (M⊙/pc³) | ρ_obs central (M⊙/pc³) | pred/obs |
|---|---|---|---|---|
| Fornax dSph (classical) | 11 | 0.094 | 0.016–0.07 [Mateo+ 1991; Jardel & Gebhardt 2012] | 2.8× |
| IC 2574 (dwarf/LSB) | 57 (= v_max/√2, v_max ≈ 80) | 0.018 | ≈ 0.006 [de Blok+ 2008] | 3.1× |

Both observed central densities sit a *similar* factor (~3×) below ρ₁(0.20), and — the discriminating point — **the offset is flat across the 5× span in σ₁D**. A velocity-*dependent* σ/m rising toward dwarfs would drive the Fornax offset far above IC 2574's; that is not seen, so the data are consistent with the velocity-*independent* prediction and inconsistent with light-mediator SIDM's v⁻⁴ trend. The common ~3× lies within the factor-few (f × halo-model) uncertainty; if real it nudges the normalization marginally below 0.20 (cores a touch more developed than the bare one-scatter floor), still velocity-flat. Cores form in both (ρ_obs < ρ₁), consistent with their observed cores. *(This is the density test, which ρ₁ gives directly; a full core-radius confrontation — notably IC 2574's large ~8 kpc core — awaits the NFW r₁ inversion in the core-radius-vs-σ/m panel.)*

[FILLED] **Core size vs σ/m (Fig. 3, `figures/0851_core_radius_vs_sigma.png`; verify via `scripts/0851_core_radius_vs_sigma.py`).** Inverting the NFW r₁ condition ρ_NFW(r₁) = ρ₁(σ/m) turns the density test into a core-*size* prediction. For a Fornax-scale halo (V_max ≈ 25 km/s), σ_V/m = 0.20 gives r₁ ≈ 0.32 kpc — inside the observed ≲ 0.3–0.7 kpc core, with the f-band [0.07, 0.6] bracketing it: **consistent**. For IC 2574 (V_max ≈ 80 km/s), σ_V/m = 0.20 gives r₁ ≈ 1.8 kpc, **well below** its observed ~8 kpc core; that core requires σ/m ≈ 1.1–2.7 cm²/g — *above* the f-band. So the core-radius test, more constraining than the central-density test above, surfaces a **genuine tension at the high-velocity end**: the largest LSB cores want more self-interaction than velocity-independent 0.20 supplies, echoing the velocity-*dependent* σ/m ~ 1–2 that rotation-curve SIDM fits infer at galaxy scales. This is a falsifier-relevant limitation (§7), reported not hidden — its escape routes are (i) f underestimated at galaxy scale (the color-polarizability estimate carries a factor ~3), (ii) residual velocity-dependence in the residual cross-section, or (iii) IC 2574's low-concentration halo inflating the required σ/m. It carries the halo-model (c, factor ~2) and r_core/r₁ (O(1)) systematics.

## 7. Falsifiability  *(draft)*

[FILLED] The signature is the **flatness**. If the cross-system data require σ/m to *fall* from ~1–3 (dwarfs) to ~0.1 (clusters) — i.e. velocity-dependent SIDM — the flat ≈ 0.20 prediction fails on the dwarf side (too small for strong cores; it physically cannot rise at low v) and mildly on the cluster side. If the data are consistent with a flat ~0.1–0.3 across scales, CPP predicts it from first principles with no free knobs beyond f. Clean two-sided test.

## 8. Inherited / calibrated inputs (stated, not hidden)  *(draft)*

[FILLED] Two inputs are *calibrated*, on par with ΛCDM, and the paper says so plainly:
- **Absolute mass scale.** Only the *ratios* (color factor 3, geometric mean) are derived; the absolute DP/QCD scale is calibrated. Its first-principles derivation is **Project C** (Λ_QCD from l_P + sea_strength via PSR saturation).
- **Dark-to-baryon ratio Ω_DM/Ω_b ≈ 5.36.** Not derived; relocated to the primordial swirl amplitude (Step 2). The promising route is asymmetric DM via a shared Sea asymmetry (route B; possibly fed by the substrate chirality arc), but it bottoms out in undeveloped sub-sectors (the DM-unit mass; CPP baryogenesis). [OPEN]

## 9. The cosmological gate (DM-2 / Sea gravitation) — status  *(draft, REVISED)*

[FILLED] DM-2 asks: does the *uniform* Sea stay gravitationally inert cosmologically while its *inhomogeneities* gravitate as dark matter, with Friedmann recovery? Current state (sea_gravitation/, Patches 0720–0814): the falsification-first sequence A→D is **traversed twice with no kill**, and is a *conditional structure*, not a wide-open gate:
- **Step A (uniform Sea inert): SURVIVES** — this is Seeliger's paradox, resolved by Milne–McCrea (1934) Newtonian cosmology; in CPP gravity sources from ∇(ΔSSV), so a uniform Sea is inert *by construction*.
- **Step B (Sea-vs-matter distinction): structurally resolved** by the single ∇(ΔSSV) mechanism (Sea ground state = reference level).
- **Step C (Λ suppression): PARTIAL** — scaling + coefficient + factor-2 magnitude derived, *replacing* the (l_P/R_H)² coincidence-restatement with a substrate mechanism; precise coefficient + horizon choice deferred.
- **Step D (Friedmann recovery): CONDITIONAL CAPSTONE** — recovered, checks pass, resting on **two named conditions**: (1) the c08 strong-field field-equation reduction, (2) the event-horizon selection.
- **D2 (ground-state exclusion) is separable** from the hard strong-field closure (Step 1/2a), conditional on the net-broadcast lemma whose load-bearing condition (k·Δ|SSV| ≪ 1 at the ZBW scale) was **closed** at Step 2a.
[ASSESSMENT] The "uniform Sea does not gravitate" half is essentially **in hand**; the still-open work is the **Λ-suppression coefficient + horizon selection**, which overlaps the cosmological-constant / l_P excavation now running in the Project C window. So DM-1 (this paper) should *cite* the DM-2 structure as conditional-but-traversed, and not claim full identification — but the gate is far less of a wall than a "wide-open decisive gate" framing implies.

## 10. Discussion & grade  *(draft)*

[FILLED] What this paper establishes: a derived, falsifiable, **velocity-independent self-interacting** dark-matter candidate with a positive signature (σ_V/m ≈ 0.20 cm²/g, mild flat dwarf cores) that distinguishes it from both collisionless CDM and velocity-dependent SIDM — lifting the candidate from *consistency-grade* (Patch 1200) to a *positive-discriminant* result. What it does not establish: the full cosmological identification (the calibrated mass scale and abundance, §8; the conditional Sea-gravitation gate, §9). Honest one-line grade: **a viable, microphysically-derived, falsifiable SIDM candidate with a specific qDP/hTetra signature — not yet a fully-derived identification.**

## 11. What is left to fill (checklist)

1. **[TIGHTEN] f → magnitude band.** Shrinks the factor-3 on σ_V/m (partly Project-C-feedable). Flatness already robust.
2. **[TO FILL] §6 observational confrontation.** Fit 1–2 specific observed dwarfs (+ a cluster) rather than the representative NFW.
3. **[DONE] Figures.** V(r)/saturation (§4, Fig. 1, Patch 0849); σ_V(v) overlay (Fig. 0840); specific-dwarf density confrontation (§6, Fig. 2, Patch 0850); **core-radius-vs-σ/m panel (§6, Fig. 3, Patch 0851)**.
4. **[OPEN] §8 abundance (route B).** Asymmetric-DM / shared-Sea-asymmetry derivation of ~5:1 — needs the DM-unit mass + a baryogenesis sub-arc.
5. **[DEP] §8 mass scale = Project C** (running in the 1000-series window).
6. **[DEP] §9 DM-2 Λ-coefficient** — overlaps Project C's cosmological-constant/l_P work; coordinate, don't race.
7. **[TO FILL] Intro CPP primer + citations; references throughout.**
8. **[DECISION] Promotion to .tex + flagship checklist** once §6 and the f-band are in and DM-2's two conditions are reported as conditional.

## Provenance

§4 ← 0830–0836; §5 ← 0840–0841; §6 ← 0842, 0850 (specific-dwarf confrontation), 0851 (core-radius-vs-σ/m panel); §7 ← 0840/0842; §8 ← 0704 (abundance), 0833 + Project C (mass), 0843 (route B); §9 ← 0720–0814 (sea_gravitation); §3/§10 ← consolidation Patch 1200.
