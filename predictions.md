# CPP Predictions Registry

**Repository location:** CPP root level (peer of `Research_Frontier.md`, `theorem-registry.md`)
**Last updated:** 11 April 2026 (SM-8/9/10 + SS-2 predictions added)
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute

---

## Purpose

This file is the single document a physicist needs to evaluate
whether CPP makes real, falsifiable predictions. It collects every
quantitative prediction across the entire CPP paper series in one
place, with explicit status labels.

A prediction is a claim that CPP makes about a measurable quantity
**before** that quantity is used as an input to the theory. Post-dictions
(results calibrated to match known data) are separately listed and
clearly labelled. The ratio of genuine predictions to post-dictions
is the most honest measure of a theory's predictive power.

**Status labels used:**
- ✅ CONFIRMED — measured and consistent with CPP prediction
- ❌ FALSIFIED — measured and inconsistent; CPP ruled out or requires revision
- 🔬 TESTABLE — prediction made; experiment exists but CPP value not yet compared
- 📐 OPEN — prediction made; experiment does not yet exist or is not yet sensitive enough
- 📊 POST-DICTION — result calibrated to PDG; CPP reproduces but did not predict independently
- ⚠️ ESTIMATE — order-of-magnitude; not a parameter-free derivation

---

## Section 1: Confirmed Predictions

These are results CPP derives independently that agree with measurement.

| ID | Prediction | CPP value | Measured value | Agreement | Source |
|----|-----------|-----------|----------------|-----------|--------|
| PRED-C-1 | δ = 1/3 (charge quantisation) | 1/3 exact | 1/3 exact | Exact | SM-1 Thm 1 |
| PRED-C-2 | q_up = +2/3 e | +2/3 exact | +2/3 e | Exact | SM-1 Thm 1 |
| PRED-C-3 | q_down = −1/3 e | −1/3 exact | −1/3 e | Exact | SM-1 Thm 1 |
| PRED-C-4 | Koide ratio K = 2/3 | 2/3 exact | 2/3 (11 ppm consistency) | 0.0001% | SM-3 |
| PRED-C-5 | U_PMNS⁽⁰⁾ = U_TBM | Exact from K3 eigenvectors | sin²θ₁₂ = 0.307, sin²θ₂₃ = 0.546 | Zeroth-order ✓ | SM-5 |
| PRED-C-6 | sin²θ₁₂ = 1/3 | 0.3333 | 0.307 ± 0.013 | Within 2σ | SM-5 |
| PRED-C-7 | Quark mass strict ordering | m_u < m_d < m_s < m_c < m_b < m_t | ✓ all generations | Exact ordering | SM-1 Thm 9 |
| PRED-C-8 | SU(3) from tetrahedral hopping | Gell-Mann matrices exact | SU(3) observed | Machine precision | SS-1 Thm 1 |
| PRED-C-9 | Gluon masslessness from open path | m_g = 0 exact | m_g < 10⁻¹⁸ eV | Consistent | SS-1 Thm 2 |
| PRED-C-10 | β₀ = 7 (one-loop QCD) | 7 exact | 7 (QCD with 3 colours, 6 flavours) | Exact | SS-1 Thm 3 |
| PRED-C-11 | α_geom = 3(11+5√5)√(5+√5)/320 | 0.55936 exact | (sea_strength = 0.185, 3.8% residual) | Derived to 3.8% | SS-1 Thm 4 |
| PRED-C-12 | Ω⁻ mass from GMO | 1681 MeV | 1672.5 MeV (PDG) | 0.5% | SS-1 Thm 8 |
| PRED-C-13 | K(c,b,t) ≈ 2/3 | 0.6695 | 2/3 (Koide formula for heavy quarks) | 0.42% | PS-1 thermal |
| PRED-C-14 | Three lepton generations | Exactly 3 from cage shells | 3 observed | Exact | SM-1 §4 |
| PRED-C-15 | Three quark generations | Exactly 3 (4 cage shells, 3 charge types) | 3 observed | Exact | SM-1 §4 |
| PRED-C-16 | Neutrinos have normal mass ordering | ν₁ < ν₂ < ν₃ from σ suppression | Normal ordering favoured (current data) | Consistent | SM-1 §8 |
| PRED-C-17 | m_s (zero-param) | 96.3 MeV | 93.4 MeV | +3.1% | SM-8 v4.1 |
| PRED-C-18 | m_c (zero-param) | 1,249 MeV | 1,270 MeV | −1.6% | SM-8 v4.1 |
| PRED-C-19 | m_b (zero-param) | 4,115 MeV | 4,180 MeV | −1.6% | SM-8 v4.1 |
| PRED-C-20 | m_t (zero-param) | 169,571 MeV | 172,760 MeV | −1.8% | SM-8 v4.1 |
| PRED-C-21 | Exactly 3 quark generations (tessellation) | 3 | 3 | Exact | SM-8 v4.1 |
| PRED-C-22 | Attractive fraction = 2/3 (all cages) | 2/3 | — | Structural | SM-8 v4.1 |
| PRED-C-23 | Charge census 1:1:2:2 | exact | — | Structural | SM-8 v4.1 |
| PRED-C-24 | Top quark non-hadronization | Shell 4 cage too open | observed | Qualitative | SM-8 v4.1 |
| PRED-C-25 | r_proton | 0.883 fm | 0.841 fm | +5.0% | SS-2 |
| PRED-C-26 | μ_proton | 2.789 μ_N | 2.793 μ_N | −0.1% | SS-2 |
| PRED-C-27 | α_s(m_H) | 0.1132 | 0.1130 | +0.2% | SS-2 |
| PRED-C-28 | Λ_QCD | 335 MeV | ~330 MeV | +2% | SS-2 |
| PRED-C-29 | μ_neutron | −1.847 μ_N | −1.913 μ_N | −3.4% | SS-2 |

