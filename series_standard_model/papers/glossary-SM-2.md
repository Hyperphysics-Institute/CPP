# Glossary — SM-2: Mass Generation from Geometric Hierarchies in the 600-Cell Lattice

**Paper:** SM-2_mass_generation_geometric_hierarchies.tex (v30)
**Last updated:** 30 March 2026

*Terms defined as they function in SM-2 specifically. SM-2 introduces
the VEV formula, the Yukawa coupling from geometry, the four mass
contributions, the DP composition rules, and the complete SM mass table.
Terms defined in SM-1 that appear here with the same meaning are
cross-referenced rather than repeated. New terms specific to SM-2 are
defined fully.*

---

## Section 1: The Mass Scale Problem

**Planck energy (E_P)**
The natural energy unit of CPP: E_P = ℏ c / l_P ≈ 1.22 × 10²⁸ MeV,
where l_P ≈ 1.616 × 10⁻³⁵ m is the Planck length. In SM-2, E_P is
the starting point of the mass scale: the total computational energy
available per Absolute Moment in a single 600-cell. The particle masses
are this Planck energy suppressed by the lattice structure via the VEV
formula. The ratio E_P/m_e ≈ 2.4 × 10²⁸ is the scale hierarchy that
SM-2 must bridge with geometric suppression.

**Planck-to-particle scale hierarchy**
The approximately 28 orders-of-magnitude ratio between the Planck scale
(~10¹⁹ GeV) and particle masses (~MeV to ~100 GeV). In standard physics,
this hierarchy is unexplained — the Higgs mechanism sets the electroweak
scale but does not explain why the electroweak scale is so much smaller
than the Planck scale (the "hierarchy problem"). In SM-2, this hierarchy
is partially explained by the geometric suppression factor N_lattice⁴ = 120⁴:
the particle's mass is the Planck energy divided by the fourth power of
the lattice size, reflecting the idea that a particle occupies a specific
fraction of the full lattice's computational space. The remaining factor k
is a calibration constant whose geometric origin is OP-SM-1 (solved to
3.8% via α_geom).

---

## Section 2: The VEV Formula

**Vacuum expectation value (VEV, ⟨φ⟩)**
In SM-2, the VEV is the effective energy scale available to a single
cage particle:

    ⟨φ⟩ = k × E_P / N_lattice⁴ × φ_k

where k ≈ 0.0185 is the calibration constant, N_lattice = 120,
and φ_k is the golden-ratio generation factor. The VEV is not the
Higgs VEV of the Standard Model (246 GeV) — it is a per-particle
energy scale determined by the lattice geometry and the particle's
generation. The name "VEV" is used analogically: it is the background
energy from which particle masses are drawn, as the Higgs VEV is the
background from which SM Yukawa couplings draw their masses.

In SM-2, ⟨φ⟩ has units of energy (MeV) and is different for each
generation because φ_k = φ^j where j is the generation number
(j=1: electron/up/down; j=2: muon/strange/charm; j=3: tau/bottom/top).
The golden-ratio progression φ¹, φ², φ³ ≈ 1.618, 2.618, 4.236 gives
each generation a 1.618× larger energy scale than the previous,
consistent with the observed rough mass ratios between generations.

**Generation factor (φ_k = φ^j)**
The golden-ratio power that sets the energy scale for each SM
generation. First generation: φ¹ ≈ 1.618. Second generation:
φ² ≈ 2.618. Third generation: φ³ ≈ 4.236. This factor is
motivated by the golden-ratio geometry of the 600-cell (the lattice's
edge lengths and shell radii involve φ at every level), but its
exact role in determining generation masses is an open derivation.
The K3 spectral theorem (SM-3) derives the Koide mass ratio K = 2/3
independently without using the φ^j generation factor — the two
approaches are compatible but connect through different pathways.

