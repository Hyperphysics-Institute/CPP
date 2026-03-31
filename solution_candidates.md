# CPP Solution Candidates Registry

**Repository location:** CPP root level
**Last updated:** 30 March 2026
**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute

---

## Purpose

This file records specific candidate mechanisms for open problems — the intermediate research layer between "the problem exists" (open_problems/README.md) and "the problem was solved" (postulates_and_theorems.md). It captures the how before the idea is lost: the specific formula, the computation steps, the tractability estimate, and crucially the ordered record of what was tried and why it succeeded or failed.

Each entry targets a specific OPEN-P item, gives the proposed mechanism, records its origin session, estimates its tractability, and records its current status. Falsified entries are kept permanently — the record of what does not work is as scientifically valuable as the record of what does.

**This file is distinct from:**
- open_problems/README.md — states *what* is open, not how to solve it
- propositions.md — records CPP physics claims, not solution strategies
- predictions.md — records testable predictions, not research approaches
- development-*.md files — narrative history; this file is a structured research target register

---

## Format

Each entry has: **ID**, **Targets**, **Origin**, **Status**, **Mechanism** (with formula and computation steps where available), and **Tractability** estimate.

**Status labels:**
- ACTIVE — viable candidate; computation not yet performed
- PARTIAL — computation started; result inconclusive
- FALSIFIED — mechanism ruled out; reason recorded
- SUPERSEDED — replaced by a better candidate
- SOLVED — the target open problem was solved using this approach

---

## SC-1: Grok's Exact-Volume + PSR + Interference Mass Ladder

**Targets:** OPEN-P-SS-1 (quark mass formula from 600-cell geometry)
**Origin:** Grok (xAI), 24 March 2026 session
**Status:** PARTIALLY COMPUTED 30 March 2026 — structural issue identified; see findings

**Mechanism:** The structural quark mass for cage depth n is derived from the exact 600-cell shell geometry rather than the approximate E ≈ N/2 formula of SM-1:

    M_q(n) = Σ_{l=1}^{n}  N_l · E_eDP · V_l^proj · (r_eff^(n)/r_l)³ · C_n

where V_l^proj is the exact 3D-projected Voronoi volume of 600-cell shell l, r_eff^(n) is the PSR-compressed effective radius from the multi-shell SSV field, and C_n = |Σ_{m=0}^{n} e^{i·2πm/φ²}| / n is the inter-shell phase cancellation factor.

**Why it was deferred:** Grok produced a mass table (112, 1480, 4620, 195000 MeV) that was verified by Claude Sonnet and Opus to be PDG × 1.15 — the numbers were fabricated rather than computed from the stated formula. The conceptual framework was not tested with actual computed values.

**Required computation steps:**
1. Compute the exact 3D-projected Voronoi volumes for shells 1–4 from 600-cell vertex coordinates (numerical, not from the N/2 approximation)
2. Compute C_n numerically for n=1,2,3,4 (partially done: 0.72, 0.24, 0.36, 0.07)
3. Evaluate the full formula with these values and compare to PDG quark masses
4. If agreement is within ~20%, apply the derived ZBW correction from SM-3

**Computation result (30 March 2026):**

C_n phase cancellation factors confirmed exactly:

    C_1 = 0.7247,  C_2 = 0.2374,  C_3 = 0.3563,  C_4 = 0.0750

The simplified SC-1 formula (without V_l^proj and PSR factors) gives the right qualitative direction — cumulative mass increases with shell depth — but the wrong quantitative scale for heavy quarks:

    n=1 → 730 MeV   (constituent strange: ~540 MeV,  0.74×)
    n=2 → 1128 MeV  (constituent charm:  ~1550 MeV,  1.37×)
    n=3 → 1487 MeV  (constituent bottom: ~4730 MeV,  3.18×)
    n=4 → 1675 MeV  (constituent top:  ~172690 MeV, 103×)

**Structural issue identified:** The V_l^proj and (r_eff/r_l)³ factors are dimensionless and bounded, so they cannot provide the ~103× amplification needed for the top quark. The phase cancellation factor C_4 = 0.075 is the primary problem — destructive inter-shell interference at shell 4 kills the top quark mass contribution rather than enhancing it.

**Root cause of the 103× discrepancy:** The 600-cell shell structure accumulates only 74 actual vertices across 4 shells. SM-2's effective N_k = 30,000 for the top quark (vs 30 actual vertices in shell 4) represents a factor of ~1000 that SC-1's formula cannot generate from C_n and N_l alone.

