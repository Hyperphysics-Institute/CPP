# Glossary — Chirality Derivations

Terms specific to the chirality-derivations sub-corpus. Programme-wide terms are in
`master_glossary.md`; this glossary covers the constructs introduced or made load-bearing by the
three derivation theorems.

**Primitive-count theorem.** A theorem that decides *how many independent primitives* a quantity
introduces, rather than its magnitude. THEO-CHIR-PCD-ORIENTATION-1 is one: it shows `ω_PCD` is a
product of two already-registered primitives, hence introduces no third — without computing its
magnitude. The economy is that the count is robust to open commitments that the magnitude is not.

**Symmetric-bias generator.** The functional `β(d_i,d_j) = (d_j − d_i)/(d_j + d_i)` of a pair of
600-cell distances, taken as the form of the chirality-magnitude generator (THEO-CHIR-CHI-1
Definition 3.1). A scale-free left/right imbalance of two characteristic lengths. The *form* is a
structural assumption; the *pair* is selected by the locality criterion.

**Locality criterion.** The rule selecting the symmetric bias of the host vertex's two *nearest*
distance shells (`φ⁻¹` icosahedron, `1` dodecahedron) — equivalently the unique adjacent
shortest pair. It uniquely yields `χ = φ⁻³` and excludes `1/√5` (edge↔φ-shell) and `5−2√5`
(edge↔antipode) as non-local. The geometric content: the two nearest shells are the
icosahedron+dodecahedron vertex-figure neighborhood where `n̂` breaks `H₄ → I_h`.

**ζ-involution.** The SD-CHIR `Z₂` pairing-convention generator, identified as the consumed
capture handedness. `ζ^W: p ↦ φn̂ − p` (icosahedral-center inversion in 4D, linear part `−I`
flipping `n̂`); `ζ^qDP` adds the qCP-sign flip (A1 charge-conjugation). Being an involution
(`ζ² = 1`), it relates a configuration to its `n̂`-flipped partner but **carries no handedness
sign by itself** — hence the involution × sign factorization.

**Involution × sign.** The structural form `(handedness) = ζ (registered geometry) × σ (sign)`,
shared by E20 (`ω_PCD = σ_cycle·n̂`, axis × sign) and E19 (`capture = ζ × σ_capture`). Isolates
the open question to the *sign* once the geometry is registered.

**σ_cycle.** The handedness of the temporal primitive — which of P→C→D or D→C→P is forward.
Carried by A1 (the perceive/respond steps) + A4 (the Absolute-Moment cadence). The sign factor of
E20. *Temporal.*

**σ_capture.** The handedness sign of the capture/partnering step (the sign factor of E19).
THEO-CHIR-CAP-1 verdict R1: `σ_capture = sign(n̂) = `the FI-C-9 enantiomorph. *Spatial.* Whether
`σ_capture = σ_cycle` (the merge) is the open E19/E20 cross-link.

**FI-C-9 enantiomorph sign.** The frozen substrate-vacuum chirality sign — the choice of `n̂` vs
`−n̂`, equivalently which of the two mirror-image 600-cells is the actual substrate. "A frozen
boundary condition coeval with the existence of CPs." Consumed (not derived) by all three
theorems; its derivation is sub-gap 1d-β.

**Edge-perturbation pattern.** The first-shell field `δ(e) = ε(ê·n̂)` carrying the chirality
bias. Odd under `n̂ → −n̂`, so the matrix-element sign tracks `n̂` (the basis of CAP-1 verdict R1).
Vanishes on first-shell↔first-shell edges (those are tangent to `n̂`).

**Local-`I_h`-preservation.** Finding C-W39: the first-shell icosahedron at `v_host` is preserved
as `I_h`-symmetric at first order, with all first-shell↔first-shell edges tangent to `n̂`
(`ê·n̂ = 0`). Consequence here: the chirality bias lives on first→second-shell edges, not the
nearest-shell edges.

**Sub-gaps 1d-α / 1d-β.** The decomposition of OPEN-CHIR-1d (derive `χ = φ⁻³`): **1d-α** = ratio
selection (closed by THEO-CHIR-CHI-1 via locality); **1d-β** = the symmetry-breaking dynamics
that select the broken chiral phase, eliminating FI-C-9 (deep, deferred to F.1 §14.17 / OPEN-SM-4
↔ SS-corpus).

**Verdicts R1 / R2 / R3 (E19).** The three candidate resolutions of `σ_capture`: **R1** = the
FI-C-9 enantiomorph (→ E19 emergent; *confirmed*); **R2** = `σ_cycle` (→ merge E19+E20;
*hypothesis*); **R3** = an independent new primitive (→ register E19; *refuted*).

**emergent (E) / emergent (P) / unregistered / registered-primitive.** The audit's calibrated
classification labels: emergent (E) = a registered derivation exists; emergent (P) = reducible in
principle, derivation owed/provisional; unregistered = consumed but not yet placed;
registered-primitive = an acknowledged irreducible input. E20 and E19 resolved to emergent (P);
E19's alternative outcome would have been registered-primitive (R3, refuted).

**No-false-reduction discipline.** The rule (CAP-1 §0) that every reduction step must terminate in
a registered object; a step importing an unregistered object is a gap, not a closure. Applied to
E19 because a spurious reduction there would relabel the load-bearing ζ-inputs of three shipped
theorems as results.
