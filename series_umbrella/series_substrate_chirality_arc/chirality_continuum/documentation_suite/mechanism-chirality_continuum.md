# Mechanism: Chirality Continuum — Substrate Handle $\chi/6$ Propagation to Observable Layer 4 EFT

**Series:** Flagship paper (Chirality Continuum line)
**Last updated:** 20 May 2026 (Patch 0511 — chirality continuum v1.0 SHIPPED companion suite production)

This file describes the physical mechanism of the chirality continuum joint paper at a level intended for physicists who want intuition without re-reading the paper's full theorem chain. The polished derivations live in `chirality_continuum.tex` v1.0 SHIPPED §3 + §4 + §5; this file translates the derivations into mechanism language.

---

## Overview

The chirality continuum joint paper closes a single physical question across two sectors of the Standard Model:

> How does the substrate-level chirality magnitude $|M^{\text{sector}}| = \chi/6 \approx 0.0394$ — established at Layer 3 substrate-physics rigor in Capotauro v2.0 — propagate to observable phenomena at Standard Model accessible energy scales (electroweak scales for V–A coupling structure; thermodynamic scales for leptogenesis CP-asymmetry)?

The mechanism is a five-step physical chain:

1. **Substrate-level magnitude** $\chi/6$ exists on the 600-cell polytope at Layer 3.
2. **Block-spin renormalization** projects substrate-level structure to continuum-limit effective field theory at scales much larger than the polytope edge length.
3. **Magnitude inheritance** preserves $\chi/6$ at leading order via the topological-projection argument — the substrate-handle magnitude is a topological quantity protected from RG-flow renormalization.
4. **Sector-specific operator identification** maps the continuum operator $\mathcal{O}^{\text{eff,sector}}$ to (a) the V–A current operator $\bar{\psi}_L\gamma^\mu\psi_L$ in the SF-2 sector or (b) the chirality-asymmetric stabilization-energy operator $\Delta F^{qDP}$ in the SM-2 sector.
5. **Observable predictions** at electroweak scales (Michel $\rho = 3/4$ + 100% LH at massless helicity limit) + thermodynamic scales (leptogenesis CP-asymmetry $\Delta p_{LR} \approx 0.0394$).

The chirality continuum paper closes all five steps at theorem-level rigor (with the conditional-closure caveat that FI-CHIR-CONT-1 + FI-CHIR-CONT-2 remain Layer 2 inputs pending Q1$'$+Q1$'$.A Layer 3 promotion).

---

## Inputs and constants

The mechanism uses 15 foundational inputs (FI-CHIR-CONT-1 through -15) inherited from Capotauro v2.0 + SF-2 v1.0 + SM-2 v1.0:

| FI | Definition | Source |
|---|---|---|
| FI-CHIR-CONT-1 | Substrate primitive 4D direction $\hat{n}$ at vertex-aligned Reading C | Capotauro v2.0 §sec:primitive_direction + Finding C-W37 |
| FI-CHIR-CONT-2 | Substrate chirality magnitude $|\chi| = \varphi^{-3} \approx 0.236$ | Capotauro v2.0 §sec:chi_resolution + Finding C-W39 |
| FI-CHIR-CONT-3 | Substrate residual symmetry $H_3 = I_h$ at host vertex | Capotauro v2.0 §sec:stab_h_four |
| FI-CHIR-CONT-9 | Substrate-Locality Theorem | Capotauro v2.0 §sec:substrate_locality |
| FI-CHIR-CONT-10 | W-bracelet sector specialization | Capotauro v2.0 §sec:w_bracelet + THEO-SD-CHIR-1 |
| FI-CHIR-CONT-11 | SF-2 Yang-Mills $SU(2)_L \times U(1)_Y$ EFT framework | SF-2 v1.0 §sec:YM_EFT_thm |
| FI-CHIR-CONT-12 | Continuum-EFT $\gamma_5$ chirality-projection structure | Standard Dirac formalism + SF-2 v1.0 |
| FI-CHIR-CONT-13 | qDP/eDP sector specialization (Linear-ZBW + $D_{5d}$ + combined $CP$) | Capotauro v2.0 §sec:qdp + THEO-SD-CHIR-2 |
| FI-CHIR-CONT-14 | SM-2 effective free-energy / partition-function framework | SM-2 v1.0 §10 chiral-polarity-bias mechanism |
| FI-CHIR-CONT-15 | Continuum-EFT combined-$CP$-parity structure | SM-2 v1.0 §10 + Boltzmann-like thermodynamic distribution |

