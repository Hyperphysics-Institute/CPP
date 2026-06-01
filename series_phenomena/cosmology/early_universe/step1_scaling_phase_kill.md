# Early-Universe Dynamics — Step 1: the scaling-phase kill-check (OPEN-SR-7 → OPEN-COSMO-DM-2)

*Session 153b, 1 June 2026 (Opus, single-window). Patch 0729. The falsification-first
Step 1 of the OPEN-SR-6 arc: the cheapest potential kill for the DM-2 generation barrier.
This is a **conditional negative result** — it does not manufacture a mechanism; it shows the
two available branches cannot supply one. No THEO registered (arc convention: conditional/negative).*

## The question (Step 1, hard-ordered before Step 2)

OPEN-COSMO-DM-2 decomposes (Patch 0726) into (1) horizon/correlation — candidate-answered by the
atemporal Nexus — and (2) **perturbation generation + scale-invariance**, the real barrier. The
cheapest kill: **does CPP early dynamics (the GP-exclusion / CP–GP packing dynamics from the initial
Moment, OPEN-SR-6 ∪ OPEN-SR-7) admit ANY scaling-symmetric / quasi-de-Sitter phase** — any window of
(near-)constant Hubble rate H able to generate a near-scale-invariant (equal-power-per-log-interval),
adiabatic primordial spectrum? If a clean no-go surfaces, that is a clean **false** for CONJ-COSMO-1
as the primary structure source.

## Step-0 foundation (what is derived vs assumed)

- **GP = grid points** (600-cell vertices) at fixed spacing l_P; the lattice *is* space (`master_glossary`).
  Cosmic expansion is **lattice growth**, not metric stretching of a continuum. The CP–GP density ratio is
  the occupation/packing fraction; the **initial Moment is the GP-exclusion-saturated state**, and expansion
  is relaxation/dilution from saturation. OPEN-SR-6 (the expansion law) and OPEN-SR-7 (the packing limit) are
  registered but **undeveloped one-liners** (dated 23 Mar 2026); no early-universe packing dynamics exists in-corpus.
- **Derived background (sea_gravitation A→D):** CPP recovers standard ΛCDM via excess-sourcing. The early
  universe is **radiation-dominated** (w=1/3, strongly decelerating) — there is no de-Sitter era anywhere in the
  recovered history.
- **Load-bearing fact (Step B / c08 D2, Gate 1):** gravity couples to the SSV **excess** above the Sea ground
  state, not absolute energy. A uniform Sea is a constant g_tt (coordinate rescaling, zero curvature) and
  **explicitly "does not drive de Sitter expansion"** — this is precisely how CPP avoids the CC catastrophe.
- **No scaling material:** the corpus contains **no** de-Sitter / scale-invariance / inflation / self-similar /
  fixed-point / conformal mechanism — only the registry entries that *name* the gap.

## The derivation (parameter-free; `scripts/0729_scaling_phase_nogo.py`, 19/19 PASS)

Work inside the Step-D excess-sourcing Friedmann framework (Gate 1) that the whole cosmo sector already rests on.

**Lemma 1 — the constant-H requirement.** In FRW, a phase has constant H = ȧ/a iff the gravitating density ρ is
time-constant iff the effective EoS w = −1 (de Sitter). For barotropic w = const > −1, a(t) ∝ t^(2/[3(1+w)]) and
H(t) = 2/[3(1+w)t] — H falls monotonically as 1/t; no constant-H window. Equal power per log-interval (scale
invariance) is the signature of the w=−1 scaling symmetry; w > −1 gives no inflationary stretching. *(CHECK 1.)*

**Lemma 2 — what the packing/exclusion source gives.** An exclusion/degeneracy pressure increases monotonically
with density, vanishes as n→0, and stiffens toward the causal limit w → 1 as n → n_max (the saturated initial
Moment) — the same physics as Pauli degeneracy pressure or hard-sphere packing. The deceleration parameter
q = (1+3w)/2 > 0 for all w > −1/3; the packing range **w ∈ (0,1] is firmly decelerating**, with the stiff extreme
w=1 giving a ∝ t^(1/3), the *slowest, most decelerating* causal expansion — the polar opposite of de Sitter.
*(CHECK 2; a parameter-free excluded-volume EoS p = n e₀·x/(1−x), x=n/n_max, confirms w(n) ∈ (0,1] across the
full dilution history and never approaches −1 — CHECK 3.)*

