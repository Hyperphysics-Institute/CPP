# The echo searches do not probe the CPP wall — the ringdown does. GWTC-2's echo section gives Bayes factors, no amplitude limit, and a template built for Planck-scale delays; the CPP cavity's round trip is 0.7 ms. But the observed (2,2) prograde ringdown agrees with Kerr, and a wall at 1.33 r_S moves that mode by its impedance: the compatible band is β ≈ −0.07 to +0.05 — a calibration by an existing observation

**Patch 3615, Session 161, 4 Sep 2026.** Verify `code/3615_ringdown_constrains_the_wall_verify.py` (4/4; 3359/3392 SN ladder, prograde m = +2, χ = 0.68, r_w = 2.734 M). Source: GWTC-2 TGR §VII.B (arXiv:2010.14529), pasted verbatim by the founder. Reasoning `reasoning/3615.md`.

## §1 What the GWTC-2 echo section says (founder's paste)
- Template-based search (Lo et al. [255]; ADA model [256]): the IMR ringdown repeated with **five echo parameters** — relative amplitude, damping between echoes, ringdown start time, first-echo time, echo delay — **uniform priors**.
- 31 BBH events: **no statistically significant evidence**; detection threshold log₁₀B ≈ 2.48; highest value 0.17 (GW190915); GW150914 −0.57, GW170814 −0.49, GW190521 −1.82.
- **"The posterior distributions of the extra echo parameters mostly recover their corresponding prior distributions."** I.e. **no amplitude limit is reported**, and the data are largely uninformative about the template's amplitude within its prior.

So the expectation of 3614 §A — "if the limits are below ~0.4, lossless walls are disfavoured" — does **not** follow from this paper: it sets no such limit. Two further reasons the echo searches do not test the CPP wall:
- **Delay.** The ADA template and the searches built on it target echo delays of Planck-scale walls (`Δt ~ 8M ln(M/l_P)`, ~0.1–0.3 s for GW150914). The CPP cavity at the ratified surface has a round trip of `2.29 M ≈ 0.7 ms` (3390): its "echoes" are one cycle apart and blend into the ringdown. The template's delay prior almost certainly does not reach there (the prior range should be confirmed in Lo et al. — requested), and if it does not, the null results say nothing about a 0.7 ms cavity.
- **Morphology.** A 0.7 ms cavity does not produce separated pulses; it produces a *modified ringdown* — which is exactly what the pole calculations describe.

## §2 The observation that does test it: the ringdown itself
The (2,2) prograde mode is what the detectors measure (GW150914 at ~250 Hz), and the no-hair tests find it Kerr-consistent to a few percent in frequency and tens of percent in damping. A wall at the ratified Kerr surface **moves that mode**, by an amount set by its impedance:

| wall β (on the SN function, 2.734 M, χ = 0.68) | (2,2) prograde | δf vs Kerr | δτ vs Kerr |
|---|---|---|---|
| +0.10 | 0.553 − 0.168i | +4.7% | −51% |
| **0 (Neumann)** | 0.518 − 0.113i | **−2.0%** | −27% |
| **−0.05** | 0.497 − 0.089i | **−5.8%** | **−7.7%** |
| −0.10 | 0.474 − 0.066i | −10% | +24% |
| −0.15 | 0.447 − 0.043i | −15% | +89% |
| −0.20 | 0.416 − 0.021i | −21% | +300% |
| Dirichlet (hard) | ~0.77 (unconverged) | ~+45% | — |

(Kerr reference `0.528 − 0.082i`, literature value for a ≈ 0.7; the published δf̂₂₂₀, δτ̂₂₂₀ constraints are requested to draw the band exactly.)

**Result.** A wall at 1.33 r_S is compatible with the observed ringdown only in a narrow band around **Neumann: β ≈ −0.07 … +0.05** at the ringdown frequency. Soft walls (β ≲ −0.1) and hard walls (Dirichlet, the shipped assumption) are **excluded by the ringdown** — the shipped `X = 0` would have moved GW150914's ringdown frequency by tens of percent. This is the calibration S-EMPIRICS-ARBITER asked for, and it comes from an observation already made, not from a future echo.

## §3 What the band says about the theory
The theory's derived RW-gauge law (3391) and the odd-sector law (3384) were both Neumann-like at the mode frequency — the "Neumann crossing at the barrier top" regularity (3383, unexplained). The ringdown now says: **that is the property a surface at 1.33 r_S must have to look like a Kerr black hole.** Whether the lattice-frame (C5) law has it is the open computation; the band it must land in is now known.

## §4 Requests (to draw the band exactly)
- The GWTC-2 or GWTC-3 TGR ringdown section: the δf̂₂₂₀ and δτ̂₂₂₀ 90% intervals (pyRing/pSEOB) for GW150914 and the combined constraint.
- Lo et al. (arXiv:1811.07431): the prior range on the echo delay Δt_echo.
