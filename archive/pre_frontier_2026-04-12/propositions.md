# CPP Propositions Registry

**Last updated:** 30 March 2026 (tiering update following Opus review)
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute

---

## Purpose

This file catalogues CPP Propositions — physical claims asserting a specific CPP mechanical account for phenomena that standard physics either treats as primitive postulates, derives from separate frameworks, or leaves unexplained. Each proposition stands independently: it identifies a phenomenon, states what CPP claims about its mechanism, and records the physical argument.

A proposition is promoted to Theorem when a formal proof from CPP axioms is completed. It is demoted to Conjecture if a gap in the physical argument is found. It is Falsified if a counter-example or internal inconsistency is identified. No entry is ever deleted.

**30 March 2026 tiering update:** An independent review by Claude Opus (Anthropic) found that the original file did not adequately distinguish "physically motivated narrative" from "quantitatively verified claim." Four explicit maturity tiers have been added throughout. Readers should treat Tier 3 items as strong research candidates and Tier 4 items as candidate mechanisms awaiting quantitative development — not as established results.

---

## Maturity Tiers

**TIER 1 — THEOREM**
Derived from CPP axioms by complete logical proof. No additional computation or verification needed. Indistinguishable in status from theorems in postulates_and_theorems.md.

**TIER 2 — PROOF-COMPLETE, FORMALISATION PENDING**
The key calculation has been performed and is internally consistent. The physical argument is at near-theorem standard. What remains is a formal proof write-up from axioms, not a new computation.

**TIER 3 — NEEDS QUANTITATIVE VERIFICATION**
The physical mechanism is sound and logically coherent, but the central numerical claim has not been computed from CPP primitives. Each Tier 3 item has one specific, identified, tractable calculation that would confirm or refute it. Until that calculation is performed, the item is a strong candidate, not a result.

**TIER 4 — CANDIDATE MECHANISM**
A physically motivated narrative consistent with CPP postulates that qualitatively accounts for the relevant phenomenon. No quantitative test has been performed. These items belong in a candidate mechanisms register and should not be cited alongside Tier 1 or Tier 2 items as equivalent results. Opus (30 March 2026): "Each proposition needs either a quantitative prediction that can be checked or a formal derivation from the postulates. Without that, they're not contributing to the theory's maturity."

The boundary between Tier 3 and Tier 4 is the existence of a specific, identified, tractable calculation. If such a calculation exists and has a known form, the item is Tier 3. If the physical picture is correct but the path to quantification is not yet identified, the item is Tier 4.

---

## Maturity Summary Table

| ID | Name | Tier | Key test or gap |
|----|------|------|----------------|
| THEO-1 | CP Non-Persistent Co-Occupation | **TIER 1** | Proved from AXIM-1,2,4 |
| CORL-1a | ZBW Turning Point at Superimposition | **TIER 1** | Corollary of THEO-1 |
| CORL-1b | Stochastic Partner Exchange | **TIER 1** | Corollary of THEO-1, CORL-1a |
| PROP-3 | Tetrahedral Cage Uniqueness | **TIER 2** | Calculation done; formal proof needed |
| PROP-1 | Random Walk / Quantum Uncertainty | **TIER 3** | Derive ℏ from CPP (OPEN-P-QM-new-1) |
| PROP-2 | Rogue Wave Tunneling | **TIER 3** | Compute WKB rate from SSV stats (OPEN-P-QM-new-3) |
| PROP-4 | Elastic Tunneling via Cage Dissolution | **TIER 3** | Rate calc pending; photon-absence confirmed |
| PROP-5 | Radial DP Chain Equilibrium Length | **TIER 3** | Computed 30 Mar 2026: r_chain ≠ r_e; corollary of α_fine derivation |
| PROP-6 | DP Chain Compaction = de Broglie λ | **TIER 4** | Chain period calculation not performed |
| PROP-7 | Cage Reformation from Sea CPs | **TIER 4** | Reformation rate not computed |
| PROP-8 | Dual Stable Configurations of −eCP | **TIER 4** | A↔B transition rates not computed |
| PROP-9 | Atomic Orbitals as DP Chain Standing Waves | **TIER 4** | SWE derivation open (OPEN-P-QM-new-6) |
| PROP-10 | Electron Identity Transfer / Born Rule | **TIER 4** | Depends on OPEN-P-QM-new-1 |
| PROP-11 | Virtual Particles and Gauss's Law | **TIER 4** | VP lifetime formula not verified |
| PROP-12 | Critical Separation Distance r_crit | **TIER 4** | Same calc as PROP-5; upgrades with it |
| PROP-13 | Photon Pair Production via Lorentzian Asymmetry | **TIER 4** | Cross-section not computed |
| PROP-14 | Mass as Thermodynamic Boundary | **TIER 4** | Definitional reframing of AXIM-6; weakest item |
| PROP-15 | Pair Annihilation: Isentropic vs Non-Isentropic | **TIER 4** | Ortho:para ratio requires cage geometry calc |

