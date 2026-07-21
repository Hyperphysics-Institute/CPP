# Red-team adjudications — open, per-return, computation-level (started Patch 2310, 6 July 2026)

Per the brief's promise: every KILL/WOUND receives a written computation-level response here. Findings
are adjudicated CONFIRMED / PARTIAL / DISMISSED, each with its decisive check executed and its
consequence routed (normative-table amendment now; paper errata queued to `deposit_errata_queue.md` for
the release-day v1.0.1 fold; stability-cycle impact ruled explicitly).

## Return 1 — ChatGPT (6 July). Headline: NO KILL; 5 WOUNDs. Adjudication:

**W1 (slope law is capture-only) — CONFIRMED, protocol-level; FIXED; cycle intact.**
Reproduced exactly (verify `code/2310_...py`): the total-σ slope departs from the capture slope where
the floor contaminates (52% capture fraction at 600 km/s; 13% at 1150). The law and the paper's p-values
are correct AS STATED (the paper defines p for σ_cap); the *operational* protocol was under-specified.
**Fix (normative table amended):** the inversion runs either in the capture-dominated window
(cap/total ≥ 0.9, v ≲ 250 km/s — where p still runs 0.6 → 1.8, a factor 3: fully invertible) or
floor-subtracted using the published measured floor (registered data). **End-to-end demo executed:**
floor-subtracted slopes at 20 & 150 km/s invert to R_s = 25.4 fm → χ_inv = 0.0393 — exact recovery —
with a slope-only consistency identity ((4/p₁−1)/(4/p₂−1) = √(σ₁/σ₂) = 2.899 = 2.899) that is
**amplitude-free**: a zero-freedom shape test the finding forced us to articulate. The wound made the
protocol stronger. Cycle ruling: no quantitative paper claim moved (the paper's numbers are capture
slopes, correctly labeled); operational sharpening + one abstract-sentence clarification queued as
release-day erratum.

**W2 (χ-from-the-sky circularity) — PARTIAL; protocol sharpened.**
The charge fails against the shape channel and half-lands against the absolute channel. As the W1 demo
shows, the p-running consistency test is amplitude-free — blind to the dwarf normalization by
construction. The ABSOLUTE R_s extraction needs one amplitude (any single σ/m point + m_rod) — the
protocol now says so explicitly and does not privilege the dwarf pin. Model-conditionality was already
folded at v1.0 per panel. Decisive check (blind slope-only refit) is exactly the amended protocol's
shape test; DEMONSTRATED above.

**W3 (comparator under-generalized) — DISMISSED, by the decisive check the finding requested.**
Executed (`code/2310`): the realizable single-mediator Yukawa transfer family (Born + classical,
Tulin–Yu-class approximants; 2 parameters fitted to the same anchors) attains at most
**σ/m(1150) ≈ 1.0×10⁻³ vs the CPP floor 0.046 — short by ×46**; 1500/3500 worse. The
arbitrary-power-law loophole (v^−1.26 fits the anchors and yields 0.088) is closed by realizability:
sustaining that exponent to 1150 requires β(1150) > 1, which forces a near-flat log² curve at 50–200
and breaks the anchor ratio. S1 STANDS; the "representative family" wording was already folded at v1.0.

**W4 (Javorsek citation) — CONFIRMED, bibliographic; corrected.**
PDG listing confirms two distinct papers: PRD **64** 012005 (SIMPs bound to gold — actually the MORE
on-point citation for a rod-bound Au nucleus) and PRD **65** 072003 (anomalous Au/Fe nuclei search).
The pin's substance (Au searched in-window; limits 10⁻¹¹–10⁻⁸; ≥4-order margin) is intact under either.
**Fix:** normative table now cites both; paper erratum queued; original-figure digitization added to the
release-day checklist. Cycle intact (no number moved).

**W5 ("certified" overstates) — CONFIRMED, wording; erratum queued.**
DM-2's own §8 says "at the stated conditional level"; DM-3's §1/abstract compress it to "certified."
Cross-paper consistency fix: "conditionally certified" in DM-3, release-day erratum. Cycle intact.

**Return-1 summary: 0 KILL / 2 CONFIRMED (protocol + bibliographic, both fixed) / 1 PARTIAL (protocol
sharpened) / 1 DISMISSED by computation / 1 wording. Zero quantitative claims moved; the stability
cycles stand; the falsifier suite exits STRONGER (an amplitude-free shape test now exists that did not
before).**

