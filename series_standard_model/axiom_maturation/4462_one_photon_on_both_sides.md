# One Photon's Light From Both Sides: the Founder Asks Whether the Photon's Length Is Known or Only the Statistics of When Photons Are Detected; Warns That Omnidirectional Emission Would Need the Whole Photon Reassembled at Detection, Perhaps After Billions of Years, a New Layer of Postulate; and Corrects Claude: the Nucleus Gives the Emission Swing Its Direction, Not Its Power, the Energy Coming From the CP's KE Across the Transit. The Decay Curve Is Indeed a Histogram; Each Photon's Fading Shape Is an Inference From Two-Photon Interference Plus the Line's Width, Not a Measurement of One Photon. The Reassembly Is Real, but a Directed Packet Does Not Avoid It: Diffraction Spreads a Half-Metre Packet to Over a Hundred Light-Years in a Billion Years, and a Single Ion's Light From Both Sides Adds Up in Each Photon's Arrival. With the Transit Timed by Speed Instead of the Pull, the Order of Lyman-α and Lyman-β Still Comes Out Wrong

**Patch:** 4462. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4462_pulse_length_reassembly_nucleus_direction.md` (answers 4461 §8).
**Script:** `series_standard_model/code/4462_packet_length_spread_and_transit.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It checked the cited experiments against their papers. It found that the
first draft:
- used a length spread that does not reproduce the exponential histogram (the right one gives an overlap of 1/2, not 0.39);
- described Somaschi 2016 as two separate emitters (also wrong in 4452 §2);
- claimed the line shape alone gives a fading packet;
- misdescribed Claude's 4461 misreading;
- cited 4453 for his "statistical rather than causal" (it is 4454);
- overstated the line-order failure;
- left the recharge leg and the "emitted total" reading unmarked;
- called a radius a width;
- described the Eschner experiment loosely;
- had a broken founder question;
- mixed numbering in the dispositions;
- stated an interpretation as the observation.

All thirteen required changes are taken in. One is corrected further: the critic's waist bound was itself wrong, since no starting width keeps a Lyman-α
packet within a telescope after a billion light-years (§3).

## 1. His answer

- **The pulse length:** "can we be certain of the length of the photon pulse? Are we measuring the statistics of emission after stimulation, that is, the
  distribution of time over which a photonic pulse is measured, or the length of time over which it is radiated."
- **Omnidirectional radiation:** portions of an emission swing going out in all directions "would require a reassembly of the entirety of the photon upon
  collision, of a photon which had been distributed omnidirecdionally, potentially for billions of years. This would require an entirely new layer of
  postulate to accomodate such a reassembly."
- **The nucleus:** "Regarding the pull of the nucleus, that was not my postulate. I was using the positive nucleus as the direction of the emission swing,
  not its source of power. The power/energy that was emitted total was related to its KE from the start of its transit to its end at the other side."

## 2. The photon's length: a histogram, and what makes it each photon's (script part 1)

**He is right about what the decay curve is.** The exponential fading is built from many photons: an atom is excited, one photon is detected at some time
afterward, and the times from many repetitions are collected into a histogram (4452 §2). One detection gives one time, not a length. That is the point he
made in 4454 ("statistical rather than causal"), which 4454 §2 already accepted as an inference resting on two-photon interference. Claude's 4461 wording,
"the light is measured fading away smoothly" and "the leak must shrink", went back beyond it.

**What carries the inference to each photon:**
- **Two-photon interference.** Two photons sent into the two inputs of a beam splitter at the same time leave together through one output when they are
  identical; the closer their shapes, the stronger the effect. Suppose photons were flat packets, starting at the excitation, with lengths spread so as to
  reproduce the exponential histogram. That needs lengths distributed as (L/τ²)e^(−L/τ). (Exponentially spread lengths would not do it: they give a curve
  that piles up near zero; script.) Two such photons would overlap on average only one half (script: Monte Carlo and exact).
  - Photons from two trapped ions about a metre apart interfere with about 95% contrast (Maunz and others, 2007).
  - Photons from two trapped rubidium atoms are consistent with identical packets (Beugnon and others, 2006).
  - Successive photons from one quantum dot reach 99.6% (Somaschi and others, 2016). That is a test of sameness from one emitter, not between two (4452 §2,
    corrected here and in an erratum there).
  - Two-photon interference has also been resolved in time within the photons' duration (Legero and others, 2004), the closest measurement to his "the
    length of time over which it is radiated".
- **What the two measurements give together.** If the photons are identical and pure, which near-perfect two-photon interference indicates, the histogram
  is each photon's own envelope (in energy). Random start times or timing jitter comparable to the lifetime would lower the interference, so they are
  excluded by that step. The line's width, exactly 1/(2πτ) once the atoms' motion is removed (4451 §3; usually measured in absorption or excitation, not on
  the emitted photons), then excludes a chirp or a wandering phase. The line shape alone could not tell a fading packet from a rising one, and identical
  flat packets would give side lobes (4461 §3.2).

