# Handover — SS-9 Session 26 Close

**Last updated:** 6 May 2026 (Session 26 v1.0 polish sub-task (b) close).

This handover supersedes Session 25 close handover (patch 0229). Apply chain for Session 26: 5-patch chain 0230–0234 from `640f3da` origin/main baseline (Session 25 close).

---

## What Session 26 accomplished

**v1.0 polish sub-task (b) DONE.** SS-9 v0.2 → v0.3. Sub-Lemma 2.2 (\S 2.6) added deriving 3D-non-degeneracy from existing inheritance hypotheses C1$'$ + C2 + C3 + C5 via the maximum-edge selection principle (Lemma C):

\[
\text{At } \Nalpha \geq 4, \text{ no ground-state cluster has all centroids coplanar.}
\]

**Proof structure (4 steps):**

1. **Coplanar-centroid degree bound.** Any 2-plane through $c_i$ contains at most 2 of $\alpha_i$'s 4 LO face-normals. Reason: any 3 of the 4 face-normals span $\mathbb{R}^3$ (they form 3 of 4 vertices of a non-degenerate regular tetrahedron centered at $c_i$). Combined with C2 (face-to-face contact requires centroid direction parallel to a face-normal): $\deg_G(c_i) \leq 2$ in any coplanar contact graph.

2. **Planar edge bound.** Handshake: $2|E_{\mathrm{planar}}| = \sum_i \deg_G(c_i) \leq 2\Nalpha$, so $|E_{\mathrm{planar}}| \leq \Nalpha$.

3. **3D edge bound.** FvdW deltahedra realize $|E_{\mathrm{3D}}| = 3\Nalpha - 6$ at $\Nalpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$, with $|E| = 6, 9, 12, 15, 18, 21, 24, 30$ respectively. Physically realizable under C1$'$ (facets a, b).

4. **Strict edge gain in 3D.** $|E_{\mathrm{3D}}| - |E_{\mathrm{planar}}| \geq 2\Nalpha - 6 \geq 2$ at $\Nalpha \geq 4$. Binding-energy gain $\geq 2 \Bpair = 4.684$ MeV. By Lemma C (max edges) + C5 (ground state), no coplanar configuration is a ground state.

**Three remarks accompany the sub-lemma.**

- **Remark 2.2 (tightness, $\Nalpha = 3$ exception).** At $\Nalpha = 3$: planar $|E| = 3$ coincides with $3\Nalpha - 6 = 3$. Strict inequality fails. ${}^{12}$C as planar triangle is consistent with maximum-edge selection at $\Nalpha = 3$. Matches Theorem's exclusion of $\Nalpha = 3$ from scope. Threshold $\Nalpha \geq 4$ is sharp.
- **Remark 2.3 (refined-C1 facet (b) compatibility).** Facet (b) activates only at degree $\geq 5$; planar bound establishes $\deg \leq 2$, so facet (b) not invoked. Facet (b) operates within $\sim 5\%$ LO rigidity envelope; face-normal directions remain $O(5\%)$-deformed from regular tetrahedron, preserving "any 3 face-normals span $\mathbb{R}^3$."
- **Remark 2.4 (effect on §9 Gap 4).** §9 Gap 4 flagged this exact closure route. Sub-Lemma 2.2 delivers it. 3D-non-degeneracy now derivable from existing inheritance hypotheses, not an independent auxiliary assumption.

**Effect on §9 gap list.** "3D-non-degeneracy" gap (Gap 4 in v0.1) **CLOSED at v0.3.** Combined with Session 25's closure of Gap 5 ("C7 motivation argument") at v0.2, the v0.1 6-gap list is reduced to 4 remaining gaps:

| Gap | v0.1 status | v0.3 status |
|-----|-------------|-------------|
| 1. C5 (ground-state existence/uniqueness) | OPEN | OPEN (sub-task (c) candidate Session 27) |
| 2. C6 (cluster surface-realization) | OPEN | OPEN (programme-level OPEN-SS-30) |
| 3. C7 (contact-graph planarity) | OPEN | OPEN (programme-level OPEN-SS-33, conditionally closed at v0.2 modulo H4+H5) |
| 4. 3D-non-degeneracy | OPEN | **CLOSED v0.3** |
| 5. C7 motivation argument formalization | OPEN | **CLOSED v0.2** |
| 6. Steinitz invocation pre-conditions | OPEN | OPEN |