(Full FI inventory at `chirality_continuum.tex` §3.1 + §4.1 + §5.1.)

Five CPP axioms most load-bearing: AXIM-1 (CP existence; load-bearing for chirality operator), AXIM-2 (600-cell topology; load-bearing for polytope-geometric invariants), AXIM-3 (Dipole Sea / DI-bit propagation; load-bearing for continuum-EFT framework), AXIM-4 (SSV interaction / Nexus; load-bearing for Substrate-Locality Theorem), AXIM-7 (Substrate-stress; load-bearing for substrate primitive direction $\hat{n}$).

---

## Step-by-step derivation

### Step 1: Substrate-level magnitude $\chi/6$ exists at Layer 3

Capotauro v2.0 v1.0 SHIPPED (19 May 2026) closed three sector instantiations of the same magnitude $|M^{\text{sector}}| = \chi/6 \approx 0.0394$ at full Layer 3 rigor:

- $|M^{K3}| = \chi/6$ via THEO-CAP-1 (Composite Capotauro Wigner-Eckart Theorem) at K3-doublet sector
- $|M^W| = \chi/6$ via THEO-SD-CHIR-1 (W-Bracelet Sector Substrate Chirality Closure) at electroweak V–A sector
- $|M^{qDP}| = \chi/6$ via THEO-SD-CHIR-2 (qDP/eDP Sector Substrate Chirality Closure) at electromagnetic handedness sector

The unification at substrate level — three structurally distinct sector mechanisms producing identical numerical magnitude — is the **substrate-handle** that the chirality continuum paper propagates to observable scales.

### Step 2: Block-spin renormalization projects substrate to continuum

Wilson-Fisher block-spin renormalization at substrate cutoff $\Lambda_{\text{sub}} = \ell_{\text{edge}}^{-1}$ where $\ell_{\text{edge}}$ is the 600-cell polytope edge length. The projection map $\Phi$ (Definition 3.2 of joint paper) takes substrate-level structure $(G = I_h, \Gamma, \zeta^{\text{sector}}, \text{matter-doublet}, \hat{C}^{\text{sector}})$ to continuum-limit structure $(G^{\text{cont}}, \Gamma^{\text{cont}}, \zeta^{\text{cont,sector}}, \psi^{\text{eff}}, \mathcal{O}^{\text{eff,sector}})$.

The projection conditions (equivariance + block-spin commutativity + well-defined continuum-limit existence) ensure that group-theoretic structure is preserved under projection: $\Gamma \to \Gamma^{\text{cont}}$ isomorphically; $\mathbb{Z}_2$ generator inheritance $\zeta \to \zeta^{\text{cont}}$; irrep inheritance preserving dimension + $\zeta$-parity content (Lemma 4.1 = THEO-CHIR-CONT-1.1; Symmetry-Content Preservation under $\Phi$).

The deep-infrared regime characterizing the chirality continuum paper's regime of interest is $a/L = \ell_{\text{edge}} \mu_{\text{obs}}^{\text{sector}} \sim 10^{-18}$ at SF-2 electroweak scale ($\mu_{\text{obs}}^W \sim m_W \sim 80$ GeV) and similarly small at SM-2 thermodynamic scale.

### Step 3: Magnitude inheritance via topological-projection argument

The key recognition. Magnitude inheritance — $|M^{\text{eff}}| = \chi/6$ at the continuum-EFT level — is established at leading order in $a/L$ by Theorem 15.3.1 (= THEO-CHIR-CONT-1.3; Magnitude Inheritance via Topological Projection).

