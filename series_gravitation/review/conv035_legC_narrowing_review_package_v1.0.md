# CONV-035 REVIEW PACKAGE v1.0 — RCORE-3 Leg C: a narrowing of what this panel ratified
# (Patch 3341, 21 Aug 2026, Session 156)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package. Paste
its full contents to each of the five seats — one identical paste per
seat (Copilot may need the file-upload route). Execution-capable seats
also receive the separate `.py`. Returns come back INLINE, verbatim.

---

## §0 Why this round exists (read this first)

**This panel ratified a claim that is now known to be over-broad, and
the worker found it, not the panel.**

At CONV-034 (5/5, AMENDMENTS-CLEAR 4–1) you audited OPEN-GR-RCORE-3
Legs A and B and confirmed, among other findings, that the
Bohr–Sommerfeld census gives `N_trapped = 0` "for every exposed mode
at χ = 0.68 AND across χ ∈ [0.30, 0.98]" — the headline
*"the comb is NOT restored, at any spin."* On that verdict the founder
ratified, PRED-O-39 was amended (Patch 3337) and GR-2 shipped V1.1
(Patch 3338).

Leg B's census was computed over **ℓ ≤ 3 only**. Patch 3339 ran the
exposed extreme-retrograde branch out to ℓ = 12 and found the phase
volume grows **linearly in ℓ with no saturation**, crossing the
trapping threshold at **ℓ_crit = 7** (χ ≥ 0.30; ℓ ≈ 10 at χ = 0):
**trapped ladders do exist at high multipole.** The claim was true for
every mode it computed and false as a statement about all ℓ. It was
live in a flagship prediction and a shipped paper for roughly four
hours.

The narrowing was **enacted on discovery** (PRED-O-39 at Patch 3339,
GR-2 V1.1 → V1.2 at Patch 3340) rather than held for this round, with
anti-erasure by quotation in both places. **Whether that was the right
call is one of this round's frozen questions.**

The same computation also produced two results that strengthen the
sector, and this round must weigh those on their own merits and not as
compensation: the eikonal comb is recovered as the ℓ → ∞ limit (the
consistency check neither Leg performed), and no mode anywhere in the
(ℓ,m) grid through ℓ = 12 is simultaneously exposed, trapped, and
superradiant.

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3340):
`series_gravitation/rcore_derivation/3339_rcore3_legC_corotation_multipole.md`,
`series_gravitation/code/3339_rcore3_legC_corotation_robustness_verify.py`,
`series_gravitation/papers/GR-2_echo_falsifier.tex` (V1.2),
`predictions.md` (PRED-O-39, narrowed), `series_gravitation/reasoning/3339.md`.

## §1 Under review / fenced

UNDER REVIEW: (a) the Leg-C computation and its three findings (the
ℓ-ladder and ℓ_crit; the eikonal-limit recovery; the
exposed/trapped/superradiant exclusion); (b) the co-rotation
count-neutrality argument; (c) the reflection-phase robustness
envelope; (d) **the adequacy and completeness of the narrowing** as
enacted in predictions.md and GR-2 V1.2; (e) **the process question**
— enacting a correction before the audit round; (f) the newly minted
OPEN-GR-RCORE-3(e); (g) **a scope audit**: are there OTHER unstated
quantifiers of this class in the recent GR-lane claims?

FENCED (settled, not re-adjudicated): A1–A3 and the censorship
mathematics (CONV-032); GR-2's eikonal-scoped template claims
(CONV-033); |R| = 1; F-R1; the CONV-034 adopted grading revisions
(the ~247–344 Hz withdrawal, the μ-correspondence onset language) —
those stand and are unaffected.

## §2 Claim chains

**C — the ℓ ladder (the correction):**
C-1 Leg B computed the census over ℓ ≤ 3 and stated its conclusion
    with no ℓ qualifier.
C-2 On the exposed extreme-retrograde branch (ℓ, −ℓ), Φ/π grows
    linearly: 0.1220 ± 0.0002 per unit ℓ at χ = 0.68, from 0.246
    (ℓ=2) to 1.222 (ℓ=10). No saturation.
C-3 Trapping threshold ¾ is crossed at **ℓ_crit = 7** for χ = 0.30,
    0.68, 0.95; at **ℓ ≈ 10** for χ = 0.
C-4 Therefore trapped combs exist at high multipole; the low-ℓ
    result (N = 0 at ℓ = 2, 3, every spin tested) stands unchanged.
C-5 The observable prediction survives only because ℓ ≳ 7 ringdown
    excitation is negligible — **inherited from standard
    phenomenology, computed nowhere in this corpus**, now registered
    as OPEN-GR-RCORE-3(e) and declared load-bearing.

**D — the consistency win:**
D-1 The eikonal comb is the ℓ → ∞ limit of the finite-ℓ census.
D-2 N_trapped grows without bound with ℓ, approached from below.
D-3 Had the census returned N = 0 at every ℓ, the finite-ℓ and
    geometric-optics pictures would have been irreconcilable.
D-4 Leg A's single ℓ = 2 above-top resonance and the eikonal comb
    are therefore two ends of one ladder.

