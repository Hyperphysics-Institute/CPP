# SI-1 — Substrate Inversion Arc, Task 1: the unknown ledger, the target ledger, and the forward-map system (CONV-004 execution)

**Status:** foundation document (Patch 1887, 6 July 2026). Charter: founder ruling of 6 July
(`founders_voice/founder_ruling_measured_coefficients_2026-07-06.md`; CONV-004). Every number below carries
its CONV-004 tag; every modeling choice is J-tagged. Verify: `code/1887_si1_forward_maps_counting.py`.

## 1. Target ledger M (what the data have fixed)

| # | Quantity | Value | Tag | Source |
|---|---|---|---|---|
| M1 | m_s — colour-residual channel gap | χ·ħc/r_c = 7.764 MeV (R_s = 25.42 fm) | **MEASURED** | halo ladder, 1863–1877 |
| M2 | S_c — colour-singlet coupling suppression | [0.005, 0.05], center R_N/R_s = 0.035 | **MEASURED** | XQC/LZ/shielding ladder, 1879–1881 |
| M3 | E_ee — eDP side-bond energy | 0.9 MeV | PINNED (corpus, 1813) | |
| M4 | E_c — rod–rod unipolar residual at contact | ≈ 0.3 MeV (flat) / 0.02N (additive) | PINNED (corpus, 1858-era anchors) | |
| M5 | d ≡ a — rung spacing / lattice pitch | 1.0–1.3 fm | PINNED (0835/1812) | |
| M6 | E_hDP — qDP bond scale | ≈ 150 MeV (λ = ħc/E_hDP ≈ 1.3 fm) | PINNED (0835) | |
| M7 | m_el — element mass | 1408 MeV | PINNED (08xx band) | |
| M8 | kT_form — formation-window temperature | 16.2–16.6 keV | **MEASURED-scoping** (1873; cap mechanism open) | |
| M9 | m_const — cage constituent scale | ħc/r_ZBW = 312.7 MeV (r_ZBW = 0.631 fm) | DERIVED (SS-2) | |

r_c = 1 fm is used interchangeably with a throughout the DM corpus [J-SI-1: r_c ≡ a adopted; the η = χ
measurement then reads "the gap in PITCH units is the Capotauro constant"].

## 2. Unknown ledger U (the founder's named depths, in registered language)

| # | Symbol | Meaning (glossary-grounded) | Prior range scanned |
|---|---|---|---|
| U0q | α_q | CP-scale colour-channel coupling strength (dimensionless, fine-structure-like) | 10⁻⁴ – 10 |
| U0e | α_e | CP-scale e-channel coupling strength | 10⁻⁴ – 10 |
| U1 | n | DP Sea number density (fm⁻³); occupancy f_occ = n·a³ | 10⁻³ – 10 fm⁻³ |
| U2 | E_z | ZBW energy scale of a quiescent Sea DP (ħω_z; glossary: CP oscillation between DP partners) | 1 keV – 1 GeV |
| U3 | C_r | residual (non-cancelled) fraction of the colour channel in the quiescent Sea — the founder's "cancellation" | 10⁻⁶ – 1 |
| U4 | S_p | superposition factor for collective Sea response (√N-random ↔ N-coherent, expressed as multiplicative factor) | 10⁻² – 1 |
| U5 | D_st | static fraction of a confined colour-singlet's leading residual moment | 10⁻³ – 1 |
| U6 | T_amb | ambient Sea excitation temperature | 0.1 – 10³ keV |
| U7 | D_occ | Sea occupancy diffusivity at the R_s scale (c·fm); forward map = PRW-D (Patch 2327): survive iff D ∈ [5.2×10⁻³, 3.7×10⁻²] c·fm, KILL-on-suite outside; joint with U6/U2 via v = √(2T_amb/m_DP) once m_DP pinned; cosmological history D(z) additionally constrained by OPEN-DM-AGG-1 (Patch 2328: early knee ≳ 0.6 MeV-class required — the survive branch needs D early-high, late-in-window). **DERIVED as a law at Patch 2330 (no-carried-velocity ruling):** knee_tot(T_amb) = ħ[D_hop k² + Γ_loc], D_hop = (a²κ_νE_z/6ħ)e^(−κ_aE_ee/T_amb) (ballistic-capped), Γ_loc = κ_cκ_ν(E_z/ħ)e^(−E_gap/T_amb); monotone in T_amb; window invariant form = knee_tot ∈ [1.60, 11.3] keV; the accepted corner rides Γ_loc (see X4′, §4); Planck floor l_P·c/6 for the coherent channel (harmonic-null theorem) | static (0) – ballistic cap cℓ_cp/3 ≈ 1.06 c·fm |

