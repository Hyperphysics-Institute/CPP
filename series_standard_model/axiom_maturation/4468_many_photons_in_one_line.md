# Many Photons in One Line: the Founder Reads the Line Width as the Statistical Spread of Many Photons' Energies From the High-to-Low Drop, Not as One Photon With Ten Thousand Crests. The First Half Is Right: a Measured Line Is Built From Many Photons, and in a Low-Pressure Gas Most of Its Width Is a Spread of Different Photons' Energies — Though the Cause There Is the Atoms' Motion, Not a Varying Jump. With the Motion Removed, What Is Left Is Each Photon's Own Spread: Photons From Like Emitters Behave as Identical. And the Second Half Does Not Follow: Most Photons' Own Spreads Must Fit Inside the Line (a Few Short Ones Would Only Add a Faint, Broad Pedestal), and a Photon Narrower Than the Line Must Hold at Least About 0.9 ÷ (the Line's Width) Crests. Short Independent Photons Cannot Make a Narrow Line However Their Energies Are Distributed. Both Readings Hold at Once: Many Photons, Most of Them Long

**Patch:** 4468. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4468_line_width_as_energy_distribution.md` (answers 4467 §2–§3).
**Script:** `series_standard_model/code/4468_many_photons_in_one_line.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the main result and the Doppler-free citation. It found that
the first draft:
- repeated "each photon" where the bound covers most;
- left out the independence assumption behind the grating argument, and the phase-locked exception;
- credited Claude's Doppler mechanism to him as "exactly his picture";
- missed the measurement that tests his jump-energy mechanism (two-photon interference);
- gave a crude one-crest figure, and a middle-row number that was a sampling artifact;
- cited the Doppler-free paper incompletely;
- did not qualify the Doppler share;
- asked a question that could not discriminate;
- dropped carried wording;
- missed new items and a convenient branch.

All eleven required changes are taken in, with most of the optional notes.

## 1. His reading

"the line width represents the spectrum of energy distributions of photons emitted by the hydrogen from a higher to a lower energy jump. Thus, the line
intensity at each frequency corresponds to the statistical distribution of the energy from a high- to low-energy emission drop"; "Rather than saying the line
width represents a photon with 10,000 crests, we mean that over the line width, the line may contain many different photon energies, distributed statistically
across it." "Do you think that is correct?"

## 2. The first half is right, with a different cause

- **A measured line is built from many photons.** A spectrometer collects many photons and shows how many arrive at each colour. That is a statistical
  distribution, as he says. His statistical reading was accepted for the timing in 4454 and 4462 §2; it holds for the colour too.
- **In a low-pressure gas, most of the width is a spread of different photons' energies.** Each atom moves at its own speed toward or away from the
  spectrometer, and its photon is shifted up or down in colour accordingly (the Doppler effect). So a gas's line is mostly a distribution of photons of
  different energies, as he says, though the cause here is the atoms' motion, not a varying jump. (In denser discharges, collisions also widen each photon's
  own spread, which only strengthens the bound of §3.) This is what 4467 §3 meant by the measured width being an *upper* limit on most photons' spread, and the
  crest count a *lower* limit.
