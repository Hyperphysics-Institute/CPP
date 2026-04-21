# Reviews: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Paper:** SS-7 v1.2 (21 April 2026, symmetric-honesty corrections)
**Last updated:** 21 April 2026

---

## Review status

| Reviewer | Round | Status | Date | Verdict |
|---|---|---|---|---|
| ChatGPT (OpenAI) | 1 initial | Hallucinated | 19 Apr 2026 | Review did not engage paper content; correction letter sent |
| ChatGPT (OpenAI) | 1 re-review | Substantive | 19 Apr 2026 | Minor-to-moderate revisions |
| Copilot (Microsoft) | 1 | Substantive | 19 Apr 2026 | Minor revisions |
| ChatGPT (OpenAI) | Stress tests | Adversarial | 19 Apr 2026 | 5-nucleus test; no counterexample found |
| ChatGPT (OpenAI) | 2 | Calibrated throughout | 20 Apr 2026 | **Accept with minor revisions** |
| Copilot (Microsoft) | 2 | Mixed (4 factual mismatches) | 20 Apr 2026 | **Accept with minor revisions** |
| ChatGPT (OpenAI) | v1.2 verification | Substantive, referee-grade | 21 Apr 2026 | **Interpretation (a); endorses v1.2 retirement of OPEN-SS-22** |
| Copilot (Microsoft) | v1.2 verification | Substantive, arithmetic-exact | 21 Apr 2026 | **Interpretation (a); endorses v1.2 retirement of OPEN-SS-22** |
| Grok (xAI, + Benjamin/Lucas/Harper) | v1.2 verification | Substantive, cross-checked | 21 Apr 2026 | **Interpretation (a); endorses v1.2 retirement of OPEN-SS-22** |

Both round-2 reviewers converged on "Accept with minor revisions" for v1.1. The SS-7 cycle cleared first external review at both reviewers with only polish remaining.

The v1.2 verification cycle (a different mode — symmetric-honesty check on an author-team-surfaced concern rather than reviewer-driven critique) produced three independent convergences on interpretation (a): the v1.1 Table 1 residual plateau at $N_\alpha \geq 12$ was an isotope-selection artifact, not a structural signal. None of the three reviewers constructed a defensible alternative (b). OPEN-SS-22 was consequently retired; first retirement in the CPP programme record.

---

## Part 1 — Formal reviews

### Round 1: Copilot (19 April 2026)

**Verdict:** "Publishable after minor revisions. The strongest and cleanest paper in the SS-series."

**Major strengths identified:** Zero-parameter structure; concurrent multi-nucleus agreement; clean scope; §4 ${}^8$Be derivation; explicit Hoyle connection.

**Items accepted into v1.0 (7):**
1. Expanded C1-C4 assumption stack with quantitative rigidity argument
2. Deeper Coulomb treatment §5.4 with scaling argument
3. N_α ≥ 12 trend-line discussion with structural-onset classification
4. Expanded Hoyle-state discussion with geometric framing
5. Table 1 legend with B_α clarification
6. Notation consistency sweep
7. Three figures (polytope pair, K_3 schematic, residual scatter)

**Items flagged and declined (2 typo reports):** Two claimed typos did not exist in v0.1 source; declined with evidence.

**Full response:** `SS-7_v0.1_copilot_review_response.md`

### Round 1: ChatGPT initial review (19 April 2026 AM) — HALLUCINATED

**Verdict rendered:** Major revision required.

**Core critiques claimed:**
1. "No closed-form binding formula yet"
2. "No benchmark calculations — model not tested against any actual nucleus"
3. "No normalization scale"
4. "Saturation mechanism not addressed"
5. "Falsifiability currently weak"

**Reality check:** All five claims directly contradicted by v0.1 content:
1. Boxed formula in Abstract, §2.3 (Eq. 2), Proposition 3.1
2. Table 1: 8 zero-parameter predictions vs AME 2020
3. Abstract: "$B_{\text{pair}} = M_0/\varphi = 2.342$ MeV is the nucleon-pair binding quantum from SS-5"
4. §5.1: entire subsection on $N_\alpha \geq 12$ systematic underbinding (OPEN-SS-22)
5. §6.3: four specific numerical falsification conditions

