# DM-1 Review Package v1.2 — OPEN-SS-43 resolved by campaign: η = χ, the measured floor, and a superseded convention (re-ratification request)

**Artifact:** DM-1 v1.2-DRAFT — quantitative resolution of the conditionality you ratified at v1.1, plus supersession of two v1.1 statements (the capture-only cluster-safety numbers and the ε·0.11·N floor convention).
**Patches:** 1863–1873 (the OPEN-SS-43 campaign) + 1874 (the §5 v1.2-DRAFT notice). Campaign record: `OPEN-SS-43_Rs_derivation.md` §§5–18; per-patch verbatim reasoning 1863–1874; verify scripts in `code/`.
**What changed and why you are being re-consulted:** at v1.1 you ratified 4/4 with dwarf cores CONDITIONAL on OPEN-SS-43 ("R_s never derived; honestly reverse-engineered") and cluster safety quoted from the capture term. The campaign has since (a) pinned the empirical dwarf target from the published SIDM literature, (b) found that the Capotauro constant η = χ = φ⁻³/6 lands the screening length inside that window at N ≈ 15–20 and survives every confrontation run, (c) discovered — via a four-step, fully recorded correction chain — that the v1.1 floor convention overestimated transport ×4–6, and (d) replaced it with a directly *measured* floor from a soft-potential rigid-body Monte Carlo at registry-pinned geometry, under which the full cluster bound ladder passes. You are asked to ratify the v1.2-DRAFT notice (or refute/restate specific claims), with particular attention to the correction chain: this is the second consecutive version in which load-bearing v-prior numbers were caught in-house, and the process note you requested at v1.1 is continued here.
**Grade claimed (v1.2-DRAFT):** robust = velocity-dependent self-interaction passing dwarf pin, LSB, full cluster ladder (incl. Andrade < 0.13, ×2.7–4.5 margin), and Bullet, with the floor measured not conventioned. Zero-parameter candidate = η = χ (equivalently gap m_s = χ·ħc/r_c = 7.76 MeV), N ≈ 15–20 selected by the np scattering channel. Conditional = the de-novo derivation of that gap (the sharpened OPEN-SS-43 target) — until derived, χ is a surviving candidate value, not a theorem. Layer-C consistency, strengthened. No THEO registered.

**Full sources (inline content below is authoritative; links are provenance only):**
- Paper: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/DM-1/DM-1_substrate_dark_matter_candidate.tex
- Campaign file: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_phenomena/cosmology/dark_matter/OPEN-SS-43_Rs_derivation.md
- Registry: https://github.com/Hyperphysics-Institute/CPP/blob/main/frontier_sectors/SS.md (OPEN-SS-43)

**Responses aggregate in:** `series_phenomena/cosmology/dark_matter/DM-1/review/reviews-DM-1.md`.

---

## §1. Context (cold-start; skip if you reviewed v1.1)

DM-1's candidate is the Cross-Rod: a rod of N cube elements (8 qCP color-balanced core + 8 eCP shell, m_el = 1408 MeV). v1.1 (which you re-ratified 4/4) corrected the velocity-dependence mechanism from fragmentation to **capture** — the screened unipolar E_qq residual, Sea-screened at length R_s — and left two open flanks: the dwarf-core magnitude was CONDITIONAL on deriving R_s (~15–30 fm needed), and the elastic floor was fixed by convention at σ_T/m = ε·0.11·N, ε ≈ 0.30.

## §2. The campaign chain (this is what to review)

1. **Founder inversion (1864).** Rather than guess the screening mechanism, the campaign calibrated the Sea's residual-response amplitude η ≡ r_c/R_s from the coring requirement, then confronted every other pillar ("calibrate-then-confront"; founder mandate: judgment at each juncture, loop back on counterfactuals, data trumps theory).

2. **The empirical dwarf pin (1865, J3′).** The published dwarf-scale SIDM landscape is a broad band, not the corpus's [1, 2] cm²/g: rotation-curve fits prefer ~2–3 (Kaplinghat–Tulin–Yu 2016, PRL 116 041302; Ren et al. 2019, PRX 9 031020); core-formation viability at V_max ≈ 40 km/s spans 0.5–50 with the largest cores at 5–10 (Elbert et al. 2015, MNRAS 453 29); MW dSphs at lower v want 20–100 (Correa 2021; Roberts et al. 2024). High-v bounds: groups 0.5 ± 0.2 at ~1150 km/s (Sagunski et al. 2021); clusters < 0.35 (Sagunski 95%), < 0.19 (Eckert/X-COP 2022), **< 0.13 (Andrade et al. 2022, tightest)**. Adopted: **σ/m(50 km/s) ∈ [1, 5] central, [0.5, 10] extended.** The band-drawing across heterogeneous analyses is a tagged judgment — you may re-draw it; sources are pinned in `code/1865`.

