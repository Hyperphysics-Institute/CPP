# f as a number — the coupling vertex resolved to α_s, f ≈ 0.2, residual depth ≈ 50–130 MeV

**Patch:** 0835 (Session 156, 10 June 2026) · **Type:** derivation (f to a factor of ~3; the coupling question resolved). · **Lane:** DM-2 / `dark_matter/`.
**Closes 0834's open ingredient:** which color coupling mediates the neutral qDP–qDP residual (the qDP → light-DP exchange vertex). **Verify:** `code/0835_f_as_a_number.py`.

---

## The vertex resolves: it is α_s, via the color polarizability

0834 left f's value split across a ~10³ range because two corpus couplings could in principle enter — the weak DP-binding 3α (≈0.022) and the strong confinement α_s (≈0.3–1). The resolution is a physical observation, not a new assumption: **a color-singlet qDP has no net color charge (no long-range color field, per SS-1) but a nonzero color *polarizability*** — it is distorted by color-field *gradients*, the two qCPs responding oppositely. So the residual has two van der Waals channels, electric (coupling 3α) and color (coupling α_s), and the color channel dominates by

  f_color / f_electric = (α_s / 3α)² ≈ (0.5/0.022)² ≈ 500×.

The residual is therefore the **color van der Waals**, governed by α_s — and the dipole suppression that worried 0834 is carried automatically by the polarizability `α_pol = α_c ℏc/(μω²)` (Compton-scale, not the tiny internal r_min). The coupling question is settled: α_s, not 3α.

## The number

With `α_pol(color) = α_s ℏc/(μω²)` (μ = m_qDP/4 ≈ 66 MeV, ℏω = E_qDP = 264 MeV) and the London depth `ε = (¾ E_qDP α_pol²)/a⁶` at contact a:

| α_s | a [fm] | f | V₀ = f·E_qDP [MeV] |
|---|---|---|---|
| 0.3 | 1.00 | 0.19 | 50 |
| 0.5 | 1.15 | **0.23** | **60** |
| 0.5 | 1.30 | 0.11 | 29 |
| 1.0 | 1.15 | 0.90 | 239 |

**Central estimate: f ≈ 0.2, a factor-of-~3 range (≈0.07–0.6).** Crucially, the spread is now *physical* — α_s at the qDP scale (~264 MeV is below Λ_QCD ≈ 1 GeV, so α_s is nonperturbative, O(0.5–1)) and the contact distance a (the eDP-coat hard core, ~1.0–1.3 fm, entering steeply as 1/a⁶) — not the structural coupling ambiguity that spanned 10³ in 0834. f ≈ 0.2 lands squarely in the original "realistic ~0.1" estimate, now derived rather than analogized.

## The residual potential is now quoted, not parametrized

f ≈ 0.2 fixes the residual Yukawa depth used as a free parameter in 0831/0832:

  **V₀ = f · E_qDP ≈ 53 MeV** (range ~50–130), range λ ≈ ℏc/E_hDP ≈ 1.3 fm, hard core ~1.0–1.3 fm.

So the 0831/0832 potential is no longer a scan over f — it is a specific ~50 MeV-deep, 1.3 fm-range color van der Waals well behind a ~1 fm hard core.

## Arc consistency — confirmed at the derived value

Every Era-2 conclusion holds at f ≈ 0.2 and across the whole physical range f < 1:
- **Collisionless:** at f = 0.2, 0831 gives a = 0.71 fm, σ/m = 0.12 cm²/g — safely below SIDM; even the worst case f = 1 gave 0.50.
- **Diffuse:** the de Boer parameter is Λ = 0.747/√f, so Λ(f=0.2) ≈ 1.7 and Λ > 0.75 for *all* f < 1 — always far above He-4's 0.18, too quantum to self-bind.
- **Glueball-avoidance:** f-independent (hard core + quantum pressure).

So the derived f confirms the arc rather than straining it.

## One honest caveat

The color van der Waals is the *computable, dominant* channel. If the lightest hybrid (hDP) plays a pion-like Goldstone role, a coherent one-hDP exchange could *add* to it — as one-pion-exchange dominates two-gluon exchange in the nuclear force. That would raise f toward (but not past) the f < 1 ceiling. It is a possible enhancement of a known mechanism, not a new free parameter, and the arc absorbs it (collisionless and diffuse hold for all f < 1). Establishing whether the hDP is a Goldstone is the only thing that could move f above the ~0.2 color-vdW estimate.

## Scope

Derivation of f to a factor of ~3, with the coupling vertex resolved (color van der Waals, α_s). **No closure, no THEO/ID, no verdict.** Oscillator/London model at contact a ≈ 1.0–1.3 fm — at the edge of the multipole expansion (a comparable to the qDP size), so the factor-~3 honesty is real; α_s at the qDP scale is nonperturbative. Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.
