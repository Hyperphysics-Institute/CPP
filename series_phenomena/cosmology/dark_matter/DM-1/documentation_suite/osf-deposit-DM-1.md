# OSF Deposit Record — DM-1 (prepared at v1.4 + Patch 1891 hardening state)

Section-F registration record, house format (cf. `osf-deposit-EU-1.md`). Claude cannot deposit to OSF
directly; this file is the prepared metadata for Thomas (or Isak) to execute at the OSF web interface.
Fill the minted DOI back into this file, the paper title block, `paper_catalog.md`, and `INDEX.md`.
**GATE: do not deposit until the stability-cycle completion criterion (§6) is checked off and
founder-signed.**

## 1. Parent project and DOI versioning

- CPP parent OSF project DOI: `10.17605/OSF.IO/JXE8D`. Create **DM-1 as a component** of the parent
  (consistent with Capotauro / Chirality Continuum / EU-1 / TP-1 / SR-2 deposits).
- **Priority chain:** the conjecture registration of 8 June 2026
  (`osf_registration_qdp_dm_conjecture.md`, CONJ-COSMO-1 lineage) is the time-stamped priority record for
  the *idea*. DM-1 is the candidate-identification paper that supersedes-and-extends it. At deposit:
  (a) if that registration was minted as its own component, add it under OSF "Related resources" as
  "extends / supersedes-in-part" and state so in the description; (b) if it was never separately minted,
  upload it INTO this component as a dated priority artifact. Either way the git history
  (`github.com/Hyperphysics-Institute/CPP`) is cited as the fine-grained timestamp source.
- Version label at deposit: **DM-1 v1.4 (Patch 1890) + hardening record through Patch 1891.** Future paper
  versions update the same component (OSF preserves file version history); do NOT mint a new component per
  version.

## 2. Component metadata

**Title:** DM-1: A Substrate Dark-Matter Candidate — the Cross-Rod Aggregate with a Zero-Parameter
Screening Constant (η = χ = φ⁻³/6), a Measured Elastic Floor, Baryon-Sector Survival, and the First
Data-Drawn Portrait of the DP Sea

**Contributors:** Thomas Lee Abshier, ND (Hyperphysics Institute); Claude Opus (Anthropic).

**Category:** Project / Paper preprint.

**License:** CC-BY 4.0 (matches parent-project convention per the SM-6/SM-7 precedent; confirm parent
setting at deposit time).

**Tags:** dark matter; SIDM; Conscious Point Physics; 600-cell; golden ratio; zero-parameter prediction;
Capotauro constant; screening length; XQC; LZ; strongly interacting dark matter; DAMIC; measured
coefficients; effective theory; DP Sea; substrate inversion; falsifiability; multi-AI review.

## 3. Description / abstract (honest-scope version; paste into OSF Description)

> DM-1 identifies a dark-matter candidate within Conscious Point Physics (CPP): the Cross-Rod, an
> extended aggregate of N ≈ 15–20 colour-balanced substrate elements (m ≈ 25.3 GeV), whose
> velocity-dependent self-interaction arises from capture via a Sea-screened colour-residual channel.
> The screening length resolves to a zero-parameter candidate value: η = χ = φ⁻³/6 (R_s = 25.4 fm),
> equivalently a channel gap m_s = χ·ħc/r_c = 7.76 MeV — the gap, in lattice-pitch units, IS the
> programme's Capotauro constant. At that value the candidate passes the dwarf-scale empirical window,
> LSB galaxies, the full cluster bound ladder (including Andrade < 0.13 cm²/g, with the elastic floor
> MEASURED by rigid-body Monte Carlo at registry-pinned geometry rather than fixed by convention), and
> the Bullet cluster, while predicting a group-scale σ/m ≈ 0.03–0.05 — an order below the current mild
> detection and a standing falsifier. The baryon sector nearly killed the candidate: a partial-wave
> recomputation of the XQC rocket exposure (Born-invalid regime; solver validated to 0.1%) excludes the
> naive additive nucleon coupling ×20–30, and the composed XQC/LZ/overburden landscape leaves exactly one
> non-sterile survival island, S_c ∈ [0.012, 0.05] after a pre-registered DAMIC adjudication, whose
> center is the first-power colour-dipole scale R_N/R_s = 0.035 — adopted as an explicitly PROVISIONAL,
> survival-conditional ruling whose multipole order remains a standing derivation target with intact
> kill-branches (zeroth order = XQC-dead; second = LZ-dead). Under the programme's measured-coefficient
> discipline (CONV-004; Galilean-layer effective theory with MEASURED/DERIVED/CONJECTURED ledger tags and
> an overdetermination requirement), the campaign's data were inverted through registered-structure
> forward maps into the first empirical portrait of the DP Sea: colour coupling α_q ≈ 0.9, channel ladder
> α_e/α_q ≈ 6×10⁻³, colour-channel cancellation C_r ≈ 2.4×10⁻⁴, occupancy f_occ ≈ 0.1 (a sparse Sea) —
> with the under-determined directions and prior-shaped entries flagged as such. Near-term falsifiers:
> an XQC-class reflight sits ×11–×30 above the predicted 8–50 recoil events; a thermalized deep-Earth
> rod population n̄ ~ 2×10¹³ cm⁻³ is predicted. The record includes three full five-member adversarial
> AI review cycles (5/5 each), one unanimously-ratified retraction of a previously ratified claim, and
> every verify script and verbatim reasoning fragment needed to reproduce each number. The work is
> Layer-C consistent and framework-conditional; it does not claim completed derivation of the substrate
> coefficients, and states exactly what would kill it.

