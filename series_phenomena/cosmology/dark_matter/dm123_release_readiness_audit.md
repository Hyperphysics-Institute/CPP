# DM-1/2/3 RELEASE-READINESS AUDIT (Patch 2814)

**Filed 2026-07-26. Method: every condition re-derived from its SOURCE
document (banners in the .tex files; `release_plan_2026-07-20.md`
founder decision B7; the frozen PR1–PR7 texts in
`kinetic1_returns_adjudication.md` §5), then checked against
post-S4-X/post-AUTOMATON state. No status inherited from summary
prose — the 2795 erratum's rule applied throughout.**

## §1 — What the banners actually say (source-derived)

- **DM-1** (v1.5, founder-attested Patch 2369): KILL RECORDED — both
  candidate branches dead (capture at the registered frame, 2333;
  population at the audited frames, 2369). Paper retained as record,
  **NOT-FOR-RELEASE, NOT rewritten**; revision deferred behind
  OPEN-DM-DSPH-1 by founder decision. Additionally "NOT YET
  RE-SHIPPED: panel round pending."
- **DM-3**: same founder-attested banner.
- **DM-2**: **carries NO banner.**
- **`release_plan_2026-07-20.md`**: CLOSED as a plan. **Founder
  decision B7 (Patch 2684): option (i) HOLD** — all three papers hold
  behind the Candidate (B) revision path; no standalone release, no
  record release.

**Correction to a working assumption (mine, same-font):** the banners
are NOT waiting on the S4-X screening question. They are waiting on
**a successor candidate reaching paper-revision maturity**. S4-X
closing and PR1 retiring do NOT by themselves move any banner. The
audit's hypothesis — "the banner conditions may have materially
changed" — is **only partly borne out**: what changed is the
*Candidate (B) promotion path*, which is the banners' upstream
dependency, not the banners themselves.

## §2 — The actual release chain

> banners → founder decision B7 (HOLD) → Candidate (B) revision path
> → **Candidate (B) promotion** → promotion requires **PR1–PR7 ALL
> evaluable and met** (frozen; amendable only by new panel motion)
> → revised DM-1/DM-3 → fresh panel round → fresh stability cycle
> → deposit.

**Therefore: PR1–PR7 is the gate. Everything else is downstream.**

## §3 — PR1–PR7 status, each re-derived against source

