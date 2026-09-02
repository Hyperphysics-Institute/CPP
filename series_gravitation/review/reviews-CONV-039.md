# CONV-039 — Returns receiver: the parity theorem, the trace wall, the a = 0 lines, the Kerr wall map, the odd sector

**Dispatched:** Patch 3380, 2 Sep 2026 (Session 161), on the founder's instruction ("please initiate review protocol") after the worker's economy-protocol assessment at 3379 (trigger 2a on the Kerr wall map; partial win on the theorem and the a = 0 lines).
**Package:** `conv039_parity_trace_wall_kerr_map_review_package_v1.0.md` (CONV-001 single block; 3378/3379 records and scripts inlined; 3375–3377 as context). Scripts ship separately for own-run.

**What this round gates:** whether the parity theorem and the trace-derived Robin wall stand (Q1); whether the a = 0 extraction and its −13.4% shift are real (Q2); **the METHOD for the Kerr wall map (Q3)** — the worker's declared exhaustion; what governs the odd sector (Q4 — may route to the founder); GR-2's honest V1.8 sentence (Q5); the two unexplained regularities (Q6).

**Binding rules:** majority per question; UNSOUND on Q1(i) voids the wall law; NO-VIABLE-ROUTE on Q3 registers the Kerr recompute as standing OPEN; VECTOR-SECTOR-RULE-NEEDED on Q4 routes to the founder; UNDERIVED-BOTH-SECTORS on Q5 obliges the sentence into GR-2 V1.8.

**Seat mandates:** IDENTITY, OWN-RUN (3378 17/17; 3379 12/12), EK-1 sealed key (SHA-256 in package §6), COUNT-LINE, TIER, inline returns.

**Returns: 5/5. EK-1: 2 of 5 hash-matched (GPT, Grok — computed from the exact laws); Gemini, Copilot, DeepSeek returned the values obtained by plugging the package's ROUNDED coefficients (b2 = 1.5922–1.5923, b3 = 1.9725) — graded INSPECTED. Adjudicated Patch 3381: `conv039_adjudication.md`.**

---

## Seat 1 — GPT — EK-1 HASH-MATCH (execution-verified; SCRIPT-EXECUTED both)

