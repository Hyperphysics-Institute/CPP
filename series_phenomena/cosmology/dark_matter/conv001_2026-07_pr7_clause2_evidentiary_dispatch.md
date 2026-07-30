# CONV-001 — PR7 CLAUSE 2 (OPEN-K1-MEMORY-1B): EVIDENTIARY BURDEN, N, AND THE ORDER OF THE CORRECTION — DISPATCH (Patch 2873)

**Chartered at `founders_voice/founder_reframing_bias_on_ringing_carrier_2026-07-29.md` §7
(Patch 2864). Named first priority in four consecutive patches — 2863,
2864, 2865, 2866 — and not written in any of them. The reason is on the
record: it requires the founder to paste a block, so it is not work the
worker can complete alone, and everything chosen instead was. It is
written now, before any other item in the queue.**

**1B remains OPEN. Six of seven. Founder Decision B7 continues to hold
DM-1/DM-2/DM-3. Candidate (B) 79.5% PROVISIONAL-FAVORABLE, untouched.
Nothing in this dispatch computes τ_Sea, N, or any v/c bound — the 2864
stop-order forbids it until Q1 and Q2 return.**

---

## §1 — What the panel is being asked to adjudicate, and why it is not a re-reading

**This is NOT a request to re-read clause 2.** Patch 2861 §3 established
that the panel already adjudicated the reading 5–0 at the naming motion
(`conv001_2026-07_pr7_naming_adjudication.md` N2), and that the worker
was wrong to say otherwise. That finding stands and is not reopened.

What is unadjudicated is narrower and downstream of the reading: **what
KIND of evidence discharges the burden**, given that the founder's
inertia arc (Patches 2862–2870) changed the mechanism under which τ_Sea
is to be obtained. The arc retired two worker objections and one
period-transfer question, and replaced them with a single unpinned
quantity, N. None of that has been before the panel.

**The governing 1B specification is K4**
(`conv001_2026-07_k1_memory_adjudication.md`, Patch 2837), adopted from
S1, verbatim:

> **OPEN-K1-MEMORY-1B — SUBDOMINANCE BOUND: OPEN.** Derive the
> kernel-to-instantaneous-force bound
> |F_mem|/|F_inst| ≤ C_mem(v/c) + O(v²/c²) — or, if the first-order
> term cancels by symmetry, at O(v²/c²) — specifying C_mem, the norm,
> the state class, and the frequency/acceleration range independently
> of the measured ambient velocity; **and** bound the ambient physical
> Sea v/c without using AUTOMATON regime-artifact values.

K4 also adopted the operative threshold: **δ_mem ≡ |F_mem|/|F_inst| ≤
0.15, NOT a velocity ratio**, with v/c ≤ 0.15/C_mem following as a
consequence, and a v/c ≤ 0.15 screening bar retained but labelled
**NECESSARY, NOT SUFFICIENT**.

## §2 — A correction the worker owes the charter, made before the questions are put

The session-close handover restated chartered question (a) as *"does
clause 2's evidentiary burden admit an **empirical bound on τ_Sea**
(e.g. via measured inertia) or does it require a substrate
derivation?"*

**That is not the chartered question. It is the weaker 2863 framing that
2864 §5 explicitly superseded, and the panel must not be asked it.**

- At **2863 §5** the worker proposed using the *absence of observed
  inertial lag* as an empirical **upper bound** on τ_Sea, and flagged
  that the panel might reject an empirical input as failing clause 2's
  evidentiary burden.
- At **2864 §5** the founder's reframing inverted that. If extraction
  and restoration were perfectly balanced each Moment there would be no
  inertial force at all; the inertial effect *requires* the lag.
  Verbatim: **"τ_Sea is not merely bounded by inertia. τ_Sea is what
  makes inertial mass nonzero."** The relation is therefore not a bound
  but a **functional dependence, m_inertial = f(τ_Sea), with f
  invertible.**
- The chartered question (2864 §7a) is accordingly whether clause 2
  admits **m_inertial as a calibration input under that inversion** —
  with the same epistemic standing as the programme's single existing
  calibration input, m_e — i.e. *a derivation with one measured
  constant*, not an empirical substitute for a derivation.

The distinction is load-bearing: an empirical bound is plausibly
inadmissible under K4's "independently of the measured ambient
velocity" language, whereas a calibration input of m_e's standing is
plausibly admissible. **Asking the weaker form would have invited a
refusal that does not reach the actual claim.** This is the fifth
handover-gloss failure of the arc and the first caught before it
reached the panel; it is disclosed rather than silently fixed.

