# EXECUTION RECORD — PROMOTION VARIATION (1.3× DOMAIN) + EXTENSION PREREG

**Patch 2911. Executed against the frozen §4 of
`mobile_sea_sign_round_record.md` (Patch 2910, applied before
execution).**

# VERDICT: **NOT PROMOTED — HOLDS REMAINS PROVISIONAL.** M/SE = 1.95
# against a frozen threshold of 2.0. The line is the line.

---

## §1 — RESULT (ρ_max 10.4, x_half 19.5, seed 1, classes A/B)

Data: `data/2911_variation_results.json`, raw legs
`data/2911_raw_legs.json`, driver `code/2911_promotion_variation.py`.

Floor: ΔD(0) legs −0.66/+0.42 ×10⁻³, mean −0.12 ± 0.54 ×10⁻³ —
within 2σ of zero ✓.

| β | class | Δ ×10⁻³ |
|---|---|---|
| 0.05 | A / B | −0.81 / +1.20 |
| 0.10 | A / B | +1.39 / −0.09 |
| 0.20 | A / B | +3.91 / +2.73 |

> **M_var = +1.388×10⁻³, SE_var = 0.712×10⁻³, M/SE = 1.95 (4/6
> positive).** Frozen criteria: M > 0 ✓; floor ✓; **M ≥ 2·SE ✗ (1.95).**
> Not PROMOTE. Not REVOKE (requires negative at ≥2σ; this is positive).
> ⟹ frozen else-clause applies: **remains provisional; larger variation
> ensemble pre-registered below.**

**Recorded plainly:** 1.95 vs 2.00 is the strongest promotion temptation
this arc has produced, and it is refused. The variation is fully
*consistent* with the main result (+1.39 vs +1.62 ×10⁻³; sign stable
under the domain change; the shortfall is pure ensemble size, 6 vs 18
values) — consistency is encouragement, not a verdict.

## §2 — EXTENSION PREREG (frozen here, before execution)

Seeds {2, 3} × classes {A, B} × β {0.05, 0.10, 0.20}, paired legs, at
the SAME 1.3× domain, procedure identical; plus mobile floor legs seeds
{2, 3} × classes. **Frozen criterion, on the POOLED 18 variation values
(this patch's 6 + the new 12): PROMOTE iff M_pool > 0 and
M_pool ≥ 2·SE_pool and pooled floor within 2σ of 0; REVOKE iff
M_pool < 0 at ≥2σ; else provisional continues and the variation
programme escalates to a pre-registered 1.6× domain.** Expected power:
SE_pool ≈ 0.41×10⁻³; a stable +1.4×10⁻³ resolves at ~3.4σ.

## §3 — STANDING

CONJ-FP-1: A HOLDS (provisional — unchanged); B CLOSED. Curvature owned
by the hybrid pipeline. Ledger untouched: 1B OPEN; PR7 PARTIAL; six of
seven; B7 holds; Candidate (B) 79.5%. G1, P-A2-1, statics suspension,
7 July ruling stand.
