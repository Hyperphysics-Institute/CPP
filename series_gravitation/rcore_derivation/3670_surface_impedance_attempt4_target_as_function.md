# OPEN-GR-SURFACE-IMPEDANCE-1 attempt 4, step 2: the two-datum target is not two numbers — and, stated where the pole is decided, it has no passive-surface solution. The "a = 0 real step |R| = 0.53 at −3°" (row 7, 3657 §4) was β at the complex pole read with k real (RECORD CORRECTION, extending 3668 §2): at real ω the a = 0 horizon from 8M/3 reflects Z⁺ at 0.39, −43°; at Kerr the real-ω reading is 0.77, −13°; across spin |R| runs 0.39 → 0.80 and the phase −43° → +99°. At the complex poles — the data that decide — the hypothesis's law sits 0.04–0.06 from the horizon's admittance at all three a = 0 fundamentals (that is the group's descriptiveness; s is not ℓ-flat, 3.24 → 3.90), while at Kerr from χ ≈ 0.4 the horizon's admittance at the pole has Im β > 0 in the even variable — the opposite sign to any absorbing law −ik/s. A real step, a delayed surface (a one-Moment delay is 10⁻³⁹ degrees), and a co-rotating step all fail; the only zero-parameter structure meeting both pole data is GR's excised region itself. The open problem is RE-CUT: its target is the complex admittance function β_hor(ω, ℓ, m, χ) at the poles, not a constant; s = 3.22 is the ℓ = 2, a = 0 pole value of that GR function. H-SURFACE-IMPEDANCE: count unchanged 1/4/2/1, its number now identified as a GR pole value; CANDIDATE-S-AREA loses its object.

**Patch 3670, Session 165, 7 Sep 2026.** Verify `code/3670_surface_impedance_attempt4_target_as_function_verify.py` (13/13; exec's 3668's CD Z⁺ instrument; ~5 min). Reasoning `reasoning/3670.md`. Paper: GR-2 → V2.6 at 3671 (the "= the horizon's own from that radius" clause and the V2.5 "requirement" sentences restated). Ledger `3641_triangulation_ledger.md` row 7 and §5 updated. No panel (a re-cut of an open problem and a record correction are neither a win nor a stuck point).

## §1 Why this step before a sixth derivation
Attempts 1, 2a, 2b, 3, 3b each tried to produce one number from a surface mechanism; 3655 named a constant candidate. 3668 added a second datum with a phase. The two "data" had never been checked to be the same object. They were not.

## §2 RECORD CORRECTION — the "a = 0 real step" was a mixed-frequency number
3657 §4's row "a = 0, Zerilli (3644's point): |R| = 0.526 at −2.7°" was `refl(bhZ0, Re ω)` with `bhZ0 = 0.008 − 0.116i` — β at the **complex** pole (3668 §2) — read with k **real**. The hypothesis's own reflectivity (s − 1)/(s + 1) = 0.526 at 0° was then "= the horizon's own from that radius" by construction of the pin, not by a measurement. Evaluated consistently:

| a = 0, 8M/3, Z⁺ | at real Re ω_QNM: β_hor, \|R\|, phase | at the complex pole: β_hor, Re ω/\|Im β\| |
|---|---|---|
| ℓ = 2 | +0.116 − 0.185i, **0.39, −43°** | +0.0086 − 0.1155i, 3.235 |
| ℓ = 3 | +0.148 − 0.251i, 0.44, −33° | +0.0086 − 0.1649i, 3.636 |
| ℓ = 4 | +0.172 − 0.305i, 0.47, −28° | +0.0093 − 0.2076i, 3.897 |

**There is no real step at a = 0.** At real ω the horizon from 8M/3 is a complex reflector at −43° to −28° with ratio ω/|Im β| = 2.0–2.7; at the poles Re β is +0.009 at all ℓ and the ratio rises 3.24 → 3.90. Consequences: row 7's "the ringdown requires a coherent partial reflection |R| ≈ 0.53 at 8M/3 = the horizon's own from that radius" (3644; in GR-2 V2.3–V2.5 and PRED-O-39) is corrected — 0.53 is the *step's* reflectivity; the horizon's own real-frequency reflection from that radius is 0.39 at −43°; the two share the ℓ = 2 pole to a few % because the pole is set at the complex frequency, where the horizon's admittance (+0.009 − 0.116i) and the step's (−0.028 − 0.116i) differ by 0.036. 3668 §3/§5's "a = 0 real step 0.53 at −3°" inherits the correction (dated line added there); 3657's dated line extended.

## §3 Why the a = 0 group was descriptive
At the poles the hypothesis's law −iω/3.218 sits **0.036, 0.043, 0.058** from the horizon's admittance at ℓ = 2, 3, 4 — the ℓ = 2 calibration residual (−2.2%/+4.9%) *is* the 0.036, and ℓ = 3, 4 pass the box because their pole mismatch is of the same size. It is not that s is ℓ-flat (it is not: 20% spread) but that the box tolerates ~0.05 in β. **What one constant described is the near-imaginary value of GR's own admittance at the three a = 0 poles**, within the box's tolerance. That is the whole content of "4/4 at a = 0".

