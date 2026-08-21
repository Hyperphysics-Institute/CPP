# CONV-034 — Returns receiver: OPEN-GR-RCORE-3 Legs A+B Audit

**Dispatched:** Patch 3335, 21 Aug 2026 (Session 156).
**Package:** `conv034_rcore3_audit_review_package_v1.0.md` (single
CONV-001 block; both records + both verify scripts inlined in full;
reference runs included; the two `.py` files also ship separately to
execution-capable seats).
**Under review:** the Leg-A instrument + findings (Patch 3333), the
Leg-B instrument + findings (Patch 3334), the retraction discipline,
the PROVISIONAL PRED-O-39 refinement text, and the GR-2 amendment
set. FENCED: A1–A3/censorship (CONV-032), GR-2 V1.0's eikonal-scoped
claims (CONV-033), |R| = 1, F-R1.
**Binding rules:** majority per question; majority INVALID on Q1/Q2
reverts the corresponding Leg to OPEN and strikes its amendment
items; majority OVERCLAIMS on Q5 blocks the predictions.md execution
regardless of Q7b.
**Seat mandates riding this dispatch:** IDENTITY (per-seat Gemini AND
DeepSeek lines), OWN-RUN (FAST-mode legitimate; reference-quoting =
INSPECTED), COUNT-LINE verbatim, INDEPENDENT-HARNESS available,
returns INLINE only.

**Status (Patch 3336): 5/5 REGISTERED SAME-SESSION — ROUND COMPLETE.**
All five returns inline, no delivery failures. Seat hygiene: Gemini
identity HOLDS (third clean round); DeepSeek identity HOLDS (second
clean round); GPT own-ran BOTH scripts (first full double own-run
from that seat — the FAST-mode design fully paid off); DeepSeek
own-ran both with verbatim count lines (its R(wall) = −3.267 probe
value is environment-consistent with the reference); Grok honest
INSPECTED + correctly-used INDEPENDENTLY RECOMPUTED on the two
load-bearing quantities (a→0 anchor, ¾ margin); Copilot honest
INSPECTED with two recorded anomalies (see its registration note).
Adjudication FINAL in `conv034_adjudication.md` (Patch 3336).

Returns are registered below VERBATIM in paste order, each with a
registration note. Adjudication lands in `conv034_adjudication.md`.

---

## Seat 1 — ChatGPT (GPT-5.6 Sol)

**Registration note (Patch 3336):** Third consecutive round as the
sole dissent whose revisions the adjudication adopts — the seat now
functions, de facto, as the corpus's grading auditor. FIRST FULL
DOUBLE OWN-RUN from this seat (both scripts, count lines verbatim):
the FAST-mode adoption built for its two rounds of friction is fully
validated. Its Q3(iii)/Q5 dissents carry the round's substantive
yield; its defect list maps the triage exactly (T-1/T-2 fire, T-3/T-5
pass, T-4 open).

### Verbatim paste

REVIEWER: GPT-5.6 Sol
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: VALID-WITH-CAVEATS [INSPECTED + SCRIPT-EXECUTED] — The Leg-A instrument design is substantially sound. The FD scattering-phase/Wigner-delay observable is the right way to distinguish a genuine cavity resonance from the failed carrier/autocorrelation interpretations, and the wall-shift test is particularly valuable because it interrogates the claimed geometric content rather than merely convergence. The supplied record also correctly retains the failed-instrument trail and explicitly retracts the finite-ℓ comb-spacing interpretation.  My own FAST run independently reproduces the Kerr-recon/closed-form subset 4/4. I did not execute the non-FAST FD+TD portion, so the χ=0 resonance numerics themselves remain INSPECTED rather than SCRIPT-EXECUTED for this seat. Caveat: "exactly ONE prominent resonance" depends on the declared prominence/smoothing prescription, so it is an instrument-relative statement; the cross-validation and above-barrier location make the physical conclusion substantially stronger than the peak-count algorithm alone.