The argument: the substrate magnitude $\chi/6 = \varphi^{-3}/6$ is a **topological substrate quantity** (Definition 15.1.1). Its value depends entirely on combinatorial-geometric structure:
- $|\chi| = \varphi^{-3}$ derived from 600-cell polytope edge-length ratios via perturbative-distance-ratio constraint (no substrate-field-theoretic dynamics; Claim 15.1.2)
- Cage-shell factor $1/6 = d_\Gamma/V_{\text{cage}} = 2/12$ derived from integer-valued representation-theoretic + polytope-topological invariants (Claim 15.2.1)

Topological substrate quantities are preserved exactly under continuum-limit projection $\Phi$ at leading order, by the standard QFT protection-of-topological-quantities principle:
- Anomaly coefficients $1/(16\pi^2)$ exact at all loop orders per Adler-Bardeen
- Topological charges $n \in \mathbb{Z}$ in $\theta$-vacuum sectors
- Chern-Simons levels $k \in \mathbb{Z}$
- Atiyah-Singer index theorem contributions
- Discrete symmetry parities $\mathbb{Z}_2$-valued
- Polytope-geometric invariants

The substrate-handle magnitude $\chi/6$ inherits the same protection. There is no RG-flow renormalization correction at any scale between $\Lambda_{\text{sub}}$ and $\mu_{\text{obs}}^{\text{sector}}$. The magnitude propagates from substrate to observable at leading order.

**This is the mechanism by which the substrate-level theorem produces an observable-level prediction at zero free parameters.**

Sub-leading corrections at order $(a/L)^n$ for $n \geq 1$ exist but are suppressed by deep-infrared regime — $\sim 10^{-18}$ at SF-2 electroweak scale + similarly small at SM-2 thermodynamic scale. Structural upper bound $\chi^2 \approx 0.056$ from substrate-handle natural scale; actual sub-leading corrections vastly smaller.

### Step 4: Sector-specific operator identification

The continuum operator $\mathcal{O}^{\text{eff,sector}} = \Phi_*\hat{C}^{\text{sector}}$ is identified sector-specifically.

#### SF-2 W-bracelet sector → V–A current operator

Three structural identifications close the SF-2 sector at Theorem 4.2 = THEO-CHIR-CONT-2:

- **$\zeta^{\text{cont,W}} \leftrightarrow \gamma_5$**: The W-bracelet's $\mathbb{Z}_2$ generator $\zeta^W = r^3$ (icosahedral-center inversion in 4D ambient with linear part $-I$) projects to the continuum chirality-flipping involution $\gamma_5$, matching its $\mathbb{Z}_2$ structure $\gamma_5^2 = 1$ and chirality-flipping action $\gamma_5\psi_L = -\psi_L, \gamma_5\psi_R = +\psi_R$.

- **Matter-doublet** $\{|\psi^{\text{eff}}_+\rangle, |\psi^{\text{eff}}_-\rangle\} \leftrightarrow \{\psi_R, \psi_L\}$: The substrate matter-doublet basis with opposite-$\zeta^W$-parity projects to Dirac-spinor basis with opposite-$\gamma_5$-parity (right-handed + left-handed Weyl spinors).

- **Operator** $\mathcal{O}^{\text{eff,W}} \leftrightarrow \bar{\psi}_L\gamma^\mu\psi_L = \frac{1}{2}\bar{\psi}\gamma^\mu(1-\gamma_5)\psi$: The unique $\gamma_5$-ODD vector operator with non-vanishing matrix element between opposite-$\gamma_5$-parity matter-doublet, by Theorem 4.2 + Yang-Mills EFT framework.

The pure-V–A coupling structure emerges with $g^V_{LL} = 1$ in the general ten-coupling parametrization; scalar + tensor + right-handed-chirality vector couplings excluded.

#### SM-2 qDP/eDP sector → chirality-asymmetric stabilization-energy operator

Three structural identifications close the SM-2 sector at Theorem 5.5 = THEO-CHIR-CONT-3:

- **$\zeta^{\text{cont,qDP}} \leftrightarrow$ combined $CP$**: The qDP/eDP sector's $\zeta^{qDP}$ is the combined $CP$ operation (host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip); projects to the continuum chirality-flipping involution combining the same three flips on continuum Linear-ZBW configurations.

