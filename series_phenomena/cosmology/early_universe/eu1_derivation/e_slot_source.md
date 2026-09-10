# The 3862 residual resolved — **AP-4's E slot must be sourced by the origin GP's RESIDENT CP charges, and this is forced rather than chosen.** Read strictly as arrivals-only, the E recursion is linear and homogeneous with a zero initial condition, so E = 0 at every GP for all time and the theory has no physics at all. First-Moment bits carry count **and** direction. **One-line clarification owed to AP-4**

**Patch 3870, Session 194, 9 Sep 2026. Lane: EU.** Discharges the residual left open at 3862 §3. Verify `scripts/3870_e_slot_source.py` (10/10). Reasoning `reasoning/3870_e_slot_source.md`. Nothing adopted; **no amendment proposed** — the finding is that the corpus's practice is already Reading R and its wording should say so; PRED-C-96 untouched; 3710 not retired.

## §1 The residual, and the search that framed it (verify T1, T2)
3862 closed the AP-4c retraction with one narrow observation left open: AP-4 defines the payload's directional slot as

> **E = the vector sum of all polar-charge contributions (eCP and qCP indistinguishably) integrated by the origin GP in the previous Moment.**

Read strictly, the E a GP imprints comes **only from what it received** — and at Moment 1 it received nothing. So first-Moment bits would carry count without direction.

**D-1 applied first.** I searched `master_glossary.md`, `axiom-registry.md` and `founders_voice/` for any statement that a GP's **own resident CP charges** source the E it imprints. **No such statement exists.** The corpus words E as previous-Moment integration everywhere it appears. The absence is the finding, and it is reported as an absence rather than filled in by assumption.

## §2 The strict reading is excluded by reductio (verify T3, T4)
Reading S (arrivals-only) makes the E recursion

> **E_i(t) = Σ_j E_j(t−1)** — linear and **homogeneous**.

Its initial condition at ignition is the one 3816 §1 established and 3862 confirmed: **every register empty, E_j(0) = 0.** A linear homogeneous recursion started at zero stays at zero, whatever the weights and however many neighbours contribute.

> **Under Reading S, E = 0 at every GP for all time.**

And the consequence is not a failed ignition but the absence of physics: SSV_net = E + S = 0 identically, so by A1′/AP-3 **no CP ever displaces**, and nothing in the theory ever happens. The recursion never leaves its fixed point.

## §3 So Reading R is forced (verify T5, T6)
> **Reading R:** E_i(t) = **q_i(resident CPs)** + Σ_j E_j(t−1).

The resident charge is a **source term**, making the recursion inhomogeneous. E is nonzero from Moment 1 and propagates outward through the cascade.

**This is a derivation of the reading, not a preference between glosses.** Reading S is excluded; Reading R is the only remaining one; therefore AP-4's E slot is resident-sourced. It has the same shape as 3860's surviving half, where "deposit exactly once" was forced by emission-budget conservation rather than stipulated — a consistency requirement doing the work of a postulate.

## §4 What it discharges (verify T7, T8)
- **The 3862 residual is resolved.** First-Moment bits carry **count and direction**: the count from AP-4's unconditional fixed emission, the direction from the resident CPs. The observation that they "carry count without direction" was correct only under the excluded reading, and is withdrawn.
- **The founder's ignition picture requires it.** Twelve CPs per GP each displacing to an icosahedral vertex (3813/3814) needs a directional SSV_net at Moment 1. Under Reading R the resident twelve supply it. Under Reading S ignition could never occur — so the picture presupposed Reading R all along, which is further evidence that Reading R is what the corpus has always meant.

## §5 What is owed
**A one-line clarification to AP-4's E-slot wording**, not an amendment. Reading R is what the programme has always practised — every field result in it presupposes a resident source, or there would be no fields — but the ratified text admits a reading that yields no physics, and a ratified text should not admit that.

**This is the founder's call**, and it is small: the E slot's definition should say that the origin GP's own resident CP charges enter the sum alongside the previous Moment's arrivals. No axiom count changes; no result moves.

## §6 Honest scope
- The reductio depends on the E recursion being **linear** in the arrivals. AP-4 says *vector sum*, which is linear. If some non-linear or threshold element were intended, the argument would need redoing — but nothing in the corpus suggests one.
- I did not find Reading R stated anywhere, and I am not treating its absence as proof it was never intended. The claim is that **the text admits an excluded reading**, not that the programme believed it.
- **SSV_abs is untouched.** It sums *magnitudes* and remains count-like and arrival-built; the resident term is directional-slot only. n̄ stays a count.

## §7 Standing
- **3862's residual DISCHARGED.** First-Moment bits carry count and direction.
- **Reading R (resident-sourced E) is FORCED** by reductio on Reading S.
- **One-line AP-4 clarification owed** — founder's call, no axiom count change, no result moved.
- **The founder's ignition picture is supported**, and shown to have presupposed Reading R.
- Unaffected: SSV_abs, n̄, PRED-C-96's tilt, T-1, T-2, the amplitude closure, 3816's restored basis.
- **Lane status otherwise unchanged from 3866/3868** — substantive work complete pending maintainer decisions.
