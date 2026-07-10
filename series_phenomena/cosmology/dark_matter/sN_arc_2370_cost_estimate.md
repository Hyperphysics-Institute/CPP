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

---

## Q3b-1 EXECUTED — THE FULL-DISTRIBUTION GRADE: THE EQUILIBRIUM SHAPE DIES AT THE GATE (CANDIDATE) (Patch 2375, 9 July 2026)

`code/2375_q3b1_full_distribution_grade.py` + `2375_results.json` +
`2375b_verdict_robustness.json`. Verify 2/3 AS PRE-REGISTERED, with the failed
check's decisive content discharged by executed supplementary check (2368
pattern): V-a two-species limit reproduces stored 2371 totals to 2.6e-16;
V-b single-species limit reproduces stored 2366b exactly; V-c totals moved
1.03% under N_cut 96→128 against a pre-registered 0.5% tolerance — FAILED as
stated — and the supplementary check shows the PASS VERDICT itself is robust
(viol = 1.0000 at N_cut 96/128/192; a 128-anneal converges to the same
point). Two process events owned in the reasoning: a first-run truncation
artifact at N_cut=32 caught by V-c BEFORE recording (anchor N_cut raised to
96), and the scan budget reduced 150k→30k wide for tractability, disclosed,
seed-stability retained.

**The two channels:**

**XQC (summed criterion + hurting-direction tail bound, corridor floor):**
NO ⟨N⟩ₙ ∈ [1.5, 12] is viable at ANY surviving corridor point — both signs,
both ρ. Closest approaches: ×1.214 (repulsive, ρ=0.2, ⟨N⟩ₙ=6.00), ×1.821
(repulsive, ρ=0.3), ×1.729 (attractive, ρ=0.2), ×2.593 (attractive, ρ=0.3)
— binding bin 36–128 eV in every case. Not a hair-thin miss anywhere the
two-species corridor actually lives.

**Anchor suite (eff() generalized exactly from 2344's own two-species form;
g²(N) = g₀²(N/4)^p strain family):** the CENTRAL audited frame REFUSES the
Flory shape outright — best ×1.043, echoing the 2344-era near-miss
character. The EXTENDED frame admits Flory passes (⟨N⟩ₙ ≈ 9.6, p ≈ 5.9,
R_s ≈ 26; verdict-robust to N_cut=192) — and every such pass sits at
XQC-unviable ⟨N⟩ₙ anyway.

**OUTCOME (b) as pre-registered — CANDIDATE KILL of the equilibrium-shaped
(Flory/isodesmic) small-N family:** even where the anchor suite admits the
shape, the summed XQC gate excludes every ⟨N⟩ₙ at every corridor point.
CONTAINMENT: candidate only — no verdict moves, no paper edits; verification
= flash panel round on this single computation (2366→2367 pattern).

**The contrast that now defines Q3's remaining physics:** the 2371
TWO-SPECIES POINTS still pass both channels at the central-repulsive corner;
the EQUILIBRIUM SHAPE does not, anywhere. The corridor can host sharply
peaked, near-bidisperse populations but not broad equilibrium ones — the
distribution spreads mass across many species whose recoils pile into the
same 36–128 eV bin. Death mode (ii) is REARMED in sharpened form: the
derivation must produce a strongly non-Flory, near-bidisperse distribution —
nucleation with a critical nucleus AND a stiff size ceiling, not isodesmic
growth — plus the D5/D6 coupling and sign demands. That is a much taller
order than the 2374 sheet's modest ×1.4–2.1 rectangle-bound reading
suggested, and the sheet's own loud caveat (the ungraded N>6 tail) is
exactly where it died.

**Scope stated:** the XQC kill is graded at the corridor floor grid points
that survived 2374c (S_c=0.012, ρ ≤ 0.3-class); above the floor the
two-species exclusions stand from 2374c and higher S_c only increases
couplings. Halo parameters, explicit (panel WOUND, 2378): ρ ∈ {0.2, 0.3}
GeV/cm³ IS the graded grid; the velocity distribution is the 1879 pinned SHM
set (v₀ = 220, v_esc = 584, v_det = 233.8 km/s) and was NOT varied in 2375. Flory truncated/renormalized at N_cut=32 XQC-side with the
additive tail bound carrying the remainder in the hurting direction.

