# Phase 7B Content Pack — F.1 Dynamical Substrate Law v1.0 SHIPPED

**Location:** `flagship_papers/dynamical_substrate_law/phase_7B_content_pack.md`
**Purpose:** Pre-stage all programme-level registry content needed for Phase 7B (Patches 0574–058N) of the F.1 paper completion sequence. Created at Phase 7B initiation (Session 143 Patch 0573) so subsequent sessions can ship ONE registry per session WITHOUT re-reading the F.1 `.tex` source or the SHIP-time companion files. Each subsequent session reads: (1) `bootup.md` §3 and §3.5 (lightweight mode), (2) latest handover, (3) THIS FILE, (4) the ONE target registry — and emits ONE surgical patch.
**Created:** Session 143 Patch 0573 (25 May 2026).
**Lifecycle:** This file is RETIRED after Phase 7B closes (Patch 058N close) and Phase 7C ships the OSF deposit. Either delete it at Phase 7C close or move to `archive/` for historical reference.
**Maintenance discipline:** Each subsequent Phase 7B Patch updates the **Landing status** field for its registry below — flipping `PENDING` → `LANDED at Patch 05NN`. This makes the pack self-tracking and lets any later session see at a glance which registries are still outstanding.

---

## §0. Context recap (read first)

**F.1 SHIPPED state.** The paper `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` shipped v1.0 at Session 142 Patch 0570 (24 May 2026) as the first F-line flagship v1.0 SHIP in CPP corpus history. Three reviewers converged on SHIP-ready; ChatGPT R6 verdict was the strongest-positive of the cycle. Frozen PDF lives at `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.pdf` (33 pages, MD5 `49e56be92a3ccc126ce09210b5898794`).

**Phase 7A closed.** Patches 0572 → 0572a–0572i produced the full SHIP-time companion suite: 7 companion files (`mechanism-`, `glossary-`, `phenomena-`, `philosophy-`, `reviews-`, `keywords-`, `changelog-dynamical-substrate-law.md`) + verification notebooks B1–B5 + paper-specific registries (bibliography, INDEX, paper README) + curated transcripts. Patch 0572i commit message: *"Phase 7A FINAL item; CLOSES Phase 7A."*

**Phase 7B scope (this content pack).** Eleven candidate programme-level registries, of which roughly 8 require substantive updates, 1 is N/A by audit (axiom-registry), 1 may already be partially landed (research_frontier), and 1 is small/optional (organizational_frontier). Ordering, per-registry insertion blocks, and anti-collision anchors are below.

**Phase 7C ahead (NOT in this pack).** OSF deposit + anthology chapter at `book_project/chapters/F1_dynamical_substrate_law.md` + H1–H5 final-verification audit. Scoped at end of pack §13 only as forward pointer.

---

## §1. Theorem candidates — the load-bearing intel

Three programme-level theorem candidates emerge from F.1 v1.0:

| Candidate | Composition | Layer rigor | Conditional on |
|---|---|---|---|
| **THEO-DSL-1** | Theorem 6.1 (perturbation-theory propagation rule) + Corollary 6.2 (shell-locality at O(δ¹)) | publication-grade Layer 3 | unconditional; hardened at Patch 0550 |
| **THEO-DSL-2** | Theorem 5.1 (host-to-first-shell uniform projection) + Theorem 5.2 (first-shell-to-first-shell perpendicularity) | publication-grade Layer 3 | conditional on G1 (first-shell inner-product primitive); hardened at Patches 0551 + 0552 |
| **THEO-DSL-3** | Theorem 7.1 (substrate-locality umbrella; closed-form result $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$) | **sketch-document Layer 3** | assembled from Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2; not independently hardened |

**CPP axiom dependencies (all three theorems):** A1 (CP existence), A2 (600-cell substrate topology), A3 (Dipole Sea / DI-bit propagation), A4 (SSV interaction / Nexus connectivity), A7 (substrate-stress / primitive-direction sourcing). Plus **framework axioms MA.1 + MA.2** (Mechanism A propagation-rate asymmetry + framework-local current construction), taken as substrate-physics input at Layer 3; Layer 4 axiomatic derivation of Mechanism A from A1–A11 is OPEN-FP-F1-2.

**Foundational inputs (FIs) inherited from Capotauro v2.0 Reading C closure:** FI-C-RC-1 (primitive 4D direction $\hat{n}$) + FI-C-RC-2 (vertex-aligned reading $\hat{n} = \vhost$).

**Falsifiers (one per theorem candidate):**
- THEO-DSL-1 falsifier: demonstration of a first-order-in-$\delta$ contribution at any vertex beyond first-shell range (a $\delta^1$ term in the substrate current at a second-shell or further vertex).
- THEO-DSL-2 falsifier set: (a) demonstration via explicit 600-cell calculation that $\hat{u}_i \cdot \hat{n} \neq -1/(2\phi)$ for some first-shell vertex; (b) demonstration of $\hat{e}_{ij} \cdot \hat{n} \neq 0$ for some first-shell-to-first-shell edge. Both testable on Coxeter's canonical 600-cell coordinates; numerically verified at `code/verify_phase1.py`.
- THEO-DSL-3 falsifier: demonstration of a different prefactor on $\hat{n}$ at $\mathcal{O}(\delta^1)$ from any valid first-principles calculation on the 600-cell with Mechanism A inputs. Also falsifiable by demonstration of any tangent-to-$\hat{n}$ component at first order.

**Cross-sector consistency anchor (load-bearing for reviewer pre-rebuttal):** The host-to-first-shell uniform projection constant $-1/(2\phi)$ appears identically in Capotauro v2.0 §3 spatial-sector substrate-locality theorem. F.1 and Capotauro v2.0 share the same first-shell geometric identities (G1 + G2 + Theorem 5.1 analog + Theorem 5.2 analog) despite spatial vs temporal sector contexts. Grok R1 explicitly emphasized this as a structural payoff.

**Open Problems registered at F.1 v1.0:** OPEN-FP-F1-1 through OPEN-FP-F1-5 (in-body §9); OPEN-FP-F1-6 (prose-density tightening) registered separately at Patch 0569e from R6 follow-up. See §13.6 of this pack for the registry-level entries.

---

## §2. Predictions — PRED-O-NN candidates

F.1's predictions are **structural mathematical constants** (not empirical-comparison predictions in the SS-7 / SF-4 / SM-2 sense). The swarm-validation contribution is at the structural-constant + cross-sector-consistency level. Five paper-body predictions + three foundations-work predictions (the foundations-work three are documented in `flagship_papers/dynamical_substrate_law/sketches/F1_phase2_foundations_work.md`, verified by code, but not in the paper body — registry inclusion is optional, recommend a single grouped entry referencing the sketch).

The next available PRED-O-NN number must be looked up at registry-edit time by scanning `predictions.md` for the highest existing `PRED-O-NN` ID. As of the last full audit (Session 141), the F.1 predictions slot into the post-PRED-O-25 range; verify the exact next number when editing.

