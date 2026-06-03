# SR-1 reconciliation brick #1: l_P, PSR, and grid resolution — the three-level distinction

*Patch 0734, Session 153d. First brick of the SR-1 rederivation pass. This note supersedes the l_P framing in
BOTH Patch 0732 (which read l_P as "one grid step") and Patch 0733 (which over-corrected to "l_P = 10³⁰ GPs,
documented"). The accurate situation is more useful than either: the corpus carries two inconsistent readings,
and the inflation/first-moment questions turn on a different axis than the one 0732/0733 argued about.*

## 1. The objects that must be kept distinct
- **The GP graph** — the vertices of the repeated 600-cell motifs, "the absolute, eternal markers of space"
  (SR-1 §, line 1168). FIXED. This is what founders "Occupancy" L33 and Patch 0731 mean by "the lattice does
  not change": the *graph* is fixed and the DP Sea dilutes on it.
- **The grid resolution** — the physical spacing between adjacent GPs. **This is where the corpus is
  inconsistent (Q1 below).**
- **The baseline reach `l_P`** — the maximum displacement (Planck Sphere *Radius*) per Moment in unstressed
  space: PSR = l_P at ΔSSV=0 (c07; glossary-SR-1: l_P is "the unstressed baseline"). The *reach*, not the step.
- **`PSR_eff = l_P/(1+k·ΔSSV)`** — the stressed reach. Since ΔSSV ≥ 0 (it is the *excess* stress), **PSR_eff ≤ l_P
  always**: l_P is a hard ceiling on displacement per Moment, i.e. the speed of light c = l_P/t_P.

## 2. The two foundational questions the corpus does not currently settle

**Q1 — Grid resolution: l_P-scale tiling, or nested sub-Planck hierarchy?**
- *Reading A (SR-1 paper proper):* l_P is the standard Planck length (1.616×10⁻³⁵ m, line 711); the 600-cell
  edge is ~l_P/φ (R/a=φ, line 416); GPs are spaced at ~l_P. Then PSR=l_P is ~one cell edge — a few GPs at most.
  This is essentially the reading Patch 0732 used.
- *Reading B (companions + development):* GPs sit "at sub-Planck spacing" (c07, line 179); there are "~10³⁰ GPs
  per Planck length" (c01 development) and "~10³⁰ GPs per PSR (the PSR at STP)" (c07 notes); a PSR of radius R
  encloses ~R³ GPs. Then PSR=l_P is a radius enclosing ~10³⁰ nested GPs. This is the reading Thomas intended.
- *Likely reconciliation (to be made canonical in the rederivation):* the **nested 600-cell hierarchy** — a
  single 600-cell is l_P-scale (Reading A), and space is "a heavily nested array of 600-cell polytopes" (c01
  dev), so the *effective* resolution is sub-Planck (Reading B). "One step per tick" at the coarse scale = many
  fine GPs traversed (c01 dev: "multi-scale 600-cells, one step per tick"). Velocity gradation then lives in the
  fine nesting; the coarse step is the reach ceiling. **The rederivation must pick one reading and carry it
  through every paper consistently** — the present mixed usage is the defect that produced the 0732/0733 churn.

**Q2 — Metric variability: is l_P (the physical reach per Moment) FIXED, or epoch/medium-dependent?**
- *Fixed-metric reading:* l_P is a fixed geometric length set by the lattice (k = l_P³/E_P with the standard
  Planck l_P anchors the five SR predictions — line 712). c = l_P/t_P is constant.
- *Variable-metric reading (Thomas's VSL intuition):* l_P is the physical distance a one-Moment reach represents,
  and that is set by the medium (DP Sea μ, ε) on the fixed graph — so it can differ by epoch. c then varies.

## 3. What actually decides inflation — and it is Q2, not Q1
PSR_eff ≤ l_P holds under **both** Q1 readings (the ceiling is l_P whether it is ~1 edge or ~10³⁰ nested GPs).
So the maximum recession rate is c = l_P/t_P, and expansion at the ceiling is **linear at c**, not exponential —
under both readings. De-Sitter inflation *is* super-luminal recession of comoving points (recession ∝ distance,
unbounded), which **requires l_P itself to change** (a varying physical metric), i.e. the variable-metric branch
of Q2. **Therefore the GP-count question (Q1) is irrelevant to whether CPP can inflate; only Q2 is.** Patch
0732 (and the colourful "super-c by 10³⁰" framing) conflated the two; this is the correction that supersedes
both 0732 and 0733.

**Crucially, the Q2 variable-metric route is NOT closed by Patch 0731.** 0731 closed *graph growth* (adding GPs /
stretching the lattice scaffold). A variable physical metric on a *fixed* graph (same eternal GPs, different
physical distance per step, set by the medium) is a *different* mechanism that 0731 did not address. So:
**inflation in CPP is genuinely OPEN via the variable-metric / VSL route** — consistent with the fixed GP graph
(line 1168) — and this is the live thing the rederivation should evaluate. (0729's "no constant-H source" was
also computed at fixed c and must be redone in a variable-c framework.)

## 4. The first-moment "infinite displacement" question also hinges on Q2
- *Fixed-metric:* with no DP Sea, ΔSSV=0 ⇒ PSR_eff = l_P (the finite geometric ceiling). **No infinity; the H
  axiom's `l_P_base` is unnecessary, not ad hoc.** The "c=1/√(με)→∞ with no medium" intuition double-counts by
  treating the bare lattice as zero-impedance; the lattice geometry itself sets a finite ceiling.
- *Variable-metric:* with no medium, l_P (the physical reach) is large/undefined ⇒ the infinity returns and needs
  a regulator (a floor, or the H axiom). 
So Q2 has **opposite implications** for the first-moment problem and for inflation, and they are linked: the same
choice that dissolves the infinity (fixed metric) also forecloses VSL inflation, and vice-versa. This is the
sharp fork the rederivation must confront.

## 5. What is invariant regardless of Q1/Q2 (present-epoch anchors — untouched)
- GPs are fixed/eternal (line 1168); the graph does not change.
- k = l_P³/E_P with the standard Planck l_P (lines 711–712); the five SR predictions and the muon-storage-ring
  bound are anchored at the **present epoch** (present DP-Sea density). Any early-epoch VSL leaves them intact.
  So "the SR/SM sector is unchanged at the scales we test" is correct under either Q2 branch.
- PSR_eff ≤ l_P (ΔSSV ≥ 0): the speed-of-light ceiling at any given epoch.

## 6. Net (supersedes 0732 + 0733 on l_P)
The corpus carries two inconsistent grid-resolution readings (Q1); the inflation and first-moment questions turn
not on Q1 but on whether the physical metric is fixed or epoch-dependent (Q2); the Q2 variable-metric/VSL route
is open and is *not* closed by 0731 (which closed only graph growth); and the primordial **spectrum** (Gaussianity
+ scale-invariance) remains separately owed under any Q2 choice. The honest status of CPP-native inflation is
therefore **OPEN via the variable-metric route**, with two genuine sub-problems: (i) does a variable metric admit
a sustained constant-H phase, and (ii) the spectrum. The present-epoch SR/SM results are untouched throughout.

## 7. Pointers
- Supersedes the l_P discussion in `axiom_h_inflation_engine_evaluation.md` (0732/0733).
- Corpus citations: SR-1 lines 711–712, 1168, 411–416; c07_weak_field_GR.tex line 179, 196–198; glossary-SR-1.md
  line 84; c01_absolute_moment_postulate development_discussion.md lines 172, 525, 721; c07 development notes 699.
- Next bricks: see handover `handovers/2026-06-02_session_153_SR1_rederivation_scope.md`.
