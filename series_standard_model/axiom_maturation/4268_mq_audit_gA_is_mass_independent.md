# m_q Audit: g_A Does Not Depend on m_q; Its +2.7% Is Its Own Residual; m_q Fixes μ_p and Predicts μ_n

**Patch:** 4268. **Lane:** EW → strong (TODO-4234-DELTA item (iii)). **Session:** 239.
**Verify:** `series_standard_model/code/4268_mq_audit_and_the_mu_prediction.py`.

## 1. Searched (D-1, D-10)

`m_const` is **assigned, not derived**:
- SI-1 row M9 records it as *"ASSIGNED m_p/3 in SS-2"*, corrected from DERIVED at Patch 4240.
- SS-2's μ_p = 2.789 is the non-relativistic quark model with m_u, m_d = 336, 340 MeV. It carries no motion
  reduction.
- The SS-2 development transcript's *"r_ZBW/l_unit = Λ_QCD/m_const … derivable"* is circular, because r_ZBW is
  defined as ħc/m_const.
- OP-SS-1 and SS-1's glossary say the u/d constituent mass is "entirely ZBW-driven", without a number.

No route on file fixes m_q.

## 2. A correction to 4261 §3 and 4262 §3(iv)

Those sections called the g_A residual "really" the m_q tension. **That was wrong for g_A.** Route (H) works in units
of m_q c. The breath runs at ω = m_q c²/ħ (4266), so every mode's momentum spread is fixed *in those units*, and R_u,
R_d and g_A are the same for any m_q. m_q enters only the moments, as μ = (M_N/m_q)·S.

The accurate statement is this. At fixed m_q, anything that lowers g_A lowers μ_p with it, which is what those
sections saw. But once the motion is fixed at zero parameters, as it now is, **the g_A residual (+2.7%) belongs to
the motion itself, and no m_q removes it.** An erratum line is appended to both fragments.

## 3. Rows verbatim (D-11)

```
  (1) SS-2: m_q = m_p/3 (assigned, M9)       m_q= 312.8 MeV  g_A=1.3095 (+2.7%)  mu_p=2.675 ( -4.2%)  mu_n=-1.805 ( -5.7%)  mu_n/mu_p=-0.6746 (meas -0.6850)
  (2) m_q fitted to mu_p                     m_q= 299.6 MeV  g_A=1.3095 (+2.7%)  mu_p=2.793 ( -0.0%)  mu_n=-1.884 ( -1.5%)  mu_n/mu_p=-0.6746 (meas -0.6850)
  NRQM reference (R_u = R_d = 1, m_q = m_p/3): mu_p = 2.780, g_A = 1.6667 (SS-2's 2.789 used m_u, m_d = 336, 340)

-> g_A is m_q-independent: its +2.7% is a residual of the motion, not of the mass.  Fitting m_q to mu_p (1 number)
   leaves mu_n as a prediction (-1.5%); the ratio mu_n/mu_p, which no m_q can change, is -1.5% off as well.
```

## 4. Result

With the ruled-picture state (4262, exchange included):

- **g_A = 1.310 (+2.7%)**, independent of m_q.
- **μ_p fixes m_q = 299.6 MeV**, 4.2% below SS-2's assigned m_p/3.
- **μ_n is then a prediction:** −1.884 (−1.5%).
- **μ_n/μ_p = −0.675** against −0.685 measured (−1.5%), which no choice of m_q can change.

So the model fits 3 observables with 1 number (m_q), with residuals of +2.7% in g_A and −1.5% in μ_n.

What still moves g_A: the u–d exchange (owed), and the frame geometry the exchange overlap depends on (SS-2's
0.620/1.071 fm). What would fix m_q: a CPP derivation of the up quark's mass from its structure (+qCP in a polarised
eDP sphere, founders_voice/4263; c04's cloud resonance). That stays filed as item (iii).

## 5. PD-008

Quoting "3 observables, 1 parameter" is the convenient framing. The honest count: m_q is fitted, and g_A and μ_n are
the two predictions. Both are recorded with their residuals.


**Erratum (Patch 4271):** μ_n in this fragment was computed by flavour; in the neutron's own frame (the proton's mirror) R is assigned by role. Corrected, the ruled-state prediction is μ_n = −1.871 (−2.2%) at m_q fitted to μ_p. See `series_standard_model/axiom_maturation/4271_neutron_mirror_mu_n_correction_free_nucleon.md` §2.
