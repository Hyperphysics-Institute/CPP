# CONV-001 ROUND 2384 — RETURNS + ADJUDICATION (Patch 2385, 9 July 2026)

**Round:** combined verification + ratification on the 2381–2383 derived-nucleation arc
(brief: `conv001_2026-07_arc2381_2383_verification_brief.md`).
**Status: 2 substantive returns of 5 seats.** Adjudication block OPEN below.

## 1. Seat status (founder-relayed causes)

| Window (founder relay) | Return | Cause / note |
|---|---|---|
| GPT | **Return A** (attached document) | complete deliverable |
| Grok | none | "could not reply, disconnected" |
| Gemini | **Return B** (pasted inline) | complete deliverable |
| Copilot | none | "could not reply, rules for retrieval" — BOTH delivery paths failed this round: no return on the pasted-content route, and the raw-link route blocked by the seat's own retrieval rules. The 2378 A2 fix is NOT sufficient for this seat; standing exposure recorded. |
| DeepSeek | none at collection | relay line empty — possibly pending; adjudication item D1 |

**Seat mapping (2363: self-IDs are claims, founder mapping governs).** BOTH returns open
with the label "R1" — a **LABEL COLLISION**, documented: the paste evidently did not
prepend distinct seat labels, and both models defaulted to the brief's own example label.
This is NOT a 2378-A1-type anomaly: the two returns are textually distinct in structure,
phrasing, and findings throughout. **Protocol note for future rounds:** the founder
assigns the label in a one-line paste preamble ("You are seat Rn"), not inside the shared
block. Recommendation only; no template edit this patch.

## 2. Deliverable-completeness grading

Both returns are COMPLETE per the round spec: five grades + R1 vote + R2 opinion +
≤2 ranked findings + re-ran-vs-audited disclosure. Both disclose **audited, not re-ran** —
acceptable per the deliverable; noted that NO seat re-executed the code this round (the
exit-coded batteries and the in-repo regression chain are the only executed verification;
this is recorded, not hidden).

## 3. Tally

| Item | Return A | Return B | Tally |
|---|---|---|---|
| V1 stability floor | VERIFIED | VERIFIED | 2× VERIFIED |
| V2 cascade + r³ | VERIFIED | VERIFIED | 2× VERIFIED |
| V3 XQC integrity | VERIFIED | VERIFIED | 2× VERIFIED |
| V4 anchor + amendments | VERIFIED | VERIFIED | 2× VERIFIED |
| V5 sign + composition | VERIFIED | VERIFIED | 2× VERIFIED |
| R1 (2380 B2 addendum) | RATIFY | RATIFY | 2× RATIFY, 0 objections |
| R2 (Clause 1(d)) | add new condition, retain original | add new condition | CONVERGENT |

**Halting rules: none triggered.** Zero REFUTED, zero INDETERMINATE across both returns.

## 4. Findings triage (executed actions marked)

**F-A1 (Return A, rank 1, "WOUND"):** the load-bearing assumption is no longer the
cascade algebra — it is the identification of κ and E_bond as genuine
temperature-independent substrate constants; elevate from inherited convention to
explicit theorem if possible. **ACTION EXECUTED this patch:** the
**SUBSTRATE-CONSTANCY THEOREM DEMAND** is appended (dated, additive) to the arc doc's
Q3c inherited-target list — κ(T), E_bond(T) constancy or bounded drift, to be
discharged inside the same SSV/OPEN-FP-SF-2-η work that owes the absolute pair.

**F-A2 (Return A, rank 2, "SCRATCH"):** keep every occurrence of the attractive-default
explicitly tagged as ARGUMENT-LEVEL extraction pending OPEN-SS-43. **ACTION EXECUTED
this patch:** dated additive tag line appended to arc doc §Q3b-2c's sign paragraph;
original text untouched.

**Return B findings (rank 1: the epoch-free N_stab; rank 2: the sign-tension
resolution):** commendations; no action.

## 5. R2 draft for founder attestation (NOT applied by this patch; add-only rule)

> **(d′) [ADDED ____, panel-recommended (2384 round, 2 seats convergent),
> founder-attested: ____]:** a direct-detection null at the derived ring-population
> mass scale — dominant species ≈ 8.45 GeV (N = 6), companions ≈ 7.04 / 9.86 GeV — at
> the floor coupling (S_c ≈ 0.012) and the abundance the derived family requires,
> effective as an exit condition once the derived family is registered as the successor
> branch. The original (d) is retained verbatim for provenance; against the dead dimer
> branch it reads through as vacuous.

Attestation is the founder's alone: attest verbatim, edit, or decline.

## 6. ADJUDICATION BLOCK — OPEN (founder's entries required)

