# HANDOVER — 15 July 2026 — SR-1 triaged, H.1 broken, prediction audit opened

**Patches this session:** 2471 → 2475 (all pushed; 2475 pending founder push at time of writing).
**Warm keyword:** `AUDIT-WARM-2476`. **Next patch:** 2476.
**Supersedes:** `2026-07-14_sf6_inertia_impulse_investigation_opened.md` (Patch 2470).

---

## READ THIS FIRST — the session went somewhere the keyword does not describe

This session opened on **SF6-WARM-2470**: an isolated SF-6 inertia impulse-transfer
investigation, to give the DM dance a momentum store. **Do not resume that.** It is not
wrong, but it is now blocked behind, and downstream of, what follows.

**Trace of the drift** (recorded because the route is the lesson): SF-6 EM mechanism
playback → founder correction (store tracks *velocity*, not acceleration) → classical
electromagnetic-mass anchor → neutral-mass problem → founder supplies SSV_abs
(per-CP unconditional emission) → missing source clause in A3′ (C0) → required reading
SR-1 §Grid Resolution → surfaced `k` → surfaced α_geom → **SR-1's flagship billing
collapsed.**

Nothing pointed here. It was found by walking past it.

---

## WHAT CHANGED (SR-1)

**k is a normalisation convention, not a prediction.** α cancels identically in
k·ΔSSV for *any* α (verified, `code/2471_*.py`, 31/31). App. A.5 Step 3's "dimensional
analysis forces prefactor identically 1" is invalid and withdrawn — dimensional analysis
fixes dimensions, never a dimensionless prefactor — as are two further instances in App. E.
The March-2026 remedy (adopt α_geom = 0.5594) is **REJECTED**: α_geom is unit-dependent
(0.5594/circumradius vs **0.2444/l_P**), a defect its own script printed and walked past.

**γ is an INPUT.** App. A.8.1 *defines* ΔSSV ∝ (γ_SR−1)mc²/V. Exact Lorentz equivalence
follows by construction. Conceded in abstract, plain-language summary, conclusion.

**SR-1 has ZERO falsifiable predictions.** γ_CPP = γ_SR is an identity; an identity admits
no deviation. The claimed deviation δt′/t′ ≈ k·ΔSSV **is** γ_SR−1 — double-counted. Every
ΔSSV definition is velocity-dependent; all five predictions scaled with *acceleration*;
no derivation bridges them. δ ~ 10⁻²⁰ ⇒ v ≈ 4 cm/s, unrelated to 10²⁰g. All withdrawn,
plus the muon bound (void twice: bounds a convention AND a forbidden deviation).

**H.1 IS FALSE AS STATED.** Cap expansion published f^{1/2}; **correct f^{5/2}** (measured
exponent 2.4999999990; the published formula is off by 20 orders of magnitude at f=10⁻¹⁰).
The theorem's claim (n ≤ 1 ∀ models) is **refuted by its own Model 3** (n = 5/2), and its
proof's premise *was* the arithmetic error. Demoted to a three-model Proposition.

**Four fabricated Monte-Carlo citations withdrawn.** Both repo MC files are stubs
(`vertices = []`; loop is `pass`); quoted figures were hard-coded comments; one contains
*"For brevity **in this response**…"* — AI chat output committed as code and cited in a
shipped paper. Replaced with `code/2471_*.py` (stdlib only, runs anywhere).

---

## THE PRIORITY QUEUE (my read; founder decides)

**1. `OPEN-WORKFLOW-PREDICTION-AUDIT` — CRITICAL.** The registry lists ~28 zero-parameter
predictions; the √N null-hypothesis-raise rests on them being independent and genuinely
parameter-free. **k was neither, for four months.** *And it must now cover THEOREMS too* —
H.1 was the result I personally nominated as most secure, and it was false. A proof is an
artifact; an unverified proof is a stub. Everything else is contingent on this answer.

**2. The gate (`publication_audit.sh`)** — precondition for (1). FAIL on: a cited script
that is absent / non-executable / imports outside stdlib without declaring it / generates
its test data from the quantity it fits (circularity); elision markers ("for brevity",
"full version in repo"); any prefactor computed → absorbed → billed as derived; any
frontier status contradicting a paper claim.

