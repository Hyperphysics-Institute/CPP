# Dynamical Substrate Law — F.1 Flagship Paper Folder

**Status: v1.0 SHIPPED (Session 142 close, 24 May 2026, Patch 0570)**

This folder contains the *Dynamical Substrate Law* flagship paper of the CPP corpus — **the first F-line flagship v1.0 SHIP in CPP corpus history.** The paper closes OPEN-SD-CHIR-PRIMITIVE manifestation (iv) thermodynamic causal arrow at **sketch-document Layer 3** via Theorem 7.1 substrate-locality umbrella, establishing the closed-form first-order DI-bit current at the host vertex:

$$\vec{j}_{DI}^{\text{net}}(\vhost) = \frac{6\delta}{\phi^2}\,\hat{n} + \mathcal{O}(\delta^2)$$

at vertex-aligned Reading C in the 600-cell substrate under Mechanism A (the propagation-rate-asymmetry primitive $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$). The structural constant $6/\phi^2 \approx 2.293$ is universal for the temporal sector and emerges from the icosahedral residual symmetry $H_3 = I_h$ at the host vertex + the first-shell host-to-first-shell uniform projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ — the same projection constant Capotauro v2.0 §3 uses for spatial-sector substrate-locality.

**Important scope clarification preserved end-to-end:** F.1 closes manifestation (iv) at the *substrate-locality structure* level only. The candidate thermodynamic-arrow emergence narrative (entropy production / coarse-graining / macroscopic irreversibility in the conventional physics sense) is *supported by* but *not derived from* the closure. The emergence layer is registered as future work beyond the present paper's framework qualifiers (§10 explicit disclaimer). This honesty-of-scope discipline — operationalised throughout the paper and codified as the **anti-erasure discipline** at §8.3 — is the central methodological commitment of the F.1 v1.0 SHIP.

The paper is the **seventh flagship paper to v1.0 in the CPP corpus** (after SS-9 Session 32, SF-4 Session 54, SF-2 Session 83, Capotauro v1.0 Session 122, Capotauro v2.0 Session 135, Chirality Continuum Session 137) and the **third flagship paper outside the SF-N numerical convention** (after Capotauro and Chirality Continuum). It is the first paper in the F-line flagship series proper; the F-line trajectory is the dynamical-substrate-law programme target identified by all three external reviewers at the chirality continuum v1.0 SHIP cycle as the defining next programme gate.

## Paper-type declaration

The paper-type is **structurally-grounded sketch-document Layer 3 flagship framework preprint with publication-grade hardened components but non-publication-grade umbrella theorem** — a nine-word declaration that summarises the Layer-rigor architecture and is captured in the title-page scope subtitle (Variant b `\date{}` line scope-framing pattern; corpus-establishing for future F-line flagship trajectories with similar Layer-distinction structure). The four claims of the declaration:

- **"Structurally-grounded"** — the paper rests on three publication-grade Layer 3 hardened-theorem artifacts at `hardened_theorems/` (Patches 0550 + 0551 + 0552; 741 lines LaTeX combined).
- **"Sketch-document Layer 3"** — the umbrella theorem (Theorem 7.1) assembly is at sketch-document Layer 3, not publication-grade; independent hardening is a candidate follow-up Patch.
- **"Flagship framework preprint"** — first F-line flagship paper; preprint rather than finished publication because key follow-up work (G1 hardening, umbrella hardening, Layer 4 derivation) is registered as Open Problems.
- **"Publication-grade hardened components but non-publication-grade umbrella theorem"** — the components-vs-umbrella Layer distinction is the central honesty commitment.

## Cross-reviewer convergent verdict at v1.0 SHIP

