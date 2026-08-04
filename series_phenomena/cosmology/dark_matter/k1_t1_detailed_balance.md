# K1-MEMORY W-1 — THEOREM T-1: DETAILED BALANCE AT CONSTANT VELOCITY (NEWTON 1 AT MECHANISM LEVEL)

**Patch 2964 (3 Aug 2026). Executes W-1 of the K1-MEMORY derivation
charter (`k1_memory_derivation_charter.md`, Patch 2961): statement
and proof of T-1 at mechanism level, with toy verify script
`code/2964_t1_ledger_toy.py` (12/12 PASS). Status: T-1
ESTABLISHED-AT-MECHANISM-LEVEL, PANEL-PENDING per charter §3
(conservative outcome → combined completed-package review). No
value of any open quantity is minted; toy units only.**

**CHANGELOG — v1.2 (Patch 2980): CONV-012 Q2 wording strengthening — per-step reciprocity stated as an exact event-level property of the registered update (Copilot adoption, 2979). No content change.**

**CHANGELOG — v1.1 (Patch 2975, 3 Aug 2026): CONV-011 condition C-2
executed (adjudication 2971 §2 Q1; Copilot addendum 2974). Adds
§R1 the explicit conditional-on-A2 statement; §R2 Lemma T-1.L (the
DISCRETE traversal telescoping — exact at every finite Moment step,
every initial phase, every commensurability, via the DP-book ledger
route) with the pairing/bijection corollary; §R3 the A3 import
citation sharpened to microscopic reciprocity only. New sweep
verify `code/2975_t1_discrete_sweep.py` (Copilot's exhaustive
phase-sweep requirement + negative control). Theorem CONTENT
unchanged; the proof obligations the panel named are discharged
explicitly. Grade remains ESTABLISHED-AT-MECHANISM-LEVEL per the
panel; operator-grade use stays gated on C-1/B-1 review.**

**Assumptions cited (charter duty, every result):**
- **PROTOCOL-D1** (2960, reopenable working default): Version B
  band arrival. Load-bearing use: guarantees every GP in the
  pattern volume is touched by the relay every Moment, so the
  co-moving pattern's SSV is refreshed and the anchored arc
  configuration can be re-sustained each Moment (the stationarity
  premise A2 below).
- **PRINCIPLE-R1** (2961, **RATIFIED** 2963, reopenable): sampling
  not consumption. Load-bearing use: the relay tier transports no
  energy (non-destructive conserved read), so the DP-polarization
  response account is the ONLY energy account in the coasting
  ledger; closing it closes the theorem. Without R1, a
  transit-imprint deposition would add an unbalanced drag term
  linear in path length, and T-1 would fail.

**Admissible inputs used:** the 2956 verbatim arc mechanism; V-2 GP
protocol (2958); SF-6 curl linkage (B = rotational displacement
component of the same dipole displacement whose radial component is
E); banked FACT G1 (I_h-equivariance → exact isotropy through
spherical-harmonic degree 5, first lattice anisotropy at degree 6).
**Bars honored:** no α1-chain descendants, no AUTOMATON occupancy
values, no tuned constants, no QM-1 lineage (TODO-2957-B open).
**Orientation convention (2956 §2 reservation, now fixed at first
use):** arc rotation sense is defined with respect to the velocity
axis v̂ by the right-hand rule as viewed from the fore side looking
aft; the founder's "counterclockwise" is this sense for the
positive-pole outer arc. Nothing below depends on the choice —
fore/aft congruence is sense-blind — so the convention is fixed for
descriptive definiteness only.

---

## §1 — SETUP AND DEFINITIONS

**D1 (Pattern).** A bound charge pattern S moves at constant
velocity v through the homogeneous DP Sea. Per 2956, S carries a
co-moving arc configuration: Sea DPs polarized into inner/outer
arcs about the velocity axis, distributed 360° azimuthally and fore
to aft, charging in the fore volume and discharging in the aft.