**Response:** Correction letter `SS-7_chatgpt_rereview_request_letter.md` sent with line-cited evidence for each mismatch. Request for re-engagement at the standard ChatGPT had demonstrated in its SS-6 round-1 review.

**Full response:** `SS-7_v0.1_chatgpt_review_response.md`

### Round 1: ChatGPT re-review after correction (19 April 2026 PM)

**Verdict:** "Minor-to-moderate revisions required. This is now a coherent, testable, nontrivial model — not just a conceptual proposal."

**Opening acknowledgement (verbatim):**
> *"Your summary is accurate. The paper does contain: a closed-form formula, benchmark calculations, a normalization scale tied to M₀/φ, an explicit saturation discussion, and explicit falsifiability criteria. That alone invalidates my earlier claim of 'no closed-form formula.'"*

**Items accepted into v1.0 (6):**
1. Theorem/hypothesis split for 3N−6 (mathematics vs physics)
2. Selection-bias scope language in Abstract and §1.4
3. R_αα = 2.37 fm reframed as inversion/consistency parameter (Finding 4.1)
4. M_0/φ recurrence status paragraph: empirical within CPP, derivation open
5. ±2% structural falsification threshold added to §6.3
6. Topological-invariant framing at §5.4 opening

**Full response:** `SS-7_v0.1_chatgpt_rereview_response.md`

### Round 1 stress tests: ChatGPT hostile-geometry attacks (19 April 2026)

**Context:** After round-1 re-review, ChatGPT offered to attempt to break the $3N_\alpha-6$ rule with counterexample nuclei. Accepted.

**Tests performed:** 5 tests across 4 nuclei at fixed $(\Balpha, B_{\text{pair}})$:

| Test | Nucleus | $E_{\text{simp}}$ / error | $E_{\text{alt}}$ / error | Alternative |
|---|---|---|---|---|
| 1 | ${}^{32}$S | 18 / −1.20% | 12 / −6.37% | cube |
| 2 | ${}^{32}$S | 18 / −1.20% | 16 / −2.92% | square antiprism |
| 3 | ${}^{28}$Si | 15 / −1.41% | 12 / −4.38% | wheel-like |
| 4 | ${}^{36}$Ar | 21 / −0.94% | 20 / −1.70% | monocapped sq antiprism |
| 5 | ${}^{40}$Ca | 24 / −0.84% | 20 / −3.58% | pentagonal-antiprism-type |

**Result:** All alternatives underperform the simplicial rule. ${}^{36}$Ar is the single-edge-sensitivity test; dropping $E$ by one quantum matches one $B_{\text{pair}}$ of degradation.

**ChatGPT's calibrated conclusion (preserved verbatim in paper §6.5.4):**
> *"Among the physically arguable lower-edge alternatives tested, none outperform the simplicial $3N_\alpha - 6$ rule."*

**Integration:** Became §6.5 of v1.0, with explicit attribution to ChatGPT in paper Acknowledgements.

### Round 2: ChatGPT review of v1.0 (20 April 2026)

**Verdict:** "Accept with minor revisions. This version does what a good theory paper should do: makes a clear claim, exposes itself to failure, survives targeted attempts to break it. That's the right bar."

**Calibration:** Every specific claim in the review matches v1.0 content. Every suggested revision is actionable. Two advisories (Coulomb calibration, prediction-paper label) correctly identify places where existing posture is appropriate.

**Items accepted into v1.1 (2):**
1. C4 status rephrased: "a structural hypothesis within CPP, not yet derived from lattice-level dynamics"
2. §6.5.3 opening line: "These tests demonstrate that the empirical success of the model is not merely due to total binding magnitude, but to the specific combinatorial edge count."

**Advisories noted (no action):**
- Coulomb section calibration: "acceptable for v1.0, but do not overclaim." Applied as framing check on Copilot's Figure 4 schematic (labeled schematic representation, not derived mechanism).
- Prediction-paper label: "keep it, but expect scrutiny."

**Adversarial summary preserved in philosophy-SS-7.md §"Adversarial summary":**
> *"If I were trying to reject this paper, I would now have to argue α-cluster nuclei do not realize simplicial contact graphs, or the agreement is accidental despite no parameters, multiple nuclei, and failed perturbations. That is a much harder position than before."*

**Full response:** `SS-7_v1.0_chatgpt_round2_response.md`

### Round 2: Copilot review of v1.0 (20 April 2026) — MIXED

