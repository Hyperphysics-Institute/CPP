# A Second Observable for the Breath's Frequency: r_p Asks for 1.4, g_A for 1.1; and c04's Mass Proof Is Broken

**Patch:** 4272. **Lanes:** foundations (TODO-4264-PASSTHROUGH step 2) and EW → strong. **Session:** 239.
**Verify:** `series_standard_model/code/4272_breath_frequency_second_observable_rp.py`.

## 1. Why the c04 sweep started here

The c04 corrections (sweep step 2) turned on the frequency question 4266 left. Under R-ZBW-PASS-THROUGH the CP
crosses its partner at top speed. If that speed is c, the lattice limit, then **frequency × amplitude = c**, so the
choice of frequency *is* the choice of the swing's size. The corpus holds both sizes:

- **SS-2's orbit radius r_ZBW = ħ/mc** gives ω = mc²/ħ: route (H).
- **c04's resonance radius r_th = ħ/2mc** gives ω = 2mc²/ħ. That is exactly Schrödinger's triad: amplitude ħ/2mc,
  frequency 2mc²/ħ, speed c. At that frequency the harmonic ground-state width is exactly r_th.

This recasts 4266 §3(iii). Schrödinger's frequency is not only a beat: with c04's radius and a speed-c crossing it is a
genuine swing frequency. The g_A number cannot settle the choice alone, but the proton charge radius measures the
breath's *width* directly, so it is a second, independent observable.

## 2. Rows verbatim (D-11)

```
SS-2 check (uniform s^2 = r_ZBW^2, delta = 0): r_p = 0.8834 fm (SS-2: 0.883); measured 0.8409

  omega = 1.0 mc^2/hbar:  g_A = 1.2952 ( +1.6%)   r_p = 0.9202 fm ( +9.4%)   [u-u overlap 0.350]
  omega = 1.2 mc^2/hbar:  g_A = 1.2626 ( -1.0%)   r_p = 0.8771 fm ( +4.3%)   [u-u overlap 0.284]
  omega = 1.4 mc^2/hbar:  g_A = 1.2342 ( -3.2%)   r_p = 0.8450 fm ( +0.5%)   [u-u overlap 0.227]
  omega = 1.6 mc^2/hbar:  g_A = 1.2090 ( -5.2%)   r_p = 0.8201 fm ( -2.5%)   [u-u overlap 0.181]
  omega = 2.0 mc^2/hbar:  g_A = 1.1655 ( -8.6%)   r_p = 0.7839 fm ( -6.8%)   [u-u overlap 0.113]

  omega that closes g_A: 1.12 mc^2/hbar;  omega that closes r_p: 1.43 mc^2/hbar

-> No single frequency closes both.  Route (H) (omega = 1): g_A +1.6%, r_p +9.4%.  Schrodinger's triad (omega = 2):
   g_A -8.6%, r_p -6.8%.  The two observables ask for 1.1 and 1.4 -- a tension, recorded, not resolved.
```

## 3. Result

**No single frequency closes both observables.** g_A (free-nucleon ruled state) asks for ω ≈ 1.12 mc²/ħ, and r_p
asks for ≈ 1.43.

- **Route (H):** g_A +1.6%, but r_p = 0.920 fm (+9.4%), worse than SS-2's +5.0%. The founder's modes add width
  (three modes per u, four for a free-proton d) where SS-2 smeared once at r_ZBW².
- **Schrödinger's triad:** g_A −8.6%, r_p −6.8%.

The r_p model is coarse: non-relativistic widths, the d's eCP at δ = 0, no exchange correction to positions, and
SS-2's frame distances. Its +9.4% should be read as "route (H)'s breath is too wide for r_p by several percent", not
as a precise number. The tension is recorded, not resolved.

**PD-008.** The r_p value 1.43 is close to √2, and g_A's 1.12 is not. Quoting "ω ≈ √2 mc²/ħ fits r_p" would be
numerology, and it is not adopted. Neither is splitting the difference.

## 4. c04's mass proof does not hold as written (found on the sweep)

c04 Proposition "Rest mass from Compton standing wave", proof, eq. (E-cloud):
E = N_Planck·ħ/(2t_P) with N_Planck = ν_P/ν_C and ν_P = 1/(2t_P). That gives E = (ν_P/ν_C)·ħν_P = **ħν_P²/ν_C**, not
ħν_C. The displayed intermediate expression (1/(2t_Pν_C))·(ħ/2t_P)·(1/(2t_P)) is not even dimensionally an energy.
The conclusion mc² = ħν_C is therefore asserted, not derived. Separately, c04 pairs ħ with 1/T (T_C = 2r_th/c =
ħ/mc²), where Planck's E = hν pairs h with 1/T (4266).

Both go to the c04 fix, which is a `.tex` edit plus a recompile by the founder. The fix has to choose the swing size
(r_th or r_ZBW), and §3 shows that the observables do not yet agree on it. So the c04 text correction is held until
the frequency tension is examined further. The proof error is filed now, so it is not lost.
