# Reviews and FAQ: SM-3 — The Koide Relation from the Colour Cage Base Graph

**Series:** 600-Cell Standard Model Emergence
**Document type:** Living review record and FAQ
**Last updated:** 30 March 2026


# PART 1: FORMAL REVIEWS


## Review 1: Claude Sonnet Sessions B–G (March 2026)

**Reviewers:** Claude Sonnet (Anthropic) across multiple iterative sessions
**Date:** March 2026
**Context:** SM-3 was developed iteratively. The main theorem was established early; the challenge was deriving all three propositions (P1, P2, P3) from CPP axioms rather than stating them as independent postulates. Several candidate derivations of P3 (the equipartition postulate) were attempted before the DP Sea thermalisation argument succeeded. Several candidate mechanisms for deriving θ were attempted before the structural impossibility theorem (SM-4 Theorem 2) was proved.


### Objection 1.1: P3 (Thermal Equipartition) Was Originally a Postulate

**The objection:** Early versions stated P3 — equal eigenstate occupation — as an axiom: "the three K₃ eigenstates are equally populated." This was labelled a postulate of the K₃ spectral theorem, which meant the theorem had a free postulate with no CPP derivation.

**Assessment: VALID — major theoretical gap**

A theorem with an ungrounded postulate is not a theorem — it is a conditional statement ("if P3, then K = 2/3"). The CPP programme's standard requires all three propositions to be derived from the seven CPP axioms. P3 needed a physical derivation.

**Response/revision (v5):** P3 is derived from DP Sea thermalisation in the high-temperature limit. The ZBW resonator couples to the DP Sea thermal bath (Caldeira-Leggett coupling via DI-bit exchange). Since kT_P/ℏω₀ ≈ 10²⁰ >> 1, the Boltzmann state approaches the uniform mixture |c_n|² = 1/3 for all three eigenstates. This is state-counting equipartition in the high-temperature limit — a derived consequence of the DP Sea temperature being vastly greater than the ZBW energy scale. P3 is now a derived proposition, not a postulate.

**Status: RESOLVED**


### Objection 1.2: θ Cannot Be Derived from K₃ + SSV

**The objection:** Multiple sessions attempted to derive the Koide phase θ = 132.73° from the K₃ framework: Aharonov-Bohm flux through the cage triangle (Session B), spin-orbit coupling within the cage (Session C), self-consistent ZBW mass feedback (Session K), 4D 600-cell embedding breaking C3 degeneracy (Session G). All failed. The question was: is θ derivable in principle from the K₃+SSV framework, or is there a structural reason it cannot be?

**Assessment: STRUCTURAL IMPOSSIBILITY — important negative result**

Session G established that the C3 symmetry of K₃ makes the antibonding subspace exactly degenerate: both antibonding eigenstates have eigenvalue −1. Any mechanism that respects C3 (which the cage geometry requires) cannot split this degeneracy and therefore cannot select θ. The antibonding eigenstates are related by the C3 rotation, so C3 symmetry permutes them — any physical quantity that is C3-invariant cannot distinguish between them. This is not a gap in our analysis; it is a structural feature of K₃ that makes θ inaccessible to the K₃+SSV framework by construction.

**Response/revision (SM-4 Theorem 2):** The structural impossibility is proved as a theorem in SM-4: "No mechanism acting on the K₃ cage base that respects C3 symmetry can break the antibonding degeneracy and select θ." This converts a failure (θ cannot be derived here) into a theorem (θ cannot be derived here, and here is the proof). SM-3 registers θ as OPEN-P-SM-7d with the notation that its derivation requires the electroweak sector.

**Status: RESOLVED — structural impossibility established and documented**


### Objection 1.3: SM-3 v3 Did Not Have All Three Propositions Labelled

**The objection:** Version 3 proved K = 2/3 but did not make the three-proposition structure explicit. Readers could not easily identify which physical inputs the theorem depended on.

**Assessment: VALID — pedagogical clarity**

**Response/revision (v4/v5):** Three explicit Proposition environments (P1, P2, P3) added, each with a derivation subproof. A scope table in §6 explicitly distinguishes what is "Proved," "Derived," "Calibrated," and "Open." The paper now makes the logical structure immediately legible.

**Status: RESOLVED**


### Objection 1.4: Why Quarks Do Not Satisfy Koide Not Explained

**The objection:** Version 3 stated only that quarks do not satisfy Koide (K ≈ 0.73 and 0.85 observed). It did not explain why — which would leave the reader wondering whether the CPP framework is selective or post-hoc.

**Assessment: VALID — scientific completeness**

**Response/revision (v4/v5):** A Remark in §5 explains the mechanism: quarks carry qDP chain binding energy, inter-cage bonding, and cage-depth scaling that leptons do not. These strong-sector contributions break the K₃ spectral symmetry underlying the theorem. The deviations (10% and 27%) are consistent with the CPP account of quark mass structure. The fact that quarks do not satisfy Koide is a CPP prediction, not a coincidence.

**Status: RESOLVED**


## Summary Table

| # | Objection | Assessment | Status |
|---|-----------|-----------|--------|
| 1.1 | P3 was an ungrounded postulate | Valid — major theoretical gap | Resolved (v5) |
| 1.2 | θ cannot be derived from K₃+SSV | Structural impossibility (proved) | Resolved (SM-4 Thm 2) |
| 1.3 | Three-proposition structure not explicit | Valid — clarity | Resolved (v4/v5) |
| 1.4 | Quarks not satisfying Koide unexplained | Valid — completeness | Resolved (v4/v5) |


# PART 2: FAQ — CONVENTIONAL PHYSICS PERSPECTIVE

---

*FAQ content has been moved to FAQ-SM-3.md.*
