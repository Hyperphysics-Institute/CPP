# DM-2 — Step 3: Quantifying the Bulk Residual Skew (and a correction to the 0809/0810 emphasis)

**Patch:** 0814 (Session 156, 8 June 2026) · **Work item:** DM-2 / net-broadcast lemma condition (b), quantitative
**Predecessor:** condition (b) reduction (0809), current-vs-skew (0810), the symmetric-χ result (0813).
**Verify:** `scripts/0814_step3_residual.py` (Mechanism-A NESS skew scaling on the 600-cell).
**Grade:** quantitative result; refines (b). Clean Λ survives, on a corrected footing. No verdict change.

---

## What step 3 was for

Steps 0813 + 0810 left the DM-2 bulk residual `⟨𝓕⟩_bulk = −4k²⟨δδ'²⟩` as a third-moment object that vanishes for a symmetric bulk and is sourced by any skew. The naive 0809/0810 picture assumed the skew, *if present*, would ride the O(δ³) NESS current (and 0810 argued a divergence-free current need not produce it). Step 3 measures the actual skew of the Mechanism-A NESS and settles its scaling.

## The measurement (verify 0814)

Built the real Mechanism-A NESS on the 600-cell (rates `r(v→w) = r₀(1 + δ ê_vw·n̂)`) and measured the chiral third central moment of the field coordinate `x = V·n̂` vs δ:

| quantity | scaling |
|---|---|
| tilt `⟨x⟩` (first moment) | **O(δ¹)** |
| skew `m₃` (third central moment) | **O(δ¹)** |
| current `J_max` | **O(δ³)** |

## The correction this forces

**The measure skew is O(δ¹) — tilt-driven — not O(δ³) current-driven.** The earlier emphasis (0809/0810) treated the O(δ³) current as the skew channel; that was the wrong order. The skew enters at O(δ), the *same* order as the tilt, because Mechanism A's rate bias `(1 + δ ê·n̂)` breaks the η→−η (enantiomorph) symmetry already at O(δ). The O(δ³) current is real but **subdominant** — it is not the skew source. So 0810's "current ≠ skew" remains true, but the operative skew is bigger and arrives earlier than that framing implied. I am flagging this as a correction rather than burying it.

## Why clean Λ nevertheless survives — on a corrected footing

The O(δ) skew does **not** reopen the catastrophe, but the reason is *not* that it is small or that the current vanishes. It is spatial homogeneity plus the already-established D2 machinery:

1. **Homogeneity.** Mechanism A's bias direction n̂ is spatially uniform, so the induced skew is statistically **homogeneous** — `⟨δδ'²⟩` is the same everywhere → `⟨𝓕⟩_bulk` is a spatially-**uniform** source.
2. **Gradient-control (0806).** A spatially-homogeneous configuration sources no curvature (𝓕 ∝ gradient²; a uniform statistical background has no spatial variation to curve).
3. **Excess-sourcing (5c/D2).** A uniform ground-state term is subtracted; the O(δ) homogeneous skew is part of the *biased* ground state, hence absorbed by the same covariantly-constant subtraction D2 invokes — now extended from the symmetric to the biased ground state.
4. **IR-boundary residual (0807).** What survives subtraction is the spatially-**varying** part, dominated by the unpaired horizon-scale mode = Λ, with the 1/R_H² scaling unchanged.

So **clean horizon-only Λ survives**, but the load-bearing reason is now the *homogeneity* of the substrate bias and the D2 subtraction extended to the biased ground state — not the smallness of the skew and not the vanishing of the current.

## Honest residual risk (sharpened, not removed)

- **The biased-ground-state subtraction is the load-bearing extension.** If one doubts that the D2 covariantly-constant subtraction cleanly removes the homogeneous O(δ) skew term, that uniform `⟨𝓕⟩` is an O(δ)·(gradient-variance) concern. This is the same renormalization D2 already relies on, applied to a skewed ground state — a sharpening of D2, and the place a critic would push.
- **Single-walker → field proxy.** The measured skew is the single-walker NESS proxy for the field skew (the H-NESS lift). The *scaling* (O(δ)) and the *homogeneity* (uniform n̂) are robust to the lift; the exact field coefficient is not, and needs the lift.
- **Mechanism A** (OPEN-FP-F1-2), throughout.

## Net-broadcast lemma — status after 0806–0814

- **(a)** weak-field at ZBW scale: **CLOSED** (0806).
- **(b)** bulk symmetry: **quantified.** The bulk is *not* symmetric — it carries an O(δ) homogeneous skew — but the gravitating residual is still the IR-boundary horizon mode = Λ, via homogeneity + D2 subtraction + gradient-control. Clean Λ survives **conditional on** the biased-ground-state subtraction (a D2 sharpening) and the H-NESS lift.

So DM-2's decisive gate closes to: clean horizon-only Λ, resting on the biased-ground-state subtraction. The O(δ³) current is subdominant and does not change this.

## Scope held

No verdict moved (CONJ-COSMO-1 NOT-confirmed; chirality V3/W3 untouched). No THEO, no ID. No chirality-lane or shared-registry edits. This is the DM-side residual read; it consumes the Mechanism-A NESS (read-only) and the F.1 lift scoping (0812–0813). The correction to the 0809/0810 emphasis is recorded explicitly. Conditional on Mechanism A and the H-NESS lift.