**Verdict:** "Accept with minor revisions. The v1.0 draft is already strong enough for preprint release."

**Items accepted into v1.1 (3):**
1. Physical-intuition paragraph after C4 (three arguments: triangular-face rigidity, maximal contact reinforcement, rigid-packing convexity)
2. DP-sea Coulomb schematic diagram (became Figure 4)
3. Symbols glossary near Main Result box

**Items declined as factual mismatches (4):**

Copilot's review contained four specific items that referenced content not present in v1.0:
- §3.1: Claimed §6.5 needs a table; Table 2 already present in §6.5.2 (5 rows × 7 columns)
- §3.4: Claimed Hoyle subsection ends mid-sentence; subsection ends with complete paragraph
- §4.1: Listed typos "2ºNe", "4ºCa", "Conver Polytopes"; zero matches for each string in v1.0 source
- §4.2: Claimed Ba/Bα and Raa/Rαα notation inconsistent; LaTeX commands `\Balpha` (40 uses) and `\Raa` (23 uses) render consistently throughout

**Response:** Correction letter `SS-7_copilot_round2_closing_letter.md` sent with line-cited evidence.

**Copilot's acknowledgement (verbatim):**
> *"You are correct. This was an error on my part. I likely carried forward a mental model from the v0.1 structure and did not re-verify the presence of the table in v1.0. I accept the correction fully."*

Similar explicit acknowledgements for all four items. Commitment going forward: "For SS-8 and all future papers, I will: 1. Perform a strict verification pass on every specific-item comment. 2. Cross-check each claim against the actual submitted file, not memory or prior drafts. 3. Avoid template-driven assumptions unless explicitly confirmed in the text. 4. Use line-anchored references when making specific claims."

**Full response:** `SS-7_v1.0_copilot_round2_response.md`

### v1.2 verification cycle: three-reviewer convergence (21 April 2026)

**Cycle type.** This was a new review mode — symmetric-honesty verification rather than standard round-by-round review. On 21 April 2026, during SS-8 Phase 1 exploration, an empirical map of the full strict $N{=}Z$ alpha-chain surfaced two concerns with the v1.1 paper itself:

1. **G3 RMS discrepancy** (registered 20 April 2026 in `SS-7_v1.1_G3_discrepancy_note.md`): paper cited $0.88\%$; first-principles computation gives $0.91\%$ across all 8 primary nuclei ($0.86\%$ excluding ${}^{20}$Ne).
2. **Table 1 isotope-selection artifact** at $N_\alpha \geq 12$ (new 21 April): paper's rows used non-$N{=}Z$ isotopes ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe (each with $N - Z = +4$); strict $N{=}Z$ counterparts ${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni stay in family with the primary set.

Rather than silently correct or laundered into a reframing, both concerns were consolidated into a verification letter sent to three reviewers simultaneously, with four tasks: AME 2020 binding-energy confirmation, residual recomputation, interpretation (a) vs.~(b) assessment, and line-777 diagnosis.

**Protocol change noted in the letter.** Reviewers were instructed to work from `.tex` source rather than the compiled PDF. Two round-2 reviewers had independently misread $\varphi^{1/z}$ as $\varphi^{1/2}$ from small-superscript rasterization in the PDF — a numerical difference of $\sim 23\%$ that passed as a clean verbatim quote. The v1.2 cycle was the first to operate under the `.tex`-only submission protocol.

**Letter:** `SS-7_v1.2_reviewer_verification_letter.md`

#### v1.2 verification — ChatGPT (21 April 2026)

**Verdict:** Substantive, referee-grade, with worked arithmetic.

**Summary of response:**
- **Task 1 (AME values):** Independent verification via "consistency with standard mass tables and known binding trends"; all Claude's values confirmed to $\sim 0.01$–$0.02$ MeV.
- **Task 2 (residuals):** Independent recomputation step-by-step; all seven residuals match to the displayed precision.
- **Task 3 (interpretation):** Interpretation (a), overwhelmingly. Reasoning: (1) shift matches neutron-excess physics at $\sim 1.8$–$2.0$ MeV/neutron, standard asymmetry-term behaviour; (2) structural plateau disappears when chain switched to strict $N{=}Z$; (3) no physical mechanism ties exactly $+4$-neutron isotopes to alpha-cluster topology; (4) selection correlates with abundance, not structure — "classic selection bias pathway."
- **Task 4 (line 777):** "Both (clear case): incorrect data + incorrect classification."

