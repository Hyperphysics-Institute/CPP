# Round 1 — RECONNAISSANCE ONLY: the exact-emergent-Lorentz root, stated formally

**Patch 2059, 2058-band (campaign owns 2058–2099).** Window opened by the campaign handover
`series_relativity/development/mu_eps_closure/em_emergence/2058_HANDOVER_lorentz_root_campaign.md`.
**Status of this note:** reconnaissance. **NO theorem claim. NO status move. NO THEO.** This file only
(a) pulls the exact PCD rule and exact 600-cell / binary-icosahedral structure *as the corpus states
them*, (b) records the reading of METH-CHIR-CONT-2, and (c) writes the formal exact-Lorentz target plus
the World 1/2/3 criteria. Round 2 (the first real probe — the quaternionic bridge) is NOT begun here.

---

## 0. What was pulled this round (with corpus citations — verbatim where load-bearing)

### 0.1 The exact PCD rule (the dynamics whose symmetry is in question)

**PCD cycle (primitive).** `master_glossary.md` §PCD: *"Perceive-Compute-Displace — the three-phase
agentic cycle executed by each CP at every Absolute Moment: perceive local SSV environment, compute
response per A1–A9 rules, displace to new position."* Distinct from ZBW (the between-CP oscillation in
DPs).

**Absolute Moment (the global tick).** `master_glossary.md` §"Absolute Moment": *"One tick of the cosmic
clock during which every CP executes one PCD cycle. Duration t_P. Time in CPP is discrete and absolute
(not relative)."* This is the object that makes a *preferred slicing* manifest — the symmetry question
is precisely whether the dynamics hide it.

**The GP update / displacement-budget law (SSV-only; the budget split).** SR-1 §"4D→3D Projection"
(`series_relativity/papers/SR-1_special_relativity_emergence.tex`, Eq. 4d_radius_A and following):
the 4D insphere radius decomposes as
  R_4D² = r_3D² + τ²,   with τ = l_P the **fixed, stress-invariant** timelike step (Absolute-Moment
  postulate, Appendix B / c01 absolute-moment-postulate), and r_3D the spatial displacement magnitude.
Under stress the 4D radius contracts by 1/(1 + k·ΔSSV); because τ is invariant, the spatial budget
contracts by the same factor, giving the master relation
  PSR_eff = l_P / (1 + k·ΔSSV).
The continuous velocity gradation enters as **|d_spatial| = l_P·(v/c)** (SR-1 line ~423, the
fine-nesting clause), i.e. the per-Moment budget l_P is *partitioned* between a timelike advance and a
spatial step. Equivalent budget form (handover §4 phrasing): **l_P² = (c·Δτ)² + |d_spatial|².**

**CRITICAL recon finding on SR-1's "exact Lorentz" (flagged so the campaign does not over-lean on it).**
SR-1 establishes γ_CPP = γ_SR **exactly**, but the corpus is explicit that this is the *scalar
γ-magnitude* (time-dilation factor), and that it is recovered **only via the energy–momentum bridge**
(Appendix A.8.1): the *physical identification* of ΔSSV with the relativistic kinetic-energy density
(γ_SR − 1)·mc²/V₀, which gives k·ΔSSV = γ_SR − 1 at Planck normalization. SR-1's own **elimination
theorem (Appendix H.1)** proves that **no purely geometric displacement model recovers the v²/c² scaling
at low velocity** — i.e. pure displacement geometry does *not* give Lorentz; the energy–momentum bridge
is the necessary physical input. Consequence for this campaign: **SR-1 cannot be cited as already having
the root.** It has the boost-magnitude scalar, conditional on a physical identification, on a single
self-field's clock. The root theorem below (continuous SO(3,1) **action on the emergent fields**, with
rigid co-moving stationarity and no drag / no lattice-Cherenkov) is strictly stronger and genuinely open.

**The emergent fields the action must act on (post-A3′).** `master_glossary.md` §"LSP′ (Completed
Lattice State Packet) — Axiom A3′" (registered Patch 1129): the GP→GP broadcast carries **nine dynamical
components** — scalar Φ = |SSV|_abs (icosahedral irrep A, l = 0), vector V_i = SSV_net (T₁, l = 1), and
symmetric-traceless Q_ij (H, l = 2; the radiative/GW tensor) — *"exactly the lattice's rotationally
protected representation content (intact descents are l = {0,1,2} only; no fourth rung)."* These reps are
labelled by the **static** icosahedral group; whether the *dynamics* promote them to carriers of a
*continuous* SO(3,1) is the whole question.

### 0.2 The exact 600-cell / binary-icosahedral structure (as the corpus states it)

