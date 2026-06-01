# NESS — constructing the Mechanism-A non-equilibrium stationary measure (the sign(μ²) verdict-mover, setup pass)

**Patch 0694 (Session 153). Construction + setup sketch for Priority 1 (the μ²-sign computation). Builds and characterizes the Mechanism-A NESS; maps the pipeline from π to the η-curvature; surfaces the one load-bearing gap (H-NESS). Carries a setup/characterization verify script (`code/setup_ness_stationary_measure.py`). NO η-field built, NO susceptibility computed, NO sign(μ²) asserted, NO verdict move (V3/W3 stand). Conditional on Mechanism A (axiom, OPEN-FP-F1-2).**

**Scope:** TARROW-2 (Patch 0692, review-closed 3/3) cleared the μ²-sign computation to proceed by identifying that the "missing DSL measure" behind §14.17 *is* the stationary measure of the Mechanism-A Markov process. This sketch executes the first step Thomas named — **construct that NESS stationary distribution π before reaching for the η²-curvature** — and does three things: (1) build π concretely and verify it is a valid non-equilibrium steady state whose current reproduces the Patch-0689 O(δ³) result from the stationary side; (2) map the precise pipeline from π to sign(μ²) and locate where the sign bit lives; (3) name honestly the one new load-bearing hypothesis the route now rests on (H-NESS), distinct from the §14.17 wall that 0684 hit. Constructs the measure; computes no curvature; fixes no sign; moves no verdict.

---

## §0 Firewall + anti-priorities (scope/setup discipline: 0637/0668/0679/0683/0684/0688/0689)

1. **NO η-field built, NO susceptibility computed, NO sign(μ²) asserted.** π is constructed; the η²-curvature is *not* taken. The verdict bit is not decided here.
2. **NO verdict move.** FI-C-9 stays **V3**; sign(δ) stays **W3**.
3. **NO new theorem ID, NO reserved-ID consumed.** THEO-CHIR-CAPACITY-1 stays reserved/untouched. NO new programme-level Open-Problem; this is a setup component of B-iii-(i) (capacity ⟺ sign(μ²), 0668) on the route opened in the 0679 sign(μ²) scope and re-cleared by TARROW-2. **NO header count change.**
4. **NO closed theorem reopened** (TARROW-1/2, VW-1/2, STATUS-1/2, BRIDGE-1, CAP-1, MERGE-1/2, the THEO-DSL stack, CONT-1/2/3) and **no F.1 / DSL / OPEN-SM-4 / Capotauro source edited** — all *consumed*. BRIDGE-1's kinematic/P2 cap rides every cross-sector statement.
5. **Conditional on Mechanism A** (F.1 Axioms MA.1/MA.2, OPEN-FP-F1-2 — the rate law is a framework axiom, not yet derived from A1–A11). Every downstream statement carries that conditionality.
6. **No fabricated fluctuation measure.** π is the *stationary distribution of a specified process* (Mechanism A), constructed by solving πQ=0 — not an invented action. The gap between this walker-NESS and an η-field fluctuation measure is named, not papered over (§5).

---

## §1 What the verdict-mover needs, and why the NESS is the right object now

The capacity bit is **sign(μ²)**, the curvature of the ℤ₂-even Landau potential V(η) = V₀ + μ²η² + λη⁴ + … in the chiral (det-coset) order parameter η — the continuous precursor of the pseudoscalar sign(n̂) = FI-C-9 (STATUS-2; the H₄/H₄⁺ label). B-iii/0668: μ²>0 ⇒ η=0 stable ⇒ no chiral vacuum ⇒ **V3 stands by principle**; μ²<0 ⇒ chiral double-well ⇒ the det-coset ℤ₂ breaks ⇒ **V3→V1** (the headline result of the arc). The Landau identity (0684 §1) reduces this to one correlator:

  **χ_η⁻¹ = ∂²V/∂η²|_{η=0} = 2μ²  ⇒  sign(μ²) = sign(χ_η⁻¹),  χ_η = Σ_x ⟨η_x η_0⟩_c.**

**The 0684 wall, and why it is now lifted.** The SUSC sketch (Patch 0684) found that the connected correlator ⟨η_x η_0⟩_c is a property of a *probability measure over substrate configurations*, and that on a **fixed** 600-cell configuration there are no fluctuations — the correlator degenerates, the sign bit is unreachable, both the VW principle-route and the SUSC computation-route terminate at "the §14.17 measure." TARROW-2's reframe supplies exactly that missing object: **Mechanism A is a rate law, hence the transition rates of a Markov process on the 600-cell, hence it has a stationary measure π** — and that π *is* the substrate fluctuation measure SUSC found missing. The measure is no longer free or absent; it is the determinate stationary distribution of a specified process. **That is what clears Priority 1 to proceed.**