## §4 The requirement as a function of spin (Z⁺, (2,2), surface frame; the CD instrument, Leaver poles)
| χ | r_w | Ω_w | ω_QNM | real-ω: \|R\|, phase | at the pole: β_hor | hypothesis at the pole | mismatch |
|---|---|---|---|---|---|---|---|
| 0 | 2.6667 | 0 | 0.3737 − 0.0890i | 0.39, −43° | +0.009 − 0.116i | −0.028 − 0.116i | 0.036 |
| 0.2 | 2.6742 | 0.021 | 0.4021 − 0.0883i | 0.51, −43° | +0.014 − 0.027i | −0.027 − 0.112i | 0.095 |
| 0.4 | 2.6943 | 0.039 | 0.4398 − 0.0869i | 0.63, −38° | +0.020 **+0.064i** | −0.027 − 0.112i | 0.182 |
| 0.6 | 2.7221 | 0.055 | 0.4940 − 0.0838i | 0.74, −25° | +0.025 +0.172i | −0.026 − 0.119i | 0.296 |
| 0.68 | 2.7344 | 0.060 | 0.5240 − 0.0815i | 0.77, −13° | +0.027 +0.224i | −0.025 − 0.126i | 0.353 |
| 0.8 | 2.7534 | 0.067 | 0.5860 − 0.0756i | 0.80, +21° | +0.027 +0.320i | −0.024 − 0.141i | 0.463 |
| 0.9 | 2.7694 | 0.072 | 0.6716 − 0.0649i | 0.78, +99° | +0.018 +0.435i | −0.020 − 0.164i | 0.600 |

Also at χ = 0.68: (2,0) real-ω 0.52 at −37°; (2,−2) 0.36 at −31° (retrograde-keyed template). Two facts: (i) at real ω the requirement is a strong function of spin — no spin gives a real step; (ii) **at the poles, from χ ≈ 0.4 the horizon's admittance in the even variable is not absorbing at all (Im β > 0)**. The 3657/3668 Kerr failures are located here: no real s, no frame, no delay produces a sign flip of Im β. (The sign is a property of the even variable at the complex frequency — on SN's Y the pole value differs; the basis-dependence of CONV-042 GPT 5 — but the mismatch to −ik/s is large on every realization tested.)

## §5 Mechanisms against both pole data (parameter-free)
- **(i) real step** (H-SURFACE-IMPEDANCE; CANDIDATE-S-AREA ψ⁴): meets a = 0 to 0.04 (calibration); cannot meet Kerr (opposite Im sign). Verdict as a mechanism: FAILS.
- **(ii) delayed compliant surface**: a delay is a phase e^{−2ikτ} on a passive reflector — it cannot flip the sign of Im β. On the real-ω readings the Kerr-fitted delay τ_d = 0.28 M predicts −12° at a = 0 against −43°. A **one-Moment (Planck) delay gives 8 × 10⁻³⁹ degrees**: the one-Moment-delay compliance of 3375/3376 is a phase-zero surface at ringdown frequencies and cannot be the origin of any phase. FAILS.
- **(iii) co-rotating step** = (i) in the surface frame; tested at 3657/3668. FAILS.
- **(iv) the excised region itself** — GR's wave equation between r_w and r₊ with horizon absorption behind it — meets both by construction and is the only zero-parameter structure that does.

## §6 The open problem RE-CUT
**OPEN-GR-SURFACE-IMPEDANCE-1 as posed — "derive from the cycle why the saturated register presents a wave with ~3× the exterior's impedance" (3645 §3) — has no passive-surface solution and its number is not a CPP constant:** s = 3.22 is the ℓ = 2, a = 0 pole value of GR's own admittance β_hor from 8M/3. **Re-cut target:** the complex admittance function β_hor(ω, ℓ, m, χ) at the poles — which a saturated register meets only if it propagates the exterior's wave equation below the cap with horizon-like absorption behind it, i.e. only at the black-hole end of V2.0's map. The re-cut problem is therefore the same question as OPEN-GR-CORE-DISSIPATION-1 and the excluded extension's wave sector: *does the cycle, above the cap, propagate A3′'s tensor wave as Einstein's equations do?* Attempt 5, if any, is not a surface law; it is that derivation. Registered as the re-cut; no attempt numbered.

## §7 Standing
- **H-SURFACE-IMPEDANCE:** count unchanged 1/4/2/1; its number identified (§3) — the hypothesis is an approximation to GR's pole admittance at a = 0, never a surface property; not amended, not adopted, `UNEXPLAINED` label replaced by `IDENTIFIED (GR pole value, 3670)`. **CANDIDATE-S-AREA (3655): loses its object** — there is no surface constant to be ψ⁴; recorded as withdrawn (the 3% static near-coincidence of 3655 §3 stands as a coincidence).
- **Row 7 requirement restated:** the surface must present the exterior with GR's own complex admittance at the poles (table §4); at a = 0 that is nearly imaginary (a step describes it within the box), at Kerr it is not absorbing in the even variable.
- **Records corrected:** 3657 §4's a = 0 row; 3668 §3/§5's "a = 0 real step 0.53 at −3°" and "|R| ≈ 0.7–0.8 at −(13–17)°" as *the requirement* (they are real-ω readings, recorded as such); GR-2's "= the horizon's own from that radius" (3671); PRED-O-39's bracket (3671).
- **Instrument:** the CD Z⁺ solver now carries r_w(χ) (F_n = 4/9) and Leaver poles across spin — the spin curve of §4 is reusable for any future wall law.
- Next on the lane (ledger §5): the complex ray for the Kerr (2,+1) comparator on the CD Z⁺ instrument (unchanged); then the re-cut derivation question (§6) as the lane's physics act, with OPEN-GR-CORE-DISSIPATION-1.
