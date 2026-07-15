# SR-MECH-2485 — mechanism session derivation log

**Campaign instrument:** `OPEN-SR-H1-CLASS_campaign.md` v1.2 (binding: burden M1–M9,
kills K1–K4 incl. K3′/K3a, K4-committed candidate (a) the (ê_motion, τ̂) plane —
founder-ratified Patch 2487).
**Session order (fixed by campaign §5.3):** M4 → M9 → candidate (a) vs full burden.
**Discipline:** K3/K3′/K3a logged per step, in this file, at the step where each
judgment call occurs. Any claim goes back to the panel with the campaign file (K2).
**Effort clock (K1):** this is session 1 of the founder-bounded default 2.

---

## Step 1 — M4: arena determination (Patch 2488)

### Verdict

**The displacement arena is the PSR insphere — the ball.** The Voronoi polytope is
the *ownership* partition of the lattice, not the *reach* set of a Moment; the reach
constraint binds first everywhere, so the tube–polytope intersection M4 contemplated
never arises. Leading coefficient π·A₂·l_P²/V_cell = 2 **exactly, by arena derivation
rather than assumption**. M4 does not kill. Status: **PASSED, postulate-grounded via
A3′'s transport clause, with one scope caveat logged for K2 (below).**

### The derivation (forward; every input pre-dates the target)

**(i) The per-Moment bound is a speed, and a speed is a scalar.**
Axiom A3′ (registered Patches 1121–1129, 11–12 June 2026, drafted for the
GR-radiation sector — a month before OPEN-SR-H1-CLASS existed) fixes transport at
c = l_P/t_P "in the absolute (Nexus) frame with **flat per-hop transport**," and
couples matter "only via **geodesics** of the unique constraint-consistent assembled
metric." A scalar per-hop speed means the set of positions reachable in one Absolute
Moment is {Δx : |Δx| ≤ c·t_P} — a **ball of radius l_P** in the rest frame. This is
not a modeling choice; it is what the axiom's flat isotropic c *means*. A
direction-dependent Planck-scale reach (polytope arena) would make c anisotropic at
order unity, falsifying A3′'s flat-transport clause as written and breaking every
sector built on scalar c.

**(ii) The corpus states the same thing independently, everywhere, pre-target.**
- Glossary (pre-0736 era): PSR = "the effective displacement per Absolute Moment,"
  the "per-Moment reach ceiling" — stated as a *radius*, i.e. direction-independent.
- SR-1 §"Voronoi insphere and the baseline PSR" (Patch-0736 era): "the effective
  spatial PSR is the **insphere radius** of the 3D spatial cross-section of the
  Voronoi cell"; the strain variable of the constitutive rule V ∝ r⁴ *is* the
  insphere radius throughout SR-1's Appendices D.4/E/H.
- A3′ itself broadcasts to "its **PSR shell**" — the axiom text carries the sphere.

**(iii) The polytope never binds.** SR-1's Planck normalisation (pre-target) defines
l_P as the rest-frame insphere radius: r_in ≡ l_P. The reach ball is therefore
exactly the *inscribed* ball of the Voronoi cell — tangent to all 12
perpendicular-bisector faces from inside. Arena = reach ∩ cell = ball ∩ polytope =
**ball, exactly** (an inscribed ball's intersection with its own polytope is itself,
by definition of inscribed). The cell's corners exist but are unreachable within one
Moment; under stress the cell shrinks and PSR_eff = the shrunken insphere shrinks
with it — the arena remains the (stressed) insphere ball at every stress level.

**(iv) The coefficient.** With arena = ball: A₂ = π l_P² (central 2-plane section),
V_cell = π² l_P⁴/2, so π·A₂·l_P²/V_cell = **2 exactly** — and every higher order of
2f² − f⁴ comes with it (the identity is all-orders; campaign §2.2).

**(v) Counterfactual (kill-liveness).** For a polytope arena of the same inradius —
computed for the 4-cube — the leading coefficient is π/4 ≈ 0.785 ≠ 2 and the strain
curve misses γ − 1 at every order. Had the postulates given the polytope, the
campaign would have died at this step. The kill had teeth; the ball verdict is not
vacuous. Verify: `series_relativity/code/2488_m4_arena_coefficient.py`
(stdlib, fixed seed, C1–C5, ALL PASS).

### §2a scope-condition disposition

