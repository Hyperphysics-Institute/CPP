# Glossary: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.2 (21 April 2026, symmetric-honesty corrections)
**Last updated:** 21 April 2026

---

## Constants

### $\Balpha$
Experimental ${}^4$He binding energy, 28.296 MeV (AME 2020). Inherited from SS-5, where the LO-CPP prediction gave 27.904 MeV at $-1.4\%$. SS-7 uses the experimental value as primary input so that Table 1 isolates SS-7's edge-count structure from SS-5's per-alpha residual.

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
A nucleus with $N = Z = 2N_\alpha$ composed of $N_\alpha$ alpha clusters. SS-7 v1.2 claims predictive coverage across the strict $N{=}Z$ alpha-chain for $N_\alpha \in [3, 14]$: ${}^{12}$C, ${}^{16}$O, ${}^{20}$Ne, ${}^{24}$Mg, ${}^{28}$Si, ${}^{32}$S, ${}^{36}$Ar, ${}^{40}$Ca, ${}^{44}$Ti, ${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni. "Strict" emphasizes $N = Z$ exactly; non-$N{=}Z$ isotopes at alpha-chain $N_\alpha$ values (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe with $N - Z = +4$) are out of scope — their $\sim 2$ MeV per extra neutron signal is neutron-excess binding, not alpha-cluster physics. Non-alpha-chain cases (odd-$A$, $N \neq Z$, non-clustered structures) register as OPEN-SS-23.

### Strict $N{=}Z$ alpha-chain
Subset of the alpha-chain explicitly restricted to $N = Z = 2N_\alpha$, $A = 4N_\alpha$. This is the domain on which SS-7's central formula is claimed. Distinguishing phrase introduced in v1.2 after the v1.1 Table 1 at $N_\alpha \geq 12$ was found to have substituted non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe) for the strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni).

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

### Structural onset (retired in v1.2)
In v1.1 this phrase referred to the apparent flat-residual pattern at $N_\alpha \geq 12$ (−2% to −2.5% across ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe) that was read as new physics activating at a specific threshold (icosahedral-closure hypothesis, OPEN-SS-22). v1.2 established that the three v1.1 data points are non-$N{=}Z$ isotopes whose deviation is neutron-excess binding; the strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni) stay in family with the primary eight. The "structural onset" pattern does not exist in alpha-chain data. OPEN-SS-22 is retired; see `problem_histories/PH-OPEN-SS-22.md`. Entry retained here rather than deleted so that any reference to "structural onset" in legacy documents resolves to the correct v1.2 status.

### Isotope-selection artifact (new in v1.2)
A pattern in a residual or prediction set that arises from which isotopes were chosen to represent a $Z$ or $N_\alpha$ value rather than from the underlying physics. Named and catalogued in v1.2 after the v1.1 Table 1 flat-residual pattern at $N_\alpha \geq 12$ was diagnosed as one: the v1.1 rows at $N_\alpha = 12, 13, 14$ substituted ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe (each with $N - Z = +4$) for the strict $N{=}Z$ nuclei. The $\sim 2$ MeV/neutron of neutron-excess binding these isotopes carry was mistaken for a structural signal. Defensive check: when a formula claims strict $N{=}Z$ applicability, verify that every row in a primary-claim table is actually $N = Z$ before interpreting deviations.

### Retirement (of an open problem) — new status transition in v1.2
Programme status transition for an open problem whose registered empirical anchor is subsequently found to be an artifact (of isotope selection, measurement precision, framework contamination, or similar), such that no well-defined replacement empirical anchor exists for the hypothesis that motivated registration. Distinct from: RESOLVED (solution found), PARTIALLY RESOLVED (sub-scope solved), FALSIFIED (well-defined claim shown false). Retirement does not assign blame; retirement reflects discovery that the problem's anchor was not what it appeared to be. Precedent established by OPEN-SS-22 in v1.2.

### Hostile-geometry stress test
The four-nucleus test (§6.5) comparing the simplicial $E = 3N_\alpha - 6$ prediction against physically-arguable lower-edge alternatives (cube, square antiprism, wheel-like, monocapped square antiprism, pentagonal antiprism) at fixed $(\Balpha, B_{\text{pair}})$. All alternatives tested underperform the simplicial rule. Contributed by ChatGPT's re-review engagement.

### Inversion (of a binding condition)
Method used for Finding 4.1: given a formula with known inputs on one side and a known experimental result on the other, solve for the one undetermined variable. $R_{\alpha\alpha} = 2.37$ fm is inverted from ${}^8$Be's 92 keV unboundness, not predicted forward from CPP.

---

## Mechanism terms

### DP-sea screening
Proposed mechanism whereby the dipole-pair sea between two alphas in a bound polytope reorganizes to partially screen the local charge product, reducing effective alpha-alpha Coulomb below its vacuum value. Differs from the ${}^8$Be case where isolated alpha-alpha contact sees full Coulomb. Supported by scaling argument and cluster-model comparison (§5.4); not derived from CPP primitives. Figure 4 is a schematic representation, not a derived charge distribution. A first-principles CPP derivation of the DP-sea screening profile is registered as OPEN-SS-25 (new in v1.2; absorbs what v1.1 labeled as "OPEN-SS-22-adjacent" work).

