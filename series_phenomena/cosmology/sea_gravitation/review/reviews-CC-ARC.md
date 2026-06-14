# reviews-CC-ARC — Multi-AI review of the Cosmological Constant arc (package v1.0)

**Cycle:** opened Patch 1165 (package v1.0); responses integrated Patch 1166 (13 June 2026) · **Panel:** ChatGPT + Grok + Copilot · **Arc:** OPEN-SR-5 ≡ OPEN-SM-6
**Outcome in one line:** the arc's honest status (**conditionally supported, not derived**) is **confirmed 3/3**; the event-horizon argument **defeats the particle horizon but does not establish uniqueness** (confirming the 2-ii cap, not flipping it); and the panel surfaced **three actionable new findings** — a cheaper upstream objection (domain fragmentation), a possibly-simpler route (correlation length), and a sharper statement of the open gate (a self-consistency relation) — that **reorder the next step**. No verdict moved; no THEO.

---

## Part 1 — Per-reviewer verdicts (condensed; verbatim verdict lines preserved)

### ChatGPT
- **Q1 (A4 vs particle horizon) — CALIBRATE.** The package "successfully argues **against particle-horizon inevitability**" but "does **not yet derive event-horizon uniqueness**." The vulnerable step is identifying "ongoing mutual reachability" with *future* reachability. Particle horizon = **"live but no longer preferred."**
- **Q2 (gradient→mode reframe) — CONFIRM.** "the cleanest move"; coherence-length language is more natural for ground-state energy than equilibration-length; honestly a reinterpretation, not a strict derivation.
- **Q3 (F-COST-1) — CALIBRATE.** "the deepest remaining issue." The foreknowledge objection is defused, but the real problem is **circularity / self-consistency**: ρ_Λ(today) depends on R_h, R_h depends on the future history → a self-consistency relation must exist. "Many holographic-dark-energy constructions survive precisely because such a self-consistency equation can be written down. The package has not yet shown the corresponding CPP version."
- **Q4 (discharge) — CONFIRM.** D2 is no longer the load-bearing uncertainty; bookkeeping honest.
- **Q5 (the fork) — CALIBRATE.** "A4 or break" slightly overstates. Restate: **"Within currently registered CPP primitives, A4 is the only identified route to a viable R_h-scale coherence boundary"** — not the only *conceivable* non-retarded route.
- **Q6 — CONFIRM** (physical argument, not derivation). **Q7 — NONE FOUND** (no cheaper fatal objection than the coordinable-region problem). **Q8 — CONFIRM** ("conditionally supported, not derived" is exactly right; resist both stronger and weaker — not a "mere fit").
- **Routing: ATTEMPT THE A4 FORMALIZATION.** The gap is sharply localized; no cheaper alternative route bypasses the same issue.

### Grok
- **Q5 — SCRIPT-EXECUTED + INDEPENDENTLY-RECOMPUTED.** Ran a standalone Friedmann integration: Hubble-radius cutoff gives ~constant Ω_Λ / no sustained acceleration (**dead**, Hsu); future-event-horizon cutoff gives w_now ≈ −1.02, q crosses zero at z ≈ 0.6–0.7, Ω_Λ 0.685→1 (**reproduces observed history**, Li). "The code confirms the package claim exactly."
- **Q6 — INDEPENDENTLY-RECOMPUTED, no hidden tuning.** ρ_Λ ~ (1/8π)ρ_P(l_P/L)² follows from the zero-point energy of the longest coherent mode; the identity holds by definition; the ~2× discrepancy is "a genuine prediction, not tuning"; the 1/8π is from field-energy normalization, not fitting.
- **Q1 — INSPECTED + INDEPENDENTLY-RECOMPUTED (strongest position on the panel).** Argues CPP's causal structure **forces** the event horizon: the particle horizon is a *past* boundary fixed by initial data and "does not define *ongoing* mutual reachability"; A4 enforces coherence "now and forward"; "CPP's causal structure (A4 + expanding lattice) *forces* the IR cutoff … to be the future event horizon … the particle-horizon alternative is ruled out on first-principles grounds internal to the axioms." Claims this is "stronger than the package's physical argument."
- **Routing: PROCEED TO THE A4 FORMALIZATION** with the event horizon as target; physical argument robust; no cheaper objection or alternative route surfaced.

