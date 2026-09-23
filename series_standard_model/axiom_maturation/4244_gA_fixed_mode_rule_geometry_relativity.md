# g_A Under the Founder's Fixed Mode Rule: 1.35–1.41, Geometry and Relativity Checked — the Breath Result Stands

**Patch:** 4244. **Lane:** EW → strong (TODO-4240-CORE-MOTION, TODO-4234-DELTA). **Session:** 238.
**Founder (22 Sep, `founders_voice/4244_*`):** the two up quarks do not breathe sideways against each other; same
charge, they repel. The 4243 mode rule stands: u — radial + u–d; d — radial + two u–d.
**Verify:** `series_standard_model/code/4244_gA_mode_rule_fixed_geometry_and_relativity.py`.

## 1. What this patch closes from 4243's critic list

- **(G) Orthogonal modes.** In the SS-2 frame the d's two edge lines meet at 60.5°, not 90°, and the radial direction is
  unspecified. With the real triangle and the radial direction scanned from the plane normal into the plane, g_A moves
  by at most 0.8%. Closed.
- **(K) Relativistic anharmonicity.** Solving each mode as √(p² + m²) + ½Mω²x² (spinless Salpeter, momentum space) at
  the Compton frequency widens the per-mode spread by 12% (anchored 0.792 vs 0.707 m_const c) and lowers g_A by 2.5%.
  Closed — spin–orbit terms of a Dirac oscillator are not included, and are recorded as the remaining kinematic item.
- **Anchored vs moving partner.** Not a free choice: the founder's sideways oscillation is *between two quarks*, both of
  mass m_const, so both move. The anchored row is kept only as a lower bound.
- **α_geom's two corpus values** do not enter route (H); nothing to decide here. Left as a flag in the SS lane.

## 2. Rows verbatim (D-11)

```
per-mode ground-state spreads (units m_const c):
  NR anchored   sigma_p = 0.7071
  REL anchored  sigma_p = 0.7917
  NR u-d        sigma_p = 0.5000
  REL u-d       sigma_p = 0.5353

frame: the d's two edge lines meet at 60.5 deg (4243 assumed 90)

(G) geometry: radial direction tilted from the plane normal (NR modes)
  NR, sideways anchored, radial tilt  0 deg    R_u=0.8386 R_d=0.7903  g_A=1.3816 ( +8.3%)  mu_p=2.752 ( -1.5%)  mu_n=-1.808 ( -5.5%)
  NR, sideways anchored, radial tilt 45 deg    R_u=0.8406 R_d=0.7947  g_A=1.3857 ( +8.7%)  mu_p=2.755 ( -1.3%)  mu_n=-1.811 ( -5.3%)
  NR, sideways anchored, radial tilt 90 deg    R_u=0.8430 R_d=0.7997  g_A=1.3906 ( +9.0%)  mu_p=2.759 ( -1.2%)  mu_n=-1.815 ( -5.1%)
  NR, sideways u-d     , radial tilt  0 deg    R_u=0.8653 R_d=0.8327  g_A=1.4313 (+12.2%)  mu_p=2.794 ( +0.1%)  mu_n=-1.845 ( -3.6%)
  NR, sideways u-d     , radial tilt 45 deg    R_u=0.8668 R_d=0.8360  g_A=1.4344 (+12.5%)  mu_p=2.797 ( +0.1%)  mu_n=-1.848 ( -3.4%)
  NR, sideways u-d     , radial tilt 90 deg    R_u=0.8686 R_d=0.8396  g_A=1.4381 (+12.8%)  mu_p=2.800 ( +0.3%)  mu_n=-1.851 ( -3.3%)

(K) relativistic mode kinematics, real geometry (radial along the plane normal; tilt moves g_A by < 0.01)
  REL, sideways anchored                       R_u=0.8189 R_d=0.7674  g_A=1.3477 ( +5.7%)  mu_p=2.722 ( -2.5%)  mu_n=-1.786 ( -6.7%)
  REL, sideways u-d                            R_u=0.8502 R_d=0.8163  g_A=1.4058 (+10.2%)  mu_p=2.772 ( -0.8%)  mu_n=-1.829 ( -4.4%)

-> geometry: <= 0.8%.  relativity: -2.5%.  Direct reading of the founder's words (sideways = between two quarks, both
   move; relativistic): g_A = 1.406 (+10.2%).  Anchored partner (lower bound): 1.348 (+5.7%).  SU(6) alone: 1.667.
```

## 3. Result

**Under the founder's picture — ZBW breath of opposite charges, radial and u–d sideways, each mode at the ZBW
frequency (c04), in its ground state, relativistic kinematics, real frame geometry — g_A = 1.406 (+10.2%), with μ_p =
2.772 (−0.8%) and μ_n = −1.829 (−4.4%). Zero parameters.** The anchored-partner bound is 1.348 (+5.7%). SU(6) alone is
1.667 (+31%). The breath removes about two-thirds of the SU(6) excess, the moments are the best the corpus has produced
(4126: +7.4% / +4.5%), and the ratio μ_p/μ_n moves off −3/2 toward the measured −1.460 (−1.516 here) because R_u ≠ R_d.

**What the residual is.** g_A still needs ~20% more momentum spread per mode than the Compton ground state supplies.
None of the corrections tried moves it that far. The ~10% residual is recorded as open in TODO-4234-DELTA, not
attributed.

## 4. PD-008 — the convenient branch, marked

Headlining the anchored relativistic row (**1.348, +5.7%**) would be convenient and wrong: the founder's words make both
quarks move. The result is 1.406 (+10.2%), stated with its residual.
