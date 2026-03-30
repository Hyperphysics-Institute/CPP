# Glossary — SM-4: Charged Lepton Masses from the K3 Spectral Theorem

**Paper:** SM-4_charged_lepton_masses_from_k3.tex (v5)
**Last updated:** 30 March 2026

Terms defined as they function in SM-4 specifically. SM-4 introduces the
full Koide parametrisation with calibrated A and θ, proves the structural
impossibility of deriving θ from K3+SSV, and establishes the critical angle
θ_c = 3π/4. Terms defined in SM-3 (K₃, eigenvalues, K, ρ, the Koide circle)
are cross-referenced rather than repeated.


## Section 1: The Koide Parametrisation in Full

**Koide parametrisation (full form)**
The representation of three lepton square-root masses as points on a circle:
√mᵢ = A(1 + ρ cos φᵢ), with φᵢ = θ + 2πi/3 for i = 0, 1, 2. Three
parameters fully specify the three masses: A sets the overall mass scale,
ρ sets the fractional variation around the circle, and θ sets the angular
position of the electron on the circle. SM-3 derived ρ = √2. SM-4 calibrates
A and θ from PDG mass data. When OPEN-P-SM-7d is solved, θ will be derived
from the EW sector, leaving A as the only calibrated parameter.

**Scale parameter (A)**
The amplitude in the Koide parametrisation, with units of √(MeV). A sets the
overall mass scale of the lepton sector. Once θ is known, A is determined by
the electron mass alone: A = √m_e/(1 + √2 cos θ). The geometric meaning:
A = (√m_e + √m_μ + √m_τ)/3, the arithmetic mean of the three √mᵢ values.
Deriving A from CPP primitives requires relating ℏω₀ ≈ 87.8 MeV to the
observed electron mass, connecting to OPEN-P-QM-new-1.

**Koide phase (θ)**
The angular parameter in the Koide parametrisation that determines the
lepton mass hierarchy. θ = 0 gives degenerate masses; θ = 3π/4 gives a
massless electron; θ = 132.73° gives the observed hierarchy m_e << m_μ << m_τ.
θ is calibrated from PDG masses in SM-4. Its derivation requires the
electroweak sector (OPEN-P-SM-7d).

**Critical angle (θ_c = 3π/4 = 135°)**
The value of the Koide phase at which the electron mass vanishes exactly.
At θ = θ_c: cos(3π/4) = −1/√2, so (1 + √2 cos θ_c) = 0, hence m_e = 0.
The electron is nearly massless because θ = 132.73° is close to θ_c = 135°.
The 2.27° deviation from θ_c is the physical quantity encoding the electron's
non-zero mass. The critical angle is a derived consequence of ρ = √2, not
an additional assumption.


## Section 2: The Structural Impossibility Theorem

**Löwdin downfolding**
A technique for eliminating a subset of degrees of freedom from a
Hamiltonian, producing an effective Hamiltonian on the remaining subspace.
In SM-4 Theorem 2, the apex vertex V₄ of the tetrahedral cage is integrated
out (downfolded), producing an effective Hamiltonian on the base triangle K₃:

    H_eff(E) = A_{K₃} − (1/E) v vᵀ

where v = (1,1,1)ᵀ/√3 is the bonding eigenvector. The downfolding is exact
within the K4 cage structure.

**Antibonding subspace (of K₃)**
The two-dimensional subspace of ℝ³ spanned by the two antibonding
eigenvectors of K₃ — those orthogonal to (1,1,1)/√3. Any antibonding vector
satisfies v₁ + v₂ + v₃ = 0. The Koide phase θ parameterises a direction
within this plane. Because the antibonding subspace is two-dimensional, θ
can rotate freely within it — it is a continuously variable angular parameter
with no preferred value from the K3 structure alone.

