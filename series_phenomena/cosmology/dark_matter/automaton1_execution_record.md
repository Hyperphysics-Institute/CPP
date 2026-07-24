# AUTOMATON-1 EXECUTION RECORD (appended per leg; frozen 2796 prereg)

## LEG 1 — VALIDATION GATES: V-3 PASS, V-1 FAIL-STOP (Patch 2797)

**Executed 2026-07-24. Engine: `code/2797_automaton1_engine.py` (the
frozen Moment rule + DR-1..DR-3; FFT shell-convolution relay; DR-3
self-parcel exclusion verified structural — the shell band excludes
distance 0, so no GP ever receives its own transmission).
Reasoning: `reasoning/2797.md`.**

**V-3 (shell isotropy): PASS** — dipole-moment axis anisotropy 0.00%
at R ∈ {2, 3, 4} (|S| = 62/98/210; exact by cubic symmetry).

**V-1 (static field law): FAIL as frozen — production BLOCKED per
the prereg's own clause ("DR-1 is inadequate; STOP and
re-prereg").** Frozen procedure (pinned ± dipole, M = 32, R = 3,
window r ∈ [2R, M/3]): p = 2.683 vs band [1.8, 2.2].

**V-2: not reached** (V-1 blocks in execution order).

**Diagnostic appendix (same-font; measurements only, no re-freeze
tonight):**
1. Excluding the window's lower-edge point (r = 6 = 2R exactly):
   p = 1.988 over [7, 10] — the frozen window included its own
   near-field boundary point (the X4 window-edge lesson, recurring
   at design time).
2. The frozen configuration pins a DIPOLE and demands monopole
   scaling — the − partner's cancellation steepens large-r decay by
   construction (M = 48 wide-window: p = 2.219).
3. Single-charge jellium redesign (principled monopole): p = 2.31 —
   2.47, with LOCAL slope RISING toward the cell midplane (2.14 →
   2.35 → 2.64) — the signature of the torus itself (the field must
   vanish at M/2 by symmetry), afflicting ANY field including exact
   Coulomb.
4. Comparative-gate concept (automaton vs exact lattice Coulomb on
   identical torus/window): the quick Fourier comparator produced
   implausible exact-Coulomb slopes (local p = 0.72 near free-space
   conditions) and is itself SUSPECT — a verified real-space
   Ewald-sum comparator is required before any comparative band can
   be frozen.

**Disposition:** V-1's frozen design conflated three separable
effects (near-field edge point; dipole vs monopole scaling; torus
midplane steepening). Whether DR-1's relay field is
Coulomb-consistent is NOT YET DETERMINED — the honest current
answer is "the frozen test could not have decided it for any
field." Re-prereg (fresh patch) will freeze a comparative V-1:
automaton monopole-jellium field vs a VERIFIED exact-Coulomb
comparator on identical geometry, axes, and window, with the band
on the DIFFERENCE — after the comparator is validated against the
free-space law at small r/M. No production Moment has been run; the
79.5% is untouched; PR4 remains open pending the re-gated run.

---

## LEG 2 — V-1R COMPARATIVE GATE: 3/3 PASS; V-2 PASS — PRODUCTION LICENSED (Patch 2798)

**Executed 2026-07-24 under the frozen 2798 re-prereg
(`automaton1_v1r_reprereg.md`). Comparator:
`code/2798_ewald_comparator.py`, V-1b validated at 0.856% vs free
space. The 2797 FAIL is classified a GATE-DESIGN defect: exact torus
Coulomb itself has p = 2.291 on the original diagnostic window — the
frozen [1.8, 2.2] band was unsatisfiable for any Coulombic field on
the geometry.**

**V-1R (comparative, quoted):** R = 2: normalized ρ ∈ [0.991, 1.026],
Δp = 0.022 → PASS. R = 3 (confirmatory-disclosed): ρ ∈
[0.994, 1.029], Δp = 0.022 → PASS. R = 4: ρ ∈ [0.991, 1.005],
Δp = 0.020 → PASS. **3/3 — GATE OPEN.**

**V-2 (melee conservation/boundedness):** net charge conserved to
−2.9e−13; L1 field-content trend +1.4% second-half vs first-half
(bounded oscillation, no growth) → PASS.

**First-class positive finding (offered for the record):** the
founder's Moment rule under DR-1's minimal faithful implementation
produces EMERGENT INVERSE-SQUARE ELECTROSTATICS — shape agreement
with exact torus Coulomb within ±2.9% pointwise and Δp ≤ 0.022
across an 2× range of shell radii. The Coulomb field is not an input
anywhere in the automaton; it emerges from surface-integrated
DI-bit relay.

**Production (2796 §4, unchanged) now licensed: R ∈ {2, 3, 4}
melee runs proceed.**

---

