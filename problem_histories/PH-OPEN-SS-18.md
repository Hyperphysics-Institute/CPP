# Problem History: OPEN-SS-18 — Heavy-Nuclei Alpha-Cluster Regime for A ≥ 6

**Created:** 17 April 2026 (problem registered)
**Status:** ✓ PARTIALLY RESOLVED — 20 April 2026 (SS-7 v1.1)
**Resolution paper:** SS-7 v1.1 at N_α ∈ [3, 10] for alpha-chain nuclei; remainder split into OPEN-SS-22 (heavy N_α ≥ 12) and OPEN-SS-23 (non-alpha-chain)
**research_frontier.md entry:** OPEN-SS-18 (marked partially resolved)

---

## The Problem

Derive the empirical binding curve for medium-mass nuclei (A ≥ 6) from coupled-alpha-particle cluster structure within the CPP open-vertex framework. SS-5 had just resolved A ≤ 4 via the cascade terminating at ⁴He as the unique closed 3-polytope; no closed polytope exists at A = 5 or A = 8, which correctly predicts those nuclei as structurally unbound. The next question followed immediately: what happens above that threshold, where the empirical binding-per-nucleon curve continues to rise to its peak near ⁵⁶Fe at 8.8 MeV per nucleon?

**What was at stake:** The SS-5 cascade formula does not extend directly beyond A = 4. Without an extension, CPP would have no prediction for any nucleus heavier than ⁴He — a sector containing essentially all of chemistry and astrophysics. A successful extension would take CPP from a theory of the smallest nuclei to a theory of medium-mass nuclei as well, establishing the programme's reach into a regime where conventional nuclear physics has mature empirical descriptions but no first-principles derivations from Standard Model fundamentals.

**What would count as a solution:** A structural account reproducing the empirical binding curve within the CPP residual band, handling (a) alpha-alpha residual binding at scale ~M₀/φ per contact, (b) decreasing per-contact binding with increasing cluster size (saturation), (c) onset of stability valley and peak at A = 56, (d) termination of stability at heavy nuclei.

---

## The Journey

### 17 April 2026 — Problem registered

OPEN-SS-18 was registered in research_frontier.md alongside a preliminary observation from SS-5 v3 §9: the residual binding above cluster sum for small alpha-chain nuclei was approximately `n · M₀/φ` where n ≈ 3 for ¹²C and n ≈ 6 for ¹⁶O. The scaling broke down for heavier nuclei, suggesting the full analysis required its own paper. The slot was tentatively SS-7, following SS-6's then-planned bipyramid-scoping work.

**Initial scope (17 April):** The problem as registered covered the full range A ≥ 6, including odd-A nuclei, neutron-rich isotopes, and heavy-mass nuclei up to the iron peak. This was ambitious — closer in scope to an entire research programme than a single paper.

### 18 April 2026 — Paper slot clarified

The SS-6 slot was reassigned to deuteron-bipyramid observable scoping (addressing OPEN-SS-20 and OPEN-SS-21). The alpha-cluster territory moved firmly to SS-7. Thomas directed the alpha-cluster regime as the natural next paper after SS-6 shipped.

### 19 April 2026 morning — Pattern identified

Numerical exploration of binding-energy residuals above cluster sums for A = 4N_α nuclei produced a clean pattern: the residual n above the sum N_α · B_α matched 3N_α − 6 exactly, for N_α = 3, 4, 5, 6, 7, 8, 9, 10. This is Euler's formula for the edge count of any simplicial convex polytope on N_α vertices. Maximum deviation from B_α + 3N_α − 6 quanta of M₀/φ: 1.4% (²⁸Si).

The identification of the residual with Euler's formula was the conceptual move that converted the problem from "describe a binding curve" to "why does Euler's formula appear in nuclear binding?" The answer: if alphas at vertices of a simplicial polytope each contribute one collective K₃ bonding mode per shared triangular face, and Euler forces the triangular-face count to be 3N_α − 6, the binding formula drops out as a geometric identity.

### 19 April 2026 — v0.1 drafted, first review cycle begun

SS-7 v0.1 shipped at 13 pages, resolving OPEN-SS-18 at N_α ∈ [3, 10] for alpha-chain nuclei (N = Z = 2N_α) with the zero-parameter formula:

> **B(N_α) = N_α · B_α + (3N_α − 6) · B_pair**

using B_α = 28.296 MeV (⁴He from SS-5) and B_pair = M₀/φ = 2.342 MeV (nucleon-pair quantum from SS-5). Eight concurrent predictions (¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca) all matching AME 2020 to within ±1.5%. Zero fitted parameters.

⁸Be at N_α = 2 gave 3N−6 = 0 (no edges). Formula plus Coulomb at R_αα = 2.37 fm (inverted from the observed 92 keV unboundness) correctly reproduced ⁸Be's near-threshold unboundness — previously registered in SS-5 as a qualitative prediction, now derivable in-formula.

Round-1 reviews produced substantial refinements (see reviews-SS-7.md for the full record). ChatGPT's initial review hallucinated its critiques; a correction letter produced a re-engaged re-review contributing the theorem/hypothesis split, selection-bias scope language, R_αα inversion framing, M₀/φ recurrence status, ±2% structural falsification threshold, and the five-nucleus hostile-geometry stress test that became §6.5. Copilot's round-1 contributed assumption-stack expansion, Coulomb treatment, Hoyle expansion, and three figures.

### 20 April 2026 — v1.1 shipped

Round-2 reviews from both ChatGPT and Copilot returned "Accept with minor revisions." Five v1.1 integrations: C4 rephrased as "structural hypothesis within CPP, not yet derived from lattice-level dynamics," edge-count-dominance opening line, physical-intuition paragraph, Figure 4 DP-sea schematic, symbols glossary.

23 pages, clean build, zero errors. Resolution of OPEN-SS-18 at the alpha-chain band finalized.

### Scope split at resolution

OPEN-SS-18's original scope was broader than what SS-7 resolved. At resolution, the problem was split:

- **Resolved portion:** alpha-chain nuclei with N = Z = 2N_α and N_α ∈ [3, 10]. Eight nuclei ¹²C through ⁴⁰Ca.
- **OPEN-SS-22** (new, 19 April 2026): heavy alpha-polytope closure at N_α ≥ 12. Residuals flatten at −2% to −2.5% across ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe — suggesting structural onset (primary candidate: icosahedral closure bonus at exactly 12 alphas) rather than smooth breakdown. Target paper: SS-8.
- **OPEN-SS-23** (new, 19 April 2026): odd-A and non-alpha-chain nuclei. Extension requires handling (i) excess nucleons bound to alpha-polytope core, (ii) partial-alpha substructures (e.g., ⁶Li ≈ ⁴He + d, preliminary residual alpha-deuteron binding ≈ 2B_pair/3), (iii) N ≠ Z isotopes. Target paper: TBD.
- **OPEN-SS-24** (new, 19 April 2026): first-principles CPP derivation of the simplicial contact structure itself (assumption C4 becoming theorem). Target paper: SS-9 candidate.

---

## What Made This Problem Tractable

Three specific features of the alpha-chain sector made zero-parameter resolution possible:

1. **Rigid-tetrahedral alphas at nuclear-binding energy scales.** ⁴He's first excited state at 20.2 MeV is high enough above the per-contact alpha-alpha binding (~2.3 MeV) that alphas at contact see each other as gentle perturbations of rigid internal structure. This justifies treating alphas as vertices of a higher-level polytope rather than as penetrable clouds.

2. **K₃ face mechanism already derived by SS-5.** The collective-mode eigenvalue structure at a triangular contact face, producing one bonding mode at M₀/φ, did not need to be re-derived for SS-7. It was inherited unchanged from SS-5's treatment of nucleon-nucleon contact. The recurrence of the mechanism at the alpha scale required assumption C3 (same geometric object, same eigenvalue structure at larger spatial scale), not new machinery.

3. **Euler's formula as a classical theorem.** Once the alpha-polytope simplicial hypothesis was posited, the edge count `3N_α − 6` dropped out of eighteenth-century geometry with no physics input. This converts the problem from "predict nuclear binding" to "verify empirically that nuclei realize simplicial polytope connectivity" — a much sharper test.

Had any one of these three been absent, the resolution would not have been zero-parameter. The combination is what made the sector tractable ahead of its time.

---

## What This Resolution Does Not Do

