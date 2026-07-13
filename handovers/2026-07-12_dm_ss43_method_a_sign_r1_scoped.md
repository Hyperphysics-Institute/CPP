# Handover — OPEN-DM-FLOQUET-1: method (a) COMPLETE (sign conditional/narrow) + R1 SCOPED (branch-dependent ε map)

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

**Sort caution (same-date collision):** this file shares the date 2026-07-12 with the previous handover
`2026-07-12_dm_ss43_makeorbreak_reopened_floquet_scoped.md`. The scope prefix `method_a` sorts alphabetically AFTER
`makeorbreak`, so `ls handovers/ | sort` places THIS file last. If ever ambiguous, **`git log` names the true
newest.** Warm-launch keyword: **DM-WARM-2441.** HEAD should be Patch 2442 (this handover).

## Orientation — read this first
OPEN-DM-FLOQUET-1 is the single blocking computation for candidate (B)'s make-or-break (κ_θ/E_bond ≥ 0.43); it was
scoped last session (Patch 2438) with 7 Required Elements + guardrails G1–G7. This session executed **method (a)**
(the reduced Floquet–Mathieu sign analysis) and **scoped R1** (the driven equilibrium). Method (a) result (Patch
2440): the transverse charge-switched mode is the Meissner (square-wave) parametric oscillator; its sign is
**CONDITIONAL and NARROW** — the statically-inverted δ=3/7 mode is parametrically stabilized ONLY for
ε=(ω_A/ω_sw)² ∈ [0.18, 0.43], and the fast-switching limit is UNSTABLE (this killed the naive "fast ZBW switching
stiffens it" heuristic; G1 PASS). R1 scoping (Patch 2441): using ω_sw = the "SU(3)-type ZBW hop" (Compton-scale),
the sign is **branch-dependent** — only the **deep E_qq core + qDP-hop** corner lands ε ≈ 0.21 in-window; all other
corners are unstable. That corner is **plausible, not established** (±30% in E_qq spans the window edge), and R5
netting still gates the final sign. Candidate (B): **UNRESOLVED**; registry NOT promoted; Ω_DM parked. **Next action:
the full self-consistent R1 solve** — derive the fragmentation branch from the coordinate (R6/G6; only deep-core is
in-window), derive the effective ω_sw from residence times (R2, not the bare Compton clock), then hand to R5
(recompute + net the geometry-#3 ponderomotive tensor). It wants a fresh focused run; do NOT read "ε in-window" as
"survives."

**Repository state:** HEAD at Patch 2442 (this handover); highest substantive patch 2441. All of 2440–2441
committed under Opus authorship. No uncommitted work.
**Active work:** OPEN-DM-FLOQUET-1 (`series_phenomena/cosmology/dark_matter/OPEN-DM-FLOQUET-1_scoping.md`), under
OPEN-SS-43. Candidate (B): UNRESOLVED. Ω_DM: parked.

## Forward queue
**Priority 1:** The full self-consistent **R1 driven-equilibrium solve** on geometry #3. Read
`R1_geom3_driven_equilibrium_scoping.md` FIRST (it pins the setup, the in-hand inputs, and the branch-dependent ε
map). Deliver, in order: (1) **R6/G6** — derive which bond fragments (deep E_qq core vs shallow E_ee coat) from the
fragmentation coordinate; only the deep-core branch is even in the stability window. (2) Pin E_qq (and s) at that
branch and derive the **effective ω_sw** from the hop residence times (R2), not the bare Compton clock — this
decides whether ε lands in [0.18, 0.43]. (3) Report the dynamical δ and branch asymmetry ε_att/ε_rep.
**Priority 2:** **R5/G4** — recompute the geometry-#3 ponderomotive tensor (the 2430 analog had a −190 transverse
eigenvalue on the superseded far-out-coat geometry) and **net** K_switch against it. This gates the final sign
regardless of the R1 corner; a positive in-window K_switch can still be overturned.
**Priority 3:** Only if the netted transverse sign is positive → method (b) (MD/kMC magnitude) to get κ_θ and the
κ_θ/E_bond ratio for the decision rule (scoping §5).
**Anti-priorities:** Do NOT promote the registry or call survival on the favorable ε≈0.21 corner — it is plausible,
not established (2434 was refuted for exactly this "seize the favorable sub-case" move; G7 binds). Do NOT re-run
method (a) with a cherry-picked ε/branch. Do NOT skip R5 netting.

## Where to find detail
- **Scoping doc + progress log:** `series_phenomena/cosmology/dark_matter/OPEN-DM-FLOQUET-1_scoping.md` §7 (method (a)
  + R1 entries).
- **Method (a) result:** `series_phenomena/cosmology/dark_matter/floquet_method_a_sign_result.md`.
- **R1 scoping:** `series_phenomena/cosmology/dark_matter/R1_geom3_driven_equilibrium_scoping.md`.
- **Latest Tier 4 reasoning:** `series_phenomena/cosmology/dark_matter/reasoning/2440.md` (method (a), incl.
  self-correction of the Kapitza heuristic) and `reasoning/2441.md` (R1 scoping, incl. self-correction of "leaning
  unfavorable").
- **Verify scripts:** `code/2440_floquet_method_a_sign.py` (Meissner Floquet; reproduces the window + all numbers),
  `code/2441_r1_eps_scale_estimate.py` (branch-dependent ε table).
- **Live registry entry:** `frontier_sectors/SS.md` under OPEN-SS-43 (method (a) + R1-scoped status lines).

## Step-by-step audit of this session's handover
- **Step A** (Tier 1 session log): N/A — long-arc campaign session; per-patch Tier 4 reasoning notes serve as the
  session record (§15.14 incremental cadence); this handover is the session-close state record.
- **Step B** (Tier 2 transcript): N/A — no transcript file produced this session.
- **Step C** (Tier 3 vignette): N/A — the Orientation paragraph + arc above is the curated vignette; this is
  frontier/campaign work, not paper-.tex-scoped reasoning.
- **Step D** (Tier 4 reasoning): ✓ — `reasoning/2440.md`, `reasoning/2441.md` (verbatim, at-patch; both include the
  session's self-corrections). Every physics patch bundled its reasoning.
- **Step E** (registries, per-registry audit):
  - `frontier_sectors/SS.md` (research_frontier sector): ✓ — OPEN-SS-43 / OPEN-DM-FLOQUET-1 method (a) + R1-scoped
    status lines added.
  - `OPEN-DM-FLOQUET-1_scoping.md` progress log: ✓ — method (a) + R1 entries appended.
  - theorem-registry / axiom-registry / predictions / paper_catalog / master_glossary / methods_catalogue /
    future_projects / problem_histories / organizational_frontier: N/A — no theorems, axioms, predictions, papers,
    terms, new methods, or org items shipped (method (a) is a sign result; R1 is scoping; nothing promoted).
- **Step F** (reviewer artifacts): N/A — no CONV-001 / reviewer content this session (a leaning-conditional sign
  result and a scoping pass; no verdict promoted, so no panel run).
- **Step G** (protocol/OS updates): N/A — no OS/template changes.
- **Step H** (this document): ✓ — `handovers/2026-07-12_dm_ss43_method_a_sign_r1_scoped.md`.
- **Per-patch capture audit (§15.15):** ✓ — Patch 2440: `reasoning/2440.md` + `code/2440_floquet_method_a_sign.py`;
  Patch 2441: `reasoning/2441.md` + `code/2441_r1_eps_scale_estimate.py`. Both physics patches fully captured; no
  gaps.

## Recent session count
This session: 2 substantive patches (2440 method (a), 2441 R1 scoping) + this handover (2442). Session opened on the
2026-07-12 make-or-break handover, cleared the stranded Patch 2438 (scoping doc never applied → founder applied it),
then executed method (a) and scoped R1. OPEN-SS-43 remains the sole live DM-core coring candidate line; candidate (B)
UNRESOLVED throughout.

## Quick-start for next session
1. Paste the kickoff line above into a fresh context window (warm keyword: DM-WARM-2441).
2. Bootup: clone + read `bootup.md`; honor the CLONE-FIRST GATE (grep the registry).
3. Read `R1_geom3_driven_equilibrium_scoping.md`, then default action = Priority 1 (full self-consistent R1 solve:
   R6 branch → E_qq/ω_sw → δ), unless Thomas redirects. Then Priority 2 (R5 netting). Honor G7: report a
   negative/sub-window result as fail/unresolved, not re-parametrized into survival.