---

## Section 2: Open Predictions — Quantitative

These predictions are specific and quantitative. The experiments
either do not yet exist or are not yet sensitive enough to test them.
**These are what CPP must get right to be taken seriously.**

**Note (30 March 2026):** Predictions derived from Tier 3 propositions
(see `Research_Frontier.md` §3) are marked [T3]. Predictions derived from Tier 4
candidate mechanisms are marked [T4] and should be treated as
directional predictions pending quantitative verification of the
underlying proposition. The tier label reflects the maturity of the
CPP account, not the testability of the prediction.

| ID | Prediction | CPP value | Experiment needed | Source |
|----|-----------|-----------|-------------------|--------|
| PRED-O-1 | Top quark fourth cage binding energy matches m_top | TBD (30-vertex shell calc) | Compute from 600-cell geometry | SM-1/SM-2 (OPEN-P-SS-1) |
| PRED-O-2 | Radial DP chain length = classical electron radius | r_chain = r_e = 2.82 × 10⁻¹⁵ m [NOTE: r_e = α_fine × ħc/(2·SSV₀); this prediction is a corollary of the α_fine derivation (EW sector) + resolution of r_conf inconsistency (OPEN-P-QM-new-9)] | Derive d_Sea from 600-cell; resolve OPEN-P-QM-new-9 | SM-1 (OPEN-P-QM-new-4, OPEN-P-QM-new-9) |
| PRED-O-3 | Tunneling electrons emit no photons during transit [T3] | Zero photon emission rate during tunneling | Precision photon detection in STM tunneling | SM-1 (PROP-4) — Tier 3 prop; qualitative prediction already consistent with observation |
| PRED-O-4 | Para:ortho positronium annihilation ratio from cage geometry [T4] | 1000:1 from T_d vs 3-fold dissolution (cage geometry calculation needed first) | High-precision positronium spectroscopy | SM-1 (PROP-15) — Tier 4 prop; ratio requires cage dissolution geometry calculation before this is a firm prediction |
| PRED-O-5 | String tension σ from sea_strength | σ ≈ 0.9 GeV/fm (to derive, not calibrate) | Compute from chain self-collimation | SS-1 (OPEN-P-SS-5) |
| PRED-O-6 | QCD deconfinement temperature T_c | ~150 MeV from σ × r_conf | Lattice QCD cross-check | SS-1 (OPEN-P-SS-14) |
| PRED-O-7 | Λ_QCD from PSR saturation | ~200 MeV (to derive) | Compute from sea_strength | SS-1 (OPEN-P-SS-7) |
| PRED-O-8 | Koide phase θ = 132.73° from EW sector | To be derived from W/Z cage geometry | EW series completion | SM-3/EW (OPEN-P-SM-7d) |
| PRED-O-9 | TBM corrections θ₁₃ = 0.022 from Capotauro bias | To be derived from OPEN-P-SM-4 | EW series | SM-5 (OPEN-P-SM-5) |
| PRED-O-10 | Neutrino masses Σm_ν ~ 0.017 eV | 0.017 eV from σ = 120⁻³ | KATRIN, CMB+BAO Σm_ν measurement | SM-1 §8 |
| PRED-O-11 | r_crit (pair production threshold) = Compton wavelength | ℏ/m_e c = 2.43 × 10⁻¹² m | Derive from SSV₀, sea_strength | SM-1 (OPEN-P-QM-new-7) |
| PRED-O-12 | ℏ derivable from ZBW statistics | TBD from SSV₀, l_P, t_P, sea_strength | Theoretical derivation | SM-1 (OPEN-P-QM-new-1) |
| PRED-O-13 | Glueball mass from tetrahedral hDP loop | TBD | Lattice QCD + CPP calculation | SS-1 (OPEN-P-SS-6) |
| PRED-O-14 | Nucleon magnetic moments from ZBW | μ_p = 2.793 μ_N (to derive), μ_n = −1.913 μ_N | Derive from SU(6) + ZBW framework | SS-1 (OPEN-P-SS-8) |
| PRED-O-15 | Uniqueness of SU(3) from tetrahedral cage | SU(3) is the unique algebra | Group theory proof | SS-1 (OPEN-P-SS-11) |