### PRED-O-N1 — Host-to-first-shell uniform projection constant
- **Prediction:** $\hat{u}_i \cdot \hat{n} = -1/(2\phi) = -(\sqrt{5}-1)/2 \approx -0.309017$ uniformly across all 12 first-shell neighbours at vertex-aligned Reading C in the 600-cell.
- **Status:** Zero-parameter structural prediction; analytically derived from G1 + icosahedral residual symmetry $H_3 = I_h$.
- **Numerical verification:** `flagship_papers/dynamical_substrate_law/code/verify_phase1.py` identity (1); machine-precision pass.
- **Cross-sector consistency:** Identical structural constant appears in Capotauro v2.0 §3 spatial-sector theorem.
- **Theorem source:** Theorem 5.1 of `dynamical_substrate_law.tex`.

### PRED-O-N2 — First-shell unit-vector sum identity
- **Prediction:** $\sum_{i=1}^{12} \hat{u}_i = -(6/\phi)\,\hat{n} \approx -3.708204\,\hat{n}$.
- **Status:** Zero-parameter; follows from PRED-O-N1 + orthogonal-component cancellation by $I_h$ residual symmetry.
- **Numerical verification:** `code/verify_phase1.py` identity (2).
- **Theorem source:** §5 of `dynamical_substrate_law.tex` (intermediate identity).

### PRED-O-N3 — Icosahedral rank-1 sum identity
- **Prediction:** $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n} \approx 1.145898\,\hat{n}$.
- **Status:** Zero-parameter; combinatorial consequence of PRED-O-N1 + PRED-O-N2.
- **Numerical verification:** `code/verify_phase1.py` identity (3).
- **Theorem source:** §5 of `dynamical_substrate_law.tex` (intermediate identity, load-bearing for Theorem 7.1).

### PRED-O-N4 — Substrate-locality umbrella coefficient $6/\phi^2$
- **Prediction:** $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ at the host vertex at first order in the Mechanism A asymmetry parameter $\delta$. Numerical coefficient $6/\phi^2 = 6(2-\phi) \approx 2.291796$ — the universal structural constant for the temporal sector at vertex-aligned Reading C in the 600-cell substrate.
- **Status:** Zero-parameter; closed-form result of Theorem 7.1.
- **Numerical verification:** `code/verify_phase1.py` identity (4) for any value of $\delta$.
- **Theorem source:** Theorem 7.1 of `dynamical_substrate_law.tex` (substrate-locality umbrella).
- **Falsifier sharpest:** any tangent-to-$\hat{n}$ component at first order, OR a different prefactor at $\mathcal{O}(\delta^1)$ from a valid 600-cell + Mechanism A calculation.

### PRED-O-N5 — First-shell-to-first-shell edge perpendicularity
- **Prediction:** $\hat{e}_{ij} \cdot \hat{n} = 0$ for all 30 first-shell-to-first-shell edges at vertex-aligned Reading C.
- **Status:** Zero-parameter; **shared identity with Capotauro v2.0 §5.6** (the K3-base protection identity that makes first-order curl content vanish at the host vertex).
- **Numerical verification:** `code/verify_b1q2_curl_content.py`.
- **Theorem source:** Theorem 5.2 of `dynamical_substrate_law.tex`.

### PRED-O-N6 (foundations-work; OPTIONAL — single grouped entry recommended)
- Foundations-work predictions documented at `sketches/F1_phase2_foundations_work.md`: first-shell-vertex current magnitude $|\vec{j}(v_i)| = 2 r_0 \delta \sqrt{7-\phi}$ ($\sqrt{7-\phi} \approx 2.317216$); first-shell-vertex sum identity $\sum_{i=1}^{12} \hat{j}(v_i) = (24/\sqrt{7-\phi})\,\hat{n} \approx 10.357\,\hat{n}$; discrete curl vanishing at host vertex at first order in $\delta$. All numerically verified in `code/verify_b1q4_first_shell_current_sum.py` + `code/verify_b1q2_curl_content.py`.
- **Recommendation:** register as a single grouped entry PRED-O-N6 with subfields (a)/(b)/(c) — they share the foundations-work artifact origin and are not in paper body.

---

## §3. Glossary terms — master_glossary.md additions

15 terms recommended for `master_glossary.md` (additions only — do NOT modify any existing entry). Insert in alphabetical order within the existing glossary structure. Each term's first-use section in the F.1 paper is noted for sourcing trail.

**Constants:**
1. **$-1/(2\phi)$ (host-to-first-shell uniform projection constant)** — The structural constant proven in Theorem 5.1: for any first-shell unit vector at vertex-aligned Reading C in the 600-cell, the inner product with the substrate-direction primitive $\hat{n}$ is identically $-1/(2\phi) \approx -0.309$, uniformly across all 12 first-shell neighbours. *Shared with Capotauro v2.0 §3 spatial-sector substrate-locality theorem.* First use: F.1 §5.3 (Theorem 5.1).
2. **$6/\phi^2$ (substrate-locality umbrella coefficient)** — Numerical coefficient $\approx 2.293$ of the closed-form first-order substrate current $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$ in Theorem 7.1. First use: F.1 §7.2.
3. **$\sqrt{7-\phi}$ (first-shell-vertex current magnitude factor)** — Foundations-work structural constant $\approx 2.317$ in the per-vertex current magnitude at first-shell vertices. First use: foundations-work sketch §B.1.q4 (not in paper body).

**Structural terms:**
4. **DI-bit current** — The first-order-in-$\delta$ vector flow of DI-bit transfer events along oriented edges of the 600-cell substrate, with closed-form first-shell-localized expression at vertex-aligned Reading C. The substrate-physics quantity that F.1's substrate-locality umbrella theorem characterizes. First use: F.1 §3.4.
5. **Vertex-aligned Reading C** — The Reading C variant of the chirality continuum substrate-direction primitive in which $\hat{n}$ is identified with the host-vertex radial direction $\vhost / |\vhost|$. Maximises residual symmetry to $H_3 = I_h$ (icosahedral) at the host vertex. Two other variants (edge-aligned $D_3$, face-aligned $D_2$) are out of scope at F.1; extension is OPEN-FP-F1-5. First use: F.1 §3.2.
6. **Host vertex $\vhost$** — A chosen 600-cell vertex at which substrate physics is computed under vertex-aligned Reading C. First use: F.1 §3.2.
7. **First-shell (in the 600-cell)** — The set of 12 600-cell vertices adjacent to $\vhost$ via an edge; forms a regular icosahedron at distance $1/\phi$ from $\vhost$. Permuted transitively by $H_3 = I_h$ residual symmetry. First use: F.1 §3.2.
8. **Edge graph (of the 600-cell)** — The graph on the 120 vertices + 720 edges of the 600-cell, providing the graph-distance metric on the substrate for perturbation-theory shell-locality analysis. First use: F.1 §3.4.

**Mechanism terms:**
9. **Mechanism A (propagation-rate asymmetry)** — The substrate-physics axiom set MA.1 + MA.2 taken as framework axiom at Layer 3 for F.1: MA.1 gives the directional propagation rate $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$; MA.2 gives the framework-local current construction at first order. Layer 4 axiomatic derivation from A1–A11 is OPEN-FP-F1-2. First use: F.1 §4.
10. **G1 (first-shell inner-product primitive)** — Sketch-document Layer 3 identity inherited from Capotauro Patch 0541 §3.1: first-shell unit vector inner products $\hat{u}_i \cdot \hat{u}_j$ take a discrete set of values determined by $H_3 = I_h$ residual symmetry + first-shell-edge dihedral angle. Publication-grade hardening is OPEN-FP-F1-3 (RECOMMENDED first post-Phase-7 substantive physics Patch). First use: F.1 §3.3.
11. **G2 (first-shell edge-direction projection)** — Sketch-document Layer 3 identity: first-shell-to-first-shell edge directions are perpendicular to $\hat{n}$ for any first-shell pair sharing a 600-cell edge. Establishes Theorem 5.2. First use: F.1 §3.3.

