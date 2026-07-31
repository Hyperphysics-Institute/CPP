# THE TWO RELAYS ARE ONE FAMILY — AND PATCH 2887 OVERCLAIMED

**Patch 2890. Founder proposal: "Perhaps the resolution is simply to have
two models, where one decays into the other… can the two models be seen as
modifications of the other domain due to the addition or subtraction of
terms that become active?" That proposal is CORRECT and is implemented and
measured here.**

---

## §1 — CORRECTION: PATCH 2887 CLAIMED "NO LIGHT CONE". THAT WAS WRONG.

**2887 stated the AUTOMATON-2 convolution relay has "no finite maximum
signal speed and no light cone." That is FALSE and is withdrawn.**

`front_kernel(R)` has **finite support**, so the convolution engine cannot
propagate faster than its maximum hop radius per Moment. Measured
(`code/2890_light_cone_edge_vs_bulk.py`, M = 96, R = 4):

| t | ⟨r⟩ bulk | r_max edge | **edge/t** |
|---|---|---|---|
| 1 | 4.038 | 5.657 | **5.6569** |
| 2 | 5.428 | 11.314 | **5.6569** |
| 3 | 6.611 | 16.971 | **5.6569** |
| 4 | 7.600 | 22.627 | **5.6569** |

**edge/t = 5.6569 exactly — the kernel's maximum hop radius.** (The
apparent decline at t ≥ 5 is the extreme-tip amplitude falling below the
1e-12 detection threshold, not the front slowing.)

**What 2887 measured correctly:** the **bulk** spreads diffusively,
⟨r⟩ ~ √t. **What 2887 concluded wrongly:** that this means no light cone.
**Bulk transport class and maximum signal speed are independent
properties.** A telegraph/transport system has both a strict light cone and
diffusive bulk. That is exactly what this engine is.

**Consequences of the correction:**
- The 2884 substrate-viability escalation was **overstated**. The relay
  does have an invariant maximum speed, so relativity and photon
  kinematics are not excluded by this engine's transport class.
- The 2887 sentence "special relativity, retardation, and photon
  kinematics are not available from a √t front" is **withdrawn**.
- **G1 and P-A2-1 continue to stand.** Unaffected in both directions.

## §2 — THE UNIFIED FAMILY (founder's proposal, implemented)

    Q_d(x, t+1) = (1−σ)·Q_d(x−d, t) + σ·⟨Q⟩(x−d, t) + inj/12

with ⟨Q⟩ the direction-average over the 12 FCC channels.

- **σ = 0** — pure advection. Bits keep their heading forever.
  **This is the directed relay of Patch 2889.**
- **σ = 1** — complete re-isotropisation each Moment.
  **This is the convolution engine of AUTOMATON-2.**

**σ is physically the probability that a DI-bit is absorbed and re-emitted
isotropically rather than continuing in its direction.** Its reciprocal is
a **mean free path** λ = c_lat/σ. This is the standard linear-transport
(radiative transfer) structure, whose continuum limit is the **telegraph
equation** — a wave equation with a damping term, reducing to a pure wave
as σ → 0 and to diffusion as σ → ∞, and **retaining a strict light cone at
every σ.**

**The founder's "terms that become active" is exactly the scattering term.**

## §3 — MEASURED FAMILY BEHAVIOUR

`code/2890_transport_family_sigma.py`, M = 48.

| σ | bulk p | **edge/t** | static slope |
|---|---|---|---|
| 0.00 | 1.34 | **1.0607** | −0.098 |
| 0.25 | 1.09 | **1.0607** | −0.530 |
| 0.50 | 0.91 | **1.0607** | −0.637 |
| 0.75 | 0.76 | **1.0607** | −0.772 |
| 1.00 | 0.63 | **1.0607** | −0.970 |

**THREE FINDINGS.**

1. **The light cone is σ-INVARIANT.** edge/t is identical to four decimal
   places across the entire family. Scattering changes bulk transport and
   **leaves the maximum signal speed untouched** — the defining signature
   of transport dynamics, and confirmation that these are one family.
2. **Bulk transport slides smoothly ballistic → diffusive** as σ rises.
3. **Static falloff slides from rays (−0.10) to 1/r (−0.97)** as σ rises.
   **Scattering is what converts 12 discrete rays into a continuous
   field.**

**Fit caveat, stated rather than buried:** the absolute bulk exponents
carry an offset artifact — injection enters at t = 1, so ⟨r⟩ ∝ (t−1) and a
log-log fit over t = 2..10 is biased upward by ≈ +0.33. This is why σ = 0
reads 1.34 rather than the exact 1.0000 measured at Patch 2889. **The
offset is identical across all σ, so the TREND is sound and the absolute
values are not.**

## §4 — THE RESOLUTION IS A LENGTH SCALE, NOT A PARAMETER CHOICE

**No single σ gives both good statics and ballistic bulk at the same
radius.** σ = 0.25 gives near-ballistic bulk (p ≈ 1.09) but poor statics
(−0.53); σ = 1 gives good statics (−0.97) but diffusive bulk (0.63).

**But in transport physics the crossover is SCALE-DEPENDENT, not a global
property.** The same medium is:

- **ballistic at r ≪ λ** — few scatterings, bits travel straight
- **diffusive at r ≫ λ** — many scatterings, random walk, → Poisson → 1/r

**So one substrate can be ballistic at short range and diffusive at long
range, and both prior results can be simultaneously correct.**

**This makes the dilemma testable rather than fatal:**

- **Inertia physics** (CONJ-FP-1, round-trip asymmetry) lives at **r ~ 1–2
  GP** — the near field, where retardation structure must survive.
- **The Coulomb measurement** (G1, ±0.4%) was taken at **r ∈ [3,6]** — far
  enough out that diffusive averaging yields 1/r.

**If λ falls between these scales, both results hold at once and there is
no dilemma.**

## §5 — REGISTERED NEXT TESTS

1. **Measure λ from the C22 spec** — what physically sets the DI-bit
   scattering probability? This is a founder-physics question, not a
   coding one.
2. **Scale-resolved front test:** measure the bulk exponent p **as a
   function of radius** at fixed σ, and confirm the ballistic→diffusive
   crossover occurs at r ≈ λ.
3. **Re-run the LW discriminant at r ≪ λ**, where the relay is ballistic.
   Condition B was never testable in the diffusive regime; it should be
   testable in the near field.
4. **Check whether the G1 Coulomb fit survives at σ < 1** with radii
   pushed beyond λ.

## §6 — STANDING

**CONJ-FP-1 Condition B: OPEN, and now testable in principle** — the near
field of a transport relay is ballistic and retarded, which is what the
mechanism requires.

**Patch 2884 escalation: DOWNGRADED.** The relay does possess an invariant
maximum speed; coasting is not excluded on light-cone grounds.

**Ledger untouched:** 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/DM-2/DM-3; Candidate (B) 79.5%. **G1 and P-A2-1 stand.**