**So each photon's envelope is inferred, not measured on one photon, to fade exponentially over the lifetime.** On that inference the leak per pass must
fall as the pool drains, and the swing must shrink (4461 §3.2). If his picture allows photons that are not identical, or not fading, it must still meet
the two-photon and line-width measurements.

## 3. The reassembly (script part 2)

**He has found a real postulate.** In standard physics a single photon's wave spreads over all directions in the dipole pattern, and the photon is detected
whole, in one place. That concentration at detection is a separate rule of quantum mechanics (the measurement rule), and how to understand it is still
argued. So he is right that omnidirectional emission comes with such a layer.

**Two facts any picture has to meet, his included:**
- **A directed packet spreads too.** A packet of finite width diffracts, which is what gives fringes at all (4458). A Lyman-α packet with a waist of half a
  metre spreads at about 8 × 10⁻⁸ rad. (The half metre is its length, cτ, used here as an illustrative width.) After a billion light-years it is about 160
  light-years across; visible light about 700. A different start does not escape it: whatever its starting width, a Lyman-α packet after a billion
  light-years is at least about 9 × 10⁸ m in radius (the narrowest, from a start about 6 × 10⁸ m wide; script). A telescope intercepts a tiny part of it,
  yet records whole photons. So the concentration at detection is needed for any packet that has travelled far, directed or not; it is not an extra cost
  of emitting in all directions. (A packet that did not diffract could not make fringes.)
- **A single photon's detection carries light from both sides.** Eschner, Raab, Schmidt-Kaler and Blatt (Nature, 2001) drove a single trapped barium ion
  continuously with lasers and collected its 493 nm light on one side, while a mirror 25 cm away on the other side sent the light leaving that side back past
  the ion into the same detector. The detected light showed fringes of 72% visibility as the mirror was moved, while the photons stayed antibunched (one at a
  time). The mirror also raised or lowered the ion's own emission into that direction. (A driven ion, not a single decay; the single-decay version is not
  this experiment.) A packet sent one way only could not interfere with light that left the opposite way.

So the reassembly cannot be avoided by directing the photon. In CPP it is the question already owed as 4444 b and c: what of one photon is present on two
paths, and why marking a path removes the fringes. It now extends to opposite sides of the atom, and to arrival whole at one place after spreading.

## 4. The nucleus as direction, not power (script part 3)

**Correction taken.** In 4461 Claude read the override as setting the swing's line (4461 §2), which agrees with his clarification. But Claude then timed
each pass by the Coulomb fall (4461 §3.3) and said in the reply "if the nucleus's pull times each pass", without marking that timing as Claude's model
rather than his. His 4461 message did give the nucleus a part in the drop ("the nuclear positive charge will superimpose with the KE kick"), which made a
Coulomb test worth running, but it was never his postulate. 4461 §3.3 is re-marked as Claude's model. His intended picture: the nucleus sets the swing's
direction; the energy comes from the CP's KE across the transit.

**The transit timed by speed instead.** The rough model:
- the CP crosses from the upper orbit's distance on one side, through the nucleus, to the lower orbit's distance on the other (Bohr radii,
  (n_u² + n_l²) a₀); out and back is two crossings;
- the recharge from the lower to the upper distance between crossings is given zero time (as in 4461 §3.3; a finite recharge lengthens the higher levels'
  cycles and makes the order worse).

Two choices of speed, both Claude's:

| Speed set by | Lyman-β ÷ Lyman-α | Lyman-β ÷ Balmer-α |
|---|---|---|
| the upper level's KE (αc/n_u) | 0.33 | 1.30 |
| the energy difference (½mv² = ΔE) | 0.54 | 3.29 |
| measured | 1.19 | 6.40 |

The order of Lyman-α and Lyman-β comes out wrong: both choices make Lyman-β slower, where it is measured 1.19 times bluer. Lyman-β against Balmer-α comes
out in the right order but far too close. The reason is geometric: the distance across grows as n². To match, the CP would have to cross about 2.4 times
faster from the third level than from the second. No speed set by hydrogen's energies does (at most about 1.09 times), and a constant speed, even c, gives
half. So a crossing between the two orbits' distances cannot set the colour at any speed set by these energies, unless the swing's length is not the
orbits' size.

**The total energy.** His "the power/energy that was emitted total was related to its KE from the start of its transit to its end" fits the budget if the
sum over the passes is ΔE. That is Claude's reading, and the convenient one. Read per transit, the KE lost across one crossing would be radiated in that
crossing, which returns to 4461 §3.1's one-cycle photon. Speed (ii) uses that per-transit KE only to set the speed. §5 asks.

## 5. Question to the founder (physical picture)

- **Between which two places does the CP travel on each crossing, and what sets how fast it crosses? Is the energy given up across one crossing what that
  crossing radiates, or a share of the whole interval?**
- **A single ion's light leaving toward a detector, and its light leaving the other way and sent back by a mirror, together give fringes, while the photons
  still arrive one at a time. In his picture, what goes out on each side, and what arrives at the detector?**

## 6. What stays open

