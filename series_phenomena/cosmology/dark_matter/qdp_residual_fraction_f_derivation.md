# Deriving the residual fraction f — mechanism settled, value bounded, the missing ingredient pinpointed

**Patch:** 0834 (Session 156, 10 June 2026) · **Type:** partial derivation (real progress; not a full pin). · **Lane:** DM-2 / `dark_matter/`.
**Addresses:** the one Era-2 input 0833 left open — the residual color depth fraction f = (residual well depth)/E_qDP. **Verify:** `code/0834_residual_fraction_f_derivation.py`.

---

## The mechanism is now settled (grounded in SS-1)

The residual force between two qDPs is **not** a long-range color field. SS-1's color mechanism is decisive here: color charge is vertex occupancy, and *only a single quark* (one base vertex occupied) generates a long-range, energetically-unbounded qDP-chain color field; a symmetric, color-balanced object has its color contributions cancel exactly and carries **no long-range color field**. A qDP is a color-**singlet** +qCP/−qCP pair (meson-like), so it has no long-range color field. Its residual to another qDP is therefore the color analog of the **nuclear force between color-singlets**: a **light-DP-exchange Yukawa** (the lightest exchangeable DP sets the range, `λ ≈ ℏc/E_hDP ≈ 1.3 fm` — exactly the range used in the 0831/0832 potential), with a **London dispersion** floor underneath it. This retroactively justifies the hard-core-plus-attractive-Yukawa form assumed in 0831/0832.

## The value is bounded, and it splits on one question

f is the depth of that residual at contact, over E_qDP. Modeling the qDP as a charged oscillator (excitation `ℏω = E_qDP = 264 MeV`, internal reduced mass `μ = m_qDP/4 ≈ 66 MeV`), the polarizability is `α_pol = g_c²/(μω²)` and the London depth is `ε = (¾ E_qDP α_pol²)/a⁶` at contact `a`. The result hinges entirely on **which color coupling** enters `g_c² = α_c ℏc`:

| coupling scenario | α_c | α_pol [fm³] | f (a=1.0–1.3 fm) |
|---|---|---|---|
| weak — DP-binding (3α) | 0.022 | 0.04 | 2×10⁻⁴ – 1×10⁻³ |
| strong — confinement (α_s ≈ 0.3) | 0.30 | 0.50 | 0.04 – 0.19 |
| strong — confinement (α_s ≈ 0.6) | 0.60 | 1.0 | 0.16 – 0.75 |

Geometric cross-check `(λ_qDP/a)⁶`: 0.036–0.174 for a = 1.3–1.0 fm — matching the strong-coupling (α_s ≈ 0.3) row, confirming the polarizability scale ≈ the qDP Compton volume in that case.

So **f is bounded ≈ 10⁻⁴ (weak/dispersion) to ≈ 0.15 (strong/contact), all < 1** (the residue-weaker-than-source structural ceiling). The ~10³ spread is not vagueness — it is *exactly* Step-1's flagged σ/m-risk range, and it traces to one well-posed question: **which color coupling mediates the neutral qDP–qDP residual — the 3α DP-binding coupling, or the α_s confinement-scale coupling?** That is the qDP → light-DP **exchange vertex**, the single ingredient the corpus does not yet assemble (it supplies both couplings, the DP spectrum, and the SS-1 color-neutrality mechanism, but not the neutral-qDP coupling). Pinning f is now a sharply-defined calculation, not an open-ended one.

## Why the arc doesn't wait on it

The Era-2 conclusions are robust across the *entire* bounded range:
- **Collisionless** holds for all f ≤ 1 (0831: the resonance/SIDM-crossing sit above E_qDP, unreachable by a residue). A smaller f only deepens the margin.
- **Diffuse** holds for all f by the de Boer parameter (0833: Λ ≈ 0.75–2.4 ≫ He-4's 0.18 across the whole f range — too quantum to self-bind).
- **Glueball-avoidance** is f-independent (hard core + quantum pressure, 0830/0832).

In fact the *weak-coupling* end (f ~ 10⁻⁴) makes every conclusion stronger. So pinning f via the exchange vertex sharpens the number; it does not change any Era-2 verdict.

## Net and scope

The residual mechanism is derived (light-DP-exchange Yukawa between color-singlets, SS-1-grounded), f is bounded [10⁻⁴, ~0.15] < 1 and computed in both coupling scenarios, the geometric cross-check is consistent, and the lone remaining ingredient is identified: the qDP → light-DP coupling vertex (which of the two couplings, with its dipole suppression). **No closure, no THEO/ID, no verdict** — a partial derivation. Oscillator/London model with representative `μ = m_qDP/4`, contact `a = 1.0–1.3 fm`; the meson-exchange Yukawa would add to the dispersion floor (needs the vertex). Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.