**Methodology terms:**
12. **Sketch-document Layer 3** — Layer rigor classification: a theorem stated and proved at logical-rigor level but not independently hardened (no isolated hypothesis tracking, no five-class exclusion enumeration). Distinct from **publication-grade Layer 3** which requires a hardened-theorem artifact. Theorem 7.1 of F.1 is at sketch-document Layer 3; Theorems 5.1, 5.2, 6.1, Corollary 6.2 are at publication-grade Layer 3. First use: F.1 §1.4, throughout.
13. **Hardened-theorem artifact** — Self-contained `.tex` file under `hardened_theorems/` directory providing publication-grade Layer 3 derivation with explicit hypothesis tracking + structural-input isolation + five-class exclusion enumeration. F.1 has three: Patches 0550 (perturbation-locality) + 0551 (first-shell perpendicularity) + 0552 (host-to-first-shell uniform projection); 741 lines LaTeX combined. Pattern established for F-line flagship trajectories. First use: F.1 §5.1.
14. **Anti-erasure discipline** — Methodological commitment to preserve (a) Layer-distinction between publication-grade L3 trio and sketch-document L3 umbrella; (b) conditionality of Theorems 5.1 + 5.2 on G1; (c) explicit open higher-order questions during paper polishing. Emerged from ChatGPT R2–R6 reviewer pressure. First use: F.1 §1.4 + §8.3.
15. **Framework axiom** — Substrate-physics commitment taken as input at Layer 3 derivation level, distinct from CPP primitive axioms A1–A11 (Layer 4 inputs). Mechanism A (MA.1 + MA.2) is the canonical example for F.1. First use: F.1 §4.3.

---

## §4. Methods catalogue — 5 method candidates

Five methods candidates from F.1 trajectory (per handover §2 item 12). Methods catalogue lives at `methods_catalogue/methods_catalogue.md` (the canonical file; the legacy `methods_catalogue.md` at repo root is a pointer file — verify which is canonical at edit time, see §7 below for the bookkeeping audit). The catalogue has METH-CHIR-CONT-1 through METH-CHIR-CONT-4 from chirality_continuum.tex precedent; F.1 candidates extend this with METH-DSL-N convention.

### METH-DSL-1 — Layer 3 promotion via dependency-graph anchor visualization
A theorem-paper structural method: when promoting Layer 2 sketch content to Layer 3 paper-grade rigor, anchor the §8 Layer-distinction discipline with an explicit TikZ dependency graph (Figure 8.1 of F.1) showing per-theorem Layer status + axiom inheritance + Open Problem branch points. Visualises the publication-grade L3 trio plus sketch-document L3 umbrella as a partial-order with explicit conditionality. **Source:** Patch 0569b Round 3 ChatGPT-driven addition.

### METH-DSL-2 — `\date{}` line scope-framing pattern
At v1.0 SHIP for sketch-document-grade flagship preprints, the LaTeX `\date{}` line carries a four-claim italicized subtitle below the version+date string: (1) "structurally-grounded" + (2) explicit Layer rigor label ("sketch-document Layer 3" / "publication-grade Layer 3") + (3) paper-type ("flagship framework preprint") + (4) explicit non-publication-grade-component disclosure ("...with publication-grade hardened components but non-publication-grade umbrella theorem"). First-reader-visible scope discipline. **Source:** Patch 0570 Variant (b) v1.0 SHIP framing; ChatGPT R4 convergent recommendation; corpus-establishing for future F-line flagship trajectories that ship sketch-document content.

### METH-DSL-3 — v1.0 SHIP milestone Patch pattern (`.tex` metadata + frozen PDF + comprehensive CHANGELOG)
At v1.0 SHIP, a single milestone Patch lands three atomic edits: (a) `\date{}` line update from pre-v1.0 to v1.0 format with scope-framing subtitle; (b) CHANGELOG comment block update with comprehensive Patches-NNNN-to-NNNN cumulative build history + v1.0 SHIP cross-reviewer position summary + post-v1.0 trajectory + anti-priorities; (c) frozen PDF committed at flagship paper root via `.gitignore` exception `!flagship_papers/*/*.pdf`. **Source:** Patch 0570 (F.1 v1.0 SHIP); first F-line flagship v1.0 SHIP using this protocol.

### METH-DSL-4 — PDF-upload-default reviewer engagement protocol
Going-forward protocol for ChatGPT reviewer engagement on papers containing TikZ figures, bibliography environments, or other LaTeX content requiring compilation to render: upload the freshly-compiled PDF, not the `.tex` source. Empirical motivation: F.1 v1.0 SHIP cycle Rounds 3–5 generated a recurring identical-recommendation pattern resolved at Round 6 by switching from `.tex` upload to PDF upload (Patch 0569e diagnostic). Extends `relationship_protocol.md` reviewer-submission protocol with upload-format-aware guidance. **Source:** Patch 0569e diagnostic resolution.

### METH-DSL-5 — Recurring-pattern diagnostic resolution via upload-format check
When a reviewer (especially ChatGPT) produces identical recommendations across multiple rounds despite the corresponding fixes being already implemented: the failure mode is usually upload-format-driven (reviewer is reading `.tex` source and not "seeing" TikZ-rendered figures or bibliography-rendered references). Diagnostic protocol: (1) document the recurring-pattern explicitly; (2) switch upload format from `.tex` source to compiled PDF; (3) re-submit with no content edits; (4) verify monotonic verdict improvement. Resolves the loop without bandwidth-burning content edits. **Source:** Patch 0569e diagnostic resolution methodology.

**Cross-paper-usage note (for the methods catalogue entry):** METH-DSL-1/-3 are F-line-specific corpus-establishing patterns (first applied at F.1; templates apply to future F-line flagship v1.0 SHIPs like F.2/F.3). METH-DSL-2/-4/-5 are programme-wide patterns applicable to any future flagship paper trajectory; recommend explicit cross-paper-usage marker in the catalogue entry.

---

## §5. Per-registry insertion blocks

The blocks below are organized in the recommended Phase 7B execution order (smallest → largest target file, per the diagnostic in Session 142 close discussion). Each subsection gives:
- **Target file** (path)
- **Landing status** (PENDING / LANDED — flip when patch lands)
- **Insertion location** (anti-collision anchor; what to grep/match against, not line number)
- **Pre-staged content block** (copy-paste-ready; minor adaptation may be needed for in-place style match)
- **Anti-collision note** (what concurrent-window changes to watch for)
- **Sanity checks** (cross-references to verify before committing)

### §5.0 organizational_frontier.md audit — Patch 0574 candidate

