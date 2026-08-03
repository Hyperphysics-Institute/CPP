# K1-MEMORY W-3 — THEOREM T-3: THE DM-RING INSTANCE — THE K1 STIFFNESS FROM THE ARC MECHANISM (THE 7th DERIVATION)

**Patch 2966 (3 Aug 2026). Executes W-3, the final work item of the
K1-MEMORY derivation charter (`k1_memory_derivation_charter.md`,
Patch 2961): the Candidate B core/coat plane oscillation derived as
the bound-state version of the T-1/T-2 charging/discharging arc
storage, with its stiffness — the K1 stiffness — obtained as a
mechanism-level object, and the memory-kernel decomposition that
PR7 clause 2's specification requires. Verify script
`code/2966_t3_ring_stiffness_toy.py` (13/13 PASS). Status: T-3
ESTABLISHED-AT-MECHANISM-LEVEL, PANEL-PENDING; the T-1/T-2/T-3
package is COMPLETE and queued for combined CONV-011 review per
charter §3. This patch does NOT touch the PR ledger (enactment is
panel business, 2827); the clause-2 closure instrument is specified
in §6 for its own preregistered patch. No value of any open
quantity is minted; the ring's physical stiffness magnitude and the
2433 soft/stiff fork are NOT resolved here and are explicitly out
of scope.**

**Assumptions cited (charter duty, every result):**
- **PROTOCOL-D1** (2960, reopenable working default) — grounds the
  per-Moment anchoring refresh (via T-2 Lemma M1).
- **PRINCIPLE-R1** (2961, **RATIFIED** 2963, reopenable) — the
  relay tier moves no energy; the response-tier account is the
  whole ledger.

**NAME COLLISION, DISAMBIGUATED AT EVERY USE:** PRINCIPLE-R1
(sampling not consumption) is UNRELATED to PR7 clause 2's
"R1 (memory)", which is the KINETIC-1 memory-kernel residual
renamed **OPEN-K1-MEMORY-1** by the panel-ratified 2831 naming
motion. This document writes **K-MEM** for the latter throughout.

