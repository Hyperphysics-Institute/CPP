# Glossary — SR-1: Mechanistic Derivation of Relativistic Effects via SSV in the Dipole Sea

**Paper:** SR-1_special_relativity_emergence.tex (v17, 26 March 2026)
**Last updated:** 30 March 2026

*Definitions of all SR-1-specific terms. General CPP terms (CP, Dipole Sea, SSV, ZBW, Grid Point, Absolute Moment) are defined in the CPP master glossary. This file covers terms specific to the relativistic sector.*

---

## Absolute Moment (t_P)

The universal, frame-independent clock tick of the CPP framework — one Planck time step during which every Conscious Point evaluates its incoming DI-bits and executes exactly one displacement. The Absolute Moment is a foundational CPP postulate: it ticks once per Planck time for every CP simultaneously, in a frame-independent sense that transcends the relativity of simultaneity. The Absolute Moment rate is invariant under all local stresses — only the per-Moment displacement magnitude varies. This invariance is what makes the 4D→3D projection exact rather than approximate.

The consistency of the Absolute Moment with special relativity's prohibition on superluminal signalling is resolved by the CPP ontological hierarchy: the Nexus that enforces the Absolute Moment operates atemporally — outside the spacetime it coordinates — and transmits no causal signal through spacetime.

---

## α_geom (Geometric Coupling Constant)

The exact algebraic constant from the 600-cell Voronoi stiffness integral:

    α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594

α_geom is the second moment of the face-area distribution over the 12 nearest-neighbour faces of the Voronoi cell's dual 120-cell. It appears in both SR-1 (the k derivation, establishing the functional form of the PSR saturation curve) and SS-1 (the sea_strength derivation via THEO-SS-4). This cross-paper appearance is not a coincidence — both are consequences of the same 600-cell Voronoi geometry: α_geom is the universal geometric stiffness constant of the 600-cell lattice.

---

## Coupling Constant (k)

The SR-1 lattice normalisation coefficient relating stored energy density to the fractional PSR reduction (renamed from "coupling constant" at Patch 2474):

    k = α · l_P³/E_P   —   a normalisation convention, not a derived constant.

**Correction (Patches 2471/2474).** The earlier three-step derivation ending in "dimensional analysis forces the prefactor to exactly 1" is withdrawn — dimensional analysis fixes dimensions, never a dimensionless prefactor. What survives: the stiffness integral gives the functional form (α_geom ≈ 0.5594 per circumradius; unit-dependent, 0.2444 per l_P), and the collapse condition sets the scale SSV_crit = E_P/l_P³. The prefactor α cancels identically in the physical product k·ΔSSV for any α (verified, `code/2471_k_convention_and_alpha_geom_verification.py`, 31/31), so k's numerical value carries no physical content by itself. The earlier "confirmed by Monte Carlo to machine precision (500 trials)" citation is also withdrawn — the cited script was a stub (one of the four fabricated MC citations replaced at Patch 2471). **Inheritance rule:** (k, ΔSSV) is a matched pair; mixing conventions rescales γ−1 by exactly α.

---

## Displacement Budget

The maximum spatial displacement available to a Conscious Point per Absolute Moment, set by the Voronoi insphere radius. In the unstressed lattice the displacement budget = l_P. Under SSV stress the budget shrinks to PSR_eff = l_P/(1+k·ΔSSV). The displacement budget is shared between the CP's bulk translational motion (consuming fraction f = v/c) and its internal resonances (atomic oscillations, clock cycles). The two uses compete for the same fixed budget: more bulk motion → less internal resonance → slower clocks → time dilation. Length contraction arises from the same budget constraint applied spatially.

---

## Effective Voronoi Cell Volume (V_eff)

The free volume available for CP displacements inside a Voronoi cell under SSV stress:

    V_eff = V₀ / (1 + k·ΔSSV)

where V₀ = 600√2/(12φ³) ≈ 16.693 is the undistorted cell volume in unit circumradius coordinates. The 4D volume scales as V ∝ r⁴, so the effective insphere radius scales as PSR_eff = l_P/(1+k·ΔSSV) — the square-root relationship between volume and radius in 4D means the linear volume compression produces a linear radius compression to first order.

