# g_A Residual, Lever 1: Dirac Spin–Orbit From the Breath's Well Does Not Close It

**Patch:** 4259. **Lane:** EW → strong (TODO-4234-DELTA). **Session:** 239.
**Verify:** `series_standard_model/code/4259_gA_lever1_dirac_spin_orbit.py`.
**Input, unchanged:** the founder's mode rule (`founders_voice/4243`, `4244`) and 4244's stiffnesses — each mode at
the Compton frequency; u: radial + one u–d; d: radial + two u–d; no u–u.

## 1. The question

4244 treated each quark as a free spin-½ at the momentum its breath gives it: R = 1/3 + (2/3)⟨m/E⟩, the Wigner
dilution of a moving spin, with a spinless Salpeter ground state per mode. g_A = 1.406 needs R about 10% lower
(mean R 0.765 against 0.84). Lever 1: does the *binding field itself*, solved as a Dirac equation with its lower
component, dilute the spin further? The answer depends on how the well enters the Dirac equation, so every standard
structure was solved, each matched to the same non-relativistic well: scalar (acts on the mass), vector (time
component, as an electric potential enters), equal mixture S = V, and the Moshinsky Dirac oscillator (the "Dirac
harmonic oscillator", whose NR limit is the oscillator plus a full-strength L·S term).

Two method points. (a) The u–d sideways mode is a relative coordinate of two equal masses; mapped to one body it is
exactly 2 × [√(p²+1) − 1 + ⅛x²], so a one-body particle in K = ¼ has 4244's eigenfunctions. (b) The d's two sideways
lines (60.5°) are taken as one quadratic form with principal stiffnesses (1 ± cos 60.5°)/4, not as independent
momenta summed; rebuilt that way the kinematic baseline moves by −0.6% (row 0), so it does not bear on the residual.

The moment is computed as ⟨βΣ⟩ in the same state — the Gordon spin magnetisation, 4242's tie (1+R)/2, which holds
identically here (f² + g² = 1). No convection current, per 4242.

## 2. Rows verbatim (D-11)

```
target: g_A = 1.2754 <=> mean R = 0.7652 (SU(6) 5/3 x R)

(0) kinematic baseline, free-spinor R on the Salpeter ground state, quadratic-form geometry:
  kinematic (4244 treatment)               R_u=0.8462 R_d=0.8086  g_A=1.3979 ( +9.6%)  mu_p=2.765 ( -1.0%)  mu_n=-1.822 ( -4.7%)
    [4244, independent-mode sum: g_A = 1.4058; the joint quadratic form moves it by -0.6%]

(1) Dirac equation in the breath's well, lower component included (basis n: u 24, d 13; converged to 1e-4):
  scalar (E_u=1.593, E_d=1.753)            R_u=0.8955 R_d=0.8775  g_A=1.4865 (+16.5%)  mu_p=2.842 ( +1.8%)  mu_n=-1.884 ( -1.5%)
  S=V    (E_u=1.651, E_d=1.827)            R_u=0.8541 R_d=0.8298  g_A=1.4155 (+11.0%)  mu_p=2.779 ( -0.5%)  mu_n=-1.839 ( -3.9%)

(2) vector (time-component) well: most localised state with E in (0.5, 3) -- <r^2> grows with the basis (Klein):
    u, n=12: E=1.762  <r^2>=1.89   (S=V ground state <r^2> ~ 1.5)
    u, n=16: E=2.132  <r^2>=4.18   (S=V ground state <r^2> ~ 1.5)
    -> no bound state. A no-pair (positive-energy) projection is the class row (0) approximates; not computed here.

(3) Dirac oscillator, Gaussian state (analytic: E^2 = 1 + 2 sum w_i under one sign; E = 1, lower comp. 0, the other):
  DO, sign giving lower component 0        R_u=1.0000 R_d=1.0000  g_A=1.6667 (+30.7%)  mu_p=3.002 ( +7.5%)  mu_n=-2.001 ( +4.6%)
  DO, sign giving E^2 = 1 + 2 sum w        R_u=0.6667 R_d=0.6335  g_A=1.1000 (-13.7%)  mu_p=2.496 (-10.6%)  mu_n=-1.646 (-14.0%)
    (the DO's NR limit carries L.S at the full oscillator strength and an infinitely degenerate E = m family;
     the Gaussian is not its ground state for the second sign)

-> No Lorentz structure of the breath's well closes the residual at zero parameters. Scalar raises g_A (+16.5%),
   S=V leaves it (+11.0%), vector does not bind (a no-pair projection is the class row (0) approximates; not computed here). Only the Moshinsky oscillator crosses
   the target, and it overshoots to 1.100 (-13.7%); landing on 1.275 would need a tuned coupling strength -- a fit.
```

## 3. Result

**Lever 1 is closed: no Lorentz structure of the breath's well supplies the residual at zero parameters.**

- **Scalar** moves g_A the wrong way (1.487, +16.5%): a well that adds to the mass shrinks the lower component.
- **S = V** leaves it where it was (1.416, +11.0%).
- **Vector**, the structure an electric breath would suggest, has **no bound state** — the lowest localised state
  spreads as the basis grows (Klein). A no-pair (positive-energy-projected) vector well is the class 4244's
  free-spinor treatment approximates; it was not solved separately here (filed as a critic item, below).
- **The Moshinsky oscillator** is the only structure that crosses the target, and it straddles it: one sign gives
  no lower component (5/3), the other gives 1.100 (−13.7%) with μ_p −10.6%. Hitting 1.275 would require its
  coupling at a tuned fraction of full strength. That is a fit, and the full-strength L·S it carries has no
  counterpart in the founder's picture.

The residual therefore is not relativistic spin–orbit from the binding. Two levers remain untried: the d's internal
linear −eCP oscillator acting on its core, and excited-mode admixture.

## 4. PD-008 — the convenient branch, marked

The convenient reading is the Moshinsky oscillator: it is the only row that reaches the target, and "a partial
Dirac-oscillator coupling" would sound like physics. It is a one-parameter fit, and the oscillator's structure is
not the founder's. Not adopted.

## 5. Owed

Critic item (TODO-4234-DELTA): solve the no-pair-projected vector well and confirm it stays within ~1% of row (0).
The founder's electric breath is most naturally a vector coupling, so this is the one Dirac branch not computed to
the end. Filed in `todolist.md` in this patch.