**NO VERDICT MOVED. Founder's desk: the flash-panel round on 2375.**

---

## THE XQC FIDELITY AUDIT (Patch 2379, 9 July 2026) — FOUNDER-DIRECTED; (B) HELD FOR THIS RESULT

**Founder's question, verbatim:** "Note that the data that killed our DM-1, 3 …
were from only one study, on a rocket 20 years ago. Are we confident in the
fidelity of that measurement?" One clarification carried into the record: the
dSph anchors are the survival side; the killing channel is XQC — one
instrument, one ~100 s flight (1999), reanalyzed 2007.

**What the literature says (session-searched, cited):** the dataset's
interpretation has been independently derived by four groups over two decades
— Wandelt et al. 2000; Zaharijas & Farrar 2005; Erickcek et al. 2007 (PRD 76
042007, the pinned analysis); Mahdawi & Farrar 2017 (JCAP 12, 004) and 2018
(JCAP 10, 007); plus a 2022 systematic reanalysis (arXiv:2209.04387) — mutually
consistent where comparable. The literature's NAMED systematic is the
nuclear-recoil **thermalization efficiency ε_th** (recoil → heat → measured
energy; flagged as an assumption in that literature and bracketed as low as
ε_th = 0.02 by Mahdawi & Farrar). Our 1879 pipeline implicitly assumed
ε_th = 1. For a calorimeter, ε_th near 1 is the physical expectation (heat is
what it measures); the 0.02–0.1 extremes are worst-case literature brackets.

**The audit (`code/2379_xqc_fidelity_audit.py` + `2379_results.json` +
`2379b_eth025_refinement.json` + `2379_unit_cache.json`; verify 3/3 — ε_th=1
reproduces stored 2366b and all four stored 2375 closest approaches;
threshold-loss monotone; attenuation cross-check exact). Direction was
pre-stated honestly open: compression slides high-E_R recoils INTO the quiet
binding bins — and that is exactly what happens first (ratios RISE at
ε_th = 0.5) before threshold loss wins at lower ε_th.**

**(A1) The registered 2369 dimer kill:** all twelve pre-registered points
remain EXCLUDED at ε_th ∈ {1, 0.5, 0.1}. At ε_th = 0.02 the four
island-floor points (S_c = 0.012) un-exclude while every S_c ≥ 0.035 point
remains excluded (viol 1–2). So the kill is robust across the physically
plausible range and down to 0.1; what is conditional at the 0.02 extreme is
the WHOLESALE twelve-point form, specifically its island-floor corner.
**Outcome (ii) as pre-registered: reported to founder + panel; this audit
moves no verdict and edits no registered text.**

**(A2) The 2375 candidate kill (equilibrium shape):** wholesale at
ε_th ∈ {1, 0.5} (loosest corner ×1.130 at 0.5); first re-opening at the
(repulsive, ρ=0.2) corner at ε_th = 0.25 (×0.914; refinement run); all four
combos open by ε_th = 0.1. **Measured conditionality: the equilibrium-shape
kill holds wholesale for ε_th ≳ 0.35–0.5 (linear crossing ≈ 0.35 at the
loosest corner) — comfortably inside calorimetric expectation, outside the
literature's worst-case bracket.** The (B) adjudication language carries
this conditionality.

**(A3) The corridor itself is ε_th-sensitive, non-monotonically:** at
ε_th = 0.5 the pileup direction FLIPS marginal points EXCLUDED
(central-attractive ρ=0.3: 0.985 → 1.132; extended corners similarly); at
ε_th ≤ 0.1 the corridor widens. **The live corner (central-repulsive,
ρ ≤ 0.3) survives the ENTIRE bracket** (worst ratios 0.73 / 0.87 / 0.71 /
0.31 across ε_th = 1 / 0.5 / 0.1 / 0.02). Wall re-mapping under ε_th is
conditional work, not owed until ε_th is pinned.