- **Grok Round 1** (Patch 0568 archival): EXPLICIT *"v1.0 SHIP-acceptable as the F.1 flagship paper"*. Decisive sign-off; zero structural gaps in the load-bearing arc; four minor polish items.
- **Copilot Round 1** (Patch 0568 archival): implicit SHIP-acceptable with Tier 1/Tier 2/Tier 3 ranked-recommendation framework. Tier 1: G1 hardening + umbrella hardening.
- **ChatGPT six-round trajectory** (Patches 0568 → 0569e): monotonic verdict improvement from R1 *"NOT yet publication-grade flagship overall"* to **R6** *"substantially more credible, rigorous, and publishable than all earlier versions; first version that feels architecturally stable, epistemically disciplined, mathematically centered, structurally self-aware"* (strongest-positive). R6 was the first round with PDF upload (instead of `.tex` source); the diagnostic resolution at R6 identified the Rounds 3–5 recurring-pattern recommendations as a **TikZ-rendering processing artifact** — `\begin{tikzpicture}...\end{tikzpicture}` code was unrendered in raw `.tex` source.

## Three programme-level conventions extended at this SHIP

1. **`METH-VARIANT-B-SCOPE-SUBTITLE`** — Variant (b) `\date{}` line scope-subtitle pattern for v1.0 SHIP framing of Layer 3 + sketch-document content with explicit honesty-of-scope.
2. **`METH-PDF-UPLOAD-DEFAULT-REVIEWER`** — PDF-upload-default protocol for ChatGPT reviewer engagement (especially for papers containing TikZ figures + bibliography environments + LaTeX content requiring compilation).
3. **`METH-GITIGNORE-FLAGSHIP-PDF-EXCEPTION`** — `.gitignore` exception pattern `!flagship_papers/*/*.pdf` for v1.0+ SHIP PDFs (the F.1 v1.0 PDF is the first flagship PDF committed deliberately).

## Contents

| Path | Description |
|------|-------------|
| `README.md` | This file — F.1 flagship-paper home overview at v1.0 SHIPPED state |
| `dynamical_substrate_law.tex` | F.1 v1.0 SHIPPED paper source (1240 lines; 33 pages compiled PDF). 10 sections; theorem inventory: Lemmas 5.2.1 + 6.1.1 + 6.2.1 + 6.3.1 + Theorems 5.1 (host-to-first-shell uniform projection, pub-grade Layer 3 conditional on G1) + 5.2 (first-shell-to-first-shell perpendicularity, pub-grade Layer 3 conditional on G1) + 6.1 (perturbation-theory propagation rule, pub-grade Layer 3 unconditional) + Corollary 6.2 (shell-locality at $\mathcal{O}(\delta^1)$, pub-grade Layer 3) + 7.1 (substrate-locality umbrella, sketch-document Layer 3) |
| `dynamical_substrate_law.pdf` | F.1 v1.0 SHIPPED compiled PDF (33 pages, 489 KB, MD5 `49e56be92a3ccc126ce09210b5898794`). First flagship paper PDF committed deliberately at v1.0 SHIP per the `.gitignore` exception pattern adopted at Patch 0570 apply-fix |
| `documentation_suite/` | F.1 documentation suite at v1.0 SHIPPED (Phase 7A doc-suite production sub-arc Patches 0572 + 0572a–g, Session 143). 10-file suite: 7 SHIP-time companion files (changelog + keywords + reviews + mechanism + glossary + phenomena + philosophy) + 3 Tier files (transcript Tier 2 / development Tier 3 / reasoning Tier 4) |
| `code/` | F.1 verification scripts + `INDEX.md` doubling as B1–B5 verification notebooks audit document (Patch 0572g). 5 scripts (Python stdlib + NumPy only): `verify_phase1.py` (Net DI-bit current at host vertex; 4 identities verified including substrate-locality umbrella closed-form; B3 directly executed at audit time — PASS) + `verify_b1q2_curl_content.py` (B.1.q2 discrete curl vanishing) + `verify_b1q4_first_shell_current_sum.py` (B.1.q4 first-shell-vertex current magnitude + sum) + `verify_phase3.py` + `verify_phase4.py` (foundations-work artifacts; thermodynamic-arrow-emergence-related; out-of-scope for paper body) |
| `hardened_theorems/` | F.1 publication-grade Layer 3 hardened-theorem trio (Patches 0550 + 0551 + 0552; 741 lines LaTeX combined). `perturbation_locality.tex` (underpinning §6) + `first_shell_perpendicularity.tex` (underpinning §5.4 Theorem 5.2) + `host_first_shell_projection.tex` (underpinning §5.3 Theorem 5.1). Each with explicit hypothesis tracking + five-class exclusion enumeration. **The hardened-theorems trio convention is corpus-establishing for F-line flagship trajectories.** |
| `reviews/` | F.1 review archive. 9 reviewer letters + 1 synthesis at v1.0 SHIP archived across Patches 0568–0569e: Copilot R1 + Grok R1 + ChatGPT R1 through R6 + Round 1 synthesis classification |
| `reviewer_pause/` | F.1 reviewer-pause cycle artifacts (canonical worked example for `templates/operating_system.md` §17 + checklist Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work added Patch 0539a). 4 artifacts spanning Phase 2 foundations + Layer 3 promotion |
| `sketches/` | F.1 working sketches (Tier-4 reasoning capture). 4 sketches: `F1_phase2_foundations_work.md` + `F1_subquestion_pcd_orientation_link.md` + `F1_layer3_promotion_scoping.md` + `F1_flagship_paper_assembly_scoping.md` |

