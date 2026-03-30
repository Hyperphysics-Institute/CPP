# Mechanism — SM-2: Mass Generation from Geometric Hierarchies in the 600-Cell Lattice

**Paper:** SM-2_mass_generation_geometric_hierarchies.tex (v30)
**Last updated:** 30 March 2026

*SM-2 is the quantitative mass table paper. Where SM-1 establishes
that cages exist and are stable, SM-2 asks: given the cage structure,
what are the actual particle masses? The mechanism here is a chain of
approximations — each step is honest about its level of exactness.
The reader should know going in: SM-2 is semi-empirical. One parameter
is calibrated (k ≈ 0.0185 to the electron mass), and several structural
assignments (N_k values) are motivated by geometry but not yet derived
from it. SM-2's strength is that one calibration propagates through
uniform rules to give consistent estimates for all 15 SM particles.*

---

## Part 1: The Mass Generation Problem

**Step 1 — The problem SM-1 left open.**
SM-1 established that cage binding energy scales approximately as
E ≈ (N/2) × SSV₀, where N is the number of cage vertices and
SSV₀ = 0.2555 MeV. The electron (N=4) gives exactly m_e = 0.511 MeV
by calibration. But the muon is not simply 3× heavier than the electron
(N_μ/N_e = 12/4 = 3 would give m_μ ≈ 1.53 MeV, not 105.66 MeV).
Something else is contributing significantly to particle masses beyond
the bare cage binding energy.

**Step 2 — Three additional contributions.**
SM-2 identifies four total contributions to a particle's rest mass:

    m c² = E_cage + E_ZBW + E_inter + E_cloud

