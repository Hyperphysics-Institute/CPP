# CONV-001 ROUND — VERIFY THE SS43-Q5 TERMINAL GRADING (the corridor kill at {N = 8}) + OPEN IDEAS CHANNEL for the surviving species

**Round type:** VERIFICATION + GENERATIVE (findings-only ideas channel).
Founder verbatim: **"Please initiate review protocol as recommended."**
(11 July 2026; worker recommended this round at the §34.22 grading record.)
**Patches under review:** 2412 (the Q5 launch contract, §34.21) and 2413
(the execution + grading, §34.22: `code/2413_ss43_q5_sign_corridor.py` +
`code/2413_results.json`; `reasoning/2413.md`). Consumed derived machinery
(CLOSED inputs, cite-don't-re-derive, but attackable AS INPUTS if you find
a real defect): 2399 (linear-in-χ gap, R_s = 25.42 fm), 2401 (Class V-t),
2403 (the discreteness defect, (N−1)-order), 2410 (the four-number
direct-detection adjudication). Campaign file: §34 in
`OPEN-SS-43_Rs_derivation.md`, especially §34.21–§34.22.

**Raw links (AI-fetchable):**
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/OPEN-SS-43_Rs_derivation.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2413_ss43_q5_sign_corridor.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2413_results.json
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2413.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/reasoning/2412.md
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2403_ss43_q4c_residual_scale.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2383_q3b2c_family_channels_sign_grade.py
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_phenomena/cosmology/dark_matter/code/2383_joint_couplings.json
- https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/frontier_sectors/SS.md

## The stakes, stated plainly

This is the OPEN-SS-43 campaign's TERMINAL grading. All five pre-registered
stages (Q1–Q5) are executed. At Q5 the pre-registered kill fired: **the
{N = 8} ring family — the sole survivor of the four-number direct-detection
adjudication — is dead at the dwarf corridor, fully derived.** The founder's
successor decision (register a CDM-like no-coring branch, invest in the
|SSV| dissipation derivation, pursue a polydisperse carrier, or exit) hinges
on this verdict being REAL. A hostile pass is invited: if the kill is wrong,
now is the time. Symmetrically: if the kill is right, say so plainly — a
soft-pedaled confirmation helps no one. **No verdict moves in this round**;
the grading is recorded at §34.22 and the founder adjudicates on your
returns.

## What was computed (one paragraph)