### Topological invariant (of the edge count)
The combinatorial edge count $3N_\alpha - 6$ is a topological property of the simplicial polytope: Coulomb perturbs energy per edge but does not change how many edges exist. Framing introduced in §5.4 to clarify that the edge-count structure is robust to Coulomb corrections even when per-edge energies shift.

### M$_0/\varphi$ recurrence
The empirical fact that the same quantum $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV appears in three distinct CPP contexts: SS-5 nucleon-nucleon contact, SS-5 ${}^4$He tetrahedral closure, and SS-7 alpha-alpha contact. Empirically supported (zero-parameter agreement across three sectors) but not yet derived as structurally necessary across scales. §6.2.

### Cascade paradigm (at two levels)
SS-5 is the first level: nucleons as primary tetrahedra forming nuclei at $A \leq 4$. SS-7 is the second level: alphas as secondary tetrahedra forming nuclei at $A \geq 8$ (for alpha-chain composition). The paradigm is hierarchical rigid-tetrahedral bonding via shared triangular faces.

---

## Methodology terms

### Paper type: prediction paper
Per operating_system.md §4 taxonomy. Success criterion: concurrent multi-nucleus agreement at zero fitted parameters. SS-7 v1.2 qualifies: 12 nuclei × 2 inherited constants × 0 fits × concurrent match within $\pm 1.5\%$ (RMS $0.80\%$ across all 12; $0.91\%$ across the primary $N_\alpha \in [3,10]$ set).

### Theorem/hypothesis split
Structural improvement introduced in v1.0 and preserved through v1.2: Theorem 2.1 (mathematics: $3N_\alpha - 6$ edges for simplicial polytopes) is cleanly separated from C4 (physics: alpha-chain nuclei realize simplicial polytopes). Clarifies that Table 1 is testing C4, not Theorem 2.1. Theorem 2.1 is mathematics and cannot be falsified by nuclear data; C4 is physics and can be.

### Structural hypothesis within CPP
Status designation for C4 (and for the M$_0/\varphi$ recurrence): supported within the CPP framework by empirical success across multiple contexts, but not yet derived from lattice-level dynamics. Target-slot for derivation: OPEN-SS-24 (C4), future work (recurrence).

### Reviewer-response protocol
Documentation protocol adopted 19 April 2026 (operating_system.md §4 Phase 4): each reviewer round produces a response document with Accept/Partial/Decline disposition per item, line-cited evidence for factual pushback. SS-7 was the protocol's first full validation case; caught one wholesale-hallucination failure (ChatGPT round-1, 19 April) and one partial-template-synthesis failure (Copilot round-2, 20 April), both corrected through formal letters that produced accountable responses. In v1.2 the protocol ran in a new mode: a single symmetric-honesty verification letter sent to all three reviewers simultaneously (ChatGPT, Copilot, Grok) after the author team surfaced a diagnostic error in its own v1.1 Table 1. All three converged independently on the same interpretation (isotope-selection artifact); the convergence itself is part of the retirement criterion for OPEN-SS-22.

### Symmetric-honesty verification cycle (new in v1.2)
Review cycle mode introduced in v1.2: not driven by reviewer critique of a new paper, but by an author-team-surfaced concern about a previously-shipped paper's own framing. Letter is sent to multiple reviewers simultaneously with an explicit tasks structure; open question of the letter is framed without prejudging the answer. Retirement or revision action is taken only on reviewer convergence. Distinct from the standard round-by-round review flow because the finding is disclosed rather than discovered by the reviewer. Governing protocol: `templates/relationship_protocol.md` §2.6 (symmetric application to self).

### PDF vs .tex submission protocol (new in v1.2)
Reviewer submissions use `.tex` source rather than compiled PDF. Established in v1.2 after two v1.1 reviewers independently misread $\varphi^{1/z}$ as $\varphi^{1/2}$ from small-superscript rasterization in the compiled PDF. The numerical difference is large ($\varphi^{1/12} - 1 \approx 4.1\%$ vs $\varphi^{1/2} - 1 \approx 27.2\%$); the misreading passed as a clean verbatim quote. PDF attachments are offered on request but not sent by default.

### ±2% structural falsification threshold
Contributed by ChatGPT re-review. Any strict $N{=}Z$ alpha-chain nucleus at $N_\alpha \in [3, 14]$ showing $|\Delta B/B| > 2\%$ would falsify the $3N_\alpha - 6$ edge-count rule specifically. Chosen to exceed the CPP generic residual band by a factor, isolating structural failure from higher-order corrections. v1.2 extended the threshold's stated domain from $[3,10]$ to $[3,14]$ consistent with the extended primary claim; no predictions in $[3,14]$ currently exceed the threshold.

### Adversarially-tested model
Classification earned by SS-7 through the §6.5 stress tests: not merely a model that fits, but a model that survives systematic perturbation away from the $3N_\alpha-6$ edge count at fixed CPP constants. Distinction from "model proposal" introduced in Conclusion.