**k (mass generation calibration constant)**
The single calibration constant of SM-2: k ≈ 0.0185, fixed by
setting the electron mass to 0.511 MeV. Unlike SSV₀ in SM-1 (which
is an energy), k is dimensionless — it is a ratio that scales the
Planck energy down to the observed particle mass scale. The ratio
of the derived geometric estimate (k ~ 1/(N × φ²) ≈ 0.00318) to
the calibrated value (0.0185) is ~5.8, which is close to but not
exactly a simple geometric invariant. The exact derivation of k from
600-cell geometry was OP-SM-1 (solved to 3.8% via α_geom = 0.5594,
k_SM = α_geom/(12φ²) ≈ 0.01781; the 4% remaining between k_SM and
k ≈ 0.0185 is a calibration residual).

---

## Section 3: Yukawa Couplings

**Yukawa coupling (y_k)**
The coupling of a particle to the vacuum field, determining its mass
via m c² = y_k × ⟨φ⟩. In SM-2:

    y_k = φ^k × N_k / 120

where N_k is the effective cage occupancy and φ^k is the generation
factor. In the Standard Model, Yukawa couplings are free parameters —
one for each fermion, with no explanation for their values. In SM-2,
the Yukawa coupling is determined by the cage geometry: N_k/120 is
the fraction of the 600-cell lattice that the particle's cage occupies,
and φ^k is the generation energy scale. The SM-2 Yukawa couplings
are not free parameters — they follow from one constant k plus the
cage geometry assignments. Whether the cage geometry fully determines
N_k from first principles (without calibration to PDG masses) is OP-SS-1.

**Effective cage occupancy (N_k)**
The parameter in SM-2 that encodes how much of the 600-cell lattice
a particle's cage configuration uses. N_k is motivated by the cage
vertex counts from SM-1 Table 1, but it is not simply the vertex count
— it includes contributions from inter-layer bonding, DP cloud geometry,
and the ZBW orbital structure. Approximate values:

    Electron: N_k ≈ 1       (minimal cage)
    Muon:     N_k ≈ 4       (tetrahedral cage)
    Tau:      N_k ≈ 12      (icosahedral cage)
    Up:       N_k ≈ 1       (bare qCP)
    Down:     N_k ≈ 2.5     (bare qCP + linear ZBW DP)
    Strange:  N_k ≈ 30      (effective)
    Charm:    N_k ≈ 180     (effective)
    Bottom:   N_k ≈ 3000    (effective)
    Top:      N_k ≈ 30000   (effective; 30-vertex shell, TBD)

The gap between the simple vertex counts (4, 12, 20, 30) and the
effective occupancies reflects contributions that SM-2 includes
through the refinement terms. Deriving these effective occupancies
from the cage geometry alone — without calibration to PDG — is
OP-SS-1. The N_k values labelled "effective" above should be
understood as calibrated estimates, not derived results.

---

## Section 4: The Four Mass Contributions

**E_cage (SSV cage binding energy)**
The base SSV binding energy from SM-1's cage structure: approximately
E_cage ≈ (N/2) × SSV₀ for symmetric cages, where N is the number of
cage vertices and SSV₀ = 0.2555 MeV. This is the leading contribution
to the lepton masses and a significant contribution to quark masses.
See SM-1 §7 for the derivation.

**E_ZBW (ZBW kinetic energy)**
The kinetic energy of the orbital ZBW Dipole Pair, given by
E_ZBW = (1/2)m(c/r_eff)² × σ where σ = 120^{−d}. This is the
second-largest contribution for most particles. For fermions with
d=0 (bound orbital), E_ZBW is a fixed fraction of the total mass
(approximately 20% for the electron). For down-type quarks, the
additional linear ZBW DP (d=1) adds ~1% from the 120⁻¹ suppression.
For neutrinos (d=3), E_ZBW is the only mass contribution and is
suppressed by 120⁻³.

