# Reasoning capture — Patch 0736: Brick #2, Q1 (grid resolution) made canonical

*SR-1 rederivation pass, Session 154. Brick #2 of the program scoped in
`handovers/2026-06-02_session_153_SR1_rederivation_scope.md`. Settles Q1 from Brick #1
(`series_relativity/development/lp_psr_grid_reconciliation.md`, Patch 0734).*

## The decision

**Q1 (grid resolution) is settled canonically as the NESTED 600-CELL HIERARCHY** — the
reconciliation Brick #1 flagged as "likely," now adopted and propagated. This is the Reading-B
(nested / sub-Planck) intent, reconciled with the Reading-A (single-motif l_P-scale) arithmetic
that SR-1's own derivation uses, by assigning the two readings to two scales of one structure:

- **Coarse (motif) scale** = a single 600-cell = the l_P-scale tile. This is where the
  unit-circumradius geometry lives: R/a = φ, V₀, the insphere → l_P normalisation, and therefore
  k = l_P³/E_P. l_P is the per-Moment **reach ceiling**, c = l_P/t_P.
- **Fine (nesting) scale** = self-similar 600-cells nested down to true GP spacing ~ l_P/10³⁰.
  This is the **effective grid resolution** (sub-Planck) and it is what supplies the
  continuous-looking velocity gradation |d_spatial| = l_P·(v/c). Reading A alone cannot represent
  l_P·(v/c) for arbitrary v (too few GPs per l_P); the fine nesting is exactly what c01's velocity
  partition l_P² = (cΔτ)² + |d_spatial|² needs. This is the load-bearing reason the nested reading
  is correct rather than merely tidy.

"One coarse step per Moment" = many fine GPs traversed.

## Why this leaves all predictions invariant (the required Brick-#2 verification)

The five SR predictions + the muon-storage-ring bound flow from
PSR_eff = l_P/(1 + k·ΔSSV) with k = l_P³/E_P, evaluated at the present epoch. Both prediction-bearing
parameters are **coarse-motif quantities**:

1. **R/a = φ** is derived in unit-circumradius coordinates for a single 600-cell (binary icosahedral
   group 2I on S³, R=1; nearest-neighbour chord² = 2−φ = 1/φ²). That is the coarse motif by
   definition. The fine nested motifs are self-similar (R/a = φ at every level), so they satisfy the
   same relation at smaller absolute scale and do not enter the coarse computation.
2. **k = l_P³/E_P** is forced by dimensional analysis (unique m³/J combination of Planck quantities)
   and cross-checked by the Voronoi second-moment integral over the 120 cells of a single 600-cell
   (c02). Both are single-motif (coarse) computations at the present-epoch l_P.

The Q1 choice concerns how many GPs sit *between* coarse motif vertices — i.e. resolution — which
appears in **none** of the prediction formulae. Hence NO prediction value changes. This satisfies the
handover's Brick-#2 requirement ("Verify R/a=φ and k=l_P³/E_P are stated at the chosen scale
consistently. NO prediction value should change."). No new computation was performed; the verification
is that the resolution choice is orthogonal to the prediction inputs.

## What changed in the corpus (propagation)

- **SR-1 §"Grid Resolution: the Nested 600-Cell Hierarchy"** (new subsection, label
  `sec:grid_resolution`, inserted between Topology Clarification and Voronoi Cells) — the canonical
  declaration. Plus a Key-Properties-of-the-Lattice bullet stating the nesting.
- **c01** (`absolute_moment_postulate.tex`) — l_P annotated as the coarse per-Moment reach ceiling,
  fine grid sub-Planck by nesting; k and c coarse-scale, unaffected.
- **c02** (`c02_dipole_stiffness_C.tex`) — the stiffness second-moment integral annotated as a
  single-motif (coarse, l_P-scale tile) computation; self-similar fine nesting leaves it and k
  unchanged.
- **c07** (`c07_weak_field_GR.tex`) — its pre-existing "nested 600-cell geometry at sub-Planck
  spacing" GP definition annotated as the fine scale of the SR-1 canonical hierarchy (coarse motif =
  reach ceiling). c07 already carried Reading B; this just makes it explicitly the canonical reading.

## Scope discipline / conventions honoured

- NO THEO registered — this is semantics/grounding (definitional reconciliation), not a theorem;
  consistent with the handover's "NO THEO for conditional/negative results" and the Brick-#1 framing.
- No new quantitative prediction → no `predictions.md` entry. No new term → no glossary entry. No new
  axiom (Q2/metric-variability is deferred to Brick #3; Axiom H remains evaluated-not-adopted).
- Stayed clear of the chirality live zone. PCD = Perceive/Compute/Displace (unaffected here).
- This is the resolution of Q1 ONLY. Q2 (is l_P fixed or epoch-dependent?) is explicitly left OPEN
  and is the subject of Brick #3; the present-epoch anchoring of all predictions holds under either
  Q2 branch, so Brick #2 does not pre-empt that fork.

## Pointer
- Next: Brick #3 — pose Q2 (metric variability) as an explicit fixed-vs-variable(VSL) fork.
  See `handovers/2026-06-02_session_153_SR1_rederivation_scope.md` task list item 2.