3. **χ revives (1865).** η = χ = φ⁻³/6 (R_s = r_c/χ = 25.42 fm) delivers σ_dwarf(50) = 3.6–4.9 cm²/g at N = 15–20 — inside the pinned window. Equivalently: **the screened residual carries a gap m_s = ħc/R_s = χ·(ħc/r_c) = 7.764 MeV — the gap, in rung units, IS the Capotauro constant.**

4. **CONFRONT-1 refined; the np channel selects N (1866).** The heavy-nucleus binding shift ΔB was recomputed with the proper double density integral (uniform sphere and Woods–Saxon agree to 2%; the λ→∞ Coulomb limit reproduces the analytic uniform-sphere result to 5 decimals): the earlier pairs×⟨V⟩ estimate was ×1.6–1.8 high. The smooth ΔB(A) along the valley of stability is then absorbed by the SEMF basis to a residual ~2×10⁻⁵ of raw, with coefficient shifts far inside independent determinations — **the mass-fit channel is voided**. The binding constraint migrates to the *unabsorbable* two-body np scattering length (a_t = 5.4194(20) fm): at η = χ it **excludes N = 12 (δa_np = 3.7–4.6×10⁻³ fm), is marginal at N = 15 (2.9×10⁻³), and clears N = 18–20 (1.6–2.2×10⁻³)**. Nuclear physics selects the corner independently of the halo data it then fits. (Conditional on pairwise-additive qCP coupling — tagged J4.)

5. **The floor correction chain (1867→1871) — read this as a unit; it is the process-critical part.**
   - **1867:** composing the v1.1 capture-only cluster numbers with the elastic floor *under the v1.1 convention* exposed a cluster-ladder violation ×1.4–5.1. The v1.1 "cluster ~0.003, robust" statement was the capture term alone. Caught in-house; panel held.
   - **1868:** audit of the hard-capsule idealization: a rod's elastic size is the coat's effective interaction radius b_eff(v) solving V_coat(b) = KE. Self-consistency: the convention's implied radius (9.46 fm) matches b_eff(50 km/s) = 9.21 fm to 3% — the convention IS the coat-fattened side-projection at dwarf velocities.
   - **1869:** exact classical deflection-integral shape S(v) → claimed the ladder passes ×3.5. **RETRACTED at 1870:** the central-potential reduction is a lower bound on transport (misses multi-segment contact accumulation and the torque channel).
   - **1870:** soft-potential rigid-body MC (correct physics, still-wrong geometry) → marginal tension, normalization-limited.
   - **1871:** the registry pin closes it. The element pitch was never free: **d = the corpus rung spacing 1.0–1.3 fm (reasoning 1812/0835)** — so L(N=18) ≈ 20 fm, not the ~80 fm the 1868 inference implied. At physical geometry the MC **measures** the floor directly: **σ_T/m = 0.09–0.15 (50 km/s) → 0.06 (200) → 0.03–0.05 (1150) → 0.027–0.044 (1500) → 0.02 (3500) cm²/g.** The ε·0.11·N convention is thereby superseded (×4–6 over true transport). MC bands carried: tumbling ×~1.4, dt ×~1.2, cold/rigid/classical caveats tagged J10′.

6. **The full curve at η = χ, N = 18 (capture + measured floor):** dwarf pin 4.4–4.9 **PASS** [1,5]; LSB 0.74–0.85 **PASS** [0.7,2.5]; **cluster 0.03–0.05 — the entire ladder passes incl. Andrade < 0.13, ×2.7–4.5 margin, by measurement**; Bullet ~0.02 **PASS**; group 0.037–0.05 — **2.3σ below** Sagunski's mild 0.5 ± 0.2; dSph regime (10–40 km/s) grazes ~20–25% under the heterogeneous 20–100 window. The group undershoot survived every floor treatment (2.2σ at 1869, 1.3–1.9σ at 1870, 2.3σ at 1871) — a robust prediction, not an approximation artifact.

