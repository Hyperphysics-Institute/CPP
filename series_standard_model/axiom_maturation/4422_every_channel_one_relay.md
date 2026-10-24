# Every Channel, One Relay: a Sufficient Route to the Same PSR Ruler for the Binding Forces Is That Every Channel Rides the Same Light-Speed Relay With a Field Law Covariant at c. A One-Line Rescaling Proves That a Field of Any Range Relayed at c Takes the |Λr| Shape (Flattened by 1/γ) Around a Moving Source, While a Channel Relayed at Another Speed Flattens Differently; a 3D Grid Illustrates It. A3′ and AP-4 Already Put the Electric and Strong Channels on One Relay at c. What Remains: the Wave-Equation Form of Each Census, the Kinetic Part of Binding (Atom Sizes), and Lattice Discreteness

**Patch:** 4422. **Lane:** foundations, with GR and EM. **Session:** 242.
**Founder input:** "4421 applied. Please proceed." (on 4421's owed item: that the forces holding atoms, crystals and nuclei
together are measured with the same PSR ruler). No new physics input; Claude's working at his request.
**Script:** `series_standard_model/code/4422_every_channel_one_relay.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the rescaling, the γ prefactor
for a lab-frame source, the solver, the A3′ quote and AP-4's payload. It found that the first draft understated the grid errors,
claimed "whatever the static law" for an operator that gives only Coulomb or Yukawa laws, called a sufficient condition "the same
statement", wrongly identified the oblate PSR with the relay's light sphere, treated the γ prefactor as universal, and lacked
the D-9 entry. All six required changes are taken in.

## 1. The question

4421 showed that a moving structure does not twist if every force between its CPs depends on separation counted in the moving
CP's PSR, shortened by 1/γ along the motion: every pair potential then has the |Λr| shape, U(|Λr|) with Λ stretching the
along-motion separation by γ. The census gives the electric potential that shape (4411). Owed: the binding forces (atomic,
crystal, nuclear, quark) must have it too.

## 2. The condition: one relay at c, with the covariant wave form

**The statement.** Let a force channel's field be relayed at light speed c and obey a wave equation of the form
(∂²/∂t² − c²∇² + m²)φ = source, where m sets its range (m = 0: long range, like Coulomb; m > 0: short range, like a nuclear
Yukawa force). Around a source moving uniformly at v, the field is the static one with the along-motion coordinate stretched by
γ: φ_moving(x, y, z) = γ φ_static(γx, y, z), the |Λr| shape, **whatever the range m**. **Proof:** in the source's frame the
steady equation is −((c² − v²)∂²/∂x² + c²∇⊥²)φ + m²φ = δ(x)δ(y)δ(z); the rescaling x′ = γx turns it into the static equation
with source γδ(x′)δ(y)δ(z). More generally, any field law that is Lorentz-covariant with invariant speed c (including
higher-derivative and nonlinear laws, which is where a confining law would fall) gives the |Λr| shape; the (∂² − c²∇² + m²)
form covers only Coulomb- and Yukawa-type static laws.

**The prefactor is not universal.** The factor γ belongs to a source that is a lab-frame density (the time component of a
current, as for the electric potential). A Lorentz-scalar point source, weighted by proper time, gives no γ. The script
measures only the shape. That is why 4421's "common prefactor" stays open and depends on each channel's tensor character. A channel relayed at a
different speed c_s would flatten by √(1 − v²/c_s²) instead: a different ruler, and a structure bound by it would twist (4421
case B).

**An illustration (script).** The steady field of a moving source, solved on a 160³ periodic grid by FFT, with no assumption of
the answer. The script measures each equipotential's ratio, ahead against across, four units out (long range: m = 0.05; short
range: m = 0.8):

| channel | v | measured | 1/γ | √(1 − v²/c_s²) |
|---|---|---|---|---|
| long range, relayed at c | 0.3 | 0.9528 | 0.9539 | 0.9539 |
| long range, relayed at c | 0.6 | 0.7972 | 0.8000 | 0.8000 |
| short range, relayed at c | 0.3 | 0.9549 | 0.9539 | 0.9539 |
| short range, relayed at c | 0.6 | 0.8048 | 0.8000 | 0.8000 |
| short range, relayed at 0.7c | 0.3 | 0.9062 | 0.9539 | 0.9035 |
| short range, relayed at 0.7c | 0.6 | 0.5339 | 0.8000 | 0.5151 |

The grid errors reach about 4% at the strongest flattening, with a sign set by the source's width. For the long-range
channel (range about 20 in a box of 24), periodic images make the error grow with distance (about −6% at 8 units). The proof is
the rescaling above; the grid only illustrates it. Long and short range, relayed at c, give the same 1/γ, one shape for every
range. Relayed at another speed, the flattening follows that speed. (For linear channels the shape of one source's field is the
shape of the pair potential.)

**So, for linear channels, riding the same relay at c with a field law covariant at c is a sufficient condition for the |Λr|
shape of every force's field.** It is not the whole of "every force counted with the PSR ruler", which also needs the force law
(gradient and vector part), the common prefactor, and the moving receiver's response. Whether the moving CP's oblate PSR (4409,
4410) is itself produced by the relay is still 4421's owed item 3. (The light sphere from a moving emitter is centred on the
emission point in the absolute frame; the flattened surface is the equipotential, Heaviside's ellipsoid.)

## 3. What the registered rules already supply

- **One relay at c for every channel.** A3′ (registered) has each GP broadcast its packet to its PSR shell, "propagating at
  c = l_P/t_P in the absolute (Nexus) frame with flat per-hop transport, all channels obeying the same icosahedral shell-sum."
  A3′'s "all channels" are the packet's moments (Φ, V_i, Q_ij); the tie to E and S comes from AP-4, which puts the electric
  vector E and the strong vector S in **the same DI-bit**, and from the A3′/AP-4 reconciliation. So the electric and strong channels already
  travel together, at c, on one relay. Nothing in the rules gives the strong channel a different speed.
- **This covers the forces holding quarks in nucleons and nucleons in nuclei**, as far as they come from the S and E channels.
  It also covers the electric forces in atoms and crystals.

## 4. What remains

- **A covariant field law for each census.** 4411 assumed the electric census obeys GR-1j's wave equation (the 1/R weight per
  arrival). The strong census needs the same: that its static law, whatever it is (short-range, confining), is the steady
  solution of a propagation covariant at c, not an instantaneous rule (for example, "count within the PSR shell this
  Moment"), which would not flatten by 1/γ. Owed for each channel, the electric 1/R weight included (4411 item (a)).
- **The kinetic part of binding.** Atom sizes are set not by a static potential alone but by the electrons' motion (in standard
  physics, the balance of kinetic and potential energy, the Bohr radius a₀ = ħ²/(m_e e²) in Gaussian units); quantum bound states
  need the full covariant dynamics, not only the momentum law for point constituents. Corresponding states for moving parts needs the relativistic
  momentum law for every constituent (Bell; 4421 owed item 4). In CPP that is the coasting rule's speed dependence (4413's
  near-γ³ longitudinal response; SF-6's storage in the sea; Laue). Owed.
- **The common prefactor** (4421 owed item 2): the vector (magnetic) channel's factor, now for every channel. The force from a
  covariant channel carries it automatically in standard physics; in CPP it must come from each channel's vector part.
- **AP-5 saturation.** In dense interiors (nuclei) the saturation protocol may be active; it is a nonlinear receiver rule whose
  covariance is unexamined.
- **Lattice discreteness.** A relay on the 600-cell lattice is not exactly covariant: at the scale of a few PSRs the shell-sum is
  icosahedral, not round. The flattening is exact only in the continuum limit; any residual is a Planck-scale preferred-frame
  effect, bounded by the Lorentz-violation limits (TODO-4364-PREFFRAME).

## 5. What stays open

- **A covariant field law for every census** (electric 1/R weight, 4411 (a); strong census, new).
- **AP-5 saturation's covariance** in dense interiors.
- **The kinetic part of binding** (Bell; 4413's speed dependence; SF-6, Laue).
- **The common prefactor** via each channel's vector part (4421 item 2, 4411 open item).
- **Lattice discreteness** against the preferred-frame bounds (TODO-4364-PREFFRAME).
- **Closed in part:** 4421 item 1 (binding forces in PSR units), reduced, as a sufficient route, to "every census obeys a field
  law covariant at c on the one relay", with the relay half supplied by A3′ and AP-4. 4421 item 3 (the oblate PSR from the relay)
  stays open.
- **Carried:** 4421 items 2–6.

## 6. Question to the founder

None this patch. The registered rules answer the physical question (the strong channel rides the same DI-bits as the electric
one); what remains is derivation.

## 7. Report (Plain Language for him)

One sure way for the forces holding matter together to be counted with the same PSR ruler is for them to travel the same way: on
the same relay, at light speed, spreading by a rule that treats light speed the same in every direction. It can be proved in a
line and I illustrated it on a grid: a force of any range, long like electricity or short like the nuclear force, sent at light
speed from a moving particle is squeezed along the motion by exactly the Lorentz factor. Sent at
any other speed, it is squeezed by a different amount and would twist the body it holds together. CPP's registered rules already
send the electric and strong signals in the same DI-bit, at light speed, so the main condition is met. Three things remain.
- Each kind of signal must spread by a rule that is squeezed this way, not counted all at once.
- The motion of electrons, which sets the size of atoms, must follow relativity's momentum law.
- The lattice must be fine enough that its grain doesn't show.

## 8. PD-008

- **Convenient branch, marked:** "the binding forces are shown to use the PSR ruler." What is shown is a sufficient condition
  for the field's shape (one relay at c, a law covariant at c) and that the registered rules supply its relay half; the covariant
  law of each census, the prefactor, the receiver's response and the kinetic part are not derived.
- **Withdrawn:** the first draft's "the PSR ruler and the relay are one thing".
- Nothing registered.