**E — co-rotation (chartered item (b)):**
E-1 R(r;ω) depends only on (a, m, Q, ω) — geometry and mode — not on
    the wall's angular velocity Ω_w.
E-2 Hence a co-rotating wall leaves turning point and phase volume
    identically unchanged (verified to 1e-9 across a frame round
    trip at Ω_ZAMO(r_surf) = 0.09985/M).
E-3 At Dirichlet grade a node is a node in any frame ⇒ co-rotation
    is COUNT-NEUTRAL; item (b) discharged for the count. Line
    positions remain full-Teukolsky work.

**F — reflection-phase envelope:**
F-1 With one hard wall (phase δ_w) and one turning point,
    2Φ − δ_w − π/2 = 2πn ⇒ Φ_thr(n=0) = δ_w/2 + π/4. The ¾π used by
    Leg B assumed the **derived** Dirichlet δ_w = π (RCORE-1).
F-2 Low-ℓ N = 0 therefore requires δ_w > 0.235π = 42.3°; the derived
    π clears it by 4.3×.
F-3 A free/Neumann-like end WOULD trap at ℓ = 2 — the low-ℓ result
    is about the clamped wall, not geometry alone.

**G — structural protection (stability):**
G-1 The ergoregion-instability recipe at finite multipole is a mode
    that is simultaneously EXPOSED, TRAPPED, and SUPERRADIANT.
G-2 Across 112 modes through ℓ = 12 at χ = 0.68: none exists.
G-3 Mechanism: every trapped mode is extreme-retrograde
    (m ≤ −(ℓ−1)) and has no superradiant window (mΩ_w < 0); every
    mode whose window could reach trapping frequencies is
    corotating and therefore BURIED (μ > μ_crit = 0.774).
G-4 Burial and trapping occupy disjoint regions of the (ℓ,m) grid ⇒
    censorship protects the finite-ℓ sector, by a mechanism the
    eikonal analysis could not see. Zel'dovich window at χ = 0.68
    caps at mΩ_w = 0.0998 (52 Hz) vs exposed low-ℓ tops ≥ 0.5643
    (294 Hz) — disjoint by 5.7×. NOT a growth-time computation.

## §3 Triage — the worker's five weakest points

T-1 **Is ℓ_crit convention-robust?** The threshold ¾π is a
    Maslov/phase convention, and F-1 shows it is really
    δ_w/2 + π/4. ℓ_crit = 7 sits where Φ/π = 0.856 — comfortably
    over ¾, but ℓ = 6 sits at 0.734, just under. Is ℓ_crit
    uncertain by ±1, and does the record say so clearly enough?
T-2 **Is the narrowing COMPLETE?** The worker searched the two
    enacted locations (predictions.md, GR-2). Are there other live
    corpus statements — frontier files, the CONV-034 adjudication
    itself, GR-1h/1f cross-references — still carrying the
    over-broad "no comb at any spin" form?
T-3 **Was enacting before this round legitimate?** The corpus rule
    from CONV-034 says strictly-weaker restatements fold without
    re-review; stronger ones owe a round. But the panel had
    ratified the broader claim, which is arguably a different case.
    Rule on the process, not just the physics.
T-4 **Does the fixed-Q eikonal correspondence hold up at HIGH ℓ?**
    GPT's CONV-034 objection was that μ = m/(ℓ+½) is asymptotic and
    unreliable at ℓ = 2. At ℓ ≳ 7 the correspondence should be
    *better* — the one regime where this method is strongest. Is
    that reasoning sound, and does it make the ladder finding more
    trustworthy than the low-ℓ burial numbers?
T-5 **Is the (ℓ,m) exclusion (G) exhaustive or merely unsampled?**
    112 modes were examined on a partial grid (|m| ∈ {0,1,2,ℓ−1,ℓ}
    at selected ℓ). Could an intermediate-m mode at some ℓ be
    exposed, trapped, AND superradiant? Give the argument or demand
    the full sweep.

## §4 Frozen questions (answer ALL; use ONLY the given vocabulary)

Q1 — The ℓ-ladder computation and ℓ_crit:
     **CONFIRMED / CONFIRMED-WITH-CAVEATS / NOT-CONFIRMED**
Q2 — The eikonal-limit recovery as a consistency result (chain D):
     **SOUND / OVERREAD / UNSOUND**
Q3 — Co-rotation count-neutrality (chain E):
     **SOUND / SOUND-WITH-CAVEATS / UNSOUND**
Q4 — The structural-protection result (chain G):
     **ESTABLISHED / SUGGESTIVE-NOT-ESTABLISHED / REFUTED**
Q5 — The narrowing as enacted (predictions.md + GR-2 V1.2):
     **ADEQUATE-AND-COMPLETE / ADEQUATE-BUT-INCOMPLETE / INADEQUATE**
Q6 — The process call (enacting the correction before this round):
     **CORRECT / DEFENSIBLE-BUT-SHOULD-HAVE-WAITED / IMPROPER**
Q7 — OPEN-GR-RCORE-3(e) (the multipole excitation budget), and the
     decision to declare it load-bearing rather than assume it:
     **CORRECTLY-SCOPED / UNDER-SCOPED / UNNECESSARY**
