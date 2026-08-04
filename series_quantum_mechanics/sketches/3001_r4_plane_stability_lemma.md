# R-4 CLOSURE CANDIDATE — PLANE STABILITY UNDER THE GP REFRESH (THE 5-DESIGN LEMMA PACKAGE)

**Patch 3001 (4 Aug 2026).** Closes R-4 (registered CONV-014
adjudication E-4, severity medium–high) at derivation grade with a
verified bound, PANEL-PENDING. Verify script:
`series_quantum_mechanics/code/3001_r4_5design_check.py` — EXECUTED
this patch, ALL ASSERTIONS PASS, stdout in §6. This is the QM
re-ground arc's FIRST computational verify script; SCRIPT-EXECUTED
status becomes available at the next review round.

**The obligation (CONV-014 E-4):** prove the GP refresh preserves the
distinguished plane for the admitted pattern class (a bounding lemma
on out-of-plane perturbations under the tight-binding update), AND
establish the plane's existence for all quantum-relevant patterns
including stationary states.

---

## §1 — Setup and the case structure

At each GP, decompose SSV_net = S_∥ + S_⊥ against the distinguished
plane Π (normal n̂). The U(1) reduction is exact iff S_⊥ = 0 on the
pattern's support; the lemma bounds the S_⊥ generated per refresh.

The per-Moment refresh sums arriving per-edge contributions. The most
general single-edge transfer built from the edge direction v alone is

    T(v) = α I + β v vᵀ        (α: component-diagonal; β: direction-coupled)

Three channels can move S out of Π, and they have DIFFERENT statuses:

- **Channel A — component-diagonal transport (α).** The stencil acts
  identically on each Cartesian component.
- **Channel B1 — isotropic direction coupling (β, δ-built).**
  Grad-div–type terms; isotropic but component-mixing.
- **Channel B2 — lattice-anisotropic direction coupling (β,
  non-δ-built).** The only channel through which the LATTICE's
  discrete directions can torque the plane.

## §2 — L-1 (exact closure, Channel A): the shipped dynamics preserves the plane EXACTLY

The QM-1 evolution (Eq. evolution) applies one scalar stencil to the
site field — component-diagonal transport, α-only. A scalar stencil
cannot mix components: if the input field lies in Π everywhere, every
output component along n̂ is a linear combination of input n̂-components,
all zero. **Plane closure is exact, at all orders in Δs, for the
transport class the shipped papers use.** (Verified numerically for a
randomly oriented plane: out-of-plane fraction 4.3×10⁻¹⁷ = machine
zero; §6.) This alone discharges D-4 for the shipped model: the
worry "the Proposition does not verify that the GP refresh never
takes SSV_net out of the plane" is answered by construction for
α-transport — the shipped update literally has no operator that could
do it.

## §3 — L-2 (the 5-design bound, Channel B2): lattice anisotropy cannot act before sixth order

For the general β-kernel, the summed stencil's coefficients are the
directional moments M_n = Σ_j v_j^{⊗n} over the neighbor shell. The
600-cell's 3D neighbor shell is the icosahedron's 12 vertices (z=12;
the same object whose first and second moments the shipped Appendix A
already uses).

**Theorem input (spherical-design theory):** the 12 icosahedron
vertices form a **spherical 5-design** — every moment of order ≤ 5 is
exactly isotropic (odd orders vanish by parity; orders 2 and 4 are
δ-built). The first anisotropic moment is order 6. (Numerically
confirmed: order-4 anisotropic residual 1.9×10⁻¹⁶; order-6 residual
0.419; §6.)

**Consequence.** A β-kernel term with m gradient factors carries
total v-order 2+m. Lattice-anisotropic structure requires v-order
≥ 6, hence m ≥ 4: **the lattice-anisotropic out-of-plane channel is
suppressed as (kΔs)⁴ relative to the leading update.** Measured:
log-log slope 4.00 over three decades for in-plane-varying in-plane
fields on a random plane (§6). Negative control: on the octahedron
(a 3-design, first anisotropy at order 4) the same harness measures
slope 2.00 — the exponent tracks the design order, so the suppression
is a property of the icosahedral geometry, not of the test.

**Bound magnitude.** With Δs ≤ l_P (GP spacing is sub-Planck per the
registry) and λ ≥ λ_C(electron):

    ε_aniso per refresh ≤ (2π l_P/λ_C)⁴ ≈ 3.1×10⁻⁹⁰.

Even under worst-case fully coherent accumulation over N = t/t_P
refreshes, order-unity leakage would require t ≳ 10⁴⁶ s — some
sixty orders beyond any physical timescale. Lattice-sourced plane
leakage is negligible in the strongest sense available to the
programme.

## §4 — L-3 (Channel B1 is physics, not leakage): the isotropic direction-coupled channel is the longitudinal/spin sector

The isotropic β-terms (δ-built grad-div structure) CAN mix components
— but only by contracting the input vectors present: being built from
δ's alone, they cannot manufacture a direction not spanned by the
field and its wavevectors. Verified: with variation confined to Π,
their out-of-plane output vanishes into the (ks)⁴ anisotropic floor;
with variation along n̂, a (ks)² channel opens (slope 2.00 measured;
§6). That (ks)² channel is the **longitudinal/transverse split** —
the same structure that makes SF-6's radiation transverse — and, for
the matter pattern, tilt dynamics of the SSV_net direction. Its
status is therefore not "error to be bounded" but **the spin sector's
dynamics**: tilting the plane is precisely what a spin degree of
freedom does (QM-3's helix-axis = spin direction; QM-4's σ_z = SSV
projection). In the spinless Schrödinger regime the papers occupy,
this channel is inactive at the regime's order because the shipped
dynamics is Channel-A (L-1); where a β-coupling is physically
present, its effect is the known vector-wave/spin physics, handled by
the two-component formalism of QM-3/QM-4.

