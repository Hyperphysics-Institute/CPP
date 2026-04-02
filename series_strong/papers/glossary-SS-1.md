# Glossary — SS-1: The Strong Sector from the 600-Cell Lattice

**Paper:** SS-1: The Strong Sector from the 600-Cell Lattice (cpp_ss_unified_v3.tex)
**Last updated:** 29 March 2026

*Each definition below describes the term as it is used in SS-1 specifically — not a general dictionary definition, but the concept as it actually functions in the paper's argument. Terms from the SR-1 glossary that appear in SS-1 with the same meaning are included here for completeness; terms used differently in the strong-sector context carry updated definitions. Novice readers: read these alongside mechanism-SS-1.md. Expert readers: use this as a rapid orientation to CPP vocabulary.*

---

## Core Lattice Structure

**600-cell**
The 4-dimensional polytope — 120 vertices, 720 edges, 1200 triangular faces, 600 tetrahedral cells — whose geometry is the substrate of space in CPP. In SS-1, the specific sub-structure of interest is the *tetrahedral cell*: each of the 600 regular tetrahedra embedded in the lattice is a potential host site for a qCP cage. The 600-cell is not chosen arbitrarily; it is the unique regular 4-polytope whose quasicrystalline tiling of ℝ⁴ produces exact Lorentz covariance with no preferred directions (proved in SR-1 Appendix G). In SS-1 it is used primarily for its local geometry: the tetrahedral cell, its base triangle, and the edge hopping operators defined on that triangle.

**Grid Point (GP)**
A fixed, permanent vertex of the 600-cell lattice — one of the 120 spatial markers per lattice unit. Grid Points do not move; they are the address system of space. Conscious Points move between Grid Points by executing displacements along lattice edges. In SS-1, the four vertices {V₁, V₂, V₃, V₄} of a tetrahedral cell are the Grid Points relevant to quark color and cage structure.

**Voronoi cell**
The region of space closer to a given Grid Point than to any other — the "territory" of one lattice vertex. In SS-1, the Voronoi cell geometry determines the sea_strength coupling constant via the stiffness integral α_geom (Section 8). The Voronoi cell is also the object whose volume compression by ΔSSV produces the Planck Sphere Radius reduction central to SR-1; here it provides the geometric source of the coupling between SSV energy density and Dipole Sea displacement capacity.

**Absolute Moment**
The fundamental tick of cosmic time — one Planck time duration (t_P ≈ 5.39 × 10⁻⁴⁴ s). At each Absolute Moment, every Conscious Point evaluates its incoming DI-bits and executes exactly one displacement along a lattice edge according to deterministic update rules. The Absolute Moment is universal and frame-independent; it is enforced by the atemporal Nexus, not by any causal signal propagating through space. In SS-1 it is the time unit underlying the ZBW oscillation frequency and all dynamic processes described.

**Atemporal Nexus**
The computational substrate that enforces DI-bit conservation and coordinates all Conscious Point updates at each Absolute Moment, operating outside the spacetime it organises. In SS-1, the Nexus is the source of gauge invariance: the DI-bit conservation it enforces at every Moment is the physical content of what QFT describes as local gauge symmetry. The Nexus does not propagate causal signals; it is not a physical object in spacetime but a computational fact about how the universe's rules are structured.

**DI-bit**
The fundamental conserved unit of information in CPP — the binary charge state (±1) of a Conscious Point together with its identity and location in the lattice. DI-bit conservation is enforced globally at every Absolute Moment by the atemporal Nexus. In SS-1, DI-bit conservation is the underlying reason color charge is conserved in all strong interactions: a gluon emitted when a quark changes color carries the DI-bit of the color change, ensuring the total color content of any reaction is preserved.

---

## Conscious Points and Their Types

