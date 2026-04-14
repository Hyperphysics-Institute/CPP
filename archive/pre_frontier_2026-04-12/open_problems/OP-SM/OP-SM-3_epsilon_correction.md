# OP-SM-3: Derive $\varepsilon = -0.145$ from Lattice Geometry Exactly

**Priority:** HIGH — needed for exact charge screening $\delta = 1/3$ and $\alpha_\text{EM}$  
**Status:** OPEN — $\varepsilon$ used as a correction; origin not fully derived  
**Series:** 600-cell SM emergence, suppression/suppression\_phi.md, Appendix L  
**Session evidence:** Suppression files, 23 March 2026 session  
**Last updated:** 23 March 2026

---

## Statement

In CPP, two key quantities require a perturbative correction
$\varepsilon \approx -0.145$ to achieve exact matches:

1. **Charge screening:**
   $\delta = \phi^{-2} \cdot (1 + \varepsilon)$
   $= 0.382 \times 0.855 = 0.327 \approx 1/3$
   (2% from exact — see OP-SS-9 for the stronger topological argument)

2. **Fine-structure constant:**
   $\alpha^{-1} = 360/\phi^2 - 2/\phi^3 - \varepsilon/\phi^4$
   $\approx 137.036$ (exact to 6 digits without $\varepsilon$;
   $\varepsilon$ extends the series precision further)

Derive $\varepsilon = -0.145$ from the 600-cell geometry — specifically
from multi-layer averaging, entropy weighting, and holographic damping
(as described in Paper 2 Appendix L).

---

## What Is Known

Paper 2 and `suppression_phi.md` describe $\varepsilon$ as arising from:

- **Multi-layer averaging:** The outer cage shells contribute with
  different weighting than the inner shells; averaging over the
  $N_k$-weighted generational hierarchy shifts the effective
  $\phi^{-2}$ factor.

- **Entropy weighting:** The Boltzmann factor at scale $T = N_k$
  modulates the DP cloud composition; this modulation shifts
  the effective overlap fraction.

- **Holographic damping:** The finite vertex count $N = 120$
  introduces corrections to the infinite-lattice approximation.

The numerical value $\varepsilon = -0.145$ is stated but its exact
derivation is labelled "future work" in Appendix L.

---

## Physical Significance

$\varepsilon$ is the bridge between two key CPP results:

- Without $\varepsilon$: $\phi^{-2} = 0.382 \neq 1/3$ and
  $\alpha^{-1} = 137.036$ (already good but not exact)
- With $\varepsilon$: charge screening → 1/3 (but note OP-SS-9 shows
  this is topological, not from $\varepsilon$) and
  $\alpha^{-1}$ series extends to higher precision

**Important caveat from OP-SS-9:** The mathematical analysis in the
strong-sector session (Stage 19) proved that $\delta = 1/3$ cannot
arise from $\phi$-arithmetic alone because 1/3 is rational and $\phi$
is irrational. Therefore $\varepsilon$ as a correction to get
$\phi^{-2}(1+\varepsilon) = 1/3$ is actually *not the right approach*
for charge quantisation. The correct derivation is topological (C3
vertex symmetry). However, $\varepsilon$ may still be important for
the $\alpha_\text{EM}$ series and other quantities.

---

## Two Sub-Problems

**Sub-problem 1 — $\varepsilon$ in the $\alpha_\text{EM}$ series:**

$$\alpha^{-1} = \frac{360}{\phi^2} - \frac{2}{\phi^3} - \frac{\varepsilon}{\phi^4} - \ldots$$

The raw formula already gives 137.0356 (0.0003% from observed). The
series correction $\varepsilon/\phi^4 = -0.145/6.854 \approx -0.0212$
would give 137.057 — moving *away* from the observed value. This
suggests the series has a sign issue or $\varepsilon$ enters differently
for $\alpha$ than for the charge screening.

**Sub-problem 2 — multi-layer entropy average:**

Compute explicitly:
$$\varepsilon = \left\langle\frac{N_k \phi^j - N_\text{lattice}^{1/2}}
{N_k \phi^j}\right\rangle_j$$

where the average runs over generations $j$ weighted by thermal
Boltzmann factors, and see if this gives $-0.145$.

---

## Relationship to OP-SS-9

OP-SS-9 (charge quantisation) is independent of $\varepsilon$: the
topological proof $\delta = 1/3$ from C3 symmetry does not use
$\varepsilon$. If that proof is correct, then the $\varepsilon$
correction to $\phi^{-2}$ is an approximation to the topological
result, not the fundamental derivation. OP-SM-3 is therefore
primarily about the $\alpha_\text{EM}$ series precision and the
multi-layer entropy averaging — it is complementary to but not
required for OP-SS-9.

---

## Feeds Into

- $\alpha_\text{EM}$ precision beyond 4 digits (OP-EW-2)
- OP-SS-9 (confirmed independent — but cross-check illuminating)
- OP-G-2 (all SM parameters — $\alpha_\text{EM}$ precision matters)
