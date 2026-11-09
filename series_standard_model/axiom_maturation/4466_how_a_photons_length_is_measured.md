# How a Photon's Length Is Measured: the Founder Asks Whether 1.6 ns Is the Photon's Length or the Spread of Times Over Which Many Photons Are Emitted, Each Received Only as a Click. For the Lifetime Measurement, He Has It Right: the 1.6 ns Is a Histogram of Click Times, and By Itself Fixes No Photon's Length, Either Way. A Click Is Short Because a Detector's Response Is Short, Not Because the Photon Is. Other Experiments Measure Length: One Photon Interfering With Itself Delayed (Fringes of Strength V at a Delay d Mean at Least a Fraction V of the Photons Are at Least d Long), and Two Photons Interfering With One Delayed. For Single Emitters After a Short Pulse These Show Photons About as Long as the Emitter's Lifetime; for a Free Hydrogen Atom's Lyman-α Photon the Full Length Has Not Been Measured, and Its Colour's Sharpness in a Gas Gives Only a Lower Bound of Millimetres

**Patch:** 4466. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4466_is_the_lifetime_the_photon_length.md` (answers 4465 §7).
**Script:** `series_standard_model/code/4466_how_a_photons_length_is_measured.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the direct answer and the visibility formulas. It found that
the first draft:
- stated the self-interference bound for every photon, where it bounds a fraction and rests on two assumptions;
- overstated the gas bound;
- omitted that quantum-dot coherence tracks the lifetime only after pulsed excitation;
- leaned on the natural width without its absorption caveat (the convenient branch, unmarked);
- said "not measured" where a lower bound is measured;
- acknowledged Claude's overstatement in a self-excusing way and mis-cited its source;
- had a script part that computed nothing;
- left standard-physics assumptions unmarked;
- led the question;
- mis-stated the plain-language bound;
- did not link the new question to the old one.

All eleven required changes are taken in, with most of the optional notes.

## 1. His question

"what is the experiment that determines whether this is the emission time?" Each photon is "received only as a click, a Dirac delta or spike of some sort";
he took the 1.6 ns to be "a distribution of times for how long it took all the photons to be emitted from a group of atoms (or a single atom measured lots of
times)", "not the length of the photon". "Have I interpreted this experiment correctly?"

## 2. The lifetime measurement: yes, he has it right (script part 1)

The 1.6 ns comes from timing clicks: excite atoms (or one atom, many times), record when each photon is detected, and collect the times into a histogram. The
histogram falls off exponentially with a time constant of 1.6 ns. That is a distribution of emission times over many photons. **By itself it fixes no
photon's length**: a fading 1.6 ns packet emitted at once and a very short burst emitted at a random moment give practically the same histogram (it differs
only within the first burst-length after excitation; script: at most 0.024 in cumulative share for a burst a twentieth of a lifetime long). That is what
4452 §2 and 4462 §2 said; he asked it in 4462 and made the point in 4454 and 4463. One step of his goes past the measurement, though: it does not show that
1.6 ns is a photon's length, and it does not show that it isn't.

**Claude's overstatement.** Claude's 4465 chat reply headed the point "Hydrogen's emission time" and said the line "takes 1.6 nanoseconds to emit". Both went
beyond the measurement, which gives the spread of emission times. The "if" in the next sentence was meant for the per-photon reading, but it did not cover
that sentence, nor 4465 §7's "hydrogen's emission time" (erratum note appended to 4465).

