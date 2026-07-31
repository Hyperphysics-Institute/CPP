# THE ARC HAS BEEN TESTING THE WRONG MODEL — SHELL BROADCAST ≠ NEIGHBOUR RELAY

**Patch 2893. Found by reading the specification the founder pointed to
rather than continuing to instrument a reconstruction of it.**

---

## §1 — THE SPECIFICATION, AS WRITTEN

`series_relativity/SR_companion_papers/c05_newtonian_gravity_from_SSV/c05_gravity_from_SSV_shell_broadcast.tex`, §69–71:

> *"a Grid Point (GP) emits a fixed SSV quantum Q per Absolute Moment tick,
> distributed over the **growing spherical shell** at radius r, giving
> ΔSSV ∝ Q/4πr² ∝ 1/r²"*

and §56–57:

> *"The inverse-square law follows from the shell-broadcast geometry."*

**This is BALLISTIC expanding-shell propagation with GEOMETRIC dilution.**
The shell grows at c; a conserved quantum Q spreads over an area ∝ r²;
hence 1/r². **The inverse-square law is geometry, not a diffusive steady
state.** There is no random walk in the specification at any point.

## §2 — WHAT THE ARC ACTUALLY TESTED

| patch | engine | rule |
|---|---|---|
| 2887 | AUTOMATON-2 convolution | nearest-neighbour, isotropic re-spread |
| 2889 | directed relay | nearest-neighbour, direction retained |
| 2890 | σ-family | nearest-neighbour, σ-weighted mix |
| 2892 | coherent rule | nearest-neighbour, SSV_net conserving |

**All four are NEAREST-NEIGHBOUR RELAYS. None implements the shell
broadcast.** The diffusive behaviour found at 2887, the σ-family
construction of 2890, and the P1-closure diagnosis of 2892 are all
properties of a model the specification does not describe.

**The founder pointed at SR-1 and its companions in his 2 Aug message.
Reading it should have preceded five patches of instrumentation.**

## §3 — CAN PER-CP RE-RADIATION REPRODUCE THE SHELL? THE OBLIQUITY TENSION

The founder's 2 Aug statement describes re-radiation *at each CP*:

> *"Every CP receives the DI-bits it receives, calculates the SSV_net from
> that totality, and then re-radiates the SSV_net to the spherical shell
> that is at the distance that is present at each local SSV_abs (the
> PSR/l_P). … It produces a holographic filling."*

**Huygens' principle says per-point re-radiation CAN reproduce free
propagation — but only with the correct obliquity factor.** The Kirchhoff
factor is

    K(θ) = (1 + cos θ)/2

monopole and dipole weighted **equally**, vanishing **exactly backward**
(θ = 180°). That backward null is what prevents a back-propagating wave.

**The rule derived at Patch 2892 from exact SSV_net conservation is
different.** For a directed pulse (S = |V|), w_d = S/12 + (V·d̂)/4 gives

    w(θ) ∝ (1 + 3cos θ)/12

which vanishes at **θ = 109.5°**, not 180°, and is **negative** beyond.

Conversely, checking what the Kirchhoff form conserves: with
w_d = (S/12)(1 + V̂·d̂) and the FCC sums Σd̂ = 0, Σd̂_i d̂_j = 4δ_ij,

    Σ_d w_d d̂ = (S/12)·4·V̂ = S V̂/3

**which equals V only when |V| = S/3.**

> **CONSERVING SSV_net EXACTLY AND REPRODUCING FREE-SPACE PROPAGATION ARE
> DIFFERENT RULES.** They coincide only at the single ratio |V| = S/3.

**This is a genuine physics fork, not an implementation detail**, and it is
the reason the coherent rule returned p = 0.65 rather than 1.0.

## §4 — WHAT THIS DOES AND DOES NOT OVERTURN

**STANDS — G1 and P-A2-1.** Measured on the real engine against a pointwise
Ewald reference. **But its interpretation narrows further:** it establishes
that a nearest-neighbour relay reproduces the *static* Coulomb profile. The
specification derives 1/r² from **shell geometry instead**, so G1 was never
a test of the specification's own mechanism.

**STANDS — light-cone invariance.** Direct maximum-extent measurement,
no fitting, confirmed three times across every rule tested.

**NARROWED — the 2887 "relay is diffusive" finding.** True of the
convolution engine, which remains a fact about that engine. **It is not a
statement about the CPP specification**, which is ballistic by
construction. The 2887 escalation is narrowed accordingly.

**UNCHANGED — the statics suspension of Patch 2892.** Those measurements
were contaminated and remain suspended regardless.

**RESOLVED IN PRINCIPLE — the "dilemma" of Patch 2890.** There was never a
tension between ballistic dynamics and 1/r statics *in the
specification*: an expanding shell gives both simultaneously and trivially.
**The dilemma was an artifact of testing nearest-neighbour relays.**

## §5 — THE QUESTION NOW BEFORE THE FOUNDER

Both readings are in the corpus and they are not equivalent:

**READING A — direct shell broadcast (c05, as written).** The source's
emission expands as a shell; amplitude dilutes as 1/r² by area. Ballistic,
retarded, 1/r² — all three immediately, with no closure problem.

**READING B — per-CP re-radiation (2 Aug message).** Each CP compresses
what it receives to SSV_net and re-emits to a shell at PSR. This is a
Huygens construction and reproduces Reading A **only if** the obliquity is
Kirchhoff-like — which, per §3, conflicts with exact SSV_net conservation.

**Which is the mechanism?** If A, the propagation problem is solved and the
arc should return to CONJ-FP-1 Condition A (the sign of the Sea's
response). If B, the obliquity must be specified, and whether it conserves
SSV_net exactly or vanishes exactly backward is a physical choice with
different consequences.

## §6 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1 and P-A2-1 stand. **CONJ-FP-1 Condition B: OPEN, and now
plausibly resolvable by inspection rather than simulation** — a shell
broadcast is retarded by construction.
