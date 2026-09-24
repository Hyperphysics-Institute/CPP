# The ZBW Frequency Convention Moves g_A More Than the Residual Does

**Patch:** 4266. **Lanes:** foundations (TODO-4264-PASSTHROUGH step 8) and EW → strong (TODO-4234-DELTA).
**Session:** 239. **Verify:** `series_standard_model/code/4266_zbw_frequency_convention_and_gA.py`.

## 1. Three conventions in the corpus

"The Compton frequency" appears in the corpus under three conventions:

- **(a)** Route (H), used by every g_A number from 4243 to 4265, takes the angular frequency ω = mc²/ħ. That means
  one full pass-through swing lasts h/mc², the Compton period λ_C/c.
- **(b)** Schrödinger's ZBW runs at 2mc²/ħ. c04's remark relates it to CPP by a factor 2 from "two-way transit".
- **(c)** c04's own proof of mc² = ħν_C sets the period T_C = 2r_th/c = ħ/mc², which is angular 2πmc²/ħ.

The breath's momentum spread scales as √ω, so the choice goes straight into g_A.

## 2. Rows verbatim (D-11)

```
(a) route H, mc^2/hbar   (omega = 1.000 mc^2/hbar)
    4244 mode set            g_A=1.4056 ( +10.2%)  mu_p=2.771 ( -0.8%)  mu_n=-1.829 ( -4.4%)
    founder-ruled set (4262) g_A=1.3331 (  +4.5%)  mu_p=2.699 ( -3.4%)  mu_n=-1.811 ( -5.3%)
(b) Schrodinger, 2mc^2/hbar   (omega = 2.000 mc^2/hbar)
    4244 mode set            g_A=1.2761 (  +0.1%)  mu_p=2.656 ( -4.9%)  mu_n=-1.747 ( -8.7%)
    founder-ruled set (4262) g_A=1.1908 (  -6.6%)  mu_p=2.571 ( -8.0%)  mu_n=-1.726 ( -9.8%)
(c) c04 T_C literal, 2 pi mc^2/hbar   (omega = 6.283 mc^2/hbar)
    4244 mode set            g_A=1.0363 ( -18.8%)  mu_p=2.440 (-12.6%)  mu_n=-1.601 (-16.3%)
    founder-ruled set (4262) g_A=0.9517 ( -25.4%)  mu_p=2.356 (-15.6%)  mu_n=-1.580 (-17.4%)

  omega that closes g_A, 4244 set: 2.007 mc^2/hbar
  omega that closes g_A, ruled set: 1.337 mc^2/hbar

-> g_A's dependence on the frequency convention (1.33 / 1.19 / far below for the ruled set) is larger than the
   residual itself.  (a) is the reading consistent with E = hbar omega for the swing; (b) is an energy-gap beat
   (2mc^2) of the Dirac formalism, which the pass-through cycle shows as its speed maximum twice per swing; (c) is
   c04's h-vs-hbar slip in T_C (2 r_th/c = hbar/mc^2 is 2 pi short of the Compton period h/mc^2).
```

## 3. Result

**(i) The convention matters more than every mechanism in this arc.** For the founder-ruled mode set, g_A is 1.333,
1.191 or 0.952 under (a), (b) or (c). The residual being chased is 0.13.

**(ii) Convention (c) is a slip in c04 and is excluded.** 2r_th/c = ħ/mc² is 2π shorter than the Compton period
h/mc². c04 reaches mc² = ħν_C by pairing ħ with 1/T, where the standard relation pairs h with 1/T, or ħ with 2π/T.
The g_A rows show the consequence: 25% low. A c04 correction is filed as part of sweep step 2.

**(iii) Convention (a) is the reading consistent with E = ħω for the swing, and it stands.** Schrödinger's 2mc²/ħ is
the beat between the +E and −E parts of a Dirac state, whose energy gap is 2mc². It is not the rate at which anything
swings about a centre. In the pass-through cycle the swing crosses its centre twice per period, so its speed peaks at
2ω. That is the natural CPP counterpart of Schrödinger's doubled frequency, and it is how c04's "two-way transit"
remark should read under pass-through (added to sweep step 2). So the breath runs at ω = mc²/ħ, and 4262–4263's
g_A ≈ 1.31–1.33 stands.

**(iv) The coincidence, marked (PD-008).** With 4244's mode set (before the founder added the diagonal mode at 4262),
the ω that closes g_A exactly is **2.007 mc²/ħ**, Schrödinger's frequency to 0.4%. That is the most convenient
branch this arc has produced. It is **not adopted**, for three reasons:
- It uses a mode set the founder has since corrected (4262: the diagonal minus-vertex mode). With the ruled set,
  Schrödinger's frequency overshoots to 1.191, and the closing ω is 1.337, which is no natural value.
- It rests on convention (b), which (iii) argues is a beat frequency, not a swing frequency.
- μ_p there is −4.9%, so the m_q tension remains.

It is recorded here in full so the next context window can critique the rejection rather than rediscover the
coincidence. That critic item is filed.

## 4. Where g_A stands

Under the ruled picture (pass-through, ω = mc²/ħ, founder mode set, u–u exchange), g_A = 1.310 (simultaneous
modes) and about 1.32 (sequential with energy carried; exchange not yet recomputed). μ_p is about 4% low in every
version. Two items remain owed: the sequential exchange, and m_q (≈ 300 MeV restores μ_p).
