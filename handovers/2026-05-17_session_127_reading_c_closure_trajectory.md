# Reading C closure-trajectory handover: Sessions 124-126 consolidation

**Doc purpose:** Bootup-ready handover consolidating the Reading C three-patch arc on OPEN-FI-C-9-FP-MECHANISM (Capotauro sub-claim (b) substrate chirality mechanism candidate derivation). Sessions 124-126 (Patches 0417-0419) advanced Reading C from "Tier-4 Layer 1/Layer 2 working sketch" to "Q1+Q2 closed at Layer 3 + Q1'+Q1'.A resolved at Layer 2 toward vertex-aligned Reading C." This document captures the current state, key findings, methodological observations, and forward queue for future-context-window pickup.

**Created:** 17 May 2026 (Session 127 Patch 0421)
**Authors:** Thomas Lee Abshier ND + Claude Opus
**Repository:** Hyperphysics-Institute/CPP
**Parent open problem:** OPEN-FI-C-9-FP-MECHANISM (sub-claim (b) of OPEN-SM-4)
**Parent paper:** Capotauro v1.0 SHIPPED Session 122 Patch 0415
**Working sketch:** `flagship_papers/capotauro/sketches/Capotauro_chiral_mechanism_candidate.md` (665 lines after Patch 0419)
**Verification script:** `flagship_papers/capotauro/code/q1prime_w_bracelet_geometry.py` (~340 lines, runs <30 seconds with all checks passing)

---

## 1. Current state at handover (post-Patch 0419)

### 1.1 Closure-trajectory status

| Q | Description | Status | Layer | Patch | Finding |
|---|---|---|---|---|---|
| Q1 | $\Hfour$-stabilizer structure of $\hat{n}$ | **CLOSED** | 3 | 0417 | (refutation + correction) |
| Q2 | Consistency with paper's $\Dsix$ machinery | **CLOSED** | 3 | 0417 | (group theory) |
| Q1' | Vertex-aligned vs face-aligned $\hat{n}$ | **RESOLVED** toward vertex-aligned | 2 | 0419 | C-W37 |
| Q1'.A | K3-base geometric realization | **RESOLVED** | 2 | 0419 | (paper §10 reading) |
| Q3 | Precise $\epsilon$-$\chi$ relationship | open | sketch | — | — |
| Q4 | Higher-order $\epsilon$-expansion → fractional retention | open | sketch | — | — |
| Q5 | Cross-sector consistency with SF-2 W bracelet | partial progress | sketch-ish | 0418-0419 | C-W36 |
| Q6 | Cross-sector consistency with SM-2 qDP/eDP | open | sketch | — | — |
| Q7 | Cosmological-timing interaction with sub-claim (a) | open | sketch | — | — |

### 1.2 Findings registered across the arc

- **Finding C-W35** (Patch 0417): face-aligned $\hat{n}$ produces substrate residual symmetry equal to K3-doublet stabilizer $\Dsix$ exactly. Originally registered as the leading argument for face-aligned Q1' resolution; reframed at Patch 0419 as a preserved SUB-result within vertex-aligned (the K3-doublet's location-specific $\Dsix$ is one of 10 $D_{3d}$ subgroups of substrate $H_3$).

- **Finding C-W36** (Patch 0418): the 1200 W bracelet centroid directions on $S^3$ coincide exactly with the 120 vertex directions of the 600-cell (10 bracelets per vertex direction; each bracelet is a Petrie hexagon of the SM-1 first-shell icosahedron around the central vertex). The W bracelet orbit and the face orbit are different $\Hfour$-orbits on $S^3$ with disjoint direction sets.

- **Finding C-W37** (Patch 0419): Q1' resolves toward vertex-aligned Reading C at Layer 2. The substrate primitive direction $\hat{n}$ aligns with a 600-cell vertex direction (the host vertex of the icosahedral cage hosting the K3-doublet per Capotauro paper §10). Substrate residual symmetry $H_3 = I_h$. The K3 base is geometrically realized as a triangular face of the host's first-shell icosahedron, at cosine $\sqrt{3}/2 \approx 0.866$ off-axis from $\hat{n}$. K3-doublet $\Dsix$ stabilizer is one of 10 $D_{3d}$ sub-stabilizers of $H_3$. W bracelets (per Finding C-W36) sit on-axis at radius $\phi/2$.

