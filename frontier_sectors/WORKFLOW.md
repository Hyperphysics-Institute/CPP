<!--
  Extracted from Research_Frontier.md lines 1370-1384
  Source range: Workflow / Infrastructure
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Standing conventions (permanent — not "problems"; never cleared)

### CONV-023 — "turnaround": three senses, one convention

**Registered Patch 3203 (F-SW-10 R-5).** Full reasoning:
`series_relativity/audits/3203_fsw10_r5_turnaround_terminology_findings.md`.

| Sense | Referent | Rule |
|---|---|---|
| **A** | ZBW pair's stop-and-reverse at superposition (R-ARC-CANCEL-TURNAROUND, 3134) | **Must be qualified on first use** in any paper section — *ZBW turnaround*, *arc-cancel turnaround*, or an explicit superposition construction. Bare *turnaround* for this sense is not permitted in shipped prose. All current sites comply. |
| **B** | Relativistic trajectory reversal (twin paradox) | **Unqualified *turnaround* is correct and standard.** Do not "fix" it — it is the universal term in the SR literature and renaming it would read as an error to reviewers. |
| **C** | Elapsed project time ("24-hour turnaround", "reviewer turnaround") | **Out of scope permanently.** Ordinary English idiom, no collision risk. Excluded with prejudice; future sweeps must not re-raise it. |

**Note for future auditors:** R-2.5 initially recommended the opposite asymmetry
(qualify the relativistic sense, leave the ZBW sense bare). That recommendation
was examined and **reversed** at R-5. The principle established: a delta audit
keeps the corpus consistent with its own rulings; it does not impose
CPP-internal vocabulary onto terms that physics already owns.

### CONV-022 — Patch-number LANE RESERVATION for parallel campaigns

**Founder ruling, 16 Aug 2026 (Patch 3200).** When two campaigns run
concurrently on different machines, patch numbers are allocated by **reserved
integer block per lane**, not first-come. First allocation:

| Block | Lane | Note |
|---|---|---|
| 3100–3199 | **DE / cosmology lane** (VideoCPU: n=7, n=8 critical-FSS) | HEAD at reservation = 3144 |
| 3200– | **SR lane** (F-SW-10 delta audit and successors) | opens at 3200 |

**Why this and not alpha-suffix.** The existing collision discipline
(`operating_system.md` §16 item 7; `templates/paper_completion_checklist.md`;
Patch 0481M precedent) is *recovery* — it repairs a collision after two windows
have both claimed an integer. Lane reservation is *prevention*, and it is the
correct instrument when the concurrency is known in advance and machine-bound.
The two coexist: alpha-suffix continuation remains the recovery path for an
unforeseen collision **within** a lane. Reserving a block does not oblige a lane
to exhaust it; unused numbers in a closed lane's block are retired, not
reclaimed, so that patch number alone identifies the lane in `git log`.

**Rule for new lanes.** A new parallel campaign takes the next free hundred-block
at its launch patch, recorded by amending the table above in the same patch.

---

## Workflow / Infrastructure (WORKFLOW) — 6 problems

