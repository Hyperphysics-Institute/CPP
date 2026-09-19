# CPP Programme To-Do List

**Location**: `/CPP/todolist.md` (repo root, parallel to `research_frontier.md`, `future_projects.md`, `paper_catalog.md`).

**Purpose**: Track small carried-over items, deferred protocol steps, and hygiene gaps that don't warrant full `future_projects.md` entries but must be cleared before the next paper begins. The "easy to lose" things — things that compound if not externalized.

**Write rule (Patch 0939; bootup §0.5 D-9)**: an item enters this file **in the same commit that defers it**, under the lane that acts, checked by `python3 code/deferral_gate.py` before every `format-patch`. Nothing is "put aside for later" anywhere else — not in a review file, a sector status line, a registry bullet or a handover; those are records, this is the queue. Three arcs lost their owed items before this rule (TODO-3930-EU, TODO-3938-DM, TODO-0937-CHIR).

**Discipline (introduced 7 May 2026 Session 33 close)**: A new paper does not start until this file's **P1 — Must clear before next paper** section is empty. Items move to **Cleared items (history)** at the bottom when completed (with date and patch number for audit). Items can also be reclassified to `future_projects.md` if they grow into multi-session projects, or deleted as no-longer-applicable with a note.

## How this file relates to other tracking files

- **`future_projects.md`** — registered active projects with full mechanism / falsifier / companion fields. Multi-session work with a clear deliverable. SS-9 anthology chapter (A.3) and TATWD integration (A.4) live there, not here.
- **`research_frontier.md`** — last-updated session-by-session log of the programme's frontier state. Programme-level open problems and their status.
- **`parallel_development_roadmap.md`** — the phased roadmap + to-do for scaling CPP from solo to a collision-resistant parallel theorem-development team (coherence layer, integrity subsystem, Claude Code agentic pilot, escalation triggers). The living plan for the team-scaling initiative; this todolist tracks only its small carried-over items.
- **`session_logs/`** — per-session entries capturing what happened.
- **`todolist.md`** (this file) — *small carried-over items, deferred protocol steps, hygiene gaps*. Kept short on purpose. If an entry here grows beyond a few patches of work, promote it to `future_projects.md`.

A new item belongs here (rather than in `future_projects.md`) if it's: small enough to clear in one or a few patches; not its own multi-session project; or explicitly deferred from a session whose main work was different.

---

## Standing conventions (permanent — do NOT clear)

*Persistent workflow rules. Unlike TODO items, these are never "cleared"; they bind every future session.*

### CONV-001 — Presenting a repo file to the swarm/panel (one single copy block)

When Claude asks Thomas to present any repo file to the AI review panel (swarm), Claude must, **in the
chat response**, provide the whole package as **ONE single fenced copy-paste block** — so Thomas can
one-click-copy and paste it to each panel member without highlighting/copying multiple separate pieces.
That single block contains, in order: (1) the **GitHub links** to the file (blob form
`https://github.com/Hyperphysics-Institute/CPP/blob/main/<path>` and raw form
`https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/<path>`, valid after push); (2) a
**one-paragraph intro** framing the file for the swarm; (3) the **full rendered file content** (rendered
Markdown, NOT the patch/diff). All three inside the *same* fenced block. Rationale: Thomas presents to the
panel by pasting once; multiple separate blocks meant repeated highlight/copy/paste — never make him do
that, and never make him hunt for a file embedded in a patch. Template: `templates/presentation_file.md`.
This single presentation block is separate from the apply-and-push patch block (the patch applies the file;
this block hands it to the swarm). Registered 5 Jun 2026 Session 154; **updated 6 Jun 2026 Session 154 to
the single-block format at Thomas's request** (previously three separate elements).

### CONV-002 — Re-fetch high-risk shared files immediately before committing to them

Before committing any change to a **high-risk shared file**, re-fetch origin and re-read that file's current content, then build the edit on the latest version — never on a copy read earlier in the session. This is the lightweight collision-prevention discipline; for routine solo / few-window work it replaces the heavier post-hoc `collision_audit.sh` pass. High-risk files are the ones multiple work-streams touch, so a stale read is the main way concurrent work clobbers.

Procedure (committer, per high-risk file touched):
1. `git fetch origin && git reset --hard origin/main` (or re-clone) so the working tree matches the latest origin.
2. Re-open and re-read the target file; rebuild the intended edit against its current content.
3. Commit and push. If origin moved again between read and push, repeat.

High-risk shared files = the integration-owned list in `parallel_dev/scripts/collision_audit.sh` (`SHARED_REGEX`): `theorem-registry.md`, `predictions.md`, `axiom-registry.md`, `master_glossary.md`, `research_frontier.md`, `frontier_sectors/*`, `todolist.md`, `future_projects.md`, `paper_catalog.md`, `research_timeline.md`, `organizational_frontier.md`, `theory-overview.md`, `programme_orientation.md`, `README.md`, `INDEX.md`, `parallel_dev/lease_board.md`. The single source of truth for this list is that `SHARED_REGEX` — update it there, not here. Files inside a paper's own folder are low-risk and exempt. Registered 8 Jun 2026 Session 154.

### CONV-003 — Parameter-set provenance for load-bearing numbers (panel-requested, DM-1 v1.1)

Every **load-bearing numerical claim** in a paper, revision notice, registry entry, or review package states the **parameter set (and source patch/ledger) it was computed from**. At any **morphology / mechanism / model pivot**, every number carried across the pivot is **re-derived or explicitly rescaled at the new object's parameters** before being quoted — "same formula, stale parameters" is the failure this convention exists to prevent. Review packages for results with load-bearing numbers **embed runnable (stdlib) verification code**, and reviewers run it before verdict (SCRIPT-EXECUTED).

Origin: DM-1 v1.0 quoted the 0860 hoop ledger's collision energies (~1.95 MeV / ~0.78 keV; N=1183, m=264 MeV) in the Cross-Rod paragraph (N=5–60, m_el=1408 MeV); the paper's central velocity-dependence discriminant rested on a retired morphology's numbers, shipped v1.0, and passed the panel 4/4 — the values were internally plausible but untraced. Caught by in-house audit (Patch 1859) six days post-ship; convention requested independently by all four reviewers at the v1.1 re-ratification (Patch 1862). Author-side failure mode recorded in `templates/AI_team_expectations.md` (Opus). Registered 3 July 2026, Patch 1862.

### CONV-004 — The measured-coefficient (Galilean-layer) discipline (founder-ruled, DM sector first)

Where the substrate physics beneath a result is genuinely unresolved (DP density, lattice occupancy, ZBW
amplitude, cancellation/superposition factors), the programme may claim the STRUCTURE and let DATA fix the
coefficients that encode the unresolved depth — Galileo's law before Newton's mechanism; effective-theory
practice one level below where conventional physics believes anything exists. Rules: (1) every such number
carries a ledger tag — **MEASURED** (inverted from data through the claimed structure), **DERIVED**
(theorem-level from axioms), or **CONJECTURED** — and the tag travels with the number everywhere (CONV-003
provenance extended); (2) a measured coefficient is honest only under **overdetermination** — it must survive
channels it was not fitted to, pre-registered, no refit; the measured-vs-unknown count is kept visible, and
the moment unknowns outnumber measurements the work is curve-fitting and must say so; (3) the discipline
applies ONLY where derivation is premature — sectors holding zero-parameter DERIVED results (the programme's
strongest asset) are NOT re-framed; (4) the derivation layer remains the standing goal: with coefficients
pinned, the later axiomatic derivation is confirmed by overdetermination against numbers it did not fit — a
firewall the tags exist to guarantee (no measured value may silently leak into a "derivation" that then
"confirms" it). Origin: founder methodological ruling, 6 July 2026 (DM sector; D5/F3′ context), verbatim in
`founders_voice/founder_ruling_measured_coefficients_2026-07-06.md`. Registered Patch 1886.

### CONV-005 (v2, panel-ratified 22 Jul 2026 Patch 2764) — Blocking Hamiltonian-identity gate before every Markov-chain production run

Every act that runs (or re-runs) ANY Markov-chain sampler (Metropolis, HMC, or other) executes, BEFORE any
production sweep, a **blocking Hamiltonian-identity gate**, per distinct move type, interaction
implementation, boundary condition, external-field mode, and code path: **≥20 randomly generated states ×
≥20 proposed moves per state**, mandatorily including boundary-crossing moves, near-core moves,
particle-index edge cases (i = 0, i = N−1), deliberately large displacements, and the zero-move identity.
The incremental ΔH is compared against a from-scratch total-energy difference from an independent code
path: **|ΔH_inc − ΔH_full| ≤ 10⁻¹⁰·max(1, |ΔH_full|)** (typical target 10⁻¹²), plus the inverse-move
antisymmetry check ΔH(x→x′) = −ΔH(x′→x). ANY failure blocks production and the session reports the defect
instead. The gate re-runs after ANY change to energy computation, neighbor masks, boundary handling, or
source terms. The gate is written into the act's prereg and its PASS line is quoted in the record.
Invariance checks (permutation, periodic translation, energy/force-gradient consistency) are recommended
where the implementation admits them. Origin (v1, Patch 2758): the 2714 self-pair defect survived five
campaign acts and manufactured a 5.6σ artifact; the first five-move gate (B-CHECK-80, Patch 2754) caught it
before consuming a seed; the fixed re-run (Patch 2756) killed the anomaly at 0.02σ. v2 amendments ratified
by the CONV-001 panel at the S4-X bundle adjudication (Patch 2764): coverage 400 checks vs five; mixed
threshold; edge-case move classes; inverse-move test; all-MCMC scope; re-gate-on-change rule.

### CONV-006 — Authentication-before-adoption for artifacts of interrupted or externally-executed sessions (panel-ratified 22 Jul 2026 Patch 2764)

When a session finds completed computational artifacts it did not itself produce (stalled-window recovery,
parallel-agent output, any uncommitted work of uncertain provenance), the artifacts are NOT adopted on
trust or on memory. Before scientific adoption: (1) SHA-256 manifests for the code and data artifacts are
computed and committed with the authentication record; (2) every quoted number is reproduced by re-running
the frozen analyzers over the immutable raw archives; (3) **at least one full chain per distinct executable
configuration is regenerated from its recorded seed** to the bit-identical-sampling standard (accumulator
residues at the disclosed refresh level permitted), with the chain chosen by a rule stated BEFORE any
comparison is seen (e.g., cheapest); (4) more than one chain regenerates when conclusions depend on
chain-to-chain variance; (5) the authentication record commits BEFORE the artifacts' adoption patch or in
the same push. Clean-environment rerun is recommended, not mandatory (revisit on first discrepancy).
Origin: the RV-2714 stalled-window recovery (Patches 2761/2762); precedent authenticated by deterministic
reproduction; formalized with amendments by the CONV-001 panel at the S4-X bundle adjudication (Patch 2764).

### CONV-007 — Withheld-key admissibility (registered 29 Jul 2026 Patch 2874)

A withheld verification key issued with a CONV-001 dispatch must be a quantity that **(i)** is computable
from a committed artifact whose path is named in the dispatch — S2's requirement, established at Patch 2829
and what made honest verification possible — **AND (ii)** does **not** appear in any commit message,
docstring, README, prose file, or prior adjudication anywhere in the repository. Requirement (ii) must be
checked before the dispatch is issued, by grepping the full history (`git log --all --format=%B`) *and* the
artifact's own source, including its docstring. **A key failing (ii) is VOID and no execution ruling —
neither VERIFIED-EXECUTED nor fabrication — may be made on it.**

Originating failure: the Patch 2873 dispatch nominated the 2868 dt/vf ladders and sign as its key. Both
ladders appear verbatim in Patch 2868's commit message *and* in the target script's own `RESULT` docstring
block, so a seat could return all six values and the sign without executing anything. S2 returned correct
values and could be neither credited nor penalised. Verify script: `series_phenomena/cosmology/dark_matter/code/2874_key_void_check.py`
(6/6 values found in each location). The failure was the worker's, not the seat's — clause (i) was
satisfied and the complementary clause had never been written down.

### CONV-008 — Roster byte-identity check before scoring any CONV-001 round (registered 29 Jul 2026 Patch 2876)

**Before adjudicating any CONV-001 round, compare the returns pairwise for byte-identity or near-identity.**
Any identical pair is counted as **ONE seat position**, and the effective roster size is stated in the
adjudication's header *before any question is scored*. Independent models do not produce multi-thousand-word
identical returns; the near-certain cause is a duplicated paste at dispatch, and **no blame is assigned to any
seat** — the worker requests confirmation and proceeds on the reduced roster.

Originating history: **three occurrences.** Patch 2849 (Darwin final motion) caught it and established the
one-position rule, and requested confirmation before the next round. The SF-6 dispatch's first attempt hit it
again and **the worker did not catch it**, counting two identical declines as two independent positions and
drawing an unsound capability inference from the count. Patch 2876 hit it a third time. Per-round flagging has
failed to prevent recurrence, which is why the check is now a standing convention rather than a habit: the
check is cheap, the failure is silent, and an inflated roster count is indistinguishable from consensus.

---

### CONV-009 — Founder verbatim capture is a patch obligation, not a courtesy (registered 1 Aug 2026 Patch 2881)

**Any turn in which the founder supplies physics — a mechanism, a ruling, a correction, a decision on
scope or status — is captured VERBATIM to `founders_voice/` in the SAME patch that acts on it.** The
capture is the primary source; any conjecture entry, frontier update, paper passage, or panel dispatch
derived from it is secondary and must cite it by path. **The primary source is written FIRST, or at
minimum in the same `git am`. Registering a derivative before its source inverts the dependency and is
the error at Patch 2880.**

**Scope.** Verbatim means verbatim — the founder's own words, block-quoted, not compressed and not
tidied. Worker commentary is permitted but must be visibly separated (`**Worker note:**`) so that a
later reader can always recover what the founder actually said from what the worker made of it.

**Why this is a convention and not a reminder.** The founder reports the capture has been missed in
prior sessions whenever he has asked, i.e. it is a chronic cross-worker failure. The cause is
structural: the worker reasoning fragment rides inside the patch bundle and is carried by the
mechanical workflow, while founder capture has no trigger and therefore depends on memory. This is the
same shape as the roster duplication, which recurred three times under per-round flagging and stopped
only when it became a procedural step (CONV-008). **The founder's verbatim is the one source in the
corpus that cannot be reconstructed from anything else** — and this session demonstrated four separate
times that worker summaries drift from their sources, the source being right every time.

**Companion obligation.** The reasoning-capture rider has no exemption for addenda, corrections, or
adjudication records. Patch 2879 was skipped on the assumption that an addendum is bookkeeping; it
contained an adopted dissent and the re-scoping of an open item. **If a patch makes a judgment, it owes
a fragment.**

---

---

### CONV-010 — Tier 4 means the derivation, not a retrospective about it (registered 1 Aug 2026 Patch 2882)

**A Tier 4 fragment must contain the DERIVATION — the equations, the substitutions, the intermediate
steps, the dead ends — not a finished-prose account of having done it.** `templates/documentation-suite.md`
defines Tier 4 as *"verbatim derivation reasoning — the moment-by-moment groping, false starts, PAIRING
resolutions, recognition moments… the canonical record from which Tiers 1–3 derive."* Tiers 1–3 derive
FROM Tier 4, so **Tier 4 must be the richest layer in the suite. If a fragment is thinner than the
documents that cite it, the structure is inverted.**

**Diagnostic, applied at the patch that writes the fragment:** could a competent stranger reconstruct the
result from this file alone, without the chat transcript? If the answer is no, it is Tier 3 content and
does not discharge the Tier 4 obligation.

**Originating measurement (founder audit, 1 Aug 2026).** Fragments `reasoning/2873.md` through
`reasoning/2880.md` averaged a few hundred words of polished retrospective; `2880.md` ran 67 lines of
which **three** contained any mathematics. Two load-bearing derivations of the inertia arc — the
C·PSR = SSV_abs condition and the dipole-algebra sign reversal — existed in the corpus **only as
conclusions**, and two computations (`wake_sign`, `robustness`) were **never committed at all** despite
the reasoning-capture rider requiring a verify script whenever a computation is run. Remediated at
`sketches/tier4_derivation_record_inertia_arc.md` and `code/2882_*`.

**Observed failure mode worth naming:** the retrospective register captures **failures** well ("I nearly
did X and did not") and **successful derivations** poorly, because a chain that worked gets compressed
into its result while a chain that broke gets narrated. **That is backwards for validation** — an
external validator needs the working derivations most. Record both.

---

### CONV-011 — Branch-preregistered review timing (panel-proposed GPT S1, adopted Patch 2944)

Every prereg that freezes verdict bands for a computation must ALSO freeze, before the computation
runs, the panel-review timing per branch: falsifier-class branches (CASE-L-type) trigger pre-action
review before any conversion or downstream use; conservative/bound-type branches (CASE-Q-type)
permit a single combined completed-package review. Discretion over review timing after the branch is
known is removed. Origin: the Patch 2941 economy amendment was defensible but was made after the
branch was revealed; GPT S1's combined-cycle return (Patch 2944 adjudication §4.3) supplied the
prospective rule verbatim. Registered 2 Aug 2026 Patch 2944.

---

## P1 — Must clear before next paper (SS-10)

*(Empty — gate cleared 7 May 2026 Session 36 close patch 0288. SS-10 may begin.)*

The Session 36 P1 audit found that all originally-P1 items except TODO-002 were either deferred on external triggers (TODO-001) or were historical/programme hygiene that does not actually forward-block SS-10 (TODO-003, 004, 005, 006). Per this file's own escape-valve discipline (*"If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why"*), they were demoted to P2 and TODO-002 was cleared after its actual completion via patches 0286 + 0287 + commit `55c5986`. Result: P1 genuinely empty; SS-10 begins on a clean slate at the next session.

---

## P2 — At Thomas's discretion (not blocking next paper)

### TODO-0976-RECOMPILE — Corrigenda APPLIED to source; PDF recompiles now owed (registered Patch 0976, chirality lane)

**Status change:** the five paste-ready corrigenda carried in TODO-0937-CHIR and the F.1/TARROW-2 wording
items are **written into the `.tex` sources at Patch 0976**. What remains is mechanical: the PDFs must be
regenerated (founder / Isak, per the Binary Artifact Workflow) before any Zenodo or OSF deposit quotes them.

**Applied at 0976:**
- `capotauro.tex` — §20.1 vanishing clause, §20.2 Definition 20.2 inversion referent, §20.5 operator
  `Ĉ^qDP = χ(1/6)ŝ ∈ A₁g ⊗ C-odd` (replacing the A₂u assignment), §20.6 extended-group Wigner–Eckart,
  Theorem `thm:theo_sd_chir_2` step (iv); plus the relabel footnote at the Reading C edge-perturbation equation.
- `chirality_continuum.tex` — the three **operator** labels. *The three remaining `A_{1g} ⊕ A_{2u}` occurrences
  are the matter-doublet state-space decomposition, which 0937 did not change and which are correct as written.*
- `SM-2_mass_generation_geometric_hierarchies.tex` — edits (a)–(f), both W entries, and the down-type prose.
- `theo_chir_tarrow_2.tex` — the claim (i) scope remark.
- `dynamical_substrate_law.tex` — MA.2 vertex-independence, the `r(−ê;v)` referent, exclusion-class E1
  narrowing, `δ = −ε` pinned, and the relabel.

**Still owed, and not applied:**
- **SM-2 edit (g)** — **APPLIED at Patch 4002**, `OPEN-EW-7` resolved; no longer held. ~~Deliberately held pending `OPEN-EW-7`~~
  (does the W mass breakdown depend on species or only on count?). This is the only place a published SM-2
  number can still move; relabelling the row before the answer would assert a pure relabel that may be false.
  Lane: EW. The row still reads `Linear 6-hDP chain` on purpose.
- **The PDF recompiles themselves** — founder mechanical, five documents.
- **An observable selecting the alternating W⁰ ring order over the blocked order.** None on file; carried with
  `OPEN-EW-7`. Lane: EW.

### TODO-0974a-CAPTURE — Steps C and D of the Session 228 close — **Step C CLEARED at 0977; Step D LARGELY RECOVERED at 0975b, superseding the "unrecoverable" finding**

**CORRECTION (Patch 0975b, 13 Sep 2026).** 0977 recorded Step D as unrecoverable for 34 patches, on the basis that the reasoning "was never saved and no longer exists anywhere." **That was true of the repository and false of the world:** the window that produced those patches was still live, and reasoning it can state about its own work is *primary source*, not reconstruction. **21 of the 34 are now captured** — `chirality_derivations/reasoning/` 0942, 0943, 0944, 0946, 0947, 0950, 0951, 0953, 0955, 0957, 0961, 0963, 0964, 0965, 0966, 0968, 0970, 0971 and `dynamical_substrate_law/documentation_suite/` reasoning-0972, reasoning-0973. **The other 14 in range are exempt** under the scope test added at 0975b (0938, 0939, 0945, 0948, 0952, 0954, 0956, 0958, 0959, 0960, 0962, 0967, 0969, 0974): no original derivation, no computation, no finding.

**Arithmetic corrected at Patch 0979** (0975b's own prose, not its work): it shipped **20** fragments, not 21 — counted from the commit's file list; and its exempt list reads *"thirteen patches"* while enumerating **15**. The reconciliation is 20 captured + 14 in-range exempt = 34, with `0974a` a 15th entry lying outside the 0936–0974 range the 34 was counted over. No work is affected; the ledger now matches the tree.

**`0974a`'s exemption NOT SUSTAINED, and discharged at 0979.** It fails 0975b's own test: `next_id.py` matched `^(0\\d{3})\\s+`, so a suffixed ID put a letter where whitespace was expected and the first suffixed patch in the block would have been **invisible to the collision gate the renumber existed to satisfy** — a finding, reached by testing, shipped as a code change. Fragment filed at `chirality_derivations/reasoning/0974a.md`, marked verbatim-late. **The test works; it was applied to 0974a one patch too early, before 0974a's own content was weighed.**

**0977's refusal to fabricate was right and is not being second-guessed** — a plausible substitute for a lost original is worse than an admitted gap. What changed is that the original was not lost. **The general lesson for the next window: before declaring reasoning unrecoverable, check whether the originating window is still reachable; only it can capture rather than reconstruct.**

*(prior heading)* Steps C and D of the Session 228 close — **CLEARED at Patch 0977 (14 Sep 2026), with one part declared unrecoverable**

**Step C (Tier-3 vignettes): DONE.** Written by subject, not by session — the F.1 derivations (L4-A/B/C/E, `δ = −ε`, the non-reciprocity result) into `dynamical_substrate_law/documentation_suite/development-dynamical-substrate-law.md`; the arc-level work (C-W46, SM-2/W, piece 1, CONV-047/048/049, the V3 and TARROW-2 re-reads, 1d-β, R-1/R-2) into `chirality_derivations/documentation_suite/development-chirality-derivations.md`. **That is the placement choice this entry asked a later window to make and record: a session is not a subject, so no cross-paper vignette file was created.**

**Step D (Tier-4 verbatim): NOT DONE, AND NOT DOABLE — 34 of the session's 39 patches have no fragment, and the window that held the reasoning is gone.** Tier 4 is defined as reasoning *preserved verbatim*, and every other tier is defined as derived from it; writing fresh prose into a `reasoning-<patch>.md` file today would put a narration under the name of the canonical record, which is the specific failure the discipline exists to prevent. **No such files were written.** What was written instead is an honest pointer-map at `chirality_derivations/documentation_suite/reasoning-index-chirality-derivations.md`, listing the five patches that do have patch-time verbatim (0936, 0937, 0940, 0941, 0949 — the session's derivations) and, for the other 34, where the substance actually sits. Every pointer was checked to resolve. **This item is closed as far as it can be closed; the verbatim record for those 34 patches is a permanent loss, recorded rather than papered over.**

**Observation carried forward, not enacted (the lane does not amend the OS from a documentation patch):** capture held for all five derivation patches and lapsed across the panel, corrigendum and scoping patches, which were not felt to be "physics/derivation" patches. That intuition was wrong in at least three places — CONV-048's joint-corner finding, CONV-049's 3-plane lemma and 0966's proxy-sensitivity bound were all substantive reasoning, and two of the three came from reviewers. Whoever next revisits the reasoning-capture rider should know that **the pure-bookkeeping exemption is doing more work than it was designed for, and a panel adjudication is not bookkeeping.** Lane: governance.

*Original entry, for the record:*

**Owed:** Tier-3 development vignettes (Step C) and the Tier-4 verbatim reasoning narrative (Step D) for Session 228, patches 0936–0974a.

**Rationale for deferral** (required by Step H's deferral discipline): context-budget exhaustion in the originating window. The session ran 40 patches and closed at the end of a long founder-facing session.

**Source material, named so a later window does not have to reconstruct it:**
- Per-patch reasoning fragments: `chirality_derivations/reasoning/0937.md`, `dynamical_substrate_law/documentation_suite/reasoning-0940.md`, `-0941.md`, `-0949.md`.
- The review suite: `chirality_derivations/review/` (0937, 0950, 0951, 0953, 0955, 0957, 0960, 0964, 0968, 0971) and `sketches/` (0961, 0963, 0964, 0970).
- **Verbatim reviewer returns:** `chirality_derivations/reviews/verbatim/` (committed at 0974a — Step F).
- Session log: `session_logs/2026-09-13_session_228_log.md`; pointer-map: `session_logs/transcript-cross-paper.md`.

**Scope note:** most of this session's work is arc-scoped rather than paper-scoped, so Step C's "paper-scoped" trigger applies chiefly to the F.1 / Capotauro / SM-2 material. A future window should decide whether the vignette belongs to `dynamical_substrate_law/documentation_suite/` or to a cross-paper file, and record that choice.

### TODO-0937-CHIR — Owed items from the C-W46 four-state closure (registered Patch 0938, chirality lane, under PD-006)

**Why this entry exists:** the founder asked (13 Sep) whether the corrections and flags of Patches 0936/0937 were recorded somewhere retrievable and actionable. They were in the review file, in `frontier_sectors/CHIR.md`'s resolved entry, and in a dated `theorem-registry.md` bullet — none of which is a work queue. Same failure shape as TODO-3938-DM and TODO-3930-EU; recorded here so it is not the fourth.

**Source:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0937_c_w46_flags_f1_f3_closure.md` (verify `code/0937_d5d_extended_group_bookkeeping.py`, 14/14). Result: the antipodal-pair space carries no pseudoscalar operator; C-W46's nonzero element is the host charge sign, Ĉ^qDP = χ·(1/6)·ŝ; inversion centre = the local point group's p ↦ φn̂ − p; DM reading E1 = case (c), S = +qCP, unconditional on a reading.

**Owed, by lane:**
- **SD lane — `capotauro.tex` corrigendum (labels only; magnitude χ/6 unchanged).** Paste-ready text in the review §5 for §20.1 (refinement resolves the vanishing only with the charge-sign content), §20.2 (Def. 20.2: v ↦ −v is p ↦ φn̂ − p; "n̂ ↦ −n̂" is the substrate mirror, not a group element), §20.5 (Ĉ^qDP ∈ A₁g(D₅d) ⊗ C-odd; the printed A₂u character is a polar coordinate; A_u(I_h) ↓ D₅d = A₁u with no support on the pair), §20.6 (Wigner–Eckart line on D₅d × Z₂^C), and Theorem `thm:theo_sd_chir_2` step (iv). **Mechanical (founder): apply at the next Capotauro recompile.** Also carry into `chirality_continuum.tex`, which cites the A₂u label at four places (grep `A_{2u}`) — same correction, same recompile.
- **DM lane — the χ/6 ↔ E_DP normalisation (E2 of `OPEN-DM-SIGN-SELECTION-1`).** C-W46's χ/6 is a dimensionless reduced element ⇒ split per DP = 2·(χ/6) = χ/3 in the sector's energy unit. 3528 carried (1/φ)·χ·E_DP per direction. Under R1 the 1/(2φ) projection factor is constant on the four-state space, so it is a normalisation convention for M, not an angular dependence. Reconcile when E_coc lands; **nothing on file fixes E_DP as the unit.** Consumer: E2 and E3's numbers. (Cross-ref at the foot of `dark_matter/founders_voice/3533_E1_sharpened_note.md`.)
- **SM lane — SM-2 composition-level corrigendum: WRITTEN, Patch 0942** (`series_standard_model/corrigenda/SM-2_composition_corrigendum.md`, verify 5/5). Paste-ready, three edits: the down cage entry, the Capotauro stabilisation sign (−qCP → +qCP, now derived via 0937's Ĉ^qDP = χ(1/6)ŝ), and the linear extra's species (qDP/hDP → −eCP; σ and d = 1 unaffected). **Finding: SM-2's as-written cage list contradicts SM-2's own charge section** — a neutral extra DP gives the down −2/3, not −1/3; the founder's composition gives −1/3 exactly. Mass fit is label-level (N_k = 2.5 unmoved; no published number changes). **Mechanical (founder): apply at the next SM-2 recompile, with or after the Capotauro corrigendum so both quote the same operator.**
  - **RESOLVED by founder ruling 13 Sep 2026 — extended at Patch 0943.** The fix covers all three down-type quarks; edits (d) strange and (e) bottom added to the corrigendum, mass fits label-level (N_k = 30, 3000 unmoved). Full audit `corrigenda/code/0943_sm2_charge_audit.py` (6/6) confirms the defect is exactly the down-type family among the fermions: up-type +2/3, charged leptons −1, neutrals 0 all correct as written.
  - **NEW, found by the 0943 audit — the W boson, and NOT covered by the down-type ruling.** The cage list assigns "W: Linear hDP chain" (mass table: "Linear 6-hDP chain"). An hDP chain is a chain of bound neutral pairs and carries charge 0, but W^± carries ±1. Z and Higgs are genuinely neutral and unaffected — the defect is the charged member of the weak triplet only, and after the d/s/b repair it is **the single residual entry in SM-2 that cannot reproduce its own charge.** Not closable by arithmetic: the chain needs a net ±1 from a charged constituent or an asymmetric termination, which is a composition question. **RESOLVED 13 Sep 2026 — founder confirmed "eCPs" was a typo for "eDPs"; W edits written at Patch 0945.** Corrigendum edits (f) cage entry and (g) mass-row label added; **closing audit `corrigenda/code/0945_sm2_charge_audit_closure.py` (6/6) shows ZERO residual charge defects across all 17 SM-2 cage entries**, no regression. Edit (g) is **held** pending `OPEN-EW-5` (below); edits (a)–(f) can be applied now. Prior state, Patch 0944 (`corrigenda/W_ring_harmonization_query.md`, verify 7/7). Founder ruled 13 Sep: W⁰ neutral, a 12-member ring of three qDPs and three eCPs; W^± = W⁰ + a carried ±eCP on the enzymatic structure. **Harmonised against the Weak Sector lane** (SF-2 v1.0 Thm 4.2 via `capotauro.tex`): the W-bracelet is a Petrie hexagon of the first-shell icosahedron — **six** vertices, stabiliser D₆ of **order** 12. Ring topology confirmed; SM-2's "linear chain" is wrong on topology as well as charge. **But as stated the composition is 9 CPs, not 12, and three eCPs cannot be neutral (odd count of ±1; exhaustively, no odd-eCP 12-CP composition is neutral).** The reading that closes all four constraints is **three qDPs + three eDPs** = 6 DP objects = 12 CPs, neutral, one per Petrie site, preserving SM-2's existing 12-CP count ("Linear 6-hDP chain" is also 12 CPs) while changing topology and species. **Not assumed — awaiting the founder's confirmation that "eCPs" was meant as "eDPs".** The W^± half is adopted as stated and needs nothing: charge sits on the unpaired carried CP, exactly the 3513 partnerless-third structure.
  - **NARROWED at Patch 0947 to an ACHIRAL order; founder's choice between two options outstanding.** The founder ruled 13 Sep that the order should follow empirics. Applied honestly that excludes the chiral pair: the W⁰ is a gauge eigenstate (W³), not an observable, so no handedness can be read off it directly; the sector's empirical chirality anchor (Δp_LR ≈ 0.04) is already spent on |M^W| = χ/6 at 1.6%; and decisively, **χ is odd under all 60 orientation-reversing lattice elements, so with χ ≠ 0 the reflections are not symmetries of the physical substrate — under which the chiral class splits into TWO inequivalent neutral ring states** while the achiral classes stay at one. The SM has exactly one W³. **Options for the founder:** (1) adopt alternating `qDP–eDP–qDP–eDP–qDP–eDP` on symmetry-economy grounds (it alone retains C₃ and stabiliser order 6; blocked retains only order 2) and record it as a structural assignment pending an observable, same status as SM-2's N_k values; or (2) leave the order unspecified, recording only that it must be achiral. **RESOLVED 13 Sep 2026 — founder chose option (1) at Patch 0948:** alternating `qDP–eDP–qDP–eDP–qDP–eDP` adopted as a structural assignment pending an observable, same epistemic status as SM-2's N_k values; written into corrigendum edit (f) with the achirality requirement recorded. **Still owed:** an observable that selects alternating over blocked — none on file; falls to the EW lane with `OPEN-EW-5`. See `chirality_derivations/review/0947_w0_ring_order.md` (6/6).
  - *(superseded)* original open question, Patch 0946 — which arrangement of the three qDPs and three eDPs around the W⁰ ring? Raised at Patch 0946 while answering the founder's chirality question. The 13 Sep composition ruling fixes *what* is on the ring, not the *order*. Of the arrangements of 3+3 on a six-ring there are 4 up to rotation and 3 up to rotation+reflection, so **exactly one is chiral** (`eeqeqq`/`eeqqeq`, stabiliser order 1, the only class with no reflection); `eqeqeq` (alternating, stabiliser 6) and `eeeqqq` (blocked, stabiliser 2) are achiral. If the W⁰ is to carry a structural handedness of its own, the answer is forced to the chiral pair — and then: which handedness, and is it tied to the sign of χ? **Not assumed, not derived.**
  - **EW lane — D₆-breaking note, filed with `OPEN-EW-7` (Patch 0946; renumbered at 4001).** D₆ (order 12) is the stabiliser of the *bare* Petrie hexagon; decorating it with 3 qDP + 3 eDP drops the stabiliser to order 6, 2 or 1 by arrangement. Not an error in the lane's statement, but any downstream argument applying D₆ to the *decorated* W⁰ needs the surviving subgroup.
  - **EW lane — `OPEN-EW-7` registered at Patch 0945 as `OPEN-EW-5`, renumbered at 4001** (`frontier_sectors/EW.md`): does SM-2's W mass breakdown depend on the species of the 12 CPs or only on their count? Count is unchanged (6-hDP chain and the W⁰ ring are both 12 CPs), so either the row is a pure relabel or the W mass fit needs recomputation against 3 qDP + 3 eDP. **The only place a published SM-2 number can still move.** Consumers: corrigendum edit (g); `OPEN-EW-2`, `OPEN-EW-3`. Pointer offered in the corrigendum §4b, explicitly not a derivation: the 3513 "odd man out" partnerless-third structure (a bare CP on a DP entity, already used by the DM lane's E3 count) has the right shape and would reuse an existing mechanism.
  - **Open (physics, founder's):** whether the linear −eCP carries a rest-mass term of its own or is already folded into the N_k = 2.5 assignment. If separate, the down fit moves and N_k needs recalibration. Not assumed either way.
    - **FOUNDER REPLY, 16 Sep 2026 (verbatim, filed at Patch 0994):** *"the linear -eCP does contribute mass, but I don't know how to answer the question about it being absorbed by N_k = 2.5."* **Consequence:** the first half is now a founder ruling (the −eCP carries mass); the second half is a calibration question and is therefore Claude's under PD-006/PD-007, not the founder's: refit the three down-type cages with an explicit −eCP mass term and test whether the fit demands N_k ≠ 2.5 or whether 2.5 already absorbs it (label the result [calibration], not derivation). **Lane: SM (act when live; SM-2 corrigendum edit (g) stays held on OPEN-EW-5 meanwhile).**
- **Chirality lane — OPEN-FP-F1-2, the unconditionalizer.** **Corrected at Patch 0940 (D-2):** L4-D is NOT the next item — its chirality half was resolved at 0647 (THEO-CHIR-MERGE-2, verdict M1-χ: `sign(δ)` is the P-even/T-odd arrow, not a chirality) and its residual is OPEN-CHIR-2a, STATUS-ANSWERED at W3 (0661) with the upgrade pinned to the capacity engine — not workable without F.2. The 0933 flagship scope and the 0936 review both still say "L4-D carved as first sub-target, UNEXECUTED"; **both predate 0647 and should not be acted on** (wording fix owed to `flagship_assembly_scope.md`). What actually lifts the V3/W3 conditionality is the F.2-free remainder:
  - **L4-B — DISCHARGED, Patch 0940** (`dynamical_substrate_law/l4b_vertex_uniformity.md`, 7/7).
  - **L4-A — DISCHARGED AT FIRST HARMONIC, RESIDUAL NAMED, Patch 0949 (Fable)** (`dynamical_substrate_law/l4a_rate_law_form.md`, 8/8). Forced: r₀ isotropy (arc-transitivity); the reversal-odd first harmonic B ê·n̂ is unique = MA.1's form; A-term cancels in the current, so all O(δ¹) content sees only B. Not forced: A = 0 and linear-exact — consumed only by the NESS/O(δ³) results. **V3/W3 conditionality NARROWED to "MA.1 beyond its reversal-odd first harmonic"; not lifted.**
    - **V3 re-read DONE at Patch 0950** (`chirality_derivations/review/0950_capacity1_residual_consumption.md`, 7/7). **C1 robust** — per-edge independence survives (both residual terms are per-edge functions, so no distinct-edge coupling is introduced), and the 0828 spectral bound never references the rate law, being built from the observable's weights under the pointwise floor; re-verified, 0 violations over 120 adversarial weightings. **C2 robust where it claims** — a constant A promotes the steady current from δ³ to ~A²δ (two orders) at small δ, but C2 is stated at the physical bias, and at δ = φ⁻³ the current spread across A ∈ [0,1] is a factor of 2 with O(J²) ≤ 1.1e-9; divergence-free and T-odd throughout, so the symmetry argument is untouched.
      - **C3 RECOMPUTE DONE at Patch 0951 — IT CLEARS** (`chirality_derivations/review/0951_c3_klift_recompute.md`, 5/5, run in 0821's own machinery). K_lift is 0.0532 at A = 0 and 0.0526–0.0532 across A ∈ [0,1] and κ ∈ {±0.5, ±1, ±2}; worst case /K_c = 0.64 uniform (36% margin) and 0.20 staggered (80% margin); correlator stays short-range (|C_d2/C_d1| ≤ 0.008). Structural reason: **η is a sign**, so a reversal-even per-edge SCALE only reaches the correlator through relative within-vertex weighting — second order on ρ. **Correction to 0950:** K_lift is not computed from π, so the 10.9% measure shift did not transfer; 0950 over-weighted that risk (worth checking, not worth the flag's weight). **All three CAPACITY-1 conditions are now robust to L4-A's residual — the computational case is complete.**
        - **CONV-047 ADJUDICATED at Patch 0953 — QUORUM FAILED, NOT ENACTED** (`chirality_derivations/review/0953_conv047_adjudication.md`). 5 returns, **2 valid (GPT-5.6 Sol, Grok 4.6), 3 rejected (Gemini, Copilot, DeepSeek — none ran the scripts; one states in its own reasoning that it is simulating the panel; one reports impossible sub-second timings for a 47 s script)**. A five-slot win cannot be carried on two seats, so CAPACITY-1's registered wording stands unchanged.
          - **What the two valid seats establish (not a verdict, but usable):** Q1 SOUND both — the reversal-odd uniqueness survives independent audit, the result that matters most. Q2 SOUND both, caveated to CAPACITY-1's registered per-edge-measure construction rather than any stationary measure. Q5 piece-1 correct both — no escalation. Q4 both: mapping parity-correct but **κ must be recorded as scanned, not derived**. **Q3 split in label, identical in remedy:** Seat 1's preferred option (b) IS Seat 2's amendment — restate C2 at the physical bias on the tested magnitude/O(J²) bound, and stop characterising it as an A-independent "O(δ³) NESS current."
          - **RE-DISPATCH READY as CONV-048, Patch 0954.** Reviewer package `chirality_derivations/review/0954_conv048_reviewer_package.md` (self-contained, sent alone with the three scripts); internal wrapper `0954_conv048_dispatch_wrapper.md` (not sent); receiver `reviews-CONV-048.md` (0/5). **Reformatted on the founder's report that CONV-047's package was confusing to read.** Diagnosis: 0952 asked questions *about* C1/C2/C3/piece 1/MA.1 while never defining them — which is exactly how one rejected seat invented a "C2 class" and another misnumbered every question. Fixes: glossary defining C1/C2/C3 and saying what they are not; all internal bookkeeping moved to the wrapper; questions last, numbered, each answerable without cross-reference; plain-language physical setting first; return instructions that reward honest substitution when a script won't run. **Both earned repairs folded into the proposal** rather than asked about. **CONV-048 addendum returns 5/5 as of Patch 0957; STILL NOT ADJUDICATED.** GPT withdrew its Q3 falsifier; all five endorse the Q6 disposition; five agree on Q1/Q2/Q5. **But Grok and Copilot independently demanded the joint corner (negative A × odd quadratic), it was untested, and running it found the admissible domain is NOT a rectangle (the published |A| ≤ 1.025 is a C = 0 slice; at A = −1, C = +φ⁻³ the rate goes negative) and that stacking is SUPERADDITIVE (joint J² = 4.0× the sum of separates).** **All three corrections MADE at Patch 0958**, Addendum §A3 added, and a FINAL CONFIRMATION ROUND dispatched (`0958_conv048_final_round.md`) asking one question — does the corrected text still carry your verdict? — with a **pre-committed stop rule**: majority CONFIRMED ⇒ adjudicate and enact; notes recorded as named residuals rather than acted on; new findings become separate items against the enacted theorem; majority WITHDRAWN ends the campaign and banks the uniqueness result alone. **Procedural error recorded: WORKFLOW-REVIEW-ECONOMY 3(i) requires a pre-committed effort bound written BEFORE a multi-session campaign, and this campaign never had one — that omission is why each round's correction triggered another round.** **1d-β SCOPED at Patch 0970** (`chirality_derivations/sketches/0970_1dbeta_scoping.md`). **Its core question is ANSWERED and today closed both arms of its stated closure path.** 1d-β asks whether FI-C-9 is primitive or emergent, not to derive it — V1 excluded / V3 confirmed at 0927. Its PH names two routes: *unconditionalize* (discharge Mechanism A **and/or** derive pointwise non-degeneracy from the PCD layer) and the *V2 reopener*. **Both arms of the first are now discharged** — Mechanism A at 0960, pointwise non-degeneracy at 0968. PH status line was stale in two places; corrected.
          - **TARROW-2 RE-READ DONE at Patch 0971** (`chirality_derivations/review/0971_tarrow2_reread.md`, verify 6/6). **TARROW-2's conclusion is robust to the residual and STRENGTHENED by it; its order-counting is not.** Reproduced at A = 0: 1200 faces, `a+b+c = 0` to 2e-16, exactly 420 faces with nonzero `abc` at |abc| ∈ {1/8, 1/4}, slope 3.00. With constant A = 0.3 the slope drops to 0.99 — the per-face O(δ¹) cancellation fails because the effective tilt becomes `B/(1 + A m_e)`, position-dependent. **But the SAME 420 faces violate detailed balance at every A tested (0, ±0.3, 1.0): the residual changes the ORDER of failure, not WHETHER it fails, and it fails EARLIER.** `C_T = Yes`, non-reversibility and the W3 → W1 candidate all survive. At the physical bias the max cycle affinity is 6.9e-3 (A=0) and 5.8e-3 (A=0.3), so nothing is a small-δ artefact. **Structurally identical to CONV-048's C2 finding — conclusion survives at the physical bias, asymptotic characterisation does not — and the same repair applies.**
            - **OWED: a scope clause on TARROW-2 claim (i)**, restating it as "violated on 420 of 1200 faces, at O(δ³) for the pure reversal-odd first harmonic and at lower order otherwise". **A wording correction, bundled with the arc's other paste-ready corrigenda — NOT a re-derivation and NOT a panel** (no verdict moves; under R-2 this is not a fresh campaign).
            - **NOT claimed: the W3 → W1 upgrade.** It remains a candidate, as TARROW-2 has it. This re-read removes the Mechanism-A conditionality from its conclusion; it does not perform the upgrade.
            - *(superseded)* recommendation, Patch 0970 — TARROW-2 re-read against 0960: The PH states that discharging Mechanism A *"would unconditionalize BOTH CAPACITY-1 (spatial) and TARROW-2 (temporal)"*. **That prediction is now testable and nobody has tested it.** One session, bounded, same shape as the 0950 V3 re-read which cleared three conditions in one pass. Would extend today's result from the spatial verdict to the temporal one.
          - **DO NOT open OPEN-SM-4(b) from this lane.** That is where the genuinely deep question lives — *"symmetry breaking [600-cell] × ℤ₂ → [600-cell]; derive χ = φ⁻³; reproduce δ_CP ≈ 195°, sin²θ₁₃ ≈ 0.022, and baryon asymmetry"* — but it is a **flagship programme**, cross-sector (SM/SR), and gated on EW development. Not scopeable from inside the chirality lane.
          - **Correction recorded:** the lane's own framing of 1d-β as "derive FI-C-9 itself" (0968-turn commentary) was **wrong**; that is SM-4(b).

*(superseded)* **PIECE 1 — ROUTE A FIRST STEP COMPLETE at Patch 0963** (`chirality_derivations/sketches/0963_piece1_route_a_first_step.md`). **The corpus DOES pin the weights and already contains the floor argument; piece 1 is an assembly job, not a derivation.** (1) Every η construction in the sub-corpus — 0819, 0820, 0821 — builds the per-edge weight as `sign det[d̂, n̂, r̂₁, r̂₂]`, i.e. **unit magnitude**; the det-coset ℤ₂ *is* a sign structure, so this is the construction rather than a modelling convenience. (2) For unit weights **participation = support** (p = 12 on the full vertex figure, 4.00 on a minimal 4-edge reading). (3) The floor argument exists at `dynamical_substrate_law/sketches/lcapa_axis2_signcorr_closure.md` §5: in 4-D an orientation is the sign of a 4×4 determinant, needing ≥ 4 independent directions — this is the source of CHIR.md's "per-vertex 4-D orientation floor", and the floor of 4 is dimensional, not chosen. **⇒ p(v) ≥ 4 for the dynamical η.**
          - **THE REAL GAP, narrow but real:** the dimensional argument gives a SUPPORT floor, not a PARTICIPATION floor, and they coincide only for unit weights. An observable with full 12-edge support but 70% concentration has p = 3.79 and fails. So everything turns on statement (1) — which is a **claim about the substrate, not a definition**: is the physically realised η necessarily unit-weighted, or can an effective/coarse-grained η acquire non-unit weights? 0820 is the coarse-graining step and preserves unit magnitude — evidence, not proof, and exactly where a reviewer will press.
          - **R-1 HOSTILE PASS RUN at Patch 0964 — all three checks CLEAR** (`chirality_derivations/sketches/0964_piece1_hostile_pass.md`, verify 6/6). **Check 1:** no construction produces non-unit weights, and **0820 §(3) already states the decisive fact 0963 left open — "the bias polarises but does NOT concentrate the reading"**: the Mechanism-A tilt shifts edge MEANS, not reading WEIGHTS, so m_eff stays 12. **Check 2:** support never drops below 11 of 12 over 200 random frames, or below 7 under adversarial lattice-aligned frames. **Check 3:** 0961's singleton-orbit worry resolves favourably — on the four [1,1,5,5] shells the achievable covariant supports are 1, 2, 5, 6, 7, 10, 11, 12, so **supports 3 and 4 are not achievable and the smallest admissible reading there is 5, not 4**; only the equatorial shell is tight at exactly 4.
          - **REVIEWER TRAP FOUND IN OUR OWN CORPUS, must be handled in the assembly patch:** 0820 §(2) says *"A 4-edge det reads only 4 (⇒ emergent)"*, which read cold contradicts the p ≥ 4 floor. It is a **superseded** statement — 0819's mean-field crossover at m ≈ 8, replaced by 0828's refined-chord bound under which p ≥ 4 ⇒ ρ ≤ κ(0.5) = 2/3 < 1. A reviewer will read 0820 (it is where the uniform-weight claim lives), hit §(2), and read it as our corpus contradicting our floor. **Left unaddressed this is the single most likely falsifier vote in the next dispatch.**
          - **PIECE 1 ASSEMBLED at Patch 0965 — DRAFT, not registered** (`chirality_derivations/0965_piece1_assembly.md`, verify 6/6). Claim: p(v) ≥ 4 at every vertex for the dynamical η. Chain: **(a1)** det-coset ℤ₂ is a sign structure, weights unit magnitude by construction — *definitional*; **(a2)** the dynamics does not deform those weights — **EVIDENCED, NOT PROVED, the load-bearing link**; **(b)** unit weights ⇒ participation = support — *proved*; **(c)** 4-D orientation needs ≥ 4 independent directions ⇒ support ≥ 4 — *proved*. Assembled result: minimum p(v) = 11.00 over 150 frames × 120 vertices (floor 4); 0964's adversarial frames give 7. **0820 §(2) reconciled up front** against 0828's live bound. **A tautological non-test was written and then rejected** — a δ-free weight function observed to be δ-free proves nothing about the substrate; T3 is labelled a structural observation and the real evidence is T4, an independent reproduction of 0820's MC (C_nn = −0.0545 at δ = 0 vs −0.0542 at δ = 0.10).
          - **HONEST FRAMING FOR THE PANEL:** closing piece 1 this way **replaces** a quantitative assumption (p ≥ 4) with a structural one (the dynamical η is the undeformed det-coset sign-reading). A real improvement — the structural claim is what the corpus already builds and is definitional to "det-coset" — but a replacement, not an elimination, and the panel must be told so in those words.
          - **OWED ITEM DISCHARGED + THREE PANEL-DEMANDED FIXES MADE at Patch 0966** (`chirality_derivations/0966_piece1_physical_delta.md`, verify 6/6). Five pre-dispatch returns were unanimous HOLD; all four of their substantive corrections are now in.
            - **Grok's decisive objection answered first** — "C_nn is a proxy; if it's insensitive to a drop from p=12 toward 4, a 3e-4 shift is not evidence." Tested: C_nn = (2/π)arcsin(1/p), so C_nn(12) = 0.0531 vs C_nn(4) = 0.1609, **a factor of 3.03 across exactly the disputed range** — the proxy is strongly sensitive. **And the null result therefore converts into a BOUND: |ΔC_nn| ≤ 3e-4 excludes any p below 11.93.**
            - **Physical-bias test DONE properly:** six δ values through φ⁻³, six independent MC replicates each, standard errors, and **p_eff reported directly**. At δ = φ⁻³: **p_eff = 12.24** (floor 4), shift from δ=0 is 0.0008. **Trend runs the helpful way** — p_eff *increases* with δ at +0.92/unit, so the bias slightly de-concentrates.
            - **Link (c) RESCOPED, universal form WITHDRAWN.** GPT: "four vectors to DEFINE chirality ⇏ four coefficients to READ it" — correct, since only one of {d̂,n̂,r̂₁,r̂₂} is an edge direction. What carries (c) is scope: a single-edge det is **frame-dependent** (sign flips under 98/200 admissible frames), hence not an invariant reading; the canonical observable is the whole-vertex-figure orientation. **CAPACITY-1's η must be explicitly scoped to it.**
            - **Headline sentence WITHDRAWN and corrected** (GPT and Grok independently): not "V3 unconditional on the axioms" but *the quantitative floor is discharged and **replaced** by a structural identification that remains explicit unless separately derived*. 0965 amended in place.
            - **CONV-049 ADJUDICATED AND ENACTED at Patch 0968 — piece 1's numerical assumption DISCHARGED.** A = 5/5 YES; B = 3 YES / 2 NO. **Enacted in the dissent's form, not the majority's:** GPT and Grok both showed "whole vertex figure" names the index set of the sum and does not force nonzero terms, so the majority's definitional inference would have smuggled the floor in by a name — and Gemini's YES was itself reasoned from the dissent's geometry. **Link (c) is now the 3-plane lemma** (`code/0968_three_plane_lemma.py`, 5/5, verified independently of the seat that supplied it): at most 5 of the 12 first-shell directions lie in any admissible `span{n̂,r̂₁,r̂₂}` (5 at 94 vertices, 4 at 26), so support ≥ 7 everywhere and `p ≥ 7 > 4`. Explains 0964's hostile minimum of exactly 7. **CAPACITY-1 now carries: the axioms, the derived MA.1 first harmonic, and the explicit structural premise that the dynamical η is the undeformed det-coset sign-reading — evidenced, not derived. NOT unconditional, and must never be described as such.** V3/V1 unchanged, count unchanged. **CONV-049 CLOSED at one dispatch; the effort bound held.**
          - **Dispatch-mechanics failure recorded:** GPT did not receive the two scripts and honestly declined to claim counts. **Future dispatches must confirm attachments reached every seat** — a reviewer who cannot run the code can only audit the prose.
          - *(superseded)* dispatch record, Patch 0967: — `chirality_derivations/review/0967_conv049_reviewer_package.md` (self-contained, sent alone with the two scripts); receiver `reviews-CONV-049.md` (0/5). **Both pre-dispatch seats lifted their HOLD: GPT "READY FOR R-2 DISPATCH… further pre-panel work would start answering the panel question instead of preparing it"; Grok "HOLD lifted for R-2 dispatch, HOLD retained on registration as axiom-only V3."**
            - **EFFORT BOUND WRITTEN AT DISPATCH (clause 3(i) — the CONV-047/048 miss not repeated):** dispatch 1 of at most 2; majority YES on both A and B ⇒ enact; majority NO on A ⇒ abandon, piece 1 stands, no further dispatch; majority NO on B ⇒ one revision and at most one further dispatch, then abandon; notes are named residuals and do not trigger a round, and reviewers are told so.
            - **Question B carries GPT's precise joint verbatim, unanswered by the lane on his instruction:** does the corpus definition of the whole-vertex-figure reading actually *require* nonzero unit-magnitude contributions from ≥ 4 edges, or is "whole vertex figure" merely a label from which support is inferred?
            - **Three limits carried into the package rather than left to be found:** p_eff is an inversion of C_nn under a Gaussian relation, not a weight census; **the MC freezes the weights and moves only edge means**, so it cannot show the substrate is incapable of deforming them (Grok's precision, adopted verbatim); (c) is scope, not dimension.
            - **Founder's mechanical action: send the reviewer package + the two scripts to five seats; paste returns into `reviews-CONV-049.md`.**
          - **Three things a panel should press on, named in the draft:** (1) is the structural conditionality acceptable in place of the quantitative one; (2) does (c)'s definitional exclusion of sub-4-support observables assume the conclusion; (3) the δ = 0.10 vs φ⁻³ gap. (making V3 unconditional is verdict-adjacent; under R-2 a fresh campaign). **R-1 hostile pass first:** does any coarse-graining or effective-η construction produce non-unit weights; is a minimal 4-edge reading realisable on the vertex figure or does the construction always read all 12; do 0961's singleton-orbit shells admit a unit-weighted observable with support < 4.
          - **Revised estimate vs 0961's "a day or a year":** the derivation is a day; assembly + hostile pass + panel is two sessions and one dispatch.
          - **Route C (CAPACITY-1B, banked 0925) is no longer the likely play** — it was the fallback if piece 1 proved a programme, and it does not appear to be one.
          - **Correction to 0961:** it said the weights "must be derived from the dynamics". They already were; they were never stated in one place as a claim.

*(superseded)* **PIECE 1 SCOPED at Patch 0961** (`chirality_derivations/sketches/0961_piece1_scoping.md`) — now the sole live conditionality on CAPACITY-1. **(a) Both natural candidates clear the floor:** sign weights give p = 12 everywhere (the maximum on 12 edges, 3× the floor of 4); |det| magnitude weights give p ∈ [5.33, 12]. Reaching p = 4 needs ~70% of the weight norm on one edge. **(b) 0924's worry points the wrong way** — the n̂-extremal vertices are the BEST case (poles: Stab_v = I_h order 120, transitive on all 12 edges, p = 12); the magnitude-weighted minimum is equatorial. **(c) THE SYMMETRY ROUTE IS CLOSED** — four of nine shells (the 48 vertices at v·n̂ = ±0.809, ±0.309) have edge orbits [1, 1, 5, 5] under Stab_v, so a covariant observable may put all weight on a singleton and reach p = 1. Symmetry permits exactly the collapse piece 1 must exclude. **Route B eliminated, not untried.**
          - **Piece 1 is the η-IDENTITY problem:** not "is some observable non-degenerate" (CAPACITY-1 already quantifies over the whole class) but "which observable does the dynamics single out, and what are its weights?" Since symmetry does not force it, the weights must come from the PCD cycle.
          - **RECOMMENDED NEXT — one session, Route A first step only:** determine whether the corpus already fixes the dynamical η's weights (the det-coset construction may pin them). Definite end; decides everything downstream. If pinned and sign-like or |det|-like, piece 1 closes almost immediately; if not, it is a research programme.
          - **Route C fallback exists and is drafted:** `CAPACITY-1B` at Patch 0925 — unconditional on piece 1, stated as a domain of quantification, weaker headline. Needs a patch plus a panel, which under R-2 is a fresh campaign.
          - **Correction owed if 1B is ever fired:** 0924's "degenerating at n̂-extremal vertices" framing is misdirected; the exposure is the singleton-orbit shells, which are near-polar, not extremal.

**CONV-048 ADJUDICATED AND ENACTED at Patch 0960 — final round 2/2 CONFIRMED WITH A NOTE.** THEO-CHIR-CAPACITY-1's Mechanism-A conditionality now reads "MA.1's reversal-odd first harmonic (derived, Patch 0949) + per-edge independence + piece 1"; not conditional on A = 0 nor on first-harmonic truncation at framework scale; C2's O(δ³) characterisation retired. **V3/V1 verdicts unchanged; theorem count unchanged; piece 1 remains the live conditionality.** Five named residuals carried on the theorem, the binding one being: **residuals are coupled (4.0× superadditive), so no general compositional-robustness principle may be inferred and any new residual must be assessed JOINTLY.** Registered in `theorem-registry.md` and `frontier_sectors/CHIR.md`. **CONV-048 CLOSED — no further founder action on this campaign.** Prior status, Patch 0959: ("nine turns is a lot of effort for me"). Founder's mechanical action: send `0958_conv048_final_round.md` to GPT and Grok ONLY.** Gemini, Copilot and DeepSeek are not re-asked — their stated conditions are met verbatim by the corrections (Copilot's five required edits all in; DeepSeek's four all in; Gemini required none) and their verdicts carry; their absence is not non-response. **Cause recorded against the lane: the panel gave three of four findings and one withdrawn falsifier, but every correction to the lane's own text came from the lane AFTER dispatch — all four hostile tests were cheap and runnable beforehand. An extra round costs the lane minutes and costs the founder a full manual five-seat dispatch.**
  - **R-1 ENACTED (lane discipline, 0959): run the hostile pass BEFORE dispatch** — boundary and sign-flipped cases of every free parameter; parameters JOINTLY, not one at a time; the admissibility domain of the full parameter set, not one slice; the next order of any expansion proposed for truncation. Had these run before CONV-047, all four self-corrections would have been in the first package.
  - **R-2 ENACTED: two full dispatches per claim, then a decision** — enact on reviewers' stated conditions where the text demonstrably meets them, or abandon and bank what stands alone. A third full dispatch requires an explicit founder decision made knowing it is a third. Targeted confirmation rounds to named seats do not count against the two.
  - **Owed (governance window, not this lane): propose R-1/R-2 for the CONV-001 dispatch template generally**, alongside the clause 3(i) effort-bound omission recorded at 0958. **Three of the four substantive findings in this arc since 0954 came from the panel, not the lane.** Earlier status, Patch 0955: — Gemini, Copilot, DeepSeek returned; all three ENACT WITH AMENDMENTS, none found a Q1 falsifier, all confirm Q5. **Not adjudicated; 2 seats outstanding.** The reformat demonstrably worked (Gemini disclosed honestly that it could not run the scripts, where at CONV-047 it fabricated five seats; nobody invented a "C2 class"). **PROPOSAL AMENDED at Patch 0956** — the clause "nor on the rate law terminating at first order" narrowed to "at the scale the framework gives a second harmonic", with the reversal-odd channel named as unbounded in general; §1.7 updated (whole admissible domain now tested); NEW `0956_conv048_addendum.md` reporting both gap closures and asking two follow-up questions (whether accumulated "still clears" margins concern the reviewer; whether naming the odd channel as open is the right disposition). **The three existing returns predate this and are marked accordingly — they are asked only whether A1/A2 changes an answer, not to review again.** Remaining owed: (i) request stdout from Copilot and DeepSeek — plausible timings but every figure they cite is already in the package, and Copilot's follow-up uses future tense about running the scripts; (ii) read Gemini's Q1/Q2 as T2 not T1 at adjudication; (iii) amend the proposal's "nor on the rate law terminating at first order" clause, which overstates what 0955 shows.** **Founder's mechanical action: send the reviewer package + 3 scripts to two more seats; paste returns into `reviews-CONV-048.md`.** Prior owed text: (two changes earned from the returns) (i) fold the C2 repair into the proposal rather than asking whether it is needed — that converts the one live disagreement into agreement; (ii) state the admissible A-domain instead of an unqualified "not conditional on A = 0".
          - **Q6 ADOPTED REGARDLESS (both seats raised it independently): the admissible A-domain.** Computed at Patch 0953 (`code/0953_admissible_A_domain.py`, 4/4): rate positivity `1 + A(m·n̂) ± B(ê·n̂) > 0` gives **|A| ≤ 1.025** at the physical bias, closed form `A_max = min over edges with m·n̂ < 0 of (1 − B|ê·n̂|)/|m·n̂|`; binding edge `m·n̂ = −0.9045, |ê·n̂| = 0.309`, not the |m·n̂|-maximal edge. **The tested box A ∈ [0,1] sits inside the domain and exhausts 98% of its positive half** — the objection is correct and its effect is to strengthen the record.
          - **Q6 ALSO ADOPTED: bank L4-A's symmetry result independently of the NESS conclusions** (Seat 1 Q6.2 / Seat 2 Q6.1) — the reversal-odd uniqueness is theorem-grade on its own and should not wait on C2/C3 disposition. Standing note on the C2 line: do not let "O(δ³)" re-enter the registry by habit (Seat 2 Q6.3).
          - **FOUNDER'S CALL — seat sourcing (governance, not enacted here).** Three of five returns were not reviews. The panel mechanism cannot do its job if a majority of seats can be filled by text that formats like a review without being one. **Recommendation: re-dispatch only to seats that demonstrably execute the scripts, and treat a missing or impossible COUNT-LINE as an automatic seat REJECTION rather than a discounted vote.**
          - *(superseded)* dispatch record, Patch 0952: — package `chirality_derivations/review/0952_conv001_capacity1_conditionality_package.md`, returns receiver `review/reviews-CONV-047.md` (0/5, awaiting the founder's dispatch to the five seats). Classified a WIN under WORKFLOW-REVIEW-ECONOMY 1(a) + founder request 1(c), so the full five-slot panel is required. Q1 (uniqueness) and Q3 (C2's scope at the physical bias) are the load-bearing questions; Q3 is where the lane expects an objection. **Founder's mechanical action: paste the package to the five seats, return the blocks.** Packet = 0949 + 0950 + 0951. Proposed text: CAPACITY-1 is conditional on MA.1's reversal-odd first harmonic (derived at 0949) plus per-edge independence and pointwise non-degeneracy — NOT on A = 0 or first-harmonic truncation. Verdict-adjacent, so a single window cannot close it. **Piece 1 (pointwise non-degeneracy of the dynamical η) is untouched and remains CAPACITY-1's live conditionality — a different question from L4-A's.**
        - *(superseded)* original C3 owed item, Patch 0950: |K_lift| ≈ 0.053 vs thresholds 0.095 / 0.27 is computed from the measure, and the measure shifts by 10.9% of the A = 0 tilt at the physical bias. Margins are wide and it will likely clear, but that is not a re-check. **This is the single item standing between V3 and unconditional-on-the-residual.** If it clears, restating CAPACITY-1's conditionality as "on MA.1's reversal-odd first harmonic" is verdict-adjacent and needs a CONV-001 panel.
      - **Note to the NESS holders:** the J ~ A²δ promotion is a real sensitivity of the small-δ *exponent* to a term the framework assumes away. Results quoted at φ⁻³ are unaffected; any future argument leaning on the δ³ exponent rather than the magnitude at the physical bias should carry A = 0 explicitly.
    - **OWED — theorem candidacy for L4-A+B+C jointly:** "the reversal-odd first-harmonic H₄-covariant on directed edges of the 600-cell is one-dimensional, spanned by ê·n̂; the reversal-even part is spanned by m·n̂ and cancels in the antisymmetric current." Theorem-grade; needs a panel; registry numbering to be checked at registration. Not registered at 0949 (single pass).
    - **OWED — F.1 wording (bundle with 0940/0941 items):** §4.3 replace the "Layer 3 faith" framing of MA.1's form with the forced/not-forced split; the δ–ε "not pinned" sentence should note the two forms are the same covariant (T7), values possibly not.
    - **L4-E ADDRESSED at Patch 0972** (`dynamical_substrate_law/l4e_delta_epsilon.md`, verify 5/5). **The relation IS pinned — δ = −ε at first order — and pinning it exposed an unstated physical commitment.** Reading C's `ℓ(ê) = ℓ₀(1 + ε ê·n̂)` is described as an "effective length" but `ê·n̂` is reversal-ODD, so the same edge gets two different lengths by traversal direction (0.999691 vs 1.000309). **A metric length cannot do that: Reading C's ℓ is a DIRECTED TRAVERSAL COST and the substrate is NON-RECIPROCAL** — a physical commitment the equation has always made and the prose has never stated.
            - **The counterfactual is the real finding:** if ℓ were a genuine reversal-even length (depending on m̂·n̂), then `r = c/ℓ` is reversal-even and generates **the A-term, not δ** (measured A = −ε, δ = 0 exactly). **So MA.1's reversal-odd first harmonic cannot come from a metric length perturbation at all — its form REQUIRES non-reciprocity.**
            - **Bonus against CAPACITY-1's residual:** the same expansion fixes the second-order coefficient at `+ε²(ê·n̂)²`, reversal-**even**, so **the reversal-odd quadratic `(ê·n̂)(m̂·n̂)` — the superadditive channel of 0955/0957 — has coefficient ZERO in the Reading-C realisation.** First positive statement about that channel rather than a bound. Does not close the residual (absent in *this* realisation ≠ absent in all).
            - **ANSWERED at Patch 0973 — the non-reciprocity IS the T-arrow, not a new field** (`dynamical_substrate_law/nonreciprocity_is_the_arrow.md`, verify 6/6). The founder's instinct that "it is just geometry" is **right, and that is why the asymmetry cannot be geometric**: a metric is a symmetric bilinear form, so every length built from an inner product is reversal-even on any lattice (checked over 200 arbitrary metrics, difference exactly 0.0). The 1-form that makes a directed length possible is a Randers/Finsler `β = ε n̂` — **mathematically real but not a new field**, since n̂ is already a primitive; what changes is whether n̂ enters as a direction (even only) or as a 1-form (odd available). **Decisive test: detailed-balance violation comes ENTIRELY from the reversal-odd part** — the even term A(m̂·n̂) gives max cycle affinity **exactly 0.0 at A = 0.3, 0.5 and 1.0**, while the odd term violates on 420/1200 faces. So *"costs more one way"* ⟺ *"detailed balance violated"* ⟺ *"not time-reversible"*, and with MERGE-2 (sign(δ) is P-even, T-**odd** — an arrow, not a chirality) **the non-reciprocity is the T-arrow the arc already carries as W3.** **The substrate is NOT non-reciprocal in space — its geometry is reciprocal; its DYNAMICS are non-reciprocal in time, which is what an arrow of time means.** Fizeau analogy: distance identical both ways, traversal time not, because the medium flows.
            - **PD-006(a) RULING STILL OWED, now with only two options:** accept relabelling Reading C's ℓ from "effective length" to **directed traversal cost / hop time** (equation stands, only its description was wrong), **or** defend ℓ as a genuine length and accept that δ = 0 follows (0972 T4: a reversal-even ℓ generates the A-term and no δ). **Recommendation: the first** — it removes an apparent commitment to exotic spatial geometry and replaces it with one the programme already registers.
            - **Recorded:** the identification reversal-odd ⟺ T-odd ⟺ detailed-balance violation is verified at 0973 and was not previously stated in one place, though MERGE-2 and TARROW-2 each held half of it.
            - **Owed:** F.1 wording — replace "the δ–ε relation is not pinned" with δ = −ε plus the non-reciprocity clause; bundles with the corrigenda queue.
            - **OPEN-FP-F1-2: all five sub-targets (A–E) now carry artifacts.** Parent stays OPEN on the named residuals and the non-reciprocity question.
            - *(superseded)* **L4-E lead filed:** constant-speed traversal maps ℓ(ê) = ℓ₀(1 + ε ê·n̂) to δ = −ε + O(ε²). Whether the propagation speed is genuinely constant across perturbed edges is L4-E's question.
  - **L4-C — DISCHARGED, Patch 0941** (`dynamical_substrate_law/l4c_antisymmetric_current.md`, 8/8). Consumes L4-B (not parallel to it, as 0646 has it). Recovers α₁ = 6/φ² as a check.
  - **L4-E — OPEN, low priority.** The δ–ε magnitude relation (ε = χ = φ⁻³; couples to THEO-CHIR-CHI-1).
  - **Registry unit:** theorem candidacy for L4-A + L4-B + L4-C jointly, not L4-B alone. V3/W3 stay conditional until A and C land.
- **F.1 paper — wording corrections owed (Patches 0940 + 0941; mechanical, founder recompile; bundle both).** **From 0941:** §4.3 must state what `r(−ê; v)` denotes — the reverse traversal of the same edge governed by the rate law at the far end, which requires vertex-uniformity — because `−ê` is not an edge direction at v and the literal reading has no referent; cite `l4c_antisymmetric_current.md`. Narrow exclusion-class E1 again: of Mechanism A's four framework commitments, vertex-uniformity (0940) and the current construction (0941) are now derived; the rate-law form is not. **From 0940:** §4.3's "vertex-independence … for any host vertex, not just the chosen v_host" reads as though the current is the same at every vertex; it is not — the *construction* is vertex-independent, the *value* tracks the n̂-shell (nine shells, `v·n̂`). Restate and cite `l4b_vertex_uniformity.md` in place of the assumption; narrow exclusion-class E1 ("Mechanism A as framework axiom — not derived") to the rate-law form and the current construction, the vertex-uniformity commitment now being discharged. Bundle with the Capotauro corrigendum above if both recompile together.

**Process note (D-5, recorded once):** this window booted with Patch 0936 committed locally but unpushed; the gate caught it. Verified pushed at 0937.

### TODO-3938-DM — Register and build the CPP pairing/condensation kinetics framework (NB-S3a-1) — the one unknown two lanes now wait on (registered Patch 3938, EU lane, under PD-006)

**Why this entry exists:** the founder asked (11 Sep) whether this project was recorded anywhere actionable. It was not. NB-S3a-1 was named on 17 Jul 2026 (S3a, `series_phenomena/cosmology/dark_matter/relic1_s3a_uq_from_registered_anchors.md` §1: *"the CPP pairing/condensation kinetic framework (σv, rate equations vs expansion) is unregistered... Route α is closed for this campaign until that framework exists as its own registered project"*) and then lived only in eight July DM-lane handovers. Same failure shape as TODO-3930-EU. Registered here, in `frontier_sectors/DMDE.md` (OPEN-DM-PAIRING-KINETICS-1) and in `future_projects.md` (Project 00d) at the moment the second consumer appeared.

**What it is:** a registered rate framework for CP pairing and DP-entity condensation against expansion — cross-sections/rates for the evaporation → re-stack-or-escape → pair → aggregate chain (founder, founders_voice/3934 §4), so that populations at lock-in are *computed* rather than back-solved. Lane: DM (3500s block) with FP input; PD-007-sensitive (rates are new constants unless derived).

**Two consumers, stated so the project is not built blind:**
1. **S3a Route α** (DM lane): derive U_q from kinetics instead of back-solving it from η_B (Route β). The retro-prediction structure of S3-M1 (2520) is the target the result must reproduce.
2. **OPEN-EU-PHOTON-GENESIS-1** (EU lane, 3936–3937): C-5's adiabaticity passes iff the unpaired-+qCP inventory scales with local qCP density as n_q^p with **p ∈ [0.21, 0.48]** (linear release at ε = α_s/α = 2.70). The chain's structure predicts sub-linear, non-zero p; the framework decides whether it lands in the band. This is the only remaining condition on the EU lane's live amplitude candidate.

**OPENED 11 Sep 2026 on the founder's call — charter Patch 3508** (`OPEN-DM-PAIRING-KINETICS-1_charter.md`). Third consumer: the OPEN-DM-RELIC-1 reopening contract (dial x). **All four questions answered (3509, 3510); transition graph fixed (`kinetics1_transition_graph.md`). Next action (worker, multi-session): the residue-fraction computation under affinity-biased Poisson landing with count-law dilution, read once against D1 (p ∈ [0.21, 0.48]) and D1′ (R₊/R₋), for BOTH signs; then the paired population for D3; then the re-derivation of the S3-M1 sinks with a symmetric anti-quark channel and annihilation (D4, 2520 §2 superseded in part at 3511).** **Residue computation DONE Patch 3512** (`kinetics1_residue_computation.md`): D1′ read (R₊/R₋ = 1); D1 reduced to the terminal dilution condition — on the engine alone p → 0, constant H gives p = 1, the band lies between and is set by where the count law's dilution stops (not registered); C-5 conditional under the charter's band rule. **3513: founder answered in mechanism** (repulsive era carries dilution; third captured as a trio; residue = knock-off yield) **but not in rate — still blocked on the repulsive era's Moments-per-e-fold at the freeze and whether the interior thins.** 3516: founder's contraction worry answered from the corpus (not fatal); the repulsive-era driver is in tension with 3805 — the post-count-law dilution is the reheating release, EU lane, rate open. **3517: FORK for the founder — thermal freeze (kT through the qDP binding; band natural; needs E_b) vs dilution freeze at Planck kT (3510 Q7; needs a quench nothing supplies).** Blocked on that ruling. 3518: the exclusion rule is retired (R-EXCL-RETIRED) and not needed — the Planck-era escape is the hop rule + count law; the thermal freeze is post-count-law only. **3519: RESOLVED — the residue is thermal (R-RESIDUE-THERMAL); the orientation trap 'do not borrow freeze-out; the cutoff is by dilution at Planck kT' is SUPERSEDED (freeze-out IS the mechanism; 16.5 keV stays retired). 3520: DONE — D1 read: p = 0.016 on registered inputs, C-5 FAILS D1. Reopening route only: a DERIVED cocoon suppression of lone-qCP pairing by ~1e17–1e18 (qstiff/contact-polarizability is the nearest tool) landing in λ ≈ 10–30; a chosen suppression is post-hoc. D3/D4 not reached; item closes unless the founder opens the cocoon derivation.** **3521: the founder names the matter asymmetry (a in n_B = a·R) as the real issue; worker agrees — R₊ = R₋ exactly, so all of η_B is a; the handedness (χ/6 ≈ 0.039, THEO-CAP-1/THEO-SD-CHIR-2) and the freeze (3520) are on file, the sign-selection mechanism (Q7.1, scoped 0441, never worked) is not. Recommended: charter OPEN-DM-SIGN-SELECTION-1 (founder's). Signs supplied 3522: matter = −eCP and +qCP centres; antimatter signs sequestered as hDP-B inside hTetras (DM sector). Mechanism candidate on file: THEO-CHIR-CONT-3's chiral stabilization-energy ΔF applied to hDP-A vs hDP-B, amplified at the 3520 freeze; bottom→kaon ruled out as the mechanism (epoch, reach, size). **3523: the sign IS on file for the qDP sector — THEO-CHIR-CONT-3 / SM-2 v1.0 §10: −qCP-centred LZBW configurations preferentially stabilised (ΔF^{qDP} > 0). Only hDP-B can be −qCP-centred ⇒ B stabilised, A breaks ⇒ matter = −eCP, +qCP — the sign comes out right from the registered operator. Charter items: (a) transfer of ΔF from qDP to hDP (redo C-W46 with an eCP partner); (b) SM-2 §10 sign-chain consistency; (c) a at the freeze and the implied cocoon suppression (~1e9–1e11) vs the derived one; (d) the A/B split in ribbons/chains/balls. Founder to open OPEN-DM-SIGN-SELECTION-1.** **3524 CORRECTION: −qCP centres are ANTI-up/anti-down (founder). SM-2 §10's '−qCP centres stabilised' explains the anti-down, not the down — corrigendum candidate for SM-2 §10 and the chirality-continuum Sector B sketch (SM lane, CONV-038). 3523's 'sign without a choice' WITHDRAWN as stated: §10-corrected (S = +qCP) gives the WRONG sequestration sign under naive transfer; §10-as-written gives the right one but breaks up/down. Charter item 1 is now: settle S (SM lane); item 2: which CP is the hybrid's centre (DM lane, derivable). The only-hybrids symmetry statement stands.** **3525: founder — a free pair has no centre (both members displaced oppositely by one SSV_net); the centre exists only in the dressed quark. The centre-transfer route to an hDP-A/B split is CLOSED. Candidate reading offered: pair-breaking symmetric (D1′), DRESSING asymmetric — the chirality (S = +qCP, §10 corrected) stabilises +qCP centres as quarks, −qCP centres fail and re-pair into B; a = dressing selectivity at 2543's window. Charter items replaced: (a) SM corrigendum S = +qCP load-bearing; (b) ΔF_dress and a = tanh(ΔF/2kT); (c) eDP-sector electron counterpart; (d) DM B-content = dressing deficit. Founder's to open.** **3526: founder — 'the story works if the −qCP dresses better'; ambiguous (stays lone vs is wrapped and sequestered); clarification asked. Worker: the sign of ΔF_dress is a geometry computation — a radially polarised shell on a ± centre in the 600-cell of stated handedness — magnitude χ/6, sign fixed by the substrate's screw sense (initial condition, Q7.1 (b)/(c)); cannot be chosen to make the story work; pre-register the cross-check against PRED-O-25 as the falsifier.** **3527: FOUNDER RULED reading (i) — +qCP dresses better and survives; −qCP decays back into hDP-B. OPEN-DM-SIGN-SELECTION-1 CHARTERED (`OPEN-DM-SIGN-SELECTION-1_charter.md`, readings E1–E4 pre-registered; the sign is E1, from geometry with the handedness as input, never chosen). NEXT: the first computation (charter §6) — ΔF_dress for a radially polarised shell on a ± centre in the 600-cell of stated handedness; read E1. Owed to SM lane: the §10 corrigendum.** **3528: E1 COMPUTED — quark sector S = +qCP PASS conditional on the C-W46 convention (600-cell + F.1 Thm 5.1: the cocoon is polar w.r.t. n̂ = v_host, shell factor 1/(2φ)); lepton sector NOT PASSED under an electric-polarity rule (electron destabilised) → the composition needs a species-dependent chiral sign — LOAD-BEARING, owed to the SD/chirality lane (joint qDP/eDP theorem). **3529: founder's rules — the lepton asymmetry is INDUCED via bare −qCP + dressed +eCP → hDP-B + γ + ν; the mirror channel (bare −eCP + dressed +qCP → hDP-A) loses by exp[(ΔF_q − ΔF_e)/kT] or better since E_qDP = 3E_eDP; 3528's lepton fail not fatal; charter amended (E2 two-channel rate; E3 neutrality count; E4 γ+ν signature). **3530: FORK-DM-COMPOSITION-1 — SM-2's down = −qCP centre + linear extra vs the founder's down = +qCP core + radial −eCP (session 16x, 3513, 3524). 3524/3528's '§10 is a slip' corrected: §10 matches SM-2's own assignment; the disagreement is composition-level. BLOCKING: founder to confirm SM-2 superseded; then the SM corrigendum is the cage assignment + §10 + the down mass fit. Derived E3 count under the founder's composition: R_e⁻/R_q⁺ = 2/3 exactly. E2 blocked (E_coc's identity is composition-dependent). **3531: RESOLVED — founder reconfirms down = +qCP + linear −eCP + orbital eDP + cloud; SM-2 corrigendum composition-level (SM lane, owed). E3 STRUCTURED: two-channel sequestration forces q⁺ = e⁻; the 2/3 ratio requires the partnerless-third channel with net W − W′ = n_p + n_n (one bare −qCP per baryon in the DM sector); N_e drops out; N_q = 3B + X_A + Y + W′. **3532: E1 DOWNGRADED to OPEN — C-W46 splits only the {+ host/extra outward, − host/extra inward} doublet; the + host's inward cocoon is in the complementary subspace, sign not on file; 3528's rule was an extrapolation (cases: S = −qCP / none / S = +qCP). OWED to the SD/chirality lane: extend C-W46 to the 4-state representation and state the sign of the |+, −v⟩ class (= the corrected down quark's class; same sign the SM-2 corrigendum needs). **3533: E1 sharpened — the doublet cannot decide (any α fits); every physical extra is inward; case (a) sign-only EXCLUDED by the corrected §10 (the + host's inward extra is stabilised); open between (b) placement-only (no selectivity) and (c) dipole-orientation (S = +qCP). DECIDING QUESTION for the SD lane: does a DP's energy in the n̂-asymmetric substrate depend on which way its dipole points along n̂? NEXT: (i) that mechanism statement (SD lane) — **ANSWERED at 0936 (chirality lane), to be read by the DM window next session**; (ii) E_coc → E2; (iii) E3 numerically.**

**Deferrals audit, Session 227 (Patch 3535) — items put aside in this window that had no todolist line of their own:**
- **(DM-1) SD lane — C-W46 consistency note:** its doublet state |+, v⟩ (extra along +n̂) is not a first-shell configuration (F.1 Theorem 5.1 puts every neighbour at û·n̂ = −1/(2φ)); the physical pair is (+, inward) vs (−, inward). Goes with the E1 mechanism question (3533). Chirality lane, 0900-series (next free 0936).
- **(DM-2) Parked candidate motive forces (3517, no rates on file):** the DP sea relaxing to its vacuum spacing (exclusion pressure of freshly formed DPs); photon pressure from pairing/annihilation. Not needed by the thermal picture; kept so they are not re-invented.
- **(DM-3) E4 falsifier pointers (charter §4, 3529):** one γ + one ν per removed antilepton (vs 2γ); dark matter's B-content = the dressing deficit plus one partnerless −qCP per baryon (3531). Both need an observational handle from the DM lane before they are PRED-registrable.
- **(DM-4) Closed, recorded so it is not reopened:** 3528 §4's 'eDP-sector sign' is moot — the lepton asymmetry is induced (3529); 3512's dilution-only results stand as results about a superseded model; the C-W46 'orientation convention' is not a convention (3532).
- **(DM-5) λ (the lone-qCP pairing strength) is not on file;** it is the cocoon's pairing-suppression role, one object with E_coc (charter E3). Covered by item (ii) above; listed so the name 'λ' resolves.
 **0936/0937 (chirality lane): (i) DONE — E1 = case (c), S = +qCP, derived; see TODO-0937-CHIR for the normalisation flag on (ii).** Flag: a ~ 0.05–0.3 with η_B forces R ~ 1e-8 — opposite to C-5's need.** Then the trio dynamics, D3, D4. Cross-lane flag raised to the EU lane (like-charge push vs 3805 cancellation). FP-lane question registered: is the founder's conformational asymmetry Capotauro's χ? Multi-session.

### TODO-3930-EU — EU-lane owed items, Sessions 169–223 (registered Patch 3930)

**Added 13 Sep 2026 (Patch 3535, deferrals audit of Session 227 — these were flagged from the DM window and recorded only in DM lines; they are EU-lane items):**
- **(EU-a) The post-count-law dilution's owner.** 3516: the founder's 'repulsive era' (like-charge repulsion driving expansion after superposition ends, 3513) is in tension with 3805's 'the push neither expands nor collapses'; the corpus's own post-count-law driver is the *release* of the stored like-charge self-energy at de-saturation (3710 iii, OPEN-EU-REHEAT-BUDGET-1). Resolve which, and at what rate in Moments per e-fold. Consumer: the thermal residue's H(T) (3520).
- **(EU-b) CPP has no post-inflation H(T).** 3520 ran on the radiation-era form as an external input (the charter's 'MeV-epoch H'). A CPP-derived H(T) for kT ≲ E_qDP is owed; it moves the λ scale of 3520's table, not its shape.
- **(EU-c) Annihilation photon channel and the 17–23% composition contribution** (3936 §4, 3511 flag ii) — fold into C-5's accounting only if C-5 is reopened (3520: failed on the record).

**Registered late, and that is the point of the entry.** This arc ran 55 sessions and put **nothing** in this file; every owed item lived in handovers, which are **superseded every session**. The founder asked where these were tracked. **They were not.**

**Owed to other lanes (maintainer routing required — cross-lane sanction is not a worker act):**
- ~~**FP lane — the existential gate on C-5.**~~ **CLOSED AS REFRAMED, Patch 3934** — the question was ill-posed (B and L are not fundamental in CPP, SF-2) and the freeze-out kinetics it needs are not on file in the FP/DM lane either (S3a Route α blocked); condition restated as a photon-genesis question, **OPEN-EU-PHOTON-GENESIS-1** (non-blocking, search mode), founder's candidate mechanism registered. No FP-lane action required. *Original text:* *Does a local enrichment in Q-dominant SCPs shift η_B or the lepton asymmetry, or is the Q:E composition orthogonal to the leptogenesis sector?* **Framed in FP's terms at `series_phenomena/cosmology/early_universe/review/eu_outbound_questions.md` §1.** If it carries net B or L, **C-5 dies by ~30×**.
- **CONV-046 dispatch** — package **v1.2** (Patch 3939: adiabaticity condition restated per 3934–3937; v1.1 superseded, do not dispatch). `.../early_universe/review/conv046_eu_amplitude_arc_review_package_v1.2.md`. Economy audited at 3926; no further amendment pending.
- **The amended DE escalation** (3858) — the counting bound, re-pointed at DE-lane completion.
- ~~**`cosmic_web_generation_constraints.md` owed piece 1** (3833).~~ **DONE Patch 3935** — annotated: piece 1 discharged as blocker (0729 citation expired at 0778); piece 2 → OPEN-EU-PHOTON-GENESIS-1.
- ~~**`DM_project_map.md` is STALE** on the DM particle's identity (3884) — cross-lane, never edited.~~ **DONE Patch 3935** — staleness banner added naming the 3426 ring identity; body left for the DM lane.

**Owed by Isak (mechanical):**
- **Recompile EU-1 at V1.6** — **two versions behind**; and GR-2 at V2.11.

**Owed into EU-1 V1.7 (bundle when the recompile happens):**
- the **amended κ\* wording** — *A_s foreclosed **given the present assignment** H ∝ μ*, **never "permanently"** (3906 as corrected by the CONV-046 return at 3914);
- **the "83 orders" must not appear anywhere** (retracted 3918 — it used the bare inventory);
- the §Background **VSL clarification** (3854);
- the physical reading of eq. Nstar (3876 §5) **as qualified by 3878**.

**Master handover (Patch 3933):** `handovers/2026-09-11_EU_ARC_MASTER_HANDOVER_3816-3932.md` supersedes every individual EU handover of this arc. **Read its §0 before anything else.**

**Cadence (Patch 3932):** the **§15 session close fires at CONTEXT-WINDOW turnover or on the founder's call — not every turn** (D-8). Across Sessions 169–224 it fired per turn; **~half the lane's patch output was turnover bookkeeping for turnovers that did not happen.**

**Open, non-blocking:** OPEN-EU-LATTICE-EXTENT-1 (3878) — the lattice's extent is unspecified in the corpus; possibly a foundations question.

**NOT owed, and recorded so it is not re-opened:** the **cosmological-constant residual** belongs to the **CC lane**, where **F-CLI-1 is already FIRING-PENDING-SCRUTINY**. The EU lane touched it only through an error (3906) and a retracted patch (3920, retracted 3922). **There is no EU-lane CC work item.**

### TODO-2957-A — Correct master-glossary DI-bit entry per founder phase ruling (P1) — EXECUTED Patch 2989

Founder ruling 2 Aug 2026 (Patch 2957 P-1): DI-bits carry {charge, type, origin address}, count-like
magnitude — NO phase. Registered glossary entry claims "phase, amplitude, and polarisation" — conflict.
Correct the entry with the ruling cited and the superseded text preserved in a history note
(anti-erasure). Blocked only by nothing; execute after the Fork-A/B ruling lands so one edit carries
the full pinned content. **STAGED Patch 2988**; **EXECUTED Patch 2989** on founder ratification of AP-2 (verbatim registered at `series_phenomena/cosmology/dark_matter/founder_registration_2989_ap2_ratified.md`): entry replaced with the pinned content + falsifiers + anti-erasure history note; 2982 editorial flag removed; AP-2 registered into the A1′ row of `axiom-registry.md`. CLOSED.

### TODO-2957-B — QM-1 phase-provenance audit (P1) — EXECUTED Patch 2988

If DI-bits carry no phase, where does quantum phase live? Candidate: the DP-displacement PATTERN
level (Sea polarization configuration), DI-bits as sub-pattern carriers. Audit QM-1's shipped
"hopping amplitude → Schrödinger" derivation for survivability under re-grounding. Until resolved,
QM-1 lineage may NOT be cited as evidence in the RELAY-MECH-1 arc (2957 §3 withdrawal). Registered
Patch 2957. **BAR STATUS UPDATE (Patch 3000, CONV-014 adjudication): bar → PARTIAL.** Admissible
with a mandatory conditional note (naming OPEN-QMRG-B1 + R-4): the pattern-level phase-location
claim (FI-QMRG-1 as amended, incl. pattern rotation + SF-6 consistency) and the formal
mathematical results cited AS formal results. Still barred: B-QMRG-1's truth, unitarity beyond
the sketch Proposition, plane stability, un-noted phase interpretation. Scope authority:
`series_quantum_mechanics/conv014_adjudication.md` §6 E-1. **WIDENED at Patch 3004 (CONV-015):** additionally admissible with the conditional note (now naming OPEN-QMRG-R4-MULTILINK + OPEN-QMRG-B1-CONST): FI-QMRG-1 as the registered realization; exact shipped-class plane stability + (kΔs)⁴ single-edge suppression; B-QMRG-1 proportionality lemma; sketch-grade unitarity with regime visible. Still barred: universal microscopic stability; exact B1 constant / fully-derived 1/(2ω) coefficient claims; uniqueness; beyond-regime unitarity; closed-theorem citations in strict-proof contexts. Scope authority: `conv015_adjudication.md` §6 E-1. **TERMINAL UPDATE (Patch 3008, CONV-016): sector conditionality RESOLVED; bar WIDENED NEAR-FULL; notes removed per-obligation. Persisting note classes ONLY: η-universality/mode-independence (OPEN-QMRG-ETA), physical ρ-calibrated normalization, uniqueness (OPEN-QMRG-UNIQ criterion), universal-microscopic claims beyond the ratified registry (W-MULTILINK-1). Scope authority: `conv016_adjudication.md` §6 E-2.** **EXECUTED Patch 2988** — audit record at `series_quantum_mechanics/qm1_phase_provenance_audit.md`. Verdict: shipped per-bit phase grounding RETIRED (contradicts P-1 AND A1′ reset-per-hop); mathematical spine (tight-binding → Schrödinger, T = ℏ²/(4mΔs²), Madelung/Q) is grounding-independent → QM-1 result DEMOTED TO CONDITIONAL on OPEN-QM-1-REGROUND (pattern-level phase); **AP-2 CLEARED for ratification** (no shipped mathematics consumes DI-bit phase). Citation bar continues until the re-grounding revision ships. Follow-on sweep TODO-2988-A (QM-2..6 + SF-6 attribution check).

### TODO-2988-A — Downstream phase-attribution sweep: QM-2..6 + SF-6 (P2)

The Patch 2988 audit confirmed QM-1's phase attribution to DI-bits is prose-layer, not
math-layer. QM-2's Born-rule grounding ("DI-bit interference pattern", glossary line 210) and
QM-3..6 + SF-6's citations of the QM-1 lineage need the same attribution-layer check and, where
contaminated, relocation to the DP-displacement pattern level. Expected similar in kind to the
QM-1 finding; each paper gets its own line-cited inventory. Registered Patch 2988. **EXECUTED
Patch 2995** — sweep record at `series_quantum_mechanics/qm_series_phase_attribution_sweep.md`.
Verdicts: QM-2/3/4/5 PROSE-LAYER; QM-6 PROSE-LAYER at PRIMITIVE-DEFINITION severity (highest
revision priority — §1 states the retired ontology as the four primitives); **SF-6 CLEAN**
(pattern-level already; lineage-conditional by citation only; registered as re-grounding
template asset SF6-A1). No paper math-layer contaminated; the 2988 S-1 separability propagates
series-wide. Glossary Born Rule entry confirmed as overstating the shipped math (QM-2's proof
is already P-2-compliant); edit rides the OPEN-QM-1-REGROUND revision pass. CLOSED.

### TODO-2952-A — Reconcile "ZDC" (SF-6 shipped vocabulary) with the founder's ZBW-chain picture (P2) — RESOLVED Patch 2953/2954

At FOUNDER-Q-XI2-1 (2 Aug 2026) the founder did not recognize "ZDC pattern"; ZDC ("Zero-point
Dipole Chain") appears ~33 times in SHIPPED SF-6 v1.0 as a core term, while the founder's vocabulary
is ZBW (glossary-registered). PCD-drift-class event ("Polarize, Capture, Depolarize" precedent).
Task: confirm with the founder whether SF-6's ZDC definition faithfully renders his ZBW-chain
concept; then either record the synonymy in `master_glossary.md` or open an SF-6 terminology
correction. Also pending the same pass: the founder's "subquantum divisions" definition (recorded
verbatim at `series_phenomena/cosmology/dark_matter/founder_q_xi2_1_answered.md` §1) as a glossary
candidate. Registered Patch 2952. RESOLUTION (2 Aug 2026): founder ruled — ZDC NOT entered in glossary; SF-6 rewritten replacing the ZDC acronym with ZBW-rooted "ZBW chain" language (NOT a strict synonym: chain of ZBW oscillators vs the oscillation; blind substitution avoided). Executed Patch 2954. Still pending from the same pass: founder ruling on the "subquantum divisions" glossary candidate.

### TODO-2946-A — Recover full verbatim Grok/Gemini/Muse/Qwen A5-DISP cycle returns (P2)

Full texts recoverable from the 2 Aug 2026 session transcript (/mnt/transcripts) and Thomas's paste
records; deferred at session close under context pressure per Step D deferral discipline. Evidentiary
excerpts + GPT and Llama full texts already at review/a5_disp_combined_cycle/. Registered Patch 2946.


### TODO-3535-SM — SM-2 composition-level corrigendum (owed by the DM window, 3524/3530/3531/3533)
SM-2's Particle Cage Assignments give the down quark a −qCP centre with a linear ZBW extra, and §10 ('chirality preferentially stabilises linear ZBW extras on −qCP centres') is consistent with that. The founder's ruled composition (session 16x notes; 3513; 3524; **3531 reconfirmed**) is: down = +qCP core + linearly oscillating −eCP + orbital eDP + polarised cloud; −qCP centres are anti-up/anti-down. **Owed:** corrigendum by the CONV-038 path covering the cage assignment, §10's sign (S = +qCP for the corrected object — 3533: this excludes the sign-only coupling), and whatever the down-quark mass fit relied on. The chirality-continuum Sector B sketch §15 inherits §10's sentence and needs the same fix. The sign the corrigendum carries is the same sign OPEN-DM-SIGN-SELECTION-1's E1 needs.

### TODO-3535-REG — the chirality window's 0900-series is not in `id_block_registry.md`
The block table lists only the 3xxx lanes; the chirality lane's pointer lives in `project_ledger.md` alone (highest used 0935, 18 Jun 2026; next free 0936). Add a row when 0936 is written.

### TODO-001 — SS-9 Phase 7 Section A 7-companion documentation suite

**Status**: DEFERRED pending external-feedback trigger; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: The Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35-48) defers this until SS-9 is unambiguously done — meaning until either (a) v1.x revision ships and stabilizes after external feedback or (b) a reasonable post-posting window passes with no feedback. The trigger is gated on TODO-007 (public posting) and is *external* in nature, so the item cannot fire on its own and producing the 7 companion files prematurely risks rework. Demotion to P2 acknowledges that the file's own discipline is being honored: this is a deferred item awaiting an external trigger, not an item the next session must clear before starting SS-10.
**Trigger**: After (a) public posting (OSF + arXiv) lands AND (b) external-feedback window settles — either no v1.x revision arrives within Thomas's chosen window, or v1.x ships and stabilizes.
**Deliverable**: 7 companion files per `templates/paper_completion_checklist.md` Section A and `templates/documentation-suite.md`:
- `mechanism-SS-9.md` (A1) — step-by-step mechanism narrative with mathematical-correspondence table
- `glossary-SS-9.md` (A2) — paper-specific terms organized by category
- `phenomena-SS-9.md` (A3) — what the paper explains (PHEN-E empirical, PHEN-P predictions, PHEN-V consilience)
- `philosophy-SS-9.md` (A4) — epistemological framing
- `development-SS-9.md` (A5) — already exists as session-continuity file; may need final consolidation pass at v1.0+ trigger
- `reviews-SS-9.md` (A6) — all reviews + FAQ
- `keywords-SS-9.md` (A7) — keywords and registry cross-refs
**Estimated effort**: 1 dedicated session (~3-5 hours per checklist).
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-003 — Tier 4 reasoning recovery for chat window `a49b320e` (March 19 – April 6, 2026)

**Status**: PROGRAMME-LEVEL DEFERRED multi-session backlog; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Recovery of substantive Opus reasoning into per-paper `reasoning-[ID].md` files for already-shipped historical papers (16 papers: SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5) is hygiene work on the historical record, not a precondition for new paper work. SS-10's framing and execution do not depend on having recovered reasoning artifacts for unrelated earlier papers. This item should be revisited as a long-term backlog candidate; if it grows into a dedicated multi-session project, it should be promoted to `future_projects.md` rather than carried as a single TODO.
**Issue**: Foundational development of SR-1, EW-1 through EW-5, SS-1, QM-1 through QM-6, SM-1 through SM-5 happened in chat window `a49b320e`; substantive Opus reasoning has not been recovered into per-paper `reasoning-[ID].md` files.
**Deliverable**: Per-paper `reasoning-SR-1.md`, `reasoning-EW-1.md` through `reasoning-EW-5.md`, `reasoning-SS-1.md`, `reasoning-QM-1.md` through `reasoning-QM-6.md`, `reasoning-SM-1.md` through `reasoning-SM-5.md` (16 files). Source: chat window `a49b320e` transcript at `/mnt/transcripts/` if accessible, or `conversation_search` recovery per the `templates/operating_system.md` §6 protocol.
**Estimated effort**: Multi-session — could be ~16 separate small patches (one per paper) or a single large multi-patch chain.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-004 — `reasoning-SM-9.md` (patch 0027, pine-tree model)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003 — historical hygiene for an already-shipped paper, does not gate SS-10.
**Deliverable**: `reasoning-SM-9.md` per the four-tier discipline format used for SS-9.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-005 — `reasoning-SM-10.md` (patch 0028, FEM journey)

**Status**: PROGRAMME-LEVEL DEFERRED; not a forward blocker for SS-10
**Why P2 (Session 36 demotion)**: Same logic as TODO-003.
**Deliverable**: `reasoning-SM-10.md` per the four-tier discipline format.
**Estimated effort**: 1 patch.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2** 7 May 2026 Session 36 close patch 0288.

### TODO-006 — OPEN-WORKFLOW-1 legacy `.bib` file cleanup (programme-wide bibliography migration)

**Status**: PROGRAMME-WIDE MIGRATION — scope much larger than originally registered; not a forward blocker for SS-10
**Why P2 (Session 36 demotion + scope expansion)**: The Session 36 audit found **14 stray `.bib` files** across the repo, with most still **actively cited** by ~25 `.tex` files spanning every series. This is not a quick "audit and delete" patch — it's a programme-wide migration touching SR-1, SM-6 through SM-10, EW-1 through EW-5, QM-1 through QM-6, SS-1, SD-1 through SD-5, plus the orphan-or-active `series_strong/papers/cpp_strong_series.bib` and three `series_strong/cpp_strong_series*.bib` files at the series root. SS-7 and SS-9 use inline `\begin{thebibliography}` blocks (no .bib file at all). SS-8 and SM-3 use the canonical `bibliography/cpp_references.bib`. SS-10 can adopt the canonical pattern (like SS-8 did) regardless of what other papers use, so this migration does not forward-block SS-10. **Recommendation for next session**: consider promoting this to `future_projects.md` as a multi-session OPEN-WORKFLOW-1 project, since it's no longer "1 small patch" scope.
**Issue**: Bibliography consolidation policy established `bibliography/cpp_references.bib` as single source of truth; legacy per-series and per-paper `.bib` files are deprecated (per `templates/paper_production_workflow.md` Phase 2 note: "Do NOT create a new per-paper `[ID]_references.bib` file — those are deprecated"). Cleanup audit is registered as OPEN-WORKFLOW-1.
**Stray .bib inventory (Session 36 audit)**: `series_strong/cpp_strong_series.bib`, `series_strong/cpp_strong_series_papers.bib`, `series_strong/cpp_strong_series_root.bib`, `series_strong/papers/cpp_strong_series.bib`, `series_standard_model/papers/cpp_references.bib` (note: NOT canonical path), `series_standard_model/papers/SM-{6,7,8,9,10}_references.bib`, `series_electroweak/papers/cpp_ew_series.bib`, `series_quantum_mechanics/papers/cpp_qm_series.bib`, `series_foundations/series_superdeterminism/cpp_foundations_series.bib`, `series_relativity/papers/SR-1_references.bib`. Active `.tex` consumers identified per audit.
**Deliverable**: Programme-wide migration: (1) merge unique entries from each stray `.bib` into `bibliography/cpp_references.bib`; (2) update `\bibliography{...}` line in each consuming `.tex` to point to `../../../bibliography/cpp_references` (path depth varies by series structure); (3) delete strays; (4) recompile each affected paper to verify no broken citations.
**Estimated effort**: Multi-session if done thoroughly (likely 2-3 sessions); paper-by-paper migration with recompile verification per paper.
**Registered**: 7 May 2026 Session 33 close as P1; **demoted to P2 with scope expansion** 7 May 2026 Session 36 close patch 0288.

### TODO-007 — SS-9 public posting (OSF deposit + arXiv submission)

**Status**: PENDING Thomas's timing decision; OSF complication identified Session 36 (see below)
**Operational protocol**: `series_strong/papers/SS-9/letters/SS-9_post_ship_OSF_arXiv_submission_guide.md` (created Session 33 patch 0268).
**Session 36 update — OSF complication identified**: Thomas's existing Open-Ended Registration `10.17605/OSF.IO/JXE8D` (the "Conscious Point Physics Paper Series" master registration created Mar 31, 2026, listing SS-1, SM-1 through SM-5, SR-1) has been stuck in **"Pending Admin Contributor Approval"** state for 5+ weeks despite the documented 48-hour auto-approval window. Thomas is the only admin contributor listed. Multiple support tickets sent; one received an unhelpful response (about a different registration); subsequent tickets unanswered including a Claude-drafted escalation. The DOI is real and the priority date (Mar 31, 2026) is locked, but the registration is technically not finalized. **Decision Session 36**: Thomas will submit one more diagnostic-specific support ticket framing the issue precisely as "Pending Admin Contributor Approval state stuck >38 days, only one admin contributor, auto-approval timer never fired." Wait 5 business days for OSF response. **If OSF resolves** → add SS-9 as an Update to the existing JXE8D registration (the registration is Open-Ended, designed to be added to over time), and post to arXiv in parallel (categories nucl-th + math-ph). **If OSF still silent after 5 business days** → fallback to depositing SS-9 on **Zenodo** (CERN-run, gives DOI, no comparable workflow issues) plus arXiv, treating OSF as a later catch-up.
**Two original options remain open** (both consistent with rescoped sub-task (e)):
- **Option A**: post now to lock priority date and start external-feedback clock.
- **Option B**: wait until anthology chapter (Session 34) and TATWD integration (Session 35) are complete to present a fuller programme picture at posting time.
Both are now fully available since Sessions 34 and 35 are complete; only the OSF technical issue remains as a delay factor.
**Note**: TODO-001 (SS-9 Phase 7 Section A) trigger depends on this resolving — public posting is the precondition for the external-feedback window.
**Registered**: 7 May 2026 Session 33 close; **OSF complication and fallback plan added** 7 May 2026 Session 36 close patch 0288.

### TODO-008 — OPEN-WORKFLOW-DOCS-CATCHUP (programme-wide documentation-suite discipline-tightening per discipline-tightening-after-precedent principle)

**Status**: REGISTERED — two-part item: (A) flagship documentation-suite backlog catch-up for SF-4 v1.0 and SF-2 v1.0; (B) programme-wide gate-language codification of synchronous-documentation-suite requirement for v1.0 SHIP going forward
**Why P2 (not P1)**: This is hygiene/discipline-tightening work — it does not gate any specific next paper. The flagship papers themselves are already shipped; their documentation-suite backlog is a programme-record-completeness item. The gate-language codification is forward-looking discipline that will apply to future flagships from the next v1.0 SHIP onward. Neither sub-item blocks SS-10 or any other in-flight work.

**Precedent (Capotauro v1.0 SHIP arc)**: Capotauro v1.0 SHIPPED at Patch 0415 Session 122 with **the first complete documentation suite shipped synchronously with a CPP flagship v1.0 SHIP**. The Session 123 doc-suite catch-up arc (Patches 0416–0416L) produced ten documentation files: Section E four-tier discipline (handover ✓ 0416 + development ✓ 0416B + transcript ✓ 0416C + reasoning ✓ 0416D) + Section A six standalone companions (mechanism ✓ 0416E + glossary ✓ 0416F + phenomena ✓ 0416G + philosophy ✓ 0416H + reviews ✓ 0416I + keywords ✓ 0416J) + anthology chapter (✓ 0416K) + TATWD integration (✓ 0416L). This is the reference implementation for the synchronous-documentation-suite discipline. Per the **discipline-tightening-after-precedent principle** (recognized at Session 123 Patch 0416D as a programme-level convention; same pattern as Sessions 115–116 per-paper changelog file convention codification at Patch 0408 reference implementation → Patch 0409 programme-wide codification), the precedent makes credible the codification of synchronous-doc-suite requirement as a programme-wide v1.0 SHIP gate.

**Sub-item (A): Flagship documentation-suite backlog catch-up**

The two flagships that shipped v1.0 before Capotauro (SF-4 v1.0 at 14 May 2026; SF-2 v1.0 at 14 May 2026 jointly with its Companion paper) shipped without Section A standalone companions. Backlog inventory:

- **SF-4 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/neutrinos/documentation_suite/` has development-SF-4.md + handover-SF-4.md + reasoning-SF-4.md + transcript-SF-4.md (Section E four-tier discipline only)
  - Missing: mechanism-SF-4.md (A1) + glossary-SF-4.md (A2) + phenomena-SF-4.md (A3) + philosophy-SF-4.md (A4) + development-SF-4.md final consolidation pass (A5; current file is session-continuity, not the consolidated paper-development file) + reviews-SF-4.md (A6) + keywords-SF-4.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template
  - **Trigger**: After SF-4 v4.4 public posting (currently pending Thomas's timing decision per TODO-007-analog for SF-4) AND external-feedback window settles, per Two-Triggers discipline. Same trigger logic as TODO-001 for SS-9.

- **SF-2 v1.0 documentation-suite backlog: 0/7 standalone companions**
  - Existing: `flagship_papers/electroweak/documentation_suite/` has development-SF-2.md + handover-SF-2.md + reasoning-SF-2.md + transcript-SF-2.md (Section E four-tier discipline only); Companion paper documentation status to be audited
  - Missing: mechanism-SF-2.md (A1) + glossary-SF-2.md (A2) + phenomena-SF-2.md (A3) + philosophy-SF-2.md (A4) + development-SF-2.md final consolidation pass (A5) + reviews-SF-2.md (A6) + keywords-SF-2.md (A7)
  - Estimated effort: 1 dedicated session (~3-5 hours) following the Capotauro template; possibly 2 sessions if Companion paper warrants parallel suite
  - **Trigger**: Same Two-Triggers logic as SF-4 — after SF-2 v1.0 public posting + external-feedback window settles.

- **SS-9 v1.0 documentation-suite backlog**: Already tracked at TODO-001 (registered 7 May 2026 Session 33; demoted to P2 Session 36 Patch 0288). The SS-9 trigger logic is the canonical reference for the Two-Triggers discipline. TODO-008 does NOT re-register the SS-9 item; it cross-references TODO-001 as the SS-9 instance of the broader pattern.

**Sub-item (B): Programme-wide gate-language codification**

The Capotauro precedent makes credible a tightening of the v1.0 SHIP gate-language to require synchronous documentation-suite completion. The codification work is a separate downstream item, not bundled with the backlog catch-up:

- **`templates/operating_system.md` §4 Phase 7 (post-SHIP doc-suite work)** — modify gate-language to specify: "A flagship paper does not reach v1.0 SHIPPED status until its Section A 6 standalone companions + Section E 4 four-tier discipline files are complete in `flagship_papers/<paper>/documentation_suite/`. Synchronous completion is the default; the Two-Triggers discipline (`templates/paper_completion_checklist.md` lines 35–48) applies only as an explicit exception for cases where external-feedback gating is more important than synchronous completion (e.g., a paper that may revise substantially after first external review)."
- **`templates/paper_completion_checklist.md` Section A** — modify the Two-Triggers discipline language to clarify that synchronous completion is the new default (per Capotauro precedent), with the Two-Triggers as documented exception path rather than default workflow. The Two-Triggers default should remain available for papers like SS-9 where the v1.0 paper itself is the primary deliverable and the documentation suite can wait for external-feedback shape.
- **Cross-reference**: `book_project/chapters/capotauro_what_was_always_there.md` §"The Method Underneath" + `programme_orientation.md` Chapter 35.5 § Methodological observation as the master-document references for the precedent.
- Estimated effort: 1 patch (~30 minutes) — small editorial codification patches against the two template files. Should be done after Sub-item (A) is at least partially in hand (per discipline-tightening-after-precedent principle: the codification is credible because multiple instances of the discipline now exist).

**Estimated effort total**: 2-3 sessions for Sub-item (A) (SF-4 + SF-2 backlog completion, possibly serialized); 1 small patch for Sub-item (B) (codification).
**Registered**: 16 May 2026 Session 123 close Patch 0416M as the **final patch in the Capotauro doc-suite catch-up arc** (Patches 0416 + 0416A through 0416L preceding this patch). Forward queue: items fire on Two-Triggers external-feedback signal for each affected paper; codification patch can fire any time after Sub-item (A) is partially in hand.

---

### TODO-010 — Second-level decomposition of `frontier_sectors/SS.md` (contingent on SS-sector bootup overflow)

**Status**: CONTINGENT — fires only if loading `frontier_sectors/SS.md` (208 KB, ~700 lines) at session bootup overflows the context window. Not currently known to do so.
**Why P2**: Speculative future hygiene. The 25 May 2026 frontier decomposition reduced master `research_frontier.md` from 1852 to 280 lines, solving the bootup overflow. Sector files are loaded on demand, not at bootup, so SS.md's size is only a concern if a session needs to load the full SS sector. If that triggers overflow in future SS-focused sessions, sub-decomposition becomes necessary.
**Trigger**: First session that overflows on `frontier_sectors/SS.md` load.
**Deliverable**: Split `frontier_sectors/SS.md` into sub-topic files following the same pattern as the master decomposition (extraction script + thin index rewrite). Candidate sub-decomposition:
- `frontier_sectors/SS_cage_mechanics.md` — SS-1 through SS-6 (quark mass, generations, condensate, β1, string tension, glueball)
- `frontier_sectors/SS_nuclear_binding.md` — SS-7, SS-8, SS-10 through SS-21 (binding curves, nucleon moments, ZBW mechanisms, deuteron)
- `frontier_sectors/SS_magic_numbers.md` — SS-22 through SS-37 (alpha-cluster regime, OPEN-SS-35 magic-number gap programme, deltahedra-gap closures)
- `frontier_sectors/SS_propositions.md` — SS-specific PROPs/CONJs from SS-5, SS-6, SS-7
**Estimated effort**: 1 dedicated session (~2 hours). Same pattern as 25 May 2026 master decomposition.
**Registered**: 25 May 2026 (frontier decomposition close, flagged from SS.md size observation: 208 KB, dwarfs all other sectors).

### TODO-011 — Structural-heterogeneity normalization pass across all sector files

**Status**: hygiene improvement; not blocking next paper
**Why P2**: `research_frontier.md` accumulated heterogeneity over months of organic growth — some OPEN-XX entries are richly sub-structured with `### Status`, `### Mechanism Required`, `### Route History`, etc.; others are flat single-paragraph prose. This was preserved verbatim in the 25 May 2026 decomposition to keep the extraction deterministic and reviewable. Normalizing every entry to a uniform sub-header skeleton would make sector files easier to grep, easier for AI collaborators to parse uniformly, and easier for new sessions to bootup-into-problem.
**Deliverable**: Standardize every OPEN-XX entry across all 9 sector files in `frontier_sectors/` to use a uniform sub-header skeleton:
- `### Status` — one-line current state
- `### Mechanism Required` — what closure looks like
- `### Acceptance Criteria` — F1/F2/F3 falsifiers or equivalent
- `### Route History` — what has been tried; ruled-out routes preserved
- `### Cross-References` — related OPEN-XX entries, papers, conjectures, propositions

Empty sections marked `(none yet)` to keep the skeleton uniform across heavily-developed and stubbed entries alike.
**Estimated effort**: ~9 patches (one per sector), deliverable as a sequential arc. Could also be done piecemeal as sessions touch specific sectors for unrelated reasons (lazy normalization).
**Registered**: 25 May 2026 (frontier decomposition close, noted from sector-file spot-check when Thomas observed format heterogeneity in extracted files).

### TODO-013 — Annotate BRIDGE-1 falsifier B4 as resolved-as-documentation (DG-3, carried from Session 151)

**Status**: small hygiene note; not blocking; **do NOT edit the review-closed theorem solely for this** — carry until the next substantive BRIDGE-1 maintenance bump.
**Why P2**: `series_umbrella/series_substrate_chirality_arc/chirality_derivations/theo_chir_bridge_1.tex` (THEO-CHIR-BRIDGE-1) is multi-AI review-closed 3/3 at v1.1 (Patch 0665). Opening it solely to annotate one falsifier is disproportionate and risks re-triggering review; the correct discipline (Session 151 handover DG-3) is to fold the annotation into the *next* version bump that touches the theorem for a substantive reason.
**Issue**: Falsifier **B4** currently reads "the χ normalization is irreconcilable (φ⁻¹ vs φ⁻³)" (`theo_chir_bridge_1.tex` falsifier ledger). That worry was **resolved as a non-tension at Patches 0669 + 0670**: φ⁻³ is the unambiguous live magnitude (FI-C-9 = CHI-1 = Capotauro v1.0/v2.0); φ⁻¹ is both a registered dead-end (Findings C-1/C-2/C-3, Session 86) and the first-shell *distance* from which CHI-1 builds χ = (1−φ⁻¹)/(1+φ⁻¹) = φ⁻³. So B4 as written overstates a live risk.
**Deliverable**: at the next BRIDGE-1 maintenance bump, annotate B4 as "**resolved-as-documentation** (χ φ⁻¹-vs-φ⁻³ reconciled as a non-tension, Patches 0669/0670); **retained only as a forward hook on sub-claim (b)** — re-fires only if a future first-principles |χ| derivation returns φ⁻¹ or φ⁻² as the *magnitude*." No standalone edit, no version bump for this alone.
**Estimated effort**: trivial (one falsifier-line annotation, folded into a future bump).
**Registered**: 30 May 2026 Session 152 Patch 0674 (carried from the Session 151 handover Priority 2 / DG-3; reclassification first noted at Patch 0669).

---

### SR companion-paper set (c01–c22) audit & registry reconciliation
**Added:** 31 May 2026, Session 149, Patch 0672b. **Priority:** P2 (do NOT block the tetra-gravity DM arc — DM publication is the stated higher priority).

The `SR_companion_papers` set (c01–c22) was restored from Archive to `series_relativity/SR_companion_papers/` (origin commit f70bc05, 31 May 2026); it had been archived, probably by accident, and was not visible in the working repo. These are Sonnet-era papers that predate parts of the current OPEN-/THEO-/CONJ- registry and protocol system. Audit + reconcile when convenient:
- **Duplication** — check companion content against current SR-1 / SS / SD / EW / QM papers for overlap or supersession.
- **Stale open problems** — `frontier_sectors/SR.md` still lists OPEN-SR-4 (full field equations) and OPEN-SR-8 (equivalence principle) as OPEN with a "weak-field GR derived; full nonlinear not yet proved" best-lead note, but c05 derives Newtonian gravity (G = ℏc/m_P² exact), c07 derives weak-field GR + equivalence principle + factor-of-2 lensing, and c08 addresses strong-field GR. Reconcile SR.md ↔ companions; retire/downgrade OPEN-SR-8 and re-scope OPEN-SR-4 as warranted.
- **Registry retrofit** — register companion results into `theorem-registry.md` / frontier where they meet the bar (e.g. c05 G = ℏc/m_P², c07 weak-field Schwarzschild + lensing factor-of-2).
- **Spin-paper correction** — c20/c21/c22 may carry the pre-correction "2:1 frequency"; reconcile against THEO-SPIN-1 (v1.1) corrected this session (radius 2 / frequency 2√2).
- **DM-arc tie (added Patch 0702, 31 May 2026):** the tetra-gravity DM arc's Step-0 audit re-confirmed the SR.md staleness — `frontier_sectors/SR.md` (all entries dated 23 March, everything OPEN) does not reflect c05/c07/c08. This bullet (the "Stale open problems" item above) is the home for that reconciliation; no separate TODO was minted to avoid duplication. Step 0 of OPEN-COSMO-DM-1 only *cites* c05/c07 and does not block on this hygiene pass.
- **Effort:** multi-patch; sequence after the DM arc's Gate-1 (σ/m) and Gate-2 (bookkeeping) calculations are in hand.


### TODO-014 — c05 "G = ℏc/m_P², zero free parameters" framing: resolve the Planck-scale circularity before Step 0 leans on it
**Added:** 31 May 2026, Session 149, Patch 0702. **Priority:** P2 (does NOT block the DM arc — framing issue, not a physics blocker).

**Issue.** c05 (`c05_gravity_from_SSV_shell_broadcast.tex` §"The Gravitational SSV Quantum and Newton's G") boxes `G = ℏc/m_P²` and calls it "exact ... no free parameters," verifying numerically by plugging in CODATA `m_P = 2.176×10⁻⁸ kg`. As written this is circular: the Planck mass is *defined* by `m_P ≡ √(ℏc/G)`, so `G = ℏc/m_P²` is an algebraic identity, and the CODATA `m_P` used in the "verification" was itself computed from the measured `G`. It is a genuine zero-parameter *prediction of G* only if the Planck scale (`m_P` / `l_P` / `t_P`) is independently fixed by the 600-cell **without reference to G**.

**What c02 actually establishes (checked Patch 0700).** c02 (`c02_dipole_stiffness_C.tex`) derives a genuinely *dimensionless* geometric constant `α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594` (the Voronoi second-moment efficiency). But every dimensionful quantity is carried by `E_P`, `l_P` taken as given (`SSV_crit ≡ E_P/l_P³` asserted as the Planck energy density). So the lattice fixes dimensionless ratios; the absolute scale is **not** derived there.

**Dimensional-analysis reality (do not promise the impossible).** A dimensionful constant cannot be derived from pure geometry — at least one dimensionful input (the lattice spacing ≡ `l_P`) must set the scale. "Derive G from first principles" therefore cannot literally succeed; pursuing it as stated would be chasing a category error. The honest, defensible target is a **restatement + a verification**, not a derivation of a dimensionful number from numbers.

**Deliverable.**
1. **Verify the calibration is singular and shared** — confirm the whole CPP corpus fixes its absolute scale by exactly *one* dimensionful input (the lattice spacing / `l_P`), used consistently everywhere, with no second hidden scale-setting calibration. (If a second independent dimensionful calibration exists, the "zero free parameters" claims across the corpus need re-auditing, not just c05's.)
2. **Restate c05's claim precisely** — replace "G derived, zero free parameters" with "all *dimensionless* structure (incl. `α_geom`) is fixed by the 600-cell; the single dimensionful scale `l_P` is the one shared calibration; `G = ℏc/m_P²` then follows with **no additional** parameter." This is still a strong result; it is just not "G from nothing."
3. **Trace the upstream chain** — document where `l_P`/`E_P`/`t_P` enter (c02 and any earlier paper) and whether anything purports to fix them independently; if such a derivation is claimed, scrutinize it for a concealed dimensionful input.
4. **Step-0 wording lock** — until (1)–(3) are done, OPEN-COSMO-DM-1 Step 0 cites c05 as "**Newtonian force law recovered**" (the DM arc only needs the Newtonian *form* with a G matching observation, which c05 supplies regardless), NOT "G derived from scratch."

**Estimated effort:** 1–2 patches (an audit + a c05/c02 CHANGELOG framing bump); no new physics required for the restatement, though step (3) may surface a real open question worth its own registry entry.
**Registered:** 31 May 2026 Session 149 Patch 0702 (surfaced during the DM-arc Step-0 GR-foundation check).

### TODO-015 — c08 Open Problem 1 (full nonlinear strong-field Einstein equivalence): standing deep target, NOT blocking DM-2
**Added:** 8 June 2026, Session 156, Patch 0808. **Priority:** P2 (does NOT block the DM-2 / Sea-gravitation arc — see resolution below).

**The problem.** c08 (`c08_strong-field_GR.tex`, Open Problem 1) leaves open whether the full nonlinear feedback term 𝓕 in the CPP field equation reproduces the exact Einstein tensor `G_μν` in the **strong-field** regime — i.e. whether `box(Δ|SSV|) + 𝓕 = G_μν u^μ u^ν` for all spacetimes, or a counterexample exists. c08's weak-field reduction to linearised GR and the exact Schwarzschild solution are proved; the full nonlinear equivalence is the stated central unsolved problem of that paper. This is a genuinely deep target (effectively: derive GR's full nonlinear structure from the substrate).

**Why it is NOT on the DM-2 critical path (resolved, Patches 0805–0806).** The DM-2 Step-1 audit initially tied D2 (ground-state exclusion) to this problem. Step 1 (0805) showed the coupling is separable, and Step 2(a) (0806) closed it: gravitation is **gradient-controlled, not amplitude-controlled** — 𝓕 = [bounded amplitude factor] × [gradient² factor], so the uniform Sea's O(1) absolute SSV sources ~0 (small gradient) and never exercises the strong-**amplitude** nonlinearity OP1 is about. The only large-gradient sources are sub-Planck localized excesses, weak-field by `(m/m_P)² ~ 10⁻³⁹`. So DM-2 proceeds in full **without** OP1; it does not wait on this item. See `series_phenomena/cosmology/sea_gravitation/dm2_step2a_zbw_bound.md`.

**Status / scheduling.** Standing deep target ("in its time"). Belongs to the SR companion-paper set (c01–c22) and is adjacent to the c08 Kerr and discrete-to-continuum open problems. Candidate for promotion to `future_projects.md` if/when pursued as its own arc. Not to be confused with DM-2's net-broadcast lemma (a separate, local, weak-field question).

**Registered:** 8 June 2026 Session 156 Patch 0808 (surfaced and then de-risked during the DM-2 Step-0/1/2a audit).


### TODO-016 — DP-Sea appendix: the DP binding-energy formula is numerically inconsistent with its stated r_min by ~18 orders of magnitude
**Added:** 10 June 2026, Session 156, Patch 0834. **Priority:** P2 (does NOT block DM-2; the *ratio* the DM arc uses is unaffected).

**The problem.** In `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` (Appendix, "DP Binding Energy Calculation"), the formula `E_bind = αℏc/r_min` is quoted with `r_min = φ·l_p ≈ 2.61×10⁻³⁵ m` (the golden-ratio-scaled **Planck** length) and is said to yield `E_eDP = αℏc/(φl_p) ≈ 88 MeV`, `E_qDP = 3·E_eDP ≈ 264 MeV`. But `αℏc/(2.61×10⁻³⁵ m) ≈ 5.5×10¹⁹ MeV`, not 88 MeV — the stated r_min and the quoted energies are inconsistent by ~6×10¹⁷. The quoted 88 MeV instead requires `r_min ≈ 0.016 fm = 1.6×10⁻¹⁷ m`, eighteen orders of magnitude larger than the Planck length. So as written the **absolute** eDP/qDP energy scale does not follow from the Planck length; it is calibrated to the constituent/QCD scale and the appendix mislabels its own r_min.

**What is and isn't affected.** The **ratio** `E_qDP/E_eDP = 3` (color factor) is clean and is the only thing the DM-2 Era-2 arc leans on (it gives m_qDP ≈ 3×88 = 264 MeV, used in patches 0830–0833). So this does **not** block DM-2. But the eDP = 88 MeV scale propagates into the whole DP spectrum (hDP = √(E_eDP·E_qDP) ≈ 152 MeV, the cage binding energies, the boson-mass averaging), so the inconsistency should be reconciled at the source.

**The fix (a physics decision, hence Thomas's, not a unilateral flagship edit).** Decide what actually sets r_min ≈ 0.016 fm: (a) is it a genuine CPP length (e.g. the CP grid/lattice spacing, or a derived sub-quantum scale) that should replace "φ·l_p" in the formula and text; or (b) is the 88 MeV scale calibrated to the constituent/QCD scale, in which case the appendix should say so rather than presenting it as Planck-derived? Either way the appendix line and the "2.61×10⁻³⁵ m" value need correcting so the paper is internally consistent.

**Surfaced:** 10 June 2026 Session 156 Patch 0833 (DM-2 Era-2 required-inputs derivation pass, deriving m_qDP). Flagged to Thomas; left for his edit/publish workflow on the flagship.

**Update (Patch 0838 — decision recorded):** Thomas chose **Option C** (Planck → DP/QCD scale via derived suppression). Decisive finding: **C is already SS-1 open problem `op:lambda_psr`** ("Λ_QCD from PSR saturation": derive Λ_QCD ≈ 0.218 GeV from l_P + sea_strength via PSR_eff → l_P/2) plus `op:sigma` (string tension from sea_strength) — SS-1 honestly marks this scale *calibrated* with the Planck derivation *open*, while the DP-Sea appendix wrongly asserts it *done*. Resolution is two-track (see handover): **(1)** correct the appendix now to match SS-1's honest stance + cite `op:lambda_psr` (energies 88/264/152 + ratios retained; drop the false `αℏc/(φl_p)` derivation and the 2.61×10⁻³⁵ m identification); **(2)** pursue C proper = solving SS-1 `op:lambda_psr` (promote to `future_projects.md`), which on success upgrades both flagships from calibrated to derived. Handover updated. **Status: Track 1 awaits a draft+sign-off pass; Track 2 to be promoted to future_projects.md. No flagship edit made yet.**


### TODO-017 — Corpus-wide harmonization review (after the SU(3)/beta-decay/chirality exploratory arc settles)

When the Session-16x exploratory arc (SU(3) mechanism → beta decay → chirality) reaches a sense of completion, run a cross-corpus harmonization sweep: check all papers for internal consistency and number-agreement across the EW, SS, SF sectors and the substrate-chirality arc. Prompted by finding TODO-018 (a genuine error sitting in two shipped EW papers) — if one number-error survived into print, others may have. Scope: an internal-consistency + cross-reference pass, not new derivation. **Registered 18 June 2026.**

### TODO-018 — EW-2 / EW-5 chirality-fraction formula error (genuine bug in two shipped papers) — recommend elevating

Both `series_electroweak/papers/EW-2_w_boson_from_cpp.tex` and `series_electroweak/papers/EW-5_electroweak_unification.tex` carry the line `P_L^eff = 1 − sin²(60°) = 0.25 ⟹ 75% left-handed`, claimed as "matching the V−A structure of weak charged currents." Two faults: **(a) internally inconsistent** — `1 − sin²(60°) = 0.25`, i.e. 25%, but the line concludes 75%; it computes one value and prints another. **(b) physically short** — the weak charged current is ~maximally parity-violating (~100% left-handed; Wu 1957 + Goldhaber 1958), not a 25/75 partial preference, so "75% matching V−A" is wrong regardless of which number is meant. Action: decide the correct intended quantity, fix the formula in both papers, and **check propagation to SF-2** (the electroweak flagship likely inherits it). This is a real error in shipped work, not a hygiene gap — recommend P1. **Registered 18 June 2026.**

### TODO-019 — Mechanism note: the billiard-ball realization of the SU(3) hop (closes `op:strong_primitive` on the mechanism side, if it holds)

Memorialize the Session-16x exploratory result. SS-1b derives the SU(3) *algebra* from three tetrahedral color vertices and explicitly leaves `op:strong_primitive` open — *why* the strong force is tetrahedral hopping. The week's work built the candidate *mechanism* underneath the algebra: color = which base vertex a quark occupies; the eight gluons = the six edge hops + two diagonals among three vertices; each hop physically *carried* by a ZBW / SSV-gradient transition (the trembling is the muscle that performs the hop). Status to register honestly: **picture, not yet derivation** — the mechanism is rich enough to be a candidate carrier but was not shown to *force* the algebra from substrate geometry alone. Write as a standalone mechanism note, separate from the algebra papers (SS-1b / SF-5), and register the open residual. **Registered 18 June 2026.**

### TODO-020 — Chirality visualization writeup → Chirality window (900-series patches)

Write up the new chirality visualization and hand it to the 900-series Chirality window to test whether it helps close the substrate-chirality arc. The picture: a moving charge polarizes the surrounding DP Sea; each dipole's poles swing (opposite pole drawn toward the passing charge, like pole pushed away), turning the dipole about its center; the *sense* of that rotation relative to the charge's line of motion is the right-hand rule. So the magnetic field is the *name for the DP-Sea's rotational response to a moving charge*, not a primitive field — and handedness is *generated* by charge-through-dipoles, with sign set by the charge's polarity. Consequence to flag for the 900 window: this removes the need for a primordial/inflationary chirality imprint — the world's handedness is manufactured fresh by every moving charge. Send as a story/note (Thomas's preferred form) and see whether it advances the substrate-chirality determination. **DONE (18 Jun 2026):** the writeup is committed at `founders_voice/phenomenon_magnetism_and_chirality.md` (edited from TLA's v2; Goldhaber + type-B fixes). It carries both a "For the chirality window (900-series)" section and a "For SF-6 (electromagnetism flagship)" section. **SF-6 and the 900 window should both read it there.** A paste-ready handoff instruction for the chirality window was generated 18 Jun 2026. **Registered 18 June 2026.**

### TODO-021 — Harmonise SS-1b's per-quark-cage exposition with the cageless-quark / bonding-framework realisation

Surfaced while shipping SS-1f v1.0. SS-1b's exposition states "each quark sits inside a tetrahedral cage (four vertices: apex V4 for the qCP, base {V1,V2,V3} for color)" — a **per-quark cage** picture. TLA's clarification (and SS-1f's resolved frame) is that the hTetra is the baryon-level **bonding framework**, that **up and down quarks are cageless** (qCP core + radial ZBW eCP + cloud), and that only the **strange quark carries its own hTetra cage**. SS-1b's *algebra* is frame-agnostic (three labelled colour vertices + hops) and is unaffected; only its *physical-picture wording* is in tension. Two sub-tasks: (i) reconcile SS-1b's expository cage language with the cageless-quark realisation (edit SS-1b's prose, not its theorem); (ii) work out the detailed correspondence between SS-1b's (apex-qCP + three-colour-base) cage and the baryon hTetra's (three-quark + open-eCP-vertex) geometry. Folds into the TODO-017 corpus-harmonisation sweep but is specific and known. **Registered 18 June 2026.**

### TODO-022 — Phenomenon-story programme: a `founders_voice/phenomenon_*.md` behind every paper and glossary item

TLA's standing intent, now structurally established. `founders_voice/` hosts the fully-articulated, expanded, examined version of each paper's Plain Language Summary — the founder's mechanical billiard-ball story behind the mathematics ("this IS my story; the mathematics is what makes it credible"). Convention documented in `founders_voice/founders_voice-README.md` (six-part shape; honest-status discipline; newer conjectures flagged). Rollout: write one phenomenon story per paper (seeded from its PLS) and per major glossary item, on a rolling basis. Started 18 Jun 2026 with `phenomenon_magnetism_and_chirality.md` and `phenomenon_su3_colour_and_quark_switching.md`. Each story must name, in Honest-status, the proven mathematics that grounds it and the derivation still owed. **Registered 18 June 2026.**

### TODO-023 — Sitewide README normalization to the `{scope}-README.md` convention

The OS convention (`operating_system.md` §"README files — `{scope}-README.md` convention") mandates `{scope}-README.md` (scope prefix, hyphen, uppercase README) and notes a "retroactive normalization" cleanup is owed. Audit (18 Jun 2026): **83 non-compliant** README files — 70 plain `README.md`, 2 `{scope}_README.md` (underscore), 11 `README-{scope}.md` (leading-README) — plus 7 already compliant. `founders_voice/README.md` was fixed in passing (→ `founders_voice-README.md`). **The full batch is deferred to a dedicated, low-collision cleanup patch**, NOT folded into window work: it renames files across folders owned by every active window (series_relativity, flagship_papers/\*, series_standard_model, etc.), so it should run when windows are quiesced, as a single `git mv` sweep with a reference-update grep pass (links to `README.md` → `{scope}-README.md`). Content-neutral; the OS marks it non-forcing. Generate the batch script + ref-sweep on request. **Registered 18 June 2026.**

### TODO-024 — SS-1f v1.0 remaining Phase-7B integration items (anti-silent-dropout register)

SS-1f v1.0 production protocol initiated 18 Jun 2026 (patch 1534): the precedent-consistent core is DONE — series_strong sub-family table row (D3, the canonical home where SS-1a–1e live) + bibliography entry (C11, DOI pending Isak's OSF post). The following Phase-7B items are **deferred, not dropped** (per `paper_completion_checklist.md` "Phase 7B silent dropout" anti-pattern), pending a decision call on each because the SS-1x companion-note precedent is that SS-1a–1e are NOT individually carried in these registries:
- **C3 theorem-registry.md** — register SS-1f's Proposition 6.1 (the torus result) as a PROP-SS-* entry? Sub-family precedent = no individual registration (1b–1e absent); registering requires careful SS-header + Summary-Statistics count bumps. **Needs TLA call.**
- **C5 frontier_sectors/SS.md** — op:strong_primitive has no standalone entry in SS.md (the file is dominated by the SS-9 alpha-cluster arc); placing the "frame resolved / forcing open" status needs a deliberate new entry. **Deferred.**
- **D2 INDEX.md** — add SS-1f's files (.tex + reasoning + review artifacts). Low-risk navigation; **deferred.**
- **C10 programme_orientation.md / paper_catalog.md top-level / D1 README.md** — SS-1f is a sub-family mechanism note, not a top-level paper; 1a–1e set the precedent of light/no top-level presence. **Likely N/A; confirm.**
OSF deposit: Isak notified (18 Jun 2026); update C11 `doi` field once the DOI returns. **Registered 18 June 2026.**

### TODO-024 — SS-1f v1.0 remaining Phase-7B integration items — **DONE (18 Jun 2026, patch 1535)**

SS-1f v1.0 production protocol completed. Core (combined patch 1533+1534): series_strong sub-family table row (D3) + bibliography entry (C11, DOI pending Isak's OSF post). Remaining Phase-7B items now also done (patch 1535): **C3** — Proposition 6.1 registered as **PROP-SS-12** in theorem-registry (SS header 1→2 Propositions; no theorem-count / Summary-Statistics / ratio change, since propositions are tracked separately from the 81-theorem total); **C5** — **OPEN-SS-38** added to frontier_sectors/SS.md (the op:strong_primitive forcing problem; frame resolved by SS-1f, forcing open; SS header 19→20 problems); **D2** — SS-1f .tex added to INDEX.md. C10/D1/paper_catalog top-level confirmed N/A (sub-family companion note, per the SS-1a–1e precedent). Outstanding: only the OSF DOI (Isak) → update the C11 `doi` field on return. **Completed 18 June 2026.**

### TODO-025 — `frontier_sectors/CONJ.md` OPEN-COSMO-DM-2 / DM-2 R2 wording is stale (pre-2025 R2 arc) — **CLEARED 22 Jun 2026, Patch 2046**

**Status**: CLEARED (Patch 2046) — DM/cosmo lane was idle, so the two pointer brackets were added directly:
one to the OPEN-COSMO-DM-2 entry and one to CONJ-COSMO-1, both pointing R2's current state at
`mu_eps_closure/R2-STATUS.md` (conditional-PASS at field-content level; unconditional gated on OPEN-SR-9).
The stale "single-oscillator / Patch 2002" lines are left in place (historical record) with the pointer
overriding. *(Original deferral note retained below for audit.)* **Why it had been deferred (Patch 2041)**:
CONJ.md is the hottest cross-lane Tier-A file; the gap was cosmetic/non-verdict, so it waited for a quiet lane.
**What's stale**: the OPEN-COSMO-DM-2 entry (line ~251) and the CONJ-COSMO-1 entry (line ~314) describe R2's
status from before the 2025–2031 μ↔ε arc — e.g. "R2 PASS-conditional on the single-oscillator structure —
Patch 2002." The current state (R2-STATUS.md → Update 2041) is: **R2 conditional-PASS, both conditions met
within the audited LSP field content — (i) VTD-1 cleared at SR-1 strength (2037/2038 + panel P1-SOUND ×4);
(ii) f(C,Σ) closed at the field-content level (2028 scalar channel / 2029 ~11-order locality / 2030-2031
no-rank-2, ChatGPT CONFIRM) + A3′ OB-3 static-null theorem — with the from-substrate optical computation owed
to OPEN-SR-9.**
**The fix (small)**: a single Patch-NNNN bracket pointer appended to the OPEN-COSMO-DM-2 status line (and one
to CONJ-COSMO-1) reading "R2 current state: see R2-STATUS.md Update-2041 — conditional-PASS at field-content
level, unconditional gated on OPEN-SR-9." Do as its own minimal, refreshed edit (CONV-002) when the DM/cosmo
lane is otherwise idle. Precedent: CONJ.md line 233 already records the "R2 file stale framing owed an update
in the DM lane; not edited from another window — pointer only."

## Cleared items (history)

*Items move here with date and patch number when completed. Cleared items are not deleted — they form an audit trail of what was done and when.*

### TODO-009 — Lowercase `SOURCE=` in frontier decomposition scripts — CLEARED 1 June 2026 Session 153 Patch 0728

**Cleared**: 1 June 2026 Session 153 Patch 0728. Lowercased all `Research_Frontier` → `research_frontier` occurrences in `scripts/rewrite_research_frontier.sh` (SOURCE=, BACKUP=, and the printed `git add/diff/Open` instructions) and `scripts/decompose_research_frontier.sh` (SOURCE= + descriptive comments/echoes), giving full cross-platform correctness rather than just the two literal SOURCE= lines. Post-edit grep confirms 0 remaining capitalized refs in either script. Surfaced when Thomas asked whether a rename explained the stale `research_frontier.md` dashboard (Session 153, Patch 0727 Step E); investigation confirmed git tracks one lowercase file with no case-collision, the scripts worked on Windows because the filesystem is case-insensitive (so the rename was NOT the staleness cause — that was the 25-May decomposition shifting updates to sector files + skipped Step-E passes), but the latent portability bug was real and is now closed. **Scope note**: descriptive references to `Research_Frontier.md` elsewhere (frontier_sectors/*.md breadcrumbs, archive scripts) are harmless historical mentions, not functional, and left unchanged per TODO-009's two-script scope.

### TODO-012 — PCD acronym terminology drift cleanup — CLEARED 29 May 2026 Session 148 Patch 0631

**Cleared**: 29 May 2026 Session 148 Patch 0631 via systematic find-and-replace across 15 active files restoring the canonical "Perceive-Compute-Displace" expansion of the PCD acronym. Total occurrences corrected: 46 across 15 files; 0 drift-pattern remaining (verified by post-replace grep audit covering hyphenated form, lowercase form, en-dash form, UTF-8 arrow form, LaTeX `$\to$` arrow form, and "Polarize/Capture/Depolarize phase" PCD-phase-label patterns).

**Resolution narrative**: The Session-146 drift introduced "Polarize-Capture-Depolarize" at commit `311bc1e` in `master_glossary.md` PCD entry without rationalization; the drift propagated to ~15 active files via subsequent work that referenced the master glossary. Patch 0631 applied 5 precise sed patterns: (1) `Polarize-Capture-Depolarize` → `Perceive-Compute-Displace`; (2) lowercase variant; (3) UTF-8 arrow form `Polarize → Capture → Depolarize`; (4) LaTeX-arrow form `Polarize $\to$ Capture $\to$ Depolarize`; (5) en-dash form `Polarize–Capture–Depolarize`. Plus PCD-phase-label substitutions: `Polarize phase` → `Perceive phase`; `Capture phase` → `Compute phase`; `Depolarize phase` → `Displace phase`. Master glossary PCD entry enhanced with descriptive prose explaining the agentic cycle and its distinction from ZBW. Two prose descriptions aligned with canonical Perceive/Compute/Displace meanings (sf-2_companion glossary entry; dynamical_substrate_law §7.3 phase description). Physical-effect verbs ("polarizes the host's internal state", "depolarization") retained where they describe what happens during the cycle, not its name. Historical handover/session_log records preserved unchanged per anti-erasure discipline. CHANGELOG entries added to four SHIPPED papers (capotauro.tex, sf-2_electroweak.tex, sf-2_companion.tex, dynamical_substrate_law.tex) noting the post-SHIP terminology correction with no substantive content change.

**Files touched**: `master_glossary.md` (2 occurrences + entry enhancement); `frontier_sectors/SS.md` (1); `book_project/chapters/capotauro_what_was_always_there.md` (1); `flagship_papers/electroweak/sf-2_companion.tex` (2 + CHANGELOG); `flagship_papers/electroweak/sf-2_electroweak.tex` (2 + CHANGELOG); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/dynamical_substrate_law.tex` (7 + external changelog entry); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` (deep cleanup, 11+ occurrences including phase labels in §11 cycle structure detail); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/F1_layer3_b1q4_algebraic_derivation.md` (1, en-dash form); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/keywords-dynamical-substrate-law.md` (2); `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/documentation_suite/glossary-dynamical-substrate-law.md` (2); `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` (3 + external changelog entry); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/glossary-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/reasoning-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/capotauro/documentation_suite/philosophy-capotauro.md` (1); `series_umbrella/series_substrate_chirality_arc/chirality_continuum/sketches/F2_F3_viability_decision_gate_2026-05-21.md` (2).

**Historical records preserved unchanged** (anti-erasure discipline): `handovers/2026-05-20_session_137_close_manifestation_iv_next_window_seed.md`; `session_logs/2026-05-24_session_142_extracted_from_frontier.md`; "Earlier last-updated" entries throughout `research_frontier.md` history. Future readers encountering legacy "Polarize-Capture-Depolarize" terminology in archived/historical records can refer to the canonical master_glossary PCD entry or this TODO-012 cleared note for context.

**Forward**: Patch 0632 ships the THEO-CHIR-AUDIT-1 audit artifact under Pattern A sequencing (terminology baseline cleaned first; audit ships from clean baseline). Per Patch 0630 sketch document §5.2, the audit's §3.4 dynamics pass uses the canonical "Perceive, Compute, Displace" expansion throughout.

**Original registration**: 28 May 2026 Session 148 Patch 0630 (THEO-CHIR-AUDIT-1 scope sketch precondition gap §5.2).

### TODO-002 — SS-8 and SS-9 PDF compile (posting prerequisite) — CLEARED 7 May 2026 Session 36

**Cleared**: 7 May 2026 Session 36 via patches 0286 (SS-8.tex `\Kthree` macro `\ensuremath` fix) + 0287 (SS-8.tex `\usepackage{xcolor}` import for `yellow!10` blend) + direct commit `55c5986` (PDFs added to repo: SS-8 31 pages 507596 bytes, SS-9 32 pages 638209 bytes; both visually verified clean before commit; SS-9 compile triggered MiKTeX auto-install of `float.sty` per Phase C MiKTeX setting change).
**Resolution narrative**: First Thomas attempt (without patches 0285+0286+0287) compiled with errors and produced damaged PDFs (SS-8 abstract garbled with run-together italicized text from `\Kthree`-mode-quantum text, mdframed alert box on pages 15-16 rendering as solid black from undefined `yellow!10`). Damaged PDFs were committed as `6e86818` then reverted as `ccb6041` after diagnosis. Patches 0286 (`\Kthree` `\ensuremath` wrapper) and 0287 (`xcolor` package import) were then applied; MiKTeX auto-install set to "Yes"; aux files cleaned; recompile produced clean PDFs verified visually (K₃ subscript renders cleanly, alert box light-yellow as designed). Commit `55c5986` pushed both PDFs to origin successfully.
**Original registration**: 7 May 2026 Session 33 close patch 0274; scope corrected Session 36 patch 0285 to include SS-9.

---

## Maintenance

This file is maintained per session: any session that completes a TODO item moves it to "Cleared items (history)" with the completion date and patch number. Any session that identifies a new deferred item adds it here under the appropriate priority. Sessions that touch only this file (no other substantive work) follow the standard programme practice of session log + research_frontier.md last-updated entry — the documentation suite for a paper is updated only if the cleared item was paper-specific.

If this file's P1 section grows large (more than ~10 items), reconsider whether some items should be promoted to `future_projects.md` as registered multi-session projects rather than carried as to-dos.

If a P1 item turns out not to actually block the next paper on reflection, demote it to P2 with a note explaining why. The discipline is "P1 must be empty before SS-10," not "every deferred item is P1."

- **2026-07-15 (Patch 2502):** OPEN-SR-EPSILON RESOLVED-α (founder-ruled; W2 strength, caveats inherited); OPEN-SR-SF6-RECON-1 RESOLVED; geometric ε-route dead (round-2 unanimous). SR-1 rewrite opened, warm keyword SR1-WARM-2502. Panel next sees SR-1 when the rewrite is a shippable win.

---

### TODO-4000-EW — EW lane opened (block 4000–4099); its queue (registered Patch 4000, EW lane, under PD-006)

**Why this entry exists:** the EW lane is opened on the founder's 14 Sep ruling with two named consumers
already waiting on it. Both were previously carried only in a paper ledger, a corrigendum and a handover —
records, not a queue — which is the TODO-0937-CHIR shape. Filed here at the moment the lane opens.

- **`OPEN-EW-7` — W mass-breakdown species dependence. CLEARED at Patch 4002** (EW lane). Resolved to
  neither pre-registered branch: the row is a fixed-fraction partition of the calibrated total, so it is
  species-blind *and* count-blind; but the relabel crosses the `E_inter` cage switch, moving two cells
  (0 → 8038, 22774 → 14736) with the 80380 MeV total unchanged. Edit (g) applied in print; **SM-2 free to
  recompile.** Original entry below, for the record. ~~W mass-breakdown species
  dependence.~~ Does SM-2's W mass breakdown depend on the *species* of the W's 12 CPs, or only on their
  count? **Lane: EW.** Consumer: `SM-2_composition_corrigendum.md` edit (g), the only place a published
  SM-2 number can still move. Resolution (i) species-blind ⇒ edit (g) is a pure relabel; (ii) species-
  sensitive ⇒ the 80380 MeV total needs re-derivation.
- **`OPEN-SM-4` sub-claims (a) and (b) — the Capotauro mechanism. RESTATED at Patch 4003 after a D-2
  premise audit; the work below is NOT what the 16 May entry said it was.** (a)/(b) **are** `B-iii` of the
  CHIR↔EW bridge, twice reduced: capacity ⟺ sign(μ²) (0668), then sign(μ²) = sign(m²) (1100). `derive
  χ = φ⁻³` is already discharged (Capotauro v2.0 / CHI-1). Two residuals, both **idle since 8 June 2026**:
  - **(H1) — is the DSL measure reflection-positive? WORKED AT 4022, AND THE ANSWER IS NEITHER YES NOR NO:
    IT IS n̂-CONDITIONAL.** For reflections that **fix n̂**, π is Θ-invariant to 1e-17, the Gram matrix is
    symmetric to 1e-15 and PSD at δ = 0, 0.10, 0.35 — **RP holds**. For reflections that **flip or tilt n̂**,
    π is not Θ-invariant, the Gram matrix is **not even symmetric** (asym 1.2–4.9) and carries a strongly
    negative eigenvalue (−0.497 at δ = 0.10, −4.79 at δ = 0.35) — **RP FAILS, at O(δ)**.
  - **The asymmetry matters: the FAILURE is a proof, the SUCCESS is not.** One negative eigenvalue on any
    test class refutes RP, so the n̂-flipping case is settled by witness.
  - **~~EXTENSION OWED~~ — DISCHARGED AT 4055 FOR THE WHOLE PRODUCT HIERARCHY.** For multinomial(K, p)
    with all indices distinct, E[∏n] = K(K−1)…(K−2m+1)·∏p **exactly** — and since Θ maps the + side to
    the − side, **no coincidence term ever enters**. So the Gram matrix is **exactly G = K^(2m)·u⊗v,
    RANK ONE at every m**, symmetric iff π is Θ-invariant. **Measured at m = 2 and m = 3: n̂-fixing gives
    symmetric, PSD (asym ~1e-13, min eig ~−5e-13) at δ = 0, 0.10, 0.35; n̂-flipping gives min eig −8.21,
    −61.3, −5.63, −29.7.** **Identical verdict to single sites, and the structure is m-INDEPENDENT —
    there is no m at which a product observable could answer differently.** **4022's "necessary only"
    becomes "necessary AND sufficient within all product observables".**
  - **STILL NOT COVERED, and it is a real class: NON-PRODUCT observables** — a repeated index (n_a²) or
    any function of a sum. Those bring in the multinomial's **coincidence terms** (the +K·p_a that 4022's
    single-site Gram already carried) and the clean rank-one form breaks. **That is where a counterexample
    to RP would have to live if one exists. Lane: EW.**
  - **AND THE CHIRALITY ARGUMENT NEEDS EXACTLY THE SECTOR WHERE RP HOLDS.** `R = diag(1,1,1,−1)` with
    n̂ = e₁ is the map 4011, 4012, 4015 and 4020 all used, and 0973 puts sign(δ) as **P-even** — the P-face
    lives in the n̂-preserving sector.
  - **~~NOT MINE TO DECIDE~~ — TAKEN TO THE END AT 4023 under PD-008. VW-1's CONCLUSION SURVIVES
    RESTRICTED RP, for the P-sector.** A transfer matrix along direction *d* is built from reflection in a
    hyperplane ⊥ *d*, which **flips** *d* — so the TM exists **transverse** to n̂ (RP holds) and **not
    along** it (RP fails). And the ℤ₂ VW-1 forbids breaking is a **parity**, implemented by the
    n̂-**fixing** Θ = diag(1,1,1,−1): verified **η(ΘX) = −η(X) exactly, 6/6 seeds at ε = 0.02/0.05/0.10**.
    Operational RP confirmed by the Schwarz bound: **0/4000 violations** n̂-fixing at δ = 0.10 and 0.35;
    **2039/4000 and 2379/4000** n̂-flipping. **The reflections where RP fails generate the T-face, not the
    P-face — so the failure is OUTSIDE VW-1's scope, not inside it.**
  - **THE ONE STEP NOT CLOSED, named precisely:** VW-1's chain needs the **infinite-volume** limit. The TM
    transverse to n̂ controls **transverse** clustering; **clustering ALONG n̂ is not controlled by this
    argument.** On the **finite** substrate ⟨η⟩ = 0 exactly and no limit is needed — VW-1 holds outright.
    On the **extended** lattice (founder, 4009) the along-n̂ step is open. **Lane: EW / CHIR.**
  - **I RAN BOTH ATTACKS MYSELF AT 4024, per PD-008. ONE LANDS.**
    - **(b) P/T separability — DOES NOT LAND.** Θ = diag(1,1,1,−1) **commutes with the NESS generator
      exactly**: |ΘQΘ⁻¹ − Q| = 1.8e-15, and it is **not** time reversal (|ΘQΘ⁻¹ − Qᵀ| = 0.2 at δ = 0.10,
      0.7 at δ = 0.35, growing with δ). A pure P operation on the **dynamics**, not merely on the measure.
      0973's split holds; 4023 Step 2 stands.
    - **(a) generating set — LANDS. 4023's "outside VW-1's scope" is WITHDRAWN.** The n̂-fixing
      reflections generate a group of **8 elements, none of which moves n̂** (displacement 0.000). An
      OS/chessboard estimate is built by tiling with reflections, so the ones where RP holds generate
      **only transverse motion** and have **no traction along n̂ at all**. No-SSB is a statement about the
      whole system: a direction the argument cannot reach is a gap **inside** the scope, not a region
      outside it. **That was the convenient reading and it was wrong.**
  - **NET: the result is STRONGER in one place and WEAKER in the other.**
    - **Finite substrate — stronger.** Θ commutes with Q, so π is exactly Θ-invariant and **E[⟨η⟩] = 0 by
      symmetry alone, with NO RP anywhere.** 4023 presented this as RP-dependent; it is not.
      *(An ensemble statement: single realisations span ±0.18 and are not zero — 4020's finding, exactly.
      A draft of this check asserted per-realisation vanishing and FAILED; corrected.)*
    - **Extended lattice — weaker.** VW-1 is **genuinely weakened**, not merely incomplete: RP-based
      control exists transversally and the reflection group **cannot reach along n̂**.
  - **THE GAP ATTACKED BY DIRECT MEASUREMENT AT 4025 (PD-008): BOUNDED, NOT CLOSED.** ⟨ηη⟩_c measured on
    an extended 4D patch (4321 points, 960 usable interior, 260 realisations) sits at **0.13–0.49% of the
    on-site variance and within ~2 sem of zero, along n̂, out to 3 edge lengths**. Transverse, for
    contrast: 0.02–0.06%. **Evidence against long-range order along the drive — not proof. VW-1's
    CONCLUSION survives; VW-1's ARGUMENT still cannot reach there.**
  - **THE UNCOMFORTABLE COINCIDENCE 4025 FLAGGED IS DISCHARGED AT 4026, BY BUILDING THE FIX I NAMED.**
    Anisotropic patch elongated along n̂ (R∥ = 8.0, R⊥ = 1.3): **3,006 along-n̂ pairs against 1,518, and
    reach 12.7 edge lengths against ~3**. **And the better measurement found STRUCTURE, not a flat null:**
    a real short-range **anticorrelation** at ≈1 edge length, **−0.0123 ± 0.0036 (3.4 sem)**, which **dies
    by 1.8** — every band from 1.0 out to 9 is within 2.5 sem of zero and under 0.3% of on-site. **⇒ ξ ≲ 1
    edge length: FINITE correlation length, NO long-range order.** 4025's specific worry — that ξ ≥ 5
    would not show — is discharged: this reaches past 6 and sees nothing.
  - **RETRACTED AT 4027: 4026's "real short-range anticorrelation, 3.4 sem" IS NOT REAL.** At 10× the
    realisations the band value **drops 7× (−0.01234 → −0.00171)** and the significance collapses to
    **1.3 sem**. A real correlation does not shrink with more sampling; a fluctuation does. **With it,
    4026's claim that 4025's null was "partly a power problem" is withdrawn — 4025's null was correct.**
  - **ROOT CAUSE, and it affects BOTH 4025 and 4026: the error bars were understated.** Both quoted the
    **sem over PAIRS** in a distance band, but pairs in a band **share sites** and are not independent.
    Bootstrap over realisations gives **1.57× larger** bars — so 4026's 3.4 sem was really ~2.2 sem
    *before* the value collapsed. **Two compounding errors.**
  - **RULE ENACTED at 4027:** bootstrap over **realisations**, never sem over pair-bins; and check
    **value-stability against reps** before quoting any significance. **Enabling fix shipped: a vectorised
    η** (`4027_retraction_error_bars.py`) — 4026 used 400 reps because the per-site loop was slow, and
    4000 now costs little. **Lane: EW.**
  - **WHAT SURVIVES:** 4026's **geometry** (reach 12.7 edge lengths vs ~3) and the conclusion, now more
    cleanly — with bootstrap-corrected bars, **nothing is resolvable at ANY separation**, 0.2–0.7 sem
    across every band out to 9. **No long-range order along n̂.** And the n̂-vs-transverse **anisotropy is
    also not established**: rotating η's selection axis at 1500 reps gives diagonal − off-diagonal =
    **−0.0009 ± 0.0012 (0.7 sem)**. **Lane: EW.**
  - **Two further limits:** the patch reaches ~3 edge lengths, so ξ ≥ 5 would not show; and the icosian
    cut-and-project is a **proxy** (4013/4015 established it is not the substrate). **Lane: EW.**
  - **STILL SUBMITTED FOR CRITIQUE per PD-008** — now a completed argument with one attack landed and one
    repelled, rather than a flagged worry. **Lane: next window.**
  - **DEFECT FOUND IN PASSING, in the corpus's own order parameter.** 0813's η is *sign det of the 4
    highest-n̂-projection neighbours* — and on the **unperturbed** lattice the 4th and 5th projections tie
    at **120/120** vertices, so "top 4" is arbitrary and swapping two tied rows flips the determinant.
    **η is ill-defined there.** 0813 and 4005 both evaluate η on **perturbed** configurations where the tie
    is broken, so **no result is invalidated** — the gap is in the definition's *statement*, which never
    says a perturbation is required. **Lane: CHIR — fix in the text.**
  - **Structural echo, recorded without a story:** RP fails precisely for the reflections that **flip n̂** —
    and 0973 located the **T-arrow** in that same direction (sign(δ) P-even, **T-odd**). Same place.
    **Lane: CHIR.**
  - **(H-NESS) — CLOSED AS ILL-POSED at Patch 4004, branch (ii).** Not unjustified — ill-posed: a
    susceptibility is a number-fluctuation and Var(N_tot) ≡ 0 for a single walker, so χ = 0 and
    m² = ∞ identically. There was never a single-site reduction to find. Superseded by the item below.
  - **RECOMPUTE χ_η ON THE REAL MECHANISM-A MEASURE — RUN AT PATCH 4005, RESULT FINITE.** χ_η = +0.989 (δ=0),
    +0.788 (δ=0.10), product-base control +0.839 reproducing 0813's 0.87–1.01; d ≥ 1 correlations ~10⁻³.
    0814's O(δ) departure identified as a **single-site skew (+0.2427) carrying no correlation length**.
    ⇒ μ² > 0, unbroken branch, V3 confirmed. **`[PCD-EXT]`, conditional on NON-INTERACTING walkers.**
  - **SSV-coupling correlation length — SPLIT BY RANGE AT PATCH 4006; one half CLOSED.**
    **Zero-range** (rate set by the CP's own GP occupancy) = a ZRP ⇒ stationary measure **exactly
    product** for any rate function and any coupling; verified k = 0…0.9. χ_η finite at any coupling,
    no critical point. **CLOSED.** **Field-range** (rate set by SSV_net sourced at a distance): d = 1
    correlation is real (+0.133 ± 0.003 at k = 0.30 vs −0.034 ± 0.002 at k = 0), d ≥ 2 at noise over
    the sampled range; growth **shape not asserted**. **NOT CLOSED.**
  - **FOUNDER QUESTION (PD-006(a)) — the deciding variable, and it is a picture not a computation.**
    **ANSWERED 14 Sep 2026 (founder, PD-006(a)): "the GPs speak to the CPs, and the CPs move as
    instructed by the GPs."** Agency is GP-side. Resolved against **A3′** at Patch 4007 — each GP
    *broadcasts to its PSR shell* and the receiver *computes the moments of the census it receives*, so
    the GP's state is built from packets arriving from its **first shell**. ⇒ **FIELD-RANGE AT ONE SHELL.**
    The zero-range closure does **not** apply; 4006's d = 1 correlation is real physics.
    *(The question as put used "PSR suppression", a term I coined — the founder had to ask what it meant.
    Corpus phrasing: SSV_abs increases ⇒ PSR is reduced. Coinage retired at 4007.)*
  - **FINITE-SIZE SCALING — REQUIRED. Founder ruled 14 Sep (PD-006(a)): *"Space is composed of
    innumerable 600-cells. I think every GP is the center of its own 600-cell."*** Filed verbatim at
    `founders_voice/4009_ruling_space_is_innumerable_600_cells.md`. **4006's d ≥ 2 result is therefore
    truncated, not complete** — on one closed cell the graph shells are 1, 12, 32, 42, 32, 1, so d ≤ 2
    covers 37.5% of the graph and there is no far region to decay into. **4006's d = 1 result stands.**
  - **BLOCKER ON THE STUDY — ATTEMPTED AT 4010, AND IT HIT AN OBSTRUCTION.** The icosian
    cut-and-project was built and measured. **The unwindowed icosian ring is DENSE** (φ⁻ⁿ ∈ ℤ[φ] for
    every n, verified), so a selection rule is **mandatory** — and a ball window gives shells of
    30 / 45 / 46 / 141 / 165 / 173 points, never 120, at every window and radius tested. **Only the
    origin ever has a 120-shell, an artifact of where the window is centred.** Bounded negative: the
    correct Elser–Sloane window is the projection of the **E₈ Voronoi cell**, not a ball, and that is
    **untested**. **Lane: EW.**
  - **FOUNDER QUESTION — SETTLED MATHEMATICALLY AT 4013: THE STRICT READING IS IMPOSSIBLE, not merely
    unachieved.** In any cut-and-project set a point with perp-coordinate y gets its full 600-cell shell
    iff y + g* ∈ W for all 120 generators. Every conjugate g* is a **unit vector** (verified), and W must
    be **bounded** (the unwindowed ring is dense, 4010). So the point of W extremal in *any* direction is
    always coordination-deficient — measured at **33/120 or 45/120** across W = 1.0, 1.5, 2.0, 3.0, 5.0.
    **The window's boundary always produces deficient points, for a window of any shape.** The nine-window
    lattice scan agrees: shell counts 46 → {58,88} → {58,100} → {109,128,140} → {141,165,173} → six
    distinct values, **never uniform, and more inhomogeneous as W grows.** **So the choice is not between
    two readings — the strict one is unavailable in this construction class, and the class is forced.**
    What remains for the founder is whether the weak reading is what he means, or whether the substrate is
    built some other way entirely. **Lane: founder.** Original framing below.
  - **Recorded at 4013, flagged and explicitly NOT a mechanism:** 2I is **not** closed under Galois
    conjugation, and the conjugate set maps into 2I by an **improper** transformation (det = −1) — so
    **perpendicular space carries the mirror of physical space's 600-cell.** A left/right distinction sits
    inside the construction. It is **not** offered as a chirality mechanism: physical space's own copy is
    achiral (4011), and a mirror relation *between* two spaces is not a handedness *in* one of them.
    Recorded for whoever wants it. **Lane: CHIR / EW.**
  - ~~(PD-006(a)) — and it may be structural, not a construction failure.~~
    Aperiodicity is *forced* (Coxeter, 4009). A quasicrystal evades the crystallographic restriction
    **precisely by having finitely many different local environments.** So *"every GP is the centre of
    its own 600-cell"* read **strictly** — one identical environment everywhere — **is the crystal
    condition Coxeter excludes.** Read **weakly** — every GP has *a* 600-cell of GPs about it while the
    rest of its surroundings differ — it may be satisfiable, and that is what a construction should
    target. **Which is meant? Not decided here: adopting the weak reading unilaterally would quietly
    weaken an axiom-level statement to make a computation possible. Lane: founder.**
    ~~The lateral lattice is not constructed anywhere in the corpus.~~ The φ-nested
    hierarchy is **not** it — 0736 puts that nesting **inward**, to ~l_P/10³⁰. Named candidate: the
    **icosian registration** (DM `reasoning/2665.md`). Verified at 4009 that the 120 vertices are unit
    quaternions closed under quaternion product = the binary icosahedral group 2I, so the icosian ring
    is the natural generator with z = 12 preserved. **Build the construction first; do not guess a
    lattice and measure ξ on it. Lane: EW.**
  - **Consequence recorded at 4009:** the substrate is necessarily **aperiodic** — the 600-cell's
    dihedral angle 164.4775° does not divide 360° (verified), reproducing the Coxeter result SR.md R4
    carries panel-closed. So the extended lattice is an **icosahedral quasicrystal**, the same object
    R4/R5 built the Lorentz W2 world-call on. **Lane: EW / SR.**
    ~~Suspended at 4008 pending a founder ruling.~~
    4007 said this study was needed because the route had run on the wrong object. **That is withdrawn:**
    §177's "neighbouring vertex B" is misstated — shell 7 of A is shell 1 of A's **antipode**, a fact
    about **one closed 600-cell** (verified, `4008_a2_lattice_reading.py`), and the shells sum to 120.
    **FOUNDER QUESTION (PD-006(a)):** is A2's substrate the **closed 120-vertex S³ tessellation** (EU lane
    Patch 1300's reading, χ(S³) = 0), or is it **extended** — as "600-cell host vertex" language
    (FI-C-RC-2; 1200 W-bracelets = 10 × 120 host vertices) suggests? **Closed ⇒ no thermodynamic limit,
    ξ not well-posed, 4006's measurement is the complete answer and the route CLOSES. Extended ⇒ the
    study is required.** **Lane: founder.** Superseded text below.
    ~~NOW REQUIRED (the answer was field-range), AND RESPECIFIED AT 4007.~~
    4006 said the problem was that 120 sites of diameter 5 cannot resolve ξ > ~2. **The sharper
    statement: ξ is not defined on that object at all.** A2 says the substrate is a **tessellated**
    600-cell and `programme_orientation.md` §177 says every GP is the centre of its own 600-cell
    (shell 7 of A is shell 1 of B) — so a single 600-cell is the **first shell around one host
    vertex**, not the substrate. **Every computation in this route — 0694, 0813, 1100, 4005, 4006 —
    ran on the single cell.** Fine for a local observable like η_v; **the wrong object for a
    correlation length.** The study must be run on a **tessellated patch**, not a bigger polytope.
    **NOT DONE. Lane: EW.**
  - **Recorded at 4006, not acted on:** ZRP condensation in the zero-range sweep (on-site variance
    2.90 → 10.54). A marginal effect, not a correlation length — but it is a real feature of the
    occupancy distribution and nothing in this lane has costed it. **Lane: EW.**
  - **Carried unchanged from 0904:** condition (1) the real η (H₄/H₄⁺ coset field) must be confirmed
    **local** — 0813's η is a defensible proxy; condition (3) Mechanism A (`OPEN-FP-F1-2`) sits under the
    whole route. **Lane: EW / CHIR.**
  ~~0905's parked item, now the live one.~~
    0813 got χ_η = 0.87–1.01 (finite, positive ⇒ μ² > 0, V3 confirmed, V1-by-condensation foreclosed
    on that branch — framing corrected at 0904). But that sits on an **assumed product (ZRP-template)
    base**, and 0814 found the real NESS **departs from it, skewed at O(δ)**. 0905: *departs from
    product is NOT critical* — the recomputed χ could be finite-but-non-product or could reveal
    correlations; **unknown until run**. Well-posed definition supplied at 4004: a proper subvolume,
    Var(n_S) = K p_S(1−p_S) > 0. **NOT performed at 4004. Lane: EW.**
  - **`[PCD-EXT]` label (PD-007):** the occupation generator on a proper subvolume is the adopted
    working PCD extension for this route; every result on it carries `[PCD-EXT]` until the
    triangulation ledger closes. **Lane: EW.**
  - **CORRECTED at 4004: not "three months idle".** The lift ran at 0812/0813, was corrected at 0814/0815 and assessed at 0904/0905; 4003's claim rested on a grep scoped to two paths and generalised. What survives: no queue entry carried it. ~~cleared at 0692 and not run in three months~~
    THEO-CHIR-CAPACITY-1 was reserved then and was ENACTED at 0960; Mechanism A and pointwise
    non-degeneracy discharged at 0960/0968. **This is the next physics action in the lane. Lane: EW.**
  - **NOT PERFORMED, named as a candidate lead only (D-4):** Patches 0965/0968 established a per-vertex
    participation floor p(v) ≥ 4 for the *dynamical* η — a statement about the η-field rather than the
    single walker, which is the half of (H-NESS) that 1100 called *"lift π to the η-field measure."*
    Whether it bears on the lift **has not been checked**. Do not cite it as progress until it is.
    **Lane: EW.**
  ~~Its `Dependencies` line has read *"requires EW development"* since 16 May 2026; that is the condition
  this block exists to supply — now MET.~~ Original entry: Its `Dependencies` line has read
  *"requires EW development"* since 16 May 2026; that is the condition this block exists to supply.
  **Lane: EW (with SM/SR).** Flagship scale — scoped and declined three times from the chirality lane,
  correctly, for want of exactly this.
- **`TODO-0976-RECOMPILE` — SM-2's hold is LIFTED at Patch 4002; all five are now ready for Isak.**
  ~~do NOT recompile SM-2 yet~~ — SM-2's `.tex` carries edits (a)–(f)
  and is owed a PDF, but edit (g) is held on `OPEN-EW-7`. Recompiling now buys a second recompile later.
  **The other four papers in that entry (Capotauro, chirality_continuum, TARROW-2, F.1) owe nothing and
  are ready for Isak now.** Lane: EW holds SM-2's release; CHIR holds the other four.

- **Added at Patch 4002 (EW lane), carried forward under `TODO-4000-EW`:** SM-2's `E_inter` switch rule —
  *on iff the object has a closed polyhedral cage* — is an empirical read of the table's own 12/12
  consistency and is **not stated in prose anywhere in SM-2**. A printed number now rests on it. Owed:
  either derive the rule from the mass formula or state it explicitly in SM-2's Universal Refinements
  section at the next revision. **Lane: EW.**
- **Also at 4002:** `E_cloud`/Total is **not** uniform across the table (0.10 electron, 0.02 muon/tau,
  0.06 up, 0.05 everything else) with no rule given. Pre-existing, unrelated to the W, found while
  testing a first formulation that this falsified. Not acted on. **Lane: SM.**

---

### TODO-4015-EW — the chirality result extends; and what is and is not blocked

- **4011/4012's chirality answer SURVIVES the extended lattice — verified at 4015, not assumed.**
  The obvious worry after 4009 was that 4011 was truncated by the single 600-cell the same way
  4006's correlation measurement was. It is not. On a **4321-point extended patch**: **96 improper
  signed-permutation symmetries** at every window tested (1.2, 1.4, 1.5), including the same
  `R = diag(1,1,1,−1)`; and the direct 3-hop sum over **153,576 paths** is **zero** at δ = 0 and
  machine-zero at δ = 0.35.
- **Why it survives and 4006 did not — worth keeping, it decides what else is safe:** a correlation
  length is a property of the **whole structure**, which a diameter-5 graph cannot express. A mirror
  pairing is a property of the **generators** — every path is built from the same 120 step vectors,
  and those admit an improper symmetry fixing n̂. Extending adds paths; it adds no unpaired step.
- **CONSEQUENCE: FI-C-9 = V3 does not depend on any of the blocked work.** The susceptibility route
  (4005–4009) remains blocked on the founder's reading and the lateral construction; the **path**
  route reaches the same conclusion and depends on neither.
- **A SECOND failure of the cut-and-project class, found in passing.** Edge coordination on the
  extended patch runs **{12, 13, 14, 18, 19, 26}** — only **120 of 4321** points have z = 12.
  Independent of 4013's window-boundary argument and pointing the same way: this class is not the
  substrate's lateral construction. **Wording corrected at 4016:** 4015 put this next to *"SF-4
  requires z = 12"*, which reads as SF-4 being contradicted. **It is not** — a construction already
  known to be wrong giving a wrong z says nothing about SF-4. **Lane: EW.**
- **STILL UNANSWERED and still the deciding question (founder, PD-006(a)):** the strict reading is
  impossible (4013) — is the **weak** reading what is meant, or is the substrate built some other
  way entirely? **Lane: founder.**

---

### TODO-4014-EW — corpus hygiene: two corrupt files repaired, and a third gate

- **Found by a gate CRASHING, not by review.** `code/deferral_gate.py` died with
  `UnicodeDecodeError` reading the 4013 diff. Cause: a heredoc mangled `E₈` into the bytes
  `E 0x82 0x88` — ASCII `E` plus the tail of U+2088 with its lead byte lost. **Invisible in every
  rendered view and in `git show`.** Repaired in `series_standard_model/reasoning/4013.md`.
- **The same sweep found an OLDER one, not mine:** `Eötvös` stored as `E\xb6tv\xc3\xb6s` in
  `series_phenomena/cosmology/dark_matter/relic1_qm2_gate_smA_fails.md`. Repaired. **Lane: DM —
  noted, since it means a DM-lane file was written with a broken byte and nothing caught it.**
- **`code/deferral_gate.py` hardened**: decodes with `errors="replace"`. A gate that crashes on bad
  input is a gate that is not run.
- **`code/encoding_gate.py` added**: refuses a patch introducing invalid UTF-8 into a text file;
  `--all` sweeps every tracked file. Currently **0 of 7908**.
- **Standing:** silent mojibake is the worst class of corpus error — it does not fail, does not
  render wrong enough to notice, and survives review. Three gates now: deferrals, absences,
  encoding. **Lane: EW (done).**

---

### TODO-4011-EW — the multi-hop chirality question, answered; and one unregistered quantity

- **ANSWERED at Patch 4011 (founder question, filed verbatim).** Multi-hop DI-bit path disparity is **real**
  (hop count and physical distance separate from the 2nd re-radiation on) but **cannot produce chirality**:
  2 hops carry no 4D pseudoscalar at all; 3/4/5 hops cancel to machine precision over 2.1M paths at every
  tilt tested; and the cause is that H₄ contains reflections, so the result holds at **every** hop count.
  **Confirms FI-C-9 = V3 independently of the susceptibility line.**
- **~~OPEN — an unregistered quantity~~ — RETRACTED AT 4012, THE CLAIM WAS FALSE.** The 10% shell is the
  **PSR shell radial thickness σ_r/⟨r⟩ ≈ 0.096 (F-E2-3)**, recomputed at **D-SUBPSR-FIELD pass 3** under
  **R-OUTWARD-FANOUT** (Patch 3135) as **0.093–0.076 over N = 6–22 hops**, with **D-ARC-GAMMA** minted on
  it. **Derived, not an estimate; registered, not missing.** Nothing owed to the founder here.
- **NEW at 4012, and it is a real flag: the 10%-band derivation runs on an FCC PROXY.**
  `series_phenomena/cosmology/sea_gravitation/scripts/3133_subpsr_cascade.py` builds an **FCC lattice**
  (integer triples, even coordinate sum, 12 neighbours) — z = 12 matches the icosahedral coordination, but
  it is **3D and periodic** where the substrate is 4D and aperiodic. For a shell-*thickness* number the
  proxy may well be adequate; **that is not the EW lane's call to make.** Does **not** unblock 4010.
  **Lane: EU / SEA-GRAV.**
- **Recorded at 4012:** the single 600-cell **saturates by 5 hops** and has **zero** 6-hop outward-fanout
  paths, so the corpus's N = 6–22 hop regime cannot live on one cell — independent agreement with the
  founder's 4009 extended-lattice ruling. **Lane: EW.**
- **NOT superseded by 4011:** the lateral-lattice blocker (4010) and the strict-vs-weak reading of *every GP
  is the centre of its own 600-cell*. 4011 answers a different question and leaves both open. **Lane: EW /
  founder.**

---

### TODO-4016-EW — SF-4's z = 12: not revised, but carrying an unchecked inheritance

- **Founder asked (14 Sep) whether the neutrino result needs revising against the lattice. It does
  not**, and 4015's wording invited the worry — corrected at 4016.
- **What SF-4 claims, read from `sf-4_neutrinos.tex` rather than from a citation:** `z = 12 as
  600-cell coordination number — THEOREM (inherited from SS-1, SM-1)`, glossed as *each vertex has
  12 nearest neighbors arranged icosahedrally*. **True of the polytope, verified: all 120 vertices
  have exactly 12.**
- **THE UNCHECKED STEP, and it is real.** That theorem is about **one** 600-cell. SF-4 uses z as a
  **per-GP property of the substrate** (*every Grid Point emits its fixed DI-bit complement toward
  one of its z = 12*). The founder ruled at 4009 that space is **innumerable** 600-cells. **Whether
  every GP of the extended substrate has exactly 12 nearest neighbours has never been shown — it is
  inherited.** Same gap as the missing lateral construction. **Lane: EW / SF.**
- **AND THE EXPOSURE IS STEEP.** SF-4 depends on z twice: `M₀ = m_e·z/φ` (linear) and
  `σ_ν = z^(−2d_eff) = z^(−10)`, so **Σm_ν ∝ z^(−9)**. Reproduced: **64.9 meV at z = 12** (paper's
  number). **z = 13 → 31.6 meV (half). z = 14 → 16.2 meV.** z is an **integer**, so there is no small
  perturbation available — the nearest alternative is a factor-2 move on a cosmologically
  constrained prediction. **Not a reason to doubt z = 12; a reason the inheritance deserves an
  actual check.**
- **CONSEQUENCE FOR PRIORITY:** the founder's outstanding lateral-construction question now carries
  **SF-4's absolute neutrino mass scale** as well as the chirality route. **Lane: founder.**

---

### TODO-4017-EW — the 600-cell honeycomb is hyperbolic, and that closes the strict reading

- **Computed at 4017 (Coxeter Gram signatures, method first checked against five known cases):**
  the **Euclidean** regular honeycombs of 4-space are exactly **{3,3,4,3}, {4,3,3,4}, {3,4,3,3}** —
  **none a 600-cell honeycomb**, confirming 4009's dihedral-angle result by an unrelated route.
- **BUT {3,3,5,3} EXISTS AND IS HYPERBOLIC.** So the strict reading — innumerable 600-cells, every
  GP identical — **is realizable, regular and vertex-transitive, in H⁴.** **4013's presentation
  over-reached**: its proof stands exactly as proved, but *"the class is forced"* silently assumed a
  Euclidean embedding.
- **THE PRICE, AND THE PROGRAMME CANNOT PAY IT.** The vertex figure of {3,3,5,3} is **{3,5,3}, itself
  hyperbolic** — an infinite honeycomb — so **z = ∞**. (The single 600-cell's vertex figure is {3,5},
  the icosahedron: spherical, z = 12.) **z = 12 is load-bearing in SS-1, SM-1, SM-7, SM-8, SM-9 and
  SF-4**, with Σm_ν ∝ z⁻⁹ (4016). **⇒ strict reading CLOSED — impossible flat, and curved costs z.**
- **BOUND ON THE NEGATIVE:** this classifies **regular** honeycombs only. **Uniform-but-not-regular
  is not ruled out.** Searched unscoped: the corpus uses *vertex-transitive* only of the **single**
  600-cell under H₄ (SF-2 §§463/580/701; FP.md L4-B), never of an extended non-regular structure.
  **Lane: EW.**
- **Three classes now closed by three unrelated arguments:** periodic Euclidean (4009, dihedral
  angle), bounded-window cut-and-project (4013, window boundary), regular at any curvature (4017).
  **The weak reading is the only survivor in play — still the founder's to rule, but the option space
  is now exhausted rather than sampled. Lane: founder.**

---

### TODO-4018-EW — two more construction classes closed; three arguments, none related

- **Bravais lattices, ANY dimension — CLOSED.** The 600-cell's 12 nearest neighbours all share the
  same inner product with the vertex (−0.190983), lie in one 3-flat, and sit **strictly on one side**;
  their offsets sum to **2.291796**, not zero, and {2v₀ − wᵢ} ≠ {wᵢ}. A Bravais lattice has inversion
  symmetry at every point, so its nearest-neighbour set is **always** centrally symmetric about that
  point. **The 600-cell's is not.**
- **Any periodic structure with full H₄ site symmetry — CLOSED.** H₄ contains isoclinic rotations of
  trace **±2/φ and ±2φ — irrational**. Trace is basis-independent, so no conjugate of H₄ lies in
  GL(4,ℤ): **H₄ has no faithful integral representation and is not crystallographic in 4D.**
- **AN IDENTITY, recorded and explicitly NOT a mechanism.** |Σ(wᵢ − v₀)| = **2.291796068** — which is
  **exactly Patch 1100's graph-Laplacian spectral gap λ₁**, and both equal **12(1 − φ/2)**. The vertex
  figure's central *asymmetry* and 1100's spectral gap are one quantity seen twice. Worth someone's
  attention; no story attached here. **Lane: CHIR / EW.**
- **FIVE classes now closed by five unrelated arguments:** periodic Euclidean (4009, dihedral angle);
  cut-and-project (4013, window boundary); regular honeycomb at any curvature (4017, Gram signature);
  Bravais (4018, central asymmetry); full-H₄ periodic (4018, irrational trace).
- **NOT CLOSED, stated so it is not mistaken for closed:** periodic vertex-transitive structures whose
  site symmetry is a **proper subgroup** of H₄ but whose 12 nearest neighbours still form a regular
  icosahedron; and **aperiodic** uniform structures outside the cut-and-project class. **Five closed
  classes is not a proof that nothing works. Lane: EW / founder.**

---

### TODO-4019-EW — one fact underneath all five closures, and the question restated

- **The 600-cell carries a 7.356° ANGULAR DEFICIT PER EDGE.** Counted, not quoted: f-vector
  (120, 720, 1200, 600); **5 tetrahedra per edge**; regular-tetrahedron dihedral = arccos(1/3) =
  70.5288°; **5 × 70.5288° = 352.644°** against the **360°** a flat structure needs. 360/θ = 5.1043,
  not an integer. **Positive deficit is positive curvature — the 600-cell is intrinsically spherical.**
- **That single fact is underneath all five closures** (4009 dihedral angle, 4013 window boundary,
  4017 Gram signature, 4018 central asymmetry, 4018 irrational trace). Each fails in its own
  vocabulary; all are symptoms of one frustration. It is the **4D form of the classic icosahedral
  frustration, and the same number** — which is why icosahedral short-range order is everywhere in
  real matter and icosahedral crystals do not exist.
- **THE QUESTION IS RESTATED, AND I HAD BEEN ASKING THE WRONG ONE.** Not strict-vs-weak reading:
  - **(A) FLAT space, DISTORTED cage** — keep z = 12 and near-icosahedral order, give up the
    icosahedron being *exactly* regular; the 7.356° absorbs as strain, which is what real icosahedral
    matter does. **OPEN, and the survivor.**
  - **(B) EXACT cage, CURVED space** — keep the regular 600-cell, pay curvature. **Priced and CLOSED
    at 4017**: the only regular honeycomb of 600-cells is hyperbolic and costs z = ∞.
  **(A) is a different question from the weak reading** — weak reading was *which GPs have a
  600-cell*; this is *whether the 600-cell is regular*. I had not separated them. **Lane: founder.**
- **NOT CLAIMED:** the deficit forbids **exact** regularity in flat space and says nothing against a
  distorted cage — real icosahedral quasicrystals are the existence proof that the distorted version
  is constructible. The two classes 4018 left open remain open. **Lane: EW.**

---

### TODO-4020-EW — the distorted-cage ruling: what it costs, what it does not give, what it opens

- **FOUNDER RULED (A) 14 Sep, verbatim at `founders_voice/4020_ruling_distorted_cage.md`:** *"I think
  the 600-cell space is allowed to be slightly distorted, just like materials with icosahedral
  packing."* **The six-patch strict-vs-weak referral is closed by a ruling on a different axis.**
- **z = 12 SURVIVES.** Distortion does not change *who* a vertex's neighbours are at any amplitude
  tested — what SS-1, SM-1, SM-7, SM-8, SM-9 and SF-4 all require.
- **IT DOES NOT SUPPLY A CHIRALITY MECHANISM — tested immediately, because it might have.** The V3
  defence rests on `R = diag(1,1,1,−1)` being *exact*, and a distorted cage does not have it exactly.
  12 realisations at each of ε = 0.01/0.03/0.08: the 3-hop sum is nonzero in **every** realisation but
  its **sign wanders with the seed**, mean well inside one sd of zero (|mean|/sd = 0.16, 0.01, 0.15).
  **Each strained cage is chiral; the ensemble is not.** **FI-C-9 = V3 survives a fourth independent
  test** (4011 single cell, 4012 fan-out rule, 4015 extended lattice, 4020 distorted cage).
- **~~NEW OPEN PROBLEM~~ — NOT NEW. CLOSED-BY-REDUCTION AT 4021: it is THEO-CHIR-VW-1's question in
  different clothing.** A strain functional built from pairwise **distances** is invariant under every
  isometry, proper or improper (verified), so the relaxation landscape is **mirror-symmetric by
  construction**: mirror-image starts relax to mirror-image ends of **identical energy and exactly
  opposite handedness** (±8, ±17, ±3 over three seeds). **No gradient flow on an achiral functional can
  bias the sign.** So any handedness must be **spontaneous** — two exactly degenerate minima, one picked
  per domain — which is a ℤ₂ SSB on the substrate, **exactly VW-1's subject**, whose sole residual **(H1)**
  is already on this queue. Registering it as new would have split one problem into two. **Lane: EW.**
  ~~is the FRUSTRATION RELAXATION handed?~~
  Random strain is not the physical strain; the physical distortion is the structured relaxation of
  7.356°/edge, which in 3D icosahedral matter organises into **disclination networks**. Whether such a
  network carries handedness is a real condensed-matter question. **NOT investigated at 4020 — random
  perturbation cannot settle it either way. Lane: CHIR / EW.**
- **SF-4's z = 12 inheritance (4016): now PHYSICALLY MOTIVATED, still NOT SHOWN.** Uniform z = 12 with
  distorted icosahedra is what real icosahedral matter does. Plausible is not shown. **Lane: EW / SF.**
- **LATERAL-CONSTRUCTION TARGET — RESTATED AT FULL STRENGTH AT 4030. "Uniform z = 12" was too weak.**
  The requirement is that the nearest-neighbour shell contain **EXACTLY twelve points** — not twelve on
  average, not twelve *chosen from* a larger equidistant set — **and that those twelve span a 3-flat**.
  Both hold in the 600-cell by construction. Plus flat 4D and the 7.356°/edge carried as strain.
  Cut-and-project remains wrong (4015, and now 4030 for a third reason).
- **CORRECTION, caught by `absence_gate.py` inside this very commit: "nobody has built it" is FALSE.**
  Searched unscoped — **Patch 2685 (DM lane, `code/2685_r1_l1_arenas.py`) builds FOUR extended
  z = 12 arenas**: FCC ball, HCP ball, random-stacking Barlow ball, FCC-cubic, each *"z = 12-equivalent"*
  with coordination checked before use. They are **3D close-packings (cuboctahedral), labelled proxies**,
  so they do not hit the 4D near-icosahedral target — but they are real prior art. **Fifth scoped-grep
  near-miss this session, and the SECOND time the DM/sea-grav lane's proxy work has surfaced in this
  lane's blockers (4012 found their FCC sub-PSR cascade). That lane has been solving extended-z = 12
  with 3D proxies for months and this lane did not know. Lane: EW / DM — worth a look before building.**

---

### TODO-4021-EW — the relaxation question reduces to VW-1; and what a mechanism would actually need

- **Prior art read before building, per the note 4020 filed.** DM Patch 2685's four arenas
  (`fcc_ball`, `layered_ball`/HCP, `barlow_seq`, `fcc_rot_cube`) are real extended z = 12
  constructions, sanity-checked for coordination 12 and min-chord — but **3D close-packings with
  cuboctahedral order**, labelled proxies. Precedent, not lattice.
- **A chirality mechanism in the relaxation would need ONE of:**
  - **(i) an achirality-breaking term in the substrate dynamics** — i.e. an energy functional that is
    **not** a function of distances alone. **Nothing in the axioms supplies one**: A1′/A3′ are
    distance-and-census based. Changing that is an axiom change. **Lane: founder.**
  - **(ii) an external bias selecting between the degenerate minima** — which *is* a primitive
    handedness. **FI-C-9 = V3 restated, not derived.**
  **Both branches lead back to V3 or to H1 — the fifth independent route to the same place today.**
- **NOT CLAIMED:** that no relaxation mechanism exists. Only that a **distance-based** strain
  functional cannot supply one. **The disclination-NETWORK question is untouched at the network
  level** — 4021 treats the energetics, not the topology. **Lane: CHIR / EW.**

---

### TODO-4028-EW — 4027's rule applied backward: 4006 audited and SURVIVES

- **The exposed candidate was 4006**, because everything from 4007 onward — the founder's range
  question, the extended-lattice ruling, the whole 4009–4027 arc — sits downstream of it, **and it
  quoted a sem over three seeds.**
- **RE-RUN AT 16 SEEDS: 4006's headline reproduces almost exactly.** Reported −0.034 → +0.133; measured
  **−0.0322 ± 0.0011 → +0.1323 ± 0.0037**. The sign flip is a **42-sem effect. 4006 stands.**
- **THE DIAGNOSIS IS CONFIRMED BY A CASE WHERE IT PREDICTS SURVIVAL.** 4006 averaged over **independent
  runs**; 4026 over **pairs within a band**. The first is the right structure with too few samples; the
  second is the **wrong structure**, which no sampling fixes. *A rule that only ever condemns is not a
  rule.*
- **SCOPE, checked across every 40xx script rather than asserted:** only **4025 and 4026** used
  sem-over-pairs, both corrected at 4027. **Nothing else needs revisiting. Lane: EW — closed.**
- **4006's refusal to assert the growth SHAPE is vindicated:** at 16 seeds k = 0.60 still gives
  **+0.612 ± 0.092**. The non-monotonicity is real and its form unresolved. **Lane: EW.**
- **OPERATIONAL, AND IT NEEDS THE FOUNDER'S EYES: Patch 4027 was NOT on origin.** `origin/main` sat at
  4026 though 4027 had been reported applied; recovered from the local reflog, and a routine
  `git reset --hard origin/main` at bootup had already discarded it once. **4028 will not apply to an
  origin lacking 4027 — apply 4027 first.** **A patch that silently fails to apply is the one failure
  mode this workflow has no gate for.** **Lane: founder / EW.**

---

### TODO-4029-EW — the missing-patch gate built; and a real defect found in `next_id.py`

- **`code/continuity_gate.py` SHIPPED.** Compares local vs origin **by patch number, not by SHA** —
  `git am` on the founder's machine rewrites SHAs, so a SHA comparison reports every applied patch as
  missing (that false positive was hit and fixed while building it). Reports per-lane gaps in the
  committed run. **Gaps are reported, not failed:** a gap may be an unparsed reservation and nothing
  inside the repo distinguishes them; failing on them would make the gate noise, which is how gates die.
- **STATED LIMIT:** a cleanly-missing **tail** patch is not detectable from inside — the missing patch
  is also the one that would have updated the registry and the frontier header, so what remains is
  self-consistent at N−1. **That half is procedural and belongs in the apply macro.**
- **AND THE SCAN FOUND A REAL DEFECT IN `next_id.py`, the canonical ID gate.** It matched
  `Patch(?:es)?\s+(\d{4})` — capturing the **first** id and stopping. So a commit titled *"Patches
  3406/3407"* registered 3406 and left **3407 reading as FREE**. **21 ids were invisible** to the old
  pattern, from forms like *"Patches 0359, 0360, 0361, 0363"* and *"Patches 0314 / 0344"*. **Fixed:
  every id in a multi-id reference is now taken.**
- **NOT OVERSOLD: no lane's NEXT FREE changed.** DE rises 49 → 51 used, legacy-cosmology 99 → 100.
  **The defect was real and had not yet bitten** — a hardening, not an averted disaster. But the
  collision it could have caused is the exact shape the registry's Anomalies section records three times.
- **GAPS LEFT STANDING, HANDED TO THEIR LANES WITH THE EVIDENCE, NOT INVESTIGATED HERE:** **chir 0901,
  0934** (0978 is documented — superseded before push); **de 3427, 3428, 3437, 3447**; **dm 3502**.
  3406/3407 are explained by the fix above. **Not called losses** — this lane does not own those blocks.
  **Lane: CHIR / DE / DM.**

---

### TODO-4030-EW — the rank-based rescue for the cut-and-project, tested and killed

- **THE RESCUE:** 4015 measured z ∈ {12,…,26} with a **distance threshold**. In real quasicrystals and
  glasses coordination is **rank-based** — the 12 *nearest* — under which z = 12 holds by construction,
  and the class might have met 4020's target after all. **Tested. It does not.**
- **AND THE REASON IS NEW.** The coordination shell is **over-populated**: **13, 18, 19 or 26 points sit
  at the nearest distance** where the 600-cell has **exactly 12**. So "the 12 nearest" is a **choice among
  equals**, not a determination — the same degeneracy failure 4023 found in η, in a different object.
  **And the chosen twelve do not lie in a 3-flat** (s₄/s₁ = 0.52 against the 600-cell's 1e-16), so they
  are not a strained icosahedron but structurally a different object, and no choice among the equidistant
  points fixes it.
- **THIRD independent failure of the icosian cut-and-project**: 4013 window boundary; 4015 z-spread under
  a threshold; 4030 over-populated shell + loss of the 3-flat under a rank definition. **And 4015 is not
  merely confirmed but explained** — the spread was never a threshold artifact.
- **METHOD NOTE worth keeping:** the test only works because the offsets are **centred before the SVD**.
  An uncentred SVD gives **0.56 for the 600-cell itself**, which would have read as *the patch is as good
  as the reference*. Knowing to centre comes from **4018's** finding that the neighbour icosahedron is not
  centred on its vertex — an earlier result in this same session was needed to make this measurement mean
  anything. **Lane: EW.**

---

### TODO-4031-EW — prior art I missed for an entire arc, and the cross-sector tension it exposes

- **A DIRECTORY I NEVER SEARCHED: `Development/transcripts/`.** Across 4008–4030 my greps covered
  `frontier_sectors/`, `todolist.md`, the registry, `series_*/` and `founders_voice/` — **never this.**
- **A transcript dated 23 June 2026 already states**: the 600-cell **cannot tessellate flat 4D Euclidean
  space**; **only the tesseract, 16-cell and 24-cell** tile 4-space; it **tiles S³ and hyperbolic space**;
  and — decisively — *"the corpus's tessellated 600-cell lattice"* is **under-determined**, branching into
  **two readings**. **That is 4008's finding, three months early, and 4017's Euclidean result in prose.**
- **WHAT WAS NOT DUPLICATED, in fairness:** 4009 cited SR.md R4 for Coxeter at the time — that part was
  done properly. And the arc added: **4017's pricing of the hyperbolic branch (vertex figure {3,5,3} is
  itself hyperbolic ⇒ z = ∞ — the transcript names hyperbolic as live and never prices it, and the price
  is what closes it)**; 4019's 7.356°/edge single cause; 4018's Bravais and H₄ closures; the quasicrystal
  branch **tested** and failed three ways (4013/4015/4030); two founder rulings.
- **`code/absence_gate.py` extended:** it now names the easy-to-miss paths (`Development/transcripts/`,
  `archive/`, `founders_voice/`) when an absence claim's evidence does not mention them. **Lane: EW —
  done.**
- **THE CROSS-SECTOR TENSION, AND IT IS THE POINT.** `SR.md` R4/R5 is **panel-closed** on the substrate
  being an icosahedral **quasicrystal**, and the terminal **W2** world-call rests on it. **4030 showed the
  icosian cut-and-project quasicrystal fails the SM-side requirement** — nearest shell of 13/18/19/26
  equidistant points, not exactly 12, and the chosen twelve not spanning a 3-flat, which SS-1, SM-1, SM-7,
  SM-8, SM-9 and SF-4 all need. **Either the substrate quasicrystal is a different object from the icosian
  cut-and-project, or SR's structural commitment and SM's coordination requirement conflict.** Both are
  load-bearing; neither lane has looked at the other on this point. **NOT resolved here — SR's R4/R5 is
  panel-closed and belongs to that lane. Lane: SR / SM / founder.**
- **AND THE 4009 TENSION IS STILL OPEN:** SR.md treats SR-1's φ-self-similar **nested**-600-cell hierarchy
  *as* the substrate quasicrystal, but **0736 puts that nesting inward**, to ~l_P/10³⁰. If the nesting is
  the fine scale, SR.md's identification needs a **lateral** structure it does not name. **Lane: SR / EW.**

---

### TODO-4032-EW — the tension traced to SR-1's own "Topology Clarification", and sharpened

- **A HYPOTHESIS TESTED AND REFUTED, recorded rather than dropped.** 4030's *twelve must span a 3-flat*
  is the signature of a locally **3-dimensional** structure, and SR.md R5's "icosahedral point symmetry"
  and "l = 6" are 3D objects — so the natural resolution of 4031's tension was that SR means a **3D**
  quasicrystal while I built a 4D one. **SR-1 says otherwise in as many words:** *"we adopt the
  **quasicrystalline approximation**: space is flat **ℝ⁴** at macroscopic scales, constructed by modular
  repetition of 600-cell motifs with overlapping Voronoi [cells]."* **The tension does not dissolve.**
  It was the convenient answer and would have cost nothing.
- **AND THE PRIOR ART IS WORSE THAN 4031 REPORTED: it is a SHIPPED PAPER, not a transcript.** SR-1 has a
  subsection titled **"Topology Clarification"** whose first sentence is *"The finite 600-cell tiles the
  3-sphere S³, not flat ℝ⁴."* **4008's "discovery" was in a flagship paper's section heading.** Sixth
  and worst instance of the same failure this session.
- **THE ITEM, STATED IN THE TWO DOCUMENTS' OWN WORDS.** SR-1 calls it an **approximation** and is honest
  about it — nothing here contradicts SR-1 or touches its W2 world-call. **But SM uses the same structure
  EXACTLY:** SS-1, SM-1, SM-7, SM-8, SM-9 and SF-4 take z = 12 in a 3-flat as a *theorem about the
  600-cell* and apply it **per-GP to the substrate**. **The gap is between "approximation" and "exact",
  and it is where SF-4's Σm_ν ∝ z⁻⁹ sensitivity lives** — one integer step halves a cosmologically
  constrained prediction (4016), and an approximation does not promise an integer.
- **NOT a claim that they are inconsistent.** An approximation and an exact use of the same object are
  not a contradiction **until someone bounds the error. Nobody has. That is the item.**
  **Lane: SR / SM / founder.**

---

### TODO-4033-EW — the error cannot be bounded because the construction was never specified

- **I HAD NEVER BUILT WHAT SR-1 ACTUALLY NAMES.** Its construction is *"modular repetition of 600-cell
  motifs with overlapping Voronoi cells"* — **not cut-and-project**, which is what 4010–4030 all tested.
  Different constructions. **Seventh instance today of building on my own reading instead of the
  corpus's.**
- **SO I BUILT IT, on the most literal reading (mine, labelled): translate the 120-vertex motif by t·u
  for u in the motif, union.** No t gives anything like uniform z = 12 (**best 2.7%**), and **at several
  t the nearest-neighbour distance is 0.0000 — coincident points.** A point set with coincident points is
  not a lattice, so **the reading is wrong** — and that, not the failure, is the finding.
- **THE ACTUAL FINDING: SR-1's approximation is not specified to a level that can be checked.** The
  phrase names a **family**, not a recipe: it fixes neither the translation set, nor the overlap rule, nor
  what happens where motifs collide. **⇒ 4032's error term CANNOT be bounded until the construction is
  specified** — you cannot measure the deviation of an unbuilt object from an exact requirement.
- **AND THIS IS THE ROOT CAUSE OF THE WHOLE 4009–4032 ARC.** Every lattice built — icosian
  cut-and-project (4010/4013/4015/4030), the anisotropic patch (4026), this one — was **my guess at what
  the corpus means. The lateral lattice was never unbuilt because it is hard; it was unbuilt because it
  was never specified.**
- **RESOLVING IT NEEDS ONE OF TWO THINGS, and neither is this lane's:**
  **(i)** SR-1's construction written out to build level — translation set, overlap rule, collision
  handling; or **(ii)** a **founder ruling** that some named standard construction *is* the intended one,
  after which it can be built and measured in an afternoon. **Lane: SR / founder.**
- **SEARCHED UNSCOPED BEFORE CLAIMING IT** — `absence_gate.py` failed a draft of this, correctly. Outside
  my own files the phrase occurs only in **SR-1**, its **revision chain** (a *different* use — ΔSSV
  geometry inside cells, not lattice construction), and **two copies of one figure**. **The figure's own
  title says "Schematic"** — *600-Cell Quasicrystalline Lattice (Schematic 3D Projection)*. **The paper
  does not claim to give a construction.**
- **AND THE SECOND COPY IS SM-1's** — `series_standard_model/figures/figures-SM-1/` carries the **same**
  schematic. **So the SM sector adopted the same unspecified construction rather than supplying one of
  its own** — which is why the gap has never surfaced from either side.
- **ONE CONSTRAINT GAINED from the figure, worth having:** *"Grid Points at **all vertices**"* — every
  motif vertex is a GP, which **rules out** any reading where overlap merges or discards vertices.
  **Lane: EW — carry into the build once the construction is specified.**
- **NOT claimed:** that the approximation is bad. **Unbuilt is not wrong**, and there is no measurement
  either way. The literal reading is filed as **refuted**, which is evidence about the sentence's
  ambiguity and nothing more.

---

### TODO-4034-EW — the specification is not free: tiling and exactly-twelve pull against each other

- **4033 asked the founder to specify the construction. Under PD-008 I narrowed it first** — tested the
  candidates before handing over. **Four more fail:** φ-inflation shells, and motif-at-each-vertex at
  t = 1, φ, 2. All at z = 12 fraction **0.000**.
- **AND THE REASON IS A TRICHOTOMY IN THE TRANSLATION SCALE** (motif edge 0.618034, diameter 2.0):

  | t | nn distance | z = 12 fraction | max hole |
  |---|---|---|---|
  | φ (overlapping) | 0.381966 | 0.000 | 0.363 |
  | φ² (just touching) | 0.618034 | 0.000 | 0.588 |
  | 2φ (separated) | 0.381966 | 0.000 | 0.853 |
  | 4.0 (well separated) | 0.618034 | **0.741** | **1.280** |

  **Dense enough to tile ⇒ vertices land closer than the motif edge ⇒ the nearest shell is no longer the
  motif's twelve. Sparse enough to preserve z = 12 ⇒ holes twice the edge length ⇒ it does not tile.**
- **⇒ For translation sets drawn from the motif's own vertex directions, NO scale both tiles and
  preserves z = 12.** SR-1's *"overlapping … tile flat ℝ⁴"* and SM's *exactly twelve at the edge
  distance* pull against each other, **and the pull is geometric, not a matter of choosing well.**
- **SCOPED, not overclaimed:** only translation sets from the motif's own vertex directions were tested.
  A general translation set could differ and nothing here rules one out. **Lane: EW.**
- **ONE VALUE RECORDED:** at **t = φ²** a single translated pair touches **exactly** at the edge —
  0.618033989 vs 0.618033989. The full union still coincides (pairs *between* different translates do not
  respect the single-pair condition), but the value is exact. **Lane: EW / SR.**
- **SO THE FOUNDER QUESTION IS SHARPER THAN 4033's: not "specify the construction" but WHICH DOES THE
  SUBSTRATE GIVE UP — overlap/tiling, or exactly-twelve?** Both load-bearing: *overlapping … tile flat
  ℝ⁴* is SR-1's wording and its figure's caption; z = 12 is SS-1/SM-1/SM-7/SM-8/SM-9/SF-4, with SF-4
  carrying Σm_ν ∝ z⁻⁹. **Lane: founder / SR / SM.**

---

### TODO-4035-EW — 4034's caveat closed, and the dilemma has a THIRD horn the DM lane already uses

- **4034's CAVEAT IS CLOSED.** For z = 12 *exactly* at a vertex, no other copy's vertex may lie within e
  — its own motif already supplies twelve. **So copies cannot interpenetrate at the edge scale whatever
  the translation set, and the translation set drops out of the problem.**
- **AND MY DRAFT OF THE NEXT STEP WAS WRONG.** Draft: *so it reproduces the 600-cell's local structure,
  which carries the 7.356° deficit, so flat space forbids it.* **False — FCC is the counterexample:**
  z = 12 exactly at every interior site, largest hole 0.961 against nn 1.414, **it tiles.** Caught by
  asking for a counterexample before asserting.
- **THE OBSTRUCTION IS "ICOSAHEDRALLY", NOT "TWELVE".** FCC shares **six** neighbours per edge — 4
  tetrahedra + 4 octahedra, closing 360° exactly — where the 600-cell shares **five**, giving 352.644°
  and the 7.356° deficit. FCC's coordination is **cuboctahedral** (cos-angles −1, −0.5, 0, +0.5) against
  the icosahedron's (−1, −0.4472, +0.4472). **SF-4's own words are "12 nearest neighbors arranged
  icosahedrally" — that adjective is doing all the work.**
- **SO THE DILEMMA IS THREE-WAY, NOT TWO:**
  **(A)** give up **tiling** — keep icosahedral z = 12, accept holes or curvature.
  **(B)** give up **exactly-twelve** — accept the quasicrystal's 13/18/19/26 spread.
  **(C)** give up **icosahedral** — keep twelve **and** tiling. **That is FCC/HCP.**
- **(C) IS NOT HYPOTHETICAL — IT IS WHAT THE DM LANE ALREADY RUNS ON.** Patch 2685's four z = 12 arenas
  are FCC ball, HCP ball, random-stacking Barlow ball and FCC-cubic; Patch 3133's sub-PSR cascade is an
  FCC lattice. Both were labelled **proxies** (found at 4012 and 4020 and filed as precedent). **(C)
  explains why those proxies worked: they satisfy the constraint that is actually satisfiable in flat
  space.**
- **(C)'s COST IS THE ADJECTIVE.** SF-4, SM-1 and SS-1 all say **icosahedral**. **Whether the mass ladder
  needs the ARRANGEMENT or only the COUNT is a question about the SM papers' derivations — 4016 showed
  only the COUNT enters Σm_ν ∝ z⁻⁹. NOT decided here. Lane: SM / SF / founder.**

---

### TODO-4036-EW — I priced horn (C) and had it backwards; all three horns are expensive

- **4035 said "(C) costs a word." WITHDRAWN.** It was the cheapest-looking horn precisely because I had
  not priced it.
- **SM's particle cages are the taxonomy, not decoration.** SM-2's mass breakdown distinguishes particles
  **by cage** (tetra / icosa / dodeca), and Capotauro puts the W⁰ ring on the Petrie hexagon of the
  first-shell **icosahedron**. If the substrate is FCC, the cages must still be exact lattice
  configurations — or the taxonomy that assigns masses has no exact referent.
- **AND THEY CANNOT BE. The icosahedral group is not crystallographic.** A 5-fold rotation has trace
  1 + 2cos 72° = **φ — irrational**; trace is basis-independent, so no 5-fold rotation lies in GL(3,ℤ).
  **No lattice — FCC, HCP or any other — carries a regular icosahedron as an exact vertex configuration.**
  *(Same argument shape as 4018's H₄-is-not-crystallographic, one dimension down.)*
- **MEASURED, not asserted:** best regular icosahedron on FCC sites over **3000 orientations × 40 scales**
  gives RMS vertex error **0.327** against an FCC nn of 1.414 — **23% of the nearest-neighbour distance.**
  *(A sampling bound, not a proven optimum; the true best could be lower.)*
- **AND THAT EXCEEDS THE FOUNDER'S 4020 RULING.** He allowed the cage to be *"slightly distorted, just
  like materials with icosahedral packing"* — real icosahedral matter distorts by a **few percent**. This
  is ~23%, an order of magnitude more. **(C) would need a new and much larger ruling. Lane: founder.**
- **THE THREE HORNS, PRICED:** **(A)** holes, or curvature — and curvature costs **z = ∞** (4017), against
  SR-1's own wording. **(B)** z spreads to 13/18/19/26; SF-4's Σm_ν ∝ z⁻⁹ has no integer to stand on
  (4016). **(C)** the cages go ~23% distorted; SM-2's taxonomy loses its exact referent.
  **ALL THREE ARE EXPENSIVE — there is no free choice, and the decision is a physics one. Lane: founder.**
- **AND THE DM PROXIES ARE NOT THEREBY VINDICATED AS THE SUBSTRATE.** 4035 said they *sit on the
  survivable horn*; they survive the **coordination** constraint and pay on the **cage** one. They remain
  what their author called them: **proxies**. **Lane: DM — noted, nothing owed.**

---

### TODO-4037-EW — the founder's question: what is most likely wrong? An audit, not an opinion

- **HIS ARGUMENT:** the masses predict accurately, so they are probably right, and the wrong thing is
  elsewhere. **I agree the masses are probably right. But the inference "masses work ⇒ the geometry is
  right" does not go through, and the reason is measurable.**
- **THE STRONGEST MASS PREDICTION USES NO ICOSAHEDRAL GEOMETRY.** *"icosahedr"* appears **0 times in
  SF-1**, 2 in SF-3, 22 in SF-4, 12 in SM-2. **SF-1 is the cleanest prediction the programme has** —
  Koide K = 2/3, θ = 132.731°, m_μ and m_τ, from **one calibration (m_e) and zero shape parameters** — and
  its geometry is a **three-vertex colour triangle**, with the leptons as *"stationary occupation patterns
  of a single three-vertex colour cage."* **A triangle embeds in any lattice; 4036's crystallographic
  obstruction does not touch it.**
- **AND THE TABLE THAT DOES USE THE CAGES COMPUTES NOTHING.** 4002: SM-2's Mass Contribution Breakdown is
  a **fixed-fraction partition of the calibrated PDG total** with a residual closing the sum — all twelve
  rows. **The cage column labels rows; it does not generate numbers. So SM-2's table cannot be evidence
  for the cage taxonomy.**
- **⇒ THE MASS SUCCESSES AND THE ICOSAHEDRAL COMMITMENT ARE LARGELY DISJOINT.** SF-4 does use z, but 4016
  showed **only the COUNT enters** (M₀ ∝ z, σ_ν ∝ z⁻¹⁰), not the arrangement.
- **WHAT I THINK IS MOST LIKELY WRONG — a hypothesis, not a finding:** not the masses, not the axioms,
  **the GLOBAL LATTICE CONSTRUCTION — and it is most likely wrong because nothing in the mass sector ever
  needed it.** Everything load-bearing in SM is **local**: a three-vertex triangle (SF-1), a count of
  twelve (SF-4), a first-shell distance ratio (Capotauro/CHI-1). **None requires a global 600-cell tiling
  of flat ℝ⁴.** That is also why 4033 found it unspecified: **an unused commitment never gets pinned
  down.**
- **MEANWHILE SR-1 DOES need the global structure** — its W2 world-call rests on the substrate's symmetry
  **class**. **So the conflict this arc has chased is between SR's GLOBAL commitment and SM's LOCAL ones,
  and the local ones are satisfiable in many global structures.**
- **CHECKABLE PREDICTION, NOT YET TESTED:** no SM result changes if the global tiling is replaced,
  provided the local structures survive. **Lane: EW — test it.**

---

### TODO-4038-EW — the alternative is not a different lattice: it is icosahedral symmetry with the reflections dropped

- **A NEW COST ON HORN (C), which 4036 did not price: FCC/HCP cannot replace the 600-cell for SR.**
  Independent elastic constants: **cubic 3, icosahedral 2.** Isotropy has two. **A cubic substrate is
  anisotropic at rank 4 and loses SR's W2 world-call.**
- **AND THE ANSWER: drop the improper operations, keep the rotations — point group I (532), not I_h.**
  **I (order 60, chiral) and I_h (order 120) give the SAME elastic count — 2 and 2** — because elasticity
  is a rank-4 **even** tensor property and improper operations contribute nothing to it. **SR loses
  exactly nothing.** The same holds for the **l = 6 anisotropy floor**, also even-rank.
- **AND I HAS NO IMPROPER OPERATIONS — which is precisely what the cancellation needs.** 4011, 4012,
  4015, 4020 and 4024 all rest on one thing: an improper symmetry fixing n̂, so every path has an exact
  mirror partner. **In point group I there is no such operation and the cancellation is no longer forced.**
- **AND SM KEEPS EVERYTHING IT USES:** z = 12, the three-vertex triangle, the first-shell ratio — all
  rotation-invariant (4037). **Dropping reflections costs the mass sector nothing.**
- **NOT BUILT. Three attempts recorded rather than hidden:** close-packed polytypes (ABC, AB, ABAC,
  ABCACB, ABCB, ABCBAC, ABCACBACB) — **z = 12 exactly and chirality sum exactly 0 in every one**, so
  swapping inside the z = 12 close-packing family does not buy chirality; a **golden-angle screw** — chiral
  but **z falls to 6–10**; the **snub-24-cell attempt** (96 non-24-cell vertices) — **z = 9 and still 96
  improper signed-permutation symmetries.**
- **THE TARGET, stated:** a point set in flat space with icosahedral **rotation** symmetry I (532), **no**
  improper operations, and a nearest-neighbour shell of **exactly twelve**. **Chiral icosahedral
  quasicrystals occur in nature** — a known structure class, which is a better place to be than the
  unspecified family 4033 found. **Lane: EW — build it.**
- **FI-C-9 = V3 still stands.** Nothing here generates chirality yet; it removes the obstruction that
  forbade it.

---

### TODO-4039-EW — fourth attempt at the chiral target: fails, with a diagnosis that sharpens it

- **ATTEMPT:** decorate each of the 600 tetrahedral cells with a signed radial offset, the sign from the
  cell's vertex determinant. **Keep the rotations, break the mirrors.**
- **IT KILLS THE MIRRORS — improper symmetries go 96 → 0** at every ε. **AND THE ROTATIONS WITH THEM:
  proper go 96 → 1.** The decoration is not rotation-equivariant, so it realises **neither** I_h nor I.
- **AND THE CHIRALITY IS NOT SYSTEMATIC, which confirms it.** Sums at ε = −0.10, −0.05, +0.05, +0.10 are
  **+8, +35, +5, +8** — **the sign does not flip with ε.** A genuine chiral decoration is its own mirror
  image under ε → −ε, so the sum **must** flip. It does not: what is measured is the arbitrariness of the
  decoration, not a handedness.
- **THE DIAGNOSIS:** the per-cell sign used `det[V_i, V_a, V_b, V_c]` in **index order**, which is not a
  geometric property of the cell — a rotation permutes cells without carrying the labelling, so the sign
  is assigned inconsistently. **And no better ordering fixes it, because A REGULAR TETRAHEDRON IS
  ACHIRAL** (12 improper symmetries of its own, verified). **There is no per-cell handedness to decorate
  with.**
- **SO THE TARGET IS SHARPER: the decoration must be built on a motif that is ITSELF handed.** Natural
  candidate in the 600-cell: **the ring of FIVE tetrahedra around an edge** — five is odd, a cyclic ring
  of five admits two traversal senses, and it is the same five whose 352.644° leaves the **7.356° deficit**
  (4019). **NOT tested. Lane: EW.**
- **Fourth failed attempt at 4038's target — and the first with a diagnosis rather than a shrug.**

---

### TODO-4040-EW — 4039's edge-ring tested; and the whole DECORATION method closes

- **THE RING IS REAL:** five cells around each edge, centroids forming a regular pentagon (radii equal to
  1e-9). 4039's expectation was right about the geometry.
- **BUT ITS TRAVERSAL SENSE IS NOT A PER-EDGE INVARIANT.** Computed by a nearest-neighbour walk it splits
  **358 / 362** across the 720 edges — an almost even split, which is **the signature of an arbitrary
  tie-break**: from any pentagon vertex **two** neighbours are equidistant and the walk broke the tie by
  index. **Fifth instance today of: a quantity defined by an arbitrary choice among equals is not a
  quantity.** Done properly — orient the ring's 2-plane from (d, m) and the ambient ℝ⁴ orientation and read
  the cyclic order off *that* — the sense is **fixed by construction**, hence constant, hence carries **no
  per-edge information**. Either way the ring supplies nothing to decorate with.
- **AND THE REASON GENERALISES — THE WHOLE DECORATION APPROACH CLOSES.** The 600-cell is **regular**, so
  its symmetry group is transitive on flags and therefore on vertices, edges, faces and cells separately
  (verified: all 120 vertices at one radius, all 720 edge midpoints at one radius). **A rotation-equivariant
  assignment is therefore CONSTANT across each orbit — and a constant carries no handedness.**
  **⇒ no local decoration of the 600-cell can be chiral.** 4039 failed on cells, 4040 on edges, and
  vertex-transitivity closes the third. **Not three unlucky attempts — regularity.**
- **SO THE CHIRALITY MUST BREAK THE TRANSITIVITY.** 4038's target stands, but **it cannot be reached by
  decorating the 600-cell.** The structure must have symmetry **I from the start**, not H₄ with something
  added. In 3D that is a **chiral icosahedral quasicrystal**, which exists; the 4D analogue is what would
  have to be built. **Lane: EW.**
- **Five attempts at 4038's target now:** close-packings (achiral), golden screw (loses z = 12),
  snub-24 attempt (z = 9), cell decoration (kills the rotations), edge-ring (no invariant). **The last two
  fail for one reason, now named.**

---

### TODO-4041-EW — a BORN-CHIRAL cluster, built and proved; and two failed measurements

- **THE IDEA:** a regular icosahedron is **achiral** (60 improper symmetries of its own), so **z = 12
  icosahedral forces an achiral first shell** whatever the rest does. **Chirality must live in the second
  shell** — and a **generic** point has a **60**-point orbit under I where it would have **120** under I_h,
  so a 60-point orbit **cannot** be closed under any improper operation.
- **BUILT: icosahedron (12) + generic I-orbit (60) = 72 points. Proper symmetries 60, IMPROPER 0.** Every
  control gives 60 improper (12 + 5-fold orbit, 12 + 3-fold orbit, icosahedron alone). **This is 4038's
  target realised at cluster scale — the first object in this arc that is actually chiral with the right
  rotation group.**
- **SCOPE OF THE PROOF, stated:** the search covers I_h's improper coset {−R : R ∈ I}. **Sufficient** — a
  point group containing I plus any improper element has order ≥ 120, and the only finite point group
  containing I at index 2 is I_h. **Zero here means genuinely no improper symmetry.**
- **TWO ATTEMPTS TO MEASURE *how* chiral, both FAILED, both reported.** (i) The 3-hop path estimator that
  worked on the 600-cell has only **~240 paths** here — nn = 0.638 with shell 2 at 1.9 makes the
  nearest-neighbour graph too sparse. **It returned 0 for lack of paths, not lack of chirality.** (ii) A
  continuous chirality measure by random rotation search **floors at ~0.03 for the chiral cluster AND for
  the exactly-achiral control** — sampling-limited, not measuring. **It needs local optimisation seeded
  from the group elements. NOT DONE.**
- **NOT ACHIEVED: a lattice.** This is a 72-point **cluster**. Extending it to a space-filling structure
  while keeping z = 12 at every point is the remaining work, **and 4034's trichotomy says that step is
  where the difficulty lives.** **Lane: EW.**
- **NOT ACHIEVED: a quantified chirality.** The group count proves chirality; it does not say **how much**,
  and "how much" is what a physical prediction would need. **Lane: EW.**
- **FI-C-9 = V3 STANDS.** This removes an obstruction and builds a candidate; **it does not derive a
  handedness.**

---

### TODO-4042-EW — 4041's owed measurement discharged, and it closes a loop back to 4021

- **THE FIX, one line of reasoning:** 4041 sampled 4000 **random** rotations and floored at ~0.03 for
  everything, including exactly-achiral sets. But an achiral set's improper symmetry **is** −R for some
  R ∈ I — so **seed the search from the 60 group elements** and it lands on it exactly instead of near it.
  Then refine locally.
- **RESULT: all three achiral controls score EXACTLY 0.00000000**; the chiral cluster scores **0.01173**.
  **4041's owed measurement is discharged.**
- **VALIDATED:** CCM → 0 **linearly** as the seed approaches a 5-fold axis — CCM/offset converges to
  **0.5012** (0.414, 0.491, 0.499, 0.5009, 0.5012, 0.5012) — and is **exactly 0** at the axis, where the
  orbit collapses from 60 points to 12. *(A draft check tested consecutive ratios for a factor of 2 and
  FAILED, because the offsets do not all halve. The data was linear; the check was mis-specified.)*
- **AND THE ANSWER IS A RANGE, NOT A NUMBER: the chirality is TUNABLE over 0.012–0.187** across generic
  seeds. The second shell's position is a **continuous** parameter, so the structure admits a continuum of
  chirality strengths. **⇒ SYMMETRY PERMITS CHIRALITY; IT DOES NOT DETERMINE THE MAGNITUDE — and a
  magnitude is what any physical prediction would need.**
- **WHICH CLOSES A LOOP BACK TO 4021.** 4021 showed a strain functional built from **distances** cannot
  prefer a handedness, and that a mechanism needs **(i)** an achirality-breaking term in the dynamics or
  **(ii)** an external bias. **4042 now shows the geometry supplies a continuum of handedness strengths
  with no preference among them — so what would select one is exactly what 4021 named.** Twenty-one
  patches apart, from opposite directions: 4021 from the energetics, 4042 from the geometry. **Not a new
  result — a convergence, and it says the remaining gap is an AXIOM question, not a construction one.**
  **Lane: founder.**
- **FI-C-9 = V3 STILL STANDS.** A substrate that permits any handedness equally does not predict a definite
  δ_CP — the same objection 4020 raised against random strain.

---

### TODO-4043-EW — can the rest of CPP be derived from the chiral lattice? A qualified YES

- **THE AUDIT FIRST.** Dodecahedral-shell mentions: **SF-4 20, SF-3 5, SM-2 5, SR-1 4, SF-1 ZERO.**
  **SF-1 — the cleanest prediction in the programme — reaches no further than shell 1.** A lattice that
  destroyed the dodecahedral shell would cost the **neutrino sector** most.
  *(A draft of this check asserted "SF-4 and SR-1 both use the second shell heavily" and FAILED on SR-1 —
  the claim came from my own misread of my own column headers in an exploratory grep; SR-1 mentions the
  second shell **zero** times.)*
- **AND IT NEED NOT COST THEM. SHELLS AT DIFFERENT RADII ARE INDEPENDENT.** Built: shell 1 icosahedron
  (12, r = 1.00), shell 2 dodecahedron (20, r = 1.62), shell 3 generic I-orbit (60, r = 2.40).
  **S1 alone: improper 60, CCM 0. S1+S2: improper 60, CCM 0. S1+S2+S3: improper 0, CCM 0.0112.**
  **⇒ the icosahedral and dodecahedral shells survive intact and the chirality is carried by a THIRD shell
  that no CPP derivation references.**
- **THREE QUALIFICATIONS, none of them small.** **(1)** Still a **cluster**, not a lattice — 4034's
  trichotomy is untouched and the extension problem is exactly where it was. **(2)** The third shell is a
  **new postulate**, not a free consequence: the claim is that the change is **additive** — nothing
  existing breaks — not that nothing is added. **(3)** The magnitude is **still free** (4042: 0.012–0.187).
  Chirality becomes a **structural parameter** rather than an unexplained sign, which is progress — **but a
  parameter is not a prediction until one calibration buys more than one number**, the standard SF-1
  already meets.
- **AND WHERE IT WOULD BECOME PHYSICS.** SR-1's dispersion machinery **sums over shells** (R4: *finite
  shells suppress the icosahedral anisotropy tower one harmonic at a time but never zero it*). **A chiral
  shell contributes PARITY-ODD terms to those sums**, where every shell CPP currently has contributes only
  parity-even ones. **A parity-odd term in the vacuum dispersion is optical activity of the vacuum — an
  observable, not a parameter.** If the chirality strength sets its size, it is calibratable once and
  predictive thereafter. **That is the test of whether the reframe is explanatory or merely consistent.
  NOT COMPUTED. Lane: EW / SR — next.**

---

### TODO-4044-EW — the parity-odd term computed: real, O(k¹⁵), and it calibrates nothing

- **THE MECHANISM:** the icosahedron and dodecahedron are **centrally symmetric**, so
  Im[Σ_v e^{ik·v}] = Σ_v sin(k·v) vanishes **identically** for both. **The chiral 60-shell is not**, so it
  need not vanish. **That is the parity-odd channel.**
- **AND IT IS REAL.** Against two achiral controls that stay at **~1e-16** at every k, the chiral shell's
  |Im| rises to **7.86e-06 at k = 6**. The channel is open.
- **ITS ORDER IS k¹⁵, AND THAT WAS PREDICTED BEFORE MEASURING.** Icosahedral invariant degrees are
  **2, 6, 10, 15**, and the degree-15 invariant is the **pseudo**-invariant — even under the rotation
  group I, **odd** under reflection. Measured log-log slopes: **14.53, 14.84, 14.77, 14.63, 14.38, 14.06**,
  trending monotonically to 15 as k falls; the shortfall at large k is higher-order sine terms.
- **AT k ~ 1 THE TERM IS BELOW DOUBLE PRECISION.** An earlier run at k = 0.4–0.9 gave ~3e-15 scaling as
  **k¹** — float noise, not signal. Recorded because reading that as a measurement would have been the
  error this session has spent all day cataloguing.
- **WHAT IT MEANS. A chiral substrate DOES make the vacuum optically active** — the prediction is definite
  in form. **But it enters at (k·a)¹⁵**, so at any accessible k it is suppressed beyond conceivable
  measurement, far worse even than SR's l = 6 floor at ~l_P/10³⁰.
- **RISK RETIRED:** the chiral substrate is **not excluded** by the absence of observed vacuum optical
  activity. That was a live risk when 4043 proposed the test — a chiral vacuum could have been ruled out on
  the spot. It is not.
- **BUT 4043's CALIBRATION HOPE FAILS.** 4043 hoped the chirality strength would set the size of an
  **observable** and so become calibratable. **The observable is unobservable, so it calibrates nothing.**
  4042's free magnitude remains free, chirality is still a **structural parameter rather than a
  prediction**, and **the route 4043 proposed to promote it is now closed. A different observable would be
  needed and none is named. Lane: EW / SR.**

---

### TODO-4045-EW — the escape route from k¹⁵ tested and CLOSED; 4044 hardened

- **THE HYPOTHESIS, and it was a good one.** 4044's O(k¹⁵) assumed **full** icosahedral symmetry. CPP's
  substrate has a preferred direction **n̂** (Mechanism A's drive), which reduces I to the stabiliser of n̂
  — **and lower symmetry permits lower-degree invariants.** If so, the parity-odd term is lifted out of its
  k¹⁵ grave.
- **AND IT IS LIFTED — BY FOURTEEN ORDERS.** With δ ≠ 0 the parity-odd term is **O(k¹)**, measured slope
  1.00 across k = 0.05–0.40.
- **BUT IT IS NOT THE CHIRALITY.** Per-point parity-odd amplitude at k = 0.05, δ = 0.10:
  **chiral 60-shell 8.847293e-04, icosahedron 8.847293e-04, dodecahedron 8.847293e-04 — identical to
  seven significant figures.** The chiral shell's larger total is **entirely its larger point count.**
  **The term is the DRIVE's asymmetry, not the shell's handedness** — the weight (1 + δ·v̂·n̂) is itself not
  centrally symmetric, and that is all this measures.
- **And at δ = 0 the chiral shell returns to machine noise** (2.4e-16 rising as k¹ — float noise, exactly
  as 4044 found). **The chirality's own term is still at k¹⁵.**
- **SO THE ROUTE IS CLOSED AND 4044 IS HARDENED, NOT WEAKENED.** Any observable built on the tilted
  dispersion measures **δ**, not chirality. Isolating the chirality means subtracting the achiral
  contribution exactly — and once subtracted, what remains is back at O(k¹⁵). **The k¹⁵ suppression is
  robust against the substrate's own preferred direction**, which was the most plausible escape available
  and the one I would have reached for next.
- **NOT claimed: that no observable exists.** One route tested and closed; the space is not enumerated.
  **Chirality remains a structural parameter, with one candidate now eliminated rather than merely
  unexplored. Lane: EW / SR.**

---

### TODO-4046-EW — the arc lands on a NAMED SHIPPED open problem, whose leading candidate is refuted

- **SEARCHED UNSCOPED.** SF-6 (shipped flagship, electromagnetism) carries **`OPEN-SD-CHIR-PRIMITIVE`**:
  *"Derive the universe's primitive chirality bias from a single substrate-level mechanism"* — **and names
  its current leading candidate: a primitive 4D direction n̂ aligned with a 600-cell HOST VERTEX.**
- **THE TARGET IS PARITY VIOLATION, WHICH IS P-ODD — AND GEOMETRIC CHIRALITY IS P-ODD. The kinds match.**
  SF-6's companion `OPEN-FP-6-EMHAND` is *the entry of substrate chirality into electromagnetic
  phenomenology*; SF-2's `OPEN-FP-SF-2-CHIR` is *chirality emergence in W bracelet structure (V−A
  coupling)*. A P-odd target needs a P-odd source.
- **BUT THE LEADING CANDIDATE CANNOT WORK, AND THIS SESSION PROVED IT FIVE TIMES WITHOUT SAYING SO.**
  **A vector is not a chirality**: n̂ is P-odd, but reflection in any plane **containing** n̂ leaves it
  invariant. Verified — **Θ = diag(1,1,1,−1) maps the 600-cell to itself with det = −1 and fixes n̂
  exactly (|Θn − n| = 0.0)**, so the pair (600-cell, n̂) is invariant under an improper isometry and **the
  configuration is achiral.** That Θ **is** the map 4011, 4012, 4015, 4020 and 4024 all used. **Those five
  patches are not five confirmations of V3 — they are five demonstrations that SF-6's leading candidate
  supplies no chirality.**
- **AND THE CHIRAL LATTICE IS EXACTLY THE REPLACEMENT.** 4041's cluster has **no improper symmetry at
  all** — there is no Θ to fix n̂ because there is no Θ. **The construction removes precisely what the
  leading candidate leaves intact.** **The arc 4038–4045 is a candidate answer to a named, shipped open
  problem — it was not looking for it; it walked into it.**
- **STILL OWED, unchanged by the renaming:** a **lattice** rather than a 72-point cluster (4034's
  trichotomy untouched); a **magnitude** (4042: free, 0.012–0.187); an **observable** that fixes it (k¹⁵
  route closed at 4044, n̂-tilt route closed at 4045); and a **derivation of V−A** from the handedness,
  which is SF-2's `OPEN-FP-SF-2-CHIR` and is untouched here. **Lane: CHIR / EW.**
- **NOT CLAIMED: that the chiral lattice SOLVES OPEN-SD-CHIR-PRIMITIVE.** It is a candidate that survives
  the tests the previous candidate fails. **A real change of status, and not a closure.**

---

### TODO-4047-EW — the first nonzero path-chirality in the arc, and the first chiral LAW

- **GRAPH HELICITY:** Σ sign det[u₁,u₂,u₃] over 3-hop nearest-neighbour paths. On an achiral set every
  path has an exact mirror partner, so it is identically zero.
  **ACHIRAL S1+S2: exactly 0 at every cutoff (1.15, 1.30, 1.50).**
  **CHIRAL S1+S2+S3: −60 at cut 1.30 (19,740 paths), −120 at cut 1.50 (136,680 paths).**
- **The first nonzero path-chirality in this arc.** 4011, 4012, 4015 and 4041 all returned exact zeros —
  and 4041's was zero **for lack of paths**. **Magnitudes are multiples of 60 = |I|**: one group orbit's
  worth of net handedness.
- **VALIDATED: the mirror gives the exact opposite** — +60 and +120, sums **exactly zero** at both cutoffs.
- **AND THIS IS THE DIFFERENCE FROM 4020, WHICH IS THE WHOLE POINT.** 4020 strained the 600-cell and found
  every realisation chiral and the **ensemble** not — a chiral *object*, not a chiral *law*, which is why
  it supplied no mechanism. **Here the handedness is a FIXED PROPERTY OF THE STRUCTURE**: the same value
  every time, flipping only under reflection. **The first thing in this arc to clear the bar 4020 set and
  4021 restated.**
- **WHAT IT IS NOT.** The sign **and** magnitude depend on the seed (**+600, −360, −120**), consistent with
  4042 — the handedness remains a **free structural parameter**; nature picks one, the theory does not yet
  say which. **And it is NOT a derivation of V−A:** it shows the substrate has a definite handedness that
  **propagating paths can see** — the structural ingredient spin-momentum locking needs. **Connecting it
  to the weak coupling is SF-2's `OPEN-FP-SF-2-CHIR` and is untouched. Lane: CHIR / SF-2.**
- **It also discharges 4041's failed path measurement a second way** — 4042 fixed the chirality measure,
  this supplies the path graph 4041 lacked. **Both now agree the cluster is chiral.**

---

### TODO-4048-EW — a structural helicity bias cannot deliver V−A, and where the labour probably divides

- **WHAT V−A DEMANDS:** *maximal* parity violation — the right-handed coupling is **exactly zero**, not
  merely smaller. A structural helicity bias gives a **fraction** of paths curling one way.
- **MEASURED OVER 24 CONFIGURATIONS** (6 seeds × 2 radii × 2 cutoffs): **largest fractional helicity
  2.069%.** V−A requires **100%**. A factor of ~50 short, **and it does not trend toward 1 in any
  direction tried.**
- **AND THE REASON IS STRUCTURAL, NOT A MATTER OF SEARCHING HARDER.** The inner two shells contribute
  **exactly zero** (+0 over 10,320 paths) — because **4041: the icosahedron is achiral and z = 12
  icosahedral FORCES it to be**, so every short path cancels exactly. The helicity can live only in the
  **longer** paths reaching the outer shell, a small minority of the count. **The 2% is the ratio of chiral
  to total paths in a structure whose core is forced achiral.**
- **⇒ A STRUCTURAL HELICITY BIAS OF THIS KIND CANNOT DELIVER V−A.** A real negative on the most direct
  route from the chiral lattice to the weak coupling.
- **BUT IT MAY BE THE RIGHT DIVISION OF LABOUR.** In the Standard Model, V−A's **maximality does not come
  from a statistical bias either** — it comes from the **gauge structure**, SU(2)_L acting on left doublets
  and not right singlets, by construction. Nothing counts paths. **So the substrate would supply the SIGN
  — which handedness — and the W bracelet the MAXIMALITY.** That matches SF-2's own framing: its open
  problem is *chirality emergence in the W bracelet structure*, not *chirality from the substrate alone*.
  And 4047 showed the chiral lattice is well-suited to supplying a sign — a fixed property of the
  structure, flipping only under reflection.
- **NOT CLAIMED: that the division works.** A hypothesis about where the labour divides; **SF-2 owns the
  bracelet side and nothing here touches it.** What **is** established: **the substrate side cannot carry
  the maximality, so if the division fails, the route fails. Lane: CHIR / SF-2.**

---

### TODO-4049-EW — my own division of labour, one patch old, fails on the bracelet side

- **THE CORPUS'S OWN THEOREM ALREADY SAID IT.** SF-2 Theorem 4.2: *the 4800 induced 6-cycles partition
  into exactly 2 H₄-orbits; one orbit (size 1200, **stabilizer D₆ of order 12**) is the W bracelet.*
  **D₆ of order 12 is the dihedral group — 6 rotations AND 6 reflections. A stabilizer containing
  reflections means the object is ACHIRAL.** The corpus says so in its own theorem and I had not read it
  that way.
- **AND AN INDEPENDENT COMPUTATION AGREES.** 63 induced 6-cycles through one vertex; a skew hexagon is a
  helix (chiral) only if all six torsion signs agree. **No cycle is a helix; every pattern is
  reversal-negation symmetric** — (1,0,−1,1,0,−1), (−1,1,−1,1,−1,1), and so on. **The scaffold offers no
  two handedness states to select between: there are not two mirror-image bracelets, there is one and it
  is its own mirror image.**
- **METHOD NOTE: my first test said the opposite.** Searching the signed-permutation subgroup found **0
  improper symmetries** and would have read as CHIRAL — but that subgroup is 192 of H₄'s 14400, and it
  also found only **1 proper** symmetry, which should have been the tell. **The torsion pattern is the
  right instrument for a skew polygon.** Sixth time today an instrument returned a confidently wrong
  answer, and the second time the giveaway was a **control** coming out wrong rather than the result.
- **SO 4048's DIVISION OF LABOUR FAILS ON THE BRACELET SIDE AS CURRENTLY DESCRIBED.** I proposed it one
  patch ago as the constructive reading of a negative; **it does not survive its own test.** And the
  corpus's W *state* supplies nothing either — the bracelet is a **catalyst**, activated by charge capture
  at its **D₆-symmetric centroid**, which is achiral too.
- **WHAT THE BRACELET WOULD NEED — the actionable residue:** a **binary, P-odd, two-state degree of
  freedom on the ring** — a **circulation**, a **winding**, or a **traversal orientation**. Such a thing is
  all-or-nothing, which is exactly the maximality V−A wants, and exactly what a 2% substrate sign could
  select between. **Not present in the current description. A specific, nameable gap on SF-2's side — far
  more actionable than "derive V−A". Lane: SF-2 / CHIR. NOT this lane's to fill.**

---

### TODO-4050-EW — 4049's request was mis-specified; the right object already exists in the corpus

- **4049 ASKED FOR THE WRONG THING, one patch old.** It requested *a binary, P-odd, two-state degree of
  freedom **on the ring***, and suggested a circulation. **A circulation is P-EVEN** — an axial vector,
  like a magnetic moment; parity leaves it alone. **It cannot be what a P-odd substrate sign selects.**
- **THE RIGHT OBJECT IS THE RING TOGETHER WITH n̂, AND BOTH ALREADY EXIST.** (axial)·(polar) =
  **pseudoscalar**. The ring supplies an oriented area bivector L; **n̂ is CPP's primitive 4D direction
  (FI-C-RC-1)**. Contract with the 4D Levi-Civita and the result is **P-odd by construction**.
- **COMPUTED:** all **63** induced 6-cycles through one vertex carry a **nonzero** helicity, magnitude
  **1/(2φ) = 0.309017** — φ-valued, like everything else here.
- **AND THE TWO STATES ARE EXCHANGED BY AN EXACT SYMMETRY OF THE PRESENT SETUP.** Under
  **Θ = diag(1,1,1,−1)**, which fixes n̂ and preserves the 600-cell, the helicity **flips for all 63 rings
  and is unchanged for none.** **⇒ the two states are EXACTLY DEGENERATE and nothing in the present setup
  prefers one.**
- **WHICH COMPLETES THE MECHANISM SKETCH, IN FORM:** achiral substrate → Θ exists → degenerate; **chiral
  substrate → no Θ → degeneracy broken**; and the variable is **binary** — sign(helicity) = ±1,
  all-or-nothing, **which is the maximality V−A wants and which a 2% bias can select between.**
- **4049's NEGATIVE BECOMES THE REQUIREMENT.** The bracelet's achirality is what **guarantees** exactly two
  degenerate states; a chiral bracelet would have split them geometrically, leaving nothing for the
  substrate to do.
- **NOT DONE — THE SPLITTING IS NOT COMPUTED.** This shows the two states exist, are P-odd, binary, and
  degenerate now. It does **not** show a chiral substrate splits them, nor by how much, nor with which
  sign. **Needs the bracelet embedded in the chiral environment. Lane: EW — next.**
- **And not claimed that this is how SF-2's bracelet works** — SF-2 describes a catalyst at a D₆-symmetric
  centroid, not a helicity state. **Whether the W state carries this variable is SF-2's to say.**

---

### TODO-4051-EW — the splitting is NOT computed; two functionals, two failures, both caught by controls

- **BUILT AND VERIFIED: a chiral 4D shell.** Left-icosian orbit of a generic 4D point, **120 points**,
  **Θ does not map it to itself** — chiral. Special-position control: 120 points, **Θ-invariant**. The two
  shells differ in exactly the property under test.
- **FUNCTIONAL 1 FAILS.** ⟨sign(h)·E⟩ = **−6.290156** on the chiral shell and **−6.290201** on the
  **achiral control** — the same to five digits. **The functional is not measuring the shell at all**; it
  is dominated by the ring's own helicity, since d = s − c carries a term ∝ −helicity. **The control
  caught it.**
- **FUNCTIONAL 2 FAILS TOO.** Differencing out the control leaves **+4.482936e-05** for the chiral shell
  and **+4.444575e-05** for the **mirrored** chiral shell — **the same sign, not the opposite.** A residual
  that is the shell's chirality must flip under mirroring. **It is a P-even difference between a
  generic-position and a special-position orbit, not the quantity wanted. The mirror caught it.**
- **SO THE SPLITTING IS NOT COMPUTED.** Two functionals, two failures, **both caught by controls rather
  than by inspection** — third and fourth time today. **The controls are doing more work than the
  measurements.**
- **LIKELY REASON, offered as a hypothesis with its evidence, NOT a finding:** summing a P-odd quantity
  over a **group orbit** gives a group invariant, and for icosahedral symmetry the first **odd** invariant
  is **degree 15** (4044). **The splitting may be suppressed for exactly the reason the parity-odd
  dispersion was** — and if so, **no low-order functional of this shape will ever see it. NOT TESTED.**
- **AND THIS IS WHERE THE LANE'S TOOLS STOP REACHING.** Two consecutive patches whose computation did not
  land. **4050's mechanism sketch stands in FORM** — two P-odd binary states, exactly degenerate,
  degeneracy removable by a chiral substrate — **and its MAGNITUDE is not accessible by the means available
  here. Lane: EW / CHIR — needs a different instrument, not more of this one.**

---

### TODO-4052-EW — 4051's hypothesis TESTED and REFUTED; the real reason is a fact about four dimensions

- **4051 guessed the splitting was suppressed by the degree-15 pseudo-invariant, as at 4044.** Prediction:
  Σ_s (s·k)^m vanishes for odd m < 15 and turns on at 15. **Tested: EVERY odd moment is at machine zero,
  m = 15 included.** Nothing turns on anywhere. **The hypothesis is refuted.**
- **THE REAL REASON.** The quaternion **−1 lies in 2I**, so left-multiplication by it is **L₍₋₁₎ = −I**,
  the inversion x → −x. **So the shell is CENTRALLY SYMMETRIC — and central symmetry kills every odd
  moment identically, at every order.**
- **AND YET THE SHELL IS STILL CHIRAL**, because **in four dimensions inversion is PROPER: det(−I₄) = +1**
  (against det(−I₃) = −1). **Central symmetry and chirality COEXIST in 4D, which they cannot in 3D.**
- **SO 4051's FUNCTIONALS WERE PROBING AN EMPTY CHANNEL.** Both reduce to **odd moments** of the shell —
  sums of f(s) with f odd under s → −s — which central symmetry annihilates whatever the chirality. **The
  failures were not suppression; they were a probe aimed at a channel that is identically zero.** This
  diagnosis **replaces** 4051's.
- **AND IT SPECIFIES THE NEXT FUNCTIONAL.** A P-odd scalar in 4D needs the **Levi-Civita contracted with
  four independent vectors**. **An odd moment of one vector cannot be P-odd in 4D at all** — that is a 3D
  intuition carried across, and it is where both of 4051's functionals came from. **4050's ring helicity
  ε(L, c, n̂) already has the right shape** — the bivector supplies two of the four slots — and is the one
  P-odd quantity in this arc that has worked in 4D. **A splitting functional needs the same form with the
  shell entering through a slot the inversion cannot cancel. NOT built here — the diagnosis is the
  deliverable, and the next step now has a specification instead of a guess. Lane: EW.**

---

### TODO-4053-EW — RETRACTION: 4051's "chiral 4D shell" was never chiral

- **THE INSTRUMENT 4052 SPECIFIED, BUILT.** 4D graph helicity — Σ sign det[u₁,u₂,u₃,u₄] over 4-hop paths;
  survives central symmetry ((−1)⁴ = +1), P-odd under reflection. **It returns exactly zero on 4051's
  "chiral" shell — and on the 600-cell — with IDENTICAL path counts (1,916,640). Identical path counts for
  two supposedly different objects is the tell.**
- **BECAUSE THEY ARE THE SAME OBJECT.** `L_q` applied to (1,0,0,0) returns the first **column** of `L_q`,
  which is **q itself** — so that orbit **is** the 120 icosians, i.e. the 600-cell. And left multiplication
  is an **isometry**, so **every** left-icosian orbit is a **congruent copy of the 600-cell** (distance
  spectra match exactly). **The 600-cell is achiral: H₄ contains reflections.**
- **4051's test was misread.** *"Θ does not map it to itself"* only showed the copy was **misaligned** with
  that particular reflection. **Misaligned is not chiral, and I read it as chiral.**
- **WITHDRAWN:** 4051's chiral 4D shell; 4051's splitting attempt (it was never probing a chiral
  environment, so its two failures say **nothing** about splitting); and 4052's central-symmetry diagnosis
  as *the reason the attempt failed* — **the attempt failed because there was no chirality present.**
- **4052's POSITIVE CONTENT SURVIVES:** inversion is proper in 4D (det(−I₄) = +1); central symmetry and
  chirality can coexist in 4D; a P-odd 4D scalar needs four Levi-Civita slots. **All true, all independent
  of the retracted object — and the instrument built from it works.**
- **THE REAL STATE, WORSE THAN I HAVE BEEN REPORTING: NO CHIRAL 4D STRUCTURE HAS EVER BEEN BUILT IN THIS
  ARC.** 4041's chiral cluster is **three**-dimensional, verified against 3D controls. The 4D analogue was
  attempted only at 4051 and is now retracted. **The bracelet, n̂ and the 600-cell all live in 4D.**
- **So 4050's mechanism sketch has no 4D chiral substrate to run on.** The two helicity states are real and
  exactly degenerate (4050 stands); **what would split them has not been constructed in the right
  dimension.**
- **THE REMAINING WORK, stated honestly:** build a **chiral 4D point set** — an orbit of a subgroup of
  H₄'s **rotation** half that is **not** an orbit of H₄ itself. **The left-icosian group is the wrong
  choice, because its orbits are congruent to the 600-cell. NOT attempted. Lane: EW.**

---

### TODO-4096-F3 — F3/F2 (strong and EM sector P-evenness): founder physics-picture question **ANSWERED Patch 4097** (registered Patch 4096, EW lane)

**Status: ANSWERED 18 Sep 2026, Patch 4097.**

**Founder's ruling (verbatim, filed at `founders_voice/4097_ruling_velocity_dp_arcs_not_intrinsic_to_cp.md`):**
*"the velocity of the particle is not something the CP carries intrinsically. The KE/momentum/inertia/velocity of a CP is carried by the DP arcs established during acceleration (see corpus under inertia/KE/DP arcs)."*

**Corpus pointer:** SF-6 §(Emission as ZBW-chain discharge), Patch 3202: DP-arc cohort established during acceleration carries the KE/momentum. Inertia sketch Patch 2496: "the CP itself carries no momentum and no kinetic energy — all must live in the sea [arcs]."

**Implication for F3 and F2 (worker inference from ruling):**
- v in b = sign(ω·v) is the direction of the DP arc cohort, not an intrinsic CP property.
- *Free particle:* DP arcs point persistently in the direction of travel (sustained by fore/aft SSV_net recapture). v_arcs well-defined → b ≠ 0 → bracelet reads a biased bit stream.
- *Confined quark:* confinement force continuously severs and re-establishes arcs in new directions (bremsstrahlung-like, SF-6). Net arc direction → 0 → ⟨b⟩ = 0 → strong force P-even.
- *EM sea DPs:* random arc orientations from last interactions → ⟨b_sea⟩ = 0 → EM P-even under Reading A.

**F3/F2 status after ruling:** upgraded from CONDITIONAL (no founder picture) to CONDITIONAL — founder-endorsed physical mechanism via DP arcs. **Formal derivation DELIVERED at Patch 4101** — F3 is now DERIVED conditional on R-F3 (arc cohort on cage bond directions), filed as TODO-4101-F3. F2 not discharged; see TODO-4101-F2. **Lane: EW.**

### TODO-4102-CKM65 — the 65.5° CKM signpost provenance audit — **DONE at Patch 4103** (registered Patch 4102, SM/EW lane)

**VERDICT: NO DERIVATION CHAIN; CIRCULAR REFERRAL.** SF-2 → Capotauro → SF-2. "Capotauro phase factor" occurs zero times in Capotauro. Full audit: `series_standard_model/axiom_maturation/4103_ckm65_provenance_audit.md`. Consequence: F5 is a missing mechanism, not a pending computation; H1 is not sufficient for it (a sign is not an angle).

**Why this exists.** In June 2026 the SF-2 external-validation campaign put δ_CP to a three-reviewer panel (ChatGPT / Grok / Copilot). **SQ1 returned 3/3: no derivation chain** for the 193.3° signpost — "empirical coincidence / back-calculation / signpost-only." Adjudicated RESTATEMENT-NEEDED at Patch 1202.

**That panel audited the PMNS signpost (193.3°) only.** The CKM value (65.5°) was never audited, yet it sits in the identical evidential position: SF-2 states δ_CP^(CKM) = arg(Capotauro phase factor) ≈ 65° as a "structural prediction," self-labels it "Conjectural (Phase 7 OPTIONAL)," and qualifies it — "matches at the ~1% level *if* the Capotauro phase factor closure proceeds as outlined." An unscoped corpus search confirms **arg(Capotauro phase factor) is never computed anywhere**.

**The task:** the same provenance audit Patch 1202 prescribed for 193.3° — exact source, formula, author/date, dependency chain for the ≈65°. Expected outcome by symmetry with the June finding: signpost-only. If so, F5's "O(1) phase near 65.5°" has no corpus provenance at all and the maturation document should say so.

**Why it matters now:** F5 is the one filter keeping χ₄ from panel-readiness. If the 65.5° target is signpost-only *and* F5 reduces to the H1 blocker (Patch 4102), then χ₄'s route to panel-readiness runs entirely through H1 and nothing else. That is worth knowing before any further F5 work. **Lane: SM/EW.**

### TODO-4119-CAPV21-REMAINDER — E4/E7 + the sibling-paper sweep, still owed (registered Patch 4119, CHIR lane)

Patch 4119 executed **E2** (|χ| renamed to *primitive anisotropy amplitude*, section + remark + 12 recurring occurrences), **E3** (sub-claim (a) retired as SUPERSEDED with reason, retained not deleted), **E5** (δ_CP/η_B referral withdrawn; "no candidate mechanism exists" recorded), and the E6 phrase sweep. LaTeX verified: whole-file brace balance unchanged from HEAD, all environments paired.

**Still owed:** **E4** the Q7 cosmological-nucleation scoping section (19 lines); **E7** the sub-claim architecture table and abstract restated as (a) superseded / (b) open / (c) shipped; **E6 remainder** the ~29 residual one-line mentions in capotauro.tex plus **14 pointer updates across 10 sibling papers** (theo_chir_audit_1, chirality_continuum, theo_chir_cap_1, theo_chir_chi_1, theo_chir_merge_1/2, theo_chir_tarrow_1, theo_chir_vw_1/2, dynamical_substrate_law). Bounded and mechanical. **Then** version-bump to v2.1 with changelog and recompile once (folds TODO-4104-CAPRECOMPILE). **Lane: CHIR.**

### TODO-4118-CAPV21 — the Capotauro v2.1 revision plan (registered Patch 4118, CHIR lane; E3–E7 gated on TODO-4116-CAPRETIRE)

**Founder asked whether the Capotauro papers need rewriting. Measured answer: NO — a v2.0 → v2.1 revision.** Audit of all 111 sections: real surgery is **119 lines of 2263 (5.3%)** in 7 sections, plus **41 scattered one-line edits** and **14 one-line pointer updates** across 10 sibling papers. **The flagship theorem section (`sec:composite_we`, |M| = χ/6) has ZERO affected hits** — THEO-CAP-1 and PRED-O-25/26/27/31 stand unchanged.

**E1** 4104 sign corrigendum — already in source, awaiting recompile. **E2** |χ| renaming (TODO-4117-CHIRENAME) — authorized now, follows from 4104, not contingent on the retirement. **E3–E5** retire sub-claim (a) and Q7 as *superseded notes with reasons*, not deletions; update falsifier/open-work/manifestation sections — **gated on the founder's ruling**. **E6** mechanical sweep of the 41 + 14 one-liners. **E7** sub-claim architecture table and abstract → (a) superseded, (b) open, (c) shipped.

**Sequencing:** ruling first, then E2–E7 as one v2.1 patch, **one recompile** (folds TODO-4104-CAPRECOMPILE). Plan: `capotauro/4118_revision_scope.md`. **Lane: CHIR.**

### TODO-4116-CAPRETIRE — is Capotauro still needed? Founder decision, assessment done (registered Patch 4116, CHIR/EW lane)

**Founder asked (18 Sep 2026)** whether the Capotauro event is still needed now that χ₄'s 4D helical bit supplies the chiral/mirror/parity effects.

**Assessment (Patch 4116, `series_umbrella/series_substrate_chirality_arc/capotauro/4116_is_capotauro_still_needed.md`): half yes.** Capotauro and χ₄ are not competitors — Patch 4084 settled that Capotauro supplies the **magnitude** (|M| = χ/6 = φ⁻³/6 ≈ 0.0394, from lattice geometry) and χ₄ supplies the **sign**. χ₄ produces no magnitude anywhere (unscoped search).

**REVISED at Patch 4117 after the founder pressed three challenges.** Verified by tracing the flagship theorem's own dependency list: THEO-CAP-1's section (`sec:composite_we`) contains **ZERO** nucleation mentions — its stated inputs are FI-C-1…FI-C-10 plus axioms A1/A3/A4. The word appears 41× in the paper and **never in the derivation that produces the number**. The paper's own architecture already separates them: **sub-claim (a)** is the nucleation event (hand-selection, OPEN, never closed); **sub-claim (c)** is the magnitude (SHIPPED). So retiring (a) drops an open sub-claim that was never load-bearing for (c). **Founder is right on F5 and I overstated it at 4116 by calling it a "cost":** a circular referral is not a partial answer being given up, it is the appearance of one — drop it and record F5 as having no candidate mechanism. **New editorial item TODO-4117-CHIRENAME:** since 4104 removed the sign, |χ| = φ⁻³ is an *anisotropy/perturbation amplitude*, not a "chirality magnitude" — χ₄ supplies the chirality, |χ| supplies the scale, the product is the asymmetry. Doc: `capotauro/4117_magnitude_survives_the_event.md`.

**RECOMMENDED THREE-WAY SPLIT:** (1) **KEEP** THEO-CAP-1 and the χ/6 machinery with PRED-O-25/26/27/31 — geometry not cosmology, and PRED-O-25 is validated within 2%; losing four theorems and a 2%-validated zero-parameter prediction to tidy an origin story is not a good trade. (2) **RETIRE** sub-claim (a), the nucleation event, as the handedness-selection mechanism — χ₄ supplies handedness structurally rather than historically, and the paper's own sign-from-n̂ clause was already withdrawn at 4104. Record as superseded, not deleted. (3) **RE-HOME F5 in the same decision** — 4103 established sub-claim (a) is F5's *only* named home, so retiring it leaves the CP phase with no candidate mechanism anywhere. That is acceptable and arguably more honest than a circular referral, but it must be *recorded* rather than discovered later.

**Provenance note:** Grok's authorship is not itself a reason to retire — the magnitude has since been re-derived from lattice geometry and validated. **Lane: CHIR/EW — founder decision.**

### TODO-4128-QUANTIZE — **CLOSED at Patch 4129: the clause cannot be added — it would be circular** (registered Patch 4128, EW/QM lane)

OPEN-QM-3 asks to **derive s = ½**, and s = ½ *is* the two-dimensionality that quantizing A_i would supply. So postulating A_i as a two-state spin-½ object assumes OPEN-QM-3's answer. **The QM payoff claimed at 4111 was circular and is RETRACTED.** The amendment gives spin a referent; the hard part of OPEN-QM-3 is the two-dimensionality, and a broadcast channel does not supply it. CPP derives QM rather than postulating it, so this route would abandon the programme's method on the question it cares most about. OPEN-QM-3 returns to its prior status; its 4098 progress note is corrected in `frontier_sectors/QM.md`.

**Patch 4128 withdrew A3G-8.** A classical axial 3-vector has state space S² — a continuum — while Pauli doubling needs exactly **2**. Real QM gets two because spin-½ lives in a 2-dimensional Hilbert space and the continuum of directions is a continuum of *superpositions*, not of independent states.

**The amendment as written (A1′/A3′/AP-4) adds a classical axial vector.** For the two-slot/Pauli result — the amendment's largest claimed payoff, and the one that addresses OPEN-QM-3 — A_i must be **quantized as a two-state spin-½ object**. That requirement is not presently in any of the three amended axioms and must be added. Until it is, **the QM payoff is conditional, not delivered.** Doc: `axiom_maturation/4128_b3_audit_a3g8_withdrawn.md`. **Lane: EW/QM.**

### TODO-4127-B3AUDIT — **DONE at Patch 4128; the gap was real** (registered Patch 4127, EW lane)

B3 is a **necessary condition for parity violation** ("to get V−A the parity-violating response must be odd in b"), **not** a prohibition on other readings of A. A3G-8 needed the stronger claim and I stretched B3 to give it. A P-even coupling that reads A's direction already exists — **A₁·A₂, ordinary magnetic dipole-dipole, established by my own A3G-2 at 4125** — so same-b CPs with different A *are* distinguishable and strict exclusion fails. **A3G-2 and A3G-3 STAND**: they used B3 only for the T-parity argument, which is exactly what B3 licenses. The 4127 concentration was real and broke in precisely the one place B3 was overstretched.

### TODO-4127-B3AUDIT — re-examine B3's support; it is now the amendment's single point of failure (registered Patch 4127, EW lane — PRIORITY)

**Patch 4127 found B3 (the χ₄ response is LINEAR in b) is the common factor under three passing results:** A3G-2 and A3G-3 (via the T-parity argument, B3 + F6) and A3G-8 (the two-slot/Pauli result). Six tests run, but the architecture underneath is far less redundant than the count suggests — at 4125 F6 carried two falsifiers; B3 carries three.

**Its failure mode is the most severe in the suite.** If any interaction reads A's *direction* rather than just sign(A·V), same-b CPs become distinguishable, strict exclusion fails, and Pauli doubling becomes unbounded — that does not merely refute the amendment, **it breaks fermions**.

**B3's own support has not been re-examined since Patch 4076**, where it was established as an answer to a founder question, *before* A_i existed as an axiom attribute. Whether an argument for linearity in a **binary bit** carries over to linearity in a quantity derived from a **continuous vector** is exactly the sort of step this session has repeatedly found to fail when checked (4102, 4110, 4123, 4124). **Recommend running this ahead of A3G-4/5/6:** those test whether the amendment fits; this tests whether three recorded passes are real. **Lane: EW.**

### TODO-4126-CAGEMOMENT — do the real cage evaluation of ⟨L̂ + 2Ŝ⟩ (registered Patch 4126, SS/EW lane)

Patch 4126 ran A3G-7 and got μ_p = +3.000 vs +2.793 observed (7.4%), μ_n = −2.000 vs −1.913 (4.5%), ratio −1.500 vs −1.460 (2.7%) — **zero parameters**, the amendment's first positive empirical result. But the scale came from the **naive** assignment m_q = M_N/3, not from a cage calculation. **OPEN-SS-8 asks for ⟨L̂ + 2Ŝ⟩ evaluated over the icosahedral/dodecahedral cage geometry, and that is undone.** Matching μ_p exactly needs m_q = 0.358 M_N against the naive 0.333 — a 6.9% gap that is precisely where the real calculation must do its work. **OPEN-SS-8 is ADVANCED, not closed; PRED-O-14 stays "to derive."** Doc: `axiom_maturation/4126_a3g7_result.md`. **Lane: SS/EW.**

### TODO-4124-QUADRATIC — the A3G-3 T-parity protection is linear-order only (registered Patch 4124, EW lane)

A3G-3 passes because an EDM coupling is T-ODD while χ₄'s b is T-EVEN (F6), and the response is LINEAR in b (B3) — so a T-even carrier cannot source a T-odd term. **But a response QUADRATIC in b would be T-even × T-even = T-even and is NOT excluded by this argument.** B3 established linearity, so the protection holds exactly where B3 does. A higher-order term needs separate treatment before A3G-3 can be called closed rather than passed. Bounded. **Lane: EW.**

### TODO-4123-A3G3 — **DONE at Patch 4124: A3G-3 PASSES structurally** (registered Patch 4123, EW lane)

**Corrected my own 4123 bound first:** I had modelled the field-induced tilt as a fixed direction, which is not the physical response — a field acts on a spin by torque, δA ~ A × B, perpendicular to A. With the physical form the magnetic channel **cancels exactly** (0.00000 at every δ from 0.002 to 0.2), because the tilt is odd in A and sums to zero over isotropic spins. **Ordinary magnetism does not threaten F2 at all.** What survives is the *aligning* term ~ d(A·Ê) — an electric dipole moment, bounded at |d_e| < 4.1e−30 e·cm, twenty orders tighter than the 1e−10 rad I quoted. **But χ₄ cannot source it:** an EDM is P-odd AND T-odd, while b is T-EVEN (F6, from CPT at 4085) and the response is linear (B3). T = −1 required, T = +1 supplied — forbidden. Protection is structural, from a fact derived weeks earlier for unrelated reasons.

Patch 4123 resolved the coherence question and thereby sharpened A3G-3 from a re-derivation into a **concrete calculation**: compute the **A_i-to-EM coupling coefficient** — how far an applied EM field torques a CP's axial spin — and check it against **δ_field < ~1e−10 rad** at atomic-parity-violation field strengths. If the coupling exceeds that, the amendment is withdrawn. Doc: `axiom_maturation/4123_coherence_resolved.md`. **Lane: EW.**

### TODO-4122-COHERENCE — **CLOSED at Patch 4123** — do sea-DP contributions add coherently or incoherently? (registered Patch 4122, EW lane)

**Both channels exist, with opposite fates.** The per-DP residual is nonzero only when A·V lies between 0 and δ(n̂·V), and **its sign follows sign(n̂·V)**. Sea-driven disorder → V isotropic → sign ±1 equally → **cancels, unconstrained**. Field-driven → V polarized (which is what the EM channel *is*, per SF-6's eDP-Sea polarization) → sign biased → **survives, R/N = δ exactly, independent of N**. Verified across two decades (δ = 0.002→0.2, ratio 0.95–1.02). **Consequence: the EM parity bound does not constrain the sea's disorder at all — the founder's 4122 picture is safe — and constrains only the A_i–EM coupling.**

**This one question now sets how tight F2's bound is.** Founder correction at 4122: DP-CAL-1 is a strong bias, not an identity — sea DI-bits perturb the antiparallel alignment, so vacuum magnetism is not exactly zero at finite scale. F2's residual is then **δ/π per DP** (linear, verified: a misalignment flips a bit only when A·V lies within δ of zero, measure δ/π).

Inverting the ~1e−10 intrinsic-EM-parity bound: **coherent** → δ < ~3e−10 rad, a severe constraint; **incoherent** → weakens by √N and is effectively unconstrained past N ~ 1e24. Deciding which applies is a structural question about the DI-bit sea that the corpus can address. Doc: `axiom_maturation/4122_dp_cal1_is_a_bias.md`. **Lane: EW.**

### TEST-A3G-1…9 — the test programme on the A3′ completion — **now running against a PROVISIONALLY ADOPTED axiom (Patch 4120)** (registered Patch 4115, EW lane)

**ALL THREE FALSIFIERS RUN (4121, 4124, 4125) — NONE FIRE.** A3G-1 does not fire; A3G-3 and A3G-2 both PASS by T-parity (an EDM coupling and the monopole-dipole/spin-velocity forces are T-ODD, while b is T-EVEN by F6 and the response is linear by B3). **CAVEAT THAT MATTERS FOR ADOPTION: two of the three pass by ONE structural fact (F6), so if F6 is wrong they reopen simultaneously — the protection is concentrated, not distributed — and the linear-order caveat (TODO-4124-QUADRATIC) applies to both.** Per the founder's 4093 "clean win" standard: the suite is **one-third complete**, and the completed third is the part that can only *fail*. Passing falsifiers removes objections; it supplies no positive evidence. **A3G-4/5/6 and A3G-7/8 are UNRUN, and A3G-7 (nucleon magnetic moments) is the strongest empirical test in the suite and the next thing to do.** A3G-9 effectively answered negatively at 4121. Doc: `axiom_maturation/4125_a3g2_result_and_suite_status.md`.

**A3G-1 RUN at Patch 4121 — DOES NOT FIRE, but returns a partial negative.** Only DP-CAL-1 (antiparallel) gives exact fluctuation-free cancellation of the sea's axial channel; without it the vacuum is non-magnetic only *on average* (RMS ~ √N, density ~ 1/√N). **The adopted axiom does NOT make DP-CAL-1 dispensable** — it supplies the referent, not the derivation. **This retracts payoff 5 of the 4111 scoping** ("DP-CAL-1 becomes derivable"); the payoff list is now 4, not 5. **A3G-9 should be re-scoped or retired** — it asks the same question from the other end and this largely answers it negatively in advance. **A3G-3 is now the sharper remaining falsifier.** Result: `axiom_maturation/4121_a3g1_result.md`.

**STATUS CHANGE at 4120:** the founder ruled the 4D bit approved into the CP/GP/DI-bit vector string; χ₄ is recorded **PROVISIONALLY ADOPTED** and A3′ amended in the registry. **A3G-1/2/3 remain LIVE FALSIFIERS — if any fires, the amendment is WITHDRAWN, not patched.** The suite is now the lane's primary work.

**Founder authorization 18 Sep 2026:** *"Yes, please complete all missing tests to confirm this axiom and its compliance with empirics."* (verbatim: `founders_voice/4115_authorization_test_the_axiom_against_empirics.md`)

Nine tests specified in `handovers/2026-09-18_session_233_carryover_a3g_test_programme.md` §3. **Falsifiers (run first):** A3G-1 vacuum magnetisation without DP-CAL-1; A3G-2 spin-dependent fifth force vs torsion-balance/comagnetometer bounds; A3G-3 EM parity re-derived from the axiom alone. **Consistency:** A3G-4 AP-4 messenger/computed split; A3G-5 SF-6 "axial part" disambiguation sweep; A3G-6 F3 re-derivation without R-F3. **Payoff:** A3G-7 nucleon magnetic moments (OPEN-SS-8 / PRED-O-14 — the strongest empirical test, and for L = 0 the spin half carries it entirely); A3G-8 spin-½/Pauli via 4098; A3G-9 promote DP-CAL-1 from calibration to derivation.

**NOT in scope: F5.** A·V is a sign, not an angle; the axiom supplies no CP phase (4103/4110). Do not let the suite drift there.

**Framing:** the instruction says *confirm*; the programme is written to *test*, per PD-008 and the founder's own 4093 standard ("adopt only after a clean win"). **Lane: EW.**

### TODO-4111-A3AMEND — χ₄ requires a new irrep channel in A3′; price and propose it (registered Patch 4110, EW lane — AXIOM-LEVEL, founder decision)

Patch 4110 proved that **no pseudoscalar buildable from A3′'s ratified LSP′ = (Φ, V_i, Q_ij) is nonzero on any CPP structure** — the unique candidate det[V,QV,Q²V] is a Vandermonde in Q's eigenvalues and dies on anything axially symmetric, which every CPP structure is (including the D6 W bracelet, where V−A is maximal).

**So χ₄ cannot ride existing content. It requires amending A3′** to broadcast a genuine pseudoscalar channel — exactly the "new concept that has never been used" the founder named at 4109.

**SCOPING DONE at Patch 4111** (`series_standard_model/axiom_maturation/4111_a3_amendment_scoping.md`), on the founder's question. Recommended form: **Option B — add an AXIAL VECTOR channel A_i (the CP's ZBW spin)**, matched across A1′ (CPs carry it), A3′ (LSP′ broadcasts it), AP-4 (DI-bits transport it). Then b ~ A·V is *derived*, not postulated; it bypasses the 4110 obstruction (no Q dependence); and it independently reproduces F6's P-odd/T-even signature. Preserves F2 (DP-CAL-1) and F3 (4101 cage cancellation, max |Σ| = 0 over 20,000 spins).

**TODO-4111-BCONFLICT — CLOSED at Patch 4112, NO CONFLICT.** SF-6's ∇×V and Option B's A_i are the *orbital* and *spin* halves of ⟨L̂ + 2Ŝ⟩ — the operator OPEN-SS-8's own solution statement already names. Not duplicates. And for the nucleon (ground state, L = 0) ⟨L̂⟩ = 0, so 100% of the moment is spin and orbital magnetism supplies *none* of it; spin-only SU(6) gives μ_p/μ_n = −1.500 against an observed −1.460, agreement 2.7% with no free parameter. The risk inverts into a payoff: Option B supplies the half OPEN-SS-8 (HIGH) and PRED-O-14 are blocked on. What survives is an editorial obligation at adoption — SF-6 text saying "the axial part" must specify which. **Still unchecked from 4111: AP-5 saturation budget vs +33% content.**

### TODO-4113-CONTENTCOST — AP-5 does not budget per-CONTENT cost at all (registered Patch 4113, EW/GR lane)

Ruling 1 at Patch 4113 found AP-5's saturation budget is **arrival-count based** ("more DI-bits *arrive* in one Moment than it can *act on*"; derived depth ⌈1.5 v⌉; D1 clips, D3 relays whole, D4 stores). A fourth irrep changes what each DI-bit carries, not how many arrive, so **no threshold is crossed**.

**But AP-5 quantifies no per-content cost whatsoever.** D3's whole-relay and D4's register storage would each carry 33% more content per Moment with nothing in AP-5 to measure it against. The finding is "unbudgeted", not "free" — AP-5 cannot be violated because it does not constrain this. **If a future result makes per-content cost matter (register depth, relay bandwidth, the D4 held sector), this ruling does not protect it.** Worth a GR-lane look since AP-5 is that lane's amendment. **Lane: EW/GR.**

### TODO-4112-SS8DEP — OPEN-SS-8's dependency field was wrong; check the sibling entries for the same shape (registered Patch 4112, SS lane)

OPEN-SS-8 carried **"Dependencies: None blocking"** at HIGH priority while its stated route required a spin operator CPP does not have — unreachable in principle, with nothing downstream to contradict it. Corrected in `frontier_sectors/SS.md` at 4112. **Residual:** this is the same failure shape as Patch 4102 (a route quietly presupposing something absent). The other OPEN-SS-* entries, and OPEN-G-2 (lepton anomalous moments, named as a cross-connection of SS-8), should be checked for dependency fields that presuppose missing attributes. Bounded. **Lane: SS.**

*(superseded text follows)* **REMAINING BEFORE THE AXIOM QUESTION CAN BE PUT — TODO-4111-BCONFLICT:** SF-6 derives **B as the curl of a polar displacement** (4069/4070). Option B adds a *second* independent axial object to the same packet. Formally distinct (B = ∇×V from the V channel; A a per-CP attribute) but every SF-6 result reading "the axial part of the lattice state" would need to say which. **Settle this before adoption.** Also unchecked: whether AP-5's saturation budget absorbs +33% broadcast content. **Lane: EW.**

### TODO-4109-4071 — relationship between the LSP′ pseudoscalar and Patch 4071's ≥4-directions result — **ANSWERED at Patch 4110, affirmatively for 4071** (registered Patch 4109, EW lane)

No conflict; they agree. 4071 found a CP needs ≥4 independent internal *directions* to carry a pseudoscalar. Patch 4110 reaches the same wall from the LSP′ side: (V, Q) cannot produce a nonzero pseudoscalar on any symmetric CPP structure. **4071's conclusion — "internal structure IS an axiom rather than an alternative to one" — is corroborated, not threatened.**

Patch 4109 found a pseudoscalar inside A3′'s LSP′ content: det[V, QV, Q²V], rotation-invariant and P-odd (5000/5000 P-flips), vanishing identically for isotropic Q.

Patch 4071 found that a CP needs **≥ 4 independent internal directions** to carry any pseudoscalar, with k = 1,2,3 identically zero — and concluded "internal structure IS an axiom rather than an alternative to one."

Q is a symmetric rank-2 object (5 dof), not a direction vector, so the two constructions are formally different and there is no contradiction on the face of it. But they are close enough that the relationship should be **established rather than assumed** — specifically, whether V + Q supplies what 4071 counted as ≥4 directions, and if so whether 4071's conclusion about internal structure needs restating. Bounded. **Lane: EW.**

### TODO-4104-CAPRECOMPILE — Capotauro PDF recompile owed after the 4104 sign corrigendum (registered Patch 4104, Thomas's mechanical action)

`capotauro.tex` source was edited at Patch 4104 (marked corrigendum withdrawing the sign-of-χ-from-n̂ clause; magnitude results untouched). The shipped PDF is now stale relative to source. **Thomas's mechanical action per PD-006(b).** Ledger precedent: the VW-1 v1.5 recompile owed since 0985.

### TODO-4103-NHAT — does Capotauro v2.0's sign(χ)-from-n̂ survive this lane's 4046? — **ANSWERED NO at Patch 4104** (registered Patch 4103, CHIR/EW lane)

**VERDICT: it does not survive, on two independent grounds.** (i) det(−I₄) = +1 and −I₄ is a 600-cell symmetry, so n̂ and −n̂ are related by a *proper* rotation and name the same configuration — the sign of n̂ selects no enantiomorph for **any** n̂ (4072). (ii) Under the vertex-aligned reading FI-C-RC-2 that Capotauro cites, **30 improper symmetries fix n̂**, so (600-cell, n̂) is achiral (4046). A generic n̂ escapes (ii) but not (i). Marked corrigendum applied to `capotauro.tex`; magnitude results (|χ| = φ⁻³, |M| = χ/6, THEO-CAP-1) untouched. Full write-up: `series_umbrella/series_substrate_chirality_arc/capotauro/4104_nhat_sign_corrigendum.md`. Recompile owed: TODO-4104-CAPRECOMPILE.

Capotauro v2.0 states that **both** the sign and the magnitude of χ are derived from the substrate's primitive 4D direction n̂ (FI-C-RC-1): "the sign of χ (which enantiomorph is selected) … fixed by the substrate's primitive direction."

This lane's **Patch 4046** found that n̂ aligned with a host vertex is **fixed by Θ = diag(1,1,1,−1)**, so (600-cell, n̂) is **achiral** — and read the five V3 confirmations as five demonstrations of exactly that.

**Not examined at 4103** (out of audit scope): whether these two survive together, or whether Capotauro's sign derivation uses n̂ in a way 4046 does not reach. If they do not survive together, Capotauro v2.0's sign claim is affected, which bears on sub-claim (b) and on H1's role. Bounded read of `capotauro.tex` §sec:h4_i4 against `reasoning/4046`. **Lane: CHIR/EW.**

### TODO-4102-NEXTID — `next_id.py` was blind to 4xxx bare-numbered subjects; check the other gates for the same shape (registered Patch 4102, EW lane)

**Fixed at 4102.** `taken()` matched bare-numbered commit subjects only with a leading zero (`^0\d{3}`), taught for the 09xx chirality lane at Patch 0936. The 4xxx EW lane uses the identical bare form (`4101 F3 DERIVED …`) and was invisible: **no git-log pattern saw 4100 or 4101.** The block was protected only by the `id_block_registry.md` cell narrative, so the moment a patch did not write "Patch NNNN" into a scanned file its ID vanished — which 4101 did, after which the gate RECOMMENDED the already-pushed 4101. Caught one step before a collision. Pattern broadened to any 4-digit opener; the existing `[lo, hi]` filter keeps date-like lines out; regression-checked against all lanes (chir/dm/de/gr/eu unchanged).

**Residual — DISCHARGED at Patch 4105.** The sibling gates do NOT carry the leading-zero assumption: `continuity_gate.py` matches `\s*(?:Patch\s+)?(\d{3,4})[a-z]?\b` and reads all four ID forms; `absence_gate.py`, `deferral_gate.py`, `encoding_gate.py` parse no IDs at all. **But the audit found a different defect in `continuity_gate.py`:** its `BLOCKS` still read `'ew':(4000,4099)`, so the gate whose purpose is catching a silently-missing patch was not watching 4100–4199 at all — patches 4100–4104 were outside its coverage. Root cause: Rule 6 named only `next_id.py` (written 3807; continuity_gate did not exist until 4029). **Rule 6 generalised to every gate carrying a block table**; both gates fixed and verified; exhausted block `ew-4000` restored per the eu-3800/gr-3600 convention. Fourth Rule-6 lag on record, first outside `next_id.py`. **Lane: EW — DONE.**

### TODO-4142-SSVAUDIT — audit every corpus use of "SSV_net" and resolve it to ^pot or ^disp (registered Patch 4142, GR/WORKFLOW lane)

Patch 4142 established that **SSV_net names two objects**: **SSV_net^pot** (the LSP′ l=1 broadcast component V_i = g_ti — potential-like, what GPs broadcast) and **SSV_net^disp** (the vector a CP displaces by in one Moment — field-like, built from derivatives of the broadcast potentials, what the A1′ Displace clause means). Every use in the corpus should resolve to one. Touches SR-1, GR-1 and companions, `master_glossary.md`, the A1′/A3′ axiom text, and the χ₄ patch series. **Mechanical but wide; no physics moves.** 4142 deliberately did NOT rewrite existing text. **Lane: GR/WORKFLOW.**

### TODO-4141-SSVROLE — **RESOLVED at Patch 4142** — SSV_net is used in TWO roles and b = A·V does not say which (registered Patch 4141, EW/GR lane — upstream of the amendment)

**Resolved at 4142 by the corpus's own force equation.** GR-1a, verbatim: *"The force on a second mass m′ in this SSV gradient is F = m′c² · k · ∇(ΔSSV_grav)"* — the broadcast quantity is **potential-like** and what a body responds to is its **gradient**, a derived field. So the A1′ Displace clause's "SSV_net" is **not** the LSP′ component V_i. Disambiguation proposed: **SSV_net^pot** vs **SSV_net^disp** (see [[TODO-4142-SSVAUDIT]]). b contracts A with **SSV_net^disp** — *strongly indicated, not proven*. **This RELOCATES [[TODO-4140-BIVECTOR]]**: 4141's objection was right against role 2 (V_i sits in the symmetric tensor) but does not apply to role 1, where SSV_net^disp and A_i are both attributes *of the CP* — the natural home for an M_μν pairing. **Live again, not answered.** *(original entry:)* **Role 1:** the CP's local **displacement instruction** — *"every CP executes one Displace step per its GP's computed SSV_net"* (master_glossary, A1′ division of labor). Velocity-like. **Role 2:** the l=1 **broadcast component** V_i = g_ti, the gravitomagnetic **potential** (master_glossary, LSP′ entry). Potential-like. They transform differently: a potential is gauge-dependent, so A·(potential) is not even gauge-invariant; a velocity needs a bivector partner to be protected. **The conflation predates χ₄** — it did not matter while nothing contracted V_i with an axial vector, and **b = A·V is the first construction in the corpus that does.** Touches SR-1/GR-1 usage, not just the amendment. Derivable hence mine (PD-008), but it is a corpus-wide terminology ruling and the founder should see the result. **Lane: EW/GR.**

### TODO-4140-BIVECTOR — **CLOSED AS MISCONCEIVED at Patch 4143** (not solved — the target was wrong)

**b does not need to be Lorentz-INVARIANT; it needs to be COVARIANT.** Helicity is not invariant for a massive particle in *any* theory — a collinear boost above the particle's own speed reverses p̂ (nucleon at 0.3c: any β > 0.3; photon: needs β > 1, impossible), which is exactly why the corpus's own OPEN-FP-SF-2-CHIR closes V−A **at the massless helicity limit**. The comagnetometer forbids not frame-dependence but an energy term κ(Ŝ · **n̂_cosmic**) with a **fixed cosmic direction**; a covariant theory has no such direction, since every vector in the energy is local and the lab's rotation moves them together. The founder's ruling says *"Lorentz-modified **local** reference-frame velocity … no absolute-frame signature"* — that is covariance, and I read it as invariance, which is stronger and false. **A3G-2 PASSES**, on exactly the same footing as every other CPP result relying on SR-1's emergent covariance — no weaker, no stronger. Doc: `axiom_maturation/4143_covariance_not_invariance.md`. **Lane: EW — DONE.**

*(superseded entry:)* ### TODO-4140-BIVECTOR — RE-SCOPED at Patch 4141; does NOT discharge — show that A3′/AP-4 transport mixes A_i and V_i under a boost as ONE antisymmetric rank-2 object (registered Patch 4140, EW lane — decides A3G-2)

**Pressed at 4141 and it fails on the axiom text.** LSP′'s nine components are the **traceless SYMMETRIC** rank-2 tensor (Φ = g_tt, V_i = g_ti, Q_ij the radiative tensor — the glossary says so three ways), and **a component of a symmetric tensor cannot also be half of an antisymmetric one**. So V_i is not available as A_i's partner and **4140's "forced" is WITHDRAWN**; what survives is that F6 fixes the *parities* any partner must have. A genuine partner exists in the GR sector — the gravito-electromagnetic **E^G = −∇Φ − ∂_t V** (with B^G = ∇ × V) — but then b would have to be **A·E^G, not A·V**, a different quantity built from derivatives rather than the potential. **Re-scoped:** identify A_i's polar partner and determine whether b contracts A with it or with V_i; blocked behind [[TODO-4141-SSVROLE]]. *(original entry:)* Patch 4140 showed b = A·V is a Lorentz **pseudo-invariant** — the exact analogue of E·B — **provided** (V_i, A_i) are the boost-like and rotation-like halves of one bivector, which F6 (b T-even, CPT 4085) *forces* to be the **M_μν** type rather than the F_μν type. Verified invariant to 2.1e−10 over 200 000 random boosts. **The gap:** A3′ as written lists V_i and A_i as **separate broadcast components** of LSP′, not as one tensor. If they are independent channels each transported on its own, a boost need not mix them, A·V is not invariant, and 4139's absolute-frame problem returns in full. **Derivable, not a picture question** — it is about the transport law, so it is mine under PD-008. Until it is shown, **A3G-2 is not firing and not passing.** Doc: `axiom_maturation/4140_b_is_a_bivector_invariant.md`. **Lane: EW.**

### TODO-4139-BCOVARIANT — **ANSWERED by founder 19 Sep 2026 and DERIVED at Patch 4140** — **is V in b = A·V the ABSOLUTE SSV_net or the LOCAL RELATIVE one?** (registered Patch 4139, EW lane — FOUNDER QUESTION, PD-006(a); decides A3G-2 and therefore the amendment)

**Founder ruling (`founders_voice/4140_ruling_no_absolute_frame_signature.md`): NEITHER horn.** *"The CPs do not measure their motion against the universe or the local frame… the summation yields a Lorentz-modified local reference-frame velocity… resulting in no absolute-frame signature."* There is no comparison operation; the summation over the PSR environment **is** the measurement. **Derived at 4140** rather than accepted: b is the pseudoscalar invariant of the (V, A) bivector, so **4139's drift term is WITHDRAWN** as the residue of boosting one half of a two-part object, and **4134 stands as originally written**. Residual: [[TODO-4140-BIVECTOR]]. *(original entry:)* **The single question A3G-2 now reduces to.** If V is the absolute (Nexus) SSV_net, b is frame-dependent: a lab-rest nucleon drifts at β = 1.2e−3 through that frame, the SU(6) spin projections sum to **+1** so the drift does **not** cancel, and the s-wave average cannot remove it (the drift is fixed in the lab while cage orientations average). The resulting sidereal spin-energy modulation exceeds the ³He–¹²⁹Xe comagnetometer bound **b̃⊥ⁿ < 8.4e−34 GeV** by ~**1e23** even at the most suppressed scale the corpus offers. If V is the local relative SSV_net (measured against the local sea rest frame), b is frame-independent and A3G-2 passes. **SR-1 does not settle it** — it predates the A3′ amendment and does not mention A_i; **SD-1's suppression claim does not settle it either** — its two natural readings (lab/Hubble = 7.7e−27, Planck/Hubble = 1.2e−61) straddle the bound by 3 and 25 orders respectively. Unlike [[TODO-4137-FILTERTABLE]] this IS answerable as a physical picture, so it goes up. Doc: `axiom_maturation/4139_a3g2_conditionally_firing.md`. **Lane: EW.**

### TODO-4138-A3G2MAG — **DONE at Patch 4139: A3G-2 is CONDITIONALLY FIRING** (registered Patch 4138, EW lane) — A3G-2 is back to UNRUN; the magnitude test is what decides it (registered Patch 4138, EW lane)

**Result at 4139.** The candidate rescue I proposed at 4138 is **WITHDRAWN**: (a) A_i is *broadcast* (A3′ LSP′, AP-4 payload), so the A channel is long-range by construction — "the bracelet is transient" does not reach it; (b) the comagnetometer bound is not on a two-body force at all but on the spin-direction-dependent **energy of one neutron**, so a two-body argument cannot touch it. Magnitude: κ ≤ 6.8e−31 GeV required; weak-suppressed hadronic gives 4.5e−8 GeV, over by **6.7e22**. **A3G-2 is neither passed nor unrun — it is CONDITIONALLY FIRING**, and per 4120 a fired A3G-2 *withdraws* the amendment. The one thing that decides it is [[TODO-4139-BCOVARIANT]] above. **Also revises Patch 4134** as incomplete: W was computed in the nucleon rest frame and the absolute-frame drift term survives the s-wave average. **Lane: EW — DONE.**

*(original entry:)* Patch 4138 withdrew A3G-2's T-parity protection (the spin-velocity row **A·v is T-EVEN**, as 4125's own script printed and its prose inverted; A·v and A·V are the *same* invariant given F6 + A T-odd, so **b IS a spin-velocity pseudoscalar** and "comagnetometers bound it, χ₄ can't source it" is self-refuting). **A3G-2 is UNRUN, not FAILED** — firing it requires showing the predicted spin-velocity coupling **exceeds** the comagnetometer bound, which 4138 did not attempt. **The bounded calculation:** estimate the χ₄ spin-velocity coupling for a nucleon in a comagnetometer, compare against the published bound. **One candidate rescue to test first:** if only the *transient bracelet* channel reads b (filter table), there is no LONG-RANGE spin-dependent potential at all and comagnetometer bounds do not apply — structure rather than T-parity, and conditional on [[TODO-4137-FILTERTABLE]], which now carries **five** results. **Lane: EW.**

### TODO-4138-TABLEPROSE — any conclusion resting on a script's classification table must reproduce the rows, not paraphrase them (registered Patch 4138, WORKFLOW lane)

The 4138 failure was **not** a wrong premise: it was a **computed table whose prose summary inverted two of its rows**, cited across four patches. Reasoning capture caught nothing because what was captured was the prose. **Rule to adopt:** a patch whose conclusion rests on a classification table produced by a script must paste the table's rows into the document verbatim, so the document and the script cannot silently disagree. Candidate for a gate (`code/`) that diffs a document's quoted table against the script's output. **Lane: WORKFLOW.**

### TODO-4137-FILTERTABLE — the filter table is load-bearing for four results and the founder has declined to endorse it (registered Patch 4137, EW/SS lane — now the lane's highest-leverage item)

The filter table at `chirality_axiom_maturation` §2aa (weak reads b linearly; EM and strong read magnitude only) now carries **F3, A3G-2, A3G-3 and TODO-4136-BINENERGY**. Its own status line reads **"Status: CONDITIONAL"** and records the founder's response as **"I have no explanation"** (session 233). It is a worker proposal, not established corpus. **If the strong channel reads b after all, BINENERGY's bound evaporates and route 4 of SPINORIENT reopens unbounded.** Upgrading or refuting the table — deriving from A1′/A3′/AP-4 *which* functions of A each sector's response can read — would brace four results at once. Note this is NOT a founder question in its present form: 4108's attempt to hand it up produced "I have no explanation," so it must be pressed as a derivation (PD-008). **Lane: EW/SS.**

### TODO-4136-BINENERGY — **ANSWERED CONDITIONALLY at Patch 4137** (registered Patch 4136, EW/SS lane)

**Result at 4137: YES-but-routed, conditional on the filter table.** If only the bracelet channel reads b (filter table §2aa), a P-odd term in a nucleon's internal energy cannot come from the strong or EM channel and must pass through **bracelet formation** — routed through the weak scale rather than left free. Size: G_F m_π² = **2.27e−7**. **But:** (a) the scale is **imported, not derived** — SF-2 derives m_Z/m_W at zero parameters but m_W itself is *calibrated via η_W*; (b) it sits a **factor 2.6 on the WRONG side** of 4136's bound ε ≤ 8.6e−8, which is agreement at order of magnitude with no slack, saying only that the unknown O(1) coefficient cannot be much larger than 1 and that **no CPP-extra P-odd contribution fits** on top of the weak admixture; (c) the filter table is itself **CONDITIONAL** (TODO-4137-FILTERTABLE above). **R-F3-ISO is NOT independently secured; F3 still rests on the bound it is trying to explain.** Doc: `axiom_maturation/4137_binenergy_conditional.md`. **Lane: EW/SS — DONE (conditional).**

*(original entry:)* The one route 4136 could not close. An **A·V** term (= b itself) in a nucleon's internal energy is **P-odd, T-EVEN** — T-parity cannot exclude it, precisely because F6's T-evenness is what makes b available as a carrier at all. Such a term IS hadronic parity violation, so excluding it by assumption is circular. The A3G-2 table's parenthesis (*"this is the local bit, not a force between masses"*) is a scoping remark about two-body potentials, **not** a proof that b is absent from the internal Hamiltonian — and 4136 deliberately declined to cite it as one (PD-008 branch marked; the next window should check that refusal). **The question:** the bit is read by something; does whatever reads it contribute to the energy, and at what order? Answering it would strengthen F3, A3G-2 and A3G-3 at once. **Lane: EW/SS.**

### TODO-4134-SPINORIENT — **ANSWERED at Patch 4136 for 3 of 4 routes; the 4th is TODO-4136-BINENERGY above** (registered Patch 4134, EW/SS lane)

**CORRECTED AT 4138 — the route count was wrong, the position was not.** A·v and A·V are the **same invariant** (F6 + A T-odd ⇒ V T-odd), so SPINORIENT has **three** distinct routes, not four: A·r̂ (closed, genuinely T-odd), (A·V)² (closed by the even-exponent argument, independent of F6/B3), and **A·V (open, conditionally bounded at 4137)**. The F6+B3 closure of the "A·v" route is withdrawn with A3G-2's. **One open route, conditionally bounded — unchanged.** *(original entry:)* **Result at 4136.** A correlation requires **polar order** (an energy term odd under n → −n). Of the four routes: **A·r̂** and **A·v** are closed by F6+B3 (T-odd, χ₄ cannot source); **(A·V)²** is closed by a new and independent argument — exp(c u²) is EVEN in u, so a quadratic term makes *nematic* order (⟨cos²θ⟩ 1/3 → 0.89 at c = 10) but ⟨cos θ⟩ stays **exactly zero**, so **TODO-4124-QUADRATIC's loophole, which does reopen A3G-2 and A3G-3, does NOT reopen R-F3-ISO**; the fourth (**A·V**) is not closeable this way. Sizing: ε = L(g) → g/3, and the ~1e−7 PV bound gives ε ≤ 8.6e−8, g ≤ 2.6e−7. **THE COST:** the two T-parity closures use the same **F6+B3** premise already carrying A3G-2 and A3G-3 — a **third** result on one premise; if F6 fails they reopen together. The suite is *less* independent after this patch than it looked before, though nothing fired. Doc: `axiom_maturation/4136_spinorient_answered.md`. **Lane: EW/SS — DONE (3 of 4).**

*(original entry:)* Patch 4134 found F3 holds for the nucleon **by the L = 0 s-wave average**, not pointwise: B_tot = **n·W** with W = Σ s_i V_i a polar vector in the cage frame, |W| ≈ 1.17 for the SU(6) proton, and ⟨n·W⟩ = 0 only because an s-wave's internal frame is uncorrelated with its spin axis. **R-F3-ISO** names the requirement: no spin–orientation correlation above ~1e−7 (a residual ε leaves B_tot ≈ 1.17 ε against the ~1e−7 hadronic PV bound). **The risk:** the amendment makes A_i a broadcast channel, so an A-dependent term in the dynamics could itself generate that correlation — which would not be a small correction to F3 but its failure mode. Adjacent to **TODO-4124-QUADRATIC** (a response quadratic in b is T-even and excluded by nothing on file). **Also uncovered:** excited states and L ≠ 0 structures, for which the s-wave argument says nothing. Doc: `axiom_maturation/4134_f3_on_the_real_nucleon.md` §3. **Lane: EW/SS.**

### TODO-4133-F3CALC — **CLOSED at Patch 4135; all three steps run** (registered Patch 4133, EW/SS lane)

**Steps 1–2 discharged at 4134.** Step 1 located the corpus's actual nucleon — SS-2's **distorted tetrahedral cell with one OPEN vertex**, three charge-bearing points, not the icosahedral/dodecahedral shells the entry assumed. Step 2 found the tetrahedral cell has **no inversion at all**, so 4133's inversion-pairing sketch is **withdrawn as applied to the nucleon**; 4101 is untouched, being about the antipodally paired z = 12 coordination shell, a different object. What replaced it: B_tot = n·W, W = 0 exactly for all-parallel spins (Σ V_i = 0 by action–reaction), and for the SU(6) proton F3 holds by the L = 0 orientation average under **R-F3-ISO** (TODO-4134-SPINORIENT above).

**Step 3 discharged at 4135.** The bracelet's hexagon IS antipodally paired 6/6, so the danger was real — but its polarity alternates around a ring of even length and 3 is odd, so **antipodal vertices carry opposite charge**: plain inversion does not preserve it, inversion × C does, and V_(i+3) = −V_i exactly. Over all 64 collinear ±1 spin assignments 10 give W = 0 and 54 do not, and **all 8 inversion-even assignments give W = 0**. So the bracelet is in the *same* position as the cage — **neither structure's handedness comes from its shape.** The discriminator is **R-F3-ISO itself**: a nucleon ground state satisfies it (s-wave, frame isotropic) → P-even; a bracelet in a scattering event **violates it by construction**, its frame being set by the incoming particle's momentum → P-odd. One requirement, two sectors, opposite outcomes. **Not established:** the P-odd half rests on **B3**, whose support was narrowed at 4128 and is not repaired here. Doc: `axiom_maturation/4135_bracelet_same_footing.md`; verify `code/4135_bracelet_same_footing.py`. **Lane: EW/SS — DONE.**

### TODO-4101-F3 — R-F3 — **CLOSED as a founder question: ANSWERED at Patch 4109 ("neither"), re-confirmed 19 Sep 2026 (Patch 4133)** (registered Patch 4101, EW lane)

**HEADER CORRECTED at Patch 4133.** This entry read "still awaiting founder" from 4108 until 4133. It was not awaiting anything: the founder answered at 4109 (`founders_voice/4109_ruling_gp_summation_and_the_4d_element.md`) — the bit is declared per CP, per Moment, to its own GP, and summed at the receiving GP; the per-arc / per-vector-sum dichotomy is false. Patch 4110 withdrew 4109's *carrier* and correctly reopened **F3**, but the founder's answer to the dichotomy never depended on the carrier and the header was not updated. **Cost:** the Session 234 window re-asked the founder a question he had answered ten days of patches earlier. F3's remaining work is TODO-4133-F3CALC above. *(4108 text retained below for provenance.)*

**THE QUESTION, restated at Patch 4108 (this is the form to answer):**

> **Is the helicity bit b written once per ARC in a CP's cohort, or once for the cohort's VECTOR SUM?**

**Why this replaces the 4101 wording.** Patch 4107 showed the corpus already uses the per-interaction reading in the EM sector: a polarized sea DP at rest has net momentum zero, so a net-momentum reading would leave b undefined there — yet SF-6's polarization mechanism gives each constituent its own opposed arc, which is what 4107's F2 result depends on.

**Consequences.** Per arc ⇒ a confined quark's arcs resolve per SSV partner ⇒ along the antipodally paired cage bonds ⇒ ⟨b⟩ = 0 exactly ⇒ **F3 derived**, and F2 keeps its basis. Per vector sum ⇒ b undefined for anything at rest (undermining 4107) and generic-direction for a confined quark ⇒ **F3 fails against the ~1e−7 hadronic PV bound by ~10⁷**.

**Reconciliation with the 4097 ruling:** the cohort is a *set* whose vector sum is the momentum — sea DP at rest sums to 0 with two opposed arcs; free particle sums to p; confined quark sums to ≈0 along cage bonds. All three work under the per-arc picture.

**Status:** argument from precedent, not derivation. Doc: `series_standard_model/axiom_maturation/4108_rf3_sharpened.md`. **Lane: EW.**

*(original 4101 wording retained below for provenance)*

### TODO-4101-F3-ORIG — R-F3 as originally filed: do a confined quark's DP arcs lie on cage bond directions? (registered Patch 4101, EW lane)

**Status: OPEN — awaiting founder. This is the one remaining physics-picture question in the F3 chain.**

**Background.** Patch 4101 derived F3: the SF-2 cage shells (icosahedral 12, dodecahedral 20) are exactly antipodally paired, so Σ sign(ω·v̂) = 0 for every ω — algebraically, pairwise, with no averaging and no parity assumption (equal weighting comes from the proper rotation group I alone, all det +1, transitive on both shells). A free particle's arc cohort is a single direction and does not cancel: |⟨b⟩| = 1. Same linear coupling, opposite outcomes, no separate stipulation per sector.

**The requirement that makes it work.** The icosahedral rotation group I does NOT contain −I. Antipodal pairing is a property of the **special symmetry-axis orbits** (12-shell on C5 axes, 20-shell on C3, 30-shell on C2) and **not** of icosahedral symmetry in general — 6 of 6 generic I-orbits tested come back 0/60 paired, with a residual bit sum of 6.7–10%.

**R-F3:** the confined quark's DP arc cohort must lie along cage **bond directions** (those symmetry-axis shells), not in generic directions.

**The question for Thomas (physical picture):** when a confined quark is deflected by the cage and its DP arc cohort is severed and re-established, is the new cohort laid down along a cage bond direction, or can it point in a generic direction? SF-6 describes arc establishment during acceleration but does not say whether the cage's bond geometry quantizes the resulting direction.

**Stakes.** With R-F3: ⟨b⟩ = 0 exactly, F3 derived. Without it: strong-sector parity violation at ~10%, against an observed hadronic PV of ~1e−7 that is already fully accounted for by weak admixture — an overshoot of roughly **six orders of magnitude**. R-F3 is load-bearing and falsifiable, not a modelling convenience.

**Doc:** `series_standard_model/axiom_maturation/4101_f3_derivation.md`. **Verify:** `series_standard_model/code/4101_f3_derivation_verify.py`. **Lane: EW.**

### TODO-4106-F2DP — F2: is a sea DP's (spin, arc) relative-orientation parity matched? — **ANSWERED at Patch 4107** (registered Patch 4106, EW lane)

**Status: CLOSED AFFIRMATIVE.** Founder ruled no CP spin has ever been assigned; assumes antiparallel, declines to assert, directs a calibration turn. Patch 4107 found the arc half was never a free choice (SF-6 derives EM from eDP-Sea Polarization; polarizing a dipole displaces its CPs oppositely; with 4097 the arc cohorts are opposed — forced). F2 then holds iff spins antiparallel = the assumed value. R = 0 exactly and pointwise. Empirics sweep: 4 supporting / 1 no-conflict / 1 silent. **F2 HOLDS under DP-CAL-1; the falsifier is not triggered.** Registered as a CALIBRATION, not a derivation.

**The reduction (Patch 4106).** A DP is a bound pair of opposite-polarity CPs (glossary); the response to b must be linear (B3, 4076) with a C-odd polarity coefficient forced by CPT (F6, 4085). So one sea DP's net χ₄ response is R = q(b₊ − b₋). Sea isotropy never enters — cancellation is per-DP and pointwise.

**The question for Thomas (physical picture), for a ground-state sea DP:**
1. Are the two CPs' ZBW spin vectors **parallel** or **antiparallel**?
2. Is the DP's arc cohort direction **common to both** (the pair drifts together), or **opposed** (each CP's arcs follow its own orbital motion about the pair centre)?

**F2 holds iff the two answers match in parity** (both flip, or neither). Exact, pointwise cancellation in those cases.

**Stakes.** On a mismatch, R/q = 2 for *every* sea DP, against an intrinsic-EM-parity-violation bound of ~1e−10 — an overshoot of ~2×10¹⁰. No suppression is available: linearity is required and the polarity clause is CPT-forced. **A mismatch refutes χ₄.**

**Note the hazard:** the naive reading of each — antiparallel spins (a spin-paired ground state) and a common drift direction — is one of the two fatal cells. So χ₄ needs the corpus to say otherwise on at least one.

**Doc:** `series_standard_model/axiom_maturation/4106_f2_dp_parity_match.md`. **Verify:** `series_standard_model/code/4106_f2_dp_parity_match.py`. **Lane: EW.**

### TODO-4101-F2 — F2 sea-isotropy framing — **SUPERSEDED at Patch 4106** (registered Patch 4101, EW lane)

The 4101 entry asked whether sea-DP arc directions are isotropic. **Sea isotropy turns out to be irrelevant:** the polarity clause makes the cancellation per-DP and pointwise, independent of the sea's direction distribution. Replaced by TODO-4106-F2DP above.

Patch 4101's cancellation argument extends to F2 **only if** the DP sea's arc directions are isotropic (or antipodally balanced). That is a separate claim from R-F3 and is **not** established. F2 remains CONDITIONAL on SF-6 Reading A (3-space only). Bounded follow-up once R-F3 is answered: does the same pairing argument close F2, or does the sea need its own treatment? **Lane: EW.**

### TODO-4097-R2 — δ_CP ≠ any 600-cell angle: negative result formally filed (registered Patch 4097, EW/SM lane)

**Filed per Thomas's instruction (18 Sep 2026, session 233):** "The R2 negative result on δ_CP should be filed: it rules out the simplest possibility (600-cell geometry) and cleanly redirects F5 to SF-2."

**What is filed:**
- The genuine 120-vertex 600-cell has vertex-vertex angles ONLY at multiples of 36°: {36°, 60°, 72°, 90°, 108°, 120°, 144°, 180°}. The observed CKM phase δ_CP = 65.5° ± 3.3° does not match any of them. Closest: 60° at −1.67σ, 72° at +1.97σ.
- The earlier apparent hit at 66.1° (cos θ = φ/4) was from a 216-vertex non-standard build (all permutations, not even permutations). NOT a genuine 600-cell angle.
- **The simplest derivation route for δ_CP — direct 600-cell vertex geometry — is CLOSED.**

**Locations of the filed result:**
- `series_standard_model/axiom_maturation/chirality_axiom_maturation.md` §2aa (R2)
- `series_standard_model/reasoning/4096.md`
- `frontier_sectors/SM.md` OPEN-SM-11 (references the negative result)
- `frontier_sectors/EW.md` note added at Patch 4097

**Consequence:** F5 derivation belongs entirely to SF-2's generation-transition structure. The two bracketing 600-cell angles (60° and 72°) establish the scale range — the CP phase likely comes from a combination of inter-shell transition angles within SF-2's framework, not from vertex-vertex geometry alone. Lane: SM (SF-2 vehicle).

**Status: FILED AND CLOSED** — the negative result is in the permanent record. No further action needed here; action lives in OPEN-SM-11.

### TODO-4096-SM11 — OPEN-SM-11 registered; SF-2 derivation of δ_CP is now a formal open problem (registered Patch 4096, SM/EW cross-lane)

**What was done:** OPEN-FP-3-CKM from SF-3 §8 (promised to frontier at SF-3's ship time, never entered) is now registered as **OPEN-SM-11** in `frontier_sectors/SM.md`. Thomas's instruction: "open a series and lane to refer to SF-2 for the theorem derivation as to why this CP-violating phase would be present in the Corpus."

**Key finding that motivated this:** The genuine 600-cell has vertex-vertex angles only at multiples of 36°. No angle is within 1.5σ of δ_CP = 65.5° ± 3.3°. The CKM phase does NOT emerge from vertex-vertex 600-cell geometry alone and must come from SF-2's generation-transition structure.

**Next action:** SF-2 lane session targeting the generation-transition mechanism's extension to CKM mixing angles. SF-2 already derives sin²θ_W and α_s from the 600-cell mode spectrum; the CKM matrix is the next natural target. The lane is SM, the vehicle is SF-2.

**F5 gate:** OPEN-SM-11's closure would also close χ₄'s F5 filter (the chirality axiom needs an O(1) phase near 65.5° for CP violation). Until OPEN-SM-11 is solved, no panel on χ₄.

**Lane:** SM (SF-2 vehicle).

### TODO-4094-EW — §15.15 capture audit run late; seven founder captures filed (registered Patch 4094, EW lane)

- **THE HANDOVER PROTOCOL WAS NOT FULLY EXECUTED AT 4093.** Steps A–H ran, but the **§15.15 capture audit did not** — and per CONV-009 it covers **founder verbatim**, not only fragments and scripts. Run afterwards on the founder's prompt: **1 `founders_voice/` capture for 7 founder rulings/ideas/standards**.
- **NOTHING WAS LOST** — the other six were verbatim in `todolist.md` and the maturation document — **but not in CONV-009's designated primary location**. **Fixed at 4094:** seven files created (`0994`, `4064`, `4073`, `4074`, `4082`, `4089`, `4093` in `founders_voice/`), verbatim unaltered, each with what it settled.
- **THIS IS THE EXACT FAILURE §15.15 EXISTS TO CATCH** ("zero founders_voice captures … across an entire session of founder physics"), caught again **only on the founder's prompt** — the second time the OS records that.
- **Step D re-verified file-by-file:** every patch 4063–4092 has a reasoning fragment; 4065/4067 never used; 4093 exempt by content (session close).
- **(1) FOR THE NEXT WINDOW:** treat the **§15.15 capture audit as part of Step E**, not an optional extra, and run it **incrementally** (every ~5 substantive patches) as §15.15 already requires — a close-only net cannot bound loss in a long session. **Lane: EW.**

---

### TODO-4093-EW — Session 232 close: what the next window should take up (registered Patch 4093, EW lane)

- **HANDOVER FILED:** `handovers/2026-09-17_session_232_ew_lane_chirality_axiom_maturation.md` — Steps A–H audit included. Patches 4063–4092 plus 0991–0994. **No verdict moved all session; the axiom is NOT adopted** (founder holds pending a clean win).
- **(a) FRESH-EYES ADVERSARIAL AUDIT of the maturation document — highest value, gates everything else.** Thirty patches of my own reasoning; I chose χ₄, rescued it at 4080, withdrew my own blocking verdict at 4087, and wrote every convenient-branch label. Attack targets named in the handover §5(a): §2q's encoding claim, §2r's "one sign fixes three sectors", and 4082's refutation (the co-moving SSV comparison is the one attack left). **Lane: EW, fresh window.**
- **(b) BOUNDED NEW PHYSICS, sign-independent — THEO-QM-10.** The spin bit gives **two** slots per 3D GP; THEO-QM-10 derives Pauli exclusion and spin-statistics from **one CP per GP**. Rewrite over (3D address, spin bit) pairs. Registered 4076 B5, never attempted. **Lane: QM.**
- **(c) LONG CAMPAIGN — the lattice, CPP's least-tested foundation.** Can BC helices bundle to fill 3-space at z = 12 (4078)? Would bear on 4019/4030/4034 and could retire the 4020 variable-position-GP ruling. **Lane: SR.**
- **(d) THE GATE ON THE AXIOM, not a chirality problem — F5 → CKM.** Needs an O(1) phase near 68.5° **and** the CKM mixing angles (SF-2 generation-transition). **Until that moves, the axiom cannot be completed and no panel should be convened.** **Lane: SM.**
- **(e) NOT RECOMMENDED:** a panel, or adoption. F5 is open by CPP's own zero-parameter standard.
- **SUGGESTED ORDER: (a) → (b) → (c), with (d) whenever the SM lane is live.**
- **NUMBERING TRAP (recorded):** claim the frontier's "Next patch (EW): NNNN" pointer, **not** `next_id`'s "NEXT FREE" — the latter reads one past it. Cost this session: 4065 and 4067 unused.

---

### TODO-4092-EW — the capture gives one plane; motion gives the other and selects helicity (registered Patch 4092, EW lane)

- **CAPTURE CANNOT SELECT A PAIR:** SPIN-1's inner/outer CPs orbit a common axis — coplanar (4090) — so a single-DP capture gives **one** plane; 4091's 60 orthogonal pairs are not selected by it.
- **A SECOND CAPTURED DP IS EXCLUDED, AND BACKWARDS:** SPIN-1 assigns single-DP capture to **fermions**, double-DP to **bosons**; if handedness needed two DPs, only **bosons** could be handed, while helicity and V−A act on **fermions**.
- **SO THE SECOND PLANE IS FORCED TO COME FROM MOTION** — 4089's (4th-axis, travel-direction) leg, now required rather than chosen (4091 made the 4th-axis leg dimensionally unavoidable).
- **THE GEOMETRY SELECTS HELICITY:** pseudoscalar = **2·cos(angle between spin axis and direction of travel)** exactly (+2.000000 at 0°, 0.000000 at 90°, −2.000000 at 180°) — blind to transverse spin. The arc had been *assuming* helicity since 4076; here it is picked out. `code/4092_capture_plane_selects_helicity.py`, `reasoning/4092.md`.
- **SIGN STILL ABSENT:** both hands available (±2.000000). Geometry selects the **quantity**, never the **sign** — unchanged since 4046.
- **ERROR CAUGHT IN-PATCH (10th in arc):** the spin plane built from an arbitrary orthonormal basis has an orientation that jumps with angle — 0° and 180° both gave +2.000000. Fixed by orienting the bivector with the spin axis itself.
- **STANDING:** second plane ✔, frequency ratio ✔, 4th-axis motion ✔, variable ✔ (helicity) — **sign ✘**. Four of five legs on existing structure.
- **(1) NEXT:** every remaining question is either the sign itself or belongs to another lane (F5 → CKM, 4087). **A session close and handover is the natural next step.** **Lane: EW.**

---

### TODO-4091-EW — the 600-cell supplies orthogonal orbital planes; the oscillation is grounded, not replaced (registered Patch 4091, EW lane)

- **DIMENSIONAL FACT:** three mutually orthogonal 2-planes cannot exist in ℝ⁴ (2+2 = 4), so **SPIN-1's three colour planes cannot be mutually orthogonal**. Only a pair can be — and a pair is all a double rotation needs.
- **MY FIRST TEST WAS TOO NARROW AND GAVE THE WRONG ANSWER:** testing complements against only the 12 neighbour directions gave **0 of 66**; complements may be spanned by **non-neighbour** vertices, and widened to all 119 directions the count is **60 of 66**, reproduced at a second vertex. **Verdict reversed.** `code/4091_orthogonal_lattice_planes.py`, `reasoning/4091.md`.
- **ESTABLISHED:** the double rotation can be built from **existing 600-cell geometry** (two orbits in orthogonal lattice planes), with **no new oscillation postulated**.
- **BUT THE FOURTH AXIS IS UNAVOIDABLE:** across all 60 pairs the smallest out-of-3-space component is **0.8507**, never zero — dimensionally forced. **The founder's oscillation is GROUNDED, not eliminated:** orbiting in such a plane *is* fourth-axis motion.
- **THE SIGN IS STILL ABSENT:** both hands occur among the 60 pairs, as at 4063/4068/4071/4074/4078. Geometry supplies carriers, never a choice.
- **AVENUE STANDING:** second plane ✔ (existing geometry); frequency ratio ✔ (derived, 4090); fourth-axis motion ✔ (required, not added); **sign ✘ (not derived)**. **Three of four legs now rest on existing structure.**
- **(1) NEXT, Claude, bounded:** which orthogonal pair does a captured DP actually occupy? SPIN-1 fixes radii but not planes; if its capture geometry selects a pair, the double rotation is fully determined by shipped results. **Lane: EW/QM.**
- **(2) Carried:** F5 → CKM (4087); founder's adoption decision **held**; BC-helix bundling (4078). **Lane: EW/SR (founder).**

---

### TODO-4090-EW — resonance constraint met by a derived ratio; no prediction follows (registered Patch 4090, EW lane)

- **CONSTRAINT MET.** SPIN-1 already contains a **derived** detuned pair: the captured DP's inner CP at r_in and outer CP at 2 r_in orbit with angular-frequency ratio **2√2**, *"not assumed"* — it follows from 1/r² balance and the factor-2 radius. Reproduced exactly (ω ∝ r^(−3/2) ⇒ 2^(3/2) = 2.828427). Pseudoscalar **−5.6564** at that ratio vs **0.0000** at 1:1. **4089's obstruction is removed by a structure the theory already owns.** `code/4090_resonance_constraint_met.py`, `reasoning/4090.md`.
- **BUT NO PREDICTION FOLLOWS.** |pseudoscalar| = **2 × (frequency ratio)** exactly, across 1.05/√2/2/2√2/4. The ratio does no work: 2√2 gives 5.657, nothing distinguished. **Obstruction removed, nothing predicted.**
- **GEOMETRY STILL MISSING.** SPIN-1's two orbits are **coplanar** (common axis), and two coplanar circulations do not make a double rotation (4072). **The detuned pair supplies the timing, not the second plane.** The w-leg remains required and unexplained; the founder's oscillation is still the only candidate.
- **STATUS of the founder's avenue:** second plane — only candidate, unexplained (4089); frequency ratio — available and derived (this patch); **sign — still relocated into a phase convention, not derived** (4089). **Still not a clean win**, which is the standard set for adoption.
- **(1) NEXT, Claude, bounded:** is there any corpus structure with two orbits in **orthogonal** planes? If so the w-leg might be replaceable by existing geometry. Look at the qDP colour planes (SPIN-1's deferred open problem). **Lane: EW/QM.**
- **(2) Carried:** F5 → CKM (4087); founder's adoption decision **held**; BC-helix bundling to z = 12 (4078). **Lane: EW/SR (founder).**

---

### TODO-4089-EW — the fourth axis as an axis of oscillation: worth pursuing, with a constraint (registered Patch 4089, EW lane)

- **FOUNDER'S DRIVER FAILS:** displacement along w is P-even and polarity is P-even, so "polarity drives w-motion" cannot produce handedness (same wall as 4076 B1).
- **THE OSCILLATION SUCCEEDS:** a w-oscillation phase-locked to 3D motion **is** the second rotation plane 4072 showed is the only pseudoscalar carrier — **no new variable** (w exists; the CP circulates). `code/4089_fourth_axis_oscillation.py`, `reasoning/4089.md`.
- **GEOMETRY FORCED:** a **(w, direction-of-travel)** rotation **plus** a **transverse** 3D circulation = **helicity**. (First model used only three dimensions and returned identically zero — correctly; a pseudoscalar needs all four.)
- **RESULTS:** pseudoscalar ∝ **cos(phase)** — maximal in phase/antiphase (±2.8258), zero in quadrature — and **flips with the transverse spin sense**; the hand is (phase) × (spin).
- **SHARP CONSTRAINT:** **zero at 1:1 frequency ratio** (resonance ⇒ simple rotation ⇒ no handedness): 0.0000 at Ω/ω = 1 vs −2.1000/−2.8258/−4.0000 at 1.05/√2/2. **The w-oscillation cannot simply BE the ZBW — it must be detuned.**
- **BUYS:** natural maximality (phase lock, not a tuned angle); a **mechanical** sign (in-phase vs antiphase); and, if polarity fixes the phase, discharge of the CPT-required polarity clause (4085). **DOES NOT BUY:** what fixes the phase for a given polarity — **the sign is relocated into a phase convention, not derived.** Not the clean win the founder is waiting for.
- **(1) NEXT, Claude, bounded:** is there a **detuned** oscillation already in the corpus? SPIN-1's captured-DP orbit (r_in) and the ZBW (Compton scale) run at different scales — if their frequency ratio is fixed by existing results, the resonance constraint is already satisfied or already violated. **Lane: EW/QM.**
- **(2) Carried:** founder's adoption decision **held** at his instruction (wait for a clean win); F5 → CKM (4087); BC-helix bundling (4078). **Lane: EW/SR (founder).**

---

### TODO-4088-EW — owed items cleared: SF-6 check clean, inventory corrected, F5→CKM registered (registered Patch 4088, EW lane)

- **SF-6 FOURTH-AXIS CHECK — CLEAN (owed since 4075).** Full scan of SF-6 (61,144 chars): **zero** references to a fourth coordinate in any derivation; the single "4D" hit is inside SF-6's own OPEN-SD-CHIR-PRIMITIVE problem statement. **Reading A (EM reads 3-space only) is free to adopt — it revises nothing.** F2's condition is satisfiable at zero cost. **Does NOT upgrade F2 to a consequence** (4086: still a specification). `code/4088_sf6_fourth_axis_check.py`, `reasoning/4088.md`.
- **MANIFESTATION INVENTORY CORRECTED (owed since 4071/4084).** `manifestation_inventory.md`: **(iii) EM handedness STRUCK** (a convention with no P-odd content, 4069/4070); **(iv) causal arrow RE-FILED** as T-odd not P-odd (4068), closure under THEO-DSL-3 unaffected. **Three genuine manifestations, not five** — still clears PD-007 (4084). **Lane: SD/SSCA — DONE.**
- **F5 → CKM DEPENDENCY REGISTERED** in `frontier_sectors/EW.md`: the CP-violation filter cannot close inside the chirality arc; it needs an O(1) phase near 68.5° **and** the CKM angles (SF-2's generation-transition problem, 4087). **Lane: EW — DONE.**
- **REMAINING OPEN, all registered:** F5 (reduced to CKM, 4087); F2/F3 (SM-level specifications, 4086); maximality not derived (4083); **founder's adoption decision** (4086). Lattice thread: BC-helix bundling to z = 12 (4078). **Lane: EW/SM/SR (founder for adoption).**

---

### TODO-4087-EW — F5 reframed: 4085's factor-400 verdict withdrawn (registered Patch 4087, EW lane)

- **MY 4085 COMPARISON WAS ILL-POSED.** J = s12·s13·s23·c12·c13²·c23·sin δ_CP = 3.133e-5 (PDG 3.08e-5). The **angle product alone is 3.366e-5 — a 29,706× suppression** — while **sin δ_CP = 0.931 is O(1)**. **J is small because the mixing is small, not because CP violation is weak.** The "δ³ is 400× too large" verdict is **withdrawn**. `code/4087_f5_reframed.py`, `reasoning/4087.md`.
- **THE MAXIMAL-PHASE RESCUE IS EXCLUDED:** sin δ_CP = 1 gives J 9% high, but δ_CP = 1.196 ± 0.044 rad is **8.5σ from π/2**. **No prediction is claimed.**
- **WHAT F5 REDUCES TO:** (a) an **O(1) substrate phase near 68.5°** — not derived, not a free win; (b) the **CKM mixing angles**, which belong to SF-2's generation-transition problem, **not to chirality**.
- **STATUS:** not a χ₄ failure, not satisfied — reduced and re-assigned. **Not panel-ready.**
- **(1) NEXT, Claude:** register the F5 → CKM dependency in SF-2's problem list. **Lane: EW/SF-2.**

---

### TODO-4086-EW — the capture criterion fails; the remaining clauses sized against the SM (registered Patch 4086, EW lane)

- **CAPTURE CRITERION FAILS.** SF-2's own framework **captures in the strong sector too** — quarks confined, Z built as an icosahedral cage (12-vertex first shell), H as a dodecahedral cage (20-vertex second shell), all verified independently here with the 12/20 mass gap. **Capture separates EM from weak+strong, but not weak from strong** — which is the separation F3 needs. My 4085 "most valuable open item" is closed negative. `code/4086_capture_criterion_fails.py`, `reasoning/4086.md`.
- **THE REFINEMENT DOES NOT RESCUE IT:** "only transmuting processes read the bit" names the weak interaction rather than explaining it — the same stipulation reworded.
- **PROPORTION, both ways:** **F2/F3** are **no worse than the Standard Model**, where "only the weak interaction violates parity" is also undeserved — it is the SU(2)-on-left-handed-doublets representation choice. **F5** is **worse than CPP's own standard**: the SM does not predict J either (free parameter), but CPP claims zero free parameters, so leaving J unexplained is a gap by CPP's own bar.
- **STATE OF THE ARC:** every route to a *derived* P-odd source is closed (4046, 4068–4071, 4082). χ₄ + helicity write rule survives as an **encoding**: F6 forces its polarity clause; F8 gives one sign across three sectors; F2/F3 are SM-level stipulations; **F5 is open**.
- **(1) FOUNDER DECISION, when he wants it (not asked this patch):** adopt the axiom with its stipulations (parity with the SM, economical across three sectors), or hold until F5 has a route. **The panel should not be convened until F5 is solved or consciously accepted as open.** **Lane: EW (founder).**
- **(2) F5 — the only substantive item left.** No route in hand. Speculative attack worth trying: can J's smallness come from the ratio of the bracelet's D₆ phase bias to the cage scale, rather than from a power of δ? Bounded. **Lane: EW.**
- **(3) Carried:** SF-6 4th-axis linear-use check (4075); BC-helix bundling to z = 12 (4078); `manifestation_inventory.md` correction (4084). **Lane: EW/SR/SD.**

---

### TODO-4085-EW — CPT forces the polarity clause; F5 fails; the axiom is NOT panel-ready (registered Patch 4085, EW lane)

- **F6 DONE, and it FORCES a clause I had left optional.** b = sign(ω·v) is **P-odd, C-even, T-even** ⇒ **CPT-odd**, so a bare linear term with constant coefficient is **forbidden**; it is allowed only if the coefficient is **C-odd**, i.e. the sign **flips with polarity**. **The 4072 §3 polarity clause is required by CPT, not optional.** With it: P violated, C violated, CP conserved, CPT conserved. `code/4085_f3_f5_f6_readiness.py`, `reasoning/4085.md`.
- **F5 FAILS QUANTITATIVELY.** χ₄ conserves CP exactly, so the observed CP violation needs a separate source. sign(δ) is legitimate and **not circular** (unlike K4, 4082) — but δ³ = 1.32e-2 is **~400× too large** and δ⁹ = 2.28e-6 is **~13× too small** against J = 3.08e-5. **No power of δ reproduces J. Open quantitative problem.**
- **F3 REMAINS A CLAUSE** (as does F2): nothing yet explains why **only** the weak response is linear in b.
- **(1) MOST VALUABLE OPEN ITEM — the capture distinction (Claude, bounded):** does SF-2's centroid **capture** read the captured CP's own register, while SF-6's EM acts through DP-sea **polarisation/exchange** reading displacement magnitudes only? **If so, linearity in b follows from capture and F2 + F3 become consequences instead of clauses.** **Lane: EW/SF-2/SF-6.**
- **(2) F5 — no route in hand.** Registered as open. **Lane: EW.**
- **(3) Falsifier list** — last readiness item, worth writing once F2/F3 settle. **Lane: EW.**
- **READINESS SCOREBOARD:** F1/F1a done; F2 conditional; **F3 clause**; F4 pattern only (maximality not derived, 4083); **F5 FAILS**; **F6 done**; F7 passes; F8 passes (4084); F9 done. **NOT PANEL-READY** — sending it now would spend a round on a proposal with a known open problem and two stipulations.
- **(4) Carried:** SF-6 4th-axis linear-use check (4075); BC-helix bundling to z = 12 (4078, lattice thread); `manifestation_inventory.md` correction (4084). **Lane: EW/SR/SD.**

---

### TODO-4084-EW — F8 PASSES: one sign, three sectors; panel readiness now has four items left (registered Patch 4084, EW lane)

- **THE DECISIVE OBSERVATION:** every closed result under OPEN-SD-CHIR-PRIMITIVE is a **magnitude** — THEO-CAP-1 |M^K3| = χ/6, THEO-SD-CHIR-1 |M^K3| = |M^W| = χ/6. **Neither fixes which hand.** Reproduced: χ = φ⁻³ = 0.236068, χ/6 = **0.039345**, vs the η_B/leptogenesis anchor ≈ 0.04 (1.6%). **χ₄ is not a competitor to Capotauro — it is the missing factor in it.** `code/4084_f8_single_sign_three_sectors.py`, `reasoning/4084.md`.
- **ONE SIGN FIXES ALL SECTORS:** the pairing operations (icosahedral-centre inversion for the W bracelet; combined-CP for qDP/eDP) act with **determinate eigenvalues** — 63/63 flip, 0/63 preserved, never mixed. Each sector's sign follows from its own existing convention: group theory, not a per-sector assumption.
- **SUBTLETY, recorded so it is not read as contradicting 4072:** −I₄ is **proper** in 4D yet flips helicity here, because n̂ is held **fixed** rather than co-transformed (the physically right comparison — the substrate's n̂ does not rotate with the object). Both stand.
- **F8 VERDICT: NOT single-use** — the sign is the missing factor in two **closed** sectors (K3-doublet, V−A) and the **open** cosmological one that already anchors (i) empirically.
- **THE UMBRELLA IS SMALLER THAN IT CLAIMS:** of five manifestations, (iii) EM handedness is spurious (4069/4070) and (iv) the causal arrow is T-odd not P-odd (4071). **Five are really three** — still clears PD-007. **`manifestation_inventory.md` correction owed. Lane: SD/SSCA.**
- **LIMIT UNCHANGED (4083):** χ₄ still **encodes** V−A rather than deriving it. F8 shows the encoding is economical, not explanatory.
- **(1) PANEL READINESS — four items left before the axiom goes to a panel:** **F3** (strong sector stays P-even), **F5** (χ₄ conserves CP exactly; the small observed CP violation needs a source — sign(δ) via CPT is the untested candidate), **F6** (CPT), and the **falsifier list**. Claude, bounded, in that order. **Lane: EW.**
- **(2) Carried:** SF-6 4th-axis linear-use check (4075); BC-helix bundling to z = 12 (4078, lattice thread). **Lane: EW/SR.**

---

### TODO-4083-EW — ω is defined; χ₄ encodes V−A rather than deriving it (registered Patch 4083, EW lane)

- **ω EXISTS for a seeding unpaired CP:** SPIN-1's captured-DP orbit supplies the axis, and the capture *requires* motion, so v exists too. **b = sign(ω·v) is well defined — 4076's B2 write rule survives.**
- **SPIN-1 does not fix the orbital plane's orientation, and must not:** ω ∥ v ⇒ no spin-up/down; ω ⊥ v ⇒ no weak coupling; **free orientation ⇒ ω is the spin state and b the physical helicity.** Measured: ⟨b⟩ = −0.0014 unpolarised (no substrate handedness, V3-consistent) with each particle definite; linear response gives net helicity 1.000 at c = 1 from an **unpolarised** source (= longitudinal polarisation of beta electrons), even response gives zero. `code/4083_omega_defined_and_what_chi4_assumes.py`, `reasoning/4083.md`.
- **THE HONEST ACCOUNTING.** **Derived:** ω exists; v exists; b is P-odd; ⟨b⟩ = 0 for the substrate; linear response reproduces the observed pattern. **Assumed (irreducible):** that the response is **linear** rather than even, and the **universal sign** — which helicity couples. **χ₄ is a faithful CPP ENCODING of V−A, not a derivation of it.** The P-odd primitive is located and housed, not eliminated.
- **(1) NEXT, Claude — F8 for χ₄, now the decisive test:** does the same single sign reach K3-doublet Δp_LR and baryogenesis, or does each sector need its own? **An encoding serving three sectors is worth adopting; one serving only V−A is V−A rewritten.** **Lane: EW/SM.**
- **(2) What would upgrade encoding → derivation (registered, open):** derive why the response is linear rather than even, or derive the sign. **Lane: EW.**
- **(3) Carried:** SF-6 4th-axis linear-use check (4075); BC-helix bundling to z = 12 (4078, lattice thread). **Lane: EW/SR.**
- **ESTIMATOR ERRORS caught in-patch (8th, 9th in arc):** population-count asymmetry instead of the physical observable (reported 1.0000 at zero polarisation); and a 10⁻⁹ threshold against an estimator whose sampling error is 5/√n ≈ 0.008. Both fixed before any conclusion was read.

---

### TODO-4082-EW — K3 REFUTED; the tie-break family is closed; χ₄ + helicity is the survivor (registered Patch 4082, EW lane)

- **FOUNDER ANSWER FILED (17 Sep, verbatim in maturation doc §2p):** momentum absorbed by the bracelet over a few Moments, dispersed randomly on dissolution rather than reconstituted. **Sound physics, and it helps** — the direction is not held as a free vector.
- **BUT conservation puts the momentum into BULK MOTION**, and CPP's absolute (Nexus) frame makes bulk motion substrate-visible at order v/c. Residual **ε ≈ p_captured / M_W** — the founder's mass-ratio suppression, quantified.
- **THE WINDOW IS EMPTY.** ε runs 1.2e-5 (beta decay) → 6.6e-4 (muon) → 1.1e-2 (tau) → 3.1e-2 (b) → **0.50 (top/on-shell W)**, capping register depth at **b < 1.0 bit**, while EM safety needs **b > 10.0** even on an absurd 10⁻³ bound (b > 36.5 on atomic parity violation). **Empty by 9–35.5 bits.** `code/4082_k3_window_empty.py`, `reasoning/4082.md`.
- **STRUCTURAL, not numerical:** V−A is maximal across **five orders of magnitude** of captured momentum. Degeneracy-based mechanisms must weaken as the perturbation grows, so **K3 predicts parity violation fades at high momentum — it does not.** Direct falsification. **The whole tie-break family (K3) is closed.**
- **ONE ATTACK LEFT on the refutation (registered, not pursued):** a reason the bracelet's internal SSV comparison is insensitive to its own bulk motion (a co-moving comparison despite the Nexus frame). Not obviously available in CPP. **Lane: EW.**
- **SURVIVING CANDIDATE — χ₄ with the helicity write rule (4074/4076):** it acts **always**, independent of local symmetry, so it is immune to the failure that killed K3. **Arc returns to it.**
- **(1) NEXT, Claude:** is ω (3D spin axis) defined for a seeding unpaired CP in SPIN-1's construction? Decides the helicity write rule. **Lane: EW/QM.**
- **(2) Claude — F8 for χ₄:** does it reach K3-doublet Δp_LR and baryogenesis, stated once? **Lane: EW/SM.**
- **(3) Carried:** SF-6 4th-axis linear-use check (4075); BC-helix bundling to z = 12 (4078, lattice thread). **Lane: EW/SR.**

---

### TODO-4081-EW — K3 load test passed on SF-2's own construction; one residual is the founder's (registered Patch 4081, EW lane)

- **ESTABLISHED:** ties survive a perturbation iff ε < 2⁻ᵇ (below one LSB it quantises away). Measured: 1.0000 up to ε ≈ 10⁻⁵; dead by ε ≈ 10⁻¹; knee tracks 2⁻ᵇ. Controls: ε = 0 → 1.0000 at every depth (4080 reproduced); ε = 1 → dead at every depth. `code/4081_k3_load_test_incoming_particle.py`, `reasoning/4081.md`.
- **TENSION FOUND (corrects 4080's "deeper is better"):** EM safety wants **deep** registers (leak ~2⁻ᵇ); bracelet ties want the perturbation **below one LSB**, which deep registers make harder. **K3 lives only in the window ε_bracelet < 2⁻ᵇ < Δ_EM.**
- **SF-2 REMOVES THE LEADING OBSTRUCTION:** §5 — the bracelet *"activates when an external charge is captured at its **D₆-symmetric centroid**"* and *"disintegrates statistically per local SSV-gradient probabilities."* A charge at the symmetry centre is a **fixed point of D₆** and does **not** break the symmetry, so the order-unity perturbation is absent by symmetry, and the channel-selecting SSV comparison is exactly where a tie-break would act.
- **(1) FOUNDER PHYSICS QUESTION (picture form) — the residual, and it decides K3:** the captured charge sits at the centroid but it **arrives moving**. Does the bracelet's SSV comparison at the moment of disintegration see only the charge's **position** (which is symmetric — a fixed point of D₆, leaving the ring's twelve contributions exactly equal), or does it also see the charge's **direction of arrival** (which picks out an axis and breaks the equality)? If position only, K3 delivers maximal parity violation with no new variable. If the direction is seen at full strength, there is no window and K3 fails. **Lane: EW (founder).**
- **(2) Carried:** ω for a seeding unpaired CP (4076); SF-6 4th-axis linear-use check (4075); F8 for χ₄; BC-helix bundling to z = 12 (4078). **Lane: EW/SM/SR.**

---

### TODO-4080-EW — K3's EM leak was a model artifact; the real separation is exponential (registered Patch 4080, EW lane)

- **CORRECTION to my own 4079 model.** AP-4 verbatim: the DI-bit imprint is "a STATIC SNAPSHOT of the origin GP's computed registers"; SSV_net = E + S is a **vector sum**; "every GP emits the same fixed number of DI-bits every Moment" — value **nowhere specified**. Degeneracy is equal **SSV_net vector sums**, not equal arrival counts. 4079 measured the wrong quantity.
- **ESTABLISHED:** generic tie rate vs register depth b — 0.177 (b=4), 0.0114 (8), 0.00333 (10), 0.00056 (12), 0.00000 (16); **symmetric rate = 1.0000 at every depth**. Reason: the 600-cell vertex stabiliser is icosahedral and transitive on the 12 neighbours, so an isotropic source gives twelve identical contributions exactly, at any precision. **Separation is exponential in b, not 4079's marginal 7×.** `code/4080_k3_register_depth.py`, `reasoning/4080.md`.
- **K3's EM objection ANSWERED** for any register deeper than a few bits (0.3% leak at b = 10). Requirement softens from "DI-bit counts ≳10³" to "registers deeper than a few bits" — **no tuned parameter**. K3 returns to first place.
- **MODEL ERROR caught in-patch (seventh in arc):** first symmetric model used the same register *vector* at every neighbour — anisotropic, tied 0.24, and the symmetric rate fell with depth (absurd: symmetry is exact). Caught by the control "symmetric rate must not fall with b"; corrected to an isotropic source.
- **(1) NEXT, Claude — the remaining load test of K3:** is the W bracelet's **decision environment** symmetric at the points where the catalytic step chooses, or is the D₆ symmetry broken by the incoming particle? This could still kill K3. Bounded. **Lane: EW/SF-2.**
- **(2) Carried:** ω for a seeding unpaired CP (4076); SF-6 4th-axis linear-use check (4075); F8 for χ₄; BC-helix bundling to z = 12 (4078). **Lane: EW/SM/SR.**

---

### TODO-4079-EW — K3 tested: maximality delivered, EM leak found, requirement quantified (registered Patch 4079, EW lane)

- **ESTABLISHED:** on the 600-cell with integer DI-bit arrivals, tie fractions are **1.0000 symmetric**, 0.8664 ring-with-noise, **0.1427 generic**, 0.0000 continuum control. A3′ C5's "unique assembled metric" governs layer-1 displacement but does not make arrival **counts** non-degenerate. `code/4079_k3_degeneracy_frequency.py`, `reasoning/4079.md`.
- **THE HALF THAT WORKS — first in this arc:** the W bracelet is D₆-symmetric, so every decision inside it is a tie and a chiral tie-break governs **~100%** ⇒ **MAXIMAL violation with no new variable**. Earlier routes capped at ~2% bias (4048).
- **THE HALF THAT FAILS:** 0.1427 in generic configurations ⇒ the same rule biases 14% of EM decisions ⇒ **parity-violating EM**, excluded by 4069/4070. **K3 does not separate the sectors by itself.** My 4078 ranking of K3 first rested on the opposite expectation and was wrong.
- **CONVERTED INTO A QUANTITATIVE REQUIREMENT:** generic tie fraction vs DI-bit dynamic range — 0.878 (0–4), 0.140 (0–40), 0.0054 (0–1000), 0.0007 (0–10 000); symmetric = 1.0000 at every range. **K3 holds iff typical DI-bit counts in ordinary matter are ≳10³** (leak ≲0.5%). Falsifiable against a number the corpus has never specified.
- **(1) NEXT, Claude — does the corpus fix or bound the DI-bit count scale** (SSV_abs register depth, PSR shell occupancy, arrivals per Moment)? **That number decides K3.** Bounded. **Lane: EW/QM.**
- **(2) Carried:** ω for a seeding unpaired CP (4076); SF-6 4th-axis linear-use check (4075); F8 for χ₄; BC-helix bundling to z = 12 (4078). **Lane: EW/SM/SR.**

---

### TODO-4078-EW — routes evaluated: K2 is a lattice proposal, K3 leads for chirality, K4 withdrawn (registered Patch 4078, EW lane)

- **K2 (helical packing) — founder's claim CONFIRMED:** BC stacking uses **perfectly regular** tetrahedra (edge spread 2.5e-13 over 400 cells), so it fits **without stretching** — a genuine alternative to the 4020 variable-position-GP ruling. Deficit recomputed independently: 5 × 70.5288° = 352.6439°, **7.3561°** (4019 confirmed).
- **K2 — the costs, three of them:** (a) twist arccos(−2/3) = 131.81°, irrational, so the helix **never closes or repeats** (0 closures in 10,000) ⇒ **aperiodic; no repeating GP address grid**; (b) a single helix gives **z = 6**, not 12 — bundling helices to fill 3-space at z = 12 is an **open construction**; (c) both hands are valid stackings (torsion ±283.55) ⇒ **supplies a hand, not a choice of hand**. **Verdict: strong LATTICE proposal (belongs with 4019/4020/4034), weak chirality proposal.** `code/4078_evaluate_helix_tiebreak_cpt.py`, `reasoning/4078.md`.
- **K4 — WITHDRAWN as circular.** The C-odd element proposed was the matter excess, but Sakharov's conditions make C and CP violation an **input** to baryogenesis — so it assumes what it should explain. Needs a C-odd element independent of baryogenesis; none on file.
- **K3 — ranked first for chirality**, with a dependency named: the tie-break must be built from **locally available 3D** quantities (an SSV gradient), **not** n̂ (which is the 4th axis, not a 3D vector).
- **RANKING:** (1) K3 tie-break; (2) χ₄ / spin bit (needs helicity write rule + F8); (3) K2 in the lattice thread; (4) K5 weak; K4 withdrawn.
- **(1) NEXT, Claude — does the PCD cycle have genuine degeneracies, and what resolves them today?** Decides K3. Bounded. **Lane: EW.**
- **(2) Claude — can BC helices be bundled to fill 3-space at z = 12?** **CLOSED at Patch 4099.** Fundamental obstruction: BC helix diameter 2r≈1.039 > 1 = required axis spacing for unit bonds. z=12 requires D=1; non-overlap requires D>2r. Mutually exclusive. At D=1: min inter-vertex d=0.320 (overlap). 4020 distortion ruling stands. **Lane: SR/EW — DONE.**
- **(3) Carried:** ω for a seeding unpaired CP (4076); SF-6 4th-axis linear-use check (4075); F8 for χ₄. **Lane: EW/QM.**

---

### TODO-4077-EW — correction to my counting, and four further P-odd routes (registered Patch 4077, EW lane)

- **CORRECTION (mine, to 4071/4073/4074):** under physical parity (3-space inversion), **det₃ of three spatial vectors is P-odd** (20,000/20,000) — 4071's "four directions" was the threshold for the 4D invariant. And "no composite confined to 3-space can be handed" holds for **rotations** (B∧B ≡ 0, stands) but is **false for arrangements** (a fixed cyclic triad: det₃ = +1, mirror −1). **A chiral arrangement in ordinary 3-space is P-odd with no 4th-axis machinery.** `code/4077_other_routes_and_correction.py`, `reasoning/4077.md`.
- **K3 — procedural chirality (cheapest; Claude's pick):** put the hand in the **tie-break rule** for degenerate CP moves — a rule the corpus has never specified. Chiral tie-break gives net P-odd invariant 1.000/step; P-even tie-break exactly 0.000. **No new variable.** Degeneracy is where a binary rule has the all-or-nothing leverage V−A needs (4050). **Lane: EW.**
- **K2 — chiral packing (Boerdijk–Coxeter):** tetrahedra stacked face-to-face form a helix of definite hand (torsion +9.19 / −9.19, sum 0). No new variable; the hand is in the packing. **Connects to 4019** (600-cell cannot tile flat ℝ⁴): the global-lattice question and the chirality question may be the same question. **Lane: EW/SR.**
- **K4 — the CPT route:** P-odd = (C-odd) × (T-odd). CPP has a T-odd element (sign δ, W3); nature has a C-odd fact (matter excess); their product is P-odd if CPT is exact. **No new primitive — the LINK is what is owed.** Most speculative, highest value: would make parity violation a consequence of the arrow of time. **Lane: EW.**
- **K5 — P-odd initial condition:** listed, judged weak (V−A is maximal and exact everywhere; a frozen initial condition would vary or dilute). **Lane: EW (recorded).**
- **(1) NEXT, Claude:** does the PCD cycle have degeneracies, and what resolves them today? Decides K3. **Lane: EW.**
- **(2) Claude:** is the corpus's 600-cell packing helical anywhere? Decides K2 and may bear on 4019. **Lane: EW/SR.**
- **(3) Claude:** attempt K4's link. **Lane: EW.**
- **(4) Carried from 4076:** is ω defined for a seeding unpaired CP (decides the spin-bit repair); SF-6 4th-axis linear-use check. **Lane: EW/QM.**
- **NOTE:** none of K2–K5 has been tested against CPP's actual dynamics. They are candidates, and each could fail as the first four did.

---

### TODO-4076-EW — the founder's spin bit: assessed, repaired, and its QM side effect (registered Patch 4076, EW lane)

- **FILED:** `founders_voice/founder_fourth_dimension_spin_bit_2026-09-17.md` (edited per the founder's standing transcript rule); raw Otter transcript at `founders_voice/raw_transcripts/2026-09-17_...` as provenance only.
- **B1 — as defined the spin bit is P-EVEN** and does not give chirality: a ±1 value attached to an address is a scalar; parity relocates the address, not the value. Same class as polarity (4071).
- **B2 — the repair:** write the bit with **helicity**, b = sign(ω·v) — P-odd in 20,000/20,000 draws. Register, DI-bit transport, majority rule and CP seeding all unchanged; only the write rule changes.
- **B3 — answers the founder's question ("what response?"):** parity violation appears iff the response is **linear** in the bit; an even response gives exactly zero asymmetry even with a P-odd bit.
- **B4:** B3 is 4075's requirement in the founder's variable — **the spin bit is a concrete implementation of χ₄'s 4th-axis carrier**, with DI-bit machinery the corpus already has.
- **B5 — two slots per 3D GP** (Pauli doubling). **Revises THEO-QM-10's basis**, which derives Pauli exclusion and spin-statistics from *one* CP per GP via THEO-1. Not a contradiction of THEO-1 (co-occupation of the same point); THEO-QM-10 would need rewriting over (3D address, spin bit) pairs. **Lane: QM (registered, not attempted).**
- **(1) NEXT, Claude — is ω defined for the seeding unpaired CP** in SPIN-1's captured-DP construction? If not, B2 has no ω and needs a different P-odd write rule. Decides the repair. **Lane: EW/QM.**
- **(2) Claude — F2 follow-up from 4075:** does any shipped SF-6 result use the 4th-axis component linearly? **Lane: EW/SF-6.**
- **(3) Founder, when ready:** adopt helicity as the spin bit's write rule (B2)? **Lane: EW (founder).**
- **(4) NOT ASSESSED at 4076, registered:** the transcript's even/odd address scheme (a position label is P-even by B1, so unlikely to give chirality alone — may bear on exclusion), the orbital-DP-as-artifact suggestion, and the W⁰ bracelet eCP/qCP even–odd relationships. **Lane: EW/SM.**

---

### TODO-4075-EW — axiom maturation step 4: χ₄ passes F2 conditionally (registered Patch 4075, EW lane)

- **RECORD CHECK:** SF-6 never specifies whether the DP displacement is 3D or includes the 4th axis — F2 is a requirement χ₄ imposes, not a lookup.
- **ESTABLISHED:** χ₄'s hand lives entirely in the 4th-axis component (3D remainder ∝ cos sθ, even; 4th-axis part ∝ sin sθ, odd). **Reading A** (EM reads 3-space only): identical fields for both hands, E·B = 1.3e-14 — parity-even, compatible. **Reading B** (4D proximity feedback): E·B = 95.7, flips with hand at −1.0000 — parity-odd, excluded. **F2 passes iff EM reads the 4th axis only through even functions.** `code/4075_chi4_em_parity_filter.py`, `reasoning/4075.md`.
- **REQUIREMENT χ₄ IMPOSES (not a result):** EM reads 3-space; the handed process reads the 4th axis linearly. Would explain why only the weak interaction violates parity *if* the W⁰ step is shown to read the 4th axis (F8).
- **ERROR CAUGHT IN-PATCH (sixth in arc):** first Reading-B run built B = v × E from the modified field, forcing E·B = 0 by construction while the fields differed by 5.7 — a blind control. Fixed by building B from the source's motion. Recorded in the fragment.
- **(1) NEXT, Claude — does any shipped SF-6 result use the 4th-axis component of the displacement linearly?** If none, Reading A is free to adopt; if one, χ₄ fails F2. **Lane: EW/SF-6.**
- **(2) Founder, when ready (not asked yet):** accept "EM reads 3-space; the weak step reads the 4th axis" as part of χ₄'s package? **Lane: EW (founder).**
- **(3) Claude — F8** (does χ₄ reach K3 Δp_LR, W V−A, baryogenesis) and **F3** (strong stays P-even). Unchanged. **Lane: EW/SM.**
- **(4) P-even side effect to track:** Reading A scales the 3D field by cos θ for both hands; a varying θ could be observable. **Lane: EW.**
- TODO-4074-EW item (1) is discharged by this entry.

---

### TODO-4074-EW — axiom maturation step 3: the fourth axis is the carrier; L2 and L3 merge into χ₄ (registered Patch 4074, EW lane)

- **FILED:** founder ruling on the fourth axis (verbatim, maturation doc §2f). Record check: confirmed the corpus gives the 4th axis no physical role. **F1a RESOLVED** — P = diag(+1,−1,−1,−1); S1 (4073) now unconditional. Arc's earlier negatives (4046–4073) stand: achirality does not depend on which improper element is named P.
- **ESTABLISHED:** T1 the P-odd object is a rotation mixing the 4th axis with 3-space, aligned with a 3D spin (e·ω flips exactly). T2 **carrier yes, sign no** — substrate's 4th-axis-mixing rotations: 118 left / 118 right, net 2.6e-14; a rule is still needed. T3 sign(e·ω) = left/right factor in **236/236** ⇒ **L2 (4th-axis form) and L3 are one rule.** `code/4074_fourth_axis_carrier_and_sign.py`, `reasoning/4074.md`.
- **LEADING CANDIDATE χ₄ (draft, doc §2h):** when CP interaction mixes the 4th-axis address with 3-space, the mixing and the 3D circulation align in one sense (left-isoclinic), reversed for opposite polarity. No new variable.
- **(1) NEXT, Claude — F2 (most dangerous):** founder says interaction is processed by proximity, which on a 4D lattice includes the 4th axis. Determine whether SF-6's DP displacement uses 4th-axis proximity and whether χ₄'s rule would then enter EM (excluded by experiment, 4069). Could kill χ₄. **Lane: EW.**
- **(2) Claude — F8 for χ₄:** stated once, does it reach K3 Δp_LR, W V−A and baryogenesis? **Lane: EW/SM.**
- **(3) Open in χ₄'s wording:** is the polarity clause necessary; does the rule apply to all interactions or only some? Decided by (1) and (2). **Lane: EW.**
- TODO-4073-EW items (1) and (2) are superseded by this entry's (1) and (2).

---

### TODO-4073-EW — axiom maturation step 2: founder answers in; three locations for the axiom (registered Patch 4073, EW lane)

- **FILED:** founder answers to Q1–Q3 (verbatim, maturation doc §2c). **F9 RESOLVED** (antiparticle = opposite polarity, nothing else reverses). **Q1/Q2 RESOLVED negative** (no second plane; any spin pole or second plane is an axiomatic addition).
- **CORRECTION:** 4072 said χ "adds no attribute"; **wrong** — it adds a variable. Corrected in the doc.
- **ESTABLISHED:** S1 composites confined to 3-space are never handed (B∧B ≡ 0 for any sum; **conditional on F1a**). S2 handedness = B∧B = 2 e·ω, a helicity-shaped rotation into the 4th axis (3.6e-15). S3 H4⁺ already split into left/right isoclinic factors (±0.789568, swapped by conjugation). `code/4073_composites_substrate_split_axiom_locations.py`, `reasoning/4073.md`.
- **THE DECISION RESTRUCTURED — three locations (doc §2e):** L1 new chirality label; L2 rotation into the 4th axis (founder's "spin pole"); **L3 a rule selecting one of H4⁺'s existing factors — no new variable**. Claude's ranking L3 → L2 → L1, with L3's failure mode (single-use) attached.
- **(1) NEXT, Claude — F1a:** resolve from the corpus how n̂ relates to physical 3-space. Decides S1 and every parity claim in the arc. **Lane: EW.**
- **(2) Claude — F8 for L3:** can a left-factor rule be stated once and reach K3 Δp_LR and baryogenesis, or does it need a separate rule per sector? Decides L3 vs L2. **Lane: EW/SM.**
- **(3) Founder, later:** choose L1/L2/L3 once (1) and (2) are done. Not asked yet. **Lane: EW (founder).**

---

### TODO-4072-EW — chirality axiom maturation (registered Patch 4072, EW lane; living document)

- **WORKING OBJECT:** `series_standard_model/axiom_maturation/chirality_axiom_maturation.md`. Founder direction: mature the axiom fully *before* any panel. Its §6 readiness criteria are the gate. No AP number minted. **Lane: EW.**
- **ESTABLISHED at 4072:** (a) **n̂ vs −n̂ is not a chirality in ℝ⁴** — det(−I₄) = +1 and −I₄ ∈ H4⁺, so the two are congruent by rotation; FI-C-9 *as worded* in CAP-1 scope R1 names no chirality (V3 unaffected — it concerns spontaneous breaking). (b) **A double rotation carries a pseudoscalar, a simple one does not** — B∧B ≡ 0 for one plane (1.8e-15); ±2 for isoclinic SD/ASD; proper-invariant, reflection-odd. 4071's four-directions threshold is right for vectors; its *minimal-form conclusion* missed the bivector route. `code/4072_what_can_carry_handedness.py`, `reasoning/4072.md`.
- **CANDIDATE χ (draft):** the ZBW is a *double* rotation whose relative sense (SD/ASD) is fixed by polarity. Adds no attribute; specifies the existing ZBW. Truth table gives P violated, C violated, CP conserved — the weak pattern *by form*, not derived; predicts CP *exactly* conserved (nature: small violation), so a second source is owed.
- **(1) FOUNDER QUESTIONS (picture form) — Q1–Q3 in the maturation doc §5:** Q1 does the ZBW circulate in one plane or two at once? Q2 if two, do + and − CPs turn the same or opposite way in the second plane? Q3 is a CP's antiparticle just opposite polarity? **Lane: EW (founder).**
- **(2) BLOCKING — F1a: define physical parity in CPP's 4D setting.** Every P-odd claim in this arc (4046–4072) used Θ-type reflections as a proxy. Claude, next. **Lane: EW.**
- **(3) BLOCKING — F9: verify CPP antiparticle = polarity-reversed CP** against A1′ and the corpus. χ's CP argument depends on it. Claude, next. **Lane: EW.**
- **(4) F2/F3:** show the second ZBW plane does not enter the EM or strong force laws (else χ makes them P-odd — excluded). **Lane: EW.**
- **(5) F5:** test sign(δ) as the small-CP-violation source via CPT. **Lane: EW.**
- **(6) F8:** derive one of K3 Δp_LR / W V−A / baryogenesis under χ far enough to give a non-trivial sign or number. **Lane: SM/EW.**
- **(7) NUMBERING NOTE:** `next_id.py` counts the frontier "Next patch: N" pointer as a reservation, so its "NEXT FREE" reads N+1. Claim the pointer number itself. This fully explains the unused 4065 and 4067. No tool bug. **Lane: EW (recorded).**

---

### TODO-4071-EW — the P-odd search is exhausted; a P-odd axiom is required and is NOT single-use (registered Patch 4071, EW lane)

- **CLOSED at 4071 — internal CP/DP structure does not avoid an axiom, it IS one.** Counting theorem: in R⁴ the only P-odd scalar from vectors is det[a,b,c,d], so a CP needs **≥ 4 independent internal directions** to carry any P-odd quantity. Verified: k = 1, 2, 3 give pseudoscalar **identically zero** (20,000 draws each); k = 4 gives 6.95e+01, flipping exactly under reflection. Polarity scalars (±) are P-even and cannot help. **This rederives 4046 generally** — n̂ fails because one vector is three short, not by luck. And lattice-derived quadruples give **80 positive / 80 negative**, ensemble sum −2.8e-17: the 600-cell supplies magnitude but **no net sign**. `code/4071_internal_cp_structure_needs_four_directions.py`, `reasoning/4071.md`.
- **SEARCH EXHAUSTED — all four routes closed:** n̂ static (4046), Mechanism A δ-tilt (4068), EM/magnetism (4069/4070), internal CP structure (4071). U (4063) remains but is *also* an axiom (its handedness is set by fiat) at 61× sites. **Structural finding: CPP's axiom set contains no P-odd element, and no combination of its P-even elements manufactures one** — consistent with STATUS-2. δ is a scalar tilt (enough to break T); breaking P needs a pseudoscalar (four directions the substrate lacks).
- **(1) FOUNDER DECISION — the axiom, and its scope (answers his question directly).** SF-6's `OPEN-SD-CHIR-PRIMITIVE` names five manifestations a single chirality primitive must cover. **Two must be struck:** *(3) EM handedness* is spurious — a convention with no P-odd content (4069/4070); *(4) thermodynamic causal arrow* is **T**-odd, not P-odd — it is sign(δ) at W3 (TARROW-1/2, 4068), misfiled here. **Three genuine, disjoint P-odd targets survive, and they are NOT all W⁰:** *(i)* K3-doublet chirality / Capotauro Δp_LR (mass-mixing), *(ii)* W-bracelet V−A (electroweak), *(iii)* baryogenesis / matter–antimatter (cosmological). **So a P-odd axiom is not single-use** — it is load-bearing in three disjoint sectors, which is exactly PD-007's criterion for a legitimate carried-across-phenomena primitive. **Minimal form:** the CP carries a pseudoscalar sign not derived from the lattice (a fourth internal direction with primitive sign, or a primitive ± entering the PCD cycle with opposite sense). No new particle, no new field, no change to the 600-cell. **Lane: EW (founder).**
- **(2) SF-6 REVISION OWED:** `OPEN-SD-CHIR-PRIMITIVE`'s manifestation list should drop item 3 (EM handedness, spurious) and re-file item 4 (causal arrow) under the T-arrow. Paper edit, not a verdict move. **Lane: SM/SF-6.**
- **(3) CONV ROUND PROPOSED, not dispatched:** the claim *"CPP's axiom set contains no P-odd element; four routes to manufacturing one are closed"* is a negative theorem with corpus-wide reach and is panel-worthy under the review economy. It proposes an axiom change ⇒ founder's call under PD-006/PD-008. **Lane: EW (founder authorises).**
- **(4) IF the axiom is adopted, attempt K3/Δp_LR first** — the most quantitative of the three targets and the least entangled with unresolved structure; V−A maximality and baryogenesis magnitude are separate derivations that could each fail. Not claimed, registered. **Lane: SM.**

---

### TODO-4070-EW — the right-hand rule is a convention, not a clue; the EM→weak bridge is closed both ways (registered Patch 4070, EW lane)

- **ANSWERED (founder question, 16 Sep):** *"the cross product only obeys the right-hand rule... Where does that come from?"* → **From our definition of B.** Magnetostatics rebuilt end-to-end left-handed (B_L = −(v×E), Lorentz flipped to match) gives **bit-identical** forces: charge-charge, element-element, and force-on-loop-element all 0.000e+00 over 5,000 random configs each. B is produced by one cross product and consumed by another; every observable has two, so the handedness cancels. **Decisive:** the same force is expressible with **no cross product at all** (antisymmetric tensor / SF-6's bivector — an oriented plane, no hand to choose), agreeing to 7e-15. A real asymmetry is not removable by notation. Control: E·B flips sign under a *true* mirror, so the test sees real parity when present. `code/4070_right_hand_rule_is_convention.py`, `reasoning/4070.md`.
- **FOUNDER'S TWO PROPOSED BRIDGES, BOTH CLOSED.** *(a)* "derive the right-hand rule for DP-Arc motion, then extend it to W⁰ parity violation" → a derivation of a **convention** has no P-odd content to extend; and if it produced any, it would contradict experiment (4069). *(b)* "perhaps the EM right-hand rule falls out of W⁰ handedness" → a physical asymmetry cannot source a notational one; if weak interactions fixed the EM convention's sign, that would be an observable P-odd EM effect, which is excluded. **Lane: EW (closed, no action).**
- **ERROR RECORDED (caught in-patch):** my first loop test compared the **torque vector** across conventions and it appeared to flip (3.97e+02). Invalid — torque is itself axial (r × F) and flips with the convention like B does; I was comparing notation to notation. Corrected to the force on each current element (polar, measurable). Fifth instrument error in this arc caught by a category check rather than by the number.
- **UNCHANGED AND STILL THE LIVE ITEM:** the last free P-odd candidate — **internal CP/DP orientation beyond n̂** (SF-6 `OPEN-SD-CHIR-PRIMITIVE`), TODO-4069-EW (1)(a). Bounded, unassessed, costs nothing. Claude's recommendation stands: run it before the founder decides between a P-odd axiom and U. **Lane: EW.**

---

### TODO-4069-EW — the P-odd source: three candidates closed, two left (registered Patch 4069, EW lane)

- **CLOSED at 4069 — EM/DP-sea magnetism is NOT a P-odd source, and cannot be.** SF-6's mechanism (B = curl of the DP displacement whose radial part is E) makes B axial *because* it is a curl of a polar field. Mirrored sources reproduce the axial transport of B to 1e-12; the P-odd invariants v·B and E·B **vanish identically** for a moving charge (B = v×E ⊥ both), over 20,000 random configurations. Control with E ∥ B gives E·B = 1.000, so the test sees P-oddness when present. **The right-hand rule is the bookkeeping of a curl, not a handedness**; parity violation lives in the weak sector, which is why the arc kept landing on the W bracelet. `code/4069_em_right_hand_rule_is_p_even.py`, `reasoning/4069.md`.
- **SCOREBOARD of P-odd candidates:** Mechanism A δ-tilt → REFUTED (4068). n̂ static → REFUTED (4046). EM/magnetism → REFUTED (4069). **Remaining: (a)** internal CP/DP orientation beyond n̂ (SF-6 `OPEN-SD-CHIR-PRIMITIVE`), unassessed; **(b)** chiral GP arrangement U (4063), costed at 61× sites; **(c)** an axiom-level rate law coupling to an oriented volume — founder 16 Sep: *"there is no provision for rate law coupling. This would require a deep axiomatic modification of the theory. This may be necessary."*
- **(1) FOUNDER DECISION, framed (the fork the arc has reached):** every P-even object in the corpus has now been tested and every one is P-even; the corpus has a T-arrow and **no** P-source, consistent with STATUS-2 (no P-odd pseudoscalar in the present axioms). So the choice is: **(i)** accept a P-odd primitive as an additional axiom (sign(n̂) promoted from V3-gap to postulate, the "deep axiomatic modification" — honest, and matches how the SM treats V−A as structural); **(ii)** adopt U, buying chirality geometrically at 61× sites; or **(iii)** keep searching internal CP/DP structure (candidate (a)) before conceding. **Claude's recommendation under PD-006: assess (a) first** — it is bounded and free, and SF-6 already names it; then decide (i) vs (ii) with the search exhausted. **Lane: EW (founder decides; Claude can run (a)).**
- **(2) Physics pointer, not a result:** in the SM parity violation is a property of the weak coupling structure, not of space or EM. If CPP reproduces that, the P-odd element should be expected in the W bracelet's environment rather than in substrate geometry — an argument for candidate (a) and against (b). Recorded as reasoning, **not registered as a finding**. **Lane: EW.**

---

### TODO-4068-EW — the chirality mechanism has lost its candidate: what in CPP is P-odd at all? (registered Patch 4068, EW lane)

- **SETTLED at 4068:** Mechanism A **cannot** split the W bracelet. Θ = diag(1,1,1,−1) is an exact improper symmetry of the whole dynamics (Q Θ-equivariant to 1.8e-15, π Θ-invariant to 2.5e-17, every δ incl. φ⁻³), because the rates depend on geometry only through e·n̂ and Θ fixes both. The helicity is Θ-odd ⇒ splitting identically zero (max|Δ| = 1.5e-17 vs circulations 1.0e-5). **δ breaks T, not P.** `code/4068_mechanism_a_cannot_split_the_bracelet.py`, `reasoning/4068.md`.
- **(1) FOUNDER PHYSICS QUESTION (picture form) — the live one:** a P-odd source must distinguish a configuration from its mirror image. Mechanism A's tilt along n̂ is P-even. **Is there anything in the CPP axioms that is P-odd?** Three candidate directions, none assessed: **(a)** a rate law coupling to an oriented *volume* — a triple product of edge vectors with n̂ — which is Θ-odd, unlike e·n̂ (an axiom-level change to Mechanism A, founder's call); **(b)** the DP/CP internal structure: do CPs carry an orientation beyond n̂ that a mirror would flip (SF-6 `OPEN-SD-CHIR-PRIMITIVE`)? **(c)** a chiral GP arrangement — U (4063), costed at 61× sites. **Lane: EW (founder).**
- **(2) 4066's "cheaper candidate route" is REFUTED.** 4064 reason #1 is gone; the case against promoting U now rests only on reasons #2 (61× sites, second length scale) and #3 (geometry supplies a sign, not V−A maximality). If (1)(a) and (1)(b) both fail, U returns as the only identified P-odd source and should be re-weighed at that known price. **Lane: EW.**
- **(3) ERRATUM to 4050 (filed at 4068):** 4050 states all 63 rings through a host vertex carry |h| = 1/(2φ). **False** — |h| = 1/(2φ) on 21 of 63, and 0.269672 on the other 42; the magnitude was read off one ring and generalised. P-oddness and the Θ-flip (what the argument needs) are unaffected. SF-2 unrevised; no verdict moved. **Lane: EW (recorded, no action).**
- **(4) Unaffected:** the *status* question (FI-C-9 = V3; why sign(n̂) has its sign) stays OPEN-CHIR-1d-β, deep and deferred. TARROW-1/2 stand — this patch confirms the T-arrow, it only denies it is also a P-source. **Lane: CHIR (pointer only).**

---

### TODO-4066-EW — the W⁰ handedness splitting: the live chirality mechanism question (registered Patch 4066, EW lane)

- **CONTEXT / ERRATUM.** My chat summary at 4064 said the corpus "already carries handedness through the CPs' own orientation." **Wrong** — 4046: Θ fixes n̂, so (600-cell, n̂) is achiral; a vector is not a chirality. FI-C-9 = sign(n̂) is at **V3 = not yet derived**, a registered gap, not a working mechanism. Founder caught this. The *status* question is closed (V3/W3, CAPACITY-1); the **mechanism** question — what carries handedness into observable physics — is **OPEN and lives in EW**.
- **(1) SPLIT THE DEGENERATE PAIR** (Claude, bounded, next EW computation): 4050 showed the W bracelet's two helicity states (ring bivector ∧ centroid ∧ n̂, |helicity| = 1/(2φ)) are **P-odd and exactly degenerate** under Θ, and that **the splitting is not computed** — "nor by how much, nor with which sign." Embed the bracelet in a Mechanism-A environment (Q = L + δC, δ = φ⁻³) and compute the induced difference between the two states: sign, magnitude, and δ-scaling (δ or δ³). No new GPs needed. **If it splits:** substrate δ → bracelet helicity → V−A sign; a win, CONV round warranted (maximality still owed to the gauge-structural argument, 4048). **If not:** Mechanism A is insufficient and U returns at its known price (4064). **Lane: EW.**
- **(2) Does the W state carry this variable at all?** 4050 flags that SF-2 describes the W⁰ as a catalyst activated at a D₆-symmetric centroid, **not** as a helicity state. Whether SF-2's catalysis uses the split variable is SF-2's to say. Second unclosed link, distinct from (1). **Lane: SM/SF-2.**
- **(3) Not closed by (1) or (2):** the *status* question — why sign(n̂) has the sign it has — stays OPEN-CHIR-1d-β (deep, deferred). Settling W⁰ handedness closes the mechanism chain, not the origin of the primitive. **Lane: CHIR (pointer only).**
- **(4) 4064 reason #1 CORRECTED:** "not needed — the corpus already has a reviewed route" → "the corpus has a **cheaper candidate** route (dynamical P-odd δ-term vs 7,200 GPs) **whose decisive step is unexecuted**." 4064's recommendation (do not promote U) stands on reasons #2 (61× sites, second length scale) and #3 (geometry gives a sign, not maximality). **Lane: EW.**

---

### TODO-4063-EW — after the chiral 4D cluster: helicity measurement, and whether U is a physical candidate (registered Patch 4063, EW lane)

- **(1) 4D graph helicity on U** (Claude, bounded): repeat 4047's path-chirality measurement on U's decoration graph (7,200 points, ~10⁵ short paths — 4054's density requirement is met). Report sign, magnitude, mirror-flip, and the structural bias fraction against 4048's 3D cap of ~2%. **Lane: EW.**
- **(2) CLEARED at 4064 — founder ruling (verbatim in `reasoning/4064.md`):** no condition restricts GP count per cell; decoration points = additional GPs, acceptable; interpolations between GPs would require reworking. **Claude's recommendation under PD-006: do not promote U** — decoration-as-GPs costs 61× the sites and a second length scale (spacing 0.11–0.19 vs 0.618, coordination 2), buys no phenomenon, and cannot reach V−A maximality (4048); the reviewed route (n̂ primitive + sign(δ) arrow, chiral dynamics on an achiral lattice) stands. U kept as an existence result with a price tag. No CONV round. **(1) demoted to optional** for the same reason.
- (original text of (2):) **Founder physics question, in picture form:** U needs a 7,200-point decoration per 600-cell, on no mirror of the cell. Can the substrate's constituents (CPs/DPs per GP) supply that many distinct positions, or is the handedness carried some other way (e.g. by n̂ + sign(δ) alone, per CAPACITY-1/TARROW-1)? If U-like, a CONV round promotes U to a corpus object; if not, U is a mathematical existence result only. **Lane: EW (founder).**
- **(3) The global lattice** stays where 4019/4030/4034/4037 left it: no flat-R⁴ tiling of 600-cells with z = 12; the 7.356° deficit is the cause. Chirality no longer blocks it; tiling does. Not an EW item — SR/SM. **Lane: SR (pointer only).**

### TODO-4054-EW — a third consecutive non-landing, and a stop (**CLEARED at 4063**)

- **THE ATTEMPT:** lift 4041's verified 3D chiral orbit into 4D by **conjugation** (x → q x q̄), which fixes
  the real part and acts as SO(3) on the imaginary part.
- **IT DOES NOT LAND, twice over.** (i) The supposed **5-fold-axis seed also gives a 60-point orbit** where
  3D gives 12 — **my special positions are not where I think they are in the conjugation frame**, so there
  is no working 3D → 4D lift yet, only an unaligned map. (ii) The resulting 60-point shell has only
  **~120 4-hop paths** — **4041's failure repeated exactly: a zero that means "I cannot see", not "there is
  nothing there".** I recognised that trap at 4041, wrote it up, **and built it again.**
- **THIS IS A THIRD CONSECUTIVE NON-LANDING, AND THAT IS THE SIGNAL.** 4051 both functionals wrong →
  retracted at 4053; 4052 diagnosis partly true but the wrong reason; 4053 retraction; 4054 this.
  **The last four patches have produced one retraction and no result. The lane should stop here rather
  than produce a fourth — continuing past this point is how a second retraction gets made.**
- **WHAT IS ACTUALLY ESTABLISHED, for whoever picks this up:**
  - SF-6's `OPEN-SD-CHIR-PRIMITIVE` names **n̂-on-a-host-vertex** as leading candidate; **it cannot work** —
    Θ fixes n̂ and preserves the 600-cell (4046).
  - A chiral cluster with icosahedral **rotation** symmetry and an achiral z = 12 first shell **exists and
    is measured — in THREE dimensions** (4041, 4042, 4047), and it **preserves the icosahedral and
    dodecahedral shells CPP uses** (4043).
  - Its parity-odd dispersion enters at **O(k¹⁵)** — not excluded by the absence of vacuum optical
    activity, and **not calibratable** by it (4044, 4045).
  - A structural helicity bias **caps at ~2%**, so it **cannot supply V−A's maximality** (4048).
  - The **W bracelet is achiral**, by the corpus's own Theorem 4.2 and independently (4049).
  - **Ring-bivector ∧ n̂ IS the P-odd binary variable**, and its two states are **exactly degenerate** under
    the present symmetry (4050).
  - **NO CHIRAL 4D STRUCTURE HAS BEEN BUILT.** Everything chiral here is 3D (4053, 4054).
- **CLEARED at 4063 — TARGET MET.** U = 600-cell ∪ generic H4⁺-orbit (7,200 pts, radius 1.7): symmetry group exactly H4⁺ by exhaustive count over all 7,200 improper elements; z = 12 on every core vertex; pseudoscalar ±43.04, flips exactly, control 0. Steinberg: every H4⁺-orbit of a mirror point is achiral, which is why 4051–4054 could not land; 7,200 per shell is the minimum. `series_standard_model/code/4063_chiral_4d_cluster_z12.py`, `reasoning/4063.md`.
- (original text retained:) **THE GAP IS DIMENSIONAL AND IT IS THE WHOLE REMAINING PROBLEM:** a chiral 4D point set with icosahedral
  rotation symmetry, **tested with the 4D graph helicity on a graph dense enough to resolve it.** Both
  halves are requirements; **this patch met neither. Lane: EW.**

---

### TODO-4055-EW — 4022's owed extension discharged; first debt cleared since the chirality line stopped

- **A DIFFERENT ITEM FROM THE QUEUE.** The chirality-construction line stopped at 4054; this is an
  unrelated debt from 4022.
- **RESULT:** RP's verdict is **identical at m = 1, 2 and 3**, and the Gram structure is **m-independent** —
  rank one at every m, symmetric exactly when π is Θ-invariant. **4022's "necessary only" becomes
  "necessary and sufficient within all product observables".**
- **WHY IT IS CLOSED-FORM AND NOT SAMPLED:** Θ maps the + side to the − side, so every index in
  ⟨(ΘF)(F)⟩ is **distinct** and the multinomial's coincidence terms **never enter**. The moment is exact.
- **STILL OPEN: the non-product classes** — repeated indices, functions of sums. **Where a counterexample
  to RP would have to live. Lane: EW.**
- **Nothing downstream changes:** 4023 and 4024 rest on RP holding in the n̂-preserving sector, now
  established on a **strictly larger class** than before.

---

### TODO-4056-EW — [DOWNGRADED AT 4062: fails on an ISOLATED 600-cell by O(1/K) only; "δ = 0 untouched" withdrawn] H1 FAILS. The counterexample 4055 predicted, found where it predicted.

- **4055 named the non-product class as the only place a counterexample could live. Looked there. FOUND
  ONE.**
- **THE ALGEBRA.** n_i² = (n_i)₂ + n_i, so for i ≠ j:
  E[n_i²n_j²] = K⁽⁴⁾p_i²p_j² + K⁽³⁾(p_i²p_j + p_ip_j²) + K⁽²⁾p_ip_j. For F = Σ w_a n_a² on the + side,
  ⟨Θ(F)F⟩ = K⁽⁴⁾s² + 2K⁽³⁾st + K⁽²⁾t², **PSD iff K⁽⁴⁾K⁽²⁾ − (K⁽³⁾)² ≥ 0.**
  **That equals −K²(K−1)²(K−2) — negative for every K ≥ 3, and INDEPENDENT of p.** The indefiniteness is
  in the **multinomial itself**, not in the measure.
- **AND ON THE REAL MEASURE, IN THE n̂-FIXING SECTOR, IT BITES.** Gram minimum eigenvalue: **δ = 0 → PSD**
  (the measure is uniform, p² ∥ p, the indefinite form is never probed); **δ = 0.10 → −5.44e-03;
  δ = 0.35 → −4.74e-02.** **Explicit witness:** a single F gives **⟨Θ(F)F⟩ = −2.02e+02**. One F suffices.
- **⇒ H1 IS FALSE ON [PCD-EXT] FOR δ > 0, IN BOTH SECTORS.** 4022 found failure for n̂-**flipping**
  reflections; it fails for n̂-**fixing** ones too, on the class 4022 did not test and 4055 explicitly
  named as untested.
- **WHAT IT COSTS.** **4055's strengthening stands but is the smaller half** — "necessary and sufficient
  within all *product* observables" is still true; the product hierarchy was simply the wrong place.
  **4023 is UNDERMINED**: its *VW-1's conclusion survives restricted RP* has no RP left to be restricted
  to. **4024's finite-substrate strengthening SURVIVES** — E[⟨η⟩] = 0 by exact symmetry of the generator,
  and **that argument never used RP.**
- **δ = 0 is untouched:** RP holds there in both sectors. **The failure is entirely a NESS effect** — the
  same place 4022 found the flipping-sector failure.
- **NOT CLAIMED: that the DSL measure fails RP.** `[PCD-EXT]` is 4004's **working extension**, and every RP
  result in this arc is about it. **What is established: the working extension does not satisfy H1, so it
  cannot be used to discharge it. Lane: EW / CHIR — VW-1's holder should see this.**

---

### TODO-4057-EW — [CONCLUSION WITHDRAWN AT 4062: H1 is OPEN, not false] WHY H1 fails: CP conservation. The fix exists and the founder's ruling forbids it.

- **THE CAUSE.** 4056's indefiniteness was **p-independent**, so it lives in the **multinomial**, not the
  physics. A multinomial has a **fixed total K** — a **non-local constraint**, the classic way to break
  reflection positivity. **Tested the grand-canonical version (independent Poisson):** in the n̂-**fixing**
  sector Poisson is **PSD at every δ** (−2.2e-13, −5.8e-13) against multinomial's **−5.44e-03, −4.74e-02**.
  **So the n̂-fixing failure IS caused by the fixed total.**
- **But the n̂-FLIPPING failure SURVIVES the change** (Poisson −9.32, −85.2): that one is a **genuine
  Θ-asymmetry of the measure**, not a constraint artifact.
- **AND THE FIX IS RULED OUT BY THE FOUNDER'S OWN REGISTERED RULING.** GR-FE-1 (19 Aug 2026): *"The GPs,
  the CPs, and DI-bits are all conserved"*; `T2_T3_uniqueness_and_source.md` records it as the registered
  picture, **"CPs are conserved"**. **So the fixed total is PHYSICAL.** The Poisson measure is not a better
  model of the same physics — **it is a model of different physics.**
- **⇒ H1's FAILURE IS REAL, NOT AN ARTIFACT.** 4056 stands; **4023 stays undermined; 4024 stays standing**
  (its argument never used RP).
- **THE SHAPE OF THIS IS ON RECORD.** The convenient answer was **available and correct-looking** — Poisson
  restores RP exactly where it was needed — and I could have written *"the failure is a modelling artifact,
  replace [PCD-EXT]"* without checking admissibility. **The check that killed it was a corpus search, not a
  computation: the computation SUPPORTED the convenient reading.**
- **FOR VW-1's HOLDER, and it is worse news than 4056's:** RP on the physical measure fails in **both**
  sectors for δ > 0; the n̂-flipping failure is intrinsic and the n̂-fixing one is **caused by CP
  conservation, which is axiom-level and cannot be traded away for RP.** **H1 is not merely unproven — on
  the physical measure it is FALSE, and no occupation model respecting CP conservation will do better.**
  **NOT claimed:** that no positivity condition survives — only that **reflection** positivity, on the
  squared class, does not. **Lane: CHIR (VW-1's holder).**

---

### TODO-4058-EW — H1's refutation does NOT reopen V1; and 4023's η defect lands on CAPACITY-1's piece 1

- **THE WORRY, CHECKED.** After refuting a theorem's sole residual, the natural question is what falls with
  it. **CAPACITY-1's conditionality, narrowed at 0960, names three things:** MA.1's reversal-odd first
  harmonic (derived and unique up to scale, 0949); **per-edge independence**; and **pointwise
  non-degeneracy of the dynamical η** (piece 1, still assumed). **None of them is reflection positivity.**
- **⇒ 4057 DOES NOT REOPEN V1.** H1 was **VW-1's** residual; VW-1 and CAPACITY-1 are **different theorems
  reaching a compatible conclusion by different routes**. Refuting H1 removes VW-1's support and leaves
  CAPACITY-1 untouched. **V1 stays EXCLUDED; V3 stays CONFIRMED.** And 4005's direct measurement — χ_η
  finite, d ≥ 1 correlations ~1e-3 — is a **third leg**, independent of both theorems.
- **BUT CAPACITY-1's THIRD CONDITION IS THE ONE 4023 FOUND DEFECTIVE.** *Pointwise non-degeneracy of the
  dynamical η* — and 4023 established that η's 4th/5th projections **tie at 120/120 vertices on the
  unperturbed lattice** (re-verified here), so η is **pointwise degenerate** there.
- **The condition HOLDS where CAPACITY-1 uses it** — perturbation breaks the ties at all three amplitudes
  tested, and 0813 and 4005 both evaluate η on perturbed configurations. **No result is invalidated.**
- **But the statement carries no "on perturbed configurations" qualifier.** 4023 found that defect **without
  knowing it landed on a named conditionality of a 3/3 review-closed theorem.** More consequential than
  4023 reported — not because anything is wrong, but because **the assumption is now known to be FALSE in
  the unperturbed limit and the theorem does not say so.**
- **Filed for the CHIR lane as a TEXT fix, not a physics one:** add the qualifier to piece 1. **NOT this
  lane's to edit — CAPACITY-1 is review-closed. Lane: CHIR.**
- **AND THE ABSENCE GATE FORCED A SEARCH THAT FOUND SOMETHING LARGER.** The draft said *"VW-1 and H1
  appear nowhere in it"* — true of CAPACITY-1's conditionality, but the gate required it **unscoped**, and
  **H1 turns out to be load-bearing where I had not looked.** `reviews-SF2-DELTACP-SCOPING.md` records
  Copilot's verdict: ***"CONDITIONAL-GO — viable only if SQ1 salvage or H1 closes within ~10 sessions"***,
  and the adjudication judges the **other** contingency *"near zero"*. **So H1 was effectively the
  surviving contingency for proceeding on δ_CP. 4057 closes it NEGATIVELY** — H1 does not close; on the
  physical measure it is **false**. **That is a decision input SF-2's lane should have. NOT this lane's
  decision to revise. Lane: SF-2 / founder.**
- **The gate is why this was found.** The computation and the CHIR.md reading were both correct and both
  scoped; only the unscoped search reached the review package. **Third time today a gate or control
  produced the patch's most consequential line.**

---

### TODO-4059-EW — ["both contingencies refuted" WITHDRAWN AT 4062: they are OPEN] 4058 overstated it; the accurate consequence is sharper. BOTH δ_CP contingencies reduce to H1.

> **SF-2 NOTICE (Patch 0987, CHIR lane; closes TODO-0984-CHIR (3)).** The δ_CP long-horizon contingency was written (June 2026) as *H1 reflection-positivity*, i.e. the **VW route** to the capacity bit sign(μ²). Two things have happened since. (i) **THEO-CHIR-CAPACITY-1** (0927, 3/3; narrowed 0960) closed that same bit by a different route — *no det-coset condensation ⇒ μ² > 0* — conditional on MA.1's first harmonic, per-edge independence, and η non-degeneracy on perturbed configurations (0986). (ii) The VW route is **inapplicable as posed** (0984/0985; VW-1 v1.5). **So δ_CP's contingency should no longer be stated as "H1"; the capacity bit is CAPACITY-1's, under CAPACITY-1's conditions**, and H1's status (OPEN ⟺ VW-a-4) is irrelevant to it. The 2028+ plan is parked; this notice changes what it is contingent on, not whether it is parked. **Lane: SF-2, at un-parking.** Everything below is the 4059/4062-era text, retained.

- **4058 SAID 4057 "settles a go/no-go question that was left open". WITHDRAWN.** The adjudication says
  otherwise in its own words: **"Adopted verdict: RESTATEMENT-NEEDED"**, *"Grok's framing is adopted as the
  more accurate one"*, and the SQ1 probability already judged **"near zero"**. **The decision was made
  before this session started.** I read a reviewer's verdict line and not the adjudication three lines
  below it — the same shape as 4049, where I read SF-2's theorem statement twice without registering what
  D₆ meant. **Reading the right document is not the same as reading enough of it.**
- **BUT THE ACCURATE CONSEQUENCE IS SHARPER, NOT SMALLER.** δ_CP was **retained as a long-horizon target**:
  *"δ_CP becomes a LONG-HORIZON TARGET (2028+, contingent on **H1 reflection-positivity + OPEN-SM-4
  sub-claim (a)/(b) closure**)"*.
  - **Contingency 1 — H1 reflection-positivity: REFUTED at 4057**, with the cause (CP conservation) being
    axiom-level.
  - **Contingency 2 — OPEN-SM-4 sub-claim (a)/(b): reduces to H1 TOO.** 4003: B-iii reduced twice —
    capacity ⟺ sign(μ²) at 0668, then sign(μ²) = sign(m²) at 1100 — leaving **exactly two residuals, (H1)
    and (H-NESS)**; and **4004 closed (H-NESS) as ill-posed**. **So (a)/(b)'s only surviving residual IS
    H1.**
- **⇒ BOTH of δ_CP's 2028+ contingencies reduce to H1, AND H1 IS REFUTED. The long-horizon target has no
  surviving route as stated.**
- **AND THAT IS MORE CONSEQUENTIAL THAN A GO/NO-GO, FOR A DIFFERENT REASON.** A go/no-go gets revisited
  when new information arrives. **A long-horizon plan contingent on a named condition is not revisited at
  all** — it sits until someone tries to execute it in 2028 and discovers the condition was refuted in
  2026. **Nothing in the workflow would surface that on its own.** Less urgent, more durable.
- **NOT this lane's to revise.** SF-2's campaign plan belongs to SF-2; what this lane owes is the notice,
  now on record with **both** contingencies traced. **Lane: SF-2 / founder.**

---

### TODO-4060-EW — H1's exposure swept: 40 live files, not two. Plus a correction I repeated for eight patches.

- **CORRECTION, REPEATED SINCE 4022: VW-1 HAS THREE HYPOTHESES, NOT ONE.** CHIR.md states it as a
  conjunction — *"if the DSL measure is reflection-positive **[H1]** + the det-coset ℤ₂ is
  vectorial-not-axial **[H2]** + no θ-term **[H3]**"*. **I have been calling H1 "VW-1's sole residual"
  since 4022** — that phrasing came from 4003, which said B-iii's residuals were (H1) and (H-NESS), a
  statement about **OPEN-SM-4's sub-claim**, not about VW-1's hypothesis list. **The conclusion is
  unaffected** (a conjunction fails if one conjunct fails), but the description made VW-1 look more
  fragile than it is and H1 more central. **And if anyone repairs H1, H2 and H3 become live again and are
  NOT discharged.**
- **A MAP THE CORPUS ALREADY HAS AND I WAS WORKING WITHOUT.** CHIR.md's *P-face / T-face map
  (CPT-unified, from TARROW-1)*: **sign(n̂) = FI-C-9, P-ODD ↔ electroweak PARITY VIOLATION (V−A), E26**;
  **sign(δ), T-ODD ↔ SM CP-VIOLATION (δ_CP)**. **⇒ the chiral-lattice arc (4038–4048) bears on V−A; the
  H1 arc (4022–4059) bears on δ_CP.** Two different faces. It would not have changed a computation — it
  would have changed how I described where each result lands.
- **THE SWEEP, AND MY DRAFT ASSERTED THE ANSWER BEFORE RUNNING IT.** Draft: *"the live dependency set is
  SMALL and already known"* — **FAILED. It is 40 live files.** Among them **3 theorem sources**
  (`theo_chir_vw_1.tex`, **`theo_chir_vw_2.tex`**, **`theo_chir_tarrow_2.tex`** — the last two I did not
  know about), **9 scoping / GO-NO-GO documents** including a dedicated **H1 attack-scoping** doc and a
  dedicated **OS-positivity probe scoping**, and **`flagship_assembly_scope.md`**.
- **⇒ 4058 AND 4059 DID NOT COVER THE EXPOSURE.** They found two consumers; there are more. **Which are
  load-bearing is a CHIR-lane audit, not an EW-lane grep.** This patch delivers the **list** and the
  **correction**, not the audit. **Lane: CHIR — audit owed.**

---

### TODO-4061-EW — A2 note added; session handover written; lane closed at 4061

- **A2 NOTE ADDED** to `axiom-registry.md`, below the axiom table (a paragraph inside a markdown table
  splits it in two; the first draft did that and was moved). **The cage is not required to be exactly
  regular; the 7.356°/edge frustration is carried as strain.** Points at
  `founders_voice/4020_ruling_distorted_cage.md` and `4019_angular_deficit.py`.
- **Three guards written into the note:** the 7.356° is **derived, not chosen** (so it licenses a *specific*
  strain, not irregularity in general); **z = 12 is inside A2**, so giving up exactly-twelve *would* be an
  amendment while this is not; and A2's **f-vector-vs-"tessellated" tension is flagged as open**, pointing
  at 4009–4034.
- **NOT an axiom change.** A2's text is untouched.
- **HANDOVER WRITTEN:** `handovers/2026-09-15_session_230_ew_lane_4000_4061.md` — orienting paragraph,
  what was established, **eight traps**, what is owed and to whom, next-session items, governance enacted.
- **LANE CLOSED AT 4061.** Nothing in it is bounded and unblocked. **Next free: 4062.**
- *(A draft of the handover asserted that H1's 40 dependents had never been audited. `absence_gate.py`
  caught the assertion and it is **withdrawn rather than evidenced**: the supportable statement is that
  **4060 produced the list and did not characterise it**, and the files belong to CHIR rather than this
  lane. Seventh time this session a gate or a control corrected a claim — the last one landing on the
  handover itself.)*

---

### TODO-4062-EW — SUPERSEDED at 0983 (chirality lane): the object 4056–4062 tested is not H1

- **0983 finding.** H1 per `theo_chir_vw_2.tex` v1.1 is Θ_OS (Euclidean time-reflection) positivity, ⟺ VW-a-4; the
  spatial parity is the *tested symmetry*, a reading VW-2 v1.1 itself withdrew. 4022–4062 tested the spatial
  parity on the occupation law throughout. **H1 is OPEN exactly as before 4022** — not refuted (4056/4057), not
  conditionally restored (4062). Items (i)–(iii) below are moot as H1 items; (i) and (iii) are answered
  (a finite window is irrelevant to VW-a-4 as posed; 4022's reading is NOT VW-1's OS sense).
- **CLEARED:** SF-2 notice — δ_CP contingencies OPEN on H1 as defined (SF-2 lane need not act; 4059's notice
  stands with verdict OPEN). CHIR audit — DONE at 0983: none of the 40 absorbed the spatial reading.
- **STILL OWED (CHIR, from 4060, unrelated to H1):** CAPACITY-1 piece 1 text fix, add "on perturbed
  configurations" (η pointwise degenerate on the unperturbed lattice, 4023/4058). Text fix. → TODO-0983-CHIR.
- **OWED (CHIR, PD-008 attack on 0983):** (a) does VW-1 Thm 6.1 consume Θ_OS positivity alone, or also
  spatial-parity positivity? (VW-2 review Q2: "H1 ⟺ VW-a-4" is *too sharp* unless VW-a-1/2/3 carry the
  distinction.) If the latter, 4056/4062's object is relevant after all. (b) Finish the exact-rate Θ_OS run at
  δ = 0.35, t = 1 (float-rate result −3.5e−15, unclaimed). → TODO-0983-CHIR.
- Original 4062 text retained below for provenance.

<details><summary>4062 text (superseded)</summary>

### TODO-4062-EW — PD-008 critique of 4056/4057: H1 REFUTED → OPEN (conditional). Convenient branch, submitted.

- **RESULT.** 4057 step (3) read *CPs are conserved* (GR-FE-1) as *the total on one 600-cell is fixed*. The
  source states **continuity with flux**, constancy only for an **isolated system**; A2's substrate is
  **tessellated**. The fixing-sector violation is **−1/K_tot exactly** and vanishes in the limit; the
  independent-Poisson measure 4057 called inadmissible **is that limit**. VW-1 locates RP in CONT-1, where a
  finite polytope *does not literally possess* it. **H1 (n̂-fixing) is OPEN**, conditional on (a)
  non-interacting walkers and (b) Θ-symmetry of the tessellated substrate's generator.
- **ALSO WITHDRAWN:** 4056's "δ = 0 is untouched" (F = n_a/(K p_a) − 1 violates at δ = 0 on a finite total).
- **QUANTIFIER:** H1 is NOT claimed on any finite window. It is false there.
- **OWED — attack this result first (next EW/CHIR window, PD-008):** (i) does any H1 consumer need RP on a
  finite window rather than the limit state? (ii) condition (b) on the aperiodic tessellation (4009);
  (iii) not re-examined: whether 4022's static spatial-reflection reading of H1 is VW-1's
  Osterwalder–Schrader sense. **Lane: CHIR (VW-1's holder), with EW.**
- **OWED — SF-2 / founder notice CORRECTED:** 4059's notice said δ_CP's 2028+ contingencies are refuted.
  **They are OPEN**, both still reducing to H1, now conditional on (a) and (b). The notice stands; its
  verdict changes. **Lane: SF-2.**
- **OWED — 4060's CHIR audit RE-SCOPED:** from *which of the 40 files fall* to *which of the 40 state H1
  without its conditions*. None of the 40 was annotated as refuted by 4056–4061 (only SM.md, the frontier
  header, the registry and this file carried it, all corrected here). **Lane: CHIR.**
- **The session-230 handover** carries "H1 REFUTED"; an erratum line is added at its head so the next
  window's first read does not inherit it.

</details>

### TODO-0983-CHIR — Owed from the H1 audit (registered Patch 0983, chirality lane)

- **(1) CLEARED at 0986** — qualifier added in `frontier_sectors/CHIR.md` (two places) and `theorem-registry.md`; CAPACITY-1 has no .tex yet (flagship assembly scope), so the .tex inherits it at drafting. Original: **CAPACITY-1 piece 1 text fix** — add "on perturbed configurations" to the η non-degeneracy condition
  (4023: η is pointwise degenerate on the unperturbed lattice, 120/120 vertices; 4058 located it on CAPACITY-1's
  narrowed conditionality). Not physics. **Lane: CHIR.**
- **(2) PD-008 attack on 0983** — is Θ_OS positivity the only positivity VW-1 Thm 6.1 consumes? Read Thm 6.1's
  proof, not VW-2's bridge remark about it. **Lane: CHIR.**
- **(3) MOVED to TODO-0988-CHIR** (the script is now in the repo; this entry had no executable form). Original: Exact-rate Θ_OS probe at δ = 0.35, t = 1 (30+ digits from φ-exact rates) to settle whether the
  −3.5e−15 is a signal or float input. If negative and confirmed: a necessary condition for VW-a-4 fails on
  the single-walker [PCD-EXT] toy — a toy result, not H1. **Lane: CHIR.**
- **(2) CLEARED at 0984** — answered: Thm 6.1 (ii) consumes neither reflection; see TODO-0984-CHIR.
- **(4) CLEARED at 0987** — erratum line added at the head of `series_standard_model/reasoning/4022.md` (EW lane is closed at 4061; done from CHIR under PD-006, fragment otherwise verbatim).

### TODO-0984-CHIR — VW-1 Thm 6.1 (ii) needs an unstated phase-source hypothesis (registered Patch 0984, chirality lane)

- **(1) CLEARED at 0985** — corpus reads R⁴ as space, Moment as time (glossary ζ^W/ζ^qDP/Moment; VW-2 Thm A); no continuum reading gives η a time index. 0984 stands.
- **(2) CLEARED at 0985** — VW-1 v1.5 corrigendum applied; recompile owed (ledger A11); panel not held.
- (original text of (1) retained:) **PD-008 attack on 0984:** is there any reading of CONT-1's Φ-continuum under which
  η's source is a phase — i.e. a Euclidean rotation group mixing the Moment index with R⁴ under which η is a
  full pseudoscalar? If yes, H1′ may hold in the continuum and the route survives there. **Lane: CHIR.**
- **(2) VW-1 v1.2 corrigendum** — after (1): add H1′ to Thm 6.1 (ii) and the unification remark; Def. 2.1's
  *no sign problem* clause marked as automatic for a stochastic substrate. Panel only if (1) makes it a win or a
  stall (review economy). Then `paper_regeneration_ledger.md`. **Lane: CHIR.**
- **(3) CLEARED at 0987** — notice written at the head of TODO-4059-EW: the contingency is CAPACITY-1's conditions, not H1.
- **(4) CLEARED at 0992** — escape is not a route: the VW positivity bound is free for any classical measure (C1); a Moment-odd composite acquires a phase only via OS reconstruction, which needs detailed balance, under which ⟨K⟩ = 0 exactly (C3); at δ ≠ 0 the composite is explicitly sourced and Thm A is gone; and a bound on K does not reach sign(μ²) of η (1100). 0985 and VW-1 v1.5 stand; no CONV round (review economy). Convenient branch, marked in `reasoning/0992.md`.
- (original text of (4) retained:) **Candidate escape, NOT built (D-3):** a P-odd AND Moment-odd order parameter (η × TARROW-2's O(δ³)
  current) would carry the time index VW needs. T-face. Scope before building. **Lane: CHIR.**
- **(5) MOVED to TODO-0988-CHIR.**

### TODO-0988-CHIR — Exact-rate Θ_OS probe (registered 0988; RUN 1 done 0989; RUN 2 done 0991 — **NEGATIVE at (0.35, 1) and (0.35, 2)**; **CLEARED at 0993 — RUN 3 WITHDRAWN**)

> **0993 status — CLEARED.** The probe tested only the real-symmetric part of the OS pairing; VW-2 Thm A states it Hermitian (⟨Θ_OS(Ā)A⟩ = ⟨A,TA⟩_π). The Hermitian pairing fails at every tested δ ≠ 0 (0.05, 0.1, φ⁻³, 0.35), and an exhaustive search over H4 (14,400 automorphisms, all of which rescue at δ = 0) finds **no** involution J with J π = π and J Q Jᵀ = Q̂ — so VW-a-4 is refuted on the single-walker [PCD-EXT] measure, including at the physical bias. Run 3 would decide nothing a theorem consumes: **withdrawn**, founder action not needed. Script `code/0993_theta_os_hermitian_exhaustive.py`; fragment `reasoning/0993.md`. H1 on the full DSL measure stays OPEN, with a named requirement (an internal involution reversing TARROW-2's current) — recorded in `frontier_sectors/CHIR.md`, not a queued action. **Lane: CHIR.**

> **0991 status.** Run 2 adjudicated under the 0989 rule: **NEGATIVE** at (0.35, 1) (λ_min/floor = −3.2×10¹⁵, 8-digit stable across dps 30/45/60) and (0.35, 2) (two negative directions); resolved positive at (0.35, 0.75). Exact δ = 7/20 reproduces the float-δ run to every digit. **Finding (toy):** the single-time OS pairing of the single-walker [PCD-EXT] measure goes negative at δ = 0.35 for t ≥ 1 — VW-a-4 fails on this toy at that tilt. Consistent with VW-2 Thm A (positivity from detailed balance at δ = 0 only). Not H1 on the DSL measure; no verdict moved. Filed in `code/0989_results_kila6_run2.txt`, `reasoning/0991.md`. **RUN 3 OWED (founder, mechanical, Kila6, low priority):** the physical bias δ = φ⁻³ ≈ 0.236 (0966) sits between run 1's positive δ = 0.2 and negative δ = 0.35; same command (`python 0988_theta_os_exact_probe.py` → `0991_results.txt`), eight cases, rule unchanged. **Lane: CHIR.**

> **0989 status.** Run 1 (seven cases, Kila6, 15 Sep) filed in `code/0988_results_kila6_run1.txt`; verdict under the 0988 rule: **claim nothing** (thresholds were mis-sized against the spectrum's ~10⁻¹⁶ tail — my error). Value at (0.35, 1): −3.52×10⁻¹⁵, identical at dps 30/45, i.e. exactly resolved; the float-input error in δ (2×10⁻¹⁷) cannot account for it (slope bound ≈ 0.25). **RUN 2 OWED (founder, mechanical, Kila6):** script revised (string inputs, exact-δ assert, floor printed) and a corrected rule pre-committed in its docstring — NEGATIVE if λ_min < −10⁶·floor and 6-digit-stable across dps 30/45/60; ZERO if |λ_min| < 10³·floor. Nine cases, ~20–40 min each: `cd ~/Documents/GitHub/CPP/series_umbrella/series_substrate_chirality_arc/chirality_derivations/code && python 0988_theta_os_exact_probe.py` → `0989_results.txt`. Paste into a CHIR window. Either outcome is a toy result and moves no verdict. **Lane: CHIR.**

- **What.** `chirality_derivations/code/0988_theta_os_exact_probe.py` — the OS time-reflection pairing on 4022's
  single-walker [PCD-EXT] toy measure, with rates built exactly in Q[φ] at 30 and 45 digits. Settles whether
  0983's −3.5×10⁻¹⁵ (δ = 0.35, t = 1, float-precision rates) is a signal or float input. **Decision rule is
  pre-committed in the script's docstring**; construction stage tested exactly in-container (0988), the
  expm/eigsy stage not runnable here (5-minute cap).
- **Who / where.** Founder, mechanical: on **Kila6** (`python`, not `python3`; deps numpy + mpmath, pure wheels):
  `cd ~/Documents/GitHub/CPP/series_umbrella/series_substrate_chirality_arc/chirality_derivations/code && python 0988_theta_os_exact_probe.py`
  — ~10–20 min per case, seven cases, results appended to `0988_results.txt` in that folder. Paste the file
  (or the lines) into a CHIR window; Claude files the outcome.
- **Stakes, stated so the job is sized right.** Either outcome is a toy result on [PCD-EXT]: ZERO strengthens
  the single-time necessary condition for VW-a-4; NEGATIVE is a failure of that necessary condition on the
  single-walker toy only. Neither touches H1 on the DSL measure or any verdict. Low priority; run when Kila6 is
  idle between DM campaign phases. **Lane: CHIR.**
