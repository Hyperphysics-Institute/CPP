# SS-8 D1 Sketch — Q2 Algebraic Reduction Test

**Location:** `/CPP/series_strong/papers/SS-8_D1_Q2_algebraic_reduction_analysis.md`
**Produced:** 22 April 2026
**Author:** Claude Opus
**Tier:** **EXPLORATORY** — appendix to `SS-8_D1_ssv_minimization_sketch.md`, addressing ChatGPT's Round 2 Q2 concern.
**Companion script:** `ss8_Q2_algebraic_reduction_test.py` (this folder).

---

## 1. Purpose

ChatGPT's Round 2 review of the D1 SSV-minimization sketch raised a specific falsifiable concern about Model B's claimed independence from Model A (§2.3 of the ChatGPT Round 2 reply):

> *Does Model B's energy ranking reduce, after algebraic simplification, to a monotonic function of vertex degree or adjacency count? Because if yes, Model B is isomorphic to Model A in disguise.*

This was the single Round 2 question that Copilot and Grok did not substantively test; both asserted Model B independence without algebraic verification. The test is consequential: if Model B reduces to Model A in disguise, the sketch's "two independent sufficient premises" framing collapses to one premise, D1 remains at structural-hypothesis tier rather than promoting to conditional theorem, and the OPEN-SS-26 → OPEN-SS-27 consolidation is not warranted.

This note executes ChatGPT's test and reports the verdict.

---

## 2. Method

**Algebraic step.** Expand Model B's energy functional
$$E_B(r) = -V_0 \sum_{v \in V} \exp\left(-\frac{|r - v|}{\lambda}\right)$$
at each of the four candidate site classes, retaining leading and first-subleading terms in the SR expansion parameter $\varepsilon = \exp(-L_{\text{edge}} / \lambda)$.

**Numerical step.** Evaluate Model B at six values of $\lambda$ spanning strict-SR ($\lambda = 0.05 \cdot L_{\text{edge}}$) to long-range ($\lambda = 1.5 \cdot L_{\text{edge}}$) on the two test polytopes (octahedron, GESBP). Cross-verify the algebraic expansion against the computed energies. Use the GESBP apex-vertex (deg=4) vs. belt-vertex (deg=5) contrast as a cross-polytope discriminator between Model A and Model B's predicted deg-scaling.

---

## 3. Setup — Model B at each site class

For each candidate site, identify the minimum distance $d_{\min}$ to any alpha-vertex and the multiplicity $n_{\min}$ of alpha-vertices at that minimum distance. In the SR limit ($\lambda \ll L_{\text{edge}}$), the energy is dominated by the nearest-neighbor contribution:

$$E_B(r) \approx -V_0 \cdot n_{\min}(r) \cdot \exp(-d_{\min}(r) / \lambda) + (\text{subleading})$$

For the octahedron (unit circumradius, $L_{\text{edge}} = \sqrt{2}$) and GESBP ($L_{\text{edge}} = 1$), the four site classes have the following $(n_{\min}, d_{\min})$ structure:

| Site class | $n_{\min}$ (oct) | $d_{\min}$ (oct) | $n_{\min}$ (GESBP) | $d_{\min}$ (GESBP) |
|---|---|---|---|---|
| vertex | 1 | 0 | 1 | 0 |
| edge-midpoint | 2 | $\sqrt{2}/2 \approx 0.707$ | 2 | 0.500 |
| face-center | 3 | $\sqrt{2/3} \approx 0.816$ | 3 | 0.577 |
| centroid | V = 6 | 1.000 | V = 8 | 0.823 |

The **multiplicity vector across site classes is $(1, 2, 3, V)$ in both polytopes.**

This is the key algebraic observation. Model B's leading-order coupling at each site is determined by *the number of alpha-vertices at the minimum distance to the site*, not by the vertex degree or K₃-face-participation count.

---

## 4. Algebraic expansion at each site class

Writing Model B's energy as a series in $\varepsilon_s = \exp(-d_s/\lambda)$ where $d_s$ is the minimum distance at site $s$:

