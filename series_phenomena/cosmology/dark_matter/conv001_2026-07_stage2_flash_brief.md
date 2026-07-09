# CONV-001 FLASH BRIEF — Stage-2 verification round: the dimer XQC computation (Patch 2367, 9 July 2026)

**To the panel.** This is a FLASH round (2354 pattern) on a SINGLE computation whose
verification or refutation decides whether the dark-matter campaign records its
second kill. Stakes stated plainly: Patch 2366 registered a CANDIDATE-KILL — the
2007 XQC data appears to exclude the dimer-weighted corner of every passing region
at every registered island coupling, and per DM-3's own registration ("every
suite-passing population the formation kinetics realize is dimer-weighted or
dimer-heavy") a verified finding kills the formation-realizable population at
every audited frame. The 20-July OSF release is at risk for DM-1/DM-3 pending
this round. You are asked to BREAK this computation if it can be broken.

## The computation under review (everything reproducible from a clean clone)
- `DM-3/code/2365_overburden_ceiling.py` + `2365_results.json` — Stage 1: CSDA
  overburden ceilings at 2.8 GeV (SNOLAB 8.9e-32 / LSM 1.1e-31 / MINOS-depth
  2.3e-30 / surface 6.7e-29 cm², hurting-direction coherent-SI convention).
- `code/2366_dimer_stage2.py` + `2366_results.json` — Stage 2: the 1879
  partial-wave pipeline (Numerov, validated 0.1%, the v1-retraction instrument)
  run at the dimer: N=2, M=2m_el=2816 MeV, L=1.15 fm, E_rN=3E_c/16=0.05625 MeV,
  effective coupling E_rN×S_c per the 1888 island convention, S_c∈{0.012,0.035,
  0.05}, both signs, f∈{0.94,0.99}, ρ_χ∈{0.2,0.6} GeV/cm³. Outputs: σ_T →
  σ_eff = 1.8e-29–4.3e-28 cm² (above every underground ceiling); XQC totals
  482–53,523 predicted vs 527 observed.
- `code/2366b_perbin_test.py` + `2366b_results.json` — the corrected exclusion
  test: 1879's own registered per-bin conservative criterion (pred > obs +
  5√(obs+1) ⇒ EXCLUDED-class; "their X² 90% CL is stricter"). Result: ALL
  TWELVE pre-registered points EXCLUDED-class; violations persist below the
  island floor (S_c=0.006); driven by the 29–36 eV (obs 0) and 36–128 eV
  (obs 11) bins with published sensitivity factors (0.38, 0.51) applied.
- Context: `rate_computation_stage1_overburden.md`, `rate_computation_stage2_dimer.md`,
  `code/1879_xqc_recomputation.py`, `code/1888_si2_scan_and_predictions.py`.

## Verification items (verdict grammar per item: VERIFIED / REFUTED — error named / INDETERMINATE — check named)

**V1 — The N=2 adaptation.** Are the dimer parameters correctly derived from
registered quantities (M=2816 MeV, L=(N−1)·1.15=1.15 fm, E_rN=3E_c/(8N))? Is the
Numerov solver valid at the dimer's mass and momenta (lighter than the rod, fewer
partial waves — anything that breaks at N=2 that held at N=18)? Re-run or audit;
state which.

**V2 — The island-coupling convention (the load-bearing modeling choice).** 2366
applies the rod's D_st-suppressed screening factor S_c ∈ [0.012, 0.05] to the
dimer's rod–nucleus channel (effective coupling = E_rN × S_c), on the reading
that "the coupling the passing regions imply" is the registered island. Attack
this: does anything in the record entitle the dimer to a DIFFERENT (in
particular, smaller) S_c than the rod's island? Note the boundary scan: even
S_c = 0.006 — half the island floor — still violates; a save requires deriving
suppression the record does not currently contain, and any proposed save must
pay rent (name what it costs and where it is checked).

**V3 — The criterion.** 2366 pre-registered a B1 threshold using F5's reflight
kill-high (314) and OWNED it as mis-specified for a contribution to
already-observed data; the corrected test (pre-stated in 2366b's header before
the run) is 1879's own per-bin criterion. Two questions: (a) is the correction
handling itself sound (grade-as-written + owned + corrected-pre-stated), and
(b) is the per-bin conservative criterion the RIGHT exclusion standard here —
too strict, too loose, or correct? If XQC's unattributed background could absorb
the predicted counts in the violating bins, show it quantitatively.

**V4 — Robustness of the exclusion.** The violating bins at the weakest corner
are XQC's quietest (29–128 eV). Check: recoil kinematics of a 2.8 GeV particle
on HgTe/Si (do the recoils land where 2366 says they land?); the velocity/
exposure conventions (pinned verbatim from Erickcek et al. via 1879); the
sensitivity factors; the σ_T convention for the overburden comparison. Name any
convention whose defensible alternative reading changes the verdict.

**V5 — The consequence mapping.** IF V1–V4 verify: does DM-3's registration
("every suite-passing population is dimer-weighted or dimer-heavy," 2344/2349
record) indeed make the exclusion wholesale — the formation-realizable
population dead at every audited frame — or does any registered passing region
escape the dimer requirement? This is a record-reading item: cite the rows.

## Rules (binding)
Rent rule on all proposed saves. State which files you opened and what you
re-ran vs audited. **Deliverable per panelist:** V1–V5 verdicts with reasons +
at most two ranked additional findings. A REFUTED on any of V1–V4 with the
error named halts the kill and Stage 2 completes on the corrected number; V1–V4
VERIFIED with V5 verified makes the kill adjudication-ready for the founder.
INDETERMINATE verdicts must name the specific check that would resolve them.
