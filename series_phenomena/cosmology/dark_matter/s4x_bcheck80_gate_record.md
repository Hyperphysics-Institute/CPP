# S4-X B-CHECK-80 GATE RECORD (DRIVE-AUDIT-1, fourth act, part 1) — executed under the frozen 2753 prereg: **GATE FAIL — BLOCKING, as frozen** — and the failure is the discovery: the Hamiltonian-identity gate localized, to machine precision and BEFORE any production sweep, a **concrete line-level defect in the campaign's A path** — every proposed Metropolis move's ΔE carries a spurious positive self-pair term g(|δ|) = Q²·f(|old−new|) ∈ ~2–28 MeV (move-size dependent, comparable to Θ ≈ 35 MeV), because the new-position pair sum `d_n = pos − newp` retains the moved particle at its OLD position and the `>1e-12` mask does not exclude it — **the defect entered at Patch 2714 (S4-E Ewald rewrite; the 2709 S4-N code is CLEAN, it zeroed `en[i]` explicitly) and is inherited verbatim by 2737, 2740 (X3-LONG — the chains that produced the original B2 anomaly), 2743, 2746 run_A, and 2749 (X7-NSCAN + EXT)** — production is NOT run under the 2753 charter; an amended frozen prereg (B-CHECK-80B) re-charters the discriminant with a corrected gate plus an A-FIX pair, so one act now tests whether the named defect IS the anomaly's mechanism

**Patch 2754, 22 July 2026. Gate consumed no pool seed (seed 1, five
trial moves, no observable read). Frozen seed 20260795 remains
unconsumed. Diagnosis reproduced by `code/2754_gate_diagnosis.py`.
Reasoning: `reasoning/2754.md`. 79.5% not in scope.**

## §1 — Gate execution (frozen protocol, §3 of the 2753 prereg)

Five seed-1 trial moves at N = 80: |ΔE_B − dE_A| relative
discrepancies 8.4×10⁻² to 3.8×10⁰ — **FAIL on all five** (threshold
10⁻⁸). Per the frozen prereg, FAIL blocks the production run and the
session reports the defect instead. It does.

## §2 — Localization (machine precision)

For every gate move, dE_A − dE_B equals EXACTLY (residuals ≤ 3×10⁻¹⁴)
the pair term

  g(|δ|) = Q² Z_i² [ erfc(α|δ|)/|δ| − 1/|δ| + 1/√(|δ|² + a_s²) ],

the masked-erfc + softcore interaction of the moved particle's NEW
position with its own OLD position. Mechanism: in run_A's increment,
`d_n = pos − newp` is evaluated while `pos[i]` still holds the old
position; `d_n[i] = pos[i] − newp` is a small NONZERO vector, and the
mask `(rn < RC) & (rn > 1e-12)` — which correctly removes the exact
zero in `d_o[i]` — passes it. Every proposed move is therefore
penalized by g(|δ|) > 0: ≈ 28 MeV as |δ| → 0, ≈ 2 MeV at |δ| ≈ 0.18,
against Θ ≈ 35.2 MeV. A displacement-dependent penalty entering the
acceptance exponent identically for forward and reverse proposals
breaks detailed balance with respect to exp(−H/Θ): in the regime
|ΔH| < g the acceptance ratio squares the Boltzmann factor. The
stationary law of every affected chain is NOT the Gibbs law of its
Hamiltonian — driven or undriven alike, by an amount the ensemble
comparisons themselves must quantify.

## §3 — Reach survey (code-level facts only; no reclassification here)

- **CLEAN:** `2709_alpha1_s4n_simulation.py` — `eo[i]=0; en[i]=0`
  explicit. The S4-N act is unexposed to THIS defect.
- **DEFECT ENTERS:** `2714_alpha1_s4e_ewald.py` — the rewrite replaced
  the explicit zeroing with the 1e-12 mask. Regression, classic form:
  a guard correct for the old-position sum silently insufficient for
  the new-position sum.
- **INHERITED VERBATIM:** `2737` (X5 external field), `2740` (X3-LONG
  — the N = 432/686 chains where the B2 anomaly was first read),
  `2743` (X5-LIN), `2746` run_A (the X5-FE A-path anchors), `2749`
  (X7-NSCAN + EXT, all twelve series).
- Full repo-wide reach audit (earlier campaign code, any consumer of
  these ensembles' observables, exposure of the standing fluctuation-
  spectrum and shape findings) is chartered as follow-up, NOT enacted
  in this record. The economy rule holds: everything bundles to the
  panel after the audit resolves.

## §4 — What the gate result does and does not establish

1. It **does** hand candidate (a) — "numerical pathology in the
   incremental path" — a concrete named mechanism for the first time,
   present in the exact lines that produced the anomaly.
2. It does **not** yet establish that the defect IS the mechanism of
   the B2 enhancement: the penalty acts on driven and undriven chains
   alike; its net effect on the driven-mean/tilt ratio and its
   N-dependence are empirical questions. The X5-FE N = 64 agreement
   of defective-A with correct-B (0.3–1.1σ) proves the defect's
   observable-level effect can be small; whether it turns ON across
   (64, 80] is exactly what the amended act measures.
3. F3's mechanism sentence ("no line-level defect of the wrong-formula
   kind exists") is **impeached as stated** — a line-level defect
   exists; F3's numerical content (three-ensemble agreement at N = 64)
   stands as measured. Corrections-ledger entry queued.
4. Byproduct: the 2753 §5.1 committed-2746 prefactor question is
   RESOLVED — with the FULL prefactor, B's k-space increment matches
   A's to 10⁻¹⁴; A's convention is full PREF, and the archived B file's
   half-prefactor line is confirmed as a stale pre-fix snapshot
   (capture defect, ledger entry stands).

## §5 — Disposition

Production under the 2753 charter: **BLOCKED, as frozen.** The
discriminant re-charters immediately as **B-CHECK-80B**
(`s4x_bcheck80b_prereg.md`, Patch 2755): corrected blocking gate
(B totals vs A-FIX increments), an A-FIX pair at N = 80 (one-line
fix: `mn[i] = False`; fresh frozen seeds 20260796/97) giving the
CLEAN tilt and clean driven mean cheaply, plus the B production run
(seed 20260795, unconsumed) — one frozen J-fork then adjudicates
defect-is-mechanism vs enhancement-survives-the-fix vs residual
disagreement. Benchmark disclosed: 0.215 s/sweep for B in this
container (seed 1, 3 sweeps, discarded) → ≈ 0.78 h.
