# CPP Propositions, Theorems and Corollaries — Partner-Switching Session

**Session date:** 29–30 March 2026
**Participants:** Thomas Lee Abshier ND, Claude Sonnet (Anthropic)
**Source conversation:** SM-1 documentation → ZBW mechanism discussion →
partner-switching Sea pressure → QM implications
**Last updated:** 30 March 2026
**Repo location:** CPP top level (peer of postulates_and_theorems.md)

*This file records all new theoretical items generated during the
partner-switching session. Items are listed in the order they were
identified, with full statements suitable for incorporation into
the main postulates_and_theorems.md registry.*

---

## Summary of New Items

| ID | Type | Title |
|----|------|-------|
| T-CPP-1 | Theorem | CP Non-Persistent Co-Occupation (replaces P-exclusion postulate) |
| C-CPP-1a | Corollary | ZBW Turning Point at Grid Point Superimposition |
| C-CPP-1b | Corollary | Stochastic Partner Exchange in the Dipole Sea |
| P-CPP-1 | Proposition | Random Walk of Central CP and Quantum Position Uncertainty |
| P-CPP-2 | Proposition | Solitonic (Rogue Wave) Tunneling Mechanism |
| P-CPP-3 | Proposition | Tetrahedral Cage as Unique Minimum Stable Cage |
| P-CPP-4 | Proposition | Elastic Tunneling via Cage Dissolution and Reformation |
| P-CPP-5 | Proposition | Radial DP Chain Equilibrium Length |
| P-CPP-6 | Proposition | Relativistic DP Chain Compaction as the de Broglie Wavelength |
| P-CPP-7 | Proposition | Cage Reformation from Partner-Transitioning Sea CPs |
| P-CPP-8 | Proposition | Dual Stable Configurations of the Central −eCP |
| P-CPP-9 | Proposition | Atomic Orbital Probability Density as DP Chain Standing Waves |
| P-CPP-10 | Proposition | Electron Identity Transfer and the Orbital Born Rule |
| P-CPP-11 | Proposition | Virtual Particles as Transient CP Configurations Constrained by Gauss's Law |
| P-CPP-12 | Proposition | Critical Separation Distance for Real Pair Production |
| P-CPP-13 | Proposition | Photon Pair Production via Lorentzian Asymmetry |
| P-CPP-14 | Proposition (Definition) | Mass as Thermodynamic Nucleation-Dissipation Boundary |
| P-CPP-15 | Proposition | Pair Annihilation as Isentropic vs Non-Isentropic Cage Dissolution |

**New open problems:** OP-QM-new-1 through OP-QM-new-8 (see Section 3)

**Postulate demotion:** P5 (ZBW oscillations) is no longer an axiom —
it is derivable from P3+P4 as T-CPP-1 demonstrates. See Section 4.

**SSV distinction registered:** SSV_net vs SSV_abs are formally
distinct quantities requiring separate glossary entries. See Section 5.

---

## Section 1: Theorem and Corollaries

### T-CPP-1: CP Non-Persistent Co-Occupation
*(Replaces the CP Exclusion Postulate — that postulate is now redundant)*

**Statement:** Two Conscious Points cannot persistently occupy the
same Grid Point.

**Proof structure:**

*Case 1 — Same-polarity pair:* The SSV_net on CP A from CP B of the
same polarity is repulsive and grows monotonically as A approaches B
(1/r² dependence). No reversal of SSV_net occurs before superimposition.
Same-polarity CPs are driven apart before they can reach the same Grid
Point. Same-polarity CPs never superimpose under the SSV force law.

*Case 2 — Opposite-polarity pair:* SSV_net is attractive throughout
the approach and increases monotonically as separation decreases. There
is no logical point of SSV_net reversal before superimposition — the
attractive force grows all the way to the Grid Point occupied by the
partner. At superimposition (both CPs at the same Grid Point), the
intra-pair direction vector r̂_{A→B} is undefined — no directional
contribution to SSV_net from the partner. The SSV_net at the shared
Grid Point is governed entirely by the bulk Dipole Sea. Because A and
B have opposite polarities, they respond to the same bulk SSV_net
vector with opposite displacements: they separate on the next Absolute
Moment. Superimposition is therefore transient — lasting exactly one
Absolute Moment — not a persistent state. □

**Consequence:** The CP Exclusion Postulate is redundant. Persistent
co-occupation of a Grid Point by two CPs is prevented by the SSV
force law for same-polarity pairs (never approach) and by the
geometry of opposite-polarity superimposition (one-Absolute-Moment
transience). The CP Exclusion Postulate should be removed from the
CPP postulate list and replaced by this theorem.

**Key postulates used:** P1 (CPs), P2 (lattice discreteness), P4 (SSV force law)

---

### C-CPP-1a: ZBW Turning Point at Grid Point Superimposition

**Statement:** The turning point of the ZBW oscillation of a bound
DP pair occurs at Grid Point superimposition — the single Absolute
Moment when both CPs occupy the same Grid Point — not at any prior
Grid Point during the approach phase.

**Derivation:** The SSV_net on A(−) from B(+) is attractive and
monotonically increasing in magnitude throughout the approach (1/r²
dependence, r decreasing step by step). No reversal of SSV_net
direction occurs at any intermediate Grid Point. The direction of
SSV_net on A from B becomes undefined only at r = 0 (superimposition).
After superimposition, the bulk SSV_net at the shared Grid Point
drives A and B apart in opposite directions. □

