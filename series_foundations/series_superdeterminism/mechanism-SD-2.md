# Mechanism — SD-2: H₄ Angular Structure of the Nexus Correction

**Paper:** SD-2 (cpp_sd2_h4_angular_structure_v1.tex)
**Last updated:** 31 March 2026

---

## Part 1: The Problem SD-2 Solves

SD-1 established that the CPP correction to Bell correlations takes the form E_CPP = −cos θ + ε × f_{H₄}(θ) + O(ε²), but left f_{H₄} as an unknown function. SD-2 derives the functional form of f_{H₄} from the symmetry of the 600-cell lattice, using only group theory and the established CPP geometry — no new CPP calculations needed.

---

## Part 2: D₅ Projected Symmetry (Theorem 1)

**Step 1 — H₄ symmetry projects to D₅ on the measurement-angle circle.**
The 600-cell has Coxeter group H₄ of order 14,400. When the measurement angle θ = θ_A − θ_B is treated as a coordinate on the circle S¹, the H₄ action on the 600-cell projects to a residual symmetry on this circle. THEO-SD-1 (D₅ projected symmetry): the projected symmetry group on the measurement-angle circle is the dihedral group D₅ — the symmetry group of the regular pentagon, order 10.

**Step 2 — D₅ symmetry forces the leading Fourier term to be cos(5θ).**
D₅ has a 5-fold rotation axis. Any function on S¹ that is D₅-invariant must have Fourier components at multiples of 360°/5 = 72°. The leading non-trivial Fourier mode consistent with D₅ symmetry is cos(5θ), corresponding to the 5-fold icosahedral structure of the 600-cell.

---

## Part 3: Fourier Decomposition (Theorem 2)

**Step 3 — The full angular function has a specific Fourier series.**
THEO-SD-2 (Fourier decomposition of f_{H₄}):

    f_{H₄}(θ) = A₅ cos(5θ) + A₃ cos(3θ) + A₁₀ cos(10θ) + ...

where:
- The 5n-fold terms (cos 5θ, cos 10θ, ...) arise from the 5-fold icosahedral symmetry of H₄
- The 3-fold term (cos 3θ) arises from the independent tetrahedral cell symmetry of the 600-cell (each 600-cell face is a tetrahedron, giving a separate C₃ contribution)
- Higher harmonics are suppressed by φ^{-n} factors from the golden-ratio geometry

**Step 4 — A₅ is conjectured to equal φ⁻³/(2π).**
The amplitude of the leading correction A₅ is conjectured to be the same geometric dilution factor φ⁻³ ≈ 0.236 that governs the electroweak boson masses in the EW series. This would make the angular correction a consequence of the same 600-cell volume ratio that was derived without free parameters in EW-1. Proof requires the full Nexus correlation function K (SD-4).

---

## Part 4: H₄-Special Angles and the CHSH Blind Spot (Theorems 3–4)

**Step 5 — H₄-special angles are the extrema of f_{H₄}.**
THEO-SD-3: The local extrema of f_{H₄} occur at the golden-ratio angles of the 600-cell:

    θ ∈ {36°, 60°, 72°, 90°, 108°, 120°, ...}

These are the angles where cos(5θ) and cos(3θ) have simultaneous extrema — the directions of highest and lowest CPP correction.

**Step 6 — CHSH optimal angles are not H₄-special.**
THEO-SD-4 (CHSH blind spot): The CHSH-optimal angle θ = 45° is not an H₄-special angle. Proof: cos(45°) = 1/√2 ∉ ℚ(φ) — it cannot be expressed as a rational function of the golden ratio φ, which is the algebraic closure of the 600-cell vertex coordinates. Therefore θ = 45° is not an extremum of f_{H₄}. The four CHSH angles {0°, 45°, 90°, 135°} are all non-H₄-special, making the standard CHSH test the worst possible experiment for detecting the CPP angular correction.

**Step 7 — The optimal experiment is a continuous angular scan.**
The CPP signal is maximal when θ is scanned continuously across [0°, 180°] with angular resolution better than ~5°. The ratio test δE(36°)/δE(120°) ≈ −1.065 is a dimensionless prediction that does not depend on the unknown amplitude A₅ — it tests the angular structure alone and is falsifiable at precision ~ ε × 10⁻² ~ 10⁻²⁸.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–2: D₅ projected symmetry | §3, THEO-SD-1 |
| Steps 3–4: Fourier decomposition | §4, THEO-SD-2, Amplitude Conjecture |
| Steps 5–6: H₄-special angles and CHSH blind spot | §5, THEO-SD-3, THEO-SD-4 |
| Step 7: optimal experiment | §6 (Experimental Programme) |