**Conclusion:** SC-1 in this form is FALSIFIED for the top quark. The C_n geometric factors are real and confirmed, but the formula architecture needs fundamental rethinking to explain the top quark mass scale. The middle shells (strange/charm/bottom) are within 0.7–3× of constituent masses, suggesting the formula captures something real for lighter quarks but breaks down for the top.

**Next step for OPEN-P-SS-1:** The top quark's mass scale requires a mechanism beyond cumulative shell vertex counts × phase cancellation. The SM-3 ZBW thermal picture (K(c,b,t) ≈ 2/3 to 0.42%) suggests heavy quarks are dominated by ZBW thermal energy, not cage geometry. SC-1 may be the correct approach for light/middle quarks only.

---

## SC-2: Aharonov-Bohm Self-Energy Loop for Koide Phase θ

**Targets:** OPEN-P-SM-7d (Koide phase θ from CPP dynamics)
**Origin:** Claude Sonnet, Session E, 24 March 2026
**Status:** FALSIFIED — ruled out in AB session, 25 March 2026

**Mechanism:** The eCP at apex V4 exchanges virtual DPs with the base vertices {V1, V2, V3} via the K3 triangle loop. If there is a magnetic-like flux Φ through the K3 triangle from the ZBW orbital angular momentum, the self-energy acquires an Aharonov-Bohm phase:

    δE_AB = f(sea_strength) · e^{i·Φ/Φ₀}

where Φ₀ = hc/e is the flux quantum. This phase would select a preferred orientation θ in the antibonding subspace, analogous to the Berry phase in molecular systems.

**Why it failed:** For the AB mechanism to select θ, the ZBW orbital on K3 must be chiral — it must have a preferred circulation direction around the triangle. The C3 symmetry of K3 (derived from 600-cell geometry, SM-1 Theorem 1) makes the three vertices V1, V2, V3 geometrically equivalent, which prevents any chiral preference from arising within the K3+SSV framework. The same C3 symmetry that makes K3 give K = 2/3 also prevents any AB-like mechanism from selecting θ. This is a special case of the general structural impossibility proved in SM-4 Theorem 2.

**Note:** This mechanism was one of 11 candidate approaches for θ tested between Sessions B and K. All 11 were falsified, establishing the structural impossibility result registered as OPEN-P-SM-7d.

---

## SC-3: Löwdin Downfolding with Non-Uniform Apex Coupling

**Targets:** OPEN-P-SM-7d (Koide phase θ)
**Origin:** Claude Sonnet, Session E, 24 March 2026
**Status:** FALSIFIED for uniform coupling; non-uniform coupling is also ruled out (see SC-4)

**Mechanism:** Session E showed that the uniform apex coupling v = (1,1,1)/√3 decouples completely from the K3 antibonding modes — V4 is dark to the antibonding subspace (⟨φ₋|v⟩ = 0 exactly). However, if the coupling is non-uniform — for example if the eCP ZBW orbital creates an asymmetric SSV pattern on the base vertices through a self-consistency requirement — then the Löwdin downfolding H_eff(E) = A_{K3} − (1/E)·v·vᵀ would have v with antibonding components, breaking the degeneracy and potentially selecting θ.

**Why it failed:** The non-uniform coupling route requires breaking the equivalence between V4-V1, V4-V2, and V4-V3 couplings. The regular tetrahedron's T_d symmetry makes all three apex-to-base edges identical in both 3D and 4D (confirmed by SC-4's full 4D computation). There is no mechanism within K3+SSV that can produce the required asymmetry.

---

## SC-4: 4D 600-Cell Embedding Breaks C3 Symmetry to Select θ

**Targets:** OPEN-P-SM-7d (Koide phase θ)
**Origin:** Claude Sonnet, Session G (PS-3b), 25 March 2026
**Status:** FALSIFIED — 4D embedding preserves C3 exactly

**Mechanism:** The K3 triangle is embedded in the full 4D 600-cell, where each tetrahedral cage {V1, V2, V3, V4} occupies a specific orientation in 4D space. The K3 base triangle's 4D normal vector is a preferred direction that might not be preserved under the 3D C3 rotation V1→V2→V3→V1. The 3D rotation might not extend to a 4D symmetry of the 600-cell. If so, the full 4D Hamiltonian before projection might break the antibonding degeneracy, with the correct θ emerging from the projected effective Hamiltonian.