---

## Source and Vocabulary

All items arose from the SM-1 mechanism essay discussion of ZBW oscillation mechanics (29–30 March 2026), which identified stochastic partner exchange in the Dipole Sea as a single unifying principle with implications across quantum mechanics, pair production, virtual particles, atomic orbitals, tunneling, and relativistic mass. Authors: Thomas Lee Abshier ND and Claude Sonnet (Anthropic).

Logical chain of discovery:

    ZBW turning point question
    → THEO-1 (CP exclusion is a theorem)
    → CORL-1a (turning point at superimposition)
    → CORL-1b (stochastic partner exchange)
    → PROP-1 through PROP-15

Note: THEO-1 and Corollaries CORL-1a/1b are listed here for context. Their canonical home is postulates_and_theorems.md.

---

## TIER 1 — THEOREMS

### THEO-1: CP Non-Persistent Co-Occupation

**Tier:** TIER 1 — THEOREM (proved from AXIM-1, AXIM-2, AXIM-4)
**Consequence:** CP Exclusion Postulate is redundant and removed. Axiom count reduced from 7 to 6.

**Statement:** Two Conscious Points cannot persistently occupy the same Grid Point.

**Proof:** Same-polarity CPs: repulsive SSV_net grows monotonically as separation decreases — same-polarity CPs never reach superimposition. Opposite-polarity CPs: SSV_net is attractive and monotonically increasing throughout approach. No reversal occurs before superimposition. At superimposition, the intra-pair direction vector r̂_{A→B} is undefined — the bulk Dipole Sea SSV_net governs both CPs. Because A and B have opposite polarities, they respond to the same bulk SSV_net with opposite displacements and separate on the next Absolute Moment. Superimposition lasts exactly one Absolute Moment. □

---

### CORL-1a: ZBW Turning Point at Grid Point Superimposition

**Tier:** TIER 1 — THEOREM (corollary of THEO-1)
**Consequence:** f_ZBW ≈ 1/(2t_P) is derived, not postulated. AXIM-5 demoted.

**Statement:** The ZBW oscillation turning point of a bound DP pair occurs at Grid Point superimposition. SSV_net on A from B is attractive and monotonically increasing throughout approach — no reversal occurs until intra-pair SSV direction vanishes at superimposition. For a minimal-amplitude oscillation, period = 2 Absolute Moments → f_ZBW ≈ 1/(2t_P) as a geometric consequence.

---

### CORL-1b: Stochastic Partner Exchange in the Dipole Sea

**Tier:** TIER 1 — THEOREM (corollary of THEO-1 and CORL-1a)

**Statement:** DP pair identity is not persistent. After each superimposition, each CP's next partner is determined by the dominant SSV_net at its post-superimposition Grid Point, which need not be its previous partner. The Dipole Sea is a gas of transient partnerships renewed each ZBW cycle. This corollary is the physical principle underlying all propositions PROP-1 through PROP-15.