### Copilot
- **Headline — RESTATE (structural-calibration).** Coherent as a conditional physical argument; **two structural seams (Q2, Q4)** require tightening before authorizing a deep A4 attempt; **no fatal flaw**.
- **Q1 (calibration) — INSPECTED, no over-claim. Q3 — internally consistent but incomplete.**
- **Q2 (reframe) — PARTIAL, structural gap.** The package "does not yet justify that the CPP Sea's residual ΔSSV *is* a coherence mode rather than a retarded gradient leftover … **the arc assumes the residual is a mode because it *must* be a mode for the event-horizon argument to survive.**" A merge-for-elegance risk unless supported by a substrate-level argument that the Sea ground state is globally defined, adiabatically drifting, with a well-defined IR mode spectrum.
- **Q4 (discharge gap) — YES, one subtle but real gap.** A3′ + the shell-sum prove the **local operator** structure (∇²ΔSSV, degree-0 annihilation) but **not the global uniqueness** of the Sea ground state. Step C/D assume a single global ground state whose residual is the only Λ source; "if the Sea admits multiple metastable uniform configurations or domain structures, the argument breaks."
- **Q5/Q6 — INSPECTED, sound.**
- **Q7 — TWO actionable findings.** (i) **Cheaper objection — domain fragmentation:** a discrete finite-connectivity lattice has no demonstrated mechanism preventing domain formation / long-wavelength topological defects; if the Sea fragments, the IR scale = domain size, "and the arc collapses *before* A4 is even relevant." (ii) **Simpler route — correlation length:** IR scale = the largest scale over which the Sea's ground-state two-point correlation function stays positive (a correlation length ξ); if ξ(t) tracks R_h then ρ_Λ ~ 1/ξ² "without invoking A4" — "more physics-standard than the deep A4 coordinable-region construction."
- **Routing: ROUTE C — pursue the correlation-length route first;** close the Q2/Q4 seams and test the domain-fragmentation kill regardless, before the deep A4 formalization.

## Part 2 — Cross-reviewer synthesis

**Strong convergence (3/3):**
- **Honest status confirmed.** "Conditionally supported, not derived; no theorem; condition (1) discharged; condition (2) on a physical argument" is **exactly calibrated** — neither over- nor under-claimed (ChatGPT Q8, Copilot Q1, Grok implicit). Notably ChatGPT explicitly resists the *weaker* "mere fit" label too: the arc now carries a real A4 rationale.
- **Condition (1) discharge sound** (ChatGPT Q4 CONFIRM, Copilot Q4 "operator side closed", Grok implicit) — *modulo* Copilot's global-uniqueness nuance (below).
- **Magnitude + dynamics clean, no tuning** (Grok SCRIPT-EXECUTED Q5/Q6; Copilot INSPECTED; ChatGPT undisputed). The Hubble-dead / event-horizon-works linchpin is independently reproduced.

