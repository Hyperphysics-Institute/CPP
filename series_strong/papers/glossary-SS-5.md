# Glossary: SS-5 — Light-Nuclei Binding from the Open-Vertex Cascade

**Paper:** SS-5 v0.2
**Last updated:** 17 April 2026

---

## Terms introduced or emphasised in SS-5 v0.2

### Base-to-base configuration
Nucleon pair arrangement in which the triangular quark-bearing bases of two hybrid tetrahedra are in direct contact, with the open vertices pointing outward on opposite sides. Predominant configuration of the deuteron (Proposition SS-5 v0.2 §2). Supersedes v0.1's vertex-to-vertex picture.

### K₃ base-contact collective mode
The three qq-pair oscillators across a base-to-base nucleon contact form a K₃ complete-graph structure with eigenvalue spectrum $\{+2, -1, -1\}$. The $\lambda_+ = +2$ eigenvalue carries the collective binding; the two $\lambda_-$ eigenvalues are antibonding. The collective mode is a single effective pair quantum at $B_{\text{pair}} = M_0/\varphi$.

### Cascade factor $(A-1)$
Multiplicative reinforcement of each np pair binding by the number of closed-polytope completion pathways through the remaining nucleons in a closed A-nucleon polytope. A=2: factor 1. A=3: factor 2. A=4: factor 3. Central content of CONJ-SS-11; rigorous derivation pending (OPEN-SS-19).

### Closed-polytope gap
The geometric fact that the 600-cell admits no closed polytope at A=5, 6, 7, 8, 9, 10, 11 nucleon-vertices. Basis of SS-5 v0.2's unboundness predictions for ${}^5$He, ${}^5$Li, ${}^8$Be.

### Closure bonus
Additional binding of $M_0/\varphi = B_{\text{pair}} = 2.342$ MeV activated when A=4 nucleons form a closed tetrahedral polytope. Analogous to SS-1/SS-3 internal-cage closure.

### Pauli coefficient $M_0/\varphi^3$
Energy penalty per same-polarity open-vertex pair in the cascade formula. Numerical value $0.895$ MeV per like-pair. Motivated by propagation-step-count argument (one extra $1/\varphi^2$ attenuation vs pair binding) but not rigorously derived from CPP primitives (OPEN-SS-19).

### Pair binding $B_{\text{pair}}$
$B_{\text{pair}} = M_0/\varphi = m_e z/\varphi^2 = 2.342$ MeV. The binding energy of a single np pair across a base-to-base contact. The $A=2$ limit of the cascade formula.

### Cascade formula (CONJ-SS-11)
$$B(A,Z) = (A-1) n_{np} (M_0/\varphi) - n_{pp} \alpha_{em}\hbar c/(1.2 A^{1/3}) - (n_{pp}+n_{nn})(M_0/\varphi^3) + \delta_{A,4}(M_0/\varphi)$$
Zero-parameter light-nuclei binding formula.

### Open-vertex (cascade-available)
The polarity-assigned unoccupied vertex of a hybrid-tetrahedral nucleon. In v0.2 base-to-base, the open vertex points outward from the bonded pair and is available for cascade bonding to additional nucleons (vertex-to-vertex or vertex-to-base).

### Closed-polytope completion pathway
One of the $A-1$ distinct ways a given np-pair bond in a closed A-nucleon polytope can be reinforced by connections through the remaining nucleons. Basis of the cascade-factor multiplicity.

### Structural prediction
A qualitative CPP prediction (bound/unbound, I=0/I=1, S=0/S=1) derived directly from geometric/polarity/closed-polytope considerations without numerical calculation. Example: ${}^5$He unbound, deuteron I=0.

---

## Terms inherited from prior papers

| Term | Defined in |
|---|---|
| 600-cell polytope, $V$, $E$, $F$, $C$, $z$ | SM-1, SM-6 |
| Hybrid tetrahedron (nucleon) | SS-2 §5 |
| qDP chain, ZBW oscillator | SM-1, SS-1 |
| Propagation efficiency $\eta = 1/\varphi$ | SM-6 §4, Axiom A5 |
| DP energy quantum $M_0 = m_e z/\varphi$ | SM-8 |
| Lattice unit $l_{\text{unit}}$, edge $l_{\text{edge}}$ | SS-2 §2 |
| K$_3$ spectrum $\{+2, -1, -1\}$ | SM-3 |
| Koide collective-mode reduction | SM-3 |
| 4+4 physical mode basis | SS-3 |
| Stereographic residual $\varphi^{1/z} - 1$ | SS-1 §11, SS-4 Remark 4.1 |
| Layer A / Layer B / Layer C | SS-3, SM-3 |
| Swarm validation / star shot | founders_vision.md, 16 April 2026 |

---

## Status labels used

- **CONJ-SS-11:** The cascade formula. Status: conjecture pending rigorous derivation of $(A-1)$ and Pauli coefficient.
- **PROP-SS-5-2:** Base-to-base predominant over vertex-to-vertex. Status: proposition (supported by three empirical indicators).
- **PROP-SS-5-3:** ${}^5$He, ${}^5$Li, ${}^8$Be unbound by closed-polytope gap. Status: proposition (confirmed empirically).
- **CONJ-SS-10 (superseded):** The v0.1 deuteron single-bond formula, now recovered as A=2 special case of CONJ-SS-11.
- **OPEN-SS-10:** Nuclear binding V(r). Status: resolved at A=2,3,4 for integrated binding; full V(r) shape still open.
- **OPEN-SS-17:** Light-nuclei curve. Status: partially resolved by SS-5 v0.2.
- **OPEN-SS-18 (NEW):** Heavy-nuclei alpha-cluster regime A≥6.
- **OPEN-SS-19 (NEW):** Rigorous derivation of $(A-1)$ and Pauli coefficient.
