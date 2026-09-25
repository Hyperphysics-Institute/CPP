# PD-008 Critic of Session 239: 4276's r_p Fit Used Two Quark Masses; With One, No Frame Size Fits r_p and g_A Is Not Pinned

**Patch:** 4284. **Lane:** EW → strong (TODO-4234-DELTA, critic item). **Session:** 240.
**Verify:** `series_standard_model/code/4284_critic_one_mq_rp_floor_pauli.py` (reuses 4276's script verbatim).
**Critiques:** 4276 (and the same step in 4273, 4274), 4274 §1.2, 4266 (iv).

## 1. The finding

4272 §1 fixes the ZBW orbit radius as **r_ZBW = ħ/mc**, with m the quark mass. Resolving the symbol (D-7), the same
m_q sets the length unit and the moments. Rows 4273, 4274 and 4276 use **two**:
- m_q = m_p/3 = 312.8 MeV to convert r_p into fm (`mq=938.272/3; rZ=197.327/mq`), and
- m_q ≈ 296 MeV, which they report as fixed by μ_p in the same row.

With one m_q throughout, the model has two unknowns, the frame size t = a/r_ZBW and m_q. g_A depends on t alone
(4268). μ_p fixes m_q ≈ 293–297 MeV across the range, and r_p then follows. **No t and no allowed shape reaches
r_p.** The floor is **+1.0%**, at a collapsed flat frame (t → 0, u–u overlap 0.90). At 4276's own geometries
(t = 0.95, 0.81, 0.70) r_p is **+5.8% to +5.9%**.

So 4276's statement *"size fitted to r_p, g_A predicted 1.267–1.270"* does not survive. The g_A values are
correct **for those geometries**, but r_p does not select them. Over the allowed range, g_A spans **1.242–1.282
(−2.6% to +0.5%)** and is not pinned. μ_n is robust at **−2.2% to −2.6%**.

## 2. Rows verbatim (D-11)

```
(A) 4276's length unit (m_q = m_p/3), shape u-u/u-d = 1.2 (4276's fitted a = 0.509 fm)
  a=0.350 fm  r_p=0.8219  g_A=1.2603 (-1.19%)  overlap p=0.807
  a=0.420 fm  r_p=0.8293  g_A=1.2637 (-0.92%)  overlap p=0.759
  a=0.509 fm  r_p=0.8415  g_A=1.2684 (-0.55%)  overlap p=0.691
  a=0.600 fm  r_p=0.8562  g_A=1.2731 (-0.18%)  overlap p=0.616
  a=0.700 fm  r_p=0.8788  g_A=1.2786 (+0.25%)  overlap p=0.531
  a=0.850 fm  r_p=0.9196  g_A=1.2869 (+0.90%)  overlap p=0.408

(C) u, no exchange: Gaussian R_u=0.7901  true-distribution R_u=0.7913  -> g_A shift +0.0016  (kurtosis pa 3.16, Gaussian 3)
(B) exchange off: g_A = 1.3118 (Gaussian u), 1.3134 (true u);  4276 row with exchange: 1.2681

(D) ONE m_q throughout (r_ZBW = hbar c/m_q, m_q from mu_p).  t = u-d edge / r_ZBW
ratio u-u/u-d = 1.000
  t=0.05  m_q(mu_p)= 292.7 MeV  r_p=0.8718 fm (+3.7%)  g_A=1.2418 (-2.63%)  mu_n=-1.872 (-2.2%)  overlap p=0.95
  t=0.20  m_q(mu_p)= 293.1 MeV  r_p=0.8702 fm (+3.5%)  g_A=1.2454 (-2.35%)  mu_n=-1.871 (-2.2%)  overlap p=0.94
  t=0.40  m_q(mu_p)= 293.8 MeV  r_p=0.8692 fm (+3.4%)  g_A=1.2516 (-1.87%)  mu_n=-1.870 (-2.3%)  overlap p=0.90
  t=0.60  m_q(mu_p)= 294.5 MeV  r_p=0.8729 fm (+3.8%)  g_A=1.2575 (-1.40%)  mu_n=-1.869 (-2.3%)  overlap p=0.85
  t=0.80  m_q(mu_p)= 295.1 MeV  r_p=0.8812 fm (+4.8%)  g_A=1.2630 (-0.97%)  mu_n=-1.868 (-2.4%)  overlap p=0.78
  t=1.00  m_q(mu_p)= 295.7 MeV  r_p=0.8935 fm (+6.3%)  g_A=1.2686 (-0.53%)  mu_n=-1.867 (-2.4%)  overlap p=0.69
ratio u-u/u-d = 1.200
  t=0.05  m_q(mu_p)= 293.1 MeV  r_p=0.8616 fm (+2.5%)  g_A=1.2446 (-2.41%)  mu_n=-1.870 (-2.2%)  overlap p=0.93
  t=0.20  m_q(mu_p)= 293.5 MeV  r_p=0.8616 fm (+2.5%)  g_A=1.2480 (-2.15%)  mu_n=-1.870 (-2.3%)  overlap p=0.91
  t=0.40  m_q(mu_p)= 294.2 MeV  r_p=0.8642 fm (+2.8%)  g_A=1.2549 (-1.61%)  mu_n=-1.868 (-2.3%)  overlap p=0.86
  t=0.60  m_q(mu_p)= 295.0 MeV  r_p=0.8733 fm (+3.9%)  g_A=1.2618 (-1.07%)  mu_n=-1.867 (-2.4%)  overlap p=0.79
  t=0.80  m_q(mu_p)= 295.8 MeV  r_p=0.8893 fm (+5.8%)  g_A=1.2684 (-0.55%)  mu_n=-1.866 (-2.5%)  overlap p=0.69
  t=1.00  m_q(mu_p)= 296.5 MeV  r_p=0.9106 fm (+8.3%)  g_A=1.2749 (-0.04%)  mu_n=-1.865 (-2.5%)  overlap p=0.59
ratio u-u/u-d = 1.414
  t=0.05  m_q(mu_p)= 293.6 MeV  r_p=0.8492 fm (+1.0%)  g_A=1.2481 (-2.14%)  mu_n=-1.868 (-2.3%)  overlap p=0.90
  t=0.20  m_q(mu_p)= 294.0 MeV  r_p=0.8511 fm (+1.2%)  g_A=1.2516 (-1.87%)  mu_n=-1.868 (-2.4%)  overlap p=0.88
  t=0.40  m_q(mu_p)= 294.7 MeV  r_p=0.8605 fm (+2.3%)  g_A=1.2584 (-1.33%)  mu_n=-1.867 (-2.4%)  overlap p=0.82
  t=0.60  m_q(mu_p)= 295.6 MeV  r_p=0.8787 fm (+4.5%)  g_A=1.2661 (-0.73%)  mu_n=-1.865 (-2.5%)  overlap p=0.72
  t=0.80  m_q(mu_p)= 296.5 MeV  r_p=0.9022 fm (+7.3%)  g_A=1.2742 (-0.09%)  mu_n=-1.864 (-2.6%)  overlap p=0.60
  t=1.00  m_q(mu_p)= 297.4 MeV  r_p=0.9367 fm (+11.4%)  g_A=1.2822 (+0.53%)  mu_n=-1.862 (-2.6%)  overlap p=0.48

(E) Pauli kinetic energy per u (units m_q c^2), shape 1.2, lengths in r_ZBW
  u-u=0.48  overlap=0.86  pair Pauli excess=+0.3528
  u-u=0.72  overlap=0.79  pair Pauli excess=+0.3071  dE/d(u-u)=-0.191 m_q c^2/r_ZBW
  u-u=0.96  overlap=0.69  pair Pauli excess=+0.2601  dE/d(u-u)=-0.196 m_q c^2/r_ZBW
  u-u=1.20  overlap=0.59  pair Pauli excess=+0.2147  dE/d(u-u)=-0.189 m_q c^2/r_ZBW
  u-u=1.44  overlap=0.48  pair Pauli excess=+0.1698  dE/d(u-u)=-0.187 m_q c^2/r_ZBW
  u-u=1.80  overlap=0.34  pair Pauli excess=+0.1081  dE/d(u-u)=-0.171 m_q c^2/r_ZBW

-> (D): with one m_q, r_p >= +1.0% at every size and shape (floor at a collapsed frame); 4276's rows sit at +5% to +6%.
   g_A then depends on t alone and spans -2.6% .. +0.5% over the allowed range; it is not pinned by r_p.
```

## 3. What the other checks say

**(A) The size lever.** At 4276's unit, a 2.4× change in a moves r_p only from 0.82 to 0.92 fm, because r_p is
carried by the swing widths, not the frame. So fitting a to r_p is a long lever, about 0.2% of g_A per 1% of r_p.
A few-percent inconsistency in r_p's length unit therefore moves the fitted a by a factor of order one. That is
what happened.

**(B) The exchange carries the whole closure.** With the u–u exchange removed, g_A = 1.312. The Pauli term at
overlap 0.69 moves it to 1.268 (−3.4%), amplified by 1/(1−s²) ≈ 1.9. Whatever pins the frame pins g_A.

**(C) The Gaussian approximation is not the problem.** The true route-(H) momentum distribution (kurtosis 3.16)
shifts g_A by +0.0016.

**The Slater sign was checked, not assumed.** 4261 (C) identifies colour with the vertex, so the vertex-attached
breath carries the colour label and is antisymmetrised once. Symmetric spin–flavour × antisymmetric vertex-breath is
antisymmetric in total, and SU(6)'s 5/3 is untouched. (A separate colour factor would make the Slater minus a double
count; on the founder's story there is none.)

**The missing effects make it worse.** 4276 §3(iii) lists the vertex CPs' own swing and the shorter inner swing.
Both *add* to r_p, so they raise the +1.0% floor. Within this model the r_p gap cannot close by adjusting the frame.
It needs something that shrinks the quark swings themselves, or a change in the r_p formula (centroid origin,
point CPs, SS-2's form, all listed at 4274 §PD-008). Nothing on file supplies either.

## 4. 4274 §1.2: the conclusion stands, the reason given does not

4274 dropped SS-2's +ħc/r as the breath's kinetic energy "counted twice". They are not the same energy. SS-2's term
is the pair's localisation energy at separation r and depends on r. Under route (H) the breath width is set by m_q
alone and does not depend on r, so the breath's kinetic energy exerts **no force on the frame**. The correct
statement is this: once the widths are fixed by route (H) and exceed the frame (w ≈ r_ZBW > a), the pair is not
localised to r, so there is no ħc/r term to keep. The consequence (no kinetic repulsion of SS-2's form) is the
same. The argument should cite r-independence, not double counting.

**One r-dependent kinetic term does survive: the u–u Pauli energy** (rows (E)). The antisymmetrised pair's excess
kinetic energy falls as the ups separate, at an almost constant ≈ 0.19 m_q c²/r_ZBW, which is about 84 MeV/fm at
m_q = 296 MeV. That is a repulsion on the minus diagonal, about a tenth of a QCD-scale string tension and far below
SS-2's ħc/r (≈ 550 MeV/fm at 0.6 fm). It is a **candidate** for what holds the diagonal open. It cannot be balanced
yet, because no bond law for the hTetra's edges is on file. Filed as a lead, not a result.

## 5. 4266 (iv): the rejection stands on one reason, not three

- **Reason 1 is decisive by itself.** The ω = 2.007 closure used the mode set the founder corrected at 4262. With the
  ruled set, Schrödinger's 2mc²/ħ gives 1.191 (−6.6%).
- **Reason 2** (iii)'s beat-versus-swing argument, is sound but not needed.
- **Reason 3 is void.** Per 4268, m_q is fitted to μ_p, so μ_p's residual cannot count against a branch.

## 6. PD-008 (my own branches)

- **Convenient branch taken, and marked.** Reporting that g_A's allowed span (−2.6% to +0.5%) *contains* the
  measured value is the convenient framing. The honest content: once r_p cannot select t, g_A is **unpredicted** at
  the ±1.5% level, and the model misses r_p by at least 1%.
- **Branch not taken.** Fitting m_q to r_p instead of μ_p (the floor reaches r_p at m_q ≈ 301 MeV, collapsed frame)
  would trade the r_p miss for a μ_p miss of about +2%. That is not better, and it is recorded here so it is not
  rediscovered as a fix.
- **What would change this.** A derivation of the u swing widths that differs from route (H) (smaller widths lower
  r_p), or a derivation of m_q (4268 item (iii)). Either is a physics question, not a bookkeeping one.
- **Not done in this patch:** the 4262 / 4271 critic (modes adopted from founder pictures). Filed.

**Symbol trail (D-7, D-10).** 4240 lines 20–22 resolve r_ZBW = ħc/m_const and record m_const as *assigned* in SS-2
(m_p/3), not derived. 4268 then fits **the same quantity** to μ_p (*"4.2% below SS-2's assigned m_p/3"*) and names one
open item for it, *"a CPP derivation of the up quark's mass"*. Neither defines a second mass for the orbit radius.
So the corpus has one symbol, re-fitted in the moments and left at its assigned value in the length unit from 4272
on. For the next context window: press this reading. If the founder's picture distinguishes the mass that sets the
swing radius from the mass in the magneton, that is an axiom-level distinction and would reopen 4276 as stated.
