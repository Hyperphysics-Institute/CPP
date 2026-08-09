# AXIOM AMENDMENT PROPOSAL AP-4 — THE DI-BIT PAYLOAD RESPECIFICATION ({origin address, E, S}; weighted SSV_abs; emergent gravitational channels)

**v1.1, Patch 3031 (8 Aug 2026). PANEL-ENDORSED-WITH-AMENDMENTS at
CONV-013 (completion adjudication, Patch 3023); this revision folds the
three panel amendments — Q-A no-phase invariant restatement + proof
sketch (§2-I, [COP], 4/5 confirm-class), Q-B messenger-content vs
computed-state clarifying clause (appended to AP-4d, [Gemini][DS][COP]
3/5 — drafted as an AP-4d clarifying clause rather than an A3′ textual
amendment, the drafting choice the ruling delegated to the proposal),
and Q-D explicit no-tunability statement (appended to AP-4b,
[DS]+[COP], 3/5). Q-C: O-6 SEVERABLE from the CONV-013 round, BLOCKING
for AP-4-dependent shipping. Q-E: provenance disclosure SUFFICIENT and
already satisfied by the header below. AWAITING FOUNDER RATIFICATION —
nothing enacts until the founder ratifies; AP-2/AP-3 stand meanwhile.
On ratification: the full O-7 corpus sweep fires (the F-SW-7 audit's
registered entries — SR-1 glossary + master glossary DI-bit — resolve
in that pass); the SR-lineage reconciliation notes shipped at Patch
3030 convert from "ratification pending" to settled citations.**

**v1.0, Patch 3016 (6 Aug 2026). DRAFT for the dispatch-day panel round.
Founder anchor: `founders_voice/founder_specification_dibit_payload_automaton_2026-08-06.md`
(Patch 3015). Drafting provenance DISCLOSED: the §3 automaton sequence in
the anchor was Grok-drafted from founder text and founder-adopted; Grok
holds a panel seat and reviews this proposal — seats should weigh this in
their own returns.**

**Process:** panel-endorsement then founder-ratification, per the
AP-1/AP-2/AP-3 precedent (CONV-012 pattern). Batched with the MEAS-2
dispatch-day round. Nothing enacts before ratification.

---

## §1 — Proposed amendment text

**AP-4a (supersedes the AP-2 content clause under A1′):** A DI-bit
carries exactly **{origin address, electric vector E, strong vector S}**,
all imprinted by its originating GP at emission: E = the vector sum of
all polar-charge contributions (eCP and qCP indistinguishably; polarity
and magnitude folded into the vector; directions from contributor
addresses) integrated by the origin GP in the previous Moment; S = the
vector sum of all strong-charge contributions (qCP only), the separate
slot being the only species identifier. The imprint is a STATIC SNAPSHOT
of the origin GP's computed registers: the DI-bit carries no oscillator,
no evolving degree of freedom, and no per-messenger phase variable. The
receiver extracts SSV_net = E + S and SSV_abs per AP-4b. Every GP emits
the same fixed number of DI-bits every Moment.

**AP-4b (the absolute register):** SSV_abs = Σ|polar| + k·Σ|strong|,
with k > 1 a fixed universal constant encoding the intrinsic
strong-to-electric strength ratio, unchanged by external conditions
(environment acts only through arrival counts, directions, and geometric
dilution). k is subject to the identification obligation O-2 (§4) — it
enters as a citation of shipped derived couplings, not as a free
parameter. *(Q-D no-tunability statement, v1.1, folded per
[DS]+[COP]):* **k is substrate-determined and not tunable.** It takes
one value, everywhere, always: fixed by the intrinsic strong-to-electric
charge-strength ratio of the substrate itself, prior to and independent
of any configuration, environment, or observation, and identical at
every GP and every Moment. Nothing in CPP — no fit, no calibration, no
per-sector adjustment — may set, refine, or vary k; the programme's
only permitted act regarding k's value is *identification* with an
already-shipped derived coupling ratio per O-2. If no shipped
identification exists, the honest state is "k unidentified," reported
as such — never "k fitted." This preserves the zero-parameter posture:
k is a substrate constant awaiting recognition, not a dial.*

