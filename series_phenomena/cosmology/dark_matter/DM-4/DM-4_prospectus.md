# DM-4 Prospectus — from substrate dynamics to halo structure (registered Patch 2308, 6 July 2026; work NOT started)

**Status: PROSPECTUS ONLY.** Founder directive: document the complete outline/strategy/methods while
fresh, for execution after (1) the DM-1 OSF release and (2) ideally the Gate-1/B1 discharge. This file
is the memory. Nothing here is registered physics; every judgment below is a PLANNING judgment, to be
re-derived at campaign open under the then-current corpus (CLONE-FIRST at open — grep the registry
before claiming IDs or re-stating any number).

## 1. What DM-4 is

The June-era scoping (session-156 handover) defined a DM-3 that the rod-era series deliberately did not
absorb: **derive the halo density profile ρ(r) from substrate dynamics and predict the scaling
relations** — Tully–Fisher (BTFR), core-size–V_max, the rotation-curve diversity band — from first
principles. DM-1/2/3 *tested* the candidate against halo data; DM-4 must *produce* the halos. It is the
difference between certifying a particle and deriving the galaxy, and it is the sector's "discriminating
win" in the June language.

## 2. The central physics insight to build on (the reason DM-4 is not just SIDM-with-our-σ)

**CPP halo dynamics is not elastic-scattering gravothermal evolution.** The registered interaction is
*dissipative-reach capture*: encounters that enter the potential-dominant region bind, with the energy
going into the Sea/internal channels — kinetic energy *leaves* the halo budget, and the products are
*aggregates* (larger effective N). Standard SIDM cores form by elastic heat conduction; dissipative dark
matter generically *cools and contracts*. So DM-4's dynamics is a **population-balance problem coupled
to gravothermal evolution**: the N-distribution of rods evolves (capture → aggregation; possibly
fragmentation in energetic collisions — the v1.0-era channel), σ/m ∝ N feeds back on the interaction
itself, and the energy ledger carries a dissipative sink. Nobody in the SIDM literature models exactly
this combination (the dissipative-DM literature — dark cooling, atomic DM — is the nearest neighbor and
should be mined for methods at open).

## 3. The dependency stack (Stage 0 — rulings needed before any halo computation)

- **(i) Gate-1/B1 discharged (or explicitly carried).** You cannot derive halo assembly from a sourcing
  rule whose GR limit is ungrounded. If DM-4 opens before the discharge, the conditionality must be
  stated DM-3-style with kill-propagation — but the strong recommendation is: discharge first.
- **(ii) THE CAPTURE-AFTERMATH RULING (the true gate; substrate question).** What does a captured pair
  *become*? Options with entirely different halo consequences: (a) prompt merger into a 2N rod (binding
  energy radiated to the Sea → fast dissipation, strong aggregation); (b) long-lived orbiting binary
  (partial dissipation; binary heating channel — could HEAT the halo center like SIDM does, an
  anti-collapse valve); (c) capture-then-release above an energy threshold (effective elasticity at
  high v). The registered corpus fixes the reach criterion but NOT the aftermath. This ruling — founder
  + derivation + panel — gates every downstream number. Budget 1–2 sessions.
- **(iii) Initial conditions / seeds.** The acausal-seed items (OPEN-COSMO-DM-1/DM-2; the
  structure-formation R2 gated on OPEN-SR-9) are open. The defensible EFT move if they stay open:
  ASSUME ΛCDM initial conditions at z ~ 50 and evolve forward with CPP microphysics, tagged as an
  explicit assumption (the candidate is cold and 25 GeV — ΛCDM ICs are the natural null). Do not let
  DM-4 silently inherit a solved seed problem.
- **(iv) Adjacent, NOT absorbed: the relic abundance.** Why Ω_DM/Ω_b ≈ 5.4 is a formation-era question
  (the 16 keV formation temperature / F7 corner / the open formation-cap mechanism), likely its own
  paper. DM-4 should take Ω_DM as measured input and say so. Flag: the abundance is the sector's
  biggest unclaimed prize; keep it visibly separate so DM-4's scope stays finite.

## 4. Method stack (staged, cheapest kill first)