## Returns 2–5 — Grok, Gemini, Copilot, DeepSeek (6 July). Panel complete.

**Attribution note:** an early duplicate paste (Copilot's text delivered twice) was resolved by the
founder's re-delivery; DeepSeek's genuine return arrived last. Final set: ChatGPT (5W), Grok (2W+1S),
Gemini (1 KILL-claim + 2W + 1S), Copilot (auditable NO FINDINGS, 9 surfaces), DeepSeek (1 KILL-claim +
1W + 1S).

### The two KILL claims — the round's center of gravity

**GEMINI KILL (no dissipation channel at dwarf energies) — CONVERTED TO A NAMED GATE
(OPEN-DM-CAPTURE-1); neither confirmed nor dismissed today.** Verify `code/2311_...py`: the sub-gap
kinematics CONFIRM every gapped channel closed (encounter ħω is 10²–10⁴ below m_s, E_ee, rod
vibration/rotation — Gemini right on each); the premise "no light mediator" is FALSE against the
registered gapless |SSV| mode (1107–1108) — but that mode's coupling to a moving rod pair is
unregistered. The claim therefore identifies a genuinely un-derived load-bearing assumption. Routed:
the gate file, window priority #1, release-decision rule pre-stated. This is the round's most valuable
finding and precisely what the brief asked for.

**DEEPSEEK KILL (rigidity/J4 breakdown at cluster velocities) — DISMISSED BY ITS OWN ARITHMETIC, with
a legitimate residue queued.** Their computed sound speed c_s ≈ 0.1c vs cluster velocity 0.005c: the
motion is SUBSONIC by ×20, the collision adiabatic (stress waves cross the rod ~400× during the
encounter), the rigid-body treatment validated — their "supersonic" premise contradicts their own
numbers. Residue extracted and QUEUED (J-FLOOR-FOCUS): does the measured floor include field-focusing
where V_contact ~ KE (cluster velocities)? Even a ×2 floor clears Andrade (0.07–0.08 vs 0.13) —
refinement-class, not kill-class; one MC rerun with the potential on settles it.

### The wounds — adjudicated or queued with sizing

**Gemini W2 (solar accumulation/helioseismology) — QUEUED, sized (`code/2311`):** geometric-ceiling
accumulation is 2×10⁻¹¹ M_⊙ — eight orders below mass-fraction sensitivity; the queued computation is
CONDUCTION-focused (the rods' huge self-scattering vs rod-nucleon transport at S_c in solar plasma). A
genuinely new confrontation surface; window task.
**Gemini W3 + DeepSeek W (VDF sensitivity: p(v) smearing; XQC halo-model dependence) — MERGED and
QUEUED:** one computation covers both — convolve σ_cap(v) and the XQC rate over SHM++/Gaia-class VDFs;
report p_obs variance and the F5 band's movement. The F-DM3-2 protocol already carries the
"observationally ambitious" caveat; this quantifies it.
**Gemini SCRATCH (formation latent heat vs N_eff) — DISMISSED (`code/2311`):** fractional bath
injection ~3×10⁻⁸, seven orders below N_eff sensitivity.
**Grok W1 (P(v) < 1) — MERGED into OPEN-DM-CAPTURE-1** (the soft form of the same physics; his
decisive check — re-anchor with P(v) and propagate — is the gate's partial-efficiency branch).
**Grok W2 (formation-N vs floor-N reconciliation) — CONFIRMED as an open reconciliation; QUEUED**
(1855-style kinetics with capture+floor active → N distribution → floor check; the decisive check as
specified).
**Grok SCRATCH (Javorsek digitization) — already on the release-day checklist** (with the W4 dual-cite
fix from return 1).
**DeepSeek SCRATCH (Λ-coefficient circularity charge) — PARTIAL; folded into Gate-1/B1's scope:** the
1/8π rides on the c05/c07 field-energy normalization; the reduction must DERIVE that normalization,
not import it — added to the Gate-1/B1 claim-set. The paper's conditionality already points there.

### Round synthesis

0 confirmed KILLs. 1 named gate opened (the round's crown finding, convergent with our own DM-4
prospectus). 4 queued window computations (solar conduction; VDF sensitivity; formation-N
reconciliation; floor-focusing). 2 dismissals by executed arithmetic. 2 auditable nulls (Copilot;
Grok's checked-surfaces list). Zero quantitative claims moved; the stability cycles stand; the papers
rest. **The window's priorities are now: OPEN-DM-CAPTURE-1 + Gate-1/B1 (joined derivation campaign),
then the four queued computations, then the release ritual.**

### W2 execution update (Patch 2328, 7 July 2026)

**Grok W2 EXECUTED** (`grok_w2_formation_floor_reconciliation.md`, `code/2328_...py`, 8/8): static
reconciliation PASSES (N_form 3–27 ∋ floor-N 18 ≤ ceiling 18–21); formation-epoch capture
reach-dead (Θ_crit(337 km/s) = 1.59 > 1) — the 1855 endpoint stands. NEW SURFACE: post-formation
free-streaming descent activates capture in the radiation era for EVERY spectrum under D = const
(survive window z ~ 5×10⁷ at ~10⁵/Hubble; light-speed cap z ~ 1.3×10⁷ at ~10⁴/Hubble; bare Ohmic
borderline O(1) at z ~ 10⁴) → the monomeric anchor-calibration population does not survive to the
halo era → **OPEN-DM-AGG-1 registered** (routes: (i) D(T_amb) cooling history — delivered by the
same Stage-3 D derivation that decides G4; (ii) endpoint reproduction via the d_f map, disfavored).
Dynamic reconciliation CONDITIONAL on AGG-1; no registered verdict moved; survive branch now reads
PRW-D ∧ route-(i) history.

### Stage-3 execution addendum (Patch 2330, 7 July 2026)

**D(T_amb) DERIVED** (`gate1_b1_G4_stage3_D_of_Tamb_derivation.md`, `code/2330_...py`, 12/12):
harmonic-null theorem (coherent transport = 0 exactly under the no-carried-velocity ruling) ⇒
activated two-channel law knee_tot(T) = ħ[D_hop k² + Γ_loc], monotone in T. **Route (i) of
OPEN-DM-AGG-1 is now half-closed, half-narrowed:** the transport half CANNOT deliver it (hop knee
≤ 324 keV < 579 keV pin requirement — the W2 light-speed row is the derived optimum of the whole
hop branch); the surviving half is R-III (above-gap activated creation), generic under
free-streaming cooling, protecting to v_edge = 0.15 km/s ((1+z) ≈ 3.1×10⁴). Residual registered as
**AGG-1-R**: the tail integral below v_edge under the derived law with a specified T_amb(z)
(window-D ceiling 17/Hubble at onset, marginal by construction). New surface **OPEN-DM-TAMB-1**
(closure bound: thermalized gapless mode caps T_amb at 3.2 meV; bites the corner ×10²⁹ and the F7
soft target ×6.5×10²⁶; two-temperature Sea or one-ledger exemption required). W2's dynamic-layer
condition now reads: AGG-1 ⇐ R-III history ∧ AGG-1-R tail ∧ TAMB-1 evasion.

### TAMB-1 sharpening addendum (Patch 2331, 7 July 2026)

**Uncertainty floor** (`gate1_b1_tamb1_uncertainty_floor.md`, `code/2331_...py`, 6/6): closure is
mechanism-independent — ρ ≥ knee_tot/R_s³ for any activated window knee (×10³⁴⁺ today; ×10¹²–10²³
over radiation in the R-III era). Evasion (a) closed-insufficient; the W2 dynamic-layer condition
tightens to: AGG-1 ⇐ R-III history ∧ AGG-1-R tail ∧ **TAMB-1(b)** (one-ledger status of dynamical
Sea excitation — the sole surviving evasion, a G-sector derivation).

### TAMB-1(b) resolution (Patch 2333, 7 July 2026)

**Derived — fails** (`gate1_b1_tamb1b_one_ledger_status.md`, `code/2333_...py`, 7/7): the
apparatus's one zeroing mechanism (Σv̂ = 0) reaches exactly the gradient-free component;
harmonic-null forces knee-carriers to be localized events; Case-3 provenance-blindness and
C-d form-blindness exclude any discriminant; DM-2 §5's own Λ already sources a Sea
excitation ×5×10³⁹ gentler in gradient. Exemption = inconsistency, not open-ness. Corner
DEAD; G4 → KILL-on-suite-conditional per pre-registered outcome (ii). **Panel: attack
check 3 (the a-fortiori anchor) first — it is the load-bearing novelty.** Kill stack =
corner stack (symmetric; no selective exposure).

### The attraction MC (Patch 2336, 7 July 2026)

**Measured** (`gate1_b1_attraction_mc.md`; grading 6/6): the 2335 in-prior elastic
closure holds by direct MC — measured low-v slope s = 0.85 (envelope said ≤2; bars
need ≥2.71 / ≤1.42 jointly). Suite fails on dSph ×2.1 (8.8σ) and the pin/LSB
simultaneity. **Texture corrected:** the killed candidate is a velocity-dependent
elastic SIDM near-miss (×486 dynamic range, cluster-safe, LSB-grazing), NOT a flat
0.046 relic. **Panel note:** the classical-MC flag is now load-bearing at the ×2
margin; the quantum s-wave treatment and the unregistered S_ATT(N) scaling are the
two named founder-gated follow-ups. Verdict untouched.

---

# SECOND WAVE — five returns registered 20 July (Patch 2682); TRIAGE + release-gate ruling; full computation-level adjudication = RELEASE SESSION agenda item 1

**Returns verbatim: `red_team_returns_2026-07-20_verbatim.md` (R-A…R-E,
attribution PENDING FOUNDER — paste labels supplied blank). Per the
brief's promise, every KILL/WOUND receives a written computation-level
response; this section registers the TRIAGE (dedupe into finding
classes, record-answered items pointed at their records, computation
checks named and queued) and rules on the release gate. Nothing below is
a final adjudication except where marked; final CONFIRMED/PARTIAL/
DISMISSED rulings execute in the RELEASE SESSION with the papers and
code open.**

## Release-gate ruling (now, Patch 2682)

Three KILL-class claims are on the table (T2, T3, T4 below). None is
CONFIRMED; none is dismissible without computation except T4a (whose
dismissal computation is one line and is executed below). **Per plan
§Release gates, the deposit (items B5–B6) is PAUSED-PENDING-ADJUDICATION
of T2/T3/T5. This is the gate working as designed, not a schedule slip:
the wave came back same-day and the adjudication was already scheduled
(B4) ahead of sign-off.**

## Triage classes (deduped across R-A…R-E)

**T1 — Relic abundance / production history** (R-A F1; R-E S2 BBN
energy-injection). Record: the relic question is REGISTERED OPEN —
OPEN-DM-RELIC-1 stands at charter level with target T1 = n_ring/n_b =
0.4468 ± 0.0054 and BOTH naive readings failing at open (charter v1.1
FROZEN, panel-amended). RELEASE SESSION check: verify the three papers
STATE the relic status as open/conditional rather than claiming a closed
production history (if any sentence overclaims → WOUND, erratum; if the
disclosure is present → PARTIAL, pointer response). R-E's BBN
energy-injection remedy is queued as an OPEN-DM-RELIC-1 campaign
sub-item, not a release blocker, unless the papers claim BBN safety
quantitatively (check in-session; R-E quotes a sentence — verify it
exists as quoted).

**T2 — CMB momentum-transfer bounds on σ_DM-baryon (KILL-class; R-C
K1).** The genuinely new confrontation of the wave: Planck-era
DM-baryon scattering limits (Gluscevic/Boddy parameterization) vs the
σ_DM-b implied by the capture/overburden physics at 25 GeV. Not in the
existing confrontation ledger by name. RELEASE SESSION computation:
extract the registered σ_DM-b (velocity dependence included — the
capture channel is dissipative/composite, NOT a constant elastic σ, and
the v-scaling between recombination (~10⁻⁶ c thermal) and terrestrial
(~10⁻³ c) regimes is exactly where this check will be decided); compute
the recombination-era momentum-transfer rate; compare to the published
25 GeV bound. CONFIRMED → release pauses per gate; DISMISSED → the
computation joins the confrontation ledger as a new passed row (the
attack strengthens the arc either way).

**T3 — SIDM cluster bounds on σ_self/m (KILL-class; R-D F1).**
PRELIMINARY-DISMISSAL-PENDING-VERIFICATION: the finding is explicitly
conditional ("IF DM-1's σ_self/m band overlaps or exceeds ∼1 cm²/g"),
and the paper's registered band — σ_V/m ≈ 0.11–0.20 cm²/g halo-scale,
0.037–0.05 cm²/g group-scale, velocity-independent — sits a factor
5–25 BELOW the quoted exclusion threshold, on the reviewer's own
numbers. RELEASE SESSION: verify the band from the paper text, execute
the v ≈ 1000 km/s recomputation the reviewer names, write the
DISMISSED (or otherwise) ruling with the numbers in the response.

**T4 — XQC astrophysics** (R-E K1 focusing; R-D W2 halo ensemble; R-A
S4 single-pipeline).
- **T4a (R-E K1, gravitational focusing "factor 2–3") — DISMISSED at
  computation level, here.** Gravitational focusing enhancement for a
  collisionless flow scales as 1 + (v_esc/v∞)² at the body. Earth:
  v_esc = 11.2 km/s against a halo flow v∞ ≈ 220 km/s →
  1 + (11.2/220)² = 1.0026 (0.26%). Sun at 1 AU: v_esc,☉(1 AU) =
  42.1 km/s → 1 + (42.1/220)² = 1.037 (3.7%), and the annual-average
  focusing correction used in the direct-detection literature is at the
  percent level. A "factor 2–3 density enhancement" at 250 km altitude
  for a 220 km/s flow is off by ~two orders of magnitude and would
  require v∞ ≈ v_esc, i.e., a gravitationally bound population — which
  is not the halo model under attack. "Solar radiation pressure effects"
  on dark matter is not a mechanism (DM is not photon-coupled at any
  strength relevant here — that is the arc's own point and also the
  reviewer's elsewhere). No release impact. (Verify script queued for
  the RELEASE SESSION as a one-liner for the record; the arithmetic
  above is complete.)
- **T4b (halo-model bracketing, R-D W2):** legitimate protocol check —
  whether the XQC confrontation brackets ρ ∈ [0.2, 0.6] GeV/cm³ and
  v_0 ∈ [180, 260]. RELEASE SESSION: read the paper's stated margin
  (the record cites ×20–30 exclusion margins in the J4-additive case
  and order-of-magnitude margins elsewhere — a ×2–3 halo systematic
  does not move a ×20 margin; state this with the paper's numbers).
- **T4c (single-pipeline reproducibility, R-A S4):** fold as a deposit-
  record item (manifest already lists 49 scripts; the residual scan
  confirms the XQC chain end-to-end or notes the gap honestly).

**T5 — Born-regime S_c² overburden scaling at low velocity
(KILL/WOUND-class; R-C W2 + R-E K2, same physics).** The sharpest
technical attack of the wave and the one the first-wave round did not
hit. RELEASE SESSION computation: (i) establish what the papers
actually claim the S_c² scaling FOR (shielding suppression en route to
deep detectors) and in which velocity regime; (ii) check the Born
validity criterion in that regime against the registered potential; if
Born fails where the paper uses it, quantify the direction of the error
(NOTE: Born breakdown at low v generically INCREASES stopping — which
STRENGTHENS shielding/suppression conclusions where the paper's claim
is "the flux is stopped/degraded" and WEAKENS them where the claim is
"flux survives to depth X" — the direction question is the whole
adjudication and must be answered against the paper's actual claim
structure, not in the abstract).

**T6 — Cross-paper parameter/J4 ledger** (R-A W3; R-D F3; R-C S3; R-E
W1). Record: the six-axis DEP-1 dependency ledger and
`n2b_dep1_dependency_ledger.md` already exist for the candidate-B
validation lane; the papers' own cross-paper ledger is the residual-scan
deliverable (B3). RELEASE SESSION: produce the single-table ledger the
reviewers ask for (E_c, pitch, χ, floor — value + scope + provenance per
paper); any mismatch found = WOUND with erratum; expected clean (the
1892 deposit record already manifests provenance). R-E W1's three-body
additivity check at rod spacing: NOTE the scale error to correct in the
response — R-E quotes d_DP = 0.589 fm and reads ℓ = 0.091 fm as
"comparable to interparticle spacing"; ℓ/d_DP ≈ 0.25 wait — this ratio
and its consequence for pairwise additivity at rod scale is a REAL check
worth one computation (three-body correction under exponential
screening at spacing ≈ 4ℓ is suppressed ~e^{-2·(extra path)/ℓ}; make
the estimate concrete in-session). Also correct in the response: R-E's
d_DP value (the registered d_DP = ℓ_edge = 0.364 fm in the FA lane;
0.589 fm is a different quantity — identify which the papers use where,
this is itself a T6 ledger row).

**T7 — Disclosed-tension items re-attacked** (R-B F1 IC 2574; R-B F2
Sagunski 2.3σ). The reviewer's own quotes show the paper DISCLOSES both
(the under-prediction and the 2.3σ). RELEASE SESSION: verify the
disclosures are load-stated (abstract-level where load-bearing), then
rule PARTIAL (presentation) or DISMISSED (already-disclosed
confrontation, reviewer confirms the numbers) — the F2 charge that
"similar margins are treated as exclusions elsewhere" deserves one
honest paragraph on the asymmetry (a 2.3σ *shortfall against one
measurement with large systematics* vs a ×20 *exclusion margin*).

**T8 — Conditional-status propagation** (R-B F3 first-multipole; R-B F5
propagation; R-B F4 Gate-1/B1 + L insertion). Record answers exist:
the first-multipole conditionality is IN THE PAPER as quoted by the
reviewer (v1.2 retraction disclosed; survival conditional — that is
the honest state, and F5-class falsifiers carry it); Gate-1/B1 is NOT
open — the campaign EXECUTED post-brief (2310–2336, TAMB-1(b)
resolution; errata-queue items 5–6 already anticipate exactly the §2/§5
wording upgrades). RELEASE SESSION: point F4 at the campaign record +
fold the queued errata; respond to F3/F5 with the registered
conditional-claims policy (conditions carried in-paper, falsifier-
classed) and the ±factor-2 propagation exercise the reviewer names IF
cheap (else queue with owner).

**T9 — DM-2 scope/wording** (R-B F6 referential zero; R-D F6 shell-sum
vs later Sea structure; R-E S3 priors). SCRATCH-class; fold candidates
for the errata queue. R-D F6 note: the FA-SEA-GREEN sign-staggered
result is CANDIDATE-B-LANE, fm-scale, observation-grade, and fenced
(F1–F4) — the DM-2 shell-sum scope sentence can cite the registered
rider without importing the result; draft at RELEASE SESSION. R-B F6's
requested paragraph (referential zero from the axioms) EXISTS as
D2/1161 (symmetry-enforced monopole annihilation, Σv̂ = 0 — exactly the
"not by construction" derivation asked for); errata-queue item 5
already queues this wording; extend it to note the staggered-response
compatibility question as registered (the zeroing is of the absolute-
|SSV| monopole; the staggered component is a gradient structure the
mechanism does not touch — one sentence, verify in-session).

**T10 — "1871" misreadings** (R-D F4; R-E S1; R-B F1c usage). **1871 is
a PATCH NUMBER** (the measured-floor MC of Patch 1871, July 2026), not
the year 1871 and not "1871 MeV." R-E attacked a nonexistent
19th-century apparatus ("historical apparatus diagrams … thermal
expansion"); R-D rendered it "1871 MeV measured floor." DISMISSED as
posed, both — but the misreading is diagnostic: if two independent
reviewers parse the label as a year/energy, cold readers will too.
**Erratum queued (new item): rename/gloss on first use in every paper
and companion — "the measured floor (Patch 1871 MC)" — and the
deposit-record manifest entry likewise.** R-D's underlying geometry-
robustness question (floor spread under motif/box/boundary variation)
survives the misreading as a fair check: answer in-session from the
1871 MC's own registered robustness content, or queue with owner if
absent.

## RELEASE SESSION agenda (supersedes the bare B4 row; order is severity)

1. T2 computation (CMB σ_DM-b bound) — the live KILL check.
2. T5 computation (Born validity + direction ruling) — the live
   KILL/WOUND check.
3. T3 verification (paper band vs SIDM bounds) — expected DISMISSED
   with numbers.
4. T4a verify one-liner; T4b margin statement; T6 ledger table (+ the
   ℓ/spacing three-body estimate + the d_DP row); T7/T8/T9 record-
   pointer responses; T10 erratum fold.
5. Then B1–B3 as scheduled (deposit records, reader's guide, residual
   scan — the scan now cites this section).
6. Errata queue updated throughout; gate re-assessed at close: all
   KILL-class DISMISSED → B5 sign-off unblocks.

**Attribution:** final per-return credit lines are written when the
founder confirms the R-A…R-E ↔ seat mapping.