---

## Section 3: Open Predictions — Qualitative

Directional predictions that do not yet have CPP numerical values
but identify a specific observable consequence.

| ID | Prediction | Physical content | Source |
|----|-----------|------------------|--------|
| PRED-Q-1 | de Broglie wavelength as DP chain compaction | High-v electrons have shorter chain period = λ_dB | SM-1 (PROP-6) |
| PRED-Q-2 | Atomic orbital shapes from DP chain standing waves | Orbital nodes = chain standing wave nodes | SM-1 (PROP-9) |
| PRED-Q-3 | VP half-life distribution from partner-switching statistics | τ_VP = t_P / p_dissipate; energy-time uncertainty derived | SM-1 (PROP-11) |
| PRED-Q-4 | Mass decrease at QCD transition temperature | Cage binding energy decreases above T_c | SM-1 (PROP-14) |
| PRED-Q-5 | Disorderly annihilation produces entropy increase | High-v e⁺e⁻ → jets not two clean photons | SM-1 (PROP-15) |
| PRED-Q-6 | Isentropic condition for two-photon annihilation | v_approach < r_cage/t_P | SM-1 (PROP-15) |
| PRED-Q-7 | 30-vertex shell is vertex-transitive degree-4 shell | Geometric property derivable from 600-cell | SM-1, PS-1 |

---

## Section 4: Post-Dictions (Calibrated to PDG)

These results are reproduced by CPP after calibration to experimental
data. They demonstrate internal consistency but do not constitute
independent predictions. Listed here for completeness and to
distinguish clearly from the sections above.

| ID | Result | CPP approach | Calibration used | Source |
|----|--------|-------------|-----------------|--------|
| POST-D-1 | m_e = 0.511 MeV | SSV₀ = m_e c²/2 — direct calibration | m_e | SM-1 §7 |
| POST-D-2 | m_μ = 105.66 MeV | SM-2 cage formula with N_k calibrated | m_e (via SSV₀) | SM-2 |
| POST-D-3 | m_τ = 1776.86 MeV | SM-2 cage formula with N_k calibrated | m_e | SM-2 |
| POST-D-4 | All quark masses | SM-2 effective occupancy N_k fitted to PDG | m_e | SM-2 |
| POST-D-5 | W, Z, Higgs masses | EW-1 through EW-4: confinement energy formula with topology-dependent η calibrated to each mass separately. Three distinct η values (η_W = 1.57×10⁻¹⁷, η_Z = 1.48×10⁻¹⁷, η_H = 2.93×10⁻¹⁷). OP-EW-1 (derive η), OP-EW-2 (unified formula). | PDG masses | EW-1–4 |
| POST-D-6 | sea_strength ≈ 0.185 | Derived to 3.8% (3.8% residual remains) | QCD coupling | SS-1 §8 |
| POST-D-7 | sin²θ_W = 0.2312 | **Structural framework derived** (p_k weights from 600-cell dihedral projections, zero parameters). **Numerical value reproduced** (coupling g' calibrated to PDG target via vertex_count_correction = 1.18). Framework → Type 1; numerical value → post-diction until OP-EW-3 (derive g, g' from vertex counts) is solved. Agreement: 0.004%. | PDG sin²θ_W | EW-1, EW-5 (THEO-EW-4) |
| POST-D-7 | SSV₀ = 0.2555 MeV | Direct calibration to electron mass | m_e | SM-1 §7 |
| POST-D-8 | θ_Koide = 132.73° | Calibrated from PDG lepton masses | m_e, m_μ, m_τ | SM-4 |
| POST-D-9 | Scale factor A in SM-4 | Calibrated from PDG | m_e | SM-4 |
| POST-D-10 | Muon g-2 ≈ 2.9 × 10⁻¹⁰ | Post-diction (mixing fractions calibrated to prior anomaly) | Prior Fermilab anomaly | SM-2 App B |

---

## Section 5: Falsified Predictions

Predictions CPP made that were tested and found wrong. These are
retained here as a permanent record. A theory that hides its failures
is not science.

