# Glossary — SM-1: Binding Mechanisms and Cage Stability in the 600-Cell Lattice

**Paper:** SM-1_binding_mechanisms_and_cage_stability.tex (v6)
**Last updated:** 29 March 2026

*Each entry defines the term as it is used specifically in SM-1 — not a
general dictionary definition, but the concept as it functions in this
paper's argument. SM-1 is the foundation paper of the series: it introduces
the SSV force law, the cage concept, and the one calibration constant SSV₀.
Later papers (SM-2 through SM-5) build on these definitions without
redefining them; cross-references are noted where relevant.*

---

## Section 1: The Lattice and Its Geometry

**600-cell**
The 4-dimensional polytope — 120 vertices, 720 edges, 1200 triangular
faces, 600 tetrahedral cells — whose geometry is the spatial substrate of
CPP. In SM-1, the 600-cell is used primarily for its local geometry: the
arrangement of nearest-neighbour vertices around any reference point, which
determines what cage shapes are geometrically available. The four cage
types in SM-1 (tetrahedral, icosahedral, dodecahedral, 30-vertex shell)
are the four natural distance shells of the 600-cell at increasing radii,
not freely chosen polyhedra. See also: the 600-cell entry in glossary-SS-1.md
for a fuller treatment of the global lattice structure.

**Grid Point (GP)**
A fixed vertex of the 600-cell lattice — one of the 120 spatial address
points per lattice unit. Grid Points do not move. They are the locations
at which Conscious Points can reside. In SM-1, the central CP of a cage
sits at one Grid Point, and each compensating CP sits at an adjacent Grid
Point. The nearest-neighbour distance d₀ between adjacent Grid Points
is the natural length unit of SM-1's binding energy calculation.

**Nearest neighbours**
The 12 Grid Points closest to any given Grid Point in the 600-cell lattice,
forming the first full distance shell (icosahedral arrangement). In SM-1,
the tetrahedral cage uses a subset of 4 of these 12 nearest neighbours —
specifically, the four that form a regular tetrahedron. The choice of 4
from 12 is not arbitrary: 4 is the minimum number of CPs that can fully
cancel the SSV field at the central CP (see mechanism Steps 7–10).

**Distance shells**
The concentric layers of Grid Points at increasing distances from a
reference vertex. In SM-1, four shells are relevant as cage candidates:

    Shell 0 subset: N=4  (tetrahedral, d² = 1/φ², subset of first shell)
    Shell 0 full:  N=12  (icosahedral, d² = 1/φ², full first shell)
    Shell 1:       N=20  (dodecahedral, d² = 1)
    Shell 2:       N=12  (d² = 1+1/φ² — duplicate count, skipped)
    Shell 3:       N=30  (d² = 2, degree-4 vertices, vertex-transitive)

The palindromic structure of the 600-cell shells (vertex counts form a
symmetric pattern) means shells repeat their counts. Shell 2 is skipped
in the cage assignment because it has the same vertex count as the
icosahedral shell — two different physical particles cannot have identical
cage structures. The cage sequence is therefore {4, 12, 20, 30}, forced
by geometry.

**Absolute Moment**
The fundamental time tick of CPP — one Planck time t_P ≈ 5.39 × 10⁻⁴⁴ s.
At each Absolute Moment, every Conscious Point evaluates the SSV field at
its Grid Point and executes exactly one displacement. In SM-1, the Absolute
Moment sets the ZBW oscillation frequency: f_ZBW ≈ 1/(2t_P), the rate at
which DP pairs oscillate between their two polarisation states. The mass
energy of a particle is proportional to the energy stored per Absolute
Moment in its cage configuration.

---

## Section 2: The Dipole Sea

**Dipole Sea**
The physical vacuum of CPP — all of space filled with oscillating dipole
pairs (DPs) at the ZBW frequency. In SM-1, the Dipole Sea is the medium
that transmits the SSV field: when a CP's polarity polarises nearby DPs,
this polarisation propagates outward as the SSV field, mediating forces
on other CPs. The Dipole Sea's equilibrium state (maximum entropy,
random orientation) is what empty space looks like in CPP. A particle
is a stable departure from this equilibrium: a region where the Sea has
been locally organised into a coherent, low-entropy configuration, and
the energy cost of maintaining that organisation is the particle's mass.

