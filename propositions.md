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
| PROP-5 | Radial DP Chain Equilibrium Length | **TIER 3** | Compute r_chain vs r_e — HIGHEST PRIORITY |
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

**Tier:** TIER 3 — NEEDS QUANTITATIVE VERIFICATION — HIGHEST PRIORITY
**Required calculation:** Compute r_chain = d_Sea/√sea_strength numerically using d_Sea from 600-cell geometry and sea_strength = 0.1780 (SS-1 Theorem 6). Compare to r_e = 2.82 × 10⁻¹⁵ m.
**If r_chain ≈ r_e:** Chain equilibrium picture confirmed; r_e derived from CPP geometry rather than defined circularly.
**If r_chain ≠ r_e:** Equilibrium condition wrong, or d_Sea identification incorrect; picture needs revision.
**Reviewer note (Opus):** "Do one quantitative check from this session before moving on. The strongest candidate is PROP-5: compute r_chain from SSV₀ and sea_strength and see if it matches r_e. This is a single calculation with a definitive answer."
**Open problems:** OPEN-P-QM-new-4, OPEN-P-QM-new-5

**Statement:** The four radial DP chains extending from the cage vertices reach equilibrium length r_chain set by the balance of radial SSV attraction, lateral inter-chain repulsion, and thermal Sea dissolution. Equilibrium condition: SSV₀/r_chain² = sea_strength × SSV₀/d_Sea², giving r_chain ~ d_Sea/√sea_strength ≈ 2.37 × d_Sea. The chain organisational energy is additional rest mass beyond 2 SSV₀; if non-negligible, it requires revising the SM-1 calibration (OPEN-P-QM-new-5).

---

## TIER 4 — CANDIDATE MECHANISMS

The following propositions are physically motivated narratives consistent with CPP postulates. No quantitative test has been performed for any of them. They should be read as candidate mechanisms — potential future Tier 3 items — not as established results. Opus (30 March 2026) specifically recommends these belong in a "candidate mechanisms" register rather than beside proved results.

---

### PROP-6: Relativistic DP Chain Compaction as the de Broglie Wavelength

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute the physical spatial period of the cage-plus-chain structure as a function of velocity using PSR_eff = l_P/(1 + k·SSV_abs); verify period = h/p = h/(γmv).

**Statement:** At high velocity, SSV_abs compresses PSR at each chain DP Grid Point, reducing the physical distance between consecutive chain DPs. The spatial period of the cage-plus-chain structure decreases as 1/γ, reproducing λ_dB = h/p without a wave postulate. Wave-particle duality is a continuous mechanical transition — long-period (low v, wave-like) to short-period (high v, particle-like) — not a change of description.

---

### PROP-7: Cage Reformation from Partner-Transitioning Sea CPs

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute the cage reformation rate from Sea CP partner-switching kinetics; verify the electron cage is stable (reformation rate >> dissociation rate at T = 0).

**Statement:** Cage +eCPs that reform around a newly-arrived central −eCP are Sea CPs in mid-transition between partnerships, intercepted by the central CP's strong SSV_net. Cage reformation is normal partner-switching dynamics biased by a strong SSV_net source. The cage is a persistent geometric relationship, not a persistent collection of specific CPs. The electron's identity is in the central −eCP alone.

---

### PROP-8: Dual Stable Configurations of the Central −eCP

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute A→B and B→A transition rates as functions of temperature and Sea CP density; verify B→A is sufficiently rare to account for the electron's effective infinite stability.

**Statement:** A −eCP has two energetically distinct configurations: (A) DP enrollment (binding energy ≈ SSV₀/2, Sea constituent) and (B) 4-vertex tetrahedral cage (binding energy = 2 SSV₀ = m_e c², the electron as an SM particle). B is the deeper energy minimum. Pair creation = correlated A→B transition; pair annihilation = correlated B→A transition.

---

### PROP-9: Atomic Orbital Probability Density as DP Chain Standing Waves

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** OPEN-P-QM-new-6 (derive SWE from DP chain standing wave stability conditions). This is the hardest open problem in the QM series — likely requires several formal sessions before quantitative testing is possible.

**Statement:** Atomic orbital |ψ(x)|² arises from three simultaneous CPP mechanisms: (1) KE polarisation of the Sea into directed chains with period λ_dB (PROP-6); (2) nuclear SSV gradient biasing the central CP random walk toward high-|ψ|² regions; (3) self-reinforcing DP chain standing waves in the stationary SSV landscape, with nodes and antinodes corresponding to orbital nodes and antinodes.

---

### PROP-10: Electron Identity Transfer and the Orbital Born Rule

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Depends on PROP-9 and OPEN-P-QM-new-1. The Born rule emergence from identity transfer statistics is conceptually important but requires ℏ to be derived first.

**Statement:** The electron's position is the Grid Point of whichever −eCP currently occupies the central cage role. The Born rule |ψ|² is the time-averaged distribution of these central positions, shaped by the SSV landscape. The Born rule is not postulated; it emerges from CP identity transfer statistics in the SSV field.

---

### PROP-11: Virtual Particles as Transient CP Configurations Constrained by Gauss's Law

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute τ_VP = t_P/p_dissipate for a specific VP configuration; verify τ_VP × ΔE ≈ ℏ.

