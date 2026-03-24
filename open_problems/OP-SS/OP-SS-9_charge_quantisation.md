# OP-SS-9: Prove $\delta = 1/3$ from 600-Cell Geometry Rigorously

**Priority:** HIGH  
**Status:** OPEN — topological proof exists in C15; integral approach fails  
**Series:** C15; SS\#2  
**Notebook evidence:** `notebooks/fractional_charges_overlap.ipynb` (v8.0, Stage 19)  
**Last updated:** 23 March 2026

---

## Statement

Provide a rigorous, self-contained proof that the hDP overlap fraction
$\delta = 1/3$ follows from the geometry of the 600-cell, with no
free parameters.  The fractional quark charges $+2/3$ and $-1/3$ then
follow immediately:

$$q_\text{up} = +e(1 - \delta) = +\tfrac{2}{3}e, \qquad
q_\text{down} = -e(1 - 2\delta) = -\tfrac{1}{3}e.$$

---

## What is Known

### 1. The topological proof (C15, established)

Color is vertex identity on the tetrahedral base $\{V_1, V_2, V_3\}$.
A quark qCP occupies exactly one of the three base vertices.  The hDP
chain linking the qCP to the cage boundary has overlap fraction:

$$\delta = \frac{1}{N_\text{vertices}} = \frac{1}{3}$$

by C3 rotational symmetry.  This proof is clean and exact.

**The result is topological, not integral.**  The value $1/3$ is
rational; $\phi$ is irrational; they are algebraically independent,
so no $\phi$-based volume integral can equal $1/3$ exactly.

### 2. The integral approach (`fractional_charges_overlap` v8, Stage 19)

The notebook proposes:

$$\delta = \phi^{-2} \times \frac{\int_{r_0}^{1} S(r)\,\gamma(r)\,r^2\,dr}
{\int_0^1 S(r)\,\gamma(r)\,r^2\,dr}$$

where $S(r) = 1/r^4$ (SSV stress density), $\gamma(r) = 1 + k\,S(r)$
(Lorentz amplification), and $\phi^{-2} = 1/\phi^2$.

**Analysis:** For this to equal $1/3$ requires
$\text{outer/total} = \phi^2/3 \approx 0.873$.  With $S = 1/r^4$
and $r_0 = 1/\phi$, the computed ratio is $\sim 0.002$, far too
small.  No choice of integer powers of $\phi$ for $r_0$ reproduces
the required ratio.  The integral approach is physically motivated
but cannot reach $1/3$ exactly from $\phi$-arithmetic.

---

## What Remains

The topological C15 proof is essentially complete.  The remaining
work is of two kinds:

**Kind 1 — Formalise the topological proof:**  
Write it as a theorem with explicit hypotheses about the 600-cell
vertex structure, the C3 symmetry group action, and the hDP chain
boundary conditions.  Ensure the proof makes no implicit assumptions
about the specific cage shape beyond C3 symmetry.

**Kind 2 — Reconcile with the integral approach:**  
Show explicitly why the SSV integral gives $\sim \phi^{-2}$ as an
approximation to $1/3$, i.e., why:
$$\phi^{-2} \approx \frac{1}{3} \times 1.146$$
(they differ by $\sim 15\%$).  The integral should recover the
topological result in the appropriate limit — identify that limit.

---

## Why This Matters

This is the deepest geometric result in CPP.  Charge quantisation —
the empirical fact that all observable charges are integer multiples
of $e/3$ — has no explanation in the Standard Model (it follows from
anomaly cancellation, which itself requires the fermion content).  A
direct geometric proof from the 600-cell would be the most striking
single prediction of the CPP programme.

---

## Feeds Into

- OP-G-2 (full SM from 600-cell — charge quantisation is foundational)
- Lepton charges ($q_e = -e$ follows from $\delta = 0$ for bare eCP
  with no cage — also needs proof)
- EW sector (hypercharge assignments)