**The split that matters — event-horizon *strength* (Q1):** the panel ranges from Grok ("forced, particle horizon ruled out from first principles") through ChatGPT ("particle horizon defeated, but uniqueness *not* derived — step 4 is vulnerable") to Copilot ("internally consistent but incomplete"). **Honest adjudication: side with ChatGPT/Copilot over Grok.** Grok's "forced" is the *same* physical argument asserted more confidently — it does not add the missing step (it neither produces the formal coordinable-region construction nor rules out ChatGPT's "some other global-consistency construction"). So the defensible reading is the one the package already held and 2-ii capped: **the particle horizon is defeated/de-preferred (the arc's real win), but event-horizon *uniqueness* is not established.** The review *confirms* the 2-ii cap rather than flipping it — a healthy outcome.

**The three findings that change the plan (the review's payoff):**
1. **Self-consistency, not foreknowledge (ChatGPT Q3).** The right form of F-COST-1 is a **circularity**: ρ_Λ(t) ← R_h ← future history ← ρ_Λ. HDE survives by writing a self-consistency equation (Li's ODE is exactly this). **So whatever route we take must produce the CPP self-consistency relation** — that is the concrete deliverable, sharper than "derive the boundary."
2. **Global ground-state uniqueness gap (Copilot Q4) + the gradient-vs-mode precondition (Copilot Q2).** These are the **same question** I flagged in 2-ii(a): A3′ closes the *local* operator but not that the Sea is a *single, global, well-defined* ground state with an IR mode spectrum. Until that holds, the (a) reframe ("the residual is a coherence mode") is assumed-because-needed — merge-for-elegance risk. Copilot independently lands on the precondition I named; that convergence is signal.
3. **Domain fragmentation = a cheaper kill, upstream of A4 (Copilot Q7).** If the discrete lattice fragments into domains/defects, the IR scale is the domain size, not R_h, and the arc breaks **before** the A4 question is even reached. This is the cheaper objection the package's Q7 explicitly invited and ChatGPT did not find. It is also the *same* physics as findings 2: "single global coherent ground state, no fragmentation" is one property, and it is the true next gate.
4. **The correlation-length route (Copilot Q7).** IR scale = ground-state correlation length ξ; ρ_Λ ~ 1/ξ². A two-point-function handle, more standard and computable than a "coordinable region," that *may* land ξ on R_h. Honest caveat: it may **relocate** rather than remove the causal-structure question (why ξ → R_h is the same "why R_h"), but a correlation function is a more tractable object, and it could expose the answer (or the domain-fragmentation kill) more cheaply.
5. **Fork de-rated (ChatGPT Q5).** "A4 or break" → "within currently-registered CPP primitives, A4 is the only *identified* route." Copilot's correlation-length proposal is a live demonstration that the space of routes was not exhausted.

## Part 3 — Adjudicated routing

**Panel vote:** 2 (ChatGPT, Grok) → attempt the A4 formalization now; 1 (Copilot) → correlation-length route first. **But the vote is not on equal information:** the two A4-voters did not have Copilot's domain-fragmentation objection in view (ChatGPT explicitly searched for a cheaper objection and found none; Copilot found one). A cheaper kill that fires upstream is a *physics* fact, not a majority question — so the union of findings, not the vote count, governs.

**Adjudicated route: C-then-A, gated on the ground-state-coherence question.**
1. **First, the true next gate (cheapest, and a precondition to everything): is the Sea ground state a single, global, defect-free coherent configuration?** This one question simultaneously (a) tests Copilot's **domain-fragmentation cheaper kill** (Q7 — if it fragments, the arc breaks here, A4 moot), (b) closes the **Q2 reframe precondition** (a single global coherent ground state *is* a coherence mode, licensing 2-ii(a)), and (c) closes the **Q4 global-uniqueness seam** (the discharge needs a unique global ground state). If the Sea fragments → **D-FRAG fires, arc breaks** (clean, cheap negative). If it is single/global/defect-free → all three seams close at once.
2. **Then, the IR-scale derivation via the correlation-length route (Copilot) first**, with the **A4 coordinable-region construction (ChatGPT/Grok) as the fallback** — and require *either* route to produce ChatGPT's **CPP self-consistency relation** (the Li-analog ODE) that lands ξ (or R_h) on the future event horizon. Correlation-length is the cheaper handle; if it reduces back to the causal-structure question, the A4 route is there.
3. The event-horizon **uniqueness** target stands (particle horizon defeated, not the boundary derived); the formalization's job is to *derive* it (or fail honestly).

This is **not** abandoning the A4 route (ChatGPT/Grok's concern) — it is sequencing the cheap upstream gate and the cheaper handle before the expensive construction, exactly the leverage the review-first decision was meant to buy.

## Part 4 — Action items (renumbered into the live 11xx CC lane; Copilot's 1165–1169 collided with consumed numbers)

1. **(next) Ground-state-coherence gate** — derive/argue whether the CPP Sea ground state is single/global/defect-free, or admits domain fragmentation (the D-FRAG cheaper-kill test + the Q2/Q4 seam closure, in one). Promote-or-break upstream of A4.
2. **Correlation-length route** — define the Sea ground-state two-point function, derive ξ(t), test whether ξ tracks R_h in a ΛCDM background; seek the self-consistency relation.
3. **A4 coordinable-region construction (fallback)** — only if (2) reduces to the causal-structure question; target: derive boundary = R_h + the self-consistency relation, rule out particle horizon.
4. **Frontier batch (queued):** SR.md OPEN-SR-5d + CONJ-COSMO-2 — record the review outcome (status confirmed conditionally-supported; event-horizon = particle-defeated-not-unique; the gate reorder) at the next handover/milestone window (SM.md live under SF-2).

**Anti-priorities:** no verdict moved; no THEO; the package v1.0 stays the immutable request record; this file is the immutable review record. The arc remains conditionally supported.