**On the click.** A click is short because a detector's response is short: one electron is released at one place and amplified into a pulse. Any photon,
long or short, ends in one click. So the click does not show that the photon is short, any more than it shows that it is long. 4462 §2 recorded this ("one
detection gives one time, not a length"). That one click per photon follows from the standard detector rule; CPP's detector rule is owed (4463 c; 4459 d).

## 3. The experiments that measure a photon's length (script parts 2–3)

**One photon interfering with itself, delayed.** Split each photon's light in an interferometer whose two arms differ in length, and recombine it. Light from
independent emitters makes fringes only through each photon overlapping its own delayed copy; terms between different photons average out because their
phases are random, and the adding is strict (4459 §2). So **fringes of visibility V at a delay d mean that at least a fraction V of the photons are at least
d long.** Random phase jumps or gaps inside a photon only lower the visibility, so the bound stands. Here "length" means the stretch over which what arrives
can interfere with itself, including any gaps; the test gives no upper limit. For a fading packet the visibility falls as e^(−d/2τ) (0.61 at one lifetime);
for a short burst it is gone after the burst's length (script).
- Michelson used this on spectral lamps. Cadmium's red line gives fringes over path differences of tens of centimetres, delays up to about a nanosecond.
  (Sodium's D line is a doublet, so its fringes fade and return every 0.3 mm or so; its overall fade sets delays of tens of picoseconds.) In a gas the atoms'
  motion broadens the line and lowers the visibility, so a gas gives a **lower bound** on the photons' length (in the sense above), not each photon's full
  length.
- Photons from single quantum dots, after a short excitation pulse, are routinely measured this way, one at a time; the visibility falls over delays
  comparable to the dot's emission time (hundreds of picoseconds to a nanosecond), and spectral wandering often makes it shorter. Under weak steady laser
  driving, a single emitter's photons are longer still, taking the laser's coherence (Matthiesen and others, 2012). That is further evidence against short
  bursts, not a measurement of the lifetime packet.

**Two photons interfering, one delayed.** Send two photons into a beam splitter, delaying one. They interfere (leave together) only as far as they overlap in
time; the effect fades as the delay grows past their length (e^(−d/τ) for fading packets; script part 3). Photons from two trapped ions interfere with about
95% contrast after dark-count subtraction (Maunz and others, 2007; 4462 §2, 4463 §3), which shows their starts are fixed to well within a lifetime. Time-
resolved versions (Legero and others, 2004) see the interference unfold within the photons' duration; those were cavity photons whose length was set by the
pump laser (microseconds), not by a lifetime, so they show directly that one photon is spread out in time, not that it lasts about a lifetime.

## 4. So where does that leave the 1.6 ns for hydrogen? (script part 4)

- **Measured:** the click-time histogram (1.6 ns, the spread of emission times); the 2p level's natural width, about 1/(2π × 1.6 ns), measured mostly in
  absorption or excitation (an ensemble width; 4462 §2).
- **Measured for other single emitters after a short pulse:** photons about as long as the emitter's lifetime, by self-interference and two-photon
  interference.
- **Not measured:** the full length of one Lyman-α photon from a free hydrogen atom. To Claude's knowledge, no one has done the self-interference test on
  single hydrogen atoms. On a gas, emission gives only a lower bound, set by the atoms' motion: at room temperature the Doppler width is about 3 × 10¹⁰ Hz
  (1 part in 10⁵), a coherence of a few tens of picoseconds, millimetres to a centimetre, of order 10⁴–10⁵ cycles (script; hotter discharges give less).
- **So "each Lyman-α photon lasts about 1.6 ns" is an inference**, from the natural width plus what is measured for other single emitters. A strong one, in
  Claude's view, but not a measurement on hydrogen.

## 5. What this means for 4464–4465

The 2.6 × 10⁻⁶ eV per cycle in 4465 rests on that inference, as 4465 said. The line-width failure of a one-cycle photon (4464 §3) does not rest on the
per-photon-length inference. It rests on the emitted light. Even motion-broadened lamp lines have widths of order 10⁻⁶ of their frequency; hydrogen's own
room-temperature Lyman-α emission is about 1 part in 10⁵ wide (about 30 GHz); one cycle would be about 1. By Wiener–Khinchin the emitted spectrum and the
self-interference fringes are one measurement seen two ways, not two independent ones. The natural width, about 1/(2π × 1.6 ns), is measured on the 2p
level, mostly in absorption or excitation; it is an ensemble width, and applying it to the emitted photons uses the standard rule that the two lines
coincide.

## 6. Question to the founder (physical picture)

Light from a cadmium or sodium lamp, split and recombined with one path centimetres longer than the other, still makes fringes; as the extra path is made
longer still, the fringes fade away. **In his picture, what of one photon meets what at the recombining mirror, and what sets the extra path at which the
fringes fade?**

## 7. What stays open

- **(a) A photon's length in CPP terms**, against self-interference at long delays, including what "length" is in his volume picture (bears on 4464 b, e).
- **(b) Carried from 4465, by letter:** (a) CPP's radiation rule (= 4464 i), including the analogue of the quantum dipole emission rate and the CP-in-atom
  case; and 4464's (a) what swings at ΔE/h (= 4463 a, 4461 a, 4460 a, 4457 b, 4446 c); (b) one cycle or many; (c) envelope shape against the measured
  rise-then-fade; (d) the pilot-wave resemblance in CPP terms (h/p; 4443, 4444); (e) path-difference coherence; (f) its carried list (4463 b, c, d, f, j;
  4462 a, b; 4444 b, c; 4461 c, d, e, i, j, k, l; 4460 b, c, e, g; 4459 c, e, f, i; 4457 d–g; 4456); (g) founder question 4464 §5; (j) velocity or
  acceleration as what radiates; (k) the envelope reading's slow-transit speed (0.2 m/s); (l) the orientation of his metre; (m) the Eschner both-sides
  result, with 4461 l.
- **(c) Founder question 4466 §6.**
- **(d) Dispositions:** his 4466 question answered (§2–§4): his reading of the lifetime measurement is right; the photon's length is measured by other
  experiments, and for hydrogen it is inferred, with a measured lower bound. 4466 §6 sharpens 4464 §5's second question (path-difference coherence) for lamp
  light; both stay open, as (c) here and 4465 (b)(g). Erratum notes appended to 4465 §7 ("hydrogen's emission time") and to 4464 §3 ("an atom or a quantum
  dot": no single-atom first-order measurement after pulsed excitation is cited). 4465 (c) dispositions stand.

## 8. Answer to his question

Yes, for that measurement he's interpreted it correctly. The 1.6 nanoseconds comes from timing clicks: excite the atoms, note when each photon arrives, and
make a histogram. That's the spread of emission times over many photons, and on its own it doesn't fix how long any one photon is, either way. My wording,
calling it "hydrogen's emission time" and saying the line "takes 1.6 nanoseconds to emit", went further than that measurement.

But the click doesn't show the photon is short either. A detector always answers with one quick click, whatever arrives. A photon's length is measured
differently: split its light, make one path longer, and bring it back together. A photon can only make fringes by overlapping its own delayed copy, so
fringes at a delay mean that at least some of the photons, as many as the fringes' strength shows, are at least that long. Lamp light keeps making fringes
with one path centimetres longer, and photons from single quantum dots, measured one at a time after a short pulse, last about as long as the dot takes to
emit. Two photons meeting at a beam splitter tell the same story.

For a free hydrogen atom's ultraviolet photon, no one has measured the full length, so "each one lasts 1.6 nanoseconds" is an inference. Even for hydrogen
gas, though, the sharpness of its emitted colour shows its photons are at least a few millimetres long; that's a lower limit, set by the atoms' motion. I've
asked, in his picture, what of one photon meets what when lamp light makes fringes across a longer path, and what makes the fringes fade as the path grows.

## 9. PD-008

- **Agreed:** the lifetime measurement is a histogram of click times and fixes no photon's length on its own; Claude's 4465 wording went beyond it.
- **Not softened:** a click does not show the photon is short; self-interference of visibility V at a delay d requires at least a fraction V of the photons
  to be at least d long; the emitted light's spectrum rules out a one-cycle photon regardless of the histogram.
- **Marked:**
  - for hydrogen Lyman-α, the per-photon length is an inference; only a lower bound (millimetres) is measured, from the emitted spectrum of a gas;
  - the self-interference bound assumes strict linear adding (4459 §2) and random relative phases between independent emitters; the click's shortness is
    standard detector physics, with CPP's rule owed;
  - the cadmium and sodium figures are lamp (Doppler-broadened) values, lower bounds on photon length;
  - that the 4464 line-width failure survives his point is the convenient branch for Claude (it keeps 4464 standing); it is held because it uses the emitted
    light's spectrum, not the natural width;
  - "a strong inference" is Claude's judgement.
- **Not claimed:** novelty for Michelson interferometry, first-order coherence, two-photon interference or quantum-dot coherence measurements.
- Nothing registered.