### OPEN-WORKFLOW-1: Consolidate All Bibliography Files
**Status:** OPEN
**Sector(s):** Infrastructure
**Priority:** MEDIUM
**One-line statement:** Merge all 12 per-paper and per-series `.bib` files into `bibliography/cpp_references.bib` as the single master bibliography; update old paper `.tex` files to reference it.
**What a solution looks like:** (1) Audit all 245 existing entries across 12 files; (2) resolve 22 known citation-key collisions (different content with same key); (3) merge 113 unique entries into master; (4) update `\bibliography{}` commands in all existing paper `.tex` files to reference master only; (5) move legacy `.bib` files to `archive/pre_consolidation_2026-04-15/`; (6) verify all papers still compile with same citation output.
**Tractability:** 1 dedicated session (2–3 hours of focused collision resolution and compile verification)
**Tooling (13 June 2026):** `scripts/consolidate_bibliography.sh` automates the per-paper consolidation **for local use** (needs working pdflatex+bibtex; not the container). It merges each per-paper bib's unique entries into the master (collisions keep the master entry), repoints the `.tex`, and converts a paper **only if** its BibTeX-generated `.bbl` is byte-identical before/after the repoint — proving the rendered bibliography (hence the OSF artifact) is unchanged. Papers whose `.bbl` changes (e.g. a self-citation where the master entry renders a trailing URL differently) are auto-reverted and flagged `[REVIEW]` for a manual accept-or-canonicalize decision. Per-series bibs (`cpp_*_series`, `gr_companion`, `references`) are deliberately excluded pending content-classification. Run `--dry-run` first; does not commit.
**What was done (15 April 2026):** Policy declared — master file is single source of truth; new papers cite master only; legacy files frozen with deprecation headers. SS-3 bibliography entries (cpp_ss3, humphreys1972) added to master. Stale `cpp_ss3` key in strong-series bibs renamed to `cpp_ss3_old_gluons` to free the namespace.
**What was done (13 June 2026 — SR-2 SHIP audit + gate hardening):** The SR-2 SHIP surfaced a *fresh* regression — a local `SR-2_references.bib` authored at draft time (Patch 1136) in violation of the 15-Apr policy — which the per-step checklist did not catch. Fixed: migrated to master + removed (Patch 1147); SR-2 is now the **first paper fully central-bib compliant at SHIP**. Hardened against recurrence (Patch 1149): OS §10 now states an explicit **BLOCKING SHIP GATE** precluding *creation* of any new per-paper/per-series `.bib`; paper-completion-checklist item **H7** added; `scripts/publication_audit.sh` now emits a `[FAIL]` (not advisory) for a paper's own local `.bib` or a `\bibliography{[ID]_references}` in its `.tex`.
**Current non-compliant inventory (13 June 2026 audit; remediation = this consolidation task):**
- Per-paper local bibs: `SR-1_references.bib`; `SM-6/7/8/9/10_references.bib` (6 papers).
- Stray master copy: `series_standard_model/papers/cpp_references.bib` (duplicate outside `bibliography/`).
- Per-series bibs cited in `.tex`: `cpp_ew_series` (EW-1..5), `cpp_strong_series` (SS-line), `cpp_qm_series` (QM-1..6), `cpp_foundations_series` (SD-1..5), `gr_companion` (c07 + GR companions), `references` (DP-Sea model).
- Compliant: SR-2 (and any future paper, enforced by the H7 gate).
**Collision classification (13 June 2026 audit — de-risks the consolidation):** The per-paper-bib key collisions with the master were sampled and are **benign / cosmetic, not "different content"** as the earlier "(2) resolve 22 known collisions" line feared. Every external-reference collision checked (`coxeter1973`, `pdg2024`, `koide1983`, `georgi1974`, `foot1994`, `rivero2005`, `humphreys1972`) is the **same reference** in legacy and master (identical titles); the diffs are whitespace / field-order / a trailing `\url{}`. Self-entry collisions (`abshier2026*`) are version/URL drift (e.g. master `abshier2026sr1` lacks the `\url{}` the SM-6 copy carries). **Implication:** repointing a paper to the master keeps the master entry (canonical) and renders the *same* bibliography. Unique-entry merge load (legacy keys absent from master): **SR-1 = 18**, SM-6 = 1, SM-8 = 1, SM-9 = 2, SM-7 = 0, SM-10 = 0; the stray `series_standard_model/papers/cpp_references.bib` = 31 entries, all already in master (unreferenced by any `.tex`), so removable. **Not yet classified:** the per-series bibs (`cpp_*_series`, `gr_companion`, `references`) — the documented "22 collisions" figure may live there; classify in the dedicated session.
**OSF re-deposit determination (13 June 2026):** A central-bib repoint that preserves rendered output does **not** require an OSF update. OSF versions track the scholarly artifact (the paper as read); the CPP convention ties re-deposit to mechanism/main-claim changes (paper-completion-checklist Completion Criterion), not internal build wiring. Because the sampled collisions are same-reference, the rendered bibliography is preserved (modulo trivial formatting like a stray URL — not a content revision). The only papers that would need an OSF touch are any where a *per-series* collision turns out to resolve a citation to a genuinely different work — which is exactly what the per-series classification (above) must confirm before that paper is repointed. Net: for SR-1 + SM-6..10, expected **no OSF re-deposit**; confirm per-paper at remediation by diffing the rendered reference list pre/post.
**Verification constraint:** step (6) "verify same citation output" requires a clean per-paper recompile; the container cannot reliably compile the legacy papers (SR-1's in-place compile truncated its PDF during the 1149 audit run), so the remediation must run on a machine where each paper compiles — i.e. the dedicated local session, not an in-container sweep.
**Paper(s):** None (infrastructure)
**Last updated:** 13 June 2026

---

### OPEN-WORKFLOW-2: Harmonize bibliography DOIs with actual OSF registrations
**Status:** OPEN (ACTIVE — worksheet handed to Isak, 13 June 2026)
**Sector(s):** Infrastructure / Publication
**Priority:** HIGH
**One-line statement:** The master bib asserts the *umbrella* project DOI `10.17605/OSF.IO/JXE8D` for 17 CPP self-citations (+2 in note) and no DOI for 12 — most are wrong, because CPP stopped using the single open registration (after a problem with it) and now registers most papers individually. Replace each entry's DOI with the paper's real OSF DOI; keep the umbrella only for the 6–8 genuine open-project files; for unregistered papers **strip** the wrong DOI and mark "deposit pending" (do **not** fabricate).
**Why it matters:** A wrong DOI is worse than none — it misdirects a reader/reviewer chasing a citation. For a validation-first programme, false provenance on shipped papers is a self-inflicted credibility wound. The 1153–1159 consolidation makes this fixable in **one file** (master) instead of 12 scattered bibs.
**What a solution looks like:** (1) fill `bibliography/doi_harmonization_worksheet.csv` (real DOI per `bib_key`; `Y` on the 6–8 open-project rows); (2) automate the join into master (Isak — Claude Code GitHub↔OSF method); (3) per the README rule: `REAL_DOI` → set `doi` + note `\url`; `KEEP_UMBRELLA=Y` → unchanged; both blank → strip DOI + note "deposit pending"; (4) re-run `scripts/publication_audit.sh <ID>` per paper.
**Artifacts (13 June 2026):** `doi_harmonization_worksheet.csv` (31 rows) + `DOI_HARMONIZATION_README.md`, handed to Isak.
**Paper(s):** All shipped CPP papers (DOI fields only)
**Last updated:** 13 June 2026

---

### OPEN-WORKFLOW-3: OSF-snapshot the theorem registry at each campaign close
**Status:** OPEN (locking mechanism to adopt)
**Sector(s):** Infrastructure / Publication
**Priority:** MEDIUM
**One-line statement:** Lock the registry-only theorems (those not proved inline in a shipped paper) by depositing a **versioned snapshot of `theorem-registry.md`** on OSF at each campaign close — citable as "THEO-X, CPP Theorem Registry v.Y, DOI…" — instead of promoting each theorem to a standalone companion paper.
**Background (load-bearing test, 13 June 2026):** Ran the promotion test across all 108 THEO ids. Only 13 have a standalone `.tex`; only 5 are referenced in a shipped paper — and **all 5 are proved *inline* in their own parent** (THEO-SR-EIN-1..4 inside SR-2; THEO-SM-5 inside SM-5), i.e. already published + OSF-frozen via the parent. **Zero theorems are both load-bearing and homeless**, so a per-theorem promotion campaign would only *duplicate* already-frozen content (two citable versions, divergent DOIs — strictly worse). The genuine gap is that the ~90 registry-only theorems aren't themselves snapshotted.
**What a solution looks like:** (1) set cadence = each campaign close; (2) deposit `theorem-registry.md` as a versioned OSF document (one DOI); (3) adopt the "THEO-X, Registry v.Y, DOI" citation form; (4) add a registry-snapshot step to the §15 session-/campaign-close protocol.
**Paper(s):** None (registry artifact)
**Last updated:** 13 June 2026

---

### OPEN-WORKFLOW-4: Chirality companion series (publish-time task)
**Status:** OPEN (deferred to chirality-arc publication)
**Sector(s):** Substrate Chirality Arc / Publication
**Priority:** LOW (until the arc ships)
**One-line statement:** The 11 chirality-arc theorems (`THEO-CHIR-*` + `THEO-CAP-1`) already exist as standalone `theo_chir_*.tex` documents but are cited in no shipped paper (they're internal to the as-yet-unshipped chirality arc). When that arc reaches publication, register them as the **chirality companion series** — one series registration / DOI, mirroring the ~20-paper SR-companion model — and add master bib entries.
**Background:** Surfaced by the 13 June 2026 load-bearing test as the only theorem cluster with standalone documents but no shipped-paper home. They are already written, so promotion is a registration + bib-entry job, not a writing job — hence deferrable to publish time with no rot.
**What a solution looks like:** at chirality-arc publication — (1) one OSF companion-series registration; (2) master bib entries (deposit-pending until registered); (3) remap any internal citations to the canonical keys.
**Paper(s):** Substrate chirality arc (companion set)
**Last updated:** 13 June 2026

---


---

### OPEN-WORKFLOW-1 — Session 1152 findings (bibliography consolidation, attempt 2)

**Context.** Re-attempt of the per-paper-bib → master consolidation after the
Session-1151 live run (commit `3911b39`) was reverted (`0c497b4`). The first run
failed every paper (3×SKIP, 3×REVERT) and zeroed two committed PDFs; revert
restored all. Root-causing the failures surfaced several findings independent of
the bib task itself.

**Script bugs fixed (consolidate_bibliography.sh v2, commit `9a53a62`):**
- *Backslash repoint path* — `os.path.relpath` on Windows emitted
  `..\..\bibliography\cpp_references`; LaTeX read `\b`,`\c` as escapes → bibtex
  never found master → recompile failed → false REVERT (SM-7/8/9). Fixed:
  force forward slashes.
- *Brittle baseline compile* — `-halt-on-error` on a cold first pass (no
  `.aux`/`.bbl`) returned non-zero on healthy papers → false SKIP. Fixed: no
  halt-on-error, two pdflatex passes, judge on `.bbl` production not exit code.
- *CRLF in `.bbl` diff* — MiKTeX CRLF output would read as a change vs an LF
  baseline → latent false REVIEW. Fixed: normalize line endings before compare.

**Repo-health findings (not bib-related; surfaced by the failures):**
- **`.gitignore *.pdf` blocks figure PDFs repo-wide.** Papers whose `.tex` does
  `\includegraphics{...pdf}` cannot compile from a clean clone — the figure PDFs
  are build artifacts, never committed (only SVG+PNG are). SM-6 was the tripwire;
  this is a *systemic* reproducibility gap affecting any PDF-figure paper.
  Fix pattern established (Option A, commit `19b4ac1`): commit a `build_figures.sh`
  in the figure dir that regenerates PDFs from committed SVGs via cairosvg;
  figure PDFs stay ignored. Reusable for other papers as the same issue is found.
- **SR-1 latent cold-compile bug** (commit `037e1e3`): line 1512 had escaped
  underscores in two `\ref` keys → `Missing \endcsname` fatal. Shipped PDF had
  been built from a state that no longer compiled cold (source/artifact drift).
- **SM-10 original SKIP was a false negative** — compiles clean cold, no repair
  needed; only the script bugs blocked it.

**OSF re-deposit pending** (rendered artifact changed vs deposit):
- SR-1 — 47→50 pp after the `\ref` fix (broken refs now resolve).
- SM-6 — rebuilt 16 pp with real (previously-missing) figures.
- (Bib repoint, when run, requires NO re-deposit — `.bbl`-identity by design.)

**State at note time:** three `1152` commits staged locally on `0c497b4`; bib
consolidation itself NOT yet re-run (pending `--only SM-10` validation of v2).

---

### OPEN-WORKFLOW-1 — Session 1152 addendum: SM-7/8/9 PARKED (master-bib content reconciliation needed)

**Where consolidation stopped and why.** SM-10 consolidated cleanly (commit
`c97b76d`). Extending to SM-7/8/9 surfaced that the master bib diverges from the
per-paper bibs in **three independent content classes**, varying entry-by-entry —
so a mechanical repoint would silently degrade shipped bibliographies. This is no
longer a consolidation task; it is a **reference-data reconciliation audit**, and
is parked for a dedicated session with the source-paper `.tex` titles/CHANGELOGs
open for adjudication.

**The three divergence classes found:**
1. **Version drift** (self-citation `note` versions). FIXED in master this session
   (commit `2d220f1`): SM-6 v2.1→v3, SM-10 v0.1→v2.0. Authority = each paper's own
   CHANGELOG. Other master SM entries already correct (SM-3 v6, SM-8 v4.1, SM-9 v2.2).
2. **URL/DOI completeness.** Master entries are MISSING `\url{...}` DOI links that
   the per-paper bibs carry (seen in SM-7's `[REVIEW]`: master drops the OSF DOI on
   abshier2026sm6/sm2 and a PhysRevLett.32.438 URL). Repoint-to-master would lose links.
3. **Title divergence (same key, different title).** `abshier2026sm2` (SM-2):
   - SM-7 local bib: "Mass Generation from Geometric Hierarchies"
   - master:         "Quark Mass Formula and Hybrid Spectral Structure"
   Substantive, not formatting. Authority = SM-2's own `.tex` title (UNRESOLVED —
   needs a look at SM-2_*.tex).

**Known-stale per-paper bib entries (will be corrected BY repointing to a
reconciled master, once master is made a correct superset):**
- SR-1 / SM-6 / SM-8 local bibs say SM-3 v5 (true: v6).
- SM-8 / SM-9 local bibs say SM-10 v1.0 (true: v2.0).
- SM-9 local bib says SM-9 v1.0 (true: v2.2) — stale about its own paper.

**Method limitation recorded.** The `.bbl`-byte-identity check proves "rendering
unchanged after repoint," NOT "rendering is correct." SM-10 passed only because its
local bib and master happened to agree on what SM-10 cites; it does not certify
those shared values are right. Reconciliation must validate against source `.tex`,
not against `.bbl` identity.

**Next-session task list (OPEN-WORKFLOW-1):**
1. Make master bib a correct superset: resolve SM-2 title vs SM-2.tex; restore the
   missing `\url{}` DOI fields; re-verify all self-citation versions vs CHANGELOGs.
2. Re-run consolidation SM-7 → SM-8 → SM-9 against the reconciled master; expect
   `[REVIEW]` to clear to loss-free `[OK]` (or accept changes that are pure
   corrections, manually repoint+archive).
3. Consolidate SR-1 and SM-6 (bibs still local; both now compile cold).
4. OSF re-deposit: SR-1 (47→50 pp), SM-6 (figures restored). 
5. Confirm SM-8 current version (header says v4.0; decided v4.1 — verify in CHANGELOG).

**Banked & committed this session (commits `9a53a62`→`2d220f1`):** script v3
(2 bug fixes, validated); SM-10 consolidated; SR-1 typo repair; SM-6 figure
build-script (Option A); master version-drift correction; this documentation.
1151 failed run honestly reverted (`0c497b4`). Tree clean at park.

---

### OPEN-WORKFLOW-1 — Session 1153: master-bib reconciliation, Task-1 actions A–C DONE

**Scope.** Executed the parked "make master a correct superset" reconciliation
against **source-`.tex` authority** (not `.bbl` identity). Re-audited the
divergence map; it is smaller than the 1152 park feared, and one flagged hazard
was a false alarm.

**`ss2` "title landmine" DEFUSED (false alarm).** The 1152 park warned that
master `abshier2026ss2` ("Lattice-Scale Grounding / Nucleon Structure," = SS-2)
vs the SM-8/SM-9 local-bib `abshier2026ss2` ("SU(3) Colour Algebra," = now SS-3's
content) would silently change a citation on repoint. **Neither SM-8 nor SM-9
actually `\cite`s `ss2`** — the stale entry never enters their `.bbl`. Dead weight,
not a hazard. (Actual SM-8 self-cites: sm3, sm6, sm7. SM-9: sm10, sm8, sm9v1.)

**Three master-bib actions committed (authority-resolved):**
- **A. Title fix** — `abshier2026sm2`: master "Quark Mass Formula and Hybrid
  Spectral Structure" → **"Mass Generation from Geometric Hierarchies"** (authority:
  `SM-2_mass_generation_geometric_hierarchies.tex` `\title` + filename; SM-7's
  local bib already carried the correct title). Master was the wrong one.