**Target:** `organizational_frontier.md`
**Landing status:** LANDED at Patch 0574 (Session 143, 25 May 2026). Two new OPEN-ORG entries registered: **OPEN-ORG-019** (PDF-upload-default reviewer engagement protocol + recurring-pattern diagnostic resolution methodology codification in `templates/operating_system.md` §17; status OPEN, trigger opportunistic next reviewer-round cycle, per handover §6 Step G explicit flag) + **OPEN-ORG-020** (Phase 7B context-overflow → lightweight-bootup-mode codification; status RESOLVED via Patch 0573 in same session; third same-session register-and-resolve pattern in CPP corpus history mirroring OPEN-ORG-013/014/008).
**Audit hypothesis:** likely N/A — handover §6 Step E says *"OPEN-ORG-018 status unchanged (template creation still deferred; no new OPEN-ORG registered or closed at Session 142)."* Patch 0574 should be either:
- (a) **No-op confirmation patch** documenting that organizational_frontier.md was audited at Phase 7B opening and required no changes from F.1 v1.0 SHIP, OR
- (b) **Small registration patch** if any of the post-SHIP follow-up items at handover §2 turn out to constitute a new OPEN-ORG candidate — e.g., the diagnostic-framing recurring-pattern at Patch 0569e + Round 6 resolution could codify a `templates/operating_system.md` §17 reviewer-protocol update as OPEN-ORG-NNN; this is registered as "deferred follow-up Patch" candidate in the handover.
- Recommend: read `organizational_frontier.md` §1 at session open. If any OPEN-ORG-NNN slot fits one of the post-SHIP follow-up items, register it as Patch 0574; otherwise ship Patch 0574 as a no-op confirmation noting audit-clean at this state.

**Anti-collision note:** organizational_frontier.md is updated by any session that registers an organizational item — check for concurrent additions at session open before insertion.

### §5.1 README.md — Patch 0575 candidate

**Target:** `README.md` (repo root)
**Landing status:** LANDED at Patch 0575 (Session 143, 25 May 2026). Five surgical edits applied: (1) Last-updated header prepend for F.1 v1.0 SHIP at Patch 0575; (2) F.1 Dynamical Substrate Law v1.0 SHIPPED bullet added to Programme Status Update "Major programme advancements" list after Capotauro v2.0 entry; (3) Forward queue paragraph updated — G1 publication-grade hardening (OPEN-FP-F1-3) added as recommended first post-Phase-7 substantive physics Patch + OPEN-SD-CHIR-PRIMITIVE manifestation (iv) status changed to "CLOSED at sketch-document Layer 3 via F.1 v1.0 SHIPPED" + manifestation (v) restated as OPEN-FP-F1-4 + summary "4 of 5 manifestations now closed"; (4) Registered Papers section header flagship count "5 flagships SHIPPED at v1.0" → "6 flagships SHIPPED at v1.0"; (5) Registered Papers narrative extended to include "F-Line flagship SHIPs: F.1 Dynamical Substrate Law v1.0 SHIPPED 24 May 2026". Theorem count NOT advanced from 67 (THEO-DSL-1/2/3 register at Patch 0581); swarm count NOT advanced from 108 (F.1 predictions land at Patch 0580). NOTE FOR FUTURE: content pack §5.1 anticipated a "flagship papers table" containing Capotauro/chirality_continuum rows — README actually has only the SF-line bullet list at lines 53-65; the Capotauro/chirality_continuum/F.1 paper-row entries live in `paper_catalog.md` (Patch 0576 target). Adding an F-line architectural description sub-section to README parallel to the existing SF-line description is a candidate follow-up beautification (NOT registered as formal organizational item at this Patch; surfaced for handover consideration).
**Insertion location:** Flagship papers table (search for the existing row containing "chirality_continuum" or "Capotauro" to find the F-line flagship table block). The F.1 paper should appear as a NEW ROW after the Capotauro / chirality_continuum rows.

**Pre-staged content block:**

| F.1 Dynamical Substrate Law | `flagship_papers/dynamical_substrate_law/` | v1.0 SHIPPED 2026-05-24 | First F-line flagship v1.0 SHIP in CPP corpus; substrate-locality of DI-bit currents at vertex-aligned Reading C; closes OPEN-SD-CHIR-PRIMITIVE manifestation (iv) at sketch-document Layer 3 |

(Adjust column count and exact column headers to match the in-place README table at edit time.)

**Also update:** the README flagship paper count (search for "flagship" + count of papers; F.1 v1.0 SHIP increments the F-line flagship count by 1).

**Anti-collision note:** README.md is occasionally touched for non-flagship updates (link refresh, narrative section); use the table anchor specifically, not the line-number top.

**Sanity checks:** verify that the row format matches existing F-line flagship rows (column count, status-string format, date format YYYY-MM-DD).

### §5.2 paper_catalog.md — Patch 0576 candidate

**Target:** `paper_catalog.md`
**Landing status:** LANDED at Patch 0576 (Session 143, 25 May 2026). Three surgical edits applied: (1) Last-updated header prepend for F.1 v1.0 SHIP catalog registration; (2) F.1 row inserted in SF-Line Flagship Papers table after Chirality Continuum row (table now contains 5 flagship paper rows: SF-2, SF-4, Capotauro, Chirality Continuum, F.1; SF-Line section header now contains four non-SF-N papers — Capotauro, Chirality Continuum, F.1, and Capotauro v2.0 v1.0 implicit in Capotauro row — rename to "Flagship Papers" is a candidate beautification deferred to handover); (3) F.1 Documentation paragraph inserted after Capotauro Documentation paragraph. **Ordinal correction in own prepend**: F.1 is the SEVENTH flagship v1.0 SHIP in CPP corpus (after SS-9, SF-4, SF-2, Capotauro v1.0, Capotauro v2.0 v1.0, Chirality Continuum), not sixth — Capotauro v1.0 and Capotauro v2.0 v1.0 counted as separate flagship ships per Chirality Continuum row precedent. **README.md flagship count drift**: at Patch 0575 the count advanced "5 flagships SHIPPED" → "6 flagships SHIPPED" reflecting F.1 only, but Chirality Continuum (sixth) was already missing from the pre-Patch-0575 count — README count should be 7 not 6; small bookkeeping correction deferred (NOT registered as formal organizational item; surfaced for handover consideration).
**Insertion location:** (1) `Last updated:` header (prepend new paragraph for F.1 v1.0 SHIP); (2) F-Line table (add new row for F.1 below Capotauro row).

**Last-updated frontier prepend (model after Patch 0457 Capotauro entry):**

```
**Last updated:** 25 May 2026 (Session 143 Patch 0576 — **F.1 Dynamical Substrate Law v1.0 SHIPPED post-SHIP catalog registration**: F.1 row added to F-Line table reflecting Session 142 Patch 0570 v1.0 SHIP. First F-line flagship v1.0 SHIP in CPP corpus; closes OPEN-SD-CHIR-PRIMITIVE manifestation (iv) at sketch-document Layer 3 via Theorem 7.1 substrate-locality umbrella with three publication-grade Layer 3 inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2). Three reviewers converged on SHIP-ready; ChatGPT R6 verdict strongest-positive of cycle. Frozen PDF at `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.pdf` (33 pages, 489 KB, MD5 49e56be92a3ccc126ce09210b5898794). 1240 lines `.tex` source. Three new theorem candidates (THEO-DSL-1/2/3) for theorem-registry.md per Patch 058N. Three hardened-theorem artifacts at `hardened_theorems/` (Patches 0550 + 0551 + 0552; 741 lines LaTeX combined). Five Open Problems in body §9 (OPEN-FP-F1-1 through OPEN-FP-F1-5) + OPEN-FP-F1-6 registered separately at Patch 0569e. Phase 7A SHIP-time companion suite landed at Patches 0572 → 0572a–0572i. Phase 7B programme-level registry updates underway at Patches 0573+; Phase 7C OSF deposit + anthology chapter at Patch 058N+1+.
```

