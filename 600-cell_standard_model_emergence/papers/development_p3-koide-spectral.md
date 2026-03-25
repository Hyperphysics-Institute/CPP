# Development Log: Paper 3 — K3 Spectral Theorem and Koide Formula
# `600-cell_standard_model_emergence/papers/paper_3_k3_spectral_theorem_koide_formula.tex`

**Session date:** 24 March 2026  
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)  
**Opus review:** Claude Opus (Anthropic) — pre-submission evaluation  
**Status:** Theorem proved (conditional); three postulates open; lepton masses blocked on θ derivation

---

## Session Summary

This session derived the **K3 Spectral Theorem**: the Koide relation
K = 2/3 for the three charged lepton masses follows from the adjacency
spectrum of the colour cage base graph K3 (the equilateral triangle
{V1, V2, V3}), given three physically motivated postulates.

This is the central result for Paper 3. It connects two prior results
(Theorem 1 from Paper 1: δ=1/3; the K=2/3↔ρ=√2 algebraic identity
from this session) into a single derivation from the cage geometry.

---

## What Was Attempted and What Was Found

### 1. Lorentz-ZBW mass mechanism (explored, partially productive)

**Motivation (Thomas):** ZBW DP oscillator mass contributions should be
Lorentz-dependent, with tighter orbital radii at higher kinetic energy.

**What was derived:**
- The algebraic identity K = (1 + ρ²/2)/3 from the Koide
  parametrisation √m_i = A(1 + ρ cos φ_i) with C3 phases.
- K = 2/3 ↔ ρ = √2 exactly (no approximation).
- The critical point: at (ρ,θ) = (√2, 3π/4), the electron mass
  vanishes. The SSV coupling shifts θ below 3π/4, generating m_e.
- Near-miss: θ_Koide ≈ (1-δ)·arccos(-1/3) + δ·π to 0.19%, where
  δ = 1/3 from Theorem 1. Connects Koide phase to cage geometry.

**What was NOT derived:**
- The coefficient 5/4 in θ = 3π/4 - (5/4)sea² was FITTED, not derived.
  Opus caught this explicitly. The mass "predictions" from this formula
  used the fitted coefficient — they are not first-principles predictions.
- WHY ρ = √2 from the Lorentz mechanism — no physical principle from
  P1–P6 forces ρ to this value.

**Eigenmode calculation verdict (Opus recommendation, carried out):**
- The ZBW spherical-box eigenmode calculation with cage boundary
  conditions gives m_i ∝ 1/R_i (particle-in-a-box limit).
- With R_e = λ_C(e) ≈ 386 fm (Compton wavelength) and
  R_μ = r_conf ≈ 0.4 fm (tetrahedral cage), the ratio gives
  m_μ/m_e ≈ 965, not 207. The cage-radius mechanism is FALSIFIED.
- Root cause: the electron has no cage boundary at the confinement
  scale. Its radius is self-referential through its own mass.

### 2. K3 adjacency spectrum — Path B (the productive path)

**Observation:** The base triangle K3 = {V1, V2, V3} has adjacency
eigenvalues +2 (once, bonding) and -1 (twice, antibonding).

**Key computation:**
  ρ² = λ_max / |λ_min| = 2/1 = 2  →  ρ = √2

Combined with the algebraic identity K = (1+ρ²/2)/3:
  K = (1+1)/3 = 2/3  ✓  (exact)

**The derivation is exact, not approximate.** The spectral ratio 2:1
comes from the complete graph K3 having N=3 vertices. This is verified
to machine precision (λ_max = 2.000000000000, λ_min = -1.000000000000).

**Additional result — K = 2/3 is unique to N=3:**
For K_N: eigenvalues N-1 (once) and -1 (N-1 times).
Applying equipartition: K = (N+1)/(2N).
  K_2 → K = 1/2,  K_3 → K = 2/3,  K_4 → K = 5/6.
Only the triangle gives K = 2/3. The three-colour structure of
the cage base is specifically required — any other vertex count
gives a different Koide ratio.