```
REVIEWER: GPT-5.6
TIER LEGEND USED: T1 = own-executed symbolic/numerical verification; T2 = mathematical and numerical-method audit; T3 = CPP physical-dictionary, slicing, or boundary-response claim requiring additional derivation

Q1: (i) SOUND-WITH-CAVEATS; (ii) SOUND-WITH-CAVEATS; (iii) CORRECT-WITH-CAVEATS [T1/T2/T3] — Both reconstruction formulas agree symbolically, and the code verifies that a generic harmonic Zerilli solution has nonzero H₂−K in the stated RW gauge. This establishes that the scalar conformal factor is not the complete even-parity wave. It does not establish that a conformally flat three-metric can contain no wave information at an isolated slice, because radiative data can also reside in the extrinsic curvature. The trace relation δlnψ⁴=(H₂+2K)/3 and the resulting βℓ(ω) algebra reproduce, but "register pinned ⇒ trace pinned" remains conditional on identifying CPP absolute-time slices with the Schwarzschild slicing and on zero trace compliance. CONV-038's one-Moment-delay compliant response does not by itself imply δtrace=0. Thus βℓ is correct for the stated trace-Dirichlet boundary model, not yet an unconditional CPP wall law.

Q2: SOUND-WITH-CAVEATS; shift UNDETERMINED [T1/T2] — I reproduce both scans and the stated centroids. Subtracting 4b₂ shows that the raw delay is not wholly the isolated wall contribution, but scattering delays in a barrier-plus-dispersive-wall system do not generally decompose into a uniquely additive "flat-wall delay + cavity delay." The half-maximum centroid also compares a broad plateau with a narrow feature. A direct complex-pole calculation using the frequency-dependent Robin condition, plus locator variation, is required before −13.4% is certified as a resonance displacement rather than a Wigner-locator effect.

Q3: RECONSTRUCTION-REQUIRED; cost LITERATURE-PROJECT [T2/T3] — Use Hertz-potential/CCK reconstruction from the Teukolsky solution, followed by an explicit gauge transformation from ingoing or outgoing radiation gauge into a regular, surface-adapted gauge in which the CPP absolute-time spatial trace is defined. Then impose the trace response on the physical wall worldtube and translate it back into a boundary operator on the Teukolsky/SN amplitudes. The construction must include reconstruction completion terms, gauge regularity at the timelike surface, tetrad choice, surface displacement, and spin-induced harmonic/parity mixing. At generic Kerr spin there is no invariant global even/odd split, so a Chandrasekhar "Kerr-Zerilli" potential cannot simply inherit the Schwarzschild trace law. A slow-spin truncation at χ=0.68 is not controlled without computed higher-order convergence.

Q4: VECTOR-SECTOR-RULE-NEEDED [T3] — The scalar register does not determine the axial response, but that does not prove the odd response is nonexistent or permanently underivable. A candidate SSV_net/vector rule must specify a causal surface impedance; conserve total perturbative flux or explicitly identify other channels; recover a definite axial Regge–Wheeler boundary law as a→0; respect rotational mode coupling; and generate the Kerr boundary matrix without inserting X=0 by convention. It should also state whether even and odd responses remain independent at a=0 or are linked by the substrate dynamics.

Q5: UNDERIVED-BOTH-SECTORS [T2/T3]; SENTENCE: "The published 188–194 Hz line is conditional on an imposed axial X=0 wall; CPP presently derives neither the Kerr even-sector trace map nor the odd/vector-sector response, so no Kerr echo frequency is yet derived." — At a=0 there is a conditional even-sector trace-wall calculation, but the shipped Kerr axial wall is underived and no Kerr even-sector wall has been constructed.

Q6: UNDETERMINED [T2] — Two multipoles cannot establish either regularity as structural. Decide with direct complex poles, several independent resonance locators, ℓ≥4, variation of r_w, and an analytic large-ℓ comparison of the zeros of βℓ with the Zerilli barrier maxima. Stability of the fractional shift under those changes would support structure; movement with centroid convention would identify an artifact.

Q7: ITEMS-FOUND [T2/T3] —
1. "A conformally-flat spatial slice cannot carry an even-parity gravitational wave" is broader than the demonstrated harmonic RW-gauge spatial-metric statement; extrinsic-curvature radiative data are not excluded.
2. "Register pinned" is treated as zero trace perturbation although the inherited physical picture is a one-Moment-delay compliant response.
3. "The axial sector is not governed by the register at all" should read "not governed by SSV_abs alone"; a vector-sector SSV_net rule remains possible.
4. "Strong near-trapped modes" exceeds the Wigner-delay evidence until complex poles are located.
5. The exact −13.4% equality is based on two modes and a shared centroid prescription and must remain provisional.
6. The 166/250 Hz Kerr scaling is not a spectral result and should remain outside prediction language.
7. "Even sector" and "odd sector" cannot be carried unchanged to generic Kerr without addressing spin-induced parity and harmonic mixing.
8. The proposed restatement presents H₂+2K=0 as imposed by the surface rather than conditional on the zero-compliance trace model and slicing identification.

Q8a: PROPER-WITH-REVISIONS  Q8b: RESTATE-REQUIRED [T2/T3] — The parity audit correctly invalidates the shipped X=0 wall as a derived CPP condition and identifies the proper Kerr reconstruction problem. Enactment should retain the a=0 Robin computation as conditional, describe the Wigner features rather than confirmed modes, mark −13.4% provisional, and distinguish SSV_abs insufficiency from the still-open vector response.

SCRIPT: SCRIPT-EXECUTED
3378 verify: 17 passed, 0 failed
3379 verify: 12 passed, 0 failed

EK-1: b2=1.5919;b3=1.9733;a3=10.0104

DEFECTS/OBJECTIONS:
1. The recalled reconstruction formulas were mutually checked but not independently checked against a primary-source convention.
2. The CPP absolute-time slice has not been mapped to the Schwarzschild perturbation slicing.
3. Zero trace perturbation is stronger than the previously retained compliant one-Moment-delay boundary picture.
4. Flat-wall phase subtraction does not by itself isolate a unique cavity lifetime in the combined scattering problem.
5. No complex pole confirms either reported near-trapped feature.
6. Generic Kerr requires a coupled, gauge-controlled metric boundary map, not a scalar rescaling of the Schwarzschild result.
7. The odd/vector-sector physical response remains absent.
```

## Seat 2 — Grok — EK-1 HASH-MATCH (execution-verified; INDEPENDENT-HARNESS with sources open)

