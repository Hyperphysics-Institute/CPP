# SUSC — opening the chiral-susceptibility backstop: sign(μ²) = sign(χ_η⁻¹) from the connected η–η two-point function

**Patch 0684 (Session 152). Setup + channel-analysis sketch — opens SUSC (registered in the 0679 sign(μ²)-route scope sketch §5). NO susceptibility computed, NO sign asserted, NO new theorem, NO verdict move (V3/W3 stand).**

**Scope:** Open the SUSC backstop concretely. Write the construction (η, χ_η, the Landau identity sign(μ²) = sign(χ_η⁻¹)); set up the computation against the THEO-DSL pipeline; decompose χ_η into its channels and partition them into *computable-now* vs *§14.17-gated*; identify the precise reason the sign bit is gated; record the convergence with the VW-a-4 residual; refine (anti-erasure) the 0679 optimism about the pipeline's reach; state the framework hypothesis (H-SUSC) a finite-lattice answer would rest on; record honest caps, the disposition, and falsifiers. Computes no susceptibility; fixes no sign; proves nothing about μ².

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS
The VW-a probe (0683) found the principle route to sign(μ²) stalls at §14.17 (the cross-Π transfer-operator positivity residual VW-a-4 needs the explicit action or a δ≠0 reversibility resolution). Per DG-2, that triggers the computation route — SUSC. This sketch *opens* SUSC: it sets up the concrete χ_η computation, and the act of setting it up rigorously surfaces exactly which part is reachable with the existing THEO-DSL machinery and which part is gated.

### §0.2 Anti-priorities sustained (scope-sketch discipline; 0679 precedent)
1. **NO susceptibility computed; NO sign asserted.** sign(μ²) is **not** determined. A geometric-proxy number *could* be produced (§5.2) but is (H-SUSC)-contingent and is deliberately **not** computed here — running it and presenting it as sign(μ²) would overclaim.
2. **NO verdict move.** FI-C-9 stays **V3**; sign(δ) stays **W3**.
3. **NO new programme-level Open-Problem / NO header count change / NO new theorem ID.** SUSC is a route-component of B-iii-(i), already registered. THEO-CHIR-CAPACITY-1 stays reserved, untouched.
4. **NO modification of closed theorems** (VW-1, STATUS-1/2, TARROW-1, BRIDGE-1, the THEO-DSL stack, CONT-1/2/3) or of the DSL / F.1 / OPEN-SM-4 sources — all *consumed*. BRIDGE-1's kinematic/P2 cap rides every downstream statement.
5. **NO fabricated measure.** A connected correlator is a property of a probability measure over substrate configurations; this sketch does not invent one.

---

## §1 The SUSC construction (concrete)
η is the **det-coset order parameter** — the continuous, ℤ₂-even-potential precursor of the pseudoscalar sign(n̂) = FI-C-9 (the H₄/H₄⁺ label, STATUS-2). In Landau–Ginzburg form V(η) = V₀ + μ²η² + λη⁴ + …, the capacity bit is sign(μ²) (μ²<0 ⇒ chiral double-well ⇒ ℤ₂ breaks ⇒ V3→V1; B-iii / 0668).

The **zero-momentum connected susceptibility** is χ_η = Σ_x ⟨η_x η_0⟩_c, and the Landau identity at the symmetric point is

  **χ_η⁻¹ = ∂²V/∂η² |_{η=0} = 2μ²  ⇒  sign(μ²) = sign(χ_η⁻¹).**

So one does not need V(η) in full — only the sign (or divergence) of one correlator: χ_η positive-finite ⟺ μ²>0 (stable symmetric vacuum, V3-by-principle); χ_η divergent/negative ⟺ μ²≤0 (instability toward chiral ordering, V3→V1).

---

