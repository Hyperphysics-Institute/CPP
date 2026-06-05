# Specification: what a CPP "stack ensemble" would have to be (to derive n_s = 0.9649)

*Patch 0750, Session 154. A constructive specification — NOT a derivation. It states precisely what
structure CPP would have to own for a stack of n CPs on a GP to carry a concentration chemical potential
μ ∝ ln(n/V), which (0749) is the only thing that yields H_eff ∝ ln n → n_s = 1 − 2/N_* = 0.9649,
coefficient-free. Each required ingredient is given in CPP terms and assessed honestly for plausibility.
NO THEO. The point is to make the commitment explicit and checkable so the swarm can decide whether CPP
can own it.*

## 0. What it would buy, and the one robust fact

If a stack of n identical CPs on a GP has a concentration chemical potential μ(n) ∝ ln n, and the
H-engine boost couples to it (H_eff ∝ μ), then:

  H_eff ∝ ln n̄,  n̄(N) = n̄_init·e^{−3N},  ln n̄ = 3·N_rem  ⇒  n_s − 1 = 2·d ln H_eff/dN = −2/N_rem.

At the pivot N_rem ≈ 57 this is **n_s = 0.9649**. The single robust fact worth holding onto: **the tilt
p = 2 is independent of every coefficient and additive offset** in μ = a + b·ln n (for large n the b·ln n
term dominates d ln H/dN). So we do NOT have to derive a temperature, a volume, or a normalization — only
that the n-dependence is logarithmic and roughly stationary over the observable window. That is what
makes this worth specifying: most of the usual thermodynamic detail is irrelevant to the prediction.

## 1. The particles — identical, indistinguishable CPs

The "gas" is the n CPs of a single species stacked on one GP. They must be **indistinguishable**
(identical CPs of the same type). This is the crux from 0749: the ln n is the Gibbs/indistinguishability
result; if the CPs were made distinguishable (e.g. by permanent per-CP phase labels), the count would be
Ω = qⁿ, the entropy extensive, the chemical potential constant, and the spectrum the excluded n_s = 1
cliff. **Requirement:** same-species CPs in a stack carry no permanent distinguishing label.
**Assessment:** plausible — CPs of one species are identical in CPP by construction. The danger is only
if ZBW phase is treated as a permanent label (it must not be; see §4).

## 2. The volume — the fixed GP cell

