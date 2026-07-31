# TIER 4 — DERIVATION RECORD: THE VOLUME-TRANSFER INERTIA ARC

**Patch 2882. Written on the founder's audit of Tier-4 compression.**

**WHAT THIS FILE IS, AND WHY IT EXISTS.** `templates/documentation-suite.md`
defines Tier 4 as *"verbatim derivation reasoning — the moment-by-moment
groping, false starts, PAIRING resolutions, recognition moments… the
canonical record from which Tiers 1–3 derive."* The fragments this worker
filed at `reasoning/2873.md` through `reasoning/2880.md` are **not that.**
They are polished retrospective essays: `2880.md` runs 67 lines of which
**three** contain any mathematics. **That is Tier 3 content — curated
vignettes in finished prose — filed in Tier 4's location.** The structure
is thereby inverted: Tiers 1–3 are supposed to derive from Tier 4, so
Tier 4 must be the richest layer, and ours was the thinnest.

**This file supplies the derivations that were compressed to conclusions.
Nothing here is new physics. Everything here was done and then not
written down.**

---

## §1 — DERIVATION A: FROM THE MECHANISM TO C·PSR = SSV_abs

**Recorded conclusion (CONJ-FP-1 §2): four lines. Actual chain, below.**

### A.1 — The two statements being combined

**The CPP primitive** (`master_glossary.md`; founder ruling 7 July 2026):
each Moment a CP displaces by

    d = (|SSV_net| / SSV_abs) · PSR                                  (1)

where SSV_abs is the magnitude-sum of arriving contributions, SSV_net the
vector sum, and PSR the per-Moment reach ceiling. The prefactor is a
**directional coherence fraction** in [0,1]: unity when all arrivals
agree in direction, zero when they cancel exactly.

**The founder's mechanism** (founders_voice, 30 Jul): the net drive is
the slab of arc volume transferred from the charging side to the
discharging side per Moment. That slab has thickness equal to one
displacement increment. So, with C collecting arc number density × the
Position Plane's interacting cross-section × forward impulse per
discharging arc:

    SSV_net = C · d                                                  (2)

**Why (2) has this form and not another.** The transferred volume is
(cross-section) × (slab thickness), and the slab thickness *is* d by
construction — the plane advances exactly d per Moment. Each arc in that
volume contributes one forward impulse on discharge. So the drive is
linear in d with no other d-dependence. **This is the step that makes the
mechanism work where retardation could not:** a propagation delay gives an
asymmetry ∝ a (see §3), whereas (2) is ∝ d ∝ v, which is the scaling
persistence requires.

### A.2 — The substitution

Put (2) into (1):

    d = (C·d / SSV_abs) · PSR

**d appears on both sides and is nonzero for a moving CP, so divide:**

    1 = C · PSR / SSV_abs

    ⟹   C · PSR = SSV_abs                                            (3)

### A.3 — Reading (3): why this is not a tautology, and what it is instead

**The worker's first reaction was that this was circular** — v = k·v looks
vacuous. That reading is wrong and the reason matters. The displacement
cancelled, but what remains is **not** an identity in d; it is a
constraint on three quantities that are each defined independently of the
others:

- **C** — from arc physics (density, cross-section, impulse per discharge)
- **PSR** — from the substrate (per-Moment reach ceiling, = l_P at rest)
- **SSV_abs** — from the local field magnitude-sum

None is defined in terms of the others. **(3) is therefore a real physical
condition, not a restatement.**

### A.4 — The three regimes, derived

Perturb: suppose C·PSR = (1+δ)·SSV_abs. Then (1) and (2) give
d_next = (1+δ)·d. Hence

- **δ > 0** (C·PSR > SSV_abs): d grows each Moment. **Runaway.**
- **δ < 0** (C·PSR < SSV_abs): d shrinks each Moment. **Drag; motion decays.**
- **δ = 0**: d reproduces itself exactly. **Every velocity persists —
  Newton I.**

**This is why Newton I is a marginality condition in this mechanism, and
why "every v is a solution" is the correct reading of the δ = 0 case
rather than a sign of vacuity.** It is a one-parameter family of
self-consistent coasting states, each neutrally reproduced.

### A.5 — The observation that (3) may be forced, and its status

PSR is *defined* as the displacement achieved at **full coherence**, i.e.
d = PSR exactly when |SSV_net| = SSV_abs. Evaluate (2) at that point:

    SSV_net = C · PSR,  and full coherence means SSV_net = SSV_abs

    ⟹   C · PSR = SSV_abs