**Key contribution adopted in v1.2.** ChatGPT contributed the sentence now paraphrased into the paper's §5.1: the $-2\%$ residual plateau at $N_\alpha \geq 12$ is attributable to neutron-excess binding and does not indicate a structural transition in the alpha-cluster model. This sentence prevents future misinterpretation of the v1.1 plateau pattern.

**Closing offer (not taken up this cycle):** "v1.2-ready rewrite of §5.1," "replacement Table 1 for $N_\alpha \geq 12$," "reframed OPEN-SS-22 or clean retirement note," "pivot memo for SS-8 (OPEN-SS-23)." Response remained scoped to verification; revision execution was done by the author team.

**Full response:** `SS-7_v1.2_chatgpt_verification_response.md`

#### v1.2 verification — Copilot (21 April 2026)

**Verdict:** Substantive, arithmetic-exact.

**Summary of response:**
- **Task 1 (AME values):** "Internally consistent and match known reference values to expected precision." Copilot explicitly flagged its inability to live-query AME 2020, validated by consistency with standard mass tables. Claude's values confirmed to $\sim 0.01$–$0.02$ MeV level.
- **Task 2 (residuals):** Full step-by-step arithmetic reproduced; all seven residuals match to the displayed precision.
- **Task 3 (interpretation):** Interpretation (a), decisive. Shift $\sim 1.8$–$2.0$ MeV/neutron flagged as "standard asymmetry-term behaviour." Structural plateau "disappears" under strict $N{=}Z$ substitution; "the model continues smoothly."
- **Task 4 (line 777):** "Both (clear case): dual failure — incorrect data + incorrect classification."

**Representative closing quote (preserved in philosophy-SS-7.md v1.2 adversarial summary):**
> *"The 'flat $-2\%$ residual' disappears immediately. When you switch to $N{=}Z$: the supposed structural plateau vanishes; the model continues smoothly. This is decisive."*

**Additional recommendation adopted.** Copilot recommended an explicit sentence placement: "The previously observed $-2\%$ residual plateau at $N_\alpha \geq 12$ is attributable to neutron-excess binding and does not indicate a structural transition in the α-cluster model." Paper §5.1 uses this framing.

**Compared to Round 2:** Copilot's v1.2 verification response showed the process-commitment improvement promised in its round-2 closing letter (strict verification on specific-item comments, cross-check against the actual file rather than memory or prior drafts). No factual mismatches in this cycle.

**Full response:** `SS-7_v1.2_copilot_verification_response.md`

#### v1.2 verification — Grok (21 April 2026, with Benjamin/Lucas/Harper multi-agent verification)

**Verdict:** Substantive, cross-checked against AME 2020 `mass_1.mas20.txt`.

