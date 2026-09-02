# Changelog — GR-2: The Echo Falsifier

**Paper:** `series_gravitation/papers/GR-2_echo_falsifier.tex`
**Convention:** canonical filename never carries a version suffix.

---

## V0 — 21 August 2026, Patch 3329 (Session 156)

Assembly draft, opened on the founder-ratified CONV-032 adjudication
(verbatim "Ratify the bundle. Please proceed with GR-2"). Complete
input set inherited at ratified strength: F-R1 (CONV-030), |R| = 1
(GR-1d V3, spin-independent), Schwarzschild closed form (3/2 + 8 ln 2)
GM/c³, derived Kerr exclusion surface + censorship theorem +
prograde-burial finding (Patch 3320; CONV-032 5/5,
derivation-conditional on A1–A3), binding error-bar rider. Claim
discipline: conditionality leads the abstract; no new derivations; no
new predictions (PRED-O-39 is the paper's single quantitative content;
swarm count unchanged). PD-001 suite in from the start (Keywords, PLS,
CP/GP Signature, Mechanism Bridge, Swarm-Validation, Verification).

**Verify:** `code/3329_gr2_template_verify.py`, 9/9 PASS; FAST subset
4/4 (first enactment of the CONV-032 FAST-mode dispatch adoption).
**Finding surfaced by the script's own first run:** the template
SATURATES in spin above burial onset — dΔt/dχ = 0.299 GM/c³ at
χ = 0.68, so the mandated ±0.1 spin bar is ±0.35% (mass ±6.5%
dominates ~20×); the worker's prior 3–10% expectation was wrong and
is recorded in the script header per computation-before-claims. The
strong spin lever lives below onset (2.151 → 2.607 ms across
χ = 0 → 0.55); for the remnant population the template is effectively
mass-only.

Compile gate: pdflatex ×2, 0 errors, 0 undefined refs, 7 pages.
Standing: V0 / inputs reviewed, assembly NOT yet panel-reviewed —
a CONV round is the natural next gate before any V1.0/ship move.

## V1.0 — 21 August 2026, Patch 3332 (Session 156) — SHIPPED

