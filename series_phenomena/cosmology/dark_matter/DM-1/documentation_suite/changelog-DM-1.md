# Changelog — DM-1 (Substrate Dark-Matter Candidate)

Canonical .tex: `DM-1/DM-1_substrate_dark_matter_candidate.tex`
(Filename fixed; version history tracked here, not in the filename.)

**Versioning convention:** assembled drafts ship at **v0.1 (DRAFT)** and increment
through the panel review cycle (v0.2, v0.3, … as reviewer feedback is folded in),
promoting to **v1.0** only once the multi-AI panel is satisfied at final ship.
DM-1 is pre-review.

## v1.1 — Mechanism Correction: Fragmentation → Capture — Patch 1860 (3 July 2026)

- **PANEL RE-RATIFIED 4/4 (same day, Patch 1862):** Grok, Gemini, Copilot RATIFY;
  ChatGPT RATIFY-WITH-CHANGES; no REFUTE; 4/4 SCRIPT-EXECUTED. Changes folded:
  "parameter-free" → "robust within the stated capture model"; explicit process
  note added (the v1.0 panel missed the stale provenance; caught by audit, not
  review). CONV-003 registered. Copilot's ∝1/v⁴ gloss vs corpus ∝1/v² pinned to
  OPEN-SS-43. Records: `documentation_suite/reviews-DM-1.md` Round 2 (curated);
  `review/reviews_v1.1_panel_returns.md` (verbatim).

- **What changed:** the v1.0 velocity-dependence mechanism (Cross-Rod fragments at
  cluster velocities ⇒ collisionless) is **retracted**; the mechanism is **capture**
  (screened unipolar E_qq residual, reasoning/code 1857/1858).
- **Why:** the 1859 collision-energy reconciliation **proved** §5's fragmentation
  figures (~1.95 MeV cluster / ~0.78 keV dwarf) were unrescaled imports from the
  0860 **hoop** ledger (N=1183, m_rung=264 MeV, 312 GeV rod). At the Cross-Rod's
  own pins (N=5–60, m_el=1408 MeV, 7–85 GeV rod) typical-cluster collisions
  deposit 0.044–0.53 MeV < E_ee = 0.9 MeV: **no fragmentation** (the Maxwellian
  tail prunes only N ≳ 40). Verify: `code/1859_collision_energy_reconciliation.py`.
- **What stands (robust, parameter-free):** velocity-dependent, cluster- and
  Bullet-safe self-interaction — capture's steep Rutherford-like falloff gives
  cluster σ/m ~ 0.003, Bullet ~ 0.001 for **any** screening length R_s.
- **What is now conditional:** dwarf-core magnitude, gated on the de-novo
  R_s(N) ~ 15–30 fm / E_c ~ 0.3 MeV derivation (**OPEN-SS-43**).
- **Convention settled (task 3):** observable = transport σ_T/m = ε·0.11·N,
  ε ≈ 0.30 (1856 MC); bare 0.11·N demoted to perpendicular-limit upper bound.
  Cluster floor ⇒ **N ≲ 20** (`code/1860_floor_ceiling_convention.py`), cutting
  the v1.0 N = 5–60 band from the cluster side.
- **Where:** layered olive mdframed notice at §5 (`sec:xsec`), restated live
  falsifiers at §Falsifiability, top-of-paper notice, title bump. All v1.0 text
  retained as the superseded record per house convention.
- *(Record note: the v0.1-R2 → v0.2 → v1.0 entries were tracked in the .tex
  header changelog block, Patches 0879–0889; see the .tex header for that arc.)*

## v0.1-R (DRAFT, under revision) — Extended-Aggregate Pivot — Patch 0864 (25 June 2026)
- **Retraction.** The point-scattering self-interaction σ/m ≈ 0.20 cm²/g (abstract,
  §5, §6, Table 1, Figs. 2–4) is withdrawn. Patch 0859 identified it as an artifact
  of a hard-wall boundary condition in the partial-wave solver. Corrected screened-LJ
  point-scattering gives σ/m ≈ 0.11 cm²/g — flat but ~5–20× below dwarf-core needs,
  no closure across the f-band. The as-shipped positive coring discriminant does not
  hold for the bare aggregate.
- **Survives.** Velocity-independence (the flatness) is unaffected by the BC error —
  a robust kinematic consequence of the heavy constituent (264 MeV) + short range
  (1.3 fm). Still distinguishes the candidate from light-mediator SIDM (∝ v⁻⁴).