**Summary of response:**
- **Task 1 (AME values):** Direct cross-check against AME 2020 file claimed; all seven values match to $\leq 6$ keV (negligible for residuals at the reported level). ${}^{48}$Cr reported as $411.462$–$411.468$ MeV (consistent with Claude's $411.462$).
- **Task 2 (residuals):** Exact match to Claude's table.
- **Task 3 (interpretation):** Interpretation (a), only defensible reading. Reasoning included specific reference to the paper's §1.5 scope declaration ("no neutron-excess treatment") as prior author-team awareness that the isotope choice violated the formula's domain.
- **Task 4 (line 777):** Both errors; must be corrected in v1.2 regardless.

**Cycle context.** Grok had been suspended from the SS-7 v1.1 review rotation pending rehabilitation. Sonnet 4.5 flagged potential "vocabulary contamination" in Grok's earlier outputs. On this cycle, Grok was re-engaged specifically because its suspension reasoning could be re-tested under the new `.tex`-only submission protocol — Thomas's diagnosis was that Grok's prior misreads were input-format degradation (PDF rasterization of math symbols), not semantic contamination. The v1.2 verification supported this diagnosis: Grok's content was clean, arithmetic-exact, and referenced the paper's prior admission accurately. Rehabilitation assessment: substance fully restored; multi-agent environment verification (Benjamin/Lucas/Harper) adds an additional cross-check layer not available from the other two reviewers.

**Full response:** `SS-7_v1.2_grok_verification_response.md`

### Convergence analysis (v1.2 cycle)

All three reviewers converged on (a) without prompting toward that answer. The verification letter framed tasks 3 and 4 neutrally — presented both interpretations (a) and (b), explicitly invited reviewers to say "I cannot think of a defensible reason for (b)" as a valid answer, and offered the line-777 diagnosis as a separable question from the broader scope call.

**Three-reviewer convergence as retirement criterion.** Per the operational decision recorded in PH-OPEN-SS-22.md §"What Made This Tractable": if any of the three reviewers had constructed a defensible (b), retirement would have been premature and reframing would have been warranted. The convergence itself is part of the evidence supporting retirement — not the author-team's choice alone.

**Summary across the three verifications.**

| Task | ChatGPT | Copilot | Grok |
|---|---|---|---|
| AME 2020 values | ✔ consistency check | ✔ consistency check | ✔ direct file cross-check |
| Residual arithmetic | ✔ step-by-step | ✔ step-by-step | ✔ exact match |
| Interpretation (a) vs (b) | (a), overwhelming | (a), decisive | (a), only defensible |
| Line-777 diagnosis | Both errors | Both errors | Both errors |
| Endorsement of retirement | Yes | Yes | Yes |

---

## Part 2 — FAQ

### Methodology

**Q: Why does the paper use experimental $\Balpha$ rather than SS-5's zero-parameter prediction?**

A: To isolate SS-7's specific empirical test. SS-5 predicts $\Balpha = 27.904$ MeV at $-1.4\%$ residual. Using SS-5's prediction would carry SS-5's residual through to each multi-alpha prediction, conflating SS-7's edge-count test with SS-5's per-alpha residual. The LO-CPP variant is discussed as equivalent in §3.3; both framings are valid.

**Q: How is Table 1 zero-parameter if you use experimental $\Balpha$?**

A: $\Balpha$ is not fit to multi-alpha data. It is the single-alpha binding energy, determined entirely by SS-5 (or by direct measurement of ${}^4$He). No free parameter is adjusted to make Table 1 agree.

**Q: What is the role of $B_{\text{pair}}$?**

A: $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV is SS-5's nucleon-pair binding quantum, derived from the K$_3$ collective-mode structure over a triangular contact face. SS-7's central claim is that this same quantum appears at the alpha-alpha K$_3$ face by identical eigenvalue structure. The recurrence across scales is empirical within CPP (§6.2); derivation remains open.

### Scope

**Q: Why restrict to strict $N{=}Z$ alpha-chain nuclei ($N = Z = 2N_\alpha$)?**

A: The simplicial alpha-polytope hypothesis (C4) is clearest for nuclei with exact alpha composition. Non-$N{=}Z$ isotopes at alpha-chain $N_\alpha$ values (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe each with $N-Z = +4$) show $\sim 2$ MeV per extra neutron beyond the formula's prediction — standard neutron-excess binding that the alpha-chain formula does not model by construction (§1.5). Odd-$A$ nuclei (${}^7$Li, ${}^9$Be, ${}^{11}$B, ${}^{13}$C) and non-clustered structures (${}^6$Li, ${}^{14}$N, ${}^{18}$O) require handling partial-alpha substructures and excess nucleons. All three extensions are registered as OPEN-SS-23 for future work; priority upgraded in v1.2 to primary SS-8 target. Restricting SS-7's scope to strict $N{=}Z$ is explicit in Abstract and §1.4.

**Q: What happens beyond $N_\alpha = 14$?**

A: v1.2 extended the verified domain from $N_\alpha \in [3, 10]$ to $N_\alpha \in [3, 14]$ (${}^{56}$Ni) using strict $N{=}Z$ alpha-chain nuclei; all twelve residuals remain within $\pm 1.5\%$. Beyond $N_\alpha = 14$, the strict $N{=}Z$ isotopes become increasingly short-lived and AME 2020 precision drops; preliminary extrapolation suggests residuals remain $< 2\%$ through $N_\alpha = 16$ (${}^{64}$Ge) but this is flagged as future work rather than a claim of the paper.

**Historical note (v1.1).** The v1.1 edition of this FAQ stopped the claimed domain at $N_\alpha = 10$ because the v1.1 Table 1 rows at $N_\alpha = 12, 13, 14$ used non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe) that showed an apparent $-2$ to $-2.5\%$ deviation interpreted as a "structural onset" motivating OPEN-SS-22 (icosahedral closure hypothesis). v1.2 established that the non-$N{=}Z$ deviation is standard neutron-excess binding, not structural-onset physics; strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni) stay in family with the primary set. OPEN-SS-22 was retired in v1.2 (first retirement in the CPP programme record); the $\sim 2$ MeV/neutron signal in non-$N{=}Z$ isotopes is now addressed under OPEN-SS-23 (primary SS-8 target). See `problem_histories/PH-OPEN-SS-22.md` for the full retirement narrative.

