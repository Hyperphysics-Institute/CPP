# Mechanism — SS-8: Interstitial-Neutron Binding and the 2E/V Scaling Law on the Alpha-Polytope

**Location:** `/CPP/series_strong/papers/SS-8/documentation_suite/mechanism-SS-8.md`
**Last updated:** 26 April 2026 (v1.0 currency)
**Companion to:** `SS-8_interstitial_neutron_2EV_scaling.tex` (v1.0)

---

## Mechanism 1: Interstitial localization at an alpha-vertex (D1)

**What it does:** Selects which point in the alpha-polytope a freshly-added interstitial neutron occupies — the answer is "an alpha-vertex," not an edge-midpoint, face-center, or polytope centroid.

**How it works:** When a neutron is added to a strict-$N=Z$ alpha-cluster nucleus beyond the baseline, the SSV-minimization functional has its lowest value at an alpha-vertex site. Two functionally independent physical pictures both deliver this conclusion: Model A counts K₃-edge contacts available at each candidate site (under D2's coupling rule, vertices have access to more contacts than edge-midpoints or face-centers), and Model B applies short-range Yukawa pair physics directly (the strong-interaction range is shorter than the polytope edge length, so localization at a vertex maximizes overlap with the alpha core). Q2 algebraic-reduction analysis (22 April 2026 session) confirms Model B does *not* reduce to Model A under any short-range regime — they make distinguishable predictions about multiplicity vectors, non-vertex orderings, and vertex-degree scaling.

**Key insight:** The two models look superficially similar (both pick alpha-vertices) but operate on functionally independent principles, giving D1 the status of a Level-1+2 conditional theorem rather than a single-mechanism conjecture. Where the conditionality remains (Level-3 OPEN-SS-26 PARTIAL): both models share a "proximity-binding" ancestor — the implicit assumption that interstitials prefer to be close to the alpha core rather than far from it. A model that produced D1 *without* invoking proximity would close the Level-3 gap.

---

## Mechanism 2: K₃-edge coupling at the host vertex (D2)

**What it does:** Specifies how an interstitial neutron at an alpha-vertex couples to its surroundings — through the K₃ contact-face edges incident at that vertex.

**How it works:** Each alpha-alpha contact face in the polytope is a K₃ collective mode (inherited from SS-7's per-edge $B_\text{pair}$ derivation). When an interstitial neutron localizes at vertex $v$, it overlaps the outer-nucleon contact face of its host alpha. That overlap activates the K₃ mode along each contact edge incident at $v$ — and each activated K₃ edge contributes binding strength exactly $B_\text{pair}$, the same quantum that operates at the SS-5 nucleon-pair scale and the SS-7 alpha-alpha scale. The total per-neutron binding accrual at vertex $v$ is therefore $\deg_v \cdot B_\text{pair}$, where $\deg_v$ is the polytope vertex degree.

**Key insight:** This is the third recurrence of the $B_\text{pair}$ quantum at a coarser physical scale. SS-5 placed it at nucleon-pair contacts internal to the alpha; SS-7 placed it at alpha-alpha base-to-base contact faces; SS-8 places it at the interstitial-host coupling. The same eigenvalue calculation replicates because the underlying graph is the same topological object (K₃) — only the physical scale at which its three nodes live changes. D2 is invoked as a paper-level structural hypothesis in SS-8 v1.0; OPEN-SS-27 targets its derivation from an A6′ extension.

---

## Mechanism 3: Bulk-regime averaging (D3)

**What it does:** Connects the per-vertex binding accrual $\deg_v \cdot B_\text{pair}$ (which depends on which specific vertex the neutron localizes at) to a polytope-level average that depends only on $N_\alpha$.

**How it works:** When $N_\text{ex}/V \ll 1$, the $N_\text{ex}$ interstitial neutrons distribute approximately uniformly across the $V = N_\alpha$ available vertices. Under uniform vertex-distribution, the average per-neutron binding is the average vertex degree $\bar{d}_v = (1/V) \sum_v \deg_v = 2E/V$, where the second equality follows from the graph-theoretic identity that each edge contributes 2 to the sum of degrees. For simplicial 3-polytopes specifically, Euler's formula $V - E + F = 2$ together with the triangle constraint $2E = 3F$ gives $E = 3V - 6$ exactly, so $2E/V = 6 - 12/V$. Multiplying by $B_\text{pair}$ delivers the SS-8 central prediction $\Delta_1(N_\alpha) = (6 - 12/N_\alpha) \cdot B_\text{pair}$.

**Key insight:** The geometric content of the central prediction is purely combinatorial — the $6 - 12/V$ form is a theorem of graph theory, exact, polytope-identity-independent. Whether two simplicial deltahedra at the same $N_\alpha$ realize the polytope (e.g., octahedron vs. triangular antiprism at $N_\alpha = 6$) does not change the prediction: both have $2E/V = 4$, both predict the same $\Delta_1$. This robustness is why the SS-8 prediction agrees at sub-1% levels at the most symmetric polytopes despite the polytope-identity ambiguity. The bulk-regime assumption breaks down at $N_\text{ex} \geq 5$ on small polytopes ($N_\alpha \leq 8$), which is the scope-disclosed limit of the secondary 30-cell extension.

---

## Mechanism 4: Pattern 6 scale recurrence

**What it does:** Provides a structural account of why the same quantum $B_\text{pair}$ operates at three nuclear scales without rescaling.

**How it works:** The eigenvalue $B_\text{pair} = M_0/\varphi$ comes from the K₃ graph's spectral structure — a mathematical object defined by its connectivity rather than by any specific physical scale. SS-5 implements K₃ as a triangle of nucleon-nucleon contacts internal to a single alpha. SS-7 implements K₃ as a triangle of alpha-alpha contact faces at each polytope edge. SS-8 implements K₃ as the three contact-face edges incident at each polytope vertex. Each implementation is a *physical* realization of the same *topological* object; the eigenvalue calculation runs identically because it depends only on the graph, not on the scale. Each new physical realization produces a new empirical test of the same axiom-derived constant.

**Key insight:** This is the deepest structural claim in SS-8 — and the one the paper most carefully avoids over-asserting. Whether the K₃ structure is *forced* to recur at successive scales by the CPP axiom set (in which case finding a fourth scale where it does not appear would falsify CPP), or merely *permitted* (in which case the scale recurrence is contingent and the absence at a fourth scale is allowed), remains genuinely open. SS-8 v1.0 adds a fourth data point to the Pattern 6 inquiry — the interstitial-interstitial pair-bonus transport in §4.5 (H3′ residual decomposition) — without claiming to resolve which interpretation is correct.

---

## Mechanism 5: Provisional residual model — opposite-polarity pair bonus (H3′) and small-polytope attenuation (H5′)

**What it does:** Accounts for the observed bulk-regime residual (mean $+0.21$ in $k_\text{eff}$, corresponding to $+0.49$ MeV per interstitial) by inheriting two SS-5 mechanisms transported to the interstitial-alpha scale.

**How it works:** H3′ posits that two interstitials of opposite polarity at the same vertex (or paired across a polytope edge) gain an additional $B_\text{pair}/\varphi^2 \approx 0.895$ MeV pair bonus per pair, inherited from SS-5's K₃ pair mechanism with a $1/\varphi^2$ geometric attenuation factor reflecting the longer interstitial-vs-nucleon distance. Empirically this matches the +0.98 MeV per pair (within 10%) implied by the bulk-regime residual, supporting the inheritance interpretation. H5′ posits that small polytopes ($N_\alpha \leq 4$) attenuate the H2′ scaling law because the bulk-regime averaging assumption is violated at the polytope-size limit. Both H3′ and H5′ are *interpretive* — they are applied after the leading-order proof of THEO-SS-15 rather than as part of the proof.

**Key insight:** The residual decomposition is a structural tightening, not a fit. No parameters are introduced; H3′'s pair bonus is the SS-5 inheritance with no rescaling; H5′'s attenuation is structural rather than parametric. The decomposition shrinks the apparent bulk-regime band from 8–15% to 3–7% per row, but the paper's primary epistemic load remains on the conditional 2E/V law itself — readers may accept or reject H3′/H5′ without affecting the status of the 12 primary predictions.
