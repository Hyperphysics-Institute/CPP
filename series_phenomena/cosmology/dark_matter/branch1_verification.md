# BRANCH 1 VERIFIED — TRAVELLING DI-BITS GIVE BALLISTIC, 1/r², ISOTROPIC, RETARDED

**Patch 2895. This discharges the verification registered as OWED (not
claimed) at Patch 2894 §8.**

---

## §1 — WHY THIS WAS RUN RATHER THAN ASSERTED

Patch 2894 concluded that Branch 1 — DI-bits as travelling conserved
entities — gives 1/r² "from conservation plus spherical spreading," and
explicitly declined to claim it: *"'follows by construction' is what was
said about several things this session that then failed on measurement."*

**Good instinct: the first test nearly produced a false confirmation.**

## §2 — THE NEAR-MISS, RECORDED BECAUSE IT ALMOST PASSED

Steady-state **shell-averaged** radial density
(`code/2895_branch1_radial_profile.py`), 60 Moments, 20k bits/Moment:

| emission scheme | slope [5,25] | slope [10,40] |
|---|---|---|
| continuum directions | −2.064 | −2.041 |
| lattice-binned | −2.038 | −2.013 |
| **12 FCC rays** | **−2.025** | **−2.026** |

**All three give −2.0, including the 12-ray case — which is precisely the
configuration flagged at Patch 2889 §7 as FAILING to produce a continuous
1/r² field.**

**Diagnosis: shell-averaged density is 1/r² by conservation alone.** Bits
per shell is constant while shell volume grows as r², so **any** conserved
ballistic flux returns −2, whether the field is smooth or confined to
rays. **The observable measures geometry, not field structure, and cannot
discriminate.**

**Had this been reported as the verification, it would have been the
fourth false confirmation of the session** — and of exactly the
established shape: a number landing on the physically expected value,
accepted without interrogating what produced it.

## §3 — THE DISCRIMINATING TEST: ANGULAR ISOTROPY

A physical force law requires the field to be **isotropic at fixed
radius** — a test charge sitting off a ray must still feel a force.
Measured as the coefficient of variation across **equal-area solid-angle
patches** (equal-area in cos θ, 8×16 patches), deliberately avoiding the
lattice-shell binning that produced the symmetry artifact at Patch 2891.

| emission scheme | r=15 | r=25 | r=35 |
|---|---|---|---|
| continuum directions | 0.026 | 0.023 | 0.026 |
| **lattice paths to full PSR shell** | **0.024** | **0.022** | **0.023** |
| 12 FCC edge directions only | **3.109** | **3.109** | **3.109** |

**Poisson noise floor for these counts is ≈ 0.025.** The first two sit
**at** the noise floor — genuinely isotropic. The 12-direction case sits
**two orders of magnitude above** it, and is **constant in radius**: the
rays are exactly radial, so the angular structure is scale-invariant and
**never fills in at any distance.**

## §4 — THE ACTUAL DISCRIMINATOR IS NOT LATTICE vs CONTINUUM

**It is whether bits are emitted toward the WHOLE PSR SHELL or only along
the 12 edge directions.**

Bits travelling along lattice edges toward arbitrary shell GPs are
**isotropic to the noise floor** (0.023). The lattice is not the problem.

**The founder's specification says the whole shell** — *"re-radiates the
SSV_net to the spherical shell that is at the distance that is present at
each local SSV_abs (the PSR/l_P)"*, and *"the DI bits transit all the
edges between all GPs between GP_origin to GP_PSR."*

**The 12-direction restriction was the worker's, inherited from the 2802
kernel and carried unexamined through every engine of this arc** —
convolution (2887), directed relay (2889), σ-family (2890), coherent rule
(2892), obliquity family (2894). **The ray problem registered at 2889 §7
as a defect of Branch 1 was a defect of the worker's 12-neighbour
implementation, not of the specification.**

## §5 — BRANCH 1 STATUS: ALL FOUR PROPERTIES

| property | status | source |
|---|---|---|
| **Ballistic** (p = 1.0000 exactly) | ✓ | Patch 2889, direct measurement |
| **Light cone** (invariant) | ✓ | Patches 2890, 2892, 2894 — three confirmations, no fitting |
| **1/r² shell-averaged** | ✓ | §2 — but note this is conservation+geometry, weak |
| **Isotropic** (smooth field) | ✓ | §3 — the discriminating test |
| **Retarded** | ✓ | by construction: a bit arriving at r carries the source state from r/c ago |

**CONJ-FP-1 Condition B is satisfied under Branch 1: the relay is retarded
and NOT Liénard–Wiechert.** A travelling-bit shell carries the source's
*past* state; there is no mechanism producing the LW cancellation, which
requires the field to point at the instantaneous position.

## §6 — WHAT REMAINS OPEN

**Condition B closes; the conjecture does not.** Still open:

- **CONDITION A** — the sign of the Sea's response (repulsive → forward
  drive; attractive → drag). Untested.
- **LINK 2** — the marginality condition C·PSR = SSV_abs. Never computed.
- **LINK 3** — stability of the coasting family (B1). No panel seat can
  execute it; the worker's own job.
- **Statics claims** remain suspended per Patch 2892 (background
  contamination). §2 here does **not** lift that: it is a particle-count
  measurement with no background, and is not a substitute for a field
  steady-state measurement.

## §7 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/DM-2/DM-3; Candidate (B) 79.5%. G1 and P-A2-1 stand.
