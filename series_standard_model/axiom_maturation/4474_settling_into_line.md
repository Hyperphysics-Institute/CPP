# Settling Into Line: the Founder Answers How One DP Arc Pushes Another — by Discharging, an Arc Changes Its Separation and So Its Distance and Angle to the Surrounding CPs and DP Arcs, Which Displaces and Rotates Them; the Cloud Re-Equilibrates to the New Forces After Each Discharge, With Part of Each Newly Rotated Arc Along the Discharge Direction. Re-Equilibration Gives "the Same Duration" Under Three Conditions: Whichever Way the Arcs Settle (a Swing That Rings, or a Creep That Sets the Interval Between Discharges), the Time Must Not Depend on the Size of the Discharge; the Restoring Action Must Be Isochronous (Linear Is Sufficient, Not Necessary); and the Stiffness Must Not Change as Arcs Discharge, to About Four Parts in 10⁸ per e-Fold. A Toy Cloud Shows the Third Is Hard: Its Internal Modes Shift by About a Sixth When Two-Thirds of It Is Removed; Only the Whole Cloud Moving Together in a Linear Hold Stays Fixed, and for Neutral Arcs That Motion Radiates Nothing — What Radiates Is Each Arc's Stretch and Turn. The Registered Hold (the CP's Polarising Pull) Is What His Trigger Disturbs. Met, the Conditions Make the Realignment a Ringing Mode (4472's "Ring On"; Marked Convenient)

**Patch:** 4474. **Lane:** foundations, with QM and EM. **Session:** 242.
**Founder input:** `founders_voice/4474_arc_pushes_by_changed_separation.md` (answers 4473 §6).
**Script:** `series_standard_model/code/4474_reequilibration_clock.py`.
**Critic:** fresh context, ACCEPT WITH CHANGES; all eleven required changes taken in (review file, Patch 4474).

## 1. His message

- **How one arc pushes another:** "one arc pushed on another to realign it by being in a more discharged state, so it will be in a different position, which will
  inherently/unavoidably change the distance and angle of the surrounding DP-arcs and thus exert a force on them to displace and thus rotate so that there will
  be a portion of the angle of discharge that will be inline/oriented with the discharge angle."
- **The bottom line:** "every DP-arc that discharges changes its DP-arc separation, which changes its relative angle and distance to all surrounding CPs/DP-arcs,
  causing the system to re-equilibrate to the new forces after each discharge, causing the newly rotated DP-arcs to be in line with a portion of their
  projection in the discharge angle directions."

## 2. What it answers

The second half of 4473 §6 is answered in kind: the push is indirect. A discharging arc changes its own separation, so its position and its distance and angle
to every neighbour change; the neighbours feel new forces, are displaced and rotated, and the cloud "re-equilibrate[s] to the new forces". So the push depends on
both distance and angle, as he says, though the law (how strongly, at what distance and angle) is not given; that is the arc–arc force still owed (4473 c).