- **(a) The photon's envelope:** inferred to fade exponentially, from identical, pure photons (two-photon interference) plus a transform-limited line, not
  measured on one photon; his picture must meet both (new).
- **(b) The reassembly** (= 4444 b, c, extended): light from both sides of the atom in each photon's arrival, and arrival whole after spreading; in
  standard physics the measurement rule.
- **(c) The transit's length and speed** (founder question): a crossing between the orbits' distances gets the Lyman-α/Lyman-β order wrong for any speed set
  by these energies; and the reading of "emitted total" (sum over passes, convenient; per transit, fails 4461 §3.1).
- **(d) Carried from 4461 by letter:** (a) what times the swing at ΔE/h; (b) the share per pass and where the rest goes; (c) the swing must shrink, now
  conditional on (a) here; (d) the extended unit in CPP terms; (e) the sideways step; (f) its carried list (4460 b, c, e, g; 4459 c, d, e, f, i; 4457 d–g;
  4444 b, c); (i) the sign of the restoring force; (j) the recharge leg, used at zero time here; (k) the axis-turn bound; (l) whether he keeps "photon along
  the collision"; (m) which reading of "quantum".
- **(e) Founder question 4462 §5.**
- **(f) Dispositions:**
  - 4461 §6 Q1 (how much of each drop leaves as light, and where the rest goes): not answered; carried as 4461 (b) and (m).
  - 4461 §6 Q2 (the same turning places as the pool empties): not answered; carried as 4461 (c), now conditional on (a) here, and bears on (c) here.
  - 4461 (g), the founder question: disposed as above. (4461's (h) is its dispositions; the carried list (a)–(f), (i)–(m) is complete.)
  - 4461 §3.3 (Coulomb timing) re-marked as Claude's model, not his; superseded by §4 here.
  - 4461's "the leak must shrink" restated as an inference (§2 here).
  - 4452 §2's description of Somaschi 2016 corrected (same dot, successive photons; erratum appended to 4452).
  - 4454 cited for "statistical rather than causal" (the draft had 4453).

## 7. Answer to his "What do you think?"

He's right that the fading curve is a statistic. Each atom gives one photon at one moment, and the curve is built from many, so I said too much about a
single photon. What lets us infer each photon's shape is two more measurements. First, photons from two separate trapped ions behave as identical when they
meet at a beam splitter, matching about 95%. If photons were flat bursts of different lengths that still made the same curve, they'd match only about half
the way. Second, if the photons are identical, the fading curve built from many of them is each one's own shape, and the width of the colour shows the
packet isn't chirped. So each photon fading away is an inference, not something measured on one photon, but a strong one.

On reassembly, he's found a real postulate. In standard physics a photon spreads out in all directions and is still detected whole in one place, and that
is a separate rule, still argued about. But sending the photon in one direction doesn't escape it. Any packet spreads as it travels: a half-metre one is
over a hundred light-years across after a billion years, and no starting width keeps it small. A telescope catches a tiny part of it yet records whole
photons. And in one experiment a single ion sits between a detector and a mirror. Its light leaving the side away from the detector, sent back by the
mirror, interferes with its light leaving toward it, while the photons still come one at a time. So light from both sides of the atom adds up in each
photon's arrival. Explaining that is the same open question as what goes through both slits.

On the nucleus, I misread him, and I've corrected it. I had timed each pass by the nucleus's pull without saying that was my assumption. If the nucleus
only sets the direction and the CP's energy carries it across, the crossing is timed by its speed. I tried two ways of setting the speed, and the colours
still come out wrong: the line from the higher level should be bluer, and both ways make it redder. That's because the distance across the higher orbits
grows faster than any of these speeds. So I've asked how far the CP travels each crossing, what sets its speed, and whether one crossing radiates its whole
energy or a share.

## 8. PD-008

- **Corrected:** Claude's 4461 statement about single photons (now an inference); Claude's unmarked Coulomb timing of the pass (4461 §3.3); 4452's
  description of Somaschi 2016.
- **Not softened:** a directed packet still diffracts and still needs concentration at detection; a single photon's detection carries light from both sides
  of a driven ion; a crossing between the orbits' distances gives the wrong Lyman-α/Lyman-β order and the wrong Lyman-β/Balmer-α ratio for both speeds
  tried, and for any speed set by these energies.
- **Marked:**
  - the two speeds in §4 are Claude's choices; the Bohr radii as the crossing's ends are Claude's reading of "from the start of its transit to its end at
    the other side"; the recharge leg is given zero time;
  - "emitted total" read as the sum over passes is Claude's reading and the convenient one; the per-transit reading fails 4461 §3.1;
  - the overlap of 0.50 is for flat packets starting together, with lengths spread to reproduce the exponential histogram; one alternative among others;
  - the near-perfect quantum-dot figure is for successive photons from one dot, not separate emitters;
  - the half-metre waist is illustrative.
- **Not claimed:** novelty for two-photon interference, Gaussian-beam diffraction, the measurement rule or the Eschner experiment.
- Nothing registered.