**Admissible inputs used:** T-1 (2964) and T-2 (2965),
arc-internal, PANEL-PENDING as a package; the 2956 verbatim arc
mechanism (§4: "the core/coat plane oscillation as the BOUND-STATE
version of the same charging/discharging storage, whose stiffness
is the K1 stiffness"); the 2433 founder-corrected Candidate B
geometry (two planes of eCP–qCP–qCP–eCP crosses; jello qCP core
with no static bending integrity; eCP coat the sole static
resistance); V-2 GP protocol; SF-6 curl linkage; FACT G1.
**Bars honored:** no α1-chain descendants, no AUTOMATON occupancy
values, no tuned constants, no QM-1 lineage (TODO-2957-B open); no
value of ξ₂, ζ, η, d_DP, n_DP, or N; the E_qq window, κ_θ/E_bond,
and every 2433 fork quantity remain exactly as registered.

---

## §1 — THE MODE

**D8 (Coordinate).** Let x be the relative displacement of the qCP
core against the eCP coat structure within a Candidate B element
(the core/coat plane oscillation of 2956 §4), measured from the
bound equilibrium. Per the 2433 founder geometry, the equilibrium
configuration has a reflection symmetry through the element's
mid-plane; x and −x are mirror configurations.

**D9 (Stored content).** At displacement x (held quasi-statically),
the element's CPs anchor a re-arranged Sea/internal polarization
configuration; E(x) denotes the total energy of the composite
(element + anchored content) in that configuration — the SAME
energy functional as T-2's E(v), now read along a displacement
coordinate instead of a velocity coordinate. At displacement AND
velocity, E = E(x, ẋ) with the T-2 structure in ẋ.

## §2 — THEOREM T-3 (statement)

Under the T-1/T-2 premises, PROTOCOL-D1, and PRINCIPLE-R1:

**(i) Existence and quadratic leading order of the stiffness.**
E(x) is even in x (mirror symmetry of the configuration + Sea
parity, exact through degree 5 per FACT G1), so
E(x) = E₀ + ½K₁x² + O(x⁴) with **K₁ ≡ ∂²E/∂x²(0): the K1
stiffness exists as the displacement-curvature of the anchored
content's establishment cost.** This is T-2(ii) with velocity
replaced by displacement — the same theorem shape, the same
mechanism, the same energy functional.

**(ii) The bound-state storage identification.** The oscillation
x(t) = A cos(ωt) is the bound-state version of T-1's
charging/discharging cycle: as the core moves toward one coat
plane, the compression-side anchored content charges while the
extension side discharges; at the turning points the mode's energy
sits in displacement storage (½K₁x²), at mid-swing in velocity
storage (½M₁ẋ², which by T-2(iv) is itself anchored curl content).
**The whole oscillation is arc content breathing between its
displacement form and its velocity form — energy shuttles at 2ω
between the two storages of one functional.** Nothing outside the
anchored content participates at leading order.

**(iii) One functional, both coefficients.** The mode frequency is
ω² = K₁/M₁ where M₁ = ∂²E/∂ẋ²(0) is the T-2 inertia of the same
content. **Both coefficients are curvatures of the single anchored-
content energy functional E(x, ẋ)** — stiffness in x, inertia in
ẋ. No object beyond the arc storage is needed to characterize the
mode; this is the 7th derivation's content: the K1 stiffness is
not a new posit but the displacement face of the same storage whose
velocity face is inertia (T-2) and whose steady state is Newton 1
(T-1).

**(iv) Content structure and the jello-core exclusion.** K₁ is
per-DP additive over the anchored content re-arranged by the
displacement (T-2(iv) machinery). Per the 2433 founder ruling, the
jello qCP core contributes no STATIC restoring term (no static
well; ZBW-held soup), so **K₁'s static part is carried by the eCP
coat's anchored content** — the mechanism-level derivation agrees
with, and grounds, the founder's "the eCP coat is the sole bending
resistance." What the core contributes is inertia (M₁ content) and
any DYNAMICAL (average/ponderomotive) terms — which belong to the
open 2433 fork machinery, not to this theorem.

**(v) Radiative width.** The mode's damping is the unanchored
leakage of T-2 Lemma M1: content the oscillation fails to
re-anchor departs at c and does not return. The mode is therefore
conservative at leading (anchored) order with a radiative width
set by the leakage — consistent in kind with the campaign's
existing dissipation-channel treatment
(`OPEN-DM-CAPTURE-1_dissipation_channel.md`), which is neither
re-derived nor modified here.

## §3 — PROOF

**(i).** Mirror map: the configuration at −x is the reflection of
the configuration at +x through the element mid-plane (D8). Sea
parity (G1, exact through degree 5) makes reflected configurations
energy-degenerate, so E(x) = E(−x); smoothness at the bound
equilibrium gives the quadratic leading order; K₁ ≡ E″(0). The
lattice fingerprint enters at degree-6/O(x⁴) order, not against
the quadratic term's existence. (Toy: parity to 4e-16; quartic
fraction 0.001 on the scan; K₁ matches the toy's closed-form
overlap curvature to 4 digits, X1–X1d.) ∎

**(ii).** At quasi-static displacement the books are T-2(i) with
E_rad → 0: work in = ΔE = ½K₁x² stored in anchored content. At
mid-swing the same content carries the T-2 velocity form. Over a
cycle the exchange is internal to E(x, ẋ): T-1's detailed balance
(per-DP cycle closure) applies to each half-cycle's
charge/discharge pair, so no net content is created or destroyed
per cycle at anchored order; what escapes is (v)'s leakage. (Toy:
near-core stored energy anti-correlates with mode KE at −0.92 and
the exchange runs at exactly 2ω — 0.3471 vs 0.3471, X3/X3b.) ∎