Campaign §2a condition 1 ("continuum-conditional") is **discharged**: the
countervailing substrate fact it recorded ("the PSR is by definition a sphere
radius — if the displacement arena is the PSR insphere the ball is exact") is what
the derivation lands on, now *settled not chosen*, from A3′ + the pre-target
constitutive structure. The identity's arena condition is met by derivation.

### K3 / K3′ / K3a log for this step

- **K3 (explicit target invocation):** none. No step above invokes n = 2, γ, or
  coefficient 1 as a premise. CLEAN.
- **K3′ (implicit-target test — "would the step have been taken, in that form, by a
  derivation that did not know the target?"):** the load-bearing selection is
  reach-set = ball. A target-ignorant derivation, asked "what positions can a CP
  occupy at the next Moment," reads A3′'s scalar flat-transport c and answers "the
  ball of radius c·t_P" — there is no fork at which the polytope was live *given the
  axiom text*, and the axiom text is a year-class artifact of another sector. CLEAN.
- **K3a (intermediate-principle launder + n = 3 counterfactual):** no new principle
  is posited; every input (A3′, glossary PSR, SR-1 insphere normalisation) is
  corpus-established pre-target. Counterfactual test: if the target were n = 3, the
  identical reasoning yields the identical ball — which would then *fail* to produce
  n = 3. The reasoning does not bend to the target. PASS.

### Caveat logged for the K2 panel (stated against interest)

The single-CP per-Moment *target-set* rule is not a standalone axiom. The ball
conclusion is carried by (a) A3′'s flat-per-hop-c + geodesic-coupling clauses and
(b) the corpus-wide pre-target definitional structure (glossary reach ceiling; SR-1
insphere-variable constitutive rule; PSR-shell axiom text). If the panel judges
A3′'s matter clause to govern only aggregate-scale geodesic motion and not the
single-CP per-Moment reach set, M4's status drops from **postulate-grounded** to
**corpus-conditional** and the gap becomes an explicit foundational input (FI) of
the eventual mechanism claim. This scope question ships with the K2 package. Note
also that M6 (micro-to-macro bridge) remains fully open regardless — M4 settles the
*arena*, not the aggregate-level exclusion rule.

### Step outcome

M4 **PASSED**. Next step per campaign §5.3: **M9 stress-scaling** (second-cheapest
kill — local (v/c)·PSR_eff vs absolute (v/c)·l_P; the absolute branch kills for
stressed aggregates; fork pinned in `code/2486_stressed_arena_fork.py`). Note M4's
clause (iii) above bears on M9: the arena tracks the *stressed* insphere
(PSR_eff), which is the local branch's premise — but M9 requires the scaling of the
*exclusion radius d*, a distinct object, so nothing is prejudged; the M9 derivation
must come forward on its own.

---

## Step 2 — M9: stress-scaling (Patch 2489)

### Verdict

**The fork dissolves.** The exclusion radius is the kinematic per-Moment drift
d = v_abs·t_P — Branch L's formula in *absolute* velocity — and c07's pre-target
channel structure makes that same d **identically** Branch P's formula in *locally
measured* velocity: d = (v_loc/c)·PSR_eff. The two branches are one rule expressed
in two velocity variables; they are exclusive only if "v" is assumed to denote the
same variable in both formulas, which nothing in the postulates licenses.
Consequences, all verified (`code/2489_m9_stress_scaling.py`, V1–V5 ALL PASS):
ε = γ(v_loc) − 1 at every background stress; composition exactly multiplicative
g_bg·γ(v_loc); the reduced *coordinate* ceiling c/g_bg is exactly the point
v_loc = c (Shapiro-consistent, locally measured ceiling = c — not a pathology).
Status: **RESOLVED-BY-DISSOLUTION — PENDING K2 PANEL CONFIRMATION.** Because this
derivation defuses a registered kill trigger, the dissolution is itself a claim;
it is NOT self-certified here and ships to the panel with the K2 package.

### The derivation (forward)

**(i) d is kinematic and forced.** M3's own registered text sets the exclusion
radius at d = v·t_P — the distance the aggregate actually drifts per Absolute
Moment in the Nexus frame. A coordinate drift distance is what it is; no postulate
rescales it. In the 2486 fork's labels this is Branch L: d = (v_abs/c)·l_P.

**(ii) f = (v_abs/c)·g_bg.** Arithmetic: f = d/PSR_eff with the M4 arena (stressed
insphere, radius l_P/g_bg, an absolute-frame length — the cell shrinks in absolute
coordinates; that is what "Voronoi volume shrinks" has meant since SR-1).

**(iii) The velocity variable is fixed by c07, pre-target.** c07's metric
identification (Definition, eqs. g_tt/g_ij) sources the two channels differently:
g_tt from the scalar **magnitude** Δ|SSV|_abs (the PSR contraction — clocks), and
g_ij from the **gradient tensor** |∇SSV_net|_ij — a different LSP component. For
M9's registered setup — *uniform* background stress, ∇SSV_bg = 0 — this gives
g_ij = δ_ij: **rods are unaffected; only clocks slow** (dt_loc = dt_abs/g_bg, the
SR-1 core mechanism). Hence the locally measured velocity is v_loc = v_abs·g_bg.
This channel split is load-bearing for c07's factor-of-2 lensing result (the
retroactive Eddington prediction) and predates this campaign entirely.

**(iv) Substitution.** f = (v_abs/c)·g_bg = v_loc/c. So
d = (v_abs/c)·l_P = (v_loc/c)·(l_P/g_bg) = (v_loc/c)·PSR_eff, identically (V1).
Branch L ≡ Branch P. Then ε = γ(v_loc) − 1 exactly at every g_bg (V2); the total
reach factor composes as l_P/r_total = g_bg·γ(v_loc), exactly multiplicative (V3);
and f = 1 occurs at v_abs = c/g_bg, i.e. precisely v_loc = c (V4) — the coordinate
light-speed reduction the corpus already carries as Shapiro structure.

**(v) Counterfactual (kill-liveness).** Had c07 sourced g_ij from the magnitude
channel too (rods contracting by g_bg under uniform stress), then
v_loc = v_abs·g_bg², f = (v_loc/c)/g_bg, and ε ≠ γ(v_loc) − 1 for every g_bg > 1:
M9 would have killed (V5). The outcome is decided by c07's pre-target channel
structure, not by anything selected in this session. The kill path was live.

### K3 / K3′ / K3a log for this step

- **K3:** no step invokes γ, n = 2, or coefficient 1 as a premise. The target
  (multiplicative composition) is compared against AFTER the derivation lands,
  never used to steer it. CLEAN.
- **K3′ ("would the step have been taken by a target-ignorant derivation?"):** the
  load-bearing steps are (i) d = v_abs·t_P — definitional kinematics, no fork —
  and (iii) the c07 channel reading. A target-ignorant derivation asking "what do
  uniform-stress backgrounds do to rods and clocks" reads c07's Definition and
  gets the same answer; the gradient-sourcing of g_ij was fixed a sector away,
  for lensing, before this campaign existed. CLEAN.
- **K3a (intermediate-principle launder + n = 3 counterfactual):** the one
  principle invoked — g_tt from magnitude, g_ij from gradient — is
  corpus-established (c07 Definition + the |h_tt| = |h_rr| remark), previously
  used for moving/propagating content (light deflection), not posited here.
  Counterfactual: were the target n = 3 or any other composition law, c07's text
  reads identically and v_loc = v_abs·g_bg still follows; the reasoning does not
  bend. PASS.

### Caveats logged for the K2 panel (stated against interest)

1. **Kill-trigger semantics.** Campaign v1.2's M9 text says "if the derivation
   lands on the absolute branch... K1 fires." This derivation lands on the
   absolute branch's *formula* while showing it is identically the local branch's
   formula in the observable velocity variable — the trigger's premise (branch
   exclusivity) fails. The panel must ratify that reading; if the panel holds the
   trigger to its letter regardless, K1 fires and the negative is recorded. This
   session does not adjudicate its own kill condition.