**D2 (Steady state).** In co-moving coordinates x′ = x − vt, the
arc polarization field p(x′) and its stored energy density
u(x′) ≥ 0 (energy of displaced-CP configuration against restoring
structure; u vanishes outside the pattern's support and far from S)
are time-independent. That such a co-moving steady state exists and
is re-sustained each Moment is the anchoring premise **A2**,
grounded in 2956 §2.3 (anchored patterns do not cancel because the
source re-sustains them each Moment) and PROTOCOL-D1 (every GP in
the volume refreshed per Moment). T-1 characterizes this state; it
does not derive its existence (that is T-2's establishment
problem).

**D3 (Moment stepping and slab throughput).** Per Moment τ_M the
pattern advances one increment δ = v·τ_M. Equivalently, in the
pattern frame, a slab of Sea material of width δ enters the fore
boundary and a congruent slab exits the aft boundary — the 2956
slab-throughput picture.

**D4 (Ledger accounts).** Per-Moment: E_in = energy invested
charging Sea DPs whose u increased; E_out = energy recovered from
Sea DPs whose u decreased; J = net momentum exchanged between S and
the Sea; U = total stored arc energy Σ u.

**D5 (Exchange symmetry, premise A3).** The influence between S
and a Sea DP is mediated by the same sampled-SSV / DP-displacement
channel in both directions (the SF-6 shipped structure): per-Moment
displacement influence is pairwise equal and opposite. This is the
substrate form of action–reaction already load-bearing in SF-6 and
is used here as an admissible imported premise, not re-derived.

## §2 — THEOREM T-1 (statement)

Under A2 (steady co-moving pattern), A3 (exchange symmetry),
PROTOCOL-D1, and PRINCIPLE-R1, for a bound charge pattern at
constant velocity v:

**(i) Energy detailed balance.** Per Moment, E_in = E_out exactly:
the fore-volume arc-charging cost is paid in full by the aft-volume
arc-discharging return. Equivalently U is constant.

**(ii) Momentum closure.** Per Moment, the net momentum exchanged
with the Sea is zero: transverse components cancel by azimuthal
symmetry; the longitudinal charging recoil (backward push) is
exactly cancelled by the discharging advance (forward push). The
SSV_net differential sustains exactly one displacement increment δ
per Moment — motion is re-caused each Moment at zero net cost.

**(iii) Newton 1 at mechanism level.** Consequently constant v with
its co-moving pattern is a conservative fixed point of the
mechanism: zero net energy drawn, zero net momentum leaked, no
wake; coasting persists indefinitely. Inertia enters only when v
changes (T-2).

## §3 — PROOF

**Lemma L1 (per-DP cycle lemma).** Fix a Sea DP at lab position
x₀. As the steady pattern sweeps past, the DP traverses the
polarization history p(x₀ − vt): unpolarized (far fore) → full
charging profile → discharging profile → unpolarized (far aft).
Initial and final configurations are identical (unpolarized rest),
so the net energy exchanged between S and that DP over the complete
traversal is u_final − u_initial = 0. The impulse delivered to the
DP telescopes the same way: the work–displacement bookkeeping over
the traversal is a total difference of the stored configuration,
which vanishes. By A3, the equal-and-opposite tally on S over the
same traversal is also zero. ∎(L1)

**Lemma L2 (steady-population lemma).** Parameterize the cycle by
phase φ (position within the pattern along v̂, at fixed transverse
offset). At steady state the Sea-DP population density at each φ is
time-independent: per Moment, the material entering phase φ (slab
width δ, cross-sectional density uniform by Sea homogeneity) equals
the material leaving it — throughput is uniform along the cycle.
Hence any per-Moment total over the pattern equals throughput ×
(the per-DP full-cycle integrand summed over phase). ∎(L2)

**Proof of (i).** Two independent routes, which agree:

*Route A (translation congruence).* U_n = Σ_sites u(x − nδ). Over a
homogeneous Sea, the sum is invariant under translation of its
argument, so U_{n+1} = U_n. Energy conservation at the response
tier — which is the WHOLE energy ledger, because R1 (RATIFIED)
makes the relay tier a non-destructive read that transports no
energy — gives E_source,n + E_out − E_in = E_source,n+1. The bound
pattern's internal energy is stationary (D1), and ΔU = 0, so
E_in = E_out exactly.

*Route B (cycle × population).* By L2 the per-Moment net energy
exchange equals throughput × (per-DP full-cycle net exchange),
which is zero by L1. So E_in − E_out = 0.

Route A closes the books globally; Route B locates WHERE they
close: every Sea DP individually returns to its initial state, so
the balance is detailed (per cycle), not merely aggregate — hence
the theorem's name. This also reconciles the 2956 phrasing: the
COUNT asymmetry ("more arcs in the back discharging than in the
front charging") is a phase-population statement about where the
throughput slab sits in the cycle; the balanced quantity is the
cycle integral, and the count asymmetry is exactly what makes the
instantaneous fore and aft sub-ledgers sum to the same magnitude
with opposite sign. ∎(i)

**Proof of (ii).** Transverse: the arc configuration is distributed
360° about v̂ (2956); by azimuthal symmetry (exact through degree 5
per FACT G1; see §4 for the degree-6 caveat) transverse exchanges
cancel identically. Longitudinal: by L1 the full-cycle impulse on
each Sea DP is zero, and by L2 the per-Moment total longitudinal
exchange is throughput × 0 = 0. The charging recoil and discharge
advance are the two halves of that zero. What remains per Moment is
not a force imbalance but the SSV_net displacement instruction:
under the substrate's re-caused motion (displacement must be
produced each Moment), the fore/aft differential produces exactly
the increment δ that reproduces the same steady state one step
advanced — with zero net momentum flux into the Sea (no wake: the
Sea behind S is fully returned to unpolarized rest by L1). ∎(ii)

**Proof of (iii).** By (i) no net energy is drawn per Moment; by
(ii) no net momentum is exchanged and the produced increment is
again δ; therefore the configuration at Moment n+1 is the Moment-n
configuration translated by δ — the same steady state. Constant v
is a fixed point, sustained at zero cost, indefinitely. This is
Newton 1 stated and proved inside the mechanism. ∎(iii)

## §4 — DISCRETENESS DISCLOSURE (lattice caveat, FACT G1)

The proof's translation invariance is exact in the coarse-grained
/ continuum reading of the arc content. On the literal GP lattice:
(a) for a smooth (smoothly decaying) arc profile, the discrete sum
Σ u(x_i − s) is translation-invariant to aliasing accuracy —
super-polynomially small in lattice spacing (Poisson summation) —
verified at machine precision in the toy for commensurate AND
incommensurate stepping (checks C1, C3, C6); (b) for profiles with
sharp support edges, per-Moment residuals appear at the edge scale
and shrink with resolution, balancing on time-average (first-run
toy behavior, disclosed in reasoning/2964.md); (c) angular
corrections to the transverse cancellation enter first at
spherical-harmonic degree 6 (FACT G1) — the same single lattice
fingerprint as everywhere in this arc. None of these caveats opens
a net drain: they bound fluctuation, not dissipation, and the
per-DP cycle lemma is exact regardless of stepping.

## §5 — VERIFY SCRIPT

`code/2964_t1_ledger_toy.py` — ledger-arithmetic toy (scope
disclosed in-file: verifies the congruence/cycle arguments, not a
substrate simulation). 12/12 PASS: per-Moment E_in = E_out at
machine precision (commensurate, both profile classes; C1);
stored U constant (C1b); net force ≈ 0 at steady state (C2);
incommensurate residuals at machine epsilon for smooth profiles
with time-mean ~1e-19 (C3/C3b); per-DP full-cycle net energy and
impulse exactly zero (C4/C4b); acceleration contrast ΔU > 0 —
establishment cost exists, T-2 preview only, not a T-2 result
(C5); balance across velocities v = 1,2,5,11 grid units at machine
precision (C6). Toy units only.

## §6 — WHAT T-1 DOES AND DOES NOT ESTABLISH

Established: the coasting ledger closes exactly, with the balance
detailed at the per-DP cycle level; the mechanism's Newton 1 is a
theorem, not an input. Not established here: existence/uniqueness
of the steady co-moving state (premise A2 — T-2's establishment
problem); the magnitude of the establishment cost (T-2, the
mass-energy link); the bound-state ring instance and the K1
stiffness (T-3, the 7th derivation). The falsifier branch frozen at
charter §3 (T-1 failure = ledger does not balance) is NOT taken:
outcome is conservative-class.

## §7 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL (= OPEN-K1-MEMORY-1); B7
holds DM-1/DM-3 banners; Candidate (B) 79.5%; 2855 PROVISIONAL;
d_DP ceiling ACTIVE. T-1 status: ESTABLISHED-AT-MECHANISM-LEVEL,
PANEL-PENDING (combined completed-package review with W-2/W-3 per
charter §3). W-2 (T-2, inertia as establishment cost) is next in
the frozen order.


---

## §R1 (v1.1, C-2(a)) — The conditional statement, stated

T-1 is, and always was, a CONDITIONAL theorem until Lemma M1 is
invoked: *Assume the translated bound steady state exists (premise
A2); then the fore-charging cost and aft-discharging return balance
exactly, per DP, per traversal, in energy and in impulse.* Premise
A2 is discharged — non-circularly — by T-2's Lemma M1 (the anchored
configuration is the fixed point of the D-1 per-Moment refresh; M1
makes no use of T-1). The dependency order is M1 → T-1 → (T-2's
p = Mv identification), a DAG with no cycle. Until M1 is cited,
every T-1 consequence carries the A2 condition explicitly. This
section makes the panel-accepted reading (GPT Q1; 2971 C-2(a)) the
letter of the theorem.

