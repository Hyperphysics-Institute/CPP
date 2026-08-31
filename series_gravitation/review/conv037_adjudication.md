# CONV-037 adjudication — FINAL v1.0 (Patch 3361)

**Round:** the Teukolsky ladder (3353–3359) and the flagship frequency
move to 191 Hz. Receiver `reviews-CONV-037.md`, 5/5 registered (Seat 4
provisional on identity — see §5). Two panel-named gaps were **computed
before adjudicating** (`code/3361_conv037_gaps_verify.py`: G1 1/1,
G2–G3 2/2), so the verdict rests on what is now known.

**Headline: AMENDMENTS-CLEAR 3–2, no binding rule fires, and every
seat's revision list is adopted — including the BLOCK dissent's, which
caught the round's one genuine error in the proposed text.**

---

## §1 Tally

| Q | Verdict | Tally | Adjudication |
|---|---|---|---|
| Q1 ladder | **SOUND-WITH-GAPS** | 4–1 (DeepSeek SOUND) | The gap all four named — no Kerr-interior SN test — is now CLOSED by G1 (§3). |
| Q2 SN + BC | **VALID-WITH-CAVEATS** | 5–0 | Unanimous, and unanimous on *which* caveat: X = 0 is assumed, not derived. Adopted into the text. |
| Q3(i)(ii) | **CONFIRMED-WITH-CAVEATS** | 5–0 | The caveats (one spin; assumed BC) are the same two; one is now a band (G2). |
| Q3(iii) no comb at ℓ=2 | **CONFIRMED** | 4–1 (GPT NOT-CONFIRMED) | GPT is right at *exact* grade: a local root search cannot prove absence. But the census (3334/3354) established N_trapped = 0 at ℓ = 2 by phase volume at eikonal-WKB grade. Adopted as a grade split (§2 item 5). |
| Q4 corrections | **ADEQUATE** | 5–0 | Unanimous. |
| Q5 method limit | **CORRECTLY-SCOPED** | 4–1 (GPT UNDER-SCOPED) | GPT's point that the 0.12–0.3 grey zone is unmapped is correct and Grok/Copilot echo it; the reported roots (0.065, 0.088) sit in the demonstrated-success region. Adopted as a wording fix ("demonstrated at", not "validated for") plus an owed mapping study. |
| **Q6 amendment text** | **FAITHFUL-AT-GRADE** | 4–1 (GPT OVERCLAIMS) | **The block rule does not fire.** But GPT's Q6 defect 5 is simply correct: the text assigned "Q ≲ 1.5" to a mode the record marks NOT LOCATED. That is an error, not a grading choice, and it is fixed. |
| Q7 scope audit | **ITEMS-FOUND** | 4–1 | Seventeen items across four seats, heavily overlapping; consolidated to nine in §2. All adopted (frozen rule). |
| Q8a | **PROPER-WITH-REVISIONS** | 4–1 | |
| Q8b | **AMENDMENTS-CLEAR** | 3 CLEAR / 1 RESTATE / 1 BLOCK | Majority governs; the revisions fold at enactment (CONV-034/035 precedent, all strictly weaker) — with one panel-*requested* addition (§3). |

## §2 Adopted revisions — the consolidated list (17 seat-items → 9)

1. **X = 0 declared an assumption** (GPT, Grok, Gemini, Copilot): "Dirichlet on the Sasaki–Nakamura variable X, the Regge–Wheeler analogue of the clamped-register node — an *assumed* Kerr generalisation, not a substrate derivation; the spectrum is conditional on it." New open item: derive the Kerr wall condition from the rotating clamped register.
2. **(2,+1): NOT LOCATED, full stop** (GPT). The proposed "too broad (Q ≲ 1.5)" is struck; "the present instrument cannot determine its frequency or Q."
3. **"Sharpest" → "the sharper of the two located retrograde modes"** (GPT, Grok, Copilot); "dominant" **conditioned** on the inherited 3349/3350 excitation model — this ladder computed no excitation amplitudes.
4. **"Exact Kerr wall resonance" → "exact numerical solution of the SN/X-Dirichlet model at the derived surface"** (GPT).
5. **"No comb at ℓ = 2" split by grade** (GPT Q3(iii)): absent at census grade (N_trapped = 0, 3334/3354); at exact grade, one broad root located and no comb *demonstrated*.
6. **Method limit re-worded** (GPT, Grok, Copilot): "demonstrated at |Im ω| = 0.065–0.117; failed at 0.25–0.30; the interval between is unmapped." Owed: a stability-vs-Im ω mapping study.
7. **RCORE-3 registry re-labelled per item by grade** (GPT, Grok): Zel'dovich (d) = corollary at eikonal-WKB grade; excitation (e) = derived for ℓ ≥ 9, source-side for 7–8 with the counter-rotation factor bounded, hierarchy inherited; nothing described as "discharged" without its grade.
8. **3359 script K3 text fixed** (GPT item 6): it still says the scalar proxy was faithful for "ordering" — struck.
9. **"χ ≈ 0.68" → the computed band** (Gemini Q7(1); Copilot; Grok D3): see §3.

