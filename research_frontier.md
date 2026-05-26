# CPP Research Frontier

**Location:** `/CPP/research_frontier.md`
**Last updated:** 24 May 2026 (Session 142, F.1 / SS-9 / Capotauro thread). Prior session-by-session running-update log extracted to [`session_logs/2026-05-24_session_142_extracted_from_frontier.md`](session_logs/2026-05-24_session_142_extracted_from_frontier.md) on 25 May 2026 (changelog decomposition).

**Last updated:** 20 May 2026 (Session 137, OPEN-SS-35 / SS-9 closure-programme thread). Prior session-by-session running-update log (21 sessions, head Session 137 plus 20 Earlier-marked blocks) extracted to dated `session_logs/2026-05-*_session_*_extracted_from_frontier.md` files on 25 May 2026.
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute
**Architecture:** See `templates/research_frontier_architecture.md`
**Nomenclature:** See `nomenclature.md`

---

## Purpose

One flat file showing the complete landscape of every identified problem, conjecture, proposition, and frontier item in Conscious Point Physics — with status, sector, dependencies, and enough context to assess interconnections.

**Answers the question:** *What is solved, what is open, and what connects to what?*

**Problem count:** 86 entries (51 open, 16 conjectures, 15 propositions, 6 resolved, 6 falsified). *(Counts exclude sub-problems.)*

---

## How to Use This File

- **Finding work:** Scan by sector or priority. Start with the Recommended Attack Order (§7).
- **Starting a problem:** Read the entry here for context, then the history file (when it exists) for what has been tried.
- **After a session:** Update the relevant entry's status, "Current best lead," and "Last updated" fields.
- **After a paper:** Move resolved items to §5. Update dependency graph.

---

# §1 — Active Open Problems (OPEN)

Problems with no candidate solution, or where candidate solutions have been explored but no resolution is in sight.

---


## Sector Index — Active Open Problems, Conjectures, and Propositions

The active open problems, conjectures, and propositions are organized by sector under [`frontier_sectors/`](frontier_sectors/). Each sector file contains the full problem statements with status, mechanisms, route history, and acceptance criteria. Load only the sector you are working on.

### §1 — Active Open Problems by Sector

| Sector | File | Scope | Problems |
|--------|------|-------|----------|
| FP | [`frontier_sectors/FP.md`](frontier_sectors/FP.md) | Flagship Papers — apex layer (SF-line) | 9 |
| SS | [`frontier_sectors/SS.md`](frontier_sectors/SS.md) | Strong Sector (includes SS-specific propositions and conjectures from SS-5, SS-6, SS-7) | 18 active, 1 retired |
| SM | [`frontier_sectors/SM.md`](frontier_sectors/SM.md) | Standard Model Emergence | 11 |
| EW | [`frontier_sectors/EW.md`](frontier_sectors/EW.md) | Electroweak Sector | 6 |
| QM | [`frontier_sectors/QM.md`](frontier_sectors/QM.md) | Quantum Mechanics | 5 |
| SR | [`frontier_sectors/SR.md`](frontier_sectors/SR.md) | Special Relativity / Gravity | 8 |
| SD | [`frontier_sectors/SD.md`](frontier_sectors/SD.md) | Foundations / Superdeterminism | 6 |
| GLOBAL | [`frontier_sectors/GLOBAL.md`](frontier_sectors/GLOBAL.md) | Cross-Series (e.g., three SM generations, full SM from single 600-cell) | 2 |
| WORKFLOW | [`frontier_sectors/WORKFLOW.md`](frontier_sectors/WORKFLOW.md) | Workflow / Infrastructure | 1 |

### §2, §3 — Cross-Sector Categories

| Category | File | Description |
|----------|------|-------------|
| §2 Conjectures | [`frontier_sectors/CONJ.md`](frontier_sectors/CONJ.md) | Conjectures under investigation, all sectors |
| §3 Propositions | [`frontier_sectors/PROP.md`](frontier_sectors/PROP.md) | Propositions in progress, all sectors |

### Loading Discipline

- **Bootup** loads this dashboard only (~280 lines). It does NOT load any sector file.
- **Session work** loads the relevant sector file on demand. Working OPEN-SS-35 → load `frontier_sectors/SS.md`. Working SF-4 → load `frontier_sectors/FP.md`. Working PMNS angles (OPEN-SM-5) → load `frontier_sectors/SM.md`.
- **Cross-sector planning** may load multiple sector files, but rarely all eleven. Programme-level questions (e.g., "what closes if SS-35 closes?") use §8 Dependency Graph below as the entry point.

### Decomposition Provenance