- **Matter-doublet** $\{|\Psi_-^{qDP,(1)}\rangle, |\Psi_-^{qDP,(2)}\rangle\} \leftrightarrow \{|\text{LZBW},+\rangle, |\text{LZBW},-\rangle\}$: Linear-ZBW chirality-eigenstate pair on opposite-sign qCP centers with combined-$CP$-EVEN positive-chirality + combined-$CP$-ODD negative-chirality.

- **Operator** $\mathcal{O}^{\text{eff,qDP}} \leftrightarrow \Delta F^{qDP} = F[\text{LZBW},+] - F[\text{LZBW},-]$: The unique combined-$CP$-ODD scalar operator with non-vanishing matrix element via effective free-energy framework.

The chirality-asymmetric stabilization-energy structure emerges; combined-$CP$ involution + Boltzmann-like thermodynamic distribution structure.

### Step 5: Observable predictions

At electroweak scales (SF-2 sector via THEO-CHIR-CONT-2):

- **Michel parameter $\rho = 3/4$** at finite mass via standard V–A four-fermion kinematics; one-loop SM radiative correction $\delta\rho^{\text{QED}} = +1.1 \times 10^{-4}$ preserves V–A structure; PDG 2024 $\rho^{\text{obs}} = 0.7497 \pm 0.0010$ within $0.3\sigma$.

- **100% LH at massless helicity limit** via chirality-helicity coincidence $P_L^{\text{helicity}}(v) = (1+v)/2 \to 1$ as $m_\psi/E_\psi \to 0$; multi-sector validation (Goldhaber 1958, Wu 1957, LEP $\tau$-polarization, LHC top).

At thermodynamic scales (SM-2 sector via THEO-CHIR-CONT-3):

- **Leptogenesis CP-asymmetry $\Delta p_{LR} \approx 0.0394$** via Boltzmann-like thermodynamic distribution $N[\text{LZBW},-]/N[\text{LZBW},+] = \exp(\Delta F^{qDP}/(k_B T))$ + tanh kinematics; empirical anchor $\Delta p_{LR}^{\text{obs}} \sim 0.04$ from BAU back-derivation (Davidson, Nardi, Nir 2008 Physics Reports 466, 105); **match within 2%**.

The same primary observable — leptogenesis CP-asymmetry $\Delta p_{LR}$ — simultaneously validates both Layer 4 closures via Threshold (C) of Capotauro Falsifier 6. This is the cross-sector convergence at observable scale framed at §6.5 as structural prediction of the joint-paper format.

---

## Mathematical correspondence table

| Physics claim | Equation | Paper section |
|---|---|---|
| Substrate magnitude $\|M^{\text{sub}}\| = \chi/6$ on three sectors | $\|M^{K3}\| = \|M^W\| = \|M^{qDP}\| = \varphi^{-3}/6$ | §3 (Capotauro v2.0 inherited) |
| Continuum-limit projection map | $\Phi: G \supset \Gamma \supset \zeta \to G^{\text{cont}} \supset \Gamma^{\text{cont}} \supset \zeta^{\text{cont}}$ | §3.2 (Definition 3.2) |
| Magnitude inheritance | $\|M^{\text{eff}}\| = \chi/6$ at leading order in $a/L$ | §3.3 (Theorem 3.3 = THEO-CHIR-CONT-1.3) |
| V–A operator identification | $\mathcal{O}^{\text{eff,W}} = \bar{\psi}_L\gamma^\mu\psi_L$ | §4 (Theorem 4.2 = THEO-CHIR-CONT-2) |
| Michel parameter | $\rho_{\text{V-A}}^{\text{tree}} = 3/4 = 0.7500$ | §4.3 |
| Massless helicity limit | $P_L^{\text{helicity}}(v) \to 1$ as $m/E \to 0$ | §4.4 |
| Chiral-polarity-bias operator | $\mathcal{O}^{\text{eff,qDP}} = \Delta F^{qDP}$ | §5 (Theorem 5.5 = THEO-CHIR-CONT-3) |
| Leptogenesis CP-asymmetry | $\Delta p_{LR} = \tanh(\Delta F^{qDP}/(2 k_B T)) \approx \chi/6$ | §5.5 |
| Cross-sector convergence at observable scale | $\Delta p_{LR}^{\text{obs}} \sim 0.04$ within 2\% of $\chi/6$ via THEO-CHIR-CONT-2 + -3 | §6.5 |
| Capotauro Falsifier 6 Threshold (A) | $\|\rho^{\text{obs}} - 3/4\| > 3 \times 10^{-3}$ | §4 + §9.4 |
| Capotauro Falsifier 6 Threshold (B) | $\|a_{\text{V+A}}\|^2 > 3 \times 10^{-2}$ | §4 + §9.4 |
| Capotauro Falsifier 6 Threshold (C) | $\|\Delta p_{LR}^{\text{obs}} - 0.0394\| > 0.015$ | §5 + §6.5 + §9.4 |

