# Reasoning capture — Patch 0758: ChatGPT stress test + language calibration

*Session 154. Acts on ChatGPT's review of 0756/0757: language calibration + the beyond-quadratic stress
test. Records Grok/Copilot endorsements. Finding: `.../stress_test_finding.md`. Script:
`.../scripts/0758_stress_test.py`. NO THEO.*

## Calibration adopted (ChatGPT)
0756 slightly overclaimed. Corrected: 'charge neutrality cancels the LEADING mean-field (~n) in the
quadratic toy', NOT 'neutrality protects the log'. Bath clause sharpened to: fast neutral Gibbs bath with
excess chemical-potential growth negligible vs ln nbar at the pivot. Whether a sub-leading sqrt(n)
survives is the open question (0757 analytic + this stress test).

## Stress test (ran)
3D L=8, balanced +/-, screened-Coulomb g exp(-r/xi)/r, Widom mu_excess over lambda{4,8,16,32}. The 4-term
A n+B sqrt n+C ln n+D fit is ill-conditioned (collinear basis over 4..32) -> report raw mu + robust single
power p instead. Results:
 - UNBALANCED on-site control (K0=0.1): mu ~ n, p=1.02 -> POSITIVE CONTROL passes (probe detects
   mean-field; matches 0756 config B). Important: null results elsewhere are meaningful.
 - balanced short screened (xi=0.7): mu tiny (max 0.02) -> CLEAN. Matches 0756/0757 on-site/short-range.
 - balanced medium/long screened (xi=1.5,4): mu BLOWS UP super-linearly (p>2) at high lambda -> small-L
   toy BREAKING DOWN (absurd density 16-32/site on 512 sites, strong coupling, under-equilibration), NOT
   a clean sqrt(n) or linear. UNRESOLVED.

## Honest conclusion
Stress test (a) validates the probe, (b) confirms balanced short-range/on-site clean (the on-GP point-
stack, 0757), (c) does NOT clear long-range inter-GP -- toy breaks down. So:
 - on-GP point-stack: clean (0757 no-sub-GP-space + 0756/0758 short-range numeric).
 - long-range inter-GP residual: GENUINELY OPEN. Needs a proper large-L, well-equilibrated, dilute Ewald/
   RPA MC with the full A n+B sqrt n+C ln n+D fit and the pass condition 'residual subdominant to ln nbar
   at 1e74'. Added to the swarm request as the priority independent task.
Did NOT claim absence in general; claimed absence on-site/short-range, UNRESOLVED long-range -- ChatGPT's
calibrated phrasing.

## Honesty calibration
- Adopted ChatGPT's calibration verbatim in intent (no 'protects the log').
- Did NOT force a clean pass: reported the toy breakdown honestly as breakdown, not as evidence either way.
- Relabeled the unbalanced control accurately (it is the positive control, not a balanced case).
- Flagged the ill-conditioned 4-term fit and switched to a robust single-power diagnostic.
- Kept the on-GP point-stack (the load-bearing case) as the clean, supported result; isolated the
  long-range inter-GP case as the explicit open task with a concrete recommended method.

## Pointer
- Swarm priority task: large-L Ewald/RPA dilute MC, balanced long-range, full fit, pass = residual <<
  ln nbar at 1e74. Grok ready to run with real SSV form. Clear of chirality. PCD = Perceive/Compute/Displace.