**The crucial new feature (why the NESS is more than "a measure").** Patch 0689 proved detailed balance **fails at O(δ³)**: π is not an equilibrium e^{−S} but a genuine **non-equilibrium steady state** carrying a steady probability current. This matters for the sign computation in a specific, computable way (§4): in a NESS the susceptibility is **not** the equilibrium fluctuation formula — by the generalized fluctuation–response relation it acquires a current/"frenetic" contribution. So sign(χ_η⁻¹) has a symmetric (equilibrium-like) part *and* a current part, and the current part is precisely the O(δ³) Kolmogorov content TARROW-2 hardened. The NESS is not just the missing measure; it is a measure whose non-equilibrium character is itself a term in the answer.

---

## §2 The NESS construction (concrete, and built)

**State space.** The 120 vertices of the 600-cell (a single DI-bit walker's position), graph degree 12, 720 undirected edges.

**Generator.** Mechanism A gives the directed-edge rates
  r(v→w) = r₀(1 + δ ê_vw·n̂),  ê_vw = unit(V[w]−V[v]),  with ê_wv·n̂ = −ê_vw·n̂.
The continuous-time generator Q has off-diagonals Q_vw = r(v→w) on edges (0 otherwise) and Q_vv = −Σ_w Q_vw (rows sum to 0).

**Stationary measure.** π solves **πQ = 0** — the left null vector of Q (equivalently the null vector of Qᵀ), normalized to Σπ_v = 1. For δ in the physical range the chain is irreducible ⇒ π is unique and strictly positive.

**Steady current.** On edge (v,w), J_vw = π_v r(v→w) − π_w r(w→v). Detailed balance ⟺ J ≡ 0 ⟺ Kolmogorov cycle condition (0689). A nonzero J is the stationary-side signature of the broken detailed balance.

**Built and characterized** (`code/setup_ness_stationary_measure.py`, this patch; CHECK 1/2/5 PASS, CHECK 3/4 confirm scaling):

| Quantity | Result | Meaning |
|---|---|---|
| δ=0 anchor | π uniform (max\|π−1/120\| ≈ 3e−17), J_max ≈ 3e−17 | isotropic rates ⇒ reversible equilibrium (VW-2's δ=0 RP anchor, stationary side) |
| δ≠0 validity | π_v>0, Σπ=1 for all sampled δ | a valid non-equilibrium stationary measure |
| tilt scaling | d log(max\|π−1/120\|)/d log δ = **1.016 ≈ 1** | π tilts from uniform at **O(δ¹)** — the conservative gradient part (detailed balance through O(δ²) ⇒ π has a leading equilibrium-like tilt) |
| current scaling | d log(J_max)/d log δ = **3.000 ≈ 3** | the steady current **onsets at O(δ³)** — reproducing the Patch-0689 detailed-balance violation **from the stationary-measure side** |

The J_max ∝ δ³ result (slope 3.000) is an **independent cross-check of TARROW-2**: the O(δ³) Kolmogorov per-face content (2δ³abc, 420/1200 faces) and the O(δ³) onset of the stationary current are the same non-reversibility seen from the cycle side and the steady-state side. The construction is correct and consistent with the reviewed foundation.

---

## §3 Inputs consumed

TARROW-2 v1.1 (the NESS reframe + the O(δ³) current, review-closed 3/3); the 0689 finding + `verify_odelta3_kolmogorov_curl.py` (the per-face curl, the 600-cell build reused here); 0684 SUSC (the Landau identity sign(μ²)=sign(χ_η⁻¹); the missing-measure crux now lifted); 0688 engine decomposition (the curl/Kolmogorov framing, dictionary D1–D4); STATUS-2 (η = det-coset label, ℤ₂-even form forced, V2-excluded at axiom level); VW-1 v1.1 (the no-go + the H1 reflection-positivity residual); B-iii/0668 (capacity ⟺ sign(μ²)); the F.1 DSL paper (Mechanism A §3–§4; the §6 path-amplitude rule; OPEN-FP-F1-1 `op:delta-squared`, OPEN-FP-F1-2 `op:layer4-mechanism-a`).

---

## §4 The pipeline from π to sign(μ²), and where the sign bit lives

With π in hand, the route to the sign has four stages. Stage 1 is done (this patch); stages 2–4 are the next computations, with stage 3 carrying the load.

1. **Construct π (DONE, this patch).** Valid NESS; current at O(δ³); equilibrium-like tilt at O(δ¹).
2. **Define the local η-field (stage 2 — reachable structural step).** η must be a *local* order-parameter field η_v on vertices (or on a coarse-graining), ℤ₂-even-potential, whose global sign is sign(n̂)=FI-C-9. The natural candidate is the local det/orientation indicator of a vertex's neighborhood frame (the local enantiomorph label), the field whose homogeneous value is the STATUS-2 H₄/H₄⁺ label. Pinning η_v precisely (and confirming it is the right precursor) is a bounded geometric/representation-theoretic task — the reachable structural deliverable, the NESS analog of SUSC-structural.
3. **The connected susceptibility under π — THE SIGN (stage 3 — the load-bearing computation).** χ_η = Σ_{v,w} ⟨η_v η_w⟩_c, with the connected correlator taken **in the NESS π**. Here the non-equilibrium character enters concretely. Decompose by the generalized fluctuation–response (Agarwal / Baiesi–Maes–Wynants) structure:
   - **symmetric (time-reversible) part** — the equilibrium-like correlator built from the O(δ¹)-tilted, detailed-balance-through-O(δ²) part of π. This is the part a naive e^{−S} reading would give; by VW-2/VW-1 logic it tends to **μ²>0** (the reversible no-go survives where detailed balance survives, i.e. through O(δ²)).
   - **current (frenetic / entropy-production) part** — the genuinely non-equilibrium contribution, governed by the steady current J and hence **O(δ³)** (this patch + 0689). This is the term with no equilibrium counterpart; it is where a sign flip, if any, must come from.
   So the sharp sub-question stage 3 must answer is: **does the O(δ³) current correction to χ_η⁁ flip sign(χ_η⁻¹), or merely perturb a μ²>0 fixed by the symmetric part?** Because the symmetric part is ~O(δ⁰–δ²) and the current part is ~O(δ³), the generic expectation is that the symmetric part *sets* the sign and the current part *perturbs* it — i.e., the naive reading would say μ²>0. The honest open question is whether the symmetric susceptibility is *finite and positive* (giving μ²>0, V3-by-principle, capacity settled negative) or *divergent/marginal* at the symmetric point (so that the O(δ³) current piece becomes sign-determining, opening V3→V1). **This is not decided here.**
4. **Extract sign(μ²) (stage 4 — the verdict-mover, review-gated).** sign(μ²)=sign(χ_η⁻¹). μ²>0 ⇒ V3 stands by principle (spontaneous branch closed); μ²<0 ⇒ V3→V1. Per DG-3, no verdict language without multi-AI review.

---

## §5 The one load-bearing gap, named honestly: (H-NESS)

The NESS lifts the 0684 "no measure" wall, but it introduces one new hypothesis that the route now rests on, and which is **not** justified at this pass:

> **(H-NESS):** the connected η-susceptibility computed in the *single-walker* Mechanism-A stationary measure π (a distribution over one walker's vertex position) tracks the sign of the η²-curvature μ² of the *coarse-grained chiral order-parameter field's* effective potential.

This is the NESS analog of (H-SUSC) (0684 §4) and of the (H5) path-class-weight hypotheses (THEO-DSL): the load-bearing link between a *constructible* object (here π, a 120-state stationary distribution) and the *thermodynamic* object the verdict needs (the η-field potential curvature). The gap is specifically: π is a measure over **where one walker sits**, whereas χ_η is a fluctuation property of an **η-field configuration measure**. Bridging them requires either (i) a many-walker / occupation-field lift of Mechanism A whose stationary measure is a measure over η-configurations, or (ii) a justified argument that the single-walker π's η-moments equal the field theory's η-moments (a mean-field / single-site reduction). **Neither is established here.** Absent (H-NESS)'s justification, a number produced from π is a *proxy*, not sign(μ²) — and computing one and labeling it the verdict would overclaim (the 0684 §5.2 anti-erasure caution, carried forward).

**Honest status of the wall.** 0684 said: *no measure ⇒ no correlator ⇒ §14.17-gated.* TARROW-2 + this patch say: *the measure exists and is constructed; the residual is no longer "find the measure" but "justify (H-NESS) / lift to the field measure, then take the curvature."* That is a **genuine reduction of the gate** — from "invent/derive the whole §14.17 effective action" to "lift the constructed single-walker NESS to the η-field measure (or justify the single-site reduction), then compute one correlator's sign." It is **not** a discharge of the gate. The verdict does not move.

---

## §6 Reachable-now vs gated (after this patch)

- **Reachable now (structural):** (a) π itself — DONE; (b) the η-field definition (stage 2) — a bounded geometric task, deliverable as a small structural result; (c) the *symmetric-part* susceptibility's **form** (the 600-cell graph Green's function / Laplacian envelope, as in 0684 §3 "kinetic channel") — geometric, reachable.
- **Gated (the sign):** (d) the *sign* of the symmetric susceptibility at the symmetric point (finite-positive vs divergent) — needs the η-field measure, i.e. (H-NESS) or the field lift; (e) the O(δ³) current correction's effect on the sign — needs the same. The verdict bit lives in (d)+(e).

So this patch moves the route forward by one concrete stage (the measure is now built and validated, the pipeline and the precise residual are mapped) **without** moving the verdict.

---

## §7 Verdict + disposition

**The NESS measure that 0684 found missing is now constructed, validated, and shown consistent with TARROW-2** (current onset at O(δ³), independent of the Kolmogorov-cycle computation). The route to sign(μ²) is reduced to: define the local η-field (reachable), compute the connected susceptibility **in π** with its symmetric + O(δ³)-current decomposition, and justify (H-NESS) (or lift to the η-field measure). The load-bearing residual is now **(H-NESS)** — a sharper, more local object than "the whole §14.17 action."

**Disposition.** This is a setup/construction pass: it builds the measure and maps the pipeline. **The verdict stands — V3/W3.** The sign is not computed; the (H-NESS) bridge is not justified; no theorem is registered. The next disciplined step (Thomas's choice, §9) is the stage-2 η-field definition and the symmetric-part form — the reachable structural deliverable — before any attempt at the sign, which remains review-gated and (H-NESS)-contingent.

---

## §8 Honest caps + falsifiers

**Caps:** (a) no η-field, no susceptibility, no sign — π only; (b) π is the *single-walker* stationary measure, not (yet) the η-field fluctuation measure — (H-NESS) bridges them and is unjustified; (c) the symmetric-vs-current decomposition (§4) is the *structure* of the NESS susceptibility, not a computed value; (d) conditional on Mechanism A (axiom, OPEN-FP-F1-2); (e) the continuum caveat (finite 600-cell suggestive; block-spin/CONT-1 trend the honest statement) carries from 0679/0684; (f) **NO verdict move — V3/W3 stand.**
**Falsifiers (for the route map, not the verdict):** (N1) if the single-walker π provably *cannot* track the η-field curvature sign (H-NESS false) — would send stage 3 to the occupation-field lift; (N2) if a justified single-site reduction makes π's η-moments equal the field's (H-NESS true) — would make the symmetric-part sign a genuine reachable answer and could *settle capacity* without §14.17 (a major result, review-gated); (N3) if the symmetric susceptibility is divergent at the symmetric point — would make the O(δ³) current piece sign-determining and open V3→V1; (N4) if the η-field cannot be defined locally as a ℤ₂-even precursor of FI-C-9 (contradicting STATUS-2's det-coset structure) — would redirect stage 2. None fires on current results; the constructed π is consistent with all consumed foundations.

---

## §9 Next

The NESS is built. Options, per Thomas's choice:
1. **Stage 2 — define the local η-field** (the ℤ₂-even det/orientation precursor of FI-C-9 on the 600-cell) and crystallize the **symmetric-part susceptibility form** (the graph-Laplacian/Green's-function envelope) into a small structural result with a verify script — the reachable structural deliverable, no sign, no verdict.
2. **Attack (H-NESS) directly** — either the occupation-field lift of Mechanism A (whose stationary measure *is* an η-configuration measure) or a justification of the single-site reduction — the load-bearing bridge; if it falls, stage 3's sign becomes reachable (review-gated).
3. **Discharge OPEN-FP-F1-2** (derive Mechanism A from A1–A11) — Priority 2 — which would make every NESS statement unconditional and ground the construction from first principles.

**No verdict move — V3/W3 stand until stage 3 returns a reviewed sign.**
