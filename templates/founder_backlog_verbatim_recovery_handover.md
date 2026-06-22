# HANDOVER — Verbatim Recovery of Founder Contributions (June multi-window backlog)

**Purpose:** a dedicated fresh window to recover, *verbatim*, the substantive founder (Thomas/TLA)
contributions from the intense June 2026 multi-window period that never reached `founders_vision.md`. Written
22 June 2026 (Patch 2036) at the close of the R2 arc. Worker recovers; TLA integrates.

---

## 0. Why this window exists

`founders_vision.md` had no entries between 11 June and 22 June despite an intensely interactive period across
~6 parallel windows (SF-7 synthesis, SF-1–6 flagships, §10 consistency theorems, the R2 vacuum-impedance
campaign, cosmology/LRDs, and more). Diagnosis (Patch 2034): founder contributions were captured only as
*paraphrase* inside worker reasoning fragments, never verbatim/attributed, with no promotion path. The
going-forward fix is the Reasoning-Capture Protocol **§10** (founder-contribution capture rides the per-patch
contract) + `templates/sweep_founder_contributions.sh`. This handover covers the **backlog**.

## 1. What is already done (do not redo)

- **Patch 2033** — the pivotal R2 contribution (Thomas's scalar-SSV argument, 22 Jun) is in
  `founders_vision.md` **verbatim**.
- **Patch 2035** — backlog *substance* recovered, marked **[reconstructed]** (paraphrase, NOT verbatim), for
  two contributions: (a) 15 Jun, "l_P is the baseline PSR not the Grid-Point spacing, environment-dependent"
  (cosmology 0733 + strong 1004); (b) 22 Jun, the DP-pinning mechanism that unblocked OPEN-SR-9 (R2 2016).
  **These two need their verbatim upgrade** — find Thomas's actual words and replace the [reconstructed]
  bodies (keep the dates/attribution; swap paraphrase → quote).

## 2. The mission

Recover, verbatim, the substantive TLA contributions from ~**1 June → 22 June 2026** (and spot-check back to
the last prior `founders_vision.md` entry if 11 June left gaps). "Substantive" = shaped a result: an insight,
mechanism, reframe, correction, or decision. Exclude routine instructions ("apply this", "proceed").

## 3. Method

1. **Retrieve the sessions.** Use `recent_chats` (paginate with `before`/`after` across the 1–22 June window;
   ≤20 per call, ~5 calls max per range) and `conversation_search` (topic keywords: "SF-7", "consistency
   theorem", "R2 impedance", "l_P grid spacing", "OPEN-SR-9", "matter power spectrum", "neutrino", "Capotauro",
   "δ_CP", etc.). These tools are the verbatim source; the repo only has paraphrase.
2. **Cross-index with the repo.** The committed `reasoning/` fragments name where TLA shaped a result (126
   fragments mention TLA/Thomas; most are boilerplate "integrator = Thomas" — filter for contribution-verbs:
   `grep -riE "TLA (supplied|pushed|proposed|corrected|argued|gave|caught|identified)|Thomas (pushed|supplied
   |proposed|corrected|argued)"`). Each genuine hit points to a session to pull the verbatim quote from.
3. **Extract verbatim.** For each, capture TLA's actual words (the load-bearing passage) + date + one-line
   context + the result it shaped.
4. **Promote** into `founders_vision.md` in the established entry form (dated header, attribution, verbatim
   blockquote, the resolution). Upgrade the two [reconstructed] entries from Patch 2035 in place.
5. **Capture as you go** under §10: this window's own patches must carry `## FOUNDER CONTRIBUTION (verbatim —
   TLA, <date>)` blocks; run `sweep_founder_contributions.sh` at the end to confirm zero orphans.

## 4. Known target list (seed — not exhaustive)

From memory + the repo, substantive TLA contributions likely needing verbatim capture include: the
*Tetrahedrons All the Way Down* framing (Margo coined it — capture attribution precisely); the multi-window
parallel-development protocol decisions; the A3′ Completed Broadcast Axiom (first axiom-level change);
the PCD-acronym correction ("Perceive, Compute, Displace"); the swarm-validation epistemology; and the
contributions already seeded in §1. Search the sessions; do not rely on this list being complete.

## 5. Environment, protocols, definition of done

- **Repo/worker rules/CONV-001/apply-chain:** unchanged — see `VTD-1_handover.md` §5 for the full statement
  (repo, container clone, owned greenfield paths, defer shared-registry edits to TLA, precautionary
  apply-and-push macro, verify clean apply before presenting). Patch band: confirm with TLA (parallel windows
  ⇒ disjoint band).
- **Canonical-file caution:** `founders_vision.md` is canonical; you are editing it heavily. Bundle promotions
  into reviewable patches; TLA integrates and confirms placement.
- **Done when:** every substantive TLA contribution in the window is in `founders_vision.md` verbatim
  (the two [reconstructed] entries upgraded; the seed list and search-discovered ones captured); the sweep
  reports zero orphans; and a short coverage note records the date-range swept and any sessions that could not
  be retrieved (honest gaps, not silent ones).

NO THEO. This is documentation recovery; it changes no physics. The point is fidelity to the founder's voice,
captured in his own words, with honest marking of anything that remains reconstructed.
