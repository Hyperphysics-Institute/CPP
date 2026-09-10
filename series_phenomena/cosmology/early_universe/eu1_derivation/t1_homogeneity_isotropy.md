# T-1 delivered — the twelve-per-GP ignition is homogeneous by construction and isotropic *exactly* through ℓ = 5; the residual enters at ℓ = 6. The worker's quadrupole expectation (E-2) is withdrawn: ℓ = 2 vanishes identically

**Patch 3820, Session 170, 9 Sep 2026. Lane: EU.** Charter target T-1 (`OPEN-EU-1_derivation_charter.md` §2). Follows the occupancy re-grounding (3816) and the T-3b HALT (3818). Verify `scripts/3820_t1_icosahedral_isotropy.py` (6/6; double precision, confirmed to 40 digits). Reasoning `reasoning/3820_t1_homogeneity.md`. **Grade: ENTAILMENT** given the founder's twelve-vertex ignition — exact group theory, not a bridge statement. Nothing minted; no constant adopted (PD-007); PRED-C-96 untouched; 3710 not retired.

## §1 The statement (S-IGNITION-ISOTROPIC)

> **S-IGNITION-ISOTROPIC.** Under the founder's ignition (twelve CPs per GP, one to each icosahedral vertex, at every address of the pre-ignition ball), the first Moment's census at every grid point is (a) **identical across grid points** — homogeneous — because the initial condition assigns the same twelve-vertex configuration to every address; and (b) **isotropic exactly through ℓ = 5** at each grid point, because the icosahedral group I_h admits no invariant spherical harmonic at ℓ = 1, 2, 3, 4, 5. The first non-vanishing anisotropic multipole of the ignition census is **ℓ = 6**; the second is **ℓ = 10**.

Consequences, each verified:
- **ℓ = 1 (dipole) = 0.** The twelve momenta cancel: no net push at any GP. This was asserted at 3814 §1 and 3805; it is here verified as an identity, not an approximation.
- **ℓ = 2 (quadrupole) = 0.** No net shear at any GP. The traceless second moment Σᵢ vᵢvⱼ − (12/3)δᵢⱼ vanishes identically.
- **ℓ = 3, 4, 5 = 0.** No octopole, hexadecapole, or ℓ = 5 structure.
- **ℓ = 6 ≠ 0.** S₆/S₀ = 5.72. This is the entire angular content of the icosahedral start below ℓ = 10.

## §2 What this delivers against the charter

Charter §2 T-1 asked for: *"derive, or state and instrument, that the DP-sea dilution is homogeneous and isotropic at the causal-patch scale … and quantify the residual anisotropy the icosahedral start could imprint. Deliverable: a statement at the S-HENGINE-HELD grade (bridge or entailment, stated which) plus an instrument."*

- **Homogeneity:** delivered, and it is trivial rather than hard — it follows from the initial condition's uniformity (twelve per GP at *every* address), not from any subsequent mixing process. No stirring, no relaxation time, no 3805 pairing argument is needed for homogeneity as such.
- **Isotropy:** delivered, and *stronger than the charter asked for*. The charter expected an approximate statement with a quantified residual. The residual through ℓ = 5 is not small — it is zero, identically, by the representation theory of I_h.
- **Residual quantified:** first at ℓ = 6, with S₆/S₀ = 5.72; next at ℓ = 10.
- **Grade:** ENTAILMENT. Given the founder's twelve-vertex picture, this is a theorem about the icosahedral group, not a bridging identification of the S-HENGINE-HELD kind. It requires no new axiom, no PCD-level extension, and no [PCD-EXT] label.
- **Instrument:** `scripts/3820_t1_icosahedral_isotropy.py`.

## §3 The worker's E-2 expectation is WITHDRAWN

