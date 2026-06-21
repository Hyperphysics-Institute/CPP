# Reasoning capture — Patch 2008: R2 / C-vs-K from shared Coulomb origin

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.
Pushes the R2 residual left open by 2007 (the C-vs-K stiffness question), at Thomas's request to "push the
physics now, with the circularity caveat in mind."

## The trap I had to respect
Thomas was explicit: a lattice-EM model I build could cancel C by construction (circular), proving nothing.
So I refused to (a) assume C=K, (b) assume them independent, or (c) write down a lattice Lagrangian tuned
to give a geometric Z0. The only honest move: derive C and K from ONE shared physical origin and read off
what is robust.

## The one input and the result
Corpus (0739): CP-CP interaction is Coulomb-like. So BOTH the on-site stiffness C=U''(d_DP) and the
inter-site coupling K=U''(a) are curvatures of the SAME Coulomb-derived potential, at different lattice
distances. Both are then LINEAR in the common strength Q=q^2/4pi eps0 (the SSV-screening channel). Script
confirms: C and K each scale exactly with Q, so K/C is EXACTLY Q-invariant (0.0e+00 across 8x). And -- a
bonus I didn't anticipate -- d_DP is also Q-invariant (the bond minimum is scale-invariant), so d_DP/a is
preserved too. The natural silly-putty SSV channel therefore preserves everything Z0 depends on -> A=0 ->
PASS with no residual from that channel.

## Where I held the line on honesty
- The negative K sign and its value are toy-potential artifacts (bare-pair curvature at a is not the real
  collective-mode coupling). I said so, and leaned only on the SIGN-INDEPENDENT robust fact: Q-linearity of
  both stiffnesses -> Q-invariance of K/C. I did not dress the toy's specifics up as physics.
- I did NOT compute absolute Z0. That needs the full c06 EM Lagrangian + self-consistent eps0, and is
  exactly where cancellation-by-construction would creep in. The RATIO is what is robust and non-circular,
  and it is what R2 needs. I stated this boundary explicitly rather than reaching for the absolute result.
- I kept the residual honest and narrow: a FAIL now requires an EXOTIC SSV channel that differentially
  distorts d_DP/a relative to the fixed GP lattice -- not the uniform screening of the silly-putty picture
  -- plus the sub-question of whether the DP exclusion core scales with the EM coupling (d_DP rigid) or is a
  fixed Planck scale (small shift). Both narrow, both favored toward PASS, neither hand-waved to zero.

## Net
R2 moves from "PASS conditional on un-derived single-oscillator" (2002) -> "single-response corpus-derived"
(2007) -> "C-vs-K locking derived from shared Coulomb origin; natural SSV channel gives full PASS" (2008).
The clean-kill exposure now needs a specific exotic channel, a long way from the open ~6-order falsifier R2
began as. I resisted declaring outright closure: the absolute-Z0 / core-scaling pieces are real, narrow,
and left for the c06 Lagrangian + the panel.

## Discipline
- Worker patch, owned path mu_eps_closure/lattice_ck/ only. NO edit to c06/0740/CONJ (proposed c06 cross-ref
  in finding section 6 for integrator). NO THEO. Files via bash; git status verified (2005 lesson).