**Conscious Point (CP)**
The fundamental entity of CPP — a ±1 charge carrier that executes one displacement per Absolute Moment along a 600-cell lattice edge according to deterministic rules. CPs are not classical particles (no trajectory between Moments) and not quantum fields (they are discrete and countable). In SS-1, two types of CP are relevant: eCPs (electron Conscious Points, charge ±1 in lepton units) and qCPs (quark Conscious Points, carrying fractional charge after screening). The word "Conscious" is not metaphorical — CPP makes the specific ontological claim that these entities perceive and respond to their local field environment. This terminology is retained precisely.

**qCP (quark Conscious Point)**
A Conscious Point that carries fractional electric charge and participates in the strong interaction. A positive qCP (+qCP) has bare charge +1 before screening and corresponds to the up-type quarks (u, c, t) after screening produces +2/3. A negative qCP (−qCP) has bare charge −1 before screening and corresponds to the down-type quarks (d, s, b) after screening produces −1/3. The qCP's color state — which of the three base vertices of its tetrahedral cage is currently occupied by the DP cloud — is what QCD calls color charge. In SS-1, the qCP's polarity (+/−) determines which quark type it represents; its cage configuration determines its generation (mass scale).

**eCP (electron Conscious Point)**
A Conscious Point that carries unit electric charge and participates in the electromagnetic and weak interactions but not the strong interaction. eCPs do not form tetrahedral cages; they form icosahedral and dodecahedral cages for the charged leptons (electron, muon, tau). In SS-1, eCPs appear primarily by contrast: where qCPs form tetrahedral cages and generate SU(3) color algebra, eCPs form different cage types and generate U(1) and SU(2) algebras in the EW sector.

---

## The Dipole Sea and Its Constituents

**Dipole Sea**
The CPP vacuum — all of space filled with randomly-oriented oscillating dipole pairs (DPs) at the Zitterbewegung frequency. The Dipole Sea is maximum entropy by default; its statistical randomness is what empty space means in CPP. Particles are stable departures from this randomness: regions where the Sea is locally organised by the SSV field of a central CP. In SS-1, the Dipole Sea plays two roles: (1) it is the source of qDP chains that mediate quark confinement, and (2) its stiffness properties — quantified by α_geom — determine the sea_strength coupling constant.

**DP (Dipole Pair)**
A pair of oppositely-charged Conscious Points bound by mutual SSV attraction and oscillating at the ZBW frequency. DPs are the constituents of the Dipole Sea. In SS-1, three types of DP are relevant: eDPs (electron-sector DPs), qDPs (quark-sector DPs), and hDPs (hybrid DPs — the CPP implementation of weak and strong bosons). The type of DP determines its energy scale and its coupling to different quark and lepton structures.

**hDP pair (Hybrid Dipole Pair)**
A DP whose charge composition spans both the electron and quark sectors, making it the carrier of interactions that bridge these sectors — specifically, the weak bosons and the gluons. In SS-1, transient hDP pairs propagating along tetrahedral edges are gluons (color-changing, massless). Stable closed hDP configurations are the massive weak bosons: the W bracelet, the Z icosahedral cage, the H dodecahedral cage. The word "hybrid" describes the charge mixture; the word "pair" describes the ±CP binding.

**qDP chain (Quark Dipole Pair chain)**
A linear sequence of qDP pairs spanning the space between two quarks inside a hadron. qDP chains are the CPP implementation of the colour-electric flux tube — the "string" in the Cornell potential V(r) = −α_s ℏc/r + σr. At separations beyond r_conf ≈ 0.16 fm, qDP chains self-collimate (lateral excursions are suppressed by ZBW dynamics) and the linear potential term becomes dominant. The string tension σ ≈ 0.9 GeV/fm is the energy per unit length of a self-collimated qDP chain. Approximately 99% of the proton mass is qDP chain energy — not the bare masses of the constituent quarks.

---

## The Tetrahedral Cage and Color