- **When that distribution is removed, the line becomes much narrower.** Doppler-free methods pick out only the atoms that are not moving along the beam.
  Applied to hydrogen's red Balmer-α line, they resolved structure (the Lamb shift) hidden inside the Doppler-widened line (Hänsch, Shahin and Schawlow,
  "Optical resolution of the Lamb shift in atomic hydrogen by laser saturation spectroscopy", Nature Physical Science 235, 63, 1972). So the gas line is indeed
  mostly a spread of many atoms' slightly different colours, and each atom's own response is far narrower. (Those measurements are in absorption; carrying
  them to emitted photons uses the standard rule that the lines coincide, 4466 §5. It is a different line, red, n = 3 → 2, from the ultraviolet Lyman-α, so it
  shows how a discharge line is built, not Lyman-α's photon length.)

**What is left when the motion is removed is each photon's own spread, not a spread of jump energies.** Once the motion is removed, the remaining width is the
natural width (4451 §3, 4466 §5). If that width were made of photons with different definite energies, photons from the same kind of emitter would differ in
colour and could be told apart. Then two of them meeting at a beam splitter would not leave together. Measured, they do: about 95% for two trapped ions (Maunz
and others, 2007), and 99.6% for successive photons from one quantum dot (Somaschi and others, 2016) (4462 §2). So at that level, each photon carries the
whole spread itself. These are other emitters, not hydrogen. (Energy-resolving detectors are far too coarse, of order 10⁻³ or worse, to test a photon's
energy at this level directly; the interference and grating measurements are the operative tests.)

## 3. The second half does not follow (script)

**Most photons' own spreads have to fit inside the line.** The line is the sum of all the photons' own spectra. (This holds when the photons' phases are random
relative to each other, as for independent atoms in a lamp. Short packets whose phases are locked to each other can build narrow lines, as a mode-locked
laser's pulse train does, but only by forming one long coherent wave, and the overall spread stays as wide as one packet's; a lamp's independent atoms do not
do this.) A photon that lasts N crests has a spread of colours of about 0.9 ÷ N of its frequency, whatever its average energy (4467 §3). So if photons were
short, each would on its own spread across a wide band, and the sum of many such photons could not be narrower than that band, however their energies were
distributed. In the script:

| Photons | Spread of their energies | Width of the resulting line |
|---|---|---|
| 1 crest each | 1 part in 10⁴ | of order one (0.9 in this simple model; 0.7–1.07 for real single cycles, 4467 §3) |
| 10⁵ crests each | 1 part in 10⁴ | about 1 part in 10⁴ (the spread of energies) |
| 10⁵ crests each | none (all alike) | about 1 part in 10⁵ (each photon's own spread) |

So "many different photon energies distributed across the line" and "most photons have at least ten thousand crests" are not alternatives. **Both hold at
once**: the line is many photons of slightly different energies, and most of them must be long enough to be narrower than the line. A line of width w needs
most of its photons to have at least about 0.9 ÷ w crests (a small fraction of short ones would show only as a faint, broad pedestal in the wings); it says
nothing about how much longer they are.

**The fringes say the same, photon by photon.** Lamp light split and recombined with one path longer still makes fringes. A photon can only make fringes by
overlapping its own delayed copy, so fringes at a delay need photons at least that long, whatever the spread of energies among them; the spread only lowers the
fringes further (4466 §3). This rests on strict adding and random phases between independent atoms (4466 §9).

**In his picture.** If a photon in his picture has a definite energy but is only one or a few crests long, then by this rule its colour is not definite: a
grating would spread each such photon over a wide band of angles. A sharp line from such photons would need a different rule linking a photon's length to its
spread of colours. That would be a CPP-specific claim, and it would have to meet the fringe and two-photon measurements.

## 4. Question to the founder (physical picture)

A grating sends each colour to its own angle. **In his picture, when one photon of a single, definite energy, but only one or a few crests long, reaches a
grating, does it go to one sharp angle, or is it spread over a range of angles? And what in the photon decides which?** (This bears on 4466 (a), a photon's
length in CPP terms, and on 4467 §4, what lays down the crests.)

## 5. What stays open

- **(a) The rule linking a photon's length to its spread of colours in CPP** (new): the standard rule (spread about 0.9 ÷ crests for a flat train, within about
  2 for other shapes) underlies 4464–4468; with it, whether a photon can have a definite energy while short (§3, "In his picture").
- **(b) Carried from 4467:**
  - 4467(a) the 4466 carried list: 4466(a) a photon's length in CPP terms, including what "length" is in his volume picture (bears on 4464 b, e); 4465(a)
    CPP's radiation rule (= 4464 i), with the quantum dipole emission-rate analogue and the CP-in-atom case; 4464(a) what swings at ΔE/h (= 4463 a, 4461 a,
    4460 a, 4457 b, 4446 c); 4464(b) one cycle or many; 4464(c) envelope shape against the measured rise-then-fade; 4464(d) the pilot-wave resemblance (h/p;
    4443, 4444); 4464(e) path-difference coherence; 4464(f) 4463 b, c, d, f, j; 4462 a, b; 4444 b, c; 4461 c, d, e, i, j, k, l; 4460 b, c, e, g; 4459 c, e,
    f, i; 4457 d–g; 4456; 4464(g) founder question 4464 §5; 4464(j) velocity or acceleration; 4464(k) the envelope reading's slow-transit speed (0.2 m/s);
    4464(l) the orientation of his metre; 4464(m) the Eschner both-sides result, with 4461 l;
  - 4467(b) founder question 4466 §6;
  - 4467(c) founder question 4467 §4 (does each crest come from one back-and-forth of the CP, can a single jump lay down many crests and what spaces them a
    wavelength apart, or does something other than the CP's motion lay them down), sharpening 4464 §5's first question and 4464 (b);
  - 4467(d) a measured Lyman-α emission profile (lamp or beam), to replace the computed Doppler bound.
- **(c) Founder question 4468 §4.**
- **(d) Dispositions:** his reading assessed (§2–§3): right that a line is many photons and that a gas's width is mostly a spread of their energies (from
  motion); not right that a spread of jump energies makes up the natural width (two-photon interference, other emitters), nor that this replaces long photons.
  4467(e) dispositions stand: 4466 dispositions and errata stand, including the 4466 erratum added in 4467.