2. **Uniform-background scope.** The dissolution is exact for uniform SSV_bg (the
   setup 2486 registered). Real gravitational backgrounds carry gradients, where
   c07's g_ij ≠ δ_ij and rod corrections enter at gradient order — tidal/GR
   territory outside M9's registered scope. The scope boundary is explicit.
3. **v_loc operationalisation.** "Locally measured velocity" here means measured
   by co-located stressed clocks and (uniform-case) unstressed rods, per c07's
   channels. If the panel judges a different local-measurement convention to be
   the physical one, step (iv)'s substitution must be re-derived under it.

### Step outcome

M9 **RESOLVED-BY-DISSOLUTION, PENDING K2**. The two cheapest kills (M4, M9) are
now both discharged at session level with live counterfactuals on record. Next
per campaign §5.3: **the committed candidate — (ê_motion, τ̂), K4-binding —
against the full M1–M9 burden**, beginning with M1 (canonical uniqueness of the
distinguished 2-plane). This is the heavy half of the session; K1's effort clock
(two focused sessions, founder-bounded) is running.

---

## Step 3 — M1: canonical uniqueness of the distinguished 2-plane (Patch 2491)

**Session note:** this step opens session 2 of the K1 effort clock (fresh context,
warm keyword SR-MECH-2490). K4-binding: all work below is on the ratified candidate
(a), the (ê_motion, τ̂) plane; no other campaign candidate is constructed or tested.

### Verdict

**Exactly one 2-plane is postulate-distinguished for a uniformly moving aggregate:
Π = span(τ̂, ê_motion) — the committed candidate (a) — and it is canonical: it is
the span of the postulate-available data itself, not a selection among
alternatives.** The uniqueness argument runs over the space of ALL k-planes
(k = 1, 2, 3) on postulate criteria alone; k = 2 emerges as the unique dimension at
which the invariant candidate set is even finite (two members: Π and its
orthocomplement P⊥), and Π is the unique member containing any of the data. At
v = 0 no 2-plane is distinguished, consistently with d = v·t_P = 0. Status:
**M1 PASSED at session level, subject to K2**, with two scope caveats and one
orientation caveat logged below.