**Implication for ZBW frequency:** The ZBW period is the number of
Absolute Moments required to traverse from maximum separation to
superimposition and back. For a minimal-amplitude oscillation
(nearest-neighbour separation d₀), the period is approximately 2
Absolute Moments, giving f_ZBW ≈ 1/(2t_P). This is a derived
consequence of the lattice step size and SSV force law, not an
independent postulate. **P5 (ZBW oscillations) is demoted from
postulate to theorem** — the ZBW frequency emerges from P4 (SSV
force law) and P2 (lattice), rather than being independently assumed.

**Follows from:** T-CPP-1

---

### C-CPP-1b: Stochastic Partner Exchange in the Dipole Sea

**Statement:** The partnership identity of Dipole Pairs in the Dipole
Sea is not persistent. After each superimposition event, each CP's
next partner is determined by the dominant SSV_net at the CP's
post-superimposition Grid Point, which need not be its previous partner.

**Mechanism:** After superimposition, A(−) departs to a new Grid Point
GP_new under the bulk SSV_net. The SSV_net at GP_new is the vector sum
of contributions from all nearby CPs — the prior partner B(+) at
distance r_AB, and all competing Sea CPs. Whichever CP C(+)
contributes the strongest SSV_net toward A at GP_new becomes A's
next partner. No binding mechanism forces re-pairing with B; the
SSV force law is local and moment-by-moment.

**Consequence:** The Dipole Sea is a gas of transient partnerships
renewed each ZBW cycle — not fixed DP molecules. The rate of partner
exchange depends on the local CP density and the relative magnitudes
of intra-pair vs inter-pair SSV_net at each post-superimposition
location. This stochastic partner exchange is the physical mechanism
underlying quantum position uncertainty, tunneling, virtual particles,
and atomic orbital probability density (see P-CPP-1 through P-CPP-10).

**Follows from:** T-CPP-1, C-CPP-1a

---

## Section 2: Propositions

### P-CPP-1: Random Walk of the Central CP and Quantum Position Uncertainty

**Statement:** The central CP of a fermion executes a stochastic
random walk through the 600-cell lattice as a consequence of ZBW
partner switching, producing a position probability distribution
whose RMS width corresponds to the quantum mechanical position
uncertainty Δx.

**Physical mechanism:** At each ZBW cycle, the central CP undergoes
superimposition with a cage or Sea CP. After separation, the bulk
SSV_net at the post-superimposition Grid Point is stochastic — it
includes contributions from the cage CPs, Sea DPs, and competing
nearby CPs. The next Grid Point of the central CP is therefore not
deterministic. Over N ZBW cycles, the central CP's displacement from
its initial position grows as √N × l_P. The probability distribution
of central CP locations is the CPP account of |ψ(x)|².

**Connection to Born rule:** Regions of high SSV_abs have compressed
PSR — each lattice step covers less physical distance. The central
CP visits high-SSV_abs regions less frequently per unit of physical
volume. The probability per unit physical volume is therefore weighted
inversely by the local SSV_abs — the CPP account of |ψ|² as a
field-weighted position probability. The Born rule emerges from the
metric-compression effect of SSV_abs without being independently
postulated.

**Status:** Proposition — physically motivated. The quantitative
connection between the random walk amplitude and ℏ requires
identifying the CPP account of Planck's constant (see OP-QM-new-1).

**Postulates used:** P1, P2, P3, P4; follows from C-CPP-1b

---

### P-CPP-2: Solitonic (Rogue Wave) Tunneling Mechanism

**Statement:** Quantum tunneling of a particle across an energy barrier
occurs when a rogue-wave stochastic superposition of SSV_net vectors
arriving at the central CP's Grid Point from surrounding Sea CPs and
cage CPs produces a rare large-amplitude SSV_net spike sufficient to
displace the central CP across the barrier width in a single Absolute
Moment or small number of Moments.

**Mechanism:** At each Absolute Moment, the central CP receives SSV_net
contributions from every CP and DP within its PSR. Normally these sum
to approximately zero at the cage centre (cage T_d symmetry cancels
cage contributions; Sea contributions are randomised). On rare occasions,
by constructive superposition analogous to rogue wave formation, a large
fraction of the stochastic Sea vectors align in the same direction,
producing an SSV_net spike far above the typical fluctuation. The spike
displaces the central CP in the spike direction by a distance potentially
exceeding the barrier width.

**Statistical character:** For N independent SSV_net vectors of mean
magnitude μ contributing at one Grid Point:
P(|SSV_net_total| > A) ∝ exp(−A²/Nμ²)
The barrier height enters as an energy threshold on the required spike
amplitude, giving tunneling probability:
P(tunnel per ZBW cycle) ∝ exp(−V_b/Nμ²)
This reproduces the exponential WKB tunneling dependence from pure
SSV_net statistics, without wave mechanics.

**Note on terminology:** This mechanism involves the rogue-wave
stochastic superposition of Sea SSV_net vectors at the central CP's
near-side location — not a geometric partner-switching from a far-side
CP. The central CP is ejected from the near side by a statistical
anomaly in its own local SSV_net environment.

**Status:** Proposition — physically motivated; quantitative derivation
requires OP-QM-new-3.

---

### P-CPP-3: Tetrahedral Cage as Unique Minimum Stable Cage

