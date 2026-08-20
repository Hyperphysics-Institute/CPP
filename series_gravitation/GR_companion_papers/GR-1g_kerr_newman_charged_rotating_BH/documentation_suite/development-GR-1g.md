# Development log — GR-1g (The Kerr–Newman Metric)

**STATUS: reconstructed.** GR-1g predates the vignette convention; the
March 2026 authoring is thin because nothing was recorded at the time.

## March 2026 — closing the family

**Vignette 1 — three sources, one spacetime.** With mass handled by
GR-1c and spin by GR-1f, charge was the last parameter. Its broadcast
component was already in hand — radial vector SSV, from the companion
that derives Coulomb's law — so the paper's work was composition:
showing the three components source the same spacetime and produce
Δ_KN = r² − 2Mr + a² + Q², with the Coulomb contribution entering the
Kerr Δ additively. Every limit was checked: Q = 0 gives Kerr, a = 0
gives Reissner–Nordström, both zero gives Schwarzschild.

**Vignette 2 — the bound generalizes without new machinery.** GR-1f had
derived the Kerr bound from broadcast subluminality at the outer
horizon. The same argument with three components gives M² ≥ a² + Q² —
the Kerr–Newman extremality condition. Extremality remains a causality
limit rather than a censorship conjecture, inheriting both the strength
and the exposure of GR-1f's argument.

**Vignette 3 — a second singularity, the same rule.** Kerr–Newman's
classical pathology is a *ring* singularity at r = 0, θ = π/2, where
Σ → 0. The CP Exclusion bound PSR_eff ≥ l_P/2 saturates the lattice at
Planck density before Σ can vanish, leaving a Planck-density ring core.
The paper mentions this almost in passing, but it is the strongest
indirect support the Exclusion argument has: an untouched rule handling
a structurally different divergence in a different geometry.

**Vignette 4 — and a note on relevance.** The paper records that charge
neutralises rapidly for most astrophysical holes, so the evaporation
chain generically reduces to Kerr → Schwarzschild → Planck remnant. The
charged branch is a limiting case, and the result is about completeness
of the family rather than about objects in the sky.

## August 2026 — renamed and formatted

**Vignette 5 — c12 becomes GR-1g.** Moved in the arc reorganization
(Patch 3230); CP/GP Signature added in the W-A pass (Patch 3273). No
content changes.

## Session 152, 20 Aug 2026 — the suite

**Vignette 6 — the list that aged well.** After GR-1b, GR-1c, and GR-1f
all turned up overtaken open-problem sections, this one is nearly clean:
three of four items are still genuinely open, and the fourth
(Kerr–Newman superradiance) only moved partway — GR-1h supplies the
threshold form ω < mΩ₊ + qΦ₊ that the item names, but the quantitative
amplification it asks for is still open even for the uncharged case.
This sharpens rather than softens the earlier pattern: status sections
rot exactly where the programme advanced past them, and it has not
advanced into charged evaporation, charged echoes, or the all-orders
rotating-charged structure.

**Vignette 7 — where the suite points a future panel.** At additivity.
The paper's method is that three broadcast components superpose; the
Einstein–Maxwell system is nonlinear and charge does not generally
superpose onto vacuum solutions. Whether the CPP components genuinely
add, or whether agreement with Δ_KN is obtained by construction, is
unexamined — and the reasoning behind that step was never captured
either, so the uncaptured part and the exposed part coincide again.
