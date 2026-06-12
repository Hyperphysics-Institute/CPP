# Reasoning capture — Patch 1125 (Task 4: the readout, the TT-only response, the energy closure)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1125_task4_tt_response_energy.md` + `code/1125_task4_tt_response_energy.py`.

---

## The trap found in planning (the step's real content)

OB-2 part 2 as framed at 1124 asked only about Q's helicity-0,±1 components. Working the
readout exposed the larger danger: **the scalar and vector channels radiate too.** Any
massless field sourced by ρ has a far-zone 1/r quadrupole tail from the retardation expansion
(monopole killed by mass conservation, dipole by momentum, but the quadrupole term
(1/2c²)n̂n̂:M̈ survives). Two potential disasters, both at Newtonian coupling strength with no
Brans–Dicke 1/ω suppression available (CPP's scalar IS Newtonian gravity, full strength):
(i) breathing/longitudinal strain at O(25%) of tensor — against the polarization tests;
(ii) an extra radiative energy channel shifting binary decay at O(10%) — against the double
pulsar at 10⁻⁴. Either kills the model. GR contains the identical structures (harmonic-gauge
h̄_00, h̄_0i radiative tails) and survives via a conservation-enforced cancellation in the
curvature. So the task became: prove the CPP assembly inherits GR's cancellation, exactly.

Key structural insight that made the inheritance plausible before computing: in Brans–Dicke
the scalar couples to matter *independently* (test particles carry scalar charge); in CPP the
channels couple to matter **only through one assembled metric** (the C5 readout — CPs follow
geodesics of a single effective metric). One metric + one conserved source is precisely GR's
configuration; the cancellation should carry over. It does — with one wrinkle.

## P1 — why the symbolic computation, and what the counting argument adds

The theorem (constraint ⇒ R_{i0j0} is TT-only) is classical, but DG-3 should receive it as a
direct computation, not a citation: sympy, plane wave along z, four constraint substitutions
(H_tν = −H_zν, with H_tt = H_zz forced by symmetry of the t-z relation), trace-reversal,
linearized Riemann, simplify. Result exact: R depends only on (H_xx−H_yy)″ and H_xy″. The
counting argument explains *why* it had to come out that way (constraints leave 6 functions;
4-parameter residual gauge acts within them; curvature is gauge-invariant ⇒ 2 invariants =
TT) — but the computation is the proof; the counting is the explanation.

Constraint inheritance, the one-line theorem stated in the doc: retarded solutions of
□h̄_μν = −λT_μν with ∂^μT_μν = 0 satisfy ∂^μh̄_μν = 0 automatically (the divergence obeys the
sourceless wave equation with no incoming radiation). Conservation anchors as in 1124:
CP-count (exact, c07 rules); momentum (substrate bookkeeping; flagged, not over-claimed).

## P2 — the missing-trace crisis and its resolution (the session's discovery)

Counting components against the harmonic pattern: GR's h̄_μν has 10; CPP's packet supplies 9
(h̄_00, h̄_0i, h̄^{TF}_ij). The missing one is the spatial trace τ = h̄_kk, sourced by T_kk —
and it *radiates* for non-circular sources (∫T_kk = ½d²/dt²∫ρr² ≠ 0 when the separation
changes). First reaction: is the packet one slot short — does A3′ need a sixth tensor
component or a second scalar? That would have wrecked the completion theorem's elegance and
added a degree of freedom.

Resolution, checked before celebrating: **τ is redundant.** The wave-zone constraint
(ν = z component) reads H_tt = H_zz = n̂n̂:(Q + ⅓δτ) ⇒ τ = 3(H_tt − n̂n̂:Q). Test against the
binary's retarded solution: τ_completed = 3(h̄_tt − n̂n̂:Q) vs τ_GR = (2G/c⁴r)M̈_kk — agree to
4×10⁻¹⁹. Local (direction-free) form for the Compute step: the ν = i constraints give
∇τ = 3(∂_t h̄_{0i} − ∂_j Q_{ji}) — built from shell-gradients the GP already perceives;
curl-consistency of the RHS is guaranteed by the channels being retarded solutions of one
conserved system. And the statics check: τ_static = ∫T_kk = 0 by the virial theorem — which
retroactively explains why c07/c08's exact static recovery never surfaced the slot.

The pleasing closure: a spatial trace is rotationally l=0 — a *second scalar*. The 1123
completion theorem said the packet carries every protected irrep exactly once; the physics
now ratifies the geometry: conservation is what makes the second A-slot unnecessary. The
lattice provides one scalar seat; the dynamics needs only one.

Honesty discipline on C5 v0.2: the completion rule adds no degrees of freedom and is the
unique assembly that does not violate identities the channels already satisfy, reducing to
c07's map in statics — our position is "derived-unique." But whether DG-3 scores it as
derivation or as postulate content is genuinely arguable, so it is posed as explicit review
question Q1 rather than buried.

## P3 — designing the test to arm the trap

Circular orbits have M̈_kk = 0 (constant separation) — they *hide* the trace channel. So the
six-mode Eardley test uses e = 0.6. With the completed assembly: breathing/longitudinal/
vector ≤ 4×10⁻¹¹ of tensor (finite-difference noise floor); tensor response matches −½ḧ^TT at
2.4×10⁻¹¹. The counterfactual (τ = 0) is documented deliberately: 2.6×10⁻² O(1)-relative
breathing+longitudinal violation — proving the completion is load-bearing exactly for the
eccentric/inspiraling sources real detectors see, and that a reviewer testing only circular
waveforms would miss it. One bug in-session: my tensor cross-check initially compared
modes['plus'] to 2×(reference) — factor-2 error in the comparison line, not in the physics
(E_xx − E_yy = −(H_xx−H_yy)″/2 = the reference, no 2). Fixed; residual dropped from 1.0 to
2.4×10⁻¹¹.

## P4 — what "the normalization is forced" means

With dynamics (C3), coupling (λ = 16πG/c⁴), and readout (C5 v0.2) all fixed, the effective
TT-sector theory is linearized GR with no remaining conventions; its canonical/Isaacson
energy is then unique — there is nothing left to choose. The numerical closure (sphere-
integrated flux / Einstein luminosity = 1.000246, quadrature accuracy) confirms source-side
decay (1124's Peters) = field-side flux. And the cancellation theorem doubles as the energy
statement: the scalar/vector tails are constraint pattern, not dynamics — no independent
energy, no extra luminosity channel, the double-pulsar pass is real. A substrate-microscopic
re-derivation of (c⁴/32πG) is a refinement candidate (OPEN item for the registration patch),
not a debt: the effective theory is closed.

## Discipline notes

- Built on the pushed 1124 (architect's hash b9c1d52; re-synced before building).
- NO VERDICT MOVED: no THEO/PRED/ID registered (the TT-response result is a candidate
  theorem riding the axiom package; registration post-DG-3). Private-lane paths only; the
  1123 candidate text edited in-lane (C5 → v0.2 with changelog).
- Falsifiers honored: the symbolic computation would have displayed any non-TT dependence
  verbatim; the counterfactual run shows what failure looks like and that the test can see
  it. Had the completion NOT reproduced τ_GR, the step would have reported the packet one
  slot short and reopened Task 2.
- The construction phase (Tasks 1–4) is complete; all four obligations discharged; the
  package is DG-3-ready with two named review questions (Q1 completion rule status; Q2
  amendment-vs-addition accounting). Task 5 dispatch awaits the architect's "initiate review
  protocol."