7. **CONFRONT-2 (1872):** no conflict with the CC correlation-length route (ρ_Λ ~ 1/ξ², ξ → event horizon): the DM screening is a **gapped** color-residual response channel (7.76 MeV) while the CC coherence rides the **gapless** |SSV| scalar (the 1107–1108 icosahedral 5-design result); e^(−m_s r) cannot leak to cosmological r; rods are localized excesses on baryon footing (D-FRAG clean).

8. **Formation-lane scoping (1873):** with every input pinned and zero tuning, the reversible-aggregation equilibrium inversion for ⟨N⟩ = 15–20 gives kT_form = 16.2–16.6 keV — inside the 0860 hook (≤ 19 keV) and log-robust — but rate/H ~ 10⁵ there, so the N-cap must be kinetic/collisional. **Coincidence registered, not claimed.**

9. **Falsifiers (v1.2).** **F1 (sharpest, near-term):** group-scale σ/m ≈ 0.03–0.05 at ~1150 km/s — an order below the current mild detection; 0.5 confirmed at high significance kills the model; relaxation to ≲ 0.1 confirms against the alternative. **F2:** improved a_t precision squeezes N ≳ 15 from below. **F3 (promotion gate):** the de-novo derivation must yield m_s = χ·(ħc/r_c); any other value displaces χ and returns the magnitude to calibration status. **F4:** the formation cap must land ⟨N⟩ = 15–20 without spoiling the 16.5 keV window.

## §3. The asks (per claim: RATIFY / RATIFY-WITH-CHANGES / RESTATE / REFUTE)

- **A.** The J3′ empirical pin ([1,5] central at 50 km/s) is a defensible reading of the cited literature.
- **B.** η = χ at N ≈ 15–20 is correctly characterized as a *zero-parameter candidate surviving the confrontation suite* — neither over-claimed as derived nor under-claimed as a fit.
- **C.** The 1866 ΔB/absorption argument and the migration of CONFRONT-1 to the np channel are sound.
- **D.** The supersession of the ε·0.11·N convention by the measured floor (J8 registry pin + soft MC) is justified, and the v1.2 anchor-table verdicts follow from the quoted numbers.
- **E.** The correction chain (1867→1871), including the 1869 retraction, is adequately disclosed in the paper notice — the process standard you set at v1.1 is met.
- **F.** The falsifier set F1–F4 is live, pre-registered, and honestly stated (including the group 2.3σ undershoot and the dSph grazing as recorded weaknesses).

## §4. Verification pointers (all stdlib/numpy; run from repo root)

- `code/1865_empirical_dwarf_pin_recalibration.py` — pin, recalibration, χ check, cluster-bound scan.
- `code/1866_db_density_integral.py` — density integral, Coulomb sanity, SEMF absorption, per-channel verdicts.
- `code/1867_sigma_v_shape_test.py` — the composition that exposed the v1.1 gap.
- `code/1868_coat_radius_floor.py`, `code/1869_coat_channel_deflection_integral.py` — the audited/retracted intermediate steps (retained for the trail).
- `code/1870_soft_rod_mc.py`, `code/1871_soft_rod_mc_pinned_geometry.py` (+ `1871_results.json`) — the measured floor; worker-mode per velocity; seeds/dt/tumbling bands in-file.
- `code/1872_confront2_cc_xi_channel.py`, `code/1873_formation_lane_scoping.py` — consistency and scoping.

## §5. Weaknesses we invite you to attack

(i) The J3′ band-drawing maps heterogeneous analyses (different velocity scales, viability vs preference) to one number at 50 km/s. (ii) The MC is classical, rigid-element, cold-rod baseline (tumbling as a ×1.4 band), R_samp-truncated, with dt sensitivity ×~1.2 — the ×2.7–4.5 cluster margin must survive these bands (it does on the quoted spans, but check). (iii) The group 2.3σ undershoot of a positive (if mild) measurement. (iv) The dSph-regime grazing. (v) The formation cap mechanism is open — the 16.5 keV result is scoping only. (vi) The de-novo gap is underived — χ's status rests on survival, not derivation. (vii) The paper's `\smm` macro renders σ_V/m while the v1.1/v1.2 observable is σ_T/m — a notation wrinkle to adjudicate. (viii) Two consecutive versions required in-house corrections of load-bearing numbers; judge whether CONV-003 provenance tagging as now practiced is a sufficient control.
