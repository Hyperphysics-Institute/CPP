# SS-7 v1.2 — Revision Plan

**Status:** Draft plan, execution contingent on reviewer verification of the N=Z alpha-chain finding (see `SS-7_v1.2_reviewer_verification_letter.md`)

**Purpose:** Combine two v1.1-era findings that accumulated after v1.1 shipped:

1. **G3 discrepancy** — Paper cites RMS 0.88%; first-principles computation gives 0.91% (all 8 nuclei) or 0.86% (excluding ²⁰Ne). Registered in `SS-7_v1.1_G3_discrepancy_note.md`, 20 April 2026. Severity: minor, no individual prediction affected.

2. **Table 1 isotope-choice error at N_α ≥ 12** — The paper's structural-onset anchor (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) uses non-N=Z isotopes with +4 neutron excess each. The strict N=Z alpha-chain (⁴⁸Cr, ⁵²Fe, ⁵⁶Ni) residuals stay in family with the primary set (+0.40% to +0.73%). Surfaced during SS-8 Phase 1, 21 April 2026. Severity: significant — likely invalidates OPEN-SS-22 as currently framed.

**Date range of v1.2 work:** depends on reviewer turnaround; target ~1 week after verification letters sent.

---

## Decision tree — depends on reviewer response to Task 3

### Branch A: reviewers confirm interpretation (a) — isotope-choice artifact, no principled reason for ΔN = +4

**v1.2 scope under Branch A:**

#### A.1 Abstract (§1 of .tex)
- "RMS error 0.88%" → "RMS error 0.91% (0.86% excluding ²⁰Ne; see §5.3)"
  *Alternative phrasing for brevity:* "RMS error ≈ 0.9%"
- Remove or soften the reference to "heavy-nuclei structural onset at N_α = 12" if it appears in abstract
- Confirm: the abstract's headline claim about 8 concurrent predictions at ±1.5% is unchanged

#### A.2 Table 1 (§3.1, .tex lines ~760-782)
- **Replace** the three paper-choice rows (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) with the strict N=Z alpha-chain rows (⁴⁸Cr, ⁵²Fe, ⁵⁶Ni)
- **Retire** the `(not N=Z)` annotation on what was line 777 — ⁴⁸Cr becomes the primary entry, not the dashed-out one
- **Extend**, optionally, to include ⁴⁴Ti (N_α=11), which is actually within the paper's primary-set claim of N_α = 3-10 plus adjacent. ⁴⁴Ti at +0.26% is a clean data point that strengthens the case.
- **Optional addendum row/table**: "Non-N=Z counterparts for reference" with ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe residuals — showing the +2% pattern — labeled as the neutron-excess signal that SS-7 does *not* address.

#### A.3 §5.1 "Heavy nuclei: OPEN-SS-22" (.tex lines ~785-790)
- Rewrite the "Trend shape" paragraph (lines 785): the flat −2 to −2.5% pattern in ⁴⁸Ti/⁵²Cr/⁵⁶Fe is not a structural onset at all; it is a consistent +4-neutron excess binding, roughly 2 MeV/neutron, that the SS-7 formula does not model.
- Rewrite "Why N_α = 12 is the natural threshold" (lines 787): the icosahedral-closure argument no longer has empirical anchor. Move this passage to §6 (Discussion) as speculative future work rather than as current active hypothesis.
- Rewrite "Candidate mechanisms ranked by plausibility" (line 789): list is no longer ranked against an empirical pattern; reframe as motivation for possible future SS-9+ work, not as an open problem with data anchor.

#### A.4 OPEN-SS-22 registration (research_frontier.md, predictions.md, paper_catalog.md, phenomena-SS-7.md)
- **Retire** OPEN-SS-22 in its current form.
- Registry slot OPEN-SS-22 can either:
  - **(a.i) Be recycled** for the correct empirical question: "neutron-excess contribution to binding energy in non-N=Z nuclei" (this is currently OPEN-SS-23 territory, so retiring one and splitting the other may be cleaner).
  - **(a.ii) Be retired** and the slot left vacant. New open problem registered as OPEN-SS-2X for the neutron-excess extension.
