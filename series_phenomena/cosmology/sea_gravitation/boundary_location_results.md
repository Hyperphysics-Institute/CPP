# THE BOUNDARY LOCATION PASS — LOCATED: d_s* = 4.25 ± 0.50 l_P (primary locator, the majority-switching crossing) — ABOVE the corridor; F-CLI-2-POINT: FIRES (shortfall ×1.35 in ρ), in the frozen words; the residual band [0.35, 0.79] GRAZES the band's lower edge; the two locators disagree by ~1.0 l_P and the disagreement is FLAGGED — the secondary (attainability) edge sits INSIDE the corridor; verdict at the primary per the frozen rule; the panel adjudicates the flag

**Patch 3114 (13 Aug 2026). Executes `boundary_location_prereg.md`
(Patch 3113) exactly. Verify: `scripts/3114_boundary_location.py`
(parts 1–3; imports the 3111 instrument verbatim). No rule below was
touched after the numbers existed.**

## §1 — The r(d_s) curve (mixed, σ_n = 0.30, seed-averaged)

| d_s | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 5.0 |
|---|---|---|---|---|---|---|---|
| r | 0.730 | 0.743 | 0.719 | 0.664 | 0.591 | 0.527 | 0.419 |
| phase | OTHER | OTHER | OTHER | OTHER | FAITHFUL | FAITHFUL | FAITHFUL |

Seed agreement excellent (≤ 0.005 everywhere). Sensitivity: halving
σ_n moves r by < 0.03 (2.5) and −0.025 (3.5) — the crossing is
noise-robust. Pure-e comparison: r lower by ~0.12 at 3.5 (the mixed
weave switches more — the q-overshoot physics), crossing shifted
low, consistent with the disclosed MB hint being the pure-e line's
crossing, not the physical weave's. The small non-monotonic dip
(2.0 → 2.5, −0.024) is within the declared 5% tolerance; the
location stands. Phases at d_s ≤ 3.0 are OTHER with stat ≈ 1.0 —
stationary but unbound-η: the high-switching (plasma-side) regime,
physically consistent with the boundary picture.

## §2 — The locators (frozen rules applied)

- **PRIMARY (majority-switching crossing r = 0.5): d_s* = 4.25 ±
  0.50 l_P** — the crossing falls between 4.0 and 5.0.
- **SECONDARY (FAITHFUL-attainability edge): 3.0–3.5** — FAITHFUL
  lost at every cell ≤ 3.0, held at 3.5.
- **Disagreement ≈ 1.0 l_P — AT the flag threshold: FLAGGED to the
  panel** as the prereg requires. Both are reported; the verdict
  runs at the primary, per the frozen rule. The panel receives the
  interpretive question explicitly: which locator embodies
  R-DS-BOUNDARY's "partner-switching gives way to monogamy" — the
  majority crossing (primary, as frozen) or the bound-phase edge
  (which sits INSIDE the corridor)? The worker does not relitigate
  this; the rule was frozen and the verdict follows it.

## §3 — F-CLI-2-POINT (fold verbatim; frozen words)

Central inputs (3111) at d_s* = 4.25: **central c_Li = 0.516;
residual band [0.350, 0.786]; band [0.6, 0.9].**

**VERDICT: the central point falls below the band. F-CLI-2-POINT:
FIRES (shortfall ×1.35 in ρ), in those words.**

Stated with both hands: this is the closest confrontation the arc
has produced — the residual band's upper reach (0.786) OVERLAPS the
band's lower portion — and the frozen rule is the central-value
rule, so it fires. No post-hoc widening; no locator switched after
the fact; the overlap is reported as a fact of the residual band,
not as a stay.

## §4 — The arc's three verdicts and the panel handoff

**F-CLI-1 FIRED (×2.2–62, inertial, 3107) → successor IN BAND
(BRACKETED) (3112) → F-CLI-2-POINT FIRED (shortfall ×1.35, 3114).**
Each honest iteration closed the gap by roughly an order of
magnitude; the arc ends this session ×1.35 short at the frozen rule,
with the residual band grazing the target. The panel round
(CONV-018) receives the complete 3097–3114 lineage with the named
residuals: the locator flag (§2), the C coherence fork (×1.27), the
arrangement estimator (pathological twice; upgrade specified), O-2
ratification, FQ-8.1–8.3 (still open), and small-array statistics.
No further assembly occurs without panel adjudication or new ruled
physics. Kila6 Route C and the DM ledger untouched; arrival still
trumps all.
