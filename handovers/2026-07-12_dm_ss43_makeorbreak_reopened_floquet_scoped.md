# Handover — OPEN-SS-43 make-or-break: kill → reopened → inversion refuted → scoped as OPEN-DM-FLOQUET-1

**BLOCKING CLONE-FIRST GATE (line 1):** before registering any ID, placing any file, or computing any coefficient,
clone the repo and grep the registry. Skipping this caused the Session-146 misgrounding. Every action this handover
queues begins after the clone + registry grep.

**Canonical next-session kickoff line (paste this into a fresh window):**
> Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at
> https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE
> before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry
> first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named
> YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is
> handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated
> entry.

**Sort caution (earned twice now):** within a same-date group, alphabetical `ls | sort` misleads. This file is
dated 2026-07-12 to sort cleanly after the two 2026-07-11 files. If two files share a date, `git log` names the
true newest. **Warm-launch keyword: DM-WARM-2438.** HEAD should be Patch 2438.

---

## 1. One-paragraph state
Candidate (B) — the N=8 CDM-like closed ring, last survivor of the OPEN-SS-43 coring campaign — has its make-or-break
(κ_θ/E_bond ≥ 0.43) **UNRESOLVED**. This session took it through favorable → FALSIFIED → SURVIVES → REFUTED and
landed, correctly, on a scoped open computation: **OPEN-DM-FLOQUET-1** (the transverse charge-switched bending
eigenvalue on geometry #3). Candidate (B) is neither falsified (the kill's geometry was superseded) nor surviving
(the rescue was refuted by CONV-001). Ω_DM stays parked. Do NOT reopen the make-or-break with another cheap shortcut;
OPEN-DM-FLOQUET-1 pins the disciplined computation and its anti-bias guardrails.

## 2. The arc (patches 2426–2438), honestly
- **2426** — derived κ_θ/E_bond = 2R²/d² ≈ 0.74–1.5 on the founder Cross-Rod; E_bond validated 494 vs 490 keV.
  Favorable — but assumed ISOTROPIC dynamic stiffness (f_stiff = f_depth).
- **2427** — Kapitza test of that assumption, AXIAL mode: favorable. Later RETRACTED (wrong mode).
- **2428/2429** — CONV-001 #1: 1 VERIFIED + 4 caveats → "not-yet-falsified." Gemini (D): κ_θ is TRANSVERSE; by
  Laplace the transverse dynamic stiffness need not track the axial.
- **2430** — ponderomotive stiffness TENSOR strongly anisotropic + sign-indefinite (eig [−190,+173,+292]) →
  f_stiff ≠ f_depth → isotropic assumption REFUTED, favorable verdict withdrawn.
- **2431** — CLOSED (kill): founder gradient read (1835, far-out coat) + 2430 tensor + registered 0.345 → all
  < 0.43 → soft → light rings → LZ-excluded → FALSIFIED. (1811 #2 shown moot via 1836 ZBW-cancellation.)
- **2432** — registered (B) FALSIFIED (founder said "register B").
- **2433** — REOPENED (founder): the kill's geometry was wrong. Corrected **geometry #3**: uniform axial spacing;
  eCP coat at LARGER transverse radius R_e > r_q; **qCP core is JELLO** (no static bending integrity —
  superposition-rebound = Earnshaw). eCP coat sole bending resistance.
- **2434** — charge-switching rescue: κ_θ = δ·Σk_rep·x² → 2δ (deep branch) → 0.67 at δ=1/3 → STIFF. INVERTED the kill.
- **2435** — DM-lattice δ = 3/7 from 4+/4− cube neutrality (SS-1-C₃ analog), brute-forced, geometry-independent →
  2δ = 6/7 = 0.857 → survives at drifted mass (N≈12, ~17 GeV).
- **2436/2437** — CONV-001 #2: 2 REFUTED + 2 HOLD + 1 survives → 4/5 do-not-promote; 3/5 MOTIVATED REASONING.
  **Decisive error (GPT + Gemini, worker-verified):** 2434 kept only the same-charge (+curvature) fraction and
  DROPPED the (1−δ) opposite-charge (−curvature) fraction; honest average = (2δ−1)·2A/z³ = **−1/7 < 0** at δ=3/7
  (positive only for δ>1/2). 6/7 / N≈12 / 17 GeV WITHDRAWN. Worker accepted the refutation and the motivated-
  reasoning finding.
- **2438** — registered **OPEN-DM-FLOQUET-1** (scoping doc): the single blocking computation, 7 Required Elements +
  7 anti-bias guardrails G1–G7 + pre-registered sign commitment. Multi-session; no single-patch shortcut authorized.

## 3. Durable gains (survive the refutation — real, keep them)
- **Geometry #3** (founder-pinned): uniform axial d; eCP coat at larger transverse R_e > r_q (because E_ee < E_qq →
  eCP–qCP equilibrium farther out); qCP core jello; eCP–qCP–qCP–eCP diagonals; two planes, opposite polarity.
  This RETIRES the 2431 kill's lattice input — the kill is not reinstated.
- **δ = 3/7 = 0.4286** — the same-charge apposition fraction from the 8-qCP cube's 4+/4− neutrality, exact and
  geometry-independent. A UNIFORM-sampling UPPER BOUND, not the dynamical value.
- **The α_s/α ≈ 53 branch factor** — E_bond deep (E_qq) vs shallow (E_ee) differ by 53×; branch unresolved.
- **1811 #2 (ZBW amplitude/frequency) is MOOT** for the ratio (1836 cancellation) — do not re-derive it.

## 4. Lessons (why the shortcuts failed — read before the next attempt)
Four attempts, four failure modes, each now a guardrail in OPEN-DM-FLOQUET-1:
(1) isotropic f_stiff=f_depth [2426] → refuted by the anisotropic tensor [2430];
(2) far-out-coat soft gradient read [2431] → superseded by geometry #3;
(3) axial curvature for the transverse mode [2434] → G2;
(4) dropped the (1−δ) negative-curvature phase [2434] → G1; and the meta-failure: motivated reasoning toward the
founder's survival lean (3/5 seats), the pattern being "keep the favorable phase, drop the unfavorable, land on the
preferred answer." Running CONV-001 BEFORE promoting the registry is what caught it — keep that discipline.

## 5. Next-session work (default action)
**Primary:** OPEN-DM-FLOQUET-1 (`series_phenomena/cosmology/dark_matter/OPEN-DM-FLOQUET-1_scoping.md`) — the
transverse charge-switched bending eigenvalue on geometry #3. Read the scoping doc FIRST; it pins the 7 Required
Elements and G1–G7. Recommended method order: (a) reduced Floquet–Mathieu for the SIGN honestly (with G1–G7), then
(b) MD/kMC for the magnitude if (a) is favorable. This wants a FRESH, unrushed run against the guardrails — it was
explicitly deferred from this session to avoid a tired end-of-thread shortcut. Pre-registered sign commitment (G7)
is binding: a negative/sub-0.43 result is reported as fail/unresolved, not re-parametrized into survival.
**Alternative cleaner threads if the founder redirects:** the SF-2 δ_CP lane; or any non-DM frontier item. The DM
make-or-break is not urgent — it is correctly parked at UNRESOLVED with a disciplined spec.

## 6. Step A–H Completion Audit
- **Step A** (Tier 1 session log): N/A — long-arc campaign session; per-patch Tier 4 reasoning notes serve as the
  session record (§15.14 incremental cadence); this handover is the session-close state record.
- **Step B** (Tier 2 transcript): N/A — no transcript file produced this session.
- **Step C** (Tier 3 vignette): N/A — the arc §2 above is the curated vignette in the handover.
- **Step D** (Tier 4 reasoning): ✓ — `reasoning/2426.md, 2427.md, 2430.md, 2431.md, 2433.md, 2434.md, 2435.md`
  (verbatim, at-patch) + two CONV-001 adjudication docs (2429, 2437). Every physics patch bundled its reasoning.
- **Step E** (registries, per-registry audit):
  - `research_frontier.md` / `frontier_sectors/SS.md`: ✓ — OPEN-SS-43 CLOSE→REOPEN→UNRESOLVED updates; OPEN-DM-FLOQUET-1 registered.
  - `DM-CANDIDATE-B_N8_cdm_like_registration.md`: ✓ — FALSIFIED→REOPENED→UNRESOLVED banner + §6 record.
  - theorem-registry / axiom-registry / predictions / paper_catalog / master_glossary / methods_catalogue: N/A —
    no theorems, axioms, predictions, papers, terms, or new methods shipped (all attempts refuted/withdrawn).
  - organizational_frontier: N/A.
- **Step F** (reviewer artifacts): ✓ — two CONV-001 briefs (`conv001_2026-07_rungbond_ssv_makeorbreak_brief.md`,
  `conv001_2026-07_dm_inversion_brief.md`) + two returns-adjudications.
- **Step G** (protocol/OS updates): N/A — no OS/template changes.
- **Step H** (this handover document): ✓ — `handovers/2026-07-12_dm_ss43_makeorbreak_reopened_floquet_scoped.md`.

## 7. Repo state
HEAD = Patch 2438. All of 2426–2438 committed under Opus authorship. No uncommitted work. Candidate (B): UNRESOLVED.
Ω_DM: parked. OPEN-DM-FLOQUET-1: OPEN, blocking. Warm keyword: DM-WARM-2438.
