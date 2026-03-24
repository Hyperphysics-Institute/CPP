# OP-SM-7: Derive K = 2/3 (Koide Relation) from CPP First Principles

**Priority:** HIGH — empirically exact to 11 ppm; no CPP derivation exists  
**Status:** OPEN — algebraic theorem (K=2/3 ↔ ρ=√2) proved; physical origin unknown  
**Session evidence:** Lorentz-ZBW analysis, 24 March 2026  
**Last updated:** 24 March 2026

---

## Statement

Prove from CPP dynamics that the three charged lepton masses satisfy:

$$K \equiv \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

exactly (observed to 11 ppm: $K_{\rm obs} = 0.66665909$).

---

## What Is Known

**Algebraic theorem (proved this session):**
In the parametrisation $m_i = \gamma_0(1 + \rho\cos\phi_i)^2 m_{\rm base}$
with C3-symmetric phases $\phi_i = \theta + 2\pi i/3$:

$$K = \frac{1 + \rho^2/2}{3} \implies K = \frac{2}{3} \Leftrightarrow \rho = \sqrt{2}$$

This reduces the Koide problem to: **why does $\rho = \sqrt{2}$?**

**Critical point structure:**
At $(\rho, \theta) = (\sqrt{2}, 3\pi/4)$, the electron mode satisfies
$(1 + \sqrt{2}\cos(3\pi/4)) = 0$, so $m_e = 0$. The electron is the
lightest lepton because its ZBW mode is closest to this zero-mass
critical point.

**Phase observations (not derivations):**
- $\theta_{\rm Koide} \approx (1-\delta)\arccos(-1/3) + \delta\pi$
  to 0.19% ($\delta = 1/3$ from Theorem 1)
- $\theta_{\rm Koide} \approx 3\pi/4 - (5/4)\,\text{sea}^2$
  to 0.0016% (coefficient 5/4 is fitted, not derived)

---

## Why This Is Hard

The Koide formula $K = 2/3$ is exact to 11 ppm — one of the most
precisely satisfied unexplained relations in particle physics.
Any CPP derivation must explain:

1. Why the three lepton ZBW modes have the *specific* phase
   separation $2\pi/3$ (C3 symmetry — this comes from the cage base,
   but needs to be connected to the mass generation mechanism).

2. Why the Lorentz modulation depth $\rho$ takes the value $\sqrt{2}$
   and not some other number.

3. Why the ZBW energy of the electron mode is proportional to
   $(1 + \sqrt{2}\cos\theta)^2$ rather than some other functional form.

---

## Candidate Mechanisms

**A. Critical-point selection:**
The system sits at the maximum $\rho$ consistent with all three modes
having positive-definite mass. At $\rho = \sqrt{2}$ and $\theta$ slightly
less than $3\pi/4$, the electron is marginally bound. This selects
$\rho = \sqrt{2}$ as the stability boundary.

**B. Holographic bound:**
The $1/2$ in $(1 + \rho^2/2)/3 = 2/3$ may come from the Koide circle
living on a 2-sphere surface (dimension 2, not 3), giving a factor of
$2/(2+1) = 2/3$. The 600-cell's S³ geometry might enforce this.

**C. ZBW phase averaging:**
The $\rho^2/2$ comes from $\langle\cos^2\phi\rangle = 1/2$ over C3 angles.
If the ZBW wavefunction samples all three modes equally, equipartition
gives $K = 1/3 + (1/2)\rho^2/3$. Setting $\rho = \sqrt{2}$ gives $K = 2/3$.
The question becomes: what forces $\rho = \sqrt{2}$?

---

## Feeds Into

- OP-SM-5 (lepton mass derivation)  
- Lepton series paper  
- OP-G-1 (three generations — Koide connects generation structure to masses)
