# Glossary: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.1 (20 April 2026, post-round-2 minor revisions)
**Last updated:** 20 April 2026

---

## Constants

### $\Balpha$
Experimental ${}^4$He binding energy, 28.296 MeV (AME 2020). Inherited from SS-5, where the LO-CPP prediction gave 27.904 MeV at $-1.4\%$. SS-7 uses the experimental value as primary input so that v1.0 Table 1 isolates SS-7's edge-count structure from SS-5's per-alpha residual.

### $B_{\text{pair}}$
Nucleon-pair binding quantum, $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV. Inherited from SS-5 as the K$_3$ collective-mode strength over a triangular contact face. SS-7 uses the same quantum at the alpha-alpha face; the recurrence across scales is empirical within CPP, derivation remains open (§6.2).

### $M_0$
CPP unit mass, 3.7898 MeV, from SM-8's 600-cell distance-shell analysis.

### $\varphi$
Golden ratio, $(1 + \sqrt{5})/2 = 1.618034\ldots$

### $R_{\alpha\alpha}$
Alpha-alpha contact distance, 2.37 fm. Extracted via inversion from the ${}^8$Be unboundness (Finding 4.1). This is a consistency parameter, not a forward prediction; first-principles derivation is OPEN-SS-24-adjacent.

---

## Structural terms

### Alpha-chain nucleus
A nucleus with $N = Z = 2N_\alpha$ composed of $N_\alpha$ alpha clusters. SS-7 claims predictive coverage for $N_\alpha \in [3, 10]$: ${}^{12}$C, ${}^{16}$O, ${}^{20}$Ne, ${}^{24}$Mg, ${}^{28}$Si, ${}^{32}$S, ${}^{36}$Ar, ${}^{40}$Ca. Nuclei outside this pattern (odd-$A$, $N \neq Z$, $N_\alpha \geq 12$) are out of scope; OPEN-SS-22, OPEN-SS-23.

