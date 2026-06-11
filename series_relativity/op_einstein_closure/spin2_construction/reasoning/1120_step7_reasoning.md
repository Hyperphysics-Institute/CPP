# Reasoning capture — Patch 1120 (Step 7, the tensor-meson test)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1120_step7_tensor_meson_test.md` + `code/1120_step7_tensor_meson_test.py`.

---

## The question and the stakes (from the kickoff handover)

The handover flagged tensor mesons (f₂(1270)) as the "candidate SECOND motivation to TEST":
if CPP's strong sector hits the same representational wall for spin-2 hadrons that the GW
sector hit (1116), that is an independent phenomenon demanding the same `Q_ij` axiom —
converting the axiom from mono- to multi-motivated, a strong convergent justification. If the
strong sector builds spin-2 hadrons emergently, the second motivation dissolves and the axiom
stays mono-motivated — which must then be stated honestly.

## The prior, stated to the architect before running

Expected the wall NOT to recur, for one reason: matter-side configurations can carry any l —
that is exactly what the SS-5/SS-6 nuclear quadrupole moments are (spatial arrangements of
multiple constituents). The 1116 wall is *per-point* (the broadcast data is 4-dimensional); a
two-constituent state spanning many GPs carries arbitrary l in its relative-coordinate
wavefunction, which lives in a function space. Predicted outcome: a sharpened contrast rather
than a second motivation. Both outcomes were identified as informative before the run; the
discipline was to run it regardless of the prior.

## Step 0 — corpus audit before any calculation

Per the grounding discipline (claims anchored in the corpus, not assumed):

- Searched the corpus for f₂(1270)/tensor-meson treatments: none exist (the test is new
  territory; only the kickoff handover and the SR frontier file mention it).
- **SS-1e found to already contain the answer in embryo:** the charmonium table lists
  χ_c2(1P) as "L=1, J=2" — a ³P₂ orbital excitation handled by the standard machinery
  (Cornell-potential excitations over CPP constituent masses), no new d.o.f. χ_c2 has the
  *same quantum-number construction* as f₂(1270). This was the decisive find: the corpus
  treats a spin-2 meson as emergent already; Step 7's job became making the mechanism explicit
  and testing its lattice support, rather than discovering the answer.
- **SS-6's negative finding repurposed:** the deuteron's observed Q_d = +0.286 fm² is
  orbital-dominated (rigid bipyramid gives −0.022 fm², wrong sign and 10× small). Read in this
  arc's light, SS-6 is a *demonstration* that CPP attributes measured l=2 observables to
  extended orbital wavefunctions — emergent rank-2 on the matter side, working quantitatively.
- c8/c9: constituent spin-½ = emergent ZBW orbital (vector). So the ³P₂ inputs (S from ½⊗½,
  L orbital) are both emergent vectors in CPP's standing treatment.

## The three calculations and why each

1. **Composition (P1):** build J = L + S on the 9-dim L=1 ⊗ S=1 space, diagonalize J²:
   multiplets {0,1,2} with degeneracies {1,3,5} — exact, standard Clebsch–Gordan, included so
   the step document *demonstrates* rather than cites that two emergent vectors reach J=2 at
   configuration level. The key conceptual point: this composition happens in the *state
   space* of two distinct constituent degrees of freedom — it is not the field bilinear of
   1115 (same field squared, second order in amplitude, double frequency). A bound state's
   quantum numbers carry no amplitude-order bookkeeping.
2. **Configuration-space support (P2):** mirror of 1112's shell computation, but in
   *configuration space*: evaluate the 5 real l=2 harmonics on lattice relative-position
   vectors (shells 1–2, 72 vectors); rank 5 = full support. This makes the resource contrast
   exact and quotable: per-point data = 4 components (l ≤ 1, fixed); relative-coordinate
   wavefunctions = function space (every l).
3. **Icosahedral protection (P3):** character-theory branching of D^(l) under the icosahedral
   rotation group I (order 60; classes E, 12C₅, 12C₅², 20C₃, 15C₂) vs the cubic group O.
   Motivation: check whether the *lattice discretization itself* could obstruct spin-2 matter
   (the one way the wall could have recurred). Result: the opposite — l=2 → H, irreducible
   (intact 5-fold multiplet), with first splitting only at l=3; under O, l=2 → E ⊕ T₂ (splits
   2+3). So not only does the lattice not obstruct spin-2, the icosahedral choice *uniquely
   protects* it — and the protecting irrep is exactly the H_g slot of 1112. Verified the
   character arithmetic numerically (multiplicities integer to 10⁻¹²; χ_T1(C₅) = 1+2cos72° = φ
   as a golden-ratio cross-check).

## The honest accounting (the part that must not be softened)

The second motivation dissolves. The axiom is mono-motivated by GW empirics, and the writeup
must say so plainly rather than padding the motivation list. The justification's strength is of
a different kind: *necessity* (three independent assaults closed — 1115 bilinears, 1116
collective modes, 1119 connection) rather than *breadth*. The distinction goes into the axiom
preamble verbatim. What the test bought instead:

- the granularity diagnosis located with precision (the wall is per-point — matter-side
  demonstration of the architect's intuition);
- the protection bonus (cubic would split the 5-fold multiplet; icosahedral does not — an
  internal consistency credit and a free forward-looking property: once `Q_ij` is granted, its
  5 components stay degenerate at leading order, no lattice fine-structure of GW
  polarizations);
- the diagnostic phase of the sub-arc is now COMPLETE (Steps 1–7), and the construction
  proper (flow choice, axiom text, source coupling, GR-recovery, DG-3) begins on a fully
  mapped floor.

## Discipline notes

- Re-synced to origin (`git reset --hard origin/main`) before building, since the architect's
  `git am` of 1119 created its own commit hash — the patch is built on the pushed history
  (CONV-002 spirit).
- NO VERDICT MOVED: no THEO/PRED/ID registered, no count change. Private-lane paths only
  (spin2_construction/ + parent INDEX/README, owned subtree). No contested file touched.
- Falsifier honored: had the lattice branching split l=2, or had the corpus shown the strong
  sector unable to construct J=2 states, the step would have reported the wall recurring and
  opened the multi-motivation route instead.