- **B. Add `abshier2026sm7`** (was MISSING from master; cited by SM-8). Title from
  SM-7.tex authority: "The Heavy Quark Mass Spectrum and Strong Coupling from
  600-Cell Lattice Geometry"; v2.2 (SM-7.tex CHANGELOG, 3 Apr 2026); OSF DOI.
  Placed in the older `@misc`+DOI family next to sm1–6 (contemporaneous v2.2 paper).
- **C. Add `abshier2026sm9v1`** (was MISSING; SM-9 deliberately self-cites its own
  v1.0 at line 127 — "SM-9 v1.0 investigated the origin of…"). Historical entry,
  title "The Quark Mass Scaling Exponent: Constraints, Negative Results, and Open
  Problems"; placed in the newer `@article` family beside sm9/sm10.

**Version re-verify (Task-1 sub-item) — CLEAN.** Confirmed against CHANGELOGs:
sm2 v30 ✓, sm3 v6 ✓, sm8 v4.1 ✓, sm9 v2.2 ✓ (sm6 v3 / sm10 v2.0 already fixed at
1152). Master self-citation versions are now correct.

**Post-A–C resolution check:** every self-cite key the parked papers render now
resolves uniquely in master — SM-6 {ew1,qm1,sm1,sm3,sr1,ss1}; SM-7 {sm2,sm6,ss1};
SM-8 {sm3,sm6,sm7}; SM-9 {sm10,sm8,sm9v1}; SR-1 = no self-cites (18 external
unique, mechanical merge). Master = 65 → 67 entries; no duplicate keys.

