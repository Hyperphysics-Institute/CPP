# What the Line Width Counts: the Founder Restates the Results — the Energy of a Single Jump Is Not Measured, the Microvolt Is Not a Measured Maximum, the 1.6 ns Does Not Show the Jump Takes That Long, and Only Self-Interference Over Millimetres Is Known — and Asks for the Line-Width Criterion. His Statement Is Largely Fair, With Adjustments: One Source of the Microvolt Used No Fringes, the Other Rests Partly on Interference Measurements on Other Emitters; Cadmium Light and Single Emitters Reach Further; the Natural Width Is Also Measured; and the Millimetres for Hydrogen's Ultraviolet Line Is Itself a Computation. The Criterion: a Wave Train of N Crests Has a Spread of Colours About 1/N of Its Frequency, so a Sharp Line Means Many Crests; Motion Only Widens a Line, so a Gas's Width Gives a Lower Bound on Most Photons' Crests — Computed for a Hot Discharge, of Order Ten Thousand. On His Own Dipole Picture (4459), That Means an Average of Order a Thousandth of an eV or Less per Out-and-Back

**Patch:** 4467. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4467_fair_statement_and_line_width.md` (answers 4466 §8).
**Script:** `series_standard_model/code/4467_line_width_counts_crests.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the numbers and the central result. It found that the first
draft:
- presented the Lyman-α "millimetres" as measured, as 4466 had (it is computed; room-temperature hydrogen does not emit Lyman-α);
- said "by measurement alone" and "we know" for a computed count;
- gave two numbers wrong (one part in a hundred thousand; a hundred thousand times narrower) and a wrong wavelength range;
- conceded too little on the microvolt's source;
- omitted the measured natural width;
- said "each photon" where the bound covers most;
- conflated crests with reversals;
- omitted the envelope-shape caveat;
- left convenient branches unmarked;
- left the visible-line claim unsourced;
- did not link the question to the open ones;
- dropped wording from the carried items.

All fifteen required changes are taken in, with most of the optional notes; an erratum note is appended to 4466.

## 1. His statement and request

He states: "we do not know how much energy a single jump of the orbital electron CP can emit"; "we cannot say for certain that the maximum amount of energy
that could be emitted in a single jump is millionths of an electron-volt. That is a backward inference from how long the emission appears to be because of the
difference in path length that still produces interference"; "we cannot say the jump between orbitals takes 1.6 ns; therefore, it must be divided into
millions of small increments"; "We only know that the pulse length produces an effect that interferes with itself when the path length is on the order of
millimeters." "Is that a fair statement of the results?" And: "I don't understand this hydrogen line-width criterion that you are using yet. Please explain."

## 2. Is it a fair statement? Largely yes, with adjustments

**Fair:**
- The energy one jump can emit is not measured (4465 §2).
- "Millionths of an electron-volt" is not a measured maximum (4465 §2).
- The lifetime alone does not show that a jump, or a photon, takes 1.6 ns (4466 §2). So "millions of small increments" is not established by measurement;
  it rests on the inference that each photon lasts about the lifetime (4466 §4).

**Adjustments:**
- **Where the microvolt came from.** One source, the radiation-rule estimate (4464 §3, 4465 §2), used no fringes. The other, 10.2 eV ÷ 3.9 million cycles
  (4465 §3), assumes each photon lasts the lifetime. That assumption rests on the natural width and on interference measurements, self-interference and
  two-photon, on other emitters (4466 §3–§4). So for that branch his description is partly right: it is an inference from how long emission appears to
  last, drawn partly from interference, but not from hydrogen's millimetre fringes.
- **Other sources reach further, and one more thing is measured on hydrogen.** Cadmium's red line interferes with itself over tens of centimetres; photons from
  single quantum dots after a short pulse last about as long as the dot's emission time (4466 §3). These are other sources, not hydrogen. Also measured, on
  hydrogen: the 2p level's natural width, about 1/(2π × 1.6 ns), in absorption or excitation; an ensemble width, which applies to each emitted photon only by
  the standard rule that the two lines coincide (4466 §5).
- **The millimetres is itself a computation.** No measured Lyman-α emission profile has been cited; the millimetre figure is the Doppler width computed for an
  assumed temperature (§3). Room-temperature hydrogen does not emit Lyman-α; a discharge does, with hotter atoms, and fast atoms from dissociation (a few eV)
  would widen the line to about 10⁻⁴ of its frequency, about 10⁴ crests, about 1 mm (script). 4466 presented this as measured; an erratum note is appended
  there.
- **Millimetres already mean many crests.** Lyman-α's wavelength is 0.12 μm, so a millimetre holds about ten thousand crests.

