# How the Substrate Can Meet the Coasting Conditions: Read the Founder's Round-Trip Asymmetry as a Timing Ratio, Not a Force. (Back Time − Front Time)/(Back Time + Front Time) Is Exactly v/c at Every Speed, Distance and Coupling; a CP Stepping by It Coasts at Any Speed, the Same for Every Particle, and the Exact Rule Even Makes Fast CPs Harder to Push (Close to γ³). It Needs the Sea to Echo the CP's Past Position Back, and It Would Restate a Registered Clause

**Patch:** 4413. **Lane:** foundations, with GR and EM. **Session:** 242. **Claude's working at the founder's request**
("4412 applied. Please work out how the substrate meets these conditions"); no new founder physics input.
**Script:** `series_standard_model/code/4413_coasting_by_timing_ratio.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It confirmed the central identity and
ran the exact rule, which showed what the first draft's toy hid (a speed-dependent inertia); it also found an overstated
information claim, an unnamed conflict with a registered clause, a wrong flowing-sea consequence, and a leading founder
question. All nine required changes are taken in.

## 1. The conditions (from 4412)

1. **Self-consistent coasting at every speed:** with no velocity carried by the CP, whatever moves it each Moment must give
   exactly a displacement of v per Moment at velocity v, with neutral stability and the light-speed limit respected.
2. **The same for every particle**, free or bound, to preferred-frame precision.
3. **No self-drive** of a moving bound state, and forces between co-moving CPs equal and opposite (the census channel).

## 2. The proposal: the round-trip asymmetry as a timing ratio

The founder's 2 August 2026 ruling identified a round-trip asymmetry in a moving CP's returns from the DPs of the sea,
"possibly … the source of the full storage of inertial volume". CONJ-FP-1 read it as a **force**, a net forward SSV_net,
and found it vanishes under Liénard–Wiechert propagation (Condition B), which relativity of bound matter requires
(4411–4412).

Read it instead as **timing**. For a CP moving at v, with reflecting DPs at rest in the absolute frame at distance r (at
emission) ahead and behind, the returns come back after t_f = 2r/(c + v) and t_b = 2r/(c − v), and

    (t_b − t_f) / (t_b + t_f) = v / c       exactly

(script part 1: to twelve decimals for v from 0.001 to 0.999 and r from 1 to 10⁶). The ratio has no units, so a common
clock rate (absolute or dilated) cancels. **Coasting rule:** each Moment a CP steps by the velocity its own returns
encode, plus whatever forces add.

## 3. What it delivers

- **Condition 1:** at any velocity the readout is exactly that velocity, and always below 1, so no CP reaches light speed.
  The exact rule (script part 5: each Moment the step is the ratio from the returns arriving then, r = 10, with the true
  unequal fore and aft windows) coasts and is neutrally stable at v = 0.2 and 0.9, and a kick leaves a lasting velocity
  change: Newton's first law, with inertia. **The kick response falls with speed**: relative to rest, 0.93 at v = 0.2, 0.61
  at 0.5, 0.23 at 0.8, 0.11 at 0.9, close to but not equal to 1/γ³ (0.94, 0.65, 0.22, 0.08), which is special relativity's
  longitudinal inertia. So the coasting rule itself makes fast CPs harder to push along their motion. (The first draft's
  moving-average toy, v_n = the mean of the last W velocities, is its low-speed limit: at rest the exact response equals
  2Δx/(W + 1) with W = 2r.) How this depends on r was not converged in this patch (a short check at r = 5 and 20 did not
  settle at v = 0.9).
- **Condition 2:** the ratio depends only on timing, not on the CP's charge or mass, the sign or strength of the sea's
  response, the reflectors' distance, or the local SSV_abs, **provided the reflecting DPs are at rest in the absolute
  frame.** If a CP's nearest reflectors are its own polarized cloud and that polarization moves with it, the readout is
  biased toward zero by a species-dependent amount (a gap, owed).
- **Condition 3:** coasting is not a force, so it adds nothing between CPs; forces between co-moving CPs come from the census
  channel and are equal and opposite (4411–4412). (Script part 4 illustrates the forces only.) A positronium atom moving
  through the sea: each CP reads its own returns from DPs at rest and coasts at its own velocity; nothing pushes the pair.
- **No receiver-rule split:** the DPs return what reaches them; the asymmetry is in the timing created by the CP's motion
  relative to them. 4412's gap does not arise.
- **CONJ-FP-1:** Condition B, and the automaton moving-source test, still stand as tests of the **force** reading, which
  this proposal sets aside; under Liénard–Wiechert the field of a moving source still encodes its velocity, so the
  information exists. CONJ-FP-1's marginality condition (C·PSR = SSV_abs) becomes unnecessary under the timing reading,
  since the step is v by construction.

## 4. Conditions and costs

- **What the CP needs to know.** AP-4's DI-bit payload carries an origin address, not an emission time; a return
  re-imprinted by a DP carries that DP's address and Moment. With reflectors at every distance, the CP cannot pair fore and
  aft returns from equal r unless a return also carries the Moment and place it was first sent from, or the CP remembers
  its emissions. And once a return carries (x_e, t_e), the CP has its velocity directly, (x_now − x_e)/(t_now − t_e); the
  fore/aft ratio is one readout among equivalent ones. **What the mechanism really needs is that the sea echoes the CP's
  past position back to it.** That fits the 7 July ruling that velocity is held in the sea, but only if the memory is in
  flight in the sea, not stored in the CP's GP; otherwise it is carried velocity under another name.
- **A registered clause would change.** R-CP-NO-REST-MASS reads "Each Moment a CP advances by its SSV_net (V_i)", with
  inertia as the DP-arcs' reaction (SF-6), and the founder's 4404 input says "the arcs and separation maintain the constant
  velocity". The rule "step = readout + forces" replaces "advances by SSV_net" unless the readout can be written as part of
  V_i. Adopting it needs a restatement of the clause, which is the founder's call and already owed (todolist 4404).
- **No fixed reflection delay:** a constant delay per reflection biases the readout low (script part 2: −4.5×10⁻³ at r = 100,
  falling as 1/r). That is not just an error: it would slow every CP relative to the sea, a first-order preferred-frame
  effect (TODO-4364-PREFFRAME, 4412 (iv)). His 30 July disavowal of a medium response lag supports immediate reflection;
  his 2 August "one-increment delay" means the fore/aft difference, not a fixed per-reflection delay.
- **Resolution:** returns arrive in whole Moments, so the readout's resolution is about 1/(4r) per Moment, which bears on
  sub-GP steps.
- **Inertia and mass:** if the window W is set by the reflectors' distance and that is the cloud's size, inertia would
  grow with size while the ZBW radius shrinks as mass grows: the wrong way. If instead W is set by the PSR (DI-bits do not
  reach beyond it, per the R-DIBIT rulings), coasting inertia would be the same for every CP and would depend on location
  (smaller where the PSR shrinks near a mass). The relation to mass (GR-1a, SF-6) is owed.
- **Relativistic form:** the light-speed limit is automatic, and §3 shows the exact rule already gives a speed-dependent
  longitudinal inertia close to γ³. That must be reconciled with the relativistic storage in the sea (SF-6, Laue; CONJ-FP-1
  debt (d)) without double counting.
- **A flowing sea:** if the reflectors move at u, the ratio reads exactly (v − u)/(1 − uv/c²), the relativistic relative
  velocity (script part 6). A CP at rest in the flow reads zero and, stepping by the readout in absolute coordinates, is
  **not** carried. It is carried only with an added rule: the step is taken in the reflecting DPs' frame. With that rule,
  a CP at rest in an inward-flowing sea falls with it (the river picture, 4397, 4403 §6), and the founder's outward sign
  (4402, 4409) would carry it outward, which ties back to the open 2M question.

## 5. What stays open

- **The echo:** whether a return carries the Moment and place it was sent from, or the CP remembers (and that the memory is
  in the sea, not the GP).
- **The R-CP-NO-REST-MASS restatement** (step = readout + forces versus "advances by SSV_net"), for a founder ruling.
- **Self-cloud reflectors** biasing the readout (species dependence).
- **No fixed reflection delay** (a preferred-frame requirement).
- **The speed-dependent inertia** (close to γ³; r-convergence; reconciliation with SF-6 storage).
- **Inertia scaling** (window from the cloud, or from the PSR).
- **The flowing-sea rule** (step in the reflectors' frame) and its sign consequence (4402).
- **Readout resolution** (whole Moments; sub-GP steps).
- **CONJ.md (line 477)** to carry this proposal when the 4411 (f) update is made.
- **Carried:** 4412 items (iii), (iv), (v); 4412 items (i) and (ii) addressed by this proposal, pending his answer.

## 6. Answer to his request

The conditions can be met. Read his round-trip asymmetry as a speedometer rather than a push: comparing how much sooner the
returns come back from ahead than from behind gives a CP's speed exactly, for any particle at any speed. A CP that steps by
that keeps coasting at its speed, never reaches light speed, and does it the same way whatever kind of particle it is.
Because coasting is not then a force, particles moving together still push each other equally, and a moving bound pair
cannot drive itself. The exact rule even makes a fast particle harder to push along its motion, by close to the amount
relativity predicts.

What it needs: the sea must echo a particle's past position back to it (so the returns carry when and where they were
sent, or the particle remembers), reflections must add no fixed delay, and the registered rule that a CP advances by its
SSV_net would have to be restated, which is his decision.

## 7. Question to the founder (physical pictures)

A CP moving through the sea gets its DI-bits back from the DPs ahead a little sooner than from those behind. Which picture
is yours?
- **(a) The imbalance pushes it forward** (the force reading; it disappears if signals behave the textbook way, which
  relativity of bound matter requires).
- **(b) The returns tell it its speed**, and it steps by exactly that each Moment (the timing reading worked out here).
- **(c) The DP-arcs and DP separation store its velocity** and carry it each Moment, as you said in 4404.

And one physical detail: **does a returning DI-bit carry the Moment and place the CP sent it from, or must the CP remember
where it was?**

## 8. PD-008

- **Convenient branch, marked:** "the conditions are met." They are met by the proposed reading in a model; the echo
  mechanism, the clause restatement, the inertia scaling and the reconciliation with the sea's storage are not derived.
- **Not overclaimed:** this reinterprets his 2 August ruling and would amend a registered clause; it is offered to him,
  with the alternatives, not registered.
- Nothing registered.
