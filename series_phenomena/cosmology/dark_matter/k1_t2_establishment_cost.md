# K1-MEMORY W-2 — THEOREM T-2: INERTIA AS ESTABLISHMENT COST (THE MASS–ENERGY LINK AT MECHANISM LEVEL)

**Patch 2965 (3 Aug 2026). Executes W-2 of the K1-MEMORY derivation
charter (`k1_memory_derivation_charter.md`, Patch 2961): statement
and proof of T-2 at mechanism level, with dynamical verify script
`code/2965_t2_establishment_toy.py` (12/12 PASS). Also discharges
the A2 debt flagged at T-1 (existence/attraction of the co-moving
steady state, established at mechanism level with toy-grade
dynamical demonstration). Status: T-2
ESTABLISHED-AT-MECHANISM-LEVEL, PANEL-PENDING per charter §3
(combined completed-package review with T-1/T-3). No value of any
open quantity is minted; toy units only; all toy coefficients
disclosed as toy-specific.**

**CHANGELOG — v1.1 (Patch 2976, 3 Aug 2026): CONV-011 conditions
C-3 + C-4 executed (adjudication 2971 §2 Q2; Copilot addendum
2974). Adds §R1 Lemma T-2.P (the orientation-sense
energy-degeneracy lemma — the compressed parity step made explicit:
inversion is INSIDE the equivariance group, so the sense reversal
is covered by invariance, not ignored); §R2 the dE = v·dp
grounding with the route DECLARED (definitional-with-consistency)
and the dependency DAG stated; §R3 the M-vs-anchored-content sweep
(Copilot's item). New verify `code/2976_t2_parity_sweep.py`.
Theorem CONTENT unchanged; grade remains
ESTABLISHED-AT-MECHANISM-LEVEL per the panel.**

**Assumptions cited (charter duty, every result):**
- **PROTOCOL-D1** (2960, reopenable working default): per-Moment
  band refresh of every GP in the pattern volume. Load-bearing
  use: the anchoring update that makes the co-moving steady state
  the fixed point of the per-Moment map (Lemma M1).
- **PRINCIPLE-R1** (2961, **RATIFIED** 2963, reopenable): sampling
  not consumption. Load-bearing use: the relay tier transports no
  energy, so the response-tier account is the entire ledger; the
  cost theorem's books (work in = stored + radiated) have no third
  account to leak into.

**Admissible inputs used:** the 2956 verbatim arc mechanism
("Inertia = the stiffness of ESTABLISHING or CHANGING this
co-moving pattern; coasting = its conservative steady state" —
T-2 formalizes exactly this sentence); T-1 (Patch 2964,
PANEL-PENDING, cited as arc-internal); V-2 GP protocol; SF-6 curl
linkage (a moving charge's displacement field acquires a curl
component proportional to v — the shipped B-from-motion
identification); FACT G1 (isotropy through degree 5). **Bars
honored:** no α1-chain descendants, no AUTOMATON occupancy values,
no tuned constants, no QM-1 lineage (TODO-2957-B open).
**Consistency scope:** T-2 is derived inside the K1 arc and is
consistent with (does not re-derive, does not modify) the pinned
SF-6 inertia mechanism grounding SR-1; the relativistic remark in
§6 is qualitative and toy-illustrated only.

---

## §1 — SETUP

As in T-1 (D1–D5 of `k1_t1_detailed_balance.md`): bound charge
pattern S with co-moving anchored arc configuration in the
homogeneous DP Sea. New objects:

**D6 (Composite and its energy).** The moving entity is the
COMPOSITE: source + anchored pattern. E(v) denotes the total
energy of the composite in its co-moving steady state at velocity
v (source internal energy + anchored polarization energy + the
anchoring stresses that hold the configuration). The
proportionality claims of T-2 are claims about E(v) of the
composite; §5 discloses what happens when one books only part of
the system.

**D7 (Transition).** An external agent applies force F(t) taking
the composite from steady state at v₁ to steady state at v₂. W
denotes the agent's total work; E_rad the energy carried off by
unanchored propagating content (the transient the change sheds).

## §2 — THEOREM T-2 (statement)

Under A2/A3 (as established below and in T-1), PROTOCOL-D1, and
PRINCIPLE-R1:

**(i) Cost theorem.** Any transition v₁ → v₂ obeys the exact
ledger W = E(v₂) − E(v₁) + E_rad with E_rad ≥ 0, and E_rad → 0 in
the quasi-static (adiabatic) limit. Changing velocity has an
unavoidable minimum cost ΔE = E(v₂) − E(v₁): the establishment
cost of the new co-moving configuration. This is the founder's
2956 sentence as a theorem.

**(ii) Structure: evenness and quadratic leading order.** E(v) is
even in v — reversing v maps the co-moving configuration to its
spatial mirror, and the Sea is parity-symmetric (exactly, at coarse
grain, through degree 5 per FACT G1). Hence
E(v) = E₀ + ½Mv² + O(v⁴) with **M ≡ E″(0)**: the inertia
coefficient IS the velocity-curvature of the establishment cost.
Kinetic energy's quadratic form is derived from Sea parity, not
assumed.

**(iii) Momentum link (Newton 2 structure).** Per Moment, the
agent's force delivers work F·(vτ_M) and impulse F·τ_M — the SAME
force, differing only by the displacement-per-Moment factor. Hence
for the composite, exactly, dE = v·dp. With (ii):
p(v) = M v + O(v³), the same M. Force = dp/dt = M·(dv/dt) at low
v: Newton 2 emerges at mechanism level with a single consistent
inertia coefficient.

**(iv) Mass–energy proportionality.** M scales linearly with the
anchored polarization content. Mechanism argument: the composite's
energy is per-DP additive over the anchored population (quadratic
small-displacement storage); by the SF-6 curl linkage, each
anchored DP's configuration at velocity v carries a curl component
proportional to v on top of its radial component, so each anchored
DP contributes an energy increment ∝ v² — the same quadratic
measure that its rest storage uses. Doubling anchored content
therefore doubles both E₀ and E″(0) together. **Inertial mass ∝
anchored pattern content: the mass–energy link at mechanism
level.** The proportionality COEFFICIENT is deliberately not
minted (charter bar on tuned constants; the toy's coefficients are
toy-specific and disclosed).

**(v) Establishment lemma (discharges T-1's A2 debt).** Under
D-1's per-Moment refresh, the co-moving anchored configuration is
the fixed point of the per-Moment update map, and it is attracting:
source-anchored content is re-sustained each Moment while
unanchored content propagates off at c and does not return.
Therefore the steady state T-1 premised EXISTS and is reached from
generic initial data after a velocity change, with the mismatch
shed as E_rad. (Mechanism level; dynamically demonstrated at toy
grade, W7.)

## §3 — PROOF

**(i).** Energy conservation at the response tier — the whole
ledger by R1 (RATIFIED) — over the transition: the agent's work
enters the composite; whatever is not stored in the final anchored
configuration is, by M1 (below), unanchored propagating content
that leaves and does not return: W = ΔE + E_rad, E_rad ≥ 0 because
radiated energy density is non-negative. Adiabatic limit: as the
transition slows, the configuration tracks the instantaneous
co-moving steady state; the mismatch that sources radiation is
proportional to the tracking error, which vanishes with the ramp
rate; hence E_rad → 0 and W → ΔE. (Toy: W/ΔE = 1.2197 → 1.0307 →
1.0171 from above as the ramp slows, W4; fast-ramp excess equals
the measured far-field radiated energy to 0.3%, W5.) ∎

**(ii).** Mirror map: the configuration at −v is the parity image
of the configuration at +v (the arcs' rotation sense flips with
the sense convention fixed at T-1, which T-1 proved inert). Parity
symmetry of the Sea (exact through degree 5, G1) makes the mirror
image energy-degenerate: E(−v) = E(v). An even function smooth at
0 has E(v) = E₀ + ½E″(0)v² + O(v⁴). Define M ≡ E″(0). Degree-6
lattice corrections enter the O(v⁴)-and-angular terms, not the
quadratic coefficient's existence. (Toy: parity exact, W3;
curvature/β² matches the toy's own exact series 3 + 5β² + 7β⁴ to
6e-4, W3b — quadratic leading order confirmed with the toy's NLO
structure fully accounted.) ∎

**(iii).** The substrate's motion is re-caused per Moment (T-1):
under external force F, the composite's per-Moment displacement is
vτ_M, so per-Moment work = F·vτ_M while per-Moment impulse =
F·τ_M. Dividing: dE = v·dp — a kinematic identity of re-caused
motion for the composite, exact, no dynamics assumed. Integrating
with (ii): p(v) = ∫dE/v = ∫(Mv + O(v³))dv/v·… more directly,
dE/dv = v·dp/dv with dE/dv = Mv + O(v³) gives dp/dv = M + O(v²),
so p = Mv + O(v³) — the same M. ∎

**(iv).** Per-DP additivity: the anchored configuration's energy
is a sum of per-DP quadratic storage terms (small-displacement
form, generic, no tuned constant). SF-6 curl linkage: at velocity
v each anchored DP's displacement acquires a curl component ∝ v
(this is the shipped identification of B for a moving charge, used
as-is). The per-DP energy increment at velocity v is therefore
quadratic in v with a coefficient set by the SAME per-DP storage
measure as its rest term. Summing over the anchored population: E₀
and ½Mv² scale together, linearly in content. (Toy: doubling
source amplitude scales the rest energy and the velocity-curvature
by the identical factor 4 = A², to machine precision, W6 —
amplitude scaling is the toy's proxy for content, disclosed.) ∎

**(v) Lemma M1 (establishment/attraction).** Decompose the field
content each Moment into anchored (source-sustained, per D-1's
refresh of every GP in the volume) and unanchored (everything
else). The per-Moment update: (a) anchored content is re-created
by the source's SSV imprint — the co-moving configuration
reproduces itself translated by δ (this is T-1's fixed-point
statement); (b) unanchored content receives no sustaining imprint
and propagates at c (relay tier); since c > v, it outruns the
source and exits any co-moving neighborhood, never to return
(ballistic, no back-scatter at the relay tier per Version B's
outward-only volley). So the co-moving neighborhood converges to
the anchored fixed point; the departed content is E_rad. (Toy,
W7: after an abrupt kick from rest, the energy-carrying
observables (φ_x, φ_t) converge to the analytic co-moving steady
state to 0.3% in the co-moving window while the transient departs;
books close to 1e-3, W7b. The toy also exhibits an energy-inert
constant offset in the wake — a gauge-like potential shift
carrying no energy — predicted analytically by d'Alembert
bookkeeping and matched to five digits, W7c; disclosed as a
toy-1D feature, not a mechanism claim.) ∎

## §4 — WHY THERE IS INERTIA AT ALL (the mechanism in one paragraph)

T-1 showed coasting is free: the co-moving pattern pays for its
own fore-charging out of its aft-discharging, every Moment,
exactly. T-2 shows why CHANGING v is not free: a different v means
a DIFFERENT co-moving configuration (more curl content per
anchored DP, per SF-6), and the substrate provides no channel by
which the old configuration can become the new one without the
agent supplying the difference — the relay tier can't pay (R1:
sampling moves no energy) and the Sea can't pay (T-1: it is
returned unchanged). So the agent pays ΔE at minimum, plus
whatever tracking mismatch it sheds as radiation. Inertia is the
Sea's establishment invoice for a new co-moving arc pattern; mass
is the size of that invoice per unit of (v²/2); and the invoice
scales with how much pattern there is to re-establish — which is
the mass–energy link.