**(B) Attenuation envelope:** filter stack (generous 10⁻⁴ g/cm² envelope) and
residual atmosphere (10⁻⁵ g/cm²) give attenuation ~3×10⁻⁶ and ~4×10⁻⁷ at the
dimer's worst-sign per-nucleus σ_T (5.9×10⁻²⁵ cm² on C at the island high
edge) — the 1879 no-attenuation model is VINDICATED at envelope level; no
paper-level pin owed.

**Registered regardless of outcome (SI-1): the SINGLE-FLIGHT CONDITIONALITY**
— every XQC-channel verdict is conditional on XQC-2007 fidelity, with ε_th
the named systematic and the measured sensitivity thresholds above; DAMIC
independently carves the island's edges; **F5 (the reflight prediction, 46
events at the ruling point) is the direct future test, Micro-X-class
sounding-rocket calorimeters the natural vehicle; the ε_th pin itself
(thermalization of nuclear recoils in HgTe/Si microcalorimeters — a
detector-physics literature question) is the owed external input.**

**NO VERDICT MOVED.** Desk: (A) seat anomaly; (B) the 2375 kill adjudication,
now in conditional form; (B2) NEW — whether the registered 2369 kill text
gains the ε_th conditionality clause (founder + panel); (C) Q3b-2 go/no-go.

---

## ADJUDICATIONS EXECUTED + Q3b-2 OPENED (Patch 2380, 9 July 2026; founder-delegated "Recommend and proceed.")

**(A)** the round stands at THREE substantive seats (unanimity in substance;
duplication anomaly stays open as a seat-hygiene item). **(B)** the
equilibrium-shape kill is **REGISTERED, CONDITIONAL on ε_th ≳ 0.35–0.5** —
verdict text in `open_dm_dsph_1_inverse_arc.md`, Flory-scoped, both binding
panel findings carried. **(B2)** the 2369 registered kill's ε_th
conditionality clause EXECUTED as a dated addendum (claim-weakening only;
panel ratification flagged). **(C) Q3b-2 is GO.**

### Q3b-2 OPENED — the derived-nucleation attempt (weeks-scale; the arc's decisive derivation)

**The contract (pre-registered here, binding on the derivation):** outputs —
the realized size distribution w(N) (from substrate kinetics: 0861
ring-closure/nucleation machinery grounded first), the interaction SIGN, and
the realized coupling — are COMPUTED, then checked against: the corridor
walls (2374c, ε_th-robust live corner), the demand sheet (2374), the
near-bidisperse requirement (2375/2380 registered kill), and G-XQC-0 summed.
No steering; no smuggled parameters (0865 discipline); the absolute-coupling
stage remains root-blocked on OPEN-FP-SF-2-η — Q3b-2 derives the SHAPE and
SIGN; Q3c pays or declares the η rent.

**Stages:** **Q3b-2a** — grounding pass: 0861/0881 kinetics machinery
re-run on clean clone; the ring-closure bending-cost statement extracted and
its N_c implication computed; the derivation contract's verify battery
fixed. **Q3b-2b** — the kinetics computation: nucleation-and-growth under
registered SSV/PCD primitives; does a critical nucleus N_c ≥ 3 AND a
ceiling above N ≈ 6 EMERGE (not get imposed)? **Q3b-2c** — the derived
w(N) through both channels + walls; sign extracted; outcome graded.

**Death modes carried (all registered):** SSV-underivability; equilibrium
shape emerging anyway (now a REGISTERED kill to collide with); steepness
cap; coupling-landing (D5); sign (D6). Any one fires → the third kill lands
fully derived and the arc says so.

**Warm-launch: keyword class DM-WARM-2381; handover = this document
(§Q1 → §Q3b-2, complete) + `2379_unit_cache.json` (committed, reusable) +
the adjudication doc. Patch numbering resumes at 2381.**

---

## Q3b-2a EXECUTED — THE GROUNDING PASS: FLOOR STRUCTURAL, CEILING NOT FREE, STIFFNESS DEMAND INVERTED (Patch 2381, 9 July 2026)

