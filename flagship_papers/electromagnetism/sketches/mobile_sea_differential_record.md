# EXECUTION RECORD — DIFFERENTIAL DRESSED DRIVE (ROUND 1) + ROUND-2 PRE-REGISTRATION

**Patch 2904. Executed against the frozen bands of
`mobile_sea_differential_amendment.md` (Patch 2903), committed before any
differential number existed.**

# VERDICT: **INCONCLUSIVE** — Q_Δ fails at two of three β.

**Second consecutive inconclusive round. The worker's declared
expectation (CANCELLATION) has now twice received no support; neither has
any other outcome.**

---

## §1 — RESULT

Checkpointed paired legs (driver `code/2904_differential_driver.py`;
raw legs `data/2904_raw_legs.json`; summary
`data/2904_differential_results.json`). Windows grid-matched per the
amendment (100/100/75/63 Moments for β = 0/0.05/0.10/0.20), T_eq = 40.

**Floor:** mobile β = 0 gives +4.107×10⁻⁴; frozen β = 0 gives
**+1.7×10⁻¹⁷ — machine zero** (the symmetric grid is exactly symmetric
and the frozen leg is chatter-free, validating both the 2903 defect fix
and the common-mode design). ΔF₀ = 4.107×10⁻⁴; **Q_Δ = 2.054×10⁻³**.

| β | D_mobile | D_frozen | **ΔD** | Q_Δ | ΔD/β |
|---|---|---|---|---|---|
| 0.05 | +1.366×10⁻³ | −0.245×10⁻³ | **+1.611×10⁻³** | **FAIL** | +0.0322 |
| 0.10 | +2.147×10⁻³ | −0.538×10⁻³ | **+2.685×10⁻³** | pass | +0.0268 |
| 0.20 | −1.524×10⁻³ | −1.534×10⁻³ | **+0.010×10⁻³** | **FAIL** | +0.00005 |

## §2 — WHAT IS AND IS NOT LICENSED

**Not licensed:** any band. Q_Δ fails at 0.05 and 0.20; the frozen
criterion says INCONCLUSIVE, and it is so recorded.

**Recorded, flagged weightless, for the next round to test rather than
believe:**

1. **ΔD is positive at all three β** — a uniformly forward (repulsive)
   response, the Condition-A-HOLDS direction — but two of the three
   points sit below the floor criterion, so the uniformity cannot be
   banked.
2. **At β = 0.20 the two legs agree to 1×10⁻⁵** while both read
   −1.5×10⁻³: the common-mode subtraction is working exactly as designed
   (the shared transit-lock artifact cancels to 0.6%), and the *response*
   there is consistent with zero.
3. The apparent shape — response ~2×10⁻³ at low β, collapsing toward
   zero by β = 0.2 — is not monotone in β and matches no band; with
   per-leg standard errors ~1×10⁻³ it is equally consistent with a small
   positive response plus noise. **This is precisely the ambiguity
   statistical power exists to resolve.**

## §3 — DIAGNOSIS: CHATTER-LIMITED, WITH THE POWER ARITHMETIC EXPLICIT

The frozen legs (chatter-free) have per-Moment scatter 1.7–2.1×10⁻³; the
mobile legs 6–8×10⁻³, dominated by ZBW chatter of the ~10⁴ nearest-pair
oscillations. At 60–100-Moment windows this puts every leg's standard
error near 1×10⁻³ — the same size as the candidate signal. Windows must
grow ~4× for a 3–6σ resolution of a 2×10⁻³ signal.

## §4 — ROUND-2 PRE-REGISTRATION (frozen here, before execution)

**Same observable, same bands, same procedure** as the amendment —
nothing about the criteria moves. Only statistical power changes:

- Windows ×4, still integer multiples of the grid period 2.5/β:
  **β = 0 → 400; β = 0.05 → 400 (k = 8); β = 0.10 → 300 (k = 12);
  β = 0.20 → 250 (k = 20).** T_eq = 40 unchanged.
- ΔF₀ and Q_Δ re-measured at the 400-Moment floor pair (same-window
  comparison, per the 2902 lesson).
- Execution checkpointed across turns; partial results reported as
  partial; **bands untouched regardless of outcome; a banded outcome
  remains provisional pending the original §5 convergence variations.**
- Power estimate, recorded in advance: SE_leg ≈ 3.5×10⁻⁴ at these
  windows; a real 2×10⁻³ response resolves at ~5σ; expected
  Q_Δ ≈ 1.2×10⁻³ < the candidate signal. **If the response is real and
  of the size round 1 hints at, round 2 is powered to band it; if round
  2 is inconclusive again, the signal is smaller than 1×10⁻³ in these
  units and the next escalation is a denser Sea, pre-registered in
  turn.**

**Worker expectation, declared a third time: CANCELLATION** (which, note,
predicts a *nonzero, linear, forward* ΔD — cancellation of curvature is
not cancellation of the drive; a ΔD consistent with zero at all β would
support neither CANCELLATION nor RETAINED and would instead reopen the
LW-like-dressing worry of the 2899 escalation note).

## §5 — STANDING

CONJ-FP-1 Conditions and LINKs unchanged (A OPEN, B CLOSED per 2895).
Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate
(B) 79.5%. G1, P-A2-1, statics suspension, 7 July ruling all stand.