**A fairer statement:** the energy of one jump is not measured. The Doppler width computed for a hot discharge implies the light has at least of order 10⁴
crests (a measured Lyman-α profile is owed). For other single emitters (quantum dots, not hydrogen), measured directly, the photons last up to about the
emitter's lifetime. If each cycle comes from one out-and-back of what radiates (his 4459 picture), the average per cycle is of order a thousandth of an eV or
less (10.2 eV ÷ 10⁴, a few ten-thousandths to about a thousandth); about 2.6 millionths if the photon lasts the lifetime. The link from cycles to
out-and-backs is his 4459 picture, not a measurement; in his 4464 postulate, one jump would make one cycle, and that is what the line width rules out (§3).

## 3. The line-width criterion, explained (script)

**The idea in one sentence:** a wave that lasts for only a few crests does not have one sharp colour; the fewer the crests, the more its colour is spread out.

**An everyday version.** Strike a bell and let it ring: you hear a clear pitch. Tap it and damp it at once: you hear a click with no clear pitch. A sound with
many cycles has a sharp pitch; a sound of one or two cycles has none. Light is the same. (An illustration, not evidence.)

**In numbers** (script part 1). A wave train of N crests has a spread of frequencies of about 0.9 ÷ N of its frequency (for a flat train; other envelope
shapes change the factor by about two, so the counts are orders of magnitude, not exact):