```
REVIEWER: Grok (xAI)
TIER LEGEND USED: RECORD / ALGEBRA / LITERATURE / JUDGEMENT / OPEN-DEPENDENCY
Q1: (i) SOUND-WITH-CAVEATS; (ii) SOUND-WITH-CAVEATS; (iii) CORRECT-WITH-CAVEATS [LITERATURE+ALGEBRA] — T-1: L1 is not a recollection-only check. Lousto–Price 1997 (gr-qc/9705071) give, in RW gauge, K = [6M²+3Mλr+λ(λ+1)r²]/[r²(λr+3M)] ψ + f ∂rψ and the matching H₂(ψ,ψ′,ψ″); Moncrief's definition inverts to H₂ = Λ/(rf)[(λ+1)ψ/r − K] + r K′. Those are exactly the two formulas in 3378; they agree identically once Z″ is eliminated by the Zerilli equation (own sympy). λ = (ℓ−1)(ℓ+2)/2 is the LP/Moncrief convention (ℓ=2 → 2, ℓ=3 → 5), consistent with Martel–Poisson's μ = 2λ. L2: c₂ = −M(λr+3r−3M)/(r(λr+3M)) ≠ 0 and c₁ carries ω², confirmed. L3: with G=h₁=0 the residual ξᵗ∂ₜ on static Schwarzschild leaves g_rr and g_θθ unchanged, so H₂−K is gauge-fixed-invariant on that slice. Caveats: L3 is RW-gauge residual only, not full 4-diffeomorphism invariance of a 3-trace; "cannot carry an even wave" means the conformal *register* is not the wave (H₂−K is the wave), not that even GW is forbidden as an extra field. (ii) δ ln ψ⁴ = (H₂+2K)/3 is the correct linearized spatial-trace map on a t=const Schwarzschild slice; identifying that slice with CPP Absolute-Moment time is unproven at linear order (lapse/shift pollution if the slicings differ). (iii) β₂M = 2.4959−14.464(Mω)² and β₃M = 6.1553−16.728(Mω)² at r_w=9M/4 reproduce the stated 2.496−14.46 and 6.155−16.73; Neumann roots 0.415 / 0.607 hold. Caveat: r_w=9M/4 is the CONV-038 *extremal* edge of a conditional window 0.536<u_max≤1, so β_ℓ is the wall law at that radius, not a radius-independent identity.
Q2: SOUND-WITH-CAVEATS; shift UNDETERMINED [JUDGEMENT] — |R|=1 and a large cavity delay after subtracting 4b₂ at the Neumann crossing are robust (the raw delay peak sitting on the crossing is the wall's own dφ/dω, correctly removed). The derived-wall feature at 0.412 / 0.604 is therefore real as a near-crossing peak. The −13.4% is a ratio against a Dirichlet *centroid-over-half-max* on a broad plateau: 3378 located Dirichlet at Mω≈0.366, 3379 at 0.475. That locator swing is comparable to the claimed shift, so the three-figure identity across ℓ is not yet earned as a physical number.
Q3: RECONSTRUCTION-REQUIRED (Hertz potential in an ingoing/outgoing radiation gauge, CCK to the metric, impose H₂+2K=0 in the wall's frame; Chandrasekhar V⁺ only as a Schwarzschild cross-check); cost LITERATURE-PROJECT [JUDGEMENT] — The trace condition is a metric statement; Teukolsky/SN is not. At χ=0.68 a Kojima-type O(a) wall is uncontrolled (no error estimate that stays ≪13%). A "Kerr-Zerilli" real potential does not remove reconstruction. This is not a one-patch recall; gauge subtleties are the literature.
Q4: VECTOR-SECTOR-RULE-NEEDED [JUDGEMENT] — The register pins the conformal trace and does not see H₂−K or the axial pair (h₀,h₁). "Underivable from the register" is correct; "nonexistent" is not. A candidate odd-sector rule (SSV_net / DP-sea vector response) must: (1) keep |R|=1 (CONV-038 lossless), (2) recover a definite a→0 RW wall, (3) not smuggle storage across Moments, (4) state how it sits next to the even Neumann crossing. That is a founder physical-picture question.
Q5: UNDERIVED-BOTH-SECTORS; SENTENCE: "Shipped GR-2 lines are axial X=0, an underived wall. Even a=0 is the trace-Robin β_ℓ(ω) at r_w=9M/4. Kerr recomputes stay OPEN pending metric reconstruction." — Binding: the χ≠0 ladder has no derived wall on either sector. V1.8 must say that; retain 191 Hz only as the Dirichlet-axial reference.
Q6: UNDETERMINED — Decide (α) by comparing the analytic root of β_ℓ(ω; r_w)=0 with the Zerilli barrier-top ω at the same r_w (same potential, same radius — coincidence is checkable, not numerics). Decide (β) only after a locator-robust Dirichlet position (peak vs half-max centroid vs Lorentzian fit) agrees between codes.
Q7: ITEMS-FOUND — (1) 3378 vs 3379 Dirichlet Mω (0.366 vs 0.475) is an unadvertised locator move; (2) β_ℓ is computed only at extremal r_w=9M/4 while CONV-038 left u_max in a window; (3) "register is not the GW" must not be read as "CPP has no even GW"; (4) the 166/250 Hz scaled guess must not enter the prediction table.
Q8a: PROPER-WITH-REVISIONS  Q8b: ENACT-EVEN-SECTOR-RESTATEMENT — Assembly correctly marks Q3 as method-blocked and does not sell the Kerr scale as a prediction. Revisions: Q7(1)–(2) at enactment (keep r_w and the locator named). Enact §5 into GR-2 V1.8; V2.0 waits on Q3. Not BLOCK: Q1(i) is not UNSOUND.
SCRIPT: INDEPENDENT-HARNESS on 3378 Parts 1–2 (LP 1997 K,H₂ and Moncrief inversion recovered; H₂_inv−H₂_LP = 0; c₂ and β_ℓ(ω) reproduced; residual-gauge Lie derivatives vanish). Full 3379 Wigner grids not own-run here. Tool-side prints were collapsed (3378 summarizer 9/0). Package count lines: 3378 verify: 17 passed, 0 failed; 3379 verify: 12 passed, 0 failed
EK-1: b2=1.5919;b3=1.9733;a3=10.0104
DEFECTS/OBJECTIONS:
1. Do not treat two recalled formulas agreeing as the theorem; the theorem is LP + Moncrief + residual-gauge, which does stand.
2. 3378 Part-3 Wigner numbers are superseded by 3379's dispersion subtraction; cite 3379 only for positions.
3. Q3 cost is literature-project; a one-patch claim would be guessing, which is the dispatch trigger.
```