**Statement:** The regular tetrahedron (N=4 same-polarity cage CPs
around an opposite-polarity central CP) is the unique minimum
configuration that simultaneously satisfies two independent stability
conditions: (a) energetic stability — total SSV potential energy is
negative (cage is bound); (b) geometric completeness — T_d symmetry
cancels all SSV_net multipole moments at the central CP, producing
a force-free equilibrium.

**Energetic stability argument:**
Total potential energy U = U_attraction + U_repulsion
= −N × SSV₀/r_c + (N(N−1)/2) × SSV₀/r_v

For N=4 (tetrahedron): r_v ≈ 1.633 r_c, 6 repulsive pairs:
U_tetra ≈ SSV₀/r_c × (−4 + 3.67) = −0.33 SSV₀/r_c < 0 ✓ (bound)

For N=12 (icosahedron): r_v ≈ 1.051 r_c, 30 repulsive pairs:
U_icosa ≈ SSV₀/r_c × (−12 + 28.5) = +16.5 SSV₀/r_c > 0 ✗ (unbound)

The 12-vertex icosahedral arrangement of same-polarity CPs is
energetically unbound — mutual repulsion overwhelms central attraction.
The electron cage is tetrahedral, not icosahedral.

**Geometric completeness argument:** The regular tetrahedron's T_d
symmetry group causes the vector sum of the four unit vectors from
centre to vertices to be exactly zero. The SSV_net on the central CP
from all four cage CPs therefore cancels exactly in all directions.
For N < 4, residual multipole moments create a net SSV_net on the
central CP — no stable equilibrium exists. For N = 4 in tetrahedral
arrangement, all multipole moments vanish simultaneously.

**Consequence:** The tetrahedral cage is the unique cage geometry
where energetic binding and force-free equilibrium coincide. It is
not an arbitrary choice — it is the only geometry available to a
cage eCP system in the 600-cell nearest-neighbour shell.

**Postulates used:** P1, P2, P4

---

### P-CPP-4: Elastic Tunneling via Cage Dissolution and Reformation

**Statement:** During a tunneling event driven by a rogue wave SSV_net
spike (P-CPP-2), the central −eCP crosses the barrier while the cage
+eCPs remain at their original positions. The cage dissolves,
releasing its organisational energy into the Dipole Sea isotropically.
No photon is emitted. The −eCP immediately reforms an identical cage
from partner-transitioning Sea CPs on the far side of the barrier.
The tunneling is elastic: mass and charge are conserved.

**Four-phase mechanism:**

Phase 1 (Rogue wave displacement): The SSV_net spike acts on the
central −eCP at its specific Grid Point in one Absolute Moment. The
four cage +eCPs are at different Grid Points and experience independent
SSV_net summations — the probability of a correlated rogue wave at
all five Grid Points simultaneously is negligible. The central −eCP
is displaced across the barrier; the cage +eCPs remain.

Phase 2 (Chain dissipation): The four radial DP chains lose their
anchor. Previously held in tetrahedral geometry by the central CP's
SSV field, the chains experience loss of radial tension and dissipate
their organisational energy into the surrounding Dipole Sea.

Phase 3 (Isotropic dissipation — no photon): The chains were arranged
tetrahedrally — symmetrically in all directions. Their dissipation is
therefore spherically symmetric. No preferred emission direction exists.
No photon can form: photon formation requires a directed, linearly
polarised DP chain with a preferred axis.

**Testable prediction:** Tunneling electrons emit no photons during
barrier transit. This is consistent with observation.

Phase 4 (Cage reformation): The −eCP arrives at the far-side Grid Point
and immediately polarises the local Dipole Sea. Partner-transitioning
+eCPs from the Sea are intercepted by the strong SSV_net of the central
CP. The tetrahedral cage geometry reforms because it is the SSV energy
minimum regardless of which specific +eCPs fill the four positions.
The cage reforms with identical mass and charge.

**Identity principle:** The electron's identity during transit is
carried solely by the central −eCP. The cage is a statistical structure
that dissolves and identically reforms. The electron is not a rigid
extended object — it is a point-like −eCP that repeatedly recruits
a local cage from whatever Sea CPs are available.

**Energy accounting:** SSV₀ × 2 = 0.511 MeV deposited into Sea during
dissolution; 0.511 MeV extracted from Sea during reformation. Net
change: zero. Tunneling is elastic.

**Status:** Proposition — mechanism consistent with all known tunneling
observations. Quantitative rate calculation requires OP-QM-new-3.

---

### P-CPP-5: Radial DP Chain Equilibrium Length

**Statement:** Each of the four radial DP chains extending from the
tetrahedral cage vertices reaches an equilibrium length r_chain set
by the balance of three competing forces: (a) radial SSV attraction
toward the central CP (inward); (b) lateral inter-chain SSV repulsion
driving chains outward at close spacing; (c) thermal DP Sea exchange
dissolving chain integrity beyond the point where the central CP's
SSV field falls below the thermal fluctuation amplitude.

**Physical derivation:** The equilibrium condition:
SSV₀/r_chain² = sea_strength × SSV₀/d_Sea²
gives r_chain ~ d_Sea/√sea_strength

The physical interpretation: r_chain is the radius at which the
central CP's SSV field, attenuated by 1/r², equals the thermal
fluctuation amplitude of the Sea (proportional to sea_strength × SSV₀).
Beyond r_chain, thermal partnership switching dominates chain integrity
and the chain dissolves into the bulk.

**Predicted value:** r_chain is the CPP candidate for the classical
electron radius r_e ≈ 2.82 × 10⁻¹⁵ m. Whether the CPP equilibrium
length equals r_e when computed from SSV₀ and sea_strength is an
open calculation (OP-QM-new-4).

