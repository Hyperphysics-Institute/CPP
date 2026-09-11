# EU-lane Handover — Session 201 Close (9 Sep 2026) — DM ring correction; 3882's amplitude result retracted

**Patch 3885. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3883 at session start; 3884–3885 delivered as patch files. **Next free: 3886.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## Read this if you inherited 3882's summary
**3882's headline is WITHDRAWN.** It reported DM clumping as coming *"within a factor of two on amplitude — a first for this arc."* **That used a mass the worker invented.** At the corpus's actual value the shortfall is **31 orders**.

**The correct statement: no candidate in this arc has come close on amplitude — without exception.**

## The correction
**CPP's DM particle is the RING:** 16 DM planes organised as 8 two-plane elements, **11.26 GeV**, formed when extreme turbulence bends a straight 16-plane **rod** into a closed circle. **Founder registration Patch 3426, 25 August 2026.**

**How the error happened, and it is a D-3 failure of a specific kind.** 3882 quoted `DM_project_map.md`, whose own header reads *"Last updated: Session 156, 10 June 2026"* — **two and a half months before** the ring registration. **D-3 was applied to the project map instead of to the lane**, one session after the rule was written into `bootup.md` §0.5.

> **A project map is a summary, and summaries age. The lane files and the `founders_voice/` record do not age the same way.** That distinction is what D-3 is actually about, and it should be read into the rule.

## The founder's question, worked as asked
*Could aggregation of rings at the various fractal levels satisfy the CMB anisotropy?*

**Amplitude — reachable, but only by choosing the level.** δ = 10⁻⁵ at 100 Mpc needs **N = 10¹⁰ objects**, i.e. **3.2×10⁶ M☉ per clump ≈ 3×10⁶² rings each**. Selecting the aggregation level to land on the answer is calibration (PD-007).

**Shape — fails at EVERY clump mass, and this is decisive because it is amplitude-independent.** Poisson seeding is **white**, so **δ ∝ r^{−3/2}**:

| scale | Poisson (normalised at 100 Mpc) | observed |
|---|---|---|
| 10 Mpc | 3.2×10⁻⁴ | ~10⁻⁵ |
| 100 Mpc | 1.0×10⁻⁵ | ~10⁻⁵ |
| 1000 Mpc | 3.2×10⁻⁷ | ~10⁻⁵ |

> **Choosing the clump mass slides the whole curve vertically and never tilts it. Aggregation changes amplitude and never shape — so no arrangement of fractal levels can help.**

**Plus two unchanged exclusions:** 10⁶ M☉ clumps must exist **at recombination** and structure that massive forms far later (the observed CMB is itself the evidence against them); and Poisson DM clumping is **isocurvature** (Planck-bounded) and an **active source** (acoustic peaks).

**Four independent exclusions now, where 3882 had three — the founder's correction strengthened the verdict.**

## What survives
**"Massiveness buys noise"** remains a sound lesson — it is precisely why the invented heavy mass looked promising and why the real light one does not. **The lesson was right; its application to CPP's DM was wrong**, because the worker supplied a parameter the corpus contained.

## Owed (none of it worker work)
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 dispatch; the amended DE escalation (3858); `cosmic_web_generation_constraints.md` owed-piece 1 (3833); **and new — `DM_project_map.md` is stale on the DM particle's identity** (flagged, not edited: cross-lane, no sanction).
- **EU-1 V1.7 (bundle):** the §Background VSL clarification (3854); the physical reading of eq. Nstar (3876 §5) as qualified by 3878.

## Forward queue
**OPEN-EU-LATTICE-EXTENT-1** (3878) — non-blocking. Nothing else.

**Anti-priorities:** follow **§0.5 D-1…D-6**, and specifically **read the lane, not the project map**; **never supply a parameter the corpus contains** — check first, always; no calibration against an observable (PD-007); no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_201_log.md` (3885). **B** transcript row 3884. **C** development vignette (Session 201).
- **D** Tier 4: `reasoning/3884_dm_ring_retraction.md`.
- **E** Registries: `research_frontier.md` (3884 prepend); `id_block_registry.md` (next free 3886); `future_projects.md`; in-place retraction at `dm_clumping_cmb.md` §2b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`; **`DM_project_map.md` deliberately NOT edited** — cross-lane.
- **F** none (no panel). **G** no PD minted; founder correction registered verbatim. **H** this file.

## Governance note — the sharpest version of D-3 yet
**Three sessions, three escalating instances of the same failure.** At 3866 D-3 caught a mis-scoped item in the worker's own handover. At 3884 it was the worker again — but this time the rule was *applied* and still failed, because it was applied to a **summary document** rather than to the primary record.

> **Amend D-3 in practice: "locate the object" means the lane files and `founders_voice/`, not a project map, roadmap, or status table. Those are summaries and they go stale silently.**

And a second, harder rule this session earns: **never supply a parameter the corpus contains.** The invented mass was flagged as a fit, which felt like sufficient honesty at the time. It was not — the flag excused using a made-up number instead of prompting a search for the real one.
