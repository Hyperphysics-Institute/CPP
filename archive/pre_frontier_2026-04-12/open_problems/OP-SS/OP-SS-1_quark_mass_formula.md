# OP-SS-1: Quark Mass Formula $M_q(n_\text{layers})$ from sea\_strength

**Priority:** HIGHEST  
**Status:** PARTIAL — Theorems 2 and 3 proved (structural + scale);
full ZBW composition corrections remain semi-empirical  
**Solved in:** `op_ss9_ss1_theorems.tex` Theorems 2–3  
**Series:** SS\#1, SS\#5  
**Last updated:** 23 March 2026

---

## What Is Now Proved

**Theorem 2 (Cage ordering, SS-1a) — SOLVED:**
$$M_q(n) = M_{\rm inner} + E_{\rm eDP}
\sum_{l=1}^{n} N_l\,\phi^{3(l-1)}$$
- $N_l = 4, 12, 20, 60$ from 600-cell shell geometry (fixed)
- $\phi^{3(l-1)}$ from golden-ratio shell volume scaling (derived)
- Strict ordering $M_q(0) < M_q(1) < \cdots < M_q(4)$ proved
- Direction $m_u < m_d$ proved from SSV polarity asymmetry

**Theorem 3 (Energy scale, SS-1b) — NEAR-SOLVED:**
$$E_{\rm eDP} = \frac{{\rm sea\_strength} \cdot \hbar c}{\phi^2 \cdot r_{\rm conf}}
\approx 83.9\ {\rm MeV}$$
- sea\_strength is now **derived** from $\alpha_{\rm geom}$ (OP-SM-1 solved)
- $r_{\rm conf}$ is the one remaining input (awaits OP-SS-5)
- 4.7% residual from notebook value 88 MeV (within MC precision)

**Lepton series template established:** equation (6) of theorems document.

---

## What Remains Open

The ZBW composition gradient ($\tau = 1/\ln\phi^2$) and inter-layer bonding
corrections explain why charm/strange = 13.6 (not 6 from the structural
formula). These are semi-empirical in Paper 2 and require first-principles
derivation from the 600-cell SSV dynamics. This is the full OP-SS-1 problem
and connects to OP-SS-3 (chiral condensate).

---

## Feeds Into

- Lepton series (template now established) ✓
- OP-SS-2 (three generations)
- OP-SS-3 (chiral condensate — light quark masses)
- OP-G-1 (lepton mass formula by analogy) ✓ template ready

---

## Statement

Express all six constituent quark masses as a single formula:

$$M_q(n) = F\!\left(n,\ \text{sea\_strength},\ \phi,\ \{E_{\mathrm{DP}}\}\right)$$

where $n$ is the cage depth from SS\#1 Table 1 (up/down: $n=0$;
strange: $n=1$; charm: $n=2$; bottom: $n=3$; top: $n=4$) and all
inputs are derivable from CPP primitives.  No quark mass may be a
free parameter.

---

## What is Known

### 1. The cage-depth table (SS#1, Thomas)

| Quark | $n$ | Charge | Structure |
|---|---|---|---|
| up | 0 | +2/3 | bare +qCP |
| down | 0 | −1/3 | bare −qCP |
| strange | 1 | −1/3 | tetrahedral cage |
| charm | 2 | +2/3 | tetra + icosa |
| bottom | 3 | −1/3 | tetra + icosa + dodeca |
| top | 4 | +2/3 | tetra + icosa + dodeca + C₆₀ |

### 2. The volume-scaling mechanism (`cpp_benchmark` v12, Stage 14)

$$M_q(n) \approx M_\text{inner} + \sum_{l=1}^{n} E_\text{DP}(l) \cdot \phi^{3(l-1)}$$

The $\phi^{3(l-1)}$ factor is the 3D cage-shell volume scaling.  Each
additional cage layer multiplies the mass contribution by $\phi^3
\approx 4.236$.  This gives ratios spanning $\sim 2$ orders of
magnitude over 4 layers — closer to the observed span than the
additive integral approach but still short of the $1:78\,000$
ratio $m_u : m_t$.

