# KERRWALL-1: the Sasaki–Nakamura ↔ local-wave dictionary at the Kerr wall is DERIVED and EXACT (Y = X/√η; β_X = β_Y + F/2) — and it does NOT rescue the Kerr member: H-SURFACE-IMPEDANCE's (2,2) line at χ = 0.68 FAILS in every frame, at every s in [1.5, 40]. The failure is the FORM, not the number: seen from 8M/3 in the surface's frame the Kerr horizon reflects the local wave with |R| = 0.71 at −17°, a COMPLEX impedance, where the hypothesis is a real one. Requirement recorded. The a = 0 group is parity-robust (ℓ = 2, 3 on Regge–Wheeler in the box, s unchanged). Hypothesis 4/5 computed members; the even-type Kerr variable (Chandrasekhar–Detweiler Z⁺) is the one untested reading — KERRWALL-1b, literature-bound

**Patch 3657, Session 164, 7 Sep 2026.** *CONV-042 (3665): dictionary SOUND 4/4; Kerr verdict restated as "fails on the SN local-wave realization; even-type Kerr variable (Z⁺) untested — OPEN-GR-KERRWALL-1b"; W's F′/2 sign corrected in §1; the Kerr "surface frame" is a chosen prescription (GPT 9); the horizon's reflection from 8M/3 is basis-, frame- and frequency-dependent, not a universal surface property (GPT 5).* *KERRWALL-1b closed (3668): §3's parity contrast and test (1b) are WITHDRAWN — 3644's Zerilli point +0.008 − 0.116i was evaluated at the COMPLEX QNM frequency, and §3 compares Regge–Wheeler at REAL ω against it; at matched ω the parities are alike (pole: Zerilli +0.0086 − 0.1155i, RW −0.0020 − 0.1487i; real ω: +0.116 − 0.185i, +0.105 − 0.206i). §5's "the hypothesis lives naturally on the even variable" had no a = 0 support. The even-type Kerr variable, built from the literature, FAILS the Kerr member too (3668). §3's parity-robustness of the a = 0 group and §4's Kerr numbers stand.* Verify `code/3657_kerrwall1_sn_local_wave_dictionary_verify.py` (13/13; run from the repo root — exec's 3359's SN machinery as 3619/3644 do; ~10 min). Reasoning `reasoning/3657.md`. No paper touched. CONV-042 held. Ledger `3641_triangulation_ledger.md` row 7 and §5 updated.

## §1 The dictionary
The SN equation is `X'' − F X' − U X = 0` (′ = d/dr*). The first-derivative term is what 3644 §3 pointed at: it makes X not locally plane-wave at the wall, so "pure-imaginary β on X" is not "locally ingoing". The term is removable exactly. With `F = η′Δ/(η(r²+a²))` and `dr*/dr = (r²+a²)/Δ`, **`F dr* = d ln η`** — verified pointwise at Kerr (2,2) to 8e−11 with 3359's own η — so
- `Y = X/√η` obeys `Y'' = W Y`, `W = U + F²/4 − F′/2` *(sign corrected at 3665 on CONV-042/GPT item 8: substitution gives −F′/2, not +F′/2; the transport β_X = β_Y + F/2 and every number in this note are unaffected)* (Schrödinger form: Y is the local wave of the SN family);
- any wall law transports as **`β_X = β_Y + F(r_w)/2`**;
- at a = 0, η = c₀ = const, F = 0, Y = X = Regge–Wheeler: the dictionary is the identity.

