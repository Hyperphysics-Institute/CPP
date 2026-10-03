# A Round-Trip Clock in the Founder's Two-Sided Field Gives Einstein's Factor Exactly: the Size Problem Reduces to One Number, κ, the Fraction of Half the Stress by Which Each Leg Is Helped or Hindered (κ = 1 Is Exact Schwarzschild; the Ringdown Needs κ ≳ 0.70)

**Patch:** 4379. **Lane:** foundations, with GR. **Session:** 242.
**Answers:** TODO-4365-THIRDORDER (a), the model owed at 4378 (Claude's work; no founder input this turn).
**Verify:** `series_standard_model/code/4379_round_trip_clock_gives_einstein.py` (sympy + scipy). Both endpoints
reproduce: κ = 0 gives the one-PSR exponential exterior (4365), and κ = 1 gives exact Schwarzschild (photon sphere 3m,
shadow 3√3 m).

## 1. The clock as a round trip (corpus anchor)

> **Erratum (Patch 4381):** the ± leg asymmetry below is Claude's construction, not the founder's picture (4377: slowing "by collision", on both legs); a static field cannot make outward and inward speeds differ without a flow. "The founder's … made quantitative" is withdrawn. The fixed path also conflicts with the thermal-boundary rule (c04). See `4381_hold_clock_ruling_gr_exterior_is_calibration.md` §2.

The corpus already models the electron's ZBW clock as a **radial round trip**: a wave runs outward from the unpaired
eCP through its polarisation cloud, reflects at the cloud's edge and returns, and the round-trip time sets the frequency
(`series_relativity/SR_companion_papers/c04_ZBW_hbar_mass_units/development/development_notes.md` L1475–1490).

In the founder's two-sided field (4377: opposite charges drawn in, like charges pushed out), one leg of that round trip
is helped and the other hindered. Let each leg's rate change by ±κϱ, with ϱ = kΔ/2. Over a fixed path length L:

    T = L/(1 + κϱ) + L/(1 − κϱ) = 2L/(1 − κ²ϱ²)    ⇒    X = 1 − κ²ϱ²   (exactly)

- **The first order cancels exactly.** This is the upstream–downstream (light-clock) arithmetic: the helped leg's gain
  and the hindered leg's loss cancel at first order, leaving a pure square. That is the founder's "opposite drawn in,
  like pushed out", made quantitative, and it meets 4373's Cassini condition by construction.
- **κ = 1 gives Einstein's factor to all orders.** With GR-1c's self-consistency (4372) the lapse becomes
  N = ((1 − κϱ)/(1 + κϱ))^{1/κ}. At κ = 1 that is (1 − ϱ)/(1 + ϱ), GR-1c's artanh Form A, exact isotropic
  Schwarzschild. **Exactness, not just the leading term, follows from the round trip.**
- **Condition:** the path length is fixed (the cloud's diameter, which scales with the ruler), so the clock rate is
  the harmonic mean of the two legs. If the legs were instead averaged by time spent at each speed rather than by
  distance, the effect would vanish.

## 2. What the ringdown needs (script)

| κ | photon sphere (areal) | shadow vs GR | ringdown frequency vs GR | damping vs GR |
|---|---|---|---|---|
| 0 (one PSR) | 3.297 m | +4.63% | −4.42% | −4.42% |
| 0.50 | 3.228 m | +3.52% | −3.40% | −3.40% |
| 0.70 | 3.158 m | +2.43% | −2.37% | −2.37% |
| 0.85 | 3.088 m | +1.34% | −1.32% | −1.32% |
| 1 (Einstein) | 3.000 m | 0 | 0 | 0 |

GW250114's −2.4% edge (eikonal, non-spinning) needs **κ ≳ 0.70**. Weak field: X enters at second order in the stress,
so Mercury and Cassini are untouched for every κ.

## 3. What remains: one number

The size problem of 4377–4378 is now a single physical question. **By how much is each leg helped or hindered,
compared with half the PSR's first-order shrinkage (ϱ = kΔ/2 = ε/2)?** κ = 1 means exactly half. Then black holes are
Einstein's exactly; κ ≥ 0.7 passes the current ringdown. A reason for "half" would make the result a derivation. One
candidate (my inference): the stress excess is shared equally between the two members of a polarised DP pair, the one
drawn in and the one pushed out.

## 4. What it would change, if confirmed

- **The founder's 4362 ruling (one PSR for rulers and clocks)** would hold at first order and gain a second-order
  clock factor (1 − κ²ϱ²), a new ruling beside R-PSR-PACE-AT-N.
- **κ = 1:** GR-1c's exact-Schwarzschild theorem would be restored, now with a mechanism. The steady-percentage
  curve (4365) would describe the PSR (ruler) only, not the clock. The wormhole geometry (4375) would no longer be the
  exterior, and THEO-PCD-SEA's horizon would stand.
- **The AP-5 cap / floor separation flagged at 4373** would become real: sphere full (ruler ½) at ϱ = √2 − 1, clock ½
  at ϱ = ⅓.

## 5. Question to the founder (physical picture)

Picture the electron's clock as a wave going out through its polarised cloud and coming back. Near a black hole, the
two-sided pull helps the wave one way and hinders it the other. Is the help on one leg, and the hindrance on the other,
equal to **half** of how much the Planck sphere has shrunk there? If yes, black holes come out exactly as Einstein's.
If it is at least 70% of that half, they pass the best ringdown measurement.

## 6. PD-008

- **The convenient branch, marked:** "κ = 1, so Einstein is derived." It is not: κ = 1 is the value that reproduces
  Einstein, and its reason ("half", shared by the pair) is my inference, put to the founder.
- **What is derived:** given a round-trip clock over a fixed path in a two-sided field with symmetric ±κϱ legs, the
  first-order cancellation and the exact functional form 1 − κ²ϱ² follow, and with self-consistency so does the whole
  exterior.
- **Not sent to a fresh critic:** the algebra is two lines plus 4372's validated family; no exclusion is claimed.