## 3. Forward-map system F: U → M (registered structure only; κ's are O(1) geometric constants of the
600-cell, scanned in [1/3, 3] — J-SI-2)

- **F1 (screening/gap):** Debye-form response of a polarizable medium to a colour-residual source
  [J-SI-3: Debye form adopted; plasmon form differs by O(1) absorbed in κ₁]:
  **m_s² = κ₁ · 4π α_q (ħc)³ · n C_r S_p / E_z.**
- **F2 (e-channel bond):** contact bond at pitch: **E_ee = κ₂ · α_e ħc / a.**
- **F3 (q-channel bond):** **E_hDP = κ₃ · α_q ħc / a.** (F2/F3 ⇒ α_e/α_q = (κ₃/κ₂)·E_ee/E_hDP ≈ 6×10⁻³·O(1)
  — a substrate inference independent of a.)
- **F4 (rod residual):** the unipolar residual exists because cancellation is imperfect and the cage is
  coherent: **E_c = κ₄ · C_r · 8 · α_q ħc / a** [J-SI-4: linear in C_r; cage coherence factor 8 (one per
  core qCP) folded; alternative coherence powers absorbed in κ₄ span].
- **F5 (singlet suppression):** **S_c = κ₅ · D_st · (R_N/R_s).** The MEASURED S_c ≈ R_N/R_s therefore
  reads: **D_st ≈ 1/κ₅ = O(1) — the data dictate that a confined singlet presents an essentially fully
  STATIC leading moment to the Sea channel** (not a fluctuating/van-der-Waals one). First substrate
  inference of the arc, available before any scan.
- **F6 (constituent/element):** **m_el = κ₆ · 8 · m_const · b₈**, b₈ ≈ 0.563 the cage binding fraction
  implied by 1408/(8·312.7) [J-SI-5: LOW-CONFIDENCE MAP — bookkeeping identity until the SS-band binding
  chain is imported; carried for counting, not constraint].
- **F7 (formation window):** **T_amb = kT_form** if aggregation freezes at ambient [CONJECTURED — the 1873
  cap mechanism is open; carried as a soft target].

## 4. Elimination and counting (the CONV-004 ledger)

Unknowns: 8 (U0q, U0e, U1–U6). Hard targets: M1–M6 = 6 (M7 via F6 is soft; M8 via F7 is soft; M9 feeds F6).
κ-freedom: [1/3, 3] per map (J-SI-2). **The hard system is 6 equations / 8 unknowns at O(1) resolution:
UNDER-determined by 2 — honestly stated.** What the data pin are COMBINATIONS:
- **X1 ≡ α_q n C_r S_p / E_z = m_s² / (4π κ₁ (ħc)³)** — the Sea's colour-channel response density.
- **X2 ≡ α_q / a = E_hDP / (κ₃ ħc)** and **α_e/α_q ≈ 6×10⁻³** — the channel-strength ladder.
- **X3 ≡ C_r = E_c a / (8 κ₄ α_q ħc) = (κ₃/8κ₄)·E_c/E_hDP ≈ 2.5×10⁻⁴·O(1)** — **the cancellation is
  measured: the quiescent Sea cancels the colour channel to a few parts in 10⁴.** Second substrate inference
  available before scanning (F3+F4 combine; a and α_q drop out).
