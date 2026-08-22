# CHARTER — **TRANSFER-1: MEASURE THE RESPONSE MAP IN THE CAMPAIGN'S OWN GEOMETRY**, the one remaining move that can decide the DM comparison — and the move 3189's diagnostic identified by ELIMINATING the expensive alternative

**Patch 3190 (22 Aug 2026). Chartered, NOT launched: step 1 is a
single timing leg, and the founder's go/no-go follows the measured
cost rather than an estimate.**

## §1 — Why this and not the other campaign

3188 §4.1 prescribed re-running the 2914 symmetric-Sea legs to shrink
the archive's statistical error. **3189's sensitivity diagnostic
retired that prescription**: at β = 0.20 the arm sits 5.1σ of that
error above the band, so sharpening it changes nothing.

What the diagnostic did NOT retire is the **transfer assumption**
(3187 §2): the a1 response profile was MEASURED in the symmetric Sea
and APPLIED to the jittered one. Every comparator in 3188 rests on it,
and it is untested. **It is also the only remaining uncertainty that
could move the β = 0.20 reading**, since a genuinely different
response profile in the campaign geometry could shift F_JIT by any
factor at all.

**Also retired here, explicitly: the class-resolved comparator**
(F_MAP^A, F_MAP^B) proposed at 3186 §3. It refines the SYMMETRIC-Sea
comparator, and the arms do not use that geometry — so it cannot
inform the arm comparison. Recorded so the idea is not picked up
later as though it were still live.

## §2 — What TRANSFER-1 measures

2914-style instrumented legs run on `build_sea_jittered` at the
campaign's own constants (RHO = (1,8), SPACING = 2.5, X_HALF = 28,
JIT ± 0.05, source from X_SRC0 = −24), producing **that geometry's
OWN a1 map** in the same co-moving bins. Then F is recomputed from the
native map, and the comparison becomes assumption-free in the one
place it currently is not.

**Bin coverage note, already visible:** only 252 of 828 pairs fall
inside the archive's ±12 ξ-window. The native map should be binned
over the campaign's actual ξ range, which also removes the
zero-increment approximation 3188 was forced into for 70% of pairs.

## §3 — STEP 1 IS A TIMING LEG (no commitment)

Before any campaign is chartered, **one leg** is run and timed on
VideoCPU: one β, one seed, T_EQ = 40 plus a short T_meas, on the
jittered geometry with the 2914 instrumentation. Deliverables:
wall-time per leg, memory, and a verified-nonzero response signal.
**Only then** is a leg count chosen and a prereg frozen — statistic,
floors, and readings written before any physics leg runs, per §9.

**If the timing leg shows the campaign costs more than the β-ladder,
TRANSFER-1 is not chartered** and the comparison stays where 3188
left it, with the held CONV-023 question the only live path.

## §4 — Fence

Nothing here re-reads existing data (that is the held question's
subject and stays frozen). No Kila6 time. DISP-I3 un-re-adjudicated,
COEFFICIENT-OVERPREDICTED suspended, ledger untouched. **This charter
commits to a measurement of cost, not to a campaign.**