**Tetrahedral cage**
A regular tetrahedron formed by four Grid Points of the 600-cell lattice: apex V₄ (where the central qCP resides) and base vertices {V₁, V₂, V₃} (the color triplet). The tetrahedral cage is the CPP model identification for a quark: a qCP-plus-cage configuration. This identification is a *model postulate* — geometry derives the SU(3) algebra from the cage, but the identification of this structure with physical quarks is a foundational claim of CPP, not a consequence of the geometry alone. The cage is additional mass-generating structure: u and d quarks have no polyhedral cage (they are bare qCPs with ZBW clouds); the strange quark acquires a tetrahedral cage; heavier quarks acquire successive cage shells.

**Cage base (K₃ graph)**
The equilateral triangle {V₁, V₂, V₃} formed by the three base vertices of the tetrahedral cage. This triangle is the geometric object from which both the color algebra and the charge fraction δ = 1/3 are derived. It is also the object from which the Koide lepton mass relation K = 2/3 is derived in SM-3 via its spectral structure. The same geometric object — an equilateral triangle with three-fold rotational symmetry — encodes quark color (via vertex occupancy), fractional charge (via C₃ combinatorics), and lepton mass ratios (via K₃ eigenvalues). In SS-1 specifically, the cage base is the arena for the 8 gluon operators and the C₃ color symmetry.

**V₁, V₂, V₃ (base vertices)**
The three Grid Points forming the equilateral base of the tetrahedral cage. Their occupancy by the DP cloud determines the quark's color state: V₁ → red, V₂ → green, V₃ → blue. The three vertices are geometrically identical — same distance from V₄, same distance from each other, same local lattice environment — which is why red, green, and blue are physically equivalent (color is not observable in isolation). In SS-1, the edges connecting these three vertices generate the six color-changing gluon operators; the phase differences between them generate the two color-neutral gluon operators.

**V₄ (apex vertex)**
The Grid Point at the apex of the tetrahedral cage where the central qCP resides. V₄ is the "seat" of the quark: the qCP's SSV field radiates from V₄, polarising the Dipole Sea in the three base-vertex directions and establishing the three color states. V₄ is not one of the color states — it is the quark itself. Color is a property of the base, not the apex.

**Color charge**
In SS-1, color charge is not an intrinsic quantum number of the qCP. It is a relational property: which of the three base vertices {V₁, V₂, V₃} currently hosts the DP cloud of the tetrahedral cage. A quark is "red" if V₁ is occupied, "green" if V₂ is occupied, "blue" if V₃ is occupied. This is the entire content of color in CPP. The C₃ rotational symmetry of the equilateral base triangle — the fact that V₁ → V₂ → V₃ → V₁ is an exact geometric symmetry — is why the three colors are equivalent and why no single color is observable in isolation.

**Color-neutral**
A hadronic state in which the three base vertices are all occupied (baryon: one red quark occupying V₁, one green occupying V₂, one blue occupying V₃) or a vertex-antivertex pair cancels (meson: quark occupying Vₖ, antiquark occupying anti-Vₖ). In both cases, the SSV fields of the individual color charges cancel at long range, producing no net color field. Color neutrality is the geometric condition for hadron stability: only configurations with zero net long-range color SSV field are energetically bounded.

**C₃ symmetry**
The three-fold rotational symmetry of the cage base triangle: the rotation V₁ → V₂ → V₃ → V₁ is an exact isometry of the equilateral triangle. In SS-1, C₃ symmetry is what makes the three color states equivalent (no color is preferred over another) and is what forces the charge fraction δ = 1/3 exactly: if the three base vertices are equivalent (C₃) and together they account for all the screening (completeness), then each contributes exactly 1/3. This is Theorem 1 of SM-1, invoked in SS-1's charge discussion.

---

## The Gluons and SU(3) Algebra

**Gluon**
In SS-1, a gluon is a transient hDP pair propagating along a single open edge of the tetrahedral cage base. When the DP cloud hops from base vertex Vᵢ to vertex Vⱼ (a color change), the ZBW oscillation emits an hDP pair along the edge Vᵢ–Vⱼ. This pair propagates through the Dipole Sea carrying the color-change information. The gluon has two defining properties: (1) it is massless, because it is an open-path structure with no closed confinement geometry; (2) it carries color charge (it is itself colored), because the edge hop changes color and the emitted hDP pair carries the color difference. Eight distinct gluons arise from the three cage edges and their real/imaginary hopping modes plus two diagonal phase operators.

