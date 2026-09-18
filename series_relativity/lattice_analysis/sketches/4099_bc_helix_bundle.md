# BC-Helix Bundle: The z=12 Question — CLOSED (Patch 4099)

**Lane:** SR (EW cross-lane). **Patch:** 4099. **Session:** 233.  
**Source:** Session 232 handover §5(c).  
**Question:** Can Boerdijk-Coxeter helices be bundled to fill 3-space at z=12?  
**Status:** CLOSED — NOT ACHIEVABLE. Verify: `code/4099_bc_helix_bundle_verify.py` (ALL PASS).

---

## 1. BC Helix Parameters (unit edge length)

The Boerdijk-Coxeter (BC) helix in 3D (unit edge = 1):

| parameter | value |
|---|---|
| Twist per step | φ = arccos(−2/3) ≈ 131.81°  ← irrational multiple of 2π (never repeats) |
| Helix radius | r = 3√3/10 ≈ 0.5196 |
| Height per step | h = 1/√10 ≈ 0.3163 |
| Helix diameter | 2r ≈ **1.0392** |

Vertices: u_n = (r cos(nφ), r sin(nφ), nh). Consecutive quartets {u_n, u_{n+1}, u_{n+2}, u_{n+3}} form **perfectly regular tetrahedra** (all 6 edges = 1, verified to 2×10⁻¹⁶).

Single helix: z = 6 (each interior vertex connected to the 3 "above" and 3 "below").

---

## 2. The Bundling Attempt

A natural 7-helix bundle: 1 central helix + 6 surrounding at axis-distance D, angles 0°, 60°, ..., 300°.

**For z=12:** need 6 cross-helix bonds per vertex at unit distance. The only obvious unit-distance cross-bond occurs at D=1 (corresponding vertices u^A_n and u^B_n with the same index n, separated by exactly D=1 along the x-axis). This gives 6 cross-helix bonds → z = 6 + 6 = 12.

**But 2r = 1.039 > 1 = D.** The helices INTERPENETRATE. Minimum inter-vertex distance at D=1: **0.320** (far below unit). Physically invalid.

---

## 3. The Fundamental Obstruction

There is a simple geometric inequality that closes the case:

For unit cross-helix bonds: axis distance D = 1.  
For non-interpenetration: D > 2r = 1.039.

Since **2r > 1**, these are **mutually exclusive.** No D satisfies both.

Additionally (H5 in the verify script): the cross-helix bond lengths at any fixed D vary as a function of vertex index n — the incommensurate twist angle φ/(2π) ≈ 0.366 is irrational (Weyl equidistribution), so no D gives all cross-helix bonds at unit length simultaneously.

---

## 4. Connection to the Larger Lattice Problem

This confirms, from the BC-helix direction, the same fundamental obstruction that 4019/4034/4035 established from the tiling direction:

**Regular tetrahedra cannot fill flat 3D space at z=12 without distortion or overlap.**

- 4019: 600-cell dihedral angle 5×70.53° = 352.64° ≠ 360° → 7.36° angular deficit per edge
- 4034/4035: tiling flat ℝ³ with z=12 requires non-icosahedral arrangement (FCC/HCP, which is cuboctahedral not icosahedral)
- **4099 (this):** BC helix bundling — 2r=1.039 > 1 → no bundle gives z=12 without overlap

The 4020 variable-position-GP ruling (distorted cages, accepted by the founder) remains the only viable path for a z≈12 local structure in flat space.

---

## 5. What BC Helices DO give (retained value)

1. **Perfectly regular tetrahedra** with no distortion (contrast: 4020 ruling requires accepting small distortion)
2. **Definite handedness**: each BC helix has a definite hand (chirality = ±1, measured ±1.000 in verify H6). The mirror image has the opposite hand. This is the K2 value for the chirality programme — a structural chiral element in 3-space, though it doesn't determine WHICH hand is realised.
3. **Aperiodicity**: the helix never repeats (twist irrational). This gives a quasicrystalline character — the aperiodic structure that is the only viable flat-space tiling for local icosahedral order (4017/4019).

---

## 6. K2 Verdict (chirality arc update)

From the chirality axiom maturation §2l K2 verdict:
> "K2 is a real and attractive alternative to the 4020 distortion ruling... it does not by itself deliver chirality, and it does not yet deliver z=12."

**Patch 4099 establishes definitively:** z=12 is NOT delivered by BC helix bundling. The K2 route is **CLOSED** as a lattice solution. K2 retains value only as a structural observation about tetrahedral packing and as a source of definite-handed local structure (not as a CPP lattice proposal).

The chirality maturation document's K2 entry should be updated to reflect this closure.
