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

*(M1 entry to follow as the session's step 3.)*