**which is (3).** So the marginality condition may be an identity forced
by PSR's own definition, in which case Newton I follows from the primitive
with nothing tuned.

**NOT BANKED, and the reason is specific.** The step assumes the *same* C
governs both the full-coherence configuration and the coasting
configuration. C contains a geometric cross-section which need not be the
same in both. **If C is configuration-dependent, C_coherent ≠ C_coast and
the identity fails.** This was the seventh favourable convergence of the
arc, arriving one turn after it was wanted; six prior ones died. Filed as
Route 2 of CONJ-FP-1, not as a result.

### A.6 — The density-cancellation observation

C ∝ (arc number density) by construction. SSV_abs is a magnitude-sum over
arriving contributions and is **also** ∝ (arc number density). **If both
scale identically, density cancels from (3) and the marginality condition
is density-independent** — which would remove the hardest input from
Q1, since the DP-Sea density is exactly what OPEN-SEA-DENSITY-1 could not
supply. **Not verified.** The two densities are not obviously the same
density: C counts arcs *in the transferred slab*, SSV_abs sums arrivals
*at the CP from all directions*. They coincide only for a spatially
uniform Sea.

## §2 — DERIVATION B: THE SIGN, FROM DIPOLE ALGEBRA

**This derivation appeared NOWHERE in the repository. Only its conclusion
reached the founder. It is the load-bearing step of the whole mechanism.**

### B.1 — Setup

Positive CP of charge Q at the origin. A polarizable DP at position
**r** relative to it, with induced dipole moment **p**. Field at the CP
due to that dipole, with **n̂** the unit vector from dipole to CP
(so **n̂** = −**r̂**):

    E_dip = [3(p·n̂)n̂ − p] / r³

Substituting **n̂** = −**r̂**, the two sign flips cancel in the first term:

    E_dip = [3(p·r̂)r̂ − p] / r³                                      (4)

    F_on_CP = Q · E_dip                                              (5)

### B.2 — Equilibrium case: attraction, both sides, cancelling

The CP's field at the DP points along **+r̂** (outward from a positive
source), so an equilibrated induced dipole has **p** = p **r̂**, p > 0.
Then p·**r̂** = p, and (4) gives

    E_dip = [3p r̂ − p r̂]/r³ = 2p r̂ / r³

    F_on_CP = 2Qp r̂ / r³        — along +r̂, i.e. TOWARD the dipole.

**Attraction, as expected for an induced dipole.** A DP ahead pulls the CP
forward; a DP behind pulls it backward. **For a fore/aft symmetric
distribution these cancel exactly** — which is the "it truly would be a
static system" of the founder's account, here derived rather than asserted.

### B.3 — Stale case: repulsion, and the sign reverses

The axial polarization must **flip** as the DP crosses the Position Plane,
because the CP's field points forward ahead of it and backward behind it.
It cannot flip instantaneously. So a DP just past the plane retains its
**fore-configuration** polarization.

Set up: DP now behind, so **r̂** = −**x̂**. Stale polarization still points
along +**x̂**: **p** = p **x̂** = −p **r̂**. Now p·**r̂** = −p, and (4) gives

    E_dip = [3(−p)(−x̂) − p x̂]/r³ = [3p x̂ − p x̂]/r³ = 2p x̂ / r³

    F_on_CP = 2Qp x̂ / r³        — along +x̂, i.e. FORWARD.

**The sign reverses.** A stale, anti-aligned arc behind the CP **repels**
it forward. This is the founder's *"the repulsive pole is now closer to
the CP-current in the aft configuration"* — derived, and confirmed.

### B.4 — What this retracts

The worker had told the founder that *"conventional medium physics
predicts the opposite sign."* **§B.3 shows that is false as stated.** The
textbook polarization-drag result assumes the polarization has
**equilibrated** to its local field (§B.2). The stale regime (§B.3) is a
different regime and the force genuinely reverses in it. **Retraction
issued to the founder 1 Aug and recorded here with the algebra that
forced it.**

## §3 — DERIVATION C: WHY RETARDATION ALONE CANNOT DO IT

The prior record carries this mechanism as a *retardation* account
(`founders_voice/founder_mechanism_ssv_asymmetry_retardation_2026-07-29.md`).
The founder has since disavowed time-delay in favour of displacement.
The derivation showing why that disavowal was necessary:

For a source in **uniform** motion, the retarded field configuration is
just the boosted static configuration. It carries no fore/aft asymmetry:
the Liénard–Wiechert fields of a uniformly moving charge point at the
**instantaneous** position, not the retarded one. A propagation delay
therefore produces an asymmetry proportional to **ȧ**, i.e. to the rate of
change of the drive —

    asymmetry ∝ a  ⟹  vanishes identically at constant v.

