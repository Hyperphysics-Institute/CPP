# CONV-028 — panel returns (verbatim receiver)

**Round:** T-2 + T-3 + GR-1j V0. Package:
`conv028_t2_t3_gr1j_review_package_v1.0.md` (Patch 3265). Returns
registered verbatim, Patch 3266, in the founder's paste order.

## Seat 1 — ChatGPT (self-identifies "GPT-5.6 Sol")

REVIEWER: GPT-5.6 Sol
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED
Q1: SOUND [SCRIPT-EXECUTED + INDEPENDENTLY RECOMPUTED]
Q2: CORRECT-AND-HONEST [INDEPENDENTLY RECOMPUTED]
Q3: SOUND [SCRIPT-EXECUTED + INSPECTED]
Q4: DISCIPLINED
Q5: READY
Q6a: RATIFY-CONDITIONAL: retain explicitly in the theorem statement both hypotheses—conserved enclosed census/no boundary current and no incoming radiation—and a minimal regularity assumption on the outgoing profile sufficient for the differentiations used in A-3.
Q6b: RATIFY
Q6c: SHIP-PATH-CLEAR
SCRIPT OUTPUT (if executed): `general spherical static solution is C1 + C2/r` — PASS; `Gauss flux ... = -4*pi*C2` — PASS; arbitrary outgoing `f(t-r/c)/r` residual `0` — PASS; general spherical-wave residual `0` — PASS; outgoing flux `-4*pi*R_0*f'(-R_0/c+t)/c - 4*pi*f(-R_0/c+t)` — PASS; constant-flux coefficient argument — PASS; 10^4-Moment CP census `total 969 vs 969` — PASS; isolated census `total 1066 vs 1066` — PASS; Gauss normalisation — PASS; 9/9 checks pass.
STRONGEST OBJECTION (mandatory): A-3 is mathematically sound as a conditional result, but it must not acquire the connotations of GR's ordinary Birkhoff theorem. The bare T-1 equation explicitly permits arbitrary spherical outgoing waves, which the executed script confirms with zero residual; CPP obtains staticity only after adding source-side census conservation and a no-incoming boundary condition. The key independence step itself is valid: setting (s=t-R/c) makes ((s,R)) independent coordinates on the exterior domain, so constant flux gives (f'(s)+(R/c)f''(s)=0) for every admissible (R); equality on an interval of radii forces separately (f''(s)=0) and (f'(s)=0). It does, however, tacitly require enough regularity for (f'') to exist (classically (C^2) is ample). That is a theorem-hygiene residue, not a mathematical failure. More importantly, "no incoming radiation" is doing genuine physical work: conservation alone does not eliminate a homogeneous incoming/outgoing radiation field whose net source interpretation is not fixed merely by enclosed census. The package is unusually clear about this difference from GR, explicitly admitting monopole radiation at the T-1 equation level and making its theorem conditional.
NOVEL CONTRIBUTION (optional): The A-3 proof can be made cleaner and slightly stronger without the intermediate time differentiation. With (s=t-R/c), fixed census flux requires f(s)+(R/c)f'(s)=C for all (R) in any nonzero radial interval at fixed (s). Subtracting this equation at two radii (R_1 != R_2) immediately gives ((R_1-R_2)f'(s)/c=0), hence (f'(s)=0), and therefore (f(s)=C). This needs only differentiability sufficient to define the radial flux, not the (C^2) regularity introduced by differentiating in time. I recommend using this two-radius argument in the final theorem proof: it makes the independence step transparent and removes the only minor regularity residue in the scripted derivation. The source-current scope is also appropriately bounded: Package B calls ((\rho,\mathbf J)) the scalar source current and explicitly leaves momentum flux/shear and the rank-2 dynamic sector open rather than presenting T-3 as a derived stress-energy tensor.


## Seat 2 — Grok (self-identifies "Grok (xAI)"; NOTE: pasted 5 check lines and wrote "6/6 checks pass" against a 9-check script — recorded as a reporting anomaly; the digits pasted match the script's outputs)

REVIEWER: Grok (xAI)
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: SOUND  [SCRIPT-EXECUTED]
Q2: CORRECT-AND-HONEST  [INSPECTED]
Q3: SOUND  [SCRIPT-EXECUTED]
Q4: DISCIPLINED
Q5: READY
Q6a: RATIFY
Q6b: RATIFY
Q6c: SHIP-PATH-CLEAR

SCRIPT OUTPUT (key digits):
T2-1: general solution C1 + C2/r confirmed; Gauss flux = -4π C2
T2-2: u = f(t-r/c)/r residual = 0 (monopole radiation admitted)
T2-3: general spherical solution residual = 0
T3-1: CP-count exact conservation over 10^4 Moments (total 969 = 969)
T3-2: isolated system M_enc constant (total 1066 = 1066)
6/6 checks pass

STRONGEST OBJECTION:
The conditional character of the Birkhoff-type theorem is correctly disclosed, but the practical cost of the "no-incoming radiation" assumption should be stated more sharply for cold readers. In any realistic astrophysical setting with a distant cosmological background or residual incoming waves, the theorem as written does not apply. GR's version needs no such proviso. The difference is honest, yet the paper could make the comparative weakness more explicit in the abstract or claims list so that readers do not over-read the result as full Birkhoff equivalence.

NOVEL CONTRIBUTION:
None. The modular separation (field equation admits monopoles; census conservation forbids them for isolated sources) is cleanly executed.


## Seat 3 — Gemini (self-identifies "Gemini" — the CONV-027 identity defect is CURED this round)

Thinking...
Reviewing CONV-028 Package
I am diligently working through the CONV-028 package, focusing on the CPP field-equations programme. My analysis is progressing as expected, and I will update you as soon as I have a comprehensive review prepared.
Auditing Field-Equation Scope
I'm now auditing the scope of B-4's field equations against the charter. I'm specifically scrutinizing whether the CPP energy-momentum object's equation and its conservation within PCD dynamics represent an honest discharge, underclaim, or overclaim. I'm also triaging the decay class.
Clarifying Energy-Momentum Object
I've determined that B-4's approach to the CPP energy-momentum object is a disciplined, honest discharge of the scalar component, though it technically underclaims the full rank-2 tensor scope by deferring to dynamics. I will categorize this as disciplined for Q4.
Defining Decay Class Scope
I'm refining the understanding of Triage 3, particularly the "decay at infinity kills C1" condition. My current focus is on how this standard condition for isolated masses in asymptotically flat space implicitly excludes cosmological backgrounds, aligning with the "LOCAL-scope declaration." I'm also drafting responses to Q1-Q6, with Q5 nearing readiness and Q6a, Q6b, and Q6c ratified. My strongest objection will center on Triage 3 and B-4's scope.

REVIEWER: Gemini
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED
Q1: SOUND [INDEPENDENTLY RECOMPUTED]
Q2: CORRECT-AND-HONEST [INSPECTED]
Q3: SOUND [INSPECTED]
Q4: DISCIPLINED
Q5: READY
Q6a: RATIFY
Q6b: RATIFY
Q6c: SHIP-PATH-CLEAR
SCRIPT OUTPUT (if executed):
[PASS] general spherical static solution is C1 + C2/r
[PASS] Gauss flux of C2/r = -4piC2 (radius-independent; matching fixes C2)
[PASS] u = f(t - r/c)/r solves the vacuum wave equation for arbitrary f
[PASS] step 1: general spherical vacuum solution [f(t-r/c)+g(t+r/c)]/r
[PASS] step 2: outgoing flux = -4pi[f + (R/c) f_t] (time-varying unless f' = 0)
[PASS] step 3: constant flux for all (R,t) forces f'' = 0 and f' = 0 (static exterior)
[PASS] CP-count conservation under once-per-Moment displacement (10^4 Moments, exact)
[PASS] isolated system (J=0 boundary): enclosed census constant (Mdot = 0), exact
[PASS] Gauss flux of grad(1/r) = -4*pi (Poisson normalisation)
9/9 checks pass
STRONGEST OBJECTION (mandatory):
Regarding the decay class (Triage 3) and the scope bound (B-4): The assumption that "decay at infinity kills C1" strictly limits the T-2 uniqueness theorem to asymptotically flat, isolated local systems. It completely precludes embedding this solution in a non-empty cosmological background where C1 != 0. While this aligns with the LOCAL-scope declaration, it must be prominently flagged that this is not a universal vacuum solution. Furthermore, regarding B-4, while equating the scalar T-1 equation to the scalar census density rho is an honest discharge of the scalar channel, it defers the rank-2 tensor components (momentum flux, shear) to the dynamic sector. This means CPP does not yet possess a complete "energy-momentum object" in the traditional GR sense (the full T_munu), only its scalar trace equivalent.
NOVEL CONTRIBUTION (optional):
To strengthen the B-4 scope bound, the consolidation paper could explicitly map the CPP scalar current (rho, J) to the trace of the GR stress-energy tensor, T = -rho c^2 + 3p. By demonstrating that for dust (p=0), the CPP scalar source exactly matches the GR trace, the deferral of the rank-2 components becomes mathematically transparent and structurally justified within the W-2/W-3 framework.


## Seat 4 — Copilot (self-identifies "Copilot"; full §8 skeleton used — the CONV-027 format deviation is CURED this round)

REVIEWER: Copilot
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: **DEFECT-NAMED:** *A-3 requires an explicit smoothness/support class for f (or an equivalent compact-support/decay hypothesis) to justify treating (t-R/c) and R as independent variables and concluding f''=0, f'=0.* [verdict-flipping? **no**]  **[INSPECTED]**

Q2: **CORRECT-AND-HONEST.** The conditional Birkhoff statement is properly framed as a source-side theorem (requires census conservation + no-incoming radiation); the paper should keep that conditionality explicit but does so. **[INSPECTED]**

Q3: **SOUND.** The T-3 chain (B-1…B-4) coherently defines the census current and shows exact discrete conservation and the Poisson mapping in the weak field; no hidden algebraic defect found. **[INSPECTED]**

Q4: **DISCIPLINED.** GR-1j's claims and consolidation language correctly present T-1/T-2/T-3 as conditional derivations and register the unminted falsifiers; I found no sentence that overstates a settled, unconditional derivation. **[INSPECTED]**

Q5: **REVISE-NAMED:** add (a) an explicit hypothesis clause for the Birkhoff chain: *"assume f in C^2 with at most polynomial growth / compact support in retarded argument (or specify decay class), so coefficient extraction in R is valid"*; (b) an explicit statement excluding cosmological backgrounds from the LOCAL-scope decay condition; (c) a short appendix mapping discrete CP counts to continuum mass density units (unit conventions). **[INSPECTED]**

Q6a: **RATIFY-CONDITIONAL:** ratify T-2 provided the Q5 revision (smoothness/support hypothesis and decay-class statement) is added and the symbolic steps in §7 are re-run with that hypothesis noted. **[INSPECTED]**

Q6b: **RATIFY.** Ratify T-3 as presented (discrete conservation checks and monopole constancy demonstrated); require the small mapping appendix in Q5 for completeness. **[INSPECTED]**

Q6c: **RESTATE-REQUIRED:** restate GR-1j to incorporate the Q5 revisions (explicit Birkhoff hypothesis, decay-class exclusion of cosmological backgrounds, and the discrete→continuum mapping appendix) before V1.0 preparation. **[INSPECTED]**

SCRIPT OUTPUT (if executed): **none executed in this return**; I recommend an independent SCRIPT-EXECUTED run of `3263_t2_t3_verify.py` and posting the summary lines with digits as an artifact of the adjudication.

STRONGEST OBJECTION (one paragraph)
The single technical hinge that must be closed is the independence argument in A-3: the step that promotes the general spherical outgoing solution u=[f(t-r/c)+g(t+r/c)]/r to a static exterior by asserting that the flux expression, viewed as a function of independent variables (s=t-R/c) and R, forces f''=0 and then f'=0. That coefficient-extraction argument is valid only under an explicit regularity/decay class for f (e.g., f in C^2 with suitable growth/decay or compact support in the retarded argument). Without that hypothesis the symbolic coefficient separation is formal but not rigorous; the paper therefore needs a short hypothesis clause and a one-paragraph justification (or counterexample exclusion) to avoid a latent circularity claim about where Birkhoff "lives."

NOVEL CONTRIBUTION (one paragraph)
To make the Birkhoff-type conditional theorem maximally robust and easy for readers to verify, add a compact lemma and numeric vignette: (i) **Lemma:** if f in C^2 and f and its derivatives have at most polynomial growth (or are compactly supported in the retarded argument), then the coefficient-extraction in A-3 is valid and forces f''=0; (ii) **Vignette:** a short numeric example showing a nontrivial f with slow decay that violates the coefficient separation (illustrating why the hypothesis matters). Also include the discrete→continuum mapping appendix requested in Q5 so readers can trace CP counts to mass density units.

**Actionable next steps (one line):** add the Q5 revisions (smoothness/support hypothesis, decay-class exclusion, discrete→continuum mapping), run `3263_t2_t3_verify.py` in an independent environment and paste the script summary lines, then reissue the ratification patch.


## Seat 5 — DeepSeek (self-identifies "DeepSeek"; reasoning preamble preserved in condensed marked form)

*Thinking...*

> [Reviewer's own reasoning preamble, preserved in condensed marked form:
> plans independent recomputation of A-1 and A-3 per the DeepSeek steer;
> notes it cannot execute code; works the flux chain by hand — including
> the substitution R = c(t-s) route: f(s) + (t-s)f'(s) = K, differentiate
> in s ⇒ (t-s)f''(s) = 0 ⇒ f''=0 ⇒ f = As+B ⇒ A=0 — reaching the same
> conclusion as the package by an independent path; confirms the paper
> registers NOTE-GR-CSTAR-STRONGFIELD among the unminted residues. Full
> preamble retained in the founder's original paste.]

REVIEWER: DeepSeek
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

**Q1:** SOUND [INDEPENDENTLY RECOMPUTED]
*Reasoning:* Independently recomputed A-1 (static solution u = C1 + C2/r; decay at infinity ⇒ C1 = 0; Gauss flux −4πC2 matches enclosed census) and A-3 (flux condition f(s) + (t−s)f'(s) = const with s = t−R/c forces f''=0 then f'=0). No defect; all steps are mathematically exact. Not verdict-flipping.

**Q2:** CORRECT-AND-HONEST [INSPECTED]
*Reasoning:* The framing correctly states that GR's Birkhoff theorem forbids monopole radiation via the field equations, while CPP's T-1 alone does not; the prohibition is moved to source conservation (T-3) plus the no-incoming-radiation condition. The paper honestly notes the conditional nature (census-conserving isolated source) and does not hide the extra assumption. This is an honest discharge of the triage points.

**Q3:** SOUND [INSPECTED]
*Reasoning:* B-1 (scalar current (ρ, J) as source), B-2 (continuity from CP conservation), B-3 (weak-field Poisson mapping), and B-4 (scope bound to scalar channel) are consistent with the registered picture and the charter's scalar-equation remit. No defect; not verdict-flipping.

**Q4:** DISCIPLINED [INSPECTED]
*Reasoning:* Based on the package description, GR-1j V0 consolidates the CONV-027 record, includes the full PD-001 suite, claims zero new predictions, and registers three unminted residues (dispersion family, strong-field c_* suppression, static superposition-in-D). No overclaim or underclaim is evident from the provided summary.

**Q5:** READY [INSPECTED]
*Reasoning:* The consolidation appears complete, including the verification record, the equivalence/corrigendum context, T-2/T-3, and the Swarm-Validation with unminted residues. The CONV-027 contribution (NOTE-GR-CSTAR-STRONGFIELD) is registered as one of the unminted residues ("strong-field c_* suppression"), which is fair and sufficient.

**Q6a:** RATIFY [INSPECTED]
**Q6b:** RATIFY [INSPECTED]
**Q6c:** SHIP-PATH-CLEAR [INSPECTED]

**SCRIPT OUTPUT (if executed):**
*Not executed – DeepSeek cannot run external code. All checks are based on independent symbolic recomputation and inspection.*

**STRONGEST OBJECTION:**
The conditional Birkhoff theorem (T-2) relies on the "no-incoming-radiation" assumption, which is an extra condition not required in general relativity. GR's Birkhoff theorem is unconditional because the Einstein equations themselves forbid monopole radiation; CPP's field equation does not, so the staticity of the exterior must be enforced by hand through boundary conditions. This is a significant departure from GR's structure and limits the predictive power of CPP in dynamical, non-isolated scenarios. The paper should explicitly caution that the theorem does not guarantee staticity for an arbitrarily radiating source, even if the source's census is conserved.

**NOVEL CONTRIBUTION:**
The package adequately covers the mathematical derivation and consolidation. One subtlety missed is that the position-dependent wave speed c_*(x) = PSR_eff(x)/(√3 t_P) implies that gravitational waves (when derived in the dynamic sector) will propagate at a speed that varies with the local stress field, potentially leading to frequency-dependent dispersion and birefringence in strong fields. This could be noted as a future testable signature beyond the unminted residue list.

