# CPP Parallel-Development Roadmap & To-Do

**Location:** `/CPP/parallel_development_roadmap.md` (repo root)
**Purpose:** The living plan for scaling CPP from a one-researcher effort to a collision-resistant, parallel theorem-development team. Captures the strategic frame, the phased roadmap with gates, the Claude Code agentic-pilot assessment, the integrity subsystem requirements, and a phase-tagged to-do checklist. This file exists so the roadmap is **not lost** between sessions.
**Maintainer:** Thomas Lee Abshier, ND — Hyperphysics Institute
**Status:** PLANNING (no human workers onboarded yet; Phase 0 proof-of-concept is the current gate)
**Last updated:** 6 June 2026 (Session 154 — initial roadmap capture)

---

## Relationship to existing tracking files (read first — this is NOT a parallel registry)

This file is a **plan**, not a second source of truth. It reuses the existing infrastructure and points into it. It must never duplicate the registries.

- **`operating_system.md`** — the worker protocol (Phase 2) will be written here as a new section, NOT as a separate `theorem-dev/` subtree. One operating system.
- **`theorem-registry.md`, `predictions.md`, `axiom-registry.md`, `frontier_sectors/`** — the canonical registries. Workers read/write these. No new registry is created.
- **`research_frontier.md` + `frontier_sectors/`** — the frontier-surface map (Phase 2) extends these, it does not replace them.
- **`future_projects.md`** — this initiative is registered there as a multi-session project; this file is its detailed plan.
- **`todolist.md`** — tracks small carried-over items; it points here for the team-scaling initiative.
- **`handovers/` + §15 protocol** — the handover discipline is the coordination backbone; parallel work plugs into it, not around it.

> **Governing principle:** Thomas is the single integrator of conceptual coherence. Every parallel branch eventually lands on him for harmonization. The entire design goal of this roadmap is to make parallel work **safe to integrate** (low-collision, terminology-clean, dead-ends-registered) so that integration stays cheap — *not* to maximize raw patch volume.

---

## 1. Strategic frame — why parallelize, and what actually scales

**The bottleneck reframe (Thomas, Session 154).** The scarce resource is Thomas's creative-physics judgment: inventing PCD/mechanical models that let a phenomenon's required mathematics emerge from the 9 axioms *without* adding a new axiom. Under the current solo process this is invoked rarely (the n_s / 1/k / p-thermalization harmonization was the first in months); nearly all of Thomas's time goes to shepherding the recommend → patch → run → publish cycle. That is a low-value use of a high-value resource.

**What parallelization changes.** A team of workers mining the theoretical landscape — taking derivations as far as they go, then registering the outcome (proven, dead-end, duplicate, open problem, or *needs-PCD-mechanism*) — would surface the judgment-heavy moments at a far higher rate. Thomas then spends most of his time on the creative-physics layer (his comparative advantage), and far less on decision-tree management. The bottleneck does not vanish; it **moves to the highest-value place**.

**What does NOT scale by adding workers.** Conceptual coherence. Two workers' arguments can each be locally correct yet globally incompatible; only Thomas's whole-theory judgment catches that. Therefore worker *output* must arrive pre-formatted for cheap integration, and the integrity subsystem (§4) is not optional polish — it is the thing that keeps integration from becoming the new bottleneck.

---

## 2. Phased roadmap with gates

Each phase has an explicit **GATE** that must pass before the next begins. Gates are how we avoid the negative-returns trap.

### Phase 0 — Proof of concept: collision-free multi-window (CURRENT)
Thomas runs 3 windows (3 simulated workers) on distinct theorems on one machine, with zero collisions and clean integration.
- **GATE 0:** 3 windows run a full work cycle each, produce 3 applied patches, with no file collisions, no terminology drift, and no duplicated derivation — verified by audit. **No human worker is onboarded until GATE 0 passes.**

### Phase 1 — Coherence layer (do before adding anyone)
Build the whole-theory view that currently does not exist, so parallel work is safe.
- `paper_summary/` extraction: one structured summary per paper (claim, dependencies, terms introduced, results, open items).
- Harmonization audit against **one enforced glossary** (`master_glossary.md`); flag/clean residual Grok/Sonnet terminology contamination.
- **GATE 1:** every published paper has a summary; glossary is the single terminology authority; a terminology-drift scan runs clean.

### Phase 2 — Worker protocol + integrity subsystem
Write the protocol as a section of `operating_system.md` (not a new subtree). Stand up the integrity subsystem (§4).
- **GATE 2:** protocol documented; collision-resistance, dual-terminology scan, dead-end/duplicate registration, repair protocol, and frontier-surface map all operational and tested in the Phase 0 multi-window setting.

### Phase 3 — Work classification + escalation triggers
Classify every task as **mechanical** (routable to a trainee/agent) or **judgment-heavy** (stays with Thomas). Define the escalation triggers (§5) that fire when a derivation hits a PCD/mechanism gap.
- **GATE 3:** a written triage rubric exists; escalation triggers are explicit and conservative; a worker can self-classify a task without Thomas.

### Phase 4 — First human worker (Mika)
Onboard one human. Thomas + Mika pair on her first cycles; she works only mechanical-class tasks; insight and final integration stay with Thomas.
- **GATE 4:** Mika completes N supervised cycles producing clean, integrable patches; her dead-ends/duplicates are correctly registered.