## LEG 3 — PRODUCTION + DELIVERABLES: **VERDICT NOT-GIBBS** — the bare Moment rule QUENCHES (Patch 2799)

**Executed 2026-07-24/25 under frozen 2796 §4. Analysis:
`code/2799_automaton1_deliverables.py`; final states archived
(`data/x3x4/automaton1_final_states.json.gz`; full trajectories
regenerate deterministically from the committed engine + seeds).
Reasoning: `reasoning/2799.md`.**

**The observed dynamics (all three R, identically in kind):** during
warm-up the melee AGGREGATES into massive multi-CP piles (R = 2: 57
occupied sites, piles to 26 CPs; R = 3: 34 sites, to 52 CPs; R = 4:
extreme) — then FREEZES COMPLETELY: zero CP motion across the entire
80k-Moment production window at every R (all 4000 samples identical;
⟨H⟩ variance exactly zero).

**Mechanism (diagnosed, two parts):** (1) **Co-location is
absorbing** — the committed rule samples the field at the CP's GP,
so CPs sharing a GP feel identical fields and displace identically
forever; merges are irreversible and piles only grow, regardless of
charge sign (R = 2 final state holds 1378 like-sign same-site
pairs). (2) **Rounding-floor stasis** — once inter-pile fields
produce displacement components < ½ GP, the nearest-GP snap
(committed engine convention) yields zero motion; the pile
configuration locks. The bare rule is deterministic and dissipative:
it finds a fixed point and stays there.

**Committed deliverable evaluations (frozen bands):**
- **D-(vi) θ_κ/θ_H: FAILS BY NON-EXISTENCE, 3/3 R.** The frozen
  automaton ⟨H⟩ is POSITIVE (+106.0 / +495.4 / +5030.2 — same-site
  like-pair stacking dominates); Gibbs ⟨H⟩ for the lattice
  Hamiltonian is NEGATIVE at every temperature (−126.0 ± 0.5 at
  θ = 0.5 → −43.2 ± 1.0 at θ = 8, → 0⁻ as θ → ∞). No matching θ_H
  exists.
- **D-(ii) Gibbsian screening: FAIL, 3/3 R.** The automaton
  "ensemble" is a delta function on a frozen crystal (R = 4 κ
  extraction degenerate at 0.000); Gibbs κ ∈ [0.45, 0.94] across
  the grid. No band can be met.
- **D-(i):** the stationary marginal is a point mass — vacuously
  "energy-only," substantively uninformative; recorded as
  DEGENERATE.
- **D-(iii):** probability currents identically zero (frozen) —
  trivially detailed-balance-consistent; DEGENERATE.
- **D-(iv):** relaxation time infinite (motion ceased);
  SLOW-VARIABLE in the extreme.
- **D-(v):** the committed dipole estimator (signed min-image COM)
  is torus-wrap ill-defined and its nine biased-run responses show
  no coherent on-axis pattern — reported FAIL/NOISE same-font, with
  the estimator defect flagged (a Resta-phase polarization is the
  clean follow-up estimator; not substituted post-hoc).

**FROZEN VERDICT: NOT-GIBBS** (committed bands (ii) and (vi) fail at
3 of 3 R). Per the charter: an adverse outcome is a first-class
physics finding, reported in full; no promotion from inside; the
79.5% untouched.

**The physics finding (offered for the founder and the record):**
the Moment rule as chartered (commitments 14–18) contains NO
agitation source — it is deterministic and, with the displacement
quantization, dissipative. Left alone it does exactly what such a
rule must: binds opposite charges, aggregates (co-location
absorption), and quenches to a static configuration — a T → 0
quench, not a finite-θ ensemble. **Gibbs statistics — the
foundational assumption of the entire MCMC screening programme —
therefore requires an EXPLICIT agitation degree of freedom that the
bare rule does not supply.** This lands precisely on the founder's
ZBW-as-agitation-bath route (the K1-S1 arc): PR4's discriminator
elevates that route from "a derivation path for κ·a = 2" to "the
physically necessary ingredient for the Sea to be a statistical
ensemble at all." Two further doctrine-adjacent observations for the
founder's reading: (a) the spontaneous ± binding the automaton
exhibits is qualitatively the Sea's dipole (DP) formation; (b) what
the automaton lacks — the agitation that keeps the Sea from total
collapse into inert piles — is exactly what ZBW supplies in the
founder's physical picture. Whether the next automaton iteration
adds a chartered agitation term (founder's physics) is a founder
question, not a worker resolution.

**Positive findings retained from this arc:** emergent inverse-
square electrostatics (leg 2, ±2.9% shape, Δp ≤ 0.022) stands
independently of the quench result — the bare rule gets the FIELD
right and the STATISTICS absent, which is itself a sharp,
publishable characterization of the Moment rule.
