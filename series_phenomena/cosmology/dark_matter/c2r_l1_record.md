# C2R-L1 RECORD — the leading-order derivation CLOSES: from the every-Moment response rule and the 2767 occupied-core ruling, the homogenized screening equation (−∇² + κ²)ψ = 4πQδ follows with **κ² = 4πnα**, making the continuum matching the UNIQUE occupied-core closure rather than a prescription — **D1 = 0 exactly** (α_derived = κ²/(4πn) = 0.08193374 fm = a/(π√2) to machine identity at the operating point) — and the discreteness accounting reconciles the L4 record's 59%/22% decomposition to the digit: the site matching's "self-exclusion" is, verbatim, the responding core medium it wrongly dropped (59.40% of S_cont; the shell-discreteness excess is +21.5% of S_cont, +52.9% of the outer continuum — same accounting, different denominator)

**Patch 2770, 22 July 2026. Prereg: `c2r_l1_prereg.md` (2769, frozen
before execution; route followed with no amendment). Verify:
`code/2770_c2r_l1_closure.py` (deterministic, no seeds; every number
below is script output). Reasoning: `reasoning/2770.md`. Fences
F1–F3 in force; 79.5% not in scope.**

## §1 — Derivation (route steps 1–3, executed)

Per-site linear response q_i = −αψ(r_i) from the every-Moment rule
(2767 §3: weak static bias → time-averaged statistical rearrangement
= χ_static); self-consistency ψ(r) = ψ_ext − Σ_j αψ(r_j)/|r−r_j|;
homogenization licensed EVERYWHERE — including r < a — by the
occupancy ruling (no exclusion exists in the update rule), giving
∇²ψ = ∇²ψ_ext + 4πnαψ, i.e. the screened equation with
**κ² = 4πnα**. Inverted at fixed (κ, n): α = κ²/(4πn) is the unique
closure. At the operating point (a = 0.3640220194 fm, κ = 2/a =
5.494173 fm⁻¹, n_FCC = √2/a³ = 29.317844 fm⁻³):

- α_derived = κ²/(4πn) = **0.08193374 fm**
- α_imposed = a/(π√2) = **0.08193374 fm**
- **D1 = 0.000** (charter threshold 5%; the identity is exact, not
  approximate — κ²/(4πn) = (4/a²)·a³/(4π√2) = a/(π√2) algebraically)

The 2671 matching is thereby DERIVED: its content was never a free
normalization but the Debye-form self-consistency of an occupied
responding medium. The dependency chain is the result: **occupancy
(2767) → homogenized closure → α.** Had the core been excluded, the
homogenization integral would lose the r < a region and the closure
would fail near sites — which is exactly the L2 question (the actual
χ(r) profile vs uniform), not a leading-order ambiguity.

## §2 — Discreteness accounting (route step 4, executed; sets up L2)

- S_cont = 1/α = **12.2050 fm⁻¹**; S_disc = Σ_{j≠0} e^{−κr_j}/r_j =
  **7.5761 fm⁻¹** (direct FCC generation, cutoff 12a, convergence
  6×10⁻⁸) — reproducing the L4 record's committed value to the
  digit; ratio S_cont/S_disc = **1.6110** (L4: 1.611).
- Decomposition: the r < a core-medium contribution is S_cont ×
  (1 − 3e⁻²) = 12.2050 × **0.5940** = **7.2497 fm⁻¹** — the L4
  record's "59% self-exclusion," now reinterpreted under the 2767
  ruling as the RESPONDING MEDIUM the site sum omits. The outer
  continuum (r > a) carries 4.9553 fm⁻¹; the discrete shells sum to
  7.5761 fm⁻¹ — an excess of **+21.5% of S_cont** (the L4 record's
  "+22% shell discreteness"; equivalently +52.9% of the outer
  continuum — the two published fractions are the same accounting
  under different denominators, and −59.40% + 21.47% = −37.9% ⇒
  S_disc/S_cont = 0.6207 = 1/1.6110, closing the ledger exactly).
- Status restatement (binding for consumers): the α′ site matching's
  entire 1.611 factor decomposes into (i) dropping medium the
  ontology says responds (the dominant term) and (ii) replacing the
  smooth outer medium by discrete shells (the smaller, sign-opposite
  term). Item (i) is premise-rejected (2767); item (ii) is the
  physically real discreteness/superposition structure whose net
  effect on ℓ is precisely what **C2R-L2's χ(r) computation** must
  deliver as δℓ/ℓ_LO.

## §3 — Decision quantities and class status

**D1 = 0** (≤ 5%: first C2R-CONFIRM condition MET). **D2: ℓ_LO =
0.0904 ± 0.0028 fm** — the committed robustness envelope at the
derived α; no re-run owed at D1 = 0 (same α, same frozen operator,
same envelope). Honesty bound as committed: κ·a = 2 itself and the
per-site stiffness behind it remain underived — named
KINETIC-1-adjacent, NOT an obstruction (the chartered L1 objective,
the α↔κ closure, closes). The campaign class fires only at L4, after
L2 reports δℓ/ℓ_LO against W = 3.1%.