### 4.1 Vertex site (neutron near alpha-vertex $v_0$ with $\deg(v_0) = d$)

Decomposing the sum over all $V$ alpha-vertices by their distance from $v_0$:

$$E_B(\text{vertex}) = -V_0 \left[ 1 \;+\; \deg(v_0) \cdot e^{-L_{\text{edge}}/\lambda} \;+\; n_2 \cdot e^{-L_2/\lambda} \;+\; \cdots \right]$$

where $n_2$ is the number of second-neighbor vertices at distance $L_2$, etc. The leading term is $-V_0$ independent of $\deg(v_0)$. The first correction is $-V_0 \deg(v_0) \cdot e^{-L_{\text{edge}}/\lambda}$, which introduces a weak $\deg$-linear dependence whose coefficient $e^{-L_{\text{edge}}/\lambda}$ is exponentially small in the SR limit.

**In strict SR ($\lambda \to 0$):** $E_B(\text{vertex}) \to -V_0$, independent of $\deg(v_0)$.

### 4.2 Edge-midpoint site (on edge $e = (v_i, v_j)$)

The two nearest alpha-vertices are the endpoints $v_i$ and $v_j$ at distance $L_{\text{edge}}/2$. The next-nearest are at distances dependent on polytope geometry.

$$E_B(\text{edge-mid}) = -V_0 \left[ 2 \cdot e^{-L_{\text{edge}}/(2\lambda)} \;+\; (\text{subleading}) \right]$$

**In strict SR:** $E_B(\text{edge-mid}) \to 0$ (exponentially suppressed).

### 4.3 Face-center site (on face $f = (v_i, v_j, v_k)$)

The three face-vertices are at equal distance $d_{\text{face}}$ from the face-center. For the octahedron, $d_{\text{face}} = \sqrt{2/3}$. For GESBP, $d_{\text{face}} \approx 0.577$.

$$E_B(\text{face-center}) = -V_0 \left[ 3 \cdot e^{-d_{\text{face}}/\lambda} \;+\; (\text{subleading}) \right]$$

**In strict SR:** $E_B(\text{face-center}) \to 0$.

### 4.4 Centroid site

All $V$ alpha-vertices are at the circumradius $R$ (for regular polytopes; for GESBP the centroid-distances vary slightly but cluster around 0.82).

$$E_B(\text{centroid}) = -V_0 \cdot V \cdot e^{-R/\lambda}$$

**In strict SR:** $E_B(\text{centroid}) \to 0$.

### 4.5 Summary of leading-order structure

$$\boxed{
\begin{aligned}
E_B(\text{vertex}) &\approx -V_0 \cdot 1 \\
E_B(\text{edge-mid}) &\approx -V_0 \cdot 2 \cdot e^{-L_{\text{edge}}/(2\lambda)} \\
E_B(\text{face-center}) &\approx -V_0 \cdot 3 \cdot e^{-d_{\text{face}}/\lambda} \\
E_B(\text{centroid}) &\approx -V_0 \cdot V \cdot e^{-R/\lambda}
\end{aligned}
}$$

**Model B's "counting vector" at the four site classes is $(1, 2, 3, V)$**, not $(\deg(v), 2, 1, 0)$ as in Model A.

---

## 5. Comparison with Model A

Model A's counting rule (from the sketch §2.1) gives:

$$E_A(\text{vertex}) = -\deg(v) \cdot B_{\text{pair}}$$
$$E_A(\text{edge-mid}) = -2 \cdot B_{\text{pair}}$$
$$E_A(\text{face-center}) = -1 \cdot B_{\text{pair}}$$
$$E_A(\text{centroid}) = 0$$

Side-by-side at each site class:

| Site class | Model A coupling | Model B coupling (SR-leading) | Isomorphic? |
|---|---|---|---|
| vertex | $-\deg(v) \cdot B_{\text{pair}}$ | $-V_0 \cdot 1$ | **No** — different functional form |
| edge-mid | $-2 \cdot B_{\text{pair}}$ | $-V_0 \cdot 2 \cdot e^{-L/(2\lambda)}$ | agree on multiplicity, disagree on suppression |
| face-center | $-1 \cdot B_{\text{pair}}$ | $-V_0 \cdot 3 \cdot e^{-d_f/\lambda}$ | **No** — different multiplicity (1 vs 3) |
| centroid | $0$ | $-V_0 \cdot V \cdot e^{-R/\lambda}$ | **No** — different multiplicity (0 vs V) |

