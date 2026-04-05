# Mechanism — QM-3: Entanglement and Bell Inequality Violation

**Paper:** QM-3 (cpp2040c_v31.tex)
**Last updated:** 31 March 2026

---

## Part 1: Spin-½ from ZBW Helix

**Step 1 — The ZBW helix encodes spin direction.**
A spin-½ CP aggregate traces a ZBW helix on the 600-cell lattice (C4, SM-1). The helix axis defines the spin quantisation axis. The two-component DI-bit state at each site carries the ZBW phase, encoding the spin direction as a phase relationship between the two components:

    |ψ⟩ = α|↑⟩ + β|↓⟩,   |α|² + |β|² = 1

where |α|² and |β|² are the DI-bit densities in the up and down helix modes respectively.

---

## Part 2: The Singlet State Is Non-Separable

**Step 2 — A two-CP system created in total-spin-zero has a non-separable DI-bit state.**
When two spin-½ CP aggregates are created simultaneously in a spin-zero configuration, the Nexus enforces total phase circulation = 0 globally. This forces the joint DI-bit state:

    |Ψ⁻⟩ = (1/√2)(|↑⟩_A|↓⟩_B − |↓⟩_A|↑⟩_B)

THEO-QM-3 (Non-separability): This state cannot be written as |φ_A⟩ ⊗ |φ_B⟩ for any single-particle states |φ_A⟩ and |φ_B⟩. Proof: assuming separability leads to a contradiction with the total-spin-zero constraint. The non-separability is a mathematical consequence of the Nexus's global phase constraint — entanglement is not a spooky action at a distance but a global constraint built into the lattice dynamics.

---

## Part 3: Bell Inequality Violation

**Step 3 — The singlet correlation function matches the quantum prediction exactly.**
When Alice measures along axis â and Bob along b̂, the joint DI-bit density for the singlet gives:

    E(â, b̂) = −cos(θ_AB)

where θ_AB is the angle between â and b̂. This is the standard quantum correlation function, derived from the ZBW helix phase relationship and the Nexus constraint — not postulated.

**Step 4 — The CHSH inequality is maximally violated.**
THEO-QM-4 (Tsirelson bound): At angles 0°, 90°, 45°, −45°:

    S = E(â,b̂) + E(â,b̂') + E(â',b̂) − E(â',b̂') = −2√2,   |S| = 2√2

The Tsirelson bound |S| ≤ 2√2 is saturated, consistent with all quantum mechanical predictions. The classical Bell bound |S| ≤ 2 is violated by the non-separable DI-bit structure — the Nexus global constraint allows correlations stronger than any local hidden variable model.

---

## Part 4: The Nexus Is Not an LHV

**Step 5 — The Nexus is not a local hidden variable.**
The Nexus operates atemporally — it enforces the global phase constraint at every Absolute Moment simultaneously, without any signal propagating between Alice and Bob's measurement sites. THEO-QM-5 (No-signaling): Alice's marginal probability P(A=+1) = 1/2 regardless of Bob's measurement axis, and vice versa. This is proved directly from the marginal of the singlet density matrix. The Nexus satisfies the no-signaling condition despite being non-local — it is a constraint, not a signal.

**Step 6 — Lattice corrections are negligible.**
The 600-cell lattice introduces corrections to the correlation function at order (l_P/d)², where d is the separation between Alice and Bob. For any macroscopic separation, these corrections are ~ 10⁻⁶⁶ per metre and completely unobservable.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Step 1: spin-½ from ZBW helix | §2 (Spin-½ Qubit from ZBW Helix) |
| Step 2: singlet non-separability | THEO-QM-3, §3 |
| Steps 3–4: correlation and CHSH | THEO-QM-4, §4–5 |
| Step 5: Nexus is not LHV | THEO-QM-5, §7 (Why the Nexus is not an LHV) |
| Step 6: lattice corrections | §8 (Lattice Corrections) |
