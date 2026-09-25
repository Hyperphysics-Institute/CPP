# The Folded-Square Frame: Size Fitted to r_p, g_A Predicted at −0.4% to −0.7% Across the Founder's Shape Range

**Patch:** 4276. **Lane:** EW → strong (TODO-4234-DELTA). **Session:** 239.
**Founder:** `founders_voice/4276_ruling_htetra_is_a_folded_square.md`.
**Verify:** `series_standard_model/code/4276_folded_square_frame.py`.

## 1. What the folded square fixes

The attractive pairs are the square's four **edges**, and the like-sign pairs are its two **diagonals**. For the
proton (ups on the two minus corners, d on the +qCP corner, +eCP corner open):

- **u–d is an edge**, of length a.
- **u–u is the minus diagonal**, between a (fully folded, a regular tetrahedron) and √2·a (flat square).
- **The d's diagonal mode** (4271) points across the plus diagonal to the open +eCP corner. Its direction, which
  4271 could only bracket, now follows from the fold.

So the founder's picture fixes the frame's **shape**, u–u/u–d ∈ [1, √2], but not its **size** a (4275). SS-2's
triangle (u–u/u–d = 1.73, a 120° apex) lies **outside** that range.

## 2. Rows verbatim (D-11)

```
ratio u-u/u-d=1.000: a (u-d) = 0.598 fm, u-u = 0.598 fm, fold angle 71 deg -> r_p=0.8410  g_A=1.2670 (-0.66%)  m_q(mu_p)=295.5  mu_n=-1.867 (-2.4%)  overlaps x 0.73 p 0.71
ratio u-u/u-d=1.200: a (u-d) = 0.509 fm, u-u = 0.611 fm, fold angle 97 deg -> r_p=0.8411  g_A=1.2681 (-0.57%)  m_q(mu_p)=295.7  mu_n=-1.866 (-2.5%)  overlaps x 0.72 p 0.69
ratio u-u/u-d=1.414: a (u-d) = 0.439 fm, u-u = 0.621 fm, fold angle 180 deg -> r_p=0.8407  g_A=1.2699 (-0.43%)  m_q(mu_p)=296.0  mu_n=-1.864 (-2.5%)  overlaps x 0.70 p 0.67

-> Across the founder's whole allowed shape range (regular to flat), fitting the size to r_p puts u-u at 0.60-0.62 fm
   and predicts g_A = 1.267-1.270 (-0.4% to -0.7%).  SS-2's 120-degree shape (u-u = 1.73 u-d) lies outside the range.
```

## 3. What I think

**(i) The folded square is the missing geometry.** It explains why the proton's hTetra is irregular: two ups pull the
minus diagonal closed while the d pulls the plus diagonal closed. It bounds the shape to the range regular-to-flat,
and it turns the d's diagonal mode into a determined direction.

**(ii) One fit and one prediction.** a is not yet derivable, so it is fitted to r_p (one number). Across the whole
allowed shape range the fit lands at **u–u ≈ 0.60–0.62 fm**, with u–d 0.44–0.60 fm, and g_A is then predicted at
**1.267–1.270 (−0.4% to −0.7%)**. μ_p fixes m_q ≈ 296 MeV, and μ_n is −2.4% to −2.5%. The prediction is insensitive
to the unknown fold, which is why it is worth stating.

**(iii) Still missing, and each item shifts the fitted a (filed from 4275):**
- *The vertex CPs' own swing.* The founder did not give an amplitude. Any swing adds to r_p, so a would shrink.
- *The shorter inner swing.* It makes the breath lopsided outward, adding to r_p and raising momentum slightly.
- *The large overlaps (≈ 0.7).* These keep the Gaussian exchange at its roughest.

Each pulls g_A somewhat further down, so the −0.5% should be read as "within about a percent", not as a precision
figure.

## 4. PD-008

This is convenient: the prediction lands close. It rests on one fitted size, and the three missing effects are named
beside it. The earlier 4274 anchor (u–d = 0.364 fm) stays withdrawn. Here a comes from r_p, not from a lattice
length.

**Erratum (Patch 4284, PD-008 critic):** the r_p fit converts to fm at m_q = m_p/3 while the same row reports m_q ≈ 296 MeV from μ_p; r_ZBW = ħ/m_q c takes one mass (4240, 4272). With one m_q, **no frame size fits r_p** (floor +1.0%, collapsed frame), and these rows sit at r_p ≈ +5.8%. The g_A values are right for these geometries, but r_p does not select them: over the allowed range g_A spans 1.242–1.282 (−2.6% to +0.5%) and is **not predicted**. μ_n −2.2% to −2.6% is robust. See `series_standard_model/axiom_maturation/4284_critic_4276_two_quark_masses_rp_floor.md`.
