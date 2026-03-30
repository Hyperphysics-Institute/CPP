# Mechanism — SM-4: Charged Lepton Masses from the K3 Spectral Theorem

**Paper:** SM-4_charged_lepton_masses_from_k3.tex (v5)
**Last updated:** 30 March 2026

SM-4 applies the K3 Spectral Theorem (SM-3) to compute the three individual
charged lepton masses. The mechanism here is not a new derivation — the hard
work was done in SM-3. SM-4 is a parameter-counting paper: it shows exactly
what the K3 theorem determines (ρ = √2, hence the mass ratio constraint
K = 2/3), what remains free (the overall scale A and the Koide phase θ),
how those free parameters are calibrated, and why θ cannot in principle be
derived from within the K3+SSV framework. The structural impossibility
theorem for θ is the paper's deepest result.


## Part 1: What SM-3 Left Open

SM-3 proved K = 2/3 exactly from the K3 adjacency spectrum and thermal
equipartition. This is one constraint on three masses. The Koide
parametrisation writes the three square-root masses as:

    √mᵢ = A(1 + ρ cos φᵢ),   φᵢ = θ + 2πi/3,   i = 0, 1, 2

The three parameters in this representation are A (the overall mass scale),
ρ (the modulation depth), and θ (the Koide phase). SM-3 derived ρ = √2 from
the K3 eigenvalue ratio. Two parameters remain: A and θ. With three masses
and one constraint (K = 2/3, equivalent to ρ = √2), the system has two
degrees of freedom. SM-4 addresses both.


## Part 2: The Scale Parameter A

The scale A sets how large the masses are in physical units. It is defined
by the electron mass:

    A = √m_e / (1 + √2 cos θ)

Since θ is separately determined (from calibration), A is set by m_e alone —
one calibration to one mass. Once A is fixed, the muon and tau masses follow
from the Koide parametrisation:

    m_μ = (A + √2 A cos(θ + 2π/3))²
    m_τ = (A + √2 A cos(θ + 4π/3))²

A is a calibration constant, not a derived result. Its physical meaning is
the overall energy scale of the ZBW resonator in physical units. Why A has
the value it has — why the electron mass is 0.511 MeV rather than 5.11 MeV
or 0.0511 MeV — is equivalent to asking why the ZBW hopping energy ℏω₀
corresponds to this particular physical mass scale. This connection is an
open problem (related to OPEN-P-QM-new-1, the derivation of ℏ from CPP
statistics).


## Part 3: The Koide Phase θ and the Consistency Check

The Koide phase θ is extracted from all three PDG lepton masses
simultaneously. Using PDG 2024 values:

    m_e = 0.51099895 MeV,   m_μ = 105.6583755 MeV,   m_τ = 1776.86 MeV

The extracted values are:

    A = (√m_e + √m_μ + √m_τ)/3
    θ = 132.7323°  (equivalently, 2.31663 radians)

The consistency check: with ρ = √2 (from SM-3) and A, θ from the above
calibration, the Koide parametrisation reproduces:

    m_e:   0.51100 MeV (input)
    m_μ:   105.654 MeV vs PDG 105.658 MeV (0.004% error)
    m_τ:   1776.87 MeV vs PDG 1776.86 MeV (0.001% error)

The 11 ppm overall consistency confirms that nature's three charged lepton
masses lie on the Koide circle with ρ = √2 to high precision. This is the
empirical content of SM-4: not a prediction but a consistency check showing
that the K3 theorem's constraint is satisfied by the real masses.

The 0.004% and 0.001% residuals reflect the precision to which nature
satisfies K = 2/3, not the precision of a CPP calculation. Since ρ is
derived and A, θ are calibrated from the same data, the only non-trivial
content is that a single K = 2/3 constraint (with two calibrated parameters)
is consistent with the measured masses to 11 ppm. This would fail if the
masses were independently drawn from any reasonable prior.


## Part 4: The Structural Impossibility of Deriving θ

The most important result in SM-4 is not the consistency check but the
proof that θ cannot in principle be derived from the K3+SSV framework.

