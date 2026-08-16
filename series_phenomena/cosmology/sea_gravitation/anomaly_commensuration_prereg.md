# THE ANOMALY MAP + A CANDIDATE ARTIFACT DIAGNOSIS, WITH ITS FALSIFIER FROZEN BEFORE THE RUN: the d_s = 2.0 feature sits exactly where TWO INDEPENDENT INSTRUMENT CONSTANTS COINCIDE — the bound/swap threshold (d_s/2) equals the Coulomb softening radius (r_soft = 1.0) at d_s = 2.0 and nowhere else; the fine grid shows sharp structure (Binder +0.30 at d_s = 1.9, sign-flipping to −0.24 at 2.0, f_b in a sharp V-minimum at ≈ 2.0), and the commensuration test predicts, IN ADVANCE: if artifact, the whole feature MOVES to d_s = 2·r_soft; if physics, it STAYS at 2.0

**Patch 3152 (15 Aug 2026). Executes the panel-mandated anomaly map
(CONV-021 Q5) and freezes the follow-up test's prediction before the
follow-up runs. Instrument parameterized (`r_soft`); DEFAULT 1.0
retained and **bit-identity of all prior results regression-verified**.**

## §1 — The anomaly map (n = 8 and n = 9, fine grid, both seeds)

| d_s | f_b (n=8) | U (n=8) | f_b (n=9) | U (n=9) |
|---|---|---|---|---|
| 1.75 | 0.2035 | +0.083 | 0.2022 | +0.117 |
| 1.90 | 0.1789 | **+0.323** | 0.1787 | **+0.283** |
| 2.00 | 0.1560 | (not measured) | 0.1515 | −0.038 |
| 2.10 | 0.1592 | −0.052 | 0.1521 | −0.004 |
| 2.25 | 0.2151 | +0.019 | 0.2066 | −0.018 |

Two features, both seed-consistent: a **sharp positive Binder peak at
d_s = 1.90** (+0.28 to +0.32, stable across sizes) and a **sign
reversal to strongly negative at 2.00** (−0.24 at n = 10, growing
with size), with f_b in a narrow V-minimum at ≈ 2.0–2.1. This is
real, localized, reproducible structure — the question is what
produces it.

## §2 — The candidate diagnosis: an exact coincidence of instrument constants

The instrument contains two independent constants: the bound-state /
poach threshold at **d_s/2**, and the Coulomb softening radius at
**r_soft = 1.0** (forces use max(r, 1)). **At d_s = 2.0 — and at no
other spacing on the grid — these coincide exactly:
d_s/2 = 1.0 = r_soft.** At that spacing the definition of "bound"
lands precisely on the radius where the force law changes character.
That is the kind of coincidence that manufactures anomalies, and it
explains a puzzle: the feature deepens with system size because
larger arrays sample the coincidence more heavily, not because a
correlation length is growing.

**This diagnosis directly threatens the 3151 §4 hypothesis** (that
the true critical point sits at 2.0). Recorded plainly: the worker
advanced that hypothesis one patch ago and is now supplying the
argument against it.

## §3 — THE FALSIFIER, FROZEN BEFORE THE RUN

Vary r_soft; the feature must follow whichever thing owns it.
- **If ARTIFACT (commensuration):** the feature moves to
  d_s = 2·r_soft — to **1.5** at r_soft = 0.75, to **2.5** at
  r_soft = 1.25.
- **If PHYSICS (spacing-intrinsic):** the feature stays at **2.0**
  under both variants.
Cells: n = 7, d_s ∈ {1.4, 1.5, 1.6, 1.9, 2.0, 2.1, 2.4, 2.5, 2.6},
r_soft ∈ {0.75, 1.25}, both seeds (36 cells,
`scripts/3152_commensuration_test.py`).
**FROZEN VERDICT RULE:** feature location (f_b minimum) within ±0.15
of 2·r_soft in BOTH variants ⇒ **ARTIFACT-CONFIRMED**; within ±0.15
of 2.0 in both ⇒ **PHYSICS-CONFIRMED**; otherwise ⇒ **AMBIGUOUS →
panel**.

## §4 — Consequences either way

**If ARTIFACT:** the 3151 collapse confounding (d_c 2.675 → 1.810)
is instrument-induced, the 2.0 dip drops out of the physics, the
"critical signature at 2.0" hypothesis is withdrawn — and the
peak-locator results across eight sizes become CLEANER, since the
confounding region was never physical. The frozen d_s* = 2.450
and the challenge are unaffected in status but better understood.
**If PHYSICS:** the corpus has a second, sharper transition at
d_s ≈ 2.0 that the whole campaign has been treating as noise, and
the CC lane's boundary story needs rebuilding around it.
Either outcome is worth the two hours. Frozen 2.450 unrevised;
calibration untouched. Kila6 untouched; arrival still trumps all.
