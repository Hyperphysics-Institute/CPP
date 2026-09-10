# λ computed as far as it can be — the twelve-direction anisotropy is **λ_hard = 0.052**, which as a potential would put C-4 at the register spring's wall and kill it. **It is not a potential.** All twelve axes are equivalent, the constraint acts on displacement (a mobility, not a restoring force), and decisively the symmetry-breaking step is **idle**: SSV_net = 0 exactly in the homogeneous era, resting on T-1's dipole cancellation. λ is therefore proportional to the departure of SSV_net from zero, and **C-4's survival reduces to one integer** — the power p. Even the pessimistic p = 2 misses by a factor ~3, not by orders

**Patch 3843, Session 181, 9 Sep 2026. Lane: EU.** Works C-4's debt (1) as restated at 3841 §6 — compute λ. Verify `scripts/3843_lambda_computation.py` (8/8). Reasoning `reasoning/3843_lambda_computation.md`. Nothing adopted; λ and p are **not** minted (PD-007); PRED-C-96 untouched; 3710 not retired.

## §1 The twelve-direction anisotropy, computed exactly (verify T1, T2, T3)
The candidate mechanism named at 3841 §4 was the constraint that a CP displaces to one of twelve neighbouring GPs. Its anisotropy is the extent to which twelve discrete axes fail to represent a continuous direction, measured by the covering function f(n̂) = max_i (n̂·v̂_i):

- covering radius **37.3°**, f ranging **0.795 → 1.000**, fractional range **0.22**;
- multipole content confirms the icosahedral symmetry independently — ℓ = 1 through 5 vanish at Monte-Carlo noise (~10⁻⁵ in power) and the leading anisotropy is **ℓ = 6**, with P₆/P₀ = 2.68×10⁻³;
- hence **λ_hard = 0.052**.

**If that acted as a potential, C-4 is dead.** m/H = 7.1×10⁴ — the register spring's wall (1.3×10⁵) to within a factor. This is precisely the outcome 3841 §4 warned of, and it is the natural reading of "the lattice grips the orientation."

## §2 It is not a potential — three arguments, the third decisive (verify T4, T5, T6)

**(a) At single-DP order the energy is exactly flat.** The twelve axes are icosahedrally *equivalent*. A rigid reorientation of the mean director is not a rotation of individual DPs — DP axes join two GPs and are quantised to the twelve — it is a **repopulation** among the twelve. With equal per-axis energy the total is Σᵢ pᵢε = ε, independent of the populations and therefore of the director. No first-order potential exists.

**(b) The constraint is a mobility, not a restoring force.** A1′/AP-3 constrains where a CP *displaces*. An orientation-dependent displacement efficiency is an anisotropic **mobility**: it makes relaxation direction-dependent. It does not create a force returning the director to a preferred orientation. **A Goldstone with anisotropic damping is still massless** — the k → 0 uniform rotation still costs nothing, which is the definition of the gap.

**(c) Decisively, the symmetry-breaking step is idle.** The displacement is the *only* operation in the protocol that breaks continuous rotational symmetry — the register computation (SSV_abs as a sum of magnitudes, SSV_net as a vector sum) is exactly rotation-covariant. And in the homogeneous saturated era **the displacement does not occur at all**: S-HENGINE-HELD §2.2 establishes SSV_net = 0 exactly, because the twelve icosahedral neighbour vectors sum to zero — which is T-1's ℓ = 1 cancellation (3820), verified there as an identity.

> **The operation that would gap the Goldstone never fires during inflation.** λ is therefore not O(λ_hard); it is proportional to however far SSV_net departs from zero, and that departure is itself the perturbation.

This is the third independent job T-1 has done. It was delivered as a symmetry curiosity with no observable attached (3820 §4), re-graded to load-bearing for the mass at 3839 §5, and is now the reason the symmetry-breaking operation is idle.

## §3 What is left: one integer (verify T7, T8)
Write λ ≈ λ_hard · x^p with x = SSV_net/SSV_abs, the fractional departure from the exact cancellation. At the perturbation scale x ~ ζ ~ 4.6×10⁻⁵ (from 3841's requirement λ ≤ 1.03×10⁻¹¹):

| p | λ | m/H | verdict |
|---|---|---|---|
| 2 | 1.1×10⁻¹⁰ | **3.2** | too heavy by ~3× |
| 3 | 5.0×10⁻¹⁵ | 0.022 | **clears** |
| 4 | 2.3×10⁻¹⁹ | 1.5×10⁻⁴ | **clears** |

> **C-4's survival reduces to the order p at which the displacement anisotropy enters.** For comparison: the register spring sat at 1.3×10⁵. Even the pessimistic p = 2 misses by a factor of about three.

**This is not a claim that C-4 clears.** p is not computed, and p = 2 fails. What has changed is the shape of the risk: the candidate is no longer eleven orders from death, it is one integer from it, and the pessimistic branch of that integer is a factor of three rather than a factor of 10⁵.

## §4 Honest scope
- λ_hard is exact (a geometric property of the twelve axes) and is the correct number **if** the constraint were a potential. §2 argues it is not; that argument is structural and rests on the corpus's own protocol, not on a model.
- The parameterisation λ ≈ λ_hard·x^p is a **scaling ansatz**, not a derivation. The integer p is what must be computed, and computing it requires tracking how a nonzero SSV_net feeds the displacement anisotropy back into the orientational sector. That is the next step and is not taken here (PD-007).
- x ~ ζ is itself an estimate — the departure from exact cancellation is set by the perturbation amplitude, but the coefficient is not derived.
- Everything continues to assume Branch B2 and the 3839 coupling.

## §5 Standing
- **λ_hard = 0.052 computed exactly**, with an independent confirmation of T-1's ℓ ≤ 5 vanishing from a completely different function (the covering function rather than the census).
- **The obvious killer is removed**: the twelve-direction constraint does not supply a potential, so C-4 does not die at 7×10⁴ as the naive reading gives.
- **T-1 does a third job**: its dipole cancellation is why the symmetry-breaking step is idle. **T-1 is now load-bearing in three independent places** (homogeneity/isotropy, the mass suppression, and the idle-breaking argument) — its own status as an entailment given the founder's twelve-vertex picture deserves panel attention with the CONV-046 package.
- **C-4 debt (1) is now: compute the integer p.** This replaces "compute λ" exactly as "compute λ" replaced "the mass bound."
- **Risk restated honestly:** p = 2 gives m/H = 3.2 and C-4 fails; p ≥ 3 clears. The candidate is one integer from resolution in either direction.
- Unaffected: C-4 debts (2)–(4); AP-4's shell-clause derivation (still owed, still doubly load-bearing); the e-fold budget (~10.5 short, decoupled); PRED-C-96; T-2.