**E_inter (inter-layer bonding energy)**
The SSV interaction energy between adjacent cage shells in
multi-shell particles (muon has 2 shells, tau has 3, charm has 2,
bottom has 3, top has 4). The inner and outer shell CPs interact
through the SSV force — the inner shell's positive CPs are pulled
toward the central negative CP, but they also interact with the
outer shell CPs through the SSV gradient across the shell boundary.
E_inter is computed as a fixed fraction of E_cage per additional
shell boundary. For the muon: E_inter ≈ 10.566 MeV (~10% of total).
The exact formula for E_inter from the cage geometry is part of OP-SS-1.

**E_cloud (DP cloud energy)**
The energy of the polarised Dipole Sea cloud surrounding the cage.
The cage's SSV field organises nearby Sea DPs into the radial chain
structure described in SM-1 (P-CPP-5 in propositions.md). The energy
stored in these organised chains contributes to the total rest mass.
E_cloud is computed as a fixed fraction of E_cage (approximately
10% for leptons). The exact formula connecting E_cloud to chain
equilibrium length (OP-QM-new-4) and SM-2's cloud energy is an
open connection.

**Residual term**
The difference between (E_cage + E_ZBW + E_inter + E_cloud) and
the PDG mass. In SM-2, this residual is explicitly shown in the
mass table and is non-zero for all particles. The residual is a
systematic measure of what the four-contribution framework has
not yet captured. Notably, the residuals follow a pattern —
they increase with cage complexity — suggesting they are a single
missing contribution that scales with the cage rather than random
errors. Identifying this contribution is part of OP-SS-1.

---

## Section 5: DP Composition Rules

**DP composition**
The fractional mix of Dipole Pair types (eDP, qDP, hDP-A, hDP-B)
that a particle's cage draws on from the Dipole Sea. The composition
determines the ZBW energy mode and hence the mass contribution from
the Sea polarisation.

**Lepton DP composition: equal 25% mix**
Leptons have central eCPs that couple equally to all DP types —
no preferred sector coupling. The 25% equal mix (eDP, qDP, hDP-A,
hDP-B) is the maximum-entropy composition. Physically: the eCP's
SSV field does not distinguish between DP types, so it draws
randomly from the Sea. The equal mix means each DP type contributes
equally to E_ZBW.

**Quark DP composition: radial gradient**
Quarks have central qCPs with colour coupling (t = 0.5 from SS-1).
The qCP's SSV field preferentially attracts qDPs at the cage centre
where the field is strongest. At larger radii, the field weakens and
the composition approaches the equal mix. This radial gradient from
qDP-dominant (inner) to equal-mix (outer) is the SM-2 model for
quark DP structure. The gradient is the reason quark masses follow
a different scaling law from lepton masses: the qDP-dominant inner
region stores more SSV energy per vertex than the equal-mix outer
region.

**eDP (electron Dipole Pair)**
A DP composed of two eCPs. Mediates electromagnetic interactions
in the Dipole Sea. The dominant DP type for leptons (25% of total).

**qDP (quark Dipole Pair)**
A DP composed of two qCPs. Mediates strong interactions in the
Dipole Sea. Dominant near the centre of quark cages. The linear
ZBW DP of down-type quarks is a qDP or hDP oscillating radially.

**hDP (hybrid Dipole Pair)**
A DP bridging the electron and quark sectors — one eCP + one qCP.
Two types (hDP-A and hDP-B depending on polarity combination).
hDPs mediate weak interactions and appear in both the W bracelet
structure (EW series) and as 25% of the lepton DP composition.

---

## Section 6: The Suppression Factor

**σ = 120^{−d} (geometric suppression)**
As defined in SM-1 §8, σ encodes the number of unbound spatial
dimensions d of a particle's ZBW mode in the 600-cell lattice.
In SM-2, this factor appears in the ZBW energy term E_ZBW and
also in the neutrino mass formula. The factor 120 is the total
vertex count of the 600-cell, reflecting the idea that a particle
with d unbound dimensions dilutes its ZBW energy across the full
lattice in d dimensions.

Key values:
- d=0 (bound orbital, all charged particles): σ = 1
- d=1 (linear ZBW extra, down-type quarks): σ = 1/120 ≈ 0.0083
- d=3 (unbound neutrino ZBW mode): σ = 1/120³ ≈ 5.8 × 10⁻⁷

