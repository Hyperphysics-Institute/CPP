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

*(M9 entry to follow as the session's step 2.)*
