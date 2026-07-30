# CONV-001 PR7 CLAUSE 2 DISPATCH — ADJUDICATION (Patch 2874)

**Five returns. Q1 5–0 · Q2 5–0 · Q3(i) 5–0 · Q3(ii) 5–0 · Q3(iii)
ADJUDICATED TO THE MINORITY 1–4 · Q4 resolved on a precedent the
majority cited only half of. The worker's own candidate reconciliation
is REJECTED. Zero fabrications. And the withheld key was not withheld —
a worker design error that voids the execution ruling.**

**LEDGER: 1B OPEN. PR7 PARTIAL. Six of seven. B7 holds DM-1/2/3.
Candidate (B) 79.5% untouched. This round made 1B HARDER, not easier.**

---

## §1 — EXECUTION INTEGRITY: THE KEY WAS VOID, AND THAT IS THE WORKER'S FAULT

**S2 (Grok) claimed EXECUTED and returned:** dt ladder F_hold =
4.683e-5, 4.688e-5, 4.698e-5; vf ladder F_hold/vf = 9.416e-4, 9.377e-4,
9.436e-4; sign POSITIVE/FORWARD.

**Every value is correct.** The worker independently re-executed
`flagship_papers/electromagnetism/code/2868_hold_force_refinement.py`
this patch and obtained an exact match on all six figures and the sign.

**And that establishes nothing, because the key was never withheld.**
The identical values are published in two places a seat can read without
executing anything:

1. **Patch 2868's own commit message**, verbatim: *"F_hold
   4.683e-5/4.688e-5/4.698e-5"*, *"F_hold/vf = 9.416e-4/9.377e-4/
   9.436e-4"*, *"T4 SIGN: forward"* — public in `git log`.
