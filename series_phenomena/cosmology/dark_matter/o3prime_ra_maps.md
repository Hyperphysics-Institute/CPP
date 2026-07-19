# O3′ executed: the accessibility maps — the strong channel is open at the epoch, the electric channel has zero accessible epoch cells; 49 unanimous-DEAD cells hand off to K1a triage

**Patch 2571, 19 July 2026. Governed by `o3prime_preregistration.md` (2570) ONLY. Artifact:
`code/2571_o3prime_maps.py` (83 s; all coherence asserts pass). Status: R-A, R-B, R-C EXECUTED;
maps FROZEN.**

## 1. Estimator disclosure (anti-erasure; before any result)

First run: the W-2 ≤ min W-1 coherence assert FIRED at b = 0.25·a_qq by 7×10⁻⁵ MeV — a
finite-grid artifact (W-2's orientation/separation grid missed an optimum that W-1's finer line
scan found). Fix, structural not tolerance-based: W-2's admissible set CONTAINS W-1's by
definition (prereg §3), so the estimator now enforces the superset by explicit union (and the
canonical axes were added to the orientation grid so class orientations are exact). The fix can
only DEEPEN W-2 — the generous direction — making DEATH strictly harder to declare: the honest
direction. Re-run clean. No convention was chosen or changed; the prereg's definitions are
implemented more faithfully, not differently.

## 2. The frozen wells (MeV; floor ±2)

**qDP+qDP:** W-2(b) = −59.7 / −55.8 / −46.5 / −35.8 / −26.5 / −16.6 / −13.1 across
b/a_qq = 0…2.0. Per-class W-1 spans reach the same depths at optimal classes; repulsive-only
lines (W-1 ≥ 0) exist at every b for adverse (class, parity) combinations — orientation matters
structurally, exactly why the map is per-class.
**qDP+eDP:** W-2(b) = −10.2 / −9.0 / −6.6 / −4.5 / −3.4 / −2.3 / −1.3 — an order of magnitude
shallower, as the √(α_s·α) coupling implies.

## 3. The frozen verdict grids (summary; full grids in the artifact)

**qq:** ACCESSIBLE (unanimous or majority) throughout E ≤ 5 MeV at b ≥ 0.25; at the epoch rows
(E = 10, 15; ambient context only) accessible at b/a_qq ∈ [0.5, 1.0], mixed/marginal at the
edges; unanimous DEAD begins at (20, b ≥ 1.5) and covers E = 50 for b ≥ 0.5 and all of E = 100.
**qe:** accessible only at E ≤ 1 MeV and small b; **at the epoch rows the channel has ZERO
ACCESSIBLE cells** — E = 15 is unanimous-DEAD at every b; E = 10 is dead for b ≥ 0.5 and
marginal (not accessible) at b ≤ 0.25. The prereg's channel-level adverse reading ("all-DEAD at
EVERY epoch row") does not fire — E = 10 retains marginal cells — so the finding banks at map
strength with the frozen categories, stated plainly: **at the derived formation epoch, free
qDP+eDP capture is energetically closed or marginal everywhere; only the strong (qq) channel
presents accessible cells.** Evidence-shaped note for K2's prereg (an observation, no mechanism
reading, trap clause intact): epoch-era assembly, if it initiates, initiates through the strong
channel; electric-sector attachment at epoch energies cannot begin from free-pair capture on
this map.

## 4. R-C handoff (the triage table for O1a production)

Unanimous-DEAD cells (excludable from O1a production per prereg §5): **qq — 14 of 63** (E = 20:
b ≥ 1.5; E = 50: b ≥ 0.5; E = 100: all b). **qe — 35 of 63** (E = 5: b ≥ 1.5; E = 10: b ≥ 0.5;
E ≥ 15: all b). Total 49/126 cells (~39%) excluded. Rigidity disclosure travels: DEAD is
conditional on rigid DPs; revival of any dead cell requires K1a/K1b deformation-channel
evidence, never retroactive softening of this map (prereg §5, verbatim). Mixed cells (lowercase
in the artifact grids) run in O1a per-class where their accessible sub-cells sit.

## 5. Reading (per 2570 §5, frozen)

**MAPS FROZEN AND BANKED as the K1a triage input.** No capture claim exists anywhere in this
document; ACCESSIBLE asserts possibility only. No composition reading. The 102-scale contact
depth appearing inside the qq wells is the pre-existing registered lineage (fence-noted, nothing
new). No new √5. Dated line to the standing disclosure queue.

## 6. Bookkeeping

79.5% untouched. Queue: **K1a pre-registration next** (O1a instrument + capability census +
bound-state invariance control + this handoff table as a named input), then K1b R-A. Next
patch: 2572, the K1a prereg.