**F-Line table row insertion (after Capotauro row):**

```
| F.1 | F.1 Dynamical Substrate Law | v1.0 SHIPPED | 2026-05-24 | OPEN-SD-CHIR-PRIMITIVE manifestation (iv) substrate-locality of DI-bit currents at vertex-aligned Reading C | Sketch-document Layer 3 (umbrella Theorem 7.1) + publication-grade Layer 3 trio (Theorems 5.1, 5.2, 6.1 + Corollary 6.2) | `flagship_papers/dynamical_substrate_law/` |
```

(Adjust column count and order to match in-place table at edit time.)

**Documentation paragraph (model after Capotauro Documentation paragraph):**

Add new paragraph after Capotauro Documentation paragraph, summarizing F.1's documentation suite: 7 SHIP-time companion files at `documentation_suite/` + 5 verification scripts at `code/` + frozen PDF + 8 reviewer letter files at `reviews/` + Tier 3/4 files (development-/transcript-/reasoning-dynamical-substrate-law.md) + changelog file. Patches 0554–0570 (paper assembly + v1.0 SHIP) + Patches 0571 (handover) + 0572 → 0572a–0572i (Phase 7A doc-suite) + 0573+ (Phase 7B registries) + 058N+1+ (Phase 7C OSF + anthology + verification).

**Anti-collision note:** paper_catalog.md is touched whenever ANY paper ships or revises. Use the F-Line table anchor specifically (search for "F.1 Dynamical Substrate Law" or "F-Line"). If any other paper has shipped concurrently, do NOT use a line-number-based edit — use grep-anchored str_replace on stable text near the insertion point.

**Sanity checks:** verify column count matches existing rows; verify the post-SHIP-of-other-paper bookkeeping has not changed table columns (e.g., a "predictions count" column added since v0.572 last touched).

### §5.3 INDEX.md — Patch 0577 candidate

**Target:** `INDEX.md`
**Landing status:** LANDED at Patch 0577 (Session 143, 25 May 2026). Audit found INDEX was already substantially populated at Patch 0572h (Phase 7A) with 9 F.1 entries (umbrella dynamical_substrate_law/ + .tex + .pdf + documentation_suite/ + code/ + hardened_theorems/ + reviews/ + reviewer_pause/ + sketches/) — exceeding the content pack's pre-staged single-entry expectation. Patch 0577 is therefore a **gap-fill audit**, not a major addition. Three post-Patch-0572h artifacts identified as missing from INDEX and added: (1) `layer3_promotion/` directory (5 Layer 3 promotion sub-question files preserving Tier-4 reasoning for B.1.d/q1/q2/q3/q4 closure trajectory; pre-existing but uncited at Patch 0572h); (2) `phase_7B_content_pack.md` (Patch 0573 execution scaffolding); (3) `development-transcripts/` directory (Patch 0572i curated transcripts directory + F1_transcript_session_143_phase_7a_opus.md). Plus Last-updated header prepend for Patch 0577 audit context. Note: existing Patch 0572h F.1 entries are NOT modified — the audit preserves prior entry content verbatim and adds gap-fill rows only.
**Insertion location:** Flagship papers section (`flagship_papers/` subsection). Add F.1 entry between Capotauro and any subsequent F-line papers (currently only F.1 exists at F-line).

**Pre-staged content block:**

```
- `flagship_papers/dynamical_substrate_law/` — F.1 Dynamical Substrate Law (v1.0 SHIPPED 2026-05-24, Session 142 Patch 0570). First F-line flagship v1.0 SHIP. Substrate-locality of DI-bit currents at vertex-aligned Reading C in the 600-cell. Closes OPEN-SD-CHIR-PRIMITIVE manifestation (iv) at sketch-document Layer 3.
  - `dynamical_substrate_law.tex` — Paper source (1240 lines)
  - `dynamical_substrate_law.pdf` — Frozen v1.0 SHIP PDF (33 pages, 489 KB, MD5 49e56be92a3ccc126ce09210b5898794)
  - `documentation_suite/` — 10 companion files (4 Tier 3/4 + 7 SHIP-time + 1 changelog)
  - `hardened_theorems/` — 3 publication-grade Layer 3 artifacts (Patches 0550 + 0551 + 0552)
  - `code/` — 5 verification scripts (Python stdlib + NumPy)
  - `reviews/` — 8 reviewer letter files (R1–R6 + synthesis)
  - `sketches/` — closure trajectory sketches + foundations work
  - `layer3_promotion/` — Layer-3 promotion arc artifacts
  - `reviewer_pause/` — reviewer-pause cycle artifacts
```

(Verify in-place format style; adjust nesting indentation if INDEX.md uses 4-space or tab.)

**Anti-collision note:** INDEX.md is touched whenever new top-level directories are added; use the flagship_papers/ anchor specifically.

**Sanity checks:** verify file paths exist (especially `code/`, `reviews/`, `sketches/`).

### §5.4 methods_catalogue.md — Patch 0578 candidate

**Target:** TBD at edit time — verify whether `methods_catalogue.md` (repo root, 213 lines) or `methods_catalogue/methods_catalogue.md` (subdirectory file, 184 lines) is canonical. If both exist as distinct documents, register METH-DSL-N entries in the canonical one and update the pointer in the other if needed.

**Landing status:** PENDING
**Insertion location:** Append METH-DSL-1 through METH-DSL-5 entries after the last existing METH-* entry (search for "METH-CHIR-CONT-4" as the most recent prior entry per handover history).

**Pre-staged content block:** see §4 of this pack — METH-DSL-1/2/3/4/5 entries. Each entry should follow the in-place format style of METH-CHIR-CONT-N entries (name, one-paragraph description, source patch, cross-paper-usage notes if any).

**Anti-collision note:** If any non-F.1 methods entries have been added concurrently (METH-CAP-N, METH-CHIR-CONT-5, etc.), splice in around them — METH-DSL-1 just needs to follow the last existing METH-* entry, doesn't need to be sequentially numbered with anything else.

**Sanity checks:** verify METH-DSL-N numbering is internally consistent (1, 2, 3, 4, 5); verify all referenced source patches (0570, 0569b, 0569e) are accurately cited.

**Bookkeeping note (do this at edit time):** if `methods_catalogue.md` (repo root) and `methods_catalogue/methods_catalogue.md` are duplicated content, register the OPEN-ORG candidate for reconciliation. If one is a pointer file (one-line "see [other path]"), this is a known pattern and no reconciliation needed.

### §5.5 future_projects.md — Patch 0579 candidate

**Target:** `future_projects.md`
**Landing status:** PENDING
**Insertion location:** F.1 row update — search for any existing F.1 / "Dynamical Substrate Law" / "OPEN-FP-F1-*" entries. Status should advance from "ACTIVE / closure trajectory" to "v1.0 SHIPPED; post-v1.0 trajectory queue".

**Pre-staged content (if F.1 row exists, str_replace; if not, append new row):**

