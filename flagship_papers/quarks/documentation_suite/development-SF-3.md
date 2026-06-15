# Development History: SF-3 — The Quark Sector from 600-Cell Geometry

## Purpose of This File

This is the Tier-3 development record for SF-3: how the paper came to be — the
decisions, the dead ends, the route adjudication, and the timeline. It is the
lab-notebook narrative for future collaborators (human and AI) who pick the
paper up after a context switch and need to know not just *what* SF-3 says but
*why it says it that way*.

## The Starting Point

By the time the SF-3 window opened (Session 161, 1500-patch band), the quark
sector was already almost entirely *shipped* — just scattered across six papers
that nobody had ever assembled into one account:

- **SM-8** — the zero-parameter cage-mass formula `M_q = m_e (z/φ) V^{7/3}` with
  the four bonded shells `V ∈ {4, 12, 20, 30}` (s, c, b, t).
- **SM-9** — the derivation of the `7/3` exponent and the anchor `M_0 = m_e z/φ`.
- **SM-7** — the strong coupling `α_s = 5/(8φ)`, the electroweak–strong
  complementarity `sin²θ_W + α_s = 1/φ`, and the quark Koide phase via an
  isotropic self-energy shift on the K₃ cage.
- **SM-10** — the finite-element chain-network scaling *mechanism* (a calibrated
  model, four parameters / four data, pending GPU closure).
- **SS-1 / SS-2** — SU(3) colour from cage-face permutation symmetry and the
  colour Casimir `C_F = 4/3`.
- **SM-6** — the Weinberg angle `sin²θ_W = 3/(8φ)` from 600-cell spectral traces.

SF-3 was therefore scoped from the outset as a **synthesis / reframing
flagship**: no new derivation, just the assembly of shipped results into a
single quark-sector account, with the cross-sector consistency threads that
SF-7 (grand unification) will need.

## Key Discoveries (chronological)

### Discovery 1: Two mass-routes existed, and they disagreed about m_c

The corpus survey surfaced two shipped routes to the heavy-quark masses. **Route
A (SM-8)** predicts all four masses from `m_e` + geometry at RMS 2.1%, with
`m_c` an *output* (1249 MeV, −1.6%). **Route B (SM-7)** used the charm mass as a
*calibration constant* to place the quark Koide phase, buying marginally better
`b/t` residuals at the cost of a second calibration. The central drafting
question of SF-3 was: which route is canonical, and does the quark sector need
one calibration or two?

### Discovery 2: m_c can be demoted from calibration to prediction

Because Route A *derives* `m_c` from `m_e` at zero parameters, Route B's `m_c`
calibration is **redundant** — `m_c` can be supplied by the Route-A prediction
rather than fitted. Adopting Route A as canonical and demoting `m_c` to a
derived quantity **restores the single-`m_e` calibration headline** for the
quark sector. This is the spine of the SF-7 "hierarchy without hierarchy"
argument: one calibration across charged leptons (SF-1), neutrinos (SF-4), and
quarks (SF-3).

### Discovery 3: the quark Koide phase does not depend on m_c (Proposition 5.1)

The SF-3 *outline* had worried that the quark-phase machinery would need to be
"re-grounded" on the derived `m_c` once `m_c` was demoted. Working through the
retained SM-7 isotropic-shift formula showed this step is **unnecessary**: the
phase `θ_quark` is a function of `{α_s, sin²θ_W, z}` only. The mass amplitude
`A_q` (the only place `m_c` ever entered the SM-7 construction) is an overall
scale in the Koide parametrisation and cancels from the ratio that fixes
`cos θ_quark`. This is **Proposition 5.1** — explicitly a *bookkeeping
separation* of inherited structure, not a new theorem.

### Discovery 4 (review-cycle): the independence is conditional on structural α_s

The single most valuable catch of the four-round review cycle (v0.4 adversarial
pass): Proposition 5.1's `m_c`-independence holds **because** `α_s` is taken as
the *structural* value `5/(8φ)`. Were `α_s` instead extracted from a
running-coupling fit at the charm scale, `m_c` would re-enter indirectly through
that fit. SF-3 adopts the structural value, so the proposition stands — but the
unstated version invited the objection. Stated explicitly at v1.0.

## Failed Approaches

### Failed Approach 1: keeping Route B (the two-calibration route) for accuracy

The temptation was to keep Route B's better `b/t` residuals (~0.3% improvement).
Rejected: a sub-percent accuracy gain is not worth a second calibration that
contradicts the single-`m_e` spine of SF-7. Route A canonical; Route B's
structural content (`α_s`, the complementarity, the Koide phase) retained as the
electroweak–strong complementarity layer.

### Failed Approach 2: claiming CKM via SM-10's "incidental mention"

SM-10 mentions CKM in passing, which briefly looked like a mixing-matrix handle.
It is not: SM-10 is the finite-element *scaling-mechanism* paper, not a mixing
paper. There is no CKM derivation anywhere in the quark corpus. This was
registered honestly as **OPEN-FP-3-CKM** rather than papered over.

