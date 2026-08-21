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

| χ | Φ/π at ℓ=2 | ℓ=6 | ℓ=7 | ℓ=10 | **ℓ_crit ± 1** |
|---|---|---|---|---|---|
| 0.00 | 0.180 | 0.467 | 0.539 | 0.755 | **10 ± 1** |
| 0.30 | 0.240 | 0.667 | 0.774 | 1.094 | **7 ± 1** |
| 0.68 | 0.246 | 0.734 | 0.856 | 1.222 | **7 ± 1** |
| 0.95 | 0.232 | 0.729 | 0.854 | 1.228 | **7 ± 1** |

**Trapped resonances — a comb — DO exist, for ℓ ≳ 7 ± 1.** The corpus
statements enacted from Leg B two patches ago ("the comb is NOT
restored, at χ = 0.68 or at ANY spin"; PRED-O-39's amended row; GR-2
V1.1's `rem:rcore3`) are **OVER-BROAD in ℓ** and are narrowed at
Patches 3339–3340. The correct statement:

> **No trapped comb exists in the observationally dominant low
> multipoles (ℓ = 2, 3 — N = 0 at every spin tested, checks 3);
> trapped ladders switch on at ℓ ≳ 7 ± 1 (ℓ ≈ 10 ± 1 at χ = 0),
> where ringdown excitation is negligible — that negligibility being
> INHERITED from standard ringdown phenomenology, OPEN-GR-RCORE-3(e),
> and NOT computed in this programme.**

## §2 THE OTHER HALF: this is also the consistency check neither Leg performed — and it VALIDATES the framework

The eikonal (geometric-optics) comb is the ℓ → ∞ limit. If the finite-ℓ
census had found N = 0 at *every* multipole, the two pictures would
have been irreconcilable and something would have been wrong. Instead
N_trapped grows monotonically and near-linearly over the COMPUTED
range ℓ = 2..10, **approached from below** — the unbounded-growth
statement being an asymptotic inference from that trend plus the
eikonal construction, not a computational finding (CONV-035 adopted): the
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
simultaneously EXPOSED, TRAPPED, and SUPERRADIANT. Over an EXHAUSTIVE,
explicitly declared domain — **165 modes = all (ℓ,m) with ℓ = 2..12 at
χ = 0.68** — **none exists.** (CONV-035 GPT defect 1, adopted and fixed
AT THE COMPUTATION: the first version of this check swept selected ℓ and
described its domain as "the whole (ℓ,m) grid" — the same quantifier
defect this record was written to diagnose, committed inside it. The
sweep is now complete over the declared range, and the mode count is
ASSERTED in the check itself so the claim cannot drift from its domain
again without failing.) Grade: **ESTABLISHED-OVER-A-DECLARED-EXHAUSTIVE-
DOMAIN, reconnaissance** — a *structural* exclusion requires the analytic
disjointness inequality (prove trapped ⇒ m ≤ −(ℓ−1) and
superradiance-capable ⇒ buried), registered as work. Every trapped mode is
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