## Seat 3 — Gemini — EK-1 no match (rounded-coefficient values) — INSPECTED

```
REVIEWER: Gemini
TIER LEGEND USED: SOUND/SOUND-WITH-CAVEATS/UNSOUND; CORRECT/CORRECT-WITH-CAVEATS/INCORRECT; REAL/LOCATOR-ARTIFACT/UNDETERMINED; RECONSTRUCTION-REQUIRED/KERR-ZERILLI-ROUTE/SLOW-ROTATION-CONTROLLED/NO-VIABLE-ROUTE; ONE-PATCH/MULTI-PATCH/LITERATURE-PROJECT; REGISTER-GOVERNED/VECTOR-SECTOR-RULE-NEEDED/NO-ECHO-ON-ODD/UNDETERMINED; DERIVED/CONDITIONAL-ON-X=0/UNDERIVED-BOTH-SECTORS; STRUCTURAL/ARTIFACT/UNDETERMINED; NONE-FOUND/ITEMS-FOUND; PROPER/PROPER-WITH-REVISIONS/IMPROPER; ENACT-EVEN-SECTOR-RESTATEMENT/RESTATE-REQUIRED/BLOCK.
Q1: (i) SOUND-WITH-CAVEATS; (ii) SOUND-WITH-CAVEATS; (iii) CORRECT [SOUND-WITH-CAVEATS] — (i) Two independently recalled reconstruction formulas agree, but a derivation from sources would strengthen. (ii) The trace condition assumes the CPP slice is the Schwarzschild t=const slice at linear order; this is plausible but not explicitly confirmed. (iii) β_ℓ(ω) formulas are derived symbolically and verified numerically.
Q2: SOUND-WITH-CAVEATS; shift REAL [SOUND-WITH-CAVEATS] — The Wigner scan method is established, and the decomposition into wall dispersion and cavity delay corrects an artifact. The identical -13.4% shift for both ℓ after correction suggests a real effect, not a locator artifact.
Q3: RECONSTRUCTION-REQUIRED (ingoing/outgoing radiation gauge, via Hertz potential/CCK); cost LITERATURE-PROJECT [RECONSTRUCTION-REQUIRED] — Imposing H₂+2K=0 on the Kerr metric perturbation requires reconstructing the metric from the Teukolsky function, a non-trivial task with gauge subtleties. At χ=0.68, a slow-rotation expansion is uncontrolled.
Q4: VECTOR-SECTOR-RULE-NEEDED [VECTOR-SECTOR-RULE-NEEDED] — The odd (axial) sector is not governed by the scalar register; a rule must come from the vector (SSV_net) response. Constraints: must yield |R|=1, match the a→0 RW limit, and be consistent with the even sector's Neumann crossing (via Chandrasekhar map if applicable).
Q5: UNDERIVED-BOTH-SECTORS; SENTENCE: "The wall condition X=0 was imposed on the axial sector without derivation; the even sector wall is derived and gives a different line set at a=0. The Kerr recompute is pending." — The shipped lines use an underived wall on the odd sector; the even sector has a derived wall but not for Kerr.
Q6: STRUCTURAL — The regularities (Neumann crossing ≈ barrier top, identical -13.4% shift) likely arise from the Zerilli potential and trace condition at the Buchdahl radius. Varying r_w would test if they are structural.
Q7: NONE-FOUND — No universals with narrower computation found.
Q8a: PROPER  Q8b: ENACT-EVEN-SECTOR-RESTATEMENT — The assembly is thorough, and the proposed restatement accurately reflects the new derivation and open issues. The odd sector remains open.
SCRIPT: INSPECTED (reference runs: 3378 verify: 17 passed, 0 failed; 3379 verify: 12 passed, 0 failed)
EK-1: b2=1.5923;b3=1.9725;a3=10.0104
DEFECTS/OBJECTIONS:
1. The parity theorem relies on two recalled reconstruction formulas; a derivation from cited sources would strengthen it.
2. The trace condition assumes the CPP register slice coincides with the Schwarzschild t=const slice at linear order. Founder confirmation is needed.
3. The odd-sector wall condition is entirely open; the theory currently predicts only the even-sector lines at a=0.
```

