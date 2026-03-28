# Development History: SM-4 — Charged Lepton Masses from the K3 Spectral Theorem

**Series:** 600-Cell Standard Model Emergence  
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)  
**Document type:** Development narrative — laboratory notebook record  
**Last updated:** 26 March 2026

---

## Purpose of This File

This document records the intellectual history of SM-4: how the paper was
scoped, what it originally attempted, where its ambitions were trimmed back,
and why the trimming was an improvement rather than a retreat. SM-4 is
notable in the CPP series because it is primarily a paper about *limits* —
what the K3 theorem can and cannot do — and because its most important
result is a negative one: the proof that the Koide phase θ is undetermined
within the K3+SSV framework.

---

## The Starting Point: What SM-3 Left Open

SM-3 proved K = 2/3 exactly. But the Koide parametrisation has three
parameters: ρ (derived), A (scale), and θ (phase). SM-3 determined ρ.
It left A and θ as free parameters to be calibrated from experiment.

The natural ambition for SM-4 was to close this gap — to derive θ from
CPP dynamics and thereby predict all three lepton masses from the electron
mass alone. This would have been a remarkable result: zero free parameters
beyond the one calibration (m_e), and three masses predicted.

SM-4 does not achieve this. It proves instead that this ambition cannot be
realised within the K3+SSV framework — a structural impossibility, not a
gap waiting to be filled.

---

## First Approach: Trying to Derive θ from SSV Dynamics

The first attempt to derive θ asked: can the SSV potential at the apex
vertex V₄ of the tetrahedral cage break the degeneracy of the antibonding
subspace and select a preferred orientation θ?

The physical picture was plausible: V₄ is the apex of the tetrahedron,
geometrically distinct from the three base vertices V₁, V₂, V₃. The SSV
potential from V₄ descends toward the base, and if it couples differently
to the two antibonding modes, it could select one over the other and fix θ.

**What was tried:**
- Direct computation of the SSV gradient from V₄ at the three base vertices
- Perturbation theory: treating the V₄ coupling as a small perturbation
  on the K₃ Hamiltonian and computing first-order corrections to the
  antibonding eigenstates
- Löwdin downfolding: integrating out the apex degree of freedom to get
  an effective Hamiltonian on the three base vertices

**What was found:**
All three approaches gave the same answer: the apex couples only to the
bonding mode, not to the antibonding modes. The coupling vector from V₄
to the base is proportional to (1,1,1)^T/√3 — the bonding eigenvector of
K₃. Since the antibonding modes are orthogonal to (1,1,1)^T, the apex
is completely invisible to them. No SSV perturbation from the apex can
lift the antibonding degeneracy.

This is the content of the Löwdin downfolding proof in Theorem 4.1:
H_eff(E) = A_{K₃} - (1/E) v vᵀ, where v = (1,1,1)ᵀ/√3. The second
term acts only on the bonding sector; the antibonding sector is unaffected
for all E.

**Why this is a theorem, not just a failed calculation:**
The result generalises. It is not specific to the particular form of the
SSV potential or the particular distance from the apex to the base. Any
perturbation with C3 symmetry — any perturbation that treats V₁, V₂, V₃
equally — must couple to the (1,1,1)ᵀ direction and therefore can only
affect the bonding mode. The antibonding degeneracy is protected by C3
symmetry itself, not by any accidental cancellation.

---

## The Decision to Frame the Result Honestly

Once the negative result was established, a choice had to be made about
how to frame SM-4. Two options:

**Option A (overstating):** Present SM-4 as deriving the muon and tau masses
from the electron mass, using θ as a "second calibration constant." Claim
that two experimental inputs (m_e and θ) predict the other two masses.

**Option B (honest):** Present SM-4 as applying the K3 theorem to the lepton
mass problem, with K=2/3 as a consistency check at 11 ppm, and with θ
explicitly identified as not predicted by K3+SSV.

The series standard — established in the corrections to SM-2 — is Option B.
The paper is explicit: "The empirical content is that nature satisfies
K = 2/3 to 11 ppm — a remarkable consistency check, not a two-from-one
derivation."

This framing is more defensible under scrutiny, more useful for the
development of the series, and more scientifically honest. A paper that
appears to predict two masses from one but actually uses two experimental
inputs disguised as one would be criticised correctly. The current framing
invites no such criticism.

---

## The Parameter Counting Analysis

A key contribution of SM-4 is the careful parameter counting in the Remark
following Theorem 1. This analysis deserves its own development note because
it was not obvious how to count correctly.