| Crests in the train | Spread of colours (share of the frequency) |
|---|---|
| 1 | of order one (0.7 of the peak for a flat cycle; 4464's push-pull gave 1.07) |
| 10 | about 0.09 |
| 100 | about 0.009 |
| 10,000 | about 0.00009 |

So measuring how spread out a line's colour is gives the least number of crests the light can have. A spectrometer measures the spread directly. Chirps,
phase jumps and gaps inside a photon only widen its spectrum, so they cannot make a short photon look narrow.

**Why the result is a lower bound.** In a gas, atoms move toward and away from the spectrometer, and each atom's light is shifted up or down in colour by its
speed (the Doppler effect). Collisions and the instrument also only widen. So the measured width is an **upper limit** on the spread of most photons, and the
number of crests it implies is a **lower limit** on the crests of most of the photons (a small fraction of short ones would barely change the width). For
Lyman-α, computed from the Doppler formula, not measured (script part 2):
- a gas at 300 K: about 1.2 × 10⁻⁵ of its frequency, at least about 7 × 10⁴ crests, about 9 mm (hypothetical: room-temperature hydrogen does not emit);
- a hot discharge at 3000 K: about 3.9 × 10⁻⁵, at least about 2 × 10⁴ crests, about 3 mm;
- fast atoms of about 2 eV from dissociation: about 1.3 × 10⁻⁴, at least about 7 × 10³ crests, about 0.8 mm.

(Claude's general knowledge, no source cited: Balmer-line widths in discharges are measured at 10⁻⁵–10⁻⁴ of their frequency, including fine structure; a
different transition, so not a bound on Lyman-α.) The bound applies to the light as it reaches the spectrometer; a narrow filter in between could lengthen
photons, which does not arise for an unfiltered lamp.

**The same thing as the fringes.** A train of N crests can interfere with its own copy delayed by up to about N crests, and the fringes fade as the delay
approaches N (script part 3). So the spread of colours and the path difference at which fringes fade are one measurement seen two ways (Wiener–Khinchin, 4466
§5). The "millimetres" in his statement and the line width are the same fact, and for Lyman-α both are computed here.

**Why it rules out one jump making one crest.** One crest has a spread of colours of order its own frequency: Lyman-α would be smeared over about 90 to 190 nm,
across the vacuum ultraviolet (script). The exact share depends on the shape of the single cycle (4464's push-pull gave 1.07 of the peak); any one-cycle shape
gives a share of order one. The line is computed to be tens of thousands of times narrower (from the Doppler width; the natural width, measured in absorption,
is some twenty million times narrower).

## 4. Question to the founder (physical picture)

A hydrogen ultraviolet photon, by its colour's sharpness, carries at least of order ten thousand crests. **In his picture, does each crest come from one
back-and-forth of the CP, or can a single jump lay down many crests? If the latter, what in the jump spaces them one wavelength apart? Or does something other
than the CP's motion lay them down?** (This sharpens 4464 §5's first question and 4464 (b).)

## 5. What stays open

- **(a) What lays down the crests:** one per out-and-back (his 4459 picture), many per jump, or something other than the CP's motion (founder question).
- **(b) Carried from 4466:**
  - 4466(a) a photon's length in CPP terms, against self-interference at long delays, including what "length" is in his volume picture (bears on 4464 b, e);
  - 4466(b), the 4465 list: 4465(a) CPP's radiation rule (= 4464 i), with the quantum dipole emission-rate analogue and the CP-in-atom case; and 4464(a) what
    swings at ΔE/h (= 4463 a, 4461 a, 4460 a, 4457 b, 4446 c); 4464(b) one cycle or many; 4464(c) envelope shape against the measured rise-then-fade;
    4464(d) the pilot-wave resemblance (h/p; 4443, 4444); 4464(e) path-difference coherence; 4464(f) 4463 b, c, d, f, j; 4462 a, b; 4444 b, c; 4461 c, d, e,
    i, j, k, l; 4460 b, c, e, g; 4459 c, e, f, i; 4457 d–g; 4456; 4464(g) founder question 4464 §5; 4464(j) velocity or acceleration; 4464(k) the envelope
    reading's slow-transit speed (0.2 m/s); 4464(l) the orientation of his metre; 4464(m) the Eschner both-sides result, with 4461 l;
  - 4466(c) founder question 4466 §6.
- **(c) Founder question 4467 §4.**
- **(d) Dispositions:** his statement assessed (§2): fair on the energy of one jump, the microvolt and the 1.6 ns; adjusted on the microvolt's sources, the
  other measured bounds, the natural width and the computed millimetres. His request for the line-width criterion answered (§3). 4467 §4 sharpens 4464 §5's
  first question and 4464 (b); all stay open. Errata on 4465 §7 and 4464 §3 stand; erratum on 4466 §5/§9 (computed width; this patch); the 4466 todolist
  wording corrected.
- **(e) A measured Lyman-α emission profile** (lamp or beam), to replace the computed Doppler bound.

## 6. Answer to his question

It's largely fair. We don't know by measurement how much energy one jump gives off; "millionths of an electron-volt" isn't a measured maximum; and the 1.6
nanoseconds doesn't show that a jump takes that long, so "millions of small steps" isn't established. Some adjustments. One source of the millionths, my
radiation-rule calculation, used no fringes; the other, dividing 10.2 eV by the cycles in 1.6 ns, assumes each photon lasts that long, which rests partly on
interference measurements on other light sources, so he's partly right there. Other light, like cadmium's red line, interferes with itself over tens of
centimetres. And the "millimetres" for hydrogen's ultraviolet light is itself worked out from how fast the atoms move, not read off a measured spectrum; I
presented it as measured in 4466, and I've corrected that. Even so, a millimetre of that light holds about ten thousand crests. So if each crest comes from
one back-and-forth, as in his antenna picture, each one gives off on average about a thousandth of an electron-volt or less, from the computed width alone.

The line-width idea is like a bell. Let it ring and you hear a clear note; tap it and stop it at once and you hear a click with no note. A wave with many
cycles has a sharp colour; a wave of one or two cycles has its colour smeared out. The fewer the crests, the wider the spread: ten crests spread the colour by
about a tenth, ten thousand crests by about a ten-thousandth. A spectrometer measures that spread, so it gives the least number of crests the light can have.
In a gas the moving atoms widen the line further, so what's seen is an upper limit on most photons' spread, and the crest count is a lower limit. Hydrogen's
ultraviolet line from a hot gas, computed from the atoms' speeds, is about one part in tens of thousands wide, so most of its photons have at least of order
ten thousand crests. That's the same fact as the fringes surviving over a millimetre or so, seen another way.

So I've asked: in his picture, does each crest come from one back-and-forth of the CP, can a single jump lay down many crests (and if so, what spaces them a
wavelength apart), or does something other than the CP's motion lay them down?

## 7. PD-008

- **Agreed:** the energy of one jump is not measured; the microvolt is not a measured maximum; the lifetime alone does not show a jump takes 1.6 ns.
- **Corrected:** 4466's presentation of the Lyman-α width as measured (erratum appended); the draft's "by measurement alone".
- **Not softened:** a sharp line requires many crests; one crest per jump gives a spread of order one, which any observed width rules out.
- **Marked:**
  - "of order a thousandth of an eV per out-and-back" uses his 4459 cycle-per-out-and-back picture; the millionths figure adds the lifetime inference;
  - the Lyman-α widths are computed for stated temperatures; a measured Lyman-α emission profile is owed;
  - that the line width still rules out one jump making one cycle is the convenient branch for Claude (it keeps 4464 standing); it is held because any width
    of the observed order needs of order 10⁴ cycles or more;
  - the reading that the microvolt's sources did not involve interference was the convenient branch; corrected in §2 (the lifetime branch rests partly on
    interference measurements on other emitters);
  - the Balmer-line widths are Claude's general knowledge, unsourced, and a different transition;
  - the bell analogy is an illustration, not evidence.
- **Not claimed:** novelty for the time–bandwidth relation, Doppler broadening or Wiener–Khinchin.
- Nothing registered.