**Warm-launch DM-WARM-2381 consumed as registered.** All three contracted
items executed; artifact `code/2381_q3b2a_grounding_ringclosure_Nc.py`
(exit-coded battery). **VERIFY 6/6.**

**Re-runs (clean clone):** 0861 reproduces exactly (SY peak 3.37; ℓ_p band
[105, 702] fm; representative N_peak = 820); 0881 reproduces exactly
(E_bond/kT_form ≈ 24–41; closure all-YES at kT_form ≤ 19 keV). The D1
small-N band independently recomputed from the 0881 inverse map:
survivors N = 3–6 → **[23.2, 36.2]**, exact match to the registered 2374
demand sheet.

**Bending-cost statement (extracted):** E_close(N) = c·(ℓ_p/ℓ_rung)·kT/N;
c = 14.054 (SY, registered J-factor) or 2π² = 19.739 (rigid). The discrete
N-gon equals the continuum rigid ring to machine precision (V4) — the form
is trustworthy down to N = 3.

**The N_c implication (four computed statements):**
1. **Floor — STRUCTURAL.** Closed rings require N ≥ 3; N = 1, 2 cannot
   close non-degenerately. If the frozen stable species is the ring,
   w(1) = w(2) = 0 IDENTICALLY (D2/D3 met identically, not marginally) and
   N_c = 3 EMERGES. Conditional carried: "stability = closure" is Q3b-2b's
   to derive; residual open chains at freeze-out re-arm D2/D3.
2. **Energetic window roomy:** closure at N = 3 favorable for
   ℓ_p/ℓ_rung ≲ 3.5–7.7 under D1.
3. **Placement — the stiffness demand INVERTS:** peak at survivors
   N ∈ [3, 6] demands **ℓ_p/ℓ_rung ∈ [0.89, 1.78]** — ×59–×788 softer than
   the 0861 large-loop era. Same single substrate object (2eDP:2qDP
   rung-bond SSV angular stiffness), inverted band. **NAMED KILL for
   Q3b-2b:** derived stiffness lands in [0.89, 1.78] or the ring mechanism
   dies at placement.
