# The Founder's Shape Alone May Be the Whole Answer: a Round Planck Sphere Shifted Away From the Sun by the Speed of a Body Falling From Far Away Gives Einstein's Gravity Exactly, With Light Always Crossing One Planck Sphere per Moment

**Patch:** 4397. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4397_psr_smallest_toward_sun_independent_concept.md` (answers 4396 §5).
**Script:** `series_standard_model/code/4397_fore_aft_and_side_parts_of_the_psr.py`.
**Critic:** a fresh-context critic returned HOLD on the first draft (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). The first draft said the
toward-versus-away part of his sphere is invisible and only a flattening bends light. That holds only for a tiny shift.
The critic showed that a pure shift of the right size already reproduces Einstein exactly. All four required changes
are taken in, and the script now checks the exact case.

## 1. His answer, and a correction to the record

- **Attribution, corrected:** the direction-dependent PSR was his **independent gedanken experiment** to produce
  gravity, not chosen to match Einstein. 4396's "calibrated to Einstein" applies only to the **numbers** Claude used
  (PSR_r = 1 − 2u, PSR_t = √(1 − 2u)), as he says, not to the concept. An annotation is added to 4396.
- **His shape:** around each GP, the PSR is smallest toward the Sun and grows with the angle to a maximum 180° away. He
  does not know the numbers.

## 2. Toward-versus-away and line-versus-across (script part 1)

Write the PSR around a GP, with θ the angle from the direction toward the Sun and c = cos θ, as

    PSR(θ) = P₀ [1 − a c − b c²]

Light crosses one PSR per Moment, so the time per unit grid length is 1/PSR:

    1/PSR = 1 + a c + (b + a²) c² + (terms of order a³, ab)

- **The term linear in a** (toward versus away) adds −∫a dr to a travel time: an end-point term. It does not bend light
  and cancels in any round trip.
- **Its square does not cancel.** a² multiplies c², which is the same in both directions along a line, so it bends light
  exactly as b does. **The measurable quantity is b_eff = b + a², and the data need b_eff = U.**
- If a is of order √U, then a² is of order U and matters at first order. The first draft treated a as small and missed
  this.

## 3. The decisive case: a round sphere, simply shifted (script parts 2–3)

Take a Planck sphere of unit radius, not flattened at all, with its centre moved off the GP by β, away from the Sun.
Light still crosses exactly one Planck sphere per Moment; it is the GP that sits off-centre inside it. The reach from
the GP is then:

| direction | reach per Moment |
|---|---|
| toward the Sun | 1 − β |
| away from the Sun | 1 + β |
| across | √(1 − β²) |
| any angle θ | −β cos θ + √(1 − β² sin² θ) |

That is his shape exactly: smallest toward the Sun, growing steadily with the angle to a maximum directly away.

Now let **β² = 2u**: β is the speed, in units of light speed, of a body that has fallen from very far away to this
point. Then:

- **round-trip light speed along the line to the Sun** is the harmonic mean of 1 − β and 1 + β, which is 1 − β² = **1 − 2u**;
- **light speed across** is **√(1 − 2u)**;
- **a clock held at rest** runs at √(1 − β²) = **√(1 − 2u)**: the Lorentz factor of the fall speed;
- **a ruler held at rest** is Lorentz-contracted along the line to the Sun by the same factor, and unchanged across;
- **the floor** (across reach = ½, R-DIBIT-COUNT-AT-FLOOR's value) falls at u = ⅜, r = 8m/3, where β = √3/2. The
  point where β reaches light speed (r = 2m) lies inside the floor.

These are exactly the Schwarzschild values, **to all orders, not only weak field.** In GR this is a known form of the
black-hole geometry: Painlevé–Gullstrand coordinates, the "river model" (Hamilton & Lisle, Am. J. Phys. 76, 519
(2008)), in which space flows at the fall speed on a flat background and light moves at c relative to the flow. Here
the flat background is the fixed GP grid, consistent with a flat-harmonic census, and "light moves at c relative to the
flow" is "light crosses one Planck sphere per Moment". The script confirms the shifted-sphere reach equals the river's
light speed at every angle tested.

**So his shape alone, with no flattening, may be the whole answer.** It also matches his own language from 4394: the
clock slowing is the Lorentz factor, and the rulers are Lorentz-contracted along the line to the Sun. And it fits his
4385 statement that gravitational and kinetic SSV_abs are equivalent: the shift is set by the speed a falling body
would have.

## 4. What is calibrated, and what differs from 4396

- **β² = 2u is calibrated.** It is physically natural (the fall speed from infinity), but it is chosen to match, not
  derived from PCD. The PCD derivation, possibly from his gravitational-kinetic SSV equivalence, is owed.
- **4396's flattened, centred sphere and this shifted, round sphere agree on every round-trip and light-synchronised
  measurement.** In GR they are the same geometry in two coordinate systems. In CPP, Moments are universal and the GP
  grid is physical, so the two are different claims about the slicing. They differ in **one-way** light times between
  two points with clocks set by the Moment: with the shift, A→B and B→A differ by 2∫a dr. Whether CPP can ever detect
  that difference is open (owed).
- **The sign.** His sphere, shortest toward the mass, corresponds to space flowing **outward**. The usual black-hole
  river flows **inward**, with the sphere shortest **away** from the mass, which is why light inside cannot get out. The
  two are identical for every measurement outside r = 2m. They differ only at a horizon, inside the floor.
- **Matter's motion is not yet modelled.** A shifted Planck sphere might be what drives falling, which was the purpose of
  his gedanken experiment. That is owed, not shown.

## 5. The first draft's corpus tie is withdrawn

The first draft suggested the toward-versus-away part is A3′'s V channel and the line-versus-across part is the Q
channel. That conflicts with A3′ as written:
- A3′ says V "sources spatial curvature … g_ij statics";
- C4 sources Q from T^TF, which is zero for static matter, so A3′'s Q is zero for the static Sun;
- C3 sources h̄₀ᵢ from T₀ᵢ, which is zero for a static mass (the static harmonic condition allows a radial h̄₀ᵢ only as
  C/r² outside the matter);
- 3608's Q, the second moment of the DI-bit addresses, is not obviously the same object as C4's Q.

**The suggestion is dropped.** How a shifted Planck sphere maps onto A3′'s channels is filed as owed.

## 6. What stays open

- **The PCD reason for the shift** and its size β² = 2u (calibrated now).
- **Moving and rotating masses:** frame dragging (Gravity Probe B, LAGEOS) is a real test of the shift's direction and
  size (owed).
- **The census:** 4396's first owed item (is the grid census flat-harmonic with non-round PSR shells?) now also covers
  off-centre shells.
- **The sign** (outward versus inward flow) at a horizon.
- **4396's owed items carry.**

## 7. Answer to his "What do you think?"

His shape works, and may be all that is needed. A Planck sphere that keeps its round shape but sits shifted away from
the Sun is shortest toward the Sun and longest away, as he pictured. Light crosses exactly one of them per Moment, never
slower. If the shift equals the speed a body would have after falling from far away, the bending of starlight, the
radar delay, the clock slowing and the black-hole floor all come out as Einstein's, exactly.

## 8. Question to the founder (physical picture)

Picture the Planck sphere around a GP near the Sun as a round ball that has slid a little away from the Sun, so the GP
sits off-centre, nearer the sunward side. **Is that your picture: the same round sphere, just shifted, by an amount equal
to the speed a body falling from far away would have at that point?** And for a black hole, which light cannot escape:
is the sphere still shortest toward it, or does it flip, becoming shortest away from it?

## 9. PD-008

- **Convenient branch, re-marked:** the first draft's "only the flattening matters; the shift is invisible". It kept the
  patch's earlier reasoning but was wrong. The likelier result is the one above: his pure shift already works.
- **Not to be overclaimed:** β² = 2u is a calibration, and a shifted and a flattened sphere cannot be told apart by
  round-trip measurements.
- Nothing registered. 4396 annotated for the attribution correction.