**D1 — round closure.** Close at 2/5 (convergent VERIFIED, zero refutations; coverage
caveat recorded) OR hold one collection window for DeepSeek + one Grok reconnect
attempt. *Worker recommendation:* one retry window is cheap; if nothing lands, close at
2/5 — the halting rules trigger only on REFUTED, and the arc remains candidate-grade
until Q3c pays rent regardless. Any REGISTRY-grade move (registering the derived family
as the successor branch) may be held to fuller coverage at the founder's discretion.
**D2 — if closed on this tally:** the arc is adjudicated **PANEL-VERIFIED
(2-seat coverage, convergent, zero refutations)** and Q3c OPENS on the inherited
target (r ≈ 8.5–12; N_stab ≈ 3.3–7.3; S_c at the island floor; R_s ≈ 20–50 fm;
Λ thresholds; 8.45 GeV dominant; + the F-A1 substrate-constancy theorem demand;
sign status ARGUMENT-LEVEL per F-A2).
**D3 — R1 ratification effective?** 2× RATIFY, 0 objections; the 2380(B2) flag is
discharged on the founder's confirmation.
**D4 — R2 attestation** on the drafted (d′) above.

**NO VERDICT MOVED** pending the founder's D1–D4 entries.

---

## APPENDIX — VERBATIM RETURNS (founder-relayed)

### Return A (attached document; self-claimed label "R1"; window: GPT per relay)

**Seat label:** **R1** (using the seat label assigned in your prompt)

**Disclosure:** **Audited, not re-ran.** I reviewed the supplied package and the inline
record. I did not execute the repository code. My review is therefore limited to
consistency, derivational logic, numerical plausibility, and whether the stated
conclusions follow from the reported computations.

#### Part I — Verification

**V1 — Epoch-free stability floor — Verdict: VERIFIED**

The cancellation argument is internally consistent:

- ℓ_p = κ/kT
- ε = E_bond/kT

therefore N_stab = c·r/ε = c·κ/(ℓ_rung·E_bond) is temperature independent **provided**
both κ and E_bond are treated as substrate constants, exactly as the derivation states.
I do not see an algebraic error in the identical-scaling cancellation. The remaining
caveat is already carried honestly: if later CPP derives strong temperature dependence
of either κ or E_bond, this result would require revision. That is a future theoretical
dependency, not a flaw in the present derivation.

**V2 — Cascade formulation and r³ conversion — Verdict: VERIFIED**

The load-bearing pieces appear internally consistent. Specifically: converting a
density defined per ℓ_p³ into rung-volume density through the explicit r³ scaling is
dimensionally appropriate; the closure-vs-growth branching probability
P = J_phys·v_f/(J_phys·v_f + a·φ) has the correct limiting behaviour (closure dominates
when J ≫ a·φ; growth dominates when J ≪ a·φ). The reported "termination within ~2 of
onset" follows from the stated inequality φ < J_peak, and the reported worst-case ×6
margin is admittedly the weakest point of the scan, but it is still a positive margin
rather than a sign reversal. I therefore do not see a computation-breaking units error.
The residual concerning chain-chain reactions beyond 2+2 is appropriately disclosed
rather than hidden.

**V3 — XQC channel integrity — Verdict: VERIFIED**

The verification chain is internally coherent. In particular: cache reproduces the
registered regression; cache reproduces fresh pipeline values; linear scaling of ρ*
with abundance follows directly because abundance enters only as an overall prefactor;
floor scanned across the complete ε_th bracket; above-floor scan limitation is
explicitly disclosed rather than concealed. Most importantly, the reported conclusion
("corridor closes above the floor") means the deferred fine-wall scan is not
outcome-changing for the stated claim. I therefore do not see a methodological defect
sufficient to overturn the XQC gate.

**V4 — Anchor channel, amendments, containment — Verdict: VERIFIED**

Given the joint structure described in the brief, I do not see evidence that: the
representative-member reduction can plausibly hide an entire class reversal; the
recovered coupling parameters introduce an undisclosed optimization; the process
amendment changes the grading logic. The distinction "central rejects the coupling law
rather than the family shape" is a logically different statement from "central rejects
the family," and the documentation consistently keeps those separate. Containment is
also correctly stated: candidate only, no registry change, no paper changed, no verdict
moved.

**V5 — Sign extraction and composition diagnosis — Verdict: VERIFIED**

