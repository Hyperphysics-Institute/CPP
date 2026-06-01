# The deep engine, decomposed — §14.17 / 1d-β-ii as the curl (Kolmogorov-cycle) content of the Mechanism-A measure

**Patch 0688 (Session 152). Scope sketch — decomposes the deep capacity engine (1d-β-ii / F.1 §14.17 / OPEN-SM-4 (a)/(b)) one level deeper and locates its first reachable gate. NO measure built, NO μ² computed, NO O(δ²) curl computed, NO verdict move (V3/W3 stand).**

**Scope:** The VW arc (VW-1/VW-2) and the SUSC route both terminated at one object — the DSL effective action / the substrate fluctuation measure (§14.17) — and proved the capacity bit sign(μ²) has no Layer-2.5 shortcut around it. This sketch takes the next disciplined step: decompose §14.17 / 1d-β-ii *itself* into sub-problems (the 0652 decomposition stopped at "1d-β-ii = deep engine, deferred" and never opened it), reframe the "missing measure" against what the F.1 DSL paper actually contains, and find the first gate that is *reachable now*. Builds nothing; computes nothing; maps the engine and identifies the first verdict-moving computation.

---

## §0 Firewall + anti-priorities (scope-sketch discipline: 0637/0643/0646/0652/0662/0668/0669/0679/0683)
1. **NO measure built, NO effective action written.** The stationary-measure framing below is a *reframe* of an existing object (the Mechanism-A process), not a construction.
2. **NO μ² computed, NO sign asserted.** The capacity bit is not decided here.
3. **NO O(δ²) curl computed.** The first reachable gate is *identified*; computing it is the recommended next patch, not this one.
4. **NO verdict move.** FI-C-9 stays **V3**; sign(δ) stays **W3**. The sketch maps the gate; the gate's computation would move the verdict.
5. **Conditional on Mechanism A** (F.1 Axioms MA.1/MA.2, OPEN-FP-F1-2 — the rate law is a framework axiom, not yet derived from A1–A11). Every downstream statement carries that conditionality, exactly as the F.1 paper does.
6. **NO new theorem ID, NO reserved-ID consumed** (THEO-CHIR-CAPACITY-1 stays reserved/untouched). NO new programme-level Open-Problem; this refines existing targets (1d-β-ii, OPEN-FP-F1-1, OPEN-CHIR-3 B-iii). NO header count change.
7. **NO closed theorem reopened** (VW-1, VW-2, STATUS-1/2, TARROW-1, BRIDGE-1, CAP-1, the F.1 hardened trio) and **no F.1/OPEN-SM-4/Capotauro source edited** — all consumed. BRIDGE-1's kinematic/P2 cap rides every cross-sector statement.

---

## §1 What the engine must produce
The verdict-moving capacity bit is **sign(μ²)**, the curvature of the ℤ₂-even Landau potential V(η) in the chiral order parameter η (= the det-coset label sign(n̂), STATUS-2; the continuous precursor of FI-C-9). STATUS-2 forces the *form* (ℤ₂-even, no axiom-level pseudoscalar); B-iii/0668 gives **capacity ⟺ sign(μ²)**: μ²>0 ⇒ η=0 stable ⇒ no chiral vacuum ⇒ V3 stands by principle; μ²<0 ⇒ chiral double-well ⇒ the det-coset ℤ₂ breaks ⇒ **V3→V1**. The deep engine = *determine sign(μ²)*.

VW-1/VW-2 + SUSC reduced this to one open object: the substrate **fluctuation measure** e^{−S} (μ² = ½χ_η⁻¹ is a property of the measure's η-curvature; on a fixed configuration there are no fluctuations — SUSC's crux). That measure is §14.17.

---

