# Capotauro v2.0 Outline

**Status**: outline v0.1, established Session 133 Patch 0442 at end of Reading C closure trajectory.
**Source paper**: `series_umbrella/series_substrate_chirality_arc/capotauro/capotauro.tex` v1.0 SHIPPED Session 122 Patch 0415 (46 pages).
**v2.0 target ship**: 7-13 sessions post-Session-133 (estimated 4-6 sessions rewrite + 3-5 sessions reviewer cycles + 0-2 sessions buffer for analytical complications during integration).

---

## 1. Headline claim

The Capotauro v1.0 paper closed sub-claim (c) of OPEN-SM-4 — derivation of the K3-doublet chirality matrix element magnitude $|M^{K3}| = \chi/6 = \phi^{-3}/6 \approx 0.0394$ at theorem level (THEO-CAP-1, Patch 0397), with primary empirical prediction $\Delta p_{LR} \approx 0.0394$ validated within 2% of observed $\sim 0.04$. v1.0's scope was a single-sector closure: the substrate primitive chirality magnitude on the K3-doublet mass-mixing sector.

The Reading C closure trajectory of Sessions 124-133 (Patches 0417-0441) extended this to a **three-way cross-sector unification at substrate level**: the same substrate parameter $\chi = \phi^{-3}$ feeds three structurally distinct sectors via three cage-shell averaging operations on the shared 12-vertex icosahedral cage at the host CP, yielding identical numerical magnitude $|M^{K3}| = |M^W| = |M^{qDP}| = \chi/6$ across:

- **Manifestation (i)** K3-doublet mass-mixing (THEO-CAP-1, sub-claim (c) closure)
- **Manifestation (ii)** W-bracelet electroweak V-A coupling (THEO-SD-CHIR-1, cross-sector unification with K3)
- **Manifestation (iii)** qDP/eDP electromagnetic handedness (THEO-SD-CHIR-2, three-way unification)

v2.0's headline: **substrate primitive chirality is a universal substrate-physics handle, feeding three observable sectors at identical numerical magnitude via the same cross-sector closure pattern (substrate-locality + cage-shell factor + pairing-convention).** The umbrella OPEN-SD-CHIR-PRIMITIVE registered Patch 0422 scopes the broader five-manifestation closure target; v2.0 delivers the three-manifestation triangle at theorem-registry rigor and identifies manifestations (iv)+(v) as future-window work.

## 2. What changes from v1.0 to v2.0

### 2.1 Substantively new content (must be added to v2.0)

