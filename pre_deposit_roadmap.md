# Pre-Deposit Roadmap — what must be settled before the corpus goes to the CERN repository (Zenodo)

**Location:** `/CPP/pre_deposit_roadmap.md`. **Registered:** Patch 4335, 29 September 2026 (Session 241), at the founder's
request (*"make the short, prioritized list of the theoretical developments … needed before publication on Zenodo …
begin the process of completing the list"*, `founders_voice/4335_…`).
**Queue entry:** TODO-4335-PREDEPOSIT (`todolist.md`). Update this file when an item's status changes; the work itself is
done and recorded in the lanes named below.

**Standing facts.** Nothing is deposited yet (4334). PDFs are built by Isak at deposit (CONV-012). The founder's 19 Aug 2026
ruling (OPEN-ORG-023): a small test-run deposit first; then **most of the 105 non-gravitational papers wait until GR-1, its
companions and OPEN-GR-FE-1 are done** — and **that condition was discharged on 20 Aug** (OPEN-GR-FE-1 CLOSED at Patch 3267,
founder: "Confirm FE-1 complete."; see the correction under item 1). Deposit approval is the founder's (the queue's APPROVED column, fail-closed). A trial deposit has already been done successfully (founder, 29 Sep).

---

## The list, in order

**0. Honest labelling and the scorecard (continuous; do first, it is cheap).**
- `theory-overview.md` is stale since the 21 June commit (header 17 May); 75 scorecard-registry commits have landed since.
- Headline claims must say what they rest on:
  - "108 zero-parameter correspondences" rest on 9 axioms and **2 calibrations**.
  - W, Z and Higgs use calibrated η factors.
  - Koide K = 2/3 is conditional on Layer B.
  - SS-8 and SS-9 are conditional on hypothesis sets.
  - α is a calibrated relation (CAL-ZBW1-SWING).
  - Λ is calibrated.
- `publication_readiness.md`: 71 papers show internal codes in their PDFs; 7 are blocked by unfinished text.
- **Enforced from 4335** by `code/overview_staleness_gate.py`. **Closes when** the gate passes and every README and
  theory-overview headline carries its basis. *Lane:* governance (TODO-4335-OVERVIEW).

**1. Gravity: bring the records into line (not a derivation).**
- **Correction (4339).** As first registered at 4335, this item said the general field equations were not derived and
  that deriving them was the founder's deposit gate. **That was wrong.** OPEN-GR-FE-1 CLOSED at Patch 3267 (founder,
  20 Aug: *"Confirm FE-1 complete."*). GR-1j V1.0 derives the general static field equation (T-1), a Birkhoff-type
  uniqueness for isolated, no-incoming-radiation sources (T-2), and a conserved census current (T-3) — all conditional on
  the PSR constitutive form at W2 strength, with k a registered normalisation. The FE-1 condition of OPEN-ORG-023 is
  discharged. The error was mine: I read the item's registration text and not its status line.
- **Radiative sector:** closed by SR-2/A3′ (λ = 16πG/c⁴). **The full nonlinear Einstein equations + Λ** remain OPEN-SR-4
  research and do not gate deposit.
- **What remains before the main wave:**
  - GR-1d V3 still predicts a 2.15 ± 0.14 ms echo; AP-5 (3699) and GR-2 V2.8–V2.11 withdrew the echo (PRED-O-39 NULL).
    GR-1d must be brought into line (TODO-4339-GR1DECHO).
  - The "G = ħc/m_P², no free parameters" wording (TODO-4300-HBARSWEEP): GR-1, GR-1a, GR-1c done at 4339; the GR-1a
    FAQ/phenomena companions remain.
  - GR-1i: reviewed and cleared 5–0 (CONV-029) but still V0.1 (TODO-4339-GR1IV1). GR-2 recompile at deposit (Isak).
  - OPEN-ORG-023's entry was never updated after 3232; the planned test-run set (the spin trio) is no longer available
    because SPIN-1/2 are held (TODO-4339-TESTRUN).
- **Open research that does not gate deposit:** O2 (G in DI-bit counts, 4310–4313); the black-hole PSR factor 4.1 (4322).
  *Lane:* GR / governance.

**2. The lattice-to-SI scale and the PSR floor.**
- OPEN-SD-lattice-scale is marked *"#1 foundational — blocks experimental scrutiny"* (`frontier_sectors/SM.md`): how
  many GPs make a Planck length (R = PSR/s = 10³⁰ or 10³²).
- Tied to it is the black-hole PSR. Its disagreement with the register floor l_P/2 was 10¹⁶ (4310). After this session's
  flip ruling it is a factor of 4.1 (4322 §4, not yet re-adjudicated). 4311 dropped the surface-count identification; the
  critic owes whether to reverse that.
- *Closes when* R is fixed by an independent observable or declared a calibration with its consequences stated.
  *Lane:* foundations/GR.

**3. Spin and the unit of action.**
- ħ is identified, not derived; this session gave ħ/2 a physical carrier (the Planck ZBW half-swing, 4320/4325), but its
  size is calibrated.
