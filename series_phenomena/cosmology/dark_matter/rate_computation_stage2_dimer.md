# F-DM3-4 rate computation — STAGE 2: σ_dimer via the P2 machinery at A_dimer (Patch 2366, 9 July 2026)

## STATUS: VERIFIED BY FLASH PANEL (2368, V1–V5 all seats) — ADJUDICATION-READY, ON THE FOUNDER'S DESK
**Finding, stated plainly: the 2007 XQC data appears to exclude the dimer-weighted
corner of every passing region — at every point of the registered island
[0.012, 0.05], both potential signs, the full abundance bracket — and the exclusion
persists below the island floor (violations at S_c = 0.006).** Because DM-3
registers that *every suite-passing population the formation kinetics realize is
dimer-weighted or dimer-heavy*, a verified finding kills the formation-realizable
population at every audited frame: the second kill of the campaign, arriving
through F5's own channel, from data already in hand. NO verdict is moved by this
patch — the finding is registered as CANDIDATE, the verification path is a flash
panel round on this single computation, and the papers are untouched pending it.

## Reconnaissance (the arc's first step, as committed at 2365)
- The pipeline exists and is parameter-level in N: `code/1879_xqc_recomputation.py`
  (Numerov partial-wave, validated 0.1%, the instrument of the v1 retraction) +
  `code/1888_si2_scan_and_predictions.py` (the island convention: effective
  coupling = E_rN × S_c, island [0.012, 0.05] post-DAMIC, ruling 0.035).
- Clean-clone reproduction: 1879 re-run as-is, reproduces its registered
  EXCLUDED-class rod verdict (the CONFRONT-3 record).
- Dimer parameters, all registered quantities: N=2, M = 2m_el = 2816 MeV,
  L = 1.15 fm, E_rN = 3E_c/16 = 0.05625 MeV, same R_s = r_c/χ.

## Pre-registration (fixed in the 2366 script header before execution)
Island bracket S_c ∈ {0.012, 0.035, 0.05}; both signs; abundance f ∈ {0.94, 0.99}
× ρ_χ ∈ {0.2, 0.3, 0.6}; σ_T at 300 km/s on Ā ∈ {14.5, 22, 28}; per-nucleon-
equivalent in the Stage-1 convention; XQC exposure pinned verbatim from 1879 with
N_dm rescaled to (f·ρ/M_dimer); outcome map O-A/O-B(B1–B4)/O-C; hurting-first.

## Results (code/2366_dimer_stage2.py, 2366_results.json)
1. **σ_eff = 1.8×10⁻²⁹ – 4.3×10⁻²⁸ cm²** across the full bracket: ABOVE every
   underground ceiling from Stage 1 (SNOLAB 8.9e-32, LSM 1.1e-31, MINOS-depth
   2.3e-30) — **SENSEI/DAMIC-M/SuperCDMS-class experiments are overburden-blind
   to the dimer.** The listed-experiment null form of F-DM3-4 is unexecutable as
   written. Straddles the surface ceiling at the weak edge.
2. **XQC totals: 482 – 53,523 predicted events** vs 527 observed (2007), across
   the bracket; ruling point 8,000–25,000.

## Criterion correction (owned, stated before the corrected run)
The pre-registered B1 threshold (>314, F5's folded reflight kill-high) was
MIS-SPECIFIED for this question: it is a decision band for a future reflight of
the rod's 46-event prediction, not an exclusion criterion for a dimer
contribution to an already-observed spectrum. B1-as-written fired (all points
>314) but is set aside as mis-specified. The registered conservative exclusion
criterion is 1879's own, per-bin: predicted > observed + 5√(obs+1) ⇒
EXCLUDED-class ("their X² 90% CL is stricter"). The corrected run
(code/2366b_perbin_test.py, correction pre-stated in its header):

| point (sign, S_c, f, ρ) | violated bins | total | verdict |
|---|---|---|---|
| attr, 0.05, 0.99, 0.6 | 12 | 53,523 | EXCLUDED-class |
| attr, 0.035, 0.94, 0.2 | 8 | 8,016 | EXCLUDED-class |
| attr, 0.012, 0.94, 0.2 | 3 | 642 | EXCLUDED-class |
| rep, 0.05, 0.99, 0.6 | 12 | 19,952 | EXCLUDED-class |
| rep, 0.035, 0.94, 0.2 | 7 | 3,405 | EXCLUDED-class |
| rep, 0.012, 0.94, 0.2 | 2 | 482 | EXCLUDED-class |
(full 12-point table + boundary scan in 2366b_results.json)

**All twelve pre-registered points EXCLUDED-class.** Boundary scan at the weak
corner: violations persist at S_c = 0.010, 0.008, 0.006 — below the island floor.
The violating bins at the weakest corner are 29–36 eV (obs 0) and 36–128 eV
(obs 11) — the light dimer's recoils land exactly in XQC's quietest bins; the
exclusion rests on the most robust part of the spectrum, with the published
sensitivity factors (0.38, 0.51) already applied. **Background
model (panel repair, Patch 2368):** the criterion assumes ZERO background
subtraction — the predicted signal alone must exceed observed + 5√(obs+1); any
unattributed background only tightens the allowance. Weakest-corner margins:
15.1 predicted vs threshold 5 (29–36 eV); 142.3 vs 28.3 (36–128 eV).

## What could still save the corner (the honest list — each item owes rent)
(a) **A dimer S_c structurally below the rod's island** — would need DERIVING
    (the D_st screening suppression is a rod-channel quantity; nothing in the
    record entitles the dimer to extra suppression, and even ×2 below the floor
    still violates). The rent rule cuts against assuming it.
(b) **Solver validity at N=2** — the machinery is validated 0.1% at N=18;
    N=2 is lighter and fewer partial waves (cleaner, not dirtier). Panel-checkable.
(c) **Velocity/exposure conventions** — pinned verbatim from Erickcek et al.
    via 1879; panel-checkable.
(d) **Formation kinetics NOT requiring the dimer at 0.94–0.99** — contradicts
    the registered 2344/2349 record ("present at every passing point of every
    audited frame"); reopening it reopens the population finding itself.

## Consequences IF VERIFIED (mapped, not executed)
- The dimer-weighted corner dies at every audited frame ⇒ per DM-3's own
  registration, the formation-realizable population dies wholesale — the
  campaign's second kill (capture at the registered frame, 2333; population at
  the audited frames, via XQC-2007). Clause 1 exit-class event (the dimer face,
  adverse direction); OPEN-DM-DSPH-1 verdicts are UNFROZEN by the attested
  Clause 1 — the missing-physics search re-opens with both candidate branches
  dead.
- DM-1/DM-3 require major pre-release revision; the 20-July unified release is
  AT RISK and should not proceed for DM-1/DM-3 with this unadjudicated.
  DM-2 (cosmological channel) is not directly named by this finding — its
  20-July release can stand independent review.

## Recommended path (worker; decisions = founder's)
IMMEDIATE flash panel round (2354 pattern) on this single computation — scope:
the 1879-at-N=2 adaptation, the island-coupling convention, the corrected
per-bin criterion, the boundary scan. Days, not weeks; the runway to the 20th
exists precisely for this. On verification: founder adjudication of the kill,
paper revisions, release re-decision. On refutation: the refuting seat names
the error and F-DM3-4's Stage-2 completes on the corrected number.
