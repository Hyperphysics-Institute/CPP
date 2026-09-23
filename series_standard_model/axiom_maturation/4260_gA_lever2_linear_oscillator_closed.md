# g_A Residual, Lever 2: The Down Quark's Linear Oscillator Cannot Supply It

**Patch:** 4260. **Lane:** EW → strong (TODO-4234-DELTA). **Session:** 239.
**Verify:** `series_standard_model/code/4260_gA_lever2_linear_oscillator_recoil.py`.

## 1. The object, located first (D-3, D-7)

The object is described in `founders_vision.md` §6 and SS-2 §6. The d is an up core (its +qCP with its own
orbital spin ZBW) that has captured an electron. The −eCP binds to the core as a **linear** hDP ZBW oscillator
passing through it. The electron's orbital spin DP left as the neutrino. The u has no linear oscillator.

Two consequences follow from that picture. First, a linear oscillation carries no angular momentum, so the
oscillator cannot dilute the d's spin directly. It can act on g_A only through the **core's recoil**: extra core
momentum along the line, which enters 4244's free-spinor R like any other motion. Second, it reaches only the
d, and the d carries one fifth of g_A: g_A = (4/3)R_u + (1/3)R_d. Even infinite recoil (R_d → 1/3) leaves
g_A ≥ 1.245.

## 2. Rows verbatim (D-11)

```
baseline (4244 REL u-d): R_u=0.8502 R_d=0.8163 g_A=1.4057   <E_d>=1.445 m_const
d's share of g_A: (1/3)R_d of (5/3)R -- the lever acts on 1/5 of g_A
R_d needed for g_A = 1.2754 with R_u fixed: 0.4254   (floor R_d -> 1/3 at infinite recoil gives g_A = 1.2447)

recoil spread s (Gaussian along the line, units m_const c) -> R_d, g_A, core energy, tied moments:
  s=0.000 (     0 MeV)  R_d=0.8163  g_A=1.4057 (+10.2%)  <E_d>= 1.445 m_const (  452 MeV)  mu_p=2.772 ( -0.8%)  mu_n=-1.829 ( -4.4%)
  s=0.013 (     4 MeV)  R_d=0.8163  g_A=1.4057 (+10.2%)  <E_d>= 1.445 m_const (  452 MeV)  mu_p=2.772 ( -0.8%)  mu_n=-1.829 ( -4.4%)
  s=0.100 (    31 MeV)  R_d=0.8154  g_A=1.4054 (+10.2%)  <E_d>= 1.448 m_const (  453 MeV)  mu_p=2.771 ( -0.8%)  mu_n=-1.828 ( -4.4%)
  s=0.500 (   156 MeV)  R_d=0.7961  g_A=1.3990 ( +9.7%)  <E_d>= 1.519 m_const (  475 MeV)  mu_p=2.768 ( -0.9%)  mu_n=-1.815 ( -5.1%)
  s=1.000 (   313 MeV)  R_d=0.7561  g_A=1.3856 ( +8.6%)  <E_d>= 1.709 m_const (  534 MeV)  mu_p=2.762 ( -1.1%)  mu_n=-1.789 ( -6.5%)
  s=2.000 (   626 MeV)  R_d=0.6817  g_A=1.3608 ( +6.7%)  <E_d>= 2.268 m_const (  709 MeV)  mu_p=2.749 ( -1.6%)  mu_n=-1.739 ( -9.1%)
  s=4.000 (  1251 MeV)  R_d=0.5898  g_A=1.3302 ( +4.3%)  <E_d>= 3.645 m_const ( 1140 MeV)  mu_p=2.734 ( -2.1%)  mu_n=-1.678 (-12.3%)
  s=6.000 (  1877 MeV)  R_d=0.5384  g_A=1.3131 ( +3.0%)  <E_d>= 5.139 m_const ( 1607 MeV)  mu_p=2.725 ( -2.4%)  mu_n=-1.643 (-14.1%)
  s=8.000 (  2502 MeV)  R_d=0.5062  g_A=1.3023 ( +2.1%)  <E_d>= 6.658 m_const ( 2082 MeV)  mu_p=2.720 ( -2.6%)  mu_n=-1.622 (-15.2%)

closing value: s = 20.31 m_const c = 6353 MeV along the line; <E_d> = 16.36 m_const = 5117 MeV (M_N = 939)
  tied moments there: mu_p=2.706 ( -3.1%)  mu_n=-1.568 (-18.0%)

scale on file: the d-u mass difference, 2.5 MeV (founders_vision s6: the energy of forming the d from the u) to
4 MeV (SS-2's 340-336); recoil at that scale (s = 0.013 row) moves g_A by < 1e-4. (A deeply bound oscillator's kinetic
energy is not capped by the net mass difference, so the exclusion rests on the closing row, not on this scale.)
eCP trading onto a u (f_trade ~ 4%, founders_vision 10 Apr 2026): bound even at infinite recoil, |dg_A| <= (4/3) f (R_u - 1/3) = 0.028

-> Lever 2 cannot close the residual: it reaches only the d's 1/5 share of g_A, so closing needs a d core whose
   mean energy is ~5 M_N, and mu_n falls 18% below measured there; the scale on file moves g_A by < 1e-4.
```

## 3. Result

**Lever 2 is closed.** With R_u held at 4244's value, closing the residual needs R_d = 0.425. The recoil that
gives this is ~6 GeV along the line, and the d core's mean energy is then 16 m_const ≈ 5.4 M_N. At that point
μ_n = −1.568, 18% below measured. The scale the corpus attaches to the linear oscillator is the u→d mass
difference, 2.5–4 MeV. Recoil at that scale moves g_A by less than 1e−4.

That scale is not the exclusion. A deeply bound oscillator's kinetic energy is not capped by the net mass
difference. The exclusion rests on the closing row: the energy it needs, and the moment it breaks.

eCP trading onto a u (f_trade ≈ 4%, founders_vision 10 Apr 2026) is bounded at |Δg_A| ≤ 0.028 even at infinite
recoil. That is too small to close a 0.13 gap.

**What this leaves.** Levers 1 and 2 are both closed. The u's R carries four fifths of g_A, so the residual has
to come from the u's own modes (the radial and one u–d breath) or from something acting on both quarks alike.
Lever 3, excited-mode admixture, is of that kind and is the remaining untried item.

## 4. PD-008 — the convenient branch, marked

The convenient reading would be to cite the neutron-radius displacement δ (SS-2, fitted) as evidence of a strong
linear oscillation and let it carry the residual. δ is a fitted parameter, and it concerns position, not
momentum. No row here uses it.