Review basis: CONV-033, 5/5 same-session, Q7b V1.0-PREP-CLEAR 4–1
(`review/conv033_adjudication.md` v1.0). The adjudication's six
adopted revisions folded at the bump (GR-1i/CONV-029 fold precedent;
the minority's restate list IS the fold list): (1) amplitude grade
split — |R| = 1 exact/parameter-free vs ~5% transmission as an
argument-level GR-1d estimate, in abstract, §4 (retitled "exact
reflectivity, estimate-grade transmission"), and PLS; strike
condition retained at estimate grade; (2) "effectively mass-only at
equatorial eikonal grade" at every occurrence incl. conclusion;
(3) search-coverage claim cited (Abedi+2017; Westerweck+2018;
Tsang+2020 — supplied in-round by the falsifier seat) and bounded to
"surveyed here"; (4) null falsifier operationalized: preregistered
injection-recovery-efficiency criterion at the predicted delay and
amplitude; (5) discriminator scoped: CPP surface ordering vs
horizon-keyed templates, not uniqueness over all ECOs; (6) dedicated
abstract sentence naming the eikonal systematic the dominant formal
uncertainty. No numbers changed; verify script unchanged, 9/9 PASS
(FAST 4/4). Compile gate: pdflatex ×2, 0 errors, 0 undefined refs,
7 pages. Deposit posture: queue row stays fail-closed (founder
APPROVED column + Isak's DOIs remain the gate).

## V1.1 — 21 August 2026, Patch 3338 (Session 156) — RCORE-3 amendment set

Review basis: CONV-034, 5/5 same-session, AMENDMENTS-CLEAR 4–1
(`review/conv034_adjudication.md` v1.0); founder-ratified ("Ratify
the bundle", `founders_voice/founder_ruling_conv034_rcore3_
ratification_2026-08-21.md`). ADDITIVE under the existing CONV-033
eikonal scoping — no shipped claim is falsified as scoped, and no
number in the template table changes; the verify script is untouched
and still passes 9/9 (FAST 4/4).

New Remark (§3, `rem:rcore3`) records what the finite-ℓ discharge
found: (i) the comb does not survive — a single top-of-barrier
resonance at ℓ=2, χ=0, and N_trapped = 0 for every exposed mode at
χ=0.68 and across χ ∈ [0.30, 0.98] (the integer census at
eikonal-WKB grade); (ii) a mode-resolved LINE SET replaces it, with
Eq. (1)'s delay retained as the early-transient timescale, and line
positions/widths explicitly NOT quantitatively predicted — eikonal
tops 211/233/260/294 Hz are orientation-scale, and the single
computed anchor's +17%/Q≈5 gives direction and rough scale, NOT an
error model (CONV-034 adopted revision); (iii) burial sharpens to
the entire corotating (ℓ,ℓ) branch, so the discriminator survives as
line ORDERING, while the onset is repriced to χ ≈ 0.665 UNDER THE μ
CORRESPONDENCE with the finite-ℓ onset unquantified and the 0.026
margin possibly inside the correspondence error, and the wave-side
check is corroborative AT THE SAME GRADE; (iv) co-rotation UNTESTED
for line structure. Also: §3's onset labelled "equatorial eikonal";
Honest Limits (2) rewritten and (5) updated to the paper's real
review basis (CONV-033 + CONV-034, both ratified); conclusion points
at the remark. Preamble gains a `remark` theorem environment.
Compile gate: pdflatex ×2, 0 errors, 0 undefined refs, 8 pages.
Deposit posture unchanged: queue row fail-closed behind the founder
APPROVED column + Isak's DOIs; publication held until the GR series
completes.

## V1.2 — 21 August 2026, Patch 3340 (Session 156) — Leg-C narrowing + two additions

Basis: OPEN-GR-RCORE-3 Leg C (Patch 3339, verify 6/6, all-FAST).
**CONV-035 is OWED** — the panel ratified (CONV-034) the
generalization this version narrows; the narrowing is enacted on
discovery because a known-over-broad claim in a shipped paper is a
defect, and the direction is strictly weaker.

NARROWING (anti-erasure — the superseded V1.1 wording is quoted in
the .tex header changelog): the V1.1 remark asserted N_trapped = 0
"for every exposed mode ... across χ ∈ [0.30, 0.98]" — a census
computed over ℓ ≤ 3 and stated with no ℓ qualifier. The
Bohr–Sommerfeld phase grows LINEARLY in ℓ without saturation
(Φ/π ≈ 0.122 ℓ at χ = 0.68) and crosses the trapping threshold at
ℓ_crit = 7 for χ ≥ 0.30 (ℓ ≈ 10 at χ = 0): trapped ladders DO exist
at high multipole. §3's remark now states the swept range as part of
the claim; records that the negligibility of ℓ ≳ 7 ringdown
excitation is INHERITED from standard phenomenology and computed
nowhere in this programme (OPEN-GR-RCORE-3(e), now load-bearing);
and notes the consistency win — the geometric-optics comb is the
ℓ → ∞ limit, recovered from below, so the ℓ = 2 single resonance and
the eikonal comb are two ends of one ladder. Low-ℓ robustness
quantified: the threshold is δ_w/2 + π/4 in the wall reflection
phase, so N = 0 at ℓ = 2,3 needs δ_w > 0.235π (42.3°); the derived
clamped-register δ_w = π clears it 4.3×.

ADDITIONS: (iv) co-rotation is COUNT-NEUTRAL at Dirichlet grade —
R(r;ω) depends only on (a,m,Q,ω), so a wall rotating at Ω_w leaves
turning point and phase volume unchanged (RCORE-3 item (b)
discharged for the count; line positions remain Teukolsky work);
(v) across 112 modes through ℓ = 12 no mode is simultaneously
exposed, trapped, and superradiant — burial and trapping occupy
disjoint regions of the (ℓ,m) grid, so censorship protects the
finite-ℓ sector by a mechanism the eikonal analysis could not see.

Compile gate: pdflatex ×2, 0 errors, 0 undefined refs, 9 pages. No
number in the template table changes; the GR-2 verify script is
untouched at 9/9. Deposit posture unchanged (fail-closed).

## V1.3 — 21 August 2026, Patch 3345 (Session 156) — CONV-035 adopted revisions

Review basis: **CONV-035 CLOSED 5/5** (`review/conv035_adjudication.md`
v2.0). Q9b CLEAR 4–1; Q6 — the process call on enacting corrections
before their audit round — **CORRECT 3–2, resolved by the dissent
seat itself**, so enact-on-discovery stands with no standing
constraint; the Gemini/Copilot minority reasoning is recorded.

Five adopted revisions, all folded here:
1. **ℓ_crit quoted 7 ± 1** (10 ± 1 at χ = 0) everywhere, never the
   bare integer — at χ = 0.68, ℓ = 6 already sits at Φ/π = 0.734,
   only 0.016π below the Dirichlet threshold. Four seats carried this
   caveat.
2. **The high-ℓ excitation clause** carries its inherited/uncomputed
   qualifier inline and is explicitly barred from being read as an
   established result of this paper (OPEN-GR-RCORE-3(e),
   undischarged, load-bearing).
3. **The eikonal-recovery claim regraded**: monotone, near-linear
   growth over ℓ = 2–10 is the COMPUTED content; unbounded growth in
   ℓ is an ASYMPTOTIC INFERENCE from that trend plus the eikonal
   construction, not a numerical finding.
4. **The stability result regraded** to
   ESTABLISHED-OVER-A-DECLARED-EXHAUSTIVE-DOMAIN (all 165 modes,
   ℓ = 2–12) and explicitly **not** a structural exclusion — which
   would require the analytic disjointness inequality
   (trapped ⇒ m ≤ −(ℓ−1); superradiance-capable ⇒ buried), registered
   as open work.
5. **The underlying sweep was made exhaustive AT THE COMPUTATION**
   (Patch 3344), not repaired in prose. V1.2 inherited a check that
   described a selected-ℓ sweep as "the whole (ℓ,m) grid" — the same
   quantifier defect this paper's remark exists to record, committed
   inside the corrective patch. The check now asserts its own mode
   count against the declared domain, so the claim cannot drift from
   its domain again without failing.

No number in the template table changes; the GR-2 verify script is
untouched at 9/9. Compile gate: pdflatex ×2, 0 errors, 0 undefined
refs, 9 pages. Deposit posture unchanged (fail-closed). **OWED before
the next flagship prediction move: the corpus-wide quantifier audit
across the eleven GR papers.**

## V1.4 — 30 August 2026, Patch 3348 (Session 157) — the verification claim corrected, and made self-testing

Basis: the corpus-wide quantifier audit (Patch 3347), which found §2's
"every number is reproduced by the paper's verify script
(`3329_gr2_template_verify.py`, 9/9 PASS)" to be **false** — and false
in a way that worsened with every version bump. The ~5% first-echo
amplitude was inherited from GR-1d V3 and never lived in 3329 (false
since V1.0); V1.1–V1.3 then added ℓ_crit = 7 ± 1, the Φ/π ≈ 0.122 ℓ
slope, the 165-mode domain, the 236 Hz χ = 0 resonance, the four
eikonal tops and the δ_w > 0.235π envelope, every one computed by
3333, 3334 or 3339. **No DOI should carry that sentence.**

THE FIX, structural rather than editorial. The blanket claim is
replaced by an explicit **provenance table** naming four scripts with
their counts (3329 → 9/9; 3333 → 9/9; 3334 → 7/7; 3339 → 6/6) and what
each reproduces, plus a declared exception: **the ~5% amplitude is not
script-verified in this paper at all** — |R| = 1 is exact and derived,
but the barrier-transmission fraction is an argument-level estimate
inherited from GR-1d V3.

Per the standing practice minted at 3347 ("any sentence asserting what
a script covers is re-read at every version bump, **and asserted in
code where practical**"), the table is itself checked by
`code/3348_gr2_verification_provenance.py` (**6/6 PASS**, all FAST,
fail-closed and directory-independent): every cited script exists at
its cited path; every quoted count equals that script's actual
`check()` total (the rot-detector — change a script and the paper's
claim FAILS a test rather than quietly becoming false); the inherited
quantity is still declared; and the defective phrasing cannot return.
The regression arm was **adversarially tested**: reinstating the V1.3
sentence drops the checker to 5/6 with "REGRESSION: the V1.3 sentence
is back", and removing it restores 6/6.

No physics changed. No number in the template table moved. The four
underlying verify scripts are untouched. Compile gate: pdflatex ×2,
0 errors, 0 undefined refs, 9 pages. Deposit posture unchanged
(fail-closed behind the founder APPROVED column + Isak's DOIs).

## V1.5 — 30 August 2026, Patch 3351 (Session 157) — RCORE-3(e) closed; the paper's claim about it corrected

V1.4's remark called the negligibility of high-ℓ excitation
"inherited from standard ringdown phenomenology, not computed in this
programme… undischarged, load-bearing." **True when written, and made
false by Patches 3349–3350.** V1.5 replaces it with three *computed*
arguments, ordered by margin:

1. **Band separation** (widest margin) — the trapped ladder lies at
   602–986 Hz, the predicted line set at 211–294 Hz, a factor 2.0
   clear. Holds at every ℓ, independent of excitation, so a search in
   the predicted band cannot be contaminated at all.
2. **Barrier penetration** — e^(−4Γ) = 7e−4 at ℓ = 9, falling ~3e−2
   per multipole; explicitly **not** decisive at ℓ = 7 (0.20), because
   ℓ_crit is where trapping just begins and the barrier is thinnest.
3. **Source-side budget** for ℓ = 7–8 — 1.9e−4 and 3.6e−6 at the worst
   case of a velocity scan bounded by v_ISCO = 0.536, with the
   counter-rotation mismatch bounded conservatively at unity.

**The thin margin on (3) is stated in the paper text**: the ℓ = 7
budget crosses 10⁻³ at v = 0.589, only 0.053 above v_ISCO — closed
within the derived physical range, marginal just outside it. Argument
(1) carries no such sensitivity.

Provenance table extended to **six** scripts (3349 → 8/8, 3350 → 9/9).

**The provenance checker gained a SCOPE-CREEP DETECTOR (now 7/7).**
V1.4's version validated ledger → paper but never paper → ledger, so
numbers arriving from an unlisted script could enter silently — *the
very mechanism that grew the V1.0–V1.3 defect*. It failed correctly
while this edit was in progress, which is how the edit got made. Two
further self-corrections during the patch, both recorded in the code:
the detector first passed **vacuously** (it matched raw LaTeX, found
one citation, and reported "all in the ledger"), so it now runs on
normalized text and **fails closed on its own reach**; and its
exclusions (this script itself, `build_osf_queue.py`) are **named with
reasons** rather than silently exempted. Adversarially tested: a bogus
unledgered citation is caught.

No physics changed. Compile gate: pdflatex ×2, 0 errors, 0 undefined
refs, 10 pages. Deposit posture unchanged (fail-closed).

## V1.6 — 31 August 2026, Patch 3363 (Session 157) — the flagship line at gravitational grade

Basis: **CONV-037 CLOSED 5/5** (`review/conv037_adjudication.md`;
AMENDMENTS-CLEAR 3–2; every seat's revisions adopted; two panel-named
gaps computed before ruling), **founder-ratified 31 Aug** ("please
ratify the bundle").

The Teukolsky ladder (Patches 3353–3361) replaces V1.5's "line
positions and widths not yet quantitatively predicted" and its
one-point "+17%, Q ≈ 5" anchor with exact s = −2 Kerr wall
resonances: **(2,−2) at 188–194 Hz across χ ∈ [0.62, 0.74] (191.2 Hz at
0.68), Q ≈ 2.1; (3,−3) at 284–292 Hz, Q ≈ 4.2.** Below every prior
estimate — the s = −2 potential sits lower than the scalar/eikonal one;
the "+17% above the top" was wrong-signed for gravitational waves.

**The assumption is stated in the paper:** X = 0 is the Regge–Wheeler
analogue of the clamped-register node, *assumed* rather than derived
for a rotating surface; the spectrum is conditional on it. (2,+1) NOT
LOCATED; the ordering discriminator stands at eikonal-WKB grade only;
"dominant" conditioned on the inherited excitation model; superseded
tops and the V1.5 anchor retained per anti-erasure.

Provenance ledger extended to **ten** scripts (3356 8/8, 3358 9/9,
3359 9/9, 3361 3/3); the 3348 checker's ledger extended with it and
passes 7/7 with its scope-creep detector satisfied. No template-table
number changed. Compile gate: pdflatex ×2, 0 errors, 0 undefined,
11 pages. Deposit posture unchanged (fail-closed).

## V1.7 — 2 September 2026, Patch 3371 (Session 161) — two caveats on the flagship line (CONV-038, 5/5)

**Trigger.** The founder asked what a "clamped register" is. The term (Opus coinage, 3297) traced to the CP Exclusion Rule, which the founder ruled RETIRED (R-EXCL-RETIRED; never in its cited source c01). The floor l_P/2 under the whole R-core arc lost its only derivation; re-derived at 3367 as a Buchdahl bound; CONV-038 (5/5, EK-1 two seats execution-verified) ruled attainment unproved, phase π not derived, caveat obliged 5–0. Founder R-FLOOR-FINITE / R-CELL-SIZE-OPEN (2 Sep). Sensitivity 3370: the admissible window 0.536 < u_max ≤ 1 runs the cavity 2.15 ms → 0.14 ms.

**Edits (text only; no number changed; no template moved).** In the V1.6 gravitational-grade paragraph, after the standing "X = 0 assumed" sentence, a V1.7 block: (a) boundary phase — the replacement boundary is a one-Moment-delay compliant surface of which X = 0 is the zero-compliance limit; |R| = 1 survives with caveats, phase π does not; the boundary-phase shift is uncomputed and the 188–194 Hz band excludes it; (b) floor value — every number computed at u = 1, a conditional bound, not a derived floor; window 0.536 < u_max ≤ 1; the line set is not robust to the floor value. `\date` → Version 1.7 (2 September 2026). Header changelog entry. Compile gate: pdflatex ×2, 0 errors, 0 undefined, 11 pp.

**Standing banner inherited from GR-1c Corrigendum 3:** *floor undetermined within a derived window; Buchdahl conditional bound PSR ≥ l_P/2.* "Clamped register" remains in the text as a named misnomer pending the wall-impedance computation (OPEN-GR-ROT-1).