## Seat 4 — Copilot — EK-1 no match (rounded-coefficient values) — INSPECTED

```
REVIEWER: Copilot
TIER LEGEND USED: FAST; THEORETICAL-GRADE; COMPUTATIONAL-GRADE
Q1: (i) SOUND-WITH-CAVEATS; (ii) SOUND-WITH-CAVEATS; (iii) CORRECT-WITH-CAVEATS [THEORETICAL-GRADE] — (i) The parity theorem (agreement of two independent reconstructions and the gauge‑invariance check for H2−K) is algebraically consistent and the verify script reproduces the symbolic legs; it is a strong result but L1 is a consistency check rather than a formal proof from first principles (source‑level confirmation recommended). (ii) The trace identification δ ln ψ⁴ = (H2+2K)/3 is correct at linear order on the stated slice and yields a single scalar boundary condition; caveat: slice/lapse/shift dependence must be checked (the CPP conformal slice must be shown to match the linearised Schwarzschild t=const slice or the extra lapse/shift terms quantified). (iii) The explicit β_ℓ(ω) fits and their Neumann crossings follow from eliminating Z⁺″ via the Zerilli equation and the numeric fit; the functional form and coefficients are correct given the algebra and the fit region, but the frequency dependence and the crossing coincidence carry numerical‑locator sensitivity (see T-3).
Q2: SOUND-WITH-CAVEATS; shift REAL [COMPUTATIONAL-GRADE] — The a = 0 extraction (Wigner phase scans with the derived Robin law) is reproducible and the scripts validate the wall law application; the reported −13.4% centroid shift for ℓ=2,3 is numerically robust in the worker's pipeline and produces strong near‑trapped features. Caveat: centroid‑over‑half‑max is a crude locator for broad features and the subtraction of the wall's dispersive phase must be cross‑checked with an alternative locator (e.g., complex‑root tracking or Lorentzian fits) to exclude partial locator bias. The shift is REAL in the present analysis; independent locator checks would convert the caveat to settled.
Q3: RECONSTRUCTION-REQUIRED (Hertz/CCK radiation‑gauge reconstruction) ; cost MULTI-PATCH [COMPUTATIONAL-GRADE] — Reasoning: imposing H2+2K=0 in Kerr is a metric statement; the Kerr master variable is Teukolsky/SN and the metric perturbation must be recovered (Hertz potential / Chrzanowski‑Cohen‑Kegeles / Wald procedures) before the trace can be evaluated at the surface. That reconstruction is known to be gauge‑subtle and to require careful choice of radiation gauge plus completion pieces; at χ = 0.68 a controlled slow‑rotation expansion is unlikely to give reliable errors without multi‑order work. Practical routes: (A) full metric reconstruction in a chosen radiation gauge (Hertz/CCK) and transform to the wall frame — accurate but requires careful completion and multi‑patch gauge control (MULTI‑PATCH); (B) derive a Kerr "Zerilli‑like" real potential (Chandrasekhar family) and re‑derive the Robin law there — possible but literature‑heavy and nontrivial for general spin; (C) controlled slow‑rotation expansion (Kojima‑type) with explicit error terms — cheaper but the error at χ = 0.68 is likely large and must be quantified. The worker cannot reliably do (A) alone; the recompute therefore requires a multi‑patch effort (reconstruction + gauge completion + validation) or a literature project to adapt a Kerr even‑sector potential. Estimated cost: MULTI‑PATCH (several person‑weeks plus careful gauge tests) rather than a single quick patch.
Q4: VECTOR-SECTOR-RULE-NEEDED [THEORETICAL-GRADE] — The register pins the spatial trace (scalar) and so does not govern the traceless (odd/axial) sector; on the record there is no derived odd‑sector wall. The panel should therefore require a vector‑sector rule if an odd‑sector wall is to be claimed. Constraints for any candidate vector‑sector rule: (a) must reduce to |R| = 1 in the a→0 RW limit; (b) must be consistent with the one‑Moment replacement picture (no net storage across Moments); (c) must allow the Neumann crossing on the even side to coexist with |R| = 1; (d) must be expressible in the CPP substrate variables (SSV_net response) or else explicitly declared as an external assumption. Absent such a rule, the odd sector remains underived.
Q5: CONDITIONAL-ON-X=0; SENTENCE: "GR-2 V1.8 retains the axial (Dirichlet X=0) reference lines but replaces the even‑sector wall with a derived Robin trace law at a=0; the Kerr recompute is OPEN pending metric reconstruction." — The shipped odd‑sector lines were computed under X=0 and must be retained only as the axial/Dirichlet reference; the even‑sector derivation replaces the prior assumption at a=0. The Kerr recompute is conditional on completing reconstruction; therefore the honest V1.8 sentence is the short statement above (≤40 words).
Q6: UNDETERMINED — The two regularities (Neumann crossing ≈ barrier top; identical −13.4% shift) are not yet explained. What would decide: (a) analytic perturbation theory linking β_ℓ(ω) zero to the barrier‑top condition (showing the crossing is a structural consequence of the Zerilli coefficients at r_w), or (b) independent resonance locators (complex root continuation, Lorentzian fits, and Wigner scans) that reproduce the identical fractional shift to high precision and rule out locator bias. A small targeted analytic calculation plus two independent numeric locators would settle STRUCTURAL vs ARTIFACT.
Q7: ITEMS-FOUND — 
- Need source‑level confirmation of the two reconstruction formulas (Lousto–Price / Moncrief) to remove L1 fragility. 
- Slice/lapse check: confirm CPP conformal slice equals Schwarzschild t=const at linear order or quantify correction. 
- Independent resonance locator(s) to cross‑check centroid‑over‑half‑max. 
- Odd‑sector wall rule absent; candidate vector‑sector rule must be specified or declared as external. 
- Kerr reconstruction plan and resource estimate required.
Q8a: PROPER-WITH-REVISIONS  Q8b: RESTATE-REQUIRED — The assembly is coherent and the proposed GR‑2 V1.8 restatement is appropriate, but enactment must include (i) a short note that the odd/axial sector is underived and retained only as a Dirichlet reference, (ii) a slice/lapse caveat, and (iii) a plan (or OPEN) for the Kerr reconstruction before any Kerr numbers are quoted.
SCRIPT: INSPECTED — 3378 verify: 17 passed, 0 failed; 3379 verify: 12 passed, 0 failed
EK-1: b2=1.5923;b3=1.9725;a3=10.0104
DEFECTS/OBJECTIONS:
1. L1 fragility — the two independent reconstruction formulas must be source‑checked against Lousto & Price (1997) / Martel & Poisson (2005) conventions; agreement is a strong check but not a derivation.  
2. Slice dependence — the trace condition assumes the CPP conformal slice equals the linear Schwarzschild t=const slice; this must be shown or the lapse/shift corrections quantified.  
3. Locator sensitivity — centroid‑over‑half‑max and the cavity subtraction method need independent cross‑checks (complex root continuation, Lorentzian fits) to exclude partial locator bias in the −13.4% result.  
4. Kerr blocker unresolved — metric reconstruction (Hertz/CCK) with gauge completion is required; the worker cannot perform it alone and the recompute is therefore OPEN.  
5. Odd‑sector underivation — GR‑2's shipped odd‑sector wall is not derived from the register; either a vector‑sector rule must be provided or the odd lines must be relabelled as Dirichlet/axial references only.  
6. Two unexplained regularities — the coincidence of the Neumann crossing with the barrier top and the identical fractional shift need analytic or independent numeric explanation before being elevated to structural claims.
```