### 3. The three postulates (status after Opus review)

Opus identified a hidden equipartition assumption in the v1 proof.
v2 of the theorem document makes this explicit as three postulates:

**P1 (H-1, OP-SM-7a):** H_ZBW = ħω₀ A_K3
  - Physical motivation: ZBW hops between colour vertices via SSV
    gradient interactions (same mechanism as Gell-Mann operators).
    All three K3 edges equivalent by C3 symmetry → uniform hopping.
  - Status: OPEN. Derivation from CPP interaction rules not yet done.

**P2 (ZBW-1, OP-SM-7b):** m_i ∝ |ψ_i|²
  - Physical motivation: each CP processes DI-bit flows at rate ∝ |ψ_i|².
    Mass = stored ZBW energy ∝ DI-bit flow rate.
    This is the lepton-sector Born rule — special case of OP-QM-1.
  - Status: OPEN. Derivation from CPP postulates not yet done.

**P3 (thermal equipartition, OP-SM-7c):** equal occupation per eigenstate
  - Physical motivation: at thermal equilibrium in classical Boltzmann
    limit (high T), all 3 K3 eigenstates have equal occupation 1/3.
    1 bonding state + 2 antibonding states → |c-|²/|c+|² = 2 → ρ = √2.
  - Status: OPEN (milder than P1, P2 — is a consequence of Thomas's
    thermal equilibrium picture).
  - NOTE: This is STATE-COUNTING equipartition, not energy equipartition.
    Explicitly distinguishing these was Opus's Issue 1.

### 4. Why quarks don't satisfy Koide (Opus Issue 2)

Quarks also use the K3 base but deviate from Koide:
  K(d,s,b) = 0.731 (9.7% above 2/3)
  K(u,c,t) = 0.849 (27.3% above 2/3)

CPP explanation: quark masses include qDP chain binding energy
(~99% of proton mass), inter-cage bonding, and cage-depth scaling.
These strong-sector contributions are large, vary across generations,
and break the K3 spectral symmetry. Leptons carry no colour charge,
have no qDP chains, and their masses ARE purely from K3 ZBW modes.
The K3 theorem is a lepton result, not a universal one.

### 5. Corollary: K3 encodes both lepton charge and lepton mass ratios

Theorem 1 (Paper 1): δ = 1/3 from C3 combinatorics (three equal vertices
summing to 1). Uses COMBINATORIAL structure of K3.

Theorem K3 (Paper 3): K = 2/3 from eigenvalue ratio 2:1. Uses
SPECTRAL structure of K3.

The same equilateral triangle encodes both the charge of leptons
(fractional charge fraction δ = 1/3) and the ratios of their masses
(Koide K = 2/3). The cage base is doing double duty.

---

## Open Problems Registered This Session

| ID | Problem | Status |
|---|---|---|
| OP-SM-5 | Lepton mass derivation | OPEN — cage-radius mechanism falsified |
| OP-SM-7 | Koide K=2/3 origin | PARTIAL — K3 theorem proved given P1,P2,P3 |
| OP-SM-7a | Derive P1 (H = ħω₀ A_K3) | OPEN |
| OP-SM-7b | Derive P2 (m_i ∝ |ψ_i|²) | OPEN |
| OP-SM-7c | Derive P3 (thermal equipartition) | OPEN |
| OP-SM-7d | Derive Koide phase θ exactly | OPEN |

---

## What the Theorem Proves vs Doesn't

**PROVES (given P1, P2, P3):**
- K = 2/3 exactly
- ρ = √2 from K3 spectral ratio
- C3 phase structure from cage symmetry (Theorem 1)
- K = 2/3 is unique to N=3 colour vertices

**DOES NOT PROVE:**
- Individual masses m_μ, m_τ (need θ and scale A = √m_e)
- WHY ρ = √2 from deeper principles (P3 gets there, but P3 is a postulate)
- The phase θ = 132.73° (requires SSV dynamics derivation — OP-SM-7d)
- Why quarks deviate from Koide (qualitative explanation only)