**Still open under Task 1 (deferred this session):**
- **D. DOI/URL parity** on the newer `@article` block (sm8/sm9/sm9v1/sm10, ss2–8)
  — they carry no `doi` field while the older `@misc` block does. NOT a blocker for
  the cited-key sets above (SM-8/9 render correctly as-is); decide as a deliberate
  normalization pass, not entangled with A–C.
- Task 5 SM-8 version: header v4.0 vs decided v4.1 — master note already says v4.1;
  confirm the `.tex` header at consolidation time.

**Next:** re-run consolidation SM-7 → SM-8 → SM-9 against the now-reconciled master
(Task 2; expect pure-correction `[REVIEW]`s — e.g. SM-8's sm3/sm6 gain the master
DOI — accept + repoint + archive), then SR-1 + SM-6 (Task 3), then OSF re-deposits
(Task 4: SR-1 47→50pp, SM-6 figures). Consolidation steps need a local machine with
working pdflatex+bibtex (container cannot reliably compile the legacy papers).

---

### OPEN-WORKFLOW-1 — Session 1154: master rendering-fidelity pass (Task-1 "restore \url{}" + title-case)

**Why.** The 1153 dry-run + live `--only SM-6,SM-7,SM-8,SM-9` produced the first
real `.bbl` diffs. They showed the master `@misc` self-block is NOT a rendering
superset under `plainnat`: (i) the OSF link lives in a `doi={}` field that this
plainnat does NOT render, so the local bibs (which carry it as `\url{}` in `note`)
render the link and a repoint-to-master would DROP it — a regression; (ii) old-block
titles are single-braced, so plainnat lowercases them ("the charged lepton…"),
degrading SM-8 whose local entries are double-braced (case-preserved).

**Fix applied (this patch).** For the 9 cited old-block self-entries (`ew1, qm1,
sm1, sm2, sm3, sm6, sm7, ss1, sr1`): appended `\url{https://doi.org/10.17605/OSF.IO/JXE8D}`
into `note` (byte-matching the local-bib form that is proven to render) and
double-brace-protected the title (canonical Titlecase; matches the newer `@article`
block; preserves SM-8). For the external `georgi1974` (Georgi–Glashow PRL 32, 438,
cited by SM-7): added `\url{https://doi.org/10.1103/PhysRevLett.32.438}` to `note`.
`doi={}` fields retained (harmless; future-proof if natbib DOI rendering is enabled).
Brace-balanced; notes verbatim-match the locals so URL renders are identical.

**HARD CONSTRAINT MET: no URL lost anywhere.** Every repoint now ADDS or PRESERVES
links; none drops one.

**Cascade manifest (papers whose master-rendered bib changes):**
- Parked, consolidating: SM-6, SM-7, SM-8, SM-9 — gain URLs / proper title case /
  version corrections. No loss.
- Already-compliant cascade: **SM-3 only** (cites `sm1`,`ss1` from master) — gains
  OSF URL + Titlecase on those two refs. Cosmetic.
- Unchanged: SR-2 (externals only), SM-10, SS-8, DSL flagship (cite master but none
  of the touched keys).
