# With A and B Fixed on the Grid, One Number (the PSR) Sets Both Clock and Light Slowing, but the Data Need a Factor 2 Between Them; Picture (b) Needs A and B to Move Closer by Half the PSR's Fraction

**Patch:** 4390. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4390_choice_b_absolute_clock_ab_fixed_on_grid.md` (answers 4389 §5).
**Script:** `series_standard_model/code/4390_one_number_cannot_do_two_jobs.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). All seven required changes are
taken in.

## 1. His answer

- **Choice (b):** light crosses one PSR every Moment. (a) is not his conception.
- **The absolute clock** (from the Nexus) never slows. "Clocks slowing" is a relative-frame statement: oscillations
  take more absolute Moments "to go the same distance".
- **His thesis:** the distance between crystal CPs A and B is set by the inverse-square fall-off of a CP's DI-bit
  concentration in absolute distance, and it does not change in the Sun's field. The PSR's contraction only sets how
  many PSRs it takes to go from A to B. The DI-bit shell thickness is a later question.
- **His question:** can it be made to work that way, with A and B fixed on the grid?

## 2. Agreed first

The absolute clock never slows. That is the corpus's position (the Moment is universal), and every "slowing" in
4384–4389 was relative. His clock mechanism, more Moments to cover the same distance, is CPP's registered clock
mechanism (the clock-rate ruling).

## 3. As stated, it cannot be made to work (script part 1)

With A and B fixed and light at one PSR per Moment, **one number**, the PSR ratio p, sets both:
- the clock slowing: crossings of A–B per Moment go as p;
- light's speed on the grid, which also goes as p.

The data need light to slow **twice** as much as clocks (4389):

| tune p to | clock slowing at the Sun's surface | bending at the limb | GPS gravitational offset |
|---|---|---|---|
| the clocks (p = 1 − U) | 2.12 × 10⁻⁶ ✓ | **0.876″** (measured 1.751″) ✗ | 45.7 μs/day ✓ |
| the bending (p = 1 − 2U) | **4.24 × 10⁻⁶** ✗ | 1.751″ ✓ | **91.4 μs/day** ✗: GPS would drift about 14 km a day |

Gravity Probe A confirmed the clock effect to about 7 × 10⁻⁵ of its size, and GPS corrects for it every day. The solar
redshift itself agrees to a few percent. No single p does both jobs.

- **Redshift measurements cannot escape this.** In a static field, a photon's frequency counted in Moments is
  conserved. So the received ratio reads the emitter's rate in Moments directly.
- **The one escape is a clock that is not a light-speed crossing:** CPs moving at a speed that goes as √p (4388
  row 5). It is excluded by the registered clock ruling (4389). It is also excluded by data, because a light clock (a
  cavity between a fixed A and B) still runs as p whatever the atoms do. Comparisons of a cavity with an atomic clock
  over the annual swing in the Sun's potential (about 3.3 × 10⁻¹⁰) would see the mismatch (published bounds owed).

**This is also what (b) said.** 4389's (b) was "one PSR per Moment **with crystals shrinking half as much as the
PSR**". With p = 1 − 2U, a clock runs at 1 − U only if A and B move closer on the grid by U, half the PSR's fraction
(script part 2). His (b) and his thesis that A and B stay fixed cannot both hold. The fixed-A,B version is 4388's
row 1 (light bends half), which the data exclude.

## 4. His inverse-square idea can give (b), but only under one particular sensing rule (script part 3; Claude's suggestion, not on file)

He says the distance is set by "how much the DI-bit concentration from a CP has gone down". CP_A's concentration falls
as 1/d² in absolute distance. Suppose CP_B settles where what it senses reaches a fixed level. Then where it settles
depends on **what it counts**:

| CP_B senses CP_A's DI-bits … | spacing d | clock | result |
|---|---|---|---|
| per grid point | fixed | = light's rate | half the bending ✗ (his current thesis) |
| per Planck-sphere length | ∝ √p (shrinks half as much as the PSR) | 1 − U | **(b) works** |
| per Planck-sphere cross-section | ∝ p | no slowing | ✗ |
| per Planck-sphere volume | ∝ p^1.5 | clocks **speed up** | ✗ |

The family "p^n per 1/d²" gives d ∝ p^(n/2), so any exponent is available. **The length rule is the one chosen to hit
the target: it is a fit, not a prediction.** (d ∝ √p ≈ 1 − U is exactly GR's isotropic spatial factor.) The most natural
reading of "measured over its own Planck sphere", the volume, fails. The founder's 4385 statement that a CP responds
"only to the sum of DI-bits on the GP on which it is positioned" points to the per-grid-point case, which also fails.
So something in the balance rule must change, and only one particular rule gives (b).

## 5. Question to the founder (physical picture)

When CP_B settles at its distance from CP_A, what decides where it stops?
- the number of CP_A's DI-bits arriving at the single grid point it sits on; or
- something measured over its own Planck sphere, which is smaller near the Sun?

The first keeps A and B fixed, and light then bends only half the measured amount. The second lets the crystal shrink,
but only one way of measuring works: if what counts is spread over the Planck sphere's whole volume, clocks would speed
up instead. Everything fits only if the crystal shrinks by half the Planck sphere's fraction.

## 6. PD-008

- **Convenient answer refused:** "yes, it can work as you said." It cannot. One number cannot set both the clock and
  the light slowing when the data need a factor 2 between them.
- **Convenient branch, marked:** the √p rescue (§4). It keeps his inverse-square language alive, but the length rule was
  chosen to fit, and the volume reading fails. None of the rows is derived.
- Nothing registered. His statements (choice (b); the absolute clock never slows; A and B fixed) are recorded. The last
  is flagged as conflicting with the data unless the balance rule changes.