**The worker does not assert that f exists in closed form, has not
derived it, and is not asserting that it does.** That caveat is the
founder-arc worker's own (2864 §5) and is carried forward unweakened.

## §3 — A tension surfaced this patch, not previously flagged, bearing on (c)

Chartered question (c) is *"confirm ε_mem is first order given §2
retires the ring-down picture."* Before that can be confirmed the panel
must resolve an apparent conflict inside the corpus, which the worker
did not create and cannot adjudicate.

**Position 1 — the first order CANCELS.**
`open_k1_memory_1b_cmem_derivation.md` (Patch 2838) argues that K4's own
escape clause is the case that obtains: for charges coupled to a field
propagating at c, eliminating the field produces no O(v/c) correction to
the instantaneous Coulomb interaction, because in Coulomb gauge the
scalar potential is *exactly* instantaneous and all retardation sits in
the vector potential, entering the inter-charge interaction at second
order (Darwin). Hence **δ_mem ≤ C₂(v/c)² with C₂ ∈ [0.5, 1]** naturally
and C₂ ≤ 2 conservative. That note also observes that the founder's
**fore/aft antisymmetry of the arc (2026-07-25) is structurally the
statement that the first-order longitudinal effect cancels** — described
physically before it was needed there.

**Position 2 — ε_mem is FIRST order.** Founder ruling 2863 so ruled,
against the reading the worker had said favoured it. Patch 2864 §3
states that *"0.15 is the threshold on ε_mem, and k is what converts it
to a v/c bar,"* with **k = N**; and the transit-asymmetry mechanism
(2865–2867) has front arcs partially charged and opposing while rear
arcs are fully charged and discharging hence assisting — **an asymmetry,
i.e. a surviving first-order net effect.**

**These may not be in conflict at all, because they may not be the same
quantity, and the corpus does not say which.** Three distinct
definitions carry the label and/or the 0.15 threshold at different
points in the record:

| # | symbol as used | definition | source |
|---|---|---|---|
| 1 | δ_mem | \|F_mem\|/\|F_inst\| — a **force** ratio | K4, Patch 2837 (**operative threshold adopted here**) |
| 2 | δ_mem(k,ω) | \|χ(k,ω) − χ(k,0)\|/\|χ(k,0)\|, with φ_mem = \|arg χ(k,ω)\| — a **susceptibility** ratio | naming motion N3(i), Patch 2832 |
| 3 | ε_mem | τ_Sea/τ_slow, evaluated at d_DP — a **timescale** ratio, linear in v/c by construction since τ_slow ≃ d_DP/v | derivation sketch §2, Patch 2834 |

A timescale ratio and a force ratio are not interchangeable. **A kernel
can have finite width — ε_mem of first order — while its first moment
vanishes by symmetry, so that the induced force correction begins at
second order.** If that is the situation, Position 1 and Position 2 are
both correct about different objects, the founder's first-order ruling
stands, and 2838's cancellation also stands, and 1B's operative bar is
on δ_mem, not on ε_mem. If instead the corpus intends ε_mem ≡ δ_mem with
k ≡ C_mem, then Position 1 and Position 2 are in direct conflict and one
must yield.

**The worker flags, symmetrically and in both directions:** Position 1
is a *favourable* convergence (second-order suppression makes the
ambient-Sea requirement permissive — v/c < 0.19–0.55 per 2838 §2), and
Position 2 is *unfavourable* (it requires N pinned before any bar
follows). Per the standing pattern-warning, the fact that one of these
would ease closure is a reason for more scepticism about it, not less.
**2838 is CONDITIONAL and does not close 1B by its own statement**: its
§3 records that CPP's relay reproducing the transverse sector *with the
correct weight* is NOT established, that emergent Coulomb tests the
scalar sector only, that no committed artifact tests the
magnetic/transverse sector against electrodynamics, and that if CPP's
transverse structure differs then C₂ changes and **could in principle
restore an O(v/c) term.**

## §4 — QUESTIONS

**Q1 — EVIDENTIARY BURDEN. This gates everything downstream; answer it
first and independently of Q2–Q4.**
Under the §5 inversion — m_inertial = f(τ_Sea), f invertible, the lag
being what makes inertial mass nonzero — does clause 2's evidentiary
burden admit **m_inertial as a calibration input** of the same standing
as m_e, yielding a derivation with one measured constant? Or does K4's
requirement that C_mem be specified *"independently of the measured
ambient velocity"* also exclude a measured **inertial** input, so that
clause 2 requires a substrate derivation of τ_Sea taking no measured
input at all? **If the answer is conditional, state the condition as a
test on f, not on the numerical value obtained.**