- SPIN-1 and SPIN-2 are **held from deposit** because they take ħ/2 as input (TODO-4289-SPINREV/SPINSWEEP).
- OPEN-QM-3 (spin-½ and Pauli) is open; its 4098 progress note was retracted.
- Spin is input throughout the corpus. *Closes when* SPIN-1/2 are revised to state ħ/2 as input, and the corpus-wide
  "spin derived, no free parameter" wording is swept. *Lane:* QM/SPIN.

**4. Layer B and the QM foundation.**
- OPEN-SS-16 (operator formalism and system–bath coupling, "CRITICAL") conditions Koide K = 2/3 and much of the strong
  sector.
- OPEN-QM-1-REGROUND ("un-conditions the QM sector") and OPEN-QM-1 (Born rule) sit beside it.
- *Closes when* derived, or when every dependent paper states its conditionality in print. *Lane:* SS/QM.

**5. The electromagnetic constants and α.**
- OPEN-FP-6-CONSTANTS: μ₀, ε₀ and c rest on a parameter-tuned toy model.
- α = PSR/(2L) with one calibrated swing (CAL-ZBW1-SWING, 4326–4329). Its local position invariance is **not established**: 4330's "passes via saturation" had an outward-step sign bug (independent critic, 4352); with the rule as ruled the fill is 0.72–0.80, and a far-field problem is open (OPEN-ALPHA-FARFIELD-1). The logarithmic running law (4331) needs a DP-arc cloud model.
- *Closes when* α is published as a calibrated relation with LPI and the running stated as open constraints (the honest option now), or the far-field and cloud models pass them.
  *Lane:* EW → foundations/SF-6.

**6. Special relativity: the residual theorem debt.**
- **Correction to the list as first given in chat (29 Sep):** OPEN-SR-EPSILON is **not** open at the verdict level. It
  was recorded SATISFIED for closed self-bound patterns at W2 world-call strength (founder ruling, Patch 2502; ε = γ − 1
  grounded at the energy level via the SF-6 pin and Laue).
- What remains are theorem-grade debts, **not verdict-bearing**: OPEN-SR-10 item (i) (the from-PCD dispersion
  derivation), SF-6 debt (b) (vector completion) and capacity-set integration.
- SR-1 can be published with those stated. *Lane:* SR.

**7. Cosmology: dark matter, dark energy, the cosmological constant — a scope decision, not a prerequisite.** (Status as
recorded, surveyed at 4335.)
- **Dark energy:** the corpus's own verdict is *"Λ-like, Λ from calibration, no distinguishing dynamical mechanism"*
  (3430; w = −1.00 ± 0.02, 3419).
  - Routes closed: VARC-1 (3430), GRADIENT-1 (3433), TIMEDIL-1 (3440). F-W-1 (w = −1.023) was demoted: its IR scale is
    fitted and its sign is contradicted by the corpus's own calibration.
  - The only live route, the open/comoving build, has a frozen budget and no execution. There is no DE paper.
- **Cosmological constant / vacuum energy:** TN-SR-1's 1/N² ≈ 10⁻¹²² suppression is labelled by the paper itself *"a
  conjecture (OP-SR-5), not a derived theorem"*.
  - OPEN-SR-5 is open (Step 5b partial).
  - 3920 found the Λ density degenerate in the Friedmann equation, so it cannot set H.
  - 3930: the EU lane is not working Λ.