## §2 Inputs consumed
THEO-CHIR-VW-1 v1.1 (the unification + VW-a-4 residual); the 0683 VW-a probe (the §14.17 stall + the δ=0 detailed-balance anchor); STATUS-2 (η = det-coset label); THEO-DSL-3..12 (the validated directed-path-enumeration + `mpmath.pslq` pipeline producing closed-form **substrate-current** coefficients, real ℚ[φ]); CONT-1 (the Φ Wilson–Fisher block-spin continuum map); B-iii / 0668 (capacity ⟺ sign(μ²)); the 0679 SUSC registration (§5).

---

## §3 Channel analysis — what the pipeline gives, and what χ_η⁻¹ needs

Decompose the η effective action near the symmetric point into its channels and ask which the existing machinery reaches:

| Channel | Object | Reachable now? |
|---|---|---|
| **Vector-current** | j_k(v) ∝ n̂ + … (the THEO-DSL closed forms) | **✓** — this is exactly what THEO-DSL-3..12 compute (real ℚ[φ], multi-AI-confirmed). |
| **Kinetic / gradient** | the p² channel: the 600-cell lattice Laplacian / graph Green's-function structure for η | **✓ (geometric)** — pure geometry of the 600-cell graph; computable by the same machinery. Sets the *momentum dependence* of χ_η. |
| **Mass / η² (THE SIGN)** | μ² = the η²-coefficient of the effective action = ½ χ_η⁻¹ | **✗ §14.17-gated** — this is neither the vector-current channel nor the kinetic channel; it is the curvature of the effective *potential*, the §14.17 object. |
| **Connected correlator** | ⟨η_x η_0⟩_c (the fluctuations) | **✗ §14.17-gated** — a *connected* correlator is a property of the probability measure e^{−S}; on the fixed 600-cell configuration there are no fluctuations (⟨η_xη_0⟩_c degenerate). Defining χ_η requires the measure. |

**The crux.** The THEO-DSL pipeline operates on the *fixed* 600-cell configuration and produces the *vector-current* channel and (by the same geometry) the *kinetic* channel. But sign(χ_η⁻¹) = sign(μ²) lives in the **mass channel** — the even η² curvature of the effective potential — which is a different object, and a genuine *connected* correlator additionally needs the *measure*. Both the mass channel and the measure are the §14.17 effective action. So pointing the current/geometry pipeline at χ_η yields the structural/kinetic envelope but **not the sign bit**.

---

## §4 SUSC-structural (reachable) vs SUSC-sign (gated); the hypothesis (H-SUSC)

Mirroring the THEO-DSL structural-vs-coefficient split (THEO-DSL-4/6/8 structural; -5/7/9 coefficient):

- **SUSC-structural (reachable now):** at the symmetric (η=0) point χ_η is a single **ℤ₂-even I_h-scalar** (one number, by I_h-invariance — no tensor structure to fix); its momentum dependence is the 600-cell graph Green's function (geometric). The *form* is determinate; only the *overall sign of the inverse* is free.
- **SUSC-sign (§14.17-gated):** sign(χ_η⁻¹) = sign(μ²) is set by the mass channel + requires the measure. Not reachable without §14.17.

A finite-lattice SUSC *answer* would rest on **(H-SUSC):** that a geometric/kinematic susceptibility proxy built from THEO-DSL/600-cell data tracks the sign of the thermodynamic curvature μ². This is the SUSC analog of the (H5) path-class-weight hypotheses — and, like them, it is the load-bearing, currently-unjustified link. Absent (H-SUSC)'s justification, no determinate sign follows.

---

## §5 The convergence finding + anti-erasure refinement of 0679

### §5.1 Both routes reach the same gate, independently
VW-a-4 (the cross-Π transfer-operator positivity residual, 0683) and SUSC-sign (the mass channel + measure) are **the same §14.17 object reached by two independent routes** — the principle route (a no-go on sign(μ²)) and the computation route (a correlator for sign(μ²)). That they converge is itself informative: the §14.17 gate on the capacity bit is **structural, not an artifact of the VW framing**. The spatial capacity question (V3→V1) genuinely has no reachable shortcut around §14.17 at current rigor — consistent with the 0668 B-iii diagnosis and the TARROW-1 / F.2 temporal counterpart (the P-side and T-side of one gate, per the VW-1/TARROW-1 CPT unification).

