# VW-a probe — sharpening H1 (reflection positivity of the DSL measure) into an Osterwalder–Schrader criterion on the Φ-image

**Patch 0683 (Session 152). Scope sketch — probes VW-a (= Prop. 4.2 of THEO-CHIR-VW-1 v1.1). NO positivity proved, NO new theorem, NO verdict move (V3/W3 stand).**

**Scope:** Take VW-1's open residual — VW-a, "is the DSL measure reflection-positive (H1)?", currently a first-pass real-measure assessment only — and push it toward an actual Osterwalder–Schrader (OS) positivity criterion. State the OS reflection-positivity condition concretely for the substrate measure under the det-coset reflection; decompose H1 into sub-ingredients VW-a-1..5; partition them into *reachable now* vs *§14.17-gated*; identify the single residual and its reachable candidate sufficient condition; determine whether VW-a closes or stalls. Executes no dynamics; fixes no coefficient; proves no positivity.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS
VW-1 closed the *structural/conditional* half of the sign(μ²) route: the unification (V2-exclusion + the VW no-go as two faces of one parity-even, reflection-positive measure) and the conditional verdict map (if H1 then μ²>0), review-hardened 3/3 at Patch 0682. The whole conditional rested on **one open hypothesis, H1** — reflection positivity of the DSL measure — for which VW-1 had only criteria + a first-pass "real ℚ[φ] coefficients, no manifest obstruction." This sketch deepens that first pass into an actual OS criterion and locates exactly where H1 becomes provable-now versus §14.17-gated.

### §0.2 Anti-priorities sustained (scope-sketch discipline: 0637/0643/0646/0652/0662/0668/0669/0679)
1. **NO positivity proved.** H1 is **not** established. sign(μ²) is **not** computed. This sketch sharpens the question and finds its stall; it does not answer it.
2. **NO verdict move.** FI-C-9 stays **V3**; sign(δ) stays **W3**.
3. **NO claim the substrate is (ir)reversible.** Whether the δ≠0 dynamics remain reversible or acquire a genuine arrow is precisely the unbuilt object (DSL substrate-locality is established; entropy production / irreversible coarse-graining are NOT — they are the candidate mechanism narrative, TARROW-1 W3). Both this sketch and VW-1 keep that open.
4. **RP is NOT T-symmetry.** Reflection positivity encodes *unitarity* of the continuation, not time-reversal invariance; a unitary theory can be T-violating. So "irreversibility" does **not** automatically negate RP. The coupling stated in §5 is a *sufficient-condition* link (detailed balance ⇒ RP), not an equivalence — failure of detailed balance removes a guarantee, it does not prove RP-violation.
5. **NO new programme-level Open-Problem / NO header count change / NO new theorem ID.** This refines the route structure of VW-a, an existing residual inside THEO-CHIR-VW-1. No reserved ID consumed (THEO-CHIR-CAPACITY-1 stays reserved, untouched).
6. **NO modification of closed theorems** (VW-1, STATUS-1/2, TARROW-1, BRIDGE-1, MERGE-1/2, CHI-1, CAP-1, CONT-1/2/3) or of the DSL / F.1 / OPEN-SM-4 sources. All *consumed*, not edited. BRIDGE-1's kinematic/P2 cap rides every downstream statement.

---

## §1 The reachable anchor: H1 holds at the δ=0 substrate

The substrate dynamics are governed by Mechanism A's rate function; the net DI-bit current at the host vertex **vanishes identically at δ=0** — the idealized H₄-symmetric substrate, characterized as **outgoing–incoming detailed balance** (F.1 `F1_subquestion_pcd_orientation_link.md` §; DSL Theorem 7.1 / THEO-DSL-3). Detailed balance is a *sufficient* condition for a self-adjoint, positive transfer operator (a reversible Markov process has real non-negative transfer spectrum), which is exactly the OS positivity content. Therefore:

> **At δ=0, the substrate measure is reflection-positive.** H1 holds at the symmetric reference point.

The chirality *capacity* question (does parity break spontaneously — sign(μ²)) lives at **δ≠0**: the chiral order parameter η is the continuous precursor of sign(n̂)=FI-C-9, and the substrate current at first order in δ is the THEO-DSL object (real ℚ[φ], THEO-DSL-3..12). So H1 for the *full* DSL measure is **not** "prove RP from nothing"; it is:

> **H1 (sharpened): does reflection positivity survive the δ-perturbation away from the δ=0 detailed-balance substrate?**

This is the genuine advance: H1 is anchored, and its residual is a *persistence-under-perturbation* question, not a from-scratch construction.

---

## §2 Inputs consumed
THEO-CHIR-VW-1 v1.1 (the OS/RP definition, the det-coset reflection as θ, VW-b vectorial, VW-c evasion audit, Prop. 4.2 = VW-a); STATUS-2 (the det-coset ℤ₂ = H₄/H₄⁺ reflection, det=−1; achirality); THEO-DSL-3..12 (real ℚ[φ] substrate-current coefficients; δ=0 detailed balance); CONT-1 (the Φ Wilson–Fisher block-spin continuum map at Λ_sub=ℓ_edge⁻¹); TARROW-1 (sign(δ) = W3, the arrow status; the substrate arrow is a candidate mechanism narrative, not derived); the standard Osterwalder–Seiler / Osterwalder–Schrader lattice reflection-positivity criteria.

---

## §3 The OS reflection-positivity criterion, stated concretely
For a reflection θ about a hyperplane Π, the Euclidean measure e^{−S} is **reflection-positive** if ⟨θ(Ā) A⟩ ≥ 0 for every observable A supported on one side of Π. The standard lattice route (Osterwalder–Seiler; Fröhlich–Israel–Lieb–Simon) splits the action

  **S = S₊ + θ(S₊) + S_I**,

with S₊ supported on the positive side, θ(S₊) its reflection, and S_I the cross-Π coupling. RP holds if **e^{−S_I} is a positive operator** on the half-space Hilbert space — concretely, if S_I has the "ferromagnetic"/Osterwalder–Seiler form S_I = −Σ_{i,j} c_{ij} φ_i θφ_j with c positive semidefinite (equivalently, a positive self-adjoint cross-plane transfer operator).

