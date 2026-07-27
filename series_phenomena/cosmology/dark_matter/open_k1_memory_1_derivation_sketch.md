# OPEN-K1-MEMORY-1 — DERIVATION SKETCH (Patch 2834)

**Filed 2026-07-27 at founder direction, alongside the Patch 2833
obstacle note. A SKETCH, not a preregistration and not a claim: it
sets out an analytic route to clause 2, identifies the two ingredients
it needs, and reports honestly which are pinnable and which are not.
Nothing here is enacted; PR7 remains PARTIAL.**

## §1 — The founder's ruling reframes the question

**Founder, 2026-07-27:** *"There is no memory in the system for the
KE/momentum, only an out-of-equilibrium position of the DP poles,
which exert force on the moving charge."*

This is C23 restated: no velocity memory anywhere; the current state
(CP positions **plus** displaced DP poles) determines the future
completely. **The full dynamics is therefore MARKOVIAN.**

**Consequence, and it dissolves the obstacle of Patch 2833.** Memory
kernels are properties of *descriptions*, not of dynamics. In the
Mori–Zwanzig construction a kernel appears exactly when degrees of
freedom are projected out: what the eliminated variables were doing
instantaneously reappears, in the reduced description, as
history-dependence of the retained ones. A Markovian full dynamics,
projected, yields a non-Markovian reduced dynamics — that is the
entire content of the formalism.

**So PR7 clause 2 is not asking whether the substrate has memory.**
(By the founder's ruling, it does not.) It asks: **when the Sea is
projected out and only the charge degrees of freedom are retained —
which is precisely what the screening derivations do — how large is
the INDUCED memory at d_DP?** This is a question about the
substrate, answerable analytically, and it does not route through any
Monte Carlo sampler. The 2833 obstacle is thereby avoided rather than
worked around.

## §2 — The subdominance criterion

The induced kernel K(t) decays on the relaxation time of the
projected-out variables — here, the DP arc configuration. Write
**τ_Sea** for that time and **τ_slow** for the time on which the
retained variables change appreciably at the d_DP scale. Standard
result: as τ_Sea/τ_slow → 0 the kernel collapses toward a delta
function and the Markovian (instantaneous) bridge holds to leading
order. **The subdominance parameter is**

> **ε_mem ≃ τ_Sea / τ_slow , evaluated at d_DP.**

The founder's ZBW draft already asserts the needed inequality
qualitatively: *"Given the rapidity of the ZBW cycle compared to the
translational velocity of the DP center, each ZBW cycle will have
approximately the same SSV_net operating at each superposition and
perigee moment."* That IS a timescale-separation statement. Clause 2
asks for it quantitatively at d_DP.

## §3 — The two ingredients, and the decisive fork

**Ingredient 2 — τ_slow — is pinnable.** The retained variables at
d_DP change as a DP centre traverses that distance:
τ_slow ≃ d_DP / v, with d_DP = a = 0.3640 fm and v the DP-centre
translational speed.

**Ingredient 1 — τ_Sea — is NOT yet pinned, and everything turns on
it.** The Sea's arc configuration relaxes on the ZBW cycle, but the
record supports two readings that differ by ~10²:

- **Reading (A): Compton-scale ZBW.** τ_Sea ≃ λ̄_C/c with
  λ̄_C = 386.2 fm. Then λ̄_C/d_DP = **1061**, so
  **ε_mem ≃ 1061 (v/c)** — subdominance below 0.15 requires
  **v/c < 1.4 × 10⁻⁴**.
- **Reading (B): Sea-lattice ZBW.** AUTOMATON-2 measured a bonded-pair
  ZBW period of **10–12 Moments** (Patch 2805) at its own lattice
  scale. If the Sea's arc relaxation is set by that — τ_Sea ≃ 10 a/c —
  then since d_DP = a, **ε_mem ≃ 10 (v/c)**, and the 0.15 bar needs
  only **v/c < 1.5 × 10⁻²**.

**These are not close.** Reading (A) demands a Sea thermal velocity
below 10⁻⁴ c; reading (B) is comfortably satisfied by any
non-relativistic Sea. **Clause 2 closes on paper under (B) and is in
genuine doubt under (A).**

## §4 — What this sketch does NOT claim

It does not assert ε_mem is small. It asserts that ε_mem is
**analytically expressible** and reduces to ONE unpinned quantity:
the physical relaxation time of the DP arc configuration. It also
does not transfer AUTOMATON-2's 10–12-Moment period to the physical
d_DP scale — the regime diagnosis (Patch 2810) showed exactly how
badly lattice-scale conclusions can travel, and reading (B) leans on
precisely such a transfer. **That transfer is the sketch's weakest
joint and is named as such.**

## §5 — The founder question this reduces to

**On what timescale does the DP arc configuration around a moving
charge relax — the Compton-scale ZBW of the constituent particles, or
the Sea-lattice ZBW cycle of the bonded pair?** With that ruled, ε_mem
is a number, and clause 2 either closes analytically or fails with a
specific quantitative reason. **This is a single physics question, not
a campaign** — and it is markedly smaller than the FEM study the
founder feared clause 2 might require.

If the answer is (A), the FEM route returns as the way to pin τ_Sea
directly. If (B), clause 2 closes with a derivation and PR7 completes
without new compute.

## §6 — Standing

Nothing enacted. PR7 PARTIAL; ledger six of seven; B7 holds. The
sketch travels to the panel with the 2833 obstacle note so both are
adjudicated together.
