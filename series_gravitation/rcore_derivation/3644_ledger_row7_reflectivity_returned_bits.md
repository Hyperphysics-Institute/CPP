# Ledger row 7 FAILS FOR THE EXTENSION AS WRITTEN [PCD-EXT]: the returned-bit fraction (D−K)/D = 1 − cap/v is ZERO at the surface, so the budget law makes the surface transparent — and every transparent-surface reading of the wave (lossless transmit, absorb at the surface, absorb at any depth) fails the ringdown: frequencies can be matched, but the damping is ~30% too fast at a = 0 and at Kerr. The black hole itself, seen from 8M/3, is a partial COHERENT reflector (|R| = 0.55 at the QNM frequency, Re β ≈ 0). That is the founder's surface stiffness (R-CAP-SPRING; 3639 §4 "χ < 1 strictly"), which the budget law dropped. Named calibration: ONE number, the interior wave impedance s = 3.22 × the exterior's, pinned by the a = 0 ℓ = 2 horizon point; TEST PASSED without refit at ℓ = 3 (−1.4% / −1.3%); Kerr test owed to KERRWALL-1. Consequence for PRED-O-39: no reading gives both a black-hole ringdown and a coherent 0.95 ms echo at 0.44 — the echo amplitude is (1 − R²) × 0.44 × f_core ≤ 0.3, and 0 if the core dissipates. Founder's pin required (3641 §2 rule 5)

**Patch 3644, Session 163, 6 Sep 2026.** Verify `code/3644_ledger_row7_reflectivity_returned_bits_verify.py` (16/16; run from the repo root — it exec's 3359's SN machinery as 3619 does). Reasoning `reasoning/3644.md`. No paper touched. CONV-042 held. Ledger `3641_triangulation_ledger.md` row 7 updated; row 5 annotated.