## 4. Files to upload (manifest — all paths repo-relative; upload as a zipped snapshot PLUS loose key files)

**Loose (top-level of component):**
1. `DM-1/DM-1_substrate_dark_matter_candidate.pdf` (compiled v1.4)
2. `DM-1/DM-1_substrate_dark_matter_candidate.tex`
3. `OPEN-SS-43_Rs_derivation.md` (the campaign record, §§1–30)
4. `SI-1_unknowns_and_forward_maps.md` (the inversion-arc foundation)
5. `founders_voice/founder_ruling_measured_coefficients_2026-07-06.md` (CONV-004, verbatim)
6. `osf_registration_qdp_dm_conjecture.md` (the 8 June priority record; see §1)
7. `DEPOSIT_ADDENDUM_1891.md` (§7 below — generate at deposit time from this section)

**Zipped archive `DM-1_full_record.zip`:**
8. `DM-1/documentation_suite/` (complete: changelog, development, glossary, keywords, mechanism ×2,
   phenomena, philosophy, reviews)
9. `DM-1/review/` (packages v1.2/v1.3/v1.4 + verbatim panel returns ×3)
10. `code/18*.py` + `code/1871_results.json` + `code/1888_xqc_island_grid.json` (49 verify scripts, the
    complete computational chain 1811–1891)
11. `reasoning/18*.md` (63 verbatim reasoning fragments)
12. `frontier_sectors/SS.md` (registry state at deposit)

## 5. Zenodo parallel (optional) + arXiv candidate

Zenodo: same metadata; cross-link OSF DOI under Related Identifiers ("isVersionOf"). arXiv abstract
candidate: use §3 trimmed to 1,920 characters (the honest-scope paragraph survives trimming; cut the
review-process sentence last).

## 6. Stability-cycle completion criterion (OBJECTIVE — the OSF gate as a checklist)

The cycle that started at **Patch 1890 (6 July 2026)** is COMPLETE when ALL of:
- [ ] **Duration:** ≥ 14 calendar days elapsed (≥ 20 July 2026) OR ≥ 2 full DM-lane working sessions
      after Patch 1890, whichever is LATER.
- [ ] **No load-bearing corrections:** zero changes to any quantitative claim, falsifier, or governance
      sentence in the DM-1 notices. (Pre-registered adjudications recorded in the campaign file — the
      Patch-1891 DAMIC trim is the precedent — do NOT count; that is the falsifier system operating.)
- [ ] **No open REFUTE:** no panel member or founder-flagged objection standing against v1.4.
- [ ] **Residual scan:** one closing pass over the open-thread list (D_st ✓ done; DAMIC ✓ done;
      rod–nucleus MC refinement, formation cap, F1/F5 data watch — confirm none has produced a
      load-bearing result).
- [ ] **Founder sign-off:** Thomas states in-session "stability cycle complete — deposit approved."
Then execute §§1–4 and backfill DOIs.

## 7. Deposit addendum (Patch 1891 refresh — paste into `DEPOSIT_ADDENDUM_1891.md` at deposit)

> **Post-v1.4 pre-registered adjudication (Patch 1891, 6 July 2026).** The v1.4 notice pre-registered
> that a DAMIC-floor determination would adjudicate 40% of the accepted substrate region. That
> adjudication has been executed by bounding argument (MF17 arXiv:1709.00430 pins; ≥10³ margin): the
> unshielded corner S_c < 0.012 is excluded, trimming the survival island to **S_c ∈ [0.012, 0.05]**
> with the ruling point (0.035) untouched. Consequently the region-weighted F5 prediction quoted in the
> v1.4 notice (2–28 events) refreshes to **8–50 events (median ~17; margin ×30 below existing XQC
> data)** and is robust across 1.5 orders of magnitude of D_st-prior variation. The in-paper figure is
> retained as the time-stamped pre-adjudication value per the notice's own statement; this addendum is
> the current value. Nothing in this addendum is a correction: it is the pre-registered falsifier system
> operating as designed.

## 8. Post-deposit actions

- `paper_catalog.md`: DM-1 row → "Registered on OSF" + component DOI.
- `INDEX.md` + `frontier_sectors/SS.md`: DOI cross-links; OPEN-SS-43 status → RELEASED.
- Paper title block: add component DOI (this is a metadata edit, permitted post-cycle).
- Announce per founder's choice (fellowship essay / Renaissance Ministries channel — the reader's guide
  of item 3 is the companion for that step).