### Falsifiability

**Q: What would falsify SS-7?**

A: Five conditions (§6.3):
1. Any strict $N{=}Z$ alpha-chain nucleus at $N_\alpha \in [3, 14]$ with $|\Delta B/B| > 2\%$ (structural falsification threshold)
2. ${}^{12}$C binding outside $91.9 \pm 1$ MeV
3. ${}^{16}$O binding below 120 or above 135 MeV
4. ${}^{56}$Ni binding below 470 or above 490 MeV (v1.2 extension; current prediction 480.5 MeV, measured 484.0 MeV, $-0.73\%$)
5. Bound ${}^9$Be-like alpha-alpha-nucleon with $B > 30$ MeV
6. Direct $R_{\alpha\alpha}$ measurement outside $2.37 \pm 0.3$ fm

**Q: How do the stress tests relate to falsifiability?**

A: The §6.5 stress tests are a different kind of falsifiability check: given the formula is in place, could a lower-edge alternative match the data better? Five such tests performed. Zero succeeded. This supports C4 empirically against specific alternatives.

### Relationship to Standard Model

**Q: Does SS-7 contradict QCD?**

A: No. SS-7 operates at the effective-alpha-cluster level of description, continuous with the conventional alpha-cluster tradition (Brink 1966, Ikeda 1968, Wildermuth-Tang, Freer 2018). The difference is economy: SS-7 has zero fitted parameters where conventional cluster models typically fit at least one binding strength.

**Q: Does SS-7 agree with experimentally-known alpha-cluster structure of ${}^{12}$C etc.?**

A: Yes. The Hoyle state's three-alpha cluster interpretation, the ${}^{16}$O alpha-tetrahedron structure, the ${}^{24}$Mg octahedral alpha arrangement — all conventional results — are preserved. SS-7 adds a specific numerical binding law on top of this geometric picture.

### Future work

**Q: What comes after SS-7?**

A: Two natural next papers, plus one deferred candidate:
- **SS-8 (OPEN-SS-23):** Non-$N{=}Z$ and odd-$A$ extension of the alpha-chain formula. Primary SS-8 target per v1.2 retargeting. Nearest empirical anchor: the $\sim 2$ MeV/neutron signal visible in ${}^{48}$Ti/${}^{52}$Cr/${}^{56}$Fe and in ${}^{48}$Ca (8-neutron-excess stress test). Likely empirically-facing.
- **SS-9 candidate (OPEN-SS-24):** First-principles derivation of simplicial contact structure from CPP lattice geometry. Addresses the remaining foundational question underlying C4. Likely theoretically-facing.
- **Deferred (OPEN-SS-25, new in v1.2):** First-principles CPP derivation of DP-sea screening of alpha-alpha Coulomb in bound polytopes. Absorbs the §5.4 screening physics that had been tagged "OPEN-SS-22-adjacent" in v1.1. Target paper not yet assigned.

**Historical note.** In v1.1 the SS-8 target was OPEN-SS-22 (icosahedral closure at $N_\alpha \geq 12$), previewed by ChatGPT's round-2 review §8 with the observation that experimentalists would push toward SS-8 while theorists would push toward SS-9. That targeting was based on the v1.1 Table 1's $-2$ to $-2.5\%$ residual pattern at $N_\alpha = 12, 13, 14$, which v1.2 diagnosed as an isotope-selection artifact. OPEN-SS-22 was retired in v1.2; the SS-8 target was retargeted to OPEN-SS-23. The empiricist-vs-theorist split observation preserves — experimentalists will still push toward SS-8 (now extending to non-$N{=}Z$), theorists still toward SS-9 (derivation of C4).