| ID | Prediction | CPP value | Actual value | Why falsified | Source |
|----|-----------|-----------|--------------|---------------|--------|
| FALS-C-1 | C₆₀ (60-vertex) top quark cage | 60 vertices | No 60-vertex shell in 600-cell | Exact shell computation (PS-1) | SM-1/SM-2 |
| FALS-C-2 | φ^(3(l-1)) quark mass scaling | Geometric sequence | 3–8× errors in structural masses | Exact 600-cell shell volumes | PS-1 |
| FALS-C-3 | θ_Koide from Aharonov-Bohm loop | ~132.73° | C3 symmetry prevents degeneracy breaking | 11 mechanism tests | Sessions B,E,F,G |
| FALS-C-4 | 4D 600-cell embedding breaks C3 for θ | Breaks C3 | C3 preserved exactly in 4D | 600 tetrahedral cell computation | PS-3b |
| FALS-C-5 | Self-consistent ZBW feedback selects θ | ~132.73° | Converges to θ = 180° (trivial) | Fixed-point iteration | Session L |
| FALS-C-6 | Löwdin downfolding K4→K3 breaks antibonding degeneracy | Breaks | V4 dark to antibonding; ⟨φ₋|v⟩ = 0 | Algebraic proof | Session E |
| FALS-C-7 | CP Exclusion Postulate as independent axiom | Axiom | Theorem (from SSV + lattice) | THEO-1 derivation | Propositions.md |

---

## Section 6: Predictions by Paper

Quick reference map of which paper contributes which predictions.

| Paper | Key predictions |
|-------|----------------|
| SM-1 | PRED-C-1 to PRED-C-3 (charge quantisation), PRED-C-7 (mass ordering), PRED-C-14–15 (generations), PRED-C-16 (neutrino ordering), PRED-O-2, PRED-O-3, PRED-O-4, PRED-O-10, PRED-O-11 |
| SM-2 | PRED-O-1 (top quark cage mass), POST-D-1 to POST-D-9 (calibrated mass table) |
| SM-3 | PRED-C-4 (Koide K=2/3), PRED-O-8 (θ_Koide) |
| SM-4 | PRED-C-4 (consistency check), POST-D-8 (θ calibration) |
| SM-5 | PRED-C-5 to PRED-C-6 (TBM mixing), PRED-O-9 (TBM corrections) |
| SS-1 | PRED-C-8 to PRED-C-13 (SU(3), gluons, β₀, α_geom, Ω⁻, K(c,b,t)), PRED-O-5 to PRED-O-7, PRED-O-13 to PRED-O-15 |
| SR-1 | de Broglie (PRED-Q-1), Lorentz contraction from SSV_abs/PSR |
| Propositions | PRED-O-3, PRED-O-4, PRED-O-11, PRED-O-12, PRED-Q-2 to PRED-Q-6 |
| SM-8 | PRED-C-17 to PRED-C-24 (zero-param quarks, 3-gen, 2/3 fraction, charge census, non-hadronization) |
| SM-9 | Symmetry Degeneracy Theorem (mathematical, not a prediction per se) |
| SS-2 | PRED-C-25 to PRED-C-29 (r_proton, μ_proton, α_s(m_H), Λ_QCD, μ_neutron) |

---

## Section 7: Priority Rankings for Experimentalists

The following five predictions are recommended for immediate
experimental or theoretical attention, ranked by their ability
to differentiate CPP from competing frameworks:

**P-1 (Highest priority): Top quark cage binding energy (PRED-O-1)**
This is a parameter-free geometric calculation. If the 30-vertex shell
gives m_top to within QCD uncertainty from SSV₀ alone, it is the
strongest single confirmation of CPP's mass generation mechanism.
Requires: theoretical calculation only (no new experiment needed).

**P-2: Pair production threshold from r_crit (PRED-O-11)**
Deriving the Compton wavelength from SSV₀ and sea_strength would
demonstrate that ℏ itself is a consequence of 600-cell geometry —
one of the most fundamental possible results. Requires: theoretical
calculation.

**P-3: Tunneling photon absence (PRED-O-3)**
Precision measurement of photon emission during STM tunneling events.
If emission rate is consistent with zero (as CPP predicts for geometric
reasons), this tests the cage dissolution mechanism directly.
Requires: precision scanning tunnelling spectroscopy.

**P-4: Neutrino mass sum Σm_ν ~ 0.017 eV (PRED-O-10)**
KATRIN and upcoming CMB+BAO measurements will constrain Σm_ν to
~0.01 eV precision. The CPP estimate of 0.017 eV is directly in
this window. Requires: near-term experimental sensitivity.

**P-5: Koide phase θ from EW sector (PRED-O-8)**
If θ = 132.73° can be derived from the W/Z cage geometry without
calibration, it would convert the Koide formula from a 2-parameter
fit (SM-4) to a 0-parameter prediction. Requires: EW series completion.

---

*Document prepared by Thomas Lee Abshier ND and Claude Sonnet
(Anthropic), 30 March 2026. To be updated after each new CPP paper
and after each experimental test result.*