**(iii).** Small oscillations of the coordinate x in the
functional E(x, ẋ) = E₀ + ½K₁x² + ½M₁ẋ² + … give ω² = K₁/M₁
directly. That M₁ is the T-2 inertia OF THE SAME content is
T-2(iii)/(iv) applied to the mode coordinate. (Toy: the frequency
predicted from statics-K₁ plus the independently drag-measured
dressing agrees with the directly observed oscillation frequency
to 8% in the adiabatic regime, with the residual's direction being
the finite-ω dressing deficit — retardation, i.e. exactly the
memory content §6 bounds; the non-adiabatic regime's larger
deficit was observed at small bare mass and is disclosed, X2.) ∎

**(iv).** Per-DP additivity as in T-2(iv). The static exclusion of
the qCP core is imported from the 2433 founder registration as a
geometry fact (Earnshaw-type absence of a static well), not
re-derived; its consequence at mechanism level is immediate: a
component with no static well contributes no E″(0) term, so the
static K₁ sums over coat-anchored content only. (Toy: K₁ scales
linearly with coat source strength, exactly 2.0000 at doubling,
X6 — the additivity proxy.) ∎

**(v).** T-2 Lemma M1 verbatim, applied to the oscillating
anchoring. (Toy: amplitude 0.150 → 0.057 over the run with the
lost mode energy accounted in the far field and total books
closing to 1e-3, X4/X4b.) ∎

## §4 — WHAT THE 7th DERIVATION IS (one paragraph)

