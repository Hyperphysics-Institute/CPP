# OPEN-EU-BATH-DEPTH-1 RESOLVED — the bath keeps up at depth 10⁷⁴, with a margin of ~300. The item reduces to how the mixing count scales with depth, and **AP-3's per-Moment synchrony makes the substrate massively parallel**, so the scaling is **logarithmic**: N_mix ~ ln n̄ ~ 170, R = 3.3×10⁻³, **~300 re-thermalizations per e-fold**. Serial and diffusive scalings would have failed by 69 and 32 orders

**Patch 3874, Session 196, 9 Sep 2026. Lane: EU.** Works the last open EU item, registered on CONV-045 ratification as Priority 3 and explicitly non-blocking. Verify `scripts/3874_bath_depth.py` (8/8). Reasoning `reasoning/3874_bath_depth.md`. Nothing adopted; no constant minted; PRED-C-96 untouched; 3710 not retired.

## §1 D-1 first: the mechanism was on file (verify T1)
Patch 0769 §(b) already sets up the bath-rate test:

> τ_eq ~ N_mix·t_P against t_efold ~ 1/H, so **R = N_mix·(H/E_Pl)** must be ≪ 1. With N_mix = O(10–30) toy-measured (0753), **R ~ 4×10⁻⁴** — the bath re-thermalizes ~2600 times per e-fold.

**But 0769 established that for the generic case.** OPEN-EU-BATH-DEPTH-1 asks whether it survives at **depth ~10⁷⁴** — whether N_mix stays O(10–30) when the stack is that deep. That is a real question and 0769 did not answer it: **mixing times generally grow with system size**, and a stack of 10⁷⁴ is not a generic system.

## §2 The item reduces to one exponent (verify T3, T4)
The threshold is sharp: **R = 1 at N_mix = 5.2×10⁴.** So the bath clause survives depth **iff** N_mix at n̄ = 10⁷⁴ stays below ~5×10⁴. Four candidate scalings, and they split cleanly:

| N_mix scaling | N_mix at n̄ = 10⁷⁴ | R | verdict |
|---|---|---|---|
| O(1), depth-independent | 20 | 3.9×10⁻⁴ | **passes** (2600/e-fold) |
| **O(ln n̄)** — parallel mixing | **170** | **3.3×10⁻³** | **passes** (304/e-fold) |
| O(√n̄) — diffusive | 10³⁷ | 1.9×10³² | fails by 32 orders |
| O(n̄) — serial | 10⁷⁴ | 1.9×10⁶⁹ | fails by 69 orders |

**There is no middle ground.** Either the mixing is parallel-like, in which case the margin is hundreds, or it is serial or diffusive, in which case the bath clause is destroyed at depth and with it the Gibbs ln n̄ that the tilt rests on.

## §3 The resolution is structural (verify T5, T6, T7)
> **AP-3 (per-Moment synchrony, ratified Patch 2982): every GP executes Perceive → Compute → Displace every Moment, and every CP displaces every Moment.**

**The substrate is massively parallel, with one actor per CP.** It is never serial — there is no queue, no single agent stepping through occupants — and it is not single-agent diffusive, because every CP acts simultaneously rather than one walker wandering the state space. Those are precisely the two failing scalings, and **the protocol excludes both by construction.**

Parallel mixing of n items by n actors is **O(log n)**. Hence

> **N_mix ~ ln n̄ ~ 170 at depth 10⁷⁴ ⇒ R = 3.3×10⁻³ ⇒ ~300 re-thermalizations per e-fold.**

**The bath keeps up, with a margin of ~300 to the failure threshold.** OPEN-EU-BATH-DEPTH-1 is resolved.

A satisfying detail: the depth penalty is exactly ln n̄ = 3N_rem — the same logarithm that carries the count law. Going from the generic case to depth 10⁷⁴ costs a factor 170/20 ≈ 8.5 in mixing time and nothing else.

## §4 Honest scope (verify T8)
- The result rests on the **parallelism argument**, which is structural (AP-3) rather than a measured mixing time at depth. **What is excluded is serial and diffusive scaling; what is asserted is that the protocol cannot be either.**
- **N_mix itself remains toy-measured** (0753, O(10–30)), not derived. This patch establishes its *scaling*, not its value.
- The depth scaling is **argued from parallelism, not simulated at depth.** A direct measurement at large n̄ would harden it, and is the natural follow-on if anyone wants one — though at a margin of 300 it is not urgent.
- **Status: grounded, not proven** — deliberately the same status 0769 claimed for the bath clause itself. It would be inconsistent to claim more for a sub-question than the clause it serves.

## §5 Standing
- **OPEN-EU-BATH-DEPTH-1: RESOLVED.** N_mix ~ ln n̄ by parallelism; R = 3.3×10⁻³ at depth 10⁷⁴; ~300 re-thermalizations per e-fold; margin ~300 to failure.
- **The two failing scalings are excluded by AP-3's per-Moment synchrony**, not by assumption.
- **Nothing new is added to the conditionality.** The bath clause remains a working postulate (0769, LEMMA-NS-BATH); this patch shows only that *depth* does not break it.
- **This was the lane's last open item.** With it resolved, the EU lane's queue is empty in fact as well as in description — the remainder is maintainer decisions, a founder picture question, and Isak's recompiles.
- PRED-C-96, T-1, T-2, the amplitude closure, 3816: unaffected.