## §1 What the law fixes and what it does not
The returned fraction is fixed: `(D − K)/D = 1 − cap/v(r̄)` — **0 at the surface** (v = cap), 1/3 at the centre. Nothing is returned promptly by the surface. What the law does not fix is how returned bits act on a *wave*. Taken literally per Moment, the cumulative return over a depth δ is `(δ/M)²(M/l_P)/3`, which reaches unity at `δ = √(3 l_P/M) M ≈ 2×10⁻¹⁶ m` (62 M☉): a *skin*, so a per-Moment reading is a surface wall (mirror if coherent, absorber if not), not an interior process. The remaining reading is that the wave rides the register (3643's transmit on the graded metric) and loses coherence, if at all, at depth.

## §2 The readings as wall laws, priced against the pinned empiric (the ringdown; GW150914's box δf ∈ (−4.8, +6.3)%, δτ ∈ (−22, +24.4)%, 3616)
Machinery validated first: the horizon-equivalent wall at 8M/3 (ingoing at the horizon, integrated out) reproduces the Schwarzschild ℓ = 2 QNM `0.37367 − 0.08896 i` to 0.04%/0.04%, and ℓ = 3 to 0.02%.

| reading | wall at 8M/3 | a = 0, ℓ = 2 pole | δf | δτ | box |
|---|---|---|---|---|---|
| A2 mirror (Dirichlet / Neumann) | hard | 0.3855 − 0.204 i / 0.3905 − 0.060 i | +3 / +5% | −57 / +49% | out |
| A1 lossless graded transmit (3643) | real β(ω) | 0.4586 − 0.1315 i | **+23%** | −32% | out |
| B absorber at the surface | −iω | 0.3430 − 0.1326 i | −8% | −33% | out |
| C absorber at depth r̄_abs (family 1.45 → 0.3) | interior ingoing | best 0.3789 − 0.1295 i at r̄_abs = 1.2 | +1.4% | **−31%** | out (all) |
| horizon itself (reference) | β_hor(ω) | 0.3735 − 0.0890 i | 0 | 0 | — |
| **D stiffness s = 3.22 (pinned)** | −iω/s | **0.3656 − 0.0848 i** | −2.2% | +4.9% | **in** |

At Kerr (a = 0.68, 2.734 M, prograde (2,2), 3619's SN solver; the interior laws carried over from the a = 0 profile as estimates): B `0.4515 − 0.096 i` (−14.5% / −15%), A1 `0.611 − 0.053 i` (+16% / +55%), C `0.483 − 0.193 i` (−8.5% / −58%) — all out.

**The pattern:** every transparent reading can be tuned to the *frequency* (C at 20% depth) but none to the *damping*: the mode decays ~30% too fast. The reason is in the horizon-equivalent law itself: at ω_QNM, `β_hor(8M/3) = +0.008 − 0.116 i`, i.e. an admittance `|Im β|/ω = 0.31` — **the black hole, seen from 8M/3, reflects |R| = 0.55 of the amplitude coherently and absorbs the rest.** A C¹ surface with continuous wave speed (admittance 1) absorbs too much. What the ringdown asks of the surface is a coherent partial reflection with `Re β ≈ 0`: an impedance *step*.

## §3 Reading D — the founder's stiffness, one number
An interior whose wave impedance is `s ×` the exterior's, locally ingoing inside: `β = −iω/s`. This is R-CAP-SPRING at the surface — "a stiffness that prevents full PSR displacement" — which 3639 §4 read as `χ < 1 strictly` and which THEO-PCD-BUDGET's `χ = cap/v → 1 at the surface` dropped.
- **Pin once (rule 1), named here:** `s = ω_QNM / |Im β_hor(ω_QNM)| = 3.218` from the a = 0 ℓ = 2 horizon point. The pinned line: `0.3656 − 0.0848 i` (−2.2% / +4.9%).
- **Test 1, no refit — PASSED:** ℓ = 3 at a = 0 with the same s: `0.5911 − 0.0939 i` vs GR `0.5994 − 0.0927 i` — **−1.4% / −1.3%**.
- **Not knife-edge:** s ∈ [2.5, 5] keeps both a = 0 lines in the box; s → 1 (transparent) and s → ∞ (mirror) leave it.
- **Test 2, Kerr — OWED (not scored):** with `β = −i(ω − mΩ_H)/s`, the (2,2) line is `0.4902 − 0.1089 i` (−7.2% / −24.7%), just outside; and *no* s puts a pure-imaginary law inside the Kerr box (probed with Ω_H, with the wall's own frame-dragging rate 0.060, and with neither). The cause is the dictionary, not the physics: on the Zerilli function a pure-imaginary β *is* the local absorber (β_hor has Re = +0.008 at real ω); on the SN function it is not — 3619's horizon-equivalent law has `Re β = +0.063, Im −0.159` at real ω, because the SN transformation mixes X and X′. A local wall law at the Kerr surface needs the SN ↔ local-wave map at the wall — **KERRWALL-1's**. (Note in passing: 3619's text says "Ω_w at the wall"; its code used Ω_H.)
- Physical content: prompt coherent reflection `|R| = (1 − 1/s)/(1 + 1/s) = 0.53` (the horizon's own 0.55); `1 − R² = 0.72` of the energy enters the core.

## §4 Consequence for PRED-O-39 (row 5 re-cut)
No reading gives both a black-hole ringdown and a coherent 0.95 ms echo at 0.44 of the ringdown. The lossless reading (A1) is the only one with f = 1, and it is 23% off in frequency. Under D (and under the horizon itself) the first echo's amplitude is `(1 − R²) × |T_barrier|² × f_core = 0.72 × 0.44 × f_core ≤ 0.32`, with `f_core` the core's coherent return — **0 if the core dissipates within a crossing (3621 §2, 3623's storage as CP vibration), which is what the ringdown's damping already prefers.** The 0.95 ms delay (3640) stands as the cavity time; the *amplitude* is bounded above at 0.3 and expected near 0. Row 5's "a detection at 0.95 ms confirms the extension" is re-cut: a detection at 0.95 ms would measure `f_core`; a null result is what the extension predicts.

## §5 Standing and what is asked
- **Row 7: FAILS for THEO-PCD-BUDGET as written** (rule 5). The failure is located: the law's χ → 1 at the surface (no stiffness), against the founder's own R-CAP-SPRING.
- **Calibration named (rule 1):** one number `s`, the interior's wave impedance relative to the exterior's, pinned by the a = 0 ℓ = 2 horizon point; one independent test already passed (ℓ = 3); one owed (Kerr, after the KERRWALL-1 dictionary). No refit anywhere.
- **The founder's action (3641 §2 rule 5 reserves this):** pin `s` — i.e. amend the working extension to THEO-PCD-BUDGET + surface stiffness — or let row 7 stand as the extension's failure. Either is a one-word ruling; the physics on both sides is computed above.
- Rows 8 (passes), 9 (stands), 3 (passes) are unaffected: the stiffness is a wave-impedance statement at the surface, not a change to the register profile, the cavity, or the neutron-star statics.
- Owed: KERRWALL-1's wall dictionary (then the Kerr test of s); the odd sector at 8M/3 with J = 32/9 (3643 §5); row 6 (Love number) proceeds after the pin ruling since the spring deflection depends on the same stiffness.