### 1.3 Trajectory estimate

Reading C Layer 3 closure of full chirality magnitude derivation:

- Pre-arc estimate (Patch 0414): 10-20 sessions
- Post-Patch 0417 (Q1+Q2 closed): 8-18 sessions
- Post-Patch 0418 (Q1' partial progress): 8-18 sessions (unchanged)
- **Post-Patch 0419 (Q1'+Q1'.A resolved): 7-17 sessions**

Three sessions consumed across the arc (one per patch).

---

## 2. Detailed recap of the three-patch arc

### 2.1 Patch 0417 — Q1+Q2 closure at Layer 3 (Session 124)

**Setup.** Reading C's §2.2 made a specific Claim: the $\Hfour$-stabilizer of $\hat{n}$ is isomorphic to $\Ifour = H_4^+$ (the rotational subgroup of $\Hfour$, order 7,200). This was registered Session 122 Patch 0415 with a falsifier: "$\hat{n}$ stabilizer in $\Hfour$ NOT isomorphic to $\Ifour$" would falsify Reading C at sketch level.

**Q1 result.** The Claim is **refuted at theorem level** by elementary orbit-stabilizer counting on $\Hfour$. The actual orbit-stabilizer pairs of $\Hfour$ acting on $\mathbb{R}^4$ are:

| Orbit on $\mathbb{R}^4$ | Orbit size | Stabilizer of representative | Order |
|---|---|---|---|
| 120 600-cell vertices | 120 | $H_3 \cong I_h$ | 120 |
| 720 edge centers | 720 | $D_5 \times \mathbb{Z}_2$ | 20 |
| 1200 face centers | 1200 | $\mathbb{Z}_2 \times S_3 \cong D_6$ | 12 |
| 600 cell centers | 600 | $S_4$ | 24 |
| Generic point | 14,400 | trivial | 1 |

No orbit has stabilizer of order 7,200. The §2.2 Claim is mathematically incorrect.

**Q2 result.** The Capotauro paper's downstream machinery operates via Wigner-Eckart on $\Dsix$ (the K3-doublet stabilizer). For the paper's derivation to be preserved under Reading C, the substrate's residual symmetry must contain $\Dsix$. Checking each candidate:

- Vertex-aligned ($H_3$): contains $\Dsix$ via $D_{3d}$ embedding at any 3-fold axis of the icosahedron. ✓
- Face-aligned ($\Dsix$): identical to $\Dsix$. ✓
- Edge-aligned ($D_5 \times \mathbb{Z}_2$): does NOT contain $\Dsix$ (order 20 with no order-12 subgroup of the right structure). ✗
- Cell-aligned ($S_4$): does NOT contain $\Dsix$ (Sylow-3 analysis rules out $D_6$). ✗

Only vertex-aligned and face-aligned cases are consistent with the paper.

**Methodological observation registered.** A falsifier hitting a specific instance of a framework does not by itself kill the framework if a rigorous correction is simultaneously available. The §2.2 Claim was refuted but Reading C survived because the corrected stabilizer ($H_3$ or $\Dsix$) is consistent with the paper's $\Dsix$-based machinery. This is the "refutation that doesn't kill the framework" pattern.

**New sub-question Q1' registered**: vertex-aligned vs face-aligned. Finding C-W35 registered as leading argument for face-aligned (substrate residual = K3-doublet stabilizer exactly).

**Forward queue at end of patch**: Q1' resolution at next substrate-physics session; trajectory estimate 8-18 sessions.

### 2.2 Patch 0418 — Q1' partial progress via cross-sector W bracelet (Session 125)

**Setup.** §9.6 forward queue from Patch 0417 flagged the cross-sector check with SF-2's W bracelet $\Dsix$ stabilizer as a candidate Q1' tie-breaker. Working hypothesis: maybe the W bracelet 1200-orbit and the face 1200-orbit are the same $\Hfour$-orbit on $S^3$, in which case vertex/face would unify into a single primitive-direction substrate.

**Setup correction.** Direct reading of SF-2 v1.0 §sec:Wbracelet_thm shows the W bracelet is *not* a unit-vector orbit. It's an orbit of induced hexagonal 6-cycles in the 600-cell vertex graph. Each bracelet is 6 vertices forming a regular hexagon with all 6 vertices at radius $r_\mathcal{B} = 0.58779$ from a common centroid, and the centroid at $\|\bar{v}\| = \phi/2 \approx 0.809$ from origin.

The casual orbit-cardinality matching heuristic doesn't apply directly; geometric analysis required.

**Computational verification.** Built standalone Python script (~290 lines, NumPy-only) at `flagship_papers/capotauro/code/q1prime_w_bracelet_geometry.py`. The script:

1. Generates 120 vertices of 600-cell from icosian / Hurwitz-quaternion coordinates.
2. Identifies 720 edges at distance $1/\phi$.
3. Verifies vertex degree 12 (matches z=12 icosahedral first-shell coordination).
4. Enumerates 1200 triangular faces (3-cliques in edge graph).
5. Enumerates 4800 induced 6-cycles via depth-5 DFS with chord-exclusion.
6. Classifies cycles by $\Hfour$-invariant signature (sorted multiset of 15 pairwise squared distances): 3600 in orbit A, 1200 in orbit B (W bracelet). Matches SF-2 Theorem 4.2 exactly.
7. Verifies orbit-B centroid radius is exactly $\phi/2$.
8. Compares bracelet centroid directions vs face centroid directions on $S^3$.

**Finding C-W36 result.** The 1200 W bracelet centroid directions on $S^3$ reduce to exactly **120 distinct unit vectors**, which are precisely the **120 vertex directions of the 600-cell** (verified set-equality). Each vertex direction hosts exactly **10 bracelets** ($10 \times 120 = 1200$). For each bracelet at vertex direction $v_i$, the 6 hexagonal-cycle vertices are all edge-neighbors of $v_i$ — i.e., they lie in the icosahedral first shell. Structural identification: **each bracelet is a Petrie hexagon of the SM-1 first-shell icosahedron** around its central vertex (regular icosahedron admits 10 inscribed regular hexagons; lifted into 4D at radius $\phi/2$ along each vertex direction).

The W bracelet orbit and the face orbit are **different orbits on $S^3$** with disjoint direction sets. Closest face-direction cosine to any bracelet centroid direction is $\sqrt{(1+\phi)/3} \approx 0.934$ — the vertex-to-containing-face-centroid cosine identity (when the host vertex is itself one of the face's 3 vertices).

**Implication for Q1' (the structural trade-off).** Under either Reading C alternative, *exactly one* of the two substrate objects (W bracelet vs K3-doublet) is on-axis with $\hat{n}$, and the other is off-axis at cosine $\sqrt{(1+\phi)/3}$:

- **Vertex-aligned** ($\hat{n}$ = 600-cell vertex direction): 10 W bracelets on-axis at radius $\phi/2$; K3-doublet (face-centered) off-axis.
- **Face-aligned** ($\hat{n}$ = 600-cell face direction): K3-doublet on-axis; W bracelet off-axis.

The two readings split the cross-sector substrate objects rather than uniting them. Q1' acquires complementary structural-coincidence arguments on both sides (C-W35 vs C-W36) and remains contested at this patch.

**Methodological observation.** Cross-sector unification is not always convergent. The casual heuristic "both substrate objects with $\Dsix$ stabilizers at 1200-orbits should unify under one Reading C alternative" is refuted by direct computation. Cross-sector arguments can expose substrate-location dichotomies that subdivide foundational alternatives rather than reducing them.

**Q1'.A registered**: K3-base geometric realization (face direction or first-shell 3-fold triangle?).

**Forward queue at end of patch**: Q1'.A resolution at next session; trajectory unchanged at 8-18 sessions.

### 2.3 Patch 0419 — Q1'+Q1'.A resolved at Layer 2 toward vertex-aligned (Session 126)

**Setup.** Q1'.A is the deciding sub-question between vertex-aligned and face-aligned. Working hypothesis: re-read the Capotauro paper §6.1 (sec:k3_base) and §10 for any internal commitment about the K3 base's geometric placement.

**Paper-internal commitment found at §10 line 541**:

> *"The structural identity $V_\text{cage} = |\Dsix| = 12$ has physical content: the icosahedral cage hosting the K3-doublet has exactly the order of the K3-doublet's stabilizer group. This is a consequence of the substrate's geometric structure --- the 600-cell's icosahedral first shell hosts the same $\Sthree \times \mathbb{Z}_2$ that stabilizes the K3 base extended over the cage."*

The phrase "icosahedral cage hosting the K3-doublet" carries an internal commitment to a unique host vertex (the central 600-cell vertex around which the V=12 icosahedral first shell forms). The K3 base is "extended over the cage" as 3 of the 12 first-shell vertices forming a triangular face of the icosahedron.

**Computational verification (script extension).** Three additional Q1'.A checks added to the verification script (~50 lines):

1. **First-shell triangles are 600-cell faces.** All 20 triangular faces of any host vertex's first-shell icosahedron are 600-cell faces (verified across all 120 host vertices, total 2400 (host, face) pairs).
2. **Each 600-cell face has exactly 2 host vertices.** Common-neighbor distribution Counter({2: 1200}) — degenerate at multiplicity 2. Hosts are outside the face (no self-loops). Face-host bipartite graph has degree 20 on hosts and degree 2 on faces, accounting for $120 \times 20 = 2400 = 1200 \times 2$.
3. **K3-face cosine identity.** The K3 face centroid lies at cosine $\sqrt{3}/2 \approx 0.866$ ($30°$) from the host vertex direction. Closed-form: $v_0 \cdot \hat{c} = (3\phi/2)/\sqrt{3+3\phi} = \sqrt{3\phi^2/(4(1+\phi))} = \sqrt{3/4} = \sqrt{3}/2$ using $\phi^2 = \phi + 1$.

**Finding C-W37 registered.** Q1' resolves toward vertex-aligned Reading C at Layer 2 via three converging arguments:

1. **Paper-internal hosting argument**: paper §10 requires unique host vertex; vertex-aligned provides this while face-aligned has 2-host ambiguity ($\hat{n}$ alone does not distinguish the 2 hosts).
2. **Cross-sector unification with SF-2 W bracelet (Finding C-W36)**: vertex-aligned puts 10 W bracelets on-axis with $\hat{n}$ at radius $\phi/2$ as Petrie-polygon subgroups of substrate $H_3 = I_h$.
3. **SM-1 first-shell icosahedron preserved**: vertex-aligned retains the standard CPP first-shell icosahedral geometry as substrate's local structure.

**Reconciliation with Finding C-W35**: face-aligned algebraic-substrate-equality preserved as a SUB-result within vertex-aligned. The K3-doublet's location-specific $\Dsix$ stabilizer is one of 10 $D_{3d}$ subgroups of substrate $H_3$, corresponding to the K3 face's 3-fold axis. The Capotauro paper's Wigner-Eckart machinery on $\Dsix$ in §6-§10 operates at this sub-stabilizer level correctly; no modification to v1.0 paper downstream derivation needed.

**Q1'.A resolved**: K3 base = triangular face of host vertex's first-shell icosahedron = 600-cell face.

**Methodological observation.** "Partial progress + paper re-examination" as efficient closure pattern. When cross-sector analysis produces complementary arguments on both sides, the next move is often to mine the existing flagship paper's framing for already-internal commitments that pin down the alternatives, before reaching for additional cross-sector or empirical input. The paper §10's "icosahedral cage hosting the K3-doublet" framing was the disambiguating constraint that resolved Q1' toward vertex-aligned at Layer 2.

**Forward queue at end of patch**: Q3 ($\epsilon$-$\chi$ relationship sharpening) at next substrate-physics session; trajectory revised to 7-17 sessions.

---

## 3. Methodological observations registered across the arc

Three patterns worth carrying forward to future closure-trajectory work:

### 3.1 Refutation that doesn't kill the framework (Patch 0417)

A falsifier hitting a specific instance of a framework does not by itself kill the framework if the correction landing the framework on solid ground is itself rigorously available. The §2.2 Claim ($\Ifour = H_4^+$ stabilizer isomorphism) was refuted at theorem level by elementary orbit-stabilizer counting, but Reading C survived because the corrected stabilizer identifications ($H_3$ for vertex-aligned, $\Dsix$ for face-aligned) are consistent with the paper's $\Dsix$-based machinery. The §9 closure exemplifies this pattern: falsification of a specific Claim + simultaneous rigorous identification of the correct alternative = framework refinement, not framework death.

### 3.2 Cross-sector unification is not always convergent (Patch 0418)

The casual heuristic "both substrate objects with $\Dsix$ stabilizers at 1200-orbits should unify under one Reading C alternative" was refuted by direct geometric computation. The W bracelet orbit and the face orbit are different $\Hfour$-orbits on $S^3$ with disjoint direction sets. Cross-sector arguments can expose substrate-location dichotomies that subdivide foundational alternatives rather than reducing them. The two Reading C alternatives split the cross-sector substrate objects (K3-doublet at face direction; W bracelet at vertex direction) rather than uniting them.

### 3.3 Partial progress + paper re-examination as efficient closure pattern (Patch 0419)

When cross-sector analysis produces complementary arguments on both sides (Findings C-W35 vs C-W36), the next move is often to mine the existing flagship paper's framing for already-internal commitments that pin down the alternatives, before reaching for additional cross-sector or empirical input. The paper §10's "icosahedral cage hosting the K3-doublet" phrase carries an internal commitment to a unique host vertex that disambiguates the Reading C alternatives. The paper's authors had already made commitments during paper drafting that constrain downstream closure trajectory work, even when those commitments were not explicitly framed as "Q1' resolutions at the time." Mine the existing paper for already-internal commitments before doing more cross-sector work.

---

## 4. Forward queue and next-session priority

### 4.1 Immediate next priority: Q3 (precise $\epsilon$-$\chi$ relationship sharpening)

**Statement.** Given the established Reading C structure under vertex-aligned $\hat{n}$, sharpen the perturbative-distance-ratio argument from sketch §2.3-§2.4 (and paper §2.3) to specify whether $\epsilon$ and $\chi$ are equal, related by a structural factor, or related by some other constraint.

**Current sketch position (§2.3-§2.4).** Each 600-cell edge $\vec{e}_{ij}$ acquires a chirality-correlated length perturbation $\|\vec{e}_{ij}\|_\text{actual} = \|\vec{e}_{ij}\|_\text{ideal} \cdot (1 + \epsilon \cdot (\hat{e}_{ij} \cdot \hat{n}))$ where $\epsilon$ is the perturbation magnitude. The perturbative-distance-ratio constraint forces $\epsilon \to 0$ at first viable scale; the $\phi^{-n}$ ladder is argued to land at $n=3$ as the first viable scale (smaller scales destroy the 600-cell's geometric structure at zeroth order).

**Question.** Does $\epsilon = \chi$ exactly (the perturbation magnitude equals the chirality magnitude)? Or is there a structural factor relating them — possibilities include $\epsilon = \chi/\sqrt{3}$ (mirroring the K3-amplitude factor $b = \chi/\sqrt{3}$ in the Capotauro paper), $\epsilon = \chi/6$ (mirroring the cage-shell averaging factor), or some other relationship from the geometry of the perturbation vs the chirality observable.

**Estimated 1-3 sessions** to closure. The natural candidates each carry their own derivation path; the resolution might come from:
- Direct identification (if $\epsilon$ is defined identically to $\chi$ in the substrate-physics framework)
- Structural factor derivation (if the perturbative-distance-ratio constraint relates $\epsilon$ to $\chi$ through icosahedral geometry)
- Sub-stabilizer averaging (if the K3-doublet's location-specific $\Dsix$ sub-stabilizer within $H_3$ introduces a factor of $1/\sqrt{3}$ or $1/6$ via Schur-orthogonality-on-sub-stabilizer)

### 4.2 Subsequent priorities

- **Q4** (higher-order $\epsilon$-expansion → fractional retention prediction at theorem level): estimated 2-3 sessions. The fractional chirality retention prediction across observable classes (mass observables retain $\mathcal{O}(\chi^2) \sim 0.6\%$; chirality observables retain $\chi/6 \approx 3.9\%$) needs theorem-level formalization.

- **Q5** (cross-sector consistency with SF-2 W bracelet at theorem level): partial progress in hand from Findings C-W36 + C-W37. Theorem-level formalization estimated 3-5 sessions.

- **Q6** (SM-2 qDP/eDP cross-sector consistency): open at sketch level. Estimated 3-5 sessions.

- **Q7** (cosmological-timing interaction with sub-claim (a) Capotauro nucleation event): estimated 3-5 sessions.

- **Layer 3 promotion of Q1' resolution**: derivation from CPP primitives forcing $\hat{n}$ alignment with host vertex via dynamical/causal/energetic argument, or empirical falsifier distinguishing vertex-aligned and face-aligned predictions at observable level. Long-horizon work; deferred.

### 4.3 Capotauro paper v2.0+ trigger

Q1' minimum closure achieved. The v2.0 paper's §2 reframe path established: $H_4 \to H_3 = I_h$ (vertex-aligned reading) with K3-doublet at one of 10 $D_{3d}$ sub-stabilizers. The v1.0 paper's §6-§10 Wigner-Eckart machinery on $\Dsix$ preserved unchanged at sub-stabilizer level. Additional Q3-Q7 closures would further strengthen the trigger but are not strictly required for v2.0+ ship.

---

## 5. Bootup instructions for next-session pickup

### 5.1 Initial read

Before doing Q3 work, read in order:

1. **This document** (Reading_C_closure_trajectory_handover.md) — full state summary.
2. **`Capotauro_chiral_mechanism_candidate.md` §2.3-§2.4** — the perturbative-distance-ratio argument that Q3 sharpens.
3. **`Capotauro_chiral_mechanism_candidate.md` §11** — the most recent Q1'+Q1'.A resolution at Patch 0419, establishing the vertex-aligned context Q3 operates within.
4. **`capotauro.tex` §2 (sec:substrate_vacuum)** — the paper's substrate-vacuum chirality framing, especially §2.3 (sec:order_parameter) and §2.4 (sec:chi_resolution) — the $\phi^{-3}$ uniqueness argument that Q3 builds on.
5. **`flagship_papers/capotauro/code/q1prime_w_bracelet_geometry.py`** — the verification script (skim if needed; script already establishes Findings C-W36 + C-W37 at <30 second runtime).

### 5.2 Framing question for Q3

The Q3 question rephrased operationally: under vertex-aligned Reading C with $\hat{n} = $ host vertex direction, the 600-cell edges acquire chirality-correlated length perturbations. The substrate's K3-doublet (off-axis at $30°$ from $\hat{n}$) inherits a $\chi$-scale chirality signature. What is the precise scaling relationship between the edge-perturbation magnitude $\epsilon$ and the K3-doublet chirality magnitude $\chi$ that the Capotauro paper takes as foundational input FI-C-9?

The relationship is constrained by:
- The perturbative-distance-ratio argument (paper §2.3-§2.4) forcing $\epsilon$ to land at $\phi^{-3}$ scale
- The K3-doublet's location at a 600-cell face (one of 20 first-shell triangular faces of the host vertex's icosahedron)
- The chirality matrix element machinery's dependence on $\chi$ (FI-C-9) appearing as the primitive scale

### 5.3 Anti-priorities

Do NOT in the next session:
- Modify the Reading C working sketch §1-§11 substantively (only add §12 for Q3 work).
- Modify the verification script's existing checks (only extend if Q3 work requires new geometric verification).
- Modify the Capotauro paper v1.0 .tex source (v2.0+ reframe deferred until further trajectory progress).
- Modify Research_Frontier OPEN-FI-C-9-FP-MECHANISM entry's Q1+Q2+Q1'+Q1'.A content (those questions are closed/resolved; only append Q3 progress).

### 5.4 Trajectory expectation

A Layer 3 closure of Q3 within 1-3 sessions would advance the trajectory estimate from 7-17 sessions → 4-14 sessions. Q4 (2-3 more sessions) would follow, possibly in the same context window. Q5/Q6 (3-5 sessions each) and Q7 (3-5 sessions) are the remaining bulk; total trajectory of 7-17 sessions to full Layer 3 closure remains the standing estimate.

---

## 6. Related artifacts

### 6.1 Sketch sections (`Capotauro_chiral_mechanism_candidate.md`)

| § | Content | Status | Patch |
|---|---|---|---|
| §1 | Introduction | original | 0414 |
| §2 | The Reading C postulate | original (§2.2 Claim retired) | 0414 |
| §3-§8 | Geometric/structural development | original | 0414 |
| §9 | Q1+Q2 closure at Layer 3 | added | 0417 |
| §10 | Q1' partial progress via SF-2 W bracelet | added | 0418 |
| §11 | Q1'+Q1'.A resolution toward vertex-aligned | added | 0419 |

### 6.2 Verification script (`flagship_papers/capotauro/code/q1prime_w_bracelet_geometry.py`)

| Block | Content | Patch |
|---|---|---|
| Steps 1-10 | 600-cell enumeration; SF-2 Theorem 4.2 reproduction; W bracelet centroid → vertex direction identification; cosine identity verification | 0418 |
| Q1'.A verification | Face-host common-neighbor distribution (Counter({2: 1200})); host-outside-face check; K3-face cosine $\sqrt{3}/2$ identity | 0419 |

### 6.3 Session logs

- `session_logs/2026-05-16_session_124_log.md` (Patch 0417)
- `session_logs/2026-05-16_session_125_log.md` (Patch 0418)
- `session_logs/2026-05-16_session_126_log.md` (Patch 0419)

### 6.4 Programme-level registries

- `Research_Frontier.md` OPEN-FI-C-9-FP-MECHANISM entry (Status, Current best lead, Registered fields all updated through Patch 0420)
- `master_glossary.md` Capotauro section (15 entries, including Findings C-W35/C-W36/C-W37 via Patch 0420)
- `predictions.md` PRED-O-25 entry (source field references Reading C trajectory via Patch 0420)
- `problem_histories/PH-OPEN-SM-4.md` Reading C closure trajectory progress section (added Patch 0420)

### 6.5 Patch chain

- Patch 0417 commit (Q1+Q2 closure; sketch §9)
- Patch 0418 commit (Q1' partial progress; sketch §10; verification script created)
- Patch 0419 commit (Q1'+Q1'.A resolution; sketch §11; verification script extended)
- Patch 0420 commit (registry refresh consolidating Sessions 124-126 findings)
- Patch 0421 commit (this handover doc)

---

## 7. Honest scope statement

What this document captures:
- The current state of OPEN-FI-C-9-FP-MECHANISM Reading C closure trajectory through Session 126 Patch 0419.
- All findings, methodological observations, and trajectory revisions from the three-patch arc.
- The forward queue for Q3 and subsequent questions.
- Bootup instructions specific enough for a future context window to pick up Q3 work without re-deriving the Q1+Q2+Q1'+Q1'.A closures.

What this document does NOT capture:
- The detailed mathematical content of sketch §9, §10, §11 (those sections are the primary source; this doc references them).
- The detailed Q3 derivation work itself (that's the next session's substance, not this handover's).
- Cross-sector implications for OPEN-FP-SF-2-CHIR or other downstream closures (mentioned only briefly; primary tracking is at Research_Frontier).

This is a **bootup-ready handover**, not a comprehensive synthesis. It's optimized for getting a next-context-window session productive on Q3 in the first few exchanges, not for being the canonical reference doc for the Reading C closure trajectory (the sketch is canonical).

---

*Created 17 May 2026 (Session 127 Patch 0421). Designed for stale-context-window pickup at next substrate-physics session.*
