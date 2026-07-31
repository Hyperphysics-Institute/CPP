# ⚠ CONJ-FP-1 MAJOR REVISION — PATCH 2884: MECHANISM REPLACED, FREE PARAMETER ELIMINATED

**The founder has ruled the ROUND-TRIP TIMING ASYMMETRY the sole
mechanism, superseding the volume-transfer/slab account below. Source:
`founders_voice/founder_mechanism_roundtrip_timing_inertia_2026-08-02.md`.
Computation: `../code/2884_roundtrip_asymmetry.py`.**

**FILENAME RETAINED DELIBERATELY.** This path is the registered pointer
for CONJ-FP-1 in `frontier_sectors/CONJ.md`; renaming it would break the
registry reference. The banner carries the correction instead. *(Noted
because this worker criticised exactly this defect — a filename
misdescribing its contents — two patches ago.)*

## What changed

**ξ_arc IS ELIMINATED.** The round-trip asymmetry is **pure kinematics**:
it follows from the CP moving during a finite-speed out-and-back and
assumes nothing about arc dynamics. **No collapse asymmetry, no
store-and-release lifecycle, no arc/spacing ratio, and no DP-Sea density
are required.** LINK 1 of §3 below is **RETIRED**, and with it Route 1
(the AUTOMATON ξ_arc measurement) as a *gating* item.

**Replaced by two BINARY structural conditions**, both testable without
any density measurement:

| | condition | status |
|---|---|---|
| **A** | the Sea's net response to a moving CP is **REPULSIVE** (attractive gives drag of the same magnitude) | founder asserts; untested |
| **B** | the relay does **NOT** reproduce Liénard–Wiechert structure — the DP responds to the **retarded** separation, not the instantaneous position | **untested; see escalation** |

**Two binary questions in place of one unmeasured continuous parameter is
a strict gain in falsifiability**, and it removes the dependence on
OPEN-SEA-DENSITY-1 that was the stated reason for filing as a conjecture.

## What survives unchanged

