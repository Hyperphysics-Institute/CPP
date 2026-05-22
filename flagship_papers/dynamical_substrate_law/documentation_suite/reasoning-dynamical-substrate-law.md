# Tier 4 — Verbatim Opus Reasoning Narrative: Dynamical Substrate Law

**Paper:** F.1 = Dynamical-Substrate-Law gate (flagship paper home: `flagship_papers/dynamical_substrate_law/`, paper not yet assembled — closure trajectory at sketch level pending Phase 2 foundations work).

**File started:** 21 May 2026 (Session 138 close, Patch 0530 — handover protocol execution per §15 Step D, Thomas's directive "record all substantive physics verbatim").

**Discipline:** Per `templates/operating_system.md` §4 Four-Tier Documentation Discipline + §15 Step D. This file preserves verbatim substantive reasoning across the F.1 sub-question closure trajectory (Patches 0522–0529) at Session 138 continuation. Tier 4 is **the canonical record** per Thomas's goal-statement; the sketch §11–§14 polished content is a derivative artifact of the reasoning preserved here, not a substitute.

**Anti-pattern explicitly avoided:** This file does NOT compress the substantive reasoning into polished prose. The alternatives considered, framings revised, moments of uncertainty, and pushbacks are preserved as they occurred. Where this conflicts with prose readability, the reasoning preservation takes precedence.

---

## §0 One-paragraph summary

The F.1 sub-question closure trajectory at Session 138 (Patches 0522–0529) attempted to close the F.2/F.3 viability decision gate's load-bearing question: *does the substrate primitive 4D direction $\hat{n}$ induce PCD-cycle-orientation $\vec{\omega}_{PCD}$ via a substrate-mechanism derivable from CPP axioms?* Four phases were executed in sequence under Mechanism A (DI-bit propagation-rate asymmetry primitive): Phase 1 derived a non-vanishing cycle-mediated informational bias current $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\varphi^2)\hat{n}$ at Layer 3 (Patch 0524); Phase 2 derived a PCD-coupling rule $\vec{\omega}_{PCD} = \sigma_{cycle} \cdot \hat{j}_{DI}^{net}/|\hat{j}_{DI}^{net}|_0$ via parity-repair at Layer 2.5 (Patch 0525); Phase 3 derived the substrate-Wigner-Eckart matrix element $|M^{thermo}| = |\delta|/6$ via canonical normalization + reduced matrix element + universal Schur factor, with Case A.1 minimal unified realization ($\delta = \chi$) giving $\chi/6 \approx 0.0394$ at Layer 3 (Patch 0526); Phase 4 established phenomenological consistency at 1.64% deviation vs $\Delta p_{LR}^{obs} \sim 0.04$ at viability level (Patch 0527). After ChatGPT reviewer-pause checkpoint identified eight overclaimed-language items + one unflagged ansatz, Patch 0528 applied calibrations downgrading "FULL CLOSURE" to "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work," and Patch 0529 re-engaged the decision gate with calibrated §7.2 verdict structure. Three open structural commitments registered as the real bottleneck: (B.1) local algebraic representation ansatz, (B.2) $\sigma_{cycle}$ algebraization rigor, (B.3) Case A.1 derivational support.

## §1 Tier 4 inclusion scope

**Included verbatim:**
- Substantive physics reasoning across the four phases (alternatives considered, derivation choices, framings)
- Reviewer-pause checkpoint reasoning (the moment of self-recognition that triggered the package; the engagement with ChatGPT's pushback)
- Calibration reasoning (the eight language-calibration items at Patch 0528)
- Decision-gate re-engagement reasoning (the §7.2 verdict structure update logic)
- Programme-level reasoning that informed the trajectory (the swarm-validation framing, the chirality continuum architectural template inheritance, the Capotauro substrate-locality precedent)

**Excluded as housekeeping:**
- Tool-call narration ("let me check," "running this command")
- Status confirmations ("got it," "applied successfully")
- Procedural housekeeping (filename clarifications, "where should this file live")
- Verbatim quotations from existing repository files (recoverable from source pointers below)

**Source pointers for excluded verbatim content:**
- Polished sketch sections preserving the derivation work: `flagship_papers/dynamical_substrate_law/sketches/F1_subquestion_pcd_orientation_link.md` §11 (Phase 1), §12 (Phase 2), §13 (Phase 3), §14 (Phase 4), §14.16–§14.17 (Patch 0528 calibration), §14.16 forward (decision-gate re-engagement)
- Numerical verification scripts (machine-precision verified): `flagship_papers/dynamical_substrate_law/code/verify_phase1.py`, `verify_phase3.py`, `verify_phase4.py`
- Decision gate verdict structure: `flagship_papers/chirality_continuum/sketches/F2_F3_viability_decision_gate_2026-05-21.md` §7 (original), §14 (Patch 0529 re-engagement)
- Reviewer package for ChatGPT: `/mnt/user-data/outputs/F1_closure_reviewer_package_for_ChatGPT.md` (assembled between Patches 0527 and 0528)
- ChatGPT review verdict: integrated into Patch 0528 calibration; full reviewer text preserved at user-side
- Programme-state registries: `research_frontier.md`, `future_projects.md` (F.1 entry across Patches 0524–0529)
- Session transcripts: `/mnt/transcripts/2026-05-21-{14-12-46, 14-37-46, 14-58-55, 17-49-48}_*.txt`

---

## §2 Strategy — the trajectory's high-level shape

The F.1 sub-question was identified at Patch 0522 (F.2/F.3 viability decision gate) as the load-bearing question whose closure determines whether F.2 and F.3 (manifestations iv and v of OPEN-SD-CHIR-PRIMITIVE) can proceed at Layer 4 closure via the chirality continuum architectural template. The strategy for closure followed a four-phase scoping established at the F.1 sub-question scoping sketch (Patch 0523):

**Phase 1.** Compute the net DI-bit current at the host vertex under a chirality-bias mechanism primitive (Mechanism A: $r(\hat{e}_{ab}) = r_0(1 + \delta \hat{e}_{ab} \cdot \hat{n})$). Falsifier: if local $I_h$-preservation forces the current to vanish by symmetry-cancellation, Mechanism A fails at Phase 1 and the trajectory pivots to Mechanism B or C.

**Phase 2.** Derive the coupling rule $\vec{j}_{DI}^{net} \mapsto \vec{\omega}_{PCD}$ from the Phase 1 result. Falsifier: if no derivation succeeds without introducing new substrate-physics primitives beyond CPP axioms A1–A11.

**Phase 3.** Derive the substrate-Wigner-Eckart matrix element magnitude $|M^{thermo}|$ under Case A.1 ($\delta = \chi$) or Case A.2 ($\delta$ independent). Falsifier: if neither matches the empirical leptogenesis CP-asymmetry target $\Delta p_{LR}^{obs} \sim 0.04$.

**Phase 4.** Detailed empirical validation against $\Delta p_{LR}^{obs}$ with error analysis, JUNO context, sensitivity to model-dependent assumptions. Falsifier: if more precise observational data falsifies the prediction at ~5σ.

The strategic intuition behind the trajectory: if Mechanism A closes all four phases positively, then (1) Scenario A of the decision gate is confirmed (substrate-mechanism derived); (2) F.2 and F.3 unblock at Layer 4 closure via the chirality continuum template; (3) substrate-locality unification extends from Capotauro's 3-sector closure to 4-sector closure including manifestation (iv). The trajectory's structural ambition was high; the actual closure achievement at Patches 0524–0527 turned out to be more modest than initially framed (per Patch 0528 calibration below).

**Strategic move at Patch 0524 (Phase 1):** the choice to compute the *net DI-bit current* rather than alternative substrate observables. Reasoning: the Capotauro v2.0 substrate-locality framework (Patches 0424–0440) had established that substrate-locality at the host-vertex first-shell icosahedron produces non-trivial geometric facts under Reading C — specifically, $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniformly across all 12 spoke edges and $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$. If Mechanism A is to produce a non-trivial substrate object at the host vertex aligned with $\hat{n}$, the natural construction is to sum the non-reciprocal-propagation contributions over the 12 spoke edges using these geometric facts. The "net DI-bit current" framing operationalizes this by writing $\vec{j}_{DI}^{net} = \sum_i (r_+^i - r_-^i)\hat{u}_i$.

**Strategic move at Patch 0525 (Phase 2):** the choice to address the TI-parity issue via cycle-orientation algebraization rather than alternative parity-repair constructions. Reasoning: once the TI-parity issue surfaced (Phase 1 result is TI-even but the substrate-Wigner-Eckart datum requires TI-odd), three structural options were available — (i) introduce a TI-odd substrate primitive at axiom level (ad hoc, undesirable); (ii) construct a TI-odd substrate object from existing TI-even contents (impossible — products of TI-even contents are TI-even); (iii) recognize that CPP framework already contains TI-odd content latent in axiom A5's cycle-orientation commitment, and algebraize that latent content into a multiplicative pseudoscalar $\sigma_{cycle}$. Option (iii) was chosen as the structurally minimal move. At the time of Patch 0525, I framed this as "structural-consistency argument" with no new primitives introduced; ChatGPT review (between Patches 0527 and 0528) corrected this framing to "parity-repair via cycle-orientation algebraization" with $\sigma_{cycle}$ as "explicitation and algebraization of latent A5 structure" — see Patch 0528 calibration reasoning below.

**Strategic move at Patch 0526 (Phase 3):** the choice to follow the Capotauro v2.0 §20 Wigner-Eckart precedent for the substrate-Wigner-Eckart matrix element computation. Reasoning: Capotauro v2.0 had established for the qDP/eDP sector the matrix element chain $|M| = |\hat{C}_{\text{reduced}}| \cdot d_\Gamma/V_{\text{cage}}$ with three structural inputs — (a) normalized substrate object (directional content), (b) chirality operator's reduced matrix element scaling as substrate chirality magnitude, (c) universal Schur factor at the icosahedral cage. Applying this precedent to manifestation (iv) is the natural template-inheritance move. The Case A.1 vs A.2 choice was framed as a minimal-primitives preference at the time; ChatGPT review correctly identified this as a unification *hypothesis*, not a derivation.

**Strategic move at Patch 0527 (Phase 4):** the choice to frame the empirical observable chain through SF-4 rather than through other potential substrate-to-empirical bridges. Reasoning: the SF-4 neutrino-sector flagship paper had already established (v1.0, Patch 0314) the empirical-observable chain $|M^{thermo}| \to \Delta p_{LR} \to \delta_{CP} \to \varepsilon_1 \to \eta_B$ for the leptogenesis CP-asymmetry target. Using this established chain rather than constructing a new one preserves the framework's empirical-observable coherence.

**Strategic move at Patch 0528 (reviewer-pause checkpoint + calibration):** the choice to pause and assemble a reviewer package after Patch 0527's "FULL CLOSURE" claim rather than proceeding directly to F.2/F.3 substantive content. Reasoning: the trajectory had gone from sketch to "FULL CLOSURE" in one continuation session with no reviewer pushback between phases. Honest self-assessment recognized that the speed of closure was also a structural risk — fast iteration on uninspected foundations. The reviewer-pause checkpoint methodology was an in-trajectory innovation triggered by this self-recognition. ChatGPT's review confirmed the methodological judgment was correct: eight calibration items + one unflagged ansatz emerged.

**Strategic move at Patch 0529 (decision-gate re-engagement):** the choice to update the decision gate's §7.2 verdict structure with calibrated language rather than treating the calibration as internal to the F.1 sub-question scoping sketch. Reasoning: the F.2/F.3 trajectories depend on the decision gate's verdict structure for closure-language inheritance. Were F.2/F.3 substantive content to proceed without decision-gate re-engagement, they would inherit "Scenario A verdict CONFIRMED" language from the pre-calibration state, requiring subsequent retraction. The re-engagement memo functions as a propagation-prevention step.

---

## §3 Phase 1 reasoning (Patch 0524, Finding DSL-1)

### §3.1 The Mechanism A primitive choice

Three candidate mechanisms were considered at the F.1 scoping sketch (Patch 0523 §2):
- **Mechanism A:** DI-bit propagation-rate asymmetry primitive $r(\hat{e}_{ab}) = r_0(1 + \delta \hat{e}_{ab} \cdot \hat{n})$ — non-reciprocal propagation in the direction of $\hat{n}$.
- **Mechanism B:** PCD cycle-phase temporal-lag mechanism — cycle phases acquire $\hat{n}$-dependent timing offsets.
- **Mechanism C:** Hybrid A+B — both propagation rate and cycle timing acquire $\hat{n}$-dependent perturbations.

Mechanism A was selected as the leading candidate at Patch 0523 §3 based on three structural considerations: (1) it is the minimal modification of the substrate's DI-bit propagation structure under the substrate primitive $\hat{n}$; (2) it integrates naturally with the Capotauro substrate-locality framework's host-vertex first-shell icosahedron geometry; (3) the parameter $\delta$ has a natural identification with the Capotauro substrate chirality magnitude $|\chi| = \varphi^{-3}$ under minimal-primitives unification (Case A.1).

**Honest reasoning at the time:** I noted that Mechanism A is *non-reciprocal* at first order in $\delta$ — the outgoing rate from host to neighbor $i$ along direction $\hat{u}_i$ differs from the incoming rate from neighbor $i$ to host along direction $-\hat{u}_i$. This raises a substrate conservation question: where does the per-cycle bit-imbalance go? At the time of Patch 0524, I deferred this question, treating it as an interpretive concern rather than a structural obstacle. The deferred question returned at Patch 0528 calibration (per ChatGPT review §11.11 calibration), where I explicitly characterized the current as a "cycle-mediated informational bias current, not conserved transport" — the per-cycle imbalance is absorbed by the CP's internal SSV-state via the Capture phase.

### §3.2 The DI-bit current derivation

At the host vertex $v_{\text{host}}$ with vertex-aligned $\hat{n} = v_{\text{host}}/|v_{\text{host}}|$:

Outgoing rate from host to neighbor $i$ along $\hat{u}_i$:
$$r_+^i = r_0 \cdot (1 + \delta \cdot \hat{u}_i \cdot \hat{n}) = r_0 \cdot (1 - \delta/(2\phi))$$
uniform across all 12 neighbors by Capotauro v2.0 §13.2 geometric fact (ii) ($\hat{u}_i \cdot \hat{n} = -1/(2\phi)$ uniform).

Incoming rate from neighbor $i$ to host along $-\hat{u}_i$:
$$r_-^i = r_0 \cdot (1 + \delta \cdot (-\hat{u}_i) \cdot \hat{n}) = r_0 \cdot (1 + \delta/(2\phi))$$
also uniform across all 12 neighbors.

Net DI-bit current at the host:
$$\vec{j}_{DI}^{net}(v_{\text{host}}) = \sum_{i=1}^{12} (r_+^i - r_-^i)\,\hat{u}_i = 2 r_0 \delta \sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i$$

**Key reasoning step:** the geometric identity $\sum_i (\hat{u}_i \cdot \hat{n})\hat{u}_i = (3/\varphi^2)\hat{n}$. This follows from pulling the uniform scalar $(\hat{u}_i \cdot \hat{n}) = -1/(2\phi)$ outside the sum and using the Capotauro §13.2 sum identity $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$:

$$\sum_{i=1}^{12} (\hat{u}_i \cdot \hat{n})\,\hat{u}_i = -\frac{1}{2\phi} \sum_{i=1}^{12} \hat{u}_i = -\frac{1}{2\phi} \cdot \left(-\frac{6}{\phi}\right)\hat{n} = \frac{3}{\phi^2}\,\hat{n}$$

Therefore:
$$\boxed{\;\vec{j}_{DI}^{net}(v_{\text{host}}) = \frac{6 r_0 \delta}{\phi^2}\,\hat{n} \; + \; \mathcal{O}(\delta^2)\;}$$

**Verification choice.** I chose to verify the Phase 1 result with an explicit numerical script (`verify_phase1.py`) constructing the 600-cell from first principles (120 vertices on $S^3$ via standard Coxeter construction) and testing the geometric identities at machine precision. Reasoning: a Layer 3 closure should have explicit numerical verification, not just symbolic derivation; the verification provides independent confirmation that the analytic derivation is correct and that the inherited Capotauro v2.0 geometric facts are being applied correctly.

Verification result (machine precision $\leq 4 \times 10^{-16}$): all three identities confirmed across the 12 host-to-first-shell edges. Phase 1 result $\vec{j}_{DI}^{net} = (6r_0\delta/\phi^2)\hat{n}$ tested across five $\delta$ values $\{0, 0.1, \phi^{-3}, 0.5, -0.2\}$, all matching analytic prediction.

### §3.3 The falsifier check

*Phase 1 falsifier:* if local $I_h$-preservation at $v_{\text{host}}$ forces the current to vanish by symmetry-cancellation (analog of K3-face protection where icosahedron edges are tangent in 4D and protected from first-order chirality perturbation).

**Reasoning through the falsifier:** the $I_h$ residual symmetry at $v_{\text{host}}$ preserves the $\hat{n}$ direction (it is the central axis of the first-shell icosahedron). Symmetry-cancellation operates on the *orthogonal-to-$\hat{n}$* components of $\sum_i (\hat{u}_i \cdot \hat{n})\hat{u}_i$; those components DO cancel by $I_h$ centroid-at-center (this is what produces the sum identity $\sum_i \hat{u}_i = -(6/\phi)\hat{n}$ — the orthogonal components cancel, the $\hat{n}$-aligned components accumulate). The $\hat{n}$-aligned component does NOT cancel — it accumulates uniformly across the 12 edges by virtue of the uniform projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$.

**Result: falsifier does NOT activate.** The Phase 1 result is non-zero at first order in $\delta$, aligned with $+\hat{n}$ for $\delta > 0$. This was the trajectory's first positive verdict; without it, Mechanism A would have failed at Phase 1 and the trajectory would have needed to pivot.

### §3.4 The spatial-protection / temporal-coupling complementarity observation

A structural complementarity surfaced during Phase 1 derivation between the two edge classes at the host vertex's first-shell icosahedron:

| Edge class | Count | $\hat{e} \cdot \hat{n}$ | Role |
|---|---|---|---|
| First-shell-to-first-shell (icosahedron edges) | 30 | $0$ (tangent in 4D) | **Spatial K3-base PROTECTED** from direct first-order chirality perturbation (Capotauro §13.3) |
| Host-to-first-shell (spokes) | 12 | $-1/(2\phi)$ (uniform oblique) | **Temporal DI-bit current ENABLED** at first order (this Phase 1 result) |

Both phenomena derive from the *same* host-vertex first-shell icosahedron geometry in 4D, but the two edge classes play structurally opposite roles. This is not a coincidence — the 4D geometry naturally separates "tangent" and "oblique" edge classes via the projection onto $\hat{n}$, and the two classes carry orthogonal physical contents.

**Reasoning about programme-level implications:** ChatGPT review (Patch 0528 calibration context) later identified this complementarity as "**one of the strongest conceptual features of the package**" and "structurally real rather than ad hoc." More importantly, ChatGPT identified this as a possible early hint that the chirality magnitude $|\chi| = \varphi^{-3}$ itself might emerge from geometric imbalance counting (orthogonal-edges 30 vs spoke-edges 12, with the imbalance encoding chirality strength) rather than being postulated as an axiomatic substrate primitive. Registered as the long-term programme target at Patch 0528 §14.17.

### §3.5 Finding DSL-1 registration

**Finding DSL-1 (Layer 3):** Under CPP axioms A1 + Reading C with vertex-aligned $\hat{n} = v_{\text{host}}$ + Mechanism A primitive, the net DI-bit current at the host CP at first order in $\delta$ is $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\phi^2)\hat{n}$, non-zero, aligned with $+\hat{n}$ for $\delta > 0$. Phase 1 falsifier check PASSES negatively (current does not vanish by symmetry-cancellation).

**Calibration applied at Patch 0528 §11.11:** the "net DI-bit current" framing was preserved but clarified as "cycle-mediated informational bias current, not conserved transport" — the per-cycle bit-imbalance is absorbed by the CP's internal SSV-state via the Capture phase, not a violation of substrate-level conservation. This is interpretive calibration, not mathematical change; the result $\vec{j}_{DI}^{net} = (6r_0\delta/\phi^2)\hat{n}$ remains.

---

## §4 Phase 2 reasoning (Patch 0525, Finding DSL-2) — the critical phase

### §4.1 The TI-parity issue surfaces

After Phase 1 produced $\vec{j}_{DI}^{net} = (6r_0\delta/\phi^2)\hat{n}$, my initial reasoning was that the substrate-Wigner-Eckart datum could identify $\vec{\omega}_{PCD} \propto \vec{j}_{DI}^{net}$ directly. The decision gate §2.1 framing of $\vec{\omega}_{PCD}$ as "axial vector / analog of angular momentum" suggested this should work without further structural moves.

**Then I checked the parity transformation properties.** The decision gate §2.3 pairing-convention generator is $\zeta^{thermo} = TI$ (combined time-reversal + spatial inversion); the chirality operator $\hat{C}^{thermo}$ is $\zeta^{thermo}$-ODD; the matter-doublet has $\pm$ chirality eigenvalues under $\zeta^{thermo}$. For the Wigner-Eckart matrix element to be non-zero, $\vec{\omega}_{PCD}$ must be **TI-ODD**.

Phase 1 result $\vec{j}_{DI}^{net}$ transforms as:
- Under T: currents reverse → $\vec{j}_{DI}^{net} \to -\vec{j}_{DI}^{net}$. **T-odd.**
- Under I: polar vectors flip → $\vec{j}_{DI}^{net} \to -\vec{j}_{DI}^{net}$. **I-odd.**
- Combined TI: $\vec{j}_{DI}^{net} \to +\vec{j}_{DI}^{net}$. **TI-EVEN.**

**Direct identification $\vec{\omega}_{PCD} = \vec{j}_{DI}^{net}$ fails on parity grounds.** This was a real structural obstacle — not a notational issue, not a sign-convention issue, a genuine parity mismatch.

**Moment of uncertainty.** At this point in the trajectory, I considered three options:
1. **Abandon Mechanism A.** Pivot to Mechanism B (cycle-phase temporal-lag) or Mechanism C (hybrid). But Mechanism A had just closed Phase 1 positively; abandoning it after one falsifier-survival felt premature.
2. **Reframe the substrate object.** Maybe $\vec{\omega}_{PCD}$ isn't the right substrate object for manifestation (iv); maybe the substrate-Wigner-Eckart datum framing at decision gate §2 was wrong. But §2 inherited from Capotauro v2.0's substrate-locality framework + the chirality continuum architectural template; reframing would propagate structural changes across multiple closed sectors.
3. **Find a TI-odd construction within Mechanism A's content.** Search for a way to produce a TI-odd substrate object from the Phase 1 TI-even result, using only existing framework primitives.

Option (3) was chosen as the structurally least disruptive move. The question became: *what TI-odd content does the framework already contain that could be combined with $\vec{j}_{DI}^{net}$ to produce a TI-odd substrate object?*

### §4.2 The cycle-orientation move

The PCD cycle's temporal direction is universal under CPP axiom A5: every CP executes P → C → D in sequence at every Absolute Moment. **The cycle direction has meaning** — it goes P → C → D forward in time, not D → C → P.

**Under T-reversal, the cycle direction reverses.** The "forward" cycle P → C → D becomes "backward" D → C → P. This is a real transformation property, not a notational issue.

**Under I (spatial inversion), the cycle direction is unaffected.** The cycle is internal to each CP (P, C, D are phases of the CP's internal state evolution); spatial inversion of the CP's external coordinates does not change which phase the CP is in.

So the cycle direction is:
- T-odd (reverses under T).
- I-even (unaffected by I).
- **TI-odd.**

I formalized this as a framework pseudoscalar $\sigma_{cycle}$:
$$\sigma_{cycle} = \begin{cases} +1 & \text{if cycle direction is P → C → D (forward, by global convention)} \\ -1 & \text{if cycle direction is D → C → P (reverse)} \end{cases}$$

with axiom A5 fixing $\sigma_{cycle} = +1$ globally.

**The product structure.** Combining TI-odd $\sigma_{cycle}$ with the appropriately-normalized TI-even $\hat{j}_{DI}^{net}/|\hat{j}_{DI}^{net}|_0$ gives a TI-odd substrate object:
$$\vec{\omega}_{PCD}(v) := \sigma_{cycle} \cdot \hat{j}_{DI}^{net}(v) / |\hat{j}_{DI}^{net}|_0$$

with TI-parity (TI-odd) × (TI-even) = **TI-odd** ✓.

### §4.3 The framing question at Patch 0525

At the time of Patch 0525, I framed this construction as a "structural-consistency argument" with the claim that $\sigma_{cycle}$ is a "CPP framework primitive at axiom A5" — meaning no new structure was introduced beyond what A5 already explicitly contains. The construction's structural status was claimed as "structural-consistency closure (Layer 2.5)" — less explicit-numerical than Phase 1's Layer 3, but using no primitives beyond A1–A11.

I also claimed the product structure was "the unique TI-odd substrate object constructible at the host vertex from CPP axioms A1 + A5 + Reading C + Mechanism A" — the *uniqueness* claim at §12.5 of the sketch.

**Honest reasoning about confidence.** At the time of Patch 0525, I noted that Layer 2.5 status was a step down from Phase 1's Layer 3 closure. The "structural-consistency argument" language was an attempt to communicate the lower rigor while still claiming positive closure. The "uniqueness" claim was made without exhaustive enumeration of alternative TI-odd constructions; the implicit reasoning was "the natural minimal construction is the product, so it's effectively unique."

**Both framings turned out to be overstated under ChatGPT review.** See Patch 0528 calibration reasoning at §6 below for the corrected framings.

### §4.4 The cross-check vs angular momentum

Standard angular momentum $\vec{L} = \vec{r} \times \vec{p}$ has parity:
- T: $\vec{r}$ T-even, $\vec{p}$ T-odd; product T-odd. **T-odd.**
- I: $\vec{r}$ I-odd, $\vec{p}$ I-odd; product I-even. **I-even.**
- Combined TI: T-odd × I-even = **TI-odd.**

The Phase 2 coupling rule's $\vec{\omega}_{PCD}$ has parity:
- T: $\sigma_{cycle}$ T-odd, $\hat{j}_{DI}^{net}$ T-odd; product T-even. **T-even.**
- I: $\sigma_{cycle}$ I-even, $\hat{j}_{DI}^{net}$ I-odd; product I-odd. **I-odd.**
- Combined TI: T-even × I-odd = **TI-odd.**

**Both are TI-odd. But individual T and I parities differ.** Standard $\vec{L}$: T-odd, I-even. Phase 2's $\vec{\omega}_{PCD}$: T-even, I-odd.

This is the structurally important point that I emphasized at Patch 0525: **the Wigner-Eckart matrix element computation is sensitive only to the combined TI-parity** — individual T and I parities can differ from standard $\vec{L}$ without affecting the matrix element. The decision gate §2.1 framing of $\vec{\omega}_{PCD}$ as "axial vector / analog of angular momentum" is suggestive but does not capture the precise substrate-physics structure that Phase 2 surfaces.

### §4.5 The falsifier check

*Phase 2 falsifier:* if no PCD-coupling rule derivation succeeds without introducing new substrate-physics primitives beyond CPP axioms A1–A11.

**Claimed answer at Patch 0525: PASSES.** The derivation uses A1 (DI-bit propagation), A5 (PCD cycle direction → $\sigma_{cycle}$), Mechanism A primitive (previously introduced at Patch 0523 §2.1), Capotauro substrate-locality framework (previously established), and structural-consistency argument for TI-parity matching (claimed: application of framework transformation properties, not a new primitive).

**This claim turned out to be partially overstated under ChatGPT review.** ChatGPT diagnosed that $\sigma_{cycle}$ is an "explicitation and algebraization of latent A5 structure" — A5 commits to ordered cyclicity (P → C → D as oriented temporal sequence), which carries T-asymmetry, but promoting that to a multiplicative TI-odd pseudoscalar with tensor-construction algebraic properties is a stronger move than A5 explicitly contains. The falsifier check is honestly satisfied only with this corrected framing.

### §4.6 Finding DSL-2 registration (with calibrated framing applied)

**Finding DSL-2 (Layer 2.5 parity-repair construction, calibrated framing per Patch 0528):** Under CPP axioms A1–A11 + Reading C + Mechanism A + Phase 1 result, the PCD-cycle-orientation pseudovector is $\vec{\omega}_{PCD}(v) = \sigma_{cycle} \cdot \hat{j}_{DI}^{net}(v)/|\hat{j}_{DI}^{net}|_0$ where $\sigma_{cycle}$ is the cycle's intrinsic TI-odd handedness pseudoscalar (explicitation and algebraization of latent A5 structure) and $|\hat{j}_{DI}^{net}|_0$ is a Phase 3 normalization target. At host vertex with $\delta > 0$: $\vec{\omega}_{PCD}(v_{\text{host}}) = +\hat{n}$. **Construction is the minimal canonical lowest-order TI-odd substrate object** (not formally proven unique); local algebraic representation ansatz applied (substrate object is representable as local algebraic object at host vertex).

---

## §5 Phase 3 reasoning (Patch 0526, Finding DSL-3)

### §5.1 The Wigner-Eckart chain

Following the Capotauro v2.0 §20.5–§20.7 precedent for the qDP/eDP sector closure:
$$|M^{thermo}| = |\hat{C}^{thermo}_{\text{reduced}}| \cdot \frac{d_\Gamma}{V_{\text{cage}}}$$

Three structural inputs to determine:
(a) Normalization $|\hat{j}_{DI}^{net}|_0$ for the substrate object.
(b) Reduced matrix element $|\hat{C}^{thermo}_{\text{reduced}}|$.
(c) Schur factor $d_\Gamma/V_{\text{cage}}$.

### §5.2 The normalization choice

I argued the normalization is uniquely determined by the Capotauro v2.0 §20 precedent: in the qDP/eDP closure, the substrate object was the qCP configuration (Linear-ZBW on $-qCP$ stabilization energy) — a *directional/configurational content*. The substrate's chirality magnitude $|\chi|$ entered through the chirality operator's reduced matrix element, not through the substrate object's magnitude.

Applying this precedent to manifestation (iv):
$$|\hat{j}_{DI}^{net}|_0 \equiv |\vec{j}_{DI}^{net}(v_{\text{host}})| = \frac{6 r_0 \delta}{\phi^2}$$

so that:
$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle} \cdot \hat{n} \quad \text{(unit vector)}$$

The Phase 1 geometric prefactor $6/\phi^2$ is **absorbed by the normalization**.

**Alternative normalizations considered:**
- Option α (ADOPTED): $|\hat{j}_{DI}^{net}|_0 = |\vec{j}_{DI}^{net}|_{\text{host}}$ → unit-vector $\vec{\omega}_{PCD}$.
- Option β: $|\hat{j}_{DI}^{net}|_0 = 6r_0/\phi^2$ → $|\vec{\omega}_{PCD}| = \delta$.
- Option γ: $|\hat{j}_{DI}^{net}|_0 = r_0$ → $|\vec{\omega}_{PCD}| = 6\delta/\phi^2$.

**At Patch 0526 I claimed Option α was uniquely determined by Capotauro precedent.** ChatGPT review correctly pointed out this was overstated — Options β and γ are not nonsense, they correspond to different allocations of magnitude information between state geometry and operator strength. Option α is the **structurally canonical** choice by Capotauro precedent + representation-theoretic cleanliness + prior sector consistency + parameter minimality + avoidance of double-counting chirality magnitude. These are strong reasons, but they constitute a **canonical-choice justification, not a uniqueness theorem**.

The calibrated framing at Patch 0528 §13.16 Calibration 1: "Unit-vector normalization is the minimal canonical choice consistent with the Capotauro substrate-object precedent. Alternative normalizations (Options β, γ) are not formally ruled out; the canonical choice is justified by representation-theoretic cleanliness, prior sector consistency, and avoidance of double-counting."

### §5.3 The reduced matrix element

By direct analog to Capotauro spatial-sector treatment (where $\hat{C}^{qDP}, \hat{C}^{K3}, \hat{C}^{W}$ all have reduced matrix elements $|\chi|$):

$$|\hat{C}^{thermo}_{\text{reduced}}| = |\delta|$$

**Structural argument:** the chirality operator extracts the substrate's chirality content from the matter-doublet states. The substrate's chirality content under Mechanism A is encoded in the propagation-rate-asymmetry parameter $\delta$. Therefore the operator's reduced matrix element scales linearly with $|\delta|$.

This is the cleanest part of Phase 3 — ChatGPT review noted that "once Mechanism A is accepted, $\delta$ is literally the parameter controlling substrate asymmetry strength, so linear scaling of the reduced matrix element with $|\delta|$ is the natural lowest-order expectation." Less problematic than the normalization claim.

### §5.4 The Schur factor

Inherited from Capotauro §20.7 / Finding C-W40 substrate-locality unification:
$$\frac{d_\Gamma}{V_{\text{cage}}} = \frac{2}{12} = \frac{1}{6}$$

Manifestation (iv) is the FOURTH closed sector sharing this universal Schur factor. Together with K3-doublet, W-bracelet, qDP/eDP — all four sectors share the universal $1/6$ at the icosahedral cage.

### §5.5 Matrix element result

$$\boxed{\;|M^{thermo}| = |\delta| \cdot \frac{1}{6} = \frac{|\delta|}{6}\;}$$

### §5.6 The Case A.1 vs A.2 verdict

**Case A.1:** $\delta = \chi = \varphi^{-3}$ unification (substrate primitive's chirality bias manifests with equal magnitude in spatial and temporal sectors). Gives $|M^{thermo}| = \chi/6 \approx 0.0393$ as zero-parameter prediction.

**Case A.2:** $\delta$ independent of $\chi$ (free parameter). Gives $|M^{thermo}| = \delta/6$ with $\delta$ free; empirical match requires $\delta \approx 0.24 \approx \chi$ (ratio 1.0167).

**At Patch 0526 I argued Case A.1 is favored by three criteria:**
1. **Minimal-primitives principle.** Case A.1 keeps the framework zero-parameter; Case A.2 introduces $\delta$ as a second parameter doubling the primitive count.
2. **Zero-parameter empirical prediction.** Case A.1 gives $\chi/6 \approx 0.0394$ matching empirical $\sim 0.04$ to 1.64% without fitting.
3. **Substrate-locality unification consistency.** Case A.1 preserves the Capotauro §20.7 unification at the parameter level.

The framing language at Patch 0526 was "Case A.1 structurally derived" — overstated. ChatGPT review correctly identified Case A.1 as a "unification hypothesis strongly motivated by minimality" rather than a derivation from CPP axioms. The framework shows $\chi$ governs spatial chirality, $\delta$ governs temporal-transport chirality, the two are numerically compatible — but it does NOT show they MUST be identical.

The calibrated framing at Patch 0528 §13.16 Calibration 2: "Case A.1 is the minimal unified realization of substrate primitive chirality bias across spatial and temporal sectors. Derivational identification of $\delta = \chi$ from CPP axioms is not established; Case A.1's selection is motivated by minimal-primitives principle + empirical phenomenological consistency, not by derivation."

### §5.7 Numerical evaluation under Case A.1

- $\phi = 1.618033988749895$
- $\chi = \phi^{-3} = 0.236067977499790$
- $\chi/6 = 0.039344662916632 \approx 0.0393$

**Empirical agreement:**
| Quantity | Value |
|---|---|
| Phase 3 prediction $\chi/6$ | $0.0393$ |
| Empirical central value $\Delta p_{LR}^{obs}$ | $\sim 0.04$ |
| Deviation | $1.64\%$ |
| Conservative empirical range | $[0.035, 0.045]$ |

### §5.8 Cross-check against alternative structural-value candidates

I designed the `verify_phase3.py` script to test alternative structural candidates beyond Case A.1's $\chi/6$. Reasoning: if the framework's parameter space genuinely points to $\chi/6$, then alternative structural readings should NOT match empirical $\sim 0.04$.

| Candidate | Value | Match to $\sim 0.04$? |
|---|---|---|
| $\chi/6 = \phi^{-3}/6$ | $0.0393$ | ✓ **MATCH** |
| $\chi/(6\phi) = \phi^{-4}/6$ | $0.0243$ | ✗ |
| $\chi\phi/6 = \phi^{-2}/6$ | $0.0637$ | ✗ |
| $1/(6\phi^2)$ | $0.0637$ | ✗ |
| $1/(6\phi)$ | $0.1030$ | ✗ |

Only $\chi/6$ matches.

**Reasoning about the cross-check's significance:** ChatGPT review later confirmed that "the strongest point in favor of the match is NOT the raw numerical match but the constrained structural pathway. The framework is not freely curve-fitting; the icosahedral geometry, the Schur factor, and the chirality scale all heavily constrain the outcome. The cross-check ruling out four alternative structural candidates demonstrates that the framework's parameter space genuinely points to $\chi/6$ rather than just happening to land on a number near 0.04." This is the calibrated framing — "nontrivial phenomenological consistency signal" rather than "empirical confirmation."

### §5.9 Finding DSL-3 registration (with calibrated framing applied)

**Finding DSL-3 (Layer 3 mathematical, calibrated framing per Patch 0528):** Under Mechanism A with Case A.1 minimal unified realization ($\delta = \chi = \varphi^{-3}$), the substrate-Wigner-Eckart matrix element for manifestation (iv) is $|M^{thermo}| = \chi/6 \approx 0.0394$. **First zero-parameter empirical prediction from Mechanism A**, matching $\Delta p_{LR}^{obs} \sim 0.04$ at 1.64% deviation as **nontrivial phenomenological consistency signal**. Manifestation (iv) confirmed as FOURTH closed sector sharing universal Schur factor $1/6$ (at viability level, pending Phase 2 foundations work hardening of underlying commitments).

---

## §6 Phase 4 reasoning (Patch 0527, Finding DSL-4)

### §6.1 The empirical observable chain

The substrate-level $\Delta p_{LR}^{obs}$ observable is the empirical counterpart to $|M^{thermo}|$, extracted through the SF-4 neutrino-sector flagship paper's empirical-observable chain:

| Level | Observable |
|---|---|
| Substrate | $\|M^{thermo}\|$ — substrate-W-E matrix element (Phase 3 prediction) |
| Substrate | $\Delta p_{LR}^{obs}$ — substrate-level temporal asymmetry |
| Flavor sector | $\delta_{CP}$ — PMNS phase |
| Flavor sector | $\varepsilon_1$ — leptogenesis CP-asymmetry parameter |
| Cosmological | $\eta_B$ — baryon-to-photon ratio |

The mapping at each level involves flavor-mixing factors and seesaw-scale considerations specific to the SF-4 framework.

### §6.2 Current observational precision

Combined observational precision for substrate-level $\Delta p_{LR}^{obs}$ from current data: **~12% at central value ~0.04** → conservative range $[0.035, 0.045]$.

Phase 3 prediction $\chi/6 \approx 0.0393$ deviates from central by **1.64%, 0.14σ-equivalent** — far below 5σ falsification threshold (factor ~36 below).

### §6.3 Sensitivity to model-dependent assumptions

Three categories of variations in observational extraction:
1. Leptogenesis scenario (thermal vs resonant): ~factor 2.
2. Seesaw mass scale (high vs low): ~factor 1.5.
3. Flavor structure variations: ~factor 1.3.

**Combined expanded range:** $[0.027, 0.060]$. Phase 3 prediction within expanded range. ✓

### §6.4 JUNO neutrino-sector update context

JUNO expected precision improvements:
- $\theta_{12}$ to ~0.5%, $\Delta m^2_{21}$ to ~0.3%, $\Delta m^2_{31}$ to ~0.2%.
- Substrate-level $\Delta p_{LR}^{obs}$ precision: from current ~12% to ~5–8% post-JUNO peer-review.

**Discrimination capability:** discrimination from closest alternative $\chi/(6\phi) \approx 0.024$ requires ~18.8% precision. JUNO at ~6.5% is sufficient.

At Patch 0527 I framed this as "JUNO sufficient to discriminate Phase 3 prediction from alternatives." ChatGPT review correctly pointed out that the JUNO precision propagation from direct measurements through the SF-4 chain to substrate-level $\Delta p_{LR}^{obs}$ precision involves significant model-dependent assumptions not yet rigorously tested. The calibrated framing at Patch 0528 §14.16 Calibration 2: "JUNO-era constraints may become sufficient to discriminate Phase 3 prediction from alternative structural candidates, depending on the stability of the observable mapping from JUNO's direct measurements through the SF-4 empirical chain to substrate-level $\Delta p_{LR}^{obs}$."

### §6.5 Cross-checks with related observables

- Cosmological $\eta_B \sim 6.1 \times 10^{-10}$ (Planck CMB, tight): consistent with current $\Delta p_{LR}^{obs}$.
- PMNS $|\sin\delta_{CP}| \sim 0.6$–$0.8$ from T2K+NOvA: consistent.
- $m_{\beta\beta}$ upper limits from KamLAND-Zen: consistent.

### §6.6 Falsifiability conditions

- 5σ direct falsification: $\Delta p_{LR}^{obs}$ outside $[0.016, 0.064]$.
- Discrimination falsification: JUNO data giving $\sim 0.024 \pm 0.003$ (consistent with closest alternative $\chi/(6\phi)$).
- Cross-observable tension falsification.

Current observational state does NOT approach any of these.

### §6.7 Finding DSL-4 registration (with calibrated framing applied)

**Finding DSL-4 (Layer 2.5/3 hybrid, calibrated framing per Patch 0528):** Phase 3 prediction $\chi/6 \approx 0.0394$ matches empirical $\Delta p_{LR}^{obs} \sim 0.04$ at 1.64% deviation, 0.14σ-equivalent, within conservative + model-dependent expanded ranges, consistent with cross-observables, not falsified at 5σ. JUNO peer-review update is future stress test. Verdict: **viability-level consistency-and-falsifiability check** (calibrated from "CONDITIONAL PASS" Patch 0527 framing). JUNO discrimination claim: "may become sufficient depending on observable mapping stability" (calibrated).

---

## §7 Reviewer-pause checkpoint reasoning (between Patches 0527 and 0528)

### §7.1 The moment of self-recognition

After Patch 0527 declared "F.1 SUB-QUESTION FULL CLOSURE UNDER SCENARIO A," Thomas asked: *"Was this trajectory really worth the work? Are these four substantive findings real, or did you build them too fast for your own good?"*

This was an important moment. My immediate honest response: the trajectory had gone from sketch to "FULL CLOSURE" in one continuation session with no reviewer pushback between phases. The empirical agreement at 1.64% was real, the cross-check was real, the substrate-locality unification was real — but the *speed* of closure was also a structural risk. I was building fast on uninspected foundations.

**The honest self-assessment:** "Phase 1 and Phase 3 are Layer 3 with explicit numerical verification. Phase 2 is Layer 2.5 (structural-consistency argument). Phase 4 is Layer 2.5/3 hybrid (CONDITIONAL PASS verdict). The 'FULL CLOSURE' framing slightly papers over that Phase 2's rigor is genuinely a step down from Phase 1's."

**The structural concern:** the trajectory's claims propagate into downstream sectors (F.2, F.3, flagship paper assembly, decision-gate verdict). Without reviewer scrutiny BEFORE downstream propagation, any structural weakness would compound across the closure cascade.

### §7.2 The reviewer package assembly

Thomas requested the reviewer package for ChatGPT. I produced a 515-line reviewer package at `/mnt/user-data/outputs/F1_closure_reviewer_package_for_ChatGPT.md` containing:

1. **Reviewer brief** with explicit confidence ranking and acknowledgment of trajectory speed risk.
2. **Background context** (load-bearing inputs): CPP axioms A1, A5; Reading C; Capotauro substrate-locality framework + §13.2 geometric facts + §20.7 Schur factor universality; Mechanism A primitive specification; decision gate §2 Wigner-Eckart datum framing.
3. **The four phases** with extracted substantive content from sketch §11–§14.
4. **Programme implications claimed** (5 items, all flagged as conditional on trajectory holding up under scrutiny).
5. **22 stress-test questions** organized by phase + programme-level, pointed at where I had lower confidence.
6. **Closing note from Claude (author of patches)** with explicit confidence ranking by phase and request for hard pushback.

The closing note is particularly important: it signaled to the reviewer that I wanted hard pushback, not validation. "Please pushback hard on anything that looks structurally weak. The trajectory's value depends on reviewer scrutiny that hasn't happened yet."

### §7.3 ChatGPT's review verdict

Thomas pasted the package to ChatGPT and received a pointed review. Key diagnoses:

**(1) Phase 2 should be framed as "parity-repair via cycle-orientation algebraization" rather than "structural-consistency argument."** ChatGPT's descriptive characterization of the operational structure: derive TI-even → observe target must be TI-odd → introduce TI-odd pseudoscalar → multiply → declare canonical. This is parity repair — a structurally motivated completion move — rather than a uniqueness theorem derived from first principles. My "structural-consistency argument" framing was defensive language; ChatGPT's "parity-repair" framing is descriptive.

**(2) Phase 2 contains an unflagged LOCAL ALGEBRAIC REPRESENTATION ANSATZ.** I had missed this entirely. Phase 2 quietly assumes the thermodynamic chirality observable can be represented as a LOCAL ALGEBRAIC OBJECT at the host vertex. It could instead emerge from cycle-history accumulation, nonlocal transport asymmetry, or coarse-grained update statistics. That's an unflagged ansatz, and ChatGPT caught it where I didn't. This is the **largest open question** of the trajectory.

**(3) $\sigma_{cycle}$ is "explicitation and algebraization of latent A5 structure" rather than "covered by axiom A5."** ChatGPT's wording for what $\sigma_{cycle}$ is — weaker than "no new primitives," stronger than "ad hoc." Axiom A5 commits to ordered cyclicity (P → C → D), which carries T-asymmetry. But promoting that into a multiplicative TI-odd pseudoscalar available for tensor construction is an algebraic move beyond what A5 explicitly contains. Defensible — but should be labeled as algebraization, not pure recovery.

**The pattern across all three:** where I had defensive framing ("structural-consistency," "uniqueness," "no new primitives," "FULL CLOSURE"), ChatGPT substituted accurate operational descriptions. The mathematics doesn't change; the epistemic claims do.

**ChatGPT's verdict on "FULL CLOSURE":** Not in the strongest sense. The current package supports Scenario A viability, Scenario A coherence, Scenario A phenomenological plausibility, and a candidate derivational pathway. But Phase 2 remains partly interpretive. The honest framing is something like: *"Scenario A provisionally closed at the viability level pending stronger derivational closure of the TI-odd coupling structure and future empirical discrimination."*

**ChatGPT's most important programme-level observation:** "The strongest revision you could make is not adding more mathematics. It is tightening epistemic discipline." This is the critical methodological reframing for the trajectory.

**ChatGPT's validation of Thomas's "emergent chirality" intuition:** "the F.1 work points toward 'chirality manifestations across distinct sectors appear to descend from geometric asymmetry relations of the 600-cell substrate rather than from independent phenomenological primitives.' That is a real structural pattern. However, the framework still currently inserts $\hat{n}$ and $|\chi| = \phi^{-3}$ axiomatically. So chirality is not yet emergent in the strong sense. The genuinely major future programme target would be: derive the chirality scale itself from pure polytope geometry and locality constraints."

This was a significant validation of the long-term programme direction. Registered at Patch 0528 §14.17 as the long-term programme target (deferred behind Phase 2 foundations work + F.1/F.2/F.3 stabilization).

---

## §8 Patch 0528 calibration reasoning

### §8.1 The calibration philosophy

The mathematics of Patches 0524–0527 didn't change. What changed was the **epistemic claims attached** to the mathematics. ChatGPT's diagnosis was clear: the strongest revision is not adding more mathematics but tightening epistemic discipline. So Patch 0528 was a *language calibration patch*, not a mathematical patch.

**Method:** preserve all derivation content (Findings DSL-1 through DSL-4 remain registered at their original Layer statuses), apply calibration *subsections* to each phase that explicitly reframe the epistemic claims. The structure was additive — calibration content was appended to each phase (§11.11, §12.13, §13.16, §14.16, §14.17) rather than rewriting the original sections — to preserve the historical record of what was originally claimed.

### §8.2 The eight calibrations applied

**Calibration 1 (Phase 1, §11.11):** "Net DI-bit current" → "cycle-mediated informational bias current, not conserved transport." Clarifies the physical interpretation of the non-reciprocal propagation rule: per-cycle bit-imbalance is absorbed by the CP's internal SSV-state via Capture phase, not a violation of substrate-level conservation.

**Calibration 2 (Phase 2, §12.13 Cal. 1):** "Structural-consistency argument" → "parity-repair via cycle-orientation algebraization." Descriptive characterization of the operational structure.

**Calibration 3 (Phase 2, §12.13 Cal. 2):** "$\sigma_{cycle}$ as CPP framework primitive at axiom A5" → "explicitation and algebraization of latent A5 structure." A5 commits to ordered cyclicity carrying T-asymmetry; promoting that to multiplicative TI-odd pseudoscalar with tensor-construction properties is stronger than A5 explicitly contains.

**Calibration 4 (Phase 2, §12.13 Cal. 3):** "Unique TI-odd construction" → "minimal canonical lowest-order TI-odd construction." Uniqueness not proven; possible alternatives (higher-order cycle-correlation objects, local circulation tensors, bivector constructions, pseudoscalar contractions involving temporal update ordering) likely reduce to same lowest-order direction but reduction unproven.

**Calibration 5 (Phase 2, §12.13 Cal. 4, LARGEST OPEN QUESTION):** **Local algebraic representation ansatz flagged.** Phase 2 assumes the thermodynamic chirality observable is representable as a local algebraic object at host vertex; could instead emerge from cycle-history accumulation, nonlocal transport asymmetry, or coarse-grained update statistics. This ansatz was unflagged in Patches 0524–0527; flagging it explicitly is the largest single calibration of the patch.

**Calibration 6 (Phase 3, §13.16 Cal. 1):** "Uniquely structurally consistent" unit-vector normalization → "minimal canonical choice." Options β and γ not formally ruled out; canonical choice justified by representation-theoretic cleanliness + prior sector consistency + parameter minimality + avoidance of double-counting; not uniqueness theorem.

**Calibration 7 (Phase 3, §13.16 Cal. 2):** Case A.1 "structurally derived" → "minimal unified realization." Derivational identification of $\delta = \chi$ from CPP axioms not established; Case A.1 selection motivated by minimal-primitives principle + empirical phenomenological consistency, not by derivation.

**Calibration 8 (Phase 3+4, §13.16 Cal. 3, §14.16 Cal. 1):** 1.64% "empirical agreement / confirmation" → "nontrivial phenomenological consistency signal." Observable chain through SF-4 is indirect with model-dependence at each level; constrained structural pathway makes match nontrivial but uncertainty budget not rigorously propagated; not high-confidence empirical confirmation.

Plus Phase 4 JUNO discrimination claim "sufficient" → "may become sufficient depending on observable mapping stability" (§14.16 Cal. 2).

### §8.3 The §14.17 status reframing

The most consequential framing change at Patch 0528: F.1 sub-question status from "FULL CLOSURE under Scenario A" (Patch 0527 §14.11) to **"PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work"** (Patch 0528 §14.17). Scenario A status reframed from "verdict CONFIRMED" to **"structurally VIABLE + phenomenologically CONSISTENT at viability level, derivationally PROVISIONAL."**

Three open structural commitments registered (§14.17 table):
- (B.1) Local algebraic representation ansatz (largest open question, Phase 2).
- (B.2) $\sigma_{cycle}$ algebraization rigor + uniqueness of TI-odd construction (Phase 2).
- (B.3) Case A.1 derivational support (Phase 3).

These three commitments together constitute the **real structural bottleneck** of the F.1 trajectory.

### §8.4 The long-term programme target registration

Patch 0528 §14.17 also registered the long-term programme target identified by ChatGPT review: **derive the chirality scale $|\chi| = \varphi^{-3}$ itself from pure 600-cell polytope geometry and locality constraints**, with no chirality input. This would be substantially deeper than the F.1 closure (which still inserts $\hat{n}$ and $|\chi|$ axiomatically) and represents a major future programme ambition.

The Phase 1 spatial-protection / temporal-coupling complementarity (§11.10) is identified as an early hint that chirality magnitude might emerge from geometric imbalance counting rather than being postulated. This avenue is registered as a long-term programme target but is deferred until F.1 / F.2 / F.3 are structurally stable.

---

## §9 Patch 0529 decision-gate re-engagement reasoning

### §9.1 The propagation-prevention logic

Why re-engage the decision gate immediately after calibration? Because the F.2/F.3 trajectories depend on the decision gate's §7.2 verdict structure for closure-language inheritance. If F.2 substantive content were to proceed at the post-calibration state without decision-gate re-engagement, F.2 would inherit "Scenario A verdict CONFIRMED" language from the pre-calibration §7.2, requiring subsequent retraction once the inheritance was noticed.

The cost of decision-gate re-engagement (1 patch, ~200 lines) is far less than the cost of unwinding F.2/F.3 substantive content built on uninspected foundations.

### §9.2 The §7.2 verdict structure update

The original §7.2 framed three scenarios (A: substrate-mechanism derived, B: independent primitive, C: partial). With Patch 0528 calibration applied:

**Scenario A — STATUS: PROVISIONAL ACTIVE.** Mechanism A supplies a plausible derivational pathway, structurally VIABLE + phenomenologically CONSISTENT at 1.64% agreement, derivationally PROVISIONAL with three open structural commitments. F.2/F.3 closure machinery is structurally compatible with Phase 2 coupling rule **subject to Phase 2 foundations work** hardening B.1–B.3; F.2/F.3 substantive content trajectories are **DEFERRED at decision-gate level** until those commitments are addressed.

**Scenario B — STATUS: NOT CURRENTLY ACTIVE.** Mechanism A viability trajectory has not failed; no falsifier across Phases 1–4 has activated. Pivot not warranted at current trajectory state. Remains available as fallback if Phase 2 foundations work falsifies the local algebraic representation ansatz (commitment B.1) or demonstrates no Mechanism A variant can produce the required TI-odd construction.

**Scenario C — STATUS: NOT CURRENTLY ACTIVE.** F.1 sub-question scoping focused on manifestation (iv) under Mechanism A; manifestation (v) has not been substantively engaged. Scenario C's partial-derivation framing not currently motivated by data. Remains available if Phase 2 foundations work succeeds for manifestation (iv) but fails to extend to manifestation (v), or vice versa.

### §9.3 The reviewer-pause checkpoint precedent registration

Patch 0529 §14.8 registered a **methodological precedent** for future programme work: substantive multi-phase closure trajectories should incorporate reviewer-pause checkpoints between phases or at trajectory completion BEFORE downstream work begins inheriting closure-claim language.

The Patches 0524–0528 trajectory establishes this precedent in practice:
1. *Substantive multi-phase work* (Patches 0524–0527) — four phases in one continuation session producing claimed "FULL CLOSURE."
2. *Reviewer-pause checkpoint* (between Patches 0527 and 0528) — reviewer package assembly + ChatGPT engagement + identification of overclaim language + unflagged ansatz.
3. *Calibration patch* (Patch 0528) — applied calibrations + downgrade to PROVISIONAL CLOSURE.
4. *Decision-gate re-engagement* (this Patch 0529) — updated decision-gate-level verdict structure with calibrated language.

The reviewer-pause checkpoint between Patches 0527 and 0528 prevented overclaim cascade into downstream F.2/F.3 work. Without it, F.2 substantive content drafting would have inherited "Scenario A verdict CONFIRMED" language requiring subsequent retraction.

**Methodological lesson:** reviewer-pause checkpoints have low cost (1 reviewer-package assembly + 1 calibration patch) and high value (prevent overclaim cascade into downstream sectors). The precedent applies particularly to trajectories where closure language would propagate into multiple downstream sectors.

---

## §10 Findings registered (consolidated with calibrated status)

| Finding | Phase | Patch | Layer | Calibrated framing |
|---|---|---|---|---|
| DSL-1 | 1 | 0524 | 3 (numerical) | Cycle-mediated informational bias current $\vec{j}_{DI}^{net}(v_{\text{host}}) = (6 r_0 \delta/\varphi^2)\hat{n}$; not conserved transport |
| DSL-2 | 2 | 0525 | 2.5 (parity-repair) | $\vec{\omega}_{PCD} = \sigma_{cycle} \cdot \hat{j}_{DI}^{net}/\|\hat{j}_{DI}^{net}\|_0$; minimal canonical lowest-order TI-odd construction under local algebraic representation ansatz; $\sigma_{cycle}$ as explicitation of latent A5 structure |
| DSL-3 | 3 | 0526 | 3 (mathematical) | $\|M^{thermo}\| = \|\delta\|/6$; under Case A.1 minimal unified realization gives $\chi/6 \approx 0.0394$; canonical (not uniquely forced) normalization |
| DSL-4 | 4 | 0527 | 2.5/3 (viability) | Phenomenological consistency signal at 1.64% deviation; viability-level consistency-and-falsifiability check; not high-confidence empirical validation |

**All four findings remain registered at calibrated framing.** No retraction at Patch 0528 or Patch 0529.

---

## §11 Verdict at Session 138 close

**F.1 sub-question status:** PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work.

**Scenario A status:** structurally VIABLE + phenomenologically CONSISTENT at viability level, derivationally PROVISIONAL.

**Scenario B / Scenario C status:** NOT CURRENTLY ACTIVE.

**Three open structural commitments registered as real bottleneck:**
- (B.1) Local algebraic representation ansatz justification — largest open question.
- (B.2) $\sigma_{cycle}$ algebraization rigor + uniqueness of TI-odd construction.
- (B.3) Case A.1 derivational support from CPP axioms.

**Long-term programme target registered (deferred):** derive chirality scale $|\chi| = \varphi^{-3}$ from pure 600-cell polytope geometry and locality constraints.

**Methodological precedent established:** reviewer-pause checkpoint methodology for substantive multi-phase closure trajectories.

---

## §12 State at session close

**Programme state advancement:**
- F.1 sub-question identified as load-bearing for decision gate (Patch 0522, Session 138 opening) → F.1 sub-question PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work, decision-gate re-engaged with calibrated status, F.2/F.3 DEFERRED at decision-gate level (Patch 0529, this session close).

**Patch trajectory:** 7 patches across Session 138 continuation arc (Patches 0522 → 0523 → 0524 → 0525 → 0526 → 0527 → 0528 → 0529, plus this Patch 0530 handover).

**Findings registered:** 4 (DSL-1, DSL-2, DSL-3, DSL-4) at calibrated Layer statuses.

**No new axioms introduced.** Mechanism A primitive (and the calibrated framing of $\sigma_{cycle}$ as explicitation of latent A5 structure) remain within CPP axiomatic framework A1–A11.

**No modifications to v1.0 SHIPPED paper sources:** Chirality Continuum v1.0, Capotauro v2.0 v1.0, SF-2 v1.0, SM-2 v1.0, SF-4 v4.4 all .tex frozen.

**Documentation suite assets created at Patch 0530 (this handover):**
- `flagship_papers/dynamical_substrate_law/documentation_suite/` directory created.
- `reasoning-dynamical-substrate-law.md` (this file) — Tier 4 verbatim Opus reasoning narrative.
- `handovers/2026-05-21_session_138_F1_sub_question_provisional_closure.md` — Step H paste-ready handover document at canonical location.

---

## §13 Forward-looking pointers — Phase 2 foundations work (B.1, B.2, B.3)

**Phase 2 foundations work is the immediate next substantive priority** when work resumes. Three sub-targets with estimated effort:

### §13.1 (B.1) Local algebraic representation ansatz justification — LARGEST OPEN QUESTION

**Target:** demonstrate that the thermodynamic chirality observable IS representable as a local algebraic object at the host vertex, OR re-derive Phase 2 under a nonlocal/coarse-grained representation and show consistency with the Wigner-Eckart datum.

**Approach options:**
1. **Justify locality.** Show from CPP framework principles (axioms A1–A11 + Reading C + Capotauro substrate-locality framework) that the substrate's chirality content localizes at the host vertex via the icosahedral cage structure. Argument structure: the substrate-locality theorem (Capotauro Finding C-W39) supports that chirality content localizes geometrically at the first-shell icosahedron; extending this localization to the temporal sector (Mechanism A) is the missing piece.
2. **Re-derive under nonlocality.** If localization can't be justified, re-derive Phase 2 under one of the alternative representations: cycle-history accumulation (chirality content builds up over many Absolute Moments), nonlocal transport asymmetry (chirality content distributes across substrate connectivity graph), or coarse-grained update statistics (chirality content emerges only at scales above individual CP cycles).
3. **Show alternative representations give same lowest-order result.** Demonstrate that the local algebraic representation and the alternatives all reduce to the same Phase 2 coupling rule at lowest order in $\delta$, making the ansatz a representational choice rather than a structural commitment.

**Estimated effort:** 2–6 sessions of sketch-level structural exploration. Output: sketch-level (not flagship-paper-level) until ansatz is examined.

### §13.2 (B.2) $\sigma_{cycle}$ algebraization rigor + uniqueness of TI-odd construction

**Target:** justify the algebraic move from A5's ordered cyclicity to multiplicative TI-odd pseudoscalar with tensor-construction properties; rule out alternative TI-odd constructions.

**Approach options:**
1. **Strengthen $\sigma_{cycle}$ derivation.** Show from A5's content (ordered cyclicity, T-asymmetry of cycle direction) that the algebraization to a multiplicative TI-odd pseudoscalar is the structurally minimal move; demonstrate that any framework consistent with A5 contains $\sigma_{cycle}$ at the algebraic level.
2. **Enumerate and rule out alternatives.** Identify the space of possible TI-odd substrate objects constructible from CPP framework content (higher-order cycle-correlation objects, local circulation tensors, bivector constructions, pseudoscalar contractions involving temporal update ordering); show that they all reduce to the Phase 2 product at lowest order in $\delta$, OR identify a structurally inequivalent alternative.

**Estimated effort:** 2–5 sessions of sketch-level structural exploration.

### §13.3 (B.3) Case A.1 derivational support

**Target:** derive $\delta = \chi$ identification from CPP axioms rather than minimal-primitives preference.

**Approach options:**
1. **Single-primitive structural argument.** Show from CPP framework that the substrate primitive's chirality bias is necessarily characterized by a single magnitude $|\chi|$ at the axiomatic level; both Capotauro's spatial-sector $\chi$ and Mechanism A's temporal-sector $\delta$ are different manifestations of this single primitive content; therefore $|\delta| = |\chi|$.
2. **Symmetry-based derivation.** Show that spatial-sector and temporal-sector chirality bias magnitudes must be equal by a framework symmetry argument (e.g., a substrate-level analog of CPT symmetry forcing parity-related magnitudes to be equal).
3. **Geometric derivation from polytope.** Long-term: derive $|\chi| = \varphi^{-3}$ from 600-cell geometry directly (the long-term programme target); in this case $|\delta| = |\chi|$ would emerge from the same geometric source.

**Estimated effort:** 1–4 sessions for options 1–2; option 3 connects to the long-term programme target and is multi-session-arc-scale.

### §13.4 Aggregate estimate

**Total Phase 2 foundations work:** 5–15 sessions of structural exploration, output sketch-level rather than flagship-paper-level until the local algebraic representation ansatz is examined. Success criteria: B.1–B.3 hardened to derivational status, F.1 sub-question status upgraded from PROVISIONAL CLOSURE at viability level to derivational closure.

**Anti-pattern to avoid:** F.1 flagship paper assembly BEFORE Phase 2 foundations work substantively progresses on B.1–B.3. Premature paper assembly would propagate calibrated overclaim language into a published artifact, requiring subsequent retraction.

---

## §14 Long-term programme target (deferred behind Phase 2 + F.1/F.2/F.3 stabilization)

**Goal:** derive the chirality scale $|\chi| = \varphi^{-3}$ from pure 600-cell polytope geometry and locality constraints, with no chirality input at the axiomatic level.

**Current framework state:** $\hat{n}$ and $|\chi|$ are inserted at the axiomatic level (Reading C + Capotauro v2.0 substrate primitive specification). The F.1 work (this trajectory) shows the temporal-sector manifestation of chirality ($\vec{\omega}_{PCD}$) is unified with the spatial-sector substrate primitive via Mechanism A, but the substrate's chirality magnitude $|\chi| = \varphi^{-3}$ and directional content $\hat{n}$ remain axiomatic.

**Conceptual signal pointing toward emergence:** The Phase 1 spatial-protection / temporal-coupling complementarity (sketch §11.10) — orthogonal-edges 30 vs spoke-edges 12 at the host-vertex first-shell icosahedron, with the imbalance encoding chirality-related content — may be an early hint that chirality magnitude could emerge from geometric imbalance counting rather than being postulated.

**ChatGPT review observation (preserved verbatim from review verdict):** "Chirality manifestations across distinct sectors appear to descend from geometric asymmetry relations of the 600-cell substrate rather than from independent phenomenological primitives. That is a real structural pattern. However, the framework still currently inserts $\hat{n}$ and $|\chi| = \phi^{-3}$ axiomatically. So chirality is not yet emergent in the strong sense. The genuinely major future programme target would be: derive the chirality scale itself from pure polytope geometry and locality constraints."

**Programme-level significance if achieved:** Would be substantially deeper than the F.1 closure (which still inserts $\hat{n}$ and $|\chi|$ axiomatically). The chirality scale's emergence from polytope geometry would close a foundational gap in the framework — extending CPP's "zero-parameter" character to include the chirality scale itself rather than treating it as a substrate primitive.

**Deferred behind:** (i) Phase 2 foundations work (B.1, B.2, B.3); (ii) F.1 flagship paper assembly with calibrated language; (iii) F.2 substantive content trajectory; (iv) F.3 substantive content trajectory. Multi-session-arc-scale ambition; not in current forward queue.

---

## §15 Methodological precedent — reviewer-pause checkpoint discipline

The Patches 0524–0528 trajectory establishes a methodological precedent for future Layer 4 closure trajectories:

**Trigger:** substantive multi-phase closure work where the closure language would propagate into multiple downstream sectors.

**Mechanism:** between substantive multi-phase work (closure trajectory) and downstream propagation (F.X+1 substantive content, flagship paper assembly, decision-gate verdict update), insert a reviewer-pause checkpoint:
1. Self-assessment of trajectory: where rigor is high, where rigor is lower, where claims are overstated.
2. Reviewer package assembly: structured stress-test brief with explicit confidence ranking + targeted questions.
3. External review engagement: pause for reviewer scrutiny BEFORE downstream propagation.
4. Calibration patch: apply reviewer-identified calibrations without retracting mathematical content.
5. Downstream re-engagement: update decision-gate-level / programme-level state with calibrated language.

**Cost:** ~1 reviewer-package assembly + ~1 calibration patch + ~1 downstream re-engagement patch (3 patches total for full reviewer-pause cycle).

**Value:** prevents overclaim cascade into downstream sectors; trajectories where this would have produced an inheritance cost of 5–15+ sessions of retraction work are protected.

**Applicability:** any closure trajectory where the closure status would propagate into multiple downstream documents/sectors. Most acutely needed for trajectories that close in one continuation session without external review between phases.

**Anti-pattern to avoid:** treating the reviewer-pause checkpoint as optional when downstream propagation is imminent. The cost of the checkpoint is low; the cost of NOT doing it scales with how far downstream the overclaim propagates before being noticed.

---

*This Tier 4 reasoning narrative records the substantive Opus physics reasoning across the F.1 sub-question closure trajectory at Session 138 continuation (Patches 0522–0529, plus this Patch 0530 handover). The trajectory's mathematics is preserved in the sketch §11–§14 polished content; this file preserves the reasoning behind that content — the alternatives considered, the framings revised, the moments of uncertainty, the engagement with reviewer pushback. Append-only across future sessions per Four-Tier Documentation Discipline; future F.1 work (Phase 2 foundations work on B.1, B.2, B.3) will append new Tier 4 reasoning entries below this initial baseline.*

*The canonical record of the F.1 closure trajectory's substantive physics lives here. Tier 3 development vignettes (curated narrative summaries), Tier 2 transcript pointer-maps (transaction-indexed roadmap), and Tier 1 session-log entries derive from this Tier 4 source.*

---

## §16 Session 139 / Patch 0531 — Phase 2 foundations work opening reasoning

*This section captures the substantive physics reasoning behind the Patch 0531 sketch `F1_phase2_foundations_work.md`. The session opened Phase 2 foundations work registered at Patch 0528 §14.17 as the real structural bottleneck of the F.1 sub-question closure trajectory.*

### §16.1 The framing decision — which commitment first

The Patch 0528 §14.17 + handover §13 register three open structural commitments: B.1 (local algebraic representation ansatz), B.2 ($\sigma_{cycle}$ algebraization + uniqueness), B.3 (Case A.1 derivational support). Per the handover §13.1, B.1 is the LARGEST OPEN QUESTION; per §13.2, B.2 is mid-tier; per §13.3, B.3 is most tractable in the short term but option (iii) connects to the long-term programme target.

The reasoning to focus the bulk of substantive work on B.1: if B.1 fails (the local algebraic representation cannot be justified), then Phase 2's coupling rule needs to be re-derived under nonlocal/coarse-grained representation, which would propagate to B.2 (the uniqueness question would shift to whichever new representation) and B.3 (the Case A.1 hypothesis is interpreted within whichever representation). So B.1 is structurally load-bearing for the other two. Working it first concentrates the foundation-laying effort.

Within B.1, the further decision was to focus on substantive structural exploration (not closure attempts). The handover §10.4 lesson ("fast multi-phase closure on uninspected foundations") explicitly warned against the Patches 0524–0527 pattern; an opening session producing closures would repeat that anti-pattern. The deliberate scope was: explore B.1 deeply enough to identify what would close it without claiming to close it.

### §16.2 The three-layer disambiguation — the surprise of this session

The most substantive structural move in this session was the §2.2 three-layer disambiguation (substrate per-cycle / substrate matrix element / observable cosmological). This emerged from working through what specifically ChatGPT's "cycle-history accumulation," "nonlocal transport asymmetry," and "coarse-grained update statistics" alternatives WOULD MEAN at the substrate-matrix-element layer.

**Initial reading.** My first pass on the alternatives was to take them at face value: $\vec{\omega}_{PCD}$ at vertex $v$ might depend on history, nonlocal transport, or statistics, each making the local algebraic form $\vec{\omega}_{PCD}(v) = f(\hat{j}^{net}(v), \sigma_{cycle})$ inadequate.

**Tension surfaced.** When I tried to write down what cycle-history accumulation would mean for the SUBSTRATE-MATRIX-ELEMENT computation, I noticed it didn't fit. The Wigner-Eckart matrix element is per-event, per-AM. Accumulation over time is exactly what Phase 4's chain ($|M^{thermo}| \to \Delta p_{LR}^{obs} \to \delta_{CP} \to \varepsilon_1 \to \eta_B$) handles. So "cycle-history accumulation at the substrate-matrix-element layer" felt like a category error.

**Resolution.** ChatGPT's alternatives could be read either as:
- Concerns at the substrate-matrix-element layer (where the local algebraic representation question genuinely lives), OR
- Concerns at the observable-cosmological layer (where accumulation/statistics naturally enter via Phase 4's chain).

The disambiguation in §2.2 is my best attempt to clarify what B.1 actually asks. It locates the meaningful B.1 question at the substrate-matrix-element layer and explains why the listed alternatives, taken at face value, don't naturally sit there.

**Caveat I added at §2.2.** The disambiguation itself is sketch-level — I might be drawing a line where ChatGPT didn't draw one, or I might be missing a way to interpret ChatGPT's concerns that actually does locate them at the substrate-matrix-element layer. The B.1.q5 sub-question (review-pause checkpoint on the disambiguation) explicitly flags this; the §6.1 self-assessment notes it as a high-rigor structural clarification with the caveat that "future review of the disambiguation against ChatGPT's original verdict is itself a sub-question."

**Why this matters structurally.** If the disambiguation holds up, B.1 becomes substantially narrower than ChatGPT's framing suggested — it becomes a question of whether spatial derivatives at the host vertex contribute to the matrix element at first order in $\delta$. That's a tractable computational question (B.1.q2). If the disambiguation doesn't hold up, B.1 is broader and harder, and the §2.4 reduction arguments don't apply as written.

### §16.3 The reduction argument structure for B.1 alternatives

The §2.4 reduction arguments (R1, R2, R3 alternatives reducing to local algebraic form at $\mathcal{O}(\delta)$) all share a common structural pattern:
1. Identify the alternative's form.
2. Apply icosahedral residual symmetry at the host vertex.
3. Reduce the alternative to a scalar multiple of $\hat{n}$ × the Phase 2 ansatz.

This pattern depends on:
- **B.1.a** Icosahedral-symmetry preservation at the substrate-matrix-element layer (Capotauro's spatial-sector preservation extended to temporal).
- **B.1.b** Derivative content at the host vertex reducing to scalar-multiple-of-$\hat{n}$ (no perpendicular components at first order).
- **B.1.c** Steady-state substrate dynamics (no cosmological time dependence of $\hat{n}$).
- **B.1.d** Substrate-locality extension to temporal sector (Capotauro Finding C-W39/C-W40 extending).
- **B.1.e** First-shell current sum identity (parallel to Capotauro's $\sum_i \hat{u}_i = -(6/\varphi)\hat{n}$).

I deliberately flagged all five as ansatzes rather than treating them as established. The reduction argument is therefore CONDITIONAL on these ansatzes; if any of them fails, the reduction fails or needs to be redone. This is the operational discipline learned from Patch 0528 (every assumption beyond CPP axioms gets flagged).

**Why I did not try to prove B.1.a–B.1.e in this session.** Each is a substantial structural claim that deserves its own treatment. Bundling them into a single closure attempt would replay the Patches 0524–0527 anti-pattern. The session's deliverable is to flag them, queue them as sub-questions (B.1.q1–q6), and leave their substantive examination to future sessions.

### §16.4 The minimal-derivative-order characterization for B.2

The §3.4 reframing of "uniqueness" as "minimal-derivative-order canonical" emerged as a way to sharpen the Patch 0528 §12.13 Calibration 3 framing without overclaiming.

**Patch 0528's framing.** "Phase 2 establishes the *minimal canonical lowest-order* TI-odd substrate object; uniqueness is not proven and remains an open structural question." This is honest but the "lowest-order" qualifier is ambiguous (lowest order in what?).

**The clarification at §3.4.** The candidate TI-odd constructions divide by derivative order in the substrate's local content:
- Order 0: $\sigma_{cycle} \cdot \hat{j}^{net}(v)$
- Order 1: $\nabla \times \vec{j}^{net}(v)$ and similar first-derivative constructions
- Order 2+: higher-derivative + cycle-correlation constructions

The Phase 2 ansatz is uniquely the minimal-derivative-order TI-odd substrate object constructible from $\sigma_{cycle}$ + $\hat{j}^{net}$. Higher-derivative alternatives may exist but they are at higher derivative order, structurally distinct from the order-0 content.

**Why this is cleaner.** The previous "unique" claim required ruling out alternatives that ARE structurally distinct. The "minimal-derivative-order" claim acknowledges those alternatives exist and characterizes the Phase 2 ansatz precisely in terms of its derivative-order content. The claim "the Phase 2 ansatz is the unique TI-odd substrate object at derivative-order 0" is potentially provable, while the broader uniqueness claim is not.

**Status.** The §3.4 minimal-derivative-order characterization is itself a sketch claim. B.2.q2 queues its formalization as a future sub-question. The §7.2 methodological note registers this reframing pattern as potentially generalizable to other CPP uniqueness claims.

### §16.5 The B.1–B.3 dependency structure I noticed

Working through B.1 (§2), B.2 (§3), B.3 (§4) sequentially surfaced that B.1 and B.3 share structural work. Specifically:
- B.1.d (substrate-locality extension to temporal sector) is the same structural claim as B.3.Move-1 (Substrate-Locality Unification's temporal-sector extension).
- A future session that closes the substrate-locality temporal extension would advance BOTH B.1 and B.3 simultaneously.

I flagged this dependency in §4.3's Move-1 ("parallels the §2.4.3 B.1.d ansatz") and in the §5.3 forward queue (B.1.q3 and B.3.q1 share structural work).

**Methodological observation.** When commitments share underlying structural claims, the foundations work programme should be sequenced to pick up shared structural work efficiently. This is the kind of cross-commitment dependency that wouldn't have been visible without working through all three substantively in one session — even though no commitment was closed.

### §16.6 The reviewer-pause checkpoint applied to THIS patch

Per the Patches 0524–0528 methodological precedent (handover §10.1, §15), I applied a self-reviewer-pause checkpoint at §6 of the Patch 0531 sketch before propagating.

**Trigger criterion check.** The §10.1 trigger is "substantive multi-phase closure work where the closure language would propagate into multiple downstream sectors." This Patch is a foundations-work OPENING — it doesn't claim closures, doesn't propagate into downstream sectors. So the formal trigger doesn't activate.

**Why I still applied self-checkpoint at §6.** Even without formal trigger, the lesson from Patches 0527 → 0528 is that self-assessment at session close — explicit identification of where rigor is high vs lower, where claims could be overstated — is a cheap discipline that protects against drift. The §6.1 self-assessment caught two places where the sketch could overstate ("provisional structural claim" reading as closer to closure than actual; "minimal-derivative-order characterization" as established rather than candidate); the preventive flagging at §6.1 makes those framings explicit for future readers.

**The discipline pattern.** Even foundations-work patches should incorporate brief self-checkpoint sections. This is registered (implicitly) as a methodological extension of the §15 reviewer-pause checkpoint precedent.

### §16.7 What I deliberately did NOT do

To avoid replaying the Patch 0527 anti-pattern, I deliberately did NOT:
- Claim B.1.a–B.1.e as proven (each remains a flagged ansatz).
- Register the §2.4 reduction argument as a finding (it's a sketch structural argument, not formal closure).
- Update Phase 2 §12 polished content in `F1_subquestion_pcd_orientation_link.md` (the calibrated framing at §12.13 remains the binding state).
- Promote the F.1 sub-question status from "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work."
- Modify v1.0 SHIPPED paper sources.
- Bundle B.1 + B.2 + B.3 into a single "Phase 2 foundations work closure" claim.

These restraints are the operational discipline learned from Patch 0528. Without them, this session's substantive work would propagate as if it were closure-grade, which would require future retraction once external review caught the overclaim.

### §16.8 Forward-looking pointer

The §5.3 forward queue prioritizes B.1.q5 (review-pause on §2.2 layered disambiguation) as the immediate next priority. This is itself a methodological choice: before deeper substantive work on B.1.q1–q4, verify that the disambiguation framing actually addresses ChatGPT's original concern. If it does, the substantive work proceeds in the §2.4 direction; if not, the framing of B.1 needs revision.

The recommended order — disambiguation review → tractable computations (B.1.q2, B.1.q4) → substantive substrate-locality extensions (B.1.q3, B.3.q1) — front-loads the cheapest validation moves before committing to the multi-session structural extensions.

**Estimated trajectory.** Following the §5.3 priority order, Phase 2 foundations work could substantively progress on the load-bearing sub-questions (B.1.q1–q3 + B.2.q1–q2 + B.3.q1) in 5–9 sessions. After that progress, a reviewer-pause checkpoint should be triggered before any upgrade of the F.1 sub-question status or propagation to downstream documents.

---

*Patch 0531 Tier 4 reasoning appended at Session 139 open. Foundations work substantively underway; no closures claimed; fourteen sub-questions queued. The trajectory remains in foundations-exploration state.*

---

## §17 Patch 0532 — B.1.q5 review-pause checkpoint Tier 4 reasoning

*Session 139 Patch 0532 — substantive review-pause work on §2.2 three-layer disambiguation against ChatGPT's original Patch 0528 verbatim verdict.*

### §17.1 Decision to execute B.1.q5 at this Patch

The §5.3 priority ordering at Patch 0531 recommended B.1.q5 as the immediate next sub-question post-Patch 0531 — explicitly because review-pause sub-questions are the cheapest validation moves and should be front-loaded before deeper structural commitments. Patch 0531's §6.1 self-checkpoint specifically flagged two §2.2 framings that could overstate; B.1.q5 is the operationalization of testing whether the §2.2 placement itself overstates.

The Patch 0531 §6.1 self-checkpoint noted "provisional structural claim reads as closer to closure than actual" — that is a §2.5 concern. But the §2.2 disambiguation was registered with all three of ChatGPT's listed alternatives placed at observable cosmological layer; this placement was made on grounds of *charitable reading* of ChatGPT's alternatives — not on verbatim correspondence. Whether the charitable reading is accurate was the explicit B.1.q5 target.

### §17.2 Verbatim recovery from Patch 0528 §12.13 Calibration 4

The Patch 0528 §12.13 Calibration 4 text was preserved in `F1_subquestion_pcd_orientation_link.md` and provides the registered version of ChatGPT's concern. The verbatim text identifies three alternatives with parenthetical qualifications:

(1) "**Cycle-history accumulation** (the temporal chirality content builds up over many Absolute Moments, **not at a single cycle**)"

(2) "**Nonlocal transport asymmetry** (the chirality content distributes across the substrate's connectivity graph rather than **localizing at one vertex**)"

(3) "**Coarse-grained update statistics** (the chirality content emerges only at scales **above individual CP cycles**)"

The parentheticals are load-bearing. Reading them as decisive disambiguators — which is how technical writing parentheticals function — gives:

- (1): "not at a single cycle" → multi-AM = cosmological
- (2): "rather than localizing at one vertex" → substrate-spatial distribution = substrate-matrix-element layer
- (3): "above individual CP cycles" → multi-cycle = cosmological

This is the key substantive recovery: alternative (2) has a substrate-spatial parenthetical, NOT a cosmological-scale parenthetical. Alternatives (1) and (3) have cosmological parentheticals.

### §17.3 The surprise that drove the verdict

The Patch 0531 §2.2 was written from memory of Patch 0528's calibration content — placing all three alternatives at observable cosmological layer felt cleanly defensible at the framing level. The §2.2 disambiguation table looked structurally clean.

Working through the verbatim text at Patch 0532 surfaced a substantive mismatch: alternative (2) "Nonlocal transport asymmetry" with its parenthetical "distributes across the substrate's connectivity graph rather than localizing at one vertex" is precisely the language used in CPP substrate-physics to describe substrate-spatial structure at one vertex versus distributed across the substrate's connectivity. That language was registered in Capotauro v2.0's substrate-locality theorem framework (Finding C-W39 / C-W40) for the spatial sector.

ChatGPT was, in alternative (2), invoking the same conceptual framework — asking whether the Phase 2 ansatz's chirality content legitimately localizes at the host vertex or actually distributes across the host + first-shell connectivity graph. That is a substrate-matrix-element / substrate-object layer concern, not an observable cosmological concern.

The Patch 0531 §2.2 placement collapsed this distinction. The §2.2 was charitably-reading-aligned but not verbatim-faithful for alternative (2).

### §17.4 What the §8 verdict establishes — and what it does not

**The §8 verdict establishes:**

- §2.2's three-layer framework is structurally coherent and analytically valuable (no walk-back of the layered disambiguation framework itself).
- §2.2's placement of (1) and (3) at observable cosmological layer is verbatim-correct.
- §2.2's placement of (2) at observable cosmological layer is verbatim-incorrect; the correct placement is at substrate-matrix-element / substrate-object layer.
- The corrected placement of (2) connects directly to $\hat{j}_{DI}^{net}(v_{\text{host}})$'s first-shell-aggregated structure (Phase 1 result) — Phase 2's ansatz treats this as a host-vertex quantity (per standard CPP substrate-physics convention), but ChatGPT was specifically asking whether that treatment is structurally justified.
- B.1.d substrate-locality temporal extension (ansatz §2.4.3) is THE load-bearing structural framework for B.1's response to alternative (2). B.1.q3 (the sub-question hardening B.1.d) is therefore elevated in priority.
- Via B.1.d ↔ B.3.Move-1 cross-commitment dependency, B.3.q1 advances in priority simultaneously.

**The §8 verdict does NOT establish:**

- That alternative (2) is "resolved" — B.1.d is still an ansatz at Patch 0532. Resolution awaits B.1.q3 substantive closure (estimated 1–3 sessions per §2.6 table).
- That the priority elevation in §8.8 is binding programme commitment — it is sketch-level recommendation pending Thomas's authorization.
- That §2.2 should be modified inline at Patch 0531 — the immutable-Patch discipline means Patch 0531's §2.2 stands as registered; the refined placement is registered in §8.6 of Patch 0532 and supersedes for downstream work.
- That ChatGPT's verbatim review text is fully recovered — only the Patch 0528 calibrated registration is recovered. Full verbatim recovery (if Thomas can supply ChatGPT's raw review text) might surface additional refinements.

### §17.5 Methodological structure of the review-pause itself

The B.1.q5 review-pause has a specific methodological structure worth registering as a programme pattern:

1. **Identify a substantive structural move made in a prior patch.** (Here: §2.2 three-layer disambiguation at Patch 0531.)
2. **Identify the prior reviewer concern the structural move purports to address.** (Here: ChatGPT's Patch 0528 verbatim alternative-mechanism listing.)
3. **Recover the verbatim source material.** (Here: Patch 0528 §12.13 Calibration 4 verbatim text preserved at `F1_subquestion_pcd_orientation_link.md` §12.13.)
4. **Check the structural move's faithfulness to the verbatim source.** (Here: per-alternative placement check against parenthetical qualifications.)
5. **Issue a sketch-level verdict.** Possible verdicts: full match, partial match, full mismatch. (Here: partial match — framework correct, one placement incorrect.)
6. **Translate the verdict into forward-queue implications.** (Here: B.1.q3 / B.3.q1 priority elevation.)
7. **Apply self-checkpoint discipline.** (Here: §8.10 noted two places §8 itself could overstate and one place it could under-claim.)

The cost is approximately half a session of analytical work; the value is preventing downstream propagation of a structural misplacement. The pattern is cheap and high-value — recommended for any future structural-disambiguation work in CPP.

### §17.6 Connection to Patch 0531's §6 reviewer-pause self-checkpoint

The Patch 0531 §6 reviewer-pause self-checkpoint operated at session close on the entire Patch 0531 work. It caught two §2.2 / §3.4 places where the sketch could overstate.

The Patch 0532 B.1.q5 review-pause operates at sub-question scale on a specific §2.2 placement. It caught one alternative-placement that the §6 self-checkpoint did not flag.

The two review-pause disciplines are complementary, not redundant:
- §6 reviewer-pause at session close catches over-claim language that survives the writing process.
- B.1.q5-style review-pauses catch placement / mapping errors against verbatim source material from prior reviewer concerns.

Both are cheap (half-session each) and high-value (prevent downstream propagation). Programme-level lesson: deploy both at appropriate scales — session close + immediate-next sub-question — for substantive structural patches.

### §17.7 What is deliberately NOT in Patch 0532

- No modification of Patch 0531's §2.2 inline (immutable-Patch discipline).
- No promotion of any B.1.a–B.1.e ansatz to closure (B.1.q5 is sketch-level analytical work, not B.1 substantive closure).
- No finding registered (B.1.q5 verdict is at sketch level; findings live at theorem-level / sub-claim-closure level).
- No F.1 sub-question status change (remains at "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work").
- No v1.0 SHIPPED .tex source modification.
- No §5.3 priority revision applied as binding (the §8.8 revision is sketch-level recommendation; Thomas's authorization required for binding revision).
- No external reviewer engagement (sub-task (e) external review remains future-work item).

### §17.8 Forward-looking pointer

Following Patch 0532, the recommended (sketch-level) next priority is B.1.q4 (first-shell current sum identity) — tractable single-session computational sub-question. Closing B.1.q4 produces the explicit identity $\sum_i \hat{j}_{DI}^{net}(v_i) \parallel \hat{n}$ at first order, which is a structural input both to B.1.q3 (substrate-locality temporal extension) and to B.1.q2 (curl content explicit computation).

After B.1.q4, the recommended priority is the **B.1.q3 + B.3.q1 substrate-locality temporal extension** structural work — the load-bearing response to ChatGPT's alternative (2) per the Patch 0532 verdict. This is estimated at 1–3 sessions (B.1.q3) plus shared work with B.3.q1.

The overall Phase 2 foundations work (Phase 2.5) trajectory estimate remains at ~5–9 sessions for load-bearing sub-question progress, with a programme-level reviewer-pause checkpoint anticipated after substantive progress on B.1.q1–q3 + B.2.q1–q2 + B.3.q1 before any F.1 sub-question status upgrade.

---

*Patch 0532 Tier 4 reasoning appended. B.1.q5 review-pause delivered substantive refinement of §2.2 placement of ChatGPT's alternative (2). No closures claimed; no findings registered. The trajectory remains in foundations-exploration state with sharpened priority ordering recommended.*

---

## §18 Patch 0533 — B.1.q4 first-shell current sum identity Tier 4 reasoning

*Session 139 Patch 0533 — substantive computational work executing B.1.q4 first-shell current sum identity per the authorized §5.3 priority revision.*

### §18.1 Authorization of the §8.8 priority revision

The §8.8 recommended priority revision (registered at Patch 0532 as sketch-level recommendation pending Thomas's authorization) is authorized by Thomas at Session 139 continuation. The revised §5.3 ordering is now binding programme priority — the "sketch-level recommendation pending authorization" qualifier is removed. The B.1.q3 + B.3.q1 substrate-locality temporal extension is now formally promoted from priority (4) to (3) in the §5.3 ordering.

The authorization triggered B.1.q4 execution per priority (2) — the tractable computational sub-question that informs both B.1.q3 (substrate-locality temporal extension) and B.1.q2 (curl content). The 1-session estimate from §2.6 table proved accurate for this work.

### §18.2 The structural surprise of B.1.q4

The §2.4.3 sketch had registered the B.1.e ansatz as "$\sum_i \hat{j}_{DI}^{net}(v_i) \parallel \hat{n}$ at first order by icosahedral symmetry (parallel to Capotauro's $\sum_i \hat{u}_i$ identity)." The framing was heuristic — the structural argument was sketched but the explicit identity was deferred.

The substantive work in §9 revealed two things the §2.4.3 sketch had implicitly assumed without verification:

**First subtlety**: the framework $\hat{n}$ is GLOBALLY FIXED (per Capotauro Reading C, vertex-aligned to $v_{\text{host}}$). At a general vertex $v \neq v_{\text{host}}$, the framework $\hat{n}$ does NOT realign to $\hat{v}$ — it stays parallel to $v_{\text{host}}$'s direction. The Phase 1 simplification $\hat{u}_j \cdot \hat{n} = -1/(2\phi)$ uniform (which was the load-bearing identity for Phase 1's boxed result) is SPECIFIC to vertex-aligned $\hat{n} = v_{\text{host}}$ at the host. At $v_i \neq v_{\text{host}}$, the projections $\hat{u}_j^{v_i} \cdot \hat{n}$ are NOT uniform; they depend on $v_i$'s orientation in the global frame.

**Second subtlety**: the §2.4.3 "parallel to Capotauro's identity" framing was correct at the GROUP-THEORETIC level but heuristic at the EXPLICIT level. Both Capotauro's position sum and the B.1.q4 current sum exhibit direction-collapse by icosahedral central symmetry of perpendicular components — the structural parallel is real. But the explicit coefficient for the current sum requires a substantive computation through the per-vertex current formula generalized to arbitrary $v$.

These two subtleties imply B.1.q4's actual derivation is more substantive than the §2.4.3 sketch suggested. The deliverable in §9 is not just "$\parallel \hat{n}$" but an explicit closed-form coefficient $24/\sqrt{7-\phi}$ derived from the 600-cell first-shell geometry.

### §18.3 The general per-vertex current formula

The key technical move of §9 is the general per-vertex current formula derived in §9.4:

$$\vec{j}_{DI}^{net}(v) = 2 r_0 \delta \left[(2+\phi)\,\hat{n} - \frac{4a}{\phi}\,\hat{v}\right] + \mathcal{O}(\delta^2), \quad a \equiv \hat{v}\cdot\hat{n}$$

This formula is a sketch-level generalization of Phase 1's boxed result. It uses standard icosahedral tensor sum identities ($\sum_j \hat{w}_j^v = 0$ central symmetry + $\sum_j \hat{w}_j^v \otimes \hat{w}_j^v = 4 P_{\perp v}$ via $I_h$-irreducibility on the 3D hyperplane perpendicular to $\hat{v}$) combined with the 600-cell vertex-transitivity that gives every vertex the same first-shell structure in its local frame.

At $v_{\text{host}}$ ($a = 1$, $\hat{v} = \hat{n}$): the formula reduces to Phase 1's $(6 r_0\delta/\phi^2)\hat{n}$ — sanity check passes exactly. At $v_i$ ($a = \phi/2$ from the 600-cell first-shell geometry): the formula gives $\vec{j}^{net}(v_i) = 2 r_0\delta[(2+\phi)\hat{n} - 2\hat{v}_i]$, which decomposes into a uniform $\hat{n}$-component $4 r_0\delta$ plus a per-vertex perpendicular component $-4 r_0\delta\sin(36°)\hat{e}_i$.

**Why this formula is registered at sketch level, NOT as a new finding.** The derivation chain (Phase 1 formula + general first-shell decomposition + icosahedral tensor sum identities) is all standard substrate-physics machinery. Promoting the general formula to a "finding" would invoke a higher rigor status (theorem-level claim) than the derivation supports at present — the formula is an INTERMEDIATE result supporting the B.1.q4 identity; it is not the primary deliverable. The Patch 0533 anti-priorities sustain the "no findings registered" discipline.

### §18.4 The B.1.q4 identity and its numerical verification

The main result of §9:

$$\sum_{i=1}^{12} \hat{j}_{DI}^{net}(v_i) = \frac{24}{\sqrt{7-\phi}}\hat{n} \approx 10.345\,\hat{n} \quad \text{at first order in}\; \delta$$

Two derivation paths converge to this result:

**Path A (group-theoretic)**: $I_h$ residual symmetry at $v_{\text{host}}$ permutes the 12 first-shell vertices, hence permutes their currents, hence the sum is $I_h$-invariant; the $I_h$-invariant direction is $\hat{n}$; therefore $\sum_i \vec{j}^{net}(v_i) \parallel \hat{n}$. This establishes the direction but not the coefficient.

**Path B (explicit)**: per-vertex formula at $v_i$ gives $\vec{j}^{net}(v_i) = 4 r_0\delta[\hat{n} - \sin(36°)\hat{e}_i]$ with uniform magnitude $2 r_0\delta\sqrt{7-\phi}$ across the 12 vertices; sum of unit vectors gives $(24/\sqrt{7-\phi})\hat{n}$ since perpendicular components $\hat{e}_i$ cancel by icosahedral central symmetry in 3D perpendicular to $\hat{n}$.

Both paths confirm the identity. Path B provides the explicit coefficient that Path A leaves open.

**Numerical verification at machine precision**: the explicit 600-cell construction in `code/verify_b1q4_first_shell_current_sum.py` confirms all five load-bearing identities (uniform polar angle at $v_{\text{host}}$; Phase 1 position sum; Phase 1's boxed current; per-vertex first-shell current magnitude $2 r_0\delta\sqrt{7-\phi}$ uniform; B.1.q4 unit-current sum $(24/\sqrt{7-\phi})\hat{n}$) across five test $\delta$ values $\{0, 0.1, \phi^{-3}, 0.5, -0.2\}$ with max deviations $\leq 2 \times 10^{-15}$.

The numerical verification at machine precision is structurally significant: it confirms not just the B.1.q4 identity itself but the entire derivation chain through the general per-vertex formula. If any step in §9.2–§9.6 were wrong, the numerical sum would not match the analytical $24/\sqrt{7-\phi}$ exactly. The match to $2 \times 10^{-15}$ over multiple $\delta$ values verifies the derivation comprehensively.

### §18.5 The structural payoff for R3 reduction in §2.4.3

The B.1.q4 identity provides the explicit content that completes the §2.4.3 (R3) nonlocal spatial averaging reduction:

$$\vec{\omega}_{PCD}(v_{\text{host}}) = \sigma_{cycle}\left(W_0 + \frac{24 W_1}{\sqrt{7-\phi}}\right)\hat{n} = \sigma_{cycle} \cdot c' \hat{n}$$

This is along $\hat{n}$ — same direction as the Phase 2 local algebraic form $\sigma_{cycle}\hat{n}$. The coefficient $c' = W_0 + 24 W_1/\sqrt{7-\phi}$ is absorbed into Phase 3's normalization choice (the $|\hat{j}_{DI}^{net}|_0$ in sketch §13.4 of `F1_subquestion_pcd_orientation_link.md`). Therefore (R3) is structurally equivalent to the Phase 2 ansatz at first order, up to renormalization.

This completes the §2.4.3 sketch reduction for (R3) at first order. The B.1.d ansatz (substrate-locality extension to temporal sector) is now demonstrated for the leading-order direction-uniformity at sketch level — the chirality content distributed across the host + first-shell connectivity aligns along $\hat{n}$ at leading order, structurally consistent with the host-vertex localization claim of the Phase 2 ansatz at first order.

### §18.6 What B.1.q4 contributes to ChatGPT's alternative (2) response

The Patch 0532 §8.7 verdict located ChatGPT's alternative (2) at substrate-matrix-element / substrate-object layer, with the resolution framework being B.1.d substrate-locality temporal extension (hardening via B.1.q3).

B.1.q4 contributes a PARTIAL structural response: at first order in $\delta$, the first-shell-distributed current content, summed over the 12 first-shell vertices, points along $\hat{n}$ — the same direction as the host vertex current. The per-vertex direction-variation at the first-shell ($\hat{e}_i$ components) cancels by icosahedral central symmetry. The "chirality content distribution across substrate's connectivity graph" (ChatGPT's verbatim language) collapses to a direction-uniform multiple of the host current direction when summed appropriately.

**What this establishes** (leading-order direction-uniformity): the distribution-vs-localization distinction reduces to a coefficient renormalization at leading order. The Phase 2 ansatz's treatment of $\vec{\omega}_{PCD}$ as a host-vertex quantity is consistent with the first-shell-aggregated structure at leading order.

**What this does NOT establish** (substrate-locality theorem at all orders): the Capotauro v2.0 spatial-sector substrate-locality theorem (Finding C-W39) is an all-orders structural theorem in $\varepsilon$; its temporal-sector analog at all orders in $\delta$ is the B.1.q3 target. B.1.q4 contributes leading-order direction-uniformity; full substrate-locality temporal extension at all orders requires the B.1.q3 work.

The relationship: B.1.q4 provides the explicit identity that B.1.q3's substantive derivation needs as input. Without B.1.q4's explicit coefficient, B.1.q3 would need to either derive it as a sub-step or work at a more abstract level. With B.1.q4 closed, B.1.q3 can focus on the all-orders theorem structure using the leading-order identity as a calibrated anchor.

### §18.7 Self-checkpoint at session close — places where §9 could overstate

Three places where §9 overstate risks were caught and addressed:

(i) **First-order restriction**: the explicit coefficient $24/\sqrt{7-\phi}$ is first-order. §9.10 explicitly registers this and notes higher-order corrections require B.1.q6 work. Without the explicit qualifier, §9 could read as if the coefficient extends to all orders.

(ii) **Partial vs. full response to alternative (2)**: §9.9 explicitly notes "PARTIAL structural response" with the full response requiring B.1.q3. Without this distinction, §9 could read as if B.1.q4 substantively resolves alternative (2) — which it does not.

(iii) **General per-vertex formula at sketch level**: §9.4's general formula generalizes Phase 1's vertex-aligned result. §9.12 explicitly registers this as sketch-level (NOT a new finding) to maintain the no-findings-registered anti-priority. Without this registration, the general formula could be over-claimed as a theorem-level result.

These three self-checkpoint catches reflect the §6 reviewer-pause discipline applied at sub-question scale — the same pattern as Patch 0532's B.1.q5 review-pause but applied preventively rather than retrospectively. The pattern (sketch-level work + immediate-next self-checkpoint identifying overclaim risks) is internalized as standard discipline for foundations-work patches.

### §18.8 What is deliberately NOT in Patch 0533

- No promotion of B.1.q4 identity to programme-level finding (sketch-level identity only).
- No promotion of §9.4 general per-vertex formula to a new finding (intermediate result, not primary deliverable).
- No closure of B.1 itself (B.1.q1, B.1.q2, B.1.q3, B.1.q6 remain open; B.1.q4 and B.1.q5 closed at sketch level).
- No F.1 sub-question status change (remains "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work").
- No v1.0 SHIPPED .tex source modification.
- No Phase 2 §12 polished content modification in `F1_subquestion_pcd_orientation_link.md`.
- No modification to Capotauro v2.0 content; B.1.q4 uses Capotauro's structural results (Reading C, vertex-aligned $\hat{n}$, first-shell geometry) but does not extend or modify Capotauro v2.0 itself.
- No claim that B.1.d substrate-locality temporal extension theorem is proven (B.1.d remains an ansatz; B.1.q4 contributes structural identity for the eventual B.1.q3 derivation).

### §18.9 Forward-looking pointer

Following Patch 0533, the recommended next priority per revised §5.3 ordering is **B.1.q3 + B.3.q1 substrate-locality temporal extension** (shared structural work via B.1.d ↔ B.3.Move-1 cross-commitment dependency). The B.1.q4 identity derived in this Patch (§9.6) provides the explicit first-shell sum structure that B.1.q3 needs as input. The estimated effort is 1–2 sessions for the shared work.

After B.1.q3 + B.3.q1: B.1.q2 curl content explicit computation (1 session), then B.2.q1 minimal algebraic realization formalization (1–2 sessions).

The overall Phase 2 foundations work (Phase 2.5) trajectory estimate remains at ~5–9 sessions for load-bearing sub-question progress, with a programme-level reviewer-pause checkpoint anticipated after substantive progress on B.1.q1–q3 + B.2.q1–q2 + B.3.q1 before any F.1 sub-question status upgrade.

---

*Patch 0533 Tier 4 reasoning appended. B.1.q4 first-shell current sum identity closed at sketch level with explicit coefficient $24/\sqrt{7-\phi}$ and numerical verification at machine precision. The trajectory remains in foundations-exploration state with B.1.q3 + B.3.q1 substrate-locality temporal extension as the recommended next priority.*


---

## §19 Patch 0534 — B.1.q3 + B.3.q1 substrate-locality temporal extension Tier 4 reasoning

*Session 139 Patch 0534 — substantive structural work executing the now-binding §5.3 priority (3) item, closing both B.1.q3 (substrate-locality extension to temporal sector) and B.3.q1 (Move-1: articulate Substrate-Locality Unification's temporal extension parallel to Finding C-W40) at sketch level via the cross-commitment dependency B.1.d ↔ B.3.Move-1.*

### §19.1 Decision to close B.1.q3 and B.3.q1 together at this Patch

The Patch 0531 §5 cross-commitment dependency identification was that B.1.d and B.3.Move-1 are the same underlying substrate-locality claim approached from two angles: B.1.d (B.1.q3 target) frames it as a substrate-locality theorem supporting the R3 nonlocal averaging reduction; B.3.Move-1 (B.3.q1 target) frames it as the Substrate-Locality Unification corollary parallel to C-W40 (uniformity across first-shell-built substrate objects).

The decision to close both in one Patch was natural given (i) the cross-commitment dependency, (ii) the load-bearing structural content is the same theorem, and (iii) the priority ordering at §8.8 (now binding) lists them as paired. Bundling concern: closing two sub-questions together risks the "bundled-closure anti-pattern" warned against at Patch 0528. But B.1.q3 + B.3.q1 are explicitly identified as cross-commitment-coupled at Patch 0531 §5; closing them together is the natural consequence of that coupling, not an arbitrary bundle.

### §19.2 The structural insight that drove the proof — K3-base protection inherits

The substantive insight: the temporal-sector parallel to Capotauro's spatial-sector K3-base protection is precisely the first-shell-to-first-shell zero-perturbation identity $\hat{e}_{ab}\cdot\hat{n} = 0$ for all icosahedron edges. This SAME geometric identity that Capotauro uses to establish K3-base protection in the spatial sector (first-shell-to-first-shell edges have zero edge-length perturbation at $\mathcal{O}(\varepsilon)$ because $\hat{e}_{ab}\cdot\hat{n} = 0$ via 600-cell geometry) gives the analogous temporal-sector result (zero Mechanism A rate perturbation at $\mathcal{O}(\delta)$ on the same edges).

This was not initially obvious from §2.4.3's sketch. The §2.4.3 framing of B.1.d as "substrate-locality extension" presented it as a parallel claim requiring its own structural work. Working through the proof in §10.4, the parallel turned out to be more than structural — it's INHERITED directly from the same geometric identity used in Capotauro's spatial-sector substrate-locality. The substrate-locality temporal extension is in some sense a "consequence" of Capotauro C-W39's geometric setup applied to a different perturbation parameter.

This is a methodologically interesting result: extending Capotauro's structural framework from spatial to temporal sector doesn't require new geometry — it reuses the existing 600-cell first-shell identities with the temporal-sector perturbation primitive substituted for the spatial-sector one.

### §19.3 What §10 establishes — and what it does not

**§10 establishes:**

- B.1.d Substrate-Locality Temporal Extension Theorem at $\mathcal{O}(\delta)$, sketch Layer 2, with three explicit content parts (a) first-shell-to-first-shell zero perturbation, (b) host-to-first-shell uniform perturbation, (c) $\mathcal{O}(\delta)$ perturbative locality of substrate-physics content at $v_{\text{host}}$.
- Direct parallel to Capotauro C-W39 at matching rigor level ($\mathcal{O}(\varepsilon)$ vs $\mathcal{O}(\delta)$ first-order substrate-locality theorems).
- B.3.Move-1 Substrate-Locality Unification corollary at sketch level, parallel to Capotauro C-W40 — substrate-locality applies uniformly to any first-shell-built substrate object in the temporal sector.
- Connection of B.1.d to the Case A.1 unification ($\delta = \chi = \varphi^{-3}$): both spatial and temporal sectors governed by substrate-locality theorems operating on the same first-shell geometric structure; $\chi = \delta$ identification is the natural consequence of unified-substrate-primitive structure.
- Combined with Patch 0533's B.1.q4 identity, the R3 nonlocal spatial averaging reduction completes at $\mathcal{O}(\delta)$ with explicit coefficient renormalization $c' = W_0 + 24 W_1/\sqrt{7-\phi}$, structurally equivalent to Phase 2 ansatz at first order.
- Full structural response to ChatGPT's alternative (2) at $\mathcal{O}(\delta)$: substrate-spatial chirality content is bounded to first-shell with explicit coefficient; alternative (2) substrate-distribution concern resolved at leading order.

**§10 does NOT establish:**

- B.1.d at higher orders in $\delta$. The $\mathcal{O}(\delta^2)$ extension is open under sub-question B.1.q6 — symmetric with Capotauro's spatial-sector state where C-W39's $\mathcal{O}(\varepsilon^2)$ extension is also open.
- Layer 3 promotion of B.1.d. The Capotauro side has Layer 3 status for C-W39 in the spatial sector; B.1.d Layer 3 promotion would require additional rigor work matching that spatial-sector standard, deferred to future work.
- Explicit cage-shell-factor computations for temporal-sector substrate objects parallel to Capotauro Finding C-W41 (which gives the W-bracelet $1/6$ cage-shell factor). The B.3.Move-1 corollary is at Layer 2 structural-argument level only; Layer 3 with explicit cage-shell factors deferred.
- F.1 sub-question status change. The status remains "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work" — but the foundations work is substantially progressing, and the F.1 status upgrade question becomes live after B.1.q1 + B.1.q2 substantively progress.

### §19.4 Methodological structure of cross-commitment-coupled sub-question closure

The B.1.q3 + B.3.q1 closure pattern is a programme-methodological lesson worth registering: when two sub-questions are identified as cross-commitment-coupled (sharing the same underlying structural work), closing them together in a single Patch is the natural execution pattern — provided the coupling is genuine and the Patch's content addresses both sub-questions explicitly.

This is distinct from the "bundled-closure anti-pattern" warned against at Patch 0528, which referred to bundling MULTIPLE INDEPENDENT closure claims into a single Patch to over-claim aggregate progress. Cross-commitment coupling is different: the multiple sub-questions are not independent claims but two angles on the same structural work, and closing them together reflects that coupling, not aggregation.

The pattern: (i) identify the cross-commitment coupling explicitly at an earlier Patch (here: Patch 0531 §5); (ii) state the shared structural content (here: B.1.d substrate-locality theorem); (iii) execute the substantive closure addressing both angles in a single Patch (here: §10.3 theorem statement + §10.7 corollary articulation); (iv) register both sub-questions' closure status at the same level of rigor (here: both at sketch Layer 2 matching Capotauro C-W39/C-W40 spatial-sector status).

### §19.5 Status of B.1 ansatz framework — three of five demonstrated

After Patch 0534, the five B.1 ansatzes from §2.4 stand at:

- B.1.a (icosahedral-symmetry preservation at matrix-element layer): ansatz, B.1.q1 target. Open.
- B.1.b (curl content non-perpendicular to $\hat{n}$): ansatz, B.1.q2 target. Open.
- B.1.c (steady-state substrate dynamics): framework-level ansatz via Reading C global $\hat{n}$ fix. Demonstrated at framework level.
- B.1.d (substrate-locality temporal extension): demonstrated at sketch Layer 2 at $\mathcal{O}(\delta)$, this Patch 0534.
- B.1.e (first-shell current sum identity): demonstrated at sketch Layer 2 at $\mathcal{O}(\delta)$, Patch 0533.

Three of five at sketch-level status (B.1.c framework, B.1.d and B.1.e demonstrated). Two genuinely open (B.1.a, B.1.b). The §2.5 provisional structural claim from Patch 0531 ("conditional on B.1.a-B.1.e the alternatives reduce to Phase 2 local algebraic form") is now conditional only on B.1.a + B.1.b — the load-bearing ansatzes have narrowed from five to two.

This narrowing is substantive: B.1 substantive closure becomes a question of two specific structural sub-questions (icosahedral-symmetry preservation at matrix-element layer + curl content perpendicular content at first order). Both are tractable computational sub-questions estimated 1-2 sessions each per §2.6. After their closure, the B.1 substantive closure question becomes ripe for full evaluation.

### §19.6 Connection to broader programme arc

The Patch 0534 closure of B.1.q3 + B.3.q1 has implications beyond B.1's local trajectory:

**For the F.1 sub-question status**: with three of five B.1 ansatzes at sketch-level status, the F.1 "PROVISIONAL CLOSURE at viability level pending Phase 2 foundations work" status is becoming progressively less burdened. After B.1.q1 + B.1.q2 substantively progress (estimated 2-3 sessions cumulative), the F.1 status upgrade question becomes live. The §6.2 external reviewer-pause checkpoint should be triggered AT THAT POINT before any status propagation — not at this Patch, but anticipated as the next checkpoint.

**For the OPEN-SD-CHIR-PRIMITIVE umbrella**: the Substrate-Locality Unification corollary (B.3.Move-1) at sketch level provides the structural framework supporting Case A.1 unification ($\delta = \chi$). With Capotauro's C-W40 spatial-sector unification + this Patch's temporal-sector unification corollary, the cross-sector unification at substrate-primitive level is structurally articulated. Patch 0526 §13.11's four-candidate cross-check identified Case A.1 phenomenologically; this Patch articulates the structural foundation.

**For long-term programme target**: the chirality scale from polytope geometry (long-term target registered at Patch 0528 §14.17) is now closer to a tractable question. The substrate-locality theorems (C-W39 + B.1.d) establish that chirality content is first-shell-determined at first order in both sectors; the long-term derivation would extend this to determining the chirality scale magnitude $\chi = \varphi^{-3}$ from polytope geometric structure. Patch 0534's contribution is the substrate-locality framework, not the chirality scale derivation itself — which remains deferred behind F.1/F.2/F.3 stabilization.

### §19.7 What is deliberately NOT in Patch 0534

- No promotion of B.1.d to a registered finding (sketch Layer 2 only; promotion to programme-level Finding registry would require Layer 3 rigor work).
- No promotion of B.3.Move-1 corollary to Capotauro paper (lives in foundations work sketch only; Capotauro paper modifications would need separate review-pause + author-coordination work).
- No claim of B.1 substantive closure (three of five ansatzes at sketch level; B.1.a + B.1.b remain genuinely open).
- No F.1 sub-question status change.
- No v1.0 SHIPPED .tex source modification.
- No Phase 1 §11 or Phase 2 §12 polished content modification.
- No higher-order extension of B.1.d (B.1.q6 territory).
- No external reviewer engagement (deferred until B.1.q1 + B.1.q2 substantively progress).

### §19.8 Forward-looking pointer

Following Patch 0534, the recommended next priority per revised §5.3 ordering is **B.1.q2 curl content explicit computation** — explicit derivation of $\nabla\times\vec{j}_{DI}^{net}|_{v_{\text{host}}}$ at first order in $\delta$, addressing the B.1.b ansatz. Estimated 1 session. The computation uses the per-vertex current formula $\vec{j}_{DI}^{net}(v) = 2 r_0\delta[(2+\phi)\hat{n} - (4a/\phi)\hat{v}]$ from Patch 0533 §9.4, evaluated at neighbors of $v_{\text{host}}$ and differenced to extract the curl content.

After B.1.q2: B.2.q1 minimal algebraic realization formalization (1-2 sessions), then B.1.q1 substantive icosahedral-symmetry preservation at matrix-element layer (1-2 sessions, B.1.a ansatz target). The §6.2 external reviewer-pause checkpoint should be triggered after B.1.q1 + B.1.q2 substantively progress, BEFORE any F.1 sub-question status upgrade.

The overall Phase 2 foundations work trajectory remains in foundations-exploration state; the load-bearing sub-questions are progressively narrowing.

---

*Patch 0534 Tier 4 reasoning appended. B.1.q3 + B.3.q1 substrate-locality temporal extension closed at sketch Layer 2 via the cross-commitment-coupled-closure pattern. The K3-base protection inherits directly from spatial to temporal sector via the same first-shell geometric identity. Three of five B.1 ansatzes now at sketch-level status; B.1.a + B.1.b remain the load-bearing open questions. F.1 sub-question status upgrade question anticipated to become live after B.1.q1 + B.1.q2 substantively progress.*


---

## §20 Patch 0535 — B.1.q2 curl content explicit computation Tier 4 reasoning

*Session 139 Patch 0535 — substantive computational work executing the revised §5.3 priority (4) item B.1.q2 curl content explicit computation, addressing the B.1.b ansatz from §2.4.1.*

### §20.1 Decision to execute B.1.q2 at this Patch

Following Patch 0534's closure of B.1.q3 + B.3.q1 substrate-locality temporal extension, the §5.3 priority ordering pointed to B.1.q2 as the next item (preserved priority (4)). The estimated effort was 1 session — tractable computational sub-question using the general per-vertex current formula from Patch 0533 §9.4 as input.

The §2.4.1 B.1.b ansatz framing was specific: "the argument that $\nabla \times \vec{j}^{net}|_{v_{\text{host}}}$ has no component perpendicular to $\hat{n}$ at first order requires explicit computation; the icosahedral symmetry argument suggests this but does not prove it in 4D." The §11 task was to make the explicit computation precise.

### §20.2 The substantive insight — stronger result than the ansatz claimed

The B.1.b ansatz claimed only "no perpendicular-to-$\hat{n}$ component" — leaving room for an $\hat{n}$-aligned curl component (e.g., a "twist" around the $\hat{n}$ axis). The §11 computation establishes a stronger result: the FULL 4D curl 2-form vanishes at $v_{\text{host}}$ at first order, including all six components.

The substantive insight that drove the stronger result: the $I_h$ residual symmetry at $v_{\text{host}}$ acts on the 4D 2-form space at $v_{\text{host}}$. This 6D space decomposes under $I_h$ into TWO 3D irreducible representations — the $F_{0i}$ vector-like components (involving the $\hat{n}$ direction) and the $F_{ij}$ dual-vector-like components (purely perpendicular). Both 3D irreps are non-trivial — neither contains a trivial sub-representation. Therefore the $I_h$-invariant subspace of the 4D 2-form space is zero-dimensional — any $I_h$-invariant 4D 2-form at $v_{\text{host}}$ vanishes identically.

The curl at $v_{\text{host}}$ at first order is constructed from contributions of the 12 first-shell vertices that are permuted by $I_h$, so the sum is $I_h$-invariant. Therefore the curl vanishes identically — not just the $F_{ij}$ components.

The B.1.b ansatz was structurally too conservative. The actual content is full curl-vanishing.

### §20.3 The K3-base protection identity as the load-bearing structural source

Working through the algebraic computation in §11.5 surfaced a methodologically interesting result: the curl-vanishing is **another consequence of the K3-base protection identity** $\hat{e}_{ij}\cdot\hat{n} = 0$ for first-shell-to-first-shell edges.

Specifically: the $\hat{n}$-content cancellation in the trapezoidal-circulation calculation uses $\hat{n}\cdot(v_i - v_j) = 0$ — i.e., $v_i$ and $v_j$ have identical $\hat{n}$-projection. This follows directly from $(v_i - v_j) \propto \hat{e}_{ij}$ being a first-shell-to-first-shell edge vector, which is perpendicular to $\hat{n}$ via the K3-base protection identity.

This identity is now governing three distinct programme results across both perturbation sectors:

1. **Capotauro v2.0 §13.6 (Finding C-W39 / K3-base protection)**: K3-base edges have zero spatial-sector edge-length perturbation at $\mathcal{O}(\varepsilon)$ because $\hat{e}_{ij}\cdot\hat{n} = 0$ → no Reading C $\varepsilon\,\hat{e}\cdot\hat{n}$ coupling.

2. **Patch 0534 §10.3 (B.1.d substrate-locality temporal extension)**: First-shell-to-first-shell edges have zero temporal-sector Mechanism A rate perturbation at $\mathcal{O}(\delta)$ because $\hat{e}_{ab}\cdot\hat{n} = 0$ → no $\delta\hat{e}\cdot\hat{n}$ coupling. This is the direct temporal-sector analog of K3-base protection.

3. **Patch 0535 §11 (B.1.b curl vanishing, this Patch)**: Discrete curl at $v_{\text{host}}$ vanishes at $\mathcal{O}(\delta)$ because the trapezoidal-circulation contributions cancel via the $\hat{n}$-uniform-projection structure of first-shell vertices, which itself derives from $\hat{e}_{ij}\cdot\hat{n} = 0$.

One geometric identity, three programme results across two perturbation sectors. The K3-base protection identity is doing remarkable structural work.

**Methodological observation registered**: when a load-bearing geometric identity is found to govern one sub-question, it is worth probing whether it governs related sub-questions in adjacent sectors. The cross-sector unification through a single identity is a structural-economy signal that the underlying geometry is doing more than initially apparent.

### §20.4 What §11 establishes — and what it does not

**§11 establishes:**

- B.1.q2 closed at sketch Layer 2 with the curl-vanishing result $(\nabla\times\vec{j}_{DI}^{net})|_{v_{\text{host}}} = 0$ at $\mathcal{O}(\delta)$.
- B.1.b ansatz from §2.4.1 demonstrated with room to spare — actual result is stronger than ansatz claimed.
- Explicit algebraic derivation in §11.5 showing trapezoidal-circulation cancellation on all 30 host-first-shell side-face triangles.
- $I_h$ residual symmetry argument in §11.6 showing the spanning argument: 30 face 2-forms span the full 6D 2-form space, so zero circulation on all 30 implies vanishing curl.
- Numerical verification at machine precision via `code/verify_b1q2_curl_content.py` — all 30 side-face circulations vanish at machine precision across five test $\delta$ values, max deviation $\leq 2.8 \times 10^{-17}$.
- K3-base protection identity registered as the structural source (§11.8) — three programme results across both perturbation sectors derive from the same 600-cell first-shell geometric fact.
- Phase 2 ansatz strengthened: no curl-mediated derivative content at $v_{\text{host}}$ at $\mathcal{O}(\delta)$; the local algebraic form is structurally protected from curl-mediated corrections at leading order.

**§11 does NOT establish:**

- Curl-vanishing at $\mathcal{O}(\delta^2)$ and higher. By $I_h$ residual symmetry, the curl remains $I_h$-invariant at all orders → vanishes at all orders by the §11.6 symmetry argument. But the specific trapezoidal-circulation cancellation mechanism from §11.5 may not extend directly; higher-order verification remains B.1.q6 territory.
- Layer 3 promotion of B.1.q2. The result is at sketch Layer 2, matching Capotauro C-W39 / Patch 0534 B.1.d rigor level.
- Resolution of the remaining B.1.a ansatz (icosahedral-symmetry preservation at matrix-element layer). B.1.q1 remains the single open load-bearing structural question for B.1 substantive closure.

### §20.5 Programme state — load-bearing ansatzes narrowed to one

After Patch 0535, the five B.1 ansatzes from §2.4 stand at:

- B.1.a (icosahedral-symmetry preservation at matrix-element layer): ansatz, **B.1.q1 target. ONE remaining open.**
- B.1.b (curl content non-perpendicular to $\hat{n}$): **demonstrated at sketch Layer 2 at $\mathcal{O}(\delta)$ this Patch (with stronger result than ansatz claimed)**.
- B.1.c (steady-state substrate dynamics): framework-level ansatz via Reading C global $\hat{n}$ fix.
- B.1.d (substrate-locality temporal extension): demonstrated at sketch Layer 2 at $\mathcal{O}(\delta)$ at Patch 0534.
- B.1.e (first-shell current sum identity): demonstrated at sketch Layer 2 at $\mathcal{O}(\delta)$ at Patch 0533.

**Four of five at sketch-level status; ONE remains genuinely open.** The §2.5 provisional structural claim from Patch 0531 ("conditional on B.1.a-B.1.e the alternatives reduce to Phase 2 local algebraic form") is now conditional only on B.1.a — load-bearing ansatzes narrowed from five to one.

B.1.q1 closure becomes the SINGLE load-bearing structural question for B.1 substantive trajectory. The narrowing trajectory: Patch 0531 (five ansatzes flagged) → Patch 0533 (B.1.e demonstrated, four open) → Patch 0534 (B.1.d demonstrated, three open: B.1.a, B.1.b, plus B.1.c framework) → Patch 0535 (B.1.b demonstrated, ONE open: B.1.a). The trajectory has been remarkably efficient — averaging one ansatz closure per session across Patches 0533, 0534, 0535.

### §20.6 Connection to broader programme — F.1 status upgrade question becoming imminently live

The narrowing of B.1's load-bearing ansatzes from five to one substantially changes the F.1 sub-question status trajectory.

Before Patch 0535: F.1 status upgrade question was anticipated to become live "after B.1.q1 + B.1.q2 substantively progress" (estimated 2-3 sessions cumulative per Patch 0534 §10.11). With B.1.q2 closed this Patch, the upgrade question is now anticipated to become live **after B.1.q1 substantively progresses** (estimated 1-2 sessions). The timeline has compressed.

The §6.2 external reviewer-pause checkpoint becomes the binding gate before any F.1 status propagation. The checkpoint should be triggered after:
- B.1.q1 closes (B.1.a ansatz demonstrated or definitively falsified, completing B.1's substantive trajectory)
- B.2.q1 substantively progresses ($\sigma_{cycle}$ algebraization rigor)
- B.3.q1 closed at Patch 0534 (substrate-locality temporal extension corollary)

After the external reviewer-pause completes positively, F.1 sub-question status upgrade from "PROVISIONAL CLOSURE at viability level" to a stronger framing becomes a live programme question.

**Anti-priority sustained**: do NOT trigger F.1 status upgrade until external reviewer-pause completes positively. The reviewer-pause is the binding gate, not optional.

### §20.7 What is deliberately NOT in Patch 0535

- No promotion of B.1.q2 result to registered finding (sketch Layer 2 only; Findings registry promotion would require Layer 3 rigor work).
- No higher-order extension (B.1.q6 territory; the $I_h$-symmetry argument extends to all orders but explicit verification beyond first order is deferred).
- No F.1 sub-question status change.
- No v1.0 SHIPPED .tex source modification.
- No Phase 1 §11 or Phase 2 §12 polished content modification.
- No external reviewer engagement (deferred until B.1.q1 closes).
- No claim of B.1 substantive closure (B.1.a remains genuinely open under B.1.q1).
- No premature F.1 status upgrade preparation (the reviewer-pause is the binding gate, not the closure of B.1.q1 + B.2.q1 alone).

### §20.8 Forward-looking pointer

Following Patch 0535, the recommended next priority per revised §5.3 ordering is **B.2.q1 minimal algebraic realization formalization** (preserved priority (5); 1-2 sessions; formalize the argument that $\sigma_{cycle}$ is the canonical multiplicative TI-odd realization of A5's $\mathbb{Z}_2$ content analogous to $\gamma^5$ in Dirac field theory; per §3.3).

Following B.2.q1: **B.1.q1 substantive icosahedral-symmetry preservation at matrix-element layer** (priority (6); 1-2 sessions; B.1.a ansatz target; the LAST remaining genuinely-open B.1 ansatz). This becomes the SINGLE load-bearing structural question for B.1 substantive closure. After B.1.q1 closure, the F.1 sub-question status upgrade question becomes IMMEDIATELY live; §6.2 external reviewer-pause checkpoint must be triggered BEFORE any F.1 status propagation.

The overall Phase 2 foundations work trajectory is approaching completion of its substantive load-bearing trajectory; the F.1 sub-question status upgrade question moving from "anticipated future" to "imminent live programme question" is the most significant programme-state shift since Patch 0531's opening of foundations work.

---

*Patch 0535 Tier 4 reasoning appended. B.1.q2 curl content explicit computation closed at sketch Layer 2 with stronger result than B.1.b ansatz claimed. K3-base protection identity registered as structural source of three programme results across two perturbation sectors. Four of five B.1 ansatzes at sketch-level status; B.1.a remains the single open load-bearing structural question. F.1 sub-question status upgrade question becoming imminently live; reviewer-pause checkpoint is the binding gate.*