- OSF: per the recorded CPP convention (re-deposit ties to mechanism/main-claim
  change, not reference-list cosmetics), these URL-additions + case-fixes are
  **not** re-deposit triggers; architect confirms per paper by eyeballing the diff.

**Predicted post-fidelity consolidation outcomes (re-run `--only SM-6,SM-7,SM-8,SM-9`):**
- SM-7 → `[REVIEW]` = title-case upgrade ONLY (URL-loss cured; notes now identical).
  No longer a regression — a clean improvement to accept.
- SM-8 → `[REVIEW]` = enrichment (gains URL + version-note; case already matched).
- SM-6 → `[REVIEW]` = title-case + sm3 v5→v6 + fuller sr1 title (corrections).
- SM-9 → `[REVIEW]` = sm10 v1.0→v2.0 correction + journal/note format (no URL involved).
- None lose a URL; all are accept-as-correction. The clean `[OK]` auto-path is
  exhausted for these papers (their local bibs are each individually incomplete vs
  a canonical master) — that is expected, not a fault.

**Next:** (2) accept the four consolidations (manual repoint+archive, or build
script v4 `--accept-review ID[,ID]` to apply a reviewed `[REVIEW]` instead of
reverting); (3) SR-1 key-remap (legacy `abshier_sm1/_ss1/_sm3` → `abshier2026*`,
then merge only the genuine externals + `abshier_tnsr1` + `abshier2025`); (4) OSF
re-deposits SR-1 (47→50pp) + SM-6 (figures). D (DOI parity on newer `@article`
block) remains optional/cosmetic.

---

### OPEN-WORKFLOW-1 — Session 1155: consolidate_bibliography.sh v4 (operator-accept + clean-tree)

**Built (this patch).** v4 adds `--accept-review ID[,ID]`: when Phase 2 finds a
paper's rendered `.bbl` CHANGED (a `[REVIEW]`), for a named ID it KEEPS the repoint
and archives the legacy bib (operator-approved correction) instead of reverting; the
diff is still printed first. This unblocks the parked SM-6/7/8/9, which post-fidelity
are all accept-as-correction `[REVIEW]`s (the clean auto-`[OK]` path is exhausted for
them). Also FIX C: `restore_pdf` (git checkout) on every SKIP/ERROR/REVERT/REVIEW-
revert path — pdflatex rewrites the PDF non-deterministically each compile, which was
the source of the uncommittable `*.pdf` residue a non-converting run left behind; only
accepted/`[OK]` papers now keep their rebuilt-against-master PDF.

**Validated in-container:** `bash -n` syntax, `--help` (v4 usage), accept-review
case-match logic (only listed IDs accept; empty list never accepts). The compile-
dependent archive/repoint + restore_pdf paths mirror the validated `[OK]` path but
need a local pdflatex run to confirm end-to-end (as with v2/v3).

**Operator workflow (local):**
1. `bash scripts/consolidate_bibliography.sh --only SM-6,SM-7,SM-8,SM-9` — eyeball each `[REVIEW]` diff (confirm correction/enrichment, no URL loss).
2. `bash scripts/consolidate_bibliography.sh --accept-review SM-6,SM-7,SM-8,SM-9` — applies: repoints .tex, archives the 4 local bibs, merges `ma2001` (SM-6), rebuilds PDFs against master.
3. `git diff` review → `bash scripts/publication_audit.sh <ID>` per paper → commit.
4. OSF: reference-list cosmetics need no re-deposit per convention; SM-6 still owes a re-deposit for the restored figures (separate, from 1152).

**Then:** SR-1 key-remap (legacy `abshier_sm1/_ss1/_sm3` → `abshier2026*`; merge only the genuine externals + `abshier_tnsr1` + `abshier2025`).

---

### OPEN-WORKFLOW-1 — Session 1156: SR-1 bib cleanup (was mis-scoped as "key remap")

**Correction to the 1154/1155 next-step.** The parked plan called SR-1 a "self-cite
key remap" (legacy `abshier_sm1/_ss1/_sm3` → `abshier2026*` in the `.tex`). On
inspection SR-1.tex does NOT cite those legacy keys at all — they are **uncited dead
entries** in `SR-1_references.bib`. So no `.tex` edit is needed; the fix is to strip
the dead entries so the script's Phase-1 (which merges by bib key, not by citation)
doesn't pull duplicates/orphans into master.

**SR-1 actually cites 13 keys** (all resolve): `abshier2025` + 12 externals
(`bailey1977, bannai1979, conway1988, coxeter1973, einstein1905, humphreys1990,
michelson1887, penrose1971, planck1900, thooft2016, unruh1976, weyl1946`). Of these,
only `coxeter1973` is already in master; the other 12 are unique → Phase-1 merges them.

**Removed 6 uncited dead entries from `SR-1_references.bib` (this patch):**
- `abshier_ss1`, `abshier_sm1`, `abshier_sm3` — duplicate self-cites (master has
  `abshier2026ss1/sm1/sm3`; the local copies were also stale, e.g. SM-3 v5 vs v6).
  Removing prevents different-key duplicate corruption of master.
- `abshier_tnsr1` ("Holographic Vacuum Energy Suppression") — orphan, uncited, not in
  master.
- `lorentz1904`, `minkowski1908` — genuine foundational SR externals but **uncited by
  SR-1**. Removed as hygiene. *Flagged to architect:* if these should live in master
  for future SR papers, add them deliberately (not as an SR-1 consolidation side-effect).

No change to SR-1's rendered `.bbl` (all removed entries were uncited) → no OSF impact.
Brace-balanced; 13 cited keys remain.

**SR-1 now ready for consolidation:**
`bash scripts/consolidate_bibliography.sh --only SR-1` (review) then
`--accept-review SR-1` (apply). Expected: Phase-1 merges 12 unique externals +
`abshier2025`; the `.bbl` diff should be empty or limited to `coxeter1973` (the only
pre-existing master collision) → likely clean `[OK]` or a tiny accept.

**Remaining OPEN-WORKFLOW-1 after the SM + SR-1 consolidations land:** per-series bibs
(`cpp_ew_series`, `cpp_strong_series`, `cpp_qm_series`, `cpp_foundations_series`,
`gr_companion`, `references`) still unclassified/unconsolidated; OSF re-deposits
SR-1 (47→50pp) + SM-6 (figures). D (DOI parity on newer `@article` block) optional.

---

