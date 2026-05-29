# Development — Chirality Derivations

Session vignettes for the chirality-derivations arc (Session 148, Patches 0632–0640), append-only.
The verbatim per-patch reasoning is in `reasoning/<patch>.md`; these are the curated
paragraph-form vignettes (Tier 3) pointing at it.

---

## Patch 0632 — THEO-CHIR-AUDIT-1 registered (the catalogue)

The 27-entry chirality entry-point enumeration was rebuilt after a working-window overflow and
registered as the new CHIR sector's founding theorem. It classifies every point where chirality
enters CPP (spatial/temporal/CP-asymmetric senses) as primitive / emergent / unregistered, with
the central finding that spatial chirality reduces to the single primitive `n̂`. The audit named
the three downstream targets this folder then discharged: E20 (conditional), E21 (emergent-P,
magnitude), E19 (the deepest unregistered entry).

## Patches 0633–0635 — the AUDIT-1 review cycle

A multi-AI review (Copilot referee-grade, Grok recompute+contribute, ChatGPT meta-review) was
run and integrated. No falsifier was produced; the v1.0→v1.1 calibration sharpened labels only
(graded emergent (E)/(P); E20 → unregistered-conditional; ZBW as exclusion X5). The cycle closed
3/3 on v1.1, and the audit `.tex` was frozen. Two reviewer seeds (Grok's E19 and E21 sketches)
were logged as starting structures, *not* closures — ChatGPT's calibration that a plausibility
sketch is not a derivation set the discipline for the derivations that followed.

## Patch 0636 — E20 resolved (THEO-CHIR-PCD-ORIENTATION-1)

The first downstream theorem. The key move was scoping it as a primitive-*count* question:
`ω_PCD = σ_cycle·n̂` is a product of two already-registered primitives, so no third primitive,
Scenario B refuted, E20 emergent. The §3 precondition (σ_cycle attributed to A1+A4, not the F.1
sketch's pre-canonical "A5") was cleared. Honest cap: emergent (provisional), inheriting the F.1
viability ceiling; the primitive count is robust to the three open F.1 commitments.

## Patches 0637–0638 — E21 / 1d-α resolved (THEO-CHIR-CHI-1)

The scope sketch (0637) found that `χ = φ⁻³` is a foundational input (FI-C-9) whose *value* has
a partial derivation (Finding C-3), corrected the audit's imprecise "CONT-1.3 addresses E21"
note (CONT-1.3 is inheritance, not derivation), and decomposed the gap into 1d-α (ratio
selection) + 1d-β (dynamics). The distance-spectrum exploration (0638) then *succeeded*: a
locality criterion (the symmetric bias of the two nearest 600-cell shells) uniquely selects
`φ⁻³`, excluding `1/√5` and `5−2√5` as non-local. 1d-α closed at Layer 2/2.5; the exponent
question ("why −3") retired. (A leftover patch file swept into the commit by `git add -A` was
caught and removed before delivery — the lesson logged.)

## Patches 0639–0640 — E19 resolved (THEO-CHIR-CAP-1)

The deepest unregistered entry. The scope sketch (0639) led with a no-false-reduction discipline
(E19 is consumed by three shipped theorems) and found the organizing insight: the capture
handedness, as consumed, is the SD-CHIR `ζ`-generator, an *involution* (registered geometry)
that carries no sign by itself — so capture handedness = `ζ × σ_capture`, parallel to E20. The
artifact (0640) ran the decisive 1c-β test by reading the SD-CHIR sign bookkeeping: the
matrix-element sign is carried by the edge-perturbation `ε(ê·n̂)`, whose sign is the `n̂` sign =
the FI-C-9 enantiomorph. **Verdict R1**: `σ_capture = sign(n̂) = FI-C-9`, no independent primitive,
E19 emergent. R3 (new primitive) refuted; R2 (merge with E20's temporal sign) left as a
hypothesis. A first verify-script version found the perturbation field zero on first-shell↔first-
shell edges — recognized as the local-`I_h`-preservation theorem (tangency), not a bug, and the
check moved to the bias-carrying first→second-shell edges.

## Patch 0641 — this documentation-suite consolidation

At the three-derivations milestone, the per-patch verbatim reasoning + scripts (captured
throughout per the reasoning-capture protocol) were consolidated into this `documentation_suite/`
plus the folder README. No physics changed; this is the synthesis layer over the canonical
Tier-4 fragments.
