# OP-QM-2: Rigorous Derivation of the Schrödinger Equation from PCD Discrete Updates

**Priority:** HIGH  
**Status:** OPEN — derivation sketched in QM#2; continuum limit not proved rigorously  
**Series:** QM#2 (Wave-Particle Duality)  
**Session evidence:** Born-rule audit (March 2026) — listed as "suggested, not proved"  
**Last updated:** 23 March 2026

---

## Statement

Prove that the Schrödinger equation:

$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$

is the *exact* continuum limit of the CPP lattice bit-diffusion master
equation as $\Delta t \to 0$, $\Delta s \to 0$, with the Hamiltonian
$\hat{H}$ arising entirely from SSV potentials on the 600-cell.

---

## What QM#2 Establishes

QM#2 presents the following argument:

**Step 1 — Wavefunction as bit density amplitude:**

$$\psi(r,t) \sim \sqrt{\rho_\text{bit}(r,t)}\, e^{i\phi(r,t)}$$

where $\rho_\text{bit}$ is the DI bit density and $\phi$ accumulates
from lattice edge angles.

**Step 2 — Master equation for bit density:**

$$\rho(r, t+\Delta t) = \rho(r,t) + \nabla \cdot [j - D\nabla\rho]$$

where $j$ is the net bit flux and $D$ is the diffusion coefficient
set by the ZBW step size and frequency.

**Step 3 — Continuum limit claim:**

As $\Delta t \to 0$, $\Delta s \to 0$ (with $\Delta s^2 / \Delta t =
\hbar/m$ held fixed), the master equation becomes:

$$i\hbar\frac{\partial\psi}{\partial t} = 
\left[-\frac{\hbar^2}{2m}\nabla^2 + V(r)\right]\psi$$

where $V(r)$ is the SSV potential at position $r$.

---

## Why the Derivation Is Not Yet Complete

The Born-rule audit flagged this derivation as "suggested rather than
proved" for three reasons:

**1. The continuum limit error bound is not controlled.**  
The transition from lattice to continuum requires showing that the
discretisation error $\varepsilon(\Delta t, \Delta s)$ goes to zero
uniformly.  For generic lattice diffusion this is non-trivial; on the
600-cell, the discrete symmetry group $[3,3,5]$ introduces
anisotropies that must be shown to vanish in the limit.

**2. The imaginary unit $i$ is not derived.**  
The Schrödinger equation is complex; the master equation for
$\rho_\text{bit}$ is real.  The appearance of $i$ requires the
introduction of the phase variable $\phi$.  QM#2 assumes
$\psi = \sqrt{\rho}\,e^{i\phi}$ but the equation of motion for
$\phi$ (the Hamilton-Jacobi equation in quantum form) is not derived
from the lattice dynamics — it is borrowed from the Madelung
decomposition.

**3. The Hamiltonian identification needs proof.**  
QM#2 asserts $V(r) =$ SSV potential, but the precise relationship
between the SSV field at a 600-cell vertex and the quantum mechanical
potential energy has not been derived.  This requires connecting the
CPP SSV field equations (from the SR series) to the potential
$V(r)$ in $\hat{H}$.

---

## What Remains

### Task 1 — Control the continuum limit

Show that the 600-cell discrete bit-diffusion equation converges to
the Schrödinger equation uniformly as $\Delta t, \Delta s \to 0$.
The key is the isotropy of the 600-cell at large scales: the 120-vertex
icosahedral symmetry group averages out lattice anisotropies for
wavelengths $\lambda \gg l_P$.

**Quantitative prediction to verify:** Discretisation corrections
should scale as $(\Delta s / \lambda)^2 \sim (l_P/\lambda)^2$, which
at $\lambda \sim 10^{-10}$~m (atomic scale) gives corrections of
order $10^{-50}$ — unobservably small.  At $\lambda \sim 10^{-17}$~m
(ZBW scale), corrections become $\mathcal{O}(1)$ — QM breaks down.

### Task 2 — Derive the phase equation from PCD dynamics

Show that the phase $\phi(r,t)$ obeys the quantum Hamilton-Jacobi
equation from the PCD cycle.  The key claim: during each PCD tick,
a CP's phase advances by an amount proportional to the net SSV field
energy in its neighbourhood, giving:

$$\frac{\partial\phi}{\partial t} = -\frac{E_\text{SSV}}{\hbar}$$

which is the CPP equivalent of $\partial_t\phi = -E/\hbar$.

### Task 3 — Identify SSV potential with quantum potential

Show $V(r) = V_\text{SSV}(r)$ where:
$$V_\text{SSV}(r) = \text{sea\_strength} \times S(r) \times \hbar c / l_P$$

and $S(r)$ is the dimensionless SSV stress field from the CPP field
equations.

---

## Falsifiable Prediction (from the derivation)

The discrete corrections to the Schrödinger equation produce energy
level shifts:

$$\delta E_n \sim E_n \cdot \left(\frac{l_P}{\lambda_n}\right)^2$$

For hydrogen-like atoms, $\lambda_n \sim n^2 a_0 \sim 10^{-10}$~m,
giving $\delta E_n \sim E_n \times 10^{-50}$ — well below current
experimental sensitivity.  However, at $n \sim 10^{10}$ (Rydberg
atoms with $\lambda \sim 10^{-3}$~cm), corrections become:

$$\delta E \sim E_n \times \left(\frac{l_P}{10^{-3}}\right)^2
\sim 10^{-62}\ \text{(still unmeasurable)}$$

The testable regime is at atomic clock frequencies ($\sim 10^{10}$~Hz),
where QM#2 predicts deviations $\sim \delta\nu/\nu \sim (l_P/c) \times
\nu \sim 10^{-43}$ per Hz — below any near-term measurement.  The
prediction is correct in sign and structure even if not yet
experimentally accessible.

---

## Prerequisites

- OP-QM-1 (Born rule — probability interpretation of $|\psi|^2$ needed
  for the continuum limit argument)
- OP-SD-1 (explicit $K_0$ — the bit-propagator determines $D$)

## Feeds Into

- OP-QM-3 (spin — the Pauli equation is the Schrödinger equation plus
  spin terms)
- OP-QM-7 (QFT — second quantization is built on the Schrödinger
  equation continuum limit)
- Atomic physics predictions (hydrogen spectrum from CPP)