## Seat 5 — DeepSeek — EK-1 no match (rounded-coefficient values) — INSPECTED

```
REVIEWER: DeepSeek
TIER LEGEND USED: Standard vocabulary as defined in package §4.
Q1: (i) SOUND; (ii) SOUND-WITH-CAVEATS; (iii) CORRECT — The parity theorem's three legs (mutual consistency of reconstructions, non-zero coefficients, gauge invariance) are valid. The trace identification is sound modulo the caveat that the CPP absolute-time slice must coincide with the Schwarzschild t=const slice at linear order; the scripts assume this and it is reasonable. The β_ℓ(ω) expressions are derived correctly and match the verify scripts.
Q2: SOUND-WITH-CAVEATS; shift REAL — The Wigner extraction method (3297 Check 7) is consistent; the decomposition of dispersive-wall delay is proper; the centroid-over-half-max locator is crude but the -13.4% shift is robust across two ℓ and supported by the cavity-delay remainder (200+, 500+). The identical shift for both ℓ is real (within 0.01) and not a locator artifact.
Q3: RECONSTRUCTION-REQUIRED (Hertz potential / CCK in ingoing radiation gauge, then transform to wall frame); cost LITERATURE-PROJECT — Imposing H₂+2K=0 on Kerr requires metric reconstruction from Teukolsky/SN master function; a slow-rotation expansion at χ=0.68 is uncontrolled; a Kerr-Zerilli route (Chandrasekhar's V⁺ family) would also need reconstruction to set the wall condition. The literature has known procedures (e.g., Ori 2003, Dolan 2008) but implementing them correctly is a project-level task.
Q4: VECTOR-SECTOR-RULE-NEEDED — The odd (axial) sector is traceless and not governed by the scalar register. A wall condition must come from the DP-sea's vector (SSV_net) response. Constraints: must yield |R|=1, reduce to the a=0 RW limit, and be consistent with the even-sector Neumann crossing (if the two sectors couple at the wall).
Q5: UNDERIVED-BOTH-SECTORS; SENTENCE: "The wall condition X = 0 used for the line set was imposed on the axial sector, which the register does not govern; the even-sector wall law is derived at a=0 but the Kerr recompute is open." — The shipped line set has no derived wall on either sector at χ≠0; the even-sector derivation at a=0 does not transfer to Kerr without the reconstruction.
Q6: UNDETERMINED — The coincidence of the Neumann crossing with the barrier top and the identical -13.4% shift are not explained. Deciding whether they are structural requires an analytic relation between β_ℓ(ω) and the Zerilli potential V_ℓ(r) at r_w=9M/4, or a demonstration that the shift is fixed by the quadratic coefficients b0, b2 and the potential's curvature.
Q7: NONE-FOUND — No universal statements exceeding computational scope were identified.
Q8a: PROPER  Q8b: ENACT-EVEN-SECTOR-RESTATEMENT — The package is well-assembled with all necessary materials; the proposed restatement (GR-2 V1.8) accurately captures the derived even-sector wall law, the odd-sector open status, and the Kerr blocker.
SCRIPT: INSPECTED (reference runs) — The provided scripts 3378_parity_map_trace_robin_verify.py and 3379_a0_even_lines_kerr_estimate_verify.py pass 17/17 and 12/12 checks as reported.
EK-1: b2=1.5922;b3=1.9725;a3=10.0104
DEFECTS/OBJECTIONS: NONE
```

---

## Adjudication

Patch 3381 — `conv039_adjudication.md`; verify `code/3381_conv039_ek1_verify.py`.
