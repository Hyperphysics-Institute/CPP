# One Ruler, No Twist: the Founder's Principle (the Trouton–Noble Twist Is the Michelson–Morley Problem, Resolved by the PSR Contracting in the Direction of Motion) Works Out. If Every Force Between CPs Depends on Separation Counted in the Moving CP's PSR, Shortened by 1/γ Along the Motion, a Moving Capacitor Has No Preferred Orientation (No Twist), and With a Common Prefactor Its Equilibrium Is Exactly the Contracted Rest Shape (Proved, and Computed for a Model Capacitor). Binding Left in Absolute Units Twists. Owed: Binding Forces in PSR Units, the Vector Channel's Common Factor, and the Dynamics

**Patch:** 4421. **Lane:** foundations, with GR and EM. **Session:** 242.
**Founder input:** `founders_voice/4421_twist_is_michelson_morley_psr_contraction.md` (answers 4420).
**Script:** `series_standard_model/code/4421_one_ruler_no_twist.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the theorem, the chain rule, the
identification with 4411 and the Lorentz attribution. It found that the first draft credited the census with a common factor
4411 assigns to the still-owed vector channel, understated the theorem (no twist needs only the PSR argument; the common factor
fixes the exact shape), overclaimed "if and only if", measured Case B's twist on an unrelaxed shape, shifted his phrasing, and
cited only 4409 for the oblate PSR. All six required changes are taken in; the script now also relaxes each case.

## 1. His answer

- **"The plate-DPs are essentially an integrated system moving through space."** The forces acting on the plates and the DPs in
  the interplate space produce the same effects in that frame regardless of the plates' orientation.
- **It is the Michelson–Morley problem, with the same resolution:** "contracting space in the direction of motion through the
  absolute space", giving the Lorentz contraction and the relativity principle, "as we have derived before" (Claude's gloss:
  4408–4412).
- **The mechanism is the PSR contracting in the appropriate directions.** The geometry is too complex for him to give; he gives
  the principle.

## 2. The principle, worked out: one ruler for every force

**The statement.** Suppose every force between CPs, whatever its kind (electric between the plates, the binding that keeps each
plate rigid, the cohort's pull), depends on the separation **measured in the moving CP's PSR**, and the PSR is shortened by 1/γ
along the motion and unchanged across it (his oblate PSR, 4409; the 1/γ-along, unchanged-across result fixed in 4410 from 4409's
ratio and 4408's clock rate). Then a separation r in absolute units counts as |Λr| in PSR
units, with Λ stretching the along-motion component by γ, and every pair potential U(r) becomes U(|Λr|), times a common factor.

**That is the census shape.** 4411 found that the census channel gives the electric potential between co-moving CPs exactly the
|Λr| shape: R(1 − n·v) = |Λr|/γ, so the convection potential is γ/|Λr|. The full co-moving force is −(1 − v²) times its gradient,
a factor 1/γ times the gradient of 1/|Λr|, but 4411 assigns that overall (1 − v²) factor to the vector (magnetic) channel, which
is still owed. So his principle says every force takes the |Λr| shape the census gives the electric potential; the common
prefactor depends on the vector channel.

**The theorem, in two parts (Lorentz's corresponding states, 1895, with the PSR as the common ruler).**
- **(a) No twist needs only the ruler.** If every interaction depends on separations counted in PSR units, the total energy is a
  function of Λx alone, and in PSR-scaled coordinates it is unchanged by rotation, whatever the prefactors of the different
  forces. So the moving structure has no preferred orientation: no twist. This holds for many-body binding too (bond angles), as
  long as all geometry is counted in PSR units.
- **(b) The exact corresponding state needs a common prefactor.** Let s be any equilibrium at rest and place the moving structure
  at Λ⁻¹s, its rest shape contracted by 1/γ along the motion. If every force carries the same prefactor, the force on each CP is Λ
  times its rest force, times that factor, and its rest force is zero: every CP is in equilibrium, the total couple is zero, and
  the moving capacitor is exactly the contracted copy of the resting one, as the relativity principle requires. With mismatched
  prefactors there is still no twist, but the shape differs slightly from the contracted rest shape.

In the particle picture, the binding forces supply the couple opposite to the electric one between the plates (4420: (v²/2)
sin 2θ), because forces between co-moving particles act along Λ²r, off the line joining them. In Laue's continuum description the
balance is booked instead as the rate of change of the angular momentum carried by the moving stresses: two bookkeepings of the
same balance.

**Computed (script).** A model capacitor in two dimensions: two plates of five charges, springs within each plate, spacers and
braces across the gap (a rigid frame), every charge interacting electrically with every other. Its rest equilibrium is found;
it is then tilted, contracted, and moved at half light speed.
- **Every force in PSR units, common prefactor:** at the contracted rest shape the largest force on any charge is about 10⁻¹²
  (round-off) and the total couple about 10⁻¹³, at 0°, 30°, 45°, 60° and 90°. Relaxed from 30°, 45° and 60°, it stays at its
  starting tilt.
- **PSR units with mismatched prefactors:** relaxed, it also stays at its starting tilt (no twist), with a slightly different
  shape.
- **Electric potential in census shape, binding left in absolute units:** neither the contracted nor the uncontracted shape is
  an equilibrium (couple near −0.15 at 45°, ≈0 at 0° and 90°). Relaxed from 30°, 45° and 60°, **the capacitor turns** until its
  plates lie along the motion: a preferred orientation, the twist.

So the twist vanishes when every force is counted in PSR units; with binding left in absolute units it does not.

## 3. What remains for CPP to show

- **(a) Every binding force in PSR units** (settles no twist). The binding of a plate (atomic and crystal forces, the strong force
  inside nuclei) must depend on separation measured in the moving CP's PSR, as the electric potential does through the census.
  That is 4410's owed item (the DI-bit relay giving the convection form for every CP-to-CP force), with the precise target: the
  |Λr| shape.
- **(b) The common prefactor** (settles the exact corresponding state): the vector (magnetic) channel's (1 − v²) factor for the
  electric force (4411's open item), and the same factor for every other force.
- **The oblate PSR from the relay.** That the moving CP's PSR is shortened by exactly 1/γ along the motion and unchanged across
  it (4409's geometry, which fixes the ratio, with the clock rate fixing "unchanged across").
- **Dynamics.** Corresponding states covers equilibrium. Moving parts (orbits, swings, the cohort's partner switching) also need
  the relativistic momentum law for every constituent (Bell), and the cohort's coherence (SR-9).
- **The sea-mediated part** of the force (4412) and the cohort's transverse momentum (4420; Laue's dL/dt in the lab
  description) must fit the same pattern.
- **Laue's description**, for the record: in the lab frame one can also say the electric couple is matched by the rate of change
  of the angular momentum carried by the moving stresses. The corresponding-states statement above is the equivalent one in terms
  of forces on each part.

## 4. What stays open

- **Binding forces in PSR units** (4410 owed; the |Λr| target; settles no twist).
- **The common prefactor** via the vector channel (4411 open item; settles the exact corresponding state).
- **The oblate PSR** derived from the relay (4409).
- **Dynamics** (Bell; cohort coherence, SR-9).
- **The sea-mediated force part** (4412) and the cohort's transverse momentum (4420).
- **Closed:** 4420 question (answered in principle: one ruler, the contracted PSR, for every force); 4420 item 4 (no twist)
  reduced to "binding forces in PSR units" (no twist) and "the common prefactor" (exact shape).
- **Carried:** 4420 items 2, 3, 5, 6, 7.

## 5. Question to the founder

None this patch. His principle has been worked out to a theorem and a model; what remains is derivation (the relay giving every
force in PSR units), not a physical-picture question.

## 6. Answer to his "What do you think?"

He is right, and the geometry can be done. If every force between CPs is counted in the moving CP's own PSR, and that PSR is
shorter along the motion by the Lorentz factor and unchanged across it, then every force takes the same form, the form CPP's
census already gives the electric force between moving charges. With that, a moving capacitor has no preferred orientation, so nothing
tries to turn it; and if every force also carries the same overall strength factor, its resting shape squeezed along the motion
balances exactly, every part feeling zero force, whatever the tilt. It is Lorentz's theorem of
corresponding states with the PSR as the ruler, and I checked it on a model capacitor at half light speed: balanced to round-off
at every tilt, and left free it stays at whatever tilt it starts. If instead the forces holding the plates rigid were counted in
absolute distances, the same capacitor, left free, turns to line its plates up with the motion.

So what CPP has to show is the piece he points to: that the forces holding matter together, inside atoms, crystals and nuclei,
are counted in the moving CP's PSR, the same as the electric force.

## 7. PD-008

- **Convenient branch, marked:** "his principle is shown." The theorem and the model show no twist follows **if** every force is
  counted in PSR units with the oblate PSR, and the exact contracted shape if they also share a prefactor; that the relay does this
  for binding forces, the vector channel's factor, and the oblate PSR itself are not derived.
- **Not overclaimed:** the model is two-dimensional and static; dynamics is owed.
- Nothing registered.
