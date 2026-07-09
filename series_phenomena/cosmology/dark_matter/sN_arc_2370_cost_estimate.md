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
