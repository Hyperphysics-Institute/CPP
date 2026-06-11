# Spin-2 Step 5 — the emergent-graviton verdict: option D fails; the spin-bit axiom is necessary (Patch 1116)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1116_step5_emergent_graviton_modes.py`
**Result — the assault on the wall, decisive:** the emergent/collective route (option D) **fails**. The
long-wavelength effective theory of the scalar+vector field on the 600-cell lattice has propagating
modes of helicity **{0, 0, ±1} only** — **no helicity-±2**, for *any* couplings. Closing `op:einstein`
(a), and matching the observed tensor gravitational-wave polarizations, therefore **requires a
fundamental rank-2 degree of freedom — the spin-bit axiom (A/B/C). This is now a conclusion, not an
open question.** **op:einstein (a) remains formally OPEN pending the axiom choice; NO VERDICT MOVED.**

## The calculation
Per Grid Point the dynamical content is one scalar (`|SSV|_abs`) + one vector (`SSV_net`) = 4 real
components. So the dynamical matrix `D(k)` is 4×4 and there are exactly **4 propagating branches** per
wavevector. Their helicity is fixed by the little group (rotations about `k̂`):
- scalar → helicity 0; `V_∥` → helicity 0; `V_⊥` (two components) → helicity ±1.

A helicity-±2 mode would require a basis vector transforming as `e^{±2iθ}` under rotation about `k̂` —
**which does not exist** in the 4-dimensional space `span{φ, V_x, V_y, V_z}` (max `|helicity| = 1`).
Building `D(k)` explicitly with the most general icosahedral nearest-neighbor couplings
(`code/1116_step5_emergent_graviton_modes.py`) confirms it: the scalar–vector mixing only couples `φ`
to `V_∥` (helicity 0); the transverse `(V_x, V_y)` block is a pure helicity-±1 doublet with **no**
`V_x`–`V_y` quadrupole channel. The four branches are **{0, 0, +1, −1}**, and the couplings
(`c_s, λ, μ, g`) set only their dispersions, never their helicity content.

**Conclusion:** no emergent helicity-±2 mode exists, and this is *representation-theoretic*, not a
matter of finding the right dynamics. The 600-cell's H_g (l=2) geometric slot (1112) and the
rank-agnostic shell-sum (1113) would propagate a quadrupole *if one existed* — but the scalar+vector
substrate provides no field component to put in that slot. The composite/bilinear route was already
excluded (1115: second-order, double-frequency, not the linear GW). All no-new-axiom routes are now
closed.

## Why this was the expected place to land (and why it is not a defect)
This is the *normal* situation in physics, not an anomaly. In every successful formulation of gravity
the spin-2 graviton (the metric) is a **fundamental** field; emergent-graviton programs are the exotic,
hard, and rarely-successful exception, and even they need large internal Hilbert spaces that a
scalar+vector site does not have. CPP attempting the emergent route and finding it cannot work places
CPP **with** mainstream gravity, not against it: gravity's tensor sector is fundamental, and CPP must
carry it as such. The Weinberg–Witten evasion (1115) showed the emergent route was *permitted*; this
calculation shows it is nonetheless *not realized* by a scalar+vector substrate — the permission was
necessary but not sufficient.

## The architect's granularity intuition was correct
The founder anticipated the reason: *"possibly because the granularity of space was insufficient to
reproduce the spin."* That is exactly the finding. The information transmitted per Grid Point — a scalar
magnitude `|SSV|_abs` and a vector direction `SSV_net` (the "tangent of its arc") — is representationally
too poor to reconstruct the transverse-traceless (spin-2) part of the gravitational field. The vector
carries the *first* derivative of direction (helicity 0, ±1); the GW radiation is the genuinely
*rank-2* content that a vector's superposition, to any order, cannot supply as a linear massless mode.
The "missing information" is precisely the l=2 quadrupole.

## Verdict and the resolved decision
- **Option D (emergent, no new axiom): RULED OUT.** The collective spectrum of scalar+vector is
  {0,0,±1}; no spin-2.
- **Options A/B/C (fundamental spin-bit axiom): NECESSARY.** To carry the tensor GW sector, a Grid
  Point (or the CP State Register, or the GP→CP instruction) must carry a symmetric-traceless rank-2
  attribute `Q_ij` — the l=2 quadrupole, geometrically slotted by the 600-cell's H_g representation and
  propagated by the rank-agnostic shell-sum.
- **The decision is now made *by the physics*, not by preference:** the spin-bit axiom is required for
  CPP to reproduce General Relativity's radiative sector and the observed GW polarizations. What remains
  is the *engineering* of the axiom — which flow (A/B/C), its precise form, and the source coupling
  `Q_ij ↔ T_μν` (the quadrupole formula) — a deliberate foundational step to take with intent.

## Status of the whole `op:einstein` climb
- **(b)/(b′):** excess-sourcing / inert-uniform-Sea — conditionally closed, grounded in 600-cell
  symmetry. The cosmological-constant local half is secure and unaffected by this result.
- **(a):** GR-recovery — the scalar and vector sectors are recovered (Schwarzschild exactly,
  Newtonian, gravitomagnetic); the **spin-2 radiative sector requires the axiom**, now established as
  necessary. CPP is a scalar–vector gravity *that must be extended by one rank-2 d.o.f.* to be complete.

This concludes the spin-2 construction sub-arc's investigation: the question "is the spin bit
necessary?" is answered — **yes**, on rigorous grounds, with the architect's granularity intuition
identifying precisely why.