### §5.2 Anti-erasure: refining the 0679 expectation
The 0679 scope sketch registered SUSC optimistically — "point the validated pipeline at the η–η susceptibility; a single-bit target in the programme's native zero-parameter style." Opening SUSC concretely **refines that**: the pipeline reaches the *structural/kinetic* channel of χ_η, **not the mass-sign channel** that the bit lives in; a *connected* correlator further needs the measure. A geometric-proxy number is producible but is (H-SUSC)-contingent and is **not** a determinate sign(μ²) — computing one and labeling it sign(μ²) would overclaim. (Cf. the THEO-DSL-8 V₄ structural correction and the Patch-0596/0597 stabilizer corrections: optimism registered at scope-time is openly refined when the concrete setup reveals more — earlier records preserved unchanged.)

---

## §6 Verdict + disposition

**The sign(μ²) route is now fully mapped, and both of its branches terminate at §14.17.** The principle branch (VW): structure reachable (VW-b/c established; VW-a-1/2/3 met), the positivity residual VW-a-4 gated (0683). The computation branch (SUSC): structure reachable (SUSC-structural; the χ_η form + kinetic channel), the sign residual SUSC-sign gated (this Patch). No reachable handle circumvents the gate.

**Disposition.** The reachable CHIR-sector work on the capacity question is complete: capacity ⟺ sign(μ²) (0668); the value-side is axiom-excluded (STATUS-2 V2-exclusion); the principle and computation routes to the sign are both mapped to §14.17 (VW-1 review-hardened 3/3; VW-a + SUSC). **The verdict stands — V3/W3.** Actual *emergence* (V3→V1) now genuinely waits on §14.17 (the F.1 viability ceiling — the DSL effective action's η²/mass channel and measure) or F.2 (the σ physicalization), i.e. the deep cross-sector arc **1d-β-ii / OPEN-SM-4 (a)/(b)** — exactly the engine STATUS-1/2 and the 0652 decomposition pinned as the sole V3→V1 lever. The sign(μ²) route did not move the verdict; it **established that no Layer-2.5-reachable move can**, which is the honest closure of this reachable arc.

---

## §7 Honest caps + falsifiers
**Caps:** (a) no susceptibility computed, no sign asserted; (b) SUSC-structural (the χ_η form) is reachable but is *not delivered as a theorem* here — it is noted as the reachable component, available for a future structural Patch if wanted; (c) (H-SUSC) is unjustified — any finite-lattice answer is contingent on it; (d) the continuum caveat (finite-lattice suggestive; block-spin trend the honest statement) carries over from VW-a-5 / 0679; (e) no verdict move. **Falsifiers (for the route map, not the verdict):** (F1) if a measure-free determinate construction of sign(χ_η⁻¹) exists that the channel analysis missed (would reopen SUSC as reachable — not seen; the connected-correlator-needs-measure obstruction is structural); (F2) if (H-SUSC) is justified from first principles (would make the geometric proxy a genuine answer — would itself be a §14.17-level result); (F3) if the mass channel turns out computable from geometry alone independent of the measure (would collapse the gate — contradicted by the channel analysis §3). None fires on current results.

---

## §8 Next
The sign(μ²) route is closed at its reachable boundary. Options, per Thomas's choice: (i) crystallize **SUSC-structural** into a small structural theorem (the χ_η = single ℤ₂-even I_h-scalar + 600-cell Green's-function form — reachable, would carry a verify script) for completeness; (ii) turn to the deep engine **1d-β-ii / OPEN-SM-4 (a)/(b)** (the actual V3→V1 lever, gated behind §14.17 — a multi-session cross-sector arc); (iii) step back to other reachable CHIR/programme targets. **No verdict move — V3/W3 stand.**
