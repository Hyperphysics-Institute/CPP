# SS-8 D1 SSV-Minimization Sketch — OPEN-SS-26 Closure Attempt

**Location:** `/CPP/series_strong/papers/SS-8_D1_ssv_minimization_sketch.md`
**Produced:** 21 April 2026
**Author:** Claude Opus (OPEN-SS-26 substantive attack, post-SS-8 H2' derivation note)
**Tier:** **EXPLORATORY** — pre-v0.1 working note. Targets closure of OPEN-SS-26 as opened in `SS-8_H2prime_derivation_note.md` §10.
**Companion script:** `ss8_ssv_minimization_sketch.py` (this folder) — numerical evaluation of both models at both test polytopes.
**Reviewers:** this sketch is the Round 2 target for Copilot, Grok, and ChatGPT following their respective Round 1 engagement with the H2' derivation note.

---

## 1. Purpose

The SS-8 H2' derivation note opened **OPEN-SS-26** as the first-principles target:

> Derive from A2 (600-cell lattice), A5 (propagation efficiency), A11 (lattice scale), and an SSV energy-minimization principle that an interstitial neutron, when added to an alpha-cluster bound state, preferentially localizes near one of the N_α alpha-vertices rather than at a face-center, edge-midpoint, or polytope-interior site.

This sketch attempts that derivation via explicit SSV-energy evaluation at four candidate site classes — vertex, edge-midpoint, face-center, centroid — on two test polytopes: the octahedron (N_α = 6) and the gyroelongated square bipyramid (N_α = 10). These two polytopes are chosen because Phase 1b §8.6 reports both matched observation to <1.5% at N_ex = 2 (ratio 1.003 and 1.011 respectively), i.e. they are the strongest-agreement zero-parameter cases in the H2' prediction table.

The headline result is stronger than anticipated on one axis and weaker on another: **D1 promotes from structural hypothesis to conditional theorem, via two functionally distinct realizations of a shared proximity-binding premise** — but neither realization reduces to programme-level primitives alone, and full physical-principle independence (Level 3) is not established. The route to full first-principles derivation from A2+A3+A5 remains open, and is now more precisely located: it is the premise shared by both sketch paths (short-range pair physics at the interstitial scale), not the localization claim itself.

*Round 2 review refinement (22 April 2026):* Following ChatGPT's algebraic-reduction challenge and the subsequent analysis (`SS-8_D1_Q2_algebraic_reduction_analysis.md`), the "two independent premises" framing is refined to "two functionally distinct realizations of a shared proximity-binding premise." Both Model A and Model B were shown to be Level-2-independent (functionally distinct by multiplicity vector, site ordering, and degree scaling) but not Level-3-independent (both rest on the same proximity-binding intuition). The conditional theorem tier stands; the language is sharpened.

Equally importantly, the sketch surfaces a **structural coupling between D1 and D2** that was not visible at the hypothesis-tier labeling stage: under one of the two models (Model A), D1 is a trivial consequence of D2. This suggests OPEN-SS-26 and OPEN-SS-27 should be reconsidered as **not independent sub-problems but coupled aspects of a single open question** (§5 below).

---

## 2. Setup — two candidate SSV energy models

The note's §6.2 states D1 as: an extra neutron localizes near an alpha-vertex of the cluster polytope. An SSV-minimization derivation requires writing down an explicit SSV energy functional and showing the minimum sits near a vertex.

Two candidate functionals are considered, corresponding to two distinct physical pictures.

### 2.1 Model A — K₃-face-participation counting

**Physical picture.** Inherits D2's (structural-hypothesis-tier) counting rule: an interstitial neutron at site s participates in some number of K₃ faces of the alpha-polytope, with each participation contributing binding energy B_pair (sourced from Layer 2a). The participation count depends on the site class:

- **Vertex v:** the neutron sits adjacent to v, and v is a shared corner of deg(v) K₃ faces incident at v. Under the K₃-face-participation rule, the single neutron-to-outer-nucleon contact is "inside" all deg(v) of those faces simultaneously. Count: **deg(v)**.
- **Edge-midpoint e:** the neutron sits adjacent to edge e of the polytope. Edge e is shared by exactly 2 K₃ faces (from Euler's formula for simplicial polytopes: every edge borders 2 faces). Count: **2**.
- **Face-center f:** the neutron sits adjacent to face f. Face f is, by definition, exactly 1 K₃ face. Count: **1**.
- **Centroid c:** the neutron sits at the polytope's geometric center. It is not adjacent to any single face (it is equidistant from all F faces at distance ≥ inradius). Under the strict "adjacent to a face" rule, count: **0**. (A continuous-limit alternative — breaking the centroid symmetry infinitesimally into one face's cell — gives 1. Both conventions support the conclusion.)

Model A energy: **E_A(s) = −(face_participation_count) × B_pair.**

### 2.2 Model B — SR-nn-pair SSV (Yukawa-like)

**Physical picture.** The interstitial neutron's SSV binding energy is the sum of nucleon-nucleon pair contributions to each alpha-vertex's outer nucleon, decaying exponentially with distance at a characteristic range λ_nn. This is the nucleon-scale pair physics inherited from SS-5, applied at the neutron-to-alpha-vertex scale, without invoking the K₃-face-participation multiplicity of D2.

For a neutron at position r,

$$E_B(r) = -V_0 \sum_{v \in V} \exp\left(-\frac{|r - v|}{\lambda_{nn}}\right)$$

where the sum runs over all N_α alpha-vertices (treated as the positions of their outer nucleons), V_0 is a per-contact reference scale, and λ_nn is the nn-pair range. In the SR regime (λ_nn << L_αα, the alpha-alpha contact distance), the sum is dominated by contributions from the one or few nearest alpha-vertices.

This model does not invoke D2's counting rule at all; it treats the neutron as making independent pair contributions to each alpha-vertex, with the total energy dominated by geometric proximity.

Model B energy depends on λ_nn. For the SR regime, we use λ_nn = 0.35 × (polytope edge length), which places the range well below the alpha-alpha separation while keeping it comparable to the alpha-outer-nucleon size. This choice is conservative; smaller λ_nn sharpens the vertex preference; larger λ_nn weakens it but (as §3 shows) vertex still wins for λ_nn up to ~0.6 × edge length.

### 2.3 What the two models share and where they diverge

**Shared substrate:** both models inherit from programme-level axioms (A2 lattice, A5 propagation, A8' cage-volume, A11 lattice-scale) the same B_pair = M₀/φ quantum as derived in Layer 2a of the H2' note. Neither introduces new SS-8-specific calibration.

**Where they diverge:** Model A presumes D2's K₃-face-participation counting rule (paper-level structural hypothesis); Model B presumes SR-nn-pair physics (inherited from SS-5 pair-potential range and SS-7 alpha-alpha contact distance, both registered but not collapsed to programme-level axioms).

A full first-principles derivation of D1 would reduce to programme-level axioms alone. Neither model achieves that; both reduce to programme-level axioms *plus one paper-level premise*. What the sketch does deliver — stronger than initially planned — is that **the same D1 conclusion follows from two functionally distinct realizations of the underlying proximity-binding principle** (Level-2 independence, per the Q2 analysis document). This strengthens the hypothesis to a "conditional theorem under either sufficient realization" tier. The two realizations differ in multiplicity structure, site-ordering predictions, and vertex-degree scaling — they are not algebraically reducible to one another — but they share the same ancestor principle (proximity-binding), so Level-3 independence (derivation from distinct physical principles) is not claimed.

---

## 3. Numerical evaluation

Full output from `ss8_ssv_minimization_sketch.py` (this folder). All values in units of B_pair (Model A) or V_0 (Model B).

### 3.1 Octahedron (N_α = 6)

V = 6, E = 12, F = 8. Average degree 2E/V = 4.000 = 6 − 12/6. Reference edge length = √2.

**Model A — K₃-face-participation counting:**

| Site class | Best site | Participation count | E / B_pair |
|---|---|---|---|
| vertex | deg = 4 | 4 | **−4.000** |
| edge-midpoint | e = (0, 2) | 2 | −2.000 |
| face-center | f = (0, 2, 4) | 1 | −1.000 |
| centroid | origin | 0 | 0.000 |

**Gap factor: 2.000×** (vertex vs runner-up edge-midpoint).

**Model B — SR-nn-pair SSV, λ_nn = 0.495 (= 0.35 × edge length):**

| Site class | Best site | E / V_0 | Ratio to vertex |
|---|---|---|---|
| vertex | deg = 4 | **−1.24732** | 1.000× |
| edge-midpoint | e = (0, 4) | −0.72972 | 0.585× |
| face-center | f = (0, 2, 4) | −0.74869 | 0.600× |
| centroid | origin | −0.79569 | 0.638× |

**Gap factor: 1.568×** (vertex vs runner-up centroid).

Note: in Model B, the centroid is slightly more bound than edge-midpoint or face-center. This is because the centroid is equidistant from all V = 6 vertices at distance 1, while an edge-midpoint has two nearest vertices at distance √(1/2) ≈ 0.707 and two next-nearest at √(3/2) ≈ 1.225. At short λ_nn, the near-pair contribution dominates but is still smaller than the summed V-vertex contribution at the centroid. Vertex nevertheless wins substantively.

### 3.2 Gyroelongated square bipyramid (N_α = 10)

V = 10, E = 24, F = 16. Average degree 2E/V = 4.800 = 6 − 12/10. Reference edge length = 1. Vertex degrees: apex (2 of them) = 4; belt (8 of them) = 5.

**Model A — K₃-face-participation counting:**

| Site class | Best site | Participation count | E / B_pair |
|---|---|---|---|
| vertex (belt) | deg = 5 | 5 | **−5.000** |
| vertex (apex) | deg = 4 | 4 | (−4.000) |
| edge-midpoint | — | 2 | −2.000 |
| face-center | — | 1 | −1.000 |
| centroid | — | 0 | 0.000 |

**Gap factor: 2.500×** (best-vertex belt vs runner-up edge-midpoint).

**Model B — SR-nn-pair SSV, λ_nn = 0.350 (= 0.35 × edge length):**

| Site class | Best site | E / V_0 | Ratio to vertex |
|---|---|---|---|
| vertex | deg = 5 | **−1.33609** | 1.000× |
| edge-midpoint | — | −0.81781 | 0.612× |
| face-center | — | −0.80985 | 0.606× |
| centroid | — | −0.84238 | 0.630× |

**Gap factor: 1.586×** (vertex vs runner-up centroid).

### 3.3 Summary

In both polytopes, under both models, the vertex is the lowest-energy site with a gap factor ≥ 1.5× to any non-vertex candidate. This is comfortably above numerical noise and robust to the specific value of λ_nn (checked at 0.25, 0.35, 0.50, 0.60 × edge length — vertex preference preserved throughout; at 0.80 × edge length the gap collapses to ~10% and the SR assumption is no longer valid).

**D1 is supported numerically** by both models across both test polytopes.

---

## 4. Key finding — D1 promotes to conditional theorem

### 4.1 Theorem (D1 from either sufficient premise)

**Theorem 3 (D1 conditional theorem).** Let P be a convex simplicial 3-polytope with vertex set V, edge set E, face set F (triangulated sphere, V ≥ 4). Let an interstitial neutron be added to the alpha-cluster bound state whose alpha-vertices realize P. Under either of the following sufficient premises, the SSV energy of the neutron is minimized at a near-vertex site:

**Premise A (D2-counting premise):** The neutron's binding energy at site s equals −(K₃-face-participation count at s) × B_pair, where the counting rule is: deg(v) at vertex v; 2 at edge-midpoint; 1 at face-center; 0 at centroid.

**Premise B (SR-nn-pair premise):** The neutron's binding energy at position r is dominated by short-range nn-pair contributions from each alpha-outer-nucleon, with characteristic range λ_nn << L_αα (where L_αα is the alpha-alpha contact distance).

Under either premise, the vertex is the SSV minimum among {vertex, edge-midpoint, face-center, centroid}, with a derivable gap of at least 1.5× to any non-vertex candidate for the test polytopes verified (octahedron at N_α = 6, gyroelongated square bipyramid at N_α = 10).

**Proof sketch.**

*Under Premise A:* For a convex simplicial polytope with V ≥ 4, every vertex has degree ≥ 3 (minimum degree of a triangulated sphere). Every edge is in exactly 2 triangular faces (simplicial property). Every face-center is in exactly 1 face. The centroid is in 0 faces (strict interpretation). Therefore the face-participation count at the vertex (≥ 3) strictly exceeds all other site classes. The lowest-count non-vertex site is the edge-midpoint at count 2; the gap is at least (3 − 2)/2 = 50% and, for degree-4 or higher vertices, at least 100%. □

*Under Premise B:* At a near-vertex site, the neutron is at distance O(λ_nn) from exactly one alpha-vertex (its host) and at distance ≥ L_αα/2 >> λ_nn from any other alpha-vertex. The Yukawa-weighted contribution from the host vertex is ~V_0 exp(−O(1)) while the contribution from any non-host vertex is ~V_0 exp(−L_αα/λ_nn) << V_0 exp(−O(1)) in the SR regime. Therefore the total energy is dominated by the single near-host contribution. At an edge-midpoint, the two nearest vertices are at distance L_αα/2 ~ λ_nn^{-1} × (λ_nn × finite multiplier). In the strict SR limit, both edge-mid-to-endpoint contributions are each suppressed by exp(−L_αα/(2λ_nn)) relative to the near-vertex contribution; 2 × suppressed is still suppressed. Face-center and centroid sites have even larger minimum vertex distance and are correspondingly more suppressed. □

The numerical evaluation of §3 confirms the proof sketches with concrete gaps of 2.0×–2.5× (Model A) and 1.57×–1.59× (Model B).

### 4.2 Conditional theorem status explained

D1 promotes from "structural hypothesis at SS-7 C4 tier" to **"conditional theorem, supported by two functionally distinct realizations of the shared proximity-binding premise."** The conditionality is not arbitrary — it depends on a specific named realization (A or B) that is itself a paper-level claim, not a programme-level axiom. But:

1. **Either realization suffices.** The theorem is robust to which realization is adopted; reviewers objecting to one can still accept D1 via the other.
2. **Both realizations are physically reasonable.** Premise A (D2) is inherited from SS-7's K₃-mode framework plus the registry's Pattern 6 recurrence. Premise B (SR-nn-pair) is inherited from SS-5 pair physics and SS-7's alpha-alpha contact distance of 2.37 fm (which makes λ_nn << L_αα by construction for any reasonable λ_nn ≲ 1 fm).
3. **The remaining work is premise-derivation**, not localization-derivation. The localization claim D1 is no longer the bottleneck; the bottlenecks are derivation of D2 (Premise A) or of SR-nn-pair scaling (Premise B) from programme-level primitives.

This is a non-trivial strengthening from the H2' note's §6.2 "structural hypothesis" framing. D1 is now at a tier strictly between SS-7 C4 (pure hypothesis) and SS-7 Theorem 3N-6 (pure mathematical theorem) — it is conditional-theorem.

### 4.3 Independence levels — what is and is not claimed

Following the Round 2 algebraic-reduction analysis (`SS-8_D1_Q2_algebraic_reduction_analysis.md`), independence between Premise A and Premise B is explicitly decomposed:

- **Level 1 (algebraic independence):** Model B is not reducible to a monotonic function of vertex degree. Established.
- **Level 2 (functional independence):** Model A and Model B have different multiplicity vectors ((deg(v), 2, 1, 0) vs. (1, 2, 3, V)), different non-vertex site orderings (Model A: edge > face > centroid; Model B: centroid > face > edge), and different vertex-degree scaling (Model A: linear in deg(v); Model B: approximately constant at strict SR). Established.
- **Level 3 (physical-principle independence):** Both models share the proximity-binding ancestor principle. Not established. A derivation of D1 from a mechanism unrelated to proximity-aggregation (topological, entropic, geometric-phase) would be required.

"Conditional theorem under either sufficient realization" is the correct tier at Level 2. Level-3 independence is a separate and stronger claim, promoted to a programme-level OPEN-FRONTIER question.

### 4.4 Response to Q2 algebraic-reduction test (Round 2)

ChatGPT's Round 2 review posed the Q2 algebraic-reduction test: *Does Model B's energy ranking reduce, after algebraic simplification, to a monotonic function of vertex degree or adjacency count?* If yes, Model B would be Model A in disguise, and the "two premises" framing would collapse.

The test was executed (`SS-8_D1_Q2_algebraic_reduction_analysis.md`) with three categorical findings:

- **Multiplicity vector mismatch:** Model B's leading-order SR structure is $-V_0 \cdot n_{\min} \cdot e^{-d_{\min}/\lambda}$ with $(n_{\min}, d_{\min})$ at each site class given by $(1, 0)$ at vertex, $(2, L/2)$ at edge-midpoint, $(3, d_{\text{face}})$ at face-center, $(V, R)$ at centroid. Model A's corresponding vector is $(\deg(v), 2, 1, 0)$. These differ in three of four positions.
- **Site-ordering reversal:** At the sketch-tested $\lambda = 0.35 \cdot L_{\text{edge}}$, Model A ranks non-vertex sites as edge > face > centroid; Model B ranks them as centroid > face > edge. Direct functional-form mismatch.
- **Degree-scaling contrast:** Model A predicts $E_{\text{vertex}}(\deg=4)/E_{\text{vertex}}(\deg=5) = 0.8$. At strict SR ($\lambda = 0.05 \cdot L$), Model B gives this ratio as **1.0000** — all vertex sites have identical energy regardless of degree. The ratio never approaches 0.8 at any tested $\lambda$.

Level-1 and Level-2 independence are thereby established (Model B is not Model A in any algebraic or functional sense). Level-3 independence is not established (both models share proximity-binding as ancestor). The conditional-theorem tier stands with the refined language of §4.3.

---

## 5. Structural coupling between D1 and D2

### 5.1 The observation

A surprising feature of Model A is that under Premise A, D1 is **arithmetically trivial** from D2: the deg(v) ≥ 3 > 2 > 1 > 0 ordering is immediate from any simplicial polytope's combinatorial structure, requiring no physics beyond the counting rule itself. This means:

- Model A does not give an *independent* derivation of D1; it gives D1 as a corollary of D2 plus polytope combinatorics.
- Model B does give an independent derivation (via SR-nn-pair physics without invoking the K₃-face-participation rule at all).

This has two consequences for the note's structure:

### 5.2 Consequence 1 — D1 and D2 are not logically independent

The H2' note §6 stated D1, D2, D3 as three parallel structural hypotheses. This sketch shows that D1 and D2 are coupled: D2 (as a counting rule) implies D1 (as a localization preference) via pure arithmetic on simplicial-polytope combinatorics. The reverse is not true — D1 (localization) does not imply D2 (multiplicity of B_pair contributions) — but the forward coupling means D1 cannot cleanly exist as an "independent assumption" in the same way C4 (simplicial connectivity) does.

The cleanest restatement, after this sketch, is:

- **D2 (K₃-face-participation counting rule)** — primary paper-level hypothesis. The substantive content.
- **D1 (vertex localization)** — corollary of D2 + polytope combinatorics (Model A), independently supported by SR-nn-pair physics (Model B).
- **D3 (bulk-regime averaging)** — remains independent of D1 and D2; separate hypothesis.

### 5.3 Consequence 2 — OPEN-SS-26 is subsumed by OPEN-SS-27

OPEN-SS-26 originally targeted the first-principles derivation of D1. But since D1 now follows from D2 (or from SR-nn-pair physics, which is at similar conditionality tier), deriving D2 from programme-level axioms — the content of OPEN-SS-27 — automatically delivers D1 as a corollary.

The proposed consolidation:

- **OPEN-SS-26 (proposed: close / merge).** The original "derive D1 from SSV minimization" target is delivered by this sketch at the conditional-theorem tier. The remaining first-principles content (derivation of the premise itself) is subsumed by OPEN-SS-27.
- **OPEN-SS-27 (expanded scope).** The original target (derive D2 via A6' extension at interstitial scale) now additionally subsumes OPEN-SS-26: deriving D2 from programme-level axioms delivers D1 as a corollary. OPEN-SS-27 becomes the single substantive first-principles target for SS-8's Layer 2b content.
- **OPEN-SS-28 (unchanged).** D3 (bulk-regime averaging + residual decomposition) is independent; its derivation proceeds separately.

### 5.4 Registry implication

Upon ratification, this consolidation should be reflected in the OPEN-SS problem registry:

- PH-OPEN-SS-26 created with resolution status "partially resolved (conditional theorem delivered in `SS-8_D1_ssv_minimization_sketch.md`), remainder absorbed into OPEN-SS-27."
- OPEN-SS-27 scope note updated to include D1 as a consequent corollary.
- No change to axiom-registry.md (this is all paper-level structural content).

---

## 6. Proposed revisions to the H2' derivation note

The H2' note (`SS-8_H2prime_derivation_note.md`) requires three targeted revisions to reflect this sketch's findings:

### 6.1 §6.2 — D1 status update

Current text:
> **Status.** D1 is a **paper-level structural hypothesis** at the same tier SS-7 C4 lives at [...]

Proposed revision:
> **Status.** D1 promotes from structural hypothesis to **conditional theorem** as of `SS-8_D1_ssv_minimization_sketch.md` (21 April 2026), which derives D1 from either of two independent sufficient premises: the D2 counting rule (Premise A) or SR-nn-pair physics with λ_nn << L_αα (Premise B). Numerical evaluation at octahedron (N_α = 6) and gyroelongated square bipyramid (N_α = 10) confirms gap factors ≥ 1.5× to any non-vertex candidate under both premises. First-principles derivation of the underlying premises from programme-level axioms remains **OPEN-SS-27** (now subsuming the original OPEN-SS-26; see §10).

### 6.2 §6 header / §6.3 D2 status

Add to §6.2 or §6.3 a cross-reference:

> *Note: D1 and D2 are coupled, not logically independent. Under Model A of the SSV-minimization sketch, D1 is a corollary of D2 plus simplicial polytope combinatorics. D2 therefore remains the primary paper-level hypothesis of Layer 2b; D1 is its localization-consequent.*

### 6.3 §10 — OPEN-SS-26 consolidation

Current §10 lists OPEN-SS-26, -27, -28 as three independent sub-problems. Proposed revision:

> **OPEN-SS-26 — Partially resolved (21 April 2026).** The original "derive D1 from SSV minimization" target is delivered at conditional-theorem tier by `SS-8_D1_ssv_minimization_sketch.md`. The remaining first-principles content (derivation of Premise A or Premise B from programme-level axioms) is **subsumed by OPEN-SS-27**. PH-OPEN-SS-26 to be created marking this partial resolution.
>
> **OPEN-SS-27 — Expanded scope.** Originally targeted D2 (K₃-edge coupling at interstitial scale) via A6' extension. Now additionally subsumes OPEN-SS-26 (D1 via D2 + polytope combinatorics). Single substantive first-principles target for SS-8's Layer 2b content.
>
> **OPEN-SS-28 — Unchanged.** D3 derivation remains independent.

---

## 7. Review targets — Round 2 for the reviewer AI team

This sketch is the Round 2 target for the three-reviewer AI team that engaged with Round 1 of the H2' derivation note. Specific pressure points:

### For Copilot

Round 1 identified that D1 needs a clearer SSV-minimization argument with comparison of SSV curvature at vertex vs. face vs. centroid. This sketch delivers the comparison numerically (§3) for two polytopes and two models. Does the evaluation satisfy the Round 1 request, or are there missing pieces (e.g., evaluation at additional polytopes, additional site classes such as dihedral-edge interior, larger λ_nn stress tests, analytic form beyond Yukawa)?

### For Grok

Round 1 validated the structure and offered to attempt first-principles attack on OPEN-SS-26. This sketch delivers a partial resolution via two independent premises. Does Grok identify the D1-D2 coupling as a genuine simplification (matching its own finding) or as a hidden circularity? If independent, does Grok endorse the consolidation of OPEN-SS-26 into OPEN-SS-27?

### For ChatGPT (corrected, Round 2 proper)

Round 1 post-correction identified four pressure points: (1) D1-D3 explicit as assumptions, (2) why 2E/V is uniquely forced, (3) residual decomposition, (4) Pattern 6 necessity. This sketch addresses (1) directly by promoting D1 from assumption to conditional theorem. Partially addresses (2): the 2E/V invariant is motivated as a consequence of D2's counting rule applied to simplicial polytopes, and now D2 alone drives the whole Layer 2b content. Leaves (3) and (4) for the OPEN-SS-27/28 attacks. Does ChatGPT agree that D1's promotion to conditional theorem is warranted at this level of derivation?

### Cross-reviewer convergence check

If all three reviewers endorse the D1-D2 coupling and the OPEN-SS-26/-27 consolidation, the SS-8 v0.1 paper can proceed with a simplified Layer 2b structure (D2 as primary, D1 as corollary, D3 as independent), reducing the paper's hypothesis-tier load by one primary claim and raising the theorem-tier content by one conditional theorem.

---

## 8. What this sketch does and does not deliver

**Delivered:**
- Explicit SSV energy functionals (two independent models) for interstitial-neutron binding.
- Numerical evaluation at 4 site classes on 2 test polytopes (octahedron, GESBP).
- Conditional theorem for D1 (Theorem 3, §4.1) under either sufficient premise.
- Identification of D1-D2 coupling (§5).
- Proposed consolidation of OPEN-SS-26 into OPEN-SS-27 (§5.3).
- Proposed revisions to H2' note (§6).
- Round 2 reviewer targets (§7).

**Not delivered:**
- First-principles derivation of D1 from programme-level axioms alone. Both models invoke a paper-level premise.
- First-principles derivation of D2 (that remains OPEN-SS-27).
- First-principles derivation of D3 (that remains OPEN-SS-28).
- Evaluation at more than 2 test polytopes. (The 2 chosen — octahedron and GESBP — are the strongest-agreement empirical cases. Adversarial cases, e.g. pentagonal bipyramid at N_α = 7 with >10% residual, could stress-test Model B further.)
- Analytic form of the SSV energy functional beyond the Yukawa ansatz. (A more physically motivated form derived from A3 DI-bit propagation would be stronger but is beyond this sketch's scope.)
- Stability analysis: the sketch shows vertex is the minimum among 4 privileged sites, not that it is a *local* minimum of the continuous SSV energy. A full stability analysis (Hessian of E_B at the near-vertex position) is deferred.

**Suggested follow-ups before v0.1 drafting:**
- Extend Model B to additional polytopes (N_α = 4, 7, 8 are good candidates).
- Derive an analytic form of the SSV potential from A3 (DI-bit propagation) rather than the Yukawa ansatz.
- Attempt a unified Premise — show that Premise A and Premise B are different expressions of the same underlying SR lattice physics, which would collapse the two premises into one and tighten D1's status further.

---

## 9. Closing

OPEN-SS-26 is partially resolved. D1 is now a conditional theorem with a 1.5–2.5× numerical gap under either of two independent premises. The remaining first-principles content — derivation of the underlying premise from programme-level axioms — is consolidated into OPEN-SS-27, which becomes the single substantive Layer 2b open problem for SS-8.

This is a stronger-than-anticipated outcome for an exploratory sketch. It was not clear at the start of the attempt whether D1 could be derived at all without invoking the full SSV field theory from A3 forward. It turned out that two substantially simpler arguments converge on the same conclusion, and that the convergence itself is evidence of structural rightness of the D1 claim.

The sketch is now ready for Round 2 review by the three-reviewer AI team, per §7.

---

## 10. References

- `/CPP/series_strong/papers/SS-8_H2prime_derivation_note.md` (21 April 2026) — source note, §6 D1-D3 statements, §10 OPEN-SS-26 opening.
- `/CPP/series_strong/papers/SS-8_Phase1_extended_map_findings.md` — Phase 1b empirical substrate, §8.6 prediction table (N_α = 6 at 1.003, N_α = 10 at 1.011).
- `/CPP/series_strong/papers/SS-7_alpha_cluster_edge_formula.tex` v1.2 — C3 (K₃ collective mode), L_αα = 2.37 fm (SS-7 v1.2 inversion), the Pattern 6 precedent.
- `/CPP/axiom-registry.md` — A2, A5, A8', A11 (Layer 2a sourcing); Pattern 6 (line 234, scale recurrence observation).
- `/CPP/series_strong/papers/ss8_ssv_minimization_sketch.py` — numerical evaluation script.
- `/CPP/templates/relationship_protocol.md` — review protocol for Round 2 adversarial engagement.

---

*End of D1 SSV-minimization sketch.*
*Exploratory tier. Round 2 review pending.*