**2413 (Q5 execution):** the effective per-channel transfer sign for the
closed N = 8 ring (11.26 GeV, monodisperse w(8) = 1.0) was DERIVED, not
chosen. The E_qq capture residual (attract-only, 1858) enters ring–ring
scattering with the 2403 discreteness-defect protection on BOTH legs — each
partner is a closed Class V-t loop, so the pair coupling carries
D̄²(q ~ ħc/r) with D̄/ring = 1.21×10⁻¹⁴ at r = R_s = 25.42 fm. Under a
deliberately GENEROUS unprotected ceiling (first-moment envelope
g²_env = N²·E_C·R_s = 488 MeV·fm — chosen to hurt the kill's own margin)
the derived ring–ring coupling is 7.1×10⁻²⁶ MeV·fm at the screening range
and 6.9×10⁻¹³ even at the 3-fm far-field edge. The surviving dwarf-channel
term is the E_ee coat floor (repulsive; the 1868–1871 rod-measured record,
transplanted byte-identical) — so the derived dwarf-velocity sign is
REPULSIVE, coat-dominated, discharging the F-A2 ARGUMENT-LEVEL tag AGAINST
the 2383 attractive default. The 2383 two-channel corridor was then
re-graded at w(8) = 1.0: the anchor channel fails BOTH audited frames at
every probed range (viol 27.13 extended / 90.42 central; totals = the bare
coat floor 0.111/0.091/0.051/0.041 at v = 30/50/200/1500 km/s; binding
wall = the v = 30 coring demand). Hurting-first diagnostics: the extended
frame is coupling-closed (required g² = 2.61×10⁻² MeV·fm; shortfall
10^23.6) and the central frame is SHAPE-closed (no passing g² exists on
[10⁻⁸, 10⁶]; best viol 1.80). XQC passes at the derived coupling (exact
cached ρ* ≥ 1 at the island floor, both signs, monotone in S_c). Battery
ALL PASS: V1 scratch-chain green (2410/2403/2401/2393); V2 pass-gates —
all 17 committed 2383 anchor viol values and all 438 ρ* rows reproduced at
rel 0.0 BEFORE grading, coat floor verified against the committed 1871
band, C_8 selection exact fresh with the (N−1) law at ratio 1.09; V3 3/3;
V4 zero tunables, no external data; V5 cache read-only. One instrument
misstep gate-caught (a sub-numerical-floor V2 probe at q = 2 MeV — the
2403 absolute-floor criterion reapplied; the error over-stated the E_qq
coupling, i.e., ran AGAINST the kill; no grading value moved).

## PART I — VERIFICATION (grade each: VERIFIED / REFUTED-error-named / INDETERMINATE-check-named)

**V1 — the kill itself (the corridor re-grade).** From the committed
machinery (`2383_q3b2c...py` ingredients, transplanted verbatim into 2413):
verify that eff_dist at w(8) = 1.0, R_s = 25.42 fm, with the derived g²
reduces to the bare FL floor; that viol(audited_extended) = 27.13 and
viol(audited_central) = 90.42 against the committed 2345 frames; and that
the §34.21 kill clause ("anchor fails BOTH audited frames at the derived
coupling") therefore fired mechanically, with no post-derivation
adjustment. Challenge: name any error in the frame values, the viol
convention (2349/2371), the floor transplant, or the clause's application
— with direction (does fixing it un-fire the kill?).

**V2 — the sign derivation (the double defect protection — the round's
load-bearing physics).** (a) Is the double application of the structure
factor registered-structure sound: the 2403 defect law was derived for the
ring as SOURCE against a nucleon probe; 2413 applies D(q) on BOTH legs of
a ring–ring amplitude (source and responder are each closed Class V-t
loops under the same C_N selection). Name any registered mechanism by
which a ring RESPONDS to an external residual field WITHOUT its own
structure-factor suppression. (b) The far-field correspondence q ↔ ħc/r
(PIN-Q5b-1): robustness was shown across r = R_s down to 3 fm with 12+
orders of margin, and sub-3-fm contact scattering was argued to BE the
coat floor, already counted. Attack the correspondence and the
no-crack-between-regimes argument. (c) The generous ceiling: is
g²_env = N²·E_C·R_s a true upper bound on the unprotected pair coupling,
or can you name registered structure exceeding it? (d) PIN-Q5a-1: FL is
the ROD-measured coat floor; the ring factor is untraced O(1)–O(few) and
the verdict was claimed robust to ANY such rescaling (shortfall ×27–×90
at floor level). Name any mechanism making a ring coat ×27+ LARGER than a
rod coat. (e) Is there ANY registered attraction channel at dwarf
momentum transfers that the analysis misses? (The gapless |SSV|
dissipation channel was recorded as adjacent fact, NOT consumed — its
coupling is unregistered per OPEN-DM-CAPTURE-1; consuming it would violate
the no-dark-sector-freedom rule 0865.)

**V3 — the shape-closure finding (new, and consequential for ANY
successor).** The central audited frame admits NO passing g² for
monodisperse {8} at any coupling on [10⁻⁸, 10⁶] (best viol 1.80): the
[10,100]@30 / [1,5]@50 / [0.7,2.5]@200 windows cannot be jointly satisfied
by the single-species σ(v) shape the committed F-table machinery produces
at this mass. Verify from the machinery, or name the error. If VERIFIED,
note the consequence you read: even a future attraction channel at the
right STRENGTH would still need composition or shape freedom to pass
central — this constrains avenue (C) below.

## PART II — OPEN IDEAS CHANNEL (findings-only; ranked; no grades)

**The candidate's state, honestly:** N = 8 (11.26 GeV) is the programme's
first zero-parameter species to clear the FULL published direct-detection
ladder unconditionally (LZ ×32 inside at the superseding strict point;
DAMIC by orders; XQC ρ* ≥ 1 at the island floor) — and it is now
corridor-dead for the coring claim, by its own completed derivation: the
(N−1)-order protection that hides it from detectors is channel-blind and
removes its grip on other rings. What died is the CORING mechanism, not
the species' experimental viability.

**Three avenues are on the worker's list — attack, extend, or re-rank
them, and name any avenue NOT listed:**

- **(A) The |SSV| dissipation route.** OPEN-DM-CAPTURE-1 (a prior panel
  product) left exactly one dissipation candidate: the gapless |SSV| mode,
  coupling UNREGISTERED. If derived, dwarf-core dynamics could come from
  capture-aggregation + gravothermal physics (the DM-4 Stage-0(ii)
  convergence) rather than elastic σ_T — a mechanism the defect protection
  does not touch. Name the cheapest kill for this route before it is
  funded.
- **(B) CDM-like successor registration, no coring claim.** Keep N = 8 as
  an experimentally-clean 11.26-GeV relic candidate; dwarf cores revert to
  non-DM explanations. The named concern: falsifier poverty — the defect
  coupling likely sits below the neutrino fog, pushing falsifiability to
  the formation/relic-abundance lane. Opine: is a hard-to-kill candidate
  worth registering under this programme's swarm-validation epistemics,
  and what falsifiers would you attach?
- **(C) Polydisperse carrier admixture.** The 2383 passers were
  multi-species; open chains are NOT defect-protected and could carry the
  coring coupling. The binding constraint: the 2382 kinetic cascade is
  what selected rings — a surviving open-chain fraction must be DERIVED
  from the same cascade, not asserted (0865), and V3's shape-closure
  finding constrains what compositions can pass central at all.

**Deliverable for Part II:** ≤ 3 ranked findings per panelist (avenue
rankings with reasons; kills-in-waiting; unlisted avenues; falsifier
proposals for (B)).

## Rules of the round

- REFUTED on V1 or V2 HALTS the successor decision; the round completes on
  the corrected number and the grading re-fires mechanically on it.
  REFUTED on V3 narrows only the successor constraints, not the kill.
- V1–V3 VERIFIED = the terminal grading is adjudication-ready; the founder
  decides the successor direction on your Part II returns.
- **Deliverable per panelist:** three grades (V1–V3) + Part II ranked
  findings (≤ 3) + re-ran-vs-audited disclosure (state plainly whether you
  executed code or audited it).
- **Seats:** five (labels assigned by the founder in a one-line paste
  preamble — the 2385 label-collision lesson; each return must OPEN with
  the seat label it was given; self-IDs are claims, the founder's mapping
  governs). Copilot seat: full content pasted per the standing 2378 fix,
  AND the raw links above provided for direct retrieval.

## NO VERDICT MOVED. The grading stands recorded at §34.22; the founder's adjudication block opens when the returns land.
