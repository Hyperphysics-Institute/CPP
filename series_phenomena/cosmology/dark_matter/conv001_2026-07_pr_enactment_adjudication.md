# CONV-001 PR ENACTMENT — ADJUDICATION (Patch 2829)

**Five returns, complete roster. UNANIMOUS 5–0 ON ALL FIVE QUESTIONS.
Execution integrity: 5/5 REASONED-UNVERIFIED, ZERO fabrications —
the SECOND consecutive clean round under the withheld-challenge-key
protocol.**

| Q | S1 | S2 | S3 | S4 | S5 | Disposition |
|---|---|---|---|---|---|---|
| E1 PR3 | UPHOLD | YES | UPHOLD | UPHOLD | UPHOLD | **PR3 MET 5–0** |
| E2 PR5 | AMEND(rider) | YES | UPHOLD | UPHOLD | UPHOLD | **PR5 MET 5–0; worker objection OVERRULED 5–0** |
| E3 PR6 | UPHOLD | YES | UPHOLD | UPHOLD | UPHOLD | **PR6 MET 5–0** |
| E4 PR4-BARE | UPHOLD-AMD | YES | UPHOLD | UPHOLD | UPHOLD | **ARTIFACT ACCEPTED 5–0** |
| E5 PR7 | UPHOLD | YES | UPHOLD | UPHOLD | UPHOLD | **PARTIAL SUSTAINED 5–0** |

## E1 — PR3 MET (adopted wording, S1)

> **PR3 MET.** A preregistered founder-run response experiment
> measured fluctuation-response concordance at two decisive shells,
> with linearity, undriven-control, and power gates passed. A
> factor-of-two observable-label defect was corrected from the
> unchanged archived time series. The verdict does not depend on the
> marginal n²=1 cell.

**S1's four acceptance conditions — ENACTED THIS PATCH:** (1) the
measured observable is now defined before the susceptibility equation
and (2) the factor-of-two relation derived explicitly — both added as
a header block to the runner (`code/2829_pr3r2_founder_run_v2c.py`)
and restated in the execution record; (4) the erroneous label is
removed from the script's report line, which now reads
`UNPERT <(Re rho)^2>` with the relation stated inline. **Condition
(3) — "regenerate every Λ from the archived time series" — is
PARTIALLY met and the shortfall is disclosed:** the founder returned
the bootstrap block summary, not the raw per-sample series, which
were not committed. Every Λ was regenerated from those committed
block means and bootstrap errors, not from raw samples. **A seat
wishing full condition-3 compliance should say so and the founder can
return the series.**

**S1's caution ADOPTED:** the slow-mode diagnosis explains 2822's
failure but **does not retroactively convert that run into
evidence** — 2820 stands UNRESOLVED and 2822 stands VOID, as
recorded.

## E2 — PR5 MET; the worker's objection OVERRULED 5–0

All five seats declined to sustain the worker's own procedural
objection. **S1's reasoning adopted:** preregistration protects
against adapting methods to observed data, and the material tests are
whether estimators and inclusion rules were frozen before the
results, whether all rungs were reported, and whether the imported
evidence tests PR5's proposition — all satisfied. **A PR5-labelled
prereg re-running the same frozen estimators on the same data would
add no protection.** (S3: "formalism over substance"; S5: "penalising
the result for a label when the methodology is sound would be
bureaucratic, not scientific.")

**S1's necessary qualification ADOPTED VERBATIM as the enactment
wording, and it constrains all downstream citation:**

> **PR5 MET by incorporated preregistered evidence.** Independent
> extraction representations are mutually compatible within their
> declared total uncertainties and identify the same near-DH
> monotonic screening mode. **It may NOT be said that the routes
> agree at the 0.5% level** — that validation gate failed and remains
> FAIL. The historical 0.5% gate is not part of the passing claim.

## E3 — PR6 MET (adopted wording, S1)

> **PR6 MET.** Continuum asymptotics, measured external-field
> response, and explicit Moment-rule simulations independently
> support one monotonic near-DH screened mode. The 0.091 fm proxy
> remains a separately labelled discretization diagnostic.

S1's standing note adopted: the three representations need not agree
on finite-distance estimators, only on the physical class — monotonic
screened mode, no robust staggered alternation, asymptotic screening
near the DH scale. The ℓ_proxy separation remains explicit.

## E4 — PR4-BARE artifact ACCEPTED (adopted wording, S1)

> **PR4-BARE MET-NEGATIVE.** A submittable analytic and computational
> artifact finds strong nonconservation for six physically motivated
> candidate energies across four geometries, with no specified
> alternative conserved energy, bath coupling, or detailed-balance
> mechanism. Therefore the bare rule does not presently license a
> Gibbsian marginal or thermodynamic density inference. This does not
> prove the nonexistence of every possible invariant.
> **OPEN-PR4-C23C24 remains binding for the completed rule.**

S1's direction adopted: the failed H-CONTRACT and H-FINITE hypotheses
**remain in the artifact**, because their disclosure demonstrates the
conclusion was narrowed rather than protected from falsification.

## E5 — PR7 PARTIAL SUSTAINED 5–0

Clause 1 **MET**; clause 2 **UNVERIFIED**. S1's specification of what
closing clause 2 requires is adopted as the standing target: a defined
R1 memory kernel or correlation function; evaluation at the physical
d_DP; a preregistered "subdominant" threshold; uncertainty and
finite-size controls; and separation from the short-range transient
and regulator effects. **Neither monotonic screening nor the PR3
bridge establishes this automatically.** (S3: "the worker's refusal to
read clause 2 generously in service of a milestone is exactly the
adversarial rigor this panel relies upon.")

## THE PROMOTION LEDGER, ENACTED

| PR | Status |
|---|---|
| PR1 | **MET** / retired resolved-systematic |
| PR2 | **MET** |
| PR3 | **MET** |
| PR4-BARE | **MET-NEGATIVE** (artifact accepted) |
| PR4-COMPLETED | **OPEN-PR4-C23C24** |
| PR5 | **MET** (incorporated evidence; 0.5% gate excluded from the claim) |
| PR6 | **MET** |
| PR7 | **PARTIAL** — clause 1 MET, clause 2 UNVERIFIED |

**SIX OF SEVEN PROMOTION REQUIREMENTS ARE MET.** The sole substantive
promotion gap is **PR7 clause 2: a bound on the R1 memory kernel at
the d_DP scale**, to S1's five-part specification above. **Founder
decision B7 continues to hold DM-1/2/3; nothing in this adjudication
moves a banner.**

## Execution-integrity

All five seats declared REASONED-UNVERIFIED and none reported a
challenge value. **Second consecutive round with zero fabrication
events.** S2 noted usefully that the packet did not carry the four
driven amplitudes needed to recompute the key — **a worker-side
lesson: a withheld key must remain computable from committed
artifacts, and the packet should name where those live.** Future
dispatches will cite the file path alongside the challenge.
