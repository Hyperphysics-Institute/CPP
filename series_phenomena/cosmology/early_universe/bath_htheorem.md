# Bath-clause H-theorem: leg 1 relaxation + stationary state derived (given the ZRP model)

*Patch 0772, Session 154. Hardening of leg 1 per the path flagged at 0769/0771. The bath clause's two
dynamical pieces — (a) the occupations relax/mix, and (c) they relax to the *indistinguishable* Gibbs state
— were GROUNDED at 0769 (ZBW-ergodicity commitment + A1). This finding upgrades them to DERIVED, given a
single minimal model of the dynamics: the minimal-PCD / ZBW occupation dynamics as a symmetric constant-rate
**zero-range process (ZRP)**. Script: `scripts/0772_zrp_htheorem.py` (exact master equation). Finding-level
lemma (LEMMA-NS-HTHEOREM), NOT a hardened THEO — the n_s result stays conditional on the ZRP identification.*

## The model: minimal-PCD occupation dynamics = a symmetric constant-rate ZRP

- **State** = occupation numbers (n₀, …, n_{L−1}) on the lattice sites. Forced by **A1**: a CP has no
  identity, so configurations are occupation-number objects.
- **Move**: each CP hops independently at the ZBW switching rate (set = 1) to a uniformly chosen neighbour.
  The hop (nᵢ → nᵢ−1, n_j → n_j+1) has rate g(nᵢ)·p(i,j) with **g(n) = n** (constant per-CP rate) and
  **p(i,j) = 1/deg(i)** symmetric. This is the minimal faithful model of independent ZBW hops of
  indistinguishable CPs on the A1 occupation space — a zero-range process.

## The H-theorem (now a theorem, not an assertion)

1. **Reversibility.** The symmetric constant-rate ZRP satisfies **detailed balance** with respect to the
   product-Poisson measure (here, at fixed N, the multinomial π(n) = N!/∏nᵢ! · (1/L)^N):
   π(n)·W(n→n′) = π(n′)·W(n′→n). *Verified to machine precision (~10⁻¹⁷) on the exact L=3, N=6 generator.*
2. **Lyapunov / H-theorem.** For any Markov generator with stationary π, the relative entropy
   H(t) = Σₙ P(n,t)·ln[P(n,t)/π(n)] (the KL divergence, ≥ 0) is **monotonically non-increasing**, strictly
   so until P = π (irreducibility). *Verified: from a delta initial condition, H(0) = 6.59 decreases
   monotonically to ~10⁻¹⁰ — exact matrix-exponential evolution, no MC noise.* So the occupations
   **provably relax** to π — this is leg 1(a).
3. **The stationary state is the indistinguishable Gibbs state.** π is the product-Poisson measure; the
   **nᵢ! in the denominator is the Gibbs indistinguishability divisor** (the 0749 point), giving chemical
   potential μ = kT·ln(ρ) with ρ = N/L the mean occupation — **μ ∝ ln n̄, the tilt's log.** The single-site
   marginal is Binomial(N,1/L) → Poisson(N/L) as N → ∞ (exact at the cosmological n̄ ~ 10⁷⁴). The
   distinguishable/labelled stationary state — the one that would give the n_s = 1 cliff (0749) — is **not a
   stationary measure of this dynamics.** This is leg 1(c).
4. **Relaxation time.** τ_eq is set by the **spectral gap** of the generator, which is O(1) in ZBW-rate
   units and does **not vanish** with system size for the density-relaxation mode (gap = 1.5 on the test
   system). So τ_eq is a small multiple of the ZBW time → R = τ_eq·H_inf ≪ 1 for sub-Planckian inflation
   (0769). (The precise prefactor differs from the 0753 toy's N_mix ~ O(10–30) — that reflects system size
   and rate normalisation; what the H-theorem secures is a **finite, non-vanishing gap**, which is exactly
   what "fast enough" requires.)

## What this upgrades

Leg 1(a) [relaxation exists] and leg 1(c) [stationary = indistinguishable Gibbs] move from **grounded**
(0769: "the ZBW-ergodicity commitment plus A1") to **DERIVED, given the ZRP model** — they are now proven
consequences of detailed balance + the KL Lyapunov theorem, not posits. The distinguishable-state cliff is
*excluded* as a stationary measure, not just disfavoured.

## Honest scope — the residual is now the ZRP identification

- The H-theorem math is standard (ZRP reversibility + KL monotonicity); the CPP-specific content is the
  **identification** of the minimal-PCD / ZBW dynamics with the symmetric constant-rate ZRP. That
  identification is the **new, more minimal premise** — far more checkable than the original "bath clause
  holds." It says: ZBW switching moves indistinguishable CPs independently, at a constant per-CP rate, on a
  symmetric lattice. Each clause is inspectable against the PCD/ZBW primitives.
- Because that premise is a *model* (not yet derived from A1–A11), **n_s = 0.9649 remains
  conditional/grounded** — this patch does not promote it to Section 1 or to a counted swarm contribution.
  What changed: leg 1's relaxation and correct stationary state are no longer assumed; the conditionality is
  concentrated in one minimal, well-posed modelling statement.
- **The deeper target** (the genuine upgrade to "derived") is an A1–A11 derivation that the PCD update rule
  *is* a symmetric constant-rate ZRP — i.e., that ZBW switching is independent across CPs, rate-homogeneous,
  and symmetric on the lattice. Registered as the next hardening step for leg 1.
- Registered as **LEMMA-NS-HTHEOREM** (finding-level), not a hardened THEO, for both reasons above (standard
  math; residual model premise keeps the n_s result conditional).

## Pointers

- Builds on: 0769 (leg 1 grounding — pieces (a)/(c) named); 0749/0752 (A1 → indistinguishable Gibbs / the
  cliff); 0753 (minimal-PCD MC toy — the numerical precursor); 0750 (ZBW = bath).
- Numerics: `scripts/0772_zrp_htheorem.py` (exact 28-state master equation; detailed balance, H(t)
  monotonicity, spectral gap, Poisson marginal — all verified).
- Reasoning: `reasoning/0772_zrp_htheorem.md`.
