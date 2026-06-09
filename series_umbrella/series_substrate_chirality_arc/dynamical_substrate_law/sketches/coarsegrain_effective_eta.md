# Coarse-Graining Probe: the Effective η-Field Resolves to the Canonical m=12 Indicator → Primitive Lean (no PCD insight required to get here)

**Patch:** 0820 (Session 156, 8 June 2026) · **Type:** infrastructure result · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Predecessor:** K_lift derivation (0819). **Verify:** `code/0820_coarsegrain_effective_eta.py`. **For:** the chirality lane (the K_lift / effective-η input they were stuck without).

---

## The question this probe answered

0819 reduced the chirality verdict to one quantity — the effective η-field's d.o.f.-structure (equivalently K_lift) vs K_c = 1/12 — and showed it's a knife-edge: the verdict hinges on which effective η-field the dynamics produces (full-vertex-figure → primitive; more-local → emergent). This probe attempts to **pin that by coarse-graining the Mechanism-A dynamics**, and to find out whether it resolves mechanically or bottoms out at the PCD layer.

## Result: it resolves toward primitive, and did not bottom out at the PCD layer

Three findings, the first two from direct computation (verify 0820), the third structural:

1. **The canonical local enantiomorph reads all 12 incident edges.** The geometrically/physically canonical local handedness is the orientation of the *whole* vertex figure (the icosahedron of 12 neighbours) — a **symmetric** function reading all 12 incident edges with equal weight (reading-weight participation ratio = 12 by construction). A 4-edge determinant reads only 4 (→ emergent) but is a *non-canonical, arbitrary* 4-subset choice; the geometric enantiomorph is the symmetric all-12 object.

2. **Direct MC of an explicit geometric pseudoscalar confirms weak coupling for the m=12 indicator.** For the canonical (m=12) η: `C_nn ≈ −0.054`, i.e. `|K_lift|/K_c ≈ 0.65` → **off-critical → primitive**. (The arcsin estimate of 0819 is validated by an explicit pseudoscalar.) The coupling came out **antiferromagnetic**; on the frustrated icosahedral/600-cell structure that *further* disfavours ordering — a supporting point, not load-bearing. The load-bearing result is simply `|K_lift| < K_c`.

3. **The Mechanism-A bias polarises but does not drive criticality.** The bias `δ(ê·n̂)` shifts edge *means* (the tilt → ⟨η⟩≠0, the harmless O(δ) homogeneous skew already handled in 0814) but leaves the reading *weights* uniform → `m_eff` stays 12, and the *connected* coupling is ≈δ-independent (MC: `C_nn ≈ −0.054` at δ=0 and `−0.059` at δ=0.10). So the bias does not concentrate the reading or push the coupling toward `K_c`.

**Net:** coarse-graining selects the canonical symmetric full-vertex-figure edge-pattern η (the 0906 actualization), giving `|K_lift|/K_c ≈ 0.65 < 1` → **primitive (V3) lean** — derived from geometry + weak bias + mean-field, **without requiring the PCD mechanism**. And the true `K_c` exceeds the mean-field `1/12`, so the margin is only *safer*.

## What this is — and is not (for the chirality lane / DG-3)

This is the **K_lift / effective-η input** the chirality lane needs to run its VW-1/verdict machinery toward CAPACITY-1 (V3 confirmed / V1 excluded). It is **not** a verdict — I assert none. It is a defensible *primitive lean* at a stated rigor level (geometric-canonical η + weak-bias + mean-field), with a sharp, named residual gap rather than a diffuse wall.

## Residual gaps (the only places insight or further rigor could still be needed)

1. **Dynamical = geometric η.** This assumes the *dynamically-selected* effective η (the actual slow mode of Mechanism A) is the *geometrically-canonical* symmetric vertex-figure indicator. There is no evident mechanism making it more local, but "no evident mechanism" is not a proof. Confirming this is the residual rigor step — and it is the one spot where physical insight *could* enter, though it looks like a tractable slow-mode identification, not a creative-mechanism task.
2. **Mean-field K_c.** The comparison uses mean-field `K_c = 1/12`; the true value is higher (favourable). A lattice computation of the true `K_c` would tighten the margin.
3. **Frustrated AFM non-ordering.** The antiferromagnetic coupling on the frustrated lattice almost certainly does not order, but that should be checked rather than assumed.

None of these is the "imagine a new PCD mechanism" showstopper. The probe took the verdict to a **defensible primitive lean without the PCD layer**, and localized what remains to sharp refinements.

## Scope held

Infrastructure (effective-η coarse-graining + K_lift confirmation). **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Mean-field map and the geometric-canonical-η assumption flagged. Conditional on Mechanism A (OPEN-FP-F1-2). Coordinated hand-off to the chirality lane.