**Effect on programme-level OPEN-* registries: NONE.** 3D-non-degeneracy was an auxiliary assumption local to SS-9, not registered as a programme-level OPEN-SS-* problem. Closure at v0.3 is paper-internal. No changes to Research_Frontier.md OPEN-* status entries from this session — only the "Last updated" header reflects Session 26 polish work.

This contrasts with Session 25's sub-task (a), which advanced OPEN-SS-33 (a programme-level open problem) from raw open to conditional closure.

**Compilation.** Three pdflatex passes (draftmode for 1, 2; output for 3): zero errors all passes; one pre-existing hyperref Token-not-allowed warning preserved unchanged from v0.2 (cosmetic only). Output 25 pages (was 23 in v0.2; +2 pages from sub-lemma + 3 remarks).

**Theorem statement and proof unchanged at v0.3.** Theorem 6.1 still lists "3D-non-degeneracy" in its conditional hypothesis stack for clarity in conditional-hypothesis readability. Remark 2.4 explicitly notes this is now a derived condition, not an assumed one. v1.0 may consolidate.

---

## Session 26 selection logic

The 0229 (Session 25 close) handover identified sub-task (b) as the natural Session 26 starting point: the §9 v0.1 Gap 4 entry already specified the closure route in some detail, so the work was largely formalization of an already-clear closure path. Sub-task (b) is a much shorter and cleaner sub-lemma than sub-task (a), reflecting the fact that 3D-non-degeneracy is a more local geometric statement than C7 (and so derivable from local geometric hypotheses rather than requiring new global topological hypotheses like H4/H5).

The natural ordering (a) → (b) → (c) → (d) → (e) was sustained: (a) closes the largest registered gap (C7 motivation, programme-level OPEN-SS-33); (b) closes the second-largest registered gap (3D-non-degeneracy, paper-internal); (c) addresses the C5 well-definedness (paper-internal, smaller scope); (d) AI review on a tightened paper; (e) external review.

---

## Programme-level state at Session 26 close

- **12 programme-level negative results UNCHANGED** (v1.0 polish work is paper-internal, not programme-level).
- All earlier closures preserved.
- R2 FORMALLY CLOSED (Session 15) — preserved.
- Gaussian-K$_3$ framework FORMALLY CLOSED (Session 16) — preserved.
- Phase 8 Refinement A standing best refinement preserved AND structurally STRENGTHENED.
- Phase 11 R3-Pauli NULL RESULT preserved (structural-redundancy methodological category).
- Single-session R3-channel refinement candidates EXHAUSTED — preserved.
- **OPEN-SS-24 ADVANCED** to conditional theorem at C5 + C6 + C7 + C1$'$ + C2 + C3 inheritance tier — preserved from Session 24.
- **OPEN-SS-33 ADVANCED** from raw open to conditionally closed modulo (H4) + (H5) — preserved from Session 25.
- **OPEN-ORG-012 RETIRED** — preserved from Session 24.
- **SS-9 at v0.3** (was v0.2 at Session 25 close).
- **v1.0 polish track:** sub-tasks (a) and (b) DONE; sub-tasks (c)/(d)/(e) pending.
- **§9 v0.1 6-gap list reduced to 4 remaining gaps** (Gaps 4 and 5 closed at v0.3 and v0.2 respectively).
- §7 stable — no shifts since Phase 11 NULL saturation.

---

## Session 27 forward queue

### Priority 1 within v1.0 polish track: sub-task (c) C5 well-definedness via compactness

**Goal.** Verify that the C5 ground state is well-defined: the set of physically realizable $\Nalpha$-alpha cluster configurations at fixed $\Nalpha$ is compact, and $B(\mathcal{C})$ is continuous on this set, so the supremum $\sup_{\mathcal{C}} B(\mathcal{C})$ is attained — the ground state exists.