**AP-4c (transit and reset — AP-3 clarification, not correction):** the
imprint is invariant during the sub-Planck transit from GP_origin to its
PSR shell; deposit occurs exactly once, at the shell; the DI-bit resets
upon delivery (absorbed one Moment, re-emitted the next with a fresh
imprint). AP-3's "reset per hop" is hereby pinned to the Moment-level
(origin→PSR) reading. The pass-through tally (intermediate GPs reading
transiting DI-bits) is EXCLUDED; near-field information is carried by the
relay recursion (each GP's own per-Moment re-emissions).

**AP-4d (emergence of the broadcast channels):** the A3′ LSP′ packet
(Φ, V_i, Q_ij — the nine protected irreps) is the GP's COMPUTED STATE,
reconstructed each Moment by receiver-side summation of arriving
payloads; only {origin address, E, S} rides the messenger. All
gravitational parameters are emergent (founder ruling Q2). Energy has no
payload slot: energy in all its forms is an emergent low-entropy
configuration of CPs/DPs/unpaired CPs, seen by the census through the
Sea polarization it maintains (anchor §5).

*(Q-B clarifying clause, v1.1, folded per [Gemini][DS][COP]; drafted as
an AP-4d clarifying clause rather than an A3′ textual amendment — A3′'s
ratified text is untouched):* **Wherever A3′ or any downstream text
speaks of the LSP′ packet being "broadcast," "transmitted," or
"carried," the referent is the computed state that receivers
reconstruct, never additional messenger content: messenger content is
exhaustively {origin address, E, S}, and everything else attributed to
the broadcast channel — Φ, V_i, Q_ij, SSV_net, SSV_abs, and all
gravitational parameters — is computed state, produced receiver-side by
summation over arriving payloads.** The division is exclusive and
exhaustive: every quantity in the theory is either (i) messenger
content (the three payload slots), or (ii) computed state (a GP
register or a function of GP registers); no quantity is both, and no
third category exists.*

## §2 — Reconciliation arguments (for the panel to test)

**I-1 (the no-phase invariant, restated — Q-A amendment, v1.1, folded
per [COP], 4/5 confirm-class).**

*Invariant:* **No per-messenger phase degree of freedom exists anywhere
in AP-4, and none of AP-4's obligations (O-1..O-7) can reintroduce
one.** Precisely: the DI-bit's state space is the static tuple {origin
address, E, S} (AP-4a), imprinted once at emission, invariant during
transit (AP-4c), and reset at delivery; a phase degree of freedom would
require either (i) a messenger variable that evolves during transit —
excluded by AP-4c's invariance clause — or (ii) a compact variable in
the payload beyond the three enumerated slots — excluded by AP-4a's
exhaustive enumeration. The orientations of E and S are not phase
degrees of freedom: they are frozen images of the origin GP's register
orientation, carrying no dynamics; the phase-equivalent content of the
theory is the RECEIVER's SSV_net orientation register (FI-QMRG-1:
φ = SSV_net orientation), reconstructed by summation, exactly as R-1
below states.

*Proof sketch that the identification obligations reintroduce no phase
degree of freedom (obligation by obligation):*

- **O-1 (census-tracks-energy):** a receiver-side scaling claim about
  aggregate census perturbations; consumes counts and magnitudes only;
  adds no messenger state.
- **O-2 (k identification):** k is a fixed universal scalar constant in
  the receiver-side summation rule AP-4b — and now, per the Q-D clause,
  explicitly non-tunable. A constant is not a degree of freedom, let
  alone an oscillating one, and k appears nowhere in the messenger
  tuple.
- **O-3 (conservation-under-recursion):** a ledger property of fixed
  emission counts and shell dilution; states no new variable.
- **O-4 (F-E2-3 arrival-band):** a transit-property formalization.
  AP-4c fixes the imprint invariant during transit, so any arrival-band
  reading constrains delivery timing and geometry, never messenger
  content.
- **O-5 (Q_ij emergence):** derives the tensor register as
  receiver-side computed state (AP-4d); by construction the derived
  object lives in the GP register, not on the messenger.
- **O-6 (W-MULTILINK-1 re-runs):** re-derivations conducted UNDER
  AP-4a's premises, which include the snapshot clause; any derivation
  admitted through O-6 that irreducibly required per-messenger phase
  dynamics would trip the falsifier F-AP4-1 rather than amend the
  payload.
- **O-7 (corpus sweep):** editorial; touches text, not ontology.

*Closure:* every obligation either (a) operates receiver-side on
registers and aggregates, (b) concerns a fixed constant, or (c) is
editorial; none has write access to the messenger tuple. The invariant
is therefore stable under the discharge of all seven obligations, and
F-AP4-1 (§5) remains the standing falsifier should any future
derivation contradict this sketch.

**R-1 (the no-phase clause).** The 2957 ruling (AP-2's provenance)
retired the COHERENT-FRONT picture: a per-messenger oscillating phase
degree of freedom. AP-4a carries a static snapshot of the source's
SSV_net register — the phase-equivalent content lives in the GP register
(FI-QMRG-1: φ = SSV_net orientation), and the messenger transports a
frozen image of it, not an oscillator. The proposal's claim: everything
F-AP2-1 protected (no derivation may irreducibly require per-messenger
phase dynamics) survives; the falsifier is restated as F-AP4-1 (§5). The
panel is asked to CONFIRM or BREAK this reading.

**R-2 (the exclusion-theorem premises).** The 3005 T1 theorem quoted
AP-2's minimal content as Clause 2 ("one arrival carries one edge's
data"). Under AP-4a one arrival carries an aggregate over the source's
whole environment — the premise as quoted breaks, and W-MULTILINK-1 has
FIRED. The proposal's claim: the conclusion survives because the
formation rule remains pure vector addition over arrivals with no
cross-terms between distinct arrivals (the property that actually
protected the plane), and the per-Moment reset (AP-4c) still closes the
receiver-memory route. This claim must be RE-DERIVED, not asserted
(obligation O-6).

**R-3 (SR/gravity corpus).** Under AP-4, c07's "the LSP carries four
quantities" becomes substantially TRUE AS WRITTEN (the payload is
{address, E, S}, an LSP in miniature), while the nine-channel packet
language reads as computed state (AP-4d). The SR-lineage audit (F-SW-7)
holds its R-B/R-C classifications pending this proposal's outcome.