**Mass implication:** The radial chain organisational energy (the
energy stored in four chains of DP pairs out to r_chain) constitutes
an additional mass contribution beyond the tetrahedral cage binding
energy of 2 SSV₀. This chain energy may require revising the SM-1
calibration: if the chain energy is non-negligible, SSV₀ = 0.2555 MeV
calibrated from cage binding alone may need to partition the 0.511 MeV
between cage and chain contributions (OP-QM-new-5).

**Status:** Proposition — physically motivated; quantitative derivation
requires OP-QM-new-4.

---

### P-CPP-6: Relativistic DP Chain Compaction as the de Broglie Wavelength

**Statement:** At high velocity, the increased SSV_abs at each chain
DP's Grid Point (from kinetic energy via the PSR compression formula
PSR_eff = l_P/(1 + k·ΔSSV)) reduces the physical distance between
consecutive chain DPs at their equilibrium lattice positions. The
spatial period of the cage-plus-chain structure in physical units
decreases as 1/γ with increasing velocity, reproducing the de Broglie
wavelength λ = h/p without a wave postulate.

**Mechanism:** High velocity → high KE → high SSV_abs → PSR compressed
→ metric compressed at chain locations → more DPs per physical unit
length in each chain → denser, shorter, more compact cage-plus-chain
structure → shorter spatial period → shorter de Broglie wavelength.

**Wave-particle duality:** At low velocity, the chain structure has
a long spatial period — the electron is wave-like (long λ_dB,
interference, diffraction). At high velocity, the chain compresses —
the particle is particle-like (short λ_dB, well-defined trajectory).
This is not a philosophical shift between two descriptions but a
continuous mechanical compression of the same physical structure.

**Unification:** SR-1's Lorentzian metric compression and SM-1's chain
structure are not separate physics. The relativistic compaction of the
electron is the SSV_abs-driven compression of its DP chain cloud.
The matter wave is the spatial periodicity of the electron's own
organisational structure under relativistic compression.

**Status:** Proposition — physically motivated; quantitative derivation
requires connecting SSV_abs at chain DP Grid Points to the standard
Lorentz factor γ = 1/√(1−v²/c²).

---

### P-CPP-7: Cage Reformation from Partner-Transitioning Sea CPs

**Statement:** The cage +eCPs that form around a newly-arrived central
−eCP are not specially prepared CPs but Sea CPs in mid-transition
between partnerships — CPs that have recently completed a
superimposition event and are departing toward their next partner.
Cage reformation is the normal partner-switching dynamics of the Sea,
suddenly biased by the appearance of a strong SSV_net source.

**Consequence:** The cage is a persistent geometric relationship, not
a persistent collection of specific CPs. The four cage positions are
filled continuously by whatever transitioning +eCPs are locally
available; each is eventually replaced as it finds a stronger partner
elsewhere. The electron's identity is in the central −eCP; the cage
is the crowd that continuously reforms around it. The specific CPs
filling the cage positions are irrelevant to the electron's identity.

**Postulates used:** P1, P2, P3, P4; follows from C-CPP-1b

---

### P-CPP-8: Dual Stable Configurations of the Central −eCP

**Statement:** A −eCP has two energetically distinct configurations:

(A) DP enrollment: single partnership with one +eCP, binding energy
≈ SSV₀/2, contributing to the Dipole Sea as an ordinary DP.

(B) 4-vertex cage: tetrahedral cage with four +eCPs and four radial
chains, binding energy = 2 SSV₀ = m_e c², constituting the electron
as an SM particle with persistent identity.

Configuration B is the deeper energy minimum. Spontaneous transition
A→B occurs when three additional +eCPs are available at approximately
tetrahedral geometry around the −eCP. Transition B→A requires
simultaneous disruption of three cage bonds, making stable electrons
far more common than free Sea −eCPs at low temperature.

**Pair creation and annihilation:** Pair creation from a high-energy
photon is the correlated A→B transition of a −eCP and a +eCP,
promoted by the Lorentzian disruption of the photon's DP chain
(P-CPP-13). Pair annihilation is the correlated B→A transition
when a −eCP cage and a +eCP cage approach and dissolve into each other
(P-CPP-15).

**Status:** Proposition — thermodynamic argument; quantitative
transition rates from Sea statistics require further development.

---

### P-CPP-9: Atomic Orbital Probability Density as DP Chain Standing Waves

**Statement:** The probability density |ψ(x)|² of the electron in an
atomic orbital is the time-averaged distribution of the cage's central
position, produced by three simultaneous mechanisms:

(1) KE polarisation of the Dipole Sea by the moving −eCP, creating
a directed chain structure with spatial period equal to the de Broglie
wavelength (P-CPP-6).

(2) The structured SSV landscape from nucleus and other occupied
orbitals, biasing the central CP's random walk toward regions of
strong attractive SSV_net (high |ψ|²) and away from regions of
repulsive SSV_net (nodes, |ψ|² = 0).

(3) Self-reinforcing standing waves of DP chains in the SSV landscape:
chain reformation at each ZBW cycle reinforces the chain structure of
the previous cycle in regions where the background SSV landscape is
stationary, producing a standing wave whose nodes and antinodes
correspond to the nodes and antinodes of the Schrödinger wave function.