- **Recommendation:** (a.ii). Retiring an open problem honestly is cleaner than quietly recycling its identifier. `problem_histories/PH-OPEN-SS-22.md` documents the retirement with the programme-integrity narrative.

#### A.5 Figure 3 (scatter plot, .tex line ~685-710)
- Regenerate with correct N=Z alpha-chain at N_α ≥ 11. The "red squares beyond domain" and the "structural onset signature" visual features go away.
- Caption rewrite: remove "icosahedral closure at N_α = 12" motivation.
- Optional: add a second panel showing the +4-neutron isotope pattern as a separate data signal, properly labeled as neutron-excess contribution (future-work flag).

#### A.6 §7.5 adversarial stress test
- Re-evaluate: the stress test was run against ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca — these are all in the primary set and unaffected by the finding. Stress test itself remains valid.
- Confirm no ⁴⁸Ti/⁵²Cr/⁵⁶Fe dependency in stress-test conclusion.

#### A.7 §6 falsifiability inventory
- The ±2% structural falsification threshold was set to exceed the residual band by a factor. This stands unchanged; the threshold argument was independent of the N_α ≥ 12 data.
- Remove any references to ⁴⁸Ti/⁵²Cr/⁵⁶Fe as "falsification-adjacent" or "near threshold."

#### A.8 CHANGELOG (.tex header)
Add v1.2 entry summarizing:
```
v1.2 (date TBD): Correct Table 1 isotope choice for N_α = 12, 13, 14
(48Cr, 52Fe, 56Ni instead of 48Ti, 52Cr, 56Fe); the original choice
conflated neutron-excess binding with a hypothesized icosahedral-closure
signal. Retire OPEN-SS-22 in its current form; the heavy-nuclei residual
pattern that motivated it was an isotope-choice artifact. Update RMS
citation to 0.91% (all 8 nuclei, all N=Z). Finding surfaced during
SS-8 Phase 1 exploration, verified independently by ChatGPT and Copilot
on [date], filed under programme symmetric-honesty protocol.
```

### Branch B: reviewers identify a principled reason for the non-N=Z choice

Less likely but possible. v1.2 under Branch B is more limited:

#### B.1 Abstract & §5.1: keep the ΔN = +4 data, but explicitly state why
- Add an explicit paragraph in §5.1 (or a new §5.1.1) specifying the principle — e.g., "these are the most-stable isotopes because the N=Z alpha-chain above N_α = 10 becomes unstable due to Coulomb barrier crossing; AME values for ⁴⁸Cr, ⁵²Fe, ⁵⁶Ni are short-lived-state measurements and [specified reason for preferring the stable isotopes]."
- Retain Table 1 as-is (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) BUT add the line-777 correction on ⁴⁸Cr.
- OPEN-SS-22 survives but with a more careful statement about which data it predicts.

#### B.2 G3 RMS fix (as in Branch A)
- Still needed; independent of the Task 3 outcome.

#### B.3 CHANGELOG
```
v1.2 (date TBD): Correct line-777 Table 1 data error on 48Cr (AME 2020
binding energy is 411.462 MeV, not "---"; 48Cr IS N=Z). Clarify §5.1
rationale for including +4-neutron isotopes at N_α = 12, 13, 14
[specified reason per reviewers]. Update RMS citation to 0.91% per
G3 discrepancy note.
```

---

## Companion-documentation updates for v1.2

Following `paper_completion_checklist.md` (the new authoritative checklist — SS-7 v1.2 will be its first validation test):