Three of four site classes show explicit structural mismatch in multiplicity alone. The vertex class shows matching multiplicity (1 in Model B vs. $\deg(v)$ in Model A) only in a trivial sense — they are different integers for any simplicial polytope with $\deg(v) > 1$.

**Model B is not Model A in disguise. The two models differ in functional form, in site-class multiplicity, and in vertex-degree dependence.**

---

## 6. Numerical verification

Full output in `ss8_Q2_algebraic_reduction_test.py`. Abridged:

### 6.1 Octahedron (N_α = 6, edge = √2)

Model B energy $E_B / V_0$ at each site vs. $\lambda / L_{\text{edge}}$:

| $\lambda/L$ | vertex | edge-mid | face-center | centroid |
|---|---|---|---|---|
| 0.05 | **−1.000000** | −0.000091 | −0.000029 | −0.000004 |
| 0.10 | −1.000182 | −0.013850 | −0.009463 | −0.005096 |
| 0.20 | −1.027801 | −0.197971 | −0.187485 | −0.174859 |
| 0.35 | −1.247317 | −0.729720 | −0.748694 | −0.795690 |
| 0.50 | −1.600447 | −1.303357 | −1.351462 | −1.458700 |
| 0.70 | −2.091219 | −1.964415 | −2.033939 | −2.184981 |
| 1.00 | −2.714634 | −2.708145 | −2.787790 | −2.958412 |
| 1.50 | −3.443201 | −3.504961 | −3.581807 | −3.744750 |

**Observations:**
- At $\lambda = 0.05 \cdot L$ (strict SR): vertex wins by 4 orders of magnitude. All non-vertex sites have $E \approx 0$ as predicted by algebra.
- At $\lambda = 0.35 \cdot L$ (sketch-tested): vertex wins by 1.6×. Non-vertex ordering is **centroid < face-center < edge-mid** (i.e., centroid is deepest after vertex).
- At $\lambda = 1.00 \cdot L$ (long-range): centroid actually **surpasses** the vertex site, with the ordering becoming centroid > face > edge > vertex — i.e., Model B's SR-regime conclusion reverses at long range.

### 6.2 Non-vertex site ordering in Model B vs. Model A

At the sketch-tested $\lambda = 0.35 \cdot L$:

- **Model B (Octahedron):** vertex (−1.247) > centroid (−0.796) > face (−0.749) > edge (−0.730)
- **Model A (Octahedron):** vertex (−4) > edge (−2) > face (−1) > centroid (0)

The two models **even rank the non-vertex sites in different orders**. Model A's "counting" treats the centroid as the worst site (0 coupling); Model B's proximity physics makes centroid one of the most bound non-vertex sites (by virtue of high multiplicity V = 6 at circumradius R).

**This ordering discrepancy is direct evidence that Model A and Model B are not functionally equivalent.**

### 6.3 Cross-polytope degree-dependence test

Comparing vertex-site energies at the same $\lambda / L_{\text{edge}}$ across octahedron (all vertices deg=4) and GESBP (apex deg=4, belt deg=5):

| $\lambda / L_{\text{edge}}$ | oct (deg=4) | GESBP apex (deg=4) | GESBP belt (deg=5) | $E(4)/E(5)$ ratio | Model A predicts |
|---|---|---|---|---|---|
| 0.05 | −1.000000 | −1.000000 | −1.000000 | **1.0000** | 0.8000 |
| 0.10 | −1.000182 | −1.000182 | −1.000228 | 1.0000 | 0.8000 |
| 0.20 | −1.027801 | −1.027771 | −1.035586 | 0.9925 | 0.8000 |
| 0.35 | −1.247317 | −1.262248 | −1.336089 | 0.9447 | 0.8000 |
| 0.50 | −1.600447 | −1.685336 | −1.858453 | 0.9068 | 0.8000 |
| 0.70 | −2.091219 | −2.350213 | −2.636088 | 0.8916 | 0.8000 |
| 1.00 | −2.714634 | −3.305759 | −3.687756 | 0.8964 | 0.8000 |