**Gell-Mann matrices (λᵃ)**
The eight standard basis matrices for traceless Hermitian operators on ℂ³ — the standard generators of SU(3). In SS-1, the Gell-Mann matrices appear as the *result* of a geometric computation, not as inputs. The eight tetrahedral hopping operators Tᵃ are computed from the cage geometry and found to equal λᵃ/2 exactly (verified to residual < 10⁻¹⁶). This is a theorem, not a postulate: the operators were derived, then found to match the known matrices. The Gell-Mann matrices are in this sense a consequence of tetrahedral geometry in CPP.

**SU(3) structure constants (f^{abc})**
The numerical coefficients in the commutation relation [Tᵃ, Tᵇ] = if^{abc}Tᶜ — the defining algebraic property of SU(3). In SS-1, the structure constants are computed from the commutators of the eight tetrahedral hopping operators and verified against the standard PDG values (Table 2 of SS-1). The nonzero values (e.g., f¹²³ = 1, f¹⁴⁷ = 1/2, f⁴⁵⁸ = √3/2) are derived from the cage geometry. Their physical meaning: f^{abc} ≠ 0 for a given triple (a,b,c) means that a gluon of type a interacting with a gluon of type b can produce a gluon of type c — the gluon self-coupling that makes QCD non-Abelian.

**Casimir invariants (C_A, T_F, C_F)**
Numerical constants that characterise how strongly a given representation of SU(3) couples to the algebra. In SS-1, all three are derived from Theorem 1 (the SU(3) algebra proof):
- C_A = 3: the adjoint Casimir, quantifying gluon self-coupling strength. Derived from the structure constant identity Σ_{bc} f^{abc}f^{abc} = C_A δ^{aa}.
- T_F = 1/2: the fundamental representation trace factor, from Tr(TᵃTᵇ) = T_F δᵃᵇ.
- C_F = 4/3: the fundamental Casimir, from Σ_a TᵃTᵃ = C_F · 1. Physical meaning: a quark in a color field is screened by a factor of 4/3 compared to a simple charge.
All three are verified numerically to < 10⁻¹⁰.

---

## Confinement and Asymptotic Freedom

**Confinement**
In SS-1, quark confinement is *energetic*, not topological. A free qCP is not geometrically forbidden — it is energetically suppressed. When quarks separate, qDP chains from the Dipole Sea span the gap and self-collimate beyond r_conf ≈ 0.16 fm, creating a linear potential V(r) = σr whose energy grows without bound. It is always energetically cheaper to break the chain (creating a quark-antiquark pair from the Dipole Sea) than to extend it to infinite separation. Confinement is therefore a consequence of qDP chain self-collimation dynamics, not a topological constraint. Importantly, this means confinement is *temperature-dependent*: above the QCD transition temperature, thermal energy prevents self-collimation and quarks are effectively free — the quark-gluon plasma.

**String tension (σ)**
The energy per unit length of a self-collimated qDP chain — the linear coefficient in the Cornell potential V(r) = −α_s ℏc/r + σr. In SS-1, σ ≈ 0.9 GeV/fm is calibrated to the charmonium/bottomonium spectrum. The geometric origin of σ in CPP is the elastic bow rigidity of the qDP chain: when pulled, the chain bows transversely rather than breaking immediately, storing elastic potential energy proportional to extension. Deriving σ from sea_strength and 600-cell geometry — expressing the bow factor in terms of CPP primitives — is Open Problem OP-SS-2.

**Confinement radius (r_conf)**
The separation at which qDP chains transition from random (short range) to self-collimated (long range) behaviour — approximately 0.16 fm in SS-1. Below r_conf, the Coulomb-like 1/r term dominates the Cornell potential; above r_conf, the linear σr term dominates. Physically: at separations below r_conf, ZBW oscillations of the chain's constituent qDP pairs produce enough lateral turbulence to prevent self-collimation; at separations above r_conf, the chain length is great enough that the ZBW phases average out and self-collimation is spontaneous.