- Original monolithic file: 1852 lines (Research_Frontier.md pre-2026-05-25).
- Decomposition performed 2026-05-25 to resolve repeated context-window overflow at bootup.
- §1 sector content extracted by line-range to `frontier_sectors/<SECTOR>.md`. §2 and §3 extracted to `frontier_sectors/CONJ.md` and `frontier_sectors/PROP.md`.
- §4–§10 (Recently Resolved, Resolved Archive, Falsified, Recommended Attack Order, Dependency Graph, Problem Count Summary, Anomalies) retained in this dashboard below.
- Pre-decomposition snapshot also recoverable from git history.

# §4 — Recently Resolved (THEO)

Kept here for one cycle, then moved to §5.

---

### THEO-SS-9 → OPEN-SS-9: δ = 1/3 Proved (C₃ + Cage Completeness)
**Resolved:** 29 March 2026
**Resolving paper:** SM-1 Theorem 1 (v6)
**Resolved by:** Thomas Lee Abshier ND, Claude Sonnet, Grok
**Summary:** Topological proof: C₃ symmetry forces δ₁ = δ₂ = δ₃; cage completeness forces δ₁+δ₂+δ₃ = 1; therefore δ = 1/3 exactly. Corollary: q_up = +2/3, q_down = −1/3. Integral approach (δ ≈ φ⁻² ≈ 0.382) superseded.

### THEO-SM-1 → OPEN-SM-1: k_SM Derived from 600-Cell Voronoi
**Resolved:** 23 March 2026
**Resolving expression:** k_SM = α_geom/(12φ²) ≈ 0.017805
**Summary:** α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.55936 from Voronoi stiffness integral. 3.8% residual = stereographic projection correction. Same α_geom appears in SR coupling.

### THEO-SM-2 → OPEN-SM-2: sea_strength = 10 × k_SM
**Resolved:** 23 March 2026
**Resolving expression:** sea_strength = (N_lattice/z) × k_SM = (120/12) × k_SM = 10 × k_SM ≈ 0.17805
**Summary:** Factor of 10 = total vertices / coordination number. Exact geometric ratio. Coupling sector has zero free parameters.

### THEO-QM-2 → OPEN-QM-2: Schrödinger Equation Derived
**Resolved:** 31 March 2026
**Resolving paper:** QM-1 (cpp2040a_v31.tex), THEO-QM-1
**Summary:** Complex DI-bit hopping approach gives exact Schrödinger equation in continuum limit.

### THEO-QM-4 → OPEN-QM-4: Decoherence Timescale
**Resolved:** 31 March 2026 (effectively)
**Resolving papers:** QM-4 THEO-QM-6 (Lindblad) + SD-3 THEO-SD-6 (apparatus)
**Summary:** Single-qubit dephasing rate derived in QM-4; macroscopic decoherence time derived in SD-3.

### THEO-QM-new-9 → OPEN-QM-new-9: r_conf Inconsistency
**Resolved:** 30 March 2026 (same session)
**Summary:** Mislabeling in SM-3 eq:hop_amp. All three constants correct; SM-3 assigned wrong name to computed value.

---

# §5 — Resolved Archive (THEO)

Complete list of all problems that became theorems.

| ID | Resolution | Date | Paper |
|---|---|---|---|
| THEO-SS-9 | δ = 1/3 from C₃ symmetry + cage completeness | 29 Mar 2026 | SM-1 Theorem 1 (v6) |
| THEO-SM-1 | k_SM = α_geom/(12φ²) | 23 Mar 2026 | SS-1 §8 + SR-1 companion |
| THEO-SM-2 | sea_strength = 10 × k_SM | 23 Mar 2026 | SS-1 §8 |
| THEO-QM-2 | Schrödinger equation from lattice dynamics | 31 Mar 2026 | QM-1 v3.1 |
| THEO-QM-4 | Decoherence timescale γ and τ_dec | 31 Mar 2026 | QM-4 + SD-3 |
| THEO-QM-new-9 | r_conf labeling error (not true inconsistency) | 30 Mar 2026 | SM-3 correction |

---

# §6 — Falsified (FALS)

Tested and found wrong. Never deleted. The record of what failed is as valuable as the final solution.

---

### FALS-C-SM-1: C₆₀ (60 Vertices) as Top Quark Cage
**Falsified:** March 2026 (PS-1 session)
**Why it fails:** No 60-vertex distance shell exists in the 600-cell.

### FALS-C-SM-2: φ^(3(l-1)) Quark Mass Scaling
**Falsified:** March 2026 (PS-1 session)
**Why it fails:** Actual shell volumes deviate by 3–8×. Volumes peak at equatorial shell, then decrease (palindromic structure).

### FALS-C-SM-3: AB Loop as Origin of θ_Koide
**Falsified:** Session F (25 March 2026)
**Why it fails:** C₃ symmetry prevents chiral preference on K₃; numerics also fail.