## §R2 (v1.1, C-2(b)) — Lemma T-1.L: the discrete traversal telescoping (exact)

**Setting.** Under the registered Moment-stepped update, a Sea DP's
interaction with the passing pattern is a finite state sequence
s_0 → s_1 → … → s_K in the DP's own state space, where s_0 is
unpolarized rest and — by the M1/Version-B structure (anchored
content is the pattern's, not the DP's; unanchored content departs
at c with no return) — the traversal CLOSES: s_K = s_0. At each
step the interaction is a PAIR exchange: the impulse delivered to
the composite at step k is the negative of the DP's momentum change
at step k (microscopic reciprocity, §R3), and likewise for energy.

**Lemma T-1.L.** For every Sea DP, every initial phase φ, every
velocity v (commensurate with the Moment lattice or not), and every
finite Moment step Δt:

  Σ_{k=0}^{K−1} Δp_k^{→comp} = −[p_DP(s_K) − p_DP(s_0)] = 0
  Σ_{k=0}^{K−1} ΔE_k^{→comp} = −[E_DP(s_K) − E_DP(s_0)] = 0

both EXACTLY — no continuum limit is taken anywhere.

**Proof.** The per-step exchanges telescope against the DP's own
books: summing the reciprocity identity over the traversal, the
right side is a pure difference of the DP's state functions at the
endpoints, and closure (s_K = s_0) annihilates it. Phase φ and
commensurability enter only through WHICH sequence {s_k} is
traversed and how many steps K it takes; they never touch the two
ingredients of the proof (per-step reciprocity; endpoint closure).
Boundary/spin-up transients (Copilot Q1) are outside the theorem by
the §R1 conditional: the establishment transient is T-2's ledger
(W = ΔE + E_rad), not T-1's, and the steady-state premise excludes
it by construction. ∎

