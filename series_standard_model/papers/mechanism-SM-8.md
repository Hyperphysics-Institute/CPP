# Mechanism — SM-8: Quark Generation Structure from 600-Cell Distance Shells

**Paper:** SM-8 v4.1 (9 April 2026)
**Series:** Standard Model

---

## 1. What SM-8 builds on

SM-8 builds on SM-6 (charged-lepton spectrum from edge-mode traces) and SM-7 (heavy-quark spectrum from cage-level self-energy shifts and the Koide route). It introduces a different geometric feature — the **distance-shell structure** of the 600-cell — as the origin of quark generations and masses.

## 2. The four bonded shells

Starting from any vertex of the 600-cell, the 119 remaining vertices sort into 8 distance shells. Of these, only four contain lattice edges (nonzero adjacency): Shell 1 (icosahedron, V=12, E=30), Shell 2 (dodecahedron, V=20, E=30), Shell 4 (icosidodecahedron, V=30, E=60), plus the tetrahedral cells (V=4, E=6) that form the 600-cell's building blocks.

Shell 3 (V=12) contains **zero edges** — the structural gap. This is a forced combinatorial property of the 600-cell, not an assumption.

## 3. Cage-quark correspondence

The four bonded shells map one-to-one to the four heavy quarks via the unique order-preserving bijection (larger cage → heavier quark): tetrahedron → strange, icosahedron → charm, dodecahedron → bottom, icosidodecahedron → top.

## 4. The zero-parameter mass formula

The mass formula is:

```
M_q = m_e × (z/φ) × V^(7/3)              for q = s, c, b
M_t = m_e × (z/φ) × V_t^(7/3) × z·C_F   for q = t
```

where m_e = 0.511 MeV (electron mass), z = 12 (600-cell coordination), φ = golden ratio, C_F = 4/3 (SU(3) Casimir), and V ∈ {4, 12, 20, 30}.

Every constant is derived or measured elsewhere in the CPP series:
- m_e from SM-6 (lepton spectrum)
- z, φ from SR-1 (lattice geometry)
- C_F from SS-2 (colour algebra)
- V from SM-8's own shell enumeration
- 7/3 from SM-9 (pair model)

## 5. The Shell 3 gap mechanism

Pre-gap quarks (s, c, b) have cages connected to the central vertex by direct lattice edges. Post-gap (top) requires chains to tunnel through the edgeless Shell 3 via the z = 12 coordination bonds of the ambient lattice. Each coordination bond carries the bare SU(3) vertex factor C_F = 4/3, giving a total post-gap multiplier of z × C_F = 16.

## 6. The palindrome and three generations

The distance shells exhibit mirror symmetry: Shell 7 = Shell 1 (icosahedron), Shell 6 = Shell 2 (dodecahedron), Shell 5 = Shell 3 (gap). In the tessellated lattice, the outer shells are identified with the inner shells of neighbouring 600-cells. No new particle species can form — the Standard Model has exactly three generations.

## 7. The charge census

At the 2/3 attractive fraction assignment: eDP:qDP:hDP:repulsive = 1:1:2:2. This ratio is combinatorial and independent of cage geometry. The attractive fraction 2/3 appears across all cages.

## 8. Mathematical correspondence

| Mechanism step | Paper section |
|---------------|--------------|
| Shell enumeration | §3 (Theorem 3.1) |
| Cage-quark map | §4 |
| Zero-parameter formula | §6.3 (Theorem 6.1) |
| Gap mechanism | §7, Appendices A–C |
| Palindrome/generations | §8 (Theorem 8.1) |
| Charge census | §9 |
| Anticipated criticisms | §10 |

---

*Document prepared by Thomas Lee Abshier ND and Claude Opus (Anthropic), 9 April 2026.*
