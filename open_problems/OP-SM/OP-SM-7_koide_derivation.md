# OP-SM-7: Derive K = 2/3 (Koide Relation) from CPP First Principles

**Priority:** HIGH  
**Status:** PARTIAL — K3 spectral theorem proved given two postulates (OP-SM-7a, 7b open)  
**Session evidence:** K3 spectral theorem, 24 March 2026  
**Theorem document:** `k3_spectral_theorem.tex`  
**Last updated:** 24 March 2026

---

## What Is Now Proved

**Theorem K3 (24 March 2026):** Under Postulates ZBW-1 and H-1, the Koide
relation $K = 2/3$ follows from the adjacency spectrum of the colour cage base
graph $K_3$.

**The four-step proof:**

1. **K3 adjacency spectrum** (computed exactly):
   $\lambda_{\max} = 2$ (bonding, once), $\lambda_{\min} = -1$ (antibonding, twice)

2. **Spectral ratio → ρ:**
   $\rho^2 = \lambda_{\max}/|\lambda_{\min}| = 2/1 = 2 \Rightarrow \rho = \sqrt{2}$

3. **C3 + ρ = √2 → K = 2/3** (algebraic identity, proved 24 March 2026)

4. **Consequence:** $\Sigma m_i/(\Sigma\sqrt{m_i})^2 = 2/3$ exactly

**Corollary:** Both charge quantisation ($\delta = 1/3$, Theorem 1) and
the Koide formula ($K = 2/3$, Theorem K3) arise from the same K3 structure.
$\delta = 1/3$ uses the combinatorial structure; $K = 2/3$ uses the spectral
structure. The two deepest CPP lepton results share one geometric source.

---

## The Two Postulates (open sub-problems)

**OP-SM-7a — Postulate H-1:** Prove that the ZBW Hamiltonian on the colour
cage base is $\hat{H}_{ZBW} = \hbar\omega_0 A_{K_3}$.

Physical motivation: the ZBW orbital hops between colour vertices via SSV
gradient interactions (the same mechanism giving the Gell-Mann generators).
All three K3 edges are equivalent by C3 symmetry. A derivation from the CPP
interaction rules would close this.

**OP-SM-7b — Postulate ZBW-1:** Prove that lepton mass scales as squared ZBW
amplitude: $m_i \propto |\psi_i|^2$.

Physical motivation: each CP processes DI-bit flows at rate $\propto |\psi_i|^2$.
Mass = stored ZBW energy $\propto$ DI-bit flow rate. This is the lepton-sector
Born rule — likely derivable from OP-QM-1 (Born rule) specialised to the ZBW
mass context.

**OP-SM-7c — Phase θ:** Derive the Koide phase $\theta$ exactly from the SSV
coupling. Currently: $\theta \approx 3\pi/4 - (5/4)\,\text{sea}^2$ to 0.0016%
(coefficient 5/4 fitted, not derived).

---

## What Remains Open

- Individual masses $m_\mu$, $m_\tau$ (need θ and scale A = √m_e)
- OP-SM-7a, 7b, 7c (the two postulates and the phase)

---

## Feeds Into

- Lepton series paper (OP-SM-7a+7b close the derivation chain)
- OP-G-1 (three generations — K3 structure connects generation count to Koide)
- OP-QM-1 (Born rule — ZBW-1 is a special case of the Born rule)
