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
- **G3 (per-dSph likelihood):** CLEARED-conditional-on-strand (2351). Anticorrelation ordering native to the population; isothermal strand holds per-galaxy; collapse strand (Correa 2021, exact anchors) missed ×1.34+ — traced to a DEMAND-INTERNAL collision (σ_C(50)=28 fails the pin ceiling ×2.8–5.6 for any candidate). L4-b pin-velocity reading now load-bearing (s 17→3.1). ALL THREE GATES TRAVERSED → F3 v2-adoption auto-proposal ASSEMBLED (annex in dsph_frame_adoption_decision.md); trigger FABLE-CERTIFIED/PROVISIONAL adequate at 2352 (frame-asymmetric carve-out named); founder block empty — adoption, Clause 1, DM-1 strand placement await verbatim.
**SLATE RATIFIED (2358, founder-attested 9 July 2026): F3 ADOPTED (dual-frame primary); pin band-reporting [50,72] ADOPTED; Clause 1 population form ATTESTED (arc verdicts unfrozen); release R2 split ADOPTED (DM-2 ≥ 20 July; DM-1/DM-3 on panel pass).**

**FLASH-REVIEW REGISTRATIONS (2355):**
- **L4-b (pin-velocity audit): EXECUTED (2356), outcome (i).** The pin is the 1865 J3′ synthesis window; v_pin=50 is its steepest admissible reading (⟨v⟩-convention band extends to ~72 via the Elbert leg). Collision reading-dependent (dissolves at v_pin ≥ 59.6); **both-strands pass exists at the Elbert-centered reading (extended frame, ×1.000 at v_pin=64; strains α=100/p=12.3 relaxing to near-natural at 70)**; central never passes; v1 kill pin-independent (dSph ×1.58). The pin reading is a demand-side choice on the founder's desk with the frame decision. Completion path: per-source ⟨v⟩ recomputation from published dispersions (KTY/Ren low edge not digitized — steep edge live).
- **Freezing-dynamics debt (D3(b) survivor):** the frozen-mode reading owes the freezing mechanism and the derivation of the measured 0.700 (DeepSeek finding; inverse-coefficient ledger entry stands).
- **0.700 quarantine rule:** empirical, not derived; may not be used as a prior or input in any other CPP sector until independently derived (R3 finding; also stated in DM-2 §5 box).
- **Perturbation-level growth residual:** dynamic Sea response to matter overdensities (μ(k,z), slip η, growth under Case-3) not discharged by the standing-density bookkeeping; forward map housed with the Gate-1/B1 c08 reduction (4 seats; DM-2 §8 carries the named residual).
routes back through the anchor suite under Gate-1/B1 grading.

- **[Patch 2365: STAGE 1 DONE — outcome (i), ≥6-decade window every site class; STAGE 2 (σ_dimer via the P2 machinery at A_dimer + gap treatment + pinned floors) is now the sole gate to F-DM3-4 activation.]** [Patch 2362] Overburden/rate computation PROMOTED to the population lane's required next computation (joint-round J-D BREAK, unanimous-in-substance + top ranked finding): F-DM3-4 (dimer ~2.8 GeV) is a registered CONDITIONAL falsifier until the rate computation demonstrates visibility below the strongly-interacting overburden ceiling; the computation now gates the discriminant's activation in both DM-1 and DM-3. Clause 1 exit (d) unaffected (fires on a null at computed-visible abundance).
- **[Patch 2362] F5 script review-grade reformatting** (R1 finding 3, SCRATCH): queued to next DM-3 code pass; not release-blocking.

