# CONV-001 — SF-6 INERTIA PIN: CORRECTIONS TO A SHIPPED DEVELOPMENT ARTIFACT — DISPATCH (Patch 2875)

**Handover next-action item 3. Four corrections to `sketches/sf6_inertia_impulse_pin.md`,
of which one refutes a compliance claim, one substantially WITHDRAWS a flag
the worker raised against its own file, one adds a founder-ruled scope
caveat, and one kills a lead the worker registered at Patch 2874 §4.2
yesterday.**

**FIRST, THE SCOPE CORRECTION THAT SHRINKS THIS ITEM.** The 2872 handover
recorded this as *"a shipped Tier-2 result's compliance claim was
refuted."* **The refuted claim is NOT in the shipped paper.**
`sf-6_electromagnetism.tex` (v1.0, 21 June 2026) was grepped this patch
for `galilean`, `time-stagger`, `hold residual`, `2.9%`, `coast` and
`newton's first`: **zero matches.** The Galilean-compliance attribution
existed only in the development sketch. **SF-6 v1.0 does NOT require
re-versioning or re-shipping on this account**, and the panel is not
being asked to authorise one. What SF-6 v1.0 does still carry, unchanged
since it shipped, is a parameter-**tuned** effective-inertial-mass
passage (`.tex` line 213, *"in the high-v limit and by tuning the model
parameters"*) — which the pin's §6 proposed to replace. That proposal is
affected by the corrections below and is question A3.

---

## §1 — CORRECTION 1 (Patch 2868): THE COMPLIANCE ATTRIBUTION IS REFUTED. STANDS.

Pin §4 read: the 2.9% hold residual is *"Galilean compliance in-model;
the residual is the time-staggering floor of the integrator."*

**Refuted in the model's own numbers** by
`code/2868_hold_force_refinement.py`: F_hold is flat under 4× dt
refinement, flat under 2× σ refinement, exactly linear in v (F_hold/v
constant to 0.6% across 4× in v), and **points FORWARD, along the
motion** — not a drag. It is neither a temporal nor a spatial
discretization artifact. The quoted *ratio* rises to 6.0% at σ = 3.0 only
because the denominator halves while the numerator sits still — a reading
trap in the original presentation.

**Galilean compliance is not demonstrated there.** The founder's sign was
confirmed against the worker, which had argued from textbook
induced-dipole physics that a lagging cloud pulls backward. Correction
banner applied in place at 2868; unchanged by this patch.

## §2 — CORRECTION 2 (Patch 2875): THE WORKER'S OWN COAST-FIT FLAG IS SUBSTANTIALLY WITHDRAWN

At 2870 the worker flagged, narrowly and explicitly **not** as an error,
that 2496's Stage C coast fit selects its window with
`(tv > tv[0]+6) & (vv > 1e-4)`, excluding the region where sign reversal
occurs, and stated that *"at μ = 10 the coast begins at v = 6.7e-4, less
than one decade above the 1e-4 cut, so τ = 7.87 is fitted across under
one decade of decay."*

**Measured rather than characterised, at
`code/2875_coast_full_diagnostic.py`. Both published τ values reproduce
exactly. On all three points:**

**(i) "Under one decade" is FALSE.** The fit window spans **2.172
decades** at μ = 10 and **1.090** at μ = 25. The worker read the trace's
first sample as the fit's starting value; the window opens at `tv[0]+6`,
by which time v has risen to its peak. **The premise was right and the
inference was wrong.**

**(ii) "The coast oscillates" is NOT SUPPORTED.** Fitting a damped
oscillation against a pure exponential over the full coast returns
best-fit angular frequencies **indistinguishable from zero** at both
mobilities, with RMS residual improvements under 2×, and the improvement
attributable to the envelope rather than to any oscillation. **There is
one zero crossing at μ = 10 and none at μ = 25.** The coast is
**non-monotone**, which is a different and weaker statement than
oscillatory.

**(iii) The window choice is legitimate and is now understood.**
`tv > tv[0]+6` excludes a **release spin-up transient** — at release the
CP switches to v = μF_s from rest and is driven up by stored field
momentum before decaying — and `vv > 1e-4` removes the sub-noise tail
and, at μ = 10, the single late crossing. **Note additionally that
`np.log(vv)` is undefined for vv ≤ 0, so the estimator structurally
cannot span a sign change; the filter is doing double duty.**

**What remains owed is prose, not a number:** Stage C's description says
v(t) ≈ v₀exp(−t/κμ), which describes neither the spin-up nor the μ = 10
tail crossing. Pin amended accordingly.

**This is the third worker characterisation of this one file to require
correction in four patches** (the "integrator artifact" gloss; the Stage
B/C sign contradiction; now the one-decade claim). 2870 warned it was at
risk of a third confident claim and then made one.

## §3 — CORRECTION 3: THE FOUNDER'S NO-SELF-FORCE RULING, ADDED AS A SCOPE CAVEAT

Founder, 2026-07-29: *"CPP's use of the word force is shorthand for
SSV_net… THERE IS NO SELF-FORCE IN CPP; there is a message sent out for
others to respond to, but nothing that powers the CP to locomote."*

Two consequences now recorded at pin §5.7(a):

1. **The Abraham–Lorentz framing is WEAKENED.** The A–L divergence is an
   artifact of a point's self-energy integral in continuum field theory. A
   **discrete** substrate has no such integral to diverge, so the
   reservoir may be bounded by the lattice and the runaway may not survive
   in CPP proper at all.
2. **Whether this toy's F_self corresponds to any CPP quantity is now an
   OPEN QUESTION, not an assumed correspondence.** SSV_net is others'
   responses re-entering at the CP's location, which is not obviously what
   F_self measures. Until settled, §5.7(a) is a statement about the scalar
   toy only.

## §4 — CORRECTION 4: A LEAD REGISTERED YESTERDAY IS DEAD

Patch 2874 §4.2 registered a lead: S1's rejection of the worker's
kernel reconciliation requires **signed or oscillatory weights** for a
vanishing first moment, and 2870's non-monotonic coast looked like it
might supply exactly that structure. It was flagged as the **sixth
favourable convergence** of the arc and explicitly not banked.

**§2(ii) kills it.** The measured frequency is indistinguishable from
zero and the oscillatory model earns no decisive improvement. **There is
no oscillation here to serve as evidence of a signed kernel.**
Withdrawn one patch after registration, by the computation that was
named as the condition for banking it. **The lead's death costs the
programme nothing, because it was never counted.**

## §5 — QUESTIONS, SPLIT BY TYPE

**PROCEDURAL NOTE, NEW THIS ROUND AND BINDING.** At the clause-2
adjudication (2874) a **mathematical** question — whether a kernel's
first temporal moment vanishes — was put in a format that invited
adjudication, and four seats voted for a proposition that the fifth
refuted with a two-line calculation. **The failure was the dispatch's,
not the seats'.** Questions are therefore now typed, and the type governs
what counts as an answer.

### TYPE A — ADJUDICATION. Seat judgment IS the product.

**A1 — Does §2's withdrawal go far enough, or too far?** The worker has
now been wrong about this file three times in four patches, twice in the
pessimistic direction and once optimistic. §2 withdraws most of a flag
the worker itself raised. **A seat should consider whether the worker is
now over-correcting toward exoneration of its own shipped numbers**, and
say so if it thinks the residual caveat (spin-up prose, μ = 10 crossing)
is too thin.

**A2 — What is the status of §3's correspondence question?** If it is
open whether the toy's F_self corresponds to any CPP quantity, then what
exactly does the pin's headline result — F = κa read Momentwise off the
substrate — establish about CPP? Options the worker sees, without
choosing: (a) it stands as a substrate-mechanism result because κ is
pinned by statics independently of F_self's interpretation; (b) it is
demoted to a scalar-toy analogue pending the correspondence; (c) the
correspondence is not actually in doubt and the founder's ruling bears
only on the runaway. **The worker does not propose an answer.**

**A3 — Does the pin still buy SF-6 what §6 says it buys?** Pin §6 claims
the paper's parameter-tuned inertial-mass passage can be replaced by (i)
the statics-pinned open-cloud coefficient κ = (2/3)U/c² and (ii) the Laue
coefficient-1 result for closed standing patterns. **(i) appears
untouched** — κ is statics-pinned, six readings agree, and 2868 did not
bear on it. **(ii) is a theorem invocation whose CPP instantiation (the
SF-1 cage under this protocol) remains owed at §5.7(d).** But the
open-cloud case now describes an object measured to sit on the runaway
side. **Is the §6 replacement still authorised, authorised in part, or
withdrawn pending §5.7(d)?**

### TYPE B — DERIVATION. Only a computation counts. A VOTE IS INADMISSIBLE.

**B1 — Does the coasting solution have a growing perturbation?** This is
2870's specified and never-attempted test, and it is the only route to
the μα knife-edge. Required: a **linear stability analysis about the
steady coasting solution** — perturb v about the coast, measure whether
the perturbation grows, enforce |v| ≪ c so the branch stays physical, and
choose dt for the coast branch rather than inheriting it from the ramp.
Arithmetic gives μ_crit = 1/α = 1067.7 from α = F_hold/v_f = 9.3661e-4;
**that number is an untested consequence and the earlier numerical test
of it FAILED on two independent disqualifiers** (|v| reached 10 in units
where c = 1; the endpoint-ratio diagnostic is meaningless for a
non-monotone signal). **A seat that has not run a stability analysis
should say so and answer nothing else here.** Reasoned opinion on B1 is
not an answer to B1.

## §6 — Standing

**Nothing in this dispatch touches 1B, ε_mem, τ_Sea, N, or the ambient
Sea.** 1B OPEN; PR7 PARTIAL; six of seven; B7 holds DM-1/2/3; Candidate
(B) 79.5% untouched. **SF-6 v1.0 stands as shipped and is not proposed
for re-version.** The vector redo owed at §5.7(b) is NOT discharged; the
SF-1 cage computation at §5.7(d) is NOT discharged.

## §7 — Execution integrity

**CONV-007 applies** (registered Patch 2874 after the previous round's key
was found published in both a commit message and the target's own
docstring, voiding the ruling). This key has been checked against
`git log --all --format=%B` and against every committed prose file and
docstring, and does not appear in any of them.

**Withheld key.** From `code/2875_coast_full_diagnostic.py`, run at the
published parameters: report **(i)** the number of samples the published
window retains, out of the total, at each of μ = 10 and μ = 25; and
**(ii)** the value of v at the final sample of the coast at μ = 25, to
four significant figures. Expected values are withheld and held by the
worker.

Seats not executing declare **REASONED-UNVERIFIED with reasons**. Four of
five seats reported retrieval failure last round; that is costless and
preferable to a reported number that was not computed. **Four consecutive
clean rounds stand.**

**Seats:** S1 (GPT), S2 (Grok), S3 (Gemini), S4 (Copilot), S5 (DeepSeek).
Answer A1–A3 in any order. **On B1, silence or REASONED-UNVERIFIED is the
correct return unless a stability analysis was actually performed.**