| PR | Requirement (frozen) | Status | What remains |
|---|---|---|---|
| **PR1** | Error closure: re-analyse all chains (IACT/ESS, covariance-aware, independent-chain), CLASSIFY the discrepancy; barred while unexplained > 2σ; monotonic character must survive | **MET / RETIRED** | Nothing. S4-X delivered ESS (242–740), 24×2000 covariance-aware bootstrap, independent-chain variation (X3 REPLICATED); the discrepancy is CLASSIFIED (extraction/window systematic, adopted 5–0 at 2794 P1); PR1 formally retired resolved-systematic (P3, 5–0); monotonic character confirmed at Ewald grade over an 8× a_s range (zero alternations, 12 chains) |
| **PR2** | GP-limit ladder; joint (a_s, 1/L) extrapolation giving κ_eff/κ_D **consistent with 1 within total uncertainty ≤ 3%**; no staggering | **BLOCKED — but see the flagged ambiguity** | PR2-FROZEN FAIL stands as-letter (permanent). PR2-PHYS successor: κ_eff/κ_D = 1.0349 ± 0.0194, GOF MET, staggering clause met. Statistics extension DIRECTED 3–2 (2813). **AMBIGUITY FLAGGED FOR THE PANEL, NOT RESOLVED HERE:** PR2's own frozen text requires "consistent with 1 within total uncertainty ≤ 3%" — the successor result IS consistent with 1 (1.8σ) with total uncertainty 1.94% ≤ 3%. The [0.97, 1.03] **band was a worker operationalization in the 2795 prereg, STRICTER than PR2's text.** The worker will not re-score its own gate after seeing data; the panel must rule which reading governs |
| **PR3** | Independent susceptibility: external charge potential at ≥ 3 small wave numbers; measured χ(k,0) vs S_zz-inferred, testing the fluctuation-response bridge | **PARTIAL** | The instrument verdict was contaminated-withdrawn; the clean N = 80 linear-response pass (0.3σ) is **partial evidence only**. The full ≥3-wave-number external-field measurement has never been run on clean chains. **EXECUTABLE NOW** — same machinery as the X4 campaign, no new physics decisions |
| **PR4** | Kinetic-measure discriminator: a registered Moment-rule automaton **— or an analytically equivalent derivation from the explicit Moment transition law —** demonstrating the stationary marginal is energy-only and Gibbsian; Metropolis/HNC concordance cannot substitute | **NOT MET — THE HARD BLOCKER** | AUTOMATON-1 returned NOT-GIBBS (3/3 R). AUTOMATON-2's arc CLOSED at the FEM boundary; limitation **L-2 explicitly bars** citing its Maxwell–Boltzmann result for PR4. **The automaton route is closed at hostable scale.** **BUT — the finding of this audit — PR4 WAS NEVER AUTOMATON-ONLY.** Its frozen text permits *"an analytically equivalent derivation from the explicit Moment transition law."* **That route has never been attempted.** It is an analysis task, not a compute task, and it is the single unexplored path past the release chain's hard blocker |
| **PR5** | Analytic extraction cross-check: HNC GP-limit constant by ≥ 2 independent methods agreeing; the failed 0.5% gate stays FAIL | **STATUS PASS NEEDED** | The X6 re-read predates the 2714 defect; the clean-data restatement was never formally scored against PR5's text. Cheap desk task |
| **PR6** | No representation conflict: continuum response, external-field response, AND the Moment-rule result all select a monotonic screened mode | **PARTIAL — coupled to PR3 + PR4** | Continuum + Ewald legs: monotonic, confirmed. External-field leg: awaits PR3. Moment-rule leg: awaits PR4 |
| **PR7** | Bridge validity: no adjudicated defect below leading-order validity; R1 (memory) bounded subdominant at d_DP | **STATUS PASS NEEDED** | No current status established in the audited records; requires a defect-ledger sweep against the K1-S1 conditional-FDT amendment |

## §4 — Findings

1. **The release is no longer blocked by the screening question.** PR1
   is met and retired; the anomaly that consumed the last campaign is
   resolved as systematic. That is real progress toward the prime
   goal.
2. **The release IS blocked by PR4**, and the automaton route to PR4
   is now bounded by the FEM limit established at arc closure.
3. **PR4's frozen text contains an unexplored second route** — an
   analytic derivation of the stationary measure from the Moment
   transition law. This is the audit's most consequential finding:
   the hard blocker has a door nobody has tried.
4. **Three items are cheap and executable now:** PR3 (external-field
   χ — real compute, existing machinery), PR2 (directed statistics
   extension), PR5/PR7 (desk status passes).
5. **Even with all seven met, release is not immediate:** the chain
   still requires Candidate (B) promotion enactment, a revised
   DM-1/DM-3 (the 2683 revision checklist + errata items 1–9), a
   fresh panel round, and a fresh stability cycle. **Founder decision
   B7 remains in force and only the founder can lift it.**

## §5 — Recommended sequence (worker recommendation; founder rules)

1. **PR4 analytic route — scoping pass first.** Determine whether the
   Moment transition law admits a tractable stationary-measure
   analysis (detailed balance / current-free conditions on the
   deterministic map). Cheap to scope, decisive either way: if
   tractable, the hard blocker opens; if provably intractable, that
   is itself a finding the panel must weigh against PR4's letter.
2. **PR3 external-field susceptibility** — executable now, and it is
   also PR6's missing leg.
3. **PR2 statistics extension** — directed, pure compute; and the
   panel must rule the §3 ambiguity (PR2's text vs the successor's
   band) regardless of the extension's outcome.
4. **PR5 + PR7 status passes** — desk work, may close cheaply.
5. Only then: the v3 enactment adjudication, revision, panel round,
   stability cycle, deposit.
