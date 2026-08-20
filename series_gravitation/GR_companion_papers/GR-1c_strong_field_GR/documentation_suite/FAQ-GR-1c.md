# FAQ — GR-1c

**Q1. How can a substrate theory reproduce Schwarzschild *exactly*?**
By not approximating. The PSR response PSR_eff = l_P/(1 + kΔ|SSV|) is
already nonlinear — it is the full constitutive statement, not a
linearization awaiting corrections. Integrated over shells with the
exact source kΔ|SSV| = GM/rc², it gives the isotropic Schwarzschild
metric with no free parameters. GR-1a and GR-1b are the same expression
truncated at zeroth and first order.

**Q2. Where does CPP differ from GR observationally?**
Nowhere outside the horizon — g_tt(r_S) = 0 exactly and the exterior is
identical at all r > r_S. The departures are all interior or
Planck-scale: the core, the evaporation remnant, and the suppressed
scalar/vector wave modes. This is honest but also a limitation, and the
paper says so: the Planck core is falsifiable only through
interior-sensitive channels.

**Q3. Isn't a Planck-scale cutoff just the usual way of hiding a
singularity?**
The distinction worth pressing is whether the cutoff was introduced *for
this purpose*. The CP Exclusion Rule — no two Conscious Points on one
Grid Point — long predates the black-hole discussion and does other work
elsewhere in the theory. That it bounds PSR_eff ≥ l_P/2 and therefore
forbids the metric from reaching zero is a consequence, not a repair.

**Q4. What exactly is at the centre, then?**
A Planck-density core: radius r_core = GM/c² = r_S/2, density
~5.16×10⁹⁶ kg m⁻³. For a solar-mass hole that is 1.48 km, comfortably
inside r_S ≈ 2.95 km — which is why no exterior measurement can see it.

**Q5. The field-equation Proposition was wrong. What happened?**
It shipped with a defective compensator, and the error was caught by a
*later* derivation's HALT check comparing its own static reduction
against this paper's published equation. The Proposition failed against
**this paper's own exact solution** — O(a⁴) where O(a³) was required.
The root cause: it had been written for the wrong potential. The exact
measured-frame statement is that the *logarithmic lapse*
N = ln√(−g_tt/c²) is harmonic. The defect was registered rather than
quietly patched, diagnosed, approved 5–0 at CONV-027, ratified by the
founder, and enacted at V2.2 with the defective formula preserved
verbatim in a Corrigendum Remark.

**Q6. Did anything else in the paper depend on the defective formula?**
No — and this was checked, not assumed. Solution-level agreement was
exact throughout: the metric, the classical tests, and the weak-field
limit were untouched, and GR-1i's 8/8 verify stands. The defect lived in
the *equation* layer, which nothing downstream had yet consumed.

**Q7. Does the corrected Proposition mean CPP now has Einstein's field
equations?**
No, and the enactment patch says so explicitly. The corrected
Proposition is proven algebraically equivalent to the census-derived T-1
— which is a real result — but whether that quasilinear structure
produces the exact Einstein tensor is `op:einstein`, and it is still
open after the whole field-equation programme.

**Q8. What's the "one equation in two variables" claim?**
The equivalence identity: □_g artanh(kv/2) = [32k/((2−kv)(2+kv)⁵)]·∇²_flat v
for generic v, with no derivative terms surviving. So the measured-frame
equation and the flat-lattice census equation are the same law written
in two bookkeepings — clock rates multiply, so the observer's potential
is a logarithm; messenger counts add, so the substrate's is not.

**Q9. Are the paper's Open Problems still open?**
Three of five are not. `op:kerr` was delivered by GR-1f (and GR-1g for
Kerr–Newman); `op:echoes` by GR-1d; `op:hawking` substantially by GR-1e.
`op:einstein` remains correctly open. **`op:24cell` is a special case**:
Spin III now exists and supplies the spectrum it asked for — but on the
regular dodecahedron, because founder ruling A1 retired the 24-cell as
the Voronoi domain (the 600-cell's dual is the 120-cell). That item
states a superseded geometry, not merely a stale status. The paper has
not been edited; see `phenomena-GR-1c.md` for the full table.

**Q10. What's the weakest step?**
Theorem 1's shell integration and Theorem 2's Exclusion-Rule argument —
not because either looks wrong, but because neither has ever been
attacked from outside. CONV-027 reviewed the field-equation Proposition
and nothing else in this paper. A future round should start there.
