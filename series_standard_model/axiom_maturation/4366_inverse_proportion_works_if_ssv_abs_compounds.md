# The Founder's Inverse Proportion Works Exactly If SSV_abs Compounds: Count × SSV_abs = Constant Then Gives Mercury's ½ and Needs No k·SSV_abs,0 Condition — the Same Physics as 4365's Compounding Count

**Patch:** 4366. **Lane:** foundations, with GR. **Session:** 242.
**Founder:** `founders_voice/4366_what_makes_inverse_proportion_work.md` ("What would be needed to make this work?").
**Verify:** `series_standard_model/code/4366_inverse_proportion_needs_compounding_ssv.py` (sympy).

## 1. Why the plain inverse proportion fails

GR-1j writes SSV_abs as the homogeneous value plus the linear census, SSV_abs = S0 + Δ (L193–194). With the Planck-sphere
count n ∝ 1/SSV_abs and q = (n/n_∞)^{1/3}, the PSR law is q = (1 + Δ/S0)^{−1/3}. This has no free knob:

- matching first order forces k·S0 = 1/3, which is 4360's condition;
- the second order then comes out 2, not ½, so β = 5/2 and Mercury fails;
- the local field depends on the background at first order, so the clocks see α drift.

A higher power, n ∝ SSV_abs^{−m} with c = m/3, gives q = (1 + ε/c)^{−c}:
- second order (c+1)/(2c), which Mercury needs within ~10⁻⁴ of ½, so c ≳ 5000;
- background factor c/(c+ε₀), so the annual clock swing is dU/c, needing c ≳ 3×10⁷.

As c → ∞ the power law becomes e^{−ε}. **An inverse power works only in the limit where it already is compounding.**

## 2. What makes it work exactly

Keep the founder's inverse proportion, **n ∝ 1/SSV_abs**, and change how SSV_abs is computed from the arriving
stress. Each arriving unit raises it by **a fixed fraction of what is already there** rather than by a fixed amount:

    SSV_abs = S0 · e^{3kΔ},   Δ = the linear, harmonic census (GR-1j's census-linearity lemma and exact statics unchanged)

Then:
- **n × SSV_abs = constant holds exactly.** This is 4360's "PSR³ × SSV_abs constant", now exact.
- **q = e^{−kΔ} for any S0.** The background value drops out, so **4360's k·SSV_abs,0 = 1/3 condition disappears**.
- The second order is **½, Mercury's value**, and the absolute background (Sun, Galaxy, cosmology) scales out of every
  local measurement.
- **The physics is identical to 4365's compounding count.** Only the bookkeeping differs: in 4365 the count
  compounds with an additive SSV_abs; here SSV_abs compounds and the count is its plain inverse.
- **Not changed:** the 4364 source rule (injection ∝ n_s) is still needed. The third order (−1/6 against GR-1c's −¼)
  and the 4.6% larger shadow with no horizon (4365, TODO-4365-THIRDORDER) come with it.

The relay still adds stress linearly. That is Δ, and it is what makes the statics exactly Laplace (GR-1j). What
compounds is the register the GP computes from that sum, the SSV_abs it uses to set its PSR. GR-1j L193's "SSV_abs =
S0 + Δ" would then read SSV_abs = S0·e^{3kΔ}, with Δ keeping every role it has in the paper. Precedent: the 0747 audit
(SR lane) credited a count-driven PSR with "multiplicative = exponential" as the right architecture, and noted that
logarithms arise from per-unit contributions that diminish in proportion to what is already there.

## 3. Question to the founder (physical picture)

When stress arrives at a grid point, does each new unit of stress raise its SSV_abs by the **same amount**, or by the
**same percentage** of what it already holds? With the same percentage, your inverse proportion (count of grid points in
the Planck sphere ∝ 1/SSV_abs) works exactly. It gives Mercury's orbit without a calibration, needs no special value for
the background stress, and keeps every laboratory the same in any background. With the same amount, it fails.

## 4. PD-008

- **The convenient branch:** "the founder's inverse proportion was right all along." It is right *given* a compounding
  SSV_abs, which is a new statement about how a GP computes SSV_abs. It is put to him, not assumed.
- **No new physics is claimed over 4365:** §2 is the same q(Δ). Its value is that it keeps his rule as stated and
  removes 4360's condition, and it shows that the plain inverse proportion cannot be patched by a power.
- **Not sent to a fresh critic:** the content is three lines of algebra (script parts 1–2), and the consequential
  claims (third order, shadow) were critic-checked at 4365.