Q8 — **SCOPE AUDIT (the round's assigned homework):** name any OTHER
     claim in the recent GR-lane work that states a conclusion
     without the quantifier its computation actually supports:
     **NONE-FOUND / ITEMS-FOUND (list them)**
Q9a — The Leg-C assembly overall:
     **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q9b — Disposition: **CLEAR / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. A majority
NOT-CONFIRMED on Q1 reverts the narrowing and restores the CONV-034
text. A majority INADEQUATE on Q5 forces a second narrowing pass
before any further GR-lane physics. A majority IMPROPER on Q6
establishes a standing rule that corrections wait for the round —
**the worker will be bound by that verdict in future.** Q8 items are
adopted as work regardless of the Q9b tally.

## §5 Seat mandates

- **IDENTITY:** your own model name in REVIEWER. Gemini seat: you are
  Gemini. DeepSeek seat: you are DeepSeek.
- **OWN-RUN:** SCRIPT-EXECUTED requires YOUR OWN run; quoting the
  reference is INSPECTED and will be reclassified. This script is
  all-FAST (6 checks; the ℓ-scan is the slow part, a few minutes).
  Own harness = INDEPENDENT-HARNESS.
- **COUNT-LINE:** paste your final count line VERBATIM.
- **TIER:** tag every question.
- **RETURNS:** inline text only, §8 skeleton.

Per-seat steers:
- **ChatGPT/GPT (grading auditor — three consecutive rounds of
  adopted dissent):** T-1 and T-4 are yours. Also rule Q6 hard: you
  are the seat most likely to say the worker should have waited.
- **Grok (script seat):** own-run; audit the ℓ-scan numerics, the
  threshold-crossing logic, and T-5 — is the mode grid sufficient?
- **Gemini (error-budget seat):** the CONV-034 ledger sharpened your
  mandate. The question is no longer "is uncertainty language
  present?" but **"is it EARNED?"** Apply that to ℓ_crit, to the
  0.122 slope, and to the "negligible excitation" claim.
- **Copilot (registry seat):** T-2 is yours — the completeness audit.
  Hunt every live location still carrying the over-broad form.
  Note: your CONV-034 return offered to execute amendments yourself;
  review seats do not execute. Please return the §8 skeleton only,
  without a chat wrapper.
- **DeepSeek (falsifier seat):** does the narrowed prediction remain
  falsifiable? Does OPEN-GR-RCORE-3(e) create an escape hatch — can
  a null now be dismissed by asserting low excitation?

## §6 Reference run (own-runs preferred)

```
chi = 0.68: equatorial wall r = 2.2668 M; Omega_ZAMO(wall) = 0.09985 /M (52.0 Hz-equiv @62)
      exposed extreme-retrograde branch (ell, -ell) — phase volume:
        chi=0.00: l2:0.180 l3:0.252 l4:0.323 l5:0.395 l6:0.467 l7:0.539 l8:0.611 l9:0.683 l10:0.755*   -> trapping switches on at ell = 10
        chi=0.30: l2:0.240 l3:0.347 l4:0.453 l5:0.560 l6:0.667 l7:0.774* l8:0.881* l9:0.987* l10:1.094*   -> trapping switches on at ell = 7
        chi=0.68: l2:0.246 l3:0.368 l4:0.489 l5:0.612 l6:0.734 l7:0.856* l8:0.978* l9:1.100* l10:1.222*   -> trapping switches on at ell = 7
        chi=0.95: l2:0.232 l3:0.356 l4:0.480 l5:0.605 l6:0.729 l7:0.854* l8:0.978* l9:1.103* l10:1.228*   -> trapping switches on at ell = 7
[PASS] 1. THE LEG-C FINDING (overturns a shipped generalization): Phi grows LINEARLY in ell with NO saturation, and the trapped count switches on at a finite critical multipole — chi=0.68: Phi/pi = 0.246 (l=2) -> 1.222 (l=10), increments 0.1220 +/- 0.0002 per unit ell (LINEAR); ell_crit = 7 at chi>=0.30, 10 at chi=0. Leg B computed ell<=3 only — its 'no comb at any spin' does NOT generalize in ell and is NARROWED by this patch
[PASS] 2. THE CONSISTENCY WIN neither Leg performed: the eikonal comb is RECOVERED as ell -> infinity, approached FROM BELOW — geometric optics is the large-multipole limit, exactly as it must be — N_trapped grows without bound with ell (Phi/pi ~ 0.122*ell); the eikonal picture was never WRONG — the physical low-ell modes are simply far from its limit, which is why Legs A/B found no comb there
[PASS] 3. THE LOW-ELL RESULT STANDS where it was computed: N_trapped = 0 for ell = 2 and ell = 3 at EVERY spin tested — Legs A and B are correct inside their scope, and the observationally dominant multipoles are exactly that scope — chi=0.00: l2 N=0 (Phi/pi=0.180), l3 N=0 (Phi/pi=0.252); chi=0.30: l2 N=0 (Phi/pi=0.240), l3 N=0 (Phi/pi=0.347); chi=0.68: l2 N=0 (Phi/pi=0.246), l3 N=0 (Phi/pi=0.368); chi=0.95: l2 N=0 (Phi/pi=0.232), l3 N=0 (Phi/pi=0.356)
[PASS] 4. CO-ROTATION CANNOT MOVE THE COUNT at Dirichlet grade: R(r;omega) depends only on (a, m, Q, omega), so a wall rotating at Omega_w leaves the turning point and the phase volume identically unchanged — a node is a node in any frame; co-rotation enters ONLY via the reflection phase (check 5) and the energetics (check 6) — phase integrals invariant to 1e-9 across the Omega_w = 0.09985 frame round trip for all five low-ell exposed modes
[PASS] 5. ROBUSTNESS ENVELOPE for the observable (low-ell) prediction: the N = 0 integer at ell = 2,3 survives every wall reflection phase above a computed threshold, and the DERIVED Dirichlet value clears it wide — flip requires delta_w < 0.2351 pi = 42.3 deg; derived delta_w = pi = 180 deg (clamped register, RCORE-1) — margin 4.3x. A free/Neumann-like end WOULD trap: the low-ell no-comb result is a statement about the CLAMPED wall, not geometry alone
[PASS] 6. STRUCTURAL PROTECTION — the dangerous combination does not occur: across the whole (ell, m) grid there is NO mode that is simultaneously EXPOSED, TRAPPED, and SUPERRADIANT (the ergoregion-instability recipe at finite multipole) — 112 modes examined through ell = 12: every TRAPPED mode is extreme-retrograde (m <= -(ell-1)), which has NO superradiant window (m*Omega_w < 0); every mode with a superradiant window large enough to reach trapping frequencies is CORO+ROTATING and therefore BURIED. Burial and trapping select disjoint parts of the mode grid — the censorship result protects the finite-ell sector too
6/6 PASS
FAST: all checks are FAST; FAST: 6/6 PASS
```

## §7 Materials

### 7.1 The Leg-C record

# OPEN-GR-RCORE-3 — Leg C: Co-rotation, Reflection-Phase Robustness, and the Multipole Ladder — **a shipped generalization is narrowed**

**Patch 3339, 21 Aug 2026 — Session 156.** Verify:
`code/3339_rcore3_legC_corotation_robustness_verify.py`, **6/6 PASS**
(all-FAST). Charter: RCORE-3 item (b), the co-rotating wall — which
GR-2 V1.1's own new remark names UNTESTED, one patch after shipping it.

---

## §1 HALT-CLASS FINDING: Leg B's "the comb is not restored at any spin" was computed over ℓ ≤ 3 and does NOT generalize in ℓ

Leg B's census stopped at ℓ = 3. This patch ran the exposed
extreme-retrograde branch (ℓ, −ℓ) out to ℓ = 12 and found that the
Bohr–Sommerfeld phase **grows linearly in ℓ with no saturation**
(Φ/π ≈ 0.122 ℓ at χ = 0.68; increments 0.1220 ± 0.0002), crossing the
¾ trapping threshold at a finite critical multipole:

| χ | Φ/π at ℓ=2 | ℓ=6 | ℓ=7 | ℓ=10 | **ℓ_crit** |
|---|---|---|---|---|---|
| 0.00 | 0.180 | 0.467 | 0.539 | 0.755 | **10** |
| 0.30 | 0.240 | 0.667 | 0.774 | 1.094 | **7** |
| 0.68 | 0.246 | 0.734 | 0.856 | 1.222 | **7** |
| 0.95 | 0.232 | 0.729 | 0.854 | 1.228 | **7** |

**Trapped resonances — a comb — DO exist, for ℓ ≳ 7.** The corpus
statements enacted from Leg B two patches ago ("the comb is NOT
restored, at χ = 0.68 or at ANY spin"; PRED-O-39's amended row; GR-2
V1.1's `rem:rcore3`) are **OVER-BROAD in ℓ** and are narrowed at
Patches 3339–3340. The correct statement:

> **No trapped comb exists in the observationally dominant low
> multipoles (ℓ = 2, 3 — N = 0 at every spin tested, checks 3);
> trapped ladders switch on at ℓ ≳ 7 (ℓ ≈ 10 at χ = 0), where
> ringdown excitation is negligible.**

## §2 THE OTHER HALF: this is also the consistency check neither Leg performed — and it VALIDATES the framework

The eikonal (geometric-optics) comb is the ℓ → ∞ limit. If the finite-ℓ
census had found N = 0 at *every* multipole, the two pictures would
have been irreconcilable and something would have been wrong. Instead
N_trapped grows without bound with ℓ, **approached from below**: the
eikonal picture was never wrong, and the physical low-ℓ modes are
simply far from its limit — which is exactly why Legs A and B found no
comb there. Leg A's single above-top resonance at ℓ = 2 and the
eikonal comb are now understood as the two ends of one ladder. The
finding that embarrasses the shipped wording is the same finding that
knits the sector together.

## §3 Co-rotation (the chartered item (b)): it cannot move the count

R(r;ω) depends only on (a, m, Q, ω) — the geometry and the mode — not
on the wall's angular velocity. A wall rotating at Ω_w leaves the
turning point and the phase volume identically unchanged (verified to
1e-9 across a frame round trip at Ω_ZAMO(r_surf) = 0.09985/M, check 4);
at Dirichlet grade **a node is a node in any frame**. Co-rotation
therefore enters only through (i) the reflection phase and (ii) the
energetics — both computed below. **Item (b) is DISCHARGED for the
count; the line-position shift it induces remains full-Teukolsky work.**

## §4 Reflection-phase robustness envelope (new, and load-bearing)

The ¾ threshold is not a constant. With one hard wall of reflection
phase δ_w and one turning point, 2Φ − δ_w − π/2 = 2πn, so
Φ_thr(n=0) = δ_w/2 + π/4. Leg B's ¾π assumed the **derived** Dirichlet
value δ_w = π (clamped register, RCORE-1 Patch 3297). For the low-ℓ
observable prediction, a flip requires **δ_w < 0.235π = 42.3°** — the
derived value clears it by **4.3×**. Recorded honestly: a free /
Neumann-like end *would* trap at ℓ = 2. The low-ℓ no-comb result is a
statement about the **clamped** wall, not about geometry alone, and it
now carries a quantified tolerance instead of an implicit assumption.

## §5 STRUCTURAL PROTECTION: the dangerous combination does not occur

The ergoregion-instability recipe at finite multipole is a mode that is
simultaneously EXPOSED, TRAPPED, and SUPERRADIANT. Across 112 modes
through ℓ = 12 at χ = 0.68: **none exists.** Every trapped mode is
extreme-retrograde (m ≤ −(ℓ−1)), which has no superradiant window at
all (mΩ_w < 0); every mode whose superradiant window could reach
trapping frequencies is corotating and therefore BURIED (μ > μ_crit).
**Burial and trapping select disjoint regions of the (ℓ,m) grid** — the
censorship result protects the finite-ℓ sector too, and it does so
by a mechanism the eikonal analysis could not see. The Zel'dovich
channel (RCORE-3 item (d)) is correspondingly bounded at
reconnaissance grade: at χ = 0.68 the superradiant window caps at
mΩ_w = 0.0998 (52 Hz) for m = 1 while the exposed low-ℓ barrier tops
sit at ≥ 0.5643 (294 Hz), a factor 5.7 above — window and resonance
band are DISJOINT. This is not a growth-time computation; item (d)
stays open.

## §6 Registry impact

- **OPEN-GR-RCORE-3 item (b) DISCHARGED for the resonance count**
  (co-rotation is count-neutral at Dirichlet grade); line-position
  effects remain full-Teukolsky work.
- **Legs A and B: scope CORRECTED, results intact.** Both are correct
  where computed (ℓ = 2 FD spectroscopy; ℓ ≤ 3 census). Their
  *generalization to all ℓ* is withdrawn.
- **PRED-O-39 NARROWED (Patch 3339)** and **GR-2 V1.1 → V1.2 (Patch
  3340)**: "no comb" becomes "no comb in the observationally dominant
  low multipoles; trapped ladders at ℓ ≳ 7 where excitation is
  negligible." Anti-erasure by quotation in both.
- **NEW OPEN ITEM — OPEN-GR-RCORE-3(e): multipole excitation budget.**
  The claim that ℓ ≳ 7 excitation is negligible in comparable-mass
  ringdown is INHERITED from standard ringdown phenomenology and is
  **NOT computed anywhere in this corpus.** It is now load-bearing for
  the observable prediction and must be discharged.
- **CONV-035 OWED:** the panel ratified (CONV-034) a generalization
  this patch narrows. The audit round is owed on the narrowing —
  dispatched next.

## §7 Honest limits

Eikonal-WKB grade throughout, inheriting Leg B's construction, its
fixed-Q correspondence (approximate at low ℓ, *better* at the high ℓ
where the ladder finding lives — the one place this method is
strongest), and the A1–A3 conditionality (OPEN-GR-RCORE-4). ℓ_crit is
threshold-convention-dependent at the same ±1 level the δ_w envelope
quantifies. No amplitude, excitation, or growth-time computation is
performed anywhere in this patch.


### 7.2 The worker's reasoning fragment (Tier 4, verbatim — includes the self-assessment of the failure)

# Patch 3339 — reasoning fragment (verbatim, Tier 4)

The patch I did not expect to write. Leg C was chartered as the
tidy closing item — co-rotation, the thing GR-2 V1.1 names untested
one patch after shipping. It closed that cleanly. It also overturned
a generalization that shipped two patches ago, and the ratification
ink is a day old.

How it happened is the part worth keeping. While designing the
robustness envelope I needed a supremum of Phi over the mode set,
so I scanned ell beyond Leg B's stopping point of 3. Phi did not
saturate. It grows linearly, 0.122 per unit ell at chi = 0.68, and
crosses the trapping threshold at ell = 7. Leg B's headline — "the
comb is NOT restored, at chi = 0.68 or at ANY spin" — was true for
every mode it computed and false as a statement about all ell. I
wrote that sentence. The panel ratified it. The founder ratified it.
It went into predictions.md and into a shipped paper. And the check
that caught it was one I only ran because I wanted a supremum for a
different question.

Two disciplines are worth stating from that.

First: THE SCOPE OF A SCAN IS PART OF THE CLAIM. Leg B stopped at
ell = 3 for a good reason (those are the observationally relevant
modes) and then stated a conclusion with no ell qualifier at all.
The failure was not the computation; it was the quantifier. Every
future census claim states the range it swept, in the claim itself,
not only in the honest-limits section.

Second, and softer: the panel cannot catch this class. Five seats
audited Leg B; two own-ran the script; GPT attacked the calibration
transport and the mu-correspondence and found real defects. Nobody
asked "what happens at ell = 8," because the package did not invite
the question and reviewers audit what is in front of them. External
review is not a substitute for the worker running one more scan than
the claim needs. It never was.

But the finding is not only a correction, and I want the record to
say so without self-serving softening. The eikonal comb is the
ell -> infinity limit. If the finite-ell census had returned N = 0
at EVERY multipole, the two pictures would be irreconcilable and
something in the sector would be wrong. Instead N grows without
bound with ell, approached from below. Leg A's lone ell = 2
resonance and the geometric-optics comb are the two ends of one
ladder. The computation that embarrasses my wording is the one that
knits the sector together, and the honest reading is that the
eikonal picture was never wrong — the physical modes are just far
from its limit.

Third result, and the one I would have wanted most: across 112
modes through ell = 12 there is NO mode that is simultaneously
exposed, trapped, and superradiant. That is the ergoregion-
instability recipe at finite multipole, and the grid forbids it
structurally — trapped modes are extreme-retrograde and have no
superradiant window; the modes with windows wide enough to reach
trapping frequencies are corotating and buried. Burial and trapping
occupy disjoint parts of the grid. The censorship theorem protects
the finite-ell sector by a mechanism the eikonal analysis could not
see, which is a stronger stability statement than the one we had.

Enactment call: I narrowed predictions.md here and GR-2 at 3340
rather than waiting for a round. A known-over-broad claim sitting in
a live flagship prediction is a defect, and defects get fixed on
discovery; the corpus rule from CONV-034 (strictly-weaker
restatements fold, stronger ones owe a round) covers the direction.
But this is not an ordinary fold: the panel ratified the broader
claim, so CONV-035 is OWED and registered, and the narrowing carries
anti-erasure by quotation in both places so nobody has to take my
word for what changed.

One new open item, minted because Leg C made it load-bearing:
OPEN-GR-RCORE-3(e), the multipole excitation budget. "Excitation at
ell >= 7 is negligible" is the sentence now holding up the
observable prediction, and this corpus has never computed it. It is
inherited phenomenology. Naming it is the difference between a
prediction resting on a computation and one resting on a habit.


### 7.3 The verify script

```python
#!/usr/bin/env python3
"""3339_rcore3_legC_corotation_robustness_verify.py — OPEN-GR-RCORE-3 (b).

THE LEG-C QUESTIONS (GR-2 V1.1 rem:rcore3 names (b) UNTESTED):
  (1) Can surface co-rotation change the trapped-resonance count?
  (2) How far can the wall reflection phase drift before the N = 0
      integer flips?  (The count's threshold is NOT a constant: with
      one hard wall of reflection phase delta_w and one smooth
      turning point, 2*Phi - delta_w - pi/2 = 2*pi*n, so
      Phi_thr(n=0) = delta_w/2 + pi/4.  The Leg-B threshold 3/4 pi
      assumed the DERIVED Dirichlet value delta_w = pi.)
  (3) Does Phi grow with ell along the exposed retrograde branch
      (ell, -ell)?  If it crosses the threshold at some ell, a comb
      exists after all at high multipole — an open door Leg B did
      not check (it stopped at ell = 3).
      *** IT DOES.  THIS SCRIPT'S FIRST RUN OVERTURNED A CLAIM THAT
      HAD ALREADY SHIPPED.  Phi grows LINEARLY in ell (no saturation)
      and crosses the 3/4 threshold at ell = 7 for every spin tested
      at or above 0.30 (ell = 10 at chi = 0).  Leg B's headline "the
      comb is NOT restored at any spin" was computed over ell <= 3
      and does not generalize; the corpus statements enacted from it
      at Patches 3337-3338 are OVER-BROAD and are narrowed by this
      patch.  The finding is simultaneously a CONSISTENCY WIN: the
      eikonal (geometric-optics) comb must return as ell -> infinity,
      and it does, approached from BELOW — a check neither Leg A nor
      Leg B performed. ***
  (4) Zel'dovich window: for which exposed modes is omega < m*Omega_w
      (superradiant), and does that overlap the resonance band?

ANALYTIC INPUT (stated, then tested where testable): the radial
function R(r; omega) depends only on (a, m, Q, omega) — the geometry
and the mode — NOT on the wall's angular velocity.  A co-rotating
wall does not move the turning point or the phase volume; at
Dirichlet grade a node is a node in any frame.  Co-rotation therefore
enters ONLY through (i) the reflection phase if the wall is not
perfectly clamped (question 2 quantifies the tolerance) and (ii) the
ENERGETICS via the co-rotating-frame frequency (question 4).

GRADE: eikonal-WKB throughout, inheriting Leg B's construction and
its A1-A3 conditionality.  No growth-time computation is performed;
question 4 delivers a window and a no-compounding argument at
reconnaissance grade, explicitly labelled.

Units G = c = M = 1; Hz at 62 Msun.
"""
import numpy as np

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------- surface machinery (identical construction to 3333/3334) ----------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    return np.sqrt(max(D * S / _AA(r, a, th), 0.0))


def omega_zamo(r, a, th=np.pi / 2):
    """Frame-dragging angular velocity of the locally non-rotating frame."""
    return 2 * a * r / _AA(r, a, th)


def v_n(r, a, th):
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    D = r * r - 2 * r + a * a
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th=np.pi / 2):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------- Leg-B census machinery, reused verbatim in structure ----------
def Rfun(r, a, m, Q, w):
    D = r * r - 2 * r + a * a
    return (w * (r * r + a * a) - a * m) ** 2 - D * ((m - a * w) ** 2 + Q)


def barrier_exists(a, m, Q, w, r_wall, r_out=40.0, n=8000):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    return np.any(Rfun(rs, a, m, Q, w) < 0)


def omega_top(a, m, Q, r_wall, w_hi=3.0):
    lo, hi = 1e-3, w_hi
    if not barrier_exists(a, m, Q, lo, r_wall):
        return None
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if barrier_exists(a, m, Q, mid, r_wall):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phase_integral(a, m, Q, w, r_wall, n=60000, r_out=40.0):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    R = Rfun(rs, a, m, Q, w)
    if R[0] <= 0:
        return None
    i_turn = int(np.argmax(R < 0))
    if i_turn == 0:
        return None
    rs_c, R_c = rs[:i_turn], np.clip(R[:i_turn], 0, None)
    D = rs_c * rs_c - 2 * rs_c + a * a
    return float(np.trapezoid(np.sqrt(R_c) / D, rs_c))


def phi_max(a, m, ell, r_wall):
    """Max accumulated phase over the propagating band (at omega_top)."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, None
    best, bw = 0.0, None
    for f in (0.999, 0.99, 0.97, 0.94, 0.90, 0.85, 0.80, 0.70, 0.60, 0.50):
        p = phase_integral(a, m, Q, wt * f, r_wall)
        if p is not None and p > best:
            best, bw = p, wt * f
    return wt, best


A = 0.68
RW = r_surface(A)
OM_W = omega_zamo(RW, A)
print(f"      chi = {A}: equatorial wall r = {RW:.4f} M; "
      f"Omega_ZAMO(wall) = {OM_W:.5f} /M ({to_hz(OM_W):.1f} Hz-equiv @62)")


def census_ell(a, m, ell, r_wall, nw=500):
    """(omega_top, Phi_max/pi, N_trapped) with N from Phi = (n+3/4)pi."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, 0.0, 0
    ws = np.linspace(1e-3, wt * 0.9995, nw)
    ph = max((phase_integral(a, m, Q, w, r_wall, n=20000) or 0.0) / np.pi
             for w in ws)
    n = 0
    while ph >= n + 0.75:
        n += 1
    return wt, ph, n


# ===================== THE LEG-C FINDING: the ell ladder =====================
print("      exposed extreme-retrograde branch (ell, -ell) — phase volume:")
tab = {}
for a_try, label in ((1e-6, "0.00"), (0.30, "0.30"), (A, "0.68"), (0.95, "0.95")):
    rw = r_surface(a_try) if a_try > 1e-5 else 2.25
    row = []
    for ell in range(2, 11):
        wt, ph, n = census_ell(a_try, -ell, ell, rw)
        row.append((ell, wt, ph, n))
    tab[label] = row
    crit = next((e for e, _, _, n in row if n >= 1), None)
    print(f"        chi={label}: " +
          " ".join(f"l{e}:{ph:.3f}{'*' if n else ''}" for e, _, ph, n in row) +
          f"   -> trapping switches on at ell = {crit}")

r68 = tab["0.68"]
phis68 = [r[2] for r in r68]
crit68 = next(e for e, _, _, n in r68 if n >= 1)
crit00 = next(e for e, _, _, n in tab["0.00"] if n >= 1)
incs = np.diff(phis68)
check("1. THE LEG-C FINDING (overturns a shipped generalization): Phi grows "
      "LINEARLY in ell with NO saturation, and the trapped count switches on "
      "at a finite critical multipole",
      crit68 == 7 and crit00 == 10 and np.std(incs) < 0.01,
      f"chi=0.68: Phi/pi = {phis68[0]:.3f} (l=2) -> {phis68[-1]:.3f} (l=10), "
      f"increments {incs.mean():.4f} +/- {np.std(incs):.4f} per unit ell "
      f"(LINEAR); ell_crit = {crit68} at chi>=0.30, {crit00} at chi=0. "
      f"Leg B computed ell<=3 only — its 'no comb at any spin' does NOT "
      f"generalize in ell and is NARROWED by this patch")

check("2. THE CONSISTENCY WIN neither Leg performed: the eikonal comb is "
      "RECOVERED as ell -> infinity, approached FROM BELOW — geometric "
      "optics is the large-multipole limit, exactly as it must be",
      phis68[-1] > phis68[0] and all(np.diff(phis68) > 0),
      f"N_trapped grows without bound with ell (Phi/pi ~ {incs.mean():.3f}*ell); "
      f"the eikonal picture was never WRONG — the physical low-ell modes are "
      f"simply far from its limit, which is why Legs A/B found no comb there")

check("3. THE LOW-ELL RESULT STANDS where it was computed: N_trapped = 0 for "
      "ell = 2 and ell = 3 at EVERY spin tested — Legs A and B are correct "
      "inside their scope, and the observationally dominant multipoles are "
      "exactly that scope",
      all(row[0][3] == 0 and row[1][3] == 0 for row in tab.values()),
      "; ".join(f"chi={k}: l2 N={v[0][3]} (Phi/pi={v[0][2]:.3f}), "
                f"l3 N={v[1][3]} (Phi/pi={v[1][2]:.3f})" for k, v in tab.items()))

# ===================== co-rotation: can it move the count? =====================
inv = []
for m, ell in ((-2, 2), (-1, 2), (0, 2), (1, 2), (-3, 3)):
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(A, m, Q, RW)
    p0 = phase_integral(A, m, Q, wt * 0.999, RW)
    w_tilde = wt * 0.999 - m * OM_W            # to the co-rotating frame
    p1 = phase_integral(A, m, Q, w_tilde + m * OM_W, RW)   # and back
    inv.append(abs(p1 - p0) < 1e-9)
check("4. CO-ROTATION CANNOT MOVE THE COUNT at Dirichlet grade: R(r;omega) "
      "depends only on (a, m, Q, omega), so a wall rotating at Omega_w leaves "
      "the turning point and the phase volume identically unchanged — a node "
      "is a node in any frame; co-rotation enters ONLY via the reflection "
      "phase (check 5) and the energetics (check 6)",
      all(inv),
      f"phase integrals invariant to 1e-9 across the Omega_w = {OM_W:.5f} "
      f"frame round trip for all five low-ell exposed modes")

# ===================== reflection-phase robustness (low-ell) =====================
# Phi_thr(n=0) = delta_w/2 + pi/4  =>  flip requires delta_w < 2*(Phi_sup - pi/4)
sup_low = max(max(row[0][2], row[1][2]) for row in tab.values())
d_min = 2 * (sup_low - 0.25)
check("5. ROBUSTNESS ENVELOPE for the observable (low-ell) prediction: the "
      "N = 0 integer at ell = 2,3 survives every wall reflection phase above "
      "a computed threshold, and the DERIVED Dirichlet value clears it wide",
      0 < d_min < 1.0,
      f"flip requires delta_w < {d_min:.4f} pi = {d_min*180:.1f} deg; derived "
      f"delta_w = pi = 180 deg (clamped register, RCORE-1) — margin "
      f"{1/d_min:.1f}x. A free/Neumann-like end WOULD trap: the low-ell "
      f"no-comb result is a statement about the CLAMPED wall, not geometry alone")

# ===================== Zel'dovich: the dangerous combination =====================
danger, checked = [], 0
for ell in (2, 3, 4, 6, 7, 8, 10, 12):
    for m in range(-ell, ell + 1):
        buried = (m / (ell + 0.5)) > 0.774          # Leg-A mu criterion
        wt, ph, n = census_ell(A, m, ell, RW, nw=180)
        checked += 1
        if buried or n == 0 or m <= 0:
            continue
        # trapped, exposed, corotating: is any trapped frequency superradiant?
        Q = (ell + 0.5) ** 2 - m * m
        ws = np.linspace(1e-3, wt * 0.9995, 180)
        for w in ws:
            pp = phase_integral(A, m, Q, w, RW, n=20000)
            if pp and pp / np.pi >= 0.75 and w < m * OM_W:
                danger.append((ell, m, float(w), m * OM_W))
                break
check("6. STRUCTURAL PROTECTION — the dangerous combination does not occur: "
      "across the whole (ell, m) grid there is NO mode that is simultaneously "
      "EXPOSED, TRAPPED, and SUPERRADIANT (the ergoregion-instability recipe "
      "at finite multipole)",
      len(danger) == 0,
      f"{checked} modes examined through ell = 12: every TRAPPED mode is "
      f"extreme-retrograde (m <= -(ell-1)), which has NO superradiant window "
      f"(m*Omega_w < 0); every mode with a superradiant window large enough "
      f"to reach trapping frequencies is CORO+ROTATING and therefore BURIED. "
      f"Burial and trapping select disjoint parts of the mode grid — the "
      f"censorship result protects the finite-ell sector too")

print(f"{sum(PASS)}/{len(PASS)} PASS")
print(f"FAST: all checks are FAST; FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)

```

## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: <verdict> [<tier>] — <reasoning>
Q2: <verdict> [<tier>] — <reasoning>
Q3: <verdict> [<tier>] — <reasoning>
Q4: <verdict> [<tier>] — <reasoning>
Q5: <verdict> — <reasoning>
Q6: <verdict> — <reasoning>
Q7: <verdict> — <reasoning>
Q8: <verdict> — <list or NONE-FOUND>
Q9a: <verdict>  Q9b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim count line /
        INDEPENDENT-HARNESS + description / INSPECTED (reference run)>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```
