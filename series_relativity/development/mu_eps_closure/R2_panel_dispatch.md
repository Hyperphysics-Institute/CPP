# R2 Panel Dispatch — single-block package (CONV-001)

Copy everything inside the 4-backtick fence below and paste once to each panel member
(default panel: ChatGPT / Grok / Copilot). One click, one paste per reviewer.

`````
**CPP review request — adversarial. Attack the PASS; do not confirm it.**

We are hardening the one remaining conditional falsifier of CPP's variable-speed-of-light (VSL) early-universe horizon mechanism (work item OPEN-COSMO-DM-2, residual R2). Your job is to try to BREAK the claim below, not to agree with it. A successful break is a ~6-order falsification of the mechanism, so please be hostile. Two specific questions are at the end.

GitHub (blob = rendered, raw = plain):
- R2 result (virial mechanism):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_relativity/development/mu_eps_closure/R2-Z0-VIRIAL-CLOSURE.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_relativity/development/mu_eps_closure/R2-Z0-VIRIAL-CLOSURE.md
- R2 hardening (single-response is corpus-derived):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_relativity/development/mu_eps_closure/R2-HARDENING.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_relativity/development/mu_eps_closure/R2-HARDENING.md
- verify script (both readings):
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_relativity/development/mu_eps_closure/scripts/2002_z0_impedance_fork.py

## Setup (what is and isn't in dispute)

In CPP the DP Sea is the electromagnetic medium, so c = 1/sqrt(mu0*eps0) (product) and the fine-structure constant alpha is proportional to sqrt(mu0/eps0) = Z0 (the vacuum impedance / ratio). The VSL horizon mechanism makes c_eff vary in the early universe (high early c_eff solves causal contact without de Sitter inflation). The falsifier: if a density/SSV-driven change in c also drags alpha, it violates the atomic-clock Local-Position-Invariance bound |k_alpha| < 1e-6. Exactly:

  Delta(alpha)/alpha = Delta ln Z0,   and   k_alpha = A = (d_mu - d_eps)/(d_mu + d_eps) = -dZ/dc.

So the entire falsifier reduces to ONE question: when an SSV perturbation changes the DP-Sea stiffness C (hence c), does the impedance Z0 = sqrt(mu0/eps0) move?
- A = 0 (Z0 geometric, C-independent): the c-variation is pure metric = gravity, alpha is fixed -> PASS.
- A ~ O(1) (Z0 carries C): alpha drifts with density -> FAIL by ~6 orders vs the clock bound.

## The claim we want you to attack

(1) MECHANISM (derived, script-checked). Model the DP as one charged harmonic oscillator: stiffness C (SSV-variable), inertia m, ZBW frequency omega^2 = C/m with omega FIXED by the Absolute Moment (geometric, NOT a function of C). The harmonic virial theorem gives <KE> = <PE> exactly (because omega^2 = C/m). If the electric field energy and the magnetic field energy are the two halves (potential and kinetic) of this ONE oscillation, they carry IDENTICAL C-dependence, so C cancels in the ratio Z0 = sqrt(mu0/eps0) (geometric) but survives in the product mu0*eps0 = 1/c^2 (so c varies = gravity, c ~ sqrt(C), the right sign for high early c_eff). Script: Z0 flat (A = 0 exact) across a 4x swing in C; the alternative (independent magnetic inertia) gives Z0 ~ C^1, A ~ O(1).

(2) HARDENING (corpus-derived, not cartoon). CPP's DERIVED field-strength math (companion c06 line 91; EW-5 field-strength tensor) defines the magnetic component as the curl of the propagating polarization pattern over the FIXED, ETERNAL GP lattice: B = curl(P). So B is a FUNCTIONAL of the one polarization (displacement) field, not an independent magnetic field with its own coordinate. This excludes the strong "independent magnetic oscillator" horn structurally, from existing derivation.

## The two questions (please answer both, adversarially)

Q1. Does "B = curl(P) over the fixed GP network" genuinely exclude an independent magnetic inertia, as claimed in (2)? Or can a medium with B defined as a curl-functional of one displacement field STILL exhibit an impedance that depends on the medium's stiffness? Give the cleanest counterexample you can.

Q2. The honest residual: the electric energy is on-site (local polarization, stiffness C -> eps0 ~ n q^2 / C); the magnetic energy is the gradient/curl of the displacement (governed by the INTER-SITE coupling stiffness K between neighboring GPs). Does Z0 = sqrt(mu0/eps0) come out C-independent (PASS) ONLY if K is rigidly locked to C, or is there a reason in lattice EM that the curl/impedance ratio is geometric regardless of K vs C? Concretely: under an SSV perturbation that changes the on-site C, does the inter-site K move identically (ratio preserved, PASS) or can it split (FAIL)? If you can construct a physical lattice where K and C carry different SSV-dependence, that is a candidate kill — please try.

Please give a verdict token (CONFIRM / RESTATE / REVISE / REJECT) on the claim "Z0 is geometric -> A = 0 -> R2 PASS", plus your sharpest attack on each of Q1 and Q2.
`````