The first half (why the realignment would take the same time as the cloud empties) is not answered directly. His word "re-equilibrate" gives a route, which
§3–§4 follow to the end. (Claude's reading.)

## 3. Settling into a new equilibrium: when its time is fixed (script, part 1)

After each discharge every neighbour has a new resting place, and it has to get there. It can do so in two ways:
- **Creep in** (heavily damped, like a door on a closer): it never passes its new resting place, so the arc itself does not ring (script: no sign change). A
  wave can still come once per realignment if, as in 4473, each realignment brings a new portion into line and that portion discharges: a creep-then-discharge
  cycle is a relaxation oscillator (like a dripping tap; 4472's "wait at each stage"). Its period is then set by how long the creep takes to bring the next
  portion to the point of discharge, which depends on the drag, the stiffness and the size of the step, and must itself stay fixed to the same tolerance.
- **Swing past and back** (lightly damped, like a plucked string): it rings about its new resting place. That gives waves.

If it swings, its timing depends on how the force pulling it back grows with distance from the resting place:
- **Linear** (twice as far, twice the pull): the swing time is the same whatever the size of the shift. In the script the period is 2π to seven figures for
  shifts from 0.01 to 1. So the size of each discharge does not matter, which is what "the same duration" needs.
- **Non-linear** (here an extra pull growing as the cube, small for small shifts and half the linear pull at a shift of 1): the time depends on the shift:
  from 6.2831 at 0.01 to 5.37 at 1. For four parts in 10⁸, the displacements must be tiny compared with the distance over which the force law bends.

(Linearity is sufficient, not necessary: the cycloidal pendulum and the potential ax² + b/x² are exactly isochronous though non-linear, and an arc precessing
about a steady field turns at a rate that does not depend on its tilt; Claude's working-out, not claimed as new.)

Whether the cloud can settle as one body depends on the speed of the push: across an atom (about 10⁻¹⁰ m) at light speed takes about 3 × 10⁻¹⁹ s, under a thousandth of a
Lyman-α period (4 × 10⁻¹⁶ s); at the CP's own speed, about c/137, it is 0.1–0.3 period (4472 §3). At light speed the cloud acts as one body; at the CP's own speed the far side lags the
near side by a tenth to a third of a cycle, which the in-step condition (4471 g, 4472 g) must then absorb.

So his re-equilibration gives "the same duration" if three things hold: **(i) whichever way the arcs settle (a swing that rings, or a creep that sets the interval between discharges), the time it takes must not depend on the size
of the discharge; (ii) the restoring action must be isochronous over the displacements: a linear force is the simplest case (twice as far, twice the pull); a
few non-linear forms, and steady precession about a field, also keep a fixed time; (iii) the stiffness and inertia that set the swing do not change as arcs discharge, to about 4 × 10⁻⁸ per e-fold for Lyman-α (4473 §3).** And
(4473 a) the swing time must equal h ÷ ΔE.

## 4. The hard condition: a cloud that empties changes its own stiffness (script, parts 2–3)

In his picture the forces come from the arcs themselves, and every discharge changes the separations that make them. A toy cloud (30 like charges with mutual
repulsion, held by an outside pull toward the centre, in 2D; not CPP dynamics) shows what happens when two-thirds of it is removed, about one e-fold if the energy goes with the number of arcs:
- **Internal modes** (parts of the cloud moving against each other): the median frequency falls by about 16%, the highest from 2.76 to 2.32. Far from fixed.
- **The whole cloud moving together**, with a linear outside hold: its frequency stays exactly 1 (change 3 × 10⁻¹¹, numerical precision), whatever is
  removed. This is a known result: for identical particles the mutual forces cancel in the sum, so only the outside hold moves the cloud as a whole (the trapped-ion
  "centre-of-mass mode"; Dobson's harmonic potential theorem, Phys. Rev. Lett. 73, 2244, 1994; first form, Kohn, Phys. Rev. 123, 1242, 1961). With a slightly non-linear hold it is no longer an exact mode, and its frequency shifts by
  about 1%.
- **A cloud of arcs**, each a + and a − (part 3): each arc is neutral, so moving it whole changes nothing that radiates; the radiating sum is the total of the
  arcs' own dipoles (charge × separation), changed only by an arc stretching or turning, his "changed separation" and "rotate". The sum is moved by the mutual
  forces, since a pair force contributes (q_i − q_j) F_ij / m (equal inertia assumed; in CPP a CP has no rest mass and its inertia comes from its DP-arcs,
  R-CP-NO-REST-MASS, so this is toy dynamics). Inside one arc that term is the arc's own pull between its + and −, which the other arcs need not change;
  between arcs it is their mutual push, which changes as they discharge. So the theorem does not carry over, and the clock is fixed only if each arc's own
  stretch or turn sets it and the arc–arc coupling shifts it by less than about 4 × 10⁻⁸ per e-fold.

So a fixed clock in an emptying cloud is possible when the radiating motion is driven by a linear hold that the discharging arcs do not make. In his picture the
forces come from "all surrounding CPs/DP-arcs" (4474) and "the forces acting between DPs change after each discharge" (4473); so far as they come from the arcs,
they drift (Claude's reading); so far as they come from the CPs, they may be the hold. What holds the cloud is therefore the
deciding question (§5).

The registry already names one hold the discharging arcs do not make: the unpaired CP's polarising pull, which orients the DPs around it and sets the cloud's
radius (R-DPSEA-UNIFORM). It acts on orientation, so it bears on the turning of arcs, not on moving the whole cloud. But in 4473 the trigger is that the central
CP is knocked out of resonance and "is no longer organizing" the cloud, so on his own sequence this hold is disturbed during the discharge. Whether the CP's
pull still sets the turning while the cloud discharges is therefore the sharp form of the question. A turning in the CP's pull is a pendulum-like swing,
isochronous only for small angles (or a precession), and its rate depends on the strength of the pull where each arc sits, so arcs at different distances
would turn at different rates unless something locks them in step. (Claude's working-out.)

A hold fixed independently of the arcs gives one rate per hold, set by its stiffness, not by ΔE; it shares the failure of 4461 §4 (one cloud, one rate, not a
family of lines), so (4473 a)'s "equal to h ÷ ΔE" is not met by a fixed hold alone.

Met, conditions (i)–(iii) make the realignment a ringing mode of the cloud, losing a share each cycle: 4472's "quick trigger, then each section rings on"
and Claude's harmonic candidate (4461 §4). That convergence is onto Claude's own earlier option and is marked convenient (§8).

## 5. Question to the founder (physical picture)

**When the neighbouring arcs come into their new line after a discharge, how do they get there: do they swing past and back, ease straight in, or keep
turning steadily, like a top? And once the rogue wave has knocked the central CP out of resonance, does the CP's pull still turn the arcs while the cloud
discharges, or are they then turned only by one another, or by something else?**

## 6. What stays open

- **(a) The re-equilibration clock:** whether the arcs swing, creep or turn; whether the restoring action is isochronous over the displacements (linear or
  otherwise); what keeps the stiffness and inertia setting the time fixed as arcs discharge, to about 4 × 10⁻⁸ per e-fold for Lyman-α, and equal to h ÷ ΔE; in
  an arc cloud (+ and −) the mutual forces move the radiating sum (§4) (= 4473 a).
- **(b) The hold:** what holds and orients the arc cloud around the CP, whether it is linear in displacement, and whether it is made by the discharging arcs or
  by something they do not change; a fixed hold alone gives one rate, not set by ΔE (the Thomson failure of 4461 §4) (§4).
- **(c) The arc–arc force law:** how the push depends on distance and angle (his qualitative answer, §2), derived from the CP-level rules (= 4473 c).
- **(g) The other clocks:** the creep-then-discharge (relaxation) clock and the steady turning or precession of arcs, each with what would keep its time fixed as
  the cloud empties (§3, §4).
- **(h) The radiating coordinates of an arc cloud:** each arc's separation and orientation (not the whole cloud's motion), how much of their restoring comes from
  the arc itself, from the CP's polarising pull (R-DPSEA-UNIFORM) and from the other arcs, and whether the CP's pull acts after the 4473 trigger (§4).
- **(d) Carried from 4473, word for word:**
  - 4473(a) **The realignment clock:** what makes the realignment time independent of the energy left, to about 4 × 10⁻⁸ per e-fold for Lyman-α, and equal to h ÷ ΔE (= 4472 a; 4470 a, b).
    The arcs' contributions in phase across the cloud, in step and without gaps (4471 g, 4472 g).
  - 4473(b) **The size of each increment:** a share of what is left (as the measured fading requires), not a fixed amount.
  - 4473(c) **The rule set for a simulation, derived from the registered CP-level rules (A3′/AP-4, R-CP-NO-REST-MASS, R-DPSEA-UNIFORM):** the force between DP arcs (separation, orientation), how arcs turn and move, the discharge rule, the radiation rule (4465
    a), the cloud's starting state; then a many-body or FEM-type simulation of the discharge.
  - 4473(d) **Carried from 4472, word for word:**
    - 4472(a) **What keeps time in the staged decay:** crawl, waiting at each stage, cycling, or a quick trigger with each section ringing on (Claude's list); what sets
      the rhythm at ΔE/h, in step and without gaps (= 4471 a, g; 4470 a).
    - 4472(b) **Why a front would be so slow:** about 0.06–0.2 m/s for a single sweep lasting the lifetime, or about 1.5–4.6 × 10⁶ m/s for one round per period, both far
      below the relay speed.
    - 4472(c) **The CPP analogue of a near-threshold oscillator** (Brusselator-like, below or above threshold), with energy kept track of; how near threshold (B within
      about 8 × 10⁻⁸ for 3.9 million cycles, in the Brusselator).
    - 4472(d) **The unit of action:** his 4320 ruling (ħ/2 as one GP over one Moment), restated at 4325 (the whole Planck ZBW half-swing), and the 4457 one-GP floor on
      energy per Moment, against h per period of an atomic photon; and the tension between a share per period (h ÷ N) and an ħ per increment (= OPEN-QM-3, 4470 b).
    - 4472(e) **What a "transformation cell" is in his picture.**
    - 4472(f) **What collides with the electron CP, and why the trigger's timing is random** (isolated atoms in vacuum decay at the measured lifetime).
    - 4472(g) **Local-depletion emissions as one excitation:** separate local emissions in step and without gaps, or several lines or quanta (= 4471 g, h).
    - 4472(h) **The share readings:** a share at the rate f, a share at f ÷ N, or a unit of action (§5).
    - 4472(i) **The LaViolette description to verify:** subquantum kinetics and its reaction–diffusion system ("Model G", extending the Brusselator; LaViolette, Int. J.
      General Systems, 1985; *Subquantum Kinetics*, 1994), whose main use is spatial (stationary structures forming particles), closer to his "defect formed" than to
      a clock.
    - 4472(j) **Carried from 4471, word for word:**
      - 4471(a) **The sequence of wavelets:** at once, in sequence or otherwise (founder question); in sequence, what sets the spacing and keeps them in step (= 4467 §4,
        4470 a).
      - 4471(b) **The common rule λ = h ÷ p from the DP-arc cohort** for photons and particles (his task; = 4464 d, 4470 b, 4443 c, PROP-6).
      - 4471(c) **Carried from 4470, word for word:**
        - 4470(a) **The emitting cohort's eigenmode in CPP terms:** its dynamical variable, its equation, its eigenfrequency (= ΔE/h), its ringing time, its grating
          coupling and its line shape (Copilot's list; = 4461 a, 4464 a).
        - 4470(b) **Energy and frequency linked by h** in CPP: why the eigenmode's energy and its rate stand in the ratio h (Copilot's E = hν vs Fourier ν; 4456).
        - 4470(c) **Transverse multiplicity vs longitudinal cycles:** his central CP plus polarized DP cloud adds width, not cycles; what in CPP adds cycles along the
          travel.
        - 4470(d) **Carried from 4469:**
          - 4469(a) its 4468 list, by label: 4468(a) CPP's rule linking a photon's length to its spread of colours (standard: about 0.9 ÷ crests for a flat train,
            within about 2 for other shapes), and whether a photon can have a definite energy while short; 4468(b) the 4467 list — 4467(a) the 4466 list: 4466(a) a
            photon's length in CPP terms, including what "length" is in his volume picture (bears on 4464 b, e); 4465(a) CPP's radiation rule (= 4464 i), with the
            quantum dipole emission-rate analogue and the CP-in-atom case; 4464(a) what swings at ΔE/h (= 4463 a, 4461 a, 4460 a, 4457 b, 4446 c); 4464(b) one cycle
            or many; 4464(c) envelope shape against the measured rise-then-fade; 4464(d) the pilot-wave resemblance (h/p; 4443, 4444); 4464(e) path-difference
            coherence; 4464(f) 4463 b, c, d, f, j; 4462 a, b; 4444 b, c; 4461 c, d, e, i, j, k, l; 4460 b, c, e, g; 4459 c, e, f, i; 4457 d–g; 4456; 4464(g) founder
            question 4464 §5; 4464(j) velocity or acceleration; 4464(k) the envelope reading's slow-transit speed (0.2 m/s); 4464(l) the orientation of his metre;
            4464(m) the Eschner both-sides result, with 4461 l; 4467(b) founder question 4466 §6; 4467(c) founder question 4467 §4 (does each crest come from one
            back-and-forth of the CP, can a single jump lay down many crests and what spaces them a wavelength apart, or does something other than the CP's motion lay
            them down), sharpening 4464 §5's first question and 4464 (b); 4467(d) a measured Lyman-α emission profile (lamp or beam), to replace the computed Doppler
            bound; 4468(c) founder question 4468 §4 (when one photon of a single, definite energy but only one or a few crests long reaches a grating, does it go to
            one sharp angle or spread over a range, and what in the photon decides which); 4468(d) its dispositions (right that a line is many photons and a gas's
            width mostly a spread of their energies, from motion; not right that a spread of jump energies makes up the natural width, nor that this replaces long
            photons; 4467(e) dispositions stand, including the 4466 erratum added in 4467); 4468(e) the independence assumption (whether in CPP independent atoms'
            photons have random relative phases; used by the grating and fringe arguments);
          - 4469(b) founder question 4469 §6 (is a short photon of definite energy more like the few-crest pulse at a grating, or like the steady beam, or something
            else, and what in its structure makes the difference), open;
          - 4469(c) dispositions stand, with 4469 §3 re-read in Copilot's order.
        - 4470(e) **Founder question 4470 §5.**
        - 4470(f) **Dispositions:** his new aspect (central CP plus polarized DP cloud, and in the attachment the spin DP) recorded, as transverse multiplicity. His
          "many waves each carrying part of the energy" not adopted; one extended excitation absorbed as one quantum (§2). His drop-time-as-colour postulate assessed
          (§3): the trend conceded; the drop time does not set the colour under three readings. His eigenmode half kept, with the drop as the envelope and the eigenmode
          assigned to the emitting cohort (§4, Claude's reading). 4469 §6 left open; the split answers it only on the reading where the photon is long. 4468 §4 still
          open.
        - 4470(g) **The third reading's evidence:** measured natural widths of the Balmer-α components against the computed ones (3 × 10⁷ and 1 × 10⁸ Hz), with 4467(d).
        - 4470(h) **CPP's account of the decay-rate trend with frequency** (rate ∝ frequency³ × dipole² in standard physics), under 4465(a).
        - 4470(i) **Which cohort carries the eigenmode:** the emitting cohort (Claude's split) or the photon's own DP-arc cohorts (Copilot's model B).
      - 4471(d) **Founder question 4471 §5.**
      - 4471(e) **Dispositions:** his solid datum agreed, with the momentum-not-energy qualifier; his identical-wavelet proposal assessed (§3): it gives a common centre
        colour (given the rate–ΔE link), and a single fine line only in sequence, in step and without gaps. 4470 §5 answered in part (the colour tied to the energy
        difference; the drop's speed not returned to as the colour). His "single large potential difference" read as one energy gap; whether crossed at once is not
        said. 4470(f) dispositions stand.
      - 4471(f) **Momentum, not total energy, sets matter's wavelength:** which part of the DP-arc cohort sets h ÷ p (= 4443 c, PROP-6, 4464 d).
      - 4471(g) **The no-gap condition:** in his sequence picture, what makes the wavelets follow on without gaps, or else the light splits into several lines.
      - 4471(h) **One excitation:** whether a gapless in-step sequence of wavelets is one excitation absorbed whole (consistency with 4470 §2 and (f)).
    - 4472(k) **Founder question 4472 §6.**
    - 4472(l) **Dispositions:** the momentum qualifier agreed by both (4471 f recorded as agreed; its CPP derivation still owed; implicit earlier in PRED-Q-1 / PROP-6).
      4471 §5 answered in part, tentatively: one after another, as a propagated cascade of sections of the orbital; whether in step and without gaps is not yet
      said. His staged decay judged plausible in outline, with the timing requirement. The Brusselator accepted as an analogy for one part (a rate held while the
      swing dies away), not evidence. His pieces are shares adding up to hf (his own wording); what "E = hf" attaches to in each is open. His ħ recollection
      identified as his 4320 ruling, restated at 4325. 4471(e) dispositions stand.
  - 4473(e) **Founder question 4473 §6.**
  - 4473(f) **Dispositions:** 4472 §6 answered: each section, once set off, discharges the portion aligned with the photon's direction; the rest realign under the
    changed forces and discharge in turn; the rhythm is the realignment time (closest to 4472's "wait at each stage", self-timed). His request for a simulation
    answered: possible in principle, owed, arc-level rules first (derived by Claude). "The same energy" per increment, read as equal size, not adopted (§4); read
    as the same colour, open under 4472(h). 4472 §5's hf ÷ N refined as the average share. 4472(l) dispositions stand.
- **(e) Founder question 4474 §5.**
- **(f) Dispositions:** 4473 §6 answered in part: the push is indirect, through the discharging arc's changed separation, distance and angle to the
  surrounding CPs and DP arcs, and the cloud re-equilibrates (recorded); why the time stays the same not answered directly; his re-equilibration gives it under
  three conditions (§3), linearity being sufficient, not necessary. 4473(f) dispositions stand.

## 7. Answer to his "What do you think?"

That's a clear answer to how one arc pushes another: by discharging, an arc changes its own separation, so its distance and angle to every neighbour change, the
neighbours are pushed and turned, and the cloud settles into a new balance. I'll take that as the picture for working out the force between arcs.

"Settles into a new balance" is also the key to the timing, and I followed it through. Settling can give repeated waves two ways: the arcs can
swing past their new position and back, like a plucked string, and ring; or they can ease straight in, like a door on a closer, and each easing-in brings the
next portion into line to discharge, like a dripping tap. Either way, the time it takes has to be the same every time. If they swing, and the pull back grows in
step with how far they are out, the swing time is the same whatever the size of each discharge, which is what "the same duration" needs (a few other kinds of
pull, and steady turning like a top, keep a fixed time too). The catch is the stiffness: in
your picture much of the force comes from the arcs themselves, so as they discharge the stiffness changes, and so would the swing time. In a toy cloud, removing two-thirds of it moves
its internal swings by about a sixth. The one motion that stays exactly fixed is the whole cloud swinging together in a hold that doesn't depend on the parts
leaving, and for a cloud of + and − arcs even that breaks. For arcs, which are + and − together, what gives off light is their stretching and turning, not the cloud
moving as a whole; and the one outside pull the record already has, the CP orienting the arcs around it, is the thing your rogue wave knocks out. So whether
the CP still turns the arcs while they discharge is the sharp question.

If those conditions are met, the realignment becomes the cloud ringing like a bell and giving up a share each ring, which is close to one of my own earlier
options, so I've marked that as the convenient reading.

## 8. PD-008

- **Agreed:** the push is indirect, through the discharging arc's changed separation; the cloud re-equilibrates (his).
- **Not softened:** re-equilibration gives a fixed time under (i)–(iii); in an arc cloud the arcs' own forces move the radiating sum, so the clock drifts as
  they go unless a hold they do not make sets it.
- **Marked:**
  - the swing/creep split and conditions (i)–(iii) are Claude's working-out of his "re-equilibrate";
  - the toy cloud (like charges, outside linear hold, 2D) is Claude's, not CPP dynamics; the 16% is illustrative, the theorem exact;
  - the convergence onto a ringing mode (4472 "ring on", 4461 §4) is onto Claude's own earlier option, and convenient;
  - "the hold decides" is Claude's conclusion, and convenient: a fixed linear hold is Claude's own 4461 §4 candidate, with its Thomson failure (one rate, not
    set by ΔE); the question (§5) is asked so that his picture can overturn it;
  - the creep branch (a relaxation clock, 4472 "wait at each stage") and the turning/precession branch are not worked to the end here; owed (§6 g).
- **Not claimed:** novelty for isochronism, the centre-of-mass theorem or normal-mode analysis.
- Nothing registered.