### OPEN-WORKFLOW-1 — Session 1157: fidelity-2 (SM-6 external URLs) + workflow findings from first live accept attempt

**First live `--only` run (architect, local) — findings.** Ran `--only SM-6,SM-7,SM-8,SM-9`
(review) then tried `--accept-review` on the same. Three things surfaced:

1. **SM-6 external URL loss (FIXED here).** Beyond the 9 self-cites covered by 1154,
   SM-6 cites four externals whose master entries lacked the `\url{}`/arXiv `note` its
   local bib carries: `foot1994` (arXiv:hep-ph/9402242), `rivero2005` (arXiv:hep-ph/0505220),
   `koide1983` (\url PhysRevD.28.252), `pdg2024` (\url PhysRevD.110.030001). Repoint
   dropped them. This patch adds those four `note` fields to master, verbatim-matching
   the local form. SM-6 now loses no URL. (SM-7's only external `georgi1974` was already
   fixed at 1154; SM-8/SM-9 cite only self-entries and GAIN URLs — all three were already
   URL-safe, confirmed by their diffs.)

2. **Two-pass workflow self-blocks.** The `--only` "review" pass is NOT read-only — its
   Phase 1 merges unique entries into master, dirtying the tree, so the following
   `--accept-review` pass fails its clean-tree preflight. **Correct usage: run
   `--accept-review ID[,ID]` DIRECTLY** — it prints each diff *then* applies, so a
   separate review pass is unnecessary and harmful. (Or commit the Phase-1 merge first.)

3. **Phase 1 merges uncited dead bib keys.** `ma2001` (an uncited dead entry in SM-6's
   bib — SM-6 does not cite it) was merged into master as a unique key and then committed
   (local commit `7df1b8f`, mislabeled "consolidate…", nothing actually consolidated).
   It is an orphan in master. Other dead entries (SM-7 koide/pdg; SM-8/9 various) are
   already in master so Phase 1 skips them and they don't render — harmless, no action.
   Recommended: drop the mislabeled `7df1b8f` (reset to origin) so `ma2001` leaves master,
   OR remove `ma2001` forward; it is uncited either way.

**Post-1157 accept readiness:** SM-7, SM-8, SM-9 = URL-safe accept-as-correction NOW.
SM-6 = URL-safe after this patch. SR-1 (post-1156 cleanup) ready on its own run.
All four SM diffs are improvements/corrections (Titlecase + version fixes), no URL loss.

**Corrected operator sequence (clean tree):**
`bash scripts/consolidate_bibliography.sh --accept-review SM-6,SM-7,SM-8,SM-9`  (prints diffs + applies)
then review `git diff`, `publication_audit.sh <ID>` per paper, commit; repeat `--accept-review SR-1`.

---

### OPEN-WORKFLOW-1 — Session 1158: per-PAPER consolidation COMPLETE; per-SERIES scoped + classified

**MILESTONE — per-paper bibs fully consolidated to central master (commit `73fe66a`).**
One `--accept-review SR-1,SM-6..9` pass (v4) landed all remaining per-paper bibs:
- **SR-1 → `[OK]`** (rendered `.bbl` byte-identical post-1156 cleanup; no re-deposit).
- **SM-6/7/8/9 → `[ACCEPTED-REVIEW]`** (Titlecase + version corrections; **no URL lost** —
  1154 self-cite + 1157 SM-6-external fidelity passes confirmed in the diffs).
- 5 legacy `_references.bib` renamed into `archive/pre_consolidation_2026-04-15/`; master
  +122 lines (SR-1 ×12 externals + `ma2001`); 5 `.tex` repointed; all five `publication_audit.sh`
  = full `[PASS]`. With SM-10 (1152), **every per-paper bib (SR-1 + SM-6..10) is now central.**
- *Record-keeping note:* `73fe66a`'s message reads "consolidate SM-6..9" (the `11xx`
  placeholder) and omits SR-1, which was consolidated in the same pass; left as-is (pushed —
  not worth a history-rewriting amend). This note is the accurate record.
- OSF: SM-7/8/9 reference-list cosmetics → no re-deposit. SR-1 (47→50pp `\ref` fix) + SM-6
  (figures) re-deposits were already owed from 1152; this pass added nothing to that.

**Remaining OPEN-WORKFLOW-1 scope = the per-SERIES bibs only.** Five live + a strong-series
tangle. Classification audit (this session, read-only) — de-risks the consolidation:

| series bib | entries | collisions w/ master | unique→merge | self-key flags |
|---|---|---|---|---|
| `cpp_ew_series` (EW-1..5) | 20 | 0 | 20 | none |
| `cpp_strong_series` (SS-1) | 31 | 1 benign | 30 | `abshier_sr` = **DUP of abshier2026sr1** |
| `cpp_qm_series` (QM-1..6) | 40 | 2 benign | 38 | `abshier2026c1..c6` = genuine new (QM sub-papers) |
| `cpp_foundations_series` (SD-1..5) | 27 | 2 benign | 25 | `abshier_sr` = **DUP of abshier2026sr1** |
| `gr_companion` (c07) | 51 | 2 benign | 49 | `abshier2026sr` = **DUP of abshier2026sr1**; 9 genuine GR-companion self-keys (am/born/gr/grav/mass/series/stiff/swarm/zdc) |

**Key results:** (i) **ZERO genuine-content collisions** — every master-collision is benign
same-title (the long-feared "22 different-content collisions" does not exist here, mirroring
the per-paper finding). (ii) ~162 unique entries would merge (mostly real external refs not
yet central — a large but legitimate master enrichment). (iii) **Self-key dedup needed before
merge** (same lesson as SR-1): `abshier_sr` (strong + foundations) and `abshier2026sr` (GR) all
mean SR-1 → remap citing `.tex` to `abshier2026sr1` + drop the dupes, do NOT blind-merge.
`abshier2026series`/`abshier2026c*`/GR-companions are genuine new papers → merge (consider
giving them canonical `abshier2026*` keys). (iv) **Strong-series file tangle:**
`series_strong/cpp_strong_series.bib` (31, 1 citer) and `series_strong/papers/cpp_strong_series.bib`
(33, 1 citer) are both live; `cpp_strong_series_papers.bib` (33) and `cpp_strong_series_root.bib`
(31) have **0 citers (stale → removable)**. Untangle which of the two live files SS-1 actually
resolves before consolidating.