```
### F.1 Dynamical Substrate Law

**Status:** v1.0 SHIPPED at Session 142 Patch 0570 (24 May 2026). First F-line flagship v1.0 SHIP in CPP corpus.
**Paper:** `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` + frozen PDF at `dynamical_substrate_law.pdf`
**Closes:** OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow — at **sketch-document Layer 3 only** (Theorem 7.1 umbrella; not independently hardened).
**Post-v1.0 trajectory queue (recommended priority order):**
1. **G1 publication-grade hardening (OPEN-FP-F1-3)** — RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent priority. Would produce `hardened_theorems/first_shell_inner_product_primitive.tex` parallel to Patches 0550/0551/0552 trio structure. Unlocks unconditional publication-grade Layer 3 status for Theorems 5.1 + 5.2 + strengthens Theorem 7.1 umbrella footing. Estimated 1–2 sessions.
2. **OPEN-FP-F1-1 extension to $\mathcal{O}(\delta^2)$** — substantive geometric + perturbation-theory project at higher order; introduces second-shell geometry. Estimated multi-session project.
3. **OPEN-FP-F1-2 Layer 4 axiomatic derivation of Mechanism A** — derive MA.1 + MA.2 from CPP primitive axioms A1–A11. Long-term programme target; multi-Patch trajectory.
4. **OPEN-FP-F1-4 Sector-5 schema instantiation** — manifestation (v) closure target.
5. **OPEN-FP-F1-5 Non-vertex-aligned Reading C variants** — edge-aligned + face-aligned Reading C variants; methodologically tractable but not yet attempted.
6. **OPEN-FP-F1-6 prose-density tightening** — addressable by F.1-condensed companion paper trajectory at Theorem 6.1 + Corollary 6.2 + Theorem 7.1 scope with minimal CPP interpretation; for academic submission.
7. **Substrate-locality umbrella publication-grade hardening** — Theorem 7.1 promotion from sketch-document to publication-grade L3 via independent hardened-theorem artifact (§7.4 candidate follow-up Patch; not formal Open Problem to preserve in-body 5-OP commitment).
```

**Cross-paper integration (also update):** if SF-2 / SM-5 / Capotauro / chirality_continuum / SF-4 entries in future_projects.md reference F.1 as gate or dependency, update those references to "SHIPPED at v1.0".

**Anti-collision note:** future_projects.md is structured with per-paper subsections; use the F.1-specific anchor or insertion-point grep, not a line range.

**Sanity checks:** verify the 6 OPEN-FP-F1-N IDs are not duplicated or mis-numbered; verify the priority ordering reflects ChatGPT R1–R6 convergent priority and not an arbitrary reorder.

### §5.6 predictions.md — Patch 0580 candidate

**Target:** `predictions.md`
**Landing status:** PENDING
**Insertion location:** (1) Update `Last updated:` header with frontier-prepend paragraph; (2) Append F.1 prediction entries (PRED-O-N1 through PRED-O-N5 + optional PRED-O-N6) after the last existing PRED-O-NN entry (verify current highest PRED-O number at edit time).

**Frontier-prepend paragraph (model after recent prepends):**

```
**Last updated:** 25 May 2026 (Session 143 Patch 0580 — **F.1 Dynamical Substrate Law v1.0 SHIPPED predictions registration**: 5 paper-body + 1 grouped foundations-work predictions registered as PRED-O-N1 through PRED-O-N5(+N6). F.1 predictions are structural mathematical constants (host-to-first-shell uniform projection -1/(2φ); first-shell unit-vector sum identity; icosahedral rank-1 sum identity; substrate-locality umbrella coefficient 6/φ²; first-shell-to-first-shell edge perpendicularity), not empirical-comparison predictions in the SS-7 / SF-4 sense. Cross-sector consistency check: -1/(2φ) is shared identically with Capotauro v2.0 §3 spatial-sector substrate-locality theorem; ê_{ij}·n̂=0 perpendicularity is the same identity as Capotauro v2.0 §5.6 K3-base protection. All paper-body predictions numerically verified in `flagship_papers/dynamical_substrate_law/code/`.
```

**Entry blocks for PRED-O-N1 through N5 (and optional N6):** see §2 of this pack for the per-prediction content. Each entry should follow the in-place format style of existing PRED-O-NN entries.

**Anti-collision note:** verify PRED-O-NN numbering at edit time; the highest existing number may have advanced since Session 142.

**Sanity checks:** verify each prediction's numerical value at machine precision (e.g., $-1/(2\phi) = -0.309017$); verify the cited verification scripts exist; verify the theorem-source references to F.1 sections.

### §5.7 theorem-registry.md — Patch 0581 candidate

**Target:** `theorem-registry.md`
**Landing status:** PENDING
**Insertion location:** (1) Update `Last updated:` header with frontier-prepend paragraph for F.1 v1.0 SHIP + 3 theorem candidates; (2) Insert a new "F-Line" sub-section (or extend existing F-Line section if it exists) with THEO-DSL-1, THEO-DSL-2, THEO-DSL-3 entries; (3) Update Summary Statistics table (F-Line row OR add F-Line row if not yet present; Total theorem count +3 from 67 → 70).

**Theorem candidate full statements:**

**THEO-DSL-1 (Perturbation-Theory Propagation Rule + Shell-Locality at $\mathcal{O}(\delta^1)$):**
Under the framework axioms MA.1 + MA.2 (Mechanism A propagation-rate asymmetry + framework-local current construction) on the 600-cell substrate's edge graph, the DI-bit current at any vertex $v$ at first order in the asymmetry parameter $\delta$ depends only on edges incident to $v$ or to vertices within graph-distance 1 of $v$. Equivalently: the substrate current at any vertex beyond the first shell of the host vertex receives no $\mathcal{O}(\delta^1)$ contribution from Mechanism A. **Hardened-theorem artifact:** `hardened_theorems/perturbation_locality_propagation.tex` (Patch 0550). **Falsifier:** demonstration of a first-order-in-$\delta$ contribution at any vertex beyond first-shell range. **Layer rigor:** publication-grade Layer 3, unconditional. **CPP axiom dependencies:** A1, A2, A3, A4, A7 + framework axioms MA.1 + MA.2. **Source:** Theorem 6.1 + Corollary 6.2 of `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` v1.0.

**THEO-DSL-2 (First-Shell Geometric Identities at Vertex-Aligned Reading C, conditional on G1):**
At vertex-aligned Reading C in the 600-cell with substrate-direction primitive $\hat{n} = \vhost / |\vhost|$, the 12 first-shell unit vectors $\hat{u}_i$ satisfy: (a) **uniform projection** $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ identically across all 12 first-shell neighbours (Theorem 5.1); (b) **first-shell-to-first-shell edge perpendicularity** $\hat{e}_{ij} \cdot \hat{n} = 0$ for all 30 first-shell-to-first-shell edges (Theorem 5.2). **Hardened-theorem artifacts:** `hardened_theorems/host_first_shell_uniform_projection.tex` (Patch 0552) + `hardened_theorems/first_shell_perpendicularity.tex` (Patch 0551). **Falsifier set:** see §1 of this pack. **Layer rigor:** publication-grade Layer 3, **conditional on G1** (first-shell inner-product primitive; G1 publication-grade hardening is OPEN-FP-F1-3 RECOMMENDED first post-Phase-7 substantive physics Patch). **CPP axiom dependencies:** A1, A2, A4, A7 + framework axiom G1 (inherited from Capotauro Patch 0541 §3.1 at sketch-document Layer 3). **Cross-sector consistency:** $-1/(2\phi)$ identical to Capotauro v2.0 §3 spatial-sector substrate-locality theorem. **Source:** Theorems 5.1 + 5.2 of F.1 v1.0.