**O-R4-1 (registered observation, NOT claimed as theorem).** The
full configuration space this exposes — tilt direction on S² times
in-plane angle U(1) — is exactly the spinor structure of standard QM
(the Hopf fibration S³ → S² with U(1) fiber: Bloch vector = tilt,
phase = in-plane angle). If made rigorous, the out-of-plane degree of
freedom IS the spin degree of freedom and D-4's "leakage" dissolves
into the spin sector entirely. Registered as an observation and
candidate future theorem; not consumed by any claim in this package.

## §5 — L-4 (universality clause): the plane exists wherever ρ > 0, including stationary states

The panel's universality worry (DeepSeek): stationary states might
lack a periodic component. Under the corpus identification E = ħν_C
(total energy IS pattern rotation rate), a massive pattern's rotation
rate is ω = E/ℏ ≥ mc²/ℏ > 0 ALWAYS — "stationary" in the Schrödinger
sense means stationary ENVELOPE (ρ, and φ up to the global e^{-iEt/ℏ}
rotation), never a frozen pattern. The periodic component is nonzero
wherever ρ > 0; the plane is defined on the full support; the only
degenerate loci remain the ρ→0 nodes (recorded per CONV-014 as
consistency-by-construction). Massless patterns: the transverse
plane, per SF-6. Universality holds for the massive and massless
classes together.

## §6 — Verify stdout (EXECUTED, Patch 3001)

```
--- DESIGN CHECK: icosahedron (600-cell 3D neighbor shell, z=12) (12 vertices) ---
 order 1: odd moment |M|/N = 3.205e-17  (ZERO (parity))
 order 2: anisotropic residual (rel) = 0.000e+00  (ISOTROPIC)
 order 3: odd moment |M|/N = 1.388e-17  (ZERO (parity))
 order 4: anisotropic residual (rel) = 1.896e-16  (ISOTROPIC)
 order 5: odd moment |M|/N = 7.693e-18  (ZERO (parity))
 order 6: anisotropic residual (rel) = 4.193e-01  (ANISOTROPIC)
 first anisotropic order: 6
 PASS: 5-design confirmed (first anisotropy at order 6)

--- CLOSURE-A: scalar stencil (beta=0), random plane, normal n = [0.9632, 0.252, 0.0932] ---
 max out-of-plane fraction (any k direction, ks=0.5): 4.262e-17
 PASS: component-diagonal transport preserves the plane EXACTLY (all k)

--- SCALING-B: direction-coupled kernel (beta=1), in-plane-only variation ---
 icosahedron: out-of-plane fraction at ks=[0.3, 0.1, 0.03, 0.01] -> ['3.310e-06', '4.047e-08', '3.275e-10', '4.042e-12']; log-log slope = 4.00
 PASS: lattice-anisotropic out-of-plane channel suppressed as (ks)^4 (5-design)

--- CONTRAST-B2: same kernel, variation including the plane normal ---
 icosahedron/3D-k: out-of-plane fraction at ks=[0.3, 0.1, 0.03, 0.01] -> ['2.257e-03', '2.498e-04', '2.238e-05', '2.494e-06']; log-log slope = 2.00
 PASS: the (ks)^2 channel is the isotropic grad-div (longitudinal) physics, present only with normal-direction variation

--- NEGATIVE CONTROL: octahedron (3-design; first anisotropy at order 4) ---
 order 4: anisotropic residual (rel) = 6.325e-01  (ANISOTROPIC)
 first anisotropic order: 4
 octahedron: out-of-plane fraction ... log-log slope = 2.00
 PASS: control confirms the exponent tracks the DESIGN ORDER (icosahedron 4 vs octahedron 2)

--- BOUND MAGNITUDE --- (Delta s <= l_P; lambda >= lambda_C(e))
 relative anisotropic leakage per refresh  <= (2 pi l_P/lambda_C)^4 = 3.068e-90
ALL ASSERTIONS PASS
```

## §7 — Status, honest limits, and registrations

**R-4 status: CLOSURE CANDIDATE at derivation grade, PANEL-PENDING.**
What is proved vs. inherited:
- L-1 is exact and elementary (component-diagonal operators cannot
  mix components) — theorem-strength for the shipped transport class.
- L-2's mathematical input (the icosahedral 5-design) is a known
  theorem, numerically confirmed here; the (kΔs)⁴ suppression follows
  and is measured. The bound's PHYSICAL applicability assumes the
  microscopic transport is expressible in the T(v) = αI + βvvᵀ
  single-edge class; multi-edge-correlated transport kernels are
  outside this package's scope (registered limit).
- L-3's identification of the (ks)² channel with the spin sector is
  physical-argument grade, supported by the QM-3/QM-4 structure;
  O-R4-1 is an observation only.
- L-4 consumes the corpus E = ħν_C identification (SF-6 Tier 1).

**Enactment this patch:** QM-1 → v2.2 (the Grade remark's R-4 entry
updated from "registered obligation" to "closure candidate,
panel-pending, per this package"). The citation-bar scope (CONV-014
E-1) is UNCHANGED — bar movement requires adjudication of this
package at the next round, where SCRIPT-EXECUTED credit is now
available for the first time in the arc.

**Ledger:** DM untouched. QM: R-4 → CLOSURE-CANDIDATE (panel-pending);
OPEN-QMRG-B1 and OPEN-QMRG-UNIQ remain open (B1 is the next
campaign-independent target; its natural home is the QM-5 mode
machinery). Nothing minted.
