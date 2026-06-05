# Cover note to the panel — the Ewald/RPA test, and why Stage A gates everything

*For the CPP AI review panel (Grok, Claude, ChatGPT, Copilot). Short framing for the full protocol in
`series_phenomena/cosmology/early_universe/ewald_rpa_spec.md`. Read this first; run Stage A first.*

## Where we are (one paragraph)

The n_s = 0.9649 derivation has been narrowed, with your help, to a single open question. The logarithm is
A1 (indistinguishable occupation-number counting — not dynamical, not measured). The bath (fast Gibbs
equilibration) passed in the toy under charge neutrality, with the leading mean-field cancelling. The one
thing neither the toy nor the analytics fully settled is the **sub-leading Debye residual**: for a
charge-balanced **long-range** (inter-GP) CP plasma, is there a μ_excess ∝ −√n̄ whose **dimensionless**
coefficient B (the √n̄ coefficient of μ_excess/**kT**) is large enough that B·√n̄ ≳ ln n̄ ≈ 170 at the
cosmological pivot n̄ ~ 10⁷⁴ (both sides dimensionless)? If yes, it dominates the
logarithm and the tilt is excluded; if no (B ≈ 0, or the point is beyond the Debye regime, or B is tiny),
the corner closes and n_s = 0.9649 stands as a zero-new-axiom prediction.

## Why we are handing you a spec, not a result

Our in-house toy (Patch 0758) **broke** on exactly this case — small lattice, strong coupling, raw Widom
insertion, and an ill-conditioned fit. Rather than dress up artifacts as physics, we wrote a rigorous
protocol (0759) and **validated the two methodological fixes** that the toy got wrong:
- **the fit** — recovering a known √n̄ coefficient needs a *wide, log-spaced* density range (the toy's
  narrow range is collinear and unrecoverable); report the column-normalized condition number and subtract
  the A1 ln n̄ first;
- **the estimator** — use **Kirkwood charging integration**, not raw Widom, which is rare-event-dominated
  and blows up at the densities of interest.

Both are demonstrated in `scripts/0759_ewald_method_validation.py`. Please don't re-run the broken toy;
build to the spec (or your own equivalent — independent implementations converging is the strong result).

## The gate: do Stage A first, and stop if it fails

**Stage A is non-negotiable and comes before everything else.** Run unscreened Coulomb in the dilute,
weak-coupling regime and confirm your implementation **reproduces the Debye–Hückel limiting law
μ_excess/kT ∝ −√n** to a defined bar — |B_fit − B_DH|/B_DH < 5% after finite-size extrapolation, with
recovered B_fit, analytic B_DH, relative error, and an uncertainty estimate all reported (ChatGPT's
operationalization, so reviewers apply one standard). This is the calibration against a
*known analytic answer*. If Stage A does not recover the textbook √n, the Ewald sum, the charging
integration, or the fit is wrong — and **no result from Stages B–D can be trusted until Stage A passes.**
Treat a Stage-A failure as a bug to fix, not a physics finding.

Only after Stage A passes:
- **Stage B** — scan coupling/density; locate the crossover n_* and check it against the analytic
  n_* ~ (kT/q²)³ (Patch 0757).
- **Stage C** — scan screening length ξ; map B(ξ) → 0.
- **Stage D** — plug in the real CPP SSV kernel and read off B; evaluate B·√n̄ vs ln n̄ at the pivot.

## What we need back, and what we still owe you

From you: the Stage-A validation (DH √n reproduced), then B for the relevant kernels, with the pass/fail
at the cosmological pivot (pass if B ≈ 0, or the point is above n_*, or B·√n̄ ≪ ln n̄ ≈ 170; fail only if
unscreened-long-range **and** in the Debye regime **and** B·√n̄ ≳ ln n̄). Note the comparison is
**dimensionless** throughout (per ChatGPT's calibration): B is the √n̄ coefficient of μ_excess/kT, compared
to ln n̄ — reduce μ_excess by kT before comparing, so no stray kT factor can hide an error.

From us: the one physical input Stage D needs — the **actual SSV interaction range and form**. Stages A–C
can proceed and bound the answer without it; Stage D is where the corner is finally settled, and we will
supply the kernel.

Adversarial readings and independent designs welcome, as always. The full protocol, observables, and
pass/fail criteria are in `ewald_rpa_spec.md`.
