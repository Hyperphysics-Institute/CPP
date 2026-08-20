# Phenomena — GR-1c

**Explained / derived (within the CPP ontology, conditional on the PSR form):**
- **The exact Schwarzschild metric** in isotropic coordinates, from the
  unexpanded response with no free parameters (Theorem 1). The arc's
  central technical result.
- **The horizon**, at exactly the GR location; the exterior is identical
  to GR at all r > r_S.
- **Singularity resolution** (Theorem 2): the CP Exclusion Rule bounds
  PSR_eff ≥ l_P/2, so the metric cannot reach zero. A Planck-density
  core replaces the classical singularity.
- **Why the exact solution is conformally flat** — observed here,
  *explained* later by GR-1j (the lattice is flat; only rulers and
  clocks shrink).

**Predicted beyond GR (this paper's genuine departures):**
- **Planck core**: r_core = r_S/2 (1.48 km for a solar-mass hole),
  ρ_core ≈ 5.16×10⁹⁶ kg m⁻³. Falsifiable only via interior-sensitive
  observation — Hawking spectral modification or ringdown echoes.
- **Planck remnant**: evaporation terminates at M ~ m_P rather than
  proceeding to zero (qualitative; quantitative deferred → GR-1e).
- **Suppressed scalar/vector GW modes**: permitted by the four-component
  LSP but suppressed by (l_P/λ)² ≈ 10⁻⁷⁶ in the LIGO band — undetectable
  now, a distinguishing signature for any future Planck-scale detector.

**Not claimed:**
- Einstein-equivalence. The corrected Proposition gives the CPP field
  equation and its weak-field reduction; whether it produces the exact
  Einstein tensor is `op:einstein`, still open after the field-equation
  programme.

---

## STALENESS FINDING (registered at the Session 152 suite pass, Patch 3285)

**Three of the paper's five Open Problems have been delivered or
superseded, and one rests on a geometry the founder has since retired.**

| GR-1c open problem | Status now |
|---|---|
| `op:einstein` — exact equivalence of the CPP field equation and Einstein's | **Still open**, correctly. Advanced by GR-1j (T-1 derived from the census; the corrected Proposition proven equivalent to it), but full rank-2 equivalence is untouched and remains the arc's frontier. |
| `op:kerr` — full Kerr from rotational SSV | **DELIVERED** — GR-1f; GR-1g extends to Kerr–Newman. |
| `op:24cell` — discrete-to-continuum proof via the Spin III spectrum | **DOUBLY STALE.** Spin III now exists (SPIN-3, v1.0 shipped Patch 3248) and supplies a spectrum — but **on the regular dodecahedron, not the 24-cell**. Founder ruling A1 (Patch 3236) retired the 24-cell as carrying no physical-picture weight: the 600-cell's dual is the 120-cell, so the Voronoi domain is the regular dodecahedron. The problem statement's geometry is superseded, not merely its status. |
| `op:hawking` — quantitative Planck remnant and spectrum | **Substantially addressed** — GR-1e. |
| `op:echoes` — GW echoes from the Planck core | **DELIVERED** — GR-1d. |

**No .tex change made.** Consistent with Patch 3283: a paper overtaken
by later work is a founder decision about how a legacy document should
read, not a worker's bookkeeping. This is the **third** such finding and
the most consequential, because `op:24cell` does not merely list a
solved problem as open — it states a retired geometry as current. Scoped
to the proposed **W-D** status-note pass (anti-erasure: original
retained, dated note beside it).