1. **§2 reframe** from $H_4 \to I_4$ algebraic reduction to $H_4 \to H_3 = I_h$ vertex-aligned reduction per Q1' resolution (Patch 0419, Finding C-W37). The v1.0 §2 reduction was the chirality-only Operation A; vertex-aligned Reading C is the strictly stronger Operation B containing additional structural information that the v1.0 framing didn't expose. Operation B implies Operation A but resolves Q1' (vertex vs face vs edge vs cell alignment) and pins down the K3-doublet stabilizer location within the substrate residual symmetry. Two new foundational inputs registered: **FI-C-RC-1** (primitive 4D direction $\hat{n}$ as substrate's chirality-breaking primitive) and **FI-C-RC-2** (vertex-aligned reading $\hat{n} = v_{\text{host}}$ per Q1' resolution by three converging arguments).

2. **NEW substrate-locality theorem** (Finding C-W39, Patch 0424): under vertex-aligned Reading C with $\hat{n} = v_{\text{host}}$, the first-shell icosahedron at $v_{\text{host}}$ is preserved as $I_h$-symmetric at first order in $\epsilon$ with only isotropic radial scaling. All first-shell-to-first-shell 600-cell edges are tangent to $\hat{n}$ in 4D ($\hat{e}_{ab} \cdot \hat{n} = 0$ identically, numerically verified at machine precision). Substrate chirality magnitude identified directly as $\chi \equiv \epsilon$ at substrate level (supersedes Finding C-W38 from Patch 0423 which was 3D-framed in error).

3. **NEW Substrate-Locality Unification theorem** (Finding C-W40, Patch 0425): the local-$I_h$-preservation theorem applies uniformly to any first-shell-vertex substrate object; both K3-base and W-bracelet inherit substrate chirality from the same identification via cage-shell averaging on respective $D_6$ sub-stabilizers of the same $H_3 = I_h$ residual symmetry.

4. **NEW cage-shell factor identity** (Finding C-W41 with §17.10 refinement, Patches 0427+0429): Schur-orthogonality cage-shell averaging on the icosahedral cage shared between K3 and W gives $|M_\perp^W| = d_E/V_{\text{cage}} = 2/12 = 1/6$ identical to the K3-doublet's cage-shell factor.

5. **NEW pairing-convention identification** (Finding C-W43, Patch 0429): the W-bracelet's $\mathbb{Z}_2$ generator $\zeta^W$ identified as the icosahedral-center inversion in 4D ambient; matter-doublet basis $\Psi_-^{W,(1)} \in E_2(D_6)$ and $\Psi_-^{W,(2)} \in E_1(D_6)$ spans 2D subspace of $E_2 \oplus E_1$; composite matrix element $|M^W| = \chi/6$ at full Layer 3 rigor.

6. **NEW THEO-SD-CHIR-1** (Patch 0434): Cross-Sector Substrate Chirality Unification Theorem registering the K3-doublet ↔ W-bracelet pair closure at theorem-registry rigor.

7. **NEW qDP/eDP cross-sector extension** (Findings C-W44+C-W45+C-W46, Patches 0437-0439): substrate-locality applied to SM-2 qDP/eDP sector per §5+§6+Glossary Linear-vs-Orbital ZBW characterization; antipodal-pair $D_{5d}$ refinement; $\zeta^{qDP}$ identified as combined $CP$ operation (host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip); composite matrix element $|M^{qDP}| = \chi/6$ at full Layer 3.

8. **NEW THEO-SD-CHIR-2** (Patch 0440): qDP/eDP Sector Substrate Chirality Closure Theorem registering manifestation (iii) closure with three-way cross-sector unification achieved.

9. **NEW Q7 scoping section** (Patch 0441): sub-questions Q7.1-Q7.4 for future-window cosmological-nucleation work.

### 2.2 What's preserved from v1.0 unchanged

- §0 abstract (rewritten but core THEO-CAP-1 statement preserved)
- §1 introduction (rewritten but K3-doublet $\Delta p_{LR}$ headline preserved as one of three sector predictions)
- §3-§10 THEO-CAP-1 derivation chain (eight-step proof, end-to-end numerical verification, FI-C-1 through FI-C-10, 4 CPP axioms A1+A3+A4+A7) — preserved largely unchanged; cross-references updated to integrate with new cross-sector content
- v1.0 figures, tables, bibliography entries (preserved; new figures and tables added for cross-sector content)
- THEO-CAP-1 theorem statement (preserved at exact wording; framed as one of three sector closures within OPEN-SD-CHIR-PRIMITIVE umbrella)

### 2.3 What's deferred from v2.0 to later versions / dedicated papers

- **Q7 substantive work** (sub-questions Q7.1-Q7.4 cosmological-nucleation derivation): deferred to dedicated future-window sessions; not in v2.0 scope. v2.0 includes Q7 scoping section identifying sub-questions but no substantive closure work.
- **Manifestations (iv) thermodynamic causal arrow and (v) cosmological-vacuum asymmetry**: deferred to future-window work, possibly under dedicated SF-line cosmological-asymmetry paper rather than Capotauro v3.0+.
- **Q1'+Q1'.A Layer 2 → Layer 3 promotion** (dynamical/causal/energetic derivation of vertex-alignment from CPP primitives): deferred; remains at Layer 2 via three converging arguments. v2.0 acknowledges this as open and identifies it as scope-deferred.
- **Layer 4 EFT continuum-limit calculations** for the three sectors' observable predictions (SF-2 V-A coupling 75% → 100% massless-limit, SM-2 chiral-polarity-bias EFT, K3-doublet $\Delta p_{LR}$ kinematic projection): deferred to dedicated sector-specific papers. v2.0 provides the substrate-physics handles at Layer 3; Layer 4 closures are SF-2 / SM-2 / SF-4 territory.

## 3. Section-by-section structure (v2.0 target)

Estimated page count: 60-75 pages (v1.0 was 46 pages; +14-29 pages for cross-sector content + Q7 scoping section).

### §0 Abstract (rewritten)

Three-way cross-sector unification headline replacing v1.0's K3-doublet-only headline. Primary empirical prediction $\Delta p_{LR} \approx 0.0394$ preserved; cross-sector predictions for W-bracelet V-A coupling (substrate handle $\chi/6$ feeding SF-2 Layer 4 EFT) and qDP/eDP chiral-polarity-bias (substrate handle $\chi/6$ feeding SM-2 §10 mechanism) registered as new content. Conditional theorem closure on FI-C-1 through FI-C-10 + FI-C-RC-1 + FI-C-RC-2 + SM-2 §5+§6+Glossary substrate characterization + 4 CPP axioms (A1, A2, A4, A7; A1+A7 most load-bearing per Picture B substrate-orientation-field framework).

### §1 Introduction (rewritten)

Programme positioning: Capotauro v2.0 as second-paper-version of the first programme-level theorem-registry registration ahead of dedicated flagship paper publication (Patch 0397 THEO-CAP-1 pattern). Reading C closure trajectory historical narrative (Sessions 124-133, Patches 0417-0441, 17 patches across 10 sessions, two theorem-registry-level cross-sector theorems). Position within OPEN-SD-CHIR-PRIMITIVE umbrella (registered Patch 0422; five-manifestation scope; three-manifestation triangle closure achieved at v2.0).

### §2 Substrate Primitive Chirality (REFRAMED)

**v1.0 →** $H_4 \to I_4$ algebraic chirality-only reduction (Operation A). **v2.0 →** $H_4 \to H_3 = I_h$ vertex-aligned reduction (Operation B) per Q1' resolution (Patch 0419, Finding C-W37). FI-C-RC-1 (primitive 4D direction $\hat{n}$) and FI-C-RC-2 (vertex-aligned $\hat{n} = v_{\text{host}}$) registered as additional foundational inputs. Three converging arguments for vertex-alignment: paper-internal hosting language (§10 K3-doublet host vertex), cross-sector unification with SF-2 W-bracelet (Finding C-W36 W-bracelet centroid coincidence with 600-cell vertex directions), SM-1 first-shell icosahedron preserved as substrate local structure. Operation B implies Operation A; the v1.0 §2 framing is preserved as the chirality-only coarsening of v2.0's full structural reduction.

### §3 Substrate-Locality Theorem (NEW)

Finding C-W39 (Patch 0424): local-$I_h$-preservation at $v_{\text{host}}$. Numerical verification at machine precision: all 30 first-shell-to-first-shell 600-cell edges have $|\hat{e} \cdot \hat{n}| < 10^{-9}$; all 12 host-to-first-shell edges have $\hat{e} \cdot \hat{n} = -1/(2\phi)$ uniformly. Substrate chirality magnitude identified directly: $\chi \equiv \epsilon$ at substrate level (no $f_{\text{geom}}$, no $f_{\text{irrep}}$ factor; supersedes Finding C-W38 from Patch 0423 §12 which was 3D-framed in error). The §13 §12 correction narrative is preserved as substantive scientific correction per `founders_voice/004` discipline.

### §4 K3-Doublet Sector: Composite Capotauro Wigner-Eckart Theorem (preserved from v1.0)

v1.0 §3-§10 content largely preserved: eight-step proof of THEO-CAP-1; chirality-eigenvalue matching factor $\chi$ from cross-product structure of unique $A_2$ generator (paper §7.4 Lemma spectral_S + §7.5); cage-shell averaging factor $1/6$ from $d_E/V_{\text{cage}} = 2/12$ (paper §10 Schur orthogonality); composite matrix element $|M^{K3}| = \chi/6 \approx 0.0394$; primary empirical prediction $\Delta p_{LR} = \chi/6$ validated within 2%. Cross-references updated: §4 now framed as **one sector of three** under OPEN-SD-CHIR-PRIMITIVE umbrella; FI-C-9 retained as v1.0 foundational input now sourced from §2's primitive $\hat{n}$ identification.

### §5 W-Bracelet Sector: Cross-Sector Unification with K3-Doublet (NEW)

THEO-SD-CHIR-1 (Patch 0434) integrated. Four-step proof chain:
- (i) Substrate-Locality Unification (Finding C-W40, sketch §14): K3-base and W-bracelet both inherit chirality from same identification via cage-shell averaging on respective $D_6$ sub-stabilizers of same $H_3 = I_h$
- (ii) Cage-shell factor identity (Finding C-W41 + §17.10 refinement, sketch §15): $|M_\perp^W| = 2/12 = 1/6$ identical to K3
- (iii) Pairing-convention identification (Finding C-W43, sketch §17): $\zeta^W$ = icosahedral-center inversion in 4D ambient; matter-doublet $\Psi_-^{W,(1,2)}$ spans 2D subspace of $E_2 \oplus E_1$ in $D_6$; chirality operator $B_2(D_6) = A_2(S_3) \otimes \sigma(\mathbb{Z}_2)$
- (iv) Composite $|M^W| = \chi/6$ at full Layer 3 via Wigner-Eckart factorization analog of K3 §5.3-§5.4

Cross-sector unification corollary: $|M^W| = |M^{K3}|$ at theorem-registry rigor. SF-2 V-A coupling Layer 4 closure (continuum-EFT Yang-Mills derivation of 75% finite-mass to 100% massless-limit) registered as deferred Layer-4 work; substrate-level $\chi/6$ from this section provides the substrate-physics handle.

### §6 qDP/eDP Sector: Three-Way Cross-Sector Unification (NEW)

THEO-SD-CHIR-2 (Patch 0440) integrated. Per SM-2 v1.0 §5+§6+Glossary: qDP/eDP distinction is ZBW-configuration-type (orbital $d=0$ chirality-neutral reference vs Linear $d=1$ chirality-coupled), NOT particle-type distinction. Four-step proof chain:
- (i) Substrate-Locality Unification applied to qDP/eDP sector (Finding C-W44, sketch §18): Linear ZBW = 1-vertex subset with $C_{5v}$ stabilizer; Orbital ZBW = trivial subset with $I_h$ stabilizer
- (ii) Cage-shell factor Layer 2 conservative with Q6-PAIRING registered (Finding C-W45, sketch §19): $A_u(I_h) \downarrow A_2(C_{5v})$; matrix element vanishes under naive 1-vertex framing; antipodal-pair refinement to $D_{5d}$ required
- (iii) Q6-PAIRING resolved via combined $CP$-inversion (Finding C-W46, sketch §20): $\zeta^{qDP}$ = host-CP-centered spatial inversion + $\hat{n}$-flip + qCP-sign flip; matter-doublet basis spans 2D subspace of $A_{1g} \oplus A_{2u}$ in $D_{5d}$; chirality operator $A_{2u}(D_{5d})$
- (iv) Composite $|M^{qDP}| = \chi/6$ at full Layer 3 via Wigner-Eckart factorization

Three-way unification corollary: $|M^{qDP}| = |M^W| = |M^{K3}| = \chi/6$. Manifestation-comparison table (§20.11). SM-2 §10 chiral-polarity-bias mechanism feeds from substrate-level $\chi/6$; Layer 4 SM-2 EFT closure of the substrate-handle-to-Linear-ZBW-stabilization-energy bridge registered as deferred work.

### §7 Empirical Predictions and Cross-Sector Implications (rewritten)

Master predictions table: $\Delta p_{LR} = \chi/6 \approx 0.0394$ (K3-doublet, validated within 2% per PRED-O-25); substrate-handle to SF-2 V-A coupling at $\chi/6$ (substrate-physics handle for Layer 4 EFT); substrate-handle to SM-2 chiral-polarity-bias at $\chi/6$ (substrate-physics handle for Layer 4 EFT). Three-way magnitude-level unification claim: all three sectors at identical $\chi/6$ at substrate level despite distinct sector-specific stabilizers and $\zeta$ generators. Umbrella closure prediction: manifestations (iv)+(v) expected at $\chi/6$ at substrate level (future-window work).

### §8 Falsifiers (extended)

v1.0 falsifier preserved: $\Delta p_{LR} \neq \chi/6 \approx 0.0394$ observed beyond 2% would falsify THEO-CAP-1. NEW falsifiers from cross-sector unification:
- $|M^W|$ observed at substrate-physics scale substantially different from $\chi/6$ would falsify THEO-SD-CHIR-1
- $|M^{qDP}|$ observed at substrate-physics scale substantially different from $\chi/6$ would falsify THEO-SD-CHIR-2
- Three-way magnitude-level unification violation across any pair of (i)+(ii)+(iii) falsifies the umbrella's unification-at-magnitude-level claim
- Capotauro nucleation event absent or operating at different cosmological epoch than Q7 framings (a)+(b)+(c) (Q7.4 anticipated falsifiers; framed as future-window work; included in v2.0 scoping)

### §9 Q7 Cosmological-Nucleation Scoping (NEW)

Sub-questions Q7.1-Q7.4 per Patch 0441 §21 decomposition. Three candidate framings per sub-question registered as future-window work. Three immediate analytical handles available from Q1-Q6 closure: cross-sector unification at magnitude level (§20.14), three-step closure pattern as template for manifestations (iv)+(v), THEO-CAP-1's $\phi^{-3}$-scale primitive direction as substrate-physics anchor. Scope-deferral framing: v2.0 includes scoping not substantive closure; Q7 work is dedicated future-window territory.

### §10 Discussion (rewritten)

Programme-level pattern observations:
- v2.0 as first multi-manifestation cross-sector unification flagship paper in CPP corpus
- Three-step closure pattern (substrate-locality + cage-shell factor + pairing-convention) demonstrated as structurally complete across three manifestations with distinct sector-specific content but identical numerical magnitude
- Unification-at-magnitude-level claim as stronger than unification-at-mechanism-level claim
- Reading C closure trajectory methodological observations: §15.12 cross-sector extension surfaces ambiguities; §16.12 register-then-resolve discipline; §17.13 cross-sector unification pattern; §19.11 matter-doublet pairing convention universality; §20.14 three-way magnitude-level unification
- Future-window targets: Q7 substantive work, manifestations (iv)+(v) closures, Capotauro v3.0+ or dedicated cosmological-asymmetry flagship paper
- Cross-sector closure precedent (SF-4 v4.0 OPEN-FP-SF-4-2 + SM-5 op:nu_id was first cross-sector closure in CPP at SF-line; Capotauro v2.0 is first three-way cross-sector unification at SD-line)

### §11 Bibliography (extended)

v1.0 bibliography preserved. NEW entries for:
- Q5/Q6 sketch sections (sketch §13-§21)
- THEO-SD-CHIR-1 and THEO-SD-CHIR-2 (with theorem-registry pointer)
- SM-2 v1.0 §5+§6+Glossary cross-reference for Linear-vs-Orbital ZBW
- Reading C foundational input papers (Patch 0419 Finding C-W37 vertex-alignment, Patch 0424 §13 local-$I_h$-preservation)

## 4. Drafting plan and timeline

### 4.1 v0.1 → v1.0 SHIP estimated 7-13 sessions

Following SS-9 / SF-4 / Capotauro v1.0 patterns:
- **Sessions 1-2** (post-handover): v2.0 outline lock + §2 reframe drafting + cross-references inventory between existing v1.0 sections and new cross-sector sections
- **Sessions 3-4**: v0.2 draft with new §3 (Substrate-Locality Theorem), §5 (W-Bracelet), §6 (qDP/eDP) sections drafted at full paper-quality from sketch §13-§20 content
- **Sessions 5-6**: v0.3 draft with §7 (Predictions), §8 (Falsifiers), §9 (Q7 Scoping), §10 (Discussion) sections completed + bibliography extension
- **Session 7**: v0.4 → v0.5 integration polish + first PDF compile + cross-reference verification
- **Sessions 8-12**: AI review passes (3-5 passes expected per Capotauro v1.0 pattern) + integration of feedback
- **Session 13**: v1.0 SHIP with final integration + theorem-registry update + paper_catalog update + master_glossary update + four-tier documentation suite

### 4.2 Scope discipline (must maintain across drafting)

- **NO** substantive Q7.x work in v2.0 (scoping section only)
- **NO** manifestations (iv) thermodynamic causal arrow or (v) cosmological-vacuum asymmetry substantive work (deferred)
- **NO** Layer 4 EFT continuum-limit calculations (deferred to sector-specific papers)
- **NO** Q1'+Q1'.A Layer 3 promotion attempts (remains at Layer 2 with three converging arguments)
- **YES** preserve v1.0 §3-§10 derivation chain with minimal modification (cross-reference updates only)
- **YES** integrate sketch §13-§21 content at full paper-quality
- **YES** maintain conditional theorem closure framing inheriting from THEO-CAP-1 / THEO-SD-CHIR-1 / THEO-SD-CHIR-2 precedent
- **YES** maintain symmetric-honesty discipline per `founders_voice/004` throughout
- **YES** preserve all v1.0 foundational input enumerations (FI-C-1 through FI-C-10) and extend with FI-C-RC-1, FI-C-RC-2

### 4.3 Reviewer-concern anticipations

1. **"Why three sectors at identical magnitude?"** — addressed in §10 Discussion (cross-sector unification at magnitude level is structural consequence of shared 12-vertex icosahedral cage with shared effective matter-doublet dimension 2; distinct sector-specific content lives in $\zeta$ generators not in numerical magnitude)
2. **"Why combined CP for qDP and pure geometric inversion for K3/W?"** — addressed in §6.3 (Capotauro mechanism's three-way coupling between vertex direction × $\hat{n}$ × qCP-sign; spatial inversion alone preserves qCP-sign as parity-EVEN intrinsic property)
3. **"What about manifestations (iv)+(v)?"** — addressed in §10 (registered as future-window work; three-step closure pattern templates them with sector-specific $\zeta$ generators containing time-direction or cosmological-asymmetry content)
4. **"Why is FI-C-9 still a foundational input post-v2.0?"** — addressed in §2 (vertex-aligned Reading C identifies $\hat{n}$ alignment but $|\chi| = \phi^{-3}$ magnitude remains structural-argument-level via perturbative-distance-ratio constraint; full first-principles derivation of magnitude from CPP primitives remains future-window work)
5. **"How does v2.0 relate to OPEN-SM-4?"** — addressed in §10 (sub-claim (c) closure preserved at v1.0; v2.0 extends to cross-sector unification under umbrella registered Patch 0422; sub-claims (a) and (b) covered by Q7 scoping and Reading C closure trajectory respectively)

### 4.4 What v2.0 establishes vs does not establish

**Establishes**:
- Three-way cross-sector unification at substrate level across manifestations (i)+(ii)+(iii) at theorem-registry rigor
- Identical numerical magnitude $\chi/6 \approx 0.0394$ across three sectors via shared icosahedral cage + shared effective matter-doublet dimension
- Substrate primitive direction $\hat{n}$ as vertex-aligned reading at Layer 2 with three converging arguments
- Q7 cosmological-nucleation sub-questions decomposition framework

**Does not establish**:
- Sub-claim (a) Capotauro nucleation event substantive closure (Q7 scoping only)
- Manifestations (iv) thermodynamic causal arrow + (v) cosmological-vacuum asymmetry closures (future-window)
- Layer 4 EFT continuum-limit calculations for any of the three sectors' observable predictions
- First-principles derivation of $|\chi| = \phi^{-3}$ magnitude from CPP primitives (FI-C-9 retained as foundational input)
- Sub-claim (b) substrate chirality mechanism candidate derivation closure (Reading C closure trajectory addressed this via cross-sector unification framework; full first-principles closure of $\hat{n}$ alignment derivation Q1'+Q1'.A remains at Layer 2)

## 5. Trigger conditions and decision points

v2.0 v0.1 drafting begins after:
- (A) Session 133 close handover landed (Patch 0442+ session-close work)
- (B) v2.0 scope locked at this outline level (this patch)
- (C) Future-window context loaded with: this outline + sketch §13-§21 + theorem-registry THEO-SD-CHIR-1 + THEO-SD-CHIR-2 + v1.0 .tex source + Reading C closure trajectory Last-updated header history

v2.0 v1.0 SHIP requires:
- All four-condition tests ✓ per Patch 0397 / THEO-CAP-1 / THEO-SD-CHIR-1 / THEO-SD-CHIR-2 precedent
- 3-5 AI review passes converging on v1.0-ready verdict
- Cross-references resolve cleanly between v1.0-preserved §4 K3-doublet content and new §5+§6 cross-sector content
- Programme-level registers (theorem-registry, research_frontier, paper_catalog, master_glossary) updated at SHIP

v2.0 trigger to begin v0.1 drafting: after handover landing (Patch 0442 estimated 1 session) and at Thomas's discretion for new-context-window pickup.

---

**End of v2.0 outline.** Total outline length: ~250 lines. Section structure locked; section-by-section content notes locked; drafting timeline estimated 7-13 sessions; scope discipline registered. v0.1 drafting begins at future-window context with this outline as scoping anchor.
