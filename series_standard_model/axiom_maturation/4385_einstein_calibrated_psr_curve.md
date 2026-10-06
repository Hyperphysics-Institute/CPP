# Rulers Are Fixed in PSR Units, So CPP Lives in Its One-PSR Class; Calibrated to Einstein as the Founder Asks, the Curve Matching Einstein's Redshift Versus Areal Radius Is q = e^(−asinh ε): His Photon Sphere, Shadow and Pitch Exactly, Damping About 13% Lower, Floor at 8m/3. It Needs the PSR to Resist Shrinking Gradually as Its Shell Fills: the Opposite of the Founder's Tentative Sign, and in Tension With R-PSR-PACE-AT-N

**Patch:** 4385. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4385_rulers_in_psr_units_use_einstein_as_calibration_dps_act_in_vacuum.md`
(answers 4384 §7).
**Script:** `series_standard_model/code/4385_einstein_calibrated_psr_curve.py`. Its steady-curve line reproduces 4374
(ℓ = 2: −4.05% / −4.57%).
**Critic:** a fresh-context critic re-derived the maths and returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). All nine required changes are
taken in.

## 1. His answers

1. **Rulers.** The positions of the CPs in an atom, a crystal or "the subatomic particle cage" are set by the forces
   between them. Those forces fall off as the inverse square of distance, with the PSR as the unit. So near a black hole
   the equilibrium spacing is the same number of PSRs, and the same number of Moments pass for the same number of
   PSR-size hops: "the same physics in every frame", whether SSV_abs rose by gravitational stress or by kinetic energy.
2. **Which way.** Unclear to him. He asks for the effect that complies with Einstein, using Einstein's prediction as a
   calibration "to get a clue, and see if we can rationalize that effect", since the empirics near black holes are
   consistent with Einstein. He is not yet prepared to make a prediction instead.
3. **Vacuum or matter.** DPs outside a black hole respond to their SSV_abs as matter does. There is no fundamental
   difference between mass and energetic entities; all are arrangements of CPs, each responding only to the DI-bits on
   its own GP. A black hole's interior has no DPs, only CPs at PSR spacing. A thicker shell delivers DI-bits to GPs
   between GP_origin and GP_PSR that would otherwise have received the information only on a later re-radiation, so
   more DI-bits land on early re-radiations. That **probably shrinks the PSR**. He is not sure, and the effect may be
   insignificant.

## 2. Registered: R-RULER-IN-PSR-UNITS (founder 4385)

> **R-RULER-IN-PSR-UNITS (founder 4385).** The spacing of the CPs in an atom, a crystal or the subatomic particle cage is
> set by the forces among them. Those forces act over distances counted in PSRs, so near a black hole, where the PSR is
> smaller, the equilibrium spacing is the same number of PSRs. The same number of Moments pass for the same number of
> PSR-size hops, giving the same physics in every frame, whether SSV_abs is raised by gravitational stress or by kinetic
> energy.

**Consequences (with founder 4362, the clock rate and relay reach share the PSR, and 4384, light advances one PSR per
Moment):**
- **Clocks, rulers and light share one PSR, so X = N√A = 1.** CPP's exterior is in the one-PSR class (κ = 0). This
  closes 4384's condition, 4381 §3's universality worry, and 4381's Mercury question (the ratified ½ is the PSR's).
- **The absolute metric** g₀₀ = −q², g_ij = q⁻²δ, and with it γ = 1, additionally needs 3386's proper-length reading,
  which is unratified (4384, owed item iv). Read literally, "the same number of Moments for the same number of PSR hops"
  fixes ratios, not the clock-to-Moment rate.
- **WC-GR-EXTERIOR is excluded within CPP:** it needed clocks and light to slow relative to rulers. It is kept only as a
  labelled convention for comparing with GR (as 4384 §4 said), and is replaced for CPP work by §3's convention.
- **4372's and 4365 L41's reading** ("one PSR for clocks and rulers") is now backed by the founder's own statement.

## 3. The Einstein calibration within the one-PSR class (script parts 1–3)

No one-PSR metric is Schwarzschild: Einstein's exterior has X = 1 − ϱ² in isotropic form. So "matching Einstein" means
choosing what to match.

**Matching his clock rate as a function of areal radius** is the natural choice. The circumference fixes the photon
sphere and the shadow, and redshift versus area is what observations of the light ring probe. This choice fixes the
curve uniquely:

    q² = 1 − 2m/R,  R = r/q   ⇒   q = √(1 + ε²) − ε = e^(−asinh ε).

Matching his isotropic lapse instead would give GR-1c's Padé (1 − ε/2)/(1 + ε/2), which has a different photon sphere
and a horizon at ε = 2.

| | Einstein | this curve | steady curve e^{−ε} |
|---|---|---|---|
| redshift vs areal radius | 1 − 2m/R | **identical** | different |
| photon sphere (areal) | 3m | **3m** | 3.297m |
| shadow | 3√3 m | **3√3 m** | +4.63% |
| eikonal pitch | — | **0%** | −4.42% |
| eikonal damping | — | **−13.4%** (exactly √3/2; robust) | −4.42% |
| ℓ = 2 scalar-proxy WKB, frequency / damping | — | −0.48% / −13.3% (fit-window spread < 0.01; accuracy not established) | −4.05% / −4.57% |
| floor q = ½ | — | ε = ¾, **areal 8m/3** | ε = ln 2, areal 2.885m |
| horizon | at 2m | **none above the floor** | none above the floor |

- **Against GW250114:** frequency ±2.4%, damping rate γ₂₂₀ −14.5%/+17.6% (conv042 L8 quotes the same box in τ as
  (−15, +17)%). The curve is **consistent with the box, not fitted to it**, and only 1.2 points inside the damping edge.
  The hedges:
  - the comparison is non-spinning, and the remnant has χ_f = 0.68;
  - the ℓ = 2 result uses a scalar potential as a stand-in;
  - the ℓ = 2 peak sits 1.33 tortoise units outside the floor, inside the region where 4384 found WKB unreliable;
  - M_f was inferred with GR inspiral dynamics, and this curve departs from GR at 2PN.

  Only the eikonal √3/2 is robust.
- **What differs from Einstein is the radial ruler:** g_RR / g_RR(Einstein) = (R − m)²/(R(R − 2m)) = 1 + m²/R² + ….
  This sets the damping, and it is the curve's **earliest weak-field departure (2PN, spatial metric)**: a possible
  falsifier.
- **The floor lands at areal 8m/3**, the radius of 3390's held surface and of conv042's wall studies. That is automatic,
  since q = ½ where 1 − 2m/R = ¼.
- **Weak field:** q = 1 − ε + ε²/2 + 0·ε³ − ε⁴/8. Mercury's ½ is kept (R-PSR-LAW-LOG). The third-order coefficient is
  0; the ruling left it open, so nothing is amended (e^{−ε} has −1/6, GR-1c's Padé −¼).
- **Price (4365's formula, not re-derived here):** the background residual becomes 1 − ε₀²/2. That is unobservable for
  G. For α it matters only if α's reading carries the lapse's sensitivity (TODO-4364-EPSABS), where it would be about
  twice 4381's κ = 1 estimate.

**Recorded as a working convention, not a ruling:**

> **WC-EINSTEIN-AREAL (working convention, founder-directed calibration, Session 242).** Strong-field work uses the
> one-PSR exterior with q = e^(−asinh ε): the unique curve in CPP's class that reproduces Einstein's redshift as a
> function of areal radius, and with it his photon sphere, shadow and eikonal pitch. It is a calibration to GR at the
> founder's direction (4385), not a derivation. It also relies on 3386's proper-length reading. It replaces
> WC-GR-EXTERIOR for CPP work. Its departures from Einstein (damping about 13% lower, eikonal; floor at 8m/3; 2PN
> spatial metric) are CPP's predictions under this calibration.

## 4. What the calibration asks of the back-reaction (script part 4)

The PSR's rate of shrinking per unit stress must be S = d(−ln q)/dε = 1/√(1 + ε²). In terms of Claude's fill mapping
f = 1/(8q³) (unratified; 4384 owed item iii), with u = 2f^{1/3} = 1/q, that is **S = 2u/(1 + u²)**:

| place | ε | fill | S | PSR shrinks … per unit stress |
|---|---|---|---|---|
| ordinary space | 0 | 0.125 | 1 | as the compounding law |
| neutron-star surface (roughly) | 0.2 | 0.227 | 0.981 | 1.9% slower |
| photon sphere | 0.577 | 0.650 | 0.866 | 13.4% slower |
| floor (the N point) | 0.75 | 1.000 | 0.800 | 20% slower |

**So the calibration needs the PSR to resist shrinking as its shell fills, and it never needs it to shrink faster.**

**Two conflicts with registered items, stated plainly:**
- **The founder's tentative mechanism.** More DI-bits arriving early, between GP_origin and GP_PSR, means larger
  SSV_abs and a smaller PSR. That is the opposite sign. If it holds and is not small, CPP's own prediction moves away
  from Einstein (4384 §5: a faster shrink lowers the pitch).
- **R-PSR-PACE-AT-N** (founder 4369) places the PSR's change of pace at the N point, the floor. This curve changes pace
  gradually from ε = 0 onward: about 2% already at a neutron-star surface. That conflicts with a registered ruling; it
  is not a matter of wording. It goes to the founder (§6 Q2).
- **A second conflict with a ratified item:** the floor is at ε = ¾ here, while AP-5's ratified cap and 4371 quote ⅔
  (Einstein's isotropic value) at the same areal radius. The variables in which AP-5 states its cap need checking
  before this can be called a conflict or a relabelling (owed).

**One way the resisting sign could arise (Claude's suggestion, not on file):** redundancy. A thicker shell delivers to a
GP early the same source's information that the GP would have received anyway on a later re-radiation. If each GP
registers a source's information only once, the early copy adds nothing in total. As the fill approaches 1, more
arrivals are redundant, so the effective census grows more slowly than the stress (S < 1). This fits the corpus's
saturation idea (AP-5's saturation protocol; 4370 Q1). It **reframes** his picture: his was about extra early arrivals,
not repeated copies. And it gives at most the direction of the effect, not yet its size 2u/(1 + u²).

## 5. Still open (all in todolist.md, D-9)

- A full mode calculation with the floor's boundary condition at 8m/3 and this g_RR; conv042's wall programme and
  3390's instability check redone with this exterior.
- The spinning ringdown in the one-PSR class with this curve.
- ε = ¾ versus AP-5's ⅔.
- R-PSR-PACE-AT-N (§6 Q2).
- TODO-4364-EPSABS (α background).
- 3386's proper-length reading, now load-bearing for g₀₀ and γ.
- A PCD-level derivation of S(f).
- The 2PN spatial-metric departure as a weak-field test.
- 4384's carried items: the fill mapping versus "small chance"; μ₀ε₀ from DPs; the single-charge-clock check.

## 6. Questions to the founder (physical pictures)

He asked to be told what Einstein needs, so the needed direction is stated.

1. **Early copies.** A thicker shell delivers a DI-bit to a GP a few Moments early: information from the same source
   that the GP would otherwise have received on a later re-radiation. Does the GP then count that source **twice** (the
   early copy now and the later one when it arrives), or **once**, so that the later copy adds nothing? Counting twice
   makes the Planck sphere shrink faster and moves black holes away from Einstein's pitch. Counting once lets it resist
   shrinking, which is the direction Einstein needs (not yet the amount). If neither picture fits, please describe what
   the GP does.
2. **When the pace changes.** Your ruling puts the change in the Planck sphere's pace of shrinking at the point where its
   sphere holds N grid points (the floor). Einstein's calibration needs the pace to ease off **gradually**, starting
   well before the floor: about 2% slower at a neutron star's surface, 13% at the photon sphere, 20% at the floor. Can the
   change begin gradually as the shell fills, or does it happen only at the floor?

## 7. PD-008

- **Convenient branch, marked:** "the calibration fits GW250114, so CPP agrees with black holes." It agrees because it is
  calibrated to Einstein's redshift-versus-area. The damping (about −13%) is a genuine consequence of CPP's class, but it
  sits 1.2 points from the box edge, with spin, the floor condition and the GR-inferred mass not done.
- **Required, not derived:** the resisting sign. It runs against the founder's tentative mechanism and conflicts with
  R-PSR-PACE-AT-N as worded.
- **Earliest falsifier:** the 2PN spatial metric.
- **Founder-directed:** the calibration. **Registered:** his ruler statement, in his terms. **Excluded within CPP:**
  WC-GR-EXTERIOR, kept for comparison only.
