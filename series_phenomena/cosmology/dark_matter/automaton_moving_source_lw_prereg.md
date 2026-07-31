# PRE-REGISTRATION — AUTOMATON MOVING-SOURCE TEST (LW DISCRIMINANT)

**Patch 2885. Written and committed BEFORE execution. The git history is
the evidence: this file's commit precedes the execution commit, and any
reader may verify the ordering with `git log --follow`.**

**Why pre-registration matters more than usual here.** The worker has a
stake in the outcome. CONJ-FP-1's Condition B requires the relay to be
**non-LW**, and the worker has already stated an expectation (below) that
it will be. **Bands are frozen here so that the expectation cannot be
retrofitted to the result.**

---

## §1 — THE QUESTION

CONJ-FP-1 Condition B: does CPP's relay reproduce **Liénard–Wiechert**
structure — a field pointing at the source's **instantaneous** position —
or does it retain **retarded** structure, pointing at where the source
**was**?

**Why it matters beyond the conjecture** (Patch 2884 escalation): if the
relay is LW-like, the Sea exerts no net axial drive on a coasting CP, so
SSV_net = 0, and the primitive d = (|SSV_net|/SSV_abs)·PSR gives **d = 0.
Nothing could coast.** This is a substrate-viability test, not merely an
inertia test.

**What the AUTOMATON has and has NOT established.** The arc measured the
**static** Coulomb profile to ±0.4% pointwise under two independent relays
(Patch 2802 G1). **It has never run a moving source.** Static Coulomb does
not imply Liénard–Wiechert; the programme has been treating the relay's
dynamics as settled by a statics measurement.

## §2 — ENGINE AND ITS SEMANTICS (established by inspection, Patch 2885)

`series_phenomena/cosmology/dark_matter/code/2802_automaton2_engine.py`,
the committed AUTOMATON-2 engine used for the ratified G1 gate.

Update rule, verbatim from `moment()`:

    pay   = Q + inj
    Q_new = pay ⊛ K            (K = R-hop directed outward front kernel)

with directional components Vx, Vy, Vz returned as `pay ⊛ u_{x,y,z}`.

**Two properties fixed by inspection before any run:**

1. **The field carries propagation memory.** Q_old is re-convolved each
   Moment rather than recomputed from the current source position, so the
   field is genuinely retarded rather than instantaneous-action.
2. **The update is FIRST ORDER in time.** It is a transport/relay update,
   **not** a second-order wave equation. **The LW cancellation is a
   property of second-order wave dynamics.**

**WORKER EXPECTATION, DECLARED IN ADVANCE:** on (2), the worker expects
the relay to test **NON-LW**, i.e. Condition B to HOLD. **This is stated
so that a confirming result is weaker evidence than a disconfirming one,
and so that the bands below cannot be adjusted after the fact.**

## §3 — OBSERVABLE AND DISCRIMINANT

A source is advected at constant velocity along **+x** through the
periodic lattice, with a uniform neutralising background so totals remain
bounded. After a declared equilibration, the directional field
(Vx, Vy, Vz) is read at off-axis test points.

At a test point **P** = (p_x, p_⊥), the field direction **û** is taken from
the returned directional components. Its **aim point** is the intercept of
the line through **P** along −**û** with the axis of motion:

    x_aim = p_x − p_⊥ · (u_x / u_⊥)

**Discriminant**, with x_src the source's position at read time, r the
source–test separation, and β = v/c_lat (c_lat = R hops per Moment):

> **A ≡ (x_aim − x_src) / (β · r)**

- **LW structure** ⟹ the field points at the instantaneous position ⟹
  x_aim = x_src ⟹ **A → 0**.
- **Fully retarded structure** ⟹ the field points at the position the
  source occupied one light-transit ago ⟹ x_aim − x_src ≈ −β·r ⟹
  **A → −1**.

## §4 — FROZEN BANDS (declared before execution)

| outcome | criterion | consequence |
|---|---|---|
| **LW-LIKE** | \|A\| < 0.15 at **every** tested β, at ≥ 2 of 3 radii | **Condition B FAILS.** CONJ-FP-1's mechanism yields no drive; and per §1, coasting is impossible in the substrate as currently specified. **This would be a major negative result for the programme, not merely for the conjecture.** |
| **RETARDED / NON-LW** | A < −0.50 at every tested β, at ≥ 2 of 3 radii, and monotone in neither direction required | **Condition B HOLDS.** The mechanism survives; sign (Condition A) becomes the remaining question. |
| **INCONCLUSIVE** | anything else, including sign-inconsistency across radii or β | No verdict. Report as inconclusive and state the obstacle. **An inconclusive result may NOT be reported as support for either side.** |

**Additional frozen requirement — LINEARITY.** A must be **approximately
β-independent** across the tested β (spread < 30% of the mean). A
discriminant that drifts systematically with β indicates the observable is
contaminated by a β-dependent artifact rather than measuring structure,
and forces **INCONCLUSIVE regardless of the value of A.**

## §5 — PARAMETERS (frozen)

- Lattice M = 48 (matching the ratified G1 configuration).
- Hop count R = 4 (the G1 configuration that achieved ±0.4%).
- β ∈ {0.10, 0.20, 0.40} — three values, spanning 4×.
- Test radii r ∈ {4, 6, 8} lattice units; perpendicular offset p_⊥ = r/√2.
- Equilibration: 4M Moments before the source begins moving; read after a
  further 2M Moments of uniform motion.
- Uniform neutralising background at −(source)/M³ per site per Moment.
- Read along both +⊥ and −⊥ and average, to cancel any transverse bias.

## §6 — WHAT EACH OUTCOME OBLIGATES

**If LW-LIKE:** CONJ-FP-1 Condition B fails and the conjecture's mechanism
is dead as stated. **The escalation of Patch 2884 then becomes the live
issue** — the primitive would forbid coasting, and either the primitive,
the relay specification, or the reading of SSV_net must change. **The
worker commits in advance to reporting this outcome as prominently as the
favourable one**, and to registering it as a substrate-level open item
rather than as a conjecture-level failure.

**If RETARDED:** Condition B holds. **This does NOT establish the
mechanism** — Condition A (the sign of the Sea's response) and LINK 2
(the marginality condition) and LINK 3 (stability, B1) all remain open.
**A favourable result here must not be reported as "the mechanism works."**

**If INCONCLUSIVE:** state the obstacle and what would resolve it. Do not
re-band.

## §7 — STANDING

This test bears on CONJ-FP-1 and on substrate viability. **It does not
touch the dark-matter ledger:** 1B OPEN; PR7 PARTIAL; six of seven; B7
holds DM-1/2/3; Candidate (B) 79.5%.