### FALS-C-SM-4: 4D 600-Cell Embedding Breaks C₃ for θ
**Falsified:** Session G (25 March 2026)
**Why it fails:** All 600 tetrahedral cells computed; C₃ preserved exactly in 4D.

### FALS-C-SM-5: Self-Consistent ZBW Mass Feedback Selects θ
**Falsified:** Session L
**Why it fails:** Fixed-point iteration converges to θ = 180° (trivial), not 132.73°.

### FALS-C-SM-6: Löwdin Downfolding (K₄→K₃) Breaks Antibonding Degeneracy
**Falsified:** Session E (24 March 2026)
**Why it fails:** V₄ is dark to antibonding modes; ⟨φ₋|v⟩ = 0 exactly.

### FALS-SC-1 (partial): Hybrid Quark Mass Ladder
**Falsified:** 30 March 2026
**Why it fails:** Top quark mass cannot come from C_n × N_l (103× discrepancy). C_n confirmed as real geometric quantities; formula architecture needs fundamental rethinking for top quark.

---

# §7 — Recommended Attack Order

Ordered by: fewest prerequisites, most tractable, highest leverage on downstream problems.

| Rank | ID | Why | Tractability |
|------|-----|------|-------------|
| ~~1~~ | ~~OPEN-SS-11~~ | ~~Pure group theory; 1–2 pages. Elevates SS-1 to necessity.~~ | ~~1 session~~ **RESOLVED → THEO-SS-10** |
| 1 | OPEN-SS-5 | One dimensional-analysis step. Prerequisite for 4 other problems. | 1 session |
| 2 | OPEN-SS-13 | WKB calculation; confirms C₃ proof mechanically. | 1 session |
| 3 | OPEN-SS-8 | Clear SU(6) + ZBW path. | 1–2 sessions |
| 4 | OPEN-SS-12 | Requires reading EW-2; high physical importance. | 2 sessions |
| 5 | OPEN-SS-1 | Mechanism established; find ZBW-frequency kernel. | Multi-session |
| 6 | OPEN-SS-27 | D2 derivation via A6' extension. Closure auto-delivers D1 under simplicial combinatorics (two-for-one). SS-8 v0.1 drafting target. | 2-3 sessions |
| 7 | OPEN-SD-1 | Resolves superdeterminism amplitude conjecture. | 2 sessions |
| 8 | CONJ-EW-1 | Gates CONJ-SM-6 (which gives θ to 0.003%). | Multi-session |
| 9 | OPEN-SS-3 | ZBW notebooks give starting point. | 2 sessions |
| 10 | OPEN-SM-10-FEM | #1 forward project; GPU implementation. | Multi-session |
| 11 | OPEN-SD-lattice-scale | Foundational; blocks experimental scrutiny. | 2 sessions |
| 12 | OPEN-EW-1 | Hardest single problem; requires new scaling argument. | Unknown |
| 13 | OPEN-G-1/G-2 | Capstone; emerges when sector problems converge. | Depends on all |

---

# §8 — Dependency Graph

```
SOLVED:
  THEO-SS-9 (δ=1/3) ✅ ──────────────────────────────► OPEN-G-2
  THEO-SM-1 (k_SM) ✅ ────────────────────────────────► OPEN-G-2
  THEO-SM-2 (sea_strength) ✅ ────────────────────────► OPEN-G-2
  THEO-QM-2 (Schrödinger) ✅
  THEO-QM-4 (decoherence) ✅

STRONG SECTOR:
  OPEN-SS-5 (σ) ────► OPEN-SS-7 (Λ_QCD) ────────────► OPEN-G-2
                ├──── OPEN-SS-10 (nuclear)
                ├──── OPEN-SS-6 (glueball)
                └──── OPEN-SS-14 (deconfinement T)
  OPEN-SS-1 (M_q) ──► OPEN-SS-3 (chiral) ───────────► OPEN-G-1
                 └──► OPEN-SS-2 (generations) ────────► OPEN-G-1
  OPEN-SS-11 (SU3 unique) ───────────────────────────► SS-1 Thm 1 (strengthens)
  OPEN-SS-12 (W bracelet) ───────────────────────────► OPEN-G-2
  OPEN-SS-8 (μ_N) ───────────────────────────────────► OPEN-G-2
  OPEN-SS-4 (β₁) ────────────────────────────────────► OPEN-G-2

ELECTROWEAK:
  CONJ-EW-1 (sin²θ_W) ──► CONJ-SM-6 (θ_Koide) ─────► OPEN-SM-7d
  OPEN-EW-1 (η) ─────────────────────────────────────► OPEN-G-2
  OPEN-EW-2 (masses) ──► OPEN-EW-4 (ratios) ─────────► OPEN-G-2

STANDARD MODEL:
  OPEN-SM-7 (K=2/3) ─► OPEN-SM-7d (θ) ──────────────► Lepton masses
  OPEN-SM-4 (Capotauro) ──► OPEN-SM-5 (PMNS) ───────► OPEN-G-2
  OPEN-SM-10-FEM ──► OPEN-SM-cage-1 (α=2.38) ────────► OPEN-SS-1

FOUNDATIONS:
  OPEN-SD-1 (K₀) ──► OPEN-SD-2 (interp.) ──► OPEN-SD-3 (A₅, A₃)

RELATIVITY:
  OPEN-SR-3 (SSV def) ──► OPEN-SR-1 (PSR) ──► OPEN-SR-4 (Einstein)
  OPEN-SR-2 (k) ──► OPEN-SR-1

CROSS-SERIES:
  OPEN-SD-lattice-scale ──────────────────────────────► All spatial predictions
```