**Corollary (the pairing/bijection, GPT's formulation).** Closure
plus reciprocity implies the fore/aft pairing exists: the involution
on traversal steps induced by the DP's return path pairs each
charging exchange with a discharging counterpart of opposite sign.
The ledger proof above SUBSUMES the bijection — the theorem does
not need the pairing exhibited, because endpoint closure is
strictly stronger — but the corollary records that the discrete
update operator preserves exactly the one-to-one structure the
telescoping argument was accused of assuming.

**What the lemma does and does not claim.** It upgrades the
telescoping argument from continuum-sweep-plus-toy-numerics to an
exact finite-step identity, discharging C-2(b) as stated by the
panel (GPT's "decisive missing item" and DeepSeek's "decisive
computation" — the same object). It does NOT claim engine-grade
verification of closure itself: closure is inherited from M1 at
M1's grade (mechanism level; its instrument-grade test is the W-4
ensemble via the B-1 bridge's L-4 leg). The condition is inherited,
not laundered.

**Wording strengthening (v1.2, Patch 2980, CONV-012 Q2 adoption).** "Per-step
reciprocity" in this lemma is an EXACT event-level property of the registered
update rule — each Perceive-stage exchange is a pairwise transfer in which the
impulse (energy) credited to the composite's book at step k equals the negative
of the DP's momentum (energy) change at step k, by the event's own bookkeeping —
NOT an assumption layered on top of the update. The SF-6 mutual-messaging
citation of §R3 is the provenance of this event-level structure.

**Sweep verification.** `code/2975_t1_discrete_sweep.py` (18/18):
random initial phases × incommensurate velocities × step counts,
per-DP impulse and energy sums at machine zero; plus a NEGATIVE
CONTROL — an update with closure deliberately broken produces a
nonzero residual, demonstrating the sweep can fail and is therefore
a test, not a tautology.

## §R3 (v1.1, C-2(c)) — The A3 import, cited exactly

What T-1 imports from SF-6 is MICROSCOPIC RECIPROCITY OF PAIR
EXCHANGES: each Perceive-stage message between the pattern's
anchored content and a Sea DP is mutual — the curl-linkage messaging
of the SF-6 stencil — so each interaction event's impulse/energy
books balance pairwise at the event. This is a statement about the
stencil's mutual messaging, NOT composite-level action–reaction:
Newton 3 for composites is downstream OUTPUT of the package (via
T-1/T-2/B-1), never input. The panel-accepted scope (GPT: "only
microscopic translation symmetry/reciprocity"; Grok: "mutual
messaging, not action-reaction pairs of forces") is hereby the
letter of the import.
