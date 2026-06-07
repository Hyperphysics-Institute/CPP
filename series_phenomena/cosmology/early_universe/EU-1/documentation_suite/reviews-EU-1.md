# Reviews — EU-1: The Primordial Scalar Spectral Index from Substrate Inflation

**Publication-facing review record.** The full working synthesis (verdict table, triage outcome
T1–T5, calibration disposition, close decision) lives in `../review/reviews-EU-1.md`; the
self-contained dispatch package is `../review/EU-1_review_package_v1.0.md`. This file is the polished
summary for authors and referees.

**Cycle:** one round, three independent reviewers (ChatGPT, Grok, Copilot). **Outcome: 3/3 SHIP, zero
verdict-flipping objections.** Numerics independently reproduced (Grok, Copilot) and SCRIPT-EXECUTED
(ChatGPT, Grok); all verification checks PASS. The convergent calibration (language-tightening, result
unchanged) was folded in at Patch 0783; v0.1 → v1.0.

## Review 1: ChatGPT — Mixed-positive (SHIP with calibration)
**Verdict:** advance to v1.0 (SHIP) with calibration edits, not a v1.1 restatement; the result holds at its claimed scope.
- Confirmed the A1 → indistinguishable-counting → $\mu \propto \ln\bar n$ spine is internally consistent and the strongest part of the paper; recomputed $n_s$, $\alpha_s$, and the ideal-ZRP slope (SCRIPT-EXECUTED).
- Pressed two points (non-flipping): (1) "uniquely selects the log" is *practical*-uniqueness, not theorem-level; (2) $N_* = 57$ is a *derived total ~60.5 + adopted pivot placement*, not a single locked prediction.
- Suggested "confirmed at leading order" → "derived at leading order" (handled as a maintainer wording decision at Patch 0785).

## Review 2: Grok — Positive (SHIP)
**Verdict:** SHIP / register; the zero-new-axiom claim clears the promotion bar.
- Full §7 verification script SCRIPT-EXECUTED — all checks PASS exactly (geometry, detailed-balance, Poisson limit, tilt coefficient, Debye scaling, $n_s$ coefficient-invariance).
- Independently recomputed the $\delta N$ tilt relation $n_s - 1 = 2\,d\ln H_{\text{eff}}/dN = -2/N_{\text{rem}}$ from first principles.
- Cross-checked LEMMA-NS-ZRP-DERIVE against its own earlier independent Monte-Carlo bath test (Poisson stationary + fast equilibration): fully consistent.

## Review 3: Copilot — Positive (SHIP, tighten language)
**Verdict:** SHIP; tighten the uniqueness and "entailed vs minimal" language before locking v1.0.
- Referee-grade per-question structural consistency T1–T5; H-theorem application correct; the A1 state-space restriction (distinguishable cliff excluded) judged conceptually sound.
- Flagged that ZRP properties (i)–(iii) are a *minimal leading-order reduction*, not strict entailment (assume no $O(1)$ occupancy-dependent microphysics beyond SSV).
- Found no verdict-flipping flaw in the ZRP identification or the A1→log spine.

## Critical Review: convergent objections — Detailed Response

### Objection 1: "the log is uniquely forced by near-scale-invariance"
**Response:** softened to "the unique robust candidate among the natural occupation laws surveyed — practical-uniqueness within minimal CPP assumptions, not theorem-level; RG/geometric/composite logs are unnatural but not formally excluded." (Applied, Patch 0783.)

### Objection 2: "$p = 2$ is forced by A1"
**Response:** restated as "forced within the A1→ZRP→$\delta N$ chain, given the linear coupling $H_{\text{eff}} \propto \mu$ and the spectator $\mathcal{P}_\zeta \propto H_{\text{eff}}^2$ — not by A1 in isolation." (Applied, Patch 0783.)

### Objection 3: "$N_* = 57$ is derived"
**Response:** the paper now separates the *derived* total $\approx 60.5$ (CP-count logarithm) from the *adopted* observable pivot $\approx 57$ (standard placement, consistency-level). (Applied, Patch 0783.)

### Objection 4: ZRP "is a" symmetric constant-rate process
**Response:** reframed as "reduces to … a minimal leading-order reduction" with the no-$O(1)$-microphysics assumption made explicit. (Applied, Patch 0783.)

## Summary

EU-1 passed first-round external review 3/3 SHIP with no verdict-flipping objection. The reviewers'
convergent point — and the paper's now-explicit posture — is that the remaining conditionality is
concentrated in *visible, framework-level commitments* (A1 occupation counting, the ZRP reduction,
cosmological homogeneity, neutrality) rather than hidden tuning. Registered as a leading-order,
framework-conditional zero-parameter prediction (PRED-C-96 + PRED-O-34); no THEO; not an
empirically-confirmed A1–A11 theorem.
