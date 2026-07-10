# CONV-001 ROUND 2384 — RETURNS + ADJUDICATION (Patch 2385, 9 July 2026)

**Round:** combined verification + ratification on the 2381–2383 derived-nucleation arc
(brief: `conv001_2026-07_arc2381_2383_verification_brief.md`).
**Status: 2 substantive returns of 5 seats.** Adjudication block OPEN below.
**[Patch 2386 supplement, 9 July 2026: a THIRD return (DeepSeek, seat R3) landed
before adjudication and Grok is definitively out — final collection 3 of 5. Updated
table, tally, coverage fact, and D1 recommendation in the SUPPLEMENT at the end of
this file. The sections below stand as written at 2385.]**

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


---

# SUPPLEMENT — THIRD RETURN RECEIVED; COLLECTION FINAL AT 3/5 (Patch 2386, 9 July 2026)

## S1. Final seat status

| Window (founder relay) | Return | Cause / note |
|---|---|---|
| GPT | Return A (self-label "R1") | complete; audited-not-reran |
| Grok | none — FINAL | "thought for a long time and then disconnected; no result" — second failure, definitive for this round |
| Gemini | Return B (self-label "R1") | complete; audited-not-reran |
| Copilot | none — FINAL | structurally unable, both delivery paths (per 2385 record) |
| DeepSeek | **Return C (seat label "R3")** | complete; **RE-RAN 2381 + 2382** (batteries independently confirmed 6/6 and 7/7), audited 2383 with spot-checks |

Seat labeling note: Return C carries a DISTINCT label ("R3") — no collision this time;
the 2385 label-collision note applies to Returns A/B only.

## S2. Final tally (3 returns)

| Item | A | B | C | Tally |
|---|---|---|---|---|
| V1 stability floor | VERIFIED | VERIFIED | VERIFIED | **3× VERIFIED** |
| V2 cascade + r³ | VERIFIED | VERIFIED | VERIFIED | **3× VERIFIED** |
| V3 XQC integrity | VERIFIED | VERIFIED | VERIFIED | **3× VERIFIED** |
| V4 anchor + amendments | VERIFIED | VERIFIED | VERIFIED | **3× VERIFIED** |
| V5 sign + composition | VERIFIED | VERIFIED | VERIFIED | **3× VERIFIED** |
| R1 | RATIFY | RATIFY | RATIFY | **3× RATIFY, 0 objections** |
| R2 | add, retain original | add | add (text proposed) | **CONVERGENT ×3** |

**Halting rules: none triggered.** Zero REFUTED, zero INDETERMINATE across all three.

## S3. Coverage fact UPDATED

The 2385 record stated "no seat executed code this round." **Superseded by Return C:**
the DeepSeek seat RE-RAN the 2381 grounding script and the 2382 cascade script and
independently confirmed both exit-coded batteries (6/6, 7/7), and spot-checked the 2383
XQC ρ* values for the N6-dominant members, the anchor anneal outputs, the cache
regression, and the sign-extraction logic — "all checks align with the reported
outcomes." The round now includes independent re-execution of the arc's two derivation
stages and targeted verification of the collision stage.

Return C's V5(b) adds a mechanism statement in its own words (light species carry a
higher number density per unit mass — the N-dependent NDM prefactor — so light
contaminants drag ρ* down); its illustrative "Q1 central ρ* ≈ 0.2" is the reviewer's
own approximation, directionally consistent with the stored rows and not relied on by
the tally. Return C's ranked findings align with Returns A/B rank-1 (the epoch-free
floor) and B rank-2 (the sign-tension resolution); no new actionable finding — the
F-A1/F-A2 actions executed at 2385 stand and cover the set.

Return C's R2 opinion proposes concrete clause text ("a direct-detection null at the
derived dominant mass (≈ 8.45 GeV) at the abundance the passing regions require") —
consistent with, and slightly leaner than, the (d′) draft in §5; both are before the
founder at D4.

## S4. D1 recommendation UPDATED

The 2385 recommendation (one retry window for DeepSeek + Grok) is DISCHARGED BY EVENTS:
DeepSeek landed; Grok failed a second, definitive time. **Updated worker
recommendation: CLOSE the round at 3/5** — three complete convergent-VERIFIED returns,
one with independent re-execution; the two non-returns have recorded structural causes
(one seat disconnects, one seat cannot ingest by either path). Nothing further is
collectible at reasonable cost. D2–D4 stand as written, now on the 3/5 tally.

## S5. Verbatim Return C (DeepSeek window per relay; seat label "R3")

**Seat: R3**

### PART I — VERIFICATION

