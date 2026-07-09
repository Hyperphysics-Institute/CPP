# The S(N) arc — opening cost estimate (Patch 2370, 9 July 2026)

**Authority:** founder "proceed as recommended" on the 2369 pivot. **This patch
estimates; it does not derive.** Per the discipline: substrate theory gets an
honest cost map before investment, with the cheap kills ordered first.

## What OPEN-SS-43 actually demands (two coupled quantities)
1. **R_s(N)** — the DM-core sea-screening length (the registered make-or-break,
   `OPEN-SS-43_Rs_derivation.md`; partially worked in the DM-1 v1.2 era).
2. **S(N)** — the coupling-vs-N law the 2344/2349 machinery parameterized and
   never derived. The 2344 near-pass carried S(N) ~ N¹² as a "named strain,
   formally admissible under OPEN-SS-43"; G1's central-frame passes demanded
   p ≥ 13; the extended-frame natural pass demanded none (p_min = 0). The rent:
   derive S(N) from substrate structure, then see what populations the true
   kinetics realize.

## The structural fact that shapes everything
The registered passing regions are TWO-SPECIES objects (2344): a **dimer at
0.94–0.99 mass fraction supplying the steep dSph channel**, plus a **trace
N≈5 strongly-coupled species whose cross channel carries LSB**. The 2369 kill
removed the dimer. Therefore the wide door is only wide if **some N≥3 species
can carry the dSph channel instead** — and that is an empirical question about
the anchor suite, answerable CHEAPLY with existing machinery, BEFORE any
derivation is attempted. Deriving a beautiful S(N) that suppresses N=2 is
worthless if no dimer-free mixture passes the suite at any audited frame.

## Machinery inventory (all clean-clone-verified lanes)
- `code/2344_polydisperse_closure.py` — the mixture scanner (~800k configs,
  anneal + corner strata). Parameter-level to re-floor at N_min = 3.
- `code/1855_kinetic_aggregation_Nform_scan.py` + `code/2349_g1_engine.py` /
  `2349_g1_audits.py` — the formation-kinetics realizer and the G1 grader.
- `code/1879_xqc_recomputation.py` — G-XQC-0, parameter-level in (N, M),
  demonstrated cheap (2366).
- `code/0861_formation_kinetics_loop_distribution.py`, `0881_freezeout_kinetics_Ndwarf.py`
  — the loop-era equilibrium-polymerization + freezeout machinery: the
  substrate-side S(N) starting point IF Q3 is ever reached. Note its own
  physics: ring-closure statistics SUPPRESS small N (bending cost) — a
  qualitative hint that a derived distribution may not populate N=2, which
  would be convenient; convenience is precisely why it must be derived, not
  assumed.

## The plan, cheap-kill-first (costed)

**Q1 — the dimer-free rescan (cheap: one session).** Rerun the 2344 scanner
with N_min = 3, frames and windows FIXED per the attested Clause 1 (the
audited frames as ratified; no softening; the registered-frame kill untouched).
Pre-registered outcomes: (a) **no N≥3 mixture passes** → the wide door closes
at the current anchor demands; the arc escalates honestly (large-N-only
families per the 0860/0861 band, or the missing physics is not a population at
all); (b) **passes exist** → their (N-composition, S(N) steepness, α-cost)
become the concrete derivation target for Q3.

**Q2 — G-XQC-0 on Q1 survivors (cheap: one session).** Every surviving species
(trimer ≈ 4.2 GeV, N=5 ≈ 7.0 GeV, ...) through the 1879 pipeline at its
required abundance, per-bin criterion, plus the Stage-1 ceiling map for the
underground question. Any family failing the gate dies BEFORE derivation
investment. If ALL small-N carriers are XQC-excluded at passing abundances,
the small-N population family dies wholesale and the search changes character.