**Statement:** Virtual particles are transient Sea partner-switching configurations that momentarily reproduce real particle charge and field structure but lack a persistent nucleation seed. Gauss's law requires a compensating anti-configuration within any enclosing charge-neutral volume. Mean VP lifetime τ_VP = t_P/p_dissipate, where p_dissipate increases with VP energy. The energy-time uncertainty ΔE·Δt ≈ ℏ emerges from this lifetime-complexity relationship.

---

### PROP-12: Critical Separation Distance for Real Pair Production

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Relationship to PROP-5:** r_crit = d_Sea/√sea_strength is the same formula as r_chain. Once PROP-5 is verified (OPEN-P-QM-new-4), this item upgrades to Tier 3 automatically, because both use the same calculation.
**Open problem:** OPEN-P-QM-new-7

**Statement:** A +CP/−CP pair nucleates real particles when separation r exceeds r_crit = d_Sea/√sea_strength — the radius at which independent cage nucleation overcomes intra-pair recombination pressure. Below r_crit: VP. Above r_crit: real particles. CPP candidate for the electron Compton wavelength ℏ/m_e c.

---

### PROP-13: Photon Pair Production via Lorentzian Asymmetry

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute the pair production cross-section σ(E) from the nuclear SSV gradient disruption picture; verify σ ∝ Z² and correct energy dependence near threshold.

**Statement:** A photon near a heavy nucleus undergoes Lorentzian asymmetry (inner limb PSR compressed more than outer limb by the nuclear SSV). At hf ≥ 2m_e c², this asymmetry separates a +CP/−CP pair to r > r_crit. Each CP nucleates a cage from Sea CPs. The nucleus absorbs recoil momentum. A nucleus is required because free-space single-photon pair production violates both momentum conservation and the symmetry requirement.

---

### PROP-14: Mass as Thermodynamic Nucleation-Dissipation Boundary

**Tier:** TIER 4 — CANDIDATE MECHANISM (weakest item in this list)
**Reviewer note (Opus, 30 March 2026):** "This is a definition, not a theorem. The testable content would be: compute the temperature at which the electron cage dissolves and show it matches some known transition. That computation hasn't been done."
**Path to testable content:** Compute the cage dissolution temperature from SSV₀ and sea_strength; compare to the QCD transition temperature T_c ≈ 150 MeV (OPEN-P-QM-new-8, OPEN-P-SS-14).

**Statement:** Rest mass = the ground-state organisational energy required to maintain a stable nucleation seed against thermal DP Sea dissipation at T = 0, v = 0. Corollaries: temperature-dependent mass, relativistic mass as chain compaction energy (PROP-6), m_e c² as the threshold organisational energy at r_crit, the second law as DP chain organisation tending toward maximum entropy. This is a useful conceptual reframing of AXIM-6 rather than an independent physical claim.

---

### PROP-15: Pair Annihilation as Isentropic vs Non-Isentropic Cage Dissolution

**Tier:** TIER 4 — CANDIDATE MECHANISM
**Path to Tier 3:** Compute the ortho:para positronium decay ratio from the cage dissolution geometry — show T_d (two-fold axis) cage dissolution gives rate R₂γ and three-fold dissolution gives R₃γ with R₂γ/R₃γ ≈ 1000, matching the observed lifetime ratio (para: 125 ps, ortho: 142 ns).
**Qualitative predictions confirmed:** Low-v e⁺e⁻ → two back-to-back photons; high-v → jets and multiple particles. Both observed, consistent with the isentropic / non-isentropic distinction.

**Statement:** Pair annihilation proceeds through mutual cage dissolution. At low velocity (isentropic): quasi-static dissolution; eight cage CPs form a symmetric structure around the superimposition point; energy dissipates along the approach axis as two back-to-back 0.511 MeV photons; no entropy increase. At high velocity (non-isentropic): incomplete misaligned dissolution; partial cage structures survive; jets and new particles form; entropy increases. Three-photon ortho-positronium outcome arises from three-fold (rather than two-fold) cage dissolution geometry.

---

## Open Problems Cross-Reference

| Proposition | Tier | Required calculation | OP ID |
|-------------|------|---------------------|-------|
| PROP-1 | 3 | Derive ℏ from CPP random walk statistics | OPEN-P-QM-new-1 |
| PROP-2 | 3 | Compute WKB rate from SSV_net rogue wave stats | OPEN-P-QM-new-3 |
| PROP-4 | 3 | Tunneling rate; dissolution/reformation energy balance | OPEN-P-QM-new-3 |
| PROP-5 | 3 | Compute r_chain; compare to r_e **(NEXT SESSION)** | OPEN-P-QM-new-4, OPEN-P-QM-new-5 |
| PROP-9 | 4 | Derive SWE from DP chain standing wave stability | OPEN-P-QM-new-6 |
| PROP-12 | 4 | Compute r_crit; upgrades with PROP-5 | OPEN-P-QM-new-7 |
| PROP-14 | 4 | Compute cage dissolution temperature | OPEN-P-QM-new-8, OPEN-P-SS-14 |

---

*See also: postulates_and_theorems.md (THEO-1, CORL-1a/1b in canonical form), open_problems/README.md (OPEN-P-QM-new-1 through OPEN-P-QM-new-8), predictions.md.*

*Independent review: Claude Opus (Anthropic), 30 March 2026. Tier assignments reflect that review.*