The Dipole Sea plays three roles in SM-1: (1) it is the medium through
which the SSV force is transmitted; (2) its ZBW oscillation sets the
energy scale of the force; (3) the energy stored in organising it
constitutes mass.

**Dipole Pair (DP)**
A bound state of two Conscious Points of opposite polarity: one +CP and
one −CP, held together by their mutual SSV attraction, oscillating at the
ZBW frequency f_ZBW ≈ 1/(2t_P). DPs are the basic constituents of the
Dipole Sea — the sea is a gas of these pairs in their equilibrium,
randomly-oriented state. In SM-1, DPs appear in two roles: (a) as
constituents of the ambient Sea that transmit the SSV field, and (b) as
the orbital ZBW DP that every fermion carries to produce its spin-½.

**Orbital ZBW DP**
A specific DP that executes a closed orbital loop around a particle's
central CP, rather than oscillating in place like a Sea DP. All fermions
in SM-1 carry one orbital ZBW DP. Its orbital motion is the CPP realisation
of Dirac's Zitterbewegung — the trembling motion that produces spin-½ in
the Dirac equation. The orbital ZBW DP contributes ZBW kinetic energy to
the particle's total mass: E_ZBW = (1/2)m(c/r_eff)² × σ, where σ is the
geometric suppression factor. Unlike the cage binding energy (which scales
with N), the ZBW contribution is common to all fermions and represents
the spin-generating organisational cost.

---

## Section 3: Conscious Points and Their Properties

**Conscious Point (CP)**
The fundamental entity of CPP — a ±1 charge carrier that executes one
displacement per Absolute Moment along a 600-cell edge according to
deterministic rules set by the SSV field at its current Grid Point.
In SM-1, CPs appear in two roles: as the central CP of a particle (the
entity whose mass is being derived) and as compensating cage CPs (the
outer shell that creates the binding energy). The word "Conscious" is
used precisely — CPs perceive and respond to their local field environment.

**eCP (electron Conscious Point)**
A CP carrying unit electric charge in the lepton sector. In SM-1, the
electron's central CP is a −eCP, and each of the four tetrahedral cage
vertices is occupied by a +eCP. The type coupling factor for eCPs is
t = 1 — eCPs couple to the SSV field with full strength. All SM-1
binding energy calculations for leptons use eCPs with t = 1.

**qCP (quark Conscious Point)**
A CP carrying fractional electric charge in the quark sector. In SM-1,
qCPs appear in the cage assignment table but the worked electron example
uses eCPs only. The type coupling factor for qCPs is t = 0.5, reflecting
the colour-like rotational symmetry of the 600-cell that reduces the
effective SSV coupling strength by half. This factor is asserted in
SM-1 (§3) and derived rigorously in SS-1 (Theorem 1: SU(3) from
tetrahedral hopping operators). The t = 0.5 factor is not a free
parameter — it is a consequence of the cage geometry proved in SS-1.

**Polarity (p)**
The charge state of a CP: p = +1 or p = −1. Polarity is the single
binary degree of freedom of a CP. Opposite polarities attract (the SSV_net
gradient points toward the opposite polarity); like polarities repel.
In SM-1, polarity is what drives both the assembly of cages (central
and compensating CPs must be opposite-polarity) and the force law
(the SSV field magnitude is proportional to p). Polarity is conserved
across all Absolute Moments — a CP cannot spontaneously switch polarity;
only a W-bracelet interaction (EW sector) can change it.

Note on CP co-occupation (30 March 2026): the CP Exclusion Postulate
(two CPs cannot occupy the same Grid Point) is no longer needed as an
independent axiom. For same-polarity pairs, repulsive SSV_net prevents
approach to the same Grid Point. For opposite-polarity pairs, co-occupation
(superimposition) is a transient one-Absolute-Moment state: at
superimposition, intra-pair SSV_net direction is undefined; bulk SSV_net
drives opposite displacements on the following Moment. Persistent
co-occupation is impossible in both cases without any additional postulate.
See Theorem T-CPP-1 in propositions.md.

**Planck Sphere Radius (PSR)**
The effective interaction range of a CP — the radius within which the
CP's SSV field can act on other CPs. In SM-1, the PSR sets the
minimum effective orbital radius for cage CPs: no cage vertex can be
closer to the central CP than the PSR allows. The PSR is not a fixed
physical constant — it is compressed by high SSV density (as in SR-1,
where PSR compression produces Lorentz contraction). In SM-1, at the
low energies relevant to atomic-scale masses, PSR compression is
negligible and the PSR is treated as fixed at the Planck length l_P.
The PSR also sets the range of the SSV field: beyond PSR, the field
falls to zero. In SM-1, the 600-cell nearest-neighbour distance d₀
is assumed to be within the PSR.

