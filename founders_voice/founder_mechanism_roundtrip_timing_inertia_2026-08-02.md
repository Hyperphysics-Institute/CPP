# FOUNDER VERBATIM — ROUND-TRIP TIMING AS THE SOLE INERTIAL MECHANISM

**2 August 2026, Patch 2884. Captured in the same patch that acts on it,
per CONV-009 — the first case to arise under that convention.**

**A NEW FILE RATHER THAN AN APPENDIX**, because the mechanism it records
**supersedes** the one in
`founder_mechanism_volume_transfer_inertia_2026-08-01.md`, and appending
would leave that file's name misdescribing its own contents — the exact
defect this worker flagged two patches ago in
`founder_mechanism_ssv_asymmetry_retardation_2026-07-29.md`, whose title
still names a retardation account the founder had disavowed.

---

## §1 — The round-trip delay, identified

Founder, verbatim:

> I noted one thing in your summary of the debate that you reported that I
> had explicitly denied as the cause of the front-back differential: a
> delay in timing.
>
> - After the last examination of the differential in effect between
>   forward and rear volumes, I realize that there actually is a delay in
>   timing.
> - There is a one-increment delay in every DP's reflection back to the
>   CP-current when comparing the increment forward and increment
>   backward.
> - The increment at distance d backward will arrive 1 Moment after the
>   corresponding increment in the forward volume. Thus, there will be
>   mis-timing of effects reflected back onto the CP-current. Possibly
>   this is the source of the full storage of inertial volume (along with
>   the other angular effects we noted).

**Worker note — this is NOT a reversal of the 30 July disavowal.** Two
distinct delays are in play and only one was disavowed. The founder
rejected the **medium response lag** (the DP taking time to polarise,
τ_Sea). What he identifies here is a **round-trip propagation asymmetry**:
the CP moves during the signal's out-and-back, so fore and aft round trips
differ in length. These are independent and both may hold.

**Worker note — arithmetic confirmed, with one refinement.** Exactly:

    t_fwd = 2r/(c+v),   t_aft = 2r/(c−v),   Δt = 4rv/(c²−v²) ≈ 4rβ

**First order in v/c**, which is the order the mechanism requires. But it
is **not** a fixed one-increment offset — it **grows linearly with
distance**. Δt equals exactly one Moment at r = (1−β²)/(4β): about one
lattice spacing at β = 0.25, about 25 GP at β = 0.01. "One increment" is
right at close range and moderate speed.

## §2 — The founder rules it the SOLE mechanism

Worker question: *is the round-trip contribution governed by the same
ξ_arc, or does it introduce a second parameter?* Founder, verbatim:

> I think this idea replaces all the others because every DP-arc, on-axis
> or off-axis, has a corresponding effect that is related to the timing
> delay. So, we don't have to proliferate effects. I think this is the
> only effect. Computing it might be another story, but I'll leave it to
> you to turn that into an analytic representation of the time-delay
> system we just uncovered.

**Worker note — this is a significant strengthening of the conjecture and
the worker endorses it.** The round-trip asymmetry is **pure kinematics**:
it follows from the CP moving during a finite-speed round trip and assumes
**nothing** about arc dynamics. It therefore needs no collapse asymmetry,
no store-and-release lifecycle, and **no ξ_arc**. **CONJ-FP-1's single
free parameter is eliminated.** The founder also correctly resists
mechanism proliferation, which the worker had flagged as a threat to the
conjecture's falsifiability.

## §3 — What the computation returned (worker, same patch)

`code/2884_roundtrip_asymmetry.py`. Static Sea in the absolute frame; CP
at the origin now, moving +v; for each DP the **doubly-retarded** round
trip solved exactly.

**Result 1 — the founder's kinematics is confirmed.** The drive is
**exactly linear in β**: drive/β = −15.955, −15.954, −15.947, −15.923 at
β = 0.01, 0.02, 0.05, 0.10. Constant to four significant figures.

**Result 2 — the sign is the response's sign, inverted.** Modelled with an
**attractive** (induced-dipole) response the drive is **backward: drag.**
With a **repulsive** response it is **forward**, of exactly the form
required. The founder has said "repulsive" throughout, so this is
consistent with his picture — but it is now a single binary question
carrying the whole mechanism.

**Result 3 — and this is the hard one.** Under **Liénard–Wiechert**
propagation, which is what a wave equation produces for a uniformly moving
source, the drive is **exactly zero at every β** (10⁻¹⁷ across β = 0.01 to
0.4). The LW field points at the source's **instantaneous** position, so
the retardation is exactly compensated by the field direction.

**Therefore the mechanism requires CPP's relay to NOT reproduce
Liénard–Wiechert structure** — the DP must respond to how far the CP
*was*, not to where it *is*.

## §4 — THE CONSEQUENCE THAT EXCEEDS THIS CONJECTURE

If the relay **is** LW-like, the Sea exerts **no net drive on a coasting
CP at all** — so SSV_net = 0 for uniform motion, and the primitive
d = (|SSV_net|/SSV_abs)·PSR then gives **d = 0. Nothing could coast.**

**The programme therefore needs a non-LW relay for coasting itself to be
possible, independently of whether this inertia mechanism is correct.**
Condition B below is a question about the substrate's viability, not
merely about inertia. Registered as such.

## §5 — Status

**Two binary structural conditions replace one unmeasured continuous
parameter.** That is a strict improvement in falsifiability: neither
condition requires the DP-Sea density, which OPEN-SEA-DENSITY-1 could not
supply and which was the reason CONJ-FP-1 was filed as a conjecture rather
than pressed to a theorem.

- **CONDITION A** — the Sea's net response to a moving CP is **repulsive**.
- **CONDITION B** — the relay does **not** reproduce LW structure; the DP
  responds to the retarded separation, not the instantaneous position.

Founder's disposition, verbatim: *"It sounds like you've got this. Please
proceed!"*
