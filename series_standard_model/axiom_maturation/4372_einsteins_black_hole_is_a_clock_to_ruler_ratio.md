# Einstein's Black Hole Is a Clock-to-Ruler Ratio, Not a Fill-Dependent Speed-Up: Under GR-1c's Self-Consistency, "One PSR for Clocks and Rulers" Forces the Steady Curve, and Einstein Needs Clocks to Slow by an Extra Factor (1 − ϱ²). A One-Dial Family Connects Them, and the Ringdown Box Needs at Least Half of It

**Patch:** 4372. **Lane:** foundations, with GR. **Session:** 242.
**Founder:** `founders_voice/4372_no_mechanism_for_speedup_axioms_or_prediction.md`.
**Verify:** `series_standard_model/code/4372_clock_to_ruler_ratio_family.py` (scipy + sympy). Both endpoints reproduce
exactly: λ = 1 gives Schwarzschild (photon sphere 3m, shadow 3√3 m, Lyapunov 1/(3√3 m)), and λ = 0 gives 4365/4369's
exponential values.

## 1. The founder's answer, and what it closes

There is no mechanism in the axioms for a fill-dependent conversion (4371). That candidate is dropped. His framing
stands: if the empirics require Einstein's ringing, the axioms are missing something or wrong; if not, the theory
predicts.

## 2. Where the corpus already puts the question (D-1)

GR-1c derives its field equation from a self-consistency condition (L614–629): "the metric … determines how LSPs
propagate between Grid Points. In equilibrium, these must be mutually consistent." In the continuum this makes the
lapse N harmonic in the effective geometry (GR-1c L636–645). For a spherical body with conformally flat rulers
(g_ij = A δ) that reads

    r² √A dN/dr = m.

With the census ϱ = kΔ/2 = m/2r flat-harmonic (GR-1j), **the lapse curve is not a free choice. It follows from how
clocks relate to rulers.** Write the clock-to-ruler ratio as

    N·√A = (1 − ϱ²)^λ,   so   ln N = −2 ∫₀^ϱ dx/(1 − x²)^λ.

- **λ = 0: one PSR for clocks and rulers** (founder 4362). This forces N = e^{−ε}, the steady curve. 4365's critic
  noticed the same route.
- **λ = 1: clocks slow by an extra factor (1 − ϱ²)** beyond the rulers' shrinkage. This gives N = (1 − ϱ)/(1 + ϱ)
  and A = (1 + ϱ)⁴: GR-1c's boxed exact-Schwarzschild theorem, and its Form A, N = −2 artanh(kΔ/2), exactly.

So 4365–4371's "speed-up in the conversion" is the same thing seen from the other side. **Einstein's black hole is a
statement about clocks and rulers, not about how a sphere fills.**

## 3. The one-dial family (script)

| λ | photon sphere (areal) | shadow vs GR | ringdown frequency vs GR | damping vs GR |
|---|---|---|---|---|
| 0 (one PSR) | 3.297 m | +4.63% | −4.42% | −4.42% |
| 0.25 | 3.224 m | +3.49% | −3.37% | −3.54% |
| 0.50 | 3.150 m | +2.34% | −2.28% | −2.53% |
| 0.75 | 3.075 m | +1.17% | −1.16% | −1.37% |
| 1 (Einstein) | 3.000 m | 0 | 0 | 0 |

- To bring the frequency inside GW250114's −2.4% edge needs **λ ≳ 0.47** (eikonal, non-spinning; indicative only).
- **Weak field is untouched for every λ.** N = 1 − ε + ε²/2 − (1/6 + λ/12)ε³, so Mercury's ½ holds and γ = 1. λ enters
  at third order in the lapse and second order in the rulers, which no solar-system test can see.
- **The size of the extra factor:** at Einstein's photon sphere, clocks slow 7.2% more than rulers shrink
  (1 − ϱ² = 0.928). In ordinary space ϱ² ~ U²/4, about 10⁻¹⁷ at Earth.
- **The price:** λ > 0 restores a local-G background residual (1 + λε₀²/4), which is unobservable. For α it matters
  only per TODO-4364-EPSABS.

## 4. Three ideas, with what each needs

1. **Clocks and rulers part company at second order (λ > 0).** This is where "the axioms are missing something"
   would live if the ringdown demands it. It would amend the founder's 4362 ruling (one PSR for both) at second order
   only; first order is untouched. There is corpus precedent for the clock leaving the PSR in strong fields: 3703's
   matter lapse is capped at ½ while the Sea lapse runs on to 0.
   - **Needs:** a physical reason, in the PCD cycle, why a clock (a CP's displacement per Moment, or a bound ZBW cycle;
     R-CLOCK-RATE-IS-DISPLACEMENT) would slow by slightly more than the PSR shrinks deep in a well. That is put to the
     founder (§5).
2. **The ringdown is not yet decided (λ = 0 kept).** The −4.4% is eikonal and non-spinning (GW250114's remnant has
   χ_f = 0.68), and it uses GR's wave equation on the CPP exterior. A real test needs CPP's tensor-wave operator on the
   exterior and the spinning remnant. If that lands inside the box, nothing changes. If outside, idea 1 is forced.
   - **Needs:** the computation (TODO-4365-THIRDORDER (b), owed, GR lane). This is the "we can only predict" branch,
     with the prediction made sharp.
3. **Prediction if λ = 0 survives:** shadow +4.6%, ringdown frequency and damping each about −4%, and no strict
   horizon. The EHT's next-generation shadows and LVK's O5 ringdowns would test it.

## 5. Question to the founder (physical picture)

Your ruling is that one PSR sets both rulers and clocks, and in ordinary gravity that is exactly right to the precision
anyone can measure. Deep in a well, near a black hole, is there anything in the PCD cycle that would make a clock tick
slightly slower than the PSR alone says? For example, does a bound oscillation, a CP circling within its domain, take a
little longer per cycle there than its PSR would suggest? About 7% slower at the photon sphere, and it must vanish in
ordinary space, would give Einstein's black hole exactly. Half of that would already satisfy the best ringdown so far.

## 6. PD-008

- **The convenient branch:** treating λ = 1 as "the corpus's answer" because GR-1c's theorem already assumes it.
  GR-1c assumed Schwarzschild's rulers; the founder's 4362 ruling, read exactly, gives λ = 0. Neither is adopted; the
  dial is put to him.
- **Not claimed:** that λ = 0 fails. The ringdown comparison is eikonal and non-spinning (idea 2).
- **Not sent to a fresh critic:** both endpoints reproduce known exact solutions, the family is one quadrature, and no
  exclusion is claimed. The GW comparison was critic-checked at 4369.
