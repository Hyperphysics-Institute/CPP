# r_p Refined: The Frequency Tension Survives; the Frame's Size Is the Unfixed Input Behind It

**Patch:** 4273. **Lanes:** EW → strong and foundations (4272 owed). **Session:** 239.
**Verify:** `series_standard_model/code/4273_rp_refined_rel_widths_and_exchange.py`.

## 1. What was refined

4272's r_p used non-relativistic widths and no Pauli term. Two refinements were added here:

- **Relativistic widths.** Each mode's ⟨x²⟩ is taken from its Salpeter ground state. The softer relativistic
  kinetic energy spreads the state in momentum and narrows it in position.
- **u–u exchange on positions.** The two ups' one-body density is the Slater density of their seat Gaussians. The
  Pauli term pushes them apart.

## 2. Rows verbatim (D-11)

```
  omega=1.0 NR   <x^2> anchored 0.500, u-d share 0.250   r_p no exchange 0.9202 fm ( +9.4%)   with u-u exchange 1.0099 fm (+20.1%)  [position overlap 0.505]
  omega=1.0 REL  <x^2> anchored 0.400, u-d share 0.218   r_p no exchange 0.8712 fm ( +3.6%)   with u-u exchange 0.9382 fm (+11.6%)  [position overlap 0.445]
  omega=1.2 NR   <x^2> anchored 0.417, u-d share 0.208   r_p no exchange 0.8771 fm ( +4.3%)   with u-u exchange 0.9468 fm (+12.6%)  [position overlap 0.454]
  omega=1.2 REL  <x^2> anchored 0.324, u-d share 0.178   r_p no exchange 0.8294 fm ( -1.4%)   with u-u exchange 0.8771 fm ( +4.3%)  [position overlap 0.383]
  omega=1.4 NR   <x^2> anchored 0.357, u-d share 0.179   r_p no exchange 0.8450 fm ( +0.5%)   with u-u exchange 0.8999 fm ( +7.0%)  [position overlap 0.410]
  omega=1.4 REL  <x^2> anchored 0.271, u-d share 0.150   r_p no exchange 0.7986 fm ( -5.0%)   with u-u exchange 0.8330 fm ( -0.9%)  [position overlap 0.328]
  omega=1.6 NR   <x^2> anchored 0.312, u-d share 0.156   r_p no exchange 0.8201 fm ( -2.5%)   with u-u exchange 0.8634 fm ( +2.7%)  [position overlap 0.369]
  omega=1.6 REL  <x^2> anchored 0.231, u-d share 0.129   r_p no exchange 0.7751 fm ( -7.8%)   with u-u exchange 0.7993 fm ( -5.0%)  [position overlap 0.280]
  omega=2.0 NR   <x^2> anchored 0.250, u-d share 0.125   r_p no exchange 0.7839 fm ( -6.8%)   with u-u exchange 0.8116 fm ( -3.5%)  [position overlap 0.299]
  omega=2.0 REL  <x^2> anchored 0.177, u-d share 0.100   r_p no exchange 0.7417 fm (-11.8%)   with u-u exchange 0.7538 fm (-10.4%)  [position overlap 0.201]

-> REL widths shrink r_p; the u-u exchange pushes the ups apart and grows it.  With both (the consistent state),
   r_p is closed near omega ~1.35-1.4 and is +11.6% at route (H); g_A (with the same exchange) asks ~1.12.
   The tension survives the refinements.  r_p is dominated by the frame term (sum e|r|^2 = 0.382 fm^2 of ~0.71),
   and SS-2's frame size comes from a force balance written with fractional charges (founder 4263: effective only).
```

## 3. Result

The two refinements pull in opposite directions. Relativistic widths shrink r_p by about 5%, and the exchange grows it
by 4–8%. In the consistent state (relativistic, with exchange, the same exchange g_A uses), **r_p closes near
ω ≈ 1.35–1.4 mc²/ħ and is 0.938 fm (+11.6%) under route (H)**, while g_A asks for about 1.12. The tension from 4272
survives.

**What drives it.** The frame term Σe|r|² (0.382 fm²) is more than half of r_p². That comes from SS-2's frame size
(u–u 1.071 fm, u–d 0.620 fm), which was set by a force balance with fractional charges (+2/3, −1/3) and SS-2's colour
coefficient. The founder has since said the fractional charges are effective only (4263). A smaller frame would lower
r_p at any ω and raise the u–u overlap, and with it the exchange. So r_p cannot arbitrate the frequency until the
frame size is derived again on the founder's present picture.

**PD-008.** Fitting ω and the frame scale together to g_A and r_p would be two parameters for two data points, so it
tests nothing, and it is not done. The frequency stays at route (H) on the E = ħω argument (4266). The r_p tension is
recorded as pointing at the frame size.

Note on method: the momentum-space Gaussians used for g_A's exchange (overlap 0.35) and the position-space Gaussians
used here (overlap 0.45) are not the same minimum-uncertainty state, because relativistic ground states are not
Gaussian. A single consistent non-Gaussian treatment is part of the filed item.

**Erratum (Patch 4284):** r_p here is converted to fm at m_q = m_p/3; with m_q fitted to μ_p (4268) it is ≈ 5–6% larger. See `series_standard_model/axiom_maturation/4284_critic_4276_two_quark_masses_rp_floor.md`.
