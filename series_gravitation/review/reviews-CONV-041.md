# CONV-041 — Returns receiver: WIN-CHECK — the static R-core: surface condition, tidal Love numbers, thin-shell reading, fixed compactness

**Dispatched:** Patch 3628, 4 Sep 2026 (Session 161), on the founder's steer ("do the review protocol if you think it will help with the next derivations") — the next derivations rest on the static picture audited here.
**Package:** `conv041_static_rcore_love_numbers_review_package_v1.0.md` (CONV-001 single block; 3622/3624/3625/3626 records + three scripts inlined).

**What this round gates:** Q1 the static equations; **Q2 the surface condition K(R) = 0 and whether dropping the second junction condition hides a parameter**; Q3 the rigid-interior sign argument; Q4 the magnetic matching + convention; Q5 the thin-shell reading vs the corpus's mass bookkeeping; **Q6 the fixed-compactness claim (C = 0.375 for every R-core) — sound as derived? viable against neutron-star data?**; Q7 detectability; Q9 whether V2.1's tidal block stands.

**Binding rules:** UNSOUND on Q2 voids the Love numbers (→ a family over the surface condition); YES on the hidden parameter obliges it into the open item and V2.1; EXCLUDED-BY-NS-DATA on Q6 obliges a corrigendum before the claim is used further.

**Seat mandates:** IDENTITY, OWN-RUN (3624 9/9; 3625 6/6; 3626 3/3), EK-1 sealed (§6), COUNT-LINE, TIER, inline.

**Returns: 5/5 (GPT, Grok, Gemini, Copilot, DeepSeek). Adjudicated Patch 3629.**

---

## Seat 1 — GPT
Q1 SWC (3624's BH check is vacuous — 'or True'); Q2 SWC, hidden parameter YES (the second Israel condition and the shell's constitutive law are absent; 'adjusting stress' is an unspecified response); Q3 UNSOUND (constant strain not globally pure gauge with a boundary; 'curved solution needs stress' false for externally sourced vacuum tidal curvature); Q4 UNSOUND (h₀′ continuity assumes no axial shell current; k₂^B extracted by catastrophic cancellation of ~3e9 quantities; convention uncalibrated; BP cited); Q5 UNDETERMINED (shell, count, ADM masses not bridged); Q6 SWC, standing UNDETERMINED (conditional on a saturation rule; NICER radii far above 8M/3); Q7 OVERSTATED (leading term at v = 0.4; needs PE study); Q8 12 items; Q9a PWR, Q9b RETRACT. SCRIPT-EXECUTED 9/9, 6/6, 3/3. EK-1 matched. 12 defects.

## Seat 2 — Grok
Q1 SOUND (Hinderer's vacuum coefficients reproduced; the axial form standard); Q2 SWC, YES (not a complete Israel problem; S_ab or a second BC free; the exterior-lapse level set would change ξ); Q3 SWC (legitimate A3′ argument for no extra interior ODE; consistent with 3605 only if the Sea's strain IS the moving level set); Q4 SWC (a shell can carry an axial surface current; BP vs Damour–Nagar/Landry–Poisson magnetic numbers differ, even in sign between static and irrotational — name the convention); Q5 UNDETERMINED (three accountings not identified by one rule); Q6 SWC, UNDETERMINED (decides: a saturation threshold; if any measured NS must be an R-core → EXCLUDED); Q7 OVERSTATED; Q8 4 items; Q9a PWR, Q9b RESTATE. INDEPENDENT-HARNESS on L1/K(R)=0/Hinderer/Israel. EK-1 matched. D1: y = −31/3 exactly.

