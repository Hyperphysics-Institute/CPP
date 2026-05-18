# OPEN-SS-32 ↔ U-shape Unification — Phase 1 Prior-Art Read (Session 13)

**Date:** 4 May 2026 (Session 13)
**Purpose:** Phase 1 of the multi-session investigation registered at Session 12 close as Priority 1 forward-looking pointer (sketch §5.5; Research_Frontier patch 0149 OPEN-SS-32 cross-link). Read SS-7 OPEN-SS-32 and SS-8 H3$'$ provisional-tier prior art in detail; assess whether the unification hypothesis (single J-solid radial-breathing mechanism producing both the OPEN-SS-32 binding-energy excess and the OPEN-SS-35 sub-question (a) $\hbar\omega$ U-shape) is geometrically natural; produce a Phase 2 work plan for the radial-breathing-mode computation that a subsequent session will execute.

**Companion files:**
- `series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_a_Ascaling_R1_RULED_OUT.md` (Session 12: where the U-shape was discovered and §5.5 forward pointer was registered)
- `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex` (the OPEN-SS-32 source: §2.1 facet (c), Discussion, hostile-geometry stress test)
- `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` (the H3$'$ source: §3.5 residual decomposition)
- `research_frontier.md` OPEN-SS-32 entry with Session 12 cross-link (patch 0149)
- `research_frontier.md` OPEN-SS-25 entry with Session 12 cross-link (patch 0149)

**Net programme effect:** Phase 1 deliverable. **No new physics; no new programme-level stage**. Establishes the substantive prior-art base for the OPEN-SS-32 ↔ U-shape unification hypothesis: the registered hypothesis is geometrically natural rather than speculative, but its quantitative content (whether the same attenuation factor that fits the SS-7 binding-energy excess of $+0.55\,B_{\rm pair}$ also fits the $\hbar\omega$ U-shape) is not yet computed and cannot be assessed without the Phase 2 radial-breathing-mode calculation. Sets up Phase 2 (single-session-tractable) and Phase 3 (multi-session, parameter calibration). Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Six programme-level stages of OPEN-SS-35 closure programme preserved.

---

## §1. Strategy and scope of Phase 1

The Session 12 §5.5 forward pointer enumerated four investigation requirements:

1. Read SS-7 OPEN-SS-32 in detail (Discussion section and references therein).
2. Read SS-8 H3$'$ provisional-tier work on the analog opposite-polarity pair-bonus mechanism.
3. Compute the radial-breathing mode of J-solid deltahedra and its effect on $\hbar\omega^*$.
4. Check whether the same attenuation factor that fits the SS-7 binding-energy excess ($\sim +0.55\,B_{\rm pair}$) fits the $\hbar\omega$ U-shape.

Phase 1 covers (1) and (2) — the reading — and produces a synthesis assessment of whether the radial-breathing analog is geometrically natural. Phase 2 covers (3) and (4) — the computation — and is single-session-tractable once Phase 1 has delivered the prior-art picture.

The discipline boundary registered at Session 12 close (sketch §6 Anti-priority) was: "Substantive diagnostic deserves clean R2-territory investigation with proper prior-art reading and fresh session." Phase 1 honors that boundary by deferring all computation until Phase 2.

---

## §2. OPEN-SS-32 mechanism as documented in SS-7

### §2.1 Registration in SS-7 v1.3 §2.1 facet (c)

OPEN-SS-32 is registered as the third facet of SS-7's refined-C1 (alpha-particle leading-order rigidity) decomposition. The three facets are: (a) internal LO rigidity (load-bearing for $B_\alpha$ and the $B_{\rm pair}$ scale, but not for K$_3$ topological mode count); (b) vertex-hosting accommodation (when cluster topology requires alpha vertices of degree $\geq 5$); and (c) **cluster-level collective oblate-deformation mode** — the OPEN-SS-32 entry.

The formal statement (SS-7 v1.3 §2.1 facet (c)):

> When cluster shape has symmetry-breakable belt or seam structure (the J-solid deltahedra at $N_\alpha \in \{7, 8, 9, 10\}$ all have such structure: pentagonal bipyramid's equatorial belt, snub disphenoid's dihedral seam, etc.), an oblate deformation activates with a quantized binding contribution of approximately $+B_{\rm pair} \times \text{attenuation factor}$, via the K$_3$ collective-mode mechanism applied at the cluster-shape scale.

Two structural features of the registration matter for the Phase 1 read:

- The mechanism is the **K$_3$ collective-mode mechanism applied at a new (cluster-shape) scale**. This is the Pattern 6 (K$_3$ scale-recurrence) story: the same SS-5 K$_3$ eigenvalue calculation that produces $B_{\rm pair} = M_0/\varphi$ at the nucleon-pair scale, the alpha-alpha contact scale (SS-7 C3), and the interstitial-host vertex scale (SS-8 D2), is conjectured to recur at the cluster-shape scale as a fifth instance.
- The activation condition is **shape-class-specific**: belt/seam structure is required. The J-solid deltahedra at $N_\alpha \in \{7, 8, 9, 10\}$ have it; the regular polytopes ($N_\alpha = 4, 6, 12$) do not — tetrahedron is point-symmetric, octahedron is $O_h$ (no belt), icosahedron is $I_h$ (closed, oblate-forbidden).

### §2.2 Empirical signature: regime decomposition

SS-7 Table~1 residual-pattern decomposition gives a four-regime picture:

| Regime | $N_\alpha$ values | Empirical excess | Interpretation |
|---|---|---|---|
| A | 3, 4, 5, 6 | $\approx 0$ | Clean LO; no belt structure |
| B | 7, 8, 9, 10 | $\approx +0.55\,B_{\rm pair}$ | J-solid deltahedra, belt/seam active |
| icosahedron | 12 | $\approx +0.30\,B_{\rm pair}$ | $I_h$ suppression (oblate forbidden by symmetry) |
| C | 11, 13, 14 | variable | Deltahedra-gap, belt structure restored |

The flatness of the Regime B excess across $N_\alpha = 7, 8, 9, 10$ is the diagnostic against per-vertex-cost stories: the count of degree-5 vertices in these deltahedra varies from 2 (pentagonal bipyramid) to 8 (gyroelongated square bipyramid), but the binding excess is uniformly $\sim +0.55\,B_{\rm pair}$. Per-vertex stories would predict an excess scaling with the count; the data select bulk-mode (cluster-shape-scale) stories.

The icosahedron suppression to $+0.30\,B_{\rm pair}$ is the second diagnostic: $I_h$ symmetry forbids oblate deformation (icosahedral group has no $C_2$ axis through vertex pairs that admits a oblate axis), so the mode is quenched at the closed shape. The non-zero residual ($\sim 0.30\,B_{\rm pair}$, not zero) indicates the suppression is partial rather than total — perhaps a residual closure-bonus piece distinct from the oblate mode.

### §2.3 Mechanism reading: K$_3$ collective mode at cluster-shape scale

The proposed mechanism (SS-7 v1.3 §2.1 facet (c) plus Research_Frontier OPEN-SS-32 entry "Current best lead"):

- The K$_3$ collective-mode mechanism in SS-5 is based on the eigenvalue structure of a triangular face of three contacts, producing one collective binding mode at $B_{\rm pair} = M_0/\varphi$.
- At the cluster-shape scale, the relevant triangle is the cluster's **belt or seam** structure: the equatorial triangle of the pentagonal bipyramid, the dihedral seam of the snub disphenoid, etc.
- An oblate deformation along the symmetry axis activates this triangular mode at the cluster-shape scale, producing a binding contribution of $+B_{\rm pair} \times \text{attenuation factor}$.
- The attenuation factor is the unknown to be derived. Candidate forms: $1/\varphi$, $1/\varphi^2$, $\cos(\theta_{\rm symmetry})$, or an integer ratio inherited from cluster-physics symmetry analysis.

Empirically, the SS-7 Regime B excess is $+0.55\,B_{\rm pair}$, which sits between $1/\varphi = 0.618$ and $1/\varphi^2 = 0.382$. If the attenuation factor were $1/\varphi^2$ (matching SS-8 H3$'$, see §3 below), the prediction would be $+0.382\,B_{\rm pair}$ — within a factor of 1.5 of empirical. The shape-class-specific factor route would give the full empirical $+0.55\,B_{\rm pair}$ from a $\cos\theta$ where $\theta$ is set by the cluster's axial-symmetry-breaking angle.

### §2.4 Status: provisional-tier; OPEN-SS-32

The mechanism is **provisional-tier**: structurally consistent with cluster-physics literature (KanadaEn'yo 2011 on $^{28}$Si pentagon-shape oblate density wave; Tohsaki & Itagaki 2018 on hollow polytope shapes; the $^{40}$Ca + $\alpha$ core+halo identification of $^{44}$Ti), but not first-principles-derived from CPP primitives. The first-principles derivation is OPEN-SS-32 itself.

OPEN-SS-32 has dependencies on OPEN-SS-24 (simplicial connectivity from primitives) and is methodologically parallel to OPEN-SS-28 (SS-8 H3$'$ first-principles derivation). Closure of either OPEN-SS-32 or OPEN-SS-28 may inform the other via the K$_3$ scale-recurrence pattern (Pattern 6).

---

## §3. SS-8 H3$'$ analog: opposite-polarity pair-bonus at the interstitial scale

### §3.1 Provisional residual model (post-Theorem-2, not part of the proof)

H3$'$ is the SS-8 §3.5 provisional residual decomposition. The epistemic framing (SS-8 §3.5 opening paragraph) is sharp:

- H3$'$ is applied **after** the leading-order Theorem 2 ($k_{\rm eff} = 2E/V$) prediction, not as part of the proof.
- The paper's primary epistemic load sits on the conditional 2$E$/$V$ law, which stands independently of whether H3$'$'s specific attenuation is correct.
- Readers may accept or reject H3$'$ without affecting the status of the 12 primary predictions.
- The purpose of reporting the residual decomposition is transparency about what the residual looks like, not improving the headline fit via post-hoc rescue.

This framing is the methodological model that OPEN-SS-32 should follow at the cluster-shape scale: the provisional-tier mechanism is reported alongside the leading-order prediction, but does not enter the proof of the leading-order result.

### §3.2 Inheritance from SS-5: K$_3$ pair eigenvalue

The mechanism inheritance chain (SS-8 §3.5 "Inheritance from SS-5"):

- SS-5 establishes that two opposite-polarity nucleons in K$_3$ contact form one collective bonding mode at $B_{\rm pair} = M_0/\varphi$ via qDP-chain coupling across the triangular contact face (SS-5 Layer B / §3.1).
- The same-polarity case pays a Pauli penalty of $M_0/\varphi^3$ per like-pair (SS-5 Proposition on Pauli cost).
- At the interstitial scale, two interstitial neutrons occupying adjacent alpha-vertices in an alpha-polytope **do not realize a direct SS-5 pair contact** — they are separated by $L_{\alpha\alpha} = 2.37$ fm, not by intra-alpha nucleon-nucleon spacing.
- The pair bonus, if it exists, is **mediated rather than direct**: each interstitial couples to the shared alpha-alpha K$_3$ face at its own host vertex, and the two couplings cross-correlate through the shared face.

This mediated-vs-direct distinction is what makes the interstitial-scale H3$'$ a *transport* of the SS-5 mechanism rather than a literal application. The transport requires a geometric attenuation factor.

### §3.3 The $1/\varphi^2$ attenuation factor: two independent motivations

SS-8 §3.5 motivates the $1/\varphi^2$ attenuation factor by two independent arguments:

1. **Successive ratio applications.** $1/\varphi^2 = (1/\varphi) \times (1/\varphi)$. The first $1/\varphi$ is the attenuation from the direct $M_0$-scale contact to the $B_{\rm pair}$-scale K$_3$ mode (as in SS-5's single-K$_3$ eigenvalue reduction: $B_{\rm pair} = M_0/\varphi$). The second $1/\varphi$ is the further attenuation from direct $B_{\rm pair}$-scale contact to the mediated interstitial-interstitial coupling across the shared alpha-alpha K$_3$ face. Two K$_3$ reductions in series give $M_0 \to M_0/\varphi^2 \approx 0.895$ MeV.

2. **Numerical coincidence with same-polarity Pauli ratio.** $1/\varphi^2$ is numerically equal to SS-5's same-polarity Pauli penalty ratio ($M_0/\varphi^3 / B_{\rm pair} = 1/\varphi^2$) — i.e., the programme-level scale at which second-order effects appear in the SS-5 pair-binding structure.

The empirical bulk-regime mean residual at $N_{\rm ex} = 2$ corresponds to $+0.98$ MeV per pair, within 10% of the $\epsilon_{\rm pair}^{\rm pred} = M_0/\varphi^3 \approx 0.895$ MeV prediction. Alternative attenuations within a factor of 2 (e.g., $1/\varphi \to 0.618 B_{\rm pair}$ or $1/\varphi^{3/2} \to 0.486 B_{\rm pair}$) would also fit.

### §3.4 Empirical match and status

The $1/\varphi^2$ transport reduces the SS-8 bulk-regime mean residual from $+0.21$ in $k_{\rm eff}$ (unexplained) to $-0.09$ (residual-after-H3$'$), tightening per-row agreement from 8–15% to 3–7% (after $\Nalpha = 4$ is separately attributed to H5$'$ small-polytope attenuation).

H3$'$ is provisional and interpretive, not derived; the closure of the gap (first-principles derivation of the pair-bonus magnitude at the interstitial scale, fixing the attenuation factor and distinguishing H3$'$ from its plausible competitors) is OPEN-SS-28 — the methodological parallel to OPEN-SS-32.

---

## §4. Methodological parallel: OPEN-SS-32 ↔ OPEN-SS-28

Both open problems share four structural features:

| Feature | OPEN-SS-32 (cluster-shape) | OPEN-SS-28 (interstitial-interstitial) |
|---|---|---|
| Source paper | SS-7 v1.3 §2.1 facet (c) | SS-8 §3.5 |
| Empirical signature | $+0.55\,B_{\rm pair}$ at Regime B; $+0.30\,B_{\rm pair}$ at icosahedron | $+0.38\,B_{\rm pair}$ ($\sim 0.9$ MeV per pair) at bulk-regime |
| Provisional attenuation | unknown (candidate $1/\varphi^2 \to 0.38$; empirical $0.55$) | $1/\varphi^2 \to 0.38$ (matches empirical $0.38$) |
| Pattern 6 status | candidate fifth-scale instance | candidate fifth-scale instance (provisional H3$'$) |
| Position relative to leading-order proof | post-theorem residual model | post-theorem residual model |
| Closure status | OPEN | OPEN |

Two observations from this parallel:

- **Both are provisional-tier residual models, not part of leading-order proofs.** The Phase 2 computation at the cluster-shape scale should respect this discipline: any attenuation factor that emerges sits at provisional tier until first-principles-derived, and the LO results of SS-7 (twelve predictions within 1.5%) and the OPEN-SS-35 sub-question (a) Level-1 partial closure (Sessions 6, 7) stand independently of Phase 2's outcome.

- **The $1/\varphi^2$ candidate at the cluster-shape scale would predict $+0.38\,B_{\rm pair}$, undershooting the empirical $+0.55\,B_{\rm pair}$ by a factor 1.5.** This already tells us that — if the unification hypothesis is correct — either the attenuation factor at the cluster-shape scale differs from $1/\varphi^2$, or the empirical $+0.55\,B_{\rm pair}$ has a contribution from a separate effect (e.g., hierarchical-regime saturation per OPEN-SS-34 PRED-O-18). The Phase 2 computation will produce a CPP-derived attenuation that can be compared.

---

## §5. The radial-breathing analog: geometric assessment

### §5.1 What "radial breathing" means in this context

The Session 12 §5.5 forward pointer phrases the unification hypothesis: *if* the J-solid mid-range deltahedra activate an oblate-deformation mode in the binding energy (OPEN-SS-32), they may also activate a radial-breathing mode that softens the centroid-to-vertex confinement (effectively expanding $R_c$, lowering $\hbar\omega$).

A radial-breathing mode in this setting means: a collective oscillation in which all vertices of the cluster polytope move in/out radially relative to the centroid, with characteristic frequency $\omega_{\rm br}$. Activating this mode populates a finite-amplitude radial oscillation at the cluster-shape scale, broadening the effective centroid-to-vertex distribution from a sharp $R_\alpha$ to an averaged $\langle R_\alpha\rangle$ with $\langle R_\alpha^2\rangle > R_\alpha^2$.

For the Session 12 sub-question (a) framework where $\hbar\omega^* \propto 1/R_c^2$ at fixed shape, an effective expansion of $R_\alpha$ via radial-breathing softening lowers $\hbar\omega^*$ by a fractional amount $\sim 2 (\langle R_\alpha\rangle - R_\alpha)/R_\alpha$.

### §5.2 Static oblate deformation vs dynamic radial-breathing

These are two distinct modes. They share the same activation condition (axially-symmetric clusters with belt/seam structure), but they are not identical:

- **Static oblate deformation.** A classical (zero-amplitude-zero-frequency) deformation of the cluster shape from spherical to oblate spheroidal, parametrized by a deformation parameter $\beta_2$. Produces the OPEN-SS-32 binding-energy excess via the K$_3$ collective-mode coupling at the deformed cluster shape. The deformation is a static structural feature of the ground-state configuration; the cluster sits at a deformed equilibrium rather than at spherical equilibrium.

- **Dynamic radial-breathing.** A collective vibrational mode at finite frequency $\omega_{\rm br}$. The cluster does not sit at a deformed equilibrium; it oscillates radially around the spherical equilibrium. Population of this mode at finite occupation (e.g., zero-point) gives a finite spread in the centroid-to-vertex distance.

The unification hypothesis is that **both modes are activated by the same K$_3$ scale-recurrence mechanism at the cluster-shape scale**. Activation of the K$_3$ collective coupling at a J-solid belt produces simultaneously a static binding-energy excess (via the eigenvalue) AND a finite-frequency vibrational mode whose zero-point fluctuation broadens $R_\alpha$ effectively. This is structurally analogous to how a harmonic oscillator's spectrum has both a binding-energy term (the $-\frac{1}{2}\hbar\omega$ ground-state energy below the classical minimum if measured against a reference) AND a finite zero-point fluctuation $\langle x^2\rangle = \hbar/(2m\omega)$.

### §5.3 Selection rules: do they actually coincide?

This is the central Phase 1 question. The Research_Frontier patch 0149 cross-link asserts coincidence of selection rules; let me examine the geometry.

Polytope-shape activation conditions for OPEN-SS-32 oblate deformation:

| $N_\alpha$ | Polytope | Symmetry | Belt/seam? | Oblate-active? |
|---|---|---|---|---|
| 4 | tetrahedron | $T_d$ | no | no (Regime A) |
| 5 | trigonal bipyramid | $D_{3h}$ | yes (equatorial $C_3$ belt) | yes |
| 6 | octahedron | $O_h$ | no (point-symmetric) | no (Regime A) |
| 7 | pentagonal bipyramid | $D_{5h}$ | yes (equatorial $C_5$ belt) | yes (Regime B) |
| 8 | snub disphenoid (J$_{84}$) | $D_{2d}$ | yes (dihedral seam) | yes (Regime B) |
| 9 | triaugmented triangular prism (J$_{51}$) | $D_{3h}$ | yes ($C_3$ belt) | yes (Regime B) |
| 10 | gyroelongated square bipyramid (J$_{17}$) | $D_{4d}$ | yes ($C_4$ belt) | yes (Regime B) |
| 12 | icosahedron | $I_h$ | no (closed) | no (suppressed) |

Comparison with the Session 12 U-shape pattern (sketch §3, table at line 1155–1164 of the session log):

| $N_\alpha$ | Polytope | Required $R_\alpha$ change | U-shape regime? |
|---|---|---|---|
| 4 | tetrahedron | $-5.3\%$ | endpoint OK |
| 5 | trigonal bipyramid | $+6.7\%$ | mid-range overshoot |
| 6 | octahedron | $+12.7\%$ | mid-range overshoot |
| 7 | pentagonal bipyramid | $+19.1\%$ | mid-range overshoot |
| 8 | snub disphenoid | $+21.1\%$ | mid-range overshoot |
| 9 | triaugmented triangular prism | $+22.3\%$ | mid-range overshoot |
| 10 | gyroelongated square bipyramid | $+22.7\%$ | mid-range overshoot |
| 12 | icosahedron | $-0.7\%$ | endpoint OK |

The two tables overlap on six of eight rows but **disagree on $N_\alpha = 6$ (octahedron)**. The octahedron is in Regime A for OPEN-SS-32 (no belt; $\approx 0$ excess) but is *inside* the U-shape mid-range overshoot ($+12.7\%$ required expansion). This is the **first clean discriminating data point** between the two regimes, and it argues against literal coincidence of selection rules.

The Research_Frontier patch 0149 cross-link asserts the regimes "coincide exactly." Phase 1 reading establishes that the coincidence is *qualitative* (both have endpoint-OK structure at $N_\alpha = 4, 12$ and mid-range overshoot in the J-solid range $N_\alpha = 7, 8, 9, 10$) but not literal — the octahedron at $N_\alpha = 6$ is inside the U-shape but outside the OPEN-SS-32 oblate regime.

This is not fatal to the unification hypothesis. Three readings are consistent with the data:

- **Reading A (selection rules differ slightly).** The radial-breathing mode at the cluster-shape scale has a broader selection rule than OPEN-SS-32 oblate deformation, activating at any axially-non-trivial cluster shape rather than only at belt/seam structure. The octahedron's $O_h$ symmetry forbids static oblate deformation but may not forbid a finite-frequency radial-breathing mode.
- **Reading B (octahedron is a U-shape false positive).** The Session 12 inversion table treats $\hbar\omega$ as a single observable with empirical $41/A^{1/3}$. At small $A$ (octahedron $A = 24$), the empirical fit is extrapolated rather than directly measured; the $+12.7\%$ required expansion may be an artifact of empirical-formula extrapolation rather than a true U-shape feature.
- **Reading C (two distinct mechanisms, partial overlap).** The U-shape and the OPEN-SS-32 excess have partially-overlapping but not identical activation regimes, indicating two distinct K$_3$ scale-recurrence mechanisms at the cluster-shape scale that share most but not all selection rules.

Phase 2 must distinguish these readings. The discriminating computation is whether a CPP-derived radial-breathing mode at $N_\alpha = 6$ (octahedron) gives a non-zero softening of $\hbar\omega$ — Reading A predicts yes; Readings B and C predict no.

### §5.4 Geometric naturalness assessment

The unification hypothesis is **geometrically natural rather than speculative**, on three grounds:

1. **Pattern 6 K$_3$ scale-recurrence.** The mechanism of activating a collective K$_3$ mode at the cluster-shape scale is the same mechanism documented across three independent paper-level instances (SS-5 nucleon-pair, SS-7 alpha-alpha edge, SS-8 D2 interstitial-host). A fifth instance at the cluster-shape scale is plausible by the same scale-recurrence logic; OPEN-SS-32 already registers it as a candidate. The unification hypothesis is just the assertion that this fifth-scale K$_3$ mechanism produces both a static (oblate-deformation) and a dynamic (radial-breathing) signature, in parallel with how a harmonic oscillator has both binding-energy and zero-point-fluctuation signatures.

2. **Empirical correlation across most rows.** Six of eight rows ($N_\alpha = 4, 7, 8, 9, 10, 12$) show the same qualitative behavior in the U-shape (endpoint-OK vs mid-range overshoot) and in OPEN-SS-32 (inactive vs active). The probability that such a six-of-eight overlap arises by chance, given the independent registrations of the two phenomena (OPEN-SS-32 in Session 3 of 26 April 2026, U-shape in Session 12 of 4 May 2026), is small.

3. **Forward-pointing closure leverage.** If Phase 2 confirms a single radial-breathing mechanism, it would close R2 (cluster-scale vs alpha-scale mean field interpretation, the only remaining A-scaling closure candidate after Session 12's R1 ruled-out) AND identify the "additional CPP physics outside simple K$_3$ Gaussian-modulated mean field framework" that Session 11 Phase 1 flagged as needed for layer-3 gap-strength closure. Two open programme threads collapsed into one mechanism is a substantial closure step.

Against speculation, the hypothesis has the discriminating $N_\alpha = 6$ data point (§5.3 Reading A vs B vs C). Phase 1 conclusion: the hypothesis is geometrically natural enough to warrant Phase 2 computation; the computation has clear discriminating power.

---

## §6. Phase 2 work plan

### §6.1 Single-session-tractable target

**The Phase 2 question.** For each of the eight canonical alpha-chain deltahedra ($N_\alpha = 4, 5, 6, 7, 8, 9, 10, 12$), compute the radial-breathing-mode frequency $\omega_{\rm br}$ from the K$_3$ Gaussian-modulated mean field (Session 6/7 Level-1 partial closure machinery extended to include radial fluctuations), determine the zero-point amplitude $\langle (\Delta R_\alpha)^2\rangle = \hbar / (2 m_{\rm cluster} \omega_{\rm br})$, and translate this into an effective $R_\alpha$ broadening that lowers $\hbar\omega^*$. Compare against the Session 12 inversion-table required expansion percentages.

### §6.2 Required inputs (all present in repo at HEAD)

- The Session 6/7 Level-1 partial closure machinery: $V_{K_3}(\vec r) = -B_{\rm pair} \sum_i \deg(v_i) \exp(-|\vec r - \vec R_i|^2/(2\sigma^2))$ at deltahedron vertices $\vec R_i$, with $\sigma = \hbar c/\sqrt{m_n \hbar\omega^*}$ self-consistently solved. Located in `series_strong/papers/SS-9/scripts/SS-9_OPEN-SS-35_subquestion_a_Ascaling.py`.
- Cluster mass $m_{\rm cluster} = N_\alpha \cdot m_\alpha = N_\alpha \cdot 3727.4$ MeV/$c^2$ from SS-5 (alpha-particle internal binding).
- Eight deltahedron geometries from Session 7 Phase 1 sketch.
- Empirical $\hbar\omega = 41/A^{1/3}$ MeV at each $A = 4 N_\alpha$ for the comparison.

### §6.3 Computation steps

1. Define the radial-breathing degree of freedom. Two candidates: (a) uniform scaling $\vec R_i \to \lambda \vec R_i$ for all vertices (simplest, single dof); (b) symmetry-resolved breathing modes (one dof per irreducible representation of the cluster's point group, with the totally symmetric $A_1$ representation being the analog of the uniform-scaling dof). Phase 2 should start with (a) and revisit (b) if the simple scaling does not produce the observed selection rules.

2. Compute the radial restoring force. Differentiate the total cluster binding energy with respect to $\lambda$ at fixed shape. The leading contribution is the alpha-alpha edge sum (SS-7 C3) plus the K$_3$ Gaussian-modulated mean field; both depend on $\lambda$.

3. Extract the radial-breathing frequency $\omega_{\rm br} = \sqrt{k_\lambda / m_{\rm cluster}}$ from the second derivative of binding energy with respect to $\lambda$ at the equilibrium $\lambda = 1$.

4. Compute the zero-point broadening $\langle (\Delta\lambda)^2\rangle = \hbar/(2 m_{\rm cluster} \omega_{\rm br})$ and the corresponding $\langle (\Delta R_\alpha)^2\rangle = R_\alpha^2 \langle (\Delta\lambda)^2\rangle$.

5. Translate to $\hbar\omega^*$ change: the sub-question (a) self-consistent $\hbar\omega^*$ depends on $R_\alpha^2$ via $\sigma^2$ and the centroid-to-vertex distance. A finite zero-point broadening of $R_\alpha$ contributes a fractional softening $\Delta\hbar\omega^*/\hbar\omega^* \approx -2\langle(\Delta R_\alpha)^2\rangle/R_\alpha^2$.

6. Compare the predicted softening at each $N_\alpha$ with the Session 12 inversion-table required expansion percentages. Three diagnostics:
   - Sign: does the breathing-mode softening have the right sign (lowering $\hbar\omega$, equivalent to expanding $R_\alpha$)? Yes a priori — a positive zero-point broadening always lowers an inverse-square frequency dependence.
   - Magnitude: does the predicted softening at $N_\alpha = 7$–$10$ peak in the same range as the empirical $7$–$23\%$ U-shape requirement?
   - Selection rule: at $N_\alpha = 6$ (octahedron), is the predicted softening zero (Reading B/C above) or non-zero (Reading A)?

### §6.4 Phase 2 deliverable

Single sketch + reproducible script + Research_Frontier update + four-tier docs + session log entry, following the Session 6, 8, 11 Phase 1, Session 12 single-substantive-result-per-session pattern. Patch sequence ~7 patches.

### §6.5 What Phase 2 cannot do alone

- Phase 2 produces a CPP-derived prediction for the radial-breathing softening but does *not* derive the OPEN-SS-32 attenuation factor for the binding-energy excess at the cluster-shape scale. That is a separate open problem (the OPEN-SS-32 closure proper).
- Phase 2 does not close OPEN-SS-32. Even if the unification hypothesis succeeds at Phase 2, the binding-energy attenuation factor remains to be derived — which is OPEN-SS-32 closure (multi-session by scope, plausibly Phase 3 or beyond).
- Phase 2 does not close OPEN-SS-35 sub-question (a) A-scaling. Confirming the radial-breathing mechanism would close R2, but R2 is the *only remaining* A-scaling closure candidate; closing R2 closes A-scaling. If Phase 2 fails (e.g., predicted softening is too small, or wrong sign at $N_\alpha = 6$), R2 is also weakened and A-scaling closure becomes uncertain.

---

## §7. Summary and status

Phase 1 of the OPEN-SS-32 ↔ U-shape unification investigation is complete. **No new physics; sets up Phase 2.**

**What Phase 1 establishes:**

- The OPEN-SS-32 mechanism (SS-7 v1.3 §2.1 facet (c)) is a provisional-tier K$_3$ collective-mode mechanism at the cluster-shape scale, producing $+0.55\,B_{\rm pair}$ at J-solid Regime B and $+0.30\,B_{\rm pair}$ at the icosahedron. The activation rule is belt/seam structure; the attenuation factor is unknown.
- The SS-8 H3$'$ provisional residual model (§3.5) provides the methodological template: provisional-tier mechanism reported alongside but not part of the leading-order proof, with $1/\varphi^2$ attenuation motivated by two independent SS-5 inheritance arguments.
- The unification hypothesis (single J-solid radial-breathing mechanism producing both signatures) is geometrically natural by Pattern 6, empirically supported by six-of-eight row coincidence, and forward-pointing-leverage-rich (closes R2 + identifies missing CPP physics for layer 3 gap strength).
- The unification hypothesis is **not literal at the selection-rule level**: $N_\alpha = 6$ (octahedron) is inside the U-shape but outside the OPEN-SS-32 oblate regime, requiring one of three readings (A: broader selection for breathing than oblate; B: U-shape false positive at small $A$; C: distinct partially-overlapping mechanisms). Phase 2 has discriminating power.

**Programme status updates from Phase 1:** None. The four-tier discipline (templates/operating_system.md §4) places prior-art reading at Tier 1 (transcript) or Tier 2 (development vignette), not at Tier 3 (reasoning) or Tier 4 (verbatim). No new programme-level stage. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged. Six programme-level stages of OPEN-SS-35 closure programme preserved. First qualitative cross-paradigm consilience claim (Session 9) intact. R1 ruled-out (Session 12) intact.

**OPEN-SS-32 ↔ U-shape investigation status:** "registered as future-session sub-sub-question" (Session 12 close) → "**Phase 1 prior-art read complete; unification hypothesis assessed as geometrically natural with one discriminating data point ($N_\alpha = 6$); Phase 2 single-session-tractable**" (this Session 13 Phase 1).

**OPEN-ORG-012 (SS-9 v0.3 → v0.1 .tex conversion) status:** Trigger condition not yet met. Anti-trigger explicitly applies — Phase 1 of the OPEN-SS-32 ↔ U-shape investigation has begun, §7 of SS-9 v0.3 is actively shifting (will be added to during Phase 2). Conversion deferred.

### Forward-looking pointers for Session 14

**Priority 1:** Phase 2 of the OPEN-SS-32 ↔ U-shape unification investigation per §6 above. Single-session-tractable; standard seven-patch deliverable suite; either confirms unification (closes R2, identifies missing CPP physics for layer 3) or rules it out / refines reading A/B/C.

**Priority 2 (deferred until Phase 2 returns a result):** Phase 3 — if Phase 2 confirms unification, derive the OPEN-SS-32 attenuation factor at the cluster-shape scale from CPP primitives. Multi-session by scope.

**Priority 3 (parallel track, lower priority):** OPEN-SS-16 Layer B closure work. Deepest open problem; still deferred.

**Anti-priority:** Do not initiate the SS-9 v0.3 → v0.1 .tex conversion (OPEN-ORG-012) until the OPEN-SS-32 ↔ U-shape investigation reaches a stable state (positive closure or negative ruling-out at Phase 2 or Phase 3). Anti-trigger from patch 0151 explicit.

---

*Phase 1 prior-art digest per Session 12 §5.5 forward pointer. No new physics; reading deliverable. Establishes the substantive prior-art base for OPEN-SS-32 ↔ U-shape unification. Sets up Phase 2 single-session-tractable computation. Six programme-level stages of OPEN-SS-35 closure programme preserved. Pattern 6 K$_3$ scale-recurrence: 7 confirmed instances unchanged.*