**Why it failed:** Full computation of all 600 tetrahedral cells of the 600-cell confirmed that the C3 symmetry is preserved exactly in 4D. All normal vectors n_i = n_j for all base vertices — the apex's 4D displacement is identical for all three base vertices. The 3D rotation V1→V2→V3→V1 does extend to an exact 4D isometry of the 600-cell, and C3 is not broken at any level of the geometry.

**Implication:** This was the most geometrically sophisticated candidate for θ within the cage framework. Its falsification closed the last plausible cage-geometry route. All 11 cage-geometry candidates exhausted. θ is definitively an electroweak quantity.

---

## SC-5: Electroweak Identification of θ with PMNS Phase Structure

**Targets:** OPEN-P-SM-7d (Koide phase θ)
**Origin:** Claude Sonnet, Session E, 24 March 2026; promoted to primary candidate after SC-2 through SC-4 falsified
**Status:** ACTIVE — primary candidate following exhaustion of cage-geometry approaches

**Mechanism:** The Koide phase θ appears in the charged lepton mass matrix in exactly the position occupied by the CP-violating phase δ_CP in the PMNS matrix. If θ = f(δ_CP, PMNS mixing angles), then θ is not derivable from the lepton cage geometry alone — it requires the full electroweak sector. The SM-4 structural impossibility theorem (no K3+SSV mechanism can select θ) is consistent with this identification: the EW sector is the only remaining source of symmetry breaking capable of splitting the antibonding degeneracy.

**Known numbers for comparison:**
- θ_Koide = 132.73°
- PMNS δ_CP ≈ 197° (NuFIT 5.3 best fit) — not directly equal to θ_Koide
- The full PMNS phase structure, when rotated into the charged lepton sector, may produce θ_Koide through a combination of charged lepton and neutrino rotation matrices

**Required development:** The EW series papers (EW-1 through EW-5) must be far enough developed to give the CPP electroweak coupling of the Capotauro bias to the K3 base. Until then, this candidate cannot be numerically tested. It is registered as the primary candidate after cage-geometry exhaustion.

**Tractability:** LOW in the near term. This is OPEN-P-EW-1 territory.

---

## SC-6: φ¹¹ and φ¹⁷ Exponent Derivation for Lepton Mass Ratios

**Targets:** OPEN-P-SM-5 (lepton mass mechanism), OPEN-P-SM-7d (tangentially)
**Origin:** Computed from observed masses, Session B, 24 March 2026
**Status:** ACTIVE — empirical observation; geometric derivation not yet found

**Mechanism:** Numerically, m_μ/m_e ≈ φ¹¹ to 3.8% and m_τ/m_e ≈ φ¹⁷ to 2.7%. The exponents have suggestive geometric interpretations: 11 = z − 1 where z = 12 is the 600-cell coordination number (removing one apex contribution), and 17 = z + 5 where 5 is related to the icosahedral faces per vertex. If these exponents can be derived from the 600-cell coordination geometry, they provide an independent check of the SM-4 Koide formula predictions.

**Required derivation:** Show that the lepton mass ratio involves φ raised to a power determined by the 600-cell coordination geometry, specifically that the exponent 11 encodes "full coordination minus apex" and exponent 17 encodes "full coordination plus icosahedral contribution." Currently the 3.8% and 2.7% deviations from exact φ-powers are consistent with higher-order corrections — they may be the signatures of the Koide phase corrections computed in SM-4.

**Connection to SM-4:** If φ¹¹ can be derived from cage geometry, it constrains the free parameter A in the SM-4 lepton mass formula. Currently A is calibrated to the electron mass; a geometric derivation of the inter-generation ratio would over-constrain the system and provide a falsification test.

**Tractability:** MEDIUM — requires group-theoretic analysis of the 600-cell adjacency structure and coordination geometry. One to two sessions.

---

## SC-7: Radial DP Chain Length as Classical Electron Radius

**Targets:** OPEN-P-QM-new-4 (derive r_chain from SSV₀ and sea_strength), OPEN-P-QM-new-5 (chain contribution to electron mass)
**Origin:** Partner-switching session, 30 March 2026 (PROP-5 in propositions.md)
**Status:** COMPUTED 30 March 2026 — r_chain ≠ r_e for any natural CPP scale; two findings emerged