Q2: VALID-WITH-CAVEATS [SCRIPT-EXECUTED + INSPECTED] — My own run reproduces all 7/7 checks, including the (a\to0) anchor, (\Phi_{\max}/\pi=0.178), the exposed-mode census, longest-cavity sensitivity (0.245\to0.304), and spin-scan maximum 0.247. The zero-trapped-mode conclusion has a large enough phase-volume margin that ordinary Maslov/turning-point convention changes do not plausibly turn the reported values into (N\ge1); even the package-wide maximum quoted, 0.366, remains far below 0.75.  Caveats are nevertheless material: fixed (Q=(\ell+1/2)^2-m^2) is an eikonal correspondence applied at (\ell=2), and the static Dirichlet wall omits the explicitly open co-rotation boundary condition. Thus I accept the **integer census at eikonal-WKB grade**, not exact finite-ℓ Kerr spectroscopy.

Q3: (i) CONFIRMED; (ii) CONFIRMED; (iii) NOT-CONFIRMED [SCRIPT-EXECUTED + INSPECTED] — (i) At the stated Leg-A grade, the evidence supports one broad above-barrier resonance rather than a sub-top trapped comb; importantly the record identifies (\omega_1) above (\sqrt{V_{\max}}) and reports FD/TD agreement.  (ii) CONFIRMED **at eikonal-WKB grade**: the own-run census gives (N=0) throughout the tested spin range with a large numerical margin. (iii) I do **not** confirm the numerical finite-ℓ claim "onset 0.665" as a physical ((2,+2)) result. The package itself states that
[
\mu=m/(\ell+\tfrac12)\approx \xi/\sqrt{\xi^2+\eta}
]
is an eikonal correspondence, approximate at (\ell=2), while the reported GW150914-class margin is only (0.800-0.774=0.026).  That is precisely the regime where an unquantified finite-ℓ correspondence error can move the boundary. What **is** confirmed is the conditional statement: *under this geodesic/eikonal correspondence*, the calculation gives onset ≈0.665 and burial at χ=0.68. The stronger language that the actual finite-ℓ ((2,+2)) mode buries at 0.665 outruns the method's error control.

Q4: ADEQUATE — The +1–3% correction is fully killed, not merely demoted. The record explicitly identifies why the attractive 7.00 versus 7.045 agreement was misleading: the measured quantity was (\pi/\omega_1), and (\omega_1\simeq\pi/(2L)) structurally creates the coincidence. It also preserves convergence/parity agreement as examples of diagnostics that did **not** validate the interpretation. That is exactly the right anti-erasure discipline.

Q5: OVERCLAIMS — The load-bearing **"no comb / (N_{\rm trapped}=0)"** refinement is faithful at grade. The proposed numerical line set is not. Transporting a **single χ=0, ℓ=2 calibration of +17%** across (m=-2,-1,0,+1), into Kerr at χ≈0.68, and even to (\ell=3), does not provide a demonstrated error model for "~247–344 Hz." The record itself admits that the above-top shift was calibrated at one point and that exact positions require full Teukolsky work.  The tilde does not repair that inferential gap. Likewise (Q\sim5) is transported from Leg A without a Kerr/mode-dependent width calculation. The prediction should instead say **"mode-resolved lines near the corresponding barrier-top frequencies; positions and widths not yet quantitatively predicted pending full finite-ℓ Kerr/Teukolsky calculation."** The raw eikonal-top ordering (approximately 211, 233, 260, 294 Hz for the listed ℓ=2 modes at the adopted mass/spin) may be retained explicitly as an **orientation-scale calculation**, not upgraded through the universal ×1.17 transport into a registered predicted band. Because Q5=OVERCLAIMS, the package's binding rule blocks predictions.md execution.

Q6: MISSING-ITEMS — The amendment set needs two grading corrections before execution: (1) onset 0.665 must be described as **"0.665 under the eikonal/geodesic μ correspondence; finite-ℓ onset unquantified"**, rather than as the mode-resolved physical onset simpliciter; and (2) the line-set restatement must remove or explicitly demote the universal +17% transport and Kerr (Q\sim5). The Leg-A pointer, disappearance of the comb, thin-margin warning, and line-set qualitative restatement are otherwise appropriate additive amendments under the existing eikonal scoping.

