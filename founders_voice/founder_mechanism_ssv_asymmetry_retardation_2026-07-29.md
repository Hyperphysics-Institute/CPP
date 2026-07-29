# FOUNDER MECHANISM — THE SSV ASYMMETRY AS A PROPAGATION-DELAY EFFECT

**Patch 2866, 29 July 2026. Assessment of the founder's causal account
of how the front/back SSV differential is created and why it persists.**

---

## §1 — The mechanism, verbatim (operative claims)

> In CPP, the only reason that anything moves is a net SSV. It is an
> absolute frame system… (there is no memory, no velocity, just an
> amount of displacement each Moment, and that equals the appearance of
> velocity).
>
> 1) The SSV_forward is created by the initial accelerating force. This
> creates a persistent cloud of SSV_net acting on the CP… 2) The
> SSV_back is a secondary decelerating force opposing the acceleration
> for all the DP arc reasons we have discussed.
>
> Once the initial KE DP arc cloud is set up, the same asymmetrical
> structure of SSV_forward and SSV_rearward is persistent…
>
> The only method I can think of that would produce this asymmetry… is
> that the SSV_forward is set up by the accelerating push, which would
> have been acting on the rear side of the CP first/before the
> SSV_rearward was set up (since that is at a distance, and will happen
> on the next Moment). **So, it is the propagation delay between the
> side being pushed and the reaction of the space (by DP arcs) being
> created.**

## §2 — The acceleration half is right, and it is already the derived mechanism

**Retardation is exactly what 2496 measures.** Its §3 Stage B:

> *"the back-reaction tracks the **instantaneous** acceleration,
> **retarded only by the cloud light-crossing time σ/c**."*

The founder's "the near side is pushed first, the far side responds a
Moment later" **is** the cloud light-crossing retardation, stated in
physical language. During acceleration the mechanism is not merely
plausible — it is the one that produces F = κa in the existing
computation. **No dispute on this half.**

## §3 — The persistence half is where the mechanism strains

**A retardation asymmetry scales with the rate of change of the drive,
not with the drive.** For a source in *uniform* motion the retarded
configuration is just the boosted static configuration — in vacuum it
carries no fore/aft asymmetry at all. A propagation delay produces an
asymmetry **∝ a**, which vanishes when the push stops.

**A persistent asymmetry at constant v therefore cannot come from bare
retardation. It requires the medium to have a finite response time** —
a comoving polarization wake that lags because the Sea cannot
reorganise instantaneously. That is a real and standard effect.

**But now note what governs its size.** The fractional fore/aft
asymmetry of a wake behind a source crossing its own scale is

> asymmetry fraction ~ (medium response time)/(traversal time)
> = τ_Sea/(d_DP/v) = **ε_mem**

**The founder's persistent asymmetry IS ε_mem.** The quantity his
coasting mechanism requires to be *large enough to sustain motion* is
the same quantity clause 2 requires to be *small enough to be
subdominant*. These are not obviously incompatible — but they are the
same number, and the programme has been treating them as unrelated.

## §4 — The k = 1 convergence, and why the worker will not bank it

If the entire SSV_net arises from the lag-induced asymmetry, then
|SSV_net|/SSV_abs = ε_mem, and the CPP primitive v/c = |SSV_net|/SSV_abs
gives

> **ε_mem = v/c identically ⇒ k = 1**

and clause 2's threshold ε_mem < 0.15 becomes **exactly** the statement
that the Sea is non-relativistic.

**This is the same k = 1 that fell out of "each Moment" at 2864, now
arriving from an unrelated direction.** Two independent routes landing
on the same value is normally corroboration. **Here it is flagged, not
banked, for three reasons:**

1. **Circularity risk.** The identity holds only if *all* of SSV_net is
   lag-induced. The founder asserts this ("the only method I can think
   of"); it is not derived. If any part of SSV_net is non-lag in
   origin, the identity fails and k ≠ 1.
2. **It is the fifth consecutive turn** in which a route toward closing
   the programme's last gate has appeared. The register says this is
   the condition under which numbers get manufactured.
3. **It would close clause 2 in one line**, which is the standing
   disqualifier applied at 2864 and 2865 and applied again here.

## §5 — The direct conflict with 2496, and the crux question

**2496 finds Galilean compliance:** *"steady velocity is a comoving
pattern costing nothing,"* with the hold-phase residual at **2.9% of
peak back-reaction**, explicitly attributed to *"the time-staggering
floor of the integrator"* — i.e. an artifact expected to shrink under
refinement.

**The founder's mechanism requires that residual to be physical and to
scale with v.** Both cannot be right.

**But whether they even conflict depends on one definitional question,
and the worker cannot answer it:**

> **Does "SSV_net" in the coasting case denote (i) the net EXTERNAL
> force on the CP, or (ii) the total local field asymmetry including
> the comoving cloud's own structure?**

- **Under (i)** — the reading that matches 2496's F — coasting requires
  SSV_net → 0, the founder's persistent nonzero SSV_net is the finite-μ
  drag, and momentum drains as exp(−t/κμ). **Conflict, and the founder's
  coasting account needs revision.**
- **Under (ii)**, a comoving lossless cloud can carry a permanent
  internal asymmetry with **no drain and no external force**. Newton I
  is preserved, 2496's μ → ∞ limit and the founder's "persistent cloud"
  describe the same object, and **there is no conflict at all** — only
  two accountings of one physics.

**Reading (ii) reconciles everything. That is precisely why the worker
does not assert it.** It is a founder physics question about his own
primitive and it is put back.

## §6 — The decisive empirical test, specified but NOT run

`flagship_papers/electromagnetism/code/2496_sf6_inertia_impulse.py`
already measures the disputed quantity as **`F_hold`** — the mean
back-reaction during the constant-velocity hold phase.

**Test:** sweep the integrator timestep and the hold velocity.

- **F_hold → 0 under dt-refinement, independent of v** ⇒ artifact.
  2496 stands, the founder's persistent-asymmetry coasting account
  needs revision.
- **F_hold converges to a nonzero value scaling with v** ⇒ physical.
  The founder's mechanism is confirmed in-model, **and universal drag
  on all coasting matter becomes an immediate observational
  constraint.**

**Deliberately not run this turn.** Under §5 reading (ii) the test
measures an *external* force and therefore does not bear on an
*internal* cloud asymmetry — **the test's meaning depends on the crux
question, so running it first would produce a number whose
interpretation is still open, and this session's record shows what the
worker does with numbers whose interpretation is open.** Crux first,
test second.

## §7 — What is genuinely new here

Stripped of the corrections: **the founder has supplied the first
causal account of *why* the fore/aft asymmetry exists rather than
merely asserting that it does**, and it grounds that asymmetry in
retardation — a mechanism the programme has already measured on the
acceleration side. **If reading (ii) holds and the identity of §3
survives, then the DM campaign's last open gate and the SF-6 inertia
mechanism are the same physics viewed from two ends**, and ε_mem is not
an obstacle to be bounded but a quantity the programme already computes
under another name.

**That is a conditional worth testing, not a result. 1B remains OPEN.
Six of seven. B7 holds. No number computed.**
