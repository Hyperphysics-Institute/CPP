# CONV-001 SF-6 PIN CORRECTIONS — ADJUDICATION (Patch 2876)

**Four distinct positions, not five. A1 4–0 · A2 4–0 · A3 3–1 · B1 4–0
REASONED-UNVERIFIED. Zero fabrications, fifth consecutive clean round.
The question-typing discipline is validated on its second use. And the
pin's headline result is DEMOTED by unanimous panel ruling.**

---

## §1 — ROSTER INTEGRITY: THIRD OCCURRENCE, AND THE WORKER MISSED THE SECOND

**Two returns this round are BYTE-IDENTICAL** — identical opening verdict
("broadly appropriate, but it should stop short of exoneration"),
identical LaTeX rendering artifacts, identical section structure,
identical closing table with identical wording. They arrived labelled as
**S1 (GPT)** and **S4 (Copilot)**. Independent models do not produce
several thousand words of identical text.

**Per the Patch 2849 precedent, which is directly on point and which the
worker should have consulted before this round rather than after:
byte-identical returns are counted as ONE seat position, not two.**
2849's handling is adopted verbatim — most probable cause is a duplicated
paste at dispatch rather than seat misconduct, **no blame is assigned**,
and confirmation is requested. **Effective roster this round: four
distinct positions** (S1, S2, S3, S5), with **S4 recorded as NOT
RETURNED** pending confirmation. **No conclusion below rests on the
doubled position's extra weight.**

**WORKER DISCLOSURE — THIS IS THE THIRD OCCURRENCE AND THE SECOND WENT
UNCAUGHT.** At the SF-6 dispatch's first (placeholder) attempt, S4 and S5
returned byte-identical declines and **the worker counted them as two
independent declines**, then drew a capability inference from the count.
That inference was unsound and is corrected in §2. 2849 had already
established the check, in this repository, and the worker did not run it.
**Fourth instance this session of the answer being in the corpus
unconsulted.**

**Per-round flagging has now failed to prevent three occurrences.
Registered as CONV-008** (`todolist.md`): before adjudicating any CONV-001
round, returns are compared pairwise for byte-identity or near-identity,
and any identical pair is counted as one position with the roster size
adjusted in the adjudication's header before any question is scored.

## §2 — CORRECTED CAPABILITY FINDING (supersedes Patch 2875's chat claim)

The worker stated at the 2875 re-issue that S1, S4 and S5 cannot fetch
raw GitHub. **That rested on counting one duplicated decline as two.**
Corrected, on confirmed evidence only:

| seat | raw-GitHub fetch | evidence |
|---|---|---|
| S1 (GPT) | **CANNOT** | stated explicitly, tried both raw and blob forms |
| S2 (Grok) | **CAN** | returned file-precision values (2.172/1.090) and §5's option labels before inlining |
| S3 (Gemini) | **CAN** | same |
| S4 (Copilot) | **UNDETERMINED** | may never have returned; see §1 |
| S5 (DeepSeek) | **UNDETERMINED** | its decline may have been the duplicated one |

**Operational consequence, unchanged and reinforced:** CONV-001's
requirement that the full rendered file be inlined is load-bearing, and
the worker's placeholder at the first attempt was a violation of it. The
template's own text predicted the outcome — *"a reviewer who cannot see
the source will (correctly) decline to review"* — and three returns did
exactly that. **The convention was right and the worker was wrong; no
amendment to CONV-001 is warranted, only compliance.**

## §3 — A1: THE WITHDRAWAL STANDS, 4–0, WITH S1'S QUALIFICATION ADOPTED

A1 asked the panel to check whether the worker, having been wrong about
this file three times in four patches, was now over-correcting toward
exoneration of its own shipped numbers.

**All four distinct positions: NOT over-correcting.** S2 — "goes far
enough and does not over-correct." S3 — "appropriately calibrated." S1 —
"broadly appropriate, but it should stop short of exoneration." S5 —
"appropriately far... measured, evidence-based."

**Adopted. The withdrawal stands.** A criticism whose named test has
refuted it must not be preserved, and §2(i)–(iii) of the dispatch are
measurements rather than characterisations.

**S1's two qualifications are ADOPTED, and the second is new to the
record:**

1. **The prose debt remains open, not discharged.** Stage C still says
   v(t) ≈ v₀exp(−t/κμ), which describes neither the release spin-up nor
   the μ = 10 tail crossing. Registered; owed as prose.
2. **PROCEDURAL DEFENSIBILITY IS NOT PHYSICAL VALIDITY.** S1, verbatim:
   *"Showing that the fitting window is legitimate does not establish
   that the toy's late-time behavior is the correct physical analogue. It
   establishes that the reported τ values were extracted in a
   procedurally defensible way."* **This distinction was not in the
   dispatch and the worker had not drawn it.** What §2 established is
   that the estimator was applied honestly — not that the coast's
   late-time behaviour models anything. **Registered as a standing
   caveat on all three coast τ readings.**

**Note for the record: A1 is the question the worker least wanted
answered, and the answer was favourable. Per standing discipline that is
a reason for less confidence in it rather than more — but the
qualification S1 attached is unfavourable and specific, and it is adopted
in full, which is the part that matters.**

## §4 — A2: THE HEADLINE RESULT IS DEMOTED. UNANIMOUS, 4–0, FOR OPTION (b).

**Every distinct position ruled (b): the pin's headline F = κa result is
demoted to a SCALAR-TOY ANALOGUE pending the correspondence.** No seat
took (a); no seat took (c).