**Stage 1 — semi-analytic (the campaign's core; SF-7-scale, multi-session).** Modify the standard
gravothermal fluid treatment of SIDM halos (Balberg–Shapiro lineage; the modern calibrated versions) to
CPP microphysics: (a) conduction term from the MEASURED elastic floor (that part is genuinely
SIDM-like); (b) capture sink/source terms from the registered σ_cap(v) with the Stage-0(ii) aftermath
ruling deciding the energy branch; (c) a two-population (monomer/aggregate) or N-binned
population-balance layer with σ/m ∝ N feedback; (d) the dissipative energy ledger.
**THE CHEAP KILL, RUN FIRST (K1): the dissipative core-collapse timescale.** If capture-dissipation at
the registered σ(v) drives dwarf-scale halos to cusp/collapse in ≪ Hubble time — and no derived
saturation (aggregate depletion of σ_cap at low relative velocity within bound systems? binary heating
under aftermath (b)?) rescues it — the candidate dies at the halo level, and better we find it in a
200-line fluid code than a referee does. Estimated cost of K1 alone: 1–2 sessions.
**Stage 2 — data confrontation.** Targets, in confrontation order: (1) dwarf core sizes vs the 1865
pins (self-consistency: DM-1's window was an input; DM-4 must REPRODUCE it from evolution, not assume
it — the anti-circularity check is that core sizes emerge at the registered σ(v) with zero refit);
(2) core-size–V_max relation; (3) the diversity problem (the spread of rotation-curve shapes at fixed
V_max — SIDM's celebrated success; CPP must match it); (4) BTFR slope/normalization from the SPARC
library; (5) exploratory only, flagged as such: the radial-acceleration relation (do NOT promise a₀).
Also: (6) the F-DM3-2 synergy — with ρ(r) in hand, the running-slope law becomes a concrete observing
program (predicted p(v) along each rotation curve), converting DM-3's programme-level goal toward
practice.
**Stage 3 — N-body (collaboration-scale; optional for v1.0).** A capture+aggregation module spec in the
style of the public SIDM implementations, published as an invitation rather than executed solo. DM-4
v1.0 can ship on Stages 0–2; Stage 3 is the community hook.

## 5. Kill-conditions (pre-registered at open)

K1 dissipative collapse timescale (above — the opener). K2 BTFR slope/normalization outside empirical
tolerances with no derived rescue. K3 diversity band inconsistent (too narrow OR too wide). K4 the
dwarf-window reproduction fails (anti-circularity: the evolution must land the window DM-1 assumed).
K5 inherited kills propagate (Gate-1/B1, F3′, F1′ — per the DM-3 ledger discipline). Every K gets a
named falsifier ID at open.

## 6. Deliverables and paper shape

DM-4 v1.0 = Stage-0 rulings (documented) + the Stage-1 model (with K1 survival shown) + the Stage-2
confrontation table + the F-DM3-2 observing-program section + the inheritance ledger (DM-3-style, with
kill-propagation) + protocol updates to `DM-3/falsifier_protocols.md` (which remains the sector's
normative table — DM-4 ADDS rows, never forks the table). CONV-001 panel per cycle; CONV-004 tags
throughout; the population-balance and aftermath choices J-tagged.

## 7. Cost estimate and sequencing (planning judgment)

Stage 0: 2–4 sessions (the aftermath ruling dominates). Stage 1: 4–8 sessions (the fluid+population
solver and its validation against published SIDM baselines before any CPP claim — validate-against-
known-physics first, exactly as the XQC solver was Born-validated). Stage 2: 3–5 sessions. Paper +
panel: 2–3 sessions. **Total: a multi-week arc — the founder's read ("a lot of time") is correct.**
Sequencing: OSF release → Gate-1/B1 campaign → DM-4. If Gate-1/B1 stalls, DM-4 Stage 0(ii) (the
aftermath ruling) is independently valuable and can run in parallel lanes per the multi-window protocol.

## 8. What must NOT happen (recorded so future-us keeps faith)

- No silent absorption of the seed problem or the relic abundance (both named, both separate).
- No refit of σ(v) to make halos work: the curve is registered and panel-ratified; if halos fail at the
  registered curve, that is a RESULT (a kill or a fork), not a tuning opportunity.
- No claim of the dwarf window as a success without the anti-circularity framing (K4).
- The aftermath ruling is a substrate-physics decision (founder-gated, CONV-004-tagged) — not a
  convenience parameter chosen to save K1.
