# Brick #4 follow-up: stack entropy — the log is INDISTINGUISHABILITY, not distinguishable phases

*Patch 0749, Session 154. Tests the swarm's (Copilot) stack-entropy proposal: drive H by the
configurational entropy S(n) of n CPs on a GP, H ∝ ∂S/∂n (chemical potential), with Ω(n) ∼ n! "→ ln n".
Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0749_stack_entropy_test.py`. NO THEO.
**Result: the entropy route is correct (real convergence with 0748), and the log IS a chemical
potential — but specifically the concentration chemical potential of INDISTINGUISHABLE CPs, μ ∝
ln(n/V). Copilot's stated mechanism (distinguishable ZBW-phase arrangements → Ω ∼ n!) is muddled:
distinguishable labels give Ω = qⁿ → extensive entropy → CONSTANT μ → the n_s = 1 cliff (excluded). The
log needs the opposite. n_s = 0.9649 is derivable iff a CP stack is a genuine thermodynamic ensemble in
CPP — the sole remaining commitment.***

## What's right (real convergence)

Copilot independently reached the 0748 conclusion: **only microstate counting can give the log**;
geometry/placement/packing all give power laws or constants (excluded). That diagnosis is correct, and
the focus on a configurational entropy S(n) with H ∝ ∂S/∂n (chemical potential) is the right object.

## What's right about the log specifically

The log is a chemical potential — the **standard chemical potential of an over-concentrated species**:
n identical CPs crammed into the fixed volume of one GP have μ ∝ ln(n/V) ∝ ln n. This is textbook
statistical mechanics (the n! Gibbs divisor in Z = zⁿ/n! → Sackur–Tetrode → μ ∝ ln(concentration)). It
is well-motivated, and it gives n_s = 1 − 2/N_* = 0.9649 with the tilt p = 2 **independent of any
coefficient** (since d ln(ln n̄)/dN = −1/N_rem regardless of the constant). So *if* the boost is this
concentration chemical potential, 0.9649 follows robustly.

## The catch (computed, not asserted)

"Ω ∼ n! generically" is **not** generic — the microstate count decides everything, and the two natural
readings give opposite answers:

| stack entropy model | S(n) | μ = ∂S/∂n | n_s | verdict |
|---|---|---|---|---|
| **distinguishable** labels (distinct ZBW phases), Ω = qⁿ | n·ln q (extensive) | const | **1.0000** | cliff — EXCLUDED |
| **indistinguishable** ideal gas, fixed V (Ω = zⁿ/n!) | n·ln(V/n)+… | ∝ ln n | **0.9649** | matches Planck |
| orderings counted, Ω = n! | ln(n!) | ∝ ln n | **0.9649** | matches Planck |

**Copilot's stated mechanism — distinguishable ZBW-phase arrangements — gives the CLIFF, not the log.**
If each CP independently carries one of q phase-states, Ω = qⁿ, the entropy is extensive (S = n·ln q),
the chemical potential ∂S/∂n = ln q is **constant**, H_eff is constant, and n_s = 1 (Harrison–Zel'dovich,
excluded). The log comes from the **opposite** property — *indistinguishability* (the Gibbs n! divisor /
fixed-volume concentration) — which is the standard chemical potential of a concentrated species and
does **not** need ZBW phase microstates at all. The ZBW phases were invoked to make CPs *distinguishable*
(so there would be microstates to count), but distinguishability is exactly what pushes toward the
excluded cliff.

## The honest structural commitment

Getting the indistinguishable-concentration chemical potential μ ∝ ln(n/V) requires treating a CP stack
as a genuine **thermodynamic ensemble** — a CPP "temperature" / Gibbs statistics at the stack level.
CPP's primitives are deterministic PCD; whether they support a real stack ensemble (so that μ ∝ ln(n/V)
is a legitimate quantity, not an analogy) is the open commitment. This is the sharpened, and now
*correctly posed*, version of the question:

- **If a CP stack is a thermodynamic ensemble** (identical CPs, a notion of stack temperature/statistics)
  → μ ∝ ln(n/V) is the standard concentration chemical potential → H ∝ ln n → **n_s = 0.9649 derived**
  (coefficient-free p = 2), and the spectrum thread closes.
- **If CPP has no stack thermodynamics** → the log has no home and n_s = 0.9649 stays favored, not
  derived.

## Status

- Entropy route: **correct** (converges with 0748). Geometry/placement: dead.
- The log: **a standard concentration chemical potential of INDISTINGUISHABLE CPs** (μ ∝ ln(n/V)), not
  distinguishable phase arrangements (those give the cliff). Coefficient-free p = 2.
- Remaining question (sharp, physical, and now correctly framed): **does a stack of identical CPs in one
  GP constitute a thermodynamic ensemble in CPP — a temperature / Gibbs statistics — so that μ ∝ ln(n/V)
  is a real quantity?** That, not phase labels and not a placement rule, is what makes 0.9649 derived.

## Pointers

- Builds on 0748 (only microstate counting gives the log) and 0746 (count-driven branch). Tests the
  Copilot stack-entropy transcript.
- Toy + verify: `.../early_universe/scripts/0749_stack_entropy_test.py`.
- Reasoning: `series_relativity/development/reasoning/0749_stack_entropy_test.md`.
- THE question: is a CP stack a thermodynamic ensemble in CPP (→ μ ∝ ln(n/V) → 0.9649 derived)? The log
  needs indistinguishable-particle concentration statistics, not distinguishable ZBW-phase microstates.