4. **Ceiling — NOT FREE (the pass's honest surprise):** equilibrium ring
   weighting gives tail suppression ×1.0–1.2 at the soft end and
   ANTI-suppression ×0.4–0.7 at the stiff end — the ceiling above N ≈ 6
   does not come from ring statics. If it exists it is KINETIC: rings have
   no reactive ends, growth stops at closure, and the frozen product is set
   by closure-vs-growth competition on open chains. That shutoff is
   Q3b-2b's named ceiling candidate; the registered death mode
   ("equilibrium shape emerges anyway") stays fully armed. (Closing text
   corrected in-session after the grid refuted the drafted summary — the
   2375 pattern, owned pre-commit.)

**Battery FIXED (binding under Q3b-2b/2c):** V1 SY peak; V2 0861 band;
V3 0881 + D1; V4 bending identity; V5 unit-cache integrity (336 keys,
schema N,sign,S_c,ε_th, 13 bins). Semantic cache cross-check
(viol = 3/642.219095) deliberately left to the summed-criterion channel in
Q3b-2c. **NO VERDICT MOVED.** Reasoning: `reasoning/2381.md`.

---

## Q3b-2b EXECUTED — NUCLEATION-AND-GROWTH: FLOOR, CEILING, AND NEAR-BIDISPERSITY ALL EMERGE; THE STABILITY FLOOR IS EPOCH-FREE (Patch 2382, 9 July 2026)

**Founder verbatim: "recommend and proceed."** Worker recommendation
executed: the QSS closure-vs-growth branching cascade (cheap-kill-first;
the time-dependent master equation deferred as unneeded — no verdict came
out marginal). Artifact `code/2382_q3b2b_nucleation_growth_cascade.py`,
**VERIFY 7/7** (2381 battery re-run green underneath by subprocess).

**Formulation (all registered or bracketed):** growth = a·φ per tick
(registered φ bracket); closure = g_SY(N/r)/r³·v_f (the r³ ℓ_p→rung
conversion carried explicitly — it moves onsets by decades); ε over the D1
band; v_f ∈ [0.1, 10], kernel ratio q ∈ [0.5, 2].

**The organizing result — the stability floor is EPOCH-FREE:** with
ℓ_p = κ/kT and ε = E_bond/kT scaling identically under cooling,
**N_stab = c·r/ε = c·κ/(ℓ_rung·E_bond)** — temperature-independent, a pure
stiffness-to-depth ratio of the one rung-bond SSV well. Rings below it pop
forever; above it lock permanently; ln Λ delays, never moves, the boundary.

**Contract answer: YES on both counts, nothing imposed.**
- **Floor:** N_c = max(3 topology, N_stab, closure onset J·v_f ≳ a·φ) —
  three stacked derived mechanisms; N_c ≥ 3 everywhere, rising with r.
- **Ceiling:** cascade termination — φ < J_peak across the whole registered
  window (×6 worst corner to ×10¹⁰⁺), onset always on J's exponential
  rising side, escape ≤ 1.5e-28, width ≤ 2 at every corridor placement. A
  NARROW MOVING BAND, not an N=6 wall: W(N>6) ≤ ~0.08 for peaks ≤ 5,
  ~0.5 at the peak=6 top edge — quantified exposure carried to 2c.
- **Near-bidispersity EMERGES BY MECHANISM:** dimers, the unique
  closure-less chain species, accumulate (C₂/c₁ = 0.31–0.41) and pair-jump
  (2+2→4): w(3) = 0.71–0.88, w(4) = 0.12–0.29 in the deep-closure regime —
  dominant light ring + O(20%) heavier companion, the qualitative shape of
  the 2371 corridor occupants, from topology + kinetics.
- **Anti-Flory collision:** DOES NOT FIRE. Categorical metric =
  top2-adjacent share ≥ 0.71 everywhere vs Flory ≤ ~0.3 matched (×3.4+).
  Honest edge owned: the first-draft summary claimed zero N>6 tail at every
  placement; the grid refuted it (0.48 at the peak=6 edge, Flory-tail ratio
  ×1.5 there) — corrected pre-commit, third machinery-catches-author this
  arc. The shape verdict rests on width.

**Placement kill RESTATED (2381 implication-3 SUPERSEDED,
retained-not-rewritten):** the binding placement is kinetic —
N_c(r, φ, ε) ∈ [3, 6] ⇔ **r ≲ 5.5–13** (bracket-corner table in script) —
an upper kill only; the equilibrium band [0.89, 1.78] was the wrong
ensemble, as 2381's own implication 4 anticipated.

**Λ condition registered (named, not fabricated):** D2/D3 budgets met for
Λ = ν_PCD/H(form) > 5.1e10–5.7e15 (φ-corner-dependent); SF/substrate-
cosmology pin owed, direction generic.

**Residuals carried:** chain-chain beyond 2+2 = O(1) shape correction near
onset; r-epoch drift bracketed by the scan; SY u>6 usage confined to
r<0.5 (flexible regime, one-sided robust — battery V7).

**NO VERDICT MOVED.** Reasoning: `reasoning/2382.md`. **Next — Q3b-2c:**
the derived w(N | r, ε) family through summed-XQC (2379 unit cache) + the
anchor suite at the ε_th-robust live corner, SIGN extraction, outcome
graded: the derived (3,4)-dominant shape lands in the corridor or the
third kill lands fully derived.

---

## Q3b-2c EXECUTED — THE COLLISION: OUTCOME (c)+(d); THE HEAVY DERIVED MEMBERS SURVIVE BOTH CHANNELS AT STANDARD DENSITY ON THE REGISTERED-DEFAULT SIGN (Patch 2383, 9 July 2026)

**Founder verbatim: "Please recommend and proceed."** Cheap channel first.
Artifacts: `code/2383_q3b2c_family_channels_sign_grade.py` (**VERIFY 5/5**,
pre-registered header incl. outcome taxonomy + hurting-first predictions),
`2383_results.json`, `2383_joint_couplings.json`, extended
`2379_unit_cache.json` (360 keys). Process owned: first launch killed by an
environment limit at the anchor header (XQC complete); DISCLOSED AMENDMENT
pre-anchor — stratified representatives (19/73), reduced budgets;
joint-member couplings recovered by targeted re-anneal.

**The 2381-named semantic debt DISCHARGED (V2):** the cache reproduces the
stored 2366b regression at 1.8e-16 AND matches a fresh 1879 pipeline call
bit-level. V4: the Q1 compositions re-graded from the cache reproduce every
stored 2374c verdict + worst ratio checked.

**XQC channel (73 members; exact ρ*; floor across the full ε_th bracket):**
- **Deep-closure (3,4) members DIE AT THE GATE** (ρ* = 0.099 rep / 0.066
  att at the floor) — G-XQC-0 kills the family's own light end.
- N4-dominant marginal (ρ* ≲ 0.24); N5-dominant alive at ρ=0.2 only.
- **N6-dominant members (r ≈ 8.5–12): ρ* = 0.43–0.66 repulsive /
  0.32–0.52 attractive, ε_th-robust — SAFE AT STANDARD DENSITY, BOTH
  SIGNS.**
- Above the floor the corridor CLOSES for every member (ρ* ≤ 0.09 at
  S_c ≥ 0.035): the population is **FLOOR-ANCHORED** — D5 is now a sharp
  landing demand at S_c ≈ 0.012.

**Anchor channel (composition PINNED; coupling-only scans):** the extended
frame admits nearly the whole family under BOTH laws; the central frame
REFUSES the registered strain family for every member (1.25–2.15) but
admits every multi-species member with free per-species couplings (the
2375 finding sharpened: central refuses the strain LAW, not these shapes);
the one shape failure is monodisperse {4} (fails both frames). Passing
couplings: g0² ≈ 0.001–0.011, p ≈ 1.3–12.6 (pass REGION; demanded
steepness as low as p ≈ 1.3), R_s ≈ 20–51 fm — bracketing the OPEN-SS-43
15–30 fm target.

**SIGN (extracted, not chosen):** the registered 1858 residual (screened
unipolar E_qq) is ATTRACT-ONLY — the registered default is attractive in
both channels; repulsion must emerge (or not) from the OPEN-SS-43 derived
form. **The run's central finding: 2374c's "repulsive or bust" was
composition-specific** (the Q1 points carry light contaminants); the
derived heavy members carry none (ring topology zeroed it) and **survive
at standard density on the default sign** — {6:1.0} ρ*=0.428
[bracket-min 0.344], plus three more attractive members ≥ 0.3 ε_th-robust.
**D6 does not fire on the default;** the sign now prices corridor WIDTH
(repulsive ≈ doubles headroom), not existence.

**OUTCOME (graded as pre-registered): (c)+(d).** Six repulsive joint
points at ρ ≥ 0.3; nine attractive at ρ ≥ 0.2, four of them ≥ 0.3.

**Q3c inherits a fully-specified derived target:** r ≈ 8.5–12;
N_stab = c·κ/(ℓ_rung·E_bond) ≈ 3.3–7.3; S_c at the island floor (sharp);
R_s ≈ 20–50 fm; either sign at standard ρ (repulsive preferred); Λ per
2382; masses N=6 → 8.45 GeV dominant (+7.04/9.86 companions) — the
direct-detection discriminant moves from the dead dimer's ≈2.8 GeV to
≈8.5 GeV (**Clause-1(d) relevance flagged to founder + panel**).

**Failures recorded with equal weight:** light members dead at the gate;
monodisperse {4} anchor-dead; strain law central-dead family-wide;
above-floor corridor closed.

**NO VERDICT MOVED** — candidate grading only (2375 precedent binds).
Reasoning: `reasoning/2383.md`. **WORKER RECOMMENDATION: combined CONV-001
verification round on the 2381–2383 arc** (stability floor, cascade, both
channel grades, sign extraction, disclosed amendments), carrying the
flagged 2380(B2) ratification + 2378 seat-hygiene mapping. Founder's desk:
round go/no-go; block EMPTY.
