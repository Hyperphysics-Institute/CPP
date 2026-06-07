# Problem History: OPEN-EU-1 — A1–A11 derivation of FRW/VSL homogeneity + the exact ZRP-correction structure

**Created:** 6 June 2026 (registered at EU-1 v1.0 SHIP, Session 155; PH created Patch 0790)
**Status:** OPEN — registered open frontier at EU-1 v1.0 SHIP; closure path partially identified
**research_frontier.md entry:** OPEN-EU-1 (frontier sector home: `frontier_sectors/SR.md`)
**Target paper:** EU-1 v1.x revision, or a dedicated early-universe homogeneity/engine paper
**Parent paper:** EU-1 v1.0 SHIPPED 6 June 2026 (`series_phenomena/cosmology/early_universe/EU-1/`)

---

## The Problem

EU-1 derives the CMB scalar spectral index $n_s = 1 - 2/N_* \approx 0.9649$ as a leading-order,
**framework-conditional** result. Two of its inputs are grounded as standing CPP cosmology-sector
commitments but are **not yet derived from the primitive axioms A1–A11**:

1. **FRW/VSL homogeneity** — the symmetric, position-independent hop kernel ($p(i,j) = 1/12$) of the
   zero-range process requires a homogeneous, isotropic inflating background. EU-1 takes this as an
   epoch input (grounded at Patch 0776), shared with standard inflationary cosmology, which also does
   not derive homogeneity from first principles. Deriving it from A1–A11 (why the inflating substrate
   is homogeneous) is the deepest residual.
2. **The exact ZRP-correction structure** — LEMMA-NS-ZRP-DERIVE identifies the PCD/ZBW dynamics with a
   symmetric constant-rate ZRP *to leading order*, assuming no $O(1)$ occupancy-dependent microphysics
   beyond the SSV coupling. The exact form of the $O(\alpha)$ correction $g(n) = n[1 + \lambda(n-1)]$
   and its coefficient are model-dependent; deriving them from primitives would close the theory
   uncertainty ($\Delta n_s \sim 5\times10^{-4}$).

Closing OPEN-EU-1 would convert PRED-C-96 from a framework-conditional entry toward an unconditional
A1–A11 derivation.

## Why it does not block the result

OPEN-EU-1 is registered as a residual that **does not block the count**: $n_s$ is counted (PRED-C-96)
at the conditional/grounded level, exactly as the 55 nuclear-physics conditional predictions are counted
on their own structural-hypothesis stacks. The CPP cosmology sector is **at parity** with standard
inflationary cosmology on the homogeneity-from-first-principles question — neither derives it — so EU-1
is not behind the field; it simply does not claim more than it has.

## Progress to date (the n_s arc, Patches ~0729–0778; EU-1 ship 0781–0789)

- The tilt was reduced to $n_s = 1 - 2/N_*$ with $N_*$ from the CP count (0741–0742).
- The boost law was shown to be logarithmic and uniquely so among natural occupation laws (0743–0746),
  with the log traced to A1 indistinguishability (0749).
- The bath was derived to leading order as a symmetric constant-rate ZRP with a provable $H$-theorem
  (LEMMA-NS-HTHEOREM 0772, LEMMA-NS-ZRP-DERIVE 0774/0775); homogeneity grounded (0776).
- Charge neutrality (leg 2, DP-Sea, 0770) and the long-range Debye closure (LEMMA-NS-BATH, 0764–0768)
  were established.
- A candidate axiom (CAND-AX-EU-1) was drafted and then dissolved — its ergodicity half is MC-derivable
  and its log half is A1 — so no new axiom was needed (0751→0778).

## Closure path

- **Homogeneity (item 1):** derive FRW/VSL homogeneity of the inflating substrate from A1–A11 — likely
  via the substrate's maximum-entropy / vertex-transitive 600-cell symmetry under the PCD/ZBW dynamics.
  This is the harder, deeper target and the same open question the rest of CPP cosmology shares.
- **ZRP-correction (item 2):** derive the exact $O(\alpha)$ SSV deformation of $g(n)$ from the
  SSV-mediated CP–CP coupling, replacing the model-dependent $\lambda \sim \alpha$ assumption with a
  computed coefficient. More tractable; would sharpen the theory uncertainty.
- A related, separately-registered residual is the **constant-$H$ / inflation-engine debt** — EU-1
  derives the *spectrum*, not the *engine* (the constant-$H$ background / VSL dynamics). That is the
  other half of "deriving inflation" and the highest-leverage early-universe target overall.

## Pointers
- Parent paper: `series_phenomena/cosmology/early_universe/EU-1/EU-1_primordial_spectral_index.tex` (v1.0).
- Findings: `zrp_derivation.md`, `bath_htheorem.md`, `neutrality_grounding.md`,
  `inflationary_homogeneity_grounding.md`, `bath_temperature_lemma.md`.
- Prediction: PRED-C-96 (`predictions.md` §1); companion PRED-O-34 ($\alpha_s$).
- Frontier: `frontier_sectors/SR.md` (OPEN-EU-1).
