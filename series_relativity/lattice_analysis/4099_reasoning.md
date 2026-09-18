# 4099 — BC helix bundle z=12 test (SR/EW cross-lane)

**STATUS:** at-patch, verbatim. **Lane:** SR (cross-lane EW). **Session:** 233.
**Trigger:** Session 232 handover §5(c): "Can BC helices be bundled to fill 3-space at z=12?"

## The computation and the result

Single BC helix:
- Twist φ = arccos(-2/3) ≈ 131.81° (irrational multiple of 2π — never closes)
- r = 3√3/10 ≈ 0.5196, h = 1/√10 ≈ 0.3163
- Perfect regular tetrahedra (all edges exactly 1)
- z = 6 per interior vertex

The bundling attempt: 7-helix configuration (1 central + 6 at distance D).

For unit cross-helix bonds: D = 1 (corresponding vertices at d=1 exactly).
For no interpenetration: D > 2r = 2×0.5196 = 1.039.

2r = 1.039 > 1 = D_required. **These are mutually exclusive.** QED.

At D=1: minimum inter-vertex distance = 0.320 (severe interpenetration, confirmed by exhaustive search over 40 interior vertices × 16 window).

At D=1.2 (> 2r): near-zero unit-distance cross-bonds (0.125 per vertex). z ≈ 6 total.

Analytic reinforcement: cross-bond lengths at any D vary with vertex index n (incommensurate twist). No D gives uniform unit-distance cross-bonds for all n simultaneously.

## What the result means for CPP

The same geometric frustration that prevents flat tiling of ℝ³ with regular tetrahedra at z=12 (7.36°/edge angular deficit, established in 4019) also prevents BC helix bundles from achieving z=12 without overlap. The frustration manifests as the inequality 2r > edge length.

The 4020 variable-position-GP ruling (slight distortion, accepted by the founder) remains the only viable path for local z≈12 in flat space.

## Chirality note (retained value of BC helix)

BC helices ARE chiral (definite handedness, confirmed by 3-hop path determinant test: chirality = +1.000 and mirror = -1.000). The K2 chirality value is confirmed — a BC helix bundle gives local chiral structure. But it doesn't determine WHICH hand is realised, and it doesn't deliver z=12.

## Convenient branch check

The result closes the K2 route as a z=12 lattice solution. This is the INCONVENIENT branch (the campaign was hoping for a positive result that would "dissolve the tiling problem and retire the 4020 variable-position-GP ruling"). The inconvenient result: it doesn't. The 4020 ruling stands.
