# Swarm request: independent confirmation of the interacting bath-clause MC

*For the CPP AI review panel (Grok, Claude, ChatGPT, Copilot). Follows the 0754 briefing and your reviews
(which we integrated). We ran the interacting bath-clause Monte Carlo in-house; below is the result and a
request that you reproduce or refute it with your own independently-designed simulation. Self-contained.*

## What we tested

The bath clause of the n_s derivation: do A1-invariant occupation-number dynamics, seeded on the 13-GP
cohort, thermalize a CP stack to an *effectively ideal* Gibbs ensemble (so μ ∝ ln n survives) when the ±
SSV interaction is switched on? Per-GP site energy used:

  E(n₊,n₋) = (K/2)[n₊(n₊−1)+n₋(n₋−1)] − K_att·n₊·n₋   (same-sign crowding cost; ± co-location bind)

Observables (counts only): τ_eq; Poisson stationary (mean≈var); long-wavelength structure factor S(0)
(block-count Fano, per ChatGPT); μ_excess(n̄) slope via Widom insertion (the decisive tilt-contamination
probe); R = τ_eq/t_efold. Three configs, each at λ ∈ {10,20,40}.

## Our result

| config | R | Poisson (mean/var) | S(0) | dμ_excess/dn̄ | verdict |
|---|---|---|---|---|---|
| A baseline K=K_att=0 | 0.038 | 20.0/20.1 | 1.23 | +0.0000 | ideal (reference) |
| B unbalanced K=0.05, K_att=0 | 0.028 | 20.0/13.7 | 0.70 | **+0.0246** | **contaminated** |
| C balanced K=K_att=0.05 | 0.048 | 20.0/21.4 | 1.00 | −0.0002 | ideal |

**All three thermalize fast (R ≪ 1).** Thermalization is not the discriminator. The chemical potential is:
a *generic* (unbalanced) interaction gives μ_excess a slope ∝ n̄ and S(0) < 1 (dispersed) — it
**contaminates the tilt**. Only the **charge-balanced** ± interaction (K = K_att) cancels the mean-field,
returning μ_excess slope ≈ 0 and S(0) ≈ 1.

## The claim we want you to confirm or break

1. **Thermalization is necessary but not sufficient** — confirmed here: all configs thermalize; only the
   chemical-potential probe separates them.
2. **A generic ± SSV interaction contaminates the tilt** (μ_excess ∝ n̄), which at the cosmological n̄ ~
   10⁷⁴ would swamp ln n̄ ~ 170 and push n_s into the excluded power-law branch.
3. **Charge neutrality (balanced ±) protects the log** — the leading mean-field cancels at K = K_att,
   restoring an ideal chemical potential. We propose this as a new, load-bearing physical requirement:
   *the bath clause holds only for an effectively charge-neutral early CP plasma.*

## What we ask of you

Run **your own** independently-designed occupation-number Monte Carlo (your lattice, your hop rule, your
equilibration metric, your chemical-potential probe). We are specifically interested in whether you
reproduce:
- the **necessary-but-not-sufficient** structure (fast thermalization with a contaminated chemical
  potential), and
- the **charge-neutrality protection** (balanced ± → ideal μ; unbalanced → ∝ n̄ contamination).

We would also value:
- a check of the **sub-leading** μ_excess: even when the leading mean-field cancels, a Debye-like ∝ √n̄
  residual could matter at cosmological n̄. Does your run see one, and does it threaten the tilt?
- any interaction form for which the cancellation **fails** despite charge balance (a counterexample to
  claim 3 would be valuable).
- your judgement on whether "effectively charge-neutral CP plasma" is a *safe* CPP assumption for the
  inflationary epoch, or itself an open question.

## Honest framing

This is a toy of CPP's dynamics, not the dynamics themselves. A clean in-house result is a first data
point and a methodology check; it does not derive n_s and does not substitute for the real microphysics
or for your independent runs. A reproduction across independent designs would make the bath clause (under
neutrality) robust; a divergence would tell us where the toy misleads. As before, adversarial readings are
welcome.

## Addendum (Patch 0758): the long-range / Debye stress test

ChatGPT's review asked us to scan balanced interactions *beyond* the quadratic on-site toy and fit
μ_excess = A·n̄ + B·√n̄ + C·ln n̄ + D, with the pass condition that any residual stay subdominant to
ln n̄ ≈ 170 at n̄ ~ 10⁷⁴ (not merely A ≈ 0). We ran a small 3D version: a positive control (unbalanced
on-site → μ_excess ∝ n̄, p ≈ 1.0, correctly detected); balanced short-range screened → clean (μ_excess ≈
0); but balanced **medium/long-range** screened **broke the small toy** (super-linear blow-up at high λ on
an 8³ lattice — strongly coupled and under-equilibrated), so the long-range functional form is
**unresolved**, not cleared.

**This is the open task we'd most value your independent run on:** a proper **large-L, well-equilibrated,
dilute-regime** Monte Carlo of a charge-balanced screened/long-range CP plasma (Ewald or RPA for the
long-range part), measuring μ_excess across many λ and fitting the full A·n̄+B·√n̄+C·ln n̄+D form. The
question is whether a balanced *long-range* (inter-GP) interaction generates a **√n̄** (Debye) residual
that survives — and if so, whether its coefficient is small enough to stay below ln n̄ at the cosmological
pivot. Note our analytic 0757 argument that for the **on-GP stack itself** there is no sub-GP spatial
substrate (so the interaction is on-site → no √n̄); this stress test concerns the **inter-GP** long-range
case only. A counterexample (a balanced long-range form with a surviving, non-negligible √n̄) would be a
genuine threat to the tilt; a demonstration that screening/lattice cutoff kills it would close the last
corner.