---

# §9 — Problem Count Summary

| Sector | Total | Open | Conj | Prop | Resolved | Falsified |
|--------|-------|------|------|------|----------|-----------|
| FP (Flagship Papers) | 2 | 2 | 0 | 0 | 0 | 0 |
| SS (Strong) | 26 | 16 | 5 | 1 | 1 | 1 |
| SM (Standard Model) | 23 | 11 | 6 | 1 | 3 | 5 |
| EW (Electroweak) | 10 | 6 | 3 | 0 | 0 | 0 |
| QM (Quantum Mechanics) | 13 | 5 | 0 | 4 | 3 | 0 |
| SR (Relativity) | 8 | 8 | 0 | 0 | 0 | 0 |
| SD (Foundations) | 7 | 6 | 1 | 0 | 0 | 0 |
| GLOBAL | 2 | 2 | 0 | 0 | 0 | 0 |
| **Total** | **91** | **56** | **15** | **6** | **7** | **6** |

*(Note: Propositions counted only at Tier 2–3 level in this summary. Tier 4 items (10) grouped under PROP-6–15.)*

---

# §10 — Anomalies and Housekeeping Actions

The following issues were identified during the consolidation from `open_problems/` into this file and require action:

### Duplicate files (action: delete the stale copy)
1. **`open_problems/OP-EW/CONJ-SM-6_koide_phase.md`** — duplicate of `OP-SM/CONJ-SM-6_koide_phase.md`. The OP-SM copy has a dead-end correction the OP-EW copy lacks. **Keep OP-SM version; delete OP-EW copy.**
2. **`open_problems/OP-EW/CONJ-EW-1_weinberg_angle.md`** and **`CONJ-EW-1_weinberg_angle_zero_parameter.md`** — two versions of the same conjecture. The former (182 lines) is more complete. **Keep `weinberg_angle.md`; archive `zero_parameter.md`.**

### Misplaced files (action: move to correct location)
3. **`open_problems/OP-EW/development-EW-Weinberg-Koide-session-20260401.md`** — development transcript, not a problem file. **Move to `series_electroweak/development-transcripts/`.**
4. **`open_problems/OP-SS/OP-SS-1_quark_mass_ladder_ps1_analysis.md`** — a .tex paper, not an open problem. **Move to `series_strong/papers/`.**
5. **`open_problems/OPEN-P-SM-10-FEM.md`** — at root of open_problems instead of in OP-SM/. **Moot after archival; noted for record.**

### Naming convention (action: rename on Phase 5 archival)
6. All files in `open_problems/` use `OP-` or `OPEN-P-` prefixes. The new standard is `OPEN-`. Renaming will occur during Phase 5 (consolidation/archival), not now.

### Content absorbed from other files
7. **`propositions.md`** — Tier 1–3 items absorbed into §3 and §4. Tier 4 items referenced by group.
8. **`solution_candidates.md`** — SC-1 through SC-7 absorbed into relevant entries' "Current best lead" fields and the FALS section.
9. **Conjectures from `postulates_and_theorems.md`** — CONJ-SM-1 through CONJ-SM9-2, CONJ-EW-1, CONJ-EW-2, CONJ-SS-2-1 absorbed into §2.
10. **`open_problems/OP-SS/conjectures-SS.md`** — CJ-SS-1, CJ-SS-2, candidate postulate absorbed into §2.

---

*This file consolidates content from: `open_problems/` (63 files), `propositions.md`, `solution_candidates.md`, conjectures from `postulates_and_theorems.md`, and `open_problems/OP-SS/conjectures-SS.md`. No content has been deleted — all items are either in this file or referenced by it. The source files will be archived after verification (Phase 5).*

*Created 12 April 2026 during Phase 1 of the Research Frontier Architecture implementation.*
*Authors: Thomas Lee Abshier ND and Claude Opus (Anthropic).*