**Orbital shapes:** The geometric pattern of nodes and antinodes in
the CPP standing wave in the nuclear SSV landscape is the CPP account
of s, p, d, f orbital shapes — not a separate postulate but a
consequence of the SSV landscape geometry of the nucleus.

**Status:** Proposition — physically motivated; quantitative derivation
requires OP-QM-new-6 (derive SWE from DP chain standing wave conditions).

---

### P-CPP-10: Electron Identity Transfer and the Orbital Born Rule

**Statement:** The identity of which CP is "the electron" at any
given Absolute Moment may transfer through partner switching: a
transitioning Sea −eCP may be enrolled as the new cage centre while
the prior central −eCP departs as a Sea DP. The electron's position
is therefore not the trajectory of a single CP but the sequence of
Grid Points that successively occupy the central cage role.

**Born rule consequence:** The probability distribution of central
cage positions across many ZBW cycles is the Born rule probability
density |ψ|², shaped by the SSV landscape without being postulated
independently. This mechanism distinguishes CPP from both classical
mechanics (no probability) and standard QM (probability postulated
via the Born rule): in CPP, probability emerges from the statistics
of CP identity transfer in the SSV field.

**Relationship to P-CPP-9:** Identity transfer provides the mechanism
by which the central position hops through the standing wave pattern
of P-CPP-9. The standing waves define the stable regions; the identity
transfer populates them according to the SSV gradient.

**Status:** Proposition — physically motivated; formal connection to
the Born rule requires OP-QM-new-1.

---

### P-CPP-11: Virtual Particles as Transient CP Configurations
### Constrained by Gauss's Law

**Statement:** Virtual particles are transient configurations of the
Dipole Sea's partner-switching dynamics that momentarily reproduce the
charge and field structure of real SM particles, but lack a persistent
unpaired central CP as a nucleation seed.

**Gauss's law constraint:** The integral of the SSV field over any
closed surface in a charge-neutral volume is zero. Every VP
configuration must therefore have a compensating anti-configuration
within the enclosing volume. The recombination SSV_net linking the
VP pair is always present throughout the VP's lifetime, distinguishing
it from a real particle pair.

**Lifetime distribution:** Without a persistent nucleation seed,
thermal dissipation overwhelms cage maintenance at each ZBW cycle.
The mean VP lifetime is:
τ_VP = t_P / p_dissipate
where p_dissipate is the probability per ZBW cycle that partner-
switching disrupts the configuration. More energetic (more organised,
rarer) VP configurations have higher p_dissipate and shorter lifetimes.

**Connection to uncertainty principle:** The energy-time uncertainty
relation ΔE·Δt ≈ ℏ is the statistical expression of the relationship
between VP organisational complexity (energy) and mean lifetime —
derived from Sea statistics rather than postulated from Fourier analysis.

**Status:** Proposition — the Gauss's law constraint and lifetime
derivation are physically motivated; formal proof requires OP-QM-new-1.

---

### P-CPP-12: Critical Separation Distance for Real Pair Production

**Statement:** A produced +CP/−CP pair constitutes real particles
rather than a VP when their separation r exceeds the critical distance
r_crit at which the mutual SSV_net attraction is balanced by the
thermal pressure of the ZBW partner-switching Sea.

**Equilibrium condition:**
SSV₀/r_crit² = sea_strength × SSV₀/d_Sea²
r_crit = d_Sea / √sea_strength ≈ 2.37 × d_Sea

**Physical interpretation:** Below r_crit, recombination is
thermodynamically favoured — the intra-pair SSV_net dominates and
pulls the pair back together. Above r_crit, each CP independently
nucleates a cage — the thermal pressure of the Sea exceeds the
intra-pair SSV_net and the CPs find independent cage partners before
recombining.

**Predicted identification:** r_crit is the CPP candidate for the
electron Compton wavelength ℏ/m_e c. If correct, this provides a
derivation of the Compton wavelength from SSV₀ and sea_strength
alone (OP-QM-new-7).

**Status:** Proposition; quantitative verification requires OP-QM-new-7.

---

### P-CPP-13: Photon Pair Production via Lorentzian Asymmetry

**Statement:** Photon pair production near a heavy nucleus proceeds
in three stages:

(1) The nucleus's SSV field creates Lorentzian asymmetry (via PSR
compression) between the inner and outer limbs of the photon's DP
chain, disrupting the phase relationship that maintains the photon's
propagation. The inner limb is physically compressed relative to
the outer limb.

(2) At sufficient photon energy (hf ≥ 2m_e c²), this asymmetry
separates a +CP and −CP into independent displacement trajectories
with separation r > r_crit (P-CPP-12).

(3) Each CP nucleates a cage from local Sea CPs (P-CPP-7), forming
a real electron-positron pair. The nucleus absorbs recoil momentum
through the SSV gradient force on the photon chain's inner limb —
momentum conservation requires this third body. Excess photon energy
above 2m_e c² becomes KE of the produced pair, further stabilising
them against recombination via relativistic chain compaction (P-CPP-6).

**Why a nucleus is required:** In free space, no asymmetric Lorentzian
distortion is available to break the photon chain's left-right symmetry.
The nucleus provides the spatial SSV gradient that breaks this symmetry
and also absorbs the recoil momentum required by momentum conservation.
Pair production in free space from a single photon violates both
momentum conservation and the symmetry requirement — consistent
with QED selection rules.

**Status:** Proposition; quantitative cross-section calculation
requires OP-QM-new-7.

---