- **(e) The independence assumption:** whether in CPP independent atoms' photons have random relative phases, which both the grating and fringe arguments use
  (§3).

## 6. Answer to his question

Half of it is right. A measured line is built from many photons, and in a gas most of its width is a spread of different photons' energies, as he says, though
the cause there is the atoms moving at different speeds, which shifts each photon's colour slightly. That's why I called the crest count a lower limit. When
experimenters pick out only the atoms that aren't moving along the beam, hydrogen's red line gets much narrower (measured in absorption), showing each atom's
own colour is far sharper than the gas's line. And what's left then isn't a spread of different jump energies: photons from like emitters behave as identical
when they meet at a beam splitter, so each carries the remaining spread itself.

But it doesn't replace long photons. Most photons' own spread of colour has to fit inside the line, and a photon can only be that sharp if it's long: a photon
of one crest is spread across a huge band all by itself, and no way of distributing many such independent photons makes a narrow line. So both are true at
once: the line is many photons of slightly different energies, and most of them have to have at least of order ten thousand crests (from the width computed
for a hot discharge, 4467). Lamp light making fringes across a longer path says the same thing photon by photon.

So I've asked: in his picture, when one photon of a single energy but only a crest or two long reaches a grating, does it go to one sharp angle or get spread
out, and what decides that?

## 7. PD-008

- **Agreed:** a line is many photons; a low-pressure gas's width is mostly a distribution of their energies (from motion); the crest count is a lower limit.
- **Not softened:** most photons' own spread must fit inside the line; short independent photons cannot make a narrow line by any distribution of energies.
- **Marked:**
  - the rule "spread about 0.9 ÷ crests" is standard wave physics; CPP's version is owed (new item a);
  - the Doppler-free hydrogen measurements are in absorption, and on Balmer-α, a different transition from Lyman-α;
  - the grating argument, like the fringe argument, assumes random phases between photons from independent atoms; phase-locked short packets are the exception
    (mode-locked lasers), and do not apply to a lamp;
  - that the residual width is each photon's own spread rests on two-photon interference on other emitters (ions, quantum dots), not hydrogen;
  - treating his "distribution of energies" as the Doppler distribution was Claude's reframing; it would let the half credited to him rest on a mechanism he
    did not propose. Corrected in §2 (his jump-energy mechanism is assessed separately against two-photon interference);
  - holding that his reading does not replace long photons is the convenient branch for Claude (it keeps 4464–4467 standing); it is held because the script
    shows short independent photons cannot make a narrow line.
- **Not claimed:** novelty for inhomogeneous broadening, Doppler-free spectroscopy, mode-locking or the time–bandwidth relation.
- Nothing registered.
