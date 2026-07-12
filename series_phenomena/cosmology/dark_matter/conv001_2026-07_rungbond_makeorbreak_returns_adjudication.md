# CONV-001 RETURNS — rung-bond SSV make-or-break (2426+2427). Adjudication (worker; no verdict moved — founder calls it)

**Five seats returned.** Tally: **1 VERIFIED (Grok), 4 VERIFIED-WITH-CAVEATS (GPT, Gemini, Copilot, DeepSeek).**
Unanimous on the local algebra; unanimous that the NET picture is **"not-yet-falsified," not "survives."** The panel
materially changed the picture and caught a real error in 2427. Recorded here; the founder adjudicates.

## What the panel VERIFIED (5/5)
- **The local reduction κ_θ/E_bond = 2R_perp²/d² ∈ [0.74, 1.51]** (R_perp ∈ [0.7,1.0] fm, d=1.15) clears 0.43.
  Grok independently re-derived it and the crossover R_perp* = 0.53 fm. Algebra is sound *as a reduced-model result*.
- **E_bond = 494 keV is a real Madelung output** at R_perp=0.9 fm (all seats reproduce it).
- **Earnshaw → dynamic** is correctly read (static κ<0; stiffness must be dynamic).

## Three findings that change the disposition (I accept all three)

### 1. Gemini (D) is correct, and it exposes an OVERCLAIM in my 2427 — I own this.
κ_θ is a **transverse/bending** stiffness. 2427 tested the **axial** dynamic mode (1D bond average) and concluded
"no branch sinks it." But by Laplace ∇²V = 0, the ponderomotive curvatures in **orthogonal** directions have
opposite-sign static seeds and need NOT share the f_ZBW prefactor: **f_stiff (transverse) ≠ f_depth (axial) is not
excluded** — it is the generic anisotropic-trap case. So 2427 tested the wrong mode for the make-or-break. **My
"the |V''| assumption holds / no branch sinks it" claim is retracted to: the AXIAL branch is favorable; the
TRANSVERSE (bending) branch — the one that actually sets κ_θ — is UNTESTED and can soften independently.** The
Kapitza question is therefore **reopened**, now sharpened to a specific target: the transverse ponderomotive
(Floquet) curvature of the outer eCP vs the axial one.

### 2. The r-band tension is real (GPT, Grok, Copilot, DeepSeek) — direction is UP, correcting DeepSeek.
κ_θ/E_bond ∈ [0.74,1.51] ⇒ via the registered relation **r = ε·(κ_θ/E_bond)** (ε=29.7) ⇒ **r = ℓ_p/ℓ_rung ≈ 22–45**,
2–4× the registered [8.5,12] ⇒ N_stab ≈ 10–21 ⇒ ring family drifts **N=8 (11.26 GeV) → N≈10–21 (15–30 GeV)**.
**DeepSeek's correction is noted but its arithmetic is wrong**: it used ℓ_p = √(κ_θ/E_bond) → r≈1 → "too floppy."
That is not the registered relation (r = ε·(κ_θ/E_bond), not √). The correct direction is r **too STIFF** (heavier
ring), not too floppy. DeepSeek's instinct ("~factor 10 mismatch") is right; its sign is inverted. Either way: the
derived ratio is inconsistent with the registered N=8 point and the DD-selection must be re-run at the new mass.

### 3. E_bond "validation" is a consistency check, not independent validation (GPT) — own it.
The 494-vs-490 keV headline uses f_ZBW=1.0; the committed code's default f_ZBW=0.5 returns 247 keV. And 490 keV is
an earlier internal rung-bond estimate, not an external measurement. So 494≈490 is a **self-consistency check**
(and the geometry does reproduce the internal scale), NOT an independent validation. Reframe accordingly.

## Copilot (B), also accepted
The "E_ee sets bending, E_qq only global rigidity" split is a **model choice**, not a derived constraint — no
registered mechanism forbids the continuous E_qq spine from entering per-joint bending. If a modest fraction does,
the band shifts (and the +E_qq≈54 "absurd" value flags that the beam decomposition itself may be the wrong
framework for a continuous spine). Bound the E_qq bending contribution or justify its exclusion.

## Net disposition (worker recommendation — founder decides)
**Verdict: VERIFIED-WITH-CAVEATS → the make-or-break is NOT leaning favorable; it is OPEN.** The favorable local
number is (a) possibly an artifact of the untested transverse mode [1], (b) built on an under-justified E_ee-only
decomposition [Copilot B], and (c) inconsistent with the registered candidate point / drifts the mass [2]. Correct
survival language: **not-yet-falsified**, not "survives."

**Candidate (B)** retained as a **Cross-Rod ring family, mass-drift OPEN**, conditional on, in priority order:
1. **The transverse (bending) dynamic stiffness** — the corrected make-or-break (Gemini D). Compute the transverse
   ponderomotive Floquet curvature of the outer eCP vs the axial one; does f_stiff track f_depth or soften? THIS
   is the number that now decides the candidate. (Supersedes 2427's axial-only result.)
2. **r-band reconciliation** — is the registered [8.5,12] a superseded floppy-chain estimate, or does the beam
   derivation over-stiffen (Copilot B)? Resolve before any mass-dependent downstream.
3. **R_perp relaxation** — dynamically relax the transverse cross-section (ratio ∝ R_perp², load-bearing).
4. **Re-run formation + DD + Ω_DM at the resulting N-distribution.**

**Ω_DM: DO NOT BUILD YET.** 5/5 effectively agree building at a sharp N=8 is premature — the mass is entangled
with items 1–2. (Gemini: expects the transverse mode to drag the ratio back toward 0.345 → N=8; GPT/Grok: build at
drifted mass; Copilot: N=8 provisional; DeepSeek: N=8 registration refuted pending resolution.) The mass is not
pinned until item 1 closes.

## Bottom line
The panel did exactly what it was for: it caught that 2427 answered the axial question when the make-or-break is the
transverse one. The honest state is **OPEN on the transverse dynamic stiffness**, with the local geometry (2426)
verified and the r-band + E_bond framing flagged for reconciliation. Next calculation: the transverse ponderomotive
stiffness (item 1).
