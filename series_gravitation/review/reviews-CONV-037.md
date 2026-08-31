# CONV-037 — Returns receiver: the Teukolsky ladder (3353–3359) and the flagship frequency move to 191 Hz

**Dispatched:** Patch 3360, 30 Aug 2026 (Session 157, on Fable).
**Package:** `conv037_teukolsky_ladder_review_package_v1.0.md` (CONV-001
single block; six records + the load-bearing 3359 script inlined; the
3356/3358/3359 `.py` files ship separately).

**ID note:** CONV-036 was skipped. Two DE-lane documents dated 26 Aug
reference "CONV-036"; whether earmark or typo could not be verified
from the GR lane, and after this week's ID collision the rule is: gaps
are cheap, collisions are not. If the DE lane did not intend a round,
036 is void.

**What this round gates:** a flagship frequency. PRED-O-39's
retrograde-keyed (2,−2) line would move from the orientation-scale
211 Hz (and the scalar-exact 251 Hz) to **191 Hz at gravitational
grade, Q ≈ 2.1**, with (3,−3) at 288 Hz, Q ≈ 4.2. Also under review:
the seven-rung validation ladder; the Sasaki–Nakamura recall and the
X = 0 boundary-condition choice; three self-corrections and the
withdrawal of 3358's (2,+1); the method limit (Q ≲ 1.5 unreachable)
and the consequent downgrade of the ordering test.

**Binding rules:** majority per question; majority OVERCLAIMS on Q6
blocks predictions.md regardless of Q8b; majority INVALID on Q2 leaves
the gravitational spectrum unregistered; Q7 items adopted regardless.

**Seat mandates riding:** IDENTITY (per-seat lines), OWN-RUN (3359
~3 min, no FAST), COUNT-LINE verbatim, INDEPENDENT-HARNESS, inline
returns. Steers aimed at T-1/T-2 (GPT), T-4 (Grok), T-3 (Gemini),
T-5 (Copilot), falsifiability (DeepSeek).

**Status (Patch 3361): 5/5 REGISTERED SAME-SESSION — ROUND COMPLETE;
ADJUDICATION in `conv037_adjudication.md`.**

Seat hygiene: GPT own-ran 3359 (9/9 verbatim), genuine CONV-037 return
on the first delivery this time; Grok INDEPENDENT-HARNESS on T1 and the
Hz conversion, honest about not hosting the 3-minute run; Gemini
(paste 3) honest INSPECTED; DeepSeek identity holds, honest INSPECTED.
**IDENTITY ANOMALY, NEW CLASS: the COPILOT slot (founder's paste 4)
self-labels "REVIEWER: Gemini."** The founder's slot label is the
provenance record, so it is registered as Seat 4 with the anomaly
flagged; founder confirmation that it came from the Copilot session is
requested. (Its tier legend — bold FAST / GRAVITATIONAL GRADE tags — is
stylistically unlike the Gemini seat's paste-3 return, which supports
the slot label.)

---

## Seat 1 — ChatGPT (GPT-5.6) — REGISTERED, COUNTED

**Registration note (Patch 3361):** own-ran 3359, 9/9 verbatim. The
round's dissent: Q6 OVERCLAIMS, Q8b BLOCK, Q7 seven items, Q5
UNDER-SCOPED, Q3(iii) NOT-CONFIRMED. Fifth consecutive round in which
this seat's grade objections are substantively right (see adjudication
§2) — including catching that the proposed §5 text assigned a Q to a
mode the record itself marks NOT LOCATED.

### Verbatim paste

REVIEWER: GPT-5.6
TIER LEGEND USED: T1 = own-executed numerical result; T2 = analytic/code-inspection inference; T3 = physical interpretation or substrate-level claim not derived by the computation

Q1: SOUND-WITH-GAPS [T1/T2] — The supplied 3359 script reproduces its 9/9 result, including the Schwarzschild reduction, Schwarzschild wall resonance, and two stable Kerr zeros. L1/L5 provide useful independent benchmarks for the Leaver machinery. The remaining gap is material: no test validates the Sasaki–Nakamura implementation in the Kerr interior. A term proportional to a and localized at finite r would evade T1–T3.

