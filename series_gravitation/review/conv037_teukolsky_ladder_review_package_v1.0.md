# CONV-037 REVIEW PACKAGE v1.0 — The Teukolsky Ladder (Patches 3353–3359): OPEN-GR-RCORE-3 discharged, and the flagship echo frequency moves to 191 Hz
# (Patch 3360, 30 Aug 2026, Session 157)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package — one
identical paste per seat (Copilot may need the file-upload route).
Execution-capable seats also receive the `.py` files shipped alongside
(3356, 3358, 3359 are the load-bearing three; 3359 runs in ~3 min, no
FAST subset exists for it). Returns INLINE, verbatim.

**ID NOTE:** this round is CONV-037, not -036. Two DE-lane documents
dated 26 Aug already reference "CONV-036"; whether that is an earmark
or a typo could not be verified, and this programme lost three patches
to an ID collision this week. Gaps are cheap; collisions are not.

---

## §0 What this round decides, in one paragraph

Since the panel last sat (CONV-035), the GR lane built the full
Teukolsky solver in seven validated rungs and used it to compute the
**first exact gravitational (s = −2) Kerr wall resonances** for the
CPP horizonless remnant at the GW150914 benchmark (χ = 0.68, derived
surface r_w = 2.2668 M). **Result: the retrograde-keyed (2,−2) line is
at 191 Hz with Q = 2.09; (3,−3) at 288 Hz, Q = 4.24.** That is BELOW
every prior estimate this panel has seen — the eikonal barrier top
(211 Hz), the transport CONV-034 withdrew (247 Hz), and the exact
scalar-sector line (251 Hz) — and it is the number the registered
prediction PRED-O-39 and the shipped paper GR-2 V1.5 would now carry.
**A flagship frequency moving is exactly what this panel exists to
gate.** Along the way the worker made three corrections to his own
earlier work (Leg A's Q ≈ 5 → 1.9–2.1; 3353's direction call reversed
at 3354; 3358's scalar-proxy framing corrected and its (2,+1) value
WITHDRAWN as a non-converged root), found a hard method limit
(direct integration cannot see Q ≲ 1.5 modes), and consequently
**downgraded** the retrograde-keyed *ordering* test back to eikonal-WKB
grade. Every one of those is under review here too.

GitHub (repo `CPP`, branch `main`, HEAD = Patch 3359):
`series_gravitation/rcore_derivation/335{3,4,6,7,8,9}_*.md`,
`series_gravitation/code/335{3,4,6,7,8,9}_*_verify.py`.

## §1 Under review / fenced

UNDER REVIEW: (a) the validation ladder itself — Leaver Schwarzschild
(3356 R1), Leaver Kerr vs tabulated QNMs (3358 A1), Sasaki–Nakamura
reduction to Regge–Wheeler and the a = 0 wall-mode reproduction
(3359 T1–T3); (b) the gravitational spectrum (3359 §2); (c) the
boundary-condition choice — Dirichlet on the SN variable X as the Kerr
generalisation of the CPP "clamped register" node; (d) the three
self-corrections and the 3358 withdrawal; (e) the method limit and the
ordering-test downgrade; (f) the PROPOSED PRED-O-39 / GR-2 amendment
text (§5 below); (g) the standing scope audit (3347 practice).

FENCED (settled, not re-adjudicated): A1–A3 / censorship (CONV-032);
the derived surface r_w(a); GR-2's eikonal-scoped template and its
2.624 ms early-transient delay (CONV-033/034); the 3352 disjointness
theorem and 3355 corollary (they use only R(r_w) < 0 in the window and
are untouched by any number here); CONV-035's Q6 process ruling.

## §2 The ladder, as claim chains

L1 (3356 R1) Leaver's Schwarzschild continued fraction, written from
   memory, reproduces published QNMs at ℓ = 2, 3, 4 to 7.5e−6.
L2 (3356 R2) Direct inward integration with the wall reproduces Leg A's
   TD peak to −0.05% and gives the first exact complex resonance:
   0.44859 − 0.11749i, Q = 1.91. Leg A's Wigner-delay Q ≈ 4.9 was
   2.5× too narrow — corrected.
L3 (3353/3357/3358) The angular sector: exact scalar eigenvalue vs the
   eikonal (ℓ+½)² (+4.4% at ℓ = 2, +0.5% at ℓ = 7 — GPT's objection
   measured); the s = −2 eigenvalue via finite differences (ℓ ≥ 3) and
   via Leaver's angular CF (all ℓ, closing the ℓ = 2 gap).
L4 (3354) Census re-run with exact Q(ω): ℓ_crit = 7 ± 1 UNCHANGED at
   three spins; 3353's "could move DOWN" was a one-sided argument and
   is reversed (ω_top also drops; net residue −3e−4, opposite sign).
L5 (3358 A1) Leaver's Kerr CFs (angular + radial, s = −2, from memory)
   reproduce tabulated (2,2) Kerr QNMs at a/M = 0, 0.5, 0.7, 0.9 to
   ≤ 1.2e−4.
L6 (3358 B) Exact SCALAR Kerr wall modes: (2,−2) 251 Hz Q 2.06;
   (3,−3) 327 Hz Q 4.00. (2,+1) WITHDRAWN at 3359 (see L8).
L7 (3359 T1–T3) Sasaki–Nakamura, from memory: reduces to RW at a = 0
   pointwise (1.6e−9, F ≡ 0); short-range in Kerr; reproduces L2's
   wall mode from independent code to 2.7e−6.
L8 (3359 §2–4) GRAVITATIONAL Kerr wall modes: (2,−2) 0.36694 − 0.08782i
   → 191.2 Hz, Q 2.09; (3,−3) 0.55333 − 0.06522i → 288.4 Hz, Q 4.24;
   each individually r₀-independent (3e−9) and sharp (6e−9). (2,+1)
   NOT LOCATED: the root-finder returned its own guess (contrast 0.75);
   at Q ≈ 1 the inward instability is ~e^27. The scalar (2,+1) from L6
   had passed no such test and is WITHDRAWN. Consequence: the
   retrograde-keyed ORDERING test is not established at exact grade
   in either sector and reverts to eikonal-WKB grade.
L9 (3359 §3) Gravitational lines sit 12–24% BELOW scalar (ratios
   0.763, 0.881); a = 0 already showed it (RW/scalar = 0.794). 3358's
   "scalar = exact version of the lane's grade" was right for STRUCTURE,
   wrong for POSITIONS. The withdrawn "+17% above the top" was
   wrong-SIGNED for GWs: the (2,−2) line sits 7% BELOW the geodesic top.

## §3 Triage — the worker's six weakest points

T-1 **The boundary condition.** Dirichlet on the SN variable X is the
    natural Kerr generalisation of Leg A's ψ = 0 and reduces to it at
    a = 0. But is X = 0 what the CPP "clamped register" actually
    implies for gravitational perturbations of a rotating surface? The
    corpus has never derived the Kerr wall condition from the
    substrate; it has assumed the RW analogue. Rule on whether that is
    a fenced inheritance or an unexamined assumption.
T-2 **SN from memory.** T1–T3 are strong, but they test the a = 0
    limit and the far-field. A term proportional to a that vanishes at
    a = 0 AND at large r would pass all three. Is there a Kerr-specific
    check the worker should have run (e.g. reproducing a tabulated
    Kerr QNM via SN direct integration with a horizon-side condition)?