---

## Failure modes

The mechanism could fail at any of the five steps. Failures cascade:

| Step | Failure mode | Cascade |
|---|---|---|
| 1 | Substrate magnitude $\chi/6$ not universal across sectors | Capotauro v2.0 falsified; chirality continuum's bridge inapplicable |
| 2 | Continuum-limit projection $\Phi$ not well-defined | Lemma 4.1 fails; bridge theorem inapplicable |
| 3 | Magnitude not preserved under $\Phi$ | Theorem 15.3.1 fails; substrate handle does not propagate; predictions deviate at non-trivial RG-flow-scale-dependent amounts |
| 4 | Sector-specific operator identification wrong | One or both sector theorems fail; cross-sector convergence at observable scale would not hold |
| 5 | Observable predictions deviate at $> 3\sigma$ at any of three thresholds | Falsifier 6 activates; chirality continuum mechanism falsified |

The observational threshold for falsification is currently at $\sim 0.5$–$3 \times 10^{-3}$ across the three thresholds (combined LEP + LHC + PDG + BAU back-derivation precision). Future-collider precision could push to $\sim 10^{-3}$ to $\sim 10^{-4}$ by 2030–2040+. The structural upper bound from $\chi^2 \approx 0.056$ is vastly above the actual sub-leading $\sim 10^{-18}$ at SF-2 electroweak scale; precision improvements pushing toward the structural upper bound would surface theoretical-content questions about substrate-handle inheritance.

Cross-references: §9.4 of `chirality_continuum.tex` (failure modes + falsifiability commitments); `problem_histories/PH-OPEN-FP-SF-2-CHIR.md` (closure declaration + caveat that closure is conditional on FI-CHIR-CONT-1/2 future-window).

---

## Why the mechanism works

Three structural features make the chirality continuum mechanism produce a zero-parameter prediction at observable scale:

1. **Substrate-level unification across three sector instantiations** (Capotauro v2.0). The universal magnitude $\chi/6$ is not sector-dependent at substrate level — three structurally distinct sector mechanisms produce identical numerical magnitude.

2. **Topological-projection argument** (THEO-CHIR-CONT-1.3). The substrate magnitude is a topological substrate quantity, preserved exactly under continuum-limit projection at leading order via standard QFT protection-of-topological-quantities principle.

3. **Cross-sector convergence at observable scale** (§6.5). The same primary observable validates both sector-specific Layer 4 closures, providing structural redundancy: a single empirical anchor tests two independent theorem chains.

The mechanism's strength is its insensitivity to RG-flow scale + sector-specific details (the bridge theorem is sector-agnostic) + cross-sector consistency (two physical channels converging on the same numerical prediction). Its weakness is the conditional-closure caveat: FI-CHIR-CONT-1 (substrate primitive $\hat{n}$) + FI-CHIR-CONT-2 ($|\chi| = \varphi^{-3}$) remain Layer 2 inputs pending Q1$'$+Q1$'$.A Layer 3 promotion programme. The dynamical-substrate-law gate is the defining next programme gate identified by all three external reviewers at v1.0 SHIP.