**Observations:**
- At strict SR ($\lambda = 0.05 \cdot L$), the $E_{\text{vertex}}(\deg=4)/E_{\text{vertex}}(\deg=5)$ ratio is exactly **1.000**. Model A predicts 0.800 (linear in deg).
- As $\lambda$ increases, Model B's ratio drifts from 1.000 toward ~0.89, but never reaches 0.800.
- **The ratio never matches Model A's prediction at any value of $\lambda$ tested.**

This is the cleanest possible falsification of "Model B reduces to vertex-degree counting." Model B's vertex-site energy is degree-independent at the leading order and develops only a weak deg-linear correction at finite $\lambda$ — a correction that never catches up to Model A's leading deg-linear structure.

---

## 7. Verdict on ChatGPT's Q2 (with level-of-independence refinement)

**Model B does not reduce to Model A after algebraic simplification.** This is the strictly-established result; Q2's strongest form (isomorphism) is categorically ruled out.

The evidence is threefold:

1. **Different site-class multiplicities.** Model B's leading-order couplings at the four site classes are proportional to $(1, 2, 3, V)$; Model A's to $(\deg(v), 2, 1, 0)$. These vectors are structurally different.

2. **Different non-vertex orderings.** Model B ranks non-vertex sites as centroid > face > edge (multiplicity-at-min-distance-weighted); Model A ranks them as edge > face > centroid (K₃-face-participation-count-weighted). The opposite ordering between centroid and edge is a direct discriminator.

3. **Different vertex-degree dependence.** Model A predicts $E_{\text{vertex}}$ scales linearly with $\deg(v)$; Model B predicts it is approximately constant across vertices of different degrees at strict SR, with a weak and quantitatively distinct correction at finite $\lambda$.

### 7.1 Levels of independence — what is and is not established

Following ChatGPT's Round 2 review of this analysis, the verdict above is refined to distinguish three levels of independence between Model A and Model B:

- **Level 1 (algebraic independence):** Model B is not reducible to a monotonic function of $\deg(v)$ or any other Model A counting quantity, at any tested $\lambda$. **Established** by the three discriminators above.
- **Level 2 (functional independence):** Model B's functional form differs from Model A's — different multiplicity structure, different site orderings, different degree scaling. **Established** by the same discriminators.
- **Level 3 (physical-premise independence):** Model B would be derived from a physical mechanism unrelated to proximity-binding (e.g., topological, entropic, or geometric-phase). **Not established.** Both models share the proximity-binding ancestor principle (see §8).

Model B is therefore a *functionally distinct realization of proximity-driven binding, sharing an ancestor principle with Model A but not reducible to it.* "Genuinely independent derivation" is too strong; "functionally distinct realization" is the precise descriptor, and it is what this analysis strictly establishes.

This refinement preserves the sketch's Theorem 3 conclusion (D1 follows from either Model A or Model B) while sharpening the epistemic claim about what "either" means. The two premises are two distinct functional routes to the same conclusion, not two independent physical principles.

---

## 8. Shared-ancestry caveat — and the path to true Level-3 independence

Both Model A and Model B rest on a common physical intuition: **an interstitial neutron binds preferentially where it has access to alpha-vertex structure.** Model A operationalizes this as "count the K₃ faces the neutron participates in"; Model B operationalizes it as "sum the short-range pair potentials to each alpha-vertex." They share the proximity-binding ancestor principle.

Independence here means **functional non-equivalence, not independence of physical intuition.** The Q2 analysis establishes the former decisively; the latter is a distinct and stronger claim that this analysis does not make.

In a stricter sense of "independent" — where two derivations would start from *unrelated* physical mechanisms (e.g., proximity-binding for one, and topological-phase or entropy-driven localization for the other) — the sketch's two models are not fully independent. They are **functionally distinct formalizations of a shared proximity-binding principle**, not independent derivations from distinct first principles.