## §5 — ACCOUNTING DISCLOSURE: COMPOSITE vs PARTIAL BOOKS

The theorem's claims are for the COMPOSITE (D6). If one books only
the field content and omits the anchoring stresses (the classic
partial-accounting trap), the field-only momentum and the
field-only energy curvature yield DIFFERENT apparent inertia
coefficients — the toy exhibits this exactly per its own
analytics (field p(v) = v(c²−v²)⁻²G vs energy curvature 3E₀/c²,
W8), and the discrepancy is the known incomplete-system effect,
not a mechanism failure. The mechanism-level identity dE = v·dp
(iii) holds for the composite, where the agent's force is the only
external channel. Registered as a scope note so no reviewer
mistakes the toy's partial-books split for a T-2 inconsistency.

## §6 — QUALITATIVE RELATIVISTIC REMARK (toy-illustrated, no claim minted)

The toy's exact steady-state energy grows without bound as v → c
(its co-moving profile steepens as (c²−v²)⁻¹ — a
contraction-like factor appearing from the wave structure alone).
Qualitatively this is the right shape for the relativistic growth
of inertia and is consistent with the SF-6/SR-1 grounding picture;
the toy's specific exponents are 1D-scalar-specific and no
relativistic coefficient is claimed here. Any quantitative CPP
statement stays with the shipped SR/SF-6 corpus.