**Q3 — the substrate derivation (expensive: weeks-scale; GATED on Q1+Q2
leaving a live target).** The 2eDP:2qDP rung-bond SSV potential (SF-2/SF-5
registered quantities) → E_bond + angular stiffness → nucleation pathway and
critical nucleus N_c → S(N) and the realized N-distribution → G1-style
regrade + G-XQC-0. Honest death modes, stated now: (i) the SSV well may not
be derivable from registered axioms without new assumptions — if so, the rent
cannot be paid and the arc says so rather than assuming; (ii) the derived
distribution may populate N=2 anyway (equilibrium polymerization generically
LOVES small N; only closure/nucleation barriers fight it) — in which case the
kill extends and the population idea dies at the substrate level; (iii) the
derived S(N) may cap below the steepness any Q1 survivor demands.

## Cost summary
| Stage | Cost | Kills cheaply if | Proceeds to |
|---|---|---|---|
| Q1 rescan (2371) | ~1 session | no dimer-free pass exists | Q2 |
| Q2 G-XQC-0 (2372) | ~1 session | all survivors XQC-excluded | Q3 |
| Q3 derivation | weeks, gated | SSV well underivable; N=2 populated anyway; steepness cap | G1 regrade + gate |

**Recommendation: execute Q1 as Patch 2371.** Its answer reshapes everything
downstream, it costs one session, and either outcome is progress: a target or
a closed door.

---

## Q1 EXECUTED — OUTCOME (b): DIMER-FREE PASSES EXIST (Patch 2371, 9 July 2026)

`code/2371_q1_dimerfree_rescan.py` + `2371_results.json`, verify 3/3 (machinery
equivalence to stored 2344 totals at 0 rel dev; N≥3 floor enforced across every
evaluated point; anneal seed-stability <5%). Pre-registered ranges and outcomes
per the script header; frames FIXED per the attested Clause 1.

| Frame | best violation | PASS | best composition |
|---|---|---|---|
| audited_extended | **1.0000** (already in wide scan) | **YES** | N=(4, 5), w=0.217, R_s=27.0 |
| audited_central | **1.0000** | **YES** | N=(3, 6), w=0.064, R_s=90.6 |
| registered | 1.0927 (anneal best) | no | — (coherent with the standing registered-frame kill) |

**The dSph channel CAN be carried without the dimer.** Small-N (3–6) two-species
mixtures pass the entire anchor suite elastically at both audited frames. The
successor family is live; masses in play: N=3 → 4.22 GeV, N=4 → 5.63, N=5 →
7.04, N=6 → 8.45 GeV, at mixture fractions where BOTH species are substantial.