Q2: VALID-WITH-CAVEATS [T2/T3] — The SN instrument is valid as a conditional numerical construction, but not yet fully validated for Kerr. A Kerr QNM reproduction using this SN direct integrator, with the standard horizon condition and a tabulated frequency, is owed. Separately, X = 0 is well posed and recovers the adopted Schwarzschild node, but it is ASSUMED rather than derived from the CPP clamped-register condition. Short-range asymptotics do not uniquely make X the physical surface displacement, and SN transformations admit convention/normalization freedom. The spectrum is therefore conditional on the X-Dirichlet wall model.

Q3: (i) CONFIRMED-WITH-CAVEATS; (ii) CONFIRMED-WITH-CAVEATS; (iii) NOT-CONFIRMED [T1/T2/T3] — I reproduce ω22 = 0.36694−0.08782i and ω33 = 0.55333−0.06522i, with the stated Q values and strong local r0/contrast tests. Their physical interpretation inherits the unvalidated Kerr-interior SN terms and assumed X = 0 boundary. One broad ℓ = 2 zero does not establish "no trapped comb": the solver searches locally from one seed and performs no contour count, systematic root census, or exclusion proof for additional ℓ = 2 resonances.

Q4: ADEQUATE [T2] — The three corrections and the 3358 withdrawal are explicit, adverse where appropriate, and anti-erasure is preserved. The live amendment removes the scalar (2,+1) number and exact-grade ordering. Remaining downstream wording defects are listed under Q7 rather than concealed.

Q5: UNDER-SCOPED [T1/T2] — Withdrawing (2,+1) and downgrading the ordering test are correct. But "validated for |Im ω| ≲ 0.12" and a Q ≲ 1.5 boundary are stronger than the evidence. The runs establish successful cases near 0.065–0.117 and failure near 0.25–0.30 for particular modes, leaving an unmeasured grey zone dependent on r0, fitting order, precision, mode, and conditioning. The reported widths lie in the demonstrated-success region but do not define a universal cutoff.

Q6: OVERCLAIMS [T2/T3] — The amendment should say "a located (2,−2) resonance" rather than promote an unconditional exact physical line before a Kerr-specific SN benchmark and boundary derivation. More decisively, "its prograde comparator (2,+1) is too broad (Q ≲ 1.5)" is not a result: the comparator was NOT LOCATED, so its Q is unknown. "No trapped comb" is also not established by the local root searches. "The sharpest line" must be limited to the reported/located modes, and "dominant" must remain conditional on the inherited, non-Teukolsky excitation argument.

Q7: ITEMS-FOUND [T2/T3] —
1. "No trapped comb at ℓ = 2" exceeds a calculation locating one broad root; no global ℓ = 2 root census was performed.
2. "The sharpest line is (3,−3)" exceeds the two validated modes; write "the sharper of the two located retrograde modes."
3. "(2,+1) is too broad (Q ≲ 1.5)" exceeds NOT LOCATED; write that the present instrument cannot determine its frequency or Q.
4. "Retrograde-keyed dominant line" is narrower computationally than the sentence unless explicitly conditioned on the inherited 3349/3350 excitation model; this ladder computes no excitation amplitudes.
5. "OPEN-GR-RCORE-3: all chartered items discharged," including excitation and Zel'dovich bounds, is not supported by the materials presented here and conflicts with the admitted absence of a relative-excitation calculation.
6. K3's script text still says the scalar calculation was a faithful proxy for "ordering," although the scalar comparator and scalar-exact ordering were withdrawn.
7. "Exact Kerr wall resonance" should be scoped as exact numerical solution of the stated SN/X-Dirichlet model, not an exact CPP surface prediction.

