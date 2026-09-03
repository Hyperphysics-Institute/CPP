# OPEN-GR-CENSUS-P answered: p = 0 — the ratified census does not self-enhance. The second-order term the bare theory needs is SR-1's own OPEN constitutive coefficient, and Mercury fixes it to ½: no new axiom, one number the theory left unspecified

**Patch 3389, Session 161, 2 Sep 2026.** Verify `code/3389_census_p_and_sr1_beta_verify.py` (15/15). Reasoning `reasoning/3389.md`. Withdraws 3388 §2's mechanism; sustains C-NO-SPECIAL-RULE in full.

## §1 p = 0, and why 3388 was wrong

The ratified census (T-1 §2–3) is a **shell mean**: `u(x) = mean of u over the sphere of radius PSR_eff(x)`. The mean-value property holds for every radius, so `u` is harmonic for *any* PSR profile and `u = v = μ/r̄` exactly (verified here with position-dependent radii, 2 × 10⁻⁷). **The census has no second-order self-enhancement: p = 0.**

3388 claimed the hop length enhances the deposit count ("deposits ∝ 1/PSR"). That assumed a conserved flux from a fixed source. The relay re-emits a fixed N₀ at *every* GP, so the per-GP arrival count is N₀ everywhere in steady state; the only correction is second order in the *gradient* of the hop length (`1 + h′² + …`, continuum identity; smooth-lattice check 10⁻³), which for a macroscopic field is `~(l_P/r)²v²` — Planck-suppressed. 3388's mechanism is withdrawn. The founder's constraint stands with no exception.

## §2 Where the freedom actually is — and it is not new

SR-1 (App. D.4/E) states its PSR constitutive law as a series, `s(ε) = 1 − ε + β ε² + γ ε³ + …`, and says the linear form `PSR = l_P/(1 + ε)` is "**exact to first order**." The Padé `1/(1+ε)` (β = 1, γ = −1) is "the unique lowest-order rational form satisfying both constraints" — a *working choice*, not a derivation. **The second-order coefficient of the PSR law is open in the bare theory.**

With the founder's clock mechanism `N = PSR/l_P` (R-CLOCK-RATE-IS-DISPLACEMENT) and the census `u = v` (p = 0), the PPN parameter is

    β_PPN = ½ + β_SR1.

| β_SR1 | PSR law | β_PPN | Mercury |
|---|---|---|---|
| 1 (Padé, the corpus's working form) | `1/(1+v)` | 3/2 | 35.8″ — fails |
| **½** | **`(1 − v/2)/(1 + v/2)`** | **1** | **42.98″ — passes** |

And `(1 − v/2)/(1 + v/2)` is **exactly the ratified log-lapse.** So: Mercury fixes an open constitutive coefficient of the bare theory to ½; with it, the founder's clock mechanism *reproduces GR's time dilation identically* — the log-lapse the T-1 charter imposed by dictionary is now `PSR/l_P` itself. No axiom added; no special rule; one unspecified number pinned by the oldest test of GR. The third-order coefficient γ (−¼ if the whole log form holds) is left for a strong-field test.

## §3 The founder's disappointment, answered

"Mercury is not computed from the original bare theory" — it is, once the bare theory's own open coefficient is set. The theory was not changed; it was *completed* at an order it had explicitly left open. The 1/(1+ε) form was always labelled first-order-exact.

## §4 What follows (as 3387 D, now with its mechanism located; NOT enacted)

- `PSR = l_P N`; lattice hop per Moment `N/ψ²` = GR's coordinate light speed; **J = 6.75 at any wall; the strong-field departure of 3385/3386 closes.**
- The PSR floor `l_P/2` is reached at `N = ½`, `v = 2/3`: **areal 8μ/3 = 1.33 r_S** (not Buchdahl's 1.125), `z = 1`, cavity **0.70 ms**.
- 3378's `β_ℓ`, 3383's and 3384's poles were at `r_w = 9/4` and must be redone at `8/3` (where `β_ℓ` has flipped sign).
- SR-1 owes a corrigendum: β_SR1 = ½ fixed by Mercury (SR lane; ledger row B1 grows).

## §5 To the founder
Two things are yours. (i) **Ratify** β_SR1 = ½ as the completion of the PSR law's second order (it is your law; Mercury is the argument). (ii) The **saturation surface moves** to 1.33 r_S as a consequence — the R-core arc's surface was placed by the Padé form's floor; under the log form the same floor `l_P/2` sits further out. Do you see anything in the substrate that prefers the Padé form's second order over the log form's? If not, (ii) follows from (i).
