# SS-1f v0.1 → v0.2 — panel review cycle synthesis

**Panel:** ChatGPT, Grok, Gemini, Copilot (same panel as SF-5). Submitted via CONV-001. Reviewed against four asked criteria: (1) Prop 6.1 soundness; (2) honesty-box scope; (3) internal coherence vs SS-1b/1c; (4) open-problem + §7-seam registration.

## Verdict tally
- **Grok — SHIP as v1.0.** No reconciliation required pre-ship; seam already correctly registered as open. Note is tight, honest, does its job. Only minor notes (hop target-vertex is a sketch = the registered forcing problem; one clarifying sentence on the "eight modes" origin would help a fresh reader).
- **Copilot — conditionally SHIP as v1.0.** Conditions: in §6 either make the algebra check explicit (commutators/trace/closure) AND soften "iff", or label Prop 6.1 a mechanism-level conjecture; add one sentence on not-yet-matching full QCD dynamics. (Reviewed conceptually — could not load raw source.)
- **ChatGPT — reconcile §7 seam before SHIP, "but only because the note's own framing makes that seam load-bearing; otherwise close to v1.0."** Two surgical edits: (a) scope the "iff" to the C^3/vertex-occupancy ansatz (not a general-math claim); (b) distinguish the abstract 8-mode torus from diagonal operators on C^3 (where the diagonal algebra is ≤3-dim, 2-dim traceless). Soften "supply a physical realisation" → "candidate ... pending §7". Register the sub-problem: define what E_ij acts on (internal colour coord / baryon-vertex occupancy / quotient).
- **Gemini — reconcile §7 seam before SHIP (hard line).** Argues the seam is a geometric contradiction, not a reconciliation: per-quark cage = 3×4 = 12 vertices, hop intra-quark; baryon hTetra = 4 vertices, hop = inter-quark swap. The SSV gradient cannot be computed without fixing the geometry. Also: Prop 6.1 is a correct-but-trivial guardrail; the SSV→f^abc justification is "painted on", not derived.

**Net: 2 ship / 2 reconcile-seam — but the split is narrower than it looks.** The two "reconcile" votes reduce substantially: ChatGPT's is "make two surgical edits + register the operator-domain sub-problem," not "solve the geometry"; only Gemini holds the hard line that the geometry must be *resolved* before any ship.

## Convergence (acted on in v0.2)
1. **Prop 6.1 "iff" scoped** to the vertex-occupancy realisation, with a new Remark (rem:iff) stating it is not a basis-independent uniqueness claim. [ChatGPT + Copilot]
2. **C^3 diagonal-count fixed:** statement + proof now note that C^3 has only two traceless diagonal d.o.f., so the 8-fold torus is for *abstract* modes only; on the colour space ≤2 generators are diagonal and the six colour-changing ones are forced off-diagonal. [ChatGPT — the sharpest catch]
3. **§1 "physical realisation" → "candidate ... pending the §7 frame map."** [ChatGPT]
4. **§7 seam sharpened** to the explicit "what does E_ij act on?" sub-problem (internal colour coord / baryon-vertex occupancy / quotient), with an explicit labelling-vs-dynamics split: the *labelling* coincidence (colour ↔ vertex for a singlet) is all the algebra-level claim needs; the *dynamical* geometry is part of the open forcing problem. This directly answers Gemini's objection by locating the geometric fixing inside op:strong_primitive rather than denying it. [ChatGPT + Gemini]
5. **New Open Problem 9.4 — connection to SS-1d dynamics** (running/confinement/positive beta): the note is kinematic only; reproducing or coexisting with SS-1d's dynamical results is an open consistency check. [Copilot]

## The one remaining fork (TLA to decide)
After the v0.2 edits, the converged math/scope objections are addressed and 3/4 reviewers ship. The single open decision is Gemini's editorial bar:

- **Option A — SHIP as v1.0 (open-problem note).** Rationale: the note is a mechanism note whose stated purpose includes posing op:strong_primitive sharply; the seam is now registered with maximal precision (the operator-domain sub-problem) and its dynamical content explicitly placed inside the open forcing problem. Grok, Copilot, and ChatGPT (post-edit) all reach a v1.0 here. The algebra-level claim depends only on the labelling coincidence, which is sound.
- **Option B — HOLD; resolve the cage-vs-hTetra geometry first.** Rationale: Gemini's standard — a mechanism note should not leave the fundamental geometry ambiguous, since the SSV-gradient mechanism has definite physical content only once the geometry is fixed. This is a legitimate bar; resolving it (deciding intra-quark vs baryon-level, or proving the quotient) is the next research step *regardless* of the ship decision, because it is the core of op:strong_primitive on the mechanism side.

**Recommendation (Opus):** Option A — ship the v0.2-revised note as v1.0, because resolving the seam is itself the research programme (op:strong_primitive), not a v0.1 deliverable, and the note's value is precisely in posing it sharply; the labelling/dynamics split now makes that honest. But Option B is defensible and the seam-resolution is the next target either way — so the choice is genuinely TLA's editorial call, not a correctness question.

**Ship gate either way:** the §7 frame map (operator-domain question) is the gate the proposal already named; v0.2 registers it precisely. SHIP would also trigger the deferred shared-registry integration (theorem-registry, paper_catalog, predictions, frontier_sectors, research_frontier).