The concentration is n/V. The relevant V is the **fixed lattice cell of one GP** (the equilibrium home
of one CP), so the concentration relative to the equilibrium n* = 1 CP/GP is just the occupation number
n. Then μ ∝ ln(n/V) = ln n + const. **Requirement:** V is the (fixed) GP cell, not the PSR_base reach
volume. (Using the reach volume would make V grow during inflation and tangle the chemical potential
with the very PSR_base we are computing — circular. The over-occupation is "n CPs where 1 belongs," a
per-GP count, so V = the GP cell is the correct and non-circular choice.) **Assessment:** natural — GPs
are fixed and eternal (Brick #2); V = const is exactly what gives the clean ln n. Its numerical value
only sets the additive offset, which does not affect the tilt.

## 3. The temperature — a ZBW jitter scale, and why its value does not matter

A chemical potential needs a temperature: μ = a + kT·ln n. The natural CPP candidate for T is the
**ZBW (zitterbewegung) jitter energy scale** — the characteristic energy of the sub-Moment oscillation
the CPs already undergo. **Requirement:** T is set by the ZBW scale and is **approximately constant over
the observable window** (the ~7–8 e-folds of observable scales). **Assessment:** the *value* of T is
irrelevant to the tilt (it is the coefficient b = kT, which drops out of d ln H/dN). What matters is only
that T does not vary *fast* across the window — if d ln T/dN were comparable to 1/N_rem ≈ 0.017 it would
add to the tilt. During the de Sitter plateau the local ZBW microphysics is roughly stationary (it is the
global reach/occupation that evolves), so T ≈ const is plausible — but this is a check to run, not a
given.

## 4. The statistics — Gibbs (indistinguishable), and the ZBW phases as an exchangeable bath

The ln n is the configurational/mixing chemical potential of indistinguishable particles — the 1/n!
Gibbs factor in Z = zⁿ/n!. **Requirement:** the stack obeys Gibbs statistics, i.e. the ZBW phases act as
an **exchangeable thermal bath** (a shared, re-randomizing stochastic layer), **not** as permanent labels
that tag individual CPs. This is the precise lesson of 0749: ZBW-as-bath → indistinguishable → ln n →
0.9649; ZBW-as-label → distinguishable → constant μ → cliff. **Assessment:** this is a genuine
commitment, but a natural one — the ZBW phases are already treated as an effectively random, re-sampling
layer everywhere else they are used. Which leads to the central point:

## 5. The deep point — determinism is not a barrier, and this is the SAME commitment as Gaussianity

CPP is a deterministic PCD substrate, and one might object that a deterministic substrate cannot have a
temperature or an ensemble. **It can — for exactly the reason classical statistical mechanics works.**
Newtonian mechanics is deterministic, yet temperature, entropy, and chemical potentials emerge from
coarse-graining many degrees of freedom under *molecular chaos* (effective mixing/ergodicity). A CPP
stack ensemble requires the same thing: the ZBW layer must be **effectively mixing/ergodic** so that
coarse-graining a stack yields a Gibbs ensemble.

Crucially, **this is not a new assumption.** The early-universe sector already relies on exactly this:
the Gaussianity result (0738) is "CLT over ZBW phases," which *already* treats the ZBW layer as an
effectively random, exchangeable bath generating Gaussian statistics. A stack chemical potential μ ∝
ln n is the *same* ZBW-as-effective-thermal-bath assumption applied to a different observable
(configurational entropy of occupation, rather than sums of kicks). So the cost of "stack thermodynamics"
is not a fresh structural commitment bolted on for the tilt — it is the continuation of the commitment
the sector already made for Gaussianity. If you accept ZBW-driven CLT Gaussianity, you are most of the
way to accepting a ZBW-driven stack ensemble.

## 6. The boost coupling — H_eff ∝ μ, and the graceful exit comes free

**Requirement:** the H-engine grows PSR_base at a rate proportional to the stack's chemical potential
(the dispersal drive), H_eff ∝ μ(n̄) ∝ ln n̄ — the count-driven/entropic branch established as the only
viable one in 0746 (PSR_base is the SSV-independent baseline, so an entropic count-driven growth is
consistent with what PSR_base is). **Bonus consistency:** μ(n) ∝ ln n vanishes at equilibrium n* = 1
(ln 1 = 0). So as the patch dilutes to n̄ → 1, H_eff → 0 **smoothly** — the graceful exit is automatic
and is the *same* mechanism as the plateau, not a separate exit rule. This is exactly the smooth wind-down
(not a cliff) that 0744 identified as required, now delivered by the chemical potential itself.

## 7. What is robust, what is assumed, what would break it

**Robust (needs no derivation):** the tilt p = 2 / n_s = 0.9649, given only μ ∝ ln n and T ≈ const over
the window. Independent of T's value, V's value, and the offset.

**Assumed (the explicit commitments):**
- (A) The ZBW layer is effectively mixing/ergodic, so a stack of identical CPs is a Gibbs ensemble with a
  chemical potential — *continuous with the Gaussianity assumption (§5).*
- (B) The H-boost couples to that chemical potential (count-driven branch, 0746).

**Falsifiers (what would send it back to the excluded column):**
- ZBW phases are *permanent per-CP labels* (distinguishable) → Ω = qⁿ → constant μ → n_s = 1 cliff.
- T varies across the observable window at a rate ~1/N_rem → an extra, uncontrolled tilt.
- The boost is field/stress-driven (SSV) rather than chemical-potential-driven → the 0746 mechanical
  branch → excluded.

## 8. Honest status

This is a **specification, not a derivation.** It does not show that CPP *has* a stack ensemble; it states
precisely what CPP would have to own (§1–§6) and shows that the cost is smaller than it looks — most of
the thermodynamic detail is irrelevant to the tilt (§0, §7), and the load-bearing assumption (ZBW as an
effective thermal bath) is the *same* one the sector already uses for Gaussianity (§5). If CPP can own
that — i.e. if the ZBW layer legitimately gives a stack of identical CPs a concentration chemical
potential — then **n_s = 0.9649 is derived, coefficient-free, with N_* fixed by the CP count**, and the
spectrum thread closes. If not, n_s = 0.9649 remains favored, not derived. The decision is now a single,
well-posed question about CPP's foundations: **does the ZBW layer make a CP stack a thermodynamic
ensemble?**

## Pointers

- Builds on 0749 (the log = indistinguishable concentration chemical potential), 0746 (count-driven
  branch), 0738 (CLT-over-ZBW Gaussianity — the precedent for ZBW-as-bath).
- Reasoning: `series_relativity/development/reasoning/0750_stack_ensemble_spec.md`.
- Next: the foundational question — can CPP's ZBW layer be shown (or posited as a named axiom) to give a
  CP stack Gibbs statistics with μ ∝ ln(n/V)? If yes, write the derivation chain
  ZBW-bath → Gibbs stack → μ ∝ ln n → H_eff ∝ ln n → n_s = 0.9649 and register it.