Six derivations stand behind Candidate B's ledger; the seventh was
owed for the object that holds the ring together as a DYNAMICAL
thing: the stiffness of its internal core/coat oscillation. T-3
derives that stiffness from the arc mechanism with no new posits:
the Sea's anchored displacement content — the same content whose
steady co-motion is Newton 1 (T-1) and whose establishment cost is
inertia and mass (T-2) — has a displacement-curvature, and that
curvature IS the K1 stiffness. Stiffness, inertia, and coasting
are three faces of one storage. The founder's 2956 sentence
("the core/coat plane oscillation as the bound-state version of
the same charging/discharging storage, whose stiffness is the K1
stiffness") is now a theorem chain rather than a picture.

## §5 — SCOPE FENCES (what T-3 does NOT do)

1. **No magnitude.** K₁'s physical value requires the anchored-
   content profile of the actual element (E_qq window, coat
   geometry, the 2433 fork quantities) — all open, all barred
   here. T-3 delivers the object, its symmetry-forced form, its
   content decomposition, and its relation to M₁; not a number.
2. **The 2433 soft/stiff fork stands.** Whether the ring family
   closes at N=8 or drifts is a magnitude question (κ_θ/E_bond);
   nothing here moves it. T-3 is consistent with EITHER branch.
3. **No PR enactment.** PR7 remains PARTIAL; six of seven stands;
   the ledger line is untouched. §6 specifies the closure
   instrument; the closure is its own preregistered patch and the
   status motion is the panel's.

## §6 — THE FEED TO PR7 CLAUSE 2 (K-MEM): THE MECHANISM-DERIVED KERNEL DECOMPOSITION

Clause 2 (frozen text) requires K-MEM "bounded subdominant at the
d_DP scale," to S1's five-part specification (2829): defined
kernel/correlation function; evaluation at physical d_DP; a
preregistered subdominance threshold; uncertainty and finite-size
controls; separation from short-range transient and regulator
effects. T-3 supplies the mechanism-level structure that makes
that measurement well-posed:

**Decomposition (mechanism-derived).** Under the arc mechanism,
the Sea's retarded force response at a tagged CP splits exactly
along the T-2 M1 decomposition:

- **Anchored part** — source-sustained co-configured content.
  This is CONSERVATIVE storage: in Mori–Zwanzig language it
  renormalizes the INSTANTANEOUS (Markovian) force term — it is
  stiffness and inertia dressing, NOT dissipative memory. The K1
  arc's entire content lives here.
- **Unanchored part** — content not re-sustained, departing
  ballistically at c with no back-scatter (Version B outward-only
  volley; PRINCIPLE-R1's non-destructive transit) and no return
  (M1). Its force autocorrelation therefore has support bounded by
  the transit time of the correlated volume — at the d_DP scale,
  t_K ≲ d_DP/c — with no long-time tail.

**Prediction (testable, falsifiable).** The mechanism therefore
predicts **Markovian-plus-stiffness response at d_DP**: the
dissipative kernel K(t) is transient-only with ballistic support,
and the apparent "memory" beyond it is the conservative anchored
renormalization, separable by its reactive (non-dissipative)
phase. (Toy demonstration at X5/X5b: the clamped step response
settles to the static stiffness value within the ballistic time
2L/c, with the tail beyond at 1e-12 of the step scale — Markovian
plus stiffness, no memory tail; and X2's finite-ω dressing deficit
exhibits the reactive part's frequency dependence in the
non-adiabatic regime, which vanishes adiabatically.)

**Closure instrument (specified, not executed).** Route (a) or
(b) of the 2831 N3 advisory, executed as its own preregistered
patch with: the kernel DEFINED as the dissipative (odd/absorptive)
part after subtracting the anchored reactive renormalization
(this document's decomposition supplying spec item 1 and the
transient-separation principle of item 5); evaluation at physical
d_DP (item 2); a preregistered subdominance threshold ∫K dt vs the
instantaneous term (item 3); uncertainty/finite-size controls
(item 4). A measured long-time dissipative tail at d_DP would
CONTRADICT this section's prediction — registering that as the
arc's exportable falsifier: the K1 mechanism stands or falls with
Markovian-plus-stiffness at d_DP.

## §7 — VERIFY SCRIPT

`code/2966_t3_ring_stiffness_toy.py` — the 2965 dynamical toy
promoted to a bound state (dynamical core between two fixed coat
dipoles, closed total books; the restoring opposite-sign coupling
is a toy device, disclosed). 13/13 PASS: E(x) parity to 4e-16 with
quadratic dominance and K₁ matching the closed-form overlap
curvature to 4 digits (X1–X1d); two independent frequency routes
agreeing to 8% in the adiabatic regime with the residual direction
identified as retardation (X2), and the dressing a 27% effect —
stiffness AND inertia visibly from the same stored content (X2b);
energy shuttling at exactly 2ω with −0.92 anticorrelation
(X3/X3b); books closing with radiative decay accounted (X4/X4b);
the clamped step response Markovian-plus-stiffness with ballistic
support and a 1e-12 tail (X5/X5b); stiffness linear in coat
content (X6). First-run findings, disclosed in reasoning/2966.md:
one REAL sign bug in the static solver (whose signature — a fake
restoring well at exactly 3× the true curvature — is itself
instructive), one hard-coded sign slip in the scaling check, and
two measurement-design lessons (near-core window; adiabatic
regime for the two-route comparison).

## §8 — LEDGER

Nothing moves: six of seven; PR7 PARTIAL (= OPEN-K1-MEMORY-1,
K-MEM); B7 holds DM-1/DM-3 banners; Candidate (B) 79.5%; 2855
PROVISIONAL; d_DP ceiling ACTIVE. T-3 status:
ESTABLISHED-AT-MECHANISM-LEVEL, PANEL-PENDING. **The T-1/T-2/T-3
package is COMPLETE**: queued for the combined CONV-011
completed-package review per charter §3, alongside the already-
queued E-1+E-2 items, the 2951 roadblock item, and the PR2 verdict
ambiguity (2962-audited pending list). The K-MEM closure
instrument of §6 is schedulable as its own preregistered patch
under the campaign's promotion governance.