**Anticipated Sub-Lemma 2.3 statement.** \emph{The set of physically realizable $\Nalpha$-alpha cluster configurations at fixed $\Nalpha$ (modulo rigid motions) is compact, and $B: \mathrm{Conf}(\Nalpha) \to \mathbb{R}$ is continuous; hence the supremum $\sup_{\mathcal{C}} B(\mathcal{C})$ is attained.}

**Proof sketch.** Configuration space:
\[
\mathrm{Conf}(\Nalpha) = \big\{ (c_1, R_1, \ldots, c_{\Nalpha}, R_{\Nalpha}) \in (\mathbb{R}^3 \times \mathrm{SO}(3))^{\Nalpha} \;\big|\; \text{physically realizable} \big\} \big/ \mathrm{SE}(3)
\]
where physical realizability requires (i) no alpha-alpha interpenetration; (ii) cluster connected through $G$.

Compactness: (a) $G$-connectedness implies bounded diameter $\leq (\Nalpha - 1) R_{\alpha\alpha}$, so centroids modulo $\mathrm{SE}(3)$ live in a compact subset of $(\mathbb{R}^3)^{\Nalpha} / \mathrm{SE}(3)$; (b) $\mathrm{SO}(3)^{\Nalpha}$ is compact; (c) physical realizability is closed (no-interpenetration is a closed condition; $G$-connectedness is closed in the configuration topology). Quotient of a closed subset of a compact space by a continuous group action remains compact.