---

## Section 4: The SSV Field and Force Law

**Space Stress Vector (SSV) — overview**
The local field produced by Conscious Points through their polarisation
of the Dipole Sea. Every CP polarises the DPs within its PSR, aligning
their positive poles toward itself (for a negative CP) or away. This
polarisation propagates outward as the SSV field. Two physically
distinct quantities arise from the SSV field and must be carefully
distinguished (30 March 2026 clarification):

**SSV_net (directional SSV field)**
The vector sum of all SSV contributions at a Grid Point from all CPs
within their PSR. SSV_net has both magnitude and direction. It governs
which Grid Point a CP moves to next — a CP moves toward the adjacent
Grid Point with the highest SSV_net gradient. SSV_net is what drives
the ZBW oscillation to reverse: when A(−) rebounds from B(+), it is
because the SSV_net at the superimposition Grid Point (now from the
bulk Dipole Sea, not from B) points away from B's original position.

    SSV_net = Σ SSV₀ · p · t · f(type) · r̂ / r²   [Eq. 1 of SM-1]

Key property: at the cage centre (central CP surrounded by four
tetrahedral cage CPs), SSV_net from the cage = 0 exactly (T_d symmetry
cancels all contributions). The central CP sits in a force-free pocket
governed entirely by external SSV_net fields. This is why electrons
are mobile — their cage provides no restoring force on the central CP's
absolute position.

Key property: at Grid Point superimposition of an opposite-polarity
pair, SSV_net from the intra-pair interaction = 0 (direction undefined).
The bulk SSV_net governs both CPs, driving them apart in opposite
directions.

**SSV_abs (scalar SSV magnitude)**
The scalar magnitude of the total SSV field at a Grid Point —
|SSV_net| combined with any isotropic stress contributions. SSV_abs
has no direction; it is a local energy density. High SSV_abs means
the Dipole Sea is strongly stressed at that location. SSV_abs governs
PSR compression:

    PSR_eff = l_P / (1 + k · SSV_abs)

High SSV_abs → compressed PSR → each lattice step covers less physical
distance → metric is locally contracted. This is the GR/Lorentzian
effect: SSV_abs compresses space. It is what produces Lorentz
contraction and gravitational time dilation in SR-1.

Critical distinction: at Grid Point superimposition of an opposite-
polarity pair, SSV_abs is near its maximum (intra-pair field strongest)
while SSV_net from the intra-pair interaction is exactly zero. This
demonstrates that SSV_abs and SSV_net are physically independent
quantities — one can be maximised while the other vanishes at the
same Grid Point.

Summary of roles:
- SSV_net → determines CP displacement direction → governs dynamics
- SSV_abs → determines PSR compression → governs local metric
- SM-1 is primarily an SSV_net story (force law, cage stability)
- SR-1 is primarily an SSV_abs story (PSR compression = Lorentz effects)
- Both operate simultaneously in all physical processes

In SM-1, the SSV is the mediator of all forces. There is no separate
field for each force in CPP; all forces are aspects of the SSV gradient,
with the strong force involving t = 0.5 for qCPs and gravitational
effects arising from SSV_abs/PSR compression.

**SSV₀ (elementary stress magnitude)**
The SSV field strength of a single CP at unit distance. SSV₀ is the one
calibration constant of SM-1. Its value is:

    SSV₀ = m_e c² / 2 = 0.2555 MeV

fixed by setting the electron binding energy (2 lattice units) equal to
the electron rest mass energy (0.511 MeV). Every other mass prediction
in SM-1 uses this same SSV₀, so the mass hierarchy is determined purely
by cage geometry once SSV₀ is fixed.