### P-CPP-14: Mass as Thermodynamic Nucleation-Dissipation Boundary
*(Definition-level proposition)*

**Statement:** The rest mass of a particle is the ground-state
organisational energy of its CP cage structure — the energy required
to maintain a stable nucleation seed against thermal dissipation of
its DP chains at T = 0 and v = 0.

**Corollaries:**

(a) Temperature dependence: At high T, more organisational energy is
required to maintain the same cage against stronger thermal dissipation.
At T = T_c (QCD transition temperature), the quark cage energy equals
the thermal dissipation energy — confinement dissolves (OP-SS-14).
At T ≈ 10¹⁵ K (electroweak scale), no cage structure can maintain
itself — all particle masses effectively vanish.

(b) Velocity dependence: At high v, SSV_abs compresses the chain
structure (Lorentzian compaction, P-CPP-6), storing additional energy
identified as relativistic mass. The relativistic mass formula
m_rel = γm₀ is the energy stored in a Lorentzian-compacted chain
structure relative to its rest-frame value.

(c) Ground-state energy: m_e c² = 0.511 MeV is the organisational
energy at the threshold of stability — the cage energy at r_crit —
where the nucleation SSV_net just exceeds the thermal dissipation
pressure at T = 0.

(d) SM-1 calibration: SSV₀ = 0.2555 MeV is the ground-state baseline
at T ≈ 0, v = 0, from which thermal and relativistic corrections depart.

(e) Second law: Entropy increase corresponds to the conversion of
organised DP chain structures (particles, photons) into the maximum-
entropy Sea. Mass is the most concentrated form of DP chain organisation;
photons are intermediate; Sea DPs are maximum entropy. All physical
processes convert between these levels with entropy non-decreasing.

**Status:** Definitional proposition — this reframes the existing
P6 (mass as organisational energy) in thermodynamic terms and extends
it with explicit temperature and velocity dependence.

---

### P-CPP-15: Pair Annihilation as Isentropic vs Non-Isentropic
### Cage Dissolution

**Statement:** Pair annihilation of a matter-antimatter particle pair
proceeds through mutual cage dissolution driven by inter-particle CP
attraction, producing two distinct regimes:

**(a) Isentropic (orderly) annihilation:** At low relative velocity
(v_approach < r_cage/t_P), cage dissolution is quasi-static. The
eight cage CPs from both particles (four from each) momentarily form
a symmetric structure around the central CP superimposition point,
with the approach axis as the sole preferred direction. Chain energy
dissipates along this axis as two back-to-back photons of energy
m c² each, conserving momentum and producing no entropy increase.
This is the CPP account of e⁺e⁻ → γγ and positronium decay.

**(b) Non-isentropic (disorderly) annihilation:** At high relative
velocity (v_approach > r_cage/t_P), cage dissolution is incomplete
and misaligned. Partial cage structures survive and recruit Sea CPs
to form new particle configurations. Chain energy dissipates in
multiple directions producing jets, broad photon spectra, and new
particle-antiparticle pairs above rest mass thresholds. Entropy
increases. Total energy is conserved but distributed across photonic,
massive, and thermal Sea degrees of freedom.

**(c) Three-photon outcome:** Ortho-positronium (spin-1) decay to
three photons arises when the cage dissolution geometry has three-fold
rather than two-fold axis symmetry, from specific spin alignment of
the electron-positron pair in the bound state. The 1000:1 ratio of
two-photon (para) to three-photon (ortho) annihilation is a testable
prediction of the cage dissolution geometry.

**(d) Isentropy condition:** Clean two-photon annihilation requires
collision duration > ZBW cycle time: v_approach × t_P < r_cage.
This is satisfied for positronium annihilation but violated for
ultra-relativistic collisions, consistent with observation.

**Note — distinction from tunneling dissolution:** In tunneling
(P-CPP-4), cage dissolution is isotropic (no photon). In annihilation,
cage dissolution is axially directed (two photons). The difference
is the presence vs absence of an approach axis: tunneling has a
displaced central CP but no approaching anti-partner; annihilation
has two approaching cages with a shared axis.

**Status:** Proposition; the 1000:1 ortho:para ratio is a quantitative
testable prediction requiring computation of the cage dissolution
geometry for spin-0 vs spin-1 positronium.

---

## Section 3: New Open Problems

### OP-QM-new-1: Planck's Constant from ZBW Partner-Switching Statistics

**Priority:** HIGHEST
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Derive ℏ from CPP partner-switching random walk
dynamics. Specifically: identify the combination of SSV₀, l_P, t_P,
and sea_strength that equals ℏ, and demonstrate that the random walk
amplitude over one ZBW period equals the reduced Compton wavelength
λ_C = ℏ/mc for the electron.

**Context:** P-CPP-1 identifies the central CP random walk as the
CPP account of quantum position uncertainty. For this identification
to be quantitative, the RMS displacement per ZBW cycle must equal
the Compton wavelength at the relevant mass scale. The Compton
wavelength of the electron is λ_C ≈ 2.43 × 10⁻¹² m, requiring
approximately N ≈ (λ_C/l_P)² ≈ 10⁴⁶ ZBW steps to traverse that
distance in a random walk.

**Feeds into:** OP-QM-1 (Born rule), OP-QM-2 (Schrödinger equation),
P-CPP-1, P-CPP-10

---

### OP-QM-new-2: Stochastic Variation of ZBW Period from Bulk Sea Fluctuations