**LINK 2** (the marginality condition, §2 below) and **LINK 3** (stability
of the coasting family — B1, still the worker's own job) are untouched.
The drive's magnitude must still land exactly on the self-consistency
condition, and that family must still be neutrally stable.

## The computed result

`2884_roundtrip_asymmetry.py`, static Sea in the absolute frame, CP at the
origin moving +v, doubly-retarded round trip solved exactly per DP:

- **Exactly linear in β** — drive/β = −15.955, −15.954, −15.947, −15.923
  at β = 0.01, 0.02, 0.05, 0.10. Constant to four significant figures.
  **The founder's kinematic claim is confirmed.**
- **Sign = inverse of the response's sign.** Attractive → backward (drag).
  Repulsive → forward, of exactly the required form.
- **Under Liénard–Wiechert propagation: EXACTLY ZERO at every β** (10⁻¹⁷
  across β = 0.01–0.4). The LW field of a uniformly moving source points
  at its **instantaneous** position, so retardation is exactly compensated
  by field direction. **This is also the computation's self-validation** —
  it reproduces the known null result for a uniformly moving charge, which
  is what licenses trusting case A.

## ESCALATION: CONDITION B EXCEEDS THIS CONJECTURE

**If the relay IS LW-like, the Sea exerts no net drive on a coasting CP at
all.** Then SSV_net = 0 for uniform motion, and the CPP primitive
d = (|SSV_net|/SSV_abs)·PSR gives **d = 0 — nothing could coast.**

**The programme therefore requires a non-LW relay for COASTING ITSELF to
be possible, independently of whether this inertia mechanism is correct.**
Condition B is a question about the **substrate's viability**, not merely
about inertia, and it is registered at that level.

## New executable route, replacing Route 1

**AUTOMATON MOVING-SOURCE TEST.** The arc measured the **static** Coulomb
profile to ±0.4% under two independent relays. **Whether a MOVING source
produces a field pointing at its instantaneous or its retarded position
has never been run.** It is a defined simulation on an existing, committed
engine (`2802_automaton2_engine.py`), needs no new physics, and settles
Condition B — and with it, whether coasting is possible in the substrate
at all.

---

# CONJ-FP-1 — THE VOLUME-TRANSFER MECHANISM OF INERTIAL MAINTENANCE

**Founder mechanism, developed 29 July – 1 August 2026 across the
founders_voice inertia arc and the subsequent dialogue. Registered as a
CONJECTURE at Patch 2880 on the founder's own motion, after the mechanism
was traced to a dependence on a substrate quantity the programme has not
measured.**

**This is not a derivation and is not presented as one. It is a
mechanism with three named unproven links, each with an executable route
to settlement.**

---

## §1 — THE MECHANISM

Define the **Position Plane**: the plane through the Conscious Point,
normal to its axis of motion.

1. DP arcs **ahead** of the Position Plane are **charging** — being forced
   apart by the approaching CP — and while charging they push **rearward**,
   opposing advance.
2. DP arcs **behind** the Position Plane are **discharging** — collapsing
   back — and while discharging they push **forward**.
3. These two populations would **cancel exactly**, and the system would be
   static, were their volumes equal.
4. They are not equal. Each Moment the CP advances by exactly one
   displacement increment, so a **slab of space one increment thick**
   crosses from the charging side to the discharging side.
5. **That transferred slab is the entire net drive.** Everything else
   cancels.
6. A faster CP advances the plane further per Moment, so a thicker slab
   transfers, so the drive is larger — the drive scales with the
   displacement increment, i.e. with v.

**Founder, verbatim:** *"That single, one-moment-wide volume of space is
the only difference between the volume of DP-arcs in front of the Position
Plane that are charging and pushing back on the CP, and the volume of
DP-arcs behind the Position Plane that are discharging and pushing
forward… It truly would be a static system if the charging and discharging
DP-arcs were the same volume."*

### §1.1 — Why the fore/aft populations do not cancel

Compression accumulates on approach and is **maximal at closest approach**,
which is the Position Plane itself. So an arc just ahead is still charging
toward its maximum; an arc just behind has passed maximum and is
collapsing. Fore and aft are at **different points of the same lifecycle**,
not at arbitrarily different amplitudes.

**The arc is a store-and-release element, not a polarization chasing the
local field.** This is the founder's explicit answer (1 Aug) and it is
load-bearing: it is what distinguishes this mechanism from a relaxing
dielectric, for which the net effect is drag (see §4, Route 1's negative
result).

### §1.2 — Why the sign can be forward

An arc's axial polarization must **reverse** as it crosses the plane
(the CP's field points forward ahead of it, backward behind it). It cannot
reverse instantly. An arc just past the plane therefore retains its
**fore**-configuration polarization, which places its **like pole nearer
the CP** — giving **repulsion**, which drives the CP forward.

**This is geometrically sound and is not ruled out by conventional medium
physics**, contrary to a worker objection raised and withdrawn on 1 Aug.
The textbook drag result assumes the polarization has *equilibrated* to
its local field; the stale, anti-aligned region just past the plane is a
different regime and the force genuinely reverses in it.

## §2 — CONSEQUENCE: WHAT NEWTON I BECOMES

Write the drive as SSV_net = C·d, with C collecting arc number density,
the Position Plane's interacting cross-section, and the forward impulse
per discharging arc. Combine with the CPP primitive
d = (SSV_net/SSV_abs)·PSR:

> **C · PSR = SSV_abs**

The displacement **cancels**. Every velocity is then a solution — which is
Newton I — **but only if that single condition on the coefficients holds.**
Above it, the CP accelerates itself (runaway); below it, motion decays
(drag).

**This is not circular.** It relates three independently meaningful
quantities. It is, however, a **marginality** condition, and the mechanism
as stated does not force it.

**Flagged, NOT banked:** PSR is *defined* as the displacement at full
coherence, i.e. d = PSR exactly when SSV_net = SSV_abs. Evaluating
SSV_net = C·d at d = PSR gives C·PSR = SSV_abs directly. **The condition
may therefore be forced by the definition of PSR itself**, in which case
Newton I follows from the primitive with nothing tuned. This is not
asserted: it would be the seventh favourable convergence of this arc, it
arrived one turn after it was wanted, and the previous six all died. It is
**Route 2 below**, not a result.

## §3 — THE THREE UNPROVEN LINKS

**LINK 1 — THE COLLAPSE ASYMMETRY.** A collapsing ± pair returns to its
own centre of mass, and a **symmetric** collapse delivers **zero net
momentum** to anything. For the discharge to drive the CP forward, the
collapse must be asymmetric — one pole travelling further than the other,
shifting the pair's centre of mass rearward. The two poles do sit at
different distances from the CP, so an asymmetry exists; but in a
multipole treatment it is suppressed by

> **ξ_arc ≡ (fully-charged arc separation) / (inter-DP spacing)**

**If ξ_arc ≪ 1 the suppression bites and the discharge cannot supply the
drive. If ξ_arc ~ 1 the multipole expansion fails, the suppression does
not apply, and the mechanism is clear.** ξ_arc is the conjecture's single
free parameter and **the programme has not measured it.**

**LINK 2 — THE MARGINALITY CONDITION.** C·PSR = SSV_abs is required and
has never been computed. See §2.

**LINK 3 — STABILITY OF THE COASTING FAMILY.** Self-consistency at every
v is **necessary but not sufficient** for Newton I. An equation satisfied
at all velocities says nothing about whether a velocity *persists*. Newton
I additionally requires the coasting family to be **neutrally stable** —
not attracting (drag), not repelling (runaway). **Never computed.**

## §4 — THREE EXECUTABLE ROUTES TO SETTLEMENT

**ROUTE 1 — MEASURE ξ_arc FROM BANKED AUTOMATON DATA.** AUTOMATON-2
measured the ZBW turning radii at the lattice's **√2 and 2√2** in a run of
**definite DP density**. Both quantities are in the same units from the
same run, so **ξ_arc is computable from data already banked**, and those
results are **L-4 exempt** from the arc-closure limitations. The
density-dependence characterisation is **already a registered item**, so
the question "does ξ_arc survive across densities?" is scheduled work, not
an unanswerable one.

*Indication only, explicitly NOT banked:* the pair correlation shows the
gas is entirely unlike pairs at those radii with **no like-charge contact
structure**, which reads as ξ_arc ~ 1 rather than ξ_arc ≪ 1 — the regime
in which LINK 1 does not bite. **This is an inference from a correlation
function, not a spacing measurement, and it would be the ninth favourable
turn of this arc.**

**ROUTE 2 — TEST WHETHER C·PSR = SSV_abs IS FORCED.** Compute C from the
arc physics and check against the definition of PSR (§2). **Note that the
arc number density plausibly appears in BOTH C and SSV_abs and may
cancel**, in which case the marginality condition is density-independent
and the hardest input drops out. Not verified.

**ROUTE 3 — THE LINEAR STABILITY ANALYSIS (B1).** Perturb v about the
steady coasting solution, measure whether the perturbation grows, enforce
|v| ≪ c, and choose the timestep for the coast branch rather than
inheriting it from the ramp. **This has been dispatched to the review panel
twice and returned 5–0 REASONED-UNVERIFIED both times — no seat has an
execution environment. It is the worker's own job.** It is not a loose end:
**it is the test of LINK 3 and therefore of the conjecture.**

## §5 — THE OVER-DETERMINATION PROTOCOL (pre-registered)

The founder proposes fixing ξ_arc and cross-checking it against other
phenomena. **That is legitimate triangulation only under a condition, which
is registered here in advance:**

> **ξ_arc is to be fixed ONCE, by Route 1, and must thereafter PREDICT
> the other phenomena with nothing further adjustable.**

If tunneling rates, Schrödinger compliance, and orbital structure each
receive their own free parameter, that is **not triangulation — it is three
fits.** The distinguishing property is that **ξ_arc must be
over-determined**: several independent phenomena must demand the *same*
value. This is the same pre-registration discipline the programme applies
to gates, applied to a postulate.

**Nominated cross-checks** (to be predicted, not fitted): barrier
tunneling rates; Schrödinger compliance of orbital electrons; ZBW
spectral signature at physical density.

## §6 — COST TO THE PROGRAMME'S CALIBRATION COUNT

**Registered honestly rather than absorbed.** CPP advertises a **single**
calibration input, m_e. **A postulate carrying a free parameter is a
second measured input unless ξ_arc is derived or shown to be a measurement
of an already-declared scale.** This is the accounting S1 raised at
OPEN-CALIB-COUNT-1 and it applies here directly. **If CONJ-FP-1 is
promoted with ξ_arc fitted rather than derived, the programme's
one-constant framing must be updated across
`axiom-registry.md`, `predictions.md`, `theory-overview.md`,
`programme_orientation.md` and every zero-parameter claim resting on it.**

Better to declare two inputs than to have a reviewer find the second.

## §7 — WHAT THIS MECHANISM REPLACES, AND WHY THAT MATTERS

The prior account of inertia — `sf6_inertia_impulse_pin.md`, F = κa from
DP-sea back-reaction — was **demoted 4–1 by the CONV-001 panel (Patches
2876, 2879)** to a scalar-toy result pending
OPEN-FSELF-CORRESPONDENCE-1, on the founder's own ruling that **there is
no self-force in CPP.**

**Inspection of the 2496 code at Patch 2880 shows why the demotion was
correct and goes further than the panel knew.** 2496 integrates
`phi_new = 2*phi - phi_old + dt*dt*(c*c*lap(phi) + g*rho)` — a **scalar
wave field** propagating at c, with the self-force read off as the field
against the source's own gradient. **It contains no arcs, no charge
separation, no charging, no discharge, and NO RELAXATION TIME.** Its only
memory is retardation.

**Two consequences, both material:**

1. **The forward F_hold measured at Patch 2868 is not evidence for this
   conjecture.** It is a wave-toy self-interaction and contains none of the
   store-and-release structure the mechanism requires. The worker offered
   it as in-model support on 1 Aug and **withdraws it.**
2. **ε_mem is untested by 2496 as well**, since ε_mem = τ_Sea/τ_slow is a
   *relaxation* ratio and 2496 has no relaxation time. **The bridge the
   inertia arc has been assuming between the SF-6 pin and dark-matter
   clause 2 rests on a model containing neither of the two quantities it
   is supposed to connect.** Registered as a gap.

**No existing artifact can settle the sign, because none contains arcs.**
What is needed is a model with discrete ± pairs that charge on approach
and release on recession, with the collapse asymmetry resolved rather than
assumed — at minimum the vector redo owed at pin §5.7(b), and in truth
more than that.

## §8 — THE WORKER'S ASSESSMENT, ON RECORD

**This is the most coherent account of inertia the programme has had.** It
makes inertia a property of the Sea rather than of the particle, which
follows the founder's own 7 July no-carried-velocity ruling and is more
elemental than what SF-6 currently ships. It supplies the **first causal
account of why the fore/aft asymmetry exists** rather than asserting it.
And it correctly requires that steady motion be **cyclic reuse rather than
draw-down of a store**.

It survives every objection raised against it except LINK 1, which is
answerable. **Calling it a conjecture is correct. Calling it finished would
overclaim the derivation and simultaneously underclaim how close the
remaining questions are to being computable.**