## §7 — VERIFY SCRIPT

`code/2965_t2_establishment_toy.py` — genuine dynamical toy (1D
scalar wave field, moving dipole source ρ = g′, leapfrog, closed
energy books). 12/12 PASS: books close (W1); analytic co-moving
steady state propagates self-similarly and matches U(v) (W2/W2b);
E(v) even with quadratic leading order matching the toy's exact
series (W3/W3b); adiabatic limit W/ΔU → 1 from above (W4);
fast-ramp excess = radiated energy to 0.3% (W5); content scaling
exact (W6); establishment after an abrupt kick with the transient
departing and books closing (W7/W7b), including the predicted
energy-inert wake offset to five digits (W7c); field-momentum
fidelity to the toy's own analytics (W8). First-run findings, all
disclosed in reasoning/2965.md: two check-design fixes (raw-φ was
the wrong establishment observable — the energy-carrying pair
(φ_x, φ_t) is right; the curvature tolerance ignored the exact
series' NLO/NNLO terms, twice) and one hand-algebra slip in the
offset prediction corrected against the numerics ((c−v), not
(c+v)).

## §8 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL (= OPEN-K1-MEMORY-1); B7
holds DM-1/DM-3 banners; Candidate (B) 79.5%; 2855 PROVISIONAL;
d_DP ceiling ACTIVE. T-2 status: ESTABLISHED-AT-MECHANISM-LEVEL,
PANEL-PENDING (combined completed-package review with T-1/T-3 per
charter §3). T-1's A2 debt: DISCHARGED (Lemma M1 + W7). Next in
the frozen order: **W-3 (T-3, the DM-ring instance — the K1
stiffness, THE 7th derivation).**


---

## §R1 (v1.1, C-3) — Lemma T-2.P: orientation-sense energy degeneracy

**The panel's worry (GPT Q2; dispatch Q2 attack line):** the arcs
carry a rotation SENSE; does the mirror map genuinely produce an
energy-degenerate configuration, or does sense-flip break the
degeneracy? The v1.0 proof used the degeneracy without stating it.

**Lemma T-2.P.** Let P be the Sea parity map — the inversion
element: positions → −positions about the pattern center,
velocities → −velocities (true vectors), and every arc's rotation
sense UNCHANGED (a sense is a PSEUDOVECTOR: inversion-even; this is
the transformation law, not a choice). Then E(P·config) =
E(config) for every admissible configuration, hence E(v) = E(−v).

**Proof.** (i) The stored-energy functional is built from
I_h-equivariant stencil contractions (FACT G1's class). (ii) The
icosahedral group I_h CONTAINS the inversion −1 (I_h = I × {±1};
equivalently: the 12-direction stencil is centrally symmetric,
antipodal pairs — verified as CHECK 1 of the sweep). (iii)
Therefore invariance of the functional under I_h already includes
invariance under P. In particular every P-odd scalar a chiral term
could ride on (e.g. a position–sense contraction x̂·ŝ, odd because
x̂ flips and ŝ does not) is EXCLUDED from the functional by the G1
class — this exclusion, not a sense flip, is what protects the
degeneracy. (iv) P maps the +v translated steady state onto a −v
translated state with the SAME arc senses; because inversion is a
symmetry of the stencil dynamics, the image of a steady state is a
steady state, i.e., an admissible −v steady state; by (iii) the two
are exactly energy-degenerate. ∎

**Answering the panel's question as ASKED.** The dispatch asked
whether "sense-flip breaks the degeneracy." The precise answer: the
sense does not flip under the degeneracy-generating map at all —
pseudovectors are inversion-even — and the degeneracy is protected
because the G1 functional class admits no term odd under the map.
The v1.0 compression hid this; the first sweep run then exposed
that the worker itself had the transformation law backwards (the
toy's negative control refused to fire under a sense-flipping map —
the P-odd probe term was accidentally invariant), which is recorded
publicly in `reasoning/2976.md`: the toy corrected the worker on
the very point the panel flagged.

**Remark (what would break it).** If the functional carried an
I-equivariant-but-not-I_h-equivariant term (a genuinely chiral term
odd under inversion), the degeneracy would fail and E(v) could
carry odd powers. The registered stencil class excludes this (G1);
the substrate chirality results (FI-C-9 line) live in a different
object (the pseudoscalar sign, not the stored-energy functional)
and do not inject such a term — noted so the chirality arc and this
lemma are seen to be consistent, not in tension.

## §R2 (v1.1, C-4) — dE = v·dp: the route DECLARED

**The panel's demand (DeepSeek Q2; GPT Q2):** derive dE = v·dp from
re-caused motion, or declare the definitional route — the theorem
must say which it takes. **Declaration: T-2 takes the
DEFINITIONAL-WITH-CONSISTENCY route.** Explicitly:

1. E(v) = E₀ + ½Mv², M ≡ E″(0), is DERIVED (parity, §R1 + G1
   through degree 5, + smoothness) — no momentum concept used.
2. p is DEFINED as the composite's book momentum: the cumulative
   pairwise-reciprocal impulse tally of the composite's books
   (well-defined because every interaction event balances pairwise,
   §R3 of T-1 v1.1), normalized to p = 0 at v = 0.
3. **Consistency (the content):** at linear order, the book
   momentum changes ONLY through external impulse — because by T-1
   (now available: the DAG is M1 → T-1 → this step, no cycle) the
   Sea's exchanges with the coasting composite cancel exactly over
   traversals. External quasi-static work dW = ΔE with E from (1)
   then gives, along any adiabatic path, dE = M v dv; and the same
   external impulse gives dp = M dv IF AND ONLY IF the book
   momentum satisfies p = Mv. The toy's establishment dynamics
   verifies precisely this (v1.0's p_num = p_ana check; re-run in
   the 2976 sweep across parameters), closing the consistency loop:
   the DEFINED p and the DERIVED E satisfy dE = v·dp identically,
   with the same M in both.
4. What is NOT claimed: Newton 2 as input (no force law is assumed
   — the external agent is a boundary condition of the ledger);
   conservation of p from translation symmetry (that is downstream
   OUTPUT territory, with B-1, not input); any physical value of M
   (coefficient deliberately not minted, unchanged).

DeepSeek's own Q2 analysis exhibited exactly this route as the
legitimate one ("p = Mv + constant; the constant is zero if p = 0
at v = 0 … so it works") — the defect was silence about which route
the theorem took. The silence is hereby removed.

## §R3 (v1.1, Copilot 2974) — M ∝ anchored content: the sweep

Copilot's added requirement: a numeric sweep of M against anchored
content with uncertainties. Executed in
`code/2976_t2_parity_sweep.py`: toy composites at anchored-content
counts N_a swept over an order of magnitude; M extracted per N_a
from the establishment-energy curvature with bootstrap
uncertainties; linear fit through the origin. Result (toy units):
proportionality confirmed at the toy level — slope stable,
intercept consistent with zero, R² at the 1-per-mille level of
unity (exact figures in the script output). SCOPE unchanged from
v1.0: this is the toy-level demonstration of the per-DP-additivity
+ curl-linkage structural consequence; the proportionality
COEFFICIENT remains deliberately not minted; instrument-grade
standing unchanged.