I view this as the most interpretation-sensitive item. The paper does **not** claim
that attractive residual interactions have been rigorously derived. Instead it claims:
the presently registered substrate mechanism is attract-only; therefore the default
sign entering this candidate analysis is attractive; a future OPEN-SS-43 derivation
could still modify the effective screened transfer. That is appropriately graded as an
argument-level extraction rather than a completed derivation. Likewise, the explanation
for why the earlier repulsive-only result disappears is internally consistent with the
reported compositions: earlier compositions contained light contaminants; the derived
heavy-ring family suppresses those components; therefore the population-level XQC
behaviour changes without changing the underlying interaction sign. I do not see an
internal inconsistency in that reasoning.

#### Part II

**R1 — 2380(B2) addendum — Vote: RATIFY.** The addendum weakens the earlier claim
rather than strengthening it, retains the original wording, and explicitly carries the
conditionality introduced by the later audit. That is appropriate scientific
record-keeping.

**R2 — Clause 1(d) — Opinion.** I would recommend **adding** a new exit condition
rather than rewriting the existing one. Reason: the original 2.8 GeV clause still
documents the historical dimer branch; if this derived family is ultimately ratified,
the operational discriminant has moved to roughly the N≈6 mass scale (~8–10 GeV).
Keeping both preserves provenance while making the live falsifier explicit.

#### Ranked findings

**1. WOUND.** The load-bearing assumption is no longer the cascade algebra — it is the
identification of κ and E_bond as genuine temperature-independent substrate constants.
Future derivations should elevate this from inherited convention to explicit theorem if
possible.

**2. SCRATCH.** The attractive-sign discussion is correctly labeled candidate-grade in
the body, but because it materially changes the interpretation of earlier work, I would
keep every occurrence explicitly tagged as an argument-level extraction pending
OPEN-SS-43. That reduces the chance readers mistake it for a completed derivation.

### Return B (pasted inline; self-claimed label "R1"; window: Gemini per relay; the
window's visible reasoning chrome ("Thinking… Reviewing Documented Tasks / Analyzing
Verification Status") preceded the return and is omitted here as UI chrome)

SEAT R1

PART I — VERIFICATION

- V1 — The epoch-free stability floor: VERIFIED. The identical-scaling cancellation
  where both ℓ_p = κ/kT and ε = E_bond/kT scale with 1/kT correctly yields a
  temperature-independent ratio N_stab = c·κ/(ℓ_rung·E_bond). Treating κ and E_bond as
  substrate constants is consistent with registered structure, and the asymptotic
  argument for locking vs. popping open is physically sound.
- V2 — The cascade formulation and the r³ unit conversion: VERIFIED. The r³ unit
  conversion is dimensionally necessary to convert a contact density per ℓ_p³ to
  rung-volume units. The dilution guarantee holds across the bracket, and the
  mathematical identities for the QSS pair channel are sound.
- V3 — XQC channel integrity: VERIFIED. The exact ρ* calculation by f·ρ linearity is
  mathematically sound given the 1/M number density scaling. The deferral of the
  above-floor bracket is safe since the corridor closes anyway, and the floor-anchoring
  finding is clearly supported by the computed ρ* values dropping below viable local
  densities at higher S_c.
- V4 — Anchor channel + disclosed amendments + containment: VERIFIED. The use of 19/73
  stratified representatives is justified by the smoothness of the weights and
  eff_dist. The central frame's behavior correctly identifies a failure of the specific
  strain law rather than the shapes themselves. The targeted re-anneal for parameter
  recovery is a standard and acceptable process fix.
- V5 — The sign extraction and composition-specificity diagnosis: VERIFIED. Reading the
  1858 E_qq residual as attract-only correctly establishes the default sign. The
  diagnosis that the previous "repulsive or bust" finding was an artifact of light
  contaminants in the Q1 points is accurate; the heavy derived members lack these
  contaminants (due to ring topology) and thus survive on the attractive default.

PART II — RATIFICATIONS

- R1 — The 2380(B2) executed addendum: RATIFY. The addition of the ε_th conditionality
  is strictly claim-weakening and accurately reflects the findings of the 2379 fidelity
  audit.
- R2 — Clause 1(d) exposure (OPINION): Clause 1(d) as written is indeed vacuous now
  that the dimer branch is dead. A 2.8 GeV null test tests nothing live. A new exit
  condition targeting the derived mass scale (≈ 8.45 GeV, with its specific companions)
  should be added to maintain the falsifiability of the hypothesis.

RANKED FINDINGS

1. The identification of N_stab as an epoch-free, temperature-independent constant is a
   highly robust theoretical result that elegantly anchors the entire derivation
   without requiring complex thermal history tracking.
2. The resolution of the sign tension — demonstrating that the heavy derived members
   survive on the registered-default attractive sign at standard density — removes a
   major theoretical hurdle and validates the topological suppression of light
   contaminants.

DISCLOSURE Audited the provided code, logs, and reasoning documents. Did not re-run the
scripts locally.