The d=3 suppression for neutrinos is why they are nearly massless:
their ZBW energy is diluted across all three spatial dimensions of
the macroscopic lattice. This is a geometric explanation for the
neutrino mass hierarchy — not postulated but derived from the
number of unbound lattice dimensions.

---

## Section 7: The Boson Cages

**W boson as linear hDP chain**
The W boson in SM-2 is modelled as a linear chain of 6 hDP pairs.
In contrast to the closed polyhedral cages of the fermions, the W
is an open linear structure — consistent with SS-1's gluon
masslessness argument (open paths → masslessness) reversed: closed
structures → mass. The W is not massless because it is a bracelet
(closed ring), not an open chain — but in SM-2 it is approximated
as a linear structure for the mass calculation. The full treatment
of the W as a bracelet is in the EW series.

**Z boson as icosahedral cage**
The Z boson in SM-2 is modelled as an icosahedral hDP cage (12
vertices) — the same geometry as the charm quark's outer shell and
the muon's cage. The coupling to the Sea is symmetric (unlike the W
bracelet) — consistent with the Z's observed parity-conserving
coupling vs the W's parity-violating coupling.

**Higgs boson as dodecahedral cage**
The Higgs boson in SM-2 is modelled as a dodecahedral hDP cage
(20 vertices) — the same geometry as the bottom quark's third shell.
The Higgs mass (≈125 GeV) is the highest of the three gauge bosons,
consistent with the dodecahedral cage (N=20) producing more binding
energy than the icosahedral (N=12) Z cage.

---

## Section 8: Superseded Results in SM-2

**1/φ² ≈ 1/3 approximation (Appendices G and H)**
SM-2 Appendices G and H derive quark charges from the approximation
1/φ² ≈ 0.382 ≈ 1/3. This is superseded by SM-1 Theorem 1 (δ = 1/3
exactly from C₃ cage symmetry). The φ-based argument is retained
for historical context but carries a 14.6% error relative to the
exact topological proof. Do not cite Appendices G or H as the charge
quantisation derivation; cite SM-1 Theorem 1.

**C₆₀ fullerene cage for top quark**
SM-2 versions before v30 used a C₆₀ cage (60 vertices) for the top
quark. This was falsified by PS-1 (2026): no 60-vertex distance shell
exists in the 600-cell. Version 30 uses the 30-vertex shell candidate.
All references to "C₆₀" or "fullerene cage" in SM-2 should be read
as referring to the 30-vertex shell (d²=2) from SM-1 version 6 onward.

**Koide ratio from φ-scaling**
SM-2 reproduced the Koide ratio K ≈ 2/3 through φ-based scaling of
the cage vertex counts. This is the right result by the wrong mechanism.
The correct derivation is the K3 spectral theorem in SM-3: K = 2/3
exactly from the eigenvalue ratio of the K3 cage base graph, with no
free parameters. The SM-2 φ-scaling argument gives the right order
of magnitude but is not the derivation.

---

## Section 9: Open Problems Specific to SM-2

**OP-SS-1 (primary):** Derive the effective occupancies N_k from
600-cell geometry and the four-contribution formula (E_cage + E_ZBW
+ E_inter + E_cloud) from first principles. This would convert
SM-2 from a semi-empirical framework to a parameter-free one.

**Open connection:** The relationship between SM-2's k ≈ 0.0185
and SM-1's SSV₀ = 0.2555 MeV. Both measure the energy scale of
the SSV interaction but at different levels of the framework.
Their relationship through the 600-cell geometry has been
partially identified (k_SM = α_geom/(12φ²) from SS-1) but the
remaining 4% discrepancy is the projection correction.

**Open connection:** The relationship between SM-2's VEV formula
and SM-3's ZBW thermal energy scale (ℏω₀ = sea_strength × ℏc/r_conf).
These should be consistent — both describe the same mass generation
mechanism — but the formal connection is not yet derived.