SD-2 §"Mathematical Preliminaries: H₄ and the 600-Cell"
(`series_foundations/series_superdeterminism/SD-2_h4_angular_structure.tex`):

- **Polytope.** 600-cell = regular 4-polytope: **120 vertices, 720 edges, 1200 triangular faces, 600
  tetrahedral cells**, coordination z = 12.
- **Static symmetry group.** H₄, the largest non-crystallographic Coxeter group, **order |H₄| = 14400**,
  with descent chain **H₄ ⊃ H₃ ⊃ H₂ ≅ I₂(5)** (H₃ icosahedral, order 120; H₂ pentagon dihedral,
  order 10).
- **Vertex coordinates (exact, in ℚ(φ)):**
    {½(±1,±1,±1,±1)} ∪ {even permutations of ½(0,±1,±φ⁻¹,±φ)}.
  All pairwise inner products lie in ℚ(φ); distinct values {0, ±½, ±1/(2φ), ±φ/2, ±1/φ², ±1}.
- **Adjacency spectrum (six eigenvalues):** λ ∈ {12, 1+φ, φ−1, 1−φ, −φ, −(1+φ)} — the same spectrum
  that selects the EW bosons elsewhere in the corpus.

**The quaternionic / binary-icosahedral fact the campaign needs (standard math; NOT yet corpus-wired).**
The 120 vertices above, taken as unit quaternions, ARE the **binary icosahedral group 2I** (the unit
*icosians*), a discrete subgroup of the unit quaternions S³ ≅ SU(2), |2I| = 120. The corpus states the
*coordinates* and the *Coxeter* symmetry H₄ (order 14400 = 120·120, ≅ (2I × 2I)/±1 acting as
rotations), but a search this round found **no corpus file that makes the vertices-as-2I /
unit-quaternion identification load-bearing**, and none that connects it to an SL(2,ℂ) / Lorentz
presentation. **World 1 therefore has no existing bridge to inherit** — it must be built. (Recorded as a
recon fact, not a claim.)

> **Distinction to keep straight (do not conflate):** the handover §2 phrases the obstacle as "H₄ … is a
> FINITE group and cannot BE the continuous Lorentz group." Precise reading: the *static* symmetry is
> finite at **two** distinct orders — the **order-120 vertex group 2I** (binary icosahedral, the
> quaternionic object relevant to World 1's bridge) and the **order-14400 Coxeter group H₄** (the full
> isometry group). Both are finite; neither can *be* SO(3,1). Exactness, if it exists, comes from the
> **PCD dynamics**, not from either static group.

### 0.3 METH-CHIR-CONT-2 — read in full (the Tier-1 tool for World 2, possibly World 1)

`methods_catalogue.md` §METH-CHIR-CONT-2 "Continuum-Limit Projection Map Φ via Wilson–Fisher Block-Spin
Renormalization at Substrate Cutoff." Verbatim load-bearing content:

- **Object.** A linear map Φ : ℋ^sub → ℋ^cont, the Wilson–Fisher block-spin limit as a → 0 holding
  observable correlation length L fixed, with substrate cutoff Λ_sub = ℓ_edge⁻¹ at the 600-cell edge.
- **Three construction conditions:** (i) **block-spin commutativity** — Φ commutes with discrete
  symmetry actions by construction; (ii) **continuum-limit existence** — Φ well-defined as a → 0 at any
  fixed μ < Λ_sub; (iii) **equivariance** — for any discrete g ∈ I_h, Φ(g·|Ψ^sub⟩) = g^cont·Φ(|Ψ^sub⟩),
  where g^cont is the continuum action of g.
- **Induced operator map:** Φ_* Ô^sub = Φ Ô^sub Φ⁻¹.
- **Dependencies:** substrate residual symmetry H₃ = I_h at host vertex (FI-CHIR-CONT-3); Capotauro v2.0
  Substrate-Locality Theorem (FI-CHIR-CONT-9, preserves locality under block-spin); standard
  Wilson–Fisher machinery.
- **Scope:** any discrete substrate → continuum field theory at μ ≪ Λ_sub; deep-IR regime a/L ≪ 10⁻¹⁵
  at all SM-observable scales.

**Reading for this campaign (recon, not a claim).** METH-CHIR-CONT-2's equivariance condition is exactly
a *discrete-symmetry-in → continuum-symmetry-out* intertwiner. It is built to push the **finite**
icosahedral group I_h through to its continuum action — it does **not, as stated, manufacture a
*larger* continuous group (SO(3,1)) that the discrete input lacked.** So as written it is the natural
**World-2** engine (Lorentz exact in the block-spin/IR limit, with a substrate floor), and its honest
limit is the boundary between World 2 and World 1: for World 1 it would have to be shown that the *PCD
dynamics* enlarge the equivariance group from (image of 2I/H₄) to all of SO(3,1) — which is the thing in
question, not something Φ supplies for free.

