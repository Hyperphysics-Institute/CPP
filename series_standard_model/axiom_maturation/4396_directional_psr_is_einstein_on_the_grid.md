# Yes, It Is in the Prior Work (P-ORIGINAL-DIRECTIONAL-PSR, Patches 3606–3609). With Light Always Exactly One PSR per Moment and the PSR Different by Direction, the Solar-System Tests Fit With No Slower-Than-PSR Light; Calibrated to Einstein, the Exact Form on the Fixed Grid Is PSR_r = 1 − 2u, PSR_t = √(1 − 2u)

**Patch:** 4396. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4396_light_is_psr_leading_edge_directional_psr.md` (answers 4395 §5).
**Script:** `series_standard_model/code/4396_directional_psr_is_schwarzschild_on_the_grid.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the kinematics,
including oblique rays, and corrected three overstated framings. All six required changes are taken in.

## 1. His answer

Light **is** the leading edge of the Planck sphere, so it can never travel slower than one PSR per Moment; that was
settled at the start of the theory. His original concept for gravity was a **different PSR radius in every direction**
from every GP. He does not know its granularity. He asks whether this is in the prior work.

**So 4395 §5 is answered: no.** Light is not squeezed below one PSR per Moment. 4395's reading (i) and 4387 (B) /
4389 (a) are set aside for good, as he said in 4390. I apologise for the wording of the last several patches, which
described light as slower than one PSR per Moment. That was the wrong frame for CPP.

## 2. Yes, it is in the prior work

- **P-ORIGINAL-DIRECTIONAL-PSR** (founder statement, 3 Sep 2026, Patch 3607,
  `founders_voice/founder_statement_original_directional_psr_2026-09-03.md`): "the original conception of the PSR had
  θ,φ (azimuth/elevation) dependence; the isotropic single-radius PSR was introduced in the AI rewrite."
- **3606:** the rank-2 register would be an anisotropic PSR, "the perception sphere as an ellipsoid".
- **3607:** restoring it is a restoration, not a rewrite. A spherical PSR cannot make gravitational waves (rank).
  Statics cannot tell an isotropic PSR from a radially anisotropic one: same geometry, two coordinatizations.
- **3608 (P-DIRECTION-VIA-ADDRESSES):** the directional PSR derived from the DI-bit addresses through their second
  moment Q_ij: PSR_ij = l_P[(1 − kΔ|SSV|)δ_ij − k₂Q_ij]. For a static mass, "areal coordinates need
  (kΔ, k₂Δ) = (u/3, u); isotropic coordinates need (u, 0)".
- **3609, R-RANK-2-REAFFIRMED:** the rank-2 channel was already in A3′ (Q_ij), founder-ratified.

**What happened since:** the GR lane went on using the isotropic PSR, the "one-PSR" metric of 4362–4395, which is
3608's k₂ = 0 case. The "light slower than one PSR" phrasing in 4387–4395 came from identifying the PSR with the clock
factor through a single isotropic function. A directional PSR removes the need for it.

**A mismatch to reconcile (owed):** 3608's (kΔ, k₂Δ) = (u/3, u), with Q ∝ (n̂n̂ − δ/3), gives a radial factor of 1 − u
and an unchanged tangential factor. Those are **ruler** factors (3608 speaks of "spatial geometry"). This patch's PSR is
the **light step**, ruler × clock factor: 1 − 2u radially and √(1 − 2u) sideways. Either the PSR concept shifted between
the two patches, or one of them is mislabelled. They agree once 3608's numbers are read as rulers.

## 3. The directional PSR fits the Sun with light always one PSR per Moment (script parts 1–3)

Let the fixed GP grid be the coordinate system, let u = m/r be the census on it (flat-harmonic), and let light advance
**exactly one PSR per Moment in whatever direction it moves**. Allow the PSR to differ radially (PSR_r) and sideways
(PSR_t):

| | weak field | exact |
|---|---|---|
| PSR along the radius (toward the mass) (U and u are the same quantity, m/r) | 1 − 2U | **1 − 2u** |
| PSR sideways | 1 − U | **√(1 − 2u)** |
| clocks (any orientation of light-crossing) | 1 − U | √(1 − 2u) |
| crystals, radially | shrink by U | √(1 − 2u) |
| crystals, sideways | **unchanged** | unchanged |
| light, measured locally | c in every direction | c |

- **Light bending and Shapiro delay come out at GR's values** (1.751″ at the Sun's limb; the null geodesic in this
  metric gives 4m/b). The extra radial shrinkage of the PSR is the "space half". It needs no light slower than one PSR,
  only a PSR that is shorter along the line to the mass than across it.
- **Oblique rays:** the PSR ellipsoid (radii PSR_r and PSR_t) coincides with the null cone at every angle (script part 5),
  so "one PSR per Moment in its direction" is consistent for any ray, not just radial and sideways ones.