**Per-series consolidation plan (next session, local compile):** (1) resolve the 3 SR-1 dup
self-keys (remap `.tex` + drop); (2) classify/canonicalize the genuine new self-keys (c*, GR
companions, series); (3) untangle + dedupe the 4 strong bibs (remove 2 stale); (4) merge uniques
into master (fidelity: ensure url-in-note + Titlecase parity so multi-paper repoints don't lose
links — same pattern as 1154/1157, applied across EW-1..5 / QM-1..6 / SD-1..5 / c07); (5) run
v4 `--accept-review` per series (the script currently scans only `series_relativity/papers` +
`series_standard_model/papers` — extend its find roots to cover EW/QM/SD/strong/GR dirs).

---

### OPEN-WORKFLOW-1 — Session 1159: per-series tanglement risk assessed; gate blind-spot closed + dead files removed

**Question answered (does deferring per-series consolidation risk future tanglement?):**
Active spread risk is LOW — only **SS-1** still cites a per-series bib (`cpp_strong_series`);
SS-8 already went central; SS-2..7/9 and SS-1a..e use inline/no bib. The per-series pattern
is static, not metastasizing. BUT one real growth vector existed: the `publication_audit.sh`
bib-compliance gate `[FAIL]`'d on per-PAPER bibs only and was **blind to per-SERIES bibs**, so a
future paper copying SS-1's `\bibliography{cpp_strong_series}` preamble would silently re-adopt
the deprecated pattern and still PASS. Two cheap fixes (this patch, no compile) convert that
latent risk into structural prevention:

1. **Gate blind-spot CLOSED.** `publication_audit.sh` now basename-matches the bibliography
   target: `cpp_references` = PASS (central); `cpp_*_series` / `gr_companion` / `references` =
   `[FAIL]` (per-series, OS §10 central-only). Central bib is never false-flagged. Validated:
   SS-1/EW-1/QM-1 → FAIL (caught); SM-6/SR-1 → PASS. **Expected consequence:** the audit now
   flags every not-yet-consolidated per-series paper (SS-1, EW-1..5, QM-1..6, SD-1..5, c07) —
   intended, keeps them visible until the per-series consolidation lands.

2. **3 dead-weight strong bibs REMOVED** (0 citers, no live content): `series_strong/cpp_strong_series.bib`
   (exact subset/dupe of the live `papers/` copy), `cpp_strong_series_papers.bib` +
   `cpp_strong_series_root.bib` (contained only the deprecated `cpp_ss3_old_gluons` tombstone).
   The strong-series tangle is now a single live file: `series_strong/papers/cpp_strong_series.bib`
   (cited by SS-1). The 4-file naming trap is resolved; the SS-1→central repoint remains the only
   strong-series consolidation step (deferred, needs local compile).

**Net:** the per-series consolidation can be safely deferred — new accretion is now gate-blocked,
and the strong-series file confusion is cleared. Remaining per-series work unchanged (merge
EW/QM/SD/GR/strong uniques + the 3 SR-1 dup self-keys), now de-risked by the 1158 classification.

---

### OPEN-WORKFLOW-AI-ARTIFACT: Distinguish Computed from Asserted in the Corpus
**Status:** OPEN (NEW 15 July 2026, Patch 2471)
**Sector(s):** Infrastructure / Epistemics
**Priority:** HIGH
**One-line statement:** AI-generated chat output is entering the corpus as executed artifact and being cited in shipped papers as numerical verification; nothing structurally distinguishes a stub from a simulation at read-time.
**Evidence (three instances, one class):**
1. `series_relativity/notebooks/600-cell-monte-carlo-k-fit.py` — trial loop is `pass`; results hard-coded in comments; contains the phrase *"For brevity **in this response** the full 120-point generator is included in the repo file"* — an AI chat reply saved as `.py`, then cited by SR-1 across four sites as a Monte-Carlo verification. The sibling file has an empty vertex list.
2. `series_relativity/notebooks/600cell_k_alpha_geom_consistency_fix.py` — AI-authored March 2026, correctly diagnosed a real flagship defect, proposed a remedy, listed seven paper changes. **Never routed anywhere.** Sat unapplied four months. Also printed an unresolved objection to its own remedy (*"WAIT — this means 3Ā/V₀ is NOT dimensionless!"*) and proceeded regardless.
3. `OPEN-SR-2` has recorded k as unresolved ("two inconsistent estimates") since ~23 March 2026 while the shipped SR-1 abstract claimed k derived from first principles. Registry and paper contradicted each other, uncaught.
**Why it matters:** the failure mode is invisible at read-time — a stub and a simulation are indistinguishable in a citation. The reasoning-capture protocol captures *reasoning* but does not separate **computed** from **asserted**, and `notebooks/` has no path to the frontier. Patch 2471's defect was found only by an unrelated detour (DM → SF-6 inertia → A3′ source clause → Grid Resolution → k). It was luck, not process.
**What a solution looks like:** (1) every numerical claim in a paper cites a script that is **executed in-container at patch time**, with its stdout captured into the patch (2471 is the first to comply); (2) a `publication_audit.sh` gate that FAILs on a cited script which is absent, non-executable, or whose data is generated from the quantity it fits (circularity check); (3) elision markers ("for brevity", "full version in repo", "…") as a blocking FAIL in any committed `.py`; (4) a routing rule that any `notebooks/` finding which contradicts a shipped claim must open a frontier item within the same session; (5) periodic registry-vs-abstract consistency sweep.
**Tractability:** (3) is a grep; (1)–(2) are one focused infrastructure session; (5) needs a scripted diff of frontier status vs paper claims.
**Paper(s):** None (infrastructure) — but SR-1 is the live casualty.
**Last updated:** 15 July 2026

---