### The derivation (forward; every input pre-dates the target)

**(i) Inventory: what the postulates make available for a uniformly moving
aggregate.** The distinguishing data — the structure that separates the moving
aggregate from the same aggregate at rest — is exhaustively:

- **τ̂ — the Absolute Moment axis.** c01 (Absolute Moment postulate, pre-target):
  "every CP advances exactly l_P in the timelike direction once per universal tick
  t_P = l_P/c, frame-independently and independent of local Voronoi-cell stress."
  One universal timelike direction, the same for every CP and every aggregate.
  SR-1 (§3D-projection): the four coordinates are (**x**, τ) with τ = c·t_P "fixed
  and universal," the two subspaces "orthogonal by construction." A3′ carries the
  same structure ("At every Absolute Moment… in the absolute (Nexus) frame").
- **ê_motion — the absolute velocity direction.** The scenario's own
  specification: uniform motion = constant absolute velocity v = v·ê_motion; for
  v ≠ 0 this supplies exactly one unit spatial direction. This is the ONLY datum
  that motion adds.
- **The per-Moment displacement 4-vector.** Δ = c·t_P·τ̂ + v·t_P·ê_motion: the
  temporal part is c01's mandatory universal advance; the spatial part is the
  kinematic drift d = v·t_P already established forward at step 2(i) (Patch 2489:
  "no postulate rescales a coordinate drift distance"). Δ lies in span(τ̂,
  ê_motion) identically, with zero component elsewhere.
- **The arena and its symmetry.** M4 (step 1): the displacement arena is the PSR
  insphere — a round ball. A3′ C2 (flat isotropic per-hop transport) plus the ball
  verdict means the per-Moment displacement problem carries the arena's continuous
  spatial isotropy: SO(3) rotations about the aggregate, with τ̂ fixed (c01/SR-1:
  the Moment axis is a separate universal register, not mixable with space by any
  lattice operation). The arena contributes NO directional structure of its own.
- **What is NOT in the inventory.** (1) Internal aggregate structure (ZBW plane,
  composition, phasing): aggregate-particular and not motion-sourced — it persists
  unchanged at v = 0, where the drift d = 0. Recorded as an inventory fact, NOT as
  an evaluation of campaign candidates (b)/(c) — K4 intact. (2) The GP lattice's
  discrete orientation: excluded from per-Moment displacement kinematics on the
  same grounds M4 established (reach = ball; the polytope never binds; A3′ C2's
  flat isotropic c). Caveat 1 below states this against interest.

**(ii) The construction.** For v ≠ 0 the data {τ̂, ê_motion} spans exactly one
2-plane: **Π = span(τ̂, ê_motion) = span(τ̂, Δ)** — the plane the obligatory
per-Moment displacement lies in. No coefficient, no choice, no menu: Π is the span
of the data itself.

**(iii) Uniqueness: enumeration over ALL subspaces.** Definition (the standing
meaning of "postulate-distinguished, not chosen by hand," with corpus precedent in
the equivariance-at-construction condition of METH-CHIR-CONT-2, methods catalogue,
chirality sector, pre-target): a subspace is postulate-distinguished iff it is
(a) constructible from the inventory in (i) and postulate scalars alone, and
(b) invariant under the stabilizer of the data inside the arena's symmetry group —
otherwise its specification requires structure the postulates do not supply, which
is precisely a hand choice. The stabilizer of {τ̂, ê_motion} is SO(2), rotations
about ê_motion, acting as the identity on Π and as rotation on the spatial
orthocomplement plane P⊥. Under this SO(2), ℝ⁴ = span(τ̂) ⊕ span(ê_motion) ⊕ P⊥ =
trivial ⊕ trivial ⊕ rotation-rep. Enumerating invariant k-planes for EVERY
k ∈ {1, 2, 3} — the dimension is an output, not an input:

- **k = 1:** every line in Π is invariant (SO(2) acts trivially there), and a
  continuum of them is constructible — span(τ̂), span(ê_motion), span(Δ),
  span(c·τ̂ − v·ê_motion), … **No unique distinguished line exists.** (V3)
- **k = 3:** the orthocomplements of that continuum — τ̂⊥, ê_motion⊥, Δ⊥, … **No
  unique distinguished 3-space exists.** (V3)
- **k = 2:** an invariant 2-plane must decompose into invariant summands of the
  rep: it is the trivial² summand Π, or the rotation summand P⊥, or a (line in Π)
  ⊕ (invariant line in P⊥) — and at generic rotation angle P⊥ has no invariant
  lines. **Exactly two invariant 2-planes exist: Π and P⊥.** (V1, V2)