**Priority:** MEDIUM
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Compute the variance in the ZBW period as a function
of the number density and mean orientation coherence length of
surrounding Dipole Sea pairs. Determine whether this variance connects
to the quantum mechanical uncertainty in particle position or to
finite-temperature mass corrections.

**Context:** At each ZBW turning point (superimposition), the bulk
SSV_net that drives A and B apart is stochastic — it includes
contributions from all nearby Sea CPs with randomised orientations.
The restoring force for the next oscillation cycle therefore has a
distribution of magnitudes, producing a distribution of ZBW periods
rather than a single sharp frequency. This ZBW frequency variance
is expected to produce: (a) a natural linewidth in the ZBW frequency
spectrum (Lorentzian broadening); (b) spatial diffusion of the DP
pair centre over many cycles; (c) temperature-dependent mass corrections
via increased thermal variance at high T.

**Expected magnitude:** The variance is small — the intra-pair SSV
dominates over bulk fluctuations at near-superimposition distances
by ∝ (l_P/d_bulk)². The approximation f_ZBW ≈ 1/(2t_P) is highly
accurate, but the correction is not exactly zero.

---

### OP-QM-new-3: Biased vs Unbiased Tunneling Rates from CPP

**Priority:** HIGH
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Derive the tunneling current as a function of barrier
width, barrier height, and (for biased case) applied field SSV_net,
from the rogue-wave SSV_net spike statistics of the Dipole Sea.
Verify agreement with Fowler-Nordheim (biased) and WKB (unbiased)
tunneling formulae.

**Two cases:**

Biased (transistor): External SSV_net gradient biases the stochastic
partner-switching in the transmission direction. Compute the net
rate of central CP displacements across the barrier as a function
of bias field magnitude.

Unbiased (diffusion tunneling): No external field. Compute the
probability that a rogue-wave SSV_net spike at the central CP's
near-side location exceeds the barrier height, as a function of
barrier width and height. Expected result: P ∝ exp(−V_b/Nμ²),
reproducing WKB exponential.

---

### OP-QM-new-4: Derive r_chain from SSV₀ and sea_strength

**Priority:** HIGH
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Compute the equilibrium length of the radial DP chains
from the balance of radial tension, inter-chain repulsion, and thermal
dissolution. Verify that the result equals the classical electron
radius r_e ≈ 2.82 × 10⁻¹⁵ m. Compute the ratio r_e/r_conf from
the leptonic and hadronic coupling strengths and verify against the
observed ratio of ~18.

**Feeds into:** P-CPP-5, OP-QM-new-5

---

### OP-QM-new-5: Chain Contribution to Electron Rest Mass