**THEO-DSL-3 (Substrate-Locality Umbrella; sketch-document Layer 3):**
Under MA.1 + MA.2 + vertex-aligned Reading C + Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2, the closed-form first-order-in-$\delta$ DI-bit current at the host vertex of the 600-cell at vertex-aligned Reading C takes the form $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$. **Layer rigor:** sketch-document Layer 3 — assembly of Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2 via the icosahedral rank-1 sum identity $\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = (3/\phi^2)\,\hat{n}$; not independently hardened. Independent publication-grade hardening is a §7.4 candidate follow-up Patch (not formal Open Problem to preserve in-body 5-OP commitment). **Falsifier:** demonstration of a different prefactor on $\hat{n}$ at $\mathcal{O}(\delta^1)$ from any valid first-principles 600-cell + Mechanism A calculation, or any tangent-to-$\hat{n}$ component at first order. **CPP axiom dependencies:** A1, A2, A3, A4, A7 + framework axioms MA.1 + MA.2 + G1 (via inheritance from THEO-DSL-2). **Source:** Theorem 7.1 of F.1 v1.0.

**Closure significance:** F.1 is the **first F-line flagship** in CPP corpus to register theorem-registry entries. The THEO-DSL-N sub-prefix convention is introduced at this patch, paralleling THEO-CHIR-CONT-N (chirality_continuum) and THEO-CAP-N (Capotauro) conventions. THEO-DSL-1 + THEO-DSL-2 + THEO-DSL-3 jointly close OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow at sketch-document Layer 3 — the **fourth manifestation of OPEN-SD-CHIR-PRIMITIVE to close** (manifestations (i)+(ii)+(iii) closed in Capotauro v2.0 / chirality_continuum at Layer 3; manifestation (v) remains OPEN as OPEN-FP-F1-4).

**Summary Statistics update:**
- F-Line row: introduce (or update) entry — 3 theorems + 0 propositions + 0 lemmas (THEO-DSL-1/2/3 are theorems; Lemmas 5.2.1, 6.1.1, 6.2.1, 6.3.1 are paper-internal lemmas not registered at programme level per the F.1 v1.0 SHIP convention).
- Total theorem count: 67 → 70 (+3).
- Theorems:Axioms ratio: update from current value to (70 + corollaries) / 9. **NB:** corollary counting convention — Corollary 6.2 is bundled with Theorem 6.1 in THEO-DSL-1 per the paper's structure (Corollary 6.2 is an immediate corollary of Theorem 6.1, not a standalone theorem candidate); if your registry style counts corollaries separately, add +1 corollary for Corollary 6.2.

**Frontier-prepend paragraph (model after Patch 0440 / Patch 0487 / Patch 0509 entries):** to be drafted at edit time using the THEO-DSL-1/2/3 content above; should be comparable in detail to those precedent entries (each was ~5-15 paragraphs of context).

**Anti-collision note:** theorem-registry.md is a high-traffic file (every paper ships with a theorem-registry update). Pre-check at session open whether any THEO-* IDs have advanced since the last F-line update; if a THEO-DSL-N number conflicts with a concurrent registration, advance the F.1 IDs (THEO-DSL-1 unique to F.1 should not conflict).

**Sanity checks:** verify the three hardened-theorem artifact files exist at `hardened_theorems/`; verify Patch numbers (0550, 0551, 0552) are correct; verify cross-section consistency claim with Capotauro v2.0 §3 is accurate (cross-check at Capotauro v2.0 substrate-locality theorem statement); verify the 5-OP body §9 commitment is preserved (theorem-registry should reference OPEN-FP-F1-1 through -5 as in-body opens, OPEN-FP-F1-6 as separately registered).

### §5.8 master_glossary.md — Patch 0582 candidate

**Target:** `master_glossary.md`
**Landing status:** PENDING
**Insertion location:** Each new entry inserted in alphabetical order within the existing glossary structure. The 15 terms (see §3 of this pack) cover Constants (3 entries), Structural terms (5 entries), Mechanism terms (3 entries), Methodology terms (4 entries).

**Pre-staged content:** see §3 above. Each glossary entry follows the in-place format: term name + bolded; brief definition; first-use reference; cross-references to related terms.

**Anti-collision note:** master_glossary.md is touched by any paper that introduces new terms. Alphabetical ordering provides natural collision-avoidance; check before insertion whether any concurrent additions occupy alphabetical neighbours.

**Sanity checks:** verify alphabetical ordering is preserved; verify no entry duplicates an existing master_glossary entry (especially for $\phi$, golden ratio, 600-cell, $H_3$/$H_4$ — these may already have entries from prior papers).

**Glossary section structure note:** the in-place glossary may organize by section (Constants / Structural / Methodology / Mechanism); follow the existing structure rather than inventing new section headers. If existing structure is purely alphabetical, integrate that way.

### §5.9 programme_orientation.md — Patch 0583 candidate

**Target:** `programme_orientation.md`
**Landing status:** PENDING
**Insertion location:** Multiple updates:
1. **One-Paragraph summary** (front matter) — update flagship paper count + manifestations-of-OPEN-SD-CHIR-PRIMITIVE-closed count.
2. **Net scorecard / Predictions scorecard** (Part VIII per bootup pointer) — F.1 contributes 5-6 structural-constant predictions at zero parameters; integrate into scorecard table.
3. **Papers-in-active-corpus** — update F.1 entry from "ACTIVE / in development" to "v1.0 SHIPPED 2026-05-24"; update F-line description if it currently says "no F-line flagships yet" or similar.
4. **F.1 dynamical-substrate-law gate status** — update from "OPEN" to "v1.0 SHIPPED at sketch-document Layer 3; OPEN-FP-F1-3 G1 publication-grade hardening RECOMMENDED first post-Phase-7 substantive physics Patch".
5. **Chirality continuum closure narrative** — extend with F.1 closure of manifestation (iv); update the table of manifestation closures (manifestations (i)+(ii)+(iii) closed in Capotauro v2.0 / chirality_continuum; manifestation (iv) closed in F.1 at sketch-document L3; manifestation (v) OPEN as OPEN-FP-F1-4).

**Anti-collision note:** programme_orientation.md is touched by every flagship v1.0 SHIP. Use semantic anchors (search for "chirality continuum", "F-line", "OPEN-SD-CHIR-PRIMITIVE", "manifestation (iv)") rather than line numbers.

