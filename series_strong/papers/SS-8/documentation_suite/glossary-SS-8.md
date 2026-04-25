# Glossary — SS-8: Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope

**Location:** `/CPP/series_strong/papers/SS-8/documentation_suite/glossary-SS-8.md`
**Last updated:** 26 April 2026 (v1.0 currency)
**Companion to:** `SS-8_interstitial_neutron_2EV_scaling.tex` (v1.0)

---

## Core Mathematical Objects

**$N_\alpha$:** Vertex count of the alpha-polytope — the number of bound alpha particles in a strict-$N=Z$ alpha-chain nucleus. Equals $Z/2 = N/2 = A/4$ for the strict-$N=Z$ case. Range studied in SS-8: $N_\alpha \in \{3, \ldots, 14\}$, corresponding to ${}^{12}\mathrm{C}$ through ${}^{56}\mathrm{Ni}$.

**$N_\text{ex}$:** Number of interstitial neutrons added to the strict-$N=Z$ alpha-chain baseline. $N_\text{ex} = 2$ is the primary regime; $N_\text{ex} \in \{3, \ldots, 8\}$ is the secondary regime with acknowledged precision degradation.

**$\Delta_1(N_\alpha)$:** The single-neutron interstitial binding strength as a function of polytope size. SS-8's central prediction: $\Delta_1(N_\alpha) = (6 - 12/N_\alpha) \cdot B_\text{pair}$.

**$B_\text{pair} = M_0 / \varphi = 2.342$ MeV:** The K₃ collective-mode quantum derived in SS-5 from K₃-eigenvalue analysis, transported unrescaled to the alpha-alpha contact scale in SS-7 and to the interstitial-alpha contact scale in SS-8. Three-scale recurrence is documented as Pattern 6 in `axiom-registry.md`.

**$M_0 = m_e \cdot z / \varphi = 3.790$ MeV:** Programme-level mass scale derived from electron mass calibration (A8′), 600-cell coordination number $z = 12$ (A2), and golden-ratio efficiency factor $\varphi$ (A5).

**$2E/V$:** Average vertex degree of a simplicial 3-polytope, equal to $6 - 12/V$ exactly by Euler's formula (Theorem `thm:euler-degree`). SS-8's central scaling law identifies the per-neutron interstitial binding strength with this combinatorial quantity times $B_\text{pair}$.

**$k_\text{eff}^\text{obs}$:** Effective coordination, computed from observed binding via $k_\text{eff}^\text{obs} = \Delta_1^\text{obs} / B_\text{pair}$. The 12-row primary table compares $k_\text{eff}^\text{obs}$ against the predicted $2E/V = 6 - 12/N_\alpha$.

**Simplicial 3-polytope:** Closed convex polyhedron in 3D whose every face is a triangle. Examples relevant to SS-8: tetrahedron ($N_\alpha = 4$), trigonal bipyramid (5), octahedron (6), pentagonal bipyramid (7), gyroelongated square bipyramid (10), icosahedron (12). The simplicial constraint is hypothesis C4 from SS-7.

**Deltahedron:** Synonym for simplicial 3-polytope used in the SS-8 v1.0 text (Greek "delta" for triangular faces). Eight convex deltahedra exist; SS-8 uses 12 of them — including non-convex realizations at $N_\alpha \in \{3, 7, 9, 11, 13, 14\}$.

**Polytope-identity ambiguity:** The case where multiple simplicial deltahedra can realize the same vertex count. Notable at $N_\alpha = 6$ (octahedron vs. triangular antiprism) and $N_\alpha = 12$ (icosahedron vs. less-symmetric alternatives). First-principles polytope identification is content of OPEN-SS-24.

---

## Physical Concepts

**Interstitial neutron:** A neutron added to an alpha-cluster nucleus beyond the $N = Z = 2N_\alpha$ baseline. Localized at an alpha-vertex of the polytope per Hypothesis D1 (proximity-binding); SS-8's prediction concerns the binding strength such a neutron acquires.

**Host alpha-vertex / host vertex:** The specific alpha-vertex at which a given interstitial neutron localizes. SS-8 Hypothesis D2 specifies that the K₃-edge bonds of contact faces incident at the host vertex couple to the host alpha's outer-nucleon contact face, transmitting binding strength $B_\text{pair}$ per edge.

**Bulk regime:** The condition $N_\text{ex}/V \ll 1$ under which uniform-vertex-distribution averaging applies. Holds well at $N_\alpha \geq 6$, $N_\text{ex} = 2$ (primary domain). Breaks down at small $N_\alpha$ (small-polytope attenuation H5′) and large $N_\text{ex}/V$ (precision degradation in the secondary regime).