**Asymptotic freedom**
The vanishing of the strong coupling α_s at short distances (high energies). In SS-1, the mechanism is PSR saturation: as two quarks approach to within a few Planck lengths, the effective PSR shrinks and the Dipole Sea cannot nucleate qDP chains fast enough to self-collimate between the rapidly-approaching quarks. No self-collimated chains → no linear potential → α_s → 0. The algebraic capture of this is the β-function coefficient β₀ = 7 > 0 (Theorem 4 of SS-1), which guarantees that α_s decreases with increasing energy scale.

**PSR saturation**
The physical mechanism underlying asymptotic freedom in CPP. PSR (Planck Sphere Radius) is the local interaction range of a Conscious Point. Under SSV compression from kinetic or gravitational energy, PSR_eff = l_P/(1 + k·ΔSSV) shrinks toward its minimum. At short quark separations, the SSV density between quarks is very high, compressing PSR_eff severely. With a compressed PSR, qDP chains cannot form and self-collimate fast enough to transmit the confining force — the Dipole Sea's response is too slow relative to the quarks' approach speed. The result is a weaker effective coupling at shorter distances, which is asymptotic freedom.

**β-function coefficient (β₀)**
The leading-order coefficient governing how α_s changes with energy scale: α_s(Q) decreases with Q because β₀ > 0. In SS-1, β₀ = 11C_A/3 − 4T_F n_f/3 = 11×3/3 − 4×½×6/3 = 7. All three inputs (C_A = 3, T_F = 1/2 from Theorem 1; n_f = 6 from the six cage configurations of Table 1) are derived from the 600-cell cage geometry. β₀ = 7 is arithmetic from these derived inputs — it is not a free parameter.

**Cornell potential**
The phenomenological quark-antiquark potential V(r) = −α_s ℏc/r + σr, where the first term is a short-range Coulomb-like attraction and the second term is the long-range linear confinement. In SS-1, this potential is *reproduced* by the qDP chain mechanism (not derived from scratch): the short-range term comes from SSV exchange between the qCPs, and the linear term comes from the self-collimated qDP chain energy. The value σ ≈ 0.9 GeV/fm is calibrated to charmonium; its derivation from CPP first principles is Open Problem OP-SS-2.

---

## The Coupling Constants

**sea_strength**
The overall coupling constant of the SSV field interaction between Dipole Sea pairs — in SS-1 a dimensionless number ≈ 0.185. It sets the energy scale of the strong interaction and enters the confinement radius, the string tension, and the quark mass formula. In SS-1, sea_strength is shown to be derived to within 3.8% from the 600-cell Voronoi stiffness integral: sea_strength = (N_lattice/z) × α_geom/(z·φ²) = 10 × 0.55936/(12 × 2.618) ≈ 0.178. The 3.8% residual is identified as the stereographic S³→ℝ³ projection correction; its analytic derivation is deferred to the Stiffness C companion. Previously this was a calibrated constant; its derivation from geometry is the principal new result of SS-1 Section 8.

**α_geom (geometric invariant)**
The exact algebraic constant α_geom = 3(11 + 5√5)√(5+√5)/320 ≈ 0.5594, derived from the H₄ Voronoi stiffness integral of the 600-cell. This constant is a pure geometric invariant — it depends only on the golden ratio φ and the icosahedral coordination structure of the 600-cell. In SS-1, it is the source of sea_strength (via k_SM = α_geom/(12φ²) and sea_strength = 10·k_SM). The same constant appears independently in the SR-1 coupling constant k_rel and the CPP electromagnetic stiffness derivation — its appearance across three independent physical sectors (relativistic, electromagnetic, strong) is evidence of the 600-cell's role as the unified geometric substrate.

