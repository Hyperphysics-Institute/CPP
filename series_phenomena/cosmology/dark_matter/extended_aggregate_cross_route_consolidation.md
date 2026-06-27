# Extended-Aggregate Dark-Matter Candidate — Goalpost Campaign Status (the 4-wide cross route)

**Version:** v1.0 (consolidation memo) · **Patch:** 0871 · **Lane:** DM-local (08xx)
**Work item:** DM-1 extended-aggregate pivot · **Conjecture served:** CONJ-COSMO-1
**Proposed ID (RESERVED, not registered here):** `LEMMA-DM-CROSS-ROUTE-1` — registration pending Thomas sign-off + panel pass
**Status of result:** Layer C (bracketed / physical-reasoning), **one goalpost now brackets FAVORABLY**; see §8 grading.
**Consolidates:** patches 0865 (G2), 0866 (G3), 0867 + 0869 (G1-strand), 0868 (d_f/morphology), 0870 (G1-cross), and the corona-closure dialogue (§7, uncomputed).
**Does NOT do:** edit `DM-1_substrate_dark_matter_candidate.tex` (held at v0.1); register any ID; add any axiom; change any prior verdict. DM-1 stays v0.1.

---

## 1. Purpose and scope

The DM-1 paper proposes that dark matter is **neutral, extended aggregates** of the CPP substrate
(charge-offset qDP/hTetra structures). The pivot to *extended* objects (away from point qDP/hTetra,
whose self-interaction is too weak — see §2) raised a chain of make-or-break questions ("goalposts").
This memo states, in one citeable place, **where each goalpost now stands**, so the next DM-1 revision
and the AI review panel can reference one synthesis rather than re-litigating six patches.

The headline change since the last consolidation (1200, the point-particle survival memo): the
**4-wide cross** has emerged as a morphology whose stiffness brackets *favorably* — the first goalpost
in this campaign that is not a kill-risk — and a physical-reasoning argument (§7) closes the one
remaining dilution risk on it. That corona-closure argument is **uncomputed** and is the principal
thing this memo asks the panel to attack.

## 2. The σ/m problem and the one number that governs every morphology

The dwarf-core (SIDM) preference window is **σ/m ≈ 0.6–2 cm²/g** at dwarf velocities, while remaining
collisionless at cluster scale (σ/m ≲ 1 cm²/g there; velocity-dependence of extended scatterers
supplies the split). The corrected point-scattering value is **σ/m ≈ 0.11 cm²/g** — a *floor* that is
~5–20× below the window. Extended objects must lift σ/m off that floor.

For an extended scatterer of N constituents, gyration radius R_g, monomer size a, fractal dimension d_f:

> σ ∝ R_g², m ∝ N, N ∝ (R_g/a)^d_f ⟹ **(σ/m)_agg / (σ/m)_monomer = (R_g/a)^(2 − d_f).**

- **d_f < 2** → σ/m **grows** with size → reaches the band. **WORKS.**
- **d_f = 2** → σ/m flat at the floor. **Dilution threshold.**
- **d_f > 2** → σ/m **falls** below the floor. **DILUTES → candidate dies.**

Every morphology question below reduces to: *does this object present d_f < 2 (or, equivalently, stay
extended rather than compact) at a size that reaches the band?*

## 3. The morphologies and the goalposts

Three candidate morphologies compete for the same hTetra pool, terminated by depletion:
**(i) single strand / loop**, **(ii) the 4-wide cross / ribbon**, **(iii) amorphous branched ball.**
The goalposts that gate them:

- **G2 — edge-bond depth.** Are the ee/qq edge bonds deep enough to be stable over cosmological time
  yet shallow enough to fragment into the right size distribution? (depth window + lifetime floor)
- **G3 — glueball dilution.** Is the unwanted qDP-center glueballing suppressed enough not to collapse
  the aggregates? (concentration/chaperone suppression)
- **G1 — bend stiffness.** Is the structure stiff enough to form/stay an extended object of band size
  (persistence length vs object length), with the straight/extended config stable (no buckling)?

## 4. Goalpost status — summary table

| Goalpost / morphology | Patch(es) | Status | One-line reason |
|---|---|---|---|
| **G2** edge-bond depth | 0865 | **Bracketed-reachable** | fm-scale Coulomb ceiling (1.44 MeV) sits at the top of the fragmentation window [0.8 keV, 2 MeV]; in-window for natural screening residual |
| **G3** glueball dilution | 0866 | **Robust (over-determined)** | suppression ρ = C·S over-determined by the Sea-vs-relic concentration hierarchy C; robust to the bracketed geometry factor S |
| **G1 — single strand/loop** | 0867, 0869 | **KILLED (two kill-conditions)** | symmetric vertex family BUCKLES; alternating family docks at a robustly-large angle (~18°) → loops ~20 rungs, ~15× too small |
| **morphology / d_f** | 0868 | **Channel-dependent** | monomer-fed ball d_f ≈ 2.5 (dilutes); only cluster-cluster coalescence of *extended* sub-units reaches d_f < 2 |
| **G1 — 4-wide cross** | 0870 | **FAVORABLE (brackets good)** | bend stiffness is a BEAM property (bond-stretch × width²), over-determined by the same G2/0865 depth; sign-safe |
| **cross corona** | §7 (uncomputed) | **Closed by reasoning** | the eDP coat is bulk-Sea thermal texture, not bound mass → no σ/m-diluting accumulation |

