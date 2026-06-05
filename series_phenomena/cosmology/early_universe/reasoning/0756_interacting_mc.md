# Reasoning capture — Patch 0756: interacting bath-clause MC (in-house run)

*Session 154. Ran the interacting bath-clause MC; surfaced the charge-neutrality requirement. Finding:
`.../interacting_mc_finding.md`. Swarm request: `.../swarm_request_interacting_mc.md`. Script:
`.../scripts/0756_interacting_mc.py`. NO THEO. Toy of CPP dynamics, not the dynamics.*

## Design
A1-invariant occupation dynamics (counts only), 13-GP seed, site E=(K/2)[np(np-1)+nn(nn-1)]-Katt*np*nn.
3 configs x 3 lambda{10,20,40}; 5 observables; mu_excess slope vs nbar via Widom = decisive probe.

## Result (ran, not predicted)
A baseline (K=Katt=0): R 0.038, Poisson 20.0/20.1, S(0) 1.23, slope +0.0000 -> ideal (ref).
B unbalanced (K=0.05,Katt=0): R 0.028, Poisson 20.0/13.7, S(0) 0.70, slope +0.0246 -> CONTAMINATED.
C balanced (K=Katt=0.05): R 0.048, Poisson 20.0/21.4, S(0) 1.00, slope -0.0002 -> ideal.
All thermalize fast; thermalization is NOT the discriminator. The chemical potential is.

## The finding
mu_excess slope must be ~0 because at cosmological nbar~1e74, even slope +0.025 gives ~0.025*1e74 >>
ln nbar ~170 -> tilt to excluded power-law branch. The slope is NOT automatically 0 under interactions:
a GENERIC (unbalanced) +/- SSV interaction contaminates it (+0.025, S(0)=0.70 dispersed). CHARGE BALANCE
(K=Katt) cancels the leading mean-field (K-Katt)*nbar/2 -> slope ~0, S(0)~1. => NEW falsifiable
requirement: the bath clause holds only for an effectively charge-neutral early CP plasma. Cosmological
charge neutrality protects n_s=0.9649. S(0)~1 is the in-sim neutrality signature.

## Methodology validation
- ChatGPT's S(0) observable flagged B cleanly (0.70, dispersed) -- earned its place.
- mu_excess slope is the decisive discriminator (panel agreed); R did not separate configs.
- A1 discipline held (counts-only observables).

## Honesty calibration
- Ran it; reported the actual numbers including the CONTAMINATED config (did not hide the failure mode --
  it's the informative part).
- Stated toy caveat prominently; flagged the unresolved sub-leading Debye ~sqrt(nbar) residual as a real
  open risk even under neutrality (did not claim full closure).
- Framed charge neutrality as a NEW requirement surfaced by the run, not a prior assumption -- and as
  falsifiable (asked the swarm for counterexamples).
- Requested INDEPENDENT confirmation (swarm .md): own lattice/rule/probe; specifically asked them to try
  to BREAK claim 3 and to look for the Debye residual. Convergence -> robust; divergence -> toy misleads.

## Pointer
- Next: independent swarm runs; and (real-dynamics) whether the actual SSV interaction is charge-balanced
  and whether a sqrt(nbar) residual survives. Clear of chirality. PCD = Perceive/Compute/Displace.