T-3 **No error budget on 191 Hz.** The number carries convergence and
    stability assertions but NO physical error budget: mass ±6.5% (the
    GR-2 budget) propagates trivially, but SPIN dependence at exact
    grade is unknown (one spin computed), and the A1–A3 surface
    location r_w(a) feeds directly into the cavity length. Is "191 Hz"
    honest without a stated band?
T-4 **The method limit.** Direct integration is validated for
    |Im ω| ≲ 0.12 and fails at 0.3. The reported (2,−2) at Im = −0.088
    and (3,−3) at −0.065 are inside the validated range — but is the
    boundary between "works" and "returns its guess" as sharp as the
    worker implies, or is there a grey zone that could bias the
    reported widths?
T-5 **The withdrawal chain.** Three self-corrections in seven patches
    (3354 reverses 3353; 3356 corrects Leg A; 3359 corrects 3358 and
    withdraws a number). Is the record honest about each, and is
    anything ELSE downstream of a corrected number still uncorrected?
T-6 **Excitation.** 3349/3350's source-side budget argued (2,−2) is
    the dominant retrograde-keyed line. Nothing in this ladder computes
    relative excitation of (2,−2) vs (3,−3). Is calling (3,−3) "the
    sharpest line" an invitation to over-read it as the best target?

## §4 Frozen questions (answer ALL; vocabulary only)

Q1 — The validation ladder (L1, L5, L7): **SOUND / SOUND-WITH-GAPS / UNSOUND**
Q2 — The SN instrument and the boundary-condition choice (T-1, T-2):
     **VALID / VALID-WITH-CAVEATS / INVALID**
Q3 — The gravitational spectrum, each: (i) (2,−2) at 191 Hz, Q ≈ 2.1;
     (ii) (3,−3) at 288 Hz, Q ≈ 4.2; (iii) no trapped comb at ℓ = 2:
     **CONFIRMED / CONFIRMED-WITH-CAVEATS / NOT-CONFIRMED**
Q4 — The self-corrections and the 3358 withdrawal (T-5):
     **ADEQUATE / INADEQUATE**
Q5 — The method limit and the ordering-test downgrade (T-4):
     **CORRECTLY-SCOPED / UNDER-SCOPED / OVER-SCOPED**
Q6 — The PROPOSED amendment text (§5): **FAITHFUL-AT-GRADE / OVERCLAIMS / UNDERCLAIMS**
Q7 — Scope audit (any universal whose computation is narrower than the
     sentence): **NONE-FOUND / ITEMS-FOUND (list)**
Q8a — Assembly: **PROPER / PROPER-WITH-REVISIONS / IMPROPER**
Q8b — Disposition: **AMENDMENTS-CLEAR / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. Majority OVERCLAIMS on
Q6 BLOCKS the predictions.md execution regardless of Q8b (standing
flagship rule since CONV-034). Majority INVALID on Q2 leaves the
gravitational spectrum UNREGISTERED. Q7 items adopted as work
regardless of tally. Strictly-weaker revisions fold at enactment
(CONV-034/035 precedent); anything STRONGER than what is proposed owes
its own round.

## §5 THE PROPOSED AMENDMENT (what would enter predictions.md and GR-2 V1.6 on clearance)

> **PRED-O-39, refined at gravitational grade (Patch 3359, CONV-037):**
> for a GW150914-class remnant (M = 62 ± 4 M_⊙, χ ≈ 0.68), the
> retrograde-keyed dominant line is at **f(2,−2) ≈ 191 Hz** (exact
> s = −2 Kerr wall resonance ω = 0.3669 − 0.0878i at χ = 0.68), with
> **Q ≈ 2.1** — a single broad top-of-barrier feature, no trapped comb.
> The sharpest line is **(3,−3) ≈ 288 Hz, Q ≈ 4.2**. Mass scaling is
> exact (f ∝ 1/M: ±6.5% for the stated mass band); **spin dependence
> at exact grade is computed at one spin only and is not yet a band**.
> The early broadband transients at the eikonal delay 2.624 ms are
> unchanged. The retrograde-keyed *ordering* discriminator stands at
> eikonal-WKB grade only: its prograde comparator (2,+1) is too broad
> (Q ≲ 1.5) for the present instrument. Supersedes the orientation-scale
> eikonal tops (211/233/260/294 Hz) registered at Patch 3337, which are
> retained as superseded per anti-erasure. Conditional on A1–A3
> (OPEN-GR-RCORE-4).

## §6 Seat mandates

- **IDENTITY:** own model name. Gemini seat: you are Gemini. DeepSeek
  seat: you are DeepSeek.
- **OWN-RUN:** SCRIPT-EXECUTED = your own run. 3359 takes ~3 minutes
  (no FAST subset); 3356 ~2 min; the others under a minute. Reference
  count lines: 3359 9/9, 3358 9/9, 3357 6/6, 3356 8/8, 3354 7/7,
  3353 9/9. INDEPENDENT-HARNESS welcome (e.g. your own SN check).
- **COUNT-LINE** verbatim; **TIER** on every answer; **RETURNS** inline
  in the §8 skeleton.

Steers: **GPT** — T-1 and T-2 are yours; you have been right four
rounds running on grade, so rule hard on whether X = 0 is derived or
assumed. **Grok** — own-run 3359 and 3356; audit T-4, the
direct-integration stability boundary. **Gemini** — T-3: is "191 Hz"
EARNED without a spin band? Your CONV-035 standard applies. **Copilot**
— T-5: the withdrawal chain and anti-erasure in 3358's corrected
record; confirm nothing downstream of a withdrawn number is still live.
**DeepSeek** — falsifiability of the amended prediction: what kills a
191 Hz / Q 2 line? Is Q ≈ 2 too broad to be a useful target?

## §7 Materials — the six records in full, and the load-bearing script

### 7.1 Patch 3353 record
# Teukolsky Leg 1 — the eikonal Carter constant's error, finally computed: the dissent seat was right, and the correction cuts against us

**Patch 3353, 30 Aug 2026 — Session 157.** Verify:
`code/3353_teukolsky_angular_verify.py`, **9/9 PASS** (all-FAST).
Charter: the full-Teukolsky item, taken by its separable angular half.

---

## §1 Why the angular sector first

Every result in this lane since Patch 3334 rests on the eikonal Carter
constant **Q_eik = (ℓ+½)² − m²**: the census, ℓ_crit, the excitation
budget, and the disjointness theorem. GPT objected to it twice —
CONV-034 ("an eikonal correspondence applied at ℓ = 2") and CONV-035
("materially more credible at ℓ ≳ 7 than at ℓ = 2"). **Nobody had ever
computed the error.** Matching the radial equations term by term
identifies the exact quantity as **Q_exact = A_{ℓm}(aω) − m²**, so the
approximation is precisely the claim A ≈ (ℓ+½)².

## §2 The error, quantified at the modes the lane actually uses

| mode | aω | **A_exact** | A_eik | rel. error | used by |
|---|---|---|---|---|---|
| (2,−2) | 0.2757 | 5.9891 | 6.2500 | **+4.36%** | census, 3334 |
| (2,+2) | 0.4366 | 5.9727 | 6.2500 | **+4.64%** | burial, 3333 |
| (3,−3) | 0.3809 | 11.9839 | 12.2500 | +2.22% | census, 3334 |
| (7,−7) | 0.7855 | 55.9636 | 56.2500 | **+0.51%** | ℓ_crit, 3339/3349 |
| (9,−9) | 0.9395 | 89.9579 | 90.2500 | +0.32% | discharge, 3349 |
| (12,−12) | 1.1529 | 155.9507 | 156.2500 | +0.19% | domain edge, 3339 |

