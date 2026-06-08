# DM-2 — Step 1: Separability of D2 (Ground-State Exclusion) from c08 Open Problem 1

**Patch:** 0805 (Session 156, 8 June 2026) · **Work item:** DM-2 / OPEN-SR-5d (D2) · **Type:** separability kill-test (analytic + symbolic)
**Predecessor:** Step-0 audit (Patch 0802).
**Verify:** `scripts/0805_separability_check.py` (4 structural checks, all PASS).

---

## The question

The Step-0 audit found that D2 (ground-state exclusion — the uniform Sea does not gravitate cosmologically) is currently tied, in both the SR.md entry and the DM-2 handover, to c08's **central open problem (OP1)**: whether the full nonlinear 𝓕 term reproduces the exact Einstein G_μν in the strong-field regime. Step 1 tests whether that coupling is real or spurious:

> **Can D2 be established from c08's *established* results alone — the excess-sourcing field-equation form, the exact Schwarzschild theorem, and the proved weak-field reduction — without invoking OP1?**

If yes, the c08 dependency de-risks to the weak-field regime (already proved) and the gate's risk concentrates on the IR/horizon piece (5b coefficient + D3). If no — if ground-state exclusion genuinely needs the strong-field closure — that is the wall signal.

## The c08 source structure (established, not OP1)

The field equation is `box(u) + 𝓕[u] = (8πG/c⁴)T`, with `u := Δ|SSV|` the excess and

    𝓕[u] = [2k u² / (1+ku)²] · box(ln(1+ku)).

Two established-results routes show the **mean uniform Sea** is non-gravitating:

- **Source route.** For any spatially/temporally uniform `u` (including the ground state `u=0`), the factor `box(ln(1+ku)) = 0` (d'Alembertian of a constant), so `𝓕 = 0` *exactly* — and the linear term `box(u) = 0` likewise. The uniform Sea sources nothing. (Verify CHECK 1.)
- **Geometry route.** A uniform `|SSV|_abs` maps to a *constant* `g_tt` (the c07 mapping); a constant metric has identically zero Christoffel symbols → zero Riemann → `G_μν = 0`. Flat, hence non-gravitating, independent of the field equation entirely. (Verify CHECK 4.)

Both routes sit at the maximally-weak-field point. **Neither invokes OP1** (a strong-field statement). So for the *mean* uniform Sea, D2 is separable from OP1 outright.

## The fluctuation channel (where the CC catastrophe lives) — and why it is suppressed

The standard cosmological-constant catastrophe enters through vacuum *fluctuations*: even if `⟨u⟩` is uniform, the zero-point ZBW oscillation makes `u = u₀ + δ(x)` with `⟨δ⟩ = 0`, and in ordinary semiclassical gravity `⟨T_μν[δ]⟩ ≠ 0` gravitates. We test whether the CPP field-equation structure suppresses this.

Symbolic expansion (CHECK 2) shows 𝓕 is **cubic-leading** in the fluctuation amplitude:

    𝓕 = 2k² δ² δ'' + O(δ⁴),

because the prefactor is O(δ²) and the `box(ln(1+kδ))` factor is O(δ). Its value, first, **and** second derivatives at `δ=0` all vanish. Consequently (CHECK 3), for a zero-mean fluctuation:

- the **linear term** `⟨box(δ)⟩ = box⟨δ⟩ = 0` exactly;
- the **nonlinear term** `⟨𝓕⟩` vanishes at leading (cubic) order **by parity** for any statistically *symmetric* `δ` (the cubic integrand `2k²δ²δ''` is odd-leading; explicit period-average for `δ = sin x` gives 0);
- a **parity-breaking / skewed** `δ` (e.g. `sin x + ½cos 2x`) gives `⟨𝓕⟩ = 3k²/2 ≠ 0` — a real residual source.

So the field-equation structure dodges the catastrophe *automatically*: a symmetric zero-mean Sea fluctuation sources **zero** mean gravity at leading order, with no tuning and no OP1. This is a genuine CPP-specific advantage over continuum QFT, where no such structural cancellation exists.

## Verdict: CONDITIONAL PASS — separability holds, gated on the net-broadcast lemma (not OP1)

D2's ground-state exclusion **is separable from c08 Open Problem 1.** What remains is **not** the strong-field nonlinear Einstein closure but a single, local, sharper condition — the **net-broadcast lemma**:

> The Sea's zero-point ZBW fluctuation sources zero mean gravitation, provided (a) it is in the weak-field regime `k·Δ|SSV| ≪ 1` at the ZBW scale, and (b) it is statistically symmetric (bounded skew / non-Gaussianity), so the parity cancellation above holds.

This reframes the whole c08 dependency. "D2 rests on c08's central conjecture (OP1)" becomes "D2 rests on the symmetry and weak-field character of the ZBW zero-point" — a much cheaper Step-2 target.

## Honest kill-risk (falsification-first)

The net-broadcast lemma is **not** free, and condition (a) carries a genuine kill-risk:

- **Weak-field validity at the ZBW scale (the real danger).** The ZBW is a Planck/Compton-scale oscillation; whether `k·Δ|SSV| ≪ 1` *there* is not obvious. If `k·Δ|SSV| ~ O(1)` at the ZBW scale, the weak-field truncation fails, `⟨𝓕⟩` must be evaluated with the full nonlinear term — and that **is** OP1 territory. In that case D2 is *not* separable and the gate is back on c08's hardest problem. **This is the load-bearing check for Step 2.**
- **ZBW symmetry.** If the Perceive–Compute–Displace cycle is not time-symmetric (a directional bias in the displace step), `δ` is skewed and the residual `⟨𝓕⟩ ≠ 0` channel opens. Plausibly bounded, but must be shown, not assumed.

## Conjecture flagged for Step 2 (not claimed here)

The *surviving* residual source is exactly the parity-breaking part of the Sea fluctuation — i.e. the component that cannot be made symmetric/uniform. It is tempting to identify this residual with the horizon-scale non-cancellable mode that Step C (5b) already isolates as Λ (the largest gradient the finite causal Sea cannot null). If that identification holds, the *same* structure that excludes the bulk ground state would deliver exactly one residual = Λ. This is a **conjecture for Step 2**, recorded so it is not mistaken for an established result.

## Next move

Step 2 = establish (or kill) the net-broadcast lemma: bound `k·Δ|SSV|` at the ZBW scale (condition a — the kill-risk), and establish the ZBW zero-point symmetry (condition b). A clean result either de-risks the c08 dependency to the weak-field regime (separability confirmed) or shows D2 is OP1-gated (wall).

## Scope held

No verdict moved (CONJ-COSMO-1 stays NOT-confirmed). No THEO minted; the net-broadcast lemma is a *named target*, not a registered result. No shared-registry edits — the SR.md OPEN-SR-5d note (narrowed c08 dependency: OP1 → net-broadcast lemma) is **deferred** to a batched registry patch, per the registry freeze (chirality window active at 0902).
