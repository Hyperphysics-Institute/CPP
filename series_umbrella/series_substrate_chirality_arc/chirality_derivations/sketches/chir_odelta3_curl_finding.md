# O(δ³) Kolmogorov computation — the Mechanism-A substrate is NON-reversible at third order

**Patch 0689 (Session 152). Computation + finding — the first verdict-relevant computation of the deep engine (1d-β-ii / F.1 §14.17). Verify script `chirality_derivations/code/verify_odelta3_kolmogorov_curl.py` (CHECK 1/2 PASS; CHECK 3 reports the curl content). NO theorem registered, NO verdict move (V3/W3 stand — see §6). Conditional on Mechanism A (axiom, OPEN-FP-F1-2).**

**Scope:** Execute the first reachable gate the 0688 sketch identified — the detailed-balance / curl content of the Mechanism-A rate field on the 600-cell. The act of computing it *corrected the order-counting* (the gate is O(δ³), not O(δ²)) and returned a determinate result: **detailed balance fails at O(δ³).** This document records the correction, the per-face formula, the computed result, and its honest verdict implications. It registers no theorem and moves no verdict; it rules out one branch of the 0688 gate and surfaces a concrete arrow candidate.

---

## §0 What this is and is not
- **IS:** a faithful, machine-precision computation of the Kolmogorov cycle content of the substrate rate field, the dictionary-D1 object done properly (Kolmogorov on the rate field, not the proxy "current curl").
- **IS NOT:** a theorem (no ID registered; DG-3 requires review before any verdict language); a μ²-sign computation (it lifts a guarantee, it does not compute the curvature); a verdict move (V3/W3 stand).
- Conditional on Mechanism A (F.1 Axioms MA.1/MA.2 — the rate law is a framework axiom, OPEN-FP-F1-2).

---

## §1 The order-counting correction (honest amendment to the 0688 sketch)
The 0688 sketch located the gate at **O(δ²)**. Working the Kolmogorov condition exactly corrects this. Detailed balance (reversibility) of the Mechanism-A Markov process holds iff, for every cycle, ∏(forward rates) = ∏(backward rates). The per-directed-edge log-ratio is
\[
L(a\to b)=\log\frac{r(a\to b)}{r(b\to a)}=\log\frac{1+\delta c}{1-\delta c}=2\Bigl(\delta c+\tfrac{\delta^3}{3}c^3+\tfrac{\delta^5}{5}c^5+\cdots\Bigr),\qquad c=\hat e_{ab}\!\cdot\!\hat n .
\]
**Only odd powers of δ survive** (forward/backward antisymmetry: reversing an edge sends c→−c, and L is odd). Therefore the detailed-balance violation has **no O(δ²) term at all** — it is identically zero by parity. The first possible violation is **O(δ³)**. (This sharpens dictionary D4; D1 is now the rate-field Kolmogorov object, not the current-curl proxy.)

---

## §2 The per-face formula
Detailed balance ⟺ Σ L vanishes around every face (the faces generate the cycle space of the 600-cell 1-skeleton). Per triangular face with oriented edge-projections a, b, c (loop A→B→C→A):
- **O(δ¹):** Σ = 2δ(a+b+c). The three oriented edge *vectors* sum to zero (closed loop), and all 600-cell edges share one length ℓ=1/φ, so a+b+c = (Σℓ ê)·n̂ / ℓ = 0 for **every** face. The O(δ¹) violation vanishes identically — for all faces, not by any special geometry.
- **O(δ³):** Σ = (2δ³/3)(a³+b³+c³). Since a+b+c=0, the identity a³+b³+c³ = 3abc gives
\[
\boxed{\;\text{per-face O}(\delta^3)\text{ Kolmogorov content} \;=\; 2\,\delta^3\,abc\;}
\]
the **triple product of the three oriented edge-projections.** Detailed balance to O(δ³) ⟺ abc = 0 for every triangular face.

---

## §3 The computation (verify script, machine precision)
`verify_odelta3_kolmogorov_curl.py` builds the 600-cell and enumerates its faces:
- **CHECK 1 (geometry):** 120 vertices, 720 edges, 1200 triangular faces, uniform degree 12. **PASS.**
- **CHECK 2 (O(δ¹)):** max|a+b+c| over all 1200 faces = 2.2×10⁻¹⁶ ≈ 0. Detailed balance holds at first order. **PASS.** (Identity a³+b³+c³=3abc verified to 5.6×10⁻¹⁶.)
- **CHECK 3 (O(δ³), n̂ vertex-aligned):**
  - max|abc| = **0.25**;
  - **420 of 1200 faces have abc ≠ 0** (distinct nonzero values {1/8, 1/4});
  - **all 420 nonzero faces touch the second shell** — consistent with the first-shell cancellation (first-shell icosahedral faces have all edges ⊥ n̂, so abc=0; host-side faces have one ⊥ edge plus two host-edges of opposite orientation whose cubes cancel; the residual lives exactly where 0688 predicted, at the second shell).

