# Reasoning capture — Patch 0745: depth-based boost — near-scale-invariance selects the entropic log

*Session 154. Tests the depth-based H-boost. Writeup: `.../development/depth_based_boost_finding.md`.
Toy: `.../scripts/0745_depth_based_boost.py`. NO THEO.*

## The discipline I held

Copilot reasoned BACKWARD ("log → p=2, so use log"). I refused to assume the log. Instead I tested six
physically-distinct depth-laws h(n) and computed n_s for each, to see which physical picture the data
select and whether it is motivated or reverse-engineered.

## Result (the informative part is the EXCLUSIONS)

- mechanical/power laws h~n, n^2, n^2/3 give n_s = -5, -11, -3 — ABSURD, wildly excluded. So the naive
  "deeper pushes harder" (linear/power) is ruled out HARD. This is the key finding: the depth response
  CANNOT be power-law.
- on/off (fraction) → n_s=1 (HZ), excluded.
- ONLY h ~ ln(n) gives a sensible near-scale-invariant spectrum, landing on n_s = 1 - 2/N_* = 0.9649.

So near-scale-invariance UNIQUELY selects the logarithmic depth-law among the candidates.

## Why the log is motivated (not reverse-engineered)

The log is NOT mechanical "deeper pushes harder" (power → absurd). It is the ENTROPIC / chemical-
potential form: dispersal drive of an over-concentrated species is mu = mu0 + kT ln(c), logarithmic in
concentration (STANDARD stat mech). Thomas's story is literally "relax over-occupation toward 1/GP
equilibrium" = a DISPERSAL process = entropic mu ~ ln(n). So IF the boost is entropic dispersal
pressure, h ~ ln(n) is the natural textbook form and p=2 is a consequence.

Favored three ways: (i) physical naturalness (chemical potential), (ii) uniqueness (only log gives
near-invariance; power laws absurd), (iii) correct small running (1/N form). And the precise 0.9649 is
NOT circular: only qualitative near-invariance selects the log; the quantitative value comes from N_*
fixed independently by the CP count.

## Important correction to Thomas's intuition (logged for the reply)

Thomas's "deeper stack → larger PSR increment, initial expansion large" is right in DIRECTION but must
be LOGARITHMIC, not linear: a 10^30-deep stack boosts only ~30x harder than a 10-deep stack (log ratio),
NOT 10^29x. Linear/power dependence is absurdly excluded. The viable depth response is the gentle,
saturating entropic log.

## Honest boundary (did NOT overclaim)

CONSISTENT-AND-FAVORED, not DERIVED. Load-bearing assumption: relaxation is ENTROPIC (mu~ln n, dispersal)
vs MECHANICAL (~n^q, repulsion). Mechanical → absurd; entropic → 0.9649. Story + data both favor
entropic, but the PCD-level derivation that the relaxation is entropic-logarithmic is owed. Did not
register a prediction (still conditional on the entropic derivation). p=2 upgraded from "wish" (0744) to
"favored & consistent" — short of "predicted."

Partial-circularity flagged honestly: "near-invariance selects log" uses the qualitative data; only the
quantitative 0.9649 (from CP-count N_*) is a genuine non-circular match given the log.

## Conventions
NO THEO. No prediction registered (conditional on entropic derivation). Verify script bundled. Clear of
chirality. PCD = Perceive/Compute/Displace.

## Pointer
- THE remaining computation: PCD-level derivation that over-occupation relaxation is entropic (∝ ln n,
  chemical potential of dispersal) and not mechanical (∝ n^q). If entropic confirmed → n_s=0.9649 is a
  zero-parameter CPP prediction (N_* CP-fixed) and the spectrum thread closes.