- **Re-scope.** Magnitude/coring discriminant (§6) re-scoped to EXTENDED charge-offset
  aggregates (2eDP:2qDP ribbons, hTetra-chain loops, 4-wide crosses), σ/m ∝ N, hitting
  0.6–2 cm²/g at N ~ 10²–10³ rungs (R ~ 50–400 fm). Supporting arc:
  - 0860: σ(N) pass + (N, E_bond) over-determination ledger; one (N,E_bond) fits
    magnitude+lifetime+fragmentation iff ambient thermal-eDP kT_amb ≲ 19 keV.
  - 0861: PCD formation kinetics — loop-size knob collapses onto rung-bond
    persistence length ℓ_p (ring-closure peak L ≈ 3.4 ℓ_p); in-band ℓ_p ~ 100–700 fm
    is the same ℓ_p the σ/m ∝ N scaling requires.
  - 0862: stiffness ladder hTetra < ribbon < cross; one edge-bond strength sets ℓ_p
    AND selects geometry; glueball-dilution tax identified.
  - 0863: chaperoning (high [hTetra], zero-barrier hDP→hTetra) crosses ribbons before
    glueball apposition → dilution defanged (glueball fraction <10% iff [hTetra]/[ribbon]
    ≳ 9); surviving relic = two extended species (4-wide cross + hTetra loop), both ∝ N.
- **Deciding calc (make-or-break, SF-2/SF-5, cross-window).** Derive the 2eDP:2qDP /
  hTetra edge-bond SSV potential → (G1) ℓ_p ~ 100–700 fm (κ_θ ~ 100–700 kT_form,
  ~3–8°/hinge) + second-moment ladder; (G2) E_bond ~ 0.8 keV–2 MeV; (G3) glueball-arrest
  radius ~ 100s fm not ~fm + branching ratios (registered OPEN-SS-39).
- **Grade now:** Layer-C consistency (velocity-independence positive; magnitude via an
  underived substrate stiffness). NOT a positive coring discriminant at this revision.
- **Stays v0.1.** In-place revision notice added at §5 covering §5–§6; as-shipped body
  retained as record. NO promotion to v1.0; gated on the SF-2/SF-5 deciding calculation.


## v0.1 (DRAFT) — Positive-Discriminant Candidate — Patch 0856 (assembled) / 0857 (version label) (24 June 2026)
- **Promotion to .tex.** Publication-form conversion of the working markdown draft
  `series_phenomena/cosmology/dark_matter/DM-1_draft_manuscript.md` (assembled
  Patches 0700–0855) into the EU-1 house style (article class, natbib/plainnat,
  CPP macros, per-paper subfolder).
- Three figures included via `\graphicspath{{../figures/}}`: residual V(r) +
  saturation (Fig. 1, Patch 0849), density confrontation (Fig. 2, Patch 0850),
  core-radius-vs-σ/m panel (Fig. 3, Patch 0851).
- Embedded bibliography: CPP flagships (SF-3, SF-5, SR-1, QM-1) + verified
  external refs (Mateo+ 1991; Goerdt+ 2006; Jardel & Gebhardt 2012; de Blok+ 2008;
  Oh+ 2008; Kaplinghat, Tulin & Yu 2016; Li 2004; McCrea & Milne 1934). All
  external citation details web-verified at promotion.
- Honesty carried verbatim from the draft: the IC 2574 high-velocity tension
  (abstract, §6, §7, grade), the calibrated mass scale + abundance (§8), and the
  Sea-gravitation gate now down to one condition after the c08 discharge (§9,
  Patch 1161). Grade: positive discriminant, not full identification.
- Compiles clean (pdflatex, two-pass: 0 undefined citations/refs; 9 pp).

### Content provenance (markdown draft → .tex)
Draft sections §1–§11 → paper §§1–10 + appendix; internal dev scaffolding
([FILLED]/[TIGHTEN]/[DONE] markers, the §11 checklist, the provenance block)
dropped in the publication form. The markdown draft remains the working source
of truth; the .tex is the shippable artifact.

### Open at ship (none gating; all flagged in §8–§10 + Open Directions)
- **Review cycle OPENED (Patch 0858):** self-contained panel review package at
  `review/DM-1_review_package_v0.1.md` (claim chain, triage, embedded stdlib
  verify code, reviewer steers, response format all inline). Dispatch to the
  panel (ChatGPT/Grok/Copilot) pending; responses aggregate in
  `review/reviews-DM-1.md`. v0.1 → v1.0 promotion gated on panel satisfaction.
- f pin-down (companion mass-scale / colour-polarizability) → collapses the
  magnitude band and decides the IC 2574 tension.
- Sea-gravitation: one remaining condition (event-horizon IR-scale selection).
- Abundance route-B (asymmetric DM) derivation of ~5:1.
- OSF deposit manifest (Thomas-action manual step).
