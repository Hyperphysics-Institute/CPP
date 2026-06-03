# Reasoning capture — Patch 0741: the roll-off law — FOUND PROBLEM (predicts excluded n_s=1)

*SR-1 rederivation pass, Session 154. The first-principles attempt to make n_s a prediction (Brick #4
/ 0738 left it a tuning). Toy: `.../early_universe/scripts/0741_rolloff_law.py`. Writeup:
`series_relativity/development/rolloff_law_finding.md`. NO THEO. NEGATIVE result, reported straight.*

## What I did

Implemented the roll-off FAITHFULLY from the H-axiom (no tuning):
  H_eff(N) = H0·f(N);  f = Poisson P(occupancy≥2) = 1 − e^{−n̄}(1+n̄);  n̄(N) = (N_CP/N_GP)·e^{−3N};
  n_s − 1 = 2 d ln f/dN at horizon crossing.
Then computed n_s across the observable CMB window (scales crossing ~47–55 e-folds before f=0.5 end).

## What it gave (and why)

n_s = 1.000000 across ALL observable scales (HZ). Reason: n̄ ≳ 10⁶¹ throughout the observable window,
so f = 1 to machine precision (every GP superposed ⇒ exact de Sitter ⇒ scale-invariant). The red tilt
appears ONLY in the final ~1 e-fold (n̄ ~ 7), where it crashes through 0.82 to negative — a sharp
running feature at sub-observable scales. Planck excludes n_s=1 at ~8σ.

The H-axiom superposition rule is effectively ON/OFF: H_eff ≈ H0 (const) while n̄≫1, then a cliff at the
graceful exit. A cliff at the end ≠ a gentle tilt across the window. The observable modes all froze at
the same H0.

## The honesty call (the important part)

I did NOT rig a roll-off to hit 0.965. The 0738 "modest roll-off → 0.965" was a POSITED smooth decline
with no dynamical support; the actual dynamics give a step, not a smooth decline, so the 0738 tilt was
a tuning with no first-principles backing — and the dynamics that DO exist give the excluded HZ value.
Reported as a found problem / candidate vulnerability, not spun. This supersedes the optimistic
brick4 framing.

Temptation resisted: I could have placed the observable window in the last 1–2 e-folds (where n̄~10
gives n_s~0.97) to claim success. That is unphysical — observable CMB modes cross ~50–60 e-folds before
the end, not in the final e-fold — so it would be rigging. Did not do it; flagged the mismatch explicitly.

## Constructive redirect (not a rescue)

The tilt requires a SUSTAINED gentle decline d ln H_eff/dN ≈ −0.017 over the full observable window
(~50 e-folds). The on/off occupancy rule cannot give that. The only natural source is the SMOOTH
decline of background SSV/DP-Sea density during inflation governing the boost CONTINUOUSLY — i.e. a
smooth H=H(SSV) or injection σ=σ(SSV), not an occupancy switch. That is a well-posed next target but is
NOT derived, and matching −0.017/e-fold would need a specific gentle SSV-dependence. So n_s stays
unpredicted; we now know the obvious mechanism (unstacking exit) is the WRONG source.

## Sector status after this brick
Gaussianity (CLT) solid; A_s a tuning; horizon via high c_eff; Δc reduced to Z₀-geometric (0740);
**tilt n_s = FOUND PROBLEM** — simplest roll-off predicts excluded HZ. Sharpest open problem; genuine
candidate vulnerability. "CPP predicts n_s=0.965" is NOT currently supportable.

## Conventions
NO THEO (negative dynamical result). No prediction registered (the point is that the prediction FAILS).
Verify script bundled. Clear of chirality.

## Pointer
- If pursued: smooth H(SSV)/σ(SSV) roll-off during the constant-H phase — derive the SSV-dependence,
  test for a natural sustained ~−0.017/e-fold. Otherwise this stands as the sector's main open risk.