**GPT was right in direction and the size is now on the record:**
worst low-ℓ error **+4.6%** against worst high-ℓ error **+0.5%** — a
factor of nine. The unquantified caveat the panel kept flagging is now
a number.

The correspondence also degrades monotonically with aω — (2,−2) runs
+4.2% at aω = 0 to +10.3% at aω = 1.5 — so the error is largest
exactly where this lane works, at high spin and high frequency.
Recorded rather than hoped.

## §3 The direction cuts against us, and that is why it is stated first

Q enters the radial function with a **minus** sign:
R = K² − Δ[(m−aω)² + Q]. The eikonal value **overshoots**, so the exact
Q is *smaller*, so R is *larger*, so the phase volume Φ is *larger* —
**trapping is slightly easier than the eikonal census assumed, and
ℓ_crit could move DOWN rather than up.**

That is the unfavourable direction. It does not overturn anything yet
(a +0.5% shift in A at ℓ = 7 is far below the ±1 already carried on
ℓ_crit), but it is the direction a reader should be told about without
having to derive it.

## §4 What survives untouched, and why

**The 3352 disjointness theorem is completely unaffected.** Its Step 3
used only **Q > 0**, never Q's value. Exact Q remains positive at every
sampled mode (minimum 1.97), so the stability result is insensitive to
this correction *by construction* — an accidental robustness worth
naming, since the theorem is now the lane's strongest claim.

## §5 What the failures taught, kept in the code

The self-validation check failed **three times** before passing, and
each failure was informative rather than fatal:

1. **m = 0 is wrong** — the discretisation imposes S = 0 at the poles,
   correct for m ≠ 0 and wrong for m = 0 (Legendre solutions satisfy
   P_ℓ(±1) = ±1). Fenced, with its reason; no reported mode has m = 0.
2. **Intermediate |m| < ℓ degrades** — the pole behaviour
   (1−x²)^{|m|/2} vanishes weakly there and a uniform grid resolves it
   poorly (error 1.8e−1 at ℓ = 5, 8). Fenced; no reported mode is one.
   A graded mesh or the (1−x²)^{|m|/2} substitution recovers it, and
   belongs with the s = −2 build.
3. **The tolerance was the wrong metric** — an absolute bar silently
   tightens as eigenvalues scale like ℓ(ℓ+1). Replaced by a *relative*
   bar benchmarked against the smallest effect claimed: discretisation
   error is 1.6e−7, a factor **11,690** below the +0.19% at ℓ = 12, so
   the measurement is not reporting its own grid.

**|m| = ℓ — the sector every reported mode lives in — reproduces
ℓ(ℓ+1) to machine precision at every N from 800 to 6400.**

## §6 Fence, declared before results and asserted in code

This is the **scalar (s = 0)** angular sector. The gravitational case
is s = −2, whose eigenvalue differs. This patch therefore
**characterises the correspondence's error and its scaling**; it does
**not** deliver gravitational separation constants, and it does **not**
deliver Teukolsky line positions. The radial sector is untouched.

## §7 Registry impact

- **The eikonal-Q criticism (CONV-034 Q3(iii), CONV-035 Q1) is
  DISCHARGED in size**: +4.6% at ℓ = 2, +0.5% at ℓ = 7, +0.19% at
  ℓ = 12, degrading with aω.
- **OPEN-GR-RCORE-3 remaining, now sharper:** (i) the s = −2 angular
  sector; (ii) the **radial** Teukolsky integration with
  Sasaki–Nakamura stabilisation and complex root-finding — *the heavy
  item, and the one where a higher model tier earns its keep*;
  (iii) Zel'dovich growth-time bounds.
- **Queued, not enacted:** a census re-run with exact Q to see whether
  ℓ_crit moves. Cheap, and it should be done before any GR-2 amendment
  that quotes ℓ_crit more precisely than ±1.


### 7.2 Patch 3354 record
# The census with the exact Q — ℓ_crit does not move, and 3353's direction call was wrong

**Patch 3354, 30 Aug 2026 — Session 157.** Verify:
`code/3354_census_exact_Q_verify.py`, **7/7 PASS** (all-FAST). Charter:
the item 3353 queued as owed before any GR-2 amendment quotes ℓ_crit
tighter than ±1.

---

## §1 The result

The Bohr–Sommerfeld census re-run with the exact, frequency-dependent
separation constant **Q(ω) = A_{ℓm}(aω) − m²** in place of the fixed
eikonal Q = (ℓ+½)² − m², on the extreme-retrograde branch at χ = 0.68:

| ℓ | Φ/π eikonal | Φ/π exact | ΔΦ/π | ω_top eik → exact | N |
|---|---|---|---|---|---|
| 2 | 0.2459 | 0.2456 | −0.0003 | 0.4055 → 0.3953 | 0 |
| 3 | 0.3676 | 0.3674 | −0.0002 | 0.5601 → 0.5528 | 0 |
| **6** | 0.7336 | 0.7336 | −0.0000 | 1.0246 → 1.0204 | 0 |
| **7** | 0.8558 | 0.8557 | −0.0000 | 1.1794 → 1.1758 | **1** |
| 12 | 1.4666 | 1.4666 | −0.0000 | 1.9538 → 1.9514 | 1 |

**ℓ_crit = 7, unchanged** — at χ = 0.68, 0.30 and 0.95. The ℓ = 6 miss
stays at +0.0164 below threshold. N = 0 at ℓ = 2, 3 stands. The
reflection-phase envelope is unchanged to four figures (0.2348π).

## §2 3353's direction prediction was one-sided, and this patch corrects it

3353 argued: Q enters R with a minus sign, the eikonal Q overshoots, so
the exact Q raises R and raises Φ — *trapping gets easier, ℓ_crit could
move down.* **That argument considered only the fixed-ω effect.** The
exact (smaller) Q also **lowers the barrier top**, so Φ_max is evaluated
at a lower ω_top, and the two effects cancel to better than 10⁻³ — with
a tiny **net negative** residue, the opposite sign from the one flagged.

The check built on 3353's prediction failed on the first run and was
rewritten to record the corrected physics rather than smoothed into
agreement. **A 4.4% error in Q at ℓ = 2 becomes a 0.03% error in Φ.**

## §3 What this settles

- **The eikonal census is robust to the correction its critics asked
  for.** GPT's CONV-034/035 objection was right about the *size* of the
  Q error (3353 measured it) and right that it should be computed; it
  turns out not to move any census conclusion, because the quantity the
  census actually depends on is insensitive to it by near-cancellation.
  That is a better answer than "the error is small" — it is "the error
  is 4%, and here is why 4% doesn't matter."
- **GR-2's ℓ_crit = 7 ± 1 stands as written**; the queued amendment need
  not tighten it and now should not.
- **The +0.0164 margin at ℓ = 6 is a real number, not a convention
  artefact**: it survives the correction unchanged.

## §4 Fence