The resolution is genuine but scoped. Honest inventory of what remains:

- **R_αα is not derived from first principles.** The alpha-alpha contact distance of 2.37 fm used in ⁸Be Coulomb balance is extracted by inversion from the observed 92 keV unboundness. This is a consistency parameter, not a forward prediction. A CPP derivation of R_αα from lattice geometry is adjacent to OPEN-SS-24 and remains open.

- **C4 is an assumption, not a theorem.** Why alphas realize simplicial polytopes (maximum-connectivity triangulated spheres) rather than lower-connected graphs is empirically supported by the eight concurrent matches plus five hostile-geometry stress tests, but is not derived from CPP primitives. OPEN-SS-24 targets this derivation.

- **DP-sea Coulomb screening mechanism is schematic.** §5.4 of SS-7 v1.1 shows that effective alpha-alpha Coulomb in bound polytopes must be substantially reduced from vacuum value (otherwise predictions would degrade by ~15-20% from Coulomb per-edge subtraction). A scaling argument from conventional-cluster treatments gives the right order of magnitude, but a first-principles CPP derivation of DP-sea screening is OPEN-SS-22-adjacent.

- **Hoyle state energy not predicted quantitatively.** §4.3 gives the geometric interpretation (N_α = 3 dilated triangle), consistent with the conventional alpha-cluster tradition, but the 7.654 MeV excitation energy would require excited-state methods beyond rigid-polytope formalism.

- **Heavy nuclei (N_α ≥ 12) not addressed.** Flat −2% to −2.5% residual pattern across ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe registered as OPEN-SS-22. Resolution target: SS-8.

- **Non-alpha-chain nuclei not addressed.** Registered as OPEN-SS-23. No target paper yet.

---

## Significance for the CPP Programme

OPEN-SS-18's resolution adds eight zero-parameter quantitative predictions to the CPP corpus (PRED-C-42 through PRED-C-49), plus the in-formula re-derivation of ⁸Be unboundness (PRED-C-50). Axiom-to-prediction ratio drops from 0.26 to 0.21.

The resolution also establishes the **cascade paradigm at two levels**: nucleons as primary tetrahedra (SS-5 at A ≤ 4) and alphas as secondary tetrahedra (SS-7 at A = 4N_α). The same M₀/φ binding quantum appears in both contexts — not as fitted coincidence but because the same K₃ geometric structure exists at both spatial scales. Whether this pattern continues to a third level (alpha-polytope clusters combining into still-larger structures) is an open question for heavier nuclei.

For the broader programme, SS-7 demonstrates that the SS-5 machinery is reusable across scales without modification. This strengthens confidence that CPP's derivation of small-nuclei binding is not a local fit but reflects structural mechanism. If the same mechanism correctly predicts eight unrelated medium-mass nuclei using the same two constants, the probability that the agreement is coincidence drops substantially compared to any single-nucleus match.

---

## For Future Work

The natural next papers are SS-8 (OPEN-SS-22, icosahedral closure at N_α = 12) and SS-9 candidate (OPEN-SS-24, first-principles derivation of simplicial contact structure). Both reviewers (ChatGPT and Copilot) explicitly committed to continued engagement on these targets. The SS-18 resolution leaves the programme well-positioned for either target as the next production cycle.

**Diagnostic test for SS-8:** if icosahedral closure is the correct mechanism for the N_α ≥ 12 onset, ⁴⁸Cr specifically (N_α = 12, though not a stable nucleus) should show reduced underbinding compared to ⁴⁸Ti, ⁵²Cr, ⁵⁶Fe. A sharp signature at N_α = 12 would distinguish icosahedral closure from alternative mechanisms (per-alpha Pauli reactivation, face-count correction, deformation onset).

**Conceptual test for SS-9:** the derivation of C4 from lattice geometry should explain not only *that* simplicial connectivity is selected but *why the lattice prefers triangulated sphere topology over alternative closed-polytope topologies*. A derivation that merely re-labels the assumption does not count as resolution.

---

*Problem history closed at partial-resolution threshold. Future SS-8 and SS-9 work will either extend this resolution further (if mechanisms found) or confirm the scope split is final (if OPEN-SS-22 and OPEN-SS-24 prove intractable within current CPP machinery).*
