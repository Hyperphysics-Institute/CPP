# Where the Microvolt Comes From: the Founder Asks What Experiment Shows a Single Emission Swing Gives at Most Millionths of an eV. None Does Directly. The 4464 Figure Is a Calculation With the Standard Radiation Rule (Larmor), Not a Measured Ceiling; It Becomes an Approximate Ceiling Once the Colour Fixes the Swing's Duration and the Energy Available Caps Its Speed. The Free-Charge Rule Is Measured From a Single Electron's Femtowatt to a Storage Ring's Giga-Electron-Volts Lost per Turn, and Its Quantum Form Is Tested Inside Atoms by Every Measured Lifetime; the Arithmetic of the Lifetime (About Four Million Cycles for Lyman-α) Gives an Average of About 2.6 Millionths of an eV per Cycle, if Each Photon Is Emitted Over the Lifetime. Radiating 10.2 eV in One Rise and Fall Would Take About 7 MeV of Kinetic Energy

**Patch:** 4465. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4465_which_experiment_microvolt.md` (answers 4464 §3, §8).
**Script:** `series_standard_model/code/4465_where_the_microvolt_comes_from.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the numbers and the direct answer. It found that the first
draft:
- put his "at most" on 4464;
- called the figure "not a ceiling" while giving a speed cap that makes it roughly one;
- gave a "fifteen times light speed" that is an artefact of the slow-speed formula (about 7 MeV is the physical statement);
- said the rule was never tested inside an atom, and called the agreement independent, where its quantum form is tested by every lifetime and the agreement
  is expected;
- gave the 2p lifetime to four figures as measured;
- simplified Project 8's result;
- cited the envelope inference's basis incompletely.

All eight required changes are taken in, with most of the optional notes.

## 1. His question

"What is the experiment that gives evidence that a single emission swing can, at most, give millionths of an eV?"

## 2. The direct answer: no experiment measures it