### 0.4 The campaign's method (refuse-the-new-axiom) — read

`methods_catalogue/methods_catalogue.md` §METH-L3-004 "Would-be-axiom → extract the constraint, then
build the mechanism": when a step looks like it needs a new axiom, first extract the *exact* structure
the answer must satisfy (here: an exact SO(3,1) action), then build it from existing primitives (PCD +
600-cell) before adding any axiom. Complement §METH-L3-006 "Axiom-necessity by exhaustive route closure":
an axiom earns *necessity* only after every no-axiom route is independently closed (local-polynomial /
emergent-collective / transport-connection), each with its own falsifier. These two govern, respectively,
the refusal-and-attempt and what a complete failed attempt must look like before any axiom is drafted.

---

## 1. The exact-Lorentz target — FORMAL STATEMENT

Let the substrate be the 600-cell GP lattice Λ with the PCD dynamics of §0.1, evolving in discrete
Absolute Moments of duration t_P. Let a **self-field configuration** be a localized excitation of the
emergent LSP′ field
  𝔽(x) = ( Φ(x), V_i(x), Q_ij(x) )            [scalar l=0, vector l=1, symm-traceless l=2; §0.1],
i.e. the assembled metric/field content broadcast GP→GP under A3′. Let 𝔽₀ denote a stationary
rest-frame self-field (a particle at rest on the Grid).

For a boost parameter (β = v/c, n̂) with β ∈ [0,1), n̂ ∈ S², let Λ_β be the PCD evolution of 𝔽₀ under the
budget split l_P² = (c·Δτ)² + |d_spatial|² with |d_spatial| = l_P·β along n̂ (§0.1).

> **TARGET (T) — exact emergent Lorentz, the root.** There exists a map B(β,n̂) acting on the emergent
> field 𝔽 such that:
>
> **(T1) Continuous action.** The family { B(β,n̂) : β ∈ [0,1), n̂ ∈ S² } realizes the **proper
> orthochronous Lorentz group SO⁺(3,1)** as an **exact** action on 𝔽 — closed under composition
> (B(β₁,n̂₁)∘B(β₂,n̂₂) = B(β₃,n̂₃) per relativistic velocity addition) and defined at a **continuum** of
> β and **all** directions n̂, not merely at the finite set of lattice-special boosts.
>
> **(T2) Rigid co-moving stationarity.** A boosted self-field B(β,n̂)·𝔽₀ is, in its co-moving frame, an
> **exact rigidly-translating stationary** configuration: 𝔽(x,T) = 𝔽(x − vT, 0) for all integer numbers
> of Absolute Moments T, with **no Peierls/lattice drag** (no β-dependent or position-dependent restoring
> force pinning the field to lattice sites) and **no lattice-Cherenkov radiation** (no emission into
> lattice modes as the field translates).
>
> **(T3) Isotropy of c.** The emergent signal speed is the same constant c in every boosted frame and
> every direction — equivalently, the dispersion relation seen by 𝔽 is invariant under the B(β,n̂) of
> (T1). [This is the simultaneity-brick / R2 premise (i); §0.1.]
>
> The claim is "**exact at the discrete level**" if (T1)–(T3) hold with the substrate spacing a = ℓ_edge
> kept **finite and nonzero** — i.e. with **exactly zero** O((a/L)ⁿ) violation, no continuum limit taken
> and no Planck-suppressed floor permitted.

**"Exact at the discrete level," made precise.** Write the lattice-induced violation of any of (T1)–(T3)
as a residual 𝓥(β, n̂, a/L). Then:
  - **discrete-exact** ⟺ 𝓥 ≡ 0 identically for finite a > 0, for all β ∈ [0,1) and all n̂ ∈ S²;
  - **limit-exact** ⟺ 𝓥 → 0 as a/L → 0 with 𝓥 = O((a/L)ⁿ), n ≥ 1, but 𝓥 ≠ 0 at finite a;
  - **obstructed** ⟺ 𝓥 is bounded below by a positive, n̂- or β-dependent floor that no choice of
    dynamics on this substrate can remove (a genuine preferred-frame signature).

This residual 𝓥 is the single scalar the budget should pin down. (No numerical or FEM evaluation of 𝓥 is
performed this round; recon only. Per handover §7, any later numerics are consistency-evidence, never
proof.)

---

## 2. The three worlds — decision criteria (formal)

A result is bankable in a given world iff the corresponding criterion is met by a panel-reviewed
argument (not by numerics alone).

