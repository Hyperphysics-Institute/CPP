# PATCH 2870 — A FAILED TEST, A PARTIAL RETRACTION, AND ONE FLAG

**29 July 2026. The worker designed a test to locate the knife-edge,
ran it, and it did not work. Reported as a failure rather than
presented with the numbers it produced.**

---

## §1 — The founder's three elaborations, recorded

> *"CPP's use of the word force is shorthand for SSV_net, since there is
> no pushing or pulling in CPP, only an amount of displacement in a
> Moment… **There is no self-force in CPP**; there is a message sent out
> for others to respond to, but nothing that powers the CP to
> locomote."*

**This is more than terminology and it bears on 2869 §2.** The worker
argued there that a runaway draws on *divergent bare-point
self-energy*, citing Abraham–Lorentz. **That divergence is a
continuum-field-theory artifact.** If CPP has no self-action — only a
declaration to which other entities respond, their responses re-entering
as SSV_net at the CP's location — and if the substrate is discrete, then
**there is no self-energy integral to diverge.** The reservoir the
worker called unbounded may be bounded by the lattice.

**2869 §2's argument is accordingly weakened**, and the founder's
conservation objection recovers some of the force the worker denied it.
`Fs` in the 2496 toy is a *scalar-field back-reaction*, and whether it
corresponds to anything in CPP proper is now an open question rather
than an assumed correspondence.

Also recorded: the founder's point that eternal constant velocity
implies **cyclic reuse** of the initial input rather than draw-down of a
store. That is a genuine empirical constraint on the mechanism.

## §2 — 2869 §4 partially retracted, and the retraction's stated reason was ALSO wrong

2869 §4 claimed Stage B and Stage C are "opposite signs for what should
be the same physics."

**The worker's intended retraction was that `v = mu*Fs` makes Fs > 0
mandatory during coast. That reasoning is wrong** — v can go negative,
so Fs can too. **And it does:** at μ = 10, Fs runs from +6.704e-05 to
−9.720e-05 during the coast. There *is* sign reversal.

**But the original §4 framing was also wrong.** The coast is not a
sign-inverted version of the hold; it is **non-monotonic** — v decays,
crosses zero, and oscillates. Neither "forward self-force" nor
"exponential decay" describes it fully.

**Net: §4's claim of a Stage B/C contradiction is withdrawn. What is
actually there is an oscillatory coast that neither the pin's summary
nor 2869 characterised correctly.**

## §3 — THE TEST FAILED

Prediction, arithmetic and unchanged: with α = F_hold/v_f = 9.3661e-04,
the primitive v = μ·α·v gives marginality at

> **μ_crit = 1/α = 1067.7**

**The numerical test of that prediction is invalid.** Raw output:

| μ | μ/μ_crit | v_init | v_final |
|---|---|---|---|
| 266.9 | 0.250 | 1.79e-02 | **−5.19** |
| 800.8 | 0.750 | 5.37e-02 | **+6.00** |
| 1067.7 | 1.000 | 7.16e-02 | **−1.11** |
| 2135.4 | 2.000 | 1.43e-01 | **−10.09** |

**Two independent disqualifiers:**

1. **|v| reaches 10 in units where c = 1.** The runs are unphysical
   well before μ_crit is approached. Whatever these branches are doing,
   it is not the physics the prediction concerns.
2. **The diagnostic was wrong for the signal.** `v_final/v_init` is
   meaningless for a non-monotonic oscillating quantity. Alternating
   signs and ratios of −290, +112, −16, −70 are the signature of a bad
   metric, not of a located transition.

**μ_crit = 1067.7 therefore remains an untested arithmetic
consequence.** The worker will not quote the sweep as evidence for or
against it in either direction.

**What the test would have needed:** a linear stability analysis about
the steady coasting solution — perturb v and measure whether the
perturbation grows — with a velocity cap enforcing |v| ≪ c and a
timestep chosen for the coast branch rather than inherited from the
ramp. That is a different computation and it is not attempted here.

## §4 — One flag on the shipped result, stated narrowly

2496's coast fit selects its window with `m = (tv > tv[0] + 6) & (vv >
1e-4)` — i.e. it **excludes the region where v falls below 1e-4**, which
is exactly where the sign reversal of §2 occurs.

**Rejecting a noise floor is legitimate practice and the filter is
visible in the code.** But two consequences follow and neither is stated
in the pin:

- The reported coast is **a fit to a truncated monotone segment**, not a
  characterisation of the full coast, which oscillates.
- At μ = 10 the coast *begins* at v ≈ 6.7e-04, less than one decade
  above the 1e-4 cut. **τ = 7.87 is fitted across under one decade of
  decay.**

**This is flagged for the panel, not asserted as an error.** The worker
has been wrong twice in three patches about this file and is not making
a third confident claim.

## §5 — Position

**Retracted this patch:** 2869 §4's Stage B/C contradiction; 2869 §2's
divergent-self-energy argument (weakened by §1); the worker's own
proposed retraction reasoning (§2).

**Standing:** 2868's refinement result — F_hold flat under 4× dt and
2× σ refinement, linear in v, forward. That is unaffected by any of
the above and remains the correction to the pin's §4 attribution.

**Open and now sharper in statement, no closer in fact:** whether
μα = 1. The arithmetic gives μ_crit = 1067.7 and the model goes
unphysical before it can be probed there.

**1B OPEN. Six of seven. B7 holds. Nothing here touches ε_mem or the
ambient Sea.**
