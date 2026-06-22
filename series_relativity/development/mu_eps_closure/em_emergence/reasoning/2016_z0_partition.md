# Reasoning capture — Patch 2016: Z₀ from the single-DP E/B response (PASS-pointing)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

## How this came about
After the 2011 negative, I told Thomas honestly that OPEN-SR-9 was blocked on a physics decision I could not
compute my way into — how the gapless photon emerges. He supplied it: his B-field/neutrino mechanism note +
a back-and-forth that pinned the model (DP centers pinned to GPs; only internal poles move; E=radial,
B=tangential, both under one Coulomb binding; bounded/restored response). That is exactly the input that was
missing, and it is his, not mine.

## What I computed and the discipline I held
I refused to assume C cancels. I extracted alpha_E (numerically, driven oscillator) and alpha_B (Larmor
diamagnetic, textbook 1/m), formed Z0=sqrt(alpha_B/alpha_E) under a symmetric emergence scheme, and SWEPT C.
Critically I added a COUNTERFACTUAL: rerun with omega_0 free (m fixed). If C cancels in both, it's by
construction and worthless. Result: CPP (omega_0 fixed) -> Z0 flat (5e-9 over 16x C) AND c~C varies;
counterfactual -> Z0~sqrt(C) FAIL. So the cancellation is forced by the fixed Absolute Moment, not built in.

## Why it works (the mechanism, honestly)
alpha_E ~ 1/C (compliance). alpha_B ~ 1/m (Larmor). The Absolute Moment fixes omega_0, welding m=C/omega_0^2,
so alpha_B ~ 1/C too -> ratio geometric -> Z0 geometric (alpha fixed) while c~C varies (VSL). The fixed
omega_0 is the load-bearing CPP input, and the counterfactual proves it.

## Where I held back from overclaiming
This is PASS-POINTING, not certified closure. The load-bearing assumption is the symmetric emergence scheme
mu0 ~ alpha_B (as eps0 ~ alpha_E). If mu0 ~ 1/alpha_B instead, it FAILS. I flagged this as the gate
(OPEN-SR-9 sub-Q3, eps0/mu0 symmetry) rather than burying it. I also flagged that alpha_B uses the textbook
Larmor formula (cited, not re-derived in the DP-Sea tangential picture) — the 1/m scaling is robust but the
full DP-Sea re-derivation would close the loop. I did not register a THEO (conditional result; fixed-omega_0
is existing c02).

## The honest arc
2011 said the naive action FAILS and the residual is the emergence mechanism. Thomas supplied the mechanism.
2016 computes it and gets PASS + VSL, conditional on one sharply-posed scheme question. That is real forward
progress on OPEN-SR-9 — and it came from the founder's physical intuition unblocking a computation, exactly
the division of labor I flagged was needed. R2's full PASS is now within reach of one more derivation (the
mu0-emergence scheme), not blocked.

## Discipline
- Worker patch, owned path mu_eps_closure/em_emergence/ only. NO edit to c06/CONJ/SR.md/R2-STATUS (status
  note lives in this finding + the scope doc update in this patch). NO THEO. Files via bash; git status verified.