**k_SM**
The SSV energy coupling per lattice vertex per shell unit: k_SM = α_geom/(12φ²) ≈ 0.01781. Derived from the 600-cell coordination number z = 12, the golden ratio φ² ≈ 2.618, and α_geom. In SS-1, k_SM connects the Voronoi geometric structure to the physical sea_strength coupling: sea_strength = 10·k_SM, where the factor 10 = N_lattice/z = 120/12 counts the number of coordination shells that tile the full lattice.

---

## Quark Structure

**Inner orbital ZBW (Zitterbewegung)**
The inner of two orbiting Dipole Sea pairs that every quark carries — oscillating at twice the frequency of the outer orbital (2:1 inner-to-outer frequency ratio). The inner orbital is the quark's spinor structure, producing spin-½ in the same way as the electron's orbital ZBW. In SS-1, the inner orbital provides the first +1/3 charge screening for both up-type and down-type quarks: the inner orbital DP spends an increased fraction of its time in the tightly-bound 1/r³ dipole configuration (relativistic time dilation in the high-centripetal-acceleration regime), partially neutralising the central qCP charge. The C₃ geometric proof establishes that this screening is exactly 1/3; the ZBW mechanism should agree quantitatively (Open Problem OP-SS-new-3).

**Linear ZBW DP**
An additional Dipole Sea pair oscillating along the radial direction — present in all down-type quarks (d, s, b) and absent from all up-type quarks (u, c, t). The linear ZBW DP is the structural feature that distinguishes down-type from up-type quarks. It provides a second +1/3 charge screening, bringing the down-type quark charge from (−1 + 1/3) = −2/3 to (−1 + 1/3 + 1/3) = −1/3. The presence of this additional DP is also the structural reason that the W bracelet interaction — which transforms up-type to down-type — must acquire or release a linear ZBW DP during the flavor transition, with the W acting as the catalyst.

**Up-type quark**
A quark with a positive central qCP (+qCP), inner orbital ZBW, and no linear ZBW DP. Net charge after screening: +2/3. The three up-type quarks — u, c, t — have zero, two, and four polyhedral cage layers respectively. In SS-1, the up-type designation is associated with the +qCP polarity; the down-type designation with the −qCP polarity. Every quark flavor transition between up-type and down-type involves the central qCP switching polarity, mediated by the W bracelet.

**Down-type quark**
A quark with a negative central qCP (−qCP), inner orbital ZBW, *and* a linear ZBW DP. Net charge after screening: −1/3. The three down-type quarks — d, s, b — have zero, one, and three polyhedral cage layers respectively. The linear ZBW DP is structurally universal across all three down-type quarks; it is not an additional feature of the strange or bottom quark but a defining feature of the down-type category.

**Cage depth (cage layers)**
The number of nested polyhedral cage shells surrounding the central qCP. Each additional shell adds SSV compression energy and therefore rest mass:
- 0 layers: u, d (bare qCPs, no polyhedral cage — ZBW cloud only)
- 1 layer: s (tetrahedral cage, 4 vertices)
- 2 layers: c (tetrahedral + icosahedral, 4+12 = 16 vertices)
- 3 layers: b (+ dodecahedral, 16+20 = 36 vertices)
- 4 layers: t (+ 30-vertex shell, 36+30 = 66 vertices)

The mass scale rises by roughly an order of magnitude per additional cage layer. This qualitative ordering is proved (Theorem 9 of SS-1: strict mass ordering m_u < m_d < m_s < m_c < m_b < m_t); the quantitative formula is Open Problem OP-SS-1.

---

## The W Boson and Flavor Transitions

**W₀ bracelet**
The W boson in CPP: a closed ring (bracelet) of hDP pairs. The ring topology gives the W its mass (closed structure with f_geom > 0 — unlike the open-path gluon). Unlike the Z's icosahedral cage (which couples symmetrically to all vertices), the bracelet presents a *locally linear coupling face* to the qCP at the point of interaction: the relevant geometry is a linear segment of the ring. This directional asymmetry is the geometric origin of the W's polarity-inverting coupling. The W acts as a catalyst in quark flavor transitions: it mediates the +qCP ↔ −qCP switch without being consumed, while the quark's cage structure transforms accordingly (acquiring or releasing a linear ZBW DP). (Conjectural: CJ-SS-new-1, CJ-SS-new-2; rigorous derivation is Open Problem OP-SS-new-2.)