- **Clocks come out isotropic, but only by assumption:** a radial and a sideways light-crossing clock both run at
  √(1 − 2u) because the crystal is **taken** to shrink radially by just that much. That is the metric-universality
  premise (his 4385 "same physics in every frame"), owed since 4394. Hughes–Drever tests are safe if matter couples to
  the same geometry.
- **His 4395 squeeze becomes exact:** the PSR along V (radial) equals the sideways PSR squeezed once more by the same
  factor, PSR_r = PSR_t × PSR_t.
- **A consequence for him to confirm:** CP spacings **across** the line to the mass stay fixed on the grid, as in his
  4390 "A and B fixed". Only spacings **along** it shrink.

**The exact form is Einstein's black hole written on the fixed grid.** g_tt = −(1 − 2u), g_rr = 1/(1 − 2u), and grid
circles have their full circumference: Schwarzschild in areal coordinates, with u = m/r on the grid. In PSR terms, the
radial PSR is **linear in the census**, 1 − 2u, and the sideways PSR is its square root.

- **The floor** (PSR_t = ½) falls at u = ⅜, r = 8m/3: the same surface as 3390 and 4385. PSR_r = ¼ there.
- **The light ring** (3m) lies outside the floor, so the non-spinning ringdown is Einstein's. The horizon (u = ½) lies
  inside the floor.

## 4. What it changes, and what it costs

- **What caused the 4372–4385 black-hole tension.** It was not isotropy as such: 4380–4381 reached exact Einstein in
  the isotropic picture at κ = 1, and 3607 notes that statics cannot tell the two coordinatizations apart. The tension
  came from the **one-PSR (κ = 0) rule**: a single function setting both clocks and rulers, g_tt·g_rr = −1. **That
  single-function rule cannot be Schwarzschild in isotropic coordinates, but it is exactly Schwarzschild in areal ones.**
  Applied along the radius (a directional PSR) instead of isotropically, the one-function idea becomes Einstein. That is
  the finding.
- **It is still a calibration.** PSR_r = 1 − 2u is chosen to reproduce Schwarzschild, just as κ = 1 was (4381's critique
  applies). The isotropic one-PSR law was e^(−2ε); this one is linear in the grid census. Which law the PCD cycle gives is
  owed.
- **R-PSR-LAW-LOG would be amended, not merely restated.** The ratified law gives the PSR as a function of the census on
  the grid, with second-order coefficient +½ (ε²/2). If the grid census is u (areal), the clock factor √(1 − 2u) has
  coefficient −½: the opposite sign. The physics is the same only through a change of radius. Because the GP grid is
  fixed, this would amend a founder ruling (as 4381 said of κ = 1). It goes to him before anything is registered.
- **Owed:**
  1. **Is the grid census really flat-harmonic when the PSR shells are ellipsoids?** The relay sums over each GP's PSR
     shell. With PSR_r ≠ PSR_t the shell is not a sphere, and GR-1j's flat-Laplace result was derived for spheres.
     This is the first thing to check (TODO).
  2. **Why radial = 1 − 2u exactly**, linear in the census, from the PCD cycle and the directional census (3608's
     Q_ij or the V channel).
  3. **Strong-field consistency:** the corpus floor/cap conventions (AP-5, R-DIBIT-COUNT-AT-FLOOR) were stated for an
     isotropic PSR.
  4. **The suspended conventions (WC-DP-SEA-PV, WC-EINSTEIN-AREAL)** become unnecessary if this holds. They should be
     re-graded once item 1 is done.
  5. **The C5-text vs c07/GR-1i attribution of V** (4394) and the GR-1b gradient question (4395) are both reframed:
     the direction-dependent part of the PSR is the space half.
  6. **The PSR's granularity** (his question): how finely the PSR varies with direction (continuous, or in the
     600-cell's directions?). Unaddressed.

## 5. Question to the founder (physical picture)

Near the Sun, is the Planck sphere **shorter along the line toward the Sun than across it**? Specifically: does it
shrink about twice as much toward the Sun as sideways, so that light, always crossing one Planck sphere per Moment,
covers less ground when heading toward the Sun than when passing across? And do the CPs of a crystal keep their grid
spacing **across** that line, shrinking only **along** it?

## 6. PD-008

- **Convenient branch, marked:** "this solves gravity and black holes." It reproduces Einstein exactly **if** the census
  on an ellipsoidal-PSR grid is still flat-harmonic (owed item 1). PSR_r = 1 − 2u is calibrated to Einstein, not derived,
  and it would amend R-PSR-LAW-LOG's sign. It is presented as a restoration of his original concept with a precise target.
- Nothing registered yet. Registering "light advances exactly one PSR per Moment" (his foundational statement) and the
  directional PSR waits for his §5 answer and owed item 1.
