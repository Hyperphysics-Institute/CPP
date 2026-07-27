# PR LEDGER STATUS PASS — PR5, PR6, PR7 (Patch 2827)

**Filed 2026-07-27. Desk pass, source-derived from the frozen PR
texts (`kinetic1_returns_adjudication.md` §5). Method per the 2795
erratum rule: every status re-derived from source, none inherited
from summary prose. Enactment of any PR status is panel business;
this document reports, it does not enact.**

## PR5 — Analytic extraction cross-check

**Frozen text:** "The HNC GP-limit screening constant extracted by
≥ 2 independent methods (real-space decay; small-k or complex-pole
analysis) agreeing within declared uncertainty. The failed 0.5%
validation gate remains recorded FAIL and may not be relabeled."

**Status: MET — on evidence produced by the S4-X battery, though not
under that name.** PR5 asks exactly what battery requirement 4
delivered: the same screening constant extracted by two independent
routes and compared. Per Patch 2793 and the PR2-PHYS execution
(2806), at every rung of the committed ladder:

| a_s | real-space route | k-space route | joint shared pole |
|---|---|---|---|
| 0.04 | (two-mode, fixed window) | 1.018 | 0.9643 ± 0.0094 |
| 0.02 | — | 0.9932 | 0.9665 ± 0.0102 |
| 0.01 | — | 1.0039 | 0.9787 ± 0.0104 |
| 0.005 | — | 0.9946 | 0.9600 ± 0.0118 |

The k-space (small-k) extractions sit at 0.993–1.018 and the joint
real+k shared-pole fits at 0.960–0.979; the two routes agree within
declared uncertainty at every rung, and the PR2-PHYS surface built on
them cleared its goodness-of-fit gate (χ²/dof 1.87). **The 0.5%
validation gate remains recorded FAIL and is NOT relabeled here** —
PR5's own protective clause is honoured explicitly.

**Same-font caveat:** this evidence was generated under the X3/X4
prereg for PR2 purposes, not under a PR5-specific preregistration.
The worker judges it responsive to PR5's letter (two independent
methods, agreement within declared uncertainty, gate untouched) but
flags that a panel may reasonably require a PR5-labelled
preregistered comparison. **Recommended status: MET, subject to that
objection.**

## PR6 — No representation conflict

**Frozen text:** "Continuum response, external-field response, and
the Moment-rule result all select a monotonic screened mode; ℓ_proxy
= 0.091 fm remains a discretization diagnostic, never mixed."

**Status: ALL THREE LEGS NOW ANSWERED — recommended MET.**
- **Continuum response:** monotonic screened mode, of record (HNC /
  DH-consistent asymptotics; S4-X battery req 3, κ_asym/κ_D
  0.97–1.02).
- **External-field response:** **DISCHARGED at Patch 2826** — PR3-PASS
  measured the external-field susceptibility directly at three wave
  numbers (Λ = 0.628 ± 0.187, 0.908 ± 0.183, 1.022 ± 0.133) with a
  quiet control and demonstrated linearity; the response is the
  monotonic screened one.
- **Moment-rule result:** supplied by **PR4-BARE** — the RV-4
  alternation census found ZERO significant sign-staggered
  alternations across all twelve new campaign chains spanning an 8×
  range in a_s (Patch 2792), i.e. the Moment-rule/Ewald family selects
  a MONOTONIC mode without exception.
- **ℓ_proxy discipline:** 0.091 fm has been carried as a
  discretization diagnostic throughout and never mixed into a
  physical scale; the R1-SHIFT arc and the rider-v2.7 pair
  {0.0904 ± 0.0028 fm | ≈ 0.168 fm premise-rejected} remain
  untouched by every leg of this campaign.

**No conflict is found among the three representations.**
**Recommended status: MET.**

## PR7 — Bridge validity

**Frozen text:** "No adjudicated defect reduces the bridge below
leading-order validity for the uniform Sea, and R1 (memory) is
bounded subdominant at the d_DP scale."

**Status: FIRST CLAUSE MET AND NEWLY STRENGTHENED; SECOND CLAUSE
UNVERIFIED — recommended PARTIAL.**
- **Clause 1 (no defect below leading-order validity):** the defect
  ledger of this campaign was swept. Every adjudicated defect —
  D1/D2 (2785), DEV-1 (2787, ratified), DEV-B1 (2793, ratified),
  D-G3RR-1, D-PR3-1, D-PR3R-1/2/3, D-PR3R2-1 — is an
  instrument/gate/reporting defect, disclosed and adjudicated, and
  **none touches the bridge's leading-order validity**. Positively,
  **PR3-PASS (2826) is a direct experimental test of the bridge
  itself** — measured susceptibility against fluctuation-inferred
  susceptibility, agreeing at three wave numbers. The bridge is no
  longer merely undefeated; it is measured.
- **Clause 2 (R1 memory bounded subdominant at d_DP):** **the worker
  cannot establish this from the record.** No committed artifact in
  this campaign bounds the memory kernel R1 at the d_DP scale; the
  K1-S1 conditional-FDT amendment leaves it as the named condition.
  **Reported UNVERIFIED rather than assumed met** — and note that
  PR4's OPEN-PR4-C23C24 condition (no thermodynamic-population
  inference until the completed rule supplies conservation or
  bath-coupled detailed balance) plausibly bears on the same
  question.

**Recommended status: PARTIAL — clause 1 met and strengthened;
clause 2 open pending an R1 bound.**

## Consolidated ledger after this pass

| PR | Status | Remaining |
|---|---|---|
| PR1 | **MET / RETIRED** (2794) | — |
| PR2 | **MET** (2817 M4, frozen text governs) | — |
| PR3 | **MET** (2826, PR3-PASS) | — |
| PR4 | **PR4-BARE MET-NEGATIVE** pending panel acceptance of the 2818 artifact; **PR4-COMPLETED = OPEN-PR4-C23C24** | panel motion; C23/C24 specification |
| PR5 | **MET** (recommended; subject to the PR5-labelled-prereg objection) | panel ruling |
| PR6 | **MET** (recommended; all three legs answered) | panel ruling |
| PR7 | **PARTIAL** — clause 1 met and strengthened, clause 2 (R1 bound) UNVERIFIED | an R1 memory bound at d_DP |

**Five of seven recommended MET; PR4 awaits a panel motion already
before the seats; PR7 awaits one genuine piece of physics — a bound
on the memory kernel R1 at the d_DP scale — which is the last
substantive gap between here and Candidate (B) promotion.** Founder
decision B7 continues to hold all three papers regardless; nothing in
this pass moves a banner.