**Cascade paradigm:** The structural picture across SS-5, SS-7, and SS-8 in which the same K₃ collective-mode quantum $B_\text{pair}$ operates at three successively coarser physical scales — nucleon-to-nucleon, alpha-to-alpha, interstitial-to-alpha — without rescaling.

**K₃ collective mode:** The eigenmode of the complete graph on three edges (the $K_3$ graph), originally derived in SS-5 from the SS-5 nucleon contact-face geometry. Its eigenvalue produces the $1/\varphi$ factor in $B_\text{pair} = M_0/\varphi$.

**Conditional theorem:** A theorem proved under explicit structural hypotheses that are not themselves derived from CPP axioms. SS-8 carries three: D1 (vertex localization), D2 (K₃-edge coupling at host vertex), D3 (bulk-regime averaging). D1 is promoted to a conditional theorem at Level-1+2 independence under two functionally independent realizations (Models A and B); D2 and D3 remain at proposition tier.

**Level-1/2/3 independence (decomposition methodology):** A discipline introduced in SS-8 for evaluating multi-premise theorems. Level-1 is algebraic independence (the premises don't reduce to one another by symbolic manipulation). Level-2 is functional independence (the premises produce distinguishable empirical signatures). Level-3 is physical-principle independence (the premises don't share a deeper ancestor). SS-8's D1 achieves Level-1+2; Level-3 is OPEN-SS-26 PARTIAL because both Models A and B share a proximity-binding ancestor.

**Proximity-binding:** A precondition shared by D1's two model realizations: an interstitial neutron localizes near (rather than far from) the alpha-cluster, with the localization site selected by an SSV-minimization principle. The "proximity" content is what bounds D1's Level-3 independence — a third model that produces D1 without invoking proximity would close the Level-3 gap (OPEN-SS-26 closure path).

**Pattern 6 scale recurrence:** The empirical observation that $B_\text{pair} = M_0/\varphi$ produces the same quantum at three physical scales (nucleon-pair in SS-5, alpha-alpha in SS-7, interstitial-alpha in SS-8) without rescaling. Documented in `axiom-registry.md` Pattern 6. Whether the recurrence is structurally *necessary* (forced by the axiom set) versus *allowed* (consistent with but not implied by the axioms) remains an open programme-level question.

---

## Standard Physics Terms (used non-standardly)

**Vertex degree ($\deg_v$):** In SS-8, the number of K₃-contact face edges incident at vertex $v$ in the alpha-polytope. Distinguished from graph-theoretic degree (which counts edges of any type) in cases where the polytope's edge set is not the same as its K₃-contact-face-edge set. For pure simplicial 3-polytopes the two counts coincide, so the distinction is mostly a clarification of usage.

**Coordination number:** Used in two distinct senses in SS-8 — (a) the 600-cell vertex coordination $z = 12$ from axiom A2, and (b) the per-vertex coordination $\deg_v$ within the alpha-polytope, which varies across vertices for non-vertex-transitive polytopes. The "effective coordination" $k_\text{eff}$ refers to the vertex-averaged $\deg_v$, equal to $2E/V = 6 - 12/V$ on simplicial 3-polytopes.

**Pauli decrement:** SS-8's H4′ provisional model for the precision degradation at $N_\text{ex} > 2$. Inherits the same-polarity Pauli cost $M_0/\varphi^3 \approx 0.895$ MeV from SS-5 but modulates per-pair contribution by the vertex-availability factor as $N_\text{ex}$ grows. Distinct from the standard nuclear-physics "Pauli blocking" terminology, though related in content.

---

## Status Labels

**THEOREM (conditional):** Proved under stated structural hypotheses; the proof is rigorous given those hypotheses but the hypotheses themselves are not derived from CPP axioms. SS-8's D1, D2, D3, and the central 2E/V scaling law (THEO-SS-15) all carry conditional status.

**PROPOSITION:** A claim with strong structural motivation but not yet a proof. SS-8's residual decomposition (H3′, H5′) is propositional — the decomposition tightens the empirical band substantially but is not part of the proof of the central law.

**HYPOTHESIS (paper-level structural):** A premise invoked within a single paper to enable a derivation; explicitly not promoted to programme-level axiom. C1–C4 (inherited from SS-7) and D1–D3 (introduced in SS-8) are paper-level structural hypotheses.

**OPEN:** A registered problem in `Research_Frontier.md`. SS-8 opens OPEN-SS-26 (D1 Level-3 PARTIAL), OPEN-SS-27 (D2 derivation), OPEN-SS-28 (D3 derivation), and partially resolves OPEN-SS-23.

**SIGNAL:** Empirical agreement at high precision but the underlying theorem is not yet rigorously proved. Used in CPP-wide registries for entries like PRED-C-13 (heavy-quark Koide K(c,b,t)). SS-8's predictions are not signal-tier — they are conditional theorems with explicit structural dependencies.
