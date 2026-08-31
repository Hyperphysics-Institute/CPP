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
