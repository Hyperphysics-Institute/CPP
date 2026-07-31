# FOUNDER RULING — DI-BIT CONSERVATION IS FOUNDATIONAL; AND THE SUB-MOMENT PROPOSAL

**2 August 2026, Patch 2894. Captured in the same patch that acts on it,
per CONV-009.**

---

## §1 — THE FOUNDATIONAL RULING

> The requirement of DI-bit conservation and Shell Broadcast, and
> re-broadcast, and holographic superimposition are the foundation of the
> CPP system at the most elemental level. All phenomena should fall out of
> this. **If it doesn't then this is the rule that should be changed.**

**That last sentence is a falsification licence and this patch uses it.**

## §2 — THE SUB-MOMENT PROPOSAL, verbatim

> - A few sessions ago we considered changing the model a little in terms
>   of how the DI-bits radiated from the GP_origin to the PSR.
> - In that scenario, the DI bits transit all the edges (between all GPs
>   between GP_origin to GP_PSR (PSR at SSV_abs).
> - In this scenario, the DI bits were repeatedly re-radiated spherically
>   to their 12 closest neighbors.
> - Thus every GP would radiate (and repeatedly re-radiate at each GP) to
>   all the GPs between the GP_origin to all the GPs on the shell radius
>   (PSR) at GP_PSR associated with the SSV_net.
> - Each of the sub-radiations would be a "sub-Moment".
> - There is thus an ambiguity; how many sub-Moments are there?
> - And how many DI-bits are emitted by each GP_origin?
> - This might be the maximum possible steps between the GP_origin and the
>   potential most distant CP.
> - Do the DI-bits recycle or are they emitted new each Moment? (I think
>   every DI Bit issuing a new DI-bit each moment is the cleanest, but that
>   is an ontology problem, **the DI-bit is actually a conscious point that
>   is moving between GPs communicating with the GPs at each hop.**) So,
>   the DI-bits probably have to be conserved, just like CPs, GPs, and now
>   DI-bits.

## §3 — THE RULING DISSOLVES THE PATCH 2893 FORK

At 2893 the worker reported a conflict between exact **SSV_net (vector)**
conservation and clean forward propagation. **That conflict was an
artifact of the worker's own choice at 2892 to impose vector
conservation.** The founder specifies conservation of the **DI-bit count —
a scalar.**

Verified: for **any** dipole coefficient k, the rule
w_d = S/12 + k(V·d̂) has Σ_d w_d = S exactly, because Σ_d d̂ = 0.
**Measured DI-bit total = 1.00000 for all three obliquities tested.**

**Scalar bit conservation places NO constraint on obliquity.** The fork is
withdrawn.

## §4 — THE MEASUREMENT (code/2894_obliquity_shell_test.py)

M = 64, impulse at t = 0, 12 sub-steps, shell fraction = |Q| in the outer
25% of the light cone r ≤ t√2.

| rule | obliquity | bulk p | shell frac | bits |
|---|---|---|---|---|
| Kirchhoff | (1+cos θ)/12 | 0.431 | 0.002 | 1.00000 |
| 2892 vector | (1+3cos θ)/12 | **0.674** | **0.145** | 1.00000 |
| isotropic | 1/12 | 0.379 | 0.000 | 1.00000 |
| **directed relay (Patch 2889)** | *no closure* | **1.0000** | — | — |

**FINDING 1 — the founder's "subtraction" is doing the work, and the
worker predicted this backwards.** Kirchhoff merely *vanishes* backward;
the vector rule goes *negative* backward, actively cancelling. **Negative
backward lobe → more ballistic.** The worker expected Kirchhoff to win
because it is the textbook Huygens factor; it loses, decisively.

**FINDING 2 — and it is decisive for the proposal.** Even the best
re-radiation rule reaches p = 0.674 with only **14% of amplitude on the
shell**. The directed relay, which performs **no re-radiation at all** and
simply lets each channel continue, gives **p = 1.0000 exactly** (Patch
2889).

> **ANY re-radiation rule that compresses the arriving pattern to a
> low-order moment LOSES BALLISTICITY, regardless of obliquity. What makes
> propagation ballistic is the FULL ANGULAR DISTRIBUTION, and every
> closure discards it.**

## §5 — CONSEQUENCE: THE SUB-MOMENT RE-RADIATION PICTURE CANNOT BUILD THE SHELL BROADCAST

The c05 specification requires a **growing spherical shell** with
Q/4πr² dilution — amplitude **on** the shell, ballistic front.

**Sub-Moment re-radiation, as described in §2, does not produce that.** N
sub-Moments of compress-and-re-emit gives a filled, largely diffusive ball
with a front at radius ≈ √N rather than N, and ≤ 14% of amplitude near the
front. **This is measured, not argued.**

**Under the founder's own falsification licence (§1), this is the rule
that should change.**

## §6 — THE FORK IS ONTOLOGICAL, AND THE FOUNDER STATED IT HIMSELF

His parenthesis is the resolution: *"the DI-bit is actually a conscious
point that is moving between GPs communicating with the GPs at each hop."*

**BRANCH 1 — DI-bits are TRAVELLING CONSERVED ENTITIES.** A bit keeps its
identity and heading, communicating with each GP it passes rather than
being re-computed by it. **Consequences, all measured or immediate:**
ballistic (p = 1.0000, Patch 2889); a genuine expanding shell; **1/r²
falloff from conservation plus spherical spreading — exactly c05's
geometric dilution**; retarded by construction, which **answers CONJ-FP-1
Condition B by inspection.**

**BRANCH 2 — DI-bits are RE-RADIATED AMPLITUDES.** Each GP absorbs and
re-emits based on its local SSV_net. **Consequences, measured:** p ≤ 0.674
at best, no sharp shell, ≤ 14% amplitude on the front. **Cannot reproduce
the shell broadcast at any obliquity.**

**The founder's own instinct — "a conscious point that is moving between
GPs" — is Branch 1, and Branch 1 is the one that works.**

## §7 — THE SUB-MOMENT COUNT, ANSWERED UNDER BRANCH 1

The founder asked how many sub-Moments there are. **Under Branch 1 the
question resolves itself:** a bit travelling ballistically from GP_origin
reaches the PSR shell in

    N = PSR / l_P   hops

so **the number of sub-Moments is the shell radius in lattice units**,
which is precisely the founder's own suggestion — *"the maximum possible
steps between the GP_origin and the potential most distant CP."*
**Self-consistent, with no free parameter.**

**Under Branch 2 the count remains genuinely ambiguous**, because the
front advances as √N and never cleanly "arrives" anywhere.

## §8 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1 and P-A2-1 stand. Statics claims remain suspended per 2892.
**CONJ-FP-1 Condition B: resolvable by inspection under Branch 1.**
