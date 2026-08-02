```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file (named YYYY-MM-DD_session_NNN_*.md) — that newest entry is the canonical "what's next" pointer. Note: the folder is handovers/ (plural) and there is no file named handover.md; never look for either — always use the newest dated entry.
```

# SESSION CLOSE — PATCHES 2917–2924: ROUND 2 EXECUTED, THE β⁰ CORE FOUND AND IDENTIFIED, TWO INSTRUMENT DEFECTS CAUGHT BY THEIR OWN FROZEN TRIPWIRES, AND THE TURNOVER REFUTED — THE DRIVE SUSTAINS THROUGH β = 0.30

## Orientation — read this first

**Session of 1 Aug 2026 (patches 2917–2924 + this close). Worker:
Claude, inheriting the 2900–2915 handover and the 2916 window pin.**
The hybrid pipeline ran its full arc — round 2, the β = 0 control,
rounds 3 and 3b, and the turnover test — and ended with the direct
instrument holding the record: **the substrate drive is sustained,
growing, and near-linear through β = 0.30; no drag, no turnover;
c_direct = +0.91 ± 2.40 with the static-Sea 1/5 comfortably inside
and every catastrophe (c ~ 16–20, turnover) dead as instrument
artifact.** The precision route to c is no longer compute (power wall
re-derived: σ_c 0.05 needs ~2000× legs) — it is analysis.

## §1 — WHAT'S NEXT (single pointer)

**The analytic derivation of c = 1/5 (and the c₄ = 7/240 candidate)
from the round-trip angular moments** — queued since Patch 2900,
"cheap, high value" then, now also the ONLY affordable route to the
static-channel precision verdict. Its confrontation target is frozen
and banked: the direct bound c = +0.91 ± 2.40 (16–84%: −1.5 .. +2.8),
`code/2924_direct_fit.py` + `data/2924_turnover_results.json` (all
paths relative to `flagship_papers/electromagnetism/`). Secondary
queue: OPEN-EW-ANTISCREEN-1 (founder-physics candidate), LINK 2,
OPEN-K1-MEMORY-1 (B7 gate), OPEN-HYB-SHAPE-1 (deprioritized).

## §2 — HEADLINE RESULTS

1. **ROUND 2 EXECUTED** (2917): 60 fresh legs at the 2916-pinned
   windows; corrected χ² gate FAILS 4/5 (real β-structure resolved at
   12-leg statistics); Stage 2 INCONCLUSIVE as frozen — and the
   diagnostics indict the (β, β³) basis: the pattern carries a
   **β-INDEPENDENT core** (~14× the linear part at β = 0.04).
2. **THE β⁰ CORE IDENTIFIED** (2918): β = 0 control at two windows —
   the core is a persistent static pattern (amplitude matches the
   frozen a₀ to 3%) plus an even, window-diluted transient. **Round
   1's "disparity ~0.4β" CORRECTED: it was dominantly the motionless
   pattern**; the true motion response is ~0.026β.
3. **COLLECTIVE ANTI-SCREENING DISCOVERED** (2918): the persistent
   pattern is polarization-reversed (+ leans toward the + source);
   isolated pair audits normal. Many-body physics, question OPEN
   (OPEN-EW-ANTISCREEN-1) — bears on the suspended statics rebuild.
4. **ROUND 3** (2919/2920): corrected basis pre-registered with
   data-blind conditioning (14.3); **adequacy gate PASSES** (1.419);
   the pre-registered exact-zero assert catches a **PARITY DEFECT in
   the shared Stage-2 evaluator present since 2914** (edge-landing
   cells read the pattern asymmetrically; kernel audits clean).
   Sixth instance of the inheriting-from-the-arc genus; caught in
   one turn because the invariant was FROZEN as an assert.
5. **ROUND 3b** (2921/2922): parity-clean evaluator (assert passes at
   4.3e-19); k_tot = +0.0120 ± 0.0016 lands in the thrice-validated
   band (the fix moved the answer TOWARD independent measurements);
   c_tot localized ~16 ± 3.4 → perturbative form declared inadequate
   per the frozen §4 commitment; 2σ cross-instrument tension with the
   direct 2910 drives isolated to the high-β regime.
