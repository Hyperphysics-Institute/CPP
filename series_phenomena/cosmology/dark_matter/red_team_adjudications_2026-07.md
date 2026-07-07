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