Q7a: PROPER-WITH-REVISIONS  Q7b: RESTATE-REQUIRED — The important negative result survives my audit: **the finer calculation does not rescue the eikonal comb; the available WKB phase volume is nowhere remotely sufficient for a sub-top trapped-mode ladder in the audited census.** That is a substantive and useful discharge at its stated grade. The retraction discipline is also strong. But the package crosses its own grade boundary when it converts a one-point Schwarzschild calibration into a quantitative Kerr line band and when it treats an uncontrolled ℓ=2 eikonal correspondence as sufficient to mint a numerical burial onset. Those are repairable without rerunning the central census. Under the frozen rule, Q5=OVERCLAIMS independently prevents immediate predictions.md execution. The package itself correctly identifies these as its T-1/T-2 weak points.

SCRIPT: SCRIPT-EXECUTED (own run) + verbatim count lines:
FAST: 4/4 PASS
7/7 PASS
FAST: all checks are FAST (no TD evolution in this instrument); FAST: 7/7 PASS

DEFECTS/OBJECTIONS:

1. **T-1 fires:** the universal **+17% calibration transport is not established.** One Schwarzschild ℓ=2 calibration cannot presently support ~247–344 Hz as a registered Kerr prediction. Retain barrier-top frequencies as orientation-scale estimates or widen the prediction to "near the mode-dependent barrier tops."
2. **Transported (Q\sim5) has the same problem.** Leg A's χ=0 RW/Zerilli widths do not establish Kerr widths for every exposed ((\ell,m)).
3. **T-2 fires on the numerical onset:** χ=0.665 and the 0.026 burial margin are outputs of an uncontrolled ℓ=2 use of an asymptotic correspondence. Report them as **geodesic-correspondence estimates**, not established finite-ℓ mode thresholds.
4. **The qualitative burial result is stronger than the numerical onset.** The wave-side ((2,+2)) result at χ=0.68 is useful supporting evidence, but it uses the same fixed-eikonal-Q construction and therefore does not independently eliminate the finite-ℓ correspondence uncertainty.
5. **T-3 does not fire:** the phase-volume margin is large. The reported maximum 0.366π versus the nominal 0.75π threshold is sufficiently separated that reasonable WKB phase-offset conventions do not look capable of manufacturing a trapped comb.
6. **T-4 remains genuinely open:** co-rotation can alter mode-dependent boundary phases/frequencies. Nothing in these two patches demonstrates that it cannot alter detailed line structure. I see no supplied evidence that it plausibly overturns the large (N=0) phase-volume margin, but that stronger robustness claim has not itself been computed.
7. **T-5 passes:** the +1% result is genuinely retracted and its seductive convergence/parity agreement is not used afterward to resurrect it.

---

## Seat 2 — Grok (xAI)

**Registration note (Patch 3336):** Honest INSPECTED on the scripts,
with the INDEPENDENTLY RECOMPUTED tier used exactly as designed on
the two load-bearing quantities (the a→0 anchor and the ¾-threshold
margin). Its two defects concede the substance of the dissent seat's
T-1/T-2 while reading the grade language as sufficient — the
adjudication resolves that split.

### Verbatim paste

REVIEWER: Grok (xAI)
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: VALID [INSPECTED] — The FD scattering-phase + Wigner-delay instrument is correctly validated by the wall-shift test (geometric-optics plateau growth) and by TD cross-validation at the 1 % level. The five-dead-end trail is fully documented and the final instrument is free of the carrier-period trap.

Q2: VALID [INDEPENDENTLY RECOMPUTED] — The WKB census recovers the a→0 Leg-A result exactly (N=0, ω_top match <1 %). The ¾-threshold margin is everywhere ≥ factor 2 (largest Φ_max/π = 0.366), so phase-convention uncertainty cannot flip any N to 1. Grid density and turning-point clipping are adequate for an integer count.

Q3: (i) CONFIRMED; (ii) CONFIRMED; (iii) CONFIRMED [INSPECTED] — Single top-of-barrier resonance at χ=0 is robust. N_trapped = 0 at every astrophysical spin is the load-bearing integer result. The (ℓ,ℓ) burial onset 0.665 with thin margin is correctly graded as geodesic/eikonal-correspondence and carries the stated caution.

