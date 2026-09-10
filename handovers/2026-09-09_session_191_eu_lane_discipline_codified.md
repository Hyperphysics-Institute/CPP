# EU-lane Handover — Session 191 Close (9 Sep 2026) — process rules moved into the read path; BATH-DEPTH-1 is next

**Patch 3865. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3863 at session start; 3864–3865 delivered as patch files. **Next free: 3866.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## Read `bootup.md` §0.5 before doing any work
That section is new this session and it is the reason this handover is short. **Six standing rules, each with the cost that produced it**, now sit in the Step 1 read table at priority 1.5 — because Step 1 is read every session and **a handover is not**.

## The single most important next action
**OPEN-EU-BATH-DEPTH-1.** It owns **κ = kT_bath/E_Pl**, and κ is exactly what T-2's residual reduces to: 3850 delivered **λ = α/κ**, so every remaining uncertainty in the O(α) correction — and therefore in EU-1's quoted theory error, now a one-sided shift of +5.0×10⁻⁴ — is κ's and nothing else's.

It is the **last substantial item that is local, unblocked, and needs nothing from outside the lane.** Everything else here is maintainer-gated.

Two things already constrain κ and should be the starting point:
- **κ ≤ 1** (3850 §2) — the bath runs on the substrate clock, so kT ≤ E_Pl.
- **κ ≳ 0.1** (3850 §4) — from the observed tilt: Planck 1σ requires λ ≲ 9.7α. An observation *bounding* a parameter, not a fit.

So κ ∈ [0.1, 1] already, and the question is whether the bath clause can derive it rather than bound it.

## What was done this session
**3864 — the arc's process rules codified into `bootup.md` §0.5.**

The founder asked whether the governance rules had changed the template/OS or were only a note to one context window. **The answer was the second, and the question exposed a defect.** The rules were in handovers, logs and the frontier — committed, persistent — but **bootup Step 2 reads only the most recent handover and every session supersedes the last**, so a durable process rule placed there **leaves the read path within one session**: it stays in the repository and stops being read. **And bootup.md had no standing worker-discipline section at all**, which is precisely why the rules kept landing in handovers.

**Fixed:** §0.5, in the Step 1 table at priority 1.5, marked *read before doing any work*. **D-1** search the corpus for the **mechanism** a clause names before declaring it fails; **D-2** re-check the premise of any item carried over >2 sessions; **D-3** locate an object before building on it; **D-4** a flagged check is not a performed check; **D-5** check `git log` and the id counter against origin before starting; **D-6** check a lane is complete before escalating against its numbers. Each carries its cost record. **Common remedy: one `grep` on the thing it names.**

**Honest limit, recorded in the patch:** this is the necessary condition, not the sufficient one — a version of D-2 was written at 3854 and its spirit violated twice in the three sessions that followed.

**No physics was touched.** PRED-C-96, T-1, T-2, 3816's restored basis and the amplitude closure are all where 3862 left them.

## Forward queue
1. **OPEN-EU-BATH-DEPTH-1** (above). The last substantial local item.
2. **Maintainer:** CONV-046 dispatch; the amended DE escalation (3858); `cosmic_web_generation_constraints.md` owed-piece 1 (3833).
3. **EU-1 V1.7 (small, bundle):** the §Background VSL clarification (3854). No repair note is owed — **3816 stands** (3862).
4. **Residual observation** (3862): first-Moment bits carry count without directional content. An ignition-dynamics question; not urgent.

**Anti-priorities:** follow **§0.5 D-1…D-6**; no calibration against an observable (PD-007); **do not re-open 3816's basis** — it was restored at 3862; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc is a refutation of n_s** — PRED-C-96 has never moved.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_191_log.md` (3865). **B** transcript row 3864. **C** development vignette: **N/A** — 3864 touches no paper content; the EU-1 development file records physics, and a process-documentation patch does not belong in it.
- **D** Tier 4: `reasoning/3864_discipline_codification.md`.
- **E** Registries: `bootup.md` §0.5 **(new; the substantive change)**; `research_frontier.md` (3864 prepend); `id_block_registry.md` (next free 3866); `future_projects.md`. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — no physics touched.
- **F** none (no panel). **G** no PD minted; founder question answered and acted on. **H** this file.

## Governance note
**A rule written where it will not be read is not a rule.** This session's whole content was discovering that six lessons had been recorded faithfully and filed somewhere that guarantees they would be forgotten. The founder caught it by asking a question I had not thought to ask myself — the difference between *writing something down* and *putting it where the next reader looks*.