### Failed Approach 3 (mislabels caught in review): version and over-claim drift

The first assembly was mislabeled v1.0 (corrected to v0.1 — pre-review drafts
are v0.x; v1.0 means SHIPPED in this programme). Across rounds the reviewers
also caught a sequence of over-claims that were progressively walked back:
"forced" → "selected by the mechanism" → "selected within the SM-8
antipodal-identification model" (generation count); "complete quark sector" →
"heavy-quark sector"; "unification" softened to "mode-fraction correspondence,
not a dynamical unification."

## Key Decisions and Why

### Decision 1: Route A canonical, m_c demoted (single-m_e calibration)

See Discovery 2. The load-bearing decision of the paper; everything downstream
(the SF-7 master table reading "one calibration for all fermion masses")
depends on it.

### Decision 2: Proposition 5.1 is a bookkeeping observation, NOT a theorem

It separates inherited SM-7 structure; it derives nothing new. It is therefore
*not* registered in `theorem-registry.md`. Calling it a theorem would have
inflated the paper's claimed originality.

### Decision 3: CKM registered as OPEN-FP-3-CKM, framed parallel to δ_CP

The quark mixing gap is the structural analog of SF-4's open neutrino δ_CP —
"masses derived, mixing-sector open" — stated as a *parallel of posture, not an
equivalence of difficulty*. The quark CP phase inside CKM is a separate object
from the neutrino δ_CP being pursued in the dedicated δ_CP window, so the gap
carries low cross-window collision risk.

### Decision 4: ship to v1.0 on four-round convergence (no Sonnet pass)

Thomas delegated the ship call. Four rounds, Grok SHIP all four, ChatGPT/Copilot
REVISE→SHIP convergence, zero physics blockers, numbers independently
re-verified every round. The optional Sonnet hostile pass was flagged as
available before public OSF/arXiv deposit but not required for the repo-internal
v1.0 state — the same bar SF-2/SF-4 shipped on.

## The Paper

`sf-3_quarks.tex` (v1.0 SHIPPED, 13 pages, 0 errors). Single `m_e` calibration;
zero shape parameters. Heavy-quark masses (RMS 2.1%), `α_s = 5/(8φ)`,
complementarity `sin²θ_W + α_s = 1/φ`, quark Koide phase 124.04° (0.05%),
three-generation count. CKM inherited-open. Inline `thebibliography` (master bib
also carries `abshier2026sf3`). All numbers verified by
`code/1500_verify_sf3_core.py` (ALL CHECKS PASS).

## Open Problems

- **OPEN-FP-3-CKM** (registered at SHIP, `frontier_sectors/FP.md`): quark mixing
  matrix + quark CP phase undelivered. Candidate route (to flag, not pursue): a
  quark-sector cage-mixing structure analogous to SM-5's K₃ → tri-bimaximal
  derivation of the PMNS matrix; presently unscoped.
- **Inherited:** SM-10's first-principles cascade remains a calibrated model
  pending GPU closure (the mass *values* do not depend on it).

## File Manifest

- `sf-3_quarks.tex` — the paper (v1.0 SHIPPED)
- `sf-3_outline.md` — pre-draft outline (patch 1303)
- `README.md` — subfolder orientation
- `sketches/SF-3_structural_core.md` — structural core sketch (patch 1308)
- `code/1500_verify_sf3_core.py` — numerical verification (ALL CHECKS PASS)
- `documentation_suite/` — changelog, reasoning (Tier 4), development (this
  file, Tier 3), transcript (Tier 2), + the 7-file companion suite
- `review/` — four review rounds (v0.1–v0.4), all reviewers, verbatim

## Timeline

- **Patches 1303, 1308** — outline + structural-core sketch (window bootstrap)
- **Patch 1500** — v0.1 assembly (initially mislabeled v1.0)
- **Patch 1501** — relabel v1.0 → v0.1
- **Patch 1502** — v0.1 → v0.2 (round-1 review incorporation: Prop 5.1 scoped as
  bookkeeping, m_c qualified, soften "unification", PDG-scheme caveat)
- **Patch 1503** — v0.2 → v0.3 (round-2: conclusion qualifier, §4 bare-partition
  gloss, §7 boxed summary, 120×120 adjacency anchor)
- **Patch 1504** — v0.3 → v0.4 (round-3: "forced" → "selected by the mechanism",
  §4 "one spectral trace" bounded, SM-10 reminder)
- **Patch 1505** — v0.4 → **v1.0 SHIP** (round-4 final items: generation-count
  model-dependence, Prop 5.1 α_s-structural nuance, §4 structural-correspondence,
  §9 MeV-scale, §10 "within the CPP ontology")
- **Patch 1506** — ship-time registry integration (OPEN-FP-3-CKM, predictions,
  paper_catalog, README, INDEX, master bib; swarm count held at 108)
- **Patch 1507** — Phase 7A documentation suite (this file + companions)