Continuity of $B$: $B(\mathcal{C}) = \Nalpha \Balpha + |E(\mathcal{C})| \Bpair$. $|E|$ is locally constant on the configuration space (small perturbations don't change which faces coincide), with jumps at face-coincidence boundaries. Continuity in the upper-semi-continuous sense: $B$ is bounded above on $\mathrm{Conf}(\Nalpha)$ (since $|E| \leq 3\Nalpha - 6$); supremum is attained on the closed configuration space.

**Expected single-session-tractability.** Yes — the proof requires careful topological setup but is standard compactness-of-configuration-space + continuity-of-energy-functional argument.

### Priority 1 at programme level (parallel multi-paper track): SS-10 sub-shell-physics

SS-10 sub-shell-physics decomposition. Strutinsky-style shell-corrected baseline integration replacing SEMF; revised polytope-residual decomposition; assess whether $^{28}$Si and $^{32}$S fall into line under shell correction. SS-9 v0.1 (now v0.3) serves as canonical anchor reference.

**Multi-paper, multi-session scope.** Independent of v1.0 polish track sub-task progress. Runs at whatever cadence fits Thomas's schedule.

### Sub-tasks (d)/(e) scheduling

- **Session 28 candidate:** sub-task (d) AI-team review per symmetric-honesty protocol (ChatGPT primary; Copilot rotation; same standards applied to SS-9 own work as to reviewer feedback). At Session 28, all 3 sub-lemmas (C7 conditional derivation, 3D-non-degeneracy, C5 well-definedness) will be in place; review feedback is most valuable on a paper with all known gaps closed.
- **Session 29+ candidate:** sub-task (e) external review via reviewer-response protocol (`templates/operating_system.md` §4 Phase 4).

---

## Anti-priorities sustained

- **Do NOT modify SS-9 v0.3 .tex outside of v1.0 polish revisions.** Each polish revision bumps the CHANGELOG version (v0.3 → v0.4 → ... → v1.0). The shipped versions are: v0.1 Session 24 ship; v0.2 Session 25 sub-task (a) C7 sub-lemma close; v0.3 Session 26 sub-task (b) 3D-non-degeneracy sub-lemma close.
- **Do NOT propose any single-session R3-channel refinement to close the remaining 52% empirical gap.** (Sustained from Phase 11 close.) Single-session R3-channel refinement candidates remain EXHAUSTED.
- **All Phase 4–11 anti-priorities remain in force.**

---

## Cumulative trajectory summary (Session 26)

Session 26 is the second session of the v1.0 polish track. Sessions 25–26 have closed 2 of the 5 polish sub-tasks. Two of the v0.1 6-gap list items (Gaps 4 and 5) are now closed, with Gap 1 (C5 well-definedness) the next target at Session 27. Both sub-tasks (a) and (b) demonstrated that the §9 gap list was diagnostically accurate — the sketched closure routes formalized cleanly without surfacing unexpected obstructions.

The v1.0 polish track is on track to span Sessions 25–29 at sub-task-per-session cadence. SS-10 sub-shell-physics development runs in parallel from Session 25 onward at programme-level Priority 1 — multi-paper, multi-session scope, sole remaining path to closing the 52% empirical gap registered at Phase 11 close.

---

## Apply chain for Session 26 (5-patch chain 0230–0234)

**Baseline:** `640f3da` (Session 25 close, post-patch-0229).

**Patches:**

| # | Hash | Description |
|---|------|-------------|
| 0230 | `6914a9b` | Substantive: SS-9 v0.3 .tex Sub-Lemma 2.2 (3D-non-degeneracy from maximum-edge selection) + ripples (§9 Gap 4 CLOSED, CHANGELOG v0.3) |
| 0231 | `ab3779b` | Step A + Step C: Session 26 entry to session log + Vignette 33 to development-SS-9.md |
| 0232 | `fd3ea15` | Step B + Step D: transcript pointer-map (transactions 541-558) + Tier 4 verbatim reasoning |
| 0233 | `1511d44` | Step E: Research_Frontier last-updated header + future_projects.md (A.2) sub-task (b) DONE / sub-task (c) PROMOTED + recently completed entry (no programme-level OPEN-* changes since 3D-non-degeneracy is paper-internal) |
| 0234 | (this commit) | Step H: Session 26 close handover (rm + recreate handover-SS-9.md) |

**Apply order:** 0230 → 0231 → 0232 → 0233 → 0234 (sequential).

**Per-registry audit (Step H support):**

- ✓ `Research_Frontier.md`: Last-updated header updated to Session 26 sub-task (b) closure; no programme-level OPEN-* status block changes (3D-non-degeneracy is paper-internal)
- ✓ `Organizational_Frontier.md`: no Session 26 changes (sub-task (b) work is paper-internal, not organizational)
- N/A `axiom-registry.md`: no axiom changes
- ✓ `theorem-registry.md` (implicit): Sub-Lemma 2.2 is a paper-internal lemma; tracked via SS-9 v0.3 internal numbering; no global theorem registry update needed at sub-lemma tier
- N/A `predictions.md`: no new predictions
- ✓ `future_projects.md`: (A.2) entry sub-task (b) DONE / sub-task (c) PROMOTED; Recently Completed Session 26 entry added
- N/A `problem_histories/`: no programme-level OPEN-* registry changes; problem history not yet started for OPEN-SS-33 (Session 25 advancement registered in main registry)
- N/A `master_glossary.md`: terms inherited from SS-7
- N/A `paper_catalog.md`: SS-9 entry exists from v0.1 ship; v0.3 is internal version increment, no catalog change
- ✓ `session_logs/2026-05-02_session_log.md`: Session 26 entry appended (patch 0231)
- ✓ `series_strong/papers/SS-9/documentation_suite/development-SS-9.md`: Vignette 33 appended (patch 0231)
- ✓ `series_strong/papers/SS-9/documentation_suite/transcript-SS-9.md`: transactions 541-558 appended (patch 0232)
- ✓ `series_strong/papers/SS-9/documentation_suite/reasoning-SS-9.md`: Session 26 Tier 4 verbatim reasoning appended (patch 0232)
- ✓ `series_strong/papers/SS-9/documentation_suite/handover-SS-9.md`: Session 26 close handover (this file, patch 0234)
- ✓ `series_strong/papers/SS-9/SS-9_simplicial_alpha_polytope_connectivity.tex`: Sub-Lemma 2.2 added at v0.3 (patch 0230)

**Verification:** Three pdflatex passes on SS-9.tex post-0230 produced 25 pages, zero errors after pass 3. Local HEAD `1511d44` (post-0233) builds clean against `640f3da` baseline. 0234 (this commit) adds only the handover document; no compilation impact.