---

## The One Remaining Near-Miss Worth Recording

θ_Koide ≈ (1-δ)·arccos(-1/3) + δ·π  [0.19% accuracy]

where δ = 1/3 = hDP overlap fraction (Theorem 1). This connects the
Koide phase to the tetrahedral bond angle and δ, both from the cage.
It is a CONJECTURE (0.19% in angle → ~29% in masses), not a derivation.
If this becomes exact (or if the 0.19% residual can be derived from
SSV coupling), it would close OP-SM-7d.

---

## Files Produced This Session

| File | Location | Description |
|---|---|---|
| `k3_spectral_theorem.tex` | `600-cell_standard_model_emergence/papers/paper_3_k3_spectral_theorem_koide_formula.tex` | Main theorem document (v2, 4 pages, 0 compile errors) |
| `k3_spectral_theorem.pdf` | same directory | Compiled PDF |
| `open_problems.zip` | project root | Updated OP-SM-5, OP-SM-7, OP-SM-7a–d |

---

## Next Steps (Priority Order)

1. **OP-SM-7b (P2: m_i ∝ |ψ_i|²)** — the ZBW Born rule.
   This is the most direct path to closing Paper 3. If m_i ∝ |ψ_i|²
   can be derived from the CPP DI-bit flow rate postulate, P2 is closed.
   This is a restricted version of OP-QM-1 (general Born rule) applied
   specifically to ZBW mass generation.

2. **OP-SM-7a (P1: H = ħω₀ A_K3)** — the ZBW Hamiltonian.
   Derive from the SSV hopping mechanism (already done for Gell-Mann
   operators in Paper 1/strong sector). The extension to the ZBW
   orbital should follow the same argument.

3. **OP-SM-7d (θ from SSV dynamics)** — the Koide phase.
   The hardest remaining step. The near-miss θ ≈ (1-δ)θ_tetra + δπ
   (0.19%) suggests the answer involves δ=1/3 and the tetrahedral
   angle, but the mechanism connecting SSV coupling to the angular
   offset has not been found.

4. **FEM calculation** (parallel, Thomas's suggestion) — SSV field
   profiles for tetrahedral vs. icosahedral cages. Would independently
   verify the cage-size hierarchy and the SSV radial dependence.

---

## Opus Pre-Submission Evaluation (24 March 2026)

**Overall verdict:** "A genuine conditional result that deserves to be
in a paper."

Three issues identified and addressed:

**Issue 1 (FIXED in v2):** The "energy equipartition" in Step 4 was
a hidden third postulate. Now explicitly stated as P3 (thermal
state-counting equipartition). Physical motivation: ZBW thermalises
with DP Sea at high T, giving equal occupation per eigenstate.

**Issue 2 (FIXED in v2):** Quarks also use K3 but don't satisfy Koide.
Now Remark 5 in the theorem explains why: strong-sector contamination
(qDP chains, cage binding) dominates quark mass and breaks K3 symmetry.
The theorem is a lepton result.

**Issue 3 (ALREADY IN v1, CLARIFIED in v2):** The theorem proves K=2/3
but not individual masses. The scope table now lists θ (OP-SM-7d) and
scale A (calibrated to m_e) as separate open items.

---

## Session Participants and Roles

- **Thomas Lee Abshier ND:** Physical insight (Lorentz-ZBW mechanism,
  thermal picture, cage structure intuition). Direction of inquiry.
- **Grok (xAI):** Earlier mass table work (prior sessions); noted as
  having fabricated numerical results in cage mass calculation —
  Opus audit caught this and all numerical results were re-verified
  by code in this session.
- **Claude Sonnet (Anthropic):** All calculations in this session.
  Eigenmode calculation, K3 spectral analysis, algebraic proofs,
  LaTeX compilation, open problems registration.
- **Claude Opus (Anthropic):** Pre-submission review of theorem v1.
  Caught three issues; all three addressed in v2.