**Flavor transition (quark)**
The process by which a quark changes from one flavor to another — for example, a u quark (up-type, +qCP) becoming a d quark (down-type, −qCP). In SS-1, every such transition involves: (1) the central qCP switching polarity (+→− or −→+), mediated by the W bracelet; (2) a corresponding change in the cage's linear ZBW DP content (absent in up-type, present in down-type); (3) the W bracelet acting as the catalyst, providing the charge exchange that drives the polarity switch. This picture is observationally consistent with all known quark decay pathways and has been checked systematically across generations; formal proof from CPP EW-strong coupling is Open Problem OP-SS-new-2.

---

## Hadron Properties

**Gell-Mann–Okubo (GMO) relations**
Mass formulae for hadron multiplets that follow from the Casimir structure of SU(3)_flavor. In SS-1, the GMO relations are derived consequences of Theorem 1 (the SU(3) algebra) — they require no additional postulates. Key predictions: the baryon octet relation (0.6% agreement with PDG), the decuplet equal-spacing rule (exact), and the Ω⁻ mass prediction (1681 MeV vs PDG 1672.5 MeV, 0.5% agreement). The Ω⁻ prediction was historically the most dramatic confirmation of SU(3) flavor symmetry; in CPP it is a corollary of the geometric derivation.

**Chiral limit**
The theoretical regime m_u, m_d → 0. In SS-1, the pion mass vanishes exactly in this limit (Theorem 5). The physical reason: u and d quarks have no polyhedral cage; their constituent mass is entirely ZBW-driven and vanishes with their current mass. The pion (a ud̄ pair with no cage binding) therefore has no residual mass source in the chiral limit. This is the CPP account of the Nambu-Goldstone boson: the pion is light not because it is special but because it is composed of the two lightest quarks, which have no cage.

**Quark-gluon plasma**
The deconfined phase of QCD matter at temperatures above approximately 150 MeV (~1.7 × 10¹² K). In CPP, this corresponds to the regime where thermal energy exceeds the qDP chain self-collimation threshold: the chains cannot maintain their linear flux tube structure against the thermal disruption of the Dipole Sea. With no self-collimated chains, there is no linear potential, no confinement, and qCPs move as effectively free particles. The QCD transition temperature from the CPP perspective is the temperature at which kT ≈ σ·r_conf — the thermal energy sufficient to disrupt chain self-collimation at the confinement scale. Deriving this temperature from sea_strength and 600-cell geometry is Open Problem OP-SS-new-4.

---

## Open Problems Registered in SS-1

**OP-SS-1** — Quark mass formula from cage depth: derive M_q(n_layers) as a function of sea_strength and 600-cell geometry, requiring no free parameters beyond geometry. Leading candidate: K₃ thermal picture (ZBW Schrödinger equation with cage boundary conditions).

**OP-SS-2** — String tension σ from sea_strength: express the bow factor of qDP chain self-collimation in terms of CPP primitives, giving σ and r_conf from first principles.

**OP-SS-new-1** — Uniqueness of SU(3) operator mapping: prove the 8 tetrahedral hopping operators are the unique set consistent with C₃ cage symmetry.

**OP-SS-new-2** — W bracelet polarity inversion from first principles: prove from CPP EW-strong coupling that the bracelet's locally-linear coupling face *requires* qCP polarity switching.

**OP-SS-new-3** — ZBW mechanism for δ = 1/3: derive from the relativistic 1/r³ time fraction that exactly 1/3 charge is neutralised; confirm agreement with the C₃ geometric proof.

**OP-SS-new-4** — QCD deconfinement temperature from CPP: derive the temperature at which thermal energy disrupts qDP chain self-collimation, giving the QCD phase transition from first principles.
