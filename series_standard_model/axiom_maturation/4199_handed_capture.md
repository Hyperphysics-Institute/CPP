# Handed Capture — the Founder's Neutrino Picture Does Bear on the Right-Handed Question

**Patch:** 4199. **Lane:** EW. **Session:** 236. **Last ID of block 4100–4199; the gate is switched
to 4200–4299 in this commit.**
**Founder verbatim:** `founders_voice/4199_how_the_neutrino_is_formed.md`.
**Verify:** `series_standard_model/code/4199_handed_capture_checks.py`.
**Corrects:** 4197 §3.2 and 4198 §1 (my reading of where the neutrino's unit comes from).
**Status:** the founder's picture, plus ONE trial rule of mine, checked against three measured facts.
Nothing adopted.

---

## 1. The picture, and what it repairs

The founder: the linear −eCP escapes (W⁰ catalysis, W⁰ → W⁻); moving through the Sea it **captures an
orbital DP** and so becomes a complete electron; the DP-arcs thrown up by that capture organise on a
nearby DP, and **the spin induced there is the neutrino, carrying the anti-spin of the captured
orbital DP.**

- **It agrees with SF-4** (*"unbound 3D orbital ZBW configuration of dipole-pair structures with no
  central CP anchor"*): a spinning Sea DP with nothing at its centre.
- **It removes 4198's mismatch.** I read the antineutrino as *the linear mode set free*, and could
  not square "linear" with SF-4's "orbital". In his picture the linear −eCP simply **has no orbital
  DP yet**; the orbital motion is created at capture, **in a pair** — one spin on the electron's new
  DP, the opposite spin left in the Sea. **4198's mode term survives as bookkeeping but is re-read:**
  −1 is *an orbital DP not yet acquired*; the antineutrino is *the Sea's receipt for supplying it*.
- **Angular momentum is conserved by construction**, which the corpus needs and I had not supplied.

## 2. Why it bears on handedness after all

Everything in the capture as described — attraction to the +eCP end, DP-arcs — is mirror-symmetric
(4069/4070). **So the capture cannot by itself decide which way round the new DP orbits** relative to
the −eCP's motion. But measured beta electrons are left-handed, by −v/c. **So this is the place the
one primitive sign must act: the sense in which a moving bare CP's captured DP orbits, relative to
its motion.** As a rule:

> **The weak vertex selects q (v̂·A) = +1.**

**This is the same term as 4193's gate, read in the other direction.** 4193/4196: *given the spin, the
displacement is biased along qA* (neutral current). Here: *given the motion, the spin is acquired
along q v̂* (charged current). **One pseudoscalar, q (v̂·A), favoured positive, covers both.**

Three things then follow without further input:

1. **−v/c, in kind.** The founder says the DP is captured *"by its velocity through the DP Sea."* The
   velocity is the only axis available; at rest there is none, and no sense can be preferred. A
   handedness that grows with speed and vanishes at rest is what is measured. *(The linear form
   −v/c is not derived.)*
2. **Right-handed states do not couple — 4198's first gap.** A right-handed electron is not a
   different particle; it is an electron whose motion has since been turned against its spin. The
   vertex *is* the acquiring (or, reversed, the shedding) of the orbital DP, and that is handed
   relative to the motion. **An electron moving the wrong way round its spin cannot shed its DP by
   the reverse of the process that would have given it one.** T₃ = 0 for right-handed states is that
   statement.
3. **A correlation the picture did not set out to explain.** Rows verbatim (D-11):

```
helicity h = sign(v_hat . A); rule: q*h = +1

object           q  h required    measured helicity
electron        -1          -1         left  (-v/c)
positron         1           1         right (+v/c)
antineutrino     1           1                right
neutrino        -1          -1                 left

beta-minus, one axis: electron velocity v_e = +1 or -1, antineutrino v_nu = +1 or -1
 v_e  v_nu  A_e  A_nu  spins opposite (founder)   allowed?
   1     1   -1     1                      True   YES: same direction
   1    -1   -1    -1                     False   no
  -1     1    1     1                     False   no
  -1    -1    1    -1                      True   YES: same direction

=> with anti-parallel spins the two leptons must leave in the SAME direction:
   electron-antineutrino correlation a = +1, the measured value for pure Fermi (0+ -> 0+) decays.
   Gamow-Teller decays (a = -1/3) need PARALLEL lepton spins, which the picture as stated does not supply.
```

   **Anti-parallel spins (the founder's statement) plus the handed rule force the electron and the
   antineutrino out in the same direction: a = +1, the measured electron–antineutrino correlation for
   pure Fermi decays.**

## 3. What it does not cover

- **Gamow–Teller decays** need the two leptons' spins *parallel* (a = −1/3; the neutron is mostly
  this). The picture as stated always gives anti-parallel. The quark core's own spin would have to
  turn over and hand one unit to the pair; nothing here says how.
- **For the neutrino, q is a particle/antiparticle label, not a polarity** — it has no unpaired CP.
  What in a spinning Sea DP distinguishes ν from ν̄ is not identified.
- **Range** (4198's second gap) — untouched; SF-2's W⁰ catalyst framework not yet read.

## 4. PD-008

Convenient branch: **yes, in part** — it puts the primitive on the CP at a local vertex, my 4191
lean. It is also the founder's own picture doing the work, and the Fermi correlation was not aimed at.
Attack points: §2 item 2 is an argument, not a computation; the rule is imposed, not derived — this
patch *locates* the primitive, it does not explain it; §2 item 3 uses one spatial axis.