- **Section A (companion suite):** update each of the 7 companion files:
  - `mechanism-SS-7.md` — update correspondence table if §5.1 mechanism description changes
  - `glossary-SS-7.md` — no change expected
  - `phenomena-SS-7.md` — update PHEN-P (predictions) with corrected Table 1, update PHEN-V (consilience) if OPEN-SS-22 retired
  - `philosophy-SS-7.md` — update falsifiability inventory if affected
  - `development-SS-7.md` — add v1.2 development entry
  - `reviews-SS-7.md` — add Part 1 entries for the v1.2 verification letter + responses
  - `keywords-SS-7.md` — update registry entries (OPEN-SS-22 status change)

- **Section B (verification notebooks):** update `SS-7_alpha_cluster_edge_formula.py` to regenerate the corrected Table 1 values.

- **Section C (registry updates):** propagate OPEN-SS-22 status change to:
  - `research_frontier.md`
  - `predictions.md`
  - `paper_catalog.md` (v1.2 entry)
  - `problem_histories/PH-OPEN-SS-22.md` (new — retirement narrative under Branch A; update under Branch B)
  - `master_glossary.md` if neutron-excess terms introduced
  - `CPP_the_theory.md` if scorecard affected

- **Section D (navigation):** README.md paper count update if affected.

- **Section G (git commit/push).**

- **Section H (final verification):** reapply G3 to ensure the new Table 1 values match companion files.

---

## Open questions / sanity checks before starting v1.2 work

1. **Is there a principled reason SS-7 chose ⁴⁸Ti/⁵²Cr/⁵⁶Fe that we're missing?** Primary question in the verification letter. If yes, Branch B; if no, Branch A.

2. **Are there other paper passages that reference ⁴⁸Ti/⁵²Cr/⁵⁶Fe beyond Table 1 and §5.1?** Quick `grep` audit needed once Branch is chosen.

3. **Does the finding affect SS-5?** SS-5 handled ²H through ⁴He. The alpha-chain extension is entirely SS-7. SS-5 should be unaffected. Verify no cross-citations break.

4. **Does OPEN-SS-23 absorb the retired OPEN-SS-22 content, or does it remain distinct?** OPEN-SS-23 as currently registered is "odd-A and non-alpha-chain nuclei (⁶Li, ⁶He, ⁹Be, ¹¹B, ...)". The ΔN = +4 even-even isotopes (⁴⁸Ti, ⁵²Cr, ⁵⁶Fe) are arguably a distinct sub-case. Possible clean split: OPEN-SS-23a (odd-A), OPEN-SS-23b (non-N=Z even-even). To decide during v1.2.

5. **Is this a v1.2 or a v2.0?** Rule of thumb: v1.2 for changes that don't alter the central formula or main claim; v2.0 for changes that do. The Table 1 correction is a v1.2 scope per this rule — formula is unchanged, primary 8-nucleus result is unchanged. If Branch A forces retirement of OPEN-SS-22 and a significant §5.1 rewrite, it's on the border; suggest v1.2 unless reviewers argue otherwise.

---

## What this v1.2 does NOT do

- Does not re-open the central Theorem 2.1 or the formula derivation.
- Does not re-open the primary 8-nucleus empirical claim (N_α = 3-10).
- Does not alter the ⁸Be in-formula derivation.
- Does not alter the §7.5 adversarial stress test (run on primary-set nuclei).
- Does not merge with unrelated revisions; G3 and the Table 1 fix are paired because they emerged from the same verification posture, not because they are substantively linked.

---

## Prep work Claude can do now, before reviewer responses arrive

1. Grep the `.tex` for all references to ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe (beyond line 777-780) to scope the rewrite precisely.
2. Draft the retirement narrative for `problem_histories/PH-OPEN-SS-22.md` under Branch A.
3. Re-run the verification notebook script with corrected AME values to confirm residual numbers.
4. Draft the replacement text for §5.1 under Branch A (can hold until reviewers respond, but pre-drafting accelerates the turnaround).

Claude can work on any or all of these while Thomas is waiting on reviewer responses. No commitment needed until the reviewers have weighed in.