The proof works through the Löwdin downfolding argument. The full tetrahedral
cage has four vertices: the apex V₄ and the three base vertices {V₁, V₂, V₃}.
When the apex is integrated out (Löwdin downfolding from K₄ to K₃), the
effective Hamiltonian on the base triangle acquires a correction term:

    H_eff(E) = A_{K₃} − (1/E) v vᵀ

where v = (1,1,1)ᵀ/√3 is the bonding eigenvector of K₃. The key observation
is that the antibonding eigenvectors φ₋ of K₃ are orthogonal to v by
definition — they are orthogonal to (1,1,1). Therefore ⟨φ₋|v⟩ = 0 exactly.
The downfolding correction v vᵀ is zero in the antibonding subspace.

The antibonding eigenvalues remain exactly −1 regardless of E. The
two-dimensional antibonding subspace is never split by this correction.
No value of the energy E can break the degeneracy in the antibonding plane.

Since C3 symmetry permutes the two antibonding states into each other, any
C3-symmetric perturbation also leaves the degeneracy intact. The antibonding
degeneracy is exact and structural — it is a consequence of C3 symmetry, not
an accident of a particular interaction strength.

θ is a parameter within the antibonding subspace (it specifies the direction
within the 2D antibonding plane that each lepton generation points). Because
the antibonding subspace is never split by K3+SSV perturbations, θ is
unconstrained within this framework. This is not a gap in the analysis; it
is a structural feature of K3 proved as a theorem.


## Part 5: The Critical Angle and Its Physical Significance

The Koide phase θ = 132.73° is close to the critical value
θ_c = 3π/4 = 135°. At θ = θ_c, the electron mass vanishes:
(1 + √2 cos θ_c) = 0 exactly, since cos(3π/4) = −1/√2. The electron is
the lightest charged lepton precisely because θ is close to but not equal
to θ_c.

The deviation θ_c − θ = 2.27° is empirical — no CPP mechanism currently
explains it. The correction is of second order in the SSV coupling:
θ_c − θ ≈ (5/4) × sea_strength² (empirical coefficient 5/4, not derived).
This suggests a perturbative correction to the K3+SSV energy landscape from
a higher-order SSV interaction, but the specific mechanism is open.

The physical significance: the electron's non-zero mass is the result of θ
being slightly displaced from the zero-mass critical angle. The electron is
not massless by an arbitrary calibration — it is nearly massless because θ
is close to θ_c, and the 2.27° displacement from θ_c is a small but
non-zero physical quantity requiring explanation.


## Part 6: Parameter Summary

The full parameter accounting for the lepton mass problem across SM-3 and SM-4:

Starting parameters: three (m_e, m_μ, m_τ — any three numbers in principle)
SM-3 derives: ρ = √2 from the K3 eigenvalue ratio — reduces three parameters to two
SM-4 calibrates: A from m_e (one experimental input, reduces to one free parameter)
SM-4 calibrates: θ from all three PDG masses (remaining parameter, proved not derivable from K3+SSV)
Open: θ requires EW sector (OPEN-P-SM-7d)

When OPEN-P-SM-7d is solved, the lepton mass problem will be fully determined
from one calibration (A from m_e) plus derived quantities (ρ from SM-3,
θ from EW sector). This would constitute a complete near-parameter-free
derivation of all three lepton masses from CPP geometric inputs, with only
the absolute energy scale requiring experimental calibration.


## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|---------------|
| K3 theorem recap | §1 (Prerequisites) |
| Koide parametrisation with ρ = √2 | §2, Theorem 1 |
| Parameter counting | §2, Remark (counting free parameters) |
| 11 ppm consistency check | §3, Proposition |
| Nature of consistency check | §3, Remark |
| Structural theorem for θ | §4, Theorem 2 |
| Löwdin downfolding proof | §4, Theorem 2 proof |
| Three θ candidates | §4, Remark |
| Critical angle θ_c = 3π/4 | §4, Remark (electron is lightest lepton) |
| Open problems | §5 |
| Summary table | §6 |
