# Mechanism — QM-2: Superposition and Interference from Multi-Path DI-Bit Propagation

**Paper:** QM-2 (cpp2040b_super_v31.tex)
**Last updated:** 31 March 2026

---

## Part 1: Multi-Path Propagation

**Step 1 — A DI-bit emitted from source vertex s propagates simultaneously along all geodesics.**
In CPP, a DI bit emitted from source vertex s on the 600-cell lattice does not follow a single path to detector vertex d. The Nexus enforces DI-bit number conservation globally — each bit propagates along all available paths simultaneously, with each path contributing a complex amplitude. This is not a postulate of path superposition; it is the consequence of the Nexus conservation law applying to all paths at once.

**Step 2 — Each path k accumulates a deterministic geometric phase φₖ.**
Along path k of length nₖ edges, the DI bit accumulates phase φₖ = nₖ × m_CP × c × l_P / ħ. Since l_P and t_P are fixed (AXIM-2, AXIM-6), and c = l_P/t_P (SR-1 Theorem A.8.2), the phase is determined entirely by the path length — no free parameters.

**Step 3 — The total amplitude is the sum over all paths.**
The complex amplitude at detector vertex d:

    ψ(d) = Σₖ A₀ e^{iφₖ}

where A₀ is the amplitude per path (uniform by isotropy of the 600-cell). This is the discrete Feynman path integral on the 600-cell lattice, derived from the Nexus conservation constraint rather than postulated.

---

## Part 2: Interference and the Born Rule

**Step 4 — Constructive and destructive interference arise from phase differences.**
When multiple paths to d have similar phase (Δφ ≈ 0), they add constructively: |ψ(d)| is large. When they have opposite phase (Δφ ≈ π), they cancel: |ψ(d)| ≈ 0. This is the CPP account of quantum interference — not a wave-like spreading of a particle, but the deterministic phase accumulation along multiple simultaneously-propagating DI-bit paths.

**Step 5 — The Born rule follows from DI-bit density.**
The detection probability at d is proportional to the DI-bit number density: P(d) = |ψ(d)|² = ρ(d). The Born rule is not a separate postulate in CPP; it is the statement that detection probability equals DI-bit density, which follows from the definition ψ = √ρ × e^{iφ} (Step 1 of QM-1).

---

## Part 3: SSV as Which-Path Information

**Step 6 — SSV disturbance along a path destroys phase coherence.**
When the DP Sea along path k is disturbed by an SSV perturbation (e.g., by a measurement device), the phase φₖ acquires a random component. The complex amplitudes from different paths no longer sum coherently. The interference pattern disappears — the which-path information has been encoded in the DP Sea, destroying the phase relationship between paths. This is the CPP account of the quantum eraser: SSV perturbation tags paths, and removing the tag (reversing the DP Sea perturbation) restores the interference pattern.

---

## Mathematical Correspondence Index

| Mechanism step | Paper element |
|----------------|--------------|
| Steps 1–3: multi-path amplitude | §2 (DI-Bit Multi-Path), §3 (Total Amplitude) |
| Steps 4–5: interference and Born rule | §3, §4 (Born Rule from DI-Bit Density) |
| Step 6: SSV which-path and eraser | §5 (SSV as Which-Path Tag), §6 (Quantum Eraser) |
