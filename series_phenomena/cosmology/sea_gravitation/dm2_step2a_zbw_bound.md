# DM-2 — Step 2(a): The ZBW-Scale Bound on k·Δ|SSV| — Is D2 OP1-Gated?

**Patch:** 0806 (Session 156, 8 June 2026) · **Work item:** DM-2 / OPEN-SR-5d (D2) / net-broadcast lemma condition (a)
**Predecessor:** Step-1 separability (Patch 0805), which made this the load-bearing kill-risk.
**Verify:** `scripts/0806_zbw_bound_gradient_control.py` (bound + gradient-control + bounded-factor checks).

---

## The kill-risk this resolves

Step 1 found D2 (ground-state exclusion) separable from c08 Open Problem 1 (the unproven strong-field nonlinear Einstein closure), **conditional on the net-broadcast lemma**, whose load-bearing half is condition (a): the weak-field truncation `k·Δ|SSV| ≪ 1` must hold at the ZBW scale. If instead `k·Δ|SSV| ~ O(1)` there, `⟨𝓕⟩` would need the full nonlinear term — OP1 — and separability would fail. This is that check.

## The bound (established c08 facts only)

c08 fixes `k·Δ|SSV| = GM/rc²` exactly (the shell-broadcast source), and the CP Exclusion Rule bounds `k·Δ|SSV| ∈ [0,1]` (saturating at 1 at the Planck core, `PSR_eff = l_P/2`). For a ZBW oscillation at the Compton radius `r = ħ/mc` of a constituent of mass `m`:

    k·Δ|SSV|_ZBW = G m / (r c²) = G m² / (ħ c) = (m / m_P)².

Numerically (verify CHECK 1):

| constituent | m | k·Δ|SSV| = (m/m_P)² | regime |
|---|---|---|---|
| electron | 0.511 MeV | 1.8×10⁻⁴⁵ | weak |
| proton | 0.938 GeV | 5.9×10⁻³⁹ | weak |
| GeV DM constituent | 1 GeV | 6.7×10⁻³⁹ | weak |
| 100 GeV | 100 GeV | 6.7×10⁻³⁵ | weak |
| Planck mass | 1.22×10¹⁹ GeV | 1.0 | O(1) ceiling |

So **every sub-Planck constituent — all matter and all DM candidates — is weak-field by ≥ 35 orders of magnitude.** The only thing that reaches `k·Δ|SSV| ~ O(1)` is the Planck-scale Sea ground state itself.

## The resolution: gravitation is gradient-controlled, not amplitude-controlled

The naive worry is that the Planck-scale ground state's `O(1)` amplitude drags us into OP1. It does not, and the reason is structural. The nonlinear term factorizes as

    𝓕 = [2k u² / (1+ku)²] · box(ln(1+ku)),   u := Δ|SSV|,

a **bounded amplitude factor** times a **gradient factor**. Expanding around an `O(1)` background `u₀` with a slow fluctuation `a·sin(qx)` (verify CHECK 2):

    𝓕_lin = −2k² q² u₀² sin(qx) / (1 + k u₀)³.

The source carries `q²` — the **gradient squared**. The `O(1)` background `u₀` enters *only* through the factor `2(ku₀)²/(1+ku₀)³`, which is **bounded** on `ku₀ ∈ [0,1]`, with maximum `1/4` at the ceiling `ku₀ = 1` (verify CHECK 3). It never blows up; it multiplies the gradient rather than amplifying on its own.

Physically this is just the statement that curvature depends on the *variation* of the metric (`∂²g`), not on the *value* of `|SSV|_abs`. A uniform Sea — however large its absolute SSV — has near-zero gradient, so it sources near-zero gravitation, and the strong-**amplitude** nonlinearity that OP1 is about is never exercised.

## Verdict: condition (a) PASSES — separability is ROBUST, D2 is not OP1-gated

- **Uniform Sea ground state:** `O(1)` amplitude but vanishing gradient → sources ~0 via the bounded gradient-controlled `𝓕` (and, redundantly, via the amplitude-independent geometry route: constant `g_tt` → flat). OP1 never enters.
- **The only large-gradient sources** are sub-Planck localized excesses (matter, DM swirls), which are weak-field by `(m/m_P)² ~ 10⁻³⁹`. There the weak-field truncation and the Step-1 parity argument hold by a 35–45 order margin.

So the earlier honest kill-risk — "if k·Δ|SSV| ~ O(1) at the ZBW scale, D2 is back on c08's hardest problem" — is **retired**: the `O(1)` value occurs only for the uniform ground state, exactly where gradient-control makes it harmless. **DM-2's D2 does not bottom out on c08 OP1.**

## Residual (narrow, NOT OP1) → handed to 0807

One condition of the net-broadcast lemma remains: condition (b), whether the discrete Planck-scale zero-point carries a *net parity-broken gradient* that survives coarse-graining. That is pursued as the residual↔Λ identification in Patch 0807. It is a local symmetry question, not the strong-field closure.

## Scope held

No verdict moved (CONJ-COSMO-1 stays NOT-confirmed). No THEO minted. No shared-registry edits — the SR.md OPEN-SR-5d note (OP1 → condition (b) only; condition (a) closed) is deferred to a batched registry patch per the freeze (chirality window active at 0902). The c08 OP1 dependency status is recorded in `todolist.md` (Patch 0808) as a standing c08 target, explicitly **not blocking DM-2**.