**Lemma 3 — the vacuum route is independently closed (from Step 0).** The only component with the non-diluting
constant ρ that de Sitter requires is the uniform Sea ground state; by excess-sourcing (Gate 1) it is
**non-gravitating**. So the vacuum route to constant H is forbidden, and every gravitating source is a diluting
excess (Lemmas 1–2).

**The clincher — comoving Hubble radius (reading-independent).** Scale-invariant *generation* requires a **shrinking**
comoving Hubble radius, d/dt[(aH)⁻¹] < 0 ⇔ ä > 0 ⇔ w < −1/3, so modes exit the horizon and freeze. The packing
branch (w ∈ (0,1]) gives ä < 0 ⇒ the comoving horizon **grows** ⇒ modes *enter* (not exit) ⇒ nothing freezes ⇒
no scale-free spectrum is generated. *(CHECK 4.)*

## Verdict

**Conditional on Gate-1 excess-sourcing** (the cosmo sector's existing load-bearing commitment), **CPP early
dynamics admits no scaling-symmetric / quasi-de-Sitter phase.** The only constant-H-capable source (the uniform
Sea) is non-gravitating; the GP-exclusion source is a maximally stiff (w→1) diluting excess giving the most-
decelerating expansion. Constant H needs w=−1; the packing route delivers w ∈ (0,1]. **No equal-power-per-
log-interval window exists.** ⇒ The DM-2 generation half cannot be supplied by CPP early dynamics within the
recovered Friedmann framework ⇒ **CONJ-COSMO-1 fails as a *primary structure-formation* model — a clean
CONDITIONAL false (on Gate 1).** Its microphysics/rotation-curve gates (Steps 1–3, 5) still pass; this kills only
the structure-formation role.

## The one honest residual escape (why this is conditional, not unconditional)

A **substrate-intrinsic lattice-growth law not governed by the recovered Friedmann/excess-sourcing dynamics** —
e.g. each GP spawning neighbours at a constant per-GP rate → exponential N_GP growth → a de-Sitter-analog
constant-H window decoupled from gravitational sourcing. This is **triply disfavoured**: (i) undeveloped/
unregistered (no mechanism, no rate); (ii) it must coexist with — and not double-count against — the already-
recovered radiation-dominated, strongly-decelerating early Friedmann background; (iii) the lattice's fixed l_P is a
built-in fundamental scale (the antithesis of scale-freeness), and even a saturated-packing phase carries the
characteristic density n_max, not a scale-free spectrum. It is **not formally excluded by a single registered
theorem**, so the verdict is "clean conditional false with one narrow, undeveloped, disfavoured escape," not
"unconditional false." Closing the escape (or confirming it is empty) is the natural next sub-step: characterise the
OPEN-SR-7 lattice-growth law and test it against the Friedmann recovery for double-counting.

## Falsifiers

- **S1-1** — a CPP early component with constant gravitating ρ (true CC at Planck scale) consistent with Gate 1 → de Sitter restored (would also need to evade the CC catastrophe).
- **S1-2** — the OPEN-SR-7 lattice-growth law shown to give a self-consistent exponential (constant-H) phase that does *not* conflict with the recovered radiation-dominated background → escape opens; verdict reverts to open.
- **S1-3** — a non-de-Sitter scale-invariant generation mechanism (equal power per log-interval without ä>0) exhibited in CPP → Step 1 does not kill; proceed to Step 2.

## Pointers
- Verify: `scripts/0729_scaling_phase_nogo.py` (19/19 PASS). Reasoning: `reasoning/0729.md`.
- Foundation read: `series_phenomena/cosmology/sea_gravitation/stepD_friedmann_and_checks.md` (D2 excess-sourcing).
- Registry: `frontier_sectors/SR.md` OPEN-SR-6/SR-7; `frontier_sectors/CONJ.md` OPEN-COSMO-DM-2, CONJ-COSMO-1.
- Gate dependency: Gate 1 = c08 closed field equation (excess vs absolute |SSV|) — this result is conditional on it.
