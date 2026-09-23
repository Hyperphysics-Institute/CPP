# The Breath's Size Calculated: g_A = 1.38–1.43 From the Founder's Modes at the ZBW Frequency, Zero Parameters

**Patch:** 4243. **Lane:** EW → strong (TODO-4240-CORE-MOTION, TODO-4234-DELTA). **Session:** 238.
**Founder (22 Sep, `founders_voice/4243_*`):** the breath is the ZBW oscillation of opposite charges; it also runs
sideways between opposite-charge quarks; the modes follow the colour combinations; *"The distance … is something you
will have to calculate."*
**Verify:** `series_standard_model/code/4243_zbw_breath_modes_gA.py`.

## 1. What the calculation uses, and where each piece is on file

- **Frequency:** c04 — a ZBW cycle of mass m runs at the Compton frequency ω = mc²/ħ (4238 confirmed identical to
  4231/4233's cycle). The breath is a ZBW oscillation (founder), so it runs at ω for m = m_const.
- **Modes (founder's rule, applied to the proton):** one radial mode per quark against its vertex; sideways modes only
  along edges to opposite-charge quarks. u: radial + u–d (2); d: radial + d–u₁ + d–u₂ (3). u–u is same-sign.
- **Size, two independent routes:** (H) each mode in its quantum ground state at ω — σ_x = √(ħ/2mω) = r_ZBW/√2 for an
  anchored partner (the frame vertex), reduced-mass form for u–d with both quarks moving; (C) the 4231 fall-reset-return
  as a classical relativistic Coulomb fall along one line, amplitude fixed by period = Compton period.
- **Axial and moment:** 4242's R = 1/3 + (2/3)⟨m/E⟩ per quark, isotropic (4134); g_A = (4/3)R_u + (1/3)R_d from the
  4240 state; moment tie S = (1+R)/2 per quark, now with R_u ≠ R_d.
- **Couplings (D-7):** α_geom = 1/√5 is SS-2's value; SS-1 carries 0.559 under the same name — not used; flagged.

## 2. Rows verbatim (D-11)

```
========================================================================================================================
(H) harmonic ground state at the Compton frequency, founder's mode rule
========================================================================================================================
  per-mode position spread, anchored partner: sigma_x = r_ZBW/sqrt2 = 0.446 fm; u quark (2 modes) <r^2> = r_ZBW^2 exactly -- SS-2's smearing, as a CHECK not an input
  radial anchored, sideways anchored                   R_u=0.8385 R_d=0.7872  g_A=1.3804 ( +8.2%)  mu_p=2.751 ( -1.5%)  mu_n=-1.806 ( -5.6%)
  radial anchored, sideways u-d both moving            R_u=0.8652 R_d=0.8308  g_A=1.4306 (+12.2%)  mu_p=2.794 ( +0.0%)  mu_n=-1.844 ( -3.6%)
  needed: every mode's sigma_p x 1.368                 R_u=0.7772 R_d=0.7173  g_A=1.2754 ( -0.0%)  mu_p=2.658 ( -4.8%)  mu_n=-1.738 ( -9.1%)
  -> the measured g_A needs each mode's momentum spread 37% above the Compton ground state (sigma_x 0.326 fm per mode)

========================================================================================================================
(C) classical fall-reset-return along one line, period = Compton period (4231 mechanism, c04 frequency)
========================================================================================================================
  a = (2/3) alpha_geom  (SS-2 qq colour coefficient) (0.298): amplitude A = 1.232 r_ZBW = 0.777 fm  vs u-d edge 0.620 fm;  one line: g_A = 1.5031 (+17.9%)
  a = alpha_geom                                     (0.447): amplitude A = 1.380 r_ZBW = 0.871 fm  vs u-d edge 0.620 fm;  one line: g_A = 1.4648 (+14.9%)
  a = (4/3) alpha_geom                               (0.596): amplitude A = 1.492 r_ZBW = 0.941 fm  vs u-d edge 0.620 fm;  one line: g_A = 1.4335 (+12.4%)
  -> a single-line Coulomb breath with the ZBW period is as large as the frame (0.78-0.94 fm > 0.62 fm) and still gives g_A 1.43-1.50.

========================================================================================================================
(T) the 4242 tie inverted, one R for u and d: measured g_A and mu_p together fix m_q
========================================================================================================================
  R=0.7652, S=0.8826; M_N/m_q=3.1643 -> m_q=296.7 MeV (m_p/3 = 312.8); then mu_n=-1.862 vs -1.913 (-2.7%)

========================================================================================================================
(Q) sensitivity to the mode rule: sideways along u-u too (colour attraction, SS-2's (2/3) alpha_geom term), all three quarks 3 modes
========================================================================================================================
  u-u included, all anchored                           R_u=0.7872 R_d=0.7872  g_A=1.3120 ( +2.9%)  mu_p=2.683 ( -3.9%)  mu_n=-1.788 ( -6.5%)
  u-u included, sideways both moving                   R_u=0.8308 R_d=0.8308  g_A=1.3847 ( +8.6%)  mu_p=2.748 ( -1.6%)  mu_n=-1.832 ( -4.2%)
```

## 3. What is established

**(i) The size is calculable, and the two routes disagree in a way that decides between them.** A classical Coulomb
breath with the ZBW period needs an amplitude of 0.78–0.94 fm — larger than the 0.62-fm u–d edge it lives on. The
quantum ground state at the same frequency has σ_x = 0.446 fm per mode, and **the up quark's two modes reproduce SS-2's
smearing ⟨r²⟩ = r_ZBW² exactly** — a check, not an input: SS-2's number was written for a circular orbit, and it comes
out of the founder's two-mode breath at the ZBW frequency. Route (H) is the one consistent with the frame.

**(ii) First zero-parameter CPP g_A: 1.38–1.43** (anchored / u–d both moving), against 1.2754 measured and 1.667 for
SU(6) alone — **the breath supplies 70–73% of the reduction.** The measured value needs each mode's momentum spread 37%
above the Compton ground state (σ_x 0.33 fm per mode).

**(iii) The moments move the other way, and that is informative.** Same state, same tie: μ_p = 2.751 / 2.794
(−1.5% / 0.0%), μ_n = −1.806 / −1.844 (−5.6% / −3.6%) — better than 4126's +7.4% / +4.5%. So at m_q = m_p/3 the moments
want *less* reduction than g_A does. Inverting the tie with one R: measured g_A and μ_p together fix m_q = 296.7 MeV
(vs 312.8 assigned), and then μ_n = −1.862 (−2.7%). The residual is a tension between g_A and SS-2's m_q = m_p/3
assignment, not a free parameter to tune.

**(iv) Sensitivity to the mode rule.** If the sideways ZBW also runs along u–u — the colour attraction SS-2 already puts
in the u–u potential ((2/3)α_geom), despite the same electric sign — every quark has three modes and g_A = 1.312 (+2.9%)
anchored, 1.385 (+8.6%) with both moving. The mode rule is the largest single lever, and it is the founder's to state.

## 4. PD-008 — the convenient branches, marked

Two were available: (a) headline **μ_p = 2.794, 0.0%** from the both-moving row — refused, because the same row gives
g_A +12%; (b) adopt the u–u-included anchored row, **g_A = 1.312, +2.9%** — refused as a result, because the founder's
words say "opposite-charge quarks" and u–u is same-sign; it is shown as sensitivity and handed up. **Result as it
stands:** under the founder's stated modes at the ZBW frequency, g_A = 1.38–1.43 (+8 to +12%), zero parameters, with
the moments at −1.5 to −5.6%. Submitted to the next window for critique: the anchored-vs-moving partner choice, the
harmonic treatment of a mode whose ground-state kinetic energy is ~mc²/4 (relativistic anharmonicity unquantified), and
the orthogonal-modes approximation (radial and edge directions are not orthogonal in the frame).

## 5. Handed up (PD-006(a), one picture)

**Do the two up quarks ZBW-oscillate sideways against each other along the u–u edge?** Electrically they are both
positive, but SS-2's force balance holds that edge together with a colour attraction. If the colour attraction makes
them a breathing pair, each quark has three modes and g_A comes to 1.31; if only electrically opposite charges breathe
sideways, it stays at 1.38–1.43.