Q4: ADEQUATE — The +1 % claim is fully dead; the structural coincidence π/ω₁ ≈ eikonal is correctly diagnosed; the five-dead-end trail is retained in the script header exactly as required by computation-before-claims.

Q5: FAITHFUL-AT-GRADE — The provisional PRED-O-39 text correctly converts the eikonal comb into a mode-resolved line set plus early transients, preserves retrograde keying as line ordering, and keeps the +17 % calibration and Q~5 as grade statements rather than precise predictions.

Q6: COMPLETE — The additive amendment set (Leg-A pointer, onset 0.665, thin-margin caution, line-set restatement) exhausts the new content under the existing eikonal scoping of GR-2 V1.0.

Q7a: PROPER
Q7b: AMENDMENTS-CLEAR — Both legs discharge their portions of OPEN-GR-RCORE-3 at the stated grades; the refined search target is ready for founder ratification and the additive GR-2 / PRED-O-39 updates.

SCRIPT: INSPECTED (reference runs) + independent numeric checks on a→0 anchor and ¾-threshold margin
(Full own-run of the TD portion of Leg A was not required for the integer census results that carry the load.)

DEFECTS/OBJECTIONS:
1. The +17 % single-point calibration transport remains the weakest quantitative statement; the "~" and grade language are honest, but a future Teukolsky upgrade should replace it.
2. The ℓ=2 μ-correspondence error is unquantified; the thin (2,+2) margin could in principle sit inside that error. The geodesic-grade label already acknowledges this.

---

## Seat 3 — Gemini

**Registration note (Patch 3336):** Identity HOLDS — third
consecutive clean round; the cure is settled law. Visible thinking
registered verbatim. One tension for the adjudication: as the
error-budget seat it certifies "It does not quote precision it
cannot know," while the adopted revisions (below) conclude the +17%
band was exactly that — recorded honestly, without prejudice: the
majority read the declared grade statement as sufficient control.

### Verbatim paste

Thinking...
Reviewing CONV-034 Package
I've begun the initial assessment of CONV-034, focusing on understanding the core tenets of the presented physics theory. My immediate priority is to grasp the fundamental concepts and identify any preliminary areas requiring deeper scrutiny, setting the stage for a thorough evaluation.
Assessing Input Validity
My current focus is on evaluating the provided input against established criteria, particularly concerning the precision and expression of uncertainty in quoted numerical data. I'm scrutinizing whether every figure presented inherently acknowledges its own limitations and potential unknowns.
Validating Numerical Claims
I'm now delving into the specific numerical claims, confirming that the reported values align with the underlying calculations and that uncertainties are consistently and appropriately expressed. This involves checking if the stated precision reflects the methodology's limitations.
REVIEWER: Gemini
TIER LEGEND USED: INSPECTED
Q1: VALID [INSPECTED] — The frequency-domain scattering phase instrument is robustly validated by the geometric wall-shift test and independently cross-validated by the time-domain evolution (yielding agreement within 3%).
Q2: VALID [INSPECTED] — The eikonal-WKB instrument is appropriately anchored to the a→0 limit, successfully reproducing the Leg-A finding of zero trapped resonances, and explicitly tests sensitivity to the wall position.
Q3: (i) CONFIRMED; (ii) CONFIRMED; (iii) CONFIRMED [INSPECTED] — The reference scripts clearly demonstrate the single resonance above the barrier at χ=0, the robust N=0 census across all astrophysical spins, and the μ_crit threshold computation yielding the 0.665 onset with its thin margin.
Q4: ADEQUATE — The retraction of the provisional +1% claim is explicit, and the documentation of the five dead ends (especially the structural coincidence of the carrier half-period) demonstrates excellent scientific honesty.
Q5: FAITHFUL-AT-GRADE — As the error-budget seat, I confirm the text strictly bounds its claims. It explicitly tags the frequencies with "~", names the "+17% calibration" transport, states the Q∼5 approximation, and correctly defers exact line positions to full-Teukolsky work. It does not quote precision it cannot know.
Q6: COMPLETE — The amendment set correctly folds in the Leg-A pointer, the refined 0.665 onset, the thin-margin caution, and the line-set restatement without invalidating the previously scoped eikonal claims.
Q7a: PROPER Q7b: AMENDMENTS-CLEAR — The assembly honestly discharges the eikonal systematic identified in GR-2 V1.0 and refines the search target with appropriate error language.
SCRIPT: INSPECTED (reference run)
DEFECTS/OBJECTIONS: NONE

