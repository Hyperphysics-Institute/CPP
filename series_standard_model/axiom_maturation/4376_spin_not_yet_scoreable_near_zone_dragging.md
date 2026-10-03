# Spin Cannot Yet Be Scored: the Same Far-Field Frame Dragging Gives Opposite Spin Trends Depending on the Near Zone, Which No Rotating CPP Exterior Fixes. Only the Static −4.1% Stands

**Patch:** 4376. **Lane:** foundations, with GR. **Session:** 242.
**Answers:** TODO-4365-THIRDORDER (b), spin item, first look.
**Verify:** `series_standard_model/code/4376_spin_first_look_lense_thirring.py` (numpy + scipy).
**Critic:** a fresh-context critic (D-14) reviewed a draft that reported "spin makes it worse: −14% at χ = 0.68". It
found the trend depends on an unforced choice. The return is appended verbatim to
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`; its verdict is adopted.

## 1. What was computed

Both exteriors (Schwarzschild and the λ = 0 exponential metric) were given first-order frame dragging with the same
far-field Lense–Thirring tail (GR-1b reproduces it exactly). The prograde light-ring frequency (eikonal, ℓ = m = 2) was
then compared against **exact Kerr**.

The baseline check, GR + LT against exact Kerr: +0.05% at χ = 0.2, −0.08% at 0.4, **−2.73% at 0.68**. First order in
spin is not adequate for a number at GW250114's spin.

Three near-zone profiles, all with the same far-field J:

| profile | χ = 0.2 | 0.4 | 0.68 | note |
|---|---|---|---|---|
| A: w = 2J/R³ (areal) | −6.31% | −9.23% | −16.74% | the draft's choice |
| C: GR's tφ operator on the background | −5.64% | −7.49% | −12.90% | light ring inside the cap at 0.68 |
| B: g_tφ = −2J/r_iso (isotropic weak-field form, as in GR-1b) | −0.94% | **+6.35%** | **+16.67%** | light ring inside the cap from 0.4, inside the throat at 0.68 |

Static, χ = 0: −4.42% (eikonal); the ℓ = 2 WKB value is −4.06% (4374).

## 2. What can honestly be said

- **The sign of the spin trend is not robust.** It depends on how the spinning body drags space close in. Matching the
  far-field J fixes only the 1/r³ tail, and no rotating CPP exterior exists to fix the rest.
- Under profiles B and C the prograde light ring falls inside the cap, where the exterior metric no longer applies. A
  rotating CPP object may ring from the cap region rather than from a light ring.
- **LIGO's χ_f and M_f come from GR templates.** CPP's different ISCO (areal 6.34 m) and light ring would change the
  radiated energy and the final spin. The frequency moves about 2.4% per Δχ ≈ 0.03, so a fair comparison needs CPP's
  own remnant mapping or ringdown-only posteriors.
- **So:** the only solid number is the static ℓ = 2 shift, −4.06% against ±2.4%, a strong tension at zero spin only.
  **No exclusion and no spin-dependent tension can be claimed.** The draft's "−14%" is withdrawn as a result.

## 3. What the spin calculation needs (the blocker, named)

A rotating CPP exterior:
- the frame-dragging g_tφ derived from the A3′ vector channel to all orders in m/r on the λ = 0 background;
- then the O(J²) terms (quadrupole, oblateness), about 3% even in Kerr at χ = 0.68;
- then the ℓ = m = 2 mode, compared through CPP's own remnant mapping.

This is now the controlling unknown for the ringdown test, alongside CPP's tensor-wave operator.

## 4. PD-008

- **The convenient branch, caught:** I presented a result moving toward exclusion; under D-14 it went to a critic first,
  which showed the trend came from my choice of profile. Recorded as indicative only.
- **Not claimed either way:** that spin rescues λ = 0 (profile B's reversal is equally unforced).