## Theorem inventory at v1.0 SHIP

The paper proves 4 theorems + 1 corollary at publication-grade Layer 3 (the first two conditional on G1) + 1 theorem at sketch-document Layer 3 (the umbrella), plus 4 supporting lemmas:

- **Theorem 5.1** (host-to-first-shell uniform projection; publication-grade Layer 3, conditional on G1) — for any first-shell unit vector $\hat{u}_i$ of $\vhost$, $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniformly across the 12 first-shell neighbours.
- **Theorem 5.2** (first-shell-to-first-shell perpendicularity; publication-grade Layer 3, conditional on G1) — for any first-shell-to-first-shell edge $\hat{e}_{ij}$, $\hat{e}_{ij} \cdot \hat{n} = 0$.
- **Theorem 6.1** (perturbation-theory propagation rule; publication-grade Layer 3 unconditional) — the $\mathcal{O}(\delta^n)$ coefficient of the substrate current at any vertex depends only on edges within graph-distance $n$ on the 600-cell edge graph.
- **Corollary 6.2** (shell-locality at $\mathcal{O}(\delta^1)$; publication-grade Layer 3) — immediate corollary specialising Theorem 6.1 at $n=1$.
- **Theorem 7.1** (substrate-locality umbrella; sketch-document Layer 3) — closed-form expression $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\,\hat{n} + \mathcal{O}(\delta^2)$.

Supporting Lemmas: 5.2.1 (tangent-hyperplane chord length); 6.1.1 (path-amplitude expansion); 6.2.1 (perturbed-step counting); 6.3.1 (connected-subgraph confinement). Imported Lemma: G1 (first-shell inner-product primitive; sketch-document Layer 3; publication-grade hardening is OPEN-FP-F1-3).

## Open Problems registered at v1.0 SHIP

Five Open Problems registered in body §9 with explicit independence analysis:

- **OPEN-FP-F1-1** — Extension to $\mathcal{O}(\delta^2)$ (higher-order corrections; second-shell inner-product + edge-projection identities).
- **OPEN-FP-F1-2** — Layer 4 axiomatic derivation of Mechanism A from CPP primitive axioms A1–A11 (long-term programme target).
- **OPEN-FP-F1-3** — G1 publication-grade hardening (**RECOMMENDED first post-Phase-7 substantive physics Patch** per ChatGPT R1–R6 convergent "single highest-value next action" priority).
- **OPEN-FP-F1-4** — Sector-5 schema instantiation (manifestation (v) of OPEN-SD-CHIR-PRIMITIVE; candidate domains: thermal-equilibrium gauge fixing, symmetry-restoration dynamics, cosmological-arrow alignment).
- **OPEN-FP-F1-5** — Non-vertex-aligned Reading C variants (edge-aligned $D_3$ + face-aligned $D_2$).

Plus **OPEN-FP-F1-6** prose-density tightening (registered separately at Patch 0569e from ChatGPT R6 follow-up to preserve in-body 5-OP commitment).

