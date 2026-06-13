# Glossary — SR-2: The Spin-Bit Axiom

Key terms for SR-2, in dependency order where possible. Programme-wide terms are in
`../../../master_glossary.md`; this file covers the spin-2 / `op:einstein` arc specifics.

**Spin bit.** The informal name for the new degree of freedom added by axiom A3′: a single
symmetric-traceless rank-2 field Q_ij carried in the Grid-Point broadcast. "Bit" by analogy to the
DI-bit and the LSP — successive rungs of the broadcast ladder.

**Lattice State Packet (LSP).** The data each Grid Point broadcasts to its Planck-Shell-Radius
neighbours each Absolute Moment. Pre-A3′: scalar |SSV|_abs + vector SSV_net (4 components).

**LSP′ (completed broadcast).** The LSP after A3′: (x_GP, t_abs; Φ, V_i, Q_ij), with dynamical
content Φ (scalar) ⊕ V_i (vector) ⊕ Q_ij (tensor) = A ⊕ T₁ ⊕ H = 1 + 3 + 5 = 9 components.

**Q_ij.** The symmetric-traceless (Q_ij = Q_ji, Q_kk = 0) rank-2 broadcast field; five components;
the radiative tensor sector. Maps to the TT metric perturbation h^TT_ij.

**Φ ≡ |SSV|_abs.** The scalar broadcast channel (irrep A, l=0); sources g_tt / the Newtonian
potential / gravitational time dilation.

**V_i ≡ SSV_net.** The vector broadcast channel (irrep T₁, l=1); sources g_ij statics and
gravitomagnetism.

**Helicity.** The eigenvalue under rotation about the propagation axis. Scalar → 0; vector → 0, ±1;
the GW + and × polarizations → ±2. The "helicity-±2 gap" is the absence of a ±2 channel in a
scalar+vector packet.

**Irreps A, T₁, H.** The icosahedral rotation group's representations of dimensions 1, 3, 5; the
intact descents of the SO(3) multiplets l = 0, 1, 2. The H ("H_g") irrep is the geometric seat of
Q_ij.

**Completion Theorem (THEO-SR-EIN-1).** The statement that l = {0,1,2} are the only SO(3) multiplets
descending intact to the icosahedral group; l ≥ 3 (2l+1 ≥ 7 > 5) split permanently. Hence LSP′ = 9
is the lattice's full protected content — no fourth rung.

**Shell-sum.** The icosahedral 12-edge neighbour sum the Compute step applies to broadcast
components; in the continuum it becomes ∝ ∇² (from Σ v̂_i v̂_j = 4·𝟙). It is *rank-agnostic*: it acts
component-wise and so propagates a scalar, vector, or tensor identically, at c.

**Spherical 5-design.** A property of the 12-vertex icosahedral shell: moments up to degree 5
match the sphere's. Consequences used here: Σ v̂ = 0 (annihilates the absolute-|SSV| monopole) and
l=2 ⊥ l=0,1 on the shell.

**Eardley class N₂.** The classification of a metric theory's radiative content; N₂ = the two
tensor (helicity-±2) modes only, as in GR. SR-2's response is N₂ (THEO-SR-EIN-3).

**Trace completion (τ).** The spatial trace τ = h̄_kk the packet does *not* carry. It is redundant —
fixed locally by the channels the packet does carry: ∇τ = 3(∂_t h̄_{0i} − ∂_j Q_ji); τ_static = 0.
Not a tenth channel; zero new degrees of freedom.

**Operational-Energy Lemma (THEO-SR-EIN-4).** Because C5 is the only field↔matter coupling and the
channels are generated (retarded functionals of matter), there is no independently operational
energy channel; emission = work by the assembled retarded metric (= Einstein quadrupole luminosity),
absorption = TT-only. The microscopic energy functional is a declared refinement, not a debt.

**op:einstein.** The programme open problem: does c08's field operator assemble into the full
Einstein tensor? (a) = the radiative tensor sector (closed here); (b) = excess-vs-absolute sourcing /
inert uniform Sea (conditionally closed). Tracked as OPEN-SR-4 in the frontier.

**PCD cycle.** Perceive–Compute–Displace: the per-Moment GP operation. Q_ij participates identically
to Φ and V_i — perceived from neighbour packets, shell-summed at Compute, re-broadcast.

**Absolute (Nexus) frame.** The substrate's preferred frame, in which packet components are stated;
the reason the broadcast connection is flat (the third assault's conclusion).
