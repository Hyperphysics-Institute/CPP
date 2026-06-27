# Extended-Aggregate Dark-Matter Candidate — Goalpost Campaign Status (the 4-wide cross route)

**Version:** v3 (consolidation memo; integer-per-revision — rev1 = old v1.0/0871, rev2 = old v1.1/0872, **rev3 = this/0873**) · **Lane:** DM-local (08xx)
**Work item:** DM-1 extended-aggregate pivot · **Conjecture served:** CONJ-COSMO-1
**Proposed ID (RESERVED, NOT registered — corona not yet closed):** `LEMMA-DM-CROSS-ROUTE-1` — registration withheld pending V_surf/kT ≲ 0.5 + Thomas sign-off
**Status of result:** Layer C. Cross route **VIABLE but NOT CLOSED**: beam stiffness confirmed favorable (panel 4/4 on Q2); the corona now reduces to **one SF number — V_surf/kT ≲ 0.5** (fork-(a) excavation, §7/§11: the density gives no margin).
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
in this campaign that is not a kill-risk (panel-confirmed 4/4, §11) — while the one remaining dilution risk
on it, the spine corona, has been examined by the panel and **downgraded from a claimed closure to an
explicit conditional bound** (§7, patch 0872). The route is therefore **viable but not closed**: it now
rests on two SF/substrate numbers (V_surf/kT and ρ_Sea/ρ_spine), and the reserved lemma stays unregistered
until those close the corona favorably.

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
| **cross corona** | §7, 0872–0873 | **Reduced to ONE SF number** | σ/m-safe iff the residual eDP→spine surface well V_surf/kT ≲ 0.5; density gives no margin (fork-(a)); plausible but SF-pending; NOT closed |

## 5. The single strand is retired (0867, 0869)

The single hTetra strand's bend stiffness is the second derivative of a sub-Planck **near-cancellation**
in the bend coordinate — no external ceiling. Two sign-families exhaust the 2+,2− folded-vertex apposition:

- **Symmetric (++ ‖ −−):** the straight config is an energy *maximum* (k₀ < 0) → **BUCKLES** (symmetric
  double-well) for all but the largest gaps. (0867's kill-risk, confirmed in 0869.)
- **Alternating (+/− ‖ +/−):** a finite *preferred* fold angle (no hard buckling — softer), but the angle
  is a **geometric docking angle, robustly ~18° (worse, to ~50°, in the wide limit), not moved below ~17°
  by any charge magnitude or lever.** A loop closes at N₀ = 360°/θ₀ → **~20 rungs, ~15× too small** for the
  300–2500 band, and resists tuning into it.

**Conclusion (scope per panel Q3):** the **currently-defined 2+,2− strand morphology** is killed — both
families miss a band-sized loop, and recovering one would require a *qualitatively different vertex design*
(a different fold-angle family), **not** a parameter tweak of charge magnitude or lever. Recorded as two
kill-conditions. (We do not claim every conceivable strand-like topology is excluded — only that the
modeled family, and any continuous deformation of it, is dead.)

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

## 7. The corona — BOUNDED and CONDITIONAL (Q1; panel RESTATE-with-fix incorporated, patch 0872)

The risk: the qe-branching that builds the amorphous mass could decorate the spine with a corona,
burying the clean rod toward the diluting d_f ≈ 2.5 blob (0868). The v1.0 memo argued this was *closed*
because the eDP coat is bulk-Sea thermal texture at the same chemical potential as the bulk. **The panel
(3/4: ChatGPT, Gemini, Copilot) correctly judged that overreach:** equal bulk chemical potential rules out
*unlimited* deposition, but NOT a finite surface excess or a kinetically trapped layer, unless the spine's
residual *surface* potential well **V_surf** is actually bounded. "Promiscuous ee-edge, no deep specific
bond" is not "zero attractive well." Patch 0872 makes the bound explicit. The coat dilutes σ/m only via:

- **Channel 1 — kinetic trapping** (the "slow Gyr deposition" worry). A coat eDP escapes by thermal
  activation, τ_res = τ_0·exp(V_surf/kT); it is diluting dead mass only if τ_res ≳ t_halo. Threshold
  (V_surf/kT)\*_trap = ln(t_halo/τ_0) = **60–93** for any plausible τ_0 ∈ [10⁻²³,10⁻¹⁰] s. With the 0865
  floor E_bond/kT ≳ 100, trapping requires **V_surf ≳ 0.6–0.9 E_bond** — i.e. a bare ambient eDP would
  have to bind to the spine at 60–90% of a *full hTetra bond depth*. Robustly bounded; the promiscuous edge
  argues V_surf ≪ E_bond, so this channel is plausibly safe — now as an explicit bound, not an assertion.
- **Channel 2 — equilibrium surface excess** (the "wetting layer" worry). m_coat/m_spine =
  G·(⟨e^(V_surf/kT)⟩−1), with G ~ (ρ_Sea/ρ_spine)·(perimeter·λ_D/A_spine). Orientation cancellation on the
  promiscuous edge makes the bracket **second-order**, ⟨e^(V/kT)⟩ → cosh(V/kT) ≈ 1 + (1/2)(V/kT)², so the
  excess is suppressed; but the prefactor **G is SF/substrate-pending** (needs ρ_Sea/ρ_spine and λ_D). Safe
  for G ≲ 0.4 (ρ_Sea/ρ_spine ≲ 0.1) and V_surf/kT ≲ 1; larger ρ_Sea/ρ_spine is the failure corner.

**Honest status (the fix delivered):** §7 is downgraded from "closed by reasoning" to an **explicit
conditional bound** — the clean-spine result HOLDS iff **(1)** V_surf/kT ≲ 60–90 (no Gyr trapping; robust,
computed) AND **(2)** G·(cosh(V_surf/kT)−1) ≪ 1 (thin equilibrium excess).

**Fork-(a) update (rev3, patch 0873) — the density gives NO margin, so the corona reduces to ONE number.**
The natural hope was that the prefactor G ~ (ρ_Sea/ρ_spine)·(perimeter·λ_D/A_spine) is ≪ 1 (closing channel
(2) in-house). Excavation of the qDP relic/abundance corpus says otherwise: there is **no** local
ρ_Sea/ρ_spine bracketed; the cosmic Sea-vs-relic hierarchy (0866's C ≫ 1) is a **global species-count**
ratio and does **not** apply to the **local** coat (locally the ambient Sea and the spine are both
substrate close-packing → ρ_Sea/ρ_spine ~ **O(1)**). So **G ~ 1.6–6** — no suppression. Channel (2) then
needs a **shallow** well, V_surf/kT ≲ 0.5 (G=1) to ≲ 0.3 (G=3) — far tighter than the trapping threshold.
**Both channels collapse to a single SF number:** the corona is σ/m-safe **iff V_surf/kT ≲ 0.5** (the
equilibrium-excess channel binds; trapping is slack). Plausible — V_surf is the residual, Sea-screened,
orientation-averaged well of a promiscuous, charge-cancelled ee-edge to a *bare* eDP (≲ ~10 keV clears it,
below the bond window) — but **SF-pending**, and now the cross route's sole remaining load-bearing item. The
three v1.0 physical arguments survive as the *reasons* a sub-thermal V_surf is plausible; the route is **not
closed** until the SF residual-charge-geometry calculation returns V_surf/kT ≲ 0.5.

## 8. Honest epistemic grading

| Claim | Grade | Provenance |
|---|---|---|
| σ/m = (R_g/a)^(2−d_f) scaling; d_f = 2 dilution threshold | **Computed/derived** | 0868 (estimator validated: line→1.0, disk→2.0, cube→2.8) |
| Strand symmetric-family buckling; alternating docking ~18° not tunable | **Computed** | 0867, 0869 (parameter scans) |
| Cross ℓ_p = c_geom·(E_bond/kT); over-determined by 0865; sign-safe | **Computed + bracketed** | 0870 (beam model; c_geom from the cross-section second moment — presented as a bracket per panel Q2; assumes no soft inter-strand shear/slip mode) |
| Monomer-fed ball d_f ≈ 2.5 (dilutes) | **Computed** | 0868 (validated estimator) |
| Cluster-cluster of extended sub-units → d_f < 2 | **Cited external anchor, NOT in-house** | 0868 (DLCA ≈ 1.8 aggregation physics; in-house CCA toy did NOT converge; cluster-cluster leg is model-dependent — panel Q4) |
| G2 depth in-window; G3 suppression over-determined | **Bracketed** | 0865, 0866 |
| **Corona (§7): clean spine holds iff V_surf/kT ≲ 0.5** | **One explicit SF number, pending** | 0872 + 0873 — kinetic-trapping threshold computed (~60–90, slack); density prefactor G ~ O(1)–few (no margin; fork-(a) excavation), so the equilibrium-excess channel binds at V_surf/kT ≲ 0.5; **NOT closed** until the SF residual-charge-geometry returns V_surf |

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

---

## 11. Panel returns (v1.0 → v1.1)

The v1.0 memo was reviewed by the four-model panel (ChatGPT, Grok, Copilot, Gemini). Verdicts on the §10
questions, and the fixes folded into v1.1:

| Q | Topic | ChatGPT | Grok | Copilot | Gemini | Net | Fix applied in v1.1 |
|---|---|---|---|---|---|---|---|
| **Q1** | Corona closure (load-bearing) | RESTATE | CONFIRM | RESTATE | RESTATE | **RESTATE-with-fix (3/4)** | §7 rewritten as an explicit conditional bound (patch 0872): kinetic-trapping threshold computed (~60–90 kT); equilibrium-excess prefactor SF-pending. **Not closed.** |
| **Q2** | Beam stiffness | CONFIRM | CONFIRM | CONFIRM | CONFIRM | **CONFIRM (4/4)** | c_geom now stated as a bracket; soft inter-strand shear/slip mode flagged as a check (§8). |
| **Q3** | Strand retirement | CONFIRM | CONFIRM | RESTATE | CONFIRM | **CONFIRM (3/4)** | §5 scope narrowed to "the currently-defined 2+,2− morphology and its continuous deformations," not all conceivable topologies. |
| **Q4** | d_f / DLCA | CONFIRM | CONFIRM | CONFIRM | CONFIRM | **CONFIRM (4/4)** | §8 labels DLCA an external anchor and the cluster-cluster leg model-dependent. |

**Net status after v1.1:** the cross route is **viable but not closed**. Q2–Q4 are confirmed (with minor
scope/labeling fixes already applied). Q1 — the load-bearing corona — is **bounded and conditional**, not
closed: it now rests on two explicit SF/substrate numbers (V_surf/kT and ρ_Sea/ρ_spine, §7). The reserved
lemma stays **unregistered** until Q1 closes favorably.

**rev3 update (fork (a), patch 0873):** the second of those two numbers, ρ_Sea/ρ_spine, was excavated from
the qDP relic/abundance corpus and found to give **no safety margin** — there is no favorable local ratio
bracketed, and the cosmic Sea-vs-relic hierarchy (global species count) does not apply to the local coat
(locally both are substrate close-packing, ρ_Sea/ρ_spine ~ O(1), prefactor G ~ 1.6–6). Consequence: the
corona collapses to a **single** SF number — σ/m-safe **iff V_surf/kT ≲ 0.5** (equilibrium-excess channel
binding; trapping slack). Fork (a) did not retire half the risk; it **localized the entire corona risk to
one sharply-posed SF residual-charge-geometry calculation**. That calculation (V_surf, the promiscuous
charge-cancelled screened ee-edge well to a bare eDP, vs kT) is the cross route's sole remaining load-bearing
item, and the next step requires the SF-2/SF-5 charge geometry (the one DM-local-insufficient input).
