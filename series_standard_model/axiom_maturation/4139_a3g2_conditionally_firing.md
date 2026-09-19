# A3G-2's Magnitude Test — the Amendment Meets the Preferred Frame

**Patch:** 4139. **Lane:** EW. **Session:** 234.
**Discharges:** TODO-4138-A3G2MAG. **Withdraws:** my own 4138 rescue.
**Revises:** Patch 4134 (the rest-frame calculation was incomplete).
**Verify:** `series_standard_model/code/4139_a3g2_magnitude.py`.

---

## 1. The 4138 rescue does not survive being written out

I proposed one candidate at 4138: if only the *transient* bracelet channel reads b, there is no
long-range spin-dependent potential and comagnetometer bounds do not apply. It fails twice.

**(a) A_i is broadcast, not local.** The amendment puts A_i into LSP′, the GP→GP packet (A3′),
and into the DI-bit payload (AP-4) — the same long-range channel that carries Φ and V_i. A
component in the broadcast is long-range by construction, and 4125 itself identified A₁·A₂ as
ordinary long-range magnetic dipole–dipole. "The bracelet is transient" does not make the A
channel short-range.

**(b) The bound is not on a two-body force at all.** The comagnetometer measures a
spin-direction-dependent **energy of one neutron**, modulating at the sidereal frequency as the
lab rotates. No second body is involved, so an argument about two-body potentials cannot reach
it. I should have checked what the experiment measures before proposing the rescue.

## 2. The frame problem — and it revises Patch 4134

b = A·V with V = SSV_net, which the corpus defines in the **absolute (Nexus) frame**: A3′ has
LSP′ propagating *"at c = l_P/t_P in the absolute (Nexus) frame."* A nucleon at rest in the lab
is **not** at rest in that frame — it drifts at ~370 km/s, β = 1.23×10⁻³.

**4134 computed W = Σ s_i V_i in the nucleon rest frame.** Add the common drift **u** that the
absolute frame requires, and W → W + (Σ s_i)**u**. For the SU(6) proton Σ s_i = **+1**, not zero.
**The drift does not cancel.** Worse, the s-wave average cannot remove it: **u** is fixed in the
lab while the cage orientations average, so it survives exactly the averaging that killed the
internal term at 4134.

Residual ⟨b⟩ from drift alone ~ 1.2×10⁻³ — a factor 10⁴ above the ~10⁻⁷ hadronic PV bound, if
anything reads b linearly. **The 4134 calculation is incomplete as recorded, and the correction
does not go my way.**

## 3. The magnitude comparison

Empirical input: the ³He–¹²⁹Xe free-precession comagnetometer bound on the equatorial component
of a background field coupling to the **bound neutron** spin, **b̃⊥ⁿ < 8.4×10⁻³⁴ GeV** (68% C.L.;
Allmendinger *et al.*). This is an energy — a spin-direction-dependent splitting modulating at
the sidereal frequency.

Writing E = κ β cos θ:

| | κ | vs bound |
|---|---|---|
| bound requires | ≤ 6.8×10⁻³¹ GeV | — |
| strong / confining scale | 2×10⁻¹ GeV | ×2.9×10²⁹ |
| weak-suppressed hadronic (G_F m_π² Λ) | 4.5×10⁻⁸ GeV | **×6.7×10²²** |

Even the most suppressed scale the corpus offers — the one 4137 argued for — overshoots by ~10²³.
This is not a coefficient quibble.

**The corpus's own suppression claim, checked.** SD-1 answers Hossenfelder's preferred-frame
objection: *"The preferred frame is real but its effects are suppressed by the ratio of laboratory
scales to cosmological scales."* Taking that literally: lab/Hubble = 7.7×10⁻²⁷ gives κ ~ 1.5×10⁻²⁷
GeV — **still 2×10³ over**. Planck/Hubble = 1.2×10⁻⁶¹ over-suppresses by 25 orders. **The two
natural readings straddle the bound**, so the claim as written does not settle this case either
way. It names a mechanism without fixing the ratio. That is where the work has to go.

## 4. What this establishes, stated carefully

It does **not** show the amendment is false. It shows that **if** anything reads b linearly **and**
V is the absolute-frame SSV_net, a bound neutron carries a sidereal spin-energy modulation ~22
orders above the measured limit. One of those two must give.

**The live escape is not numerical.** SR-1 derives special relativity from the SSV_abs/SSV_net
decomposition — observables do not depend on absolute velocity. If that coverage extends to the A
channel, the drift term is unobservable and the bound does not bite. **But SR-1 predates the A3′
amendment and does not mention A_i.** The amendment added a broadcast component SR-1's derivation
never covered.

So the whole test reduces to one sharp question:

> **Is b = A·V Lorentz-covariant under CPP's own emergent SR?** Is V the **absolute** SSV_net —
> then b is frame-dependent and A3G-2 fires — or the **local relative** SSV_net, measured against
> the local sea rest frame — then b is frame-independent and A3G-2 passes?

## 5. Status change

**A3G-2 is neither passed nor unrun. It is CONDITIONALLY FIRING** — it fires unless b is shown
Lorentz-covariant, and the gap if it is not is ~10²³.

Per 4120, a fired A3G-2 **withdraws the amendment** rather than patching it. Nothing here fires it
outright, because the covariance question is genuinely open and is the corpus's to answer. But the
record should show that χ₄ is now in a materially worse position than the session-start summary
described, and that this is the second falsifier-status change today.

## 6. PD-008 — the convenient branch, marked

Every branch here went against the convenient reading, and I want that visible rather than
implied: my own rescue from one patch earlier is withdrawn (§1); my own calculation from five
patches earlier is revised as incomplete (§2); and the corpus's standing answer to exactly this
objection is checked and found not to cover the case (§3). The convenient move at each step was to
accept the existing text. I did press to the end rather than handing up early, per PD-008 — and
the end is a question that is genuinely the founder's, not mine.

## 7. What is owed

**TODO-4139-BCOVARIANT** — is V in b = A·V absolute or local-relative? This is a physics question
framed in a physical picture and is **PD-006(a) founder territory**, unlike the filter table (which
4108 established the founder cannot answer as posed). It decides A3G-2 and therefore the amendment.

χ₄ provisionally adopted, now with **three of nine** suite items standing clean. **F5 remains the
blocker** — but it is no longer the most urgent thing in the lane.
