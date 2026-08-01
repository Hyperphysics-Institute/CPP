# EXECUTION RECORD — DIFFERENTIAL DRESSED DRIVE, ROUND 2 (ENSEMBLE)

**Patch 2906. Executed against the bands of
`mobile_sea_differential_amendment.md` (unchanged), under the amended
ensemble procedure of `mobile_sea_round2_amendment.md` (Patch 2905,
committed before execution). Kernel gate: PASS at 4.0×10⁻¹⁵ after the
gate CAUGHT an inverted bisection branch in the first kernel build —
see §4.**

# VERDICT: **INCONCLUSIVE** — Q_Δ fails at all three β. Third consecutive.

---

## §1 — RESULT (4-phase ensemble, pairwise mobile − frozen)

Data: `data/2906_round2_results.json`, raw legs `data/2906_raw_legs.json`,
driver `code/2906_ensemble_driver.py`.

| β | ΔD per phase (0 / 0.625 / 1.25 / 1.875) ×10⁻³ | ensemble ΔD | Q_Δ |
|---|---|---|---|
| 0 | +0.72 / +1.29 / −2.63 / −1.42 | **−0.51 ± 0.91 ×10⁻³** | (floor) |
| 0.05 | +2.68 / +0.38 / +1.10 / +0.80 | **+1.24 ± 0.50 ×10⁻³** | **FAIL** |
| 0.10 | +0.07 / +2.05 / +1.43 / −0.92 | **+0.66 ± 0.67 ×10⁻³** | **FAIL** |
| 0.20 | +1.47 / −1.53 / +3.15 / +1.93 | **+1.26 ± 0.99 ×10⁻³** | **FAIL** |

ΔF₀ = 5.12×10⁻⁴ ⟹ Q_Δ = 2.56×10⁻³; no ensemble mean reaches it.

**Recorded, flagged weightless for bands:** pooled over the 12 moving-β
differences: **+1.05 ± 0.40 ×10⁻³, 10 of 12 positive** (2.6σ, forward /
Condition-A direction) — across both rounds now 13 of 15 differential
values positive. Suggestive; not bankable; the next round exists to make
it bankable or kill it.

## §2 — WHY THE PROMISED POWER DID NOT MATERIALIZE (diagnosis with proof)

The 2904 §4 power arithmetic assumed the noise was statistical (ZBW
chatter, SE ∝ 1/√T). Round 2 shows the dominant noise is a
**phase-dependent SYSTEMATIC**, proven by the frozen legs themselves,
which carry no chatter at all: frozen β = 0 reads **6×10⁻¹⁸ at phase 0**
(the exactly symmetric position) but **−2.4×10⁻³ at phase 0.625** — a
pure **finite-domain asymmetry**: only phase 0 is a reflection-symmetric
position of the truncated grid; every off-symmetric source position sees
a statically asymmetric Sea at the 10⁻³ level. In the mobile legs this
asymmetry is *polarization-dressed* and does not cancel in mobile −
frozen. The 4-phase mean suppresses it incompletely. Additionally, a
charged source in a mobile dipole Sea has **no static equilibrium** —
polarized pairs feel a gradient force and slowly accrete — so legs are
weakly non-stationary within their windows.

**Consequence for the 2904 escalation clause:** its "third inconclusive
bounds the response below 1×10⁻³" was premised on SE ≈ 3.5×10⁻⁴, which
was not achieved. **The bound is NOT claimed.** What round 2 actually
establishes: the differential floor is systematics-limited at ~1×10⁻³
under this design, and the candidate response sits at the same ~1×10⁻³
scale.

## §3 — ROUND-3 DESIGN DIRECTION (named here; to be PRE-REGISTERED in its
own patch before any round-3 leg runs)

1. **Symmetric-class phases only:** the truncated grid admits exactly two
   reflection-symmetric source positions per period — on-site-plane
   (phase 0 with the committed grid) and mid-cell (a grid built at
   xs = ±1.25 + 2.5k, symmetric by construction). Both have *provably
   zero* static asymmetry; together they still sample the washboard at
   half-period.
2. **Seeded-jitter ensemble:** decorrelated ZBW phases via small seeded
   jitter of initial pair separations (physics unchanged at the declared
   level), giving a true 1/√K statistical ensemble; the engine is
   deterministic, so repetition without jitter adds nothing.
3. **Detrending:** fit-and-remove the slow accretion trend per leg
   before averaging.

## §4 — INFRASTRUCTURE NOTE

The compiled kernel's first build FAILED the frozen gate at 7.6×10⁻³ —
an **inverted bisection branch** (no retardation), which V1 alone could
not catch (static emitters are insensitive to retardation) but the
10-Moment dynamic comparison caught immediately. Corrected kernel:
agreement 4.0×10⁻¹⁵, V1/V2 identical, ~6× throughput. The gate earned
its existence on its first use.

## §5 — STANDING

CONJ-FP-1 Condition A remains OPEN; B CLOSED per 2895. Ledger untouched:
1B OPEN; PR7 PARTIAL; six of seven; B7 holds; Candidate (B) 79.5%. G1,
P-A2-1, statics suspension, 7 July ruling stand.
