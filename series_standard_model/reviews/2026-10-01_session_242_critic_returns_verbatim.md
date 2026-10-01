# Session 242 — Fresh-Context Critic Returns, Verbatim

**Filed:** Patch 4364, 1 October 2026. Each report is the final message of an independent sub-agent with no stake in the
work, reproduced verbatim (AI output, not founder text). The fragment that acted on it:
`series_standard_model/axiom_maturation/4364_source_rule_injection_scales_with_psr_ball.md` (§5, §7). The critic's own
check script (`ref_check.py`) lived in a scratch directory and is not filed; its two decisive results (the scatter
kernel's far coefficient following R_f⁻², and the receiver-side β) are reproduced in `series_standard_model/code/4364_*`.


## Patch 4364 — Independent critic of the draft source rule (p = 3)

*Sub-agent id `abd3dd44cd7c352b5`.*

# Referee report: Patch 4364 (source rule)

I ran the script and reproduced its output. I also wrote my own check, `scratchpad/ref_check.py`, which tests the series expansion, compares two relay kernels, and tests vacuum fixed points. Every derivation below marked "mine" is my own.

## Claim 1: far-field coefficient set by the PSR at the source
**VERIFIED, but only for the kernel GR-1j wrote down. Wrong under the founder's emission picture.**
- **Discretisation checks out.** The sphere-mean formula (1/2rR)∫s u ds is right, including the r<R case. The piecewise-constant cell integral is fine. The u = C/r + D fit has residuals around 3e-5, and the uniform-case C is 0.47893 against 6/4π = 0.47746, a 0.3% offset. The ratios match R_s⁻² to within 3e-4.
- **"R at the source only" is partly an artefact of the profile.** The script's transition sits at r = 3 to 6, well outside the source. When I move it to r = 0.3 to 1.5, inside one PSR of the source, C/C₀ becomes 0.927 for (R_s, R_f) = (1, 1.2) and 1.214 for (0.9, 1). The correct statement is C = (6/4π)∫σ/R² dV, with R taken locally over about one PSR around the source. Physically this does no harm.
- **Major gap: the result depends on gather versus scatter (mine).**
  - GR-1j L208–211 uses M_{R(x)}, which is the receiver's own PSR (gather).
  - The founder's picture is different: DI-bits go "from every GP_origin to its GP_PSR" (4362, and AP-4). That is the origin's PSR (scatter).
  - I built the scatter operator as the volume-transpose of the script's kernel. Under it:
    - C follows R_f⁻², not R_s⁻²: (1, 1.2) gives 0.694 = 1.2⁻², and (0.9, 1) gives 1.000.
    - The vacuum is no longer Laplace: a constant u fails the fixed-point test by 3.5%.
  - So claim 1, and GR-1j's own exact-Laplace theorem, both hold only if the receiver sets the reach. That should be stated as a premise and put to the founder. It should not be assumed.

## Claim 2: local invariance iff p = 3
**The exponent is VERIFIED. "Exact, no second-order residual" is WRONG.**
- **What checks out:**
  - The scaling C ∝ q_s^(p−2), with distance read in local PSRs, gives δln q ∝ q_s^(p−3).
  - My check of the local acceleration: a_loc = a_coord/q³ and ∇_loc = q∇, so a_loc = −∇_loc ln q. Fixing δln q at a fixed local distance is therefore the right observable.
  - p = 0 gives (1+3U), and p = 2 gives (1+U). Both are correct.
- **The error (mine).** The ratified law gives ln q = −ε + ε³/6 + …, but the field response is the derivative: d ln q/dε = −1 + ε²/2. So G_loc and α_loc ∝ 1 − ε₀²/2. That is a second-order residual in the background. The draft's "O(ε³)" confuses ln q with its derivative. The script's part B hard-codes ln q = −ku, so it cannot see this.

## Claim 3: EIH check
**The coefficients are VERIFIED. Its standing as an independent LLR check is OVERSTATED.**
- **The EIH coefficients.** Will (TEGP, the N-body PPN equations) gives 1 − (2β+2γ)U₀ − (2β−1)U₀, which is 1 − 5U₀ in GR.
  - My independent check: inside a static shell in GR isotropic coordinates, x_loc = (1+U₀)x and τ = (1−U₀)t. This gives a_coord = (m/r²)(1−3U₀)(1+U₀)⁻² = 1 − 5U₀.
- **The CPP side.** For a static metric and a test particle at rest, d²x/dt² = −Γ^i₀₀ exactly, with Γ^i₀₀ = −½g^{ij}∂_j g₀₀ = q⁴∂_i ln q. So the receiver contributes q⁴ (matching 4 = 2β+2γ) and the source contributes q^(p−2) (matching 1 = 2β−1).
- **Coordinates are not a problem here.** For a constant U₀, harmonic and isotropic coordinates agree at linear order. Their difference enters at O(m_b²), not O(m_b U₀).
- **Why it is not independent.** A constant-U₀ test is the shell case. It is claim 2 restated in coordinates (local invariance), not a separate test. It is not what LLR actually measures, which is the Nordtvedt term, velocity and preferred-frame terms, and tidal and gradient terms.

## Claim 4: Tolman check
**VERIFIED as algebra. A fair separation, but not a derivation either.**
- **The algebra.** D^iD_iN = 4πGN(ρ+3p) is the standard static R₀₀ equation. On h = q⁻²δ, the conformal Laplacian q³∇²ln q is right; sympy gives 0 residual. Proper volume is the coordinate volume over q³, which agrees with rulers ∝ q. So ρ_prop = q³ρ_lat (my check), and s ∝ R²·q ∝ R³.
- **Caveat on "exact."** The exponential metric does not satisfy the R_ij equations beyond 1PN: g_ij = 1 + 2U + 2U², where Schwarzschild has 3/2 U². Only R₀₀ is exact here, which is enough for p at O(U₀).
- **Circularity.** It is not circular with respect to Einstein (GR-1j L158–159 bars that). But claim 2 does not derive p either: it imposes LPI and solves for p. Both the Tolman check and claim 2 agree because both encode local invariance. The honest word is "required by", not "derived". Extending the founder's α ratio principle to G rests on his broader clause "no laboratory measurements change" (founders_voice/4360). That reading is defensible.

## Claim 5: receiver-side versus source-side compensation
**The algebra is VERIFIED. The conclusion "no tension" is OVERCLAIMED.**
- **The algebra.** In PPN, a = (1 − 2(β+γ)U)∇U. Matching −(4+j) gives β = 1 + j/2, and j = 3 gives 5/2. This agrees with 4361 §2, which is the same q⁻³ structure, since (1+3U)^(−1/3) = 1 − U + 2U².
- **Missing point.** Receiver-side w also breaks A3′'s "geodesics of the assembled metric" (axiom-registry L39). That is a second reason to reject it.
- **Where the conclusion goes too far.** The source-side factor is constant only for a point-like body; see claim 8. The ε₀²/2 residual from claim 2 survives at p = 3. It is 9× smaller than 4360's 4.5ε². Its annual swing is ε₀·dε, which is about 3.3e-18 (0.27× the bound) if ε₀ = U_sun. The k·SSV_abs,0 = 1/3 condition is indeed no longer needed.

## Claim 6: the founder's (b)
**PARTLY FAIR, PARTLY CONVENIENT.**
- **Where 4364 is right.** 4360 §3, "total fixed", does contradict the founder's clause "its total over the sphere is a little less". 4359 §4 had also framed (b) as the passing option.
- **Where it is selective.**
  - "A little less" means any p > 0, not specifically 3.
  - p = 3 needs every GP in the ball to be reached. The registered landing is a band of N bits (R-DIBIT-COUNT-AT-FLOOR, axiom-registry L401–406). With N fixed and the same push per bit, the total is fixed, which is p = 0.
  - The founder's 4361 statement, "the GP_PSR band receives the same message from GP_origin regardless" of SSV_abs, was made about the charge's signal. Read literally, it gives p = 0.
- **Can any realisation work?**
  - Payload weight ∝ R_origin³ changes the message, which conflicts with 4361.
  - Receiver weighting by hop length is allowed as receiver-computed state (AP-4d). But it must touch only the CP-resident part, or the vacuum statics stop being Laplace. AP-4's E is a single summed vector, "resident CPs together with those integrated" (axiom-registry L35), so a receiver cannot separate source from relay.
  - The only consistent site is therefore the origin GP scaling its resident contribution. That requires reading "same message" as same count and form, not same magnitude. The draft should say so.

## Claim 7: the galactic potential
**The arithmetic is VERIFIED (3.0e-15, about 247×). It cuts against the draft itself.**
- GR-1j L193 defines u as a departure from the homogeneous Sea, so it is absolute.
- If ε is absolute, the p = 3 residual swing is ε₀·dε ≈ 1e-6 × 3.3e-10 = 3.3e-16, about 27× the bound. The tension reappears for p = 3.
- Worse, the Local Group and the cosmological potential make ε₀ ≳ 1e-5, or even O(1). At that size the PSR-law expansion, and Mercury's calibration of the ½, become ill-posed.
- Possible factor of 2: dε = 2eU is peak-to-peak, while the bound is described as an amplitude.

## Claim 8: self-gravitating bodies
**CORRECTLY OWED, but understated.**
- **What is right.** Σm_i q_i = m − Σm_iU_i = m − 2|E_g| is correct (mine). GR's Tolman mass is m + E_int − |E_g|, with the 3p term supplying +|E_g| by the virial theorem. GR-1j L410–416 does defer pressure.
- **What is missed:**
  - **Sign problem.** The trace source is ρ − 3p, so a trace-sourced scalar gets the 3p with the wrong sign (−3|E_g|). The vector and tensor channels would have to supply +6p, not +3p.
  - **It is a falsifier, not just an owed item.** If unrepaired, the active and passive mass mismatch is about |E_g|/mc² ≈ 4.6e-10 for Earth and 1.9e-11 for the Moon. Against LLR's roughly 1e-13 on the Earth–Moon ratio, that is excluded by about 10³.
  - **The wrong masses are named.** Nordtvedt's η_N concerns passive versus inertial mass. Active-mass equality is a separate test (Bartlett–van Buren). The passive and inertial masses of a self-gravitating body in CPP are not stated.
  - **"Per CP" is the wrong carrier.** GR-1j's source is the compressed-DP census excess (L419–425), not a CP count. Whether nuclear and other binding energy carries active mass, a WEP-active composition question, is unaddressed.

## What the draft missed
1. **Gather versus scatter** (claim 1). This is the decisive premise behind everything.
2. **The ε₀²/2 residual** from the ratified law. It is not exact.
3. **Preferred-frame effects.** CPP has an absolute Nexus frame. LLR bounds α₁ at about 1e-5, the solar spin axis bounds α₂ at about 1e-9, and the solar system moves at 370 km/s relative to the CMB. A moving source's rule (Lorentz-contracted PSR) is owed.
4. **Self-consistency.** q_s includes the source's own field, so a point source is ill-defined. The rule is nonlinear for compact bodies.
5. **Velocity terms at 1PN.** Only the static U₀ coefficient was checked.

## Verdict on the headline
**Overclaimed.**
- **Supportable:** if the relay is gather (receiver PSR) and LPI is imposed, p = 3 is the unique power-law source rule. It gives G and α invariant to first order in U₀, with no k·SSV_abs,0 condition.
- **Not supportable:**
  - "Must": the rule is conditional on the kernel and imposed, not derived.
  - "Exactly": there is a ½ε₀² residual.
  - "The tension does not arise": it falls 9× and passes only if ε₀ ≈ U_sun. On the draft's own claim 7 premise it fails by about 27×.
- **On "a physical question for the founder":** fair, but the draft should state plainly that his 4360 and 4361 statements, read literally, imply p = 0. It should also ask which PSR sets the reach, the origin's or the receiver's.

## Plain Language summary
The draft says a mass or charge sitting deeper in a gravity well must push the grid harder, by exactly the cube of how much its grid spacing has shrunk. With that rule, gravity's strength and α come out the same in every lab. That cube rule really is the only one that keeps lab measurements unchanged, but only if the receiving grid point, not the sending one, sets how far a message reaches. I ran it the other way and the result reverses.

The draft also overstates its case in three places:
- **"Exactly"** is not true: the Mercury-tuned shrinkage law leaves a small second-order leftover.
- **"No tension"** holds only if the Sun's pull is all that counts. If the Galaxy's pull counts too, which the draft's own side note assumes, yearly clock tests would see the leftover at about 27 times their limit.
- **Self-gravitating bodies** are an open failure risk, not just an item to finish later. Without a pressure fix, the Earth and Moon would fall toward the Sun differently, at about a thousand times what lunar laser ranging allows.

---

## Claude's response to the return (Patch 4364, not part of the verbatim report)

- **Kernel:** accepted and reproduced (the scatter far coefficient follows R_f⁻²). The critic's "the result reverses"
  holds for the *far* field across a gradient. Near the source, in a region of uniform PSR, both kernels give R_s⁻² to
  0.3% (fragment §1 table), so the local-invariance requirement p = 3 does not depend on the kernel. GR-1j's
  exact-Laplace theorem does depend on it → TODO-4364-KERNEL.
- **ε₀²/2:** accepted for G. Whether α carries it depends on whether the charge reading has the lapse's sensitivity.
  That is inferred, not shown, and owed → TODO-4364-EPSABS.
- **"Derived" → "required":** accepted.
- **Self-gravitating bodies:** accepted as an open test (TODO-4364-SELFGRAV). One correction to the report's framing:
  the |E_g|-sized gap is not introduced by p = 3. GR-1j's implied p = 2 leaves the same size with the opposite sign.
- **Preferred frame:** accepted → TODO-4364-PREFFRAME.
- **"Per CP" vs census excess (GR-1j L419–425):** accepted as wording. The fragment speaks of "a source's injection";
  the carrier is GR-1j's census excess.