For the substrate: **θ = the det-coset reflection** (the STATUS-2 generator, det=−1 isometry of H₄ through a 600-cell mirror hyperplane — VW-b confirms it is vectorial, in VW's protected class); the fields are the substrate orientation / DI-bit degrees of freedom; S = S_DSL is the DSL effective action (the §14.17 object).

---

## §4 Decomposition VW-a-1 .. VW-a-5 (reachable vs gated)

| Sub-ingredient | Statement | Status |
|---|---|---|
| **VW-a-1** | A reflection θ exists and is a lattice symmetry | **REACHABLE ✓** — H₄ is a reflection group; the det-coset reflection maps the 600-cell to itself (STATUS-2). |
| **VW-a-2** | The measure is real | **REACHABLE ✓ (first pass)** — THEO-DSL-3..12 coefficients real ℚ[φ]; the net current ∥n̂ and Mechanism-A rate function real (VW-1 VW-c(c)). |
| **VW-a-3** | The action is reflection-symmetric, S = θS | **REACHABLE ✓ for the geometric/kinematic part** — substrate achiral (H₄ ⊇ reflections); the rate function is I_h-equivariant at the host vertex (THEO-DSL-4). The *dynamical* part inherits the §14.17 gate. |
| **VW-a-4** | The cross-Π coupling e^{−S_I} is a positive operator (positive transfer matrix) | **THE RESIDUAL** — needs the explicit form of S_I, i.e. §14.17. Reachable *candidate sufficient condition*: PCD/substrate detailed balance persisting at δ≠0 (§5). |
| **VW-a-5** | RP is preserved along the Φ block-spin flow to the continuum | **REACHABLE to state as a required lemma** — a reflection-symmetric blocking (CONT-1 at Λ_sub) preserves RP; the blocking must commute with θ. Stated, not proved. |

Three ingredients (VW-a-1/2/3-geometric) are met at first pass; the entire weight of H1 sits on **VW-a-4**, with VW-a-5 as a continuum caveat. This is the OS sharpening of VW-1's "real, no manifest obstruction."

---

## §5 The residual VW-a-4, and its coupling to the substrate arrow (TARROW-1)

VW-a-4 — positivity of the cross-Π transfer operator — has a **reachable candidate sufficient condition** that does not require integrating the full §14.17 action:

> **If the δ≠0 substrate dynamics remain a reversible (detailed-balance) Markov process, the transfer operator is self-adjoint and positive ⇒ RP holds ⇒ H1 true ⇒ VW applies ⇒ μ²>0 ⇒ parity unbroken ⇒ V3 by principle.**

This is more structurally accessible than the effective action: it is a question about the *form* of the PCD update at δ≠0 (does it preserve the δ=0 detailed balance?), not about the integrated Boltzmann weight. It connects VW-a-4 to the **substrate arrow** (TARROW-1's W-side):

- **Reversible branch:** δ≠0 dynamics keep detailed balance (no genuine arrow) → transfer operator positive → RP for free → no spontaneous parity breaking.
- **Irreversible branch:** δ≠0 dynamics acquire a genuine arrow (detailed balance fails) → the simple positivity *guarantee* is removed → RP must be checked directly. (Per §0.4: this does **not** establish RP-violation — RP encodes unitarity, not T-symmetry — but it removes the cheap route, and is where a capacity *could* open.)

So **H1's truth is pinned to the same unbuilt object as the arrow question**: whether the substrate develops genuine irreversibility at δ≠0 is exactly what the DSL paper does **not** derive (entropy production / irreversible coarse-graining = candidate mechanism narrative; TARROW-1 sign(δ)=W3) and what §14.17 / the F.2 physicalization would settle. The spatial capacity residual (VW-a-4) and the temporal arrow residual (TARROW-1 W1-upgrade) are **the same §14.17/F.2 gate viewed from the P-side and the T-side** — consistent with VW-1's and TARROW-1's CPT unification of the two reopeners.

---

## §6 Verdict and decision gate

**VW-a ADVANCES but does NOT close.**
- *Advance:* H1 is sharpened from "is the DSL measure reflection-positive?" to the anchored, precise residual — *"RP holds at the δ=0 detailed-balance substrate; does it persist at δ≠0 — equivalently, does the PCD dynamics remain reversible, or does a genuine arrow emerge?"* — with VW-a-1/2/3 met at first pass and a reachable candidate sufficient condition (detailed-balance persistence) identified for the residual VW-a-4.
- *Stall:* a *proof* of VW-a-4 needs either the explicit §14.17 action or a resolution of the δ≠0 reversibility/arrow question — both behind the F.1 §14.17 viability ceiling / F.2 (unbuilt). **This is the DG-2 stall signal registered in the 0679 scope sketch.**

> **DG (this Patch): open the SUSC backstop** (0679 §5). Compute sign(μ²) = sign(χ_η⁻¹) from the connected η–η two-point function via the validated THEO-DSL path-enumeration + PSLQ machinery — a direct correlator computation that *sidesteps the positivity proof entirely*. VW-a-4's sharpened residual (the detailed-balance-persistence route) is registered as the parallel deep structural route, to be revisited if/when §14.17 or F.2 advances.

Honest reading: VW (the principle route) cannot *force* the bit now — it stalls at the same gate B-iii flagged — so the computation route (SUSC) is the reachable next move, with the understanding that a finite-lattice sign is *suggestive* and the block-spin trend is the honest continuum statement (VW-a-5 caveat carries over).

---

## §7 Honest caps + falsifiers
**Caps:** (a) nothing here proves RP — VW-a-4 is open; (b) the δ=0 detailed-balance anchor is the *idealized* H₄-symmetric substrate (the physical content is the δ≠0 deviation, exactly the unproved part); (c) "detailed balance ⇒ RP" is a sufficient-condition direction only; (d) the continuum lemma VW-a-5 is stated, not proved; (e) no verdict move. **Falsifiers (for the route, not the verdict):** (F1) if the det-coset reflection is *not* a lattice symmetry of the relevant measure (would break VW-a-1 and VW-b — contradicted by STATUS-2, so not expected); (F2) if the δ=0 substrate does *not* satisfy detailed balance (would remove the anchor — contradicted by the DSL δ=0 vanishing-current result); (F3) if a reflection-symmetric Φ blocking provably fails to preserve RP (would void VW-a-5 and decouple finite-lattice from continuum). None fires on current results.

---

## §8 Next
Open **SUSC** (candidate next Patch): construct the connected η–η two-point function on the 600-cell via the THEO-DSL pipeline, read sign(μ²) = sign(χ_η⁻¹); finite-lattice sign suggestive, block-spin trend the honest continuum statement; would carry a verify script (genuine computation). Per Thomas's choice. V3/W3 stand.