Q8a: PROPER-WITH-REVISIONS  Q8b: BLOCK [T2/T3] — The ladder is substantial and the two reported local roots reproduce cleanly, but the proposed flagship amendment contains stronger claims than the computation supports. Under the frozen Q6 rule, predictions.md execution is blocked pending a weaker amendment. Required revisions: state the X = 0 assumption; add a Kerr-specific SN benchmark or label that validation gap; replace the prograde Q claim with NOT LOCATED; limit "sharpest" and "dominant"; and change "no trapped comb" to "the located ℓ = 2 resonance is broad, with no comb demonstrated."

SCRIPT: SCRIPT-EXECUTED (own run)
9/9 PASS
FAST: all checks are FAST; FAST: 9/9 PASS

DEFECTS/OBJECTIONS:
1. No Kerr-interior validation of the SN implementation; the existing tests share a blind spot for finite-r spin-dependent errors.
2. X = 0 is an inherited wall-model assumption, not a derived CPP gravitational boundary condition.
3. Local root-finding cannot prove absence of an ℓ = 2 comb or additional modes.
4. The claimed direct-integration cutoff is inferred from sparse successful and failed examples, not mapped.
5. The amendment assigns Q ≲ 1.5 to an unlocated comparator.
6. "Sharpest," "dominant," and full RCORE-3 discharge require explicit scope restrictions.

---

## Seat 2 — Grok (xAI) — REGISTERED, COUNTED

**Registration note (Patch 3361):** INDEPENDENT-HARNESS on T1 (own
sn_FU vs V_RW) and on the Hz/Q conversions; honest that its sandbox
cannot host the 3-minute DOP853 run. Names the same T-1/T-2 gaps as
GPT and supplies the cheap Kerr-interior check the adjudication then
executed (`3361_conv037_gaps_verify.py` G1). Rules AMENDMENTS-CLEAR
with text revisions.

### Verbatim paste

