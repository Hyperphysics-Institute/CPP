# The founder's method enacted as rule 6 (derive → hypothesis → group → reconnect); OPEN-GR-SURFACE-IMPEDANCE-1 attempt 2a (the two-channel wall as a parallel admittance mixture) FAILS; the statistics-level HYPOTHESIS H-SURFACE-IMPEDANCE (impedance 3.22× the exterior's at the level set) carried unchanged to a third phenomenon — the ℓ = 4 fundamental — and found descriptive (−1.0% / −5.1%). Group score: 3 of 3 computed (ℓ = 2 pin, ℓ = 3, ℓ = 4); the overtone not computed (solver limit); Kerr owed (dictionary)

**Patch 3646, Session 163, 6 Sep 2026.** Founder text `founders_voice/founder_method_derive_then_hypothesis_2026-09-06.md` (verbatim). Verify `code/3646_surface_impedance_hypothesis_group_verify.py` (4/4; run from the repo root). Reasoning `reasoning/3646.md`. No paper touched. CONV-042 held.

## §1 Rule 6 (3641 §2), from the founder's words
(1) Derive from the nine axioms. (2) If that fails, state a statistics-level hypothesis that satisfies the phenomenon and plausibly connects to the axioms — labeled `HYPOTHESIS`, never adopted. (3) Apply it *unchanged* to a group of related phenomena. (4) Only after several show it descriptive, attempt to connect it to the axioms. A hypothesis is never a result and never enters an abstract. This is what 3644 skipped: it went from one fit to a request for adoption, omitting (3).

## §2 Attempt 2a — the two-channel wall as an admittance sum: FAILS
Count channel = the 3390 trace-pinned element `β_trace = b₀ − b₂ω²` (lossless, `−1.26` at the QNM frequency); tensor channel = a local absorber `−iω`; `β_mix = f·β_trace + (1 − f)(−iω)`. Target `β_hor(ω_QNM) = +0.008 − 0.116 i`. No f comes within 0.25; the f that matches the absorption (0.69) puts `Re β = −0.87` where the target has ≈ 0. The trace element carries a large real part the horizon does not have. **The admittance-sum form is not the junction.** Attempt 2b is JUNCTION-1 proper — the two channels coupled through A3′'s metric map, not added — and is the next derivation act.

## §3 The hypothesis, and the group
`H-SURFACE-IMPEDANCE`: the saturated register presents a passing wave with impedance `s ×` the exterior's, `s = 3.22`, locally ingoing behind it (`β = −iω/s`). Plausible connection to the axioms: the c/2 hop kinematics at the floor and R-CAP-SPRING's anchoring — named, not derived.

| phenomenon (a = 0, 8M/3) | GR | hypothesis | δf / δτ | status |
|---|---|---|---|---|
| ℓ = 2 fundamental | 0.3737 − 0.0890 i | 0.3656 − 0.0848 i | −2.2% / +4.9% | the pin (3644) |
| ℓ = 3 fundamental | 0.5994 − 0.0927 i | 0.5911 − 0.0939 i | −1.4% / −1.3% | descriptive (3644) |
| **ℓ = 4 fundamental** | 0.8092 − 0.0942 i | **0.8010 − 0.0992 i** | **−1.0% / −5.1%** | **descriptive (this patch)** |
| ℓ = 2 first overtone | 0.3467 − 0.2739 i | — | — | not computed: direct integration stalls at Im ω ≈ −0.27; needs a Leaver solver |
| Kerr (2,2), a = 0.68 | 0.528 − 0.082 i | — | — | owed: the SN ↔ local-wave dictionary at the wall (KERRWALL-1) |

Machinery: the horizon-equivalent wall reproduces the ℓ = 4 GR mode to 0.01% / 0.3%. The hypothesis' residuals shrink with ℓ in frequency (−2.2, −1.4, −1.0%) and stay small in damping: one number, three lines, no refit. **Descriptive on the group so far; not yet evidence about the axioms.** Under rule 6 the next step on this track is more members (overtone with a proper solver; Kerr after the dictionary; the Love number as the static limit of the same impedance — row 6), and the derivation track (2b) runs in parallel.

## §4 Standing
- OPEN-GR-SURFACE-IMPEDANCE-1: open; attempts 1 (3645) and 2a (this patch) failed; 2b next.
- H-SURFACE-IMPEDANCE: `HYPOTHESIS`, 3/3 computed members descriptive; s stays `UNEXPLAINED`.
- Ledger row 7: FAILS as written (unchanged); the requirement and the hypothesis both recorded there.
- Row 6 next: the Love number computed under the budget interior with the surface impedance as the static stiffness family — the hypothesis' fourth member if it lands, a bracket if it does not.