**So retardation explains the acceleration phase and goes silent at
coasting.** The founder's displacement mechanism (§1, eq. 2) gives
asymmetry ∝ d ∝ v, which does not vanish. **The two accounts are not
variants; only one of them can sustain Newton I.** The file title in
`founders_voice/` now misdescribes the mechanism it records.

## §4 — COMPUTATION D: THE RELAXING-MEDIUM MODEL, AND ITS NEGATIVE RESULT

**Scripts, committed at Patch 2882 after running uncommitted at
Patch 2880 — a reasoning-capture violation disclosed in the commit:**
`code/2882_wake_sign_relaxing_medium.py`, `code/2882_wake_sign_robustness.py`.

### D.1 — What was modelled

Linear relaxation toward the instantaneous-field equilibrium:

    dp/dt = (χ E(r) − p)/τ

on a cylindrical grid, with the force on the charge from (4)–(5), summed
over the medium in steady state. The single dimensionless control is
ε = vτ/d — the lag distance in units of the interaction scale, i.e.
ε_mem.

### D.2 — Result

**Drag at every ε tested, 0.02 through 8.0. No sign change anywhere.**
Magnitude peaks near ε ≈ 1.2 and declines on both sides — the classic
dielectric-drag resonance. **Robust across seven geometry/cutoff
variations**; magnitude is cutoff-sensitive as b_min → 0 (near field
dominates) but the sign never moves.

**Model self-validation:** at ε = 0 the drive is −5.66×10⁻¹⁶, i.e.
numerically exact zero. **Instantaneous response gives exact
cancellation**, which is §B.2's analytic result recovered numerically.
That is what licenses the rest of the sweep.

### D.3 — What it does and does not establish

**The stale-forward region of §B.3 is real but SUBDOMINANT** under linear
relaxation: the equilibrated far-rear pull outweighs it at every lag.
Adding a directional discharge impulse as an adjustable term, the sign
flips only when that term is ~35× the conventional dipole force — **a
dominant mechanism, not a correction.**

**Therefore:** the founder's mechanism cannot be a lag-correction to
conventional polarization response. It requires the arc to be a
**store-and-release element**, which the founder confirmed (1 Aug). **The
computation constrains the claim; it does not refute it, because it models
the wrong object.**

## §5 — THE MOMENTUM-CONSERVATION OBJECTION, DERIVED

A collapsing ± pair returns toward its own centre of mass. **For a
symmetric collapse the centre of mass does not move, so the collapse
delivers zero net momentum to anything.** The discharge can drive the CP
only if the collapse is asymmetric — one pole travelling further,
shifting the pair's centre of mass rearward so the CP goes forward.

The asymmetry exists, because the two poles sit at different distances
from the CP and the CP's field differs at each. But in a multipole
treatment it enters at relative order

    ξ_arc ≡ (charged arc separation) / (inter-DP spacing)

**ξ_arc ≪ 1 ⟹ suppressed ⟹ mechanism fails.
ξ_arc ~ 1 ⟹ multipole expansion invalid ⟹ suppression does not apply.**

**This is the single unmeasured input and the reason CONJ-FP-1 is a
conjecture rather than a theorem.**

## §6 — FALSE STARTS, RECORDED BECAUSE TIER 4 REQUIRES THEM

1. **"The identity is circular."** Wrong — §A.3. The displacement cancels
   but three independently defined quantities remain.
2. **"Conventional physics predicts the opposite sign."** Wrong as stated
   — §B.4. True only for equilibrated polarization.
3. **"The 2868 forward F_hold supports the founder's sign."** Wrong —
   2496 is a scalar wave field with no arcs and no relaxation time. The
   worker offered this to the founder as his strongest evidence and
   withdrew it (Patch 2880 §7).
4. **"The coast oscillates, which may supply the signed kernel S1
   required."** Wrong — measured best-fit frequency indistinguishable from
   zero (Patch 2875). Killed by the computation named as its own banking
   condition.
5. **Treating a forward force on a coasting CP as a runaway pathology.**
   Newtonian reflex; in a v ∝ SSV_net substrate a persistent forward drive
   gives persistent *velocity*, not acceleration.

**Items 1–3 were all corrections in the founder's favour, made by the
worker against its own prior position. Items 4–5 were the worker
correcting itself unprompted. Recorded together because a Tier 4 record
that keeps only the successful chain is worth less than one that keeps the
groping.**
