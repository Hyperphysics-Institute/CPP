# EXECUTION RECORD — POOLED PROMOTION VARIATION: **CONDITION A PROMOTED**

**Patch 2912. Executed against the frozen §2 of
`mobile_sea_promotion_variation_record.md` (Patch 2911, applied before
execution).**

# VERDICT: **PROMOTE. CONJ-FP-1 CONDITION A HOLDS — no longer
# provisional.** The mobile Sea's response to a moving charge is
# FORWARD (repulsive), stable under a 1.3× domain change, at 5.4σ in the
# variation ensemble alone (5.7σ in the main ensemble).

---

## §1 — RESULT (pooled 18 values at ρ_max 10.4 / x_half 19.5)

Data: `data/2912_pooled_variation_results.json`, raw legs
`data/2912_raw_legs.json`.

Floor (6 paired β = 0 legs): mean **−0.0014 ± 0.21 ×10⁻³** — within 2σ
of zero (spectacularly so) ✓.

| β | 6-member Δ values ×10⁻³ | M_β ± SE_β ×10⁻³ |
|---|---|---|
| 0.05 | −0.81 +0.61 +0.08 +1.20 +1.20 +0.20 | **+0.41 ± 0.31** |
| 0.10 | +1.39 +2.25 +3.04 −0.09 +1.29 +2.33 | **+1.70 ± 0.45** |
| 0.20 | +3.91 +3.64 +3.09 +2.73 +2.52 +2.46 | **+3.06 ± 0.25** |

> **M = +1.725×10⁻³, SE = 0.322×10⁻³, M/SE = 5.36; 16/18 positive.**
> Frozen criteria: M > 0 ✓; M ≥ 2·SE ✓ (5.36); floor ✓. **⟹ PROMOTE.**

Notable within the ensemble: at β = 0.20 all six values are positive
with M_β/SE_β = 12.5 — at the largest speed and largest domain the
forward response is individually overwhelming.

## §2 — WHAT IS NOW ESTABLISHED, AND WHAT IS NOT

**Established (banded, variation-stable): CONJ-FP-1 Condition A.** The
Sea's differential response to uniform source motion is repulsive
(forward), growing with β, robust under domain scaling, with clean
at-rest controls, measured from the primitive with nothing adjustable.
Together with Condition B (retarded non-LW relay, closed 2895), **both
substrate-level conditions of the volume-transfer inertia mechanism now
HOLD.** The chaotic ZBW Sea coheres into a directed forward response.

**Not established:** the curvature/linearity of the drive at the
c ~ 0.05–0.3 discrimination level (renounced; owned by the hybrid
pipeline), LINK 2, LINK 3, and everything downstream in B1. The
per-β/β values (8.3, 17.0, 15.3 ×10⁻³) remain merely *consistent with*
linear growth.

## §3 — REGISTRY ACTION

CONJ-FP-1 condition table updated this patch (sketch appendix):
**Condition A: HOLDS (Patches 2909–2912, sign round + pooled 1.3×
variation). Condition B: CLOSED-VERIFIED (2895).**

## §4 — INFRASTRUCTURE (declared)

The kernel's numba disk cache proved fragile across processes
(ModuleNotFoundError from cache relocation, twice); disk cache disabled
(`cache=False`), a flag with no effect on generated code or numerics
(the 4×10⁻¹⁵ gate result is unaffected); per-process JIT (~60 s) is the
accepted cost, and single-process batching is the mitigation.

## §5 — STANDING

Ledger: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate (B)
79.5%. G1, P-A2-1, statics suspension, 7 July ruling stand. Next per the
2908 restructure: the hybrid pipeline (entrainment response function →
analytic dressed curvature), which awaits the founder's arcs-question
answer for its tabulation design.