Reasoning converged independently. The founder's ruling separates the
toy's F_self from CPP's SSV_net and denies that any self-force exists in
CPP; until a mapping is established, results proven inside the toy do not
transfer. S1: option (a) *"presumes the mapping"*; option (c) fails
because the ruling's wording *"explicitly broadens the uncertainty beyond
the runaway discussion."* S5 adds the sharpest form: κ is statics-pinned,
but **the dynamical reading F = κa depends on what F represents**, so if
F_self maps to nothing in CPP, the dynamical law may not translate even
though the coefficient survives.

**ADOPTED. Pin §5 conclusion 1 — "Newton II is derived in-model" — is
demoted to a statement about the scalar toy.** It is not falsified and
not withdrawn; its CPP interpretation is conditional.

**S1's formulation of what is now owed is adopted as the registered
requirement.** The chain was:

> statics → toy → automatically CPP

and is now:

> statics → toy → **correspondence theorem** → CPP

**Registered as OPEN-FSELF-CORRESPONDENCE-1:** establish explicitly
whether the 2496 toy's F_self corresponds to a CPP substrate observable
— specifically whether it is expressible in terms of others' responses
re-entering as SSV_net at the CP's location — or whether it is an
artifact of the scalar toy's continuum construction. **Until this is
discharged, no CPP-level inertia claim may cite the pin's dynamical
result.**

**This is a real cost to a result the programme was leaning on, and it
was delivered unanimously by a panel with nothing to gain from it.**

## §5 — A3: SPLIT 3–1. VALIDITY TO THE MAJORITY, ACTION TO THE DISSENT.

**S1, S2, S3: authorised in part** — (i) the statics-pinned
κ = (2/3)U/c² is untouched and authorised; (ii) the Laue coefficient-1
half waits on the SF-1 cage computation at §5.7(d).

**S5 dissents for full withdrawal**, on a ground the majority did not
address: *"Authorizing only part (i) would give an incomplete and
potentially misleading replacement for SF-6's parameter-tuning
passage."*

**RESOLVED BY SEPARATING TWO QUESTIONS THE DISPATCH HAD CONFLATED:**

| question | ruling |
|---|---|
| Is (i) a **valid result**? | **YES — majority adopted.** κ is pinned by statics, six readings agree, and neither 2868 nor 2875 bears on it. It survives A2's demotion because it does not route through F_self. |
| Should (i) **now replace** SF-6's tuned passage? | **NO — S5's dissent adopted. DEFERRED until (ii) lands.** |

**S5's argument is correct on the action.** SF-6 v1.0's tuned passage is a
**disclosed** limitation — the paper says "by tuning the model
parameters." Replacing it with half the intended argument would trade a
disclosed weakness for an undisclosed gap, which is worse presentation
even though (i) is individually stronger than what it would replace. And
because **SF-6 v1.0 requires no re-ship** (dispatch preamble, grep
confirmed), **deferring costs the programme nothing.** Where the cautious
option is free, it is taken.

**Net: (i) may be cited as a result. The §6 replacement of SF-6's
inertial-mass passage is DEFERRED pending §5.7(d) AND
OPEN-FSELF-CORRESPONDENCE-1.**

## §6 — B1: THE TYPING WORKED AGAIN. 4–0 REASONED-UNVERIFIED.

**Not one seat offered a reasoned opinion in place of the requested
arithmetic.** S1 declined and listed precisely what it therefore would
not assert (growing perturbation, μ_crit, coast stability). S3 cited the
instruction explicitly. S5 noted that μ_crit = 1067.7 *"is not the
stability analysis itself"* — correctly distinguishing an arithmetic
consequence from a test of it.

**Two rounds of evidence now:** at 2874, four of five seats voted on a
mathematical question. At 2875 and here, **zero seats did, twice.**
Question-typing is retained as standing practice.

**B1 REMAINS UNANSWERED AND IS NOW THE WORKER'S OWN JOB.** No seat has
the execution environment. The linear stability analysis about the steady
coasting solution — perturb v, enforce |v| ≪ c, choose dt for the coast
branch — is the only route to μα and it will not arrive from the panel.

## §7 — EXECUTION INTEGRITY

**4–0 REASONED-UNVERIFIED, all with reasons.** S2 named the specific
obstacle: `2875_coast_full_diagnostic.py` requires its dependency
`2496_sf6_inertia_impulse.py`, which was not among its retrieved
artifacts. That is a precise and honest account and it is credited as
such.

**Zero fabrications. Fifth consecutive clean round.** The withheld key
under CONV-007 went unclaimed by every seat; the key was admissible and
simply unreachable. **Standing note: a CONV-007-compliant key is
answerable only by a seat that can fetch BOTH the diagnostic and its
dependencies**, which on §2's corrected table is at most S2 and S3. Keys
should be scoped to a single self-contained artifact in future rounds.

## §8 — NET EFFECT AND CONSEQUENCE FOR SF-8

**Nothing here touches 1B.** 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5% untouched. **SF-6 v1.0 stands as shipped,
unmodified, no re-version.**

**Changed:** pin §5 conclusion 1 demoted to scalar-toy scope; §6
replacement deferred; three new registered items —
**OPEN-FSELF-CORRESPONDENCE-1**, the standing
procedural-defensibility caveat on the coast τ readings, and the owed
Stage C prose.

**DIRECT CONSTRAINT ON SF-8, WHICH IS THE NEXT ITEM.** SF-8 is chartered
on emergent Coulomb plus the measured ZBW Sea and sits in the same tree.
**Per §4 it must NOT cite the pin's F = κa as a CPP substrate-mechanism
result.** It may cite the statics-pinned coefficient (§5), and it may
cite the toy result as a toy result. **This constraint is registered
before SF-8 assembly begins rather than discovered during review.**
