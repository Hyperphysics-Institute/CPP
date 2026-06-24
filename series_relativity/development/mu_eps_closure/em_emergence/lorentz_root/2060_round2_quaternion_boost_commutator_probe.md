# Round 2 — first real probe: does the 2I → SL(2,ℂ) boost half survive the PCD update?

**Patch 2060, 2058-band.** Campaign: exact-emergent-Lorentz root (handover 2058). Builds on the Round-1
recon note `lorentz_root/2059_round1_recon_exact_lorentz_target.md`.
**Status:** FINDING from the first real probe. **Panel-pending — NOT banked. NO THEO. NO status move. NO
proof claim.** Numerics in `verify/2060_addition_law_signature.py` are consistency-evidence only
(handover §7; the 2055-overclaim fence). The world-call is NOT made here; it is made at the Round-15 hard
checkpoint.

---

## 0. The probe, precisely

Round-2 question (handover §5): *does the binary-icosahedral → quaternionic → SL(2,ℂ) bridge survive
contact with the actual PCD update, or die immediately — specifically, does the fixed Absolute-Moment
τ = l_P obstruct the boost generators at the first commutator?*

The World-1 prize requires (Round-1 §2, criterion W1): an explicit map carrying the **2I (unit-icosian /
quaternionic) structure of the 600-cell vertices** into an **SL(2,ℂ) ≅ Spin⁺(3,1)** action on the LSP′
field 𝔽 = (Φ, V_i, Q_ij), such that the **PCD update intertwines with the boost generators**. So the
probe is sharp: take the boost half of SL(2,ℂ) and ask whether the PCD displacement law (the budget
split + A3′ broadcast) can carry it exactly.

## 1. Result in one line

**The naive static-geometric quaternion bridge dies at the first commutator.** The boost the PCD
*budget split* manufactures is a **compact Euclidean rotation** (real form so(4)), not a non-compact
Lorentz boost (real form so(3,1)). The fixed Absolute-Moment τ = l_P is exactly the obstruction: it
enters the budget as a **+ (positive-definite) quadrature term**, which forces the compact real form.
The probe therefore **moves the world-probabilities sharply** and relocates the entire World-1/2 question
from *static geometry* to *broadcast causality*. Detail below.

## 2. Step 1 — where 2I sits in SL(2,ℂ) (kills the bridge before the dynamics even enter)

The 120 vertices of the 600-cell, as unit quaternions, are the binary icosahedral group **2I ⊂ S³ ≅
SU(2)** (Round-1 §0.2). In the Lorentz double cover,
  SL(2,ℂ) = SU(2) · {boosts},   (polar decomposition: A = U·P, U ∈ SU(2), P = exp(½ η n̂·σ) Hermitian
  positive, det 1).
SU(2) is the **maximal compact subgroup**; the boosts P are the **non-compact** Hermitian-positive
directions (eigenvalues e^{±η/2}, not on the unit circle). **Every element of 2I is unitary** (a unit
quaternion ↔ an SU(2) matrix), so

> **2I contains no boost. The vertex group lies entirely inside the rotation (compact) half of SL(2,ℂ)
> and touches the boost directions nowhere.**

So the static vertex algebra gives, at most, the **rotation** half. The boost half cannot come from the
vertices; it must be manufactured by the **PCD dynamics**. The probe thus reduces to: *does the PCD
update supply the missing non-compact (boost) directions?*

## 3. Step 2 — the boost the PCD budget split actually manufactures is COMPACT

The PCD displacement law (Round-1 §0.1; SR-1 §4D→3D) partitions the fixed per-Moment budget l_P as
  **l_P² = (c·Δτ)² + |d_spatial|²,   |d_spatial| = l_P·β.**
Hence (c·Δτ, |d_spatial|)/l_P = (√(1−β²), β), a point on the **unit circle**. The transformation taking
rest (β=0) to velocity β, preserving this **positive-definite** form, is therefore a **Euclidean
rotation** in the (c·Δτ, d_spatial) plane by angle
  **α = arcsin β,**
whose generator is the **antisymmetric** M = [[0,−1],[1,0]] with **M² = −I** (compact, circular). This
is *not* a Lorentz boost, whose generator is the **symmetric** N = [[0,1],[1,0]] with **N² = +I**
(non-compact, hyperbolic, β = tanh η).

The single invariant **sign of the generator square** (M² = −I vs N² = +I) is the entire difference
between the two real forms. The budget split, being a 4D-insphere (++++) relation, hands you M.

### 3.1 The first-commutator / composition diagnostics (three smoking guns; `verify/2060`)

1. **Collinear composition (the cleanest observable).** Composing two budget-split boosts gives the
   **circular** addition β₃ = β₁√(1−β₂²) + β₂√(1−β₁²), **not** the relativistic
   (β₁+β₂)/(1+β₁β₂). Numerically (verify §3): β₁=β₂=0.6 → Euclid 0.960 vs Lorentz 0.882; they diverge at
   O(β³).
2. **Finite-composition reach of c (a hard kill).** Two equal Euclidean boosts at **β = 1/√2** compose to
   **exactly β₃ = 1** — the circular law reaches the speed of light at *finite* composition, and is
   **non-monotone** beyond it (compose(0.9,0.9) = 0.785 < 1). A Lorentz boost can never reach c:
   (β+β)/(1+β²) < 1 for all β < 1. The budget-split "boost" therefore violates the structure of a boost
   group outright.
