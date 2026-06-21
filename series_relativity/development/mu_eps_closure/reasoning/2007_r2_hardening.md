# Reasoning capture — Patch 2007: R2 hardening + panel dispatch

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.
Follows the OPEN-COSMO-DM-2 arc (2001-2006) and the 2005 remediation / 2006 consolidation.

## The job
Thomas: harden R2, the remaining conditional kill. My 2002 PASS was conditional on the single-oscillator
structure, which I had flagged as "a physical cartoon, NOT in the corpus." The honest question: is that
structure really un-derived, or did I under-read the EM sector?

## What I found (the hardening)
The b-field note's own corpus-status line: "the mechanical picture is NOT in the corpus; only the
curl/field-strength math is (EW-5, c06)." So the MECHANICAL narration (poles swinging) is cartoon, but the
FIELD-STRENGTH MATH is derived. And c06 line 91 (derived text) says the magnetic component "arises from
the curl of the propagating SSV pattern"; c06 line 185 already states the R2 prediction (Z0 geometric
because B is the curl of the polarization over the fixed eternal GP network); EW-5 derives F = dA - dA.

So the STRUCTURAL fact R2 needs -- B = curl(P), a functional of the one polarization field, no independent
magnetic field -- is corpus-derived, not cartoon. That discharges the "cartoon" caveat on R2's load-bearing
claim. The 2002 PASS is no longer hanging on an un-derived picture.

## Where I deliberately did NOT overclaim
"B = curl(P)" excludes an independent magnetic FIELD/coordinate. It does NOT by itself prove the magnetic
ENERGY carries the same stiffness-dependence as the electric energy. Electric = on-site polarization
(stiffness C); magnetic = gradient/curl of displacement (governed by the inter-site coupling K between
GPs). So the genuine residual is sharper than "single oscillator?": it is "is K rigidly locked to C under
SSV (Z0 geometric, PASS), or can K and C split (FAIL)?" I stated this as the honest open residual rather
than declaring full closure -- the derived math removes one horn (independent field) but not the
stiffness-locking horn. The fixed/eternal GP network (SSV-independent) favors the geometric/PASS outcome
(why c06 line 185 predicts it), but the inter-site K SSV-dependence is uncomputed.

## Why dispatch rather than force the derivation
The residual is now crisp and decidable (C vs K under SSV), but settling it cleanly needs the c06 lattice
EM Lagrangian (the owed mu0,eps0 in terms of C,c computation), and which horn is right is exactly the kind
of thing an adversarial panel is good at pressure-testing before I sink effort into a lattice model that
could cancel C by construction (circular). So I built the CONV-001 single-block dispatch posing two
hostile questions: (Q1) does B=curl(P) really exclude independent magnetic inertia? (Q2) can K split from
C under SSV? -- asking reviewers to ATTACK the PASS, give a counterexample lattice, and return a verdict
token. That is the honest next step: get the adversarial read, then formalize whichever way it points.

## Discipline
- Worker patch, owned path mu_eps_closure/ only. NO edit to c06/EW-5/0743-note (proposed c06 cross-ref in
  finding section 6 for the integrator). Dispatch package is for Thomas to paste to the panel.
- NO THEO (hardening + dispatch; no new axiom/term/counted prediction). Patch 2007, 2000-band.
- Created all files via bash (cat >) after the 2005 stray-path lesson; verified git status before commit.
