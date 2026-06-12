# Reasoning capture — Patch 1124 (Task 3: the coupling and the quadrupole formula)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1124_task3_coupling_quadrupole_formula.md` + `code/1124_task3_quadrupole_verification.py`.

---

## The defect caught in my own v0.1 drafting (the patch's first result)

Planning the retarded-solution chain immediately exposed C4 v0.1 as ill-formed. I had written
the source as κ ∂²_t[q_ij] with q_ij a "quadrupole density." Two failures: (1) a density of
the form ρ(x)·x_i x_j is **origin-dependent** — under x → x + a it shifts by dipole and
monopole terms, so it cannot be a legitimate local law; (2) physically, a Planck-scale GP
cannot "perceive the binary's quadrupole" — the quadrupole of an extended system is not local
data. The repair is the structure GR itself uses: source by the **local traceless stress**
T_ij^{TF} (momentum-flux density — origin-independent, genuinely local, assemblable from CP
momentum flux), and let the quadrupole *emerge in the far field* through the conservation
identity ∫T_ij d³x = ½M̈_ij. Flagged prominently rather than silently patched: catching one's
own drafting defect in derivation is exactly what the candidate-then-review process is for,
and DG-3 should see the correction trail.

The repair pays three dividends: the law is local and clean; the no-static constraint
*upgrades from clause to theorem* (perfect-fluid T^{TF} = 0 identically; tensor virial for any
bounded static system); and conservation becomes load-bearing in the radiation chain — which
is where OB-2 needs it to live.

## How λ was fixed (and what is convention vs physics)

Chain: □Q = −λT^{TF} → far-zone retarded solution Q = (λ/8πr)M̈^{TF} → match to GR's
h̄_ij = (2G/c⁴r)M̈_ij under the **strain-valued readout convention** (Q enters the metric map
as the TT strain, dimensionless). Result: λ = 16πG/c⁴. Honesty about the convention: the
*number* 16π is convention-laden (a rescaled Q with a rescaled readout gives a rescaled λ);
the **physics claim is convention-free**: the tensor sector's coupling is fixed by the scalar
sector's G with no independent dial — one degree of freedom, zero parameters. The observable
chain (Peters decay, strain amplitudes) is invariant under the convention.

Checked the factor chain twice (the classic 4↔2↔½ trap): GR retarded solution
h̄ = (4G/c⁴)∫T/|x−x′| → far (4G/c⁴r)∫T = (4G/c⁴r)(½M̈) = (2G/c⁴r)M̈. CPP:
(λ/4πr)(½M̈) = (λ/8πr)M̈. Equate: λ/8π = 2G/c⁴ ⇒ λ = 16πG/c⁴. ✓ (Also the sanity anchor:
□h̄ = −(16πG/c⁴)T is the textbook harmonic-gauge equation — the matching had to land there.)

## Why the luminosity is "inherited" rather than re-derived (and the remaining debt)

With λ fixed, the Q-sector field equations are *term-for-term* linearized GR's TT sector. The
Einstein luminosity P = (G/5c⁵)⟨Q⃛Q⃛⟩ then follows by isomorphism — *provided* the field's
energy normalization is the standard one ((c⁴/32πG)⟨ḣ²⟩ Isaacson density). That normalization
is a property of the shell-sum dynamics' energy bookkeeping, not of the wave equation alone —
so it is booked into Task 4 (it is the same calculation as the readout, since both are "what
does the Compute step assign to a given Q amplitude"). Stated explicitly in the step doc so
the inheritance is not mistaken for a free lunch.

## OB-2's two halves (why part 1 falls now and part 2 doesn't)

Part 1 (no monopole/dipole radiation) is a property of the **source expansion**: the identity
chain consumes mass conservation (kills monopole) and momentum conservation (kills dipole),
both anchored in CPP (CP-count rules in c07; displacement-rule momentum bookkeeping — whose
formal CPP statement is itself part of the Task-4 work). Consequence promoted loudly: the
no-dipole leg of the evidential preamble is now a *derived consequence* of A3′.

Part 2 (helicity-0,±1 of the *propagating* field) is a property of the **readout**: all five
components of Q arrive at 1/r; in GR the non-TT pieces carry no 1/r curvature (the
conservation-constrained component relations cancel them in Riemann); CPP must show the C5
differential-strain response is TT-only by the analogous cancellation. That is genuinely
Task-4 work and remains the axiom's kill switch — kept loudly open.

## Numerical checks and sources of the reference values

- Conservation identity on an e = 0.6 Kepler binary: residual 6×10⁻⁷ (velocity-Verlet,
  numerical second differences — residual is differentiation noise).
- Peters decay with λ-fixed quadrupole luminosity: B1913+16 (P_b = 0.322997448918 d,
  e = 0.6171340, 1.438/1.390 M☉ — Weisberg–Huang 2016 reference values) → −2.4031×10⁻¹²
  against the literature GR value −2.4026×10⁻¹² (difference = input rounding);
  J0737-3039 (P_b = 0.10225156248 d, e = 0.0877775, 1.3381/1.2489 M☉ — Kramer et al. 2021)
  → −1.2483×10⁻¹² against literature −1.2479×10⁻¹². Observed/GR ratios quoted from the
  literature as reference context (0.9983 ± 0.0016; 0.999963 ± 0.000063).
- GW150914-class strain order: ~3×10⁻²¹ from the waveform formula (order-of-magnitude check
  against ~10⁻²¹ observed; no calibration attempted).

## Discipline notes

- Built on the pushed 1123 (architect's hash 1d3cdd3; re-synced before building).
- The DG-3 question from the architect answered from the corpus: DG-N = "Decision Gate N"
  (established usage, e.g. the Patch-0652 theorem-registry entry's DG-1…DG-5); "the DG-3
  swarm" is the programme's standing name for the three-reviewer adversarial gate
  (ChatGPT + Copilot + Grok). A master_glossary pin is a candidate item for the eventual
  registration patch (contested file — not touched now).
- NO VERDICT MOVED: no THEO/PRED/ID registered; results ride the candidate axiom pending
  DG-3. Private-lane paths only. The 1123 candidate text edited in-lane (v0.1 → v0.2 with
  changelog) so reviewers receive one current document.
- Falsifier honored: had the conservation identity failed numerically, or had the matching
  required a coefficient inconsistent with the scalar-sector G, the step would have reported
  OB-1 undischargeable as stated.