**3. Blast radius — 14 artifacts cite SR-1's k / PSR formula** (c01, c02, c03, c05, c07,
c08, c09, c12, c14 + early-universe reasoning). Do they inherit the withdrawn billing?
Bounded and mechanical. **Hazard:** (k, ΔSSV) must be inherited as a **matched pair** —
mixing conventions rescales γ−1 by exactly α (44%).

**4. `OPEN-SR-H1-CLASS` — HIGH, and the only thing here that could be good news.** The
corrected exponents **bracket** the target (1 < 2 < 5/2). Nothing excludes an exclusion
geometry with V_excl ∝ f², which by V ∝ r⁴ gives ε ∝ f² = γ_SR−1 exactly. *The erroneous
theorem was closing a route that may be open.*
> **G7 WARNING, read before touching this.** A region reverse-engineered to give f² is
> **fitting, not deriving**. The motivation must be independent of the target exponent.
> The pull toward "find the f² geometry and win the flagship back" is *precisely* the
> pressure that produced the k defect. If you attack this, pre-register the kill condition.

**5. `OPEN-SR-EPSILON` — CRITICAL, the real physics.** Derive ε(v) from substrate dynamics
without importing γ_SR. (4) is its cheapest attack route.

**6. SF-6 / DM (the original window).** Downstream of (5): the dance needs a momentum
store, the store is ΔSSV, and ΔSSV's operational definition is exactly what's missing.
**Note the convergence:** three CONV-001 reviewers independently said α becomes *physical*
if ΔSSV couples to another sector with an independent normalisation — one named the DM
campaign specifically. The original window is where OPEN-SR-EPSILON becomes answerable.

---

## FOUNDER ACTIONS OUTSTANDING

- **OSF re-deposit / retraction** — the deposit claims five predictions and a
  first-principles derivation. Both gone. Founder said he would post the retraction.
  It should **not** yet say "but the elimination theorem stands" — H.1 is demoted pending
  `OPEN-SR-H1-CLASS`.
- Push 2475 if not already pushed.

---

## STILL UNAUDITED (flagged, not fixed)

- **Appendix G** (d=4 dimensionality theorem). Billed as *"the deepest level of
  first-principles derivation currently achieved within CPP"*, derived from postulates that
  **include exact Lorentz covariance** — which this paper now concedes is imported. Scope
  note added at 2474; **the theorem itself has not been checked.**
- App. E's Casimir (l_P/d)⁴ — retained as conditional; needs an independent 4D
  spectral-measure derivation before it can be a prediction.
- `development/lattice-derived_coupling_constant_k.md` and
  `development/k_prefactor_resolution.md` — two *prior* attempts at the k problem, both
  unrouted. Names embed the retracted claim.

## C0 / A3′ — PARKED, NOT DEAD

The session's original axiom finding still stands and was never patched: **A3′ has no
source clause for Φ.** Superseded A3 read *"DI-bits propagate **between CPs**"*; the A3→A3′
consolidation relocated the transaction to GP↔GP and lost the source. C4 already
presupposes it (*"the CP momentum flux it already registers"*). Founder-approved draft
clause (C0: per-CP unconditional DI-bit emission; Φ = Σ|·| unsigned, V_i = Σ signed) is in
this session's transcript and should be recovered before it is lost. Also: DI-bit has
**three live expansions** in the corpus ("Displacement Increment" canonical, "Digital
Information bit", "Direction Information bit") — a PCD-class drift.

---

## THE THING THE NEXT INSTANCE SHOULD INTERNALISE

Five defects this session, every one found by **verifying rather than reading**, every one
already sitting in the corpus, every one invisible at read-time: η's scope, the shell
scale, two extra instances of a withdrawn argument, the prediction double-counting, and
H.1. Fixing H.1's billing alone took **eight passes** — I corrected the instance in front
of me and the claim survived elsewhere every time, including in text I had written one
patch earlier. `git diff --check` — a whitespace linter — caught two that my own
claim-level audit missed.

**Grep the claim, not the wording. Verify the artifact, don't read it. And assume the
important finding is off-plan** — it was, four times out of four.