**Honest limits of Q1 (carried into Q2's scope):** these are annealed POINTS,
not mapped regions; couplings are in the mixture machinery's units and need the
registered per-N bridge (E_rN = 3E_c/(8N) × island S_c) for the XQC gate;
naturalness costs (α, S(N) steepness) not yet graded — that is G1-machinery
work and belongs with Q3's target-setting if Q2 clears.

**Next: Q2 (2372) — G-XQC-0 on the survivors:** every species of both passing
compositions through the 1879 per-bin criterion at its required abundance
(heavier species: recoils shift into XQC's populated bins and number density
drops as 1/M — genuinely open both ways), plus the Stage-1 ceiling map. The
gate the dimer failed is the gate these must clear before any derivation
investment.

---

## Q2 EXECUTED — OUTCOME (b), CORRIDOR-CONDITIONED: THE SUCCESSORS CLEAR THE GATE ONLY AT THE ISLAND FLOOR (Patch 2372, 9 July 2026)

> **CORRECTION NOTICE (Patch 2374):** the composition verdicts in this section
> used a PER-SPECIES criterion (each species alone vs the full bin threshold —
> a convention inherited from the single-species 2366 run, where it was exact).
> For a mixture the observed spectrum is the SUM over species; under the
> corrected summed-spectrum criterion, TWO verdicts flip (extended at
> (S_c=0.012, ρ=0.3), both signs: SAFE → EXCLUDED); all EXCLUDED verdicts
> stand a fortiori. Text below retained as record; corrected grading in §Q3
> OPENED (2374). The 2369 kill and Q1 are unaffected.

`code/2372_q2_gxqc0_survivors.py` + `2372_results.json`, verify 3/3 (V-a: the
dimer regression anchor reproduces stored 2366b EXACTLY — viol=3, total
642.219, rel dev 0.0; V-b: bridge E_rN = 3E_c/(8N)·S_c asserted at every
evaluated point; V-c: 2368-class convergence at the N=6 hurting corner —
violated bins unchanged, totals ≤1.1e-4 rel under h/r_max/l_max variations).
Conventions pre-stated: the XQC-side mediator range stays the REGISTERED
R_s = r_c/χ = 25.4 fm (the Q1 mixture R_s is the OPEN-SS-43 dSph-side
screening, a different quantity); geometry M = N·1408 MeV, L = (N−1)·1.15 fm;
abundance per species = its Q1 mass fraction × ρ, Erickcek normalization;
criterion = 1879's own per-bin conservative test, verbatim, no new criterion.

**The grid (2 signs × S_c {0.012, 0.035, 0.05} × ρ {0.2, 0.3, 0.6}), both
compositions, all four species:**

| Grid point class | extended N=(4,5) w=0.217 | central N=(3,6) w=0.064 |
|---|---|---|
| S_c = 0.05 (island high edge), any ρ | EXCLUDED-class (up to 12 bins) | EXCLUDED-class (up to 12 bins) |
| S_c = 0.035 (ruling point), any ρ | EXCLUDED-class (1–8 bins) | EXCLUDED-class (1–9 bins) |
| S_c = 0.012 (island floor), ρ = 0.6 | EXCLUDED-class (1 bin, ×1.39) | EXCLUDED-class (1 bin, ×1.03–1.31) |
| **S_c = 0.012, ρ ∈ {0.2, 0.3}** | **XQC-SAFE, both signs, both species** | **XQC-SAFE, both signs, both species** |

**What resolved of the "open both ways" physics:** at the island floor, the
1/M number-density suppression plus the populated-bin thresholds win — the
successor recoils land in bins where obs + 5√(obs+1) is a real budget, and
the dimer's quiet-bin kill (29–128 eV, obs 0 and 11, persisting below the
floor to S_c = 0.006) does NOT transfer. Above the floor, coupling wins: the
ruling point S_c = 0.035 excludes everything decisively. The high-ρ boundary
is soft in the hurting direction honestly stated: the ρ = 0.6 exclusions at
the floor are near-threshold (×1.03–1.39 in the 36–128 eV bin) — the corridor
edge, not a wall.

**The gate-cleared target Q3 inherits (sharpened, not just alive):** the
successor family survives in a CORRIDOR — S_c ≈ 0.012 (the post-DAMIC low
island edge, exactly the DAMIC-adjudicable boundary) at ρ_local ≤ 0.3
GeV/cm³. A Q3 derivation must now deliver BOTH: an S(N) that suppresses N=2
while populating N = 3–6, AND a realized coupling landing at the low island
edge. Noted as hint, not evidence: 1888's accepted-region S_c distribution
skews low, so the corridor is where the data-drawn portrait already lived.

**Stage-1 map at the surviving coupling (record):** σ_eff ~ 0.8–8×10⁻³⁰ cm²
across N = 3–6 — overburden-blind to the deep sites (SNOLAB/LSM ceilings
0.9–1.1×10⁻³¹) but inside or near the MINOS-depth window (2.3×10⁻³⁰) and
below the surface ceiling: **the survivors are not invisible; shallow-site
experiments have a computed visibility window** — an F-DM3-4-class
falsification channel attaches to the corridor from day one.

**Honest limits carried forward:** corridor endpoints are grid points, not
mapped boundaries (the S_c edge between 0.012 and 0.035, and the ρ edge
between 0.3 and 0.6, are unbracketed inside); Q1's limits persist (annealed
points not regions; naturalness ungraded). **NO VERDICT MOVED** — G-XQC-0 was
pre-registered as the derivation-investment gate, and it has now been passed
in corridor form. Q3 entry is UNLOCKED per the 2370 plan; whether to pay the
weeks-scale cost is the founder's call.

---

## CORRIDOR EDGE-MAPPING (Patch 2373, 9 July 2026) — THE WALLS, MEASURED: A GRADED CORRIDOR, KNIFE-EDGE AT ONE CORNER, MODEST AT THE OTHER