**Priority:** HIGH
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Compute the total organisational energy stored in the
four radial DP chains at equilibrium length r_chain. Determine what
fraction of the electron's 0.511 MeV rest mass comes from (a) the
tetrahedral cage binding energy (2 SSV₀ from SM-1's calibration) and
(b) the radial chain organisational energy. If the chain contribution
is non-negligible, the SM-1 calibration requires revision: SSV₀ must
be set by the total (cage + chain) binding energy, not cage alone.

**Note:** This is the most consequential near-term open problem for
SM-1's internal consistency. If the chain energy is significant, the
current calibration SSV₀ = 0.2555 MeV overcounts the cage contribution
to the electron mass, and must be partitioned between cage and chain.

---

### OP-QM-new-6: Derive Schrödinger Equation from DP Chain Standing
### Wave Stability Conditions

**Priority:** HIGH
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Derive the stability condition for DP chain standing
waves in a nuclear SSV landscape and show that this condition reduces
to the time-independent Schrödinger equation Ĥψ = Eψ for the
appropriate identification of the Hamiltonian with the SSV landscape
energy function.

**Context:** P-CPP-9 identifies atomic orbital shapes with DP chain
standing wave patterns in the nuclear SSV landscape. The standing
waves are stable when the background SSV landscape is stationary and
chain reformation at each ZBW cycle reinforces the previous cycle's
structure. The formal stability condition for this self-reinforcing
wave process should produce eigenvalue equations whose eigenfunctions
are the atomic orbitals — i.e., the Schrödinger equation.

**Connection to Nelson/Fenyes:** Stochastic mechanics (Nelson 1966,
Fenyes 1952) showed mathematically that quantum mechanics is equivalent
to a stochastic diffusion process. CPP provides the physical mechanism
for this diffusion: ZBW partner switching in the SSV landscape.
The derivation of the SWE from CPP chain standing waves would be
the CPP realisation of the Nelson/Fenyes programme with explicit
physical grounding.

---

### OP-QM-new-7: Derive r_crit and Pair Production Threshold from
### CPP Primitives

**Priority:** HIGH
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Compute the critical separation distance r_crit from
SSV₀, sea_strength, and the Sea's mean CP density. Verify that:
(a) the energy required to separate a +CP/−CP pair to r_crit equals
m_e c²; (b) r_crit equals the electron Compton wavelength ℏ/m_e c;
(c) the nuclear SSV gradient required to produce asymmetric disruption
of a photon chain is consistent with the observed pair production
cross-section near heavy nuclei.

**Feeds into:** P-CPP-12, P-CPP-13, P-CPP-14

---

### OP-QM-new-8: Temperature Dependence of Rest Mass from CPP

**Priority:** MEDIUM
**Status:** OPEN
**Registered:** 30 March 2026

**Statement:** Derive the temperature correction to particle rest mass
from the increased thermal dissipation pressure on DP chains at
temperature T. Verify that the correction: (a) vanishes at T = 0
(recovering SM-1's calibration); (b) produces confinement dissolution
at T = T_c ≈ 150 MeV (feeding into OP-SS-14); (c) is consistent with
electroweak symmetry restoration at T ≈ 10¹⁵ K.

**Feeds into:** OP-SS-14, P-CPP-14

---

## Section 4: Postulate Demotion — P5

The existing CPP core postulate P5 states:

> **P5 (ZBW oscillations):** Dipole pairs oscillate at
> f_ZBW ≈ 1/(2t_Pl). One full cycle = attraction phase + repulsion
> phase over two Planck times. This oscillation is the source of spin
> and contributes to mass.

Based on T-CPP-1 and C-CPP-1a, P5 is no longer needed as an axiom.
The ZBW oscillation frequency is a derivable consequence of P4 (SSV
force law) and P2 (lattice discreteness): opposite-polarity CPs
attract monotonically until superimposition, at which point intra-pair
SSV direction vanishes and bulk SSV drives separation. The period of
this oscillation is 2 Absolute Moments, giving f_ZBW = 1/(2t_P)
as a theorem, not a postulate.

**Recommended change to postulates_and_theorems.md:**

Replace P5 with:
> **P5 (ZBW oscillations) [DEMOTED — now T-CPP-1 + C-CPP-1a]:**
> The ZBW oscillation of bound DP pairs is a derived consequence of
> the SSV force law (P4) on a discrete lattice (P2): opposite-polarity
> CPs approach under monotonically increasing SSV_net attraction to
> superimposition; at superimposition, intra-pair SSV direction
> vanishes; bulk SSV drives opposite displacements on the next Absolute
> Moment. Period ≈ 2t_P, giving f_ZBW ≈ 1/(2t_P) as a theorem.
> See T-CPP-1 and C-CPP-1a.

**If P5 is removed:** The CPP postulate count decreases from 7 to 6.
The minimum postulate target noted in the existing registry (P3–P6
potentially derivable) is now partially achieved: P5 is derived.

---

## Section 5: SSV_net vs SSV_abs — Glossary Entries Required

These two quantities were used throughout the existing CPP literature
without formal distinction. The partner-switching session revealed
that they are physically independent and must be separately defined
in glossary-SM-1.md, glossary-SS-1.md, and eventually a CPP
master glossary.

**SSV_net (directional SSV field):**
The vector sum of SSV contributions at a Grid Point from all CPs
within their PSR. SSV_net has both magnitude and direction.
It governs the direction of each CP's next displacement — a CP moves
to the adjacent Grid Point with the highest SSV_net gradient.
SSV_net is what causes ZBW oscillation to reverse: when A(−) rebounds
from B(+), it is because SSV_net at the superimposition Grid Point
(now from the bulk, not from B) points away from B.
*SSV_net is zero at the cage centre by T_d symmetry — this is the
force-free pocket of P-CPP-3.*

**SSV_abs (scalar SSV field magnitude):**
The scalar magnitude of the total SSV field at a Grid Point —
|SSV_net| from all sources including any isotropic contributions.
SSV_abs is not a direction; it is a local energy density / intensity.
High SSV_abs means the Dipole Sea is strongly stressed at that location.
Via the PSR compression formula:
PSR_eff = l_P / (1 + k · SSV_abs)
SSV_abs governs the local metric — it determines how much physical
distance each lattice step corresponds to. This is the GR/Lorentzian
effect: SSV_abs compresses space.

**Critical distinction:** At Grid Point superimposition of an
opposite-polarity pair, SSV_abs is near its maximum (the intra-pair
field is at greatest strength) while SSV_net from the intra-pair
interaction is exactly zero (direction undefined). This is the
clearest demonstration that SSV_abs and SSV_net are independent
quantities — one can be maximised while the other vanishes.

**Summary:**
- SSV_net → determines CP displacement direction → governs dynamics
- SSV_abs → determines PSR compression → governs metric (GR effects)
- SR-1 is primarily an SSV_abs story (PSR compression = Lorentz contraction)
- SM-1 is primarily an SSV_net story (force law = cage stability)
- Both operate simultaneously in all physical processes

---

## Section 6: Provenance Notes

All items in this document emerged from a single conversation session
(29–30 March 2026) beginning with the SM-1 mechanism essay discussion
of the ZBW oscillation turning point. The logical chain was:

1. ZBW turning point question → T-CPP-1 (CP exclusion is a theorem)
2. T-CPP-1 → C-CPP-1a (turning point at superimposition)
3. C-CPP-1a + C-CPP-1b → stochastic partner exchange
4. Partner exchange → P-CPP-1 (random walk, uncertainty)
5. Partner exchange → P-CPP-2 (rogue wave tunneling)
6. SM-1 cage stability question → P-CPP-3 (tetrahedron uniqueness)
7. Tunneling + P-CPP-3 → P-CPP-4 (elastic tunneling)
8. Chain structure question → P-CPP-5, P-CPP-6
9. Cage reformation question → P-CPP-7, P-CPP-8
10. Orbital probability question → P-CPP-9, P-CPP-10
11. VP question + Gauss's law → P-CPP-11, P-CPP-12
12. Pair production question → P-CPP-13
13. Mass definition synthesis → P-CPP-14
14. Pair annihilation question → P-CPP-15

All items originated with Thomas Lee Abshier ND's physical intuitions
and were formalised collaboratively with Claude Sonnet (Anthropic).