So k = 2 is the unique dimension at which the invariant set is finite — and of the
two members, exactly one contains any of the data: τ̂, ê_motion, Δ ∈ Π; the
P⊥-projection of every datum is identically zero (V6). P⊥ is distinguished only
negatively, as the plane the data avoids (equivalently, as Π's orthocomplement).
**The unique positively-distinguished 2-plane is Π — candidate (a).** Purely
spatial planes through ê_motion, planes containing τ̂ and a transverse direction,
and every other 2-plane fail invariance and are excluded automatically by the
enumeration — the argument never consults the campaign's candidate menu.

**(iv) The v → 0 limit (pre-logged risk zone ii).** At rest, ê_motion is
undefined; the inventory reduces to {τ̂}; the stabilizer grows to the full spatial
SO(3); ℝ⁴ = trivial(τ̂) ⊕ vector(3), and the 3D vector rep is irreducible over ℝ —
**no invariant 2-plane exists at all** (V4; only span(τ̂) at k = 1 and the spatial
3-space at k = 3 survive). The distinguished plane ceases to exist exactly where
the exclusion scale d = v·t_P vanishes: nothing is left needing it. Consistency,
not a patch. (As v → 0⁺ the plane Π depends on the limiting direction of ê_motion
and has no continuous limit — but its physical payload, the exclusion of radius
d = v·t_P → 0, converges to the empty exclusion along every direction sequence;
the directional discontinuity is unobservable. The quantitative version belongs to
M2/M3.)

**(v) Counterfactual (kill-liveness) — the broken branch kept.** The finiteness of
the invariant set — hence the uniqueness — is carried by the arena symmetry being
the CONTINUOUS SO(2). Had the residual symmetry about ê_motion been discrete —
e.g., C₂ = {1, R(π)}, the generic surviving element if the lattice's point-group
orientation participated in displacement kinematics — then R(π) = −1 on P⊥ fixes
every line of P⊥, and the entire two-parameter mixed family (line in Π) ⊕ (line in
P⊥) becomes invariant: a continuum of "distinguished" 2-planes; **uniqueness dies**
(V5, machine-verified). For fully generic ê_motion the discrete stabilizer is
trivial and the invariance constraint evaporates altogether. M1's uniqueness
therefore rides on A3′ C2 + M4's ball verdict — the same load-bearing structure,
and the same failure mode, M4 already put on record. Had the postulates given the
polytope's discrete symmetry to the displacement problem, M1 would have died at
this step. The kill was live. Secondary data counterfactual (qualitative): without
c01's universal τ̂ (per-CP local ticks), Π's second spanning vector does not exist
and no 2-plane containing the drift is constructible at all — M1 fails for want of
data. Verify: `series_relativity/code/2491_m1_plane_uniqueness.py` (stdlib, fixed
seed 2491, V1–V6, ALL PASS).

### K3 / K3′ / K3a log for this step

- **K3 (explicit target invocation):** none. No step invokes n = 2, γ,
  coefficient 1, or (1−f²)². The enumeration runs over all k ∈ {1, 2, 3}; the
  target's dimensionality is compared against only AFTER the enumeration returns
  its answer. CLEAN.
- **K3′ ("would the step have been taken, in that form, by a derivation that did
  not know the target?"):** two load-bearing selections. (1) The distinguishedness
  criterion (constructible + stabilizer-invariant): this is what "not chosen by
  hand" means, and equivariance-imposed-at-construction is corpus method a sector
  away, pre-target (METH-CHIR-CONT-2). A target-ignorant derivation asked "which
  subspaces do the postulates single out for a moving aggregate" formulates
  exactly this and enumerates exactly these reps. (2) The positive/negative
  discrimination between Π and P⊥ by data-containment: the question M1 answers is
  "which plane does the MOTION distinguish," and the motion's entire geometric
  content is Δ; the plane Δ distinguishes is its span (with the universal τ̂), in
  the same sense a vector distinguishes its span and not its orthocomplement.
  Fitting pressure was highest here — the tube wants Π — so the honest fallback is
  logged as caveat 2 rather than argued away. Pre-logged risk zone (i)
  (privileging the drift-spanned plane BECAUSE the tube needs it) is discharged
  structurally: the enumeration ran over the full Grassmannian at every dimension,
  and Π's selection criterion (span of the data) is stated without reference to
  what any exclusion geometry needs. CLEAN, with caveat 2 shipping to the panel.
- **K3a (intermediate-principle launder + n = 3 counterfactual):** no new physical
  principle is posited. Inputs: c01 (τ̂, 2025-era), A3′ C2 (June 2026, GR sector),
  SR-1's τ-orthogonality (Patch-0736 era), M4 and d = v·t_P (this campaign, steps
  1–2, forward), equivariance-at-construction (chirality sector, pre-target).
  Counterfactual test: were the target n = 3 — needing a unique distinguished
  3-space — the identical inventory and enumeration return "k = 3 carries a
  continuum; no unique 3-space exists" and the campaign dies at M1. The reasoning
  cannot bend to an n = 3 target; it would KILL under one. This is the strongest
  form of the test: the same argument is target-lethal under the counterfactual
  target. PASS.

### Caveats logged for the K2 panel (stated against interest)

1. **Lattice-orientation scope (shared with M4's caveat — ships together).** The
   finiteness of the invariant set requires the per-Moment displacement problem to
   carry the arena's continuous isotropy (A3′ C2 + M4), with the GP lattice's
   discrete orientation not participating. If the panel judges the lattice
   orientation postulate-available to displacement kinematics, the stabilizer is
   generically trivial (or C₂), V5's continuum appears, and M1's uniqueness fails
   as derived. This is the same scope question M4 logged, now with a second,
   sharper consequence attached.
2. **Π vs P⊥ orientation.** {Π, P⊥} is one geometric datum (an orthogonal
   splitting). The selection of Π within the pair rests on the positivity
   criterion (the data spans Π and avoids P⊥). If the panel finds that criterion
   insufficiently postulate-grounded, M1 delivers "unique distinguished splitting"
   rather than "unique plane," and the orientation transfers to M2's burden —
   where the exclusion rule's derivation must show the obligatory drift prices
   Π-budget (its own support) and not P⊥-budget. Nothing downstream changes if M2
   carries it; the accounting of where the orientation is established should be
   honest.
3. **Distinguishedness as methodological definition.** The
   constructible-plus-invariant criterion is the standing corpus meaning of "no
   hand choice" (METH-CHIR-CONT-2 precedent) but is itself a methodological
   definition, not an axiom. Recorded so the panel may reject or sharpen it.

### Interlocks noted forward (pre-logged risk zone iii)

- **M2:** the stabilizer machinery transfers directly — any postulate-derived
  exclusion region must be SO(2)-invariant about ê_motion, which is exactly M2's
  "full symmetric neighborhood, not a half, sector, or weighted variant"
  requirement. M2 should derive the rule and then check SO(2)-invariance as a
  consistency output, not impose it.
- **M3(ii)/(iv):** τ̂ ∈ Π by construction; SR-1's τ-invariance decomposition
  (R²₄D = r²₃D + τ²) applies with Π ∩ τ̂⊥ = span(ê_motion), so the 4D→3D
  projection of the Π-projection condition is the object M3(iv) must track — the
  projection treatment must preserve d = v·t_P. Nothing here prejudges it.
- **M7:** the derivation used zero internal structure — inventory (i) is
  aggregate-independent by construction, which is the backbone the ratified §3a
  rationale anticipated. M7's residual burden is that the EXCLUSION RULE (M2/M6)
  also uses none.

### Step outcome

M1 **PASSED at session level, subject to K2** (nothing promoted; the eventual
mechanism claim carries this step's caveats in the panel package). Next per the
burden: **M2 — the exclusion rule** (forbidden targets are exactly those whose
projection onto the distinguished pair is ≤ d, full symmetric neighborhood,
derived from single-CP rules — interlocking with M6's micro-to-macro bridge).

---

## Step 4 — M2: the exclusion rule (Patch 2492)

### Verdict

**M2 IS NOT DERIVED — and this session records that the failure is structural,
not merely effort-bounded: the exclusion rule is UNDERDETERMINED BY THE CURRENT
CORPUS.** The candidate rules for how the obligatory drift interacts with the
per-Moment capacity set were enumerated forward; one available forward filter
(rest-limit continuity) kills two of six; the four survivors — including the
tube — are pairwise inequivalent at leading order and the postulates, as
currently developed, do not discriminate among them. The discriminating input is
the per-Moment, single-CP content of the motion state — i.e., **the SF-6 inertia
mechanism, which is an explicitly unpinned, registered open investigation**
(founder-directed, Patch 2470, handover 2026-07-14: "the SF-6 inertia
coefficient is not pinned from anything yet (the mechanism was documented 'on
the road to DM' and set aside)"). The SR registry independently flags this
coupling as the recommended route (OPEN-SR-EPSILON: "couples to the DM/SF-6
sector with an independent normalisation… OPEN-SR-EPSILON and the DM campaign
become the same problem"). Per the campaign's own discipline, the disposition —
K1 NEGATIVE now versus explicit founder extension pending the SF-6 isolated
investigation — is NOT this session's to adjudicate. The fork is pinned
(`code/2492_m2_rule_fork.py`, W1–W3 ALL PASS) and ships to founder + panel.

### What M2 requires, decomposed

The rule to derive: forbidden targets are exactly {x : |P_Π x| ≤ d}, the full
symmetric codim-2 tube. Decomposed into its three independent features, each
needing forward grounds: **(i) a floor** (the in-plane commitment is ≥ d, not
= the drift vector); **(ii) on the magnitude of the Π-projection** (not the
ê_motion component); **(iii) Π-plane isotropic** (symmetric between τ̂ and
ê_motion — noting NO postulate symmetry rotates τ̂ into space; c01 makes τ̂
absolutely distinguished, so (iii) cannot come from any stabilizer argument).

### The candidate-rule enumeration (forward; target never consulted for selection)

For a single CP whose aggregate is in motion state v, the postulate-available
kinematics are: c01's displacement-response (the step is set by net SSV,
Eq.~(disp)), A3′/M4's reach bound (arena = the ball), M1's distinguished plane,
and the drift d = v·t_P (2489 step (i)). The composition rules these admit:

- **R1 — translation/relabeling.** The drift is bookkeeping inside the one
  computed displacement; the admissible target set is unchanged. V_free/V₀ = 1;
  ε = 0. This is what reach + displacement-response give with NO further
  principle: the strongest honest statement of the current postulates' default.
- **R2 — vector reach consumption (lens).** The drift consumes reach
  vectorially and the discretionary part carries its own full-reach bound:
  capacity = Ball ∩ (Ball + d·ê_motion). V_free/V₀ = 1 − (8/3π)f + O(f³);
  n = 1. The double-bound premise has no corpus source.
- **R3h — component floor (half-space).** The ê_motion component cannot fall
  below the drift: free iff x₁ ≥ d. **KILLED FORWARD** by the rest-limit
  filter: V_free/V₀ → 1/2 (not 1) as v → 0⁺, a discontinuity in ε at rest,
  inconsistent with c01's displacement-response being continuous in net SSV (an
  infinitesimally moving aggregate is an infinitesimally perturbed Sea state).
- **R3s — exact-advance slice** (the corpus's one established per-Moment
  obligation template, c01's τ-advance, transferred to the drift): x₁ = d
  exactly. Free set has measure zero; ε → ∞ for any v > 0. **KILLED FORWARD**
  by the same filter. Notable finding: the corpus's own obligation template
  does NOT produce the tube — it produces a slice, and the slice dies.
- **R3y — symmetrized component slab** (codim-1; E₁ of the 2482 family):
  forbidden iff |x₁| ≤ d. V_free/V₀ = 1 − (16/3π)f + O(f³); n = 1. Survives
  the filter. No forward source for the symmetrization found.
- **R4 — in-plane magnitude floor** (codim-2 tube; E₂; the identity's rule):
  forbidden iff |P_Π x| ≤ d. V_free/V₀ = (1−f²)² exactly; n = 2. Survives the
  filter. Feature (iii) has a PARTIAL pre-target anchor — SR-1's budget metric
  is round in all four coordinates (the strain variable is the 4D radius,
  R² = r² + τ²), so a rule stated at budget level would inherit Π-roundness —
  but features (i) and (ii) have **no forward source found**, in c01, SR-1's
  corrected text, A3′, or anywhere in the pre-target corpus.

**The corpus sweep (recorded so the panel can audit exhaustion):** c01's
"displacement step set by net SSV" is a response rule, not an obligation
structure for a persisting motion state; a momentum/dressed-state per-Moment
mechanism does not exist in the corpus (grep across series_relativity/ and
series_quantum/ returns nothing); SR-1's "bulk velocity consumes part of the
displacement budget" (line 768) is the assertion the 2471–2475 triage withdrew
— SR-1's corrected text itself registers the derivation as owed (line 337) —
so it cannot serve as a premise without circularity; OPEN-SR-EPSILON's own
registry entry routes the missing normalisation through the SF-6 coupling; and
the SF-6 inertia mechanism is unpinned by explicit founder ruling as of 14 July
(Patch 2470), with the isolated impulse-transfer investigation opened and
unstarted. The convergence is exact: **the input M2 needs is the deliverable of
a registered open investigation.**

### Why the session does not select R4 (the K3′ record)

Every route constructed toward features (i)+(ii) passed through a step whose
only distinguishing virtue was that it produces the tube — the precise K3′
profile ("structures whose only distinguishing virtue is target-consistency").
Three such routes were drafted and abandoned, recorded verbatim in
`reasoning/2492.md`: (1) a dressed-state/polaron narrative ("the state's
per-Moment reproduction consumes in-plane capacity isotropically") — its
Π-isotropic magnitude-floor form has no source other than yielding the tube,
and the dressed-state per-Moment mechanics is exactly the unpinned SF-6
content; (2) treating the burden text's own wording ("full symmetric
neighborhood") as a premise — the burden was panel-designed AFTER the target
was known (campaign §1c); it describes what must be derived and cannot ground
the derivation; (3) leaning the budget-metric roundness into more than it
carries — it grounds (iii) only, and was demoted accordingly. Per the
handover's binding instruction ("if the honest answer is ever 'this step
exists because the target needs it,' that is K1 firing early — take the
kill"), the session declines to select.

### K3 / K3′ / K3a log for this step

- **K3:** the target is never used to select. The finding "only R4 reproduces
  γ" is computed and stated AFTER the enumeration and filter (script output,
  labeled as such). The step's verdict exists BECAUSE K3 discipline was
  enforced, not despite it. CLEAN.
- **K3′:** three near-misses caught live and recorded (above and verbatim in
  the reasoning fragment). The rest-limit filter itself passes the test: a
  target-ignorant derivation checking any candidate rule's physical sanity
  applies the v → 0 limit first (M1's step (iv) had already established the
  structure dies at rest), and the filter kills candidates on both sides of
  the exponent ledger indiscriminately (it kills the slice, which would have
  given no identity, and the half-space, whose exponent class n = 1 is shared
  by a survivor). CLEAN.
- **K3a:** no new principle is posited — the step's content is precisely the
  REFUSAL to posit one. The rest-limit continuity filter is grounded in c01's
  displacement-response continuity in net SSV, not posited fresh. n = 3
  counterfactual: the identical enumeration, sweep, and filter yield the
  identical four-way underdetermination — under ANY target the reasoning
  returns "the corpus does not discriminate"; it cannot bend because it
  selects nothing. PASS.
- **K4:** untouched — the fork is a RULE fork within the committed candidate
  (a); no alternative plane candidate was constructed or tested. **M5:** no
  constant was absorbed (nothing was derived).

### Disposition — stated against interest in BOTH directions

- **Against the campaign:** K1's default effort bound is two focused sessions;
  this is session 2; the burden is not met and will not be met this session.
  "Blocked-on-open-item" must not become a device for indefinitely deferring a
  registered kill — the panel should weigh whether the SF-6 dependency was
  foreseeable at pre-registration (§2a condition 6 and OPEN-SR-EPSILON's
  registry text suggest the sector coupling was already visible).
- **Against the kill:** recording NEGATIVE-FOR-MECHANISM now would encode "the
  postulates do not select the exclusion rule" when the demonstrated state is
  "the corpus has not yet derived what the postulates select" — a negative
  carrying a known, in-flight confound: the SF-6 isolated investigation
  (opened for independent reasons, founder-directed, one day before this step)
  has as its deliverable exactly M2's missing input. K1's own text makes the
  effort bound founder-adjustable ("founder may extend explicitly").
- **The session adjudicates neither.** Per the 2489 precedent (a session must
  not lawyer its own kill conditions — in either direction), the fork, the
  sweep, and both framings ship to the founder and the K2 panel. The two
  clean options on the table: **(α)** K1 fires — campaign closes
  NEGATIVE-FOR-MECHANISM, H.1's successor graduates to the four-model
  Proposition per the registered kill branch; **(β)** founder explicitly
  extends/suspends the campaign PENDING the SF-6 isolated investigation, whose
  result then discriminates the pinned fork {R1, R2, R3y, R4} — with the
  explicit pre-commitment that if SF-6's mechanism lands on R1/R2/R3y (or on
  nothing), K1 fires with no further extension. Option (β), if taken, should
  itself be pre-registered before SF-6 work resumes, so the inertia
  investigation cannot be steered toward R4 (the SF-6 window was opened
  blind to this fork — that independence is an asset to preserve; the fork
  should NOT be shown to the SF-6 working instance, only to the panel).

### Effect on the remaining burden

M3, M6, M7, M8 are downstream of the rule (there is no projection treatment,
bridge, universality proof, or frame-consistency check FOR a rule that has not
been derived); M5 is a standing ban, not a work item. **Mechanism derivation
work on this campaign STOPS at this step** pending the founder/panel
disposition. Working M3+ "conditionally on R4" would evaluate the target rule's
consequences without a derivation — geometry the 2482 identity already
supplies — and would add fitting surface while the rule is underivable. Not
done.

### Step outcome

M2 **NOT DERIVED — UNDERDETERMINED; FORK PINNED
(`code/2492_m2_rule_fork.py`, seed 2492, W1–W3 ALL PASS); DISPOSITION TO
FOUNDER + PANEL (options α/β above).** The session's mechanism phase closes
here. Assets for the dispatch: this entry, the campaign file, the fork script,
`reasoning/2492.md`, and the SF-6 handover cross-reference
(`handovers/2026-07-14_sf6_inertia_impulse_investigation_opened.md`).

---

*(Session 2 of the K1 clock ends at this step; handover to follow on founder
instruction.)*