---

## TIER 2 — PROOF-COMPLETE, FORMALISATION PENDING

### PROP-3: Tetrahedral Cage as Unique Minimum Stable Cage

**Tier:** TIER 2 — PROOF-COMPLETE, FORMALISATION PENDING
**Upgrade path:** Write formal proof from AXIM-1, AXIM-2, AXIM-4 using the energetic argument as the core.
**Reviewer note (Opus):** "The calculation showing N=4 is bound and N=12 is unbound is straightforward electrostatics and the conclusion is right."

**Statement:** The regular tetrahedron (N=4 same-polarity cage CPs around an opposite-polarity central CP) is the unique minimum configuration satisfying two independent stability conditions:

(a) Energetic stability:

    U = −N × SSV₀/r_c + (N(N−1)/2) × SSV₀/r_v

    N=4 tetrahedron (r_v ≈ 1.633 r_c, 6 pairs):
    U_tetra ≈ −0.33 SSV₀/r_c < 0  ✓  BOUND

    N=12 icosahedron (r_v ≈ 1.051 r_c, 30 pairs):
    U_icosa ≈ +16.5 SSV₀/r_c > 0  ✗  UNBOUND

(b) Geometric completeness: T_d symmetry cancels all SSV_net multipole moments at the central CP. N < 4: residual moments prevent force-free equilibrium. N = 4 tetrahedron: all multipole moments vanish simultaneously. N=4 is the unique cage geometry in the 600-cell nearest-neighbour shell where both conditions coincide.

---

## TIER 3 — NEEDS QUANTITATIVE VERIFICATION

These are the highest-priority research targets for the CPP QM series. Each has one identified tractable calculation.

---

### PROP-1: Random Walk of the Central CP and Quantum Position Uncertainty

**Tier:** TIER 3 — NEEDS QUANTITATIVE VERIFICATION
**Required calculation:** Compute the random walk RMS displacement per ZBW cycle from CPP primitives (SSV₀, l_P, t_P, sea_strength); verify this equals the Compton wavelength ℏ/m_e c at the electron mass scale. This amounts to deriving ℏ from CPP statistics.
**Open problem:** OPEN-P-QM-new-1
**If confirmed:** ℏ is derived; uncertainty principle emerges without postulating it.
**If refuted:** The random walk amplitude or scaling is wrong; picture needs revision.

**Statement:** The central CP of a fermion executes a stochastic random walk through the 600-cell lattice as a consequence of ZBW partner switching. At each ZBW cycle, the post-superimposition Grid Point is determined by the instantaneous bulk SSV_net — stochastic because surrounding Sea DPs have randomised orientations. Over N cycles the displacement grows as √N × l_P. The distribution of central CP locations is the CPP account of |ψ(x)|².

The Born rule connection (high SSV_abs → compressed PSR → fewer visits per physical volume → probability ∝ 1/SSV_abs) is qualitatively coherent but part of the same unverified picture. The Born rule has not been derived from CPP; the qualitative account has been sketched.

---

### PROP-2: Solitonic (Rogue Wave) Tunneling Mechanism

**Tier:** TIER 3 — NEEDS QUANTITATIVE VERIFICATION
**Required calculation:** Compute P(tunnel per ZBW cycle) from the statistics of N independent SSV_net vectors of mean magnitude μ at the central CP's near-side Grid Point; verify this equals exp(−2κd) with the correct κ for given barrier height and width.
**Open problem:** OPEN-P-QM-new-3
**If confirmed:** WKB tunneling is derived from SSV_net vector statistics; no wave mechanics required.
**If refuted:** The statistics do not produce the correct exponential; picture needs revision.