---

## Seat 4 — Copilot (Microsoft AI)

**Registration note (Patch 3336):** Identity correct; honest
INSPECTED tier, which remains legal. TWO anomalies recorded without
prejudice: (a) its preamble asserts "You did not request an OWN-RUN,
and nothing in the steer requires me to run the scripts" — this
MISSTATES the package: §5's OWN-RUN mandate binds all seats
(INSPECTED is the honest fallback tier, which the seat correctly
used, but the justification misreads the mandate); (b) the return is
wrapped in assistant-chatter addressed to the founder, closing with
offers to "apply the amendment set" and "update predictions.md once
ratified" — actions firmly outside a review seat's role; no standing,
noted for the seat-conduct ledger. The §8 skeleton content itself is
complete and properly formatted.

### Verbatim paste

Thomas — **I have everything now.**
Parts 1–3 give the *full* CONV‑034 review package, including:

- Leg‑A record
- Leg‑B record
- Frozen questions
- Seat mandates
- Reference runs
- The §8 return skeleton

My seat is **Copilot**, the registry/discipline seat.
Per mandate, I must:

- Audit registry discipline
- Verify no improper edits to predictions.md or GR‑2
- Verify amendment set is additive under CONV‑033 scoping
- Verify anti‑erasure on the retraction
- Answer Q1–Q7 using ONLY the allowed vocabulary
- Tag each answer with INSPECTED / SCRIPT‑EXECUTED / INDEPENDENT‑HARNESS
- Provide COUNT‑LINE if I run the scripts

You did **not** request an OWN‑RUN, and nothing in the steer requires me to run the scripts.
So I will answer using **INSPECTED** tier.

Below is your **complete §8 reviewer return**, ready for panel aggregation.

---

# **§8 — Copilot Reviewer Return (CONV‑034)**

REVIEWER: Copilot
TIER LEGEND USED: INSPECTED

---

### **Q1 — Leg‑A instrument**
**VALID** [INSPECTED] — The FD scattering-phase instrument is validated by the wall‑shift test (4.12 vs 4.00 geometric), stable under grid/box refinement, and cross‑checked by TD evolution (0.4488 vs 0.4535). The record preserves the full dead‑end trail and clearly identifies why earlier instruments failed. Registry discipline is intact: the retraction is explicit, anti‑erasure is honored, and the validated instrument is correctly marked as the one that discharged Leg‑A.

---

### **Q2 — Leg‑B instrument**
**VALID-WITH-CAVEATS** [INSPECTED] — The WKB census is internally consistent, reproduces the a→0 Leg‑A anchor, and the Φ_max/π values remain well below the ¾ threshold across spins and wall positions. The caveat is correctly stated: fixed‑Q correspondence is exact only as ℓ→∞, and the +17% calibration is a single‑point transport. The record states these limits explicitly, and registry discipline is correct.

---

### **Q3 — Findings**
(i) **CONFIRMED** — Single top‑of‑barrier resonance at χ=0; no surviving comb.
(ii) **CONFIRMED** — N_trapped = 0 at every spin; comb not restored.
(iii) **CONFIRMED** — (ℓ,ℓ) burial with onset 0.665 and thin margin, at geodesic grade.
[INSPECTED] — All findings match the reference runs and are correctly graded. The thin‑margin caution is explicitly preserved, and the μ‑mapping limitations are stated.

---

### **Q4 — Retraction discipline**
**ADEQUATE** — The +1% provisional claim is fully dead: the record preserves the entire five‑instrument trail, explains precisely why the earlier instruments misled, and identifies the structural coincidence (π/ω₁ ≈ eikonal) that produced the false match. Anti‑erasure is honored: the dead‑end trail is kept in the script header and record §3.

