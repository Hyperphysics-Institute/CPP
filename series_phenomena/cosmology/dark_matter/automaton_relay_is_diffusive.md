# THE AUTOMATON-2 RELAY IS DIFFUSIVE, NOT BALLISTIC — THERE IS NO LIGHT CONE

**Patch 2887. Found while re-running the moving-source LW test under the
registered fix. This finding is larger than the test that produced it and
it bears on a RATIFIED result.**

---

## §1 — THE MEASUREMENT

`code/2887_front_propagation_class.py`. Single impulse at t = 0, no
further injection, M = 96, R = 4 — the ratified G1 kernel. Track the
weighted mean radius of |Q| per Moment.

| t | ⟨r⟩ | ⟨r⟩/t | ⟨r⟩/√t |
|---|---|---|---|
| 1 | 4.038 | 4.038 | 4.038 |
| 4 | 7.600 | 1.900 | 3.800 |
| 8 | 10.685 | 1.336 | 3.778 |
| 12 | 13.062 | 1.089 | 3.771 |

**⟨r⟩/√t is constant to 2% across twelve Moments. ⟨r⟩/t varies by a factor
of four.** Fitted exponent:

> **p = 0.478 in ⟨r⟩ ~ t^p.  Ballistic ⟹ p = 1. Diffusive ⟹ p = 0.5.**

**The relay is diffusive. There is no finite maximum signal speed and no
light cone.**

**Corollary — a quantity the programme has been misreading.** The
"c_lat = 4.0384 units/Moment" computed from the kernel's mean front radius
**is not a propagation speed.** It is the one-hop kernel width. After t
Moments the front is at 3.78√t, not 4.04t.

## §2 — DIAGNOSIS: THE TRANSLATION-INVARIANCE REDUCTION IS THE CULPRIT

The engine's own docstring: *"field rule = directed-front kernel W_R
(**translation-invariance reduction** of the C22 origin-directed hop
relay)."*

Update, verbatim from `moment()`:

    pay   = Q + inj
    Q_new = pay ⊛ K

**The C22 specification is an ORIGIN-DIRECTED relay: hops proceed outward
away from the SOURCE.** `front_kernel()` correctly builds an
outward-directed front — but **relative to its own centre.** Used as a
*convolution* kernel over the whole field, **every point re-radiates
outward from ITSELF**, which destroys the memory of which way a
contribution was already travelling. A contribution moving +x is
re-spread isotropically at the next Moment.

**Repeated convolution with a spreading kernel is a random walk.** Hence
√t. **The diffusion is intrinsic to this update form, not a tuning
artifact.**

**A convolution cannot be origin-directed, because a translation-invariant
kernel cannot know where the origin was.** The reduction named in the
docstring is precisely the step that converts a directed relay into a
diffusive one.

## §3 — WHY THE STATIC GATE PASSED ANYWAY, AND WHY THAT IS NOT REASSURING

**A diffusive relay under continuous injection reaches a steady state
satisfying Poisson's equation, whose solution is 1/r.** So static Coulomb
emerges from diffusion exactly as well as from wave propagation.

**This is why G1 passed at ±0.4% and why it tells us nothing about
dynamics.** The ratified measurement is a *statics* measurement, and
statics cannot distinguish a diffusive relay from a ballistic one. The
programme has been treating the G1 result as establishing the relay; **it
establishes the relay's steady state only.**

## §4 — WHAT THIS DOES AND DOES NOT PUT IN QUESTION

**NOT in question — the ratified static result stands.** G1's ±0.4%
pointwise agreement, Δp = 0.010, P-A2-1 CONFIRMED: **unaffected.** It is a
correct measurement of the steady-state profile. SF-8's §3, which reports
only the static shape and explicitly disclaims dynamics, is **unaffected**.

**IN QUESTION — that the ENGINE implements the C22 SPEC for dynamics.**
The spec is origin-directed; the engine is translation-invariant; those
differ precisely where propagation direction matters, i.e. everywhere
except the static limit. **This is an implementation-fidelity question,
not necessarily a defect in C22 itself.**

**IN QUESTION — CPP's capacity to produce relativity from this relay as
implemented.** A diffusive substrate has no invariant speed, unbounded
signal propagation, and no light cone. Special relativity, retardation,
and photon kinematics are not available from a √t front. **Registered as
an open item at substrate level, not as a conjecture-level issue.**

## §5 — CONSEQUENCE FOR THE LW TEST (Patch 2886, re-run at 2887)

The discriminant A = (x_aim − x_src)/(β·r) presumes a retardation lag
∝ r/c. **Under diffusion the lag goes as r²/D, so A ∝ r.** That is exactly
the r-dependence observed in both runs and it fully accounts for the
linearity failure.

**The LW test is ill-posed against a diffusive relay.** Condition B asks
whether the relay reproduces Liénard–Wiechert structure; the answer is
that it reproduces neither LW nor sharp retardation, because it has no
light cone at all. **CONJ-FP-1 Condition B cannot be settled on this
engine.** The re-run's numbers are recorded at §6 for provenance but carry
no verdict.

## §6 — RE-RUN RESULT (Patch 2887, registered fix applied)

M = 128, no wrap (max travel 64.6 on a 128-box), trilinear interpolation
replacing lattice rounding, fore and aft reported separately.

| β | r=4 fore/aft | r=6 fore/aft | r=8 fore/aft |
|---|---|---|---|
| 0.10 | −0.789 / −0.635 | −1.963 / −2.535 | −2.457 / −2.842 |
| 0.20 | −0.572 / −0.749 | −1.612 / −2.173 | −2.033 / −2.297 |
| 0.40 | −0.168 / −0.398 | −0.834 / −1.501 | −1.262 / −1.526 |

**The wrap fix WORKED: the per-β band criterion now PASSES** (≥2 of 3
radii with A < −0.50 at every β, both fore and aft) — resolving Failure 2
of Patch 2886. **Linearity still fails** (spread/|mean| = 0.556 fore,
0.515 aft, against the frozen 0.30), **and §5 now explains why it was
always going to.**

**VERDICT: INCONCLUSIVE, and the bands remain unchanged.** No re-banding.

## §7 — WHAT WOULD ACTUALLY SETTLE CONDITION B

Not a better-instrumented run on this engine. **An engine that implements
C22 as specified** — carrying propagation direction forward rather than
re-spreading isotropically each Moment. Concretely: advance contributions
along their existing hop direction, rather than convolving the whole field
with a centre-directed kernel. **Then test whether the front is ballistic
(p = 1), and only then ask the LW question.**

**Front-class test first, LW test second.** Asking the LW question of a
relay whose propagation class is unknown was the error in the original
sequencing, and it is registered here so the next attempt does not repeat
it.

## §8 — STANDING

**No change to the dark-matter ledger:** 1B OPEN; PR7 PARTIAL; six of
seven; B7 holds DM-1/DM-2/DM-3; Candidate (B) 79.5%. **G1 and P-A2-1
stand.** CONJ-FP-1 Condition B: **OPEN and not settleable on the present
engine.** The Patch 2884 substrate-viability escalation: **live, and now
sharper** — the question is no longer only whether the relay is LW-like,
but whether it has a light cone at all.
