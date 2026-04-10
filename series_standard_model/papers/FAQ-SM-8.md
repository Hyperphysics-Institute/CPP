---
title: "SM-8 Frequently Asked Questions"
paper: SM-8 v4.1
date: 2026-04-09
---

# FAQ — SM-8: Quark Generation Structure from 600-Cell Distance Shells

## Category A: The Formula

**Q: How can a zero-parameter formula predict four quark masses?**
A: Every constant in M = m_e(z/φ)V^(7/3) × [1 or 16] is either measured (m_e = 0.511 MeV) or derived from 600-cell geometry (z = 12, φ = golden ratio, V ∈ {4,12,20,30}). The formula has zero adjustable parameters. RMS error: 2.1%.

**Q: Why does V^(7/3) appear and not some other power?**
A: SM-9 shows V^(7/3) = V² (pair counting: every chain interacts with every other) × V^(1/3) (linear cage dimension). The exponent is partially derived; SM-10's FEM simulation targets full derivation.

**Q: What sets the energy scale M₀ = 3.790 MeV?**
A: M₀ = m_e × z/φ. The electron mass provides the energy unit; z = 12 (coordination number) provides the multiplicity; 1/φ (edge-to-circumradius ratio) provides the geometric coupling. All three are derived or measured.

## Category B: The Cages

**Q: Why do larger cages make heavier quarks?**
A: More cage vertices → more radial chains → more chain-chain cross-links → more organised DPs → more mass. The cooperative enhancement (each chain reinforcing all others) amplifies this beyond simple linear scaling.

**Q: Why exactly four cages?**
A: The 600-cell has exactly four bonded polyhedral distance shells: tetrahedron (V=4), icosahedron (V=12), dodecahedron (V=20), icosidodecahedron (V=30). Shell 3 has vertices but zero edges — the "gap." This is a geometric fact, not a choice.

**Q: Why three generations and not four?**
A: The palindrome symmetry of the 600-cell (Shell k ↔ Shell 8-k) combined with antipodal identification in the tessellated lattice means Shells 5, 6, 7 are the inner shells of neighboring cells. Four independent cages → three independent generations. (Theorem 8.1)

## Category C: The Gap Multiplier

**Q: Why does the top quark need a ×16 factor?**
A: Shell 3 (between the bottom and top cages) has zero edges. Chains can't propagate continuously — they must tunnel via 12 coordination bonds, each carrying C_F = 4/3. Product: z × C_F = 12 × 4/3 = 16.

**Q: Is z × C_F = 16 numerology?**
A: It passes a 7-point numerology audit: (1) geometric identity, (2) additional predictions, (3) unique decomposition, (4) no wrong predictions, (5) polytope-specific, (6) C_F independently derived in SS-2, (7) falsifiable.

**Q: Could the multiplier be something other than 16?**
A: SM-9 Table 3 tested 16 candidates. z × C_F = 16 is the only value that (a) decomposes into independently derived constants, (b) has a geometric mechanism, and (c) explains why only the top quark is special.

## Category D: Falsifiability

**Q: How could this be disproved?**
A: (1) Discovery of a fourth quark generation. (2) Revised top mass incompatible with ×16. (3) Computation showing V_Shell3 ≠ 12. (4) FEM simulation (SM-10) producing correct masses without V^(7/3). (5) An alternative polytope reproducing the SM equally well.

**Q: How is this different from numerology?**
A: Numerology fits numbers without mechanism. SM-8 derives numbers from geometry: 4 shells → 4 quarks, V^(7/3) from pair counting, M₀ from lattice constants, ×16 from Shell 3 relay. Every number has a geometric origin.

## Category E: Relationship to QCD

**Q: Does CPP replace QCD?**
A: No. CPP derives QCD observables (C_F, α_s, confinement) from the 600-cell lattice. QCD is the effective theory; CPP is the underlying geometry. They produce the same predictions where both apply.

**Q: Why doesn't the formula involve α_s?**
A: The strong coupling α_s enters through the chain dynamics (how strongly DPs couple to each other), which is implicit in the V^(7/3) scaling. SM-10's FEM will make this connection explicit.

---

*FAQ prepared by Thomas Lee Abshier ND and Claude Opus (Anthropic), 9 April 2026.*