## Seat 3 — Gemini
Q1 SOUND; Q2 SOUND, NO (the second junction dictates the induced shell stress needed to maintain the cap, no free parameter in the exterior matching); Q3 SOUND (the founder's Sea deformation IS the moving level set; interior rigid); Q4 SOUND; Q5 CONSISTENT; Q6 SOUND, UNDETERMINED (a saturation threshold; NS not R-cores if they do not reach the floor); Q7 FAIR; Q8 NONE; Q9a PROPER, Q9b STANDS. INSPECTED. EK-1 matched. No defects.

## Seat 4 — Copilot
Q1 SWC; Q2 SWC, YES (second junction dropped; a constitutive law or surface EOM needed); Q3 SWC (explicit exclusion of admissible capped-core stresses needed); Q4 SWC (cross-check BP/DN; quantify the 13%); Q5 CONSISTENT (with the bridge owed); Q6 SWC, EXCLUDED-BY-NS-DATA (C = 0.375 vs NS 0.15–0.25; decides: saturation-threshold physics vs the NS survey); Q7 FAIR; Q8 6 items; Q9a PWR, Q9b RESTATE. SCRIPT-EXECUTED 9/9, 6/6, 3/3. EK-1 matched. 7 defects.

## Seat 5 — DeepSeek
Q1 SOUND; Q2 SWC, YES (shell stress not determined by any corpus rule); Q3 SOUND; Q4 SWC (convention); Q5 CONSISTENT; Q6 SWC, UNDETERMINED (a saturation criterion); Q7 FAIR; Q8 NONE; Q9a PROPER, Q9b RESTATE. Claims SCRIPT-EXECUTED with the package's count lines, but **EK-1 = y=-10.3300;k2=-0.0800;m=1.3333 — read from the package's 2-decimal print, not computed; does not match the hash** (the 3394 pattern: the key did its job). Treated as INSPECTED.

---

## Adjudication (Patch 3629)

| Q | tally | verdict | binding consequence |
|---|---|---|---|
| Q1 | SOUND 3 (Grok, Gemini, DeepSeek) / SWC 2 | **SOUND** (caveat adopted: the vacuous 3624 check replaced by a real BH-limit check — passes to 1e-10) | — |
| Q2 | SWC 4 / SOUND 1; hidden parameter **YES 4–1** | **SWC; YES** | **BINDING: the shell's second junction datum (S_ab / a constitutive law) is an open parameter — into the open item and V2.1's text; the Love numbers are the K(R) = 0 member of a family** |
| Q3 | SOUND 2 / SWC 2 / UNSOUND 1 → SOUND folds | **SWC 4–1** | GPT's objection answered by computation (3629 §2): the static VACUUM tide inside a flat region is a lapse + pure-trace (conformal) perturbation — both register-pinned at cap; the traceless harmonic tensor has NONZERO Ricci (10B/3 δ_ij), so it is not a vacuum field and does need stress. The rigid-interior conclusion stands, restated in those terms; the boundary-relative constant strain = the moving level set (Gemini, Grok). |
| Q4 | SWC 3 / UNSOUND 1 / SOUND 1 → SOUND folds | **SWC 4–1** | GPT D6/D7 UPHELD: the 3625 extraction was catastrophically ill-conditioned (and non-convergent in r₀: 7.7, 7.6, 75.6). RE-DONE (3629 §3): the exact horizon-regular solution h_G = r²(r − 2M) (no r⁻² tail — BH k₂^B = 0 exactly), the decaying solution by reduction of order, no cancellation: **k₂^B = +0.0277** (structural convention; the axial shell current (T-4) and the named-convention question (T-5, Grok) remain caveats). |
| Q5 | CONSISTENT 3 / UNDET 2 | **CONSISTENT** with the bridge owed (ADM M = the exterior parameter = GR-1c's M = the count at cap by GR-1c's dictionary; the shell "rest mass" 4M/3 is GR's bookkeeping of that same M, not a CPP quantity — one sentence, recorded) | — |
| Q6 | derivation SWC 4–1; standing UNDETERMINED 4 / EXCLUDED 1 | **SWC; UNDETERMINED → decided by computation (3629 §4)** | The deciding quantity every seat named — a saturation threshold — computed at Newtonian/uniform-density level: the register reaches the cap at the centre only for **M/R ≳ 0.44 — the Buchdahl bound**, far above any neutron star (0.15–0.30). **Neutron stars do not saturate; C = 0.375 is a claim about collapsed (post-Buchdahl) objects only; the NS data do not test it.** Copilot's EXCLUDED does not carry. OPEN-GR-SATURATION-THRESHOLD-1 minted for the relativistic version. |
| Q7 | FAIR 3 / OVERSTATED 2 | **FAIR** with the caveat adopted: "a target for ET/CE pending a full-waveform parameter-estimation study" replaces "within reach" | — |
| Q8 | items adopted: the vacuous check (fixed); "zero-parameter" softened to "no free parameter beyond the shell datum"; the interior argument restated; the axial shell current named; k₂^B re-extracted; χ = 0.68 labelled a surface-radius estimate; C = 0.375 conditional on saturation (now: post-Buchdahl); the mass bridge sentence; detectability wording | | |
| Q9a | PWR 3 / PROPER 2 | **PWR** | |
| Q9b | RESTATE 3 / RETRACT 1 / STANDS 1 | **RESTATE-REQUIRED** | **V2.2 enacted (3629)** |

**EK-1:** GPT, Grok, Gemini, Copilot matched. DeepSeek's key was read from a 2-decimal print — flagged (the second time the key has caught a seat; the protocol works).

