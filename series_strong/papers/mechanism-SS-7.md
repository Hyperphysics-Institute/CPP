# Mechanism: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.2 (21 April 2026, symmetric-honesty corrections)
**Last updated:** 21 April 2026
**Document type:** Physical mechanism description for physicists

---

## One-sentence summary

For strict $N{=}Z$ alpha-chain nuclei ($N=Z=2N_\alpha$, $N_\alpha \in \{3,\ldots,14\}$), each alpha acts as a rigid tetrahedral unit that bonds base-to-base with its neighbors across triangular K$_3$ contact faces, assembling into a simplicial convex polytope whose $3N_\alpha-6$ edges (Euler's formula) each carry one $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV collective mode, yielding the zero-parameter binding law $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$ that matches AME 2020 to $\pm 1.5\%$ across twelve nuclei from ${}^{12}$C through ${}^{56}$Ni.

---

## Inputs and constants

All constants are inherited from prior CPP papers, not tuned to SS-7 data.

| Symbol | Value | Source |
|---|---|---|
| $\Balpha$ | 28.296 MeV (experimental); 27.904 MeV (SS-5 LO) | SS-5 cascade at $A=4$ |
| $B_{\text{pair}}$ | 2.342 MeV | SS-5, K$_3$ collective mode over triangular contact face |
| $M_0$ | 3.7898 MeV | SM-8 CPP unit mass |
| $\varphi$ | 1.618034$\ldots$ | golden ratio |
| $R_{\alpha\alpha}$ | 2.37 fm | Extracted via inversion from ${}^8$Be unboundness (not derived; OPEN-SS-24) |

Zero fitted parameters. All twelve Table 1 predictions use the same two constants ($\Balpha$, $B_{\text{pair}}$).

---

## The mechanism, step by step

### Step 1: Alpha as rigid tetrahedral unit (C1, inherited from SS-5)

Each alpha is SS-5's closed-polytope $A=4$ structure: four nucleons arranged as a tetrahedron with binding $\Balpha = 28.296$ MeV. At energies per alpha-alpha contact ($\sim 2.3$ MeV), this structure is rigid: the first excited state of ${}^4$He lies at 20.2 MeV, above the $^3$H+p breakup threshold. Contact interactions perturb alphas by $\sim 1\%$ of their first-excitation threshold, justifying leading-order rigidity.

### Step 2: Alpha-alpha base-to-base contact (C2, geometric extension of SS-5)

When two alphas meet in a nuclear assembly, they do so base-to-base: one triangular outer face of each alpha is shared with the neighbor. This is the direct analog of SS-5's nucleon-nucleon base-to-base configuration at the next level of the cascade. Each alpha has four candidate contact faces, constraining the geometry of any multi-alpha assembly.

### Step 3: K$_3$ collective mode at each contact (C3, SS-5 rule applied at alpha scale)

The shared triangular contact face between two alphas has three nucleon-nucleon pair connections at its vertices — one per vertex of the triangle — forming a complete graph K$_3$ on three edges. The SS-5 eigenvalue calculation for a K$_3$ structure (eigenvalues $\{+2, -1, -1\}$) applies at the alpha-alpha face identically to how it applies at the nucleon-nucleon face: one collective bonding mode at $B_{\text{pair}} = M_0/\varphi$ per K$_3$ face.

### Step 4: Simplicial polytope assembly (C4, hypothesis)

$N_\alpha$ alphas in a bound strict-$N{=}Z$ nucleus arrange as the vertices of a convex, triangular-faced, simplicial 3-polytope. Each edge of the polytope is one alpha-alpha contact — equivalently, one K$_3$ face — contributing one $B_{\text{pair}}$ quantum. C4 is a structural hypothesis within CPP, not yet derived from lattice-level dynamics; supported empirically by the extended Table 1 ($N_\alpha \in [3,14]$, twelve concurrent zero-parameter matches) and the stress tests in §6.5, registered as OPEN-SS-24.

Physical intuition (not derivation): triangular faces follow from C1+C2 (rigid tetrahedra share triangular faces only); maximal connectivity follows from thermodynamic selection (ground state maximizes edge count at fixed vertex count); convexity follows from rigid-packing constraints.

### Step 5: Edge count from Euler's formula (Theorem 2.1)

For any simplicial convex polyhedron on $N_\alpha \geq 4$ vertices, Euler's formula $V - E + F = 2$ combined with the triangular-face constraint $2E = 3F$ gives $E = 3N_\alpha - 6$. This is a pure mathematical theorem about simplicial polytopes; it holds regardless of which specific polytope is realized. Degenerate cases: $N_\alpha = 3$ (triangle) gives $E = 3$; $N_\alpha = 2$ (line segment) gives $E = 1$, non-simplicial and handled separately in §4.

### Step 6: Binding energy assembly

Total binding energy is the sum of per-alpha and per-edge contributions:

$$B(N_\alpha) = N_\alpha \cdot \Balpha + (3N_\alpha - 6) \cdot B_{\text{pair}} \qquad (N_\alpha \geq 3)$$

The first term is the intra-alpha binding (inherited from SS-5); the second term is the inter-alpha contact binding summed over the topologically-fixed edge count.

### Step 7: ${}^8$Be re-derivation ($N_\alpha = 2$, degenerate case)

At $N_\alpha = 2$ the formula gives $3N-6 = 0$, predicting no alpha-polytope bond. Two alphas on a line have one contact; but this single contact, in isolation, sees full alpha-alpha Coulomb repulsion at vacuum strength. Imposing the observed 92 keV unboundness as the binding condition inverts to $R_{\alpha\alpha} = 2.37$ fm (Finding 4.1). This is a consistency check, not a forward prediction of $R_{\alpha\alpha}$.

---

## Mathematical correspondence table

| Physics claim | Equation | Paper section |
|---|---|---|
| Alpha rigidity | $\Balpha \gg B_{\text{pair}}$ | §2.1, C1 |
| Each K$_3$ face contributes one quantum | $B_{\text{per-face}} = B_{\text{pair}} = M_0/\varphi$ | §2.1, C3 |
| Simplicial polytope edge count | $E(N_\alpha) = 3N_\alpha - 6$ | §2.2, Theorem 2.1 |
| Main binding formula | $B(N_\alpha) = N_\alpha\Balpha + (3N_\alpha-6)B_{\text{pair}}$ | §1 Main Result; §2.3 Eq.(2) |
| ${}^8$Be Coulomb balance | $E_{\text{Coul}}(R) = 5.765/R$ MeV | §2.4 |
| $R_{\alpha\alpha}$ from ${}^8$Be | $R_{\alpha\alpha} = 5.765/2.434 = 2.37$ fm | §4, Finding 4.1 |
| Neutron-excess signal (non-$N{=}Z$) | $\Delta B / B \sim -2\%$ to $-2.5\%$, $\sim 2$ MeV/neutron | §5.1 traceability footnote; OPEN-SS-23 |
| Structural falsification threshold | $|\Delta B/B| > 2\%$ at $N_\alpha \in [3,14]$ strict $N{=}Z$ | §6.3 |

---

## Failure modes

Where the mechanism is known to break down or incomplete:

1. **Beyond $N_\alpha = 14$ on the strict $N{=}Z$ chain:** Preliminary indication (from less-precise AME values at $N_\alpha = 15, 16$) that residuals remain $< 2\%$ through ${}^{64}$Ge, but not a claim of this paper. Formula applicability beyond ${}^{56}$Ni is future work.

2. **Non-$N{=}Z$ isotopes at alpha-chain $N_\alpha$ values (OPEN-SS-23, primary SS-8 target):** ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe each have $N - Z = +4$ and show $\sim 2$ MeV per extra neutron beyond Eq.(2)'s prediction — standard neutron-excess binding that the formula does not model by construction. ${}^{48}$Ca at $N - Z = +8$ is a natural stress test for a CPP neutron-excess mechanism. Formula does not apply to these nuclei; derivation of the neutron-excess term is the primary target for SS-8.

3. **Odd-$A$ and non-alpha-clustered nuclei (OPEN-SS-23):** Odd-$A$ cases (${}^7$Li, ${}^9$Be, ${}^{11}$B, ${}^{13}$C) and non-clustered structures (${}^6$Li, ${}^{14}$N, ${}^{18}$O) require extension of the formula to handle partial-alpha substructures and excess nucleons.

4. **Simplicial connectivity not derived (OPEN-SS-24):** C4 remains a hypothesis. Three physical-intuition arguments (triangular faces, maximal reinforcement, rigid-packing convexity) in §2.1 are suggestive but not rigorous. Derivation targeted for SS-9 candidate paper.

5. **$R_{\alpha\alpha}$ not derived:** Finding 4.1 extracts $R_{\alpha\alpha} = 2.37$ fm via inversion from ${}^8$Be; not a forward prediction. First-principles derivation is OPEN-SS-24-adjacent work.

6. **Coulomb screening mechanism schematic only (§5.4, OPEN-SS-25):** DP-sea rearrangement as screening mechanism is supported by a scaling argument and cluster-model comparison, but not derived from CPP primitives. Figure 4 is labeled schematic representation. First-principles treatment deferred under OPEN-SS-25 (DP-sea screening of alpha-alpha Coulomb in bound polytopes; new in v1.2, absorbs the screening physics that was tagged "OPEN-SS-22-adjacent" in v1.1).

7. **Hoyle-state energy not predicted (§4.3):** Geometric framing (dilated triangle) is consistent with the SS-7 structure, but quantitative Hoyle energy requires excited-state methods beyond rigid-polytope formalism.

8. **${}^{20}$Ne $+1.19\%$ deviation:** Largest residual in Table 1. Consistent with ${}^{20}$Ne's known prolate deformation. No open problem registered; within the $\pm 1.5\%$ band.

### Retired failure mode (v1.1): heavy-nuclei icosahedral closure onset

v1.1 of this companion file listed an OPEN-SS-22 failure mode ("$-2\%$ to $-2.5\%$ underbinding at ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe; flat-residual shape suggests structural onset at icosahedral closure, $N_\alpha = 12$"). That item was diagnosed in v1.2 as an isotope-selection artifact: the three v1.1 nuclei are non-$N{=}Z$ (each has $N - Z = +4$); the strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni) stay in family with the primary eight. The "flat plateau" does not exist in strict-$N{=}Z$ alpha-chain data. The ~2% deviation in the v1.1 nuclei is neutron-excess binding, covered under item 2 above. OPEN-SS-22 is retired in v1.2; see `problem_histories/PH-OPEN-SS-22.md` for the retirement narrative.