Charter §5 E-2 (on record before the founder's pictures): *"a neutral sea diluting on a fixed lattice is homogeneous by construction except for the icosahedral axes of the start. The residual is a quadrupole-scale anisotropy set by twelve directions — small, but the corpus should say how small, because a large-angle CMB anomaly aligned to twelve axes would be a fingerprint."*

**This was wrong, and in a way worth recording.** "Twelve directions" does not mean "quadrupole structure." The quadrupole is *exactly* zero, as are ℓ = 1, 3, 4, 5. The intuition that a discrete set of axes imprints low-ℓ anisotropy fails for the icosahedron specifically, which is the most isotropic finite point group in three dimensions — it is precisely the platonic symmetry whose lowest invariant sits at ℓ = 6.

**A misattribution this closes off.** The observed CMB large-angle anomalies (the quadrupole–octopole alignment, ℓ = 2 and ℓ = 3) **cannot** be attributed to CPP's icosahedral ignition. Those are exactly the multipoles the icosahedral start cannot produce. Any future attempt in the corpus to connect the twelve-vertex start to the low-ℓ CMB anomalies is excluded by this result, and should be.

## §4 Honest scope — what this does NOT establish

- **This is a statement about the ignition, not a CMB prediction.** The ℓ = 6 residual lives in the angular structure of the census at each GP at Moment 1. The ignition's structure is at the grid-point scale; after ~64 e-folds it is stretched by ~10²⁸ linearly, which carries sub-Planck structure to microscopic scales — not to CMB scales. **No observable fingerprint is claimed**, and none should be inferred from the ℓ = 6 number. What the result establishes is that the initial state's symmetry is exact through ℓ = 5, so no low-ℓ anisotropy needs to be diluted away in the first place.
- **It does not derive FRW/VSL homogeneity from A1–A11.** That was OPEN-EU-1's registered scope (0778). What is delivered is the ignition's symmetry, which is the part the founder's picture determines. The dilution's homogeneity *thereafter* rests on S-HENGINE-HELD's held-sector process (no GP created or moved) — unchanged, and not re-derived here.
- **It says nothing about the amplitude.** OPEN-EU-AMPLITUDE-1 (3818) is untouched. Note the tension: a start this symmetric is a start with *no* structure to seed ζ — the isotropy result and the amplitude gap are two faces of the same fact, and §5 records that explicitly.

## §5 The AP-4c near-field check (3816 §6) — resolved by separation, not by assumption

3816 §6 flagged AP-4c as load-bearing for T-1: deposit "occurs exactly once, at the [PSR] shell … pass-through tally excluded, near field carried by the relay recursion." For a ball *smaller* than the reach, the l_P shell lies outside the ball, so a literal shell-deposit-only reading would have no interior GP tallying anything at Moment 1.

**The check separates, and T-1 does not depend on it.** The twelve-per-GP census is a *local* fact at each address — twelve CPs, one to each icosahedral vertex, fixed by the initial condition. §1's isotropy and homogeneity follow from that local configuration and from its uniformity across addresses. Neither requires any GP to perceive the whole ball.

What *does* require the near-field relay to deliver is the **count** n̄ ≈ 10⁸⁴ within the PSR at Moment 1 — Branch P's occupancy, and hence the e-fold total. So the AP-4c question is load-bearing for the **count law (3816 §3) and OPEN-EU-PSR-EARLY-1**, not for homogeneity. 3816 §6's flag is hereby **re-pointed** to that item; it is not discharged, and it is not T-1's blocker.

## §5b AMENDMENT (Patch 3822) — the homogeneity clause presumed species-uniformity

§1(a) reads homogeneity from the initial condition assigning "the same twelve-vertex configuration to every address." That presumed uniformity of **species** as well as of **geometry**, and the presumption was not stated. The founder's picture (3822) denies it: with three interaction classes (eCP–eCP, eCP–qCP, qCP–qCP), no assignment of species and sign makes every local environment equivalent, so a perfectly homogeneous simultaneously-strong-and-electric-neutral mix is not constructible.

**Effect on this document:** §1(b) — the isotropy result, exact through ℓ = 5 — is purely geometric and is **unaffected**: it depends on the twelve icosahedral directions, not on what occupies them. §1(a) — homogeneity across grid points — is **conditional on species-uniformity** and, under the founder's picture, holds for the geometry while failing for the charge/species content. The residual inhomogeneity from that source is assessed at `charge_mix_and_edge_assessment.md` §1: real, but not a ζ source (frozen, white, and blind to the species-free end condition).

## §6 Standing

- **T-1 DELIVERED** at ENTAILMENT grade: S-IGNITION-ISOTROPIC (§1), instrument `scripts/3820_t1_icosahedral_isotropy.py`.
- **Charter §5 E-2 WITHDRAWN** (quadrupole expectation false; ℓ = 2 vanishes identically).
- **Excluded:** attribution of the CMB ℓ = 2/3 anomalies to the icosahedral ignition.
- **AP-4c near-field check RE-POINTED** from T-1 to the count law / OPEN-EU-PSR-EARLY-1 (§5). Still open there.
- **OPEN-EU-1** remaining targets: T-2 (the O(α) ZRP coefficient); T-3a/T-3b blocked at the HALT (3818) pending a founder picture on Q1.
- **CONV-046 candidate package** now: the re-grounding (3816) + the S-HENGINE-HELD wording note + the T-3b HALT (3818) + this T-1 entailment. This is the first *win* in the package (review economy §2) — T-1 delivered above the grade the charter asked for. Panel timing is a maintainer call; the package is assembled.
- PRED-C-96 untouched; nothing minted; 3710 not retired.