- **Dark matter:** CONJ-COSMO-1 (Tetra-Gravity DM) is a conjecture, conditional-PASS on structure formation.
  - The candidate is the 16-plane ring at 11.26 GeV (3426). At its real mass, clumping is **31 orders short** of the
    required amplitude (Poisson δ ≈ 6 × 10⁻³⁷ against 10⁻⁵), and white Poisson clumping also **fails on shape at every
    clump mass** (3884, which also retracted 3882's "within a factor of two").
  - DM-1 and DM-3 are on the never-deposit list (record, not release); DM-2 is not approved.
  - Open: OPEN-DM-SIGN-SELECTION-1, OPEN-DM-PAIRING-KINETICS-1, the owed "DM dance v5" rerun.
- **The ~86-order DE–EU tension** was resolved at 3876 as the two lanes counting different objects. The counting bound it
  left (N_CP ≥ 1.7 × 10¹⁸³, 99 orders above the founder's 10⁸⁴) is owed to the DE lane (TODO-3930-EU).
- **Recommendation (sequencing, PD-006; deposit approval stays the founder's):** none of these is a prerequisite for
  depositing the rest of the corpus, **provided nothing in the deposited papers claims them**.
  - Keep DM-1/DM-3 as they are, and DM-2 unapproved.
  - Deposit TN-SR-1 only as the labelled conjecture it already calls itself, or hold it.
  - Sweep the deposited papers for any "CPP explains dark matter / dark energy / Λ" wording and scope it to "conjecture"
    or "calibrated".
  - A cosmology wave follows when a DM derivation closes the amplitude and shape gaps or the DE comoving build runs.

**8. Chirality — OPEN-SD-CHIR-PRIMITIVE / OPEN-CHIR-3.**
- Handedness is a primitive, not derived.
- It can be published as a stated axiom without damaging anything else. *Lane:* chirality/EW.

---

## Work log (append; newest last)

- **4335:** roadmap registered; `code/overview_staleness_gate.py` added (the item-0 gate); OS and bootup amended
  (theory-overview refresh triggered by scorecard-registry changes, not every turn).
- **4336 (item 0, stage 1):** theory-overview.md header, *Current state and headline basis* section and one-paragraph
  theory rewritten from the live registries; the gate reports PARTIAL until stage 2 (paper tables, results, series status,
  open problems, README headline table) lands.
- **4337 (item 0, stage 2):** theory-overview.md fully refreshed (results re-audited row by row with a basis column);
  README headlines refreshed; the overview gate passes. Item 0 stays open for TODO-4337-TALLYHOLDS, TODO-4337-SIGMALINK and
  the corpus-wide wording sweep.
- **4338 (item 0):** predictions.md tally audited in place (holds, calibrated-in-effect rows, SS-7 measured input tagged;
  PRED-C-67/72 corrected); σ now cites CONJ-SS-5. Item 0 remains open only for the corpus-wide wording sweep.
- **4339:** **item 1 corrected** — OPEN-GR-FE-1 was closed at 3267, so the founder's deposit gate is discharged; the item is
  now records-into-line. GR-1/GR-1a/GR-1c "no free parameters" wording scoped (TODO-4300-HBARSWEEP, papers part). Sweep tool
  `code/claim_wording_sweep.py` added (item 0/7).
- **4340 (items 0 and 7):** cosmology wording sweep done (DP-Sea v1.3, EU-1 v1.6.1; others already labelled) —
  `wording_sweep_register.md`. Item 7's wording condition is met for every deposit candidate except DM-2 (not approved).
  Item 0 continues with the zero-parameter triage (TODO-4340-ZEROSWEEP).
- **4341 (item 0):** zero-parameter triage started — SF-2 (arithmetic erratum: the predicted Weinberg value had been
  written as the observed one) and SF-4 done; a corpus-wide compile pass registered (TODO-4341-COMPILEERR).
- **4342 (items 0 and 8):** SS-8 and Capotauro triaged; Capotauro v2.4 carries a status note (chirality: magnitudes only,
  the hand a primitive — consistent with item 8); identifier-appendix regeneration registered (TODO-4342-GLOSSREGEN).
- **4343 (build readiness):** identifier appendices regenerated (72 papers); compile pass: 98/123 clean, the 25 others listed
  in `compile_status.md` (TODO-4341-COMPILEERR) — a precondition for Isak's PDF build.
- **4344 (build readiness):** 121/122 compile clean; DP-Sea's missing figures are the one blocker (founder asked).
  Deposit queue 122 (a development transcript excluded).
- **4345 (item 1):** GR-1d → V4 (echo withdrawn, status note); GR-1i → V1.0. Item 1's records-into-line work is done except
  the test-run choice (proposed: SS-3 and GR-1i; founder approval) and the OPEN-ORG-023 close.
- **4346:** founder: a trial deposit was already done successfully; no second trial (TODO-4339-TESTRUN closed). Its papers
  and DOIs must be written into the queue before the wave (TODO-4346-TRIALDOIS).
- **4347 (item 0):** zero-parameter sweep second tranche: EU-1 pivot stated as adopted; SS-7 inputs and fully-CPP RMS (1.77%);
  held SS papers carry status notes.
- **4348 (item 0): CLOSED.** The zero-parameter sweep is complete; with the overview refreshed (4336–4337), the tally audited
  (4338), the cosmology wording swept (4340) and the gate passing, item 0's closing condition is met. Build readiness is
  tracked separately (compile_status.md: DP-Sea's figures).
- **4349 (item 3):** SPIN-1 v2.2 and SPIN-2 v2.1 revised and released from the hold; SPIN-3 noted; spin sweep done.
  Item 3's wording condition is met; the physics (why the elementary action is ħ/2) stays open (OPEN-QM-3).
- **4350:** deposit queue now reports each paper's current version (TODO-4333-VERSIONPARSE closed); R-CP-NO-REST-MASS
  registered under A1′ (TODO-4316-CPMASSAXIOM closed).
- **4352 (item 5):** independent critic of the α arc: algebra confirmed; the LPI pass withdrawn (4330 sign bug); on-shell running
  numbers and the Lange 2021 clock bound adopted; c03 v2.3. α is a calibrated re-expression; LPI and running are open constraints.
- **4353 (item 5):** founder's inward-fill landing protocol tested: the band's outer edge is pinned to the PSR (near-field
  LPI premise restored as a protocol); solid only if a blocked bit spreads sideways first (TODO-4353-LANDINGRULE). Far field still open.
- **4354 (item 5):** R-DIBIT-INWARD-FILL registered (founder: sideways first). Far field is re-radiation: Gauss's law follows;
  α's LPI there hangs on one founder answer (does a charge read the net flow across its own PSR?).
- **4355 (item 5):** the registered relay answers the window and Gauss's law; α's far-field LPI now hangs on one founder answer
  (does a charge's family fill its whole PSR ball?). Otherwise k_α = −3.
