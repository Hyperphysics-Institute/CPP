# R2 / Step 1 — Lattice-EM Action Attempt: A Negative Result (Not Tasted)

**Patch:** 2011 (21 June 2026) · **Window:** 2000-band · **Work item:** OPEN-COSMO-DM-2 residual R2
**Status of result:** **NEGATIVE / BLOCKED. Attempting the full lattice-EM action (ChatGPT closure
condition #2, the c06 owed computation) without tasting does NOT close R2 — it shows that a
straightforward construction fails to reproduce the established heuristics, and that the real closure is
blocked on a deeper missing piece: the c06 EM-*emergence* mechanism. The 2002/2008 geometric-Z₀ result is
revealed to be a heuristic the correct action must still be shown to reproduce — which a naive action does
not. R2's full PASS is genuinely owed to physics not yet specified at the needed level. This is reported as
a negative result rather than a closure, by design.**
**Verify:** `scripts/2011_lattice_action_attempt.py`
**Discipline:** worker patch; owned path `mu_eps_closure/lattice_action/`; no shared-registry/c06 edit.

---

## 1. The task and the constraint

Thomas: take R2 the rest of the way — the c06 full lattice-EM action, then the screening bound, then
round-3 review, in order, **and not by tasting.** Step 1 is the field-theory derivation ChatGPT named as
the closure condition: write `L = ½C P² + ½K(∇×P)²` with both coefficients from one microscopic action and
show whether K inherits C's SSV-dependence in the field theory (not just the pair potential).

The non-negotiable: build the action from corpus-grounded terms only, integrate out, and report whatever
the result is — including a failure.

## 2. The construction (every term justified, none tuned)

`L = ½ μ_DP (∂_t u)² − ½ C u² − ½ K a² (∇u)² + q u·E`, with the DP inertia μ_DP = C/ω_ZBW² (ω_ZBW fixed,
c02), the on-site stiffness C = Q·g_C and inter-site coupling K = Q·g_K both Coulomb-derived (2008), and
the polarization P = nqu coupling to the field. Integrate out u → ε₀ (on-site polarizability), identify the
propagating transverse mode → c, then μ₀ = 1/(ε₀c²) and Z₀ = √(μ₀/ε₀).

## 3. What it actually gives (the negative result)

- **Stiffness channel (vary Q ⇒ C, K scale together):** `Z₀ ∝ Q` (the explicit stiffness does **not**
  cancel — Z₀ runs 2.08 → 16.68 across an 8× Q sweep), **and** `c` is geometric (does not move). So this
  construction reproduces **neither** the 2002/2008 geometric-Z₀ **nor** the VSL c-variation.
- **Kinematic PSR channel (vary the stepping rate, the actual 0738 VSL):** `c` moves (good — this is the
  VSL), but in this construction the PSR enters only μ₀ (propagation), not ε₀ (static polarizability), so
  `Z₀ ∝ 1/c → A = −1 → FAIL`.

Both channels are wrong, and that is the signal. **A DP-lattice acoustic mode is a phonon, not the photon.**
The naive "photon = transverse acoustic mode of the DP lattice" mis-identifies the EM emergence, which is
why it reproduces neither established result. The pair-potential/virial cancellation (2002/2008) does **not**
survive into this action — exactly the failure mode ChatGPT warned of ("cancellations can vanish in the
field theory").

## 4. The honest diagnosis and consequence

This does **not** mean 2002/2008 are wrong — it means they are **heuristics** (virial energy-equality;
pair-potential curvature ratio) that a *correct* action must be shown to reproduce, and a naive action does
not. The missing piece is deeper than the stiffness ratio (2008) or the scale-dependent screening (ChatGPT
#1): it is **the c06 EM-emergence mechanism itself** —

> how a *gapless photon* (not a phonon) emerges from the DP Sea; how its c varies (the VSL channel — and
> whether that channel is the stiffness C, the bare Coulomb coupling, or the kinematic PSR); and whether
> that channel enters ε₀ and μ₀ *symmetrically* (→ A=0 PASS) or asymmetrically (→ A≠0 FAIL).

Until that emergence construction exists, the action-level curl-coefficient cannot be derived correctly,
and the geometric-Z₀ heuristic cannot be confirmed (or refuted) at the level R2's PASS requires.

## 5. Effect on the R2 residual ledger (honest, including a deepening)

- **Leading-order K∝C (panel-CONFIRMed, 2008/2009):** stands — it is a statement about the stiffness
  *ratio*, and is not touched by this.
- **Action-level geometric-Z₀ (the actual R2 PASS criterion):** now explicitly **UNCONFIRMED** — a naive
  action does not reproduce it. This is a deepening, not a closure: the residual is no longer just
  "screening + curl coefficient" but **"the EM-emergence mechanism that fixes the VSL channel and its
  ε₀/μ₀ symmetry."**
- **Net R2 status:** still REVISE, with the residual correctly relocated to the EM-emergence construction.
  Steps 2 (screening bound) and 3 (round-3 review) of the requested plan are **not reachable yet** — they
  presuppose step 1 (the action), which is blocked on the emergence mechanism. I did not fake past this.

## 6. The actual prerequisite (what the next window genuinely needs)

R2's full closure requires the c06 **EM-emergence** derivation — the gapless-photon construction from the
DP Sea, with the VSL channel identified and its ε₀/μ₀ symmetry settled. That is a substantial physics task
requiring corpus microphysics not specified at the needed level (the c06 paper has the field-strength
*math*, B=∇×P, but not the emergence dynamics that fix Z₀'s channel behavior). It is the right next target,
and it is genuinely upstream of the screening bound and the panel re-review.

**HONEST BOTTOM LINE:** "take R2 the rest of the way" was attempted in earnest and **did not close it.** The
untasted attempt found the real blocker instead — and that is the correct, integrity-preserving outcome:
R2 remains a REVISE-level conditional PASS whose full closure is owed to the c06 EM-emergence construction,
not to me tuning a lattice now.

NO THEO (negative result + residual relocation; no new axiom/term/counted prediction).