|m| = ℓ only (3353's validated sector, enforced by an assert); scalar
s = 0 angular eigenvalues, **not** s = −2; self-consistent WKB census,
**not** a Teukolsky mode calculation. The radial Teukolsky build — the
genuinely heavy item — remains OPEN and is not started on this tier.

## §5 Registry impact

- 3353's queued item **DISCHARGED**: ℓ_crit does not move.
- 3353's "could move DOWN" flag **CORRECTED** to "does not move; net
  residue negligible and slightly negative."
- **OPEN-GR-RCORE-3 remaining:** s = −2 angular; radial Teukolsky with
  Sasaki–Nakamura and complex root-finding; Zel'dovich bounds.
- GR-2 amendment queue: unchanged in content; the ℓ_crit line is
  confirmed rather than revised.


### 7.3 Patch 3356 record
# Teukolsky ladder, rungs 1–2 — the radial build begins on validated ground, and the first exact complex resonance corrects Leg A's width by 2.5×

**Patch 3356, 30 Aug 2026 — Session 157.** Verify:
`code/3356_teukolsky_ladder_rungs12_verify.py`, **8/8 PASS**.

## §1 Rung 1 — validation against known answers

Leaver's continued fraction for Schwarzschild, recurrence written from
memory — precisely the kind of step that has been wrong twice this
session, which is *why* known answers are the test:

| ℓ | computed | published | rel. error |
|---|---|---|---|
| 2 | 0.37367 − 0.08896i | 0.37367 − 0.08896i | 7.5e−6 |
| 3 | 0.59944 − 0.09270i | 0.59944 − 0.09270i | 7.4e−6 |
| 4 | 0.80918 − 0.09416i | 0.80918 − 0.09416i | 5.3e−6 |

Root-finder and recurrence proven to five figures before any new
physics is touched.

## §2 Rung 2 — the first exact complex wall resonance in the lane

Direct inward integration from the outgoing asymptotic solution
(coefficients fitted numerically to the ODE residual, not recalled),
Dirichlet wall at areal 9M/4, χ = 0, ℓ = 2:

| parity | ω (M = 1) | f @ 62 M_⊙ | **Q** | e-fold time |
|---|---|---|---|---|
| Regge–Wheeler | **0.44859 − 0.11749i** | 233.8 Hz | **1.91** | 8.5 GM |
| Zerilli | 0.44506 − 0.13442i | 232.0 Hz | 1.66 | 7.4 GM |

**Instrument validation, asserted:** the root is independent of the
integration start (r₀ = 40, 60, 80 agree to 2.5e−8 — the instability
test for Im ω < 0), and the zero is sharp (|ψ| at the root is 6e−8 of
its value a small step away).

## §3 Against Leg A (3333): position right, width wrong by 2.5×

- **Position:** exact Re ω = 0.44859 vs Leg A's time-domain peak
  0.4488 (**−0.05%**) and its FD Wigner peak 0.4535 (−1.1%). Leg A's
  TD cross-check was, in hindsight, the more accurate of its two
  instruments.
- **Width — a correction, stated as one:** Leg A inferred **Q ≈ 4.9**
  from the Wigner delay τ = 21.5. The exact root gives **Q = 1.91**.
  The Wigner-delay-to-lifetime mapping is unreliable for a resonance
  sitting on the barrier top, and it overestimated the lifetime ~2.5×.
  That Q ≈ 5 propagated into GR-2 (demoted at CONV-034 to a
  "directional note" for the Kerr transport, but still quoted) — **the
  note now needs the exact number.** The line is broader than the
  paper implies.
- **The anchor re-measured:** the above-top shift is **+15.3%** exact
  (was +17% from the FD peak).

## §4 What this means for the observable prediction

Nothing moves in *position* — 234 Hz vs 236 Hz at the benchmark. But
a broader line (Q ≈ 1.9 rather than ≈ 5) is a **less sharp
spectroscopic target**, and GR-2 V1.5's "Q ≈ 5, indicating direction
and rough scale" should read "Q ≈ 1.9 at χ = 0, ℓ = 2 (exact); Kerr
widths not yet computed." Queued for the next GR-2 touch; it weakens
a directional note rather than a registered quantity, so it folds
without a round.

## §5 Scope and what remains

Schwarzschild only; RW/Zerilli (s = 2 axial/polar), not Kerr
Teukolsky; direct integration validated at r₀ = 40–80 (instability
grows beyond ~120). **Rung 3 — Kerr, s = −2, Sasaki–Nakamura — is the
remaining heavy build and is not started here.** The instrument that
will do it (numerically-fitted outgoing series + inward integration +
complex root-finding + r₀-independence and sharpness assertions) is
now validated on the case where the answer was known, which is the
only honest way to start.


### 7.4 Patch 3357 record
# Rung 3a — the gravitational (s = −2) angular sector: validated two ways, and 3353's fence is priced

**Patch 3357, 30 Aug 2026 — Session 157.** Verify:
`code/3357_teukolsky_angular_s2_verify.py`, **6/6 PASS** (all-FAST).

## §1 Validation, before any new number

Two independent known checks on the spin-weighted angular operator:

- **K1 (c → 0):** A = ℓ(ℓ+1) − s(s+1) = ℓ(ℓ+1) − 2, reproduced to 1e−7
  relative for every |m| = ℓ, ℓ = 4–12.
- **K2 (first-order slope, sign-sensitive):** dA/dc at c = 0 matches
  the known −2ms²/(ℓ(ℓ+1)) to 5e−4 — the check a c = 0 limit cannot
  see, and the one that would have caught a wrong sign in the 2csx term.

**Endpoint discipline, applied before running** (the 3353 lesson):
S ~ (1−x)^{|m+s|/2}(1+x)^{|m−s|/2}. ℓ ≥ 4 has both exponents ≥ 1 and
converges to machine precision. **ℓ = 3** has one exponent of exactly
½ and converges at **first order** (observed order 0.99) — reported
with a Richardson-extrapolated value and a stated ±9e−4, not dropped
and not passed off as exact. **ℓ = 2 is excluded** with its reason: for
s = −2, |m| = 2, one pole exponent is *zero*, which needs the
endpoint-regularised method. That is the observable line, so the
fence is stated up front.

## §2 The result, and the hypothesis it overturned

| ℓ | c = aω_top | A(s = −2) | A(s = 0) | residual beyond −s(s+1) | 1st-order prediction 8c/(ℓ+1) | relative to A |
|---|---|---|---|---|---|---|
| 3 | 0.3759 | 10.686 | 11.984 | +0.701 | +0.752 | 6.6% |
| 7 | 0.7995 | 54.695 | 55.962 | **+0.732** | +0.800 | **1.3%** |
| 9 | 1.0106 | 88.690 | 89.951 | +0.738 | +0.808 | 0.8% |
| 12 | 1.3270 | 154.679 | 155.935 | +0.744 | +0.817 | 0.5% |

**I expected the residual to shrink with ℓ. It doesn't — it sits at
~+0.7 and grows slightly. The failure was the hypothesis, not the
number.** The residual *is* the first-order spin-weight term
−2ms²c/(ℓ(ℓ+1)) = +8c/(ℓ+1) for m = −ℓ; since c = aω_top grows
~linearly with ℓ while the coefficient falls as 1/ℓ, the product tends
to a constant. The measured residual matches that analytic prediction
to within higher-order corrections at every ℓ.

**Relative to A ~ ℓ² it does shrink** — 6.6% at ℓ = 3, 1.3% at ℓ = 7,
0.5% at ℓ = 12 — the same order as the eikonal error 3354 showed
cancels in Φ.

## §3 What is and is not concluded

- **3353's fence is now priced:** the s = 0 proxy under-shoots the
  gravitational eigenvalue by an O(1) constant ≈ 0.73 across the
  ladder, i.e. ~1.3% at ℓ_crit.
- **Whether that cancels in Φ, as the eikonal error did at 3354, is
  NOT asserted.** The s = −2 census is not a drop-in Q replacement:
  the s = −2 radial operator carries extra −2is(r−M)K/Δ + 4isωr terms.
  That belongs to rung 3b, the heavy build.
- **ℓ = 2 — the observable line — remains open in the angular sector**
  and needs a method change (endpoint regularisation), not a rerun.

## §4 Registry

- RCORE-3 "s = −2 angular": **discharged for ℓ ≥ 3 on the |m| = ℓ
  branch; ℓ = 2 open (method change).**
- **Remaining: rung 3b — the radial Kerr Teukolsky/Sasaki–Nakamura
  build — plus the ℓ = 2 angular regularisation.** Both need the
  higher tier; both start from validated instruments.


### 7.5 Patch 3358 record (as corrected in place by 3359)
# Rung 3b — Leaver Kerr validated against tables; the ℓ = 2 gravitational angular gap closed; and the first EXACT Kerr wall spectrum (scalar sector)

**Patch 3358, 30 Aug 2026 — Session 157, on Fable.** Verify:
`code/3358_kerr_wall_modes_verify.py`, **9/9 PASS**.

## §1 Part A — validation before anything new

Leaver's coupled Kerr continued fractions (angular + radial, s = −2),
both written from memory, against **tabulated** (2,2) Kerr QNMs:
a/M = 0, 0.5, 0.7, 0.9 all reproduced to ≤ 1.2e−4. That validates the
s = −2 angular sector for *all* (ℓ,m) — including ℓ = 2, which 3357 had
to exclude — because Leaver's series absorbs the pole exponent into its
prefactor. **The ℓ = 2 gap is closed:** A(2,−2; c = 0.2688) = 4.665 for
s = −2 (vs 5.989 scalar, 6.25 eikonal; the +0.68 beyond the −2 offset
matches the first-order +8c/(ℓ+1) = 0.72 prediction from 3357).

Cross-instrument: Leaver's s = 0 angular CF agrees with 3353's
finite-difference eigenvalue at real c to 1e−6.

## §2 Part B — the first exact Kerr wall resonances

Direct inward integration of the **scalar** Kerr radial Teukolsky
equation from a numerically-fitted outgoing series to the derived wall
(r_w = 2.2668 M), root-finding on R(r_w) = 0. Validation ladder,
asserted: (B1) at a = 0 it reproduces the Schwarzschild s = 0 wall mode
from the independent rung-2 code to five decimals (0.56473 − 0.13886i,
two codes, one number); (B2) root independent of r₀ = 30/40/50 to
2e−8; (B3) zero sharp (contrast 5e−8).

| mode | ω (M = 1) | f @ 62 M_⊙ | Q | eikonal top (3334/3354) | exact vs top |
|---|---|---|---|---|---|
| **(2,−2)** | **0.48085 − 0.11668i** | **250.6 Hz** | **2.06** | 0.3953 | **+21.6%** |
| (3,−3) | 0.62812 − 0.07843i | 327.4 Hz | 4.00 | 0.5528 | +13.6% |
| (2,+1) | ~~0.63877 − 0.30216i~~ **WITHDRAWN (Patch 3359)** | — | — | 0.5643 | — |

**CORRECTION (Patch 3359, anti-erasure):** the (2,+1) entry above is
**WITHDRAWN**. It never received the r₀-independence and sharpness
tests that (2,−2) did, and 3359 found that direct inward integration
cannot locate Q ~ 1 modes at all (|Im ω| ≈ 0.3 → e^27 instability
growth; the root-finder returns its own guess). The value was a
non-converged guess, not a root. Every claim below that leaned on
(2,+1) — the exact-grade ordering test B6 — is downgraded accordingly.
The (2,−2) and (3,−3) entries stand (both fully validated).

## §3 What this says about the shipped prediction

- **The retrograde-keyed (2,−2) line is a broad top-of-barrier
  feature — no trapped comb at ℓ = 2, now exactly.** Q ≈ 2, consistent
  with 3356's Q = 1.9 at χ = 0 and confirming that Leg A's Q ≈ 5 was
  the outlier.
- **The above-top shift is +21.6% at Kerr**, not the +15–17% of the
  χ = 0 anchor. The band CONV-034 withdrew (~247–344 Hz) sat close to
  the scalar-exact answer — it was withdrawn correctly anyway, because
  it was *unearned*; now the number is computed.
- ~~GR-2's retrograde-keyed ordering survives at exact grade~~ **WITHDRAWN
  (3359)**: the (2,+1) comparator was unvalidated; the ordering test
  remains at eikonal-WKB grade.
- **(3,−3) at Q = 4 is the sharpest line** — a spectroscopically
  better target than the dominant (2,−2), though weaker-excited.

## §4 Fence and what remains

Part B is **s = 0**. It is the exact version of the grade every lane
census has been at, not the gravitational spectrum. The s = −2 wall
requires the boundary condition on the Sasaki–Nakamura variable — **rung
3c, the last item**, and the one with the largest recall risk (SN's
functions must be validated by reducing to Regge–Wheeler at a = 0).

**PRED-O-39 / GR-2:** the orientation-scale tops now have exact
scalar-sector counterparts. Registered here; **not enacted** —
changing a flagship prediction's quoted frequencies warrants a panel
round (CONV-036) once s = −2 lands, since the gravitational numbers are
what the prediction is about.


### 7.6 Patch 3359 record
# Rung 3c — the gravitational (s = −2) Kerr wall spectrum: the last item, and it moves the flagship line

**Patch 3359, 30 Aug 2026 — Session 157, on Fable.** Verify:
`code/3359_sn_gravitational_wall_modes_verify.py`, **9/9 PASS**.

## §1 The recall risk, discharged by three tests before any Kerr number

The Sasaki–Nakamura functions (η, α, β, F, U with c₀…c₄) were written
from memory. A wrong term gives plausible wrong QNMs — the worst
failure mode — so three tests ran first:

- **T1:** at a = 0, U_SN + ω² = V_RW pointwise to 1.6e−9 and F ≡ 0 —
  the SN equation reduces exactly to Regge–Wheeler.
- **T2:** in Kerr, U → −ω² as 1/r — short-range, so X = 0 is a
  well-posed node condition.
- **T3 (decisive):** at a = 0 the SN wall instrument reproduces 3356's
  exact RW wall resonance from an independent code:
  0.44859 − 0.11749i, |Δ| = 2.7e−6.

## §2 The gravitational Kerr wall spectrum, χ = 0.68

| mode | ω (M = 1) | **f @ 62 M_⊙** | Q | contrast | r₀-spread |
|---|---|---|---|---|---|
| **(2,−2)** | **0.36694 − 0.08782i** | **191.2 Hz** | **2.09** | 6e−9 | 3e−9 |
| (3,−3) | 0.55333 − 0.06522i | 288.4 Hz | 4.24 | 4e−9 | 3e−10 |
| (2,+1) | **NOT LOCATED** | — | — | 0.75 | — |

Every reported root passed r₀-independence and sharpness
*individually*. The (2,+1) row is the method's limit (§4), not a
result.

## §3 What changed, and it is the flagship line

**The gravitational (2,−2) line is 191 Hz for GW150914** — below every
prior estimate: the eikonal top (211 Hz), the CONV-034-withdrawn +17%
transport (247 Hz), and the exact scalar line (251 Hz, 3358). The
gravitational lines sit **12–24% below** the scalar ones (ratios 0.763
and 0.881), and the a = 0 case already said so (RW/scalar = 0.794) —
the s = −2 effective potential is lower than the s = 0 one, so its
resonances sit lower. **3358's framing that the scalar sector was "the
exact version of the lane's grade" was right for STRUCTURE (no comb,
broad Q ≈ 2 at ℓ = 2) and wrong for POSITIONS.** Corrected here.