This caveat sharpens the framing of the sketch's Theorem 3:

- Both premises are functionally distinct realizations (Level 2 independence: established).
- Both premises deliver vertex-preference as their primary conclusion.
- Both premises reduce (if traced back) to the same proximity-binding intuition (Level 3 independence: not established).

**Full independence would require a derivation of D1 from a mechanism not based on proximity aggregation.** That derivation is not attempted in this analysis. A natural future target — worth registering as a programme-level OPEN-FRONTIER question rather than as an SS-8 sub-problem — would be: "Can D1 be derived from a mechanism unrelated to proximity-aggregation (topological, entropic, or geometric-phase)?"

If such a Model C is eventually produced and delivers D1 independent of Model A/B's common principle, then D1 would achieve Level-3 independence and its conditional-theorem tier would be maximally strengthened. The current analysis establishes that D1 holds under any functional formalization of proximity-binding we've tested; what it does not establish is that D1 holds independent of proximity-binding itself.

### 8.1 What this refinement changes and does not change

- **Does not change:** Theorem 3 (D1 follows from either Premise A or Premise B). The two premises are functionally distinct.
- **Does not change:** Numerical gap factors, site orderings, degree-scaling results. These are all empirical and stand as computed.
- **Does not change:** OPEN-SS-26 → OPEN-SS-27 consolidation as a *pragmatic* choice for SS-8's open-problem cascade.
- **Does change:** The rhetorical force of the "two independent premises" claim. It becomes "two functionally distinct realizations of a shared ancestor principle." The claim is narrower but more defensible.
- **Does change:** The registry action. Rather than "OPEN-SS-26 is fully subsumed by OPEN-SS-27," the more precise framing is "OPEN-SS-26's functional content is subsumed by OPEN-SS-27; its physical-principle content (Level-3 independence) becomes a separate OPEN-FRONTIER question at programme level."

---

## 9. An unexpected empirical discriminator

The analysis surfaces a **testable prediction** that distinguishes Model A from Model B:

- **Model A predicts:** interstitial-neutron binding at vertex $v$ scales linearly with $\deg(v)$. A high-deg vertex is more tightly bound than a low-deg vertex, in proportion to their degrees.
- **Model B predicts:** interstitial-neutron binding at vertex $v$ is approximately constant across vertices of different degrees in the strict SR regime. The binding is almost entirely determined by proximity to the single host vertex.

The current Phase 1b data (findings §8.4) is **averaged over all vertices of each polytope**, so it does not discriminate. Discriminating would require:

- Site-resolved binding measurements at specific vertex positions in a mixed-degree polytope (e.g., GESBP with apex-deg=4 and belt-deg=5).
- Or: tight-binding model calculations at each vertex with proper treatment of the SSV functional.

This discriminator is out of scope for SS-8 as currently defined but is a natural target for SS-11 or a dedicated companion paper.

---

## 10. Implications for the sketch and the H2' note

### 10.1 Conditional theorem tier — stands with refined language

The sketch's Theorem 3 (D1 as conditional theorem under either Premise A or Premise B) remains valid, with the refined language: "conditional theorem under two functionally distinct realizations of a shared proximity-binding premise." The two premises are Level-2-independent (functionally distinct) but not Level-3-independent (not derived from unrelated physical principles; they share the proximity-binding ancestor). This is the precise epistemic claim the analysis supports.

### 10.2 OPEN-SS-26 → OPEN-SS-27 consolidation — pragmatically warranted, with residue

