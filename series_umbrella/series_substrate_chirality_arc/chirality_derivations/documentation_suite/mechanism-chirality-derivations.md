# Mechanism — Chirality Derivations

How the three audit-downstream derivations work, as one mechanism. Synthesized at Patch 0641
from the Tier-4 reasoning fragments (`reasoning/0635–0640.md`) and the three artifacts.

---

## 0. The shared substrate handle: `n̂`

Every CHIR derivation consumes the same chirality input: the primitive 4D direction `n̂`
(FI-C-RC-1), vertex-aligned at the host (`n̂ = v_host`, FI-C-RC-2), under which the substrate's
`H₄` symmetry breaks to the residual `H₃ = I_h` at the host vertex. The audit's central finding
is that *all spatial chirality reduces to `n̂`*; the three derivations are the discharge of that
claim for the three entries the audit left conditional or unregistered.

Two further registered inputs recur: the 600-cell geometry (A2) and the single substrate
chirality datum **FI-C-9** (the magnitude `|χ| = φ⁻³` and the frozen enantiomorph **sign**,
i.e. the choice of `n̂` vs `−n̂`). FI-C-9 is *consumed* by all three theorems and *eliminated*
by none — its derivation (the symmetry-breaking dynamics) is the deferred sub-gap 1d-β.

---

## 1. E20 — the PCD-cycle orientation (THEO-CHIR-PCD-ORIENTATION-1)

**Mechanism.** The PCD cycle's orientation pseudovector factors as
`ω_PCD = σ_cycle · n̂`: the axis is `n̂` (inherited from the F.1 Phase-1 net DI-bit current
being `∥ n̂`), and the sign is `σ_cycle`, the handedness of the temporal primitive (the ordered
Perceive→Compute→Displace cycle, carried by A1 + A4). Both factors are already-registered
primitives (E16 spatial axis; E2/E5/E17 temporal sign), so `ω_PCD` introduces **no independent
third primitive** — Scenario B (ω_PCD an independent primitive) is refuted, and E20 is emergent.

**Why it is a primitive-*count* result.** The theorem deliberately answers "how many independent
primitives?" not "what is the magnitude?". This is what makes it robust: the three open F.1
commitments affect representation/explicitation/magnitude, but none reintroduces an independent
direction or handedness, so the count is firm while the magnitude stays provisional.

---

## 2. E21 — the chirality magnitude `χ = φ⁻³` (THEO-CHIR-CHI-1)

**Mechanism.** The magnitude is the **symmetric bias** of a 600-cell distance pair:
`χ = (d₂−d₁)/(d₂+d₁)`. The host vertex's chord spectrum has eight shells; a **locality
criterion** — the bias of the two *nearest* shells, `d₁ = φ⁻¹` (the 12-vertex icosahedral vertex
figure) and `d₂ = 1` (the 20-vertex dodecahedral next shell), the local neighborhood where `n̂`
breaks `H₄ → I_h` — uniquely gives
`χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻²/φ = φ⁻³`. The exponent `−3` is then fixed (numerator `φ⁻²`,
denominator `φ`). The literature alternatives are excluded as **non-local**: `1/√5` is the
edge-to-`φ`-shell bias (skips three shells), `5−2√5` the edge-to-antipode bias (the global
extreme).

**What it does and does not settle.** It selects the *ratio* (sub-gap 1d-α, closed); it assumes
the symmetric-bias *form* of the generator (a stated structural input); and it does not derive
the symmetry-breaking dynamics (1d-β). So it answers "why exponent −3" — by answering "why the
two-nearest pair" — without eliminating FI-C-9.

---

## 3. E19 — the capture/partnering handedness (THEO-CHIR-CAP-1)

**Mechanism.** The capture handedness, as consumed by the SD-CHIR theorems, is the `Z₂`
pairing-convention generator `ζ`, which factors as **`ζ` (a registered-geometric involution)
× `σ_capture` (a sign)**. `ζ^W: p ↦ φn̂ − p` (icosahedral-center inversion, from `n̂` + A2) is an
involution whose linear part `−I` flips `n̂` but which carries no handedness by itself; `ζ^qDP`
adds the qCP-sign flip (A1 charge-conjugation). The decisive question is the sign `σ_capture`:
reading the SD-CHIR sign bookkeeping, the chirality matrix-element sign is carried by the
edge-perturbation pattern `ε(ê·n̂)` (odd under `n̂ → −n̂`), whose sign is the `n̂` sign — which
*is* the FI-C-9 frozen enantiomorph ("any primitive direction picks one enantiomorph"). So
`σ_capture = sign(n̂) = FI-C-9`: **no independent third primitive; E19 emergent.**

**The local-`I_h` subtlety.** The chirality bias does *not* live on the nearest-shell edges:
first-shell↔first-shell edges are tangent to `n̂` (`ê·n̂ = 0`, the local-`I_h`-preservation
theorem), so the bias is carried by the first→second-shell edges. The sign still tracks `n̂`.

---

## 4. The unified picture (and its open seam)

Across the three: `n̂` is the spatial axis everywhere; the 600-cell supplies the geometry
(the shells for E21, the inversion for E19); and **one substrate chirality datum (FI-C-9)**
supplies both the magnitude (E21) and the sign (E19). The E20 and E19 results share the same
*axis/involution × sign* shape.

The open seam: E19 pins the **spatial** sign to `sign(n̂) = FI-C-9`; E20's sign is the
**temporal** `σ_cycle`. The unifying hypothesis — `σ_cycle = sign(n̂)`, so one enantiomorph
fixes spatial capture, temporal cycle, and n̂-orientation together — would merge E19 and E20
onto a single sign primitive. It is plausible (the FI-C-9 note calls the chirality "a property
of the substrate vacuum state itself, more primitive than any dynamical event") but **unproven**,
and is the natural next structural target after the dynamics (1d-β).