- **D_st ≈ O(1)** (F5, above).
- **X4 ≡ κ_ν E_z e^(−κ_aE_ee/T_amb) ∈ [6.2, 43.7] MeV** and **X4′ ≡ κ_cκ_ν E_z e^(−E_gap/T_amb) ∈
  [1.60, 11.3] keV** — the Patch-2330 PRW inversions (transport- and local-channel forms of the same
  knee window; the existence scan puts 99.8% of the accepted corner on X4′, with T_amb marginal
  82–872 keV, ×5–53 above the F7 soft target — named tension). Conditional on the G4 survive branch;
  subject to OPEN-DM-TAMB-1, SHARPENED at Patch 2331 to the uncertainty floor: any activated
  realization of a window knee carries ρ ≥ knee_tot/R_s³ = ×2×10³⁴⁺ over closure (event energy
  cancels; T⁴ bound was the weaker face; evasion (a) two-temperature Sea CLOSED-insufficient) —
  survival is BINARY on TAMB-1(b), the one-ledger status of dynamical Sea excitation (G-sector
  derivation, Gate-1's own apparatus); if (b) holds, all closure faces evaporate including F7's
  ×6.5×10²⁶. **RESOLVED at Patch 2333: TAMB-1(b) FAILS — dynamical Sea excitation SOURCES**
  (DERIVED-conditional on the corner's own stack: one zeroing mechanism reaching exactly the
  gradient-free component; harmonic-null forces localized knee-carriers; Case-3 provenance-blindness
  + C-d form-blindness exclude the discriminant; Case-4/Λ a-fortiori anchor). **X4/X4′ are DEAD as
  survive-branch quantities** — OPEN-DM-TAMB-1 adjudicated-operative; the closure surface binds the
  whole keV-class U6 prior; G4 → KILL-on-suite-conditional per pre-registered outcome (ii).
Substituting X3 into X1 pins **n S_p / E_z** — the density-coherence-per-restoring combination. The two
residual flat directions are (n vs S_p vs E_z internal split) and (T_amb) — exactly where new targets from
other sectors (or the F7 cap mechanism) will bite. **Overdetermination margin at task-1 resolution: 0 on the
hard system; the arc's growth path is importing more pinned corpus numbers as targets, not adding unknowns.**

## 5. Task-2 plan

Monte-Carlo existence scan over U (log-priors above, κ ∈ [1/3, 3]): accept a sample iff ALL hard targets are
reproduced within the κ bands. Deliverables: existence verdict (non-empty/empty), the accepted region's
marginal ranges (the "what the data reveal about the DP Sea" table), the pinned-combination values with
uncertainties, and the no-refit forward predictions (F5/F6-falsifier channels, DAMIC edge, group point) from
the accepted region. Kill-condition stands: an empty region is a structural falsification of the candidate.

## OPEN-DM-DSPH-1 (registered Patch 2339) — the inverse arc
The Gate-1/B1 kill treated as specification: SPEC-1 (charter §2) states the measured
requirements on the physics the dSph anchors demand and the registered structure has
not yet supplied. Founder working hypothesis (correct candidate, missing mechanism)
carried under RENT + EXIT discipline; Clause 1 falsification condition PROPOSED,
awaiting founder-attested text — arc verdicts frozen until ratified. Lanes L1–L4 per
charter §3; forward map: any lane producing a derived, rent-paying SPEC-1 mechanism

**FRAME-ADOPTION GATE LEDGER (from Patch 2346/F3; updated at 2349):**
- **G1 (formation rent):** PASSED-with-texture (2349). 1855 kinetics realize suite-passing populations at both audited frames; extended deep/unstrained (natural α=1, p_min=0), central shallow/strained (α≈3–6, p≥13). Dimer-dominance reachable (α_99≈989) but not required. v1 kill strengthened (×1.189). Inverse targets registered: α_pass(central), p_min(central)=13, S(N) derivation under OPEN-SS-43.
- **G2 (satellite survival):** PASSED-with-texture (2350). Evaporation clears ×6+; population in the Concerto-simulated viable collapse branch; 1856 ε(N) measured (0.17–0.32, kinder to long rods than feared); transport bracket: extended BRACKET-STABLE joint pass, central envelope-split by 0.32% (inside proxy systematics). Forward maps: SASHIMI-class abundance modeling; derived rod-source residual correction (OPEN-SS-43 geometry).
- **G3 (per-dSph likelihood):** OWED — Correa-class, pericentre priors; the rigorous version of the 2345 synthesis.
All three clear → F3 v2-adoption auto-proposal to founder. Clause 1 re-draft still pending founder text.
routes back through the anchor suite under Gate-1/B1 grading.