> **CORRECTION NOTICE (Patch 2374):** these walls were located under the 2372
> per-species criterion. Corrected walls (summed-spectrum criterion, ρ* now
> EXACT) in §Q3 OPENED (2374): every wall moves INWARD — extended-attractive
> effectively closes (ρ* = 0.211); central-repulsive remains the live corner
> (ρ* = 0.411; 5.7% of the island at ρ=0.3). Text below retained as record.

`code/2373_corridor_edge_mapping.py` + `2373_results.json`, verify 3/3 (V-a:
20/20 bracket endpoints reproduce stored 2372 composition verdicts from fresh
evaluation; V-b: bridge asserted every point; V-c: every bisection path
monotone). Bisection on the COMPOSITION verdict, 2372 machinery verbatim;
S_c* to ±1.8e-4, ρ* to ±0.0094.

**S_c* (fraction of the post-DAMIC island surviving, [0.012, 0.05]):**

| Composition, sign | S_c* @ ρ=0.3 | island kept | S_c* @ ρ=0.2 | island kept |
|---|---|---|---|---|
| extended, attractive | 0.0125 | **0.9%** | 0.0150 | 7.6% |
| extended, repulsive | 0.0146 | 6.6% | 0.0182 | 16.1% |
| central, attractive | 0.0146 | 6.6% | 0.0177 | 14.7% |
| central, repulsive | 0.0171 | **13.2%** | 0.0214 | **24.6%** |

**ρ* at the island floor (S_c = 0.012), GeV/cm³:** extended-attractive
**0.32** (a hair above the standard 0.3); extended-repulsive 0.43;
central-attractive 0.45; central-repulsive **0.58** (nearly the full 2366
bracket). **Interior headroom at (0.012, 0.3)** (worst bin ratio):
extended-attractive 0.931 (×1.07 under the gate — a hair); central-repulsive
0.514 (×1.95).

**The structure, stated hurting-first:** the extended-attractive corner is a
knife-edge on every axis — 0.9% of the island, ρ* barely above the standard
local density, ×1.07 headroom. If the substrate fixes the attractive sign
(the capture-channel heritage) AND realizes the extended-type composition,
the corridor effectively does not exist at standard ρ. The corridor is REAL
at the other corner: central-type composition (trace N=3 + heavy N=6
carrier), repulsive channel — ~13% of the island at ρ=0.3, ~25% at ρ=0.2,
ρ-exposure tolerant to 0.58, ×1.95 headroom. Ordering throughout: repulsive
> attractive; central > extended (the heavier carrier at higher fraction
buys more 1/M suppression).

