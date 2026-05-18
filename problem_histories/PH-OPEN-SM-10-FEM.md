# Problem History: OPEN-SM-10-FEM — First-Principles Quark Mass from FEM Simulation

**Created:** 9 April 2026
**Status:** OPEN (Phase 1–2 CPU proof-of-concept complete; Phase 3 GPU pending)
**research_frontier.md entry:** OPEN-SM-10-FEM

---

## The Problem

Derive the quark mass scaling V^(7/3) from explicit DP chain-formation dynamics, without imposing any scaling law. If DP chains self-organise to produce the right mass ratios when placed in cage geometries of different sizes, the entire quark mass spectrum follows from geometry alone.

---

## The Journey

### 9 April 2026 — The Simulation Campaign

Thomas and Opus conducted five simulation versions in a single session, each revealing new physics:

**v1 (Simple DP counting):** FAILED. Each cage CP bonds to exactly 1 Sea DP. No cascading. Ratios are trivial.
*Lesson: Single-bond-per-CP doesn't create chains.*

**v2 (Dipole chain simulation):** Chains form (thousands of organised DPs). But ratios are ~2–25× instead of 14–1850×.
*Lesson: Raw DP counting misses cooperative enhancement.*

**v3 (Geometric chain model with crossing energy):** Crossing energy dominates (60–94% of mass). With constant cascade rate f=0.3, ratios are 5/27/76 instead of 14/45/1850.
*Key finding: Crossing energy IS the dominant mass source.*

**v4 (Density-dependent cascade):** Best fit (f=0.10, p=1.4) gets bottom to 0.6% but misses charm by 59% and top by 36%.
*Key finding: The needed cascade rates are: Strange 0.10, Bottom 0.51, Charm 0.74, Top 0.97. The top quark is near the percolation threshold.*

**v5 (expected):** GPU implementation with full 3D geometry and self-consistent chain formation.

### Current State

Phase 1–2 (CPU proof-of-concept) demonstrated that:
1. Crossing energy is the dominant mass mechanism
2. The cascade rate must be density-dependent
3. The top quark is qualitatively different (near percolation threshold)
4. No single (f_base, p) pair fits all four quarks

Phase 3 (GPU simulation) is the next step: place cage CPs in full 3D geometry, fill with explicit DP Sea, let CPs seek opposite-polarity targets, count organised DPs. Two regimes: cascade (s,c,b) and relay (top).

---

## Success Criteria

DP count ratios match PDG mass ratios to <5% without calibration.

---

## Cross-References

- **research_frontier.md entry:** OPEN-SM-10-FEM
- **Related:** OPEN-SM-cage-1 (derive α), OPEN-SS-1 (quark mass formula)
- **Development transcript:** `series_standard_model/development-transcripts/SM-10_FEM_computational_journey_transcript.md`

---

*Stub created 12 April 2026. Needs enrichment from SM-10 transcript (9 April 2026 session) and future GPU sessions.*