This is the dictionary the SN family admits. It is not the Zerilli-type (even) variable; that is a different family (Chandrasekhar–Detweiler's Z⁺ in Kerr), see §5.

## §2 What the dictionary term is at the wall — against the expectation
At χ = 0.68, r_w = 2.734 M, (2,2), real ω = 0.5242 (the machinery's own horizon-equivalent pole, = 3619's; literature ≈ 0.528 − 0.082i, −0.7%/+1.3%):

| quantity | value (1/M) |
|---|---|
| β_hor on X (3644: "+0.063") | +0.0681 − 0.1546 i |
| **F(r_w)/2** | **+0.0108 − 0.0837 i** |
| β_hor on Y = β_X − F/2 | +0.0574 − 0.0709 i |

**The dictionary term is imaginary-dominated.** Its real part is a sixth of the horizon law's; the +0.06 real part 3644 attributed to "the SN transformation mixing X and X′" is *in the local wave itself*, not in the gauge factor. The dictionary moves the Kerr horizon point only slightly toward the imaginary axis (|Re| 0.068 → 0.057) and halves its absorption.

## §3 The a = 0 side: the variable matters, and the group is parity-robust
The hypothesis was pinned on Zerilli (even). The a = 0 member of the SN family is Regge–Wheeler (odd). On RW at 8M/3:
- horizon law at real ω_QNM: **+0.1052 − 0.2060 i** (Zerilli: +0.008 − 0.116 i) — the near-pure-imaginary horizon law is a Zerilli feature at real ω. At the complex pole RW gives −0.0002 − 0.1471 i. (Chandrasekhar's map between the parities is a first-order differential relation; a local law on one variable is non-local on the other. This is exactly the two-conventions caution of the 163 handover, in the dynamical sector.)
- **H-SURFACE-IMPEDANCE on RW, s = 3.218 unchanged: ℓ = 2 → 0.3707 − 0.0794 i (−0.8% / +12.0%) IN box; ℓ = 3 → 0.5924 − 0.0923 i (−1.2% / +0.5%) IN box.** The a = 0 group holds on the odd master function with the even-pinned number; damping residuals larger at ℓ = 2 (+12% vs +4.9%), smaller at ℓ = 3. Recorded as parity-robustness of the four a = 0 members, not as new members.

## §4 THE KERR TEST — member 5 FAILS
`β_X = F/2 − i(ω − mΩ)/s`, s = 3.218 unchanged, scored against the machinery's horizon-equivalent pole (H; 0.5242 − 0.0810 i) and the literature line (K); GW150914 box (−4.8, +6.3)% / (−22, +24.4)%.

| frame Ω | pole | vs H: δf / δτ | 3644 form (no F/2) |
|---|---|---|---|
| **Ω_w = 0.0601 (surface's own frame-dragging; the a = 0 reading carried unchanged)** | 0.4251 − 0.1539 i | **−18.9% / −47.4% out** | −12.6% / −39.7% out |
| Ω_H = 0.1962 | 0.4493 − 0.1311 i | −14.3% / −38.2% out | −6.5% / −25.6% out |
| 0 | 0.4169 − 0.1637 i | −20.5% / −50.5% out | −14.8% / −44.2% out |

The dictionary makes it *worse*: the −0.084 i in F/2 adds absorption. **s-scan, s ∈ {1.5, 2, 3.22, 5, 8, 15, 40}, both frames: nothing enters the box** (Ω_w: δτ from −52% to −43%; Ω_H: −33% to −42%). The failure is not the number.

**The Kerr requirement (recorded like row 7's).** The horizon seen from the wall as a reflector of the local wave, `R = (β + ik)/(ik − β)`, k = ω − mΩ:

| | \|R\| | phase |
|---|---|---|
| a = 0, Zerilli (3644's point) | 0.526 | −2.7° |
| the hypothesis | 0.526 | 0 |
| **Kerr, Y, Ω_w** | **0.707** | **−16.7°** |
| Kerr, Y, Ω_H | 0.397 | −59.1° |
| Kerr, Y, Ω = 0 | 0.764 | −12.7° |

At a = 0 the horizon is, to 3°, a real impedance step — which is why one real number described four members. At Kerr it is not: in the surface's frame it reflects more (0.71) with a phase of order −17° — a lossy spring, a complex impedance. The re-read pin `s_Kerr = k/|Im β_Y,hor|` = 5.70 (Ω_w), 1.86 (Ω_H), 7.39 (Ω = 0): the admittance reading does not carry a universal number across spin. **What any Kerr member of a surface law must reproduce: |R| ≈ 0.7 at ≈ −17° in the surface frame at χ = 0.68.**

## §5 Standing
- **H-SURFACE-IMPEDANCE: 4/5 computed members** (ℓ = 2, 3, 4 at a = 0; static Λ = +3.0; **Kerr (2,2) FAILS** on the SN local-wave variable, all frames, all s). Rule 6: a failed member is recorded, the hypothesis is not amended. Not carried to Kerr. The a = 0 members stand and are parity-robust (§3).
- **The one untested reading:** the hypothesis lives naturally on the even variable (its horizon law is real-impedance to 3° at a = 0; the odd one is not at real ω). The even-type Kerr master function is Chandrasekhar–Detweiler's Z⁺ (complex, ω-dependent potential). It was not built here: the transformation is a literature object with the recall risk 3359 §1 names, and must be validated at a = 0 against Chandrasekhar's parity map before any Kerr number. Registered **KERRWALL-1b** (owed, literature-bound). Honest prior from §3: the a = 0 group being parity-robust gives little reason to expect the even variable to flip the Kerr verdict; it is the last door, not a likely one.
- **CANDIDATE-S-AREA (3655)** is not discriminated by this: the discriminant was the damping spread at Kerr, and no s-value law reaches the Kerr box. The candidate stands as a candidate for the a = 0 number only.
- **GW250114's ringdown as the discriminating box** (163 handover item 2) is moot for this hypothesis: there is no Kerr member to discriminate. It remains the box for whatever law meets §4's requirement.
- **OPEN-GR-SURFACE-IMPEDANCE-1** (derive the ~3× impedance from the cycle) is now sharpened by a second datum: the target is not one real number but the a = 0 real step **and** the Kerr complex reflection (0.71, −17°) — a derivation that gives only the first is incomplete.
- PRED-O-39's amplitude re-cut (3644) is unchanged; PRED-O-40 unchanged.
- Superseded: 3644 §3's attribution of the Kerr real part to "the SN transformation mixing X and X′" (it is in the local wave; §2). 3644's "no s puts a pure-imaginary law inside the Kerr box" is confirmed and extended to the dictionaried form.
- Next on the lane (ledger §5 re-cut): the overtone (Leaver, item 3), the odd-sector re-run at 8M/3 with J = 32/9 (item 4), the closure-interior stability record (item 5), then the V2.3 write-up with the hypothesis at 4/5 and the Kerr requirement, and CONV-042 re-cut as that round. KERRWALL-1b when the literature is in hand.
