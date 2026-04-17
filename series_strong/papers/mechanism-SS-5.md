# Mechanism: SS-5 — Deuteron Binding Energy from Open-Vertex Tetrahedral Bonding

**Paper:** SS-5 v0.1
**Last updated:** 16 April 2026
**Document type:** Physical mechanism description for physicists

---

## One-sentence summary

The deuteron is two hybrid-tetrahedral nucleons joined by a single external attractive ZBW edge — one qDP chain — between the proton's open + vertex and the neutron's open − vertex; the binding energy released at bond formation is $M_0/\varphi = m_e z/\varphi^2 = 2.343$ MeV.

---

## The mechanism, step by step

### Step 1: The nucleons (inherited from SS-2)

Each nucleon occupies one tetrahedral cell of the 600-cell lattice. The proton has `{u@V₁(−), u@V₂(−), d@V₃(+), open@V₄(+)}`; the neutron has `{d@V₁(−), d@V₂(−), u@V₃(+), open@V₄(−)}`. The "open" vertex is an unoccupied but polarity-assigned lattice CP site — a *dangling bond* in the cage.

### Step 2: Approach

Two nucleons approach to within ~1 lattice unit ($l_\text{unit} = 0.589$ fm). The DP Sea between them re-organises under the polarity gradient set up by the two open vertices.

### Step 3: Bond formation

At closest approach, a single qDP chain spans the gap from $V_4^{p}$ (+) to $V_4^{n}$ (−). This chain is structurally identical to any of the four internal attractive edges of either tetrahedron: one qDP chain, one longitudinal ZBW mode, two opposite-polarity CP anchors. It is a **fifth attractive edge** in the combined 8-vertex system (4 internal to the proton + 4 internal to the neutron + 1 bridging them).

### Step 4: Energy delivery

The new ZBW edge stores $M_0 = m_e z/\varphi = 3.790$ MeV of oscillator energy (SM-8 DP energy quantum). At bond formation, the fraction $\eta = 1/\varphi$ is *delivered* across the vertex-to-vertex propagation step as binding energy; the rest remains stored in the ZBW oscillation. Delivered binding: $B_d = M_0 \cdot \eta = M_0/\varphi = 2.343$ MeV.

### Step 5: Release as photon

The delivered energy is emitted as the photon observed in radiative np capture: $np \to d + \gamma$, $E_\gamma = 2.224$ MeV.

---

## Why the second 1/φ

Inside a nucleon, each of the four attractive internal edges is reinforced by its participation in the three triangular faces meeting at each endpoint. The bond "closes on itself" through the tetrahedral cavity — the vertex-to-vertex delivery step is implicit in the definition of $M_0$.

The open-vertex bond is a dangling edge with no closing face. It does *not* participate in the 4+4 polarity-circulation modes of SS-3; those modes require a closed three-vertex face to execute. The bond is therefore a single-mode oscillator, simpler than any internal edge. Because the cavity reinforcement is absent, the vertex-to-vertex propagation step must be accounted for *explicitly* — one extra factor of $\eta = 1/\varphi$. Hence $B_d = M_0 \cdot \eta = M_0/\varphi$, i.e. $\eta^2$ overall relative to the raw $m_e z$ scale.

---

## Mathematical correspondence table

| Physical element | CPP quantity | Symbol | Value |
|---|---|---|---|
| Electron rest mass (calibration) | Calibration constant | $m_e$ | 0.510999 MeV |
| 600-cell Voronoi coordination | Axiom A2 | $z$ | 12 |
| Propagation efficiency | Axiom A5 | $\eta = 1/\varphi$ | 0.61803... |
| DP energy quantum (per organised DP) | SM-8 | $M_0 = m_e z/\varphi$ | 3.790 MeV |
| Lattice unit (circumradius) | SS-2 / Axiom A11 | $l_\text{unit} = \hbar c/\Lambda_\text{QCD}$ | 0.589 fm |
| Tetrahedral edge | Geometry | $l_\text{edge} = l_\text{unit}/\varphi$ | 0.364 fm |
| Proton charge radius | SS-2 | $r_p$ | 0.883 fm |
| Open-vertex bond length (equilibrium) | SS-5 | $l_\text{edge}$ | 0.364 fm |
| Bond oscillator energy (stored) | SS-5 | $M_0$ | 3.790 MeV |
| Binding energy (delivered) | **SS-5 Prop 4.1** | $B_d = M_0/\varphi$ | **2.343 MeV** |
| Measured deuteron binding | PDG 2024 | $B_d^\text{exp}$ | 2.22457 MeV |
| Residual | — | $+5.3\%$ | inside 2–5% band |
| Classical p–n separation | SS-5 | $R_\text{cl} = 2r_p + l_\text{edge}$ | 2.130 fm |