## §2 The reframe (load-bearing): §14.17's "missing measure" is the Mechanism-A stationary measure
The F.1 DSL paper does not leave the measure free. **Mechanism A is a rate law** (F.1 §3–§4, Eq. mechanism-a):
\[
r(\hat e) \;=\; r_0\,\bigl(1 + \delta\,\hat e\cdot\hat n\bigr),
\]
the DI-bit propagation rate, direction-correlated under the substrate primitive n̂. These are the **transition rates of a continuous-time Markov process on the 600-cell**. A Markov process with given rates has a stationary measure π; the substrate fluctuation measure e^{−S} that SUSC found "missing" is *that stationary measure*. So §14.17 is not an arbitrary action to invent — it is the stationary distribution of a *specified* process, and "does the substrate break to a chiral phase (sign μ²)" is the question whether π's η-curvature goes negative.

This is the same move that made VW-2's Theorem A possible: at δ=0 the rates are isotropic ⇒ detailed balance ⇒ π is an equilibrium ⇒ RP holds. The δ-bias is the *only* new ingredient, and it is explicit.

---

## §3 The concrete first gate: the Kolmogorov-cycle / curl condition on the rate field
Whether π is an **equilibrium** measure (a genuine potential e^{−S}, with RP) or a **non-equilibrium steady state** (carrying a probability current — an arrow) is decided by one classical criterion: the **Kolmogorov cycle condition** — the biased rate field is conservative iff the product of forward rates equals the product of backward rates around every closed loop of the 600-cell graph. Equivalently, the **discrete curl** of the induced net current vanishes. Two branches:

- **Curl-free** (Kolmogorov satisfied): the rate field is a gradient ⇒ detailed balance ⇒ π = e^{−S} is a true equilibrium ⇒ **VW-2 Theorem A extends to δ≠0** ⇒ RP holds ⇒ with VW-b (the det-coset parity is *vectorial*, det=−1) and VW-c (no θ/chiral/complex obstruction), the **Vafa–Witten no-go forces μ²>0** ⇒ the det-coset parity cannot break spontaneously ⇒ **V3 by principle** (capacity settled; the spontaneous branch closed).
- **Curl-carrying** (Kolmogorov violated): the rate field has rotational content ⇒ a steady **probability current** ⇒ a genuine substrate **arrow** (this *is* the TARROW-1 W3 arrow — detailed balance fails) ⇒ the RP guarantee is removed (VW-2's load-bearing caution: RP=unitarity≠T-symmetry, so this does not *prove* μ²<0, but it lifts the no-go) ⇒ the chiral instability μ²<0 becomes *possible* ⇒ the **V3→V1** route opens, and the residual is then the explicit η-curvature.

So the capacity bit (P-side) and the arrow (T-side) are **the same object — the curl of the Mechanism-A current** — viewed from two faces. This is the VW-1/TARROW-1 CPT unification made concrete and computational: one finite quantity decides both.

---

## §4 The find: the curl is already computed at first order — and it VANISHES
The leading-order case is **not open — it is done.** `dynamical_substrate_law/code/verify_b1q2_curl_content.py` (Session 139, **Patch 0535**) established analytically + numerically:

> The discrete curl of the net DI-bit current jₙₑₜ at v_host **vanishes identically at O(δ¹)** — zero trapezoidal circulation around all 30 host-first-shell side-face triangles; by the I_h-spanning argument (the 30 face 2-forms span the full 6D 2-form space), the full 4D curl 2-form vanishes at first order.

Curl-free at O(δ¹) ⇒ the Mechanism-A rate field is **conservative at leading order** ⇒ **detailed balance holds at δ≠0 to first order** ⇒ by §3's curl-free branch, RP holds and **μ²>0 at leading order**. This is the *leading-order case of VW-a-4's reachable sufficient condition* (VW-2 Rmk. coupling: "if the δ≠0 dynamics remain reversible ⇒ RP ⇒ μ²>0 ⇒ V3 by principle") — **already computed, never connected to the chirality verdict.** It is also the concrete content of TARROW-1 at first order: no probability current ⇒ no substrate arrow at O(δ¹).

**Honest cap:** this is *first order only*. It does not settle the verdict (see §5). It is a genuine, validated, affirmative data point — the leading-order case lands on the V3-by-principle (curl-free) side.

---

## §5 The reachable residual = the O(δ²) curl (the first verdict-moving gate)
sign(μ²) is the curvature of V(η) in the η² channel. Near the symmetric point η ~ δ, so the η²-instability structure is an **O(δ²)** property: the leading-order (O(δ¹)) curl-free result establishes detailed balance/RP *at leading order*, but whether μ²>0 *survives* is decided by whether the curl stays zero at **O(δ²)** — the order where the instability would first appear.

The O(δ²) curl is **exactly the deferred OPEN-FP-F1-1 / `op:delta-squared`** (F.1 §10): the O(δ²) current depends on the 2-ball E₂(v_host) — the 12 host-first-shell + 30 first-shell-first-shell + 60 first-shell-second-shell edges — and needs the second-shell (dodecahedral, 20-vertex) inner-product and edge-projection identities, which the F.1 paper says are "well-characterised [geometry] but … have not been worked out," and the extension is "substantive but methodologically analogous to the present paper, at higher order." So the first gate is **reachable**: a bounded, concrete, second-shell 600-cell computation, the next-order replay of the validated Patch-0535 first-order curl computation.

**Outcome map of the O(δ²) curl computation:**
- O(δ²) curl **= 0**: detailed balance persists to second order ⇒ RP ⇒ VW no-go ⇒ μ²>0 to the sign-determining order ⇒ **capacity settles V3-by-principle** (the first verdict-moving result in the chirality arc — the spontaneous-breaking branch closed, conditional on Mechanism A + the §7 dictionary).
- O(δ²) curl **≠ 0**: a second-order probability current ⇒ a genuine substrate arrow appears at O(δ²) ⇒ the VW no-go is lifted ⇒ μ²<0 becomes possible ⇒ the **V3→V1 route opens**, with the explicit η-curvature the next computation; *and* this would be the first concrete derivation of the substrate arrow (TARROW-1 W3 → W-something), the T-face of the same result.

Either branch is verdict-relevant. This is the reachable sub-piece.

---

## §6 The dictionary to nail (sub-claims, stated not assumed)
The §3–§5 chain rests on four links that this sketch *identifies* for the computation patch to establish, not assume:
- **D1 (curl ⟺ Kolmogorov):** vanishing discrete curl of the net current ⟺ the rate field r(ê)=r₀(1+δ ê·n̂) satisfies the Kolmogorov cycle condition (conservative) ⟺ detailed balance of the induced Markov process. The current j is the first-order *response* to the rate bias; the precise j-curl ↔ rate-cycle dictionary must be pinned (the Patch-0535 object is the current curl; tie it to the rate-field cycle products).
- **D2 (detailed balance ⟹ RP at δ≠0):** VW-2 Theorem A is the δ=0 statement; D2 is its extension to the δ≠0 equilibrium measure (the reversible-Markov/Nelson reconstruction applied to π at δ≠0). The Θ_OS/P_det distinction (VW-2 v1.1) must be carried: RP is OS *time*-reflection positivity, P_det the tested parity.
- **D3 (RP ⟹ μ²>0):** the VW-1 no-go, requiring VW-b (vectorial) + VW-c (no θ/chiral/complex). Inherited, review-hardened.
- **D4 (order-counting):** μ² ↔ the O(δ²) curl is the claim that the η²-instability is the second-order property; confirm the precise δ-order at which sign(μ²) is determined (the computation may reveal it needs O(δ²) only, or higher).

---

## §7 The cross-sector half (OPEN-SM-4) — distinct from the capacity front
The capacity computation (§5, the substrate-curl) is the **V3→V1** verdict-mover and is substrate-internal. The OPEN-SM-4 / Capotauro pieces are a *separate* identification layer:
- **(b) magnitude mechanism** = Reading-C: the spatial edge law ℓ(ê)=ℓ₀(1+ε ê·n̂) — the **P-face twin** of Mechanism A's temporal rate law (same first-order n̂-structure; ε↔δ). Candidate registered (OPEN-FI-C-9-FP-MECHANISM); |χ|=φ⁻³.
- **(a) sign-selection nucleation** = the cosmological universe-wide sign event (downstream of (b)); open. This is the *value* (V→fixed), not the capacity; it is the W1/V1 "free/cosmological-inheritance" slot (STATUS-2 / TARROW-1).
- **(c)** the |M|=χ/6 matrix element — SHIPPED (THEO-CAP-1, Δp_LR within 2%).

The CPT unification at the computational level: the **curl of the Mechanism-A current** (T-face/arrow, this sketch's gate) and the **Reading-C spatial chirality** (P-face, OPEN-SM-4 (b)) are the temporal and spatial readings of the *same* n̂-primitive first-order law. Whether the capacity transition *is* EWSB is CONJ-CHIR-1 (the V1→SM identification), gated behind BRIDGE-1's kinematic/P2 cap — not on the capacity-computation critical path.

---

## §8 Verdict and recommendation
**The deep engine is more reachable than "behind §14.17" implied.** It is not a free effective-action construction; it is the curl/Kolmogorov content of a *specified* measure (the Mechanism-A stationary distribution), and:

1. **(DONE, Patch 0535)** O(δ¹) curl-free ⇒ detailed balance / RP / μ²>0 at leading order — the leading-order case of VW-a-4 is already affirmative.
2. **(FIRST GATE — reachable)** the **O(δ²) curl content** (= OPEN-FP-F1-1 / `op:delta-squared`, the second-shell extension): a bounded, concrete computation, the next-order replay of Patch 0535. This is the first verdict-moving computation in the chirality arc.
3. **Result** either settles **V3-by-principle** (curl stays 0 ⇒ μ²>0) or opens **V3→V1** + delivers the substrate arrow (curl ≠ 0 ⇒ μ²<0 possible) — both verdict-relevant, both with concrete next steps.

**Prerequisite:** the second-shell inner-product + edge-projection identities (the dodecahedral 20-vertex shell), "substantive but methodologically analogous to existing work" (F.1 op:delta-squared). This is the one piece to build before the O(δ²) curl; it is geometric, bounded, and on the same footing as the hardened first-shell trio.

**DG (recommended next patch, 0689):** open the O(δ²) curl computation — first the second-shell geometric identities (the prerequisite), then the O(δ²) circulation, with the D1–D4 dictionary (§6) as the framing. This is the first move in the arc that *could* move the verdict, and it carries a genuine verify script. Per Thomas's decision (and within the 0688–0699 band, below the DM 0700 reserve).

---

## §9 Honest caps + falsifiers
**Caps:** (a) nothing here is computed — the O(δ¹) curl-free result is *cited* from Patch 0535, not re-derived; (b) first-order curl-free does NOT settle the verdict (the O(δ²) residual, §5); (c) the whole chain is conditional on Mechanism A (axiom, OPEN-FP-F1-2) and on the D1–D4 dictionary (§6, stated not proved); (d) RP=unitarity≠T-symmetry (VW-2) — a curl ≠ 0 result lifts the no-go but does not *prove* μ²<0; (e) the cross-sector EWSB identification (CONJ-CHIR-1) is not on this path; (f) **NO verdict move — V3/W3 stand.**
**Falsifiers (for the route):** (G1) if the j-curl ↔ rate-cycle dictionary D1 fails (the current's curl is not the right witness of detailed balance — would redirect the gate to the rate-field cycle products directly); (G2) if μ² is determined at an order *below* O(δ²) (would make the gate even more reachable) or only non-perturbatively (would re-defer it); (G3) if the second-shell identities prove not analogous to the first-shell trio (would raise the prerequisite cost). None contradicted by current results; the O(δ¹) curl-free datum (Patch 0535) is consistent with the curl-free branch.

## §10 Next
Open **Patch 0689**: the second-shell geometric identities + the O(δ²) curl computation (OPEN-FP-F1-1 extension), framed by the D1–D4 dictionary — the first reachable, verdict-moving computation of the engine. V3/W3 stand until it returns.