**Apex darkness to antibonding modes**
The key lemma in Theorem 2: ⟨φ₋|v⟩ = 0 exactly for any antibonding
eigenvector φ₋, where v = (1,1,1)ᵀ/√3 is the apex-to-base coupling vector.
The apex couples equally to all three base vertices (C3 symmetry), and any
equal-coupling vector is proportional to (1,1,1) — which is exactly the
bonding eigenvector, orthogonal to all antibonding vectors. Therefore the
Löwdin correction v vᵀ has zero matrix element in the antibonding subspace.
The antibonding eigenvalues remain exactly −1 for all energies E.

**Antibonding degeneracy (exact)**
The exact equality of the two antibonding eigenvalues of K₃ (both −1),
preserved by all K3+SSV perturbations. This degeneracy is protected by C3
symmetry: C3 rotation maps one antibonding eigenvector to the other, so
any C3-invariant perturbation assigns them identical eigenvalues. The
degeneracy is structural — it cannot be broken by any mechanism that
preserves the three-fold rotational symmetry of the base triangle.

**Structural impossibility (of θ from K3+SSV)**
The proved result (Theorem 2) that no mechanism within the K3+SSV framework
can determine θ. θ parameterises a direction within the antibonding subspace,
and this subspace is exactly degenerate under all K3+SSV perturbations. A
degenerate subspace has no preferred direction — no mechanism can select θ
without physics outside the K3+SSV framework. This is a structural
impossibility, not a computational gap.


## Section 3: Physical and Numerical Results

**11 ppm consistency check**
The result that the Koide parametrisation with ρ = √2 and calibrated A, θ
reproduces the three PDG lepton masses to 11 ppm overall (0.004% for m_μ,
0.001% for m_τ, with m_e as input). This is a consistency check — not a
prediction — because A and θ are both calibrated from the same PDG data. The
non-trivial content is that one derived constraint (K = 2/3) plus two
calibrated parameters suffices to reproduce three masses to high precision.

**Two free parameters (A and θ)**
The parameter count for the lepton mass problem after SM-3:

    Before SM-3:      3 free parameters (m_e, m_μ, m_τ)
    After SM-3:       2 free parameters (ρ = √2 derived, K = 2/3 constraint)
    After SM-4:       0 free parameters (A, θ calibrated from PDG)
    After EW (goal):  1 calibrated parameter (A from m_e; θ derived from EW)

**θ = 132.7323° (calibrated)**
The numerical value of the Koide phase extracted from PDG 2024 masses.
Equivalently 2.31663 radians. Not predicted by CPP — extracted from
measurement. Its explanation is OPEN-P-SM-7d.

**θ_c − θ = 2.27° (empirical)**
The angular distance from the observed θ to the critical angle. Empirically
consistent with θ_c − θ ≈ (5/4) × sea_strength² ≈ 0.040 rad ≈ 2.3°,
where sea_strength ≈ 0.178 (derived in SS-1). The coefficient 5/4 is not
derived; if confirmed theoretically, it would identify this as a second-order
SSV correction.


## Section 4: Open Problems

**OPEN-P-SM-7d — Derive θ = 132.73°**
Derive the Koide phase from CPP dynamics. Three candidate mechanisms:
(1) Aharonov-Bohm self-energy from the ZBW orbital loop on the K3 triangle;
(2) non-uniform apex coupling from higher-order 600-cell SSV corrections;
(3) EW sector connection, possibly related to the PMNS CP-violating phase.

**OPEN-P-SM-7e — Why exactly three lepton generations?**
The K3 spectral theorem is specific to N=3. A derivation of why the stable
lepton cage has exactly three base vertices — and not two or four — is open.

**Open connection — A and ℏω₀**
The scale parameter A should be derivable from the ZBW hopping energy
ℏω₀ ≈ 87.8 MeV (SM-3) and the 600-cell geometry. The formal connection
between A (in √MeV) and ℏω₀ (in MeV) through the Koide parametrisation
would close the gap between SM-3's energy scale and SM-4's mass scale.