No experiment measures the energy radiated by one swing of an electron inside an atom. In standard physics atomic emission is not described as a classical
swing, so no such measured quantity exists there either. The 4464 figure (about 2 × 10⁻⁶ eV) is a **calculation**: the standard radiation rule (Larmor's)
applied to one smooth rise and fall lasting 3.4 × 10⁻¹⁶ s, with a top speed Claude chose (the speed an electron would have if all 10.2 eV were kinetic
energy). The rule gives more for a faster swing, in proportion to the top speed squared (script part 1):

| Top speed | One rise and fall radiates |
|---|---|
| 1.9 × 10⁶ m/s (10.2 eV of kinetic energy) | 1.9 × 10⁻⁶ eV |
| 2.2 × 10⁶ m/s (hydrogen's ground-state orbital speed, 13.6 eV) | 2.5 × 10⁻⁶ eV |
| 2.2 × 10⁷ m/s (ten times that; about 1.4 keV of kinetic energy, not available to a CP with about 10 eV) | 2.5 × 10⁻⁴ eV |

**It is not a measured ceiling.** As a calculation it becomes an approximate ceiling once two things are fixed: the duration, set by the colour, and the
top speed, capped by the energy available. (The cap works through the speed: the radiated energy comes from the work the fields do on the CP, not from a
store of kinetic energy.) A swing with sharper edges, at the same top speed and duration, radiates more, but at frequencies far above Lyman-α; smooth
shapes radiate about the least. So 4464 did not say "at most". The "at most" in his question goes further than the figure itself, which 4464 already marked as
scaling with the top speed squared from a chosen speed (4464 §3, §9). As a summary of the argument, though not of any measurement, "at most" is fair.

**What the energy would need.** Radiating 10.2 eV in one rise and fall of that length would need, by the rule's relativistic form for straight-line motion
(Liénard's, which is Larmor's with the speed replaced by γ × speed), γv ≈ 15c, about 7 MeV of kinetic energy (script part 1b). A CP has about 10 eV (about
14 eV in hydrogen's ground state), which caps its speed near 2 × 10⁶ m/s. That is an argument from the rule plus the energy available, not a measurement.

## 3. The evidence that stands behind it

**First, the radiation rule is measured on free charges** (script part 2):
- **One electron.** Project 8 (Asner and others, Phys. Rev. Lett. 114, 162501, 2015) detected the radio emission of single 30 keV electrons circling in a
  field of about 0.95 T, near 26 GHz. The rate at which each electron's frequency rose as it lost energy gave a radiated power of 1.61 fW, against the rule's
  free-space 1.74 fW (script: 1.75 fW). The difference is expected, because the electron radiated inside a waveguide.
- **Storage rings.** An electron circling in a ring loses energy to synchrotron light each turn by the rule's relativistic form, 88.5 keV × (energy in
  GeV)⁴ ÷ (bending radius in m). At LEP's 104.5 GeV that is about 3.4 GeV per turn, which the accelerating cavities had to supply every turn. Every
  synchrotron light source is designed on it.
- **Antennas.** An antenna's radiated power for a given current is the same rule, with the fields of many slowly drifting electrons adding together.

What has not been tested is the classical rule applied to a single swing inside an atom; no such swing exists in standard physics. The rule's quantum dipole
form, the emission rate from the charge's dipole matrix element, is tested inside atoms by every measured lifetime, including hydrogen 2p. In CPP the
radiation rule, classical or otherwise, is owed (4464 i).

**Second, the arithmetic of the lifetime** (script part 3, which uses no radiation rule). Hydrogen's 2p state lives 1.596 ns by theory; fast-beam
measurements, timing the Lyman-α light along a beam of excited atoms (late 1960s onward), agree within their percent-level uncertainty. That is about 3.9
million cycles of Lyman-α. If each photon is emitted over the lifetime, the average energy leaving per cycle is 10.2 eV ÷ 3.9 million ≈ 2.6 × 10⁻⁶ eV. That
is an **average**, not a limit on any one swing, and it rests on the inference of 4462–4463 that each photon is emitted over the lifetime, not in a burst at a
random moment within it. That inference comes from two-photon interference between separate emitters and the transform-limited line width (4462 §2, 4462 a),
together with the detector rule (4463 §3). He has questioned the link (4463 §1), and the detector rule in CPP is owed (4463 c).

**The two agree in order of magnitude.** In standard physics that agreement is expected, not a coincidence: the lifetime is computed from the quantum form of
the same radiation rule, and the classical radiation-damping estimate of 4451 §2 (0.66 ns against 1.6 ns) is the classical form of it. So the agreement shows
that the rule's scale holds for atomic emission on average, in standard physics; it does not show that a CP swinging in an atom follows the free-charge rule.

## 4. What this changes in 4464

- 4464's energy failure stands as an argument (the rule plus the energy available caps one smooth rise and fall far below 10.2 eV), not as a measurement.
- The other three 4464 failures (line width, length, path-difference coherence) are measurements, independent of any radiation rule.

## 5. Question to the founder (physical picture)

The 4464 questions stand: how many times the radiated DP arc-separation swings to one side and back in one photon, and whether it follows the CP's speed or
its speeding up and slowing down; and what makes a laser's photons keep interfering over a longer path difference. The answer to the first decides whether
this energy argument applies to his picture at all.

## 6. What stays open

- **(a) CPP's radiation rule** (= 4464 i): how much a swing of given speed, duration and shape radiates, including the analogue of the quantum dipole emission
  rate and the CP-in-atom case.
- **(b) Carried from 4464, by letter:** (a) what swings at ΔE/h (= 4463 a, 4461 a, 4460 a, 4457 b, 4446 c); (b) one cycle or many; (c) envelope shape against
  the measured rise-then-fade; (d) the pilot-wave resemblance in CPP terms, giving h/p (4443, 4444); (e) path-difference coherence; (f) its carried list
  (4463 b, c, d, f, j; 4462 a, b; 4444 b, c; 4461 c, d, e, i, j, k, l; 4460 b, c, e, g; 4459 c, e, f, i; 4457 d–g; 4456); (g) founder question 4464 §5 (how
  many swings per photon, speed or acceleration; what keeps laser photons interfering over a longer path difference); (j) velocity or acceleration as what
  radiates; (k) the envelope reading's slow-transit speed (0.2 m/s); (l) the orientation of his metre; (m) the Eschner both-sides result, with 4461 l.
- **(c) Dispositions:** his 4465 question answered (§2–§3); 4464 (i) restated as (a) here; 4464 (h) dispositions stand.

## 7. Answer to his question

There isn't one. No experiment measures what a single swing inside an atom radiates. The "millionths of an electron-volt" was my calculation with the
standard rule for how much a moving charge radiates, using a top speed I chose. It's an estimate, not a measured limit. A faster swing radiates more, in
proportion to the speed squared, but with the energy a CP actually has, it works out to roughly a ceiling for a smooth swing. To radiate 10.2 eV in one quick
rise and fall by that rule, the CP would need about seven million electron-volts of energy to move fast enough; it has about ten.

The rule itself is measured on free electrons, from a single electron circling in a magnet and giving off under two femtowatts, up to big electron rings
that lose billions of electron-volts every turn, as the rule says. Its quantum form is checked inside atoms by their measured lifetimes, while CPP's own
version is still owed. Separately, hydrogen's emission time, 1.6 nanoseconds, is about four million cycles. If each photon is given off over that whole time,
the average per cycle is about 2.6 millionths of an electron-volt. But that "if" rests on the inference he's questioned, so it's an average under that
inference, not a measured limit on any one swing.

## 8. PD-008

- **Clarified:** 4464 did not say "at most"; its figure is an estimate that grows with the swing's speed squared, roughly a ceiling only once the colour
  fixes the duration and the energy caps the speed.
- **Not softened:** by the standard rule, a CP with about 10 eV cannot radiate 10.2 eV in one smooth rise and fall; the other three 4464 failures are
  measurements.
- **Marked:**
  - the sin² shape is Claude's choice; smooth shapes radiate about the least for a given top speed and duration; sharper ones radiate more, at far higher
    frequencies;
  - the free-charge rule is measured, and its quantum form tested by atomic lifetimes; CPP's rule is owed;
  - the per-cycle average rests on the emission-over-the-lifetime inference he has questioned;
  - the agreement between the estimate and the average is expected in standard physics, not independent evidence;
  - defending 4464's energy failure is the convenient branch for Claude; it is held as an argument, not a measurement.
- **Not claimed:** novelty for Larmor's or Liénard's rule, synchrotron radiation, Project 8's measurement, the quantum dipole emission rate or the hydrogen 2p
  lifetime.
- Nothing registered.
