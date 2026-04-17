# Mechanism: SS-5 — Light-Nuclei Binding from the Open-Vertex Cascade

**Paper:** SS-5 v0.2
**Last updated:** 17 April 2026
**Document type:** Physical mechanism description for physicists

---

## One-sentence summary

Two nucleons bond base-to-base via three quark-quark DP chains across the triangular contact face, K$_3$-reduced to one collective pair quantum $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV; embedded in a closed A-nucleon polytope, each pair is reinforced by factor $(A-1)$, modified by standard Coulomb, Pauli penalty $M_0/\varphi^3$ per like-pair, and a closure bonus $M_0/\varphi$ at A=4 — yielding light-nuclei binding energies at $\leq 5.3\%$ error with zero parameters.

---

## The mechanism, step by step

### Step 1: Nucleon structure (inherited from SS-2)

Each nucleon is a hybrid tetrahedron. Proton base $\{u, u, d\}$ at three base vertices; open $+$ vertex opposite. Neutron base $\{d, d, u\}$ at three base vertices; open $-$ vertex opposite.

### Step 2: Base-to-base contact forms the np bond

Two nucleons approach so that their triangular quark bases face each other. Each of the three base-vertex pairs hosts quarks of opposite net charge: $(u,d), (u,d), (d,u)$ — all three electromagnetically attractive. A qDP chain forms at each pair. The open $+$ and $-$ vertices point outward, available for cascade bonding.

### Step 3: K$_3$ collective-mode reduction

The three qq-pair oscillators sit on a triangular face — a K$_3$ complete graph. By the same reduction pattern that gives single eigenvalues in SM-3, SM-6, SM-7, SM-8, SS-3, the three oscillators collectively support one binding mode at $\lambda_+ = +2$. The two $\lambda_- = -1$ eigenvalues are antibonding. Net binding per pair: $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV.

### Step 4: Cascade factor $(A-1)$

Each np pair in a closed A-nucleon polytope is reinforced by $A-1$ completing pathways through the remaining nucleons. A=2: factor 1. A=3: factor 2. A=4: factor 3.

### Step 5: Pauli penalty for like-nucleon pairs

Two protons or two neutrons share same open-vertex polarity; antisymmetrisation costs $M_0/\varphi^3 = 0.895$ MeV per like-pair.

### Step 6: Closure bonus at A=4

The closed tetrahedral polytope of four nucleons activates one additional collective mode, contributing one extra $B_{\text{pair}} = M_0/\varphi$.

### Step 7: Coulomb correction (standard EM)

$n_{pp} \cdot \alpha_{\text{em}} \hbar c / R$ with $R = 1.2 A^{1/3}$ fm.

---

## Why the cascade closes at A=4

Beyond A=4, there is no closed polytope on the 600-cell lattice at the nucleon-scale until the icosahedron at A=12. Consequence: ${}^5$He, ${}^5$Li, ${}^8$Be cannot use the cascade mechanism — they bind only at the constituent subsystem level. They are unbound by geometry.

Confirmed empirically:
- $S_n(^5$He$) = -0.89$ MeV
- $S_p(^5$Li$) = -1.97$ MeV
- $S_{^4\mathrm{He}}(^8$Be$) = -92$ keV (triple-alpha bottleneck)

---

## The cascade formula

$$B(A,Z) = (A-1) \cdot n_{np} \cdot \frac{M_0}{\varphi} - n_{pp} \cdot \frac{\alpha_{\text{em}} \hbar c}{1.2 A^{1/3}} - (n_{pp}+n_{nn}) \cdot \frac{M_0}{\varphi^3} + \delta_{A,4} \cdot \frac{M_0}{\varphi}$$

Numerical evaluation:

| Nucleus | Spine | Coulomb | Pauli | Closure | CPP | Measured | Error |
|---|---|---|---|---|---|---|---|
| d | 2.342 | 0.000 | 0.000 | 0.000 | **2.342** | 2.225 | +5.3% |
| ³H | 9.369 | 0.000 | 0.895 | 0.000 | **8.474** | 8.482 | **−0.09%** |
| ³He | 9.369 | 0.832 | 0.895 | 0.000 | **7.642** | 7.718 | −1.0% |
| ⁴He | 28.106 | 0.756 | 1.789 | 2.342 | **27.904** | 28.296 | −1.4% |

All values in MeV.

---

## Mathematical correspondence table

| Physical element | CPP quantity | Symbol | Value |
|---|---|---|---|
| Electron rest mass | Calibration | $m_e$ | 0.510999 MeV |
| 600-cell coordination | Axiom A2 | $z$ | 12 |
| Propagation efficiency | Axiom A5 | $\eta = 1/\varphi$ | 0.61803 |
| DP energy quantum | SM-8 | $M_0 = m_e z/\varphi$ | 3.790 MeV |
| **Pair binding** | **SS-5 v0.2** | $B_{\text{pair}} = M_0/\varphi$ | **2.342 MeV** |
| **Pauli penalty per like-pair** | **SS-5 v0.2** | $M_0/\varphi^3$ | **0.895 MeV** |
| **Closure bonus (A=4)** | **SS-5 v0.2** | $M_0/\varphi$ | **2.342 MeV** |
| Cascade factor | CONJ-SS-11 | $A-1$ | 1, 2, 3 at A=2,3,4 |
| Coulomb correction | Standard EM | $\alpha_{em}\hbar c/R$ | $R=1.2 A^{1/3}$ fm |

---

## Qualitative predictions (no additional calculation)

1. Nuclear chart begins at deuterium.
2. pp/nn near-threshold virtual states (K$_3$ charge misalignment + Coulomb).
3. Deuteron I=0, S=1 forced by base-alignment antisymmetry.
4. ⁴He most tightly bound light nucleus per nucleon (closure bonus).
5. ⁵He, ⁵Li, ⁸Be structurally unbound (no closed polytope).
6. Heavier nuclei reconfigure as alpha clusters (A≥6, OPEN-SS-18).

---

## Honest limitations

- Full V(r) shape not derived — only integrated binding at each A.
- $(A-1)$ multiplicity and Pauli $M_0/\varphi^3$ motivated but not rigorously derived (OPEN-SS-19).
- Magnetic moment and D-wave not treated in v0.2.
- Alpha-cluster regime A≥6 sketched only.

---

## Thomas's words (17 April 2026)

> "The net charge on the quark determines the attraction or repulsion between quarks... The base-to-base bonding leaves the open vertices available for vertex-to-vertex or vertex-to-base bonding with additional layers of protons or neutrons as the atomic number increases."

SS-5 v0.2 supplies the quantitative content.