Notably, the withdrawn "+17% above the top" transport was **wrong in
sign** for gravitational waves: the (2,−2) line sits 7% *below* the
eikonal geodesic top. CONV-034's withdrawal was more right than anyone
knew.

**What survives at gravitational grade:** no trapped comb at ℓ = 2
(Q = 2.09, a single broad top-of-barrier feature); (3,−3) at Q = 4.2 is
the sharpest line; and 3352/3355's stability conclusions are untouched
(they depend only on R(r_w) < 0 in the superradiant window).

## §4 Method limit found, and a 3358 result withdrawn

Direct inward integration is validated for |Im ω| ≲ 0.12. At Q ≈ 1
(|Im ω| ≈ 0.3) the ingoing contamination grows ~e^27 across the range
and the root-finder cannot move — it returns its own guess with
contrast ≈ 1. **(2,+1) is therefore NOT LOCATED at s = −2.** And
**3358's scalar (2,+1) = 0.63877 − 0.30216i is WITHDRAWN**: it never
received the r₀/sharpness tests and was, on inspection, the same
failure. 3358's record is corrected in place. **Consequence: the
retrograde-keyed *ordering* test is NOT established at exact grade** in
either sector — the prograde-exposed comparator is unlocated — and
remains at eikonal-WKB grade. Very broad modes need a different
instrument (a Leaver-type series with the wall condition, or a
Riccati/contour formulation). Registered as open.