**What this does to Q3's specification (sharpened again, and honestly
constrained):** the derivation does not get to aim. Its outputs —
composition (which N's, what fractions), interaction sign, and realized
coupling — are COMPUTED from substrate structure and then checked against
these measured walls, no steering. The sign is now flagged as a Q3
deliverable in its own right: the substrate must SAY which sign the
rod-nucleus channel carries, because the corridor width depends on it by a
factor ~2–15. The 1888 low-skewed S_c distribution remains a hint that the
floor region is where the data-drawn portrait lived; a hint, still.

**ρ is an exposure, not a knob (pre-stated in 2373, now quantified):** the
survivors are hostage to the local-density literature at the
extended-attractive corner (dies above 0.32) and robust at the
central-repulsive corner (survives to 0.58). Stated so nobody reads ρ* as
tunable freedom.

**NO VERDICT MOVED.** The 2372 gate result stands as graded; this patch
locates its boundaries. The Q3 go/no-go is on the founder's desk with these
numbers.

---

## Q3 OPENED ON FOUNDER GO (Patch 2374, 9 July 2026) — THE DEMAND SHEET, A CRITERION CORRECTION OWNED, AND THE CORRECTED CORRIDOR

**Founder verbatim: "Please proceed with recommendation."** — Q3 is GO per the
2373 recommendation. Stage structure registered: **Q3a** (this patch) = the
quantified demand sheet from registered relations only; **Q3b** = the
mechanism layer — full-distribution grading (summed spectrum + anchor suite),
nucleation/ring-closure S(N) shape, and the SIGN deliverable; **Q3c** = the
absolute E_bond / realized coupling — root-blocked on **OPEN-FP-SF-2-η**
per the standing scoping doc (`edge_bond_ssv_makeorbreak_scoping.md`; 0865
declined to fabricate a coupling and that discipline holds): Q3c either pays
that rent through the conjectured substrate-thermodynamic closure or declares
it unpayable.

### The criterion correction (owned; 2366/B1 precedent)
Computing the demand sheet's joint contamination budgets EXPOSED a
mis-specification in my own 2372 criterion: composition verdicts tested each
species ALONE against the full per-bin threshold. The observed spectrum is
the SUM. Diagnosis confirmed before correcting: extended at (0.012, 0.3)
sums to 40.3 (att) / 29.6 (rep) vs threshold 28.3 in the 36–128 eV bin —
graded SAFE by 2372, wrongly. `code/2374c_summed_criterion_regrade.py`
re-graded everything under the summed criterion (verify 3/3: single-species
limit reproduces the stored 2366b dimer point EXACTLY; f·ρ linearity 2e-15;
bisection monotonicity). **Exactly two verdicts flip** (extended, floor,
ρ=0.3, both signs); every EXCLUDED verdict stands a fortiori; **the 2369
dimer kill (single-species) and the Q1 anchor-suite passes (2344 sums
channels correctly) are unaffected.**

### The corrected corridor (ρ* now EXACT via f·ρ linearity)
| Combo | ρ* (GeV/cm³) | island kept @ ρ=0.3 | @ ρ=0.2 | status |
|---|---|---|---|---|
| extended, attractive | 0.211 | — (absent) | 0.5% | effectively CLOSED |
| extended, repulsive | 0.287 | — (absent) | 6.6% | sub-standard-ρ only |
| central, attractive | 0.305 | ~0.0% (at the wall) | 6.6% | knife-edge |
| **central, repulsive** | **0.411** | **5.7%** | **14.7%** | **the live corner** |

The sign deliverable is now near-decisive: attractive-sign corridors are
hair-thin everywhere; the successor family effectively NEEDS the repulsive
channel and the central-type composition (trace light + heavy carrier).

### THE DEMAND SHEET (corrected; what a viable derived population must satisfy)
- **D1 — freeze-out ratio:** E_bond/kT_form = **23.2–36.2** for survivor
  N=3–6 (registered 0881 inverse map; logarithmic in φ). Closure inside the
  fragmentation window [0.78 keV, 1.95 MeV] holds at every plausible kT_form
  ≤ 19 keV — the old four-constraint closure survives the small-N transition
  essentially intact (survivor demand overlaps the registered 24–41 band).
- **D2/D3 — contamination (JOINT rectangle bounds, carriers first, floor
  coupling):** at the live corner (central-repulsive): w(2) < **0.034**,
  w(1) < **0.013** at ρ=0.3; w(2) < 0.096, w(1) < 0.037 at ρ=0.2.
- **D4 — suppression beyond generic equilibrium:** isodesmic (Flory) at
  ⟨N⟩ₙ=6 gives w(2)=0.046, w(1)=0.028 → demanded suppression ×1.4 (dimer) /
  ×2.1 (monomer) at ρ=0.3; ~×1 at ρ=0.2. **Modest, not 10×-class — the
  generic-equilibrium death mode is NOT armed as a wholesale killer.**
  CAVEAT carried loudly: isodesmic at ⟨N⟩ₙ=6 puts 67% of mass at N>6, whose
  summed-spectrum contribution AND anchor-suite behavior are UNGRADED — the
  full-distribution grade is Q3b's named first computation, and it can still
  kill.
- **D5 — coupling:** land S_c at the island floor; corrected walls above
  (central-repulsive keeps 5.7–14.7% of the post-DAMIC island).
- **D6 — sign:** derived, not chosen — and now near-decisive (repulsive or
  bust, at standard density).

**NO VERDICT MOVED** (the corridor was never a registered verdict; its
grading is corrected in the hurting direction). Q3b next: the
full-distribution summed grade is cheap-first and can close the family
before any nucleation derivation is attempted.