**Q2 — IS N PINNABLE FROM THE UPDATE RULE ALONE?**
N is the number of Moments the collective translational organization is
held in the environment before restoration; k = N. The Perceive-Compute-
Displace cycle renews every CP's state each Moment — not in dispute —
but 2864 §4 grants the objection that a **collective organization
spanning a volume** need not renew in one Moment, citing the
molecular-collision-versus-sound-absorption disanalogy. Is N therefore
derivable from the PCD update rule alone, or does it require the
C23/C24 specification (i.e. does 1B inherit OPEN-PR4-C23C24's
dependency after all)? **K5 held that 1B is *related to* but *not
identical with* OPEN-PR4-C23C24, and that a causal-retardation bound may
be derivable from deterministic field propagation without Gibbs
thermodynamics. Q2 asks whether that separation survives the
introduction of N.**

**Q3 — THE ORDER OF THE CORRECTION, AND WHICH OBSERVABLE CARRIES THE
BAR.** Per §3: (i) Are definitions 1, 2 and 3 in the §3 table the same
observable, related observables with a stated conversion, or distinct
observables? (ii) Which one does the 0.15 threshold attach to for 1B —
the worker reads K4 as attaching it to δ_mem = |F_mem|/|F_inst|, while
2864 §3 states it attaches to ε_mem. (iii) Is ε_mem first order, as
2863 ruled, **compatible** with δ_mem beginning at second order, as 2838
argues — i.e. is the reconciliation that the kernel's first moment
vanishes while its width does not? Or does one position have to yield?

**Q4 — ADDED THIS PATCH, NOT IN THE 2864 CHARTER.** 2838's cancellation
is conditional on CPP's relay reproducing an instantaneous
Coulomb-gauge scalar sector *and* a transverse sector entering at second
order, and it records that the transverse leg is untested by any
committed artifact. `open_k1_memory_1b_transverse_prereg.md` exists.
**Is the transverse-sector test a prerequisite for admitting 2838's
cancellation into 1B's ledger, or may the cancellation be admitted
conditionally with the transverse test as a registered debt?** The
worker does not propose an answer.

## §5 — Standing on dispatch

PR1 MET/retired · PR2 MET · PR3 MET · PR4-BARE MET-NEGATIVE
(PR4-COMPLETED = OPEN-PR4-C23C24) · PR5 MET · PR6 MET · **PR7 PARTIAL —
OPEN-K1-MEMORY-1A MET, OPEN-K1-MEMORY-1B OPEN.** Six of seven.

**Per OPEN-B7-SCOPE-1 resolved at R-2, PR1–PR7 are Candidate (B)'s
promotion criteria, frozen at the 2726 adjudication, so 1B is on the
release critical path and is the only remaining promotion item.**

**The 2864 stop-order is in force and this dispatch does not breach it:
no τ_Sea, no N, and no v/c bound is computed here, and none will be
before Q1 and Q2 return.**

**De-prioritised and NOT to be revived by any seat in this round:**
OPEN-SEA-DENSITY-1 as a route to 1B (Route 2 does not revive at any
physically defensible density, Patch 2861 §2); the C23/C24 FEM
arc-inertia study as the *only* route to 1B.

## §6 — Execution integrity

Five fabrication events are on the campaign record (S5 ×4, S1 ×1). S2
holds the campaign's first and so far only **VERIFIED-EXECUTED** ruling
(Patch 2832), sustained because the key was computable from a committed
artifact with the path named — S2's own 2829 correction, which is what
made honest verification possible.

**Withheld key for this round.** From the committed artifact
`flagship_papers/electromagnetism/code/2868_hold_force_refinement.py`, a
seat claiming execution should report: **(i)** the three F_hold values
across the dt ladder, **(ii)** the three F_hold/vf ratios across the vf
ladder, each to four significant figures, and **(iii)** the SIGN of
F_hold relative to the direction of motion. Expected values are withheld
from this dispatch and held by the worker for comparison.

Seats not executing must declare **REASONED-UNVERIFIED with reasons**.
Do not report a value not actually computed; a declared
REASONED-UNVERIFIED costs a seat nothing, and the last three rounds have
been clean.

**Seats:** S1–S5 per standing CONV-001 assignment. Return per question,
Q1 first and separably — a partial return answering only Q1 is more
useful than a complete return that waits.