---

## Adversarial stress tests (§6.5)

Contributed by ChatGPT's re-review engagement (19 April 2026). Four nuclei tested against plausible lower-edge alternatives at fixed $(\Balpha, B_{\text{pair}})$:

| Nucleus | $E_{\text{simp}}$ / error | $E_{\text{alt}}$ / error | Alt geometry |
|---|---|---|---|
| ${}^{32}$S | 18 / $-1.20\%$ | 12 / $-6.37\%$ | cube |
| ${}^{32}$S | 18 / $-1.20\%$ | 16 / $-2.92\%$ | square antiprism |
| ${}^{28}$Si | 15 / $-1.41\%$ | 12 / $-4.38\%$ | wheel-like |
| ${}^{36}$Ar | 21 / $-0.94\%$ | 20 / $-1.70\%$ | monocapped sq antiprism |
| ${}^{40}$Ca | 24 / $-0.84\%$ | 20 / $-3.58\%$ | pentagonal-antiprism-type |

All lower-edge alternatives underperform the simplicial rule. ${}^{36}$Ar is the tightest test: single-edge drop degrades agreement from $-0.94\%$ to $-1.70\%$, matching one $B_{\text{pair}}$ quantum. Edge-count dominance at leading order confirmed: the empirical success is not merely due to total binding magnitude but to the specific combinatorial edge count $3N_\alpha - 6$.
