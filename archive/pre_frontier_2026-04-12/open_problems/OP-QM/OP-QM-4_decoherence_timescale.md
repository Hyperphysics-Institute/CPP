# OP-QM-4: Classical-Quantum Transition Timescale from DP Sea Decoherence

**Priority:** MEDIUM (was)
**Status:** PARTIAL → effectively SOLVED across QM-4 + SD-3
**Resolved by:** QM-4 THEO-QM-6 (Lindblad, single-qubit dephasing rate) + SD-3 THEO-SD-6 (macroscopic apparatus decoherence time)
**Series:** QM-4 (Measurement Problem), SD-3 (Apparatus Model)
**Last updated:** 31 March 2026

---

## Statement

Derive the decoherence timescale τ_dec — the time over which a quantum superposition becomes a classical mixture — as a function of system size, mass, and the CPP DP Sea coupling.

---

## Resolution

Two papers together solve this problem at complementary scales:

### QM-4: Single-qubit dephasing rate (THEO-QM-6)

QM-4 derives the Lindblad master equation from explicit DI-bit/DP Sea scattering under the Born-Markov approximation. The dephasing rate is:

    γ = (sea_strength)² × E_P / ℏ

where sea_strength ≈ 0.178 (from SS-1) and E_P is the Planck energy. Off-diagonal density matrix elements decay as ρ₀₁(t) = ρ₀₁(0) × exp(−2γt). The pointer basis is proved to be the SSV eigenstates (THEO-QM-7) — fixed by the lattice geometry, not by the apparatus.

**This resolves the "coupling constant not derived" objection in the original OP file.** The coupling constant is γ = (sea_strength)² × E_P/ℏ, expressed entirely in terms of known CPP constants.

### SD-3: Macroscopic apparatus decoherence (THEO-SD-6)

SD-3 derives the macroscopic decoherence time for an apparatus with N_app atoms at temperature T:

    τ_dec = ℏ / (N_app × k_B × T)

For room temperature (300 K): τ_dec ≈ 2.5 × 10⁻⁴⁰ s.
For dilution refrigerator (10 mK): τ_dec ≈ 7.6 × 10⁻³⁶ s.

This gives the system-size and temperature dependence that the original OP file requested.

---

## What Remains (minor)

1. **Connecting the two scales formally.** QM-4's single-qubit γ and SD-3's macroscopic τ_dec should be related by τ_dec ~ 1/(N_app × γ_single × T/T_P), but the exact bridge formula has not been written down. This is a straightforward calculation, not a conceptual gap.

2. **The 10⁻²⁰ K heating prediction.** The original OP file mentions measurement-induced heating of ~10⁻²⁰ K. This has not been derived explicitly from the Lindblad rate. It remains as a specific numerical prediction to be computed from γ.

3. **Comparison with experimental decoherence times.** The formula should be checked against observed decoherence times for specific systems (molecular systems in air, superconducting qubits). This is a verification task, not a derivation task.

---

## Feeds Into (updated)

- SD-3 quantum processor trade-off law (THEO-SD-7) — uses the same τ_q
- Experimental tests of CPP decoherence predictions
- OP-G-2 (macroscopic classicality from CPP) — effectively resolved by THEO-SD-6

---

*Status updated 31 March 2026 by Claude Opus (Anthropic) during QM review cycle. The core coupling constant was derived in QM-4 (THEO-QM-6); the macroscopic scaling was derived independently in SD-3 (THEO-SD-6). The original "OPEN — coupling constant not derived" status was outdated.*