It is important to understand what SSV₀ is and is not: it is the energy
per unit of SSV stress per unit distance. It is not a coupling constant
in the QFT sense (there is no running with energy scale at this level of
SM-1's treatment). The relationship between SSV₀ and sea_strength — the
coupling constant that appears in SM-3's ZBW thermal energy scale — is
an open connection (see OP-SS-1).

**SSV gradient force**
The force on a CP due to the spatial variation of the SSV field. In SM-1,
the force on test CP j is F_j = −q_j · SSV(r_j), where q_j = p_j (the
polarity) and SSV(r_j) is the field at j's location. This is analogous
to F = qE in electrostatics, but the SSV plays the role of E and polarity
plays the role of charge. The force is directed along the SSV gradient —
toward regions of higher SSV field magnitude for opposite-polarity CPs
(attraction) and away for same-polarity CPs (repulsion).

**Type coupling factor (t)**
A dimensionless factor that scales the SSV coupling strength depending on
the CP type: t = 1 for eCPs, t = 0.5 for qCPs. In SM-1 this factor is
stated as an input; it is derived in SS-1 (Theorem 1). Its physical
meaning: qCPs interact with the SSV field at half the strength of eCPs
because the three colour states of a qCP share the available coupling
strength equally among them. The 1/3 × 3/2 = 1/2 factor reflects this
averaging: a qCP in a specific colour state uses only 1/3 of the total
SSV coupling, but there are effectively 3/2 relevant coupling channels
in the strong sector. The SS-1 derivation formalises this via the
traceless Hermitian generators and their normalisation.

**f(type compatibility)**
A function that modulates the SSV coupling when eCPs and qCPs interact.
In SM-1, this function appears in the general SSV formula [Eq. 1] to
allow for the possibility that eCP–qCP interactions have a different
coupling strength than eCP–eCP or qCP–qCP interactions. In the worked
electron example, all CPs are eCPs and f = 1. The full treatment of
cross-type coupling belongs to the EW series.

---

## Section 5: Binding Energy and Cage Stability

**Binding energy (E_binding)**
The total potential energy stored in a cage configuration — the energy
that would need to be supplied to disassemble the cage into free CPs.
In SM-1:

    E_binding = −(1/2) Σⱼ qⱼ · Φ(rⱼ)

where Φ(rⱼ) is the total SSV potential at the location of CP j from
all other CPs in the cage, and the factor 1/2 prevents double-counting
pairwise interactions. For a central CP surrounded by N compensating
CPs at uniform distance d₀:

    E_binding ≈ N/2 × SSV₀   (lattice units)

This is an approximation valid for symmetric (uniform-shell) cages.
The electron case gives E_binding = 2 SSV₀ (N=4), the muon case gives
6 SSV₀ (N=12), and so on through the cage hierarchy.

In physical units after calibration: E_binding = (N/2) × 0.2555 MeV.
The mass of a particle is identified with its binding energy in SM-1's
framework — the rest mass energy equals the energy required to disassemble
the cage into its constituent free CPs.

**Cage stability**
A cage is stable when the net SSV force on every CP in the configuration
is zero — no CP has a preferred direction to move. The condition for
stability is that all SSV multipole moments cancel at the central CP's
location. In SM-1, this is demonstrated geometrically: partial cage
occupancy leaves non-zero multipole moments that drive motion; full
tetrahedral (or higher) occupancy cancels all multipoles and produces
a force-free configuration.

The stability hierarchy from Table 2 of SM-1:
- 1 compensating CP: unstable (strong residual dipole gradient)
- 2 compensating CPs: metastable (residual torque from quadrupole moment)
- 3 compensating CPs: highly unstable (asymmetric gradients dominate)
- 4 compensating CPs at tetrahedral vertices: minimal stable configuration

Stability requires not just any 4-vertex configuration but specifically
the regular tetrahedron: the T_d symmetry group of the tetrahedron is
the minimum symmetry that cancels all SSV vector moments at the centre.

**Cage completion**
The process by which a partially-occupied cage attracts additional CPs
from the Dipole Sea to reach a stable fully-occupied configuration.
When a cage has 1, 2, or 3 compensating CPs, the net SSV gradient at
the unoccupied vertex positions is attractive to opposite-polarity free
CPs in the Sea. Cage completion is the CPP mechanism for particle
formation in the early universe: as the universe cooled and qDP chain
self-collimation began, CPs condensed into their lowest-energy cage
configurations.

**Cage dissociation**
The process by which a cage loses one or more compensating CPs and
becomes unstable. Dissociation requires sufficient energy input to
overcome the binding energy. For the electron cage (2 SSV₀ ≈ 0.511 MeV),
dissociation corresponds to pair annihilation — the central eCP and a
cage eCP combine and emit ZBW radiation. For quark cages, dissociation
is suppressed by confinement: the qDP chains that span the gap between
quarks inside a hadron resist separation (see glossary-SS-1.md:
confinement, string tension).

---

## Section 6: The Cage Hierarchy and Particle Assignments

**Tetrahedral cage (N = 4)**
The minimal stable cage — four compensating CPs at the vertices of a
regular tetrahedron surrounding a central CP. In SM-1:
- Electron: central −eCP, four +eCPs at tetrahedral vertices
- Up quark: central +qCP, no polyhedral cage (bare qCP with ZBW cloud)
- Down quark: central −qCP, no polyhedral cage

Wait — SM-1 Table 1 lists the tetrahedral cage under "example particles"
for "e, μ, u, d" but u and d quarks have no polyhedral cage in the
corrected CPP picture (see SS-1 §1.1 H4 and mechanism-SS-1.md §1).
Table 1 of SM-1 reflects an earlier view and should be read with the
correction that u and d are bare qCPs; the tetrahedral cage for quarks
begins at the strange quark. The tetrahedral cage is used by the
electron (confirmed), the up and down quarks (the cage is the K₃
color base triangle, not an outer polyhedral shell), and as the first
outer shell for strange, charm, bottom, and top.

**Icosahedral cage (N = 12)**
The full first distance shell of the 600-cell — 12 vertices equidistant
from the reference vertex, forming a regular icosahedron. In SM-1, this
is the cage assigned to the muon (12 eCPs surrounding a central −eCP),
the charm quark (first outer shell after the tetrahedral color cage),
the tau lepton (SM-4), and the Z boson (EW sector). Binding energy
≈ 6 SSV₀ ≈ 1.533 MeV from the cage formula alone; actual muon mass
includes additional ZBW and bonding contributions (SM-2).

**Dodecahedral cage (N = 20)**
The second distance shell of the 600-cell — 20 vertices forming a
regular dodecahedron. In SM-1, assigned to the tau lepton (outer shell
beyond the icosahedral), the bottom quark, and the Higgs boson.
Binding energy ≈ 10 SSV₀. The dodecahedron is the dual of the
icosahedron in 3D geometry, appearing as the natural next shell after
the icosahedron in the 600-cell's distance sequence.

**30-vertex shell (N = 30, shell 3)**
The third distance shell of the 600-cell at d² = 2. All 30 vertices
are equidistant from the reference vertex, degree-4 in the 600-cell
edge graph, and vertex-transitive. This shell replaces the previously
assumed C₆₀ fullerene (60 vertices), which does not exist as a
600-cell distance shell (PS-1, 2026). Binding energy ≈ 15 SSV₀.
Leading candidate for the top quark's fourth cage shell. The mass
formula using this shell is open (OP-SS-1): the geometry is established;
the quantitative mass calculation from cage depth and sea_strength
awaits the kernel of OP-SS-1.

**Cage depth (n_layers)**
The number of nested polyhedral cage shells surrounding a particle's
central CP. For quarks in SM-1's framework:
- n = 0: up, down (no polyhedral cage — bare qCPs)
- n = 1: strange (tetrahedral cage, 4 vertices)
- n = 2: charm (tetrahedral + icosahedral, 16 total)
- n = 3: bottom (+ dodecahedral, 36 total)
- n = 4: top (+ 30-vertex shell, 66 total — candidate)

For leptons:
- n = 0: electron (tetrahedral cage is the only cage)
- n = 0+1: muon (tetrahedral inner + icosahedral outer — 2 shells)
- n = 0+1+1: tau (tetrahedral + icosahedral + dodecahedral — 3 shells)

Cage depth drives the mass hierarchy: more depth = more binding energy
= more rest mass. The quantitative formula relating n to mass is
the principal open problem of the SM series (OP-SS-1).

---

## Section 7: The ZBW Spectrum

**Zitterbewegung (ZBW)**
The rapid oscillatory motion of a Dirac electron first identified by
Schrödinger in 1930. In SM-1, ZBW is not merely a mathematical artifact
but a physical oscillation of the orbital DP around the central CP. The
ZBW is the source of spin-½ in CPP — the orbital DP's closed loop
generates a magnetic moment identical to the Dirac result. Every fermion
carries exactly one orbital ZBW DP.

The ZBW oscillation is mechanical, not postulated (30 March 2026
clarification): the orbital DP approaches the central CP under
monotonically increasing SSV_net attraction — there is no reversal of
the attractive SSV_net before superimposition. At superimposition (both
at the same Grid Point), the intra-pair SSV_net direction is undefined;
the bulk SSV_net drives them apart on the next Absolute Moment. This
is Theorem T-CPP-1 and Corollary C-CPP-1a in propositions.md. The
oscillation turning point is at Grid Point superimposition, not before.

Note: during the approach phase, SSV_abs grows and compresses the local
PSR. The inner arc of the orbit covers less physical distance per lattice
step than the outer arc — the ZBW orbit is metrically asymmetric under
SSV_abs compression. This SSV_abs asymmetry is relevant to the ZBW
mechanical account of the charge screening fraction δ = 1/3 (OP-SS-13).

**ZBW frequency (f_ZBW)**
The oscillation frequency of the orbital ZBW DP: f_ZBW ≈ 1/(2t_P)
≈ 9.3 × 10⁴² Hz. This is now a *derived* quantity, not a postulate:
for a minimal-amplitude oscillation, the period is approximately 2
Absolute Moments (approach to superimposition + separation), giving
f_ZBW ≈ 1/(2t_P). This derivation caused P5 (ZBW oscillations) to be
demoted from the CPP core postulate list — the CPP postulate count
decreased from 7 to 6 on 30 March 2026. All macroscopic physical
frequencies are slow compared to the ZBW frequency. The full energy
E_ZBW = ℏ × 2πf_ZBW is suppressed by the geometric factor σ before
contributing to observed particle masses.

**Geometric suppression factor (σ = 120^{−d})**
The factor by which the ZBW energy is reduced from its Planck-scale
value to the observed particle mass scale. The suppression depends on
the number of unbound spatial dimensions d of the ZBW mode in the
600-cell lattice:

    d = 0 (fully bound orbital ZBW):     σ = 1          → electron, quarks
    d = 1 (linear ZBW extra, down-type): σ = 120⁻¹      → down-type quarks
    d = 3 (unbound neutrino mode):       σ = 120⁻³      → neutrinos

The factor 120 is the total vertex count of the 600-cell. A fully bound
orbital (d=0) has access to all lattice vertices simultaneously and
suffers no suppression. A neutrino (d=3) samples all three free spatial
dimensions of the macroscopic lattice and is suppressed by 120³ ≈
1.7 × 10⁶. This is why neutrinos are nearly massless: their ZBW mode
is maximally diluted across the full lattice. This is a motivated
geometric argument; the derivation of σ from 600-cell first principles
is an open problem.

---

## Section 8: The Calibration Constant

**SSV₀ = 0.2555 MeV**
The sole calibration constant of SM-1. Its derivation:

    E_binding(electron) = 2 lattice units
    E_binding = m_e c²  →  SSV₀ = m_e c² / 2 = 0.511/2 = 0.2555 MeV

This constant anchors the absolute mass scale. Once SSV₀ is fixed to
the electron, all other masses are determined by cage geometry via
E = (N/2) × SSV₀ (plus ZBW and bonding corrections from SM-2).

SSV₀ should be distinguished from sea_strength:
- SSV₀ = 0.2555 MeV is an energy (the per-unit SSV stress magnitude).
- sea_strength ≈ 0.178 is dimensionless (the DP coupling fraction).

They are related — both measure the strength of SSV-mediated interactions
— but at different levels of the framework. SSV₀ sets the overall energy
scale; sea_strength sets the fractional coupling efficiency. The exact
relationship between them is an open connection in SM-1, labelled as
the open problem feeding into OP-SS-1.

---

## Section 9: Open Problems Registered in SM-1

**OP-SS-1** (PARTIAL): Quark mass formula M_q(n) from cage depth and
sea_strength — the quantitative kernel connecting cage geometry to
exact quark masses. SM-1 establishes the qualitative ordering
(more cage depth → more mass) and the approximate scaling
E ≈ N/2 × SSV₀, but the exact formula is not derived.

**Open connection**: Relationship between SSV₀ = 0.2555 MeV (SM-1
calibration constant) and sea_strength × ℏc/r_conf (SM-3 ZBW thermal
energy scale). These two quantities should be consistent — they
both characterise the strong-sector energy scale — but their exact
relationship has not been derived.

**Open**: Derivation of σ = 120^{−d} from 600-cell geometry.
The suppression formula is motivated by the lattice dimensionality
argument but has not been proved from the 600-cell's edge structure.