REVIEWER: Grok
TIER LEGEND USED: exact-grade (validated instrument + reported root assertions); eikonal-WKB (ordering test); assumed-BC (Dirichlet on SN X); one-spin (χ = 0.68 only)
Q1: SOUND-WITH-GAPS [exact-grade on L1/L5/L7-a=0; gap on Kerr-SN] — L1 (Leaver Schwarzschild QNMs to ~7e−6) and L5 (Leaver Kerr (2,2) tables to ≤1.2e−4) are the right kind of known-answer tests for recurrences written from memory. L7 T1 is independently executed here: U_SN + ω² = V_RW to 1.6e−9 and F ≡ 0 on r ∈ [2.3, 30]. T3 (SN a=0 wall reproduces 3356's 0.44859−0.11749i) is the correct cross-code close of the instrument. The gap is T-2: no Kerr QNM has been reproduced by *this* SN + direct-integration stack with a horizon-side condition. A term ~a that vanishes at a=0 and at large r would pass T1–T3. That does not make L1/L5/L7 unsound; it means the Kerr-wall spectrum sits one check short of the same known-answer standard those rungs set for themselves.
Q2: VALID-WITH-CAVEATS [assumed-BC] — X = 0 is the natural Kerr generalisation of Leg A's ψ = 0: SN is built so that X is the short-range RW analogue, T2 shows U → −ω², and T3 shows the a=0 node condition recovers the RW wall root. That is inheritance of a fenced *structure* (clamped register = node in the short-range amplitude), not a substrate derivation of the Kerr wall condition. The corpus has never produced X=0 from the rotating "clamped register." Until that derivation exists, the BC is an unexamined but consistent assumption, not INVALID. The missing Kerr-SN QNM check (T-2) is the operational caveat on the instrument, not a reason to throw out T1–T3.
Q3: (i) CONFIRMED-WITH-CAVEATS; (ii) CONFIRMED-WITH-CAVEATS; (iii) CONFIRMED [exact-grade at one spin; assumed-BC] — Arithmetic is exact: at M = 62 M_⊙, GM = 62 × 4.92549×10⁻⁶ s, f = Re(ω)/(2π GM) gives 191.2 Hz and Q = Re/(2|Im|) = 2.09 for 0.36694−0.08782i, and 288.4 Hz / Q = 4.24 for 0.55333−0.06522i. Reported r₀-spread ~3e−9 and contrast ~6e−9 put both roots inside the instrument's validated |Im ω| ≲ 0.12 window (0.088 and 0.065). Caveats that do not withdraw the numbers: one spin only; r_w(a) feeds the cavity and is not re-varied here; X=0 is assumed; no physical error budget beyond mass scaling. (iii) is clean: Q = 2.09 is a single broad top-of-barrier feature, not a trapped comb.
Q4: ADEQUATE — 3354 reversed 3353's one-sided Φ argument with a computation, not a narrative. 3356 corrected Leg A's Q ≈ 4.9 → 1.91 and said so. 3359 withdrew 3358's (2,+1) in place, with the failure mode named (guess returned, contrast ~1, e^27 growth), and downgraded every claim that leaned on it. Anti-erasure is respected. Downstream of the withdrawal, the exact-grade ordering test is correctly no longer live. Nothing else that still quotes the withdrawn (2,+1) as a root was found in the proposed amendment.
Q5: CORRECTLY-SCOPED — Mandate item T-4. Direct integration is validated for |Im ω| ≲ 0.12 and fails at ~0.3. The reported modes sit at 0.088 and 0.065, with individual sharpness and r₀-independence at 10⁻⁹, which is not the behaviour of a guess. A grey zone between 0.12 and 0.3 is real and unmapped; it does not contaminate these two roots. Downgrading the ordering test because (2,+1) is unlocated, rather than publishing a guess, is the correct scope. Calling the boundary "sharp" would be over-scope; the record does not. It says the instrument cannot see Q ≲ 1.5 and registers a new open item. That is right.
Q6: FAITHFUL-AT-GRADE — The amendment states 191 Hz as an exact s=−2 wall resonance at one spin, Q ≈ 2.1, no comb, (3,−3) as the sharpest *located* line, mass scaling only, spin "not yet a band," 2.624 ms untouched, ordering back at eikonal-WKB, A1–A3 conditionality kept, superseded eikonal tops retained. That is the grade the ladder earned. It does not sell 191 Hz as a spin band or the ordering test as exact. "Sharpest line" is a Q statement, not an excitation claim; a reader can over-read it (T-6), but the text does not convert Q into a detection ranking.
Q7: ITEMS-FOUND — (1) "first exact gravitational Kerr wall resonances" is exact-grade at χ = 0.68 only; spin dependence is not exact-grade. The amendment already fences this; keep the fence in any heading that says "exact." (2) "Dirichlet on X = CPP clamped register in Kerr" is a generalisation, not a derived Kerr wall condition (T-1). (3) "OPEN-GR-RCORE-3: all chartered items discharged" over-reaches if Zel'dovich growth-time bounds were chartered as computed bounds rather than inherited; the 3359 registry line should name the grade of each sub-item. (4) No universal in §5 claims a spin band or an exact-grade ordering test.
Q8a: PROPER-WITH-REVISIONS  Q8b: AMENDMENTS-CLEAR — Revisions owed in text, not a new computation: (i) keep the one-spin / no-band sentence adjacent to every display of "191 Hz"; (ii) say explicitly that X=0 is the RW-analogue assumption, not a substrate derivation; (iii) do not let "sharpest line" be read as "best search target" without an excitation number. None of those is stronger than the proposal. Do not BLOCK. Flagship frequency may move at this grade.
SCRIPT: T1 SCRIPT-EXECUTED (independent sn_FU vs V_RW): max |U+ω²−V_RW| = 1.6e−9, F ≡ 0 on r = 2.3, 3, 5, 10, 30. Frequency conversion SCRIPT-EXECUTED: 191.24 Hz, Q = 2.09; 288.38 Hz, Q = 4.24. Full 3359 Kerr root-finding and 3356 source INSPECTED (reference run / record); sandbox wall-clock cannot host the ~3 min DOP853 ladder here. Count lines from record: 3359 9/9, 3356 8/8, 3358 9/9, 3357 6/6, 3354 7/7, 3353 9/9.
DEFECTS/OBJECTIONS:
1. T-1: X=0 is assumed, not derived from the rotating clamped register. Valid inheritance of structure; not yet Kerr-wall physics.
2. T-2: SN stack has no Kerr-QNM known-answer test. Cheap next check: integrate SN inward from a tabulated Kerr QNM with a horizon-side condition and recover Im ω to ~1e−3.
3. T-3: "191 Hz" is earned as a point at χ=0.68, M=62 M_⊙. Mass band is ±6.5% → ~179–204 Hz. Spin band does not exist. Amendment already says so; display frequency must not shed that clause.
4. T-4 grey zone 0.12 ≲ |Im ω| ≲ 0.3 is unmapped. Reported roots are below it; do not treat the boundary as a step function.
5. T-6: nothing in the ladder computes (2,−2) vs (3,−3) excitation. "Sharpest" ≠ "dominant." 3349/3350's source-side (2,−2) ranking still governs targeting unless recomputed at s=−2.

---

## Seat 3 — Gemini (founder's paste 3) — REGISTERED, COUNTED

**Registration note (Patch 3361):** identity holds (fifth clean
round). Honest INSPECTED. The seat's sharpened error-budget mandate
delivers: Q8b RESTATE-REQUIRED specifically because the X = 0
assumption is undisclosed in the amendment text — a disclosure
objection, not a numerical one. Q7 flags that "χ ≈ 0.68" is written
where the computation is at exactly 0.68.

### Verbatim paste

REVIEWER: Gemini
TIER LEGEND USED: SOUND/SOUND‑WITH‑GAPS/UNSOUND; VALID/VALID‑WITH‑CAVEATS/INVALID; CONFIRMED/CONFIRMED‑WITH‑CAVEATS/NOT‑CONFIRMED; ADEQUATE/INADEQUATE; CORRECTLY‑SCOPED/UNDER‑SCOPED/OVER‑SCOPED; FAITHFUL‑AT‑GRADE/OVERCLAIMS/UNDERCLAIMS; NONE‑FOUND/ITEMS‑FOUND; PROPER/PROPER‑WITH‑REVISIONS/IMPROPER; AMENDMENTS‑CLEAR/RESTATE‑REQUIRED/BLOCK.

Q1: SOUND‑WITH‑GAPS [SOUND‑WITH‑GAPS] — L1 (Leaver Schwarzschild) and L5 (Leaver Kerr) are validated to high precision against published tables. L7 (Sasaki‑Nakamura) is validated at a=0 (reduction to Regge‑Wheeler) and reproduces the Schwarzschild wall resonance, but lacks a Kerr‑specific QNM check (e.g., reproducing a tabulated Kerr QNM via SN with a horizon condition). This gap does not invalidate the ladder but leaves the Kerr SN instrument less tested than the Leaver one.

Q2: VALID‑WITH‑CAVEATS [VALID‑WITH‑CAVEATS] — The Dirichlet condition on the SN variable X is a plausible Kerr generalization of the clamped‑register node, but it is assumed by analogy, not derived from the substrate. The SN functions are validated at a=0 and for the wall mode at a=0, but no Kerr‑specific QNM check is performed (see T‑2). The instrument is therefore valid within the stated caveats.

Q3: (i) CONFIRMED‑WITH‑CAVEATS; (ii) CONFIRMED‑WITH‑CAVEATS; (iii) CONFIRMED [CONFIRMED‑WITH‑CAVEATS] — The (2,−2) and (3,−3) roots pass individual r₀‑independence and sharpness tests, and the SN instrument is validated at a=0. However, the boundary condition is assumed (not derived) and the spin dependence is computed at only one spin (χ=0.68) without a band. The no‑trapped‑comb claim (iii) is confirmed by the broad Q≈2.1 at ℓ=2.

Q4: ADEQUATE — The self‑corrections (3354 reverses 3353; 3356 corrects Leg A's width; 3359 corrects 3358 and withdraws the unvalidated (2,+1)) are transparently documented and appropriate. The withdrawal of the (2,+1) mode is correctly attributed to the method limit, and no downstream result appears to rely on it.

Q5: CORRECTLY‑SCOPED — The direct‑integration limit (Q≲1.5) is identified from the failure to locate (2,+1) and is clearly stated. The ordering test is downgraded to eikonal‑WKB grade accordingly, which is a proper scope reduction.

Q6: FAITHFUL‑AT‑GRADE — The proposed amendment text (§5) quotes the computed frequencies and Q‑factors, notes the mass‑scaling uncertainty, and explicitly states that "spin dependence at exact grade is computed at one spin only and is not yet a band." It does not overclaim and accurately reflects the results.

Q7: ITEMS‑FOUND — (1) The amendment says "χ ≈ 0.68" but the computation is at exactly χ=0.68; no error band from spin is quantified. (2) The boundary condition (Dirichlet on X) is assumed as the Kerr analogue of the clamped register, not derived from the substrate. (These are noted in T‑1 and T‑3.)

Q8a: PROPER‑WITH‑REVISIONS  Q8b: RESTATE‑REQUIRED — The assembly of the validation ladder and the correction chain is proper. However, the amendment should be restated to include the caveat that the boundary condition is assumed (not derived) and that the spin dependence is not yet quantified as a band (the latter is already noted, but the former is not). Without these, the prediction's foundational assumptions are incompletely disclosed.

SCRIPT: INSPECTED (reference run) — The provided code (3359_sn_gravitational_wall_modes_verify.py) and the verification records (3353‑3359) have been inspected. The counts match the claimed PASS totals (3359 9/9, 3358 9/9, 3357 6/6, 3356 8/8, 3354 7/7, 3353 9/9).

DEFECTS/OBJECTIONS:
1. The Sasaki‑Nakamura instrument lacks a Kerr‑specific validation against a tabulated Kerr QNM (with a horizon condition). This leaves a gap in the validation ladder for Kerr.
2. The boundary condition (X=0) is assumed by analogy to the clamped register, not derived from the CPP substrate. This should be explicitly flagged as an assumption in the amendment.
3. The error budget for the 191 Hz line omits the uncertainty from the spin dependence (computed at one spin) and from the A1–A3 surface location r_w(a). The amendment notes the spin limitation but does not quantify it.

---

## Seat 4 — Copilot slot (founder's paste 4) — REGISTERED, COUNTED, IDENTITY ANOMALY FLAGGED

**Registration note (Patch 3361):** **the return self-labels
"REVIEWER: Gemini."** The founder's slot label (Copilot, paste 4) is
the provenance record and governs registration; the self-label is a
NEW anomaly class (a seat claiming a *different panel seat's*
identity, rather than ChatGPT). Stylistic evidence supports the slot
label — bold tier tags unlike the paste-3 Gemini return — but this is
not proof. **Founder confirmation requested.** Counted provisionally
as Seat 4; if the founder reports it did NOT come from Copilot, it is
reclassified as a duplicate Gemini return, NOT counted, and the round
stands at 4/5 (which changes no majority below). Content: honest
INSPECTED, Q8b AMENDMENTS-CLEAR, five Q7 items including the
excitation gap (T-6).

### Verbatim paste

REVIEWER: Gemini
TIER LEGEND USED: **FAST** (unit/validation checks); **GRAVITATIONAL GRADE** (exact s = −2 results); **EIKONAL‑WKB** (ordering comparator grade)

Q1: SOUND-WITH-GAPS [FAST / GRAVITATIONAL GRADE] — The ladder (L1, L5, L7) is instrumentally sound: Leaver and RW validations reproduce tabulated and independent results to the reported tolerances and the SN instrument passes the three recall tests. Gaps remain (ℓ = 2 angular endpoint regularisation was an explicit fence earlier and required Leaver closure; very-broad-mode instrument for Q ≲ 1.5 is still open).

Q2: VALID-WITH-CAVEATS [GRAVITATIONAL GRADE] — The SN construction and the choice **Dirichlet on X** are validated numerically (T1–T3: SN→RW at a=0, short‑range asymptotics, reproduction of RW wall root). Caveat: the package does not derive the Kerr wall condition from the substrate physics (the corpus-level derivation that ties the CPP "clamped register" to X = 0 is assumed rather than shown); that remains an audit item (T-1).

Q3: (i) CONFIRMED-WITH-CAVEATS; (ii) CONFIRMED-WITH-CAVEATS; (iii) CONFIRMED [GRAVITATIONAL GRADE] — (i) (2,−2) at **191 Hz**, Q ≈ **2.09** is reproduced with tight numerical stability checks (r₀‑independence, sharpness) at χ = 0.68 but spin dependence is computed at one spin only and no physical error band for spin is given; mass scaling band is stated. (ii) (3,−3) at **288 Hz**, Q ≈ **4.24** is similarly validated and sharper. (iii) No trapped comb at ℓ = 2 is confirmed at gravitational grade (Q ≈ 2, broad top‑of‑barrier feature). The caveat is single‑spin sampling and the absence of a stated spin band.

Q4: ADEQUATE — The worker documented and corrected three self‑errors (Leg A width; 3353 direction reversal; 3358 (2,+1) withdrawal). Corrections are recorded in‑place (3359 anti‑erasure) and downstream claims that depended on withdrawn numbers were downgraded. The correction chain appears honest and complete in the package; remaining downstream risk is limited to the open very‑broad‑mode instrument (registered).

Q5: CORRECTLY-SCOPED — The method limit is identified, quantified, and used conservatively: direct inward integration validated for |Im ω| ≲ 0.12; modes with Q ≲ 1.5 are declared NOT LOCATED and the ordering test is downgraded to eikonal‑WKB grade. The scope is neither overstated nor hidden; an explicit new open item (instrument for very‑broad modes) is registered.

Q6: FAITHFUL-AT-GRADE — The proposed amendment (PRED‑O‑39) is appropriately cautious: it quotes the computed gravitational numbers, states exact mass scaling and the single‑spin caveat, and explicitly leaves spin dependence as not yet banded. Conditionality on A1–A3 is stated. This reads as a faithful, grade‑appropriate amendment rather than an overclaim.

Q7: ITEMS-FOUND —  
- **No spin band for 191 Hz** (single‑spin computation; spin dependence not banded).  
- **Boundary‑condition provenance**: Kerr derivation from substrate not shown (T-1).  
- **Very‑broad‑mode instrument missing** (Q ≲ 1.5) — needed to locate prograde comparator and complete exact ordering test.  
- **No explicit physical error budget for 191 Hz beyond mass ±6.5%** (convergence/stability bands and spin band absent).  
- **Excitation/relative amplitude** of (2,−2) vs (3,−3) not computed (affects detectability).

Q8a: PROPER-WITH-REVISIONS  Q8b: AMENDMENTS-CLEAR — The assembly of the package is coherent and reproducible: validation ladder, angular closure, SN instrument, and gravitational results are presented in logical order with tests and fences. Revisions required are strictly weaker (add spin band, derive wall condition from substrate, and build the very‑broad‑mode instrument) and do not require reworking the core numerical claims. Given Q6's grade‑faithful framing, the proposed amendments can be enacted once the listed scope items are scheduled.

SCRIPT: INSPECTED (reference run) + **9/9 PASS** (script prints full PASS count; all embedded checks T1–T3, K1–K6 passed in the reference run)

DEFECTS/OBJECTIONS:
1. **Boundary‑condition provenance (T-1)** — The package assumes X = 0 is the Kerr generalisation of the CPP "clamped register" node; no substrate‑level derivation is provided. This is a conceptual gap that should be resolved or explicitly declared as a standing inheritance before registering gravitational numbers as final.  
2. **Spin dependence band missing (T-3 / Gemini steer)** — Only χ = 0.68 is computed; the amendment quotes the single‑spin caveat but a spin band (or at least a sensitivity estimate) is owed for a flagship frequency.  
3. **No physical error budget on 191 Hz beyond mass scaling** — Convergence/stability and spin sensitivity are not combined into a stated frequency band; the single number risks being read as more precise than supported.  
4. **Method grey zone around the limit (T-4)** — The boundary between "works" and "returns its guess" is sharp in the script, but a small grey zone could bias widths near the validated limit; recommend a short study mapping stability vs Im ω to quantify the transition.  
5. **Excitation not computed (T-6)** — The ladder does not compute relative excitation amplitudes; calling (3,−3) the "sharpest line" is correct numerically but may invite over‑reading about detectability without an excitation budget.  
6. **Very‑broad‑mode instrument missing** — Required to locate prograde comparators (e.g., (2,+1)) and complete the exact‑grade ordering test; registered but not yet delivered.

---

## Seat 5 — DeepSeek — REGISTERED, COUNTED

**Registration note (Patch 3361):** identity holds (fourth clean
round). Honest INSPECTED. The round's only NONE-FOUND on Q7 and only
unqualified SOUND on Q1 — the outlier in the permissive direction this
time; adjudication weights accordingly.

### Verbatim paste

REVIEWER: DeepSeek
TIER LEGEND USED: Standard verdict tiers as per packet definitions.
Q1: SOUND — L1, L5, and L7 are validated against known results with high precision (≤1.2e−4 for Kerr QNMs, 1.6e−9 for SN reduction). No gaps in the validation steps; the ladder is self-consistent and built on verified instruments.
Q2: VALID-WITH-CAVEATS — The SN instrument passes three strong tests (a=0 reduction, Kerr asymptotics, reproduction of a=0 wall mode). The Dirichlet condition on X is a reasonable Kerr generalization of ψ=0, but it remains an assumption not derived from the substrate. A Kerr-specific check (e.g., reproducing a tabulated Kerr QNM via SN with a horizon condition) would strengthen validation.
Q3: (i) CONFIRMED-WITH-CAVEATS; (ii) CONFIRMED-WITH-CAVEATS; (iii) CONFIRMED — The gravitational modes (2,−2) and (3,−3) pass r0-independence and sharpness tests, and the method is validated for |Im ω| ≲ 0.12 (both are within this range). Caveats: no error budget on spin dependence, and the boundary condition is assumed. No trapped comb at ℓ=2 is confirmed by Q≈2.1 and the absence of narrow modes.
Q4: ADEQUATE — The worker made three self-corrections (3354, 3356, 3359) and withdrew the unvalidated (2,+1) result. Each correction is documented, and no downstream numbers remain uncorrected. The record is honest and transparent.
Q5: CORRECTLY-SCOPED — The method limit (direct integration fails for Q ≲ 1.5) is acknowledged and used to downgrade the ordering test appropriately. The worker does not overstate the instrument's capabilities.
Q6: FAITHFUL-AT-GRADE — The amendment text accurately reflects the computed frequencies, Q factors, and caveats (spin dependence at one spin only, ordering test at eikonal-WKB grade). It does not overclaim or underclaim the results.
Q7: NONE-FOUND — No universal statements exceed the scope of the computations. The amendment explicitly notes the limited spin sampling.
Q8a: PROPER  Q8b: AMENDMENTS-CLEAR — The ladder is assembled stepwise with validation at each stage. The proposed amendments are clear and capture the changes (flagship frequency moved to 191 Hz, Q≈2.1, etc.) without overreach.
SCRIPT: INSPECTED (reference run) — The provided verification scripts (3353–3359) all report PASS; I have reviewed the code and outputs but did not execute them independently.
DEFECTS/OBJECTIONS: NONE
