# Spin-2 Task 4 — THE READOUT, THE TT-ONLY RESPONSE, AND THE ENERGY CLOSURE: Eardley class N₂, the kill switch survives — and the assembly needed exactly one completion rule, which conservation supplies for free (Patch 1125)

**Sub-arc:** `series_relativity/op_einstein_closure/spin2_construction/` · **Charter:** `README.md`
· **Verify:** `code/1125_task4_tt_response_energy.py` · **Revises:** C5 of
`1123_task2_axiom_text_A3prime.md` (v0.2, changelog in that file)
**Status:** Task 4 of the construction phase. **OB-2 part 2 DISCHARGED** (conditional on C5
v0.2, flagged as an explicit DG-3 question). **OB-1 COMPLETED** (energy closure). **OB-4
DISCHARGED.** All four obligations of the candidate axiom are now discharged; the package is
DG-3-ready. **NO VERDICT MOVED.**

---

## 1. The kill switch, sharpened — and why this was the arc's most dangerous step

The OB-2 question as posed was "do Q's helicity-0, ±1 components radiate strain?" Planning the
derivation exposed the *real* trap, which is worse: **the scalar and vector channels have
their own radiative 1/r tails.** Any massless field sourced by ρ radiates at quadrupole order
in the retardation expansion — Φ_rad ∝ (1/r) n̂n̂:M̈(t_ret) — and the same for the vector. If
those tails entered the effective metric uncanceled, CPP would predict breathing- and
longitudinal-mode strain at *Newtonian coupling strength* (no Brans–Dicke 1/ω suppression
available — CPP's scalar IS Newtonian gravity), and an extra radiative energy channel that
would shift binary decay rates at O(10%) — flatly excluded by the double pulsar's 10⁻⁴
agreement. GR survives the identical trap through a conservation-enforced cancellation in the
*curvature*. Task 4's job: prove CPP's assembly inherits it. It does — with one discovery
along the way.

## 2. P1 — The cancellation theorem (symbolic, exact)

For a plane wave h̄_μν(t − z/c) satisfying the four conservation-inherited constraints
∂^μh̄_μν = 0 (which the retarded solutions of □h̄_μν = −λT_μν with conserved T satisfy
*automatically*: □(∂^μh̄_μν) = −λ∂^μT_μν = 0, and the sourceless retarded solution vanishes),
the tidal response computed by direct symbolic evaluation of the linearized Riemann tensor is

> **R_{i0j0} = [[−(H_xx−H_yy)″/4, −H_xy″/2, 0], [−H_xy″/2, +(H_xx−H_yy)″/4, 0], [0,0,0]]**

— it depends **only on the two TT combinations**. The scalar tail (H_tt), the vector tails
(H_tx, H_ty), the longitudinal components (H_xz, H_yz, H_zz), and the transverse trace
(H_xx+H_yy) **cancel exactly in the curvature**. (Structural reason: the constraints leave 6
free functions; the 4-parameter residual gauge acts within them; the curvature is
gauge-invariant, so it can depend on only 6−4 = 2 combinations — the TT pair. Verified by
direct computation, not just the counting argument.) Breathing, longitudinal, and vector-mode
responses are identically zero: **Eardley class N₂, the same as GR.**

## 3. P2 — The assembly, and the discovery: the trace is redundant

The theorem requires the channels to assemble into a constraint-satisfying h̄_μν. CPP's nine
channels map onto h̄_00 (scalar), h̄_0i (vector), h̄_ij^{TF} (Q) — but the harmonic pattern has
a **tenth component, the spatial trace τ = h̄_kk** (sourced by T_kk), which the packet does not
carry. Is the packet one slot short? **No — τ is redundant.** The conservation structure
determines it locally from the channels the packet *does* carry:

> **∇τ = 3(∂_t h̄_{0i} − ∂_j Q_{ji})**  (local form);  **τ = 3(h̄_tt − n̂n̂:Q)**  (wave-zone form)

— gradients across the PSR shell being exactly what the Compute step already perceives.
Verified numerically on an eccentric binary: the completion reproduces GR's
τ = (2G/c⁴r)M̈_kk to 4×10⁻¹⁹. Note what this ratifies: a spatial trace is rotationally an
l=0 object — a *second scalar* — and the completion theorem (1123) said the packet carries
every protected irrep **exactly once**. Physics agrees with the geometry: conservation makes
the second A-slot unnecessary. (Statics consistency: τ_static = ∫T_kk = 0 by the virial
theorem — which is *why* c07/c08's static recovery never noticed the slot.)

**C5 (v0.2) — the constraint-consistent assembly:** the Compute step assembles the unique
constraint-consistent (harmonic-pattern) effective metric from the nine packet channels —
h̄_00 ← Φ, h̄_0i ← V, h̄_ij ← Q + ⅓δ_ij τ with τ the conservation completion above — and the
displacement rule follows its geodesics (the existing c07 PCD→geodesic machinery, unchanged).
**Honesty flag for DG-3 (explicit review question):** is the completion rule *derived-unique*
(our position: it adds no degrees of freedom; it is the only assembly that does not violate
identities the retarded channels already satisfy; it reduces exactly to c07's map in statics)
or an independent postulate that should be scored as axiom content?

## 4. P3 — The six-mode test on the armed trap (eccentric binary)

Circular orbits hide the danger (M̈_kk = μ d²(a²)/dt² = 0), so the test uses e = 0.6, where the
trace radiates. With the completed assembly: **breathing, longitudinal, and both vector
responses vanish to finite-difference precision (≤ 4×10⁻¹¹ of the tensor amplitude)**, and the
surviving response equals −½ḧ^TT (residual 2.4×10⁻¹¹). **Counterfactual, documented:** drop
the completion (τ = 0) and O(1)-relative breathing+longitudinal violations appear (2.6×10⁻² of
tensor for this orbit, scaling with M̈_kk) — the completion is load-bearing precisely for the
eccentric and inspiraling sources LIGO actually sees. F1 (the polarization falsifier) is now
fully armed in both directions: CPP+A3′ predicts pure tensor (N₂); any first-order
breathing/longitudinal/vector detection kills it.

## 5. P4 — The energy closure (OB-1 completed; the double-pulsar pass is real)

Integrating the Isaacson flux (1/32π)⟨ḣ^TT ḣ^TT⟩ of the assembled wave over the sphere for a
circular binary returns the Einstein quadrupole luminosity to quadrature accuracy (**ratio
1.000246**). Three consequences: (i) the field-side flux equals the source-side Peters decay
used in 1124 — energy is conserved; (ii) the (c⁴/32πG) normalization is now *forced*: with
dynamics, coupling, and readout all fixed, the canonical energy of the effective dynamics has
no remaining freedom — OB-1's last debt is paid (a substrate-microscopic re-derivation of the
same number is a nice-to-have refinement, not a debt of the axiom; candidate OPEN item for the
eventual registration patch); (iii) **the scalar/vector tails carry no independent energy** —
they are constraint pattern, not dynamics — so there is **no extra luminosity channel**, and
the double pulsar's 10⁻⁴ agreement is a genuine pass rather than an unexamined assumption.

## 6. OB-4 — discharged by architecture

Matter couples to Q **only** through the assembled metric (C5): the ZBW capture dynamics and
hadron binding see Q solely as a metric perturbation (tidal effects — physically required and
utterly negligible at hadronic scales: the strain across a femtometer from any astrophysical
source is ~10⁻²¹·(fm/km)-class). Emergent spin-½ and configurational l=2 are untouched. No
double-counting channel exists by construction.

## 7. The construction-phase ledger (Tasks 1–4 complete; the package is DG-3-ready)

| Item | Status |
|---|---|
| Flow choice (Task 1) | **B — the LSP broadcast**; precedent ladder; A/C eliminated |
| Axiom text (Task 2) | **A3′ candidate v0.2** — completion theorem; zero parameters |
| Coupling + waveform (Task 3) | **λ = 16πG/c⁴**; Einstein quadrupole formula derived; Hulse–Taylor + double pulsar with nothing tuned |
| OB-1 (quadrupole formula + energy) | **DISCHARGED, COMPLETE** (flux = luminosity, normalization forced) |
| OB-2 (polarization suppression) | **DISCHARGED** — parts 1 (no monopole/dipole) + 2 (TT-only response; Eardley N₂); conditional on C5 v0.2, flagged for DG-3 |
| OB-3 (statics untouched) | **DISCHARGED as theorem** (perfect-fluid + virial) |
| OB-4 (no emergent double-counting) | **DISCHARGED by architecture** |
| Falsifiers | F1 armed both directions (pure tensor or dead); F2 (c), F3 (multiplet integrity), F4 (dispersion ceiling) standing |

**Next: Task 5 — the DG-3 dispatch.** The submission package: the candidate axiom (1123,
v0.2) + the four discharge documents (1121, 1124, 1125) + the diagnostic record (1112–1120),
with the two named review questions: (Q1) C5's completion rule — derived-unique or postulate?
(Q2) the dual count-accounting — amendment (9) or addition (10)? Per CONV-001, one fenced
single-block package per reviewer; per the dispatch protocol, on the architect's "initiate
review protocol" command.
