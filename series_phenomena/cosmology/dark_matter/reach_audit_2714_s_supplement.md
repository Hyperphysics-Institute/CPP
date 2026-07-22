# REACH-AUDIT-2714-S SUPPLEMENT — the semantic / historical / decision-lineage audit requested by two panel seats, EXECUTED: full-history token and phrase searches (3268 commits, unshallowed), current-tree phrase sweep outside the arc, held-paper and release-material citation sweep, and the Candidate (B) promotion-lineage dependency check — **result: one pre-2714 numeric coincidence and otherwise ZERO exposure; RA-3 = EMPTY SUSTAINED-WITH-SUPPLEMENT**

**Patch 2764, 22 July 2026 (same patch as the bundle returns
adjudication). All searches quoted below are reproducible verbatim
from a full clone. Scope disclosure: conversation-level exposure in
external paste channels and any uncommitted external draft are
un-auditable from the repository and are disclosed as out-of-scope;
the NOT-FOR-RELEASE banners (Patch 2369) have kept the DM papers
unreleased throughout the contamination window, bounding external
exposure.**

## §1 — Searches run and results

1. **Current tree, semantic aliases, outside the arc.**
   `grep -rln "septuply|20–26% below|20-26% below|1.461 ± 0.082|
   r_legacy|driven-equilibrium enhancement"` over all `*.md`,
   excluding `series_phenomena/cosmology/dark_matter/` (the arc's own
   records, where the terms legitimately live under their
   classifications) and `handovers/` (state records, retained
   verbatim by anti-erasure): **zero hits.**
2. **Cross-lane citation sweep.** `grep -rln "S4-E|S4-X|DRIVE-AUDIT|
   X3-LONG|X7-NSCAN"` over `flagship_papers/`, all six `series_*`
   trees (`*.md` + `*.tex`), `book_project/`,
   `programme_orientation.md`, `predictions.md`,
   `OSF_deposit_prep_2026-05-20.md`: **zero hits** — no lane, held
   paper, book chapter, orientation text, or release-prep material
   cites the arc by name or act.
3. **Full-history token search.** After `git fetch --unshallow`
   (3268 commits), `git log -S <token> -- ':!series_phenomena/
   cosmology/dark_matter' ':!handovers'` for tokens `septuply`,
   `1.461`, `driven-equilibrium enhancement`, `r_legacy`: **one hit**
   — Patch 1134 (SR-2 Phase 7A figures), where "1.461" appears inside
   an eccentric-orbit energy ledger. Patch 1134 predates Patch 2714
   by roughly four months and by ~1580 patches; it cannot be a
   descendant. Classified NUMERIC COINCIDENCE.
4. **Candidate (B) decision-lineage check.** `grep -ln "S4-E|S4-X|
   X3-LONG|DRIVE-AUDIT|septuply|2714"` over the promotion lineage
   (`conv001_2026-07_promotion_adjudication_panel_brief.md`,
   `conv001_2026-07_promotion_round_returns_adjudication.md`,
   `DM-CANDIDATE-B_N8_cdm_like_registration.md`,
   `dm_candidate_consistency_consolidation.md`): **zero hits** — the
   79.5% ledger contains no S4 support, confirming the 2759 table's
   positive genealogy at the decision-dependency level, not merely
   the numeric level.

## §2 — Ruling

The two seats' critique was correct in principle — a code census
alone cannot establish RA-3 = EMPTY — and is now discharged in fact:
the semantic, historical, cross-lane, and decision-lineage classes
they enumerated have been searched and are clean. **RA-3 = EMPTY is
SUSTAINED-WITH-SUPPLEMENT.** Residual un-auditable classes
(conversation-level, uncommitted external drafts) are disclosed, not
resolved; they are bounded by the release hold. If the outstanding
seat's return names a search class not covered here, it executes as
a rider to this supplement.

## §3 — Verification-package manifest (for the seat that could not access the repository)

`rv2714_verification_package.zip` (delivered by founder attachment;
not committed — data lives in-repo already) contains:
`code/2761_rv2714_execution.py` (includes the gate-v2
implementation), `code/2761_rv2714_x6_battery.py`,
`code/2762_rv2714_authentication.py`, `data/rv2714/` (five gzipped
per-sample chains), `data/bcheck80b/` (three ensembles),
`rv2714_reverification_prereg.md`, `rv2714_record.md`,
`s4x_bcheck80_prereg.md`, `s4x_bcheck80_gate_record.md`,
`s4x_bcheck80b_prereg.md`, `s4x_bcheck80b_record.md`,
`ENVIRONMENT.txt` (python/numpy/scipy versions), and a SHA-256
manifest of every file in the package (CONV-006 discipline applied
retroactively to this delivery).