**Statement:** Quantum tunneling occurs when a rogue-wave stochastic superposition of SSV_net vectors produces a rare large-amplitude spike sufficient to displace the central CP across the barrier. For N Sea vectors of mean magnitude μ: P(spike > A) ∝ exp(−A²/Nμ²). For barrier height V_b: P(tunnel per ZBW cycle) ∝ exp(−V_b/Nμ²), which has the WKB form. The exponent has not been computed to verify it matches κ = √(2m(V−E))/ℏ with the correct numerical value.

---

### PROP-4: Elastic Tunneling via Cage Dissolution and Reformation

**Tier:** TIER 3 — NEEDS QUANTITATIVE VERIFICATION
**Required calculation:** (i) PROP-2 rate calculation applies. (ii) Verify energy deposited/extracted in Sea during dissolution/reformation = 2 SSV₀ exactly.
**One prediction already confirmed:** Tunneling electrons emit no photons. The tetrahedral (isotropic) cage dissolution has no preferred emission axis — no photon can form. This is observed. This confirmed prediction elevates PROP-4 above a pure Tier 4 narrative.
**Open problem:** OPEN-P-QM-new-3

**Statement:** During rogue-wave tunneling (PROP-2), the central −eCP crosses the barrier while cage +eCPs remain. The cage dissolves isotropically into the Sea — no photon forms because no preferred emission axis exists. The −eCP reforms an identical cage from partner-transitioning Sea CPs on the far side. Tunneling is elastic: mass and charge conserved exactly. The electron's identity is carried solely by the central −eCP during transit.

---

### PROP-5: Radial DP Chain Equilibrium Length

**Tier:** TIER 3 — NEEDS QUANTITATIVE VERIFICATION
**Computation status:** PERFORMED 30 March 2026 — result inconclusive; see findings below.
**Open problems:** OPEN-P-QM-new-4, OPEN-P-QM-new-5, OPEN-P-QM-new-9 (new)

**Statement:** The four radial DP chains from the cage vertices reach equilibrium length r_chain where the central CP's SSV attraction balances thermal Sea dissolution pressure:

    SSV₀/r_chain² = sea_strength × SSV₀/d_Sea²
    → r_chain = d_Sea / √sea_strength

**Computation result (30 March 2026):**

The calculation was performed for every physically motivated identification of d_Sea:

    d_Sea = l_P:                 r_chain ~ 10⁻²⁰ fm  (off by ~10²⁰ from r_e)
    d_Sea = r_conf = 0.16 fm:    r_chain = 0.379 fm   (factor 7.4 below r_e)
    d_Sea = r_conf = 0.40 fm:    r_chain = 0.948 fm   (factor 3.0 below r_e)
    d_Sea = √(r_conf × r_e):     r_chain = 2.517 fm   (within 11% of r_e)

For r_chain = r_e = 2.818 fm, d_Sea must equal 1.189 fm = r_e × √sea_strength. This is circular unless d_Sea can be derived independently from CPP primitives.

**Finding 1 — r_conf inconsistency exposed:**
The CPP constants sea_strength = 0.178, ħω₀ = 87.8 MeV, and r_conf = 0.16 fm are mutually inconsistent under ħω₀ = sea_strength × ħc/r_conf. Consistent pairs are: r_conf = 0.40 fm (given sea_strength and ħω₀), or ħω₀ = 219.5 MeV (given sea_strength and r_conf = 0.16 fm). Registered as OPEN-P-QM-new-9.

**Finding 2 — r_e expressed exactly in CPP terms:**
Confirmed to machine precision: r_e = α_fine × ħc/(2 × SSV₀). This means confirming r_chain = r_e is equivalent to deriving α_fine from 600-cell geometry (EW sector). PROP-5 is a corollary of the α_fine derivation, not an independent target.

**Revised status:** The physical mechanism is sound. The claim r_chain ≈ r_e is now understood to depend on (a) resolving the r_conf inconsistency (OPEN-P-QM-new-9) and (b) deriving α_fine from CPP (EW series). PROP-5 becomes a specific prediction: r_chain = α_fine × ħc/(2 × SSV₀) once d_Sea is derived from 600-cell geometry.