### Phase 5 — Scale 3 → 5 → 10, with re-evaluation gates
Add workers one at a time. After each addition, measure: integration cost per patch, collision rate, terminology-drift incidents, and Thomas's time-share on creative physics vs. management.
- **GATE 5 (recurring):** if integration cost per added worker rises rather than falls, **stop and fix the subsystem before adding the next person.** This is the explicit guard against negative returns.

---

## 3. Claude Code / agentic pilot — assessment & shape

**Verdict:** realistic and valuable for the **mechanical execution layer**; not yet safe for **unsupervised banking of physics results**.

**Safe to automate now (agentic, human-gated):**
- The apply-and-push chain; running verify scripts; registry greps and the CLONE-FIRST gate; consistency/terminology audits; file placement; figure regeneration; transcript curation. This is exactly the GitHub-interface drudgery to lift off Thomas.

**NOT safe to automate (hard gate required):**
- Registering a THEO, promoting a prediction to counted status, or shipping a paper. These require swarm review and/or Thomas. The phantom-"task card" confabulation in the 5–6 June Copilot transcript is the canonical failure mode: confident, plausible, wrong, unwatched. An unsupervised loop would commit this silently and repeatedly.

**Pilot shape:**
1. Start Claude Code on the mechanical layer only, behind hard gates (no autonomous registration/promotion).
2. Build and tune the **escalation-trigger detector** (§5) during Phase 0 — the conservative "stop and call Thomas" classifier is the load-bearing safety component.
3. Expand the agent's autonomy only as the detector proves reliable, and never past the swarm/Thomas gate on banked results.

---

## 4. Integrity subsystem requirements (the operational guts)

These are the conditions Thomas named; they are the difference between safe parallelism and a tangle.

- **Window/lease discipline:** one theorem per window; a lightweight "who owns which files right now" lease so two windows never edit the same file concurrently.
- **Registry-grep gate:** before registering an ID, placing a file, or computing a coefficient, clone + grep the registry (existing CLONE-FIRST gate, enforced per worker).
- **Dual-terminology detection:** an automated scan against `master_glossary.md` flags any new term or synonym before it lands; new primitives require Thomas sign-off.
- **Dead-end / duplicate / open-problem registration:** every stopped derivation is logged (not deleted) with its reason, so no worker repeats it and Thomas can see the frontier honestly.
- **Repair / redundancy protocol:** when two branches collide or diverge, a defined procedure decides supersede-vs-reconcile (transformation theorem only where genuinely cheaper than re-derivation — it is a tool, not a free lunch).
- **Frontier-surface map:** extend `research_frontier.md` + `frontier_sectors/` into a navigable "next most promising attack surface" view so workers always pull from a prioritized, non-overlapping queue.
- **Progress tracking:** integration cost per patch, collision rate, drift incidents, and Thomas's creative-physics time-share are tracked as the health metrics that drive the Phase 5 gates.

---

## 5. Escalation triggers — when a worker/agent MUST stop and call Thomas

Conservative by design: when uncertain, escalate.
- The phenomenon's required mathematics will not emerge from the 9 axioms by any mechanical route the worker can find (candidate **needs-PCD-mechanism** — Thomas's layer).
- A derivation appears to require a **new axiom** (almost always actually a missing PCD/mechanical interpretation — exactly Thomas's strength; do not invent an axiom, escalate).
- Two branches conflict conceptually (not just textually).
- A result would cross a hard gate (THEO registration, prediction promotion, paper ship).
- The worker has ground for more than a set budget without a clear next mechanical step.

---

## 6. To-Do checklist (phase-tagged)

**P0 — proof of concept**
- [ ] Run 3 windows on 3 distinct theorems; verify zero collisions + clean integration (GATE 0).
- [ ] Draft the lease/ownership scratch convention for multi-window work.

**P1 — coherence layer**
- [ ] Scaffold `paper_summary/` and define the per-paper summary template (reuse existing metadata where present).
- [ ] Generate summaries for all published papers (start from existing documentation metadata).
- [ ] Run a terminology-drift audit against `master_glossary.md`; clean residual Grok/Sonnet contamination.

**P2 — protocol + integrity subsystem**
- [ ] Write the worker protocol as an `operating_system.md` section.
- [ ] Implement dual-terminology scan, dead-end/duplicate registration, repair protocol.
- [ ] Build the frontier-surface map view over `research_frontier.md` + `frontier_sectors/`.

**P3 — classification + escalation**
- [ ] Write the mechanical-vs-judgment triage rubric.
- [ ] Finalize the escalation-trigger list and the agent's conservative stop-and-ask classifier.

**P4 — first human (Mika)**
- [ ] Pair-onboard; supervised cycles; verify clean integrable output (GATE 4).

**P5 — scale**
- [ ] Add workers one at a time; run GATE 5 health check after each.

**Agentic pilot (parallel track)**
- [ ] Stand up Claude Code on the mechanical layer only, human-gated (coordinate with Isak).
- [ ] Tune the escalation-trigger detector during P0.

---

## 7. Open decisions needed from Thomas

- Project-management template: adopt this file's phase/gate structure as the reusable template, or formalize a separate `templates/` PM template?
- Phase 0 theorem selection: which 3 theorems are the proof-of-concept set?
- Agentic pilot: green-light Claude Code mechanical-layer pilot now, or after GATE 1?
- Onboarding order after Mika: confirmed slow expansion (3 → 5 → 10) with GATE 5 enforced.