---

### **Q5 — Provisional PRED‑O‑39 refinement text**
**FAITHFUL-AT-GRADE** — The refinement text correctly reflects Leg‑B's result: the search target is a line set (~247–344 Hz with +17% calibration) plus early transients at 2.624 ms. Conditionality is stated (eikonal‑top grade, Q~5, A1–A3 inherited). No overclaiming: the text does not mint new predictions and does not exceed the grade of the instruments.

---

### **Q6 — GR‑2 amendment set**
**COMPLETE** — The amendment set (Leg‑A pointer, onset 0.665, thin‑margin caution, line‑set restatement) is additive under the CONV‑033 scoping and does not alter any shipped claim. Registry audit: predictions.md and GR‑2 V1.0 are **not** edited; amendments are queued exactly as required.

---

### **Q7a — Two‑patch assembly overall**
**PROPER** — Both legs are validated at their stated grades, conditionality is preserved, retraction discipline is strong, and registry bookkeeping is correct.

### **Q7b — Disposition**
**AMENDMENTS-CLEAR** — No blocking defects; no overclaims; no invalid instruments. The amendment set may proceed to execution upon founder ratification.

---

### **SCRIPT**
**INSPECTED** — Reference runs used:
- Leg‑A FAST: 4/4 PASS; full: 9/9 PASS
- Leg‑B FAST: 7/7 PASS

No own-run performed (seat steer did not require execution).

---

### **DEFECTS/OBJECTIONS**
**NONE**

---

Thomas — this is your complete Copilot seat return for CONV‑034.
If you want, I can now help you:

- Aggregate the five-seat verdicts
- Prepare the founder ratification question
- Apply the amendment set
- Update predictions.md once ratified

Just tell me the next step.

---

## Seat 5 — DeepSeek

**Registration note (Patch 3336):** Identity HOLDS — second
consecutive clean round; the per-seat line's cure is durable. Full
own run of BOTH scripts with verbatim count lines; its Leg-B check-2
probe value (R(wall) = −3.267) differs from the reference print only
by the probe frequency's environment-dependent selection —
consistent, not anomalous. As the falsifier seat, its reasoning
(registered below) walks the kill-condition audit the steer asked
for: line ordering as discriminator, the thin-margin spin
sensitivity of the (2,+2) absence, and null-explain-away carried by
the CONV-033 preregistered criterion.

### Verbatim paste

*Thinking...*

> We are reviewing two legs of OPEN-GR-RCORE-3: Leg A (finite-ℓ cavity spectroscopy at χ=0) and Leg B (Kerr cavity census). The goal is to audit the computations and their findings, and to decide on the proposed amendments to GR-2 and PRED-O-39.
>
> We are asked to answer specific questions with given vocabulary. We must also note our identity and tier of verification.
>
> We are DeepSeek, and we are the falsifier seat. Our role is to assess the falsifiability of the line-set target and the kill conditions.
>
> We are to run the scripts ourselves if possible. The scripts are provided. We can run them in FAST mode. We note that the Leg-B script is all-FAST (7 checks, ~1 min). We will run both scripts in FAST mode and report the count lines.
>
> We are to address the triage points, but our answers are structured by the frozen questions.
>
> We are to check the line ordering as a falsifiable condition and the null result explain-away.
>
> Let's proceed.
>
> [Own-run outputs registered: Leg-A FAST 4/4 with full mode table (values matching the reference: (2,+2) r_sp=2.1631 M FULLY-BURIED, mu_crit=0.774, onset 0.665, margin 0.026); Leg-B full 7/7 with census table matching the reference (211/233/260/294/292 Hz tops; Phi_max/pi 0.245/0.138/0.056/0.007/0.366; spin-scan max 0.247 at 0.52; monotone omega_top 0.4425→0.3846); R(wall) probe −3.267.]
>
> Now we answer the questions... [reasoning on Q1–Q7 as registered in the verdicts below]
>
> Now, as the falsifier seat, we must consider the triage points and our specific role. We are to assess the falsifiability of the line-set target. The line ordering (corotating lines absent) is a structural discriminator. However, note that the (2,+2) mode is buried, but (2,+1) is exposed. So the absence of the (2,+2) line and the presence of the (2,-2) line is a specific pattern. But what if the (2,+2) line is not buried? The onset is at χ=0.665, and for χ=0.68 it is buried, but with a thin margin. If the actual spin is slightly lower, the (2,+2) mode might become exposed. This is a caveat. Also, the line frequencies are approximate. The null result explain-away: if no lines are detected, it could be because the signals are too weak, or the search is not sensitive to these frequencies. The CONV-033 caveat about the selection function (RCORE-2(viii)) still applies. The refined target does not change the falsifiability significantly; it just changes the expected signal from a comb to a set of lines. The kill conditions from CONV-033 (prograde-keyed comb at χ>0.55) are still valid, but now we have an additional discriminator: the line ordering. We think the falsifiability is preserved.
>
> We note no defects or objections.
>
> We will now write the response in the required skeleton.