### Simplicial polytope
A convex polyhedron in which every face is a triangle. Equivalently, a triangulated topological sphere. Theorem 2.1: any simplicial polytope on $N_\alpha \geq 4$ vertices has exactly $3N_\alpha - 6$ edges (Euler's formula + triangle-face constraint).

### Alpha-polytope
The simplicial convex polytope formed by the $N_\alpha$ alpha clusters of an alpha-chain nucleus. Vertex count: $N_\alpha$. Edge count: $3N_\alpha - 6$. Face count: $2N_\alpha - 4$. Specific polytope realized at each $N_\alpha$ is not uniquely determined by the formula (Remark 2.2); only the edge count matters to leading order.

### Edge-count dominance
The empirical claim (confirmed by stress tests §6.5) that binding energy at fixed $(\Balpha, B_{\text{pair}})$ is primarily controlled by the combinatorial edge count $E$; vertex-connectivity variations at fixed $E$ are subleading. This is what the stress tests demonstrate: the success of the model is not merely due to total binding magnitude but to the specific edge count $3N_\alpha - 6$.

### K$_3$ contact face
The triangular face shared between two alphas at base-to-base contact. Carries three nucleon-nucleon pair connections at its vertices, forming a complete-graph K$_3$ structure. Eigenvalue decomposition gives $\{+2, -1, -1\}$; the $\lambda_+ = +2$ collective mode is the one $B_{\text{pair}}$ quantum per contact. See Figure 2 in paper.

### Base-to-base contact
Configuration of two alphas in contact where their triangular outer faces share a K$_3$ structure. Direct analog of SS-5's nucleon-nucleon base-to-base configuration at the next level of the cascade.

### Structural onset
The flat-residual pattern at $N_\alpha \geq 12$ (−2% to −2.5% across ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe) consistent with new physics activating at a specific threshold rather than progressive smooth breakdown. Distinguishes icosahedral-closure hypothesis (primary candidate) from alternative mechanisms. See §5.1.

### Hostile-geometry stress test
The four-nucleus test (§6.5) comparing the simplicial $E = 3N_\alpha - 6$ prediction against physically-arguable lower-edge alternatives (cube, square antiprism, wheel-like, monocapped square antiprism, pentagonal antiprism) at fixed $(\Balpha, B_{\text{pair}})$. All alternatives tested underperform the simplicial rule. Contributed by ChatGPT's re-review engagement.

### Inversion (of a binding condition)
Method used for Finding 4.1: given a formula with known inputs on one side and a known experimental result on the other, solve for the one undetermined variable. $R_{\alpha\alpha} = 2.37$ fm is inverted from ${}^8$Be's 92 keV unboundness, not predicted forward from CPP.

---

## Mechanism terms

### DP-sea screening
Proposed mechanism whereby the dipole-pair sea between two alphas in a bound polytope reorganizes to partially screen the local charge product, reducing effective alpha-alpha Coulomb below its vacuum value. Differs from the ${}^8$Be case where isolated alpha-alpha contact sees full Coulomb. Supported by scaling argument and cluster-model comparison (§5.4); not derived from CPP primitives. Figure 4 is a schematic representation, not a derived charge distribution.

### Topological invariant (of the edge count)
The combinatorial edge count $3N_\alpha - 6$ is a topological property of the simplicial polytope: Coulomb perturbs energy per edge but does not change how many edges exist. Framing introduced in §5.4 to clarify that the edge-count structure is robust to Coulomb corrections even when per-edge energies shift.

### M$_0/\varphi$ recurrence
The empirical fact that the same quantum $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV appears in three distinct CPP contexts: SS-5 nucleon-nucleon contact, SS-5 ${}^4$He tetrahedral closure, and SS-7 alpha-alpha contact. Empirically supported (zero-parameter agreement across three sectors) but not yet derived as structurally necessary across scales. §6.2.

### Cascade paradigm (at two levels)
SS-5 is the first level: nucleons as primary tetrahedra forming nuclei at $A \leq 4$. SS-7 is the second level: alphas as secondary tetrahedra forming nuclei at $A \geq 8$ (for alpha-chain composition). The paradigm is hierarchical rigid-tetrahedral bonding via shared triangular faces.

---

## Methodology terms

### Paper type: prediction paper
Per operating_system.md §4 taxonomy. Success criterion: concurrent multi-nucleus agreement at zero fitted parameters. SS-7 qualifies: 8 nuclei × 2 inherited constants × 0 fits × concurrent match within $\pm 1.5\%$.

### Theorem/hypothesis split
The v1.0 structural improvement: Theorem 2.1 (mathematics: $3N_\alpha - 6$ edges for simplicial polytopes) is cleanly separated from C4 (physics: alpha-chain nuclei realize simplicial polytopes). Clarifies that Table 1 is testing C4, not Theorem 2.1.

### Structural hypothesis within CPP
Status designation for C4 (and for the M$_0/\varphi$ recurrence): supported within the CPP framework by empirical success across multiple contexts, but not yet derived from lattice-level dynamics. Target-slot for derivation: OPEN-SS-24 (C4), future work (recurrence).

### Reviewer-response protocol
Documentation protocol adopted 19 April 2026 (operating_system.md §4 Phase 4): each reviewer round produces a response document with Accept/Partial/Decline disposition per item, line-cited evidence for factual pushback. SS-7 is the protocol's first full validation case; caught one wholesale-hallucination failure (ChatGPT round-1, 19 April) and one partial-template-synthesis failure (Copilot round-2, 20 April), both corrected through formal letters that produced accountable responses.

### ±2% structural falsification threshold
Contributed by ChatGPT re-review. Any alpha-chain nucleus at $N_\alpha \in [3, 10]$ showing $|\Delta B/B| > 2\%$ would falsify the $3N_\alpha - 6$ edge-count rule specifically. Chosen to exceed the CPP generic residual band by a factor, isolating structural failure from higher-order corrections.

### Adversarially-tested model
Classification earned by SS-7 through the §6.5 stress tests: not merely a model that fits, but a model that survives systematic perturbation away from the $3N_\alpha-6$ edge count at fixed CPP constants. Distinction from "model proposal" introduced in Conclusion.