**Mechanism:** The four radial DP chains extending from the tetrahedral cage vertices reach equilibrium where the central CP's SSV attraction is balanced by thermal Sea dissolution pressure. The equilibrium condition gives:

    SSV₀ / r_chain² = sea_strength × SSV₀ / d_Sea²
    r_chain = d_Sea / √sea_strength

where d_Sea is the mean DP separation in the Dipole Sea, estimated from the 600-cell lattice geometry.

**The single computation that tests this:** Evaluate d_Sea from the 600-cell lattice spacing (l_P) and the Sea packing density, then compute r_chain numerically. Compare to the classical electron radius r_e = e²/(4πε₀ m_e c²) = 2.82 × 10⁻¹⁵ m. If r_chain ≈ r_e, the equilibrium picture is confirmed and r_e is derived from CPP geometry rather than defined circularly.

**Constants available:** sea_strength = 0.1780 (THEO-SS-6), SSV₀ = 0.2555 MeV (SM-1 calibration), l_P = 1.616 × 10⁻³⁵ m.

**Implication if confirmed:** r_chain ≈ r_e would also immediately make PROP-12 (critical separation distance for pair production) a Tier 3 verification target, since r_crit uses the same formula.

**Implication if refuted:** The equilibrium condition is wrong, or d_Sea has the wrong identification. The chain equilibrium picture in PROP-5 needs revision.

**Computation result (30 March 2026):**

The calculation was performed for all physically motivated d_Sea identifications:

    d_Sea = l_P:                 r_chain ~ 10⁻²⁰ fm  (wrong by ~10²⁰)
    d_Sea = r_conf = 0.16 fm:    r_chain = 0.379 fm   (factor 7.4 from r_e)
    d_Sea = r_conf = 0.40 fm:    r_chain = 0.948 fm   (factor 3.0 from r_e)
    d_Sea = √(r_conf × r_e):     r_chain = 2.517 fm   (within 11%)

**Finding 1 — r_conf inconsistency:** sea_strength = 0.178, ħω₀ = 87.8 MeV, and r_conf = 0.16 fm are mutually inconsistent by a factor of 2.5×. Correct r_conf = 0.40 fm given the other two constants. Registered as OPEN-P-QM-new-9.

**Finding 2 — r_e in CPP terms:** r_e = α_fine × ħc/(2 × SSV₀) exactly. Confirming r_chain = r_e is therefore equivalent to deriving α_fine from 600-cell geometry (EW sector). SC-7 is now a corollary of that derivation.

**Next step:** Resolve OPEN-P-QM-new-9 (which of the three CPP constants is correct), then determine whether the corrected r_conf gives a geometrically motivated d_Sea that produces r_chain ≈ r_e.

---

## Status Summary

| ID | Target | Status | Tractability |
|----|--------|--------|-------------|
| SC-1 | OPEN-P-SS-1 (quark mass formula) | PARTIAL — C_n confirmed; top quark 103× off | — top quark needs different mechanism |
| SC-2 | OPEN-P-SM-7d (Koide phase θ) | FALSIFIED | — |
| SC-3 | OPEN-P-SM-7d (Koide phase θ) | FALSIFIED | — |
| SC-4 | OPEN-P-SM-7d (Koide phase θ) | FALSIFIED | — |
| SC-5 | OPEN-P-SM-7d (Koide phase θ) | ACTIVE — primary candidate | LOW (needs EW series) |
| SC-6 | OPEN-P-SM-5, OPEN-P-SM-7d | ACTIVE | MEDIUM |
| SC-7 | OPEN-P-QM-new-4, OPEN-P-QM-new-5, OPEN-P-QM-new-9 | COMPUTED — r_chain ≠ r_e; see findings | — |

**SC-7 result:** Computed 30 March 2026. r_chain ≠ r_e for any natural CPP scale. Two key findings: r_conf inconsistency (OPEN-P-QM-new-9) and r_e = α_fine × ħc/(2·SSV₀) exactly. See PROP-5 in propositions.md.
**Immediate priority:** SC-1 (quark mass ladder) and OPEN-P-QM-new-9 (r_conf inconsistency).
**Long-term:** SC-5 (EW connection for θ). Requires EW series development.

---

*All cage-geometry candidates for θ (SC-2, SC-3, SC-4, plus 8 additional mechanisms not recorded here) were exhausted by Session K, 25 March 2026. The structural impossibility result is proved in SM-4 Theorem THEO-SM-5 and registered as OPEN-P-SM-7d. θ is an electroweak quantity.*

*Independent review of session propositions: Claude Opus (Anthropic), 30 March 2026.*
