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
- **SM-2 edit (g)** — the Mass Contribution Breakdown W row label. **Deliberately held** pending `OPEN-EW-5`
  (does the W mass breakdown depend on species or only on count?). This is the only place a published SM-2
  number can still move; relabelling the row before the answer would assert a pure relabel that may be false.
  Lane: EW. The row still reads `Linear 6-hDP chain` on purpose.
- **The PDF recompiles themselves** — founder mechanical, five documents.
- **An observable selecting the alternating W⁰ ring order over the blocked order.** None on file; carried with
  `OPEN-EW-5`. Lane: EW.

### TODO-0974a-CAPTURE — Steps C and D of the Session 228 close — **Step C CLEARED at 0977; Step D LARGELY RECOVERED at 0975b, superseding the "unrecoverable" finding**

**CORRECTION (Patch 0975b, 13 Sep 2026).** 0977 recorded Step D as unrecoverable for 34 patches, on the basis that the reasoning "was never saved and no longer exists anywhere." **That was true of the repository and false of the world:** the window that produced those patches was still live, and reasoning it can state about its own work is *primary source*, not reconstruction. **21 of the 34 are now captured** — `chirality_derivations/reasoning/` 0942, 0943, 0944, 0946, 0947, 0950, 0951, 0953, 0955, 0957, 0961, 0963, 0964, 0965, 0966, 0968, 0970, 0971 and `dynamical_substrate_law/documentation_suite/` reasoning-0972, reasoning-0973. **The other 13 are genuinely exempt** under the scope test added at 0975b (0938, 0939, 0945, 0948, 0952, 0954, 0956, 0958, 0959, 0960, 0962, 0967, 0969, 0974, 0974a): no original derivation, no computation, no finding.

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
  - **EW lane — D₆-breaking note, filed with `OPEN-EW-5` (Patch 0946).** D₆ (order 12) is the stabiliser of the *bare* Petrie hexagon; decorating it with 3 qDP + 3 eDP drops the stabiliser to order 6, 2 or 1 by arrangement. Not an error in the lane's statement, but any downstream argument applying D₆ to the *decorated* W⁰ needs the surviving subgroup.
  - **EW lane — `OPEN-EW-5` registered at Patch 0945** (`frontier_sectors/EW.md`): does SM-2's W mass breakdown depend on the species of the 12 CPs or only on their count? Count is unchanged (6-hDP chain and the W⁰ ring are both 12 CPs), so either the row is a pure relabel or the W mass fit needs recomputation against 3 qDP + 3 eDP. **The only place a published SM-2 number can still move.** Consumers: corrigendum edit (g); `OPEN-EW-2`, `OPEN-EW-3`. Pointer offered in the corrigendum §4b, explicitly not a derivation: the 3513 "odd man out" partnerless-third structure (a bare CP on a DP entity, already used by the DM lane's E3 count) has the right shape and would reuse an existing mechanism.
  - **Open (physics, founder's):** whether the linear −eCP carries a rest-mass term of its own or is already folded into the N_k = 2.5 assignment. If separate, the down fit moves and N_k needs recalibration. Not assumed either way.
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
