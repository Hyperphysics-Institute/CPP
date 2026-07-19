# K1a / O3′ pre-registration: the accessibility bound — capability census, closed inputs, frozen conventions and grids, the DEAD criterion, routes, and readings, committed before any derivation

**Patch 2570, 19 July 2026. Status: O3′ OPENED at pre-registration; NO derivation performed.**
Governed by the NB-S3a-1 charter v1.1 (2569) and this document only. **Verify: none needed at
prereg (declarations only).** Collision check clean (no prior O3/accessibility registration in the
DM lane).

## 0. Target, and what this map is NOT

**Target:** for the two charter encounter channels — **qDP+qDP** and **qDP+eDP** — an accessibility
map over (E_rel, b, orientation class): which cells are **DEAD** (the relative kinetic energy
exceeds every dynamically accessible well, so capture is impossible regardless of dynamics or
sink) and which are **ACCESSIBLE** (capture possible-not-established, awaiting K1a dynamics and a
K1b sink). **This map is never capture** (charter §1, verbatim): ACCESSIBLE cells assert nothing —
no efficiency, no rate, no cross-section; DEAD cells assert a falsifier-grade negative. The map's
payoff is triage: DEAD cells are excluded from expensive O1a production runs (with the §5 caution
on convention-robustness).

## 1. Capability census (charter §3 rule; satisfied by inspection)

The computation is a pure statics evaluation: the registered dance interaction energy
E(config) = Σ_pairs qw_i·qw_j / √(r² + A²ᵢⱼ) · AHC (the amat/soft_a/qw_of machinery, verbatim in
`code/2557_reregistration_reach_s.py`) evaluated on STATIC rigid configurations. No dynamics, no
reach lists, no home frames, no time stepping. The instrument trivially represents every object
this prereg names; census closed. (The 2565-banked extension and classifiers are NOT consumed
here — they belong to K1a.)

## 2. Closed input list (nothing else may enter)

1. **Interaction:** the registered dance energy function above, constants verbatim (AHC,
   α_s = 5/(8φ) [pre-existing upstream lineage, fence-noted], a_qq/a_ee/a_qe soft lengths,
   charge weights √α_s, √α).
2. **Species geometry:** qDP = qCP pair (+1, −1) at separation a_qq = 0.747 fm; eDP = eCP pair
   (+1, −1) at a_ee = 0.357 fm — rigid throughout (internal relaxation is dynamics and belongs to
   K1a; rigidity is DISCLOSED as the map's central approximation and carried in every reading).
3. **Grids (carried forward frozen from the 2564 declarations, which were never consumed by
   production):** E_rel ∈ {0.5, 1, 2, 5, 10, 15, 20, 50, 100} MeV (epoch band interior as ambient
   context only); b ∈ {0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0} × a_qq; approach axis z, initial
   separation beyond all interaction scales.
4. **Orientation classes (declared now, uniform enumeration, no weighting invented):** internal
   axes (â_A, â_B) ∈ {(x̂, x̂), (x̂, ŷ), (x̂, ẑ), (ẑ, ẑ), (ẑ, x̂)} — the five distinct classes of
   the two-axes-vs-approach-axis geometry under the system's symmetries — each with the two
   relative charge parities (aligned / anti-aligned). Results reported PER CLASS; no
   class-averaged "effective" depth may be constructed (that is phase-space weighting = kinetics).
5. **Standing pre-commitments:** the charter §2 hazard inventory where applicable (thresholds
   frozen pre-run; exploratory scans full-landscape-reported); trap clause; √5 fence; chaotic
   floor ±2 MeV applied to well depths as a resolution statement; no rate assembly; EXCLUDED
   named: the FORM-L window/wall, the E_close pin, kT·L, 16, abundance content.

## 3. The accessible-well conventions (the union; frozen)

The partial-accessibility rule (charter §1) forbids using the full equilibrium well depth where
geometry restricts access. Two defensible statics-side conventions exist; BOTH are computed and
the DEAD criterion takes their union:

- **W-1 (line-of-flight well):** for each (b, class, parity), the minimum of E_cross along the
  undeflected straight-line approach at impact parameter b — the well an unbent trajectory
  actually samples. The conservative convention (deflection can only deepen access).
- **W-2 (closest-approach relaxed well):** the minimum of E_cross over rigid configurations with
  center separation ≥ b — allowing orientation relaxation at closest approach but no penetration
  below b. The generous convention (bounds what any deflected-but-rigid encounter could reach).

W-1 ≥ W-2 in depth-magnitude ordering is expected structurally (W-2 minimizes over a superset);
the script ASSERTS it as a coherence check.

## 4. The DEAD criterion (frozen)

A cell (E_rel, b, class, parity) is **DEAD** iff E_rel > |W-2(b, class, parity)| + floor — i.e.,
the relative energy exceeds even the GENEROUS convention's accessible depth by more than the
resolution floor. (Using W-2 for death is deliberate: a falsifier-grade negative must survive the
most generous defensible reading.) A cell is **ACCESSIBLE** iff E_rel < |W-1| − floor under the
conservative convention. Cells between the two conventions' verdicts are **MARGINAL** — reported
as such, never resolved by choosing a convention (choice-by-outcome = Branch T). Repulsive-only
cells (W ≥ 0 under both conventions) are DEAD at all E_rel and flagged structurally.

## 5. Routes (order LOCKED) and readings (frozen)

- **R-A — qDP+qDP map** (9 E × 7 b × 5 classes × 2 parities × 2 conventions). Freeze.
- **R-B — qDP+eDP map** (same structure). Freeze.
- **R-C — consolidation:** DEAD/ACCESSIBLE/MARGINAL census per channel; the epoch-band interior
  rows STATED (ambient context, not a success criterion — charter fence); handoff table for K1a
  (which cells O1a production should skip).

Readings: **maps frozen** → banked as the K1a triage input; the DEAD exclusion applies to O1a
production ONLY where DEAD is unanimous across conventions and parities within a class (the §4
union built this in). **All-DEAD at every epoch-band row** → adverse-direction for the channel,
recorded as-is (reportable per charter pre-commitment; no repair). **All-ACCESSIBLE** → the map
is uninformative for triage and says so plainly; O1a runs the full grid. Rigidity disclosure
travels with every use: a DEAD verdict could in principle be overturned by internal-deformation
channels; that possibility is named once here and belongs to K1a/K1b evidence, not to relaxing
this map. Any new √5 → fence. No composition reading under any outcome.

## 6. Bookkeeping

79.5% untouched. Queue unchanged: O3′ execution (next patch) → K1a prereg → K1b R-A prereg;
REACH-AUDIT-2 alongside. Next patch: the O3′ execution, under this document only.