## 5. The single strand is retired (0867, 0869)

The single hTetra strand's bend stiffness is the second derivative of a sub-Planck **near-cancellation**
in the bend coordinate — no external ceiling. Two sign-families exhaust the 2+,2− folded-vertex apposition:

- **Symmetric (++ ‖ −−):** the straight config is an energy *maximum* (k₀ < 0) → **BUCKLES** (symmetric
  double-well) for all but the largest gaps. (0867's kill-risk, confirmed in 0869.)
- **Alternating (+/− ‖ +/−):** a finite *preferred* fold angle (no hard buckling — softer), but the angle
  is a **geometric docking angle, robustly ~18° (worse, to ~50°, in the wide limit), not moved below ~17°
  by any charge magnitude or lever.** A loop closes at N₀ = 360°/θ₀ → **~20 rungs, ~15× too small** for the
  300–2500 band, and resists tuning into it.

**Conclusion:** the strand-that-loops is not the candidate. Both families miss a band-sized loop. This is
a genuine negative result, recorded as two kill-conditions, not a parameter to be tuned.

## 6. The 4-wide cross brackets favorably (0870) — the structural win

The cross is stiff for a **structurally different reason** than the strand, which is why it sidesteps the
strand's near-cancellation entirely:

> Bending a cross-bonded bundle forces the **outer strands to STRETCH and inner to COMPRESS** (beam
> bending). The restoring energy is the **axial bond-stretch stiffness κ_ax ~ E_bond** (the robust, large
> G2/0865 depth) times the **width²** — NOT the near-cancelled hinge angular residual.
>
> **ℓ_p(rungs) = c_geom · (E_bond/kT)**, with c_geom ≈ 2 (the "+" cross, isotropic) to 5 (flat ribbon, in-plane).

Key consequences (all in 0870):

- **Over-determined by the same depth the lifetime needs.** The 0865 lifetime-floor bracket E_bond/kT ≳ 100
  supplies ℓ_p ≈ 200–500 rungs, covering/approaching the 300–2500 band (the "+" cross needs E_bond/kT ≳ 150
  — a hair above the floor — to clear 300). No separate fine-tuning.
- **Geometry confirms "cross", not "ribbon".** A flat 4-ribbon is stiff in-plane (Σdy²=5) but has *zero*
  out-of-plane stiffness (Σdz²=0) → it coils. The "+" cross is isotropically stiff (Σ≈2 both axes). The 2D
  cross-section is load-bearing.
- **Sign-safe.** The beam stiffness overwhelms any residual hinge buckling by 1–50× (for |κ_hinge| ≲ 0.5 E_bond),
  so the cross is stable **even if the bare strand hinge buckles**.
- **σ/m.** A stiff/semiflexible cross is an extended scatterer (L ≤ ℓ_p → rigid rod, d_f = 1, σ/m ∝ L;
  L > ℓ_p → semiflexible, d_f ~ 1–1.5, σ/m still grows). And it is the **extended sub-unit** whose
  cluster-cluster coalescence gives the d_f < 2 ball (0868) — so the cross unifies both routes.

## 7. The corona closure — load-bearing and UNCOMPUTED (the panel's main target)

The one residual risk on the cross: the qe-branching that builds the amorphous mass could decorate the
spine with a proliferating corona, burying the clean rod and pushing it toward the diluting d_f ≈ 2.5 blob
(0868). Three independent arguments close this — **all by physical reasoning, none computed**:

1. **No sheet (geometry).** The cross's 4-fold transverse symmetry sends side-branches into four different
   transverse directions; they populate 3D around the axis and cannot flatten into a 2D sheet. (Kills the
   sheet → d_f = 2 mode.)
2. **No proliferation driver (thermodynamics/availability).** The spine presents a *promiscuous* ee-edge
   with no strong preference among ee/qq/qe/eq; there is no energetic driver recruiting hTetras onto it.
   The corona is therefore not a runaway branching cascade but an availability-limited coating — starved by
   the same low Sea-vs-relic hTetra concentration that over-determined G3 (0866).
3. **No accumulation (the coat is bulk Sea, not bound mass).** The eDP "buffy coat" around the cross is the
   *same transient interbonding* that fills the entire DP Sea — eDPs forming momentary chains/aggregates in
   collision-free gaps, then randomizing and dispersing. The kT energetics at the coat are identical to
   un-nucleated space; the coat transitions to bulk-Sea pattern statistics within a thin shell. There is no
   binding-energy minimum, hence **no reservoir for slow Gyr-scale deposition** — the coat cannot pile up as
   σ/m-diluting dead weight, because it is at the same chemical potential as the bulk on both sides.

**Why this is the right *kind* of argument:** it is *structural*, like the 0870 beam-stiffness result —
the spine stays clean not by a lucky number but because the corona is bulk-Sea texture, not deposited mass.
The denominator of σ/m stays the spine; **σ/m ∝ L survives.**

**Why it is flagged, not asserted:** every link in §7 is physical reasoning, not a computed result. The
three are individually plausible and mutually consistent, which is why we trust the picture — but the
campaign's discipline grades such chains Layer C and lets the panel try to break them. **This is the claim
the panel is explicitly asked to attack** (§10, Q1).

## 8. Honest epistemic grading

| Claim | Grade | Provenance |
|---|---|---|
| σ/m = (R_g/a)^(2−d_f) scaling; d_f = 2 dilution threshold | **Computed/derived** | 0868 (estimator validated: line→1.0, disk→2.0, cube→2.8) |
| Strand symmetric-family buckling; alternating docking ~18° not tunable | **Computed** | 0867, 0869 (parameter scans) |
| Cross ℓ_p = c_geom·(E_bond/kT); over-determined by 0865; sign-safe | **Computed + bracketed** | 0870 (beam model; E_bond/kT bracket from 0865) |
| Monomer-fed ball d_f ≈ 2.5 (dilutes) | **Computed** | 0868 (validated estimator) |
| Cluster-cluster of extended sub-units → d_f < 2 | **Cited, not in-house** | 0868 (DLCA ≈ 1.8 from aggregation physics; in-house CCA toy did NOT converge) |
| G2 depth in-window; G3 suppression over-determined | **Bracketed** | 0865, 0866 |
| **Corona closure (§7): clean spine, σ/m ∝ L survives** | **Physical-reasoning, UNCOMPUTED** | §7 dialogue — **load-bearing; panel target** |

## 9. What remains open (SF / kinetics — not blocking this memo)

- **The corona closure (§7) wants a computed backstop** *or* a panel ratification. It is currently the load-
  bearing uncomputed link between "clean spine" and the 0868 dilution floor.
- **The actual σ/m number for the clean spine** (semiflexible cross as a rod, corona entered as bulk-Sea
  zero-net-mass) against 0.6–2 cm²/g — a scaling argument exists (§6), a hard figure does not yet.
- **The cross-bond coupling strength** (assumed present = the cross definition; at long wavelength any
  nonzero coupling gives the rigid-beam ℓ_p), the realized **width** (sets c_geom), and the precise
  **E_bond/kT** (sets whether the "+" cross clears 300 at the floor or needs ~1.5× it).
- **Glueball growth kinetics (OPEN-SS-39)** — parked per the kinetic argument that a 4-wide ribbon does not
  overlap/glueball its qDP center often enough to grow large glueballs; qualitative, not computed.

## 10. What the panel is asked to do

Attack the chain in priority order:

- **Q1 (load-bearing).** §7 corona closure: is "the eDP coat is bulk-Sea thermal texture, not bound mass,
  so it cannot accumulate as σ/m-diluting dead weight" sound? Specifically — is there *any* mechanism
  (screened residual binding, kinetic trapping, slow Gyr deposition) by which a corona could thicken on the
  cross despite being at bulk-Sea chemical potential? If yes, the clean-spine result fails and the cross
  reverts to a dilution risk.
- **Q2.** §6 beam-stiffness over-determination: is ℓ_p = c_geom·(E_bond/kT) the right long-wavelength
  persistence length for a cross-bonded bundle, and is c_geom ≈ 2 (isotropic "+" cross) defensible? Is the
  sign-safety margin (beam ≫ residual hinge) correctly argued?
- **Q3.** §5 strand retirement: are the two kill-conditions (symmetric buckling; alternating docking angle
  robustly ~18°, untunable) correct, or is there a vertex arrangement/geometry that recovers a band-sized loop?
- **Q4.** §2/§8: is the d_f < 2 vs d_f ≥ 2 dilution dichotomy the correct governing criterion, and is the
  reliance on the cited DLCA (≈1.8) for the cluster-cluster leg acceptable given the in-house CCA did not
  converge?

**Verdict requested:** for each Q, CONFIRM / RESTATE-with-fix / KILL, with the specific physical mechanism
if KILL. The cross route stands or falls primarily on Q1.

---

*Layer C consolidation. No DM-1 `.tex` edit, no registration, no axiom, no verdict change. DM-1 stays v0.1.*