**The naive count:** The Koide parametrisation has three parameters (A, ρ, θ).
SM-3 derives ρ = √2. SM-4 calibrates A and θ from PDG data. Therefore: one
derived, two calibrated. Net reduction from three free parameters to two.

**Why this is the right count:**
The Standard Model treats m_e, m_μ, m_τ as three independent free parameters.
The K3 theorem says they are not independent — they must satisfy K = 2/3.
This removes one degree of freedom. Given any two masses, the third is
determined by K = 2/3. The CPP lepton sector has two free parameters, not
three.

**What this means for the book:**
The K3 theorem is a *structural constraint* on lepton masses, analogous to
the way SU(3) is a structural constraint on the quark sector. It does not
predict the masses; it constrains their ratios. The constraint is non-trivial
and is satisfied to 11 ppm. This is the appropriate level of claim.

---

## The Proximity of θ to the Critical Angle

One of the more striking empirical observations in SM-4 is the proximity
of θ = 132.73° to the critical angle θ_c = 3π/4 = 135°. At θ = θ_c,
the electron would have zero mass: the formula gives
(1 + √2 cos(3π/4)) = 1 - 1 = 0.

The correction Δθ = θ_c - θ = 2.27° is empirically of order sea², where
sea = sea_strength ≈ 0.1780. Numerically: (5/4) × sea² ≈ (5/4) × 0.0317 ≈
0.0396 radians ≈ 2.27°. The coefficient 5/4 is not derived.

**What this suggests:**
The electron is a particle that is nearly massless but acquires a small mass
through a second-order SSV perturbation. This is reminiscent of the way
neutrino masses are suppressed in the Standard Model through the seesaw
mechanism — a small mass arising from a perturbative correction to a
zero-mass structure.

If this analogy is correct, the electroweak sector provides a perturbation
that shifts θ from its "natural" value of 3π/4 (zero electron mass) to its
observed value of 132.73°. The perturbation is of order sea², suggesting
it involves two SSV interactions rather than one. This is the physical
picture behind the Aharonov-Bohm self-energy candidate (OP-SM-7d-AB):
the ZBW orbital circulating on the K3 triangle generates a two-interaction
loop that provides exactly this second-order correction.

This remains speculative and is registered as OP-SM-7d. But the numerical
coincidence (5/4) × sea² = Δθ is suggestive enough to warrant pursuing.

---

## What SM-4 Established for the Series

SM-4 contributes four things to the CPP series:

**1. The consistency check at 11 ppm:**  
Nature satisfies K = 2/3 to 11 ppm. This is a non-trivial empirical fact
that the K3 theorem explains geometrically. The 0.004% and 0.001% errors
for m_μ and m_τ are not CPP predictions — they are measures of how well
nature satisfies a constraint that CPP derives.

**2. The structural impossibility theorem:**  
Theorem 4.1 closes off a large class of possible mechanisms for θ. Any
mechanism using K3+SSV with C3 symmetry cannot select θ. The electroweak
sector is required. This is a definitive result that focuses the search
for OP-SM-7d.

**3. The parameter counting framework:**  
The careful distinction between "derived," "calibrated," and "open" becomes
the template for all subsequent CPP papers. SM-4 establishes that CPP makes
a genuine theoretical contribution (one derived constraint) while being
honest about what requires experimental input.

**4. The critical angle observation:**  
The proximity θ ≈ 3π/4 - sea² is a new empirical observation motivated by
the K3 framework. It would not have been noticed without the Koide
parametrisation that SM-3 and SM-4 develop. It is a prediction-shaped
observation: if the Aharonov-Bohm mechanism is correct, Δθ = (5/4) sea²
is a genuine prediction of the two-loop ZBW self-energy.

---

## Summary of the Logical Chain

1. SM-3 derives K = 2/3 from K3 spectral structure. This gives ρ = √2.
2. The Koide parametrisation with ρ = √2 and experimental θ reproduces
   m_μ and m_τ from m_e to 11 ppm (Proposition 3.1).
3. The Löwdin downfolding theorem shows θ cannot be derived from K3+SSV
   (Theorem 4.1). θ requires electroweak physics.
4. The proximity θ ≈ 3π/4 - (5/4)sea² motivates the Aharonov-Bohm
   candidate for OP-SM-7d (registered, not derived).

---

*Document prepared by Claude Sonnet (Anthropic) in collaboration with  
Thomas Lee Abshier ND, March 2026.*  
*To be updated as the electroweak series develops.*
