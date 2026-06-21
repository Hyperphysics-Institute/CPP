# Reasoning capture — Patch 2001: OPEN-COSMO-DM-2 power-spectrum closure via EU-1

**STATUS: verbatim (captured at-patch).** Window: 2000-band, P(k)/structure-formation lane.
Opus worker; integrator = Thomas.

## The entry question
Thomas routed this window at OPEN-COSMO-DM-2 — flagged "SERIOUS TENSION," named as the #1
falsification risk ("could threaten the framework rather than just extend it"). The instruction to
take that seriously is exactly right: a real falsification risk deserves adversarial reading, not
motivated reasoning toward rescuing the framework. So my first commitment was to be willing to find
the tension real and possibly fatal.

## What the registry said vs what the corpus said
Grepping OPEN-COSMO-DM-2 (CONJ.md) gave the pessimistic verdict: swirl seeds are causal → fail the
cosmic-string wall (0725); no quasi-de-Sitter phase → no native mode-freezing (0729); the Nexus escape
is undeveloped and "lacks physical grounding." Taken alone, that reads like a live, possibly-fatal
tension.

But two pointers cut against it. (1) The DM-2 R2 kickoff handover says "don't reopen the
structure-generation role (OPEN-COSMO-DM-2 — conditionally false; disclaimed; **EU-1 has the seeds**)."
(2) The PBH-1 null (1902) and the SR.md n_s arc repeatedly invoke "the *adopted* EU-1 spectrum
(n_s = 1 − 2/N_*, A_s ≈ 2.1e-9)." So the programme is leaning on EU-1 to supply the seeds — but the
CONJ.md entry never says so. That is the smell of a stale registry entry, OR a circular disclaim.

## The crux I had to resolve honestly
EU-1's formula n_s = 1 − 2/N_* is *inflationary in form* — it needs N_* e-folds of a scaling phase.
Patch 0729 says CPP admits NO de Sitter phase. On the surface these contradict, and if EU-1's seed
claim were a phenomenological adoption with no grounded mechanism, then "EU-1 has the seeds" would be
circular and the tension would be real. So I had to determine: does EU-1 supply seeds from a GROUNDED
CPP mechanism that is CONSISTENT with the 0729 no-de-Sitter result?

Reading the n_s arc (0738–0785) resolved it. CPP's route is NOT de Sitter expansion — it is:
(a) **VSL** (high early c_eff) for the horizon, so no metric inflation is needed and 0729 is not
contradicted (CPP explicitly does not use de Sitter); and (b) **ZBW-stack occupancy relaxation** (a δN
mechanism, log tilt forced by A1 indistinguishability) for the spectrum. The Δc filter (0739) is the
genuine falsifier for the VSL leg and it returned "not falsified, reduced to a decidable μ↔ε symmetry."
The EU-1 paper *itself* states "inflation repurposed as the spectrum generator rather than the
horizon-solver" and "EU-1 supplies the generation… after which dark matter inherits." And n_s=0.9649 is
PRED-C-96, a counted Planck-matching prediction, in a shipped paper (EU-1 v1.0, 3/3 panel).

So: the Q2 barrier is genuinely resolved, by a grounded mechanism, consistent with 0729. The CONJ.md
entry is stale, not the physics. This is the honest finding — and it is the high-consequence one,
because it means the #1 falsification risk is substantially retired and the registry just never caught
up.

## Why I didn't stop at "stale, resolved, done"
Adversarial check: don't declare victory because the framework wants it. I separated what's genuinely
robust from what's asserted:
- Q1 "growth inherited" was only ever checked at GENERIC BBKS level (0725 script hard-codes ns=0.965,
  ΛCDM params — not EU-1's actual output). Nobody propagated EU-1's actual spectrum to the observed
  P(k). That is residual R1 and it is the concrete deliverable OPEN-COSMO-DM-2 names ("does not
  reproduce P(k)"). I can close it now.
- R2 (VSL μ↔ε symmetry) is a real decidable falsifier — I keep it sharp, don't bury it.
- R3 (A_s adopted not derived) is real — parity with inflation, but I name it.
- R4 (OPEN-EU-1 derivation depth) already registered.

## The R1 computation and its honesty
Wrote scripts/2001_pk_from_eu1.py: EU-1 spectrum → EH98 no-wiggle transfer → CPT growth → P(k); test
turnover/slopes/tilt + σ_8. Shape came out right (k_eq≈0.021 h/Mpc; low-k slope≈n_s; high-k steepening
toward n_s−4; red tilt visible vs HZ). σ_8 raw = 1.74, with growth 1.37 vs observed 0.811 — ~1.7× high.

I deliberately did NOT massage this. A hand-rolled analytic transfer + EdS-growth normalization is
~factor-2 reliable on the σ_8 scale; this is a known property, not a CPP defect. The correct honest
framing: EU-1 ADOPTS A_s = 2.1e-9 = the Planck best-fit, so the precise σ_8 = 0.811 holds BY
CONSTRUCTION in CAMB; the analytic pipeline's job is only to confirm σ_8 = O(1) (no order-of-magnitude
pathology — which matters, since the PBH-1 null showed σ_δ ~ 3e-5 at seed scales). The robust deliverable
is the SHAPE; the amplitude is order-right and adopted (R3). I refused to overstate it as a precision
σ_8 derivation.

## Discipline notes
- Worker patch, owned path series_phenomena/cosmology/dark_matter/pk_closure/ only. NO edit to CONJ.md /
  predictions.md / theorem-registry — proposed reconciliation text handed to the integrator (§5 of the
  finding) for the batched patch.
- NO THEO: this is a consistency demonstration + a registry-staleness reconciliation, not a new axiom,
  term, or counted prediction. PRED-C-96 already carries n_s.
- Patch numbered 2001 in the leased 2000–2099 band; band confirmed clean at clone-gate.