## §3 The two gaps, computed before ruling

**G1 — Kerr-interior SN benchmark (T-2; four seats).** Grok's form,
implemented: the SN direct-integration stack, asked for the frequency
at which the horizon-side solution is purely ingoing, **locates the
tabulated Kerr (2,2) QNM at a/M = 0.7 to |Δω| = 2.2e−3**
(0.53481 − 0.08065i vs 0.53260 − 0.08079i); |A_out/A_in| falls from
4.5e−2 at the table value to 1.3e−4 at the located root. GPT's stated
blind spot — a term ∝ a vanishing at a = 0 and at large r — is closed.
Q1's "gap" is now a validated rung.

**G2/G3 — the spin band (T-3; three seats).** At χ = 0.62 / 0.68 /
0.74 (GW150914's χ_f window), each root individually r₀-independent and
sharp: **(2,−2): 188.5–194.1 Hz; (3,−3): 284.5–292.5 Hz.** The spin
half-range is **±1.5%**, against the mass band's ±6.5% — the flagship
uncertainty is mass-dominated at exact grade, as it was at eikonal
grade (3329). This is a panel-*requested* addition, so its entry into
the amendment is not a worker-initiated strengthening.

## §4 THE REVISED AMENDMENT (ratification requested)

> **PRED-O-39, refined at gravitational grade (Patches 3359, 3361;
> CONV-037):** for a GW150914-class remnant (M = 62 ± 4 M_⊙,
> χ_f ∈ [0.62, 0.74]), the retrograde-keyed **(2,−2) line lies at
> 188–194 Hz across the spin window (191.2 Hz at χ = 0.68), Q ≈ 2.1** —
> a single broad top-of-barrier feature. Exact mass scaling adds
> ±6.5%; spin contributes ±1.5%. **(3,−3) lies at 284–292 Hz, Q ≈ 4.2**,
> the sharper of the two located retrograde modes. These are exact
> numerical solutions of the Sasaki–Nakamura / X-Dirichlet wall model
> at the derived surface; **the wall condition X = 0 is the
> Regge–Wheeler analogue of the clamped-register node, assumed rather
> than derived for a rotating surface, and the spectrum is conditional
> on it.** No trapped comb at ℓ = 2 at census grade (N_trapped = 0,
> 3334/3354); at exact grade one broad root is located and no comb is
> demonstrated. "Dominant" for (2,−2) is conditional on the inherited
> source-side excitation model (3349/3350); this ladder computed no
> amplitudes. The prograde comparator (2,+1) is **not located** — the
> present instrument cannot determine its frequency or Q (Q ≲ 1.5 modes
> exceed its demonstrated range) — so the retrograde-keyed *ordering*
> discriminator stands at eikonal-WKB grade only. Early transients at
> the eikonal delay 2.624 ms are unchanged. Supersedes the
> orientation-scale eikonal tops (211/233/260/294 Hz, Patch 3337),
> retained as superseded. Conditional on A1–A3 (OPEN-GR-RCORE-4).

**Enactment on the founder's word:** predictions.md row + amendment
note (anti-erasure); GR-2 V1.5 → V1.6 (`rem:rcore3` gains the
gravitational spectrum and the assumption clause; provenance ledger
extended to 3359/3361; the 3348 checker's ledger extended); RCORE-3
registry re-labelled per §2 item 7; 3359 K3 text fixed. Deposit
posture unchanged (fail-closed).

## §5 Seat ledger

- **GPT:** own-ran 3359; the round's dissent (BLOCK) and the only
  seat to catch the genuine text error (Q ≲ 1.5 on an unlocated mode).
  **Fifth consecutive round in which its grade objections are adopted.**
  Where it ruled beyond the majority (Q3(iii), Q5, Q8b) the adjudication
  took its substance as wording and owed work rather than as a block.
- **Grok:** INDEPENDENT-HARNESS on T1 and the conversions; supplied the
  Kerr-interior check that G1 then implemented. Honest about runtime.
- **Gemini (paste 3):** identity holds (5th round); RESTATE for a
  disclosure reason (the assumption clause) — adopted.
- **Copilot slot (paste 4): IDENTITY ANOMALY — self-labels "Gemini."**
  Counted provisionally on the founder's slot label; **founder
  confirmation requested.** If it was not Copilot: dropped as a
  duplicate, round stands 4/5, no majority changes.
- **DeepSeek:** identity holds (4th round); the permissive outlier this
  time (Q1 SOUND, Q7 NONE-FOUND) — weighted accordingly.

## CHANGELOG
- v1.0 (Patch 3361): FINAL at 5/5 (Seat 4 provisional). CLEAR 3–2;
  nine consolidated revisions adopted; two gaps computed pre-ruling;
  revised amendment presented for ratification.