### 3. The DP binding energy hierarchy (`cpp_benchmark` v12)

$$E_{\mathrm{eDP}} : E_{\mathrm{hDP}} : E_{\mathrm{qDP}} = 1 : \sqrt{3} : 3 \approx 88 : 152 : 264\ \text{MeV}$$

Ratios exact.  Inner layers are qDP-dominated; outer layers shift to
hDP-dominated.  The composition gradient is described by:

$$\tau = \frac{1}{\ln\phi^2} \approx 1.039$$

(derived from SSV integral, not fitted).

### 4. The inner SSV mechanism for $m_u < m_d$ (`nested_cage_masses` v8, Stage 12)

The bare up quark's +qCP creates stronger SSV stress at the ZBW
orbital radius, reducing the hDP overlap to $\delta_\text{up} \approx
0.95 \times \frac{1}{3}$ vs.\ $\delta_\text{down} \approx \frac{1}{3}$.
The direction $m_u < m_d$ is geometric, not fitted.

### 5. Current quantitative accuracy

With consistent MeV units and $\phi^{3(l-1)}$ volume scaling:

| Quark | CPP (MeV) | PDG (MeV) | Error |
|---|---|---|---|
| strange | 223 | 93.5 | 139% |
| charm | 1052 | 1273 | 17% |
| bottom | 4350 | 4183 | 4% |
| top | 17720 | 172570 | 90% |

Bottom and charm are close.  Strange and top require additional physics.

---

## What Remains

### The kernel problem

The volume-scaling formula gives ratios $1 : 4.2 : 17.9 : 76 : 322$
across 4 cage layers.  The actual ratios are $1 : 44 : 577 : 1900 :
78527$.  The formula is too mild by a factor that grows with layer depth.

**Leading candidate:** ZBW frequency kernel.  If the mass contribution
per layer scales as $M_l \propto \hbar\omega_\text{ZBW}(l) \cdot
V_l$, and $\omega_\text{ZBW}(l) \propto 1/r_l \propto \phi^{-l/2}$
(cage radius grows as $\phi^{l/2}$), then:

$$M_l \propto \phi^{-l/2} \cdot \phi^{3(l-1)} = \phi^{5l/2 - 3}$$

This gives ratios $\phi^{5/2} \approx 4.06$ per layer — still not
enough.  The correct exponent of $\phi$ per layer is approximately
$\ln(44)/\ln(\phi) \approx 8$, suggesting $M_l \propto \phi^{8(l-1)}$
or equivalently $M_l \propto \phi^{n \cdot k}$ for $k \approx 8$.

### The top quark anomaly

The top quark (C₆₀ fourth cage, 60 vertices vs.\ 20 for dodecahedron)
requires a different mechanism.  The C₆₀ fullerene is not a Platonic
solid and its volume scaling is not $\phi^{3 \times 4} = \phi^{12}$.
Deriving the C₆₀ contribution separately and confirming $M_\text{top}
\approx 172.57$~GeV is a subproblem.

### Deriving $E_\text{eDP} = 88$~MeV

The base DP binding energy must be derived from sea\_strength and $l_P$:
$$E_\text{eDP} = f(\text{sea\_strength},\ l_P,\ \phi)$$
Once this is derived, the entire quark mass formula is parameter-free.

---

## Suggested Approach

1. Fit the exponent $k$ in $M_l \propto \phi^{k(l-1)}$ to the five
   quark masses (excluding top) and check if $k$ is a simple
   $\phi$-algebraic number.
2. Derive $E_\text{eDP}$ from the SSV field energy at the ZBW orbital
   radius: $E_\text{eDP} \sim \text{sea\_strength} \cdot \hbar c / r_\text{ZBW}$.
3. Handle the top quark C₆₀ cage geometry separately.
4. Verify that Thomas's 6-entry cage table (not 3 generation shells)
   is used throughout.

---

## Feeds Into

- OP-SS-2 (three generations — cage depth structure)
- OP-SS-3 (chiral condensate — light quark masses)
- OP-G-1 (lepton mass formula by analogy)
- Lepton series (as a template)