## §5 Registry

- **OPEN-GR-RCORE-3: all chartered items discharged**, at the grades
  stated: finite-ℓ (A/B/C), co-rotation (b), excitation (e),
  Zel'dovich (d), s = −2 angular (3a/3b), radial Kerr (3b/3c).
- **NEW OPEN: very-broad-mode instrument** (Q ≲ 1.5), needed for the
  prograde comparator and the exact-grade ordering test.
- **PRED-O-39 / GR-2 amendment now OWED, and it changes the flagship
  frequency: (2,−2) ≈ 191 Hz (gravitational, exact), Q ≈ 2.1; (3,−3)
  ≈ 288 Hz, Q ≈ 4.2.** This warrants a panel round (**CONV-036**)
  before enactment — a flagship prediction's quoted frequency moves.
- A1–A3 conditionality (OPEN-GR-RCORE-4) is inherited throughout.


### 7.7 The load-bearing script: 3359_sn_gravitational_wall_modes_verify.py
```python
#!/usr/bin/env python3
"""3359_sn_gravitational_wall_modes_verify.py — TEUKOLSKY LADDER RUNG 3c,
THE LAST ITEM: gravitational (s = -2) Kerr wall resonances via the
Sasaki-Nakamura (SN) transformation.

WHY SN. The Dirichlet wall condition of this lane is "clamped register =
node in the wave amplitude" (RCORE-1). For s = -2 the Teukolsky function
R is NOT that amplitude — it has r^3 asymptotics and a long-range
potential — so R = 0 at the wall is the wrong condition. The SN variable
X is the Kerr generalisation of the Regge-Wheeler function: short-range
potential, X ~ e^{+-i omega r*} asymptotics, and X = 0 is the natural
node condition that reduces to Leg A's psi = 0 at a = 0.

THE RECALL RISK, AND THE TESTS THAT DISCHARGE IT. The SN functions
(eta, alpha, beta, F, U with the c_0..c_4 coefficients) were written from
memory (Sasaki & Nakamura 1982; Mino et al. 1997). A wrong term would
give plausible-looking wrong QNMs — the worst failure mode. Three tests
run BEFORE any Kerr number is reported:
  T1  a = 0: U_SN + omega^2 must equal V_RW pointwise, and F must vanish
      (the SN equation is known to reduce to Regge-Wheeler at a = 0).
  T2  Kerr asymptotics: U -> -omega^2 as 1/r at large r (short-range).
  T3  a = 0 WALL MODE: the SN instrument must reproduce 3356's exact RW
      wall resonance 0.44859 - 0.11749i — a five-figure number from an
      independent code.
Then the standard direct-integration assertions (r0-independence,
sharpness) at Kerr, as in 3356/3358.

THE ANGULAR INPUT: lambda = A_{-2,lm}(a omega) + a^2 omega^2 - 2 a m omega,
with A from the Leaver s = -2 angular continued fraction validated at
3358 against tabulated Kerr QNMs (complex c handled natively).

Units M = 1 (Leaver internals 2M = 1); Hz at 62 Msun.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------------- angular: Leaver s=-2 CF (validated 3358) ----------------
def ang_cf(A, c, m, s, N=300):
    kp, km = abs(m + s) / 2, abs(m - s) / 2
    al = lambda n: -2 * (n + 1) * (n + 2 * km + 1)
    be = lambda n: (n * (n - 1) + 2 * n * (km + kp + 1 - 2 * c)
                    - (2 * c * (2 * km + s + 1) - (km + kp) * (km + kp + 1))
                    - (c * c + s * (s + 1) + A))
    ga = lambda n: 2 * c * (n + km + kp + s)
    x = 0j
    for n in range(N, 0, -1):
        x = -al(n - 1) * ga(n) / (be(n) + x)
    return be(0) + x


def A_leaver(c, ell, m, s=-2):
    g = ell * (ell + 1) - s * (s + 1) + 0j
    f = lambda v: [ang_cf(v[0] + 1j * v[1], c, m, s).real,
                   ang_cf(v[0] + 1j * v[1], c, m, s).imag]
    r = fsolve(f, [g.real, g.imag], xtol=1e-13)
    return r[0] + 1j * r[1]


# ---------------- Sasaki-Nakamura functions, s = -2 ----------------
def sn_FU(r, a, w, m, lam, M=1.0):
    D = r * r - 2 * M * r + a * a
    Dp = 2 * r - 2 * M
    K = (r * r + a * a) * w - a * m
    Kp = 2 * r * w
    c0 = -12j * w * M + lam * (lam + 2) - 12 * a * w * (a * w - m)
    c1 = 8j * a * (3 * a * w - lam * (a * w - m))
    c2 = -24j * a * M * (a * w - m) + 12 * a * a * (1 - 2 * (a * w - m) ** 2)
    c3 = 24j * a ** 3 * (a * w - m) - 24 * M * a * a
    c4 = 12 * a ** 4
    eta = c0 + c1 / r + c2 / r ** 2 + c3 / r ** 3 + c4 / r ** 4
    etap = -c1 / r ** 2 - 2 * c2 / r ** 3 - 3 * c3 / r ** 4 - 4 * c4 / r ** 5
    beta = 2 * D * (-1j * K + r - M - 2 * D / r)
    betap = (2 * Dp * (-1j * K + r - M - 2 * D / r)
             + 2 * D * (-1j * Kp + 1 - 2 * Dp / r + 2 * D / r ** 2))
    alpha = -1j * K * beta / D ** 2 + 3j * Kp + lam + 6 * D / r ** 2
    V = -(K * K + 4j * (r - M) * K) / D + 8j * w * r + lam

    def Aplus(rr):
        DD = rr * rr - 2 * M * rr + a * a; DDp = 2 * rr - 2 * M
        KK = (rr * rr + a * a) * w - a * m; KKp = 2 * rr * w
        bb = 2 * DD * (-1j * KK + rr - M - 2 * DD / rr)
        bbp = (2 * DDp * (-1j * KK + rr - M - 2 * DD / rr)
               + 2 * DD * (-1j * KKp + 1 - 2 * DDp / rr + 2 * DD / rr ** 2))
        aa = -1j * KK * bb / DD ** 2 + 3j * KKp + lam + 6 * DD / rr ** 2
        return 2 * aa + bbp / DD

    h = 1e-5 * r
    dA = (Aplus(r + h) - Aplus(r - h)) / (2 * h)
    U1 = V + (D * D / beta) * (dA - (etap / eta) * (alpha + betap / D))
    G = -2 * (r - M) / (r * r + a * a) + r * D / (r * r + a * a) ** 2
    Gp = ((-2 * (r * r + a * a) + 2 * (r - M) * 2 * r) / (r * r + a * a) ** 2
          + (D + r * Dp) / (r * r + a * a) ** 2 - 4 * r * r * D / (r * r + a * a) ** 3)
    F = etap * D / (eta * (r * r + a * a))
    U = D * U1 / (r * r + a * a) ** 2 + G * G + D * Gp / (r * r + a * a) - F * G
    return F, U


# ---------------- T1: a = 0 reduction to Regge-Wheeler ----------------
w_test = 0.44859 - 0.11749j
lam0 = 4.0 + 0j
V_RW = lambda r: (1 - 2 / r) * (6 / r ** 2 - 6 / r ** 3)
d1 = []
for r in (2.3, 3.0, 5.0, 10.0, 30.0):
    F, U = sn_FU(r, 0.0, w_test, -2, lam0)
    d1.append(max(abs(U + w_test * w_test - V_RW(r)), abs(F)))
check("T1. THE RECALL TEST: at a = 0 the Sasaki-Nakamura potential reduces "
      "EXACTLY to Regge-Wheeler (U_SN + omega^2 = V_RW pointwise, F = 0) — a "
      "wrong term anywhere in eta/alpha/beta/U would break this",
      max(d1) < 1e-8, f"max pointwise deviation {max(d1):.1e} over r = 2.3..30")

# ---------------- T2: Kerr short-range ----------------
a68 = 0.68
A22 = A_leaver(a68 * w_test, 2, -2)
lam22 = A22 + a68 * a68 * w_test * w_test - 2 * a68 * (-2) * w_test
dev = [abs(sn_FU(r, a68, w_test, -2, lam22)[1] + w_test * w_test) for r in (50.0, 200.0, 1000.0)]
check("T2. KERR ASYMPTOTICS: U -> -omega^2 at large r with 1/r falloff — the "
      "SN potential is short-range, so X ~ e^{+-i omega r*} and X = 0 is a "
      "well-posed node condition",
      dev[0] > dev[1] > dev[2] and dev[2] < 1e-5,
      f"|U + omega^2| at r = 50/200/1000: {dev[0]:.1e} / {dev[1]:.1e} / {dev[2]:.1e}")

# ---------------- the SN wall solver ----------------
def _AA(r, a, th):
    D = r * r - 2 * r + a * a
    return (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2


def F_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = _AA(r, a, th)
    al = np.sqrt(max(D * S / Aa, 0.0))
    s_ = 2 * (1 - al) / (1 + al)
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    v = om * np.sqrt(gpp / al2) if al2 > 0 else np.inf
    return s_ * s_ + v * v


def r_surface(a, th=np.pi / 2):
    if a == 0.0:
        return 2.25
    lo = (1 + np.sqrt(max(1 - a * a, 0.0))) * (1 + 1e-10); hi = 60.0
    for _ in range(220):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)


def rstar(r, a):
    if a == 0.0:
        return r + 2 * np.log(r / 2 - 1)
    rp = 1 + np.sqrt(1 - a * a); rm = 1 - np.sqrt(1 - a * a)
    return (r + (2 * rp / (rp - rm)) * np.log((r - rp) / 2)
            - (2 * rm / (rp - rm)) * np.log((r - rm) / 2))


def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):
    rw = r_surface(a)
    A = A_leaver(a * w, ell, m) if a != 0.0 else (ell * (ell + 1) - 2 + 0j)
    lam = A + a * a * w * w - 2 * a * m * w
    # SN equation in r: X'' - F X' - U X = 0 with ' = d/dr*, dr*/dr = (r^2+a^2)/Delta
    # asymptotic outgoing X ~ e^{i w r*} sum c_k r^-k, coefficients fitted numerically
    c = np.zeros(nterms, dtype=complex); c[0] = 1.0
    rs = np.linspace(r0, 4 * r0, 40)

    def pd(cc, r):
        D = r * r - 2 * r + a * a
        drs = (r * r + a * a) / D
        S = sum(cc[k] / r ** k for k in range(len(cc)))
        dS = sum(-k * cc[k] / r ** (k + 1) for k in range(len(cc)))
        d2S = sum(k * (k + 1) * cc[k] / r ** (k + 2) for k in range(len(cc)))
        e = np.exp(1j * w * rstar(r, a))
        X = e * S
        # d/dr* = (1/drs) d/dr
        dX_dr = e * (1j * w * drs * S + dS)
        Xp = dX_dr / drs                                    # dX/dr*
        ddrs = (2 * r * D - (r * r + a * a) * (2 * r - 2)) / D ** 2
        d2X_dr2 = e * ((1j * w * drs) ** 2 * S + 1j * w * ddrs * S
                       + 2 * 1j * w * drs * dS + d2S)
        Xpp = (d2X_dr2 - Xp * ddrs) / drs ** 2              # d^2X/dr*^2
        return X, Xp, Xpp

    def resid(cc):
        out = []
        for r in rs:
            F, U = sn_FU(r, a, w, m, lam)
            X, Xp, Xpp = pd(cc, r)
            out.append((Xpp - F * Xp - U * X) / np.exp(1j * w * rstar(r, a)))
        return np.array(out)

    Mx = np.zeros((len(rs), nterms - 1), dtype=complex); base = resid(c)
    for k in range(1, nterms):
        cc = c.copy(); cc[k] = 1.0
        Mx[:, k - 1] = resid(cc) - base
    c[1:] = np.linalg.lstsq(Mx, -base, rcond=None)[0]
    X0, Xp0, _ = pd(c, r0)

    # integrate in r* from r*(r0) down to r*(rw); carry r as a state too
    def rhs(t, y):
        r = y[4]
        D = r * r - 2 * r + a * a
        F, U = sn_FU(r, a, w, m, lam)
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]
        Xpp = F * Xp + U * X
        drdt = D / (r * r + a * a)
        return [Xp.real, Xp.imag, Xpp.real, Xpp.imag, drdt]

    t0, t1 = rstar(r0, a), rstar(rw, a)
    sol = solve_ivp(rhs, [t0, t1], [X0.real, X0.imag, Xp0.real, Xp0.imag, r0],
                    rtol=1e-11, atol=1e-13, method="DOP853")
    return sol.y[0, -1] + 1j * sol.y[1, -1]


def wall_root(a, ell, m, guess, r0=40.0):
    f = lambda v: [X_at_wall(v[0] + 1j * v[1], a, ell, m, r0).real,
                   X_at_wall(v[0] + 1j * v[1], a, ell, m, r0).imag]
    s = fsolve(f, [guess.real, guess.imag], xtol=1e-11)
    return s[0] + 1j * s[1]


# ---------------- T3: a = 0 wall mode reproduces 3356 ----------------
w0 = wall_root(0.0, 2, -2, 0.45 - 0.11j)
check("T3. THE DECISIVE TEST: at a = 0 the SN wall instrument reproduces "
      "3356's exact Regge-Wheeler wall resonance from an independent code",
      abs(w0 - (0.44859 - 0.11749j)) < 2e-4,
      f"SN(a=0) {w0:.5f} vs RW (3356) 0.44859-0.11749i, "
      f"|diff| = {abs(w0-(0.44859-0.11749j)):.1e}")

# ---------------- THE GRAVITATIONAL KERR WALL SPECTRUM ----------------
# Every reported root must pass BOTH instability tests individually; a
# root-finder that returns its own guess is recorded as NOT-LOCATED, not
# as a number. (First run: (2,+1) came back as exactly its guess and was
# nearly reported — the contrast test below is what catches that.)
def validated_root(ell, m, guess):
    w = wall_root(a68, ell, m, guess)
    on = abs(X_at_wall(w, a68, ell, m)); off = abs(X_at_wall(w + 0.02j, a68, ell, m))
    sp = max(abs(wall_root(a68, ell, m, w, r0) - w) for r0 in (30.0, 50.0))
    ok = (on / off < 1e-2) and (sp < 1e-4)
    return w, on / off, sp, ok

targets = [(2, -2, 0.47 - 0.11j), (3, -3, 0.62 - 0.08j), (2, 1, 0.62 - 0.25j)]
res, val = {}, {}
print(f"      chi = {a68}, wall r = {r_surface(a68):.4f} M — GRAVITATIONAL (s=-2) wall modes:")
for ell, m, g in targets:
    w, contrast, sp, ok = validated_root(ell, m, g)
    val[(ell, m)] = ok
    if ok:
        res[(ell, m)] = w
        print(f"        ({ell},{m:+d}): w = {w:.5f}  f = {to_hz(w.real):.1f} Hz @62  "
              f"Q = {w.real/(2*abs(w.imag)):.2f}   [contrast {contrast:.1e}, r0-spread {sp:.1e}]")
    else:
        print(f"        ({ell},{m:+d}): NOT LOCATED — root-finder returned {w:.3f} with "
              f"contrast {contrast:.1e} (a genuine zero has < 1e-2); see K6")

w22 = res[(2, -2)]
check("K1. EVERY REPORTED ROOT IS r0-INDEPENDENT (direct-integration "
      "instability test), individually, not just the first one",
      all(val[k] for k in res) and (2, -2) in res and (3, -3) in res,
      "; ".join(f"({k[0]},{k[1]:+d}) validated" for k in res))
check("K2. EVERY REPORTED ZERO IS SHARP, individually",
      all(val[k] for k in res), "contrast < 1e-2 for each reported mode")

# First run FAILED the hypothesis "scalar was a faithful proxy": the
# gravitational lines sit 12-24% BELOW the scalar ones. The failure is
# physics, not error, and it was already visible at a = 0 (RW 0.4486 vs
# scalar 0.5647, ratio 0.794): the s = -2 effective potential is lower
# than the s = 0 one, so its resonances sit lower. Recorded as a
# correction to 3358's framing, not smoothed into agreement.
SCALAR = {(2, -2): 0.48085 - 0.11668j, (3, -3): 0.62812 - 0.07843j}
ratios = {k: res[k].real / SCALAR[k].real for k in res if k in SCALAR}
check("K3. THE HYPOTHESIS FAILED AND IS CORRECTED: the gravitational lines "
      "sit 12-24% BELOW the scalar-sector lines (3358). The scalar census "
      "was a faithful proxy for STRUCTURE (no comb, broad ell=2, ordering) "
      "but NOT for line POSITIONS — and the a = 0 ratio (RW/scalar = 0.794) "
      "already said so",
      all(0.70 < r < 0.95 for r in ratios.values()),
      "; ".join(f"({k[0]},{k[1]:+d}): grav {res[k].real:.4f} / scalar "
                f"{SCALAR[k].real:.4f} = {r:.3f}" for k, r in ratios.items())
      + "; a=0 reference 0.794")

check("K4. NO TRAPPED COMB AT ell = 2 — NOW AT GRAVITATIONAL GRADE: the (2,-2) "
      "line is a single broad top-of-barrier resonance (Q of order 2), not a "
      "narrow trapped mode",
      res[(2, -2)].real / (2 * abs(res[(2, -2)].imag)) < 4,
      f"Q(2,-2) = {res[(2,-2)].real/(2*abs(res[(2,-2)].imag)):.2f}")

check("K5. THE DISCRIMINATOR'S ORDERING TEST IS *NOT* ESTABLISHED AT "
      "GRAVITATIONAL GRADE, and this check says so: the prograde-exposed "
      "comparator (2,+1) could not be located (K6), so the retrograde-keyed "
      "ordering remains at its previous grade (eikonal-WKB, and scalar-exact "
      "at 3358 — itself now withdrawn for (2,+1), see K6)",
      (2, 1) not in res,
      "(2,+1) NOT LOCATED; ordering stated only for what IS located: "
      f"(2,-2) {to_hz(res[(2,-2)].real):.0f} Hz < (3,-3) "
      f"{to_hz(res[(3,-3)].real):.0f} Hz (both retrograde — not the discriminator)")

check("K6. METHOD LIMIT FOUND AND A 3358 RESULT WITHDRAWN: direct inward "
      "integration is reliable for |Im omega| <~ 0.12 (validated) but at "
      "Q ~ 1 (|Im omega| ~ 0.3) the ingoing contamination grows ~e^27 over "
      "the range and the root-finder cannot move. (2,+1) is therefore "
      "NOT LOCATED here — and 3358's scalar (2,+1) = 0.63877-0.30216i, which "
      "never received the r0/sharpness tests, is WITHDRAWN as unvalidated",
      (2, 1) not in res,
      "very broad (Q ~ 1) modes need a different instrument (a series method "
      "or a contour/Riccati formulation); registered as open")

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
Q3: (i) <verdict>; (ii) <verdict>; (iii) <verdict> [<tier>] — <reasoning>
Q4: <verdict> — <reasoning>
Q5: <verdict> — <reasoning>
Q6: <verdict> — <reasoning>
Q7: <verdict> — <list or NONE-FOUND>
Q8a: <verdict>  Q8b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim count line(s) /
        INDEPENDENT-HARNESS + description / INSPECTED (reference run)>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```
