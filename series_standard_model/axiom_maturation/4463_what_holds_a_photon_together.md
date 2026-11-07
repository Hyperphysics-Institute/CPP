# What Holds a Photon Together: the Founder Sets Aside the Orbit's Radius (an Orbital's Energy Is Its Totality; Each Swing May Start and End Anywhere; Only the Total Must Equal the Interval), Holds That Decay Statistics Do Not Map 1:1 Onto the Swing Sequence's Shape, and Pictures the Photon as an Organized Volume of the DP Sea, Its Active Portion About a Metre Across, Held Together by Its Own Reinforcement, With Any Growth in Width Likely From Microlensing. Claude's Radius Models Are Withdrawn as Tests of His Picture, Though an Orbital's Size Still Grows With Its Level; the Colour Is a Rate, So the Question Is What Makes Every Swing Sequence Radiate at ΔE/h. On the Statistics: if Each Photon Kept Its Own Length and Only Its Start Were Spread Over the Lifetime, Photons From Separate Atoms Could Not Both Match the Exponential Histogram and Interfere as They Do. On the Volume: Spreading Is Measured in the Lab and Goes With the Colour, Which Lensing Does Not Give; Holding a Fixed Width Would Need a Nonlinear Relay. The Ion Experiment Explained

**Patch:** 4463. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4463_orbital_totality_statistics_photon_volume.md` (answers 4462 §7 and §5).
**Script:** `series_standard_model/code/4463_random_start_overlap_and_spreading.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed every number and checked the experiments against the
papers. It found that the first draft:
- conceded the radius too far (an orbital's size still scales with its level);
- misstated how 4461 §3.3 was marked;
- presented Claude's random-start construal as his statement, and altered a quotation of his;
- overclaimed that only a packet starting at the excitation fits;
- left the "departs" measure unexplained;
- stated the detector-rule evidence too strongly;
- misstated the beam size, and argued from many-photon beams for a per-photon claim;
- gave the lensing argument without its source or size;
- overclaimed "only" in the nonlinearity argument, and missed a within-photon branch;
- left the coherence-length convention unstated and flipped 4460's reading of his metre without saying so;
- overclaimed the antibunching and misdescribed the emission change;
- dropped a hedge;
- led the first question;
- missed dispositions and an item (how a 2 mm beam is made of metre-wide photons).

All seventeen required changes are taken in, with most of the optional notes.

## 1. His answer

- **The orbital's energy:** "the distance the electron is from the nucleus does not determine the energy of an electron orbital, as you know from the
  shape of the dumbbell-shaped p orbitals"; "the energy of the orbital is the totality of the orbital"; the energy picked up and radiated in each swing
  "could be from any point and end at any point"; "I don't think it matters how much energy is in each swing, only that the total quantum equals the
  energy difference"; "the ability of the mechanism to radiate the totality of that increment is the important parameter"; the colours "come out in order
  of their energy difference, not by the orbital radius". He frames the open question as "whether the emission swings produce an equi-partition of energy
  with each swing".
- **The statistics:** each photon is detected as a pulse, emitted statistically; "the statistics of emission are related to the system that is stimulated
  and then emits, not to the characteristics of the system that cause the system to discharge an increment of energy over a large number of emission
  swings. There may be a shaping of the system, but it is not a 1:1 correlation".
- **The photon as a volume:** photons are "embedded in, and carried by, a volume of space", the volume where superposition or subtraction gives "greater
  than ambient disorder"; its influence "probably the entire light cone volume"; its active portion "probably, as you note, around a meter in diameter";
  every portion of the correlation wave "is integrated because of its mutual enforcement and cancellation to retain its structure"; the growing radius,
  "if empirically determined, it is likely due to interaction with mass along the path and the associated microscopic lensing"; the coherence, he thinks,
  "speaks to the speed-of-light mutual interaction between the DP-arc separations and the DP Sea transmission of speed-of-light signaling".
- **A request:** "Please explain the setup of the ion emission experiment in more detail."

## 2. The orbital's energy, and what sets the colour

**Claude's radius models are withdrawn as tests of his picture.** The crossings between Bohr radii were Claude's models (4461 §3.3, re-marked as Claude's in
4462 §4; 4462 §4's own speed models, marked). He is right that the energy belongs to the whole state: in the Schrödinger picture the p orbitals are spread
out in two lobes, and 2s and 2p have the same energy with different shapes. **But the orbital's overall size still scales with its energy:** in hydrogen
the energy is fixed exactly by the average of 1/distance, and the orbital's size grows as n². So any swing whose extent grows with the orbital's size meets
the same line-order difficulty as 4462 §4. Claude marks agreeing on the radius as the convenient branch (§9).

**What stays: the colour is a rate.** The measured colour of a line is how many crests pass per second (4447, 4456), and every photon of that line has
energy h × that rate. "The colours come out in order of their energy difference" is that measured fact, E = hf. A mechanism that radiates the right total
gets the energy right; the colour, on his emission-swing picture and 4459 §3's argument that a dipole radiates at the rate it swings, is set by how often
what radiates swings. So if each swing may start and end anywhere, his mechanism still has to make every swing sequence reverse at ΔE/h. That is 4461 (a),
with the radius set aside: what in the orbital's totality times the swing.

**His equipartition question** (does each swing carry an equal share?) is the per-pass question of 4461 (b). His answer, that the share per swing does not
matter so long as the total is ΔE, settles the total. The two-photon measurements of §3 bear on how the share is spread in time.

## 3. The statistics and the shape (script part 1)

**Agreed in part.** A detection-time histogram does not by itself give the shape of each photon (4452 §2, 4462 §2). Claude reads his point as: each photon
could start at a random time and have a shape of its own. That reading is Claude's, the one Claude can test, and it is marked (§9).

**The test of that reading.** Suppose each photon is a packet of its own length, and only its start is random, spread exponentially over the lifetime. Two
photons from separate atoms, excited together, then arrive at random offsets, and they interfere at a beam splitter only as far as they overlap in time.
In the script (flat packets):

| Packet length (lifetimes) | Mean two-photon overlap | Histogram departs from exponential by |
|---|---|---|
| 0.1 | 0.03 | 0.05 |
| 0.3 | 0.09 | 0.13 |
| 1 | 0.26 | 0.31 |
| 3 | 0.54 | 0.54 |
| 10 | 0.82 | 0.76 |

"Departs by" is the largest gap in the cumulative share. For packets up to a lifetime long, it is mainly a delayed, rounded start of the curve; the tail's
slope is unchanged. Seeing it needs timing finer than the packet, measured from a pulsed excitation (Maunz used picosecond excitation pulses and fine time
tags). The overlap column assumes the coincidence is integrated over the packet; integrating changes the coincidence total only through the overlap, so
the column stands for either detector.

Short packets fit the histogram but would hardly interfere. Long packets interfere more, but then the detection times spread far from the exponential
curve. Photons from two separate trapped ions interfere with about 95% contrast (Maunz and others, 2007, after dark-count subtraction, from pairs within an
8 ns window, about one lifetime of the ytterbium ion; 4462 §2). No packet length fits both when the start is spread over the lifetime. **Only packets whose
start is fixed relative to the excitation to well within a lifetime, with the exponential carried in each packet's own fading, fit both.** A small start
jitter or a fixed delay is allowed; a start spread comparable to the lifetime is not (as 4462 §2 said).

**Where the link really rests.** The step from histogram to shape uses the standard detector rule: the chance of a click in each instant follows the
packet's strength at that instant. That rule is consistent with every test so far. When an ion in a cavity is driven by a pump pulse of chosen shape, the
histogram follows the photon shape predicted for that pump (Keller and others, Nature 431, 1075, 2004, a calcium ion). A neutral-atom cavity source shows
the same with a pump-set pulse (Kuhn, Hennrich and Rempe, Phys. Rev. Lett. 89, 067901, 2002). These test emission theory and the detector rule together.
Two-photon interference resolved within the photon (Legero and others, 2004; 4462 §2) tests the rule more directly. In CPP the detector's rule is owed
(4459 d). If the CPP detector does not click in proportion to the local strength, the link would have to be rebuilt, and that is his opening. **So, as he
says, the shape is not simply read off the decay timing; it follows from the timing together with two-photon interference and the detector rule.**

## 4. The photon as a volume

**Agreed in outline:** a photon as an organized region of the DP sea, held together as one pattern by its own superposition and cancellation. In standard
terms, that is a wave whose parts travel together because each part is regenerated by its neighbours at light speed.

**But the width does grow, in the lab, and with the colour** (script part 2). A laser beam with a waist radius of 1 mm (2 mm across) spreads: after 10 m a
red beam (633 nm) is about 2.3 mm in radius and a violet one (405 nm) about 1.6 mm. That is measured routinely, over a few metres of air or vacuum with no
significant mass nearby, and the spreading goes with the wavelength. Per photon, the same spreading is seen when single-photon diffraction and
interference patterns build up one click at a time, with the spread angle in proportion to wavelength ÷ width (4444, 4458). Single-slit diffraction is the
same effect: he accepts that a slit spreads the photon, and free space spreads it by the same rule.

**Lensing cannot give it.** Gravitational lensing bends all colours alike. That comes from general relativity and is confirmed observationally (microlensing
light curves are the same in every colour); CPP's "gravitational slowing" has not been derived, so this is a borrowed fact, marked (§9). The size argument
does not depend on the colour rule: the focusing by Earth's gravity across a 10 m beam path is about (GM/R³)L²/c² ≈ 10⁻²¹, against a measured growth of
order one.

**Holding a fixed width would need a nonlinear relay.** Apart from structured beams (Bessel, Airy) whose central spot holds only over a limited range and
which still spread overall, a beam keeps a fixed width without guidance only in a medium whose response depends on the light's own strength (self-focusing
in some crystals and glasses). In empty space, light passes through light without effect (light-by-light scattering is a tiny quantum effect; 4457), and
interference needs strict adding (4459 §2). So if the photon's own reinforcement held it to a fixed width, the relay would have to be nonlinear, and two
photons crossing would disturb each other. A self-holding that acted only within one photon would be tested instead by single-photon fringes, which add
strictly (4459 §2). That branch is marked (§9).

**A sharper conflict: a 2 mm beam made of metre-wide photons.** If each photon's active portion is about a metre across, a laser beam 2 mm wide would be
made of photons each five hundred times wider than the beam. Light can be focused to a spot a wavelength across, and single photons are routinely sent into
optical fibres a few micrometres across. What his active portion is in CPP terms, and how it fits through a fibre, is carried as (j).

**His metre and the coherence length** (script part 3). Coherence length here means c × lifetime (the length over which the intensity falls to 1/e; the
other common convention, c/Δν, is 2π times longer). For natural widths: 0.48 m for Lyman-α, about 2.4 m for barium's 493 nm line, 4.9 m for sodium's D
line (real lamps are much shorter, because of the atoms' motion). He gave the photon a sideways radius of half a metre in 4460, and 4460 §4 read that, as
the convenient branch, as a sideways reach of c × τ. Here Claude reads his metre instead as the photon's length along its travel. That too is Claude's
reading and convenient, it does not match his stated sideways meaning, and under the other convention it would not match at all.

**Coherence:** agreed that it is the interesting part. In standard terms a photon's coherence along its travel is set by the source (the lifetime), and
across the beam by the source's size and the distance travelled. His picture of a correlation wave maintained by light-speed signalling is a CPP route to
the first; the second must come out as diffraction does.

## 5. The ion experiment, in more detail

Eschner, Raab, Schmidt-Kaler and Blatt, "Light interference from single atoms and their mirror images", Nature 413, 495 (2001):

```
   detector  <---- lens ----  [ ion ]  ---- lens ---- mirror
  (photon                     (one Ba+,                (25 cm from
   counter)                   held in vacuum)          the ion)
              <------------- light reflected by the mirror passes back
                             through the ion's position toward the detector
```

- **The ion:** one barium ion, ¹³⁸Ba⁺, held in vacuum by oscillating electric fields in a small trap, and cooled by lasers until its motion is small
  compared with a wavelength (which still limits the visibility to 93%).
- **The drive:** two lasers shine on it continuously, one at 493 nm (blue-green) that it scatters, and one at 650 nm (red) that keeps it from getting
  stuck in a side level. It scatters 493 nm photons, one at a time.
- **Two paths to one detector:** a lens on one side collects light going that way and sends it to a photon counter. On the opposite side, a lens 12.5 mm
  from the ion, gathering about 4% of its light, and a mirror 25 cm away send the light going that way straight back, focused onto the ion's position, so
  that it passes the ion and continues into the same detector. The detector therefore receives light that left the ion toward it, and light that left the
  ion the opposite way, travelled 50 cm further, and came back.
- **What they changed:** the mirror's distance, by fractions of a wavelength.
- **What they saw:**
  - the counting rate rose and fell as the mirror moved, with fringes of 72% visibility: the two paths interfered;
  - the photons stayed antibunched: two clicks at the same instant were strongly suppressed, so the light came one photon at a time;
  - the mirror also changed the ion itself: its total light rose and fell by about 1%, and its 650 nm light varied in opposition.
- **The caveat:** the ion was driven continuously, so much of its light is elastically scattered, sharing the laser's steady rhythm, which holds over far
  more than the 50 cm extra path. It is not one excitation followed by one decay; that version is a different experiment.

**What it shows:** each photon's detection carries light that left both sides of the ion; the 50 cm detour lies within the light's coherence.

**In his picture, as Claude reads it:** a photon's active volume about a metre across, centred on the ion, is not ruled out by the result, since it would
reach the mirror at 25 cm. But that is a volume around the emitter, not a packet heading one way, which bears on his 4460 statement that the photon goes
along the collision (4461 l). §6 asks.

## 6. Question to the founder (physical picture)

- **When the active portion of a photon leaves an atom, is it a shell spreading out around the atom, a packet heading one way, or some other form?**
- **In the lab, a red laser beam spreads more than a violet one of the same starting width, over a few metres with no large mass nearby. In his picture,
  what makes the spreading depend on the colour?**

## 7. What stays open

- **(a) What times every swing sequence at ΔE/h**, from any start to any end (= 4461 a, 4460 a, 4457 b, 4446 c), with the radius set aside; the orbital's
  size still scales as n².
- **(b) The share per swing (his equipartition question)** (= 4461 b, 4462 c): the total is ΔE; how it is spread in time is constrained by §3.
- **(c) The detector's rule in CPP** (= 4459 d): whether a click follows the local strength; the histogram-to-shape link rests on it.
- **(d) The photon's width:** diffraction in proportion to wavelength, measured in the lab and per photon; a fixed width would need a nonlinear relay (in
  tension with 4459 c, linearity). His microlensing explanation is not adopted for lab spreading (it gives no colour dependence, and is about 10⁻²¹ in
  size); §6 asks.
- **(e) Shell, packet or other form** (founder question), with 4461 (l).
- **(f) Coherence in CPP terms:** along the travel (set by the lifetime) and across (set by source size and distance).
- **(g) Carried:** 4462 (a) the envelope inference, now with §3's random-start test; 4462 (b) the reassembly (4444 b, c), with his volume picture as a
  candidate; 4461 (c), (d), (e), (i), (j), (k), (l); 4460 b, c, e, g; 4459 c, e, f, i; 4457 d–g.
- **(h) Founder question 4463 §6** (shell, packet or other form; what makes spreading depend on colour).
- **(i) Dispositions:**
  - 4462 §5 Q1 answered in part: the crossing may start and end anywhere; the radius is not the energy; the speed is not given (carried in (a)).
  - The radius models of 4461 §3.3 and 4462 §4 withdrawn as tests of his picture, with the n² caveat.
  - 4462 (c)'s "emitted total", read as the sum over swings, is now his stated view (§1), no longer only Claude's reading; the per-transit reading is
    dropped.
  - 4461 (m) (which reading of "quantum") answered in part by the same statement: the per-swing amount may vary; only the total counts.
  - 4462 §5 Q2 answered in outline (a volume carrying the photon, active portion about a metre); carried as (e).
  - His request for the ion experiment's setup answered (§5).
- **(j) The active portion in CPP terms:** his "non-zero organization integral" and the light-cone influence volume, and how a 2 mm laser beam, or a
  fibre a few micrometres across, carries photons whose active portion is about a metre across.

## 8. Answer to his "What do you think?"

He's right that an orbital's energy belongs to the whole spread-out state, and the crossings between radii were my models, not his. I've withdrawn them as
tests of his picture. One caution: an orbital's overall size still grows with its level, so any swing that grows with the orbital meets the same problem.
What stays is that a colour is a rate, how many crests pass each second. On his picture a swing radiates at the rate it swings, so whatever the swings'
starts and ends, they have to reverse at the colour's rate. That's still the thing to explain.

On the statistics, he's right that the timing curve alone doesn't give each photon's shape. I read him as saying each photon has its own length and only its
start is random. If so, photons from two separate atoms would arrive at different moments and mostly miss each other at a beam splitter. In fact they match
about 95% of the way. Short packets would fit the timing curve but hardly ever match; long ones would match more but spread the timing curve out of shape.
Only a packet that starts at a set moment after excitation and then fades fits both. That still assumes a detector clicks in step with the light's
strength, which agrees with every lab test so far but isn't yet worked out in CPP.

On the photon as a volume held together by its own organization, I agree in outline. But its width does grow, even in the lab, and photon by photon: a red
laser beam spreads more than a violet one over a few metres, with no large mass nearby. Gravity bends all colours alike, and near Earth it's far too weak,
so it can't be the cause. If a photon's own reinforcement held it to a fixed width, light would have to act on light, and interference wouldn't work as it
does. There's also a puzzle: a laser beam 2 mm wide, or a fibre a few thousandths of a millimetre across, carries photons that his picture makes a metre
wide. His metre is close to the photon's length along its travel, but he meant it sideways, so that match is mine, not his.

I've set out the ion experiment in detail. One ion in a trap is lit by lasers. A lens and a mirror 25 cm away send the light leaving one side back past
the ion into the same detector as the light leaving the other side. Moving the mirror makes the count rise and fall, while the photons still come one at a
time, and the mirror even changes how brightly the ion glows. So I've asked what shape a photon's active part has as it leaves the atom, and what makes
red spread more than violet.

## 9. PD-008

- **Withdrawn:** Claude's radius models (4461 §3.3, 4462 §4) as tests of his picture.
- **Not softened:**
  - the colour is a rate, set by what swings;
  - an orbital's size still scales as n², so a swing that grows with it meets the line-order difficulty;
  - separate atoms' photons with their own lengths and starts spread over the lifetime cannot both fit the histogram and interfere at 95%;
  - diffraction grows with wavelength in the lab and per photon, which lensing cannot give;
  - a self-held fixed width needs a nonlinear relay.
- **Marked:**
  - agreeing on the radius is the convenient branch;
  - the random-start reading of "emitted statistically" is Claude's construal, the convenient (testable) one;
  - the random-start table uses flat packets, one family among others;
  - the detector rule is consistent with tests of emission theory and the rule together, not independently established; owed in CPP, his opening;
  - lensing's colour-independence is taken from general relativity and observation, not derived in CPP;
  - the within-photon nonlinearity branch is not tested by crossing beams;
  - "his metre is the coherence length along the travel" is Claude's reading, convenient, against his 4460 sideways radius, and depends on the c × τ
    convention;
  - "a volume around the ion would reach the mirror" is Claude's reading of his picture.
- **Not claimed:** novelty for Gaussian-beam diffraction, two-photon interference, shaped single-photon emission, self-focusing, coherence, the virial
  theorem or the Eschner experiment.
- Nothing registered.