**REVIEWER:** DeepSeek
**TIER LEGEND USED:** SCRIPT-EXECUTED

**Q1:** VALID-WITH-CAVEATS [SCRIPT-EXECUTED] — The Leg-A instrument (frequency-domain scattering phase + wall-shift validation + TD cross-validation) is sound for its stated scope (χ=0, ℓ=2). The FAST checks pass, and the wall-shift validation confirms geometric optics. Caveat: the TD cross-validation is at a single point (χ=0, ℓ=2) and does not fully probe the Kerr regime, but this is within the stated grade of Leg A.

**Q2:** VALID [SCRIPT-EXECUTED] — The Leg-B instrument (WKB census with fixed Q, ¾ threshold, a→0 anchor) passes all 7 checks. The a→0 validation successfully reproduces Leg A's zero sub‑top resonances, and the spin scan confirms robustness. The instrument is appropriate for the eikonal‑WKB grade.

**Q3:** (i) CONFIRMED; (ii) CONFIRMED; (iii) CONFIRMED [SCRIPT-EXECUTED] —
(i) Leg‑A finds exactly one top‑of‑barrier resonance per parity at χ=0 (ω₁≈0.4535/0.4513, above √V_max=0.389).
(ii) Leg‑B census shows N_trapped=0 for all exposed modes at χ=0.68 and across the spin scan (max Φ_max/π=0.247 < ¾).
(iii) The (ℓ,ℓ) burial onset is χ=0.665 with thin margin (0.026) at χ=0.68, as computed in Leg‑A's geodesic reconnaissance. All findings are consistent with the script outputs.

**Q4:** ADEQUATE — The retraction of the provisional "+1% comb correction" is thoroughly documented (five dead‑end trails, wall‑shift test failure, structural coincidence). The record honestly describes the traps and the corrected conclusion (no comb at ℓ=2, χ=0).

**Q5:** FAITHFUL‑AT‑GRADE — The provisional PRED‑O‑39 refinement text ("line set at ~247–344 Hz, grade: eikonal‑top +17% calibration, Q~5, corotating (ℓ,ℓ) lines absent") explicitly states its grade and uses "~" for the frequencies. It does not overclaim; the +17% calibration from a single point (χ=0, ℓ=2) is noted, and the uncertainty is acknowledged.

**Q6:** COMPLETE — The proposed GR‑2 amendment set (Leg‑A pointer, burial onset 0.665, thin‑margin caution, line‑set restatement) is additive under the existing eikonal scoping and addresses all new findings. No missing items.

**Q7a:** PROPER  **Q7b:** AMENDMENTS‑CLEAR — The two‑patch assembly is proper: inputs are verified, conditionality is stated, and the findings discharge the stated open problems at their respective grades. The amendments can proceed to execution.

**SCRIPT:** SCRIPT‑EXECUTED (own run) + verbatim count line(s)
Leg‑A FAST:
```
FAST: 4/4 PASS
```
Leg‑B:
```
7/7 PASS
FAST: all checks are FAST (no TD evolution in this instrument); FAST: 7/7 PASS
```

**DEFECTS/OBJECTIONS:** NONE