**V1 — the epoch-free stability floor (the arc's load-bearing new theory)**
**VERIFIED**

The cancellation is exact given the registered scalings: ℓ_p = κ/kT (worm-like-chain
stiffness, 0861 convention); ε = E_bond/kT (registered D1 band from 0881). Thus
r = ℓ_p/ℓ_rung ∝ 1/kT and ε ∝ 1/kT, so the ratio r/ε is temperature-independent.
N_stab = c·r/ε = c·κ/(ℓ_rung·E_bond) depends only on substrate constants κ and E_bond.
The asymptotic argument holds: below N_stab the bending term c·r/N grows as fast as ε
under cooling → opening barrier ε − c·r/N remains finite → ring never locks; above
N_stab the barrier grows without bound → locks permanently; ln Λ affects only the lock
timing, not the boundary. No registered-structure reason to treat κ or E_bond as
temperature-dependent; the cancellation is algebraically sound. The factor-of-1.40
shift between c = 14.054 (SY) and 2π² (rigid) is carried explicitly.

**V2 — the cascade formulation and the r³ unit conversion (load-bearing units)**
**VERIFIED**

(a) Unit conversion: SY J-factor g(u) is a contact density per ℓ_p³. Converting to
rung-volume units requires division by r³ = (ℓ_p/ℓ_rung)³. J_phys(N) = g_SY(N/r)/r³·v_f
is correct; the script carries it explicitly, and the decade-shift in onsets is
accounted for. (b) Branching: P = J_phys·v_f/(J_phys·v_f + a·φ) is the correct
quasi-steady-state competition between closure (rate J_phys·v_f) and growth (rate a·φ).
The O(1) brackets for a, v_f are stated and scanned. (c) Dilution guarantee:
φ < J_peak_phys holds across the registered window. The worst-corner margin is ×6
(r = 12, φ_max, v_f = 0.1). Even at that thin edge, the onset remains on the
exponential rising side of J, so the cascade still terminates within ~2 sizes. Escape
≤ 1.5e-28 and width ≤ 2 are computed over the full grid; the conclusion survives.
(d) QSS pair channel: the identities q·x² + x = ½ (battery-verified) and ring-mass =
monomer-influx (V6) are exact. The statement that chain-chain channels beyond 2+2 are
O(1) shape corrections near onset is justified: when J ~ φ, N ≥ 3 chains are not
instantly absorbed, but the structural verdicts rest on exponential-vs-bracket margins,
not those details.

**V3 — XQC channel integrity (the gate)**
**VERIFIED**

(a) Cache regression: the committed unit cache reproduces the stored 2366b point
(viol = 3, total 642.2190945369623, rel 1.8e-16) and matches a fresh 1879 pipeline call
bit-level. Q1 compositions re-graded from the cache reproduce every stored 2374c
verdict and worst ratio (max rel 0.0). (b) Exact ρ* by f·ρ linearity: the X-ray signal
scales linearly with f·ρ (NDM prefactor), so ρ* = 1/max_ratio is exact for a given
composition. (c) Deferral verdict-safe: the floor (S_c = 0.012) is graded across the
full ε_th bracket {1, 0.5, 0.25, 0.1, 0.02}. Above-floor (S_c = 0.035, 0.05) are at
ε_th = 1 only, disclosed, with the fine-wall task deferred. This deferral is safe
because the corridor closes above the floor anyway: ρ* ≤ 0.09 at S_c ≥ 0.035, a factor
≥ 2 below any density where the floor verdicts live. (d) Floor-anchoring: the derived
population survives only at S_c ≈ 0.012 — confirmed by the numbers: for N6-dominant
members, ρ* ≥ 0.3 at S_c = 0.012 (ε_th-robust), but ρ* ≤ 0.09 at S_c = 0.035. The
island-floor demand is sharp.

**V4 — anchor channel + disclosed amendments + containment**
**VERIFIED**

(a) Scan adequacy: composition pinned, coupling-only anneals (3k wide + 6k×2 seeds) are
adequate. The 19/73 stratified representatives are justified: adjacent members differ
< 0.1 in any weight, and eff_dist is smooth in w. A class-level flip (e.g., a whole
peak-N group passing/failing) is extremely unlikely to hide. (b) Central-frame finding:
correctly read as a constraint on the coupling law, not the shapes. The central frame
refuses the registered strain family g²(N) = g0²(N/4)^p for every member (best viol
1.25–2.15) but admits every multi-species member with free per-species couplings. This
sharpens the 2375 finding: central rejects the strain law, not these shapes.
(c) Process integrity: the first launch died after XQC completed; the amendment
(stratified reps, reduced budgets) was written pre-anchor. Joint-member couplings were
recovered by targeted re-anneal because the main dump had not persisted them — no
verdict-relevant information is hidden; the recovery is sound. (d) Containment:
candidate-grade only; no verdict moved, no registry edits, no paper touched.

**V5 — the sign extraction and the composition-specificity diagnosis**
**VERIFIED**

(a) Sign extraction: the registered 1858 mechanism (OPEN-SS-43 entry) states "E_qq is
attract-only, so a qCP aggregate … cannot dipole-cancel." This fixes the DEFAULT
interaction sign as attractive in both graded channels. The status is correctly graded
as argument-level extraction: a repulsive effective transfer sign could still emerge
from the OPEN-SS-43 derived screened form (the same unpaid rent that owes S(N)).
(b) Composition-specificity: verified. The Q1 points carry light contaminants
(w(3) = 0.064 central) that drag ρ* down because light species have higher number
density per unit mass. The derived heavy members carry no light contaminants (ring
topology zeros w(1), w(2)), so their ρ* is higher. Example: {6:1.0} ρ* = 0.428
attractive (ε_th-robust) vs. Q1 central ρ* ≈ 0.2 at same S_c. The mechanism is the
N-dependent NDM prefactor. (c) Consequence containment: "D6 does not fire on the
default; the sign prices corridor width, not existence" is a candidate-grade statement
only — correctly contained.

### PART II — RATIFICATIONS

**R1 — the 2380(B2) executed addendum — RATIFY.** The addendum (dated ε_th
conditionality: robust at ε_th ∈ {1, 0.5, 0.1}; at the literature extreme 0.02 only the
island-floor corner un-excludes) is strictly claim-weakening, retains the original
verbatim, and was flagged for panel ratification. No defect; ratify as executed.

**R2 — Clause 1(d) exposure — OPINION.** Clause 1(d) as written ("a direct-detection
null at the dimer-regime mass (≈ 2.8 GeV) at the abundance the passing regions
require") is now vacuous because the dimer branch is dead (2369, conditional per R1).
The surviving derived members sit at ≈ 8.45 GeV dominant (N = 6). Per the clause's
add-only rule, a new exit condition should be added once this round verifies the
derived family: "a direct-detection null at the derived dominant mass (≈ 8.45 GeV) at
the abundance the passing regions require." This maintains the clause's protective
intent and updates the discriminant mass.

### RANKED FINDINGS

1. The epoch-free stability floor is the arc's most consequential theoretical advance.
   It replaces a Λ-entangled epoch-bookkeeping problem with a pure substrate ratio,
   sharply reducing the degrees of freedom and making the floor prediction testable
   against the SSV well properties.
2. The composition-specificity of the sign constraint resolves the 2374c "repulsive or
   bust" tension. The derived heavy members survive at standard density on the
   attractive default because ring topology eliminates light contaminants — a
   structural, not parametric, difference. This turns D6 from a kill into a
   width-pricing condition.

### DISCLOSURE

Re-ran vs audited: 2381 — re-ran the grounding script; verified battery 6/6.
2382 — re-ran the cascade script; verified battery 7/7. 2383 — audited the code and
results; spot-checked XQC ρ* calculations for N6-dominant members and anchor anneal
outputs; verified the cache regression and sign extraction logic. All checks align
with the reported outcomes.

---

# ADJUDICATION ENTRIES (Patch 2387, 9 July 2026)

**Founder verbatim, on the record:** *"Approve D1-D4 if you approve. If you want a
statement, tell me what needs to be said. I don't know what is being requested of me."*

**D1 — ENTERED: ROUND CLOSED at 3/5** (founder approval by explicit delegation to the
worker recommendation; three complete convergent-VERIFIED returns, one with independent
re-execution; both non-returns carry recorded structural causes).

**D2 — ENTERED: THE 2381–2383 ARC IS ADJUDICATED PANEL-VERIFIED** (3-seat coverage,
one re-executing seat, zero refutations; founder approval by explicit delegation).
Consequence: **Q3c OPENS** on the inherited target (r ≈ 8.5–12; N_stab ≈ 3.3–7.3 + the
F-A1 substrate-constancy theorem demand; S_c at the island floor; R_s ≈ 20–50 fm;
Λ thresholds; 8.45 GeV dominant; sign ARGUMENT-LEVEL per F-A2). Scope guard:
PANEL-VERIFIED is not registration — the derived family is NOT registered as the
successor branch by this entry; that registry-grade move follows Q3c's rent (or an
explicit earlier founder decision).

**D3 — ENTERED: R1 RATIFICATION CONFIRMED** (3× RATIFY, 0 objections; founder approval
by explicit delegation). The panel-ratification flag carried by the 2380(B2) ε_th
addendum since execution is DISCHARGED; the 2369 kill's conditionality clause stands
ratified.

**D4 — HELD, NOT ENTERED.** The blanket delegation is NOT accepted for this item, on
the worker's own judgment: D4 amends the founder-attested Clause 1, whose add-only rule
exists precisely so that exit conditions carry the founder's personal, informed
attestation — and the same founder message states *"I don't know what is being
requested of me."* An attestation entered under those words would be an attestation in
name only. The deferral is costless: (d′) becomes operative only once the derived
family is registered (post-Q3c). The exact proposed sentence stands in §5 and in the
worker's plain-language explanation to the founder; D4 enters on the founder's explicit
yes (or edited text), dated.

**Round 2384 is CLOSED.** Items outstanding from the round: D4 only.