**World 1 — clean algebraic bridge (discrete-exact; the big prize).**
*Criterion:* exhibit an explicit homomorphism/representation carrying the **2I (unit-icosian /
quaternionic) structure of the 600-cell vertices** into an **SL(2,ℂ)** (≅ Spin⁺(3,1)) action on 𝔽, and
show the **PCD update intertwines with it** so that B(β,n̂) of (T1) is realized with 𝓥 ≡ 0 at finite a.
Concretely: a map ρ : (PCD-evolved self-field) → SL(2,ℂ)-module with ρ(Λ_β) = (boost generator) acting
exactly, closing the group at a continuum of β. *Falsifier for World 1:* a proof that no such
intertwiner can exist (e.g. a conserved lattice quantity that any B(β,n̂) with β ∉ lattice-special-set
must violate) — which would push to World 3.

**World 2 — fixed-point / continuum-limit emergence (limit-exact; most likely, still a strong win).**
*Criterion:* show via METH-CHIR-CONT-2 (Φ, block-spin to the IR fixed point) that (T1)–(T3) hold with
𝓥 = O((a/L)ⁿ), n ≥ 1, i.e. **Lorentz exact in the emergent/block-spin limit with a Planck-suppressed
violation floor** at the substrate, *and* identify the leading n and the coefficient's parametric size.
This is "exact in the limit, Planck-suppressed floor" — publishable and probably physically correct.
*Boundary with World 1:* World 2 collapses *into* World 1 iff the leading coefficient is shown to vanish
identically (not merely be small) for symmetry reasons — that vanishing, if proved, is the World-1 prize.

**World 3 — obstruction (also a real result).**
*Criterion:* exhibit a concrete invariant of the PCD-on-600-cell dynamics that any exact continuous
SO⁺(3,1) action must violate — a positive lower bound on 𝓥 that is dynamics-independent on this
substrate (e.g. a nonzero Peierls barrier for generic n̂, or a forced lattice-Cherenkov channel above a
β-threshold). *Consequence if World 3:* the substrate has a real preferred frame; undetectability is then
defended operationally (the 2053 simultaneity-brick route), not by exact symmetry.

**Meta-target (the budget can almost certainly settle this even if T does not fall):** a committed
**world-call** (1/2/3) at the Round-15 hard checkpoint, with an honest residual-probability estimate —
not "still looking." A defensible result in ≥ 2 of the 3 worlds is a campaign win (handover §3, §6).

---

## 3. What Round 2 will probe (named here, not begun)

The single highest-information first probe (handover §5): **does the binary-icosahedral → quaternionic
→ SL(2,ℂ) bridge survive contact with the actual PCD update, or die immediately?** Specifically — take
2I ⊂ SU(2) ⊂ SL(2,ℂ); ask whether the PCD displacement law (budget split + A3′ broadcast) is
*covariant* under the boost half of SL(2,ℂ), or whether the fixed Absolute-Moment τ = l_P (the
stress-invariant global tick, §0.1) obstructs the boost generators at the first commutator. That one
check moves the World-1/2/3 probabilities the most. **Not performed in this note.**

---

## 4. Recon ledger (this round)

- Band: campaign owns **2058–2099**; 2058 = handover commit; first free = **2059** (this note). Confirmed
  via `git log` on a fresh clone (BLOCKING CLONE GATE honored).
- Pulled, with citations: PCD primitive + Absolute Moment + GP budget split (SR-1 §4D→3D, c01) ; A3′
  nine-component LSP′ broadcast (master_glossary) ; 600-cell + H₄ + vertex coordinates + adjacency
  spectrum (SD-2) ; METH-CHIR-CONT-2 (methods_catalogue, in full) ; METH-L3-004 + METH-L3-006
  (methods_catalogue subdir).
- Flagged recon findings (facts, not claims): (a) SR-1's "exact Lorentz" is scalar γ-magnitude via the
  energy–momentum bridge, and SR-1's own H.1 elimination theorem shows pure displacement geometry does
  *not* give Lorentz — so the root is genuinely open and SR-1 is not a shortcut to it; (b) the
  vertices-as-2I / quaternionic identification is standard math but is **not yet corpus-wired**, so
  World 1 has no inherited bridge; (c) METH-CHIR-CONT-2's equivariance is discrete-in/continuum-out at
  *fixed* group — it is the World-2 engine, and does not by itself enlarge the group to SO(3,1).
- No theorem registered. No status file touched. No THEO. No proof claim. No numerics run.

*Captured by Claude Opus under Thomas Lee Abshier's direction. Reconnaissance note; consistency-of-record
discipline (handover §7): corrections are appended forward, never overwritten.*