- **[Patch 2366] STAGE 2 EXECUTED — CANDIDATE-KILL REGISTERED (pending flash-panel verification + founder adjudication):** the dimer at registered island couplings is (1) overburden-blind to ALL underground classes (sigma_eff 1.8e-29–4.3e-28 cm^2, above every Stage-1 ceiling) and (2) EXCLUDED-class against the 2007 XQC spectrum at ALL twelve pre-registered points (per-bin conservative criterion; violations persist below the island floor to S_c=0.006). IF VERIFIED: the formation-realizable population dies at every audited frame (DM-3's dimer-weighted registration does the wholesale work) — the campaign's second kill; 20-JULY RELEASE AT RISK for DM-1/DM-3 (DM-2 not directly named). B1 criterion mis-specification owned; corrected test = 1879's own per-bin criterion, correction pre-stated. Verification scope: 1879-at-N=2 adaptation, island convention, per-bin criterion, boundary scan.

- **[Patch 2369] SECOND KILL FOUNDER-ATTESTED; ARC PIVOT:** population branch killed at audited frames (XQC-2007, 2366–2368); DM-2 releases alone on the 20th; DM-1/DM-3 pulled, marked killed-not-rewritten, revision deferred behind the new-physics arc. OPEN-DM-DSPH-1 = the lane; successor gate G-XQC-0 pre-registered (cheap-kill-first, binds every future candidate); the formation-kinetics door (OPEN-SS-43 S(N) derivation) is the recommended first pursuit — derive, don't fit, then G-XQC-0.

- **[Patch 2370] S(N) ARC OPENED — cost estimate registered:** the wide door is conditional on an empirical fact checkable cheaply first — can any N≥3 species carry the dSph channel (the 2344 passing regions were dimer 0.94–0.99 + trace N≈5 for LSB)? Plan: Q1 dimer-free rescan (N_min=3, frames fixed per Clause 1) → Q2 G-XQC-0 on survivors → Q3 substrate derivation (weeks-scale, GATED on Q1+Q2; death modes stated: SSV well underivability; equilibrium polymerization populating N=2 anyway; steepness cap). Q3 is NOT entered without a live, gate-cleared target.

- **[Patch 2372] G-XQC-0 PASSED IN CORRIDOR FORM — Q3 UNLOCKED:** the Q1 successor compositions (extended N=(4,5) w=0.217; central N=(3,6) w=0.064) clear the 1879 per-bin gate ONLY at S_c=0.012 (post-DAMIC low island edge) with ρ≤0.3 GeV/cm³; excluded at the ruling point and above, near-threshold-excluded at ρ=0.6. Q3's derivation demand is now double: S(N) suppressing N=2 while populating N=3–6, AND coupling at the low island edge. Survivors carry a computed MINOS-depth/surface visibility window (σ_eff ~1e-30 class) — an F-DM3-4-class falsification channel from day one; the corridor sits on the DAMIC-adjudicable boundary (future DAMIC-floor pin bites directly). Corridor edges (S_c between 0.012–0.035; ρ between 0.3–0.6) are unbracketed grid points — a cheap edge-mapping run is available before Q3 if wanted, not required by the gate.

- **[Patch 2374] Q3 OPENED (founder GO) — demand sheet registered + 2372 criterion CORRECTED (summed spectrum):** corrected corridor: central-repulsive the live corner (ρ*=0.411 exact; 5.7%/14.7% of the island at ρ=0.3/0.2); extended-attractive effectively closed; sign near-decisive. Demands: E_bond/kT_form 23.2–36.2 (closure holds); joint contamination w(2)<0.034, w(1)<0.013 at the live corner (ρ=0.3); suppression beyond isodesmic modest (×1.4–2.1) BUT the N>6 tail (67% of isodesmic mass at ⟨N⟩ₙ=6) is ungraded in both the summed-XQC and anchor-suite channels — Q3b's named first computation, cheap-first, can close the family before nucleation work. Q3c (absolute E_bond) remains root-blocked on OPEN-FP-SF-2-η.

- **[Patch 2379] SINGLE-FLIGHT CONDITIONALITY REGISTERED (founder-directed fidelity audit):** every XQC-channel verdict is conditional on XQC-2007 fidelity — one instrument, one ~100 s flight (1999), Erickcek et al. 2007 pinned; interpretation independently derived by four groups over two decades (Wandelt 2000; Zaharijas–Farrar 2005; Erickcek 2007; Mahdawi–Farrar 2017/2018; arXiv:2209.04387). Named systematic: nuclear-recoil thermalization efficiency ε_th (1879 assumed 1; literature brackets to 0.02). MEASURED sensitivities: the 2369 kill's twelve points robust at ε_th ≥ 0.1 (island-floor corner un-excludes only at 0.02; S_c ≥ 0.035 excluded across the whole bracket); the 2375 equilibrium-shape kill wholesale for ε_th ≳ 0.35–0.5; the corridor's live corner (central-repulsive, ρ ≤ 0.3) survives the entire bracket. Attenuation vindicated at envelope level (≲3e-6). OWED: the ε_th pin (HgTe/Si microcalorimeter nuclear-recoil thermalization — detector-physics literature). FUTURE DIRECT TEST: F5 reflight (46 events at the ruling point), Micro-X-class vehicle.
