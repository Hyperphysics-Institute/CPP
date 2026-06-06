# Inflationary-homogeneity grounding: leg 1's last input is a standing cosmo-sector commitment

*Patch 0776, Session 154. Closes the one remaining leg-1 residual flagged at 0774/0775: the symmetric ZRP
kernel's reliance on a homogeneous, isotropic inflationary background. This finding shows that homogeneity is
not a leg-1-specific assumption — it is a standing commitment of the CPP cosmology sector, equipped with a
CPP homogenization mechanism (VSL), used in at least five places, and the zeroth-order background the entire
n_s observable is defined on. Grounding (no new computation). Finding-level; NO THEO.*

## What leg 1 needs

The symmetric neighbour kernel p(i,j) = p(j,i) (zrp_derivation.md, property iii) requires no net SSV
gradient at the relevant scale during inflation — i.e. a homogeneous, isotropic background. 0774/0775 listed
this as the one input not yet grounded. This finding grounds it.

## Homogeneity is already load-bearing across the CPP cosmology sector

1. **The whole cosmo sector rests on the FRW/Friedmann framework.** `step1_scaling_phase_kill.md`: work
   proceeds "inside the Step-D excess-sourcing Friedmann framework … that the whole cosmo sector already
   rests on." The FRW metric *is* the cosmological principle — spatial homogeneity + isotropy. So a
   homogeneous-isotropic background is the assumed substrate of the entire CPP cosmology sector, not
   something introduced for leg 1.
2. **CPP has a homogenization mechanism: VSL.** `axiom_h_inflation_engine_evaluation.md` (Patch 0738,
   adopted engine): "A large early PSR (VSL) addresses the horizon/causal-contact problem." The horizon
   problem is precisely the question of *why the universe is homogeneous*; VSL (large early PSR → causal
   contact across the universe) is CPP's smoothing mechanism — the same role inflation plays in the standard
   picture.
3. **The medium is explicitly homogeneous.** `cosmic_web_generation_constraints.md`: the substrate is "a hot
   homogeneous ZBW-mixing medium."
4. **The H-engine growth is spatially uniform.** `lattice_growth_escape_closure.md`: each GP spawns
   neighbours "at a constant per-GP rate" — a spatially homogeneous growth law (no preferred location).
5. **The n_s observable itself is a perturbation on a homogeneous background.** The tilt n_s − 1 is, by
   construction, the scale-dependence of *perturbations* around a homogeneous-isotropic FRW background — this
   is cosmological perturbation theory. Without a homogeneous background there is no power spectrum to tilt.
   And the spectrum's Gaussianity (CLT over ZBW phases, Patch 0738) requires the ZBW phases to be
   statistically identical across the lattice — i.e. statistical homogeneity. So the very calculation the
   tilt lives in already assumes the homogeneity leg 1's kernel uses.

The symmetric ZRP kernel's homogeneity input is therefore the *same* homogeneity used at the FRW-sector
level (1), supplied with a mechanism (2), describing the medium (3), characterizing the H-engine (4), and
underlying the n_s observable and its Gaussianity (5). Leg 1's kernel is one more consumer of a commitment
the framework already makes five ways over — exactly parallel to how leg 1's ergodicity (0769) and leg 2's
neutrality (0770) turned out to be standing commitments rather than bespoke knobs.

## Consistency: the perturbations don't spoil the leading-order symmetry

The inhomogeneities that *are* the n_s perturbations are first-order in cosmological perturbation theory; the
symmetric kernel is the zeroth-order (background) statement. Using a symmetric kernel at leading order and
treating the SSV gradient as the perturbation is the standard, self-consistent perturbative setup — the same
O(perturbation) bookkeeping already in force throughout the arc (and the same channel as the O(α) SSV
correction quantified at 0774). So grounding homogeneity here does not conflict with the existence of the
very perturbations n_s describes.

## Honest scope

- This **grounds** homogeneity as a standing cosmo-sector commitment with a CPP mechanism (VSL), at the
  **same epistemic level as standard inflationary cosmology** — where a homogeneous background is assumed for
  perturbation theory and inflation is the smoothing mechanism. It does **not** prove homogeneity from
  A1–A11.
- **The deeper open question** — a rigorous A1–A11 demonstration that the H-engine/VSL *provably produces*
  homogeneity from generic initial conditions — remains open, and is open in *standard* inflationary
  cosmology too (the "inflationary initial conditions" problem). CPP is at parity, not at a deficit, here.
- **Net for leg 1:** with homogeneity grounded, leg 1 has **no remaining bespoke, leg-1-specific
  assumption**. Its two inputs are both accounted for: the PCD→ZRP reduction (derived to leading order,
  0774/0775) and inflationary homogeneity (grounded as a standing commitment, here). The conditionality that
  remains is the *deeper* A1–A11 layer shared with the rest of CPP and with standard cosmology: (i) the
  PCD-compute → ZRP reduction being exact at the axiom level, and (ii) the H-engine provably producing
  homogeneity. Both are leading-order-derived / grounded-with-mechanism, neither bespoke.
- n_s = 0.9649 ± ~0.0005(theory) therefore remains a **conditional/grounded** prediction, but the
  conditionality is now uniformly at the "standing-commitment / leading-order-derived" level — there is no
  longer an *ungrounded* input anywhere in either leg. Whether that clears the bar to promote n_s to Section
  1 / a counted swarm contribution is a panel judgement (offered).

## Pointers

- Grounding sources: `step1_scaling_phase_kill.md` (FRW framework the cosmo sector rests on);
  `axiom_h_inflation_engine_evaluation.md` (VSL addresses the horizon problem, Patch 0738);
  `cosmic_web_generation_constraints.md` (homogeneous medium); `lattice_growth_escape_closure.md` (uniform
  per-GP growth); Patch 0738 (CLT-Gaussianity ⇒ statistical homogeneity).
- Leg-1 chain: 0772 (H-theorem), 0774 (ZRP derivation), 0775 (panel consensus); this patch grounds the
  homogeneity input those left open.
- Reasoning: `reasoning/0776_inflationary_homogeneity_grounding.md`.