6. **TURNOVER TEST — REFUTED DECISIVELY** (2923/2924): 12 direct
   pairs at β = 0.25 (M/SE +3.55) and β = 0.30 (**M/SE +9.00, the
   hybrid's drag prediction wrong by 12σ including sign**), 12/12
   positive. The hybrid's high-β shape is dead as evidence; mechanism
   OPEN-HYB-SHAPE-1 (prime suspect tested and killed — truncation
   fraction is flat in β).
7. **The direct five-β record** (2924): D/β = {12.0, 15.2, 13.8, 8.7,
   13.4}e-3 over β = {0.05..0.30}; c_direct = +0.91 ± 2.40, χ²/dof
   1.23; no drag onset anywhere; power wall re-derived for the direct
   method (~2000× legs to σ_c = 0.05).

## §3 — FOUNDER INTERACTION STATE

PD-006 in force throughout; founder actions this session were
mechanical applies only (2917, 2918, 2919, 2920–21, 2922–23, 2924 —
all applied and pushed); **no physics rulings were issued this
session ⟹ founders_voice captures N/A** (disclosed, not skipped).
One standing founder-physics question flagged in-chat for Thomas's
intuition: the anti-screening inversion (OPEN-EW-ANTISCREEN-1) —
no response required yet; registered.

## §4 — LEDGER (unchanged all session)

1B OPEN; PR7 PARTIAL (OPEN-K1-MEMORY-1); six of seven; **B7 holds
DM-1/2/3 release banners**; Candidate (B) 79.5%
PROVISIONAL-FAVORABLE. G1 and P-A2-1 stand. Statics suspension (2892)
stands — now with a mechanism lead (anti-screening). 7 July
no-carried-velocity ruling stands. CONJ-FP-1: A HOLDS, B CLOSED;
curvature bounded O(1) by the direct instrument, precision OPEN.

## §5 — ENVIRONMENT / PROCESS NOTES FOR THE NEXT WORKER

- Tool-call compute cap ≈ 300 s CONFIRMED HARD this session (one call
  killed at ~310 s mid-leg; leg-atomic appends made it lossless).
  Batch drivers use a ~170 s budget so the worst-case leg finishes
  under the cap.
- numba disk cache remains DISABLED; ~60 s JIT per process; batch
  many legs per python process (2917/2918/2924 drivers do, resumable).
- All raw legs are archived in-repo: `data/2917_round2_legs_raw.json`
  (60 mobile), `data/2918_control_legs_raw.json` (12 static),
  `data/2924_turnover_results.json` (12 pairs pooled). /tmp is
  scratch only; nothing verdict-relevant lives there.
- **Freeze literals AND invariants:** the 2916 window-literal lesson
  fired live (this worker independently mis-derived 3/5 windows from
  the ambiguous rule before the pin arrived), and its generalization
  (the frozen exact-zero assert) caught the 2914-era parity defect
  the same day. Both are now precedent.
- Commit hygiene held: every commit was format-patched and presented
  same-turn; every founder apply confirmed before the next commit.

## §6 — STEP A–H COMPLETION AUDIT (§15.11)

- **A (Tier 1 session log):** this handover per §4
  Session-Log-as-Handover-Backbone; patch-sequence narrative in §2. ✓
- **B (Tier 2 transcript map):** N/A — chat transcript not exported
  this session; per-patch reasoning fragments carry the pointer map.
- **C (Tier 3 vignettes):** N/A as separate file — substantive
  reasoning captured incrementally per §15.14(b) in per-patch Tier-4
  fragments (below); no SF-6 paper-content patches this session.
- **D (Tier 4 verbatim reasoning):** ✓ INCREMENTAL —
  `reasoning/2917.md` … `reasoning/2924.md`, one per patch, each
  bundled in its producing commit (§15.14(b) cadence).
- **E (registries, each audited):** `research_frontier.md` dashboard —
  ✓ updated this patch (EW line). `frontier_sectors/EW.md` — ✓ two
  entries added (OPEN-EW-ANTISCREEN-1, OPEN-HYB-SHAPE-1).
  theorem-registry — N/A (no theorems). axiom-registry — N/A.
  paper_catalog — N/A (no paper versions). predictions — N/A (no new
  zero-parameter predictions; the c = 1/5 target already registered
  at 2900). master_glossary — N/A. methods_catalogue — N/A after
  audit of Tier-4 entries: the session's methods (frozen-invariant
  asserts, β = 0 control design) are workflow/OS-scope per the Patch
  0461 scope test, recorded in §5 above and in the records, not
  catalog entries. organizational_frontier — N/A. future_projects —
  N/A. INDEX — N/A (no new top-level containers).
- **F (reviewer artifacts):** N/A — no panel cycle this session.
- **G (protocol/OS updates):** N/A — lessons recorded in patch
  records; no OS text changes required (the §15.15 audit below found
  the capture discipline held).
- **H (this document):** ✓ at the canonical location; kickoff line at
  top; chat reply echoes it per Patch 0728.

## §7 — §15.15 CAPTURE AUDIT

Physics/derivation patches 2917–2924: reasoning fragments present and
CONV-010-conformant for all 8 (per-patch, same-commit; stranger test
applied — each states the numbers, the chain, and the kill/keep
decisions). Verify scripts: committed same-patch for 2917 (×3), 2918
(×2), 2920, 2922, 2924 (driver). **Two inline-computation gaps found
and captured THIS patch** (same-session, producing window still
open): `code/2919_design_check.py` (data-blind conditioning) and
`code/2924_direct_fit.py` (five-β unbanded fit) — both marked as
same-session captures in their headers. Founder verbatim: none to
capture (no rulings issued; §3). Data-archive ↔ record-text match
spot-checked for 2917/2922/2924: exact.