## v2.0+ post-SHIP trajectory

Post-Phase-7 priority queue per ChatGPT R1–R6 convergent guidance:

1. **OPEN-FP-F1-3 G1 publication-grade hardening** — produces `hardened_theorems/first_shell_inner_product_primitive.tex` parallel artifact to the existing trio; upgrades Theorems 5.1 + 5.2 from publication-grade Layer 3 conditional on G1 to publication-grade Layer 3 unconditional; consequently upgrades Theorem 7.1's conditionality clause. Estimated 1–2 sessions.
2. **OPEN-FP-F1-1 extension to $\mathcal{O}(\delta^2)$** — substantive geometric and perturbation-theory project at higher order.
3. **OPEN-FP-F1-2 Layer 4 axiomatic derivation of Mechanism A** — long-term programme target; multi-Patch trajectory.
4. **Substrate-locality umbrella publication-grade hardening** (§7.4 candidate follow-up Patch; not formal Open Problem to preserve 5-OP commitment) — produces a dedicated `hardened_theorems/*.tex` artifact for Theorem 7.1 itself.
5. **OPEN-FP-F1-6 prose-density tightening** + **F.1-condensed companion paper trajectory** — shorter geometry/locality paper focused on Theorem 6.1 + Corollary 6.2 + Theorem 7.1 with minimal CPP interpretation; depends on G1 hardening at OPEN-FP-F1-3 closure.

## Cross-paper consistency at v1.0 SHIP

- **Capotauro v2.0 §3 spatial-sector parallel** (§5.6 cross-reference in F.1): shared structural constant $-1/(2\phi)$ in the first-shell host-to-first-shell projection; shared first-shell-to-first-shell perpendicularity identity (the K3-base protection identity).
- **Chirality continuum closure pattern**: 4 of 5 OPEN-SD-CHIR-PRIMITIVE manifestations now closed at Layer 3 — (i)–(iii) at Capotauro v2.0 spatial sector + (iv) at F.1 temporal sector at sketch-document Layer 3. Manifestation (v) open as OPEN-FP-F1-4.
- **CPP corpus track record grounding**: F.1's substrate-locality umbrella extends the swarm-validation track record (SS-7 + SS-2 + SS-4 + SS-5 + SM-8 + SF-4 + SF-2 + Capotauro v1.0 + Capotauro v2.0 + Chirality Continuum + F.1) into the temporal sector at sketch-document Layer 3 honesty level.

## Reviewer-pause cycle convention precedent

F.1 trajectory is the **canonical worked example** for the reviewer-pause cycle precondition codified at `templates/operating_system.md` §17 + `templates/paper_completion_checklist.md` "Reviewer-Pause Cycle Precondition for Flagship-Paper-Trajectory Work" (added Patch 0539a, 22 May 2026):

- Phase 2 foundations work (Patches 0531–0537): seven sub-questions closed at sketch Layer 2.
- Reviewer-pause cycle (Patches 0538–0539): calibration response + status upgrade.
- Layer 3 promotion (Patches 0540–0552): substantive Layer 2 → Layer 3 promotion work + hardened-theorems trio production.
- Flagship paper assembly (Patches 0554–0570): paper skeleton → 10-Patch body assembly → bibliography → final polish → six-round reviewer cycle → v1.0 SHIP.

Future F-line flagship trajectories (F.2, F.3, …) inherit this pattern as the corpus-established F-line flagship trajectory methodology.

---

*This README is the entry point for the F.1 dynamical substrate law flagship paper folder at v1.0 SHIPPED state. Updated Session 143 Patch 0572h (24 May 2026) from the prior pre-v1.0 active-development state. Future paper-version increments (v1.1 minor revisions, v2.0 substantive extensions) trigger Status header revision + v-version content extensions. The v1.0 SHIP is the first F-line flagship v1.0 SHIP in CPP corpus history; future F-line flagship trajectories (F.2, F.3, …) inherit the methodology pattern documented in this folder's `documentation_suite/philosophy-dynamical-substrate-law.md` + `documentation_suite/changelog-dynamical-substrate-law.md` files.*
