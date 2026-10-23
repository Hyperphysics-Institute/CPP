# Coasting From the Summation: With the Founder's Rule (Move by the Rear Signal Minus the Front Signal at the GP the CP Lands On) and the Registered Even Emission, a CP's Own Returns Give a Forward Step of Exactly v at Every Speed. The Gating Obstacle Is Dilution: Normalized by All DI-Bits Arriving, the Step Falls Short and a Free CP Slows

**Patch:** 4414. **Lane:** foundations, with GR and EM. **Session:** 242.
**Founder input:** `founders_voice/4414_no_speedometer_displacement_from_summation.md` (answers 4413 §7).
**Script:** `series_standard_model/code/4414_coasting_from_the_summation.py`.
**Critic:** a fresh-context critic returned HOLD on the first draft (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). The first draft used one angle for
emission, reflection and arrival, which is wrong at first order in v; done consistently, the result flips (the registered
even emission gives exactly v; the "headlight" falls short). It also misattributed the normalization rule, missed the sign
question, and missed dilution, which is the real obstacle. All eight required changes are taken in; the corrected geometry
was checked two independent ways (an exact fixed-reflector quadrature and a Monte Carlo, both in the script). A second
critic accepted the revision with two changes (the meaning of "rear minus front"; dilution's exit (b)), both taken in.

## 1. His answer

- **There is no speedometer and no pushing.** The CP does not monitor its speed; it computes its displacement from the DI-bit
  summation at each GP it lands on, **the rear displacement signal minus the front one**, and moves that amount each Moment.
  Velocity is an effect, not a monitored parameter.
- **"Stored velocity"** is a fair higher-level name for what the DP-arcs and separation do: a summary of an impossibly large
  summation of DI-bits from many sources, which accurately represents the effect producing the inertial front-back
  difference.

4413's separate "step = readout + forces" rule is withdrawn; the registered wording (R-CP-NO-REST-MASS: "Each Moment a CP
advances by its SSV_net (V_i)") is the starting point. His "summary" remark narrows, but does not close, the restatement owed
under 4404 item 3.

## 2. The model (script part 1)

The CP moves at v; at the Moment in question it sits on its landing GP. It sent its DI-bits from earlier positions, behind
where it is now. Reflectors at rest, spread evenly, return what reaches them evenly in all directions. A return is weighted
by the emission density toward that reflector, the spreading from the emission point, the arrival-rate compression at the
reflector, and the spreading back to the landing GP; it arrives from the reflector's direction.

**Emission:** the registered case is even in the absolute frame: every GP emits the same fixed number of DI-bits every
Moment (AP-4), one per GP filling the PSR ball (R-DIBIT), and the moving CP broadcasts from where it is (4409 §2). The
"headlight" (even in the CP's own frame) is shown only for contrast.

## 3. Result

| v | projected net / total, registered even emission | headlight emission |
|---|---|---|
| 0.1 | 0.1006 | 0.034 |
| 0.3 | 0.2991 | 0.107 |
| 0.5 | 0.5006 | 0.204 |
| 0.9 | 0.9001 | 0.632 |

(Monte Carlo, two million reflectors, ±0.001; the exact quadrature gives 0.0100000000, 0.1000000000, 0.5000000000 and
0.9000000000 at v = 0.01, 0.1, 0.5 and 0.9, and the result does not depend on the reflectors' distance.)

**What "rear minus front" must mean:** the result is for the **projected net**, the vector sum of the arrivals' directions
along the line of motion (the SSV_net component), divided by the total. Read instead as raw counts (arrivals from the rear
hemisphere minus the front hemisphere), the same returns give about 1.5v (0.150 at v = 0.1, 0.669 at v = 0.5), and the CP
would speed up rather than coast.

**With the registered emission, the CP's own returns give a rear excess of exactly v, at every speed.** The returns from
behind outnumber those from in front because the CP sent them from points behind its present position, closer to the
reflectors behind. **With his rule, rear signal minus front signal taken as the projected vector sum, the step is forward and
equal to v**: the CP moves each Moment by exactly the displacement it had, preserving any speed below light speed, the same
for every kind of particle (nothing but v enters). The headlight falls short (about v/3).

(The first draft had this the other way round; its one-angle geometry was wrong at first order in v. Its "γ rise in SSV_abs"
by-product came from the wrong case and is withdrawn.)

**The sign:** his wording fixes it (rear minus front, forward step). AP-4's payload convention (V_i = E + S, with E the
reflecting GP's register, pointing away from the reflector) would give a backward step for the same rear excess; this is
CONJ-FP-1's Condition A (the sign of the sea's response) in a new form, and the two conventions need reconciling.

## 4. The gating obstacle: dilution (script part 2)

The step rule used here divides the net signal by the total, d = (|V_i|/SSV_abs)·PSR_eff. That is the AUTOMATON-1 v/c map the
founder accepted at Patch 2732, not AP-4 itself (AP-4's SSV_abs is a sum of payload magnitudes). Under it, **every DI-bit
arriving from other sources** (other charges, the sea's own activity, the gravitational SSV_abs) adds to SSV_abs and nothing
to SSV_net. The step becomes s·v, with s the CP's own share of the total, and v_{n+1} = s·v_n decays: with s = 0.99 the speed
falls by 1% per Moment. s also changes with surroundings, so a free CP would slow on entering a region with more DI-bits (near
a mass, near other charges) with nothing acting on it: a first-order breach of the first law, gravity acting like friction.

The exits:
- **(a) the CP's own returns are compared only with each other** (normalized by their own count), separately from everything
  else arriving. The origin address cannot do this alone, since a relayed DI-bit carries the relaying GP's address
  (AP-4c);
- **(b) a different step rule.**

(A self share that is merely overwhelming is not an exit: any s below 1 decays geometrically, and with some 10⁴³ Moments
a second a free CP would stop.)

This is the question that decides whether his rule coasts, and it is a physical picture for him (§7).

## 5. Fairness and other limits

- **His DP-arc point:** he says the summation the DP-arcs and separation represent carries the effect. In this model the
  coasting comes from reflectors **at rest**; reflectors moving with the CP give zero (4413 part 6: the readout is the velocity
  relative to the reflectors). If the DP-arcs are a polarized cloud moving with the CP, they would not supply the front-back
  difference here; if they are the sea's at-rest DPs organized by the CP's passage, they would. Which one is meant is open.
- **The relay:** the registered relay deposits at the PSR shell and re-imprints, and no DI-bit goes beyond its GP_PSR
  (AP-4c, R-DIBIT). The reflector model is an idealization of that; the same calculation with the registered relay is owed.
- **The reflection probability** drops out only if it is the same in every direction.

## 6. What stays open

- **Dilution** (exits a, b); founder question.
- **The meaning of "rear minus front"**: projected vector sum (gives v) versus hemisphere counts (gives ~1.5v).
- **The sign convention:** his "rear minus front" against AP-4's payload direction (Condition A).
- **The registered relay** (PSR-shell deposit and re-imprint) in place of reflectors.
- **AP-4's weighting** (sums of payload magnitudes, V_i = E + S) in place of counts.
- **Co-moving versus at-rest reflectors** (the DP-arcs).
- **CONJ.md (line 477)** to carry 4413–4414 when the 4411 (f) update is made.
- **Carried:** 4413 items (4)–(10); 4413 items (1)–(3) answered (no speedometer; the summation at the landing GP; the 4404
  restatement narrowed).

## 7. Question to the founder (physical picture)

A moving CP lands on a GP. Arriving there are its own DI-bits coming back from the sea, slightly more from behind than from in
front, and a great many DI-bits from everything else around. **Does the CP's displacement come from comparing its own returns
with each other only (rear against front), or is that difference divided by everything arriving at the GP, from every
source?** In the first case it keeps exactly its speed; in the second, the other DI-bits water it down and it slows, more so
near a mass. And is "rear minus front" the net direction of the returns (which gives exactly its speed), or simply how many
come from behind compared with in front (which would make it speed up)?

## 8. Answer to his "What do you think?"

He is right, and his rule does more than I first found. With no speedometer, the CP simply moves by the rear signal minus the
front signal at the GP it lands on. Its own DI-bits, sent out evenly as the registered rules say, come back from the sea with
exactly as much excess from behind as its speed, because it sent them from behind where it now is. So with his rule, taking rear
minus front as the net direction of the returns, it moves forward by exactly its speed each Moment, at every speed, whatever
kind of particle it is. (Counted simply as more from behind than in front, the same returns would make it speed up.) (My
first draft said a "headlight" was needed; that was a geometry error, and the reviewer caught it.)

The one obstacle is dilution: if that rear-minus-front difference is divided by all the DI-bits arriving at the GP, from every
source, the step comes out smaller than the speed and a free particle would slow down, more so near a mass. It works exactly
only if the CP's own returns are compared with each other, with nothing else in the comparison; a small share of other
DI-bits still slows it, over enough Moments, to a stop.

## 9. PD-008

- **Convenient branch, marked:** "coasting follows from his rule." It does for the CP's own returns in an idealized relay; it
  fails under the total-count normalization unless the self-returns are separated or dominate.
- **Owned:** the first draft's geometry error, the misattribution of the normalization rule, and the withdrawn γ by-product.
- Nothing registered.