---

## Energy-Momentum Bridge

The physical identification that connects the CPP geometric strain k·ΔSSV to the standard SR Lorentz factor. When ΔSSV is identified as relativistic kinetic energy density — ΔSSV = (γ_SR−1)mc²/(V₀·l_P³) for a CP aggregate of mass m moving at velocity v — the product k·ΔSSV evaluates to exactly γ_SR−1 after Planck normalisation cancels all factors of V₀ and l_P. This gives γ_CPP = γ_SR exactly. *(Corrected, Patches 2474/2508: through v18 this entry claimed the bridge "follows from the definition of k" — withdrawn; the identification supplies γ as an INPUT, and k is a normalisation convention (α cancels in k·ΔSSV; quote (k, ΔSSV) as a matched pair). The "necessity" clause via the Geometric Insufficiency Theorem is withdrawn with that theorem's demotion (Patch 2475). At v20 the bridge is grounded externally at W2 world-call strength: the blind-pinned SF-6 inertia mechanism yields ε = γ−1 at the energy level for closed self-bound patterns, Laue coefficient exactly 1 — see SR-1 v20 §Resolution.)*

---

## Geometric Insufficiency Theorem (Appendix H) — DEMOTED (Patch 2475)

**Demoted to a three-model Proposition.** Through v19 this was billed as a theorem: no purely geometric displacement model can recover the exact Lorentz factor. The proof rested on an erroneous 4D cap expansion (f^{1/2} published; f^{5/2} correct — verified to 50 digits) and the theorem was refuted by its own Model 3. What stands: the elimination of the three natural displacement models (strain exponents 1, 1, 5/2 against the required 2). The class question was subsequently pursued to closure and the geometric route is CLOSED negative-for-mechanism (OPEN-SR-H1-CLASS, K1, Patch 2493; round-2 Q1 unanimous, Patch 2500); the surviving codim-2 geometric identity is PROP-SR-H1-1, ungrounded.

---

## H₄ Symmetry Group

The Coxeter group of the 600-cell, H₄, with order 14,400. H₄ acts transitively on the 600 tetrahedral cells and the 120 vertices of the 600-cell. The second-moment tensor of the 120 vertex vectors equals (1/4)δμν by Schur's lemma — the H₄-invariant rank-2 tensor is unique and isotropic. This means every macroscopic observable averaged over one 600-cell motif is proportional to the identity metric, with no residual directional bias. Lorentz covariance at macroscopic scales is a theorem of H₄ symmetry (Appendix C.2), not a postulate.

---

## Planck Sphere Radius (PSR)

The effective maximum spatial displacement per Absolute Moment available to a Conscious Point. In the unstressed lattice, PSR = l_P (the Planck length), set by the Voronoi insphere radius r_in = 1/(φ√2) after Planck normalisation. Under SSV stress the PSR shrinks:

    PSR_eff = l_P / (1 + k·ΔSSV)

The PSR is the fundamental coupling between stored energy and physical clock and ruler behaviour. All of SR-1's relativistic effects follow from this single formula.

---

## PSR_eff (Effective Planck Sphere Radius)

The stressed-state PSR. See "Planck Sphere Radius" above. The subscript "eff" distinguishes it from the unstressed baseline l_P.

---

## Quasicrystalline Lattice

The spatial structure of CPP — an infinite tiling of overlapping 600-cell motifs in flat ℝ⁴. This is not a single finite 600-cell (which would imply a closed bounded universe with problematic boundary conditions) but a quasicrystalline arrangement analogous to 3D icosahedral quasicrystals. The overlapping motifs collectively define the Grid Points; their Voronoi cells overlap correspondingly. The quasicrystalline structure preserves perfect local H₄ (icosahedral) symmetry while extending indefinitely, yielding macroscopic isotropy and exact Lorentz covariance. Boundary effects are unobservable at all sub-cosmological scales. Discreteness corrections to macroscopic observables are suppressed by (l_P/L)² and are undetectable at all current experimental scales.

---

## ΔSSV (Excess Space Stress Vector)

The kinetic or gravitational energy stored in the Dipole Sea as increased dipole separation inside each Voronoi cell. ΔSSV is the CPP counterpart of kinetic energy density: for a CP aggregate of mass m and velocity v, ΔSSV = (γ_SR−1)mc²/(l_P³) in Planck-normalised units. At low velocity, ΔSSV ≈ mv²/(2l_P³) — the classical kinetic energy density. At relativistic velocities ΔSSV captures the full relativistic kinetic energy. The excess SSV is the physical mechanism by which particle motion compresses Voronoi cells and reduces the PSR, producing all relativistic effects.

ΔSSV can also be accumulated from gravitational sources (curved spacetime in GR corresponds to a local ΔSSV gradient in CPP). SR-1 focuses on kinematic ΔSSV from velocity; gravitational ΔSSV is treated in the companion GR extension papers.

---

## Speed Limit (c = l_P/t_P)

In CPP the speed of light is not a postulate — it is Theorem A.8.2: a theorem of the 600-cell Voronoi geometry. In the unstressed lattice (ΔSSV = 0) a CP executing a pure spatial step achieves |Δx| = l_P in time t_P, so v = l_P/t_P =: c. The Voronoi insphere makes this the maximum possible displacement. Under stress (ΔSSV > 0), PSR_eff < l_P and v_max < c. As ΔSSV → ∞, v_max → 0. The speed of light is the unique maximum velocity corresponding to zero lattice stress, and is determined specifically by the 600-cell's insphere radius r_in = 1/(φ√2), which after Planck normalisation gives l_P. No other regular convex 4-polytope produces a Voronoi insphere with the H₄ golden-ratio scaling 1/(φ√2).

---

## SSV_crit (Critical Space Stress Vector)

The SSV energy density at which one Voronoi cell's displacement budget is completely saturated — the collapse condition:

    SSV_crit = E_P/l_P³ ≈ 4.63 × 10¹¹³ J/m³

This is the Planck energy distributed over the three spatial dimensions of the Voronoi insphere (the timelike Absolute Moment direction is excluded because it is stress-invariant). SSV_crit is not a free parameter; it follows from the requirement that one Planck energy fills one Planck-volume cell. The coupling constant k = α_geom/SSV_crit = l_P³/E_P follows immediately.

---

## V₀ (Undistorted Voronoi Cell Volume)

The Voronoi cell volume in the undistorted 600-cell lattice, in unit circumradius coordinates:

    V₀ = 600√2/(12φ³) ≈ 16.693

Derived from first principles: the 600-cell has 600 congruent regular tetrahedral cells (proved by H₄ cell-transitivity); each tetrahedron with edge a = 1/φ (from the binary icosahedral group quaternion structure) has 3-volume a³√2/12; summing over 600 cells and dividing by the 120 vertices gives V₀. This derivation is self-contained and does not rely on external tabulations.

---

## Voronoi Cell

The region of 4D space closer to a given Grid Point than to any other. In the undistorted 600-cell lattice the Voronoi tessellation is dual to the 120-cell; each Voronoi cell is bounded by 12 pentagonal faces (the 12 nearest-neighbour perpendicular bisectors). The pentagonal faces arise from the icosahedral symmetry of the 120-cell dual. Under SSV stress the free volume inside each cell shrinks, reducing the effective insphere radius and hence PSR_eff.

---

## Worldline (Inertial vs Non-Inertial)

A path through the CPP spacetime lattice traced by a CP aggregate over time. An inertial worldline accumulates zero ΔSSV (v = const, no acceleration, zero net SSV above background). A non-inertial worldline accumulates nonzero ΔSSV during acceleration phases. The twin paradox is resolved by noting that only the non-inertial worldline (the travel twin's path) accumulates net ΔSSV, and this accumulation is a frame-independent physical fact — the asymmetry is real, not a reciprocal illusion of different reference frames.
