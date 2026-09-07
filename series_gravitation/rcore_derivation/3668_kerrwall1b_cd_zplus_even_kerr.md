# KERRWALL-1b CLOSED: the even-type Kerr master variable (Chandrasekhar–Detweiler Z⁺), built from a literature source and validated at a = 0 and at Kerr against Leaver, does NOT rescue the Kerr member — H-SURFACE-IMPEDANCE's (2,2) line at χ = 0.68 FAILS on Z⁺ in every frame at every s ∈ [1.5, 40], as it did on the SN local wave. The horizon seen from 8M/3 in the surface frame reflects Z⁺ at |R| = 0.77, −13°: a complex impedance in this variable too. Two records corrected: 3644's Zerilli point was evaluated at the complex QNM frequency, so 3657 (1b)'s "the variable matters already at a = 0" compared the parities at mismatched ω — at matched ω they are alike; and the even-type CD potential in Hatsuda–Kimura's parametrisation is (κ₂ > 0, b₂ = −3α²), not the literal both-plus reading of their footnote. "Fails at Kerr" may now be written, qualified: on both realizations tested (SN local wave; CD Z⁺).

**Patch 3668, Session 165, 7 Sep 2026.** Verify `code/3668_kerrwall1b_cd_zplus_even_kerr_verify.py` (14/14; run from the repo root — exec's 3359's angular CF/tortoise and 3358's Leaver radial CF; ~6 min). Reasoning `reasoning/3668.md`. No paper touched at this patch (GR-2 restatement follows as 3669). Ledger `3641_triangulation_ledger.md` row 7 and §5 updated. Hypothesis count unchanged: 1 calibration / 4 tests / 2 non-exclusions / 1 failure — the one failure is now closed on both Kerr realizations.

## §1 The literature object, and what it was checked against
The transformation was **not built from memory** (3657 §5's condition). Source: Hatsuda & Kimura, arXiv:2006.15496 (Phys. Rev. D 102, 044032), eqs. (12)–(17), citing Chandrasekhar & Detweiler, Proc. R. Soc. A 350, 165 (1976) and Detweiler, Proc. R. Soc. A 352, 381 (1977):

`X'' + (ω² − V_CD) X = 0`, `V_CD = ω² + 𝒱`, with `𝒱 = (−K² + Δλ)/(r²+a²)² + 2Δ(r³M + a⁴)/(r²(r²+a²)³) + 3a²Δ²/(r²+a²)⁴ − 4λρ²Δ[−2λρ²(r²−a²) + 2r(rM − a²)(4λr + 6M + κ₂)] / [r²(r²+a²)²(2λr² + (6M+κ₂)r − 2λα²)²]`, `α² = a² + am/σ`, `σ = −ω`, `ρ² = r² + α²`, `κ₂ = ±√(36M² − 2λ(α²(5λ+6) − 12a²) + 2b₂λ(λ+2))`, `b₂ = ±3α²`. Their λ is 3359's `lam` (A_{−2,ℓm}(aω) + a²ω² − 2amω; their footnote 8); same ω and boundary conventions as the SN instrument (their App. A). The potential is in closed form — no numerical derivative, unlike SN's U — and the CD variable is already Schrödinger-form, so a wall law applies to it directly with no dictionary term.

Four sign choices exist. **Validation before any Kerr number (BLOCKING, discharged):**
- **T1** a = 0: `𝒱 + ω² = V_Zerilli` pointwise for κ₂ > 0 (ℓ = 2 and ℓ = 3) and `= V_Regge–Wheeler` for κ₂ < 0, to 1e−16 (b₂ = 0 at a = 0, so κ₂'s sign alone selects the parity).
- **T2** a = 0: the horizon-equivalent poles at 8M/3 on Z⁺ and Z⁻ both equal Leaver's Schwarzschild ℓ = 2 QNM to 2e−5 and each other to 3e−6 — Chandrasekhar's parity map (the two potentials are isospectral).
- **T3** Kerr χ = 0.68, (2,2): with b₂ = −3α², both κ₂ signs give horizon-equivalent poles equal to Leaver's radial-CF QNM 0.52398 − 0.08151i (3358's instrument) to **2.8e−5 (Z⁺) and 5.8e−5 (Z⁻)**. With b₂ = +3α² the poles miss by 3.6e−3 and 4.2e−2 and do not converge with the horizon start: those combinations are not isospectral with Teukolsky and are excluded. **The even-type Kerr variable is Z⁺ := (κ₂ > 0, b₂ = −3α²)** — Hatsuda–Kimura's footnote 7 ("the plus signs give Zerilli") read literally as both-plus is not the isospectral choice; numerics, not the footnote, fixed it. (A wrong sign on am/σ, a wrong κ₂ or a wrong term would have failed T3; this is the test 3359 §1's recall risk asks for.)
- **T4** a = 0: the Z⁺ horizon law at 8M/3 at the complex QNM frequency is +0.0086 − 0.1155i = 3644's Zerilli point (+0.008 − 0.116i, from a 1e−4 horizon start) to 8e−4.

The CD instrument is tighter than the SN one at Kerr (3619/3657's SN horizon pole was 0.04% / 0.63% from Leaver; here 3e−5), because its potential is closed-form. Numerical caution recorded: at complex ω the outgoing branch grows outward from the horizon, so the horizon start must be r₊ + 1e−6 (1e−3 leaves 0.2–0.4% in the poles). Real-ω laws are insensitive to the start.

## §2 RECORD CORRECTION — 3644's Zerilli point is a complex-ω number; 3657 (1b) compared the parities at mismatched ω
3644's `beta_horizon(wGR)` was evaluated at the **complex** QNM frequency: that is where +0.008 − 0.116i lives, and where the pin s = Re ω/|Im β| = 3.218 was defined (re-evaluated with the converged start: 3.235; the pin stays frozen at 3.218 — rule 1, not refit). 3657 §3 and test (1b) quoted Regge–Wheeler **at real ω** (+0.105 − 0.206i) against that complex-ω Zerilli value and concluded "the near-pure-imaginary horizon law is a Zerilli feature at real ω — the variable matters already at a = 0". At matched frequency:

| a = 0, 8M/3, ℓ = 2 | Z⁺ (Zerilli) | Z⁻ (Regge–Wheeler) |
|---|---|---|
| at the complex pole | +0.0086 − 0.1155i | −0.0020 − 0.1487i |
| at real ω_QNM | +0.1161 − 0.1848i | +0.1051 − 0.2061i |

**The two parities are alike:** both near-imaginary at the pole (|Re| < 0.01), both real-heavy at real ω (Re ≈ +0.11). The contrast was an ω mismatch, not a parity property. Consequences: (i) 3657 (1b) and its sentence in the 164 handover ("the near-pure-imaginary horizon is an even-variable property") are withdrawn; (ii) 3657 §5's premise that "the hypothesis lives naturally on the even variable" had no a = 0 support — which is consistent with the a = 0 group being parity-robust (3657 §3, unchanged) and with the outcome below; (iii) the CONV-042 receiver's Q5 wording that the hypothesis "was pinned on the even Zerilli variable" stands as a fact about the pin, not as a reason to expect Z⁺ to differ. Dated correction line added to 3657's note.

## §3 The Kerr horizon in the even variable
At χ = 0.68, r_w = 2.7344 M, (2,2), real ω = 0.5240 (Leaver's Re ω): `β_hor,Z⁺ = +0.0447 − 0.0533i` (Z⁻: +0.170 − 0.209i; SN Y: +0.057 − 0.071i; SN X: +0.068 − 0.155i). The horizon seen from the wall as a reflector of Z⁺, `R = (β + ik)/(ik − β)`, k = ω − mΩ:

| frame | \|R\| on Z⁺ | phase | (SN Y, 3657) |
|---|---|---|---|
| Ω_w = 0.0601 (surface's own) | **0.769** | **−12.9°** | 0.707, −16.7° |
| Ω_H = 0.1962 | 0.474 | −43.3° | 0.397, −59.1° |
| 0 | 0.817 | −9.9° | 0.764, −12.7° |

**In the even variable too the Kerr horizon is a complex impedance from the wall** — more reflective than the a = 0 step (0.77 vs 0.53) with a phase of order −13°. The requirement of 3657 §4 is basis-robust in kind (a lossy spring) and basis-dependent in number (CONV-042 GPT 5): |R| ≈ 0.7–0.8 at −(13–17)° across the two realizations in the surface frame. The re-read pin s_Kerr = k/|Im β_Z⁺| = 7.6 (Ω_w), 2.5 (Ω_H), 9.8 (0) — not universal, as on SN (5.7 / 1.9 / 7.4).

## §4 THE TEST — the Kerr member FAILS on Z⁺
`β_Z⁺ = −i(ω − mΩ)/s`, s = 3.218 unchanged, applied directly (Z⁺ is Schrödinger-form); scored against the machinery's own Z⁺ horizon pole (H; = Leaver to 3e−5, so vs K is the same) in the GW250114 box (δf ± 2.4%, δτ (−15, +17)%; 3659) and, for continuity with 3657, the GW150914 box.

| frame | pole on Z⁺ | δf / δτ vs H | (3657 on SN X) |
|---|---|---|---|
| **Ω_w** | 0.3812 − 0.1208i | **−27.2% / −32.5% out** (out of both boxes) | −18.9% / −47.4% |
| Ω_H | 0.4050 − 0.1018i | −22.7% / −19.9% out | −14.3% / −38.2% |
| 0 | 0.3729 − 0.1292i | −28.8% / −36.9% out | −20.5% / −50.5% |

**s-scan, s ∈ {1.5, 2, 3.22, 5, 8, 15, 40}, both frames: nothing enters the box** (Ω_w: δf −33% → −22%, δτ −38% → −27%; Ω_H: δf −24% → −21%, δτ −11% → −26%). The even variable relocates the miss (frequency worse, −27% vs −19%; damping better, −32% vs −47%) and does not close it. **The failure is the form on this realization too: a real impedance step is not what the Kerr ringdown asks of the wall in any master variable tested.** 3657 §5's honest prior ("the last door, not a likely one") is confirmed; with §2, it was never a door with a = 0 support.

## §5 Standing
- **OPEN-GR-KERRWALL-1b: CLOSED** (both outcomes were to close it; this is the failing one). The CD Z⁺ instrument is validated and reusable (a = 0 to 2e−5; Kerr to 3e−5 against Leaver; closed-form potential; no dictionary term) — a candidate methods-catalogue entry (the lane's third Kerr master-variable instrument after SN and the complex ray), to be registered at the next Step-E audit.
- **H-SURFACE-IMPEDANCE count unchanged: 1 calibration / 4 tests / 2 non-exclusions / 1 failure.** The failure's record now reads **"fails at Kerr on both realizations tested — the SN local wave (3657) and the even-type Chandrasekhar–Detweiler Z⁺ (3668) — every frame, every s ∈ [1.5, 40]"**. "Fails at Kerr" may be written with that qualifier; "fails on every Kerr realization" may not (two tested).
- **The Kerr requirement (3657 §4) re-stated across realizations:** the horizon from 8M/3 in the surface frame is a complex reflector, |R| ≈ 0.7–0.8 at −(13–17)°, basis-dependent in number; the a = 0 horizon is a real step 0.53 at −3°. **OPEN-GR-SURFACE-IMPEDANCE-1's target is unchanged in kind and now bracketed in number**: the a = 0 real step AND a Kerr complex reflection in that range; a law that produces only a real number at Kerr fails on every realization tested.
- Rule 6: a failed member is recorded; the hypothesis is not amended, not carried to Kerr, s UNEXPLAINED. CANDIDATE-S-AREA (3655) remains a candidate for the a = 0 number only.
- Records: 3657 (1b) withdrawn (§2); the 164 handover's "the near-pure-imaginary horizon is an even-variable property" withdrawn; Hatsuda–Kimura's footnote-7 pairing read as both-plus is not the isospectral even-type potential (§1). GR-2 V2.4's "until it is run the failure is the SN realization's, not the hypothesis's at Kerr outright" is superseded → V2.5 restatement (3669).
- Next on the lane (ledger §5): attempt 4 on OPEN-GR-SURFACE-IMPEDANCE-1 with the two-datum target (the a = 0 real step; the Kerr complex reflection, now bracketed across two realizations); then the complex ray on SN for the (2,+1) comparator (3359 "NOT LOCATED"), where the CD Z⁺ instrument with closed-form potential is the better carrier for the complex-ray integration than SN's numerically-differentiated U.
