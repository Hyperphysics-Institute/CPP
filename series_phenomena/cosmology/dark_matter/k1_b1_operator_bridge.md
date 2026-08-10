# B-1 — THE MECHANISM→RESPONSE-OPERATOR BRIDGE (W-1, discharging condition C-1 structurally) — Patch 2973

**CHANGELOG — v1.3 (Patch 3034): §11 gains the D-KAPPA pointer — the panel-specified contraction measurement executed on the committed dynamics; point-state contraction REFUTED (micro-chaos measured), realization-class confinement + response decorrelation measured with controls; L-6 metric amendment candidate to the panel at the MEAS-3 disposition; 2990 superseded for the contraction claim. Record: `dkappa_3034_interim_record.md`.**

**CHANGELOG — v1.2 (Patch 2990): C-5(iii) discharged structurally — NEW §11 Lemma L-6 (the stationarity-regime lemma, GPT's CONV-012 Q1 item per the corrected 2986 tallies): the admissible perturbation class 𝒫 is DEFINED and proven to remain within the stationary linear-response regime licensed by M1 throughout the operator construction, via a contraction argument whose rate is supplied structurally by M1's exit-at-c/no-return property (the same structure behind L-4's finite support). Verify `code/2990_b1_stationarity_check.py` (4/4, two negative controls). §10 condition ledger updated. Subject to CONV-013 panel confirmation, same status as C-5(i)/(ii) at 2980.**

**Status:** GRADED (b) YES-CONDITIONAL AT OPERATOR GRADE (CONV-012 adjudication 2979); condition C-5 discharged in §9 below (v1.1). Conditional inheritance declared in §7.

**CHANGELOG — v1.1 (Patch 2980, 3 Aug 2026): CONV-012 condition C-5 executed. §9 added: C-5(i) Lemma L-3′ — the discrete-time (Z-domain) restatement of L-3 on the Moment-sampled spectrum, exact below the Moment Nyquist frequency, incorporating the panel-recorded entire-function observation; C-5(ii) L-2 restated on the DRESSED kernel via T-1's TOTAL-force zero — the v1.0 §3 "population superposition" remark is WITHDRAWN (the theorem never used it). New verify `code/2980_b1_discrete_check.py`. Grade per panel; promotion bar remains C-5-review + the floor-clearing W-4 ensemble.**
**Commissioned by:** CONV-011 adjudication (2971), condition C-1 / worker item W-1 — the unanimous Q3(b) gap: "the explicit bridge from the per-DP cycle lemma (and the composite steady-state cancellation) to the full linear-response operator of the ambient Sea," including the acceleration channel (DeepSeek), A2/A3 discharge at operator grade and the I_h residual-odd-channel check (Grok).
**Verify:** `code/2973_b1_bridge_toy.py` (toy units; 9/9).
**What this is NOT:** not a 1B closure; not a promotion move; not an instrument-grade test of the kernel decomposition (that is the W-4 ensemble measurement); mints no value of ξ₂, ζ, η, d_DP, n_DP, or N.

---

## §1 — The object to be constructed

The 2874 S1 replacement statement requires "proven linear-order cancellation of the full CPP response operator." T-1 (2964) proves a *mechanism* statement: for a bound charge pattern translated at constant v, every Sea DP completes a closed traversal returning to unpolarized rest with zero net energy and zero net impulse — hence zero composite force at every constant v. Q3(b) ruled, unanimously, that this is not yet the *operator* statement, because an operator statement quantifies over all admissible small drives v(t), not the constant-v family. This document constructs the operator and propagates the cancellation.

**Definition (the response operator).** Let the composite move with prescribed history x(t), velocity v(t) = ẋ(t), with |v| small (linear-response regime) about the M1 steady state. The Sea reaction force is the functional F[v(·)](t). The **CPP linear-response operator** L is the linear part:

F(t) = −L[v](t) + O(v²),  L[v](t) = M_bare v̇(t) + ∫₀^∞ γ(τ) v(t−τ) dτ,

where causality (support of γ on τ ≥ 0) and time-translation invariance (convolution form) are proved as Lemma L-1 below, and γ is the **memory kernel** — precisely the K-MEM object of PR7 clause 2, in operator form. In frequency space F(ω) = −[iω M_bare + γ̂(ω)] v(ω), γ̂(ω) = ∫₀^∞ γ(τ) e^{−iωτ} dτ.

The S1 statement, made precise: **linear-order cancellation** = (i) the DC (drag) channel of L vanishes identically, γ̂(0) = 0; and (ii) the dissipative part of L vanishes at linear order in frequency, Re γ̂(ω) = O(ω²) as ω → 0 — so that for EVERY admissible slow drive, the linear response is conservative (inertial + stiffness dressing) with dissipation entering only at radiative order.

## §2 — Lemma L-1 (kernel existence, causality, convolution form)

*Statement.* About the M1 steady state, the linear part of the Sea reaction is a causal convolution against v.

*Proof.* (a) *Causality:* the Moment-stepped re-caused dynamics (PCD cycle) updates Sea state from past state only; no DP's displacement at Moment n depends on the composite's motion at Moments > n. Hence F(t) depends on {v(t′) : t′ ≤ t} and supp γ ⊆ [0, ∞). (b) *Time-translation invariance:* Lemma M1 (T-2, 2965) establishes the translated bound state as the fixed point of the D-1 refresh — the steady state is invariant under Moment translation, so the linearized reaction depends only on t − t′; the linear functional is then a convolution (Riesz representation on the translation-invariant causal class). (c) *Linearity:* definition of the linear-response regime; higher orders are collected in O(v²). ∎

*Discharge note (A2 at operator grade).* L-1 is where premise A2 (steady-state existence) enters the operator construction, and it enters through M1 exactly as the panel accepted at Q1/Q2: conditionally at T-1, discharged at M1, non-circularly (M1 does not use T-1). The C-2(a) conditional statement propagates verbatim: L-1 is conditional on the M1 fixed point, which T-2 supplies.

## §3 — Lemma L-2 (DC cancellation: T-1 → γ̂(0) = 0, exact)

*Statement.* γ̂(0) ≡ ∫₀^∞ γ(τ) dτ = 0.

*Proof.* Take the admissible drive v(t) ≡ v₀ (constant, any |v₀| < v_max). By T-1 the composite force vanishes identically: F = 0 at every constant v₀ — the per-DP cycle lemma × steady-population lemma gives zero net impulse per traversal for every Sea DP, and the population superposition is exact (linearity of impulse). Inserting v ≡ v₀ into L: F = −v₀ ∫₀^∞ γ(τ) dτ = 0 for all v₀ ≠ 0, hence ∫γ = 0. ∎

*Remarks (v1.1, C-5(ii)).* (i) T-1's zero is stronger than linear order (it holds at every constant v below cap); L-2 uses only its linear content. (ii) γ is the DRESSED kernel of the FULL linearized dynamics as defined at L-1 — including every DP–DP (relay) effect at linear order — and T-1's statement is a TOTAL-force zero, so L-2 requires NO per-DP decomposition and NO traversal-independence premise: insert the constant drive into the full linear response and the total kernel's DC weight vanishes. The v1.0 remark that read this as a "population superposition, exact by linearity of impulse" is WITHDRAWN as unnecessary and misleading (CONV-012 C-5(ii)); the per-DP cycle-lemma picture remains the MECHANISM behind the zero, but the operator proof runs on the total force alone. (iii) L-2 inherits T-1's grade — now engine-grade discrete via T-1 v1.1 Lemma T-1.L (C-2 discharged-confirmed at 2979). The bridge does not launder conditions; see §7.

## §4 — Lemma L-3 (propagation to every admissible channel: no linear-order dissipation)

*Statement.* If γ̂(0) = 0 and γ has finite support τ_b (Lemma L-4), then Re γ̂(ω) = −(ω²/2) ∫₀^{τ_b} τ² γ(τ) dτ + O(ω⁴) — the dissipative channel vanishes at linear order in ω for EVERY admissible drive; and the first-order-in-ω part of γ̂ is purely imaginary, iω · [−∫ τ γ(τ) dτ], i.e., an inertial **dressing** ΔM = ∫₀^{τ_b} τ γ(τ) dτ, not a dissipation.

*Proof.* Expand γ̂(ω) = ∫γ(τ)[1 − iωτ − ω²τ²/2 + …] dτ. The ω⁰ term is ∫γ = 0 (L-2). The ω¹ term is −iω∫τγ dτ — imaginary, hence conservative (it renormalizes M_bare → M = M_bare + ΔM: the T-3 §6 "stiffness + dressing" in operator form). The leading REAL (dissipative) term is −(ω²/2)∫τ²γ dτ. Finite support ⇒ all moments finite ⇒ the expansion is legitimate. ∎

*Consequences.* (a) **Every admissible perturbation channel:** any admissible drive decomposes over frequencies; time-averaged absorbed power at linear response is P(ω) = ½ Re γ̂(ω) |v(ω)|² ω-by-ω = O(ω²) — zero at linear/adiabatic order for all drives, not just DC. This is the propagation the panel demanded. (b) **The acceleration channel (DeepSeek's named gap):** the linear-in-acceleration response is the inertial term (M_bare + ΔM) v̇ EXACTLY; dissipation attached to acceleration enters only at O(ω²) — the radiative order — consistent with, and required by, T-2's W = ΔE + E_rad with E_rad ≥ 0 → 0 adiabatically. T-1's zeroth-order-in-a scope is thereby extended: at first order in a the response is purely inertial. (c) *Disclosed non-derivation:* the SIGN ∫τ²γ dτ ≤ 0 (passivity, Re γ̂ ≥ 0) is a radiative-consistency requirement, NOT derived here; it is registered as a check the ensemble measurement can test, alongside the standing exportable falsifier.

## §5 — Lemma L-4 (support: T-3 §6 → finite τ_b; the Markovian-plus-stiffness limit)

*Statement.* Under the T-3 §6 kernel decomposition — anchored content conservative (Mori–Zwanzig renormalization of the instantaneous term), unanchored content a ballistic transient of support ≤ d_DP/c, no back-scatter, no return (M1) — the regular kernel γ has support τ_b ≤ d_DP/c and no long-time tail. Consequently for drives with ωτ_b ≪ 1 the operator reduces to L[v] = M v̇ (+ K₁ x in the bound case): **Markovian-plus-stiffness**, with corrections O((ωτ_b)²).

*Proof.* The decomposition is exhaustive at mechanism level (T-3 §6): anchored content contributes the instantaneous (renormalized) term and the dressing; unanchored content departs at c with no return (M1), contributing only within τ ≤ d_DP/c. Absence of a tail ⇒ γ ≡ 0 beyond τ_b ⇒ finite moments (discharging L-3's premise) ⇒ the adiabatic reduction, with the residual bounded by the L-3 expansion. ∎

*Grade note.* L-4 imports the §6 decomposition at its current grade: mechanism level, instrument-grade UNTESTED (K-MEM-MEAS-1 UNRESOLVED-BY-FLOOR; standing NONE). The registered exportable falsifier — a measured long-time dissipative tail at d_DP — is now also, via this bridge, a falsifier of the OPERATOR statement's L-4 leg. The ensemble measurement (W-4) tests the bridge, not only the mechanism.

## §6 — Lemma L-5 (isotropy: no residual odd channel after I_h averaging)

*Statement.* In three dimensions with the I_h-equivariant stencil, the kernel is scalar (γ_ij = γ δ_ij) through degree 5, and no odd-rank vector channel survives orientation averaging: every odd-rank moment of the 12-direction stencil vanishes identically.

*Proof.* FACT G1 (banked, 2951/CONV-011 Q5(ii)): every I_h-equivariant stencil is exactly isotropic through degree 5 — the only invariant tensors through that degree are δ_ij products, which are even-rank; hence γ_ij ∝ δ_ij through degree 5 and no rank-1/3/5 invariant exists. Independently and elementarily: the 12-direction stencil is centrally symmetric (antipodal pairs), so every odd-rank direction moment Σ n̂^⊗(2k+1) cancels pairwise exactly. Verified numerically (CHECK 8). ∎

*Discharge note (A3 at operator grade, C-2(c) scope).* The bridge imports from SF-6 ONLY: (i) the mutual-messaging/reciprocity of pair interactions at the microscopic level (used inside T-1, per the Grok/GPT-accepted reading — cited there, not re-imported here) and (ii) the stencil equivariance behind G1. No composite-level action–reaction is used anywhere in L-1…L-5; Newton 3 for composites is downstream OUTPUT territory, not input.

## §7 — Theorem B-1 and its honest conditionality

**Theorem B-1 (the bridge).** Under premises P1 = T-1 (constant-v detailed balance; grade: mechanism level, C-2 revision pending), P2 = M1 (steady-state fixed point; non-circular), P3 = T-3 §6 (kernel decomposition; grade: mechanism level, instrument-grade untested), P4 = FACT G1 (banked): the full CPP linear-response operator of the ambient Sea on the composite exists as the causal convolution of §1 and satisfies

γ̂(0) = 0 (exact, from P1);  γ̂(ω) = iω ΔM + O(ω²) with ΔM real (dressing);  Re γ̂(ω) = O(ω²);  supp γ ⊆ [0, d_DP/c];  γ_ij = γ δ_ij through degree 5, no residual odd channel.

Hence **the linear-order cancellation of the full CPP response operator holds**: for every admissible drive the linear response is conservative — inertial (M = M_bare + ΔM) plus stiffness (K₁, bound case) — with zero drag at DC to all orders in v and dissipation entering only at radiative order O(ω²), vanishing adiabatically, consistent with T-2.

**Conditionality (declared, not laundered).** B-1 is a *structural* discharge of C-1: the bridge exists as a theorem and the cancellation provably propagates. Its grade is capped by its premises: (i) P1 at C-2 grade — the discrete traversal bijection (W-2) upgrades L-2 from mechanism to engine-grade discrete; (ii) P3 at instrument grade — the W-4 ensemble measurement tests the support/tail leg (and now the passivity sign, §4(c)); (iii) whether B-1 satisfies the 2874 S1 statement *at operator grade* is panel business (the next CONV round), not worker self-adjudication — the worker notes only that B-1 is the object the Q3(b) gap named, presented with its computation per the seventh-convergence discipline. **Nothing in this document moves 1B, PR7, the 2838 branch, the package grade, or any ledger line.**

## §8 — What the toy verifies (and what it cannot)

`code/2973_b1_bridge_toy.py` builds an explicit per-DP traversal impulse profile satisfying the cycle lemma by construction, population-superposes it into a kernel, and verifies the full implication chain numerically: cycle-lemma zero → γ̂(0)=0 → constant-v force zero → first-order-in-ω purely imaginary (dressing extracted) → Re γ̂ = O(ω²) (log-log slope fit) → finite support → adiabatic Markovian-plus-stiffness residual scaling (ωτ_b)² (factor-4 test under Ω-doubling) → I_h odd-moment cancellation (ranks 1, 3, 5) → M-consistency of the dressed inertial coefficient. The toy demonstrates the IMPLICATION STRUCTURE of L-2…L-5; it does not re-derive the microphysics and does not test P3 at instrument grade — that is W-4's job. Toy units only; no physical value of any open quantity is computed.


---

## §9 (v1.1) — C-5(i): Lemma L-3′, the discrete-spectrum form (exact, no continuum borrowed)

**Setting.** The engine is Moment-stepped: the kernel is the finite sample sequence {γ_k}, k = 0…K−1, with K·Δt ≤ τ_b (finite support, L-4), and the admissible drive class is defined ON Moments — frequencies satisfy ω < ω_N ≡ π/Δt (the Moment Nyquist frequency) by construction of the drive space, not by assumption. The transfer function is the trigonometric polynomial

  γ̂(ω) = Δt Σ_{k=0}^{K−1} γ_k e^{−iωkΔt}.

**Lemma L-3′.** If Σ_k γ_k = 0 (the discrete DC zero, supplied EXACTLY by T-1 v1.1 Lemma T-1.L through the restated L-2), then for every admissible ω:

  Re γ̂(ω) = Δt Σ_k γ_k [cos(ωkΔt) − 1] = −(ω²Δt/2) Σ_k γ_k (kΔt)² + R(ω), with |R(ω)| ≤ (ω⁴Δt/24) Σ_k |γ_k| (kΔt)⁴;
  Im γ̂(ω) = −ωΔt Σ_k γ_k (kΔt) + O(ω³) — purely inertial dressing at first order, ΔM = Δt Σ_k γ_k (kΔt).

Hence Re γ̂(ω) = O(ω²) with an EXACT finite-sum coefficient and an EXPLICIT remainder bound — no linear-order dissipation in any admissible channel, at the discrete grade the engine computes.

*Proof.* Insert the DC zero to replace e^{−iωkΔt} by (e^{−iωkΔt} − 1) termwise; the cosine and sine Taylor expansions are exact with Lagrange remainders for each of the FINITELY many terms; sum the bounds. Because γ̂ is a trigonometric polynomial it is an ENTIRE function of ω (the worker's formulation subsuming Grok's CONV-012 support argument; attribution corrected at adjudication §7 D-2, Patch 2986): the expansion is globally convergent, and the only physical restriction is the drive class ω < ω_N, which the Moment-stepped drive space imposes by construction. Aliasing is not a failure mode but a domain statement: frequencies ≥ ω_N do not exist in the admissible class, so nothing is asserted about them. ∎

*What changed vs L-3 (v1.0).* Nothing in the conclusion; everything in the grade. L-3 expanded a continuum integral; L-3′ expands the finite Moment sum the engine actually evaluates, with exact coefficients and a bound in place of an O(·). L-3 is retained as the continuum shadow of L-3′.

**Verification.** `code/2980_b1_discrete_check.py` (9/9): coarse-sampling exactness (K = 8, where continuum quadrature is visibly wrong and the discrete identity still holds to machine precision); slope-2 fit of Re γ̂ across three decades below Nyquist; remainder-bound audit; discrete-dressing dual extraction; behavior approaching ω_N finite and defined; NEGATIVE CONTROL — Σγ_k ≠ 0 produces Re γ̂(0) ≠ 0, i.e., linear-order dissipation appears the moment the DC zero is broken, so the check can fail.

## §10 (v1.1) — Condition ledger after C-5

C-1: bridge DERIVED and panel-graded (b). C-2/C-3/C-4: DISCHARGED-CONFIRMED (2979). C-5(i)/(ii): discharged structurally HERE (v1.1, 2980); **C-5(iii): discharged structurally at §11 (v1.2, 2990)** — all three clauses subject to CONV-013 panel confirmation. Standing bar for any operator-grade promotion or 1B movement: C-5 review + the floor-clearing W-4 ensemble (which also tests L-4's support/tail leg and the disclosed passivity sign). Nothing in this revision moves the ledger.

## §11 (v1.2) — C-5(iii): Lemma L-6, the stationarity-regime lemma (the admissible class 𝒫, defined and kept)

**What the panel asked (GPT, CONV-012 Q1, corrected record 2986 D-3, verbatim basis at `reviews/conv012_returns/seat1_gpt.md`):** "explicit proof that the perturbation space used in B-1 stays within the stationary linear-response regime licensed by M1" — M1 licenses linearization *around* the translated steady state; what was missing is that admissible perturbations REMAIN inside that regime throughout the construction, not merely at the linearization instant.

**Definition (the admissible perturbation class 𝒫).** Moment-sampled drive histories {v_n} satisfying:
(𝒫-a) **amplitude bound:** sup_n |v_n| ≤ v_max ≪ c (the linearization small parameter ε = v_max/c);
(𝒫-b) **slow variation:** sup_n |v_{n+1} − v_n| ≤ Δv_max, with Δv_max small on the scale set below.
Frequency content below the Moment Nyquist is implied by Moment sampling (C-5(i) grade); no continuum class is invoked.

**Lemma L-6.** For every drive in 𝒫, the Sea state remains, at every Moment n, within a uniformly small neighborhood of the *instantaneous* M1 fixed point S(v_n):

  d_n ≡ dist(state_n, S(v_n)) satisfies sup_n d_n ≤ d_0 κⁿ + C·Δv_max/(1−κ), with κ < 1,

so the linearization of L-1 is uniformly valid along the whole trajectory (residual O(ε²), never accumulating), and the operator construction of §§2–6 proceeds inside the stationary linear-response regime at every step.

**Proof.** (i) *The fixed-point family and its linear sensitivity.* M1 (T-2 §(v)) supplies, for each constant v below cap, the anchored co-moving configuration S(v) as the attracting fixed point of the per-Moment map. The family is linearly sensitive in v at first order: the anchored content is the source's SSV imprint, whose v-dependence at first order is the SF-6 curl linkage (already an admissible T-2 input); hence dist(S(v), S(v′)) ≤ C·|v − v′| for |v|,|v′| ≤ v_max, with C the imprint sensitivity. (ii) *One Moment of an admissible drive.* Between Moments the drive moves the target fixed point by at most C·Δv_max (by (i)), and the per-Moment map contracts the existing deviation toward the instantaneous fixed point at rate κ < 1. The contraction is STRUCTURAL, not assumed: deviation content is, by M1's dichotomy, unanchored — it receives no sustaining imprint, propagates at c, and exits the co-moving neighborhood within τ_b = d_DP/c Moments with no return and no back-scatter (Version B outward-only volley) — the same exit-at-c structure that gives L-4 its finite support. A deviation that survived ≫ τ_b would BE a long-time kernel tail; boundedness of memory and contraction are one property. (iii) *The recursion.* Therefore d_{n+1} ≤ κ·d_n + C·|v_{n+1} − v_n|, and iterating: d_n ≤ d_0κⁿ + C·Δv_max·(1−κⁿ)/(1−κ) ≤ d_0κⁿ + C·Δv_max/(1−κ). Uniform, no secular growth, for every drive in 𝒫. (iv) *Uniform linearity.* With sup_n d_n uniformly O(ε), the O(v²) remainder declared at L-1(c) is uniformly bounded along the trajectory; the convolution representation and every lemma L-2…L-5 built on it operate inside the regime M1 licenses at every Moment, which is the C-5(iii) demand. ∎

**Honest boundaries.** (a) κ < 1 is established at MECHANISM grade from M1's exit-at-c/no-return structure; its instrument-grade counterpart is exactly the MEAS-2 support/no-tail leg — **a measured long-time tail at d_DP falsifies L-6's contraction and L-4's support in the same stroke** (one structure, two lemma-level consequences; the cross-falsifier link is registered here). (b) The class 𝒫 excludes fast drives by construction; nothing is claimed for |Δv| beyond Δv_max — the toy's negative control 4 shows the bound genuinely fails there, so admissibility is load-bearing. (c) No value of κ, C, τ_b, v_max, or Δv_max is minted; all appear symbolically, with toy-specific disclosed values only inside the verify script.

**D-KAPPA pointer (v1.3, Patch 3034).** The CONV-013 panel left C-5(iii) unconfirmed and specified deliverable D-KAPPA; the interim measurement record `dkappa_3034_interim_record.md` executed the route-(b) spectral-radius test on the COMMITTED leg dynamics and found: the point-state Jacobian AMPLIFIES (ρ_micro ≈ 2.1–2.6/Moment — this lemma's proof step (ii) is FALSE as worded in that metric); deviations saturate at a perturbation-independent realization-class scale; and a perturbation's late-time trace on the source-felt force equals the independent-realization noise floor (no systematic memory above floor at single-pair resolution). An L-6 metric amendment candidate (contraction at realization-class / systematic-channel level) rides to the panel with the MEAS-3 disposition, where the final κ ≤ 1−δ systematic-channel margin attaches (the registered cross-falsifier already binds the two). The 2990 toy below is SUPERSEDED for the contraction claim (its κ was an input; 3034's measurements are outputs); its checks 2–4 remain valid for what they test.

**Verification.** `code/2990_b1_stationarity_check.py` (4/4): uniform bound across 200 random admissible drives; linearity residual exponent 2.000 (halve the drive, quarter the residual — the regime holds ALONG the trajectory); NEGATIVE CONTROL κ = 1 (memory tail) breaks the bound by secular accumulation; NEGATIVE CONTROL fast drive exceeds the admissible-class bound. Both failure modes are reachable, so the checks are tests, not tautologies.