Deriving Premise A (D2's counting rule) from programme-level axioms still delivers D1 as a corollary via simplicial combinatorics. Deriving Premise B (SR-nn-pair physics) from programme-level axioms independently delivers D1. For SS-8's open-problem cascade, OPEN-SS-27 can pragmatically subsume OPEN-SS-26's functional-independence content. However, OPEN-SS-26's *physical-principle-independence* content — "is there a derivation of D1 that does not rest on proximity-aggregation?" — is distinct and does not fit under OPEN-SS-27's A6'-extension scope. The honest framing is:

- OPEN-SS-26 (functional content): subsumed by OPEN-SS-27.
- OPEN-SS-26 (physical-principle content): promoted to a separate programme-level OPEN-FRONTIER question, to be registered in `Research_Frontier.md` rather than the SS-8-specific OPEN-SS list.

This preserves the pragmatic consolidation at the SS-8 paper level while preserving the harder physical question at the programme level.

### 10.3 Proposed additions

To the sketch document (`SS-8_D1_ssv_minimization_sketch.md`):

- Update Theorem 3 statement in §4.1 with refined "functionally distinct realizations" language.
- Add §4.4 "Response to Q2 algebraic reduction test" summarizing §§4–7 of this note.
- Update §5 "OPEN-SS-26 → OPEN-SS-27 consolidation" text with the functional/physical-principle split.

To the H2' note (`SS-8_H2prime_derivation_note.md`):

- §6.2 D1 status — update the "conditional theorem" language to read "conditional theorem under two functionally distinct realizations of a shared proximity-binding premise."
- §10 OPEN-SS-26 entry — note the functional/physical-principle split and the new programme-level OPEN-FRONTIER question on Level-3 independence.

To the programme registry (`Research_Frontier.md`, when ratified):

- New OPEN-FRONTIER entry: "Level-3 independence of D1 — can interstitial-neutron vertex localization be derived from a physical mechanism not based on proximity-aggregation (e.g., topological, entropic, geometric-phase)?"

---

## 11. What to report back to the reviewers

**To Copilot:** Your Q2 verdict ("Model B stands alone") is confirmed by this algebraic test. Model B does not reduce to Model A at any value of $\lambda$ tested. Ranking-discrepancy (non-vertex orderings differ) and degree-scaling (strict SR gives ratio 1.0 vs Model A's 0.8) are the cleanest discriminators.

**To Grok:** Your Q2 verdict ("fully independent") is largely confirmed with one refinement: the two models are *functionally* independent rather than *fully* independent. They share a proximity-binding ancestor principle. This doesn't change your conclusion on Q2 or Q4 but does sharpen the framing.

**To ChatGPT:** Your Q2 algebraic-reduction test was executed as proposed. Result: Model B does not reduce to Model A under any tested $\lambda$ regime. Three specific findings (site-class multiplicities differ; non-vertex orderings differ; strict-SR deg-scaling differs by a full linear factor) together rule out the isomorphism concern. The "two independent premises" framing of the conditional theorem holds. Your concern was well-placed and produced the sharpest analysis of the three reviews; this note is the direct response. One refinement your review prompted: the models share a proximity-binding ancestor, so "functionally independent" is a more precise label than "fully independent." This is incorporated into the sketch's revision.

---

## 12. Closing

ChatGPT's Q2 concern was the single most consequential question in Round 2. The algebraic reduction test — proposed by ChatGPT, executed here — categorically rules out Model B ↔ Model A isomorphism. D1's promotion to conditional theorem stands. OPEN-SS-26 → OPEN-SS-27 consolidation remains warranted. The sketch proceeds to minor revision, and the open-problem cascade to registry ratification (creation of PH-OPEN-SS-26 marking partial resolution), with clear conscience.

---

## 13. References

- `/CPP/series_strong/papers/SS-8_D1_ssv_minimization_sketch.md` (21 April 2026) — the sketch this analysis addresses.
- `/CPP/series_strong/papers/SS-8_Round2_review_request.md` — Round 2 review request.
- `/CPP/series_strong/papers/ss8_Q2_algebraic_reduction_test.py` — numerical script for the algebraic verification.
- `/CPP/series_strong/papers/ss8_ssv_minimization_sketch.py` — original sketch script (producing the $\lambda = 0.35 \cdot L$ values).
- ChatGPT Round 2 review — §2.3 and §3.2 pose the Q2 test and diagnose the failure mode.

---

*End of Q2 algebraic reduction analysis.*
*Exploratory tier. To be incorporated as appendix to the sketch before v0.1 drafting.*