**RESULT: detailed balance is VIOLATED at O(δ³).** The Mechanism-A process is non-reversible at third order: it carries a probability current (a nonzero discrete curl) around 420 of the 1200 faces.

---

## §4 Why (the physical picture)
Mechanism A's bias δ ê·n̂ is, at the single-step level, a gradient (the linear function x·n̂) — conservative, so the O(δ¹) cycle sum vanishes. But the *rate* is r₀(1+δ ê·n̂) and the Kolmogorov condition lives in **log r**, which is *nonlinear* in ê·n̂. The nonlinearity generates the odd higher powers; the δ³ term ∝ (ê·n̂)³ is **not** a gradient and has nonzero circulation. So the substrate is reversible to second order and develops a genuine probability current at third order — **the arrow is a nonlinear effect of the multiplicative rate bias.** This is why the first-shell (where the linear/gradient structure dominates and perpendicularity protects) shows nothing, and the violation appears only at the second shell at O(δ³).

---

## §5 Honest verdict implications (framed, not asserted; no verdict move)
The 0688 gate had two branches. The curl-free branch (best case) is now **ruled out by computation**. The consequences split cleanly:

**T-side — a clean positive result (the arrow).** A non-reversible Markov process has a nonzero steady-state probability current, which *is* a time-asymmetry. So the O(δ³) curl content is a **concrete, derived candidate mechanism for the TARROW-1 substrate arrow** (W3 → a derived mechanism candidate) — the T-face. The arrow is no longer merely narrated; it has a computed source: the nonlinear Mechanism-A rate bias, first appearing at third order.

**P-side — landscape-clarifying (the capacity route stays open).** Detailed-balance failure at O(δ³) means **the VW-2 detailed-balance route to RP does not extend to δ≠0** — the cheap, no-go-forcing route to μ²>0 is gone. So **μ²>0 is no longer forced by this route**, and the V3→V1 (spontaneous-breaking) route stays **OPEN** rather than being closed by principle.

**Crucial caution (kept prominent).** This does **NOT** prove RP fails or μ²<0:
- RP = OS reflection (Euclidean) positivity ≠ T-symmetry (VW-2 v1.1, Θ_OS vs P_det). A non-reversible process can still admit a reflection-positive measure in principle; detailed balance is *sufficient*, not *necessary*, for RP. So the no-go's hypothesis is no longer *guaranteed*, not *refuted*.
- μ²<0 is now *possible*, not *established*. The η-curvature sign of the non-equilibrium stationary measure is a further, distinct computation.
**Therefore the verdict does NOT move: V3 stands (V1 not established), W3 stands.** What changed is the *landscape*: the curl-free "V3-by-principle" closure is eliminated, and the live target is now the sign of μ² in a genuinely non-equilibrium measure — with a derived arrow as a bonus T-side result.

---

## §6 Caps + falsifiers + next
**Caps:** (a) conditional on Mechanism A (axiom); (b) at O(δ³) — higher odd orders (δ⁵, …) are not computed (they could add to or, in principle, against the violation, but a *single* nonzero face already breaks reversibility, so the qualitative conclusion is order-stable); (c) the dictionary links D2 (detailed balance ⟹ RP) and D3 (RP ⟹ μ²>0) are the *forward* (curl-free) implications — their failure here lifts the guarantee but, by the §5 caution, does not invert to "¬RP" or "μ²<0"; (d) **no theorem registered, no verdict move.**
**Falsifiers (for the reading):** (H1) if the faces fail to generate the cycle space (they do — the 600-cell boundary is a simply-connected 3-sphere, faces generate; so per-face vanishing ⟺ detailed balance); (H2) if some symmetry forced a *global* cancellation making the process effectively reversible despite nonzero per-face abc (it does not — detailed balance is per-cycle, and 420 faces independently violate it); (H3) if n̂-orientation choice mattered (vertex-aligned Reading C is the framework's fixed choice; the result is computed there).
**Next (DG, recommend):** the result makes the **μ²-sign computation** the live verdict-mover — the η-curvature of the Mechanism-A non-equilibrium stationary measure (μ²<0 ⇒ V3→V1; μ²>0 ⇒ V3 stands with the capacity-mechanism active-but-non-breaking). In parallel, the T-side arrow result is clean enough to assemble into a registered theorem + multi-AI review (DG-3) — the first derived-arrow candidate for TARROW-1. Per Thomas's choice; within the 0688–0699 band, below the DM 0700 reserve.
