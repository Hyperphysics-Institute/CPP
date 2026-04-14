# OP-SM-7d-AB: Aharonov-Bohm Self-Energy Loop as Origin of Koide Phase θ

**Priority:** HIGH — most tractable candidate for OP-SM-7d  
**Status:** OPEN — identified Session E; not yet computed  
**Cited in:** Paper 4, §4 Remark; potential_solutions.md PS-2  
**Last updated:** 24 March 2026

---

## Statement

Compute the ZBW self-energy for the K3 triangle circuit
$V_4 \to V_i \to V_j \to V_k \to V_4$ including the Aharonov-Bohm
phase from ZBW orbital circulation, and check whether the resulting
phase shift equals $\Delta\theta = 2.267° = 0.0396$~rad.

---

## Physical Picture

**Session E proved:** The apex $V_4$ is dark to the antibonding modes
under the uniform coupling. No C3-symmetric perturbation can select $\theta$.

**The AB loop mechanism:** The ZBW orbital on K3 circulates around the
triangle $V_1 \to V_2 \to V_3 \to V_1$ with angular frequency $\omega_0$.
This circulation generates an effective magnetic flux through the K3
triangle area:

$$\Phi = \hbar\omega_0 \times A_{K_3}^{\text{phys}}$$

where $A_{K_3}^{\text{phys}}$ is the physical area of the K3 triangle
in the cage.

The eCP at apex $V_4$ exchanges virtual DPs with the base vertices.
The one-loop self-energy diagram traverses the triangle:

$$\Sigma_\text{AB} = g^2 \oint_{K_3} e^{i\Phi/\Phi_0}\,d\ell$$

where $g = \text{sea\_strength}\times\hbar c/r_\text{conf}$ is the
DP coupling and $\Phi_0 = hc/e$ is the flux quantum. If the circulation
is chiral (preferred direction from the 3D tetrahedral orientation in
the 600-cell), $\Sigma_\text{AB}$ has a non-zero imaginary part that
rotates the antibonding mode orientation by $\Delta\theta$.

---

## The Calculation

**Step 1: Physical area of K3 triangle.**

The K3 base is an equilateral triangle with edge $a = r_\text{conf}/\varphi$.
Physical area:
$$A_{K_3}^{\text{phys}} = \frac{\sqrt{3}}{4}a^2 = \frac{\sqrt{3}}{4}
\left(\frac{r_\text{conf}}{\varphi}\right)^2$$

With $r_\text{conf} = 0.4$~fm:
$$A_{K_3}^{\text{phys}} = \frac{\sqrt{3}}{4} \times \frac{(0.4)^2}{\varphi^2}
= 0.0297~\text{fm}^2$$

**Step 2: Effective flux.**

$$\Phi = \hbar\omega_0 \times A_{K_3}^{\text{phys}}
= \text{sea} \times \frac{\hbar c}{r_\text{conf}} \times A_{K_3}^{\text{phys}}$$

(Units: MeV$\cdot$fm$^2$ — needs conversion to flux quantum units.)

**Step 3: AB phase.**

$$\phi_\text{AB} = 2\pi \Phi / \Phi_0$$

where $\Phi_0 = hc/e = 4.136 \times 10^{-15}$~V$\cdot$s.
Check: does $\phi_\text{AB} = \Delta\theta = 0.0396$~rad?

**Step 4: Whether circulation is chiral.**

The K3 triangle embedded in 3D (as the base of the tetrahedron) has a
natural orientation given by the normal vector pointing toward $V_4$.
The ZBW orbital circulation in the direction of this normal would give
a definite sign to $\Phi$ — making the mechanism chiral and hence
able to select a specific $\theta$.

---

## Key Numerical Target

$$\Delta\theta = (5/4) \times \text{sea}^2 = 1.25 \times (0.178)^2
= 0.0396~\text{rad} = 2.267°$$

If the AB phase equals this, the mechanism is confirmed.

---

## Connection to Existing Results

- $\Delta\theta / \text{sea}^2 = 1.248 \approx 5/4$ (empirical, 0.15% fit)
- The AB loop naturally generates a correction at order $\text{sea}^2$
  (two vertices in the loop, each contributing one factor of sea\_strength)
- The coefficient $5/4$ should emerge from the geometric ratio
  $A_{K_3}/r_\text{conf}^2$ times a numerical factor from the loop integral

---

## Tractability

**One focused session.** The calculation is:
1. Compute $A_{K_3}^{\text{phys}}$ (trivial — done above)
2. Compute $\Phi$ in physical units
3. Compute $\phi_\text{AB}$
4. Compare to $\Delta\theta$

If the numbers match, OP-SM-7d is solved.
If they don't, the mechanism is falsified and PS-3 or PS-4 must be pursued.

---

## Parent Problems

- **Solves:** OP-SM-7d (Koide phase θ)
- **Enables:** Paper 4 full derivation (currently θ is calibrated, not derived)
- **Related:** PS-2 in potential_solutions.md
