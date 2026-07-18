# OPEN-DM-ENDBOND-1 pre-registration: pinning the stacking-bond depth by dedicated statics — definitions, closed input list, fenced gates, routes, and readings, committed before any derivation

**Patch 2544, 18 July 2026. Status: OPEN-DM-ENDBOND-1 REGISTERED and OPENED at pre-registration; NO
derivation performed.** Collision check clean. **Lineage: registered as the next target at founder
ratification (2542 §4(e) recommendation adopted). Inherits the 2529/2537/2541 discipline apparatus.
Verify: none needed at prereg (no structural computation here beyond what 2541/2542 already banked).**

## 0. Target and payoff

**Target:** E_endbond — the depth of the 4qCP-core-to-4qCP-core inter-plane stacking bond (alternating
parity, pitch D = 1.15 fm), by a dedicated statics computation from registered-lineage interaction
content. By the 2540 founder identity this is simultaneously the rod's inter-plane bond and the ring's
closure bond. **Payoff:** it is the widest band in every 2542 result ([40, 170] MeV); pinning it
collapses, downstream: the ΔE_close band, the survival margin, and (via nothing else) sharpens no
comparator — the kT_form band's width is comparator/convention-dominated and would NOT collapse; this
is stated now so a pinned E_endbond is not oversold.

## 1. Definitions fixed

E_endbond ≡ E(two planes, separated to non-interaction) − E(two planes at the registered stack
geometry), evaluated under the registered interaction lineage restricted per §2 — positive = bound.
The computation is a statics lattice sum over the registered pair geometry (16 CPs); no dynamics, no
rates, no thermal content.

## 2. Closed input list (nothing else may enter)

1. **Geometry:** Candidate-B element-plane (4 qCP square, edge a_q = 1.15 fm; 4 eCP diagonals,
   R_e = 1.301 fm; sequence eCP–qCP–qCP–eCP); stack pitch D = 1.15 fm; alternating parity (90°
   offset, 2540 identity).
2. **Interaction lineage (the walk):** the registered pairwise functional artifacts — the 2450
   switched-pair electric functional (couplings, δ = 3/7 duty factor, weights) and the 2455
   strong-sector contact registrations (α_s = 5/(8φ); a_qq = ℏc/264 = 0.747 fm saturation;
   a_ee = 0.357 fm; a_qe = 0.516 fm; contact depth α_s·ℏc/a_qq = 102 MeV as a REGISTERED DERIVED
   quantity). **The compute patch's mandatory first act is the functional walk:** establish, from
   these artifacts and their reasoning files ONLY, (i) which cross-plane pairs are strong-coupled,
   (ii) the registered radial form and its saturation/cutoff at contact, (iii) sign structure under
   alternating parity. If the artifacts under-determine any of (i)–(iii), that limb is **Branch I
   with "strong-sector pairwise form" as the named blocker** — NOT license to invent a form, choose a
   regularization, or import one from outside the lineage.
3. **Standing pre-commitments:** 2521; the 2529 §6 Branch-T triggers verbatim; the √5 fence (φ in
   α_s is pre-existing upstream lineage — same note as 2542; any NEW √5 → fence procedure).
4. **EXCLUDED and FENCED, named:** the E_qq map band [40, 170] MeV; the 102 MeV contact lock; the
   dance ring−straight −68.8 MeV echo and its back-implied ≈85 MeV. All four are POST-FREEZE GATES
   (§3), not inputs. Any truncation, cutoff, pair-selection, or convention chosen because it moves
   the result toward a gate = Branch T. Where the lineage admits multiple defensible conventions,
   the 2541 §3 union rule applies verbatim: compute all, report the union with spread disclosed.

## 3. Gates (frozen; compared only after the result is frozen)

G1: membership in [40, 170] MeV (the registered map). G2: proximity to the 102 MeV contact lock.
G3: proximity to the ≈85 MeV dance back-implication (echo-class; the weakest gate — consistency
pleasant, inconsistency non-fatal, since the dance functional differs). Order of disclosure fixed:
result first, then G1, G2, G3 in that order, one sentence each.

## 4. Routes (order LOCKED)

- **R-A — the functional walk, then the direct lattice sum** (16-CP pair geometry, registered forms,
  union over defensible conventions). Freeze the depth (a value or a band). Then §3 gates.
- **R-B — decomposition report (after freeze):** core–core vs coat and cross contributions, reported
  for physical insight; no reading rides on the decomposition.

## 5. Readings (frozen)

- **Depth frozen, G1 passes** → E_endbond PINNED at statics strength with its convention band; a
  downstream revision patch propagates it through the 2542 results (ΔE_close and survival margins
  collapse; kT_form band explicitly NOT collapsed — comparator-dominated, per §0). Win-class only if
  G1+G2 both pass with the union band materially inside the map band; otherwise a banked pin.
- **Depth frozen, G1 fails** → TENSION recorded as-is between the dedicated statics and the E_qq map
  lineage; no repair in-campaign; the tension becomes the named next problem.
- **Functional walk under-determined** → Branch I, named blocker "strong-sector pairwise form";
  partials (electric-sector contribution, geometry sums) bank.
- **No composition reading; no T_form re-derivation here** (RODCLOSE-1 owns those); any √5 → fence.

## 6. Bookkeeping

79.5% untouched. Queue position: OPEN-DM-ENDBOND-1 R-A is the next compute; the RODCLOSE-1 kinetic
limb (NB-S3a-1) and the plane-resident-fraction limb remain behind it; δ_E and MW-MODES TC-extension
behind those. Next patch: the ENDBOND-1 functional walk, under this document only.