E_cage: the SSV cage binding energy (SM-1's result, ≈ N/2 × SSV₀)
E_ZBW: the ZBW kinetic energy of the orbital Dipole Pair
E_inter: inter-layer bonding energy between nested cage shells
E_cloud: DP cloud energy from the polarised Dipole Sea around the cage

These four contributions, computed through uniform geometric rules
from one calibration constant, sum to the observed particle masses
within the accuracy of the framework.

---

## Part 2: The Planck-to-Particle Scale Bridge

**Step 3 — Why particle masses are so much less than the Planck scale.**
The Planck energy is E_P ≈ 1.22 × 10²⁸ MeV. The electron mass is
0.511 MeV. The ratio is ~10²⁸. Something must suppress the Planck-scale
ZBW energy by this enormous factor to produce the observed particle masses.

**Step 4 — The VEV formula: geometric suppression by lattice size.**
SM-2 proposes the vacuum expectation value:

    ⟨φ⟩ = k × E_P / N_lattice⁴ × φ_k

where N_lattice = 120 (600-cell vertex count), φ_k is a golden-ratio
generation factor, and k ≈ 0.0185 is the calibration constant.

The suppression factor N_lattice⁴ = 120⁴ ≈ 2.07 × 10⁸ is enormous
but far smaller than the required 10²⁸ suppression. The golden-ratio
factor φ_k handles the generation-specific portion. Together they
bridge the Planck scale to the MeV scale: the energy available per
particle is E_P divided by the fourth power of the lattice size —
each lattice dimension contributes one factor of N.

Physical interpretation: the Planck energy is the total computational
budget of the entire 600-cell per Absolute Moment. A particle uses a
fraction of this budget equal to 1/(N⁴) per Absolute Moment — the
fraction of all possible lattice states that its specific cage
configuration occupies. The particle's mass is the energy cost of
persistently occupying that fraction.

**Step 5 — The calibration constant k.**
k ≈ 0.0185 is fixed by setting the electron mass to 0.511 MeV. It is
motivated by the 600-cell geometry:

    k ~ 1/(N_lattice × φ²) ~ 0.00318

refined by generational averaging to 0.0185. The geometric motivation
is real — k is not a random number — but it is a calibration constant,
not a derived result. Whether k can be derived purely from 600-cell
geometry is OP-SM-1 (already solved to 3.8% via α_geom; the remaining
3.8% projection correction is OP-SM-2 domain).

---

## Part 3: Yukawa Couplings from Cage Geometry

**Step 6 — The effective cage occupancy N_k.**
Each particle is assigned an effective cage occupancy N_k, which
measures how many of the 120 lattice vertices its cage configuration
effectively uses. For the electron: N_k = 1 (minimal single-vertex
cage). For the muon: N_k = 4 (tetrahedral cage). For the tau: N_k = 12
(icosahedral cage). For quarks: N_k increases with cage depth.

These N_k values are motivated by the cage vertex counts from SM-1's
Table 1 but refined through calibration to PDG masses. The effective
occupancy is not simply the cage vertex count — it includes contributions
from inter-layer bonding and DP cloud terms. The exact derivation of N_k
from 600-cell geometry is OP-SS-1.

**Step 7 — The Yukawa coupling from geometry.**
The coupling of each particle to the vacuum field:

    y_k = φ^k × N_k / 120

where φ^k is the golden-ratio generation factor (φ¹ for first
generation, φ² for second, φ³ for third). The factor N_k/120
is the fraction of the full lattice used by the particle's cage.
The Yukawa coupling is not a free parameter per particle — it follows
from the cage geometry and the single constant k.

**Step 8 — Base mass from VEV and coupling.**
The base mass before refinements:

    m_base c² = y_k × ⟨φ⟩ = φ^k × N_k × k × E_P / (120 × N_lattice⁴) × φ_k

This is the leading-order result. For the electron: m_base ≈ 0.306 MeV
(calibration then adds the ZBW, inter-layer, and cloud corrections to
reach 0.511 MeV). The base mass captures the correct order of magnitude
for all particles from the same formula with the same k.

---

## Part 4: The Four Refinement Contributions

**Step 9 — ZBW energy contribution (E_ZBW).**
Every fermion carries an orbital ZBW Dipole Pair (SM-1 §8). The ZBW
kinetic energy adds to the base mass:

    E_ZBW = (1/2) m (c/r_eff)² × σ

where σ = 120^{−d} is the geometric suppression factor and r_eff
is the effective orbital radius. For d=0 (bound cage orbital), σ=1
and the ZBW contribution is a fixed fraction of the base mass. For
down-type quarks, the additional linear ZBW DP (d=1) adds a smaller
contribution with σ = 1/120. For neutrinos (d=3), σ = 120⁻³ produces
the ultra-small neutrino masses.

**Step 10 — Inter-layer bonding energy (E_inter).**
Particles with multiple cage shells (muon has 2 shells, tau has 3,
charm has 2, bottom has 3, top has 4) have inter-shell bonding energy
from the SSV interaction between adjacent shells. This contribution
scales with the number of shell boundaries and the SSV potential
between them. It is computed as a fixed fraction of E_cage per
additional shell, derived from the radial SSV geometry.

**Step 11 — DP cloud energy (E_cloud).**
The polarised DP cloud around the cage stores additional energy.
The SSV field of the cage organises nearby Sea DPs into radial chains
(SM-1's radial chain structure), and the energy of this organisation
contributes to the particle's total rest mass. This contribution is
a fixed fraction of E_cage, determined by the geometry of the cage's
SSV field and the Sea's mean DP density.

**Step 12 — Residual term.**
After computing E_cage + E_ZBW + E_inter + E_cloud from the cage
geometry and uniform rules, a residual correction brings the total
to the PDG value. For the electron this residual is 0.052 MeV;
for the tau it is 142.1 MeV. The residuals are not random — they
follow a systematic pattern related to the cage size — but their
exact derivation from first principles is OP-SS-1.

---

## Part 5: The Dipole Sea Composition

**Step 13 — Not all DPs are the same.**
The Dipole Sea contains three types of DP pairs: eDPs (electron-sector),
qDPs (quark-sector), and hDPs (hybrid — bridging both sectors). Their
relative composition at any Grid Point determines which type of ZBW
energy the particle's cage contributes.

**Step 14 — Lepton DP composition: equal mix.**
Leptons (electron, muon, tau, neutrinos) have central eCPs. The eCPs
interact equally with all DP types — no preferred coupling. The lepton
cage therefore draws on an equal 25% mix of eDP, qDP, hDP-A, and hDP-B.
This equal mix is the lepton's "charge neutrality" in the Sea — it
couples to all sectors equally without discrimination.

**Step 15 — Quark DP composition: radial gradient.**
Quarks have central qCPs with the additional colour coupling (t = 0.5
from SS-1). The quark cage draws preferentially on qDPs near the cage
centre (where the qCP's SSV field is strongest) and equalises toward
the outer layers where the field weakens. This radial gradient from
qDP-dominant to equal-mix determines the ZBW energy decomposition
across the cage shells and is the physical origin of the different
mass formulas for up-type and down-type quarks.

---

## Part 6: The Complete Mass Table

**Step 16 — Applying the formula to all 15 particles.**
The same four-step procedure (base mass → ZBW → inter-layer → cloud)
with the same k ≈ 0.0185 and the same σ = 120^{−d} suppression
is applied to all Standard Model particles. No additional calibration
constants are introduced per particle — only the cage geometry
assignments (N_k values) and DP composition are particle-specific,
and these follow from the cage structure.

Mass table summary (all MeV/c²):

    Electron (N_k=1):      0.511 (calibration anchor)
    Muon (N_k=4):          105.66 (✓ PDG)
    Tau (N_k=12):          1776.86 (✓ PDG)
    Up (N_k~1):            2.3 (calibrated)
    Down (N_k~2.5):        4.8 (calibrated)
    Strange (N_k~30):      95 (calibrated)
    Charm (N_k~180):       1275 (calibrated)
    Bottom (N_k~3000):     4180 (calibrated)
    Top (N_k~30000):       172690 (calibrated; 30-vertex shell TBD)
    W (linear hDP chain):  80380 (calibrated)
    Z (icosahedral cage):  91190 (calibrated)
    Higgs (dodeca cage):   125000 (calibrated)

**Step 17 — The honest status.**
The lepton masses (e, μ, τ) are calibrated to PDG via one constant k.
The quark masses have additional N_k assignments that are geometrically
motivated but not derived. The W, Z, Higgs masses are assigned cage
structures (linear hDP chain, icosahedral, dodecahedral respectively)
that are consistent with the SM-1 cage hierarchy but whose mass formula
derivation is open.

The framework is semi-empirical: the same k propagates through
consistent geometric rules to all particles, which is more
constrained than having 15 free parameters (as the Standard Model
effectively has). But it is not yet parameter-free for the quark
and gauge boson sectors.

---

## Part 7: Superseded Results Within SM-2

**Step 18 — The 1/φ² ≈ 1/3 approximation.**
SM-2 Appendices G and H use 1/φ² ≈ 0.382 ≈ 1/3 for charge screening.
This is superseded by SM-1 Theorem 1 (δ = 1/3 exactly from C₃ cage
symmetry). The 1/φ² approximation was the original CPP derivation —
physically motivated but with a 14.6% error. The exact topological proof
is the correct result; the φ-based argument is retained in SM-2 for
historical reference only.

**Step 19 — The C₆₀ cage correction.**
The original SM-2 used N_k ≈ 60000 for the top quark, motivated by
an assumed C₆₀ cage. PS-1 (2026) falsified this — no 60-vertex shell
exists in the 600-cell. SM-2 v30 uses the 30-vertex shell as the
fourth cage candidate with N_k ≈ 30000 (recalibrated). The top
quark mass formula using the 30-vertex shell geometry is OP-SS-1.

---

## Mathematical Correspondence Index

| Mechanism step | Paper equation / section |
|----------------|--------------------------|
| Steps 3–5: VEV formula | §2 (VEV derivation), Eq. ⟨φ⟩ |
| Step 6: N_k assignments | §6 (particle cage assignments), Table 1 |
| Step 7: Yukawa coupling | §3, Eq. y_k |
| Step 8: Base mass | §4, Eq. m c² = y_k × ⟨φ⟩ |
| Steps 9–12: Refinements | §5 (universal refinements) |
| Steps 13–15: DP composition | §5 (DP composition) |
| Step 16: Mass table | §7 Table (mass breakdown) |
| Steps 18–19: Corrections | §1 (consistency note), §8 |