3. **Real-form / commutator sign.** Embedding the (t,x) and (t,y) boosts, the boost–boost commutator
   lands on the (x,y) rotation block with **opposite sign** for the two readings (verify §5): the
   Euclidean pair closes with the **compact** sign, the Lorentz pair with the **non-compact** sign — the
   concrete [K_i,K_j] = +J (so(4)) vs −J (so(3,1)) distinction. This is the "first commutator" the
   handover named, and the budget-split route lands on the wrong side of it.

### 3.2 The obstruction is exactly the fixed τ = l_P, and it is corroborated internally

τ = l_P is the **stress-invariant, universal** Absolute-Moment step (Round-1 §0.1). It enters the budget
as a **+τ² quadrature term** (R_4D² = r_3D² + τ², SR-1 Eq. 4d_radius_A) — the **Euclidean** signature.
To get a Lorentz boost you need τ to enter an **indefinite** form with a **− sign** (the Minkowski
interval). A positive-definite form's isometry group is the **compact** SO(4); only an indefinite
(+−−−) form gives SO(3,1). So *the fixedness of the Moment, expressed as a +-quadrature length, is
precisely what pins the static geometry to the compact real form.*

This is independently corroborated by the corpus: SR-1's own **Appendix H.1 elimination theorem** proves
no purely geometric displacement model recovers the v²/c² scaling, and SR-1 must inject the Lorentz
factor through the **energy–momentum bridge** (A.8.1), i.e. by *hand* via the physical identification of
ΔSSV with relativistic KE (Round-1 §0.1, flagged finding (a)). Our probe explains *why* H.1 must hold:
the geometry is Euclidean, so its boosts are circular, so it cannot carry the hyperbolic law — exactly
H.1's content, now with a structural reason.

## 4. Where the minus sign must live (the live route — and Round 3's target)

The probe does **not** kill Lorentz emergence; it kills **one specific World-1 path** (the static
quaternion-bridge boost). It also tells us precisely where to look next. Note that the **Minkowski
interval is already latent** in the Grid frame: with the **fixed global tick** as the timelike leg and
the **light-cone bound** |d_spatial| ≤ c·t_P (i.e. β ≤ 1),
  **ds² = (c·t_P)² − |d_spatial|² = (c·t_P)²(1−β²) = (c·t_P/γ)²  = (c·Δτ_proper)²,**
the correct **proper time**, with a **− sign**. The crucial observation:

> The Lorentzian (−) signature does **not** come from the static insphere geometry (which is ++++); it
> comes from the **causal** relation between the universal Absolute-Moment tick and the spatial step —
> the **light-cone** |d_spatial| ≤ c·t_P. In CPP that causal structure is carried by the **retarded
> A3′ GP→GP broadcast** (the "perceive" phase reads the backward light-cone of incoming broadcasts), not
> by the budget partition.

So the genuine boost generator, if it exists, must be **N (hyperbolic, N²=+I) built from the retarded
broadcast kernel**, not **M (circular) built from the budget-partition angle**. Whether the **PCD
dynamics actually select N over M** — whether the retarded broadcast knows the Minkowski interval rather
than only the Euclidean budget — is the open question.

**Round-3 probe (named, not begun):** construct the boost candidate from the **A3′ retarded broadcast
kernel** (the causal cone of the perceive phase), and test the same three diagnostics (generator square,
collinear addition, commutator sign). If it returns N²=+I and tanh-addition → the minus sign is dynamical
and World 1/2 via the causal route is live; if it too returns the +-quadrature/compact structure → strong
World-3 (obstruction) evidence: the substrate is genuinely Euclidean with a real preferred frame.

## 5. Effect on the world-probabilities (informal; the committed call is at Round 15)

- **World 1 via the static-geometric quaternion bridge:** near-killed. 2I is compact; the budget-split
  boost is compact; the bridge lands in so(4), not so(3,1). This was the "big prize, fall almost
  embarrassingly" path — it does **not** fall this way.
- **World 1 / World 2 via the causal A3′-broadcast route:** now the **single live hypothesis** for
  exact (or limit-exact) Lorentz. The probe has *relocated* the question, not closed it.
- **World 3 (obstruction):** gains a **concrete, sharp candidate** — if the retarded broadcast also fails
  to supply the − sign, the Euclidean budget signature is the obstruction and the preferred frame is
  real. There is now a definite test that would establish World 3.

This is precisely the "single probe that shifts the world-probabilities most" the handover asked Round 2
to be: it removes the most seductive World-1 path and sharpens the remaining fork to one mechanism (causal
broadcast) with one decisive question (does it carry N²=+I?).

## 6. Discipline ledger (this round)

- Band: 2058–2099; 2059 = Round-1 recon (on origin); this = **2060**, first free. Built on origin HEAD
  06afdb8 after refresh (clone-and-grep gate honored).
- Bundle (reasoning-capture rider): this finding + verbatim reasoning fragment
  `em_emergence/reasoning/2060.md` + verify script `lorentz_root/verify/2060_addition_law_signature.py`.
- Numerics: consistency-evidence ONLY; not proof (handover §7). No FEM. No collapsed residuals.
- **No theorem. No status file touched (R2-STATUS, SR.md, CONJ.md, registries all untouched). No THEO.**
  Finding is **panel-pending**: recommend CONV-001 dispatch (ChatGPT, Grok, Gemini, Copilot) to
  pressure-test the real-form argument and the "minus-sign-lives-in-the-broadcast" relocation before any
  world-probability update is recorded.
- Honest scope: this probe kills the *naive static quaternion-bridge boost*, nothing more. Lorentz
  emergence via the causal route remains fully open; the world-call is deferred to Round 15.

*Captured by Claude Opus under Thomas Lee Abshier's direction. Corrections appended forward, never
overwritten (handover §7).*