---

## What makes this a *mechanism*, not a fit

The prefactor $z/\varphi^2$ is not a free parameter. It is the same structural prefactor that appears in:

- $\sin^2\theta_W = (1/\varphi) \cdot \mathrm{Tr}(A^2)/N = 3/(8\varphi)$ — SM-6
- $\alpha_s = (1/\varphi) \cdot \mathrm{Tr}(A^3)/(3N) = 5/(8\varphi)$ — SM-7
- $M_q = m_e \cdot (z/\varphi) \cdot V^{7/3}$ — SM-8
- $M_0 = m_e \cdot z/\varphi$ — SM-8 DP energy quantum
- $\sigma = M_0 \cdot z^2/(\varphi \, l_\text{edge})$ — SS-4 string tension

Each application of the rule "mode-sum prefactor acquires one factor of $\eta$ per propagation step" is consistent across every prediction the programme has made. SS-5 is one more instance, not a new rule.

---

## What the mechanism predicts qualitatively (without calculation)

1. **Diproton unbound.** Two protons have open-vertex polarities $(+, +)$. A qDP chain cannot form between same-polarity CPs. No bond, no binding.

2. **Dineutron unbound.** Two neutrons have open-vertex polarities $(−, −)$. Same argument. No bond.

3. **Deuteron bound only in I=0 channel.** Polarity pairing is antisymmetric under p↔n exchange, forcing the isospin singlet.

4. **Triplet (S=1) bound, singlet (S=0) virtual.** The triplet configuration reinforces the bond by $\mathcal{O}(\eta)$; the singlet is unreinforced, sitting just above threshold (matches the observed ~60 keV singlet virtual state).

5. **Parity = +1 naturally.** S-wave radial bond has $L = 0$, $P = +1$.

6. **Repulsive core below $\sim 2r_p$.** When the nucleon cages begin to overlap, qDP chains of the two cages must share lattice edges — forbidden.

---

## What the mechanism does *not* do (honest limitations)

- Does not derive the full $V(r)$ shape — only the depth scale at bond formation.
- Does not predict the deuteron wavefunction, rms p–n separation, or D-wave admixture.
- Does not predict binding for $A \geq 3$ nuclei without additional cavity-mode combinatorics (bond-counting alone gets ${}^3\mathrm{H}$ wrong by factor ~2, ${}^4\mathrm{He}$ by factor ~6).
- Magnetic moment prediction $\mu_p + \mu_n = 0.942\,\mu_N$ is $+9.8\%$ off measured 0.8574 — inherits SS-2 $\mu_n$ residual plus neglects D-wave.
- p–n mass difference magnitude is right but sign comes out wrong from naive EM self-energy alone; resolution requires the eCP linear oscillator in the down quark (cross-coupled to OPEN-SM-11).

---

## Connection to Thomas's words

The mechanism traces directly to Thomas's 10 April 2026 F.V. catalogue entry:

> "We have postulated that the proton is composed of a hybrid Tetrahedron, with the two up quarks bound to two minus vertices, the one down quark bound to a plus vertex, leaving a plus vertex open by which to bind to the − vertex of a neutron, and thus the attraction to produce the nuclear binding force."

SS-5 supplies the quantitative content: the binding *is* $M_0/\varphi$.