2. **The script's own docstring, line 24**, headed `RESULT (this script,
   N=96, g=8, c=h=1):`, which tabulates T1 through T4 including the sign.

**S2's own citation reads "(RESULT block and main() output)." The RESULT
block IS the docstring** — i.e. the non-executing path. That is not proof
S2 did not run the script; it is a reason no ruling is available either
way.

**RULING: the execution claim is UNADJUDICABLE. Not VERIFIED-EXECUTED,
not fabrication. No credit to S2, no penalty to S2.** A key whose answer
is printed in the artifact's own header and in the commit message tests
nothing. S2's 2829 correction required that a key be *computable from
committed artifacts with the path named*; the worker satisfied that and
missed the complementary requirement, which is now registered:

> **CONV-007 — WITHHELD-KEY ADMISSIBILITY.** A withheld verification key
> must be a quantity that (i) is computable from a committed artifact
> whose path is named, AND (ii) does not appear in any commit message,
> docstring, README, prose file, or prior adjudication in the
> repository. Requirement (ii) must be checked by grepping the full
> history — `git log --all --format=%B` plus the artifact source — before
> the dispatch is issued. A key failing (ii) is VOID and no execution
> ruling may be made on it.

**Four seats (S1, S3, S4, S5) declared REASONED-UNVERIFIED with
reasons.** S1 and S3 stated specifically that raw-file retrieval and
repository resolution were unavailable to them. **Zero fabrication
events this round; fourth consecutive clean round.** The honest
declarations are worth more than the unadjudicable claim, and the four
seats that declined to report numbers they had not computed did exactly
what the protocol asks.

**ROSTER FLAG, minor:** S5's return is headed "Seat 1 Response" while S5
is the fifth seat. Content is unambiguously S5's own; treated as a
labelling slip, recorded not penalised.

## §2 — Q1: ADMIT CONDITIONALLY, 5–0 — BUT S1 ALONE FOUND THE PROGRAMME-LEVEL PROBLEM

All five seats admit m_inertial as a calibration input, conditional on
properties of f. **The consensus is adopted.** K4's phrase
*"independently of the measured ambient velocity"* bars fitting the
response coefficient to the velocity the bound is meant to constrain; it
does not impose a zero-measured-input standard.

**S1's condition is adopted as the operative one**, being the strictest
and the only one that closes the loophole that matters:

> The complete form of f, including its normalization apart from the
> single declared calibration scale, must be derived independently of the
> measured inertial mass being inserted; f must be injective over the
> physically admitted state class; and its inversion must not contain
> hidden dependence on ambient v, the measured memory observable, the
> selected frequency band, **or an empirically adjusted N.**

**The N clause is the load-bearing one.** Without it, the obvious
degenerate route is to leave N unpinned and absorb it into the calibrated
value of τ_Sea — which would discharge Q2 by hiding it inside Q1. S1 saw
that and no other seat did. **Registered as a standing prohibition.**

**S1's four further inadmissible routes are adopted verbatim as
disqualifiers:** choosing f's form, exponent, coefficient or branch so
that the inferred τ_Sea passes 0.15; calibrating f from the same
force-lag or susceptibility data later presented as validation of 1B;
using several measured inertial masses to fit an otherwise underived
function and calling the result one-constant; and treating "inertia
requires lag" as sufficient to establish a quantitatively invertible f.

### §2.1 — THE CALIBRATION-COUNT PROBLEM: NEW, PROGRAMME-LEVEL, AND S1 IS RIGHT

**S1 alone raised this and it reaches past 1B into the programme's
headline claim.** CPP advertises a **single** calibration input, m_e.
S1's point, adopted:

> If the input is the already-declared m_e in its existing calibration
> role, this may remain a one-calibration construction. If a second
> measured inertial mass or an independently fitted macroscopic inertial
> coefficient is introduced, that is a **NEW calibration input** unless a
> derivation proves it is merely another measurement of the same
> universal scale. It must not be described as "of the same standing as
> m_e" while escaping the calibration count.

**The dispatch's own §4 Q1 language — "the same standing as m_e" — is
exactly the elision S1 names.** The worker wrote it and did not notice
that "same standing" and "no additional count" are different claims.
**Corrected here.** Registered as **OPEN-CALIB-COUNT-1**: any 1B closure
routing through m_inertial must either (a) demonstrate m_inertial is a
measurement of the same universal scale as m_e, or (b) declare the
programme's calibration count as two and propagate that to
`axiom-registry.md`, `predictions.md`, `theory-overview.md`,
`programme_orientation.md` and every zero-parameter claim that depends on
the one-constant framing.

**(b) is not a small bookkeeping consequence. It would touch the
programme's most-quoted structural claim.** No seat other than S1
noticed, and the worker did not either.

## §3 — Q2: N IS NOT PINNABLE FROM THE UPDATE RULE, 5–0 — S1'S NARROWER CONSEQUENCE ADOPTED, S5'S REASONING REJECTED

**Unanimous on the verdict**: per-Moment renewal of every CP's state does
not entail that a collective organization spanning a volume loses
dynamically relevant memory in one Moment. N = 1 does not follow from the
existence of a per-Moment update. **Adopted. k = N remains unpinned.**

**On the consequence the seats split, and S1's reading is adopted:**

> The dependency established is on a sufficiently specified **collective
> deterministic propagation/relaxation law**. If C23/C24 are currently the
> only committed artifacts supplying that law, then 1B is
> **operationally** blocked by their absence — but that is a **contingent
> repository dependency, not a logical identity** between 1B and
> OPEN-PR4-C23C24. A different exact or bounded deterministic derivation
> could still discharge 1B without a Gibbs treatment.

**This preserves K5 and it matters practically:** S2, S3, S4 and S5 all
wrote that 1B "inherits" OPEN-PR4-C23C24, which if enacted flatly would
make PR4-COMPLETED a hard gate on the last promotion item and hand the
FEM study back its monopoly — the exact revival the dispatch §5 forbade.

**S5's reasoning is REJECTED specifically.** S5 grounds the dependency in
*"the thermodynamic/statistical mechanics framework of C23/C24"* and
calls N *"analogous to a thermodynamic transport coefficient."* **K5 held
that a causal-retardation bound may be derivable from deterministic field
propagation WITHOUT Gibbs thermodynamics.** S5 reached the right verdict
on grounds that contradict a standing adjudication and that would, if
adopted, reinstate the FEM-only route. **Verdict accepted, reasoning not
enacted.** S3's "macroscopic/statistical property" phrasing carries the
same defect in milder form and is likewise not enacted.

## §4 — Q3: THE CORRECTION'S ORDER — AND THE WORKER'S RECONCILIATION IS DEAD

### Q3(i) — DISTINCT OBSERVABLES, 5–0. Adopted.

δ_mem = |F_mem|/|F_inst| (force ratio), δ_mem(k,ω) with φ_mem
(susceptibility ratio), and ε_mem = τ_Sea/τ_slow (timescale ratio) are
**distinct quantities with no presently derived conversion**. Relating
them requires specifying the kernel, forcing waveform, susceptibility-to-
force coupling, norm, geometry, state class and frequency band. **There
is no general identity δ_F = δ_χ = ε_mem.**

### Q3(ii) — THE 0.15 BAR ATTACHES TO THE FORCE RATIO, 5–0. Adopted.

K4 froze **δ_mem ≡ |F_mem|/|F_inst| ≤ 0.15** and said expressly that this
is not a velocity ratio. Per S1: **the text cannot bear reassignment of
that frozen threshold to ε_mem without a new adjudication or a derived
conversion theorem.**

**Consequence, and it corrects the worker:** the sentence at
`founders_voice/founder_reframing_bias_on_ringing_carrier_2026-07-29.md`
§3 — *"0.15 is the threshold on ε_mem, and k is what converts it to a v/c
bar"* — is **NON-GOVERNING and is corrected.** That sentence is **worker
prose inside a founders_voice file, not a founder ruling**; nothing in
the founder's mechanism rulings (2862–2867, 2870) is disturbed by
correcting it, and the distinction is stated explicitly so no later
reader mistakes this for overturning the founder.

**This is the 0.15 bar's THIRD misapplication.** 2855 applied it to a
centre-of-mass v/c; 2861 corrected it to ε_mem; **K4 attaches it to
δ_mem.** At Patch 2873 the worker saw this, declined to claim it, and
said only that it read K4 one way while 2864 §3 said another —
*"because the corpus does not say whether it intends ε_mem and δ_mem as
one object under two names."* **The panel has now said. The restraint was
correct and the claim is now made on the panel's authority rather than
the worker's.**

### Q3(ii-a) — A GAP S1 FOUND THAT NOBODY HAD REGISTERED

S1's intent when drafting the naming motion required a **complex**
acceptance observable — magnitude departure *and* phase lag — over a
physically anchored band. **K4's standalone text freezes a number only on
the normed force ratio and states no numerical phase threshold.**
Divergence between intent and text, disclosed by the author of both.

**Registered as OPEN-PHASE-THRESH-1:** a numerical phase-lag acceptance
limit must be recovered from the naming adjudication or freshly frozen.
Until it exists, **a 1B closure demonstrating only δ_mem ≤ 0.15 is
incomplete on S1's own construction**, because a model can present an
apparently instantaneous magnitude while carrying an unacceptable phase
delay. **New requirement on 1B, discovered this round.**

### Q3(iii) — THE WORKER'S RECONCILIATION IS REJECTED. S1 ALONE WAS RIGHT.

**The vote was 4–1 to ADOPT** the worker's candidate reconciliation
(finite kernel width with vanishing first temporal moment, permitting
ε_mem first order alongside δ_mem second order). **S2 adopted it outright
("The reconciliation is adopted"); S3 called it "entirely standard in
response theory"; S4 rendered it as a definitional entailment ("ε_mem is
a width measure → first-order; δ_mem is a moment measure → first moment
cancels"); S5 adopted it as reconciling both positions.**

**ADJUDICATED TO THE MINORITY. S1's rejection is adopted in full.** Three
independent grounds, all correct:

**(1) Finite width does not imply a vanishing first moment.** For a
normalized causal kernel K(t), χ(ω) = ∫₀^∞ K(t)e^{iωt}dt = 1 + iωμ₁ −
(ω²/2)μ₂ + …, with μ₁ = ∫₀^∞ t K(t)dt. **For an ordinary NONNEGATIVE
causal relaxation kernel with finite delay, μ₁ > 0 strictly.** A
finite-width kernel does not generically have zero first moment.
Obtaining μ₁ = 0 at nonzero width requires **signed or oscillatory
weights, cancellation among channels, or a differently centred
representation** — additional structure that has not been derived
anywhere in the record.

**(2) Spatial fore/aft cancellation is not temporal first-moment
cancellation.** A geometric cancellation between front and rear
contributions may kill the linear term in the net force after spatial
integration. **That is a different proposition from the temporal kernel's
first moment vanishing.** Either could hold; neither establishes the
other. **The worker's Q3(iii) conflated them** — the dispatch moved from
the founder's fore/aft antisymmetry (spatial) to a vanishing first moment
(temporal) in one step with nothing in between.

**(3) Coulomb-gauge bookkeeping is not a CPP symmetry proof.** An
instantaneous scalar potential in Coulomb gauge does not by itself prove
the physical CPP force response lacks an O(v/c) term. **Gauge
decomposition rearranges where interactions appear**; the physical
cancellation depends on the full longitudinal and transverse response
with correct relative weights — which 2838 itself records as
unestablished.

**Adopted replacement statement, S1's wording:**

> A first-order microscopic delay may coexist with a second-order net
> force correction **if** the full CPP response operator has a **proven
> linear-order cancellation.** At present that proof is absent.

**So: ε_mem first order and δ_mem second order remain COMPATIBLE IN
PRINCIPLE, and the specific mechanism offered to reconcile them is NOT
ADOPTED.** The founder's 2863 first-order ruling stands untouched. 2838's
cancellation stands as a conditional hypothesis and not as a finding.

### §4.1 — WHAT THIS EPISODE IS, STATED PLAINLY

The dispatch flagged this reconciliation as **the fifth favourable
convergence of the arc** and asked the panel to kill it rather than
ratify it. **Four seats ratified it on assertion; the one seat that had
authored the escape clause killed it with a two-line calculation.** The
worker constructed it, disclosed it as suspect, and was right to.

**The pattern-warning carried in the 2872 handover is now empirically
confirmed rather than merely prudent:** a favourable convergence in this
arc drew four ratifications and one derivation, and the derivation went
the other way. **Majority is not evidence.** Any future favourable
convergence gets S1's treatment — a computation — before it gets a vote.

### §4.2 — A SIXTH FAVOURABLE CONVERGENCE, FLAGGED AND EXPLICITLY NOT BANKED

S1 states that vanishing μ₁ at finite width requires **signed or
oscillatory weights**. **Patch 2870 found the Stage C coast is
NON-MONOTONIC — v decays, crosses zero, and oscillates.** An oscillatory
response is the signature of a signed kernel, so the record may already
contain the structure S1's condition demands.

**This is NOT banked, and the reasons are specific rather than
ritual.** 2870 declared its own diagnostic invalid for an oscillating
signal; the |v| values reached 10 in units where c = 1, i.e.
unphysical; the timestep was inherited from the ramp rather than chosen
for the coast branch; 2870 explicitly declined to make a third confident
claim about that file; and the observation lives in a **Tier-2 scalar
toy** measuring a bare point, which the same patch stressed does not
touch ε_mem or the ambient Sea. **It is also the sixth favourable
convergence of this arc and it arrived within one turn of the condition
that made it attractive — the exact signature the handover named.**

**Registered as a LEAD, not a result:** the computation that would make
it evidence is the **linear stability analysis about the steady coasting
solution** that 2870 specified and did not attempt — perturb v about the
coast, measure growth, cap |v| ≪ c, choose dt for the coast branch. Until
that runs, no claim about kernel sign is admissible.

## §5 — Q4: THE SPLIT DISSOLVES ON THE FULL PRECEDENT

**Apparent split 2–3:** S1 and S5 held the transverse-sector test a
**prerequisite**; S2, S3 and S4 held the cancellation admissible
**conditionally as a registered debt**.

**The split is narrower than it looks.** S1 expressly permits registering
a conditional branch and withholds only *evidentiary credit*; S3 states
1B "cannot be fully closed" until the debt is discharged; S4 states full
ledger entry requires a correctly scoped transverse measurement. **Four
of five converge on: conditional registration permitted, evidentiary
credit withheld, closure blocked.**

**S2 alone argued against prerequisite status, on precedent — and cited
half of it.** S2 wrote that the panel restored the Darwin bound while
recording the transverse sector's unmeasured status. **Verified and
accurate as far as it goes:** Patch 2849 D3 ruled **CPP-DARWIN
RESTORED-CONDITIONAL**, superseding 2848's
WITHDRAWN-PENDING-CONSTITUTIVE-CLOSURE. **But the same ruling continues:
it may NOT be cited as "proved."** The precedent therefore establishes
*conditional registration with an explicit prohibition on evidentiary
use* — **which is S1's ledger treatment, not S2's.** S2's own precedent
defeats S2's conclusion.

**ADOPTED LEDGER TREATMENT (S1's, reinforced by the Darwin precedent):**

| item | status |
|---|---|
| 2838 second-order branch | **REGISTERED CONDITIONAL HYPOTHESIS** |
| `open_k1_memory_1b_transverse_prereg.md` | **REQUIRED TEST** |
| present evidentiary credit toward 1B | **NONE** |
| 1B | **OPEN** |

**S4 and S5's citation of the mis-scoped transverse attempt is verified
accurate:** Patch 2841 (`open_k1_memory_1b_transverse_scoping_correction.md`)
narrowed what the 2840 verdict is a verdict *about*, on the founder's
correction that propagation is strictly at c, and states expressly that
it **does NOT restore the withdrawn bound.**

**S1's further requirement adopted:** because the naming motion required
a complex observable, the transverse test **cannot be a single
zero-frequency Coulomb match.** It must address response magnitude, phase
lag, their conversion into the force observable, the frozen physically
anchored band, and the stated state class. **This materially enlarges the
transverse preregistration**, which was scoped before OPEN-PHASE-THRESH-1
existed.

## §6 — NET EFFECT ON THE LEDGER

PR1 MET/retired · PR2 MET · PR3 MET · PR4-BARE MET-NEGATIVE
(PR4-COMPLETED = OPEN-PR4-C23C24) · PR5 MET · PR6 MET · **PR7 PARTIAL —
1A MET, 1B OPEN.** Six of seven. **B7 holds DM-1/DM-2/DM-3. Candidate
(B) 79.5% PROVISIONAL-FAVORABLE, untouched.**

**This round moved 1B further from closure, and that is the honest
summary.** Nothing was closed. Removed: the reconciliation that would
have delivered second-order suppression for free. Added: three new
requirements — **OPEN-PHASE-THRESH-1** (numerical phase threshold never
frozen), **OPEN-CALIB-COUNT-1** (calibration-count accounting for
m_inertial), and an enlarged transverse preregistration. **Retained
unpinned:** N, and the ambient physical Sea v/c.

**The 2864 stop-order is DISCHARGED.** Q1 and Q2 have returned, so the
prohibition on computing τ_Sea, N and v/c bounds lifts. **What it lifts
to is narrow:** Q1 permits m_inertial as calibration input **only after f
is derived and proven injective**, so no numerical τ_Sea may be inferred
from measured inertia until f exists. **The unblocked work is deriving f,
not evaluating it.**

## §7 — NEXT ACTIONS, IN ORDER

1. **Derive f in m_inertial = f(τ_Sea)** from committed substrate
   dynamics, to S1's adopted condition, with N NOT absorbed into the
   calibration. This is now 1B's critical path. Nothing numerical is
   computed until f exists and is proven injective on the admitted state
   class.
2. **OPEN-CALIB-COUNT-1** — settle whether m_inertial is a measurement of
   the same universal scale as m_e or a second calibration input, BEFORE
   any closure routes through it. If the latter, the propagation list in
   §2.1 is programme-wide.
3. **OPEN-PHASE-THRESH-1** — recover or freeze the numerical phase-lag
   acceptance limit. Cheap, and it gates the transverse test's scope.
4. **Enlarge the transverse preregistration** per §5 to a complex-response
   test over the frozen band.
5. **The 2870 linear stability analysis** — the only computation that
   could convert §4.2's lead into evidence about kernel sign. Run it to
   settle the question, NOT to confirm the sign.
6. **DM-1 v1.5 panel round; SF-6 pin corrections to panel; OPEN-DM-RELIC-1
   execution; SF-8 assembly.** All unchanged, all parallel-safe, none
   gated by the above.

**Not to be revived:** OPEN-SEA-DENSITY-1 as a 1B route; the C23/C24 FEM
study as the *only* route (S2/S3/S4/S5's flat "1B inherits
OPEN-PR4-C23C24" is not enacted — see §3).
