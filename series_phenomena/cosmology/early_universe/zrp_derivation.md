# ZRP identification derived: leg 1's residual reduced to a leading-order PCD consequence

*Patch 0774, Session 154. The deepest hardening of leg 1, per the path the panel endorsed. LEMMA-NS-HTHEOREM
(0772) proved relaxation + the indistinguishable-Gibbs stationary state *given* the symmetric constant-rate
ZRP model, leaving the **ZRP identification** as the one residual premise. This finding derives that
identification from the CPP primitives, to leading order, and quantifies the only correction channel —
tying it to the already-bounded weak coupling. Script: `scripts/0774_zrp_derivation_corrections.py`.
Finding-level (LEMMA-NS-ZRP-DERIVE), NOT a hardened THEO — residuals remain (below).*

## The three ZRP properties, derived from the primitives

**(i) Independence (single-CP elementary moves).** The PCD cycle is, by definition, *"executed by each CP
at every Absolute Moment: perceive local SSV, compute response, displace to [a neighbouring] position"*
(`master_glossary.md`). It is a **per-CP** cycle — each CP perceives its *own* local SSV and displaces on
its own. There is no joint/multi-CP move primitive. The **only** inter-CP coupling is the shared SSV field
(a CP's local SSV depends on its neighbours). In the dilute/ideal limit this coupling → 0 and the moves are
independent; the coupling is the SSV interaction, quantified by Γ ~ α (already bounded, 0764–0768).

**(ii) Rate-homogeneity g(n) = n.** By **A1**, all CPs (of a given type/polarity) are identical — no per-CP
identity. By the **Absolute Moment**, every CP executes exactly one PCD cycle per tick, at the universal
clock rate 1/t_P. So every CP leaves its site at the *same* per-CP rate, independent of site or co-occupant
count → the total rate from a site of occupation n is n·(1/t_P) → **g(n) = n** (units 1/t_P = 1). A non-linear
g(n) requires the per-CP rate to depend on occupation, which can only enter through the SSV coupling (again
O(Γ) ~ O(α)).

**(iii) Symmetric neighbour kernel p(i,j) = p(j,i).** The 600-cell is **vertex-transitive** (every vertex
equivalent; coordination z = 12; symmetry group 2I), so the lattice supplies no preferred direction. With a
**homogeneous, isotropic inflationary background** (no SSV gradient), the compute step has no directional
bias → the CP displaces to each of its 12 neighbours with equal probability → p(i,j) = 1/12, symmetric. A
directional bias requires a background SSV gradient (a net force/field), absent in the homogeneous
inflationary background at leading order.

## The structural payoff

For a zero-range process, **independence + symmetry ⇒ the stationary measure is product form, for *any*
rate function g(n)** (standard ZRP result). Two consequences:
- **g(n) = n ⇒ the product marginal is Poisson** ⇒ the A1 indistinguishable Gibbs state with μ = kT·ln ρ ⇒
  **exactly p = 2 ⇒ n_s = 1 − 2/N_* = 0.9649** (verified: the ideal case gives dμ/d ln ρ = 1 to ~10⁻¹²).
- **Product form holds for any g(n)** ⇒ no inter-site correlations ⇒ **leg 2's mean-field cancellation
  (neutrality) is untouched** by any correction to g(n). The two legs don't interfere.

## The only correction channel, quantified

The SSV coupling makes the per-CP rate weakly occupation-dependent: g(n) → n·(1 + λ(n−1)) with **λ ~ Γ ~ α**.
This keeps the product form (still a ZRP) but deforms the marginal off Poisson, shifting the effective tilt
coefficient by η(λ) = dμ/d ln ρ − 1 ≈ (linear in λ). The induced shift in n_s is Δn_s = 2η/N_*:

| coupling λ | η = dμ/d ln ρ − 1 | Δn_s = 2η/N_* | vs Planck σ (0.0042) |
|---|---|---|---|
| 0 (ideal) | 0 (exact) | 0 | — |
| 0.1·α | 1.5×10⁻³ | 5×10⁻⁵ | 0.012σ |
| **α (physical)** | **1.4×10⁻²** | **5×10⁻⁴** | **0.12σ** |
| 3·α | 4.1×10⁻² | 1.5×10⁻³ | 0.34σ |
| 10·α | 1.2×10⁻¹ | 4.3×10⁻³ | 1.0σ |

At the physical coupling λ ~ α, the correction is a **theory uncertainty of ~5×10⁻⁴ in n_s — about 0.12σ of
the Planck error**, and it reaches Planck-error size only at ~10× the physical coupling. The central
prediction n_s = 0.9649 is unchanged at leading order; the correction is a sub-Planck theory error bar.

## What this upgrades

Leg 1's residual moves from **"assume the symmetric constant-rate ZRP model"** to **"the ZRP is the
leading-order PCD dynamics, forced by {A1, the per-CP PCD cycle, the vertex-transitive 600-cell, homogeneous
inflation}, with its only correction (the SSV coupling) bounded at the same α that the √n̄ thread already
controlled — a ~5×10⁻⁴ theory uncertainty in n_s, inside Planck."** Combined with LEMMA-NS-HTHEOREM (0772),
**leg 1 is now derived to leading order**: independence + symmetry + g(n)=n ⇒ product-Poisson stationary
state ⇒ relaxation (H-theorem) to the indistinguishable Gibbs state ⇒ p = 2 ⇒ n_s = 0.9649 ± ~0.0005(theory).

## Honest scope — the remaining residuals

- **Inflationary background homogeneity/isotropy** (used for the symmetric kernel, iii). This is a property
  of the n_s-setting epoch — reasonable (homogeneity is what inflation produces) but an *input about the
  epoch*, not derived here. A residual.
- **The correction's exact sign/magnitude** depends on the true SSV occupation-dependence; the toy
  g(n)=n(1+λ(n−1)) fixes only the *scale* (~α → ~5×10⁻⁴). So n_s = 0.9649 carries a leading-order theory
  uncertainty ~5×10⁻⁴, not an exact 4-decimal guarantee. (Still 8× inside the Planck error.)
- **The PCD "compute" step's full content.** The glossary defines compute as "respond per the primitive
  axioms"; the derivation reads this as a local, per-CP, SSV-driven displacement with no added multi-CP
  structure beyond SSV. Faithful to the glossary, but the axioms' compute rules are not exhaustively
  spelled out, so this is an interpretive (though minimal) reading.
- Because of these, **n_s remains conditional/grounded** — this patch does not by itself promote it to
  Section 1 / a counted swarm contribution. What changed: leg 1's conditionality is now a *leading-order
  derivation with a quantified sub-Planck correction*, plus inflationary homogeneity — a far cry from "assume
  the bath clause." Whether this clears the bar to call leg 1 "derived" (and promote n_s) is a panel
  judgement.

## Panel consensus (Patch 0775)

All three reviewers endorse leg 1 as **derived to leading order** (the panel's shorthand for LEMMA-NS-ZRP-DERIVE is "LEMMA-NS-ZRP"):

- **ChatGPT — CONFIRM-WITH-CALIBRATION.** All three property-derivations hold at leading order (symmetry the
  weakest, honestly listed as an input). The 5×10⁻⁴ correction handling is right *in scale*, to be kept as a
  **model-dependent provisional estimate, not a theorem**. Clears the bar to call leg 1 "derived to leading
  order from the minimal PCD/ZBW-as-ZRP identification + inflationary homogeneity" — but **not** "derived
  from A1–A11" (the PCD-compute → symmetric-constant-rate-ZRP mapping is still a minimal-model reduction).
  Endorsed registration language: *"LEMMA-NS-ZRP identifies the leading-order ZBW occupation dynamics with a
  symmetric constant-rate zero-range process. Given A1, per-CP PCD updates, vertex-transitive 600-cell
  geometry, and inflationary homogeneity, the stationary measure is product-Poisson and the tilt log
  follows. SSV corrections enter at O(α), giving an estimated Δn_s ~ 5×10⁻⁴. Thus leg 1 is derived to
  leading order, with residual uncertainty in the exact SSV correction and the homogeneity assumption."*
- **Grok — endorse.** All three derivations hold with no hidden assumptions; correction correctly treated as
  bounded theory uncertainty (not a free parameter); leg 1 derived to leading order, meeting the
  conditional/grounded zero-new-axiom standard for registration.
- **Copilot — endorse.** Leg 2 correctly grounded (DP-Sea, not bespoke; √n̄ de-risked and confined); the
  PCD→ZRP reduction is a real derivation, not a modelling whim; leg 1 derived to leading order. Suggested
  status tag: *"Derived to leading order from A1+PCD+600-cell+DP Sea, conditional on homogeneous inflation
  and sub-Planck SSV corrections."*

**Consensus status (adopted into PRED-O-33):** n_s = 0.9649 ± ~0.0005(theory), α_s ≈ −2/N_*² ≈ −0.0006 — a
conditional/grounded zero-new-axiom prediction with **leg 1 derived to leading order** (PCD/ZBW-as-ZRP +
inflationary homogeneity) and **leg 2 grounded** (DP-Sea neutrality). Remaining residuals (panel-agreed):
(i) the PCD-compute → ZRP reduction is a minimal-model step (not yet A1–A11); (ii) inflationary
homogeneity/isotropy is an epoch input; (iii) the exact O(α) SSV-correction coefficient is model-dependent.
The 5×10⁻⁴ is a provisional model-error estimate, not a final uncertainty.

## Pointers

- Builds on: 0772 (H-theorem given the ZRP); the PCD definition + 600-cell (z=12, 2I) + A1 (`master_glossary.md`);
  0764–0768 (the √n̄/Γ thread that bounds the SSV coupling at ~α).
- Numerics: `scripts/0774_zrp_derivation_corrections.py` (grand-canonical perturbed ZRP → Δn_s scaling).
- Reasoning: `reasoning/0774_zrp_derivation.md`.