## §3 — What survives untouched

Count-like magnitude reasoning (SSV_abs remains a census); the fixed
per-GP emission count (the premise of exact shell dilution, verified at
2959); AP-3's compute/hold/refresh protocol and synchronous absorb/emit;
A3′ C1–C5 (the amendment adds an emergence reading, changes no clause);
the QM re-ground's register identifications (FI-QMRG-1, B-QMRG-1) at the
GP level.

## §4 — Obligations (attach to AP-4; none dischargeable by assertion)

- **O-1 (census-tracks-energy, CENTRAL):** derive that the census
  perturbation from a configured region scales linearly with its stored
  energy (required by SR-1's PSR formula and c05's mc²-proportional
  Q_grav). Verify script mandatory.
- **O-2 (k identification):** identify k with the shipped
  strong-to-electric coupling ratio. Leads: the founder's recalled ~67;
  the factor 3(11+5√5) ≈ 66.54 inside α_geom (c02); the
  α_s = 5/(8φ) (SM-7) to α_geom/SF-6 ratio route. If no shipped
  identification exists, report that finding to the panel as such.
- **O-3 (conservation-under-recursion):** extend the 2959 outbound
  conservation result to the full re-emission loop (fixed emission count
  + shell dilution as the ledger; no amplification, no bleed).
- **O-4 (F-E2-3 disposition):** formalize the founder-adopted ~10%
  arrival-band reading (transit property) against options (b)/(c) of the
  2959 record; state observable consequences if any.
- **O-5 (Q_ij emergence sketch):** derive the tensor register as the
  protected second-level summary of arriving payloads (the H-irrep
  stretch/squash pattern), completing the emergence reading of AP-4d the
  way FI-QMRG-1 grounded the phase register.
- **O-6 (W-MULTILINK-1 re-runs):** re-run the 3005 exclusion analysis,
  the 3002 B-1 fork (its rival was excluded via AP-2's intensity-like
  clause; AP-4b's census form is the survival claim), and the CONV-016
  dependency chain under AP-4a premises BEFORE anything ships on them.
- **O-7 (corpus sweep):** on enactment, sweep the QM/SR corpora for
  AP-2-content citations (the 2998 template), including the glossary
  DI-bit entry; the F-SW-7 audit's held classifications resolve in the
  same pass.

## §5 — Falsifiers

- **F-AP4-1:** a derivation that irreducibly requires per-messenger
  phase DYNAMICS (an oscillator on the DI-bit, beyond the static
  register snapshot) falsifies AP-4a's snapshot clause.
- **F-AP4-2:** failure of O-1 (census provably NOT proportional to
  stored energy in the required regimes) falsifies the no-energy-slot
  clause AP-4d and returns the payload question to the founder.
- **F-AP4-3:** an inverse-square failure under Version B + fixed
  emission count (extending F-AP2-2) indicts the census/dilution
  reading.
- **F-AP4-4 (inherited):** F-AP3-1 stands unchanged.

## §6 — Questions to the panel (v1.0 draft wording; RESOLVED at CONV-013)

Q-A: does R-1 preserve what the no-phase ruling protected (CONFIRM /
BREAK / CONFIRM-WITH-AMENDMENTS)? Q-B: is the AP-4a/AP-4d split
(messenger content vs computed state) the correct reading of A3′'s
packet language, or does A3′ require textual amendment? Q-C: are the
O-1..O-7 obligations correctly scoped and correctly BLOCKING (which must
complete before enactment vs after)? Q-D: does AP-4b's k, entered as an
identification obligation, preserve the zero-parameter posture? Q-E:
arc-integrity check on this proposal's provenance handling (Grok
drafting disclosure sufficient?).

**Outcomes (CONV-013 completion adjudication, Patch 3023; record:
`series_phenomena/cosmology/dark_matter/conv013_2026-08_returns_adjudication.md`):**
Q-A CONFIRM-WITH-AMENDMENTS (4/5 confirm-class) → §2-I above. Q-B
AMENDMENT-REQUIRED (3/5, final reversal of the 2–2 interim) → the
AP-4d clarifying clause above. Q-C O-6 SEVERABLE from the round,
BLOCKING for AP-4-dependent shipping (4/5). Q-D PRESERVES (3/5) → the
AP-4b no-tunability statement above. Q-E SUFFICIENT (3/5; the header
provenance disclosure already satisfies [COP]'s amendment). Enactment
authority: FOUNDER RATIFICATION of this v1.1 text.