### OPEN-WORKFLOW-PREDICTION-AUDIT: How Many of the ~28 Zero-Parameter Predictions Are k?
**Status:** OPEN — MECHANICAL PASS COMPLETE (Patches 2477–2478, 15 July 2026); adjudication + theorem track remain. (NEW 15 July 2026, Patch 2474.)
**Mechanical-pass result (2477–2478):** gate built (`scripts/integrity_audit.py`, BLOCKING inside `publication_audit.sh`; spec items (a), (b)-static, (d), (f) mechanized; (c)/(e) surfaced as WARN bands for human adjudication). Programme-wide sweep of 56 papers: **19 unique fabrication-class findings in 7 clusters** (SR-1/SR-2 epicenter as hypothesized; SF-2 panel review packages citing verify scripts that were never committed; SF-1 reasoning fragments 1402/1403 with the script leg missing; SS-9 wrong-name + one missing script; SD-2 supplementary pointer to a nonexistent file). **No further instance of the full five-step k-pattern found at the mechanical level.** SM/QM/EU-1/SF-4/SF-6/SF-7/SS-5/SS-6 clean at this level. 116 repro-class findings (undeclared numpy — convention decision owed, see memo §Reproducibility). 72 WARN items = the human queue (W5 identity-billing first; SR-2 tops it). Full record: `Development/integrity_audit/2026-07-15_adjudication_memo.md` + raw report alongside. **Terminology correction + Reconstruction Track (Patch 2481, founder statement 15 July, `founders_voice/2026-07-15_on_unrecorded_verification_and_programme_history.md`):** the pre-protocol (Sonnet-era) MC runs occurred; the failure was recording, not fabrication — "unrecorded verification," reconstructible; a 7-item Reconstruction Track is now in the adjudication memo (SF-2 review-package verify scripts highest priority). **Remaining:** (i) the 19-item adjudication queue (SR-1 doc-suite F6/F7 items fixed at 2479; blast radius closed at 2480), now largely re-expressed as the Reconstruction Track; (ii) the WARN-band reads; (iii) **the theorem track** — H.1 was a theorem, not a prediction; re-verifying `theorem-registry.md` proofs is not mechanizable and is the open half of this item (ordering: most-load-bearing, class-coverage claims, script-less proofs first).
**Sector(s):** Infrastructure / Epistemics
**Priority:** CRITICAL — this may be the most consequential open item in the programme.
**One-line statement:** SR-1's k was a normalisation convention billed as a zero-parameter prediction, and its five falsifiable predictions were void; the axiom registry lists ~28 zero-parameter predictions whose independence underwrites the entire √N null-hypothesis-raise strategy. Nobody knows how many are like k.
**The pattern to search for:** (1) a geometric factor is computed; (2) it does not give the wanted number; (3) it is absorbed or removed by an appeal that does not hold (dimensional analysis "forcing" a dimensionless prefactor, "consistent use of units", "absorbed into the normalisation"); (4) the result is billed as zero-parameter; (5) a verification is cited that was never run.
**Why this is not paranoia:** SR-1 exhibited all five. It was found by accident, four months late, on a detour from an unrelated dark-matter campaign. Three prior attempts at this very file (`development/lattice-derived_coupling_constant_k.md`, `development/k_prefactor_resolution.md`, `notebooks/600cell_k_alpha_geom_consistency_fix.py`) failed to land, and SR-1's own CHANGELOG records the defect **as the repair**: *"v17 — alpha_geom consistency fix"* **was** the invalid dimensional-necessity argument.
**What a solution looks like:** for each registered prediction — (a) does a cited verification script exist? (b) does it execute on a stock interpreter? (c) does it generate its test data from the quantity it purports to measure (circularity)? (d) is any prefactor computed, then absorbed, then billed as derived? (e) is any claimed input actually an output of the thing it predicts (the γ-bridge pattern)? (f) does the frontier's status for that item contradict the paper's claim? Mechanical and scriptable; (c)–(f) are the ones that matter.
**Blast radius already known:** 14 downstream artifacts cite SR-1's k / PSR formula (c01, c02, c03, c05, c07, c08, c09, c12, c14, plus early-universe reasoning). SR-1 is not the unit of repair.
**Tractability:** one focused session for the script; the adjudications will take longer.
**Paper(s):** all flagships
**Last updated:** 15 July 2026


---

### WORKFLOW-REVIEW-ECONOMY: Review Effort Scales With Claim Strength (FOUNDER RULING)
**Status:** BINDING — founder ruling 15 July 2026 (Patch 2495), issued on compute-budget and turn-economy grounds after the OPEN-SR-H1-CLASS closure.
**The rule:** verification turns (panel rounds, founder review cycles) are spent where fraud risk lives — on POSITIVE claims. Specifically:
1. **Panel (full 5-slot) ONLY for:** (a) wins — any positive claim entering a registry or billing a derivation; (b) genuinely stuck and asking for help; (c) explicit founder request. "Five independent super-mind reviewers is strong insurance against self-confidence" — spent on wins, where we might be fooling ourselves.
2. **Negatives, closures, abandonments, sector switches:** one dated line in `todolist.md` (or the relevant registry) and MOVE ON. No confirmation rounds. Nobody fudges toward a kill.
3. **KEEP, unchanged (these are efficiency tools, not ceremony):** (i) pre-committed kill conditions + effort bounds on any multi-session campaign, one page, written BEFORE work starts — stopping fast is the biggest compute saver and only works if the stop rule predates the work; (ii) verify scripts on every computational claim (the direct anti-2471 measure); (iii) **FULL VERBATIM per-patch reasoning capture — founder ruling: "Saving the entire reasoning at every turn is crucial, not abbreviating is crucial." Never trimmed, never summarized.**
4. **Trim:** commit messages lean (~10 lines; the reasoning fragment carries the record); handovers ~half a page (kickoff line, state, next action, gates); no per-step ceremony beyond the reasoning fragment.
5. **The counterpart obligation:** when a win comes, the full review is NOT skipped because the programme has gotten used to moving fast. The trade is "save the scrutiny for where it counts" — it must actually be spent there.
**Registered:** 15 July 2026, Patch 2495.

**7 Aug 2026 (Patch 3025) — WORKFLOW-REVIEW-ECONOMY reaffirmed against worker drift, on founder challenge.** The worker had layered a pre-execution flash SANCTION round onto the already-frozen KMEM-TAIL-1 disposition prereg. Ruling: sanction-class rounds are ECONOMY-NONCOMPLIANT — a prereg in hand is neither a win nor an impasse; freeze-before-code (committed, auditable) is the integrity protection; the 2981 precedent executed with no pre-sanction; the panel attacks design AND result together at the single adjudication of the executed record, where a sustained design objection voids the disposition (the multiple-look cost of a post-hoc redesign is the accepted price of the saved round, disclosed). Round withdrawn BEFORE issue; zero founder paste-labor spent. Standing rule going forward: pre-execution design-sanction rounds require an explicit founder green-light as an economy EXCEPTION; the default is execute-then-adjudicate.