**Sanity checks:** verify Net scorecard math (existing zero-parameter prediction count + F.1's 5-6 = new total); verify the chirality continuum table reflects 4/5 manifestations closed after F.1 v1.0 SHIP.

### §5.10 research_frontier.md — Patch 0584 candidate (LIKELY SMALL OR N/A)

**Target:** `research_frontier.md`
**Landing status:** PENDING — but likely already partially landed at Patch 0570 per handover §6 Step E.
**Audit hypothesis:** handover §6 Step E says *"research_frontier.md: ✓ — F.1 v1.0 SHIP frontier prepend at Patch 0570 + Patch 0571 handover prepend."* This suggests the frontier prepend is already done. However, the F.1 sub-question status update from "ACTIVE Layer 3 promotion at Patch 0540-trajectory" → "SHIPPED at v1.0 Patch 0570; v2.0+ trajectory via OPEN-FP-F1-3 G1 hardening recommended first post-SHIP" may still need to be applied as an inline status-field update at the F.1 entry.

**At edit time:** read `research_frontier.md` and search for "F.1" / "dynamical substrate law" / "OPEN-SD-CHIR-PRIMITIVE manifestation (iv)" to locate the existing entry. If status field already says "SHIPPED at v1.0", this patch is N/A or a no-op confirmation. If status field still says "ACTIVE" or "Layer 3 promotion", update it.

**Pre-staged status-field update text (if needed):**

```
**Status:** SHIPPED at v1.0 Patch 0570 (Session 142, 24 May 2026); first F-line flagship v1.0 SHIP in CPP corpus; closes manifestation (iv) of OPEN-SD-CHIR-PRIMITIVE at **sketch-document Layer 3** only (Theorem 7.1 umbrella; not independently hardened). Post-v1.0 trajectory queue: **OPEN-FP-F1-3 G1 publication-grade hardening** is the RECOMMENDED first post-Phase-7 substantive physics Patch per ChatGPT R1–R6 convergent priority. Six in-body Open Problems registered (OPEN-FP-F1-1 through OPEN-FP-F1-5 in body §9; OPEN-FP-F1-6 prose-density tightening registered separately at Patch 0569e).
```

**Anti-collision note:** research_frontier.md is the highest-traffic registry in the corpus — every session-close potentially touches the frontier-prepend. Be very careful with line-anchored edits; use stable inline anchors.

**Sanity checks:** verify the F.1 sub-question status field is internally consistent with the F.1 v1.0 SHIPPED state in `paper_catalog.md` (cross-check at edit time).

### §5.11 axiom-registry.md — N/A by audit

**Target:** `axiom-registry.md`
**Landing status:** **N/A by audit** — handover §6 Step E says *"axiom-registry.md: N/A — no new axioms at F.1 v1.0; axioms unchanged at 9."* No patch is required for axiom-registry as part of Phase 7B.

**At edit time:** confirm the axiom count is still 9 (A1–A8' + A11) and that F.1's framework axioms (MA.1 + MA.2) are correctly classified as framework axioms (Layer 3) rather than primitive axioms (Layer 4) — i.e., they should NOT appear in axiom-registry. If they have somehow been added there, remove them. Otherwise, no work.

---

## §6. Recommended Phase 7B execution order

The ordering below follows the Session 142 close diagnostic — smallest target → largest target — to build momentum and reserve harder ones for fresh windows. Each line is **one patch per session**.

| Patch | Target | This-pack section | Estimated work |
|---|---|---|---|
| 0574 | `organizational_frontier.md` audit | §5.0 | small / N/A confirmation |
| 0575 | `README.md` | §5.1 | small (one table row + count) |
| 0576 | `paper_catalog.md` | §5.2 | small-medium (header prepend + row + documentation paragraph) |
| 0577 | `INDEX.md` | §5.3 | small (one structured entry) |
| 0578 | `methods_catalogue.md` | §5.4 | medium (5 method entries) |
| 0579 | `future_projects.md` | §5.5 | medium (F.1 row + cross-paper integration) |
| 0580 | `predictions.md` | §5.6 | medium (header prepend + 5-6 entries) |
| 0581 | `theorem-registry.md` | §5.7 | medium-large (header prepend + 3 theorem entries + Summary Stats) |
| 0582 | `master_glossary.md` | §5.8 | medium (15 alphabetical insertions) |
| 0583 | `programme_orientation.md` | §5.9 | medium-large (multi-point updates) |
| 0584 | `research_frontier.md` | §5.10 | small (likely status-field update only) |
| — | `axiom-registry.md` | §5.11 | **N/A by audit; no patch** |

**Total: ~11 substantive patches.** Plus this Patch 0573 (content pack + bootup.md §3.5). After Patch 0584 closes Phase 7B, Phase 7C opens with OSF deposit + anthology chapter + H1–H5 verification (estimated 2-3 patches). Total Phase 7 effort: ~13-14 patches (excluding the content pack itself).

---

## §7. Phase-7B-mode lightweight bootup (the matched directive in `bootup.md` §3.5)

Per Patch 0573, `bootup.md` §3.5 adds a "Phase-7B-mode lightweight bootup" subsection. **Sessions executing Patches 0574 through 0584 read this content pack + the listed minimal files only, NOT the full priority-read list.** The full priority-read list (§Step 1 of bootup.md) is the right protocol for physics work / paper development / discovery sessions; it is overkill for surgical registry-update sessions and was the empirical cause of the Phase 7B overflow that prompted this content pack's creation.

Lightweight bootup checklist for Patches 0574–0584:
1. `bootup.md` §3 + §3.5 (patch contract + Phase-7B-mode directive) — ~100 lines combined
2. Latest handover at `handovers/` — ~150 lines
3. THIS FILE (`flagship_papers/dynamical_substrate_law/phase_7B_content_pack.md`) — ~600 lines
4. The ONE target registry — varies 200–1850 lines
5. (Optional) `templates/operating_system.md` §15 Step E + §16 anti-collision — grep-extracted, ~200 lines

**Total lightweight bootup: ~1,000–2,500 lines** (vs ~7,000 for full bootup; vs ~17,500 if the F.1 paper + doc suite are also re-read).

---

## §8. Sanity-check anti-rebuttal (for reviewer-facing claims)

If a reviewer (especially ChatGPT) flags an inconsistency between this pack's claims and the paper's actual content, the canonical authority order is:
1. `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED frozen at Patch 0570; the source of truth for the paper's claims)
2. `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.pdf` (the frozen v1.0 PDF; visual rendering)
3. The companion files in `flagship_papers/dynamical_substrate_law/documentation_suite/` (Phase 7A SHIP-time curation)
4. This content pack (Phase 7B execution scaffolding; derived from above)
5. The Phase 7B registry entries (downstream from this pack)

If any conflict exists between #4 and #1/2/3, **trust 1/2/3 and update this pack** before propagating to registries. Errors in this pack should not propagate into the programme-level registries.

---

## §9. Post-Phase-7B handover preparation

When Patch 0584 ships (closing Phase 7B), the Session-N close handover should:
- Mark all 11 registry entries above as `LANDED` (cross-reference the patch number that landed each)
- Tee up Phase 7C: OSF deposit + anthology chapter + H1–H5 verification
- Cross-reference the next substantive physics Patch: OPEN-FP-F1-3 G1 publication-grade hardening (`hardened_theorems/first_shell_inner_product_primitive.tex`)
- Note this pack's retirement (Phase 7C close = retire or archive)

---

## §10. Open questions for Thomas at any Patch 0574+ session open

If anything in this pack looks stale (e.g., another paper has shipped concurrently and registry contents have advanced), the session-opening AI should flag it explicitly rather than proceed on stale assumptions. Specifically:
- Has any other flagship paper shipped since Patch 0573 close that might have changed registry column structures?
- Have any METH-CHIR-CONT-5+ or METH-CAP-5+ entries been added that might shift methods_catalogue.md numbering conventions?
- Has the predictions.md PRED-O-NN counter advanced since Patch 0573 close?
- Has axiom-registry.md gained any new axioms that would invalidate the §5.11 N/A claim?
- Has the in-place format style of any target registry drifted from the assumptions in this pack?

Asking these at session open prevents stale-pack-driven errors.

---

*Content pack created Session 143 Patch 0573 (25 May 2026) as the Phase 7B initialization artifact. Retire or archive at Phase 7C close.*
