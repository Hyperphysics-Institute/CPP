# Founder rulings — the CP Exclusion Rule is RETIRED; the PSR floor is a REGISTER limit; the mirror is kept (31 Aug – 1 Sep 2026, Session 161, GR lane)

**Status:** verbatim founder text, registered at Patch 3366. Rulings minted:
**R-EXCL-RETIRED** (items 1, 3), **R-FLOOR-REGISTER** (item 3), **R-MIRROR-KEPT** (item 2).
Consequences enacted at Patches 3366–3367; corrigenda to shipped GR-1b/GR-1c
owed under CONV-038 (see `frontier_sectors/GR.md`).

**How this arose.** The Session-160 handover queued, as its load-bearing item,
"derive the wall condition X = 0 from the rotating clamped register." The
founder asked what a "clamped register" is. The term proved to be an Opus
coinage (Patch 3297, 21 Aug 2026; 40 occurrences in 19 files; no glossary
entry; never in the founder's words). Tracing its physics led to the CP
Exclusion Rule (GR-1b definitions; GR-1c Theorem 2 proof), which is absent
from `axiom-registry.md`. The founder then ruled as follows.

---

## 1. The Exclusion Rule was retired (31 Aug 2026)

> "We originally had the CP exclusion rule, and we eliminated it when we
> realized that it was unnecessary. We used the ZBW effect instead, merely
> looking at the local SSV_net at each Moment after superimposition. The CP
> exclusion rule was unnecessary because we achieved its effect simply by
> looking at the environment and moving in the direction of the SSV_net the
> next Moment."

*Opus note:* no patch, glossary line, or registry entry records this
retirement. GR-1b (shipped) and GR-1c Thm 2 (shipped, CONV-030 5–0) invoke the
rule as live. This is a **retirement without a tombstone**; the tombstone is
now `axiom-registry.md` §"Retired rules (anti-erasure ledger)", Patch 3366.

## 2. The mirror is kept (31 Aug 2026)

Offered the fork between information conserved by *reflection* (|R| = 1 exact,
Patch 3297) and by *storage in surface strata* (the founder's superposition
picture of 31 Aug, which is Axiom H, founders_vision §6e):

> "The mirror is less complicated. Let's see how it plays out. If it solves
> all the problems consistently, then that's the triangulation we are looking
> for."

## 3. The floor is a register limit, not a packing limit (1 Sep 2026)

Offered the fork "packing limit (one-per-GP, kinematic, PSR → GP spacing) vs
register limit (SSV_abs saturates at k·u = 1, PSR floor l_P/2, GPs still
~10²⁹ deep)":

> "I had seen the packing limit as one CP per GP, but I think that produces the
> frozen BH that can't move. If there are 10^29 GPs between CPs, then there is
> plenty of room for the CPs in the BH to mediate rotation and translation, and
> in general respond to the SSV_net, etc. The bottom line question is: what is
> the minimum PSR distance? How is that established? Why should that naturally
> arise as a theorem from the axioms?"

> "I think the one CP per GP is inconsistent with reality, so we can safely
> eliminate that option. I think your second framing of the register limit of
> SSV_abs and PSR floor of l_P/2 is rational. Does this follow from our axioms,
> or is this an axiom?"

*Opus answer (Patch 3367):* as of the ruling it was **neither** — its only
derivation (GR-1c Thm 2) rested on the retired rule. Re-derived at 3367 from
Buchdahl + the exact exterior + incompressibility (Route A), conditional on the
field equation holding at saturation (OPEN-GR-RCORE-4). See
`rcore_derivation/3367_psr_floor_from_buchdahl.md`.

## 4. The founder's own physical picture of the surface (31 Aug 2026) — recorded as the wall-condition definition

> "Even though the CPs are at full density, when the BH is impacted at its
> surface, the DI-bits associated with the energy of the Impact are transmitted
> to the GPs on the surface, which displace the CPs on the GPs."

> "Since the GPs are full, if a CP receives a move message, it moves onto an
> already occupied GP. Thus, in the next Moment, the CP will be transmitted via
> the SSV_net to the position associated with that displacement."

> "The register is just the value of the SSV_abs."

*Opus note:* under R-EXCL-RETIRED this is the boundary condition item 1 must
compute: a **compliant boundary with a one-Moment delay** (superimpose, then
displace per SSV_net), not a two-sided clamp. "Clamped register" is therefore
the wrong name for the wrong object; the glossary entry is HELD until the
surface response is computed (Patch 3366 registers this; the term is not yet
swept from the corpus — 40 sites — pending the computation that replaces it).

## 5. The founder's diagnosis that opened the thread (31 Aug 2026)

> "I realized that the current set of axioms cannot properly address whether
> the impact of a mass or wave on the surface of a Black Hole can propagate
> through the Black Hole. This question brings up a corollary question: how does
> a Black Hole move through space by KE … with the current axioms, the BH
> cannot move once it forms, because the SSV_net cannot transmit beyond one PSR,
> and in a 100% saturated space by axiom does not reach to the next GP. The same
> problem makes it impossible for the Black Hole to rotate."

*Opus note:* the diagnosis holds under the packing reading and dissolves under
the register reading (floor l_P/2 spans ~10²⁹ sub-Planck GPs; c_* = c/2 in the
core; translation by synchronous lockstep under A4). What survives it, and is
new: **rotation of a saturated core has never been derived** — 3339/3359
assumed a wall at Ω_w. Registered as OPEN-GR-ROT-1 (Patch 3366).

## 6. Instruction to proceed (1 Sep 2026)

> "Please proceed."
